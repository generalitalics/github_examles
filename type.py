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
lst = [1, 3, 5]                                 #
lst.append(7)                                   # append method
print(lst)                                      # add element

