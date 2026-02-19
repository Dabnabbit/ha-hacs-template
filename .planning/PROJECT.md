# HA HACS Integration Template

## What This Is

A Copier-based template for building Home Assistant custom integrations with Lovelace frontend cards, distributed via HACS. This is the shared foundation for a family of HA integrations (Argos Translate, Immich Browser, Requestarr) — all architectural decisions, shared patterns, and best practices are established here once and inherited by child projects via `copier update`.

## Core Value

Every shared integration pattern is decided and implemented once in this template, so child projects inherit correct, modern, community-quality code and can focus purely on their unique functionality.

## Requirements

### Validated

(None yet — ship to validate)

### Active

- [ ] Copier template engine with `copier.yml` and Jinja2 variable substitution across all files
- [ ] Coarse-grained Copier conditionals: whole-file inclusion/exclusion for optional patterns (WebSocket, multi-step config, multi-coordinator, service calls)
- [ ] Generic API client base class using `async_get_clientsession(hass)` with configurable auth, timeout, and error handling
- [ ] Full LitElement base card class with theme integration, loading/error states, editor pattern, and card sizing
- [ ] Config flow: single-step default pattern with host/port/API key and connection validation
- [ ] Config flow: multi-step conditional pattern for projects needing multiple service connections
- [ ] Options flow for reconfiguration without removing the integration
- [ ] DataUpdateCoordinator: single-coordinator default pattern
- [ ] DataUpdateCoordinator: multi-coordinator conditional pattern with independent intervals
- [ ] WebSocket command registration and handler pattern (conditional)
- [ ] Service call with `SupportsResponse` pattern (conditional)
- [ ] Device registry integration with `DeviceEntryType.SERVICE`
- [ ] CoordinatorEntity base with proper entity naming, unique IDs, and device grouping
- [ ] Sensor platform with example entities reading from coordinator
- [ ] Frontend static path registration via `async_register_static_paths` (HA 2025.7+)
- [ ] LitElement card editor with entity picker and text field patterns
- [ ] Strings/translations pattern (`strings.json` + `translations/en.json`)
- [ ] CI/CD: GitHub Actions for hassfest + HACS validation
- [ ] CI/CD: Tag-based release workflow with version injection and zip packaging
- [ ] Full pytest test scaffold with HA fixtures, config flow tests, coordinator mocking
- [ ] HACS distribution structure (`hacs.json`, `manifest.json`, README pattern)
- [ ] Minimum HA version 2025.7+ across all generated projects

### Out of Scope

- Project-specific API logic — each child project implements its own API endpoints and data parsing
- Project-specific card UI — each child project builds its own views on top of the base card class
- Project-specific sensors — each child project defines its own entity types and attributes
- Runtime shared library — this is a template, not an importable package. Shared code is rendered into each project at creation time.
- Mobile app / native components — web-based Lovelace cards only

## Context

### Child Projects

Three integrations share this template as their upstream:

1. **ha-argos-translate** — Local text translation via LibreTranslate. Single-step config, service call with `SupportsResponse.ONLY`, single coordinator, translation card with language dropdowns.

2. **ha-immich-browser** — Immich photo library browsing. Single-step config, WebSocket commands for album/asset data, dual coordinators (stats 5min, albums 10min), photo grid card with lightbox and blob URL thumbnails.

3. **ha-requestarr** — Media request dashboard replacing Jellyseerr. Multi-step config flow (TMDB + Radarr + Sonarr + Lidarr), WebSocket commands for search + service calls for requests, single coordinator polling multiple services, tabbed search/request card.

### Shared Bugs in Current Scaffold

All three child projects were generated from an earlier version of this template and share these issues:
- Using deprecated `hass.http.register_static_path()` instead of `async_register_static_paths()`
- Creating raw `aiohttp.ClientSession()` instead of using `async_get_clientsession(hass)`
- Missing `unique_id` in config flow entries
- No device registry integration
- No options flow
- No test structure

### HA Integration Ecosystem

- Target: Home Assistant 2025.7+ (required for `async_register_static_paths` API)
- Distribution: HACS (Home Assistant Community Store) default repository
- IoT class varies per project: `local_polling` (Argos, Immich) vs `cloud_polling` (Requestarr)
- All integrations use `integration_type: "service"` (no physical hardware)
- Frontend: Single-file LitElement cards, no build tools, no npm

## Constraints

- **HA Version**: 2025.7+ minimum — required for `async_register_static_paths` with `StaticPathConfig`
- **No pip dependencies**: All integrations use only HA-bundled libraries (aiohttp, voluptuous, LitElement)
- **Single JS file**: Frontend cards must be self-contained in one JavaScript file — no build step, no module imports
- **Copier compatibility**: All template files must use Jinja2 syntax for variable substitution; directory names use Copier's `_{{ var }}_` naming convention
- **HACS compliance**: Directory structure must pass both `hassfest` and `hacs/action` validation
- **Python 3.12+**: HA's bundled Python version

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Copier for template inheritance | Git upstream merge breaks on domain renames (directory + every file reference changes). Copier handles variable substitution deterministically and supports `copier update` for propagation. | — Pending |
| Coarse-grained conditionals | Fine-grained `{% if %}` inside code files hurts readability. Whole-file conditionals (generate websocket.py or not) + minimal section-level blocks in __init__.py keeps template clean. | — Pending |
| HA 2025.7+ minimum for all projects | `async_register_static_paths` requires 2025.7+. Aligning all projects avoids maintaining deprecated code paths. | — Pending |
| Generic API client base class | All projects need session management, auth, timeout, error handling. Differences (local vs cloud, rate limiting) are configuration, not architecture. One base serves all three. | — Pending |
| Full base card class | All projects share: hass/config wiring, theme CSS, loading/error states, editor registration, card sizing. Copy-and-extend is more maintainable than copy-and-diverge for 3+ projects. | — Pending |
| `DeviceEntryType.SERVICE` for device registry | No physical devices — all integrations are service-based. Service device type groups entities correctly in HA UI with service icon. | — Pending |
| Options flow included | Users need to change host/port/API key after setup without losing entity history. Expected for community-quality HACS integrations. | — Pending |
| Full pytest scaffold | Community HACS integrations need tests. Template provides fixtures and patterns so child projects don't start from zero. | — Pending |

---
*Last updated: 2026-02-19 after initialization*
