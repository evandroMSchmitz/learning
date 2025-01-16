from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    """Devolve o código de duas letras do Pygal para um país, dado o seu nome."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    if country_name == 'Yemen, Rep.':
        return 'ye'
    elif country_name == 'Korea, Dem. Rep.':
        return 'kp'
    elif country_name == 'Korea, Rep.':
        return 'kr'
    elif country_name == 'Venezuela, RB':
        return 've'
    elif 'Bolivia':
        return 'bo'
    elif country_name == 'Egypt, Arab Rep.':
        return 'eg'
    elif country_name == 'Congo, Dem. Rep.':
        return 'cd'
    elif country_name == 'Congo, Rep.':
        return 'cg'
    elif country_name == 'Vietnam':
        return 'vn'
    elif country_name == 'Iran, Islamic Rep.':
        return 'ir'
    elif country_name == 'Hong Kong SAR, China':
        return 'hk'
    elif country_name == 'Tanzania':
        return 'tz'
    elif country_name == 'Libya':
        return 'ly'

    
    # se o pais não foi encontrado, devolve None
    return None