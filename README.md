# Faith Sobriety Tracker

A faith-based sobriety tracker web application for daily check-ins, streak tracking, relapse reflection, and optional scripture/prayer support.

This project focuses on accountability, reflection, and growth while keeping user data private and secure.

---

## MVP (v0)

### Core Features
- User authentication (register/login)
- Daily check-in (Sober / Relapse)
- Optional notes for reflection
- Current and longest streak tracking
- History view (list or calendar)
- Relapse reflection prompts

### Faith-Based (Optional / Opt-In)
- Verse of the Day (rotating)
- Private prayer or gratitude journal entry
- Encouraging language and grace-centered UX

### Quality & Privacy
- User data is private by default
- Secure password hashing
- Export check-ins as CSV

---

## Tech Stack

**Frontend**
- React
- Vite
- TypeScript
- TailwindCSS

**Backend**
- FastAPI (Python)
- JWT Authentication

**Database**
- PostgreSQL

**Dev Environment**
- Docker + Docker Compose

---

## Architecture Overview

- React frontend communicates with FastAPI backend via REST API
- Backend handles authentication, streak calculations, and data validation
- PostgreSQL stores user data and check-ins
- Docker Compose manages local development services

---

## Local Development

### Prerequisites
- Docker
- Docker Compose

### Run the App

```bash
docker compose up --build
```

---

## Services
- Frontend: https://localhost:5173
- Backend API: https://localhost:8000
- API Docs(Swagger): https://localhost:8000/docs

---

## Project Structure
```
faith-sobriety-tracker/
│
├── frontend/
├── backend/
├── docker-compose.yml
├── README.md
└── .env (not committed)
```

---

## Roadmap
### Phase 1
- Authenication (register/login)
- Create daily check-in
- Display current streak on dashboard

### Phase 2
- History calender view
- Verse of the Day
- Relapse reflection prompts
- CSV export

### Phase 3
- Data visualizations
- Grace-mode toggle (include more encouraging language)
- Mobile responsiveness polish

---

## Privacy & Philosophy
This application is designed with compassion and accountability in mind
Faith-based features are optional and indeaded to encourage reflection, not judgement.

All user data remains private and is not shared.

---

## License
MIT License

