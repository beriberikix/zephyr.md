---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__pipe__apis.html
original_path: doxygen/html/group__pipe__apis.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Pipe APIs

[Kernel APIs](group__kernel__apis.md)

| Data Structures | |
| --- | --- |
| struct | [k\_pipe](structk__pipe.md) |

| Macros | |
| --- | --- |
| #define | [K\_PIPE\_DEFINE](#gac2256aa00c59e78199be9bdefd61aa52)(name, pipe\_buffer\_size, pipe\_align) |
|  | Statically define and initialize a pipe. |

| Enumerations | |
| --- | --- |
| enum | [pipe\_flags](#gae5471546043f4d14e97c3f6313053ee0) { [PIPE\_FLAG\_OPEN](#ggae5471546043f4d14e97c3f6313053ee0a9fc19eac7b41c00ca97c2fb0a30a2309) = BIT(0) , [PIPE\_FLAG\_RESET](#ggae5471546043f4d14e97c3f6313053ee0a37642c400a675e1dce34c9b878874df4) = BIT(1) } |

| Functions | |
| --- | --- |
| void | [k\_pipe\_init](#gae2c8d97af1f7e9deb93e670859525cf3) (struct [k\_pipe](structk__pipe.md) \*pipe, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) buffer\_size) |
|  | initialize a pipe |
| int | [k\_pipe\_write](#ga514ab3d174dcada766ecbda138944ddc) (struct [k\_pipe](structk__pipe.md) \*pipe, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Write data to a pipe. |
| int | [k\_pipe\_read](#gaecb07412025d9e065ee7b99121522257) (struct [k\_pipe](structk__pipe.md) \*pipe, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Read data from a pipe This routine reads up to *len* bytes of data from *pipe*. |
| void | [k\_pipe\_reset](#gaaedff72169127b8227c80bf8adf1f9dd) (struct [k\_pipe](structk__pipe.md) \*pipe) |
|  | Reset a pipe This routine resets the pipe, discarding any unread data and unblocking any threads waiting to write or read, causing the waiting threads to return with -ECANCELED. |
| void | [k\_pipe\_close](#ga83d4b5de8902845850d01b0c3db0702a) (struct [k\_pipe](structk__pipe.md) \*pipe) |
|  | Close a pipe. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gac2256aa00c59e78199be9bdefd61aa52)K\_PIPE\_DEFINE

| #define K\_PIPE\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *pipe\_buffer\_size*, |
|  |  |  | *pipe\_align* ) |

`#include <[kernel.h](kernel_8h.md)>`

**Value:**

static unsigned char \_\_noinit \_\_aligned(pipe\_align) \

\_k\_pipe\_buf\_##name[pipe\_buffer\_size]; \

STRUCT\_SECTION\_ITERABLE([k\_pipe](structk__pipe.md), name) = \

Z\_PIPE\_INITIALIZER(name, \_k\_pipe\_buf\_##name, pipe\_buffer\_size)

[k\_pipe](structk__pipe.md)

**Definition** kernel.h:5211

Statically define and initialize a pipe.

The pipe can be accessed outside the module where it is defined using:

extern struct [k\_pipe](structk__pipe.md) <name>;

Parameters
:   | name | Name of the pipe. |
    | --- | --- |
    | pipe\_buffer\_size | Size of the pipe's ring buffer (in bytes) or zero if no ring buffer is used. |
    | pipe\_align | Alignment of the pipe's ring buffer (power of 2). |

## Enumeration Type Documentation

## [◆ ](#gae5471546043f4d14e97c3f6313053ee0)pipe\_flags

| enum [pipe\_flags](#gae5471546043f4d14e97c3f6313053ee0) |
| --- |

`#include <[kernel.h](kernel_8h.md)>`

| Enumerator | |
| --- | --- |
| PIPE\_FLAG\_OPEN |  |
| PIPE\_FLAG\_RESET |  |

## Function Documentation

## [◆ ](#ga83d4b5de8902845850d01b0c3db0702a)k\_pipe\_close()

| void k\_pipe\_close | ( | struct [k\_pipe](structk__pipe.md) \* | *pipe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Close a pipe.

This routine closes a pipe. Any threads that were blocked on the pipe will be unblocked and receive an error code.

Parameters
:   | pipe | Address of the pipe. |
    | --- | --- |

## [◆ ](#gae2c8d97af1f7e9deb93e670859525cf3)k\_pipe\_init()

| void k\_pipe\_init | ( | struct [k\_pipe](structk__pipe.md) \* | *pipe*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *buffer\_size* ) |

`#include <[kernel.h](kernel_8h.md)>`

initialize a pipe

This routine initializes a pipe object, prior to its first use.

Parameters
:   | pipe | Address of the pipe. |
    | --- | --- |
    | buffer | Address of the pipe's buffer, or NULL if no ring buffer is used. |
    | buffer\_size | Size of the pipe's buffer, or zero if no ring buffer is used. |

## [◆ ](#gaecb07412025d9e065ee7b99121522257)k\_pipe\_read()

| int k\_pipe\_read | ( | struct [k\_pipe](structk__pipe.md) \* | *pipe*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[kernel.h](kernel_8h.md)>`

Read data from a pipe This routine reads up to *len* bytes of data from *pipe*.

If the pipe is empty, the routine will block until the data can be read or the timeout expires.

Parameters
:   | pipe | Address of the pipe. |
    | --- | --- |
    | data | Address to place the data read from pipe. |
    | len | Requested number of bytes to read. |
    | timeout | Waiting period to wait for the data to be read. |

Return values
:   | number | of bytes read on success |
    | --- | --- |
    | -EAGAIN | if no data could be read before the timeout expired |
    | -ECANCELED | if the read was interrupted by k\_pipe\_reset(..) |
    | -EPIPE | if the pipe was closed |

## [◆ ](#gaaedff72169127b8227c80bf8adf1f9dd)k\_pipe\_reset()

| void k\_pipe\_reset | ( | struct [k\_pipe](structk__pipe.md) \* | *pipe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](kernel_8h.md)>`

Reset a pipe This routine resets the pipe, discarding any unread data and unblocking any threads waiting to write or read, causing the waiting threads to return with -ECANCELED.

Calling k\_pipe\_read(..) or k\_pipe\_write(..) when the pipe is resetting but not yet reset will return -ECANCELED. The pipe is left open after a reset and can be used as normal.

Parameters
:   | pipe | Address of the pipe. |
    | --- | --- |

## [◆ ](#ga514ab3d174dcada766ecbda138944ddc)k\_pipe\_write()

| int k\_pipe\_write | ( | struct [k\_pipe](structk__pipe.md) \* | *pipe*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[kernel.h](kernel_8h.md)>`

Write data to a pipe.

This routine writes up to *len* bytes of data to *pipe*. If the pipe is full, the routine will block until the data can be written or the timeout expires.

Parameters
:   | pipe | Address of the pipe. |
    | --- | --- |
    | data | Address of data to write. |
    | len | Size of data (in bytes). |
    | timeout | Waiting period to wait for the data to be written. |

Return values
:   | number | of bytes written on success |
    | --- | --- |
    | -EAGAIN | if no data could be written before the timeout expired |
    | -ECANCELED | if the write was interrupted by k\_pipe\_reset(..) |
    | -EPIPE | if the pipe was closed |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
