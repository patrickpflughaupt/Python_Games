#!/usr/bin/env python3
# import libraries
import pandas as pd
from glob import glob
import matplotlib.pyplot as plt

def file_reader_score(path, skiprows):
    df = pd.read_csv(path, sep = ',', index_col=None, names=('Player','Score_P','DateTime_P','Computer','Score_C','DateTime_C'), header=None, skiprows = skiprows)
    return(df)

def file_reader_grid(path, skiprows):
    df = pd.read_csv(path, sep = ',', index_col=None, names=('DateTime_P','0','1','2','3','4','5','6','7','8','9'), header=None, skiprows = skiprows)
    return(df)

df_score = pd.concat((file_reader_score(f, skiprows=3) for f in sorted(glob('tictactoe_score_database.csv'))))
df_grid = pd.concat((file_reader_grid(f, skiprows=5) for f in sorted(glob('tictactoe_gridpoint_database_player.csv'))))

df_score
df_grid
