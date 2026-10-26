def list_operation(list_of_nums):
    result = [num * 2 if num % 2 == 0 else num * 3 
        for num in list_of_nums] # If number is even mult by 2 else mult by 3.
    return result


def string_operation(list_of_strings):
    result = " ".join(
        string.upper() if len(string) > 5 else string.lower()
        for string in list_of_strings # Creates a single string where greater than 5 in length
                                      # are in all uppercase else all in lowercase.
    )
    return result


def main():
    list1 = [1, 2, 3, 4, 5, 6, 7]
    list2 = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    processed_nums = list_operation(list1)
    processed_strings = string_operation(list2)

    print("Processed Numbers:", processed_nums)
    print("Processed Strings:", processed_strings)


if __name__ == "__main__":
    main()
