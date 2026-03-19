---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structmqtt__sec__config.html
original_path: doxygen/html/structmqtt__sec__config.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mqtt\_sec\_config Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [MQTT Client library](group__mqtt__socket.md)

TLS configuration for secure MQTT transports.
[More...](#details)

`#include <[mqtt.h](mqtt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int | [peer\_verify](#a0e04768b6589823464c2d13c31230cad) |
|  | Indicates the preference for peer verification. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [cipher\_count](#a25415e32e00808fb6a24187f4234059f) |
|  | Indicates the number of entries in the cipher list. |
| const int \* | [cipher\_list](#a179a97d56a7a12d5afb60257a67ce46c) |
|  | Indicates the list of ciphers to be used for the session. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sec\_tag\_count](#a6d59afc061a749ea31f5bd415918a3e0) |
|  | Indicates the number of entries in the sec tag list. |
| const [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) \* | [sec\_tag\_list](#adeb8630a9e73c4b3226afa1c9a5060fe) |
|  | Indicates the list of security tags to be used for the session. |
| const char \* | [hostname](#af7a0ee827bf98fde264000f4c9020c15) |
|  | Peer hostname for ceritificate verification. |
| int | [cert\_nocopy](#a5beac5704fec3e399e5c0099a57ce115) |
|  | Indicates the preference for copying certificates to the heap. |

## Detailed Description

TLS configuration for secure MQTT transports.

## Field Documentation

## [◆ ](#a5beac5704fec3e399e5c0099a57ce115)cert\_nocopy

| int mqtt\_sec\_config::cert\_nocopy |
| --- |

Indicates the preference for copying certificates to the heap.

## [◆ ](#a25415e32e00808fb6a24187f4234059f)cipher\_count

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_sec\_config::cipher\_count |
| --- |

Indicates the number of entries in the cipher list.

## [◆ ](#a179a97d56a7a12d5afb60257a67ce46c)cipher\_list

| const int\* mqtt\_sec\_config::cipher\_list |
| --- |

Indicates the list of ciphers to be used for the session.

May be NULL to use the default ciphers.

## [◆ ](#af7a0ee827bf98fde264000f4c9020c15)hostname

| const char\* mqtt\_sec\_config::hostname |
| --- |

Peer hostname for ceritificate verification.

May be NULL to skip hostname verification.

## [◆ ](#a0e04768b6589823464c2d13c31230cad)peer\_verify

| int mqtt\_sec\_config::peer\_verify |
| --- |

Indicates the preference for peer verification.

## [◆ ](#a6d59afc061a749ea31f5bd415918a3e0)sec\_tag\_count

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) mqtt\_sec\_config::sec\_tag\_count |
| --- |

Indicates the number of entries in the sec tag list.

## [◆ ](#adeb8630a9e73c4b3226afa1c9a5060fe)sec\_tag\_list

| const [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3)\* mqtt\_sec\_config::sec\_tag\_list |
| --- |

Indicates the list of security tags to be used for the session.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[mqtt.h](mqtt_8h_source.md)

- [mqtt\_sec\_config](structmqtt__sec__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
