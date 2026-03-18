---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structaiocb.html
original_path: doxygen/html/structaiocb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

aiocb Struct Reference

`#include <[aio.h](aio_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int | [aio\_fildes](#ad6b6e95e6e4a79487f7e6edaae26003f) |
| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | [aio\_offset](#a1e74b350a9ca189fa7c25b61c5cede6c) |
| volatile void \* | [aio\_buf](#a60a966202034e1abde4ca3ea0965fa30) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [aio\_nbytes](#a6b4f8a1d05ed5444784389734d71cda7) |
| int | [aio\_reqprio](#a7a8f63c080c8602ebcacbb86e9f5547e) |
| struct [sigevent](structsigevent.md) | [aio\_sigevent](#a7065f3086beb9cdffc525c1d09949268) |
| int | [aio\_lio\_opcode](#a8a23597de7bfc422b58ec9816ced7d47) |

## Field Documentation

## [◆ ](#a60a966202034e1abde4ca3ea0965fa30)aio\_buf

| volatile void\* aiocb::aio\_buf |
| --- |

## [◆ ](#ad6b6e95e6e4a79487f7e6edaae26003f)aio\_fildes

| int aiocb::aio\_fildes |
| --- |

## [◆ ](#a8a23597de7bfc422b58ec9816ced7d47)aio\_lio\_opcode

| int aiocb::aio\_lio\_opcode |
| --- |

## [◆ ](#a6b4f8a1d05ed5444784389734d71cda7)aio\_nbytes

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) aiocb::aio\_nbytes |
| --- |

## [◆ ](#a1e74b350a9ca189fa7c25b61c5cede6c)aio\_offset

| [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) aiocb::aio\_offset |
| --- |

## [◆ ](#a7a8f63c080c8602ebcacbb86e9f5547e)aio\_reqprio

| int aiocb::aio\_reqprio |
| --- |

## [◆ ](#a7065f3086beb9cdffc525c1d09949268)aio\_sigevent

| struct [sigevent](structsigevent.md) aiocb::aio\_sigevent |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/posix/[aio.h](aio_8h_source.md)

- [aiocb](structaiocb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
