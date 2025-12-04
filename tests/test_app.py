import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "app"))

from predict import predict


def test_predict_returns_valid_class():
    features = [5.1, 3.5, 1.4, 0.2]
    result = predict(features)

    valid_classes = {"setosa", "versicolor", "virginica"}
    
    assert result in valid_classes, f"Unexpected result: {result}"
