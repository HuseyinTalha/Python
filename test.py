input_string = (input("Enter"))
input_int = int(input_string)
input_list = [int(x) for a, x in enumerate(str(input_int))]
output_list = []
list_len = len(input_list)

for i in range(len(input_list)):
    n = i + 1
    while i == list_len:
        break
    else:
        if input_list[i] % 2 != 0:
            while n == list_len:
                break
            else:
                if input_list[n] % 2 != 0:
                    output_list.append(input_list[i])
                    output_list.append("-")
                else:
                    output_list.append(input_list[i])
        else:
            output_list.append(input_list[i])
else:
    True


output_string = ''.join(map(str, output_list))

print(output_string)



