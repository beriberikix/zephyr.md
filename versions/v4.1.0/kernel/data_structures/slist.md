---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/kernel/data_structures/slist.html
original_path: kernel/data_structures/slist.html
---

# Single-linked List

Zephyr provides a [`sys_slist_t`](../../doxygen/html/group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) type for storing simple
singly-linked list data (i.e. data where each list element stores a
pointer to the next element, but not the previous one). This supports
constant-time access to the first (head) and last (tail) elements of
the list, insertion before the head and after the tail of the list and
constant time removal of the head. Removal of subsequent nodes
requires access to the “previous” pointer and thus can only be
performed in linear time by searching the list.

The [`sys_slist_t`](../../doxygen/html/group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) struct may be instantiated by the user in any
accessible memory. It should be initialized with either
[`sys_slist_init()`](../../doxygen/html/group__single-linked-list__apis.md#ga913aea7661b4ab3b4b50a8efc0d70428) or by static assignment from SYS\_SLIST\_STATIC\_INIT
before use. Its interior fields are opaque and should not be accessed
by user code.

The end nodes of a list may be retrieved with
[`sys_slist_peek_head()`](../../doxygen/html/group__single-linked-list__apis.md#ga1af7fbf228545d591ef8961fa5f6a8f1) and [`sys_slist_peek_tail()`](../../doxygen/html/group__single-linked-list__apis.md#ga49975721fa11c48000669d2c4ec0877f), which will
return NULL if the list is empty, otherwise a pointer to a
[`sys_snode_t`](../../doxygen/html/group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) struct.

The [`sys_snode_t`](../../doxygen/html/group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) struct represents the data to be inserted. In
general, it is expected to be allocated/controlled by the user,
usually embedded within a struct which is to be added to the list.
The container struct pointer may be retrieved from a list node using
[`SYS_SLIST_CONTAINER`](../../doxygen/html/group__single-linked-list__apis.md#ga07e4257835751e18a6c06bfa5f9c25e8), passing it the struct name of the
containing struct and the field name of the node. Internally, the
[`sys_snode_t`](../../doxygen/html/group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) struct contains only a next pointer, which may be
accessed with [`sys_slist_peek_next()`](../../doxygen/html/group__single-linked-list__apis.md#ga729cbf8cafdbc34261db9274195ac5df).

Lists may be modified by adding a single node at the head or tail with
[`sys_slist_prepend()`](../../doxygen/html/group__single-linked-list__apis.md#gac962e3ec8440e4adb2ba6682dbf186ff) and [`sys_slist_append()`](../../doxygen/html/group__single-linked-list__apis.md#ga829fd7b6f1944dc38e10685e861e62b5). They may also
have a node added to an interior point with [`sys_slist_insert()`](../../doxygen/html/group__single-linked-list__apis.md#gadcbef5c013861fdfd325bae357c37b85),
which inserts a new node after an existing one. Similarly
[`sys_slist_remove()`](../../doxygen/html/group__single-linked-list__apis.md#gaee6957483d4fbe3b824f7a495d56030f) will remove a node given a pointer to its
predecessor. These operations are all constant time.

Convenience routines exist for more complicated modifications to a
list. [`sys_slist_merge_slist()`](../../doxygen/html/group__single-linked-list__apis.md#ga0c00bbb3dc6903f386fdb1e37fdd3b66) will append an entire list to an
existing one. [`sys_slist_append_list()`](../../doxygen/html/group__single-linked-list__apis.md#gaaf7393c6bbf6d5cbd303173d95269481) will append a bounded
subset of an existing list in constant time. And
[`sys_slist_find_and_remove()`](../../doxygen/html/group__single-linked-list__apis.md#ga296560229ffdfd0054c9c7b0602825a6) will search a list (in linear time)
for a given node and remove it if present.

Finally the slist implementation provides a set of “for each” macros
that allows for iterating over a list in a natural way without needing
to manually traverse the next pointers. [`SYS_SLIST_FOR_EACH_NODE`](../../doxygen/html/group__single-linked-list__apis.md#gaf32ac0f222186e497d3f6180b6c26352)
will enumerate every node in a list given a local variable to store
the node pointer. [`SYS_SLIST_FOR_EACH_NODE_SAFE`](../../doxygen/html/group__single-linked-list__apis.md#gad6f1014e26d6cf9925d00b4f53076116) behaves
similarly, but has a more complicated implementation that requires an
extra scratch variable for storage and allows the user to delete the
iterated node during the iteration. Each of those macros also exists
in a “container” variant ([`SYS_SLIST_FOR_EACH_CONTAINER`](../../doxygen/html/group__single-linked-list__apis.md#gacd97d2f1044c0560d96c9f9a6f26d2f6) and
[`SYS_SLIST_FOR_EACH_CONTAINER_SAFE`](../../doxygen/html/group__single-linked-list__apis.md#gacf3aaf32a6a3389229b548588c6d655e)) which assigns a local
variable of a type that matches the user’s container struct and not
the node struct, performing the required offsets internally. And
[`SYS_SLIST_ITERATE_FROM_NODE`](../../doxygen/html/group__single-linked-list__apis.md#ga1740075b07ec67635c1934dcbe1b5cee) exists to allow for enumerating a
node and all its successors only, without inspecting the earlier part
of the list.

## Single-linked List Internals

The slist code is designed to be minimal and conventional.
Internally, a [`sys_slist_t`](../../doxygen/html/group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) struct is nothing more than a pair of
“head” and “tail” pointer fields. And a [`sys_snode_t`](../../doxygen/html/group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) stores only a
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

The [`sys_sflist_t`](../../doxygen/html/group__flagged-single-linked-list__apis.md#ga9e7f835170787303732c805dc7375f66) is implemented using the described genlist
template API. With the exception of symbol naming (“sflist” instead
of “slist”) and the additional API described next, it operates in all
ways identically to the slist API.

It adds the ability to associate exactly two bits of user defined
“flags” with each list node. These can be accessed and modified with
[`sys_sfnode_flags_get()`](../../doxygen/html/group__flagged-single-linked-list__apis.md#ga0e258c1faa3cbaee48c29e8f2c11132b) and [`sys_sfnode_flags_set()`](../../doxygen/html/group__flagged-single-linked-list__apis.md#ga85d82a3a5927f79a5f5655cb3405ce95).
Internally, the flags are stored unioned with the bottom bits of the
next pointer and incur no SRAM storage overhead when compared with the
simpler slist code.

## Single-linked List API Reference

[Single-linked list](../../doxygen/html/group__single-linked-list__apis.md)

## Flagged List API Reference

[Flagged Single-linked list](../../doxygen/html/group__flagged-single-linked-list__apis.md)
