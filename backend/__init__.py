from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Airport AI Operations Hub API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

AGENTS = [
    {"id": "NETWORK-001", "name": "Network", "status": "ok", "summary": "Ping, port, VLAN, PoE, DNS", "capabilities": ["ping", "check_port", "vlan_status", "set_port_vlan"], "uptime": 99.9},
    {"id": "CCTV-001", "name": "CCTV", "status": "ok", "summary": "Status kamera, NVR, RTSP", "capabilities": ["camera_status", "nvr_status", "rtsp_test", "restart_camera"], "uptime": 98.1},
    {"id": "SIGNAGE-001", "name": "Digital Signage", "status": "warn", "summary": "Status layar dan content", "capabilities": ["get_status", "screenshot", "restart_player", "emergency_message"], "uptime": 97.0},
    {"id": "FIDS-001", "name": "FIDS", "status": "ok", "summary": "Data penerbangan dan gate", "capabilities": ["get_flights", "display_status", "update_flight"], "uptime": 100.0},
    {"id": "INCIDENT-001", "name": "Insiden", "status": "ok", "summary": "Korelasi dan tiket", "capabilities": ["correlate", "create", "assign", "close"], "uptime": 100.0},
    {"id": "AUDIT-001", "name": "Audit", "status": "ok", "summary": "Catatan semua perintah", "capabilities": ["query", "export", "append"], "uptime": 100.0},
    {"id": "AOPS-001", "name": "AODB · AAS · BAS · PAS · IP-Phone · RIDS · Radar", "status": "warn", "summary": "Satu agent operasional utama", "capabilities": ["aodb_get_flight", "aas_status", "bas_zone_status", "pas_play_announcement", "phone_registrations", "radar_traffic"], "uptime": 99.2},
    {"id": "WIFI-001", "name": "Access Point (WiFi)", "status": "ok", "summary": "Controller WLAN", "capabilities": ["ap_status", "client_count", "rogue_scan", "restart_ap"], "uptime": 99.7},
    {"id": "PANIC-001", "name": "Panic Button", "status": "ok", "summary": "Tombol darurat", "capabilities": ["button_status", "last_trigger", "acknowledge", "silence_alarm"], "uptime": 100.0},
    {"id": "FIRE-001", "name": "Fire Alarm", "status": "ok", "summary": "Panel FACP hanya baca", "capabilities": ["zone_status", "detector_status", "active_alarms", "trouble_list"], "uptime": 99.9},
    {"id": "TEMP-001", "name": "Suhu & Lingkungan", "status": "warn", "summary": "Sensor suhu dan kelembapan", "capabilities": ["get_temp", "history", "threshold_status", "set_threshold"], "uptime": 98.6},
    {"id": "WAYFINDING-001", "name": "Wayfinding", "status": "ok", "summary": "POI dan rute", "capabilities": ["get_route", "create_node", "connect_node", "publish_map"], "uptime": 99.8},
    {"id": "SERVER-001", "name": "Server", "status": "ok", "summary": "CPU dan disk", "capabilities": ["get_metrics", "read_log", "restart_service"], "uptime": 100.0},
    {"id": "CLOCK-001", "name": "Master Clock", "status": "ok", "summary": "Sync NTP dan relay", "capabilities": ["get_sync", "relay_state", "resync"], "uptime": 99.5},
    {"id": "NOTIFY-001", "name": "Notifikasi", "status": "ok", "summary": "WhatsApp, SMS, email", "capabilities": ["send", "escalate", "broadcast_all"], "uptime": 99.9},
    {"id": "REPORT-001", "name": "Laporan", "status": "ok", "summary": "Shift report dan SLA", "capabilities": ["shift_report", "sla_report", "export"], "uptime": 100.0},
    {"id": "BACKUP-001", "name": "Backup & DR", "status": "plan", "summary": "Backup dan restore", "capabilities": ["backup_status", "run_backup", "restore"], "uptime": 0.0},
    {"id": "FACILITY-001", "name": "Fasilitas", "status": "plan", "summary": "Sensor IoT dan fasilitas", "capabilities": ["sensor_status", "set_hvac", "door_override"], "uptime": 0.0},
    {"id": "ENERGY-001", "name": "Daya", "status": "ok", "summary": "UPS, PSU, PDU", "capabilities": ["psu_detail", "ups_status", "poe_budget", "transfer_load"], "uptime": 99.9},
    {"id": "MAINT-001", "name": "Maintenance", "status": "ok", "summary": "Work order dan PM", "capabilities": ["pm_schedule", "create_wo", "close_wo", "restart_service"], "uptime": 100.0},
]

