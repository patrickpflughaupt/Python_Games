#!/usr/bin/env python3
# import libraries
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt

def file_reader_score(path, skiprows):
    # Function used for importing csv as dataframe for analysis
    # Read multiple files into one long dataframe whilst adding custom columns
    # path: the path to the file
    # skiprows: line numbers to skip (0-indexed) or number of lines to skip (int) at the start of the file - used to skip the comment section at the beginning
    df = pd.read_csv(path, sep = ',', index_col=None, names=('Player','Score_P','DateTime_P','Computer','Score_C','DateTime_C'), header=None, skiprows = skiprows)
    return(df)

def file_reader_grid(path, skiprows):
    # Function used for importing csv as dataframe for analysis
    df = pd.read_csv(path, sep = ',', index_col=None, names=('DateTime_P','0','1','2','3','4','5','6','7','8','9'), header=None, skiprows = skiprows)
    return(df)

df_score = pd.concat((file_reader_score(f, skiprows=3) for f in sorted(glob('tictactoe_score_database.csv'))))
df_grid = pd.concat((file_reader_grid(f, skiprows=5) for f in sorted(glob('tictactoe_gridpoint_database_player.csv'))))

df_score
df_grid
