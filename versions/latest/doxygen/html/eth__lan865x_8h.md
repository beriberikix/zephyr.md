---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/eth__lan865x_8h.html
original_path: doxygen/html/eth__lan865x_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

eth\_lan865x.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](eth__lan865x_8h_source.md)

| Functions | |
| --- | --- |
| int | [eth\_lan865x\_mdio\_c22\_read](#a40e7b77347741d6f71fc2681900a997a) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data) |
|  | Read C22 registers using LAN865X MDIO Bus. |
| int | [eth\_lan865x\_mdio\_c22\_write](#a7b6bad30fa365b78d876d53e24c6a919) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data) |
|  | Write C22 registers using LAN865X MDIO Bus. |
| int | [eth\_lan865x\_mdio\_c45\_read](#a4580c639b8d4f36323ecc02cfa5bfd26) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data) |
|  | Read C45 registers using LAN865X MDIO Bus. |
| int | [eth\_lan865x\_mdio\_c45\_write](#a09613a11b8f59a3c3395a3257f494d17) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data) |
|  | Write C45 registers using LAN865X MDIO Bus. |

## Function Documentation

## [◆ ](#a40e7b77347741d6f71fc2681900a997a)eth\_lan865x\_mdio\_c22\_read()

| int eth\_lan865x\_mdio\_c22\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *prtad*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *regad*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *data* ) |

Read C22 registers using LAN865X MDIO Bus.

This routine provides an interface to perform a C22 register read on the LAN865X MDIO bus.

Parameters
:   | [in] | dev | Pointer to the device structure for the controller |
    | --- | --- | --- |
    | [in] | prtad | Port address |
    | [in] | regad | Register address |
    |  | data | Pointer to receive read data |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ETIMEDOUT | If transaction timedout on the bus |
    | -ENOSYS | if read is not supported |

## [◆ ](#a7b6bad30fa365b78d876d53e24c6a919)eth\_lan865x\_mdio\_c22\_write()

| int eth\_lan865x\_mdio\_c22\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *prtad*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *regad*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data* ) |

Write C22 registers using LAN865X MDIO Bus.

This routine provides an interface to perform a C22 register write on the LAN865X MDIO bus.

Parameters
:   | [in] | dev | Pointer to the device structure for the controller |
    | --- | --- | --- |
    | [in] | prtad | Port address |
    | [in] | regad | Register address |
    | [in] | data | Write data |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ETIMEDOUT | If transaction timedout on the bus |
    | -ENOSYS | if read is not supported |

## [◆ ](#a4580c639b8d4f36323ecc02cfa5bfd26)eth\_lan865x\_mdio\_c45\_read()

| int eth\_lan865x\_mdio\_c45\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *prtad*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *devad*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *regad*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *data* ) |

Read C45 registers using LAN865X MDIO Bus.

This routine provides an interface to perform a C45 register read on the LAN865X MDIO bus.

Parameters
:   | [in] | dev | Pointer to the device structure for the controller |
    | --- | --- | --- |
    | [in] | prtad | Port address |
    | [in] | devad | MMD device address |
    | [in] | regad | Register address |
    |  | data | Pointer to receive read data |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ETIMEDOUT | If transaction timedout on the bus |
    | -ENOSYS | if read is not supported |

## [◆ ](#a09613a11b8f59a3c3395a3257f494d17)eth\_lan865x\_mdio\_c45\_write()

| int eth\_lan865x\_mdio\_c45\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *prtad*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *devad*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *regad*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data* ) |

Write C45 registers using LAN865X MDIO Bus.

This routine provides an interface to perform a C45 register write on the LAN865X MDIO bus.

Parameters
:   | [in] | dev | Pointer to the device structure for the controller |
    | --- | --- | --- |
    | [in] | prtad | Port address |
    | [in] | devad | MMD device address |
    | [in] | regad | Register address |
    | [in] | data | Write data |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ETIMEDOUT | If transaction timedout on the bus |
    | -ENOSYS | if read is not supported |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [ethernet](dir_e26e025f1b2d5c43527f6232564fe44e.md)
- [eth\_lan865x.h](eth__lan865x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
