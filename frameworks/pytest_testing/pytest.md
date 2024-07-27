# Run tests
```commandline
 python -m pytest
```
# Run test in parallel
Option 1: pytest-xdist
```commandline
pip install pytest-xdist

-- specify number of nodes
python -m pytest -n 3
```
Option 2: Selenium Grid