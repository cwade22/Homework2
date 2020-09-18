#1)	Write code that compute the squares and cubes for numbers from 0 to 5.
# each cell occupies 20 spaces and right-aligned


print(f"{'Number':>20}{'Square':>20}{'cube':>20}")
for num in range (0,6):
    print(repr(num).rjust(20), repr(num*num).rjust(20), end= ' ')
    print(repr(num*num*num).rjust(20))

#2)	The formula to covert a Celsius temperature to a Fahrenheit temperature is 
# F = 9 / 5 * C  + 32
# Write code that use this formula to calculate and print the Fahrenheit temperature for Celsius value of -40, 0, 40 and 100.
 
#ct- Celsius Temp
#ft - Farhenheit Temp
ct1 = -40
ct2 = 0
ct3 = 40
ct4 = 100 

ft1 = int(((9/5)*ct1)+32)
ft2 = int((9/5*ct2)+32)
ft3 = int((9/5*ct3)+32)
ft4 = int((9/5*ct4)+32)

print (ct1, " degrees Celsius is equal to ", ft1, " degrees Farhenheit.")
print (ct2, " degrees Celsius is equal to ", ft2, " degrees Farhenheit.")
print (ct3, " degrees Celsius is equal to ", ft3, " degrees Farhenheit.")
print (ct4, " degrees Celsius is equal to ", ft4, " degrees Farhenheit.")


#3)	Write code that input three integers from the user. Then print the sum and average of the numbers.
x,y,z =[int(x) for x in input("please type three integers seperated by a comma").split(',')]


#sum
sum = x+y+z
print(f'The sum is {sum: ,d}')
#avg
average=sum/3
print(f'The average is {average: ,.2f}')


