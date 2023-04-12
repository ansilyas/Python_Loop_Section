#%%
# start,End,step;
for number in range(1,500):   
    print(number)
# %%
for number in range(1,10,2):
    print(number)
# %%
vowels=0
consonants=0
for letter in "feedback":
    if letter.lower() in "aeiou":
        vowels=vowels+1
    elif letter=="":
        pass
    else:
        consonants=consonants+1
        print("There are {} vowels".format(vowels))
        print("There are {} consonants".format(consonants))
# %%
strudent={
    "male":["Ans","ali","Ahmed",'Tom',"BoB","Bunny"],
    "female":["pinky","Emily","Kiran","Aman"]
}
for key in strudent.keys():
    for name in strudent[key]:
        if "a" in name:
            print(name)
# %%
answer =input("please say hi");
while answer !="hi":
    answer=input("please say hi");
print("game over")
# %%

# Loop for :
answer=input("please say hi");
for x in answer:
    print(x)

# %%
answer=[23.45,32,45,6,]
for a in answer:
    print(a)
# %%
