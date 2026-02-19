# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-02-19)

**Core value:** Every shared integration pattern is decided and implemented once, so child projects inherit correct, modern, community-quality code
**Current focus:** Phase 1 - Scaffold Fixes

## Current Position

Phase: 1 of 7 (Scaffold Fixes)
Plan: 2 of 2 in current phase (both 01-01 and 01-02 complete)
Status: Phase 1 complete — ready to advance to Phase 2
Last activity: 2026-02-19 — 01-01 and 01-02 both complete; integration core and config flow fixed for HA 2025.7+

Progress: [██░░░░░░░░] ~14% (2/14 estimated total plans)

## Performance Metrics

**Velocity:**
- Total plans completed: 2 (01-01, 01-02)
- Average duration: 2 min
- Total execution time: 4 min

**By Phase:**

| Phase | Plans | Total | Avg/Plan |
|-------|-------|-------|----------|
| 01-scaffold-fixes | 2 | 4 min | 2 min |

**Recent Trend:**
- Last 5 plans: 01-01 (~2 min), 01-02 (2 min)
- Trend: Consistent

*Updated after each plan completion*

## Accumulated Context

### Decisions

Decisions are logged in PROJECT.md Key Decisions table.
Recent decisions affecting current work:

- [Pre-roadmap]: All three child projects share the same 5 breaking defects — Phase 1 is correctness-only, no new features
- [Pre-roadmap]: Copier Jinja2/Python brace collision must be resolved before any .jinja Python files are written (Phase 2 prerequisite for all later phases)
- [Pre-roadmap]: Static path registration goes in `async_setup` (not `async_setup_entry`) to prevent duplicate registration on second config entry
- [01-01]: entry.runtime_data over hass.data[DOMAIN] — HA-recommended pattern, auto-cleaned on unload
- [01-01]: async_get_clientsession(hass) over raw aiohttp.ClientSession — HA manages HTTP session lifecycle
- [01-01]: Frontend URL uses /{DOMAIN}/ prefix; /hacsfiles/ is HACS-owned namespace for downloaded cards
- [01-01]: hacs.json homeassistant 2025.7.0 — minimum required for async_register_static_paths API
- [01-02]: OptionsFlowHandler extends OptionsFlow base class directly — do NOT define __init__ or manually assign config_entry; HA base class injects it automatically
- [01-02]: async_get_options_flow accepts config_entry parameter (required by HA calling convention) but does NOT pass it to OptionsFlowHandler() constructor
- [01-02]: unique_id uses f'{host}:{port}' string to detect duplicate entries across config flow submissions

### Pending Todos

None yet.

### Blockers/Concerns

- [Phase 4]: LitElement version (Lit 2.x vs 3.x) in HA 2025.7 needs confirmation at smoke-test time — extraction pattern works regardless but API differences may surface

## Session Continuity

Last session: 2026-02-19
Stopped at: Phase 1 complete — both plans 01-01 and 01-02 executed successfully
Resume file: None

### Phase 1 Planning Summary
- **Research:** HIGH confidence on all 8 SCAF requirements (01-RESEARCH.md)
- **Plan 01-01 (Wave 1):** Fix integration core — __init__.py (async_setup + runtime_data), coordinator.py (async_get_clientsession), sensor.py (runtime_data access), const.py (URL prefix fix), hacs.json (version bump). Covers SCAF-01, 02, 04, 07, 08.
- **Plan 01-02 (Wave 1):** Fix config flow — unique_id + abort duplicate, connection validation stub, OptionsFlow base class, options flow strings. Covers SCAF-03, 05, 06.
- **Both plans are Wave 1 (parallel)** — disjoint file sets, no dependencies.
- **Verification:** Passed all 7 dimensions. No issues found.
- **No CONTEXT.md** — user chose to proceed without discuss-phase (Phase 1 is correctness-only with no design decisions).
