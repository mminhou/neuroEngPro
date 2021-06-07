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
'''
def p300Processing(filePath):
    RAWDATA_FILENAME = filePath
    # RAWDATA_FILENAME = "factory/data/Rawdata.txt"
    forCompareData = pd.read_csv(RAWDATA_FILENAME, sep="\t", encoding='cp949').loc[:, ['Time', 'EEG_Fp2']].tail()
    time.sleep(10)
    while(1):
        time.sleep(10)
        #
        rawData = pd.read_csv(RAWDATA_FILENAME, sep="\t", encoding='cp949')
        extractData = rawData.loc[:, ['Time', 'EEG_Fp2']]
        # 종료를 위한 예외처리
        if extractData.tail().equals(forCompareData):
            print('True')
            break
        forCompareData = extractData.tail()
        #
        rawData = pd.read_csv(RAWDATA_FILENAME, sep="\t", encoding='cp949')
        extractData = rawData.loc[:, ['Time', 'EEG_Fp2']]
        extractData['Time'] = extractData['Time'].str[5:7].astype('float') * 60 + \
                              extractData['Time'].str[8:14].astype('float')
        last = float(extractData['Time'].iloc[-1])
        print(last)
        dataCondition = extractData['Time'].astype('float') > last - 10
        extractData = extractData[dataCondition]
        # 시간표현 분의 표현 issue -> 분 뽑아내서 * 60 한 후 초에 더해준다.
        # print(extractData['Time'].iloc[-1200][5:7])
        # src = float(1)
        # src = float(extractData['Time'].loc[-200][5:7]) * 60 + float(extractData['Time'].loc[-200][8:14])  # Init time
        # forCompareData = extractData.tail()
        # print(extractData['Time'].str[5:7]) // min
        # print(extractData['Time'].str[8:14]) // seconds
        x = extractData['Time']
        y = extractData['EEG_Fp2']
        plt.plot(x, y)

        leftCondition = extractData['Time'] < last - 2.5
        leftSide = extractData[leftCondition]
        #plt.plot(x[leftCondition], y[leftCondition], color='red')
        left = leftSide['EEG_Fp2'].mean()
        print(leftSide['EEG_Fp2'].mean())

        rightCondition = extractData['Time'].between(last - 5, last - 2.5)
        rightSide = extractData[rightCondition]
        #plt.plot(x[rightCondition], y[rightCondition], color='blue')
        right = rightSide['EEG_Fp2'].mean()
        print(rightSide['EEG_Fp2'].mean())

        upCondition = extractData['Time'].between(last - 7.5, last - 5)
        upSide = extractData[upCondition]
        #plt.plot(x[upCondition], y[upCondition], color='yellow')
        up = upSide['EEG_Fp2'].mean()
        print(upSide['EEG_Fp2'].mean())

        downCondition = extractData['Time'].between(last - 10, last - 7.5)
        downSide = extractData[downCondition]
        #plt.plot(x[downCondition], y[downCondition], color='green')
        down = downSide['EEG_Fp2'].mean()
        print(downSide['EEG_Fp2'].mean())

        #plt.show()
        if max([left, right, up, down]) == left:
            print("left")
        elif max([left, right, up, down]) == right:
            print("right")
        elif max([left, right, up, down]) == up:
            print("up")
        elif max([left, right, up, down]) == down:
            print("down")
    #
    rawData = pd.read_csv(RAWDATA_FILENAME, sep="\t", encoding='cp949')
    extractData = rawData.loc[-20:, ['Time', 'EEG_Fp2']]
    # extractData = rawData.tail().loc[:, ['Time', 'EEG_Fp2']]
    # 시ls간표현 분의 표현 issue -> 분 뽑아내서 * 60 한 후 초에 더해준다.
    src = float(extractData['Time'][0][5:7]) * 60 + float(extractData['Time'][0][8:14]) # Init time
    forCompareData = extractData.tail()
    # print(extractData['Time'].str[5:7]) // min
    # print(extractData['Time'].str[8:14]) // seconds
    extractData['Time'] = extractData['Time'].str[5:7].astype('float') * 60 +\
                          extractData['Time'].str[8:14].astype('float')
    print(extractData['Time'].iloc[-1])
    last = float(extractData['Time'].iloc[-1])
    sixsCondition = extractData['Time'].astype('float') > last - 6
    print(sixsCondition)
    print(extractData[sixsCondition])
    x = extractData['Time']
    y = extractData['EEG_Fp2']
    plt.plot(x, y)
    leftCondition = extractData['Time'] < src + 1.5
    leftSide = extractData[leftCondition]
    plt.plot(x[leftCondition], y[leftCondition], color='red')
    left = leftSide['EEG_Fp2'].mean()
    # print(leftSide['EEG_Fp2'].mean())
    rightCondition = extractData['Time'].between(src + 1.5, src + 3)
    rightSide = extractData[rightCondition]
    plt.plot(x[rightCondition], y[rightCondition], color='blue')
    right = rightSide['EEG_Fp2'].mean()
    # print(rightSide['EEG_Fp2'].mean())
    upCondition = extractData['Time'].between(src + 3, src + 4.5)
    upSide = extractData[upCondition]
    plt.plot(x[upCondition], y[upCondition], color='yellow')
    up = upSide['EEG_Fp2'].mean()
    # print(upSide['EEG_Fp2'].mean())
    downCondition = extractData['Time'].between(src + 4.5, src + 6)
    downSide = extractData[downCondition]
    plt.plot(x[downCondition], y[downCondition], color='green')
    down = downSide['EEG_Fp2'].mean()
    # print(downSide['EEG_Fp2'].mean())
    plt.show()
    if max([left, right, up, down]) == left:
        print("left")
    elif max([left, right, up, down]) == right:
        print("right")
    elif max([left, right, up, down]) == up:
        print("up")
    elif max([left, right, up, down]) == down:
        print("down")
    #
'''

