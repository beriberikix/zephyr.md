---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structshell__rpmsg.html
original_path: doxygen/html/structshell__rpmsg.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_rpmsg Struct Reference

RPMsg-based shell transport.
[More...](#details)

`#include <[shell_rpmsg.h](shell__rpmsg_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) | [shell\_handler](#a72307140d40e6dd9cb735e3141d66f69) |
|  | Handler function registered by shell. |
| void \* | [shell\_context](#ae2d42a908ddd784e8a792ecd47700d18) |
|  | Context registered by shell. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [ready](#ace1a7aefb13b92f5167dd4d3af3c39e9) |
|  | Indicator if we are ready to read/write. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [blocking](#aca5ea2487d3712f9fdeb6f90043cbf53) |
|  | Setting for blocking mode. |
| struct rpmsg\_endpoint | [ept](#ae2f9b114e042df5fd83fcec9c2784df3) |
|  | RPMsg endpoint. |
| struct [k\_msgq](structk__msgq.md) | [rx\_q](#ac8e38cdb8c3ffe1f630126e085238cc9) |
|  | Queue for received data. |
| struct [shell\_rpmsg\_rx](structshell__rpmsg__rx.md) | [rx\_buf](#a9bd628e39d3f7fb766d0c33b378e3cdb) [CONFIG\_SHELL\_RPMSG\_MAX\_RX] |
|  | Buffer for received messages. |
| struct [shell\_rpmsg\_rx](structshell__rpmsg__rx.md) | [rx\_cur](#a03fad4774300bfd923aafdd660b258df) |
|  | The current rx message. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [rx\_consumed](#a358e50712674ada1d01a22394e79f964) |
|  | The number of bytes consumed from rx\_cur. |

## Detailed Description

RPMsg-based shell transport.

## Field Documentation

## [◆ ](#aca5ea2487d3712f9fdeb6f90043cbf53)blocking

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) shell\_rpmsg::blocking |
| --- |

Setting for blocking mode.

## [◆ ](#ae2f9b114e042df5fd83fcec9c2784df3)ept

| struct rpmsg\_endpoint shell\_rpmsg::ept |
| --- |

RPMsg endpoint.

## [◆ ](#ace1a7aefb13b92f5167dd4d3af3c39e9)ready

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) shell\_rpmsg::ready |
| --- |

Indicator if we are ready to read/write.

## [◆ ](#a9bd628e39d3f7fb766d0c33b378e3cdb)rx\_buf

| struct [shell\_rpmsg\_rx](structshell__rpmsg__rx.md) shell\_rpmsg::rx\_buf[CONFIG\_SHELL\_RPMSG\_MAX\_RX] |
| --- |

Buffer for received messages.

## [◆ ](#a358e50712674ada1d01a22394e79f964)rx\_consumed

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) shell\_rpmsg::rx\_consumed |
| --- |

The number of bytes consumed from rx\_cur.

## [◆ ](#a03fad4774300bfd923aafdd660b258df)rx\_cur

| struct [shell\_rpmsg\_rx](structshell__rpmsg__rx.md) shell\_rpmsg::rx\_cur |
| --- |

The current rx message.

## [◆ ](#ac8e38cdb8c3ffe1f630126e085238cc9)rx\_q

| struct [k\_msgq](structk__msgq.md) shell\_rpmsg::rx\_q |
| --- |

Queue for received data.

## [◆ ](#ae2d42a908ddd784e8a792ecd47700d18)shell\_context

| void\* shell\_rpmsg::shell\_context |
| --- |

Context registered by shell.

## [◆ ](#a72307140d40e6dd9cb735e3141d66f69)shell\_handler

| [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) shell\_rpmsg::shell\_handler |
| --- |

Handler function registered by shell.

---

The documentation for this struct was generated from the following file:

- zephyr/shell/[shell\_rpmsg.h](shell__rpmsg_8h_source.md)

- [shell\_rpmsg](structshell__rpmsg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
