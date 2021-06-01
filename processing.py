import pandas as pd
import time

def biomarkers():
    BIOMARKERS_FILENAME = "factory/data/Biomarkers.txt"
    bioData = pd.read_csv(BIOMARKERS_FILENAME, sep="\t", encoding='cp949')
    # extractFp2BetaData = bioData.loc[:, ['Fp2_Beta(%)']]
    # Extract Fp2 Beta Data
    fp2BetaData = bioData['Fp2_Beta(%)']
    print(fp2BetaData.mean())       # Average of Fp2 Beta Data

    # return True False
    condition = fp2BetaData > 1.0

    # condition fp2 Beta Data
    conditionfp2BetaData = fp2BetaData[condition]
    print(conditionfp2BetaData.mean())      # Average of Condition Fp2 Beta Data


def ssvepProcess():
    # FP2_FILENAME = filename
    FP2_FILENAME = "factory/data/Fp2_FFT.txt"

    fp2Data = pd.read_csv(FP2_FILENAME, sep="\t", encoding='cp949')

    upData = fp2Data[['6.60Hz', '6.80Hz', '7.00Hz', '7.20Hz', '7.40Hz']]
    print(upData.mean().mean())

    downData = fp2Data[['8.60Hz', '8.80Hz', '9.00Hz', '9.20Hz', '9.40Hz']]
    print(downData.mean().mean())

    leftData = fp2Data[['10.60Hz', '10.80Hz', '11.00Hz', '11.20Hz', '11.40Hz']]
    print(leftData.mean().mean())

    rightData = fp2Data[['12.60Hz', '12.80Hz', '13.00Hz', '13.20Hz', '13.40Hz']]
    print(rightData.mean().mean())
    #
    # while(1):
    #     data = pd.read_csv(FP2_FILENAME, sep="\t", encoding='cp949')
    #     extractData = data.loc[:, ['7.00Hz', '9.00Hz', '11.00Hz', '13.00Hz']]
    #     if extractData.tail() == dataSample:
    #         break
    #
    #     dataSample = extractData.tail()
    #     time.sleep(3)
    #     print(dataSample)

# biomarkers()
ssvepProcess()