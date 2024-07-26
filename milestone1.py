import pandas as pd
import csv
size = pd.read_csv('./Dataset-0/1st/metadata.csv')
mf_size = int(size['Main Field Size'])
sf_size = float(size['Sub Field size'])
df = pd.read_csv('./Dataset-0/1st/CareAreas.csv',header=None)
file = open('./Dataset-0/1st/Mainfield.csv','w',newline='')
writer = csv.writer(file)
for row in df.itertuples():
    tx = row[2]+mf_size
    ty = row[4]+mf_size
    data = [row[1],row[2],tx,row[4],ty]
    writer.writerow(data)


file1 = open('./Dataset-0/1st/Subfield.csv','w',newline='')
writer2 = csv.writer(file1)
i=0
for row in df.itertuples():
    sy = row[4]
    while(sy <= row[5]):
        sy = sy + sf_size
        b=1
        sx=row[2]
        while(sx <= row[3]):
            sx = sx + sf_size
            data1 = [i,sx-sf_size,sx,sy-sf_size,sy,row[1]]
            writer2.writerow(data1)
            print(data1)
            i=i+1
            
    
        



    
