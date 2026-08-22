---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structbt__le__local__features.html
original_path: doxygen/html/structbt__le__local__features.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_le\_local\_features Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

Local Bluetooth LE controller features and capabilities.
[More...](#details)

`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [features](#a76b8cc9bd4ab099cb94ebe997d991f68) [8] |
|  | Local LE controller supported features. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [states](#aa2dc6363feab37af195ee192f2b906f1) |
|  | Local LE controller supported states. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [acl\_mtu](#a22ce370b338f687ce6860435cc0ec9c5) |
|  | ACL data packet length. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [acl\_pkts](#a19cecbe8574229844e9416842bc42b0c) |
|  | Total number of ACL data packets. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [iso\_mtu](#ad7b95feb82c1dece8bb8bb7969efa2ec) |
|  | ISO data packet length. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [iso\_pkts](#a8b413bf80ccd7e3af67f7e1c28a1beeb) |
|  | Total number of ISO data packets. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rl\_size](#ac86ae6974627ddb2e34b0d028cdcfe32) |
|  | Maximum size of the controller resolving list. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [max\_adv\_data\_len](#a932af365332149ec620413a8504d342c) |
|  | Maximum advertising data length. |

## Detailed Description

Local Bluetooth LE controller features and capabilities.

This struct provides details about the Bluetooth LE controller's supported features, states, and various other capabilities. It includes information on ACL and ISO data packet lengths, the controller's resolving list size, and the maximum advertising data length. This information can be obtained after enabling the Bluetooth stack with [bt\_enable](group__bt__gap.md#gac45d16bfe21c3c38e834c293e5ebc42b "bt_enable") function.

Refer to the Bluetooth Core Specification, Volume 6, Part B and Volume 4, Part E for detailed sections about each field's significance and values.

## Field Documentation

## [◆ ](#a22ce370b338f687ce6860435cc0ec9c5)acl\_mtu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_local\_features::acl\_mtu |
| --- |

ACL data packet length.

This represents the maximum ACL HCI Data packet which can be sent from the Host to the Controller. The Host may support L2CAP and ATT MTUs larger than this value. See Bluetooth Core Specification, Vol 6, Part E, Section 7.8.2.

## [◆ ](#a19cecbe8574229844e9416842bc42b0c)acl\_pkts

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_local\_features::acl\_pkts |
| --- |

Total number of ACL data packets.

## [◆ ](#a76b8cc9bd4ab099cb94ebe997d991f68)features

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_local\_features::features[8] |
| --- |

Local LE controller supported features.

Refer to BT\_LE\_FEAT\_BIT\_\* for values. Refer to the BT\_FEAT\_LE\_\* macros for value comparionson. See Bluetooth Core Specification, Vol 6, Part B, Section 4.6.

## [◆ ](#ad7b95feb82c1dece8bb8bb7969efa2ec)iso\_mtu

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_local\_features::iso\_mtu |
| --- |

ISO data packet length.

This represents the maximum ISO HCI Data packet which can be sent from the Host to the Controller. ISO SDUs above this size can be fragmented assuming that the number of [bt\_le\_local\_features::iso\_pkts](#a8b413bf80ccd7e3af67f7e1c28a1beeb) support the maximum size.

## [◆ ](#a8b413bf80ccd7e3af67f7e1c28a1beeb)iso\_pkts

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_local\_features::iso\_pkts |
| --- |

Total number of ISO data packets.

## [◆ ](#a932af365332149ec620413a8504d342c)max\_adv\_data\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_le\_local\_features::max\_adv\_data\_len |
| --- |

Maximum advertising data length.

Note
:   The maximum advertising data length also depends on advertising type.

See Bluetooth Core Specification, Vol 6, Part E, Section 7.8.57.

## [◆ ](#ac86ae6974627ddb2e34b0d028cdcfe32)rl\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_le\_local\_features::rl\_size |
| --- |

Maximum size of the controller resolving list.

See Bluetooth Core Specification, Vol 6, Part E, Section 7.8.41.

## [◆ ](#aa2dc6363feab37af195ee192f2b906f1)states

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) bt\_le\_local\_features::states |
| --- |

Local LE controller supported states.

Refer to BT\_LE\_STATES\_\* for values. See Bluetooth Core Specification 6.0, Vol 4, Part E, Section 7.8.27

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[bluetooth.h](bluetooth_2bluetooth_8h_source.md)

- [bt\_le\_local\_features](structbt__le__local__features.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
