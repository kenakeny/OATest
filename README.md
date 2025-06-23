**NeetCode 150 – Python Cold Start Project**

**Objective:**  
Accelerate Python mastery and DSA by learning & finishing the NeetCode 150 problem set using Python  
This project is a 3-day challenge set by myself to have fun and prepare for any coding assessment.

## 💻 Environment

- Language: Python 3
- IDE: VSCode/PyCharm

## 🧱 Progress Log

| Day | Category            | Problems Completed | Notes |
|-----|---------------------|--------------------|-------|
| 1   | Arrays & Hashing    | 3                  | Hash map, enumerates |
| x   | x                   | x                  | x |
| x   | x                   | x                  | x |
| x   | x                   | X                  | x |


```python
"""
Title 
Title: Two Sum (LeetCode #1)
Time: 13 minutes
Difficulty: Easy
Category: Arrays & Hashing
Approach:
- Use a hash map to store complement and index.
- If complement found, return indices.

Time Complexity: O(n)
Space Complexity: O(n)
"""
def twoSum(nums, target):
    hashmap = {}
    for i, val in enumerate(nums):
        diff = target - val
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[val] = i
```

---

## 🚀 Mission Goals

- [ ] Complete as many problems in NeetCode with clean, logged solutions.
- [ ] Internalize common DSA patterns: Sliding Window, Binary Search, Two Pointers, etc.
- [ ] Be OA-ready for top-tier tech companies
