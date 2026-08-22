---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/renesas__rz__dma_8h.html
original_path: doxygen/html/renesas__rz__dma_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

renesas\_rz\_dma.h File Reference

[Go to the source code of this file.](renesas__rz__dma_8h_source.md)

| Macros | |
| --- | --- |
| #define | [RZ\_DMA\_MODE\_NORMAL](#a2b81e575b015aab7551dd910d5c8204d)   (0U) |
| #define | [RZ\_DMA\_MODE\_BLOCK](#a3dc76a9c51aa176eecf2fb0a7c58ce05)   (1U) |
| #define | [RZ\_DMA\_CFG\_SRC\_DATA\_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)(val) |
| #define | [RZ\_DMA\_SRC\_1\_BYTE](#ad2630f88edccd524379229c6d08c3d6f)   [RZ\_DMA\_CFG\_SRC\_DATA\_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)(0) |
| #define | [RZ\_DMA\_SRC\_2\_BYTE](#a06c39443f03c6bf1f4a10a46492a4fcf)   [RZ\_DMA\_CFG\_SRC\_DATA\_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)(1) |
| #define | [RZ\_DMA\_SRC\_4\_BYTE](#a4bd983230d98d2a4bd98942f3b433765)   [RZ\_DMA\_CFG\_SRC\_DATA\_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)(2) |
| #define | [RZ\_DMA\_SRC\_8\_BYTE](#aadd165c44a5d9ec2d221f4de0fff99da)   [RZ\_DMA\_CFG\_SRC\_DATA\_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)(3) |
| #define | [RZ\_DMA\_SRC\_16\_BYTE](#a491d97dc4a9005cbf668fed70fe61292)   [RZ\_DMA\_CFG\_SRC\_DATA\_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)(4) |
| #define | [RZ\_DMA\_SRC\_32\_BYTE](#a05c3af12ddbc5abc07a635ee3dc184d8)   [RZ\_DMA\_CFG\_SRC\_DATA\_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)(5) |
| #define | [RZ\_DMA\_SRC\_64\_BYTE](#a47c957c6ddbf73e702d3cc406396d598)   [RZ\_DMA\_CFG\_SRC\_DATA\_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)(6) |
| #define | [RZ\_DMA\_SRC\_128\_BYTE](#afbebd4bc7e8faafa874532416b9f5977)   [RZ\_DMA\_CFG\_SRC\_DATA\_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)(7) |
| #define | [RZ\_DMA\_CFG\_DEST\_DATA\_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)(val) |
| #define | [RZ\_DMA\_DEST\_1\_BYTE](#a34bf5afed49353a0ecdff99cff12bd95)   [RZ\_DMA\_CFG\_DEST\_DATA\_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)(0) |
| #define | [RZ\_DMA\_DEST\_2\_BYTE](#a16018c672b1ff17d2065617e1145ce85)   [RZ\_DMA\_CFG\_DEST\_DATA\_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)(1) |
| #define | [RZ\_DMA\_DEST\_4\_BYTE](#ad5063a15c1612bbba264227a40b91d87)   [RZ\_DMA\_CFG\_DEST\_DATA\_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)(2) |
| #define | [RZ\_DMA\_DEST\_8\_BYTE](#a8a02c00f90f4532b44a2c2ff7f1be3ab)   [RZ\_DMA\_CFG\_DEST\_DATA\_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)(3) |
| #define | [RZ\_DMA\_DEST\_16\_BYTE](#acd01a438d73deaf6fe76b06c44593394)   [RZ\_DMA\_CFG\_DEST\_DATA\_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)(4) |
| #define | [RZ\_DMA\_DEST\_32\_BYTE](#a47929d19f83967834a22b2a5bef7dde1)   [RZ\_DMA\_CFG\_DEST\_DATA\_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)(5) |
| #define | [RZ\_DMA\_DEST\_64\_BYTE](#a1a95a59ace78fbfadbfdb113975ee361)   [RZ\_DMA\_CFG\_DEST\_DATA\_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)(6) |
| #define | [RZ\_DMA\_DEST\_128\_BYTE](#aa415a830c4e71f1c59869f1d1935a752)   [RZ\_DMA\_CFG\_DEST\_DATA\_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)(7) |
| #define | [RZ\_DMA\_CFG\_SRC\_ADDR\_MODE](#a41b9387b512f2d26315db92a55b331bc)(val) |
| #define | [RZ\_DMA\_SRC\_INCREMENTED](#a272bea303fa2484c83a197831b17ea75)   [RZ\_DMA\_CFG\_SRC\_ADDR\_MODE](#a41b9387b512f2d26315db92a55b331bc)(0) |
| #define | [RZ\_DMA\_SRC\_FIXED](#a0e47b6a3c30b6157d99d397641c672c1)   [RZ\_DMA\_CFG\_SRC\_ADDR\_MODE](#a41b9387b512f2d26315db92a55b331bc)(1) |
| #define | [RZ\_DMA\_CFG\_DEST\_ADDR\_MODE](#a35c2cf645fd17892b06760e79e7799e0)(val) |
| #define | [RZ\_DMA\_DEST\_INCREMENTED](#a4d3de22701e71b2bb3dabcf63f04c35f)   [RZ\_DMA\_CFG\_DEST\_ADDR\_MODE](#a35c2cf645fd17892b06760e79e7799e0)(0) |
| #define | [RZ\_DMA\_DEST\_FIXED](#a5cb1d2cbda322e0524c3317fe830dd2e)   [RZ\_DMA\_CFG\_DEST\_ADDR\_MODE](#a35c2cf645fd17892b06760e79e7799e0)(1) |
| #define | [RZ\_DMA\_MEM\_TO\_PERIPH](#a752b0f622d69a7eb8bffae025208f684) |
| #define | [RZ\_DMA\_PERIPH\_TO\_MEM](#a11c53b4c6de9c71d7b443ef02c2b9384) |

