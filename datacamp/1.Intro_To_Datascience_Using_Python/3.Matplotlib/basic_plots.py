import matplotlib.pyplot as plt 

year = [1950,1970,1990,2010]
pop = [2.159,3.692,5.263,6.972]


plt.scatter(year,pop)
#plt.plot(year,pop)

# Put the x-axis on a logarithmic scale
plt.xscale('log')
plt.show()