import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import numpy as np
from scipy import stats
from statsmodels.graphics.mosaicplot import mosaic

train=pd.read_csv("Downloads/train.csv")
test=pd.read_csv("Downloads/test.csv")
combine=pd.concat([train.drop('Survived',1),test])
#print combine
# train.head(8)
# train.isnull().sum()
# test.info
surv=train[train['Survived']==1]
nosurv=train[train['Survived']==0]
surv_col="blue"
nosurv_col="red"
#print "Survived: %i (%.1f percent), Not Survived: %i (%.1f percent), Total: %i " %(len(surv), len(surv)/len(train)*100.0,
                #len(nosurv), len(nosurv)/len(train)*100.0, len(train))
warnings.filterwarnings(action="ignore")
plt.figure(figsize=[12,10])
plt.subplot(331)
sns.distplot(surv['Age'].dropna().values,bins=range(0,81,1),kde=False,color=surv_col)
sns.distplot(nosurv['Age'].dropna().values,bins=range(0,81,1),kde=False,color=nosurv_col,axlabel='Age')
plt.subplot(332)
sns.barplot('Sex', 'Survived', data=train)
plt.subplot(333)
sns.barplot('Pclass', 'Survived', data=train)
plt.subplot(334)
sns.barplot('Embarked', 'Survived', data=train)
plt.subplot(335)
sns.barplot('SibSp', 'Survived', data=train)
plt.subplot(336)
sns.barplot('Parch', 'Survived', data=train)
plt.subplot(337)
sns.distplot(np.log10(surv['Fare'].dropna().values+1), kde=False, color=surv_col)
sns.distplot(np.log10(nosurv['Fare'].dropna().values+1), kde=False, color=nosurv_col,axlabel='Fare')
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,wspace=0.35)
#plt.show()

#print("Median age survivors: %.1f, Median age non-survivers: %.1f" %(np.median(surv['Age'].dropna()), np.median(nosurv['Age'].dropna())))
tab=pd.crosstab(train['SibSp'],train['Survived'])
#print tab
stats.binom_test(x=5,n=5,p=0.62)
#print "We know %i of %i Cabin Numbers in the training data set and" %(len(train['Cabin'].dropna()),len(train))
#print "We know %i of %i Cabin Numbers in the testing data set and" %(len(test['Cabin'].dropna()),len(test))
train.loc[:,['Survived','Cabin']].dropna().head(8)
#print "There are %i unique tickets out of %i tickets" %(train['Ticket'].nunique(),train['Ticket'].count())
grouped=train.groupby('Ticket')
k=0
for name,group in grouped:
   if(len(grouped.get_group(name)))>1:
        #print group.loc[:,['Survived','Name','Fare']]
        k+=1
   if k>10:
      break


#############################################

#plt.figure(figsize=(14,12))
#foo=sns.heatmap(train.drop('PassengerId',axis=1).corr(),vmax=0.6,square=True,annot=True)
#plt.show()
cols=['Survived','Pclass','Age','SibSp','Parch','Fare']
#g=sns.pairplot(data=train.dropna(),vars=cols,size=1.5,hue="Survived",palette=[nosurv_col,surv_col])
#g.set(xticklabels=[])
#plt.show()

#plt.figure()
#sns.violinplot(x="Pclass",y="Age",hue='Survived',data=train,split=True)
#plt.hlines([0,10],xmin=-1,xmax=3,linestyle="dotted")
#plt.show()


plt.figure()
dummy = mosaic(train,["Survived","Sex","Pclass"])
#plt.show()

g=sns.factorplot(x="Pclass",y="Survived",hue="Sex",col="Embarked",data=train,aspect=0.9,size=3.5,ci=95.0)
plt.show()




