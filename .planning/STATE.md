# Project State

## Project Reference

See: .planning/PROJECT.md (updated 2026-02-19)

**Core value:** Every shared integration pattern is decided and implemented once, so child projects inherit correct, modern, community-quality code
**Current focus:** Phase 7 UAT found 1 gap (hassfest failures). Fix plan 07-02 ready for execution. 48/49 active requirements satisfied (CICD-02 deferred).

## Current Position

Phase: 7 of 7 (CI/CD and HACS Distribution) — GAP CLOSURE PENDING
Plan: 2 of 2 in current phase (07-01 complete, 07-02 planned — gap closure)
Status: Phase 7 UAT revealed hassfest failures. Fix plan 07-02 ready. CICD-02 formally deferred.
Last activity: 2026-02-20 — Phase 7 UAT complete (5 pass, 1 issue), gap diagnosed, fix plan 07-02 verified

Progress: [█████████░] 95% (48/49 active requirements satisfied, 1 deferred)

## Performance Metrics

**Velocity:**
- Total plans completed: 16 (01-01, 01-02, 02-01, 02-02, 02-03, 03-01, 03-02, 03-03, 04-01, 05-01, 05-02, 05-03, 06-01, 06-02, 06-03, 07-01)
- Plans pending: 1 (07-02 gap closure)
- Average duration: ~2 min
- Total execution time: ~26 min

**By Phase:**

| Phase | Plans | Total | Avg/Plan |
|-------|-------|-------|----------|
| 01-scaffold-fixes | 2 | 4 min | 2 min |
| 02-copier-template-scaffolding | 3 | 9 min | 3 min |
| 03-backend-core | 3 | ~5 min | ~2 min |
| 04-frontend-card | 1 | 2 min | 2 min |
| 05-conditional-patterns | 3 | 4 min | 1 min |
| 06-test-scaffold | 3 | 3 min | 1 min |

**Recent Trend:**
- Last 5 plans: 05-03 (1 min), 06-01 (1 min), 06-02 (1 min), 06-03 (1 min)
- Trend: Consistent, accelerating

*Updated after each plan completion*
| Phase 03-backend-core P03 | 3 | 2 tasks | 3 files |
| Phase 04-frontend-card P01 | 2 | 3 tasks | 2 files |
| Phase 05-conditional-patterns P01 | 1 | 2 tasks | 4 files |
| Phase 05-conditional-patterns P02 | 1 | 2 tasks | 6 files |
| Phase 05-conditional-patterns P03 | 2 | 2 tasks | 1 files |
| Phase 06-test-scaffold P01 | 1 | 2 tasks | 3 files |
| Phase 06-test-scaffold P02 | 1 | 2 tasks | 2 files |
| Phase 06-test-scaffold P03 | 1 | 2 tasks | 1 files |
| Phase 07-cicd-and-hacs-distribution P01 | 1 | 2 tasks | 2 files |
| Phase 07-cicd-and-hacs-distribution P02 | - | 1 task  | 2 files | (gap closure — planned, not yet executed)

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
- [05-01]: manifest.json conditional websocket_api uses `, "websocket_api"` inside [% if use_websocket %] block — comma placement ensures valid JSON for both flag states
- [05-01]: services.yaml created as new conditional file (no Phase 2 stub existed) using same [% if use_services %]services.yaml[% endif %].jinja pattern
- [05-01]: WebSocket handler imports coordinator type lazily inside handler body (noqa: PLC0415) to avoid circular import at module level
- [Phase 05-conditional-patterns]: Option C confirmed: multi-step flow inlined in config_flow.py.jinja via [% if %] blocks — single-step [% else %] branch is byte-for-byte identical to pre-edit output
- [Phase 05-conditional-patterns]: DEFAULT_SECONDARY_SCAN_INTERVAL = 300 always included in const.py (unconditional) — harmless if unused, avoids conditional import complexity
- [Phase 05-conditional-patterns]: coordinator_secondary creates its own ApiClient (not shared with primary) to avoid concurrent refresh race conditions
- [Phase 05-conditional-patterns]: WebSocket and services called in async_setup (not async_setup_entry) — prevents duplicate handler registration when multiple config entries exist
- [Phase 05-conditional-patterns]: runtime_data uses if/else branch so all-ON case passes coordinator_secondary=coordinator_secondary to the Data constructor
- [06-01]: asyncio_mode=auto (not strict) — HA ecosystem default; zero per-test @pytest.mark.asyncio annotation; mandatory since pytest-asyncio 0.21/1.0
- [06-01]: tests/__init__.py.jinja contains comment line (not empty) — guards against Copier skipping empty-output files (Pitfall 5)
- [06-01]: mock_setup_entry patches custom_components.[[ project_domain ]].async_setup_entry at top-level __init__ (not config_flow) — where HA calls the function
- [Phase 06-test-scaffold]: Patch target for config flow is config_flow._async_validate_connection (where called, not where ApiClient is defined) — Pitfall 2 from research
- [Phase 06-test-scaffold]: Options flow test asserts entry.data[CONF_API_KEY] (not entry.options) — consistent with Phase 3-03 decision that options flow writes to entry.data
- [06-03]: Conditional test filename [% if use_websocket %]test_websocket.py[% endif %].jinja — identical pattern to Phase 5 source conditional files
- [06-03]: WebSocket test requires full integration setup (async_setup + async_block_till_done) before ws_client — handlers registered in async_setup, not async_setup_entry
- [07-01]: validate.yml is a STATIC file (no .jinja suffix) — workflow contains zero Copier variables, identical for every generated project; Copier copies static files verbatim
- [07-01]: CICD-02 (release workflow) formally deferred per user decision — ROADMAP and REQUIREMENTS updated to reflect descoping; no release.yml created
- [07-01]: ignore: brands included in HACS action — prevents CI failure for new integrations before brand images submitted to home-assistant/brands
- [07-01]: checkout step only in hassfest job — hacs/action is Docker-based and fetches repo internally; checkout is redundant in HACS job
- [07-UAT]: hassfest requires `http` in manifest dependencies even though `frontend` transitively depends on it — hassfest checks direct imports only
- [07-UAT]: hassfest requires CONFIG_SCHEMA = cv.config_entry_only_config_schema(DOMAIN) when async_setup is defined in a config-entry-only integration

