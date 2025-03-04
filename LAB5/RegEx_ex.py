import re
#1 Что делает:
# Проверяет, состоит ли строка только из:

# a (может быть сколько угодно или вообще не быть)
# b (может быть сколько угодно или вообще не быть)
def match_a_b(s):
    return re.fullmatch("a*b*", s) is not None



#2 Что делает:
# Проверяет, состоит ли строка только из:

# a (обязательно одна)
# b (ровно 2 или 3)

def match_a_b2_3(s):
    return re.fullmatch("ab{2,3}", s) is not None



#3 Что делает:
# Ищет в строке слова, где маленькие буквы соединены _.

def find_lowercase_underscore(s):
    return re.findall("\b[a-z]+_[a-z]+\b", s)



# 4 Что делает:
# Ищет слова, где первая буква заглавная, а остальные строчные.

def find_upper_lower(s):
    return re.findall("[A-Z][a-z]+", s)



# 5 Что делает:
# Проверяет, начинается ли строка с a, заканчивается на b, 
# а между ними может быть что угодно.

def match_a_anything_b(s):
    return re.fullmatch("a.*b", s) is not None




#6 Что делает:
# Заменяет пробелы, запятые и точки на :
def replace_delimiters(s):
    return re.sub("[ ,.]", ":", s)



#7 Что делает:
# Преобразует snake_case → CamelCase.
def snake_to_camel(s):
    words = s.split("_")
    return "".join(word.capitalize() for word in words)




#8 Что делает:
# Разбивает строку перед заглавными буквами.

def split_at_uppercase(s):
    return re.split("(?=[A-Z])", s)



#9 Что делает:
# Добавляет пробел перед каждой заглавной буквой, кроме первой.

def insert_spaces_capital(s):
    return re.sub("(?<!^)(?=[A-Z])", " ", s)




#10 Что делает:
# Преобразует CamelCase → snake_case.

def camel_to_snake(s):
    return re.sub("(?<!^)(?=[A-Z])", "_", s).lower()




examples = ["ab", "a", "abb", "abbb", "hello_world", "CamelCaseString", "AStringWithCapitals", "aanythingb", "This, is. a test"]

for ex in examples:
    print(f"Строка: {ex}")
    print(f"match_a_b: {match_a_b(ex)}")
    print(f"match_a_b2_3: {match_a_b2_3(ex)}")
    print(f"find_lowercase_underscore: {find_lowercase_underscore(ex)}")
    print(f"find_upper_lower: {find_upper_lower(ex)}")
    print(f"match_a_anything_b: {match_a_anything_b(ex)}")
    print(f"replace_delimiters: {replace_delimiters(ex)}")
    print(f"snake_to_camel: {snake_to_camel(ex)}")
    print(f"split_at_uppercase: {split_at_uppercase(ex)}")
    print(f"insert_spaces_capital: {insert_spaces_capital(ex)}")
    print(f"camel_to_snake: {camel_to_snake(ex)}")
    print('-' * 40)
