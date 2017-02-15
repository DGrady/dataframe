import math
import operator as op

class ColumnExpression:
    
    def __init__(self, *args):
        
        if len(args) < 1:
            raise ValueError
        elif len(args) == 1:
            self.operator = None
            self.args = args[0]
        else:
            self.operator = args[0]
            self.args = args[1:]
            assert callable(self.operator)
    
    def __repr__(self):
        if self.operator is not None:
            return repr(self.operator) + repr(self.args)
        else:
            return 'Column(' + repr(self.args) + ')'
    
    def __str__(self):
        if self.operator is not None:
            return str(self.operator) + str(self.args)
        else:
            return 'Column(' + str(self.args) + ')'
    
    def __call__(self, frame):
        if self.operator is None:
            return frame[self.args]
        else:
            return self.operator(*(a(frame) if isinstance(a, ColumnExpression) else a for a in self.args))
    
    def _binop_right(self, operator, y):
        return ColumnExpression(operator, self, y)
    
    def _binop_left(self, operator, x):
        return ColumnExpression(operator, x, self)
    
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
        return ColumnExpression(op.neg, self)

    def __pos__(self):
        return ColumnExpression(op.pos, self)

    def __abs__(self):
        return ColumnExpression(op.abs, self)

    def __invert__(self):
        return ColumnExpression(op.invert, self)

    def __complex__(self):
        return ColumnExpression(complex, self)

    def __int__(self):
        return ColumnExpression(int, self)

    def __float__(self):
        return ColumnExpression(float, self)

    def __round__(self, n=None):
        return ColumnExpression(round, self)

    def __ceil__(self):
        return ColumnExpression(math.ceil, self)

    def __floor__(self):
        return ColumnExpression(math.floor, self)

    def __trunc__(self):
        return ColumnExpression(math.trunc, self)

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
