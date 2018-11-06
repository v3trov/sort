import random


def generateintlist():
    """
    Создание тестового списка из рандомных целых чисел

    :return: testlistint
    """
    testlistint = []
    for i in range(100):
        testlistint.append(random.randint(-10000, 10000))
    return testlistint


def generatefloatlist():
    """
    Создание тестового списка из рандомных чисел с точкой

    :return: testlistfloat
    """
    testlistfloat = []
    for i in range(100):
        testlistfloat.append(random.randint(-10000, 10000)/11)
    return testlistfloat
