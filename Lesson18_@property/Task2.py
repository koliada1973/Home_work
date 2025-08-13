# Task 2:
# Реалізуйте 2 класи, перший з яких називається Boss, а другий - Worker.
# Працівник має властивість "бос", і його значенням має бути екземпляр Боса.
# Ви можете перепризначити це значення, але ви повинні перевірити, чи є нове значення босом.
# Кожен бос має список своїх робітників.
# Ви повинні реалізувати метод, який дозволяє додавати робітників до боса.
# Вам не дозволяється додавати екземпляри класу Boss до списку робітників безпосередньо через доступ до атрибута,
# використовуйте геттери та сеттери замість цього!

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    @property
    def workers_list(self):
        return self.workers

    @workers_list.setter
    def workers_list(self, worker):
        if worker.__class__ == Worker:
            self.workers.append(worker)

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    @property
    def boss(self):
        return self.big_boss

    @boss.setter
    def boss(self, boss: Boss):
        if boss.__class__ == Boss:
            self.big_boss = boss
            boss.workers_list = self

boss1 = Boss(102, "Тоні Старк", "Stark Industries")
boss2 = Boss(101, "Нік Ф'юрі", "агентство Щ.И.Т.")

worker1 = Worker(1, "Вірджинія Поттс", "Stark Industries", boss1)
worker2 = Worker(2, "Філліп Коулсон", "Stark Industries", boss1)
worker3 = Worker(3, "Брюс Беннер", "Avengers", boss2)
worker4 = Worker(4, "Тоні Старк", "Avengers", boss2)
worker5 = Worker(5, "Стівен Роджерс", "Avengers", boss2)
worker6 = Worker(6, "Клінт Бартон", "Avengers", boss2)
worker7 = Worker(7, "Наташа Романова", "Avengers", boss2)
worker8 = Worker(8, "Тор Одінсон", "Avengers", boss2)

print(f"{boss1.company}")
print(f"Boss: {boss1.name} (id:{boss1.id:03}  {boss1.company})")
for w in boss1.workers_list:
    print(f"{w.name} (id:{w.id:03}  {w.company})")

print()
print(f"Boss: {boss2.name} (id:{boss2.id:03}  {boss2.company})")
for w in worker7.big_boss.workers_list:
    print(f"{w.name} (id:{w.id:03}  {w.company})")