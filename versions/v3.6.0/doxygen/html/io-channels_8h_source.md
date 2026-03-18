---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/io-channels_8h_source.html
original_path: doxygen/html/io-channels_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

io-channels.h

[Go to the documentation of this file.](io-channels_8h.md)

1

5

6/\*

7 \* Copyright (c) 2020, Linaro Ltd.

8 \*

9 \* SPDX-License-Identifier: Apache-2.0

10 \*/

11

12#ifndef ZEPHYR\_INCLUDE\_DEVICETREE\_IO\_CHANNELS\_H\_

13#define ZEPHYR\_INCLUDE\_DEVICETREE\_IO\_CHANNELS\_H\_

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

24

[ 50](group__devicetree-io-channels.md#gaf5bbae59dca995d827ff3ec8b9ce187c)#define DT\_IO\_CHANNELS\_CTLR\_BY\_IDX(node\_id, idx) \

51 DT\_PHANDLE\_BY\_IDX(node\_id, io\_channels, idx)

52

[ 79](group__devicetree-io-channels.md#ga1d6422230eb139beec9ac0f25ca2eab3)#define DT\_IO\_CHANNELS\_CTLR\_BY\_NAME(node\_id, name) \

80 DT\_PHANDLE\_BY\_NAME(node\_id, io\_channels, name)

81

[ 89](group__devicetree-io-channels.md#gaef1d0ee74798d9e60f5c5fa0c0f8db48)#define DT\_IO\_CHANNELS\_CTLR(node\_id) DT\_IO\_CHANNELS\_CTLR\_BY\_IDX(node\_id, 0)

90

[ 100](group__devicetree-io-channels.md#gacf417be0bda7b8ddfb20503f8d846822)#define DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_IDX(inst, idx) \

101 DT\_IO\_CHANNELS\_CTLR\_BY\_IDX(DT\_DRV\_INST(inst), idx)

102

[ 112](group__devicetree-io-channels.md#gacd4b12a7698d44b56673e66643c2f88f)#define DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_NAME(inst, name) \

113 DT\_IO\_CHANNELS\_CTLR\_BY\_NAME(DT\_DRV\_INST(inst), name)

114

[ 122](group__devicetree-io-channels.md#gaf25c454ac2cf285b3efa2e9a4251dd0e)#define DT\_INST\_IO\_CHANNELS\_CTLR(inst) DT\_INST\_IO\_CHANNELS\_CTLR\_BY\_IDX(inst, 0)

123

[ 161](group__devicetree-io-channels.md#ga290c912d0a96ba65bb44341a783fac19)#define DT\_IO\_CHANNELS\_INPUT\_BY\_IDX(node\_id, idx) \

162 DT\_PHA\_BY\_IDX(node\_id, io\_channels, idx, input)

163

[ 203](group__devicetree-io-channels.md#ga6870a8215f61f87c3cb8f137a7bbbcc3)#define DT\_IO\_CHANNELS\_INPUT\_BY\_NAME(node\_id, name) \

204 DT\_PHA\_BY\_NAME(node\_id, io\_channels, name, input)

205

[ 211](group__devicetree-io-channels.md#gadcb598f00280ae1fa488e7982971e7d6)#define DT\_IO\_CHANNELS\_INPUT(node\_id) DT\_IO\_CHANNELS\_INPUT\_BY\_IDX(node\_id, 0)

212

[ 221](group__devicetree-io-channels.md#gac396f180ab5b24bdca01c021447a0211)#define DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_IDX(inst, idx) \

222 DT\_IO\_CHANNELS\_INPUT\_BY\_IDX(DT\_DRV\_INST(inst), idx)

223

[ 233](group__devicetree-io-channels.md#ga09cbce4296bd4982d2ed1e5cea45da5e)#define DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_NAME(inst, name) \

234 DT\_IO\_CHANNELS\_INPUT\_BY\_NAME(DT\_DRV\_INST(inst), name)

235

[ 241](group__devicetree-io-channels.md#ga736d38a4e3a3a5e2e294e50df805c320)#define DT\_INST\_IO\_CHANNELS\_INPUT(inst) DT\_INST\_IO\_CHANNELS\_INPUT\_BY\_IDX(inst, 0)

242

246

247#ifdef \_\_cplusplus

248}

249#endif

250

251#endif /\* ZEPHYR\_INCLUDE\_DEVICETREE\_IO\_CHANNELS\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [io-channels.h](io-channels_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
