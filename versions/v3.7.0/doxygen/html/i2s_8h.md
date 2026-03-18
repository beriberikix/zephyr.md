---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/i2s_8h.html
original_path: doxygen/html/i2s_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

i2s.h File Reference

Public APIs for the I2S (Inter-IC Sound) bus drivers.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <zephyr/syscalls/i2s.h>`

[Go to the source code of this file.](i2s_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [i2s\_config](structi2s__config.md) |
|  | Interface configuration options. [More...](structi2s__config.md#details) |

| Macros | |
| --- | --- |
| #define | [I2S\_FMT\_DATA\_FORMAT\_SHIFT](group__i2s__interface.md#gaa3f67c47874141782fbb7ec5a671b566)   0 |
|  | Data Format bit field position. |
| #define | [I2S\_FMT\_DATA\_FORMAT\_MASK](group__i2s__interface.md#gaf3eb0116133dd3a041d9a80cb3397263)   (0x7 << [I2S\_FMT\_DATA\_FORMAT\_SHIFT](group__i2s__interface.md#gaa3f67c47874141782fbb7ec5a671b566)) |
|  | Data Format bit field mask. |
| #define | [I2S\_FMT\_DATA\_FORMAT\_I2S](group__i2s__interface.md#gaa1adc5e3b722e89f20f258b0fd53a2c5)   (0 << [I2S\_FMT\_DATA\_FORMAT\_SHIFT](group__i2s__interface.md#gaa3f67c47874141782fbb7ec5a671b566)) |
|  | Standard I2S Data Format. |
| #define | [I2S\_FMT\_DATA\_FORMAT\_PCM\_SHORT](group__i2s__interface.md#ga70c7a19078a6f72e078b9c0488018b11)   (1 << [I2S\_FMT\_DATA\_FORMAT\_SHIFT](group__i2s__interface.md#gaa3f67c47874141782fbb7ec5a671b566)) |
|  | PCM Short Frame Sync Data Format. |
| #define | [I2S\_FMT\_DATA\_FORMAT\_PCM\_LONG](group__i2s__interface.md#ga7032b1894faded14a174593a3f10ca3c)   (2 << [I2S\_FMT\_DATA\_FORMAT\_SHIFT](group__i2s__interface.md#gaa3f67c47874141782fbb7ec5a671b566)) |
|  | PCM Long Frame Sync Data Format. |
| #define | [I2S\_FMT\_DATA\_FORMAT\_LEFT\_JUSTIFIED](group__i2s__interface.md#gaabc5e62ed922b8c5834ed40c6af78022)   (3 << [I2S\_FMT\_DATA\_FORMAT\_SHIFT](group__i2s__interface.md#gaa3f67c47874141782fbb7ec5a671b566)) |
|  | Left Justified Data Format. |
| #define | [I2S\_FMT\_DATA\_FORMAT\_RIGHT\_JUSTIFIED](group__i2s__interface.md#ga8ad25375c2f7344b2959bed2eec4be72)   (4 << [I2S\_FMT\_DATA\_FORMAT\_SHIFT](group__i2s__interface.md#gaa3f67c47874141782fbb7ec5a671b566)) |
|  | Right Justified Data Format. |
| #define | [I2S\_FMT\_DATA\_ORDER\_MSB](group__i2s__interface.md#ga6a6c18e170333a56086f5bcf96e552a1)   (0 << 3) |
|  | Send MSB first. |
| #define | [I2S\_FMT\_DATA\_ORDER\_LSB](group__i2s__interface.md#gacc2d0662903b2300b0e1009a8223ed7d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Send LSB first. |
| #define | [I2S\_FMT\_DATA\_ORDER\_INV](group__i2s__interface.md#ga052fa04f51ab96d90cdaf0d35f19a166)   [I2S\_FMT\_DATA\_ORDER\_LSB](group__i2s__interface.md#gacc2d0662903b2300b0e1009a8223ed7d) |
|  | Invert bit ordering, send LSB first. |
| #define | [I2S\_FMT\_CLK\_FORMAT\_SHIFT](group__i2s__interface.md#ga713fe1eb042953a315d1cb606a28d5ca)   4 |
|  | Data Format bit field position. |
| #define | [I2S\_FMT\_CLK\_FORMAT\_MASK](group__i2s__interface.md#ga16e4b44cf7f4b2d11bbd2d50522d086d)   (0x3 << [I2S\_FMT\_CLK\_FORMAT\_SHIFT](group__i2s__interface.md#ga713fe1eb042953a315d1cb606a28d5ca)) |
|  | Data Format bit field mask. |
| #define | [I2S\_FMT\_BIT\_CLK\_INV](group__i2s__interface.md#ga1bbc3f0600b406691ce016bf7bf96a5f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Invert bit clock. |
| #define | [I2S\_FMT\_FRAME\_CLK\_INV](group__i2s__interface.md#ga1cd356cbe68f622d0b3f5aee027d1f57)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Invert frame clock. |
| #define | [I2S\_FMT\_CLK\_NF\_NB](group__i2s__interface.md#gad555437f250801cbc8970cd02d7b7cde)   (0 << [I2S\_FMT\_CLK\_FORMAT\_SHIFT](group__i2s__interface.md#ga713fe1eb042953a315d1cb606a28d5ca)) |
|  | Normal Frame, Normal Bit Clk. |
| #define | [I2S\_FMT\_CLK\_NF\_IB](group__i2s__interface.md#ga85714d803548509c6b41c2579b7f2a7f)   (1 << [I2S\_FMT\_CLK\_FORMAT\_SHIFT](group__i2s__interface.md#ga713fe1eb042953a315d1cb606a28d5ca)) |
|  | Normal Frame, Inverted Bit Clk. |
| #define | [I2S\_FMT\_CLK\_IF\_NB](group__i2s__interface.md#ga5686ac4f8e3327d36f3f1293168330cd)   (2 << [I2S\_FMT\_CLK\_FORMAT\_SHIFT](group__i2s__interface.md#ga713fe1eb042953a315d1cb606a28d5ca)) |
|  | Inverted Frame, Normal Bit Clk. |
| #define | [I2S\_FMT\_CLK\_IF\_IB](group__i2s__interface.md#gaaaf186e3265d2fea6c8dc43a8030272c)   (3 << [I2S\_FMT\_CLK\_FORMAT\_SHIFT](group__i2s__interface.md#ga713fe1eb042953a315d1cb606a28d5ca)) |
|  | Inverted Frame, Inverted Bit Clk. |
| #define | [I2S\_OPT\_BIT\_CLK\_CONT](group__i2s__interface.md#ga039e7e244f7f1452dcd197c0a689d6e6)   (0 << 0) |
|  | Run bit clock continuously. |
| #define | [I2S\_OPT\_BIT\_CLK\_GATED](group__i2s__interface.md#ga4a68f73ee794684f68a02066ce1d632c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Run bit clock when sending data only. |
| #define | [I2S\_OPT\_BIT\_CLK\_MASTER](group__i2s__interface.md#ga54aaaa7f0403e4f03574ffcc6141a67f)   (0 << 1) |
|  | I2S driver is bit clock master. |
| #define | [I2S\_OPT\_BIT\_CLK\_SLAVE](group__i2s__interface.md#gaa76784ed4a645cb751b2c683bfa4be40)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | I2S driver is bit clock slave. |
| #define | [I2S\_OPT\_FRAME\_CLK\_MASTER](group__i2s__interface.md#gaedfc35128aae5058a17ef5601bdc73d2)   (0 << 2) |
|  | I2S driver is frame clock master. |
| #define | [I2S\_OPT\_FRAME\_CLK\_SLAVE](group__i2s__interface.md#ga138640dfb430fe0565840078a7b23ace)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | I2S driver is frame clock slave. |
| #define | [I2S\_OPT\_LOOPBACK](group__i2s__interface.md#ga093ed00a6081da8b4d958f80744fa09f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Loop back mode. |
| #define | [I2S\_OPT\_PINGPONG](group__i2s__interface.md#gadcb20e201a0fef1fe10f4cf916ff4b72)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Ping pong mode. |

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [i2s\_fmt\_t](group__i2s__interface.md#ga0939a3ba04a233d9d637fba8a42b0bbb) |
|  | I2S data stream format options. |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [i2s\_opt\_t](group__i2s__interface.md#gad0ca475f9bf5edeecc7de65b4f56c119) |
|  | I2S configuration options. |

| Enumerations | |
| --- | --- |
| enum | [i2s\_dir](group__i2s__interface.md#ga975a0f0901cadc789075078aa79f723f) { [I2S\_DIR\_RX](group__i2s__interface.md#gga975a0f0901cadc789075078aa79f723fac9f71d312c5d5ad7ef64af4217091aca) , [I2S\_DIR\_TX](group__i2s__interface.md#gga975a0f0901cadc789075078aa79f723fab005c2cfee6206c2b5b596638e6c8443) , [I2S\_DIR\_BOTH](group__i2s__interface.md#gga975a0f0901cadc789075078aa79f723fa3cca349476d0dbe214111b9ef5d8b272) } |
|  | I2C Direction. [More...](group__i2s__interface.md#ga975a0f0901cadc789075078aa79f723f) |
| enum | [i2s\_state](group__i2s__interface.md#ga975d09fe35ddf7942968155b62abc531) {     [I2S\_STATE\_NOT\_READY](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531a7151755b31bbb614e7b668141a7ef43a) , [I2S\_STATE\_READY](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531af6babeef999bfb034ea55366e9c59b13) , [I2S\_STATE\_RUNNING](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531aa3d21ba793efa7d8f557774e8b330a42) , [I2S\_STATE\_STOPPING](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531a972fd7e9da207b36e07731b996620a33) ,     [I2S\_STATE\_ERROR](group__i2s__interface.md#gga975d09fe35ddf7942968155b62abc531a68c0a46589ae00045900a8f79675641a)   } |
|  | Interface state. [More...](group__i2s__interface.md#ga975d09fe35ddf7942968155b62abc531) |
| enum | [i2s\_trigger\_cmd](group__i2s__interface.md#gac994676a89f1ea676475712a84003de6) {     [I2S\_TRIGGER\_START](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6a6f4cacef6ee84256e6223a4bab3bc3ac) , [I2S\_TRIGGER\_STOP](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6a37caf001d6ee6a263f3487f27952688b) , [I2S\_TRIGGER\_DRAIN](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6a7bdbdf37c5a6481faa1866be323bb9de) , [I2S\_TRIGGER\_DROP](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6ae8155a4d72875bd885dc987765d7628d) ,     [I2S\_TRIGGER\_PREPARE](group__i2s__interface.md#ggac994676a89f1ea676475712a84003de6a61943bd287840e33bffd74bbc4a59e88)   } |
|  | Trigger command. [More...](group__i2s__interface.md#gac994676a89f1ea676475712a84003de6) |

| Functions | |
| --- | --- |
| int | [i2s\_configure](group__i2s__interface.md#ga299003d72146c127f88d7c12c08889cc) (const struct [device](structdevice.md) \*dev, enum [i2s\_dir](group__i2s__interface.md#ga975a0f0901cadc789075078aa79f723f) dir, const struct [i2s\_config](structi2s__config.md) \*cfg) |
|  | Configure operation of a host I2S controller. |
| static const struct [i2s\_config](structi2s__config.md) \* | [i2s\_config\_get](group__i2s__interface.md#gacf4d51fcfd07573582858cd50a76785d) (const struct [device](structdevice.md) \*dev, enum [i2s\_dir](group__i2s__interface.md#ga975a0f0901cadc789075078aa79f723f) dir) |
|  | Fetch configuration information of a host I2S controller. |
| static int | [i2s\_read](group__i2s__interface.md#ga7f23b7959280e1c4075a4305c3edd655) (const struct [device](structdevice.md) \*dev, void \*\*mem\_block, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size) |
|  | Read data from the RX queue. |
| int | [i2s\_buf\_read](group__i2s__interface.md#ga5c8ca0bf6b394170ffbe031de8e37c28) (const struct [device](structdevice.md) \*dev, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size) |
|  | Read data from the RX queue into a provided buffer. |
| static int | [i2s\_write](group__i2s__interface.md#ga01edf23acc6c16bbaf718dab8061a7a0) (const struct [device](structdevice.md) \*dev, void \*mem\_block, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Write data to the TX queue. |
| int | [i2s\_buf\_write](group__i2s__interface.md#ga98cbfe351a8dd5db361f4667959d0b58) (const struct [device](structdevice.md) \*dev, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Write data to the TX queue from a provided buffer. |
| int | [i2s\_trigger](group__i2s__interface.md#gaaa153e6c325f8f34f2fd5d550e4d3297) (const struct [device](structdevice.md) \*dev, enum [i2s\_dir](group__i2s__interface.md#ga975a0f0901cadc789075078aa79f723f) dir, enum [i2s\_trigger\_cmd](group__i2s__interface.md#gac994676a89f1ea676475712a84003de6) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Send a trigger command. |

## Detailed Description

Public APIs for the I2S (Inter-IC Sound) bus drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i2s.h](i2s_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
