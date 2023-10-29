def get_participant_list(first_str, second_str, separator=","):
    result = []

    first_list = []
    buffer_name = ""
    for i in range(0, len(first_str)):
        if first_str[i] == separator:
            first_list.append(buffer_name)
            buffer_name = ""
        else:
            buffer_name += first_str[i]
    first_list.append(buffer_name)

    second_list = []
    buffer_name = ""
    for i in range(0, len(second_str)):
        if second_str[i] == separator:
            second_list.append(buffer_name)
            buffer_name = ""
        else:
            buffer_name += second_str[i]
    second_list.append(buffer_name)

    # для перебора меньшего списка и ускорения тем самым процесса
    smallest_list = []
    biggest_list = []
    if len(first_list) > len(second_list):
        smallest_list = second_list
        biggest_list = first_list
    else:
        smallest_list = first_list
        biggest_list = second_list

    for person in smallest_list:
        if biggest_list.count(person):
            result.append(person)

    return result


first = "A,B,C,D,Ehg,Rr"
second = "A,B,E,Rr"

print(get_participant_list(first, second))

first = "A;B;C;D,Ehg;Rr,55"
second = "A;B;E;Rr,55"

print(get_participant_list(first, second, ";"))
