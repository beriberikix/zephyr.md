---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/tracing__macros_8h.html
original_path: doxygen/html/tracing__macros_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tracing\_macros.h File Reference

`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`

[Go to the source code of this file.](tracing__macros_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SYS\_PORT\_TRACING\_TYPE\_MASK](group__subsys__tracing__macros.md#ga7c3ff6c93f71cdd1a35e3a656885fb50)(type, trace\_call) |
|  | Checks if an object type should be traced or not. |
| #define | [SYS\_PORT\_TRACING\_FUNC](group__subsys__tracing__macros.md#gadce691eea44f211b804ce44b51b2e71d)(type, func, ...) |
|  | Tracing macro for function calls which are not directly associated with a specific type of object. |
| #define | [SYS\_PORT\_TRACING\_FUNC\_ENTER](group__subsys__tracing__macros.md#ga445bcac4cec53d560ddca757de17e1e3)(type, func, ...) |
|  | Tracing macro for the entry into a function that might or might not return a value. |
| #define | [SYS\_PORT\_TRACING\_FUNC\_BLOCKING](group__subsys__tracing__macros.md#ga17c6029a89e3e1539dbac019dc9ee50b)(type, func, ...) |
|  | Tracing macro for when a function blocks during its execution. |
| #define | [SYS\_PORT\_TRACING\_FUNC\_EXIT](group__subsys__tracing__macros.md#gab0350eef3ed26733e57505ee2d0487cb)(type, func, ...) |
|  | Tracing macro for when a function ends its execution. |
| #define | [SYS\_PORT\_TRACING\_OBJ\_INIT](group__subsys__tracing__macros.md#ga19606657deb4b8902314fe11eb8bfb24)(obj\_type, obj, ...) |
|  | Tracing macro for the initialization of an object. |
| #define | [SYS\_PORT\_TRACING\_OBJ\_FUNC](group__subsys__tracing__macros.md#gaca007b62a20872de436533f26e5b1c55)(obj\_type, func, obj, ...) |
|  | Tracing macro for simple object function calls often without returns or branching. |
| #define | [SYS\_PORT\_TRACING\_OBJ\_FUNC\_ENTER](group__subsys__tracing__macros.md#ga4ce3846263099a197c043f25ebe4a253)(obj\_type, func, obj, ...) |
|  | Tracing macro for the entry into a function that might or might not return a value. |
| #define | [SYS\_PORT\_TRACING\_OBJ\_FUNC\_BLOCKING](group__subsys__tracing__macros.md#ga8e98afd586a77d158acb103b94d9cd3f)(obj\_type, func, obj, timeout, ...) |
|  | Tracing macro for when a function blocks during its execution. |
| #define | [SYS\_PORT\_TRACING\_OBJ\_FUNC\_EXIT](group__subsys__tracing__macros.md#ga94bd54c03c68d60e1c0879ce43e08730)(obj\_type, func, obj, ...) |
|  | Tracing macro for when a function ends its execution. |
| #define | [SYS\_PORT\_TRACING\_TRACKING\_FIELD](group__subsys__tracing__macros.md#ga6d1e443d7db5ecc892c89385547e75ad)(type) |
|  | Field added to kernel objects so they are tracked. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [tracing](dir_c5f5a3ad31e756e37640fc6557a06392.md)
- [tracing\_macros.h](tracing__macros_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
