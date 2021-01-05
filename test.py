print("test".find("t"))

if "Foo">"Ahmed":
    print("A")

for i in [0,2,3]:
    if i % 2 == 0 :
        print("even")
    elif i ==0:
        print("zero")
x= "Hello"
a=x[-1:]
print(a)

i=0
while i < 5:
    if i % 2 ==0:
        i += 2 
        continue
    i -= 1 
print(i)
x = 10
def change():
    global x
    print("x is " , x)
    x = 2
    print(x)

change()
print("it is ",x) 
print([1,2,3][-1])
print("\n")

x = ["a","b","c"]
y = ["d","e","f"]
z = []
i = 0
while i < 3 :
    z.append(x[i])
    z.append(y[i])
    i = i + 1

print(z)



