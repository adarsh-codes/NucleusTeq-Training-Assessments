def apply_operations(str_list):
    result = list(map(lambda string : string.upper(),str_list))
    answer = list(filter(lambda string : len(string)>=3,result))
    return answer

string_list = ['adarsh','ed','a','nucleusteq','python','','ayush','abc']
print(apply_operations(string_list))