---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/numicro-pinctrl_8h.html
original_path: doxygen/html/numicro-pinctrl_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

numicro-pinctrl.h File Reference

[Go to the source code of this file.](numicro-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [NUMICRO\_MFP\_SHIFT](#ade38f6532bffc69965d508f87d8e1df8)   0U |
| #define | [NUMICRO\_MFP\_MASK](#ac9f4334d26beb00d4dea13d857d5e7ec)   0xFU |
| #define | [NUMICRO\_PIN\_SHIFT](#a478aaec941e205a651ec9dd5e50739eb)   4U |
| #define | [NUMICRO\_PIN\_MASK](#ad6e70da52aa12c4b62e8793bd3d64435)   0xFU |
| #define | [NUMICRO\_PORT\_SHIFT](#aa189da0ec8b427feabb6e0bfe82d6e88)   8U |
| #define | [NUMICRO\_PORT\_MASK](#a82825df678162bc24705348ac1ac74ca)   0xFU |
| #define | [NUMICRO\_PINMUX](#a0309131a80b52c3c5ba0561b7cbd943f)(port, pin, mfp) |
|  | Pin configuration configuration bit field. |
| #define | [NUMICRO\_PORT](#a23e9fef3fcbdab7aec502bd71c9e64cc)(pinmux) |
| #define | [NUMICRO\_PIN](#a1ab973be84bf86ae6c286b26379ac0dd)(pinmux) |
| #define | [NUMICRO\_MFP](#ac2c31c43ea1a65f7a5e9dae18ff39b0c)(pinmux) |

## Macro Definition Documentation

## [◆ ](#ac2c31c43ea1a65f7a5e9dae18ff39b0c)NUMICRO\_MFP

| #define NUMICRO\_MFP | ( |  | *pinmux* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((pinmux) >> [NUMICRO\_MFP\_SHIFT](#ade38f6532bffc69965d508f87d8e1df8)) & [NUMICRO\_MFP\_MASK](#ac9f4334d26beb00d4dea13d857d5e7ec))

[NUMICRO\_MFP\_MASK](#ac9f4334d26beb00d4dea13d857d5e7ec)

#define NUMICRO\_MFP\_MASK

**Definition** numicro-pinctrl.h:11

[NUMICRO\_MFP\_SHIFT](#ade38f6532bffc69965d508f87d8e1df8)

#define NUMICRO\_MFP\_SHIFT

**Definition** numicro-pinctrl.h:10

## [◆ ](#ac9f4334d26beb00d4dea13d857d5e7ec)NUMICRO\_MFP\_MASK

| #define NUMICRO\_MFP\_MASK   0xFU |
| --- |

## [◆ ](#ade38f6532bffc69965d508f87d8e1df8)NUMICRO\_MFP\_SHIFT

| #define NUMICRO\_MFP\_SHIFT   0U |
| --- |

## [◆ ](#a1ab973be84bf86ae6c286b26379ac0dd)NUMICRO\_PIN

| #define NUMICRO\_PIN | ( |  | *pinmux* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((pinmux) >> [NUMICRO\_PIN\_SHIFT](#a478aaec941e205a651ec9dd5e50739eb)) & [NUMICRO\_PIN\_MASK](#ad6e70da52aa12c4b62e8793bd3d64435))

[NUMICRO\_PIN\_SHIFT](#a478aaec941e205a651ec9dd5e50739eb)

#define NUMICRO\_PIN\_SHIFT

**Definition** numicro-pinctrl.h:12

[NUMICRO\_PIN\_MASK](#ad6e70da52aa12c4b62e8793bd3d64435)

#define NUMICRO\_PIN\_MASK

**Definition** numicro-pinctrl.h:13

## [◆ ](#ad6e70da52aa12c4b62e8793bd3d64435)NUMICRO\_PIN\_MASK

| #define NUMICRO\_PIN\_MASK   0xFU |
| --- |

## [◆ ](#a478aaec941e205a651ec9dd5e50739eb)NUMICRO\_PIN\_SHIFT

| #define NUMICRO\_PIN\_SHIFT   4U |
| --- |

## [◆ ](#a0309131a80b52c3c5ba0561b7cbd943f)NUMICRO\_PINMUX

| #define NUMICRO\_PINMUX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *mfp* ) |

**Value:**

(((((port) - 'A') & [NUMICRO\_PORT\_MASK](#a82825df678162bc24705348ac1ac74ca)) << [NUMICRO\_PORT\_SHIFT](#aa189da0ec8b427feabb6e0bfe82d6e88)) | \

(((pin) & [NUMICRO\_PIN\_MASK](#ad6e70da52aa12c4b62e8793bd3d64435)) << [NUMICRO\_PIN\_SHIFT](#a478aaec941e205a651ec9dd5e50739eb)) | \

(((mfp) & [NUMICRO\_MFP\_MASK](#ac9f4334d26beb00d4dea13d857d5e7ec)) << [NUMICRO\_MFP\_SHIFT](#ade38f6532bffc69965d508f87d8e1df8)))

[NUMICRO\_PORT\_MASK](#a82825df678162bc24705348ac1ac74ca)

#define NUMICRO\_PORT\_MASK

**Definition** numicro-pinctrl.h:15

[NUMICRO\_PORT\_SHIFT](#aa189da0ec8b427feabb6e0bfe82d6e88)

#define NUMICRO\_PORT\_SHIFT

**Definition** numicro-pinctrl.h:14

Pin configuration configuration bit field.

Fields:

- mfp [ 0 : 3 ]
- pin [ 4 : 7 ]
- port [ 8 : 11 ]

Parameters
:   | port | Port ('A'..'H') |
    | --- | --- |
    | pin | Pin (0..15) |
    | mfp | Multi-function value (0..15) |

## [◆ ](#a23e9fef3fcbdab7aec502bd71c9e64cc)NUMICRO\_PORT

| #define NUMICRO\_PORT | ( |  | *pinmux* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((pinmux) >> [NUMICRO\_PORT\_SHIFT](#aa189da0ec8b427feabb6e0bfe82d6e88)) & [NUMICRO\_PORT\_MASK](#a82825df678162bc24705348ac1ac74ca))

## [◆ ](#a82825df678162bc24705348ac1ac74ca)NUMICRO\_PORT\_MASK

| #define NUMICRO\_PORT\_MASK   0xFU |
| --- |

## [◆ ](#aa189da0ec8b427feabb6e0bfe82d6e88)NUMICRO\_PORT\_SHIFT

| #define NUMICRO\_PORT\_SHIFT   8U |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [numicro-pinctrl.h](numicro-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
