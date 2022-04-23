def is_anagram(first_string, second_string):
    return bubble_sort(
        list(first_string.lower())) == bubble_sort(list(second_string.lower()))


def bubble_sort(word):
    has_swapped = True
    count = 0
    while has_swapped:
        has_swapped = False
        for index in range(len(word) - count - 1):
            if word[index] > word[index + 1]:
                word[index], word[index + 1] = word[index + 1], word[index]
                has_swapped = True
        count += 1

    return word

# Referêcia bubble_sort: Conteúdo da Trybe
