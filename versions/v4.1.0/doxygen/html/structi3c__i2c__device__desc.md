---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structi3c__i2c__device__desc.html
original_path: doxygen/html/structi3c__i2c__device__desc.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_i2c\_device\_desc Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md)

Structure describing a I2C device on I3C bus.
[More...](#details)

`#include <[i3c.h](i3c_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#acfcf72db311b19e479e9147ce5257245) |
| const struct [device](structdevice.md) \* | [bus](#a2c37ea680bc4affe83f9e1bd1a1da5d2) |
|  | I3C bus to which this I2C device is attached. |
| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [addr](#a5826aa935faccf9b9f05cf52b2fb842d) |
|  | Static address for this I2C device. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [lvr](#a672aca260630deed5d8cdf90896d1115) |
|  | Legacy Virtual Register (LVR). |

## Detailed Description

Structure describing a I2C device on I3C bus.

Instances of this are passed to the I3C controller device APIs, for example: () i3c\_i2c\_device\_register() to tell the controller of an I2C device. () i3c\_i2c\_transfers() to initiate data transfers between controller and I2C device.

Fields other than `node` must be initialized by the module that implements the device behavior prior to passing the object reference to I3C controller device APIs.

## Field Documentation

## [◆ ](#a5826aa935faccf9b9f05cf52b2fb842d)addr

| const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) i3c\_i2c\_device\_desc::addr |
| --- |

Static address for this I2C device.

## [◆ ](#a2c37ea680bc4affe83f9e1bd1a1da5d2)bus

| const struct [device](structdevice.md)\* i3c\_i2c\_device\_desc::bus |
| --- |

I3C bus to which this I2C device is attached.

## [◆ ](#a672aca260630deed5d8cdf90896d1115)lvr

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_i2c\_device\_desc::lvr |
| --- |

Legacy Virtual Register (LVR).

See also
:   [I3C\_LVR](group__i3c__interface.md#I3C_LVR "I3C_LVR")

## [◆ ](#acfcf72db311b19e479e9147ce5257245)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) i3c\_i2c\_device\_desc::node |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[i3c.h](i3c_8h_source.md)

- [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
