---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/mcp356xr-adc_8h_source.html
original_path: doxygen/html/mcp356xr-adc_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcp356xr-adc.h

[Go to the documentation of this file.](mcp356xr-adc_8h.md)

1/\*

2 \* SPDX-License-Identifier: Apache-2.0

3 \*

4 \* Copyright 2024 Syslinbit SCOP SAS

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ADC\_MCP356XR\_ADC\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ADC\_MCP356XR\_ADC\_H\_

9

10#include <[zephyr/dt-bindings/adc/adc.h](dt-bindings_2adc_2adc_8h.md)>

11

[ 12](mcp356xr-adc_8h.md#a6a5d6d4051a27377326c11d01196f1a8)#define MCP356XR\_INPUT\_INTERNAL\_VCM (15)

[ 13](mcp356xr-adc_8h.md#a4f6bd8f7228c541b17cf9b521a29d0e1)#define MCP356XR\_INPUT\_INTERNAL\_TEMPERATURE\_SENSOR\_DIODE\_M (14)

[ 14](mcp356xr-adc_8h.md#a39d249b2ad6f4577e16761ff4bf45dec)#define MCP356XR\_INPUT\_INTERNAL\_TEMPERATURE\_SENSOR\_DIODE\_P (13)

[ 15](mcp356xr-adc_8h.md#a8604cb5d9fbc49741796656f785e88d9)#define MCP356XR\_INPUT\_REFIN\_NEGATIVE (12)

[ 16](mcp356xr-adc_8h.md#ae0ab226eb2ad790e7d9a9d8a24104d87)#define MCP356XR\_INPUT\_REFIN\_POSITIVE (11)

[ 17](mcp356xr-adc_8h.md#a28de6a0a2c7ad855ed0ea27749633657)#define MCP356XR\_INPUT\_RESERVED\_DO\_NOT\_USE (10)

[ 18](mcp356xr-adc_8h.md#a940d3afad7129a802c88c285d47193d7)#define MCP356XR\_INPUT\_AVDD (9)

[ 19](mcp356xr-adc_8h.md#ad9a068c06c9b56f7b0116fb07f94834c)#define MCP356XR\_INPUT\_AGND (8)

[ 20](mcp356xr-adc_8h.md#ac6f8ca4d6a39560e2da5be2b5fd3b6cd)#define MCP356XR\_INPUT\_CH7 (7)

[ 21](mcp356xr-adc_8h.md#aab981b1678c5b75de1edaad9bd884afc)#define MCP356XR\_INPUT\_CH6 (6)

[ 22](mcp356xr-adc_8h.md#abc4bdd2dc5643c2d5c6d3dcd827be2e7)#define MCP356XR\_INPUT\_CH5 (5)

[ 23](mcp356xr-adc_8h.md#a3a6331b37edde2ae896cd1d46b71fed7)#define MCP356XR\_INPUT\_CH4 (4)

[ 24](mcp356xr-adc_8h.md#a1799772688b65ed09bd6c02aa4e115dd)#define MCP356XR\_INPUT\_CH3 (3)

[ 25](mcp356xr-adc_8h.md#a20ac9313a9bc70dbff9b856996a2816d)#define MCP356XR\_INPUT\_CH2 (2)

[ 26](mcp356xr-adc_8h.md#a7f9376ceef42f6cd2840d37749d4da8e)#define MCP356XR\_INPUT\_CH1 (1)

[ 27](mcp356xr-adc_8h.md#af1a8739665e0e6526de46d9152b3d110)#define MCP356XR\_INPUT\_CH0 (0)

28

[ 29](mcp356xr-adc_8h.md#a7ee20df7e89fb87fdf7c2d8570ba5946)#define MCP356XR\_ANALOG\_CLOCK\_NO\_DIV (0)

[ 30](mcp356xr-adc_8h.md#ac5a87179d2a5a3b0de6d48a8482d2eaf)#define MCP356XR\_ANALOG\_CLOCK\_DIV\_2 (1)

[ 31](mcp356xr-adc_8h.md#acb8dabbf6201a9cf7c85f1a62f696fc2)#define MCP356XR\_ANALOG\_CLOCK\_DIV\_4 (2)

[ 32](mcp356xr-adc_8h.md#abe24ab80baec525ccfef4cb1498dc04e)#define MCP356XR\_ANALOG\_CLOCK\_DIV\_8 (3)

33

[ 34](mcp356xr-adc_8h.md#a961331f5f30ea9ecf3b382b21a7dabba)#define MCP356XR\_BOOST\_CURRENT\_BIAS\_DIV\_2 (0)

[ 35](mcp356xr-adc_8h.md#a9dcfadb3ec9107feae72bfe2652278fc)#define MCP356XR\_BOOST\_CURRENT\_BIAS\_MUL\_0\_66 (1)

[ 36](mcp356xr-adc_8h.md#a08692ebc1a69dfd99cdbda3aee1073bf)#define MCP356XR\_BOOST\_CURRENT\_BIAS\_MUL\_1 (2)

[ 37](mcp356xr-adc_8h.md#a6f9bd4da07db025e5b4c3ed40b92dbdc)#define MCP356XR\_BOOST\_CURRENT\_BIAS\_MUL\_2 (3)

38

39#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_ADC\_MCP356XR\_ADC\_H\_ \*/

[adc.h](dt-bindings_2adc_2adc_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [adc](dir_1661dc856f6689c520a6419e0ea32218.md)
- [mcp356xr-adc.h](mcp356xr-adc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
