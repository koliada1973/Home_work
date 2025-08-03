# Task 1:
# Створіть метод класу з іменем `validate`,
# який слід викликати з методу `__init__`
# для перевірки параметра email, переданого в конструктор.
# Логіка методу `validate` може полягати у перевірці того,
# чи переданий параметр email є дійсним рядком електронної пошти.

class NewClass:
    def __init__(self, email):
        self.email = self.__class__.email(email)

    @classmethod
    def email(cls, email):
        allowed_special_simbols = '"(),:;<>@[\\]]'
        simbols_to_check = '_.-'
        if '@' not in email:
            raise ValueError('Недійсний email: відстутний обов\'язковий символ @')
        else:
            prefix, domain = email.split('@')
            # Перевірка формату префіксу email:
            # Перевірка, що крапка не є першим, останнім символом, а також що вона не з'являється послідовно
            if prefix[0] == '.' or prefix[-1] == '.' or '..' in prefix:
                raise ValueError('Недійсний email: недопустиме використання крапки!')
            for s in prefix:
                # Перевірка кожного символу, чи є він буквою, числом, або спеціальним символом
                if not(s.isalpha() or s.isdigit() or s in allowed_special_simbols or s in simbols_to_check):
                    raise ValueError('Недійсний email: використання недопустимих символів!')
                # Перевірка того, що символом підкреслення, крапкою, тире або дозволеним
                # спеціальним символом має слідувати одна або декілька букв чи цифр:
                if s in simbols_to_check:
                    index = prefix.find(s)
                    if index == -1 or (index + 1) == len(prefix):
                        raise ValueError('Недійсний email: за символом підкреслення, крапкою, тире або дозволеним спеціальним символом має слідувати одна або декілька букв чи цифр!')
                    else:
                        a = prefix[index+1]
                        if not(a in allowed_special_simbols or a.isalpha() or a.isdigit()):
                            raise ValueError('Недійсний email: використання недопустимих символів!')
        # Перевірка формату доменів електронної пошти:
        # Обрізаємо останню крапку (якщо вона є - її використання допустимо, але заважає відділити останню частину домену)
        domain = domain.rstrip('.')
        if '.' not in domain or '..' in domain:
            raise ValueError('Недійсний email: невірний формат домену!')
        else:
            # Знаходимо індекс останньої крапки в рядку домена:
            last_dot_index = domain.rfind('.')
            # Розділяємо домен на дві частини (частина до крапки та частина після крапки)
            domain_part1, domain_part2 = domain[:last_dot_index], domain[last_dot_index + 1:]
            # Перевірка першої частини домену (до крапки)
            for s in domain_part1:
                # Кожен символ перевіряємо чи є він літерой, цифрой, чи тире:
                if not(s.isalpha() or s.isdigit() or s in '-.'):
                    raise ValueError('Недійсний email: використання недопустимих символів!')
            # Перевірка останньої частини домену (після крапки)
            # - вона повинна складатися щонайменше з двох символів, наприклад: .com, .org, .cc
            if len(domain_part2) < 2:
                raise ValueError('Недійсний email: остання частина домену має складатися щонайменше з двох символів!')
        return email

class1 = NewClass("user1234567890_with_many_numbers@very.long.and.complicated.domain.name.with.multiple.subdomains.example.co.uk")
print(class1.email)

# Приклади помилкових email з неправильним префіксом:
# abc-@mail.com
# abc..def@mail.com
# .abc@mail.com
# abc#def@mail.com
# Приклади помилкових email з неправильним доменом:
# abc.def@mail
# abc.def@mail#archive.com
# abc.def@mail..com
# abc.def@mail.c
#
# Приклади правильного email:
# abc-d@mail.com
# dashes-and-dots@example.com.
# abc.def@mail.cc
# abc.def@mail-archive.com


