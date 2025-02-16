def sum_positive(numbers):
    total = 0
    for num in numbers:
        if num < 0:
            raise ValueError("Negative numbers are not allowed")
        total += num
    return total

try:
    numbers = [1, 2, 3, 4, 5]  
    result = sum_positive(numbers)
    print(f"Sum of positive numbers {numbers}: {result}")  

    numbers = [10, 20, 30]
    result = sum_positive(numbers)
    print(f"Sum of positive numbers {numbers}: {result}")  

    numbers = [0, 1, 2]
    result = sum_positive(numbers)
    print(f"Sum of positive numbers {numbers}: {result}") 

   
    numbers = [1, -2, 3, 4]
    result = sum_positive(numbers) 
    print(f"Sum of positive numbers {numbers}: {result}")

except ValueError as e:
    print(f"Error: {e}")


