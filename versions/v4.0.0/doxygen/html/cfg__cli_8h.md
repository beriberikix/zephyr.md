---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/cfg__cli_8h.html
original_path: doxygen/html/cfg__cli_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cfg\_cli.h File Reference

Configuration Client Model APIs.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](cfg__cli_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_cfg\_cli\_cb](structbt__mesh__cfg__cli__cb.md) |
|  | Mesh Configuration Client Status messages callback. [More...](structbt__mesh__cfg__cli__cb.md#details) |
| struct | [bt\_mesh\_cfg\_cli](structbt__mesh__cfg__cli.md) |
|  | Mesh Configuration Client Model Context. [More...](structbt__mesh__cfg__cli.md#details) |
| struct | [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) |
|  | Model publication configuration parameters. [More...](structbt__mesh__cfg__cli__mod__pub.md#details) |
| struct | [bt\_mesh\_cfg\_cli\_hb\_sub](structbt__mesh__cfg__cli__hb__sub.md) |
|  | Heartbeat subscription configuration parameters. [More...](structbt__mesh__cfg__cli__hb__sub.md#details) |
| struct | [bt\_mesh\_cfg\_cli\_hb\_pub](structbt__mesh__cfg__cli__hb__pub.md) |
|  | Heartbeat publication configuration parameters. [More...](structbt__mesh__cfg__cli__hb__pub.md#details) |
| struct | [bt\_mesh\_comp\_p0](structbt__mesh__comp__p0.md) |
|  | Parsed Composition data page 0 representation. [More...](structbt__mesh__comp__p0.md#details) |
| struct | [bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md) |
|  | Composition data page 0 element representation. [More...](structbt__mesh__comp__p0__elem.md#details) |
| struct | [bt\_mesh\_comp\_p1\_elem](structbt__mesh__comp__p1__elem.md) |
|  | Composition data page 1 element representation. [More...](structbt__mesh__comp__p1__elem.md#details) |
| struct | [bt\_mesh\_comp\_p1\_model\_item](structbt__mesh__comp__p1__model__item.md) |
|  | Composition data page 1 model item representation. [More...](structbt__mesh__comp__p1__model__item.md#details) |
| struct | [bt\_mesh\_comp\_p1\_item\_short](structbt__mesh__comp__p1__item__short.md) |
|  | Extended Model Item in short representation. [More...](structbt__mesh__comp__p1__item__short.md#details) |
| struct | [bt\_mesh\_comp\_p1\_item\_long](structbt__mesh__comp__p1__item__long.md) |
|  | Extended Model Item in long representation. [More...](structbt__mesh__comp__p1__item__long.md#details) |
| struct | [bt\_mesh\_comp\_p1\_ext\_item](structbt__mesh__comp__p1__ext__item.md) |
|  | Extended Model Item. [More...](structbt__mesh__comp__p1__ext__item.md#details) |
| struct | [bt\_mesh\_comp\_p2\_record](structbt__mesh__comp__p2__record.md) |
|  | Composition data page 2 record parsing structure. [More...](structbt__mesh__comp__p2__record.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_CFG\_CLI](group__bt__mesh__cfg__cli.md#ga2f0df6906a27ebbd86dcd11951114001)(cli\_data) |
|  | Generic Configuration Client model composition data entry. |
| #define | [BT\_MESH\_PUB\_PERIOD\_100MS](group__bt__mesh__cfg__cli.md#gab542c707fb5bad0a15088fefda775a42)(steps) |
|  | Helper macro to encode model publication period in units of 100ms. |
| #define | [BT\_MESH\_PUB\_PERIOD\_SEC](group__bt__mesh__cfg__cli.md#ga29435e527a73ff6e19339b773c8eb79e)(steps) |
|  | Helper macro to encode model publication period in units of 1 second. |
| #define | [BT\_MESH\_PUB\_PERIOD\_10SEC](group__bt__mesh__cfg__cli.md#ga654204077adaa08259d1afbfe92e070e)(steps) |
|  | Helper macro to encode model publication period in units of 10 seconds. |
| #define | [BT\_MESH\_PUB\_PERIOD\_10MIN](group__bt__mesh__cfg__cli.md#ga36c37f644ee39ad91b6167f68c806b7e)(steps) |
|  | Helper macro to encode model publication period in units of 10 minutes. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_cfg\_cli\_node\_reset](group__bt__mesh__cfg__cli.md#gac6675d227749a69cedc5455c70626b76) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*status) |
|  | Reset the target node and remove it from the network. |
| int | [bt\_mesh\_cfg\_cli\_comp\_data\_get](group__bt__mesh__cfg__cli.md#ga36259e9c811a8f1a21d642739cf297df) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) page, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp, struct [net\_buf\_simple](structnet__buf__simple.md) \*comp) |
|  | Get the target node's composition data. |
| int | [bt\_mesh\_cfg\_cli\_beacon\_get](group__bt__mesh__cfg__cli.md#ga2c8a79d1b70e91e0a09c848737bb4a22) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Get the target node's network beacon state. |
| int | [bt\_mesh\_cfg\_cli\_krp\_get](group__bt__mesh__cfg__cli.md#ga660df68049110332ff21610fe4e520c6) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*phase) |
|  | Get the target node's network key refresh phase state. |
| int | [bt\_mesh\_cfg\_cli\_krp\_set](group__bt__mesh__cfg__cli.md#gae51eee59090cfebed4561ed3bb4df005) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) transition, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*phase) |
|  | Set the target node's network key refresh phase parameters. |
| int | [bt\_mesh\_cfg\_cli\_beacon\_set](group__bt__mesh__cfg__cli.md#gab513c82ebe434907a958cc6da990bd0b) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Set the target node's network beacon state. |
| int | [bt\_mesh\_cfg\_cli\_ttl\_get](group__bt__mesh__cfg__cli.md#gaa141d4aabbed6c7780ac7f3955c8b580) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ttl) |
|  | Get the target node's Time To Live value. |
| int | [bt\_mesh\_cfg\_cli\_ttl\_set](group__bt__mesh__cfg__cli.md#ga2671234d739c802fd080a19d01235352) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ttl) |
|  | Set the target node's Time To Live value. |
| int | [bt\_mesh\_cfg\_cli\_friend\_get](group__bt__mesh__cfg__cli.md#ga4dd1534e9d5b04fc99231ba5dde23e05) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Get the target node's Friend feature status. |
| int | [bt\_mesh\_cfg\_cli\_friend\_set](group__bt__mesh__cfg__cli.md#gacf8ad783910449c7cdc304c1b9b3fe0b) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Set the target node's Friend feature state. |
| int | [bt\_mesh\_cfg\_cli\_gatt\_proxy\_get](group__bt__mesh__cfg__cli.md#gaaf945377cf6a3d2b3e7c7cdb5a8df016) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Get the target node's Proxy feature state. |
| int | [bt\_mesh\_cfg\_cli\_gatt\_proxy\_set](group__bt__mesh__cfg__cli.md#ga5a717835a416ba2930f65a975265649f) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Set the target node's Proxy feature state. |
| int | [bt\_mesh\_cfg\_cli\_net\_transmit\_get](group__bt__mesh__cfg__cli.md#ga92ee7984b14590ed11a470c0dfea0bc9) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*transmit) |
|  | Get the target node's network\_transmit state. |
| int | [bt\_mesh\_cfg\_cli\_net\_transmit\_set](group__bt__mesh__cfg__cli.md#ga87f7c1e06b5c721c89031c527960bf40) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*transmit) |
|  | Set the target node's network transmit parameters. |
| int | [bt\_mesh\_cfg\_cli\_relay\_get](group__bt__mesh__cfg__cli.md#ga4a50a6a5dcfdc42b7476f0b9e463ea45) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*transmit) |
|  | Get the target node's Relay feature state. |
| int | [bt\_mesh\_cfg\_cli\_relay\_set](group__bt__mesh__cfg__cli.md#ga7fe8418130568bdf2a5e56ed2ad027b0) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_relay, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_transmit, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*transmit) |
|  | Set the target node's Relay parameters. |
| int | [bt\_mesh\_cfg\_cli\_net\_key\_add](group__bt__mesh__cfg__cli.md#ga283fb06ddb6427852ff0ac556d3c1852) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_key[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Add a network key to the target node. |
| int | [bt\_mesh\_cfg\_cli\_net\_key\_get](group__bt__mesh__cfg__cli.md#gab42c5bdff36bea35e967946462b12457) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*keys, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*key\_cnt) |
|  | Get a list of the target node's network key indexes. |
| int | [bt\_mesh\_cfg\_cli\_net\_key\_del](group__bt__mesh__cfg__cli.md#gab2963ec5536cb4b941578bb490fdc013) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Delete a network key from the target node. |
| int | [bt\_mesh\_cfg\_cli\_app\_key\_add](group__bt__mesh__cfg__cli.md#gafabf4c0fa707eba1fd40cc9a403daa07) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_app\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) app\_key[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Add an application key to the target node. |
| int | [bt\_mesh\_cfg\_cli\_app\_key\_get](group__bt__mesh__cfg__cli.md#ga6391ce297ca0be73ccd51044a9e0a76f) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*keys, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*key\_cnt) |
|  | Get a list of the target node's application key indexes for a specific network key. |
| int | [bt\_mesh\_cfg\_cli\_app\_key\_del](group__bt__mesh__cfg__cli.md#ga5140472c687584babf885bc08349c865) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_app\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Delete an application key from the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_app\_bind](group__bt__mesh__cfg__cli.md#gaa4a02dd0c1f67621ee71d011fe4a29c1) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Bind an application to a SIG model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_app\_unbind](group__bt__mesh__cfg__cli.md#gaf82b54a4b2d3176b10daf728272a0977) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Unbind an application from a SIG model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_app\_bind\_vnd](group__bt__mesh__cfg__cli.md#gada33602562721c9f413eb06b34a823a8) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Bind an application to a vendor model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_app\_unbind\_vnd](group__bt__mesh__cfg__cli.md#ga1fb53b9a49be25e633cac9d668c5b209) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Unbind an application from a vendor model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_app\_get](group__bt__mesh__cfg__cli.md#ga67cf5ff993f2444cc66b2ae5353865d2) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*apps, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*app\_cnt) |
|  | Get a list of all applications bound to a SIG model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_app\_get\_vnd](group__bt__mesh__cfg__cli.md#gaf7e0f85bbbbfc382bfe4aea8298227d1) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*apps, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*app\_cnt) |
|  | Get a list of all applications bound to a vendor model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_pub\_get](group__bt__mesh__cfg__cli.md#ga1b36596a20ca8751006b0f7f2221067d) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) \*pub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Get publish parameters for a SIG model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_pub\_get\_vnd](group__bt__mesh__cfg__cli.md#ga0bc2c24403e0cd79a061ba1244b1a1db) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) \*pub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Get publish parameters for a vendor model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_pub\_set](group__bt__mesh__cfg__cli.md#ga7fc2acda16f3f03a929c38796c67028e) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) \*pub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Set publish parameters for a SIG model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_pub\_set\_vnd](group__bt__mesh__cfg__cli.md#gad2c602a2685ff38c0e78c1990b244e54) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) \*pub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Set publish parameters for a vendor model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_add](group__bt__mesh__cfg__cli.md#gaf4ee720ce27eea9602b59a380278bb57) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Add a group address to a SIG model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_add\_vnd](group__bt__mesh__cfg__cli.md#ga3ba34f8be138bc62a7eb7859b18dc441) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Add a group address to a vendor model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_del](group__bt__mesh__cfg__cli.md#ga8d8595f077267b7d784fde30cbc4b207) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Delete a group address in a SIG model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_del\_vnd](group__bt__mesh__cfg__cli.md#ga74bad73184af2d6ce71134831f70680d) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Delete a group address in a vendor model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_overwrite](group__bt__mesh__cfg__cli.md#gadac1cc360c30d290a861bbd534fca58d) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Overwrite all addresses in a SIG model's subscription list with a group address. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_overwrite\_vnd](group__bt__mesh__cfg__cli.md#ga69b2dfacc27ed94b9e1331ff4ac4b582) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Overwrite all addresses in a vendor model's subscription list with a group address. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_va\_add](group__bt__mesh__cfg__cli.md#ga2d22612cf9dc5030699bf7c6c58bf6d5) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) label[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*virt\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Add a virtual address to a SIG model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_va\_add\_vnd](group__bt__mesh__cfg__cli.md#gaa3a10a54a18a99d0b4b0aa85330b1640) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) label[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*virt\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Add a virtual address to a vendor model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_va\_del](group__bt__mesh__cfg__cli.md#gaf7107373fc0c70d091e9a521d8b641ad) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) label[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*virt\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Delete a virtual address in a SIG model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_va\_del\_vnd](group__bt__mesh__cfg__cli.md#ga8884786e3ec349bcb8b89b60aa11f198) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) label[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*virt\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Delete a virtual address in a vendor model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_va\_overwrite](group__bt__mesh__cfg__cli.md#ga69809ad3f2cff8e1f394f6da6ed63264) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) label[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*virt\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Overwrite all addresses in a SIG model's subscription list with a virtual address. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_va\_overwrite\_vnd](group__bt__mesh__cfg__cli.md#ga70d3bb7fb914fa3685f4ad9b561a48b6) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) label[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*virt\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Overwrite all addresses in a vendor model's subscription list with a virtual address. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_get](group__bt__mesh__cfg__cli.md#gaf739e5e3a4b225e10bf2aedf143d7793) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*subs, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*sub\_cnt) |
|  | Get the subscription list of a SIG model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_get\_vnd](group__bt__mesh__cfg__cli.md#ga09e751a9071402ae978c0355edfbdf03) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*subs, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*sub\_cnt) |
|  | Get the subscription list of a vendor model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_hb\_sub\_set](group__bt__mesh__cfg__cli.md#ga1adae658bf8f4512a7d80d0194dcb362) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_cfg\_cli\_hb\_sub](structbt__mesh__cfg__cli__hb__sub.md) \*sub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Set the target node's Heartbeat subscription parameters. |
| int | [bt\_mesh\_cfg\_cli\_hb\_sub\_get](group__bt__mesh__cfg__cli.md#ga86e5de1b216d62b7c77bf43b7af062fc) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_cfg\_cli\_hb\_sub](structbt__mesh__cfg__cli__hb__sub.md) \*sub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Get the target node's Heartbeat subscription parameters. |
| int | [bt\_mesh\_cfg\_cli\_hb\_pub\_set](group__bt__mesh__cfg__cli.md#ga352eb00b78ff978a1a1e81ec5a0575b8) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, const struct [bt\_mesh\_cfg\_cli\_hb\_pub](structbt__mesh__cfg__cli__hb__pub.md) \*pub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Set the target node's Heartbeat publication parameters. |
| int | [bt\_mesh\_cfg\_cli\_hb\_pub\_get](group__bt__mesh__cfg__cli.md#ga07c443476adef9c7bb573ffbb8d1b1ce) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_cfg\_cli\_hb\_pub](structbt__mesh__cfg__cli__hb__pub.md) \*pub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Get the target node's Heartbeat publication parameters. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_del\_all](group__bt__mesh__cfg__cli.md#gacd647905484fa8319a5377aa5777c254) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Delete all group addresses in a SIG model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_del\_all\_vnd](group__bt__mesh__cfg__cli.md#ga2059ccbc689af9c2127e4e399ea5bd43) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Delete all group addresses in a vendor model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_net\_key\_update](group__bt__mesh__cfg__cli.md#gafdaff279685b821a7b205e45feed9a05) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_key[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Update a network key to the target node. |
| int | [bt\_mesh\_cfg\_cli\_app\_key\_update](group__bt__mesh__cfg__cli.md#gacf1bd7a771a45981a82eeea0dcce01b7) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_app\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) app\_key[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Update an application key to the target node. |
| int | [bt\_mesh\_cfg\_cli\_node\_identity\_set](group__bt__mesh__cfg__cli.md#ga12a8618d2b73f30742f8e8d2bdddc138) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_identity, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*identity) |
|  | Set the Node Identity parameters. |
| int | [bt\_mesh\_cfg\_cli\_node\_identity\_get](group__bt__mesh__cfg__cli.md#gac02c170e260980d5b749b581910672d2) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*identity) |
|  | Get the Node Identity parameters. |
| int | [bt\_mesh\_cfg\_cli\_lpn\_timeout\_get](group__bt__mesh__cfg__cli.md#ga0ee1d0849d632b5d806ee31c87bbc888) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) unicast\_addr, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*polltimeout) |
|  | Get the Low Power Node Polltimeout parameters. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [bt\_mesh\_cfg\_cli\_timeout\_get](group__bt__mesh__cfg__cli.md#gaf5262c0a27e4b9249ecf908c259cc7d7) (void) |
|  | Get the current transmission timeout value. |
| void | [bt\_mesh\_cfg\_cli\_timeout\_set](group__bt__mesh__cfg__cli.md#ga7e3521ae973dc825422c6dd5f07ef547) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set the transmission timeout value. |
| int | [bt\_mesh\_comp\_p0\_get](group__bt__mesh__cfg__cli.md#ga1f79d98273a984f1c49b4d5dd5bf8d30) (struct [bt\_mesh\_comp\_p0](structbt__mesh__comp__p0.md) \*comp, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Create a composition data page 0 representation from a buffer. |
| struct [bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md) \* | [bt\_mesh\_comp\_p0\_elem\_pull](group__bt__mesh__cfg__cli.md#gaa6d60ebad6dc4a4f5b022937dbae3120) (const struct [bt\_mesh\_comp\_p0](structbt__mesh__comp__p0.md) \*comp, struct [bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md) \*elem) |
|  | Pull a composition data page 0 element from a composition data page 0 instance. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bt\_mesh\_comp\_p0\_elem\_mod](group__bt__mesh__cfg__cli.md#gac005f52e191c3e5628f063dbc1a19645) (struct [bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md) \*elem, int idx) |
|  | Get a SIG model from the given composition data page 0 element. |
| struct [bt\_mesh\_mod\_id\_vnd](structbt__mesh__mod__id__vnd.md) | [bt\_mesh\_comp\_p0\_elem\_mod\_vnd](group__bt__mesh__cfg__cli.md#ga4f656102982961b7bf2e3d3896a2240e) (struct [bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md) \*elem, int idx) |
|  | Get a vendor model from the given composition data page 0 element. |
| struct [bt\_mesh\_comp\_p1\_elem](structbt__mesh__comp__p1__elem.md) \* | [bt\_mesh\_comp\_p1\_elem\_pull](group__bt__mesh__cfg__cli.md#gae9a19b089d898af914ea5c287aca8fba) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, struct [bt\_mesh\_comp\_p1\_elem](structbt__mesh__comp__p1__elem.md) \*elem) |
|  | Pull a Composition Data Page 1 Element from a composition data page 1 instance. |
| struct [bt\_mesh\_comp\_p1\_model\_item](structbt__mesh__comp__p1__model__item.md) \* | [bt\_mesh\_comp\_p1\_item\_pull](group__bt__mesh__cfg__cli.md#gac8b4b670c82b80a51834f7ef32206985) (struct [bt\_mesh\_comp\_p1\_elem](structbt__mesh__comp__p1__elem.md) \*elem, struct [bt\_mesh\_comp\_p1\_model\_item](structbt__mesh__comp__p1__model__item.md) \*item) |
|  | Pull a Composition Data Page 1 Model Item from a Composition Data Page 1 Element. |
| struct [bt\_mesh\_comp\_p1\_ext\_item](structbt__mesh__comp__p1__ext__item.md) \* | [bt\_mesh\_comp\_p1\_pull\_ext\_item](group__bt__mesh__cfg__cli.md#gac527fe27308c8a61ac1831af9605e429) (struct [bt\_mesh\_comp\_p1\_model\_item](structbt__mesh__comp__p1__model__item.md) \*item, struct [bt\_mesh\_comp\_p1\_ext\_item](structbt__mesh__comp__p1__ext__item.md) \*ext\_item) |
|  | Pull Extended Model Item contained in Model Item. |
| struct [bt\_mesh\_comp\_p2\_record](structbt__mesh__comp__p2__record.md) \* | [bt\_mesh\_comp\_p2\_record\_pull](group__bt__mesh__cfg__cli.md#ga0854a494707a40b84beb8582f45e0470) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, struct [bt\_mesh\_comp\_p2\_record](structbt__mesh__comp__p2__record.md) \*record) |
|  | Pull a Composition Data Page 2 Record from a composition data page 2 instance. |
| int | [bt\_mesh\_key\_idx\_unpack\_list](group__bt__mesh__cfg__cli.md#gaa411ab7db2e71a114a8108eaec9ca12c) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dst\_arr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*dst\_cnt) |
|  | Unpack a list of key index entries from a buffer. |

## Detailed Description

Configuration Client Model APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [cfg\_cli.h](cfg__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
