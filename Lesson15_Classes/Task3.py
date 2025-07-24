# Task 3:
# Створіть простий прототип телевізійного контролера на Python.
# Він буде використовувати наступні команди:
# - first_channel() - вмикає перший канал зі списку.
# - last_channel() - вмикає останній канал зі списку.
# - turn_channel(N) - вмикає канал N. Зверніть увагу, що номери каналів починаються з 1, а не з 0.
# - next_channel() - вмикає наступний канал. Якщо поточний канал є останнім, вмикає перший канал.
# - previous_channel() - вмикає попередній канал. Якщо поточний канал є першим, вмикає останній канал.
# - current_channel() - повертає назву поточного каналу.
# - exists(N/'name') - отримує 1 аргумент - число N або рядок 'name'
# і повертає "Yes", якщо канал N або 'name' існує у списку,
# або "No" - в іншому випадку.
#
# Канал за замовчуванням, який вмикається перед усіма командами, - №1.
# Ваше завдання - створити клас TVController та методи, описані вище.

class TVController:
    def __init__(self, channel_list):
        self.channel_list = channel_list
        self.current_index = 0
        self.previous_index = 0

    def first_channel(self):
        self.previous_index = self.current_index
        self.current_index = 0
        return self.channel_list[self.current_index]

    def last_channel(self):
        self.previous_index = self.current_index
        self.current_index = -1
        return self.channel_list[self.current_index]

    def turn_channel(self, channel):
        self.previous_index = self.current_index
        self.current_index = channel-1
        return self.channel_list[self.current_index]

    def next_channel(self):
        self.previous_index = self.current_index
        if self.current_index == len(self.channel_list):
            self.current_index = 0
        else:
            self.current_index += 1
        return self.channel_list[self.current_index]

    def previous_channel(self):
        self.current_index, self.previous_index = self.previous_index, self.current_index
        return self.channel_list[self.current_index]

    def current_channel(self):
        return self.channel_list[self.current_index]

    def exists(self, channel):
        result = False
        if isinstance(channel, (int, float)):
            result = channel <= len(self.channel_list)
        else:
            result = channel in self.channel_list
        return "Yes" if result else "No"


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

print(controller.first_channel() == "BBC")
print(controller.last_channel() == "TV1000")
print(controller.turn_channel(1) == "BBC")
print(controller.next_channel() == "Discovery")
print(controller.previous_channel() == "BBC")
print(controller.current_channel() == "BBC")
print(controller.exists(4) == "No")
print(controller.exists("BBC") == "Yes")
