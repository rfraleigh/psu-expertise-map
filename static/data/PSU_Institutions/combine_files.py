import os
import json
import glob

files = glob.glob('master*.json')
#print(files)

data ={}
for ind,file in enumerate(files):
    if ind>-1:
        temp = json.loads(open(file,'r').read())
        data = {**data, **temp}
        print(len(data))
with open('merged_institutions.json','w') as f:
    f.write(json.dumps(data))
f.close()