INCIDENTS = [
    {"id": "INC-2026-0929-001", "severity": "Medium", "system": "Signage", "location": "T1 Keberangkatan", "problem": "Display T1-023 offline", "time": "01:12", "state": 0},
    {"id": "INC-2026-0929-002", "severity": "High", "system": "CCTV", "location": "Gate 5", "problem": "Kamera offline, ping gagal", "time": "00:47", "state": 1},
    {"id": "INC-2026-0929-003", "severity": "Low", "system": "Server", "location": "FIDS-SRV-01", "problem": "Disk 92%, arsipkan log lama", "time": "00:20", "state": 2},
    {"id": "INC-2026-0928-014", "severity": "Medium", "system": "Master Clock", "location": "Terminal 2", "problem": "Jam tidak sinkron", "time": "23:55", "state": 1},
]

APPROVALS = [
    {"text": "Kirim pesan evakuasi ke 48 display T1", "agent": "SIGNAGE-001 · emergency_message", "actor": "Operator shift", "status": 0},
    {"text": "Ubah VLAN port sw-t2-14 ke VLAN 40", "agent": "NETWORK-001 · set_port_vlan", "actor": "Operator shift", "status": 0},
]

SYSTEM_STATUS = [
    {"name": "CCTV", "value": 98, "status": "ok"},
    {"name": "FIDS", "value": 100, "status": "ok"},
    {"name": "Digital Signage", "value": 97, "status": "warn"},
    {"name": "Network", "value": 99.6, "status": "ok"},
    {"name": "Server", "value": 100, "status": "ok"},
    {"name": "Master Clock", "value": 100, "status": "ok"},
    {"name": "AODB", "value": 99.9, "status": "ok"},
    {"name": "BAS", "value": 99.4, "status": "ok"},
    {"name": "PAS", "value": 99.7, "status": "ok"},
    {"name": "IP Phone", "value": 98.6, "status": "warn"},
]

NETWORK = {
    "vlans": [
        {"vlan": 10, "name": "MGMT", "subnet": "10.100.10.0/24", "detail": "Switch core, distribusi, access"},
        {"vlan": 15, "name": "WLAN-MGMT", "subnet": "10.100.15.0/24", "detail": "Controller WLAN dan AP"},
        {"vlan": 20, "name": "SERVER", "subnet": "10.100.20.0/24", "detail": "Hub, DB, MQTT, Keycloak, LLM"},
        {"vlan": 30, "name": "AGENT", "subnet": "10.100.30.0/24", "detail": "20 agent"},
        {"vlan": 41, "name": "CCTV-T1", "subnet": "10.100.41.0/24", "detail": "Kamera dan NVR T1"},
        {"vlan": 51, "name": "DISPLAY-RIDS", "subnet": "10.100.51.0/24", "detail": "FIDS, signage, RIDS"},
        {"vlan": 60, "name": "BAS", "subnet": "10.100.60.0/24", "detail": "BACnet dan Modbus"},
        {"vlan": 65, "name": "AUDIO", "subnet": "10.100.65.0/24", "detail": "PAS dan AAS"},
        {"vlan": 66, "name": "SAFETY", "subnet": "10.100.66.0/24", "detail": "Gateway FACP dan panic"},
        {"vlan": 70, "name": "OPERATOR", "subnet": "10.100.70.0/24", "detail": "Workstation operator"},
    ],
    "rules": {
        "70>20": "HTTPS 443 ke hub lewat reverse proxy",
        "20>30": "HTTPS 8001-8020, hub ke agent (mTLS)",
        "30>20": "MQTT 8883, PostgreSQL 5432, Keycloak 8443",
        "30>10": "SNMPv3 dan SSH",
        "30>41": "ONVIF, RTSP",
        "30>51": "HTTPS ke player dan controller",
        "30>60": "BACnet/IP, Modbus TCP",
        "30>65": "SIP, REST",
        "30>66": "Modbus TCP read-only",
    },
}

POWER = {
    "ups": [
        {"name": "UPS-SRV-01", "location": "Ruang server", "status": "Online", "load": 62, "battery": 100, "runtime": 38, "power": 14.2, "voltage": "229 V", "temperature": 31},
        {"name": "UPS-T1-02", "location": "Core T1", "status": "Online", "load": 48, "battery": 100, "runtime": 52, "power": 9.6, "voltage": "231 V", "temperature": 29},
        {"name": "UPS-T2-03", "location": "Core T2", "status": "Baterai lemah", "load": 71, "battery": 78, "runtime": 21, "power": 11.4, "voltage": "228 V", "temperature": 36},
    ],
    "psu": [
        {"unit": "AODB-APP-01", "a": 210, "b": 205, "status": "OK"},
        {"unit": "FIDS-SRV-01", "a": 240, "b": 0, "status": "PSU B gagal"},
        {"unit": "AAS-APP-01", "a": 190, "b": 188, "status": "OK"},
        {"unit": "DS-SRV (switch)", "a": 150, "b": 148, "status": "OK"},
    ],
}

