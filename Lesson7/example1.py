Days = ['Mondey', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for i in range(len(Days)):
    Days[i] = ((i + 10), Days[i], len(Days[i]), len(Days[i]) % 2 == 0)
print(Days)