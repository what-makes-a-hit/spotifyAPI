
# Dependencies and Setup
import numpy as np

import json
import time

import requests
import pandas as pd
from pandas.io.json import json_normalize
from pprint import pprint
import numpy as np

import json
import time

import requests
import pandas as pd
from pandas.io.json import json_normalize
from pprint import pprint
''' 
unemployment data  
Source : 
https://data.bls.gov/timeseries/LNU04000000?periods=Annual+Data&periods_option=specific_periods&years_option=all_years
'''
unemployment = {'1975': '8.5',
                '1976': '7.7',
                '1977': '7.1',
                '1978': '6.1',
                '1979': '5.8',
                '1980': '7.1',
                '1981': '7.6',
                '1982': '9.7',
                '1983': '9.6',
                '1984': '7.5',
                '2000': '4.0',
                '2001': '4.7',
                '2002': '5.8',
                '2003': '6.0',
                '2004': '5.5',
                '2005': '5.1',
                '2006': '4.6',
                '2007': '4.6',
                '2008': '5.8',
                '2009': '9.3'}
ind = [i for i in range(20)]
unemploymentData = pd.DataFrame(unemployment.items(), columns=['Year', 'Unemployment'])
print(unemploymentData)
