---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/l2cap_8h.html
original_path: doxygen/html/l2cap_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

l2cap.h File Reference

Bluetooth L2CAP handling.
[More...](#details)

`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/bluetooth/buf.h](bluetooth_2buf_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/bluetooth/hci.h](hci_8h_source.md)>`

[Go to the source code of this file.](l2cap_8h_source.md)

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
| #define | [BT\_L2CAP\_HDR\_SIZE](group__bt__l2cap.md#gab33b91052026973180356640b7310659)   4 |
|  | L2CAP PDU header size, used for buffer size calculations. |
| #define | [BT\_L2CAP\_TX\_MTU](group__bt__l2cap.md#ga45ef5aee4ed4dd705cad6d234562c660)   (CONFIG\_BT\_L2CAP\_TX\_MTU) |
|  | Maximum Transmission Unit (MTU) for an outgoing L2CAP PDU. |
| #define | [BT\_L2CAP\_RX\_MTU](group__bt__l2cap.md#ga6e458a1758e5012755f3b97f8348c966)   (CONFIG\_BT\_BUF\_ACL\_RX\_SIZE - [BT\_L2CAP\_HDR\_SIZE](group__bt__l2cap.md#gab33b91052026973180356640b7310659)) |
|  | Maximum Transmission Unit (MTU) for an incoming L2CAP PDU. |
| #define | [BT\_L2CAP\_BUF\_SIZE](group__bt__l2cap.md#gab95b119de4757588074e367a90a7136a)(mtu) |
|  | Helper to calculate needed buffer size for L2CAP PDUs. |
| #define | [BT\_L2CAP\_SDU\_HDR\_SIZE](group__bt__l2cap.md#ga967c4c3f9b9beba1d0ce8516c5d1c659)   2 |
|  | L2CAP SDU header size, used for buffer size calculations. |
| #define | [BT\_L2CAP\_SDU\_TX\_MTU](group__bt__l2cap.md#gaa6fcd053d918db7005bc058501c2a598)   ([BT\_L2CAP\_TX\_MTU](group__bt__l2cap.md#ga45ef5aee4ed4dd705cad6d234562c660) - [BT\_L2CAP\_SDU\_HDR\_SIZE](group__bt__l2cap.md#ga967c4c3f9b9beba1d0ce8516c5d1c659)) |
|  | Maximum Transmission Unit for an unsegmented outgoing L2CAP SDU. |
| #define | [BT\_L2CAP\_SDU\_RX\_MTU](group__bt__l2cap.md#ga13b93a8f09157fbcf739fa4949840efe)   ([BT\_L2CAP\_RX\_MTU](group__bt__l2cap.md#ga6e458a1758e5012755f3b97f8348c966) - [BT\_L2CAP\_SDU\_HDR\_SIZE](group__bt__l2cap.md#ga967c4c3f9b9beba1d0ce8516c5d1c659)) |
|  | Maximum Transmission Unit for an unsegmented incoming L2CAP SDU. |
| #define | [BT\_L2CAP\_SDU\_BUF\_SIZE](group__bt__l2cap.md#ga1c76618c32bbe86b18fd8663760fb220)(mtu) |
|  | Helper to calculate needed buffer size for L2CAP SDUs. |
| #define | [BT\_L2CAP\_LE\_CHAN](group__bt__l2cap.md#gac936761e661a5c65d65ee9b4c185679b)(\_ch) |
|  | Helper macro getting container object of type [bt\_l2cap\_le\_chan](structbt__l2cap__le__chan.md "LE L2CAP Channel structure.") address having the same container chan member address as object in question. |
| #define | [BT\_L2CAP\_CHAN\_SEND\_RESERVE](group__bt__l2cap.md#ga281232ec622c626c0be2be23bae18d8d)   ([BT\_L2CAP\_BUF\_SIZE](group__bt__l2cap.md#gab95b119de4757588074e367a90a7136a)(0)) |
|  | Headroom needed for outgoing L2CAP PDUs. |
| #define | [BT\_L2CAP\_SDU\_CHAN\_SEND\_RESERVE](group__bt__l2cap.md#gabdb3983d3862f6654a1653dd45c4157d)   ([BT\_L2CAP\_SDU\_BUF\_SIZE](group__bt__l2cap.md#ga1c76618c32bbe86b18fd8663760fb220)(0)) |
|  | Headroom needed for outgoing L2CAP SDUs. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [bt\_l2cap\_chan\_destroy\_t](group__bt__l2cap.md#ga88baae9c159f3de4ccb34fd0e3cc8c3b)) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan) |
|  | Channel destroy callback. |
| typedef enum [bt\_l2cap\_chan\_state](group__bt__l2cap.md#ga642436bdf29f79495763b10231c6b25b) | [bt\_l2cap\_chan\_state\_t](group__bt__l2cap.md#ga5a80330e52ea0fa4ee3266094570bb16) |
|  | Life-span states of L2CAP CoC channel. |
| typedef enum [bt\_l2cap\_chan\_status](group__bt__l2cap.md#ga371a747c8939a1156111dc03c774015c) | [bt\_l2cap\_chan\_status\_t](group__bt__l2cap.md#ga3a1a88a8e87aefe9bea1dd01aa193b42) |
|  | Status of L2CAP channel. |

| Enumerations | |
| --- | --- |
| enum | [bt\_l2cap\_chan\_state](group__bt__l2cap.md#ga642436bdf29f79495763b10231c6b25b) {     [BT\_L2CAP\_DISCONNECTED](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba1dc4c69537acf13a8c00dfca5acfb83c) , [BT\_L2CAP\_CONNECTING](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25bac2a46c646c8739e8b129b89698eae7cd) , [BT\_L2CAP\_CONFIG](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba3167a1b491cb9b97ebe51f66c209f064) , [BT\_L2CAP\_CONNECTED](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba3adc86576ca2db5a7f74030d11699b68) ,     [BT\_L2CAP\_DISCONNECTING](group__bt__l2cap.md#gga642436bdf29f79495763b10231c6b25ba7a24502cfb06df715f58ad2e088cb7e8)   } |
|  | Life-span states of L2CAP CoC channel. [More...](group__bt__l2cap.md#ga642436bdf29f79495763b10231c6b25b) |
| enum | [bt\_l2cap\_chan\_status](group__bt__l2cap.md#ga371a747c8939a1156111dc03c774015c) { [BT\_L2CAP\_STATUS\_OUT](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca89aea3cf3d9a004ffd53eae602666fd5) , [BT\_L2CAP\_STATUS\_SHUTDOWN](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca82d4e553f4298d00c27045949663208e) , [BT\_L2CAP\_STATUS\_ENCRYPT\_PENDING](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015caea6cc7cae26d69926e7def91242650af) , [BT\_L2CAP\_NUM\_STATUS](group__bt__l2cap.md#gga371a747c8939a1156111dc03c774015ca91bd77f9889b59ba5b0005a51016ba2c) } |
|  | Status of L2CAP channel. [More...](group__bt__l2cap.md#ga371a747c8939a1156111dc03c774015c) |

| Functions | |
| --- | --- |
| int | [bt\_l2cap\_server\_register](group__bt__l2cap.md#ga1a5e8c81c086872d7fb8da5329f982c6) (struct [bt\_l2cap\_server](structbt__l2cap__server.md) \*server) |
|  | Register L2CAP server. |
| int | [bt\_l2cap\_br\_server\_register](group__bt__l2cap.md#ga5b0ae2abd714f46e6bb2394bce33e613) (struct [bt\_l2cap\_server](structbt__l2cap__server.md) \*server) |
|  | Register L2CAP server on BR/EDR oriented connection. |
| int | [bt\_l2cap\_ecred\_chan\_connect](group__bt__l2cap.md#gaebc2d157fb5f013722e9c332b3d81804) (struct bt\_conn \*conn, struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*\*chans, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) psm) |
|  | Connect Enhanced Credit Based L2CAP channels. |
| int | [bt\_l2cap\_ecred\_chan\_reconfigure](group__bt__l2cap.md#ga05d28a51d9fba08d609287957ea4c7ec) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*\*chans, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mtu) |
|  | Reconfigure Enhanced Credit Based L2CAP channels. |
| int | [bt\_l2cap\_chan\_connect](group__bt__l2cap.md#ga3c3cfb4b151c808c0a3d2562a5c26a20) (struct bt\_conn \*conn, struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) psm) |
|  | Connect L2CAP channel. |
| int | [bt\_l2cap\_chan\_disconnect](group__bt__l2cap.md#ga7165f82a05e3a19d6b2baf0ba292a3fe) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan) |
|  | Disconnect L2CAP channel. |
| int | [bt\_l2cap\_chan\_send](group__bt__l2cap.md#ga97b7909749667f910f83e6fcb54495c3) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Send data to L2CAP channel. |
| int | [bt\_l2cap\_chan\_give\_credits](group__bt__l2cap.md#ga9bc950a929fc2bdb1463c268cea478b6) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) additional\_credits) |
|  | Give credits to the remote. |
| int | [bt\_l2cap\_chan\_recv\_complete](group__bt__l2cap.md#gad53f5fc31314121ff84e740879eae3cf) (struct [bt\_l2cap\_chan](structbt__l2cap__chan.md) \*chan, struct [net\_buf](structnet__buf.md) \*buf) |
|  | Complete receiving L2CAP channel data. |

## Detailed Description

Bluetooth L2CAP handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [l2cap.h](l2cap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
