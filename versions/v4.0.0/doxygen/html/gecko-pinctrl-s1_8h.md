---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gecko-pinctrl-s1_8h.html
original_path: doxygen/html/gecko-pinctrl-s1_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gecko-pinctrl-s1.h File Reference

[Go to the source code of this file.](gecko-pinctrl-s1_8h_source.md)

| Macros | |
| --- | --- |
| #define | [GECKO\_PSEL](#ac1af8b10c541907308332856fa9affe7)(fun, port, pin) |
|  | Utility macro to build GECKO psels property entry. |
| #define | [GECKO\_LOC](#a0c4e8fbbb218ce88bd4059bda8170e6d)(fun, loc) |
|  | Utility macro to build GECKO\_psels property entry. |
| GECKO\_pin configuration bit field positions and masks. | |
| #define | [GECKO\_FUN\_POS](#af582c317ab79a3961ea00645514fc3f6)   24U |
|  | Position of the function field. |
| #define | [GECKO\_FUN\_MSK](#a87d929d0a1bc9808a854ce582a0c8251)   0xFFU |
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
| #define | [GECKO\_FUN\_UART\_RX\_LOC](#ac7e6a762e1e7e63f9172d736354820b3)   4U |
|  | UART RX LOCATION. |
| #define | [GECKO\_FUN\_UART\_TX\_LOC](#a59225761dc92d12b23be60f2616c0f9f)   5U |
|  | UART TX LOCATION. |
| #define | [GECKO\_FUN\_UART\_RTS\_LOC](#a8edacb8e79f7d7a84736104949157870)   6U |
|  | UART RTS LOCATION. |
| #define | [GECKO\_FUN\_UART\_CTS\_LOC](#a3ef104d8e946ef746ba9e71bb5c469f5)   7U |
|  | UART CTS LOCATION. |
| #define | [GECKO\_FUN\_SPIM\_MISO](#ad356cf8a63077cd810a13c32d7591e47)   8U |
| #define | [GECKO\_FUN\_SPIM\_MOSI](#a2a24765e466f1264e300d4975429c67c)   9U |
| #define | [GECKO\_FUN\_SPIM\_CS](#a570a5464219faf2252412f09f6281646)   10U |
| #define | [GECKO\_FUN\_SPIM\_SCK](#ab77e588c302f3d18d18b72efa943e0db)   11U |
| #define | [GECKO\_FUN\_LEUART\_RX\_LOC](#a1a9fef5c16e0ab5f2987b4f9ffdc6d22)   12U |
| #define | [GECKO\_FUN\_LEUART\_TX\_LOC](#a49bd14236c6fb7efb44418c05f1a91da)   13U |
| #define | [GECKO\_FUN\_SPIS\_MISO](#a61eedadfb95bdd6fe6e183e9c22fb7ed)   14U |
| #define | [GECKO\_FUN\_SPIS\_MOSI](#a8958587b66b8cd4942b4c9ce9826f689)   15U |
| #define | [GECKO\_FUN\_SPIS\_CS](#af67b9548ffaecb030464cd5f52b16285)   16U |
| #define | [GECKO\_FUN\_SPIS\_SCK](#ae77d65d5717e27242322424179de1cbe)   17U |
| #define | [GECKO\_FUN\_SPI\_MISO\_LOC](#afb0d7445bbbba745b9cc08cb5aa01f44)   18U |
| #define | [GECKO\_FUN\_SPI\_MOSI\_LOC](#a518ae94f50c55f1a19ff70d898bacf34)   19U |
| #define | [GECKO\_FUN\_SPI\_CS\_LOC](#ad6df2bcea0c8e0e68107d70eab753f5f)   20U |
| #define | [GECKO\_FUN\_SPI\_SCK\_LOC](#a73dea09e9111d11f41fd52ee9a296570)   21U |
| #define | [GECKO\_FUN\_I2C\_SDA](#a3c29c6046d30a743df9aaae55c2b0803)   22U |
| #define | [GECKO\_FUN\_I2C\_SCL](#a455a393df63ad05434c993ff18b9d3b5)   23U |
| #define | [GECKO\_FUN\_I2C\_SDA\_LOC](#a405973ead4fd3aa22f2d976257929185)   24U |
| #define | [GECKO\_FUN\_I2C\_SCL\_LOC](#a3216f884cccdd06204765849deec56b0)   25U |

## Macro Definition Documentation

## [◆ ](#a455a393df63ad05434c993ff18b9d3b5)GECKO\_FUN\_I2C\_SCL

| #define GECKO\_FUN\_I2C\_SCL   23U |
| --- |

