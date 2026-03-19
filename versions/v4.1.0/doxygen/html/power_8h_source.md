---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/power_8h_source.html
original_path: doxygen/html/power_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

power.h

[Go to the documentation of this file.](power_8h.md)

1/\*

2 \* Copyright 2024 NXP

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_POWER\_H\_

13#define \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_POWER\_H\_

14

15#include <[zephyr/drivers/firmware/scmi/protocol.h](protocol_8h.md)>

16

[ 17](power_8h.md#a8c95da0a183bcdde6e6fde5b111d9c22)#define SCMI\_POWER\_STATE\_SET\_FLAGS\_ASYNC BIT(0)

18

[ 25](structscmi__power__state__config.md)struct [scmi\_power\_state\_config](structscmi__power__state__config.md) {

[ 26](structscmi__power__state__config.md#a83743ab1270c319ab62148e2cf89741f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structscmi__power__state__config.md#a83743ab1270c319ab62148e2cf89741f);

[ 27](structscmi__power__state__config.md#ae246faf5674e4d885d84e8ee782cccae) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [domain\_id](structscmi__power__state__config.md#ae246faf5674e4d885d84e8ee782cccae);

[ 28](structscmi__power__state__config.md#a742409967c5487aecbccf89347dd7ae4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [power\_state](structscmi__power__state__config.md#a742409967c5487aecbccf89347dd7ae4);

29};

30

[ 34](power_8h.md#a669e3ff12b5fc6791440e4adb7596293)enum [scmi\_power\_domain\_message](power_8h.md#a669e3ff12b5fc6791440e4adb7596293) {

[ 35](power_8h.md#a669e3ff12b5fc6791440e4adb7596293a92ac48a13aed6415581beab023ef31b8) [SCMI\_POWER\_DOMAIN\_MSG\_PROTOCOL\_VERSION](power_8h.md#a669e3ff12b5fc6791440e4adb7596293a92ac48a13aed6415581beab023ef31b8) = 0x0,

[ 36](power_8h.md#a669e3ff12b5fc6791440e4adb7596293a3457133a86ab6480b10470bb1fe296d3) [SCMI\_POWER\_DOMAIN\_MSG\_PROTOCOL\_ATTRIBUTES](power_8h.md#a669e3ff12b5fc6791440e4adb7596293a3457133a86ab6480b10470bb1fe296d3) = 0x1,

[ 37](power_8h.md#a669e3ff12b5fc6791440e4adb7596293a066426afb042922071675b090fd785f3) [SCMI\_POWER\_DOMAIN\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES](power_8h.md#a669e3ff12b5fc6791440e4adb7596293a066426afb042922071675b090fd785f3) = 0x2,

[ 38](power_8h.md#a669e3ff12b5fc6791440e4adb7596293aefdc40ff9bb0939d37cb631eb2aa7daa) [SCMI\_POWER\_DOMAIN\_MSG\_POWER\_DOMAIN\_ATTRIBUTES](power_8h.md#a669e3ff12b5fc6791440e4adb7596293aefdc40ff9bb0939d37cb631eb2aa7daa) = 0x3,

[ 39](power_8h.md#a669e3ff12b5fc6791440e4adb7596293aab1e51f69264b200fa2df662e7437243) [SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_SET](power_8h.md#a669e3ff12b5fc6791440e4adb7596293aab1e51f69264b200fa2df662e7437243) = 0x4,

[ 40](power_8h.md#a669e3ff12b5fc6791440e4adb7596293aa524b1298afa78395fa4d11e010f2e47) [SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_GET](power_8h.md#a669e3ff12b5fc6791440e4adb7596293aa524b1298afa78395fa4d11e010f2e47) = 0x5,

[ 41](power_8h.md#a669e3ff12b5fc6791440e4adb7596293aa884e44de1912627adcd7b3df08ee145) [SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_NOTIFY](power_8h.md#a669e3ff12b5fc6791440e4adb7596293aa884e44de1912627adcd7b3df08ee145) = 0x6,

[ 42](power_8h.md#a669e3ff12b5fc6791440e4adb7596293ac01e7fde59373798fa0ce78d776c58bc) [SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_CHANGE\_REQEUSTED\_NOTIFY](power_8h.md#a669e3ff12b5fc6791440e4adb7596293ac01e7fde59373798fa0ce78d776c58bc) = 0x7,

[ 43](power_8h.md#a669e3ff12b5fc6791440e4adb7596293a113b5c6493366a21f4874ec25137cd1d) [SCMI\_POWER\_DOMAIN\_MSG\_POWER\_DOMAIN\_NAME\_GET](power_8h.md#a669e3ff12b5fc6791440e4adb7596293a113b5c6493366a21f4874ec25137cd1d) = 0x8,

[ 44](power_8h.md#a669e3ff12b5fc6791440e4adb7596293aee289d3ed8b8a0fbdc4befc92f10fa65) [SCMI\_POWER\_DOMAIN\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION](power_8h.md#a669e3ff12b5fc6791440e4adb7596293aee289d3ed8b8a0fbdc4befc92f10fa65) = 0x10,

45};

46

[ 56](power_8h.md#a0969968c4d6b94868295172c0408031b)int [scmi\_power\_state\_set](power_8h.md#a0969968c4d6b94868295172c0408031b)(struct [scmi\_power\_state\_config](structscmi__power__state__config.md) \*cfg);

[ 66](power_8h.md#adc7a2fbf0c4cab570d3a567ce548c947)int [scmi\_power\_state\_get](power_8h.md#adc7a2fbf0c4cab570d3a567ce548c947)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) domain\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*power\_state);

67

68#endif /\* \_INCLUDE\_ZEPHYR\_DRIVERS\_FIRMWARE\_SCMI\_POWER\_H\_ \*/

[scmi\_power\_state\_set](power_8h.md#a0969968c4d6b94868295172c0408031b)

int scmi\_power\_state\_set(struct scmi\_power\_state\_config \*cfg)

Send the POWER\_STATE\_SET command and get its reply.

[scmi\_power\_domain\_message](power_8h.md#a669e3ff12b5fc6791440e4adb7596293)

scmi\_power\_domain\_message

Power domain protocol command message IDs.

**Definition** power.h:34

[SCMI\_POWER\_DOMAIN\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES](power_8h.md#a669e3ff12b5fc6791440e4adb7596293a066426afb042922071675b090fd785f3)

@ SCMI\_POWER\_DOMAIN\_MSG\_PROTOCOL\_MESSAGE\_ATTRIBUTES

**Definition** power.h:37

[SCMI\_POWER\_DOMAIN\_MSG\_POWER\_DOMAIN\_NAME\_GET](power_8h.md#a669e3ff12b5fc6791440e4adb7596293a113b5c6493366a21f4874ec25137cd1d)

@ SCMI\_POWER\_DOMAIN\_MSG\_POWER\_DOMAIN\_NAME\_GET

**Definition** power.h:43

[SCMI\_POWER\_DOMAIN\_MSG\_PROTOCOL\_ATTRIBUTES](power_8h.md#a669e3ff12b5fc6791440e4adb7596293a3457133a86ab6480b10470bb1fe296d3)

@ SCMI\_POWER\_DOMAIN\_MSG\_PROTOCOL\_ATTRIBUTES

**Definition** power.h:36

[SCMI\_POWER\_DOMAIN\_MSG\_PROTOCOL\_VERSION](power_8h.md#a669e3ff12b5fc6791440e4adb7596293a92ac48a13aed6415581beab023ef31b8)

@ SCMI\_POWER\_DOMAIN\_MSG\_PROTOCOL\_VERSION

**Definition** power.h:35

[SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_GET](power_8h.md#a669e3ff12b5fc6791440e4adb7596293aa524b1298afa78395fa4d11e010f2e47)

@ SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_GET

**Definition** power.h:40

[SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_NOTIFY](power_8h.md#a669e3ff12b5fc6791440e4adb7596293aa884e44de1912627adcd7b3df08ee145)

@ SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_NOTIFY

**Definition** power.h:41

[SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_SET](power_8h.md#a669e3ff12b5fc6791440e4adb7596293aab1e51f69264b200fa2df662e7437243)

@ SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_SET

**Definition** power.h:39

[SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_CHANGE\_REQEUSTED\_NOTIFY](power_8h.md#a669e3ff12b5fc6791440e4adb7596293ac01e7fde59373798fa0ce78d776c58bc)

@ SCMI\_POWER\_DOMAIN\_MSG\_POWER\_STATE\_CHANGE\_REQEUSTED\_NOTIFY

**Definition** power.h:42

[SCMI\_POWER\_DOMAIN\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION](power_8h.md#a669e3ff12b5fc6791440e4adb7596293aee289d3ed8b8a0fbdc4befc92f10fa65)

@ SCMI\_POWER\_DOMAIN\_MSG\_NEGOTIATE\_PROTOCOL\_VERSION

**Definition** power.h:44

[SCMI\_POWER\_DOMAIN\_MSG\_POWER\_DOMAIN\_ATTRIBUTES](power_8h.md#a669e3ff12b5fc6791440e4adb7596293aefdc40ff9bb0939d37cb631eb2aa7daa)

@ SCMI\_POWER\_DOMAIN\_MSG\_POWER\_DOMAIN\_ATTRIBUTES

**Definition** power.h:38

[scmi\_power\_state\_get](power_8h.md#adc7a2fbf0c4cab570d3a567ce548c947)

int scmi\_power\_state\_get(uint32\_t domain\_id, uint32\_t \*power\_state)

Query the power domain state.

[protocol.h](protocol_8h.md)

SCMI protocol generic functions and structures.

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[scmi\_power\_state\_config](structscmi__power__state__config.md)

Describes the parameters for the POWER\_STATE\_SET command.

**Definition** power.h:25

[scmi\_power\_state\_config::power\_state](structscmi__power__state__config.md#a742409967c5487aecbccf89347dd7ae4)

uint32\_t power\_state

**Definition** power.h:28

[scmi\_power\_state\_config::flags](structscmi__power__state__config.md#a83743ab1270c319ab62148e2cf89741f)

uint32\_t flags

**Definition** power.h:26

[scmi\_power\_state\_config::domain\_id](structscmi__power__state__config.md#ae246faf5674e4d885d84e8ee782cccae)

uint32\_t domain\_id

**Definition** power.h:27

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [firmware](dir_e97f19a49725d52aae6eece65b856a75.md)
- [scmi](dir_b6bd1dece7d1578165357955ca5f0079.md)
- [power.h](power_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
