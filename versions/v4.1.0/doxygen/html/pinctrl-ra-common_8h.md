---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/pinctrl-ra-common_8h.html
original_path: doxygen/html/pinctrl-ra-common_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-ra-common.h File Reference

[Go to the source code of this file.](pinctrl-ra-common_8h_source.md)

| Macros | |
| --- | --- |
| #define | [PORT4\_POS](#a113d98d5dece049c593a5aef12437d75)   29 |
| #define | [PORT4\_MASK](#a6f0d2254afbdaa587e24fc3da5e01ec7)   0x1 |
| #define | [PSEL\_POS](#a36b3cbcfdb0dc8773bd2075f03b7af21)   24 |
| #define | [PSEL\_MASK](#a08e7257d70d4cddfec8fe57461aef1f7)   0x5 |
| #define | [PORT\_POS](#ab9a807cc315af3fc52903b357fe4def0)   21 |
| #define | [PORT\_MASK](#a753dc0d0821793f46a32babcf2087a82)   0x7 |
| #define | [PIN\_POS](#a34af731a37775b8da8f1c63a2e6186e3)   17 |
| #define | [PIN\_MASK](#a838ccdbc9c7ae5cfc5ec5328f1fd7404)   0xF |
| #define | [OPT\_POS](#a301c04edbd1a0282380fdaa5af14ad55)   0 |
| #define | [OPT\_MASK](#af44b6097b3ff3bd26acb0dee9a571374)   0x1B000 |
| #define | [RA\_PINCFG\_GPIO](#a90dffe4222a204ce3d83db055af089a1)   0x00000 |
| #define | [RA\_PINCFG\_FUNC](#a200abb246b5840ee429b5ffdd76fe35c)   0x10000 |
| #define | [RA\_PINCFG\_ANALOG](#aab0068f1482f166541504b8bc2958cf4)   0x08000 |
| #define | [RA\_PINCFG](#a10cac511c82da4ae64ef387f5d08183e)(port, pin, psel, opt) |

## Macro Definition Documentation

## [◆ ](#af44b6097b3ff3bd26acb0dee9a571374)OPT\_MASK

| #define OPT\_MASK   0x1B000 |
| --- |

## [◆ ](#a301c04edbd1a0282380fdaa5af14ad55)OPT\_POS

| #define OPT\_POS   0 |
| --- |

## [◆ ](#a838ccdbc9c7ae5cfc5ec5328f1fd7404)PIN\_MASK

| #define PIN\_MASK   0xF |
| --- |

## [◆ ](#a34af731a37775b8da8f1c63a2e6186e3)PIN\_POS

| #define PIN\_POS   17 |
| --- |

## [◆ ](#a6f0d2254afbdaa587e24fc3da5e01ec7)PORT4\_MASK

| #define PORT4\_MASK   0x1 |
| --- |

## [◆ ](#a113d98d5dece049c593a5aef12437d75)PORT4\_POS

| #define PORT4\_POS   29 |
| --- |

## [◆ ](#a753dc0d0821793f46a32babcf2087a82)PORT\_MASK

| #define PORT\_MASK   0x7 |
| --- |

## [◆ ](#ab9a807cc315af3fc52903b357fe4def0)PORT\_POS

| #define PORT\_POS   21 |
| --- |

## [◆ ](#a08e7257d70d4cddfec8fe57461aef1f7)PSEL\_MASK

| #define PSEL\_MASK   0x5 |
| --- |

## [◆ ](#a36b3cbcfdb0dc8773bd2075f03b7af21)PSEL\_POS

| #define PSEL\_POS   24 |
| --- |

## [◆ ](#a10cac511c82da4ae64ef387f5d08183e)RA\_PINCFG

| #define RA\_PINCFG | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *psel*, |
|  |  |  | *opt* ) |

**Value:**

((((psel)&[PSEL\_MASK](#a08e7257d70d4cddfec8fe57461aef1f7)) << [PSEL\_POS](#a36b3cbcfdb0dc8773bd2075f03b7af21)) | (((pin)&[PIN\_MASK](#a838ccdbc9c7ae5cfc5ec5328f1fd7404)) << [PIN\_POS](#a34af731a37775b8da8f1c63a2e6186e3)) | \

(((port)&[PORT\_MASK](#a753dc0d0821793f46a32babcf2087a82)) << [PORT\_POS](#ab9a807cc315af3fc52903b357fe4def0)) | ((((port) >> 3) & [PORT4\_MASK](#a6f0d2254afbdaa587e24fc3da5e01ec7)) << [PORT4\_POS](#a113d98d5dece049c593a5aef12437d75)) | \

(((opt)&[OPT\_MASK](#af44b6097b3ff3bd26acb0dee9a571374)) << [OPT\_POS](#a301c04edbd1a0282380fdaa5af14ad55)))

[PSEL\_MASK](#a08e7257d70d4cddfec8fe57461aef1f7)

#define PSEL\_MASK

**Definition** pinctrl-ra-common.h:13

[PORT4\_POS](#a113d98d5dece049c593a5aef12437d75)

#define PORT4\_POS

**Definition** pinctrl-ra-common.h:10

[OPT\_POS](#a301c04edbd1a0282380fdaa5af14ad55)

#define OPT\_POS

**Definition** pinctrl-ra-common.h:18

[PIN\_POS](#a34af731a37775b8da8f1c63a2e6186e3)

#define PIN\_POS

**Definition** pinctrl-ra-common.h:16

[PSEL\_POS](#a36b3cbcfdb0dc8773bd2075f03b7af21)

#define PSEL\_POS

**Definition** pinctrl-ra-common.h:12

[PORT4\_MASK](#a6f0d2254afbdaa587e24fc3da5e01ec7)

#define PORT4\_MASK

**Definition** pinctrl-ra-common.h:11

[PORT\_MASK](#a753dc0d0821793f46a32babcf2087a82)

#define PORT\_MASK

**Definition** pinctrl-ra-common.h:15

[PIN\_MASK](#a838ccdbc9c7ae5cfc5ec5328f1fd7404)

#define PIN\_MASK

**Definition** pinctrl-ra-common.h:17

[PORT\_POS](#ab9a807cc315af3fc52903b357fe4def0)

#define PORT\_POS

**Definition** pinctrl-ra-common.h:14

[OPT\_MASK](#af44b6097b3ff3bd26acb0dee9a571374)

#define OPT\_MASK

**Definition** pinctrl-ra-common.h:19

## [◆ ](#aab0068f1482f166541504b8bc2958cf4)RA\_PINCFG\_ANALOG

| #define RA\_PINCFG\_ANALOG   0x08000 |
| --- |

## [◆ ](#a200abb246b5840ee429b5ffdd76fe35c)RA\_PINCFG\_FUNC

| #define RA\_PINCFG\_FUNC   0x10000 |
| --- |

## [◆ ](#a90dffe4222a204ce3d83db055af089a1)RA\_PINCFG\_GPIO

| #define RA\_PINCFG\_GPIO   0x00000 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [renesas](dir_17f48eb154be6cea623223db5de209e7.md)
- [pinctrl-ra-common.h](pinctrl-ra-common_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
