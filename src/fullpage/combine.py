sources = ["../black.txt", "../white.txt"]
destinations = ["black.data", "white.data"]

preamble = "\\noindent \\begin{tikzpicture}[remember picture, overlay] \\node [shift={(0.1in,0in)}]  at (current page.south west) { \\begin{tikzpicture}[remember picture, overlay,yscale=-1,line width=1pt] "
pattern = "\\node [below right,text width=1.86in] at (\LEFTMARGIN + %d * \CARDWIDTH, \TOPMARGIN + %d * \CARDHEIGHT) { \\fontsize{12}{0}\\selectfont %s };"
postamble = "\\end{tikzpicture} }; \\end{tikzpicture} \\newpage \\backgroundreverse"

for i in range(len(sources)):
	with open(sources[i]) as source:
		with open(destinations[i], 'w') as destination:
			it = 0
			for line in source:
				if (it % 9) == 0:
					if it > 0:
						print(postamble, file=destination)
						print("\\newpage", file=destination)
					print(preamble, file=destination)
				content = line.strip()
				col = (it % 3)
				row = (it // 3) % 3
				print(pattern % (col, row, content), file=destination)
				it += 1
			print(postamble, file=destination)
