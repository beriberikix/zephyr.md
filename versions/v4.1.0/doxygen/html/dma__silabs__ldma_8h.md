---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dma__silabs__ldma_8h.html
original_path: doxygen/html/dma__silabs__ldma_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dma\_silabs\_ldma.h File Reference

`#include <[zephyr/drivers/dma.h](drivers_2dma_8h_source.md)>`

[Go to the source code of this file.](dma__silabs__ldma_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SILABS\_LDMA\_SOURCE\_MASK](#a0d4985670c10482d3999d08e4ba1fdc9)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(21, 16) |
| #define | [SILABS\_LDMA\_SIG\_MASK](#a9559b6338f281c62c4cc28a37c6eaa1b)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 0) |
| #define | [SILABS\_DMA\_SLOT\_SOURCE\_MASK](#a8b234dbc8be91a1c9ae4b6478a3ba0e9)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 3) |
| #define | [SILABS\_DMA\_SLOT\_SIG\_MASK](#a9ccf7fd9a6101b88a45feaf1170de7d5)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(2, 0) |
| #define | [SILABS\_LDMA\_REQSEL\_TO\_SLOT](#a46d84aa830d58ab1e63133e3424361fb)([signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)) |
| #define | [SILABS\_LDMA\_SLOT\_TO\_REQSEL](#a8728e84cf05e093c864fe9dc8e9854c4)(slot) |

| Functions | |
| --- | --- |
| int | [silabs\_ldma\_append\_block](#a5f6501ec9e73cb8a3be76c418ebf1456) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) channel, struct [dma\_config](structdma__config.md) \*config) |
|  | Append a new block to the current channel. |

## Macro Definition Documentation

## [◆ ](#a9ccf7fd9a6101b88a45feaf1170de7d5)SILABS\_DMA\_SLOT\_SIG\_MASK

| #define SILABS\_DMA\_SLOT\_SIG\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(2, 0) |
| --- |

## [◆ ](#a8b234dbc8be91a1c9ae4b6478a3ba0e9)SILABS\_DMA\_SLOT\_SOURCE\_MASK

| #define SILABS\_DMA\_SLOT\_SOURCE\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 3) |
| --- |

## [◆ ](#a46d84aa830d58ab1e63133e3424361fb)SILABS\_LDMA\_REQSEL\_TO\_SLOT

| #define SILABS\_LDMA\_REQSEL\_TO\_SLOT | ( |  | *[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([SILABS\_DMA\_SLOT\_SOURCE\_MASK](#a8b234dbc8be91a1c9ae4b6478a3ba0e9), [FIELD\_GET](silabs-pinctrl-siwx91x_8h.md#aa49a456f06f7bdbedfcf3517e461947e)([SILABS\_LDMA\_SOURCE\_MASK](#a0d4985670c10482d3999d08e4ba1fdc9), [signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69))) | \

FIELD\_PREP([SILABS\_DMA\_SLOT\_SIG\_MASK](#a9ccf7fd9a6101b88a45feaf1170de7d5), [FIELD\_GET](silabs-pinctrl-siwx91x_8h.md#aa49a456f06f7bdbedfcf3517e461947e)([SILABS\_LDMA\_SIG\_MASK](#a9559b6338f281c62c4cc28a37c6eaa1b), [signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)))

[SILABS\_LDMA\_SOURCE\_MASK](#a0d4985670c10482d3999d08e4ba1fdc9)

#define SILABS\_LDMA\_SOURCE\_MASK

**Definition** dma\_silabs\_ldma.h:12

[SILABS\_DMA\_SLOT\_SOURCE\_MASK](#a8b234dbc8be91a1c9ae4b6478a3ba0e9)

#define SILABS\_DMA\_SLOT\_SOURCE\_MASK

**Definition** dma\_silabs\_ldma.h:15

[SILABS\_LDMA\_SIG\_MASK](#a9559b6338f281c62c4cc28a37c6eaa1b)

#define SILABS\_LDMA\_SIG\_MASK

**Definition** dma\_silabs\_ldma.h:13

[SILABS\_DMA\_SLOT\_SIG\_MASK](#a9ccf7fd9a6101b88a45feaf1170de7d5)

#define SILABS\_DMA\_SLOT\_SIG\_MASK

**Definition** dma\_silabs\_ldma.h:16

[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)

sighandler\_t signal(int signo, sighandler\_t handler)

[FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)

#define FIELD\_PREP(mask, value)

**Definition** silabs-pinctrl-siwx91x.h:15

[FIELD\_GET](silabs-pinctrl-siwx91x_8h.md#aa49a456f06f7bdbedfcf3517e461947e)

#define FIELD\_GET(mask, value)

**Definition** silabs-pinctrl-siwx91x.h:14

## [◆ ](#a9559b6338f281c62c4cc28a37c6eaa1b)SILABS\_LDMA\_SIG\_MASK

| #define SILABS\_LDMA\_SIG\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(3, 0) |
| --- |

## [◆ ](#a8728e84cf05e093c864fe9dc8e9854c4)SILABS\_LDMA\_SLOT\_TO\_REQSEL

| #define SILABS\_LDMA\_SLOT\_TO\_REQSEL | ( |  | *slot* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[FIELD\_PREP](silabs-pinctrl-siwx91x_8h.md#aa03c8b31bf67a097dd9f8153a04ef86b)([SILABS\_LDMA\_SOURCE\_MASK](#a0d4985670c10482d3999d08e4ba1fdc9), [FIELD\_GET](silabs-pinctrl-siwx91x_8h.md#aa49a456f06f7bdbedfcf3517e461947e)([SILABS\_DMA\_SLOT\_SOURCE\_MASK](#a8b234dbc8be91a1c9ae4b6478a3ba0e9), slot)) | \

FIELD\_PREP([SILABS\_LDMA\_SIG\_MASK](#a9559b6338f281c62c4cc28a37c6eaa1b), [FIELD\_GET](silabs-pinctrl-siwx91x_8h.md#aa49a456f06f7bdbedfcf3517e461947e)([SILABS\_DMA\_SLOT\_SIG\_MASK](#a9ccf7fd9a6101b88a45feaf1170de7d5), slot))

## [◆ ](#a0d4985670c10482d3999d08e4ba1fdc9)SILABS\_LDMA\_SOURCE\_MASK

| #define SILABS\_LDMA\_SOURCE\_MASK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(21, 16) |
| --- |

## Function Documentation

## [◆ ](#a5f6501ec9e73cb8a3be76c418ebf1456)silabs\_ldma\_append\_block()

| int silabs\_ldma\_append\_block | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *channel*, |
|  |  | struct [dma\_config](structdma__config.md) \* | *config* ) |

Append a new block to the current channel.

This function allows to append a block to the current DMA transfer. It allows a user/driver to register the next DMA transfer while a transfer in being held without stopping or restarting DMA engine. It is very suitable for Zephyr Uart API where user gives buffers while the DMA engine is running. Because this function changes dynamically the link to the block that DMA engine would load as the next transfer, it is only working with channel that didn't have linked block list.

In the case that the DMA engine naturally stopped because the previous transfer is finished, this function simply restart the DMA engine with the given block. If the DMA engine stopped while reconfiguring the next transfer, the DMA engine will restart too.

Parameters
:   | dev | dma device |
    | --- | --- |
    | channel | channel |
    | config | configuration of the channel with the block to append as the head\_block. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dma](dir_0dbbf0f7c33b88bff3996b0543cef0a8.md)
- [dma\_silabs\_ldma.h](dma__silabs__ldma_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
