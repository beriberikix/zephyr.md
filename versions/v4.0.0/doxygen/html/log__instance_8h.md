---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/log__instance_8h.html
original_path: doxygen/html/log__instance_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_instance.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](log__instance_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [log\_source\_const\_data](structlog__source__const__data.md) |
|  | Constant data associated with the source of log messages. [More...](structlog__source__const__data.md#details) |
| struct | [log\_source\_dynamic\_data](structlog__source__dynamic__data.md) |
|  | Dynamic data associated with the source of log messages. [More...](structlog__source__dynamic__data.md#details) |

| Macros | |
| --- | --- |
| #define | [LOG\_OBJECT\_PTR\_INIT](#a88d644c0d8e7b8985a37dca7f467ad9b)(\_name, \_object) |
|  | Initialize pointer to logger instance with explicitly provided object. |
| #define | [LOG\_INSTANCE\_PTR](#a96ff8eee1b58c6b6025a29608b5113b8)(\_module\_name, \_inst\_name) |
|  | Get pointer to a logging instance. |
| #define | [LOG\_INSTANCE\_PTR\_INIT](#a7389934373419d74129407ffba7ea3e3)(\_name, \_module\_name, \_inst\_name) |
|  | Macro for initializing a pointer to the logger instance. |
| #define | [LOG\_INSTANCE\_PTR\_DECLARE](#a224e4a75dca6d1b363ef49e96730dcfd)(\_name) |
|  | Declare a logger instance pointer in the module structure. |
| #define | [LOG\_INSTANCE\_REGISTER](#ad18f1e8ffbef38f285f70d8005fa144f)(\_module\_name, \_inst\_name, \_level) |
|  | Macro for registering instance for logging with independent filtering. |

## Macro Definition Documentation

## [◆ ](#a96ff8eee1b58c6b6025a29608b5113b8)LOG\_INSTANCE\_PTR

| #define LOG\_INSTANCE\_PTR | ( |  | *\_module\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_inst\_name* ) |

**Value:**

Z\_LOG\_OBJECT\_PTR(Z\_LOG\_INSTANCE\_FULL\_NAME(\_module\_name, \_inst\_name))

Get pointer to a logging instance.

Instance is identified by `_module_name` and `_inst_name`.

Parameters
:   | \_module\_name | Module name. |
    | --- | --- |
    | \_inst\_name | Instance name. |

Returns
:   Pointer to a logging instance.

## [◆ ](#a224e4a75dca6d1b363ef49e96730dcfd)LOG\_INSTANCE\_PTR\_DECLARE

| #define LOG\_INSTANCE\_PTR\_DECLARE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)(CONFIG\_LOG, (Z\_LOG\_INSTANCE\_STRUCT \* \_name), \

(int \_name[[TOOLCHAIN\_HAS\_ZLA](toolchain_8h.md#a90e5fd6ed234d1494c7f156635c2e6e1) ? 0 : 1]))

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:195

[TOOLCHAIN\_HAS\_ZLA](toolchain_8h.md#a90e5fd6ed234d1494c7f156635c2e6e1)

#define TOOLCHAIN\_HAS\_ZLA

Indicate if toolchain supports Zero Length Arrays.

**Definition** toolchain.h:123

Declare a logger instance pointer in the module structure.

If logging is disabled then element in the structure is still declared to avoid compilation issues. If compiler supports zero length arrays then it is utilized to not use any space, else a byte array is created.

Parameters
:   | \_name | Name of a structure element that will have a pointer to logging instance object. |
    | --- | --- |

## [◆ ](#a7389934373419d74129407ffba7ea3e3)LOG\_INSTANCE\_PTR\_INIT

| #define LOG\_INSTANCE\_PTR\_INIT | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_module\_name*, |
|  |  |  | *\_inst\_name* ) |

**Value:**

[LOG\_OBJECT\_PTR\_INIT](#a88d644c0d8e7b8985a37dca7f467ad9b)(\_name, [LOG\_INSTANCE\_PTR](#a96ff8eee1b58c6b6025a29608b5113b8)(\_module\_name, \_inst\_name))

[LOG\_OBJECT\_PTR\_INIT](#a88d644c0d8e7b8985a37dca7f467ad9b)

#define LOG\_OBJECT\_PTR\_INIT(\_name, \_object)

Initialize pointer to logger instance with explicitly provided object.

**Definition** log\_instance.h:81

[LOG\_INSTANCE\_PTR](#a96ff8eee1b58c6b6025a29608b5113b8)

#define LOG\_INSTANCE\_PTR(\_module\_name, \_inst\_name)

Get pointer to a logging instance.

**Definition** log\_instance.h:114

Macro for initializing a pointer to the logger instance.

`_module_name` and `_inst_name` are concatenated to form a name of the object.

Macro is intended to be used in user structure initializer to initialize a field in the structure that holds pointer to the logging instance. Structure field should be declared using `LOG_INSTANCE_PTR_DECLARE`.

Parameters
:   | \_name | Name of a structure element that have a pointer to logging instance object. |
    | --- | --- |
    | \_module\_name | Module name. |
    | \_inst\_name | Instance name. |

## [◆ ](#ad18f1e8ffbef38f285f70d8005fa144f)LOG\_INSTANCE\_REGISTER

| #define LOG\_INSTANCE\_REGISTER | ( |  | *\_module\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_inst\_name*, |
|  |  |  | *\_level* ) |

**Value:**

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(CONFIG\_LOG, (Z\_LOG\_INSTANCE\_REGISTER(\_module\_name, \_inst\_name, \_level)))

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)

#define IF\_ENABLED(\_flag, \_code)

Insert code if \_flag is defined and equals 1.

**Definition** util\_macro.h:239

Macro for registering instance for logging with independent filtering.

Module instance provides filtering of logs on instance level instead of module level. Instance create using this macro can later on be used with [LOG\_INSTANCE\_PTR\_INIT](#a7389934373419d74129407ffba7ea3e3) or referenced by [LOG\_INSTANCE\_PTR](#a96ff8eee1b58c6b6025a29608b5113b8).

Parameters
:   | \_module\_name | Module name. |
    | --- | --- |
    | \_inst\_name | Instance name. |
    | \_level | Initial static filtering. |

## [◆ ](#a88d644c0d8e7b8985a37dca7f467ad9b)LOG\_OBJECT\_PTR\_INIT

| #define LOG\_OBJECT\_PTR\_INIT | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_object* ) |

**Value:**

[IF\_ENABLED](group__sys-util.md#gae67ffe50e848951dbde309ed569ea925)(CONFIG\_LOG, (.\_name = \_object,))

Initialize pointer to logger instance with explicitly provided object.

Macro can be used to initialized a pointer with object that is not unique to the given instance, thus not created with [LOG\_INSTANCE\_REGISTER](#ad18f1e8ffbef38f285f70d8005fa144f).

Parameters
:   | \_name | Name of the structure element for holding logging object. |
    | --- | --- |
    | \_object | Pointer to a logging instance object. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_instance.h](log__instance_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
