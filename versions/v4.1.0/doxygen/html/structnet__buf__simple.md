---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structnet__buf__simple.html
original_path: doxygen/html/structnet__buf__simple.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_buf\_simple Struct Reference

[Operating System Services](group__os__services.md) » [Network Buffer Library](group__net__buf.md)

Simple network buffer representation.
[More...](#details)

`#include <[net_buf.h](net__buf_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [data](#ad232efff435f425d30ac78f5abf2d8b1) |
|  | Pointer to the start of data in the buffer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [len](#ae8707c50d70c26b53281b40eb1720cf3) |
|  | Length of the data behind the data pointer. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [size](#ae6dc4aa029a67d3911293618eb30caa6) |
|  | Amount of data that net\_buf\_simple::\_\_buf can store. |

## Detailed Description

Simple network buffer representation.

This is a simpler variant of the [net\_buf](structnet__buf.md "Network buffer representation.") object (in fact [net\_buf](structnet__buf.md "Network buffer representation.") uses [net\_buf\_simple](structnet__buf__simple.md "Simple network buffer representation.") internally). It doesn't provide any kind of reference counting, user data, dynamic allocation, or in general the ability to pass through kernel objects such as FIFOs.

The main use of this is for scenarios where the meta-data of the normal [net\_buf](structnet__buf.md "Network buffer representation.") isn't needed and causes too much overhead. This could be e.g. when the buffer only needs to be allocated on the stack or when the access to and lifetime of the buffer is well controlled and constrained.

## Field Documentation

## [◆ ](#ad232efff435f425d30ac78f5abf2d8b1)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* net\_buf\_simple::data |
| --- |

Pointer to the start of data in the buffer.

## [◆ ](#ae8707c50d70c26b53281b40eb1720cf3)len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_buf\_simple::len |
| --- |

Length of the data behind the data pointer.

To determine the max length, use [net\_buf\_simple\_max\_len()](group__net__buf.md#gabfe255688a80c0abea866762ff4c5a6c "Check maximum net_buf_simple::len value."), not [size](#ae6dc4aa029a67d3911293618eb30caa6)!

## [◆ ](#ae6dc4aa029a67d3911293618eb30caa6)size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_buf\_simple::size |
| --- |

Amount of data that net\_buf\_simple::\_\_buf can store.

---

The documentation for this struct was generated from the following file:

- zephyr/[net\_buf.h](net__buf_8h_source.md)

- [net\_buf\_simple](structnet__buf__simple.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
