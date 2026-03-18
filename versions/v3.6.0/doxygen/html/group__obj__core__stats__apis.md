---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__obj__core__stats__apis.html
original_path: doxygen/html/group__obj__core__stats__apis.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Object Core Statistics APIs

[Kernel APIs](group__kernel__apis.md)

| Functions | |
| --- | --- |
| int | [k\_obj\_core\_stats\_register](#gae3fda75cf0b9e3c91bfb5ba57239621d) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, void \*stats, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stats\_len) |
|  | Register kernel object for gathering statistics. |
| int | [k\_obj\_core\_stats\_deregister](#gab2b23cf62d89e0bc21d89a0b77b01a21) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core) |
|  | Deregister kernel object from gathering statistics. |
| int | [k\_obj\_core\_stats\_raw](#ga9c5f91bd221b9086ccaea7347ac357ab) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, void \*stats, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stats\_len) |
|  | Retrieve the raw statistics associated with the kernel object. |
| int | [k\_obj\_core\_stats\_query](#ga52afc700fb116acfaa4dd5e1ca49a782) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core, void \*stats, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stats\_len) |
|  | Retrieve the statistics associated with the kernel object. |
| int | [k\_obj\_core\_stats\_reset](#ga0b4d2270e968e2c694290c0f90f208c4) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core) |
|  | Reset the stats associated with the kernel object. |
| int | [k\_obj\_core\_stats\_disable](#ga547b121e75aeafc2f54dba2d58ca62db) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core) |
|  | Stop gathering the stats associated with the kernel object. |
| int | [k\_obj\_core\_stats\_enable](#ga079df60c5ba6dd08a2270362490553fa) (struct [k\_obj\_core](structk__obj__core.md) \*obj\_core) |
|  | Reset the stats associated with the kernel object. |

## Detailed Description

## Function Documentation

## [◆ ](#gab2b23cf62d89e0bc21d89a0b77b01a21)k\_obj\_core\_stats\_deregister()

| int k\_obj\_core\_stats\_deregister | ( | struct [k\_obj\_core](structk__obj__core.md) \* | *obj\_core* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Deregister kernel object from gathering statistics.

Deregistering a kernel object core from gathering statistics prevents it from gathering any more statistics. It is expected to be invoked at the end of a kernel object's life cycle.

Parameters
:   | obj\_core | Pointer to kernel object core |
    | --- | --- |

Return values
:   | 0 | on success |
    | --- | --- |
    | -errno | on failure |

## [◆ ](#ga547b121e75aeafc2f54dba2d58ca62db)k\_obj\_core\_stats\_disable()

| int k\_obj\_core\_stats\_disable | ( | struct [k\_obj\_core](structk__obj__core.md) \* | *obj\_core* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Stop gathering the stats associated with the kernel object.

This function temporarily stops the gathering of statistics associated with the kernel object core specified by *obj\_core*. The gathering of statistics can be resumed by invoking :c:func :[k\_obj\_core\_stats\_enable](#ga079df60c5ba6dd08a2270362490553fa).

Parameters
:   | obj\_core | Pointer to kernel object core |
    | --- | --- |

Return values
:   | 0 | on success |
    | --- | --- |
    | -errno | on failure |

## [◆ ](#ga079df60c5ba6dd08a2270362490553fa)k\_obj\_core\_stats\_enable()

| int k\_obj\_core\_stats\_enable | ( | struct [k\_obj\_core](structk__obj__core.md) \* | *obj\_core* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Reset the stats associated with the kernel object.

This function resumes the gathering of statistics associated with the kernel object core specified by *obj\_core*.

Parameters
:   | obj\_core | Pointer to kernel object core |
    | --- | --- |

Return values
:   | 0 | on success |
    | --- | --- |
    | -errno | on failure |

## [◆ ](#ga52afc700fb116acfaa4dd5e1ca49a782)k\_obj\_core\_stats\_query()

| int k\_obj\_core\_stats\_query | ( | struct [k\_obj\_core](structk__obj__core.md) \* | *obj\_core*, |
| --- | --- | --- | --- |
|  |  | void \* | *stats*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *stats\_len* ) |

`#include <[obj_core.h](obj__core_8h.md)>`

Retrieve the statistics associated with the kernel object.

This function copies the statistics associated with the kernel object core specified by *obj\_core* into the buffer *stats*. Unlike the raw statistics this may report calculated values such as averages. Note that the size of the buffer (*stats\_len*) must match the size specified by the kernel object type's statistics descriptor.

Parameters
:   | obj\_core | Pointer to kernel object core |
    | --- | --- |
    | stats | Pointer to memory buffer into which to copy the queried stats |
    | stats\_len | Length of the memory buffer |

Return values
:   | 0 | on success |
    | --- | --- |
    | -errno | on failure |

## [◆ ](#ga9c5f91bd221b9086ccaea7347ac357ab)k\_obj\_core\_stats\_raw()

| int k\_obj\_core\_stats\_raw | ( | struct [k\_obj\_core](structk__obj__core.md) \* | *obj\_core*, |
| --- | --- | --- | --- |
|  |  | void \* | *stats*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *stats\_len* ) |

`#include <[obj_core.h](obj__core_8h.md)>`

Retrieve the raw statistics associated with the kernel object.

This function copies the raw statistics associated with the kernel object core specified by *obj\_core* into the buffer *stats*. Note that the size of the buffer (*stats\_len*) must match the size specified by the kernel object type's statistics descriptor.

Parameters
:   | obj\_core | Pointer to kernel object core |
    | --- | --- |
    | stats | Pointer to memory buffer into which to copy raw stats |
    | stats\_len | Length of the memory buffer |

Return values
:   | 0 | on success |
    | --- | --- |
    | -errno | on failure |

## [◆ ](#gae3fda75cf0b9e3c91bfb5ba57239621d)k\_obj\_core\_stats\_register()

| int k\_obj\_core\_stats\_register | ( | struct [k\_obj\_core](structk__obj__core.md) \* | *obj\_core*, |
| --- | --- | --- | --- |
|  |  | void \* | *stats*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *stats\_len* ) |

`#include <[obj_core.h](obj__core_8h.md)>`

Register kernel object for gathering statistics.

Before a kernel object can gather statistics, it must be registered to do so. Registering will also automatically enable the kernel object to gather its statistics.

Parameters
:   | obj\_core | Pointer to kernel object core |
    | --- | --- |
    | stats | Pointer to raw kernel statistics |
    | stats\_len | Size of raw kernel statistics buffer |

Return values
:   | 0 | on success |
    | --- | --- |
    | -errno | on failure |

## [◆ ](#ga0b4d2270e968e2c694290c0f90f208c4)k\_obj\_core\_stats\_reset()

| int k\_obj\_core\_stats\_reset | ( | struct [k\_obj\_core](structk__obj__core.md) \* | *obj\_core* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[obj_core.h](obj__core_8h.md)>`

Reset the stats associated with the kernel object.

This function resets the statistics associated with the kernel object core specified by *obj\_core*.

Parameters
:   | obj\_core | Pointer to kernel object core |
    | --- | --- |

Return values
:   | 0 | on success |
    | --- | --- |
    | -errno | on failure |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
