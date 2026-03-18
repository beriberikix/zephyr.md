---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/winstream_8h.html
original_path: doxygen/html/winstream_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

winstream.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](winstream_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sys\_winstream](structsys__winstream.md) |
|  | Lockless shared memory byte stream IPC. [More...](structsys__winstream.md#details) |

| Functions | |
| --- | --- |
| static struct [sys\_winstream](structsys__winstream.md) \* | [sys\_winstream\_init](#acc72f0f65bd88e8f2b630a3832006f9c) (void \*buf, int buflen) |
|  | Construct a [sys\_winstream](structsys__winstream.md "Lockless shared memory byte stream IPC.") from a region of memory. |
| void | [sys\_winstream\_write](#ae8686be598c081858322378c8e4368cb) (struct [sys\_winstream](structsys__winstream.md) \*ws, const char \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len) |
|  | Write bytes to a [sys\_winstream](structsys__winstream.md "Lockless shared memory byte stream IPC."). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_winstream\_read](#a55dc3b77ec21e6d799aa951e327dc392) (struct [sys\_winstream](structsys__winstream.md) \*ws, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*seq, char \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) buflen) |
|  | Read bytes from a [sys\_winstream](structsys__winstream.md "Lockless shared memory byte stream IPC."). |

## Function Documentation

## [◆ ](#acc72f0f65bd88e8f2b630a3832006f9c)sys\_winstream\_init()

| | struct [sys\_winstream](structsys__winstream.md) \* sys\_winstream\_init | ( | void \* | *buf*, | | --- | --- | --- | --- | |  |  | int | *buflen* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Construct a [sys\_winstream](structsys__winstream.md "Lockless shared memory byte stream IPC.") from a region of memory.

This function initializes a [sys\_winstream](structsys__winstream.md "Lockless shared memory byte stream IPC.") in an arbitrarily-sized region of memory, returning the resulting object (which is guaranteed to be at the same address as the buffer). The memory must (obviously) be shared between the reader and writer, and all operations to it must be coherent and consistently ordered.

Parameters
:   | buf | Pointer to a region of memory to contain the stream |
    | --- | --- |
    | buflen | Length of the buffer, must be large enough to contain the struct [sys\_winstream](structsys__winstream.md "Lockless shared memory byte stream IPC.") and at least one byte of data. |

Returns
:   A pointer to an initialized [sys\_winstream](structsys__winstream.md "Lockless shared memory byte stream IPC.") (same address as the buf parameter).

## [◆ ](#a55dc3b77ec21e6d799aa951e327dc392)sys\_winstream\_read()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_winstream\_read | ( | struct [sys\_winstream](structsys__winstream.md) \* | *ws*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *seq*, |
|  |  | char \* | *buf*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *buflen* ) |

Read bytes from a [sys\_winstream](structsys__winstream.md "Lockless shared memory byte stream IPC.").

This function will read bytes from a [sys\_winstream](structsys__winstream.md "Lockless shared memory byte stream IPC.") into a specified buffer. It will always return in constant time, it does not block or engage in any kind of synchronization beyond memory ordering. The number of bytes read into the buffer will be returned, but note that it is possible that an underflow can occur if the writer gets ahead of our context. That situation can be detected via the sequence number returned via a pointer (i.e. if "\*seq != old\_seq +
return\_value", an underflow occurred and bytes were dropped).

Parameters
:   | ws | A [sys\_winstream](structsys__winstream.md "Lockless shared memory byte stream IPC.") from which to read |
    | --- | --- |
    | seq | A pointer to an integer containing the last sequence number read from the stream, or zero to indicate "start of stream". It is updated in place and returned for future calls and for detecting underflows. |
    | buf | A buffer into which to store the data read |
    | buflen | The length of buf in bytes |

Returns
:   The number of bytes written into the buffer

## [◆ ](#ae8686be598c081858322378c8e4368cb)sys\_winstream\_write()

| void sys\_winstream\_write | ( | struct [sys\_winstream](structsys__winstream.md) \* | *ws*, |
| --- | --- | --- | --- |
|  |  | const char \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *len* ) |

Write bytes to a [sys\_winstream](structsys__winstream.md "Lockless shared memory byte stream IPC.").

This function writes the specified number of bytes into the stream. It will always return synchronously, it does not block or engage in any kind of synchronization beyond memory write ordering. Any bytes passed beyond what can be stored in the buffer will be silently dropped, but readers can detect their presence via the sequence number.

Parameters
:   | ws | A [sys\_winstream](structsys__winstream.md "Lockless shared memory byte stream IPC.") to which to write |
    | --- | --- |
    | data | Pointer to bytes to be written |
    | len | Number of bytes to write |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [winstream.h](winstream_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
