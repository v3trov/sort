#!/usr/bin/env


def bubleSort(unsortedlist):
    """
    Сортировка списка "пузырьком"
    :param unsortedlist:
    :return: sortedlist
    """

    if type(unsortedlist) is not list:
        raise TypeError("Нужен список")

    if unsortedlist is None:
        raise ValueError("Список = None")

    if len(unsortedlist) <= 0:
        raise ValueError("Количество элементов должны быть > 0")

    for passnum in range(len(unsortedlist)-1, 0, -1):
        for i in range(passnum):
            if unsortedlist[i] > unsortedlist[i+1]:
                unsortedlist[i], unsortedlist[i+1] = unsortedlist[i+1], unsortedlist[i]
    sortedlist = unsortedlist
    return sortedlist
