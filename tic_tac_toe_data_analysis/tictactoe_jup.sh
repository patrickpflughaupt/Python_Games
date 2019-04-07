#!/usr/bin/bash
# Convert python file to notebook
# Run notebook

python3 make_nb.py tictactoe_analysis.py
mv tictactoe_analysis.py.* tictactoe_analysis.ipynb
jupyter notebook tictactoe_analysis.ipynb

