def do_math_stuff(list_of_nums):
    result = [num * 2 if num % 2 == 0 else num * 3 for num in list_of_nums] # If number is even mult by 2 else mult by 3.
    return result


def do_string_stuff(list_of_strings):
    x = ""
    for s in list_of_strings:
        if len(s) > 5:
            x += s.upper() + " "
        else:
            x += s.lower() + " "
    return x.strip()


def main():
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_nums = do_math_stuff(list1)
    processed_strings = do_string_stuff(list2)

    print("Processed Numbers:", processed_nums)
    print("Processed Strings:", processed_strings)


if __name__ == "__main__":
    main()
