def find_common_participants(first_str, second_str, separator=","):

    first_set = set()
    buffer_name = ""
    for i in range(0, len(first_str)):
        if first_str[i] == separator:
            first_set.add(buffer_name)
            buffer_name = ""
        else:
            buffer_name += first_str[i]
    first_set.add(buffer_name)

    second_set = set()
    buffer_name = ""
    for i in range(0, len(second_str)):
        if second_str[i] == separator:
            second_set.add(buffer_name)
            buffer_name = ""
        else:
            buffer_name += second_str[i]
    second_set.add(buffer_name)

    result =set()
    result = first_set.intersection(second_set)


    return result

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group,participants_second_group,"|"))

participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

print(find_common_participants(participants_first_group,participants_second_group))