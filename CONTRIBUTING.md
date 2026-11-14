# Contributing

Keep this kit small, inspectable, and honest about its capabilities. A change
should improve a real workflow or fix a reproducible defect. Avoid adding
background services, hooks, broad tool approvals or dependencies without a
clear need and documented trust boundary.

1. Open an issue or a focused pull request describing the concrete behavior.
2. Make changes in a clean copy. Use dummy data, never private hub state.
3. Run `python scripts/validate.py` and `python -m unittest discover -s tests -v`.
4. If workspace files change, update manifest.json and relevant file-map/checks.
5. For skill/settings changes, link current official documentation. If you run
   a Claude smoke test, state platform, CLI version, exact request, observed
   result, and limitations. Mark unexecuted examples as unexecuted.

Tests should exercise behavior and preservation guarantees, not just match
instruction wording. Keep runtime evaluations distinct from offline checks.
Never claim independent audit, production readiness or speed improvements
without appropriate evidence.

Artwork here is original. Preserve attribution and use assets you have rights
to distribute. Contributions are submitted under this repository's MIT license.
