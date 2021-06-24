

class MyClass:

    def __init__(self, x):
        self.x = x

myvar = MyClass(x)
y = myvar.x

def func(x, kw=3.0):
    """[summary]

    Args:
        x ([type]): [description]

    Raises:
        Exception: [description]
    """

# use specific hard-wired values as the initial selected values
selection = alt.selection_single(
    name='Select',
    fields=['Major_Genre', 'MPAA_Rating'],
    init={'Major_Genre': 'Drama', 'MPAA_Rating': 'R'},
    bind={'Major_Genre': alt.binding_select(options=genres), 'MPAA_Rating': alt.binding_radio(options=mpaa)}
)

import numpy as np
idea = [3.0 , 4.0] 

ImportError 



def func(x, y=True):
    print(sd)


label = alt.selection_single(
    encodings=['x'], # limit selection to x-axis value
    on='mouseover',  # select on mouseover events
    nearest=True,    # select data point nearest the cursor
    empty='none'     # empty selection includes no data points
)




