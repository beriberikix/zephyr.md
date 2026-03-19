---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/port-endpoint_8h_source.html
original_path: doxygen/html/port-endpoint_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

port-endpoint.h

[Go to the documentation of this file.](port-endpoint_8h.md)

1

5

6/\*

7 \* Copyright 2024 NXP

8 \* Copyright (c) 2024 tinyVision.ai Inc

9 \*

10 \* SPDX-License-Identifier: Apache-2.0

11 \*/

12

13#ifndef ZEPHYR\_INCLUDE\_DEVICETREE\_PORT\_ENDPOINT\_H\_

14#define ZEPHYR\_INCLUDE\_DEVICETREE\_PORT\_ENDPOINT\_H\_

15

16#ifdef \_\_cplusplus

17extern "C" {

18#endif

19

25

36#define \_DT\_INST\_PORT\_BY\_ID(inst, pid) \

37 COND\_CODE\_1(DT\_NODE\_EXISTS(DT\_INST\_CHILD(inst, ports)), \

38 (DT\_CHILD(DT\_INST\_CHILD(inst, ports), port\_##pid)), (DT\_INST\_CHILD(inst, port\_##pid)))

39

[ 87](group__devicetree-port-endpoint.md#gaf3427020d7d560c5da3df0f553988f71)#define DT\_INST\_PORT\_BY\_ID(inst, pid) \

88 COND\_CODE\_1(DT\_NODE\_EXISTS(\_DT\_INST\_PORT\_BY\_ID(inst, pid)), \

89 (\_DT\_INST\_PORT\_BY\_ID(inst, pid)), (DT\_INST\_CHILD(inst, port)))

90

102#define \_DT\_INST\_ENDPOINT\_BY\_ID(inst, pid, eid) \

103 DT\_CHILD(DT\_INST\_PORT\_BY\_ID(inst, pid), endpoint\_##eid)

104

[ 163](group__devicetree-port-endpoint.md#ga0d2315ddc63c986da0e90177e8d8eab8)#define DT\_INST\_ENDPOINT\_BY\_ID(inst, pid, eid) \

164 COND\_CODE\_1(DT\_NODE\_EXISTS(\_DT\_INST\_ENDPOINT\_BY\_ID(inst, pid, eid)), \

165 (\_DT\_INST\_ENDPOINT\_BY\_ID(inst, pid, eid)), \

166 (DT\_CHILD(DT\_INST\_PORT\_BY\_ID(inst, pid), endpoint)))

167

[ 215](group__devicetree-port-endpoint.md#ga37c2b0183196f513fc2222ba5fbe30d7)#define DT\_NODE\_BY\_ENDPOINT(ep) \

216 COND\_CODE\_1(DT\_NODE\_EXISTS(DT\_CHILD(DT\_PARENT(DT\_GPARENT(ep)), ports)), \

217 (DT\_PARENT(DT\_GPARENT(ep))), (DT\_GPARENT(ep)))

218

[ 264](group__devicetree-port-endpoint.md#gaf1261a1a110fc0b164e6eafbaf885f7d)#define DT\_NODE\_REMOTE\_DEVICE(ep) \

265 DT\_NODE\_BY\_ENDPOINT(DT\_NODELABEL(DT\_STRING\_TOKEN(ep, remote\_endpoint\_label)))

266

270

271#ifdef \_\_cplusplus

272}

273#endif

274

275#endif /\* ZEPHYR\_INCLUDE\_DEVICETREE\_PORT\_ENDPOINT\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree](dir_f553ff8da1901e62a497da976ecba1fe.md)
- [port-endpoint.h](port-endpoint_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
