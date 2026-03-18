---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__model__pub.html
original_path: doxygen/html/structbt__mesh__model__pub.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_model\_pub Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Access layer](group__bt__mesh__access.md)

Model publication context.
[More...](#details)

`#include <[access.h](access_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [mod](#aa5026299082b3013740c7e36c01f91f5) |
|  | The model the context belongs to. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [addr](#a408c9185168b962f7e7314f9a429fe8c) |
|  | Publish Address. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [uuid](#abea9c2085c9d2e1e2fc71f03dd323ee7) |
|  | Label UUID if Publish Address is Virtual Address. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [key](#a0ad1809fe74930c9b36b32516a8d146f):12 |
|  | Publish AppKey Index. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [cred](#a3617adb0c1192419bdac2ad0f37199ac):1 |
|  | Friendship Credentials Flag. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [send\_rel](#ab704aedcfd06d374615ef18c6ecc84a9):1 |
|  | Force reliable sending (segment acks). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [fast\_period](#abdbdc3bbc5d4ac5a5d606b55bb2d50ee):1 |
|  | Use FastPeriodDivisor. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [retr\_update](#a16c13e46c012ab836acd02b8fe5f05e3):1 |
|  | Call update callback on every retransmission. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [ttl](#a820b713aaa1e0c33a4a59c80f805e854) |
|  | Publish Time to Live. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [retransmit](#a3d93d44ff85243dc94e7b4d36cde5b97) |
|  | Retransmit Count & Interval Steps. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [period](#ae550510e9ca45f8c9fd9802e4e7e0f3d) |
|  | Publish Period. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [period\_div](#a4f2ce8727ffb44f564d1dc0615ebcadf):4 |
|  | Divisor for the Period. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [count](#a4e211c851bf91a9b43f035d435e9c93c):4 |
|  | Transmissions left. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [delayable](#a23a865dbd2dce5c1af074097864611e9):1 |
|  | Use random delay for publishing. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [period\_start](#ab6e00714ea899eb32873d10b0908d278) |
|  | Start of the current period. |
| struct [net\_buf\_simple](structnet__buf__simple.md) \* | [msg](#a5f5639c01d3704ec3d527c418d35f827) |
|  | Publication buffer, containing the publication message. |
| int(\* | [update](#a0354344e08e633dc4d6c0b4e7b169080) )(const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[mod](#aa5026299082b3013740c7e36c01f91f5)) |
|  | Callback for updating the publication buffer. |
| struct [k\_work\_delayable](structk__work__delayable.md) | [timer](#af3771432d13805710e94f013332e8214) |
|  | Publish Period Timer. |

## Detailed Description

Model publication context.

The context should primarily be created using the BT\_MESH\_MODEL\_PUB\_DEFINE macro.

## Field Documentation

## [◆ ](#a408c9185168b962f7e7314f9a429fe8c)addr

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_model\_pub::addr |
| --- |

Publish Address.

## [◆ ](#a4e211c851bf91a9b43f035d435e9c93c)count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_model\_pub::count |
| --- |

Transmissions left.

## [◆ ](#a3617adb0c1192419bdac2ad0f37199ac)cred

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_model\_pub::cred |
| --- |

Friendship Credentials Flag.

## [◆ ](#a23a865dbd2dce5c1af074097864611e9)delayable

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_model\_pub::delayable |
| --- |

Use random delay for publishing.

## [◆ ](#abdbdc3bbc5d4ac5a5d606b55bb2d50ee)fast\_period

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_model\_pub::fast\_period |
| --- |

Use FastPeriodDivisor.

## [◆ ](#a0ad1809fe74930c9b36b32516a8d146f)key

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_model\_pub::key |
| --- |

Publish AppKey Index.

## [◆ ](#aa5026299082b3013740c7e36c01f91f5)mod

| const struct [bt\_mesh\_model](structbt__mesh__model.md)\* bt\_mesh\_model\_pub::mod |
| --- |

The model the context belongs to.

Initialized by the stack.

## [◆ ](#a5f5639c01d3704ec3d527c418d35f827)msg

| struct [net\_buf\_simple](structnet__buf__simple.md)\* bt\_mesh\_model\_pub::msg |
| --- |

Publication buffer, containing the publication message.

This will get correctly created when the publication context has been defined using the BT\_MESH\_MODEL\_PUB\_DEFINE macro.

```
BT_MESH_MODEL_PUB_DEFINE(name, update, size);
```

## [◆ ](#ae550510e9ca45f8c9fd9802e4e7e0f3d)period

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_model\_pub::period |
| --- |

Publish Period.

## [◆ ](#a4f2ce8727ffb44f564d1dc0615ebcadf)period\_div

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_model\_pub::period\_div |
| --- |

Divisor for the Period.

## [◆ ](#ab6e00714ea899eb32873d10b0908d278)period\_start

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_model\_pub::period\_start |
| --- |

Start of the current period.

## [◆ ](#a16c13e46c012ab836acd02b8fe5f05e3)retr\_update

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_model\_pub::retr\_update |
| --- |

Call update callback on every retransmission.

## [◆ ](#a3d93d44ff85243dc94e7b4d36cde5b97)retransmit

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_model\_pub::retransmit |
| --- |

Retransmit Count & Interval Steps.

## [◆ ](#ab704aedcfd06d374615ef18c6ecc84a9)send\_rel

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_model\_pub::send\_rel |
| --- |

Force reliable sending (segment acks).

## [◆ ](#af3771432d13805710e94f013332e8214)timer

| struct [k\_work\_delayable](structk__work__delayable.md) bt\_mesh\_model\_pub::timer |
| --- |

Publish Period Timer.

Only for stack-internal use.

## [◆ ](#a820b713aaa1e0c33a4a59c80f805e854)ttl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_model\_pub::ttl |
| --- |

Publish Time to Live.

## [◆ ](#a0354344e08e633dc4d6c0b4e7b169080)update

| int(\* bt\_mesh\_model\_pub::update) (const struct [bt\_mesh\_model](structbt__mesh__model.md) \*[mod](#aa5026299082b3013740c7e36c01f91f5)) |
| --- |

Callback for updating the publication buffer.

When set to NULL, the model is assumed not to support periodic publishing. When set to non-NULL the callback will be called periodically and is expected to update [bt\_mesh\_model\_pub::msg](#a5f5639c01d3704ec3d527c418d35f827) with a valid publication message.

If the callback returns non-zero, the publication is skipped and will resume on the next periodic publishing interval.

When [bt\_mesh\_model\_pub::retr\_update](#a16c13e46c012ab836acd02b8fe5f05e3) is set to 1, the callback will be called on every retransmission.

Parameters
:   | [mod](#aa5026299082b3013740c7e36c01f91f5) | The Model the Publication Context belongs to. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#abea9c2085c9d2e1e2fc71f03dd323ee7)uuid

| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* bt\_mesh\_model\_pub::uuid |
| --- |

Label UUID if Publish Address is Virtual Address.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[access.h](access_8h_source.md)

- [bt\_mesh\_model\_pub](structbt__mesh__model__pub.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
