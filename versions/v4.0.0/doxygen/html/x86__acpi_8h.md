---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/x86__acpi_8h.html
original_path: doxygen/html/x86__acpi_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

x86\_acpi.h File Reference

[Go to the source code of this file.](x86__acpi_8h_source.md)

| Functions | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [arch\_acpi\_encode\_irq\_flags](#ab71a9896bc2e629a452b801aa2944b25) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) polarity, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) trigger) |
|  | Encode interrupt flag for x86 architecture. |

## Function Documentation

## [◆ ](#ab71a9896bc2e629a452b801aa2944b25)arch\_acpi\_encode\_irq\_flags()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) arch\_acpi\_encode\_irq\_flags | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *polarity*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *trigger* ) |

Encode interrupt flag for x86 architecture.

Parameters
:   | polarity | the interrupt polarity received from ACPICA lib |
    | --- | --- |
    | trigger | the interrupt level received from ACPICA lib |

Returns
:   return encoded interrupt flag

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [x86\_acpi.h](x86__acpi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
