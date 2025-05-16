**Priority queue -> see course implementation**

## Binary Search Tree

**Tree**: collection of nodes.
    -> Hierarchical structure (model).
    -> Edges to catch relations between nodes (direct relations).
    -> Root -> it does not have a parent.
            -> only one root in the tree.
**Nodes**: we can store data to be processed later.

**Binary**: MAX 2 subtrees.

**Search**: Ordering rules.

**Ordering rules**: Key LS < Key.
                    Key RS > Key.

**Steps:**
* 1.Search the place to insert the desired node:
    * if we find NULL that means we found the place to insert:
        * Allocate & Glue the node to the BST.
            * new node will be a leaf (Left and Right will be NULL).
    * if we find a node with the same value:
        * we stop the allocation because we can't have two keys with same value.