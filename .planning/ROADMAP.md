# Roadmap: HA HACS Integration Template

## Overview

Seven phases that transform a broken initial scaffold into a Copier-powered template producing community-quality HACS integrations. The first two phases are non-negotiable prerequisites: fix all deprecated HA API usage so the card actually loads, then lock in the Copier render pipeline before any Python source is committed as template files. Backend core and frontend card follow, then conditional patterns and tests layer on top of a stable foundation, and CI/CD closes the loop. Each phase smoke-tests via `copier copy` before the next begins.

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [x] **Phase 1: Scaffold Fixes** - Fix all deprecated HA API usage so generated code loads cleanly on HA 2025.7+ (completed 2026-02-19)
- [ ] **Phase 2: Copier Template Scaffolding** - Establish Copier render pipeline, Jinja2 escaping strategy, and conditional file mechanics
- [ ] **Phase 3: Backend Core** - Always-on integration patterns: API client, coordinator, config/options flow, sensor, device registry, metadata
- [ ] **Phase 4: Frontend Card** - Single-file LitElement base card with editor, theme integration, loading/error states, and card registry
- [ ] **Phase 5: Conditional Patterns** - Four Copier-conditional file sets: WebSocket, services, multi-coordinator, multi-step config flow
- [ ] **Phase 6: Test Scaffold** - pytest infrastructure with HA fixtures, config flow tests, coordinator mocking, and conditional test files
- [ ] **Phase 7: CI/CD and HACS Distribution** - GitHub Actions for hassfest/HACS validation, tag-based release workflow, and distribution files

## Phase Details

### Phase 1: Scaffold Fixes
**Goal**: Generated integrations use only current HA APIs and load cleanly on HA 2025.7+ with no deprecation warnings
**Depends on**: Nothing (first phase)
**Requirements**: SCAF-01, SCAF-02, SCAF-03, SCAF-04, SCAF-05, SCAF-06, SCAF-07, SCAF-08
**Success Criteria** (what must be TRUE):
  1. A generated integration's frontend card loads in HA 2025.7+ (static path registered via `async_register_static_paths` with `StaticPathConfig`)
  2. HA logs show no "Unclosed client session" or aiohttp resource warnings after integration reload
  3. Config flow prevents duplicate entries (setting up the same host twice aborts with an existing-entry error)
  4. Config entry data is accessible via `entry.runtime_data` with a typed dataclass (no `hass.data[DOMAIN]` usage)
  5. Options flow opens and saves without errors on HA 2025.12+ (uses `OptionsFlow` base class, no `__init__` assignment)
**Plans**: 2 plans
Plans:
- [x] 01-01-PLAN.md — Fix integration core: static path registration, runtime_data, HTTP session, version metadata
- [x] 01-02-PLAN.md — Fix config flow: unique_id, connection validation, options flow

### Phase 2: Copier Template Scaffolding
**Goal**: `copier copy` and `copier update` work end-to-end; all Python template files are correctly escaped; first smoke-tested child project renders without errors
**Depends on**: Phase 1
**Requirements**: COPR-01, COPR-02, COPR-03, COPR-04, COPR-05, COPR-06, COPR-07, COPR-08
**Success Criteria** (what must be TRUE):
  1. `copier copy <template-repo> <child-dir>` completes without errors and produces a directory with the correct domain name in all file paths and file contents
  2. Python source files in the generated project contain valid Python (no corrupted dict literals, f-strings, or type hints from Jinja2 collision)
  3. `copier update` in a child project applies a template change via 3-way merge without overwriting custom edits
  4. Generated project passes `hassfest` validation without any manual post-generation edits
  5. `.copier-answers.yml` exists in the generated project root with a visible warning against manual edits
**Plans**: TBD

### Phase 3: Backend Core
**Goal**: A generated integration with default options (single-step config, single coordinator) installs, loads, creates a device entry, and exposes a sensor entity in HA
**Depends on**: Phase 2
**Requirements**: BACK-01, BACK-02, BACK-03, BACK-04, BACK-05, BACK-06, BACK-07, BACK-08, BACK-09, BACK-10
**Success Criteria** (what must be TRUE):
  1. Integration sets up via config flow using host/port/API key with connection validation (failed connection shows error, not crash)
  2. A device entry appears in HA under Settings > Devices with `DeviceEntryType.SERVICE` and the correct integration name
  3. At least one sensor entity is visible under the device and updates from coordinator data
  4. Options flow allows changing host/port/API key after setup; entity history is preserved (no re-setup required)
  5. `manifest.json`, `hacs.json`, and `strings.json`/`translations/en.json` are present and complete; config flow step labels render in the HA UI
