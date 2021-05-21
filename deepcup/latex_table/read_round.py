"""
@author: daviddeepwell
"""

import os
import pandas as pd

# read csv file containing everyone picks
def read_round(year, rnd):
    fname = str(year)+' Friendly Playoff Pool Round '+str(rnd)+'.csv'    # read file
    if os.path.isfile(fname):    
        # if file exists, return a pandas table
        fdata = pd.read_csv(fname, sep=',')
        
        # make the names of people the index (the row name)
        fdata.set_index('Name:', inplace=True)

        # over write the column headers
        header = fdata.columns.values
        if rnd == 1:
            header[1:] = ['T1','G1','T2','G2','T3','G3','T4','G4','T5','G5','T6','G6','T7','G7','T8','G8','WCC','ECC','SCC']
            #header[1:] = ['T1','G1','T2','G2','T3','G3','T4','G4','T5','G5','T6','G6','T7','G7','T8','G8','SC','R']
        elif rnd == 2:
            header[1:] = ['T1','G1','T2','G2','T3','G3','T4','G4']
        elif rnd == 3:
            header[1:] = ['T1','G1','T2','G2']
        elif rnd == 4:
            header[1:] = ['T1','G1']
        fdata.columns = header

        # Remove 'Games' in games columns and cast numbers to integer
        N_series = 2**(4-rnd)      # number of series in round
        for ind in ['G'+str(x) for x in range(1,N_series+1)]:
            if fdata[ind].values[0] == '- Games':
                # set to an integer because arithemtic won't work later (a python thing)
                fdata[ind].values[0] = '0 Games'
            # remove and cast
            fdata[ind] = fdata[ind].map(lambda x: x.rstrip(' Games')).astype(int)
    else:
        # if file does NOT exists, return a string
        fdata = '-'
    return fdata