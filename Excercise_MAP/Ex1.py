def change(string):
    return string.capitalize()
string = ('nguyenphuocquyen',"lop20CDT2")
result = map(change,string)
result_list = '\n' .join(result)
print(f"Convert capitalize:\n{result_list}")
#note: map(ham, iter)
#map chỉ nhận được kiểu tuple hoặc list 
#join chỉ với chuỗi 