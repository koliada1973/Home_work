# Task 2:
# Реалізуйте 2 класи, перший з яких називається Boss, а другий - Worker.
# Працівник має властивість "бос", і його значенням має бути екземпляр Боса.
# Ви можете перепризначити це значення, але ви повинні перевірити, чи є нове значення босом.
# Кожен бос має список своїх робітників.
# Ви повинні реалізувати метод, який дозволяє додавати робітників до боса.
# Вам не дозволяється додавати екземпляри класу Boss до списку робітників безпосередньо через доступ до атрибуту,
# використовуйте геттери та сеттери замість цього!

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers_list = []

    @property
    def workers(self):
        return self.workers_list

    @workers.setter
    def workers(self, worker):
        if worker.__class__ == Worker:
            self.workers_list.append(worker)

    @workers.deleter
    def worker(self, worker):
        self.workers_list.remove(self, worker)

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
            boss.worker = self

boss1 = Boss(102, "Тоні Старк", "Stark Industries")
boss2 = Boss(101, "Нік Ф'юрі", "агентство Щ.И.Т.")

worker1 = Worker(1008, "Вірджинія Поттс", "Stark Industries", boss1)
worker2 = Worker(1009, "Філліп Коулсон", "Stark Industries", boss1)
worker3 = Worker(1001, "Брюс Беннер", "Месники", boss2)
worker4 = Worker(1002, "Тоні Старк", "Месники", boss2)
worker5 = Worker(1003, "Стівен Роджерс", "Месники", boss2)
worker6 = Worker(1004, "Клінт Бартон", "Месники", boss2)
worker7 = Worker(1005, "Наташа Романова", "Месники", boss2)
worker8 = Worker(1006, "Тор Одінсон", "Месники", boss2)

print(f"Boss: {boss1.name} (id:{boss1.id} Company: {boss1.company})")
for w in boss1.workers:
    print(f"{w.name} (id:{w.id}  {w.company})")

print()
print(f"Boss: {worker8.big_boss.name} (id:{worker8.big_boss.id} Company: {worker7.big_boss.company})")
for w in worker7.big_boss.workers:
    print(f"{w.name} (id:{w.id}  {w.company})")