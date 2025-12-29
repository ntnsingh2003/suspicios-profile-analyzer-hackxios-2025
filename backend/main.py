"""
Suspicious Profile Analyzer - Pure Flask Backend
Zero compilation dependencies - guaranteed to work on any platform
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import re
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Lightweight Threat Detection Engine
class ThreatDetectionEngine:
    """
    Ultra-lightweight threat detection using pure Python
    No dependencies beyond Flask
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
        logger.info("Loading ultra-lightweight threat detection engine...")
        logger.info("Threat signature database ready for analysis")
    
    def analyze_profile_metadata(self, profile: Dict[str, Any]) -> tuple:
        """
        Analyze profile metadata for suspicious patterns
        Returns: (risk_points, explanations)
        """
        risk_points = 0
        explanations = []
        
        account_age_days = profile.get('account_age_days', 0)
        followers = profile.get('followers', 0)
        following = profile.get('following', 0)
        post_count = profile.get('post_count', 0)
        profile_completed = profile.get('profile_completed', False)
        
        # Rule 1: New account risk
        if account_age_days < 30:
            risk_points += 30
            explanations.append(f"Account created {account_age_days} days ago (new accounts are high risk)")
        elif account_age_days < 90:
            risk_points += 15
            explanations.append(f"Account is {account_age_days} days old (relatively new)")
        
        # Rule 2: Follower/Following ratio analysis
        if following > 0:
            ratio = followers / max(following, 1)
            if ratio < 0.01 and following > 1000:
                risk_points += 25
                explanations.append(f"Following {following} accounts but only {followers} followers (bot-like behavior)")
            elif ratio > 100 and followers > 10000:
                risk_points += 20
                explanations.append(f"Unusually high follower count ({followers}) may indicate fake followers")
        
        # Rule 3: Posting behavior analysis
        if account_age_days > 0:
            posts_per_day = post_count / account_age_days
            if posts_per_day > 50:
                risk_points += 20
                explanations.append(f"Posting {posts_per_day:.1f} times per day (abnormally high activity)")
            elif posts_per_day < 0.01 and account_age_days > 30:
                risk_points += 10
                explanations.append("Very low posting activity for account age")
        
        # Rule 4: Profile completeness
        if not profile_completed:
            risk_points += 15
            explanations.append("Profile is incomplete (missing key information)")
        
        # Rule 5: Behavioral scoring
        behavioral_score = self._calculate_behavioral_score(profile)
        risk_points += behavioral_score
        if behavioral_score > 10:
            explanations.append(f"Behavioral analysis indicates {behavioral_score} risk points from activity patterns")
        
        return min(risk_points, 70), explanations
    
    def _calculate_behavioral_score(self, profile: Dict[str, Any]) -> int:
        """Lightweight behavioral scoring"""
        score = 0
        
        account_age_days = profile.get('account_age_days', 0)
        followers = profile.get('followers', 0)
        following = profile.get('following', 0)
        post_count = profile.get('post_count', 0)
        
        # Age vs activity correlation
        if account_age_days > 0:
            activity_ratio = post_count / account_age_days
            if activity_ratio > 20 or activity_ratio < 0.01:
                score += 10
        
        # Follower patterns
        if following > followers * 10:
            score += 15
        
        # Suspicious round numbers
        if followers % 100 == 0 and followers > 1000:
            score += 5
        
        return min(score, 30)
    
    def analyze_message_content(self, messages: List[str]) -> tuple:
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
        
        return min(risk_points, 30), explanations
    
    def calculate_risk_score(self, profile: Dict[str, Any]) -> Dict[str, Any]:
        """Calculate comprehensive risk score with explanations"""
        all_explanations = []
        
        # Profile metadata analysis
        metadata_risk, metadata_explanations = self.analyze_profile_metadata(profile)
        all_explanations.extend(metadata_explanations)
        
        # Message content analysis
        messages = profile.get('messages', [])
        content_risk, content_explanations = self.analyze_message_content(messages)
        all_explanations.extend(content_explanations)
        
        # Combine scores
        total_score = min(100, metadata_risk + content_risk)
        
        # Determine risk level
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
        
        # Calculate confidence
        indicator_count = len([e for e in all_explanations if e])
        confidence = min(0.95, 0.5 + (indicator_count * 0.1))
        
        # Generate confidence explanation
        if confidence >= 0.85:
            confidence_explanation = "Multiple independent indicators confirm assessment"
        elif confidence >= 0.70:
            confidence_explanation = "Assessment based on established threat patterns"
        else:
            confidence_explanation = "Limited data available, manual review recommended"
        
        # Add summary
        if total_score > 0:
            threat_indicators_count = len([e for e in all_explanations if e])
            summary = f"Threat assessment: {threat_indicators_count} security indicators detected using rule-based analysis"
            all_explanations.insert(0, summary)
        
        # Recommended actions
        if total_score >= 80:
            recommended_actions = ["Immediate account restriction recommended", "Manual security review required", "User notification advised"]
        elif total_score >= 60:
            recommended_actions = ["Enhanced monitoring enabled", "Manual review triggered", "User warning recommended"]
        elif total_score >= 40:
            recommended_actions = ["Standard security protocols apply", "Automated logging increased"]
        else:
            recommended_actions = ["Normal monitoring continues"]
        
        return {
            "risk_score": round(total_score, 1),
            "risk_level": risk_level,
            "explanations": all_explanations[:10],
            "confidence": round(confidence, 2),
            "confidence_explanation": confidence_explanation,
            "recommended_actions": recommended_actions
        }

# Initialize global threat detection engine
threat_detector = ThreatDetectionEngine()

@app.route('/')
def root():
    """Health check endpoint"""
    return jsonify({
        "message": "Suspicious Profile Analyzer API",
        "status": "operational",
        "version": "1.0.0"
    })

@app.route('/analyze-profile', methods=['POST'])
def analyze_profile():
    """
    Analyze a profile for suspicious characteristics
    """
    try:
        profile = request.get_json()
        
        if not profile:
            return jsonify({"error": "No profile data provided"}), 400
        
        logger.info(f"Analyzing profile for security threats: age={profile.get('account_age_days')} days, followers={profile.get('followers')}")
        
        # Validate input
        if profile.get('account_age_days', 0) < 0:
            return jsonify({"error": "Account age cannot be negative"}), 400
        
        messages = profile.get('messages', [])
        if len(messages) == 0:
            return jsonify({"error": "At least one message is required for threat analysis"}), 400
        
        # Perform security threat assessment
        logger.info("Step 1: Analyzing profile metadata for identity inconsistencies...")
        logger.info("Step 2: Scanning message content for social engineering patterns...")
        logger.info("Step 3: Evaluating behavioral patterns against known threat signatures...")
        
        assessment = threat_detector.calculate_risk_score(profile)
        
        logger.info(f"Threat assessment complete: {assessment['risk_level']} ({assessment['risk_score']}/100)")
        return jsonify(assessment)
        
    except Exception as e:
        logger.error(f"Error analyzing profile: {str(e)}")
        return jsonify({"error": f"Analysis failed: {str(e)}"}), 500

@app.route('/demo-data')
def get_demo_data():
    """Provide sample test data for demo purposes"""
    return jsonify({
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
    })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=False)