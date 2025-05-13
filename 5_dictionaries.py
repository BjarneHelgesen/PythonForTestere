age = {} # empty dictionary
age = {"Bjarne": 56, "Harald": 56} # intializding data  
age["Anton"] = 35 # adding new data
#print(age["Student x"]) # exception error
print (age["Bjarne"]) # 56

for name in age:
    print(name, "is", age[name], "year")


#### Opgave 1 ####
# Lag et program som tar navn og alder inn og, lagrer det i en dictionary.
# Legg sammen alderen til alle i dictionaryen og skriv ut summen.

sum = 0
for name in age:
    sum += age[name]
print("Sum of all ages is", sum)