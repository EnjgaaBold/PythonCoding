# Python code​​​​​​‌​‌‌‌‌‌​‌‌​‌​​‌‌​‌‌‌​‌​​​ below

def factorial(num):
    if type(num) != int or num < 0:
        return None
    else:
        if num == 0:
            return 1
        else:
            return num * factorial(num-1)
    