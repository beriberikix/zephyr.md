---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/console_2tty_8h.html
original_path: doxygen/html/console_2tty_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tty.h File Reference

`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`

[Go to the source code of this file.](console_2tty_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [tty\_serial](structtty__serial.md) |

| Functions | |
| --- | --- |
| int | [tty\_init](#a5a880bb61f0bdb0f37c501acc0408d32) (struct [tty\_serial](structtty__serial.md) \*tty, const struct [device](structdevice.md) \*uart\_dev) |
|  | Initialize serial port object (classically known as tty). |
| static void | [tty\_set\_rx\_timeout](#a109fd8ee6b581a796d67025a0e33abde) (struct [tty\_serial](structtty__serial.md) \*tty, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set receive timeout for tty device. |
| static void | [tty\_set\_tx\_timeout](#a1c19c6ed8207ae711e047f9ae446e399) (struct [tty\_serial](structtty__serial.md) \*tty, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set transmit timeout for tty device. |
| int | [tty\_set\_rx\_buf](#ad05b854f19b3bd97e2635bc8ebc07ce2) (struct [tty\_serial](structtty__serial.md) \*tty, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Set receive buffer for tty device. |
| int | [tty\_set\_tx\_buf](#af6383a47f82797af9a45bc81d84de1be) (struct [tty\_serial](structtty__serial.md) \*tty, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Set transmit buffer for tty device. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [tty\_read](#a90ec3fbbe5f0fad19361d23e821c960c) (struct [tty\_serial](structtty__serial.md) \*tty, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Read data from a tty device. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [tty\_write](#af60d8a57ac3cb81a0a003a011a0f31e5) (struct [tty\_serial](structtty__serial.md) \*tty, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Write data to tty device. |

## Function Documentation

## [◆ ](#a5a880bb61f0bdb0f37c501acc0408d32)tty\_init()

| int tty\_init | ( | struct [tty\_serial](structtty__serial.md) \* | *tty*, |
| --- | --- | --- | --- |
|  |  | const struct [device](structdevice.md) \* | *uart\_dev* ) |

Initialize serial port object (classically known as tty).

"tty" device provides support for buffered, interrupt-driven, timeout-controlled access to an underlying UART device. For completeness, it also support non-interrupt-driven, busy-polling access mode. After initialization, tty is in the "most conservative" unbuffered mode with infinite timeouts (this is guaranteed to work on any hardware). Users should configure buffers and timeouts as they need using functions [tty\_set\_rx\_buf()](#ad05b854f19b3bd97e2635bc8ebc07ce2), [tty\_set\_tx\_buf()](#af6383a47f82797af9a45bc81d84de1be), [tty\_set\_rx\_timeout()](#a109fd8ee6b581a796d67025a0e33abde), [tty\_set\_tx\_timeout()](#a1c19c6ed8207ae711e047f9ae446e399).

Parameters
:   | tty | tty device structure to initialize |
    | --- | --- |
    | uart\_dev | underlying UART device to use (should support interrupt-driven operation) |

Returns
:   0 on success, error code (<0) otherwise

## [◆ ](#a90ec3fbbe5f0fad19361d23e821c960c)tty\_read()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) tty\_read | ( | struct [tty\_serial](structtty__serial.md) \* | *tty*, |
| --- | --- | --- | --- |
|  |  | void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

Read data from a tty device.

Parameters
:   | tty | tty device structure |
    | --- | --- |
    | buf | buffer to read data to |
    | size | maximum number of bytes to read |

Returns
:   >0, number of actually read bytes (can be less than size param) =0, for EOF-like condition (e.g., break signaled) <0, in case of error (e.g. -EAGAIN if timeout expired). errno variable is also set.

## [◆ ](#ad05b854f19b3bd97e2635bc8ebc07ce2)tty\_set\_rx\_buf()

| int tty\_set\_rx\_buf | ( | struct [tty\_serial](structtty__serial.md) \* | *tty*, |
| --- | --- | --- | --- |
|  |  | void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

Set receive buffer for tty device.

Set receive buffer or switch to unbuffered operation for receive.

Parameters
:   | tty | tty device structure |
    | --- | --- |
    | buf | buffer, or NULL for unbuffered operation |
    | size | buffer buffer size, 0 for unbuffered operation |

Returns
:   0 on success, error code (<0) otherwise: EINVAL: unsupported buffer (size)

## [◆ ](#a109fd8ee6b581a796d67025a0e33abde)tty\_set\_rx\_timeout()

| | void tty\_set\_rx\_timeout | ( | struct [tty\_serial](structtty__serial.md) \* | *tty*, | | --- | --- | --- | --- | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Set receive timeout for tty device.

Set timeout for getchar() operation. Default timeout after device initialization is SYS\_FOREVER\_MS.

Parameters
:   | tty | tty device structure |
    | --- | --- |
    | timeout | timeout in milliseconds, or 0, or SYS\_FOREVER\_MS. |

## [◆ ](#af6383a47f82797af9a45bc81d84de1be)tty\_set\_tx\_buf()

| int tty\_set\_tx\_buf | ( | struct [tty\_serial](structtty__serial.md) \* | *tty*, |
| --- | --- | --- | --- |
|  |  | void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

Set transmit buffer for tty device.

Set transmit buffer or switch to unbuffered operation for transmit. Note that unbuffered mode is implicitly blocking, i.e. behaves as if tty\_set\_tx\_timeout(SYS\_FOREVER\_MS) was set.

Parameters
:   | tty | tty device structure |
    | --- | --- |
    | buf | buffer, or NULL for unbuffered operation |
    | size | buffer buffer size, 0 for unbuffered operation |

Returns
:   0 on success, error code (<0) otherwise: EINVAL: unsupported buffer (size)

## [◆ ](#a1c19c6ed8207ae711e047f9ae446e399)tty\_set\_tx\_timeout()

| | void tty\_set\_tx\_timeout | ( | struct [tty\_serial](structtty__serial.md) \* | *tty*, | | --- | --- | --- | --- | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Set transmit timeout for tty device.

Set timeout for [putchar()](stdio_8h.md#a568f021a83b2c22e1e700d12559d660a) operation, for a case when output buffer is full. Default timeout after device initialization is SYS\_FOREVER\_MS.

Parameters
:   | tty | tty device structure |
    | --- | --- |
    | timeout | timeout in milliseconds, or 0, or SYS\_FOREVER\_MS. |

## [◆ ](#af60d8a57ac3cb81a0a003a011a0f31e5)tty\_write()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) tty\_write | ( | struct [tty\_serial](structtty__serial.md) \* | *tty*, |
| --- | --- | --- | --- |
|  |  | const void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

Write data to tty device.

Parameters
:   | tty | tty device structure |
    | --- | --- |
    | buf | buffer containing data |
    | size | maximum number of bytes to write |

Returns
:   =>0, number of actually written bytes (can be less than size param) <0, in case of error (e.g. -EAGAIN if timeout expired). errno variable is also set.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [console](dir_2f086bf88c9e3ffd4c7c065f4bf7757c.md)
- [tty.h](console_2tty_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
