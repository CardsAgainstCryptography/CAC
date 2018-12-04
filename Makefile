PDFs:
	cd src/booklet && make PDFs
	cd src/fullpage && make PDFs

PNGs:
	cd src/booklet && make PNGs
	cd src/individual-cards && make all

clean:
	cd src/booklet && make clean
	cd src/fullpage && make clean
	cd src/individual-cards && make clean
