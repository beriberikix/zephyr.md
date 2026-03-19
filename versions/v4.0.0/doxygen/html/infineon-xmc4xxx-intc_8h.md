---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/infineon-xmc4xxx-intc_8h.html
original_path: doxygen/html/infineon-xmc4xxx-intc_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

infineon-xmc4xxx-intc.h File Reference

[Go to the source code of this file.](infineon-xmc4xxx-intc_8h_source.md)

| Macros | |
| --- | --- |
| #define | [XMC4XXX\_INTC\_PORT\_POS](#ab656d7c0db9ceac360de0e3bb11e05c8)   0 |
| #define | [XMC4XXX\_INTC\_PORT\_MASK](#a0874a1bfc7a1590132fb5802fb490791)   0xf |
| #define | [XMC4XXX\_INTC\_PIN\_POS](#aa5617e14917f6cedae4ab8db3eafa250)   4 |
| #define | [XMC4XXX\_INTC\_PIN\_MASK](#aa8feb63e6eb01cbc5b9226ffdc499f0f)   0xf |
| #define | [XMC4XXX\_INTC\_LINE\_POS](#aa20a96b7bec4cbbf75cf879cf448a379)   8 |
| #define | [XMC4XXX\_INTC\_LINE\_MASK](#a2cae357860189d1b94dce0ee4a3867e0)   0x7 |
| #define | [XMC4XXX\_INTC\_ERU\_SRC\_POS](#a9b1fa99740e6196ae816c3d89eaf8588)   11 |
| #define | [XMC4XXX\_INTC\_ERU\_SRC\_MASK](#a95edfadbd314bf4ea27d88b1dce66e35)   0x7 |
| #define | [XMC4XXX\_INTC\_GET\_PORT](#a908ab6f538ea2a135d002b9c4d9bdea0)(mx) |
| #define | [XMC4XXX\_INTC\_GET\_PIN](#a415130dd3eeae518bb469122bfb44223)(mx) |
| #define | [XMC4XXX\_INTC\_GET\_LINE](#a7ff570440afc268c833d4991c58792d2)(mx) |
| #define | [XMC4XXX\_INTC\_GET\_ERU\_SRC](#afe9fae2864cfa87bc9a458c24d6bdc5e)(mx) |
| #define | [XMC4XXX\_INTC\_SET\_LINE\_MAP](#ac7cbe5628158a8852ea3ea8fafd4e2b1)(port, pin, eru\_src, line) |

## Macro Definition Documentation

## [◆ ](#a95edfadbd314bf4ea27d88b1dce66e35)XMC4XXX\_INTC\_ERU\_SRC\_MASK

| #define XMC4XXX\_INTC\_ERU\_SRC\_MASK   0x7 |
| --- |

## [◆ ](#a9b1fa99740e6196ae816c3d89eaf8588)XMC4XXX\_INTC\_ERU\_SRC\_POS

| #define XMC4XXX\_INTC\_ERU\_SRC\_POS   11 |
| --- |

## [◆ ](#afe9fae2864cfa87bc9a458c24d6bdc5e)XMC4XXX\_INTC\_GET\_ERU\_SRC

| #define XMC4XXX\_INTC\_GET\_ERU\_SRC | ( |  | *mx* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((mx >> [XMC4XXX\_INTC\_ERU\_SRC\_POS](#a9b1fa99740e6196ae816c3d89eaf8588)) & [XMC4XXX\_INTC\_ERU\_SRC\_MASK](#a95edfadbd314bf4ea27d88b1dce66e35))

