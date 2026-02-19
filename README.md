# HACS Template

A template repository for building Home Assistant custom integrations with Lovelace frontend cards, distributed via HACS.

## Structure

```
ha-hacs-template/
├── .github/workflows/
│   ├── validate.yml              # HACS + hassfest validation
│   └── release.yml               # Automated release on tag
├── custom_components/
│   └── hacs_template/
│       ├── __init__.py           # Integration setup + frontend registration
│       ├── config_flow.py        # UI configuration flow
│       ├── const.py              # Constants
│       ├── coordinator.py        # DataUpdateCoordinator
│       ├── sensor.py             # Example sensor platform
│       ├── manifest.json         # HA integration manifest
│       ├── strings.json          # UI strings
│       ├── translations/en.json  # English translations
│       └── frontend/
│           └── hacs_template-card.js  # Lovelace card + editor
├── hacs.json                     # HACS metadata
├── LICENSE
└── README.md
```

## Using This Template

1. Click "Use this template" on GitHub to create a new repo
2. Rename `custom_components/hacs_template/` to your integration domain
3. Update all references to `hacs_template` with your domain name
4. Update `manifest.json`, `hacs.json`, and `const.py` with your project details
5. Implement your coordinator, sensors/entities, config flow, and card

## Key Patterns

- **Config Flow**: UI-based setup via `config_flow.py` + `strings.json`
- **DataUpdateCoordinator**: Centralized polling in `coordinator.py`
- **CoordinatorEntity**: Entities that auto-update from coordinator data
- **Frontend Card**: LitElement-based Lovelace card with visual editor
- **Static Path**: Integration serves its own JS card file via `hass.http.register_static_path()`

## Development

### Testing locally

1. Copy `custom_components/hacs_template/` into your HA `config/custom_components/`
2. Restart Home Assistant
3. Add the integration via Settings > Devices & Services > Add Integration
4. Add the card to a dashboard

### Creating a release

1. Update version in `manifest.json`
2. Create a GitHub release with a tag like `v0.1.0`
3. The release workflow will create a zip artifact automatically

## License

MIT
