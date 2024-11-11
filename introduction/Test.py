import sys


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def delete_node(root, key):
    # 如果根节点为空，直接返回
    if not root:
        return root

    # 如果 key 小于当前节点的值，继续在左子树中删除
    if key < root.value:
        root.left = delete_node(root.left, key)

    # 如果 key 大于当前节点的值，继续在右子树中删除
    elif key > root.value:
        root.right = delete_node(root.right, key)

    # 找到要删除的节点
    else:
        # 情况 1: 没有子节点（叶子节点）
        if not root.left and not root.right:
            return None

        # 情况 2: 只有一个子节点
        elif not root.left:
            return root.right  # 只有右子节点
        elif not root.right:
            return root.left  # 只有左子节点

        # 情况 3: 有两个子节点
        else:
            # 找到中序后继（右子树中最小的节点）
            successor = find_min(root.right)
            # 用中序后继的值替换当前节点的值
            root.value = successor.value
            # 删除右子树中的中序后继节点
            root.right = delete_node(root.right, successor.value)

    return root


# 找到最小值的节点（即中序后继）
def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


# 构建一个简单的 BST
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

# 删除节点 50
root = delete_node(root, 50)


# print(root.value)
# print(root.left.value)
# print(root.right.value)
# print(root.left.left.value)
# print(root.left.right.value)
# print(root.right.left.value)


# 打印删除后的树结构
def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.value, end=" ")
        inorder_traversal(node.right)


inorder_traversal(root)


def networkDelayTime(times, n, k):
    """
    :type times: List[List[int]]
    :type n: int
    :type k: int
    :rtype: int
    """
    arr = [i for i in range(1, n + 1)]
    arr_dict = dict()
    arr_set = set(arr)
    for i in arr:
        if i == k:
            arr_dict[i] = 0
        else:
            arr_dict[i] = sys.maxsize
    exists = False
    while arr_set:
        # find the smallest node in arr_dict
        # [1:infinity,2:0,3:infinity,4:infinity]
        min_node_key = None
        for element in arr_set:
            if min_node_key is None:
                min_node_key = element
                continue
            if arr_dict[min_node_key] > arr_dict[element]:
                min_node_key = element
        arr_set.remove(min_node_key)

        for time_list in times:
            if time_list[0] == min_node_key:
                new_times = arr_dict[min_node_key] + time_list[2]
                if arr_dict[time_list[1]] > new_times:
                    arr_dict[time_list[1]] = new_times
                    exists = True

    max_time = max(arr_dict.values())
    return max_time if max_time < sys.maxsize else -1

times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2

# print(networkDelayTime(times,n,k))
times =[[1,2,1],[2,3,2],[1,3,1]]
n = 3
k = 2
print(networkDelayTime(times, n, k))
