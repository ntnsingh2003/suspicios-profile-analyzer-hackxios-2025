# Deployment Guide: Suspicious Profile Analyzer

## 🚀 Frontend-Only Vercel Deployment

Due to ML dependencies exceeding Vercel's 250MB serverless limit, this project deploys the frontend on Vercel and requires a separate backend deployment.

### Vercel (Frontend Only)

1. **Connect Repository**:
   - Go to [vercel.com/dashboard](https://vercel.com/dashboard)
   - Click "New Project" → Import your GitHub repo
   - Framework: "Create React App"
   - Build Command: `npm run build`
   - Output Directory: `frontend/build`

### Backend Deployment (Required Separately)

**Recommended Platforms for ML Backend:**
- **Render**: Free tier supports up to 512MB
- **Railway**: Full ML stack support
- **Fly.io**: Docker-based deployment

**Backend Setup (Render Example)**:
1. Create Web Service on Render
2. Build Command: `pip install -r requirements.txt`
3. Start Command: `cd backend && python main.py`
4. Note your backend URL (e.g., `https://your-app.onrender.com`)

### Frontend Configuration

**Environment Variables for Vercel:**
1. In Vercel dashboard → Project Settings → Environment Variables
2. Add: `REACT_APP_API_BASE_URL` = `https://your-backend-url.com`
3. Redeploy frontend to apply changes

**Local Development:**
```bash
# Create frontend/.env.local
echo "REACT_APP_API_BASE_URL=http://localhost:8000" > frontend/.env.local
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