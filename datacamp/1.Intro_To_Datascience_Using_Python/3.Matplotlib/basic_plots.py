import matplotlib.pyplot as plt 
import pandas as pd
year = [1950,1970,1990,2010]
pop = [2.159,3.692,5.263,6.972]


plt.scatter(year,pop)
#plt.plot(year,pop)

# Put the x-axis on a logarithmic scale
plt.xscale('log')
plt.show()


#create df from list of lists 
datas = [['letter_index','letter','frequency'],[1,'A',7.38],[2,'B',1.09],[3,'C',2.46],[4,'D',4.10]]

df_letters = pd.DataFrame(datas)

letters = [i[1] for i in datas if len(i[1])<2 ]
frequencies = [i[2] for i in datas if  i[2] != 'frequency']
plt.barh(letters,frequencies)
plt.show()
