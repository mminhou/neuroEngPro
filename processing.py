import pandas as pd
from matplotlib import pyplot as plt

def biomarkers():
    '''
        Biomarkers processing
    '''
    BIOMARKERS_FILENAME = "factory/data/Biomarkers.txt"
    # read csv file
    bioData = pd.read_csv(BIOMARKERS_FILENAME, sep="\t", encoding='cp949')
    # extract Fp2_Beta
    fp2BetaData = bioData['Fp2_Beta(%)']
    print(fp2BetaData.mean())       # Average of Fp2 Beta Data
    # return True False
    condition = fp2BetaData > 1.0
    # condition fp2 Beta Data
    conditionfp2BetaData = fp2BetaData[condition]
    print(conditionfp2BetaData.mean())      # Average of Condition Fp2 Beta Data

def ssvepProcess():
    '''
        Ssvep processing
    '''
    # FP2_FILENAME = filename
    FP2_FILENAME = "factory/data/Fp2_FFT.txt"
    # read csv file
    fp2Data = pd.read_csv(FP2_FILENAME, sep="\t", encoding='cp949')
    # extract 6.6, 6.8, 7.0, 7.2, 7.4Hz data
    upData = fp2Data[['6.60Hz', '6.80Hz', '7.00Hz', '7.20Hz', '7.40Hz']]    # up
    print(upData.mean().mean())
    downData = fp2Data[['8.60Hz', '8.80Hz', '9.00Hz', '9.20Hz', '9.40Hz']]  # down
    print(downData.mean().mean())
    leftData = fp2Data[['10.60Hz', '10.80Hz', '11.00Hz', '11.20Hz', '11.40Hz']] # left
    print(leftData.mean().mean())
    rightData = fp2Data[['12.60Hz', '12.80Hz', '13.00Hz', '13.20Hz', '13.40Hz']] # right
    print(rightData.mean().mean())
    # real time process
    # while(1):
    #     data = pd.read_csv(FP2_FILENAME, sep="\t", encoding='cp949')
    #     extractData = data.loc[:, ['7.00Hz', '9.00Hz', '11.00Hz', '13.00Hz']]
    #     if extractData.tail() == dataSample:
    #         break
    #
    #     dataSample = extractData.tail()
    #     time.sleep(3)
    #     print(dataSample)

def p300Processing2(filePath):
    ''' Main p300 processing '''
    RAWDATA_FILENAME = filePath
    # RAWDATA_FILENAME = 'factory/data/Rawdata.txt' # testing data Path

    ''' Extract 'Time', 'EEG_Fp2' after read Rawdata.txt '''
    rawData = pd.read_csv(RAWDATA_FILENAME, sep="\t", encoding='cp949')
    extractData = rawData.loc[:, ['Time', 'EEG_Fp2']]

    ''' 
        Time의 성분중 min과 sec을 뽑아내서 min*60 + sec을 새로운 time으로 설정 
        [-10:-8] = minute
        [-7:] = sec
    '''
    extractData['Time'] = extractData['Time'].str[-10:-8].astype('float') * 60 + extractData['Time'].str[-7:].astype('float')
    ''' 기준점이 되는 last data -> Rawdata에서 마지막 줄 데이터 '''
    last = float(extractData['Time'].iloc[-1])
    ''' last의 시간으로부터 6초전의 data 추출 '''
    dataCondition = extractData['Time'].astype('float') > last - 6
    extractData = extractData[dataCondition]

    ''' 1.5초 전의 데이터 -> down '''
    downCondition = extractData['Time'] < last - 1.5
    downSide = extractData[downCondition]
    down = downSide['EEG_Fp2'].mean()
    print(downSide['EEG_Fp2'].mean())
    ''' 3 ~ 1.5초 전의 데이터 -> up '''
    upCondition = extractData['Time'].between(last - 3, last - 1.5)
    upSide = extractData[upCondition]
    up = upSide['EEG_Fp2'].mean()
    print(upSide['EEG_Fp2'].mean())
    ''' 4.5 ~ 3초 전의 데이터 -> right '''
    rightCondition = extractData['Time'].between(last - 4.5, last - 3)
    rightSide = extractData[rightCondition]
    right = rightSide['EEG_Fp2'].mean()
    print(rightSide['EEG_Fp2'].mean())
    ''' 6 ~ 4.5초 전의 데이터 -> left '''
    leftCondition = extractData['Time'].between(last - 6, last - 4.5)
    leftSide = extractData[leftCondition]
    left = leftSide['EEG_Fp2'].mean()
    print(leftSide['EEG_Fp2'].mean())

    ''' 비교결과 max에 해당하는 동작을 return '''
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

