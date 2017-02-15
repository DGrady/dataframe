import pandas as pd

from .column_expression import ColumnExpression

def name(label, frame : pd.DataFrame):
    """Assign a name to a data frame

    ``pandas`` doesn't provide a standard location for a label that's
    associated with the entire frame; we use the `name` attribute of
    the column index.

    """

    if callable(label):
        frame.columns.name = label(frame.columns.name)
    else:
        frame.columns.name = label
    return frame


def select(labels, frame : pd.DataFrame):
    """Restrict ``frame`` to a subset of its columns.

    The relational projection operator.

    """

    if callable(labels):
        return frame[list(map(labels, frame.columns))]
    else:
        return frame[list(labels)]


def filter(condition : ColumnExpression, frame : pd.DataFrame):
    return frame[condition(frame)]
