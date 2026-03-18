---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/kernel/data_structures/dlist.html
original_path: kernel/data_structures/dlist.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Double-linked List

Similar to the single-linked list in many respects, Zephyr includes a
double-linked implementation. This provides the same algorithmic
behavior for all the existing slist operations, but also allows for
constant-time removal and insertion (at all points: before or after
the head, tail or any internal node). To do this, the list stores two
pointers per node, and thus has somewhat higher runtime code and
memory space needs.

A [`sys_dlist_t`](#c.sys_dlist_t) struct may be instantiated by the user in any
accessible memory. It must be initialized with [`sys_dlist_init()`](#c.sys_dlist_init)
or [`SYS_DLIST_STATIC_INIT`](#c.SYS_DLIST_STATIC_INIT) before use. The [`sys_dnode_t`](#c.sys_dnode_t) struct
is expected to be provided by the user for any nodes added to the
list (typically embedded within the struct to be tracked, as described
above). It must be initialized in zeroed/bss memory or with
[`sys_dnode_init()`](#c.sys_dnode_init) before use.

Primitive operations may retrieve the head/tail of a list and the
next/prev pointers of a node with [`sys_dlist_peek_head()`](#c.sys_dlist_peek_head),
[`sys_dlist_peek_tail()`](#c.sys_dlist_peek_tail), [`sys_dlist_peek_next()`](#c.sys_dlist_peek_next) and
[`sys_dlist_peek_prev()`](#c.sys_dlist_peek_prev). These can all return NULL where
appropriate (i.e. for empty lists, or nodes at the endpoints of the
list).

A dlist can be modified in constant time by removing a node with
[`sys_dlist_remove()`](#c.sys_dlist_remove), by adding a node to the head or tail of a list
with [`sys_dlist_prepend()`](#c.sys_dlist_prepend) and [`sys_dlist_append()`](#c.sys_dlist_append), or by
inserting a node before an existing node with [`sys_dlist_insert()`](#c.sys_dlist_insert).

As for slist, each node in a dlist can be processed in a natural code
block style using [`SYS_DLIST_FOR_EACH_NODE`](#c.SYS_DLIST_FOR_EACH_NODE). This macro also
exists in a “FROM\_NODE” form which allows for iterating from a known
starting point, a “SAFE” variant that allows for removing the node
being inspected within the code block, a “CONTAINER” style that
provides the pointer to a containing struct instead of the raw node,
and a “CONTAINER\_SAFE” variant that provides both properties.

Convenience utilities provided by dlist include
[`sys_dlist_insert_at()`](#c.sys_dlist_insert_at), which inserts a node that linearly searches
through a list to find the right insertion point, which is provided by
the user as a C callback function pointer, and
[`sys_dnode_is_linked()`](#c.sys_dnode_is_linked), which will affirmatively return whether or
not a node is currently linked into a dlist or not (via an
implementation that has zero overhead vs. the normal list processing).

## Double-linked List Internals

Internally, the dlist implementation is minimal: the [`sys_dlist_t`](#c.sys_dlist_t)
struct contains “head” and “tail” pointer fields, the [`sys_dnode_t`](#c.sys_dnode_t)
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

*group* Doubly-linked list
:   Doubly-linked list implementation.

    Doubly-linked list implementation using inline macros/functions. This API is not thread safe, and thus if a list is used across threads, calls to functions must be protected with synchronization primitives.

    The lists are expected to be initialized such that both the head and tail pointers point to the list itself. Initializing the lists in such a fashion simplifies the adding and removing of nodes to/from the list.

    Defines

    SYS\_DLIST\_FOR\_EACH\_NODE(\_\_dl, \_\_dn)
    :   Provide the primitive to iterate on a list Note: the loop is unsafe and thus \_\_dn should not be removed.

        User *MUST* add the loop statement curly braces enclosing its own code:

        ```text
        SYS_DLIST_FOR_EACH_NODE(l, n) {
            <user code>
        }
        ```

        This and other SYS\_DLIST\_\*() macros are not thread safe.

        Parameters:
        :   - **\_\_dl** – A pointer on a [sys\_dlist\_t](#group__doubly-linked-list__apis_1gaa03f9557215b486fee1039dd4c07e683) to iterate on
            - **\_\_dn** – A [sys\_dnode\_t](#group__doubly-linked-list__apis_1ga57fdb936802a617d16c00ab08cd2ad98) pointer to peek each node of the list

    SYS\_DLIST\_ITERATE\_FROM\_NODE(\_\_dl, \_\_dn)
    :   Provide the primitive to iterate on a list, from a node in the list Note: the loop is unsafe and thus \_\_dn should not be removed.

        User *MUST* add the loop statement curly braces enclosing its own code:

        ```text
        SYS_DLIST_ITERATE_FROM_NODE(l, n) {
            <user code>
        }
        ```

        Like [SYS\_DLIST\_FOR\_EACH\_NODE()](#group__doubly-linked-list__apis_1ga3788b5bbd11acc885e7378800a8cf974), but \_\_dn already contains a node in the list where to start searching for the next entry from. If NULL, it starts from the head.

        This and other SYS\_DLIST\_\*() macros are not thread safe.

        Parameters:
        :   - **\_\_dl** – A pointer on a [sys\_dlist\_t](#group__doubly-linked-list__apis_1gaa03f9557215b486fee1039dd4c07e683) to iterate on
            - **\_\_dn** – A [sys\_dnode\_t](#group__doubly-linked-list__apis_1ga57fdb936802a617d16c00ab08cd2ad98) pointer to peek each node of the list; it contains the starting node, or NULL to start from the head

    SYS\_DLIST\_FOR\_EACH\_NODE\_SAFE(\_\_dl, \_\_dn, \_\_dns)
    :   Provide the primitive to safely iterate on a list Note: \_\_dn can be removed, it will not break the loop.

        User *MUST* add the loop statement curly braces enclosing its own code:

        ```text
        SYS_DLIST_FOR_EACH_NODE_SAFE(l, n, s) {
            <user code>
        }
        ```

        This and other SYS\_DLIST\_\*() macros are not thread safe.

        Parameters:
        :   - **\_\_dl** – A pointer on a [sys\_dlist\_t](#group__doubly-linked-list__apis_1gaa03f9557215b486fee1039dd4c07e683) to iterate on
            - **\_\_dn** – A [sys\_dnode\_t](#group__doubly-linked-list__apis_1ga57fdb936802a617d16c00ab08cd2ad98) pointer to peek each node of the list
            - **\_\_dns** – A [sys\_dnode\_t](#group__doubly-linked-list__apis_1ga57fdb936802a617d16c00ab08cd2ad98) pointer for the loop to run safely

    SYS\_DLIST\_CONTAINER(\_\_dn, \_\_cn, \_\_n)
    :   Provide the primitive to resolve the container of a list node Note: it is safe to use with NULL pointer nodes.

        Parameters:
        :   - **\_\_dn** – A pointer on a [sys\_dnode\_t](#group__doubly-linked-list__apis_1ga57fdb936802a617d16c00ab08cd2ad98) to get its container
            - **\_\_cn** – Container struct type pointer
            - **\_\_n** – The field name of [sys\_dnode\_t](#group__doubly-linked-list__apis_1ga57fdb936802a617d16c00ab08cd2ad98) within the container struct

    SYS\_DLIST\_PEEK\_HEAD\_CONTAINER(\_\_dl, \_\_cn, \_\_n)
    :   Provide the primitive to peek container of the list head.

        Parameters:
        :   - **\_\_dl** – A pointer on a [sys\_dlist\_t](#group__doubly-linked-list__apis_1gaa03f9557215b486fee1039dd4c07e683) to peek
            - **\_\_cn** – Container struct type pointer
            - **\_\_n** – The field name of [sys\_dnode\_t](#group__doubly-linked-list__apis_1ga57fdb936802a617d16c00ab08cd2ad98) within the container struct

    SYS\_DLIST\_PEEK\_NEXT\_CONTAINER(\_\_dl, \_\_cn, \_\_n)
    :   Provide the primitive to peek the next container.

        Parameters:
        :   - **\_\_dl** – A pointer on a [sys\_dlist\_t](#group__doubly-linked-list__apis_1gaa03f9557215b486fee1039dd4c07e683) to peek
            - **\_\_cn** – Container struct type pointer
            - **\_\_n** – The field name of [sys\_dnode\_t](#group__doubly-linked-list__apis_1ga57fdb936802a617d16c00ab08cd2ad98) within the container struct

    SYS\_DLIST\_FOR\_EACH\_CONTAINER(\_\_dl, \_\_cn, \_\_n)
    :   Provide the primitive to iterate on a list under a container Note: the loop is unsafe and thus \_\_cn should not be detached.

        User *MUST* add the loop statement curly braces enclosing its own code:

        ```text
        SYS_DLIST_FOR_EACH_CONTAINER(l, c, n) {
            <user code>
        }
        ```

        Parameters:
        :   - **\_\_dl** – A pointer on a [sys\_dlist\_t](#group__doubly-linked-list__apis_1gaa03f9557215b486fee1039dd4c07e683) to iterate on
            - **\_\_cn** – A container struct type pointer to peek each entry of the list
            - **\_\_n** – The field name of [sys\_dnode\_t](#group__doubly-linked-list__apis_1ga57fdb936802a617d16c00ab08cd2ad98) within the container struct

    SYS\_DLIST\_FOR\_EACH\_CONTAINER\_SAFE(\_\_dl, \_\_cn, \_\_cns, \_\_n)
    :   Provide the primitive to safely iterate on a list under a container Note: \_\_cn can be detached, it will not break the loop.

        User *MUST* add the loop statement curly braces enclosing its own code:

        ```text
        SYS_DLIST_FOR_EACH_CONTAINER_SAFE(l, c, cn, n) {
            <user code>
        }
        ```

        Parameters:
        :   - **\_\_dl** – A pointer on a [sys\_dlist\_t](#group__doubly-linked-list__apis_1gaa03f9557215b486fee1039dd4c07e683) to iterate on
            - **\_\_cn** – A container struct type pointer to peek each entry of the list
            - **\_\_cns** – A container struct type pointer for the loop to run safely
            - **\_\_n** – The field name of [sys\_dnode\_t](#group__doubly-linked-list__apis_1ga57fdb936802a617d16c00ab08cd2ad98) within the container struct

    SYS\_DLIST\_STATIC\_INIT(ptr\_to\_list)
    :   Static initializer for a doubly-linked list.

    Typedefs

    typedef struct \_dnode sys\_dlist\_t
    :   Doubly-linked list structure.

    typedef struct \_dnode sys\_dnode\_t
    :   Doubly-linked list node structure.

    Functions

    static inline void sys\_dlist\_init([sys\_dlist\_t](#c.sys_dlist_t) \*list)
    :   initialize list to its empty state

        Parameters:
        :   - **list** – the doubly-linked list

    static inline void sys\_dnode\_init([sys\_dnode\_t](#c.sys_dnode_t) \*node)
    :   initialize node to its state when not in a list

        Parameters:
        :   - **node** – the node

    static inline bool sys\_dnode\_is\_linked(const [sys\_dnode\_t](#c.sys_dnode_t) \*node)
    :   check if a node is a member of any list

        Parameters:
        :   - **node** – the node

        Returns:
        :   true if node is linked into a list, false if it is not

    static inline bool sys\_dlist\_is\_head([sys\_dlist\_t](#c.sys_dlist_t) \*list, [sys\_dnode\_t](#c.sys_dnode_t) \*node)
    :   check if a node is the list’s head

        Parameters:
        :   - **list** – the doubly-linked list to operate on
            - **node** – the node to check

        Returns:
        :   true if node is the head, false otherwise

    static inline bool sys\_dlist\_is\_tail([sys\_dlist\_t](#c.sys_dlist_t) \*list, [sys\_dnode\_t](#c.sys_dnode_t) \*node)
    :   check if a node is the list’s tail

        Parameters:
        :   - **list** – the doubly-linked list to operate on
            - **node** – the node to check

        Returns:
        :   true if node is the tail, false otherwise

    static inline bool sys\_dlist\_is\_empty([sys\_dlist\_t](#c.sys_dlist_t) \*list)
    :   check if the list is empty

        Parameters:
        :   - **list** – the doubly-linked list to operate on

        Returns:
        :   true if empty, false otherwise

    static inline bool sys\_dlist\_has\_multiple\_nodes([sys\_dlist\_t](#c.sys_dlist_t) \*list)
    :   check if more than one node present

        This and other sys\_dlist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – the doubly-linked list to operate on

        Returns:
        :   true if multiple nodes, false otherwise

    static inline [sys\_dnode\_t](#c.sys_dnode_t) \*sys\_dlist\_peek\_head([sys\_dlist\_t](#c.sys_dlist_t) \*list)
    :   get a reference to the head item in the list

        Parameters:
        :   - **list** – the doubly-linked list to operate on

        Returns:
        :   a pointer to the head element, NULL if list is empty

    static inline [sys\_dnode\_t](#c.sys_dnode_t) \*sys\_dlist\_peek\_head\_not\_empty([sys\_dlist\_t](#c.sys_dlist_t) \*list)
    :   get a reference to the head item in the list

        The list must be known to be non-empty.

        Parameters:
        :   - **list** – the doubly-linked list to operate on

        Returns:
        :   a pointer to the head element

    static inline [sys\_dnode\_t](#c.sys_dnode_t) \*sys\_dlist\_peek\_next\_no\_check([sys\_dlist\_t](#c.sys_dlist_t) \*list, [sys\_dnode\_t](#c.sys_dnode_t) \*node)
    :   get a reference to the next item in the list, node is not NULL

        Faster than [sys\_dlist\_peek\_next()](#group__doubly-linked-list__apis_1ga76366019520dc4c2ce2735cf747c1a22) if node is known not to be NULL.

        Parameters:
        :   - **list** – the doubly-linked list to operate on
            - **node** – the node from which to get the next element in the list

        Returns:
        :   a pointer to the next element from a node, NULL if node is the tail

    static inline [sys\_dnode\_t](#c.sys_dnode_t) \*sys\_dlist\_peek\_next([sys\_dlist\_t](#c.sys_dlist_t) \*list, [sys\_dnode\_t](#c.sys_dnode_t) \*node)
    :   get a reference to the next item in the list

        Parameters:
        :   - **list** – the doubly-linked list to operate on
            - **node** – the node from which to get the next element in the list

        Returns:
        :   a pointer to the next element from a node, NULL if node is the tail or NULL (when node comes from reading the head of an empty list).

    static inline [sys\_dnode\_t](#c.sys_dnode_t) \*sys\_dlist\_peek\_prev\_no\_check([sys\_dlist\_t](#c.sys_dlist_t) \*list, [sys\_dnode\_t](#c.sys_dnode_t) \*node)
    :   get a reference to the previous item in the list, node is not NULL

        Faster than [sys\_dlist\_peek\_prev()](#group__doubly-linked-list__apis_1ga23b9f6a10a14c08ccf1fbb7d8518fc43) if node is known not to be NULL.

        Parameters:
        :   - **list** – the doubly-linked list to operate on
            - **node** – the node from which to get the previous element in the list

        Returns:
        :   a pointer to the previous element from a node, NULL if node is the tail

    static inline [sys\_dnode\_t](#c.sys_dnode_t) \*sys\_dlist\_peek\_prev([sys\_dlist\_t](#c.sys_dlist_t) \*list, [sys\_dnode\_t](#c.sys_dnode_t) \*node)
    :   get a reference to the previous item in the list

        Parameters:
        :   - **list** – the doubly-linked list to operate on
            - **node** – the node from which to get the previous element in the list

        Returns:
        :   a pointer to the previous element from a node, NULL if node is the tail or NULL (when node comes from reading the head of an empty list).

    static inline [sys\_dnode\_t](#c.sys_dnode_t) \*sys\_dlist\_peek\_tail([sys\_dlist\_t](#c.sys_dlist_t) \*list)
    :   get a reference to the tail item in the list

        Parameters:
        :   - **list** – the doubly-linked list to operate on

        Returns:
        :   a pointer to the tail element, NULL if list is empty

    static inline void sys\_dlist\_append([sys\_dlist\_t](#c.sys_dlist_t) \*list, [sys\_dnode\_t](#c.sys_dnode_t) \*node)
    :   add node to tail of list

        This and other sys\_dlist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – the doubly-linked list to operate on
            - **node** – the element to append

    static inline void sys\_dlist\_prepend([sys\_dlist\_t](#c.sys_dlist_t) \*list, [sys\_dnode\_t](#c.sys_dnode_t) \*node)
    :   add node to head of list

        This and other sys\_dlist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – the doubly-linked list to operate on
            - **node** – the element to append

    static inline void sys\_dlist\_insert([sys\_dnode\_t](#c.sys_dnode_t) \*successor, [sys\_dnode\_t](#c.sys_dnode_t) \*node)
    :   Insert a node into a list.

        Insert a node before a specified node in a dlist.

        Parameters:
        :   - **successor** – the position before which “node” will be inserted
            - **node** – the element to insert

    static inline void sys\_dlist\_insert\_at([sys\_dlist\_t](#c.sys_dlist_t) \*list, [sys\_dnode\_t](#c.sys_dnode_t) \*node, int (\*cond)([sys\_dnode\_t](#c.sys_dnode_t) \*node, void \*data), void \*data)
    :   insert node at position

        Insert a node in a location depending on a external condition. The cond() function checks if the node is to be inserted *before* the current node against which it is checked. This and other sys\_dlist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – the doubly-linked list to operate on
            - **node** – the element to insert
            - **cond** – a function that determines if the current node is the correct insert point
            - **data** – parameter to cond()

    static inline void sys\_dlist\_remove([sys\_dnode\_t](#c.sys_dnode_t) \*node)
    :   remove a specific node from a list

        The list is implicit from the node. The node must be part of a list. This and other sys\_dlist\_\*() functions are not thread safe.

        Parameters:
        :   - **node** – the node to remove

    static inline [sys\_dnode\_t](#c.sys_dnode_t) \*sys\_dlist\_get([sys\_dlist\_t](#c.sys_dlist_t) \*list)
    :   get the first node in a list

        This and other sys\_dlist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – the doubly-linked list to operate on

        Returns:
        :   the first node in the list, NULL if list is empty

    static inline size\_t sys\_dlist\_len([sys\_dlist\_t](#c.sys_dlist_t) \*list)
    :   Compute the size of the given list in O(n) time.

        Parameters:
        :   - **list** – A pointer on the list

        Returns:
        :   an integer equal to the size of the list, or 0 if empty
