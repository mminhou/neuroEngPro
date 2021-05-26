import pandas as pd
import time

FP2_FILENAME = 'factory/data/Fp2_FFT.txt'

data = pd.read_csv(FP2_FILENAME, sep="\t", encoding='cp949')
dataSample = data.loc[:, ['7.00Hz', '9.00Hz', '11.00Hz', '13.00Hz']]

print(data)
print(dataSample)

while(1):
    print(dataSample.tail())
    time.sleep(3)
