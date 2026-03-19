---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/rv32m1-pinctrl_8h.html
original_path: doxygen/html/rv32m1-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rv32m1-pinctrl.h File Reference

[Go to the source code of this file.](rv32m1-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RV32M1\_MUX](#adc4ef31269f0084e7551566b199093df)(port, pin, mux) |
|  | Specify PORTx->PCR register MUX field. |

## Macro Definition Documentation

## [◆ ](#adc4ef31269f0084e7551566b199093df)RV32M1\_MUX

| #define RV32M1\_MUX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin*, |
|  |  |  | *mux* ) |

**Value:**

(((((port) - 'A') & 0xF) << 28) | \

(((pin) & 0x3F) << 22) | \

(((mux) & 0x7) << 8))

Specify PORTx->PCR register MUX field.

Parameters
:   | port | Port name ('A' to 'E') |
    | --- | --- |
    | pin | Port pin number (0 to 31) |
    | mux | Alternate function number (0 to 7) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [rv32m1-pinctrl.h](rv32m1-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
