---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__DSA.html
original_path: doxygen/html/group__DSA.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Distributed Switch Architecture definitions and helpers

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

DSA definitions and helpers.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [dsa\_slave\_config](structdsa__slave__config.md) |
|  | Structure to provide mac address for each LAN interface. [More...](structdsa__slave__config.md#details) |

| Typedefs | |
| --- | --- |
| typedef enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)(\* | [dsa\_net\_recv\_cb\_t](#ga6c40af9c2caefa7f855d225a41b43faa)) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | DSA (MGMT) Receive packet callback. |
| typedef int(\* | [dsa\_send\_t](#gad9a6e0ad0e100914f6b932843908d42b)) (const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Pointer to master interface send function. |

| Functions | |
| --- | --- |
| int | [dsa\_tx](#ga381fae2a3cf652db81db6e64d9aea62a) (const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | DSA generic transmit function. |
| int | [dsa\_register\_recv\_callback](#gaee78adf88b0598611097e42ff94e9c52) (struct [net\_if](structnet__if.md) \*iface, [dsa\_net\_recv\_cb\_t](#ga6c40af9c2caefa7f855d225a41b43faa) cb) |
|  | Register DSA Rx callback functions. |
| struct [net\_if](structnet__if.md) \* | [dsa\_net\_recv](#ga01a24efc07ef0aa4125b91781c3039f3) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*\*pkt) |
|  | Set DSA interface to packet. |
| int | [dsa\_register\_master\_tx](#ga676bff9b468696e2158bf5b14211fd27) (struct [net\_if](structnet__if.md) \*iface, [dsa\_send\_t](#gad9a6e0ad0e100914f6b932843908d42b) fn) |
|  | DSA helper function to register transmit function for master. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [dsa\_is\_port\_master](#ga06ef38794a9ca3f7b8d3a32d2e1b2212) (struct [net\_if](structnet__if.md) \*iface) |
|  | DSA helper function to check if port is master. |
| struct [net\_if](structnet__if.md) \* | [dsa\_get\_slave\_port](#ga6ee72f05ee1192ceb3f691d0fe007e13) (struct [net\_if](structnet__if.md) \*iface, int slave\_num) |
|  | Get network interface of a slave port. |
| int | [dsa\_switch\_read](#ga131e095ddf546471952663e0ce836c59) (struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*value) |
|  | Read from DSA switch register. |
| int | [dsa\_switch\_write](#gad6464601dcfccc77f06a0fed9ce80b0f) (struct [net\_if](structnet__if.md) \*iface, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Write to DSA switch. |
| int | [dsa\_switch\_set\_mac\_table\_entry](#ga742d4531fc59bfd37a229c2f25c84239) (struct [net\_if](structnet__if.md) \*iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*mac, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) fw\_port, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tbl\_entry\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Write static MAC table entry. |
| int | [dsa\_switch\_get\_mac\_table\_entry](#ga16767d0b80c684b32c33bbcc74d54488) (struct [net\_if](structnet__if.md) \*iface, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tbl\_entry\_idx) |
|  | Read static MAC table entry. |

## Detailed Description

DSA definitions and helpers.

Since
:   2.5

Version
:   0.8.0

## Typedef Documentation

## [◆ ](#ga6c40af9c2caefa7f855d225a41b43faa)dsa\_net\_recv\_cb\_t

| typedef enum [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896)(\* dsa\_net\_recv\_cb\_t) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
| --- |

`#include <[dsa.h](dsa_8h.md)>`

DSA (MGMT) Receive packet callback.

Callback gets called upon receiving packet. It is responsible for freeing packet or indicating to the stack that it needs to free packet by returning correct [net\_verdict](group__net__core.md#ga8e5393f3bdd85491f221324e637c3896 "Net Verdict.").

Returns:

- NET\_DROP, if packet was invalid, rejected or we want the stack to free it. In this case the core stack will free the packet.
- NET\_OK, if the packet was accepted, in this case the ownership of the [net\_pkt](structnet__pkt.md "Network packet.") goes to callback and core network stack will forget it.

## [◆ ](#gad9a6e0ad0e100914f6b932843908d42b)dsa\_send\_t

| typedef int(\* dsa\_send\_t) (const struct [device](structdevice.md) \*dev, struct [net\_pkt](structnet__pkt.md) \*pkt) |
| --- |

`#include <[dsa.h](dsa_8h.md)>`

Pointer to master interface send function.

## Function Documentation

## [◆ ](#ga6ee72f05ee1192ceb3f691d0fe007e13)dsa\_get\_slave\_port()

| struct [net\_if](structnet__if.md) \* dsa\_get\_slave\_port | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | int | *slave\_num* ) |

`#include <[dsa.h](dsa_8h.md)>`

Get network interface of a slave port.

Parameters
:   |  | iface | Master port |
    | --- | --- | --- |
    | [in] | slave\_num | Slave port number |

Returns
:   network interface of the slave if successful
:   NULL if slave port does not exist

## [◆ ](#ga06ef38794a9ca3f7b8d3a32d2e1b2212)dsa\_is\_port\_master()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dsa\_is\_port\_master | ( | struct [net\_if](structnet__if.md) \* | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[dsa.h](dsa_8h.md)>`

DSA helper function to check if port is master.

Parameters
:   | iface | Network interface (master) |
    | --- | --- |

Returns:

- true if ok, false otherwise

## [◆ ](#ga01a24efc07ef0aa4125b91781c3039f3)dsa\_net\_recv()

| struct [net\_if](structnet__if.md) \* dsa\_net\_recv | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [net\_pkt](structnet__pkt.md) \*\* | *pkt* ) |

`#include <[dsa.h](dsa_8h.md)>`

Set DSA interface to packet.

Parameters
:   | iface | Network interface (master) |
    | --- | --- |
    | pkt | Network packet |

Returns
:   Return the slave network interface

## [◆ ](#ga676bff9b468696e2158bf5b14211fd27)dsa\_register\_master\_tx()

| int dsa\_register\_master\_tx | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [dsa\_send\_t](#gad9a6e0ad0e100914f6b932843908d42b) | *fn* ) |

`#include <[dsa.h](dsa_8h.md)>`

DSA helper function to register transmit function for master.

Parameters
:   | iface | Network interface (master) |
    | --- | --- |
    | fn | Pointer to master interface send method |

Returns:

- 0 if ok, < 0 if error

## [◆ ](#gaee78adf88b0598611097e42ff94e9c52)dsa\_register\_recv\_callback()

| int dsa\_register\_recv\_callback | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [dsa\_net\_recv\_cb\_t](#ga6c40af9c2caefa7f855d225a41b43faa) | *cb* ) |

`#include <[dsa.h](dsa_8h.md)>`

Register DSA Rx callback functions.

Parameters
:   | iface | Network interface |
    | --- | --- |
    | cb | Receive callback function |

Returns
:   0 if ok, < 0 if error

## [◆ ](#ga16767d0b80c684b32c33bbcc74d54488)dsa\_switch\_get\_mac\_table\_entry()

| int dsa\_switch\_get\_mac\_table\_entry | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *tbl\_entry\_idx* ) |

`#include <[dsa.h](dsa_8h.md)>`

Read static MAC table entry.

Parameters
:   |  | iface | Master DSA interface |
    | --- | --- | --- |
    |  | buf | Buffer to receive MAC address |
    | [in] | tbl\_entry\_idx | Table entry index |

Returns
:   0 if successful, negative if error

## [◆ ](#ga131e095ddf546471952663e0ce836c59)dsa\_switch\_read()

| int dsa\_switch\_read | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *reg\_addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *value* ) |

`#include <[dsa.h](dsa_8h.md)>`

Read from DSA switch register.

Parameters
:   |  | iface | The interface |
    | --- | --- | --- |
    | [in] | reg\_addr | The register address |
    |  | value | The value |

Returns
:   0 if successful, negative if error

## [◆ ](#ga742d4531fc59bfd37a229c2f25c84239)dsa\_switch\_set\_mac\_table\_entry()

| int dsa\_switch\_set\_mac\_table\_entry | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *mac*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *fw\_port*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *tbl\_entry\_idx*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *flags* ) |

`#include <[dsa.h](dsa_8h.md)>`

Write static MAC table entry.

Parameters
:   |  | iface | Master DSA interface |
    | --- | --- | --- |
    | [in] | mac | MAC address |
    | [in] | fw\_port | The firmware port |
    | [in] | tbl\_entry\_idx | Table entry index |
    | [in] | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags |

Returns
:   0 if successful, negative if error

## [◆ ](#gad6464601dcfccc77f06a0fed9ce80b0f)dsa\_switch\_write()

| int dsa\_switch\_write | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *reg\_addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *value* ) |

`#include <[dsa.h](dsa_8h.md)>`

Write to DSA switch.

Parameters
:   |  | iface | The interface |
    | --- | --- | --- |
    | [in] | reg\_addr | The register address |
    | [in] | value | The value |

Returns
:   { description\_of\_the\_return\_value }

## [◆ ](#ga381fae2a3cf652db81db6e64d9aea62a)dsa\_tx()

| int dsa\_tx | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [net\_pkt](structnet__pkt.md) \* | *pkt* ) |

`#include <[dsa.h](dsa_8h.md)>`

DSA generic transmit function.

This is a generic function for passing packets from slave DSA interface to master.

Parameters
:   | dev | Device |
    | --- | --- |
    | pkt | Network packet |

Returns:

- 0 if ok (packet sent via master iface), < 0 if error

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
