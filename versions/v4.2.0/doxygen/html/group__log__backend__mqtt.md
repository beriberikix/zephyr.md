---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/group__log__backend__mqtt.html
original_path: doxygen/html/group__log__backend__mqtt.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MQTT log backend API

[Operating System Services](group__os__services.md) » [Logging](group__logging.md) » [Logger system](group__logger.md) » [Logger backend interface](group__log__backend.md)

MQTT log backend API.
[More...](#details)

| Functions | |
| --- | --- |
| int | [log\_backend\_mqtt\_client\_set](#ga75e1b3fb99bb8211eaa684fcaa41882a) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | Set the MQTT client instance to be able to publish application's log messages to broker. |
| int | [log\_backend\_mqtt\_topic\_set](#gaad9f9b8fe0c67093e41732b525922bee) (const char \*topic) |
|  | Set the MQTT topic to which log messages will be published. |

## Detailed Description

MQTT log backend API.

## Function Documentation

## [◆ ](#ga75e1b3fb99bb8211eaa684fcaa41882a)log\_backend\_mqtt\_client\_set()

| int log\_backend\_mqtt\_client\_set | ( | struct [mqtt\_client](structmqtt__client.md) \* | *client* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/logging/log_backend_mqtt.h](log__backend__mqtt_8h.md)>`

Set the MQTT client instance to be able to publish application's log messages to broker.

This function allows the application to provide its own initialized MQTT client to the log backend. The backend will use this client exclusively for publishing log messages via [mqtt\_publish()](group__mqtt__socket.md#ga57745efa1bf6fbdf7eb1b3f01623e4c7 "API to publish messages on topics.").

Parameters
:   | client | Pointer to an initialized and connected MQTT client. The client must remain valid for the lifetime of the log backend usage. Pass NULL to disable MQTT logging. |
    | --- | --- |

Returns
:   0 on success, negative error code on failure.

Note
:   The MQTT client must be connected before calling this function.
:   The backend will not manage the client connection - this is the responsibility of the application.
:   The backend will only use [mqtt\_publish()](group__mqtt__socket.md#ga57745efa1bf6fbdf7eb1b3f01623e4c7 "API to publish messages on topics.") and will not perform any other operations on the client.

## [◆ ](#gaad9f9b8fe0c67093e41732b525922bee)log\_backend\_mqtt\_topic\_set()

| int log\_backend\_mqtt\_topic\_set | ( | const char \* | *topic* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[zephyr/logging/log_backend_mqtt.h](log__backend__mqtt_8h.md)>`

Set the MQTT topic to which log messages will be published.

Allows the application to specify the MQTT topic that the log backend will use for publishing log messages to.

Parameters
:   | topic | Pointer to a null-terminated string containing the MQTT topic. The topic must remain valid for the lifetime of the log backend usage. |
    | --- | --- |

Returns
:   0 on success, negative error code on failure.

Note
:   The topic must be a valid UTF-8 string, null-terminated and should not exceed the maximum length supported by the MQTT broker.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
