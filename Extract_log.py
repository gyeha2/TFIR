# 잘려있는 로그파일에서 특정 계정의 로그만 추출
# 특정 계정은 레이블이나 테스트 계정의 리스트 파일을 이용

import os.path
import pandas as pd

f = open('/home/tfir/KJS/labeledList.txt', 'r')
lst = f.readlines()
botList = [line.rstrip() for line in lst]
botList = [int (i) for i in botList]

str_list = ['08' ,'09' ,'10' ,'11' ,'12' ,'13' ,'14' ,'15' ,'16' ,'17']
DIR = '/home/tfir/KJS/splited/'
logDir = '/home/tfir/KJS/labelLog/'

for s in str_list:
    fname = 'log_201005' + s
    for i in range(1,9):
        chk = DIR + fname + '/' + fname + '_' + str(i) + '.csv'
        if os.path.isfile(chk):
            log = pd.read_csv(chk, low_memory=False)
            bot = log["actor_account"].isin(botList)
            bots = log[bot].reset_index(drop=True)
            bots.to_csv(logDir + fname + '/tmp{}.csv'.format(i), index=False)
    print("testLog ext complete")
