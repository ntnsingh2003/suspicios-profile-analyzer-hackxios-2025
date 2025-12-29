# Suspicious Profile Analyzer - Setup Guide

## 🚀 Quick Start (5 minutes)

### Prerequisites
- **Python 3.8+** (for backend)
- **Node.js 16+** (for frontend)
- **npm** (comes with Node.js)

### Step 1: Backend Setup

1. **Open a terminal and navigate to the backend directory**:
   ```bash
   cd backend
   ```

2. **Install Python dependencies**:
   ```bash
   pip install fastapi uvicorn pydantic scikit-learn numpy python-multipart textblob
   ```

3. **Start the backend server**:
   ```bash
   python main.py
   ```

   You should see:
   ```
   INFO: ML model trained on 1000 synthetic profiles
   INFO: Uvicorn running on http://0.0.0.0:8000
   ```

   ✅ **Backend is ready at http://localhost:8000**

### Step 2: Frontend Setup

1. **Open a NEW terminal and navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install Node.js dependencies**:
   ```bash
   npm install
   ```

3. **Start the React development server**:
   ```bash
   npm start
   ```

   The browser should automatically open to http://localhost:3000

   ✅ **Frontend is ready at http://localhost:3000**

## 🧪 Testing the System

### Quick Demo Test

1. **Open http://localhost:3000 in your browser**
2. **Click "Load Romance Scam Profile"** - this loads a high-risk test profile
3. **Click "Analyze Profile"** - you should see:
   - Risk Score: ~85-100 (High Risk)
   - Multiple explanations like "Account created X days ago", "Messages contain financial requests"
   - Confidence score around 85%

### API Testing (Optional)

Test the backend API directly:

```bash
# Health check
curl http://localhost:8000/

# Get demo data
curl http://localhost:8000/demo-data

# Analyze a suspicious profile
curl -X POST "http://localhost:8000/analyze-profile" \
  -H "Content-Type: application/json" \
  -d '{
    "account_age_days": 15,
    "followers": 5,
    "following": 2000,
    "post_count": 800,
    "profile_completed": false,
    "messages": [
      "Hello dear, I am military doctor deployed overseas.",
      "I need urgent help to transfer my inheritance money."
    ]
  }'
```

## 🎯 Demo Scenarios

### Scenario 1: Legitimate Profile
- Click "Load Legitimate Profile"
- Should show Risk Score: 0-30 (Genuine)
- Minimal risk factors detected

### Scenario 2: Suspicious Profile  
- Click "Load Suspicious Profile"
- Should show Risk Score: 31-60 (Suspicious)
- Flags bot-like behavior and new account

### Scenario 3: Romance Scam
- Click "Load Romance Scam Profile"
- Should show Risk Score: 61-100 (High Risk)
- Detects emotional manipulation + financial requests

## 🔧 Troubleshooting

### Backend Issues

**"ModuleNotFoundError: No module named 'fastapi'"**
```bash
pip install fastapi uvicorn pydantic scikit-learn numpy python-multipart textblob
```

**"Port 8000 already in use"**
- Kill any existing processes on port 8000
- Or modify `main.py` to use a different port

**Scikit-learn compilation errors on Windows**
```bash
pip install --only-binary=all scikit-learn
```

### Frontend Issues

**"npm: command not found"**
- Install Node.js from https://nodejs.org/

**"Port 3000 already in use"**
- The React server will automatically suggest port 3001
- Or set PORT=3001 before running `npm start`

**CORS errors in browser**
- Ensure backend is running on port 8000
- Check that CORS middleware is enabled in `main.py`

## 📊 Expected Results

### Legitimate Profile Analysis
```json
{
  "risk_score": 15.2,
  "risk_level": "Genuine", 
  "explanations": [
    "Risk assessment based on 1 factors",
    "Account age pattern contributes to risk assessment"
  ],
  "confidence": 0.78
}
```

### Romance Scam Profile Analysis
```json
{
  "risk_score": 95.0,
  "risk_level": "High Risk",
  "explanations": [
    "Risk assessment based on 6 factors (primarily rule-based indicators)",
    "Account created 7 days ago (new accounts are high risk)",
    "Following 500 accounts but only 2 followers (bot-like behavior)",
    "Messages show romance scam patterns (emotional manipulation + money requests)",
    "Messages contain financial requests or money transfer language"
  ],
  "confidence": 0.92
}
```

## 🎯 Key Features to Demonstrate

1. **Explainable AI**: Every risk score comes with clear explanations
2. **Hybrid Approach**: 60% rule-based + 40% ML for transparency
3. **Real-time Analysis**: Results in under 3 seconds
4. **Multiple Risk Categories**: Genuine, Suspicious, High Risk
5. **Confidence Scoring**: Shows reliability of the assessment

## 🚀 Production Deployment (Future)

For production deployment, you would:

1. **Backend**: Deploy FastAPI with Gunicorn/Docker
2. **Frontend**: Build with `npm run build` and serve with Nginx
3. **Database**: Add PostgreSQL for profile storage
4. **Monitoring**: Add logging, metrics, and alerting
5. **Security**: Add authentication, rate limiting, input validation

## 📝 Architecture Summary

```
User Browser (React) → FastAPI Backend → ML/NLP Engine → Risk Assessment
     ↓                      ↓                ↓              ↓
  Port 3000            Port 8000      scikit-learn    Explainable Score
```

**Tech Stack**:
- **Frontend**: React + TypeScript + CSS
- **Backend**: Python + FastAPI + Pydantic
- **ML/AI**: scikit-learn + TextBlob + NumPy
- **Approach**: Hybrid rule-based + Random Forest

---

**🎉 You're ready to demo the Suspicious Profile Analyzer!**

The system demonstrates explainable AI for cybersecurity, showing how transparency and user trust can be prioritized without sacrificing effectiveness.