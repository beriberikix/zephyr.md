---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__mesh__cfg__subnet.html
original_path: doxygen/html/group__bt__mesh__cfg__subnet.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Subnet Configuration

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Runtime Configuration](group__bt__mesh__cfg.md)

Subnet Configuration.
[More...](#details)

| Functions | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_subnet\_add](#ga6a6ba6ac1dcbe5f6cfce9bbf38c1851f) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16]) |
|  | Add a Subnet. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_subnet\_update](#ga47236f48940303be27fa6af4797424c2) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16]) |
|  | Update the given Subnet. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_subnet\_del](#gaec9d827d5f026b473f3ac88988d3c842) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
|  | Delete a Subnet. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_subnet\_exists](#gad48780acaae085350a8b48d033717bfa) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
|  | Check whether a Subnet is known. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_subnet\_kr\_phase\_set](#gaef15af43e74e3c71590c63c5f1e3ea55) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*phase) |
|  | Set the Subnet's Key Refresh phase. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_subnet\_kr\_phase\_get](#gad251907892150649f3f1ae6b4112cd84) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*phase) |
|  | Get the Subnet's Key Refresh phase. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_subnet\_node\_id\_set](#ga59bf9f022665edc0ad03267e4bd16632) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) node\_id) |
|  | Set the Node Identity state of the Subnet. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_subnet\_node\_id\_get](#ga683d1f9abe82649a774b3d53dcaced8e) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) \*node\_id) |
|  | Get the Node Identity state of the Subnet. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_subnet\_priv\_node\_id\_set](#ga5aa3e7f6b64e1b8b98f9737606d5d1ec) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) priv\_node\_id) |
|  | Set the Private Node Identity state of the Subnet. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_subnet\_priv\_node\_id\_get](#ga555b4a7127869355fdf6040b8d14f999) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) \*priv\_node\_id) |
|  | Get the Private Node Identity state of the Subnet. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_mesh\_subnets\_get](#ga0fd04bff5423a36b013089a4ba351d67) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idxs[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) skip) |
|  | Get a list of all known Subnet indexes. |

## Detailed Description

Subnet Configuration.

## Function Documentation

## [◆ ](#ga6a6ba6ac1dcbe5f6cfce9bbf38c1851f)bt\_mesh\_subnet\_add()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_subnet\_add | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *key*[16] ) |

`#include <[cfg.h](cfg_8h.md)>`

Add a Subnet.

Adds a subnet with the given network index and network key to the list of known Subnets. All messages sent on the given Subnet will be processed by this node, and the node may send and receive Network Beacons on the given Subnet.

Parameters
:   | net\_idx | Network index. |
    | --- | --- |
    | key | Root network key of the Subnet. All other keys are derived from this. |

Return values
:   | STATUS\_SUCCESS | The Subnet was successfully added. |
    | --- | --- |
    | STATUS\_INSUFF\_RESOURCES | No room for this Subnet. |
    | STATUS\_UNSPECIFIED | The Subnet couldn't be created for some reason. |

## [◆ ](#gaec9d827d5f026b473f3ac88988d3c842)bt\_mesh\_subnet\_del()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_subnet\_del | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Delete a Subnet.

Removes the Subnet with the given network index from the node. The node will stop sending Network Beacons with the given Subnet, and can no longer process messages on this Subnet.

All Applications bound to this Subnet are also deleted.

Parameters
:   | net\_idx | Network index. |
    | --- | --- |

Return values
:   | STATUS\_SUCCESS | The Subnet was deleted. |
    | --- | --- |
    | STATUS\_INVALID\_NETKEY | The NetIdx is unknown. |

## [◆ ](#gad48780acaae085350a8b48d033717bfa)bt\_mesh\_subnet\_exists()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_subnet\_exists | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Check whether a Subnet is known.

Parameters
:   | net\_idx | Network index |
    | --- | --- |

Returns
:   true if a Subnet with the given index exists, false otherwise.

## [◆ ](#gad251907892150649f3f1ae6b4112cd84)bt\_mesh\_subnet\_kr\_phase\_get()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_subnet\_kr\_phase\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *phase* ) |

`#include <[cfg.h](cfg_8h.md)>`

Get the Subnet's Key Refresh phase.

Parameters
:   | net\_idx | Network index. |
    | --- | --- |
    | phase | Pointer to the Key Refresh variable to fill. |

Return values
:   | STATUS\_SUCCESS | Successfully populated the `phase` variable. |
    | --- | --- |
    | STATUS\_INVALID\_NETKEY | The NetIdx is unknown. |

## [◆ ](#gaef15af43e74e3c71590c63c5f1e3ea55)bt\_mesh\_subnet\_kr\_phase\_set()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_subnet\_kr\_phase\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *phase* ) |

`#include <[cfg.h](cfg_8h.md)>`

Set the Subnet's Key Refresh phase.

The Key Refresh procedure is started by updating the Subnet keys through [bt\_mesh\_subnet\_update](#ga47236f48940303be27fa6af4797424c2). This puts the Subnet in Key Refresh Phase 1. Once all nodes have received the new Subnet key, Key Refresh Phase 2 can be activated through this function to start transmitting with the new network key. Finally, to revoke the old key, set the Key Refresh Phase to 3. This removes the old keys from the node, and returns the Subnet back to normal single-key operation with the new key set.

Parameters
:   | net\_idx | Network index. |
    | --- | --- |
    | phase | Pointer to the new Key Refresh phase. Will return the actual Key Refresh phase after updating. |

Return values
:   | STATUS\_SUCCESS | The Key Refresh phase of the Subnet was successfully changed. |
    | --- | --- |
    | STATUS\_INVALID\_NETKEY | The NetIdx is unknown. |
    | STATUS\_CANNOT\_UPDATE | The given phase change is invalid. |

## [◆ ](#ga683d1f9abe82649a774b3d53dcaced8e)bt\_mesh\_subnet\_node\_id\_get()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_subnet\_node\_id\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) \* | *node\_id* ) |

`#include <[cfg.h](cfg_8h.md)>`

Get the Node Identity state of the Subnet.

Parameters
:   | net\_idx | Network index. |
    | --- | --- |
    | node\_id | Node Identity variable to fill. |

Return values
:   | STATUS\_SUCCESS | Successfully populated the `node_id` variable. |
    | --- | --- |
    | STATUS\_INVALID\_NETKEY | The NetIdx is unknown. |

## [◆ ](#ga59bf9f022665edc0ad03267e4bd16632)bt\_mesh\_subnet\_node\_id\_set()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_subnet\_node\_id\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) | *node\_id* ) |

`#include <[cfg.h](cfg_8h.md)>`

Set the Node Identity state of the Subnet.

The Node Identity state of a Subnet determines whether the Subnet advertises connectable Node Identity beacons for Proxy Clients to connect to. Once started, the Node Identity beacon runs for 60 seconds, or until it is stopped.

This function serves the same purpose as [bt\_mesh\_proxy\_identity\_enable](group__bt__mesh__proxy.md#ga7fb3c76f1be6943dd4a18f26e8dd18e7 "bt_mesh_proxy_identity_enable"), but only acts on a single Subnet.

GATT Proxy support must be enabled through `CONFIG_BT_MESH_GATT_PROXY`.

Parameters
:   | net\_idx | Network index. |
    | --- | --- |
    | node\_id | New Node Identity state, must be either [BT\_MESH\_FEATURE\_ENABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275 "BT_MESH_FEATURE_ENABLED") or [BT\_MESH\_FEATURE\_DISABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729 "BT_MESH_FEATURE_DISABLED"). |

Return values
:   | STATUS\_SUCCESS | Successfully set the Node Identity state of the Subnet. |
    | --- | --- |
    | STATUS\_INVALID\_NETKEY | The NetIdx is unknown. |
    | STATUS\_FEAT\_NOT\_SUPP | The Node Identity feature is not supported. |
    | STATUS\_CANNOT\_SET | Couldn't set the Node Identity state. |

## [◆ ](#ga555b4a7127869355fdf6040b8d14f999)bt\_mesh\_subnet\_priv\_node\_id\_get()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_subnet\_priv\_node\_id\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) \* | *priv\_node\_id* ) |

`#include <[cfg.h](cfg_8h.md)>`

Get the Private Node Identity state of the Subnet.

Parameters
:   | net\_idx | Network index. |
    | --- | --- |
    | priv\_node\_id | Private Node Identity variable to fill. |

Return values
:   | STATUS\_SUCCESS | Successfully populated the `priv_node_id` variable. |
    | --- | --- |
    | STATUS\_INVALID\_NETKEY | The NetIdx is unknown. |

## [◆ ](#ga5aa3e7f6b64e1b8b98f9737606d5d1ec)bt\_mesh\_subnet\_priv\_node\_id\_set()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_subnet\_priv\_node\_id\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_mesh\_feat\_state](group__bt__mesh__cfg.md#ga0a3557a71597885a31cf209c6b83cedb) | *priv\_node\_id* ) |

`#include <[cfg.h](cfg_8h.md)>`

Set the Private Node Identity state of the Subnet.

The Private Node Identity state of a Subnet determines whether the Subnet advertises connectable Private Node Identity beacons for Proxy Clients to connect to. Once started, the Node Identity beacon runs for 60 seconds, or until it is stopped.

Private Node Identity can only be enabled if regular Node Identity is not enabled for any subnet.

GATT Proxy and Private Beacon support must be enabled through `CONFIG_BT_MESH_GATT_PROXY` and `CONFIG_BT_MESH_PRIV_BEACONS`.

Parameters
:   | net\_idx | Network index. |
    | --- | --- |
    | priv\_node\_id | New Private Node Identity state, must be either [BT\_MESH\_FEATURE\_ENABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedbabff35d6447ab5608292065f20d1e5275 "BT_MESH_FEATURE_ENABLED") or [BT\_MESH\_FEATURE\_DISABLED](group__bt__mesh__cfg.md#gga0a3557a71597885a31cf209c6b83cedba17b0aabc3d26da41aab09f009004f729 "BT_MESH_FEATURE_DISABLED"). |

Return values
:   | STATUS\_SUCCESS | Successfully set the Private Node Identity state of the Subnet. |
    | --- | --- |
    | STATUS\_INVALID\_NETKEY | The NetIdx is unknown. |
    | STATUS\_FEAT\_NOT\_SUPP | The Private Node Identity feature is not supported. |
    | STATUS\_TEMP\_STATE\_CHG\_FAIL | The Private Node Identity state cannot be enabled, because Node Identity state is already enabled. |
    | STATUS\_CANNOT\_SET | Couldn't set the Private Node Identity state. |

## [◆ ](#ga47236f48940303be27fa6af4797424c2)bt\_mesh\_subnet\_update()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_subnet\_update | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *key*[16] ) |

`#include <[cfg.h](cfg_8h.md)>`

Update the given Subnet.

Starts the Key Refresh procedure for this Subnet by adding a second set of encryption keys. The Subnet will continue sending with the old key (but receiving messages using both) until the Subnet enters Key Refresh phase 2.

This allows a network configurator to replace old network and application keys for the entire network, effectively removing access for all nodes that aren't given the new keys.

Parameters
:   | net\_idx | Network index. |
    | --- | --- |
    | key | New root network key of the Subnet. |

Return values
:   | STATUS\_SUCCESS | The Subnet was updated with a second key. |
    | --- | --- |
    | STATUS\_INVALID\_NETKEY | The NetIdx is unknown. |
    | STATUS\_IDX\_ALREADY\_STORED | The `key` value is the same as the current key. |
    | STATUS\_CANNOT\_UPDATE | The Subnet cannot be updated for some reason. |

## [◆ ](#ga0fd04bff5423a36b013089a4ba351d67)bt\_mesh\_subnets\_get()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) bt\_mesh\_subnets\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idxs*[], |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *max*, |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *skip* ) |

`#include <[cfg.h](cfg_8h.md)>`

Get a list of all known Subnet indexes.

Builds a list of all known Subnet indexes in the `net_idxs` array. If the `net_idxs` array is smaller than the list of known Subnets, this function fills all available entries and returns `-ENOMEM`. In this case, the next `max` entries of the list can be read out by calling

[bt\_mesh\_subnets\_get](#ga0fd04bff5423a36b013089a4ba351d67)(list, max, max);

[bt\_mesh\_subnets\_get](#ga0fd04bff5423a36b013089a4ba351d67)

ssize\_t bt\_mesh\_subnets\_get(uint16\_t net\_idxs[], size\_t max, off\_t skip)

Get a list of all known Subnet indexes.

Note that any changes to the Subnet list between calls to this function could change the order and number of entries in the list.

Parameters
:   | net\_idxs | Array to fill. |
    | --- | --- |
    | max | Max number of indexes to return. |
    | skip | Number of indexes to skip. Enables batched processing of the list. |

Returns
:   The number of indexes added to the `net_idxs` array, or `-ENOMEM` if the number of known Subnets exceeds the `max` parameter.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
