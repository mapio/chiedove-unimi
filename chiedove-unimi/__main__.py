from json import loads
from re import finditer, DOTALL
from sys import argv
from urllib.request import urlopen

SEARCH_URL = 'https://www.unimi.it/it/views/ajax?_wrapper_format=drupal_ajax' 
data = 'title={}&ur_tipo_ruolo_target_id=All&view_name=chi_e_dove&view_display_id=block_1&view_args=&view_path=%2Fit%2Fchi-e-dove&view_base_path=&view_dom_id=0&pager_element=0&_drupal_ajax=1'

DETAIL_URL = 'https://www.unimi.it/it/ugov/person/'
    
name = argv[1]

try:
    people = []
    for item in loads(urlopen(SEARCH_URL, data.format(name).encode('utf-8')).read().decode('utf-8')):
        if item['command'] == 'insert':
            for match in finditer(r'<a href="/it/ugov/person/([^"]+)"', item['data']):
                people.append(match.group(1))

    DETAIL_URL = 'https://www.unimi.it/it/ugov/person/'
    for person in people:
        data = urlopen(DETAIL_URL + person).read().decode('utf-8')
        info = [match.group(1).strip() for match in finditer(r'<title>([^<]+)\|.*</title>', data)]
        if not name in info[0].lower(): continue
        info.extend(match.group(1).strip() for match in finditer(r'<a href="mailto:([^"]+)"', data))
        info.extend(match.group(1).strip() for match in finditer(r'<div\s+class="pad-icon">([^<]+)</div>', data))
        print('\t'.join(info))
except:
    pass