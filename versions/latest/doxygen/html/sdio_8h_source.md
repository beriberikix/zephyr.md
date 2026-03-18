---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sdio_8h_source.html
original_path: doxygen/html/sdio_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sdio.h

[Go to the documentation of this file.](sdio_8h.md)

1/\*

2 \* Copyright 2023 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_SD\_SDIO\_H\_

13#define ZEPHYR\_INCLUDE\_SD\_SDIO\_H\_

14

15#include <[zephyr/device.h](device_8h.md)>

16#include <[zephyr/drivers/sdhc.h](sdhc_8h.md)>

17#include <[zephyr/sd/sd.h](sd_8h.md)>

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

[ 35](sdio_8h.md#aae010680d9035116f503d7ddc1cf8590)int [sdio\_init\_func](sdio_8h.md#aae010680d9035116f503d7ddc1cf8590)(struct [sd\_card](structsd__card.md) \*card, struct [sdio\_func](structsdio__func.md) \*func,

36 enum [sdio\_func\_num](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6) num);

37

[ 48](sdio_8h.md#aa3e60d2c643cd054af56cb44d193074b)int [sdio\_enable\_func](sdio_8h.md#aa3e60d2c643cd054af56cb44d193074b)(struct [sdio\_func](structsdio__func.md) \*func);

49

[ 61](sdio_8h.md#a417829a0558b236465b70ff637a7ca38)int [sdio\_set\_block\_size](sdio_8h.md#a417829a0558b236465b70ff637a7ca38)(struct [sdio\_func](structsdio__func.md) \*func, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bsize);

62

[ 75](sdio_8h.md#a2ac93072041651597b9027156706f0d0)int [sdio\_read\_byte](sdio_8h.md#a2ac93072041651597b9027156706f0d0)(struct [sdio\_func](structsdio__func.md) \*func, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*val);

76

[ 89](sdio_8h.md#a9bfb4970e28830151d2a293475b98435)int [sdio\_write\_byte](sdio_8h.md#a9bfb4970e28830151d2a293475b98435)(struct [sdio\_func](structsdio__func.md) \*func, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) write\_val);

90

[ 104](sdio_8h.md#a8fbc927607a156abc4c47bc551f72b11)int [sdio\_rw\_byte](sdio_8h.md#a8fbc927607a156abc4c47bc551f72b11)(struct [sdio\_func](structsdio__func.md) \*func, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) write\_val,

105 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*read\_val);

106

[ 121](sdio_8h.md#a8cf3af67ef909dd93cdfec29250d76c6)int [sdio\_read\_fifo](sdio_8h.md#a8cf3af67ef909dd93cdfec29250d76c6)(struct [sdio\_func](structsdio__func.md) \*func, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

122 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len);

123

[ 138](sdio_8h.md#a5beb64599a265b117a42858e8087ae4a)int [sdio\_write\_fifo](sdio_8h.md#a5beb64599a265b117a42858e8087ae4a)(struct [sdio\_func](structsdio__func.md) \*func, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

139 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len);

140

[ 155](sdio_8h.md#ab7ec658d92672acfa36d073191d0369f)int [sdio\_read\_blocks\_fifo](sdio_8h.md#ab7ec658d92672acfa36d073191d0369f)(struct [sdio\_func](structsdio__func.md) \*func, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

156 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) blocks);

157

[ 172](sdio_8h.md#a68f75f10ea65cef4bc650b6e2ec4001d)int [sdio\_write\_blocks\_fifo](sdio_8h.md#a68f75f10ea65cef4bc650b6e2ec4001d)(struct [sdio\_func](structsdio__func.md) \*func, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

173 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) blocks);

174

[ 188](sdio_8h.md#a341c846c55adf512a4c3397f38d4bbf9)int [sdio\_read\_addr](sdio_8h.md#a341c846c55adf512a4c3397f38d4bbf9)(struct [sdio\_func](structsdio__func.md) \*func, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

189 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len);

190

[ 205](sdio_8h.md#a55bd42c4d41643444890227ee6cbbfc5)int [sdio\_write\_addr](sdio_8h.md#a55bd42c4d41643444890227ee6cbbfc5)(struct [sdio\_func](structsdio__func.md) \*func, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) reg, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data,

206 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) len);

207

208#ifdef \_\_cplusplus

209}

