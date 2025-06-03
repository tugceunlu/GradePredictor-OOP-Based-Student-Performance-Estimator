# GradePredictor-OOP-Based-Student-Performance-Estimator

# 📊 GradePredictor – OOP-Based Student Performance Estimator

GradePredictor is a terminal-based, object-oriented Python project that predicts student final grades based on study time, assignment performance, and attendance. It uses a simple linear regression model (via scikit-learn) and emphasizes clean OOP design with practical input/output logic.

## ✅ Features

- Collects student data via terminal input
- Predicts course performance using `LinearRegression`
- Demonstrates solid OOP principles with `Student`, `Course`, and `Predictor` classes
- CLI interface, no external files needed
- Easily extendable with CSV, GUI, or database support

## 🧱 Project Structure

```
GradePredictor/
├── main.py                      # Runs the CLI application
├── models/
│   ├── student.py               # Student class with attributes
│   ├── course.py                # Course class
│   └── predictor.py             # Machine learning logic
├── data/                        # Placeholder for optional CSV files
└── requirements.txt             # Python dependencies
```

## 🚀 Installation & Running

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/GradePredictor.git
cd GradePredictor

# 2. Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python main.py
```

## 🧪 Example Interaction

```
📘 Course Performance Predictor
Enter course name: Software Engineering
How many students do you want to evaluate? 2

--- New Student ---
Enter student name: Elif
How many hours did Elif study? 10
What was Elif's assignment score (out of 100)? 85
What was Elif's attendance rate (in %)? 90

--- New Student ---
Enter student name: Can
How many hours did Can study? 7
What was Can's assignment score (out of 100)? 75
What was Can's attendance rate (in %)? 80

📊 Predicted final grades for Software Engineering:
Elif: 85.00
Can: 76.00
```

## 🛠 Technologies Used

- Python 3
- scikit-learn
- OOP (Object-Oriented Programming)

## 💡 Possible Future Improvements

- CSV file support (import/export)
- GUI version (Tkinter or Streamlit)
- Web API version with Flask or FastAPI
- Additional ML models (e.g., Decision Tree, Random Forest)

 by Tuğçe Ünlü
