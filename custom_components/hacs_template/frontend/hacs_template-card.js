/**
 * HACS Template Card
 *
 * A template Lovelace card for Home Assistant.
 * Replace this with your project-specific card implementation.
 */

const LitElement = customElements.get("hui-masonry-view")
  ? Object.getPrototypeOf(customElements.get("hui-masonry-view"))
  : Object.getPrototypeOf(customElements.get("hui-view"));
const html = LitElement.prototype.html;
const css = LitElement.prototype.css;

const CARD_VERSION = "0.1.0";

console.info(
  `%c HACS-TEMPLATE-CARD %c v${CARD_VERSION} `,
  "color: orange; font-weight: bold; background: black",
  "color: white; font-weight: bold; background: dimgray"
);

class HacsTemplateCard extends LitElement {
  static get properties() {
    return {
      hass: { type: Object },
      config: { type: Object },
    };
  }

  static getConfigElement() {
    return document.createElement("hacs-template-card-editor");
  }

  static getStubConfig() {
    return {
      header: "HACS Template",
      entity: "",
    };
  }

  setConfig(config) {
    if (!config) {
      throw new Error("Invalid configuration");
    }
    this.config = {
      header: "HACS Template",
      ...config,
    };
  }

  getCardSize() {
    return 3;
  }

  render() {
    if (!this.hass || !this.config) {
      return html``;
    }

    const entityId = this.config.entity;
    const stateObj = entityId ? this.hass.states[entityId] : null;

    return html`
      <ha-card header="${this.config.header}">
        <div class="card-content">
          ${stateObj
            ? html`
                <div class="state">
                  <span class="label">${stateObj.attributes.friendly_name || entityId}</span>
                  <span class="value">${stateObj.state}</span>
                </div>
              `
            : html`<div class="empty">No entity configured</div>`}
        </div>
      </ha-card>
    `;
  }

  static get styles() {
    return css`
      ha-card {
        padding: 16px;
      }
      .card-content {
        padding: 0 16px 16px;
      }
      .state {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 8px 0;
      }
      .label {
        font-weight: 500;
        color: var(--primary-text-color);
      }
      .value {
        font-size: 1.2em;
        font-weight: bold;
        color: var(--primary-color);
      }
      .empty {
        color: var(--secondary-text-color);
        font-style: italic;
        text-align: center;
        padding: 16px;
      }
    `;
  }
}

/**
 * Card Editor
 */
class HacsTemplateCardEditor extends LitElement {
  static get properties() {
    return {
      hass: { type: Object },
      config: { type: Object },
    };
  }

  setConfig(config) {
    this.config = config;
  }

  render() {
    if (!this.hass || !this.config) {
      return html``;
    }

    return html`
      <div class="editor">
        <ha-textfield
          label="Header"
          .value="${this.config.header || ""}"
          @input="${this._headerChanged}"
        ></ha-textfield>
        <ha-entity-picker
          label="Entity"
          .hass="${this.hass}"
          .value="${this.config.entity || ""}"
          @value-changed="${this._entityChanged}"
          allow-custom-entity
        ></ha-entity-picker>
      </div>
    `;
  }

  _headerChanged(ev) {
    this._updateConfig("header", ev.target.value);
  }

  _entityChanged(ev) {
    this._updateConfig("entity", ev.detail.value);
  }

  _updateConfig(key, value) {
    if (!this.config) return;
    const newConfig = { ...this.config, [key]: value };
    const event = new CustomEvent("config-changed", {
      detail: { config: newConfig },
      bubbles: true,
      composed: true,
    });
    this.dispatchEvent(event);
  }

  static get styles() {
    return css`
      .editor {
        display: flex;
        flex-direction: column;
        gap: 16px;
        padding: 16px;
      }
    `;
  }
}

customElements.define("hacs-template-card", HacsTemplateCard);
customElements.define("hacs-template-card-editor", HacsTemplateCardEditor);

window.customCards = window.customCards || [];
window.customCards.push({
  type: "hacs-template-card",
  name: "HACS Template Card",
  description: "A template card for HACS projects",
  preview: true,
});
