# Requirements: HA HACS Integration Template

**Defined:** 2026-02-19
**Core Value:** Every shared integration pattern is decided and implemented once, so child projects inherit correct, modern, community-quality code

## v1 Requirements

Requirements for template v1 — generates a HACS-quality Bronze/Silver integration from `copier copy`.

### Scaffold Fixes

- [ ] **SCAF-01**: Generated integration uses `async_register_static_paths` with `StaticPathConfig` for frontend JS registration
- [ ] **SCAF-02**: Generated integration uses `async_get_clientsession(hass)` for all HTTP requests (no raw `aiohttp.ClientSession`)
- [ ] **SCAF-03**: Config flow calls `async_set_unique_id` and `_abort_if_unique_id_configured` to prevent duplicate entries
- [ ] **SCAF-04**: Generated integration stores coordinator in `ConfigEntry.runtime_data` with typed generic dataclass (not `hass.data[DOMAIN]`)
- [ ] **SCAF-05**: Config flow includes connection validation stub that raises `CannotConnect` and `InvalidAuth`
- [ ] **SCAF-06**: Options flow uses `OptionsFlow` base class (not `self.config_entry = config_entry` in `__init__`)
- [ ] **SCAF-07**: Static path registration is in domain-level setup (not per-entry) to prevent duplicate registration errors
- [ ] **SCAF-08**: `async_unload_entry` properly cleans up via `async_unload_platforms` (no manual `hass.data` cleanup needed with `runtime_data`)

### Copier Template

- [ ] **COPR-01**: `copier.yml` defines questions for project domain, name, author, description, IoT class, and conditional feature flags
- [ ] **COPR-02**: Template uses Jinja2 variable substitution for domain name in all files (manifest, const, hacs.json, strings, card JS, etc.)
- [ ] **COPR-03**: Template directory uses Copier Jinja2 naming (`custom_components/{{ project_domain }}/`) for domain directory
- [ ] **COPR-04**: All Python template files use `{% raw %}...{% endraw %}` to prevent Jinja2/Python brace collision
- [ ] **COPR-05**: Conditional files (websocket.py, services.py, coordinator_secondary.py, multi-step config_flow.py) are generated or excluded based on Copier question answers
- [ ] **COPR-06**: `copier copy` generates a valid HA integration that passes `hassfest` without manual edits
- [ ] **COPR-07**: `copier update` propagates template changes to existing child projects via 3-way merge
- [ ] **COPR-08**: `.copier-answers.yml` is committed in generated projects with inline warning against manual edits

### Backend Core

- [ ] **BACK-01**: Generic `ApiClient` base class with configurable auth (header/body/query), timeout, and error handling
- [ ] **BACK-02**: `DataUpdateCoordinator` subclass using API client from `runtime_data`, with configurable `update_interval`
- [ ] **BACK-03**: Typed `ConfigEntry` generic defined as `type MyConfigEntry = ConfigEntry[MyData]` with dataclass `runtime_data`
- [ ] **BACK-04**: Sensor platform with `CoordinatorEntity` base, `_attr_has_entity_name = True`, `_attr_unique_id`, and example sensor
- [ ] **BACK-05**: Device registry integration with `DeviceEntryType.SERVICE` on every entity via `device_info` property
- [ ] **BACK-06**: Options flow for reconfiguring host/port/API key after initial setup without removing integration
- [ ] **BACK-07**: `manifest.json` with all required fields, `homeassistant: "2025.7.0"`, `dependencies: ["frontend"]`, `integration_type: "service"`
- [ ] **BACK-08**: `hacs.json` with correct `name` and `homeassistant` minimum version
- [ ] **BACK-09**: `strings.json` and `translations/en.json` covering config flow, options flow, and error messages
- [ ] **BACK-10**: `parallel_updates = 0` set on all platform files (sensor.py and any conditional platforms)

### Frontend Card

- [ ] **CARD-01**: Single-file LitElement card with HA prototype extraction (no CDN, no npm, no build tools)
- [ ] **CARD-02**: Card editor class with `getConfigElement()`, `config-changed` event dispatch (`bubbles: true, composed: true`)
- [ ] **CARD-03**: `window.customCards` registration with `type`, `name`, `description`, and `preview: true`
- [ ] **CARD-04**: `getStubConfig()` returns default config for card picker preview
- [ ] **CARD-05**: `getCardSize()` returns appropriate row count for dashboard layout
- [ ] **CARD-06**: Theme integration via CSS custom properties only (`var(--primary-color)`, etc.) — no hardcoded colors
- [ ] **CARD-07**: Loading state (spinner while coordinator data unavailable) and error state (message when entity unavailable)
- [ ] **CARD-08**: `ha-card` wrapper element for consistent HA card visual chrome

### Conditional Patterns

