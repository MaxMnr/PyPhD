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
=======
# PyPhD
Misc. tools for my PhD organize as a messy library
>>>>>>> 11161d186e99b7fdb4699c0c2acef8c7e3c0b036
