---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structlwm2m__ctx.html
original_path: doxygen/html/structlwm2m__ctx.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lwm2m\_ctx Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [LwM2M high-level API](group__lwm2m__api.md)

LwM2M context structure to maintain information for a single LwM2M connection.
[More...](#details)

`#include <[lwm2m.h](lwm2m_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [sockaddr](structsockaddr.md) | [remote\_addr](#a4ed594ecc5d442ffc2a604a879f5bfb7) |
|  | Destination address storage. |
| void \* | [processed\_req](#a9b56ad9b3f2202d25b8c48f34a898dd3) |
|  | A pointer to currently processed request, for internal LwM2M engine use. |
| [lwm2m\_set\_sockopt\_cb\_t](group__lwm2m__api.md#ga92d2227f37e7d382bc4f1a7bae21b872) | [set\_socketoptions](#a8714a3ee6870515631fd75e74644d39c) |
|  | Custom socket options. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [use\_dtls](#aeb1e3ffc83853f74f2201f582917c2ce) |
|  | Flag to indicate if context should use DTLS. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [connection\_suspended](#aff523bc7473073c917ff1c888da7bece) |
|  | Flag to indicate that the socket connection is suspended. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [buffer\_client\_messages](#ac6709d32a87ece72c7cdf283c4ff60c0) |
|  | Flag to indicate that the client is buffering Notifications and Send messages. |
| int | [sec\_obj\_inst](#ab5fe85963a265f9c059a25138a637e02) |
|  | Current index of Security Object used for server credentials. |
| int | [srv\_obj\_inst](#a76d92a14bf1729d7b0fee174c51ed4bf) |
|  | Current index of Server Object used in this context. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bootstrap\_mode](#aafa787c2b7ea7599c51d9247ea9f1090) |
|  | Flag to enable BOOTSTRAP interface. |
| int | [sock\_fd](#afed1a599a72f131e4f196848c3e6fe85) |
|  | Socket File Descriptor. |
| [lwm2m\_socket\_fault\_cb\_t](group__lwm2m__api.md#gae7bf50f9abf1b82b76ac3e9175e685ac) | [fault\_cb](#a1b90780926f3cda2d48dfa8f94b1efd8) |
|  | Socket fault callback. |
| [lwm2m\_observe\_cb\_t](group__lwm2m__api.md#gad7bea67e16e1e831e0f949dbf83d5afe) | [observe\_cb](#a412bd706adcd17ec8c00f1779012a845) |
|  | Callback for new or cancelled observations, and acknowledged or timed out notifications. |
| [lwm2m\_ctx\_event\_cb\_t](group__lwm2m__api.md#ga38dbaf038426efc75d889c4a0666dac9) | [event\_cb](#ab01ec6be0effa24dde31363a476eccbb) |
|  | Callback for client events. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [validate\_buf](#a574b50b9ec4cdfb5fac53a9b6d8c31d5) [CONFIG\_LWM2M\_ENGINE\_VALIDATION\_BUFFER\_SIZE] |
|  | Validation buffer. |
| void(\* | [set\_socket\_state](#ad3d66164415325e7009d1a4c1111f4b3) )(int fd, enum [lwm2m\_socket\_states](group__lwm2m__api.md#ga7611c1aebb0309ee8340e06dd8ee234d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Callback to indicate transmission states. |
| DTLS related information | |
| Available only when `CONFIG_LWM2M_DTLS_SUPPORT` is enabled and [lwm2m\_ctx::use\_dtls](#aeb1e3ffc83853f74f2201f582917c2ce) is set to true. | |
| int | [tls\_tag](#a6c4c9025a17a3dc3451651cb1f83d575) |
|  | TLS tag is set by client as a reference used when the LwM2M engine calls tls\_credential\_(add|delete). |
| char \* | [desthostname](#a342cb5a0aaf9e5bc53228d3b0cc0fd43) |
|  | Destination hostname. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [desthostnamelen](#aff084b28e547a81bd71215125c28f705) |
|  | Destination hostname length. |
| int(\* | [load\_credentials](#a5f17296cd4600b25515e0952dc61ea97) )(struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx) |
|  | Custom load\_credentials function. |

## Detailed Description

LwM2M context structure to maintain information for a single LwM2M connection.

## Field Documentation

## [◆ ](#aafa787c2b7ea7599c51d9247ea9f1090)bootstrap\_mode

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) lwm2m\_ctx::bootstrap\_mode |
| --- |

Flag to enable BOOTSTRAP interface.

See Section "Bootstrap Interface" of LwM2M Technical Specification for more information.

## [◆ ](#ac6709d32a87ece72c7cdf283c4ff60c0)buffer\_client\_messages

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) lwm2m\_ctx::buffer\_client\_messages |
| --- |

Flag to indicate that the client is buffering Notifications and Send messages.

True value buffer Notifications and Send messages.

## [◆ ](#aff523bc7473073c917ff1c888da7bece)connection\_suspended

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) lwm2m\_ctx::connection\_suspended |
| --- |

Flag to indicate that the socket connection is suspended.

With queue mode, this will tell if there is a need to reconnect.

## [◆ ](#a342cb5a0aaf9e5bc53228d3b0cc0fd43)desthostname

| char\* lwm2m\_ctx::desthostname |
| --- |

Destination hostname.

When MBEDTLS SNI is enabled socket must be set with destination server hostname.

## [◆ ](#aff084b28e547a81bd71215125c28f705)desthostnamelen

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lwm2m\_ctx::desthostnamelen |
| --- |

Destination hostname length.

## [◆ ](#ab01ec6be0effa24dde31363a476eccbb)event\_cb

| [lwm2m\_ctx\_event\_cb\_t](group__lwm2m__api.md#ga38dbaf038426efc75d889c4a0666dac9) lwm2m\_ctx::event\_cb |
| --- |

Callback for client events.

## [◆ ](#a1b90780926f3cda2d48dfa8f94b1efd8)fault\_cb

| [lwm2m\_socket\_fault\_cb\_t](group__lwm2m__api.md#gae7bf50f9abf1b82b76ac3e9175e685ac) lwm2m\_ctx::fault\_cb |
| --- |

Socket fault callback.

LwM2M processing thread will call this callback in case of socket errors on receive.

## [◆ ](#a5f17296cd4600b25515e0952dc61ea97)load\_credentials

| int(\* lwm2m\_ctx::load\_credentials) (struct [lwm2m\_ctx](structlwm2m__ctx.md) \*client\_ctx) |
| --- |

Custom load\_credentials function.

Client can set load\_credentials function as a way of overriding the default behavior of load\_tls\_credential() in lwm2m\_engine.c

## [◆ ](#a412bd706adcd17ec8c00f1779012a845)observe\_cb

| [lwm2m\_observe\_cb\_t](group__lwm2m__api.md#gad7bea67e16e1e831e0f949dbf83d5afe) lwm2m\_ctx::observe\_cb |
| --- |

Callback for new or cancelled observations, and acknowledged or timed out notifications.

## [◆ ](#a9b56ad9b3f2202d25b8c48f34a898dd3)processed\_req

| void\* lwm2m\_ctx::processed\_req |
| --- |

A pointer to currently processed request, for internal LwM2M engine use.

The underlying type is struct lwm2m\_message, but since it's declared in a private header and not exposed to the application, it's stored as a void pointer.

## [◆ ](#a4ed594ecc5d442ffc2a604a879f5bfb7)remote\_addr

| struct [sockaddr](structsockaddr.md) lwm2m\_ctx::remote\_addr |
| --- |

Destination address storage.

## [◆ ](#ab5fe85963a265f9c059a25138a637e02)sec\_obj\_inst

| int lwm2m\_ctx::sec\_obj\_inst |
| --- |

Current index of Security Object used for server credentials.

## [◆ ](#ad3d66164415325e7009d1a4c1111f4b3)set\_socket\_state

| void(\* lwm2m\_ctx::set\_socket\_state) (int fd, enum [lwm2m\_socket\_states](group__lwm2m__api.md#ga7611c1aebb0309ee8340e06dd8ee234d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
| --- |

Callback to indicate transmission states.

Client application may request LwM2M engine to indicate hints about transmission states and use that information to control various power saving modes.

## [◆ ](#a8714a3ee6870515631fd75e74644d39c)set\_socketoptions

| [lwm2m\_set\_sockopt\_cb\_t](group__lwm2m__api.md#ga92d2227f37e7d382bc4f1a7bae21b872) lwm2m\_ctx::set\_socketoptions |
| --- |

Custom socket options.

Client can override default socket options by providing a callback that is called after a socket is created and before connect.

## [◆ ](#afed1a599a72f131e4f196848c3e6fe85)sock\_fd

| int lwm2m\_ctx::sock\_fd |
| --- |

Socket File Descriptor.

## [◆ ](#a76d92a14bf1729d7b0fee174c51ed4bf)srv\_obj\_inst

| int lwm2m\_ctx::srv\_obj\_inst |
| --- |

Current index of Server Object used in this context.

## [◆ ](#a6c4c9025a17a3dc3451651cb1f83d575)tls\_tag

| int lwm2m\_ctx::tls\_tag |
| --- |

TLS tag is set by client as a reference used when the LwM2M engine calls tls\_credential\_(add|delete).

## [◆ ](#aeb1e3ffc83853f74f2201f582917c2ce)use\_dtls

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) lwm2m\_ctx::use\_dtls |
| --- |

Flag to indicate if context should use DTLS.

Enabled via the use of coaps:// protocol prefix in connection information. NOTE: requires `CONFIG_LWM2M_DTLS_SUPPORT`

## [◆ ](#a574b50b9ec4cdfb5fac53a9b6d8c31d5)validate\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) lwm2m\_ctx::validate\_buf[CONFIG\_LWM2M\_ENGINE\_VALIDATION\_BUFFER\_SIZE] |
| --- |

Validation buffer.

Used as a temporary buffer to decode the resource value before validation. On successful validation, its content is copied into the actual resource buffer.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[lwm2m.h](lwm2m_8h_source.md)

- [lwm2m\_ctx](structlwm2m__ctx.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
