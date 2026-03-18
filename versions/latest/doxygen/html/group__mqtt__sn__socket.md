---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__mqtt__sn__socket.html
original_path: doxygen/html/group__mqtt__sn__socket.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MQTT-SN Client library

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

MQTT-SN Client Implementation.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [mqtt\_sn\_data](structmqtt__sn__data.md) |
|  | Abstracts memory buffers. [More...](structmqtt__sn__data.md#details) |
| union | [mqtt\_sn\_evt\_param](unionmqtt__sn__evt__param.md) |
|  | Event metadata. [More...](unionmqtt__sn__evt__param.md#details) |
| struct | [mqtt\_sn\_evt](structmqtt__sn__evt.md) |
|  | MQTT-SN event structure to be handled by the event callback. [More...](structmqtt__sn__evt.md#details) |
| struct | [mqtt\_sn\_transport](structmqtt__sn__transport.md) |
|  | Structure to describe an MQTT-SN transport. [More...](structmqtt__sn__transport.md#details) |
| struct | [mqtt\_sn\_client](structmqtt__sn__client.md) |
|  | Structure describing an MQTT-SN client. [More...](structmqtt__sn__client.md#details) |

| Macros | |
| --- | --- |
| #define | [MQTT\_SN\_DATA\_STRING\_LITERAL](#gaf8223bf7e5548323c453b30be031e37e)(literal) |
|  | Initialize memory buffer from C literal string. |
| #define | [MQTT\_SN\_DATA\_BYTES](#gabb58a0e4aa418a864f1208ff188f40bc)(...) |
|  | Initialize memory buffer from single bytes. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [mqtt\_sn\_evt\_cb\_t](#gaecd8b966f3e2112261993f8a2cd5c94a)) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, const struct [mqtt\_sn\_evt](structmqtt__sn__evt.md) \*evt) |
|  | Asynchronous event notification callback registered by the application. |

| Enumerations | |
| --- | --- |
| enum | [mqtt\_sn\_qos](#ga8072226d2d96e184137ef40775389786) { [MQTT\_SN\_QOS\_0](#gga8072226d2d96e184137ef40775389786acb18ea4162f8ccac24e733da5511b389) , [MQTT\_SN\_QOS\_1](#gga8072226d2d96e184137ef40775389786a785b3ab4cde3c861f861009b00e584da) , [MQTT\_SN\_QOS\_2](#gga8072226d2d96e184137ef40775389786a4b01cb386e18de88b8f26973a65771f4) , [MQTT\_SN\_QOS\_M1](#gga8072226d2d96e184137ef40775389786a2f0dce2f9249cea36d77ea16d21f61b9) } |
|  | Quality of Service. [More...](#ga8072226d2d96e184137ef40775389786) |
| enum | [mqtt\_sn\_topic\_type](#gabca9262da31b09086b0f802d15eea3fd) { [MQTT\_SN\_TOPIC\_TYPE\_NORMAL](#ggabca9262da31b09086b0f802d15eea3fda18ad286ee41092116dd734faba7f3e9b) , [MQTT\_SN\_TOPIC\_TYPE\_PREDEF](#ggabca9262da31b09086b0f802d15eea3fda48301bc2ca23f5f53c2e320b309f923b) , [MQTT\_SN\_TOPIC\_TYPE\_SHORT](#ggabca9262da31b09086b0f802d15eea3fdad142dda8e35f4cbe428dc572fc005730) } |
|  | MQTT-SN topic types. [More...](#gabca9262da31b09086b0f802d15eea3fd) |
| enum | [mqtt\_sn\_return\_code](#gaab8c9d8ddbaa2af542fdcd3e4178ea9e) { [MQTT\_SN\_CODE\_ACCEPTED](#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea9075123172fff71a180c280b5ca99f1c) = 0x00 , [MQTT\_SN\_CODE\_REJECTED\_CONGESTION](#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea94471cce989efc2514bf37b54848cee7) = 0x01 , [MQTT\_SN\_CODE\_REJECTED\_TOPIC\_ID](#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eac6de6a7f4b8becc11e83fb60e30e2ef3) = 0x02 , [MQTT\_SN\_CODE\_REJECTED\_NOTSUP](#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eaa612db276815fadc5b379f13e7eb78f5) = 0x03 } |
|  | MQTT-SN return codes. [More...](#gaab8c9d8ddbaa2af542fdcd3e4178ea9e) |
| enum | [mqtt\_sn\_evt\_type](#gaa52518be4aa308dda9552e14d0045c42) {     [MQTT\_SN\_EVT\_CONNECTED](#ggaa52518be4aa308dda9552e14d0045c42a4c6c473a7ef6e0fd362b1b865fe3d6a6) , [MQTT\_SN\_EVT\_DISCONNECTED](#ggaa52518be4aa308dda9552e14d0045c42a9a155ce397e5eb73496bd85ef7cc44bf) , [MQTT\_SN\_EVT\_ASLEEP](#ggaa52518be4aa308dda9552e14d0045c42a65d0caaadc8ad95dffd8beb5c77ceb3f) , [MQTT\_SN\_EVT\_AWAKE](#ggaa52518be4aa308dda9552e14d0045c42ae0a691ff1d222e12aada6de2706090bd) ,     [MQTT\_SN\_EVT\_PUBLISH](#ggaa52518be4aa308dda9552e14d0045c42a5923dab1ac92c6d186920368440b53bf) , [MQTT\_SN\_EVT\_PINGRESP](#ggaa52518be4aa308dda9552e14d0045c42a06e53118fc5799c924de346ac7ee1135)   } |
|  | Event types that can be emitted by the library. [More...](#gaa52518be4aa308dda9552e14d0045c42) |

| Functions | |
| --- | --- |
| int | [mqtt\_sn\_client\_init](#gae6a3f7a7762653474df97364ef69fc74) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, const struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*client\_id, struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) \*transport, [mqtt\_sn\_evt\_cb\_t](#gaecd8b966f3e2112261993f8a2cd5c94a) evt\_cb, void \*tx, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) txsz, void \*rx, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) rxsz) |
|  | Initialize a client. |
| void | [mqtt\_sn\_client\_deinit](#ga67d69e4e3f00b31b5ea3b37fb6d653b1) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client) |
|  | Deinitialize the client. |
| int | [mqtt\_sn\_connect](#ga8c2a525f1c30e5d5ff37180d33a76d4d) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) will, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) clean\_session) |
|  | Connect the client. |
| int | [mqtt\_sn\_disconnect](#gab9cba16f8ce06f606ee81e0d34deb862) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client) |
|  | Disconnect the client. |
| int | [mqtt\_sn\_sleep](#gaf29a6339419ea02052fe53a18bb8e5ee) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) duration) |
|  | Set the client into sleep state. |
| int | [mqtt\_sn\_subscribe](#ga9b481db6d39dee05e2c58d4c721fe0a5) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, enum [mqtt\_sn\_qos](#ga8072226d2d96e184137ef40775389786) qos, struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*topic\_name) |
|  | Subscribe to a given topic. |
| int | [mqtt\_sn\_unsubscribe](#ga1bcd2a0f52610708bebb4b3b6d6cbf35) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, enum [mqtt\_sn\_qos](#ga8072226d2d96e184137ef40775389786) qos, struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*topic\_name) |
|  | Unsubscribe from a topic. |
| int | [mqtt\_sn\_publish](#ga434c3626ceaf3a9b60c5ffb75e9b5b56) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, enum [mqtt\_sn\_qos](#ga8072226d2d96e184137ef40775389786) qos, struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*topic\_name, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) retain, struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*data) |
|  | Publish a value. |
| int | [mqtt\_sn\_input](#gafa1f81168d44152ad72c5f3d1c744b49) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client) |
|  | Check the transport for new incoming data. |
| int | [mqtt\_sn\_get\_topic\_name](#gade962a4da5311a403893ba24714dc332) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*topic\_name) |
|  | Get topic name by topic ID. |

## Detailed Description

MQTT-SN Client Implementation.

MQTT-SN Client's Application interface is defined in this header. Targets protocol version 1.2.

## Macro Definition Documentation

## [◆ ](#gabb58a0e4aa418a864f1208ff188f40bc)MQTT\_SN\_DATA\_BYTES

| #define MQTT\_SN\_DATA\_BYTES | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mqtt_sn.h](mqtt__sn_8h.md)>`

**Value:**

((struct [mqtt\_sn\_data](structmqtt__sn__data.md)) { ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)[]){ \_\_VA\_ARGS\_\_ }, sizeof(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)[]){ \_\_VA\_ARGS\_\_ })})

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[mqtt\_sn\_data](structmqtt__sn__data.md)

Abstracts memory buffers.

**Definition** mqtt\_sn.h:83

Initialize memory buffer from single bytes.

Use it as follows:

struct [mqtt\_sn\_data](structmqtt__sn__data.md "Abstracts memory buffers.") data = [MQTT\_SN\_DATA\_BYTES(0x13, 0x37)](#gabb58a0e4aa418a864f1208ff188f40bc);

## [◆ ](#gaf8223bf7e5548323c453b30be031e37e)MQTT\_SN\_DATA\_STRING\_LITERAL

| #define MQTT\_SN\_DATA\_STRING\_LITERAL | ( |  | *literal* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mqtt_sn.h](mqtt__sn_8h.md)>`

**Value:**

((struct [mqtt\_sn\_data](structmqtt__sn__data.md)){literal, sizeof(literal) - 1})

Initialize memory buffer from C literal string.

Use it as follows:

struct [mqtt\_sn\_data](structmqtt__sn__data.md "Abstracts memory buffers.") topic = MQTT\_SN\_DATA\_STRING\_LITERAL("/zephyr");

Parameters
:   | [in] | literal | Literal string from which to generate [mqtt\_sn\_data](structmqtt__sn__data.md "Abstracts memory buffers.") object. |
    | --- | --- | --- |

## Typedef Documentation

## [◆ ](#gaecd8b966f3e2112261993f8a2cd5c94a)mqtt\_sn\_evt\_cb\_t

| typedef void(\* mqtt\_sn\_evt\_cb\_t) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, const struct [mqtt\_sn\_evt](structmqtt__sn__evt.md) \*evt) |
| --- |

`#include <[mqtt_sn.h](mqtt__sn_8h.md)>`

Asynchronous event notification callback registered by the application.

Parameters
:   | [in] | client | Identifies the client for which the event is notified. |
    | --- | --- | --- |
    | [in] | evt | Event description along with result and associated parameters (if any). |

## Enumeration Type Documentation

## [◆ ](#gaa52518be4aa308dda9552e14d0045c42)mqtt\_sn\_evt\_type

| enum [mqtt\_sn\_evt\_type](#gaa52518be4aa308dda9552e14d0045c42) |
| --- |

`#include <[mqtt_sn.h](mqtt__sn_8h.md)>`

Event types that can be emitted by the library.

| Enumerator | |
| --- | --- |
| MQTT\_SN\_EVT\_CONNECTED | Connected to a gateway. |
| MQTT\_SN\_EVT\_DISCONNECTED | Disconnected. |
| MQTT\_SN\_EVT\_ASLEEP | Entered ASLEEP state. |
| MQTT\_SN\_EVT\_AWAKE | Entered AWAKE state. |
| MQTT\_SN\_EVT\_PUBLISH | Received a PUBLISH message. |
| MQTT\_SN\_EVT\_PINGRESP | Received a PINGRESP. |

## [◆ ](#ga8072226d2d96e184137ef40775389786)mqtt\_sn\_qos

| enum [mqtt\_sn\_qos](#ga8072226d2d96e184137ef40775389786) |
| --- |

`#include <[mqtt_sn.h](mqtt__sn_8h.md)>`

Quality of Service.

QoS 0-2 work the same as basic MQTT, QoS -1 is an MQTT-SN addition. QOS -1 is not supported yet.

| Enumerator | |
| --- | --- |
| MQTT\_SN\_QOS\_0 | QOS 0. |
| MQTT\_SN\_QOS\_1 | QOS 1. |
| MQTT\_SN\_QOS\_2 | QOS 2. |
| MQTT\_SN\_QOS\_M1 | QOS -1. |

## [◆ ](#gaab8c9d8ddbaa2af542fdcd3e4178ea9e)mqtt\_sn\_return\_code

| enum [mqtt\_sn\_return\_code](#gaab8c9d8ddbaa2af542fdcd3e4178ea9e) |
| --- |

`#include <[mqtt_sn.h](mqtt__sn_8h.md)>`

MQTT-SN return codes.

| Enumerator | |
| --- | --- |
| MQTT\_SN\_CODE\_ACCEPTED | Accepted. |
| MQTT\_SN\_CODE\_REJECTED\_CONGESTION | Rejected: congestion. |
| MQTT\_SN\_CODE\_REJECTED\_TOPIC\_ID | Rejected: Invalid Topic ID. |
| MQTT\_SN\_CODE\_REJECTED\_NOTSUP | Rejected: Not Supported. |

## [◆ ](#gabca9262da31b09086b0f802d15eea3fd)mqtt\_sn\_topic\_type

| enum [mqtt\_sn\_topic\_type](#gabca9262da31b09086b0f802d15eea3fd) |
| --- |

`#include <[mqtt_sn.h](mqtt__sn_8h.md)>`

MQTT-SN topic types.

| Enumerator | |
| --- | --- |
| MQTT\_SN\_TOPIC\_TYPE\_NORMAL | Normal topic.  It allows usage of any valid UTF-8 string as a topic name. |
| MQTT\_SN\_TOPIC\_TYPE\_PREDEF | Pre-defined topic.  It allows usage of a two-byte identifier representing a topic name for which the corresponding topic name is known in advance by both the client and the gateway/server. |
| MQTT\_SN\_TOPIC\_TYPE\_SHORT | Short topic.  It allows usage of a two-byte string as a topic name. |

## Function Documentation

## [◆ ](#ga67d69e4e3f00b31b5ea3b37fb6d653b1)mqtt\_sn\_client\_deinit()

| void mqtt\_sn\_client\_deinit | ( | struct [mqtt\_sn\_client](structmqtt__sn__client.md) \* | *client* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mqtt_sn.h](mqtt__sn_8h.md)>`

Deinitialize the client.

This removes all topics and publishes, and also de-inits the transport.

Parameters
:   | client | The MQTT-SN client to deinitialize. |
    | --- | --- |

## [◆ ](#gae6a3f7a7762653474df97364ef69fc74)mqtt\_sn\_client\_init()

| int mqtt\_sn\_client\_init | ( | struct [mqtt\_sn\_client](structmqtt__sn__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | const struct [mqtt\_sn\_data](structmqtt__sn__data.md) \* | *client\_id*, |
|  |  | struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) \* | *transport*, |
|  |  | [mqtt\_sn\_evt\_cb\_t](#gaecd8b966f3e2112261993f8a2cd5c94a) | *evt\_cb*, |
|  |  | void \* | *tx*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *txsz*, |
|  |  | void \* | *rx*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *rxsz* ) |

`#include <[mqtt_sn.h](mqtt__sn_8h.md)>`

Initialize a client.

Parameters
:   | client | The MQTT-SN client to initialize. |
    | --- | --- |
    | client\_id | The ID to be used by the client. |
    | transport | The transport to be used by the client. |
    | evt\_cb | The event callback function for the client. |
    | tx | Pointer to the transmit buffer. |
    | txsz | Size of the transmit buffer. |
    | rx | Pointer to the receive buffer. |
    | rxsz | Size of the receive buffer. |

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#ga8c2a525f1c30e5d5ff37180d33a76d4d)mqtt\_sn\_connect()

| int mqtt\_sn\_connect | ( | struct [mqtt\_sn\_client](structmqtt__sn__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *will*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *clean\_session* ) |

`#include <[mqtt_sn.h](mqtt__sn_8h.md)>`

Connect the client.

Parameters
:   | client | The MQTT-SN client to connect. |
    | --- | --- |
    | will | Flag indicating if a Will message should be sent. |
    | clean\_session | Flag indicating if a clean session should be started. |

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#gab9cba16f8ce06f606ee81e0d34deb862)mqtt\_sn\_disconnect()

| int mqtt\_sn\_disconnect | ( | struct [mqtt\_sn\_client](structmqtt__sn__client.md) \* | *client* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mqtt_sn.h](mqtt__sn_8h.md)>`

Disconnect the client.

Parameters
:   | client | The MQTT-SN client to disconnect. |
    | --- | --- |

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#gade962a4da5311a403893ba24714dc332)mqtt\_sn\_get\_topic\_name()

| int mqtt\_sn\_get\_topic\_name | ( | struct [mqtt\_sn\_client](structmqtt__sn__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *id*, |
|  |  | struct [mqtt\_sn\_data](structmqtt__sn__data.md) \* | *topic\_name* ) |

`#include <[mqtt_sn.h](mqtt__sn_8h.md)>`

Get topic name by topic ID.

Parameters
:   | [in] | client | The MQTT-SN client that uses this topic. |
    | --- | --- | --- |
    | [in] | id | Topic identifier. |
    | [out] | topic\_name | Will be assigned to topic name. |

Returns
:   0 on success, -ENOENT if topic ID doesn't exist, or -EINVAL on invalid arguments.

## [◆ ](#gafa1f81168d44152ad72c5f3d1c744b49)mqtt\_sn\_input()

| int mqtt\_sn\_input | ( | struct [mqtt\_sn\_client](structmqtt__sn__client.md) \* | *client* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mqtt_sn.h](mqtt__sn_8h.md)>`

Check the transport for new incoming data.

Call this function periodically, or if you have good reason to believe there is any data. If the client's transport struct contains a poll-function, this function is non-blocking.

Parameters
:   | client | The MQTT-SN client to check for incoming data. |
    | --- | --- |

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#ga434c3626ceaf3a9b60c5ffb75e9b5b56)mqtt\_sn\_publish()

| int mqtt\_sn\_publish | ( | struct [mqtt\_sn\_client](structmqtt__sn__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | enum [mqtt\_sn\_qos](#ga8072226d2d96e184137ef40775389786) | *qos*, |
|  |  | struct [mqtt\_sn\_data](structmqtt__sn__data.md) \* | *topic\_name*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *retain*, |
|  |  | struct [mqtt\_sn\_data](structmqtt__sn__data.md) \* | *data* ) |

`#include <[mqtt_sn.h](mqtt__sn_8h.md)>`

Publish a value.

If the topic is not yet registered with the gateway, the library takes care of it.

Parameters
:   | client | The MQTT-SN client that should publish. |
    | --- | --- |
    | qos | The desired quality of service for the publish. |
    | topic\_name | The name of the topic to publish to. |
    | retain | Flag indicating if the message should be retained by the broker. |
    | data | The data to be published. |

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#gaf29a6339419ea02052fe53a18bb8e5ee)mqtt\_sn\_sleep()

| int mqtt\_sn\_sleep | ( | struct [mqtt\_sn\_client](structmqtt__sn__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *duration* ) |

`#include <[mqtt_sn.h](mqtt__sn_8h.md)>`

Set the client into sleep state.

Parameters
:   | client | The MQTT-SN client to be put to sleep. |
    | --- | --- |
    | duration | Sleep duration (in seconds). |

Returns
:   0 on success, negative errno code on failure.

## [◆ ](#ga9b481db6d39dee05e2c58d4c721fe0a5)mqtt\_sn\_subscribe()

| int mqtt\_sn\_subscribe | ( | struct [mqtt\_sn\_client](structmqtt__sn__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | enum [mqtt\_sn\_qos](#ga8072226d2d96e184137ef40775389786) | *qos*, |
|  |  | struct [mqtt\_sn\_data](structmqtt__sn__data.md) \* | *topic\_name* ) |

`#include <[mqtt_sn.h](mqtt__sn_8h.md)>`

Subscribe to a given topic.

Parameters
:   | client | The MQTT-SN client that should subscribe. |
    | --- | --- |
    | qos | The desired quality of service for the subscription. |
    | topic\_name | The name of the topic to subscribe to. |

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#ga1bcd2a0f52610708bebb4b3b6d6cbf35)mqtt\_sn\_unsubscribe()

| int mqtt\_sn\_unsubscribe | ( | struct [mqtt\_sn\_client](structmqtt__sn__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | enum [mqtt\_sn\_qos](#ga8072226d2d96e184137ef40775389786) | *qos*, |
|  |  | struct [mqtt\_sn\_data](structmqtt__sn__data.md) \* | *topic\_name* ) |

`#include <[mqtt_sn.h](mqtt__sn_8h.md)>`

Unsubscribe from a topic.

Parameters
:   | client | The MQTT-SN client that should unsubscribe. |
    | --- | --- |
    | qos | The quality of service used when subscribing. |
    | topic\_name | The name of the topic to unsubscribe from. |

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