def fp2GraphImage(filePath, srcTime):
    # BIOMARKERS_FILENAME = 'factory/data/Biomarkers.txt'   # tesing data Path
    BIOMARKERS_FILENAME = filePath

    ''' read Biomarkers.txt '''
    bioData = pd.read_csv(BIOMARKERS_FILENAME, sep="\t", encoding='cp949')
    ''' graph x position naming 
        [21:23] = month
        [24:26] = day
        [30] = min
        [32:34] = sec
    '''
    exeTime = BIOMARKERS_FILENAME[21:23] + '/' + BIOMARKERS_FILENAME[24:26] + ' ' + BIOMARKERS_FILENAME[30] + ':' + BIOMARKERS_FILENAME[32:34]

    ''' extract Fp1_Beta, Fp2_Beta '''
    extractFp1Beta = bioData['Fp1_Beta(%)']
    extractFp2Beta = bioData['Fp2_Beta(%)']

    ''' extract Fp1Beta > 15%, Fp2Beta > 15% '''
    conditionFp1 = extractFp1Beta > 15
    conditionFp2 = extractFp2Beta > 15

    ''' each dataframe mean '''
    avgTotalFp1 = extractFp1Beta.mean()
    avgTotalFp2 = extractFp2Beta.mean()
    avgConditionFp1 = extractFp1Beta[conditionFp1].mean()
    avgConditionFp2 = extractFp2Beta[conditionFp2].mean()

    ''' average Fp data & more than 15% data '''
    avgTotal = (avgTotalFp1 + avgTotalFp2) / 2
    avgCondition = (avgConditionFp1 + avgConditionFp2) / 2
    print(avgTotal, avgCondition)

    ''' 누적데이터 read '''
    resultData = pd.read_csv('factory/data/result.txt', sep='\t')
    ''' 누적데이터에 계산값 append '''
    resultData = resultData.append({'Time': exeTime, 'Total': avgTotal, 'Concentration': avgCondition}, ignore_index=True)
    ''' 누적데이터 다시 읽어서 마지막 5개의 데이터 extract '''
    resultData.to_csv('factory/data/result.txt', sep='\t', index=False)
    tailResult = resultData.tail()

    ''' create x range '''
    def create_x(t, w, n, d):
        return [t * x + w * n for x in range(d)]

    ''' data num condition '''
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

    ''' total, concentration x axis '''
    X_TOTAL = create_x(2, 0.8, 1, d)
    X_CONCEN = create_x(2, 0.8, 2, d)

    ''' draw total, concentration bar '''
    ax = plt.subplot()
    ax.bar(X_TOTAL, tailResult['Total'])
    ax.bar(X_CONCEN, tailResult['Concentration'])

    ''' wrtie bar name '''
    middle_x = [(a + b) / 2 for (a, b) in zip(X_TOTAL, X_CONCEN)]
    ax.set_xticks(middle_x)
    ax.set_xticklabels(tailResult['Time'])
    # save graph img
    plt.savefig('factory/image/result.png')

    # plt.show()
''' -> not used 
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

# testing
# fp2GraphImage()
# biomarkers()
# ssvepProcess()
# p300Processing()
# p300Processing2()