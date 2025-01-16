from pygal.maps.world import World

wm = World()
wm.title = 'População dos Paises da América do Norte'
wm.add('América do Norte', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')