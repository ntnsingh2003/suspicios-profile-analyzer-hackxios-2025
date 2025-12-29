# Deployment Guide: Suspicious Profile Analyzer

## 🚀 Complete Deployment Process

This project uses a **separated architecture**:
- **Frontend**: Deployed on Vercel (static hosting)
- **Backend**: Deployed on Render/Railway/Fly.io (ML dependencies support)

### Step 1: Deploy Backend to Render

**Option A: Using Render Dashboard**
1. Go to [render.com](https://render.com) and sign up/login
2. Click "New" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: `suspicious-profile-analyzer-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `cd backend && python main.py`
   - **Plan**: Free (sufficient for hackathon demo)
5. Click "Create Web Service"
6. **Note your backend URL**: `https://suspicious-profile-analyzer-backend.onrender.com`

**Option B: Using render.yaml (Infrastructure as Code)**
1. The `render.yaml` file is already configured
2. Connect your repo to Render
3. It will automatically deploy using the configuration

### Step 2: Deploy Frontend to Vercel

1. **Connect Repository**:
   - Go to [vercel.com/dashboard](https://vercel.com/dashboard)
   - Click "New Project" → Import your GitHub repo
   - **Framework Preset**: "Create React App"
   - **Root Directory**: `./` (keep default)
   - **Build Command**: `cd frontend && npm run build`
   - **Output Directory**: `frontend/build`

2. **Configure Environment Variables**:
   - In Vercel dashboard → Project Settings → Environment Variables
   - Add: `REACT_APP_API_BASE_URL` = `https://your-backend-url.onrender.com`
   - **Important**: Replace with your actual Render backend URL
   - Click "Save" and redeploy

### Step 3: Test Complete Integration

1. **Backend Health Check**:
   ```bash
   curl https://your-backend-url.onrender.com/
   ```

2. **Frontend Test**:
   - Visit your Vercel URL
   - Click "Load Legitimate Profile" demo button
   - Click "Analyze Profile for Threats"
   - Should see risk assessment results

### Alternative Backend Platforms

**Railway** (Recommended for ease):
```bash
# Install Railway CLI
npm install -g @railway/cli

# Deploy
railway login
railway init
railway up
```

**Fly.io** (Docker-based):
```bash
# Install Fly CLI
# Create fly.toml configuration
fly launch --no-deploy
fly deploy
```
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