MAINTENANCE = {
    "pm": [
        {"id": "PM-101", "title": "Cek PoE dan bersihkan filter switch core", "system": "Network", "frequency": "Bulanan", "days_until": -4},
        {"id": "PM-102", "title": "Uji restore backup PostgreSQL", "system": "Server", "frequency": "Bulanan", "days_until": 3},
        {"id": "PM-103", "title": "Uji baterai UPS ruang server", "system": "Energi", "frequency": "Triwulan", "days_until": 12},
        {"id": "PM-104", "title": "Bersihkan lensa dan cek fokus kamera", "system": "CCTV", "frequency": "Triwulan", "days_until": 20},
    ],
    "wo": [
        {"id": "WO-C-0417", "problem": "Kamera Gate 5 offline", "system": "CCTV", "priority": "High", "state": 1},
        {"id": "WO-C-0416", "problem": "Display T1-023 player gagal", "system": "Signage", "priority": "Medium", "state": 0},
        {"id": "WO-C-0412", "problem": "Jam T2 tidak sinkron", "system": "Master Clock", "priority": "Medium", "state": 2},
    ],
}

USERS = [
    {"name": "Rina Wijaya", "username": "rina.w", "role": "Supervisor", "unit": "Operasi", "active": True, "mfa": True},
    {"name": "Budi Santoso", "username": "budi.s", "role": "Operator", "unit": "Operasi", "active": True, "mfa": True},
    {"name": "Dewi Lestari", "username": "dewi.l", "role": "Operator", "unit": "Teknisi IT", "active": True, "mfa": True},
    {"name": "Agus Pratama", "username": "agus.p", "role": "Admin", "unit": "IT Infrastruktur", "active": True, "mfa": True},
    {"name": "Sari Utami", "username": "sari.u", "role": "Viewer", "unit": "Manajemen", "active": True, "mfa": False},
    {"name": "Tono Hidayat", "username": "tono.h", "role": "Operator", "unit": "Teknisi CCTV", "active": False, "mfa": True},
]

AUDIT_LOG = [
    {"time": "01:12", "agent": "INCIDENT-001", "message": "Insiden INC-…-001 dibuat dari SIGNAGE-001"},
    {"time": "01:10", "agent": "NETWORK-001", "message": "check_ping T1-023: gagal"},
    {"time": "00:47", "agent": "CCTV-001", "message": "camera_status Gate 5: offline"},
    {"time": "00:31", "agent": "AUDIT-001", "message": "Ekspor log shift malam selesai"},
    {"time": "00:20", "agent": "SERVER-001", "message": "get_metrics FIDS-SRV-01: disk 92%"},
]

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "airport-ai-operations-hub"}

@app.get("/api/overview")
def overview():
    active_agents = sum(1 for agent in AGENTS if agent["status"] in ["ok", "warn", "plan"])
    open_incidents = sum(1 for incident in INCIDENTS if incident["state"] < 3)
    pending_approvals = sum(1 for approval in APPROVALS if approval["status"] == 0)
    return {
        "active_agents": active_agents,
        "total_agents": len(AGENTS),
        "open_incidents": open_incidents,
        "pending_approvals": pending_approvals,
        "system_status": SYSTEM_STATUS,
        "platform": [
            {"name": "PostgreSQL", "status": "ok"},
            {"name": "Redis", "status": "ok"},
            {"name": "MQTT broker", "status": "ok"},
            {"name": "LLM lokal", "status": "ok"},
            {"name": "Keycloak / AD", "status": "ok"},
            {"name": "Backup terakhir: 26 jam lalu", "status": "warn"},
        ],
        "audit": AUDIT_LOG,
    }

@app.get("/api/agents")
def agents():
    return AGENTS

@app.get("/api/incidents")
def incidents():
    return INCIDENTS

@app.get("/api/approvals")
def approvals():
    return APPROVALS

@app.get("/api/network")
def network():
    return NETWORK

@app.get("/api/power")
def power():
    return POWER

@app.get("/api/maintenance")
def maintenance():
    return MAINTENANCE

@app.get("/api/users")
def users():
    return USERS

@app.get("/api/audit")
def audit():
    return AUDIT_LOG

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
