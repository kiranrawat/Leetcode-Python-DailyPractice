if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # sorted_arr = sorted(set(arr)) #nlogn
    # print(sorted_arr[-2])

    def max_element(arr):
        max_val = arr[0]
        i = 0
        while i < len(arr):
            if arr[i] > max_val:
                max_val = arr[i]
            i += 1
        return max_val

    def second_max_element(arr, max_elem):
        second_max_val = -101
        i = 0
        while i < len(arr):
            if (arr[i] != max_elem) and (arr[i] > second_max_val):
                second_max_val = arr[i]
            i += 1
        return second_max_val

    max_val = max_element(arr)
    print(second_max_element(arr, max_val))


# time complexity => o(n)
# space complexit => o(1)