## Macro Definition Documentation

## [◆ ](#a35c2cf645fd17892b06760e79e7799e0)RZ\_DMA\_CFG\_DEST\_ADDR\_MODE

| #define RZ\_DMA\_CFG\_DEST\_ADDR\_MODE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((val & 0x1) << 8)

## [◆ ](#aee9e5ee0e341869584ffcd22bec9d684)RZ\_DMA\_CFG\_DEST\_DATA\_SIZE

| #define RZ\_DMA\_CFG\_DEST\_DATA\_SIZE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((val & 0x7) << 4)

## [◆ ](#a41b9387b512f2d26315db92a55b331bc)RZ\_DMA\_CFG\_SRC\_ADDR\_MODE

| #define RZ\_DMA\_CFG\_SRC\_ADDR\_MODE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((val & 0x1) << 7)

## [◆ ](#a5a925aec5cb8d0e787c00e3bf28adabb)RZ\_DMA\_CFG\_SRC\_DATA\_SIZE

| #define RZ\_DMA\_CFG\_SRC\_DATA\_SIZE | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((val & 0x7) << 1)

## [◆ ](#aa415a830c4e71f1c59869f1d1935a752)RZ\_DMA\_DEST\_128\_BYTE

| #define RZ\_DMA\_DEST\_128\_BYTE   [RZ\_DMA\_CFG\_DEST\_DATA\_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)(7) |
| --- |

## [◆ ](#acd01a438d73deaf6fe76b06c44593394)RZ\_DMA\_DEST\_16\_BYTE

| #define RZ\_DMA\_DEST\_16\_BYTE   [RZ\_DMA\_CFG\_DEST\_DATA\_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)(4) |
| --- |

## [◆ ](#a34bf5afed49353a0ecdff99cff12bd95)RZ\_DMA\_DEST\_1\_BYTE

| #define RZ\_DMA\_DEST\_1\_BYTE   [RZ\_DMA\_CFG\_DEST\_DATA\_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)(0) |
| --- |

## [◆ ](#a16018c672b1ff17d2065617e1145ce85)RZ\_DMA\_DEST\_2\_BYTE

| #define RZ\_DMA\_DEST\_2\_BYTE   [RZ\_DMA\_CFG\_DEST\_DATA\_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)(1) |
| --- |

## [◆ ](#a47929d19f83967834a22b2a5bef7dde1)RZ\_DMA\_DEST\_32\_BYTE

| #define RZ\_DMA\_DEST\_32\_BYTE   [RZ\_DMA\_CFG\_DEST\_DATA\_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)(5) |
| --- |

## [◆ ](#ad5063a15c1612bbba264227a40b91d87)RZ\_DMA\_DEST\_4\_BYTE

