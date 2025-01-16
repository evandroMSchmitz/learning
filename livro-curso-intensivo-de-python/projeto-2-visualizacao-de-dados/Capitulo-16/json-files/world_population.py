import json

from pygal.maps.world import World
from pygal.style import LightColorizedStyle, RotateStyle

from country_codes import get_country_code

# Carregar os dados em uma lista
filename = 'Capitulo-16\\data\\population_data.json'
with open(filename) as file:
    pop_data = json.load(file)

# Construir um dicionário com os dados das populações
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        # Tratamento para casos onde a população é um número de ponto flutuante
        population = int(float(pop_dict['Value']))

        code = get_country_code(country_name)
        # Tratamento para o caso dos códigos não serem encontrados
        if code:
            cc_populations[code] = population

# Agrupar os paises em 3 níveis populacionais
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# Verificar quantos paises estão em cada nível
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = 'População Mundial em 2010, por pais'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')