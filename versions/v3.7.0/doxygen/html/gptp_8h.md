---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/gptp_8h.html
original_path: doxygen/html/gptp_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gptp.h File Reference

Public functions for the Precision Time Protocol Stack.
[More...](#details)

`#include <[zephyr/net/net_core.h](net__core_8h_source.md)>`  
`#include <[zephyr/net/ptp_time.h](ptp__time_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](gptp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [gptp\_scaled\_ns](structgptp__scaled__ns.md) |
|  | Scaled Nanoseconds. [More...](structgptp__scaled__ns.md#details) |
| struct | [gptp\_uscaled\_ns](structgptp__uscaled__ns.md) |
|  | UScaled Nanoseconds. [More...](structgptp__uscaled__ns.md#details) |
| struct | [gptp\_port\_identity](structgptp__port__identity.md) |
|  | Port Identity. [More...](structgptp__port__identity.md#details) |
| struct | [gptp\_flags](structgptp__flags.md) |
|  | gPTP message flags [More...](structgptp__flags.md#details) |
| struct | [gptp\_hdr](structgptp__hdr.md) |
|  | gPTP message header [More...](structgptp__hdr.md#details) |
| struct | [gptp\_phase\_dis\_cb](structgptp__phase__dis__cb.md) |
|  | Phase discontinuity callback structure. [More...](structgptp__phase__dis__cb.md#details) |
| struct | [gptp\_clk\_src\_time\_invoke\_params](structgptp__clk__src__time__invoke__params.md) |
|  | ClockSourceTime.invoke function parameters. [More...](structgptp__clk__src__time__invoke__params.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [gptp\_phase\_dis\_callback\_t](group__gptp.md#gade00e0d8398f015031d7f77317e4b97b)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*gm\_identity, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*time\_base, struct [gptp\_scaled\_ns](structgptp__scaled__ns.md) \*last\_gm\_ph\_change, double \*last\_gm\_freq\_change) |
|  | Define callback that is called after a phase discontinuity has been sent by the grandmaster. |
| typedef void(\* | [gptp\_port\_cb\_t](group__gptp.md#ga9bd009e6027d57cd9950b0387d727e3d)) (int port, struct [net\_if](structnet__if.md) \*iface, void \*user\_data) |
|  | Callback used while iterating over gPTP ports. |

| Functions | |
| --- | --- |
| void | [gptp\_register\_phase\_dis\_cb](group__gptp.md#gaad2282df9cbf7f05f557285323af8f07) (struct [gptp\_phase\_dis\_cb](structgptp__phase__dis__cb.md) \*phase\_dis, [gptp\_phase\_dis\_callback\_t](group__gptp.md#gade00e0d8398f015031d7f77317e4b97b) cb) |
|  | Register a phase discontinuity callback. |
| void | [gptp\_unregister\_phase\_dis\_cb](group__gptp.md#ga55d95859e5ec586cb2341929901220dd) (struct [gptp\_phase\_dis\_cb](structgptp__phase__dis__cb.md) \*phase\_dis) |
|  | Unregister a phase discontinuity callback. |
| void | [gptp\_call\_phase\_dis\_cb](group__gptp.md#ga29bf157d06a5ec5bb5a2a8a0e986709d) (void) |
|  | Call a phase discontinuity callback function. |
| int | [gptp\_event\_capture](group__gptp.md#ga9a8e2ccf20d0430b4e62f3302462c6eb) (struct [net\_ptp\_time](structnet__ptp__time.md) \*slave\_time, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*gm\_present) |
|  | Get gPTP time. |
| char \* | [gptp\_sprint\_clock\_id](group__gptp.md#ga40121c2957d58b0b5bb4468eac5de259) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*clk\_id, char \*output, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) output\_len) |
|  | Utility function to print clock id to a user supplied buffer. |
| void | [gptp\_foreach\_port](group__gptp.md#ga06ddd41c7adf9e387d1b23bcdfccbddc) ([gptp\_port\_cb\_t](group__gptp.md#ga9bd009e6027d57cd9950b0387d727e3d) cb, void \*user\_data) |
|  | Go through all the gPTP ports and call callback for each of them. |
| struct gptp\_domain \* | [gptp\_get\_domain](group__gptp.md#gae4c3aac6b88e9ce21a32ba3263b9ad59) (void) |
|  | Get gPTP domain. |
| void | [gptp\_clk\_src\_time\_invoke](group__gptp.md#ga9b27c9a741fb0ca72eff78e334e629fe) (struct [gptp\_clk\_src\_time\_invoke\_params](structgptp__clk__src__time__invoke__params.md) \*arg) |
|  | This interface is used by the ClockSource entity to provide time to the ClockMaster entity of a time-aware system. |
| struct [gptp\_hdr](structgptp__hdr.md) \* | [gptp\_get\_hdr](group__gptp.md#ga5b46fb7bbe1a380e3c327c8f5abbabeb) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Return pointer to gPTP packet header in network packet. |

## Detailed Description

Public functions for the Precision Time Protocol Stack.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [gptp.h](gptp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
