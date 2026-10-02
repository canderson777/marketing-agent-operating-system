"""Render review-only branded social cards from existing local assets.

This is intentionally a small, deterministic renderer. It does not publish,
call an image API, or alter source repositories.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont


_FONT_CANDIDATES = {
    "regular": (
        Path("C:/Windows/Fonts/arial.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"),
    ),
    "bold": (
        Path("C:/Windows/Fonts/arialbd.ttf"),
        Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
    ),
}


def _font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in _FONT_CANDIDATES["bold" if bold else "regular"]:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def _cover_crop(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    """Resize an image to cover a canvas, cropping the excess."""
    target_width, target_height = size
    source_width, source_height = image.size
    scale = max(target_width / source_width, target_height / source_height)
    resized = image.resize(
        (round(source_width * scale), round(source_height * scale)),
        Image.Resampling.LANCZOS,
    )
    left = (resized.width - target_width) // 2
    top = (resized.height - target_height) // 2
    return resized.crop((left, top, left + target_width, top + target_height))


def _wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
    """Wrap text by rendered width while preserving explicit line breaks."""
    lines: list[str] = []
    for paragraph in text.splitlines() or [""]:
        words = paragraph.split()
        if not words:
            lines.append("")
            continue
        current = words[0]
        for word in words[1:]:
            candidate = f"{current} {word}"
            if draw.textlength(candidate, font=font) <= max_width:
                current = candidate
            else:
                lines.append(current)
                current = word
        lines.append(current)
    return lines


def _fit_font(
    draw: ImageDraw.ImageDraw,
    text: str,
    max_width: int,
    start_size: int,
    min_size: int,
    bold: bool = False,
) -> tuple[ImageFont.ImageFont, list[str]]:
    for size in range(start_size, min_size - 1, -2):
        font = _font(size, bold=bold)
        lines = _wrap_text(draw, text, font, max_width)
        if len(lines) <= 4:
            return font, lines
    font = _font(min_size, bold=bold)
    return font, _wrap_text(draw, text, font, max_width)


def _line_height(draw: ImageDraw.ImageDraw, font: ImageFont.ImageFont) -> int:
    box = draw.textbbox((0, 0), "Ag", font=font)
    return max(1, box[3] - box[1])


def _draw_lines(
    draw: ImageDraw.ImageDraw,
    lines: Iterable[str],
    xy: tuple[int, int],
    font: ImageFont.ImageFont,
    fill: tuple[int, int, int, int] | tuple[int, int, int],
    spacing: int,
) -> int:
    x, y = xy
    height = _line_height(draw, font)
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += height + spacing
    return y


def render_social_card(
    output_path: str | Path,
    background_path: str | Path,
    logo_path: str | Path,
    headline: str,
    supporting: str,
    cta: str,
    size: tuple[int, int] = (1080, 1080),
    eyebrow: str | None = None,
) -> Path:
    """Create a branded square social card and return its output path."""
    output = Path(output_path)
    canvas_size = (int(size[0]), int(size[1]))

    with Image.open(background_path) as source:
        canvas = _cover_crop(source.convert("RGB"), canvas_size).convert("RGBA")
    with Image.open(logo_path) as source_logo:
        logo = source_logo.convert("RGBA")

    width, height = canvas_size
    overlay = Image.new("RGBA", canvas_size, (5, 12, 20, 142))
    canvas = Image.alpha_composite(canvas, overlay)
    draw = ImageDraw.Draw(canvas, "RGBA")
    margin = round(width * 0.075)

    # A darker lower panel keeps copy readable over any imported source image.
    panel_top = round(height * 0.39)
    draw.rectangle((0, panel_top, width, height), fill=(3, 10, 17, 155))

    logo.thumbnail((round(width * 0.22), round(height * 0.18)), Image.Resampling.LANCZOS)
    canvas.alpha_composite(logo, (margin, margin))

    text_width = width - (margin * 2)
    y = round(height * 0.49)
    if eyebrow:
        eyebrow_font = _font(round(width * 0.027), bold=True)
        draw.text((margin, y), eyebrow.upper(), font=eyebrow_font, fill=(125, 220, 205, 255))
        y += round(height * 0.055)

    headline_font, headline_lines = _fit_font(
        draw,
        headline,
        text_width,
        start_size=round(width * 0.082),
        min_size=round(width * 0.045),
        bold=True,
    )
    y = _draw_lines(draw, headline_lines, (margin, y), headline_font, (255, 255, 255, 255), round(height * 0.012))
    y += round(height * 0.025)

    supporting_font, supporting_lines = _fit_font(
        draw,
        supporting,
        text_width,
        start_size=round(width * 0.035),
        min_size=round(width * 0.022),
    )
    _draw_lines(draw, supporting_lines, (margin, y), supporting_font, (232, 240, 244, 255), round(height * 0.008))

    cta_font = _font(round(width * 0.027), bold=True)
    cta_box = draw.textbbox((0, 0), cta, font=cta_font)
    cta_width = (cta_box[2] - cta_box[0]) + round(width * 0.055)
    cta_height = (cta_box[3] - cta_box[1]) + round(height * 0.035)
    cta_left = margin
    cta_top = height - margin - cta_height
    draw.rounded_rectangle(
        (cta_left, cta_top, cta_left + cta_width, cta_top + cta_height),
        radius=round(cta_height * 0.28),
        fill=(255, 255, 255, 245),
    )
    draw.text(
        (cta_left + round(width * 0.027), cta_top + round(height * 0.017)),
        cta,
        font=cta_font,
        fill=(7, 24, 35, 255),
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(output, format="PNG", optimize=True)
    return output


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--background", required=True, type=Path)
    parser.add_argument("--logo", required=True, type=Path)
    parser.add_argument("--headline", required=True)
    parser.add_argument("--supporting", required=True)
    parser.add_argument("--cta", required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--eyebrow")
    parser.add_argument("--size", type=int, default=1080)
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    render_social_card(
        output_path=args.output,
        background_path=args.background,
        logo_path=args.logo,
        headline=args.headline,
        supporting=args.supporting,
        cta=args.cta,
        size=(args.size, args.size),
        eyebrow=args.eyebrow,
    )


if __name__ == "__main__":
    main()
