# AI Swim Set Generator (Backend)

This project is a backend API that generates structured swim workouts based on a swimmer’s level, total yardage, and training focus.

The goal of this project is to model how a swim coach would design a workout and expose that logic through a clean REST API.

## WHAT THIS APP DOES
- Generates organized swim workouts
- Adjusts difficulty based on swimmer level
- Adapts workouts based on training focus
- Returns workouts that are easy to follow during practice

Each workout is split into:
- Warmup
- Main set
- Cooldown

TARGET USERS
- High school swimmers
- Competitive swimmers
- Casual lap swimmers
- Triathletes

## HOW IT WORKS
The generator uses rule-based logic:
- Swimmer level determines volume, rest, and complexity
- Training focus determines structure:
  * Speed uses shorter repeats and sprint work
  * Technique emphasizes drills and form
  * Endurance uses longer aerobic sets
- Total yardage is divided across warmup, main set, and cooldown

 ### API FEATURES (CURRENT)
- Generate swim workouts via REST API
- Input validation
- Support for beginner, intermediate, and advanced swimmers
- Support for speed, technique, and endurance focus
- Structured workout output
- Auto-generated API documentation

EXAMPLE ENDPOINT
POST /generate

Inputs:
level
total_yards
focus
stroke
equipment

Outputs:
- Total yards
- Swimmer level
- Training focus
- Stroke
- Warmup, main set, and cooldown details

### TECH STACK
- Python
- FastAPI
- Pydantic
- Uvicorn

### PROJECT STRUCTURE
app/main.py        API routes
app/models.py      Request and response schemas
app/generator.py   Workout generation logic

### RUNNING LOCALLY
1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies
4. Run the FastAPI server
5. Open the auto-generated API docs

 ### PLANNED FEATURES...
- Save workout history to a database
- Monthly yardage tracking
- Calendar-based workout logging
- Printable workout formats
- Stroke-specific drill logic
- User authentication
- Cloud deployment

#### AUTHOR
Daniel Valenzuela
Computer Science Student
Backend-focused developer

LICENSE
MIT