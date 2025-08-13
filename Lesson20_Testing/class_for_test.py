class Mathematician:
    def square_nums(self, list1):
        """метод, що повертає елементи списку, зведені у квадрат"""
        return [i**2 for i in list1]

    def remove_positives(self, list1):
        """метод, що повертає лише ті елементи списку, що мають негативне значення"""
        return [i for i in list1 if i <= 0]

    def filter_leaps(self, list1):
        """метод, що повертає лише ті елементи списку, що відповідають високосним рокам"""
        return [i for i in list1 if i % 4 == 0 and not (i % 100 == 0 and i % 400 != 0)]