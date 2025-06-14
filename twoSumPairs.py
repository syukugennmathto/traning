class Solution:
    def twoSumAllPairs(self, nums: List[int], target: int) -> List[Tuple[int, int]]:
        num_to_indices = {}
        for i, num in enumerate(nums):
            num_to_indices.setdefault(num, []).append(i)

        seen = set()
        result = []

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_indices:
                for j in num_to_indices[complement]:
                    if i <= j:
                        pair = (i, j)
                        if pair not in seen:
                            seen.add(pair)
                            result.append(pair)
        return result
