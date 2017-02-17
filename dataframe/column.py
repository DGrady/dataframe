"""Refer to data frame columns, without referring to a specific data
frame

"""

import math
import operator as op

from .function_tree import Delayed

class Column:
    """Represents a reference to a data frame column

    """

    def __init__(self, name):
        self._column_label = name

    def __repr__(self):
        return 'C<{}>'.format(self._column_label)

    def __str__(self):
        return 'C<{}>'.format(self._column_label)

    def call(self, func):
        """Apply a function of one argument to the column

        """
        return Delayed(func, self)

    def _binop_right(self, operator, y):
        return Delayed(operator, self, y)

    def _binop_left(self, operator, x):
        return Delayed(operator, x, self)

    def __add__(self, y):
        return self._binop_right(op.add, y)

    def __radd__(self, x):
        return self._binop_left(op.add, x)

    def __sub__(self, y):
        return self._binop_right(op.sub, y)

    def __rsub__(self, x):
        return self._binop_left(op.sub, x)

    def __mul__(self, y):
        return self._binop_right(op.mul, y)

    def __rmul__(self, x):
        return self._binop_left(op.mul, x)

    def __truediv__(self, y):
        return self._binop_right(op.truediv, y)

    def __rtruediv__(self, x):
        return self._binop_left(op.truediv, x)

    def __floordiv__(self, y):
        return self._binop_right(op.floordiv, y)

    def __rfloordiv__(self, x):
        return self._binop_left(op.floordiv, x)

    def __mod__(self, y):
        return self._binop_right(op.mod, y)

    def __rmod__(self, x):
        return self._binop_left(op.mod, x)

    def __divmod__(self, y):
        return self._binop_right(divmod, y)

    def __rdivmod__(self, x):
        return self._binop_left(divmod, x)

    def __pow__(self, y):
        return self._binop_right(op.pow, y)

    def __rpow__(self, x):
        return self._binop_left(op.pow, x)

    def __lshift__(self, y):
        return self._binop_right(op.lshift, y)

    def __rlshift__(self, x):
        return self._binop_left(op.lshift, x)

    def __rshift__(self, y):
        return self._binop_right(op.rshift, y)

    def __rrshift__(self, x):
        return self._binop_left(op.rshift, x)

    def __and__(self, y):
        return self._binop_right(op.and_, y)

    def __rand__(self, x):
        return self._binop_left(op.and_, x)

    def __xor__(self, y):
        return self._binop_right(op.xor, y)

    def __rxor__(self, x):
        return self._binop_left(op.xor, x)

    def __or__(self, y):
        return self._binop_right(op.or_, y)

    def __ror__(self, x):
        return self._binop_left(op.or_, x)

    def __neg__(self):
        return Delayed(op.neg, self)

    def __pos__(self):
        return Delayed(op.pos, self)

    def __abs__(self):
        return Delayed(op.abs, self)

    def __invert__(self):
        return Delayed(op.invert, self)

    def __complex__(self):
        return Delayed(complex, self)

    def __int__(self):
        return Delayed(int, self)

    def __float__(self):
        return Delayed(float, self)

    def __round__(self, n=None):
        return Delayed(round, self)

    def __ceil__(self):
        return Delayed(math.ceil, self)

    def __floor__(self):
        return Delayed(math.floor, self)

    def __trunc__(self):
        return Delayed(math.trunc, self)

    def __eq__(self, y):
        return self._binop_right(op.eq, y)

    def __ne__(self, y):
        return self._binop_right(op.ne, y)

    def __lt__(self, y):
        return self._binop_right(op.lt, y)

    def __le__(self, y):
        return self._binop_right(op.le, y)

    def __gt__(self, y):
        return self._binop_right(op.gt, y)

    def __ge__(self, y):
        return self._binop_right(op.ge, y)
