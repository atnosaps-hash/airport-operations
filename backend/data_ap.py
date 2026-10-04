# Data AP Real dari Ruijie Network Manager
AP_DATA = [
    {
        "name": "BOARDING_GATE_11",
        "mac_address": "d833.2acf.55b1",
        "ip_address": "172.16.1.166",
        "location": "T1",
        "group": "Terminal 1",
        "model": "AP880-L",
        "status": "Online",
        "signal_strength": -45,
        "connected_clients": 24,
        "uptime": "45d 12h 30m",
        "last_seen": "2026-10-04 14:23:00",
        "channel": 6,
        "tx_power": "20 dBm",
        "ssid": ["AIRPORT_WIFI_T1", "AIRPORT_GUEST_T1"]
    },
    {
        "name": "CHECKPOINT_IMMIGRATION",
        "mac_address": "d833.2acf.6253",
        "ip_address": "172.16.2.94",
        "location": "T2",
        "group": "Terminal 2",
        "model": "AP880-L",
        "status": "Online",
        "signal_strength": -48,
        "connected_clients": 31,
        "uptime": "42d 8h 15m",
        "last_seen": "2026-10-04 14:22:55",
        "channel": 11,
        "tx_power": "20 dBm",
        "ssid": ["AIRPORT_WIFI_T2", "AIRPORT_GUEST_T2"]
    },
    {
        "name": "CHECK_IN_BARAT",
        "mac_address": "d833.2acf.5d3d",
        "ip_address": "172.16.2.163",
        "location": "T2",
        "group": "Terminal 2",
        "model": "AP880-L",
        "status": "Online",
        "signal_strength": -50,
        "connected_clients": 18,
        "uptime": "38d 5h 45m",
        "last_seen": "2026-10-04 14:22:50",
        "channel": 1,
        "tx_power": "20 dBm",
        "ssid": ["AIRPORT_WIFI_T2", "AIRPORT_GUEST_T2"]
    },
    {
        "name": "CHECK_IN_TIMUR",
        "mac_address": "d833.2acf.5d49",
        "ip_address": "172.16.3.247",
        "location": "T2",
        "group": "Terminal 2",
        "model": "AP880-L",
        "status": "Online",
        "signal_strength": -46,
        "connected_clients": 28,
        "uptime": "41d 14h 20m",
        "last_seen": "2026-10-04 14:22:48",
        "channel": 6,
        "tx_power": "20 dBm",
        "ssid": ["AIRPORT_WIFI_T2", "AIRPORT_GUEST_T2"]
    },
    {
        "name": "CIC_19-20",
        "mac_address": "d833.2acf.5ca7",
        "ip_address": "172.16.1.248",
        "location": "T1",
        "group": "Terminal 1",
        "model": "AP880-L",
        "status": "Online",
        "signal_strength": -44,
        "connected_clients": 35,
        "uptime": "46d 2h 10m",
        "last_seen": "2026-10-04 14:23:05",
        "channel": 11,
        "tx_power": "20 dBm",
        "ssid": ["AIRPORT_WIFI_T1", "AIRPORT_GUEST_T1"]
    },
    {
        "name": "DEP3_LUAR_SELFCHECKIN",
        "mac_address": "d833.2acf.5ab5",
        "ip_address": "172.16.0.82",
        "location": "T1",
        "group": "Terminal 1",
        "model": "AP880-L",
        "status": "Online",
        "signal_strength": -49,
        "connected_clients": 22,
        "uptime": "40d 18h 50m",
        "last_seen": "2026-10-04 14:22:45",
        "channel": 1,
        "tx_power": "20 dBm",
        "ssid": ["AIRPORT_WIFI_T1", "AIRPORT_GUEST_T1"]
    },
    {
        "name": "DEP_2_DEPAN_OOG",
        "mac_address": "d833.2acf.5587",
        "ip_address": "172.16.1.137",
        "location": "T1",
        "group": "Terminal 1",
        "model": "AP880-L",
        "status": "Online",
        "signal_strength": -47,
        "connected_clients": 26,
        "uptime": "43d 11h 30m",
        "last_seen": "2026-10-04 14:22:52",
        "channel": 6,
        "tx_power": "20 dBm",
        "ssid": ["AIRPORT_WIFI_T1", "AIRPORT_GUEST_T1"]
    },
    {
        "name": "DEP_2_T1",
        "mac_address": "d833.2acf.6265",
        "ip_address": "172.16.0.193",
        "location": "T1",
        "group": "Terminal 1",
        "model": "AP880-L",
        "status": "Online",
        "signal_strength": -51,
        "connected_clients": 19,
        "uptime": "39d 9h 25m",
        "last_seen": "2026-10-04 14:22:40",
        "channel": 11,
        "tx_power": "17 dBm",
        "ssid": ["AIRPORT_WIFI_T1", "AIRPORT_GUEST_T1"]
    },
    {
        "name": "DEP_3_DALAM",
        "mac_address": "d833.2acf.686b",
        "ip_address": "172.16.1.254",
        "location": "T1",
        "group": "Terminal 1",
        "model": "AP880-L",
        "status": "Online",
        "signal_strength": -45,
        "connected_clients": 29,
        "uptime": "44d 6h 55m",
        "last_seen": "2026-10-04 14:23:02",
        "channel": 1,
        "tx_power": "20 dBm",
        "ssid": ["AIRPORT_WIFI_T1", "AIRPORT_GUEST_T1"]
    },
    {
        "name": "DEP_4_LUAR",
        "mac_address": "d833.2acf.512f",
        "ip_address": "172.16.0.148",
        "location": "T1",
        "group": "Terminal 1",
        "model": "AP880-L",
        "status": "Online",
        "signal_strength": -48,
        "connected_clients": 21,
        "uptime": "41d 17h 40m",
        "last_seen": "2026-10-04 14:22:58",
        "channel": 6,
        "tx_power": "20 dBm",
        "ssid": ["AIRPORT_WIFI_T1", "AIRPORT_GUEST_T1"]
    }
]

