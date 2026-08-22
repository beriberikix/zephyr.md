---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ambiq-apollo5-pinctrl_8h.html
original_path: doxygen/html/ambiq-apollo5-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ambiq-apollo5-pinctrl.h File Reference

[Go to the source code of this file.](ambiq-apollo5-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [APOLLO5\_ALT\_FUNC\_POS](#a8c22bac02781bdc9237a2c7938d78038)   0 |
| #define | [APOLLO5\_ALT\_FUNC\_MASK](#ac35ff7ac7e5d9288dcab2c51413fb1fa)   0xf |
| #define | [APOLLO5\_PIN\_NUM\_POS](#a7d03a9ca93525a57900dd019f950f34d)   4 |
| #define | [APOLLO5\_PIN\_NUM\_MASK](#aedbb28a1b3dca93f8ce798a14365ffda)   0xff |
| #define | [APOLLO5\_PINMUX](#a2111c8a6e9540311d67885ad557f9d7b)(pin\_num, alt\_func) |

## Macro Definition Documentation

## [◆ ](#ac35ff7ac7e5d9288dcab2c51413fb1fa)APOLLO5\_ALT\_FUNC\_MASK

| #define APOLLO5\_ALT\_FUNC\_MASK   0xf |
| --- |

## [◆ ](#a8c22bac02781bdc9237a2c7938d78038)APOLLO5\_ALT\_FUNC\_POS

| #define APOLLO5\_ALT\_FUNC\_POS   0 |
| --- |

## [◆ ](#aedbb28a1b3dca93f8ce798a14365ffda)APOLLO5\_PIN\_NUM\_MASK

| #define APOLLO5\_PIN\_NUM\_MASK   0xff |
| --- |

## [◆ ](#a7d03a9ca93525a57900dd019f950f34d)APOLLO5\_PIN\_NUM\_POS

| #define APOLLO5\_PIN\_NUM\_POS   4 |
| --- |

## [◆ ](#a2111c8a6e9540311d67885ad557f9d7b)APOLLO5\_PINMUX

| #define APOLLO5\_PINMUX | ( |  | *pin\_num*, |
| --- | --- | --- | --- |
|  |  |  | *alt\_func* ) |

**Value:**

(pin\_num << [APOLLO5\_PIN\_NUM\_POS](#a7d03a9ca93525a57900dd019f950f34d) | \

alt\_func << [APOLLO5\_ALT\_FUNC\_POS](#a8c22bac02781bdc9237a2c7938d78038))

[APOLLO5\_PIN\_NUM\_POS](#a7d03a9ca93525a57900dd019f950f34d)

#define APOLLO5\_PIN\_NUM\_POS

**Definition** ambiq-apollo5-pinctrl.h:13

[APOLLO5\_ALT\_FUNC\_POS](#a8c22bac02781bdc9237a2c7938d78038)

#define APOLLO5\_ALT\_FUNC\_POS

**Definition** ambiq-apollo5-pinctrl.h:10

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [ambiq-apollo5-pinctrl.h](ambiq-apollo5-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
