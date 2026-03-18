---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/kernel/data_structures/slist.html
original_path: kernel/data_structures/slist.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Single-linked List

Zephyr provides a [`sys_slist_t`](#c.sys_slist_t) type for storing simple
singly-linked list data (i.e. data where each list element stores a
pointer to the next element, but not the previous one). This supports
constant-time access to the first (head) and last (tail) elements of
the list, insertion before the head and after the tail of the list and
constant time removal of the head. Removal of subsequent nodes
requires access to the “previous” pointer and thus can only be
performed in linear time by searching the list.

The [`sys_slist_t`](#c.sys_slist_t) struct may be instantiated by the user in any
accessible memory. It should be initialized with either
[`sys_slist_init()`](#c.sys_slist_init) or by static assignment from SYS\_SLIST\_STATIC\_INIT
before use. Its interior fields are opaque and should not be accessed
by user code.

The end nodes of a list may be retrieved with
[`sys_slist_peek_head()`](#c.sys_slist_peek_head) and [`sys_slist_peek_tail()`](#c.sys_slist_peek_tail), which will
return NULL if the list is empty, otherwise a pointer to a
[`sys_snode_t`](#c.sys_snode_t) struct.

The [`sys_snode_t`](#c.sys_snode_t) struct represents the data to be inserted. In
general, it is expected to be allocated/controlled by the user,
usually embedded within a struct which is to be added to the list.
The container struct pointer may be retrieved from a list node using
[`SYS_SLIST_CONTAINER`](#c.SYS_SLIST_CONTAINER), passing it the struct name of the
containing struct and the field name of the node. Internally, the
[`sys_snode_t`](#c.sys_snode_t) struct contains only a next pointer, which may be
accessed with [`sys_slist_peek_next()`](#c.sys_slist_peek_next).

Lists may be modified by adding a single node at the head or tail with
[`sys_slist_prepend()`](#c.sys_slist_prepend) and [`sys_slist_append()`](#c.sys_slist_append). They may also
have a node added to an interior point with [`sys_slist_insert()`](#c.sys_slist_insert),
which inserts a new node after an existing one. Similarly
[`sys_slist_remove()`](#c.sys_slist_remove) will remove a node given a pointer to its
predecessor. These operations are all constant time.

Convenience routines exist for more complicated modifications to a
list. [`sys_slist_merge_slist()`](#c.sys_slist_merge_slist) will append an entire list to an
existing one. [`sys_slist_append_list()`](#c.sys_slist_append_list) will append a bounded
subset of an existing list in constant time. And
[`sys_slist_find_and_remove()`](#c.sys_slist_find_and_remove) will search a list (in linear time)
for a given node and remove it if present.

Finally the slist implementation provides a set of “for each” macros
that allows for iterating over a list in a natural way without needing
to manually traverse the next pointers. [`SYS_SLIST_FOR_EACH_NODE`](#c.SYS_SLIST_FOR_EACH_NODE)
will enumerate every node in a list given a local variable to store
the node pointer. [`SYS_SLIST_FOR_EACH_NODE_SAFE`](#c.SYS_SLIST_FOR_EACH_NODE_SAFE) behaves
similarly, but has a more complicated implementation that requires an
extra scratch variable for storage and allows the user to delete the
iterated node during the iteration. Each of those macros also exists
in a “container” variant ([`SYS_SLIST_FOR_EACH_CONTAINER`](#c.SYS_SLIST_FOR_EACH_CONTAINER) and
[`SYS_SLIST_FOR_EACH_CONTAINER_SAFE`](#c.SYS_SLIST_FOR_EACH_CONTAINER_SAFE)) which assigns a local
variable of a type that matches the user’s container struct and not
the node struct, performing the required offsets internally. And
[`SYS_SLIST_ITERATE_FROM_NODE`](#c.SYS_SLIST_ITERATE_FROM_NODE) exists to allow for enumerating a
node and all its successors only, without inspecting the earlier part
of the list.

## Single-linked List Internals

The slist code is designed to be minimal and conventional.
Internally, a [`sys_slist_t`](#c.sys_slist_t) struct is nothing more than a pair of
“head” and “tail” pointer fields. And a [`sys_snode_t`](#c.sys_snode_t) stores only a
single “next” pointer.

![slist example](../../_images/slist.png)

An slist containing three elements.

![empty slist example](../../_images/slist-empty.png)

An empty slist

The specific implementation of the list code, however, is done with an
internal “Z\_GENLIST” template API which allows for extracting those
fields from arbitrary structures and emits an arbitrarily named set of
functions. This allows for implementing more complicated
single-linked list variants using the same basic primitives. The
genlist implementor is responsible for a custom implementation of the
primitive operations only: an “init” step for each struct, and a “get”
and “set” primitives for each of head, tail and next pointers on their
relevant structs. These inline functions are passed as parameters to
the genlist macro expansion.

Only one such variant, sflist, exists in Zephyr at the moment.

## Flagged List

The [`sys_sflist_t`](#c.sys_sflist_t) is implemented using the described genlist
template API. With the exception of symbol naming (“sflist” instead
of “slist”) and the additional API described next, it operates in all
ways identically to the slist API.

It adds the ability to associate exactly two bits of user defined
“flags” with each list node. These can be accessed and modified with
[`sys_sfnode_flags_get()`](#c.sys_sfnode_flags_get) and [`sys_sfnode_flags_set()`](#c.sys_sfnode_flags_set).
Internally, the flags are stored unioned with the bottom bits of the
next pointer and incur no SRAM storage overhead when compared with the
simpler slist code.

## Single-linked List API Reference

*group* single-linked-list\_apis
:   Single-linked list implementation.

    Single-linked list implementation using inline macros/functions. This API is not thread safe, and thus if a list is used across threads, calls to functions must be protected with synchronization primitives.

    Defines

    SYS\_SLIST\_FOR\_EACH\_NODE(\_\_sl, \_\_sn)
    :   Provide the primitive to iterate on a list Note: the loop is unsafe and thus \_\_sn should not be removed.

        User *MUST* add the loop statement curly braces enclosing its own code:

        ```text
        SYS_SLIST_FOR_EACH_NODE(l, n) {
            <user code>
        }
        ```

        This and other SYS\_SLIST\_\*() macros are not thread safe.

        Parameters:
        :   - **\_\_sl** – A pointer on a [sys\_slist\_t](#group__single-linked-list__apis_1ga44658c336b634c03938a251cdc8134f8) to iterate on
            - **\_\_sn** – A [sys\_snode\_t](#group__single-linked-list__apis_1ga69bf43aad81e3ee2d55250c59b857493) pointer to peek each node of the list

    SYS\_SLIST\_ITERATE\_FROM\_NODE(\_\_sl, \_\_sn)
    :   Provide the primitive to iterate on a list, from a node in the list Note: the loop is unsafe and thus \_\_sn should not be removed.

        User *MUST* add the loop statement curly braces enclosing its own code:

        ```text
        SYS_SLIST_ITERATE_FROM_NODE(l, n) {
            <user code>
        }
        ```

        Like [SYS\_SLIST\_FOR\_EACH\_NODE()](#group__single-linked-list__apis_1gaf32ac0f222186e497d3f6180b6c26352), but \_\_dn already contains a node in the list where to start searching for the next entry from. If NULL, it starts from the head.

        This and other SYS\_SLIST\_\*() macros are not thread safe.

        Parameters:
        :   - **\_\_sl** – A pointer on a [sys\_slist\_t](#group__single-linked-list__apis_1ga44658c336b634c03938a251cdc8134f8) to iterate on
            - **\_\_sn** – A [sys\_snode\_t](#group__single-linked-list__apis_1ga69bf43aad81e3ee2d55250c59b857493) pointer to peek each node of the list it contains the starting node, or NULL to start from the head

    SYS\_SLIST\_FOR\_EACH\_NODE\_SAFE(\_\_sl, \_\_sn, \_\_sns)
    :   Provide the primitive to safely iterate on a list Note: \_\_sn can be removed, it will not break the loop.

        User *MUST* add the loop statement curly braces enclosing its own code:

        ```text
        SYS_SLIST_FOR_EACH_NODE_SAFE(l, n, s) {
            <user code>
        }
        ```

        This and other SYS\_SLIST\_\*() macros are not thread safe.

        Parameters:
        :   - **\_\_sl** – A pointer on a [sys\_slist\_t](#group__single-linked-list__apis_1ga44658c336b634c03938a251cdc8134f8) to iterate on
            - **\_\_sn** – A [sys\_snode\_t](#group__single-linked-list__apis_1ga69bf43aad81e3ee2d55250c59b857493) pointer to peek each node of the list
            - **\_\_sns** – A [sys\_snode\_t](#group__single-linked-list__apis_1ga69bf43aad81e3ee2d55250c59b857493) pointer for the loop to run safely

    SYS\_SLIST\_CONTAINER(\_\_ln, \_\_cn, \_\_n)
    :   Provide the primitive to resolve the container of a list node Note: it is safe to use with NULL pointer nodes.

        Parameters:
        :   - **\_\_ln** – A pointer on a sys\_node\_t to get its container
            - **\_\_cn** – Container struct type pointer
            - **\_\_n** – The field name of sys\_node\_t within the container struct

    SYS\_SLIST\_PEEK\_HEAD\_CONTAINER(\_\_sl, \_\_cn, \_\_n)
    :   Provide the primitive to peek container of the list head.

        Parameters:
        :   - **\_\_sl** – A pointer on a [sys\_slist\_t](#group__single-linked-list__apis_1ga44658c336b634c03938a251cdc8134f8) to peek
            - **\_\_cn** – Container struct type pointer
            - **\_\_n** – The field name of sys\_node\_t within the container struct

    SYS\_SLIST\_PEEK\_TAIL\_CONTAINER(\_\_sl, \_\_cn, \_\_n)
    :   Provide the primitive to peek container of the list tail.

        Parameters:
        :   - **\_\_sl** – A pointer on a [sys\_slist\_t](#group__single-linked-list__apis_1ga44658c336b634c03938a251cdc8134f8) to peek
            - **\_\_cn** – Container struct type pointer
            - **\_\_n** – The field name of sys\_node\_t within the container struct

    SYS\_SLIST\_PEEK\_NEXT\_CONTAINER(\_\_cn, \_\_n)
    :   Provide the primitive to peek the next container.

        Parameters:
        :   - **\_\_cn** – Container struct type pointer
            - **\_\_n** – The field name of sys\_node\_t within the container struct

    SYS\_SLIST\_FOR\_EACH\_CONTAINER(\_\_sl, \_\_cn, \_\_n)
    :   Provide the primitive to iterate on a list under a container Note: the loop is unsafe and thus \_\_cn should not be detached.

        User *MUST* add the loop statement curly braces enclosing its own code:

        ```text
        SYS_SLIST_FOR_EACH_CONTAINER(l, c, n) {
            <user code>
        }
        ```

        Parameters:
        :   - **\_\_sl** – A pointer on a [sys\_slist\_t](#group__single-linked-list__apis_1ga44658c336b634c03938a251cdc8134f8) to iterate on
            - **\_\_cn** – A pointer to peek each entry of the list
            - **\_\_n** – The field name of sys\_node\_t within the container struct

    SYS\_SLIST\_FOR\_EACH\_CONTAINER\_SAFE(\_\_sl, \_\_cn, \_\_cns, \_\_n)
    :   Provide the primitive to safely iterate on a list under a container Note: \_\_cn can be detached, it will not break the loop.

        User *MUST* add the loop statement curly braces enclosing its own code:

        ```text
        SYS_SLIST_FOR_EACH_NODE_SAFE(l, c, cn, n) {
            <user code>
        }
        ```

        Parameters:
        :   - **\_\_sl** – A pointer on a [sys\_slist\_t](#group__single-linked-list__apis_1ga44658c336b634c03938a251cdc8134f8) to iterate on
            - **\_\_cn** – A pointer to peek each entry of the list
            - **\_\_cns** – A pointer for the loop to run safely
            - **\_\_n** – The field name of sys\_node\_t within the container struct

    SYS\_SLIST\_STATIC\_INIT(ptr\_to\_list)
    :   Statically initialize a single-linked list.

        Parameters:
        :   - **ptr\_to\_list** – A pointer on the list to initialize

    Typedefs

    typedef struct \_snode sys\_snode\_t
    :   Single-linked list node structure.

    typedef struct \_slist sys\_slist\_t
    :   Single-linked list structure.

    Functions

    static inline void sys\_slist\_init([sys\_slist\_t](#c.sys_slist_t) \*list)
    :   Initialize a list.

        Parameters:
        :   - **list** – A pointer on the list to initialize

    static inline [sys\_snode\_t](#c.sys_snode_t) \*sys\_slist\_peek\_head([sys\_slist\_t](#c.sys_slist_t) \*list)
    :   Peek the first node from the list.

        Parameters:
        :   - **list** – A point on the list to peek the first node from

        Returns:
        :   A pointer on the first node of the list (or NULL if none)

    static inline [sys\_snode\_t](#c.sys_snode_t) \*sys\_slist\_peek\_tail([sys\_slist\_t](#c.sys_slist_t) \*list)
    :   Peek the last node from the list.

        Parameters:
        :   - **list** – A point on the list to peek the last node from

        Returns:
        :   A pointer on the last node of the list (or NULL if none)

    static inline bool sys\_slist\_is\_empty([sys\_slist\_t](#c.sys_slist_t) \*list)
    :   Test if the given list is empty.

        Parameters:
        :   - **list** – A pointer on the list to test

        Returns:
        :   a boolean, true if it’s empty, false otherwise

    static inline [sys\_snode\_t](#c.sys_snode_t) \*sys\_slist\_peek\_next\_no\_check([sys\_snode\_t](#c.sys_snode_t) \*node)
    :   Peek the next node from current node, node is not NULL.

        Faster then [sys\_slist\_peek\_next()](#group__single-linked-list__apis_1ga729cbf8cafdbc34261db9274195ac5df) if node is known not to be NULL.

        Parameters:
        :   - **node** – A pointer on the node where to peek the next node

        Returns:
        :   a pointer on the next node (or NULL if none)

    static inline [sys\_snode\_t](#c.sys_snode_t) \*sys\_slist\_peek\_next([sys\_snode\_t](#c.sys_snode_t) \*node)
    :   Peek the next node from current node.

        Parameters:
        :   - **node** – A pointer on the node where to peek the next node

        Returns:
        :   a pointer on the next node (or NULL if none)

    static inline void sys\_slist\_prepend([sys\_slist\_t](#c.sys_slist_t) \*list, [sys\_snode\_t](#c.sys_snode_t) \*node)
    :   Prepend a node to the given list.

        This and other sys\_slist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – A pointer on the list to affect
            - **node** – A pointer on the node to prepend

    static inline void sys\_slist\_append([sys\_slist\_t](#c.sys_slist_t) \*list, [sys\_snode\_t](#c.sys_snode_t) \*node)
    :   Append a node to the given list.

        This and other sys\_slist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – A pointer on the list to affect
            - **node** – A pointer on the node to append

    static inline void sys\_slist\_append\_list([sys\_slist\_t](#c.sys_slist_t) \*list, void \*head, void \*tail)
    :   Append a list to the given list.

        Append a singly-linked, NULL-terminated list consisting of nodes containing the pointer to the next node as the first element of a node, to *list*. This and other sys\_slist\_\*() functions are not thread safe.

        FIXME: Why are the element parameters void \*?

        Parameters:
        :   - **list** – A pointer on the list to affect
            - **head** – A pointer to the first element of the list to append
            - **tail** – A pointer to the last element of the list to append

    static inline void sys\_slist\_merge\_slist([sys\_slist\_t](#c.sys_slist_t) \*list, [sys\_slist\_t](#c.sys_slist_t) \*list\_to\_append)
    :   merge two slists, appending the second one to the first

        When the operation is completed, the appending list is empty. This and other sys\_slist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – A pointer on the list to affect
            - **list\_to\_append** – A pointer to the list to append.

    static inline void sys\_slist\_insert([sys\_slist\_t](#c.sys_slist_t) \*list, [sys\_snode\_t](#c.sys_snode_t) \*prev, [sys\_snode\_t](#c.sys_snode_t) \*node)
    :   Insert a node to the given list.

        This and other sys\_slist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – A pointer on the list to affect
            - **prev** – A pointer on the previous node
            - **node** – A pointer on the node to insert

    static inline [sys\_snode\_t](#c.sys_snode_t) \*sys\_slist\_get\_not\_empty([sys\_slist\_t](#c.sys_slist_t) \*list)
    :   Fetch and remove the first node of the given list.

        List must be known to be non-empty. This and other sys\_slist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – A pointer on the list to affect

        Returns:
        :   A pointer to the first node of the list

    static inline [sys\_snode\_t](#c.sys_snode_t) \*sys\_slist\_get([sys\_slist\_t](#c.sys_slist_t) \*list)
    :   Fetch and remove the first node of the given list.

        This and other sys\_slist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – A pointer on the list to affect

        Returns:
        :   A pointer to the first node of the list (or NULL if empty)

    static inline void sys\_slist\_remove([sys\_slist\_t](#c.sys_slist_t) \*list, [sys\_snode\_t](#c.sys_snode_t) \*prev\_node, [sys\_snode\_t](#c.sys_snode_t) \*node)
    :   Remove a node.

        This and other sys\_slist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – A pointer on the list to affect
            - **prev\_node** – A pointer on the previous node (can be NULL, which means the node is the list’s head)
            - **node** – A pointer on the node to remove

    static inline bool sys\_slist\_find\_and\_remove([sys\_slist\_t](#c.sys_slist_t) \*list, [sys\_snode\_t](#c.sys_snode_t) \*node)
    :   Find and remove a node from a list.

        This and other sys\_slist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – A pointer on the list to affect
            - **node** – A pointer on the node to remove from the list

        Returns:
        :   true if node was removed

    static inline size\_t sys\_slist\_len([sys\_slist\_t](#c.sys_slist_t) \*list)
    :   Compute the size of the given list in O(n) time.

        Parameters:
        :   - **list** – A pointer on the list

        Returns:
        :   an integer equal to the size of the list, or 0 if empty

## Flagged List API Reference

*group* flagged-single-linked-list\_apis
:   Flagged single-linked list implementation.

    Similar to [Single-linked list](#group__single-linked-list__apis) with the added ability to define two bits of user “flags” for each node. They can be accessed and modified using the [sys\_sfnode\_flags\_get()](#group__flagged-single-linked-list__apis_1ga0e258c1faa3cbaee48c29e8f2c11132b) and [sys\_sfnode\_flags\_set()](#group__flagged-single-linked-list__apis_1ga85d82a3a5927f79a5f5655cb3405ce95) APIs.

    Flagged single-linked list implementation using inline macros/functions. This API is not thread safe, and thus if a list is used across threads, calls to functions must be protected with synchronization primitives.

    Defines

    SYS\_SFLIST\_FOR\_EACH\_NODE(\_\_sl, \_\_sn)
    :   Provide the primitive to iterate on a list Note: the loop is unsafe and thus \_\_sn should not be removed.

        User *MUST* add the loop statement curly braces enclosing its own code:

        ```text
        SYS_SFLIST_FOR_EACH_NODE(l, n) {
            <user code>
        }
        ```

        This and other SYS\_SFLIST\_\*() macros are not thread safe.

        Parameters:
        :   - **\_\_sl** – A pointer on a [sys\_sflist\_t](#group__flagged-single-linked-list__apis_1ga9e7f835170787303732c805dc7375f66) to iterate on
            - **\_\_sn** – A [sys\_sfnode\_t](#group__flagged-single-linked-list__apis_1ga02dabbe35036cbc11fbbefa99a129cc7) pointer to peek each node of the list

    SYS\_SFLIST\_ITERATE\_FROM\_NODE(\_\_sl, \_\_sn)
    :   Provide the primitive to iterate on a list, from a node in the list Note: the loop is unsafe and thus \_\_sn should not be removed.

        User *MUST* add the loop statement curly braces enclosing its own code:

        ```text
        SYS_SFLIST_ITERATE_FROM_NODE(l, n) {
            <user code>
        }
        ```

        Like [SYS\_SFLIST\_FOR\_EACH\_NODE()](#group__flagged-single-linked-list__apis_1gaa3e9a3eeef7ecca012b0926fb2758c01), but \_\_dn already contains a node in the list where to start searching for the next entry from. If NULL, it starts from the head.

        This and other SYS\_SFLIST\_\*() macros are not thread safe.

        Parameters:
        :   - **\_\_sl** – A pointer on a [sys\_sflist\_t](#group__flagged-single-linked-list__apis_1ga9e7f835170787303732c805dc7375f66) to iterate on
            - **\_\_sn** – A [sys\_sfnode\_t](#group__flagged-single-linked-list__apis_1ga02dabbe35036cbc11fbbefa99a129cc7) pointer to peek each node of the list it contains the starting node, or NULL to start from the head

    SYS\_SFLIST\_FOR\_EACH\_NODE\_SAFE(\_\_sl, \_\_sn, \_\_sns)
    :   Provide the primitive to safely iterate on a list Note: \_\_sn can be removed, it will not break the loop.

        User *MUST* add the loop statement curly braces enclosing its own code:

        ```text
        SYS_SFLIST_FOR_EACH_NODE_SAFE(l, n, s) {
            <user code>
        }
        ```

        This and other SYS\_SFLIST\_\*() macros are not thread safe.

        Parameters:
        :   - **\_\_sl** – A pointer on a [sys\_sflist\_t](#group__flagged-single-linked-list__apis_1ga9e7f835170787303732c805dc7375f66) to iterate on
            - **\_\_sn** – A [sys\_sfnode\_t](#group__flagged-single-linked-list__apis_1ga02dabbe35036cbc11fbbefa99a129cc7) pointer to peek each node of the list
            - **\_\_sns** – A [sys\_sfnode\_t](#group__flagged-single-linked-list__apis_1ga02dabbe35036cbc11fbbefa99a129cc7) pointer for the loop to run safely

    SYS\_SFLIST\_CONTAINER(\_\_ln, \_\_cn, \_\_n)
    :   Provide the primitive to resolve the container of a list node Note: it is safe to use with NULL pointer nodes.

        Parameters:
        :   - **\_\_ln** – A pointer on a [sys\_sfnode\_t](#group__flagged-single-linked-list__apis_1ga02dabbe35036cbc11fbbefa99a129cc7) to get its container
            - **\_\_cn** – Container struct type pointer
            - **\_\_n** – The field name of [sys\_sfnode\_t](#group__flagged-single-linked-list__apis_1ga02dabbe35036cbc11fbbefa99a129cc7) within the container struct

    SYS\_SFLIST\_PEEK\_HEAD\_CONTAINER(\_\_sl, \_\_cn, \_\_n)
    :   Provide the primitive to peek container of the list head.

        Parameters:
        :   - **\_\_sl** – A pointer on a [sys\_sflist\_t](#group__flagged-single-linked-list__apis_1ga9e7f835170787303732c805dc7375f66) to peek
            - **\_\_cn** – Container struct type pointer
            - **\_\_n** – The field name of [sys\_sfnode\_t](#group__flagged-single-linked-list__apis_1ga02dabbe35036cbc11fbbefa99a129cc7) within the container struct

    SYS\_SFLIST\_PEEK\_TAIL\_CONTAINER(\_\_sl, \_\_cn, \_\_n)
    :   Provide the primitive to peek container of the list tail.

        Parameters:
        :   - **\_\_sl** – A pointer on a [sys\_sflist\_t](#group__flagged-single-linked-list__apis_1ga9e7f835170787303732c805dc7375f66) to peek
            - **\_\_cn** – Container struct type pointer
            - **\_\_n** – The field name of [sys\_sfnode\_t](#group__flagged-single-linked-list__apis_1ga02dabbe35036cbc11fbbefa99a129cc7) within the container struct

    SYS\_SFLIST\_PEEK\_NEXT\_CONTAINER(\_\_cn, \_\_n)
    :   Provide the primitive to peek the next container.

        Parameters:
        :   - **\_\_cn** – Container struct type pointer
            - **\_\_n** – The field name of [sys\_sfnode\_t](#group__flagged-single-linked-list__apis_1ga02dabbe35036cbc11fbbefa99a129cc7) within the container struct

    SYS\_SFLIST\_FOR\_EACH\_CONTAINER(\_\_sl, \_\_cn, \_\_n)
    :   Provide the primitive to iterate on a list under a container Note: the loop is unsafe and thus \_\_cn should not be detached.

        User *MUST* add the loop statement curly braces enclosing its own code:

        ```text
        SYS_SFLIST_FOR_EACH_CONTAINER(l, c, n) {
            <user code>
        }
        ```

        Parameters:
        :   - **\_\_sl** – A pointer on a [sys\_sflist\_t](#group__flagged-single-linked-list__apis_1ga9e7f835170787303732c805dc7375f66) to iterate on
            - **\_\_cn** – A pointer to peek each entry of the list
            - **\_\_n** – The field name of [sys\_sfnode\_t](#group__flagged-single-linked-list__apis_1ga02dabbe35036cbc11fbbefa99a129cc7) within the container struct

    SYS\_SFLIST\_FOR\_EACH\_CONTAINER\_SAFE(\_\_sl, \_\_cn, \_\_cns, \_\_n)
    :   Provide the primitive to safely iterate on a list under a container Note: \_\_cn can be detached, it will not break the loop.

        User *MUST* add the loop statement curly braces enclosing its own code:

        ```text
        SYS_SFLIST_FOR_EACH_NODE_SAFE(l, c, cn, n) {
            <user code>
        }
        ```

        Parameters:
        :   - **\_\_sl** – A pointer on a [sys\_sflist\_t](#group__flagged-single-linked-list__apis_1ga9e7f835170787303732c805dc7375f66) to iterate on
            - **\_\_cn** – A pointer to peek each entry of the list
            - **\_\_cns** – A pointer for the loop to run safely
            - **\_\_n** – The field name of [sys\_sfnode\_t](#group__flagged-single-linked-list__apis_1ga02dabbe35036cbc11fbbefa99a129cc7) within the container struct

    SYS\_SFLIST\_STATIC\_INIT(ptr\_to\_list)
    :   Statically initialize a flagged single-linked list.

        Parameters:
        :   - **ptr\_to\_list** – A pointer on the list to initialize

    SYS\_SFLIST\_FLAGS\_MASK

    Typedefs

    typedef uint32\_t unative\_t

    typedef struct \_sfnode sys\_sfnode\_t
    :   Flagged single-linked list node structure.

    typedef struct \_sflist sys\_sflist\_t
    :   Flagged single-linked list structure.

    Functions

    static inline void sys\_sflist\_init([sys\_sflist\_t](#c.sys_sflist_t) \*list)
    :   Initialize a list.

        Parameters:
        :   - **list** – A pointer on the list to initialize

    static inline uint8\_t sys\_sfnode\_flags\_get([sys\_sfnode\_t](#c.sys_sfnode_t) \*node)
    :   Fetch flags value for a particular sfnode.

        Parameters:
        :   - **node** – A pointer to the node to fetch flags from

        Returns:
        :   The value of flags, which will be between 0 and 3

    static inline [sys\_sfnode\_t](#c.sys_sfnode_t) \*sys\_sflist\_peek\_head([sys\_sflist\_t](#c.sys_sflist_t) \*list)
    :   Peek the first node from the list.

        Parameters:
        :   - **list** – A point on the list to peek the first node from

        Returns:
        :   A pointer on the first node of the list (or NULL if none)

    static inline [sys\_sfnode\_t](#c.sys_sfnode_t) \*sys\_sflist\_peek\_tail([sys\_sflist\_t](#c.sys_sflist_t) \*list)
    :   Peek the last node from the list.

        Parameters:
        :   - **list** – A point on the list to peek the last node from

        Returns:
        :   A pointer on the last node of the list (or NULL if none)

    static inline void sys\_sfnode\_init([sys\_sfnode\_t](#c.sys_sfnode_t) \*node, uint8\_t flags)
    :   Initialize an sflist node.

        Set an initial flags value for this slist node, which can be a value between 0 and 3. These flags will persist even if the node is moved around within a list, removed, or transplanted to a different slist.

        This is ever so slightly faster than [sys\_sfnode\_flags\_set()](#group__flagged-single-linked-list__apis_1ga85d82a3a5927f79a5f5655cb3405ce95) and should only be used on a node that hasn’t been added to any list.

        Parameters:
        :   - **node** – A pointer to the node to set the flags on
            - **flags** – A value between 0 and 3 to set the flags value

    static inline void sys\_sfnode\_flags\_set([sys\_sfnode\_t](#c.sys_sfnode_t) \*node, uint8\_t flags)
    :   Set flags value for an sflist node.

        Set a flags value for this slist node, which can be a value between 0 and 3. These flags will persist even if the node is moved around within a list, removed, or transplanted to a different slist.

        Parameters:
        :   - **node** – A pointer to the node to set the flags on
            - **flags** – A value between 0 and 3 to set the flags value

    static inline bool sys\_sflist\_is\_empty([sys\_sflist\_t](#c.sys_sflist_t) \*list)
    :   Test if the given list is empty.

        Parameters:
        :   - **list** – A pointer on the list to test

        Returns:
        :   a boolean, true if it’s empty, false otherwise

    static inline [sys\_sfnode\_t](#c.sys_sfnode_t) \*sys\_sflist\_peek\_next\_no\_check([sys\_sfnode\_t](#c.sys_sfnode_t) \*node)
    :   Peek the next node from current node, node is not NULL.

        Faster then [sys\_sflist\_peek\_next()](#group__flagged-single-linked-list__apis_1ga514b41f1af89f3f08e216cfede7d5605) if node is known not to be NULL.

        Parameters:
        :   - **node** – A pointer on the node where to peek the next node

        Returns:
        :   a pointer on the next node (or NULL if none)

    static inline [sys\_sfnode\_t](#c.sys_sfnode_t) \*sys\_sflist\_peek\_next([sys\_sfnode\_t](#c.sys_sfnode_t) \*node)
    :   Peek the next node from current node.

        Parameters:
        :   - **node** – A pointer on the node where to peek the next node

        Returns:
        :   a pointer on the next node (or NULL if none)

    static inline void sys\_sflist\_prepend([sys\_sflist\_t](#c.sys_sflist_t) \*list, [sys\_sfnode\_t](#c.sys_sfnode_t) \*node)
    :   Prepend a node to the given list.

        This and other sys\_sflist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – A pointer on the list to affect
            - **node** – A pointer on the node to prepend

    static inline void sys\_sflist\_append([sys\_sflist\_t](#c.sys_sflist_t) \*list, [sys\_sfnode\_t](#c.sys_sfnode_t) \*node)
    :   Append a node to the given list.

        This and other sys\_sflist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – A pointer on the list to affect
            - **node** – A pointer on the node to append

    static inline void sys\_sflist\_append\_list([sys\_sflist\_t](#c.sys_sflist_t) \*list, void \*head, void \*tail)
    :   Append a list to the given list.

        Append a singly-linked, NULL-terminated list consisting of nodes containing the pointer to the next node as the first element of a node, to *list*. This and other sys\_sflist\_\*() functions are not thread safe.

        FIXME: Why are the element parameters void \*?

        Parameters:
        :   - **list** – A pointer on the list to affect
            - **head** – A pointer to the first element of the list to append
            - **tail** – A pointer to the last element of the list to append

    static inline void sys\_sflist\_merge\_sflist([sys\_sflist\_t](#c.sys_sflist_t) \*list, [sys\_sflist\_t](#c.sys_sflist_t) \*list\_to\_append)
    :   merge two sflists, appending the second one to the first

        When the operation is completed, the appending list is empty. This and other sys\_sflist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – A pointer on the list to affect
            - **list\_to\_append** – A pointer to the list to append.

    static inline void sys\_sflist\_insert([sys\_sflist\_t](#c.sys_sflist_t) \*list, [sys\_sfnode\_t](#c.sys_sfnode_t) \*prev, [sys\_sfnode\_t](#c.sys_sfnode_t) \*node)
    :   Insert a node to the given list.

        This and other sys\_sflist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – A pointer on the list to affect
            - **prev** – A pointer on the previous node
            - **node** – A pointer on the node to insert

    static inline [sys\_sfnode\_t](#c.sys_sfnode_t) \*sys\_sflist\_get\_not\_empty([sys\_sflist\_t](#c.sys_sflist_t) \*list)
    :   Fetch and remove the first node of the given list.

        List must be known to be non-empty. This and other sys\_sflist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – A pointer on the list to affect

        Returns:
        :   A pointer to the first node of the list

    static inline [sys\_sfnode\_t](#c.sys_sfnode_t) \*sys\_sflist\_get([sys\_sflist\_t](#c.sys_sflist_t) \*list)
    :   Fetch and remove the first node of the given list.

        This and other sys\_sflist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – A pointer on the list to affect

        Returns:
        :   A pointer to the first node of the list (or NULL if empty)

    static inline void sys\_sflist\_remove([sys\_sflist\_t](#c.sys_sflist_t) \*list, [sys\_sfnode\_t](#c.sys_sfnode_t) \*prev\_node, [sys\_sfnode\_t](#c.sys_sfnode_t) \*node)
    :   Remove a node.

        This and other sys\_sflist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – A pointer on the list to affect
            - **prev\_node** – A pointer on the previous node (can be NULL, which means the node is the list’s head)
            - **node** – A pointer on the node to remove

    static inline bool sys\_sflist\_find\_and\_remove([sys\_sflist\_t](#c.sys_sflist_t) \*list, [sys\_sfnode\_t](#c.sys_sfnode_t) \*node)
    :   Find and remove a node from a list.

        This and other sys\_sflist\_\*() functions are not thread safe.

        Parameters:
        :   - **list** – A pointer on the list to affect
            - **node** – A pointer on the node to remove from the list

        Returns:
        :   true if node was removed

    static inline size\_t sys\_sflist\_len([sys\_sflist\_t](#c.sys_sflist_t) \*list)
    :   Compute the size of the given list in O(n) time.

        Parameters:
        :   - **list** – A pointer on the list

        Returns:
        :   an integer equal to the size of the list, or 0 if empty
