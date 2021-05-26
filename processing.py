import pandas as pd
import time

def process(filename):
    FP2_FILENAME = filename

    while(1):
        data = pd.read_csv(FP2_FILENAME, sep="\t", encoding='cp949')
        extractData = data.loc[:, ['7.00Hz', '9.00Hz', '11.00Hz', '13.00Hz']]
        if extractData.tail() == dataSample:
            break

        dataSample = extractData.tail()
        time.sleep(3)
        print(dataSample)
