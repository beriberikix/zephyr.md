---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__gatt__client.html
original_path: doxygen/html/group__bt__gatt__client.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

GATT Client APIs

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_gatt\_exchange\_params](structbt__gatt__exchange__params.md) |
|  | GATT Exchange MTU parameters. [More...](structbt__gatt__exchange__params.md#details) |
| struct | [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) |
|  | GATT Discover Attributes parameters. [More...](structbt__gatt__discover__params.md#details) |
| struct | [bt\_gatt\_read\_params](structbt__gatt__read__params.md) |
|  | GATT Read parameters. [More...](structbt__gatt__read__params.md#details) |
| struct | [bt\_gatt\_write\_params](structbt__gatt__write__params.md) |
|  | GATT Write parameters. [More...](structbt__gatt__write__params.md#details) |
| struct | [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) |
|  | GATT Subscribe parameters. [More...](structbt__gatt__subscribe__params.md#details) |

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [bt\_gatt\_discover\_func\_t](#gabd3bcd3c1560956726574faed332fb13)) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) \*params) |
|  | Discover attribute callback function. |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [bt\_gatt\_read\_func\_t](#ga1ca94b4f2b6c456b6134e05127993569)) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err, struct [bt\_gatt\_read\_params](structbt__gatt__read__params.md) \*params, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length) |
|  | Read callback function. |
| typedef void(\* | [bt\_gatt\_write\_func\_t](#ga2bca8c4a45f41e0400a9e0147f4baf50)) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err, struct [bt\_gatt\_write\_params](structbt__gatt__write__params.md) \*params) |
|  | Write callback function. |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [bt\_gatt\_notify\_func\_t](#gab3e53eb5f9bb1eda7bf612ef95755b4d)) (struct bt\_conn \*conn, struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length) |
|  | Notification callback function. |
| typedef void(\* | [bt\_gatt\_subscribe\_func\_t](#ga2e914e63b4b91fa56bc3295283c43714)) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err, struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params) |
|  | Subscription callback function. |

| Enumerations | |
| --- | --- |
| enum | {     [BT\_GATT\_DISCOVER\_PRIMARY](#ggaa7bf94a9823d44c702cc26dc8ade8403ada9ac33aa77f6043da8133dcf269478f) , [BT\_GATT\_DISCOVER\_SECONDARY](#ggaa7bf94a9823d44c702cc26dc8ade8403a21be62548b816c7960a54dd6e3b37a97) , [BT\_GATT\_DISCOVER\_INCLUDE](#ggaa7bf94a9823d44c702cc26dc8ade8403a80afff1c83bb5ebb5603af699f2c26da) , [BT\_GATT\_DISCOVER\_CHARACTERISTIC](#ggaa7bf94a9823d44c702cc26dc8ade8403a71355dfe0bf30c88f9fe2f7da1ba10ae) ,     [BT\_GATT\_DISCOVER\_DESCRIPTOR](#ggaa7bf94a9823d44c702cc26dc8ade8403a0ccb2587aa8f21361c5d73847a33ecbe) , [BT\_GATT\_DISCOVER\_ATTRIBUTE](#ggaa7bf94a9823d44c702cc26dc8ade8403afe2167b873b848935d56f6ee7f2c444c) , [BT\_GATT\_DISCOVER\_STD\_CHAR\_DESC](#ggaa7bf94a9823d44c702cc26dc8ade8403a81a1f8737c415544a0f793f4e626bb61)   } |
|  | GATT Discover types. [More...](#gaa7bf94a9823d44c702cc26dc8ade8403) |
| enum | {     [BT\_GATT\_SUBSCRIBE\_FLAG\_VOLATILE](#gga07d7c3837ad936e586fdb11c0bd122d6aecdcb3baa850505f459523091c92a1cb) , [BT\_GATT\_SUBSCRIBE\_FLAG\_NO\_RESUB](#gga07d7c3837ad936e586fdb11c0bd122d6a30bfd3fb4bf4f17653ba00942ba2b2e6) , [BT\_GATT\_SUBSCRIBE\_FLAG\_WRITE\_PENDING](#gga07d7c3837ad936e586fdb11c0bd122d6afe1c3dc9380c33debd32a275d5bce8ad) , [BT\_GATT\_SUBSCRIBE\_FLAG\_SENT](#gga07d7c3837ad936e586fdb11c0bd122d6a56aa5f332d4098e3942d7a902198f7ab) ,     [BT\_GATT\_SUBSCRIBE\_NUM\_FLAGS](#gga07d7c3837ad936e586fdb11c0bd122d6a5640a1e06740a89859c5f4b183d58e79)   } |
|  | Subscription flags. [More...](#ga07d7c3837ad936e586fdb11c0bd122d6) |

| Functions | |
| --- | --- |
| int | [bt\_gatt\_exchange\_mtu](#ga0f41da23c6559a8254b04295aff8198d) (struct bt\_conn \*conn, struct [bt\_gatt\_exchange\_params](structbt__gatt__exchange__params.md) \*params) |
|  | Exchange MTU. |
| int | [bt\_gatt\_discover](#gac06a945e5f7939b6716bc4f2cea781bd) (struct bt\_conn \*conn, struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) \*params) |
|  | GATT Discover function. |
| int | [bt\_gatt\_read](#ga1a18dd726ab960a88d7f85f2a014141a) (struct bt\_conn \*conn, struct [bt\_gatt\_read\_params](structbt__gatt__read__params.md) \*params) |
|  | Read Attribute Value by handle. |
| int | [bt\_gatt\_write](#ga843a42e68e0497d88d3f655f8ffd58d4) (struct bt\_conn \*conn, struct [bt\_gatt\_write\_params](structbt__gatt__write__params.md) \*params) |
|  | Write Attribute Value by handle. |
| int | [bt\_gatt\_write\_without\_response\_cb](#ga49439413d12b5a8a1c68735e961ab6fa) (struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) handle, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sign, [bt\_gatt\_complete\_func\_t](group__bt__gatt__server.md#gac55832607b95f394d26a64ed1cfe5bba) func, void \*user\_data) |
|  | Write Attribute Value by handle without response with callback. |
| static int | [bt\_gatt\_write\_without\_response](#ga9fc78e32230637a6f092da2400c50fe7) (struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) handle, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sign) |
|  | Write Attribute Value by handle without response. |
| int | [bt\_gatt\_subscribe](#ga7d4a8e18f51ba6476886a15f81f48e5c) (struct bt\_conn \*conn, struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params) |
|  | Subscribe Attribute Value Notification. |
| int | [bt\_gatt\_resubscribe](#ga791b8bb8a4c085b022fafc0535a63511) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*peer, struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params) |
|  | Resubscribe Attribute Value Notification subscription. |
| int | [bt\_gatt\_unsubscribe](#ga56509c9b8f73f729cfa5e75be22d79ae) (struct bt\_conn \*conn, struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params) |
|  | Unsubscribe Attribute Value Notification. |
| void | [bt\_gatt\_cancel](#ga5193dea59a016692f94cf950d6b4f4f7) (struct bt\_conn \*conn, void \*params) |
|  | Try to cancel the first pending request identified by `params`. |

## Detailed Description

## Typedef Documentation

## [◆ ](#gabd3bcd3c1560956726574faed332fb13)bt\_gatt\_discover\_func\_t

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* bt\_gatt\_discover\_func\_t) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) \*params) |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Discover attribute callback function.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | attr | Attribute found, or NULL if not found. |
    | params | Discovery parameters given. |

If discovery procedure has completed this callback will be called with attr set to NULL. This will not happen if procedure was stopped by returning BT\_GATT\_ITER\_STOP.

The attribute object as well as its UUID and value objects are temporary and must be copied to in order to cache its information. Only the following fields of the attribute contains valid information:

- uuid UUID representing the type of attribute.
- handle Handle in the remote database.
- user\_data The value of the attribute, if the discovery type maps to an ATT operation that provides this information. NULL otherwise. See below.

The effective type of `attr->user_data` is determined by `params`. Note that the fields `params->type` and `params->uuid` are left unchanged by the discovery procedure.

| `params->type` | `params->uuid` | Type of `attr->user_data` |
| --- | --- | --- |
| [BT\_GATT\_DISCOVER\_PRIMARY](#ggaa7bf94a9823d44c702cc26dc8ade8403ada9ac33aa77f6043da8133dcf269478f) | any | [bt\_gatt\_service\_val](structbt__gatt__service__val.md "bt_gatt_service_val") |
| [BT\_GATT\_DISCOVER\_SECONDARY](#ggaa7bf94a9823d44c702cc26dc8ade8403a21be62548b816c7960a54dd6e3b37a97) | any | [bt\_gatt\_service\_val](structbt__gatt__service__val.md "bt_gatt_service_val") |
| [BT\_GATT\_DISCOVER\_INCLUDE](#ggaa7bf94a9823d44c702cc26dc8ade8403a80afff1c83bb5ebb5603af699f2c26da) | any | [bt\_gatt\_include](structbt__gatt__include.md "bt_gatt_include") |
| [BT\_GATT\_DISCOVER\_CHARACTERISTIC](#ggaa7bf94a9823d44c702cc26dc8ade8403a71355dfe0bf30c88f9fe2f7da1ba10ae) | any | [bt\_gatt\_chrc](structbt__gatt__chrc.md "bt_gatt_chrc") |
| [BT\_GATT\_DISCOVER\_STD\_CHAR\_DESC](#ggaa7bf94a9823d44c702cc26dc8ade8403a81a1f8737c415544a0f793f4e626bb61) | [BT\_UUID\_GATT\_CEP](group__bt__uuid.md#ga6aa143b721d810f1536d7431a9bf7cc7 "BT_UUID_GATT_CEP") | [bt\_gatt\_cep](structbt__gatt__cep.md "bt_gatt_cep") |
| [BT\_GATT\_DISCOVER\_STD\_CHAR\_DESC](#ggaa7bf94a9823d44c702cc26dc8ade8403a81a1f8737c415544a0f793f4e626bb61) | [BT\_UUID\_GATT\_CCC](group__bt__uuid.md#ga03a2d3f0ce89508b794d5c87a4303057 "BT_UUID_GATT_CCC") | [bt\_gatt\_ccc](structbt__gatt__ccc.md "bt_gatt_ccc") |
| [BT\_GATT\_DISCOVER\_STD\_CHAR\_DESC](#ggaa7bf94a9823d44c702cc26dc8ade8403a81a1f8737c415544a0f793f4e626bb61) | [BT\_UUID\_GATT\_SCC](group__bt__uuid.md#ga82567cdce8c4411cd3daf26711ba9685 "BT_UUID_GATT_SCC") | [bt\_gatt\_scc](structbt__gatt__scc.md "bt_gatt_scc") |
| [BT\_GATT\_DISCOVER\_STD\_CHAR\_DESC](#ggaa7bf94a9823d44c702cc26dc8ade8403a81a1f8737c415544a0f793f4e626bb61) | [BT\_UUID\_GATT\_CPF](group__bt__uuid.md#ga331a61702ffe9b15bac0de3d60414022 "BT_UUID_GATT_CPF") | [bt\_gatt\_cpf](structbt__gatt__cpf.md "bt_gatt_cpf") |
| [BT\_GATT\_DISCOVER\_DESCRIPTOR](#ggaa7bf94a9823d44c702cc26dc8ade8403a0ccb2587aa8f21361c5d73847a33ecbe) | any | NULL |
| [BT\_GATT\_DISCOVER\_ATTRIBUTE](#ggaa7bf94a9823d44c702cc26dc8ade8403afe2167b873b848935d56f6ee7f2c444c) | any | NULL |

Also consider if using read-by-type instead of discovery is more convenient. See [bt\_gatt\_read](#ga1a18dd726ab960a88d7f85f2a014141a) with [bt\_gatt\_read\_params::handle\_count](structbt__gatt__read__params.md#a0a36063ac0b110fbf57ef6a66f7bece8 "bt_gatt_read_params::handle_count") set to `0`.

Returns
:   BT\_GATT\_ITER\_CONTINUE to continue discovery procedure.
:   BT\_GATT\_ITER\_STOP to stop discovery procedure.

## [◆ ](#gab3e53eb5f9bb1eda7bf612ef95755b4d)bt\_gatt\_notify\_func\_t

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* bt\_gatt\_notify\_func\_t) (struct bt\_conn \*conn, struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length) |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Notification callback function.

In the case of an empty notification, the `data` pointer will be non-NULL while the `length` will be 0, which is due to the special case where a `data` NULL pointer means unsubscribed.

Parameters
:   | conn | Connection object. May be NULL, indicating that the peer is being unpaired |
    | --- | --- |
    | params | Subscription parameters. |
    | data | Attribute value data. If NULL then subscription was removed. |
    | length | Attribute value length. |

Returns
:   BT\_GATT\_ITER\_CONTINUE to continue receiving value notifications. BT\_GATT\_ITER\_STOP to unsubscribe from value notifications.

## [◆ ](#ga1ca94b4f2b6c456b6134e05127993569)bt\_gatt\_read\_func\_t

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* bt\_gatt\_read\_func\_t) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err, struct [bt\_gatt\_read\_params](structbt__gatt__read__params.md) \*params, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length) |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Read callback function.

When reading using by\_uuid, params->start\_handle is the attribute handle for this data item.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | err | ATT error code. |
    | params | Read parameters used. |
    | data | Attribute value data. NULL means read has completed. |
    | length | Attribute value length. |

Returns
:   BT\_GATT\_ITER\_CONTINUE if should continue to the next attribute.
:   BT\_GATT\_ITER\_STOP to stop.

## [◆ ](#ga2e914e63b4b91fa56bc3295283c43714)bt\_gatt\_subscribe\_func\_t

| typedef void(\* bt\_gatt\_subscribe\_func\_t) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err, struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params) |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Subscription callback function.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | err | ATT error code. |
    | params | Subscription parameters used. |

## [◆ ](#ga2bca8c4a45f41e0400a9e0147f4baf50)bt\_gatt\_write\_func\_t

| typedef void(\* bt\_gatt\_write\_func\_t) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err, struct [bt\_gatt\_write\_params](structbt__gatt__write__params.md) \*params) |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Write callback function.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | err | ATT error code. |
    | params | Write parameters used. |

## Enumeration Type Documentation

## [◆ ](#gaa7bf94a9823d44c702cc26dc8ade8403)anonymous enum

| anonymous enum |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

GATT Discover types.

| Enumerator | |
| --- | --- |
| BT\_GATT\_DISCOVER\_PRIMARY | Discover Primary Services. |
| BT\_GATT\_DISCOVER\_SECONDARY | Discover Secondary Services. |
| BT\_GATT\_DISCOVER\_INCLUDE | Discover Included Services. |
| BT\_GATT\_DISCOVER\_CHARACTERISTIC | Discover Characteristic Values.  Discover Characteristic Value and its properties. |
| BT\_GATT\_DISCOVER\_DESCRIPTOR | Discover Descriptors.  Discover Attributes which are not services or characteristics.  Note  The use of this type of discover is not recommended for discovering in ranges across multiple services/characteristics as it may incur in extra round trips. |
| BT\_GATT\_DISCOVER\_ATTRIBUTE | Discover Attributes.  Discover Attributes of any type.  Note  The use of this type of discover is not recommended for discovering in ranges across multiple services/characteristics as it may incur in more round trips. |
| BT\_GATT\_DISCOVER\_STD\_CHAR\_DESC | Discover standard characteristic descriptor values.  Discover standard characteristic descriptor values and their properties. Supported descriptors:   - Characteristic Extended Properties - Client Characteristic Configuration - Server Characteristic Configuration - Characteristic Presentation Format |

## [◆ ](#ga07d7c3837ad936e586fdb11c0bd122d6)anonymous enum

| anonymous enum |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Subscription flags.

| Enumerator | |
| --- | --- |
| BT\_GATT\_SUBSCRIBE\_FLAG\_VOLATILE | Persistence flag.  If set, indicates that the subscription is not saved on the GATT server side. Therefore, upon disconnection, the subscription will be automatically removed from the client's subscriptions list and when the client reconnects, it will have to issue a new subscription. |
| BT\_GATT\_SUBSCRIBE\_FLAG\_NO\_RESUB | No resubscribe flag.  By default when BT\_GATT\_SUBSCRIBE\_FLAG\_VOLATILE is unset, the subscription will be automatically renewed when the client reconnects, as a workaround for GATT servers that do not persist subscriptions.  This flag will disable the automatic resubscription. It is useful if the application layer knows that the GATT server remembers subscriptions from previous connections and wants to avoid renewing the subscriptions. |
| BT\_GATT\_SUBSCRIBE\_FLAG\_WRITE\_PENDING | Write pending flag.  If set, indicates write operation is pending waiting remote end to respond.  Note  Internal use only. |
| BT\_GATT\_SUBSCRIBE\_FLAG\_SENT | Sent flag.  If set, indicates that a subscription request (CCC write) has already been sent in the active connection.  Used to avoid sending subscription requests multiple times when the `CONFIG_BT_GATT_AUTO_RESUBSCRIBE` quirk is enabled.  Note  Internal use only. |
| BT\_GATT\_SUBSCRIBE\_NUM\_FLAGS |  |

## Function Documentation

## [◆ ](#ga5193dea59a016692f94cf950d6b4f4f7)bt\_gatt\_cancel()

| void bt\_gatt\_cancel | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | void \* | *params* ) |

`#include <[gatt.h](gatt_8h.md)>`

Try to cancel the first pending request identified by `params`.

This function does not release `params` for reuse. The usual callbacks for the request still apply. A successful cancel simulates a [BT\_ATT\_ERR\_UNLIKELY](group__bt__att.md#ga992baa1f0d763a00f314bdcf59965bdd "The attribute request that was requested has encountered an error that was unlikely.") response from the server.

This function can cancel the following request functions:

- [bt\_gatt\_exchange\_mtu](#ga0f41da23c6559a8254b04295aff8198d)
- [bt\_gatt\_discover](#gac06a945e5f7939b6716bc4f2cea781bd)
- [bt\_gatt\_read](#ga1a18dd726ab960a88d7f85f2a014141a)
- [bt\_gatt\_write](#ga843a42e68e0497d88d3f655f8ffd58d4)
- [bt\_gatt\_subscribe](#ga7d4a8e18f51ba6476886a15f81f48e5c)
- [bt\_gatt\_unsubscribe](#ga56509c9b8f73f729cfa5e75be22d79ae)

Parameters
:   | conn | The connection the request was issued on. |
    | --- | --- |
    | params | The address params used in the request function call. |

## [◆ ](#gac06a945e5f7939b6716bc4f2cea781bd)bt\_gatt\_discover()

| int bt\_gatt\_discover | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) \* | *params* ) |

`#include <[gatt.h](gatt_8h.md)>`

GATT Discover function.

This procedure is used by a client to discover attributes on a server.

Primary Service Discovery: Procedure allows to discover primary services either by Discover All Primary Services or Discover Primary Services by Service UUID. Include Service Discovery: Procedure allows to discover all Include Services within specified range. Characteristic Discovery: Procedure allows to discover all characteristics within specified handle range as well as discover characteristics with specified UUID. Descriptors Discovery: Procedure allows to discover all characteristic descriptors within specified range.

For each attribute found the callback is called which can then decide whether to continue discovering or stop.

The Response comes in callback `params->func`. The callback is run from the BT RX thread. `params` must remain valid until start of callback where iter attr is NULL or callback will return [BT\_GATT\_ITER\_STOP](group__bt__gatt__server.md#ggab94ce0108483b70392b31a621aa0712aaa3f2a25e27c7065a2c7bb2a9ff09542e).

This function will block while the ATT request queue is full, except when called from the BT RX thread, as this would cause a deadlock.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | params | Discover parameters. |

Return values
:   | 0 | Successfully queued request. Will call `params->func` on resolution. |
    | --- | --- |
    | -ENOMEM | ATT request queue is full and blocking would cause deadlock. Allow a pending request to resolve before retrying, or call this function outside the BT RX thread to get blocking behavior. Queue size is controlled by `CONFIG_BT_ATT_TX_COUNT` . |

## [◆ ](#ga0f41da23c6559a8254b04295aff8198d)bt\_gatt\_exchange\_mtu()

| int bt\_gatt\_exchange\_mtu | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_gatt\_exchange\_params](structbt__gatt__exchange__params.md) \* | *params* ) |

`#include <[gatt.h](gatt_8h.md)>`

Exchange MTU.

This client procedure can be used to set the MTU to the maximum possible size the buffers can hold.

Note
:   Shall only be used once per connection.

The Response comes in callback `params->func`. The callback is run from the context specified by 'config BT\_RECV\_CONTEXT'. `params` must remain valid until start of callback.

This function will block while the ATT request queue is full, except when called from the BT RX thread, as this would cause a deadlock.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | params | Exchange MTU parameters. |

Return values
:   | 0 | Successfully queued request. Will call `params->func` on resolution. |
    | --- | --- |
    | -ENOMEM | ATT request queue is full and blocking would cause deadlock. Allow a pending request to resolve before retrying, or call this function outside the BT RX thread to get blocking behavior. Queue size is controlled by `CONFIG_BT_ATT_TX_COUNT` . |
    | -EALREADY | The MTU exchange procedure has been already performed. |

## [◆ ](#ga1a18dd726ab960a88d7f85f2a014141a)bt\_gatt\_read()

| int bt\_gatt\_read | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_gatt\_read\_params](structbt__gatt__read__params.md) \* | *params* ) |

`#include <[gatt.h](gatt_8h.md)>`

Read Attribute Value by handle.

This procedure read the attribute value and return it to the callback.

When reading attributes by UUID the callback can be called multiple times depending on how many instances of given the UUID exists with the start\_handle being updated for each instance.

To perform a GATT Long Read procedure, start with a Characteristic Value Read (by setting `offset` `0` and `handle_count` `1`) and then return [BT\_GATT\_ITER\_CONTINUE](group__bt__gatt__server.md#ggab94ce0108483b70392b31a621aa0712aaea569feffa4815d3443e12be78c684f5 "BT_GATT_ITER_CONTINUE") from the callback. This is equivalent to calling [bt\_gatt\_read](#ga1a18dd726ab960a88d7f85f2a014141a) again, but with the correct offset to continue the read. This may be repeated until the procedure is complete, which is signaled by the callback being called with `data` set to `NULL`.

Note that returning [BT\_GATT\_ITER\_CONTINUE](group__bt__gatt__server.md#ggab94ce0108483b70392b31a621aa0712aaea569feffa4815d3443e12be78c684f5 "BT_GATT_ITER_CONTINUE") is really starting a new ATT operation, so this can fail to allocate resources. However, all API errors are reported as if the server returned [BT\_ATT\_ERR\_UNLIKELY](group__bt__att.md#ga992baa1f0d763a00f314bdcf59965bdd "BT_ATT_ERR_UNLIKELY"). There is no way to distinguish between this condition and a [BT\_ATT\_ERR\_UNLIKELY](group__bt__att.md#ga992baa1f0d763a00f314bdcf59965bdd "BT_ATT_ERR_UNLIKELY") response from the server itself.

Note that the effect of returning [BT\_GATT\_ITER\_CONTINUE](group__bt__gatt__server.md#ggab94ce0108483b70392b31a621aa0712aaea569feffa4815d3443e12be78c684f5 "BT_GATT_ITER_CONTINUE") from the callback varies depending on the type of read operation.

The Response comes in callback `params->func`. The callback is run from the context specified by 'config BT\_RECV\_CONTEXT'. `params` must remain valid until start of callback.

This function will block while the ATT request queue is full, except when called from the BT RX thread, as this would cause a deadlock.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | params | Read parameters. |

Return values
:   | 0 | Successfully queued request. Will call `params->func` on resolution. |
    | --- | --- |
    | -ENOMEM | ATT request queue is full and blocking would cause deadlock. Allow a pending request to resolve before retrying, or call this function outside the BT RX thread to get blocking behavior. Queue size is controlled by `CONFIG_BT_ATT_TX_COUNT` . |

## [◆ ](#ga791b8bb8a4c085b022fafc0535a63511)bt\_gatt\_resubscribe()

| int bt\_gatt\_resubscribe | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *id*, |
| --- | --- | --- | --- |
|  |  | const [bt\_addr\_le\_t](structbt__addr__le__t.md) \* | *peer*, |
|  |  | struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \* | *params* ) |

`#include <[gatt.h](gatt_8h.md)>`

Resubscribe Attribute Value Notification subscription.

Resubscribe to Attribute Value Notification when already subscribed from a previous connection. The GATT server will remember subscription from previous connections when bonded, so resubscribing can be done without performing a new subscribe procedure after a power cycle.

Note
:   Notifications are asynchronous therefore the parameters need to remain valid while subscribed.

Parameters
:   | id | Local identity (in most cases BT\_ID\_DEFAULT). |
    | --- | --- |
    | peer | Remote address. |
    | params | Subscribe parameters. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga7d4a8e18f51ba6476886a15f81f48e5c)bt\_gatt\_subscribe()

| int bt\_gatt\_subscribe | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \* | *params* ) |

`#include <[gatt.h](gatt_8h.md)>`

Subscribe Attribute Value Notification.

This procedure subscribe to value notification using the Client Characteristic Configuration handle. If notification received subscribe value callback is called to return notified value. One may then decide whether to unsubscribe directly from this callback. Notification callback with NULL data will not be called if subscription was removed by this method.

The Response comes in callback `params->subscribe`. The callback is run from the context specified by 'config BT\_RECV\_CONTEXT'. The Notification callback `params->notify` is also called from the BT RX thread.

Note
:   Notifications are asynchronous therefore the `params` must remain valid while subscribed and cannot be reused for additional subscriptions whilst active.

This function will block while the ATT request queue is full, except when called from the BT RX thread, as this would cause a deadlock.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | params | Subscribe parameters. |

Return values
:   | 0 | Successfully queued request. Will call `params->write` on resolution. |
    | --- | --- |
    | -ENOMEM | ATT request queue is full and blocking would cause deadlock. Allow a pending request to resolve before retrying, or call this function outside the BT RX thread to get blocking behavior. Queue size is controlled by `CONFIG_BT_ATT_TX_COUNT` . |
    | -EALREADY | if there already exist a subscription using the `params`. |
    | -EBUSY | if `params.ccc_handle` is 0 and `CONFIG_BT_GATT_AUTO_DISCOVER_CCC` is enabled and discovery for the `params` is already in progress. |

## [◆ ](#ga56509c9b8f73f729cfa5e75be22d79ae)bt\_gatt\_unsubscribe()

| int bt\_gatt\_unsubscribe | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \* | *params* ) |

`#include <[gatt.h](gatt_8h.md)>`

Unsubscribe Attribute Value Notification.

This procedure unsubscribe to value notification using the Client Characteristic Configuration handle. Notification callback with NULL data will be called if subscription was removed by this call, until then the parameters cannot be reused.

The Response comes in callback `params->func`. The callback is run from the BT RX thread.

This function will block while the ATT request queue is full, except when called from the BT RX thread, as this would cause a deadlock.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | params | Subscribe parameters. The parameters shall be a [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md "bt_gatt_subscribe_params") from a previous call to [bt\_gatt\_subscribe()](#ga7d4a8e18f51ba6476886a15f81f48e5c). |

Return values
:   | 0 | Successfully queued request. Will call `params->write` on resolution. |
    | --- | --- |
    | -ENOMEM | ATT request queue is full and blocking would cause deadlock. Allow a pending request to resolve before retrying, or call this function outside the BT RX thread to get blocking behavior. Queue size is controlled by `CONFIG_BT_ATT_TX_COUNT` . |

## [◆ ](#ga843a42e68e0497d88d3f655f8ffd58d4)bt\_gatt\_write()

| int bt\_gatt\_write | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_gatt\_write\_params](structbt__gatt__write__params.md) \* | *params* ) |

`#include <[gatt.h](gatt_8h.md)>`

Write Attribute Value by handle.

The Response comes in callback `params->func`. The callback is run from the context specified by 'config BT\_RECV\_CONTEXT'. `params` must remain valid until start of callback.

This function will block while the ATT request queue is full, except when called from Bluetooth event context. When called from Bluetooth context, this function will instead instead return -[ENOMEM](group__system__errno.md#ga6a05c923dad0c1208043e9c20a58c8e5 "Not enough core.") if it would block to avoid a deadlock.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | params | Write parameters. |

Return values
:   | 0 | Successfully queued request. Will call `params->func` on resolution. |
    | --- | --- |
    | -ENOMEM | ATT request queue is full and blocking would cause deadlock. Allow a pending request to resolve before retrying, or call this function outside Bluetooth event context to get blocking behavior. Queue size is controlled by `CONFIG_BT_ATT_TX_COUNT` . |

## [◆ ](#ga9fc78e32230637a6f092da2400c50fe7)bt\_gatt\_write\_without\_response()

| | int bt\_gatt\_write\_without\_response | ( | struct bt\_conn \* | *conn*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *handle*, | |  |  | const void \* | *data*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *length*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *sign* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

Write Attribute Value by handle without response.

This procedure write the attribute value without requiring an acknowledgment that the write was successfully performed

This function will block while the ATT request queue is full, except when called from the BT RX thread, as this would cause a deadlock.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | handle | Attribute handle. |
    | data | Data to be written. |
    | length | Data length. |
    | sign | Whether to sign data |

Return values
:   | 0 | Successfully queued request. |
    | --- | --- |
    | -ENOMEM | ATT request queue is full and blocking would cause deadlock. Allow a pending request to resolve before retrying, or call this function outside the BT RX thread to get blocking behavior. Queue size is controlled by `CONFIG_BT_ATT_TX_COUNT` . |

## [◆ ](#ga49439413d12b5a8a1c68735e961ab6fa)bt\_gatt\_write\_without\_response\_cb()

| int bt\_gatt\_write\_without\_response\_cb | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *handle*, |
|  |  | const void \* | *data*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *length*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *sign*, |
|  |  | [bt\_gatt\_complete\_func\_t](group__bt__gatt__server.md#gac55832607b95f394d26a64ed1cfe5bba) | *func*, |
|  |  | void \* | *user\_data* ) |

`#include <[gatt.h](gatt_8h.md)>`

Write Attribute Value by handle without response with callback.

This function works in the same way as [bt\_gatt\_write\_without\_response](#ga9fc78e32230637a6f092da2400c50fe7). With the addition that after sending the write the callback function will be called.

The callback is run from System Workqueue context. When called from the System Workqueue context this API will not wait for resources for the callback but instead return an error. The number of pending callbacks can be increased with the `CONFIG_BT_CONN_TX_MAX` option.

Note
:   By using a callback it also disable the internal flow control which would prevent sending multiple commands without waiting for their transmissions to complete, so if that is required the caller shall not submit more data until the callback is called.

This function will block while the ATT request queue is full, except when called from the BT RX thread, as this would cause a deadlock.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | handle | Attribute handle. |
    | data | Data to be written. |
    | length | Data length. |
    | sign | Whether to sign data |
    | func | Transmission complete callback. |
    | user\_data | User data to be passed back to callback. |

Return values
:   | 0 | Successfully queued request. |
    | --- | --- |
    | -ENOMEM | ATT request queue is full and blocking would cause deadlock. Allow a pending request to resolve before retrying, or call this function outside the BT RX thread to get blocking behavior. Queue size is controlled by `CONFIG_BT_ATT_TX_COUNT` . |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