### Pending Todos

None yet.

### Blockers/Concerns

None currently. Phase 4 LitElement version concern resolved: prototype extraction pattern is version-agnostic; smoke test confirmed rendered output is correct.

## Session Continuity

Last session: 2026-02-20
Stopped at: Phase 7 UAT complete. 5/6 tests passed. 1 issue: hassfest fails on clean generated project (missing http dep + CONFIG_SCHEMA). Gap diagnosed, fix plan 07-02 created and verified. Ready for execution.
Resume file: .planning/phases/07-cicd-and-hacs-distribution/07-02-PLAN.md
Resume action: /gsd:execute-phase 7 --gaps-only

### Phase 7 Execution Summary (GAP CLOSURE PENDING)
- **Plan 07-01 (Wave 1):** Created template/.github/workflows/validate.yml as static file (two-job pattern: hassfest + HACS action, SHA-pinned, permissions: {}, ignore: brands). Updated template/.gitignore with test artifact exclusions (.pytest_cache/, .coverage, coverage.xml, htmlcov/). Copier smoke test: all 8 checks PASS. CICD-01, CICD-02 (formally deferred), CICD-03 (pre-existing), CICD-04 satisfied. 1 commit.
- **UAT (5 pass, 1 issue):** Tests 1-5 passed (template structure, copier generation, .gitignore, README, hassfest catches errors). Test 6 failed: clean generated project fails hassfest (http dep missing + CONFIG_SCHEMA missing). Live test on GitHub repo Dabnabbit/uat-cicd-test confirmed both failures.
- **Plan 07-02 (Gap closure, planned):** Fix manifest.json.jinja (add "http" to dependencies) and __init__.py.jinja (add cv import + CONFIG_SCHEMA declaration). 1 task, 2 files. Verified by plan checker. Ready: `/gsd:execute-phase 7 --gaps-only`

### Phase 6 Execution Summary (COMPLETE)
- **Plan 06-01 (Wave 1):** Created pyproject.toml.jinja (asyncio_mode=auto, testpaths, pytest-homeassistant-custom-component dep), tests/__init__.py.jinja (non-empty package marker), tests/conftest.py.jinja (auto_enable_custom_integrations autouse fixture + mock_setup_entry fixture with [[ project_domain ]] Copier variable). TEST-01, TEST-05 satisfied. 2 commits.
- **Plan 06-02 (Wave 2):** Created tests/test_config_flow.py.jinja (4 cases: successful setup via mock_setup_entry, CannotConnect error, duplicate abort via MockConfigEntry unique_id, options flow via config_entries.options asserting entry.data). Created tests/test_coordinator.py.jinja (2 cases: mocked ApiClient.async_get_data success, CannotConnectError translated to UpdateFailed). TEST-02, TEST-03 satisfied. 2 commits.
- **Plan 06-03 (Wave 3):** Created conditional tests/[% if use_websocket %]test_websocket.py[% endif %].jinja with test_websocket_get_data using hass_ws_client fixture. Copier smoke tests: all-OFF (9 checks PASS, test_websocket.py absent) and all-ON (8 checks PASS, test_websocket.py present). TEST-04 satisfied. 1 commit. Phase 6 COMPLETE.

### Phase 5 Execution Summary (COMPLETE)
- **Plan 05-01 (Wave 1):** Replaced websocket.py stub with async handler (@websocket_command + @async_response + async_setup_websocket). Replaced services.py stub with SupportsResponse.OPTIONAL handler (async_register_services). Created new services.yaml conditional template. Updated manifest.json.jinja with conditional websocket_api dependency. COND-01, COND-02, COND-06 satisfied. 2 commits.
- **Plan 05-02 (Wave 1):** Inlined multi-step config flow into config_flow.py.jinja via [% if use_multi_step_config_flow %] blocks (two schemas, __init__, async_step_user chains to async_step_credentials; unique_id in last step). Deleted dead config_flow_multi_step.py stub. Updated strings.json.jinja and translations/en.json.jinja with conditional credentials step. Replaced coordinator_secondary.py stub with TemplateSecondaryCoordinator (300s interval, own ApiClient). Added DEFAULT_SECONDARY_SCAN_INTERVAL = 300 to const.py. COND-03, COND-04 satisfied. 2 commits.
- **Plan 05-03 (Wave 2):** Added 8 conditional [% if %] blocks to __init__.py.jinja (3 imports, 1 dataclass field, 2 async_setup calls, 1 secondary coordinator init, 1 if/else runtime_data). Copier smoke tests: all-OFF (22 checks PASS) and all-ON (24 checks PASS). COND-05 satisfied. 1 commit. Phase 5 complete.

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
