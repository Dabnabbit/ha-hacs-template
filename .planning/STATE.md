# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-02-19)

**Core value:** Every shared integration pattern is decided and implemented once, so child projects inherit correct, modern, community-quality code
**Current focus:** Phase 4 COMPLETE — 04-01 executed (CARD-01 through CARD-08 satisfied); Phase 5 (testing/validation) next

## Current Position

Phase: 4 of 7 (Frontend Card) — COMPLETE
Plan: 1 of 1 in current phase (04-01 complete)
Status: Phase 4 complete — LitElement card with ha-spinner/ha-alert states, getGridOptions, getStubConfig(hass), duplicate guards, Lovelace auto-registration (04-01)
Last activity: 2026-02-20 — 04-01 executed (CARD-01 through CARD-08)

Progress: [████████░░] ~60% (9/15 estimated total plans)

## Performance Metrics

**Velocity:**
- Total plans completed: 9 (01-01, 01-02, 02-01, 02-02, 02-03, 03-01, 03-02, 03-03, 04-01)
- Average duration: ~2 min
- Total execution time: ~19 min

**By Phase:**

| Phase | Plans | Total | Avg/Plan |
|-------|-------|-------|----------|
| 01-scaffold-fixes | 2 | 4 min | 2 min |
| 02-copier-template-scaffolding | 3 | 9 min | 3 min |
| 03-backend-core | 3 | ~5 min | ~2 min |
| 04-frontend-card | 1 | 2 min | 2 min |

**Recent Trend:**
- Last 5 plans: 03-01 (~1 min), 03-02 (1 min), 03-03 (3 min), 04-01 (2 min)
- Trend: Consistent

*Updated after each plan completion*
| Phase 03-backend-core P03 | 3 | 2 tasks | 3 files |
| Phase 04-frontend-card P01 | 2 | 3 tasks | 2 files |

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
- [Phase 02-copier-template-scaffolding]: _envops [[ ]] / [% %] delimiters over {% raw %} blocks — global fix eliminates Python brace collision in all template files
- [Phase 02-copier-template-scaffolding]: _subdirectory: template separates copier.yml and repo docs from template content in template/ dir
- [Phase 02]: Correct copier conditional filename pattern: [% if cond %]name.py[% endif %].jinja — entire base+extension inside [% if %] block so false renders to empty string and copier skips the file
- [Phase 02]: Answers file template uses [[ _copier_conf.answers_file ]].jinja — _envops [[ ]] delimiters apply globally including filename rendering; {{ }} is not rendered with custom envops
- [03-01]: CONF_HOST/CONF_PORT/CONF_API_KEY imported from homeassistant.const only — local shadows removed from const.py to eliminate import confusion (Research Pitfall 1)
- [03-01]: ApiClient._get_auth_headers() is overridable — supports Bearer token default, allows query-param or body auth override without subclassing _request()
- [03-01]: CannotConnectError covers connection, client, and timeout errors — single exception type simplifies coordinator error handling
- [Phase 03-backend-core]: PARALLEL_UPDATES = 0 at module level for coordinator-based sensors (coordinator controls update frequency)
- [Phase 03-backend-core]: DeviceInfo uses entry.title for name and [[ project_name ]] (Copier variable) for manufacturer in sensor template
- [Phase 03-backend-core]: manifest.json.jinja and hacs.json.jinja verified correct from Phase 1/2 — no changes needed for BACK-07 and BACK-08
- [Phase 03-03]: Options flow stores reconfigured values in entry.data via async_update_entry so coordinator re-reads on reload (not entry.options)
- [Phase 03-03]: Git tag 0.1.0 must be advanced to HEAD after each phase that adds new .jinja template files — copier uses tagged version for file list
- [Phase 04-01]: ha-spinner (not ha-circular-progress) for loading state — ha-circular-progress removed in HA frontend 20250326.0 (~HA 2025.4)
- [Phase 04-01]: getGridOptions() is an instance method (not static) — called on card instances by HA sections view framework
- [Phase 04-01]: Lovelace auto-registration wrapped in broad try/except (noqa: BLE001) — community API pattern, not official; fallback to manual registration is acceptable

