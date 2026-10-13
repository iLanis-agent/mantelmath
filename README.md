# Mantel math

Mantel math lays out the fireplace surround before the saw: the opening
plus labeled ears becomes the shelf, the shelf at the labeled span
becomes the corbels and their centers, and the shelf bottom minus the
shelf becomes the leg height.

Live site: https://ilanis-agent.github.io/mantelmath/

## The three tools

- **Mantel plan** - `opening + 2 x labeled 15 cm ears` of shelf, with
  a petite / standard / grand fireplace verdict.
- **Corbel plan** - `max(2, ceil(shelf / labeled 60 cm))` corbels at
  even centers, with a pair / row of corbels verdict.
- **Leg plan** - `shelf bottom - shelf thickness` of leg height, with
  a low / classic / tall mantel verdict.

## Limits

Every default is labeled and illustrative. Real mantels near real fire
follow the fireplace maker's clearance-to-combustibles table and the
local code. This is layout arithmetic, not a clearance ruling or a
safety rating: measure the real fireplace and let the maker's table
govern.

## Files

- `index.html` - landing page with the labeled norms
- `app.html` - the three calculators
- `engine.js` - shared calculation and render logic (browser + node)
- `oracle.py` - python mirror of the engine, writes `expected.json`
- `test.js` - runs the engine against `expected.json` (30 cases, 144 checks)

Run the tests: `python3 oracle.py && node test.js`
