# Airport AI Operations Hub

A full-stack prototype for an Airport AI Operations dashboard with a Python FastAPI backend and a browser-based frontend.

## Features

- Dashboard overview with KPI cards
- Incident management list
- Approval queue
- Agent registry with capabilities
- Network/VLAN and power monitoring mock data
- Real API for frontend consumption

## Run locally

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the backend:
   ```bash
   cd backend
   uvicorn app:app --host 0.0.0.0 --port 8000 --reload
   ```

4. Open the frontend:
   ```bash
   python -m http.server 8080 --directory frontend
   ```

5. Visit:
   ```text
   http://localhost:8080
   ```

## API endpoints

- `GET /api/health`
- `GET /api/overview`
- `GET /api/agents`
- `GET /api/incidents`
- `GET /api/approvals`
- `GET /api/network`
- `GET /api/power`
- `GET /api/maintenance`
- `GET /api/users`

## Notes

This is a mock operational dashboard intended for internal demo or LAN deployment, not a production control plane.
