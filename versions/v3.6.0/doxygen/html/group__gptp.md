---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__gptp.html
original_path: doxygen/html/group__gptp.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gPTP support

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

generic Precision Time Protocol (gPTP) support
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [gptp\_scaled\_ns](structgptp__scaled__ns.md) |
|  | Scaled Nanoseconds. [More...](structgptp__scaled__ns.md#details) |
| struct | [gptp\_uscaled\_ns](structgptp__uscaled__ns.md) |
|  | UScaled Nanoseconds. [More...](structgptp__uscaled__ns.md#details) |
| struct | [gptp\_port\_identity](structgptp__port__identity.md) |
|  | Port Identity. [More...](structgptp__port__identity.md#details) |
| struct | [gptp\_flags](structgptp__flags.md) |
| struct | [gptp\_hdr](structgptp__hdr.md) |
| struct | [gptp\_phase\_dis\_cb](structgptp__phase__dis__cb.md) |
|  | Phase discontinuity callback structure. [More...](structgptp__phase__dis__cb.md#details) |
| struct | [gptp\_clk\_src\_time\_invoke\_params](structgptp__clk__src__time__invoke__params.md) |
|  | ClockSourceTime.invoke function parameters. [More...](structgptp__clk__src__time__invoke__params.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [gptp\_phase\_dis\_callback\_t](#gade00e0d8398f015031d7f77317e4b97b)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*gm\_identity, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*time\_base, struct [gptp\_scaled\_ns](structgptp__scaled__ns.md) \*last\_gm\_ph\_change, double \*last\_gm\_freq\_change) |
|  | Define callback that is called after a phase discontinuity has been sent by the grandmaster. |
| typedef void(\* | [gptp\_port\_cb\_t](#ga9bd009e6027d57cd9950b0387d727e3d)) (int port, struct [net\_if](structnet__if.md) \*iface, void \*user\_data) |
|  | Callback used while iterating over gPTP ports. |

| Functions | |
| --- | --- |
| void | [gptp\_register\_phase\_dis\_cb](#gaad2282df9cbf7f05f557285323af8f07) (struct [gptp\_phase\_dis\_cb](structgptp__phase__dis__cb.md) \*phase\_dis, [gptp\_phase\_dis\_callback\_t](#gade00e0d8398f015031d7f77317e4b97b) cb) |
|  | Register a phase discontinuity callback. |
| void | [gptp\_unregister\_phase\_dis\_cb](#ga55d95859e5ec586cb2341929901220dd) (struct [gptp\_phase\_dis\_cb](structgptp__phase__dis__cb.md) \*phase\_dis) |
|  | Unregister a phase discontinuity callback. |
| void | [gptp\_call\_phase\_dis\_cb](#ga29bf157d06a5ec5bb5a2a8a0e986709d) (void) |
|  | Call a phase discontinuity callback function. |
| int | [gptp\_event\_capture](#ga9a8e2ccf20d0430b4e62f3302462c6eb) (struct [net\_ptp\_time](structnet__ptp__time.md) \*slave\_time, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*gm\_present) |
|  | Get gPTP time. |
| char \* | [gptp\_sprint\_clock\_id](#ga40121c2957d58b0b5bb4468eac5de259) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*clk\_id, char \*output, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) output\_len) |
|  | Utility function to print clock id to a user supplied buffer. |
| void | [gptp\_foreach\_port](#ga06ddd41c7adf9e387d1b23bcdfccbddc) ([gptp\_port\_cb\_t](#ga9bd009e6027d57cd9950b0387d727e3d) cb, void \*user\_data) |
|  | Go through all the gPTP ports and call callback for each of them. |
| struct gptp\_domain \* | [gptp\_get\_domain](#gae4c3aac6b88e9ce21a32ba3263b9ad59) (void) |
|  | Get gPTP domain. |
| void | [gptp\_clk\_src\_time\_invoke](#ga9b27c9a741fb0ca72eff78e334e629fe) (struct [gptp\_clk\_src\_time\_invoke\_params](structgptp__clk__src__time__invoke__params.md) \*arg) |
|  | This interface is used by the ClockSource entity to provide time to the ClockMaster entity of a time-aware system. |
| struct [gptp\_hdr](structgptp__hdr.md) \* | [gptp\_get\_hdr](#ga5b46fb7bbe1a380e3c327c8f5abbabeb) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Return pointer to gPTP packet header in network packet. |

## Detailed Description

generic Precision Time Protocol (gPTP) support

## Typedef Documentation

## [◆ ](#gade00e0d8398f015031d7f77317e4b97b)gptp\_phase\_dis\_callback\_t

| typedef void(\* gptp\_phase\_dis\_callback\_t) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*gm\_identity, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*time\_base, struct [gptp\_scaled\_ns](structgptp__scaled__ns.md) \*last\_gm\_ph\_change, double \*last\_gm\_freq\_change) |
| --- |

`#include <[gptp.h](gptp_8h.md)>`

Define callback that is called after a phase discontinuity has been sent by the grandmaster.

Parameters
:   | gm\_identity | A pointer to first element of a ClockIdentity array. The size of the array is GPTP\_CLOCK\_ID\_LEN. |
    | --- | --- |
    | time\_base | A pointer to the value of timeBaseIndicator of the current grandmaster. |
    | last\_gm\_ph\_change | A pointer to the value of lastGmPhaseChange received from grandmaster. |
    | last\_gm\_freq\_change | A pointer to the value of lastGmFreqChange received from the grandmaster. |

## [◆ ](#ga9bd009e6027d57cd9950b0387d727e3d)gptp\_port\_cb\_t

| typedef void(\* gptp\_port\_cb\_t) (int port, struct [net\_if](structnet__if.md) \*iface, void \*user\_data) |
| --- |

`#include <[gptp.h](gptp_8h.md)>`

Callback used while iterating over gPTP ports.

Parameters
:   | port | Port number |
    | --- | --- |
    | iface | Pointer to network interface |
    | user\_data | A valid pointer to user data or NULL |

## Function Documentation

## [◆ ](#ga29bf157d06a5ec5bb5a2a8a0e986709d)gptp\_call\_phase\_dis\_cb()

| void gptp\_call\_phase\_dis\_cb | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gptp.h](gptp_8h.md)>`

Call a phase discontinuity callback function.

## [◆ ](#ga9b27c9a741fb0ca72eff78e334e629fe)gptp\_clk\_src\_time\_invoke()

| void gptp\_clk\_src\_time\_invoke | ( | struct [gptp\_clk\_src\_time\_invoke\_params](structgptp__clk__src__time__invoke__params.md) \* | *arg* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gptp.h](gptp_8h.md)>`

This interface is used by the ClockSource entity to provide time to the ClockMaster entity of a time-aware system.

Parameters
:   | arg | Current state and parameters of the ClockSource entity. |
    | --- | --- |

## [◆ ](#ga9a8e2ccf20d0430b4e62f3302462c6eb)gptp\_event\_capture()

| int gptp\_event\_capture | ( | struct [net\_ptp\_time](structnet__ptp__time.md) \* | *slave\_time*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *gm\_present* ) |

`#include <[gptp.h](gptp_8h.md)>`

Get gPTP time.

Parameters
:   | slave\_time | A pointer to structure where timestamp will be saved. |
    | --- | --- |
    | gm\_present | A pointer to a boolean where status of the presence of a grand master will be saved. |

Returns
:   Error code. 0 if no error.

## [◆ ](#ga06ddd41c7adf9e387d1b23bcdfccbddc)gptp\_foreach\_port()

| void gptp\_foreach\_port | ( | [gptp\_port\_cb\_t](#ga9bd009e6027d57cd9950b0387d727e3d) | *cb*, |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

`#include <[gptp.h](gptp_8h.md)>`

Go through all the gPTP ports and call callback for each of them.

Parameters
:   | cb | User-supplied callback function to call |
    | --- | --- |
    | user\_data | User specified data |

## [◆ ](#gae4c3aac6b88e9ce21a32ba3263b9ad59)gptp\_get\_domain()

| struct gptp\_domain \* gptp\_get\_domain | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gptp.h](gptp_8h.md)>`

Get gPTP domain.

This contains all the configuration / status of the gPTP domain.

Returns
:   Pointer to domain or NULL if not found.

## [◆ ](#ga5b46fb7bbe1a380e3c327c8f5abbabeb)gptp\_get\_hdr()

| struct [gptp\_hdr](structgptp__hdr.md) \* gptp\_get\_hdr | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gptp.h](gptp_8h.md)>`

Return pointer to gPTP packet header in network packet.

Parameters
:   | pkt | Network packet (received or sent) |
    | --- | --- |

Returns
:   Pointer to gPTP header.

## [◆ ](#gaad2282df9cbf7f05f557285323af8f07)gptp\_register\_phase\_dis\_cb()

| void gptp\_register\_phase\_dis\_cb | ( | struct [gptp\_phase\_dis\_cb](structgptp__phase__dis__cb.md) \* | *phase\_dis*, |
| --- | --- | --- | --- |
|  |  | [gptp\_phase\_dis\_callback\_t](#gade00e0d8398f015031d7f77317e4b97b) | *cb* ) |

`#include <[gptp.h](gptp_8h.md)>`

Register a phase discontinuity callback.

Parameters
:   | phase\_dis | Caller specified handler for the callback. |
    | --- | --- |
    | cb | Callback to register. |

## [◆ ](#ga40121c2957d58b0b5bb4468eac5de259)gptp\_sprint\_clock\_id()

| char \* gptp\_sprint\_clock\_id | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *clk\_id*, |
| --- | --- | --- | --- |
|  |  | char \* | *output*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *output\_len* ) |

`#include <[gptp.h](gptp_8h.md)>`

Utility function to print clock id to a user supplied buffer.

Parameters
:   | clk\_id | Clock id |
    | --- | --- |
    | output | Output buffer |
    | output\_len | Output buffer len |

Returns
:   Pointer to output buffer

## [◆ ](#ga55d95859e5ec586cb2341929901220dd)gptp\_unregister\_phase\_dis\_cb()

| void gptp\_unregister\_phase\_dis\_cb | ( | struct [gptp\_phase\_dis\_cb](structgptp__phase__dis__cb.md) \* | *phase\_dis* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gptp.h](gptp_8h.md)>`

Unregister a phase discontinuity callback.

Parameters
:   | phase\_dis | Caller specified handler for the callback. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
