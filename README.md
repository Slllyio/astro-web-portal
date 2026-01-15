# Astrological Probability Engine - Web Portal

## Overview
Web application that generates astrological reports based on date of birth.

## Tech Stack
- **Backend**: Flask (Python web framework)
- **PDF Generation**: WeasyPrint (Markdown → PDF)
- **Frontend**: HTML/CSS/JavaScript (vanilla)

## Project Structure
```
astro_web_portal/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Frontend interface
├── static/
│   ├── style.css         # Styling
│   └── script.js         # Client-side logic
└── reports/              # Generated PDF storage (temporary)
```

## Installation & Setup

### 1. Install Dependencies
```bash
pip install flask weasyprint python-dateutil
```

### 2. Run the Application
```bash
python app.py
```

### 3. Access Portal
Open browser: `http://localhost:5000`

## Features
- ✅ Date of Birth input with validation
- ✅ Real-time report generation
- ✅ PDF download
- ✅ Professional markdown → PDF conversion
- ✅ Loading indicators
