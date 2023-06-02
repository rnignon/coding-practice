import re
def solution(s):
    nums = {}
    tokens = re.findall('\d+', s)
    for token in tokens :
        if token in nums.keys() : nums[token] += 1
        else : nums[token] = 1
    answer = sorted(nums.items(), key = lambda x : -x[1])
    answer = [int(i[0]) for i in answer]
    return answer