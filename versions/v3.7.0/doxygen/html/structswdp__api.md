---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structswdp__api.html
original_path: doxygen/html/structswdp__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

swdp\_api Struct Reference

`#include <[swdp.h](swdp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [swdp\_output\_sequence](#a4a4e268bc2e80b0fa3af76c8fb6d70c7) )(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Write count bits to SWDIO from data LSB first. |
| int(\* | [swdp\_input\_sequence](#a0480ec7f5479382457ac2e9c264e46f4) )(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Read count bits from SWDIO into data LSB first. |
| int(\* | [swdp\_transfer](#a3b2a89ee837aae3731ba0d2ba8c1c323) )(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) request, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) idle\_cycles, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*response) |
|  | Perform SWDP transfer and store response. |
| int(\* | [swdp\_set\_pins](#af83ae99fb199d5506256c13aec92f1a7) )(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pins, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
|  | Set SWCLK, SWDPIO, and nRESET pins state. |
| int(\* | [swdp\_get\_pins](#ac0e08f227a18d087fa98894caa277282) )(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Get SWCLK, SWDPIO, and nRESET pins state. |
| int(\* | [swdp\_set\_clock](#aba201f47bb6037334b3da19d17ea7349) )(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) clock) |
|  | Set SWDP clock frequency. |
| int(\* | [swdp\_configure](#a62b5b2285bdec6d9e6069f1671ad1bc3) )(const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) turnaround, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) data\_phase) |
|  | Configure SWDP interface. |
| int(\* | [swdp\_port\_on](#a642cd297ace3437669be092ca4061911) )(const struct [device](structdevice.md) \*dev) |
|  | Enable interface, set pins to default state. |
| int(\* | [swdp\_port\_off](#aa7e408b542b1bd9134b86f2a257cf004) )(const struct [device](structdevice.md) \*dev) |
|  | Disable interface, set pins to High-Z mode. |

## Field Documentation

## [◆ ](#a62b5b2285bdec6d9e6069f1671ad1bc3)swdp\_configure

| int(\* swdp\_api::swdp\_configure) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) turnaround, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) data\_phase) |
| --- |

Configure SWDP interface.

Parameters
:   | dev | SWDP device |
    | --- | --- |
    | turnaround | Line turnaround cycles |
    | data\_phase | Always generate Data Phase (also on WAIT/FAULT) |

Returns
:   0 on success, or error code

## [◆ ](#ac0e08f227a18d087fa98894caa277282)swdp\_get\_pins

| int(\* swdp\_api::swdp\_get\_pins) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
| --- |

Get SWCLK, SWDPIO, and nRESET pins state.

Note
:   The bit positions are defined by the SWDP\_\*\_PIN macros.

Parameters
:   | dev | SWDP device |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | Place to store pins state |

Returns
:   0 on success, or error code

## [◆ ](#a0480ec7f5479382457ac2e9c264e46f4)swdp\_input\_sequence

| int(\* swdp\_api::swdp\_input\_sequence) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
| --- |

Read count bits from SWDIO into data LSB first.

Parameters
:   | dev | SWDP device |
    | --- | --- |
    | count | Number of bits to read |
    | data | Buffer to store bits read |

Returns
:   0 on success, or error code

## [◆ ](#a4a4e268bc2e80b0fa3af76c8fb6d70c7)swdp\_output\_sequence

| int(\* swdp\_api::swdp\_output\_sequence) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
| --- |

Write count bits to SWDIO from data LSB first.

Parameters
:   | dev | SWDP device |
    | --- | --- |
    | count | Number of bits to write |
    | data | Bits to write |

Returns
:   0 on success, or error code

## [◆ ](#aa7e408b542b1bd9134b86f2a257cf004)swdp\_port\_off

| int(\* swdp\_api::swdp\_port\_off) (const struct [device](structdevice.md) \*dev) |
| --- |

Disable interface, set pins to High-Z mode.

Parameters
:   | dev | SWDP device |
    | --- | --- |

Returns
:   0 on success, or error code

## [◆ ](#a642cd297ace3437669be092ca4061911)swdp\_port\_on

| int(\* swdp\_api::swdp\_port\_on) (const struct [device](structdevice.md) \*dev) |
| --- |

Enable interface, set pins to default state.

Note
:   SWDPIO is set to output mode, SWCLK and nRESET are set to high level.

Parameters
:   | dev | SWDP device |
    | --- | --- |

Returns
:   0 on success, or error code

## [◆ ](#aba201f47bb6037334b3da19d17ea7349)swdp\_set\_clock

| int(\* swdp\_api::swdp\_set\_clock) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) clock) |
| --- |

Set SWDP clock frequency.

Parameters
:   | dev | SWDP device |
    | --- | --- |
    | clock | Clock frequency in Hz |

Returns
:   0 on success, or error code

## [◆ ](#af83ae99fb199d5506256c13aec92f1a7)swdp\_set\_pins

| int(\* swdp\_api::swdp\_set\_pins) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pins, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) value) |
| --- |

Set SWCLK, SWDPIO, and nRESET pins state.

Note
:   The bit positions are defined by the SWDP\_\*\_PIN macros.

Parameters
:   | dev | SWDP device |
    | --- | --- |
    | pins | Bitmask of pins to set |
    | value | Value to set pins to |

Returns
:   0 on success, or error code

## [◆ ](#a3b2a89ee837aae3731ba0d2ba8c1c323)swdp\_transfer

| int(\* swdp\_api::swdp\_transfer) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) request, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) idle\_cycles, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*response) |
| --- |

Perform SWDP transfer and store response.

Parameters
:   | dev | SWDP device |
    | --- | --- |
    | request | SWDP request bits |
    | data | Data to be transferred with request |
    | idle\_cycles | Idle cycles between request and response |
    | response | Buffer to store response (ACK/WAIT/FAULT) |

Returns
:   0 on success, or error code

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[swdp.h](swdp_8h_source.md)

- [swdp\_api](structswdp__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
