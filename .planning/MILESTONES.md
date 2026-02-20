# Milestones

## v1.0 MVP (Shipped: 2026-02-20)

**Phases:** 1-7 (17 plans) | **Commits:** 92 | **Template:** 25 files, 331 LOC
**Timeline:** 2 days (2026-02-19 to 2026-02-20)
**Git range:** 0de3a18..4a73338

**Delivered:** A Copier-powered template that generates HACS-quality Home Assistant integrations with modern APIs, conditional patterns, test scaffold, and CI/CD — passing hassfest and HACS validation out of the box.

**Key accomplishments:**
1. Fixed all deprecated HA API usage (static paths, clientsession, runtime_data) for HA 2025.7+ compatibility
2. Established Copier template pipeline with custom Jinja2 delimiters solving Python/Jinja2 brace collision
3. Built complete backend core: ApiClient, DataUpdateCoordinator, config/options flow, sensor, device registry
4. Created LitElement frontend card with editor, theme integration, loading/error states, and card picker registration
5. Implemented four conditional file patterns (WebSocket, services, multi-coordinator, multi-step config) via Copier conditionals
6. Added pytest test scaffold with HA fixtures, config flow, coordinator, and conditional test files
7. Created CI/CD pipeline with hassfest + HACS validation, verified passing on live GitHub Actions

**Known Gaps:**
- CICD-02 (release workflow) deferred to per-project setup by user decision
- Multi-step config flow test adaptation (v2 candidate)
- Missing test_services.py conditional template (v2 candidate)

**Archives:** milestones/v1.0-ROADMAP.md, milestones/v1.0-REQUIREMENTS.md, milestones/v1.0-MILESTONE-AUDIT.md

---

