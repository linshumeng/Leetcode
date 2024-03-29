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

## [Ransom

Note](https://leetcode.cn/problems/ransom-
Note/)

Date: 0315

Category: Hash Table

Difficulty: Easy

Note:

- search ransom
  Note in magazine

## [3Sum](https://leetcode.cn/problems/ransom-

Note/)

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

- two for-loops

## [Reverse String](https://leetcode.cn/problems/reverse-string/)

Date: 0319

Category: String

Difficulty: Easy

Note:

- two points from head and tail

## [Reverse String II](https://leetcode.cn/problems/reverse-string-ii/)

Date: 0319

Category: String

Difficulty: Easy

Note:

- declare a new string

## [ti-huan-kong-ge](https://leetcode.cn/problems/ti-huan-kong-ge-lcof/)

Date: 0320

Category: String

Difficulty: Easy

Note:

- use list to represent a string
- extend that list
- how to replace space

## [Reverse Words in a String](https://leetcode.cn/problems/reverse-words-in-a-string/)

Date: 0321

Category: String

Difficulty: Medium

Note:

- split the string
- convert to a list
- iterate word and swap

## [zuo-xuan-zhuan-zi-fu-chuan](https://leetcode.cn/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/)

Date: 0322

Category: String

Difficulty: Easy

Note:

- merge two parts

## [Find the Index of the First Occurrence in a String](https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/)

Date: 0322

Category: String

Difficulty: Medium

Note:

- a method similar to BF

## [Repeated Substring Pattern](https://leetcode.cn/problems/repeated-substring-pattern/)

Date: 0323

Category: String

Difficulty: Easy

Note:

- how can we get the old string

## [Implement Queue using Stacks](https://leetcode.cn/problems/implement-queue-using-stacks/)

Date: 0331

Category: Stack

Difficulty: Easy

Note:

- Reuse pop in peek

## [Implement Stack using Queues](https://leetcode.cn/problems/implement-stack-using-queues/)

Date: 0401

Category: Stack

Difficulty: Easy

Note:

- Use one deque

## [Valid Parentheses](https://leetcode.cn/problems/valid-parentheses/)

Date: 0402

Category: Stack

Difficulty: Easy

Note:

- the way to return false

## [Remove All Adjacent Duplicates In String](https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string/)

Date: 0403

Category: Stack

Difficulty: Easy

Note:

- write append in else condition

## [Evaluate Reverse Polish Notation](https://leetcode.cn/problems/evaluate-reverse-polish-notation/)

Date: 0404

Category: Stack

Difficulty: Medium

Note:

- how to use eval

## [Sliding Window Maximum](https://leetcode.cn/problems/sliding-window-maximum/)

Date: 0405

Category: Stack

Difficulty: Hard

Note:

- create a new data structure

## [Top K Frequent Elements](https://leetcode.cn/problems/top-k-frequent-elements/)

Date: 0407

Category: Stack

Difficulty: Medium

Note:

- how to sort a dictionary

## [Binary Tree Inorder Traversal](https://leetcode.cn/problems/binary-tree-inorder-traversal/)

Date: 0415

Category: Binary Tree

Difficulty: Easy

Note:

- write a helper function

## [Binary Tree Postorder Traversal](https://leetcode.cn/problems/binary-tree-postorder-traversal/)

Date: 0415

Category: Binary Tree

Difficulty: Easy

Note:

- write a helper function

## [Binary Tree Preorder Traversal](https://leetcode.cn/problems/binary-tree-preorder-traversal/)

Date: 0415

Category: Binary Tree

Difficulty: Easy

Note:

- write a helper function

## [Binary Tree Level Order Traversal](https://leetcode.cn/problems/binary-tree-level-order-traversal/)

Date: 0418

Category: Binary Tree

Difficulty: Medium

Note:

- use deque

## [Binary Tree Level Order Traversal II](https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/)

Date: 0419

Category: Binary Tree

Difficulty: Medium

Note:

- use deque
- reverse

## [Binary Tree Right Side View](https://leetcode.cn/problems/binary-tree-right-side-view/)

Date: 0419

Category: Binary Tree

Difficulty: Medium

Note:

- keep only the last element in each level

## [Binary Tree Right Side View](https://leetcode.cn/problems/binary-tree-right-side-view/)

Date: 0419

Category: Binary Tree

Difficulty: Medium

Note:

- keep only the last element in each level

## [Average of Levels in Binary Tree](https://leetcode.cn/problems/average-of-levels-in-binary-tree/)

Date: 0419

Category: Binary Tree

Difficulty: Easy

Note:

- calculate the average by saving sum and count

## [N-ary Tree Level Order Traversal](https://leetcode.cn/problems/n-ary-tree-level-order-traversal/)

Date: 0419

Category: Binary Tree

Difficulty: Medium

Note:

- extend the deque

## [Find Largest Value in Each Tree Row](https://leetcode.cn/problems/find-largest-value-in-each-tree-row/)

Date: 0419

Category: Binary Tree

Difficulty: Medium

Note:

- calculate the max

## [Populating Next Right Pointers in Each Node](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/)

Date: 0419

Category: Binary Tree

Difficulty: Medium

Note:

- compute the position of the last node

## [Populating Next Right Pointers in Each Node II](https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/)

Date: 0419

Category: Binary Tree

Difficulty: Medium

Note:

- compute the position of the last node

## [Maximum Depth of Binary Tree](https://leetcode.cn/problems/maximum-depth-of-binary-tree/)

Date: 0419

Category: Binary Tree

Difficulty: Medium

Note:

