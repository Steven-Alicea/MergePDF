import re

# checks if the input is a valid regex sequence
def is_regex_sequence(input_string):
    input_string = input_string.replace(" ", "")
    pattern = r"^(\d+)(?:(?:,|[-])(\d+))*$"
    match = re.match(pattern, input_string)
    if not match:
        return False
    return True

# removes duplicates from a list
def sort_and_remove_duplicates(pages_list):
    seen = set()
    unique_list = []
    for number in pages_list:
        number -= 1 # for remove pages function
        if number not in seen:
            seen.add(number)
            unique_list.append(number)
    unique_list.sort()
    return unique_list

# gets all page numbers from input
def get_page_deletion_list(input_string):
    result = []
    for part in input_string.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            result.extend(range(start, end + 1))
        else:
            result.append(int(part))
    result = sort_and_remove_duplicates(result)
    return result
