---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/x86__acpi_8h_source.html
original_path: doxygen/html/x86__acpi_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

x86\_acpi.h

[Go to the documentation of this file.](x86__acpi_8h.md)

1/\*

2 \* Copyright (c) 2023, Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

[ 14](x86__acpi_8h.md#ab71a9896bc2e629a452b801aa2944b25)[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [arch\_acpi\_encode\_irq\_flags](x86__acpi_8h.md#ab71a9896bc2e629a452b801aa2944b25)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) polarity, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) trigger);

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[arch\_acpi\_encode\_irq\_flags](x86__acpi_8h.md#ab71a9896bc2e629a452b801aa2944b25)

uint32\_t arch\_acpi\_encode\_irq\_flags(uint8\_t polarity, uint8\_t trigger)

Encode interrupt flag for x86 architecture.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [x86\_acpi.h](x86__acpi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
