---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__memory__attr__interface.html
original_path: doxygen/html/group__memory__attr__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Memory-Attr Interface

[Memory Management APIs](group__mem__mgmt.md)

Memory-Attr Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [mem\_attr\_region\_t](structmem__attr__region__t.md) |
|  | memory-attr region structure. [More...](structmem__attr__region__t.md#details) |

| Macros | |
| --- | --- |
| #define | [DT\_MEMORY\_ATTR\_FOREACH\_STATUS\_OKAY\_NODE](#ga316e41444a0db6bb78ec0c1c4bdc832b)(fn) |
|  | Invokes `fn` for every status okay node in the tree with property zephyr,memory-attr. |

| Functions | |
| --- | --- |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [mem\_attr\_get\_regions](#gadcf93c67fe564d65064f5f6175d7089f) (const struct [mem\_attr\_region\_t](structmem__attr__region__t.md) \*\*region) |
|  | Get the list of memory regions. |
| int | [mem\_attr\_check\_buf](#gac599eafdb0be231c0105b05eb76b657b) (void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) attr) |
|  | Check if a buffer has correct size and attributes. |

## Detailed Description

Memory-Attr Interface.

## Macro Definition Documentation

## [◆ ](#ga316e41444a0db6bb78ec0c1c4bdc832b)DT\_MEMORY\_ATTR\_FOREACH\_STATUS\_OKAY\_NODE

| #define DT\_MEMORY\_ATTR\_FOREACH\_STATUS\_OKAY\_NODE | ( |  | *fn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mem_attr.h](mem__attr_8h.md)>`

**Value:**

[DT\_FOREACH\_STATUS\_OKAY\_NODE\_VARGS](group__devicetree-generic-foreach.md#ga9aa3ee2b90a4ec30621597f4d1448c51)(\_FILTER, fn)

[DT\_FOREACH\_STATUS\_OKAY\_NODE\_VARGS](group__devicetree-generic-foreach.md#ga9aa3ee2b90a4ec30621597f4d1448c51)

#define DT\_FOREACH\_STATUS\_OKAY\_NODE\_VARGS(fn,...)

Invokes fn for every status okay node in the tree with multiple arguments.

**Definition** devicetree.h:2801

Invokes `fn` for every status okay node in the tree with property zephyr,memory-attr.

The macro `fn` must take one parameter, which will be a node identifier with the zephyr,memory-attr property. The macro is expanded once for each node in the tree with status okay. The order that nodes are visited in is not specified.

Parameters
:   | fn | macro to invoke |
    | --- | --- |

## Function Documentation

## [◆ ](#gac599eafdb0be231c0105b05eb76b657b)mem\_attr\_check\_buf()

| int mem\_attr\_check\_buf | ( | void \* | *addr*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *attr* ) |

`#include <[mem_attr.h](mem__attr_8h.md)>`

Check if a buffer has correct size and attributes.

This function is used to check if a given buffer with a given set of attributes fully match a memory region in terms of size and attributes.

This is usually used to verify that a buffer has the expected attributes (for example the buffer is cacheable / non-cacheable or belongs to RAM / FLASH, etc...) and it has been correctly allocated.

The expected set of attributes for the buffer is and-matched against the full set of attributes for the memory region it belongs to (bitmask). So the buffer is considered matching when at least that set of attributes are valid for the memory region (but the region can be marked also with other attributes besides the one passed as parameter).

Parameters
:   | addr | Virtual address of the user buffer. |
    | --- | --- |
    | size | Size of the user buffer. |
    | attr | Expected / desired attribute for the buffer. |

Return values
:   | 0 | if the buffer has the correct size and attribute. |
    | --- | --- |
    | -ENOSYS | if the operation is not supported (for example if the MMU is enabled). |
    | -ENOTSUP | if the wrong parameters were passed. |
    | -EINVAL | if the buffer has the wrong set of attributes. |
    | -ENOSPC | if the buffer is too big for the region it belongs to. |
    | -ENOBUFS | if the buffer is entirely allocated outside a memory region. |

## [◆ ](#gadcf93c67fe564d65064f5f6175d7089f)mem\_attr\_get\_regions()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) mem\_attr\_get\_regions | ( | const struct [mem\_attr\_region\_t](structmem__attr__region__t.md) \*\* | *region* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mem_attr.h](mem__attr_8h.md)>`

Get the list of memory regions.

Get the list of enabled memory regions with their memory-attribute as gathered by DT.

Parameters
:   | region | Pointer to pointer to the list of memory regions. |
    | --- | --- |

Return values
:   | Number | of memory regions returned in the parameter. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
