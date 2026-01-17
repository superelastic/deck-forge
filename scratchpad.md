# Project Scratchpad

Last updated: 2026-01-17

## Currently Working On

(Nothing active)

## Open Items

(None)

## Completed

- [x] Fixed broken `{principles,themes` directory (failed brace expansion artifact)
- [x] Created DriveNets explainer deck (12 slides, turing theme) - moved to ~/presentations/
- [x] Validated Marp build pipeline works correctly
- [x] Tested deck creation workflow end-to-end
- [x] Established deck delivery workflow: create → review → move to ~/presentations/
- [x] Updated CLAUDE.md with delivery workflow documentation
- [x] Updated STARTUP_PROTOCOL.md with orphan deck check (step 3)
- [x] Reviewed and refined quality checklist (comprehensive rewrite with tests)

## Before Session End

- [ ] Run `./scripts/archive-session.sh` to save session to .session_logs/

## Notes

- Project uses Marp for markdown-to-slides conversion
- Three themes available: plato, heidegger, turing (in themes/{corporate,technical,academic}/)
- Principles in `principles/` should be read before creating slides
- Finished decks go to `~/presentations/`, not kept in project
- Session memory enables deck recreation via re-prompting
