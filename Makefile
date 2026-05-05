PYTHON=/usr/bin/env python3

chiedove: chiedove-unimi/__main__.py
	python3 -m zipapp chiedove-unimi -o chiedove_unimi -p '$(PYTHON)'

clean:
	@rm chiedove_unimi
