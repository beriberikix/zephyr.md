---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__conn__mgr__connectivity.html
original_path: doxygen/html/group__conn__mgr__connectivity.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Connection Manager Connectivity API

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Connection Manager Connectivity API.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Connection Manager Connectivity Bulk API](group__conn__mgr__connectivity__bulk.md) |
|  | Connection Manager Bulk API. |
|  | [Connection Manager Connectivity Implementation API](group__conn__mgr__connectivity__impl.md) |
|  | Connection Manager Connectivity Implementation API. |

| Macros | |
| --- | --- |
| #define | [NET\_EVENT\_CONN\_IF\_TIMEOUT](#ga5ea6e37ca9eda2b6fd8b165b8182dd38)   (\_NET\_MGMT\_CONN\_IF\_EVENT | NET\_EVENT\_CONN\_CMD\_IF\_TIMEOUT) |
|  | net\_mgmt event raised when a connection attempt times out |
| #define | [NET\_EVENT\_CONN\_IF\_FATAL\_ERROR](#gae8f207559a7123bd2eca5ef08086d377)   (\_NET\_MGMT\_CONN\_IF\_EVENT | NET\_EVENT\_CONN\_CMD\_IF\_FATAL\_ERROR) |
|  | net\_mgmt event raised when a non-recoverable connectivity error occurs on an iface |
| #define | [CONN\_MGR\_IF\_NO\_TIMEOUT](#ga605eee24f4419b5cd6a50a0272979da7)   0 |
|  | Value to use with [conn\_mgr\_if\_set\_timeout](#ga467ecbb330d21b8dfea3e0ce08448400) and [conn\_mgr\_conn\_binding::timeout](structconn__mgr__conn__binding.md#a8474461cf7b00132441227aae07511ab "conn_mgr_conn_binding::timeout") to indicate no timeout. |

| Enumerations | |
| --- | --- |
| enum | [conn\_mgr\_if\_flag](#gaf10fb532a3dd07ec8c692a72643d0e3f) { [CONN\_MGR\_IF\_PERSISTENT](#ggaf10fb532a3dd07ec8c692a72643d0e3fa0edb461193b3486d06f75fd1da93746f) , [CONN\_MGR\_IF\_NO\_AUTO\_CONNECT](#ggaf10fb532a3dd07ec8c692a72643d0e3fadaf5c01734a04f70f3caf5c841c936dd) , [CONN\_MGR\_IF\_NO\_AUTO\_DOWN](#ggaf10fb532a3dd07ec8c692a72643d0e3fa2b65e55f411eef6b9805c9977097f86d) } |
|  | Per-iface connectivity flags. [More...](#gaf10fb532a3dd07ec8c692a72643d0e3f) |

| Functions | |
| --- | --- |
| int | [conn\_mgr\_if\_connect](#ga575d367c95592fd9f4ead694ff94543f) (struct [net\_if](structnet__if.md) \*iface) |
|  | Connect interface. |
| int | [conn\_mgr\_if\_disconnect](#gada2b5271b3e5dbcab629e1538b3d8eb4) (struct [net\_if](structnet__if.md) \*iface) |
|  | Disconnect interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [conn\_mgr\_if\_is\_bound](#ga09a1169a89eac1a3291185281952ce05) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check whether the provided network interface supports connectivity / has been bound to a connectivity implementation. |
| int | [conn\_mgr\_if\_set\_opt](#ga2a2e6d7fbb7b1ed0327706a8c253d3e4) (struct [net\_if](structnet__if.md) \*iface, int optname, const void \*optval, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) optlen) |
|  | Set implementation-specific connectivity options. |
| int | [conn\_mgr\_if\_get\_opt](#gaa79794ce9c773c0c3932121c931ac2d6) (struct [net\_if](structnet__if.md) \*iface, int optname, void \*optval, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*optlen) |
|  | Get implementation-specific connectivity options. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [conn\_mgr\_if\_get\_flag](#ga465c9491106cba3c9cb1cf296090612b) (struct [net\_if](structnet__if.md) \*iface, enum [conn\_mgr\_if\_flag](#gaf10fb532a3dd07ec8c692a72643d0e3f) flag) |
|  | Check the value of connectivity flags. |
| int | [conn\_mgr\_if\_set\_flag](#gae86d1c808f31b8ca5e67bacbc844ef47) (struct [net\_if](structnet__if.md) \*iface, enum [conn\_mgr\_if\_flag](#gaf10fb532a3dd07ec8c692a72643d0e3f) flag, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) value) |
|  | Set the value of a connectivity flags. |
| int | [conn\_mgr\_if\_get\_timeout](#gada9c37847acc604d82604351cbbb5e64) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get the connectivity timeout for an iface. |
| int | [conn\_mgr\_if\_set\_timeout](#ga467ecbb330d21b8dfea3e0ce08448400) (struct [net\_if](structnet__if.md) \*iface, int timeout) |
|  | Set the connectivity timeout for an iface. |

## Detailed Description

Connection Manager Connectivity API.

Since
:   3.4

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga605eee24f4419b5cd6a50a0272979da7)CONN\_MGR\_IF\_NO\_TIMEOUT

| #define CONN\_MGR\_IF\_NO\_TIMEOUT   0 |
| --- |

`#include <[conn_mgr_connectivity.h](conn__mgr__connectivity_8h.md)>`

Value to use with [conn\_mgr\_if\_set\_timeout](#ga467ecbb330d21b8dfea3e0ce08448400) and [conn\_mgr\_conn\_binding::timeout](structconn__mgr__conn__binding.md#a8474461cf7b00132441227aae07511ab "conn_mgr_conn_binding::timeout") to indicate no timeout.

## [◆ ](#gae8f207559a7123bd2eca5ef08086d377)NET\_EVENT\_CONN\_IF\_FATAL\_ERROR

| #define NET\_EVENT\_CONN\_IF\_FATAL\_ERROR   (\_NET\_MGMT\_CONN\_IF\_EVENT | NET\_EVENT\_CONN\_CMD\_IF\_FATAL\_ERROR) |
| --- |

`#include <[conn_mgr_connectivity.h](conn__mgr__connectivity_8h.md)>`

net\_mgmt event raised when a non-recoverable connectivity error occurs on an iface

## [◆ ](#ga5ea6e37ca9eda2b6fd8b165b8182dd38)NET\_EVENT\_CONN\_IF\_TIMEOUT

| #define NET\_EVENT\_CONN\_IF\_TIMEOUT   (\_NET\_MGMT\_CONN\_IF\_EVENT | NET\_EVENT\_CONN\_CMD\_IF\_TIMEOUT) |
| --- |

`#include <[conn_mgr_connectivity.h](conn__mgr__connectivity_8h.md)>`

net\_mgmt event raised when a connection attempt times out

## Enumeration Type Documentation

## [◆ ](#gaf10fb532a3dd07ec8c692a72643d0e3f)conn\_mgr\_if\_flag

| enum [conn\_mgr\_if\_flag](#gaf10fb532a3dd07ec8c692a72643d0e3f) |
| --- |

`#include <[conn_mgr_connectivity.h](conn__mgr__connectivity_8h.md)>`

Per-iface connectivity flags.

| Enumerator | |
| --- | --- |
| CONN\_MGR\_IF\_PERSISTENT | Persistent.  When set, indicates that the connectivity implementation bound to this iface should attempt to persist connectivity by automatically reconnecting after connection loss. |
| CONN\_MGR\_IF\_NO\_AUTO\_CONNECT | No auto-connect.  When set, conn\_mgr will not automatically attempt to connect this iface when it reaches admin-up. |
| CONN\_MGR\_IF\_NO\_AUTO\_DOWN | No auto-down.  When set, conn\_mgr will not automatically take the iface admin-down when it stops trying to connect, even if CONFIG\_NET\_CONNECTION\_MANAGER\_AUTO\_IF\_DOWN is enabled. |

## Function Documentation

## [◆ ](#ga575d367c95592fd9f4ead694ff94543f)conn\_mgr\_if\_connect()

| int conn\_mgr\_if\_connect | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_connectivity.h](conn__mgr__connectivity_8h.md)>`

Connect interface.

If the provided iface has been bound to a connectivity implementation, initiate network connect/association.

Automatically takes the iface admin-up (by calling [net\_if\_up](group__net__if.md#ga02644cc623fc7a8878c17d54984e4210 "net_if_up")) if it isn't already.

Non-Blocking.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ESHUTDOWN | if the iface is not admin-up. |
    | -ENOTSUP | if the iface does not have a connectivity implementation. |
    | implementation-specific | status code otherwise. |

## [◆ ](#gada2b5271b3e5dbcab629e1538b3d8eb4)conn\_mgr\_if\_disconnect()

| int conn\_mgr\_if\_disconnect | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_connectivity.h](conn__mgr__connectivity_8h.md)>`

Disconnect interface.

If the provided iface has been bound to a connectivity implementation, disconnect/disassociate it from the network, and cancel any pending attempts to connect/associate.

Does nothing if the iface is currently admin-down.

Parameters
:   | iface | Pointer to network interface |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOTSUP | if the iface does not have a connectivity implementation. |
    | implementation-specific | status code otherwise. |

## [◆ ](#ga465c9491106cba3c9cb1cf296090612b)conn\_mgr\_if\_get\_flag()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) conn\_mgr\_if\_get\_flag | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | enum [conn\_mgr\_if\_flag](#gaf10fb532a3dd07ec8c692a72643d0e3f) | *flag* ) |

`#include <[conn_mgr_connectivity.h](conn__mgr__connectivity_8h.md)>`

Check the value of connectivity flags.

If the provided iface is bound to a connectivity implementation, retrieves the value of the specified connectivity flag associated with that iface.

Parameters
:   | iface | - Pointer to the network interface to check. |
    | --- | --- |
    | flag | - The flag to check. |

Returns
:   True if the flag is set, otherwise False. Also returns False if the provided iface is not bound to a connectivity implementation, or the requested flag doesn't exist.

## [◆ ](#gaa79794ce9c773c0c3932121c931ac2d6)conn\_mgr\_if\_get\_opt()

| int conn\_mgr\_if\_get\_opt | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | int | *optname*, |
|  |  | void \* | *optval*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *optlen* ) |

`#include <[conn_mgr_connectivity.h](conn__mgr__connectivity_8h.md)>`

Get implementation-specific connectivity options.

If the provided iface has been bound to a connectivity implementation that supports it, retrieves implementation-specific connectivity options related to the iface.

Parameters
:   | iface | Pointer to the network interface. |
    | --- | --- |
    | optname | Integer value representing the option to set. The meaning of values is up to the [conn\_mgr\_conn\_api](structconn__mgr__conn__api.md "Connectivity Manager Connectivity API structure.") implementation. Some settings may be shared by multiple ifaces. |
    | optval | Pointer to where the retrieved value should be stored. |
    | optlen | Pointer to length (in bytes) of the destination buffer available for storing the retrieved value. If the available space is less than what is needed, -ENOBUFS is returned. If the available space is invalid, -EINVAL is returned. |

optlen will always be set to the total number of bytes written, regardless of whether an error is returned, even if zero bytes were written.

Return values
:   | 0 | if successful. |
    | --- | --- |
    | -ENOTSUP | if conn\_mgr\_if\_get\_opt is not implemented by the iface. |
    | -ENOBUFS | if retrieval buffer is too small. |
    | -EINVAL | if invalid retrieval buffer length is provided, or if NULL optval or optlen pointer provided. |
    | -ENOPROTOOPT | if the optname is not recognized. |
    | implementation-specific | error code otherwise. |

## [◆ ](#gada9c37847acc604d82604351cbbb5e64)conn\_mgr\_if\_get\_timeout()

| int conn\_mgr\_if\_get\_timeout | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_connectivity.h](conn__mgr__connectivity_8h.md)>`

Get the connectivity timeout for an iface.

If the provided iface is bound to a connectivity implementation, retrieves the timeout setting in seconds for it.

Parameters
:   | iface | - Pointer to the iface to check. |
    | --- | --- |

Returns
:   int - The connectivity timeout value (in seconds) if it could be retrieved, otherwise CONN\_MGR\_IF\_NO\_TIMEOUT.

## [◆ ](#ga09a1169a89eac1a3291185281952ce05)conn\_mgr\_if\_is\_bound()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) conn\_mgr\_if\_is\_bound | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[conn_mgr_connectivity.h](conn__mgr__connectivity_8h.md)>`

Check whether the provided network interface supports connectivity / has been bound to a connectivity implementation.

Parameters
:   | iface | Pointer to the iface to check. |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if connectivity is supported (a connectivity implementation has been bound). |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | otherwise. |

## [◆ ](#gae86d1c808f31b8ca5e67bacbc844ef47)conn\_mgr\_if\_set\_flag()

| int conn\_mgr\_if\_set\_flag | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | enum [conn\_mgr\_if\_flag](#gaf10fb532a3dd07ec8c692a72643d0e3f) | *flag*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *value* ) |

`#include <[conn_mgr_connectivity.h](conn__mgr__connectivity_8h.md)>`

Set the value of a connectivity flags.

If the provided iface is bound to a connectivity implementation, sets the value of the specified connectivity flag associated with that iface.

Parameters
:   | iface | - Pointer to the network interface to modify. |
    | --- | --- |
    | flag | - The flag to set. |
    | value | - Whether the flag should be enabled or disabled. |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EINVAL | if the flag does not exist. |
    | -ENOTSUP | if the provided iface is not bound to a connectivity implementation. |

## [◆ ](#ga2a2e6d7fbb7b1ed0327706a8c253d3e4)conn\_mgr\_if\_set\_opt()

| int conn\_mgr\_if\_set\_opt | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | int | *optname*, |
|  |  | const void \* | *optval*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *optlen* ) |

`#include <[conn_mgr_connectivity.h](conn__mgr__connectivity_8h.md)>`

Set implementation-specific connectivity options.

If the provided iface has been bound to a connectivity implementation that supports it, implementation-specific connectivity options related to the iface.

Parameters
:   | iface | Pointer to the network interface. |
    | --- | --- |
    | optname | Integer value representing the option to set. The meaning of values is up to the [conn\_mgr\_conn\_api](structconn__mgr__conn__api.md "Connectivity Manager Connectivity API structure.") implementation. Some settings may affect multiple ifaces. |
    | optval | Pointer to the value to be assigned to the option. |
    | optlen | Length (in bytes) of the value to be assigned to the option. |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | -ENOTSUP | if conn\_mgr\_if\_set\_opt not implemented by the iface. |
    | -ENOBUFS | if optlen is too long. |
    | -EINVAL | if NULL optval pointer provided. |
    | -ENOPROTOOPT | if the optname is not recognized. |
    | implementation-specific | error code otherwise. |

## [◆ ](#ga467ecbb330d21b8dfea3e0ce08448400)conn\_mgr\_if\_set\_timeout()

| int conn\_mgr\_if\_set\_timeout | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | int | *timeout* ) |

`#include <[conn_mgr_connectivity.h](conn__mgr__connectivity_8h.md)>`

Set the connectivity timeout for an iface.

If the provided iface is bound to a connectivity implementation, sets the timeout setting in seconds for it.

Parameters
:   | iface | - Pointer to the network interface to modify. |
    | --- | --- |
    | timeout | - The timeout value to set (in seconds). Pass [CONN\_MGR\_IF\_NO\_TIMEOUT](#ga605eee24f4419b5cd6a50a0272979da7) to disable the timeout. |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOTSUP | if the provided iface is not bound to a connectivity implementation. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
