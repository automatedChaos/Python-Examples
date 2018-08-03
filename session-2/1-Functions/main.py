#1. simple function with 4 statements in the code block
def sayHello():
  print("Hello")
  print("world")
  print("Hello")
  print("Hello")

#call the function above twice
sayHello()  # calls all four lines of code with one line
sayHello()

#2. function with parameters
def sayHelloTo(name):
    print("Hello " + name)
    print("how are you" + name + "?")

sayHelloTo("Alcwyn")

#3. function with multiple parameters
#Use the function in multiple ways
def add(num1, num2):
    sum = num1 + num2
    return sum

print(add(12,12))

sum1 = add(43,12)
sum2 = add(123,143)

print(add(sum1, sum2))

#4. calculate mean
def mean(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum/len(nums)

scores = [12, 3, 213, 2, 21]

print(mean(scores))
