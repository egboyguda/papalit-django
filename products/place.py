import requests

BASE_URL = 'https://isaacdarcilla.github.io/philippine-addresses/'

def fetch(json_path_name):
    try:
        response = requests.get(f'{BASE_URL}{json_path_name}.json')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return str(e)

def regions():
    try:
        data = fetch('region')
        return [
            {
                'id': region['id'], # type: ignore
                'psgc_code': region['psgc_code'], # type: ignore
                'region_name': region['region_name'], # type: ignore
                'region_code': region['region_code'] # type: ignore
            }
            for region in data
        ]
    except Exception as e:
        return str(e)

def region_by_code(code):
    try:
        data = fetch('region')
        return next((region for region in data if region['region_code'] == code), None)
    except Exception as e:
        return str(e)

def provinces(code):
    try:
        data = fetch('province')
        return [
            {
                'psgc_code': province['psgc_code'],
                'province_name': province['province_name'],
                'province_code': province['province_code'],
                'region_code': province['region_code']
            }
            for province in data if province['region_code'] == code
        ]
    except Exception as e:
        return str(e)

def provinces_by_code(code):
    try:
        data = fetch('province')
        return [
            {
                'psgc_code': province['psgc_code'],
                'province_name': province['province_name'],
                'province_code': province['province_code'],
                'region_code': province['region_code']
            }
            for province in data if province['region_code'] == code
        ]
    except Exception as e:
        return str(e)

def province_by_name(name):
    try:
        data = fetch('province')
        return next((province for province in data if province['province_name'] == name), None)
    except Exception as e:
        return str(e)

def cities(code):
    try:
        data = fetch('city')
        return [
            {
                'city_name': city['city_name'],
                'city_code': city['city_code'],
                'province_code': city['province_code'],
                'region_desc': city['region_desc'],
            }
            for city in data if city['province_code'] == code
        ]
    except Exception as e:
        return str(e)

def barangays(code):
    try:
        data = fetch('barangay')
        return [
            {
                'brgy_name': brgy['brgy_name'],
                'brgy_code': brgy['brgy_code'],
                'province_code': brgy['province_code'],
                'region_code': brgy['region_code'],
            }
            for brgy in data if brgy['city_code'] == code
        ]
    except Exception as e:
        return str(e)
