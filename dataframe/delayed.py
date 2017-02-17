"""
A class for delayed evaluation
"""

class Delayed(object):
    """A delayed evaluation tree.

    """

    def __init__(self, function, *args, **kwargs):
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return '({}, {}, {})'.format(self.function, self.args, self.kwargs)

    def __repr__(self):
        return '({}, {}, {})'.format(self.function, self.args, self.kwargs)

    def __call__(self):
        return self.evaluate()

    def call(self, f):
        """Apply a function to this expression

        """
        return Delayed(f, self)

    def evaluate(self):
        """Evaluate this tree

        """

        return self.function(
            *(a.evaluate() if isinstance(a, Delayed) else a for a in self.args),
            **self.kwargs
        )

    def map_functions(self, f):
        """Apply ``f`` to every function in the tree

        """

        return Delayed(
            f(self.function),
            *(a.map_functions(f) if isinstance(a, Delayed) else a for a in self.args),
            **self.kwargs
        )

    def map_args(self, f):
        """Apply ``f`` to every argument in the tree

        """

        return Delayed(
            self.function,
            *(a.map_args(f) if isinstance(a, Delayed) else f(a) for a in self.args),
            **self.kwargs
        )
