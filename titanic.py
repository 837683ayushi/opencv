import pandas as pd
train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")
combine=pd.concat([train.drop('Survived',1),test])
print combine
