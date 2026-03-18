---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__console__api.html
original_path: doxygen/html/group__console__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Console API

[Operating System Services](group__os__services.md)

Console API.
[More...](#details)

| Functions | |
| --- | --- |
| int | [console\_init](#ga0bf949437e32d17992435003cf8b46b5) (void) |
|  | Initialize console device. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [console\_read](#ga27785534c14d4098822db2b870b7d81d) (void \*dummy, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Read data from console. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [console\_write](#ga204fd795daf9ef6b1f2803547747545e) (void \*dummy, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Write data to console. |
| int | [console\_getchar](#ga2ba36eb1081cd0b98aa43216ccd6fbd5) (void) |
|  | Get next char from console input buffer. |
| int | [console\_putchar](#ga7bd842f1cda6c8218cb1d41420e4de49) (char c) |
|  | Output a char to console (buffered). |
| void | [console\_getline\_init](#gacd13267df8567c63f2285ce0e1cbbc20) (void) |
|  | Initialize [console\_getline()](#ga3454f5b84d38d46a6c2bbf7fd6baa815) call. |
| char \* | [console\_getline](#ga3454f5b84d38d46a6c2bbf7fd6baa815) (void) |
|  | Get next line from console input buffer. |

## Detailed Description

Console API.

## Function Documentation

## [◆ ](#ga2ba36eb1081cd0b98aa43216ccd6fbd5)console\_getchar()

| int console\_getchar | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[console.h](console_2console_8h.md)>`

Get next char from console input buffer.

Return next input character from console. If no characters available, this function will block. This function is similar to ANSI C getchar() function and is intended to ease porting of existing software. Before this function can be used, [console\_init()](#ga0bf949437e32d17992435003cf8b46b5) should be called once. This function is incompatible with native Zephyr callback-based console input processing, shell subsystem, or [console\_getline()](#ga3454f5b84d38d46a6c2bbf7fd6baa815).

Returns
:   0-255: a character read, including control characters. <0: error occurred.

## [◆ ](#ga3454f5b84d38d46a6c2bbf7fd6baa815)console\_getline()

| char \* console\_getline | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[console.h](console_2console_8h.md)>`

Get next line from console input buffer.

Return next input line from console. Until full line is available, this function will block. This function is similar to ANSI C gets() function (except a line is returned in system-owned buffer, and system takes care of the buffer overflow checks) and is intended to ease porting of existing software. Before this function can be used, [console\_getline\_init()](#gacd13267df8567c63f2285ce0e1cbbc20) should be called once. This function is incompatible with native Zephyr callback-based console input processing, shell subsystem, or [console\_getchar()](#ga2ba36eb1081cd0b98aa43216ccd6fbd5).

Returns
:   A pointer to a line read, not including EOL character(s). A line resides in a system-owned buffer, so an application should finish any processing of this line immediately after [console\_getline()](#ga3454f5b84d38d46a6c2bbf7fd6baa815) call, or the buffer can be reused.

## [◆ ](#gacd13267df8567c63f2285ce0e1cbbc20)console\_getline\_init()

| void console\_getline\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[console.h](console_2console_8h.md)>`

Initialize [console\_getline()](#ga3454f5b84d38d46a6c2bbf7fd6baa815) call.

This function should be called once to initialize pull-style access to console via [console\_getline()](#ga3454f5b84d38d46a6c2bbf7fd6baa815) function. This function supersedes, and incompatible with, callback (push-style) console handling (via [console\_input\_fn](drivers_2console_2console_8h.md#a0dab6d89950bb4c2bbb17571b9b1461f "Console input processing handler signature.") callback, etc.).

## [◆ ](#ga0bf949437e32d17992435003cf8b46b5)console\_init()

| int console\_init | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[console.h](console_2console_8h.md)>`

Initialize console device.

This function should be called once to initialize pull-style access to console via [console\_getchar()](#ga2ba36eb1081cd0b98aa43216ccd6fbd5) function and buffered output using [console\_putchar()](#ga7bd842f1cda6c8218cb1d41420e4de49) function. This function supersedes, and incompatible with, callback (push-style) console handling (via [console\_input\_fn](drivers_2console_2console_8h.md#a0dab6d89950bb4c2bbb17571b9b1461f "Console input processing handler signature.") callback, etc.).

Returns
:   0 on success, error code (<0) otherwise

## [◆ ](#ga7bd842f1cda6c8218cb1d41420e4de49)console\_putchar()

| int console\_putchar | ( | char | *c* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[console.h](console_2console_8h.md)>`

Output a char to console (buffered).

Puts a character into console output buffer. It will be sent to a console asynchronously, e.g. using an IRQ handler.

Returns
:   <0 on error, otherwise 0.

## [◆ ](#ga27785534c14d4098822db2b870b7d81d)console\_read()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) console\_read | ( | void \* | *dummy*, |
| --- | --- | --- | --- |
|  |  | void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[console.h](console_2console_8h.md)>`

Read data from console.

Parameters
:   | [Dummy L2/driver Support Functions](group__dummy.md "Dummy L2/driver support functions.") | ignored, present to follow read() prototype |
    | --- | --- |
    | buf | buffer to read data to |
    | size | maximum number of bytes to read |

Returns
:   >0, number of actually read bytes (can be less than size param) =0, in case of EOF <0, in case of error (e.g. -EAGAIN if timeout expired). errno variable is also set.

## [◆ ](#ga204fd795daf9ef6b1f2803547747545e)console\_write()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) console\_write | ( | void \* | *dummy*, |
| --- | --- | --- | --- |
|  |  | const void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[console.h](console_2console_8h.md)>`

Write data to console.

Parameters
:   | [Dummy L2/driver Support Functions](group__dummy.md "Dummy L2/driver support functions.") | ignored, present to follow write() prototype |
    | --- | --- |
    | buf | buffer to write data to |
    | size | maximum number of bytes to write |

Returns
:   =>0, number of actually written bytes (can be less than size param) <0, in case of error (e.g. -EAGAIN if timeout expired). errno variable is also set.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
