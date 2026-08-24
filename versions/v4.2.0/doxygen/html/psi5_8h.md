---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/psi5_8h.html
original_path: doxygen/html/psi5_8h.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

psi5.h File Reference

Peripheral Sensor Interface (PSI5) driver API.
[More...](#details)

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <zephyr/syscalls/psi5.h>`

[Go to the source code of this file.](psi5_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [psi5\_frame](structpsi5__frame.md) |
|  | PSI5 frame structure. [More...](structpsi5__frame.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [psi5\_tx\_callback\_t](group__psi5__interface.md#gaac8c99036369b14d639cfb82f3b9cd32)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, int status, void \*user\_data) |
|  | Defines the application callback handler function signature for sending. |
| typedef void(\* | [psi5\_rx\_frame\_callback\_t](group__psi5__interface.md#ga5f43079d704d882ae014c7a15bde6406)) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_frame, void \*user\_data) |
|  | Defines the application callback handler function signature for receiving frame. |

| Enumerations | |
| --- | --- |
| enum | [psi5\_frame\_type](group__psi5__interface.md#ga5cb0ef3be35e9ff2d05c39cc17f2659f) { [PSI5\_SERIAL\_FRAME\_4\_BIT\_ID](group__psi5__interface.md#gga5cb0ef3be35e9ff2d05c39cc17f2659fa456be16421eb918370e6e50c8367d3ff) , [PSI5\_SERIAL\_FRAME\_8\_BIT\_ID](group__psi5__interface.md#gga5cb0ef3be35e9ff2d05c39cc17f2659fad1bbb5de03efb0be1075766a396d009a) , [PSI5\_DATA\_FRAME](group__psi5__interface.md#gga5cb0ef3be35e9ff2d05c39cc17f2659fa8d7f6f8699ded09880c3febd44375c8f) } |
|  | PSI5 frame type. [More...](group__psi5__interface.md#ga5cb0ef3be35e9ff2d05c39cc17f2659f) |

| Functions | |
| --- | --- |
| int | [psi5\_start\_sync](group__psi5__interface.md#gabbc2a744edf1ab01e7bd9321054cf32b) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel) |
|  | Start the sync pulse generator on a specific channel. |
| int | [psi5\_stop\_sync](group__psi5__interface.md#gacebce085be1e554e3faa7b69fd8da61f) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel) |
|  | Stop the sync pulse generator on a specific channel. |
| int | [psi5\_send](group__psi5__interface.md#ga3a27606e2828206608a79ada7238466d) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, const [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) data, [k\_timeout\_t](structk__timeout__t.md) timeout, [psi5\_tx\_callback\_t](group__psi5__interface.md#gaac8c99036369b14d639cfb82f3b9cd32) callback, void \*user\_data) |
|  | Transmitting PSI5 data on a specific channel. |
| int | [psi5\_register\_callback](group__psi5__interface.md#ga37b0fcdecd4629c5f2657b1cc2e227b4) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, struct psi5\_rx\_callback\_configs callback\_configs) |
|  | Add a callback function to handle messages received for a specific channel. |

## Detailed Description

Peripheral Sensor Interface (PSI5) driver API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [psi5](dir_30659d2cb58c9650599fdf2ac54f2854.md)
- [psi5.h](psi5_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
