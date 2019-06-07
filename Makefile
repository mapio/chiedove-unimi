PYTHON=/usr/bin/env python3

chiedove: chiedove-unimi/__main__.py
	zip --quiet --junk-paths chiedove-unimi chiedove-unimi/__main__.py
	echo '#!$(PYTHON)' > chiedove
	cat chiedove-unimi.zip >> chiedove
	rm chiedove-unimi.zip
	chmod a+x chiedove

clean:
	@rm chiedove chiedove.zip
