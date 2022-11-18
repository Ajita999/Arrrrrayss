str = "Hi my name is Ajita"
str_arr = list(str)
print(str_arr)
output_str = ""
for i in range(0,len(str_arr)):
  output_str = output_str+str_arr[len(str_arr)-1-i]
print(output_str)


str_arr.reverse()
print(str_arr)