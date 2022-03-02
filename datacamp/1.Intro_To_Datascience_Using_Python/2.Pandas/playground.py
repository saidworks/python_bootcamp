import pandas as pd 

#create df from list of lists 
datas = [['letter_index','letter','frequency'],[1,'A',7.38],[2,'B',1.09],[3,'C',2.46],[4,'D',4.10]]

df_letters = pd.DataFrame(datas)
print(df_letters)

#find some csv on internet or previous exercise for playground 
#create dataframe and perform basic logic on some columns 