# Feito usando o módulo sinesp_client do Victor Torres
# Script escrito por Luan Devecchi

from sinesp_client import SinespClient
import warnings
import json
print('\033[1;31;40m##### Sinespy 1.0 #####\033[m\n  ')
plate = input('Digite a placa a ser consultada (sem o traco): ')
warnings.filterwarnings('ignore') ## Aqui eu ignoro as warnings pelo erro de certificado da Sinesp
c = SinespClient()

jsoncarro = c.search(plate)
json_res = json.dumps(jsoncarro, sort_keys=True,
                      indent=4, separators=(',', ': '))
parse = json.loads(json_res)
x_details = ("""
\033[1;31;40m##### Sinesp Consulta {} #####\033[m\n

Placa: {}       >>  Status: {}

Marca: {}

Modelo: {}

Ano: {}

Chassi: {}

Estado: {}

Cidade: {}

Cor: {}

### powered by sinesp_cidadao client ###
""".format(parse['date'],parse['plate'],parse['status_message'],parse['brand'],parse['model'],parse['year'],parse['chassis'],parse['state'],parse['city'],parse['color']))
print(x_details)