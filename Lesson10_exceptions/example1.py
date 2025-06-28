# Task 1:
# Добийтесь отримання виключень типу TypeError, IndexError
try:
    '2' + 2
except TypeError:
    print('TypeError')

My_list = [1, 2, 3]
try:
    My_list[5]
except IndexError:
    print('IndexError')

# Task 2:
# Обробіть виключення ZeroDivisionError, видайте повідомлення про некоректну операцію.
try:
    2/0
except ZeroDivisionError:
    print('ZeroDivisionError')


# Task 3:
# Що буде, якщо в програмі (для задачі 2), в try виконати код '2' + 2
try:
    '2' + 2
except ZeroDivisionError:
    print('ZeroDivisionError')
except TypeError:
    print('TypeError')

# Task 4:
# Обробіть виключення типу ZeroDivisionError, TypeError, IndexError в одному блоці
try:
    '2' + 2
except (ZeroDivisionError, TypeError, IndexError):
    print('MultiError!!')


# Task 5:
# те саме, що в задачі 4, лише на кожен тип помилки – окремий except.
try:
    2/0
except ZeroDivisionError:
    print('ZeroDivisionError')
except TypeError:
    print('TypeError')
except IndexError:
    print('IndexError')

# Task 6:
# реалізуйте обробку для всіх класів виключень.
try:
    4/0
except:
    print('Error')

# Task 7:
# При якій умові виконається другий except ?
try:
    1 / 0
except ZeroDivisionError:
    print(1)
except ZeroDivisionError:
    print(2)

# Task 8:
# Реалізуйте логіку роботи з кількома except для різних класів помилок, та блоком else. Коли виконується else ?
# Якщо один except виконається, наступний перевіряється ?
try:
    2/0
except ZeroDivisionError:
    print('Ділення на 0')
except:
    print('Error')
else:
    print('Success')

# Task 9:
# В блоці try викиньте виключення  (raise) з головним класом Exception,
# передайте кілька параметрів.
# В except обробіть це виключення, виведіть параметри.
try:
    raise Exception('1', 'akgla')
except Exception as e:
    print(e)

# Task 10:
# Реалізуйте варіанти з finally:
# коли код працює нормально
# коли спрацьовує виключення і ви його ловите
# коли спрацьовує виключення і ви його пропускаєте
try:
    if 2 == 2:
        raise Exception('1')

except TypeError:
    print('TypeError')
    raise TypeError('Повторюю TypeErrror!!')
finally:
    print('Success')

