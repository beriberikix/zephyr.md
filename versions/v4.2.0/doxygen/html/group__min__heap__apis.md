---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__min__heap__apis.html
original_path: doxygen/html/group__min__heap__apis.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Min-Heap service

[Utilities](group__utilities.md) » [Data Structure APIs](group__datastructure__apis.md)

[min\_heap](structmin__heap.md "min-heap data structure with user-provided comparator.")
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [min\_heap](structmin__heap.md) |
|  | min-heap data structure with user-provided comparator. [More...](structmin__heap.md#details) |

| Macros | |
| --- | --- |
| #define | [MIN\_HEAP\_DEFINE](#ga2363fb8ce4cd36e21ae5100e62d450c4)(name, cap, elem\_sz, align, cmp\_func) |
|  | Define a min-heap instance. |
| #define | [MIN\_HEAP\_DEFINE\_STATIC](#gab4b10202a0a9f63608061b2ce35d902c)(name, cap, elem\_sz, align, cmp\_func) |
|  | Define a statically allocated and aligned min-heap instance. |
| #define | [MIN\_HEAP\_FOREACH](#ga73c54e30b56717ee7498141488504137)(heap, node\_var) |
|  | Iterate over each node in the heap. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [min\_heap\_cmp\_t](#ga638b9c8b6023ec281b1adcb9ca6ba814)) (const void \*a, const void \*b) |
|  | Comparator function type for min-heap ordering. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [min\_heap\_eq\_t](#gab17087bc7c433bb85e94d4c88ad4ffbb)) (const void \*node, const void \*other) |
|  | Equality function for finding a node in the heap. |

| Functions | |
| --- | --- |
| void | [min\_heap\_init](#ga675aa066413418b51e2210331f5d352b) (struct [min\_heap](structmin__heap.md) \*heap, void \*storage, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) cap, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) elem\_size, [min\_heap\_cmp\_t](#ga638b9c8b6023ec281b1adcb9ca6ba814) cmp) |
|  | Initialize a min-heap instance at runtime. |
| int | [min\_heap\_push](#ga4cb5ee2bf40ab6f1ba557f8fa3927ba3) (struct [min\_heap](structmin__heap.md) \*heap, const void \*item) |
|  | Push an element into the min-heap. |
| void \* | [min\_heap\_peek](#ga022a40c2cd09b925118a157ba05bfc2f) (const struct [min\_heap](structmin__heap.md) \*heap) |
|  | Peek at the top element of the min-heap. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [min\_heap\_remove](#gab65afad260840bff650977b137404c7c) (struct [min\_heap](structmin__heap.md) \*heap, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) id, void \*out\_buf) |
|  | Remove a specific element from the min-heap. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [min\_heap\_is\_empty](#ga808c35eebd9e18aadeba4f5b2a4db827) (struct [min\_heap](structmin__heap.md) \*heap) |
|  | Check if the min heap is empty. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [min\_heap\_pop](#gacd04b6cd038669e229c69f60c25af9e0) (struct [min\_heap](structmin__heap.md) \*heap, void \*out\_buf) |
|  | Remove and return the highest priority element in the heap. |
| void \* | [min\_heap\_find](#ga246f404f179c6c4c8ebeec6e15b2e3c2) (struct [min\_heap](structmin__heap.md) \*heap, [min\_heap\_eq\_t](#gab17087bc7c433bb85e94d4c88ad4ffbb) eq, const void \*other, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*out\_id) |
|  | Search for a node in the heap matching a condition. |
| static void \* | [min\_heap\_get\_element](#gac0f633e80405d5e47f8bd8eb09d952c6) (const struct [min\_heap](structmin__heap.md) \*heap, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) index) |
|  | Get a pointer to the element at the specified index. |

## Detailed Description

[min\_heap](structmin__heap.md "min-heap data structure with user-provided comparator.")

## Macro Definition Documentation

## [◆ ](#ga2363fb8ce4cd36e21ae5100e62d450c4)MIN\_HEAP\_DEFINE

| #define MIN\_HEAP\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *cap*, |
|  |  |  | *elem\_sz*, |
|  |  |  | *align*, |
|  |  |  | *cmp\_func* ) |

`#include <[zephyr/sys/min_heap.h](min__heap_8h.md)>`

**Value:**

static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) name##\_storage[(cap) \* (elem\_sz)] \_\_aligned(align); \

struct [min\_heap](structmin__heap.md) name = {.storage = name##\_storage, \

.[capacity](structmin__heap.md#afb0062bd8818c9184cd8469a3f95dc6d) = (cap), \

.elem\_size = (elem\_sz), \

.size = 0, \

.cmp = (cmp\_func)}

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[min\_heap](structmin__heap.md)

min-heap data structure with user-provided comparator.

**Definition** min\_heap.h:55

[min\_heap::capacity](structmin__heap.md#afb0062bd8818c9184cd8469a3f95dc6d)

size\_t capacity

Maximum number of elements.

**Definition** min\_heap.h:59

Define a min-heap instance.

Parameters
:   | name | Base name for the heap instance. |
    | --- | --- |
    | cap | Capacity (number of elements). |
    | elem\_sz | Size in bytes of each element. |
    | align | Required alignment of each element. |
    | cmp\_func | Comparator function used by the heap |

## [◆ ](#gab4b10202a0a9f63608061b2ce35d902c)MIN\_HEAP\_DEFINE\_STATIC

| #define MIN\_HEAP\_DEFINE\_STATIC | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *cap*, |
|  |  |  | *elem\_sz*, |
|  |  |  | *align*, |
|  |  |  | *cmp\_func* ) |

`#include <[zephyr/sys/min_heap.h](min__heap_8h.md)>`

**Value:**

static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) name##\_storage[(cap) \* (elem\_sz)] \_\_aligned(align); \

static struct [min\_heap](structmin__heap.md) name = { \

.storage = name##\_storage, \

.[capacity](structmin__heap.md#afb0062bd8818c9184cd8469a3f95dc6d) = (cap), \

.elem\_size = (elem\_sz), \

.size = 0, \

.cmp = (cmp\_func) \

}

Define a statically allocated and aligned min-heap instance.

Parameters
:   | name | Base name for the heap instance. |
    | --- | --- |
    | cap | Capacity (number of elements). |
    | elem\_sz | Size in bytes of each element. |
    | align | Required alignment of each element. |
    | cmp\_func | Comparator function used by the heap |

## [◆ ](#ga73c54e30b56717ee7498141488504137)MIN\_HEAP\_FOREACH

| #define MIN\_HEAP\_FOREACH | ( |  | *heap*, |
| --- | --- | --- | --- |
|  |  |  | *node\_var* ) |

`#include <[zephyr/sys/min_heap.h](min__heap_8h.md)>`

**Value:**

for (size\_t \_i = 0; \

\_i < (heap)->size && (((node\_var) = [min\_heap\_get\_element](#gac0f633e80405d5e47f8bd8eb09d952c6)((heap), \_i)) || true); ++\_i)

[min\_heap\_get\_element](#gac0f633e80405d5e47f8bd8eb09d952c6)

static void \* min\_heap\_get\_element(const struct min\_heap \*heap, size\_t index)

Get a pointer to the element at the specified index.

**Definition** min\_heap.h:216

Iterate over each node in the heap.

Parameters
:   | heap | Pointer to the heap. |
    | --- | --- |
    | node\_var | The loop variable used to reference each node. |

Example:

void \*node;

[MIN\_HEAP\_FOREACH](#ga73c54e30b56717ee7498141488504137)(&heap, node) {

[printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)("Value: %d\n", node->value);

}

[MIN\_HEAP\_FOREACH](#ga73c54e30b56717ee7498141488504137)

#define MIN\_HEAP\_FOREACH(heap, node\_var)

Iterate over each node in the heap.

**Definition** min\_heap.h:238

[printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)

static void printk(const char \*fmt,...)

Print kernel debugging message.

**Definition** printk.h:51

## Typedef Documentation

## [◆ ](#ga638b9c8b6023ec281b1adcb9ca6ba814)min\_heap\_cmp\_t

| typedef int(\* min\_heap\_cmp\_t) (const void \*a, const void \*b) |
| --- |

`#include <[zephyr/sys/min_heap.h](min__heap_8h.md)>`

Comparator function type for min-heap ordering.

This function compares two heap nodes to establish their relative order. It must be implemented by the user and provided at min-heap initialization.

Parameters
:   | a | First user defined data pointer for comparison. |
    | --- | --- |
    | b | Second user defined data pointer for comparison. |

Returns
:   Negative value if `a` is less than `b`, positive value if `a` is greater than `b`, zero if they are equal.

## [◆ ](#gab17087bc7c433bb85e94d4c88ad4ffbb)min\_heap\_eq\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* min\_heap\_eq\_t) (const void \*node, const void \*other) |
| --- |

`#include <[zephyr/sys/min_heap.h](min__heap_8h.md)>`

Equality function for finding a node in the heap.

Parameters
:   | node | Pointer to a user defined data. |
    | --- | --- |
    | other | Pointer to a user-defined key or structure to compare with. |

Returns
:   true if the node matches the search criteria, false otherwise.

## Function Documentation

## [◆ ](#ga246f404f179c6c4c8ebeec6e15b2e3c2)min\_heap\_find()

| void \* min\_heap\_find | ( | struct [min\_heap](structmin__heap.md) \* | *heap*, |
| --- | --- | --- | --- |
|  |  | [min\_heap\_eq\_t](#gab17087bc7c433bb85e94d4c88ad4ffbb) | *eq*, |
|  |  | const void \* | *other*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *out\_id* ) |

`#include <[zephyr/sys/min_heap.h](min__heap_8h.md)>`

Search for a node in the heap matching a condition.

Parameters
:   | heap | Pointer to the heap structure. |
    | --- | --- |
    | eq | Function used to compare each node with the search target. |
    | other | Pointer to the data used for comparison in the eq function. |
    | out\_id | Optional output parameter to store the index of the found node. |

Returns
:   Pointer to the first matching element, or NULL if not found.

## [◆ ](#gac0f633e80405d5e47f8bd8eb09d952c6)min\_heap\_get\_element()

| | void \* min\_heap\_get\_element | ( | const struct [min\_heap](structmin__heap.md) \* | *heap*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *index* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/sys/min_heap.h](min__heap_8h.md)>`

Get a pointer to the element at the specified index.

Parameters
:   | heap | Pointer to the min-heap. |
    | --- | --- |
    | index | Index of the element to retrieve. |

Returns
:   Pointer to the element at the given index.

## [◆ ](#ga675aa066413418b51e2210331f5d352b)min\_heap\_init()

| void min\_heap\_init | ( | struct [min\_heap](structmin__heap.md) \* | *heap*, |
| --- | --- | --- | --- |
|  |  | void \* | *storage*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *cap*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *elem\_size*, |
|  |  | [min\_heap\_cmp\_t](#ga638b9c8b6023ec281b1adcb9ca6ba814) | *cmp* ) |

`#include <[zephyr/sys/min_heap.h](min__heap_8h.md)>`

Initialize a min-heap instance at runtime.

Sets up the internal structure of a min heap using a user-provided memory block, capacity, and comparator function. This function must be called before using the heap if not statically defined.

Parameters
:   | heap | Pointer to the min-heap structure. |
    | --- | --- |
    | storage | Pointer to memory block for storing elements. |
    | cap | Maximum number of elements the heap can store. |
    | elem\_size | Size in bytes of each element. |
    | cmp | Comparator function used to order the heap elements. |

Note
:   All arguments must be valid. This function does not allocate memory.

## [◆ ](#ga808c35eebd9e18aadeba4f5b2a4db827)min\_heap\_is\_empty()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) min\_heap\_is\_empty | ( | struct [min\_heap](structmin__heap.md) \* | *heap* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/sys/min_heap.h](min__heap_8h.md)>`

Check if the min heap is empty.

This function checks whether the heap contains any elements.

Parameters
:   | heap | Pointer to the min heap. |
    | --- | --- |

Returns
:   true if heap is empty, false otherwise.

## [◆ ](#ga022a40c2cd09b925118a157ba05bfc2f)min\_heap\_peek()

| void \* min\_heap\_peek | ( | const struct [min\_heap](structmin__heap.md) \* | *heap* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/sys/min_heap.h](min__heap_8h.md)>`

Peek at the top element of the min-heap.

The function will not remove the element from the min-heap.

Parameters
:   | heap | Pointer to the min-heap. |
    | --- | --- |

Returns
:   Pointer to the top priority element, or NULL if the heap is empty.

## [◆ ](#gacd04b6cd038669e229c69f60c25af9e0)min\_heap\_pop()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) min\_heap\_pop | ( | struct [min\_heap](structmin__heap.md) \* | *heap*, |
| --- | --- | --- | --- |
|  |  | void \* | *out\_buf* ) |

`#include <[zephyr/sys/min_heap.h](min__heap_8h.md)>`

Remove and return the highest priority element in the heap.

The caller gains ownership of the returned element and is responsible for any further management of its memory or reuse. The min-heap is rebalanced after removal to ensure proper ordering.

Parameters
:   | heap | Pointer to heap. |
    | --- | --- |
    | out\_buf | User-provided buffer where the removed element will be copied. |

Returns
:   true in success, false otherwise.

## [◆ ](#ga4cb5ee2bf40ab6f1ba557f8fa3927ba3)min\_heap\_push()

| int min\_heap\_push | ( | struct [min\_heap](structmin__heap.md) \* | *heap*, |
| --- | --- | --- | --- |
|  |  | const void \* | *item* ) |

`#include <[zephyr/sys/min_heap.h](min__heap_8h.md)>`

Push an element into the min-heap.

Adds a new element to the min-heap and restores the heap order by moving it upward as necessary. Insert operation will fail if the min-heap has reached full capacity.

Parameters
:   | heap | Pointer to the min-heap. |
    | --- | --- |
    | item | Pointer to the item to insert. |

Returns
:   0 on Success, -ENOMEM if the heap is full.

## [◆ ](#gab65afad260840bff650977b137404c7c)min\_heap\_remove()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) min\_heap\_remove | ( | struct [min\_heap](structmin__heap.md) \* | *heap*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *id*, |
|  |  | void \* | *out\_buf* ) |

`#include <[zephyr/sys/min_heap.h](min__heap_8h.md)>`

Remove a specific element from the min-heap.

Removes the specified node from the min-heap based on the ID it stores internally. The min-heap is rebalanced after removal to ensure proper ordering. The caller gains ownership of the returned element and is responsible for any further management of its memory or reuse.

Parameters
:   | heap | Pointer to the min-heap. |
    | --- | --- |
    | id | element ID to be removed. |
    | out\_buf | User-provided buffer where the removed element will be copied. |

Returns
:   true in success, false otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
