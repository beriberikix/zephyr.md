---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__subsys__tracing__macros.html
original_path: doxygen/html/group__subsys__tracing__macros.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Tracing utility macros

[Operating System Services](group__os__services.md) » [Tracing](group__subsys__tracing.md)

Tracing utility macros.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [SYS\_PORT\_TRACING\_TYPE\_MASK](#ga7c3ff6c93f71cdd1a35e3a656885fb50)(type, trace\_call) |
|  | Checks if an object type should be traced or not. |
| #define | [SYS\_PORT\_TRACING\_FUNC](#gadce691eea44f211b804ce44b51b2e71d)(type, func, ...) |
|  | Tracing macro for function calls which are not directly associated with a specific type of object. |
| #define | [SYS\_PORT\_TRACING\_FUNC\_ENTER](#ga445bcac4cec53d560ddca757de17e1e3)(type, func, ...) |
|  | Tracing macro for the entry into a function that might or might not return a value. |
| #define | [SYS\_PORT\_TRACING\_FUNC\_BLOCKING](#ga17c6029a89e3e1539dbac019dc9ee50b)(type, func, ...) |
|  | Tracing macro for when a function blocks during its execution. |
| #define | [SYS\_PORT\_TRACING\_FUNC\_EXIT](#gab0350eef3ed26733e57505ee2d0487cb)(type, func, ...) |
|  | Tracing macro for when a function ends its execution. |
| #define | [SYS\_PORT\_TRACING\_OBJ\_INIT](#ga19606657deb4b8902314fe11eb8bfb24)(obj\_type, obj, ...) |
|  | Tracing macro for the initialization of an object. |
| #define | [SYS\_PORT\_TRACING\_OBJ\_FUNC](#gaca007b62a20872de436533f26e5b1c55)(obj\_type, func, obj, ...) |
|  | Tracing macro for simple object function calls often without returns or branching. |
| #define | [SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER](#ga4ce3846263099a197c043f25ebe4a253)(obj\_type, func, obj, ...) |
|  | Tracing macro for the entry into a function that might or might not return a value. |
| #define | [SYS\_PORT\_TRACING\_OBJ\_FUNC\_BLOCKING](#ga8e98afd586a77d158acb103b94d9cd3f)(obj\_type, func, obj, timeout, ...) |
|  | Tracing macro for when a function blocks during its execution. |
| #define | [SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT](#ga94bd54c03c68d60e1c0879ce43e08730)(obj\_type, func, obj, ...) |
|  | Tracing macro for when a function ends its execution. |
| #define | [SYS\_PORT\_TRACING\_TRACKING\_FIELD](#ga6d1e443d7db5ecc892c89385547e75ad)(type) |
|  | Field added to kernel objects so they are tracked. |

## Detailed Description

Tracing utility macros.

## Macro Definition Documentation

## [◆ ](#gadce691eea44f211b804ce44b51b2e71d)SYS\_PORT\_TRACING\_FUNC

| #define SYS\_PORT\_TRACING\_FUNC | ( |  | *type*, |
| --- | --- | --- | --- |
|  |  |  | *func*, |
|  |  |  | ... ) |

`#include <[tracing_macros.h](tracing__macros_8h.md)>`

**Value:**

\_SYS\_PORT\_TRACE\_IF\_NOT\_DISABLED(type, \_SYS\_PORT\_TRACING\_FUNC(type, func), \_\_VA\_ARGS\_\_)

Tracing macro for function calls which are not directly associated with a specific type of object.

Parameters
:   | type | Type of tracing event or object type |
    | --- | --- |
    | func | Name of the function responsible for the call. This does not need to exactly match the name of the function but should rather match what the user called in case of system calls etc. That is, we can often omit the z\_vrfy/z\_impl part of the name. |
    | ... | Additional parameters relevant to the tracing call |

## [◆ ](#ga17c6029a89e3e1539dbac019dc9ee50b)SYS\_PORT\_TRACING\_FUNC\_BLOCKING

| #define SYS\_PORT\_TRACING\_FUNC\_BLOCKING | ( |  | *type*, |
| --- | --- | --- | --- |
|  |  |  | *func*, |
|  |  |  | ... ) |

`#include <[tracing_macros.h](tracing__macros_8h.md)>`

**Value:**

\_SYS\_PORT\_TRACE\_IF\_NOT\_DISABLED(type, \_SYS\_PORT\_TRACING\_FUNC\_BLOCKING(type, func), \

\_\_VA\_ARGS\_\_)

Tracing macro for when a function blocks during its execution.

Parameters
:   | type | Type of tracing event or object type |
    | --- | --- |
    | func | Name of the function responsible for the call. This does not need to exactly match the name of the function but should rather match what the user called in case of system calls etc. That is, we can often omit the z\_vrfy/z\_impl part of the name. |
    | ... | Additional parameters relevant to the tracing call |

## [◆ ](#ga445bcac4cec53d560ddca757de17e1e3)SYS\_PORT\_TRACING\_FUNC\_ENTER