210#endif

211

212#endif /\* ZEPHYR\_INCLUDE\_SD\_SDMMC\_H\_ \*/

[device.h](device_8h.md)

[sd.h](sd_8h.md)

Public API for SD subsystem.

[sdio\_func\_num](sd__spec_8h.md#a3a542344967c5c1912bde216559e7cd6)

sdio\_func\_num

SDIO function number.

**Definition** sd\_spec.h:767

[sdhc.h](sdhc_8h.md)

SD Host Controller public API header file.

[sdio\_read\_byte](sdio_8h.md#a2ac93072041651597b9027156706f0d0)

int sdio\_read\_byte(struct sdio\_func \*func, uint32\_t reg, uint8\_t \*val)

Read byte from SDIO register.

[sdio\_read\_addr](sdio_8h.md#a341c846c55adf512a4c3397f38d4bbf9)

int sdio\_read\_addr(struct sdio\_func \*func, uint32\_t reg, uint8\_t \*data, uint32\_t len)

Copy bytes from an SDIO card.

[sdio\_set\_block\_size](sdio_8h.md#a417829a0558b236465b70ff637a7ca38)

int sdio\_set\_block\_size(struct sdio\_func \*func, uint16\_t bsize)

Set block size of SDIO function.

[sdio\_write\_addr](sdio_8h.md#a55bd42c4d41643444890227ee6cbbfc5)

int sdio\_write\_addr(struct sdio\_func \*func, uint32\_t reg, uint8\_t \*data, uint32\_t len)

Copy bytes to an SDIO card.

[sdio\_write\_fifo](sdio_8h.md#a5beb64599a265b117a42858e8087ae4a)

int sdio\_write\_fifo(struct sdio\_func \*func, uint32\_t reg, uint8\_t \*data, uint32\_t len)

Write bytes to SDIO fifo.

[sdio\_write\_blocks\_fifo](sdio_8h.md#a68f75f10ea65cef4bc650b6e2ec4001d)

int sdio\_write\_blocks\_fifo(struct sdio\_func \*func, uint32\_t reg, uint8\_t \*data, uint32\_t blocks)

Write blocks to SDIO fifo.

[sdio\_read\_fifo](sdio_8h.md#a8cf3af67ef909dd93cdfec29250d76c6)

int sdio\_read\_fifo(struct sdio\_func \*func, uint32\_t reg, uint8\_t \*data, uint32\_t len)

Read bytes from SDIO fifo.

[sdio\_rw\_byte](sdio_8h.md#a8fbc927607a156abc4c47bc551f72b11)

int sdio\_rw\_byte(struct sdio\_func \*func, uint32\_t reg, uint8\_t write\_val, uint8\_t \*read\_val)

Write byte to SDIO register, and read result.

[sdio\_write\_byte](sdio_8h.md#a9bfb4970e28830151d2a293475b98435)

int sdio\_write\_byte(struct sdio\_func \*func, uint32\_t reg, uint8\_t write\_val)

Write byte to SDIO register.

[sdio\_enable\_func](sdio_8h.md#aa3e60d2c643cd054af56cb44d193074b)

int sdio\_enable\_func(struct sdio\_func \*func)

Enable SDIO function.

[sdio\_init\_func](sdio_8h.md#aae010680d9035116f503d7ddc1cf8590)

int sdio\_init\_func(struct sd\_card \*card, struct sdio\_func \*func, enum sdio\_func\_num num)

Initialize SDIO function.

[sdio\_read\_blocks\_fifo](sdio_8h.md#ab7ec658d92672acfa36d073191d0369f)

int sdio\_read\_blocks\_fifo(struct sdio\_func \*func, uint32\_t reg, uint8\_t \*data, uint32\_t blocks)

Read blocks from SDIO fifo.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[sd\_card](structsd__card.md)

SD card structure.

**Definition** sd.h:63

[sdio\_func](structsdio__func.md)

SDIO function definition.

**Definition** sd.h:48

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sd](dir_ff091b3f4b9505cc58dad89321d1c232.md)
- [sdio.h](sdio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
