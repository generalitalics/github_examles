'''
-------------------
Author: Max Shoshin
Crated:  08.06.2016
-------------------
'''

# Типы данных с примерами использования + Основные методы

# Числа
# ==================================================================
print('Numeric')
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
print('List')
print(type([1, 2, 3, 'abc', [1, 2, 3], 4]))     # <class 'list'>
print([c * 3 for c in 'list'])                  # list comprehension
                                                # ['lll', 'iii', 'sss', 'ttt']
lst = [1, 1, 5]                                 # append method
print(lst[1])                                   # 1
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
lst.pop(2)                                      # pop method. last num
print(lst)                                      # [-1, 1, 5, 7, 11]
print([1, 2, 3] + [4, 5, 6])                    # [1, 2, 3, 4, 5, 6]
print()
# ==================================================================

# Словари
# ==================================================================
print('Dict')
print(type({1: 'abc', 4: 'dsr'}))               # <class 'dict'>
print({i: i ** 2 for i in range(4)})            # dict^^ comprehension
                                                # {0: 0, 1: 1, 2: 4, 3: 9}
dct = {1: 'HH', 2: 'RR'}                        # dictionary
print(dct[1])                                   # HH
dct[3] = 'JJ'                                   # add new key: value
print(dct)                                      # {1: 'HH', 2: 'RR', 3: 'JJ'}
print(dct.get(8, 'Not key!'))                   # Not key '8': 'Not key!'
print(dct.keys())                               # dict_keys([1, 2, 3])
print(len(dct))                                 # 3
print(dct.values())                             # dict_values(['HH', 'RR', 'JJ'])
print()
# ==================================================================

# Кортежи (tuple)
# ==================================================================
print('Tuple')
print(type((2, 2.05, "Hello")))                 # <class 'tuple'>
tp = (2, 2, 'ggg', [1, 2, 3])                   # tuple
tp2 = (4, 'hdd')                                # tuple2
print(tp+tp2)                                   # (2, 2, 'ggg', [1, 2, 3], 4, 'hdd')
print(tp[3])                                    # [1, 2, 3]
print(tp.index('ggg'))                          # 2
print(tp.count(2))                              # 2
print()
# ==================================================================

# Множества (set & frozenset)
# ==================================================================
print('Set')
print(type({1, 2, 3, 'e'}))                     # <class 'set'>
st = {1, 5, 'rrrt', 4}                          # set
st2 = {5, 'rrrt', 1, 4}                         # set
print(st == st2)                                # True
print(4 in st)                                  # True
st.add('ff')                                    # add new elem
print(st)                                       # {1, 'ff', 4, 5, 'rrrt'}
print(len(st))                                  # 5
print(st.difference(st2))                       # {'ff'}
fst = frozenset('12345')                        # frozenset - unchanged set
print(fst)                                      # frozenset({'4', '1', '5', '3', '2'})
print()
# ==================================================================