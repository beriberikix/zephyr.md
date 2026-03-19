---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/devicetree_2spi_8h_source.html
original_path: doxygen/html/devicetree_2spi_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

spi.h

[Go to the documentation of this file.](devicetree_2spi_8h.md)

1

5

6/\*

7 \* Copyright (c) 2020 Nordic Semiconductor

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_DEVICETREE\_SPI\_H\_

13#define ZEPHYR\_INCLUDE\_DEVICETREE\_SPI\_H\_

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

24

[ 52](group__devicetree-spi.md#gae8db0ce095bdd0066a845bc6a9bf329d)#define DT\_SPI\_HAS\_CS\_GPIOS(spi) DT\_NODE\_HAS\_PROP(spi, cs\_gpios)

53

[ 78](group__devicetree-spi.md#gafe2bddd961fe08672e131cfbd73eb466)#define DT\_SPI\_NUM\_CS\_GPIOS(spi) \

79 COND\_CODE\_1(DT\_SPI\_HAS\_CS\_GPIOS(spi), \

80 (DT\_PROP\_LEN(spi, cs\_gpios)), (0))

81

[ 117](group__devicetree-spi.md#gad66b759d6aa4826f2c68a94e8708ad4f)#define DT\_SPI\_DEV\_HAS\_CS\_GPIOS(spi\_dev) DT\_SPI\_HAS\_CS\_GPIOS(DT\_BUS(spi\_dev))

118

[ 150](group__devicetree-spi.md#ga0eaad9de680b5ac7cd8950957560c199)#define DT\_SPI\_DEV\_CS\_GPIOS\_CTLR(spi\_dev) \

151 DT\_GPIO\_CTLR\_BY\_IDX(DT\_BUS(spi\_dev), cs\_gpios, DT\_REG\_ADDR\_RAW(spi\_dev))

152

[ 183](group__devicetree-spi.md#ga8c1dd6a65c6f7fdf67291be1ed47fc9f)#define DT\_SPI\_DEV\_CS\_GPIOS\_PIN(spi\_dev) \

184 DT\_GPIO\_PIN\_BY\_IDX(DT\_BUS(spi\_dev), cs\_gpios, DT\_REG\_ADDR\_RAW(spi\_dev))

185

[ 211](group__devicetree-spi.md#ga49fd9c174931b44584a7dbbc18f7c644)#define DT\_SPI\_DEV\_CS\_GPIOS\_FLAGS(spi\_dev) \

212 DT\_GPIO\_FLAGS\_BY\_IDX(DT\_BUS(spi\_dev), cs\_gpios, DT\_REG\_ADDR\_RAW(spi\_dev))

213

[ 221](group__devicetree-spi.md#ga830f87f79c297c090a1929a288edc7ba)#define DT\_INST\_SPI\_DEV\_HAS\_CS\_GPIOS(inst) \

222 DT\_SPI\_DEV\_HAS\_CS\_GPIOS(DT\_DRV\_INST(inst))

223

[ 231](group__devicetree-spi.md#ga0ffb7729cd90dc7bf4a1c33ead96a3d8)#define DT\_INST\_SPI\_DEV\_CS\_GPIOS\_CTLR(inst) \

232 DT\_SPI\_DEV\_CS\_GPIOS\_CTLR(DT\_DRV\_INST(inst))

233

[ 240](group__devicetree-spi.md#ga1ce1031b612257718fbab08139db44cf)#define DT\_INST\_SPI\_DEV\_CS\_GPIOS\_PIN(inst) \

241 DT\_SPI\_DEV\_CS\_GPIOS\_PIN(DT\_DRV\_INST(inst))

242

[ 250](group__devicetree-spi.md#ga6f42b7305ec5373ae14cad220a3196da)#define DT\_INST\_SPI\_DEV\_CS\_GPIOS\_FLAGS(inst) \

251 DT\_SPI\_DEV\_CS\_GPIOS\_FLAGS(DT\_DRV\_INST(inst))

252

256

257#ifdef \_\_cplusplus

258}

259#endif

260

261#endif /\* ZEPHYR\_INCLUDE\_DEVICETREE\_SPI\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [spi.h](devicetree_2spi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
