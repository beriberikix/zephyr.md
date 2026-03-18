---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mqtt_8h.html
original_path: doxygen/html/mqtt_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt.h File Reference

`#include <stddef.h>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/net/tls_credentials.h](tls__credentials_8h_source.md)>`  
`#include <[zephyr/net/net_ip.h](net__ip_8h_source.md)>`  
`#include <[zephyr/sys/mutex.h](mutex_8h_source.md)>`  
`#include <[zephyr/net/websocket.h](websocket_8h_source.md)>`

[Go to the source code of this file.](mqtt_8h_source.md)

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
| #define | [MQTT\_UTF8\_LITERAL](group__mqtt__socket.md#gaeaa4fcf581c7d6be755f9a053a3b488c)(literal) |
|  | Initialize UTF-8 encoded string from C literal string. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [mqtt\_evt\_cb\_t](group__mqtt__socket.md#gabdf01ededb62ceb4c1608a64cb718a8c)) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_evt](structmqtt__evt.md) \*evt) |
|  | Asynchronous event notification callback registered by the application. |

| Enumerations | |
| --- | --- |
| enum | [mqtt\_evt\_type](group__mqtt__socket.md#ga0071fe013b9920711456ef51cc3e6d91) {     [MQTT\_EVT\_CONNACK](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91ab6e626b5a1eda76b32053ccbb4b7b5f3) , [MQTT\_EVT\_DISCONNECT](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a8de64478f7ae463d7844fc2e786ce032) , [MQTT\_EVT\_PUBLISH](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91aa893a345e05e796cfd28392c1c4d8cf9) , [MQTT\_EVT\_PUBACK](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a2f25d5d4ca704ab63439d4706d3587de) ,     [MQTT\_EVT\_PUBREC](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a1d5f6ba2524f935dd9625d85638eda87) , [MQTT\_EVT\_PUBREL](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91ab35ebaf4dcc6698471eb16a41c8252a2) , [MQTT\_EVT\_PUBCOMP](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91afdba5e48987b4355f445d35b4dc056e8) , [MQTT\_EVT\_SUBACK](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a67caa558ae7975548b3c4e1c1de5f8fb) ,     [MQTT\_EVT\_UNSUBACK](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91aa5c333ddf366e44f932ec5545ed75bb2) , [MQTT\_EVT\_PINGRESP](group__mqtt__socket.md#gga0071fe013b9920711456ef51cc3e6d91a52842872177b26e5e0e45a3c66fdb0b5)   } |
|  | MQTT Asynchronous Events notified to the application from the module through the callback registered by the application. [More...](group__mqtt__socket.md#ga0071fe013b9920711456ef51cc3e6d91) |
| enum | [mqtt\_version](group__mqtt__socket.md#ga90d152a4b0986e9a07a12c7c56f5e2a0) { [MQTT\_VERSION\_3\_1\_0](group__mqtt__socket.md#gga90d152a4b0986e9a07a12c7c56f5e2a0ac93057183f274a064e118af6b4d681e7) = 3 , [MQTT\_VERSION\_3\_1\_1](group__mqtt__socket.md#gga90d152a4b0986e9a07a12c7c56f5e2a0ad2926cb14db1fcfb95a47f45d2f5b08e) = 4 } |
|  | MQTT version protocol level. [More...](group__mqtt__socket.md#ga90d152a4b0986e9a07a12c7c56f5e2a0) |
| enum | [mqtt\_qos](group__mqtt__socket.md#ga396015e492b0fee8da37c7168d9cdb33) { [MQTT\_QOS\_0\_AT\_MOST\_ONCE](group__mqtt__socket.md#gga396015e492b0fee8da37c7168d9cdb33a2ea1051887beb30d7c1fd61b5e153f6e) = 0x00 , [MQTT\_QOS\_1\_AT\_LEAST\_ONCE](group__mqtt__socket.md#gga396015e492b0fee8da37c7168d9cdb33a732d9d294b41bd472ef221c8dff0731d) = 0x01 , [MQTT\_QOS\_2\_EXACTLY\_ONCE](group__mqtt__socket.md#gga396015e492b0fee8da37c7168d9cdb33a9012ddca1943a824454ac14a85bcf117) = 0x02 } |
|  | MQTT Quality of Service types. [More...](group__mqtt__socket.md#ga396015e492b0fee8da37c7168d9cdb33) |
| enum | [mqtt\_conn\_return\_code](group__mqtt__socket.md#gaa17b38ed9c7e65f3e01ad906b24bb618) {     [MQTT\_CONNECTION\_ACCEPTED](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618a2fdd911a8978b8df2254766c1e3fd050) = 0x00 , [MQTT\_UNACCEPTABLE\_PROTOCOL\_VERSION](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618a9195e642b0b9e594d96aff84f0696744) = 0x01 , [MQTT\_IDENTIFIER\_REJECTED](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618aa662f46a044e31ae26397adffee82141) = 0x02 , [MQTT\_SERVER\_UNAVAILABLE](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618afe234e7084078871a567359819458df3) = 0x03 ,     [MQTT\_BAD\_USER\_NAME\_OR\_PASSWORD](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618aa12d243cef12e3e7b1f4e245f64a1134) = 0x04 , [MQTT\_NOT\_AUTHORIZED](group__mqtt__socket.md#ggaa17b38ed9c7e65f3e01ad906b24bb618a4d101dcf5a101d90ae26ba8fe54a27eb) = 0x05   } |
|  | MQTT CONNACK return codes. [More...](group__mqtt__socket.md#gaa17b38ed9c7e65f3e01ad906b24bb618) |
| enum | [mqtt\_suback\_return\_code](group__mqtt__socket.md#gaca1e61c8b14b75544e253cea355274a8) { [MQTT\_SUBACK\_SUCCESS\_QoS\_0](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8a835fdffd58e7ad800d549c9dfce1ce01) = 0x00 , [MQTT\_SUBACK\_SUCCESS\_QoS\_1](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8afd0c8b7b9c39b3e242f33f7603b3ca9c) = 0x01 , [MQTT\_SUBACK\_SUCCESS\_QoS\_2](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8ae8702eb6a2944444abd9b2f6c1fb2e1b) = 0x02 , [MQTT\_SUBACK\_FAILURE](group__mqtt__socket.md#ggaca1e61c8b14b75544e253cea355274a8a08b9651ef43ea219f29125fcb43952f7) = 0x80 } |
|  | MQTT SUBACK return codes. [More...](group__mqtt__socket.md#gaca1e61c8b14b75544e253cea355274a8) |
| enum | [mqtt\_transport\_type](group__mqtt__socket.md#gaffc2c3078004cf8d24935be086ad63b4) { [MQTT\_TRANSPORT\_NON\_SECURE](group__mqtt__socket.md#ggaffc2c3078004cf8d24935be086ad63b4a981f7e2ca25c5e478bf658750e26972a) , [MQTT\_TRANSPORT\_NUM](group__mqtt__socket.md#ggaffc2c3078004cf8d24935be086ad63b4a61056a250c98f3d29ccf5cdbdda3d3df) } |
|  | MQTT transport type. [More...](group__mqtt__socket.md#gaffc2c3078004cf8d24935be086ad63b4) |

| Functions | |
| --- | --- |
| void | [mqtt\_client\_init](group__mqtt__socket.md#gad1376509ae7c946c840d103d8b59e9a1) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | Initializes the client instance. |
| int | [mqtt\_connect](group__mqtt__socket.md#gad936f28553cb2e771a843512b0a315fa) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | API to request new MQTT client connection. |
| int | [mqtt\_publish](group__mqtt__socket.md#ga57745efa1bf6fbdf7eb1b3f01623e4c7) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_publish\_param](structmqtt__publish__param.md) \*param) |
|  | API to publish messages on topics. |
| int | [mqtt\_publish\_qos1\_ack](group__mqtt__socket.md#gae9069fceec2c018e64cc6beb16aa055c) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_puback\_param](structmqtt__puback__param.md) \*param) |
|  | API used by client to send acknowledgment on receiving QoS1 publish message. |
| int | [mqtt\_publish\_qos2\_receive](group__mqtt__socket.md#gacbe41b83d9c0676d0d4cf01dd91765eb) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_pubrec\_param](structmqtt__pubrec__param.md) \*param) |
|  | API used by client to send acknowledgment on receiving QoS2 publish message. |
| int | [mqtt\_publish\_qos2\_release](group__mqtt__socket.md#ga6c952ed014f78774096bfb6099794803) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_pubrel\_param](structmqtt__pubrel__param.md) \*param) |
|  | API used by client to request release of QoS2 publish message. |
| int | [mqtt\_publish\_qos2\_complete](group__mqtt__socket.md#ga2b17999e845d613f5b0b20015b8204f3) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_pubcomp\_param](structmqtt__pubcomp__param.md) \*param) |
|  | API used by client to send acknowledgment on receiving QoS2 publish release message. |
| int | [mqtt\_subscribe](group__mqtt__socket.md#ga40d226b891b8f62f2c486bbb11ce9678) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_subscription\_list](structmqtt__subscription__list.md) \*param) |
|  | API to request subscription of one or more topics on the connection. |
| int | [mqtt\_unsubscribe](group__mqtt__socket.md#ga4ff43a198e93e332b5553a4d0b59261d) (struct [mqtt\_client](structmqtt__client.md) \*client, const struct [mqtt\_subscription\_list](structmqtt__subscription__list.md) \*param) |
|  | API to request unsubscription of one or more topics on the connection. |
| int | [mqtt\_ping](group__mqtt__socket.md#gad1d549d37b69a61e1bf8d9d213e02ca8) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | API to send MQTT ping. |
| int | [mqtt\_disconnect](group__mqtt__socket.md#gad5e01a1b60c393adb0f7f34c1a90e6ff) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | API to disconnect MQTT connection. |
| int | [mqtt\_abort](group__mqtt__socket.md#gafb2df41fad7c318f9fe75919919139bd) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | API to abort MQTT connection. |
| int | [mqtt\_live](group__mqtt__socket.md#ga8b87710d01076c8e51b1a75634168269) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | This API should be called periodically for the client to be able to keep the connection alive by sending Ping Requests if need be. |
| int | [mqtt\_keepalive\_time\_left](group__mqtt__socket.md#gaa16bf7b0597ad00c4a3943235579e86b) (const struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | Helper function to determine when next keep alive message should be sent. |
| int | [mqtt\_input](group__mqtt__socket.md#ga2dbc3c158d63a6f57b362be94c22660a) (struct [mqtt\_client](structmqtt__client.md) \*client) |
|  | Receive an incoming MQTT packet. |
| int | [mqtt\_read\_publish\_payload](group__mqtt__socket.md#ga3559cdd6093d75c6fe6792ec2a453172) (struct [mqtt\_client](structmqtt__client.md) \*client, void \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Read the payload of the received PUBLISH message. |
| int | [mqtt\_read\_publish\_payload\_blocking](group__mqtt__socket.md#ga05213aceaa9e9cbbfaa9bab7a78b3d25) (struct [mqtt\_client](structmqtt__client.md) \*client, void \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Blocking version of [mqtt\_read\_publish\_payload](group__mqtt__socket.md#ga3559cdd6093d75c6fe6792ec2a453172 "mqtt_read_publish_payload") function. |
| int | [mqtt\_readall\_publish\_payload](group__mqtt__socket.md#ga31823965ec34a253793b40b50e800417) (struct [mqtt\_client](structmqtt__client.md) \*client, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buffer, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Blocking version of [mqtt\_read\_publish\_payload](group__mqtt__socket.md#ga3559cdd6093d75c6fe6792ec2a453172 "mqtt_read_publish_payload") function which runs until the required number of bytes are read. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [mqtt.h](mqtt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
