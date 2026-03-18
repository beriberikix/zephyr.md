---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__mem__domain__apis.html
original_path: doxygen/html/group__mem__domain__apis.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Memory domain APIs

[Kernel APIs](group__kernel__apis.md)

| Topics | |
| --- | --- |
|  | [Application memory domain APIs](group__mem__domain__apis__app.md) |
|  | Application memory domain APIs. |

| Data Structures | |
| --- | --- |
| struct | [k\_mem\_partition](structk__mem__partition.md) |
|  | Memory Partition. [More...](structk__mem__partition.md#details) |
| struct | [k\_mem\_domain](structk__mem__domain.md) |
|  | Memory Domain. [More...](structk__mem__domain.md#details) |

| Macros | |
| --- | --- |
| #define | [K\_MEM\_PARTITION\_DEFINE](#ga4360fd595cb3fe3a10b58c12ae2b7ece)(name, start, size, attr) |
|  | Statically declare a memory partition. |

| Functions | |
| --- | --- |
| int | [k\_mem\_domain\_init](#ga8a987bc85c02925685fe87213fe26c5a) (struct [k\_mem\_domain](structk__mem__domain.md) \*domain, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_parts, struct [k\_mem\_partition](structk__mem__partition.md) \*parts[]) |
|  | Initialize a memory domain. |
| int | [k\_mem\_domain\_add\_partition](#ga07da0cf76f8db54373b88d40be63b138) (struct [k\_mem\_domain](structk__mem__domain.md) \*domain, struct [k\_mem\_partition](structk__mem__partition.md) \*part) |
|  | Add a memory partition into a memory domain. |
| int | [k\_mem\_domain\_remove\_partition](#gada4f8ce609d6b720ee88e11544555fc2) (struct [k\_mem\_domain](structk__mem__domain.md) \*domain, struct [k\_mem\_partition](structk__mem__partition.md) \*part) |
|  | Remove a memory partition from a memory domain. |
| int | [k\_mem\_domain\_add\_thread](#ga7b4d6148d9375f020a268961d5afde2d) (struct [k\_mem\_domain](structk__mem__domain.md) \*domain, [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) thread) |
|  | Add a thread into a memory domain. |

| Variables | |
| --- | --- |
| struct [k\_mem\_domain](structk__mem__domain.md) | [k\_mem\_domain\_default](#ga3613abdb546a66059fa3f621a2ebd41a) |
|  | Default memory domain. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga4360fd595cb3fe3a10b58c12ae2b7ece)K\_MEM\_PARTITION\_DEFINE

| #define K\_MEM\_PARTITION\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *start*, |
|  |  |  | *size*, |
|  |  |  | *attr* ) |

`#include <[mem_domain.h](mem__domain_8h.md)>`

**Value:**

struct [k\_mem\_partition](structk__mem__partition.md) name =\

{ ([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808))start, size, attr}

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[k\_mem\_partition](structk__mem__partition.md)

Memory Partition.

**Definition** mem\_domain.h:55

Statically declare a memory partition.

## Function Documentation

## [◆ ](#ga07da0cf76f8db54373b88d40be63b138)k\_mem\_domain\_add\_partition()

| int k\_mem\_domain\_add\_partition | ( | struct [k\_mem\_domain](structk__mem__domain.md) \* | *domain*, |
| --- | --- | --- | --- |
|  |  | struct [k\_mem\_partition](structk__mem__partition.md) \* | *part* ) |

`#include <[mem_domain.h](mem__domain_8h.md)>`

Add a memory partition into a memory domain.

Add a memory partition into a memory domain. Partitions must conform to the following constraints:

- Partitions in the same memory domain may not overlap each other.
- Partitions must not be defined which expose private kernel data structures or kernel objects.
- The starting address alignment, and the partition size must conform to the constraints of the underlying memory management hardware, which varies per architecture.
- Memory domain partitions are only intended to control access to memory from user mode threads.
- If CONFIG\_EXECUTE\_XOR\_WRITE is enabled, the partition must not allow both writes and execution.

Violating these constraints may lead to CPU exceptions or undefined behavior.

Parameters
:   | domain | The memory domain to be added a memory partition. |
    | --- | --- |
    | part | The memory partition to be added |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -EINVAL | if invalid parameters supplied |
    | -ENOSPC | if no free partition slots available |

## [◆ ](#ga7b4d6148d9375f020a268961d5afde2d)k\_mem\_domain\_add\_thread()

| int k\_mem\_domain\_add\_thread | ( | struct [k\_mem\_domain](structk__mem__domain.md) \* | *domain*, |
| --- | --- | --- | --- |
|  |  | [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) | *thread* ) |

`#include <[mem_domain.h](mem__domain_8h.md)>`

Add a thread into a memory domain.

Add a thread into a memory domain. It will be removed from whatever memory domain it previously belonged to.

Parameters
:   | domain | The memory domain that the thread is going to be added into. |
    | --- | --- |
    | thread | ID of thread going to be added into the memory domain. |

Returns
:   0 if successful, fails otherwise.

## [◆ ](#ga8a987bc85c02925685fe87213fe26c5a)k\_mem\_domain\_init()

| int k\_mem\_domain\_init | ( | struct [k\_mem\_domain](structk__mem__domain.md) \* | *domain*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_parts*, |
|  |  | struct [k\_mem\_partition](structk__mem__partition.md) \* | *parts*[] ) |

`#include <[mem_domain.h](mem__domain_8h.md)>`

Initialize a memory domain.

Initialize a memory domain with given name and memory partitions.

See documentation for [k\_mem\_domain\_add\_partition()](#ga07da0cf76f8db54373b88d40be63b138) for details about partition constraints.

Do not call [k\_mem\_domain\_init()](#ga8a987bc85c02925685fe87213fe26c5a) on the same memory domain more than once, doing so is undefined behavior.

Parameters
:   | domain | The memory domain to be initialized. |
    | --- | --- |
    | num\_parts | The number of array items of "parts" parameter. |
    | parts | An array of pointers to the memory partitions. Can be NULL if num\_parts is zero. |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -EINVAL | if invalid parameters supplied |
    | -ENOMEM | if insufficient memory |

## [◆ ](#gada4f8ce609d6b720ee88e11544555fc2)k\_mem\_domain\_remove\_partition()

| int k\_mem\_domain\_remove\_partition | ( | struct [k\_mem\_domain](structk__mem__domain.md) \* | *domain*, |
| --- | --- | --- | --- |
|  |  | struct [k\_mem\_partition](structk__mem__partition.md) \* | *part* ) |

`#include <[mem_domain.h](mem__domain_8h.md)>`

Remove a memory partition from a memory domain.

Remove a memory partition from a memory domain.

Parameters
:   | domain | The memory domain to be removed a memory partition. |
    | --- | --- |
    | part | The memory partition to be removed |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -EINVAL | if invalid parameters supplied |
    | -ENOENT | if no matching partition found |

## Variable Documentation

## [◆ ](#ga3613abdb546a66059fa3f621a2ebd41a)k\_mem\_domain\_default

| | struct [k\_mem\_domain](structk__mem__domain.md) k\_mem\_domain\_default | | --- | | extern |
| --- | --- | --- |

`#include <[mem_domain.h](mem__domain_8h.md)>`

Default memory domain.

All threads are a member of some memory domain, even if running in supervisor mode. Threads belong to this default memory domain if they haven't been added to or inherited membership from some other domain.

This memory domain has the z\_libc\_partition partition for the C library added to it if exists.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
