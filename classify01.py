#!/usr/bin/python

import sys
import getopt
import pandas as pd

def classify(i_file, col_name, out_name):
    df = pd.read_csv(f'{i_file}.csv')
    if col_name not in df:
        raise Exception('Column doesnot exist')

    df = df[[f'{col_name}']].replace('\n', ' ', regex=True)
    df = df[[f'{col_name}']].replace('\r', ' ', regex=True)
    # # multiple spaces into one
    df = df[[f'{col_name}']].replace('\s+', ' ', regex=True)
    
    uniq_diseases = df[f'{col_name}'].unique().tolist().sort()
    print(uniq_diseases)

    data = {"ABCESS": "ABCESS Issues"}
    CURRENT_WORD = "ABCESS"
    CURRENT_CLASS = "ABCESS Issues"

    for d in uniq_diseases:
        i = str(d)
        if CURRENT_WORD in i:
            data[i] = CURRENT_CLASS
        else:
            CURRENT_WORD = i.split(' ')[0]
            CURRENT_CLASS = i.split(' ')[0] + " Issues"
            data[i] = CURRENT_CLASS

def main(argv):
    d_col = ''
    i_file = ''
    o_file = ''
    try:
        opts, _ = getopt.getopt(argv, "i:c:o:", ["ifile=", "dcol=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -c <d_col> -o <outputfile>')
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -c <DiseaseColumnName> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            i_file = arg
        elif opt in ("-c", "--dcol"):
            d_col = arg
        elif opt in ("-o", "--ofile"):
            o_file = arg
    print(i_file,d_col,o_file)
    classify(i_file, d_col, o_file)


if __name__ == "__main__":
    main(sys.argv[1:])
