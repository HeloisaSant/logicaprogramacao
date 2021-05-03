
import json
texto = '''{ "fiec": "instituicao_feliz", "alunos": [5,6,9], "prof": { "ti": "Fillipe "}} '''
resultados = json.loads(texto)

print(resultados)

print(resultados['fiec'])

print(len(resultados['alunos']))

print(resultados['prof'])
print(resultados['prof']['ti'])
print(resultados['prof']['ti']['hard'])
