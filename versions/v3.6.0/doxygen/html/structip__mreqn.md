---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structip__mreqn.html
original_path: doxygen/html/structip__mreqn.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ip\_mreqn Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [BSD Sockets compatible API](group__bsd__sockets.md)

Struct used when joining or leaving a IPv4 multicast group.
[More...](#details)

`#include <[socket.h](net_2socket_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [in\_addr](structin__addr.md) | [imr\_multiaddr](#ad359b69f0d0e147fe1fb82045ba6cb8e) |
|  | IP multicast group address. |
| struct [in\_addr](structin__addr.md) | [imr\_address](#aee21b302d5440d290318480657c0956c) |
|  | IP address of local interface. |
| int | [imr\_ifindex](#a57e6e1acbf98da91859c8c95e555f5a7) |
|  | Network interface index. |

## Detailed Description

Struct used when joining or leaving a IPv4 multicast group.

## Field Documentation

## [◆ ](#aee21b302d5440d290318480657c0956c)imr\_address

| struct [in\_addr](structin__addr.md) ip\_mreqn::imr\_address |
| --- |

IP address of local interface.

## [◆ ](#a57e6e1acbf98da91859c8c95e555f5a7)imr\_ifindex

| int ip\_mreqn::imr\_ifindex |
| --- |

Network interface index.

## [◆ ](#ad359b69f0d0e147fe1fb82045ba6cb8e)imr\_multiaddr

| struct [in\_addr](structin__addr.md) ip\_mreqn::imr\_multiaddr |
| --- |

IP multicast group address.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[socket.h](net_2socket_8h_source.md)

- [ip\_mreqn](structip__mreqn.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
