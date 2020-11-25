# 레이블된 계정을 리스트로 만들어 저장

import pandas as pd

def write_list(lst, fname, sep):
    file = open(fname, 'w')
    vstr = ''

    for a in lst:
        vstr = vstr + str(a) + sep
    vstr = vstr.rstrip(sep)

    file.writelines(vstr)

    file.close()
    print('File Saved')

labeled = '~/dataset/labeled_account.csv'
df = pd.read_csv(labeled, low_memory=False)

dfs = df["account"]
dfList = dfs.values.tolist()

write_list(dfList, '/home/tfir/KJS/labeledList.txt', sep='\n')
