---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structpcie__scan__opt.html
original_path: doxygen/html/structpcie__scan__opt.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pcie\_scan\_opt Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [PCIe Host Interface](group__pcie__host__interface.md)

Options for performing a scan for PCI devices.
[More...](#details)

`#include <[pcie.h](drivers_2pcie_2pcie_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bus](#a036225c7a5730ba2040e03cab491b9da) |
|  | Initial bus number to scan. |
| [pcie\_scan\_cb\_t](group__pcie__host__interface.md#ga922580e4fb6200ef75425bb54801ceda) | [cb](#a28ad6c4993eed7bdf08ce682692bf306) |
|  | Function to call for each found endpoint. |
| void \* | [cb\_data](#a11b39138d2a2b6b1e8e1bd80216a8da6) |
|  | Custom data to pass to the scan callback. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [flags](#a7e485fb824dea16f9d5fdcb7079ebb7e) |
|  | Scan flags. |

## Detailed Description

Options for performing a scan for PCI devices.

## Field Documentation

## [◆ ](#a036225c7a5730ba2040e03cab491b9da)bus

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pcie\_scan\_opt::bus |
| --- |

Initial bus number to scan.

## [◆ ](#a28ad6c4993eed7bdf08ce682692bf306)cb

| [pcie\_scan\_cb\_t](group__pcie__host__interface.md#ga922580e4fb6200ef75425bb54801ceda) pcie\_scan\_opt::cb |
| --- |

Function to call for each found endpoint.

## [◆ ](#a11b39138d2a2b6b1e8e1bd80216a8da6)cb\_data

| void\* pcie\_scan\_opt::cb\_data |
| --- |

Custom data to pass to the scan callback.

## [◆ ](#a7e485fb824dea16f9d5fdcb7079ebb7e)flags

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pcie\_scan\_opt::flags |
| --- |

Scan flags.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/pcie/[pcie.h](drivers_2pcie_2pcie_8h_source.md)

- [pcie\_scan\_opt](structpcie__scan__opt.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
