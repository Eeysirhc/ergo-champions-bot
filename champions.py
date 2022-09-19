##############################
# Author: eeysirhc
# Date written: 2022-08-12
# Last updated: 2022-09-19
##############################

import os 
import requests
import pandas as pd
import tabulate

ranks = pd.read_csv("rarity.csv")
ranks['Champion: '] = ranks['Champion: '].astype('str')

def champ(id_lookup):
	df = ranks[ranks['Champion: '] == id_lookup]
	return(df.to_markdown(tablefmt="grid", index=False))  


