---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__log__api.html
original_path: doxygen/html/group__log__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Logging API

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md)

Logger API.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [LOG\_ERR](#gad6db28c61c838c1f7316417e1e4847f2)(...) |
|  | Writes an ERROR level message to the log. |
| #define | [LOG\_WRN](#ga644db4299681d9ebf06f8745ad984c65)(...) |
|  | Writes a WARNING level message to the log. |
| #define | [LOG\_INF](#ga9c338f3170acf38a8532d1181d26704e)(...) |
|  | Writes an INFO level message to the log. |
| #define | [LOG\_DBG](#gafb97e6291db24665313453d192941330)(...) |
|  | Writes a DEBUG level message to the log. |
| #define | [LOG\_WRN\_ONCE](#gaa9b22a7d4659030d9a3273f1f1e6786c)(...) |
|  | Writes a WARNING level message to the log on the first execution only. |
| #define | [LOG\_PRINTK](#ga4ab5cae247b853bf9f4f0bf761c1c71e)(...) |
|  | Unconditionally print raw log message. |
| #define | [LOG\_RAW](#ga7dedf58739648ed9b9aef1abe982f7d6)(...) |
|  | Unconditionally print raw log message. |
| #define | [LOG\_INST\_ERR](#ga830f32743847c52e01a510ab0716fe90)(\_log\_inst, ...) |
|  | Writes an ERROR level message associated with the instance to the log. |
| #define | [LOG\_INST\_WRN](#ga76057f789dfc164adbb1dbc9f3aff417)(\_log\_inst, ...) |
|  | Writes a WARNING level message associated with the instance to the log. |
| #define | [LOG\_INST\_INF](#ga222c5b535fb3ecb36dea97885c794188)(\_log\_inst, ...) |
|  | Writes an INFO level message associated with the instance to the log. |
| #define | [LOG\_INST\_DBG](#gae10014012020ea5a6b9a86a5224f19b0)(\_log\_inst, ...) |
|  | Writes a DEBUG level message associated with the instance to the log. |
| #define | [LOG\_HEXDUMP\_ERR](#gabdae4f5b8b16804b53f83a85c3023134)(\_data, \_length, \_str) |
|  | Writes an ERROR level hexdump message to the log. |
| #define | [LOG\_HEXDUMP\_WRN](#gaf73802661fea926bb2b7e628727cdceb)(\_data, \_length, \_str) |
|  | Writes a WARNING level message to the log. |
| #define | [LOG\_HEXDUMP\_INF](#ga8e060bbe660c246a38adccd873e58c6c)(\_data, \_length, \_str) |
|  | Writes an INFO level message to the log. |
| #define | [LOG\_HEXDUMP\_DBG](#ga01dda8273f7d453a855542a52524dca8)(\_data, \_length, \_str) |
|  | Writes a DEBUG level message to the log. |
| #define | [LOG\_INST\_HEXDUMP\_ERR](#gaf2f504a779917dc0f40767cba9f940b9)(\_log\_inst, \_data, \_length, \_str) |
|  | Writes an ERROR hexdump message associated with the instance to the log. |
| #define | [LOG\_INST\_HEXDUMP\_WRN](#gab6542651f88fbb0991fb2339102b52a5)(\_log\_inst, \_data, \_length, \_str) |
|  | Writes a WARNING level hexdump message associated with the instance to the log. |
| #define | [LOG\_INST\_HEXDUMP\_INF](#ga8e38c461c6058ee604b4dddad662d4ca)(\_log\_inst, \_data, \_length, \_str) |
|  | Writes an INFO level hexdump message associated with the instance to the log. |
| #define | [LOG\_INST\_HEXDUMP\_DBG](#ga4b73e6d51cff26ea5595df8680c00563)(\_log\_inst, \_data, \_length, \_str) |
|  | Writes a DEBUG level hexdump message associated with the instance to the log. |
| #define | [LOG\_MODULE\_REGISTER](#ga2404243df68fb6e51129d1c7ecc5ca45)(...) |
|  | Create module-specific state and register the module with Logger. |
| #define | [LOG\_MODULE\_DECLARE](#ga8193b0e10e5ee64b86848bb52be31869)(...) |
|  | Macro for declaring a log module (not registering it). |
| #define | [LOG\_LEVEL\_SET](#gac396852328a77360a0c27dbf7b52356e)(level) |
|  | Macro for setting log level in the file or function where instance logging API is used. |

## Detailed Description

Logger API.

## Macro Definition Documentation

## [◆ ](#gafb97e6291db24665313453d192941330)LOG\_DBG

| #define LOG\_DBG | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log.h](log_8h.md)>`

**Value:**

Z\_LOG([LOG\_LEVEL\_DBG](log__core_8h.md#ad1f7d41b1af28ba81ea63d24c9b690cc), \_\_VA\_ARGS\_\_)

[LOG\_LEVEL\_DBG](log__core_8h.md#ad1f7d41b1af28ba81ea63d24c9b690cc)

#define LOG\_LEVEL\_DBG

**Definition** log\_core.h:23

Writes a DEBUG level message to the log.

It's meant to write developer oriented information.

Parameters
:   | ... | A string optionally containing printk valid conversion specifier, followed by as many values as specifiers. |
    | --- | --- |

## [◆ ](#gad6db28c61c838c1f7316417e1e4847f2)LOG\_ERR

| #define LOG\_ERR | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log.h](log_8h.md)>`

**Value:**

Z\_LOG([LOG\_LEVEL\_ERR](log__core_8h.md#ab3a03740685cbdaa375e2bde8247fdc6), \_\_VA\_ARGS\_\_)

[LOG\_LEVEL\_ERR](log__core_8h.md#ab3a03740685cbdaa375e2bde8247fdc6)

#define LOG\_LEVEL\_ERR

**Definition** log\_core.h:20

Writes an ERROR level message to the log.

It's meant to report severe errors, such as those from which it's not possible to recover.

Parameters
:   | ... | A string optionally containing printk valid conversion specifier, followed by as many values as specifiers. |
    | --- | --- |

## [◆ ](#ga01dda8273f7d453a855542a52524dca8)LOG\_HEXDUMP\_DBG

| #define LOG\_HEXDUMP\_DBG | ( |  | *\_data*, |
| --- | --- | --- | --- |
|  |  |  | *\_length*, |
|  |  |  | *\_str* ) |

`#include <[log.h](log_8h.md)>`

**Value:**

Z\_LOG\_HEXDUMP([LOG\_LEVEL\_DBG](log__core_8h.md#ad1f7d41b1af28ba81ea63d24c9b690cc), \_data, \_length, (\_str))

Writes a DEBUG level message to the log.

It's meant to write developer oriented information.

Parameters
:   | \_data | Pointer to the data to be logged. |
    | --- | --- |
    | \_length | Length of data (in bytes). |
    | \_str | Persistent, raw string. |

## [◆ ](#gabdae4f5b8b16804b53f83a85c3023134)LOG\_HEXDUMP\_ERR

| #define LOG\_HEXDUMP\_ERR | ( |  | *\_data*, |
| --- | --- | --- | --- |
|  |  |  | *\_length*, |
|  |  |  | *\_str* ) |

`#include <[log.h](log_8h.md)>`

**Value:**

Z\_LOG\_HEXDUMP([LOG\_LEVEL\_ERR](log__core_8h.md#ab3a03740685cbdaa375e2bde8247fdc6), \_data, \_length, (\_str))

Writes an ERROR level hexdump message to the log.

It's meant to report severe errors, such as those from which it's not possible to recover.

Parameters
:   | \_data | Pointer to the data to be logged. |
    | --- | --- |
    | \_length | Length of data (in bytes). |
    | \_str | Persistent, raw string. |

## [◆ ](#ga8e060bbe660c246a38adccd873e58c6c)LOG\_HEXDUMP\_INF

| #define LOG\_HEXDUMP\_INF | ( |  | *\_data*, |
| --- | --- | --- | --- |
|  |  |  | *\_length*, |
|  |  |  | *\_str* ) |

`#include <[log.h](log_8h.md)>`

**Value:**

Z\_LOG\_HEXDUMP([LOG\_LEVEL\_INF](log__core_8h.md#a281bc2ce5315e6fae369796c0fdf5c1d), \_data, \_length, (\_str))

[LOG\_LEVEL\_INF](log__core_8h.md#a281bc2ce5315e6fae369796c0fdf5c1d)

#define LOG\_LEVEL\_INF

**Definition** log\_core.h:22

Writes an INFO level message to the log.

It's meant to write generic user oriented messages.

Parameters
:   | \_data | Pointer to the data to be logged. |
    | --- | --- |
    | \_length | Length of data (in bytes). |
    | \_str | Persistent, raw string. |

## [◆ ](#gaf73802661fea926bb2b7e628727cdceb)LOG\_HEXDUMP\_WRN

| #define LOG\_HEXDUMP\_WRN | ( |  | *\_data*, |
| --- | --- | --- | --- |
|  |  |  | *\_length*, |
|  |  |  | *\_str* ) |

`#include <[log.h](log_8h.md)>`

**Value:**

Z\_LOG\_HEXDUMP([LOG\_LEVEL\_WRN](log__core_8h.md#a54f5db1327d9fdbaecbb03a6969de97b), \_data, \_length, (\_str))

[LOG\_LEVEL\_WRN](log__core_8h.md#a54f5db1327d9fdbaecbb03a6969de97b)

#define LOG\_LEVEL\_WRN

**Definition** log\_core.h:21

Writes a WARNING level message to the log.

It's meant to register messages related to unusual situations that are not necessarily errors.

Parameters
:   | \_data | Pointer to the data to be logged. |
    | --- | --- |
    | \_length | Length of data (in bytes). |
    | \_str | Persistent, raw string. |

## [◆ ](#ga9c338f3170acf38a8532d1181d26704e)LOG\_INF

| #define LOG\_INF | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log.h](log_8h.md)>`

**Value:**

Z\_LOG([LOG\_LEVEL\_INF](log__core_8h.md#a281bc2ce5315e6fae369796c0fdf5c1d), \_\_VA\_ARGS\_\_)

Writes an INFO level message to the log.

It's meant to write generic user oriented messages.

Parameters
:   | ... | A string optionally containing printk valid conversion specifier, followed by as many values as specifiers. |
    | --- | --- |

## [◆ ](#gae10014012020ea5a6b9a86a5224f19b0)LOG\_INST\_DBG

| #define LOG\_INST\_DBG | ( |  | *\_log\_inst*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[log.h](log_8h.md)>`

**Value:**

Z\_LOG\_INSTANCE([LOG\_LEVEL\_DBG](log__core_8h.md#ad1f7d41b1af28ba81ea63d24c9b690cc), \_log\_inst, \_\_VA\_ARGS\_\_)

Writes a DEBUG level message associated with the instance to the log.

Message is associated with specific instance of the module which has independent filtering settings (if runtime filtering is enabled) and message prefix (<module\_name>.<instance\_name>). It's meant to write developer oriented information.

Parameters
:   | \_log\_inst | Pointer to the log structure associated with the instance. |
    | --- | --- |
    | ... | A string optionally containing printk valid conversion specifier, followed by as many values as specifiers. |

## [◆ ](#ga830f32743847c52e01a510ab0716fe90)LOG\_INST\_ERR

| #define LOG\_INST\_ERR | ( |  | *\_log\_inst*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[log.h](log_8h.md)>`

**Value:**

Z\_LOG\_INSTANCE([LOG\_LEVEL\_ERR](log__core_8h.md#ab3a03740685cbdaa375e2bde8247fdc6), \_log\_inst, \_\_VA\_ARGS\_\_)

Writes an ERROR level message associated with the instance to the log.

Message is associated with specific instance of the module which has independent filtering settings (if runtime filtering is enabled) and message prefix (<module\_name>.<instance\_name>). It's meant to report severe errors, such as those from which it's not possible to recover.

Parameters
:   | \_log\_inst | Pointer to the log structure associated with the instance. |
    | --- | --- |
    | ... | A string optionally containing printk valid conversion specifier, followed by as many values as specifiers. |

## [◆ ](#ga4b73e6d51cff26ea5595df8680c00563)LOG\_INST\_HEXDUMP\_DBG

| #define LOG\_INST\_HEXDUMP\_DBG | ( |  | *\_log\_inst*, |
| --- | --- | --- | --- |
|  |  |  | *\_data*, |
|  |  |  | *\_length*, |
|  |  |  | *\_str* ) |

`#include <[log.h](log_8h.md)>`

**Value:**

Z\_LOG\_HEXDUMP\_INSTANCE([LOG\_LEVEL\_DBG](log__core_8h.md#ad1f7d41b1af28ba81ea63d24c9b690cc), \_log\_inst, \_data, \_length, \_str)

Writes a DEBUG level hexdump message associated with the instance to the log.

It's meant to write developer oriented information.

Parameters
:   | \_log\_inst | Pointer to the log structure associated with the instance. |
    | --- | --- |
    | \_data | Pointer to the data to be logged. |
    | \_length | Length of data (in bytes). |
    | \_str | Persistent, raw string. |

## [◆ ](#gaf2f504a779917dc0f40767cba9f940b9)LOG\_INST\_HEXDUMP\_ERR

| #define LOG\_INST\_HEXDUMP\_ERR | ( |  | *\_log\_inst*, |
| --- | --- | --- | --- |
|  |  |  | *\_data*, |
|  |  |  | *\_length*, |
|  |  |  | *\_str* ) |

`#include <[log.h](log_8h.md)>`

**Value:**

Z\_LOG\_HEXDUMP\_INSTANCE([LOG\_LEVEL\_ERR](log__core_8h.md#ab3a03740685cbdaa375e2bde8247fdc6), \_log\_inst, \_data, \_length, \_str)

Writes an ERROR hexdump message associated with the instance to the log.

Message is associated with specific instance of the module which has independent filtering settings (if runtime filtering is enabled) and message prefix (<module\_name>.<instance\_name>). It's meant to report severe errors, such as those from which it's not possible to recover.

Parameters
:   | \_log\_inst | Pointer to the log structure associated with the instance. |
    | --- | --- |
    | \_data | Pointer to the data to be logged. |
    | \_length | Length of data (in bytes). |
    | \_str | Persistent, raw string. |

## [◆ ](#ga8e38c461c6058ee604b4dddad662d4ca)LOG\_INST\_HEXDUMP\_INF

| #define LOG\_INST\_HEXDUMP\_INF | ( |  | *\_log\_inst*, |
| --- | --- | --- | --- |
|  |  |  | *\_data*, |
|  |  |  | *\_length*, |
|  |  |  | *\_str* ) |

`#include <[log.h](log_8h.md)>`

**Value:**

Z\_LOG\_HEXDUMP\_INSTANCE([LOG\_LEVEL\_INF](log__core_8h.md#a281bc2ce5315e6fae369796c0fdf5c1d), \_log\_inst, \_data, \_length, \_str)

Writes an INFO level hexdump message associated with the instance to the log.

It's meant to write generic user oriented messages.

Parameters
:   | \_log\_inst | Pointer to the log structure associated with the instance. |
    | --- | --- |
    | \_data | Pointer to the data to be logged. |
    | \_length | Length of data (in bytes). |
    | \_str | Persistent, raw string. |

## [◆ ](#gab6542651f88fbb0991fb2339102b52a5)LOG\_INST\_HEXDUMP\_WRN

| #define LOG\_INST\_HEXDUMP\_WRN | ( |  | *\_log\_inst*, |
| --- | --- | --- | --- |
|  |  |  | *\_data*, |
|  |  |  | *\_length*, |
|  |  |  | *\_str* ) |

`#include <[log.h](log_8h.md)>`

**Value:**

Z\_LOG\_HEXDUMP\_INSTANCE([LOG\_LEVEL\_WRN](log__core_8h.md#a54f5db1327d9fdbaecbb03a6969de97b), \_log\_inst, \_data, \_length, \_str)

Writes a WARNING level hexdump message associated with the instance to the log.

It's meant to register messages related to unusual situations that are not necessarily errors.

Parameters
:   | \_log\_inst | Pointer to the log structure associated with the instance. |
    | --- | --- |
    | \_data | Pointer to the data to be logged. |
    | \_length | Length of data (in bytes). |
    | \_str | Persistent, raw string. |

## [◆ ](#ga222c5b535fb3ecb36dea97885c794188)LOG\_INST\_INF

| #define LOG\_INST\_INF | ( |  | *\_log\_inst*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[log.h](log_8h.md)>`

**Value:**

Z\_LOG\_INSTANCE([LOG\_LEVEL\_INF](log__core_8h.md#a281bc2ce5315e6fae369796c0fdf5c1d), \_log\_inst, \_\_VA\_ARGS\_\_)

Writes an INFO level message associated with the instance to the log.

Message is associated with specific instance of the module which has independent filtering settings (if runtime filtering is enabled) and message prefix (<module\_name>.<instance\_name>). It's meant to write generic user oriented messages.

Parameters
:   | \_log\_inst | Pointer to the log structure associated with the instance. |
    | --- | --- |
    | ... | A string optionally containing printk valid conversion specifier, followed by as many values as specifiers. |

## [◆ ](#ga76057f789dfc164adbb1dbc9f3aff417)LOG\_INST\_WRN

| #define LOG\_INST\_WRN | ( |  | *\_log\_inst*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[log.h](log_8h.md)>`

**Value:**

Z\_LOG\_INSTANCE([LOG\_LEVEL\_WRN](log__core_8h.md#a54f5db1327d9fdbaecbb03a6969de97b), \_log\_inst, \_\_VA\_ARGS\_\_)

Writes a WARNING level message associated with the instance to the log.

Message is associated with specific instance of the module which has independent filtering settings (if runtime filtering is enabled) and message prefix (<module\_name>.<instance\_name>). It's meant to register messages related to unusual situations that are not necessarily errors.

Parameters
:   | \_log\_inst | Pointer to the log structure associated with the instance. |
    | --- | --- |
    | ... | A string optionally containing printk valid conversion specifier, followed by as many values as specifiers. |

## [◆ ](#gac396852328a77360a0c27dbf7b52356e)LOG\_LEVEL\_SET

| #define LOG\_LEVEL\_SET | ( |  | *level* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log.h](log_8h.md)>`

**Value:**

static const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_\_log\_level \_\_unused = \

Z\_LOG\_RESOLVED\_LEVEL(level, 0)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

Macro for setting log level in the file or function where instance logging API is used.

Parameters
:   | level | Level used in file or in function. |
    | --- | --- |

## [◆ ](#ga8193b0e10e5ee64b86848bb52be31869)LOG\_MODULE\_DECLARE

| #define LOG\_MODULE\_DECLARE | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log.h](log_8h.md)>`

**Value:**

extern const struct [log\_source\_const\_data](structlog__source__const__data.md) \

Z\_LOG\_ITEM\_CONST\_DATA([GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)(1, \_\_VA\_ARGS\_\_)); \

extern struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md) \

[LOG\_ITEM\_DYNAMIC\_DATA](log__core_8h.md#a86c2e55bace38c6e71b4d1d0736b1160)([GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)(1, \_\_VA\_ARGS\_\_)); \

\

static const struct [log\_source\_const\_data](structlog__source__const__data.md) \* \

\_\_log\_current\_const\_data \_\_unused = \

Z\_DO\_LOG\_MODULE\_REGISTER(\_\_VA\_ARGS\_\_) ? \

&Z\_LOG\_ITEM\_CONST\_DATA([GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)(1, \_\_VA\_ARGS\_\_)) : \

NULL; \

\

static struct [log\_source\_dynamic\_data](structlog__source__dynamic__data.md) \* \

\_\_log\_current\_dynamic\_data \_\_unused = \

(Z\_DO\_LOG\_MODULE\_REGISTER(\_\_VA\_ARGS\_\_) && \

IS\_ENABLED(CONFIG\_LOG\_RUNTIME\_FILTERING)) ? \

&[LOG\_ITEM\_DYNAMIC\_DATA](log__core_8h.md#a86c2e55bace38c6e71b4d1d0736b1160)([GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)(1, \_\_VA\_ARGS\_\_)) : \

NULL; \

\

static const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \_\_log\_level \_\_unused = \

\_LOG\_LEVEL\_RESOLVE(\_\_VA\_ARGS\_\_)

[GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)

#define GET\_ARG\_N(N,...)

Get nth argument from argument list.

**Definition** util\_macro.h:355

[LOG\_ITEM\_DYNAMIC\_DATA](log__core_8h.md#a86c2e55bace38c6e71b4d1d0736b1160)

#define LOG\_ITEM\_DYNAMIC\_DATA(\_name)

Creates name of variable and section for runtime log data.

**Definition** log\_core.h:478

[log\_source\_const\_data](structlog__source__const__data.md)

Constant data associated with the source of log messages.

**Definition** log\_instance.h:17

[log\_source\_dynamic\_data](structlog__source__dynamic__data.md)

Dynamic data associated with the source of log messages.

**Definition** log\_instance.h:30

Macro for declaring a log module (not registering it).

Modules which are split up over multiple files must have exactly one file use [LOG\_MODULE\_REGISTER()](#ga2404243df68fb6e51129d1c7ecc5ca45) to create module-specific state and register the module with the logger core.

The other files in the module should use this macro instead to declare that same state. (Otherwise, [LOG\_INF()](#ga9c338f3170acf38a8532d1181d26704e) etc. will not be able to refer to module-specific state variables.)

Macro accepts one or two parameters:

- module name
- optional log level. If not provided then default log level is used in the file.

Example usage:

- [LOG\_MODULE\_DECLARE(foo, CONFIG\_FOO\_LOG\_LEVEL)](#ga8193b0e10e5ee64b86848bb52be31869)
- [LOG\_MODULE\_DECLARE(foo)](#ga8193b0e10e5ee64b86848bb52be31869)

Note
:   The module's state is declared only if LOG\_LEVEL for the current source file is non-zero or it is not defined and CONFIG\_LOG\_DEFAULT\_LEVEL is non-zero. In other cases, this macro has no effect.

See also
:   [LOG\_MODULE\_REGISTER](#ga2404243df68fb6e51129d1c7ecc5ca45)

## [◆ ](#ga2404243df68fb6e51129d1c7ecc5ca45)LOG\_MODULE\_REGISTER

| #define LOG\_MODULE\_REGISTER | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log.h](log_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)( \

Z\_DO\_LOG\_MODULE\_REGISTER(\_\_VA\_ARGS\_\_), \

(\_LOG\_MODULE\_DATA\_CREATE([GET\_ARG\_N](group__sys-util.md#gabbe04a4d59a495b2b86196304b937ec6)(1, \_\_VA\_ARGS\_\_), \

\_LOG\_LEVEL\_RESOLVE(\_\_VA\_ARGS\_\_))),\

() \

) \

LOG\_MODULE\_DECLARE(\_\_VA\_ARGS\_\_)

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:179

Create module-specific state and register the module with Logger.

This macro normally must be used after including <[zephyr/logging/log.h](log_8h.md)> to complete the initialization of the module.

Module registration can be skipped in two cases:

- The module consists of more than one file, and another file invokes this macro. ([LOG\_MODULE\_DECLARE()](#ga8193b0e10e5ee64b86848bb52be31869) should be used instead in all of the module's other files.)
- Instance logging is used and there is no need to create module entry. In that case [LOG\_LEVEL\_SET()](#gac396852328a77360a0c27dbf7b52356e) should be used to set log level used within the file.

Macro accepts one or two parameters:

- module name
- optional log level. If not provided then default log level is used in the file.

Example usage:

- [LOG\_MODULE\_REGISTER(foo, CONFIG\_FOO\_LOG\_LEVEL)](#ga2404243df68fb6e51129d1c7ecc5ca45)
- [LOG\_MODULE\_REGISTER(foo)](#ga2404243df68fb6e51129d1c7ecc5ca45)

Note
:   The module's state is defined, and the module is registered, only if LOG\_LEVEL for the current source file is non-zero or it is not defined and CONFIG\_LOG\_DEFAULT\_LEVEL is non-zero. In other cases, this macro has no effect.

See also
:   [LOG\_MODULE\_DECLARE](#ga8193b0e10e5ee64b86848bb52be31869)

## [◆ ](#ga4ab5cae247b853bf9f4f0bf761c1c71e)LOG\_PRINTK

| #define LOG\_PRINTK | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log.h](log_8h.md)>`

**Value:**

Z\_LOG\_PRINTK(0, \_\_VA\_ARGS\_\_)

Unconditionally print raw log message.

The result is same as if printk was used but it goes through logging infrastructure thus utilizes logging mode, e.g. deferred mode.

Parameters
:   | ... | A string optionally containing printk valid conversion specifier, followed by as many values as specifiers. |
    | --- | --- |

## [◆ ](#ga7dedf58739648ed9b9aef1abe982f7d6)LOG\_RAW

| #define LOG\_RAW | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log.h](log_8h.md)>`

**Value:**

Z\_LOG\_PRINTK(1, \_\_VA\_ARGS\_\_)

Unconditionally print raw log message.

Provided string is printed as is without appending any characters (e.g., color or newline).

Parameters
:   | ... | A string optionally containing printk valid conversion specifier, followed by as many values as specifiers. |
    | --- | --- |

## [◆ ](#ga644db4299681d9ebf06f8745ad984c65)LOG\_WRN

| #define LOG\_WRN | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log.h](log_8h.md)>`

**Value:**

Z\_LOG([LOG\_LEVEL\_WRN](log__core_8h.md#a54f5db1327d9fdbaecbb03a6969de97b), \_\_VA\_ARGS\_\_)

Writes a WARNING level message to the log.

It's meant to register messages related to unusual situations that are not necessarily errors.

Parameters
:   | ... | A string optionally containing printk valid conversion specifier, followed by as many values as specifiers. |
    | --- | --- |

## [◆ ](#gaa9b22a7d4659030d9a3273f1f1e6786c)LOG\_WRN\_ONCE

| #define LOG\_WRN\_ONCE | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log.h](log_8h.md)>`

**Value:**

do { \

static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \_\_warned; \

if (unlikely(\_\_warned == 0)) { \

Z\_LOG([LOG\_LEVEL\_WRN](log__core_8h.md#a54f5db1327d9fdbaecbb03a6969de97b), \_\_VA\_ARGS\_\_); \

\_\_warned = 1; \

} \

} while (0)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

Writes a WARNING level message to the log on the first execution only.

It's meant for situations that warrant investigation but could clutter the logs if output on every execution.

Parameters
:   | ... | A string optionally containing printk valid conversion specifier, followed by as many values as specifiers. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
