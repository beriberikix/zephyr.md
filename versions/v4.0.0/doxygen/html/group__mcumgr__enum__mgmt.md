---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__mcumgr__enum__mgmt.html
original_path: doxygen/html/group__mcumgr__enum__mgmt.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MCUmgr enum\_mgmt API

[Operating System Services](group__os__services.md) » [MCUmgr](group__mcumgr.md)

MCUmgr enum\_mgmt API.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [ENUM\_MGMT\_ID\_COUNT](#gab16f2823b9bb4140a2fc336af5d16d2b)   0 |
|  | Command IDs for enumeration management group. |
| #define | [ENUM\_MGMT\_ID\_LIST](#ga9b6c5a3021a30f8f6a83694ff9a07bf4)   1 |
| #define | [ENUM\_MGMT\_ID\_SINGLE](#ga5b08e51b1e32c27da5597fab4f68f94e)   2 |
| #define | [ENUM\_MGMT\_ID\_DETAILS](#ga03edf25ed33ccdf00b0a21ee574e1b4d)   3 |

| Enumerations | |
| --- | --- |
| enum | [enum\_mgmt\_err\_code\_t](#gaceaae2d8284b4a64b1303513e6aa3099) {     [ENUM\_MGMT\_ERR\_OK](#ggaceaae2d8284b4a64b1303513e6aa3099aab31067e337c3220232e8eb3b3d885c0) = 0 , [ENUM\_MGMT\_ERR\_UNKNOWN](#ggaceaae2d8284b4a64b1303513e6aa3099a7f535a752e4c789024e4fecb5cdd7c7f) , [ENUM\_MGMT\_ERR\_TOO\_MANY\_GROUP\_ENTRIES](#ggaceaae2d8284b4a64b1303513e6aa3099a7866b895eac198fe6eb021ef385a185e) , [ENUM\_MGMT\_ERR\_INSUFFICIENT\_HEAP\_FOR\_ENTRIES](#ggaceaae2d8284b4a64b1303513e6aa3099ac056ab2ae764f50715d9ee478bc0c153) ,     [ENUM\_MGMT\_ERR\_INDEX\_TOO\_LARGE](#ggaceaae2d8284b4a64b1303513e6aa3099af2dff8560e72db54fea41a6345aa5f72)   } |
|  | Command result codes for enumeration management group. [More...](#gaceaae2d8284b4a64b1303513e6aa3099) |

## Detailed Description

MCUmgr enum\_mgmt API.

## Macro Definition Documentation

## [◆ ](#gab16f2823b9bb4140a2fc336af5d16d2b)ENUM\_MGMT\_ID\_COUNT

| #define ENUM\_MGMT\_ID\_COUNT   0 |
| --- |

`#include <[enum_mgmt.h](enum__mgmt_8h.md)>`

Command IDs for enumeration management group.

## [◆ ](#ga03edf25ed33ccdf00b0a21ee574e1b4d)ENUM\_MGMT\_ID\_DETAILS

| #define ENUM\_MGMT\_ID\_DETAILS   3 |
| --- |

`#include <[enum_mgmt.h](enum__mgmt_8h.md)>`

## [◆ ](#ga9b6c5a3021a30f8f6a83694ff9a07bf4)ENUM\_MGMT\_ID\_LIST

| #define ENUM\_MGMT\_ID\_LIST   1 |
| --- |

`#include <[enum_mgmt.h](enum__mgmt_8h.md)>`

## [◆ ](#ga5b08e51b1e32c27da5597fab4f68f94e)ENUM\_MGMT\_ID\_SINGLE

| #define ENUM\_MGMT\_ID\_SINGLE   2 |
| --- |

`#include <[enum_mgmt.h](enum__mgmt_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#gaceaae2d8284b4a64b1303513e6aa3099)enum\_mgmt\_err\_code\_t

| enum [enum\_mgmt\_err\_code\_t](#gaceaae2d8284b4a64b1303513e6aa3099) |
| --- |

`#include <[enum_mgmt.h](enum__mgmt_8h.md)>`

Command result codes for enumeration management group.

| Enumerator | |
| --- | --- |
| ENUM\_MGMT\_ERR\_OK | No error, this is implied if there is no ret value in the response. |
| ENUM\_MGMT\_ERR\_UNKNOWN | Unknown error occurred. |
| ENUM\_MGMT\_ERR\_TOO\_MANY\_GROUP\_ENTRIES | Too many entries were provided. |
| ENUM\_MGMT\_ERR\_INSUFFICIENT\_HEAP\_FOR\_ENTRIES | Insufficient heap memory to store entry data. |
| ENUM\_MGMT\_ERR\_INDEX\_TOO\_LARGE | Provided index is larger than the number of supported grouped. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
