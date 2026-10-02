from pathlib import Path

from PIL import Image

from social_creative_generator import render_social_card


def test_render_social_card_writes_requested_square_png(tmp_path: Path) -> None:
    background = tmp_path / "background.png"
    logo = tmp_path / "logo.png"
    output = tmp_path / "card.png"

    Image.new("RGB", (400, 220), (25, 35, 45)).save(background)
    Image.new("RGBA", (80, 80), (255, 255, 255, 255)).save(logo)

    result = render_social_card(
        output_path=output,
        background_path=background,
        logo_path=logo,
        headline="A useful headline",
        supporting="A short explanation.",
        cta="Read the breakdown",
        size=(320, 320),
    )

    assert result == output
    assert output.exists()
    with Image.open(output) as image:
        assert image.size == (320, 320)
        assert image.mode == "RGB"
