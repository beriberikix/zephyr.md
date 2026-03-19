---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hdlc__rcp__if_8h.html
original_path: doxygen/html/hdlc__rcp__if_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hdlc\_rcp\_if.h File Reference

Public APIs of HDLC RCP communication Interface.
[More...](#details)

`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`

[Go to the source code of this file.](hdlc__rcp__if_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [hdlc\_api](structhdlc__api.md) |
|  | HDLC interface configuration data. [More...](structhdlc__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [hdlc\_rx\_callback\_t](#a58fa03009f99c7927c930b06fd1dfd0e)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, void \*param) |
|  | OT RCP HDLC RX callback function. |

## Detailed Description

Public APIs of HDLC RCP communication Interface.

This file provide the HDLC APIs to be used by an RCP host

## Typedef Documentation

## [◆ ](#a58fa03009f99c7927c930b06fd1dfd0e)hdlc\_rx\_callback\_t

| typedef void(\* hdlc\_rx\_callback\_t) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, void \*param) |
| --- |

OT RCP HDLC RX callback function.

Note
:   This function is called in the radio spinel HDLC level

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [hdlc\_rcp\_if](dir_1af8727946a5235b30f274ca84c43895.md)
- [hdlc\_rcp\_if.h](hdlc__rcp__if_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