- [ ] **COND-01**: WebSocket command registration and handler pattern in `websocket.py` (conditional, for Immich/Requestarr)
- [ ] **COND-02**: Service call with `SupportsResponse` pattern in `services.py` + `services.yaml` (conditional, for Argos/Requestarr)
- [ ] **COND-03**: Multi-step config flow variant replacing single-step `config_flow.py` (conditional, for Requestarr)
- [ ] **COND-04**: Secondary coordinator with independent poll interval in `coordinator_secondary.py` (conditional, for Immich)
- [ ] **COND-05**: `__init__.py` uses minimal Jinja2 `{% if %}` blocks for conditional import/registration lines only
- [ ] **COND-06**: `manifest.json` conditionally includes `websocket_api` in `dependencies` when WebSocket pattern is selected

### Testing

- [ ] **TEST-01**: `conftest.py` with `enable_custom_integrations` fixture and HA test helpers
- [ ] **TEST-02**: `test_config_flow.py` covering successful setup, connection failure, duplicate abort, and options flow
- [ ] **TEST-03**: `test_coordinator.py` with mocked API client and coordinator refresh testing
- [ ] **TEST-04**: Conditional test files generated matching conditional source modules (e.g., `test_websocket.py` when WebSocket enabled)
- [ ] **TEST-05**: `pyproject.toml` or `pytest.ini` with `asyncio_mode = auto` and `pytest-homeassistant-custom-component` dependency

### CI/CD & Distribution

- [ ] **CICD-01**: `.github/workflows/validate.yml` running `hassfest` and `hacs/action` on push and PR
- [ ] **CICD-02**: `.github/workflows/release.yml` producing version-tagged zip from git tag with manifest version injection
- [ ] **CICD-03**: Template-generated `README.md` with HACS installation badge, setup instructions, and card usage
- [ ] **CICD-04**: Generated project has correct `.gitignore` for Python, IDE files, and OS artifacts

## v2 Requirements

Deferred to future template versions. Tracked but not in current roadmap.

### Differentiators

- **DIFF-01**: `diagnostics.py` with `async_get_config_entry_diagnostics` and `async_redact_data` for API keys
- **DIFF-02**: `quality_scale.yaml` pre-filled with Bronze/Silver rule compliance status
- **DIFF-03**: Reauthentication flow (`async_step_reauth`) stub for cloud API integrations
- **DIFF-04**: Reconfigure flow (`async_step_reconfigure`) as alternative to options flow for connection details

## Out of Scope

| Feature | Reason |
|---------|--------|
| Runtime shared library / importable package | Template renders code into each project — not a shared dependency at runtime |
| Build tooling for card (webpack, rollup, TypeScript) | HACS requires single-file JS; HA bundles LitElement already |
| pip dependencies in `requirements` | All three child projects use HA-bundled aiohttp only; zero external deps |
| YAML-based configuration (`async_setup`) | All integrations are config-flow-only; YAML config is legacy |
| Automatic discovery (zeroconf/mDNS/SSDP) | None of the three child projects need network discovery |
| Translations beyond English | Community contribution after integrations stabilize |
| Mobile app native components | Web-based Lovelace cards only |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| SCAF-01 | — | Pending |
| SCAF-02 | — | Pending |
| SCAF-03 | — | Pending |
| SCAF-04 | — | Pending |
| SCAF-05 | — | Pending |
| SCAF-06 | — | Pending |
| SCAF-07 | — | Pending |
| SCAF-08 | — | Pending |
| COPR-01 | — | Pending |
| COPR-02 | — | Pending |
| COPR-03 | — | Pending |
| COPR-04 | — | Pending |
| COPR-05 | — | Pending |
| COPR-06 | — | Pending |
| COPR-07 | — | Pending |
| COPR-08 | — | Pending |
| BACK-01 | — | Pending |
| BACK-02 | — | Pending |
| BACK-03 | — | Pending |
| BACK-04 | — | Pending |
| BACK-05 | — | Pending |
| BACK-06 | — | Pending |
| BACK-07 | — | Pending |
| BACK-08 | — | Pending |
| BACK-09 | — | Pending |
| BACK-10 | — | Pending |
| CARD-01 | — | Pending |
| CARD-02 | — | Pending |
| CARD-03 | — | Pending |
| CARD-04 | — | Pending |
| CARD-05 | — | Pending |
| CARD-06 | — | Pending |
| CARD-07 | — | Pending |
| CARD-08 | — | Pending |
| COND-01 | — | Pending |
| COND-02 | — | Pending |
| COND-03 | — | Pending |
| COND-04 | — | Pending |
| COND-05 | — | Pending |
| COND-06 | — | Pending |
| TEST-01 | — | Pending |
| TEST-02 | — | Pending |
| TEST-03 | — | Pending |
| TEST-04 | — | Pending |
| TEST-05 | — | Pending |
| CICD-01 | — | Pending |
| CICD-02 | — | Pending |
| CICD-03 | — | Pending |
| CICD-04 | — | Pending |

**Coverage:**
- v1 requirements: 45 total
- Mapped to phases: 0
- Unmapped: 45

---
*Requirements defined: 2026-02-19*
*Last updated: 2026-02-19 after initial definition*
