---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/drivers_2sent_2sent_8h.html
original_path: doxygen/html/drivers_2sent_2sent_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sent.h File Reference

Single Edge Nibble Transmission (SENT) driver API.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <zephyr/syscalls/sent.h>`

[Go to the source code of this file.](drivers_2sent_2sent_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sent\_frame](structsent__frame.md) |
|  | SENT frame structure. [More...](structsent__frame.md#details) |

| Macros | |
| --- | --- |
| #define | [SENT\_MAX\_DATA\_NIBBLES](group__sent__interface.md#ga19bb6e9149dfb7af97ca90289e33bdac)   8 |
|  | Maximum number of data nibbles. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [sent\_rx\_frame\_callback\_t](group__sent__interface.md#ga47d05656177dae0a388e1155be82494f)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_frame, void \*user\_data) |
|  | Defines the application callback handler function signature for receiving frame. |

| Enumerations | |
| --- | --- |
| enum | [sent\_frame\_type](group__sent__interface.md#ga069232b79943be845df411539ef04993) { [SENT\_SHORT\_SERIAL\_FRAME](group__sent__interface.md#gga069232b79943be845df411539ef04993adbbb93e3efeeb6d2330bc4c9cb0ae4d5) , [SENT\_ENHANCED\_SERIAL\_FRAME\_4\_BIT\_ID](group__sent__interface.md#gga069232b79943be845df411539ef04993a44b400409bb8a00ba23022490a6e6e73) , [SENT\_ENHANCED\_SERIAL\_FRAME\_8\_BIT\_ID](group__sent__interface.md#gga069232b79943be845df411539ef04993aeef9ade678a8b59d7a8e0d0154f9b137) , [SENT\_FAST\_FRAME](group__sent__interface.md#gga069232b79943be845df411539ef04993afb15bcda86b0faef89c8dc1662f060a1) } |
|  | SENT frame type. [More...](group__sent__interface.md#ga069232b79943be845df411539ef04993) |

| Functions | |
| --- | --- |
| int | [sent\_start\_listening](group__sent__interface.md#ga227aafdbe8f93dbdb97f3969517e6c63) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel) |
|  | Enable a specific channel to start receiving from the bus. |
| int | [sent\_stop\_listening](group__sent__interface.md#gae1eacde97297c97e27b67a7ae7e121cb) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel) |
|  | Disable a specific channel to stop receiving from the bus. |
| int | [sent\_register\_callback](group__sent__interface.md#ga9deb810297f7d42159187bbb8dddb8d2) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, struct sent\_rx\_callback\_configs callback\_configs) |
|  | Add a callback function to handle messages received for a specific channel. |

## Detailed Description

Single Edge Nibble Transmission (SENT) driver API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sent](dir_c7c606dbfefe42cf24a6f31b226e5895.md)
- [sent.h](drivers_2sent_2sent_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
