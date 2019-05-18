WHITE=white
BLACK=black

DESTINATION_PDFS=../../PDFs-to-print

PDFs: letter a4

letter:
	mkdir -p ${DESTINATION_PDFS}
	make letterblackblack
	mv black.pdf ${DESTINATION_PDFS}/${BLACK}-letter-black.pdf
	make letterblackgray
	mv black.pdf ${DESTINATION_PDFS}/${BLACK}-letter-gray.pdf
	make letterblackwhite
	mv black.pdf ${DESTINATION_PDFS}/${BLACK}-letter-white.pdf
	make letterwhitewhite
	mv white.pdf ${DESTINATION_PDFS}/${WHITE}-letter.pdf

a4:
	mkdir -p ${DESTINATION_PDFS}
	make a4blackblack
	mv black.pdf ${DESTINATION_PDFS}/${BLACK}-a4-black.pdf
	make a4blackgray
	mv black.pdf ${DESTINATION_PDFS}/${BLACK}-a4-gray.pdf
	make a4blackwhite
	mv black.pdf ${DESTINATION_PDFS}/${BLACK}-a4-white.pdf
	make a4whitewhite
	mv white.pdf ${DESTINATION_PDFS}/${WHITE}-a4.pdf

clean:
	rm -f *.aux *.data *.log *.pdf

data:
	WHITE=${WHITE} BLACK=${BLACK} python3 combine.py

letterblackblack: data
	xelatex black.tex
	rm -f common.aux black.aux black.log

letterblackgray: data
	xelatex "\\def\\BLACKBACKGROUNDGRAY{}\\input{black.tex}"
	rm -f common.aux black.aux black.log

letterblackwhite: data
	xelatex "\\def\\BLACKBACKGROUNDWHITE{}\\input{black.tex}"
	rm -f common.aux black.aux black.log

letterwhitewhite: data
	xelatex white.tex
	rm -f common.aux white.aux white.log

a4blackblack: data
	xelatex "\\def\\AFOURPAPER{}\\input{black.tex}"
	rm -f common.aux black.aux black.log

a4blackgray: data
	xelatex "\\def\\AFOURPAPER{}\\def\\BLACKBACKGROUNDGRAY{}\\input{black.tex}"
	rm -f common.aux black.aux black.log

a4blackwhite: data
	xelatex "\\def\\AFOURPAPER{}\\def\\BLACKBACKGROUNDWHITE{}\\input{black.tex}"
	rm -f common.aux black.aux black.log

a4whitewhite: data
	xelatex "\\def\\AFOURPAPER{}\\input{white.tex}"
	rm -f common.aux white.aux white.log
