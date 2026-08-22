---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/log__backend__mqtt_8h_source.html
original_path: doxygen/html/log__backend__mqtt_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

log\_backend\_mqtt.h

[Go to the documentation of this file.](log__backend__mqtt_8h.md)

1/\*

2 \* Copyright (c) 2024 Arif Balik <arifbalik@outlook.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_LOGGING\_LOG\_BACKEND\_MQTT\_H\_

8#define ZEPHYR\_INCLUDE\_LOGGING\_LOG\_BACKEND\_MQTT\_H\_

9

10#include <[zephyr/net/mqtt.h](mqtt_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

22

[ 42](group__log__backend__mqtt.md#ga75e1b3fb99bb8211eaa684fcaa41882a)int [log\_backend\_mqtt\_client\_set](group__log__backend__mqtt.md#ga75e1b3fb99bb8211eaa684fcaa41882a)(struct [mqtt\_client](structmqtt__client.md) \*client);

43

[ 58](group__log__backend__mqtt.md#gaad9f9b8fe0c67093e41732b525922bee)int [log\_backend\_mqtt\_topic\_set](group__log__backend__mqtt.md#gaad9f9b8fe0c67093e41732b525922bee)(const char \*topic);

59

63

64#ifdef \_\_cplusplus

65}

66#endif

67

68#endif /\* ZEPHYR\_INCLUDE\_LOGGING\_LOG\_BACKEND\_MQTT\_H\_ \*/

[log\_backend\_mqtt\_client\_set](group__log__backend__mqtt.md#ga75e1b3fb99bb8211eaa684fcaa41882a)

int log\_backend\_mqtt\_client\_set(struct mqtt\_client \*client)

Set the MQTT client instance to be able to publish application's log messages to broker.

[log\_backend\_mqtt\_topic\_set](group__log__backend__mqtt.md#gaad9f9b8fe0c67093e41732b525922bee)

int log\_backend\_mqtt\_topic\_set(const char \*topic)

Set the MQTT topic to which log messages will be published.

[mqtt.h](mqtt_8h.md)

MQTT Client Implementation.

[mqtt\_client](structmqtt__client.md)

MQTT Client definition to maintain information relevant to the client.

**Definition** mqtt.h:898

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [logging](dir_7da6482b46a75d2870a82324d67b5f7e.md)
- [log\_backend\_mqtt.h](log__backend__mqtt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