## [◆ ](#a3216f884cccdd06204765849deec56b0)GECKO\_FUN\_I2C\_SCL\_LOC

| #define GECKO\_FUN\_I2C\_SCL\_LOC   25U |
| --- |

## [◆ ](#a3c29c6046d30a743df9aaae55c2b0803)GECKO\_FUN\_I2C\_SDA

| #define GECKO\_FUN\_I2C\_SDA   22U |
| --- |

## [◆ ](#a405973ead4fd3aa22f2d976257929185)GECKO\_FUN\_I2C\_SDA\_LOC

| #define GECKO\_FUN\_I2C\_SDA\_LOC   24U |
| --- |

## [◆ ](#a1a9fef5c16e0ab5f2987b4f9ffdc6d22)GECKO\_FUN\_LEUART\_RX\_LOC

| #define GECKO\_FUN\_LEUART\_RX\_LOC   12U |
| --- |

## [◆ ](#a49bd14236c6fb7efb44418c05f1a91da)GECKO\_FUN\_LEUART\_TX\_LOC

| #define GECKO\_FUN\_LEUART\_TX\_LOC   13U |
| --- |

## [◆ ](#a87d929d0a1bc9808a854ce582a0c8251)GECKO\_FUN\_MSK

| #define GECKO\_FUN\_MSK   0xFFU |
| --- |

Mask for the function field.

## [◆ ](#af582c317ab79a3961ea00645514fc3f6)GECKO\_FUN\_POS

| #define GECKO\_FUN\_POS   24U |
| --- |

Position of the function field.

## [◆ ](#ad6df2bcea0c8e0e68107d70eab753f5f)GECKO\_FUN\_SPI\_CS\_LOC

| #define GECKO\_FUN\_SPI\_CS\_LOC   20U |
| --- |

## [◆ ](#afb0d7445bbbba745b9cc08cb5aa01f44)GECKO\_FUN\_SPI\_MISO\_LOC

| #define GECKO\_FUN\_SPI\_MISO\_LOC   18U |
| --- |

## [◆ ](#a518ae94f50c55f1a19ff70d898bacf34)GECKO\_FUN\_SPI\_MOSI\_LOC

| #define GECKO\_FUN\_SPI\_MOSI\_LOC   19U |
| --- |

## [◆ ](#a73dea09e9111d11f41fd52ee9a296570)GECKO\_FUN\_SPI\_SCK\_LOC

| #define GECKO\_FUN\_SPI\_SCK\_LOC   21U |
| --- |

## [◆ ](#a570a5464219faf2252412f09f6281646)GECKO\_FUN\_SPIM\_CS

| #define GECKO\_FUN\_SPIM\_CS   10U |
| --- |

## [◆ ](#ad356cf8a63077cd810a13c32d7591e47)GECKO\_FUN\_SPIM\_MISO

| #define GECKO\_FUN\_SPIM\_MISO   8U |
| --- |

## [◆ ](#a2a24765e466f1264e300d4975429c67c)GECKO\_FUN\_SPIM\_MOSI

| #define GECKO\_FUN\_SPIM\_MOSI   9U |
| --- |

## [◆ ](#ab77e588c302f3d18d18b72efa943e0db)GECKO\_FUN\_SPIM\_SCK

| #define GECKO\_FUN\_SPIM\_SCK   11U |
| --- |

## [◆ ](#af67b9548ffaecb030464cd5f52b16285)GECKO\_FUN\_SPIS\_CS

| #define GECKO\_FUN\_SPIS\_CS   16U |
| --- |

## [◆ ](#a61eedadfb95bdd6fe6e183e9c22fb7ed)GECKO\_FUN\_SPIS\_MISO

| #define GECKO\_FUN\_SPIS\_MISO   14U |
| --- |

## [◆ ](#a8958587b66b8cd4942b4c9ce9826f689)GECKO\_FUN\_SPIS\_MOSI

| #define GECKO\_FUN\_SPIS\_MOSI   15U |
| --- |

## [◆ ](#ae77d65d5717e27242322424179de1cbe)GECKO\_FUN\_SPIS\_SCK

| #define GECKO\_FUN\_SPIS\_SCK   17U |
| --- |

## [◆ ](#ad4dc9908bb86aea93aaa896ea7755a29)GECKO\_FUN\_UART\_CTS

| #define GECKO\_FUN\_UART\_CTS   3U |
| --- |

UART CTS.

## [◆ ](#a3ef104d8e946ef746ba9e71bb5c469f5)GECKO\_FUN\_UART\_CTS\_LOC

| #define GECKO\_FUN\_UART\_CTS\_LOC   7U |
| --- |

