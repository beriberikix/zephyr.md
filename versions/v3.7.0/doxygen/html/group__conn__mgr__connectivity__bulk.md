---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__conn__mgr__connectivity__bulk.html
original_path: doxygen/html/group__conn__mgr__connectivity__bulk.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Connection Manager Connectivity Bulk API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Connection Manager Bulk API.
[More...](#details)

| Functions | |
| --- | --- |
| int | [conn\_mgr\_all\_if\_up](#ga9e006b8b5095c223d77055fd619710c3) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) skip\_ignored) |
|  | Convenience function that takes all available ifaces into the admin-up state. |
| int | [conn\_mgr\_all\_if\_down](#gabf6f8e5d8ce51b4c1cbf48f18a57efb2) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) skip\_ignored) |
|  | Convenience function that takes all available ifaces into the admin-down state. |
| int | [conn\_mgr\_all\_if\_connect](#ga48e3c1b98f505af9f8ac811a25f94e1b) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) skip\_ignored) |
|  | Convenience function that takes all available ifaces into the admin-up state, and connects those that support connectivity. |
| int | [conn\_mgr\_all\_if\_disconnect](#ga3ce45d9040d3799e1387776257dfa8b7) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) skip\_ignored) |
|  | Convenience function that disconnects all available ifaces that support connectivity without putting them into admin-down state (unless auto-down is enabled for the iface). |

## Detailed Description

Connection Manager Bulk API.

## Function Documentation

## [◆ ](#ga48e3c1b98f505af9f8ac811a25f94e1b)conn\_mgr\_all\_if\_connect()

| int conn\_mgr\_all\_if\_connect | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *skip\_ignored* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_connectivity.h](conn__mgr__connectivity_8h.md)>`

Convenience function that takes all available ifaces into the admin-up state, and connects those that support connectivity.

Essentially a wrapper for [net\_if\_up](group__net__if.md#ga02644cc623fc7a8878c17d54984e4210 "net_if_up") and [conn\_mgr\_if\_connect](group__conn__mgr__connectivity.md#ga575d367c95592fd9f4ead694ff94543f "conn_mgr_if_connect").

Parameters
:   | skip\_ignored | - If true, only affect ifaces that aren't ignored by conn\_mgr. Otherwise, affect all ifaces. |
    | --- | --- |

Returns
:   0 if all net\_if\_up and conn\_mgr\_if\_connect calls returned 0, otherwise the first nonzero value returned by either net\_if\_up or conn\_mgr\_if\_connect.

## [◆ ](#ga3ce45d9040d3799e1387776257dfa8b7)conn\_mgr\_all\_if\_disconnect()

| int conn\_mgr\_all\_if\_disconnect | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *skip\_ignored* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_connectivity.h](conn__mgr__connectivity_8h.md)>`

Convenience function that disconnects all available ifaces that support connectivity without putting them into admin-down state (unless auto-down is enabled for the iface).

Essentially a wrapper for [net\_if\_down](group__net__if.md#ga2187650062d6139b9f4b81745a206803 "net_if_down").

Parameters
:   | skip\_ignored | - If true, only affect ifaces that aren't ignored by conn\_mgr. Otherwise, affect all ifaces. |
    | --- | --- |

Returns
:   0 if all net\_if\_up and conn\_mgr\_if\_connect calls returned 0, otherwise the first nonzero value returned by either net\_if\_up or conn\_mgr\_if\_connect.

## [◆ ](#gabf6f8e5d8ce51b4c1cbf48f18a57efb2)conn\_mgr\_all\_if\_down()

| int conn\_mgr\_all\_if\_down | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *skip\_ignored* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_connectivity.h](conn__mgr__connectivity_8h.md)>`

Convenience function that takes all available ifaces into the admin-down state.

Essentially a wrapper for [net\_if\_down](group__net__if.md#ga2187650062d6139b9f4b81745a206803 "net_if_down").

Parameters
:   | skip\_ignored | - If true, only affect ifaces that aren't ignored by conn\_mgr. Otherwise, affect all ifaces. |
    | --- | --- |

Returns
:   0 if all net\_if\_down calls returned 0, otherwise the first nonzero value returned by a net\_if\_down call.

## [◆ ](#ga9e006b8b5095c223d77055fd619710c3)conn\_mgr\_all\_if\_up()

| int conn\_mgr\_all\_if\_up | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *skip\_ignored* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_connectivity.h](conn__mgr__connectivity_8h.md)>`

Convenience function that takes all available ifaces into the admin-up state.

Essentially a wrapper for [net\_if\_up](group__net__if.md#ga02644cc623fc7a8878c17d54984e4210 "net_if_up").

Parameters
:   | skip\_ignored | - If true, only affect ifaces that aren't ignored by conn\_mgr. Otherwise, affect all ifaces. |
    | --- | --- |

Returns
:   0 if all net\_if\_up calls returned 0, otherwise the first nonzero value returned by a net\_if\_up call.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
