class GttTimelineCard extends HTMLElement {
  setConfig(config) {
    if (!config.entity) throw new Error("Missing entity");
    this.config = config;
  }

  set hass(hass) {
    const entity = this.config.entity;
    const data = hass.states[entity];
    if (!data) return;

    const fermata = data.attributes
    const linee = data.attributes.arrivi_per_linea || [];

    if (!this.content) {
      this.innerHTML = `
        <ha-card>
          <div class="gtt-container">
            <div class="gtt-stop-container">
              <span class="gtt-stop-icon">🚏</span>
              <span class="gtt-stop-id">Fermata ${data.attributes.fermata_id}</span>
              <span class="gtt-stop-name">(${data.attributes.fermata_name})</span>
            </div>
            <div class="gtt-arrivals-container"></div>
          </div>
        </ha-card>
      `;
      this.content = this.querySelector('.gtt-arrivals-container');
    }

    this.content.innerHTML = linee.map(l => {
      const passaggi = (l.prossimi_rt || []).slice(0, 3);
      const timeline = passaggi.map((p, i) => `
        <div class="tl-row">
          <div class="tl-dot"></div>
          <div class="tl-line" style="opacity:${i === passaggi.length-1 ? 0 : 1}"></div>
          <div class="tl-time">${p}</div>
        </div>
      `).join('');

      return `
        <div class="gtt-arrivals-line">
          <div class="gtt-arrivals-line-header">
            <span class="gtt-arrivals-line-icon">🚍</span>
            <span class="gtt-arrivals-line-title">${l.linea}</span>
            <span class="gtt-arrivals-line-dir"> - ${l.direzione}</span>
          </div>
          <div class="gtt-arrivals-line-timeline">${timeline}</div>
        </div>
      `;
    }).join('');
  }

  static get styles() {
    return `
      .gtt-container {
        background: var(--card-background-color);
        border-radius: 12px;
        padding: 14px;
        box-shadow: var(--ha-card-box-shadow);
      }
      .gtt-stop-container {
        font-weight: bold;
        margin-bottom: 10px;
      }
      .gtt-stop-name {
        font-size: 12px;
      }
      .gtt-arrivals-line:not(:last-of-type) {
        margin-bottom: 10px;
        padding: 0px;
      }
      .gtt-arrivals-line-header {
        margin-bottom: 4px;
        display: flex;
        align-items: center;
      }
      .gtt-arrivals-line-title {
        font-weight: bold;
        margin-left: 4px;
        margin-right: 3px;
      }
      .gtt-arrivals-line-dir {
        font-size: 12px;
        opacity: 0.8;
      }
      .gtt-arrivals-line-timeline {
        margin-left: 8px;
      }
      .tl-row {
        display: grid;
        grid-template-columns: 12px 2px auto;
        align-items: center;
        min-height: 24px;
      }
      .tl-dot {
        width: 10px;
        height: 10px;
        background: var(--primary-color);
        border-radius: 50%;
        animation: pulse 1.6s ease-in-out infinite;
      }
      .tl-line {
        display: none;
        width: 2px;
        background: var(--primary-color);
        height: 100%;
        margin-left: 5px;
      }
      .tl-time {
        padding-left: 8px;
        font-size: 1em;
      }
      @keyframes pulse {
        0% { transform: scale(1); opacity: 1; }
        50% { transform: scale(1.2); opacity: 0.7; }
        100% { transform: scale(1); opacity: 1; }
      }
    `;
  }

  connectedCallback() {
    if (this.styleElement) return;
    this.styleElement = document.createElement('style');
    this.styleElement.textContent = GttTimelineCard.styles;
    this.appendChild(this.styleElement);
  }
}

customElements.define('gtt-timeline-card', GttTimelineCard);