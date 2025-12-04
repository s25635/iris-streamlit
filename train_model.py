from pathlib import Path
import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#test

def main():

    app_dir = Path.cwd() / "app"
    app_dir.mkdir(parents=True, exist_ok=True)

    iris = load_iris()
    X, y = iris.data, iris.target

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    clf = LogisticRegression(max_iter=200)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.4f}")

    model_path = app_dir / "model.joblib"
    joblib.dump(clf, model_path)
    print(f"Saved trained model to: {model_path}")

if __name__ == "__main__":
    main()
