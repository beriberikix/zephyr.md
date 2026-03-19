---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__i2s__interface.html
original_path: doxygen/html/group__i2s__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

I2S Interface

[Device Driver APIs](group__io__interfaces.md)

I2S (Inter-IC Sound) Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [i2s\_config](structi2s__config.md) |
|  | Interface configuration options. [More...](structi2s__config.md#details) |

| Macros | |
| --- | --- |
| #define | [I2S\_FMT\_DATA\_FORMAT\_SHIFT](#gaa3f67c47874141782fbb7ec5a671b566)   0 |
|  | Data Format bit field position. |
| #define | [I2S\_FMT\_DATA\_FORMAT\_MASK](#gaf3eb0116133dd3a041d9a80cb3397263)   (0x7 << [I2S\_FMT\_DATA\_FORMAT\_SHIFT](#gaa3f67c47874141782fbb7ec5a671b566)) |
|  | Data Format bit field mask. |
| #define | [I2S\_FMT\_DATA\_FORMAT\_I2S](#gaa1adc5e3b722e89f20f258b0fd53a2c5)   (0 << [I2S\_FMT\_DATA\_FORMAT\_SHIFT](#gaa3f67c47874141782fbb7ec5a671b566)) |
|  | Standard I2S Data Format. |
| #define | [I2S\_FMT\_DATA\_FORMAT\_PCM\_SHORT](#ga70c7a19078a6f72e078b9c0488018b11)   (1 << [I2S\_FMT\_DATA\_FORMAT\_SHIFT](#gaa3f67c47874141782fbb7ec5a671b566)) |
|  | PCM Short Frame Sync Data Format. |
| #define | [I2S\_FMT\_DATA\_FORMAT\_PCM\_LONG](#ga7032b1894faded14a174593a3f10ca3c)   (2 << [I2S\_FMT\_DATA\_FORMAT\_SHIFT](#gaa3f67c47874141782fbb7ec5a671b566)) |
|  | PCM Long Frame Sync Data Format. |
| #define | [I2S\_FMT\_DATA\_FORMAT\_LEFT\_JUSTIFIED](#gaabc5e62ed922b8c5834ed40c6af78022)   (3 << [I2S\_FMT\_DATA\_FORMAT\_SHIFT](#gaa3f67c47874141782fbb7ec5a671b566)) |
|  | Left Justified Data Format. |
| #define | [I2S\_FMT\_DATA\_FORMAT\_RIGHT\_JUSTIFIED](#ga8ad25375c2f7344b2959bed2eec4be72)   (4 << [I2S\_FMT\_DATA\_FORMAT\_SHIFT](#gaa3f67c47874141782fbb7ec5a671b566)) |
|  | Right Justified Data Format. |
| #define | [I2S\_FMT\_DATA\_ORDER\_MSB](#ga6a6c18e170333a56086f5bcf96e552a1)   (0 << 3) |
|  | Send MSB first. |
| #define | [I2S\_FMT\_DATA\_ORDER\_LSB](#gacc2d0662903b2300b0e1009a8223ed7d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Send LSB first. |
| #define | [I2S\_FMT\_DATA\_ORDER\_INV](#ga052fa04f51ab96d90cdaf0d35f19a166)   [I2S\_FMT\_DATA\_ORDER\_LSB](#gacc2d0662903b2300b0e1009a8223ed7d) |
|  | Invert bit ordering, send LSB first. |
| #define | [I2S\_FMT\_CLK\_FORMAT\_SHIFT](#ga713fe1eb042953a315d1cb606a28d5ca)   4 |
|  | Data Format bit field position. |
| #define | [I2S\_FMT\_CLK\_FORMAT\_MASK](#ga16e4b44cf7f4b2d11bbd2d50522d086d)   (0x3 << [I2S\_FMT\_CLK\_FORMAT\_SHIFT](#ga713fe1eb042953a315d1cb606a28d5ca)) |
|  | Data Format bit field mask. |
| #define | [I2S\_FMT\_BIT\_CLK\_INV](#ga1bbc3f0600b406691ce016bf7bf96a5f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Invert bit clock. |
| #define | [I2S\_FMT\_FRAME\_CLK\_INV](#ga1cd356cbe68f622d0b3f5aee027d1f57)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Invert frame clock. |
| #define | [I2S\_FMT\_CLK\_NF\_NB](#gad555437f250801cbc8970cd02d7b7cde)   (0 << [I2S\_FMT\_CLK\_FORMAT\_SHIFT](#ga713fe1eb042953a315d1cb606a28d5ca)) |
|  | Normal Frame, Normal Bit Clk. |
| #define | [I2S\_FMT\_CLK\_NF\_IB](#ga85714d803548509c6b41c2579b7f2a7f)   (1 << [I2S\_FMT\_CLK\_FORMAT\_SHIFT](#ga713fe1eb042953a315d1cb606a28d5ca)) |
|  | Normal Frame, Inverted Bit Clk. |
| #define | [I2S\_FMT\_CLK\_IF\_NB](#ga5686ac4f8e3327d36f3f1293168330cd)   (2 << [I2S\_FMT\_CLK\_FORMAT\_SHIFT](#ga713fe1eb042953a315d1cb606a28d5ca)) |
|  | Inverted Frame, Normal Bit Clk. |
| #define | [I2S\_FMT\_CLK\_IF\_IB](#gaaaf186e3265d2fea6c8dc43a8030272c)   (3 << [I2S\_FMT\_CLK\_FORMAT\_SHIFT](#ga713fe1eb042953a315d1cb606a28d5ca)) |
|  | Inverted Frame, Inverted Bit Clk. |
| #define | [I2S\_OPT\_BIT\_CLK\_CONT](#ga039e7e244f7f1452dcd197c0a689d6e6)   (0 << 0) |
|  | Run bit clock continuously. |
| #define | [I2S\_OPT\_BIT\_CLK\_GATED](#ga4a68f73ee794684f68a02066ce1d632c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Run bit clock when sending data only. |
| #define | [I2S\_OPT\_BIT\_CLK\_MASTER](#ga54aaaa7f0403e4f03574ffcc6141a67f)   (0 << 1) |
|  | I2S driver is bit clock master. |
| #define | [I2S\_OPT\_BIT\_CLK\_SLAVE](#gaa76784ed4a645cb751b2c683bfa4be40)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | I2S driver is bit clock slave. |
| #define | [I2S\_OPT\_FRAME\_CLK\_MASTER](#gaedfc35128aae5058a17ef5601bdc73d2)   (0 << 2) |
|  | I2S driver is frame clock master. |
| #define | [I2S\_OPT\_FRAME\_CLK\_SLAVE](#ga138640dfb430fe0565840078a7b23ace)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | I2S driver is frame clock slave. |
| #define | [I2S\_OPT\_LOOPBACK](#ga093ed00a6081da8b4d958f80744fa09f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Loop back mode. |
| #define | [I2S\_OPT\_PINGPONG](#gadcb20e201a0fef1fe10f4cf916ff4b72)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Ping pong mode. |

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [i2s\_fmt\_t](#ga0939a3ba04a233d9d637fba8a42b0bbb) |
|  | I2S data stream format options. |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [i2s\_opt\_t](#gad0ca475f9bf5edeecc7de65b4f56c119) |
|  | I2S configuration options. |

| Enumerations | |
| --- | --- |
| enum | [i2s\_dir](#ga975a0f0901cadc789075078aa79f723f) { [I2S\_DIR\_RX](#gga975a0f0901cadc789075078aa79f723fac9f71d312c5d5ad7ef64af4217091aca) , [I2S\_DIR\_TX](#gga975a0f0901cadc789075078aa79f723fab005c2cfee6206c2b5b596638e6c8443) , [I2S\_DIR\_BOTH](#gga975a0f0901cadc789075078aa79f723fa3cca349476d0dbe214111b9ef5d8b272) } |
|  | I2C Direction. [More...](#ga975a0f0901cadc789075078aa79f723f) |
| enum | [i2s\_state](#ga975d09fe35ddf7942968155b62abc531) {     [I2S\_STATE\_NOT\_READY](#gga975d09fe35ddf7942968155b62abc531a7151755b31bbb614e7b668141a7ef43a) , [I2S\_STATE\_READY](#gga975d09fe35ddf7942968155b62abc531af6babeef999bfb034ea55366e9c59b13) , [I2S\_STATE\_RUNNING](#gga975d09fe35ddf7942968155b62abc531aa3d21ba793efa7d8f557774e8b330a42) , [I2S\_STATE\_STOPPING](#gga975d09fe35ddf7942968155b62abc531a972fd7e9da207b36e07731b996620a33) ,     [I2S\_STATE\_ERROR](#gga975d09fe35ddf7942968155b62abc531a68c0a46589ae00045900a8f79675641a)   } |
|  | Interface state. [More...](#ga975d09fe35ddf7942968155b62abc531) |
| enum | [i2s\_trigger\_cmd](#gac994676a89f1ea676475712a84003de6) {     [I2S\_TRIGGER\_START](#ggac994676a89f1ea676475712a84003de6a6f4cacef6ee84256e6223a4bab3bc3ac) , [I2S\_TRIGGER\_STOP](#ggac994676a89f1ea676475712a84003de6a37caf001d6ee6a263f3487f27952688b) , [I2S\_TRIGGER\_DRAIN](#ggac994676a89f1ea676475712a84003de6a7bdbdf37c5a6481faa1866be323bb9de) , [I2S\_TRIGGER\_DROP](#ggac994676a89f1ea676475712a84003de6ae8155a4d72875bd885dc987765d7628d) ,     [I2S\_TRIGGER\_PREPARE](#ggac994676a89f1ea676475712a84003de6a61943bd287840e33bffd74bbc4a59e88)   } |
|  | Trigger command. [More...](#gac994676a89f1ea676475712a84003de6) |

| Functions | |
| --- | --- |
| int | [i2s\_configure](#ga299003d72146c127f88d7c12c08889cc) (const struct [device](structdevice.md) \*dev, enum [i2s\_dir](#ga975a0f0901cadc789075078aa79f723f) dir, const struct [i2s\_config](structi2s__config.md) \*cfg) |
|  | Configure operation of a host I2S controller. |
| static const struct [i2s\_config](structi2s__config.md) \* | [i2s\_config\_get](#gacf4d51fcfd07573582858cd50a76785d) (const struct [device](structdevice.md) \*dev, enum [i2s\_dir](#ga975a0f0901cadc789075078aa79f723f) dir) |
|  | Fetch configuration information of a host I2S controller. |
| static int | [i2s\_read](#ga7f23b7959280e1c4075a4305c3edd655) (const struct [device](structdevice.md) \*dev, void \*\*mem\_block, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size) |
|  | Read data from the RX queue. |
| int | [i2s\_buf\_read](#ga5c8ca0bf6b394170ffbe031de8e37c28) (const struct [device](structdevice.md) \*dev, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size) |
|  | Read data from the RX queue into a provided buffer. |
| static int | [i2s\_write](#ga01edf23acc6c16bbaf718dab8061a7a0) (const struct [device](structdevice.md) \*dev, void \*mem\_block, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Write data to the TX queue. |
| int | [i2s\_buf\_write](#ga98cbfe351a8dd5db361f4667959d0b58) (const struct [device](structdevice.md) \*dev, void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Write data to the TX queue from a provided buffer. |
| int | [i2s\_trigger](#gaaa153e6c325f8f34f2fd5d550e4d3297) (const struct [device](structdevice.md) \*dev, enum [i2s\_dir](#ga975a0f0901cadc789075078aa79f723f) dir, enum [i2s\_trigger\_cmd](#gac994676a89f1ea676475712a84003de6) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
|  | Send a trigger command. |

## Detailed Description

I2S (Inter-IC Sound) Interface.

Since
:   1.9

Version
:   1.0.0

The I2S API provides support for the standard I2S interface standard as well as common non-standard extensions such as PCM Short/Long Frame Sync, Left/Right Justified Data Format.

## Macro Definition Documentation

## [◆ ](#ga1bbc3f0600b406691ce016bf7bf96a5f)I2S\_FMT\_BIT\_CLK\_INV

| #define I2S\_FMT\_BIT\_CLK\_INV   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Invert bit clock.

## [◆ ](#ga16e4b44cf7f4b2d11bbd2d50522d086d)I2S\_FMT\_CLK\_FORMAT\_MASK

| #define I2S\_FMT\_CLK\_FORMAT\_MASK   (0x3 << [I2S\_FMT\_CLK\_FORMAT\_SHIFT](#ga713fe1eb042953a315d1cb606a28d5ca)) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Data Format bit field mask.

## [◆ ](#ga713fe1eb042953a315d1cb606a28d5ca)I2S\_FMT\_CLK\_FORMAT\_SHIFT

| #define I2S\_FMT\_CLK\_FORMAT\_SHIFT   4 |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Data Format bit field position.

## [◆ ](#gaaaf186e3265d2fea6c8dc43a8030272c)I2S\_FMT\_CLK\_IF\_IB

| #define I2S\_FMT\_CLK\_IF\_IB   (3 << [I2S\_FMT\_CLK\_FORMAT\_SHIFT](#ga713fe1eb042953a315d1cb606a28d5ca)) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Inverted Frame, Inverted Bit Clk.

## [◆ ](#ga5686ac4f8e3327d36f3f1293168330cd)I2S\_FMT\_CLK\_IF\_NB

| #define I2S\_FMT\_CLK\_IF\_NB   (2 << [I2S\_FMT\_CLK\_FORMAT\_SHIFT](#ga713fe1eb042953a315d1cb606a28d5ca)) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Inverted Frame, Normal Bit Clk.

## [◆ ](#ga85714d803548509c6b41c2579b7f2a7f)I2S\_FMT\_CLK\_NF\_IB

| #define I2S\_FMT\_CLK\_NF\_IB   (1 << [I2S\_FMT\_CLK\_FORMAT\_SHIFT](#ga713fe1eb042953a315d1cb606a28d5ca)) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Normal Frame, Inverted Bit Clk.

## [◆ ](#gad555437f250801cbc8970cd02d7b7cde)I2S\_FMT\_CLK\_NF\_NB

| #define I2S\_FMT\_CLK\_NF\_NB   (0 << [I2S\_FMT\_CLK\_FORMAT\_SHIFT](#ga713fe1eb042953a315d1cb606a28d5ca)) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Normal Frame, Normal Bit Clk.

## [◆ ](#gaa1adc5e3b722e89f20f258b0fd53a2c5)I2S\_FMT\_DATA\_FORMAT\_I2S

| #define I2S\_FMT\_DATA\_FORMAT\_I2S   (0 << [I2S\_FMT\_DATA\_FORMAT\_SHIFT](#gaa3f67c47874141782fbb7ec5a671b566)) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Standard I2S Data Format.

Serial data is transmitted in two's complement with the MSB first. Both Word Select (WS) and Serial Data (SD) signals are sampled on the rising edge of the clock signal (SCK). The MSB is always sent one clock period after the WS changes. Left channel data are sent first indicated by WS = 0, followed by right channel data indicated by WS = 1.

```
   -. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-.
SCK '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '
   -.                               .-------------------------------.
WS  '-------------------------------'                               '----
   -.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.
SD  |   |MSB|   |...|   |LSB| x |...| x |MSB|   |...|   |LSB| x |...| x |
   -'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'
        | Left channel                  | Right channel                 |
```

## [◆ ](#gaabc5e62ed922b8c5834ed40c6af78022)I2S\_FMT\_DATA\_FORMAT\_LEFT\_JUSTIFIED

| #define I2S\_FMT\_DATA\_FORMAT\_LEFT\_JUSTIFIED   (3 << [I2S\_FMT\_DATA\_FORMAT\_SHIFT](#gaa3f67c47874141782fbb7ec5a671b566)) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Left Justified Data Format.

Serial data is transmitted in two's complement with the MSB first. Both Word Select (WS) and Serial Data (SD) signals are sampled on the rising edge of the clock signal (SCK). The bits within the data word are left justified such that the MSB is always sent in the clock period following the WS transition. Left channel data are sent first indicated by WS = 1, followed by right channel data indicated by WS = 0.

```
     .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-.
SCK -' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-
       .-------------------------------.                               .-
WS  ---'                               '-------------------------------'
    ---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.-
SD     |MSB|   |...|   |LSB| x |...| x |MSB|   |...|   |LSB| x |...| x |
    ---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'-
       | Left channel                  | Right channel                 |
```

## [◆ ](#gaf3eb0116133dd3a041d9a80cb3397263)I2S\_FMT\_DATA\_FORMAT\_MASK

| #define I2S\_FMT\_DATA\_FORMAT\_MASK   (0x7 << [I2S\_FMT\_DATA\_FORMAT\_SHIFT](#gaa3f67c47874141782fbb7ec5a671b566)) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Data Format bit field mask.

## [◆ ](#ga7032b1894faded14a174593a3f10ca3c)I2S\_FMT\_DATA\_FORMAT\_PCM\_LONG

| #define I2S\_FMT\_DATA\_FORMAT\_PCM\_LONG   (2 << [I2S\_FMT\_DATA\_FORMAT\_SHIFT](#gaa3f67c47874141782fbb7ec5a671b566)) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

PCM Long Frame Sync Data Format.

Serial data is transmitted in two's complement with the MSB first. Both Word Select (WS) and Serial Data (SD) signals are sampled on the falling edge of the clock signal (SCK). The rising edge of the frame sync signal (WS) indicates the start of the PCM word. The frame sync has an arbitrary length, however it has to fall before the start of the next frame. An arbitrary number of data words can be sent in one frame.

```
     .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-.
SCK -' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-
         .--- ---.    ---.        ---.                               .---
WS      -'       '-      '-          '-                             -'
    -.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---
SD   |   |MSB|   |...|   |LSB|MSB|   |...|   |LSB|MSB|   |...|   |LSB|
    -'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---
         | Word 1            | Word 2            | Word 3  |  Word n |
```

## [◆ ](#ga70c7a19078a6f72e078b9c0488018b11)I2S\_FMT\_DATA\_FORMAT\_PCM\_SHORT

| #define I2S\_FMT\_DATA\_FORMAT\_PCM\_SHORT   (1 << [I2S\_FMT\_DATA\_FORMAT\_SHIFT](#gaa3f67c47874141782fbb7ec5a671b566)) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

PCM Short Frame Sync Data Format.

Serial data is transmitted in two's complement with the MSB first. Both Word Select (WS) and Serial Data (SD) signals are sampled on the falling edge of the clock signal (SCK). The falling edge of the frame sync signal (WS) indicates the start of the PCM word. The frame sync is one clock cycle long. An arbitrary number of data words can be sent in one frame.

```
     .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-.
SCK -' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-
     .---.                                                       .---.
WS  -'   '-                                                     -'   '-
    -.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---
SD   |   |MSB|   |...|   |LSB|MSB|   |...|   |LSB|MSB|   |...|   |LSB|
    -'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---
         | Word 1            | Word 2            | Word 3  |  Word n |
```

## [◆ ](#ga8ad25375c2f7344b2959bed2eec4be72)I2S\_FMT\_DATA\_FORMAT\_RIGHT\_JUSTIFIED

| #define I2S\_FMT\_DATA\_FORMAT\_RIGHT\_JUSTIFIED   (4 << [I2S\_FMT\_DATA\_FORMAT\_SHIFT](#gaa3f67c47874141782fbb7ec5a671b566)) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Right Justified Data Format.

Serial data is transmitted in two's complement with the MSB first. Both Word Select (WS) and Serial Data (SD) signals are sampled on the rising edge of the clock signal (SCK). The bits within the data word are right justified such that the LSB is always sent in the clock period preceding the WS transition. Left channel data are sent first indicated by WS = 1, followed by right channel data indicated by WS = 0.

```
     .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-. .-.
SCK -' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-' '-
       .-------------------------------.                               .-
WS  ---'                               '-------------------------------'
    ---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.---.-
SD     | x |...| x |MSB|   |...|   |LSB| x |...| x |MSB|   |...|   |LSB|
    ---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'---'-
       | Left channel                  | Right channel                 |
```

## [◆ ](#gaa3f67c47874141782fbb7ec5a671b566)I2S\_FMT\_DATA\_FORMAT\_SHIFT

| #define I2S\_FMT\_DATA\_FORMAT\_SHIFT   0 |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Data Format bit field position.

## [◆ ](#ga052fa04f51ab96d90cdaf0d35f19a166)I2S\_FMT\_DATA\_ORDER\_INV

| #define I2S\_FMT\_DATA\_ORDER\_INV   [I2S\_FMT\_DATA\_ORDER\_LSB](#gacc2d0662903b2300b0e1009a8223ed7d) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Invert bit ordering, send LSB first.

## [◆ ](#gacc2d0662903b2300b0e1009a8223ed7d)I2S\_FMT\_DATA\_ORDER\_LSB

| #define I2S\_FMT\_DATA\_ORDER\_LSB   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Send LSB first.

## [◆ ](#ga6a6c18e170333a56086f5bcf96e552a1)I2S\_FMT\_DATA\_ORDER\_MSB

| #define I2S\_FMT\_DATA\_ORDER\_MSB   (0 << 3) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Send MSB first.

## [◆ ](#ga1cd356cbe68f622d0b3f5aee027d1f57)I2S\_FMT\_FRAME\_CLK\_INV

| #define I2S\_FMT\_FRAME\_CLK\_INV   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Invert frame clock.

## [◆ ](#ga039e7e244f7f1452dcd197c0a689d6e6)I2S\_OPT\_BIT\_CLK\_CONT

| #define I2S\_OPT\_BIT\_CLK\_CONT   (0 << 0) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Run bit clock continuously.

## [◆ ](#ga4a68f73ee794684f68a02066ce1d632c)I2S\_OPT\_BIT\_CLK\_GATED

| #define I2S\_OPT\_BIT\_CLK\_GATED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Run bit clock when sending data only.

## [◆ ](#ga54aaaa7f0403e4f03574ffcc6141a67f)I2S\_OPT\_BIT\_CLK\_MASTER

| #define I2S\_OPT\_BIT\_CLK\_MASTER   (0 << 1) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

I2S driver is bit clock master.

## [◆ ](#gaa76784ed4a645cb751b2c683bfa4be40)I2S\_OPT\_BIT\_CLK\_SLAVE

| #define I2S\_OPT\_BIT\_CLK\_SLAVE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

I2S driver is bit clock slave.

## [◆ ](#gaedfc35128aae5058a17ef5601bdc73d2)I2S\_OPT\_FRAME\_CLK\_MASTER

| #define I2S\_OPT\_FRAME\_CLK\_MASTER   (0 << 2) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

I2S driver is frame clock master.

## [◆ ](#ga138640dfb430fe0565840078a7b23ace)I2S\_OPT\_FRAME\_CLK\_SLAVE

| #define I2S\_OPT\_FRAME\_CLK\_SLAVE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

I2S driver is frame clock slave.

## [◆ ](#ga093ed00a6081da8b4d958f80744fa09f)I2S\_OPT\_LOOPBACK

| #define I2S\_OPT\_LOOPBACK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Loop back mode.

In loop back mode RX input will be connected internally to TX output. This is used primarily for testing.

## [◆ ](#gadcb20e201a0fef1fe10f4cf916ff4b72)I2S\_OPT\_PINGPONG

| #define I2S\_OPT\_PINGPONG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Ping pong mode.

In ping pong mode TX output will keep alternating between a ping buffer and a pong buffer. This is normally used in audio streams when one buffer is being populated while the other is being played (DMAed) and vice versa. So, in this mode, 2 sets of buffers fixed in size are used. Static Arrays are used to achieve this and hence they are never freed.

## Typedef Documentation

## [◆ ](#ga0939a3ba04a233d9d637fba8a42b0bbb)i2s\_fmt\_t

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [i2s\_fmt\_t](#ga0939a3ba04a233d9d637fba8a42b0bbb) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

I2S data stream format options.

## [◆ ](#gad0ca475f9bf5edeecc7de65b4f56c119)i2s\_opt\_t

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [i2s\_opt\_t](#gad0ca475f9bf5edeecc7de65b4f56c119) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

I2S configuration options.

## Enumeration Type Documentation

## [◆ ](#ga975a0f0901cadc789075078aa79f723f)i2s\_dir

| enum [i2s\_dir](#ga975a0f0901cadc789075078aa79f723f) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

I2C Direction.

| Enumerator | |
| --- | --- |
| I2S\_DIR\_RX | Receive data. |
| I2S\_DIR\_TX | Transmit data. |
| I2S\_DIR\_BOTH | Both receive and transmit data. |

## [◆ ](#ga975d09fe35ddf7942968155b62abc531)i2s\_state

| enum [i2s\_state](#ga975d09fe35ddf7942968155b62abc531) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Interface state.

| Enumerator | |
| --- | --- |
| I2S\_STATE\_NOT\_READY | The interface is not ready.  The interface was initialized but is not yet ready to receive / transmit data. Call [i2s\_configure()](#ga299003d72146c127f88d7c12c08889cc) to configure interface and change its state to READY. |
| I2S\_STATE\_READY | The interface is ready to receive / transmit data. |
| I2S\_STATE\_RUNNING | The interface is receiving / transmitting data. |
| I2S\_STATE\_STOPPING | The interface is draining its transmit queue. |
| I2S\_STATE\_ERROR | TX buffer underrun or RX buffer overrun has occurred. |

## [◆ ](#gac994676a89f1ea676475712a84003de6)i2s\_trigger\_cmd

| enum [i2s\_trigger\_cmd](#gac994676a89f1ea676475712a84003de6) |
| --- |

`#include <[i2s.h](i2s_8h.md)>`

Trigger command.

| Enumerator | |
| --- | --- |
| I2S\_TRIGGER\_START | Start the transmission / reception of data.  If I2S\_DIR\_TX is set some data has to be queued for transmission by the [i2s\_write()](#ga01edf23acc6c16bbaf718dab8061a7a0) function. This trigger can be used in READY state only and changes the interface state to RUNNING. |
| I2S\_TRIGGER\_STOP | Stop the transmission / reception of data.  Stop the transmission / reception of data at the end of the current memory block. This trigger can be used in RUNNING state only and at first changes the interface state to STOPPING. When the current TX / RX block is transmitted / received the state is changed to READY. Subsequent START trigger will resume transmission / reception where it stopped. |
| I2S\_TRIGGER\_DRAIN | Empty the transmit queue.  Send all data in the transmit queue and stop the transmission. If the trigger is applied to the RX queue it has the same effect as I2S\_TRIGGER\_STOP. This trigger can be used in RUNNING state only and at first changes the interface state to STOPPING. When all TX blocks are transmitted the state is changed to READY. |
| I2S\_TRIGGER\_DROP | Discard the transmit / receive queue.  Stop the transmission / reception immediately and discard the contents of the respective queue. This trigger can be used in any state other than NOT\_READY and changes the interface state to READY. |
| I2S\_TRIGGER\_PREPARE | Prepare the queues after underrun/overrun error has occurred.  This trigger can be used in ERROR state only and changes the interface state to READY. |

## Function Documentation

## [◆ ](#ga5c8ca0bf6b394170ffbe031de8e37c28)i2s\_buf\_read()

| int i2s\_buf\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *size* ) |

`#include <[i2s.h](i2s_8h.md)>`

Read data from the RX queue into a provided buffer.

Data received by the I2S interface is stored in the RX queue consisting of memory blocks preallocated by this function from rx\_mem\_slab (as defined by i2s\_configure). Calling this function removes one block from the queue which is copied into the provided buffer and then freed.

The provided buffer must be large enough to contain a full memory block of data, which is parameterized for the channel via [i2s\_configure()](#ga299003d72146c127f88d7c12c08889cc).

This function is otherwise equivalent to [i2s\_read()](#ga7f23b7959280e1c4075a4305c3edd655).

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | buf | Destination buffer for read data, which must be at least the as large as the configured memory block size for the RX channel. |
    | size | Pointer to the variable storing the number of bytes read. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | The interface is in NOT\_READY or ERROR state and there are no more data blocks in the RX queue. |
    | -EBUSY | Returned without waiting. |
    | -EAGAIN | Waiting period timed out. |

## [◆ ](#ga98cbfe351a8dd5db361f4667959d0b58)i2s\_buf\_write()

| int i2s\_buf\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

`#include <[i2s.h](i2s_8h.md)>`

Write data to the TX queue from a provided buffer.

This function acquires a memory block from the I2S channel TX queue and copies the provided data buffer into it. It is otherwise equivalent to [i2s\_write()](#ga01edf23acc6c16bbaf718dab8061a7a0).

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | buf | Pointer to a buffer containing the data to transmit. |
    | size | Number of bytes to write. This value has to be equal or smaller than the size of the channel's TX memory block configuration. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | The interface is not in READY or RUNNING state. |
    | -EBUSY | Returned without waiting. |
    | -EAGAIN | Waiting period timed out. |
    | -ENOMEM | No memory in TX slab queue. |
    | -EINVAL | Size parameter larger than TX queue memory block. |

## [◆ ](#gacf4d51fcfd07573582858cd50a76785d)i2s\_config\_get()

| | const struct [i2s\_config](structi2s__config.md) \* i2s\_config\_get | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | enum [i2s\_dir](#ga975a0f0901cadc789075078aa79f723f) | *dir* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2s.h](i2s_8h.md)>`

Fetch configuration information of a host I2S controller.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | dir | Stream direction: RX or TX as defined by I2S\_DIR\_\* |

Return values
:   | Pointer | to the structure containing configuration parameters, or NULL if un-configured |
    | --- | --- |

## [◆ ](#ga299003d72146c127f88d7c12c08889cc)i2s\_configure()

| int i2s\_configure | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [i2s\_dir](#ga975a0f0901cadc789075078aa79f723f) | *dir*, |
|  |  | const struct [i2s\_config](structi2s__config.md) \* | *cfg* ) |

`#include <[i2s.h](i2s_8h.md)>`

Configure operation of a host I2S controller.

The dir parameter specifies if Transmit (TX) or Receive (RX) direction will be configured by data provided via cfg parameter.

The function can be called in NOT\_READY or READY state only. If executed successfully the function will change the interface state to READY.

If the function is called with the parameter cfg->frame\_clk\_freq set to 0 the interface state will be changed to NOT\_READY.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | dir | Stream direction: RX, TX, or both, as defined by I2S\_DIR\_\*. The I2S\_DIR\_BOTH value may not be supported by some drivers. For those, the RX and TX streams need to be configured separately. |
    | cfg | Pointer to the structure containing configuration parameters. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | Invalid argument. |
    | -ENOSYS | I2S\_DIR\_BOTH value is not supported. |

## [◆ ](#ga7f23b7959280e1c4075a4305c3edd655)i2s\_read()

| | int i2s\_read | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | void \*\* | *mem\_block*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2s.h](i2s_8h.md)>`

Read data from the RX queue.

Data received by the I2S interface is stored in the RX queue consisting of memory blocks preallocated by this function from rx\_mem\_slab (as defined by i2s\_configure). Ownership of the RX memory block is passed on to the user application which has to release it.

The data is read in chunks equal to the size of the memory block. If the interface is in READY state the number of bytes read can be smaller.

If there is no data in the RX queue the function will block waiting for the next RX memory block to fill in. This operation can timeout as defined by i2s\_configure. If the timeout value is set to K\_NO\_WAIT the function is non-blocking.

Reading from the RX queue is possible in any state other than NOT\_READY. If the interface is in the ERROR state it is still possible to read all the valid data stored in RX queue. Afterwards the function will return -EIO error.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | mem\_block | Pointer to the RX memory block containing received data. |
    | size | Pointer to the variable storing the number of bytes read. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | The interface is in NOT\_READY or ERROR state and there are no more data blocks in the RX queue. |
    | -EBUSY | Returned without waiting. |
    | -EAGAIN | Waiting period timed out. |

## [◆ ](#gaaa153e6c325f8f34f2fd5d550e4d3297)i2s\_trigger()

| int i2s\_trigger | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [i2s\_dir](#ga975a0f0901cadc789075078aa79f723f) | *dir*, |
|  |  | enum [i2s\_trigger\_cmd](#gac994676a89f1ea676475712a84003de6) | *cmd* ) |

`#include <[i2s.h](i2s_8h.md)>`

Send a trigger command.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | dir | Stream direction: RX, TX, or both, as defined by I2S\_DIR\_\*. The I2S\_DIR\_BOTH value may not be supported by some drivers. For those, triggering need to be done separately for the RX and TX streams. |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | Trigger command. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EINVAL | Invalid argument. |
    | -EIO | The trigger cannot be executed in the current state or a DMA channel cannot be allocated. |
    | -ENOMEM | RX/TX memory block not available. |
    | -ENOSYS | I2S\_DIR\_BOTH value is not supported. |

## [◆ ](#ga01edf23acc6c16bbaf718dab8061a7a0)i2s\_write()

| | int i2s\_write | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | void \* | *mem\_block*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[i2s.h](i2s_8h.md)>`

Write data to the TX queue.

Data to be sent by the I2S interface is stored first in the TX queue. TX queue consists of memory blocks preallocated by the user from tx\_mem\_slab (as defined by i2s\_configure). This function takes ownership of the memory block and will release it when all data are transmitted.

If there are no free slots in the TX queue the function will block waiting for the next TX memory block to be send and removed from the queue. This operation can timeout as defined by i2s\_configure. If the timeout value is set to K\_NO\_WAIT the function is non-blocking.

Writing to the TX queue is only possible if the interface is in READY or RUNNING state.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | mem\_block | Pointer to the TX memory block containing data to be sent. |
    | size | Number of bytes to write. This value has to be equal or smaller than the size of the memory block. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | The interface is not in READY or RUNNING state. |
    | -EBUSY | Returned without waiting. |
    | -EAGAIN | Waiting period timed out. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
