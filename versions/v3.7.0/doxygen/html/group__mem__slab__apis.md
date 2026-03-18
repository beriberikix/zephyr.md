---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__mem__slab__apis.html
original_path: doxygen/html/group__mem__slab__apis.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Memory Slab APIs

[Kernel APIs](group__kernel__apis.md)

| Macros | |
| --- | --- |
| #define | [K\_MEM\_SLAB\_DEFINE](#ga60bc92eee58fcc5f121b8e4d82eaa69e)(name, slab\_block\_size, slab\_num\_blocks, slab\_align) |
|  | Statically define and initialize a memory slab in a public (non-static) scope. |
| #define | [K\_MEM\_SLAB\_DEFINE\_STATIC](#ga90bdbb15f410991f54ba16025c24bc3c)(name, slab\_block\_size, slab\_num\_blocks, slab\_align) |
|  | Statically define and initialize a memory slab in a private (static) scope. |

| Functions | |
| --- | --- |
| int | [k\_mem\_slab\_init](#ga094a8f173f287e29bb287119c26889d1) (struct k\_mem\_slab \*slab, void \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) block\_size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_blocks) |
|  | Initialize a memory slab. |
| int | [k\_mem\_slab\_alloc](#gab16a46d8394aca18de740ad044a8734a) (struct k\_mem\_slab \*slab, void \*\*mem, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Allocate memory from a memory slab. |
| void | [k\_mem\_slab\_free](#ga2635ea8f9a30b8751ec966fe62adc0e1) (struct k\_mem\_slab \*slab, void \*mem) |
|  | Free memory allocated from a memory slab. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_mem\_slab\_num\_used\_get](#gac76b96d7055e4ad94765c93530dd0720) (struct k\_mem\_slab \*slab) |
|  | Get the number of used blocks in a memory slab. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_mem\_slab\_max\_used\_get](#gae0e949c1c3476dd57bc0c0ed627d2346) (struct k\_mem\_slab \*slab) |
|  | Get the number of maximum used blocks so far in a memory slab. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [k\_mem\_slab\_num\_free\_get](#gae87577e2873cf746db69216a82f94aea) (struct k\_mem\_slab \*slab) |
|  | Get the number of unused blocks in a memory slab. |
| int | [k\_mem\_slab\_runtime\_stats\_get](#ga32030a5cfb44f663bd31b4e1b3d5dddb) (struct k\_mem\_slab \*slab, struct [sys\_memory\_stats](structsys__memory__stats.md) \*stats) |
|  | Get the memory stats for a memory slab. |
| int | [k\_mem\_slab\_runtime\_stats\_reset\_max](#gaa1f44e30f4aee98b38e1ab5e93af505c) (struct k\_mem\_slab \*slab) |
|  | Reset the maximum memory usage for a slab. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga60bc92eee58fcc5f121b8e4d82eaa69e)K\_MEM\_SLAB\_DEFINE

| #define K\_MEM\_SLAB\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *slab\_block\_size*, |
|  |  |  | *slab\_num\_blocks*, |
|  |  |  | *slab\_align* ) |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

char \_\_noinit\_named(k\_mem\_slab\_buf\_##name) \

\_\_aligned([WB\_UP](group__sys-util.md#ga8b16b3a76faa15ea544e4b0edb3e62c7)(slab\_align)) \

\_k\_mem\_slab\_buf\_##name[(slab\_num\_blocks) \* [WB\_UP](group__sys-util.md#ga8b16b3a76faa15ea544e4b0edb3e62c7)(slab\_block\_size)]; \

STRUCT\_SECTION\_ITERABLE(k\_mem\_slab, name) = \

Z\_MEM\_SLAB\_INITIALIZER(name, \_k\_mem\_slab\_buf\_##name, \

[WB\_UP](group__sys-util.md#ga8b16b3a76faa15ea544e4b0edb3e62c7)(slab\_block\_size), slab\_num\_blocks)

[WB\_UP](group__sys-util.md#ga8b16b3a76faa15ea544e4b0edb3e62c7)

#define WB\_UP(x)

Value of x rounded up to the next word boundary.

**Definition** util.h:317

Statically define and initialize a memory slab in a public (non-static) scope.

The memory slab's buffer contains *slab\_num\_blocks* memory blocks that are *slab\_block\_size* bytes long. The buffer is aligned to a *slab\_align* -byte boundary. To ensure that each memory block is similarly aligned to this boundary, *slab\_block\_size* must also be a multiple of *slab\_align*.

The memory slab can be accessed outside the module where it is defined using:

extern struct k\_mem\_slab <name>;

Note
:   This macro cannot be used together with a static keyword. If such a use-case is desired, use [K\_MEM\_SLAB\_DEFINE\_STATIC](#ga90bdbb15f410991f54ba16025c24bc3c) instead.

Parameters
:   | name | Name of the memory slab. |
    | --- | --- |
    | slab\_block\_size | Size of each memory block (in bytes). |
    | slab\_num\_blocks | Number memory blocks. |
    | slab\_align | Alignment of the memory slab's buffer (power of 2). |

## [◆ ](#ga90bdbb15f410991f54ba16025c24bc3c)K\_MEM\_SLAB\_DEFINE\_STATIC

| #define K\_MEM\_SLAB\_DEFINE\_STATIC | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *slab\_block\_size*, |
|  |  |  | *slab\_num\_blocks*, |
|  |  |  | *slab\_align* ) |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

static char \_\_noinit\_named(k\_mem\_slab\_buf\_##name) \

\_\_aligned([WB\_UP](group__sys-util.md#ga8b16b3a76faa15ea544e4b0edb3e62c7)(slab\_align)) \

\_k\_mem\_slab\_buf\_##name[(slab\_num\_blocks) \* [WB\_UP](group__sys-util.md#ga8b16b3a76faa15ea544e4b0edb3e62c7)(slab\_block\_size)]; \

static [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)(k\_mem\_slab, name) = \

Z\_MEM\_SLAB\_INITIALIZER(name, \_k\_mem\_slab\_buf\_##name, \

[WB\_UP](group__sys-util.md#ga8b16b3a76faa15ea544e4b0edb3e62c7)(slab\_block\_size), slab\_num\_blocks)

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

Statically define and initialize a memory slab in a private (static) scope.

The memory slab's buffer contains *slab\_num\_blocks* memory blocks that are *slab\_block\_size* bytes long. The buffer is aligned to a *slab\_align* -byte boundary. To ensure that each memory block is similarly aligned to this boundary, *slab\_block\_size* must also be a multiple of *slab\_align*.

Parameters
:   | name | Name of the memory slab. |
    | --- | --- |
    | slab\_block\_size | Size of each memory block (in bytes). |
    | slab\_num\_blocks | Number memory blocks. |
    | slab\_align | Alignment of the memory slab's buffer (power of 2). |

## Function Documentation

## [◆ ](#gab16a46d8394aca18de740ad044a8734a)k\_mem\_slab\_alloc()

| int k\_mem\_slab\_alloc | ( | struct k\_mem\_slab \* | *slab*, |
| --- | --- | --- | --- |
|  |  | void \*\* | *mem*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[kernel.h](kernel_8h.md)>`

Allocate memory from a memory slab.

This routine allocates a memory block from a memory slab.

Note
:   *timeout* must be set to K\_NO\_WAIT if called from ISR.
:   When CONFIG\_MULTITHREADING=n any *timeout* is treated as K\_NO\_WAIT.

Function properties (list may not be complete)
:   isr-ok

Parameters
:   | slab | Address of the memory slab. |
    | --- | --- |
    | mem | Pointer to block address area. |
    | timeout | Waiting period to wait for operation to complete. Use K\_NO\_WAIT to return without waiting, or K\_FOREVER to wait as long as necessary. |

Return values
:   | 0 | Memory allocated. The block address area pointed at by *mem* is set to the starting address of the memory block. |
    | --- | --- |
    | -ENOMEM | Returned without waiting. |
    | -EAGAIN | Waiting period timed out. |
    | -EINVAL | Invalid data supplied |

## [◆ ](#ga2635ea8f9a30b8751ec966fe62adc0e1)k\_mem\_slab\_free()

| void k\_mem\_slab\_free | ( | struct k\_mem\_slab \* | *slab*, |
| --- | --- | --- | --- |
|  |  | void \* | *mem* ) |

`#include <[kernel.h](kernel_8h.md)>`

Free memory allocated from a memory slab.

This routine releases a previously allocated memory block back to its associated memory slab.

Parameters
:   | slab | Address of the memory slab. |
    | --- | --- |
    | mem | Pointer to the memory block (as returned by [k\_mem\_slab\_alloc()](#gab16a46d8394aca18de740ad044a8734a)). |

## [◆ ](#ga094a8f173f287e29bb287119c26889d1)k\_mem\_slab\_init()

| int k\_mem\_slab\_init | ( | struct k\_mem\_slab \* | *slab*, |
| --- | --- | --- | --- |
|  |  | void \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *block\_size*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num\_blocks* ) |

`#include <[kernel.h](kernel_8h.md)>`

Initialize a memory slab.

Initializes a memory slab, prior to its first use.

The memory slab's buffer contains *slab\_num\_blocks* memory blocks that are *slab\_block\_size* bytes long. The buffer must be aligned to an N-byte boundary matching a word boundary, where N is a power of 2 (i.e. 4 on 32-bit systems, 8, 16, ...). To ensure that each memory block is similarly aligned to this boundary, *slab\_block\_size* must also be a multiple of N.

Parameters
:   | slab | Address of the memory slab. |
    | --- | --- |
    | buffer | Pointer to buffer used for the memory blocks. |
    | block\_size | Size of each memory block (in bytes). |
    | num\_blocks | Number of memory blocks. |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EINVAL | invalid data supplied |

## [◆ ](#gae0e949c1c3476dd57bc0c0ed627d2346)k\_mem\_slab\_max\_used\_get()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_mem\_slab\_max\_used\_get | ( | struct k\_mem\_slab \* | *slab* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Get the number of maximum used blocks so far in a memory slab.

This routine gets the maximum number of memory blocks that were allocated in *slab*.

Parameters
:   | slab | Address of the memory slab. |
    | --- | --- |

Returns
:   Maximum number of allocated memory blocks.

## [◆ ](#gae87577e2873cf746db69216a82f94aea)k\_mem\_slab\_num\_free\_get()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_mem\_slab\_num\_free\_get | ( | struct k\_mem\_slab \* | *slab* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Get the number of unused blocks in a memory slab.

This routine gets the number of memory blocks that are currently unallocated in *slab*.

Parameters
:   | slab | Address of the memory slab. |
    | --- | --- |

Returns
:   Number of unallocated memory blocks.

## [◆ ](#gac76b96d7055e4ad94765c93530dd0720)k\_mem\_slab\_num\_used\_get()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) k\_mem\_slab\_num\_used\_get | ( | struct k\_mem\_slab \* | *slab* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Get the number of used blocks in a memory slab.

This routine gets the number of memory blocks that are currently allocated in *slab*.

Parameters
:   | slab | Address of the memory slab. |
    | --- | --- |

Returns
:   Number of allocated memory blocks.

## [◆ ](#ga32030a5cfb44f663bd31b4e1b3d5dddb)k\_mem\_slab\_runtime\_stats\_get()

| int k\_mem\_slab\_runtime\_stats\_get | ( | struct k\_mem\_slab \* | *slab*, |
| --- | --- | --- | --- |
|  |  | struct [sys\_memory\_stats](structsys__memory__stats.md) \* | *stats* ) |

`#include <[kernel.h](kernel_8h.md)>`

Get the memory stats for a memory slab.

This routine gets the runtime memory usage stats for the slab *slab*.

Parameters
:   | slab | Address of the memory slab |
    | --- | --- |
    | stats | Pointer to memory into which to copy memory usage statistics |

Return values
:   | 0 | Success |
    | --- | --- |
    | -EINVAL | Any parameter points to NULL |

## [◆ ](#gaa1f44e30f4aee98b38e1ab5e93af505c)k\_mem\_slab\_runtime\_stats\_reset\_max()

| int k\_mem\_slab\_runtime\_stats\_reset\_max | ( | struct k\_mem\_slab \* | *slab* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Reset the maximum memory usage for a slab.

This routine resets the maximum memory usage for the slab *slab* to its current usage.

Parameters
:   | slab | Address of the memory slab |
    | --- | --- |

Return values
:   | 0 | Success |
    | --- | --- |
    | -EINVAL | Memory slab is NULL |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
