#!/usr/bin/bash

for file in tictactoe_score_database.csv
do
    cut -f2 -d"," $file | sort -n | tail -1
    cut -f5 -d"," $file | sort -n | tail -1
done
