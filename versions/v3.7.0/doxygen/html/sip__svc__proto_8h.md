---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sip__svc__proto_8h.html
original_path: doxygen/html/sip__svc__proto_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sip\_svc\_proto.h File Reference

Arm SiP services communication protocol between service provider and client.
[More...](#details)

[Go to the source code of this file.](sip__svc__proto_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [sip\_svc\_request](structsip__svc__request.md) |
|  | SiP Service communication protocol request format. [More...](structsip__svc__request.md#details) |
| struct | [sip\_svc\_response](structsip__svc__response.md) |
|  | SiP Services service communication protocol response format. [More...](structsip__svc__response.md#details) |

| Macros | |
| --- | --- |
| #define | [SIP\_SVC\_ID\_INVALID](#ad1cb9509a40e51809b13f1fccf0f35ba)   0xFFFFFFFF |
|  | Invalid id value. |
| #define | [SIP\_SVC\_PROTO\_VER](#a5544d9131eef67538c3a36bdfec5482e)   0x0 |
|  | Header format. |
| #define | [SIP\_SVC\_PROTO\_HEADER\_CODE\_OFFSET](#a218d17af00117be8baf393e6b95cd9b2)   0 |
| #define | [SIP\_SVC\_PROTO\_HEADER\_CODE\_MASK](#aa8dbe689b3b375f72d049a89389ff591)   0xFFFF |
| #define | [SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_OFFSET](#a4f147d26b354026e01225395e3f074ce)   16 |
| #define | [SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_MASK](#a2da7d9fd032cf43814b535f7b9ff9028)   0xFF |
| #define | [SIP\_SVC\_PROTO\_HEADER\_VER\_OFFSET](#a10ce84feaee4a6454c36dc3daf4f7722)   30 |
| #define | [SIP\_SVC\_PROTO\_HEADER\_VER\_MASK](#a8ffae8b2e3adb78378308944fb38601e)   0x3 |
| #define | [SIP\_SVC\_PROTO\_HEADER](#a8ad11e26b133a65a94877930e74afa90)(code, trans\_id) |
| #define | [SIP\_SVC\_PROTO\_HEADER\_GET\_CODE](#a365877f6f62717cb3f271666fa392d8e)(header) |
| #define | [SIP\_SVC\_PROTO\_HEADER\_GET\_TRANS\_ID](#a4badc2fa72b4d5ae55c9b6503e3d2f41)(header) |
| #define | [SIP\_SVC\_PROTO\_HEADER\_SET\_TRANS\_ID](#a57124f787454b1253737bdde7ad04c6f)(header, trans\_id) |
| #define | [SIP\_SVC\_PROTO\_CMD\_SYNC](#a6ea30874bbe6393807ccc8c02038cc30)   0x0 |
|  | Arm SiP services command code in request header. |
| #define | [SIP\_SVC\_PROTO\_CMD\_ASYNC](#a8bc75a10006e42097f74edf990fa1f16)   0x1 |
| #define | [SIP\_SVC\_PROTO\_CMD\_MAX](#a8d7c4970ff149584080532c7bfa0cd51)   [SIP\_SVC\_PROTO\_CMD\_ASYNC](#a8bc75a10006e42097f74edf990fa1f16) |
| #define | [SIP\_SVC\_PROTO\_STATUS\_OK](#af4153e73a6024d7d4355e9373f10388b)   0x0 |
|  | Error code in response header. |
| #define | [SIP\_SVC\_PROTO\_STATUS\_UNKNOWN](#a1c7567c532ab25d3d21ed76c655b9680)   0xFFFF |
| #define | [SIP\_SVC\_PROTO\_STATUS\_BUSY](#aeae6b273da4e3e91f0a6ee2558a7585f)   0x1 |
| #define | [SIP\_SVC\_PROTO\_STATUS\_REJECT](#aa777087a721423e0e65cac4949813aaf)   0x2 |
| #define | [SIP\_SVC\_PROTO\_STATUS\_NO\_RESPONSE](#afba704d63c783fdd3d143045ca260706)   0x3 |
| #define | [SIP\_SVC\_PROTO\_STATUS\_ERROR](#a0d92a17202ff227476277500f539fd51)   0x4 |

## Detailed Description

Arm SiP services communication protocol between service provider and client.

Client to fill in the input data in struct [sip\_svc\_request](structsip__svc__request.md "SiP Service communication protocol request format.") format when requesting SMC/HVC service via 'send' function.

Service to fill in the SMC/HVC return value in struct [sip\_svc\_response](structsip__svc__response.md "SiP Services service communication protocol response format.") format and pass to client via Callback.

## Macro Definition Documentation

## [◆ ](#ad1cb9509a40e51809b13f1fccf0f35ba)SIP\_SVC\_ID\_INVALID

| #define SIP\_SVC\_ID\_INVALID   0xFFFFFFFF |
| --- |

Invalid id value.

## [◆ ](#a8bc75a10006e42097f74edf990fa1f16)SIP\_SVC\_PROTO\_CMD\_ASYNC

| #define SIP\_SVC\_PROTO\_CMD\_ASYNC   0x1 |
| --- |

## [◆ ](#a8d7c4970ff149584080532c7bfa0cd51)SIP\_SVC\_PROTO\_CMD\_MAX

| #define SIP\_SVC\_PROTO\_CMD\_MAX   [SIP\_SVC\_PROTO\_CMD\_ASYNC](#a8bc75a10006e42097f74edf990fa1f16) |
| --- |

## [◆ ](#a6ea30874bbe6393807ccc8c02038cc30)SIP\_SVC\_PROTO\_CMD\_SYNC

| #define SIP\_SVC\_PROTO\_CMD\_SYNC   0x0 |
| --- |

Arm SiP services command code in request header.

SIP\_SVC\_PROTO\_CMD\_SYNC

- Typical flow, synchronous request. Service expects EL3/EL2 firmware to return the result immediately during SMC/HVC call.

SIP\_SVC\_PROTO\_CMD\_ASYNC

- Asynchronous request. Service is required to poll the response via a separate SMC/HVC call. Use this method if the request requires longer processing in EL3/EL2.

## [◆ ](#a8ad11e26b133a65a94877930e74afa90)SIP\_SVC\_PROTO\_HEADER

| #define SIP\_SVC\_PROTO\_HEADER | ( |  | *code*, |
| --- | --- | --- | --- |
|  |  |  | *trans\_id* ) |

**Value:**

((((code)&[SIP\_SVC\_PROTO\_HEADER\_CODE\_MASK](#aa8dbe689b3b375f72d049a89389ff591)) << [SIP\_SVC\_PROTO\_HEADER\_CODE\_OFFSET](#a218d17af00117be8baf393e6b95cd9b2)) | \

(((trans\_id)&[SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_MASK](#a2da7d9fd032cf43814b535f7b9ff9028)) \

<< [SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_OFFSET](#a4f147d26b354026e01225395e3f074ce)) | \

(([SIP\_SVC\_PROTO\_VER](#a5544d9131eef67538c3a36bdfec5482e) & [SIP\_SVC\_PROTO\_HEADER\_VER\_MASK](#a8ffae8b2e3adb78378308944fb38601e)) << [SIP\_SVC\_PROTO\_HEADER\_VER\_OFFSET](#a10ce84feaee4a6454c36dc3daf4f7722)))

[SIP\_SVC\_PROTO\_HEADER\_VER\_OFFSET](#a10ce84feaee4a6454c36dc3daf4f7722)

#define SIP\_SVC\_PROTO\_HEADER\_VER\_OFFSET

**Definition** sip\_svc\_proto.h:38

[SIP\_SVC\_PROTO\_HEADER\_CODE\_OFFSET](#a218d17af00117be8baf393e6b95cd9b2)

#define SIP\_SVC\_PROTO\_HEADER\_CODE\_OFFSET

**Definition** sip\_svc\_proto.h:32

[SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_MASK](#a2da7d9fd032cf43814b535f7b9ff9028)

#define SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_MASK

**Definition** sip\_svc\_proto.h:36

[SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_OFFSET](#a4f147d26b354026e01225395e3f074ce)

#define SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_OFFSET

**Definition** sip\_svc\_proto.h:35

[SIP\_SVC\_PROTO\_VER](#a5544d9131eef67538c3a36bdfec5482e)

#define SIP\_SVC\_PROTO\_VER

Header format.

**Definition** sip\_svc\_proto.h:30

[SIP\_SVC\_PROTO\_HEADER\_VER\_MASK](#a8ffae8b2e3adb78378308944fb38601e)

#define SIP\_SVC\_PROTO\_HEADER\_VER\_MASK

**Definition** sip\_svc\_proto.h:39

[SIP\_SVC\_PROTO\_HEADER\_CODE\_MASK](#aa8dbe689b3b375f72d049a89389ff591)

#define SIP\_SVC\_PROTO\_HEADER\_CODE\_MASK

**Definition** sip\_svc\_proto.h:33

## [◆ ](#aa8dbe689b3b375f72d049a89389ff591)SIP\_SVC\_PROTO\_HEADER\_CODE\_MASK

| #define SIP\_SVC\_PROTO\_HEADER\_CODE\_MASK   0xFFFF |
| --- |

## [◆ ](#a218d17af00117be8baf393e6b95cd9b2)SIP\_SVC\_PROTO\_HEADER\_CODE\_OFFSET

| #define SIP\_SVC\_PROTO\_HEADER\_CODE\_OFFSET   0 |
| --- |

## [◆ ](#a365877f6f62717cb3f271666fa392d8e)SIP\_SVC\_PROTO\_HEADER\_GET\_CODE

| #define SIP\_SVC\_PROTO\_HEADER\_GET\_CODE | ( |  | *header* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((header) >> [SIP\_SVC\_PROTO\_HEADER\_CODE\_OFFSET](#a218d17af00117be8baf393e6b95cd9b2)) & [SIP\_SVC\_PROTO\_HEADER\_CODE\_MASK](#aa8dbe689b3b375f72d049a89389ff591))

## [◆ ](#a4badc2fa72b4d5ae55c9b6503e3d2f41)SIP\_SVC\_PROTO\_HEADER\_GET\_TRANS\_ID

| #define SIP\_SVC\_PROTO\_HEADER\_GET\_TRANS\_ID | ( |  | *header* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((header) >> [SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_OFFSET](#a4f147d26b354026e01225395e3f074ce)) & [SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_MASK](#a2da7d9fd032cf43814b535f7b9ff9028))

## [◆ ](#a57124f787454b1253737bdde7ad04c6f)SIP\_SVC\_PROTO\_HEADER\_SET\_TRANS\_ID

| #define SIP\_SVC\_PROTO\_HEADER\_SET\_TRANS\_ID | ( |  | *header*, |
| --- | --- | --- | --- |
|  |  |  | *trans\_id* ) |

**Value:**

(header) &= ~([SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_MASK](#a2da7d9fd032cf43814b535f7b9ff9028) << [SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_OFFSET](#a4f147d26b354026e01225395e3f074ce)); \

(header) |= (((trans\_id)&[SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_MASK](#a2da7d9fd032cf43814b535f7b9ff9028)) \

<< [SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_OFFSET](#a4f147d26b354026e01225395e3f074ce));

## [◆ ](#a2da7d9fd032cf43814b535f7b9ff9028)SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_MASK

| #define SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_MASK   0xFF |
| --- |

## [◆ ](#a4f147d26b354026e01225395e3f074ce)SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_OFFSET

| #define SIP\_SVC\_PROTO\_HEADER\_TRANS\_ID\_OFFSET   16 |
| --- |

## [◆ ](#a8ffae8b2e3adb78378308944fb38601e)SIP\_SVC\_PROTO\_HEADER\_VER\_MASK

| #define SIP\_SVC\_PROTO\_HEADER\_VER\_MASK   0x3 |
| --- |

## [◆ ](#a10ce84feaee4a6454c36dc3daf4f7722)SIP\_SVC\_PROTO\_HEADER\_VER\_OFFSET

| #define SIP\_SVC\_PROTO\_HEADER\_VER\_OFFSET   30 |
| --- |

## [◆ ](#aeae6b273da4e3e91f0a6ee2558a7585f)SIP\_SVC\_PROTO\_STATUS\_BUSY

| #define SIP\_SVC\_PROTO\_STATUS\_BUSY   0x1 |
| --- |

## [◆ ](#a0d92a17202ff227476277500f539fd51)SIP\_SVC\_PROTO\_STATUS\_ERROR

| #define SIP\_SVC\_PROTO\_STATUS\_ERROR   0x4 |
| --- |

## [◆ ](#afba704d63c783fdd3d143045ca260706)SIP\_SVC\_PROTO\_STATUS\_NO\_RESPONSE

| #define SIP\_SVC\_PROTO\_STATUS\_NO\_RESPONSE   0x3 |
| --- |

## [◆ ](#af4153e73a6024d7d4355e9373f10388b)SIP\_SVC\_PROTO\_STATUS\_OK

| #define SIP\_SVC\_PROTO\_STATUS\_OK   0x0 |
| --- |

Error code in response header.

SIP\_SVC\_PROTO\_STATUS\_OK

- Successfully execute the request.

SIP\_SVC\_PROTO\_STATUS\_UNKNOWN

- Unrecognized SMC/HVC Function ID.

SIP\_SVC\_PROTO\_STATUS\_BUSY

- The request is still in progress. Please try again.

SIP\_SVC\_PROTO\_STATUS\_REJECT

- The request have been rejected due to improper input data.

SIP\_SVC\_PROTO\_STATUS\_NO\_RESPONSE

- No response from target hardware yet.

SIP\_SVC\_PROTO\_STATUS\_ERROR

- Error occurred when executing the request.

SIP\_SVC\_PROTO\_STATUS\_NOT\_SUPPORT

- Unsupported Arm SiP services command code

## [◆ ](#aa777087a721423e0e65cac4949813aaf)SIP\_SVC\_PROTO\_STATUS\_REJECT

| #define SIP\_SVC\_PROTO\_STATUS\_REJECT   0x2 |
| --- |

## [◆ ](#a1c7567c532ab25d3d21ed76c655b9680)SIP\_SVC\_PROTO\_STATUS\_UNKNOWN

| #define SIP\_SVC\_PROTO\_STATUS\_UNKNOWN   0xFFFF |
| --- |

## [◆ ](#a5544d9131eef67538c3a36bdfec5482e)SIP\_SVC\_PROTO\_VER

| #define SIP\_SVC\_PROTO\_VER   0x0 |
| --- |

Header format.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sip\_svc](dir_be59f4c2e7724c8d2ef47362c82e9052.md)
- [sip\_svc\_proto.h](sip__svc__proto_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
