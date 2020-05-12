
def quicksort(nums: list):
    def _partition(nums: list, low: int, high: int):
        i = low - 1
        pivot = high
        for j in range(low, high):
            if nums[j] <= nums[pivot]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[pivot] = nums[pivot], nums[i+1]

        return i + 1

    def _quicksort(nums, low, high):
        if low < high:
            p = _partition(nums=nums, low=low, high=high)
            _quicksort(nums=nums, low=low, high=p-1)
            _quicksort(nums=nums, low=p+1, high=high)

    return _quicksort(nums=nums, low=0, high=len(nums) - 1)

if __name__ == '__main__':
    nums = [3, 5, 1, 6, 2, 7, 4, 0]
    quicksort(nums=nums)
    print(nums)
