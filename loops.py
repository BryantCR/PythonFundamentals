#           initial index,  the limit,  increment
for num in range(0, 10, 1):
    print( num )

# for ( let i = 0; i < 10; i ++){
#     console.log( i )
# }

nums = [10, 20, 30, 40, 50]

for i in range(0, len(nums)):
    print( i, nums[i] )

for i in range( len(nums) - 1, -1, -1):
    print( i, nums[i] )

sentence = "Hello there how are you?"

for letter in sentence:
    print( letter )

car = ("Toyota", 2018, "Corolla")

for i in range( 0, len( car ), 1):
    print( i, car[i] )

student = {
    'firstName' : 'Julie',
    'lastName' : 'Miller',
    'age' : 25
}

for key in student:
    print( key, student[key] )


for num in range(0, 11, 1):
    print( num )

limit = 0

while limit <= 10:
    print( limit )
    limit = limit + 1

print( "The loop just finished" )
#import random

#print('Welcome to Python!')

#print('This is a loop printing 5 times')
#for x in range(1, 6):
#    print(f'x is: {x}')

#weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
#day = random.choice(weekdays)

#print(f'Today is: {day}')

#if day == 'Monday':
#    print('It will be a long week!')
#elif(day == 'Friday'):
#    print('Woohoo, time for the weekend!')
#else:
#    print('Not quite there yet.')