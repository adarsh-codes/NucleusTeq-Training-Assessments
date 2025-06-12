
def operate_list(list):
    total_sum = sum(list)
    average = total_sum/len(list)
    return total_sum,average

list = [1,2,3,4,5, 6,7]
sum, average = operate_list(list)
print("Sum : ",sum,", Average : ",average)