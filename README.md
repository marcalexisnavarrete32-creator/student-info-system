# Student Information System

A command-line student information system with JSON storage, configuration management, logging, and unit tests.

## Features
- Add, view (all / by ID), update, and delete students
- JSON file persistence (`data/students.json`)
- Config-driven paths and log level (`config/config.json`)
- File + console logging (`logs/app.log`)
- Error handling around all file and input operations
- Unit tests with pytest

## Project Structure
```
student-info-system/
├── src/
│   ├── models/student.py
│   ├── services/student_service.py
│   ├── utils/config.py, logger.py
│   └── main.py
├── data/students.json
├── config/config.json
├── logs/
├── tests/test_student_service.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Setup & Run
```bash
git clone https://github.com/<your-username>/student-info-system.git
cd student-info-system
pip install -r requirements.txt
python src/main.py        # run from the repository root
```

## Run Tests
```bash
pytest
```

## Configuration
Edit `config/config.json`:
| Key | Description |
|---|---|
| `data_file` | Path to the JSON data file |
| `log_file` | Path to the log file |
| `log_level` | DEBUG, INFO, WARNING, ERROR |

## Author
<Your Name>
