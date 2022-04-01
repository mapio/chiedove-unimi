from json import loads
from re import finditer, DOTALL
from sys import argv
from urllib import request, parse

SEARCH_URL = 'https://www.unimi.it/it/views/ajax'
DETAIL_URL = 'https://www.unimi.it/it/ugov/person/'

name = argv[1]

data = parse.urlencode({
    'cognome': name,
    'nome': '',
    'ur_tipo_ruolo_target_id': 'All',
    'view_name': 'chi_e_dove',
    'view_display_id': 'block_1',
    'view_args': '',
    'view_path': '/node/7663',
    'view_base_path': '',
    'view_dom_id': 'ece5376832f8559006242f5655147c55cd303248b9c1f7cc4627f7021f4537d4',
    'pager_element': '1',
    '_drupal_ajax': '1',
}).encode('utf-8')

response = request.urlopen(
    request.Request(SEARCH_URL, data = data, headers = {'User-Agent': 'Mozilla/5.0'})
).read().decode('utf-8')

#try:
people = []
for item in loads(response):
    if item['command'] == 'insert':
        for match in finditer(r'<a href="/it/ugov/person/([^"]+)"', item['data']):
            people.append(match.group(1))

DETAIL_URL = 'https://www.unimi.it/it/ugov/person/'
for person in people:
    data = request.urlopen(request.Request(DETAIL_URL + person, headers = {'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
    info = [match.group(1).strip() for match in finditer(r'<title>([^<]+)\|.*</title>', data)]
    if not name in info[0].lower(): continue
    info.extend(match.group(1).strip() for match in finditer(r'<a href="mailto:([^"]+)"', data))
    info.extend(match.group(1).strip() for match in finditer(r'<div\s+class="pad-icon">([^<]+)</div>', data))
    print('\t'.join(info))
#except:
#   pass