import requests

def get_info() -> list:
    response = requests.get('https://restcountries.com/v3.1/all')
    all_countries = response.json()
    return all_countries


def populate_database_from_api_un():
    countries = get_info()
    un_countries = []
    count=1
    for country in countries:
        country_keys = country.keys()
        print(country['name']['official'], country['unMember'], count)
        c = {
        'name_official':  country['name']['official'],
        'name_community':  country['name']['common'],
        'independent':  country['independent'] if 'independent' in country_keys else None,
        'domain':  country['tld'][0] if 'tld' in country_keys else None,
        'un_member':  country['unMember'],
        'capital':  country['capital'] if 'capital' in country_keys else None,
        'continent':  country['region'],
        'sub_region':  country['subregion'] if 'subregion' in country_keys else None,
        'landlocked':  country['landlocked'],
        'population':  country['population'],
        'coordinates':  country['latlng'] if 'latlng' in country_keys else None,
        'capital_coordinates':  country['capitalInfo']['latlng'] if 'capital' in country_keys else None,
        'timezone':  country['timezones'],
        'cca2':  country['cca2'] if 'cca2' in country_keys else None,
        'cca3':  country['cca3'] if 'cca3' in country_keys else None,
        # 'cioc':  country['cioc'],
        'ccn3':  country['ccn3'] if 'ccn3' in country_keys else None,
        'boders': country['borders'] if 'borders' in country_keys else None,
        }
        un_countries.append(c)
        count += 1
    return un_countries


def populate_database_from_api_non_un():
    countries = get_info()
    non_un_countries = []
    count = 1
    for country in countries:
        print(country['name']['official'], country['unMember'], count)
        if not country['unMember']:
            c = {
            'name_official':  country['name']['official'],
            'name_community':  country['name']['common'],
            'independent':  country['independent'],
            'domain':  country['tld'][0],
            'un_member':  country['unMember'],
            'continent':  country['region'],
            'landlocked':  country['landlocked'],
            'population':  country['population'],
            'coordinates':  country['latlng'],
            'capital_coordinates':  country['capitalInfo']['latlng'],
            'timezone':  country['timezones'],
            'cca2':  country['cca2'],
            'cca3':  country['cca3'],
            'ccn3':  country['ccn3']
            }
            try:
                c['borders'] = country['borders']
                c['capital'] = country['captial']
            except KeyError:
                c['borders'] = ''
                c['captial'] = ''
            except Exception:
                print(f"found no borders/capital for country: {country['name']['official']}")
            non_un_countries.append(c)
        count += 1
    return non_un_countries