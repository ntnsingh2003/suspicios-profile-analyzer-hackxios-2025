"""
Suspicious Profile Analyzer - Lightweight FastAPI Backend
Simplified version for reliable deployment without heavy ML dependencies
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Dict, Tuple
import re
import logging
import math

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Suspicious Profile Analyzer",
    description="Explainable AI system for detecting fake and malicious online profiles",
    version="1.0.0"
)

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # React dev server
        "https://*.vercel.app",   # Vercel deployments
        "https://suspicious-profile-analyzer.vercel.app",  # Production domain
        "https://*.onrender.com", # Render deployments
        "https://*.railway.app",  # Railway deployments
        "https://*.fly.dev"       # Fly.io deployments
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input/Output Models
class ProfileData(BaseModel):
    account_age_days: int = Field(..., ge=0, description="Days since account creation")
    followers: int = Field(..., ge=0, description="Number of followers")
    following: int = Field(..., ge=0, description="Number of accounts following")
    post_count: int = Field(..., ge=0, description="Total posts made")
    profile_completed: bool = Field(..., description="Whether profile is complete")
    messages: List[str] = Field(..., description="Sample messages from the profile")

class RiskAssessment(BaseModel):
    risk_score: float = Field(..., ge=0, le=100, description="Risk score 0-100")
    risk_level: str = Field(..., description="Risk category: Minimal/Low/Medium/High/Critical Risk")
    explanations: List[str] = Field(..., description="Human-readable security threat indicators")
    confidence: float = Field(..., ge=0, le=1, description="Assessment reliability score")
    confidence_explanation: str = Field(..., description="What the confidence score means")
    recommended_actions: List[str] = Field(..., description="Security response recommendations")

# Lightweight Rule-Based Detection Engine
class ThreatDetectionEngine:
    """
    Lightweight threat detection using rule-based analysis
    No heavy ML dependencies - pure Python logic
    """
    
    # Financial scam keywords (high precision patterns)
    FINANCIAL_KEYWORDS = [
        r'\b(send|wire|transfer)\s+(money|cash|funds)\b',
        r'\b(western\s+union|moneygram|bitcoin|paypal)\b',
        r'\b(emergency|urgent|immediate)\s+(help|assistance|money|funds)\b',
        r'\b(investment|trading|profit|returns)\s+(opportunity|guaranteed)\b',
        r'\b(lottery|winner|prize|inheritance)\b'
    ]
    
    # Personal information solicitation patterns
    PERSONAL_INFO_KEYWORDS = [
        r'\b(ssn|social\s+security|bank\s+account|routing\s+number)\b',
        r'\b(credit\s+card|debit\s+card|pin\s+code|password)\b',
        r'\b(full\s+name|address|phone\s+number|date\s+of\s+birth)\b'
    ]
    
    # Romance scam patterns
    ROMANCE_SCAM_KEYWORDS = [
        r'\b(love|darling|honey|sweetheart)\b.*\b(money|help|emergency)\b',
        r'\b(military|deployed|overseas|doctor|engineer)\b.*\b(money|funds)\b',
        r'\b(trust|faith|god)\b.*\b(send|transfer|help)\b'
    ]
    
    def __init__(self):
        logger.info("Initializing Suspicious Profile Analyzer - Cybersecurity Threat Detection System")
        logger.info("Loading lightweight threat detection engine...")
        logger.info("Threat signature database ready for analysis")
    
    def analyze_profile_metadata(self, profile: ProfileData) -> Tuple[int, List[str]]:
        """
        Analyze profile metadata for suspicious patterns
        Returns: (risk_points, explanations)
        """
        risk_points = 0
        explanations = []
        
        # Rule 1: New account risk (accounts < 30 days are high risk)
        if profile.account_age_days < 30:
            risk_points += 30
            explanations.append(f"Account created {profile.account_age_days} days ago (new accounts are high risk)")
        elif profile.account_age_days < 90:
            risk_points += 15
            explanations.append(f"Account is {profile.account_age_days} days old (relatively new)")
        
        # Rule 2: Follower/Following ratio analysis
        if profile.following > 0:
            ratio = profile.followers / max(profile.following, 1)
            if ratio < 0.01 and profile.following > 1000:  # Following many, few followers
                risk_points += 25
                explanations.append(f"Following {profile.following} accounts but only {profile.followers} followers (bot-like behavior)")
            elif ratio > 100 and profile.followers > 10000:  # Suspiciously high follower count
                risk_points += 20
                explanations.append(f"Unusually high follower count ({profile.followers}) may indicate fake followers")
        
        # Rule 3: Posting behavior analysis
        if profile.account_age_days > 0:
            posts_per_day = profile.post_count / profile.account_age_days
            if posts_per_day > 50:  # Excessive posting
                risk_points += 20
                explanations.append(f"Posting {posts_per_day:.1f} times per day (abnormally high activity)")
            elif posts_per_day < 0.01 and profile.account_age_days > 30:  # Inactive account
                risk_points += 10
                explanations.append("Very low posting activity for account age")
        
        # Rule 4: Profile completeness
        if not profile.profile_completed:
            risk_points += 15
            explanations.append("Profile is incomplete (missing key information)")
        
        # Rule 5: Behavioral scoring (lightweight ML substitute)
        behavioral_score = self._calculate_behavioral_score(profile)
        risk_points += behavioral_score
        if behavioral_score > 10:
            explanations.append(f"Behavioral analysis indicates {behavioral_score} risk points from activity patterns")
        
        return min(risk_points, 70), explanations  # Cap at 70 points
    
    def _calculate_behavioral_score(self, profile: ProfileData) -> int:
        """
        Lightweight behavioral scoring without ML dependencies
        """
        score = 0
        
        # Age vs activity correlation
        if profile.account_age_days > 0:
            activity_ratio = profile.post_count / profile.account_age_days
            if activity_ratio > 20 or activity_ratio < 0.01:
                score += 10
        
        # Follower patterns
        if profile.following > profile.followers * 10:  # Following way more than followers
            score += 15
        
        # Suspicious round numbers (often fake)
        if profile.followers % 100 == 0 and profile.followers > 1000:
            score += 5
        
        return min(score, 30)  # Cap behavioral score
    
    def analyze_message_content(self, messages: List[str]) -> Tuple[int, List[str]]:
        """
        Analyze message content for scam patterns
        Returns: (risk_points, explanations)
        """
        risk_points = 0
        explanations = []
        
        # Combine all messages for analysis
        combined_text = " ".join(messages).lower()
        
        # Check for financial scam patterns
        for pattern in self.FINANCIAL_KEYWORDS:
            if re.search(pattern, combined_text, re.IGNORECASE):
                risk_points += 25
                explanations.append("Messages contain financial requests or money transfer language")
                break
        
        # Check for personal information solicitation
        for pattern in self.PERSONAL_INFO_KEYWORDS:
            if re.search(pattern, combined_text, re.IGNORECASE):
                risk_points += 20
                explanations.append("Messages request personal or financial information")
                break
        
        # Check for romance scam patterns
        for pattern in self.ROMANCE_SCAM_KEYWORDS:
            if re.search(pattern, combined_text, re.IGNORECASE):
                risk_points += 30
                explanations.append("Messages show romance scam patterns (emotional manipulation + money requests)")
                break
        
        # Check for urgency indicators
        urgency_patterns = [r'\burgent\b', r'\bemergency\b', r'\bquickly\b', r'\basap\b', r'\bimmediately\b']
        urgency_count = sum(1 for pattern in urgency_patterns if re.search(pattern, combined_text, re.IGNORECASE))
        if urgency_count >= 2:
            risk_points += 15
            explanations.append("Messages contain multiple urgency indicators (pressure tactics)")
        
        return min(risk_points, 30), explanations  # Cap at 30 points
    
    def calculate_risk_score(self, profile: ProfileData) -> RiskAssessment:
        """
        Calculate comprehensive risk score with explanations
        """
        all_explanations = []
        
        # Profile metadata analysis
        metadata_risk, metadata_explanations = self.analyze_profile_metadata(profile)
        all_explanations.extend(metadata_explanations)
        
        # Message content analysis
        content_risk, content_explanations = self.analyze_message_content(profile.messages)
        all_explanations.extend(content_explanations)
        
        # Combine scores
        total_score = min(100, metadata_risk + content_risk)
        
        # Determine risk level using industry-standard 5-level classification
        if total_score < 20:
            risk_level = "Minimal Risk"
        elif total_score < 40:
            risk_level = "Low Risk"
        elif total_score < 60:
            risk_level = "Medium Risk"
        elif total_score < 80:
            risk_level = "High Risk"
        else:
            risk_level = "Critical Risk"
        
        # Calculate confidence based on number of indicators
        indicator_count = len([e for e in all_explanations if e])
        confidence = min(0.95, 0.5 + (indicator_count * 0.1))  # More indicators = higher confidence
        
        # Generate confidence explanation
        if confidence >= 0.85:
            confidence_explanation = "Multiple independent indicators confirm assessment"
        elif confidence >= 0.70:
            confidence_explanation = "Assessment based on established threat patterns"
        else:
            confidence_explanation = "Limited data available, manual review recommended"
        
        # Add security-focused summary explanation
        if total_score > 0:
            threat_indicators_count = len([e for e in all_explanations if e])
            summary = f"Threat assessment: {threat_indicators_count} security indicators detected using rule-based analysis"
            all_explanations.insert(0, summary)
        
        # Add recommended security actions based on risk level
        recommended_actions = []
        if total_score >= 80:
            recommended_actions = ["Immediate account restriction recommended", "Manual security review required", "User notification advised"]
        elif total_score >= 60:
            recommended_actions = ["Enhanced monitoring enabled", "Manual review triggered", "User warning recommended"]
        elif total_score >= 40:
            recommended_actions = ["Standard security protocols apply", "Automated logging increased"]
        else:
            recommended_actions = ["Normal monitoring continues"]
        
        return RiskAssessment(
            risk_score=round(total_score, 1),
            risk_level=risk_level,
            explanations=[exp for exp in all_explanations if exp][:10],  # Limit to top 10
            confidence=round(confidence, 2),
            confidence_explanation=confidence_explanation,
            recommended_actions=recommended_actions
        )

# Initialize global threat detection engine
threat_detector = ThreatDetectionEngine()

@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "Suspicious Profile Analyzer API",
        "status": "operational",
        "version": "1.0.0"
    }

@app.post("/analyze-profile", response_model=RiskAssessment)
async def analyze_profile(profile: ProfileData):
    """
    Analyze a profile for suspicious characteristics
    
    This endpoint implements rule-based threat detection:
    - Profile metadata analysis for suspicious patterns
    - Message content analysis for scam indicators
    - Returns explainable risk score with human-readable factors
    """
    try:
        logger.info(f"Analyzing profile for security threats: age={profile.account_age_days} days, followers={profile.followers}")
        
        # Validate input
        if profile.account_age_days < 0:
            raise HTTPException(status_code=400, detail="Account age cannot be negative")
        
        if len(profile.messages) == 0:
            raise HTTPException(status_code=400, detail="At least one message is required for threat analysis")
        
        # Perform security threat assessment
        logger.info("Step 1: Analyzing profile metadata for identity inconsistencies...")
        logger.info("Step 2: Scanning message content for social engineering patterns...")
        logger.info("Step 3: Evaluating behavioral patterns against known threat signatures...")
        
        assessment = threat_detector.calculate_risk_score(profile)
        
        logger.info(f"Threat assessment complete: {assessment.risk_level} ({assessment.risk_score}/100)")
        return assessment
        
    except Exception as e:
        logger.error(f"Error analyzing profile: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.get("/demo-data")
async def get_demo_data():
    """
    Provide sample test data for demo purposes
    """
    return {
        "legitimate_profile": {
            "account_age_days": 365,
            "followers": 250,
            "following": 180,
            "post_count": 120,
            "profile_completed": True,
            "messages": [
                "Thanks for connecting! Looking forward to networking.",
                "Great article you shared about industry trends."
            ]
        },
        "suspicious_profile": {
            "account_age_days": 45,
            "followers": 15,
            "following": 800,
            "post_count": 200,
            "profile_completed": False,
            "messages": [
                "Hello! I'm new to this platform.",
                "Looking to connect with professionals in your field.",
                "Would love to discuss potential opportunities."
            ]
        },
        "romance_scam_profile": {
            "account_age_days": 7,
            "followers": 2,
            "following": 500,
            "post_count": 50,
            "profile_completed": False,
            "messages": [
                "My darling, I love you so much already.",
                "I am engineer working on oil rig, need emergency money.",
                "Trust me honey, send Western Union transfer immediately."
            ]
        }
    }

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)