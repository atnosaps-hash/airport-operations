from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone
import pytz
from data_timezone import TIMEZONES, CLOCK_CONFIG

app = FastAPI(title="Airport Timezone Clock API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/clock/current")
def get_current_time():
    """Get current time in all configured timezones"""
    times = []
    
    for tz_config in TIMEZONES:
        try:
            tz = pytz.timezone(tz_config["timezone"])
            current_time = datetime.now(tz)
            
            times.append({
                "name": tz_config["name"],
                "timezone": tz_config["timezone"],
                "offset": tz_config["offset"],
                "city": tz_config["city"],
                "region": tz_config["region"],
                "time_24h": current_time.strftime("%H:%M:%S"),
                "time_12h": current_time.strftime("%I:%M:%S %p"),
                "date": current_time.strftime("%A, %d %B %Y"),
                "date_short": current_time.strftime("%d-%m-%Y"),
                "iso": current_time.isoformat(),
            })
        except Exception as e:
            print(f"Error getting time for {tz_config['timezone']}: {e}")
    
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "config": CLOCK_CONFIG,
        "timezones": times,
        "total_zones": len(times),
    }

@app.get("/api/clock/timezone/{tz_name}")
def get_timezone_time(tz_name: str):
    """Get current time for a specific timezone"""
    tz_config = next((tz for tz in TIMEZONES if tz["timezone"].lower() == tz_name.lower()), None)
    
    if not tz_config:
        return {"error": "Timezone not found", "status": 404}
    
    try:
        tz = pytz.timezone(tz_config["timezone"])
        current_time = datetime.now(tz)
        
        return {
            "name": tz_config["name"],
            "timezone": tz_config["timezone"],
            "offset": tz_config["offset"],
            "city": tz_config["city"],
            "region": tz_config["region"],
            "time_24h": current_time.strftime("%H:%M:%S"),
            "time_12h": current_time.strftime("%I:%M:%S %p"),
            "date": current_time.strftime("%A, %d %B %Y"),
            "date_short": current_time.strftime("%d-%m-%Y"),
            "iso": current_time.isoformat(),
        }
    except Exception as e:
        return {"error": str(e), "status": 500}

@app.get("/api/clock/config")
def get_clock_config():
    """Get clock configuration"""
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "config": CLOCK_CONFIG,
        "available_timezones": len(TIMEZONES),
    }

@app.get("/api/clock/local")
def get_local_time():
    """Get local time (WIB - Asia/Jakarta)"""
    tz = pytz.timezone("Asia/Jakarta")
    current_time = datetime.now(tz)
    
    return {
        "name": "Local Time (WIB)",
        "timezone": "Asia/Jakarta",
        "offset": "UTC+7",
        "city": "Jakarta",
        "time_24h": current_time.strftime("%H:%M:%S"),
        "time_12h": current_time.strftime("%I:%M:%S %p"),
        "date": current_time.strftime("%A, %d %B %Y"),
        "iso": current_time.isoformat(),
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
