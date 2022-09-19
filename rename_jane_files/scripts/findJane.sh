#!/bin/bash

true > oldFiles.txt

files=$(grep ' jane ' ../data/list.txt | cut -d ' ' -f 3)
for file in $files; do
	proper_file=${file:1}
	if test -e ../"$proper_file"; then
		echo ../"$proper_file" >> oldFiles.txt;
	fi
done
echo "Done."