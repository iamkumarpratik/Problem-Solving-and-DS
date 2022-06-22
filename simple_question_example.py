# Given a list of numbers, you have to find out running sum of the numbers in the list.
# Ex Input: [1,2,3,4], O/P: [1, 3 ,6, 10]


class Solutions:

    def running_sum(self, nums: list[int]) -> list[int]:

        output_list = []

        sum_by_far = 0

        for numbers in nums:
            sum_by_far += numbers
            output_list.append(sum_by_far)

        return output_list


sol_obj = Solutions()
given_list = [1,2,3,4,5,6,7]
running_sum = sol_obj.running_sum(given_list)
print(f"This running sum of the give list is {given_list}", running_sum)


