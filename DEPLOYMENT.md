# Deployment Guide: Suspicious Profile Analyzer

## 🚀 Clean Architecture

This project uses a **separated architecture**:
- **Frontend**: React TypeScript → Deploy to Vercel
- **Backend**: Flask Python → Deploy to Render/Railway

## 📁 Project Structure

```
suspicious-profile-analyzer/
├── frontend/                # React TypeScript application
│   ├── src/
│   ├── public/
│   └── package.json
├── backend/                 # Flask Python API
│   ├── main.py             # Flask application
│   ├── requirements.txt    # Python dependencies
│   ├── Procfile           # Deployment configuration
│   └── runtime.txt        # Python version
├── .kiro/                  # Kiro planning documents
├── HERO/                   # Strategic summaries
└── README.md
```

## 🎯 Backend Deployment (Flask)

### Deploy to Render

1. **Create Web Service**:
   - Go to [render.com](https://render.com)
   - New → Web Service → Connect GitHub repo
   - **Root Directory**: `backend`

2. **Configuration**:
   ```
   Name: suspicious-profile-analyzer-backend
   Environment: Python 3
   Root Directory: backend
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn main:app --bind 0.0.0.0:$PORT
   Plan: Free
   ```

3. **Get Backend URL**: `https://[your-service].onrender.com`

### Backend Stack
- **Flask 2.3.3** - Web framework
- **Flask-CORS 4.0.0** - Cross-origin support
- **gunicorn 20.1.0** - WSGI server
- **Python 3.11.9** - Runtime

## 🎯 Frontend Deployment (React)

### Deploy to Vercel

1. **Create Project**:
   - Go to [vercel.com](https://vercel.com)
   - New Project → Import GitHub repo
   - **Root Directory**: `frontend`

2. **Configuration**:
   ```
   Framework: Create React App
   Root Directory: frontend
   Build Command: npm run build
   Output Directory: build
   ```

3. **Environment Variables**:
   ```
   REACT_APP_API_BASE_URL = https://[your-backend].onrender.com
   ```

## 🧪 Testing Integration

1. **Backend Health Check**:
   ```bash
   curl https://your-backend-url.onrender.com/
   ```

2. **Frontend Test**:
   - Visit your Vercel URL
   - Click "Load Romance Scam Profile"
   - Click "Analyze Profile for Threats"
   - Verify risk assessment results

## 🔧 Local Development

### Backend
```bash
cd backend
pip install -r requirements.txt
python main.py
# Server runs on http://localhost:8000
```

### Frontend
```bash
cd frontend
echo "REACT_APP_API_BASE_URL=http://localhost:8000" > .env.local
npm install
npm start
# App runs on http://localhost:3000
```

---

**Ready for hackathon demonstration!** 🎉
# - Project name: suspicious-profile-analyzer
# - Directory: ./
# - Override settings? N
```

### Project Structure for Vercel

```
suspicious-profile-analyzer/
├── api/                     # Serverless API functions
│   ├── analyze-profile.py   # Profile analysis endpoint
│   └── demo-data.py         # Demo data endpoint
├── frontend/                # React application
│   ├── src/
│   ├── public/
│   └── package.json
├── backend/                 # FastAPI source code
│   ├── main.py
│   └── requirements.txt
├── vercel.json             # Vercel configuration
├── package.json            # Root package.json for build
└── requirements.txt        # Python dependencies
```

### Vercel Configuration

The `vercel.json` file configures:
- **Python API Functions**: Serverless functions for backend logic
- **Static Build**: React frontend build process
- **Routing**: API routes (`/api/*`) and static file serving
- **CORS**: Cross-origin resource sharing for API access

### API Endpoints

Once deployed, your API will be available at:
- `https://your-project.vercel.app/api/analyze-profile` - Profile analysis
- `https://your-project.vercel.app/api/demo-data` - Demo data

### Frontend

The React application will be served at:
- `https://your-project.vercel.app/` - Main application

### Troubleshooting

#### Common Issues

1. **Build Failures**:
   - Check that all dependencies are listed in `requirements.txt`
   - Ensure Python version compatibility (3.9+)
   - Verify frontend builds locally: `cd frontend && npm run build`

2. **API Errors**:
   - Check Vercel function logs in dashboard
   - Verify CORS configuration for your domain
   - Test API endpoints individually

3. **Import Errors**:
   - Ensure all Python modules are properly imported
   - Check that backend code is accessible from API functions

#### Vercel Limits

- **Function Timeout**: 10 seconds (Hobby plan)
- **Function Size**: 50MB unzipped
- **Bandwidth**: 100GB/month (Hobby plan)

### Custom Domain (Optional)

1. **Add Domain**:
   - Go to Project Settings → Domains
   - Add your custom domain
   - Configure DNS records as instructed

2. **SSL Certificate**:
   - Automatically provisioned by Vercel
   - No additional configuration needed

### Monitoring

- **Analytics**: Available in Vercel dashboard
- **Function Logs**: Real-time logs for debugging
- **Performance**: Core Web Vitals tracking

## 🔧 Local Development

### Backend
```bash
cd backend
pip install -r requirements.txt
python main.py
# Server runs on http://localhost:8000
```

### Frontend
```bash
cd frontend
npm install
npm start
# App runs on http://localhost:3000
```

## 📊 Production Considerations

### Performance
- API functions are serverless (cold start ~1-2 seconds)
- Frontend is served via Vercel's global CDN
- ML model loads on first request (cached afterward)

### Security
- CORS configured for production domains
- No sensitive data stored in client-side code
- API rate limiting handled by Vercel

### Scaling
- Automatic scaling based on traffic
- No server management required
- Pay-per-use pricing model

---

**Ready for hackathon judges and live demonstrations!**