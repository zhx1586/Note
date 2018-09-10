# 树和图

- 分而治之（Divide and Conquer）

  - 思想：将 problem 分解为 subproblem，解决 subproblem 从而解决 problem。
  - 实例：
    - 归并排序（Merge Sort）：divide 简单、conquer 复杂。
    - 快速排序（Quick Sort）：divide 复杂、conquer 简单。
  - 与深度优先搜索（DFS）的关系：
    - 深度优先搜索：搜索特定路径类的问题。
    - 分而治之：不强调路径，比如判断一个二叉树是否是二叉搜索树。
  - 树的实现（使用分而治之的思想来理解）
    - 有时不必实现 `Tree` 这个类，而是仅实现 `TreeNode` 这个类，因为已知根节点即可获得整个树中的所有信息。
    - 单个树节点`TreeNode` 既可以代表该节点本身，也可以代表以该节点为根节点的整个子树。
  - 图的实现（使用分而治之的思想来理解）
    - 对于连通图，已知单个图节点也可以获得整个图中的所有信息。

- 边界条件的判定

  - 两种边界条件：
    - 合法节点（invalid node） `if (node) {}`
    - 最终节点（end node）`if (node->next) {}` 
  - 在深度优先搜索和回溯时应当区分这两种边界。
    - 往往判断是否是最终节点更具有普适性。

- 堆（heap）

  - 堆（heap）是一种数据结构（Data Structure），而优先级队列（Priority Queue）是一个抽象数据类型（Abstract Data Type，ADT）。

- 不要在DFS函数中调用DFS函数

  - 实例：判断一个二叉树是否平衡。
  - 错误思路：
    - 判断左子树是否平衡。
    - 判断右子树是否平衡。
    - 判断左右子树的高度差是否小于 $1$ 。
  - 错误原因：
    - 计算高度和判断是否平衡都是 DFS 函数，会存在重复计算。
  - 改正：
    - 在 DFS 函数中返回更多信息（比如：高度）。 

- 前缀树（Trie / Prefix Tree）

- 图的实现方式（空间复杂度 $O(|V|+|E|)$）

  - 邻接矩阵实现：适合密集图。
  - 邻接表实现：适合稀疏图。（但是链表实现时空间上有额外的开销）

- 树相关算法

  - 由`subtree` 或者 `subgraph` 推知整个 `tree` 或者 `graph` 的相关属性（分而治之）。

    - 判断树是否为二叉树、二叉搜索树、平衡二叉树、其它树的子树等。
    - 判断图是否为有环图等。

  - 寻找特定条件的 `path` 。

    - 思路：深度优先搜索、回溯（每次只关注当前路径，直至走不通为止，再去考虑其它路径）。

    - 深度优先搜索模板

      ```c++
      void DFS(P node, vector<P>& path, ... ) {
        // 1. invalid
        if (!node)
          return ;
        // 2. success
        if (__) {
          path.push_back(node);
        }
        // 3. child nodes
        DFS(left, path, ...);
        DFS(right, path, ...);
        // 4. clean the influence of the current node
        path.pop_back();
      }
      ```

  - 将树转化为其他数据结构

    - 按照广度优先遍历（BFS）顺序输出分层结构。

  - 寻找满足条件的节点

    - 寻找中序遍历的下一个节点。

- 图相关算法

  - 图遍历算法
    - 深度优先搜索（DFS）。
    - 广度优先搜索（BFS）。
    - Dijkstra算法（最短路径问题）。
      - 在边没有权重时退化为广度优先搜索。
  - 建图问题
    - 邻接矩阵（matrix）。
    - 邻接表（linked list）。