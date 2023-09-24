def is_anagram(first_string, second_string):
    list_first_string = list(first_string)
    list_second_string = list(second_string)

    list_first_string.sort()
    list_second_string.sort()

    position = 0
    equals = True

    while position < len(first_string) and equals:
        if list_first_string[position] == list_second_string[position]:
            position = position + 1
        else:
            equals = False

    return equals
