from typing import List

def read_integers() -> List[int]:
    init_input = input()
    value = init_input.split(",")
    int_list = []
    
    for i in value:
        int_list.append(int(i))
    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
