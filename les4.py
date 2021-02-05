# ex1
my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
print(set(my_list_1) - set(my_list_2))

# ex2
date = input('Введите дату в формате dd.mm.yyyy ')
parse_date = date.split(sep='.')
date_Day = ('first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh',
            'twelfth', 'thirteenth', 'fourteenth', 'fifteenth', 'sixteenth', 'seventeenth', 'eighteenth', 'nineteenth',
            'twentieth', 'twenty-first', 'twenty-second', 'twenty-third', 'twenty-fourth', 'twenty-fifth',
            'twenty-sixth', 'twenty-seventh', 'twenty-eighth', 'twenty-ninth', 'thirty', 'thirty-first')
date_Month = ('January', 'Februvc  v y  ary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December')
day = date_Day[int(parse_date[0]) - 1]
month = date_Month[int(parse_date[1]) - 1]
year = parse_date[2]
print('The {} of {}, {} year'.format(day, month, year))

# ex3
my_list_1 = [3, 3, 3, 3, 3, 9, 3]
unique_list = []
for element in set(my_list_1):
    if my_list_1.count(element) == 1:
        unique_list.append(element)
print(unique_list)
