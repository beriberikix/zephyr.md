---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__mdio__interface.html
original_path: doxygen/html/group__mdio__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MDIO Interface

[Device Driver APIs](group__io__interfaces.md)

MDIO Interface.
[More...](#details)

| Functions | |
| --- | --- |
| void | [mdio\_bus\_enable](#ga7918fa3747d966bd62fb51ceea244c43) (const struct [device](structdevice.md) \*dev) |
|  | Enable MDIO bus. |
| void | [mdio\_bus\_disable](#gaa7562449eab35b4e3fe14ebab94540bd) (const struct [device](structdevice.md) \*dev) |
|  | Disable MDIO bus and tri-state drivers. |
| int | [mdio\_read](#gae056ee61011eb6e8d68254680f918434) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data) |
|  | Read from MDIO Bus. |
| int | [mdio\_write](#ga6a18c3d67c6dc7ef1f3f0e3780015d48) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data) |
|  | Write to MDIO bus. |
| int | [mdio\_read\_c45](#ga93e360a1201c2bb1ddd33b94e6fce619) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data) |
|  | Read from MDIO Bus using Clause 45 access. |
| int | [mdio\_write\_c45](#gad8868e94f7335fea3cd9fea338ef9bd5) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data) |
|  | Write to MDIO bus using Clause 45 access. |

## Detailed Description

MDIO Interface.

## Function Documentation

## [◆ ](#gaa7562449eab35b4e3fe14ebab94540bd)mdio\_bus\_disable()

| void mdio\_bus\_disable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mdio.h](drivers_2mdio_8h.md)>`

Disable MDIO bus and tri-state drivers.

Parameters
:   | [in] | dev | Pointer to the device structure for the controller |
    | --- | --- | --- |

## [◆ ](#ga7918fa3747d966bd62fb51ceea244c43)mdio\_bus\_enable()

| void mdio\_bus\_enable | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mdio.h](drivers_2mdio_8h.md)>`

Enable MDIO bus.

Parameters
:   | [in] | dev | Pointer to the device structure for the controller |
    | --- | --- | --- |

## [◆ ](#gae056ee61011eb6e8d68254680f918434)mdio\_read()

| int mdio\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *prtad*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *regad*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *data* ) |

`#include <[mdio.h](drivers_2mdio_8h.md)>`

Read from MDIO Bus.

This routine provides a generic interface to perform a read on the MDIO bus.

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

## [◆ ](#ga93e360a1201c2bb1ddd33b94e6fce619)mdio\_read\_c45()

| int mdio\_read\_c45 | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *prtad*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *devad*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *regad*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *data* ) |

`#include <[mdio.h](drivers_2mdio_8h.md)>`

Read from MDIO Bus using Clause 45 access.

This routine provides an interface to perform a read on the MDIO bus using IEEE 802.3 Clause 45 access.

Parameters
:   | [in] | dev | Pointer to the device structure for the controller |
    | --- | --- | --- |
    | [in] | prtad | Port address |
    | [in] | devad | Device address |
    | [in] | regad | Register address |
    |  | data | Pointer to receive read data |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ETIMEDOUT | If transaction timedout on the bus |
    | -ENOSYS | if write using Clause 45 access is not supported |

## [◆ ](#ga6a18c3d67c6dc7ef1f3f0e3780015d48)mdio\_write()

| int mdio\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *prtad*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *regad*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data* ) |

`#include <[mdio.h](drivers_2mdio_8h.md)>`

Write to MDIO bus.

This routine provides a generic interface to perform a write on the MDIO bus.

Parameters
:   | [in] | dev | Pointer to the device structure for the controller |
    | --- | --- | --- |
    | [in] | prtad | Port address |
    | [in] | regad | Register address |
    | [in] | data | Data to write |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ETIMEDOUT | If transaction timedout on the bus |
    | -ENOSYS | if write is not supported |

## [◆ ](#gad8868e94f7335fea3cd9fea338ef9bd5)mdio\_write\_c45()

| int mdio\_write\_c45 | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *prtad*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *devad*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *regad*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data* ) |

`#include <[mdio.h](drivers_2mdio_8h.md)>`

Write to MDIO bus using Clause 45 access.

This routine provides an interface to perform a write on the MDIO bus using IEEE 802.3 Clause 45 access.

Parameters
:   | [in] | dev | Pointer to the device structure for the controller |
    | --- | --- | --- |
    | [in] | prtad | Port address |
    | [in] | devad | Device address |
    | [in] | regad | Register address |
    | [in] | data | Data to write |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ETIMEDOUT | If transaction timedout on the bus |
    | -ENOSYS | if write using Clause 45 access is not supported |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
