---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/clock__control__ambiq_8h.html
original_path: doxygen/html/clock__control__ambiq_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

clock\_control\_ambiq.h File Reference

[Go to the source code of this file.](clock__control__ambiq_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [clock\_control\_ambiq\_type](#abe05789f4191227f9cbc2e6755e13c8c) {     [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_BLE](#abe05789f4191227f9cbc2e6755e13c8ca935745058b3bcd41fab102341573bd83) , [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_USB](#abe05789f4191227f9cbc2e6755e13c8ca68bdc3aa9a99d49e46e99bada885b727) , [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_ADC](#abe05789f4191227f9cbc2e6755e13c8ca11a81380c22880e5eefff8ae4e73336e) , [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_AUADC](#abe05789f4191227f9cbc2e6755e13c8ca3383b78c966e6e98d39a784232e91208) ,     [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_DBGCTRL](#abe05789f4191227f9cbc2e6755e13c8ca170229b6f0d44273a5a055a225f8c2e8) , [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_CLKGEN\_MISC](#abe05789f4191227f9cbc2e6755e13c8cabc4feb1ac062903f2289168573a6c3fc) , [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_CLKGEN\_CLKOUT](#abe05789f4191227f9cbc2e6755e13c8ca93b3569c34d2a50baa0843f43495a4d3) , [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_PDM](#abe05789f4191227f9cbc2e6755e13c8cacfe43e2a43499e4c049e6a49492347c3) ,     [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_IIS](#abe05789f4191227f9cbc2e6755e13c8cad5dcc388f72556a7334059ee75b772e9) , [CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_IOM](#abe05789f4191227f9cbc2e6755e13c8ca88af5c919f1e0e118b534734c5b43658) , [CLOCK\_CONTROL\_AMBIQ\_TYPE\_LFXTAL](#abe05789f4191227f9cbc2e6755e13c8caccf3220195f88dfd12aaf7e556aa693f) , [CLOCK\_CONTROL\_AMBIQ\_TYPE\_MAX](#abe05789f4191227f9cbc2e6755e13c8ca7e025623774e3d3b642eede1df96ce5b)   } |
|  | Clocks handled by the CLOCK peripheral. [More...](#abe05789f4191227f9cbc2e6755e13c8c) |

## Enumeration Type Documentation

## [◆ ](#abe05789f4191227f9cbc2e6755e13c8c)clock\_control\_ambiq\_type

| enum [clock\_control\_ambiq\_type](#abe05789f4191227f9cbc2e6755e13c8c) |
| --- |

Clocks handled by the CLOCK peripheral.

Enum shall be used as a sys argument in [clock\_control](group__clock__control__interface.md#ga459b95cb726892b95537d15273413099) API.

| Enumerator | |
| --- | --- |
| CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_BLE |  |
| CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_USB |  |
| CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_ADC |  |
| CLOCK\_CONTROL\_AMBIQ\_TYPE\_HFXTAL\_AUADC |  |
| CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_DBGCTRL |  |
| CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_CLKGEN\_MISC |  |
| CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_CLKGEN\_CLKOUT |  |
| CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_PDM |  |
| CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_IIS |  |
| CLOCK\_CONTROL\_AMBIQ\_TYPE\_HCXTAL\_IOM |  |
| CLOCK\_CONTROL\_AMBIQ\_TYPE\_LFXTAL |  |
| CLOCK\_CONTROL\_AMBIQ\_TYPE\_MAX |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [clock\_control\_ambiq.h](clock__control__ambiq_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
