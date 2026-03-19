---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbindesc__handle.html
original_path: doxygen/html/structbindesc__handle.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bindesc\_handle Struct Reference

`#include <[bindesc.h](bindesc_8h_source.md)>`

| Public Types | |
| --- | --- |
| enum | { [BINDESC\_HANDLE\_TYPE\_RAM](#a3367bd6f8c28a54305ba47f3f47f054ca6b384bd5837e71fd2b16f20e6b656488) , [BINDESC\_HANDLE\_TYPE\_MEMORY\_MAPPED\_FLASH](#a3367bd6f8c28a54305ba47f3f47f054ca934b7d04129a28cac848dd472ab6bdd9) , [BINDESC\_HANDLE\_TYPE\_FLASH](#a3367bd6f8c28a54305ba47f3f47f054caa79bb2c6316f34fe69662abcb9995d55) } |

| Data Fields | |
| --- | --- |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [address](#a40eb18bdca234d91bf7395ed7d6be37d) |
| enum bindesc\_handle:: { ... } | [type](#ac598522ba071536349778973692b473c) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [size\_limit](#aca15669b5589c20d6ea0e1296e0ff233) |

## Member Enumeration Documentation

## [◆ ](#a3367bd6f8c28a54305ba47f3f47f054c)anonymous enum

| anonymous enum |
| --- |

| Enumerator | |
| --- | --- |
| BINDESC\_HANDLE\_TYPE\_RAM |  |
| BINDESC\_HANDLE\_TYPE\_MEMORY\_MAPPED\_FLASH |  |
| BINDESC\_HANDLE\_TYPE\_FLASH |  |

## Field Documentation

## [◆ ](#a40eb18bdca234d91bf7395ed7d6be37d)address

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bindesc\_handle::address |
| --- |

## [◆ ](#aca15669b5589c20d6ea0e1296e0ff233)size\_limit

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bindesc\_handle::size\_limit |
| --- |

## [◆ ](#ac598522ba071536349778973692b473c)[]

| enum { ... } bindesc\_handle::type |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/[bindesc.h](bindesc_8h_source.md)

- [bindesc\_handle](structbindesc__handle.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
