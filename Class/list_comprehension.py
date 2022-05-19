lst = [num for num in range(1, 11)]
print(lst)

evens = [num for num in range(1, 11) if num % 2 == 0]
print(evens)

even_and_squared_odds = [num if num % 2 == 0 else num ** 2 for num in range(1, 11)]
print(even_and_squared_odds)

lst_input =[int(input("Enter a number: ")) for num in range(1, 4)]
print(lst_input)

list_nested_for = [(x, y) for x in range(1, 5) for y in range(6, 10)]
print(list_nested_for)

upper_name = [name.upper() for name in ["Iyawo anobi", "tolani", "ayuba"]]
print(upper_name)

name_length = [len(name) for name in ["Iyawo anobi", "tolani", "ayuba"]]
print(name_length)

#generator expression
lst = [num for num in range(1, 11)]
gen = (num for num in range(1, 11))
print(sum(lst))
print(sum(gen))

#dic comprehension

dict_comp = {k: v for k, v in zip(range(5), range(5))}
print(dict_comp)