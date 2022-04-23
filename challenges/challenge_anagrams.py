def is_anagram(first_string, second_string):
    return merge_sort(
        list(first_string.lower())) == merge_sort(list(second_string.lower()))


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left, right = merge_sort(array[:mid]), merge_sort(array[mid:])
    return merge(left, right, array.copy())


def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]
    return merged


'''
merge_sort:
(é um algoritmo de ordenação que usa dividir e conquistar,
tem mais eficiência do que o bubble sort neste caso.)
Referência - Conteúdo do bloco:
https://app.betrybe.com/course/computer-science/algoritmos/algoritmos-de-ordenacao-e-busca/29521083-44ea-488d-a74d-216b1ac79b04/conteudos/766d59bd-a04f-41a9-b41b-5fb37a2f2a3a/algoritmos-de-ordenacao/1adc1a6e-51c7-4065-ae2c-e5f8194e7578?use_case=side_bar
'''
