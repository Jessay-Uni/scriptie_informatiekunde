#!/bin/bash

yellow='\033[1;33m'
no_col='\033[0m'

echo -e "    ${yellow}Name a directory to place annotation files:${no_col} "
read -p "    " dirname

mkdir $dirname || exit 1
touch "./${dirname}/annotations.tsv"


echo -e "    ${yellow}Created directory '${dirname}' containing annotations.tsv file${no_col}"


python3 <<END_OF_PYTHON
import csv

count = 0

with open('./experiment-2.csv', 'r') as data_csv:
    text = csv.reader(data_csv)
    #line_cut = []

    for line in text:
        title = line[2]
        text = line[3]
        id = line[0]

        with open(f"./${dirname}/{count}_{id}.txt", 'w') as writefile:
            writefile.write(title)
            writefile.write("\n\n")
            writefile.write(text)

            #for word in text.split():
                #line_cut.append(word + " ")

                #if len(line_cut) == 7:
                 #   line_cut.append("\n")
                 #   writefile.writelines(line_cut)
                 #   line_cut.clear()

            #if line_cut:
             #   writefile.writelines(line_cut)
              #  line_cut.clear()

        count += 1



END_OF_PYTHON

echo -e "    ${yellow}Created .txt file for every news article!${no_col}"

rm "${dirname}/0_.txt"
mv "annotator.py" $dirname || exit 1

echo -e "    ${yellow}Moved annotator script to '${dirname}'${no_col}"
echo -e "    ${yellow}Done!${no_col}"

