---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__mipi__dsi__interface.html
original_path: doxygen/html/group__mipi__dsi__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MIPI-DSI driver APIs

[Device Driver APIs](group__io__interfaces.md)

MIPI-DSI driver APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [mipi\_dsi\_timings](structmipi__dsi__timings.md) |
|  | MIPI-DSI display timings. [More...](structmipi__dsi__timings.md#details) |
| struct | [mipi\_dsi\_device](structmipi__dsi__device.md) |
|  | MIPI-DSI device. [More...](structmipi__dsi__device.md#details) |
| struct | [mipi\_dsi\_msg](structmipi__dsi__msg.md) |
|  | MIPI-DSI read/write message. [More...](structmipi__dsi__msg.md#details) |
| struct | [mipi\_dsi\_driver\_api](structmipi__dsi__driver__api.md) |
|  | MIPI-DSI host driver API. [More...](structmipi__dsi__driver__api.md#details) |

| Macros | |
| --- | --- |
| #define | [MIPI\_DSI\_MSG\_USE\_LPM](#gaaf7954dcd5644e3ff332f5fab8fe48ef)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0x0) |

| Functions | |
| --- | --- |
| static int | [mipi\_dsi\_attach](#ga18689fac223fddc10b23b6bc6712944e) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, const struct [mipi\_dsi\_device](structmipi__dsi__device.md) \*mdev) |
|  | Attach a new device to the MIPI-DSI bus. |
| static [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [mipi\_dsi\_transfer](#gace5bb52f483634baa185f46ac61efb71) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, struct [mipi\_dsi\_msg](structmipi__dsi__msg.md) \*msg) |
|  | Transfer data to/from a device attached to the MIPI-DSI bus. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [mipi\_dsi\_generic\_read](#ga121633e8e379e7d1ebd749328f2014fd) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, const void \*params, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) nparams, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | MIPI-DSI generic read. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [mipi\_dsi\_generic\_write](#ga5442f45c7c827d1dd8c3fa21da49c560) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | MIPI-DSI generic write. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [mipi\_dsi\_dcs\_read](#ga7b5f52bcd51821bf120c5ac67b4c2fa5) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | MIPI-DSI DCS read. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [mipi\_dsi\_dcs\_write](#gad0f324e32191469bc0d24ba203286237) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | MIPI-DSI DCS write. |
| static int | [mipi\_dsi\_detach](#gace728ac82d30e15868298facd6df0228) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, const struct [mipi\_dsi\_device](structmipi__dsi__device.md) \*mdev) |
|  | Detach a device from the MIPI-DSI bus. |

| MIPI-DSI Device mode flags. | |
| --- | --- |
| #define | [MIPI\_DSI\_MODE\_VIDEO](#ga2b4ff0fda3d00061b06e576a98628e7b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Video mode. |
| #define | [MIPI\_DSI\_MODE\_VIDEO\_BURST](#gaabfe30e5981efc1a73f4f9bf2def1610)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Video burst mode. |
| #define | [MIPI\_DSI\_MODE\_VIDEO\_SYNC\_PULSE](#ga75709f3a91b803598d9d772f3c5b9eed)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Video pulse mode. |
| #define | [MIPI\_DSI\_MODE\_VIDEO\_AUTO\_VERT](#ga5871aadda35ece0944217053f5c6c6fe)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Enable auto vertical count mode. |
| #define | [MIPI\_DSI\_MODE\_VIDEO\_HSE](#ga21d9620a4986884bbe2ac3a11b311337)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Enable hsync-end packets in vsync-pulse and v-porch area. |
| #define | [MIPI\_DSI\_MODE\_VIDEO\_HFP](#ga625d1738ae1cfd25aef5772729c0aae8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Disable hfront-porch area. |
| #define | [MIPI\_DSI\_MODE\_VIDEO\_HBP](#ga90e09b889a1dbac1e2b7b9ae84f38ee4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Disable hback-porch area. |
| #define | [MIPI\_DSI\_MODE\_VIDEO\_HSA](#ga395bb9085f92a1927e3cc317196ab353)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Disable hsync-active area. |
| #define | [MIPI\_DSI\_MODE\_VSYNC\_FLUSH](#gacdc35d8e6726accc88c2e2e82c88d46d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | Flush display FIFO on vsync pulse. |
| #define | [MIPI\_DSI\_MODE\_EOT\_PACKET](#ga4bbcabcb84af1a2bd715b0bd8be78db3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | Disable EoT packets in HS mode. |
| #define | [MIPI\_DSI\_CLOCK\_NON\_CONTINUOUS](#ga75c0e183f1235e37245cf890aa4a656b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | Device supports non-continuous clock behavior (DSI spec 5.6.1). |
| #define | [MIPI\_DSI\_MODE\_LPM](#ga1f8923811fc5d704e28362e72a1f1633)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
|  | Transmit data in low power. |

| MIPI-DSI Pixel formats. | |
| --- | --- |
| #define | [MIPI\_DSI\_PIXFMT\_RGB888](#gafb9cb05fbca552449bab635544517d25)   0U |
|  | RGB888 (24bpp). |
| #define | [MIPI\_DSI\_PIXFMT\_RGB666](#gad7288299bb5248e8fab55d07c310cd85)   1U |
|  | RGB666 (24bpp). |
| #define | [MIPI\_DSI\_PIXFMT\_RGB666\_PACKED](#gadad1c9a93585a16c643bc33ef280b38b)   2U |
|  | Packed RGB666 (18bpp). |
| #define | [MIPI\_DSI\_PIXFMT\_RGB565](#gab74cc16bec1613c5e1eff30de2aa25c6)   3U |
|  | RGB565 (16bpp). |

## Detailed Description

MIPI-DSI driver APIs.

Since
:   3.1

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga75c0e183f1235e37245cf890aa4a656b)MIPI\_DSI\_CLOCK\_NON\_CONTINUOUS

| #define MIPI\_DSI\_CLOCK\_NON\_CONTINUOUS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

Device supports non-continuous clock behavior (DSI spec 5.6.1).

## [◆ ](#ga4bbcabcb84af1a2bd715b0bd8be78db3)MIPI\_DSI\_MODE\_EOT\_PACKET

| #define MIPI\_DSI\_MODE\_EOT\_PACKET   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

Disable EoT packets in HS mode.

## [◆ ](#ga1f8923811fc5d704e28362e72a1f1633)MIPI\_DSI\_MODE\_LPM

| #define MIPI\_DSI\_MODE\_LPM   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

Transmit data in low power.

## [◆ ](#ga2b4ff0fda3d00061b06e576a98628e7b)MIPI\_DSI\_MODE\_VIDEO

| #define MIPI\_DSI\_MODE\_VIDEO   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

Video mode.

## [◆ ](#ga5871aadda35ece0944217053f5c6c6fe)MIPI\_DSI\_MODE\_VIDEO\_AUTO\_VERT

| #define MIPI\_DSI\_MODE\_VIDEO\_AUTO\_VERT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

Enable auto vertical count mode.

## [◆ ](#gaabfe30e5981efc1a73f4f9bf2def1610)MIPI\_DSI\_MODE\_VIDEO\_BURST

| #define MIPI\_DSI\_MODE\_VIDEO\_BURST   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

Video burst mode.

## [◆ ](#ga90e09b889a1dbac1e2b7b9ae84f38ee4)MIPI\_DSI\_MODE\_VIDEO\_HBP

| #define MIPI\_DSI\_MODE\_VIDEO\_HBP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

Disable hback-porch area.

## [◆ ](#ga625d1738ae1cfd25aef5772729c0aae8)MIPI\_DSI\_MODE\_VIDEO\_HFP

| #define MIPI\_DSI\_MODE\_VIDEO\_HFP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

Disable hfront-porch area.

## [◆ ](#ga395bb9085f92a1927e3cc317196ab353)MIPI\_DSI\_MODE\_VIDEO\_HSA

| #define MIPI\_DSI\_MODE\_VIDEO\_HSA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

Disable hsync-active area.

## [◆ ](#ga21d9620a4986884bbe2ac3a11b311337)MIPI\_DSI\_MODE\_VIDEO\_HSE

| #define MIPI\_DSI\_MODE\_VIDEO\_HSE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

Enable hsync-end packets in vsync-pulse and v-porch area.

## [◆ ](#ga75709f3a91b803598d9d772f3c5b9eed)MIPI\_DSI\_MODE\_VIDEO\_SYNC\_PULSE

| #define MIPI\_DSI\_MODE\_VIDEO\_SYNC\_PULSE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

Video pulse mode.

## [◆ ](#gacdc35d8e6726accc88c2e2e82c88d46d)MIPI\_DSI\_MODE\_VSYNC\_FLUSH

| #define MIPI\_DSI\_MODE\_VSYNC\_FLUSH   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

Flush display FIFO on vsync pulse.

## [◆ ](#gaaf7954dcd5644e3ff332f5fab8fe48ef)MIPI\_DSI\_MSG\_USE\_LPM

| #define MIPI\_DSI\_MSG\_USE\_LPM   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0x0) |
| --- |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

## [◆ ](#gab74cc16bec1613c5e1eff30de2aa25c6)MIPI\_DSI\_PIXFMT\_RGB565

| #define MIPI\_DSI\_PIXFMT\_RGB565   3U |
| --- |

`#include <[mipi_dsi.h](dt-bindings_2mipi__dsi_2mipi__dsi_8h.md)>`

RGB565 (16bpp).

## [◆ ](#gad7288299bb5248e8fab55d07c310cd85)MIPI\_DSI\_PIXFMT\_RGB666

| #define MIPI\_DSI\_PIXFMT\_RGB666   1U |
| --- |

`#include <[mipi_dsi.h](dt-bindings_2mipi__dsi_2mipi__dsi_8h.md)>`

RGB666 (24bpp).

## [◆ ](#gadad1c9a93585a16c643bc33ef280b38b)MIPI\_DSI\_PIXFMT\_RGB666\_PACKED

| #define MIPI\_DSI\_PIXFMT\_RGB666\_PACKED   2U |
| --- |

`#include <[mipi_dsi.h](dt-bindings_2mipi__dsi_2mipi__dsi_8h.md)>`

Packed RGB666 (18bpp).

## [◆ ](#gafb9cb05fbca552449bab635544517d25)MIPI\_DSI\_PIXFMT\_RGB888

| #define MIPI\_DSI\_PIXFMT\_RGB888   0U |
| --- |

`#include <[mipi_dsi.h](dt-bindings_2mipi__dsi_2mipi__dsi_8h.md)>`

RGB888 (24bpp).

## Function Documentation

## [◆ ](#ga18689fac223fddc10b23b6bc6712944e)mipi\_dsi\_attach()

| | int mipi\_dsi\_attach | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel*, | |  |  | const struct [mipi\_dsi\_device](structmipi__dsi__device.md) \* | *mdev* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

Attach a new device to the MIPI-DSI bus.

Parameters
:   | dev | MIPI-DSI host device. |
    | --- | --- |
    | channel | Device channel (VID). |
    | mdev | MIPI-DSI device description. |

Returns
:   0 on success, negative on error

## [◆ ](#ga7b5f52bcd51821bf120c5ac67b4c2fa5)mipi\_dsi\_dcs\_read()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) mipi\_dsi\_dcs\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cmd*, |
|  |  | void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

MIPI-DSI DCS read.

Parameters
:   | dev | MIPI-DSI host device. |
    | --- | --- |
    | channel | Device channel (VID). |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | DCS command. |
    | buf | Buffer where read data will be stored. |
    | len | Length of the reception buffer. |

Returns
:   Size of the read data on success, negative on error.

## [◆ ](#gad0f324e32191469bc0d24ba203286237)mipi\_dsi\_dcs\_write()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) mipi\_dsi\_dcs\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cmd*, |
|  |  | const void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

MIPI-DSI DCS write.

Parameters
:   | dev | MIPI-DSI host device. |
    | --- | --- |
    | channel | Device channel (VID). |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | DCS command. |
    | buf | Transmission buffer. |
    | len | Length of the transmission buffer |

Returns
:   Size of the written data on success, negative on error.

## [◆ ](#gace728ac82d30e15868298facd6df0228)mipi\_dsi\_detach()

| | int mipi\_dsi\_detach | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel*, | |  |  | const struct [mipi\_dsi\_device](structmipi__dsi__device.md) \* | *mdev* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

Detach a device from the MIPI-DSI bus.

Parameters
:   | dev | MIPI-DSI host device. |
    | --- | --- |
    | channel | Device channel (VID). |
    | mdev | MIPI-DSI device description. |

Returns
:   0 on success, negative on error

## [◆ ](#ga121633e8e379e7d1ebd749328f2014fd)mipi\_dsi\_generic\_read()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) mipi\_dsi\_generic\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel*, |
|  |  | const void \* | *params*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *nparams*, |
|  |  | void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

MIPI-DSI generic read.

Parameters
:   | dev | MIPI-DSI host device. |
    | --- | --- |
    | channel | Device channel (VID). |
    | params | Buffer containing request parameters. |
    | nparams | Number of parameters. |
    | buf | Buffer where read data will be stored. |
    | len | Length of the reception buffer. |

Returns
:   Size of the read data on success, negative on error.

## [◆ ](#ga5442f45c7c827d1dd8c3fa21da49c560)mipi\_dsi\_generic\_write()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) mipi\_dsi\_generic\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel*, |
|  |  | const void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

MIPI-DSI generic write.

Parameters
:   | dev | MIPI-DSI host device. |
    | --- | --- |
    | channel | Device channel (VID). |
    | buf | Transmission buffer. |
    | len | Length of the transmission buffer |

Returns
:   Size of the written data on success, negative on error.

## [◆ ](#gace5bb52f483634baa185f46ac61efb71)mipi\_dsi\_transfer()

| | [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) mipi\_dsi\_transfer | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel*, | |  |  | struct [mipi\_dsi\_msg](structmipi__dsi__msg.md) \* | *msg* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[mipi_dsi.h](drivers_2mipi__dsi_8h.md)>`

Transfer data to/from a device attached to the MIPI-DSI bus.

Parameters
:   | dev | MIPI-DSI device. |
    | --- | --- |
    | channel | Device channel (VID). |
    | msg | Message. |

Returns
:   Size of the transferred data on success, negative on error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
