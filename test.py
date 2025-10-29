from main import caching_fibonacci, generator_numbers, sum_profit

print("=== Testing caching_fibonacci ===")
fibonacci = caching_fibonacci()

print("fibonacci(10):", fibonacci(10))
print("fibonacci(15):", fibonacci(15))

print("=== Testing sum_profit ===")

text = "The resulting profit was: from the southern possessions $ 1000, and from the northern colonies $ 5000. Total $ 6000"
total_income = sum_profit(text, generator_numbers)
print("Expected: 12000, Actual:", total_income)

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print("Expected: 1351.46, Actual:", total_income)

print("=== Testing log_analysis ===")
path = "log.txt"
analysis = log_analysis(path)
print("Expected: {'INFO': 4, 'DEBUG': 3, 'ERROR': 2, 'WARNING': 1}, Actual:", analysis)