| #define RZ\_DMA\_DEST\_4\_BYTE   [RZ\_DMA\_CFG\_DEST\_DATA\_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)(2) |
| --- |

## [◆ ](#a1a95a59ace78fbfadbfdb113975ee361)RZ\_DMA\_DEST\_64\_BYTE

| #define RZ\_DMA\_DEST\_64\_BYTE   [RZ\_DMA\_CFG\_DEST\_DATA\_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)(6) |
| --- |

## [◆ ](#a8a02c00f90f4532b44a2c2ff7f1be3ab)RZ\_DMA\_DEST\_8\_BYTE

| #define RZ\_DMA\_DEST\_8\_BYTE   [RZ\_DMA\_CFG\_DEST\_DATA\_SIZE](#aee9e5ee0e341869584ffcd22bec9d684)(3) |
| --- |

## [◆ ](#a5cb1d2cbda322e0524c3317fe830dd2e)RZ\_DMA\_DEST\_FIXED

| #define RZ\_DMA\_DEST\_FIXED   [RZ\_DMA\_CFG\_DEST\_ADDR\_MODE](#a35c2cf645fd17892b06760e79e7799e0)(1) |
| --- |

## [◆ ](#a4d3de22701e71b2bb3dabcf63f04c35f)RZ\_DMA\_DEST\_INCREMENTED

| #define RZ\_DMA\_DEST\_INCREMENTED   [RZ\_DMA\_CFG\_DEST\_ADDR\_MODE](#a35c2cf645fd17892b06760e79e7799e0)(0) |
| --- |

## [◆ ](#a752b0f622d69a7eb8bffae025208f684)RZ\_DMA\_MEM\_TO\_PERIPH

| #define RZ\_DMA\_MEM\_TO\_PERIPH |
| --- |

**Value:**

