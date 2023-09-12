import numpy as np
import pandas as pd
import os
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pickle

print(os.getcwd())
path1=r'E:\ml-project\Swiggy Table 1.csv'
df1=pd.read_csv(path1)
path2=r'E:\ml-project\Table2_Raw_data.csv'
df2=pd.read_csv(path2)
df=pd.merge(df1,df2,how='inner',on='Restaurant_id')
df.drop_duplicates(inplace=True)
df['Review_count']=df['Review_count'].fillna(0)
df=df[df['Review_count']!=0]
avg_df=pd.DataFrame(df.groupby(['Cousines','location']).agg({'Price':'mean'})).reset_index()
location_list=list(avg_df['location'].unique())
loc_list=sorted(location_list)
cusine_list=list(avg_df['Cousines'].unique())
cus_list=sorted(cusine_list)
#print(loc_list[1])
#print(cus_list[1])
loc_dit={}
for i in range(len(loc_list)):
    loc_dit[loc_list[i]]=i
cus_dit={}
for i in range(len(cus_list)):
    cus_dit[cus_list[i]]=i
#print(cus_dit['American, Continental, Steakhouse'])
avg_df['location']=avg_df['location'].apply(lambda x:loc_dit[x])
avg_df['Cousines']=avg_df['Cousines'].apply(lambda x:cus_dit[x])
x=avg_df.drop(['Price'],axis=1)
y=avg_df['Price']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=42)
sc=StandardScaler()
x_sc=sc.fit_transform(x_train)
x_test_sc=sc.transform(x_test)
new_df=avg_df.copy()
# for i in new_df:
#     if i !='Price':
#         q1=new_df[i].quantile(0.25)
#         q3=new_df[i].quantile(0.75)
#         IQR=q3-q1
#         ll=q1-(IQR*1.5)
#         ul=q3+(IQR*1.5)
#         new_df=new_df[(new_df[i]>=ll) & (new_df[i]<=ul)]
# print(avg_df.shape)
# print(new_df.shape)
# lr=LinearRegression()
# lr.fit(x_sc,y_train)
# print(metrics.r2_score(y_test,lr.predict(x_test_sc)))
#The r2 score is low moving into ensemble techniques
model=GradientBoostingRegressor(random_state=42)
model.fit(x_sc,y_train)
y_predict=model.predict(x_test_sc)
print(metrics.r2_score(y_test,y_predict))
print(metrics.r2_score(y_test,y_predict))
pickle.dump(model,open('price_model.pkl','wb'))