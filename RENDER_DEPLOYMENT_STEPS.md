# 🚀 Render.com Backend Deployment Guide

## Step-by-Step Instructions

### 1. Prepare Repository
✅ **Already Done**: All files are ready for deployment
- `render.yaml` - Deployment configuration
- `requirements.txt` - Python dependencies
- `backend/main.py` - Application with PORT configuration
- CORS setup for production domains

### 2. Deploy to Render

**Go to Render.com and follow these steps:**

1. **Sign Up/Login**:
   - Go to [render.com](https://render.com)
   - Sign up with GitHub (recommended) or email

2. **Create New Web Service**:
   - Click "New +" button
   - Select "Web Service"
   - Choose "Build and deploy from a Git repository"

3. **Connect Repository**:
   - Connect your GitHub account if not already connected
   - Select your repository: `suspicious-profile-analyzer`
   - Click "Connect"

4. **Configure Service**:
   ```
   Name: suspicious-profile-analyzer-backend
   Environment: Python 3
   Region: Oregon (US West) - or closest to you
   Branch: main (or your default branch)
   
   Build Command: pip install -r requirements.txt
   Start Command: cd backend && python main.py
   
   Plan: Free (sufficient for hackathon demo)
   ```

5. **Environment Variables** (Optional - already configured in render.yaml):
   - `PORT`: 8000 (auto-configured by Render)
   - `PYTHON_VERSION`: 3.11.0

6. **Deploy**:
   - Click "Create Web Service"
   - Wait for deployment (5-10 minutes for first deploy)

### 3. Get Your Backend URL

After successful deployment, you'll get a URL like:
```
https://suspicious-profile-analyzer-backend.onrender.com
```

**Copy this URL** - you'll need it for frontend configuration.

### 4. Test Backend Deployment

Test these endpoints to verify deployment:

1. **Health Check**:
   ```
   GET https://your-backend-url.onrender.com/
   ```
   Should return: `{"message":"Suspicious Profile Analyzer API","status":"operational","version":"1.0.0"}`

2. **Demo Data**:
   ```
   GET https://your-backend-url.onrender.com/demo-data
   ```
   Should return sample profile data

3. **API Documentation**:
   ```
   https://your-backend-url.onrender.com/docs
   ```
   Should show FastAPI interactive documentation

### 5. Common Issues & Solutions

**Build Failures**:
- Check build logs in Render dashboard
- Verify all dependencies are in requirements.txt
- Ensure Python version compatibility

**Start Command Issues**:
- Make sure `cd backend && python main.py` is correct
- Check that main.py handles PORT environment variable

**Memory Issues**:
- Free tier has 512MB RAM limit
- Our ML model is optimized for this limit
- If issues occur, consider upgrading to Starter plan ($7/month)

### 6. Expected Deployment Timeline

- **Build Time**: 3-5 minutes (installing ML dependencies)
- **Start Time**: 30-60 seconds (loading ML model)
- **Cold Start**: 2-3 seconds for first request after idle
- **Response Time**: 200-500ms for subsequent requests

### 7. Monitoring

**Render Dashboard provides**:
- Real-time logs
- Performance metrics
- Deployment history
- Service health status

**Log into Render dashboard to monitor**:
- Build progress
- Application logs
- Error messages
- Performance metrics

---

## ✅ Next Steps After Backend Deployment

1. **Copy Backend URL** from Render dashboard
2. **Deploy Frontend** to Vercel with backend URL
3. **Test Complete Integration** end-to-end
4. **Ready for Hackathon Demo** 🎉

---

**Need Help?** Check the Render documentation or deployment logs for specific error messages.