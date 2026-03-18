---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsip__svc__request.html
original_path: doxygen/html/structsip__svc__request.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sip\_svc\_request Struct Reference

SiP Service communication protocol request format.
[More...](#details)

`#include <[sip_svc_proto.h](sip__svc__proto_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [header](#aa8c71f7af00dd3195d49c04df5cb3509) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a0](#a95e4d0bb03bfca90ea78fc19c581ef7f) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a1](#a3b41176de28f042510d5ca5fc9c4678e) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a2](#aa20d78ab299064e8d4b304f4165bfdf2) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a3](#a6cd5c3cf895daad0c600544a903f2eb8) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a4](#a8d827ae174a2b8f11b50c7e6f31c3708) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a5](#a67c7626f24035b9cdfef24193e2442c6) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a6](#a35198a51b070fb2acf76458568204ec1) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | [a7](#af20b0881ec14973d7a6b79f3b146dc7a) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [resp\_data\_addr](#a9b4cc837fbb958e93a900b58b2ea3a75) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [resp\_data\_size](#aff7c782bc6690ef134db4e4d999189a7) |
| void \* | [priv\_data](#a0b70942fc037346bb5ee051484c21745) |

## Detailed Description

SiP Service communication protocol request format.

request header

- bits [15: 0] Arm SiP services command code
- bits [23:16] Transaction ID (Filled in by sip\_svc service)
- bits [29:24] Unused. Reserved.
- bits [31:30] Arm SiP services communication protocol version

a0 - a7

- User input data to be filled into a0-a7 registers when trigger SMC/HVC

resp\_data\_addr

- This parameter only used by asynchronous command.
- Dynamic memory address for service to put the asynchronous response data. The service will free this memory space if the client has cancelled the transaction.

resp\_data\_size

- This parameter only used by asynchronous command.
- Maximum memory size in bytes of resp\_data\_addr

priv\_data

- Memory address to client context. Service will pass this address back to client in response format via callback.

## Field Documentation

## [◆ ](#a95e4d0bb03bfca90ea78fc19c581ef7f)a0

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long sip\_svc\_request::a0 |
| --- |

## [◆ ](#a3b41176de28f042510d5ca5fc9c4678e)a1

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long sip\_svc\_request::a1 |
| --- |

## [◆ ](#aa20d78ab299064e8d4b304f4165bfdf2)a2

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long sip\_svc\_request::a2 |
| --- |

## [◆ ](#a6cd5c3cf895daad0c600544a903f2eb8)a3

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long sip\_svc\_request::a3 |
| --- |

## [◆ ](#a8d827ae174a2b8f11b50c7e6f31c3708)a4

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long sip\_svc\_request::a4 |
| --- |

## [◆ ](#a67c7626f24035b9cdfef24193e2442c6)a5

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long sip\_svc\_request::a5 |
| --- |

## [◆ ](#a35198a51b070fb2acf76458568204ec1)a6

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long sip\_svc\_request::a6 |
| --- |

## [◆ ](#af20b0881ec14973d7a6b79f3b146dc7a)a7

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long sip\_svc\_request::a7 |
| --- |

## [◆ ](#aa8c71f7af00dd3195d49c04df5cb3509)header

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sip\_svc\_request::header |
| --- |

## [◆ ](#a0b70942fc037346bb5ee051484c21745)priv\_data

| void\* sip\_svc\_request::priv\_data |
| --- |

## [◆ ](#a9b4cc837fbb958e93a900b58b2ea3a75)resp\_data\_addr

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sip\_svc\_request::resp\_data\_addr |
| --- |

## [◆ ](#aff7c782bc6690ef134db4e4d999189a7)resp\_data\_size

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sip\_svc\_request::resp\_data\_size |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/sip\_svc/[sip\_svc\_proto.h](sip__svc__proto_8h_source.md)

- [sip\_svc\_request](structsip__svc__request.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
