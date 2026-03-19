---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2mipi__dsi_8h.html
original_path: doxygen/html/drivers_2mipi__dsi_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mipi\_dsi.h File Reference

Public APIs for MIPI-DSI drivers.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/display/mipi_display.h](mipi__display_8h_source.md)>`  
`#include <[zephyr/dt-bindings/mipi_dsi/mipi_dsi.h](dt-bindings_2mipi__dsi_2mipi__dsi_8h_source.md)>`

[Go to the source code of this file.](drivers_2mipi__dsi_8h_source.md)

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
| #define | [MIPI\_DSI\_MSG\_USE\_LPM](group__mipi__dsi__interface.md#gaaf7954dcd5644e3ff332f5fab8fe48ef)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0x0) |
| MIPI-DSI Device mode flags. | |
| #define | [MIPI\_DSI\_MODE\_VIDEO](group__mipi__dsi__interface.md#ga2b4ff0fda3d00061b06e576a98628e7b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Video mode. |
| #define | [MIPI\_DSI\_MODE\_VIDEO\_BURST](group__mipi__dsi__interface.md#gaabfe30e5981efc1a73f4f9bf2def1610)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Video burst mode. |
| #define | [MIPI\_DSI\_MODE\_VIDEO\_SYNC\_PULSE](group__mipi__dsi__interface.md#ga75709f3a91b803598d9d772f3c5b9eed)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Video pulse mode. |
| #define | [MIPI\_DSI\_MODE\_VIDEO\_AUTO\_VERT](group__mipi__dsi__interface.md#ga5871aadda35ece0944217053f5c6c6fe)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Enable auto vertical count mode. |
| #define | [MIPI\_DSI\_MODE\_VIDEO\_HSE](group__mipi__dsi__interface.md#ga21d9620a4986884bbe2ac3a11b311337)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Enable hsync-end packets in vsync-pulse and v-porch area. |
| #define | [MIPI\_DSI\_MODE\_VIDEO\_HFP](group__mipi__dsi__interface.md#ga625d1738ae1cfd25aef5772729c0aae8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Disable hfront-porch area. |
| #define | [MIPI\_DSI\_MODE\_VIDEO\_HBP](group__mipi__dsi__interface.md#ga90e09b889a1dbac1e2b7b9ae84f38ee4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Disable hback-porch area. |
| #define | [MIPI\_DSI\_MODE\_VIDEO\_HSA](group__mipi__dsi__interface.md#ga395bb9085f92a1927e3cc317196ab353)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Disable hsync-active area. |
| #define | [MIPI\_DSI\_MODE\_VSYNC\_FLUSH](group__mipi__dsi__interface.md#gacdc35d8e6726accc88c2e2e82c88d46d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
|  | Flush display FIFO on vsync pulse. |
| #define | [MIPI\_DSI\_MODE\_EOT\_PACKET](group__mipi__dsi__interface.md#ga4bbcabcb84af1a2bd715b0bd8be78db3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
|  | Disable EoT packets in HS mode. |
| #define | [MIPI\_DSI\_CLOCK\_NON\_CONTINUOUS](group__mipi__dsi__interface.md#ga75c0e183f1235e37245cf890aa4a656b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
|  | Device supports non-continuous clock behavior (DSI spec 5.6.1). |
| #define | [MIPI\_DSI\_MODE\_LPM](group__mipi__dsi__interface.md#ga1f8923811fc5d704e28362e72a1f1633)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
|  | Transmit data in low power. |

| Functions | |
| --- | --- |
| static int | [mipi\_dsi\_attach](group__mipi__dsi__interface.md#ga18689fac223fddc10b23b6bc6712944e) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, const struct [mipi\_dsi\_device](structmipi__dsi__device.md) \*mdev) |
|  | Attach a new device to the MIPI-DSI bus. |
| static [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [mipi\_dsi\_transfer](group__mipi__dsi__interface.md#gace5bb52f483634baa185f46ac61efb71) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, struct [mipi\_dsi\_msg](structmipi__dsi__msg.md) \*msg) |
|  | Transfer data to/from a device attached to the MIPI-DSI bus. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [mipi\_dsi\_generic\_read](group__mipi__dsi__interface.md#ga121633e8e379e7d1ebd749328f2014fd) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, const void \*params, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) nparams, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | MIPI-DSI generic read. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [mipi\_dsi\_generic\_write](group__mipi__dsi__interface.md#ga5442f45c7c827d1dd8c3fa21da49c560) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | MIPI-DSI generic write. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [mipi\_dsi\_dcs\_read](group__mipi__dsi__interface.md#ga7b5f52bcd51821bf120c5ac67b4c2fa5) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | MIPI-DSI DCS read. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [mipi\_dsi\_dcs\_write](group__mipi__dsi__interface.md#gad0f324e32191469bc0d24ba203286237) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | MIPI-DSI DCS write. |
| static int | [mipi\_dsi\_detach](group__mipi__dsi__interface.md#gace728ac82d30e15868298facd6df0228) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, const struct [mipi\_dsi\_device](structmipi__dsi__device.md) \*mdev) |
|  | Detach a device from the MIPI-DSI bus. |

## Detailed Description

Public APIs for MIPI-DSI drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mipi\_dsi.h](drivers_2mipi__dsi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
