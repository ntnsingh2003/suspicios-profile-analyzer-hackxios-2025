# Quick Deployment Checklist

## ✅ Pre-Deployment Checklist

- [ ] Backend runs locally (`cd backend && python main.py`)
- [ ] Frontend runs locally (`cd frontend && npm start`)
- [ ] Both servers communicate (test demo buttons)
- [ ] All files committed to Git
- [ ] Repository pushed to GitHub

## 🚀 Deployment Steps

### 1. Deploy Backend (Choose One Platform)

**Render (Recommended - Free Tier)**
1. Go to [render.com](https://render.com)
2. New → Web Service → Connect GitHub repo
3. Settings:
   - Build: `pip install -r requirements.txt`
   - Start: `cd backend && python main.py`
4. Copy your backend URL: `https://[your-service].onrender.com`

**Railway (Alternative)**
```bash
npm install -g @railway/cli
railway login
railway init
railway up
```

### 2. Deploy Frontend

**Vercel**
1. Go to [vercel.com](https://vercel.com)
2. New Project → Import GitHub repo
3. Framework: Create React App
4. Build: `cd frontend && npm run build`
5. Output: `frontend/build`
6. Environment Variables:
   - `REACT_APP_API_BASE_URL` = `https://[your-backend].onrender.com`

### 3. Test Deployment

1. Visit your Vercel URL
2. Click "Load Legitimate Profile"
3. Click "Analyze Profile for Threats"
4. Verify results appear

## 🔧 Troubleshooting

**Backend Issues:**
- Check Render logs for Python errors
- Verify requirements.txt includes all dependencies
- Ensure PORT environment variable is handled

**Frontend Issues:**
- Check browser console for API errors
- Verify REACT_APP_API_BASE_URL is set correctly
- Ensure CORS allows your frontend domain

**Connection Issues:**
- Test backend directly: `curl https://your-backend.onrender.com/`
- Check network tab in browser dev tools
- Verify environment variables are deployed

## 📱 Demo URLs

After deployment, you'll have:
- **Frontend**: `https://suspicious-profile-analyzer.vercel.app`
- **Backend**: `https://suspicious-profile-analyzer-backend.onrender.com`
- **API Docs**: `https://suspicious-profile-analyzer-backend.onrender.com/docs`

Ready for hackathon presentation! 🎉