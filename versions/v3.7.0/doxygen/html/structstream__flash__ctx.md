---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structstream__flash__ctx.html
original_path: doxygen/html/structstream__flash__ctx.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

stream\_flash\_ctx Struct Reference

[Operating System Services](group__os__services.md) » [Storage APIs](group__storage__apis.md) » [Stream to flash interface](group__stream__flash.md)

Structure for stream flash context.
[More...](#details)

`#include <[stream_flash.h](stream__flash_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [buf](#a5d7dd0c4a0687e566deb8bd6af3f0c8d) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [buf\_len](#aff53c741cf5141338206d89274c508c0) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [buf\_bytes](#a6fcef2130672bea3b9e5170c80e6e56a) |
| const struct [device](structdevice.md) \* | [fdev](#a8d959157df9da6907d6d90ac12f762f8) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [bytes\_written](#a694774f427f3a93057f0365867d3d90a) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [offset](#a66596293929b734b3132cc0a02674e3f) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [available](#afbaf8abad7ff12865863dc4108ee8ad2) |
| [stream\_flash\_callback\_t](group__stream__flash.md#ga0bf1914bba75d4d799d546b917e35705) | [callback](#a230924b0451fa21cefc87f01e0cbf84b) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [write\_block\_size](#a97f9820d77882b0e1679d35fc5ca3579) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [erase\_value](#ae640958e28fa1b4a065b7a322e00d57b) |

## Detailed Description

Structure for stream flash context.

Users should treat these structures as opaque values and only interact with them through the below API.

## Field Documentation

## [◆ ](#afbaf8abad7ff12865863dc4108ee8ad2)available

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stream\_flash\_ctx::available |
| --- |

## [◆ ](#a5d7dd0c4a0687e566deb8bd6af3f0c8d)buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* stream\_flash\_ctx::buf |
| --- |

## [◆ ](#a6fcef2130672bea3b9e5170c80e6e56a)buf\_bytes

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stream\_flash\_ctx::buf\_bytes |
| --- |

## [◆ ](#aff53c741cf5141338206d89274c508c0)buf\_len

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stream\_flash\_ctx::buf\_len |
| --- |

## [◆ ](#a694774f427f3a93057f0365867d3d90a)bytes\_written

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stream\_flash\_ctx::bytes\_written |
| --- |

## [◆ ](#a230924b0451fa21cefc87f01e0cbf84b)callback

| [stream\_flash\_callback\_t](group__stream__flash.md#ga0bf1914bba75d4d799d546b917e35705) stream\_flash\_ctx::callback |
| --- |

## [◆ ](#ae640958e28fa1b4a065b7a322e00d57b)erase\_value

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) stream\_flash\_ctx::erase\_value |
| --- |

## [◆ ](#a8d959157df9da6907d6d90ac12f762f8)fdev

| const struct [device](structdevice.md)\* stream\_flash\_ctx::fdev |
| --- |

## [◆ ](#a66596293929b734b3132cc0a02674e3f)offset

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stream\_flash\_ctx::offset |
| --- |

## [◆ ](#a97f9820d77882b0e1679d35fc5ca3579)write\_block\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) stream\_flash\_ctx::write\_block\_size |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/storage/[stream\_flash.h](stream__flash_8h_source.md)

- [stream\_flash\_ctx](structstream__flash__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
