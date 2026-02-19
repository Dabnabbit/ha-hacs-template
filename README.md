# HA HACS Integration Template

A [Copier](https://copier.readthedocs.io/) template for building Home Assistant custom integrations with Lovelace frontend cards, distributed via HACS.

## Generating a New Project

```bash
# Install copier (once)
pipx install copier

# Generate a new project
copier copy gh:Dabentz/ha-hacs-template ./my-integration
```

You will be prompted for:
- **project_domain** — Integration domain (e.g. `my_integration`)
- **project_name** — Human-readable name (e.g. `My Integration`)
- **project_description** — Short description
- **author_name** — GitHub username
- **iot_class** — How the integration communicates (`local_polling`, `cloud_polling`, etc.)
- **integration_type** — Integration type (`service`, `hub`, `device`, etc.)
- Feature flags: WebSocket API, custom services, secondary coordinator, multi-step config flow
- **version** — Initial version (`0.1.0`)

## Template Structure

```
ha-hacs-template/                              # template repo root
├── copier.yml                                 # Copier config + questions
├── README.md                                  # this file
├── LICENSE
├── .github/workflows/                         # template repo CI
└── template/                                  # _subdirectory: template
    ├── {{ _copier_conf.answers_file }}.jinja  # generates .copier-answers.yml
    ├── hacs.json.jinja
    ├── README.md.jinja                        # generated project README
    ├── .gitignore
    └── custom_components/
        └── [[ project_domain ]]/              # rendered to your domain
            ├── __init__.py.jinja
            ├── config_flow.py.jinja
            ├── const.py.jinja
            ├── coordinator.py.jinja
            ├── sensor.py.jinja
            ├── manifest.json.jinja
            ├── strings.json.jinja
            ├── translations/
            │   └── en.json.jinja
            └── frontend/
                └── [[ project_domain ]]-card.js.jinja
```

## Updating a Generated Project

When the template is updated, propagate changes to an existing child project:

```bash
cd my-integration
copier update
```

This uses a 3-way merge to apply template changes while preserving your customizations.

## Key Patterns

The generated project includes:
- **Config Flow**: UI-based setup with host/port validation and options flow
- **DataUpdateCoordinator**: Centralized polling pattern with `async_get_clientsession`
- **CoordinatorEntity**: Entities that auto-update from coordinator data
- **Frontend Card**: LitElement-based Lovelace card with visual editor
- **Static Path**: Frontend JS served via `hass.http.async_register_static_paths` (HA 2025.7+)
- **Device Registry**: `DeviceEntryType.SERVICE` grouping for all entities

For details on the generated project's structure and usage, see the generated `README.md`.

## License

MIT
