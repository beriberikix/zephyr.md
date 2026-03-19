---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structdevice__state.html
original_path: doxygen/html/structdevice__state.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

device\_state Struct Reference

[Device Model](group__device__model.md)

Runtime device dynamic structure (in RAM) per driver instance.
[More...](#details)

`#include <[device.h](device_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [init\_res](#a4895f511a9246d27a378253ab82e263e) |
|  | Device initialization return code (positive errno value). |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [initialized](#a26bb28bbe4c17c4f0e496d2b04d4a3ad): 1 |
|  | Indicates the device initialization function has been invoked. |

## Detailed Description

Runtime device dynamic structure (in RAM) per driver instance.

Fields in this are expected to be default-initialized to zero. The kernel driver infrastructure and driver access functions are responsible for ensuring that any non-zero initialization is done before they are accessed.

## Field Documentation

## [◆ ](#a4895f511a9246d27a378253ab82e263e)init\_res

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) device\_state::init\_res |
| --- |

Device initialization return code (positive errno value).

Device initialization functions return a negative errno code if they fail. In Zephyr, errno values do not exceed 255, so we can store the positive result value in a [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type.

## [◆ ](#a26bb28bbe4c17c4f0e496d2b04d4a3ad)initialized

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) device\_state::initialized |
| --- |

Indicates the device initialization function has been invoked.

---

The documentation for this struct was generated from the following file:

- zephyr/[device.h](device_8h_source.md)

- [device\_state](structdevice__state.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
