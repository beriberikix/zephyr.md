---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__ieee802154.html
original_path: doxygen/html/group__ieee802154.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

IEEE 802.15.4 and Thread APIs

[Connectivity](group__connectivity.md)

IEEE 802.15.4 native and OpenThread L2, configuration, management and driver APIs.
[More...](#details)

| Topics | |
| --- | --- |
|  | [IEEE 802.15.4 Drivers](group__ieee802154__driver.md) |
|  | IEEE 802.15.4 driver API. |
|  | [IEEE 802.15.4 L2](group__ieee802154__l2.md) |
|  | IEEE 802.15.4 L2 APIs. |
|  | [IEEE 802.15.4 Net Management](group__ieee802154__mgmt.md) |
|  | IEEE 802.15.4 net management library. |
|  | [OpenThread L2 abstraction layer](group__openthread.md) |
|  | OpenThread Layer 2 abstraction layer. |

## Detailed Description

IEEE 802.15.4 native and OpenThread L2, configuration, management and driver APIs.

The IEEE 802.15.4 and Thread subsystems comprise the OpenThread L2 subsystem, the native IEEE 802.15.4 L2 subsystem ("Soft" MAC), a mostly vendor and protocol agnostic driver API shared between the OpenThread and native L2 stacks ("Hard" MAC and PHY) as well as several APIs to configure the subsystem (shell, net management, Kconfig, devicetree, etc.).

The **OpenThread subsystem API** integrates the external [OpenThread](https://openthread.io) stack into Zephyr. It builds upon Zephyr's native IEEE 802.15.4 driver API.

The **native IEEE 802.15.4 subsystem APIs** are exposed at different levels and address several audiences:

- shell (end users, application developers):
  - a set of IEEE 802.15.4 shell commands (see [shell](structshell.md "Shell instance internals.")> [IEEE 802.15.4 and Thread APIs](group__ieee802154.md "IEEE 802.15.4 native and OpenThread L2, configuration, management and driver APIs.") help)
- application API (application developers):
  - IPv6, DGRAM and RAW sockets for actual peer-to-peer, multicast and broadcast data exchange between nodes including connection specific configuration (sample coming soon, see [https://github.com/linux-wpan/wpan-tools/tree/master/examples](https://github.com/linux-wpan/wpan-tools/tree/master/examples) for now which inspired our API and therefore has a similar socket API),
  - Kconfig and devicetree configuration options (net config library extension, subsystem-wide MAC and PHY Kconfig/DT options, driver/vendor specific Kconfig/DT options, watch out for options prefixed with IEEE802154/ieee802154),
  - Network Management: runtime configuration of the IEEE 802.15.4 protocols stack at the MAC (L2) and PHY (L1) levels (see [IEEE 802.15.4 Net Management](group__ieee802154__mgmt.md "IEEE 802.15.4 Net Management")),
- L2 integration (subsystem contributors):
  - see [IEEE 802.15.4 L2](group__ieee802154__l2.md "IEEE 802.15.4 L2")
  - implementation of Zephyr's internal L2-level socket and network context abstractions (context/socket operations, see [Network L2 Abstraction Layer](group__net__l2.md "Network L2 Abstraction Layer")),
  - protocol-specific extension to the interface structure (see [Network Interface abstraction layer](group__net__if.md "Network Interface abstraction layer"))
  - protocol-specific extensions to the network packet structure (see [Network Packet Library](group__net__pkt.md "Network Packet Library")),
- OpenThread and native IEEE 802.15.4 share a common **driver API** (driver maintainers/contributors):
  - see [IEEE 802.15.4 Drivers](group__ieee802154__driver.md "IEEE 802.15.4 Drivers")
  - a basic, mostly PHY-level driver API to be implemented by all drivers,
  - several "hard MAC" (hardware/firmware offloading) extension points for performance critical or timing sensitive aspects of the protocol

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
