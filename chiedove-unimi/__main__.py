from html import unescape
from re import finditer
from sys import argv
from urllib import request, parse

def decode_cfemail(encoded):
    key = int(encoded[:2], 16)
    return ''.join(chr(int(encoded[i:i+2], 16) ^ key) for i in range(2, len(encoded), 2))

SEARCH_URL = 'https://www.unimi.it/it/chi-e-dove'
DETAIL_URL = 'https://www.unimi.it/it/ugov/person/'

if len(argv) < 2:
    print('chiedove_unimi: specifica il <cognome>')
    exit(1)
    
name = argv[1]

url = SEARCH_URL + '?' + parse.urlencode({
    'cognome': name,
    'nome': '',
    'ur_tipi_ruoli_target_id': 'All',
})

response = request.urlopen(
    request.Request(url, headers = {'User-Agent': 'Mozilla/5.0'})
).read().decode('utf-8')

try:
  people = []
  for match in finditer(r'<a href="/it/ugov/person/([^"]+)"', response):
      slug = match.group(1)
      if slug not in people:
          people.append(slug)

  for person in people:
      data = request.urlopen(request.Request(DETAIL_URL + person, headers = {'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
      person_name = unescape(next(match.group(1).strip() for match in finditer(r'<title>([^<]+)\|.*</title>', data)))
      if not name in person_name.lower(): continue
      phones = [match.group(1).strip().replace(' ', '') for match in finditer(r'<div\s+class="pad-icon">([^<]+)</div>', data)]
      emails = [decode_cfemail(match.group(1)) for match in finditer(r'data-cfemail="([^"]+)"', data)]
      sedi = [match.group(1).strip() for match in finditer(r'<p class="ugov-indirizzo">([^<]+)</p>', data)]
      print(person_name)
      if sedi:
          print('  Sede: ' + ', '.join(sedi))
      if phones:
          print('  Tel: ' + ', '.join(phones))
      if emails:
          print('  Email: ' + ', '.join(emails))
except:
   print('Si è verificato un errore nel recupero, o estrazione, dei dati.')   