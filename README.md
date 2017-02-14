# dataframe

[Pandas](http://pandas.pydata.org/) provides an extremely useful, high-performance library for working with in-memory tabular data sets in Python. However, the Pandas API is extremely complex and ramified: it provides many ways to accomplish common tasks, the names of methods are misleading when compared to standard SQL or standard Python idioms, and the behavior of methods is often surprising.

This library aims to provide a dramatically simpler set of basic verbs for working with data frames. It seeks to align its terminology and semantics as much as possible with SQL first and standard Python idioms second and to provide non-surprising default behavior. And it attempts to standardize the argument names and order of arguments to provide an API that fits fluently into the functional programming idiom.
