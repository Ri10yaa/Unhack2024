import pandas as pd
import csv
size = pd.read_csv('./Student-Dataset-1/2nd/metadata.csv')
mf_size = int(size['Main Field Size'])
sf_size = float(size['Sub Field size'])
df = pd.read_csv('./Student-Dataset-1/2nd/CareAreas.csv',header=None)