# Statistik AP
AP_SUMMARY = {
    "total_ap": len(AP_DATA),
    "online": sum(1 for ap in AP_DATA if ap["status"] == "Online"),
    "offline": sum(1 for ap in AP_DATA if ap["status"] == "Offline"),
    "warning": sum(1 for ap in AP_DATA if ap["status"] == "Warning"),
    "total_clients": sum(ap["connected_clients"] for ap in AP_DATA),
    "avg_signal": round(sum(ap["signal_strength"] for ap in AP_DATA) / len(AP_DATA), 1),
    "avg_clients_per_ap": round(sum(ap["connected_clients"] for ap in AP_DATA) / len(AP_DATA), 1),
}

# Channel usage
CHANNEL_USAGE = {
    "1": {"ap_count": sum(1 for ap in AP_DATA if ap["channel"] == 1), "interference": "Low", "status": "ok"},
    "6": {"ap_count": sum(1 for ap in AP_DATA if ap["channel"] == 6), "interference": "Medium", "status": "warn"},
    "11": {"ap_count": sum(1 for ap in AP_DATA if ap["channel"] == 11), "interference": "Low", "status": "ok"},
}

# Rogue AP monitoring
ROGUE_APS = [
    {"ssid": "FREE_WIFI_AIRPORT", "mac": "aa:bb:cc:dd:ee:01", "signal": -62, "threat_level": "High", "location": "T1", "detected": "2026-10-04 13:45:00"},
    {"ssid": "AIRPORT_WIFI_CLONE", "mac": "aa:bb:cc:dd:ee:02", "signal": -65, "threat_level": "High", "location": "T2", "detected": "2026-10-04 12:15:00"},
]

# AP Health Check Results
HEALTH_CHECK = {
    "cpu_usage": {"avg": 28, "max": 45, "min": 12},
    "memory_usage": {"avg": 62, "max": 78, "min": 51},
    "packet_loss": {"avg": 0.2, "max": 1.5, "min": 0.0},
    "last_check": "2026-10-04 14:22:00",
}
