with open('C:\AI\SSIS\AdmissionOutPutViewQueryData.csv', 'r') as fin:
    data = fin.read().splitlines(True)
with open('C:\AI\SSIS\AdmissionOutPutViewQueryData.csv', 'w') as fout:
    fout.writelines(data[1:])