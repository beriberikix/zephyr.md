---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__conn__mgr.html
original_path: doxygen/html/group__conn__mgr.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Connection Manager API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Connection Manager API.
[More...](#details)

| Functions | |
| --- | --- |
| void | [conn\_mgr\_mon\_resend\_status](#gacdde95f41f32e7a829d8cd3a6d0e2277) (void) |
|  | Resend either NET\_L4\_CONNECTED or NET\_L4\_DISCONNECTED depending on whether connectivity is currently available. |
| void | [conn\_mgr\_ignore\_iface](#ga7bad393c43a24df7a03176830b05b288) (struct [net\_if](structnet__if.md) \*iface) |
|  | Mark an iface to be ignored by conn\_mgr. |
| void | [conn\_mgr\_watch\_iface](#gacc8735b835dea9b31531fcca9fe8a979) (struct [net\_if](structnet__if.md) \*iface) |
|  | Watch (stop ignoring) an iface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [conn\_mgr\_is\_iface\_ignored](#gada16a88ec2c1db71fc39782b0696dac2) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check whether the provided iface is currently ignored. |
| void | [conn\_mgr\_ignore\_l2](#ga6bd1ee46dc2e3dae554fce49e82c6187) (const struct [net\_l2](structnet__l2.md) \*l2) |
|  | Mark an L2 to be ignored by conn\_mgr. |
| void | [conn\_mgr\_watch\_l2](#gad96056478dcbcb568dd2ef8d5d2ad50b) (const struct [net\_l2](structnet__l2.md) \*l2) |
|  | Watch (stop ignoring) an L2. |

## Detailed Description

Connection Manager API.

## Function Documentation

## [◆ ](#ga7bad393c43a24df7a03176830b05b288)conn\_mgr\_ignore\_iface()

| void conn\_mgr\_ignore\_iface | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_monitor.h](conn__mgr__monitor_8h.md)>`

Mark an iface to be ignored by conn\_mgr.

Ignoring an iface forces conn\_mgr to consider it unready/disconnected.

This means that events related to the iface connecting/disconnecting will not be fired, and if the iface was connected before being ignored, events will be fired as though it disconnected at that moment.

Parameters
:   | iface | iface to be ignored. |
    | --- | --- |

## [◆ ](#ga6bd1ee46dc2e3dae554fce49e82c6187)conn\_mgr\_ignore\_l2()

| void conn\_mgr\_ignore\_l2 | ( | const struct [net\_l2](structnet__l2.md) \* | *l2* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_monitor.h](conn__mgr__monitor_8h.md)>`

Mark an L2 to be ignored by conn\_mgr.

This is a wrapper for conn\_mgr\_ignore\_iface that ignores all ifaces that use the L2.

Parameters
:   | l2 | L2 to be ignored. |
    | --- | --- |

## [◆ ](#gada16a88ec2c1db71fc39782b0696dac2)conn\_mgr\_is\_iface\_ignored()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) conn\_mgr\_is\_iface\_ignored | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_monitor.h](conn__mgr__monitor_8h.md)>`

Check whether the provided iface is currently ignored.

Parameters
:   | iface | The iface to check. |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if the iface is being ignored by conn\_mgr. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if the iface is being watched by conn\_mgr. |

## [◆ ](#gacdde95f41f32e7a829d8cd3a6d0e2277)conn\_mgr\_mon\_resend\_status()

| void conn\_mgr\_mon\_resend\_status | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_monitor.h](conn__mgr__monitor_8h.md)>`

Resend either NET\_L4\_CONNECTED or NET\_L4\_DISCONNECTED depending on whether connectivity is currently available.

## [◆ ](#gacc8735b835dea9b31531fcca9fe8a979)conn\_mgr\_watch\_iface()

| void conn\_mgr\_watch\_iface | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_monitor.h](conn__mgr__monitor_8h.md)>`

Watch (stop ignoring) an iface.

conn\_mgr will no longer be forced to consider the iface unreadly/disconnected.

Events related to the iface connecting/disconnecting will no longer be blocked, and if the iface was connected before being watched, events will be fired as though it connected in that moment.

All ifaces default to watched at boot.

Parameters
:   | iface | iface to no longer ignore. |
    | --- | --- |

## [◆ ](#gad96056478dcbcb568dd2ef8d5d2ad50b)conn\_mgr\_watch\_l2()

| void conn\_mgr\_watch\_l2 | ( | const struct [net\_l2](structnet__l2.md) \* | *l2* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_monitor.h](conn__mgr__monitor_8h.md)>`

Watch (stop ignoring) an L2.

This is a wrapper for conn\_mgr\_watch\_iface that watches all ifaces that use the L2.

Parameters
:   | l2 | L2 to watch. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
