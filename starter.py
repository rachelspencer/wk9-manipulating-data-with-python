
first_name = "Rachel"
last_name = "Spencer"
print(first_name, last_name)

#age = 33
#age = 12
#age = "thirty-three"
#print(age)

#print(type(first_name))
#print(type(age))

#if age >= 18:
    #print('I am an adult')
    #print(first_name + last_name)

#elif age < 13:
    #print('I am an infant')

#else:
    #print('I am an alien')

favorite_numbers = [1,2,3,4,5," hello", True, 2.0]
#print(favorite_numbers)

for garbage in favorite_numbers:
    print(garbage)

#for stuff in range(5):
    #print(stuff)

def sum(num_1, num_2):
    return num_1 + num_2

result = sum(1,2)
#print(result)

open_file = open("FinalGrades.csv")
total_a = 0
total_b = 0
total_c = 0

#for line in open_file:
#    line = line.strip()
#   values = line.split(',')
#   print(values)
#    for value in values:
#        if value == "A":
#            total_a += 1
#       elif value == "B": 
#            total_b += 1
#        elif value == "C": 
#            total_c += 1

print("A's:", total_a, "B's:",total_b, "C's:", total_c)
    
for line in open_file:
    line = line.strip()
    values = line.split(',')
    print(values[2: 5])

open_file.close()

prime_number = float(1)
print(prime_number)
