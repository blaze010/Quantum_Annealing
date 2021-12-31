import json
from json import loads, dumps

def dwave_to_gurobi(dicte, test_name):
	#ke = [el[0] for el in dicte.keys()]
	#for el in dicte.keys():
	#	ke.append(el[1])
	#ke = set(ke)
	#ke = sorted(list(ke))
	#variab = [("x"+str(el[0])+str(el[1])) for el in ke]
	out_dicte = dumps({str(k): v for k, v in dicte.items()})
	#for (key,value) in dicte.items():
	#	k1 = "x"+str(key[0][0])+str(key[0][1])
	#	k2 = "x"+str(key[1][0])+str(key[1][1])
	#	out_dicte[k1+k2] = value
	with open('/home/blaze010/D-Wave_Gurobi_Interfacer/D-Wave_QUBOs/'+test_name+'_qubo.json', 'w') as convert_file:
     		convert_file.write(json.dumps(out_dicte))
	

