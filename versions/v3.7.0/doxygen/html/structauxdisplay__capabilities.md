---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structauxdisplay__capabilities.html
original_path: doxygen/html/structauxdisplay__capabilities.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

auxdisplay\_capabilities Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Text Display Interface](group__auxdisplay__interface.md)

Structure holding display capabilities.
[More...](#details)

`#include <[auxdisplay.h](auxdisplay_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [columns](#ac0fc352a5799328211ae6f8c94cdcd7a) |
|  | Number of character columns. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [rows](#af1bcdc27adb678ca4447614a22366aba) |
|  | Number of character rows. |
| [auxdisplay\_mode\_t](group__auxdisplay__interface.md#ga78861a5414ac95e9ca77436c0b82acc2) | [mode](#a55ac50abb253e64e9fb7be6542801dc9) |
|  | Display-specific data (e.g. |
| struct [auxdisplay\_light](structauxdisplay__light.md) | [brightness](#a15e3926754baaefffa1eff45573a59b1) |
|  | Brightness details for display (if supported). |
| struct [auxdisplay\_light](structauxdisplay__light.md) | [backlight](#ace4d7b099428e5f7164c3e9e318c1feb) |
|  | Backlight details for display (if supported). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [custom\_characters](#a4b66412a2000fe09f30c555befbd11d0) |
|  | Number of custom characters supported by display (0 if unsupported). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [custom\_character\_width](#ad77f390f5a6bdbebabc703fdc77322a3) |
|  | Width (in pixels) of a custom character, supplied custom characters should match. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [custom\_character\_height](#adc88b37e9f73a98560099c94c8797741) |
|  | Height (in pixels) of a custom character, supplied custom characters should match. |

## Detailed Description

Structure holding display capabilities.

## Field Documentation

## [◆ ](#ace4d7b099428e5f7164c3e9e318c1feb)backlight

| struct [auxdisplay\_light](structauxdisplay__light.md) auxdisplay\_capabilities::backlight |
| --- |

Backlight details for display (if supported).

## [◆ ](#a15e3926754baaefffa1eff45573a59b1)brightness

| struct [auxdisplay\_light](structauxdisplay__light.md) auxdisplay\_capabilities::brightness |
| --- |

Brightness details for display (if supported).

## [◆ ](#ac0fc352a5799328211ae6f8c94cdcd7a)columns

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) auxdisplay\_capabilities::columns |
| --- |

Number of character columns.

## [◆ ](#adc88b37e9f73a98560099c94c8797741)custom\_character\_height

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) auxdisplay\_capabilities::custom\_character\_height |
| --- |

Height (in pixels) of a custom character, supplied custom characters should match.

## [◆ ](#ad77f390f5a6bdbebabc703fdc77322a3)custom\_character\_width

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) auxdisplay\_capabilities::custom\_character\_width |
| --- |

Width (in pixels) of a custom character, supplied custom characters should match.

## [◆ ](#a4b66412a2000fe09f30c555befbd11d0)custom\_characters

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) auxdisplay\_capabilities::custom\_characters |
| --- |

Number of custom characters supported by display (0 if unsupported).

## [◆ ](#a55ac50abb253e64e9fb7be6542801dc9)mode

| [auxdisplay\_mode\_t](group__auxdisplay__interface.md#ga78861a5414ac95e9ca77436c0b82acc2) auxdisplay\_capabilities::mode |
| --- |

Display-specific data (e.g.

4-bit or 8-bit mode for HD44780-based displays)

## [◆ ](#af1bcdc27adb678ca4447614a22366aba)rows

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) auxdisplay\_capabilities::rows |
| --- |

Number of character rows.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[auxdisplay.h](auxdisplay_8h_source.md)

- [auxdisplay\_capabilities](structauxdisplay__capabilities.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
