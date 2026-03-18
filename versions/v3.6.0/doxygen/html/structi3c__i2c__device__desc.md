---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structi3c__i2c__device__desc.html
original_path: doxygen/html/structi3c__i2c__device__desc.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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
| const struct [device](structdevice.md) \* | [bus](#a2c37ea680bc4affe83f9e1bd1a1da5d2) |
|  | Used to attach this node onto a linked list. |
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

Used to attach this node onto a linked list.

I3C bus to which this I2C device is attached

## [◆ ](#a672aca260630deed5d8cdf90896d1115)lvr

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) i3c\_i2c\_device\_desc::lvr |
| --- |

Legacy Virtual Register (LVR).

- LVR[7:5]: I2C device index:
  - 0: I2C device has a 50 ns spike filter where it is not affected by high frequency on SCL.
  - 1: I2C device does not have a 50 ns spike filter but can work with high frequency on SCL.
  - 2: I2C device does not have a 50 ns spike filter and cannot work with high frequency on SCL.
- LVR[4]: I2C mode indicator:
  - 0: FM+ mode
  - 1: FM mode
- LVR[3:0]: Reserved.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[i3c.h](i3c_8h_source.md)

- [i3c\_i2c\_device\_desc](structi3c__i2c__device__desc.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
