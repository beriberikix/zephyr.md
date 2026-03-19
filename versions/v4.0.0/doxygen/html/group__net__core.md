---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__net__core.html
original_path: doxygen/html/group__net__core.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Network Core Library

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Network core library.
[More...](#details)

| Enumerations | |
| --- | --- |
| enum | [net\_verdict](#ga8e5393f3bdd85491f221324e637c3896) { [NET\_OK](#gga8e5393f3bdd85491f221324e637c3896a2a49d766ffb9422176da8e4712fdb047) , [NET\_CONTINUE](#gga8e5393f3bdd85491f221324e637c3896aac7e9cac1cfef82e00232bd746e93b4f) , [NET\_DROP](#gga8e5393f3bdd85491f221324e637c3896a464f79c041fb589d518eeef445c477c3) } |
|  | Net Verdict. [More...](#ga8e5393f3bdd85491f221324e637c3896) |

| Functions | |
| --- | --- |
| int | [net\_recv\_data](#ga3421119d2b1797ee5d70f736a61f93b7) (struct [net\_if](structnet__if.md) \*iface, struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Called by lower network stack or network device driver when a network packet has been received. |
| int | [net\_send\_data](#ga1a1699666716229a59486a51e46044fc) (struct [net\_pkt](structnet__pkt.md) \*pkt) |
|  | Send data to network. |

## Detailed Description

Network core library.

Since
:   1.0

Version
:   1.0.0

## Enumeration Type Documentation

## [◆ ](#ga8e5393f3bdd85491f221324e637c3896)net\_verdict

| enum [net\_verdict](#ga8e5393f3bdd85491f221324e637c3896) |
| --- |

`#include <[net_core.h](net__core_8h.md)>`

Net Verdict.

| Enumerator | |
| --- | --- |
| NET\_OK | Packet has been taken care of. |
| NET\_CONTINUE | Packet has not been touched, other part should decide about its fate. |
| NET\_DROP | Packet must be dropped. |

## Function Documentation

## [◆ ](#ga3421119d2b1797ee5d70f736a61f93b7)net\_recv\_data()

| int net\_recv\_data | ( | struct [net\_if](structnet__if.md) \* | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [net\_pkt](structnet__pkt.md) \* | *pkt* ) |

`#include <[net_core.h](net__core_8h.md)>`

Called by lower network stack or network device driver when a network packet has been received.

The function will push the packet up in the network stack for further processing.

Parameters
:   | iface | Network interface where the packet was received. |
    | --- | --- |
    | pkt | Network packet data. |

Returns
:   0 if ok, <0 if error.

## [◆ ](#ga1a1699666716229a59486a51e46044fc)net\_send\_data()

| int net\_send\_data | ( | struct [net\_pkt](structnet__pkt.md) \* | *pkt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[net_core.h](net__core_8h.md)>`

Send data to network.

Send data to network. This should not be used normally by applications as it requires that the network packet is properly constructed.

Parameters
:   | pkt | Network packet. |
    | --- | --- |

Returns
:   0 if ok, <0 if error. If <0 is returned, then the caller needs to unref the pkt in order to avoid memory leak.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
