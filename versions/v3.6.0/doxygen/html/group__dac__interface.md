---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__dac__interface.html
original_path: doxygen/html/group__dac__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

DAC driver APIs

[Device Driver APIs](group__io__interfaces.md)

DAC driver APIs.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [dac\_channel\_cfg](structdac__channel__cfg.md) |
|  | Structure for specifying the configuration of a DAC channel. [More...](structdac__channel__cfg.md#details) |

| Functions | |
| --- | --- |
| int | [dac\_channel\_setup](#gab8be77003ba8fd7225c0808f95602a56) (const struct [device](structdevice.md) \*dev, const struct [dac\_channel\_cfg](structdac__channel__cfg.md) \*channel\_cfg) |
|  | Configure a DAC channel. |
| int | [dac\_write\_value](#ga437a6f6b2402cf2e2a2a689429663b4e) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) value) |
|  | Write a single value to a DAC channel. |

## Detailed Description

DAC driver APIs.

## Function Documentation

## [◆ ](#gab8be77003ba8fd7225c0808f95602a56)dac\_channel\_setup()

| int dac\_channel\_setup | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [dac\_channel\_cfg](structdac__channel__cfg.md) \* | *channel\_cfg* ) |

`#include <[dac.h](dac_8h.md)>`

Configure a DAC channel.

It is required to call this function and configure each channel before it is selected for a write request.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel\_cfg | Channel configuration. |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -EINVAL | If a parameter with an invalid value has been provided. |
    | -ENOTSUP | If the requested resolution is not supported. |

## [◆ ](#ga437a6f6b2402cf2e2a2a689429663b4e)dac\_write\_value()

| int dac\_write\_value | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *value* ) |

`#include <[dac.h](dac_8h.md)>`

Write a single value to a DAC channel.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | channel | Number of the channel to be used. |
    | value | Data to be written to DAC output registers. |

Return values
:   | 0 | On success. |
    | --- | --- |
    | -EINVAL | If a parameter with an invalid value has been provided. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
