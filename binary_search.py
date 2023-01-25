# code your iterative algorithm here

def binary_search(data, el):
    first = 0
    last = len(data) - 1
    found = False

    while first <= last and not found:
        # We want to use the '//' division operator so that an integer value is returned. 
        # If we used '/', we would be working with a floating point value.
        mid = (first+last)//2

        if data[mid] == el:
            found = True
        else:
            if el < data[mid]:
                last = mid-1
            else:
                first = mid+1
    return found

test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]
print(binary_search(test_list, 22))