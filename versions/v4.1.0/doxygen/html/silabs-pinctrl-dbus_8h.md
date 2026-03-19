---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/silabs-pinctrl-dbus_8h.html
original_path: doxygen/html/silabs-pinctrl-dbus_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

silabs-pinctrl-dbus.h File Reference

`#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h_source.md)>`

[Go to the source code of this file.](silabs-pinctrl-dbus_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SILABS\_PINCTRL\_GPIO\_PORT\_MASK](#abcb19a19db6aa4c3d5fdfeb91b402742)   0x0000000FUL |
| #define | [SILABS\_PINCTRL\_GPIO\_PIN\_MASK](#a1e87772911ce845375bbbd87f8197cd5)   0x000000F0UL |
| #define | [SILABS\_PINCTRL\_PERIPH\_BASE\_MASK](#ab30280b4a9235fa54509c4a0474815eb)   0x0003FF00UL |
| #define | [SILABS\_PINCTRL\_HAVE\_EN\_MASK](#a001ac259d04f65ecbcdc148085eabc63)   0x00040000UL |
| #define | [SILABS\_PINCTRL\_EN\_BIT\_MASK](#a7eab868fae2d52d4d3ce596d0598494b)   0x00F80000UL |
| #define | [SILABS\_PINCTRL\_ROUTE\_MASK](#a904daec2c54793fc013e72a394fcdaf1)   0x1F000000UL |
| #define | [SILABS\_PINCTRL\_ANALOG\_MASK](#ab6546e7d8e43f44316e9205cbbf4958f)   0x80000000UL |
| #define | [SILABS\_PINCTRL\_ABUS\_BUS\_MASK](#a9c56c5ddaf62514981c576e8f1740c19)   0x0000C000UL |
| #define | [SILABS\_PINCTRL\_ABUS\_PARITY\_MASK](#a76b1bb8aec6c12482b9d11ddcae9c177)   0x00003000UL |
| #define | [SILABS\_PINCTRL\_ABUS\_PERIPH\_MASK](#a9d75fc562522d3fb7f54765a1fa57d41)   0x00000F00UL |
| #define | [SILABS\_PINCTRL\_UNUSED](#a524de9c4274f58e7fac79825203a29b8)   0xFF |
| #define | [SILABS\_PINCTRL\_ANALOG](#afb799e274f9128cdb1ef3d3437b3b8f9)   0xAA |
| #define | [SILABS\_DBUS](#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, periph\_base, en\_present, en\_bit, route) |
| #define | [SILABS\_ABUS](#ac9851f435704e7b096478bca454faf6c)(bus, parity, peripheral) |

## Macro Definition Documentation

## [◆ ](#ac9851f435704e7b096478bca454faf6c)SILABS\_ABUS

| #define SILABS\_ABUS | ( |  | *bus*, |
| --- | --- | --- | --- |
|  |  |  | *parity*, |
|  |  |  | *peripheral* ) |

**Value:**

