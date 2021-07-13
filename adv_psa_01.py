#  Q1 - Find out the max sum of the longest continues subarray. Kadane's Algo. Expected time complexity O(N), Space complexity O(1) or constant


def the_max_sum(given_list):
    size_of_list = len(given_list)
    current = given_list[0]
    so_far = given_list[0]
    for a in range(1, size_of_list):
        current = max(given_list[a], current + given_list[a])
        so_far = max(so_far, current)
    return so_far



#  Q2 - Find out the index of subarray which is out of order in a partially sorted array.







if __name__ == "__main__":
    given_list = [3, 5,-9 , 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
    kadens_algo = the_max_sum(given_list)
    print(f'The sum of the contagious subarray of the list {given_list} is:', kadens_algo)
