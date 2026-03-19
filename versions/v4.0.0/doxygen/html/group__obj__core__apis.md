---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__obj__core__apis.html
original_path: doxygen/html/group__obj__core__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Object Core APIs

[Kernel APIs](group__kernel__apis.md)

| Data Structures | |
| --- | --- |
| struct | [k\_obj\_core\_stats\_desc](structk__obj__core__stats__desc.md) |
|  | Object core statistics descriptor. [More...](structk__obj__core__stats__desc.md#details) |
| struct | [k\_obj\_type](structk__obj__type.md) |
|  | Object type structure. [More...](structk__obj__type.md#details) |
| struct | [k\_obj\_core](structk__obj__core.md) |
|  | Object core structure. [More...](structk__obj__core.md#details) |

| Macros | |
| --- | --- |
| #define | [K\_OBJ\_CORE](#ga2bd0c2c121afc09448926a3648c7d814)(kobj) |
|  | Convert kernel object pointer into its object core pointer. |
| #define | [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
|  | Generate new object type IDs based on a 4 letter string. |
| #define | [K\_OBJ\_TYPE\_CONDVAR\_ID](#gab8d2838ae8064facda465bb9db88e948)   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("COND") |
|  | Condition variable object type. |
| #define | [K\_OBJ\_TYPE\_CPU\_ID](#ga59c569e93e1301903618fa0c53f642ec)   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("CPU\_") |
|  | CPU object type. |
| #define | [K\_OBJ\_TYPE\_EVENT\_ID](#gac6fdf29f93b81f4a868ce39f3ae50c8c)   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("EVNT") |
|  | Event object type. |
| #define | [K\_OBJ\_TYPE\_FIFO\_ID](#ga4eadc00416f1da919c5f49fea028b79f)   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("FIFO") |
|  | FIFO object type. |
| #define | [K\_OBJ\_TYPE\_KERNEL\_ID](#gad2b7452f304d6e27c612941a578cc651)   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("KRNL") |
|  | Kernel object type. |
| #define | [K\_OBJ\_TYPE\_LIFO\_ID](#ga956d61f2af839077adeb67ccd2e15d28)   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("LIFO") |
|  | LIFO object type. |
| #define | [K\_OBJ\_TYPE\_MEM\_BLOCK\_ID](#ga83a03cfe8485b3e005ea2dc20a291115)   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("MBLK") |
|  | Memory block object type. |
| #define | [K\_OBJ\_TYPE\_MBOX\_ID](#ga6ee0890bc9e22a381440a3e156c54f2e)   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("MBOX") |
|  | Mailbox object type. |
| #define | [K\_OBJ\_TYPE\_MEM\_SLAB\_ID](#ga0d84b7ac3f48e2e2d0fcd3bfbeed2519)   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("SLAB") |
|  | Memory slab object type. |
| #define | [K\_OBJ\_TYPE\_MSGQ\_ID](#ga8bf245e4f25c61bb4ec8267b15384feb)   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("MSGQ") |
|  | Message queue object type. |
| #define | [K\_OBJ\_TYPE\_MUTEX\_ID](#gab109845d59689ce64523786ccce9b8c6)   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("MUTX") |
|  | Mutex object type. |
| #define | [K\_OBJ\_TYPE\_PIPE\_ID](#ga36eb538a1bd7f8454a9da42de170d2a9)   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("PIPE") |
|  | Pipe object type. |
| #define | [K\_OBJ\_TYPE\_SEM\_ID](#gad08de0f2f76ad2fe368ed82524bd8335)   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("SEM4") |
|  | Semaphore object type. |
| #define | [K\_OBJ\_TYPE\_STACK\_ID](#gacb41863cbd89368e1204080e6f7f14c2)   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("STCK") |
|  | Stack object type. |
| #define | [K\_OBJ\_TYPE\_THREAD\_ID](#gaf7adb45984ccfb2bbe64b1f8e559f24b)   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("THRD") |
|  | Thread object type. |
| #define | [K\_OBJ\_TYPE\_TIMER\_ID](#ga583ff6ce85756d9aa1b2baf7ac19574f)   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("TIMR") |
|  | Timer object type. |

| Functions | |
| --- | --- |
| struct [k\_obj\_type](structk__obj__type.md) \* | [k\_obj\_type\_find](#ga325c21774af7d3f092dcab17d8f260fd) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) type\_id) |
|  | Find a specific object type by ID. |
| int | [k\_obj\_type\_walk\_locked](#ga1e9a331ca6f3f7bf1f0e3b144b964b9b) (struct [k\_obj\_type](structk__obj__type.md) \*type, int(\*func)(struct [k\_obj\_core](structk__obj__core.md) \*, void \*), void \*data) |
|  | Walk the object type's list of object cores. |
| int | [k\_obj\_type\_walk\_unlocked](#ga4d3da7db72063699b66a54e56cf75e2e) (struct [k\_obj\_type](structk__obj__type.md) \*type, int(\*func)(struct [k\_obj\_core](structk__obj__core.md) \*, void \*), void \*data) |
|  | Walk the object type's list of object cores. |
| void | [k\_obj\_core\_init](#gaf00bc2c3bfa0420f00fe5bf49796b3a0) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, struct [k\_obj\_type](structk__obj__type.md) \*type) |
|  | Initialize the core of the kernel object. |
| void | [k\_obj\_core\_link](#ga6b4a21304216582d7cc16088b00e69bf) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core) |
|  | Link the kernel object to the kernel object type list. |
| void | [k\_obj\_core\_init\_and\_link](#gab1563101ae5f163fcbc06dc17660f9bc) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, struct [k\_obj\_type](structk__obj__type.md) \*type) |
|  | Automatically link the kernel object after initializing it. |
| void | [k\_obj\_core\_unlink](#ga7cb5b22d776880313c91a14583bb5d62) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core) |
|  | Unlink the kernel object from the kernel object type list. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga2bd0c2c121afc09448926a3648c7d814)K\_OBJ\_CORE

| #define K\_OBJ\_CORE | ( |  | *kobj* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[obj_core.h](obj__core_8h.md)>`

**Value:**

(&((kobj)->obj\_core))

Convert kernel object pointer into its object core pointer.

## [◆ ](#gab8d2838ae8064facda465bb9db88e948)K\_OBJ\_TYPE\_CONDVAR\_ID

| #define K\_OBJ\_TYPE\_CONDVAR\_ID   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("COND") |
| --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Condition variable object type.

## [◆ ](#ga59c569e93e1301903618fa0c53f642ec)K\_OBJ\_TYPE\_CPU\_ID

| #define K\_OBJ\_TYPE\_CPU\_ID   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("CPU\_") |
| --- |

`#include <[obj_core.h](obj__core_8h.md)>`

CPU object type.

## [◆ ](#gac6fdf29f93b81f4a868ce39f3ae50c8c)K\_OBJ\_TYPE\_EVENT\_ID

| #define K\_OBJ\_TYPE\_EVENT\_ID   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("EVNT") |
| --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Event object type.

## [◆ ](#ga4eadc00416f1da919c5f49fea028b79f)K\_OBJ\_TYPE\_FIFO\_ID

| #define K\_OBJ\_TYPE\_FIFO\_ID   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("FIFO") |
| --- |

`#include <[obj_core.h](obj__core_8h.md)>`

FIFO object type.

## [◆ ](#gaa02f30cae43a209c0c71a52d52354d3f)K\_OBJ\_TYPE\_ID\_GEN

| #define K\_OBJ\_TYPE\_ID\_GEN | ( |  | *[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[obj_core.h](obj__core_8h.md)>`

**Value:**

(([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)[0] << 24) | ([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)[1] << 16) | ([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)[2] << 8) | ([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)[3]))

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

Generate new object type IDs based on a 4 letter string.

## [◆ ](#gad2b7452f304d6e27c612941a578cc651)K\_OBJ\_TYPE\_KERNEL\_ID

| #define K\_OBJ\_TYPE\_KERNEL\_ID   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("KRNL") |
| --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Kernel object type.

## [◆ ](#ga956d61f2af839077adeb67ccd2e15d28)K\_OBJ\_TYPE\_LIFO\_ID

| #define K\_OBJ\_TYPE\_LIFO\_ID   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("LIFO") |
| --- |

`#include <[obj_core.h](obj__core_8h.md)>`

LIFO object type.

## [◆ ](#ga6ee0890bc9e22a381440a3e156c54f2e)K\_OBJ\_TYPE\_MBOX\_ID

| #define K\_OBJ\_TYPE\_MBOX\_ID   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("MBOX") |
| --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Mailbox object type.

## [◆ ](#ga83a03cfe8485b3e005ea2dc20a291115)K\_OBJ\_TYPE\_MEM\_BLOCK\_ID

| #define K\_OBJ\_TYPE\_MEM\_BLOCK\_ID   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("MBLK") |
| --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Memory block object type.

## [◆ ](#ga0d84b7ac3f48e2e2d0fcd3bfbeed2519)K\_OBJ\_TYPE\_MEM\_SLAB\_ID

| #define K\_OBJ\_TYPE\_MEM\_SLAB\_ID   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("SLAB") |
| --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Memory slab object type.

## [◆ ](#ga8bf245e4f25c61bb4ec8267b15384feb)K\_OBJ\_TYPE\_MSGQ\_ID

| #define K\_OBJ\_TYPE\_MSGQ\_ID   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("MSGQ") |
| --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Message queue object type.

## [◆ ](#gab109845d59689ce64523786ccce9b8c6)K\_OBJ\_TYPE\_MUTEX\_ID

| #define K\_OBJ\_TYPE\_MUTEX\_ID   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("MUTX") |
| --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Mutex object type.

## [◆ ](#ga36eb538a1bd7f8454a9da42de170d2a9)K\_OBJ\_TYPE\_PIPE\_ID

| #define K\_OBJ\_TYPE\_PIPE\_ID   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("PIPE") |
| --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Pipe object type.

## [◆ ](#gad08de0f2f76ad2fe368ed82524bd8335)K\_OBJ\_TYPE\_SEM\_ID

| #define K\_OBJ\_TYPE\_SEM\_ID   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("SEM4") |
| --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Semaphore object type.

## [◆ ](#gacb41863cbd89368e1204080e6f7f14c2)K\_OBJ\_TYPE\_STACK\_ID

| #define K\_OBJ\_TYPE\_STACK\_ID   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("STCK") |
| --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Stack object type.

## [◆ ](#gaf7adb45984ccfb2bbe64b1f8e559f24b)K\_OBJ\_TYPE\_THREAD\_ID

| #define K\_OBJ\_TYPE\_THREAD\_ID   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("THRD") |
| --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Thread object type.

## [◆ ](#ga583ff6ce85756d9aa1b2baf7ac19574f)K\_OBJ\_TYPE\_TIMER\_ID

| #define K\_OBJ\_TYPE\_TIMER\_ID   [K\_OBJ\_TYPE\_ID\_GEN](#gaa02f30cae43a209c0c71a52d52354d3f)("TIMR") |
| --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Timer object type.

## Function Documentation

## [◆ ](#gaf00bc2c3bfa0420f00fe5bf49796b3a0)k\_obj\_core\_init()

| void k\_obj\_core\_init | ( | struct [k\_obj\_core](structk__obj__core.md) \* | *obj\_core*, |
| --- | --- | --- | --- |
|  |  | struct [k\_obj\_type](structk__obj__type.md) \* | *type* ) |

`#include <[obj_core.h](obj__core_8h.md)>`

Initialize the core of the kernel object.

Initializing the kernel object core associates it with the specified kernel object type.

Parameters
:   | obj\_core | Pointer to the kernel object to initialize |
    | --- | --- |
    | type | Pointer to the kernel object type |

## [◆ ](#gab1563101ae5f163fcbc06dc17660f9bc)k\_obj\_core\_init\_and\_link()

| void k\_obj\_core\_init\_and\_link | ( | struct [k\_obj\_core](structk__obj__core.md) \* | *obj\_core*, |
| --- | --- | --- | --- |
|  |  | struct [k\_obj\_type](structk__obj__type.md) \* | *type* ) |

`#include <[obj_core.h](obj__core_8h.md)>`

Automatically link the kernel object after initializing it.

A useful wrapper to both initialize the core of the kernel object and automatically link it into the kernel object type's list of objects.

Parameters
:   | obj\_core | Pointer to the kernel object to initialize |
    | --- | --- |
    | type | Pointer to the kernel object type |

## [◆ ](#ga6b4a21304216582d7cc16088b00e69bf)k\_obj\_core\_link()

| void k\_obj\_core\_link | ( | struct [k\_obj\_core](structk__obj__core.md) \* | *obj\_core* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Link the kernel object to the kernel object type list.

A kernel object can be optionally linked into the kernel object type's list of objects. A kernel object must have been initialized before it can be linked. Linked kernel objects can be traversed and have information extracted from them by system tools.

Parameters
:   | obj\_core | Pointer to the kernel object |
    | --- | --- |

## [◆ ](#ga7cb5b22d776880313c91a14583bb5d62)k\_obj\_core\_unlink()

| void k\_obj\_core\_unlink | ( | struct [k\_obj\_core](structk__obj__core.md) \* | *obj\_core* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Unlink the kernel object from the kernel object type list.

Kernel objects can be unlinked from their respective kernel object type lists. If on a list, it must be done at the end of the kernel object's life cycle.

Parameters
:   | obj\_core | Pointer to the kernel object |
    | --- | --- |

## [◆ ](#ga325c21774af7d3f092dcab17d8f260fd)k\_obj\_type\_find()

| struct [k\_obj\_type](structk__obj__type.md) \* k\_obj\_type\_find | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *type\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Find a specific object type by ID.

Given an object type ID, this function searches for the object type that is associated with the specified type ID *type\_id*.

Parameters
:   | type\_id | Type ID associated with object type |
    | --- | --- |

Return values
:   | NULL | if object type not found |
    | --- | --- |
    | Pointer | to object type if found |

## [◆ ](#ga1e9a331ca6f3f7bf1f0e3b144b964b9b)k\_obj\_type\_walk\_locked()

| int k\_obj\_type\_walk\_locked | ( | struct [k\_obj\_type](structk__obj__type.md) \* | *type*, |
| --- | --- | --- | --- |
|  |  | int(\* | *func*)(struct [k\_obj\_core](structk__obj__core.md) \*, void \*), |
|  |  | void \* | *data* ) |

`#include <[obj_core.h](obj__core_8h.md)>`

Walk the object type's list of object cores.

This function takes a global spinlock and walks the object type's list of object cores and invokes the callback function on each element while holding that lock. Although this will ensure that the list is not modified, one can expect a significant penalty in terms of performance and latency.

The callback function shall either return non-zero to stop further walking, or it shall return 0 to continue walking.

Parameters
:   | type | Pointer to the object type |
    | --- | --- |
    | func | Callback to invoke on each object core of the object type |
    | data | Custom data passed to the callback |

Return values
:   | non-zero | if walk is terminated by the callback; otherwise 0 |
    | --- | --- |

## [◆ ](#ga4d3da7db72063699b66a54e56cf75e2e)k\_obj\_type\_walk\_unlocked()

| int k\_obj\_type\_walk\_unlocked | ( | struct [k\_obj\_type](structk__obj__type.md) \* | *type*, |
| --- | --- | --- | --- |
|  |  | int(\* | *func*)(struct [k\_obj\_core](structk__obj__core.md) \*, void \*), |
|  |  | void \* | *data* ) |

`#include <[obj_core.h](obj__core_8h.md)>`

Walk the object type's list of object cores.

This function is similar to [k\_obj\_type\_walk\_locked()](#ga1e9a331ca6f3f7bf1f0e3b144b964b9b) except that it walks the list without obtaining the global spinlock. No synchronization is provided here. Mutation of the list of objects while this function is in progress must be prevented at the application layer, otherwise undefined/unreliable behavior, corruption and/or crashes may result.

The callback function shall either return non-zero to stop further walking, or it shall return 0 to continue walking.

Parameters
:   | type | Pointer to the object type |
    | --- | --- |
    | func | Callback to invoke on each object core of the object type |
    | data | Custom data passed to the callback |

Return values
:   | non-zero | if walk is terminated by the callback; otherwise 0 |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
