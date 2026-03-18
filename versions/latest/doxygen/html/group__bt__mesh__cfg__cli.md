---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bt__mesh__cfg__cli.html
original_path: doxygen/html/group__bt__mesh__cfg__cli.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Configuration Client Model

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

Configuration Client Model.
[More...](#details)

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
| #define | [BT\_MESH\_MODEL\_CFG\_CLI](#ga2f0df6906a27ebbd86dcd11951114001)(cli\_data) |
|  | Generic Configuration Client model composition data entry. |
| #define | [BT\_MESH\_PUB\_PERIOD\_100MS](#gab542c707fb5bad0a15088fefda775a42)(steps) |
|  | Helper macro to encode model publication period in units of 100ms. |
| #define | [BT\_MESH\_PUB\_PERIOD\_SEC](#ga29435e527a73ff6e19339b773c8eb79e)(steps) |
|  | Helper macro to encode model publication period in units of 1 second. |
| #define | [BT\_MESH\_PUB\_PERIOD\_10SEC](#ga654204077adaa08259d1afbfe92e070e)(steps) |
|  | Helper macro to encode model publication period in units of 10 seconds. |
| #define | [BT\_MESH\_PUB\_PERIOD\_10MIN](#ga36c37f644ee39ad91b6167f68c806b7e)(steps) |
|  | Helper macro to encode model publication period in units of 10 minutes. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_cfg\_cli\_node\_reset](#gac6675d227749a69cedc5455c70626b76) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*status) |
|  | Reset the target node and remove it from the network. |
| int | [bt\_mesh\_cfg\_cli\_comp\_data\_get](#ga36259e9c811a8f1a21d642739cf297df) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) page, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rsp, struct [net\_buf\_simple](structnet__buf__simple.md) \*comp) |
|  | Get the target node's composition data. |
| int | [bt\_mesh\_cfg\_cli\_beacon\_get](#ga2c8a79d1b70e91e0a09c848737bb4a22) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Get the target node's network beacon state. |
| int | [bt\_mesh\_cfg\_cli\_krp\_get](#ga660df68049110332ff21610fe4e520c6) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*phase) |
|  | Get the target node's network key refresh phase state. |
| int | [bt\_mesh\_cfg\_cli\_krp\_set](#gae51eee59090cfebed4561ed3bb4df005) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) transition, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*phase) |
|  | Set the target node's network key refresh phase parameters. |
| int | [bt\_mesh\_cfg\_cli\_beacon\_set](#gab513c82ebe434907a958cc6da990bd0b) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Set the target node's network beacon state. |
| int | [bt\_mesh\_cfg\_cli\_ttl\_get](#gaa141d4aabbed6c7780ac7f3955c8b580) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ttl) |
|  | Get the target node's Time To Live value. |
| int | [bt\_mesh\_cfg\_cli\_ttl\_set](#ga2671234d739c802fd080a19d01235352) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*ttl) |
|  | Set the target node's Time To Live value. |
| int | [bt\_mesh\_cfg\_cli\_friend\_get](#ga4dd1534e9d5b04fc99231ba5dde23e05) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Get the target node's Friend feature status. |
| int | [bt\_mesh\_cfg\_cli\_friend\_set](#gacf8ad783910449c7cdc304c1b9b3fe0b) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Set the target node's Friend feature state. |
| int | [bt\_mesh\_cfg\_cli\_gatt\_proxy\_get](#gaaf945377cf6a3d2b3e7c7cdb5a8df016) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Get the target node's Proxy feature state. |
| int | [bt\_mesh\_cfg\_cli\_gatt\_proxy\_set](#ga5a717835a416ba2930f65a975265649f) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Set the target node's Proxy feature state. |
| int | [bt\_mesh\_cfg\_cli\_net\_transmit\_get](#ga92ee7984b14590ed11a470c0dfea0bc9) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*transmit) |
|  | Get the target node's network\_transmit state. |
| int | [bt\_mesh\_cfg\_cli\_net\_transmit\_set](#ga87f7c1e06b5c721c89031c527960bf40) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*transmit) |
|  | Set the target node's network transmit parameters. |
| int | [bt\_mesh\_cfg\_cli\_relay\_get](#ga4a50a6a5dcfdc42b7476f0b9e463ea45) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*transmit) |
|  | Get the target node's Relay feature state. |
| int | [bt\_mesh\_cfg\_cli\_relay\_set](#ga7fe8418130568bdf2a5e56ed2ad027b0) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_relay, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_transmit, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*transmit) |
|  | Set the target node's Relay parameters. |
| int | [bt\_mesh\_cfg\_cli\_net\_key\_add](#ga283fb06ddb6427852ff0ac556d3c1852) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_key[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Add a network key to the target node. |
| int | [bt\_mesh\_cfg\_cli\_net\_key\_get](#gab42c5bdff36bea35e967946462b12457) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*keys, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*key\_cnt) |
|  | Get a list of the target node's network key indexes. |
| int | [bt\_mesh\_cfg\_cli\_net\_key\_del](#gab2963ec5536cb4b941578bb490fdc013) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Delete a network key from the target node. |
| int | [bt\_mesh\_cfg\_cli\_app\_key\_add](#gafabf4c0fa707eba1fd40cc9a403daa07) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_app\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) app\_key[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Add an application key to the target node. |
| int | [bt\_mesh\_cfg\_cli\_app\_key\_get](#ga6391ce297ca0be73ccd51044a9e0a76f) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*keys, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*key\_cnt) |
|  | Get a list of the target node's application key indexes for a specific network key. |
| int | [bt\_mesh\_cfg\_cli\_app\_key\_del](#ga5140472c687584babf885bc08349c865) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_app\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Delete an application key from the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_app\_bind](#gaa4a02dd0c1f67621ee71d011fe4a29c1) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Bind an application to a SIG model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_app\_unbind](#gaf82b54a4b2d3176b10daf728272a0977) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Unbind an application from a SIG model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_app\_bind\_vnd](#gada33602562721c9f413eb06b34a823a8) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Bind an application to a vendor model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_app\_unbind\_vnd](#ga1fb53b9a49be25e633cac9d668c5b209) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Unbind an application from a vendor model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_app\_get](#ga67cf5ff993f2444cc66b2ae5353865d2) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*apps, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*app\_cnt) |
|  | Get a list of all applications bound to a SIG model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_app\_get\_vnd](#gaf7e0f85bbbbfc382bfe4aea8298227d1) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*apps, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*app\_cnt) |
|  | Get a list of all applications bound to a vendor model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_pub\_get](#ga1b36596a20ca8751006b0f7f2221067d) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) \*pub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Get publish parameters for a SIG model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_pub\_get\_vnd](#ga0bc2c24403e0cd79a061ba1244b1a1db) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) \*pub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Get publish parameters for a vendor model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_pub\_set](#ga7fc2acda16f3f03a929c38796c67028e) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) \*pub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Set publish parameters for a SIG model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_pub\_set\_vnd](#gad2c602a2685ff38c0e78c1990b244e54) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) \*pub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Set publish parameters for a vendor model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_add](#gaf4ee720ce27eea9602b59a380278bb57) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Add a group address to a SIG model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_add\_vnd](#ga3ba34f8be138bc62a7eb7859b18dc441) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Add a group address to a vendor model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_del](#ga8d8595f077267b7d784fde30cbc4b207) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Delete a group address in a SIG model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_del\_vnd](#ga74bad73184af2d6ce71134831f70680d) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Delete a group address in a vendor model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_overwrite](#gadac1cc360c30d290a861bbd534fca58d) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Overwrite all addresses in a SIG model's subscription list with a group address. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_overwrite\_vnd](#ga69b2dfacc27ed94b9e1331ff4ac4b582) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sub\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Overwrite all addresses in a vendor model's subscription list with a group address. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_va\_add](#ga2d22612cf9dc5030699bf7c6c58bf6d5) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) label[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*virt\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Add a virtual address to a SIG model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_va\_add\_vnd](#gaa3a10a54a18a99d0b4b0aa85330b1640) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) label[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*virt\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Add a virtual address to a vendor model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_va\_del](#gaf7107373fc0c70d091e9a521d8b641ad) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) label[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*virt\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Delete a virtual address in a SIG model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_va\_del\_vnd](#ga8884786e3ec349bcb8b89b60aa11f198) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) label[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*virt\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Delete a virtual address in a vendor model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_va\_overwrite](#ga69809ad3f2cff8e1f394f6da6ed63264) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) label[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*virt\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Overwrite all addresses in a SIG model's subscription list with a virtual address. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_va\_overwrite\_vnd](#ga70d3bb7fb914fa3685f4ad9b561a48b6) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) label[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*virt\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Overwrite all addresses in a vendor model's subscription list with a virtual address. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_get](#gaf739e5e3a4b225e10bf2aedf143d7793) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*subs, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*sub\_cnt) |
|  | Get the subscription list of a SIG model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_get\_vnd](#ga09e751a9071402ae978c0355edfbdf03) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*subs, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*sub\_cnt) |
|  | Get the subscription list of a vendor model on the target node. |
| int | [bt\_mesh\_cfg\_cli\_hb\_sub\_set](#ga1adae658bf8f4512a7d80d0194dcb362) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_cfg\_cli\_hb\_sub](structbt__mesh__cfg__cli__hb__sub.md) \*sub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Set the target node's Heartbeat subscription parameters. |
| int | [bt\_mesh\_cfg\_cli\_hb\_sub\_get](#ga86e5de1b216d62b7c77bf43b7af062fc) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_cfg\_cli\_hb\_sub](structbt__mesh__cfg__cli__hb__sub.md) \*sub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Get the target node's Heartbeat subscription parameters. |
| int | [bt\_mesh\_cfg\_cli\_hb\_pub\_set](#ga352eb00b78ff978a1a1e81ec5a0575b8) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, const struct [bt\_mesh\_cfg\_cli\_hb\_pub](structbt__mesh__cfg__cli__hb__pub.md) \*pub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Set the target node's Heartbeat publication parameters. |
| int | [bt\_mesh\_cfg\_cli\_hb\_pub\_get](#ga07c443476adef9c7bb573ffbb8d1b1ce) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_cfg\_cli\_hb\_pub](structbt__mesh__cfg__cli__hb__pub.md) \*pub, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Get the target node's Heartbeat publication parameters. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_del\_all](#gacd647905484fa8319a5377aa5777c254) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Delete all group addresses in a SIG model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_mod\_sub\_del\_all\_vnd](#ga2059ccbc689af9c2127e4e399ea5bd43) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) elem\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mod\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cid, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Delete all group addresses in a vendor model's subscription list. |
| int | [bt\_mesh\_cfg\_cli\_net\_key\_update](#gafdaff279685b821a7b205e45feed9a05) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_key[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Update a network key to the target node. |
| int | [bt\_mesh\_cfg\_cli\_app\_key\_update](#gacf1bd7a771a45981a82eeea0dcce01b7) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_app\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) app\_key[16], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status) |
|  | Update an application key to the target node. |
| int | [bt\_mesh\_cfg\_cli\_node\_identity\_set](#ga12a8618d2b73f30742f8e8d2bdddc138) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) new\_identity, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*identity) |
|  | Set the Node Identity parameters. |
| int | [bt\_mesh\_cfg\_cli\_node\_identity\_get](#gac02c170e260980d5b749b581910672d2) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) key\_net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*status, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*identity) |
|  | Get the Node Identity parameters. |
| int | [bt\_mesh\_cfg\_cli\_lpn\_timeout\_get](#ga0ee1d0849d632b5d806ee31c87bbc888) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) unicast\_addr, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*polltimeout) |
|  | Get the Low Power Node Polltimeout parameters. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [bt\_mesh\_cfg\_cli\_timeout\_get](#gaf5262c0a27e4b9249ecf908c259cc7d7) (void) |
|  | Get the current transmission timeout value. |
| void | [bt\_mesh\_cfg\_cli\_timeout\_set](#ga7e3521ae973dc825422c6dd5f07ef547) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set the transmission timeout value. |
| int | [bt\_mesh\_comp\_p0\_get](#ga1f79d98273a984f1c49b4d5dd5bf8d30) (struct [bt\_mesh\_comp\_p0](structbt__mesh__comp__p0.md) \*comp, struct [net\_buf\_simple](structnet__buf__simple.md) \*buf) |
|  | Create a composition data page 0 representation from a buffer. |
| struct [bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md) \* | [bt\_mesh\_comp\_p0\_elem\_pull](#gaa6d60ebad6dc4a4f5b022937dbae3120) (const struct [bt\_mesh\_comp\_p0](structbt__mesh__comp__p0.md) \*comp, struct [bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md) \*elem) |
|  | Pull a composition data page 0 element from a composition data page 0 instance. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bt\_mesh\_comp\_p0\_elem\_mod](#gac005f52e191c3e5628f063dbc1a19645) (struct [bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md) \*elem, int idx) |
|  | Get a SIG model from the given composition data page 0 element. |
| struct [bt\_mesh\_mod\_id\_vnd](structbt__mesh__mod__id__vnd.md) | [bt\_mesh\_comp\_p0\_elem\_mod\_vnd](#ga4f656102982961b7bf2e3d3896a2240e) (struct [bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md) \*elem, int idx) |
|  | Get a vendor model from the given composition data page 0 element. |
| struct [bt\_mesh\_comp\_p1\_elem](structbt__mesh__comp__p1__elem.md) \* | [bt\_mesh\_comp\_p1\_elem\_pull](#gae9a19b089d898af914ea5c287aca8fba) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, struct [bt\_mesh\_comp\_p1\_elem](structbt__mesh__comp__p1__elem.md) \*elem) |
|  | Pull a Composition Data Page 1 Element from a composition data page 1 instance. |
| struct [bt\_mesh\_comp\_p1\_model\_item](structbt__mesh__comp__p1__model__item.md) \* | [bt\_mesh\_comp\_p1\_item\_pull](#gac8b4b670c82b80a51834f7ef32206985) (struct [bt\_mesh\_comp\_p1\_elem](structbt__mesh__comp__p1__elem.md) \*elem, struct [bt\_mesh\_comp\_p1\_model\_item](structbt__mesh__comp__p1__model__item.md) \*item) |
|  | Pull a Composition Data Page 1 Model Item from a Composition Data Page 1 Element. |
| struct [bt\_mesh\_comp\_p1\_ext\_item](structbt__mesh__comp__p1__ext__item.md) \* | [bt\_mesh\_comp\_p1\_pull\_ext\_item](#gac527fe27308c8a61ac1831af9605e429) (struct [bt\_mesh\_comp\_p1\_model\_item](structbt__mesh__comp__p1__model__item.md) \*item, struct [bt\_mesh\_comp\_p1\_ext\_item](structbt__mesh__comp__p1__ext__item.md) \*ext\_item) |
|  | Pull Extended Model Item contained in Model Item. |
| struct [bt\_mesh\_comp\_p2\_record](structbt__mesh__comp__p2__record.md) \* | [bt\_mesh\_comp\_p2\_record\_pull](#ga0854a494707a40b84beb8582f45e0470) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, struct [bt\_mesh\_comp\_p2\_record](structbt__mesh__comp__p2__record.md) \*record) |
|  | Pull a Composition Data Page 2 Record from a composition data page 2 instance. |
| int | [bt\_mesh\_key\_idx\_unpack\_list](#gaa411ab7db2e71a114a8108eaec9ca12c) (struct [net\_buf\_simple](structnet__buf__simple.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*dst\_arr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*dst\_cnt) |
|  | Unpack a list of key index entries from a buffer. |

## Detailed Description

Configuration Client Model.

## Macro Definition Documentation

## [◆ ](#ga2f0df6906a27ebbd86dcd11951114001)BT\_MESH\_MODEL\_CFG\_CLI

| #define BT\_MESH\_MODEL\_CFG\_CLI | ( |  | *cli\_data* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CNT\_CB](group__bt__mesh__access.md#ga925da443eb15a4c1980d48a69388dc2c)([BT\_MESH\_MODEL\_ID\_CFG\_CLI](group__bt__mesh__access.md#ga3f8442dcd1a110ea0d0023f50057139f), \

bt\_mesh\_cfg\_cli\_op, NULL, \

cli\_data, 1, 0, &[bt\_mesh\_cfg\_cli\_cb](structbt__mesh__cfg__cli__cb.md))

[BT\_MESH\_MODEL\_ID\_CFG\_CLI](group__bt__mesh__access.md#ga3f8442dcd1a110ea0d0023f50057139f)

#define BT\_MESH\_MODEL\_ID\_CFG\_CLI

Configuration Client.

**Definition** access.h:181

[BT\_MESH\_MODEL\_CNT\_CB](group__bt__mesh__access.md#ga925da443eb15a4c1980d48a69388dc2c)

#define BT\_MESH\_MODEL\_CNT\_CB(\_id, \_op, \_pub, \_user\_data, \_keys, \_grps, \_cb)

Composition data SIG model entry with callback functions with specific number of keys & groups.

**Definition** access.h:432

[bt\_mesh\_cfg\_cli\_cb](structbt__mesh__cfg__cli__cb.md)

Mesh Configuration Client Status messages callback.

**Definition** cfg\_cli.h:33

Generic Configuration Client model composition data entry.

Parameters
:   | cli\_data | Pointer to a [Configuration Client Model](group__bt__mesh__cfg__cli.md "Configuration Client Model") instance. |
    | --- | --- |

## [◆ ](#gab542c707fb5bad0a15088fefda775a42)BT\_MESH\_PUB\_PERIOD\_100MS

| #define BT\_MESH\_PUB\_PERIOD\_100MS | ( |  | *steps* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

**Value:**

((steps) & [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(6))

[BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)

#define BIT\_MASK(n)

**Definition** adc.h:14

Helper macro to encode model publication period in units of 100ms.

Parameters
:   | steps | Number of 100ms steps. |
    | --- | --- |

Returns
:   Encoded value that can be assigned to [bt\_mesh\_cfg\_cli\_mod\_pub.period](structbt__mesh__cfg__cli__mod__pub.md#a104afe2b8d9766e037293b09c0c1b91c "Encoded publish period.")

## [◆ ](#ga36c37f644ee39ad91b6167f68c806b7e)BT\_MESH\_PUB\_PERIOD\_10MIN

| #define BT\_MESH\_PUB\_PERIOD\_10MIN | ( |  | *steps* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

**Value:**

(((steps) & [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(6)) | (3 << 6))

Helper macro to encode model publication period in units of 10 minutes.

Parameters
:   | steps | Number of 10 minute steps. |
    | --- | --- |

Returns
:   Encoded value that can be assigned to [bt\_mesh\_cfg\_cli\_mod\_pub.period](structbt__mesh__cfg__cli__mod__pub.md#a104afe2b8d9766e037293b09c0c1b91c "Encoded publish period.")

## [◆ ](#ga654204077adaa08259d1afbfe92e070e)BT\_MESH\_PUB\_PERIOD\_10SEC

| #define BT\_MESH\_PUB\_PERIOD\_10SEC | ( |  | *steps* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

**Value:**

(((steps) & [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(6)) | (2 << 6))

Helper macro to encode model publication period in units of 10 seconds.

Parameters
:   | steps | Number of 10 second steps. |
    | --- | --- |

Returns
:   Encoded value that can be assigned to [bt\_mesh\_cfg\_cli\_mod\_pub.period](structbt__mesh__cfg__cli__mod__pub.md#a104afe2b8d9766e037293b09c0c1b91c "Encoded publish period.")

## [◆ ](#ga29435e527a73ff6e19339b773c8eb79e)BT\_MESH\_PUB\_PERIOD\_SEC

| #define BT\_MESH\_PUB\_PERIOD\_SEC | ( |  | *steps* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

**Value:**

(((steps) & [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(6)) | (1 << 6))

Helper macro to encode model publication period in units of 1 second.

Parameters
:   | steps | Number of 1 second steps. |
    | --- | --- |

Returns
:   Encoded value that can be assigned to [bt\_mesh\_cfg\_cli\_mod\_pub.period](structbt__mesh__cfg__cli__mod__pub.md#a104afe2b8d9766e037293b09c0c1b91c "Encoded publish period.")

## Function Documentation

## [◆ ](#gafabf4c0fa707eba1fd40cc9a403daa07)bt\_mesh\_cfg\_cli\_app\_key\_add()

| int bt\_mesh\_cfg\_cli\_app\_key\_add | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *key\_net\_idx*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *key\_app\_idx*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *app\_key*[16], |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Add an application key to the target node.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | key\_net\_idx | Network key index the application key belongs to. |
    | key\_app\_idx | Application key index. |
    | app\_key | Application key. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga5140472c687584babf885bc08349c865)bt\_mesh\_cfg\_cli\_app\_key\_del()

| int bt\_mesh\_cfg\_cli\_app\_key\_del | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *key\_net\_idx*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *key\_app\_idx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Delete an application key from the target node.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | key\_net\_idx | Network key index the application key belongs to. |
    | key\_app\_idx | Application key index. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga6391ce297ca0be73ccd51044a9e0a76f)bt\_mesh\_cfg\_cli\_app\_key\_get()

| int bt\_mesh\_cfg\_cli\_app\_key\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *key\_net\_idx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *keys*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *key\_cnt* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get a list of the target node's application key indexes for a specific network key.

This method can be used asynchronously by setting `status` and ( `keys` or `key_cnt` ) as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | key\_net\_idx | Network key index to request the app key indexes of. |
    | status | Status response parameter. |
    | keys | App key index list response parameter. Will be filled with all the returned application key indexes it can fill. |
    | key\_cnt | App key index list length. Should be set to the capacity of the `keys` list when calling. Will return the number of returned application key indexes upon success. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gacf1bd7a771a45981a82eeea0dcce01b7)bt\_mesh\_cfg\_cli\_app\_key\_update()

| int bt\_mesh\_cfg\_cli\_app\_key\_update | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *key\_net\_idx*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *key\_app\_idx*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *app\_key*[16], |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Update an application key to the target node.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | key\_net\_idx | Network key index the application key belongs to. |
    | key\_app\_idx | Application key index. |
    | app\_key | Application key. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga2c8a79d1b70e91e0a09c848737bb4a22)bt\_mesh\_cfg\_cli\_beacon\_get()

| int bt\_mesh\_cfg\_cli\_beacon\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get the target node's network beacon state.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | status | Status response parameter, returns one of [BT\_MESH\_BEACON\_DISABLED](group__bt__mesh__cfg.md#ga8fa3d0ac3cb9f69464c4068ca61689b9 "BT_MESH_BEACON_DISABLED") or [BT\_MESH\_BEACON\_ENABLED](group__bt__mesh__cfg.md#ga01235217559423b93d7e6cf2236278f0 "BT_MESH_BEACON_ENABLED") on success. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gab513c82ebe434907a958cc6da990bd0b)bt\_mesh\_cfg\_cli\_beacon\_set()

| int bt\_mesh\_cfg\_cli\_beacon\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *val*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Set the target node's network beacon state.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | val | New network beacon state, should be one of [BT\_MESH\_BEACON\_DISABLED](group__bt__mesh__cfg.md#ga8fa3d0ac3cb9f69464c4068ca61689b9 "BT_MESH_BEACON_DISABLED") or [BT\_MESH\_BEACON\_ENABLED](group__bt__mesh__cfg.md#ga01235217559423b93d7e6cf2236278f0 "BT_MESH_BEACON_ENABLED"). |
    | status | Status response parameter. Returns one of [BT\_MESH\_BEACON\_DISABLED](group__bt__mesh__cfg.md#ga8fa3d0ac3cb9f69464c4068ca61689b9 "BT_MESH_BEACON_DISABLED") or [BT\_MESH\_BEACON\_ENABLED](group__bt__mesh__cfg.md#ga01235217559423b93d7e6cf2236278f0 "BT_MESH_BEACON_ENABLED") on success. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga36259e9c811a8f1a21d642739cf297df)bt\_mesh\_cfg\_cli\_comp\_data\_get()

| int bt\_mesh\_cfg\_cli\_comp\_data\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *page*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *rsp*, |
|  |  | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *comp* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get the target node's composition data.

If the other device does not have the given composition data page, it will return the largest page number it supports that is less than the requested page index. The actual page the device responds with is returned in `rsp`.

This method can be used asynchronously by setting `rsp` and `comp` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | page | Composition data page, or 0xff to request the first available page. |
    | rsp | Return parameter for the returned page number, or NULL. |
    | comp | Composition data buffer to fill. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga4dd1534e9d5b04fc99231ba5dde23e05)bt\_mesh\_cfg\_cli\_friend\_get()

| int bt\_mesh\_cfg\_cli\_friend\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get the target node's Friend feature status.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | status | Status response parameter. Returns one of [BT\_MESH\_FRIEND\_DISABLED](group__bt__mesh__cfg.md#ga29fe48989e760438f2c5241110134c8c "BT_MESH_FRIEND_DISABLED"), [BT\_MESH\_FRIEND\_ENABLED](group__bt__mesh__cfg.md#gaa23bba212dc1b322651723ca20f497a3 "BT_MESH_FRIEND_ENABLED") or [BT\_MESH\_FRIEND\_NOT\_SUPPORTED](group__bt__mesh__cfg.md#ga35f85e6a9c085cdad4f70b8e60d0b027 "BT_MESH_FRIEND_NOT_SUPPORTED") on success. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gacf8ad783910449c7cdc304c1b9b3fe0b)bt\_mesh\_cfg\_cli\_friend\_set()

| int bt\_mesh\_cfg\_cli\_friend\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *val*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Set the target node's Friend feature state.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | val | New Friend feature state. Should be one of [BT\_MESH\_FRIEND\_DISABLED](group__bt__mesh__cfg.md#ga29fe48989e760438f2c5241110134c8c "BT_MESH_FRIEND_DISABLED") or [BT\_MESH\_FRIEND\_ENABLED](group__bt__mesh__cfg.md#gaa23bba212dc1b322651723ca20f497a3 "BT_MESH_FRIEND_ENABLED"). |
    | status | Status response parameter. Returns one of [BT\_MESH\_FRIEND\_DISABLED](group__bt__mesh__cfg.md#ga29fe48989e760438f2c5241110134c8c "BT_MESH_FRIEND_DISABLED"), [BT\_MESH\_FRIEND\_ENABLED](group__bt__mesh__cfg.md#gaa23bba212dc1b322651723ca20f497a3 "BT_MESH_FRIEND_ENABLED") or [BT\_MESH\_FRIEND\_NOT\_SUPPORTED](group__bt__mesh__cfg.md#ga35f85e6a9c085cdad4f70b8e60d0b027 "BT_MESH_FRIEND_NOT_SUPPORTED") on success. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gaaf945377cf6a3d2b3e7c7cdb5a8df016)bt\_mesh\_cfg\_cli\_gatt\_proxy\_get()

| int bt\_mesh\_cfg\_cli\_gatt\_proxy\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get the target node's Proxy feature state.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | status | Status response parameter. Returns one of [BT\_MESH\_GATT\_PROXY\_DISABLED](group__bt__mesh__cfg.md#ga3fe3e68efd25a3a03a041b978435fd7b "BT_MESH_GATT_PROXY_DISABLED"), [BT\_MESH\_GATT\_PROXY\_ENABLED](group__bt__mesh__cfg.md#ga77f4438624aae49ea2bb66437c9623f7 "BT_MESH_GATT_PROXY_ENABLED") or [BT\_MESH\_GATT\_PROXY\_NOT\_SUPPORTED](group__bt__mesh__cfg.md#gaecec3747198a29dd10185e3755e660f8 "BT_MESH_GATT_PROXY_NOT_SUPPORTED") on success. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga5a717835a416ba2930f65a975265649f)bt\_mesh\_cfg\_cli\_gatt\_proxy\_set()

| int bt\_mesh\_cfg\_cli\_gatt\_proxy\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *val*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Set the target node's Proxy feature state.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | val | New Proxy feature state. Must be one of [BT\_MESH\_GATT\_PROXY\_DISABLED](group__bt__mesh__cfg.md#ga3fe3e68efd25a3a03a041b978435fd7b "BT_MESH_GATT_PROXY_DISABLED") or [BT\_MESH\_GATT\_PROXY\_ENABLED](group__bt__mesh__cfg.md#ga77f4438624aae49ea2bb66437c9623f7 "BT_MESH_GATT_PROXY_ENABLED"). |
    | status | Status response parameter. Returns one of [BT\_MESH\_GATT\_PROXY\_DISABLED](group__bt__mesh__cfg.md#ga3fe3e68efd25a3a03a041b978435fd7b "BT_MESH_GATT_PROXY_DISABLED"), [BT\_MESH\_GATT\_PROXY\_ENABLED](group__bt__mesh__cfg.md#ga77f4438624aae49ea2bb66437c9623f7 "BT_MESH_GATT_PROXY_ENABLED") or [BT\_MESH\_GATT\_PROXY\_NOT\_SUPPORTED](group__bt__mesh__cfg.md#gaecec3747198a29dd10185e3755e660f8 "BT_MESH_GATT_PROXY_NOT_SUPPORTED") on success. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga07c443476adef9c7bb573ffbb8d1b1ce)bt\_mesh\_cfg\_cli\_hb\_pub\_get()

| int bt\_mesh\_cfg\_cli\_hb\_pub\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | struct [bt\_mesh\_cfg\_cli\_hb\_pub](structbt__mesh__cfg__cli__hb__pub.md) \* | *pub*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get the target node's Heartbeat publication parameters.

This method can be used asynchronously by setting `status` and `pub` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | pub | Heartbeat publication parameter return buffer. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga352eb00b78ff978a1a1e81ec5a0575b8)bt\_mesh\_cfg\_cli\_hb\_pub\_set()

| int bt\_mesh\_cfg\_cli\_hb\_pub\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | const struct [bt\_mesh\_cfg\_cli\_hb\_pub](structbt__mesh__cfg__cli__hb__pub.md) \* | *pub*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Set the target node's Heartbeat publication parameters.

Note
:   The target node must already have received the specified network key.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

`pub` shall not be NULL;

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | pub | New Heartbeat publication parameters. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga86e5de1b216d62b7c77bf43b7af062fc)bt\_mesh\_cfg\_cli\_hb\_sub\_get()

| int bt\_mesh\_cfg\_cli\_hb\_sub\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | struct [bt\_mesh\_cfg\_cli\_hb\_sub](structbt__mesh__cfg__cli__hb__sub.md) \* | *sub*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get the target node's Heartbeat subscription parameters.

This method can be used asynchronously by setting `status` and `sub` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | sub | Heartbeat subscription parameter return buffer. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga1adae658bf8f4512a7d80d0194dcb362)bt\_mesh\_cfg\_cli\_hb\_sub\_set()

| int bt\_mesh\_cfg\_cli\_hb\_sub\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | struct [bt\_mesh\_cfg\_cli\_hb\_sub](structbt__mesh__cfg__cli__hb__sub.md) \* | *sub*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Set the target node's Heartbeat subscription parameters.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

`sub` shall not be null.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | sub | New Heartbeat subscription parameters. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga660df68049110332ff21610fe4e520c6)bt\_mesh\_cfg\_cli\_krp\_get()

| int bt\_mesh\_cfg\_cli\_krp\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *key\_net\_idx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *phase* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get the target node's network key refresh phase state.

This method can be used asynchronously by setting `status` and `phase` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | key\_net\_idx | Network key index. |
    | status | Status response parameter. |
    | phase | Pointer to the Key Refresh variable to fill. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gae51eee59090cfebed4561ed3bb4df005)bt\_mesh\_cfg\_cli\_krp\_set()

| int bt\_mesh\_cfg\_cli\_krp\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *key\_net\_idx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *transition*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *phase* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Set the target node's network key refresh phase parameters.

This method can be used asynchronously by setting `status` and `phase` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | key\_net\_idx | Network key index. |
    | transition | Transition parameter. |
    | status | Status response parameter. |
    | phase | Pointer to the new Key Refresh phase. Will return the actual Key Refresh phase after updating. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga0ee1d0849d632b5d806ee31c87bbc888)bt\_mesh\_cfg\_cli\_lpn\_timeout\_get()

| int bt\_mesh\_cfg\_cli\_lpn\_timeout\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *unicast\_addr*, |
|  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \* | *polltimeout* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get the Low Power Node Polltimeout parameters.

This method can be used asynchronously by setting `polltimeout` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | unicast\_addr | LPN unicast address. |
    | polltimeout | Poll timeout response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gaa4a02dd0c1f67621ee71d011fe4a29c1)bt\_mesh\_cfg\_cli\_mod\_app\_bind()

| int bt\_mesh\_cfg\_cli\_mod\_app\_bind | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_app\_idx*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Bind an application to a SIG model on the target node.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | mod\_app\_idx | Application index to bind. |
    | mod\_id | Model ID. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gada33602562721c9f413eb06b34a823a8)bt\_mesh\_cfg\_cli\_mod\_app\_bind\_vnd()

| int bt\_mesh\_cfg\_cli\_mod\_app\_bind\_vnd | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_app\_idx*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cid*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Bind an application to a vendor model on the target node.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | mod\_app\_idx | Application index to bind. |
    | mod\_id | Model ID. |
    | cid | Company ID of the model. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga67cf5ff993f2444cc66b2ae5353865d2)bt\_mesh\_cfg\_cli\_mod\_app\_get()

| int bt\_mesh\_cfg\_cli\_mod\_app\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *apps*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *app\_cnt* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get a list of all applications bound to a SIG model on the target node.

This method can be used asynchronously by setting `status` and ( `apps` or `app_cnt` ) as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | mod\_id | Model ID. |
    | status | Status response parameter. |
    | apps | App index list response parameter. Will be filled with all the returned application key indexes it can fill. |
    | app\_cnt | App index list length. Should be set to the capacity of the `apps` list when calling. Will return the number of returned application key indexes upon success. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gaf7e0f85bbbbfc382bfe4aea8298227d1)bt\_mesh\_cfg\_cli\_mod\_app\_get\_vnd()

| int bt\_mesh\_cfg\_cli\_mod\_app\_get\_vnd | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cid*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *apps*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *app\_cnt* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get a list of all applications bound to a vendor model on the target node.

This method can be used asynchronously by setting `status` and ( `apps` or `app_cnt` ) as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | mod\_id | Model ID. |
    | cid | Company ID of the model. |
    | status | Status response parameter. |
    | apps | App index list response parameter. Will be filled with all the returned application key indexes it can fill. |
    | app\_cnt | App index list length. Should be set to the capacity of the `apps` list when calling. Will return the number of returned application key indexes upon success. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gaf82b54a4b2d3176b10daf728272a0977)bt\_mesh\_cfg\_cli\_mod\_app\_unbind()

| int bt\_mesh\_cfg\_cli\_mod\_app\_unbind | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_app\_idx*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Unbind an application from a SIG model on the target node.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | mod\_app\_idx | Application index to unbind. |
    | mod\_id | Model ID. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga1fb53b9a49be25e633cac9d668c5b209)bt\_mesh\_cfg\_cli\_mod\_app\_unbind\_vnd()

| int bt\_mesh\_cfg\_cli\_mod\_app\_unbind\_vnd | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_app\_idx*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cid*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Unbind an application from a vendor model on the target node.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | mod\_app\_idx | Application index to unbind. |
    | mod\_id | Model ID. |
    | cid | Company ID of the model. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga1b36596a20ca8751006b0f7f2221067d)bt\_mesh\_cfg\_cli\_mod\_pub\_get()

| int bt\_mesh\_cfg\_cli\_mod\_pub\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) \* | *pub*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get publish parameters for a SIG model on the target node.

This method can be used asynchronously by setting `status` and `pub` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | mod\_id | Model ID. |
    | pub | Publication parameter return buffer. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga0bc2c24403e0cd79a061ba1244b1a1db)bt\_mesh\_cfg\_cli\_mod\_pub\_get\_vnd()

| int bt\_mesh\_cfg\_cli\_mod\_pub\_get\_vnd | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cid*, |
|  |  | struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) \* | *pub*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get publish parameters for a vendor model on the target node.

This method can be used asynchronously by setting `status` and `pub` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | mod\_id | Model ID. |
    | cid | Company ID of the model. |
    | pub | Publication parameter return buffer. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga7fc2acda16f3f03a929c38796c67028e)bt\_mesh\_cfg\_cli\_mod\_pub\_set()

| int bt\_mesh\_cfg\_cli\_mod\_pub\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) \* | *pub*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Set publish parameters for a SIG model on the target node.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

`pub` shall not be NULL.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | mod\_id | Model ID. |
    | pub | Publication parameters. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gad2c602a2685ff38c0e78c1990b244e54)bt\_mesh\_cfg\_cli\_mod\_pub\_set\_vnd()

| int bt\_mesh\_cfg\_cli\_mod\_pub\_set\_vnd | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cid*, |
|  |  | struct [bt\_mesh\_cfg\_cli\_mod\_pub](structbt__mesh__cfg__cli__mod__pub.md) \* | *pub*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Set publish parameters for a vendor model on the target node.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

`pub` shall not be NULL.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | mod\_id | Model ID. |
    | cid | Company ID of the model. |
    | pub | Publication parameters. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gaf4ee720ce27eea9602b59a380278bb57)bt\_mesh\_cfg\_cli\_mod\_sub\_add()

| int bt\_mesh\_cfg\_cli\_mod\_sub\_add | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *sub\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Add a group address to a SIG model's subscription list.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | sub\_addr | Group address to add to the subscription list. |
    | mod\_id | Model ID. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga3ba34f8be138bc62a7eb7859b18dc441)bt\_mesh\_cfg\_cli\_mod\_sub\_add\_vnd()

| int bt\_mesh\_cfg\_cli\_mod\_sub\_add\_vnd | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *sub\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cid*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Add a group address to a vendor model's subscription list.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | sub\_addr | Group address to add to the subscription list. |
    | mod\_id | Model ID. |
    | cid | Company ID of the model. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga8d8595f077267b7d784fde30cbc4b207)bt\_mesh\_cfg\_cli\_mod\_sub\_del()

| int bt\_mesh\_cfg\_cli\_mod\_sub\_del | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *sub\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Delete a group address in a SIG model's subscription list.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | sub\_addr | Group address to add to the subscription list. |
    | mod\_id | Model ID. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gacd647905484fa8319a5377aa5777c254)bt\_mesh\_cfg\_cli\_mod\_sub\_del\_all()

| int bt\_mesh\_cfg\_cli\_mod\_sub\_del\_all | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Delete all group addresses in a SIG model's subscription list.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | mod\_id | Model ID. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga2059ccbc689af9c2127e4e399ea5bd43)bt\_mesh\_cfg\_cli\_mod\_sub\_del\_all\_vnd()

| int bt\_mesh\_cfg\_cli\_mod\_sub\_del\_all\_vnd | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cid*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Delete all group addresses in a vendor model's subscription list.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | mod\_id | Model ID. |
    | cid | Company ID of the model. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga74bad73184af2d6ce71134831f70680d)bt\_mesh\_cfg\_cli\_mod\_sub\_del\_vnd()

| int bt\_mesh\_cfg\_cli\_mod\_sub\_del\_vnd | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *sub\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cid*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Delete a group address in a vendor model's subscription list.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | sub\_addr | Group address to add to the subscription list. |
    | mod\_id | Model ID. |
    | cid | Company ID of the model. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gaf739e5e3a4b225e10bf2aedf143d7793)bt\_mesh\_cfg\_cli\_mod\_sub\_get()

| int bt\_mesh\_cfg\_cli\_mod\_sub\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *subs*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *sub\_cnt* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get the subscription list of a SIG model on the target node.

This method can be used asynchronously by setting `status` and ( `subs` or `sub_cnt` ) as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | mod\_id | Model ID. |
    | status | Status response parameter. |
    | subs | Subscription list response parameter. Will be filled with all the returned subscriptions it can fill. |
    | sub\_cnt | Subscription list element count. Should be set to the capacity of the `subs` list when calling. Will return the number of returned subscriptions upon success. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga09e751a9071402ae978c0355edfbdf03)bt\_mesh\_cfg\_cli\_mod\_sub\_get\_vnd()

| int bt\_mesh\_cfg\_cli\_mod\_sub\_get\_vnd | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cid*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *subs*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *sub\_cnt* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get the subscription list of a vendor model on the target node.

This method can be used asynchronously by setting `status` and ( `subs` or `sub_cnt` ) as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | mod\_id | Model ID. |
    | cid | Company ID of the model. |
    | status | Status response parameter. |
    | subs | Subscription list response parameter. Will be filled with all the returned subscriptions it can fill. |
    | sub\_cnt | Subscription list element count. Should be set to the capacity of the `subs` list when calling. Will return the number of returned subscriptions upon success. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gadac1cc360c30d290a861bbd534fca58d)bt\_mesh\_cfg\_cli\_mod\_sub\_overwrite()

| int bt\_mesh\_cfg\_cli\_mod\_sub\_overwrite | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *sub\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Overwrite all addresses in a SIG model's subscription list with a group address.

Deletes all subscriptions in the model's subscription list, and adds a single group address instead.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | sub\_addr | Group address to add to the subscription list. |
    | mod\_id | Model ID. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga69b2dfacc27ed94b9e1331ff4ac4b582)bt\_mesh\_cfg\_cli\_mod\_sub\_overwrite\_vnd()

| int bt\_mesh\_cfg\_cli\_mod\_sub\_overwrite\_vnd | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *sub\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cid*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Overwrite all addresses in a vendor model's subscription list with a group address.

Deletes all subscriptions in the model's subscription list, and adds a single group address instead.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | sub\_addr | Group address to add to the subscription list. |
    | mod\_id | Model ID. |
    | cid | Company ID of the model. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga2d22612cf9dc5030699bf7c6c58bf6d5)bt\_mesh\_cfg\_cli\_mod\_sub\_va\_add()

| int bt\_mesh\_cfg\_cli\_mod\_sub\_va\_add | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *label*[16], |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *virt\_addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Add a virtual address to a SIG model's subscription list.

This method can be used asynchronously by setting `status` and `virt_addr` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | label | Virtual address label to add to the subscription list. |
    | mod\_id | Model ID. |
    | virt\_addr | Virtual address response parameter. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gaa3a10a54a18a99d0b4b0aa85330b1640)bt\_mesh\_cfg\_cli\_mod\_sub\_va\_add\_vnd()

| int bt\_mesh\_cfg\_cli\_mod\_sub\_va\_add\_vnd | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *label*[16], |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cid*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *virt\_addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Add a virtual address to a vendor model's subscription list.

This method can be used asynchronously by setting `status` and `virt_addr` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | label | Virtual address label to add to the subscription list. |
    | mod\_id | Model ID. |
    | cid | Company ID of the model. |
    | virt\_addr | Virtual address response parameter. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gaf7107373fc0c70d091e9a521d8b641ad)bt\_mesh\_cfg\_cli\_mod\_sub\_va\_del()

| int bt\_mesh\_cfg\_cli\_mod\_sub\_va\_del | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *label*[16], |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *virt\_addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Delete a virtual address in a SIG model's subscription list.

This method can be used asynchronously by setting `status` and `virt_addr` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | label | Virtual address parameter to add to the subscription list. |
    | mod\_id | Model ID. |
    | virt\_addr | Virtual address response parameter. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga8884786e3ec349bcb8b89b60aa11f198)bt\_mesh\_cfg\_cli\_mod\_sub\_va\_del\_vnd()

| int bt\_mesh\_cfg\_cli\_mod\_sub\_va\_del\_vnd | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *label*[16], |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cid*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *virt\_addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Delete a virtual address in a vendor model's subscription list.

This method can be used asynchronously by setting `status` and `virt_addr` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | label | Virtual address label to add to the subscription list. |
    | mod\_id | Model ID. |
    | cid | Company ID of the model. |
    | virt\_addr | Virtual address response parameter. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga69809ad3f2cff8e1f394f6da6ed63264)bt\_mesh\_cfg\_cli\_mod\_sub\_va\_overwrite()

| int bt\_mesh\_cfg\_cli\_mod\_sub\_va\_overwrite | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *label*[16], |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *virt\_addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Overwrite all addresses in a SIG model's subscription list with a virtual address.

Deletes all subscriptions in the model's subscription list, and adds a single group address instead.

This method can be used asynchronously by setting `status` and `virt_addr` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | label | Virtual address label to add to the subscription list. |
    | mod\_id | Model ID. |
    | virt\_addr | Virtual address response parameter. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga70d3bb7fb914fa3685f4ad9b561a48b6)bt\_mesh\_cfg\_cli\_mod\_sub\_va\_overwrite\_vnd()

| int bt\_mesh\_cfg\_cli\_mod\_sub\_va\_overwrite\_vnd | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *elem\_addr*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *label*[16], |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *mod\_id*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cid*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *virt\_addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Overwrite all addresses in a vendor model's subscription list with a virtual address.

Deletes all subscriptions in the model's subscription list, and adds a single group address instead.

This method can be used asynchronously by setting `status` and `virt_addr` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | elem\_addr | Element address the model is in. |
    | label | Virtual address label to add to the subscription list. |
    | mod\_id | Model ID. |
    | cid | Company ID of the model. |
    | virt\_addr | Virtual address response parameter. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga283fb06ddb6427852ff0ac556d3c1852)bt\_mesh\_cfg\_cli\_net\_key\_add()

| int bt\_mesh\_cfg\_cli\_net\_key\_add | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *key\_net\_idx*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *net\_key*[16], |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Add a network key to the target node.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | key\_net\_idx | Network key index. |
    | net\_key | Network key. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gab2963ec5536cb4b941578bb490fdc013)bt\_mesh\_cfg\_cli\_net\_key\_del()

| int bt\_mesh\_cfg\_cli\_net\_key\_del | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *key\_net\_idx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Delete a network key from the target node.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | key\_net\_idx | Network key index. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gab42c5bdff36bea35e967946462b12457)bt\_mesh\_cfg\_cli\_net\_key\_get()

| int bt\_mesh\_cfg\_cli\_net\_key\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *keys*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *key\_cnt* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get a list of the target node's network key indexes.

This method can be used asynchronously by setting `keys` or `key_cnt` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | keys | Net key index list response parameter. Will be filled with all the returned network key indexes it can fill. |
    | key\_cnt | Net key index list length. Should be set to the capacity of the `keys` list when calling. Will return the number of returned network key indexes upon success. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gafdaff279685b821a7b205e45feed9a05)bt\_mesh\_cfg\_cli\_net\_key\_update()

| int bt\_mesh\_cfg\_cli\_net\_key\_update | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *key\_net\_idx*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *net\_key*[16], |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Update a network key to the target node.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | key\_net\_idx | Network key index. |
    | net\_key | Network key. |
    | status | Status response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga92ee7984b14590ed11a470c0dfea0bc9)bt\_mesh\_cfg\_cli\_net\_transmit\_get()

| int bt\_mesh\_cfg\_cli\_net\_transmit\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *transmit* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get the target node's network\_transmit state.

This method can be used asynchronously by setting `transmit` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | transmit | Network transmit response parameter. Returns the encoded network transmission parameters on success. Decoded with [BT\_MESH\_TRANSMIT\_COUNT](group__bt__mesh__access.md#ga62fda0d731241efbaa4827e4eb9d1795 "BT_MESH_TRANSMIT_COUNT") and [BT\_MESH\_TRANSMIT\_INT](group__bt__mesh__access.md#ga2aa21171c5677d23ad0c472291639417 "BT_MESH_TRANSMIT_INT"). |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga87f7c1e06b5c721c89031c527960bf40)bt\_mesh\_cfg\_cli\_net\_transmit\_set()

| int bt\_mesh\_cfg\_cli\_net\_transmit\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *val*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *transmit* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Set the target node's network transmit parameters.

This method can be used asynchronously by setting `transmit` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | val | New encoded network transmit parameters. |

See also
:   [BT\_MESH\_TRANSMIT](group__bt__mesh__access.md#gaff82bf652232fbce71c31f38a10577a9 "Encode transmission count & interval steps.").

Parameters
:   | transmit | Network transmit response parameter. Returns the encoded network transmission parameters on success. Decoded with [BT\_MESH\_TRANSMIT\_COUNT](group__bt__mesh__access.md#ga62fda0d731241efbaa4827e4eb9d1795 "BT_MESH_TRANSMIT_COUNT") and [BT\_MESH\_TRANSMIT\_INT](group__bt__mesh__access.md#ga2aa21171c5677d23ad0c472291639417 "BT_MESH_TRANSMIT_INT"). |
    | --- | --- |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gac02c170e260980d5b749b581910672d2)bt\_mesh\_cfg\_cli\_node\_identity\_get()

| int bt\_mesh\_cfg\_cli\_node\_identity\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *key\_net\_idx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *identity* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get the Node Identity parameters.

This method can be used asynchronously by setting `status` and `identity` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | key\_net\_idx | Network key index the application key belongs to. |
    | status | Status response parameter. |
    | identity | Identity response parameter. Must be one of [BT\_MESH\_NODE\_IDENTITY\_STOPPED](group__bt__mesh__cfg.md#ga9a83214cdbd34ac1d4bc644136523bd9 "BT_MESH_NODE_IDENTITY_STOPPED") or [BT\_MESH\_NODE\_IDENTITY\_RUNNING](group__bt__mesh__cfg.md#ga86e88acc6fdcc26a9cea4415daad016c "BT_MESH_NODE_IDENTITY_RUNNING") |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga12a8618d2b73f30742f8e8d2bdddc138)bt\_mesh\_cfg\_cli\_node\_identity\_set()

| int bt\_mesh\_cfg\_cli\_node\_identity\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *key\_net\_idx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *new\_identity*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *identity* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Set the Node Identity parameters.

This method can be used asynchronously by setting `status` and `identity` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | new\_identity | New identity state. Must be one of [BT\_MESH\_NODE\_IDENTITY\_STOPPED](group__bt__mesh__cfg.md#ga9a83214cdbd34ac1d4bc644136523bd9 "BT_MESH_NODE_IDENTITY_STOPPED") or [BT\_MESH\_NODE\_IDENTITY\_RUNNING](group__bt__mesh__cfg.md#ga86e88acc6fdcc26a9cea4415daad016c "BT_MESH_NODE_IDENTITY_RUNNING") |
    | key\_net\_idx | Network key index the application key belongs to. |
    | status | Status response parameter. |
    | identity | Identity response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gac6675d227749a69cedc5455c70626b76)bt\_mesh\_cfg\_cli\_node\_reset()

| int bt\_mesh\_cfg\_cli\_node\_reset | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \* | *status* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Reset the target node and remove it from the network.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | status | Status response parameter |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga4a50a6a5dcfdc42b7476f0b9e463ea45)bt\_mesh\_cfg\_cli\_relay\_get()

| int bt\_mesh\_cfg\_cli\_relay\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *transmit* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get the target node's Relay feature state.

This method can be used asynchronously by setting `status` and `transmit` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | status | Status response parameter. Returns one of [BT\_MESH\_RELAY\_DISABLED](group__bt__mesh__cfg.md#gaafd10319da7d2f938207b8fd6de02dbc "BT_MESH_RELAY_DISABLED"), [BT\_MESH\_RELAY\_ENABLED](group__bt__mesh__cfg.md#gae5d235a7c182a8add961d7ce344f87aa "BT_MESH_RELAY_ENABLED") or [BT\_MESH\_RELAY\_NOT\_SUPPORTED](group__bt__mesh__cfg.md#gabbbbddd31c2a92256fe2f7a7520e76f7 "BT_MESH_RELAY_NOT_SUPPORTED") on success. |
    | transmit | Transmit response parameter. Returns the encoded relay transmission parameters on success. Decoded with [BT\_MESH\_TRANSMIT\_COUNT](group__bt__mesh__access.md#ga62fda0d731241efbaa4827e4eb9d1795 "BT_MESH_TRANSMIT_COUNT") and [BT\_MESH\_TRANSMIT\_INT](group__bt__mesh__access.md#ga2aa21171c5677d23ad0c472291639417 "BT_MESH_TRANSMIT_INT"). |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga7fe8418130568bdf2a5e56ed2ad027b0)bt\_mesh\_cfg\_cli\_relay\_set()

| int bt\_mesh\_cfg\_cli\_relay\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *new\_relay*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *new\_transmit*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *status*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *transmit* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Set the target node's Relay parameters.

This method can be used asynchronously by setting `status` and `transmit` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | new\_relay | New relay state. Must be one of [BT\_MESH\_RELAY\_DISABLED](group__bt__mesh__cfg.md#gaafd10319da7d2f938207b8fd6de02dbc "BT_MESH_RELAY_DISABLED") or [BT\_MESH\_RELAY\_ENABLED](group__bt__mesh__cfg.md#gae5d235a7c182a8add961d7ce344f87aa "BT_MESH_RELAY_ENABLED"). |
    | new\_transmit | New encoded relay transmit parameters. |

See also
:   [BT\_MESH\_TRANSMIT](group__bt__mesh__access.md#gaff82bf652232fbce71c31f38a10577a9 "Encode transmission count & interval steps.").

Parameters
:   | status | Status response parameter. Returns one of [BT\_MESH\_RELAY\_DISABLED](group__bt__mesh__cfg.md#gaafd10319da7d2f938207b8fd6de02dbc "BT_MESH_RELAY_DISABLED"), [BT\_MESH\_RELAY\_ENABLED](group__bt__mesh__cfg.md#gae5d235a7c182a8add961d7ce344f87aa "BT_MESH_RELAY_ENABLED") or [BT\_MESH\_RELAY\_NOT\_SUPPORTED](group__bt__mesh__cfg.md#gabbbbddd31c2a92256fe2f7a7520e76f7 "BT_MESH_RELAY_NOT_SUPPORTED") on success. |
    | --- | --- |
    | transmit | Transmit response parameter. Returns the encoded relay transmission parameters on success. Decoded with [BT\_MESH\_TRANSMIT\_COUNT](group__bt__mesh__access.md#ga62fda0d731241efbaa4827e4eb9d1795 "BT_MESH_TRANSMIT_COUNT") and [BT\_MESH\_TRANSMIT\_INT](group__bt__mesh__access.md#ga2aa21171c5677d23ad0c472291639417 "BT_MESH_TRANSMIT_INT"). |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gaf5262c0a27e4b9249ecf908c259cc7d7)bt\_mesh\_cfg\_cli\_timeout\_get()

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) bt\_mesh\_cfg\_cli\_timeout\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get the current transmission timeout value.

Returns
:   The configured transmission timeout in milliseconds.

## [◆ ](#ga7e3521ae973dc825422c6dd5f07ef547)bt\_mesh\_cfg\_cli\_timeout\_set()

| void bt\_mesh\_cfg\_cli\_timeout\_set | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Set the transmission timeout value.

Parameters
:   | timeout | The new transmission timeout. |
    | --- | --- |

## [◆ ](#gaa141d4aabbed6c7780ac7f3955c8b580)bt\_mesh\_cfg\_cli\_ttl\_get()

| int bt\_mesh\_cfg\_cli\_ttl\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *ttl* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get the target node's Time To Live value.

This method can be used asynchronously by setting `ttl` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | ttl | TTL response buffer. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga2671234d739c802fd080a19d01235352)bt\_mesh\_cfg\_cli\_ttl\_set()

| int bt\_mesh\_cfg\_cli\_ttl\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *val*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *ttl* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Set the target node's Time To Live value.

This method can be used asynchronously by setting `ttl` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt with. |
    | --- | --- |
    | addr | Target node address. |
    | val | New Time To Live value. |
    | ttl | TTL response buffer. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gac005f52e191c3e5628f063dbc1a19645)bt\_mesh\_comp\_p0\_elem\_mod()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_comp\_p0\_elem\_mod | ( | struct [bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md) \* | *elem*, |
| --- | --- | --- | --- |
|  |  | int | *idx* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get a SIG model from the given composition data page 0 element.

Parameters
:   | elem | Element to read the model from. |
    | --- | --- |
    | idx | Index of the SIG model to read. |

Returns
:   The Model ID of the SIG model at the given index, or 0xffff if the index is out of bounds.

## [◆ ](#ga4f656102982961b7bf2e3d3896a2240e)bt\_mesh\_comp\_p0\_elem\_mod\_vnd()

| struct [bt\_mesh\_mod\_id\_vnd](structbt__mesh__mod__id__vnd.md) bt\_mesh\_comp\_p0\_elem\_mod\_vnd | ( | struct [bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md) \* | *elem*, |
| --- | --- | --- | --- |
|  |  | int | *idx* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Get a vendor model from the given composition data page 0 element.

Parameters
:   | elem | Element to read the model from. |
    | --- | --- |
    | idx | Index of the vendor model to read. |

Returns
:   The model ID of the vendor model at the given index, or {0xffff, 0xffff} if the index is out of bounds.

## [◆ ](#gaa6d60ebad6dc4a4f5b022937dbae3120)bt\_mesh\_comp\_p0\_elem\_pull()

| struct [bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md) \* bt\_mesh\_comp\_p0\_elem\_pull | ( | const struct [bt\_mesh\_comp\_p0](structbt__mesh__comp__p0.md) \* | *comp*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_comp\_p0\_elem](structbt__mesh__comp__p0__elem.md) \* | *elem* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Pull a composition data page 0 element from a composition data page 0 instance.

Each call to this function will pull out a new element from the composition data page, until all elements have been pulled.

Parameters
:   | comp | Composition data page |
    | --- | --- |
    | elem | Element to fill. |

Returns
:   A pointer to `elem` on success, or NULL if no more elements could be pulled.

## [◆ ](#ga1f79d98273a984f1c49b4d5dd5bf8d30)bt\_mesh\_comp\_p0\_get()

| int bt\_mesh\_comp\_p0\_get | ( | struct [bt\_mesh\_comp\_p0](structbt__mesh__comp__p0.md) \* | *comp*, |
| --- | --- | --- | --- |
|  |  | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Create a composition data page 0 representation from a buffer.

The composition data page object will take ownership over the buffer, which should not be manipulated directly after this call.

This function can be used in combination with [bt\_mesh\_cfg\_cli\_comp\_data\_get](#ga36259e9c811a8f1a21d642739cf297df) to read out composition data page 0 from other devices:

[NET\_BUF\_SIMPLE\_DEFINE](group__net__buf.md#gaf85aa0b705bb4fbe2630191fde802501)(buf, [BT\_MESH\_RX\_SDU\_MAX](group__bt__mesh__access.md#ga36f299f2fc13892b5a7d871dad1ec9ce));

struct [bt\_mesh\_comp\_p0](structbt__mesh__comp__p0.md) comp;

err = [bt\_mesh\_cfg\_cli\_comp\_data\_get](#ga36259e9c811a8f1a21d642739cf297df)(net\_idx, addr, 0, &page, &buf);

if (!err) {

[bt\_mesh\_comp\_p0\_get](#ga1f79d98273a984f1c49b4d5dd5bf8d30)(&comp, &buf);

}

[BT\_MESH\_RX\_SDU\_MAX](group__bt__mesh__access.md#ga36f299f2fc13892b5a7d871dad1ec9ce)

#define BT\_MESH\_RX\_SDU\_MAX

Maximum possible payload size of an incoming access message (in octets).

**Definition** access.h:130

[bt\_mesh\_comp\_p0\_get](#ga1f79d98273a984f1c49b4d5dd5bf8d30)

int bt\_mesh\_comp\_p0\_get(struct bt\_mesh\_comp\_p0 \*comp, struct net\_buf\_simple \*buf)

Create a composition data page 0 representation from a buffer.

[bt\_mesh\_cfg\_cli\_comp\_data\_get](#ga36259e9c811a8f1a21d642739cf297df)

int bt\_mesh\_cfg\_cli\_comp\_data\_get(uint16\_t net\_idx, uint16\_t addr, uint8\_t page, uint8\_t \*rsp, struct net\_buf\_simple \*comp)

Get the target node's composition data.

[NET\_BUF\_SIMPLE\_DEFINE](group__net__buf.md#gaf85aa0b705bb4fbe2630191fde802501)

#define NET\_BUF\_SIMPLE\_DEFINE(\_name, \_size)

Define a net\_buf\_simple stack variable.

**Definition** buf.h:46

[bt\_mesh\_comp\_p0](structbt__mesh__comp__p0.md)

Parsed Composition data page 0 representation.

**Definition** cfg\_cli.h:1605

Parameters
:   | buf | Network buffer containing composition data. |
    | --- | --- |
    | comp | Composition data structure to fill. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gae9a19b089d898af914ea5c287aca8fba)bt\_mesh\_comp\_p1\_elem\_pull()

| struct [bt\_mesh\_comp\_p1\_elem](structbt__mesh__comp__p1__elem.md) \* bt\_mesh\_comp\_p1\_elem\_pull | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_comp\_p1\_elem](structbt__mesh__comp__p1__elem.md) \* | *elem* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Pull a Composition Data Page 1 Element from a composition data page 1 instance.

Each call to this function will pull out a new element from the composition data page, until all elements have been pulled.

Parameters
:   | buf | Composition data page 1 buffer |
    | --- | --- |
    | elem | Element to fill. |

Returns
:   A pointer to `elem` on success, or NULL if no more elements could be pulled.

## [◆ ](#gac8b4b670c82b80a51834f7ef32206985)bt\_mesh\_comp\_p1\_item\_pull()

| struct [bt\_mesh\_comp\_p1\_model\_item](structbt__mesh__comp__p1__model__item.md) \* bt\_mesh\_comp\_p1\_item\_pull | ( | struct [bt\_mesh\_comp\_p1\_elem](structbt__mesh__comp__p1__elem.md) \* | *elem*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_comp\_p1\_model\_item](structbt__mesh__comp__p1__model__item.md) \* | *item* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Pull a Composition Data Page 1 Model Item from a Composition Data Page 1 Element.

Each call to this function will pull out a new item from the Composition Data Page 1 Element, until all items have been pulled.

Parameters
:   | elem | Composition data page 1 Element |
    | --- | --- |
    | item | Model Item to fill. |

Returns
:   A pointer to `item` on success, or NULL if no more elements could be pulled.

## [◆ ](#gac527fe27308c8a61ac1831af9605e429)bt\_mesh\_comp\_p1\_pull\_ext\_item()

| struct [bt\_mesh\_comp\_p1\_ext\_item](structbt__mesh__comp__p1__ext__item.md) \* bt\_mesh\_comp\_p1\_pull\_ext\_item | ( | struct [bt\_mesh\_comp\_p1\_model\_item](structbt__mesh__comp__p1__model__item.md) \* | *item*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_comp\_p1\_ext\_item](structbt__mesh__comp__p1__ext__item.md) \* | *ext\_item* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Pull Extended Model Item contained in Model Item.

Each call to this function will pull out a new element from the Extended Model Item, until all elements have been pulled.

Parameters
:   | item | Model Item to pull Extended Model Items from |
    | --- | --- |
    | ext\_item | Extended Model Item to fill |

Returns
:   A pointer to `ext_item` on success, or NULL if item could not be pulled

## [◆ ](#ga0854a494707a40b84beb8582f45e0470)bt\_mesh\_comp\_p2\_record\_pull()

| struct [bt\_mesh\_comp\_p2\_record](structbt__mesh__comp__p2__record.md) \* bt\_mesh\_comp\_p2\_record\_pull | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_comp\_p2\_record](structbt__mesh__comp__p2__record.md) \* | *record* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Pull a Composition Data Page 2 Record from a composition data page 2 instance.

Each call to this function will pull out a new element from the composition data page, until all elements have been pulled.

Parameters
:   | buf | Composition data page 2 buffer |
    | --- | --- |
    | record | Record to fill. |

Returns
:   A pointer to `record` on success, or NULL if no more elements could be pulled.

## [◆ ](#gaa411ab7db2e71a114a8108eaec9ca12c)bt\_mesh\_key\_idx\_unpack\_list()

| int bt\_mesh\_key\_idx\_unpack\_list | ( | struct [net\_buf\_simple](structnet__buf__simple.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *dst\_arr*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *dst\_cnt* ) |

`#include <[cfg_cli.h](cfg__cli_8h.md)>`

Unpack a list of key index entries from a buffer.

On success, `dst_cnt` is set to the amount of unpacked key index entries.

Parameters
:   | buf | Message buffer containing encoded AppKey or NetKey Indexes. |
    | --- | --- |
    | dst\_arr | Destination array for the unpacked list. |
    | dst\_cnt | Size of the destination array. |

Returns
:   0 on success.
:   -EMSGSIZE if dst\_arr size is to small to parse full message.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
