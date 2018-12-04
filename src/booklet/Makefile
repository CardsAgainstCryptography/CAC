DESTINATION_PDFS=../../PDFs-to-print
DESTINATION_PNGS=../../PNGs-to-print

PDFs:
	mkdir -p ${DESTINATION_PDFS}
	xelatex "\\def\LINES{}\\input{booklet-outside.tex}"
	xelatex "\\def\LINES{}\\input{booklet-inside.tex}"
	xelatex "\\def\AFOURPAPER{}\\input{booklet-combined.tex}"
	mv booklet-combined.pdf ${DESTINATION_PDFS}/booklet-a4.pdf
	xelatex "\\def\LETTERPAPER{}\\input{booklet-combined.tex}"
	mv booklet-combined.pdf ${DESTINATION_PDFS}/booklet-letter.pdf
	make clean

PNGs:
	mkdir -p ${DESTINATION_PNGS}
	xelatex "\\def\BLEEDAREA{}\\input{booklet-outside.tex}"
	convert -density 300 -geometry 1392x1092 booklet-outside.pdf ${DESTINATION_PNGS}/booklet-outside.png
	xelatex "\\def\BLEEDAREA{}\\input{booklet-inside.tex}"
	convert -density 300 -geometry 1392x1092 booklet-inside.pdf ${DESTINATION_PNGS}/booklet-inside.png
	make clean

clean:
	rm -f *.aux *.log *.pdf
