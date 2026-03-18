---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__bt__mesh__rpr.html
original_path: doxygen/html/group__bt__mesh__rpr.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Remote Provisioning models

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) |
|  | Remote provisioning actor, as seen across the mesh. [More...](structbt__mesh__rpr__node.md#details) |
| struct | [bt\_mesh\_rpr\_unprov](structbt__mesh__rpr__unprov.md) |
|  | Unprovisioned device. [More...](structbt__mesh__rpr__unprov.md#details) |
| struct | [bt\_mesh\_rpr\_link](structbt__mesh__rpr__link.md) |
|  | Remote Provisioning Link status. [More...](structbt__mesh__rpr__link.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_RPR\_UNPROV\_HASH](#ga94522cf0b3832b576100b787808474bd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Unprovisioned device has URI hash value. |
| #define | [BT\_MESH\_RPR\_UNPROV\_ACTIVE](#ga31bbb1483d5bdd10e0a9da0978bd90c0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Internal. |
| #define | [BT\_MESH\_RPR\_UNPROV\_FOUND](#gac33ea72f94eb986592941ca10b7884f1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Internal. |
| #define | [BT\_MESH\_RPR\_UNPROV\_REPORTED](#ga8121bae9a6158a5f2df4bc154237e05b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Internal. |
| #define | [BT\_MESH\_RPR\_UNPROV\_EXT](#gac1eebae68c05d9e59599d0601055790d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Internal. |
| #define | [BT\_MESH\_RPR\_UNPROV\_HAS\_LINK](#ga8349a9af764b3e502bf5ecd8bb0ce203)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Internal. |
| #define | [BT\_MESH\_RPR\_UNPROV\_EXT\_ADV\_RXD](#ga1dc95fc6baba79d9bc4007169fcfe55b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Internal. |
| #define | [BT\_MESH\_RPR\_EXT\_SCAN\_TIME\_MIN](#ga2b7e2636da150f5c5cb4e3bdee13c745)   1 |
|  | Minimum extended scan duration in seconds. |
| #define | [BT\_MESH\_RPR\_EXT\_SCAN\_TIME\_MAX](#ga2a5241b2e87fec227740dd4f2de3a68a)   21 |
|  | Maximum extended scan duration in seconds. |

| Enumerations | |
| --- | --- |
| enum | [bt\_mesh\_rpr\_status](#ga77d2f7158e7629dc54acafbf65e6af90) {     [BT\_MESH\_RPR\_SUCCESS](#gga77d2f7158e7629dc54acafbf65e6af90a9375e568e9b69ab37484b91cfca75117) , [BT\_MESH\_RPR\_ERR\_SCANNING\_CANNOT\_START](#gga77d2f7158e7629dc54acafbf65e6af90aeec9abd5c000ea23fe9b7aa396f8b599) , [BT\_MESH\_RPR\_ERR\_INVALID\_STATE](#gga77d2f7158e7629dc54acafbf65e6af90ab5ff83c3503d6f709dfeb1423b957c26) , [BT\_MESH\_RPR\_ERR\_LIMITED\_RESOURCES](#gga77d2f7158e7629dc54acafbf65e6af90abb00e5ea05d585e1350d2b46d2fdda82) ,     [BT\_MESH\_RPR\_ERR\_LINK\_CANNOT\_OPEN](#gga77d2f7158e7629dc54acafbf65e6af90a9297132714fd4a3a6e426a89da7205e3) , [BT\_MESH\_RPR\_ERR\_LINK\_OPEN\_FAILED](#gga77d2f7158e7629dc54acafbf65e6af90aedea52611aef2a72da9f41100d17edc4) , [BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_BY\_DEVICE](#gga77d2f7158e7629dc54acafbf65e6af90a7677dece8ef7018469a30ec33b8cf9c8) , [BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_BY\_SERVER](#gga77d2f7158e7629dc54acafbf65e6af90afe2ea78fee8b23c53d462f48ba530095) ,     [BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_BY\_CLIENT](#gga77d2f7158e7629dc54acafbf65e6af90a97dd7c06604a54aa508ee044c3ad86e3) , [BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_AS\_CANNOT\_RECEIVE\_PDU](#gga77d2f7158e7629dc54acafbf65e6af90aa91b75cfc7e8ed3dde00fb727bb91943) , [BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_AS\_CANNOT\_SEND\_PDU](#gga77d2f7158e7629dc54acafbf65e6af90a5a0c58335ee0a2759de08c602d2922bb) , [BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_AS\_CANNOT\_DELIVER\_PDU\_REPORT](#gga77d2f7158e7629dc54acafbf65e6af90aed508e4f4a7f37c7804322a44037b0b4)   } |
| enum | [bt\_mesh\_rpr\_scan](#gabdc6782290a2c1652156e3f932e65291) { [BT\_MESH\_RPR\_SCAN\_IDLE](#ggabdc6782290a2c1652156e3f932e65291ad7b3cf3c950862565a8a6637448b3079) , [BT\_MESH\_RPR\_SCAN\_MULTI](#ggabdc6782290a2c1652156e3f932e65291abb2fcc52856a2cf0b4315c253c498690) , [BT\_MESH\_RPR\_SCAN\_SINGLE](#ggabdc6782290a2c1652156e3f932e65291a3e732d2c256ec0c45b30b3623354c0fd) } |
| enum | [bt\_mesh\_rpr\_node\_refresh](#gafef25a17e477638702ed742656b59573) { [BT\_MESH\_RPR\_NODE\_REFRESH\_DEVKEY](#ggafef25a17e477638702ed742656b59573a9723efd45622d3a9ba7a2ae07dddb574) , [BT\_MESH\_RPR\_NODE\_REFRESH\_ADDR](#ggafef25a17e477638702ed742656b59573a52ff469f64d554cd31ee2228c542b7bf) , [BT\_MESH\_RPR\_NODE\_REFRESH\_COMPOSITION](#ggafef25a17e477638702ed742656b59573a700c5b506c4c85d12e578c0c5e3016b6) } |
| enum | [bt\_mesh\_rpr\_link\_state](#ga0266611238d10f8e97f2b07156991f43) {     [BT\_MESH\_RPR\_LINK\_IDLE](#gga0266611238d10f8e97f2b07156991f43a73441835adf51cd7c7cf57c36d4df4fb) , [BT\_MESH\_RPR\_LINK\_OPENING](#gga0266611238d10f8e97f2b07156991f43aaf2850d86c8f176c1a00afd14f9f70a9) , [BT\_MESH\_RPR\_LINK\_ACTIVE](#gga0266611238d10f8e97f2b07156991f43a8821935b6e6ea3dcf40a81c285a19c36) , [BT\_MESH\_RPR\_LINK\_SENDING](#gga0266611238d10f8e97f2b07156991f43a6e0002cda37a86ecc1b4eb66c3b1cee7) ,     [BT\_MESH\_RPR\_LINK\_CLOSING](#gga0266611238d10f8e97f2b07156991f43a86e13d121f282d5b8e5ee7f2cd69d494)   } |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga2a5241b2e87fec227740dd4f2de3a68a)BT\_MESH\_RPR\_EXT\_SCAN\_TIME\_MAX

| #define BT\_MESH\_RPR\_EXT\_SCAN\_TIME\_MAX   21 |
| --- |

`#include <[rpr.h](rpr_8h.md)>`

Maximum extended scan duration in seconds.

## [◆ ](#ga2b7e2636da150f5c5cb4e3bdee13c745)BT\_MESH\_RPR\_EXT\_SCAN\_TIME\_MIN

| #define BT\_MESH\_RPR\_EXT\_SCAN\_TIME\_MIN   1 |
| --- |

`#include <[rpr.h](rpr_8h.md)>`

Minimum extended scan duration in seconds.

## [◆ ](#ga31bbb1483d5bdd10e0a9da0978bd90c0)BT\_MESH\_RPR\_UNPROV\_ACTIVE

| #define BT\_MESH\_RPR\_UNPROV\_ACTIVE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[rpr.h](rpr_8h.md)>`

Internal.

## [◆ ](#gac1eebae68c05d9e59599d0601055790d)BT\_MESH\_RPR\_UNPROV\_EXT

| #define BT\_MESH\_RPR\_UNPROV\_EXT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[rpr.h](rpr_8h.md)>`

Internal.

## [◆ ](#ga1dc95fc6baba79d9bc4007169fcfe55b)BT\_MESH\_RPR\_UNPROV\_EXT\_ADV\_RXD

| #define BT\_MESH\_RPR\_UNPROV\_EXT\_ADV\_RXD   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[rpr.h](rpr_8h.md)>`

Internal.

## [◆ ](#gac33ea72f94eb986592941ca10b7884f1)BT\_MESH\_RPR\_UNPROV\_FOUND

| #define BT\_MESH\_RPR\_UNPROV\_FOUND   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[rpr.h](rpr_8h.md)>`

Internal.

## [◆ ](#ga8349a9af764b3e502bf5ecd8bb0ce203)BT\_MESH\_RPR\_UNPROV\_HAS\_LINK

| #define BT\_MESH\_RPR\_UNPROV\_HAS\_LINK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[rpr.h](rpr_8h.md)>`

Internal.

## [◆ ](#ga94522cf0b3832b576100b787808474bd)BT\_MESH\_RPR\_UNPROV\_HASH

| #define BT\_MESH\_RPR\_UNPROV\_HASH   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[rpr.h](rpr_8h.md)>`

Unprovisioned device has URI hash value.

## [◆ ](#ga8121bae9a6158a5f2df4bc154237e05b)BT\_MESH\_RPR\_UNPROV\_REPORTED

| #define BT\_MESH\_RPR\_UNPROV\_REPORTED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[rpr.h](rpr_8h.md)>`

Internal.

## Enumeration Type Documentation

## [◆ ](#ga0266611238d10f8e97f2b07156991f43)bt\_mesh\_rpr\_link\_state

| enum [bt\_mesh\_rpr\_link\_state](#ga0266611238d10f8e97f2b07156991f43) |
| --- |

`#include <[rpr.h](rpr_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_MESH\_RPR\_LINK\_IDLE |  |
| BT\_MESH\_RPR\_LINK\_OPENING |  |
| BT\_MESH\_RPR\_LINK\_ACTIVE |  |
| BT\_MESH\_RPR\_LINK\_SENDING |  |
| BT\_MESH\_RPR\_LINK\_CLOSING |  |

## [◆ ](#gafef25a17e477638702ed742656b59573)bt\_mesh\_rpr\_node\_refresh

| enum [bt\_mesh\_rpr\_node\_refresh](#gafef25a17e477638702ed742656b59573) |
| --- |

`#include <[rpr.h](rpr_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_MESH\_RPR\_NODE\_REFRESH\_DEVKEY | Change the Device key. |
| BT\_MESH\_RPR\_NODE\_REFRESH\_ADDR | Change the Device key and address.  Device composition may change. |
| BT\_MESH\_RPR\_NODE\_REFRESH\_COMPOSITION | Change the Device key and composition. |

## [◆ ](#gabdc6782290a2c1652156e3f932e65291)bt\_mesh\_rpr\_scan

| enum [bt\_mesh\_rpr\_scan](#gabdc6782290a2c1652156e3f932e65291) |
| --- |

`#include <[rpr.h](rpr_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_MESH\_RPR\_SCAN\_IDLE |  |
| BT\_MESH\_RPR\_SCAN\_MULTI |  |
| BT\_MESH\_RPR\_SCAN\_SINGLE |  |

## [◆ ](#ga77d2f7158e7629dc54acafbf65e6af90)bt\_mesh\_rpr\_status

| enum [bt\_mesh\_rpr\_status](#ga77d2f7158e7629dc54acafbf65e6af90) |
| --- |

`#include <[rpr.h](rpr_8h.md)>`

| Enumerator | |
| --- | --- |
| BT\_MESH\_RPR\_SUCCESS |  |
| BT\_MESH\_RPR\_ERR\_SCANNING\_CANNOT\_START |  |
| BT\_MESH\_RPR\_ERR\_INVALID\_STATE |  |
| BT\_MESH\_RPR\_ERR\_LIMITED\_RESOURCES |  |
| BT\_MESH\_RPR\_ERR\_LINK\_CANNOT\_OPEN |  |
| BT\_MESH\_RPR\_ERR\_LINK\_OPEN\_FAILED |  |
| BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_BY\_DEVICE |  |
| BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_BY\_SERVER |  |
| BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_BY\_CLIENT |  |
| BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_AS\_CANNOT\_RECEIVE\_PDU |  |
| BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_AS\_CANNOT\_SEND\_PDU |  |
| BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_AS\_CANNOT\_DELIVER\_PDU\_REPORT |  |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
