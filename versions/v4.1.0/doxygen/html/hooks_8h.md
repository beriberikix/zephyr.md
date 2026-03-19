---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hooks_8h.html
original_path: doxygen/html/hooks_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hooks.h File Reference

Soc and Board hooks.
[More...](#details)

[Go to the source code of this file.](hooks_8h_source.md)

| Functions | |
| --- | --- |
| void | [soc\_reset\_hook](#ad6e8df1eefd1add03ad8379802bd989e) (void) |
|  | SoC hook executed at the beginning of the reset vector. |
| void | [soc\_prep\_hook](#adc333ec5f401d3d8311a496736bd1aa4) (void) |
|  | SoC hook executed after the reset vector. |
| void | [soc\_early\_init\_hook](#a5ee95ec1991b2083210194fe485b3a02) (void) |
|  | SoC hook executed before the kernel and devices are initialized. |
| void | [soc\_late\_init\_hook](#ad3d12da84a31f3d4db5621635f5df687) (void) |
|  | SoC hook executed after the kernel and devices are initialized. |
| void | [soc\_per\_core\_init\_hook](#aed3aa074849066c29086ea37f8f9ef8a) (void) |
|  | SoC per-core initialization. |
| void | [board\_early\_init\_hook](#a684e5461ecf7657b5ab646cdb9e41a51) (void) |
|  | Board hook executed before the kernel starts. |
| void | [board\_late\_init\_hook](#adc6098773fbea0f7ba1575f4a47649b1) (void) |
|  | Board hook executed after the kernel starts. |

## Detailed Description

Soc and Board hooks.

This header file contains function prototypes for the interfaces between zephyr architecture and initialization code and the SoC and board specific logic that resides under boards/ and soc/

Note
:   These are all standard soc and board interfaces that are exported from soc and board specific logic to OS internal logic. These should never be accessed directly from application code but may be freely used within the OS.

## Function Documentation

## [◆ ](#a684e5461ecf7657b5ab646cdb9e41a51)board\_early\_init\_hook()

| void board\_early\_init\_hook | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Board hook executed before the kernel starts.

This is called before the kernel has started. This hook is implemented by the board and can be used to perform any board-specific initialization.

## [◆ ](#adc6098773fbea0f7ba1575f4a47649b1)board\_late\_init\_hook()

| void board\_late\_init\_hook | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Board hook executed after the kernel starts.

This is called after the kernel has started, but before the main function is called. This hook is implemented by the board and can be used to perform any board-specific initialization.

## [◆ ](#a5ee95ec1991b2083210194fe485b3a02)soc\_early\_init\_hook()

| void soc\_early\_init\_hook | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

SoC hook executed before the kernel and devices are initialized.

This hook is implemented by the SoC and can be used to perform any SoC-specific initialization.

## [◆ ](#ad3d12da84a31f3d4db5621635f5df687)soc\_late\_init\_hook()

| void soc\_late\_init\_hook | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

SoC hook executed after the kernel and devices are initialized.

This hook is implemented by the SoC and can be used to perform any SoC-specific initialization.

## [◆ ](#aed3aa074849066c29086ea37f8f9ef8a)soc\_per\_core\_init\_hook()

| void soc\_per\_core\_init\_hook | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

SoC per-core initialization.

This hook is implemented by the SoC and can be used to perform any SoC-specific per-core initialization

## [◆ ](#adc333ec5f401d3d8311a496736bd1aa4)soc\_prep\_hook()

| void soc\_prep\_hook | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

SoC hook executed after the reset vector.

This hook is implemented by the SoC and can be used to perform any SoC-specific initialization.

## [◆ ](#ad6e8df1eefd1add03ad8379802bd989e)soc\_reset\_hook()

| void soc\_reset\_hook | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

SoC hook executed at the beginning of the reset vector.

This hook is implemented by the SoC and can be used to perform any SoC-specific initialization.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [platform](dir_0ba13cd2a44aeab16da188d21efe06c8.md)
- [hooks.h](hooks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
