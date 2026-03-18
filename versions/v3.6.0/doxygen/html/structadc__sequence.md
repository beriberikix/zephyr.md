---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structadc__sequence.html
original_path: doxygen/html/structadc__sequence.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

adc\_sequence Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [ADC driver APIs](group__adc__interface.md)

Structure defining an ADC sampling sequence.
[More...](#details)

`#include <[adc.h](drivers_2adc_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [adc\_sequence\_options](structadc__sequence__options.md) \* | [options](#a379c6f92153dfa97439d39cbef222451) |
|  | Pointer to a structure defining additional options for the sequence. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [channels](#a5c497c4a5de20e8591063ca8661f79c1) |
|  | Bit-mask indicating the channels to be included in each sampling of this sequence. |
| void \* | [buffer](#a5df0ee0e6d3215aa052f108476bd57ec) |
|  | Pointer to a buffer where the samples are to be written. |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [buffer\_size](#a8e1bc9a4361e274bbdaedeb3151b71e5) |
|  | Specifies the actual size of the buffer pointed by the "buffer" field (in bytes). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [resolution](#ad5480691be25ed9ee81130b775743125) |
|  | ADC resolution. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [oversampling](#a233e8b20b57bb2fdbebf2c85f076c802) |
|  | Oversampling setting. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [calibrate](#a6023e3bec29deaa11b44c4df40eb7b04) |
|  | Perform calibration before the reading is taken if requested. |

## Detailed Description

Structure defining an ADC sampling sequence.

## Field Documentation

## [◆ ](#a5df0ee0e6d3215aa052f108476bd57ec)buffer

| void\* adc\_sequence::buffer |
| --- |

Pointer to a buffer where the samples are to be written.

Samples from subsequent samplings are written sequentially in the buffer. The number of samples written for each sampling is determined by the number of channels selected in the "channels" field. The values written to the buffer represent a sample from each selected channel starting from the one with the lowest ID. The buffer must be of an appropriate size, taking into account the number of selected channels and the ADC resolution used, as well as the number of samplings contained in the sequence.

## [◆ ](#a8e1bc9a4361e274bbdaedeb3151b71e5)buffer\_size

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) adc\_sequence::buffer\_size |
| --- |

Specifies the actual size of the buffer pointed by the "buffer" field (in bytes).

The driver must ensure that samples are not written beyond the limit and it must return an error if the buffer turns out to be not large enough to hold all the requested samples.

## [◆ ](#a6023e3bec29deaa11b44c4df40eb7b04)calibrate

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) adc\_sequence::calibrate |
| --- |

Perform calibration before the reading is taken if requested.

The impact of channel configuration on the calibration process is specific to the underlying hardware. ADC implementations that do not support calibration should ignore this flag.

## [◆ ](#a5c497c4a5de20e8591063ca8661f79c1)channels

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) adc\_sequence::channels |
| --- |

Bit-mask indicating the channels to be included in each sampling of this sequence.

All selected channels must be configured with [adc\_channel\_setup()](group__adc__interface.md#ga7bc0488b2d08ae2ee4996c0eed11f0bf "Configure an ADC channel.") before they are used in a sequence. The least significant bit corresponds to channel 0.

## [◆ ](#a379c6f92153dfa97439d39cbef222451)options

| const struct [adc\_sequence\_options](structadc__sequence__options.md)\* adc\_sequence::options |
| --- |

Pointer to a structure defining additional options for the sequence.

If NULL, the sequence consists of a single sampling.

## [◆ ](#a233e8b20b57bb2fdbebf2c85f076c802)oversampling

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) adc\_sequence::oversampling |
| --- |

Oversampling setting.

Each sample is averaged from 2^oversampling conversion results. This feature may be unsupported by a given ADC hardware, or in a specific mode (e.g. when sampling multiple channels).

## [◆ ](#ad5480691be25ed9ee81130b775743125)resolution

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) adc\_sequence::resolution |
| --- |

ADC resolution.

For single-ended channels the sample values are from range: 0 .. 2^resolution - 1, for differential ones:

- 2^(resolution-1) .. 2^(resolution-1) - 1.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[adc.h](drivers_2adc_8h_source.md)

- [adc\_sequence](structadc__sequence.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
