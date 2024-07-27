```commandline
pytest
```
```commandline
pytest --cov
```
```commandline
coverage html
```
# Parametrize
```commandline
@pytest.mark.parametrize('arguments, names, separated, by, commas', arguments_parametrized_values_as_list)
```
```commandline
products =  [
     (2, 3, 6),
     (1, 2, 3)
     ]
     
@pytest.mark.parametrize('a, b, product', products)
def test_something(a, b, product):
    assert a * b == product
```
# Fixtures
Return something.
```commandline
@pytest.fixture
def something():
    return whatever
    
def test_something(something):
    something
```
If instead of return we use yield, the code after yield will be executed when the test finishes.  

Fixtures have scopes, default is "function".  
Options: 
- session (i.e. read an external file)
- class
- module
- package
# Error
```commandline
def test_something() -> None:
    with pytest.raises(ValueError) as e:
        code that raises error
        assert 'error message' in str(e.value)
```
# Mocking
```commandline
from pytest import MonkeyPatch

def test_something(monkeypatch: MonkeyPatch) -> None:
    def function_name():
        # Overwrite function: use original function name + _mock in name
        # Now it can be called in monkeypatch
        pass
    monkeypatch.setattr("function.path", moked_value)
    monkeypatch.setattr(ClassNameThatHasBeenImported, "method_name", functiona_name_plus_mock)
    assert some_code
```
# Variables
```commandline
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY") or ""
```
# Configuration files
## pytest.ini
In project's root directory. CLI configs and others.
```commandline
[pytest]
junit_family = xunit2

```
## conftest.py
Inside the `tests` folder. Contains share test code for the tests, can contain fixtures.

# CLI
`python -m pytest`  
--verbose  
--quiet  
--exitfirst : stops execution after first error  
--maxfail=10 : number of failures until stops  
--junit-xml report.xml : saves a file with the report  

## Markers
For example:
`@pytest.mark.duckduckgo`

## Filterng tests
`python -m pytest folder_name/file.py`  
`python -m pytest folder_name/file.py::test_name`  
`python -m pytest -k one` run tests that contain string "one"
`python -m pytest -m duckduckgo` marker

# Plugins
```
pip install pytest-cov
python -m pytest --cov=direcotyr_name
python -m pytest --cov=direcotyr_name --cov-report html # too see lines covered

pip install pytest-bdd
```
# Parallelization
```
pip install pytest-xdist

python -m pytest -n auto
python -m pytest -n 3 # tests must be independent
```



