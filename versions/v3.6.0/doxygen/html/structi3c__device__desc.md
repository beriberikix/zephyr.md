---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structi3c__device__desc.html
original_path: doxygen/html/structi3c__device__desc.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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
| const struct [device](structdevice.md) \*const | [bus](#affdfa3b12a01f966ba5a6a563e669803) |
|  | Used to attach this node onto a linked list. |
| const struct [device](structdevice.md) \*const | [dev](#a653090fd2c78794dae02a2031daddb4b) |
|  | Device driver instance of the I3C device. |
| const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [pid](#ac82bd8eccc52a98df76506bd2bed3961):48 |
|  | Device Provisioned ID. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [static\_addr](#a105221381d47f690219aa09a20936ae1) |
|  | Static address for this target device. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [init\_dynamic\_addr](#a0477ac021d81431a34f55fa1c9f04bb5) |
|  | Initial dynamic address. |
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
| [i3c\_target\_ibi\_cb\_t](group__i3c__ibi.md#ga814cf622b240808216ce4e87802e965c) | [ibi\_cb](#a1f9eda89e2e28971e39aace38ddbb265) |
|  | Private data by the controller to aid in transactions. |

## Detailed Description

Structure describing a I3C target device.

Instances of this are passed to the I3C controller device APIs, for example:

- i3c\_device\_register() to tell the controller of a target device.
- i3c\_transfers() to initiate data transfers between controller and target device.

Fields `bus`, `pid` and `static_addr` must be initialized by the module that implements the target device behavior prior to passing the object reference to I3C controller device APIs. `static_addr` can be zero if target device does not have static address.

Field `node` should not be initialized or modified manually.

## Field Documentation

## [◆ ](#ae1cff0a31d9cc5d7b18206556f8e0b21)bcr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::bcr |
| --- |

Bus Characteristic Register (BCR).

- BCR[7:6]: Device Role
  - 0: I3C Target
  - 1: I3C Controller capable
  - 2: Reserved
  - 3: Reserved
- BCR[5]: Advanced Capabilities
  - 0: Does not support optional advanced capabilities.
  - 1: Supports optional advanced capabilities which can be viewed via GETCAPS CCC.
- BCR[4}: Virtual Target Support
  - 0: Is not a virtual target.
  - 1: Is a virtual target.
- BCR[3]: Offline Capable
  - 0: Will always response to I3C commands.
  - 1: Will not always response to I3C commands.
- BCR[2]: IBI Payload
  - 0: No data bytes following the accepted IBI.
  - 1: One data byte (MDB, Mandatory Data Byte) follows the accepted IBI. Additional data bytes may also follows.
- BCR[1]: IBI Request Capable
  - 0: Not capable
  - 1: Capable
- BCR[0]: Max Data Speed Limitation
  - 0: No Limitation
  - 1: Limitation obtained via GETMXDS CCC.

## [◆ ](#affdfa3b12a01f966ba5a6a563e669803)bus

| const struct [device](structdevice.md)\* const i3c\_device\_desc::bus |
| --- |

Used to attach this node onto a linked list.

I3C bus to which this target device is attached

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

## [◆ ](#a260730aef8862b2898ef6f65cf4956c4)group\_addr

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::group\_addr |
| --- |

Group address for this target device.

Set during:

- Reset Group Address(es) (RSTGRPA)
- Set Group Address (SETGRPA)

0 if group address has not been assigned.

## [◆ ](#a1f9eda89e2e28971e39aace38ddbb265)ibi\_cb

| [i3c\_target\_ibi\_cb\_t](group__i3c__ibi.md#ga814cf622b240808216ce4e87802e965c) i3c\_device\_desc::ibi\_cb |
| --- |

Private data by the controller to aid in transactions.

Do not modify. In-Band Interrupt (IBI) callback.

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

## [◆ ](#ac82bd8eccc52a98df76506bd2bed3961)pid

| const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) i3c\_device\_desc::pid |
| --- |

Device Provisioned ID.

## [◆ ](#a105221381d47f690219aa09a20936ae1)static\_addr

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_device\_desc::static\_addr |
| --- |

Static address for this target device.

0 if static address is not being used, and only dynamic address is used. This means that the target device must go through ENTDAA (Dynamic Address Assignment) to get a dynamic address before it can communicate with the controller. This means SETAASA and SETDASA CCC cannot be used to set dynamic address on the target device (as both are to tell target device to use static address as dynamic address).

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[i3c.h](i3c_8h_source.md)

- [i3c\_device\_desc](structi3c__device__desc.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
