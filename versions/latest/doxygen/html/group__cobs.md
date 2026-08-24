---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__cobs.html
original_path: doxygen/html/group__cobs.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

COBS (Consistent Overhead Byte Stuffing)

[Utilities](group__utilities.md)

COBS encoding and decoding functions with custom delimiter support.
[More...](#details)

| Functions | |
| --- | --- |
| static [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [cobs\_max\_encoded\_len](#ga71047f135e408e95d83828e898e823b0) ([size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) decoded\_size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Calculate maximum encoded buffer size. |
| int | [cobs\_encode](#gadf39d47a13fe1e3b10bcc9208f5b4786) (struct [net\_buf](structnet__buf.md) \*src, struct [net\_buf](structnet__buf.md) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Standard COBS encoding. |
| int | [cobs\_decode](#gabb6193b8d15b33e5c739c9609376950f) (struct [net\_buf](structnet__buf.md) \*src, struct [net\_buf](structnet__buf.md) \*dst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Standard COBS decoding. |

## Detailed Description

COBS encoding and decoding functions with custom delimiter support.

Provides functions for COBS encoding/decoding with configurable delimiters. The implementation handles both standard zero-delimited COBS and custom delimiter variants.

## Function Documentation

## [◆ ](#gabb6193b8d15b33e5c739c9609376950f)cobs\_decode()

| int cobs\_decode | ( | struct [net\_buf](structnet__buf.md) \* | *src*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

`#include <[zephyr/data/cobs.h](cobs_8h.md)>`

Standard COBS decoding.

Parameters
:   | src | Source buffer to decode |
    | --- | --- |
    | dst | Destination buffer for decoded data |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Decoding flags (reserved) |

Return values
:   | 0 | Success |
    | --- | --- |
    | -ENOMEM | Insufficient destination space |
    | -EINVAL | Invalid COBS structure or parameters |

## [◆ ](#gadf39d47a13fe1e3b10bcc9208f5b4786)cobs\_encode()

| int cobs\_encode | ( | struct [net\_buf](structnet__buf.md) \* | *src*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *dst*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) |

`#include <[zephyr/data/cobs.h](cobs_8h.md)>`

Standard COBS encoding.

Parameters
:   | src | Source buffer to decode |
    | --- | --- |
    | dst | Destination buffer for decoded data |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Decoding flags (reserved) |

Return values
:   | 0 | Success |
    | --- | --- |
    | -ENOMEM | Insufficient destination space |
    | -EINVAL | Invalid COBS structure or parameters |

## [◆ ](#ga71047f135e408e95d83828e898e823b0)cobs\_max\_encoded\_len()

| | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) cobs\_max\_encoded\_len | ( | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *decoded\_size*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[zephyr/data/cobs.h](cobs_8h.md)>`

Calculate maximum encoded buffer size.

Parameters
:   | decoded\_size | Size of input data to be encoded |
    | --- | --- |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | COBS\_FLAG\_TRAILING\_DELIMITER to include termination byte in calculation |

Returns
:   Required buffer size for worst-case encoding scenario

- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