| #define SYS\_PORT\_TRACING\_FUNC\_ENTER | ( |  | *type*, |
| --- | --- | --- | --- |
|  |  |  | *func*, |
|  |  |  | ... ) |

`#include <[tracing_macros.h](tracing__macros_8h.md)>`

**Value:**

\_SYS\_PORT\_TRACE\_IF\_NOT\_DISABLED(type, \_SYS\_PORT\_TRACING\_FUNC\_ENTER(type, func), \_\_VA\_ARGS\_\_)

Tracing macro for the entry into a function that might or might not return a value.

Parameters
:   | type | Type of tracing event or object type |
    | --- | --- |
    | func | Name of the function responsible for the call. This does not need to exactly match the name of the function but should rather match what the user called in case of system calls etc. That is, we can often omit the z\_vrfy/z\_impl part of the name. |
    | ... | Additional parameters relevant to the tracing call |

## [◆ ](#gab0350eef3ed26733e57505ee2d0487cb)SYS\_PORT\_TRACING\_FUNC\_EXIT

| #define SYS\_PORT\_TRACING\_FUNC\_EXIT | ( |  | *type*, |
| --- | --- | --- | --- |
|  |  |  | *func*, |
|  |  |  | ... ) |

`#include <[tracing_macros.h](tracing__macros_8h.md)>`

**Value:**

\_SYS\_PORT\_TRACE\_IF\_NOT\_DISABLED(type, \_SYS\_PORT\_TRACING\_FUNC\_EXIT(type, func), \_\_VA\_ARGS\_\_)

Tracing macro for when a function ends its execution.

Potential return values can be given as additional arguments.

Parameters
:   | type | Type of tracing event or object type |
    | --- | --- |
    | func | Name of the function responsible for the call. This does not need to exactly match the name of the function but should rather match what the user called in case of system calls etc. That is, we can often omit the z\_vrfy/z\_impl part of the name. |
    | ... | Additional parameters relevant to the tracing call |

## [◆ ](#gaca007b62a20872de436533f26e5b1c55)SYS\_PORT\_TRACING\_OBJ\_FUNC

| #define SYS\_PORT\_TRACING\_OBJ\_FUNC | ( |  | *obj\_type*, |
| --- | --- | --- | --- |
|  |  |  | *func*, |
|  |  |  | *obj*, |
|  |  |  | ... ) |

`#include <[tracing_macros.h](tracing__macros_8h.md)>`

**Value:**

