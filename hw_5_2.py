import re
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
def generator_numbers(text):
    pattern = r'\d+\.\d+'
    numbers_in_text = re.findall(pattern, text)
    print (numbers_in_text)
    for item in numbers_in_text:
         numbers_float = float(item)
         
         yield (numbers_float)
print (generator_numbers(text))       
def sum_profit (text, func):
     func = sum(generator_numbers(text))
     return func
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")