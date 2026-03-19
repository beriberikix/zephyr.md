---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structi3c__config__custom.html
original_path: doxygen/html/structi3c__config__custom.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i3c\_config\_custom Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md)

Custom I3C configuration parameters.
[More...](#details)

`#include <[i3c.h](i3c_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [id](#a8a9c0173d3439ed1ed10e8c7013bdb31) |
|  | ID of the configuration parameter. |
| union { |  |
| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)   [val](#ae0320b4b277b1c3d4ad438cd71d98340) |  |
|  | Value of configuration parameter. [More...](#ae0320b4b277b1c3d4ad438cd71d98340) |
| void \*   [ptr](#a2bcc6334871ced958cd0358aeab38dcd) |  |
|  | Pointer to configuration parameter. [More...](#a2bcc6334871ced958cd0358aeab38dcd) |
| }; |  |

## Detailed Description

Custom I3C configuration parameters.

This can be used to configure the I3C hardware on parameters not covered by [i3c\_config\_controller](structi3c__config__controller.md "Configuration parameters for I3C hardware to act as controller.") or [i3c\_config\_target](structi3c__config__target.md "Configuration parameters for I3C hardware to act as target device."). Mostly used to configure vendor specific parameters of the I3C hardware.

## Field Documentation

## [◆ ](#a8d222900c02bbc7f2fa96ba09067d7a7)[union]

| union { ... } [i3c\_config\_custom](structi3c__config__custom.md) |
| --- |

## [◆ ](#a8a9c0173d3439ed1ed10e8c7013bdb31)id

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) i3c\_config\_custom::id |
| --- |

ID of the configuration parameter.

## [◆ ](#a2bcc6334871ced958cd0358aeab38dcd)ptr

| void\* i3c\_config\_custom::ptr |
| --- |

Pointer to configuration parameter.

Mainly used to pointer to a struct that the device driver understands.

## [◆ ](#ae0320b4b277b1c3d4ad438cd71d98340)val

| [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) i3c\_config\_custom::val |
| --- |

Value of configuration parameter.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[i3c.h](i3c_8h_source.md)

- [i3c\_config\_custom](structi3c__config__custom.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
