def add_two_numbers() -> int:
    int_list = []
    line = input()
    value = line.split(",")

    for i in value:
        int_list.append(int(i))
    return sum(int_list)


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
