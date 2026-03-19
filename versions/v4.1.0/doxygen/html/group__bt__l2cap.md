---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__l2cap.html
original_path: doxygen/html/group__bt__l2cap.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

L2CAP

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

L2CAP.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_l2cap\_chan](structbt__l2cap__chan.md) |
|  | L2CAP Channel structure. [More...](structbt__l2cap__chan.md#details) |
| struct | [bt\_l2cap\_le\_endpoint](structbt__l2cap__le__endpoint.md) |
|  | LE L2CAP Endpoint structure. [More...](structbt__l2cap__le__endpoint.md#details) |
| struct | [bt\_l2cap\_le\_chan](structbt__l2cap__le__chan.md) |
|  | LE L2CAP Channel structure. [More...](structbt__l2cap__le__chan.md#details) |
| struct | [bt\_l2cap\_br\_endpoint](structbt__l2cap__br__endpoint.md) |
|  | BREDR L2CAP Endpoint structure. [More...](structbt__l2cap__br__endpoint.md#details) |
| struct | [bt\_l2cap\_br\_chan](structbt__l2cap__br__chan.md) |
|  | BREDR L2CAP Channel structure. [More...](structbt__l2cap__br__chan.md#details) |
| struct | [bt\_l2cap\_chan\_ops](structbt__l2cap__chan__ops.md) |
|  | L2CAP Channel operations structure. [More...](structbt__l2cap__chan__ops.md#details) |
| struct | [bt\_l2cap\_server](structbt__l2cap__server.md) |
|  | L2CAP Server structure. [More...](structbt__l2cap__server.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_L2CAP\_HDR\_SIZE](#gab33b91052026973180356640b7310659)   4 |
|  | L2CAP PDU header size, used for buffer size calculations. |
| #define | [BT\_L2CAP\_TX\_MTU](#ga45ef5aee4ed4dd705cad6d234562c660)   (CONFIG\_BT\_L2CAP\_TX\_MTU) |
|  | Maximum Transmission Unit (MTU) for an outgoing L2CAP PDU. |
| #define | [BT\_L2CAP\_RX\_MTU](#ga6e458a1758e5012755f3b97f8348c966)   (CONFIG\_BT\_BUF\_ACL\_RX\_SIZE - [BT\_L2CAP\_HDR\_SIZE](#gab33b91052026973180356640b7310659)) |
|  | Maximum Transmission Unit (MTU) for an incoming L2CAP PDU. |
| #define | [BT\_L2CAP\_BUF\_SIZE](#gab95b119de4757588074e367a90a7136a)(mtu) |
|  | Helper to calculate needed buffer size for L2CAP PDUs. |
| #define | [BT\_L2CAP\_SDU\_HDR\_SIZE](#ga967c4c3f9b9beba1d0ce8516c5d1c659)   2 |
|  | L2CAP SDU header size, used for buffer size calculations. |
| #define | [BT\_L2CAP\_SDU\_TX\_MTU](#gaa6fcd053d918db7005bc058501c2a598)   ([BT\_L2CAP\_TX\_MTU](#ga45ef5aee4ed4dd705cad6d234562c660) - [BT\_L2CAP\_SDU\_HDR\_SIZE](#ga967c4c3f9b9beba1d0ce8516c5d1c659)) |
|  | Maximum Transmission Unit for an unsegmented outgoing L2CAP SDU. |
| #define | [BT\_L2CAP\_SDU\_RX\_MTU](#ga13b93a8f09157fbcf739fa4949840efe)   ([BT\_L2CAP\_RX\_MTU](#ga6e458a1758e5012755f3b97f8348c966) - [BT\_L2CAP\_SDU\_HDR\_SIZE](#ga967c4c3f9b9beba1d0ce8516c5d1c659)) |
|  | Maximum Transmission Unit for an unsegmented incoming L2CAP SDU. |
| #define | [BT\_L2CAP\_SDU\_BUF\_SIZE](#ga1c76618c32bbe86b18fd8663760fb220)(mtu) |
|  | Helper to calculate needed buffer size for L2CAP SDUs. |
| #define | [BT\_L2CAP\_ECRED\_MIN\_MTU](#gac201afc0f1f55b89a023f03162ba57fe)   64 |
|  | L2CAP ECRED minimum MTU. |
| #define | [BT\_L2CAP\_ECRED\_MIN\_MPS](#ga11933f5a909578f0768f60ce0c8e4c86)   64 |
|  | L2CAP ECRED minimum MPS. |
| #define | [BT\_L2CAP\_ECRED\_CHAN\_MAX\_PER\_REQ](#gaf4c98aa3e9f5293b2ff693fb69dc71c9)   5 |
|  | The maximum number of channels in ECRED L2CAP signaling PDUs. |
| #define | [BT\_L2CAP\_LE\_CHAN](#gac936761e661a5c65d65ee9b4c185679b)(\_ch) |
|  | Helper macro getting container object of type [bt\_l2cap\_le\_chan](structbt__l2cap__le__chan.md "LE L2CAP Channel structure.") address having the same container chan member address as object in question. |
| #define | [BT\_L2CAP\_CHAN\_SEND\_RESERVE](#ga281232ec622c626c0be2be23bae18d8d)   ([BT\_L2CAP\_BUF\_SIZE](#gab95b119de4757588074e367a90a7136a)(0)) |
|  | Headroom needed for outgoing L2CAP PDUs. |
| #define | [BT\_L2CAP\_SDU\_CHAN\_SEND\_RESERVE](#gabdb3983d3862f6654a1653dd45c4157d)   ([BT\_L2CAP\_SDU\_BUF\_SIZE](#ga1c76618c32bbe86b18fd8663760fb220)(0)) |
|  | Headroom needed for outgoing L2CAP SDUs. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [bt\_l2cap\_chan\_destroy\_t](#ga88baae9c159f3de4ccb34fd0e3cc8c3b)) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan) |
|  | Channel destroy callback. |
| typedef enum [bt\_l2cap\_chan\_state](#ga642436bdf29f79495763b10231c6b25b) | [bt\_l2cap\_chan\_state\_t](#ga5a80330e52ea0fa4ee3266094570bb16) |
|  | Life-span states of L2CAP CoC channel. |
| typedef enum [bt\_l2cap\_chan\_status](#ga371a747c8939a1156111dc03c774015c) | [bt\_l2cap\_chan\_status\_t](#ga3a1a88a8e87aefe9bea1dd01aa193b42) |
|  | Status of L2CAP channel. |

| Enumerations | |
| --- | --- |
| enum | [bt\_l2cap\_chan\_state](#ga642436bdf29f79495763b10231c6b25b) {     [BT\_L2CAP\_DISCONNECTED](#gga642436bdf29f79495763b10231c6b25ba1dc4c69537acf13a8c00dfca5acfb83c) , [BT\_L2CAP\_CONNECTING](#gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd) , [BT\_L2CAP\_CONFIG](#gga642436bdf29f79495763b10231c6b25ba3167a1b491cb9b97ebe51f66c209f064) , [BT\_L2CAP\_CONNECTED](#gga642436bdf29f79495763b10231c6b25ba3adc86576ca2db5a7f74030d11699b68) ,     [BT\_L2CAP\_DISCONNECTING](#gga642436bdf29f79495763b10231c6b25ba7a24502cfb06df715f58ad2e088cb7e8)   } |
|  | Life-span states of L2CAP CoC channel. [More...](#ga642436bdf29f79495763b10231c6b25b) |
| enum | [bt\_l2cap\_chan\_status](#ga371a747c8939a1156111dc03c774015c) { [BT\_L2CAP\_STATUS\_OUT](#gga371a747c8939a1156111dc03c774015ca89aea3cf3d9a004ffd53eae602666fd5) , [BT\_L2CAP\_STATUS\_SHUTDOWN](#gga371a747c8939a1156111dc03c774015ca82d4e553f4298d00c27045949663208e) , [BT\_L2CAP\_STATUS\_ENCRYPT\_PENDING](#gga371a747c8939a1156111dc03c774015caea6cc7cae26d69926e7def91242650af) , [BT\_L2CAP\_NUM\_STATUS](#gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c) } |
|  | Status of L2CAP channel. [More...](#ga371a747c8939a1156111dc03c774015c) |

| Functions | |
| --- | --- |
| int | [bt\_l2cap\_server\_register](#ga1a5e8c81c086872d7fb8da5329f982c6) (struct [bt\_l2cap\_server](structbt__l2cap__server.md) \*server) |
|  | Register L2CAP server. |
| int | [bt\_l2cap\_br\_server\_register](#ga5b0ae2abd714f46e6bb2394bce33e613) (struct [bt\_l2cap\_server](structbt__l2cap__server.md) \*server) |
|  | Register L2CAP server on BR/EDR oriented connection. |
| int | [bt\_l2cap\_ecred\_chan\_connect](#gaebc2d157fb5f013722e9c332b3d81804) (struct bt\_conn \*conn, struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*\*chans, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) psm) |
|  | Connect Enhanced Credit Based L2CAP channels. |
| int | [bt\_l2cap\_ecred\_chan\_reconfigure](#ga05d28a51d9fba08d609287957ea4c7ec) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*\*chans, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mtu) |
|  | Reconfigure Enhanced Credit Based L2CAP channels. |
| int | [bt\_l2cap\_ecred\_chan\_reconfigure\_explicit](#ga67e13b0048eb68ef35c315a5276d832d) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*\*chans, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) chan\_count, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mtu, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mps) |
|  | Reconfigure Enhanced Credit Based L2CAP channels. |
| int | [bt\_l2cap\_chan\_connect](#ga3c3cfb4b151c808c0a3d2562a5c26a20) (struct bt\_conn \*conn, struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) psm) |
|  | Connect L2CAP channel. |
| int | [bt\_l2cap\_chan\_disconnect](#ga7165f82a05e3a19d6b2baf0ba292a3fe) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan) |
|  | Disconnect L2CAP channel. |
| int | [bt\_l2cap\_chan\_send](#ga97b7909749667f910f83e6fcb54495c3) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Send data to L2CAP channel. |
| int | [bt\_l2cap\_chan\_give\_credits](#ga9bc950a929fc2bdb1463c268cea478b6) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) additional\_credits) |
|  | Give credits to the remote. |
| int | [bt\_l2cap\_chan\_recv\_complete](#gad53f5fc31314121ff84e740879eae3cf) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Complete receiving L2CAP channel data. |

## Detailed Description

L2CAP.

## Macro Definition Documentation

## [◆ ](#gab95b119de4757588074e367a90a7136a)BT\_L2CAP\_BUF\_SIZE

| #define BT\_L2CAP\_BUF\_SIZE | ( |  | *mtu* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[l2cap.h](l2cap_8h.md)>`

**Value:**

[BT\_BUF\_ACL\_SIZE](group__bt__buf.md#ga8f570211d5e391be63bd46c189eac637)([BT\_L2CAP\_HDR\_SIZE](#gab33b91052026973180356640b7310659) + (mtu))

[BT\_BUF\_ACL\_SIZE](group__bt__buf.md#ga8f570211d5e391be63bd46c189eac637)

#define BT\_BUF\_ACL\_SIZE(size)

Helper to calculate needed buffer size for HCI ACL packets.

**Definition** buf.h:61

[BT\_L2CAP\_HDR\_SIZE](#gab33b91052026973180356640b7310659)

#define BT\_L2CAP\_HDR\_SIZE

L2CAP PDU header size, used for buffer size calculations.

**Definition** l2cap.h:34

Helper to calculate needed buffer size for L2CAP PDUs.

Useful for creating buffer pools.

Parameters
:   | mtu | Needed L2CAP PDU MTU. |
    | --- | --- |

Returns
:   Needed buffer size to match the requested L2CAP PDU MTU.

## [◆ ](#ga281232ec622c626c0be2be23bae18d8d)BT\_L2CAP\_CHAN\_SEND\_RESERVE

| #define BT\_L2CAP\_CHAN\_SEND\_RESERVE   ([BT\_L2CAP\_BUF\_SIZE](#gab95b119de4757588074e367a90a7136a)(0)) |
| --- |

`#include <[l2cap.h](l2cap_8h.md)>`

Headroom needed for outgoing L2CAP PDUs.

## [◆ ](#gaf4c98aa3e9f5293b2ff693fb69dc71c9)BT\_L2CAP\_ECRED\_CHAN\_MAX\_PER\_REQ

| #define BT\_L2CAP\_ECRED\_CHAN\_MAX\_PER\_REQ   5 |
| --- |

`#include <[l2cap.h](l2cap_8h.md)>`

The maximum number of channels in ECRED L2CAP signaling PDUs.

Currently, this is the maximum number of channels referred to in the following PDUs:

- L2CAP\_CREDIT\_BASED\_CONNECTION\_REQ
- L2CAP\_CREDIT\_BASED\_RECONFIGURE\_REQ

Warning
:   The commonality is inferred between the PDUs. The Bluetooth specification treats these as separate numbers and does now guarantee the same limit for potential future ECRED L2CAP signaling PDUs.

## [◆ ](#ga11933f5a909578f0768f60ce0c8e4c86)BT\_L2CAP\_ECRED\_MIN\_MPS

| #define BT\_L2CAP\_ECRED\_MIN\_MPS   64 |
| --- |

`#include <[l2cap.h](l2cap_8h.md)>`

L2CAP ECRED minimum MPS.

The minimum MPS for an L2CAP Enhanced Credit Based Connection.

This requirement is inferred from text in Core 3.A.4.25 v6.0:

```
L2CAP implementations shall support a minimum MPS of 64 and may
support an MPS up to 65533 octets for these channels.
```

## [◆ ](#gac201afc0f1f55b89a023f03162ba57fe)BT\_L2CAP\_ECRED\_MIN\_MTU

| #define BT\_L2CAP\_ECRED\_MIN\_MTU   64 |
| --- |

`#include <[l2cap.h](l2cap_8h.md)>`

L2CAP ECRED minimum MTU.

The minimum MTU for an L2CAP Enhanced Credit Based Connection.

This requirement is inferred from text in Core 3.A.4.25 v6.0:

```
L2CAP implementations shall support a minimum MTU size of 64
octets for these channels.
```

## [◆ ](#gab33b91052026973180356640b7310659)BT\_L2CAP\_HDR\_SIZE

| #define BT\_L2CAP\_HDR\_SIZE   4 |
| --- |

`#include <[l2cap.h](l2cap_8h.md)>`

L2CAP PDU header size, used for buffer size calculations.

## [◆ ](#gac936761e661a5c65d65ee9b4c185679b)BT\_L2CAP\_LE\_CHAN

| #define BT\_L2CAP\_LE\_CHAN | ( |  | *\_ch* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[l2cap.h](l2cap_8h.md)>`

**Value:**

[CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)(\_ch, struct [bt\_l2cap\_le\_chan](structbt__l2cap__le__chan.md), chan)

[CONTAINER\_OF](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f)

#define CONTAINER\_OF(ptr, type, field)

Get a pointer to a structure containing the element.

**Definition** util.h:284

[bt\_l2cap\_le\_chan](structbt__l2cap__le__chan.md)

LE L2CAP Channel structure.

**Definition** l2cap.h:202

Helper macro getting container object of type [bt\_l2cap\_le\_chan](structbt__l2cap__le__chan.md "LE L2CAP Channel structure.") address having the same container chan member address as object in question.

Parameters
:   | \_ch | Address of object of [bt\_l2cap\_chan](structbt__l2cap__chan.md "L2CAP Channel structure.") type |
    | --- | --- |

Returns
:   Address of in memory [bt\_l2cap\_le\_chan](structbt__l2cap__le__chan.md "LE L2CAP Channel structure.") object type containing the address of in question object.

## [◆ ](#ga6e458a1758e5012755f3b97f8348c966)BT\_L2CAP\_RX\_MTU

| #define BT\_L2CAP\_RX\_MTU   (CONFIG\_BT\_BUF\_ACL\_RX\_SIZE - [BT\_L2CAP\_HDR\_SIZE](#gab33b91052026973180356640b7310659)) |
| --- |

`#include <[l2cap.h](l2cap_8h.md)>`

Maximum Transmission Unit (MTU) for an incoming L2CAP PDU.

## [◆ ](#ga1c76618c32bbe86b18fd8663760fb220)BT\_L2CAP\_SDU\_BUF\_SIZE

| #define BT\_L2CAP\_SDU\_BUF\_SIZE | ( |  | *mtu* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[l2cap.h](l2cap_8h.md)>`

**Value:**

[BT\_L2CAP\_BUF\_SIZE](#gab95b119de4757588074e367a90a7136a)([BT\_L2CAP\_SDU\_HDR\_SIZE](#ga967c4c3f9b9beba1d0ce8516c5d1c659) + (mtu))

[BT\_L2CAP\_SDU\_HDR\_SIZE](#ga967c4c3f9b9beba1d0ce8516c5d1c659)

#define BT\_L2CAP\_SDU\_HDR\_SIZE

L2CAP SDU header size, used for buffer size calculations.

**Definition** l2cap.h:52

[BT\_L2CAP\_BUF\_SIZE](#gab95b119de4757588074e367a90a7136a)

#define BT\_L2CAP\_BUF\_SIZE(mtu)

Helper to calculate needed buffer size for L2CAP PDUs.

**Definition** l2cap.h:49

Helper to calculate needed buffer size for L2CAP SDUs.

Useful for creating buffer pools.

Parameters
:   | mtu | Required BT\_L2CAP\_\*\_SDU. |
    | --- | --- |

Returns
:   Needed buffer size to match the requested L2CAP SDU MTU.

## [◆ ](#gabdb3983d3862f6654a1653dd45c4157d)BT\_L2CAP\_SDU\_CHAN\_SEND\_RESERVE

| #define BT\_L2CAP\_SDU\_CHAN\_SEND\_RESERVE   ([BT\_L2CAP\_SDU\_BUF\_SIZE](#ga1c76618c32bbe86b18fd8663760fb220)(0)) |
| --- |

`#include <[l2cap.h](l2cap_8h.md)>`

Headroom needed for outgoing L2CAP SDUs.

## [◆ ](#ga967c4c3f9b9beba1d0ce8516c5d1c659)BT\_L2CAP\_SDU\_HDR\_SIZE

| #define BT\_L2CAP\_SDU\_HDR\_SIZE   2 |
| --- |

`#include <[l2cap.h](l2cap_8h.md)>`

L2CAP SDU header size, used for buffer size calculations.

## [◆ ](#ga13b93a8f09157fbcf739fa4949840efe)BT\_L2CAP\_SDU\_RX\_MTU

| #define BT\_L2CAP\_SDU\_RX\_MTU   ([BT\_L2CAP\_RX\_MTU](#ga6e458a1758e5012755f3b97f8348c966) - [BT\_L2CAP\_SDU\_HDR\_SIZE](#ga967c4c3f9b9beba1d0ce8516c5d1c659)) |
| --- |

`#include <[l2cap.h](l2cap_8h.md)>`

Maximum Transmission Unit for an unsegmented incoming L2CAP SDU.

The Maximum Transmission Unit for an incoming L2CAP SDU when sent without segmentation, i.e. a single L2CAP SDU will fit inside a single L2CAP PDU.

The MTU for incoming L2CAP SDUs with segmentation is defined by the size of the application buffer pool. The application will have to define an alloc\_buf callback for the channel in order to support receiving segmented L2CAP SDUs.

## [◆ ](#gaa6fcd053d918db7005bc058501c2a598)BT\_L2CAP\_SDU\_TX\_MTU

| #define BT\_L2CAP\_SDU\_TX\_MTU   ([BT\_L2CAP\_TX\_MTU](#ga45ef5aee4ed4dd705cad6d234562c660) - [BT\_L2CAP\_SDU\_HDR\_SIZE](#ga967c4c3f9b9beba1d0ce8516c5d1c659)) |
| --- |

`#include <[l2cap.h](l2cap_8h.md)>`

Maximum Transmission Unit for an unsegmented outgoing L2CAP SDU.

The Maximum Transmission Unit for an outgoing L2CAP SDU when sent without segmentation, i.e. a single L2CAP SDU will fit inside a single L2CAP PDU.

The MTU for outgoing L2CAP SDUs with segmentation is defined by the size of the application buffer pool.

## [◆ ](#ga45ef5aee4ed4dd705cad6d234562c660)BT\_L2CAP\_TX\_MTU

| #define BT\_L2CAP\_TX\_MTU   (CONFIG\_BT\_L2CAP\_TX\_MTU) |
| --- |

`#include <[l2cap.h](l2cap_8h.md)>`

Maximum Transmission Unit (MTU) for an outgoing L2CAP PDU.

## Typedef Documentation

## [◆ ](#ga88baae9c159f3de4ccb34fd0e3cc8c3b)bt\_l2cap\_chan\_destroy\_t

| typedef void(\* bt\_l2cap\_chan\_destroy\_t) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan) |
| --- |

`#include <[l2cap.h](l2cap_8h.md)>`

Channel destroy callback.

Parameters
:   | chan | Channel object. |
    | --- | --- |

## [◆ ](#ga5a80330e52ea0fa4ee3266094570bb16)bt\_l2cap\_chan\_state\_t

| typedef enum [bt\_l2cap\_chan\_state](#ga642436bdf29f79495763b10231c6b25b) [bt\_l2cap\_chan\_state\_t](#ga5a80330e52ea0fa4ee3266094570bb16) |
| --- |

`#include <[l2cap.h](l2cap_8h.md)>`

Life-span states of L2CAP CoC channel.

Used only by internal APIs dealing with setting channel to proper state depending on operational context.

A channel enters the [BT\_L2CAP\_CONNECTING](#gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd) state upon [bt\_l2cap\_chan\_connect](#ga3c3cfb4b151c808c0a3d2562a5c26a20), [bt\_l2cap\_ecred\_chan\_connect](#gaebc2d157fb5f013722e9c332b3d81804) or upon returning from [bt\_l2cap\_server::accept](structbt__l2cap__server.md#ad31a1908f7dc733f9497164ccabba2af "bt_l2cap_server::accept").

When a channel leaves the [BT\_L2CAP\_CONNECTING](#gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd) state, [bt\_l2cap\_chan\_ops::connected](structbt__l2cap__chan__ops.md#a3a4dd75a11c9867adcade6d288dec2de "bt_l2cap_chan_ops::connected") is called.

## [◆ ](#ga3a1a88a8e87aefe9bea1dd01aa193b42)bt\_l2cap\_chan\_status\_t

| typedef enum [bt\_l2cap\_chan\_status](#ga371a747c8939a1156111dc03c774015c) [bt\_l2cap\_chan\_status\_t](#ga3a1a88a8e87aefe9bea1dd01aa193b42) |
| --- |

`#include <[l2cap.h](l2cap_8h.md)>`

Status of L2CAP channel.

## Enumeration Type Documentation

## [◆ ](#ga642436bdf29f79495763b10231c6b25b)bt\_l2cap\_chan\_state

| enum [bt\_l2cap\_chan\_state](#ga642436bdf29f79495763b10231c6b25b) |
| --- |

`#include <[l2cap.h](l2cap_8h.md)>`

Life-span states of L2CAP CoC channel.

Used only by internal APIs dealing with setting channel to proper state depending on operational context.

A channel enters the [BT\_L2CAP\_CONNECTING](#gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd) state upon [bt\_l2cap\_chan\_connect](#ga3c3cfb4b151c808c0a3d2562a5c26a20), [bt\_l2cap\_ecred\_chan\_connect](#gaebc2d157fb5f013722e9c332b3d81804) or upon returning from [bt\_l2cap\_server::accept](structbt__l2cap__server.md#ad31a1908f7dc733f9497164ccabba2af "bt_l2cap_server::accept").

When a channel leaves the [BT\_L2CAP\_CONNECTING](#gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd) state, [bt\_l2cap\_chan\_ops::connected](structbt__l2cap__chan__ops.md#a3a4dd75a11c9867adcade6d288dec2de "bt_l2cap_chan_ops::connected") is called.

| Enumerator | |
| --- | --- |
| BT\_L2CAP\_DISCONNECTED | Channel disconnected. |
| BT\_L2CAP\_CONNECTING | Channel in connecting state. |
| BT\_L2CAP\_CONFIG | Channel in config state, BR/EDR specific. |
| BT\_L2CAP\_CONNECTED | Channel ready for upper layer traffic on it. |
| BT\_L2CAP\_DISCONNECTING | Channel in disconnecting state. |

## [◆ ](#ga371a747c8939a1156111dc03c774015c)bt\_l2cap\_chan\_status

| enum [bt\_l2cap\_chan\_status](#ga371a747c8939a1156111dc03c774015c) |
| --- |

`#include <[l2cap.h](l2cap_8h.md)>`

Status of L2CAP channel.

| Enumerator | |
| --- | --- |
| BT\_L2CAP\_STATUS\_OUT | Channel can send at least one PDU. |
| BT\_L2CAP\_STATUS\_SHUTDOWN | Channel shutdown status.  Once this status is notified it means the channel will no longer be able to transmit or receive data. |
| BT\_L2CAP\_STATUS\_ENCRYPT\_PENDING | Channel encryption pending status. |
| BT\_L2CAP\_NUM\_STATUS |  |

## Function Documentation

## [◆ ](#ga5b0ae2abd714f46e6bb2394bce33e613)bt\_l2cap\_br\_server\_register()

| int bt\_l2cap\_br\_server\_register | ( | struct [bt\_l2cap\_server](structbt__l2cap__server.md) \* | *server* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[l2cap.h](l2cap_8h.md)>`

Register L2CAP server on BR/EDR oriented connection.

Register L2CAP server for a PSM, each new connection is authorized using the [accept()](posix_2sys_2socket_8h.md#a66e3de379c18201b21c889035ec54864) callback which in case of success shall allocate the channel structure to be used by the new connection.

For fixed, SIG-assigned PSMs (in the range 0x0001-0x0eff) the PSM should be assigned to server->psm before calling this API. For dynamic PSMs (in the range 0x1000-0xffff) server->psm may be pre-set to a given value (this is however not recommended) or be left as 0, in which case upon return a newly allocated value will have been assigned to it. For dynamically allocated values the expectation is that it's exposed through a SDP record, and that's how L2CAP clients discover how to connect to the server.

Parameters
:   | server | Server structure. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga3c3cfb4b151c808c0a3d2562a5c26a20)bt\_l2cap\_chan\_connect()

| int bt\_l2cap\_chan\_connect | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \* | *chan*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *psm* ) |

`#include <[l2cap.h](l2cap_8h.md)>`

Connect L2CAP channel.

Connect L2CAP channel by PSM, once the connection is completed channel connected() callback will be called. If the connection is rejected disconnected() callback is called instead. Channel object passed (over an address of it) as second parameter shouldn't be instantiated in application as standalone. Instead of, application should create transport dedicated L2CAP objects, i.e. type of [bt\_l2cap\_le\_chan](structbt__l2cap__le__chan.md "LE L2CAP Channel structure.") for LE and/or type of [bt\_l2cap\_br\_chan](structbt__l2cap__br__chan.md "BREDR L2CAP Channel structure.") for BR/EDR. Then pass to this API the location (address) of [bt\_l2cap\_chan](structbt__l2cap__chan.md "L2CAP Channel structure.") type object which is a member of both transport dedicated objects.

Warning
:   It is the responsibility of the caller to zero out the parent of the chan object.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | chan | Channel object. |
    | psm | Channel PSM to connect to. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga7165f82a05e3a19d6b2baf0ba292a3fe)bt\_l2cap\_chan\_disconnect()

| int bt\_l2cap\_chan\_disconnect | ( | struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \* | *chan* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[l2cap.h](l2cap_8h.md)>`

Disconnect L2CAP channel.

Disconnect L2CAP channel, if the connection is pending it will be canceled and as a result the channel disconnected() callback is called. Regarding to input parameter, to get details see reference description to [bt\_l2cap\_chan\_connect()](#ga3c3cfb4b151c808c0a3d2562a5c26a20) API above.

Parameters
:   | chan | Channel object. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga9bc950a929fc2bdb1463c268cea478b6)bt\_l2cap\_chan\_give\_credits()

| int bt\_l2cap\_chan\_give\_credits | ( | struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \* | *chan*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *additional\_credits* ) |

`#include <[l2cap.h](l2cap_8h.md)>`

Give credits to the remote.

Only available for channels using [bt\_l2cap\_chan\_ops::seg\_recv](structbt__l2cap__chan__ops.md#a7759a713038d74748952d5f2eb712429 "bt_l2cap_chan_ops::seg_recv"). `CONFIG_BT_L2CAP_SEG_RECV` must be enabled to make this function available.

Each credit given allows the peer to send one segment.

This function depends on a valid `chan` object. Make sure to default-initialize or memset `chan` when allocating or reusing it for new connections.

Adding zero credits is not allowed.

Credits can be given before entering the [BT\_L2CAP\_CONNECTING](#gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd) state. Doing so will adjust the 'initial credits' sent in the connection PDU.

Must not be called while the channel is in [BT\_L2CAP\_CONNECTING](#gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd) state.

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gad53f5fc31314121ff84e740879eae3cf)bt\_l2cap\_chan\_recv\_complete()

| int bt\_l2cap\_chan\_recv\_complete | ( | struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \* | *chan*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *buf* ) |

`#include <[l2cap.h](l2cap_8h.md)>`

Complete receiving L2CAP channel data.

Complete the reception of incoming data. This shall only be called if the channel recv callback has returned -EINPROGRESS to process some incoming data. The buffer shall contain the original user\_data as that is used for storing the credits/segments used by the packet.

Parameters
:   | chan | Channel object. |
    | --- | --- |
    | buf | Buffer containing the data. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga97b7909749667f910f83e6fcb54495c3)bt\_l2cap\_chan\_send()

| int bt\_l2cap\_chan\_send | ( | struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \* | *chan*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf](structnet__buf.md) \* | *buf* ) |

`#include <[l2cap.h](l2cap_8h.md)>`

Send data to L2CAP channel.

Send data from buffer to the channel. If credits are not available, buf will be queued and sent as and when credits are received from peer. Regarding to first input parameter, to get details see reference description to [bt\_l2cap\_chan\_connect()](#ga3c3cfb4b151c808c0a3d2562a5c26a20) API above.

Network buffer fragments (ie buf->frags) are not supported.

When sending L2CAP data over an BR/EDR connection the application is sending L2CAP PDUs. The application is required to have reserved [BT\_L2CAP\_CHAN\_SEND\_RESERVE](#ga281232ec622c626c0be2be23bae18d8d) bytes in the buffer before sending. The application should use the [BT\_L2CAP\_BUF\_SIZE()](#gab95b119de4757588074e367a90a7136a) helper to correctly size the buffers for the for the outgoing buffer pool.

When sending L2CAP data over an LE connection the application is sending L2CAP SDUs. The application shall reserve [BT\_L2CAP\_SDU\_CHAN\_SEND\_RESERVE](#gabdb3983d3862f6654a1653dd45c4157d) bytes in the buffer before sending.

The application can use the [BT\_L2CAP\_SDU\_BUF\_SIZE()](#ga1c76618c32bbe86b18fd8663760fb220) helper to correctly size the buffer to account for the reserved headroom.

When segmenting an L2CAP SDU into L2CAP PDUs the stack will first attempt to allocate buffers from the channel's alloc\_seg callback and will fallback on the stack's global buffer pool (sized `CONFIG_BT_L2CAP_TX_BUF_COUNT`).

Warning
:   The buffer's user\_data *will* be overwritten by this function. Do not store anything in it. As soon as a call to this function has been made, consider ownership of user\_data transferred into the stack.

Note
:   Buffer ownership is transferred to the stack in case of success, in case of an error the caller retains the ownership of the buffer.

Returns
:   0 in case of success or negative value in case of error.
:   -EINVAL if buf or chan is NULL.
:   -EINVAL if chan is not either BR/EDR or LE credit-based.
:   -EINVAL if buffer doesn't have enough bytes reserved to fit header.
:   -EINVAL if buffer's reference counter != 1
:   -EMSGSIZE if buf is larger than chan's MTU.
:   -ENOTCONN if underlying conn is disconnected.
:   -ESHUTDOWN if L2CAP channel is disconnected.
:   -other (from lower layers) if chan is BR/EDR.

## [◆ ](#gaebc2d157fb5f013722e9c332b3d81804)bt\_l2cap\_ecred\_chan\_connect()

| int bt\_l2cap\_ecred\_chan\_connect | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*\* | *chans*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *psm* ) |

`#include <[l2cap.h](l2cap_8h.md)>`

Connect Enhanced Credit Based L2CAP channels.

Connect up to 5 L2CAP channels by PSM, once the connection is completed each channel connected() callback will be called. If the connection is rejected disconnected() callback is called instead.

Warning
:   It is the responsibility of the caller to zero out the parents of the chan objects.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | chans | Array of channel objects. |
    | psm | Channel PSM to connect to. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga05d28a51d9fba08d609287957ea4c7ec)bt\_l2cap\_ecred\_chan\_reconfigure()

| int bt\_l2cap\_ecred\_chan\_reconfigure | ( | struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*\* | *chans*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mtu* ) |

`#include <[l2cap.h](l2cap_8h.md)>`

Reconfigure Enhanced Credit Based L2CAP channels.

Reconfigure up to 5 L2CAP channels. Channels must be from the same bt\_conn. Once reconfiguration is completed each channel reconfigured() callback will be called. MTU cannot be decreased on any of provided channels.

Parameters
:   | chans | Array of channel objects. Null-terminated. Elements after the first 5 are silently ignored. |
    | --- | --- |
    | mtu | Channel MTU to reconfigure to. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga67e13b0048eb68ef35c315a5276d832d)bt\_l2cap\_ecred\_chan\_reconfigure\_explicit()

| int bt\_l2cap\_ecred\_chan\_reconfigure\_explicit | ( | struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*\* | *chans*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *chan\_count*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mtu*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mps* ) |

`#include <[l2cap.h](l2cap_8h.md)>`

Reconfigure Enhanced Credit Based L2CAP channels.

Experimental API to reconfigure L2CAP ECRED channels with explicit MPS and MTU values.

Pend a L2CAP ECRED reconfiguration for up to 5 channels. All provided channels must share the same [Connection management](group__bt__conn.md "Connection management").

This API cannot decrease the MTU of any channel, and it cannot decrease the MPS of any channel when more than one channel is provided.

There is no dedicated callback for this operation, but whenever a peer responds to a reconfiguration request, each affected channel's reconfigured() callback is invoked.

This function may block.

Warning
:   Known issue: The implementation returns -EBUSY if there already is an ongoing reconfigure operation on the same connection. The caller may try again later. There is no event signaling when the existing operation finishes.
:   Known issue: The implementation returns -ENOMEM when unable to allocate. The caller may try again later. There is no event signaling the availability of buffers.

Attention
:   Available only when the following Kconfig option is enabled: `CONFIG_BT_L2CAP_RECONFIGURE_EXPLICIT`.

Parameters
:   | chans | Array of channels to reconfigure. Must be non-empty and contain at most 5 ([BT\_L2CAP\_ECRED\_CHAN\_MAX\_PER\_REQ](#gaf4c98aa3e9f5293b2ff693fb69dc71c9)) elements. |
    | --- | --- |
    | chan\_count | Number of channels in the array. |
    | mtu | Desired MTU. Must be at least [BT\_L2CAP\_ECRED\_MIN\_MTU](#gac201afc0f1f55b89a023f03162ba57fe). |
    | mps | Desired MPS. Must be in range [BT\_L2CAP\_ECRED\_MIN\_MPS](#ga11933f5a909578f0768f60ce0c8e4c86) to [BT\_L2CAP\_RX\_MTU](#ga6e458a1758e5012755f3b97f8348c966). |

Return values
:   | 0 | Successfully pended operation. |
    | --- | --- |
    | -EINVAL | Bad arguments. See above requirements. |
    | -ENOTCONN | Connection object is not in connected state. |
    | -EBUSY | Another outgoing reconfiguration is pending on the same connection. |
    | -ENOMEM | Host is out of buffers. |

## [◆ ](#ga1a5e8c81c086872d7fb8da5329f982c6)bt\_l2cap\_server\_register()

| int bt\_l2cap\_server\_register | ( | struct [bt\_l2cap\_server](structbt__l2cap__server.md) \* | *server* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[l2cap.h](l2cap_8h.md)>`

Register L2CAP server.

Register L2CAP server for a PSM, each new connection is authorized using the [accept()](posix_2sys_2socket_8h.md#a66e3de379c18201b21c889035ec54864) callback which in case of success shall allocate the channel structure to be used by the new connection.

For fixed, SIG-assigned PSMs (in the range 0x0001-0x007f) the PSM should be assigned to server->psm before calling this API. For dynamic PSMs (in the range 0x0080-0x00ff) server->psm may be pre-set to a given value (this is however not recommended) or be left as 0, in which case upon return a newly allocated value will have been assigned to it. For dynamically allocated values the expectation is that it's exposed through a GATT service, and that's how L2CAP clients discover how to connect to the server.

Parameters
:   | server | Server structure. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
