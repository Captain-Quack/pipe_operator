# pipe-operator

Pipe-operator friendly wrappers around functions from Python's standard library `operator` module, designed to be used with the third‑party `pipe` package.

This lets you write readable, left‑to‑right expressions using the bitwise‑or pipe provided by `pipe`:

```python
from pipe_operator import padd, pitemgetter

2 | padd(3)                     # -> 5
{"x": 10} | pitemgetter("x")  # -> 10
```

## Installation

- Python 3.8+
- Depends on the third‑party `pipe` package

Install from PyPI:

```bash
pip install pipe-operator
```

If you don't have `pipe` yet:

```bash
pip install pipe
```

## Quick start

```python
from pipe_operator import (
    padd, psub, pmul, ptruediv,
    pneg, pabs, pnot_,
    pconcat, getitem,
    pitemgetter, pattrgetter, pmethodcaller,
)

# Arithmetic
result = 2 | padd(3) | pmul(5)     # (2 + 3) * 5 = 25

# Unary and truthiness helpers
ok = [1] | pnot_()                 # False

# Sequence / mapping helpers
value = {"k": 10} | getitem("k")  # 10

# Factory-based helpers
name = "sam" | pmethodcaller("upper")  # "SAM"
```

## API highlights

All names are Pipe‑wrapped forms of functions in `operator` and are intended to be used as `value | name(args...)`.

- Arithmetic: `padd`, `psub`, `pmul`, `pmatmul`, `ptruediv`, `pfloordiv`, `pmod`, `ppow`
- In‑place arithmetic: `piadd`, `pisub`, `pimul`, `pimatmul`, `pitruediv`, `pifloordiv`, `pimod`, `pipow`
- Unary: `pneg`, `ppos`, `pabs`, `pinvert`, `pnot_`, `pindex`, `ptruth`
- Bitwise/shifts: `plshift`, `prshift`, `pand_`, `por_`, `pxor`
- In‑place bitwise/shifts: `pilshift`, `pirshift`, `piand`, `pior`, `pixor`
- Comparisons: `peq`, `pne`, `plt`, `ple`, `pgt`, `pge`, `pis_`, `pis_not`
- Sequences/mappings: `pconcat`, `pcontains`, `pcountOf`, `pindexOf`, `plength_hint`
- Item access/mutation: `getitem`, `setitem`, `delitem`, `iconcat`
- Factories: `pattrgetter`, `pitemgetter`, `pmethodcaller`

See the docstring in `pipe_operator/__init__.py` and the tests for examples of each.

## Testing

This repo uses the standard library `unittest`.

```bash
python -m unittest discover -s tests -p "test*.py" -v
```

## Compatibility

- Python 3.8+
- `pipe` >= 2, < 3

## Acknowledgements

- Powered by the excellent [`pipe`](https://pypi.org/project/pipe/) package
- Wraps functions from Python's standard library [`operator`](https://github.com/python/cpython/blob/3.13/Lib/operator.py) module
