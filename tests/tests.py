import random


def generateintlist():
    """
    Создание тестового списка из рандомных целых чисел
    :return: testlist
    """
    testlist = []
    for i in range(100):
        testlist.append(random.randint(-10000, 10000))
    return testlist


def generatefloatlist():
    testlist = []
    for i in range(100):
        testlist.append(random.randint(-10000, 10000)/11)
    return testlist