do { \

SYS\_PORT\_TRACING\_TYPE\_MASK(obj\_type, \

\_SYS\_PORT\_TRACING\_OBJ\_FUNC(obj\_type, func)(obj, ##\_\_VA\_ARGS\_\_)); \

SYS\_PORT\_TRACING\_TYPE\_MASK(obj\_type, \

\_SYS\_PORT\_TRACKING\_OBJ\_FUNC(obj\_type, func)(obj, ##\_\_VA\_ARGS\_\_)); \

} while (false)

Tracing macro for simple object function calls often without returns or branching.

Parameters
:   | obj\_type | The type of object associated with the call ([k\_thread](structk__thread.md "Thread Structure."), k\_sem, [k\_mutex](structk__mutex.md "Mutex Structure.") etc.) |
    | --- | --- |
    | func | Name of the function responsible for the call. This does not need to exactly match the name of the function but should rather match what the user called in case of system calls etc. That is, we can often omit the z\_vrfy/z\_impl part of the name. |
    | obj | Object |
    | ... | Additional parameters relevant to the tracing call |

## [◆ ](#ga8e98afd586a77d158acb103b94d9cd3f)SYS\_PORT\_TRACING\_OBJ\_FUNC\_BLOCKING

| #define SYS\_PORT\_TRACING\_OBJ\_FUNC\_BLOCKING | ( |  | *obj\_type*, |
| --- | --- | --- | --- |
|  |  |  | *func*, |
|  |  |  | *obj*, |
|  |  |  | *timeout*, |
|  |  |  | ... ) |

`#include <[tracing_macros.h](tracing__macros_8h.md)>`

**Value:**

do { \

SYS\_PORT\_TRACING\_TYPE\_MASK(obj\_type, \

\_SYS\_PORT\_TRACING\_OBJ\_FUNC\_BLOCKING(obj\_type, func) \

(obj, timeout, ##\_\_VA\_ARGS\_\_)); \

} while (false)

Tracing macro for when a function blocks during its execution.

Parameters
:   | obj\_type | The type of object associated with the call ([k\_thread](structk__thread.md "Thread Structure."), k\_sem, [k\_mutex](structk__mutex.md "Mutex Structure.") etc.) |
    | --- | --- |
    | func | Name of the function responsible for the call. This does not need to exactly match the name of the function but should rather match what the user called in case of system calls etc. That is, we can often omit the z\_vrfy/z\_impl part of the name. |
    | obj | Object |
    | timeout | Timeout |
    | ... | Additional parameters relevant to the tracing call |

## [◆ ](#ga4ce3846263099a197c043f25ebe4a253)SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER

| #define SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER | ( |  | *obj\_type*, |
| --- | --- | --- | --- |
|  |  |  | *func*, |
|  |  |  | *obj*, |
|  |  |  | ... ) |

`#include <[tracing_macros.h](tracing__macros_8h.md)>`

**Value:**

do { \

SYS\_PORT\_TRACING\_TYPE\_MASK(obj\_type, \

\_SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER(obj\_type, func)(obj, ##\_\_VA\_ARGS\_\_)); \

} while (false)

Tracing macro for the entry into a function that might or might not return a value.

Parameters
:   | obj\_type | The type of object associated with the call ([k\_thread](structk__thread.md "Thread Structure."), k\_sem, [k\_mutex](structk__mutex.md "Mutex Structure.") etc.) |
    | --- | --- |
    | func | Name of the function responsible for the call. This does not need to exactly match the name of the function but should rather match what the user called in case of system calls etc. That is, we can often omit the z\_vrfy/z\_impl part of the name. |
    | obj | Object |
    | ... | Additional parameters relevant to the tracing call |

## [◆ ](#ga94bd54c03c68d60e1c0879ce43e08730)SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT

| #define SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT | ( |  | *obj\_type*, |
| --- | --- | --- | --- |
|  |  |  | *func*, |
|  |  |  | *obj*, |
|  |  |  | ... ) |

`#include <[tracing_macros.h](tracing__macros_8h.md)>`

**Value:**

do { \

SYS\_PORT\_TRACING\_TYPE\_MASK(obj\_type, \

\_SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT(obj\_type, func)(obj, ##\_\_VA\_ARGS\_\_)); \

} while (false)

Tracing macro for when a function ends its execution.

Potential return values can be given as additional arguments.

Parameters
:   | obj\_type | The type of object associated with the call ([k\_thread](structk__thread.md "Thread Structure."), k\_sem, [k\_mutex](structk__mutex.md "Mutex Structure.") etc.) |
    | --- | --- |
    | func | Name of the function responsible for the call. This does not need to exactly match the name of the function but should rather match what the user called in case of system calls etc. That is, we can often omit the z\_vrfy/z\_impl part of the name. |
    | obj | Object |
    | ... | Additional parameters relevant to the tracing call |

## [◆ ](#ga19606657deb4b8902314fe11eb8bfb24)SYS\_PORT\_TRACING\_OBJ\_INIT

| #define SYS\_PORT\_TRACING\_OBJ\_INIT | ( |  | *obj\_type*, |
| --- | --- | --- | --- |
|  |  |  | *obj*, |
|  |  |  | ... ) |

`#include <[tracing_macros.h](tracing__macros_8h.md)>`

**Value:**

do { \

SYS\_PORT\_TRACING\_TYPE\_MASK(obj\_type, \

\_SYS\_PORT\_TRACING\_OBJ\_INIT(obj\_type)(obj, ##\_\_VA\_ARGS\_\_)); \

SYS\_PORT\_TRACING\_TYPE\_MASK(obj\_type, \

\_SYS\_PORT\_TRACKING\_OBJ\_INIT(obj\_type)(obj, ##\_\_VA\_ARGS\_\_)); \

} while (false)

Tracing macro for the initialization of an object.

Parameters
:   | obj\_type | The type of object associated with the call ([k\_thread](structk__thread.md "Thread Structure."), k\_sem, [k\_mutex](structk__mutex.md "Mutex Structure.") etc.) |
    | --- | --- |
    | obj | Object |

## [◆ ](#ga6d1e443d7db5ecc892c89385547e75ad)SYS\_PORT\_TRACING\_TRACKING\_FIELD

| #define SYS\_PORT\_TRACING\_TRACKING\_FIELD | ( |  | *type* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[tracing_macros.h](tracing__macros_8h.md)>`

**Value:**

[SYS\_PORT\_TRACING\_TYPE\_MASK](#ga7c3ff6c93f71cdd1a35e3a656885fb50)(type, struct type \*\_obj\_track\_next;)

[SYS\_PORT\_TRACING\_TYPE\_MASK](#ga7c3ff6c93f71cdd1a35e3a656885fb50)

#define SYS\_PORT\_TRACING\_TYPE\_MASK(type, trace\_call)

Checks if an object type should be traced or not.

**Definition** tracing\_macros.h:210

Field added to kernel objects so they are tracked.

Parameters
:   | type | Type of object being tracked ([k\_thread](structk__thread.md "Thread Structure."), k\_sem, etc.) |
    | --- | --- |

## [◆ ](#ga7c3ff6c93f71cdd1a35e3a656885fb50)SYS\_PORT\_TRACING\_TYPE\_MASK

| #define SYS\_PORT\_TRACING\_TYPE\_MASK | ( |  | *type*, |
| --- | --- | --- | --- |
|  |  |  | *trace\_call* ) |

`#include <[tracing_macros.h](tracing__macros_8h.md)>`

**Value:**

\_SYS\_PORT\_TRACING\_TYPE\_MASK(type)(trace\_call)

Checks if an object type should be traced or not.

Parameters
:   | type | Tracing event type/object |
    | --- | --- |
    | trace\_call | Tracing call |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