([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([SILABS\_PINCTRL\_ANALOG\_MASK](#ab6546e7d8e43f44316e9205cbbf4958f), 1) | \

FIELD\_PREP([SILABS\_PINCTRL\_ABUS\_BUS\_MASK](#a9c56c5ddaf62514981c576e8f1740c19), bus) | \

FIELD\_PREP([SILABS\_PINCTRL\_ABUS\_PARITY\_MASK](#a76b1bb8aec6c12482b9d11ddcae9c177), parity) | \

FIELD\_PREP([SILABS\_PINCTRL\_ABUS\_PERIPH\_MASK](#a9d75fc562522d3fb7f54765a1fa57d41), peripheral))

[SILABS\_PINCTRL\_ABUS\_PARITY\_MASK](#a76b1bb8aec6c12482b9d11ddcae9c177)

#define SILABS\_PINCTRL\_ABUS\_PARITY\_MASK

**Definition** silabs-pinctrl-dbus.h:41

[SILABS\_PINCTRL\_ABUS\_BUS\_MASK](#a9c56c5ddaf62514981c576e8f1740c19)

#define SILABS\_PINCTRL\_ABUS\_BUS\_MASK

**Definition** silabs-pinctrl-dbus.h:40

[SILABS\_PINCTRL\_ABUS\_PERIPH\_MASK](#a9d75fc562522d3fb7f54765a1fa57d41)

#define SILABS\_PINCTRL\_ABUS\_PERIPH\_MASK

**Definition** silabs-pinctrl-dbus.h:42

[SILABS\_PINCTRL\_ANALOG\_MASK](#ab6546e7d8e43f44316e9205cbbf4958f)

#define SILABS\_PINCTRL\_ANALOG\_MASK

**Definition** silabs-pinctrl-dbus.h:39

[FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)

#define FIELD\_PREP(mask, value)

**Definition** silabs-pinctrl-siwx91x.h:15

## [◆ ](#ad25567dd5ed53d2ffb37dc1d6cf3d898)SILABS\_DBUS

| #define SILABS\_DBUS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *periph\_base*, |
|  |  |  | *en\_present*, |
|  |  |  | *en\_bit*, |
|  |  |  | *route* ) |

**Value:**

([FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([SILABS\_PINCTRL\_GPIO\_PORT\_MASK](#abcb19a19db6aa4c3d5fdfeb91b402742), port) | \

FIELD\_PREP([SILABS\_PINCTRL\_GPIO\_PIN\_MASK](#a1e87772911ce845375bbbd87f8197cd5), pin) | \

FIELD\_PREP([SILABS\_PINCTRL\_PERIPH\_BASE\_MASK](#ab30280b4a9235fa54509c4a0474815eb), periph\_base) | \

FIELD\_PREP([SILABS\_PINCTRL\_HAVE\_EN\_MASK](#a001ac259d04f65ecbcdc148085eabc63), en\_present) | \

FIELD\_PREP([SILABS\_PINCTRL\_EN\_BIT\_MASK](#a7eab868fae2d52d4d3ce596d0598494b), en\_bit) | \

FIELD\_PREP([SILABS\_PINCTRL\_ROUTE\_MASK](#a904daec2c54793fc013e72a394fcdaf1), route))

[SILABS\_PINCTRL\_HAVE\_EN\_MASK](#a001ac259d04f65ecbcdc148085eabc63)

#define SILABS\_PINCTRL\_HAVE\_EN\_MASK

**Definition** silabs-pinctrl-dbus.h:35

[SILABS\_PINCTRL\_GPIO\_PIN\_MASK](#a1e87772911ce845375bbbd87f8197cd5)

#define SILABS\_PINCTRL\_GPIO\_PIN\_MASK

**Definition** silabs-pinctrl-dbus.h:33

[SILABS\_PINCTRL\_EN\_BIT\_MASK](#a7eab868fae2d52d4d3ce596d0598494b)

#define SILABS\_PINCTRL\_EN\_BIT\_MASK

**Definition** silabs-pinctrl-dbus.h:36

[SILABS\_PINCTRL\_ROUTE\_MASK](#a904daec2c54793fc013e72a394fcdaf1)

#define SILABS\_PINCTRL\_ROUTE\_MASK

**Definition** silabs-pinctrl-dbus.h:37

[SILABS\_PINCTRL\_PERIPH\_BASE\_MASK](#ab30280b4a9235fa54509c4a0474815eb)

#define SILABS\_PINCTRL\_PERIPH\_BASE\_MASK

**Definition** silabs-pinctrl-dbus.h:34

[SILABS\_PINCTRL\_GPIO\_PORT\_MASK](#abcb19a19db6aa4c3d5fdfeb91b402742)

#define SILABS\_PINCTRL\_GPIO\_PORT\_MASK

**Definition** silabs-pinctrl-dbus.h:32

## [◆ ](#a9c56c5ddaf62514981c576e8f1740c19)SILABS\_PINCTRL\_ABUS\_BUS\_MASK

| #define SILABS\_PINCTRL\_ABUS\_BUS\_MASK   0x0000C000UL |
| --- |

## [◆ ](#a76b1bb8aec6c12482b9d11ddcae9c177)SILABS\_PINCTRL\_ABUS\_PARITY\_MASK

| #define SILABS\_PINCTRL\_ABUS\_PARITY\_MASK   0x00003000UL |
| --- |

## [◆ ](#a9d75fc562522d3fb7f54765a1fa57d41)SILABS\_PINCTRL\_ABUS\_PERIPH\_MASK

| #define SILABS\_PINCTRL\_ABUS\_PERIPH\_MASK   0x00000F00UL |
| --- |

## [◆ ](#afb799e274f9128cdb1ef3d3437b3b8f9)SILABS\_PINCTRL\_ANALOG

| #define SILABS\_PINCTRL\_ANALOG   0xAA |
| --- |

## [◆ ](#ab6546e7d8e43f44316e9205cbbf4958f)SILABS\_PINCTRL\_ANALOG\_MASK

| #define SILABS\_PINCTRL\_ANALOG\_MASK   0x80000000UL |
| --- |

## [◆ ](#a7eab868fae2d52d4d3ce596d0598494b)SILABS\_PINCTRL\_EN\_BIT\_MASK

| #define SILABS\_PINCTRL\_EN\_BIT\_MASK   0x00F80000UL |
| --- |

## [◆ ](#a1e87772911ce845375bbbd87f8197cd5)SILABS\_PINCTRL\_GPIO\_PIN\_MASK

| #define SILABS\_PINCTRL\_GPIO\_PIN\_MASK   0x000000F0UL |
| --- |

## [◆ ](#abcb19a19db6aa4c3d5fdfeb91b402742)SILABS\_PINCTRL\_GPIO\_PORT\_MASK

| #define SILABS\_PINCTRL\_GPIO\_PORT\_MASK   0x0000000FUL |
| --- |

## [◆ ](#a001ac259d04f65ecbcdc148085eabc63)SILABS\_PINCTRL\_HAVE\_EN\_MASK

| #define SILABS\_PINCTRL\_HAVE\_EN\_MASK   0x00040000UL |
| --- |

## [◆ ](#ab30280b4a9235fa54509c4a0474815eb)SILABS\_PINCTRL\_PERIPH\_BASE\_MASK

| #define SILABS\_PINCTRL\_PERIPH\_BASE\_MASK   0x0003FF00UL |
| --- |

## [◆ ](#a904daec2c54793fc013e72a394fcdaf1)SILABS\_PINCTRL\_ROUTE\_MASK

| #define SILABS\_PINCTRL\_ROUTE\_MASK   0x1F000000UL |
| --- |

## [◆ ](#a524de9c4274f58e7fac79825203a29b8)SILABS\_PINCTRL\_UNUSED

| #define SILABS\_PINCTRL\_UNUSED   0xFF |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [silabs-pinctrl-dbus.h](silabs-pinctrl-dbus_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
