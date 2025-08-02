# Problem: Recover Swapped Nodes in a Binary Search Tree (BST)

Two elements of a Binary Search Tree (BST), represented by its root node **A**, are swapped by mistake. Your task is to identify the **two values** that were swapped. When these two values are swapped back, the BST will be restored to its correct form.

A solution using **O(n)** space (e.g., using in-order traversal and storing the elements in an array) is straightforward. However, can you devise a solution that works in **constant space (O(1))**?

### Input:

* The first and only argument is the **root node A** of the binary search tree.

### Output:

* Return a list of **two integers**, the values of the swapped nodes, in **ascending order**.

### Constraints:

* Assume the BST contains **unique elements**.
* The input tree will have **at least two nodes**.

### Example:

**Input Tree (in-order before fix):**

```
   1
    \
     3
    /
   2
```

**Output:**

```
[1, 2]
```

**Explanation:**
Nodes with values 1 and 2 are swapped. Swapping them restores the BST.

---

Use **Morris Traversal** or similar techniques to solve this problem in **O(1) space**, if possible.

---

Thanks for the clarification.

You're referring to the following **binary tree** structure:

```
    1
   / \
  2   3
```

This is **not** a valid Binary Search Tree (BST) because:

* In a BST, the **left child** should be **less than the root**.
* Here, `2` is on the left of `1`, but `2 > 1` — so it violates BST property.

If **2 and 1 were mistakenly swapped**, the **correct BST** should be:

```
    2
   / \
  1   3
```

In this correct version:

* Left child `1 < 2`
* Right child `3 > 2`

---

### ✅ Therefore, the nodes that were swapped are: `[1, 2]`

But as per your example, the output is `[2, 1]`.
However, the **problem requires the output to be in ascending order**, so:

### ✅ Final Output: `[1, 2]`

---

Here's another example:

You're referring to the following **binary tree** structure:

```
    2
   / \
  3   1
```

This is **not** a valid Binary Search Tree (BST) because:

* Left child `3 > 2` — violates the BST rule
* Right child `1 < 2` — also violates the BST rule

If **3 and 1 were mistakenly swapped**, the correct BST would be:

```
    2
   / \
  1   3
```

In this corrected version:

* Left child `1 < 2`
* Right child `3 > 2`

---

### ✅ Therefore, the nodes that were swapped are: `[1, 3]`

If the output provided is `[3, 1]`, the problem still requires the answer in **ascending order**, so:

### ✅ Final Output: `[1, 3]`
