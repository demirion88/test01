#OH MY GOD


# print(pd.__version__)

# sr = pd.Series([17000,18000,1000,5000],index=["피자","치킨","콜라","맥주"])
# print(sr)
# print(sr.values)
# print(sr.index)

# data = [
#     ['1000','steve',90.72],
#     ['1001','james', 78.09],
#     ['1002', 'Doyeon', 98.43],
#     ['1003', 'Jane', 64.19],
#     ['1004', 'Pilwoong', 81.30],
#     ['1005', 'Tony', 99.14]
# ]




#df = pd.DataFrame(data,columns=['학번','이름','점수'])

# data = { '학번' : ['1000', '1001', '1002', '1003', '1004', '1005'],
# '이름' : [ 'Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],
#          '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]}
# df = pd.DataFrame(data)

import pandas as pd
import pandas_profiling

data=pd.read_csv(r'D:\ProgramData\Dataset\spam.csv',encoding='latin1')

pr=data.profile_report()
pr.to_file('./pr_report.html') # pr_report.html 파일로 저장