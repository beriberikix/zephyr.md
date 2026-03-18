---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/dac_8h.html
original_path: doxygen/html/dac_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dac.h File Reference

DAC public API header file.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <syscalls/dac.h>`

[Go to the source code of this file.](dac_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [dac\_channel\_cfg](structdac__channel__cfg.md) |
|  | Structure for specifying the configuration of a DAC channel. [More...](structdac__channel__cfg.md#details) |

| Functions | |
| --- | --- |
| int | [dac\_channel\_setup](group__dac__interface.md#gab8be77003ba8fd7225c0808f95602a56) (const struct [device](structdevice.md) \*dev, const struct [dac\_channel\_cfg](structdac__channel__cfg.md) \*channel\_cfg) |
|  | Configure a DAC channel. |
| int | [dac\_write\_value](group__dac__interface.md#ga437a6f6b2402cf2e2a2a689429663b4e) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | Write a single value to a DAC channel. |

## Detailed Description

DAC public API header file.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [dac.h](dac_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
