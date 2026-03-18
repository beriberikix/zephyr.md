---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structieee802154__openthread__config.html
original_path: doxygen/html/structieee802154__openthread__config.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_openthread\_config Struct Reference

OpenThread specific configuration data of ieee802154 driver.
[More...](#details)

`#include <[ieee802154_radio_openthread.h](ieee802154__radio__openthread_8h_source.md)>`

| Data Fields | |
| --- | --- |
| union { |  |
| struct [ieee802154\_config](structieee802154__config.md)   [common](#ab18500f5926c8fb0bb068aca86b169d4) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [max\_extra\_cca\_attempts](#ab4cbfdddf55a95958b9df1c0f9ac70f9) |  |
|  | [IEEE802154\_OPENTHREAD\_CONFIG\_MAX\_EXTRA\_CCA\_ATTEMPTS](ieee802154__radio__openthread_8h.md#ab11e7d5ec46577a0259d68349ac19525ac06ead66659fa9a736d368a9d255bc95 "Allows to configure extra CCA for transmission requested with mode IEEE802154_OPENTHREAD_TX_MODE_TXTI...") [More...](#ab4cbfdddf55a95958b9df1c0f9ac70f9) |
| }; |  |

## Detailed Description

OpenThread specific configuration data of ieee802154 driver.

## Field Documentation

## [◆ ](#ab55c167032b6a9f85036ee809e442f04)[union]

| union { ... } [ieee802154\_openthread\_config](structieee802154__openthread__config.md) |
| --- |

## [◆ ](#ab18500f5926c8fb0bb068aca86b169d4)common

| struct [ieee802154\_config](structieee802154__config.md) ieee802154\_openthread\_config::common |
| --- |

## [◆ ](#ab4cbfdddf55a95958b9df1c0f9ac70f9)max\_extra\_cca\_attempts

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ieee802154\_openthread\_config::max\_extra\_cca\_attempts |
| --- |

[IEEE802154\_OPENTHREAD\_CONFIG\_MAX\_EXTRA\_CCA\_ATTEMPTS](ieee802154__radio__openthread_8h.md#ab11e7d5ec46577a0259d68349ac19525ac06ead66659fa9a736d368a9d255bc95 "Allows to configure extra CCA for transmission requested with mode IEEE802154_OPENTHREAD_TX_MODE_TXTI...")

The maximum number of extra CCAs to be performed when transmission is requested with mode [IEEE802154\_OPENTHREAD\_TX\_MODE\_TXTIME\_MULTIPLE\_CCA](ieee802154__radio__openthread_8h.md#a038a7e158a73533b1fd55bb92e5fa64aa75f9fb57cf10207c5142a86552cb401f "IEEE802154_OPENTHREAD_TX_MODE_TXTIME_MULTIPLE_CCA").

---

The documentation for this struct was generated from the following file:

- zephyr/net/[ieee802154\_radio\_openthread.h](ieee802154__radio__openthread_8h_source.md)

- [ieee802154\_openthread\_config](structieee802154__openthread__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
