# Risk Scoring Design: Suspicious Profile Analyzer

## Explainable Risk Scoring System

### Core Principle: No Black Box Logic
Every risk score must be traceable to specific, understandable factors. Users see exactly why a profile was flagged, enabling informed decision-making and security awareness learning.

## Input Factors

### Profile Metadata Analysis (30 points maximum)
- **Account Age**: New accounts (< 30 days) receive higher risk scores
- **Follower Ratios**: Suspicious following patterns (following thousands, few followers)
- **Profile Completeness**: Incomplete profiles indicate potential fake accounts
- **Posting Behavior**: Abnormally high or low posting frequency patterns

### Content Pattern Detection (30 points maximum)  
- **Financial Language**: Urgent money requests, wire transfer mentions, emergency appeals
- **Personal Information Requests**: SSN, banking details, password solicitation
- **Romance Scam Patterns**: Emotional manipulation combined with financial requests
- **Urgency Indicators**: Multiple pressure tactics and time-sensitive language

### Behavioral Analysis (40 points maximum)
- **ML Risk Probability**: Random Forest classifier output based on behavioral patterns
- **Feature Importance**: Account age, follower ratios, posting frequency, profile completeness
- **Confidence Weighting**: ML predictions weighted by model confidence scores

## Weighting Logic

### Rule-Based Component (60% of total score)
```
Profile Metadata Risk (0-30 points):
- New account (< 30 days): +25 points
- Suspicious follower ratio: +20 points  
- Incomplete profile: +12 points
- Abnormal posting frequency: +15 points

Content Pattern Risk (0-30 points):
- Financial request language: +20 points
- Personal info solicitation: +18 points
- Romance scam patterns: +22 points
- Multiple urgency indicators: +10 points

Rule Score = min(60, Profile Risk + Content Risk)
```

### ML Component (40% of total score)
```
Behavioral Risk (0-40 points):
- Random Forest probability × 40
- Weighted by model confidence
- Feature importance provides explanation ranking

ML Score = RF_Probability × 40 × Confidence_Factor
```

### Final Score Calculation
```
Total Risk Score = min(100, Rule Score + ML Score)
```

## Score Ranges and Risk Categories

### 0-20: Minimal Risk (Green)
- **Interpretation**: Profile shows normal characteristics with no significant red flags
- **Recommended Actions**: Standard monitoring, no special precautions needed
- **User Guidance**: "This profile appears legitimate based on available information"

### 21-40: Low Risk (Blue)  
- **Interpretation**: Some minor concerns but likely legitimate user
- **Recommended Actions**: Standard security protocols, automated logging increased
- **User Guidance**: "Exercise normal caution when interacting with this profile"

### 41-60: Medium Risk (Yellow)
- **Interpretation**: Multiple concerning patterns detected, enhanced scrutiny warranted
- **Recommended Actions**: Enhanced monitoring enabled, manual review triggered
- **User Guidance**: "Be cautious - this profile shows some suspicious characteristics"

### 61-80: High Risk (Orange)
- **Interpretation**: Strong indicators of malicious intent, user warnings recommended  
- **Recommended Actions**: Manual review triggered, user warning recommended, enhanced monitoring
- **User Guidance**: "High risk detected - avoid sharing personal information or money"

### 81-100: Critical Risk (Red)
- **Interpretation**: Severe threat indicators, immediate action required
- **Recommended Actions**: Immediate account restriction recommended, manual security review required
- **User Guidance**: "Critical threat detected - do not interact, report immediately"

## Example Explanation Output

### High-Risk Romance Scam Profile (Score: 87)
```json
{
  "risk_score": 87,
  "risk_level": "Critical Risk",
  "confidence": 0.92,
  "explanations": [
    "Account created 7 days ago (new accounts are high risk)",
    "Messages contain financial requests and money transfer language", 
    "Profile shows romance scam patterns (emotional manipulation + money requests)",
    "Following 500 accounts but only 2 followers (bot-like behavior)",
    "Multiple urgency indicators detected (pressure tactics)"
  ],
  "recommended_actions": [
    "Do not send money or share personal information",
    "Report this profile to platform administrators", 
    "Block all communication from this account"
  ],
  "confidence_explanation": "Multiple independent indicators confirm this assessment"
}
```

### Legitimate User Profile (Score: 15)
```json
{
  "risk_score": 15,
  "risk_level": "Minimal Risk", 
  "confidence": 0.78,
  "explanations": [
    "Account is 365 days old (established account)",
    "Balanced follower ratio indicates normal social activity",
    "Profile is complete with consistent information",
    "Messages contain normal social interaction patterns"
  ],
  "recommended_actions": [
    "Normal interaction is safe",
    "Continue standard security practices"
  ],
  "confidence_explanation": "Profile characteristics match legitimate user patterns"
}
```

## Transparency Requirements

### Factor Contribution Visibility
Users see exactly how each factor contributed to the final score:
- Rule-based factors show specific point values and reasoning
- ML factors show feature importance rankings with behavioral explanations
- Confidence scores indicate reliability of the assessment

### Plain Language Explanations
Technical factors translated to user-friendly language:
- "Follower ratio anomaly" becomes "Following many accounts but has few followers"
- "TF-IDF keyword match" becomes "Messages contain financial request language"
- "Random Forest probability 0.85" becomes "Behavioral patterns match known scammer profiles"

### Actionable Recommendations
Every risk assessment includes specific next steps:
- **Low Risk**: "Normal caution recommended"
- **Medium Risk**: "Ask for video call verification before sharing personal information"  
- **High Risk**: "Do not send money or share personal details"
- **Critical Risk**: "Block immediately and report to platform"

## Confidence Scoring

### Confidence Calculation
```
Rule_Confidence = Number of triggered rules / Total possible rules
ML_Confidence = Random Forest prediction probability
Agreement = 1 - |Rule_Normalized - ML_Normalized|
Final_Confidence = 0.6 + (0.4 × Agreement)
```

### Confidence Interpretation
- **0.85-1.0**: "Multiple independent indicators confirm assessment"
- **0.70-0.84**: "Assessment based on established threat patterns"  
- **0.60-0.69**: "Limited data available, manual review recommended"

This scoring system ensures complete transparency while maintaining sophisticated threat detection capabilities suitable for hackathon demonstration and real-world deployment.