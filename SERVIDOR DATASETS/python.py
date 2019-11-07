import sys



import pandas as pd
import pandas_profiling
import numpy as np


df = pd.read_csv("./uploads/"+sys.argv[1])

#df.head();

#df.describe();

report = pandas_profiling.ProfileReport(df)
report.to_file("./uploads/"+sys.argv[1] +"report.html");
print("HECHO")