**Plans**: TBD

### Phase 4: Frontend Card
**Goal**: The generated Lovelace card is installable as a dashboard resource, appears in the card picker, renders with HA theme colors, and shows loading and error states correctly
**Depends on**: Phase 3
**Requirements**: CARD-01, CARD-02, CARD-03, CARD-04, CARD-05, CARD-06, CARD-07, CARD-08
**Success Criteria** (what must be TRUE):
  1. Card appears in the Lovelace "Add card" picker with name, description, and preview thumbnail
  2. Card editor opens from the card's context menu and dispatches `config-changed` when settings are adjusted
  3. Card renders using HA theme colors (changes visually when HA theme is switched; no hardcoded hex values)
  4. Card displays a spinner while coordinator data is unavailable and an error message when the entity is unavailable
  5. Card is wrapped in `ha-card` and returns a row count from `getCardSize()` that HA uses for layout sizing
**Plans**: TBD

### Phase 5: Conditional Patterns
**Goal**: All four Copier-conditional feature sets generate correctly when selected and are absent when not selected; `__init__.py` wires them in via minimal conditional blocks
**Depends on**: Phase 3
**Requirements**: COND-01, COND-02, COND-03, COND-04, COND-05, COND-06
**Success Criteria** (what must be TRUE):
  1. Selecting WebSocket support generates `websocket.py` with a working command handler and adds `websocket_api` to `manifest.json` dependencies; deselecting omits the file entirely
  2. Selecting service calls generates `services.py` and `services.yaml` with a `SupportsResponse` pattern; deselecting omits them
  3. Selecting multi-step config flow replaces the default `config_flow.py` with a multi-step variant; both variants pass `hassfest`
  4. Selecting secondary coordinator generates `coordinator_secondary.py` with its own poll interval; `entry.runtime_data` holds both coordinators
**Plans**: TBD

### Phase 6: Test Scaffold
**Goal**: Generated projects include a working pytest setup that covers config flow, coordinator, and conditional modules; child project CI can run tests without additional configuration
**Depends on**: Phase 5
**Requirements**: TEST-01, TEST-02, TEST-03, TEST-04, TEST-05
**Success Criteria** (what must be TRUE):
  1. `pytest` runs successfully in a freshly generated project with no additional configuration (asyncio mode is auto, test discovery works)
  2. `test_config_flow.py` covers successful setup, `CannotConnect` error display, duplicate entry abort, and options flow save
  3. `test_coordinator.py` exercises coordinator refresh with a mocked API client and asserts data is stored correctly
  4. When WebSocket support is selected, a `test_websocket.py` file is generated; when not selected, no websocket test file appears
**Plans**: TBD

### Phase 7: CI/CD and HACS Distribution
**Goal**: Every push to a generated project runs hassfest and HACS validation automatically; tagging a release produces a distribution zip with the correct manifest version injected
**Depends on**: Phase 6
**Requirements**: CICD-01, CICD-02, CICD-03, CICD-04
**Success Criteria** (what must be TRUE):
  1. Pushing to a generated project's main branch triggers the validate workflow; a manifest error causes the check to fail visibly
  2. Creating a git tag (e.g., `v1.0.0`) triggers the release workflow and produces a downloadable zip artifact with the version injected into `manifest.json`
  3. Generated `README.md` includes a HACS installation badge, setup instructions, and card usage section populated with the project's domain name
  4. Generated `.gitignore` covers Python, IDE, and OS artifacts; no `__pycache__` or `.DS_Store` files appear in a fresh commit
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4 → 5 → 6 → 7

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Scaffold Fixes | 2/2 | Complete   | 2026-02-19 |
| 2. Copier Template Scaffolding | 0/TBD | Not started | - |
| 3. Backend Core | 0/TBD | Not started | - |
| 4. Frontend Card | 0/TBD | Not started | - |
| 5. Conditional Patterns | 0/TBD | Not started | - |
| 6. Test Scaffold | 0/TBD | Not started | - |
| 7. CI/CD and HACS Distribution | 0/TBD | Not started | - |