UART CTS LOCATION.

## [◆ ](#a65f270929aae6f65e659f1f6393d34fa)GECKO\_FUN\_UART\_RTS

| #define GECKO\_FUN\_UART\_RTS   2U |
| --- |

UART RTS.

## [◆ ](#a8edacb8e79f7d7a84736104949157870)GECKO\_FUN\_UART\_RTS\_LOC

| #define GECKO\_FUN\_UART\_RTS\_LOC   6U |
| --- |

UART RTS LOCATION.

## [◆ ](#a68699f16723f6a99594f068dd0c95b2a)GECKO\_FUN\_UART\_RX

| #define GECKO\_FUN\_UART\_RX   1U |
| --- |

UART RX.

## [◆ ](#ac7e6a762e1e7e63f9172d736354820b3)GECKO\_FUN\_UART\_RX\_LOC

| #define GECKO\_FUN\_UART\_RX\_LOC   4U |
| --- |

UART RX LOCATION.

## [◆ ](#a2b19bb5a846aab3b44a3628c586df77b)GECKO\_FUN\_UART\_TX

| #define GECKO\_FUN\_UART\_TX   0U |
| --- |

UART TX.

## [◆ ](#a59225761dc92d12b23be60f2616c0f9f)GECKO\_FUN\_UART\_TX\_LOC

| #define GECKO\_FUN\_UART\_TX\_LOC   5U |
| --- |

UART TX LOCATION.

## [◆ ](#a0c4e8fbbb218ce88bd4059bda8170e6d)GECKO\_LOC

| #define GECKO\_LOC | ( |  | *fun*, |
| --- | --- | --- | --- |
|  |  |  | *loc* ) |

**Value:**

(((GECKO\_LOCATION(##loc##) & [GECKO\_LOC\_MSK](#adef6df5f1daf2e87dbed89b433ef7d84)) << [GECKO\_LOC\_POS](#a12208aabccc02edd6c64a857f14455f7)) | \

((GECKO\_FUN\_##fun##\_LOC & [GECKO\_FUN\_MSK](#a87d929d0a1bc9808a854ce582a0c8251)) << [GECKO\_FUN\_POS](#af582c317ab79a3961ea00645514fc3f6)))

[GECKO\_LOC\_POS](#a12208aabccc02edd6c64a857f14455f7)

#define GECKO\_LOC\_POS

Position of the loc field.

**Definition** gecko-pinctrl-s1.h:42

[GECKO\_FUN\_MSK](#a87d929d0a1bc9808a854ce582a0c8251)

#define GECKO\_FUN\_MSK

Mask for the function field.

**Definition** gecko-pinctrl-s1.h:29

[GECKO\_LOC\_MSK](#adef6df5f1daf2e87dbed89b433ef7d84)

#define GECKO\_LOC\_MSK

Mask for the pin field.

**Definition** gecko-pinctrl-s1.h:44

[GECKO\_FUN\_POS](#af582c317ab79a3961ea00645514fc3f6)

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

(((GECKO\_PORT\_##port & [GECKO\_PORT\_MSK](#a750badf0aada694862e9cc8135ef435c)) << [GECKO\_PORT\_POS](#aafabc892e5cc1298ff87a10afdd203ca)) | \

((GECKO\_PIN(##pin##) & [GECKO\_PIN\_MSK](#a9e62aad832626ee3f12e55b8e0102b68)) << [GECKO\_PIN\_POS](#af4fc3615fcff891841b6226b363f9f4c)) | \

((GECKO\_FUN\_##fun & [GECKO\_FUN\_MSK](#a87d929d0a1bc9808a854ce582a0c8251)) << [GECKO\_FUN\_POS](#af582c317ab79a3961ea00645514fc3f6)))

[GECKO\_PORT\_MSK](#a750badf0aada694862e9cc8135ef435c)

#define GECKO\_PORT\_MSK

Mask for the port field.

**Definition** gecko-pinctrl-s1.h:39

[GECKO\_PIN\_MSK](#a9e62aad832626ee3f12e55b8e0102b68)

#define GECKO\_PIN\_MSK

Mask for the pin field.

**Definition** gecko-pinctrl-s1.h:34

[GECKO\_PORT\_POS](#aafabc892e5cc1298ff87a10afdd203ca)

#define GECKO\_PORT\_POS

Position of the port field.

**Definition** gecko-pinctrl-s1.h:37

[GECKO\_PIN\_POS](#af4fc3615fcff891841b6226b363f9f4c)

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
- [gecko-pinctrl-s1.h](gecko-pinctrl-s1_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
