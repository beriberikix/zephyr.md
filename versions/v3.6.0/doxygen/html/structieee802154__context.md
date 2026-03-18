---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structieee802154__context.html
original_path: doxygen/html/structieee802154__context.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_context Struct Reference

[Connectivity](group__connectivity.md) » [IEEE 802.15.4 and Thread APIs](group__ieee802154.md) » [IEEE 802.15.4 L2](group__ieee802154__l2.md)

IEEE 802.15.4 L2 context.
[More...](#details)

`#include <[ieee802154.h](ieee802154_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [pan\_id](#ae3c9b2de2e55d619f2d8acf5cf8b7491) |
|  | PAN ID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [channel](#ad02d219198201aee98ab1ab1793cfe6b) |
|  | Channel Number. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [short\_addr](#a64e992804fcd463ff437ac88c296dfab) |
|  | Short Address (in CPU byte order). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ext\_addr](#a3dbbea6bef660e17b3bbf7c02a4672cc) [8] |
|  | Extended Address (in little endian). |
| struct [net\_linkaddr\_storage](structnet__linkaddr__storage.md) | [linkaddr](#a77b6b4d41835dc2ee0f28a4109136733) |
|  | Link layer address (in big endian). |
| struct [ieee802154\_security\_ctx](structieee802154__security__ctx.md) | [sec\_ctx](#a0a4cc252326f86af4d142d32950d2af6) |
|  | Security context. |
| struct [ieee802154\_req\_params](structieee802154__req__params.md) \* | [scan\_ctx](#a06de84ddc495a80777b87f8934da94e5) |
|  | Pointer to scanning parameters and results, guarded by scan\_ctx\_lock. |
| struct k\_sem | [scan\_ctx\_lock](#a35bfac224aff80f256853cb0d8ce8466) |
|  | Used to maintain integrity of data for all fields in this struct unless otherwise documented on field level. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [coord\_ext\_addr](#a84053e172fbfd9d59c4d8e7a1b98d5b6) [8] |
|  | Coordinator extended address. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [coord\_short\_addr](#abf1cc83c3a4880513137e7e4955174c1) |
|  | Coordinator short address. |
| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | [tx\_power](#a800a07927c4faec1dca2910a65c1baae) |
|  | Transmission power in dBm. |
| enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) | [flags](#acf1fcafe106362eba112ea946a575bbd) |
|  | L2 flags. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [sequence](#a5618dec853ce41bbfa48e2aaa3f73262) |
|  | Data sequence number. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [device\_role](#a70b2a2936aca60a5bc4fc2b98aa11497): 2 |
|  | Device Role. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ack\_requested](#a511059cb95c0d52c907464a1891586aa): 1 |
|  | ACK requested flag, guarded by ack\_lock. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ack\_seq](#a0eeefef60bc7c266b2bb26893404ff86) |
|  | ACK expected sequence number, guarded by ack\_lock. |
| struct k\_sem | [ack\_lock](#a641c70a792f47431be8a0ffe2635a11f) |
|  | ACK lock, guards ack\_\* fields. |
| struct k\_sem | [ctx\_lock](#a462527426b11b80ee53a3f91aacf1e1e) |
|  | Context lock. |

## Detailed Description

IEEE 802.15.4 L2 context.

## Field Documentation

## [◆ ](#a641c70a792f47431be8a0ffe2635a11f)ack\_lock

| struct k\_sem ieee802154\_context::ack\_lock |
| --- |

ACK lock, guards ack\_\* fields.

## [◆ ](#a511059cb95c0d52c907464a1891586aa)ack\_requested

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_context::ack\_requested |
| --- |

ACK requested flag, guarded by ack\_lock.

## [◆ ](#a0eeefef60bc7c266b2bb26893404ff86)ack\_seq

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_context::ack\_seq |
| --- |

ACK expected sequence number, guarded by ack\_lock.

## [◆ ](#ad02d219198201aee98ab1ab1793cfe6b)channel

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ieee802154\_context::channel |
| --- |

Channel Number.

The RF channel to use for all transmissions and receptions, see section 11.3, table 11-2, phyCurrentChannel. The allowable range of values is PHY dependent as defined in section 10.1.3.

in CPU byte order

## [◆ ](#a84053e172fbfd9d59c4d8e7a1b98d5b6)coord\_ext\_addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_context::coord\_ext\_addr[8] |
| --- |

Coordinator extended address.

see section 8.4.3.1, table 8-94, macCoordExtendedAddress, the address of the coordinator through which the device is associated.

A value of zero indicates that a coordinator extended address is unknown (default).

in little endian

## [◆ ](#abf1cc83c3a4880513137e7e4955174c1)coord\_short\_addr

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ieee802154\_context::coord\_short\_addr |
| --- |

Coordinator short address.

see section 8.4.3.1, table 8-94, macCoordShortAddress, the short address assigned to the coordinator through which the device is associated.

A value of 0xfffe indicates that the coordinator is only using its extended address. A value of 0xffff indicates that this value is unknown.

in CPU byte order

## [◆ ](#a462527426b11b80ee53a3f91aacf1e1e)ctx\_lock

| struct k\_sem ieee802154\_context::ctx\_lock |
| --- |

Context lock.

This lock guards all mutable context attributes unless otherwise mentioned on attribute level.

## [◆ ](#a70b2a2936aca60a5bc4fc2b98aa11497)device\_role

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_context::device\_role |
| --- |

Device Role.

See section 6.1: A device may be operating as end device (0), coordinator (1), or PAN coordinator (2). If no device role is explicitly configured then the device will be treated as an end device.

A value of 3 is undefined.

Can be read/set via [ieee802154\_device\_role](group__ieee802154__l2.md#ga7a4fb2d89381bba54514bf8396fb6d26 "ieee802154_device_role").

## [◆ ](#a3dbbea6bef660e17b3bbf7c02a4672cc)ext\_addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_context::ext\_addr[8] |
| --- |

Extended Address (in little endian).

The extended address is device specific, usually permanently stored on the device and immutable.

See section 8.4.3.1, table 8-94, macExtendedAddress.

## [◆ ](#acf1fcafe106362eba112ea946a575bbd)flags

| enum [net\_l2\_flags](group__net__l2.md#gac7db0cc6c56d371a5803873074ec2516) ieee802154\_context::flags |
| --- |

L2 flags.

## [◆ ](#a77b6b4d41835dc2ee0f28a4109136733)linkaddr

| struct [net\_linkaddr\_storage](structnet__linkaddr__storage.md) ieee802154\_context::linkaddr |
| --- |

Link layer address (in big endian).

## [◆ ](#ae3c9b2de2e55d619f2d8acf5cf8b7491)pan\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ieee802154\_context::pan\_id |
| --- |

PAN ID.

The identifier of the PAN on which the device is operating. If this value is 0xffff, the device is not associated. See section 8.4.3.1, table 8-94, macPanId.

in CPU byte order

## [◆ ](#a06de84ddc495a80777b87f8934da94e5)scan\_ctx

| struct [ieee802154\_req\_params](structieee802154__req__params.md)\* ieee802154\_context::scan\_ctx |
| --- |

Pointer to scanning parameters and results, guarded by scan\_ctx\_lock.

## [◆ ](#a35bfac224aff80f256853cb0d8ce8466)scan\_ctx\_lock

| struct k\_sem ieee802154\_context::scan\_ctx\_lock |
| --- |

Used to maintain integrity of data for all fields in this struct unless otherwise documented on field level.

## [◆ ](#a0a4cc252326f86af4d142d32950d2af6)sec\_ctx

| struct [ieee802154\_security\_ctx](structieee802154__security__ctx.md) ieee802154\_context::sec\_ctx |
| --- |

Security context.

## [◆ ](#a5618dec853ce41bbfa48e2aaa3f73262)sequence

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_context::sequence |
| --- |

Data sequence number.

The sequence number added to the transmitted Data frame or MAC command, see section 8.4.3.1, table 8-94, macDsn.

## [◆ ](#a64e992804fcd463ff437ac88c296dfab)short\_addr

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ieee802154\_context::short\_addr |
| --- |

Short Address (in CPU byte order).

Range:

- 0x0000–0xfffd: associated, short address was assigned
- 0xfffe: associated but no short address assigned
- 0xffff: not associated (default),

See section 6.4.1, table 6-4 (Usage of the shart address) and section 8.4.3.1, table 8-94, macShortAddress.

## [◆ ](#a800a07927c4faec1dca2910a65c1baae)tx\_power

| [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) ieee802154\_context::tx\_power |
| --- |

Transmission power in dBm.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ieee802154.h](ieee802154_8h_source.md)

- [ieee802154\_context](structieee802154__context.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