- count the level

## [Minimum Depth of Binary Tree](https://leetcode.cn/problems/minimum-depth-of-binary-tree/)

Date: 0419

Category: Binary Tree

Difficulty: Easy

Note:

- no left and right means the min depth

## [Symmetric Tree](https://leetcode.cn/problems/symmetric-tree/)

Date: 0421

Category: Binary Tree

Difficulty: Easy

Note:

- use recursion

## [Count Complete Tree Nodes](https://leetcode.cn/problems/count-complete-tree-nodes/)

Date: 0422

Category: Binary Tree

Difficulty: Medium

Note:

- count the nodes

## [Balanced Binary Tree](https://leetcode.cn/problems/balanced-binary-tree/)

Date: 0422

Category: Binary Tree

Difficulty: Easy

Note:

- count the depth of the given node

## [Binary Tree Paths](https://leetcode.cn/problems/binary-tree-paths/)

Date: 0422

Category: Binary Tree

Difficulty: Easy

Note:

- two deques

## [Sum of Left Leaves](https://leetcode.cn/problems/sum-of-left-leaves/)

Date: 0423

Category: Binary Tree

Difficulty: Easy

Note:

- how to check a node is the left leaf

## [Find Bottom Left Tree Value](https://leetcode.cn/problems/find-bottom-left-tree-value/)

Date: 0423

Category: Binary Tree

Difficulty: Easy

Note:

- update the val again and again

## [Path Sum](https://leetcode.cn/problems/path-sum/)

Date: 0424

Category: Binary Tree

Difficulty: Easy

Note:

- two deque, one save node, one save result

## [Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

Date: 0424

Category: Binary Tree

Difficulty: Medium

Note:

- how to split those two lists

## [Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

Date: 0424

Category: Binary Tree

Difficulty: Medium

Note:

- how to split those two lists

## [Maximum Binary Tree](https://leetcode.cn/problems/maximum-binary-tree/)

Date: 0424

Category: Binary Tree

Difficulty: Medium

Note:

- how to split the nums

## [Merge Two Binary Trees](https://leetcode.cn/problems/merge-two-binary-trees/)

Date: 0424

Category: Binary Tree

Difficulty: Easy

Note:

- recusively build the tree

## [Search in a Binary Search Tree](https://leetcode.cn/problems/search-in-a-binary-search-tree/)

Date: 0424

Category: Binary Tree

Difficulty: Easy

Note:

- if not root
- BST: left <= a, right > a

## [Validate Binary Search Tree](https://leetcode.cn/problems/validate-binary-search-tree/)

Date: 0425

Category: Binary Tree

Difficulty: Easy

Note:

- compare all the nodes
- sort the inorder traversal

## [Minimum Absolute Difference in BST](https://leetcode.cn/problems/minimum-absolute-difference-in-bst/)

Date: 0426

Category: Binary Tree

Difficulty: Easy

Note:

- inorder traversal the BST

## [Find Mode in Binary Search Tree](https://leetcode.cn/problems/find-mode-in-binary-search-tree/submissions/)

Date: 0426

Category: Binary Tree

Difficulty: Easy

Note:

- inorder traversal the BST
- create a dict and list
- output all the nodes even though their value is the same

## [Lowest Common Ancestor of a Binary Tree](https://leetcode.cn/problems/find-mode-in-binary-search-tree/submissions/)

Date: 0426

Category: Binary Tree

Difficulty: Medium

Note:

- two ways to become ancestor: p and q appear in children; node itself is p or q

## [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/)

Date: 0426

Category: Binary Tree

Difficulty: Medium

Note:

- assume p < q

## [Insert into a Binary Search Tree](https://leetcode.cn/problems/insert-into-a-binary-search-tree/)

Date: 0426

Category: Binary Tree

Difficulty: Medium

Note:

- three conditions

## [Delete Node in a BST](https://leetcode.cn/problems/delete-node-in-a-bst/)

Date: 0427

Category: Binary Tree

Difficulty: Medium

Note:

- if root.val > < or = key
- if root.val == key
  - not root.left
  - not root.right
  - find the most left of the right child, name p
  - put root.left to p.left(p.left must be empty at this time)
  - root.right replace root(delete)

## [Trim a Binary Search Tree](https://leetcode.cn/problems/trim-a-binary-search-tree/)

Date: 0427

Category: Binary Tree

Difficulty: Medium

Note:

- L =< root <= R: handle root.left and root.right
- root < L: handle root.right
- root > R: handle root.left

## [Convert Sorted Array to Binary Search Tree](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/)

Date: 0429

Category: Binary Tree

Difficulty: Medium

Note:

- find mid and create left and right node

## [Convert BST to Greater Tree](https://leetcode.cn/problems/convert-bst-to-greater-tree/)

Date: 0429

Category: Binary Tree

Difficulty: Medium

Note:

- reverse inorder traversal

## [Combinations](https://leetcode.cn/problems/combinations/)

Date: 0430

Category: BackTracking

Difficulty: Medium

Note:

- how to trim
- res.append(path[:])

## [Combination Sum III](https://leetcode.cn/problems/combination-sum-iii/)

Date: 0503

Category: BackTracking

Difficulty: Medium

Note:

- if condition
- res.append(path[:])

## [Letter Combinations of a Phone Number](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/)

Date: 0509

Category: BackTracking

Difficulty: Medium

Note:

- letter map

## [Combination Sum](https://leetcode.cn/problems/combination-sum/)

Date: 0510

Category: BackTracking

Difficulty: Medium

Note:

- candidates can be used for multiple times
