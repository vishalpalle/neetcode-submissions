class Solution:
    def productExceptSelf(self, nums):

        zero_count = 0
        total = 1

        # multiply non-zero elements only
        for n in nums:
            if n == 0:
                zero_count += 1
            else:
                total *= n

        res = []

        for n in nums:

            # case: more than one zero
            if zero_count > 1:
                res.append(0)

            # case: exactly one zero
            elif zero_count == 1:

                if n == 0:
                    res.append(total)
                else:
                    res.append(0)

            # case: no zeros
            else:
                res.append(total // n)

        return res