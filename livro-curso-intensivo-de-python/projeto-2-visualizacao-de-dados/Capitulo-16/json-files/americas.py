from pygal.maps.world import World

wm = World()

wm.title = "Américas do Norte, Central e do Sul"

wm.add('América do Norte', ['ca', 'mx', 'us'])
wm.add('América Central', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv', 'cu', 'ht', 'do', 'jm'])
wm.add('América do Sul', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')