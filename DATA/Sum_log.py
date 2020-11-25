#파일 합치기(추려낸 파일 합치는 코드) 

import pandas as pd
import os.path

str_list = ['08', '09', '10', '11', '12', '13', '14', '15', '16', '17']
DIR = '/home/tfir/KJS/testLog/'

for s in str_list:
    log_dir = DIR + 'log_201005' + s + '/'
    output_file = log_dir + 'log_201005' + s + '.csv'

    for i in range(1, 10):
        chk = log_dir + 'tmp' + str(i) + '.csv'
        if i == 1:
            df1 = pd.read_csv(chk, low_memory=False)
            df1.fillna(0)
        else:
            if os.path.isfile(chk):
                df2 = pd.read_csv(chk, low_memory=False)
                df2.fillna(0)
                df1 = pd.concat([df1, df2], axis=0, ignore_index=True)
    df1.to_csv(output_file, index=False)    
    print("complete")
