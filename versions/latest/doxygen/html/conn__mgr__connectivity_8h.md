---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/conn__mgr__connectivity_8h.html
original_path: doxygen/html/conn__mgr__connectivity_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

conn\_mgr\_connectivity.h File Reference

API for controlling generic network association routines on network devices that support it.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/net/net_if.h](net__if_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/net/net_mgmt.h](net__mgmt_8h_source.md)>`

[Go to the source code of this file.](conn__mgr__connectivity_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NET\_EVENT\_CONN\_IF\_TIMEOUT](group__conn__mgr__connectivity.md#ga5ea6e37ca9eda2b6fd8b165b8182dd38)   (\_NET\_MGMT\_CONN\_IF\_EVENT | [NET\_EVENT\_CONN\_CMD\_IF\_TIMEOUT](group__conn__mgr__connectivity.md#ggacd7d3158508b678be598364f001910eaa0accbbb045e2db61a3ab65790b3035d5)) |
|  | net\_mgmt event raised when a connection attempt times out |
| #define | [NET\_EVENT\_CONN\_IF\_FATAL\_ERROR](group__conn__mgr__connectivity.md#gae8f207559a7123bd2eca5ef08086d377)   (\_NET\_MGMT\_CONN\_IF\_EVENT | [NET\_EVENT\_CONN\_CMD\_IF\_FATAL\_ERROR](group__conn__mgr__connectivity.md#ggacd7d3158508b678be598364f001910eaa8f0566c5ef422c202e1e032578afd069)) |
|  | net\_mgmt event raised when a non-recoverable connectivity error occurs on an iface |
| #define | [CONN\_MGR\_IF\_NO\_TIMEOUT](group__conn__mgr__connectivity.md#ga605eee24f4419b5cd6a50a0272979da7)   0 |
|  | Value to use with [conn\_mgr\_if\_set\_timeout](group__conn__mgr__connectivity.md#ga467ecbb330d21b8dfea3e0ce08448400 "conn_mgr_if_set_timeout") and [conn\_mgr\_conn\_binding::timeout](structconn__mgr__conn__binding.md#a8474461cf7b00132441227aae07511ab "conn_mgr_conn_binding::timeout") to indicate no timeout. |

| Enumerations | |
| --- | --- |
| enum | [net\_event\_conn\_cmd](group__conn__mgr__connectivity.md#gacd7d3158508b678be598364f001910ea) { [NET\_EVENT\_CONN\_CMD\_IF\_TIMEOUT](group__conn__mgr__connectivity.md#ggacd7d3158508b678be598364f001910eaa0accbbb045e2db61a3ab65790b3035d5) = 1 , [NET\_EVENT\_CONN\_CMD\_IF\_FATAL\_ERROR](group__conn__mgr__connectivity.md#ggacd7d3158508b678be598364f001910eaa8f0566c5ef422c202e1e032578afd069) } |
| enum | [conn\_mgr\_if\_flag](group__conn__mgr__connectivity.md#gaf10fb532a3dd07ec8c692a72643d0e3f) { [CONN\_MGR\_IF\_PERSISTENT](group__conn__mgr__connectivity.md#ggaf10fb532a3dd07ec8c692a72643d0e3fa0edb461193b3486d06f75fd1da93746f) , [CONN\_MGR\_IF\_NO\_AUTO\_CONNECT](group__conn__mgr__connectivity.md#ggaf10fb532a3dd07ec8c692a72643d0e3fadaf5c01734a04f70f3caf5c841c936dd) , [CONN\_MGR\_IF\_NO\_AUTO\_DOWN](group__conn__mgr__connectivity.md#ggaf10fb532a3dd07ec8c692a72643d0e3fa2b65e55f411eef6b9805c9977097f86d) } |
|  | Per-iface connectivity flags. [More...](group__conn__mgr__connectivity.md#gaf10fb532a3dd07ec8c692a72643d0e3f) |

| Functions | |
| --- | --- |
| int | [conn\_mgr\_if\_connect](group__conn__mgr__connectivity.md#ga575d367c95592fd9f4ead694ff94543f) (struct [net\_if](structnet__if.md) \*iface) |
|  | Connect interface. |
| int | [conn\_mgr\_if\_disconnect](group__conn__mgr__connectivity.md#gada2b5271b3e5dbcab629e1538b3d8eb4) (struct [net\_if](structnet__if.md) \*iface) |
|  | Disconnect interface. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [conn\_mgr\_if\_is\_bound](group__conn__mgr__connectivity.md#ga09a1169a89eac1a3291185281952ce05) (struct [net\_if](structnet__if.md) \*iface) |
|  | Check whether the provided network interface supports connectivity / has been bound to a connectivity implementation. |
| int | [conn\_mgr\_if\_set\_opt](group__conn__mgr__connectivity.md#ga2a2e6d7fbb7b1ed0327706a8c253d3e4) (struct [net\_if](structnet__if.md) \*iface, int optname, const void \*optval, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) optlen) |
|  | Set implementation-specific connectivity options. |
| int | [conn\_mgr\_if\_get\_opt](group__conn__mgr__connectivity.md#gaa79794ce9c773c0c3932121c931ac2d6) (struct [net\_if](structnet__if.md) \*iface, int optname, void \*optval, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*optlen) |
|  | Get implementation-specific connectivity options. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [conn\_mgr\_if\_get\_flag](group__conn__mgr__connectivity.md#ga465c9491106cba3c9cb1cf296090612b) (struct [net\_if](structnet__if.md) \*iface, enum [conn\_mgr\_if\_flag](group__conn__mgr__connectivity.md#gaf10fb532a3dd07ec8c692a72643d0e3f) flag) |
|  | Check the value of connectivity flags. |
| int | [conn\_mgr\_if\_set\_flag](group__conn__mgr__connectivity.md#gae86d1c808f31b8ca5e67bacbc844ef47) (struct [net\_if](structnet__if.md) \*iface, enum [conn\_mgr\_if\_flag](group__conn__mgr__connectivity.md#gaf10fb532a3dd07ec8c692a72643d0e3f) flag, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) value) |
|  | Set the value of a connectivity flags. |
| int | [conn\_mgr\_if\_get\_timeout](group__conn__mgr__connectivity.md#gada9c37847acc604d82604351cbbb5e64) (struct [net\_if](structnet__if.md) \*iface) |
|  | Get the connectivity timeout for an iface. |
| int | [conn\_mgr\_if\_set\_timeout](group__conn__mgr__connectivity.md#ga467ecbb330d21b8dfea3e0ce08448400) (struct [net\_if](structnet__if.md) \*iface, int timeout) |
|  | Set the connectivity timeout for an iface. |
| int | [conn\_mgr\_all\_if\_up](group__conn__mgr__connectivity__bulk.md#ga9e006b8b5095c223d77055fd619710c3) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) skip\_ignored) |
|  | Convenience function that takes all available ifaces into the admin-up state. |
| int | [conn\_mgr\_all\_if\_down](group__conn__mgr__connectivity__bulk.md#gabf6f8e5d8ce51b4c1cbf48f18a57efb2) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) skip\_ignored) |
|  | Convenience function that takes all available ifaces into the admin-down state. |
| int | [conn\_mgr\_all\_if\_connect](group__conn__mgr__connectivity__bulk.md#ga48e3c1b98f505af9f8ac811a25f94e1b) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) skip\_ignored) |
|  | Convenience function that takes all available ifaces into the admin-up state, and connects those that support connectivity. |
| int | [conn\_mgr\_all\_if\_disconnect](group__conn__mgr__connectivity__bulk.md#ga3ce45d9040d3799e1387776257dfa8b7) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) skip\_ignored) |
|  | Convenience function that disconnects all available ifaces that support connectivity without putting them into admin-down state (unless auto-down is enabled for the iface). |

## Detailed Description

API for controlling generic network association routines on network devices that support it.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [conn\_mgr\_connectivity.h](conn__mgr__connectivity_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
