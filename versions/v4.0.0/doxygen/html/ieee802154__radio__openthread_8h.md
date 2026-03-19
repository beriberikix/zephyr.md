---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ieee802154__radio__openthread_8h.html
original_path: doxygen/html/ieee802154__radio__openthread_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_radio\_openthread.h File Reference

This file extends interface of [ieee802154\_radio.h](ieee802154__radio_8h.md "Public IEEE 802.15.4 Driver API.") for OpenThread.
[More...](#details)

`#include <[zephyr/net/ieee802154_radio.h](ieee802154__radio_8h_source.md)>`

[Go to the source code of this file.](ieee802154__radio__openthread_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ieee802154\_openthread\_config](structieee802154__openthread__config.md) |
|  | OpenThread specific configuration data of ieee802154 driver. [More...](structieee802154__openthread__config.md#details) |
| struct | [ieee802154\_openthread\_attr\_value](structieee802154__openthread__attr__value.md) |
|  | OpenThread specific attribute value data of ieee802154 driver. [More...](structieee802154__openthread__attr__value.md#details) |

| Macros | |
| --- | --- |
| #define | [IEEE802154\_OPENTHREAD\_THREAD\_IE\_VENDOR\_OUI](#a3df2b5a9df519084df0ecdcb42a81d45)   { 0x9b, 0xb8, 0xea } |
|  | Thread vendor OUI for vendor specific header or nested information elements, see IEEE 802.15.4-2020, sections 7.4.2.2 and 7.4.4.30. |
| #define | [IEEE802154\_OPENTHREAD\_VENDOR\_OUI\_LEN](#a449d47ac13847e40a978a6fd80d5faed)   3 |
|  | length of IEEE 802.15.4-2020 vendor OUIs |

| Enumerations | |
| --- | --- |
| enum | [ieee802154\_openthread\_hw\_caps](#a80bc0d04ae7e2286abe372df49880ac8) { [IEEE802154\_OPENTHREAD\_HW\_MULTIPLE\_CCA](#a80bc0d04ae7e2286abe372df49880ac8a9a1663d68026c5156a0f127ae086adc8) = BIT(IEEE802154\_HW\_CAPS\_BITS\_PRIV\_START) } |
|  | OpenThread specific capabilities of ieee802154 driver. [More...](#a80bc0d04ae7e2286abe372df49880ac8) |
| enum | [ieee802154\_openthread\_tx\_mode](#a038a7e158a73533b1fd55bb92e5fa64a) { [IEEE802154\_OPENTHREAD\_TX\_MODE\_TXTIME\_MULTIPLE\_CCA](#a038a7e158a73533b1fd55bb92e5fa64aa75f9fb57cf10207c5142a86552cb401f) = IEEE802154\_TX\_MODE\_PRIV\_START } |
|  | TX mode. [More...](#a038a7e158a73533b1fd55bb92e5fa64a) |
| enum | [ieee802154\_openthread\_config\_type](#ab11e7d5ec46577a0259d68349ac19525) { [IEEE802154\_OPENTHREAD\_CONFIG\_MAX\_EXTRA\_CCA\_ATTEMPTS](#ab11e7d5ec46577a0259d68349ac19525ac06ead66659fa9a736d368a9d255bc95) = IEEE802154\_CONFIG\_PRIV\_START } |
|  | OpenThread specific configuration types of ieee802154 driver. [More...](#ab11e7d5ec46577a0259d68349ac19525) |
| enum | [ieee802154\_openthread\_attr](#a15a4b5a53be4b2c867eb9551de7d914a) { [IEEE802154\_OPENTHREAD\_ATTR\_T\_RECCA](#a15a4b5a53be4b2c867eb9551de7d914aa4d92697c08b14201465db37b302c2fa5) = IEEE802154\_ATTR\_PRIV\_START , [IEEE802154\_OPENTHREAD\_ATTR\_T\_CCATX](#a15a4b5a53be4b2c867eb9551de7d914aa0e68340300b0e2d29811289fa7c1987b) } |
|  | OpenThread specific attributes of ieee802154 driver. [More...](#a15a4b5a53be4b2c867eb9551de7d914a) |

## Detailed Description

This file extends interface of [ieee802154\_radio.h](ieee802154__radio_8h.md "Public IEEE 802.15.4 Driver API.") for OpenThread.

## Macro Definition Documentation

## [◆ ](#a3df2b5a9df519084df0ecdcb42a81d45)IEEE802154\_OPENTHREAD\_THREAD\_IE\_VENDOR\_OUI

| #define IEEE802154\_OPENTHREAD\_THREAD\_IE\_VENDOR\_OUI   { 0x9b, 0xb8, 0xea } |
| --- |

Thread vendor OUI for vendor specific header or nested information elements, see IEEE 802.15.4-2020, sections 7.4.2.2 and 7.4.4.30.

in little endian

## [◆ ](#a449d47ac13847e40a978a6fd80d5faed)IEEE802154\_OPENTHREAD\_VENDOR\_OUI\_LEN

| #define IEEE802154\_OPENTHREAD\_VENDOR\_OUI\_LEN   3 |
| --- |

length of IEEE 802.15.4-2020 vendor OUIs

## Enumeration Type Documentation

## [◆ ](#a15a4b5a53be4b2c867eb9551de7d914a)ieee802154\_openthread\_attr

| enum [ieee802154\_openthread\_attr](#a15a4b5a53be4b2c867eb9551de7d914a) |
| --- |

OpenThread specific attributes of ieee802154 driver.

This type extends [ieee802154\_attr](group__ieee802154__driver.md#gaf4deddd3f23ebfd65fa47c5d62634430 "ieee802154_attr")

| Enumerator | |
| --- | --- |
| IEEE802154\_OPENTHREAD\_ATTR\_T\_RECCA | Attribute: Maximum time between consecutive CCAs performed back-to-back.  This is attribute for T\_recca parameter mentioned for [IEEE802154\_OPENTHREAD\_TX\_MODE\_TXTIME\_MULTIPLE\_CCA](#a038a7e158a73533b1fd55bb92e5fa64aa75f9fb57cf10207c5142a86552cb401f). Time is expressed in microseconds. |
| IEEE802154\_OPENTHREAD\_ATTR\_T\_CCATX | Attribute: Maximum time between detection of CCA idle channel and the moment of start of SHR at the local antenna.  This is attribute for T\_ccatx parameter mentioned for [IEEE802154\_OPENTHREAD\_TX\_MODE\_TXTIME\_MULTIPLE\_CCA](#a038a7e158a73533b1fd55bb92e5fa64aa75f9fb57cf10207c5142a86552cb401f). Time is expressed in microseconds. |

## [◆ ](#ab11e7d5ec46577a0259d68349ac19525)ieee802154\_openthread\_config\_type

| enum [ieee802154\_openthread\_config\_type](#ab11e7d5ec46577a0259d68349ac19525) |
| --- |

OpenThread specific configuration types of ieee802154 driver.

This type extends [ieee802154\_config\_type](group__ieee802154__driver.md#ga34aecc5996174a812b295a3a4693ad09 "ieee802154_config_type").

| Enumerator | |
| --- | --- |
| IEEE802154\_OPENTHREAD\_CONFIG\_MAX\_EXTRA\_CCA\_ATTEMPTS | Allows to configure extra CCA for transmission requested with mode [IEEE802154\_OPENTHREAD\_TX\_MODE\_TXTIME\_MULTIPLE\_CCA](#a038a7e158a73533b1fd55bb92e5fa64aa75f9fb57cf10207c5142a86552cb401f).  Requires IEEE802154\_OPENTHREAD\_HW\_MULTIPLE\_CCA capability. |

## [◆ ](#a80bc0d04ae7e2286abe372df49880ac8)ieee802154\_openthread\_hw\_caps

| enum [ieee802154\_openthread\_hw\_caps](#a80bc0d04ae7e2286abe372df49880ac8) |
| --- |

OpenThread specific capabilities of ieee802154 driver.

This type extends [ieee802154\_hw\_caps](group__ieee802154__driver.md#gaf99cda89c29df3c0088fc57ec09cbcd4 "ieee802154_hw_caps").

| Enumerator | |
| --- | --- |
| IEEE802154\_OPENTHREAD\_HW\_MULTIPLE\_CCA | Capability to transmit with [IEEE802154\_OPENTHREAD\_TX\_MODE\_TXTIME\_MULTIPLE\_CCA](#a038a7e158a73533b1fd55bb92e5fa64aa75f9fb57cf10207c5142a86552cb401f) mode. |

## [◆ ](#a038a7e158a73533b1fd55bb92e5fa64a)ieee802154\_openthread\_tx\_mode

| enum [ieee802154\_openthread\_tx\_mode](#a038a7e158a73533b1fd55bb92e5fa64a) |
| --- |

TX mode.

| Enumerator | |
| --- | --- |
| IEEE802154\_OPENTHREAD\_TX\_MODE\_TXTIME\_MULTIPLE\_CCA | The [IEEE802154\_OPENTHREAD\_TX\_MODE\_TXTIME\_MULTIPLE\_CCA](#a038a7e158a73533b1fd55bb92e5fa64aa75f9fb57cf10207c5142a86552cb401f) mode allows to send a scheduled packet if the channel is reported idle after at most 1 + max\_extra\_cca\_attempts CCAs performed back-to-back.  This mode is a non-standard experimental OpenThread feature. It allows transmission of a packet within a certain time window. The earliest transmission time is specified as in the other TXTIME modes: When the first CCA reports an idle channel then the first symbol of the packet's PHR SHALL be present at the local antenna at the time represented by the scheduled TX timestamp (referred to as T\_tx below).  If the first CCA reports a busy channel, then additional CCAs up to max\_extra\_cca\_attempts will be done until one of them reports an idle channel and the packet is sent out or the max number of attempts is reached in which case the transmission fails.  The timing of these additional CCAs depends on the capabilities of the driver which reports them in the T\_recca and T\_ccatx driver attributes (see [IEEE802154\_OPENTHREAD\_ATTR\_T\_RECCA](#a15a4b5a53be4b2c867eb9551de7d914aa4d92697c08b14201465db37b302c2fa5) and [IEEE802154\_OPENTHREAD\_ATTR\_T\_CCATX](#a15a4b5a53be4b2c867eb9551de7d914aa0e68340300b0e2d29811289fa7c1987b)). Based on these attributes the upper layer can calculate the latest point in time (T\_txmax) that the first symbol of the scheduled packet's PHR SHALL be present at the local antenna:  T\_maxtxdelay = max\_extra\_cca\_attempts \* (aCcaTime + T\_recca) - T\_recca + T\_ccatx T\_txmax = T\_tx + T\_maxtxdelay  See IEEE 802.15.4-2020, section 11.3, table 11-1 for the definition of aCcaTime.  Drivers implementing this TX mode SHOULD keep T\_recca and T\_ccatx as short as possible. T\_ccatx SHALL be less than or equal aTurnaroundTime as defined in ibid., section 11.3, table 11-1.  CCA SHALL be executed as defined by the phyCcaMode PHY PIB attribute (see ibid., section 11.3, table 11-2).  Requires IEEE802154\_OPENTHREAD\_HW\_MULTIPLE\_CCA capability.  Note  Capability [IEEE802154\_HW\_SELECTIVE\_TXCHANNEL](group__ieee802154__driver.md#ggaf99cda89c29df3c0088fc57ec09cbcd4ab6cf4f3552d6193027a538a13b95952e "IEEE802154_HW_SELECTIVE_TXCHANNEL") applies as for [IEEE802154\_TX\_MODE\_TXTIME\_CCA](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225da42b4589afb2180fde053fdbbf58c0d3e "IEEE802154_TX_MODE_TXTIME_CCA"). |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ieee802154\_radio\_openthread.h](ieee802154__radio__openthread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
