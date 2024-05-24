#!/bin/bash

for f in words-lists/*.csv
do
	awk -F ',' '{print $2;}' "$f"
done | sort | uniq -c | sort -nr
