from __future__ import absolute_import, division, print_function
from larray_editor.api import *

"""Array editor test"""
import numpy as np
import pandas as pd



df = pd.DataFrame.from_items([('A', [1, 2, 3]), ('B', [4, 5, 6])],
                             orient='index', columns=['one', 'two', 'three'])

# data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])
# data[:] = [(1,2.,'Hello'), (2,3.,"World")]
# df_mixed_dtypes = pd.DataFrame(data, index=['first', 'second'])

edit({'df': df})
