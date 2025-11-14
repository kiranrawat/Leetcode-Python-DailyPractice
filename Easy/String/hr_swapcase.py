def swap_case(s):
    swap_str = ""
    for char in s:
        if char.islower():
            char = char.upper()
        else:
            char = char.lower()
        swap_str += char
    return swap_str


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
