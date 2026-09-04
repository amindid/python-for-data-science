# ft_package

A sample Python package created as part of the 42 Python for Data Science project.

## Description

`ft_package` provides a simple function to count the number of occurrences of an item in a list.

## Installation

Build the package:

```bash
python -m build
```

Install the package using the source distribution:

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
```

Or using the wheel:

```bash
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))
print(count_in_list(["toto", "tata", "toto"], "tutu"))
```

Output:

```text
2
0
```

## License

This project is licensed under the MIT License.
