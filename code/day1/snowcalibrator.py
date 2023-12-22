import inflect
from word2number import w2n
from attrs import define
from typing import List, Dict


@define
class SnowCalibrator:
    fancy_values: List[str]
    numbers: List[str]
    words: List[str]
    include_words: bool

    @classmethod
    def construct_instance(cls, include_words: bool = True):
        with open('input.txt') as file:
            lines = [line.strip() for line in file.readlines()]
        numbers_strings = cls.create_list_of_string_ints()
        numbers_words = cls.create_list_of_word_ints()
        return cls(lines, numbers_strings, numbers_words, include_words)

    @staticmethod
    def create_list_of_string_ints() -> List[str]:
        numbers = list(range(0, 10))
        string_numbers = [str(number) for number in numbers]
        return string_numbers

    @staticmethod
    def create_list_of_word_ints() -> List[str]:
        parser = inflect.engine()
        numbers = list(range(0, 10))
        words = []
        for number in numbers:
            word = parser.number_to_words(number)
            words.append(word)
        return words

    def set_include_words(self, include_words: bool):  # if forever reason you want to swap during run
        self.include_words = include_words

    def sum_all_numbers(self):
        numbers = self.get_all_numbers()
        return sum(numbers)

    def get_all_numbers(self) -> List[int]:
        all_numbers = []
        for line in self.fancy_values:
            mapping = self.find_first_and_last_number(line)   # mapping -> {position: number}
            number1 = list(mapping.get("first_occurrence").values())[0]
            number2 = list(mapping.get("last_occurrence").values())[0]
            combined_number = int(str(number1)+str(number2))
            all_numbers.append(combined_number)

        return all_numbers

    def find_first_and_last_number(self, line: str) -> Dict:
        numbers_mapping = {"first_occurrence": {100: "foo"}, "last_occurrence": {-1: "bar"}}

        for number in self.numbers:
            # find from left to right
            position1 = line.find(number)
            if -1 < position1 < next(iter(numbers_mapping.get("first_occurrence"))):
                numbers_mapping["first_occurrence"] = {position1: int(number)}
            # find from right to left
            position2 = line.rfind(number)
            if position2 > next(iter(numbers_mapping.get("last_occurrence"))):
                numbers_mapping["last_occurrence"] = {position2: int(number)}

        # if you want to include words like 'one' in your search
        if self.include_words is True:
            for number in self.words:
                # find from left to right
                position1 = line.find(number)
                if -1 < position1 < next(iter(numbers_mapping.get("first_occurrence"))):
                    numbers_mapping["first_occurrence"] = {position1: w2n.word_to_num(number)}
                # find from right to left
                position2 = line.rfind(number)
                if position2 > next(iter(numbers_mapping.get("last_occurrence"))):
                    numbers_mapping["last_occurrence"] = {position2: w2n.word_to_num(number)}

        return numbers_mapping  # {position: number}

