input_string = (input("Enter"))
input_int = int(input_string)
input_list = [int(x) for a, x in enumerate(str(input_int))]
output_list = []
list_len = len(input_list)

for i in range(len(input_list)):
    n = i + 1
    if i == ((list_len)-1):
        break
    else:
        if input_list[i] % 2 != 0:
            if n == ((list_len)-1):
                break
            else:
                if input_list[n] % 2 != 0:
                    output_list.append(input_list[i])
                    output_list.append("-")
        else:
            output_list.append(input_list[i])



output_string = ''.join(map(str, output_list))

print(output_string)
