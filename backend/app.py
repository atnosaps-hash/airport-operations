from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from data_ap import AP_DATA, AP_SUMMARY, CHANNEL_USAGE, ROGUE_APS, HEALTH_CHECK

app = FastAPI(title="Airport AI Operations Hub API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

AGENTS = [
    {"id": "NETWORK-001", "name": "Network", "status": "ok", "summary": "Ping, port, VLAN, PoE, DNS", "uptime": 99.9},
    {"id": "CCTV-001", "name": "CCTV", "status": "ok", "summary": "Status kamera, NVR, perekaman", "uptime": 98.1},
    {"id": "SIGNAGE-001", "name": "Digital Signage", "status": "warn", "summary": "Status player dan content", "uptime": 97.0},
    {"id": "FIDS-001", "name": "FIDS", "status": "ok", "summary": "Data penerbangan dan gate", "uptime": 100.0},
    {"id": "INCIDENT-001", "name": "Insiden", "status": "ok", "summary": "Korelasi dan tiket", "uptime": 100.0},
    {"id": "AUDIT-001", "name": "Audit", "status": "ok", "summary": "Catatan semua perintah", "uptime": 100.0},
    {"id": "AOPS-001", "name": "AODB · AAS · BAS · PAS · RIDS · Radar", "status": "warn", "summary": "Operational systems", "uptime": 99.2},
    {"id": "WIFI-001", "name": "Access Point (WiFi)", "status": "ok", "summary": "Controller WLAN dan AP", "uptime": 99.7},
    {"id": "PANIC-001", "name": "Panic Button", "status": "ok", "summary": "Tombol darurat", "uptime": 100.0},
    {"id": "FIRE-001", "name": "Fire Alarm", "status": "ok", "summary": "Panel FACP", "uptime": 99.9},
    {"id": "TEMP-001", "name": "Suhu & Lingkungan", "status": "warn", "summary": "Sensor suhu", "uptime": 98.6},
    {"id": "WAYFINDING-001", "name": "Wayfinding", "status": "ok", "summary": "POI dan rute", "uptime": 99.8},
    {"id": "SERVER-001", "name": "Server", "status": "ok", "summary": "CPU, RAM, disk", "uptime": 100.0},
    {"id": "CLOCK-001", "name": "Master Clock", "status": "ok", "summary": "NTP dan relay", "uptime": 99.5},
    {"id": "NOTIFY-001", "name": "Notifikasi", "status": "ok", "summary": "WhatsApp, SMS, email", "uptime": 99.9},
    {"id": "REPORT-001", "name": "Laporan", "status": "ok", "summary": "Shift report", "uptime": 100.0},
    {"id": "BACKUP-001", "name": "Backup & DR", "status": "plan", "summary": "Backup dan restore", "uptime": 0.0},
    {"id": "FACILITY-001", "name": "Fasilitas", "status": "plan", "summary": "Sensor IoT", "uptime": 0.0},
    {"id": "ENERGY-001", "name": "Daya", "status": "ok", "summary": "UPS, PSU, PDU", "uptime": 99.9},
    {"id": "MAINT-001", "name": "Maintenance", "status": "ok", "summary": "PM dan WO", "uptime": 100.0},
]

INCIDENTS = [
    {"id": "INC-2026-1004-001", "severity": "Low", "system": "WiFi", "location": "T1 Boarding Gate 11", "problem": "Rogue AP detected: FREE_WIFI_AIRPORT", "time": "14:23", "state": 0},
    {"id": "INC-2026-1004-002", "severity": "Medium", "system": "WiFi", "location": "T2 Check-in Barat", "problem": "Signal strength below threshold: -51 dBm", "time": "14:15", "state": 1},
]

APPROVALS = [
    {"text": "Channel optimization untuk AP T2 Check-in", "agent": "WIFI-001 · channel_optimization", "actor": "Operator shift", "status": 0},
]

VESSEL = {
    "system_status": [
        {"name": "WiFi Controller", "value": 99, "status": "ok"},
        {"name": "Network Switch", "value": 99.8, "status": "ok"},
        {"name": "AP Availability", "value": 100, "status": "ok"},
        {"name": "Rogue Detection", "value": 98, "status": "ok"},
    ],
    "platform": [
        {"name": "WiFi Controller", "status": "ok"},
        {"name": "RADIUS Server", "status": "ok"},
        {"name": "DHCP Server", "status": "ok"},
        {"name": "Portal Server", "status": "ok"},
        {"name": "Monitoring Service", "status": "ok"},
    ],
    "audit": [
        {"time": "14:23", "agent": "WIFI-001", "message": "Rogue AP detected: FREE_WIFI_AIRPORT (aa:bb:cc:dd:ee:01)"},
        {"time": "14:15", "agent": "WIFI-001", "message": "AP DEP_2_T1 signal strength below threshold"},
        {"time": "14:10", "agent": "WIFI-001", "message": "All AP heartbeat received successfully"},
    ],
}

def build_overview():
    return {
        "active_agents": sum(1 for a in AGENTS if a["status"] in ["ok", "warn", "plan"]),
        "total_agents": len(AGENTS),
        "open_incidents": sum(1 for i in INCIDENTS if i["state"] < 3),
        "pending_approvals": sum(1 for a in APPROVALS if a["status"] == 0),
        "system_status": VESSEL["system_status"],
        "platform": VESSEL["platform"],
        "audit": VESSEL["audit"],
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "airport-ai-operations-hub", "timestamp": datetime.utcnow().isoformat() + "Z"}

@app.get("/api/overview")
def overview():
    return build_overview()

@app.get("/api/agents")
def agents():
    return AGENTS

@app.get("/api/incidents")
def incidents():
    return INCIDENTS

@app.get("/api/approvals")
def approvals():
    return APPROVALS

@app.get("/api/wifi/ap")
def wifi_ap():
    """Get all Access Points dengan data real dari Ruijie Network Manager"""
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "summary": AP_SUMMARY,
        "access_points": AP_DATA,
        "total_count": len(AP_DATA),
    }

@app.get("/api/wifi/ap/{ap_name}")
def wifi_ap_detail(ap_name: str):
    """Get detail single AP"""
    ap = next((ap for ap in AP_DATA if ap["name"] == ap_name), None)
    if not ap:
        return {"error": "AP not found", "status": 404}
    return {"timestamp": datetime.utcnow().isoformat() + "Z", "data": ap}

@app.get("/api/wifi/channels")
def wifi_channels():
    """Get channel usage dan interference"""
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "channels": CHANNEL_USAGE,
    }

@app.get("/api/wifi/rogue")
def wifi_rogue():
    """Get rogue AP monitoring"""
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "rogue_aps": ROGUE_APS,
        "threat_count": len(ROGUE_APS),
    }

@app.get("/api/wifi/health")
def wifi_health():
    """Get WiFi infrastructure health check"""
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "health_check": HEALTH_CHECK,
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
