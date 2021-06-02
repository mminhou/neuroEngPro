import pandas as pd
from matplotlib import pyplot as plt
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
    print(FP2_FILENAME)

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

def p300Processing(filePath):
    RAWDATA_FILENAME = filePath
    # RAWDATA_FILENAME = "factory/data/Rawdata.txt"
    forCompareData = pd.read_csv(RAWDATA_FILENAME, sep="\t", encoding='cp949').loc[:, ['Time', 'EEG_Fp2']].tail()

    while(1):
        '''
        rawData = pd.read_csv(RAWDATA_FILENAME, sep="\t", encoding='cp949')
        extractData = rawData.loc[:, ['Time', 'EEG_Fp2']]
        # 종료를 위한 예외처리
        if extractData.tail().equals(forCompareData):
            print('True')
            break
        forCompareData = extractData.tail()
        '''
        rawData = pd.read_csv(RAWDATA_FILENAME, sep="\t", encoding='cp949')
        extractData = rawData.loc[-200:, ['Time', 'EEG_Fp2']]
        # 시간표현 분의 표현 issue -> 분 뽑아내서 * 60 한 후 초에 더해준다.
        src = float(extractData['Time'][0][5:7]) * 60 + float(extractData['Time'][0][8:14])  # Init time
        # forCompareData = extractData.tail()
        # print(extractData['Time'].str[5:7]) // min
        # print(extractData['Time'].str[8:14]) // seconds
        extractData['Time'] = extractData['Time'].str[5:7].astype('float') * 60 + \
                              extractData['Time'].str[8:14].astype('float')

        x = extractData['Time']
        y = extractData['EEG_Fp2']
        plt.plot(x, y)

        leftCondition = extractData['Time'] < src + 1.5
        leftSide = extractData[leftCondition]
        plt.plot(x[leftCondition], y[leftCondition], color='red')
        left = leftSide['EEG_Fp2'].mean()
        print(leftSide['EEG_Fp2'].mean())

        rightCondition = extractData['Time'].between(src + 1.5, src + 3)
        rightSide = extractData[rightCondition]
        plt.plot(x[rightCondition], y[rightCondition], color='blue')
        right = rightSide['EEG_Fp2'].mean()
        print(rightSide['EEG_Fp2'].mean())

        upCondition = extractData['Time'].between(src + 3, src + 4.5)
        upSide = extractData[upCondition]
        plt.plot(x[upCondition], y[upCondition], color='yellow')
        up = upSide['EEG_Fp2'].mean()
        print(upSide['EEG_Fp2'].mean())

        downCondition = extractData['Time'].between(src + 4.5, src + 6)
        downSide = extractData[downCondition]
        plt.plot(x[downCondition], y[downCondition], color='green')
        down = downSide['EEG_Fp2'].mean()
        print(downSide['EEG_Fp2'].mean())

        plt.show()

        if max([left, right, up, down]) == left:
            print("left")
        elif max([left, right, up, down]) == right:
            print("right")
        elif max([left, right, up, down]) == up:
            print("up")
        elif max([left, right, up, down]) == down:
            print("down")

        time.sleep(6)



    '''rawData = pd.read_csv(RAWDATA_FILENAME, sep="\t", encoding='cp949')
    extractData = rawData.loc[-20:, ['Time', 'EEG_Fp2']]
    print(extractData)'''
    # extractData = rawData.tail().loc[:, ['Time', 'EEG_Fp2']]
'''
    # 시간표현 분의 표현 issue -> 분 뽑아내서 * 60 한 후 초에 더해준다.
    src = float(extractData['Time'][0][5:7]) * 60 + float(extractData['Time'][0][8:14]) # Init time
    forCompareData = extractData.tail()
    # print(extractData['Time'].str[5:7]) // min
    # print(extractData['Time'].str[8:14]) // seconds
    extractData['Time'] = extractData['Time'].str[5:7].astype('float') * 60 +\
                          extractData['Time'].str[8:14].astype('float')

    x = extractData['Time']
    y = extractData['EEG_Fp2']
    plt.plot(x, y)


    leftCondition = extractData['Time'] < src + 1.5
    leftSide = extractData[leftCondition]
    plt.plot(x[leftCondition], y[leftCondition], color='red')
    left = leftSide['EEG_Fp2'].mean()
    print(leftSide['EEG_Fp2'].mean())

    rightCondition = extractData['Time'].between(src + 1.5, src + 3)
    rightSide = extractData[rightCondition]
    plt.plot(x[rightCondition], y[rightCondition], color='blue')
    right = rightSide['EEG_Fp2'].mean()
    print(rightSide['EEG_Fp2'].mean())

    upCondition = extractData['Time'].between(src + 3, src + 4.5)
    upSide = extractData[upCondition]
    plt.plot(x[upCondition], y[upCondition], color='yellow')
    up = upSide['EEG_Fp2'].mean()
    print(upSide['EEG_Fp2'].mean())

    downCondition = extractData['Time'].between(src + 4.5, src + 6)
    downSide = extractData[downCondition]
    plt.plot(x[downCondition], y[downCondition], color='green')
    down = downSide['EEG_Fp2'].mean()
    print(downSide['EEG_Fp2'].mean())

    plt.show()

    if max([left, right, up, down]) == left:
        print("left")
    elif max([left, right, up, down]) == right:
        print("right")
    elif max([left, right, up, down]) == up:
        print("up")
    elif max([left, right, up, down]) == down:
        print("down")

'''

# biomarkers()
# ssvepProcess()
p300Processing()