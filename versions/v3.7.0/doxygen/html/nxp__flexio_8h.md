---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/nxp__flexio_8h.html
original_path: doxygen/html/nxp__flexio_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp\_flexio.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](nxp__flexio_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [nxp\_flexio\_child\_res](structnxp__flexio__child__res.md) |
|  | Structure containing information about the required resources for a FlexIO child. [More...](structnxp__flexio__child__res.md#details) |
| struct | [nxp\_flexio\_child](structnxp__flexio__child.md) |
|  | Structure containing the required child data for FlexIO. [More...](structnxp__flexio__child.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [nxp\_flexio\_child\_isr\_t](#af11959c4e7c7a5ef56b082fcf0b7f42c)) (void \*user\_data) |
|  | Callback API to inform API user that FlexIO triggered interrupt. |

| Functions | |
| --- | --- |
| void | [nxp\_flexio\_irq\_enable](#a7e84a09852b713337d6e124eb2b8df7d) (const struct [device](structdevice.md) \*dev) |
|  | Enable FlexIO IRQ. |
| void | [nxp\_flexio\_irq\_disable](#a39b6b8b2eda354b4d3a40da48f41e3d2) (const struct [device](structdevice.md) \*dev) |
|  | Disable FlexIO IRQ. |
| void | [nxp\_flexio\_lock](#a3be561d6ee29eb0e23f67ddcf234d22e) (const struct [device](structdevice.md) \*dev) |
|  | Lock FlexIO mutex. |
| void | [nxp\_flexio\_unlock](#ab5ff53d4ac41321fe4726e2ede175ac2) (const struct [device](structdevice.md) \*dev) |
|  | Unlock FlexIO mutex. |
| int | [nxp\_flexio\_get\_rate](#a9c5fdb0b5b11dcc04d42c2c7b98b3ffb) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate) |
|  | Obtain the clock rate of sub-system used by the FlexIO. |
| int | [nxp\_flexio\_child\_attach](#a1208ad4ef70419ff61a87b8b1ff8d446) (const struct [device](structdevice.md) \*dev, const struct [nxp\_flexio\_child](structnxp__flexio__child.md) \*child) |
|  | Attach flexio child to flexio controller. |

## Typedef Documentation

## [◆ ](#af11959c4e7c7a5ef56b082fcf0b7f42c)nxp\_flexio\_child\_isr\_t

| typedef int(\* nxp\_flexio\_child\_isr\_t) (void \*user\_data) |
| --- |

Callback API to inform API user that FlexIO triggered interrupt.

This callback is called from IRQ context.

## Function Documentation

## [◆ ](#a1208ad4ef70419ff61a87b8b1ff8d446)nxp\_flexio\_child\_attach()

| int nxp\_flexio\_child\_attach | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [nxp\_flexio\_child](structnxp__flexio__child.md) \* | *child* ) |

Attach flexio child to flexio controller.

Parameters
:   | dev | Pointer to the device structure for the FlexIO driver instance |
    | --- | --- |
    | child | Pointer to flexio child |

Return values
:   | 0 | if successful |
    | --- | --- |
    | -ENOBUFS | if there are not enough available resources |

## [◆ ](#a9c5fdb0b5b11dcc04d42c2c7b98b3ffb)nxp\_flexio\_get\_rate()

| int nxp\_flexio\_get\_rate | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *rate* ) |

Obtain the clock rate of sub-system used by the FlexIO.

Parameters
:   |  | dev | Pointer to the device structure for the FlexIO driver instance |
    | --- | --- | --- |
    | [out] | rate | Subsystem clock rate |

Return values
:   | 0 | on successful rate reading. |
    | --- | --- |
    | -EAGAIN | if rate cannot be read. Some drivers do not support returning the rate when the clock is off. |
    | -ENOTSUP | if reading the clock rate is not supported for the given sub-system. |
    | -ENOSYS | if the interface is not implemented. |

## [◆ ](#a39b6b8b2eda354b4d3a40da48f41e3d2)nxp\_flexio\_irq\_disable()

| void nxp\_flexio\_irq\_disable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disable FlexIO IRQ.

Parameters
:   | dev | Pointer to the device structure for the FlexIO driver instance |
    | --- | --- |

## [◆ ](#a7e84a09852b713337d6e124eb2b8df7d)nxp\_flexio\_irq\_enable()

| void nxp\_flexio\_irq\_enable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Enable FlexIO IRQ.

Parameters
:   | dev | Pointer to the device structure for the FlexIO driver instance |
    | --- | --- |

## [◆ ](#a3be561d6ee29eb0e23f67ddcf234d22e)nxp\_flexio\_lock()

| void nxp\_flexio\_lock | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Lock FlexIO mutex.

Parameters
:   | dev | Pointer to the device structure for the FlexIO driver instance |
    | --- | --- |

## [◆ ](#ab5ff53d4ac41321fe4726e2ede175ac2)nxp\_flexio\_unlock()

| void nxp\_flexio\_unlock | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

Unlock FlexIO mutex.

Parameters
:   | dev | Pointer to the device structure for the FlexIO driver instance |
    | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [nxp\_flexio](dir_f4ffe9d878970d9b53b3a8be58885b76.md)
- [nxp\_flexio.h](nxp__flexio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