[XMC4XXX\_INTC\_ERU\_SRC\_MASK](#a95edfadbd314bf4ea27d88b1dce66e35)

#define XMC4XXX\_INTC\_ERU\_SRC\_MASK

**Definition** infineon-xmc4xxx-intc.h:20

[XMC4XXX\_INTC\_ERU\_SRC\_POS](#a9b1fa99740e6196ae816c3d89eaf8588)

#define XMC4XXX\_INTC\_ERU\_SRC\_POS

**Definition** infineon-xmc4xxx-intc.h:19

## [◆ ](#a7ff570440afc268c833d4991c58792d2)XMC4XXX\_INTC\_GET\_LINE

| #define XMC4XXX\_INTC\_GET\_LINE | ( |  | *mx* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((mx >> [XMC4XXX\_INTC\_LINE\_POS](#aa20a96b7bec4cbbf75cf879cf448a379)) & [XMC4XXX\_INTC\_LINE\_MASK](#a2cae357860189d1b94dce0ee4a3867e0))

[XMC4XXX\_INTC\_LINE\_MASK](#a2cae357860189d1b94dce0ee4a3867e0)

#define XMC4XXX\_INTC\_LINE\_MASK

**Definition** infineon-xmc4xxx-intc.h:17

[XMC4XXX\_INTC\_LINE\_POS](#aa20a96b7bec4cbbf75cf879cf448a379)

#define XMC4XXX\_INTC\_LINE\_POS

**Definition** infineon-xmc4xxx-intc.h:16

## [◆ ](#a415130dd3eeae518bb469122bfb44223)XMC4XXX\_INTC\_GET\_PIN

| #define XMC4XXX\_INTC\_GET\_PIN | ( |  | *mx* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((mx >> [XMC4XXX\_INTC\_PIN\_POS](#aa5617e14917f6cedae4ab8db3eafa250)) & [XMC4XXX\_INTC\_PIN\_MASK](#aa8feb63e6eb01cbc5b9226ffdc499f0f))

[XMC4XXX\_INTC\_PIN\_POS](#aa5617e14917f6cedae4ab8db3eafa250)

#define XMC4XXX\_INTC\_PIN\_POS

**Definition** infineon-xmc4xxx-intc.h:13

[XMC4XXX\_INTC\_PIN\_MASK](#aa8feb63e6eb01cbc5b9226ffdc499f0f)

#define XMC4XXX\_INTC\_PIN\_MASK

**Definition** infineon-xmc4xxx-intc.h:14

## [◆ ](#a908ab6f538ea2a135d002b9c4d9bdea0)XMC4XXX\_INTC\_GET\_PORT

| #define XMC4XXX\_INTC\_GET\_PORT | ( |  | *mx* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((mx >> [XMC4XXX\_INTC\_PORT\_POS](#ab656d7c0db9ceac360de0e3bb11e05c8)) & [XMC4XXX\_INTC\_PORT\_MASK](#a0874a1bfc7a1590132fb5802fb490791))

[XMC4XXX\_INTC\_PORT\_MASK](#a0874a1bfc7a1590132fb5802fb490791)

#define XMC4XXX\_INTC\_PORT\_MASK

**Definition** infineon-xmc4xxx-intc.h:11

[XMC4XXX\_INTC\_PORT\_POS](#ab656d7c0db9ceac360de0e3bb11e05c8)

#define XMC4XXX\_INTC\_PORT\_POS

**Definition** infineon-xmc4xxx-intc.h:10

## [◆ ](#a2cae357860189d1b94dce0ee4a3867e0)XMC4XXX\_INTC\_LINE\_MASK

| #define XMC4XXX\_INTC\_LINE\_MASK   0x7 |
| --- |

## [◆ ](#aa20a96b7bec4cbbf75cf879cf448a379)XMC4XXX\_INTC\_LINE\_POS

| #define XMC4XXX\_INTC\_LINE\_POS   8 |
| --- |

## [◆ ](#aa8feb63e6eb01cbc5b9226ffdc499f0f)XMC4XXX\_INTC\_PIN\_MASK

| #define XMC4XXX\_INTC\_PIN\_MASK   0xf |
| --- |

## [◆ ](#aa5617e14917f6cedae4ab8db3eafa250)XMC4XXX\_INTC\_PIN\_POS

| #define XMC4XXX\_INTC\_PIN\_POS   4 |
| --- |

## [◆ ](#a0874a1bfc7a1590132fb5802fb490791)XMC4XXX\_INTC\_PORT\_MASK

| #define XMC4XXX\_INTC\_PORT\_MASK   0xf |
| --- |

## [◆ ](#ab656d7c0db9ceac360de0e3bb11e05c8)XMC4XXX\_INTC\_PORT\_POS

| #define XMC4XXX\_INTC\_PORT\_POS   0 |
| --- |

## [◆ ](#ac7cbe5628158a8852ea3ea8fafd4e2b1)XMC4XXX\_INTC\_SET\_LINE\_MAP

| #define XMC4XXX\_INTC\_SET\_LINE\_MAP | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *eru\_src*, |
|  |  |  | *line* ) |

**Value:**

((port) << [XMC4XXX\_INTC\_PORT\_POS](#ab656d7c0db9ceac360de0e3bb11e05c8) | (pin) << [XMC4XXX\_INTC\_PIN\_POS](#aa5617e14917f6cedae4ab8db3eafa250) | \

(eru\_src) << [XMC4XXX\_INTC\_ERU\_SRC\_POS](#a9b1fa99740e6196ae816c3d89eaf8588) | (line) << [XMC4XXX\_INTC\_LINE\_POS](#aa20a96b7bec4cbbf75cf879cf448a379))

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [infineon-xmc4xxx-intc.h](infineon-xmc4xxx-intc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
