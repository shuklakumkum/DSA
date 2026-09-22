#1 write a function to print "Hello,World!".

def hello_world():
    print("Hello, World!")

hello_world()

# 2. Write a function that takes a name and prints a greeting.

def greet(name):
    print("Hello", name)

greet("Kumkum")

# 3. Write a function to add two numbers.

def add(a,b):
    return a+b
print(add(10,20))

# 4. Write a function to find the square of a number.

def square(n):
    return n * n

print(square(5))

# 5. Write a function to check whether a number is even or odd.

def even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

even_odd(7)

# 6. Write a function to find the maximum of two numbers.

def maximum(a, b):
    if a > b:
        return a
    else:
        return b

print(maximum(10, 25))

# 7. Write a function to convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(c):
    f = (c * 9 / 5) + 32
    return f

print(celsius_to_fahrenheit(30))



# 8. Write a function to calculate the area of a circle.

def circle_area(r):
    area = 3.14 * r * r
    return area

print(circle_area(5))


# 9. Write a function to calculate the factorial of a number.

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

print(factorial(5))


# 10. Write a function to check whether a number is positive, negative, or zero.

def check_number(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")

check_number(-10)


# 11. Write a function to find the maximum of three numbers.

def maximum_three(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

print(maximum_three(10, 25, 15))


# 12. Write a function to count vowels in a string.

def count_vowels(text):
    count = 0

    for ch in text:
        if ch.lower() in "aeiou":
            count = count + 1

    return count

print(count_vowels("Hello World"))


# 13. Write a function to reverse a string.

def reverse_string(text):
    return text[::-1]

print(reverse_string("Python"))


# 14. Write a function to check whether a string is a palindrome.

def palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

print(palindrome("madam"))


# 15. Write a function to find the sum of all elements in a list.

def list_sum(numbers):
    total = 0

    for n in numbers:
        total = total + n

    return total

numbers = [10, 20, 30, 40]
print(list_sum(numbers))


# 16. Write a function to find the largest element in a list.

def largest(numbers):
    big = numbers[0]

    for n in numbers:
        if n > big:
            big = n

    return big

numbers = [10, 50, 20, 40, 30]
print(largest(numbers))


# 17. Write a function to remove duplicate elements from in a list.

def remove_duplicates(input_list):
        return list(set(input_list))

numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1]
print(remove_duplicates(numbers))




# 18. Write a function to count how many times an element appears in a list.

def count_element(numbers, element):
    count = 0

    for n in numbers:
        if n == element:
            count = count + 1

    return count

numbers = [10, 20, 10, 30, 10, 40]
print(count_element(numbers, 10))


# 19. Write a function to check whether a number is prime.

def prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print(prime(17))


#20.  write a function to Return all prime numbers between two numbers

def primes_between(start, end):
    primes = []

    for num in range(start, end + 1):
        if num < 2:
            continue

        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes


print(primes_between(10, 30))



#21. write a function to Calculate Fibonacci numbers

def fibonacci(n):
    series = []
    a, b = 0, 1

    for i in range(n):
        series.append(a)
        a, b = b, a + b

    return series


print(fibonacci(10))

#22. Find the second largest number in a list

def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)

    return unique_numbers[1]


numbers = [10, 20, 5, 30, 25, 30]
print(second_largest(numbers))

#23. Sort a list without using sort()

def sort_list(numbers):
    result = numbers.copy()

    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]

    return result


numbers = [5, 2, 8, 1, 3]
print(sort_list(numbers))

#24. Merge two lists and remove duplicates

def merge_remove_duplicates(list1, list2):
    result = []

    for item in list1 + list2:
        if item not in result:
            result.append(item)

    return result


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print(merge_remove_duplicates(list1, list2))
