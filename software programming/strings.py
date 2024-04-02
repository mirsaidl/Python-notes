name = "Mirsaid"
id = "12225253"
age = 17

united_string = f'{name} , {id} , {age}'

#Q0
print("Q0 => " , united_string)

#Q1
splitted_string = united_string.split(',')
print("Q1 => " , splitted_string)

#Q2
unified_name = splitted_string[0]
unified_ID = splitted_string[1]
unified_age = splitted_string[2]
print("Q2 => " , f'name >>> {unified_name}, id >>> {unified_ID}, age >>> {unified_age}', sep = " " )

#Q3
print("Q3 => ", united_string[:10])





