---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/gecko-pinctrl_8h.html
original_path: doxygen/html/gecko-pinctrl_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gecko-pinctrl.h File Reference

[Go to the source code of this file.](gecko-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [GECKO\_PSEL](#ac1af8b10c541907308332856fa9affe7)(fun, port, pin) |
|  | Utility macro to build GECKO psels property entry. |
| #define | [GECKO\_LOC](#a0c4e8fbbb218ce88bd4059bda8170e6d)(fun, loc) |
|  | Utility macro to build GECKO\_psels property entry. |
| GECKO\_pin configuration bit field positions and masks. | |
| #define | [GECKO\_FUN\_POS](#af582c317ab79a3961ea00645514fc3f6)   24U |
|  | Position of the function field. |
| #define | [GECKO\_FUN\_MSK](#a87d929d0a1bc9808a854ce582a0c8251)   0xFFFU |
|  | Mask for the function field. |
| #define | [GECKO\_PIN\_POS](#af4fc3615fcff891841b6226b363f9f4c)   0U |
|  | Position of the pin field. |
| #define | [GECKO\_PIN\_MSK](#a9e62aad832626ee3f12e55b8e0102b68)   0xFFU |
|  | Mask for the pin field. |
| #define | [GECKO\_PORT\_POS](#aafabc892e5cc1298ff87a10afdd203ca)   8U |
|  | Position of the port field. |
| #define | [GECKO\_PORT\_MSK](#a750badf0aada694862e9cc8135ef435c)   0xFFU |
|  | Mask for the port field. |
| #define | [GECKO\_LOC\_POS](#a12208aabccc02edd6c64a857f14455f7)   0U |
|  | Position of the loc field. |
| #define | [GECKO\_LOC\_MSK](#adef6df5f1daf2e87dbed89b433ef7d84)   0xFFU |
|  | Mask for the pin field. |
| GECKO\_pinctrl pin functions. | |
| #define | [GECKO\_FUN\_UART\_TX](#a2b19bb5a846aab3b44a3628c586df77b)   0U |
|  | UART TX. |
| #define | [GECKO\_FUN\_UART\_RX](#a68699f16723f6a99594f068dd0c95b2a)   1U |
|  | UART RX. |
| #define | [GECKO\_FUN\_UART\_RTS](#a65f270929aae6f65e659f1f6393d34fa)   2U |
|  | UART RTS. |
| #define | [GECKO\_FUN\_UART\_CTS](#ad4dc9908bb86aea93aaa896ea7755a29)   3U |
|  | UART CTS. |
| #define | [GECKO\_FUN\_UART\_LOC](#a3cf2407ef84050edc079bd0e372b514b)   4U |
|  | UART LOCATION. |
| #define | [GECKO\_FUN\_SPI\_MISO](#a469abb3acc66dfe55f73918b8b2bf5ec)   5U |
| #define | [GECKO\_FUN\_SPI\_MOSI](#ac694f5ec91bde5c9e3de7af7fed94b6b)   6U |
| #define | [GECKO\_FUN\_SPI\_CSN](#a3a5f06615a2add43e56c58a8b497f14b)   7U |
| #define | [GECKO\_FUN\_SPI\_SCK](#a71471924b76182052cbad22824d5992e)   8U |

## Macro Definition Documentation

## [◆ ](#a87d929d0a1bc9808a854ce582a0c8251)GECKO\_FUN\_MSK

| #define GECKO\_FUN\_MSK   0xFFFU |
| --- |

Mask for the function field.

## [◆ ](#af582c317ab79a3961ea00645514fc3f6)GECKO\_FUN\_POS

| #define GECKO\_FUN\_POS   24U |
| --- |

Position of the function field.

## [◆ ](#a3a5f06615a2add43e56c58a8b497f14b)GECKO\_FUN\_SPI\_CSN

| #define GECKO\_FUN\_SPI\_CSN   7U |
| --- |

## [◆ ](#a469abb3acc66dfe55f73918b8b2bf5ec)GECKO\_FUN\_SPI\_MISO

| #define GECKO\_FUN\_SPI\_MISO   5U |
| --- |

## [◆ ](#ac694f5ec91bde5c9e3de7af7fed94b6b)GECKO\_FUN\_SPI\_MOSI

| #define GECKO\_FUN\_SPI\_MOSI   6U |
| --- |

## [◆ ](#a71471924b76182052cbad22824d5992e)GECKO\_FUN\_SPI\_SCK

| #define GECKO\_FUN\_SPI\_SCK   8U |
| --- |

## [◆ ](#ad4dc9908bb86aea93aaa896ea7755a29)GECKO\_FUN\_UART\_CTS

| #define GECKO\_FUN\_UART\_CTS   3U |
| --- |

UART CTS.

## [◆ ](#a3cf2407ef84050edc079bd0e372b514b)GECKO\_FUN\_UART\_LOC

| #define GECKO\_FUN\_UART\_LOC   4U |
| --- |

UART LOCATION.

## [◆ ](#a65f270929aae6f65e659f1f6393d34fa)GECKO\_FUN\_UART\_RTS

| #define GECKO\_FUN\_UART\_RTS   2U |
| --- |

UART RTS.

## [◆ ](#a68699f16723f6a99594f068dd0c95b2a)GECKO\_FUN\_UART\_RX

| #define GECKO\_FUN\_UART\_RX   1U |
| --- |

UART RX.

## [◆ ](#a2b19bb5a846aab3b44a3628c586df77b)GECKO\_FUN\_UART\_TX

| #define GECKO\_FUN\_UART\_TX   0U |
| --- |

UART TX.

## [◆ ](#a0c4e8fbbb218ce88bd4059bda8170e6d)GECKO\_LOC

| #define GECKO\_LOC | ( |  | *fun*, |
| --- | --- | --- | --- |
|  |  |  | *loc* ) |

**Value:**

(((GECKO\_LOCATION(##loc##) & [GECKO\_LOC\_MSK](gecko-pinctrl-s1_8h.md#adef6df5f1daf2e87dbed89b433ef7d84)) << [GECKO\_LOC\_POS](gecko-pinctrl-s1_8h.md#a12208aabccc02edd6c64a857f14455f7)) | \

((GECKO\_FUN\_##fun##\_LOC & [GECKO\_FUN\_MSK](gecko-pinctrl-s1_8h.md#a87d929d0a1bc9808a854ce582a0c8251)) << [GECKO\_FUN\_POS](gecko-pinctrl-s1_8h.md#af582c317ab79a3961ea00645514fc3f6)))

[GECKO\_LOC\_POS](gecko-pinctrl-s1_8h.md#a12208aabccc02edd6c64a857f14455f7)

#define GECKO\_LOC\_POS

Position of the loc field.

**Definition** gecko-pinctrl-s1.h:42

[GECKO\_FUN\_MSK](gecko-pinctrl-s1_8h.md#a87d929d0a1bc9808a854ce582a0c8251)

#define GECKO\_FUN\_MSK

Mask for the function field.

**Definition** gecko-pinctrl-s1.h:29

[GECKO\_LOC\_MSK](gecko-pinctrl-s1_8h.md#adef6df5f1daf2e87dbed89b433ef7d84)

#define GECKO\_LOC\_MSK

Mask for the pin field.

**Definition** gecko-pinctrl-s1.h:44

[GECKO\_FUN\_POS](gecko-pinctrl-s1_8h.md#af582c317ab79a3961ea00645514fc3f6)

#define GECKO\_FUN\_POS

Position of the function field.

**Definition** gecko-pinctrl-s1.h:27

Utility macro to build GECKO\_psels property entry.

Parameters
:   | fun | Pin function configuration (see GECKO\_FUNC\_{name} macros). |
    | --- | --- |
    | loc | Location. |

## [◆ ](#adef6df5f1daf2e87dbed89b433ef7d84)GECKO\_LOC\_MSK

| #define GECKO\_LOC\_MSK   0xFFU |
| --- |

Mask for the pin field.

## [◆ ](#a12208aabccc02edd6c64a857f14455f7)GECKO\_LOC\_POS

| #define GECKO\_LOC\_POS   0U |
| --- |

Position of the loc field.

## [◆ ](#a9e62aad832626ee3f12e55b8e0102b68)GECKO\_PIN\_MSK

| #define GECKO\_PIN\_MSK   0xFFU |
| --- |

Mask for the pin field.

## [◆ ](#af4fc3615fcff891841b6226b363f9f4c)GECKO\_PIN\_POS

| #define GECKO\_PIN\_POS   0U |
| --- |

Position of the pin field.

## [◆ ](#a750badf0aada694862e9cc8135ef435c)GECKO\_PORT\_MSK

| #define GECKO\_PORT\_MSK   0xFFU |
| --- |

Mask for the port field.

## [◆ ](#aafabc892e5cc1298ff87a10afdd203ca)GECKO\_PORT\_POS

| #define GECKO\_PORT\_POS   8U |
| --- |

Position of the port field.

## [◆ ](#ac1af8b10c541907308332856fa9affe7)GECKO\_PSEL

| #define GECKO\_PSEL | ( |  | *fun*, |
| --- | --- | --- | --- |
|  |  |  | *port*, |
|  |  |  | *pin* ) |

**Value:**

(((GECKO\_PORT\_##port & [GECKO\_PORT\_MSK](gecko-pinctrl-s1_8h.md#a750badf0aada694862e9cc8135ef435c)) << [GECKO\_PORT\_POS](gecko-pinctrl-s1_8h.md#aafabc892e5cc1298ff87a10afdd203ca)) | \

((GECKO\_PIN(##pin##) & [GECKO\_PIN\_MSK](gecko-pinctrl-s1_8h.md#a9e62aad832626ee3f12e55b8e0102b68)) << [GECKO\_PIN\_POS](gecko-pinctrl-s1_8h.md#af4fc3615fcff891841b6226b363f9f4c)) | \

((GECKO\_FUN\_##fun & [GECKO\_FUN\_MSK](gecko-pinctrl-s1_8h.md#a87d929d0a1bc9808a854ce582a0c8251)) << [GECKO\_FUN\_POS](gecko-pinctrl-s1_8h.md#af582c317ab79a3961ea00645514fc3f6)))

[GECKO\_PORT\_MSK](gecko-pinctrl-s1_8h.md#a750badf0aada694862e9cc8135ef435c)

#define GECKO\_PORT\_MSK

Mask for the port field.

**Definition** gecko-pinctrl-s1.h:39

[GECKO\_PIN\_MSK](gecko-pinctrl-s1_8h.md#a9e62aad832626ee3f12e55b8e0102b68)

#define GECKO\_PIN\_MSK

Mask for the pin field.

**Definition** gecko-pinctrl-s1.h:34

[GECKO\_PORT\_POS](gecko-pinctrl-s1_8h.md#aafabc892e5cc1298ff87a10afdd203ca)

#define GECKO\_PORT\_POS

Position of the port field.

**Definition** gecko-pinctrl-s1.h:37

[GECKO\_PIN\_POS](gecko-pinctrl-s1_8h.md#af4fc3615fcff891841b6226b363f9f4c)

#define GECKO\_PIN\_POS

Position of the pin field.

**Definition** gecko-pinctrl-s1.h:32

Utility macro to build GECKO psels property entry.

Parameters
:   | fun | Pin function configuration (see GECKO\_FUNC\_{name} macros). |
    | --- | --- |
    | port | Port (0 or 1). |
    | pin | Pin (0..31). |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [gecko-pinctrl.h](gecko-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
