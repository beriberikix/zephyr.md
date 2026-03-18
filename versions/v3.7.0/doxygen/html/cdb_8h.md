---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/cdb_8h.html
original_path: doxygen/html/cdb_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cdb.h File Reference

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](sys_2atomic_8h_source.md)>`  
`#include <[zephyr/bluetooth/mesh.h](mesh_8h_source.md)>`

[Go to the source code of this file.](cdb_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) |
| struct | [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) |
| struct | [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) |
| struct | [bt\_mesh\_cdb](structbt__mesh__cdb.md) |

| Macros | |
| --- | --- |
| #define | [NODE\_COUNT](#ae49e5e1ae89eef30538ae9f45c772b64)   0 |
| #define | [SUBNET\_COUNT](#a5ab07a907049974c089a4b0dd706ef77)   0 |
| #define | [APP\_KEY\_COUNT](#aab65f293c17c657d670e802bbfe389d7)   0 |

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [bt\_mesh\_cdb\_node\_func\_t](#a5d00af9f4c971f31c3016824757ebf66)) (struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \*node, void \*user\_data) |
|  | Node iterator callback. |

| Enumerations | |
| --- | --- |
| enum | { [BT\_MESH\_CDB\_NODE\_CONFIGURED](#a159f4eec3bbcaed25a4369b67e6937f1aab4ca02f1d0d9f6a743bee9f66eeba12) , [BT\_MESH\_CDB\_NODE\_FLAG\_COUNT](#a159f4eec3bbcaed25a4369b67e6937f1a00449c6d1403f903b115c3de36a2a3bd) } |
| enum | {     [BT\_MESH\_CDB\_VALID](#a0e45ffdd001e9fac31b74949a004e8f5ad5a2fc5c15efc200ef31b8876eabc01d) , [BT\_MESH\_CDB\_SUBNET\_PENDING](#a0e45ffdd001e9fac31b74949a004e8f5a5d07a0f33a2544be141d1fb4c6130bdd) , [BT\_MESH\_CDB\_KEYS\_PENDING](#a0e45ffdd001e9fac31b74949a004e8f5a62fc7baf49a7bf92a3b3c80eb57d8cf8) , [BT\_MESH\_CDB\_NODES\_PENDING](#a0e45ffdd001e9fac31b74949a004e8f5a3fe59a5bb698f65be4389345fe63ccc1) ,     [BT\_MESH\_CDB\_IVU\_IN\_PROGRESS](#a0e45ffdd001e9fac31b74949a004e8f5a229d9bfcc277ea2cb81e991a1a30ceb6) , [BT\_MESH\_CDB\_FLAG\_COUNT](#a0e45ffdd001e9fac31b74949a004e8f5abf303893a5d3b399856b3670c4a7fd41)   } |
| enum | { [BT\_MESH\_CDB\_ITER\_STOP](#a2ec5612f827a95662f18bc9e012048cdaf2362ea16e4733a32e26138a3577e5fb) = 0 , [BT\_MESH\_CDB\_ITER\_CONTINUE](#a2ec5612f827a95662f18bc9e012048cda6b057da4bd763f7c65e41410b7c72218) } |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_cdb\_create](#a00490e69b96e88cdf7336ca22e63617d) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16]) |
|  | Create the Mesh Configuration Database. |
| void | [bt\_mesh\_cdb\_clear](#a4bf4f49fbd75ee33876ffd34f6c6f76f) (void) |
|  | Clear the Mesh Configuration Database. |
| void | [bt\_mesh\_cdb\_iv\_update](#aa6d124339002c43fc35f301a9eef3e7c) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) iv\_index, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) iv\_update) |
|  | Set and store the IV Index and IV Update flag. |
| struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \* | [bt\_mesh\_cdb\_node\_alloc](#ab0dc86dd674f57a820aa3f5cebf77895) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uuid[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_elem, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
|  | Allocate a node. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bt\_mesh\_cdb\_free\_addr\_get](#aa10c4ec973e61626ba6424e443fb0b88) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_elem) |
|  | Get the first available address for the given element count. |
| void | [bt\_mesh\_cdb\_node\_del](#a6d9cc2d360075b6b3e939a4979e08895) (struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \*node, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) store) |
|  | Delete a node. |
| void | [bt\_mesh\_cdb\_node\_update](#ad4333e02b866589f7ca2b155cf814ca4) (struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \*node, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_elem) |
|  | Update a node. |
| struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \* | [bt\_mesh\_cdb\_node\_get](#a3d0034ec500d3964dd4b428e518abfb9) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
|  | Get a node by address. |
| void | [bt\_mesh\_cdb\_node\_store](#ac775f3d1be745aeba2979b9ae4b42c4f) (const struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \*node) |
|  | Store node to persistent storage. |
| int | [bt\_mesh\_cdb\_node\_key\_import](#a26b1e5560998cc37e2a627c44326db62) (struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \*node, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) in[16]) |
|  | Import device key for selected node. |
| int | [bt\_mesh\_cdb\_node\_key\_export](#a4a0f7577f1a8df96e4dcab6f682abf23) (const struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \*node, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) out[16]) |
|  | Export device key from selected node. |
| void | [bt\_mesh\_cdb\_node\_foreach](#ae8ed0ef1a00e973d864c944c9d9400bc) ([bt\_mesh\_cdb\_node\_func\_t](#a5d00af9f4c971f31c3016824757ebf66) func, void \*user\_data) |
|  | Node iterator. |
| struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \* | [bt\_mesh\_cdb\_subnet\_alloc](#aeba4ed506e30ab8d91746b36e7e5f968) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
|  | Allocate a subnet. |
| void | [bt\_mesh\_cdb\_subnet\_del](#a66df2f6b6363af595181fe722122996d) (struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \*sub, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) store) |
|  | Delete a subnet. |
| struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \* | [bt\_mesh\_cdb\_subnet\_get](#a34dcf031e675235cdcbe0e1f76c00cf3) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
|  | Get a subnet by NetIdx. |
| void | [bt\_mesh\_cdb\_subnet\_store](#a59e6b7da8c91df35ce6f8268da35c933) (const struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \*sub) |
|  | Store subnet to persistent storage. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_cdb\_subnet\_flags](#a121a30fd546ccb887c2c49ceef65c2d6) (const struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \*sub) |
|  | Get the flags for a subnet. |
| int | [bt\_mesh\_cdb\_subnet\_key\_import](#aba737b508e0e40dfb5ad9da9d7b6fd11) (struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \*sub, int key\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) in[16]) |
|  | Import network key for selected subnetwork. |
| int | [bt\_mesh\_cdb\_subnet\_key\_export](#ac361a17a704195e852faecda09881203) (const struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \*sub, int key\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) out[16]) |
|  | Export network key from selected subnetwork. |
| struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) \* | [bt\_mesh\_cdb\_app\_key\_alloc](#ab82dcdf26d66ea4ab0df34bc23421f39) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idx) |
|  | Allocate an application key. |
| void | [bt\_mesh\_cdb\_app\_key\_del](#a692c6980c9b0d2da18e8f47d67757f07) (struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) \*key, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) store) |
|  | Delete an application key. |
| struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) \* | [bt\_mesh\_cdb\_app\_key\_get](#ab728a20fdb1535cc7059a39e8490a736) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idx) |
|  | Get an application key by AppIdx. |
| void | [bt\_mesh\_cdb\_app\_key\_store](#a4e9470adfa797be85b7f4df43b63d6d2) (const struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) \*key) |
|  | Store application key to persistent storage. |
| int | [bt\_mesh\_cdb\_app\_key\_import](#a9ad0651ccaa7ff1f86402ce8c05c9410) (struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) \*key, int key\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) in[16]) |
|  | Import application key. |
| int | [bt\_mesh\_cdb\_app\_key\_export](#a87cfce7316efabe4c8b24be6c3b6d8b4) (const struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) \*key, int key\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) out[16]) |
|  | Export application key. |

| Variables | |
| --- | --- |
| struct bt\_mesh\_cdb | [bt\_mesh\_cdb](#afa51505628405a3778d1bdb4fd905ca0) |

## Macro Definition Documentation

## [◆ ](#aab65f293c17c657d670e802bbfe389d7)APP\_KEY\_COUNT

| #define APP\_KEY\_COUNT   0 |
| --- |

## [◆ ](#ae49e5e1ae89eef30538ae9f45c772b64)NODE\_COUNT

| #define NODE\_COUNT   0 |
| --- |

## [◆ ](#a5ab07a907049974c089a4b0dd706ef77)SUBNET\_COUNT

| #define SUBNET\_COUNT   0 |
| --- |

## Typedef Documentation

## [◆ ](#a5d00af9f4c971f31c3016824757ebf66)bt\_mesh\_cdb\_node\_func\_t

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* bt\_mesh\_cdb\_node\_func\_t) (struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \*node, void \*user\_data) |
| --- |

Node iterator callback.

Parameters
:   | node | Node found. |
    | --- | --- |
    | user\_data | Data given. |

Returns
:   BT\_MESH\_CDB\_ITER\_CONTINUE to continue to iterate through the nodes or BT\_MESH\_CDB\_ITER\_STOP to stop.

## Enumeration Type Documentation

## [◆ ](#a2ec5612f827a95662f18bc9e012048cd)anonymous enum

| anonymous enum |
| --- |

| Enumerator | |
| --- | --- |
| BT\_MESH\_CDB\_ITER\_STOP |  |
| BT\_MESH\_CDB\_ITER\_CONTINUE |  |

## [◆ ](#a0e45ffdd001e9fac31b74949a004e8f5)anonymous enum

| anonymous enum |
| --- |

| Enumerator | |
| --- | --- |
| BT\_MESH\_CDB\_VALID |  |
| BT\_MESH\_CDB\_SUBNET\_PENDING |  |
| BT\_MESH\_CDB\_KEYS\_PENDING |  |
| BT\_MESH\_CDB\_NODES\_PENDING |  |
| BT\_MESH\_CDB\_IVU\_IN\_PROGRESS |  |
| BT\_MESH\_CDB\_FLAG\_COUNT |  |

## [◆ ](#a159f4eec3bbcaed25a4369b67e6937f1)anonymous enum

| anonymous enum |
| --- |

| Enumerator | |
| --- | --- |
| BT\_MESH\_CDB\_NODE\_CONFIGURED |  |
| BT\_MESH\_CDB\_NODE\_FLAG\_COUNT |  |

## Function Documentation

## [◆ ](#ab82dcdf26d66ea4ab0df34bc23421f39)bt\_mesh\_cdb\_app\_key\_alloc()

| struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) \* bt\_mesh\_cdb\_app\_key\_alloc | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *app\_idx* ) |

Allocate an application key.

Allocate a new application key in the CDB.

Parameters
:   | net\_idx | NetIdx of NetKey that the application key is bound to. |
    | --- | --- |
    | app\_idx | AppIdx of the application key. |

Returns
:   The new application key or NULL if it cannot be allocated due to lack of resources or the key has been already allocated.

## [◆ ](#a692c6980c9b0d2da18e8f47d67757f07)bt\_mesh\_cdb\_app\_key\_del()

| void bt\_mesh\_cdb\_app\_key\_del | ( | struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) \* | *key*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *store* ) |

Delete an application key.

Delete an application key from the CDB.

Parameters
:   | key | The application key to be deleted. |
    | --- | --- |
    | store | If true, the key will be cleared from persistent storage. |

## [◆ ](#a87cfce7316efabe4c8b24be6c3b6d8b4)bt\_mesh\_cdb\_app\_key\_export()

| int bt\_mesh\_cdb\_app\_key\_export | ( | const struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) \* | *key*, |
| --- | --- | --- | --- |
|  |  | int | *key\_idx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *out*[16] ) |

Export application key.

Using security library with PSA implementation access to the key by pointer will not give a valid value since the key is hidden in the library. The application has to export the key.

Parameters
:   | key | cdb application key structure. |
    | --- | --- |
    | key\_idx | 0 or 1. If Key Refresh procedure is in progress then two keys are available. The old key has an index 0 and the new one has an index 1. Otherwise, the only key with index 0 exists. |
    | out | key value. |

Returns
:   0 on success or negative error code on failure.

## [◆ ](#ab728a20fdb1535cc7059a39e8490a736)bt\_mesh\_cdb\_app\_key\_get()

| struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) \* bt\_mesh\_cdb\_app\_key\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *app\_idx* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get an application key by AppIdx.

Try to find the application key with the specified AppIdx.

Parameters
:   | app\_idx | AppIdx of the application key to look for. |
    | --- | --- |

Returns
:   The application key with the specified AppIdx or NULL if no such key exists.

## [◆ ](#a9ad0651ccaa7ff1f86402ce8c05c9410)bt\_mesh\_cdb\_app\_key\_import()

| int bt\_mesh\_cdb\_app\_key\_import | ( | struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) \* | *key*, |
| --- | --- | --- | --- |
|  |  | int | *key\_idx*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *in*[16] ) |

Import application key.

Using security library with PSA implementation access to the key by pointer will not give a valid value since the key is hidden in the library. The application has to import the key.

Parameters
:   | key | cdb application key structure. |
    | --- | --- |
    | key\_idx | 0 or 1. If Key Refresh procedure is in progress then two keys are available. The old key has an index 0 and the new one has an index 1. Otherwise, the only key with index 0 exists. |
    | in | key value. |

Returns
:   0 on success or negative error code on failure.

## [◆ ](#a4e9470adfa797be85b7f4df43b63d6d2)bt\_mesh\_cdb\_app\_key\_store()

| void bt\_mesh\_cdb\_app\_key\_store | ( | const struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) \* | *key* | ) |  |
| --- | --- | --- | --- | --- | --- |

Store application key to persistent storage.

Parameters
:   | key | Application key to be stored. |
    | --- | --- |

## [◆ ](#a4bf4f49fbd75ee33876ffd34f6c6f76f)bt\_mesh\_cdb\_clear()

| void bt\_mesh\_cdb\_clear | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

Clear the Mesh Configuration Database.

Remove all nodes, subnets and app-keys stored in the database and mark the database as invalid. The data will be cleared from persistent storage if CONFIG\_BT\_SETTINGS is enabled.

## [◆ ](#a00490e69b96e88cdf7336ca22e63617d)bt\_mesh\_cdb\_create()

| int bt\_mesh\_cdb\_create | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *key*[16] | ) |  |
| --- | --- | --- | --- | --- | --- |

Create the Mesh Configuration Database.

Create and initialize the Mesh Configuration Database. A primary subnet, ie one with NetIdx 0, will be added and the provided key will be used as NetKey for that subnet.

Parameters
:   | key | The NetKey to be used for the primary subnet. |
    | --- | --- |

Returns
:   0 on success or negative error code on failure.

## [◆ ](#aa10c4ec973e61626ba6424e443fb0b88)bt\_mesh\_cdb\_free\_addr\_get()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_cdb\_free\_addr\_get | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_elem* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get the first available address for the given element count.

Parameters
:   | num\_elem | Number of elements to accommodate. |
    | --- | --- |

Returns
:   The first unicast address in an address range that allows a node with the given number of elements to fit.

## [◆ ](#aa6d124339002c43fc35f301a9eef3e7c)bt\_mesh\_cdb\_iv\_update()

| void bt\_mesh\_cdb\_iv\_update | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *iv\_index*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *iv\_update* ) |

Set and store the IV Index and IV Update flag.

The IV Index stored in the CDB will be the one used during provisioning of new nodes. This function is generally only used from inside the stack.

This function will store the data to persistent storage if CONFIG\_BT\_SETTINGS is enabled.

Parameters
:   | iv\_index | The new IV Index to use. |
    | --- | --- |
    | iv\_update | True if there is an ongoing IV Update procedure. |

## [◆ ](#ab0dc86dd674f57a820aa3f5cebf77895)bt\_mesh\_cdb\_node\_alloc()

| struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \* bt\_mesh\_cdb\_node\_alloc | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *uuid*[16], |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_elem*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx* ) |

Allocate a node.

Allocate a new node in the CDB.

If `addr` is 0, [bt\_mesh\_cdb\_free\_addr\_get](#aa10c4ec973e61626ba6424e443fb0b88) will be used to allocate a free address.

Parameters
:   | uuid | UUID of the node. |
    | --- | --- |
    | addr | Address of the node's primary element. If 0, the lowest possible address available will be assigned to the node. |
    | num\_elem | Number of elements that the node has. |
    | net\_idx | NetIdx that the node was provisioned to. |

Returns
:   The new node or NULL if CDB has already allocated :kconfig:option:CONFIG\_BT\_MESH\_CDB\_NODE\_COUNT nodes, or reached the end of the unicast address range, or if `addr` is non-zero and less than the lowest available address or collide with the allocated addresses.

## [◆ ](#a6d9cc2d360075b6b3e939a4979e08895)bt\_mesh\_cdb\_node\_del()

| void bt\_mesh\_cdb\_node\_del | ( | struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \* | *node*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *store* ) |

Delete a node.

Delete a node from the CDB. When deleting the node and the address of the last element of the deleted node is greater than the lowest available address, CDB will update the lowest available address. The lowest available address is reset and the deleted addresses can be reused only after IV Index update.

Parameters
:   | node | The node to be deleted. |
    | --- | --- |
    | store | If true, the node will be cleared from persistent storage. |

## [◆ ](#ae8ed0ef1a00e973d864c944c9d9400bc)bt\_mesh\_cdb\_node\_foreach()

| void bt\_mesh\_cdb\_node\_foreach | ( | [bt\_mesh\_cdb\_node\_func\_t](#a5d00af9f4c971f31c3016824757ebf66) | *func*, |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

Node iterator.

Iterate nodes in the Mesh Configuration Database. The callback function will only be called for valid, ie allocated, nodes.

Parameters
:   | func | Callback function. |
    | --- | --- |
    | user\_data | Data to pass to the callback. |

## [◆ ](#a3d0034ec500d3964dd4b428e518abfb9)bt\_mesh\_cdb\_node\_get()

| struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \* bt\_mesh\_cdb\_node\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get a node by address.

Try to find the node that has the provided address assigned to one of its elements.

Parameters
:   | addr | Address of the element to look for. |
    | --- | --- |

Returns
:   The node that has an element with address addr or NULL if no such node exists.

## [◆ ](#a4a0f7577f1a8df96e4dcab6f682abf23)bt\_mesh\_cdb\_node\_key\_export()

| int bt\_mesh\_cdb\_node\_key\_export | ( | const struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \* | *node*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *out*[16] ) |

Export device key from selected node.

Using security library with PSA implementation access to the key by pointer will not give a valid value since the key is hidden in the library. The application has to export the key.

Parameters
:   | node | Selected node. |
    | --- | --- |
    | out | key value. |

Returns
:   0 on success or negative error code on failure.

## [◆ ](#a26b1e5560998cc37e2a627c44326db62)bt\_mesh\_cdb\_node\_key\_import()

| int bt\_mesh\_cdb\_node\_key\_import | ( | struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \* | *node*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *in*[16] ) |

Import device key for selected node.

Using security library with PSA implementation access to the key by pointer will not give a valid value since the key is hidden in the library. The application has to import the key.

Parameters
:   | node | Selected node. |
    | --- | --- |
    | in | key value. |

Returns
:   0 on success or negative error code on failure.

## [◆ ](#ac775f3d1be745aeba2979b9ae4b42c4f)bt\_mesh\_cdb\_node\_store()

| void bt\_mesh\_cdb\_node\_store | ( | const struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \* | *node* | ) |  |
| --- | --- | --- | --- | --- | --- |

Store node to persistent storage.

Parameters
:   | node | Node to be stored. |
    | --- | --- |

## [◆ ](#ad4333e02b866589f7ca2b155cf814ca4)bt\_mesh\_cdb\_node\_update()

| void bt\_mesh\_cdb\_node\_update | ( | struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \* | *node*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_elem* ) |

Update a node.

Assigns the node a new address and clears the previous persistent storage entry.

Parameters
:   | node | The node to be deleted. |
    | --- | --- |
    | addr | New unicast address for the node. |
    | num\_elem | Updated number of elements in the node. |

## [◆ ](#aeba4ed506e30ab8d91746b36e7e5f968)bt\_mesh\_cdb\_subnet\_alloc()

| struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \* bt\_mesh\_cdb\_subnet\_alloc | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx* | ) |  |
| --- | --- | --- | --- | --- | --- |

Allocate a subnet.

Allocate a new subnet in the CDB.

Parameters
:   | net\_idx | NetIdx of the subnet. |
    | --- | --- |

Returns
:   The new subnet or NULL if it cannot be allocated due to lack of resources or the subnet has been already allocated.

## [◆ ](#a66df2f6b6363af595181fe722122996d)bt\_mesh\_cdb\_subnet\_del()

| void bt\_mesh\_cdb\_subnet\_del | ( | struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \* | *sub*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *store* ) |

Delete a subnet.

Delete a subnet from the CDB.

Parameters
:   | sub | The subnet to be deleted. |
    | --- | --- |
    | store | If true, the subnet will be cleared from persistent storage. |

## [◆ ](#a121a30fd546ccb887c2c49ceef65c2d6)bt\_mesh\_cdb\_subnet\_flags()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_cdb\_subnet\_flags | ( | const struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \* | *sub* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get the flags for a subnet.

Parameters
:   | sub | The subnet to get flags for. |
    | --- | --- |

Returns
:   The flags for the subnet.

## [◆ ](#a34dcf031e675235cdcbe0e1f76c00cf3)bt\_mesh\_cdb\_subnet\_get()

| struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \* bt\_mesh\_cdb\_subnet\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get a subnet by NetIdx.

Try to find the subnet with the specified NetIdx.

Parameters
:   | net\_idx | NetIdx of the subnet to look for. |
    | --- | --- |

Returns
:   The subnet with the specified NetIdx or NULL if no such subnet exists.

## [◆ ](#ac361a17a704195e852faecda09881203)bt\_mesh\_cdb\_subnet\_key\_export()

| int bt\_mesh\_cdb\_subnet\_key\_export | ( | const struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \* | *sub*, |
| --- | --- | --- | --- |
|  |  | int | *key\_idx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *out*[16] ) |

Export network key from selected subnetwork.

Using security library with PSA implementation access to the key by pointer will not give a valid value since the key is hidden in the library. The application has to export the key.

Parameters
:   | sub | Selected subnetwork. |
    | --- | --- |
    | key\_idx | 0 or 1. If Key Refresh procedure is in progress then two keys are available. The old key has an index 0 and the new one has an index 1. Otherwise, the only key with index 0 exists. |
    | out | key value. |

Returns
:   0 on success or negative error code on failure.

## [◆ ](#aba737b508e0e40dfb5ad9da9d7b6fd11)bt\_mesh\_cdb\_subnet\_key\_import()

| int bt\_mesh\_cdb\_subnet\_key\_import | ( | struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \* | *sub*, |
| --- | --- | --- | --- |
|  |  | int | *key\_idx*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *in*[16] ) |

Import network key for selected subnetwork.

Using security library with PSA implementation access to the key by pointer will not give a valid value since the key is hidden in the library. The application has to import the key.

Parameters
:   | sub | Selected subnetwork. |
    | --- | --- |
    | key\_idx | 0 or 1. If Key Refresh procedure is in progress then two keys are available. The old key has an index 0 and the new one has an index 1. Otherwise, the only key with index 0 exists. |
    | in | key value. |

Returns
:   0 on success or negative error code on failure.

## [◆ ](#a59e6b7da8c91df35ce6f8268da35c933)bt\_mesh\_cdb\_subnet\_store()

| void bt\_mesh\_cdb\_subnet\_store | ( | const struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \* | *sub* | ) |  |
| --- | --- | --- | --- | --- | --- |

Store subnet to persistent storage.

Parameters
:   | sub | Subnet to be stored. |
    | --- | --- |

## Variable Documentation

## [◆ ](#afa51505628405a3778d1bdb4fd905ca0)bt\_mesh\_cdb

| | struct bt\_mesh\_cdb bt\_mesh\_cdb | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [cdb.h](cdb_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
