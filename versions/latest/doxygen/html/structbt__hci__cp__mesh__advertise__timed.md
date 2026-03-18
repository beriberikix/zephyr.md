---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__hci__cp__mesh__advertise__timed.html
original_path: doxygen/html/structbt__hci__cp__mesh__advertise__timed.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_cp\_mesh\_advertise\_timed Struct Reference

`#include <[hci_vs.h](hci__vs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [adv\_slot](#a92f0163ec0854296ab76e49741d45196) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [own\_addr\_type](#ae395b4a53ff9e7af8885b9583562022a) |
| [bt\_addr\_t](structbt__addr__t.md) | [random\_addr](#ada4348480db5f95acaad86bfa2ddbc7e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ch\_map](#aa5bf4322faa354cc6de0c707502b4ed0) |
| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) | [tx\_power](#aae34dd11723383b5559dc102c59213c2) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [retx\_count](#adfb3acf9ea540d8405c5979115053b15) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [retx\_interval](#a6718fd6031b2351eb033333a7302a21b) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [instant](#a85a7e965b8004cac3a4bc0107844c69b) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [tx\_delay](#aee05619f0ed3b79f3bce5676c1f3aa8a) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [tx\_window](#a1a5a5964eeff05fa232543756d234759) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data\_len](#a78ecf7aa6ebf0739a585fed2a8710301) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [data](#ac097c1ee537d9a480ae16205eafc7105) [31] |

## Field Documentation

## [◆ ](#a92f0163ec0854296ab76e49741d45196)adv\_slot

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_mesh\_advertise\_timed::adv\_slot |
| --- |

## [◆ ](#aa5bf4322faa354cc6de0c707502b4ed0)ch\_map

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_mesh\_advertise\_timed::ch\_map |
| --- |

## [◆ ](#ac097c1ee537d9a480ae16205eafc7105)data

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_mesh\_advertise\_timed::data[31] |
| --- |

## [◆ ](#a78ecf7aa6ebf0739a585fed2a8710301)data\_len

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_mesh\_advertise\_timed::data\_len |
| --- |

## [◆ ](#a85a7e965b8004cac3a4bc0107844c69b)instant

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_hci\_cp\_mesh\_advertise\_timed::instant |
| --- |

## [◆ ](#ae395b4a53ff9e7af8885b9583562022a)own\_addr\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_mesh\_advertise\_timed::own\_addr\_type |
| --- |

## [◆ ](#ada4348480db5f95acaad86bfa2ddbc7e)random\_addr

| [bt\_addr\_t](structbt__addr__t.md) bt\_hci\_cp\_mesh\_advertise\_timed::random\_addr |
| --- |

## [◆ ](#adfb3acf9ea540d8405c5979115053b15)retx\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_mesh\_advertise\_timed::retx\_count |
| --- |

## [◆ ](#a6718fd6031b2351eb033333a7302a21b)retx\_interval

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_hci\_cp\_mesh\_advertise\_timed::retx\_interval |
| --- |

## [◆ ](#aee05619f0ed3b79f3bce5676c1f3aa8a)tx\_delay

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_mesh\_advertise\_timed::tx\_delay |
| --- |

## [◆ ](#aae34dd11723383b5559dc102c59213c2)tx\_power

| [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) bt\_hci\_cp\_mesh\_advertise\_timed::tx\_power |
| --- |

## [◆ ](#a1a5a5964eeff05fa232543756d234759)tx\_window

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_hci\_cp\_mesh\_advertise\_timed::tx\_window |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[hci\_vs.h](hci__vs_8h_source.md)

- [bt\_hci\_cp\_mesh\_advertise\_timed](structbt__hci__cp__mesh__advertise__timed.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
