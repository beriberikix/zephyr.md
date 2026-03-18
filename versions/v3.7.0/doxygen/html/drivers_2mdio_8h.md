---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2mdio_8h.html
original_path: doxygen/html/drivers_2mdio_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mdio.h File Reference

Public APIs for MDIO drivers.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`  
`#include <zephyr/syscalls/mdio.h>`

[Go to the source code of this file.](drivers_2mdio_8h_source.md)

| Functions | |
| --- | --- |
| void | [mdio\_bus\_enable](group__mdio__interface.md#ga7918fa3747d966bd62fb51ceea244c43) (const struct [device](structdevice.md) \*dev) |
|  | Enable MDIO bus. |
| void | [mdio\_bus\_disable](group__mdio__interface.md#gaa7562449eab35b4e3fe14ebab94540bd) (const struct [device](structdevice.md) \*dev) |
|  | Disable MDIO bus and tri-state drivers. |
| int | [mdio\_read](group__mdio__interface.md#gae056ee61011eb6e8d68254680f918434) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data) |
|  | Read from MDIO Bus. |
| int | [mdio\_write](group__mdio__interface.md#ga6a18c3d67c6dc7ef1f3f0e3780015d48) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data) |
|  | Write to MDIO bus. |
| int | [mdio\_read\_c45](group__mdio__interface.md#ga93e360a1201c2bb1ddd33b94e6fce619) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*data) |
|  | Read from MDIO Bus using Clause 45 access. |
| int | [mdio\_write\_c45](group__mdio__interface.md#gad8868e94f7335fea3cd9fea338ef9bd5) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) prtad, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) devad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) regad, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data) |
|  | Write to MDIO bus using Clause 45 access. |

## Detailed Description

Public APIs for MDIO drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mdio.h](drivers_2mdio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
