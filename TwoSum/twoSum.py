class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indexCount = 0 #index count, the value to key
        seenNum = {} #list for numbers we have seen key = numElement 
        for num in nums:
            complement = target - num #we need the complement here to compare to see if we have a matching item in the list
            #if the comparison is true the solution would be a list of the index of the complement and the current number
            #indexCount is the current index number
            if(complement in seenNum):
                solution = [indexCount, nums.index(complement)]
                return(solution)
            seenNum[num] = indexCount
            indexCount = indexCount + 1
        
        #if not returned in the loop, return 
        return []

        

        
        