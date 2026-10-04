const timezoneOptions = [
  { value: 'Asia/Jakarta', label: 'Jakarta (WIB)' },
  { value: 'Asia/Singapore', label: 'Singapore (SGT)' },
  { value: 'Asia/Bangkok', label: 'Bangkok (ICT)' },
  { value: 'Asia/Tokyo', label: 'Tokyo (JST)' },
  { value: 'Australia/Sydney', label: 'Sydney (AEST)' },
  { value: 'Europe/London', label: 'London (GMT)' },
  { value: 'Europe/Paris', label: 'Paris (CET)' },
  { value: 'America/New_York', label: 'New York (EST)' },
  { value: 'America/Los_Angeles', label: 'Los Angeles (PST)' },
  { value: 'UTC', label: 'UTC' }
];

const flights = [
  { code: 'GA 412', route: 'Jakarta → Singapore', type: 'Departure', localTime: '06:40', status: 'on-time', gate: 'A3' },
  { code: 'JT 610', route: 'Bangkok → Jakarta', type: 'Arrival', localTime: '06:55', status: 'delay', gate: 'B1' },
  { code: 'QG 807', route: 'Jakarta → Tokyo', type: 'Departure', localTime: '07:10', status: 'on-time', gate: 'A5' },
  { code: 'ID 6512', route: 'Jakarta → Sydney', type: 'Arrival', localTime: '07:15', status: 'on-time', gate: 'B4' },
  { code: 'SJ 265', route: 'Jakarta → London', type: 'Departure', localTime: '08:05', status: 'on-time', gate: 'C2' },
  { code: 'IU 723', route: 'Bangkok → Jakarta', type: 'Arrival', localTime: '09:20', status: 'delay', gate: 'C5' }
];

const timezoneSelect = document.getElementById('timezoneSelect');
const flightList = document.getElementById('flightList');
const todayDate = document.getElementById('todayDate');
const departuresCount = document.getElementById('departuresCount');
const arrivalsCount = document.getElementById('arrivalsCount');
const localClock = document.getElementById('localClock');

function buildTimezoneOptions() {
  timezoneSelect.innerHTML = timezoneOptions.map(
    (tz) => `<option value="${tz.value}">${tz.label}</option>`
  ).join('');

  timezoneSelect.value = 'Asia/Jakarta';
}

function formatDateForZone(date, timeZone) {
  return new Intl.DateTimeFormat('en-GB', {
    timeZone,
    weekday: 'short',
    day: '2-digit',
    month: 'short',
    year: 'numeric'
  }).format(date);
}

function formatTimeForZone(date, timeZone) {
  return new Intl.DateTimeFormat('en-GB', {
    timeZone,
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: false
  }).format(date);
}

function getConvertedFlightTime(baseTime, timeZone) {
  const [hour, minute] = baseTime.split(':').map(Number);
  const d = new Date();
  d.setHours(hour, minute, 0, 0);

  const formatter = new Intl.DateTimeFormat('en-GB', {
    timeZone,
    hour: '2-digit',
    minute: '2-digit',
    hour12: false
  });

  return formatter.format(d);
}

function renderFlights() {
  const selectedZone = timezoneSelect.value;
  const now = new Date();

  todayDate.textContent = formatDateForZone(now, selectedZone);
  localClock.textContent = formatTimeForZone(now, selectedZone);

  departuresCount.textContent = flights.filter(f => f.type === 'Departure').length;
  arrivalsCount.textContent = flights.filter(f => f.type === 'Arrival').length;

  flightList.innerHTML = flights.map((flight) => {
    const converted = getConvertedFlightTime(flight.localTime, selectedZone);
    const badgeClass = flight.status === 'on-time'
      ? 'on-time'
      : flight.status === 'delay'
        ? 'delay'
        : 'cancelled';

    const statusText = flight.status === 'on-time'
      ? 'On time'
      : flight.status === 'delay'
        ? 'Delayed'
        : 'Cancelled';

    return `
      <article class="flight-card">
        <div class="flight-code">${flight.code}</div>

        <div class="flight-route">
          <span>${flight.route.split(' → ')[0]}</span>
          <span class="arrow">→</span>
          <span>${flight.route.split(' → ')[1]}</span>
        </div>

        <div class="flight-status">
          <i class="dot ${flight.status === 'on-time' ? 'ok' : flight.status === 'delay' ? 'warn' : 'er'}"></i>
          ${flight.type} • ${flight.gate}
        </div>

        <div class="flight-time">
          <strong>${converted}</strong>
          <small>${flight.localTime} local</small>
        </div>

        <div class="badge ${badgeClass}">${statusText}</div>
      </article>
    `;
  }).join('');
}

buildTimezoneOptions();
renderFlights();
timezoneSelect.addEventListener('change', renderFlights);
setInterval(renderFlights, 1000);
