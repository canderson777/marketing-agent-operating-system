# Run Marketing Request

Use this as the default orchestration workflow when the operator gives a mixed or messy request.

## Purpose
Turn one marketing request into a scoped plan, the right agent assignments, and a packaged deliverable.

## Inputs
- `../shared/request-template.md` or a messy natural-language request
- `../master-agent.md`
- the relevant brand folder under `../../brands/`
- `../shared/client-profile-template.md` when brand context is still thin
- `../shared/campaign-brief-template.md` when execution needs tighter scoping

## Steps
1. Identify the brand, offer, goal, CTA, and channel.
2. Pull existing context from the matching brand folder before asking for more.
3. Label missing high-impact assumptions.
4. Decide whether this is strategy, execution, or review.
5. Choose the smallest workflow that can ship.
6. Assign only the agents needed.
7. Return one packaged output with next actions.

## Default Routing
- Unclear request -> `strategy-diagnostic-workflow.md`
- Content production request -> `weekly-content-engine.md`
- Offer or launch request -> `campaign-launch.md` or `product-launch.md`
- Lead request -> `lead-generation.md`
- Performance review request -> `reporting-review.md`

## Guardrails
- Do not duplicate the system per brand.
- Reuse shared files first.
- Use brand docs as context, not as separate operating systems.
- If a request is too broad, narrow it to one shippable outcome.