([RZ\_DMA\_MODE\_NORMAL](#a2b81e575b015aab7551dd910d5c8204d) | [RZ\_DMA\_SRC\_INCREMENTED](#a272bea303fa2484c83a197831b17ea75) | [RZ\_DMA\_DEST\_FIXED](#a5cb1d2cbda322e0524c3317fe830dd2e) | [RZ\_DMA\_SRC\_1\_BYTE](#ad2630f88edccd524379229c6d08c3d6f) | \

[RZ\_DMA\_DEST\_1\_BYTE](#a34bf5afed49353a0ecdff99cff12bd95))

[RZ\_DMA\_SRC\_INCREMENTED](#a272bea303fa2484c83a197831b17ea75)

#define RZ\_DMA\_SRC\_INCREMENTED

**Definition** renesas\_rz\_dma.h:42

[RZ\_DMA\_MODE\_NORMAL](#a2b81e575b015aab7551dd910d5c8204d)

#define RZ\_DMA\_MODE\_NORMAL

**Definition** renesas\_rz\_dma.h:15

[RZ\_DMA\_DEST\_1\_BYTE](#a34bf5afed49353a0ecdff99cff12bd95)

#define RZ\_DMA\_DEST\_1\_BYTE

**Definition** renesas\_rz\_dma.h:31

[RZ\_DMA\_DEST\_FIXED](#a5cb1d2cbda322e0524c3317fe830dd2e)

#define RZ\_DMA\_DEST\_FIXED

**Definition** renesas\_rz\_dma.h:48

[RZ\_DMA\_SRC\_1\_BYTE](#ad2630f88edccd524379229c6d08c3d6f)

#define RZ\_DMA\_SRC\_1\_BYTE

**Definition** renesas\_rz\_dma.h:20

## [◆ ](#a3dc76a9c51aa176eecf2fb0a7c58ce05)RZ\_DMA\_MODE\_BLOCK

| #define RZ\_DMA\_MODE\_BLOCK   (1U) |
| --- |

## [◆ ](#a2b81e575b015aab7551dd910d5c8204d)RZ\_DMA\_MODE\_NORMAL

| #define RZ\_DMA\_MODE\_NORMAL   (0U) |
| --- |

## [◆ ](#a11c53b4c6de9c71d7b443ef02c2b9384)RZ\_DMA\_PERIPH\_TO\_MEM

| #define RZ\_DMA\_PERIPH\_TO\_MEM |
| --- |

**Value:**

([RZ\_DMA\_MODE\_NORMAL](#a2b81e575b015aab7551dd910d5c8204d) | [RZ\_DMA\_SRC\_FIXED](#a0e47b6a3c30b6157d99d397641c672c1) | [RZ\_DMA\_DEST\_INCREMENTED](#a4d3de22701e71b2bb3dabcf63f04c35f) | [RZ\_DMA\_SRC\_1\_BYTE](#ad2630f88edccd524379229c6d08c3d6f) | \

[RZ\_DMA\_DEST\_1\_BYTE](#a34bf5afed49353a0ecdff99cff12bd95))

[RZ\_DMA\_SRC\_FIXED](#a0e47b6a3c30b6157d99d397641c672c1)

#define RZ\_DMA\_SRC\_FIXED

**Definition** renesas\_rz\_dma.h:43

[RZ\_DMA\_DEST\_INCREMENTED](#a4d3de22701e71b2bb3dabcf63f04c35f)

#define RZ\_DMA\_DEST\_INCREMENTED

**Definition** renesas\_rz\_dma.h:47

## [◆ ](#afbebd4bc7e8faafa874532416b9f5977)RZ\_DMA\_SRC\_128\_BYTE

| #define RZ\_DMA\_SRC\_128\_BYTE   [RZ\_DMA\_CFG\_SRC\_DATA\_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)(7) |
| --- |

## [◆ ](#a491d97dc4a9005cbf668fed70fe61292)RZ\_DMA\_SRC\_16\_BYTE

| #define RZ\_DMA\_SRC\_16\_BYTE   [RZ\_DMA\_CFG\_SRC\_DATA\_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)(4) |
| --- |

## [◆ ](#ad2630f88edccd524379229c6d08c3d6f)RZ\_DMA\_SRC\_1\_BYTE

| #define RZ\_DMA\_SRC\_1\_BYTE   [RZ\_DMA\_CFG\_SRC\_DATA\_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)(0) |
| --- |

## [◆ ](#a06c39443f03c6bf1f4a10a46492a4fcf)RZ\_DMA\_SRC\_2\_BYTE

| #define RZ\_DMA\_SRC\_2\_BYTE   [RZ\_DMA\_CFG\_SRC\_DATA\_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)(1) |
| --- |

## [◆ ](#a05c3af12ddbc5abc07a635ee3dc184d8)RZ\_DMA\_SRC\_32\_BYTE

| #define RZ\_DMA\_SRC\_32\_BYTE   [RZ\_DMA\_CFG\_SRC\_DATA\_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)(5) |
| --- |

## [◆ ](#a4bd983230d98d2a4bd98942f3b433765)RZ\_DMA\_SRC\_4\_BYTE

| #define RZ\_DMA\_SRC\_4\_BYTE   [RZ\_DMA\_CFG\_SRC\_DATA\_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)(2) |
| --- |

## [◆ ](#a47c957c6ddbf73e702d3cc406396d598)RZ\_DMA\_SRC\_64\_BYTE

| #define RZ\_DMA\_SRC\_64\_BYTE   [RZ\_DMA\_CFG\_SRC\_DATA\_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)(6) |
| --- |

## [◆ ](#aadd165c44a5d9ec2d221f4de0fff99da)RZ\_DMA\_SRC\_8\_BYTE

| #define RZ\_DMA\_SRC\_8\_BYTE   [RZ\_DMA\_CFG\_SRC\_DATA\_SIZE](#a5a925aec5cb8d0e787c00e3bf28adabb)(3) |
| --- |

## [◆ ](#a0e47b6a3c30b6157d99d397641c672c1)RZ\_DMA\_SRC\_FIXED

| #define RZ\_DMA\_SRC\_FIXED   [RZ\_DMA\_CFG\_SRC\_ADDR\_MODE](#a41b9387b512f2d26315db92a55b331bc)(1) |
| --- |

## [◆ ](#a272bea303fa2484c83a197831b17ea75)RZ\_DMA\_SRC\_INCREMENTED

| #define RZ\_DMA\_SRC\_INCREMENTED   [RZ\_DMA\_CFG\_SRC\_ADDR\_MODE](#a41b9387b512f2d26315db92a55b331bc)(0) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [dma](dir_4af45c18fedc476f9a2ee26ec98f56f0.md)
- [renesas\_rz\_dma.h](renesas__rz__dma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
