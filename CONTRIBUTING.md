# Contributing to Suspicious Profile Analyzer

## Hackathon Project Notice

This project was developed during a hackathon with a focus on explainable AI for cybersecurity threat detection. The current implementation represents an MVP (Minimum Viable Product) designed to demonstrate core concepts within hackathon time constraints.

## Development Setup

### Backend (Python + FastAPI)
```bash
cd backend
pip install -r requirements.txt
python main.py
```

### Frontend (React + TypeScript)
```bash
cd frontend
npm install
npm start
```

## Project Structure

- `backend/` - FastAPI server with ML/NLP analysis engine
- `frontend/` - React TypeScript UI for profile analysis
- `.kiro/` - Planning documentation and design decisions
- `HERO/` - Strategic planning summaries and trade-offs

## Key Design Principles

1. **Explainability First**: Every risk score must be traceable to specific factors
2. **Hybrid Approach**: 60% rule-based + 40% ML for transparency
3. **User Trust**: Clear explanations over black-box accuracy
4. **Hackathon Scope**: Focused MVP over feature overload

## Future Improvements

See `HERO/future-scope.md` for planned enhancements that were excluded from the hackathon MVP due to time constraints.

## Code of Conduct

This project aims to improve online safety and cybersecurity. Contributions should align with ethical AI practices and user privacy protection.