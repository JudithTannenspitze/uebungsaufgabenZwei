name = input ("Wähle bitte eine Zahl zwischen 0 und 17: ")
hallo = int (name)
count_fizz =0 
count_buzz=0
count_fizzbuzz = 0
for i in range (1,hallo+1):
    if (i%5==0 and i%3==0):
        print("Fizzbuzz")
        count_fizzbuzz+=1
    elif (i%3==0):
        print("Fizz")
        count_fizz+=1
    elif (i%5==0):
        print("Buzz")
        count_buzz+=1
    else:
        print(i)
  
print("count_fizz: " + str(count_fizz))
print("count_buzz: " + str(count_buzz))
print("count_fizzbuzz: " + str(count_fizzbuzz))