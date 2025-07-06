# Напишіть декоратор, який бере список стоп-слів і замінює їх на * всередині декорованої функції
from functools import wraps
from functools import reduce

def stop_words(words: list):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Отримуємо рядок як результат виконання переданої функціі:
            text = func(*args, **kwargs)
            # За допомогою reduce проходимо по списку стоп-слів та знайдені в рядку стоп-слова замінюємо на *
            result = reduce(lambda text, i: text.replace(i, "*"), words, text)
            return result
        return wrapper
    return my_decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name):
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

# Друк отриманого рядка (для наочності, це не потрібно за умовами задачі!!!)
print(create_slogan("Steve"))