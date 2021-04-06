# -*- coding: utf-8 -*-
"""
Created on Mon May  4 18:44:21 2020

@author: Said ZITOUNI
"""

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])





largest = None
smallest = None

while True:
        num = input("Enter a number: ")
        if num == "done" :
            break
        try:
            num=float(num)
        except: 
            num=-1

        numbers=[]
        numbers.append(num)
        for num in numbers:
            if largest is None or num>largest:
                largest=num
            elif smallest is None or num<smallest:
                smallest=num
            num=-1
        

print("Maximum is", largest)
print("Minimum is", smallest)





















from math import *
import datetime
#sort numbers in a list 
# lis=[12,25,25,26,5,25,25]
# copy=lis[:]
# for i in range(len(copy)):
#     for j in range(len(copy)-i-1):
#         if copy[j]>copy[j+1]:
#             copy[j+1],copy[j]=copy[j],copy[j+1]
# print(copy)            
# dic={key:value for key,value in zip(lis,copy)}

# class Bus:
#    pass
# my_dic= {key:value for key,value in zip(range(12),range(12))}

#Class objects learning concepts by doing
class Patient(object):
    '''Attributes 
    --------------------
    name : Patient name
    age: Patient age
    conditions : existing medical conditions
    '''
    status="patient"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.conditions=[]
    def get_details(self):
        self.conditions=" ".join(self.conditions)
        print(f'Patient record {self.name},{self.age} years. ' f'\t\tCurrent information {self.conditions}') 
    
    def add_info(self,information):
        self.conditions.append(information)
ahmed=Patient("Ahmed Zaalaka",58)
tariq=Patient("Tariq Kharbouch",45)
ahmed.add_info("Cancer treatment normal procedure")
ahmed.get_details()
class Infant(Patient):
    ''' Patient under 2 years'''
    def __init__(self,name,age):
        self.vaccinations=[]
        super().__init__(name,age)
    def add_vac(self,vaccine):
        self.vaccinations.append(vaccine)
    def get_details(self):
        self.conditions=" ".join(self.conditions)
        self.vaccinations=" ".join(self.vaccinations)
        print(f'Patient record {self.name},{self.age} years. '
              f'\nPatient has had {self.vaccinations}'
              f'\nCurrent information {self.conditions}'
              f'\n{self.name} is an infant has he had all his checks?')
archie = Infant("Archie Fittleworth",0)
archie.add_vac("MMR")        
archie.get_details()
def cal(x):
    try:
        return 2*x-1
    except SyntaxError:
        print("Fuck!")
print(cal(5))
def my_func(n1, n2): 
    return n1 + n2 
my_func(1, 2)
datetime(1970, 1, 1).strftime('%Y-%d-%B')