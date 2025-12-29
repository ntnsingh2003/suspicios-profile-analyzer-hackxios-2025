# Suspicious Profile Analyzer - Backend

Flask API for cybersecurity threat detection using explainable AI.

## 🚀 Quick Start

```bash
pip install -r requirements.txt
python main.py
```

Server runs on `http://localhost:8000`

## 📋 API Endpoints

- `GET /` - Health check
- `GET /demo-data` - Sample test profiles
- `POST /analyze-profile` - Analyze profile for threats

## 🔧 Deployment

### Render
1. Create Web Service
2. Root Directory: `backend`
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `gunicorn main:app --bind 0.0.0.0:$PORT`

### Railway
```bash
railway login
railway init
railway up
```

## 🎯 Tech Stack

- **Flask 2.3.3** - Web framework
- **Flask-CORS 4.0.0** - Cross-origin support  
- **gunicorn 20.1.0** - WSGI server
- **Python 3.11.9** - Runtime

## 🛡️ Threat Detection

The engine detects:
- Financial scam patterns
- Romance scam indicators
- Personal info requests
- Bot-like behavior
- Account age risks
- Suspicious activity patterns

All results are explainable with human-readable threat indicators.