# Student Pass/Fail Prediction - Deep Learning

## Files

- `dataset.csv` - sample student dataset
- `main.py` - loads the CSV, preprocesses data, trains the neural network, evaluates it, and predicts a new student
- `requirements.txt` - Python packages required

## Features

- attendance
- study_hours
- assignment_score
- previous_score
- absences
- participation

Target:

- `passed = 1` -> Pass
- `passed = 0` -> Fail

## Run

```bash
python -m pip install -r requirements.txt
python main.py
```

The script creates `student_pass_fail_model.keras` after training.

> Note: The included dataset is synthetic/demo data. For a real school project,
> replace `dataset.csv` with a properly collected and ethically approved dataset.
