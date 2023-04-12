#%%
#while Loop syntax:
#while Condition:
#code.....
#while True:
 #   print("hello")


# %%
Number=1
while Number<=10:
    print(Number)
    Number=Number + 1
#%%
Number=1
while Number <=100:
    if Number %2 == 0:
        print(Number)
    Number=Number +1

# %%
number=1
while number <=100:
    if number%2!=0:
        print(number)
    number=number+1
# %%
L=[]
while len(L)<3:
    new_name=input("please add a name:").strip()
    L.append(new_name)
    print("sorry list is full")
    print(L)

# %%
