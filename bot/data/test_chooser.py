import json
import random


def test_chooser(lang, level, number):
    with open(f"bot/data/test_base/{lang}/{level}.json", "r") as f:
        tests = json.load(f)['tests']
    all_test_count = len(tests)
    selected_numbers = random.sample(list(range(all_test_count)), int(number))
    selected_tests = [tests[i] for i in selected_numbers]
    return selected_tests
