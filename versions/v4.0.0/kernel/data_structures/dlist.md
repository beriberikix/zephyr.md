---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/kernel/data_structures/dlist.html
original_path: kernel/data_structures/dlist.html
---

# Double-linked List

Similar to the single-linked list in many respects, Zephyr includes a
double-linked implementation. This provides the same algorithmic
behavior for all the existing slist operations, but also allows for
constant-time removal and insertion (at all points: before or after
the head, tail or any internal node). To do this, the list stores two
pointers per node, and thus has somewhat higher runtime code and
memory space needs.

A [`sys_dlist_t`](../../doxygen/html/group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683) struct may be instantiated by the user in any
accessible memory. It must be initialized with [`sys_dlist_init()`](../../doxygen/html/group__doubly-linked-list__apis.md#gaf05dbc7d7250990b971796300aaf6c53)
or [`SYS_DLIST_STATIC_INIT`](../../doxygen/html/group__doubly-linked-list__apis.md#ga3681d4600f9cbd9237ea9ce6f67e508d) before use. The [`sys_dnode_t`](../../doxygen/html/group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98) struct
is expected to be provided by the user for any nodes added to the
list (typically embedded within the struct to be tracked, as described
above). It must be initialized in zeroed/bss memory or with
[`sys_dnode_init()`](../../doxygen/html/group__doubly-linked-list__apis.md#gadf15b39af330221921d24505280e7a32) before use.

Primitive operations may retrieve the head/tail of a list and the
next/prev pointers of a node with [`sys_dlist_peek_head()`](../../doxygen/html/group__doubly-linked-list__apis.md#ga6fc11e4682311b6b368d849e1e421183),
[`sys_dlist_peek_tail()`](../../doxygen/html/group__doubly-linked-list__apis.md#gac84d0d3aade5677f7840f51f3c65c095), [`sys_dlist_peek_next()`](../../doxygen/html/group__doubly-linked-list__apis.md#ga76366019520dc4c2ce2735cf747c1a22) and
[`sys_dlist_peek_prev()`](../../doxygen/html/group__doubly-linked-list__apis.md#ga23b9f6a10a14c08ccf1fbb7d8518fc43). These can all return NULL where
appropriate (i.e. for empty lists, or nodes at the endpoints of the
list).

A dlist can be modified in constant time by removing a node with
[`sys_dlist_remove()`](../../doxygen/html/group__doubly-linked-list__apis.md#ga06f88befada25820fba01d2019970e4e), by adding a node to the head or tail of a list
with [`sys_dlist_prepend()`](../../doxygen/html/group__doubly-linked-list__apis.md#ga6f21ba50e0de93f54bfefeaabe0c767f) and [`sys_dlist_append()`](../../doxygen/html/group__doubly-linked-list__apis.md#ga119cb342faf37cd4e97e6361c7ecabe3), or by
inserting a node before an existing node with [`sys_dlist_insert()`](../../doxygen/html/group__doubly-linked-list__apis.md#ga94987670c6afd5eabeb9957bb065a071).

As for slist, each node in a dlist can be processed in a natural code
block style using [`SYS_DLIST_FOR_EACH_NODE`](../../doxygen/html/group__doubly-linked-list__apis.md#ga3788b5bbd11acc885e7378800a8cf974). This macro also
exists in a “FROM\_NODE” form which allows for iterating from a known
starting point, a “SAFE” variant that allows for removing the node
being inspected within the code block, a “CONTAINER” style that
provides the pointer to a containing struct instead of the raw node,
and a “CONTAINER\_SAFE” variant that provides both properties.

Convenience utilities provided by dlist include
[`sys_dlist_insert_at()`](../../doxygen/html/group__doubly-linked-list__apis.md#ga667cee0bdd59d8ca3fc82a5bca2bcd48), which inserts a node that linearly searches
through a list to find the right insertion point, which is provided by
the user as a C callback function pointer, and
[`sys_dnode_is_linked()`](../../doxygen/html/group__doubly-linked-list__apis.md#gac725da0c7e65c126a96a9405af84ca41), which will affirmatively return whether or
not a node is currently linked into a dlist or not (via an
implementation that has zero overhead vs. the normal list processing).

## Double-linked List Internals

Internally, the dlist implementation is minimal: the [`sys_dlist_t`](../../doxygen/html/group__doubly-linked-list__apis.md#gaa03f9557215b486fee1039dd4c07e683)
struct contains “head” and “tail” pointer fields, the [`sys_dnode_t`](../../doxygen/html/group__doubly-linked-list__apis.md#ga57fdb936802a617d16c00ab08cd2ad98)
contains “prev” and “next” pointers, and no other data is stored. But
in practice the two structs are internally identical, and the list
struct is inserted as a node into the list itself. This allows for a
very clean symmetry of operations:

- An empty list has backpointers to itself in the list struct, which
  can be trivially detected.
- The head and tail of the list can be detected by comparing the
  prev/next pointers of a node vs. the list struct address.
- An insertion or deletion never needs to check for the special case
  of inserting at the head or tail. There are never any NULL pointers
  within the list to be avoided. Exactly the same operations are run,
  without tests or branches, for all list modification primitives.

Effectively, a dlist of N nodes can be thought of as a “ring” of “N+1”
nodes, where one node represents the list tracking struct.

![dlist example](../../_images/dlist.png)

A dlist containing three elements. Note that the list struct
appears as a fourth “element” in the list.

![single-element dlist example](../../_images/dlist-single.png)

An dlist containing just one element.

![dlist example](../../_images/dlist-empty.png)

An empty dlist.

## Doubly-linked List API Reference

[Doubly-linked list](../../doxygen/html/group__doubly-linked-list__apis.md)
