---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__mesh__cfg__app.html
original_path: doxygen/html/group__bt__mesh__cfg__app.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Application Configuration

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Runtime Configuration](group__bt__mesh__cfg.md)

Application Configuration.
[More...](#details)

| Functions | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_app\_key\_add](#ga0110ef750489af49a156a259c5a95c9b) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16]) |
|  | Add an Application key. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_app\_key\_update](#ga5ae73ef766f0e1c38c0414c0a34e4053) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16]) |
|  | Update an Application key. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_app\_key\_del](#gaa0e80a19c14d47808fc11459bf5ea2eb) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
|  | Delete an Application key. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_app\_key\_exists](#ga42c46a936e589460225a1fa69598a1ac) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idx) |
|  | Check if an Application key is known. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_mesh\_app\_keys\_get](#gad7a949a0a814f6c9a26816c076d8b92a) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) app\_idxs[], [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) max, [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) skip) |
|  | Get a list of all known Application key indexes. |

## Detailed Description

Application Configuration.

## Function Documentation

## [◆ ](#ga0110ef750489af49a156a259c5a95c9b)bt\_mesh\_app\_key\_add()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_app\_key\_add | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *app\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *key*[16] ) |

`#include <[cfg.h](cfg_8h.md)>`

Add an Application key.

Adds the Application with the given index to the list of known applications. Allows the node to send and receive model messages encrypted with this Application key.

Every Application is bound to a specific Subnet. The node must know the Subnet the Application is bound to before it can add the Application.

Parameters
:   | app\_idx | Application index. |
    | --- | --- |
    | net\_idx | Network index the Application is bound to. |
    | key | Application key value. |

Return values
:   | STATUS\_SUCCESS | The Application was successfully added. |
    | --- | --- |
    | STATUS\_INVALID\_NETKEY | The NetIdx is unknown. |
    | STATUS\_INSUFF\_RESOURCES | There's no room for storing this Application. |
    | STATUS\_INVALID\_BINDING | This AppIdx is already bound to another Subnet. |
    | STATUS\_IDX\_ALREADY\_STORED | This AppIdx is already stored with a different key value. |
    | STATUS\_CANNOT\_SET | Cannot set the Application key for some reason. |

## [◆ ](#gaa0e80a19c14d47808fc11459bf5ea2eb)bt\_mesh\_app\_key\_del()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_app\_key\_del | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *app\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx* ) |

`#include <[cfg.h](cfg_8h.md)>`

Delete an Application key.

All models bound to this application will remove this binding. All models publishing with this application will stop publishing.

Parameters
:   | app\_idx | Application index. |
    | --- | --- |
    | net\_idx | Network index. |

Return values
:   | STATUS\_SUCCESS | The Application key was successfully deleted. |
    | --- | --- |
    | STATUS\_INVALID\_NETKEY | The NetIdx is unknown. |
    | STATUS\_INVALID\_BINDING | This AppIdx is not bound to the given NetIdx. |

## [◆ ](#ga42c46a936e589460225a1fa69598a1ac)bt\_mesh\_app\_key\_exists()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_app\_key\_exists | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *app\_idx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[cfg.h](cfg_8h.md)>`

Check if an Application key is known.

Parameters
:   | app\_idx | Application index. |
    | --- | --- |

Returns
:   true if the Application is known, false otherwise.

## [◆ ](#ga5ae73ef766f0e1c38c0414c0a34e4053)bt\_mesh\_app\_key\_update()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_app\_key\_update | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *app\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *key*[16] ) |

`#include <[cfg.h](cfg_8h.md)>`

Update an Application key.

Update an Application with a second Application key, as part of the Key Refresh procedure of the bound Subnet. The node will continue transmitting with the old application key (but receiving on both) until the Subnet enters Key Refresh phase 2. Once the Subnet enters Key Refresh phase 3, the old application key will be deleted.

Note
:   The Application key can only be updated if the bound Subnet is in Key Refresh phase 1.

Parameters
:   | app\_idx | Application index. |
    | --- | --- |
    | net\_idx | Network index the Application is bound to, or [BT\_MESH\_KEY\_ANY](group__bt__mesh__access.md#ga7718cce0713be98a08420c7eab1b40ee "BT_MESH_KEY_ANY") to skip the binding check. |
    | key | New key value. |

Return values
:   | STATUS\_SUCCESS | The Application key was successfully updated. |
    | --- | --- |
    | STATUS\_INVALID\_NETKEY | The NetIdx is unknown. |
    | STATUS\_INVALID\_BINDING | This AppIdx is not bound to the given NetIdx. |
    | STATUS\_CANNOT\_UPDATE | The Application key cannot be updated for some reason. |
    | STATUS\_IDX\_ALREADY\_STORED | This AppIdx is already updated with a different key value. |

## [◆ ](#gad7a949a0a814f6c9a26816c076d8b92a)bt\_mesh\_app\_keys\_get()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) bt\_mesh\_app\_keys\_get | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *app\_idxs*[], |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *max*, |
|  |  | [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) | *skip* ) |

`#include <[cfg.h](cfg_8h.md)>`

Get a list of all known Application key indexes.

Builds a list of all Application indexes for the given network index in the `app_idxs` array. If the `app_idxs` array cannot fit all bound Applications, this function fills all available entries and returns `-ENOMEM`. In this case, the next `max` entries of the list can be read out by calling

[bt\_mesh\_app\_keys\_get](#gad7a949a0a814f6c9a26816c076d8b92a)(net\_idx, list, max, max);

[bt\_mesh\_app\_keys\_get](#gad7a949a0a814f6c9a26816c076d8b92a)

ssize\_t bt\_mesh\_app\_keys\_get(uint16\_t net\_idx, uint16\_t app\_idxs[], size\_t max, off\_t skip)

Get a list of all known Application key indexes.

Note that any changes to the Application key list between calls to this function could change the order and number of entries in the list.

Parameters
:   | net\_idx | Network Index to get the Applications of, or [BT\_MESH\_KEY\_ANY](group__bt__mesh__access.md#ga7718cce0713be98a08420c7eab1b40ee "BT_MESH_KEY_ANY") to get all Applications. |
    | --- | --- |
    | app\_idxs | Array to fill. |
    | max | Max number of indexes to return. |
    | skip | Number of indexes to skip. Enables batched processing of the list. |

Returns
:   The number of indexes added to the `app_idxs` array, or `-ENOMEM` if the number of known Applications exceeds the `max` parameter.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
