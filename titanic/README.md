# Titanic: Machine Learning from Disaster

A small, beginner-friendly project for Kaggle's Titanic competition. It trains a
baseline model from `train.csv`, reports a validation accuracy, then predicts
survival for `test.csv` and writes `submission.csv`.

## 1. Get the competition data

Join the [Titanic competition](https://www.kaggle.com/competitions/titanic) and
download its data. Put these files in the `data` folder:

```text
titanic/
  data/
    train.csv
    test.csv
```

The CSV files are not included in this project; download them from Kaggle after
accepting the competition rules.

## 2. Set up Python

From this folder, create and activate a virtual environment, then install the
dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, run the script using the environment's Python
directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## 3. Train and create a submission

```powershell
python train.py
```

The script prints validation accuracy and saves `submission.csv` next to
`train.py`. The output has exactly the required `PassengerId` and `Survived`
columns. Upload it on the competition's **Submit Predictions** page.

## What the starter model does

- Uses passenger class, sex, age, family counts, fare, and port of embarkation.
- Fills missing numeric and categorical values using training data.
- One-hot encodes categorical features and trains a random forest classifier.
- Measures accuracy on a stratified holdout before fitting on all training rows.

The validation score is an estimate and may differ from the Kaggle leaderboard
score. Use it as a baseline while learning about feature engineering and model
evaluation.
