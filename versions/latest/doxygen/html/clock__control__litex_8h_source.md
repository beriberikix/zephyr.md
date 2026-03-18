---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/clock__control__litex_8h_source.html
original_path: doxygen/html/clock__control__litex_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

clock\_control\_litex.h

[Go to the documentation of this file.](clock__control__litex_8h.md)

1/\*

2 \* Copyright (c) 2020 Antmicro <www.antmicro.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef CLK\_CTRL\_LITEX\_H

13#define CLK\_CTRL\_LITEX\_H

14

22

23#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

24

[ 25](group__clock__control__litex__interface.md#ga9b1e322b8de40ff6226e14932ef2b879)#define MMCM DT\_NODELABEL(clock0)

[ 26](group__clock__control__litex__interface.md#ga6accac6cf4c18a252888165efb14e637)#define NCLKOUT DT\_PROP\_LEN(MMCM, clock\_output\_names)

27

[ 37](structlitex__clk__setup.md)struct [litex\_clk\_setup](structlitex__clk__setup.md) {

[ 38](structlitex__clk__setup.md#a3aae2c535eda1df7dcde112a87a9f767) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [clkout\_nr](structlitex__clk__setup.md#a3aae2c535eda1df7dcde112a87a9f767);

[ 39](structlitex__clk__setup.md#a630a776504a52618c9bbdb6899956567) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rate](structlitex__clk__setup.md#a630a776504a52618c9bbdb6899956567);

[ 40](structlitex__clk__setup.md#a5f0684af5cddeb4222142c57ff935b2d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [phase](structlitex__clk__setup.md#a5f0684af5cddeb4222142c57ff935b2d);

[ 41](structlitex__clk__setup.md#a237035479b7a9fec8eaa5ac9c104e977) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [duty](structlitex__clk__setup.md#a237035479b7a9fec8eaa5ac9c104e977);

42};

43

47

48#endif /\* CLK\_CTRL\_LITEX\_H \*/

[types.h](include_2zephyr_2types_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[litex\_clk\_setup](structlitex__clk__setup.md)

Structure for interfacing with clock control API.

**Definition** clock\_control\_litex.h:37

[litex\_clk\_setup::duty](structlitex__clk__setup.md#a237035479b7a9fec8eaa5ac9c104e977)

uint8\_t duty

**Definition** clock\_control\_litex.h:41

[litex\_clk\_setup::clkout\_nr](structlitex__clk__setup.md#a3aae2c535eda1df7dcde112a87a9f767)

uint8\_t clkout\_nr

**Definition** clock\_control\_litex.h:38

[litex\_clk\_setup::phase](structlitex__clk__setup.md#a5f0684af5cddeb4222142c57ff935b2d)

uint16\_t phase

**Definition** clock\_control\_litex.h:40

[litex\_clk\_setup::rate](structlitex__clk__setup.md#a630a776504a52618c9bbdb6899956567)

uint32\_t rate

**Definition** clock\_control\_litex.h:39

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [clock\_control](dir_a984f062cf5261c2619127147b7cc64c.md)
- [clock\_control\_litex.h](clock__control__litex_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
