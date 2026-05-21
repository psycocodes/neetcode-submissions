class Solution:
    def search(self, nums: List[int], target: int) -> int:
        cut = nums.index(min(nums))
        fh_status = self.binary_search(nums[:cut], target)
        sh_status = self.binary_search(nums[cut:], target)
        if fh_status > -1:
            return fh_status
        elif sh_status > -1:
            return sh_status + cut
        else:
            return -1



    def binary_search(self, arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            # Calculate middle index (use floor division)
            mid = low + (high - low) // 2
            
            # Check if target is at mid
            if arr[mid] == target:
                return mid
            
            # If target is greater, ignore left half
            elif arr[mid] < target:
                low = mid + 1
            
            # If target is smaller, ignore right half
            else:
                high = mid - 1

        return -1

    

