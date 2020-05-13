#!/usr/local/bin/python3

import glob
import os
import subprocess

def xelatex(basename):
    subprocess.run(["xelatex", '\def\BLEEDAREA{}\input{' + basename + '.tex}'], capture_output=True)
    os.remove(basename + ".aux")
    os.remove(basename + ".log")

def pdftopng(basename):
    subprocess.run(["convert", "-density", "300", "-geometry", "732x1101", basename + ".pdf", basename + ".png"], capture_output=True)

black_prefix = os.environ["BLACK"] if "BLACK" in os.environ else "black"
white_prefix = os.environ["WHITE"] if "WHITE" in os.environ else "white"
black_txt = "../" + black_prefix + ".txt"
white_txt = "../" + white_prefix + ".txt"

prefixes = [black_prefix, white_prefix]
sources = [black_txt, white_txt]
templates = ["black", "white"]

output_directory = "../../PNGs-to-print/individual-cards"
try:
    os.mkdir(output_directory)
except FileExistsError:
    pass

old_pngs = glob.glob(output_directory + "/*.png")
for old_png in old_pngs:
    subprocess.run(["rm", old_png])

j = 0

for i in range(len(sources)):
    print("Generating " + templates[i] + "_back.png")
    xelatex(templates[i] + "_back")
    pdftopng(templates[i] + "_back")
    os.remove(templates[i] + "_back.pdf")
    with open(templates[i] + "_front.tex") as front_template:
        front_tex_template = front_template.readlines()
    front_tex_template = "\n".join(front_tex_template)
    with open(sources[i]) as source:
        for line in source:
            line = line.rstrip()
            j += 1
            print("Generating {:s} card #{:d}: {:s}".format(templates[i], j, line))
            filename = "{:s}_FRONT{:03d}".format(prefixes[i], j)
            front_tex = front_tex_template.replace("CARDTEXTHERE", line)
            with open(filename + ".tex", 'w') as front:
                print(front_tex, file=front)
            xelatex(filename)
            os.remove(filename + ".tex")
            pdftopng(filename)
            os.remove(filename + ".pdf")
            subprocess.run(["mv", filename + ".png", output_directory])
            filename = "{:s}_BACK{:03d}".format(prefixes[i], j)
            subprocess.run(["cp", templates[i] + "_back.png", output_directory + "/" + filename + ".png"])
        os.remove(templates[i] + "_back.png")
