"""Train a Titanic survival baseline and create a Kaggle submission file."""

from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"
TRAIN_PATH = DATA_DIR / "train.csv"
TEST_PATH = DATA_DIR / "test.csv"
SUBMISSION_PATH = PROJECT_DIR / "submission.csv"

NUMERIC_FEATURES = ["Pclass", "Age", "SibSp", "Parch", "Fare"]
CATEGORICAL_FEATURES = ["Sex", "Embarked"]
FEATURES = NUMERIC_FEATURES + CATEGORICAL_FEATURES
TARGET = "Survived"


def build_model() -> Pipeline:
    """Create preprocessing and classification steps as one leakage-safe pipeline."""
    numeric_pipeline = Pipeline(
        steps=[("imputer", SimpleImputer(strategy="median"))]
    )
    categorical_pipeline = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    preprocessing = ColumnTransformer(
        transformers=[
            ("numeric", numeric_pipeline, NUMERIC_FEATURES),
            ("categorical", categorical_pipeline, CATEGORICAL_FEATURES),
        ]
    )

    return Pipeline(
        steps=[
            ("preprocessing", preprocessing),
            (
                "classifier",
                RandomForestClassifier(
                    n_estimators=300,
                    min_samples_leaf=2,
                    random_state=42,
                ),
            ),
        ]
    )


def main() -> None:
    if not TRAIN_PATH.is_file() or not TEST_PATH.is_file():
        raise FileNotFoundError(
            "Could not find train.csv and test.csv. Download the Titanic "
            f"competition data and place both files in: {DATA_DIR}"
        )

    train = pd.read_csv(TRAIN_PATH)
    test = pd.read_csv(TEST_PATH)

    required_train_columns = set(FEATURES + [TARGET])
    required_test_columns = set(FEATURES + ["PassengerId"])
    missing_train = required_train_columns.difference(train.columns)
    missing_test = required_test_columns.difference(test.columns)
    if missing_train or missing_test:
        raise ValueError(
            "Unexpected input columns. "
            f"Missing from train.csv: {sorted(missing_train)}; "
            f"missing from test.csv: {sorted(missing_test)}."
        )
    if train.empty or test.empty:
        raise ValueError("train.csv and test.csv must both contain passenger rows.")

    x_train = train[FEATURES]
    y_train = train[TARGET]
    x_fit, x_validation, y_fit, y_validation = train_test_split(
        x_train,
        y_train,
        test_size=0.2,
        random_state=42,
        stratify=y_train,
    )

    model = build_model()
    model.fit(x_fit, y_fit)
    validation_predictions = model.predict(x_validation)
    print(
        "Validation accuracy: "
        f"{accuracy_score(y_validation, validation_predictions):.3f}"
    )

    model.fit(x_train, y_train)
    predictions = model.predict(test[FEATURES])
    submission = pd.DataFrame(
        {"PassengerId": test["PassengerId"], TARGET: predictions}
    )
    submission.to_csv(SUBMISSION_PATH, index=False)
    print(f"Saved {len(submission)} predictions to {SUBMISSION_PATH}")


if __name__ == "__main__":
    main()
