fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input()
if fruit in fruits: 
    print("that fruit already exist in the list")
else: 
    fruits.append(fruit)
    print(fruits)