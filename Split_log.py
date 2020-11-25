# 크기가 너무 큰 로그파일을 천만줄씩 잘라서 저장

DIR = '/home/tfir/dataset/'
fname = 'log_20100517' 

with open(DIR + fname + '.csv', 'r') as f:
    csvfile = f.readlines()
linesPerFile = 10000000
filename = 1

for i in range(0, len(csvfile), linesPerFile):
    with open(fname + '/' + fname + '_' + str(filename) + '.csv', 'w+') as f:
        if filename > 1:
            f.write(csvfile[0])
        f.writelines(csvfile[i:i+linesPerFile])
    filename += 1
