# CV-Buddy

CV-Buddy is an AI-powered CV management system that helps users create, manage, and optimize their CVs using state-of-the-art language models and intelligent agents.

## Features

- Upload and manage CVs and source materials
- AI-powered CV generation and optimization
- Context-aware CV customization based on job descriptions
- Advanced monitoring with LangSmith integration
- RESTful API for easy integration

## Technology Stack

- **Backend**: FastAPI, PostgreSQL, SQLAlchemy
- **AI Components**: LangGraph, LangSmith
- **Documentation**: OpenAPI/Swagger
- **Testing**: pytest

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/CharlieRosander/cv-buddy.git
cd cv-buddy
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Run the application:
```bash
uvicorn app.main:app --reload
```

## Development

- API documentation available at `/docs` when running locally
- Run tests with `pytest`
- Format code with `black`
- Check types with `mypy`
