---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mqtt__sn_8h.html
original_path: doxygen/html/mqtt__sn_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_sn.h File Reference

`#include <stddef.h>`  
`#include <[zephyr/net/buf.h](net_2buf_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`

[Go to the source code of this file.](mqtt__sn_8h_source.md)

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
| #define | [MQTT\_SN\_DATA\_STRING\_LITERAL](group__mqtt__sn__socket.md#gaf8223bf7e5548323c453b30be031e37e)(literal) |
|  | Initialize memory buffer from C literal string. |
| #define | [MQTT\_SN\_DATA\_BYTES](group__mqtt__sn__socket.md#gabb58a0e4aa418a864f1208ff188f40bc)(...) |
|  | Initialize memory buffer from single bytes. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [mqtt\_sn\_evt\_cb\_t](group__mqtt__sn__socket.md#gaecd8b966f3e2112261993f8a2cd5c94a)) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, const struct [mqtt\_sn\_evt](structmqtt__sn__evt.md) \*evt) |
|  | Asynchronous event notification callback registered by the application. |

| Enumerations | |
| --- | --- |
| enum | [mqtt\_sn\_qos](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786) { [MQTT\_SN\_QOS\_0](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786acb18ea4162f8ccac24e733da5511b389) , [MQTT\_SN\_QOS\_1](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a785b3ab4cde3c861f861009b00e584da) , [MQTT\_SN\_QOS\_2](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a4b01cb386e18de88b8f26973a65771f4) , [MQTT\_SN\_QOS\_M1](group__mqtt__sn__socket.md#gga8072226d2d96e184137ef40775389786a2f0dce2f9249cea36d77ea16d21f61b9) } |
|  | Quality of Service. [More...](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786) |
| enum | [mqtt\_sn\_topic\_type](group__mqtt__sn__socket.md#gabca9262da31b09086b0f802d15eea3fd) { [MQTT\_SN\_TOPIC\_TYPE\_NORMAL](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fda18ad286ee41092116dd734faba7f3e9b) , [MQTT\_SN\_TOPIC\_TYPE\_PREDEF](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fda48301bc2ca23f5f53c2e320b309f923b) , [MQTT\_SN\_TOPIC\_TYPE\_SHORT](group__mqtt__sn__socket.md#ggabca9262da31b09086b0f802d15eea3fdad142dda8e35f4cbe428dc572fc005730) } |
|  | MQTT-SN topic types. [More...](group__mqtt__sn__socket.md#gabca9262da31b09086b0f802d15eea3fd) |
| enum | [mqtt\_sn\_return\_code](group__mqtt__sn__socket.md#gaab8c9d8ddbaa2af542fdcd3e4178ea9e) { [MQTT\_SN\_CODE\_ACCEPTED](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea9075123172fff71a180c280b5ca99f1c) = 0x00 , [MQTT\_SN\_CODE\_REJECTED\_CONGESTION](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9ea94471cce989efc2514bf37b54848cee7) = 0x01 , [MQTT\_SN\_CODE\_REJECTED\_TOPIC\_ID](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eac6de6a7f4b8becc11e83fb60e30e2ef3) = 0x02 , [MQTT\_SN\_CODE\_REJECTED\_NOTSUP](group__mqtt__sn__socket.md#ggaab8c9d8ddbaa2af542fdcd3e4178ea9eaa612db276815fadc5b379f13e7eb78f5) = 0x03 } |
|  | MQTT-SN return codes. [More...](group__mqtt__sn__socket.md#gaab8c9d8ddbaa2af542fdcd3e4178ea9e) |
| enum | [mqtt\_sn\_evt\_type](group__mqtt__sn__socket.md#gaa52518be4aa308dda9552e14d0045c42) {     [MQTT\_SN\_EVT\_CONNECTED](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a4c6c473a7ef6e0fd362b1b865fe3d6a6) , [MQTT\_SN\_EVT\_DISCONNECTED](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a9a155ce397e5eb73496bd85ef7cc44bf) , [MQTT\_SN\_EVT\_ASLEEP](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a65d0caaadc8ad95dffd8beb5c77ceb3f) , [MQTT\_SN\_EVT\_AWAKE](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42ae0a691ff1d222e12aada6de2706090bd) ,     [MQTT\_SN\_EVT\_PUBLISH](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a5923dab1ac92c6d186920368440b53bf) , [MQTT\_SN\_EVT\_PINGRESP](group__mqtt__sn__socket.md#ggaa52518be4aa308dda9552e14d0045c42a06e53118fc5799c924de346ac7ee1135)   } |
|  | Event types that can be emitted by the library. [More...](group__mqtt__sn__socket.md#gaa52518be4aa308dda9552e14d0045c42) |

| Functions | |
| --- | --- |
| int | [mqtt\_sn\_client\_init](group__mqtt__sn__socket.md#gae6a3f7a7762653474df97364ef69fc74) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, const struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*client\_id, struct [mqtt\_sn\_transport](structmqtt__sn__transport.md) \*transport, [mqtt\_sn\_evt\_cb\_t](group__mqtt__sn__socket.md#gaecd8b966f3e2112261993f8a2cd5c94a) evt\_cb, void \*tx, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) txsz, void \*rx, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) rxsz) |
|  | Initialize a client. |
| void | [mqtt\_sn\_client\_deinit](group__mqtt__sn__socket.md#ga67d69e4e3f00b31b5ea3b37fb6d653b1) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client) |
|  | Deinitialize the client. |
| int | [mqtt\_sn\_connect](group__mqtt__sn__socket.md#ga8c2a525f1c30e5d5ff37180d33a76d4d) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) will, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) clean\_session) |
|  | Connect the client. |
| int | [mqtt\_sn\_disconnect](group__mqtt__sn__socket.md#gab9cba16f8ce06f606ee81e0d34deb862) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client) |
|  | Disconnect the client. |
| int | [mqtt\_sn\_sleep](group__mqtt__sn__socket.md#gaf29a6339419ea02052fe53a18bb8e5ee) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) duration) |
|  | Set the client into sleep state. |
| int | [mqtt\_sn\_subscribe](group__mqtt__sn__socket.md#ga9b481db6d39dee05e2c58d4c721fe0a5) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, enum [mqtt\_sn\_qos](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786) qos, struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*topic\_name) |
|  | Subscribe to a given topic. |
| int | [mqtt\_sn\_unsubscribe](group__mqtt__sn__socket.md#ga1bcd2a0f52610708bebb4b3b6d6cbf35) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, enum [mqtt\_sn\_qos](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786) qos, struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*topic\_name) |
|  | Unsubscribe from a topic. |
| int | [mqtt\_sn\_publish](group__mqtt__sn__socket.md#ga434c3626ceaf3a9b60c5ffb75e9b5b56) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, enum [mqtt\_sn\_qos](group__mqtt__sn__socket.md#ga8072226d2d96e184137ef40775389786) qos, struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*topic\_name, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) retain, struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*data) |
|  | Publish a value. |
| int | [mqtt\_sn\_input](group__mqtt__sn__socket.md#gafa1f81168d44152ad72c5f3d1c744b49) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client) |
|  | Check the transport for new incoming data. |
| int | [mqtt\_sn\_get\_topic\_name](group__mqtt__sn__socket.md#gade962a4da5311a403893ba24714dc332) (struct [mqtt\_sn\_client](structmqtt__sn__client.md) \*client, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id, struct [mqtt\_sn\_data](structmqtt__sn__data.md) \*topic\_name) |
|  | Get topic name by topic ID. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [mqtt\_sn.h](mqtt__sn_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
