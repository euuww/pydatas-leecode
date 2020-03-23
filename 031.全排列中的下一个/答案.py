class Solution(object):
  def nextPermutation(self, nums):
    if nums is None or len(nums) <= 1:
      return

    pos = None
    p = len(nums) - 2
    while p >= 0:
      if nums[p + 1] > nums[p]:
        pos = p
        break
      p -= 1

    if pos is None:
      self.reverse(nums, 0, len(nums) - 1)
      return

    minPos, minV = pos + 1, nums[pos + 1]
    for i in range(pos + 1, len(nums)):
      if nums[i] <= minV and nums[i] > nums[pos]:
        minV = nums[i]
        minPos = i
    # 交换变量
    nums[pos], nums[minPos] = nums[minPos], nums[pos]
    self.reverse(nums, pos + 1, len(nums) - 1)

  def reverse(self, nums, start, end):
    while start < end:
      nums[start], nums[end] = nums[end], nums[start]
      start += 1
      end -= 1