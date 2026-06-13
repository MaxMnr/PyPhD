"""Reusable hyperparameter search spaces."""

LR_PARAM_GRID = {
    "C": [0.01, 0.1, 1.0, 10.0],
    "penalty": ["l2"],
    "solver": ["lbfgs"],
}
