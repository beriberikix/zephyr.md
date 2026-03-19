---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__mesh__proxy__cb.html
original_path: doxygen/html/structbt__mesh__proxy__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_proxy\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Proxy](group__bt__mesh__proxy.md)

Callbacks for the Proxy feature.
[More...](#details)

`#include <[proxy.h](proxy_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [identity\_enabled](#ae6f129ae511681d2f1fccafedba47918) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
|  | Started sending Node Identity beacons on the given subnet. |
| void(\* | [identity\_disabled](#a207ebf7e3f1f1e732d4540af000bf2ef) )([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
|  | Stopped sending Node Identity beacons on the given subnet. |

## Detailed Description

Callbacks for the Proxy feature.

Should be instantiated with [BT\_MESH\_PROXY\_CB\_DEFINE](group__bt__mesh__proxy.md#ga325b71c3d7ed69952bf760c0288b28ef "BT_MESH_PROXY_CB_DEFINE").

## Field Documentation

## [◆ ](#a207ebf7e3f1f1e732d4540af000bf2ef)identity\_disabled

| void(\* bt\_mesh\_proxy\_cb::identity\_disabled) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
| --- |

Stopped sending Node Identity beacons on the given subnet.

Parameters
:   | net\_idx | Network index the Node Identity beacons were running on. |
    | --- | --- |

## [◆ ](#ae6f129ae511681d2f1fccafedba47918)identity\_enabled

| void(\* bt\_mesh\_proxy\_cb::identity\_enabled) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx) |
| --- |

Started sending Node Identity beacons on the given subnet.

Parameters
:   | net\_idx | Network index the Node Identity beacons are running on. |
    | --- | --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[proxy.h](proxy_8h_source.md)

- [bt\_mesh\_proxy\_cb](structbt__mesh__proxy__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
