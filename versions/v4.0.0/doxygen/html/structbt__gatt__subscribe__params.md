---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__gatt__subscribe__params.html
original_path: doxygen/html/structbt__gatt__subscribe__params.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_gatt\_subscribe\_params Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md) » [GATT Client APIs](group__bt__gatt__client.md)

GATT Subscribe parameters.
[More...](#details)

`#include <[gatt.h](gatt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [bt\_gatt\_notify\_func\_t](group__bt__gatt__client.md#gab3e53eb5f9bb1eda7bf612ef95755b4d) | [notify](#acf237ef097e8b847eb049fb0a5d4b759) |
|  | Notification value callback. |
| [bt\_gatt\_subscribe\_func\_t](group__bt__gatt__client.md#ga2e914e63b4b91fa56bc3295283c43714) | [subscribe](#a91595407b8de4e862652e41100668f0a) |
|  | Subscribe CCC write request response callback If given, called with the subscription parameters given when subscribing. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [value\_handle](#a9248418eb04a5b7a0faed5077c40bf22) |
|  | Subscribe value handle. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [ccc\_handle](#a77c53cdfd4143483b33a8ecf6061561e) |
|  | Subscribe CCC handle. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [end\_handle](#af806d24aa97db1f2e9a021e719598a6d) |
|  | Subscribe End handle (for automatic discovery). |
| struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) \* | [disc\_params](#ad3a3b9335b85777d65bdf875486e292a) |
|  | Discover parameters used when ccc\_handle = [BT\_GATT\_AUTO\_DISCOVER\_CCC\_HANDLE](group__bt__gatt__client.md#ga7ca44e95989a143ae0b21e4a5316561d "BT_GATT_AUTO_DISCOVER_CCC_HANDLE"). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [value](#a3bff1209b7a0b5908408a568622d0150) |
|  | Subscribe value. |
| [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) | [min\_security](#a5b34bad1cf39bb3efd5faf516473dd4a) |
|  | Minimum required security for received notification. |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [flags](#aedd24024881e22372505355024cd716b) [[ATOMIC\_BITMAP\_SIZE](group__atomic__apis.md#gafac28874aaad3bcec72c693186e988cb)([BT\_GATT\_SUBSCRIBE\_NUM\_FLAGS](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6a5640a1e06740a89859c5f4b183d58e79))] |
|  | Subscription flags. |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#acbc7c9d38361e3b702fdf5efd7383b34) |
| enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) | [chan\_opt](#ae139848da09705d37fe7c9de4c1a4087) |

## Detailed Description

GATT Subscribe parameters.

## Field Documentation

## [◆ ](#a77c53cdfd4143483b33a8ecf6061561e)ccc\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_subscribe\_params::ccc\_handle |
| --- |

Subscribe CCC handle.

## [◆ ](#ae139848da09705d37fe7c9de4c1a4087)chan\_opt

| enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) bt\_gatt\_subscribe\_params::chan\_opt |
| --- |

## [◆ ](#ad3a3b9335b85777d65bdf875486e292a)disc\_params

| struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md)\* bt\_gatt\_subscribe\_params::disc\_params |
| --- |

Discover parameters used when ccc\_handle = [BT\_GATT\_AUTO\_DISCOVER\_CCC\_HANDLE](group__bt__gatt__client.md#ga7ca44e95989a143ae0b21e4a5316561d "BT_GATT_AUTO_DISCOVER_CCC_HANDLE").

## [◆ ](#af806d24aa97db1f2e9a021e719598a6d)end\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_subscribe\_params::end\_handle |
| --- |

Subscribe End handle (for automatic discovery).

## [◆ ](#aedd24024881e22372505355024cd716b)flags

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) bt\_gatt\_subscribe\_params::flags[[ATOMIC\_BITMAP\_SIZE](group__atomic__apis.md#gafac28874aaad3bcec72c693186e988cb)([BT\_GATT\_SUBSCRIBE\_NUM\_FLAGS](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6a5640a1e06740a89859c5f4b183d58e79))] |
| --- |

Subscription flags.

## [◆ ](#a5b34bad1cf39bb3efd5faf516473dd4a)min\_security

| [bt\_security\_t](group__bt__conn.md#gaf0c56cd26c4147f6c9f0faa11fa01783) bt\_gatt\_subscribe\_params::min\_security |
| --- |

Minimum required security for received notification.

Notifications and indications received over a connection with a lower security level are silently discarded.

## [◆ ](#acbc7c9d38361e3b702fdf5efd7383b34)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) bt\_gatt\_subscribe\_params::node |
| --- |

## [◆ ](#acf237ef097e8b847eb049fb0a5d4b759)notify

| [bt\_gatt\_notify\_func\_t](group__bt__gatt__client.md#gab3e53eb5f9bb1eda7bf612ef95755b4d) bt\_gatt\_subscribe\_params::notify |
| --- |

Notification value callback.

## [◆ ](#a91595407b8de4e862652e41100668f0a)subscribe

| [bt\_gatt\_subscribe\_func\_t](group__bt__gatt__client.md#ga2e914e63b4b91fa56bc3295283c43714) bt\_gatt\_subscribe\_params::subscribe |
| --- |

Subscribe CCC write request response callback If given, called with the subscription parameters given when subscribing.

## [◆ ](#a3bff1209b7a0b5908408a568622d0150)value

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_subscribe\_params::value |
| --- |

Subscribe value.

## [◆ ](#a9248418eb04a5b7a0faed5077c40bf22)value\_handle

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_subscribe\_params::value\_handle |
| --- |

Subscribe value handle.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[gatt.h](gatt_8h_source.md)

- [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
