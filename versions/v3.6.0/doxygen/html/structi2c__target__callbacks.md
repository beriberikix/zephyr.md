---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structi2c__target__callbacks.html
original_path: doxygen/html/structi2c__target__callbacks.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i2c\_target\_callbacks Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I2C Interface](group__i2c__interface.md)

Structure providing callbacks to be implemented for devices that supports the I2C target API.
[More...](#details)

`#include <[i2c.h](drivers_2i2c_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [i2c\_target\_write\_requested\_cb\_t](group__i2c__interface.md#ga4cd9be521a6c7d088f15b88400624e4e) | [write\_requested](#a76260779cd35191ff64d5848e37b3134) |
| [i2c\_target\_read\_requested\_cb\_t](group__i2c__interface.md#ga244264ecdbd51210728ee92dcbebbc87) | [read\_requested](#a0e3922331e229461764951d93d8c2639) |
| [i2c\_target\_write\_received\_cb\_t](group__i2c__interface.md#ga619db7eea1c4400adcbea5dddf5cf2c5) | [write\_received](#a1606a5b4767ecdc01798d39b63b32f32) |
| [i2c\_target\_read\_processed\_cb\_t](group__i2c__interface.md#ga4cb0ae2cf41fc2105d1baa5e496e5dae) | [read\_processed](#a7566eff7e15bcd0dc7d73bf94187e04e) |
| [i2c\_target\_stop\_cb\_t](group__i2c__interface.md#ga3c898d0bef364461a3502037cf3d40b0) | [stop](#a81bea7375029c3651a8ecd09ea38c131) |

## Detailed Description

Structure providing callbacks to be implemented for devices that supports the I2C target API.

This structure may be shared by multiple devices that implement the same API at different addresses on the bus.

## Field Documentation

## [◆ ](#a7566eff7e15bcd0dc7d73bf94187e04e)read\_processed

| [i2c\_target\_read\_processed\_cb\_t](group__i2c__interface.md#ga4cb0ae2cf41fc2105d1baa5e496e5dae) i2c\_target\_callbacks::read\_processed |
| --- |

## [◆ ](#a0e3922331e229461764951d93d8c2639)read\_requested

| [i2c\_target\_read\_requested\_cb\_t](group__i2c__interface.md#ga244264ecdbd51210728ee92dcbebbc87) i2c\_target\_callbacks::read\_requested |
| --- |

## [◆ ](#a81bea7375029c3651a8ecd09ea38c131)stop

| [i2c\_target\_stop\_cb\_t](group__i2c__interface.md#ga3c898d0bef364461a3502037cf3d40b0) i2c\_target\_callbacks::stop |
| --- |

## [◆ ](#a1606a5b4767ecdc01798d39b63b32f32)write\_received

| [i2c\_target\_write\_received\_cb\_t](group__i2c__interface.md#ga619db7eea1c4400adcbea5dddf5cf2c5) i2c\_target\_callbacks::write\_received |
| --- |

## [◆ ](#a76260779cd35191ff64d5848e37b3134)write\_requested

| [i2c\_target\_write\_requested\_cb\_t](group__i2c__interface.md#ga4cd9be521a6c7d088f15b88400624e4e) i2c\_target\_callbacks::write\_requested |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[i2c.h](drivers_2i2c_8h_source.md)

- [i2c\_target\_callbacks](structi2c__target__callbacks.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
