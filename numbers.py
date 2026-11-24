# Assignment: 3 functions - Sum, Mean, Median and Mode
def get_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

def get_mean(numbers):
    total = get_sum(numbers)
    average = total / len(numbers)
    return average

def get_median_and_mode(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2

    mode = max(set(numbers), key=numbers.count)
    return median, mode

numbers = [10, 20, 20, 30, 40]

print("sum:", get_sum(numbers))
print("mean:", get_mean(numbers))
print("median and mode:", get_median_and_mode(numbers))