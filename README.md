# Suspicious Profile Analyzer

**Explainable AI cybersecurity system for detecting fake and malicious online profiles**

## Project Overview

The Suspicious Profile Analyzer addresses the $1.3B+ annual problem of online profile fraud through transparent, explainable AI detection. Unlike black-box solutions, our system provides clear explanations for every risk assessment, enabling users to understand threats and make informed decisions.

The system analyzes profile metadata, behavioral patterns, and message content to generate risk scores from 0-100 with human-readable explanations of contributing factors.

## Planning-First Development Approach

This project was developed using structured planning methodology to ensure clarity, feasibility, and focused execution within hackathon constraints. Rather than jumping directly into coding, we invested upfront time in systematic analysis:

- **Problem Definition**: Quantified the threat landscape and identified why current detection systems fail
- **Threat Modeling**: Categorized five distinct profile types with specific attack vectors and impact assessment  
- **User Personas**: Developed three detailed personas driving every design decision from API structure to explanation language
- **Feature Prioritization**: Used time/complexity/impact analysis to focus on deliverable MVP within 24-48 hours
- **ML Decision Framework**: Systematic evaluation of rule-based vs ML vs hybrid approaches across multiple criteria
- **Explainable Risk Scoring**: Designed transparent scoring system rejecting black-box approaches

This planning-first approach prevented common hackathon pitfalls of scope creep and over-engineering while ensuring judge-ready demonstrations.

## System Architecture

### High-Level Data Flow
```
User → React UI → FastAPI → ML/NLP Engine → Risk Scoring → Dashboard
```

### Core Components
- **Profile Analyzer**: Orchestrates analysis pipeline and aggregates results
- **Metadata Validator**: Rule-based analysis of account age, follower ratios, profile completeness
- **Content Classifier**: NLP analysis using TF-IDF + keyword rules for scam pattern detection
- **Risk Scorer**: Combines rule-based (60%) and ML (40%) outputs with explainable weighting
- **Explainability Module**: Generates human-readable explanations for all risk factors

### Technology Stack
- **Backend**: Python + FastAPI for rapid development with automatic API documentation
- **ML/AI**: scikit-learn Random Forest, TF-IDF vectorization, regex pattern matching
- **Frontend**: React + TypeScript for type-safe user interface development
- **Data Processing**: NumPy and pandas for efficient numerical computation

## Explainable Risk Scoring Philosophy

### Core Principle: No Black Box Logic
Every risk score is traceable to specific, understandable factors. Users see exactly why a profile was flagged, enabling informed decision-making and security awareness learning.

### Hybrid Approach (60% Rules + 40% ML)
- **Rule-Based Component**: Handles obvious red flags with perfect explainability (financial requests, new accounts, suspicious ratios)
- **ML Component**: Captures subtle behavioral patterns using Random Forest with feature importance rankings
- **Combined Scoring**: Transparent weighting system where users understand both rule and ML contributions

### Risk Categories
- **0-20 (Minimal Risk)**: Normal characteristics, standard monitoring
- **21-40 (Low Risk)**: Minor concerns, normal caution recommended  
- **41-60 (Medium Risk)**: Multiple concerning patterns, enhanced scrutiny
- **61-80 (High Risk)**: Strong malicious indicators, user warnings recommended
- **81-100 (Critical Risk)**: Severe threats, immediate action required

### Example Explanation Output
```json
{
  "risk_score": 87,
  "risk_level": "Critical Risk",
  "explanations": [
    "Account created 7 days ago (new accounts are high risk)",
    "Messages contain financial requests and money transfer language",
    "Profile shows romance scam patterns (emotional manipulation + money requests)"
  ],
  "recommended_actions": [
    "Do not send money or share personal information",
    "Report this profile to platform administrators"
  ]
}
```

## Hackathon-Focused Scope

### Strategic Trade-offs Made
1. **Explainability Over Accuracy**: Chose hybrid approach over complex deep learning for user trust and transparency
2. **Quality Over Quantity**: Focused on 4 core features rather than attempting comprehensive feature set
3. **Proven Technology**: Used established libraries (scikit-learn, FastAPI) rather than experimental approaches

### What Was Simplified
- **Training Data**: Synthetic scam examples rather than real datasets (privacy/time constraints)
- **Image Analysis**: Rule-based verification simulation rather than expensive API integrations  
- **Language Support**: English-only rather than multi-language complexity
- **Behavioral Analysis**: Basic metadata patterns rather than complex network analysis

### Future Improvements (Post-Hackathon)
- Platform-specific tuning for LinkedIn, Instagram, dating apps
- Real-time image similarity detection for stolen profile photos
- Continuous learning from user feedback and flagged profiles
- Browser extension for end-user protection

## Getting Started

### Local Development

**Backend (FastAPI)**:
```bash
cd backend
pip install -r requirements.txt
python main.py
# Server runs on http://localhost:8000
```

**Frontend (React)**:
```bash
cd frontend
echo "REACT_APP_API_BASE_URL=http://localhost:8000" > .env.local
npm install
npm start
# App runs on http://localhost:3000
```

### Live Demo

🌐 **Frontend**: Deploy on Vercel  
🔧 **Backend**: Deploy separately on Render/Railway/Fly.io  
⚙️ **Configuration**: Set `REACT_APP_API_BASE_URL` environment variable

The system demonstrates explainable cybersecurity AI with complete transparency in decision-making. Every risk assessment includes specific reasons and actionable recommendations, making it suitable for both end-user protection and platform operator compliance needs.

### Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions on Vercel.

---

**Developed using structured planning methodology for hackathon success**