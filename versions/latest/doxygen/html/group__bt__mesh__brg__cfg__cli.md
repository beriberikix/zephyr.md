---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__mesh__brg__cfg__cli.html
original_path: doxygen/html/group__bt__mesh__brg__cfg__cli.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Bridge Configuration Client Model

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

API for the Bluetooth Mesh Bridge Configuration Client model.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_brg\_cfg\_cli\_cb](structbt__mesh__brg__cfg__cli__cb.md) |
|  | Mesh Bridge Configuration Client Status messages callback. [More...](structbt__mesh__brg__cfg__cli__cb.md#details) |
| struct | [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md) |
|  | Bridge Configuration Client Model Context. [More...](structbt__mesh__brg__cfg__cli.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_BRG\_CFG\_CLI](#ga4cf994be4732bd99b2c8a4642f670efe)(\_cli) |
|  | Bridge Configuration Client model Composition Data entry. |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_brg\_cfg\_cli\_get](#ga6a4507190e425013a9d21ea0a1be1b5c) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, enum [bt\_mesh\_brg\_cfg\_state](group__bt__mesh__brg__cfg.md#ga7bddcbe2b1196df6a1c80d8c213866f9) \*status) |
|  | Sends a Subnet Bridge Get message to the given destination address. |
| int | [bt\_mesh\_brg\_cfg\_cli\_set](#ga6643d4d043af4b0cb30470a5c9a46f38) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, enum [bt\_mesh\_brg\_cfg\_state](group__bt__mesh__brg__cfg.md#ga7bddcbe2b1196df6a1c80d8c213866f9) val, enum [bt\_mesh\_brg\_cfg\_state](group__bt__mesh__brg__cfg.md#ga7bddcbe2b1196df6a1c80d8c213866f9) \*status) |
|  | Sends a Subnet Bridge Set message to the given destination address with the given parameters. |
| int | [bt\_mesh\_brg\_cfg\_cli\_table\_size\_get](#ga99951987bd6787e3e1348d8e51e64fe5) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*size) |
|  | Sends a Bridging Table Size Get message to the given destination address with the given parameters. |
| int | [bt\_mesh\_brg\_cfg\_cli\_table\_add](#ga8f055e8ee384e8ea4887a56720959b26) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_brg\_cfg\_table\_entry](structbt__mesh__brg__cfg__table__entry.md) \*entry, struct [bt\_mesh\_brg\_cfg\_table\_status](structbt__mesh__brg__cfg__table__status.md) \*rsp) |
|  | Sends a Bridging Table Add message to the given destination address with the given parameters. |
| int | [bt\_mesh\_brg\_cfg\_cli\_table\_remove](#gabdb919dcf177b8d5c8a28b057469bf18) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx1, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx2, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr1, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr2, struct [bt\_mesh\_brg\_cfg\_table\_status](structbt__mesh__brg__cfg__table__status.md) \*rsp) |
|  | Sends a Bridging Table Remove message to the given destination address with the given parameters. |
| int | [bt\_mesh\_brg\_cfg\_cli\_subnets\_get](#ga04bb227d14d4f478e4f32a8ca87d2c38) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_brg\_cfg\_filter\_netkey](structbt__mesh__brg__cfg__filter__netkey.md) filter\_net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) start\_idx, struct [bt\_mesh\_brg\_cfg\_subnets\_list](structbt__mesh__brg__cfg__subnets__list.md) \*rsp) |
|  | Sends a Bridged Subnets Get message to the given destination address with the given parameters. |
| int | [bt\_mesh\_brg\_cfg\_cli\_table\_get](#gacd3811be7b87d2d9187aed6c50945b85) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx1, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx2, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_idx, struct [bt\_mesh\_brg\_cfg\_table\_list](structbt__mesh__brg__cfg__table__list.md) \*rsp) |
|  | Sends a Bridging Table Get message to the given destination address with the given parameters. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [bt\_mesh\_brg\_cfg\_cli\_timeout\_get](#ga252994dd3119387703af45c0932ef253) (void) |
|  | Get the current transmission timeout value. |
| void | [bt\_mesh\_brg\_cfg\_cli\_timeout\_set](#gad30102a29983545ec79f178b1390ce74) ([int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Set the transmission timeout value. |

## Detailed Description

API for the Bluetooth Mesh Bridge Configuration Client model.

## Macro Definition Documentation

## [◆ ](#ga4cf994be4732bd99b2c8a4642f670efe)BT\_MESH\_MODEL\_BRG\_CFG\_CLI

| #define BT\_MESH\_MODEL\_BRG\_CFG\_CLI | ( |  | *\_cli* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[brg_cfg_cli.h](brg__cfg__cli_8h.md)>`

**Value:**

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)([BT\_MESH\_MODEL\_ID\_BRG\_CFG\_CLI](group__bt__mesh__access.md#ga9c776b4befd21c15f4867d906f631257), \_bt\_mesh\_brg\_cfg\_cli\_op, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), \_cli, \

&\_bt\_mesh\_brg\_cfg\_cli\_cb)

[BT\_MESH\_MODEL\_ID\_BRG\_CFG\_CLI](group__bt__mesh__access.md#ga9c776b4befd21c15f4867d906f631257)

#define BT\_MESH\_MODEL\_ID\_BRG\_CFG\_CLI

Bridge Configuration Client.

**Definition** access.h:193

[BT\_MESH\_MODEL\_CB](group__bt__mesh__access.md#gac062c101b7310020e11a527de9c40d3a)

#define BT\_MESH\_MODEL\_CB(\_id, \_op, \_pub, \_user\_data, \_cb)

Composition data SIG model entry with callback functions.

**Definition** access.h:495

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

Bridge Configuration Client model Composition Data entry.

Parameters
:   | \_cli | Pointer to a [Bridge Configuration Client Model](group__bt__mesh__brg__cfg__cli.md "Bridge Configuration Client Model") instance. |
    | --- | --- |

## Function Documentation

## [◆ ](#ga6a4507190e425013a9d21ea0a1be1b5c)bt\_mesh\_brg\_cfg\_cli\_get()

| int bt\_mesh\_brg\_cfg\_cli\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | enum [bt\_mesh\_brg\_cfg\_state](group__bt__mesh__brg__cfg.md#ga7bddcbe2b1196df6a1c80d8c213866f9) \* | *status* ) |

`#include <[brg_cfg_cli.h](brg__cfg__cli_8h.md)>`

Sends a Subnet Bridge Get message to the given destination address.

This function sends a Subnet Bridge Get message to the given destination address to query the value of the Subnet Bridge state of a subnet. The Subnet Bridge state indicates whether the subnet bridged feature is enabled or not. The function expects a Subnet Bridge Status message as a response from the destination node.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt the message with. |
    | --- | --- |
    | addr | Target node address. |
    | status | Status response parameter, returns one of [BT\_MESH\_BRG\_CFG\_DISABLED](group__bt__mesh__brg__cfg.md#gga7bddcbe2b1196df6a1c80d8c213866f9a20b2a18d76793d0efabeb9e7e47a3dc4 "BT_MESH_BRG_CFG_DISABLED") or [BT\_MESH\_BRG\_CFG\_ENABLED](group__bt__mesh__brg__cfg.md#gga7bddcbe2b1196df6a1c80d8c213866f9ab719036dc7e16001a14a5054331fa9b2 "BT_MESH_BRG_CFG_ENABLED") on success. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga6643d4d043af4b0cb30470a5c9a46f38)bt\_mesh\_brg\_cfg\_cli\_set()

| int bt\_mesh\_brg\_cfg\_cli\_set | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | enum [bt\_mesh\_brg\_cfg\_state](group__bt__mesh__brg__cfg.md#ga7bddcbe2b1196df6a1c80d8c213866f9) | *val*, |
|  |  | enum [bt\_mesh\_brg\_cfg\_state](group__bt__mesh__brg__cfg.md#ga7bddcbe2b1196df6a1c80d8c213866f9) \* | *status* ) |

`#include <[brg_cfg_cli.h](brg__cfg__cli_8h.md)>`

Sends a Subnet Bridge Set message to the given destination address with the given parameters.

This function sends a Subnet Bridge Set message to the given destination address with the given parameters to set the value of the Subnet Bridge state of a subnet. The Subnet Bridge state indicates whether the subnet bridge feature is enabled or not. The function expects a Subnet Bridge Status message as a response from the destination node.

This method can be used asynchronously by setting `status` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt the message with. |
    | --- | --- |
    | addr | Target node address. |
    | val | Value to set the Subnet Bridge state to. Must be one of [BT\_MESH\_BRG\_CFG\_DISABLED](group__bt__mesh__brg__cfg.md#gga7bddcbe2b1196df6a1c80d8c213866f9a20b2a18d76793d0efabeb9e7e47a3dc4 "BT_MESH_BRG_CFG_DISABLED") or [BT\_MESH\_BRG\_CFG\_ENABLED](group__bt__mesh__brg__cfg.md#gga7bddcbe2b1196df6a1c80d8c213866f9ab719036dc7e16001a14a5054331fa9b2 "BT_MESH_BRG_CFG_ENABLED"). |
    | status | Status response parameter, returns one of [BT\_MESH\_BRG\_CFG\_DISABLED](group__bt__mesh__brg__cfg.md#gga7bddcbe2b1196df6a1c80d8c213866f9a20b2a18d76793d0efabeb9e7e47a3dc4 "BT_MESH_BRG_CFG_DISABLED") or [BT\_MESH\_BRG\_CFG\_ENABLED](group__bt__mesh__brg__cfg.md#gga7bddcbe2b1196df6a1c80d8c213866f9ab719036dc7e16001a14a5054331fa9b2 "BT_MESH_BRG_CFG_ENABLED") on success. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga04bb227d14d4f478e4f32a8ca87d2c38)bt\_mesh\_brg\_cfg\_cli\_subnets\_get()

| int bt\_mesh\_brg\_cfg\_cli\_subnets\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | struct [bt\_mesh\_brg\_cfg\_filter\_netkey](structbt__mesh__brg__cfg__filter__netkey.md) | *filter\_net\_idx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *start\_idx*, |
|  |  | struct [bt\_mesh\_brg\_cfg\_subnets\_list](structbt__mesh__brg__cfg__subnets__list.md) \* | *rsp* ) |

`#include <[brg_cfg_cli.h](brg__cfg__cli_8h.md)>`

Sends a Bridged Subnets Get message to the given destination address with the given parameters.

This function sends a Bridged Subnets Get message to the given destination address with the given parameters to get the list of subnets that are bridged by the node. The function expects a Bridged Subnets List message as a response from the destination node.

This method can be used asynchronously by setting `rsp` as NULL. This way the method will not wait for response and will return immediately after sending the command.

When `rsp` is set, the user is responsible for providing a buffer for the filtered set of N pairs of NetKey Indexes in [bt\_mesh\_brg\_cfg\_subnets\_list::list](structbt__mesh__brg__cfg__subnets__list.md#a00ebe6255aabcd1cab49f08e4dc7e21b "bt_mesh_brg_cfg_subnets_list::list"). If a buffer is not provided, the bridged subnets won't be copied.

Parameters
:   | net\_idx | Network index to encrypt the message with. |
    | --- | --- |
    | addr | Target node address. |
    | filter\_net\_idx | Filter and NetKey Index used for filtering |
    | start\_idx | Start offset to read in units of Bridging Table state entries |
    | rsp | Pointer to a struct storing the received response from the server, or NULL to not wait for a response. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga8f055e8ee384e8ea4887a56720959b26)bt\_mesh\_brg\_cfg\_cli\_table\_add()

| int bt\_mesh\_brg\_cfg\_cli\_table\_add | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | struct [bt\_mesh\_brg\_cfg\_table\_entry](structbt__mesh__brg__cfg__table__entry.md) \* | *entry*, |
|  |  | struct [bt\_mesh\_brg\_cfg\_table\_status](structbt__mesh__brg__cfg__table__status.md) \* | *rsp* ) |

`#include <[brg_cfg_cli.h](brg__cfg__cli_8h.md)>`

Sends a Bridging Table Add message to the given destination address with the given parameters.

This function sends a Bridging Table Add message to the given destination address with the given parameters to add an entry to the Bridging Table. The Bridging Table contains the net keys and addresses that are authorized to be bridged by the node. The function expects a Bridging Table Status message as a response from the destination node.

This method can be used asynchronously by setting `rsp` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt the message with. |
    | --- | --- |
    | addr | Target node address. |
    | entry | Pointer to bridging Table entry to add. |
    | rsp | Status response parameter |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gacd3811be7b87d2d9187aed6c50945b85)bt\_mesh\_brg\_cfg\_cli\_table\_get()

| int bt\_mesh\_brg\_cfg\_cli\_table\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx1*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx2*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *start\_idx*, |
|  |  | struct [bt\_mesh\_brg\_cfg\_table\_list](structbt__mesh__brg__cfg__table__list.md) \* | *rsp* ) |

`#include <[brg_cfg_cli.h](brg__cfg__cli_8h.md)>`

Sends a Bridging Table Get message to the given destination address with the given parameters.

This function sends a Bridging Table Get message to the given destination address with the given parameters to get the contents of the Bridging Table. The Bridging Table contains the addresses that are authorized to be bridged by the node. The function expects a Bridging Table List message as a response from the destination node.

This method can be used asynchronously by setting `rsp` as NULL. This way the method will not wait for response and will return immediately after sending the command.

When `rsp` is set, the user is responsible for providing a buffer for the filtered set of N pairs of NetKey Indexes in [bt\_mesh\_brg\_cfg\_table\_list::list](structbt__mesh__brg__cfg__table__list.md#a44ce11d9a2cbda69b605fab6ed68cc56 "bt_mesh_brg_cfg_table_list::list"). If a buffer is not provided, the bridged addresses won't be copied. If a buffer size is shorter than received list, only those many entries that fit in the buffer will be copied from the list, and rest will be discarded.

Parameters
:   | net\_idx | Network index to encrypt the message with. |
    | --- | --- |
    | addr | Target node address. |
    | net\_idx1 | NetKey Index of the first subnet. |
    | net\_idx2 | NetKey Index of the second subnet. |
    | start\_idx | Start offset to read in units of Bridging Table state entries. |
    | rsp | Pointer to a struct storing the received response from the server, or NULL to not wait for a response. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#gabdb919dcf177b8d5c8a28b057469bf18)bt\_mesh\_brg\_cfg\_cli\_table\_remove()

| int bt\_mesh\_brg\_cfg\_cli\_table\_remove | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx1*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx2*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr1*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr2*, |
|  |  | struct [bt\_mesh\_brg\_cfg\_table\_status](structbt__mesh__brg__cfg__table__status.md) \* | *rsp* ) |

`#include <[brg_cfg_cli.h](brg__cfg__cli_8h.md)>`

Sends a Bridging Table Remove message to the given destination address with the given parameters.

This function sends a Bridging Table Remove message to the given destination address with the given parameters to remove an entry from the Bridging Table. The Bridging Table contains the net keys and addresses that are authorized to be bridged by the node. The function expects a Bridging Table Status message as a response from the destination node.

This method can be used asynchronously by setting `rsp` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt the message with. |
    | --- | --- |
    | addr | Target node address. |
    | net\_idx1 | NetKey Index of the first subnet |
    | net\_idx2 | NetKey Index of the second subnet |
    | addr1 | Address of the node in the first subnet |
    | addr2 | Address of the node in the second subnet |
    | rsp | Pointer to a struct storing the received response from the server, or NULL to not wait for a response. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga99951987bd6787e3e1348d8e51e64fe5)bt\_mesh\_brg\_cfg\_cli\_table\_size\_get()

| int bt\_mesh\_brg\_cfg\_cli\_table\_size\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *size* ) |

`#include <[brg_cfg_cli.h](brg__cfg__cli_8h.md)>`

Sends a Bridging Table Size Get message to the given destination address with the given parameters.

This function sends a Bridging Table Size Get message to the given destination address with the given parameters to get the size of the Bridging Table of the node. The Bridging Table size indicates the maximum number of entries that can be stored in the Bridging Table. The function expects a Bridging Table Size Status message as a response from the destination node.

This method can be used asynchronously by setting `size` as NULL. This way the method will not wait for response and will return immediately after sending the command.

Parameters
:   | net\_idx | Network index to encrypt the message with. |
    | --- | --- |
    | addr | Target node address. |
    | size | Bridging Table size response parameter. |

Returns
:   0 on success, or (negative) error code on failure.

## [◆ ](#ga252994dd3119387703af45c0932ef253)bt\_mesh\_brg\_cfg\_cli\_timeout\_get()

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) bt\_mesh\_brg\_cfg\_cli\_timeout\_get | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[brg_cfg_cli.h](brg__cfg__cli_8h.md)>`

Get the current transmission timeout value.

Returns
:   The configured transmission timeout in milliseconds.

## [◆ ](#gad30102a29983545ec79f178b1390ce74)bt\_mesh\_brg\_cfg\_cli\_timeout\_set()

| void bt\_mesh\_brg\_cfg\_cli\_timeout\_set | ( | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *timeout* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[brg_cfg_cli.h](brg__cfg__cli_8h.md)>`

Set the transmission timeout value.

Parameters
:   | timeout | The new transmission timeout. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
