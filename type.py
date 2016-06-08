'''
-------------------
Author: Max Shoshin
Crated:  08.06.2016
-------------------
'''

# Типы данных с примерами использования

# Числа
# ==================================================================
print(type(1))                                  # <class 'int'>
print(type(1.0))                                # <class 'float'>
print(5/2)                                      # 2.5
print(5//2)                                     # 2
print(5**2)                                     # 25
print(5 % 2)                                    # 1
print()
# ==================================================================

# Списки
# ==================================================================
print(type([1, 2, 3, 'abc', [1, 2, 3], 4]))     # <class 'list'>
print([c * 3 for c in 'list'])                  # list comprehension
lst = [1, 1, 5]                                 # append method
lst.append(7)                                   # add num
print(lst)                                      # [1, 1, 5, 7]
lst.extend([2, 11])                             # add list
print(lst)                                      # [1, 1, 5, 7, 2, 11]
lst.insert(0,-1)                                # add num in..
print(lst)                                      # [-1, 1, 1, 5, 7, 2, 11]
print(lst.count(1))                             # 2
lst.remove(1)                                   # delete first num
print(lst)                                      # [-1, 1, 5, 7, 2, 11]
lst.sort()                                      # sort method
print(lst)                                      # [-1, 1, 2, 5, 7, 11]