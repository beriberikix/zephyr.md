---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.html
original_path: doxygen/html/drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp\_rtxxx\_dsp\_ctrl.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/dt-bindings/misc/nxp_rtxxx_dsp_ctrl.h](dt-bindings_2misc_2nxp__rtxxx__dsp__ctrl_8h_source.md)>`

[Go to the source code of this file.](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [nxp\_rtxxx\_dsp\_ctrl\_api](structnxp__rtxxx__dsp__ctrl__api.md) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [nxp\_rtxxx\_dsp\_ctrl\_api\_load\_section](#ab6ed31cfcaa45744f960bc19d89f642f)) (const struct [device](structdevice.md) \*, const void \*, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9), enum [nxp\_rtxxx\_dsp\_ctrl\_section\_type](#a1230a21b6c11930f80fc5f12605de762)) |
| typedef void(\* | [nxp\_rtxxx\_dsp\_ctrl\_api\_enable](#a561283f2992839e0191d2fcfef12d989)) (const struct [device](structdevice.md) \*dev) |
| typedef void(\* | [nxp\_rtxxx\_dsp\_ctrl\_api\_disable](#a17b3a647a7798b34c820366916b2a1c5)) (const struct [device](structdevice.md) \*dev) |

| Enumerations | |
| --- | --- |
| enum | [nxp\_rtxxx\_dsp\_ctrl\_section\_type](#a1230a21b6c11930f80fc5f12605de762) { [NXP\_RTXXX\_DSP\_CTRL\_SECTION\_RESET](#a1230a21b6c11930f80fc5f12605de762a8c63b3117b7c525e96be2b054395cfff) = 0 , [NXP\_RTXXX\_DSP\_CTRL\_SECTION\_TEXT](#a1230a21b6c11930f80fc5f12605de762ab0c726ddfdf30c89075fcf9c7b4586e7) = 1 , [NXP\_RTXXX\_DSP\_CTRL\_SECTION\_DATA](#a1230a21b6c11930f80fc5f12605de762aa43ff75c06ea161e322d77b8dede7791) = 2 } |
|  | Describes an image section type selection. [More...](#a1230a21b6c11930f80fc5f12605de762) |

| Functions | |
| --- | --- |
| static int | [nxp\_rtxxx\_dsp\_ctrl\_load\_section](#af1bd0005fe3a6d46d559b249b3ff8ca8) (const struct [device](structdevice.md) \*dev, const void \*base, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length, enum [nxp\_rtxxx\_dsp\_ctrl\_section\_type](#a1230a21b6c11930f80fc5f12605de762) section) |
|  | Loads a specified image representing a specified section to a particular region in the DSP's memory. |
| static void | [nxp\_rtxxx\_dsp\_ctrl\_enable](#a9cc6dd311f29f2e7c79fc74c39658041) (const struct [device](structdevice.md) \*dev) |
|  | Starts (unstalls) the DSP. |
| static void | [nxp\_rtxxx\_dsp\_ctrl\_disable](#a2efeac2828998f896f2e1bfb532700cd) (const struct [device](structdevice.md) \*dev) |
|  | Stops (stalls) the DSP. |

## Typedef Documentation

## [◆ ](#a17b3a647a7798b34c820366916b2a1c5)nxp\_rtxxx\_dsp\_ctrl\_api\_disable

| typedef void(\* nxp\_rtxxx\_dsp\_ctrl\_api\_disable) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a561283f2992839e0191d2fcfef12d989)nxp\_rtxxx\_dsp\_ctrl\_api\_enable

| typedef void(\* nxp\_rtxxx\_dsp\_ctrl\_api\_enable) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#ab6ed31cfcaa45744f960bc19d89f642f)nxp\_rtxxx\_dsp\_ctrl\_api\_load\_section

| typedef int(\* nxp\_rtxxx\_dsp\_ctrl\_api\_load\_section) (const struct [device](structdevice.md) \*, const void \*, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9), enum [nxp\_rtxxx\_dsp\_ctrl\_section\_type](#a1230a21b6c11930f80fc5f12605de762)) |
| --- |

## Enumeration Type Documentation

## [◆ ](#a1230a21b6c11930f80fc5f12605de762)nxp\_rtxxx\_dsp\_ctrl\_section\_type

| enum [nxp\_rtxxx\_dsp\_ctrl\_section\_type](#a1230a21b6c11930f80fc5f12605de762) |
| --- |

Describes an image section type selection.

| Enumerator | |
| --- | --- |
| NXP\_RTXXX\_DSP\_CTRL\_SECTION\_RESET |  |
| NXP\_RTXXX\_DSP\_CTRL\_SECTION\_TEXT |  |
| NXP\_RTXXX\_DSP\_CTRL\_SECTION\_DATA |  |

## Function Documentation

## [◆ ](#a2efeac2828998f896f2e1bfb532700cd)nxp\_rtxxx\_dsp\_ctrl\_disable()

| | void nxp\_rtxxx\_dsp\_ctrl\_disable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Stops (stalls) the DSP.

Parameters
:   | dev | DSP device |
    | --- | --- |

## [◆ ](#a9cc6dd311f29f2e7c79fc74c39658041)nxp\_rtxxx\_dsp\_ctrl\_enable()

| | void nxp\_rtxxx\_dsp\_ctrl\_enable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Starts (unstalls) the DSP.

Parameters
:   | dev | DSP device |
    | --- | --- |

## [◆ ](#af1bd0005fe3a6d46d559b249b3ff8ca8)nxp\_rtxxx\_dsp\_ctrl\_load\_section()

| | int nxp\_rtxxx\_dsp\_ctrl\_load\_section | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | const void \* | *base*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length*, | |  |  | enum [nxp\_rtxxx\_dsp\_ctrl\_section\_type](#a1230a21b6c11930f80fc5f12605de762) | *section* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Loads a specified image representing a specified section to a particular region in the DSP's memory.

Parameters
:   | dev | DSP device |
    | --- | --- |
    | base | Base pointer of the image to load |
    | length | Length of the image |
    | section | Section type which specified image represents |

Returns
:   int 0 on success, -EINVAL for invalid parameters, -ENOMEM for image bigger than the target region

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [nxp\_rtxxx\_dsp\_ctrl](dir_6ae4f57dc0f23a67287970302be617ac.md)
- [nxp\_rtxxx\_dsp\_ctrl.h](drivers_2misc_2nxp__rtxxx__dsp__ctrl_2nxp__rtxxx__dsp__ctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