### Pending Todos

None yet.

### Blockers/Concerns

None currently. Phase 4 LitElement version concern resolved: prototype extraction pattern is version-agnostic; smoke test confirmed rendered output is correct.

## Session Continuity

Last session: 2026-02-20
Stopped at: Completed 04-01-PLAN.md (card JS loading/error states, getGridOptions, Lovelace auto-registration, copier smoke test; CARD-01 through CARD-08 satisfied)
Resume file: None

### Phase 4 Execution Summary (COMPLETE)
- **Plan 04-01 (Wave 1):** Enhanced [[ project_domain ]]-card.js.jinja with ha-spinner loading state, ha-alert error state, four-state render(), getGridOptions(), getStubConfig(hass) with sensor entity lookup, duplicate element guards. Added _async_register_lovelace_resource() to __init__.py.jinja. Copier smoke test: all 14 checks pass. Advanced git tag 0.1.0 to HEAD. 2 commits.

### Phase 3 Execution Summary (COMPLETE)
- **Plan 03-01 (Wave 1):** Created api.py.jinja with ApiClient class (CannotConnectError, InvalidAuthError, Bearer auth, timeout, _request, async_test_connection, async_get_data). Cleaned const.py.jinja of CONF_* shadowing; added DEFAULT_TIMEOUT=30. Wired coordinator.py.jinja to ApiClient. 2 commits.
- **Plan 03-02 (Wave 1):** Added device_info and PARALLEL_UPDATES to sensor.py.jinja. Verified manifest.json.jinja and hacs.json.jinja. 1 commit.
- **Plan 03-03 (Wave 2):** Updated config_flow.py.jinja with CONF_API_KEY, real ApiClient validation, options flow writing to entry.data. Added api_key labels to strings.json.jinja and translations/en.json.jinja. Copier smoke test passed all 9 file checks. 2 commits.

### Phase 2 Execution Summary
- **Plan 02-01 (Wave 1):** Created copier.yml with _envops custom delimiters, restructured all files into template/ with .jinja suffixes and [[ ]] variable substitutions. 3 commits.
- **Plan 02-02 (Wave 2):** Added conditional file templates (websocket, services, coordinator_secondary), smoke-tested copier copy/update pipeline. Auto-fixed 2 bugs: conditional filename pattern and answers file delimiter. 3 commits.
- **Verification:** 7/8 requirements satisfied. 1 gap: COPR-05 multi-step config_flow conditional file missing.
- **Plan 02-03 (Gap closure):** Added [% if use_multi_step_config_flow %]config_flow_multi_step.py[% endif %].jinja stub. Smoke tests verified inclusion (flag=true) and exclusion (flag=false). COPR-05 closed. 1 commit.
- **Phase 2 COMPLETE:** All 8 COPR requirements satisfied.

### Phase 1 Planning Summary
- **Research:** HIGH confidence on all 8 SCAF requirements (01-RESEARCH.md)
- **Plan 01-01 (Wave 1):** Fix integration core — __init__.py (async_setup + runtime_data), coordinator.py (async_get_clientsession), sensor.py (runtime_data access), const.py (URL prefix fix), hacs.json (version bump). Covers SCAF-01, 02, 04, 07, 08.
- **Plan 01-02 (Wave 1):** Fix config flow — unique_id + abort duplicate, connection validation stub, OptionsFlow base class, options flow strings. Covers SCAF-03, 05, 06.
- **Both plans are Wave 1 (parallel)** — disjoint file sets, no dependencies.
- **Verification:** Passed all 7 dimensions. No issues found.
- **No CONTEXT.md** — user chose to proceed without discuss-phase (Phase 1 is correctness-only with no design decisions).
