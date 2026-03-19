---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ieee802154__radio__openthread_8h_source.html
original_path: doxygen/html/ieee802154__radio__openthread_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ieee802154\_radio\_openthread.h

[Go to the documentation of this file.](ieee802154__radio__openthread_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_IEEE802154\_RADIO\_OPENTHREAD\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_IEEE802154\_RADIO\_OPENTHREAD\_H\_

14

15#include <[zephyr/net/ieee802154\_radio.h](ieee802154__radio_8h.md)>

16

[ 21](ieee802154__radio__openthread_8h.md#a80bc0d04ae7e2286abe372df49880ac8)enum [ieee802154\_openthread\_hw\_caps](ieee802154__radio__openthread_8h.md#a80bc0d04ae7e2286abe372df49880ac8) {

[ 25](ieee802154__radio__openthread_8h.md#a80bc0d04ae7e2286abe372df49880ac8a9a1663d68026c5156a0f127ae086adc8) [IEEE802154\_OPENTHREAD\_HW\_MULTIPLE\_CCA](ieee802154__radio__openthread_8h.md#a80bc0d04ae7e2286abe372df49880ac8a9a1663d68026c5156a0f127ae086adc8) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([IEEE802154\_HW\_CAPS\_BITS\_PRIV\_START](group__ieee802154__driver.md#ga40912ccb268768b4e96ce9cad35476af)),

26};

27

[ 29](ieee802154__radio__openthread_8h.md#a038a7e158a73533b1fd55bb92e5fa64a)enum [ieee802154\_openthread\_tx\_mode](ieee802154__radio__openthread_8h.md#a038a7e158a73533b1fd55bb92e5fa64a) {

[ 71](ieee802154__radio__openthread_8h.md#a038a7e158a73533b1fd55bb92e5fa64aa75f9fb57cf10207c5142a86552cb401f) [IEEE802154\_OPENTHREAD\_TX\_MODE\_TXTIME\_MULTIPLE\_CCA](ieee802154__radio__openthread_8h.md#a038a7e158a73533b1fd55bb92e5fa64aa75f9fb57cf10207c5142a86552cb401f) = [IEEE802154\_TX\_MODE\_PRIV\_START](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225dabbab0c864f313ee4045e5ad59ea774e2)

72};

73

[ 78](ieee802154__radio__openthread_8h.md#ab11e7d5ec46577a0259d68349ac19525)enum [ieee802154\_openthread\_config\_type](ieee802154__radio__openthread_8h.md#ab11e7d5ec46577a0259d68349ac19525) {

[ 83](ieee802154__radio__openthread_8h.md#ab11e7d5ec46577a0259d68349ac19525ac06ead66659fa9a736d368a9d255bc95) [IEEE802154\_OPENTHREAD\_CONFIG\_MAX\_EXTRA\_CCA\_ATTEMPTS](ieee802154__radio__openthread_8h.md#ab11e7d5ec46577a0259d68349ac19525ac06ead66659fa9a736d368a9d255bc95) = [IEEE802154\_CONFIG\_PRIV\_START](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a1653b2869208045415d83fc6708d015c)

84};

85

[ 92](ieee802154__radio__openthread_8h.md#a3df2b5a9df519084df0ecdcb42a81d45)#define IEEE802154\_OPENTHREAD\_THREAD\_IE\_VENDOR\_OUI { 0x9b, 0xb8, 0xea }

93

[ 95](ieee802154__radio__openthread_8h.md#a449d47ac13847e40a978a6fd80d5faed)#define IEEE802154\_OPENTHREAD\_VENDOR\_OUI\_LEN 3

96

[ 98](structieee802154__openthread__config.md)struct [ieee802154\_openthread\_config](structieee802154__openthread__config.md) {

99 union {

[ 101](structieee802154__openthread__config.md#ab18500f5926c8fb0bb068aca86b169d4) struct [ieee802154\_config](structieee802154__config.md) [common](structieee802154__openthread__config.md#ab18500f5926c8fb0bb068aca86b169d4);

102

[ 108](structieee802154__openthread__config.md#ab4cbfdddf55a95958b9df1c0f9ac70f9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_extra\_cca\_attempts](structieee802154__openthread__config.md#ab4cbfdddf55a95958b9df1c0f9ac70f9);

109 };

110};

111

[ 116](ieee802154__radio__openthread_8h.md#a15a4b5a53be4b2c867eb9551de7d914a)enum [ieee802154\_openthread\_attr](ieee802154__radio__openthread_8h.md#a15a4b5a53be4b2c867eb9551de7d914a) {

117

[ 124](ieee802154__radio__openthread_8h.md#a15a4b5a53be4b2c867eb9551de7d914aa4d92697c08b14201465db37b302c2fa5) [IEEE802154\_OPENTHREAD\_ATTR\_T\_RECCA](ieee802154__radio__openthread_8h.md#a15a4b5a53be4b2c867eb9551de7d914aa4d92697c08b14201465db37b302c2fa5) = [IEEE802154\_ATTR\_PRIV\_START](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430ad4912dc68abc1abe54bc212f023bf511),

125

[ 133](ieee802154__radio__openthread_8h.md#a15a4b5a53be4b2c867eb9551de7d914aa0e68340300b0e2d29811289fa7c1987b) [IEEE802154\_OPENTHREAD\_ATTR\_T\_CCATX](ieee802154__radio__openthread_8h.md#a15a4b5a53be4b2c867eb9551de7d914aa0e68340300b0e2d29811289fa7c1987b)

134};

135

[ 140](structieee802154__openthread__attr__value.md)struct [ieee802154\_openthread\_attr\_value](structieee802154__openthread__attr__value.md) {

141 union {

[ 143](structieee802154__openthread__attr__value.md#a794c867bf25cd23b9b1797d995696c8a) struct [ieee802154\_attr\_value](structieee802154__attr__value.md) [common](structieee802154__openthread__attr__value.md#a794c867bf25cd23b9b1797d995696c8a);

144

[ 146](structieee802154__openthread__attr__value.md#a84f1a03b847ff2050f38a59573a00cd8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_recca](structieee802154__openthread__attr__value.md#a84f1a03b847ff2050f38a59573a00cd8);

147

[ 149](structieee802154__openthread__attr__value.md#a423bc2cc48ceead6a6febd7f78504843) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [t\_ccatx](structieee802154__openthread__attr__value.md#a423bc2cc48ceead6a6febd7f78504843);

150

151 };

152};

153

154#endif /\* ZEPHYR\_INCLUDE\_NET\_IEEE802154\_RADIO\_OPENTHREAD\_H\_ \*/

[IEEE802154\_HW\_CAPS\_BITS\_PRIV\_START](group__ieee802154__driver.md#ga40912ccb268768b4e96ce9cad35476af)

#define IEEE802154\_HW\_CAPS\_BITS\_PRIV\_START

This and higher values are specific to the protocol- or driver-specific extensions.

**Definition** ieee802154\_radio.h:545

[IEEE802154\_CONFIG\_PRIV\_START](group__ieee802154__driver.md#gga34aecc5996174a812b295a3a4693ad09a1653b2869208045415d83fc6708d015c)

@ IEEE802154\_CONFIG\_PRIV\_START

This and higher values are specific to the protocol- or driver-specific extensions.

**Definition** ieee802154\_radio.h:1120

[IEEE802154\_TX\_MODE\_PRIV\_START](group__ieee802154__driver.md#ggab2bee8752291e082cb277145cef1225dabbab0c864f313ee4045e5ad59ea774e2)

@ IEEE802154\_TX\_MODE\_PRIV\_START

This and higher values are specific to the protocol- or driver-specific extensions.

**Definition** ieee802154\_radio.h:662

[IEEE802154\_ATTR\_PRIV\_START](group__ieee802154__driver.md#ggaf4deddd3f23ebfd65fa47c5d62634430ad4912dc68abc1abe54bc212f023bf511)

@ IEEE802154\_ATTR\_PRIV\_START

This and higher values are specific to the protocol- or driver-specific extensions.

**Definition** ieee802154\_radio.h:1312

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ieee802154\_radio.h](ieee802154__radio_8h.md)

Public IEEE 802.15.4 Driver API.

[ieee802154\_openthread\_tx\_mode](ieee802154__radio__openthread_8h.md#a038a7e158a73533b1fd55bb92e5fa64a)

ieee802154\_openthread\_tx\_mode

TX mode.

**Definition** ieee802154\_radio\_openthread.h:29

[IEEE802154\_OPENTHREAD\_TX\_MODE\_TXTIME\_MULTIPLE\_CCA](ieee802154__radio__openthread_8h.md#a038a7e158a73533b1fd55bb92e5fa64aa75f9fb57cf10207c5142a86552cb401f)

@ IEEE802154\_OPENTHREAD\_TX\_MODE\_TXTIME\_MULTIPLE\_CCA

The IEEE802154\_OPENTHREAD\_TX\_MODE\_TXTIME\_MULTIPLE\_CCA mode allows to send a scheduled packet if the c...

**Definition** ieee802154\_radio\_openthread.h:71

[ieee802154\_openthread\_attr](ieee802154__radio__openthread_8h.md#a15a4b5a53be4b2c867eb9551de7d914a)

ieee802154\_openthread\_attr

OpenThread specific attributes of ieee802154 driver.

**Definition** ieee802154\_radio\_openthread.h:116

[IEEE802154\_OPENTHREAD\_ATTR\_T\_CCATX](ieee802154__radio__openthread_8h.md#a15a4b5a53be4b2c867eb9551de7d914aa0e68340300b0e2d29811289fa7c1987b)

@ IEEE802154\_OPENTHREAD\_ATTR\_T\_CCATX

Attribute: Maximum time between detection of CCA idle channel and the moment of start of SHR at the l...

**Definition** ieee802154\_radio\_openthread.h:133

[IEEE802154\_OPENTHREAD\_ATTR\_T\_RECCA](ieee802154__radio__openthread_8h.md#a15a4b5a53be4b2c867eb9551de7d914aa4d92697c08b14201465db37b302c2fa5)

@ IEEE802154\_OPENTHREAD\_ATTR\_T\_RECCA

Attribute: Maximum time between consecutive CCAs performed back-to-back.

**Definition** ieee802154\_radio\_openthread.h:124

[ieee802154\_openthread\_hw\_caps](ieee802154__radio__openthread_8h.md#a80bc0d04ae7e2286abe372df49880ac8)

ieee802154\_openthread\_hw\_caps

OpenThread specific capabilities of ieee802154 driver.

**Definition** ieee802154\_radio\_openthread.h:21

[IEEE802154\_OPENTHREAD\_HW\_MULTIPLE\_CCA](ieee802154__radio__openthread_8h.md#a80bc0d04ae7e2286abe372df49880ac8a9a1663d68026c5156a0f127ae086adc8)

@ IEEE802154\_OPENTHREAD\_HW\_MULTIPLE\_CCA

Capability to transmit with IEEE802154\_OPENTHREAD\_TX\_MODE\_TXTIME\_MULTIPLE\_CCA mode.

**Definition** ieee802154\_radio\_openthread.h:25

[ieee802154\_openthread\_config\_type](ieee802154__radio__openthread_8h.md#ab11e7d5ec46577a0259d68349ac19525)

ieee802154\_openthread\_config\_type

OpenThread specific configuration types of ieee802154 driver.

**Definition** ieee802154\_radio\_openthread.h:78

[IEEE802154\_OPENTHREAD\_CONFIG\_MAX\_EXTRA\_CCA\_ATTEMPTS](ieee802154__radio__openthread_8h.md#ab11e7d5ec46577a0259d68349ac19525ac06ead66659fa9a736d368a9d255bc95)

@ IEEE802154\_OPENTHREAD\_CONFIG\_MAX\_EXTRA\_CCA\_ATTEMPTS

Allows to configure extra CCA for transmission requested with mode IEEE802154\_OPENTHREAD\_TX\_MODE\_TXTI...

**Definition** ieee802154\_radio\_openthread.h:83

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[ieee802154\_attr\_value](structieee802154__attr__value.md)

IEEE 802.15.4 driver attribute values.

**Definition** ieee802154\_radio.h:1328

[ieee802154\_config](structieee802154__config.md)

IEEE 802.15.4 driver configuration data.

**Definition** ieee802154\_radio.h:1140

[ieee802154\_openthread\_attr\_value](structieee802154__openthread__attr__value.md)

OpenThread specific attribute value data of ieee802154 driver.

**Definition** ieee802154\_radio\_openthread.h:140

[ieee802154\_openthread\_attr\_value::t\_ccatx](structieee802154__openthread__attr__value.md#a423bc2cc48ceead6a6febd7f78504843)

uint16\_t t\_ccatx

Attribute value for IEEE802154\_OPENTHREAD\_ATTR\_T\_CCATX.

**Definition** ieee802154\_radio\_openthread.h:149

[ieee802154\_openthread\_attr\_value::common](structieee802154__openthread__attr__value.md#a794c867bf25cd23b9b1797d995696c8a)

struct ieee802154\_attr\_value common

Common attribute value.

**Definition** ieee802154\_radio\_openthread.h:143

[ieee802154\_openthread\_attr\_value::t\_recca](structieee802154__openthread__attr__value.md#a84f1a03b847ff2050f38a59573a00cd8)

uint16\_t t\_recca

Attribute value for IEEE802154\_OPENTHREAD\_ATTR\_T\_RECCA.

**Definition** ieee802154\_radio\_openthread.h:146

[ieee802154\_openthread\_config](structieee802154__openthread__config.md)

OpenThread specific configuration data of ieee802154 driver.

**Definition** ieee802154\_radio\_openthread.h:98

[ieee802154\_openthread\_config::common](structieee802154__openthread__config.md#ab18500f5926c8fb0bb068aca86b169d4)

struct ieee802154\_config common

Common configuration.

**Definition** ieee802154\_radio\_openthread.h:101

[ieee802154\_openthread\_config::max\_extra\_cca\_attempts](structieee802154__openthread__config.md#ab4cbfdddf55a95958b9df1c0f9ac70f9)

uint8\_t max\_extra\_cca\_attempts

IEEE802154\_OPENTHREAD\_CONFIG\_MAX\_EXTRA\_CCA\_ATTEMPTS

**Definition** ieee802154\_radio\_openthread.h:108

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [ieee802154\_radio\_openthread.h](ieee802154__radio__openthread_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
