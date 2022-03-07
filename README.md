# Solution Management UI

---
## Directory Structure

---
```
.
├── Solutions/
|   ├── views/
|   |   └─ main_views.py
|   ├── static/
|   |   └─ style.css
|   ├── templates/
|   |   └─ index.html
|   ├── __init__.py
|   ├── models.py
├── venv/
├── app.py
├── env.json
├── README.md
└── requirements.txt
```

## Getting Started

---
To be able to run this project you need to follow these steps below:

### Prerequisites

- python 3.x ([Download Python](https://www.python.org/downloads/))
- virtualenv([venv](https://docs.python.org/3/library/venv.html))
- PyCharm IDE (or any kind of IDE) ([Download PyCharm](https://www.jetbrains.com/pycharm/download))

###Installing
1. Clone the repo
```
git clone https://github.com/msubin/SAproject.git
```
2. Navigate to where you clone and install all dependencies
```
cd /<path to your directory>

// Create virtual env folder
python -m venv venv

// Activate virtual env Linux/MacOS
source ./bin/venv/activate

// Install all dependencies
pip3 install -r requirements.txt
```
To deactivate env, run:
```
deactivate
```

## Running Development

---
1. Either, in virtual env, use default flask command. This default command does not reload when there is a new change.
```
flask run
```

2. Or, in virtual env, run using normal python command. This will enable auto reload when changes are made.
```
// Linux / MacOS
python3 app.py

// Window
python app.py
```

## Authors

---
- Subin Moon - subin.moon@hootsuite.com