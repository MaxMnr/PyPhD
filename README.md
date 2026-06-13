# pyphd

Personal Python package for reusable code: preconfigured models, hyperparameter
spaces, and small data manipulation helpers.

## Installation

From this folder:

```bash
pip install -e .
```

For development tools:

```bash
pip install -e ".[dev]"
```

## Examples

```python
from pyphd.models import LR

model = LR()
model.fit(X_train, y_train)
```

```python
from pyphd.hpo import LR_PARAM_GRID
```

```python
from pyphd.data import clean_column_names

df = clean_column_names(df)
```
