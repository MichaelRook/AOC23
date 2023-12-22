import inflect
from word2number import w2n


def get_input():
    with open('input.txt') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def create_list_of_string_ints():
    numbers = list(range(0, 10))
    string_numbers = [str(number) for number in numbers]
    return string_numbers


def create_list_of_word_ints():
    parser = inflect.engine()
    numbers = list(range(0, 10))
    words = []
    for number in numbers:
        word = parser.number_to_words(number)
        words.append(word)
    return words


def find_numbers(text: str, include_words: bool):
    numbers_mapping = {"first_occurrence": {100: "foo"}, "last_occurrence": {-1: "bar"}}

    string_ints = create_list_of_string_ints()
    word_ints = create_list_of_word_ints()

    for number in string_ints:
        # find from left to right
        position1 = text.find(number)
        if -1 < position1 < next(iter(numbers_mapping.get("first_occurrence"))):
            numbers_mapping["first_occurrence"] = {position1: int(number)}
        # find from right to left
        position2 = text.rfind(number)
        if position2 > next(iter(numbers_mapping.get("last_occurrence"))):
            numbers_mapping["last_occurrence"] = {position2: int(number)}

    if include_words is True:
        for number in word_ints:
            # find from left to right
            position1 = text.find(number)
            if -1 < position1 < next(iter(numbers_mapping.get("first_occurrence"))):
                numbers_mapping["first_occurrence"] = {position1: w2n.word_to_num(number)}
            # find from right to left
            position2 = text.rfind(number)
            if position2 > next(iter(numbers_mapping.get("last_occurrence"))):
                numbers_mapping["last_occurrence"] = {position2: w2n.word_to_num(number)}

    return numbers_mapping  # {position, number}


def get_all_numbers(include_words):
    lines = get_input()
    result = []
    for line in lines:
        line_result = find_numbers(line, include_words)
        result.append(line_result)
    return result


def sum_numbers(numbers_mapping):
    total = 0
    for combination in numbers_mapping:
        number1 = list(combination.get("first_occurrence").values())[0]
        number2 = list(combination.get("last_occurrence").values())[0]
        total += int(str(number1)+str(number2))

    return total


def fugly_main_function(include_words):
    numbers = get_all_numbers(include_words)
    total = sum_numbers(numbers)
    return  total


print(fugly_main_function(include_words=True))  # toggle to False if you do not want words
