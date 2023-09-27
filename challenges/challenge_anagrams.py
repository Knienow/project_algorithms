def spread_caractere(string):
    # string = string.lower()
    if len(string) <= 1:
        return string
    middle = len(string) // 2
    left = string[:middle]
    right = string[middle:]

    left = spread_caractere(left)
    right = spread_caractere(right)
    result = before_sort_after_merge(left, right)
    return result


def before_sort_after_merge(left, right):
    word = []
    index_l = 0
    index_r = 0
    while index_l < len(left) and index_r < len(right):
        if left[index_l] < right[index_r]:
            word.append(left[index_l])
            index_l += 1
        else:
            word.append(right[index_r])
            index_r += 1
    word.extend(left[index_l:])
    word.extend(right[index_r:])
    return word


def join_sorted_string(string):
    string = list(string)
    empty = ''
    list_string = empty.join(spread_caractere(string))
    return list_string


def is_anagram(first_string, second_string):
    first_string = first_string.casefold()
    second_string = second_string.casefold()
    first_str_spread = join_sorted_string(first_string)
    second_str_spread = join_sorted_string(second_string)
    if not first_string or not second_string:
        return (first_str_spread, second_str_spread, False)
    if len(first_string) != len(second_string):
        return (first_str_spread, second_str_spread, False)
    if first_str_spread == second_str_spread:
        return (first_str_spread, second_str_spread, True)
    else:
        return (first_str_spread, second_str_spread, False)
