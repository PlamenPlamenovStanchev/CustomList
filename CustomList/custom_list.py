from copy import deepcopy
from math import inf


class CustomList:
    def __init__(self, *args):
        self.__data = list(args)

    def append(self, value):
        self.__data.append(value)
        return self.__data

    def __check_index(self, index):
        minus_bounds = index < 0 and index >= -len(self.__data)
        plus_bound = 0 <= index < len(self.__data)
        is_index_valid = minus_bounds or plus_bound
        if not is_index_valid:
            raise IndexError("Index not in range")

    def remove(self, index):
        self.__check_index(index)
        return self.__data.pop(index)

    def get(self, index):
        self.__check_index(index)
        return self.__data[index]

    def extend(self, iterable):
        self.__data.extend(iterable)
        return self.__data

    def insert(self, index, value):
        self.__check_index(index)
        self.__data.insert(index, value)
        return self.__data

    def pop(self):
        return self.__data.pop()

    def clear(self):
        self.__data.clear()

    def index(self, value):
        try:
            return self.__data.index(value)
        except ValueError:
            raise ValueError("Element is not in the list")

    def count(self, element):
        return self.__data.count(element)

    def reverse(self):
        return list(reversed(self.__data))

    def copy(self):
        return deepcopy(self.__data)

    def size(self):
        return len(self.__data)

    def add_first(self, element):
        return self.__data.index(0, element)

    def dictionize(self):
        result = {}
        for index in range(0, len(self.__data), 2):
            if len(self.__data) % 2 != 0 and index == len(self.__data) -1:
                result[self.__data[index]] = " "
            else:
                result[self.__data[index]] = self.__data[index + 1]
        return result

    def move(self, count):
        first_part = self.__data[:count]
        second_part = self.__data[count:]
        self.__data = second_part + first_part
        return self.__data

    def sum(self):
        total_sum = 0
        for el in self.__data:
            if isinstance(el, int) or isinstance(el, float):
                total_sum += el
            else:
                total_sum += len(el)
        return total_sum

    def overbound(self):
        max_element = float('-inf')
        searched_index = None
        for index in range(len(self.__data)):
            el = self.__data[index]
            if isinstance(el, int) or isinstance(el, float):
                if el >= max_element:
                    max_element = el
                    searched_index = index
            else:
                if len(el) >= max_element:
                    max_element = len(el)
                    searched_index = index
        return searched_index

    def underbound(self):
        min_element = float('inf')
        searched_index = None
        for index in range(len(self.__data)):
            el = self.__data[index]
            if isinstance(el, int) or isinstance(el, float):
                if el <= min_element:
                    min_element = el
                    searched_index = index
            else:
                if len(el) <= min_element:
                    min_element = len(el)
                    searched_index = index
        return searched_index




