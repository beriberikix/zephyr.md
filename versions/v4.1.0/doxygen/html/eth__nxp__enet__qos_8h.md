---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/eth__nxp__enet__qos_8h.html
original_path: doxygen/html/eth__nxp__enet__qos_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eth\_nxp\_enet\_qos.h File Reference

`#include <fsl_device_registers.h>`  
`#include <[zephyr/drivers/clock_control.h](clock__control_8h_source.md)>`

[Go to the source code of this file.](eth__nxp__enet__qos_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [nxp\_enet\_qos\_config](structnxp__enet__qos__config.md) |

| Macros | |
| --- | --- |
| #define | [ENET\_QOS\_REG\_GET](#abab3f7ab5002f46083788303b4b4d645)(reg, field, val) |
| #define | [ENET\_QOS\_REG\_PREP](#a1e774124651c10843efc0feaf426225f)(reg, field, val) |
| #define | [ENET\_QOS\_ALIGN\_ADDR\_SHIFT](#a43e2b2075cec6bc77dbbaf606a14df6f)(x) |
| #define | [ENET\_QOS\_MODULE\_CFG](#ae47d351bc24796a02b96e854c02fe630)(module\_dev) |

## Macro Definition Documentation

## [◆ ](#a43e2b2075cec6bc77dbbaf606a14df6f)ENET\_QOS\_ALIGN\_ADDR\_SHIFT

| #define ENET\_QOS\_ALIGN\_ADDR\_SHIFT | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(x >> (ENET\_QOS\_ALIGNMENT >> 1))

## [◆ ](#ae47d351bc24796a02b96e854c02fe630)ENET\_QOS\_MODULE\_CFG

| #define ENET\_QOS\_MODULE\_CFG | ( |  | *module\_dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((struct [nxp\_enet\_qos\_config](structnxp__enet__qos__config.md) \*) module\_dev->config)

[nxp\_enet\_qos\_config](structnxp__enet__qos__config.md)

**Definition** eth\_nxp\_enet\_qos.h:46

## [◆ ](#abab3f7ab5002f46083788303b4b4d645)ENET\_QOS\_REG\_GET

| #define ENET\_QOS\_REG\_GET | ( |  | *reg*, |
| --- | --- | --- | --- |
|  |  |  | *field*, |
|  |  |  | *val* ) |

**Value:**

[FIELD\_GET](silabs-pinctrl-siwx91x_8h.md#aa49a456f06f7bdbedfcf3517e461947e)(\_ENET\_QOS\_REG\_MASK(reg, field), val)

[FIELD\_GET](silabs-pinctrl-siwx91x_8h.md#aa49a456f06f7bdbedfcf3517e461947e)

#define FIELD\_GET(mask, value)

**Definition** silabs-pinctrl-siwx91x.h:14

## [◆ ](#a1e774124651c10843efc0feaf426225f)ENET\_QOS\_REG\_PREP

| #define ENET\_QOS\_REG\_PREP | ( |  | *reg*, |
| --- | --- | --- | --- |
|  |  |  | *field*, |
|  |  |  | *val* ) |

**Value:**

[FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)(\_ENET\_QOS\_REG\_MASK(reg, field), val)

[FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)

#define FIELD\_PREP(mask, value)

**Definition** silabs-pinctrl-siwx91x.h:15

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [ethernet](dir_e26e025f1b2d5c43527f6232564fe44e.md)
- [eth\_nxp\_enet\_qos.h](eth__nxp__enet__qos_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
