from xml.etree import ElementTree
from urllib import urlopen
from re import sub, DOTALL
from sys import argv

URL = 'http://www.unimi.it/chiedove/listaPersoneXML.jsp?surname={surname}&name={name}&tipoOrganico=0'

surname = argv[ 1 ] if len( argv ) >= 2 else ''
name = argv[ 2 ] if len( argv ) == 3 else ''

try:
	data = urlopen( URL.format( name = name, surname = surname ) )
	data = sub( r'<script.*?</script>', '', data.read(), flags = DOTALL )
	root = ElementTree.fromstring( data )
	rows = next( root.iter( '{http://www.w3.org/1999/xhtml}tbody' ) ).iter( '{http://www.w3.org/1999/xhtml}tr' )
	print('\n'.join( '\t'.join( filter( None, [ _.text for _ in r.iter() ] ) ) for r in rows ))
except:
	pass
