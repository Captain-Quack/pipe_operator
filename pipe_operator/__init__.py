"""Pipe-operator friendly wrappers around functions from the standard library's operator module.

This package exposes Pipe-wrapped callables so you can use the bitwise-or pipe
operator from the 'pipe' package for fluent, left-to-right style expressions.

Example
-------
>>> from pipe_operator import padd, pitemgetter
>>> 2 | padd(3)
5
>>> {'x': 10} | pitemgetter('x')
10

Notes
-----
- This package depends on the third-party 'pipe' package. Install it with:
  pip install pipe
- Only the names listed in __all__ are exported from this package; internal
  helper symbols are kept private.
"""

from typing import Any, Callable
from pipe import Pipe

# ---------- helpers ----------
@Pipe
def _firstarg(value: Any, fn: Callable[..., Any], *args: Any, **kwargs: Any) -> Any:
    """Apply a callable to the piped-in value as its first positional argument."""
    return fn(value, *args, **kwargs)

@Pipe
def _curry_then_apply(value: Any, factory: Callable[..., Callable[..., Any]], *args: Any, **kwargs: Any) -> Any:
    """Build a callable using a factory (e.g., operator.attrgetter) then apply it to value."""
    return factory(*args, **kwargs)(value)

# ---------- arithmetic ----------
import operator as _op

padd        = _firstarg(_op.add)
psub        = _firstarg(_op.sub)
pmul        = _firstarg(_op.mul)
pmatmul     = _firstarg(_op.matmul)
ptruediv    = _firstarg(_op.truediv)
pfloordiv   = _firstarg(_op.floordiv)
pmod        = _firstarg(_op.mod)
ppow        = _firstarg(_op.pow)

# in-place arithmetic
piadd       = _firstarg(_op.iadd)
pisub       = _firstarg(_op.isub)
pimul       = _firstarg(_op.imul)
pimatmul    = _firstarg(_op.imatmul)
pitruediv   = _firstarg(_op.itruediv)
pifloordiv  = _firstarg(_op.ifloordiv)
pimod       = _firstarg(_op.imod)
pipow       = _firstarg(_op.ipow)

# ---------- unary ----------
pneg        = _firstarg(_op.neg)
ppos        = _firstarg(_op.pos)
pabs        = _firstarg(_op.abs)
pinvert     = _firstarg(_op.invert)
pnot_       = _firstarg(_op.not_)     # logical not
pindex      = _firstarg(_op.index)
ptruth      = _firstarg(_op.truth)

# ---------- bitwise / shifts ----------
plshift     = _firstarg(_op.lshift)
prshift     = _firstarg(_op.rshift)
pand_       = _firstarg(_op.and_)
por_        = _firstarg(_op.or_)
pxor        = _firstarg(_op.xor)

# in-place bitwise / shifts
pilshift    = _firstarg(_op.ilshift)
pirshift    = _firstarg(_op.irshift)
piand       = _firstarg(_op.iand)
pior        = _firstarg(_op.ior)
pixor       = _firstarg(_op.ixor)

# ---------- comparisons ----------
peq         = _firstarg(_op.eq)
pne         = _firstarg(_op.ne)
plt         = _firstarg(_op.lt)
ple         = _firstarg(_op.le)
pgt         = _firstarg(_op.gt)
pge         = _firstarg(_op.ge)
pis_        = _firstarg(_op.is_)
pis_not     = _firstarg(_op.is_not)

# ---------- sequence / mapping helpers ----------
pconcat     = _firstarg(_op.concat)
pcontains   = _firstarg(_op.contains)
pcountOf    = _firstarg(_op.countOf)
pindexOf    = _firstarg(_op.indexOf)
plength_hint = _firstarg(_op.length_hint)

# item access/mutation
getitem    = _firstarg(_op.getitem)
setitem    = _firstarg(_op.setitem)   # obj | setitem(key, value)
delitem    = _firstarg(_op.delitem)   # obj | delitem(key)

# in-place concat
iconcat    = _firstarg(_op.iconcat)

# ---------- factories (build-call-then-apply) ----------
from operator import attrgetter as _attrgetter
from operator import itemgetter as _itemgetter
from operator import methodcaller as _methodcaller

pattrgetter  = _curry_then_apply(_attrgetter)
pitemgetter  = _curry_then_apply(_itemgetter)
pmethodcaller= _curry_then_apply(_methodcaller)

# Public API
__all__ = [
    # arithmetic
    'padd', 'psub', 'pmul', 'pmatmul', 'ptruediv', 'pfloordiv', 'pmod', 'ppow',
    # in-place arithmetic
    'piadd', 'pisub', 'pimul', 'pimatmul', 'pitruediv', 'pifloordiv', 'pimod', 'pipow',
    # unary
    'pneg', 'ppos', 'pabs', 'pinvert', 'pnot_', 'pindex', 'ptruth',
    # bitwise / shifts
    'plshift', 'prshift', 'pand_', 'por_', 'pxor',
    # in-place bitwise / shifts
    'pilshift', 'pirshift', 'piand', 'pior', 'pixor',
    # comparisons
    'peq', 'pne', 'plt', 'ple', 'pgt', 'pge', 'pis_', 'pis_not',
    # sequence / mapping helpers
    'pconcat', 'pcontains', 'pcountOf', 'pindexOf', 'plength_hint',
    # item access/mutation and concat
    'getitem', 'setitem', 'delitem', 'iconcat',
    # factories
    'pattrgetter', 'pitemgetter', 'pmethodcaller',
]
