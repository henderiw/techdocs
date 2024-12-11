# create a package

create a virtual env but use .gitignore

example gitignore
```
# Byte-compile / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environment
venv/
.venv/
```

## strps

- create __init.py__ file in the package
- each <module>.py is a module -> using the module name of the .py file
- pip freeze > requirements.txt


## import locally

```python
import sys
sys.path.append('/Users/henderiw/code/kform/kform-dev/choreopy')
from crd import generate_crds

generate_crds("apis", "crds")
```