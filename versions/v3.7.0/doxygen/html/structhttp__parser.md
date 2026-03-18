---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structhttp__parser.html
original_path: doxygen/html/structhttp__parser.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

http\_parser Struct Reference

`#include <[parser.h](parser_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [type](#ac6c327558547d55eb64a8aea1310cc2e): 2 |
|  | PRIVATE. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [flags](#a5e54708e0cb3f9ced19bd829dcdeaf53): 8 |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [state](#a6f5952e0b47c83aeacf64fc287fd8003): 7 |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [header\_state](#ac5b254b99c6472ca19ae1f426758ce75): 7 |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [index](#a6f7ba706f975f447b3bf72be97facdf8): 7 |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [lenient\_http\_headers](#acd80a931fcc87d41999397af1662fc3c): 1 |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [nread](#a78085ca896bb3b9aa1ecb0f6fddc039d) |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [content\_length](#a7fd5a194802b1206bb773e096d291f29) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short | [http\_major](#ac994a4a8268652f5ce82de5bde5c3f9d) |
|  | READ-ONLY. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short | [http\_minor](#ae8af6433c824f5348773842db62ad4ab) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [status\_code](#a82f5aed92ca3566489def7bc384bab26): 16 |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [method](#a7955de339fafd81ad54380845913457d): 8 |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [http\_errno](#ab8638d65fa174bc1925d77e2533117fa): 7 |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [upgrade](#a748f476eacc5ac56b84dd07dbafb42a4): 1 |
| void \* | [data](#a7e87ce57b97f60f1fdb7039a8ecb0bca) |
|  | PUBLIC. |
| const struct [sockaddr](structsockaddr.md) \* | [addr](#aecffbbbfebfc4f4a8cb4c034d18ef375) |

## Field Documentation

## [◆ ](#aecffbbbfebfc4f4a8cb4c034d18ef375)addr

| const struct [sockaddr](structsockaddr.md)\* http\_parser::addr |
| --- |

## [◆ ](#a7fd5a194802b1206bb773e096d291f29)content\_length

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) http\_parser::content\_length |
| --- |

## [◆ ](#a7e87ce57b97f60f1fdb7039a8ecb0bca)data

| void\* http\_parser::data |
| --- |

PUBLIC.

## [◆ ](#a5e54708e0cb3f9ced19bd829dcdeaf53)flags

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int http\_parser::flags |
| --- |

## [◆ ](#ac5b254b99c6472ca19ae1f426758ce75)header\_state

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int http\_parser::header\_state |
| --- |

## [◆ ](#ab8638d65fa174bc1925d77e2533117fa)http\_errno

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int http\_parser::http\_errno |
| --- |

## [◆ ](#ac994a4a8268652f5ce82de5bde5c3f9d)http\_major

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short http\_parser::http\_major |
| --- |

READ-ONLY.

## [◆ ](#ae8af6433c824f5348773842db62ad4ab)http\_minor

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) short http\_parser::http\_minor |
| --- |

## [◆ ](#a6f7ba706f975f447b3bf72be97facdf8)index

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int http\_parser::index |
| --- |

## [◆ ](#acd80a931fcc87d41999397af1662fc3c)lenient\_http\_headers

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int http\_parser::lenient\_http\_headers |
| --- |

## [◆ ](#a7955de339fafd81ad54380845913457d)method

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int http\_parser::method |
| --- |

## [◆ ](#a78085ca896bb3b9aa1ecb0f6fddc039d)nread

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) http\_parser::nread |
| --- |

## [◆ ](#a6f5952e0b47c83aeacf64fc287fd8003)state

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int http\_parser::state |
| --- |

## [◆ ](#a82f5aed92ca3566489def7bc384bab26)status\_code

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int http\_parser::status\_code |
| --- |

## [◆ ](#ac6c327558547d55eb64a8aea1310cc2e)type

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int http\_parser::type |
| --- |

PRIVATE.

## [◆ ](#a748f476eacc5ac56b84dd07dbafb42a4)upgrade

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int http\_parser::upgrade |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/http/[parser.h](parser_8h_source.md)

- [http\_parser](structhttp__parser.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
