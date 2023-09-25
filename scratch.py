import csv,json 
from models import NearEarthObject,CloseApproach
from database import NEODatabase
from extract import load_neos

neos_path = 'data/neos.csv'
neos = load_neos(neo_csv_path=neos_path)



neos = []
with open(neos_path,'r') as nf:
    neos_reader = csv.DictReader(nf)    
    i = 0
    
    for line in neos_reader:
        neo_temp = NearEarthObject(info=line)
        neos.append(neo_temp)
        #print(neo_temp)
        # if line['pdes'] == '1865':
        #     print(neo_temp.designation)
        #     print(neo_temp.designation == '1865')
        #     print(line)

        

        


cad_path = 'data/cad.json'
cads = []
with open(cad_path,'r') as cf:
    cad_data = json.load(cf)
    temp_dict = {}
    keys = cad_data['fields']
    for line in cad_data['data']:
        for i,v in enumerate(line):
            temp_dict[keys[i]] = line[i]
        cads.append(CloseApproach(info=temp_dict))

print('len neos:',len(neos))
neo_db = NEODatabase(neos=neos,approaches=cads)
print(neo_db._approaches)    
    
