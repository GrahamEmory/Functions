# FUNCTIONS - instructions to do a certain actions  

# 2 things required for functions:
# 1) define them
# 2) call them to work


# 1) define function
def greeting():
  print("Hello")

# 2) call the function to work
greeting()

def goodbye(name):
  print("So long, " + name)

goodbye("King Bowser")


def add(num): 
  for i in range(5):
    sum = num + i
    print(sum)
    if sum < 5:
      print(str(sum) + " is less than 5")
    else:
      print(str(sum) + " is equal to or greater than 5")

add(3)

# Challenge:
# Create a function called sandwich
# that will print out "salami"

def sandwich(ingrediant):
  print("Yummy, a " + ingrediant + " sandwich.")
  
sandwich("salami")

def favorite(food):
  print("MMMMM, my most favorite " + food)

favorite("meaty delicacy.")


def sum(n1, n2):
  return n1 + n2
total = sum(2,5)
print(total)

def multiply(total):
  print(total * 2)
multiply(total)

def sum2(n1, n2):
  print(n1 + n2)
sum2(2,5)


def book(favfantbook):
  print("My favorite fantasy book is " + favfantbook)
book("Harry Potter.")


