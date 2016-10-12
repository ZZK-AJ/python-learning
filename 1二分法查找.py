#!_*_coding:utf-8_*_
def binary_search(data_list, find_num):
    mid_pos = int(len(data_list) / 2)  # find the middle position of the list
    mid_val = data_list[mid_pos]  # get the value by it's position
    print(data_list)
    if len(data_list) > 1:
        if mid_val > find_num:  # means the find_num is in left hand of mid_val
            print("[%s] should be in left of [%s]" % (find_num, mid_val))
            binary_search(data_list[:mid_pos], find_num)    # in here to ; data_list[:mid_pos]
        elif mid_val < find_num:  # means the find_num is in the right hand of mid_val
            print("[%s] should be in right of [%s]" % (find_num, mid_val))
            binary_search(data_list[mid_pos:], find_num)
        else:  # means the mid_val == find_num
            print("Find ", find_num)

    else:
        print("cannot find [%s] in data_list" % find_num)


if __name__ == '__main__':
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    binary_search(primes, 5)


