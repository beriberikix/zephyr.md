---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structsip__svc__response.html
original_path: doxygen/html/structsip__svc__response.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sip\_svc\_response Struct Reference

SiP Services service communication protocol response format.
[More...](#details)

`#include <[sip_svc_proto.h](sip__svc__proto_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [header](#ab2a3ed6ec283ef83a2ad8ea8eea421be) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a0](#a4f413e152dc2ef463140499164c3e410) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a1](#abfb0f411524209388f79f35a82031e79) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a2](#af973d08da13a7dcecf344f3f9d6f118e) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a3](#aac8bb11e4661e59cbce0d6b5d50a0820) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [resp\_data\_addr](#a5b8a49d292e45ecdd81920c30b650c10) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [resp\_data\_size](#a2e8373be61b16ac4f4d013103539cceb) |
| void \* | [priv\_data](#a992b3f936866852633569f9c8d37d6a0) |

## Detailed Description

SiP Services service communication protocol response format.

response header

- bits [15: 0] Error code
- bits [23:16] Transaction ID
- bits [29:24] Unused. Reserved.
- bits [31:30] Arm SiP services communication protocol version

a0 - a3

- SMC/HVC return value

resp\_data\_addr

- This parameter only used by asynchronous command.
- Dynamic memory address that put the asynchronous response data. This address is provided by client during request. Client is responsible to free the memory space when receive the callback of a asynchronous command transaction.The memory needs to be dynamically allocated, the framework will free the allocated memory if the channel is in ABORT state.

resp\_data\_size

- This parameter only used by asynchronous command.
- Valid data size in bytes of resp\_data\_addr

priv\_data

- Memory address to client context which given during request.

## Field Documentation

## [◆ ](#a4f413e152dc2ef463140499164c3e410)a0

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long sip\_svc\_response::a0 |
| --- |

## [◆ ](#abfb0f411524209388f79f35a82031e79)a1

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long sip\_svc\_response::a1 |
| --- |

## [◆ ](#af973d08da13a7dcecf344f3f9d6f118e)a2

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long sip\_svc\_response::a2 |
| --- |

## [◆ ](#aac8bb11e4661e59cbce0d6b5d50a0820)a3

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long sip\_svc\_response::a3 |
| --- |

## [◆ ](#ab2a3ed6ec283ef83a2ad8ea8eea421be)header

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sip\_svc\_response::header |
| --- |

## [◆ ](#a992b3f936866852633569f9c8d37d6a0)priv\_data

| void\* sip\_svc\_response::priv\_data |
| --- |

## [◆ ](#a5b8a49d292e45ecdd81920c30b650c10)resp\_data\_addr

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sip\_svc\_response::resp\_data\_addr |
| --- |

## [◆ ](#a2e8373be61b16ac4f4d013103539cceb)resp\_data\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sip\_svc\_response::resp\_data\_size |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/sip\_svc/[sip\_svc\_proto.h](sip__svc__proto_8h_source.md)

- [sip\_svc\_response](structsip__svc__response.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
