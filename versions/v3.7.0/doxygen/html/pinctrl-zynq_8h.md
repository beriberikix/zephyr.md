---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/pinctrl-zynq_8h.html
original_path: doxygen/html/pinctrl-zynq_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pinctrl-zynq.h File Reference

[Go to the source code of this file.](pinctrl-zynq_8h_source.md)

| Macros | |
| --- | --- |
| IO buffer type | |
| Definitions for Xilinx Zynq-7000 pinctrl power-source devicetree property values.  The value corresponds to what is written to the IO\_Type field in the MIO\_PIN\_xx SLCR register. | |
| #define | [IO\_STANDARD\_LVCMOS18](#ae50eb80b37c2b6508be7862c720c7c13)   1 |
| #define | [IO\_STANDARD\_LVCMOS25](#aebe38d401743d61abd001aa8735eba10)   2 |
| #define | [IO\_STANDARD\_LVCMOS33](#a6015c7b6d1117ad20f8cab5b0f65d06f)   3 |
| #define | [IO\_STANDARD\_HSTL](#a063cebe926942f2c295d32b5949943af)   4 |
| IO buffer edge rate | |
| Definitions for Xilinx Zynq-7000 pinctrl slew-rate devicetree property values.  The value corresponds to what is written to the Speed field in the MIO\_PIN\_xx SLCR register. | |
| #define | [IO\_SPEED\_SLOW](#a6b26a7bf79bd5160c02eb9d53415165f)   0 |
| #define | [IO\_SPEED\_FAST](#af298ed3b409d8ce6330fa4ff63c9a82e)   1 |

## Macro Definition Documentation

## [◆ ](#af298ed3b409d8ce6330fa4ff63c9a82e)IO\_SPEED\_FAST

| #define IO\_SPEED\_FAST   1 |
| --- |

## [◆ ](#a6b26a7bf79bd5160c02eb9d53415165f)IO\_SPEED\_SLOW

| #define IO\_SPEED\_SLOW   0 |
| --- |

## [◆ ](#a063cebe926942f2c295d32b5949943af)IO\_STANDARD\_HSTL

| #define IO\_STANDARD\_HSTL   4 |
| --- |

## [◆ ](#ae50eb80b37c2b6508be7862c720c7c13)IO\_STANDARD\_LVCMOS18

| #define IO\_STANDARD\_LVCMOS18   1 |
| --- |

## [◆ ](#aebe38d401743d61abd001aa8735eba10)IO\_STANDARD\_LVCMOS25

| #define IO\_STANDARD\_LVCMOS25   2 |
| --- |

## [◆ ](#a6015c7b6d1117ad20f8cab5b0f65d06f)IO\_STANDARD\_LVCMOS33

| #define IO\_STANDARD\_LVCMOS33   3 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [pinctrl-zynq.h](pinctrl-zynq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
