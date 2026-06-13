"""Preconfigured machine learning models."""

from sklearn.linear_model import LogisticRegression as LR
from sklearn.ensemble import RandomForestClassifier as RF

def LogisticRegression(**overrides) -> LR:
    """Return a default logistic regression model.

    Pass keyword arguments to override any default parameter.
    """
    params = {
        "max_iter": 1000,
        "solver": "lbfgs",
        "random_state": 42,
    }
    params.update(overrides)
    return LR(**params)


def RandomForest(**overrides) -> RF:
    """Return a default logistic regression model.

    Pass keyword arguments to override any default parameter.
    """
    params = {
        "n_estimators": 250,
        "solver": "lbfgs",
        "random_state": 42,
    }
    params.update(overrides)
    return RF(**params)

