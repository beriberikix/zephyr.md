---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/arc__dsp_8h_source.html
original_path: doxygen/html/arc__dsp_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arc\_dsp.h

[Go to the documentation of this file.](arc__dsp_8h.md)

1/\*

2 \* Copyright (c) 2022 Synopsys.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_DSP\_ARC\_DSP\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_DSP\_ARC\_DSP\_H\_

8

[ 22](arc__dsp_8h.md#a119f6c3700a75e14f3d49f38725b93d7)void [arc\_dsp\_disable](arc__dsp_8h.md#a119f6c3700a75e14f3d49f38725b93d7)(struct [k\_thread](structk__thread.md) \*thread, unsigned int options);

23

[ 37](arc__dsp_8h.md#a29fddbd6fdaad797481c6c4010e85046)void [arc\_dsp\_enable](arc__dsp_8h.md#a29fddbd6fdaad797481c6c4010e85046)(struct [k\_thread](structk__thread.md) \*thread, unsigned int options);

38

39#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARC\_V2\_DSP\_ARC\_DSP\_H\_ \*/

[arc\_dsp\_disable](arc__dsp_8h.md#a119f6c3700a75e14f3d49f38725b93d7)

void arc\_dsp\_disable(struct k\_thread \*thread, unsigned int options)

Disable dsp context preservation.

[arc\_dsp\_enable](arc__dsp_8h.md#a29fddbd6fdaad797481c6c4010e85046)

void arc\_dsp\_enable(struct k\_thread \*thread, unsigned int options)

Enable dsp context preservation.

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [dsp](dir_962e9c2a9ba605ed4f0852828f7b1083.md)
- [arc\_dsp.h](arc__dsp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
