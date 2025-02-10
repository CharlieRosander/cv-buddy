# CV-Buddy Project Structure Guide

Welcome to CV-Buddy! This guide will help you understand how the project is organized and why we made certain choices. The goal is to create a clean, maintainable, and scalable application while keeping things understandable for learning purposes.

## Project Overview

CV-Buddy is an AI-powered CV management system that helps users create, manage, and generate CVs. We're building it with Python, FastAPI, and modern AI tools.

## Project Structure

Here's our folder structure with explanations of each part:

```
cv-helper/
├── app/                    # Main application code
│   ├── api/                # All our API endpoints
│   ├── core/               # Essential application components
│   ├── db/                 # Database-related code
│   ├── services/           # Business logic
│   └── utils/              # Helper functions
├── tests/                  # All our tests
└── docs/                   # Documentation
```

Let's break down each component and understand why it's important:

### 1. API Layer (`app/api/`)
This is where we handle web requests. Think of it as the "front desk" of our application.
```
api/
├── v1/                    # Version 1 of our API
    ├── cv/                # CV-related endpoints
    ├── documents/         # Document management endpoints
    └── generation/        # AI generation endpoints
```
- **Why?** Organizing by feature makes it easy to find and modify specific functionality
- **Learning Point:** This structure helps us maintain different versions of our API if we need to make breaking changes

### 2. Core (`app/core/`)
Contains essential setup and configuration code.
```
core/
├── config/               # Application settings
├── security/             # Authentication & permissions
└── exceptions/           # Error handling
```
- **Why?** Keeps configuration and security separate from business logic
- **Learning Point:** Separating configuration makes it easier to modify settings for different environments (development, production)

### 3. Database (`app/db/`)
All database-related code lives here.
```
db/
├── models/              # Database table definitions
├── repositories/        # Database access code
└── migrations/          # Database structure changes
```
- **Why?** Keeps all database operations in one place
- **Learning Point:** Using repositories pattern makes it easier to change database types later

### 4. Services (`app/services/`)
This is where the main business logic lives.
```
services/
├── cv/                 # CV management logic
├── document/           # Document processing
└── ai/                 # AI generation logic
    ├── agents/         # LangGraph agents
    ├── monitoring/     # LangSmith monitoring setup
    └── templates/      # CV generation templates
```
- **Why?** Separates business logic from API endpoints
- **Learning Point:** Makes code more reusable and easier to test

### 5. Utils (`app/utils/`)
Helper functions that are used across the application.
- **Why?** Avoid duplicating common code
- **Learning Point:** DRY (Don't Repeat Yourself) principle in action

## Development Approach

We'll develop this project in phases:

1. **Phase 1: Basic Structure**
   - Set up the project structure
   - Create basic database models
   - Implement simple CV CRUD operations

2. **Phase 2: Document Management**
   - Add document upload/storage
   - Implement document parsing
   - Create document management endpoints

3. **Phase 3: AI Integration**
   - Add LangGraph integration
   - Set up LangSmith monitoring
   - Implement CV generation
   - Add context processing
   - Configure AI performance tracking

4. **Phase 4: Polish**
   - Add authentication
   - Implement advanced features
   - Add comprehensive error handling
   - Optimize AI agent performance using LangSmith insights

## Best Practices We'll Follow

1. **Write Clear Code**
   - Use descriptive variable names
   - Add comments for complex logic
   - Keep functions small and focused

2. **Version Control**
   - Make small, focused commits
   - Write clear commit messages
   - Use feature branches

3. **Testing**
   - Write tests for new features
   - Test before committing
   - Use automated testing
   - Monitor AI performance with LangSmith

4. **Documentation**
   - Document as you code
   - Keep README updated
   - Add docstrings to functions
   - Track AI agent behavior and performance metrics

## Getting Started

1. Clone the repository
2. Create a virtual environment
3. Install dependencies
4. Follow the setup instructions in README.md

Remember: It's okay to not understand everything at first! We'll build this step by step, and each part will become clearer as we progress.

## Next Steps

We'll start by setting up the basic project structure and implementing the first few features. Each step will build on the previous ones, making it easier to understand how everything fits together.

Feel free to ask questions at any point - this is a learning project, and questions help everyone understand better!
