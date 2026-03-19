---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structethernet__qav__param.html
original_path: doxygen/html/structethernet__qav__param.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ethernet\_qav\_param Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Ethernet Support Functions](group__ethernet.md)

Ethernet Qav specific parameters.
[More...](#details)

`#include <[ethernet.h](ethernet_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int | [queue\_id](#a4e2d2967669b758422c166140af0c1ba) |
|  | ID of the priority queue to use. |
| enum ethernet\_qav\_param\_type | [type](#a38861d9f790a61aa88801cb1373077a8) |
|  | Type of Qav parameter. |
| union { |  |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [enabled](#a031d3896b14eb8b32c3c050738421b85) |  |
|  | True if Qav is enabled for queue. [More...](#a031d3896b14eb8b32c3c050738421b85) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int   [delta\_bandwidth](#a6fde906da905c0598aaa2056c330b6f4) |  |
|  | Delta Bandwidth (percentage of bandwidth). [More...](#a6fde906da905c0598aaa2056c330b6f4) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int   [idle\_slope](#a6d43b199549cade0a07dc10adac85bff) |  |
|  | Idle Slope (bits per second). [More...](#a6d43b199549cade0a07dc10adac85bff) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int   [oper\_idle\_slope](#a0691f10a338d3c49a58d94a1adced477) |  |
|  | Oper Idle Slope (bits per second). [More...](#a0691f10a338d3c49a58d94a1adced477) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int   [traffic\_class](#a4a795e4a0c7d5bcbe8212d79f772dc6f) |  |
|  | Traffic class the queue is bound to. [More...](#a4a795e4a0c7d5bcbe8212d79f772dc6f) |
| }; |  |

## Detailed Description

Ethernet Qav specific parameters.

## Field Documentation

## [◆ ](#ab79ce599dbace4a983432dfc7a49c416)[union]

| union { ... } [ethernet\_qav\_param](structethernet__qav__param.md) |
| --- |

## [◆ ](#a6fde906da905c0598aaa2056c330b6f4)delta\_bandwidth

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int ethernet\_qav\_param::delta\_bandwidth |
| --- |

Delta Bandwidth (percentage of bandwidth).

## [◆ ](#a031d3896b14eb8b32c3c050738421b85)enabled

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ethernet\_qav\_param::enabled |
| --- |

True if Qav is enabled for queue.

## [◆ ](#a6d43b199549cade0a07dc10adac85bff)idle\_slope

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int ethernet\_qav\_param::idle\_slope |
| --- |

Idle Slope (bits per second).

## [◆ ](#a0691f10a338d3c49a58d94a1adced477)oper\_idle\_slope

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int ethernet\_qav\_param::oper\_idle\_slope |
| --- |

Oper Idle Slope (bits per second).

## [◆ ](#a4e2d2967669b758422c166140af0c1ba)queue\_id

| int ethernet\_qav\_param::queue\_id |
| --- |

ID of the priority queue to use.

## [◆ ](#a4a795e4a0c7d5bcbe8212d79f772dc6f)traffic\_class

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int ethernet\_qav\_param::traffic\_class |
| --- |

Traffic class the queue is bound to.

## [◆ ](#a38861d9f790a61aa88801cb1373077a8)type

| enum ethernet\_qav\_param\_type ethernet\_qav\_param::type |
| --- |

Type of Qav parameter.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ethernet.h](ethernet_8h_source.md)

- [ethernet\_qav\_param](structethernet__qav__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
