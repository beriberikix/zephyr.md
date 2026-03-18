---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structlora__modem__config.html
original_path: doxygen/html/structlora__modem__config.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lora\_modem\_config Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [LoRa APIs](group__lora__api.md)

Structure containing the configuration of a LoRa modem.
[More...](#details)

`#include <[lora.h](lora_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [frequency](#a08209a2dabc5111025810fc8e141c2df) |
|  | Frequency in Hz to use for transceiving. |
| enum [lora\_signal\_bandwidth](group__lora__api.md#gabb5feb9d1a2bb160d9b55939efb17136) | [bandwidth](#a0c6a90e31b4a97d962af3dbd0ee8e885) |
|  | The bandwidth to use for transceiving. |
| enum [lora\_datarate](group__lora__api.md#ga30bfeb2e6f4e35869996b597b614becb) | [datarate](#ae438c1c223f12fc6c3747d4297ec61ba) |
|  | The data-rate to use for transceiving. |
| enum [lora\_coding\_rate](group__lora__api.md#ga5af378491814d0d3a059cd6cd39265c8) | [coding\_rate](#a8e47a8506265562c7b118fab72cceb10) |
|  | The coding rate to use for transceiving. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [preamble\_len](#a9d0795c5be6ae0042babaa05615cf7f2) |
|  | Length of the preamble. |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [tx\_power](#a41a194d62e1e3e1b142e194a75efb8a1) |
|  | TX-power in dBm to use for transmission. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [tx](#a10b12a2092712050bdd64c6250c8731f) |
|  | Set to true for transmission, false for receiving. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [iq\_inverted](#a5737749b3bd29515887bb0b8c48c8bd1) |
|  | Invert the In-Phase and Quadrature (IQ) signals. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [public\_network](#af97fde1f5f40a4d702c0140872728e86) |
|  | Sets the sync-byte to use: |

## Detailed Description

Structure containing the configuration of a LoRa modem.

## Field Documentation

## [◆ ](#a0c6a90e31b4a97d962af3dbd0ee8e885)bandwidth

| enum [lora\_signal\_bandwidth](group__lora__api.md#gabb5feb9d1a2bb160d9b55939efb17136) lora\_modem\_config::bandwidth |
| --- |

The bandwidth to use for transceiving.

## [◆ ](#a8e47a8506265562c7b118fab72cceb10)coding\_rate

| enum [lora\_coding\_rate](group__lora__api.md#ga5af378491814d0d3a059cd6cd39265c8) lora\_modem\_config::coding\_rate |
| --- |

The coding rate to use for transceiving.

## [◆ ](#ae438c1c223f12fc6c3747d4297ec61ba)datarate

| enum [lora\_datarate](group__lora__api.md#ga30bfeb2e6f4e35869996b597b614becb) lora\_modem\_config::datarate |
| --- |

The data-rate to use for transceiving.

## [◆ ](#a08209a2dabc5111025810fc8e141c2df)frequency

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) lora\_modem\_config::frequency |
| --- |

Frequency in Hz to use for transceiving.

## [◆ ](#a5737749b3bd29515887bb0b8c48c8bd1)iq\_inverted

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) lora\_modem\_config::iq\_inverted |
| --- |

Invert the In-Phase and Quadrature (IQ) signals.

Normally this should be set to false. In advanced use-cases where a differentation is needed between "uplink" and "downlink" traffic, the IQ can be inverted to create two different channels on the same frequency

## [◆ ](#a9d0795c5be6ae0042babaa05615cf7f2)preamble\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lora\_modem\_config::preamble\_len |
| --- |

Length of the preamble.

## [◆ ](#af97fde1f5f40a4d702c0140872728e86)public\_network

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) lora\_modem\_config::public\_network |
| --- |

Sets the sync-byte to use:

- false: for using the private network sync-byte
- true: for using the public network sync-byte The public network sync-byte is only intended for advanced usage. Normally the private network sync-byte should be used for peer to peer communications and the LoRaWAN APIs should be used for interacting with a public network.

## [◆ ](#a10b12a2092712050bdd64c6250c8731f)tx

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) lora\_modem\_config::tx |
| --- |

Set to true for transmission, false for receiving.

## [◆ ](#a41a194d62e1e3e1b142e194a75efb8a1)tx\_power

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) lora\_modem\_config::tx\_power |
| --- |

TX-power in dBm to use for transmission.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[lora.h](lora_8h_source.md)

- [lora\_modem\_config](structlora__modem__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
