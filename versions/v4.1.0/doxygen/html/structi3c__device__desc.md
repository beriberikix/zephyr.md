---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structi3c__device__desc.html
original_path: doxygen/html/structi3c__device__desc.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_device\_desc Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md)

Structure describing a I3C target device.
[More...](#details)

`#include <[i3c.h](i3c_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a965edbd5d74c06773e190a14d4f6e3cd) |
| const struct [device](structdevice.md) \*const | [bus](#affdfa3b12a01f966ba5a6a563e669803) |
|  | I3C bus to which this target device is attached. |
| const struct [device](structdevice.md) \*const | [dev](#a653090fd2c78794dae02a2031daddb4b) |
|  | Device driver instance of the I3C device. |
| const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [pid](#ac82bd8eccc52a98df76506bd2bed3961) |
|  | Device Provisioned ID. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [static\_addr](#a105221381d47f690219aa09a20936ae1) |
|  | Static address for this target device. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [init\_dynamic\_addr](#a0477ac021d81431a34f55fa1c9f04bb5) |
|  | Initial dynamic address. |
| const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [supports\_setaasa](#af0905f27f1765c96fc3aaf601926d6ed) |
|  | Device support for SETAASA. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [dynamic\_addr](#a4e4c9614871e5ea4aa08b1560ecc40d0) |
|  | Dynamic Address for this target device used for communication. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [group\_addr](#a260730aef8862b2898ef6f65cf4956c4) |
|  | Group address for this target device. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bcr](#ae1cff0a31d9cc5d7b18206556f8e0b21) |
|  | Bus Characteristic Register (BCR). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [dcr](#aee6342edbc47c478aa39b8330fab0d9c) |
|  | Device Characteristic Register (DCR). |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [maxrd](#ad570493d49084708bf35e9774bc99523) |  |
|  | Maximum Read Speed. [More...](#ad570493d49084708bf35e9774bc99523) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [maxwr](#a02b3bd0d87f92ec67cb7d53e210ec8a9) |  |
|  | Maximum Write Speed. [More...](#a02b3bd0d87f92ec67cb7d53e210ec8a9) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [max\_read\_turnaround](#a0c1a3f65c20ddabc004c82527ec690bb) |  |
|  | Maximum Read turnaround time in microseconds. [More...](#a0c1a3f65c20ddabc004c82527ec690bb) |
| } | [data\_speed](#a85f1ab9b53f4c4979b78d48e485d8500) |
| struct { |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [mrl](#ac0ec89782c8df7e2e0debf061c754a7e) |  |
|  | Maximum Read Length. [More...](#ac0ec89782c8df7e2e0debf061c754a7e) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [mwl](#a29804ab89f08928f14fa4095f57e79ed) |  |
|  | Maximum Write Length. [More...](#a29804ab89f08928f14fa4095f57e79ed) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [max\_ibi](#a1a895792d02e00784cc76da7ce4b60c9) |  |
|  | Maximum IBI Payload Size. [More...](#a1a895792d02e00784cc76da7ce4b60c9) |
| } | [data\_length](#a27f1d7ca0b4eac2d55781f3856f31835) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [crhdly1](#a3fc3b3f1cf396eaf164612e7b667b37a) |
|  | Controller Handoff Delay Parameters. |
| struct { |  |
| union { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [gethdrcap](#ae01bc68ac8154238d85bbf44dc06dfb7) |  |
|  | I3C v1.0 HDR Capabilities (`I3C_CCC_GETCAPS1_*`). [More...](#ae01bc68ac8154238d85bbf44dc06dfb7) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [getcap1](#a062f86dec32de3b9e899b096df47d828) |  |
|  | I3C v1.1+ GETCAPS1 (`I3C_CCC_GETCAPS1_*`). [More...](#a062f86dec32de3b9e899b096df47d828) |
| } |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [getcap2](#a089da4f6eaf2b80fc689bb89d527d330) |  |
|  | GETCAPS2 (`I3C_CCC_GETCAPS2_*`). [More...](#a089da4f6eaf2b80fc689bb89d527d330) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [getcap3](#a47af0b36448dfec8307b25a31712428e) |  |
|  | GETCAPS3 (`I3C_CCC_GETCAPS3_*`). [More...](#a47af0b36448dfec8307b25a31712428e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [getcap4](#a1314218c6f6a429ccedb9975b9e02a90) |  |
|  | GETCAPS4. [More...](#a1314218c6f6a429ccedb9975b9e02a90) |
| } | [getcaps](#a7e44bedd1aa032d661335f8ec0a0d2e2) |
|  | Describes advanced (Target) capabilities and features. |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [crcaps1](#a5ab881cf948d10cfa9e1542b4b5a0f34) |  |
|  | CRCAPS1. [More...](#a5ab881cf948d10cfa9e1542b4b5a0f34) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [crcaps2](#a08e4524060eddc0dc15c985c1c59b9f1) |  |
|  | CRCAPS2. [More...](#a08e4524060eddc0dc15c985c1c59b9f1) |
| } | [crcaps](#a5dcad2306094a3ee32a20051f7eafa9a) |
| [i3c\_target\_ibi\_cb\_t](group__i3c__ibi.md#ga814cf622b240808216ce4e87802e965c) | [ibi\_cb](#a1f9eda89e2e28971e39aace38ddbb265) |
|  | In-Band Interrupt (IBI) callback. |

## Detailed Description

Structure describing a I3C target device.

Instances of this are passed to the I3C controller device APIs, for example:

- i3c\_device\_register() to tell the controller of a target device.
- i3c\_transfers() to initiate data transfers between controller and target device.

Fields [bus](#affdfa3b12a01f966ba5a6a563e669803), [pid](#ac82bd8eccc52a98df76506bd2bed3961) and [static\_addr](#a105221381d47f690219aa09a20936ae1) must be initialized by the module that implements the target device behavior prior to passing the object reference to I3C controller device APIs. [static\_addr](#a105221381d47f690219aa09a20936ae1) can be zero if target device does not have static address.

Internal field `node` should not be initialized or modified manually.

## Field Documentation

## [◆ ](#ae1cff0a31d9cc5d7b18206556f8e0b21)bcr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::bcr |
| --- |

Bus Characteristic Register (BCR).

See also
:   [I3C\_BCR](group__i3c__interface.md#I3C_BCR "I3C_BCR")

## [◆ ](#affdfa3b12a01f966ba5a6a563e669803)bus

| const struct [device](structdevice.md)\* const i3c\_device\_desc::bus |
| --- |

I3C bus to which this target device is attached.

## [◆ ](#a5dcad2306094a3ee32a20051f7eafa9a)[struct]

| struct { ... } i3c\_device\_desc::crcaps |
| --- |

## [◆ ](#a5ab881cf948d10cfa9e1542b4b5a0f34)crcaps1

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::crcaps1 |
| --- |

CRCAPS1.

- Bit[0]: Hot-Join Support
- Bit[1]: Group Management Support
- Bit[2]: Multi-Lane Support
- Bit[7:3]: Reserved

## [◆ ](#a08e4524060eddc0dc15c985c1c59b9f1)crcaps2

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::crcaps2 |
| --- |

CRCAPS2.

- Bit[0]: In-Band Interrupt Support
- Bit[1]: Controller Pass-Back
- Bit[2]: Deep Sleep Capable
- Bit[3]: Delayed Controller Handoff
- Bit[7:4]: Reserved

## [◆ ](#a3fc3b3f1cf396eaf164612e7b667b37a)crhdly1

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::crhdly1 |
| --- |

Controller Handoff Delay Parameters.

## [◆ ](#a27f1d7ca0b4eac2d55781f3856f31835)[struct]

| struct { ... } i3c\_device\_desc::data\_length |
| --- |

## [◆ ](#a85f1ab9b53f4c4979b78d48e485d8500)[struct]

| struct { ... } i3c\_device\_desc::data\_speed |
| --- |

## [◆ ](#aee6342edbc47c478aa39b8330fab0d9c)dcr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::dcr |
| --- |

Device Characteristic Register (DCR).

Describes the type of device. Refer to official documentation on what this number means.

## [◆ ](#a653090fd2c78794dae02a2031daddb4b)dev

| const struct [device](structdevice.md)\* const i3c\_device\_desc::dev |
| --- |

Device driver instance of the I3C device.

## [◆ ](#a4e4c9614871e5ea4aa08b1560ecc40d0)dynamic\_addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::dynamic\_addr |
| --- |

Dynamic Address for this target device used for communication.

This is to be set by the controller driver in one of the following situations:

- During Dynamic Address Assignment (during ENTDAA)
- Reset Dynamic Address Assignment (RSTDAA)
- Set All Addresses to Static Addresses (SETAASA)
- Set New Dynamic Address (SETNEWDA)
- Set Dynamic Address from Static Address (SETDASA)

0 if address has not been assigned.

## [◆ ](#a062f86dec32de3b9e899b096df47d828)getcap1

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::getcap1 |
| --- |

I3C v1.1+ GETCAPS1 (`I3C_CCC_GETCAPS1_*`).

- Bit[0]: HDR-DDR
- Bit[1]: HDR-TSP
- Bit[2]: HDR-TSL
- Bit[3]: HDR-BT
- Bit[7:4]: Reserved

## [◆ ](#a089da4f6eaf2b80fc689bb89d527d330)getcap2

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::getcap2 |
| --- |

GETCAPS2 (`I3C_CCC_GETCAPS2_*`).

- Bit[3:0]: I3C 1.x Specification Version
- Bit[5:4]: Group Address Capabilities
- Bit[6]: HDR-DDR Write Abort
- Bit[7]: HDR-DDR Abort CRC

## [◆ ](#a47af0b36448dfec8307b25a31712428e)getcap3

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::getcap3 |
| --- |

GETCAPS3 (`I3C_CCC_GETCAPS3_*`).

- Bit[0]: Multi-Lane (ML) Data Transfer Support
- Bit[1]: Device to Device Transfer (D2DXFER) Support
- Bit[2]: Device to Device Transfer (D2DXFER) IBI Capable
- Bit[3]: Defining Byte Support in GETCAPS
- Bit[4]: Defining Byte Support in GETSTATUS
- Bit[5]: HDR-BT CRC-32 Support
- Bit[6]: IBI MDB Support for Pending Read Notification
- Bit[7]: Reserved

## [◆ ](#a1314218c6f6a429ccedb9975b9e02a90)getcap4

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::getcap4 |
| --- |

GETCAPS4.

- Bit[7:0]: Reserved

## [◆ ](#a7e44bedd1aa032d661335f8ec0a0d2e2)[struct]

| struct { ... } i3c\_device\_desc::getcaps |
| --- |

Describes advanced (Target) capabilities and features.

## [◆ ](#ae01bc68ac8154238d85bbf44dc06dfb7)gethdrcap

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::gethdrcap |
| --- |

I3C v1.0 HDR Capabilities (`I3C_CCC_GETCAPS1_*`).

- Bit[0]: HDR-DDR
- Bit[1]: HDR-TSP
- Bit[2]: HDR-TSL
- Bit[7:3]: Reserved

## [◆ ](#a260730aef8862b2898ef6f65cf4956c4)group\_addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::group\_addr |
| --- |

Group address for this target device.

Set during:

- Reset Group Address(es) (RSTGRPA)
- Set Group Address (SETGRPA)

0 if group address has not been assigned. Only available if `CONFIG_I3C_USE_GROUP_ADDR` is set.

## [◆ ](#a1f9eda89e2e28971e39aace38ddbb265)ibi\_cb

| [i3c\_target\_ibi\_cb\_t](group__i3c__ibi.md#ga814cf622b240808216ce4e87802e965c) i3c\_device\_desc::ibi\_cb |
| --- |

In-Band Interrupt (IBI) callback.

Only available if `CONFIG_I3C_USE_IBI` is set.

## [◆ ](#a0477ac021d81431a34f55fa1c9f04bb5)init\_dynamic\_addr

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::init\_dynamic\_addr |
| --- |

Initial dynamic address.

This is specified in the device tree property "assigned-address" to indicate the desired dynamic address during address assignment (SETDASA and ENTDAA).

0 if there is no preference.

## [◆ ](#a1a895792d02e00784cc76da7ce4b60c9)max\_ibi

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::max\_ibi |
| --- |

Maximum IBI Payload Size.

Valid only if BCR[2] is 1.

## [◆ ](#a0c1a3f65c20ddabc004c82527ec690bb)max\_read\_turnaround

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) i3c\_device\_desc::max\_read\_turnaround |
| --- |

Maximum Read turnaround time in microseconds.

## [◆ ](#ad570493d49084708bf35e9774bc99523)maxrd

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::maxrd |
| --- |

Maximum Read Speed.

## [◆ ](#a02b3bd0d87f92ec67cb7d53e210ec8a9)maxwr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::maxwr |
| --- |

Maximum Write Speed.

## [◆ ](#ac0ec89782c8df7e2e0debf061c754a7e)mrl

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) i3c\_device\_desc::mrl |
| --- |

Maximum Read Length.

## [◆ ](#a29804ab89f08928f14fa4095f57e79ed)mwl

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) i3c\_device\_desc::mwl |
| --- |

Maximum Write Length.

## [◆ ](#a965edbd5d74c06773e190a14d4f6e3cd)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) i3c\_device\_desc::node |
| --- |

## [◆ ](#ac82bd8eccc52a98df76506bd2bed3961)pid

| const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) i3c\_device\_desc::pid |
| --- |

Device Provisioned ID.

## [◆ ](#a105221381d47f690219aa09a20936ae1)static\_addr

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::static\_addr |
| --- |

Static address for this target device.

0 if static address is not being used, and only dynamic address is used. This means that the target device must go through ENTDAA (Dynamic Address Assignment) to get a dynamic address before it can communicate with the controller. This means SETAASA and SETDASA CCC cannot be used to set dynamic address on the target device (as both are to tell target device to use static address as dynamic address).

## [◆ ](#af0905f27f1765c96fc3aaf601926d6ed)supports\_setaasa

| const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) i3c\_device\_desc::supports\_setaasa |
| --- |

Device support for SETAASA.

This will be used as an optimization for bus initializtion if the device supports SETAASA.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[i3c.h](i3c_8h_source.md)

- [i3c\_device\_desc](structi3c__device__desc.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
