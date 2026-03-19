---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__pcie__host__ptm__interface.html
original_path: doxygen/html/group__pcie__host__ptm__interface.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

PCIe Host PTM Interface

[Device Driver APIs](group__io__interfaces.md) » [PCIe Host Interface](group__pcie__host__interface.md)

PCIe Host PTM Interface.
[More...](#details)

| Functions | |
| --- | --- |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_ptm\_enable](#gae868e8140938c293ad5685cd77131924) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf) |
|  | Enable PTM on endpoint. |

## Detailed Description

PCIe Host PTM Interface.

## Function Documentation

## [◆ ](#gae868e8140938c293ad5685cd77131924)pcie\_ptm\_enable()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pcie\_ptm\_enable | ( | [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ptm.h](ptm_8h.md)>`

Enable PTM on endpoint.

Parameters
:   | bdf | the PCI(e) endpoint |
    | --- | --- |

Returns
:   true if that was successful, false otherwise

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