def p300Processing2(filePath):
    RAWDATA_FILENAME = filePath
    forCompareData = pd.read_csv(RAWDATA_FILENAME, sep="\t", encoding='cp949').loc[:, ['Time', 'EEG_Fp2']].tail()
    # time.sleep(10)

    rawData = pd.read_csv(RAWDATA_FILENAME, sep="\t", encoding='cp949')
    extractData = rawData.loc[:, ['Time', 'EEG_Fp2']]
    extractData['Time'] = extractData['Time'].str[5:7].astype('float') * 60 + extractData['Time'].str[8:14].astype('float')
    last = float(extractData['Time'].iloc[-1])
    print(last)
    dataCondition = extractData['Time'].astype('float') > last - 6
    extractData = extractData[dataCondition]

    leftCondition = extractData['Time'] < last - 1.5
    leftSide = extractData[leftCondition]
    left = leftSide['EEG_Fp2'].mean()
    print(leftSide['EEG_Fp2'].mean())

    rightCondition = extractData['Time'].between(last - 3, last - 1.5)
    rightSide = extractData[rightCondition]
    right = rightSide['EEG_Fp2'].mean()
    print(rightSide['EEG_Fp2'].mean())

    upCondition = extractData['Time'].between(last - 4.5, last - 3)
    upSide = extractData[upCondition]
    up = upSide['EEG_Fp2'].mean()
    print(upSide['EEG_Fp2'].mean())

    downCondition = extractData['Time'].between(last - 6, last - 4.5)
    downSide = extractData[downCondition]
    down = downSide['EEG_Fp2'].mean()
    print(downSide['EEG_Fp2'].mean())

    if max([left, right, up, down]) == left:
        print("left")
        return 'left'
    elif max([left, right, up, down]) == right:
        print("right")
        return 'right'
    elif max([left, right, up, down]) == up:
        print("up")
        return 'up'
    elif max([left, right, up, down]) == down:
        print("down")
        return 'down'

def fp2GraphImage(filePath):
    # playTime이 필요한가? -> 이 함수를 불러오는시점에서 complete데이터가 들어오는건데?
    # BIOMARKERS_FILENAME = 'factory/data/Biomarkers.txt'
    BIOMARKERS_FILENAME = filePath

    bioData = pd.read_csv(BIOMARKERS_FILENAME, sep="\t", encoding='cp949')
    exeTime = bioData['Time'][0]

    extractFp1Beta = bioData['Fp1_Beta(%)']
    extractFp2Beta = bioData['Fp2_Beta(%)']
    conditionFp1 = extractFp1Beta > 15
    conditionFp2 = extractFp2Beta > 15

    avgTotalFp1 = extractFp1Beta.mean()
    avgTotalFp2 = extractFp2Beta.mean()
    avgConditionFp1 = extractFp1Beta[conditionFp1].mean()
    avgConditionFp2 = extractFp2Beta[conditionFp2].mean()

    avgTotal = (avgTotalFp1 + avgTotalFp2) / 2
    avgCondition = (avgConditionFp1 + avgConditionFp2) / 2
    print(avgTotal, avgCondition)

    # 누적데이터의 저장
    resultData = pd.read_csv('factory/data/result.txt', sep='\t')
    resultData = resultData.append({'Time': exeTime, 'Total': avgTotal, 'Concentration': avgCondition}, ignore_index=True)
    resultData.to_csv('factory/data/result.txt', sep='\t', index=False)
    tailResult = resultData.tail()
    print(tailResult)
    print(len(tailResult))

    def create_x(t, w, n, d):
        return [t * x + w * n for x in range(d)]

    if len(tailResult) == 1:
        d = 1
    elif len(tailResult) == 2:
        d = 2
    elif len(tailResult) == 3:
        d = 3
    elif len(tailResult) == 4:
        d = 4
    elif len(tailResult) >= 5:
        d = 5

    X_TOTAL = create_x(2, 0.8, 1, d)
    X_CONCEN = create_x(2, 0.8, 2, d)

    ax = plt.subplot()
    ax.bar(X_TOTAL, tailResult['Total'])
    ax.bar(X_CONCEN, tailResult['Concentration'])

    middle_x = [(a + b) / 2 for (a, b) in zip(X_TOTAL, X_CONCEN)]
    ax.set_xticks(middle_x)
    ax.set_xticklabels(tailResult['Time'])
    plt.savefig('factory/image/result.png')

    # plt.show()


# fp2GraphImage()
# biomarkers()
# ssvepProcess()
# p300Processing()