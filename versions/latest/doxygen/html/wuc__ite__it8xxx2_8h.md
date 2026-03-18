---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/wuc__ite__it8xxx2_8h.html
original_path: doxygen/html/wuc__ite__it8xxx2_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wuc\_ite\_it8xxx2.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](wuc__ite__it8xxx2_8h_source.md)

| Functions | |
| --- | --- |
| void | [it8xxx2\_wuc\_enable](#a12abd49530eee59cb3d9670c35c307b1) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask) |
|  | A trigger condition on the corresponding input generates a wake-up signal to the power management control of EC. |
| void | [it8xxx2\_wuc\_disable](#af707d0b461010aea4fcfbfbeb82d0b2b) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask) |
|  | A trigger condition on the corresponding input doesn't assert the wake-up signal (canceled not pending). |
| void | [it8xxx2\_wuc\_clear\_status](#ad48382e2c3fd0d12c3a1334d863a9065) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask) |
|  | Write-1-clear a trigger condition that occurs on the corresponding input. |
| void | [it8xxx2\_wuc\_set\_polarity](#ab589f992436176f288056e219ead7972) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mask, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Select the trigger edge mode on the corresponding input. |

## Function Documentation

## [◆ ](#ad48382e2c3fd0d12c3a1334d863a9065)it8xxx2\_wuc\_clear\_status()

| void it8xxx2\_wuc\_clear\_status | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mask* ) |

Write-1-clear a trigger condition that occurs on the corresponding input.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | mask | Pin mask of WUC group |

## [◆ ](#af707d0b461010aea4fcfbfbeb82d0b2b)it8xxx2\_wuc\_disable()

| void it8xxx2\_wuc\_disable | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mask* ) |

A trigger condition on the corresponding input doesn't assert the wake-up signal (canceled not pending).

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | mask | Pin mask of WUC group |

## [◆ ](#a12abd49530eee59cb3d9670c35c307b1)it8xxx2\_wuc\_enable()

| void it8xxx2\_wuc\_enable | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mask* ) |

A trigger condition on the corresponding input generates a wake-up signal to the power management control of EC.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | mask | Pin mask of WUC group |

## [◆ ](#ab589f992436176f288056e219ead7972)it8xxx2\_wuc\_set\_polarity()

| void it8xxx2\_wuc\_set\_polarity | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *mask*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

Select the trigger edge mode on the corresponding input.

Parameters
:   | dev | Pointer to the device structure for the driver instance |
    | --- | --- |
    | mask | Pin mask of WUC group |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Select the trigger edge mode |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [wuc\_ite\_it8xxx2.h](wuc__ite__it8xxx2_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
