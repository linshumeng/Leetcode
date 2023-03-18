# Leetcode

To record daily progress

## [Binary Search](https://leetcode.cn/problems/binary-search/)

Date: 0220
Category: Array
Difficulty: Easy
Note:

- while condition
- floor division(in case there is a remainder)

## [Remove Element](https://leetcode.cn/problems/remove-element/)

Date: 0222
Category: Array
Difficulty: Easy
Note:

- use fast pointer to iterate all the list
- if same, slow should stop, waiting for the next not same to replace

## [Squares of a Sorted Array](https://leetcode.cn/problems/squares-of-a-sorted-array/)

Date: 0223
Category: Array
Difficulty: Easy
Note:

- reverse order iterate the list

## [Minimum Size Subarray Sum](https://leetcode.cn/problems/minimum-size-subarray-sum/)

Date: 0224
Category: Array
Difficulty: Medium
Note:

- use index variable as a pointer

##[Spiral Matrix II](https://leetcode.cn/problems/spiral-matrix-ii/)

Date: 0226
Category: Array
Difficulty: Medium
Note:

- divide into loops
- first block in the loop is true and the last block in the loop is false

## [Remove Linked List Elements](https://leetcode.cn/problems/remove-linked-list-elements/)

Date: 0227
Category: Linked List
Difficulty: Easy
Note:

- dummy head

## [Design Linked List](https://leetcode.cn/problems/design-linked-list/)

Date: 0301
Category: Linked List
Difficulty: Medium
Note:

- a class for node
- in add, can add the index >= size, but in delete, index < size
- for single direction linked list, firstly connect the node behind and then connce the node in the front

## [Reverse Linked List](https://leetcode.cn/problems/reverse-linked-list/)

Date: 0302
Category: Linked List
Difficulty: Easy
Note:

- store the next first and then process

## [Swap Nodes in Pairs](https://leetcode.cn/problems/swap-nodes-in-pairs/)

Date: 0303
Category: Linked List
Difficulty: Medium
Note:

- [猿来绘（逻辑清晰，简单易懂）- 24. 两两交换链表中的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/solution/yuan-lai-hui-luo-ji-qing-xi-jian-dan-yi-8t93h/)

## [Remove Nth Node From End of List](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/)

Date: 0304
Category: Linked List
Difficulty: Medium
Note:

- bf: get the toal length of the array, and use a for loop which stops at the exact position
- two pointers: fast runs firstly and then slow runs

## [Intersection of Two Linked Lists LCCI](https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/)

Date: 0306
Category: Linked List
Difficulty: Easy
Note:

- align at the end of the lists
- make sure one linked list is always longer than the other

## [Linked List Cycle II](https://leetcode.cn/problems/linked-list-cycle-ii/)

Date: 0307
Category: Linked List
Difficulty: Medium
Note:

- two pointers
- x = y means that one pointer run from head and one from the meeting point, if they run at the same speed, they will meet at the crossing point
- judge fast and fast.next exist

## [Valid Anagram](https://leetcode.cn/problems/valid-anagram/)

Date: 0308
Category: Hash Table
Difficulty: Easy
Note:

- store in different dictionaries

## [Intersection of Two Arrays](https://leetcode.cn/problems/intersection-of-two-arrays/)

Date: 0309
Category: Hash Table
Difficulty: Easy
Note:

- return a list

## [Happy Number](https://leetcode.cn/problems/happy-number/)

Date: 0310
Category: Hash Table
Difficulty: Easy
Note:

- define a function to calculate sum
- create a set to store the sum, if the sum appears again, then return False

## [Two Sum](https://leetcode.cn/problems/two-sum/)

Date: 0313
Category: Hash Table
Difficulty: Easy
Note:

- judge whether the residual is in the dictionary

## [4Sum II](https://leetcode.cn/problems/4sum-ii/)

Date: 0314
Category: Hash Table
Difficulty: Medium
Note:

- create a dictionary to stroe the sum from the first two list
- iterate the last two list, check the sum

## [Ransom Note](https://leetcode.cn/problems/ransom-note/)

Date: 0315
Category: Hash Table
Difficulty: Easy
Note:

- search ransomNote in magazine

## [3Sum](https://leetcode.cn/problems/ransom-note/)

Date: 0316
Category: Hash Table
Difficulty: Medium
Note:

- if nums[i] > 0: break, not false
- append is list, not three elements
- if cur == 0, how to avoid duplicate

## [4Sum](https://leetcode.cn/problems/4sum/)

Date: 0317
Category: Hash Table
Difficulty: Medium
Note:

- two for loop
