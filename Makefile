all: pyenconv.py
	# cp -f pyenconv.py pyenconv
	echo '#'!/usr/bin/env python3$$'\n'"`cat pyenconv.py`" > pyenconv
	chmod +x pyenconv
install: pyenconv
	install -cv pyenconv /usr/local/bin
.PHONY: clean
clean:
	rm -f pyenconv
