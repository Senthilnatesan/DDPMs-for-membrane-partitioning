#!/bin/bash

input_file="salm_10_final.txt"

# Looping through center values from 0 to 30
for center in {0..30}; do
    # Using awk to filter rows with the desired center value in the first column
    # and then saving the third column (z values) to a new file
    awk -v center="$center" '$1 == center {print $1, $2}' $input_file > "w${center}.dat"
done

mkdir windows
mv *dat windows/