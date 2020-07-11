temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print ("Turn on the AC.")
else: 
    print ("Open the windows")

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print ("El Paso is in the list of counties.")

else:
    print ("El Paso is not in the list of counties")

x=0
while x <= 5:
    print (x)
    x= x + 1

count = 7
while count < 1:
    print ("Hello World")

for i in range(len(counties)):
    print(counties [i])
