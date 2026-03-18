---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__pipe__apis.html
original_path: doxygen/html/group__pipe__apis.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Pipe APIs

[Kernel APIs](group__kernel__apis.md)

| Data Structures | |
| --- | --- |
| struct | [k\_pipe](structk__pipe.md) |
|  | Pipe Structure. [More...](structk__pipe.md#details) |

| Macros | |
| --- | --- |
| #define | [K\_PIPE\_DEFINE](#gac2256aa00c59e78199be9bdefd61aa52)(name, pipe\_buffer\_size, pipe\_align) |
|  | Statically define and initialize a pipe. |

| Functions | |
| --- | --- |
| void | [k\_pipe\_init](#gae9e807fb63bb7186b87015664f2c762d) (struct [k\_pipe](structk__pipe.md) \*pipe, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Initialize a pipe. |
| int | [k\_pipe\_cleanup](#gaad0ab1b97b537da408031e4bcbe04f36) (struct [k\_pipe](structk__pipe.md) \*pipe) |
|  | Release a pipe's allocated buffer. |
| int | [k\_pipe\_alloc\_init](#ga32a902a5d12ca54b17c2b58783214613) (struct [k\_pipe](structk__pipe.md) \*pipe, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Initialize a pipe and allocate a buffer for it. |
| int | [k\_pipe\_put](#gaff77638ad7217974a10c23a0a7e336ae) (struct [k\_pipe](structk__pipe.md) \*pipe, const void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes\_to\_write, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*bytes\_written, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) min\_xfer, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Write data to a pipe. |
| int | [k\_pipe\_get](#gada9aaf9a336d98a95441212f4223e9ef) (struct [k\_pipe](structk__pipe.md) \*pipe, void \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bytes\_to\_read, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*bytes\_read, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) min\_xfer, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Read data from a pipe. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [k\_pipe\_read\_avail](#ga21849ebf856532de6e3ea38489071220) (struct [k\_pipe](structk__pipe.md) \*pipe) |
|  | Query the number of bytes that may be read from *pipe*. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [k\_pipe\_write\_avail](#gaff3ed3e93591d72c60a3640d195998c3) (struct [k\_pipe](structk__pipe.md) \*pipe) |
|  | Query the number of bytes that may be written to *pipe*. |
| void | [k\_pipe\_flush](#ga41484bb5c7dcd97e7a7b7f1422f8026f) (struct [k\_pipe](structk__pipe.md) \*pipe) |
|  | Flush the pipe of write data. |
| void | [k\_pipe\_buffer\_flush](#ga71e0e38a15fa27f27c1f028223936445) (struct [k\_pipe](structk__pipe.md) \*pipe) |
|  | Flush the pipe's internal buffer. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gac2256aa00c59e78199be9bdefd61aa52)K\_PIPE\_DEFINE

| #define K\_PIPE\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *pipe\_buffer\_size*, |
|  |  |  | *pipe\_align* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

**Value:**

static unsigned char \_\_noinit \_\_aligned(pipe\_align) \

\_k\_pipe\_buf\_##name[pipe\_buffer\_size]; \

STRUCT\_SECTION\_ITERABLE([k\_pipe](structk__pipe.md), name) = \

Z\_PIPE\_INITIALIZER(name, \_k\_pipe\_buf\_##name, pipe\_buffer\_size)

[k\_pipe](structk__pipe.md)

Pipe Structure.

**Definition** kernel.h:4847

Statically define and initialize a pipe.

The pipe can be accessed outside the module where it is defined using:

extern struct [k\_pipe](structk__pipe.md) <name>;

Parameters
:   | name | Name of the pipe. |
    | --- | --- |
    | pipe\_buffer\_size | Size of the pipe's ring buffer (in bytes), or zero if no ring buffer is used. |
    | pipe\_align | Alignment of the pipe's ring buffer (power of 2). |

## Function Documentation

## [◆ ](#ga32a902a5d12ca54b17c2b58783214613)k\_pipe\_alloc\_init()

| int k\_pipe\_alloc\_init | ( | struct [k\_pipe](structk__pipe.md) \* | *pipe*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Initialize a pipe and allocate a buffer for it.

Storage for the buffer region will be allocated from the calling thread's resource pool. This memory will be released if [k\_pipe\_cleanup()](#gaad0ab1b97b537da408031e4bcbe04f36) is called, or userspace is enabled and the pipe object loses all references to it.

This function should only be called on uninitialized pipe objects.

Parameters
:   | pipe | Address of the pipe. |
    | --- | --- |
    | size | Size of the pipe's ring buffer (in bytes), or zero if no ring buffer is used. |

Return values
:   | 0 | on success |
    | --- | --- |
    | -ENOMEM | if memory couldn't be allocated |

## [◆ ](#ga71e0e38a15fa27f27c1f028223936445)k\_pipe\_buffer\_flush()

| void k\_pipe\_buffer\_flush | ( | struct [k\_pipe](structk__pipe.md) \* | *pipe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Flush the pipe's internal buffer.

This routine flushes the pipe's internal buffer. This is equivalent to reading up to N bytes from the pipe (where N is the size of the pipe's buffer) into a temporary buffer and then discarding that buffer. If there were writers previously pending, then some may unpend as they try to fill up the pipe's emptied buffer.

Parameters
:   | pipe | Address of the pipe. |
    | --- | --- |

## [◆ ](#gaad0ab1b97b537da408031e4bcbe04f36)k\_pipe\_cleanup()

| int k\_pipe\_cleanup | ( | struct [k\_pipe](structk__pipe.md) \* | *pipe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Release a pipe's allocated buffer.

If a pipe object was given a dynamically allocated buffer via [k\_pipe\_alloc\_init()](#ga32a902a5d12ca54b17c2b58783214613), this will free it. This function does nothing if the buffer wasn't dynamically allocated.

Parameters
:   | pipe | Address of the pipe. |
    | --- | --- |

Return values
:   | 0 | on success |
    | --- | --- |
    | -EAGAIN | nothing to cleanup |

## [◆ ](#ga41484bb5c7dcd97e7a7b7f1422f8026f)k\_pipe\_flush()

| void k\_pipe\_flush | ( | struct [k\_pipe](structk__pipe.md) \* | *pipe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Flush the pipe of write data.

This routine flushes the pipe. Flushing the pipe is equivalent to reading both all the data in the pipe's buffer and all the data waiting to go into that pipe into a large temporary buffer and discarding the buffer. Any writers that were previously pended become unpended.

Parameters
:   | pipe | Address of the pipe. |
    | --- | --- |

## [◆ ](#gada9aaf9a336d98a95441212f4223e9ef)k\_pipe\_get()

| int k\_pipe\_get | ( | struct [k\_pipe](structk__pipe.md) \* | *pipe*, |
| --- | --- | --- | --- |
|  |  | void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes\_to\_read*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *bytes\_read*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *min\_xfer*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Read data from a pipe.

This routine reads up to *bytes\_to\_read* bytes of data from *pipe*.

Parameters
:   | pipe | Address of the pipe. |
    | --- | --- |
    | data | Address to place the data read from pipe. |
    | bytes\_to\_read | Maximum number of data bytes to read. |
    | bytes\_read | Address of area to hold the number of bytes read. |
    | min\_xfer | Minimum number of data bytes to read. |
    | timeout | Waiting period to wait for the data to be read, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | At least *min\_xfer* bytes of data were read. |
    | --- | --- |
    | -EINVAL | invalid parameters supplied |
    | -EIO | Returned without waiting; zero data bytes were read. |
    | -EAGAIN | Waiting period timed out; between zero and *min\_xfer* minus one data bytes were read. |

## [◆ ](#gae9e807fb63bb7186b87015664f2c762d)k\_pipe\_init()

| void k\_pipe\_init | ( | struct [k\_pipe](structk__pipe.md) \* | *pipe*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Initialize a pipe.

This routine initializes a pipe object, prior to its first use.

Parameters
:   | pipe | Address of the pipe. |
    | --- | --- |
    | buffer | Address of the pipe's ring buffer, or NULL if no ring buffer is used. |
    | size | Size of the pipe's ring buffer (in bytes), or zero if no ring buffer is used. |

## [◆ ](#gaff77638ad7217974a10c23a0a7e336ae)k\_pipe\_put()

| int k\_pipe\_put | ( | struct [k\_pipe](structk__pipe.md) \* | *pipe*, |
| --- | --- | --- | --- |
|  |  | const void \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bytes\_to\_write*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *bytes\_written*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *min\_xfer*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Write data to a pipe.

This routine writes up to *bytes\_to\_write* bytes of data to *pipe*.

Parameters
:   | pipe | Address of the pipe. |
    | --- | --- |
    | data | Address of data to write. |
    | bytes\_to\_write | Size of data (in bytes). |
    | bytes\_written | Address of area to hold the number of bytes written. |
    | min\_xfer | Minimum number of bytes to write. |
    | timeout | Waiting period to wait for the data to be written, or one of the special values K\_NO\_WAIT and K\_FOREVER. |

Return values
:   | 0 | At least *min\_xfer* bytes of data were written. |
    | --- | --- |
    | -EIO | Returned without waiting; zero data bytes were written. |
    | -EAGAIN | Waiting period timed out; between zero and *min\_xfer* minus one data bytes were written. |

## [◆ ](#ga21849ebf856532de6e3ea38489071220)k\_pipe\_read\_avail()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) k\_pipe\_read\_avail | ( | struct [k\_pipe](structk__pipe.md) \* | *pipe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Query the number of bytes that may be read from *pipe*.

Parameters
:   | pipe | Address of the pipe. |
    | --- | --- |

Return values
:   | a | number n such that 0 <= n <= [k\_pipe::size](structk__pipe.md#aca3472fb8d68f01af4e26b0b88736d64 "k_pipe::size"); the result is zero for unbuffered pipes. |
    | --- | --- |

## [◆ ](#gaff3ed3e93591d72c60a3640d195998c3)k\_pipe\_write\_avail()

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) k\_pipe\_write\_avail | ( | struct [k\_pipe](structk__pipe.md) \* | *pipe* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[kernel.h](include_2zephyr_2kernel_8h.md)>`

Query the number of bytes that may be written to *pipe*.

Parameters
:   | pipe | Address of the pipe. |
    | --- | --- |

Return values
:   | a | number n such that 0 <= n <= [k\_pipe::size](structk__pipe.md#aca3472fb8d68f01af4e26b0b88736d64 "k_pipe::size"); the result is zero for unbuffered pipes. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
