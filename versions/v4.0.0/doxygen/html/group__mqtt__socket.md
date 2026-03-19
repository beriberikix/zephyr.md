---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__mqtt__socket.html
original_path: doxygen/html/group__mqtt__socket.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MQTT Client library

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

| Data Structures | |
| --- | --- |
| struct | [mqtt\_utf8](structmqtt__utf8.md) |
|  | Abstracts UTF-8 encoded strings. [More...](structmqtt__utf8.md#details) |
| struct | [mqtt\_binstr](structmqtt__binstr.md) |
|  | Abstracts binary strings. [More...](structmqtt__binstr.md#details) |
| struct | [mqtt\_topic](structmqtt__topic.md) |
|  | Abstracts MQTT UTF-8 encoded topic that can be subscribed to or published. [More...](structmqtt__topic.md#details) |
| struct | [mqtt\_publish\_message](structmqtt__publish__message.md) |
|  | Parameters for a publish message. [More...](structmqtt__publish__message.md#details) |
| struct | [mqtt\_connack\_param](structmqtt__connack__param.md) |
|  | Parameters for a connection acknowledgment (CONNACK). [More...](structmqtt__connack__param.md#details) |
| struct | [mqtt\_puback\_param](structmqtt__puback__param.md) |
|  | Parameters for MQTT publish acknowledgment (PUBACK). [More...](structmqtt__puback__param.md#details) |
| struct | [mqtt\_pubrec\_param](structmqtt__pubrec__param.md) |
|  | Parameters for MQTT publish receive (PUBREC). [More...](structmqtt__pubrec__param.md#details) |
| struct | [mqtt\_pubrel\_param](structmqtt__pubrel__param.md) |
|  | Parameters for MQTT publish release (PUBREL). [More...](structmqtt__pubrel__param.md#details) |
| struct | [mqtt\_pubcomp\_param](structmqtt__pubcomp__param.md) |
|  | Parameters for MQTT publish complete (PUBCOMP). [More...](structmqtt__pubcomp__param.md#details) |
| struct | [mqtt\_suback\_param](structmqtt__suback__param.md) |
|  | Parameters for MQTT subscription acknowledgment (SUBACK). [More...](structmqtt__suback__param.md#details) |
| struct | [mqtt\_unsuback\_param](structmqtt__unsuback__param.md) |
|  | Parameters for MQTT unsubscribe acknowledgment (UNSUBACK). [More...](structmqtt__unsuback__param.md#details) |
| struct | [mqtt\_publish\_param](structmqtt__publish__param.md) |
|  | Parameters for a publish message (PUBLISH). [More...](structmqtt__publish__param.md#details) |
| struct | [mqtt\_subscription\_list](structmqtt__subscription__list.md) |
|  | List of topics in a subscription request. [More...](structmqtt__subscription__list.md#details) |
| union | [mqtt\_evt\_param](unionmqtt__evt__param.md) |
|  | Defines event parameters notified along with asynchronous events to the application. [More...](unionmqtt__evt__param.md#details) |
| struct | [mqtt\_evt](structmqtt__evt.md) |
|  | Defines MQTT asynchronous event notified to the application. [More...](structmqtt__evt.md#details) |
| struct | [mqtt\_sec\_config](structmqtt__sec__config.md) |
|  | TLS configuration for secure MQTT transports. [More...](structmqtt__sec__config.md#details) |
| struct | [mqtt\_transport](structmqtt__transport.md) |
|  | MQTT transport specific data. [More...](structmqtt__transport.md#details) |
| struct | [mqtt\_internal](structmqtt__internal.md) |
|  | MQTT internal state. [More...](structmqtt__internal.md#details) |
| struct | [mqtt\_client](structmqtt__client.md) |
|  | MQTT Client definition to maintain information relevant to the client. [More...](structmqtt__client.md#details) |

| Macros | |
| --- | --- |
| #define | [MQTT\_UTF8\_LITERAL](#gaeaa4fcf581c7d6be755f9a053a3b488c)(literal) |
|  | Initialize UTF-8 encoded string from C literal string. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [mqtt\_evt\_cb\_t](#gabdf01ededb62ceb4c1608a64cb718a8c)) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_evt](structmqtt__evt.md) \*evt) |
|  | Asynchronous event notification callback registered by the application. |

| Enumerations | |
| --- | --- |
| enum | [mqtt\_evt\_type](#ga0071fe013b9920711456ef51cc3e6d91) {     [MQTT\_EVT\_CONNACK](#gga0071fe013b9920711456ef51cc3e6d91ab6e626b5a1eda76b32053ccbb4b7b5f3) , [MQTT\_EVT\_DISCONNECT](#gga0071fe013b9920711456ef51cc3e6d91a8de64478f7ae463d7844fc2e786ce032) , [MQTT\_EVT\_PUBLISH](#gga0071fe013b9920711456ef51cc3e6d91aa893a345e05e796cfd28392c1c4d8cf9) , [MQTT\_EVT\_PUBACK](#gga0071fe013b9920711456ef51cc3e6d91a2f25d5d4ca704ab63439d4706d3587de) ,     [MQTT\_EVT\_PUBREC](#gga0071fe013b9920711456ef51cc3e6d91a1d5f6ba2524f935dd9625d85638eda87) , [MQTT\_EVT\_PUBREL](#gga0071fe013b9920711456ef51cc3e6d91ab35ebaf4dcc6698471eb16a41c8252a2) , [MQTT\_EVT\_PUBCOMP](#gga0071fe013b9920711456ef51cc3e6d91afdba5e48987b4355f445d35b4dc056e8) , [MQTT\_EVT\_SUBACK](#gga0071fe013b9920711456ef51cc3e6d91a67caa558ae7975548b3c4e1c1de5f8fb) ,     [MQTT\_EVT\_UNSUBACK](#gga0071fe013b9920711456ef51cc3e6d91aa5c333ddf366e44f932ec5545ed75bb2) , [MQTT\_EVT\_PINGRESP](#gga0071fe013b9920711456ef51cc3e6d91a52842872177b26e5e0e45a3c66fdb0b5)   } |
|  | MQTT Asynchronous Events notified to the application from the module through the callback registered by the application. [More...](#ga0071fe013b9920711456ef51cc3e6d91) |
| enum | [mqtt\_version](#ga90d152a4b0986e9a07a12c7c56f5e2a0) { [MQTT\_VERSION\_3\_1\_0](#gga90d152a4b0986e9a07a12c7c56f5e2a0ac93057183f274a064e118af6b4d681e7) = 3 , [MQTT\_VERSION\_3\_1\_1](#gga90d152a4b0986e9a07a12c7c56f5e2a0ad2926cb14db1fcfb95a47f45d2f5b08e) = 4 } |
|  | MQTT version protocol level. [More...](#ga90d152a4b0986e9a07a12c7c56f5e2a0) |
| enum | [mqtt\_qos](#ga396015e492b0fee8da37c7168d9cdb33) { [MQTT\_QOS\_0\_AT\_MOST\_ONCE](#gga396015e492b0fee8da37c7168d9cdb33a2ea1051887beb30d7c1fd61b5e153f6e) = 0x00 , [MQTT\_QOS\_1\_AT\_LEAST\_ONCE](#gga396015e492b0fee8da37c7168d9cdb33a732d9d294b41bd472ef221c8dff0731d) = 0x01 , [MQTT\_QOS\_2\_EXACTLY\_ONCE](#gga396015e492b0fee8da37c7168d9cdb33a9012ddca1943a824454ac14a85bcf117) = 0x02 } |
|  | MQTT Quality of Service types. [More...](#ga396015e492b0fee8da37c7168d9cdb33) |
| enum | [mqtt\_conn\_return\_code](#gaa17b38ed9c7e65f3e01ad906b24bb618) {     [MQTT\_CONNECTION\_ACCEPTED](#ggaa17b38ed9c7e65f3e01ad906b24bb618a2fdd911a8978b8df2254766c1e3fd050) = 0x00 , [MQTT\_UNACCEPTABLE\_PROTOCOL\_VERSION](#ggaa17b38ed9c7e65f3e01ad906b24bb618a9195e642b0b9e594d96aff84f0696744) = 0x01 , [MQTT\_IDENTIFIER\_REJECTED](#ggaa17b38ed9c7e65f3e01ad906b24bb618aa662f46a044e31ae26397adffee82141) = 0x02 , [MQTT\_SERVER\_UNAVAILABLE](#ggaa17b38ed9c7e65f3e01ad906b24bb618afe234e7084078871a567359819458df3) = 0x03 ,     [MQTT\_BAD\_USER\_NAME\_OR\_PASSWORD](#ggaa17b38ed9c7e65f3e01ad906b24bb618aa12d243cef12e3e7b1f4e245f64a1134) = 0x04 , [MQTT\_NOT\_AUTHORIZED](#ggaa17b38ed9c7e65f3e01ad906b24bb618a4d101dcf5a101d90ae26ba8fe54a27eb) = 0x05   } |
|  | MQTT CONNACK return codes. [More...](#gaa17b38ed9c7e65f3e01ad906b24bb618) |
| enum | [mqtt\_suback\_return\_code](#gaca1e61c8b14b75544e253cea355274a8) { [MQTT\_SUBACK\_SUCCESS\_QoS\_0](#ggaca1e61c8b14b75544e253cea355274a8a835fdffd58e7ad800d549c9dfce1ce01) = 0x00 , [MQTT\_SUBACK\_SUCCESS\_QoS\_1](#ggaca1e61c8b14b75544e253cea355274a8afd0c8b7b9c39b3e242f33f7603b3ca9c) = 0x01 , [MQTT\_SUBACK\_SUCCESS\_QoS\_2](#ggaca1e61c8b14b75544e253cea355274a8ae8702eb6a2944444abd9b2f6c1fb2e1b) = 0x02 , [MQTT\_SUBACK\_FAILURE](#ggaca1e61c8b14b75544e253cea355274a8a08b9651ef43ea219f29125fcb43952f7) = 0x80 } |
|  | MQTT SUBACK return codes. [More...](#gaca1e61c8b14b75544e253cea355274a8) |
| enum | [mqtt\_transport\_type](#gaffc2c3078004cf8d24935be086ad63b4) { [MQTT\_TRANSPORT\_NON\_SECURE](#ggaffc2c3078004cf8d24935be086ad63b4a981f7e2ca25c5e478bf658750e26972a) , [MQTT\_TRANSPORT\_NUM](#ggaffc2c3078004cf8d24935be086ad63b4a61056a250c98f3d29ccf5cdbdda3d3df) } |
|  | MQTT transport type. [More...](#gaffc2c3078004cf8d24935be086ad63b4) |

| Functions | |
| --- | --- |
| void | [mqtt\_client\_init](#gad1376509ae7c946c840d103d8b59e9a1) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | Initializes the client instance. |
| int | [mqtt\_connect](#gad936f28553cb2e771a843512b0a315fa) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | API to request new MQTT client connection. |
| int | [mqtt\_publish](#ga57745efa1bf6fbdf7eb1b3f01623e4c7) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_publish\_param](structmqtt__publish__param.md) \*param) |
|  | API to publish messages on topics. |
| int | [mqtt\_publish\_qos1\_ack](#gae9069fceec2c018e64cc6beb16aa055c) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_puback\_param](structmqtt__puback__param.md) \*param) |
|  | API used by client to send acknowledgment on receiving QoS1 publish message. |
| int | [mqtt\_publish\_qos2\_receive](#gacbe41b83d9c0676d0d4cf01dd91765eb) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_pubrec\_param](structmqtt__pubrec__param.md) \*param) |
|  | API used by client to send acknowledgment on receiving QoS2 publish message. |
| int | [mqtt\_publish\_qos2\_release](#ga6c952ed014f78774096bfb6099794803) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_pubrel\_param](structmqtt__pubrel__param.md) \*param) |
|  | API used by client to request release of QoS2 publish message. |
| int | [mqtt\_publish\_qos2\_complete](#ga2b17999e845d613f5b0b20015b8204f3) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_pubcomp\_param](structmqtt__pubcomp__param.md) \*param) |
|  | API used by client to send acknowledgment on receiving QoS2 publish release message. |
| int | [mqtt\_subscribe](#ga40d226b891b8f62f2c486bbb11ce9678) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_subscription\_list](structmqtt__subscription__list.md) \*param) |
|  | API to request subscription of one or more topics on the connection. |
| int | [mqtt\_unsubscribe](#ga4ff43a198e93e332b5553a4d0b59261d) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_subscription\_list](structmqtt__subscription__list.md) \*param) |
|  | API to request unsubscription of one or more topics on the connection. |
| int | [mqtt\_ping](#gad1d549d37b69a61e1bf8d9d213e02ca8) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | API to send MQTT ping. |
| int | [mqtt\_disconnect](#gad5e01a1b60c393adb0f7f34c1a90e6ff) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | API to disconnect MQTT connection. |
| int | [mqtt\_abort](#gafb2df41fad7c318f9fe75919919139bd) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | API to abort MQTT connection. |
| int | [mqtt\_live](#ga8b87710d01076c8e51b1a75634168269) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | This API should be called periodically for the client to be able to keep the connection alive by sending Ping Requests if need be. |
| int | [mqtt\_keepalive\_time\_left](#gaa16bf7b0597ad00c4a3943235579e86b) (const struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | Helper function to determine when next keep alive message should be sent. |
| int | [mqtt\_input](#ga2dbc3c158d63a6f57b362be94c22660a) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | Receive an incoming MQTT packet. |
| int | [mqtt\_read\_publish\_payload](#ga3559cdd6093d75c6fe6792ec2a453172) (struct [mqtt\_client](structmqtt__client.md) \*client, void \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Read the payload of the received PUBLISH message. |
| int | [mqtt\_read\_publish\_payload\_blocking](#ga05213aceaa9e9cbbfaa9bab7a78b3d25) (struct [mqtt\_client](structmqtt__client.md) \*client, void \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Blocking version of [mqtt\_read\_publish\_payload](#ga3559cdd6093d75c6fe6792ec2a453172) function. |
| int | [mqtt\_readall\_publish\_payload](#ga31823965ec34a253793b40b50e800417) (struct [mqtt\_client](structmqtt__client.md) \*client, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Blocking version of [mqtt\_read\_publish\_payload](#ga3559cdd6093d75c6fe6792ec2a453172) function which runs until the required number of bytes are read. |

## Detailed Description

Since
:   1.14

Version
:   0.8.0

## Macro Definition Documentation

## [◆ ](#gaeaa4fcf581c7d6be755f9a053a3b488c)MQTT\_UTF8\_LITERAL

| #define MQTT\_UTF8\_LITERAL | ( |  | *literal* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mqtt.h](mqtt_8h.md)>`

**Value:**

((struct [mqtt\_utf8](structmqtt__utf8.md)) {literal, sizeof(literal) - 1})

[mqtt\_utf8](structmqtt__utf8.md)

Abstracts UTF-8 encoded strings.

**Definition** mqtt.h:152

Initialize UTF-8 encoded string from C literal string.

Use it as follows:

struct [mqtt\_utf8](structmqtt__utf8.md "Abstracts UTF-8 encoded strings.") password = MQTT\_UTF8\_LITERAL("my\_pass");

Parameters
:   | [in] | literal | Literal string from which to generate [mqtt\_utf8](structmqtt__utf8.md "Abstracts UTF-8 encoded strings.") object. |
    | --- | --- | --- |

## Typedef Documentation

## [◆ ](#gabdf01ededb62ceb4c1608a64cb718a8c)mqtt\_evt\_cb\_t

| typedef void(\* mqtt\_evt\_cb\_t) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_evt](structmqtt__evt.md) \*evt) |
| --- |

`#include <[mqtt.h](mqtt_8h.md)>`

Asynchronous event notification callback registered by the application.

Parameters
:   | [in] | client | Identifies the client for which the event is notified. |
    | --- | --- | --- |
    | [in] | evt | Event description along with result and associated parameters (if any). |

## Enumeration Type Documentation

## [◆ ](#gaa17b38ed9c7e65f3e01ad906b24bb618)mqtt\_conn\_return\_code

| enum [mqtt\_conn\_return\_code](#gaa17b38ed9c7e65f3e01ad906b24bb618) |
| --- |

`#include <[mqtt.h](mqtt_8h.md)>`

MQTT CONNACK return codes.

| Enumerator | |
| --- | --- |
| MQTT\_CONNECTION\_ACCEPTED | Connection accepted. |
| MQTT\_UNACCEPTABLE\_PROTOCOL\_VERSION | The Server does not support the level of the MQTT protocol requested by the Client. |
| MQTT\_IDENTIFIER\_REJECTED | The Client identifier is correct UTF-8 but not allowed by the Server. |
| MQTT\_SERVER\_UNAVAILABLE | The Network Connection has been made but the MQTT service is unavailable. |
| MQTT\_BAD\_USER\_NAME\_OR\_PASSWORD | The data in the user name or password is malformed. |
| MQTT\_NOT\_AUTHORIZED | The Client is not authorized to connect. |

## [◆ ](#ga0071fe013b9920711456ef51cc3e6d91)mqtt\_evt\_type

| enum [mqtt\_evt\_type](#ga0071fe013b9920711456ef51cc3e6d91) |
| --- |

`#include <[mqtt.h](mqtt_8h.md)>`

MQTT Asynchronous Events notified to the application from the module through the callback registered by the application.

| Enumerator | |
| --- | --- |
| MQTT\_EVT\_CONNACK | Acknowledgment of connection request.  Event result accompanying the event indicates whether the connection failed or succeeded. |
| MQTT\_EVT\_DISCONNECT | Disconnection Event.  MQTT Client Reference is no longer valid once this event is received for the client. |
| MQTT\_EVT\_PUBLISH | Publish event received when message is published on a topic client is subscribed to.  Note  PUBLISH event structure only contains payload size, the payload data parameter should be ignored. Payload content has to be read manually with [mqtt\_read\_publish\_payload](#ga3559cdd6093d75c6fe6792ec2a453172) function. |
| MQTT\_EVT\_PUBACK | Acknowledgment for published message with QoS 1. |
| MQTT\_EVT\_PUBREC | Reception confirmation for published message with QoS 2. |
| MQTT\_EVT\_PUBREL | Release of published message with QoS 2. |
| MQTT\_EVT\_PUBCOMP | Confirmation to a publish release message with QoS 2. |
| MQTT\_EVT\_SUBACK | Acknowledgment to a subscribe request. |
| MQTT\_EVT\_UNSUBACK | Acknowledgment to a unsubscribe request. |
| MQTT\_EVT\_PINGRESP | Ping Response from server. |

## [◆ ](#ga396015e492b0fee8da37c7168d9cdb33)mqtt\_qos

| enum [mqtt\_qos](#ga396015e492b0fee8da37c7168d9cdb33) |
| --- |

`#include <[mqtt.h](mqtt_8h.md)>`

MQTT Quality of Service types.

| Enumerator | |
| --- | --- |
| MQTT\_QOS\_0\_AT\_MOST\_ONCE | Lowest Quality of Service, no acknowledgment needed for published message. |
| MQTT\_QOS\_1\_AT\_LEAST\_ONCE | Medium Quality of Service, if acknowledgment expected for published message, duplicate messages permitted. |
| MQTT\_QOS\_2\_EXACTLY\_ONCE | Highest Quality of Service, acknowledgment expected and message shall be published only once.  Message not published to interested parties unless client issues a PUBREL. |

## [◆ ](#gaca1e61c8b14b75544e253cea355274a8)mqtt\_suback\_return\_code

| enum [mqtt\_suback\_return\_code](#gaca1e61c8b14b75544e253cea355274a8) |
| --- |

`#include <[mqtt.h](mqtt_8h.md)>`

MQTT SUBACK return codes.

| Enumerator | |
| --- | --- |
| MQTT\_SUBACK\_SUCCESS\_QoS\_0 | Subscription with QoS 0 succeeded. |
| MQTT\_SUBACK\_SUCCESS\_QoS\_1 | Subscription with QoS 1 succeeded. |
| MQTT\_SUBACK\_SUCCESS\_QoS\_2 | Subscription with QoS 2 succeeded. |
| MQTT\_SUBACK\_FAILURE | Subscription for a topic failed. |

## [◆ ](#gaffc2c3078004cf8d24935be086ad63b4)mqtt\_transport\_type

| enum [mqtt\_transport\_type](#gaffc2c3078004cf8d24935be086ad63b4) |
| --- |

`#include <[mqtt.h](mqtt_8h.md)>`

MQTT transport type.

| Enumerator | |
| --- | --- |
| MQTT\_TRANSPORT\_NON\_SECURE | Use non secure TCP transport for MQTT connection. |
| MQTT\_TRANSPORT\_NUM | Shall not be used as a transport type.  Indicator of maximum transport types possible. |

## [◆ ](#ga90d152a4b0986e9a07a12c7c56f5e2a0)mqtt\_version

| enum [mqtt\_version](#ga90d152a4b0986e9a07a12c7c56f5e2a0) |
| --- |

`#include <[mqtt.h](mqtt_8h.md)>`

MQTT version protocol level.

| Enumerator | |
| --- | --- |
| MQTT\_VERSION\_3\_1\_0 | Protocol level for 3.1.0. |
| MQTT\_VERSION\_3\_1\_1 | Protocol level for 3.1.1. |

## Function Documentation

## [◆ ](#gafb2df41fad7c318f9fe75919919139bd)mqtt\_abort()

| int mqtt\_abort | ( | struct [mqtt\_client](structmqtt__client.md) \* | *client* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mqtt.h](mqtt_8h.md)>`

API to abort MQTT connection.

This will close the corresponding transport without closing the connection gracefully at the MQTT level (with disconnect message).

Parameters
:   | [in] | client | Identifies client instance for which procedure is requested. |
    | --- | --- | --- |

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#gad1376509ae7c946c840d103d8b59e9a1)mqtt\_client\_init()

| void mqtt\_client\_init | ( | struct [mqtt\_client](structmqtt__client.md) \* | *client* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mqtt.h](mqtt_8h.md)>`

Initializes the client instance.

Parameters
:   | [in] | client | Client instance for which the procedure is requested. Shall not be NULL. |
    | --- | --- | --- |

Note
:   Shall be called to initialize client structure, before setting any client parameters and before connecting to broker.

## [◆ ](#gad936f28553cb2e771a843512b0a315fa)mqtt\_connect()

| int mqtt\_connect | ( | struct [mqtt\_client](structmqtt__client.md) \* | *client* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mqtt.h](mqtt_8h.md)>`

API to request new MQTT client connection.

Parameters
:   | [in] | client | Client instance for which the procedure is requested. Shall not be NULL. |
    | --- | --- | --- |

Note
:   This memory is assumed to be resident until mqtt\_disconnect is called.
:   Any subsequent changes to parameters like broker address, user name, device id, etc. have no effect once MQTT connection is established.

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

Note
:   Default protocol revision used for connection request is 3.1.1. Please set client.protocol\_version = MQTT\_VERSION\_3\_1\_0 to use protocol 3.1.0.
:   Please modify

    ```
    CONFIG_MQTT_KEEPALIVE
    ```

    time to override default of 1 minute.

## [◆ ](#gad5e01a1b60c393adb0f7f34c1a90e6ff)mqtt\_disconnect()

| int mqtt\_disconnect | ( | struct [mqtt\_client](structmqtt__client.md) \* | *client* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mqtt.h](mqtt_8h.md)>`

API to disconnect MQTT connection.

Parameters
:   | [in] | client | Identifies client instance for which procedure is requested. |
    | --- | --- | --- |

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#ga2dbc3c158d63a6f57b362be94c22660a)mqtt\_input()

| int mqtt\_input | ( | struct [mqtt\_client](structmqtt__client.md) \* | *client* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mqtt.h](mqtt_8h.md)>`

Receive an incoming MQTT packet.

The registered callback will be called with the packet content.

Note
:   In case of PUBLISH message, the payload has to be read separately with [mqtt\_read\_publish\_payload](#ga3559cdd6093d75c6fe6792ec2a453172) function. The size of the payload to read is provided in the publish event structure.
:   This is a non-blocking call.

Parameters
:   | [in] | client | Client instance for which the procedure is requested. Shall not be NULL. |
    | --- | --- | --- |

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#gaa16bf7b0597ad00c4a3943235579e86b)mqtt\_keepalive\_time\_left()

| int mqtt\_keepalive\_time\_left | ( | const struct [mqtt\_client](structmqtt__client.md) \* | *client* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mqtt.h](mqtt_8h.md)>`

Helper function to determine when next keep alive message should be sent.

Can be used for instance as a source for [poll](group__bsd__sockets.md#gae2d9b8390c125624595e2b400a08ea29 "POSIX wrapper for zsock_poll.") timeout.

Parameters
:   | [in] | client | Client instance for which the procedure is requested. |
    | --- | --- | --- |

Returns
:   Time in milliseconds until next keep alive message is expected to be sent. Function will return -1 if keep alive messages are not enabled.

## [◆ ](#ga8b87710d01076c8e51b1a75634168269)mqtt\_live()

| int mqtt\_live | ( | struct [mqtt\_client](structmqtt__client.md) \* | *client* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mqtt.h](mqtt_8h.md)>`

This API should be called periodically for the client to be able to keep the connection alive by sending Ping Requests if need be.

Parameters
:   | [in] | client | Client instance for which the procedure is requested. Shall not be NULL. |
    | --- | --- | --- |

Note
:   Application shall ensure that the periodicity of calling this function makes it possible to respect the Keep Alive time agreed with the broker on connection. [mqtt\_connect](#gad936f28553cb2e771a843512b0a315fa) for details on Keep Alive time.

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#gad1d549d37b69a61e1bf8d9d213e02ca8)mqtt\_ping()

| int mqtt\_ping | ( | struct [mqtt\_client](structmqtt__client.md) \* | *client* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[mqtt.h](mqtt_8h.md)>`

API to send MQTT ping.

The use of this API is optional, as the library handles the connection keep-alive on it's own, see [mqtt\_live](#ga8b87710d01076c8e51b1a75634168269).

Parameters
:   | [in] | client | Identifies client instance for which procedure is requested. |
    | --- | --- | --- |

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#ga57745efa1bf6fbdf7eb1b3f01623e4c7)mqtt\_publish()

| int mqtt\_publish | ( | struct [mqtt\_client](structmqtt__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | const struct [mqtt\_publish\_param](structmqtt__publish__param.md) \* | *param* ) |

`#include <[mqtt.h](mqtt_8h.md)>`

API to publish messages on topics.

Parameters
:   | [in] | client | Client instance for which the procedure is requested. Shall not be NULL. |
    | --- | --- | --- |
    | [in] | param | Parameters to be used for the publish message. Shall not be NULL. |

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#gae9069fceec2c018e64cc6beb16aa055c)mqtt\_publish\_qos1\_ack()

| int mqtt\_publish\_qos1\_ack | ( | struct [mqtt\_client](structmqtt__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | const struct [mqtt\_puback\_param](structmqtt__puback__param.md) \* | *param* ) |

`#include <[mqtt.h](mqtt_8h.md)>`

API used by client to send acknowledgment on receiving QoS1 publish message.

Should be called on reception of [MQTT\_EVT\_PUBLISH](#gga0071fe013b9920711456ef51cc3e6d91aa893a345e05e796cfd28392c1c4d8cf9) with QoS level [MQTT\_QOS\_1\_AT\_LEAST\_ONCE](#gga396015e492b0fee8da37c7168d9cdb33a732d9d294b41bd472ef221c8dff0731d).

Parameters
:   | [in] | client | Client instance for which the procedure is requested. Shall not be NULL. |
    | --- | --- | --- |
    | [in] | param | Identifies message being acknowledged. |

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#ga2b17999e845d613f5b0b20015b8204f3)mqtt\_publish\_qos2\_complete()

| int mqtt\_publish\_qos2\_complete | ( | struct [mqtt\_client](structmqtt__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | const struct [mqtt\_pubcomp\_param](structmqtt__pubcomp__param.md) \* | *param* ) |

`#include <[mqtt.h](mqtt_8h.md)>`

API used by client to send acknowledgment on receiving QoS2 publish release message.

Should be called on reception of [MQTT\_EVT\_PUBREL](#gga0071fe013b9920711456ef51cc3e6d91ab35ebaf4dcc6698471eb16a41c8252a2).

Parameters
:   | [in] | client | Identifies client instance for which the procedure is requested. Shall not be NULL. |
    | --- | --- | --- |
    | [in] | param | Identifies message being completed. |

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#gacbe41b83d9c0676d0d4cf01dd91765eb)mqtt\_publish\_qos2\_receive()

| int mqtt\_publish\_qos2\_receive | ( | struct [mqtt\_client](structmqtt__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | const struct [mqtt\_pubrec\_param](structmqtt__pubrec__param.md) \* | *param* ) |

`#include <[mqtt.h](mqtt_8h.md)>`

API used by client to send acknowledgment on receiving QoS2 publish message.

Should be called on reception of [MQTT\_EVT\_PUBLISH](#gga0071fe013b9920711456ef51cc3e6d91aa893a345e05e796cfd28392c1c4d8cf9) with QoS level [MQTT\_QOS\_2\_EXACTLY\_ONCE](#gga396015e492b0fee8da37c7168d9cdb33a9012ddca1943a824454ac14a85bcf117).

Parameters
:   | [in] | client | Identifies client instance for which the procedure is requested. Shall not be NULL. |
    | --- | --- | --- |
    | [in] | param | Identifies message being acknowledged. |

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#ga6c952ed014f78774096bfb6099794803)mqtt\_publish\_qos2\_release()

| int mqtt\_publish\_qos2\_release | ( | struct [mqtt\_client](structmqtt__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | const struct [mqtt\_pubrel\_param](structmqtt__pubrel__param.md) \* | *param* ) |

`#include <[mqtt.h](mqtt_8h.md)>`

API used by client to request release of QoS2 publish message.

Should be called on reception of [MQTT\_EVT\_PUBREC](#gga0071fe013b9920711456ef51cc3e6d91a1d5f6ba2524f935dd9625d85638eda87).

Parameters
:   | [in] | client | Client instance for which the procedure is requested. Shall not be NULL. |
    | --- | --- | --- |
    | [in] | param | Identifies message being released. |

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#ga3559cdd6093d75c6fe6792ec2a453172)mqtt\_read\_publish\_payload()

| int mqtt\_read\_publish\_payload | ( | struct [mqtt\_client](structmqtt__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | void \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) |

`#include <[mqtt.h](mqtt_8h.md)>`

Read the payload of the received PUBLISH message.

This function should be called within the MQTT event handler, when MQTT PUBLISH message is notified.

Note
:   This is a non-blocking call.

Parameters
:   | [in] | client | Client instance for which the procedure is requested. Shall not be NULL. |
    | --- | --- | --- |
    | [out] | buffer | Buffer where payload should be stored. |
    | [in] | length | Length of the buffer, in bytes. |

Returns
:   Number of bytes read or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#ga05213aceaa9e9cbbfaa9bab7a78b3d25)mqtt\_read\_publish\_payload\_blocking()

| int mqtt\_read\_publish\_payload\_blocking | ( | struct [mqtt\_client](structmqtt__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | void \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) |

`#include <[mqtt.h](mqtt_8h.md)>`

Blocking version of [mqtt\_read\_publish\_payload](#ga3559cdd6093d75c6fe6792ec2a453172) function.

Parameters
:   | [in] | client | Client instance for which the procedure is requested. Shall not be NULL. |
    | --- | --- | --- |
    | [out] | buffer | Buffer where payload should be stored. |
    | [in] | length | Length of the buffer, in bytes. |

Returns
:   Number of bytes read or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#ga31823965ec34a253793b40b50e800417)mqtt\_readall\_publish\_payload()

| int mqtt\_readall\_publish\_payload | ( | struct [mqtt\_client](structmqtt__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buffer*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) |

`#include <[mqtt.h](mqtt_8h.md)>`

Blocking version of [mqtt\_read\_publish\_payload](#ga3559cdd6093d75c6fe6792ec2a453172) function which runs until the required number of bytes are read.

Parameters
:   | [in] | client | Client instance for which the procedure is requested. Shall not be NULL. |
    | --- | --- | --- |
    | [out] | buffer | Buffer where payload should be stored. |
    | [in] | length | Number of bytes to read. |

Returns
:   0 if success, otherwise a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#ga40d226b891b8f62f2c486bbb11ce9678)mqtt\_subscribe()

| int mqtt\_subscribe | ( | struct [mqtt\_client](structmqtt__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | const struct [mqtt\_subscription\_list](structmqtt__subscription__list.md) \* | *param* ) |

`#include <[mqtt.h](mqtt_8h.md)>`

API to request subscription of one or more topics on the connection.

Parameters
:   | [in] | client | Identifies client instance for which the procedure is requested. Shall not be NULL. |
    | --- | --- | --- |
    | [in] | param | Subscription parameters. Shall not be NULL. |

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

## [◆ ](#ga4ff43a198e93e332b5553a4d0b59261d)mqtt\_unsubscribe()

| int mqtt\_unsubscribe | ( | struct [mqtt\_client](structmqtt__client.md) \* | *client*, |
| --- | --- | --- | --- |
|  |  | const struct [mqtt\_subscription\_list](structmqtt__subscription__list.md) \* | *param* ) |

`#include <[mqtt.h](mqtt_8h.md)>`

API to request unsubscription of one or more topics on the connection.

Parameters
:   | [in] | client | Identifies client instance for which the procedure is requested. Shall not be NULL. |
    | --- | --- | --- |
    | [in] | param | Parameters describing topics being unsubscribed from. Shall not be NULL. |

Note
:   QoS included in topic description is unused in this API.

Returns
:   0 or a negative error code ([errno.h](errno_8h.md "System error numbers.")) indicating reason of failure.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
