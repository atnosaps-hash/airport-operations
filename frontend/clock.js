// Multi-timezone Digital Clock Module

const CLOCK_API_BASE = 'http://localhost:8000/api/clock';

let clockData = null;
let clockConfig = null;
let clockUpdateInterval = null;

class DigitalClock {
  constructor() {
    this.format = '24h';
    this.showSeconds = true;
    this.showDate = true;
    this.updateInterval = 1000;
  }

  async init() {
    try {
      const configRes = await fetch(`${CLOCK_API_BASE}/config`);
      if (configRes.ok) {
        clockConfig = await configRes.json();
        this.format = clockConfig.config.format;
        this.showSeconds = clockConfig.config.show_seconds;
        this.showDate = clockConfig.config.show_date;
      }
    } catch (err) {
      console.error('Clock config fetch failed:', err);
    }

    await this.refresh();
    this.startAutoUpdate();
  }

  async refresh() {
    try {
      const res = await fetch(`${CLOCK_API_BASE}/current`);
      if (!res.ok) throw new Error(`Clock API error: ${res.status}`);
      clockData = await res.json();
      this.render();
      return true;
    } catch (err) {
      console.error('Clock data refresh failed:', err);
      return false;
    }
  }

  startAutoUpdate() {
    if (clockUpdateInterval) clearInterval(clockUpdateInterval);
    clockUpdateInterval = setInterval(() => this.refresh(), this.updateInterval);
  }

  stopAutoUpdate() {
    if (clockUpdateInterval) clearInterval(clockUpdateInterval);
  }

  render() {
    const container = document.getElementById('clock-container');
    if (!container || !clockData) return;

    const stats = `
      <div class="clock-stats">
        <div class="clock-stat-box">
          <div class="clock-stat-value">${clockData.total_zones}</div>
          <div class="clock-stat-label">Timezones</div>
        </div>
        <div class="clock-stat-box">
          <div class="clock-stat-value">${clockData.timezones[0]?.time_24h.split(':')[0] || '--'}</div>
          <div class="clock-stat-label">Local Hour</div>
        </div>
        <div class="clock-stat-box">
          <div class="clock-stat-value" id="updating-indicator">●</div>
          <div class="clock-stat-label">Live Update</div>
        </div>
      </div>
    `;

    const clockCards = clockData.timezones.map((tz, idx) => {
      const isLocal = idx === 0;
      return `
        <div class="clock-card ${isLocal ? 'clock-local-highlight' : ''}">
          <div class="clock-location">${tz.city} (${tz.offset})</div>
          <div class="clock-time-display">${this.format === '24h' ? tz.time_24h : tz.time_12h}</div>
          ${this.showDate ? `<div class="clock-date-display">${tz.date_short}</div>` : ''}
          <div class="clock-info">
            <span class="clock-region">${tz.region}</span>
            <span class="clock-offset">${tz.name}</span>
          </div>
          <div style="margin-top:8px;">
            <span class="clock-status"></span>
            <span style="color:var(--clock-muted); font-size:11px;">Sync</span>
          </div>
        </div>
      `;
    }).join('');

    container.innerHTML = `
      <div class="clock-container">
        <div class="clock-header">
          <div class="clock-title">⏱️ Multi-Timezone Airport Clock</div>
          <div class="clock-controls">
            <button class="clock-control-btn ${this.format === '24h' ? 'active' : ''}" data-action="toggle-format">24H</button>
            <button class="clock-control-btn" data-action="refresh-clock">Refresh</button>
          </div>
        </div>
        
        ${stats}
        
        <div class="clock-grid">
          ${clockCards}
        </div>
        
        <div class="clock-footer">
          Last updated: ${new Date(clockData.timestamp).toLocaleTimeString('id-ID')} UTC
          <br>
          Auto-refresh enabled (every 1 second)
        </div>
      </div>
    `;

    // Attach event listeners
    container.querySelectorAll('[data-action]').forEach(btn => {
      btn.addEventListener('click', (e) => {
        const action = e.target.dataset.action;
        if (action === 'toggle-format') {
          this.format = this.format === '24h' ? '12h' : '24h';
          this.render();
        } else if (action === 'refresh-clock') {
          this.refresh();
        }
      });
    });
  }
}

// Initialize clock when DOM is ready
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    const clock = new DigitalClock();
    clock.init();
  });
} else {
  const clock = new DigitalClock();
  clock.init();
}

export { DigitalClock, CLOCK_API_BASE };
