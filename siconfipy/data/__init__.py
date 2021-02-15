import pandas as pd
import os

root = os.path.abspath(os.path.dirname(__file__))
br_cods = pd.read_csv(os.path.join(root, "br_cods.csv"))
