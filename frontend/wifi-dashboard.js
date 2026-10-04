// WiFi Dashboard Module - Sinkronisasi dengan data AP real dari Ruijie Network Manager

const WIFI_API_BASE = 'http://localhost:8000/api/wifi';

let wifiData = null;
let apListData = null;
let channelData = null;
let rogueData = null;
let healthData = null;

async function fetchWifiJson(path) {
  const res = await fetch(`${WIFI_API_BASE}${path}`);
  if (!res.ok) throw new Error(`WiFi fetch failed: ${res.status}`);
  return res.json();
}

async function refreshWifiData() {
  try {
    apListData = await fetchWifiJson('/ap');
    channelData = await fetchWifiJson('/channels');
    rogueData = await fetchWifiJson('/rogue');
    healthData = await fetchWifiJson('/health');
    return true;
  } catch (err) {
    console.error('WiFi data refresh failed:', err);
    return false;
  }
}

function renderWifiOverview() {
  if (!apListData) return '';
  const summary = apListData.summary;
  
  return `
    <div class="container">
      <h2>WiFi Infrastructure Overview</h2>
      <p class="muted">Access Point monitoring synchronized with Ruijie Network Manager</p>
      
      <div class="grid">
        <div class="card">
          <p class="kpi">${summary.online}/${summary.total_ap}</p>
          <small>AP Online</small>
        </div>
        <div class="card">
          <p class="kpi">${summary.total_clients}</p>
          <small>Connected Clients</small>
        </div>
        <div class="card">
          <p class="kpi">${summary.avg_signal}</p>
          <small>Average Signal (dBm)</small>
        </div>
        <div class="card">
          <p class="kpi">${summary.avg_clients_per_ap}</p>
          <small>Average Clients per AP</small>
        </div>
      </div>

      <h3>Access Points Status (Real-time from Ruijie)</h3>
      <div style="overflow:auto; border:1px solid var(--line); border-radius:12px; background:var(--panel);">
        <table>
          <thead>
            <tr>
              <th>AP Name</th>
              <th>Location</th>
              <th>IP Address</th>
              <th>Clients</th>
              <th>Signal</th>
              <th>Channel</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            ${apListData.access_points.map(ap => `
              <tr>
                <td>
                  <strong>${ap.name}</strong><br>
                  <span class="muted">${ap.mac_address}</span>
                </td>
                <td>${ap.location}<br><span class="muted">${ap.group}</span></td>
                <td>${ap.ip_address}</td>
                <td>${ap.connected_clients}</td>
                <td>${ap.signal_strength} dBm</td>
                <td>${ap.channel}</td>
                <td>
                  <span class="dot ${ap.status === 'Online' ? '' : 'er'}"></span>
                  ${ap.status}
                </td>
              </tr>
            `).join('')}
          </tbody>
        </table>
      </div>

      <h3>Channel Usage & Interference</h3>
      <div class="grid">
        ${Object.entries(channelData.channels || {}).map(([channel, data]) => `
          <div class="card ${data.status === 'warn' ? 'warn' : ''}">
            <div class="row space-between">
              <strong>Channel ${channel}</strong>
              <span class="pill ${data.status === 'ok' ? 'ok' : 'warn'}">${data.interference}</span>
            </div>
            <p class="kpi" style="font-size:1.6rem;">${data.ap_count}</p>
            <small>AP on this channel</small>
          </div>
        `).join('')}
      </div>

      <h3>Rogue AP Detection</h3>
      ${rogueData.rogue_aps.length > 0 ? `
        <div class="grid">
          ${rogueData.rogue_aps.map(rogue => `
            <div class="card danger">
              <div class="row space-between">
                <strong>${rogue.ssid}</strong>
                <span class="pill er">${rogue.threat_level}</span>
              </div>
              <p class="muted">MAC: ${rogue.mac}<br>Signal: ${rogue.signal} dBm<br>Location: ${rogue.location}<br>Detected: ${rogue.detected}</p>
            </div>
          `).join('')}
        </div>
      ` : `
        <div class="card">
          <div class="dot"></div>
          <span class="muted">No rogue AP detected</span>
        </div>
      `}

      <h3>WiFi Infrastructure Health</h3>
      <div class="grid">
        <div class="card">
          <div class="row space-between"><span>Avg CPU Usage</span><strong>${healthData.health_check.cpu_usage.avg}%</strong></div>
          <div class="bar"><span style="width:${healthData.health_check.cpu_usage.avg}%"></span></div>
        </div>
        <div class="card">
          <div class="row space-between"><span>Avg Memory Usage</span><strong>${healthData.health_check.memory_usage.avg}%</strong></div>
          <div class="bar"><span style="width:${healthData.health_check.memory_usage.avg}%"></span></div>
        </div>
        <div class="card">
          <div class="row space-between"><span>Avg Packet Loss</span><strong>${healthData.health_check.packet_loss.avg}%</strong></div>
          <div class="bar"><span style="width:${healthData.health_check.packet_loss.avg}%"></span></div>
        </div>
      </div>

      <div class="card">
        <small class="muted">Last updated: ${apListData.timestamp}</small>
      </div>
    </div>
  `;
}

export { refreshWifiData, renderWifiOverview, WIFI_API_BASE };
