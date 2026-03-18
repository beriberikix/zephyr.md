---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structlorawan__downlink__cb.html
original_path: doxygen/html/structlorawan__downlink__cb.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lorawan\_downlink\_cb Struct Reference

[Connectivity](group__connectivity.md) » [LoRaWAN APIs](group__lorawan__api.md)

LoRaWAN downlink callback parameters.
[More...](#details)

`#include <[lorawan.h](lorawan_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [port](#a0479e13faf06b99cf9023ebed8022131) |
|  | Port to handle messages for. |
| void(\* | [cb](#adee407633f1c6fa35178769cb9355178) )([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [port](#a0479e13faf06b99cf9023ebed8022131), [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) data\_pending, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) rssi, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) snr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Callback function to run on downlink data. |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#ad54df4a4ab38003d59f82b19fb16f5fd) |
|  | Node for callback list. |

## Detailed Description

LoRaWAN downlink callback parameters.

## Field Documentation

## [◆ ](#adee407633f1c6fa35178769cb9355178)cb

| void(\* lorawan\_downlink\_cb::cb) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [port](#a0479e13faf06b99cf9023ebed8022131), [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) data\_pending, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) rssi, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) snr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
| --- |

Callback function to run on downlink data.

Note
:   Callbacks are run on the system workqueue, and should therefore be as short as possible.

Parameters
:   | [port](#a0479e13faf06b99cf9023ebed8022131) | Port message was sent on |
    | --- | --- |
    | data\_pending | Network server has more downlink packets pending |
    | rssi | Received signal strength in dBm |
    | snr | Signal to Noise ratio in dBm |
    | len | Length of data received, will be 0 for ACKs |
    | data | Data received, will be NULL for ACKs |

## [◆ ](#ad54df4a4ab38003d59f82b19fb16f5fd)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) lorawan\_downlink\_cb::node |
| --- |

Node for callback list.

## [◆ ](#a0479e13faf06b99cf9023ebed8022131)port

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lorawan\_downlink\_cb::port |
| --- |

Port to handle messages for.

- Port 0: TX packet acknowledgements
- Ports 1-255: Standard downlink port
- LW\_RECV\_PORT\_ANY: All downlinks

---

The documentation for this struct was generated from the following file:

- zephyr/lorawan/[lorawan.h](lorawan_8h_source.md)

- [lorawan\_downlink\_cb](structlorawan__downlink__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
