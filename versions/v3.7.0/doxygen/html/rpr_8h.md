---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/rpr_8h.html
original_path: doxygen/html/rpr_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rpr.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/bluetooth/mesh/main.h](main_8h_source.md)>`

[Go to the source code of this file.](rpr_8h_source.md)

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
| #define | [BT\_MESH\_RPR\_UNPROV\_HASH](group__bt__mesh__rpr.md#ga94522cf0b3832b576100b787808474bd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Unprovisioned device has URI hash value. |
| #define | [BT\_MESH\_RPR\_UNPROV\_ACTIVE](group__bt__mesh__rpr.md#ga31bbb1483d5bdd10e0a9da0978bd90c0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Internal. |
| #define | [BT\_MESH\_RPR\_UNPROV\_FOUND](group__bt__mesh__rpr.md#gac33ea72f94eb986592941ca10b7884f1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Internal. |
| #define | [BT\_MESH\_RPR\_UNPROV\_REPORTED](group__bt__mesh__rpr.md#ga8121bae9a6158a5f2df4bc154237e05b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Internal. |
| #define | [BT\_MESH\_RPR\_UNPROV\_EXT](group__bt__mesh__rpr.md#gac1eebae68c05d9e59599d0601055790d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Internal. |
| #define | [BT\_MESH\_RPR\_UNPROV\_HAS\_LINK](group__bt__mesh__rpr.md#ga8349a9af764b3e502bf5ecd8bb0ce203)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Internal. |
| #define | [BT\_MESH\_RPR\_UNPROV\_EXT\_ADV\_RXD](group__bt__mesh__rpr.md#ga1dc95fc6baba79d9bc4007169fcfe55b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Internal. |
| #define | [BT\_MESH\_RPR\_EXT\_SCAN\_TIME\_MIN](group__bt__mesh__rpr.md#ga2b7e2636da150f5c5cb4e3bdee13c745)   1 |
|  | Minimum extended scan duration in seconds. |
| #define | [BT\_MESH\_RPR\_EXT\_SCAN\_TIME\_MAX](group__bt__mesh__rpr.md#ga2a5241b2e87fec227740dd4f2de3a68a)   21 |
|  | Maximum extended scan duration in seconds. |

| Enumerations | |
| --- | --- |
| enum | [bt\_mesh\_rpr\_status](group__bt__mesh__rpr.md#ga77d2f7158e7629dc54acafbf65e6af90) {     [BT\_MESH\_RPR\_SUCCESS](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a9375e568e9b69ab37484b91cfca75117) , [BT\_MESH\_RPR\_ERR\_SCANNING\_CANNOT\_START](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90aeec9abd5c000ea23fe9b7aa396f8b599) , [BT\_MESH\_RPR\_ERR\_INVALID\_STATE](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90ab5ff83c3503d6f709dfeb1423b957c26) , [BT\_MESH\_RPR\_ERR\_LIMITED\_RESOURCES](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90abb00e5ea05d585e1350d2b46d2fdda82) ,     [BT\_MESH\_RPR\_ERR\_LINK\_CANNOT\_OPEN](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a9297132714fd4a3a6e426a89da7205e3) , [BT\_MESH\_RPR\_ERR\_LINK\_OPEN\_FAILED](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90aedea52611aef2a72da9f41100d17edc4) , [BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_BY\_DEVICE](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a7677dece8ef7018469a30ec33b8cf9c8) , [BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_BY\_SERVER](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90afe2ea78fee8b23c53d462f48ba530095) ,     [BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_BY\_CLIENT](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a97dd7c06604a54aa508ee044c3ad86e3) , [BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_AS\_CANNOT\_RECEIVE\_PDU](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90aa91b75cfc7e8ed3dde00fb727bb91943) , [BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_AS\_CANNOT\_SEND\_PDU](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90a5a0c58335ee0a2759de08c602d2922bb) , [BT\_MESH\_RPR\_ERR\_LINK\_CLOSED\_AS\_CANNOT\_DELIVER\_PDU\_REPORT](group__bt__mesh__rpr.md#gga77d2f7158e7629dc54acafbf65e6af90aed508e4f4a7f37c7804322a44037b0b4)   } |
| enum | [bt\_mesh\_rpr\_scan](group__bt__mesh__rpr.md#gabdc6782290a2c1652156e3f932e65291) { [BT\_MESH\_RPR\_SCAN\_IDLE](group__bt__mesh__rpr.md#ggabdc6782290a2c1652156e3f932e65291ad7b3cf3c950862565a8a6637448b3079) , [BT\_MESH\_RPR\_SCAN\_MULTI](group__bt__mesh__rpr.md#ggabdc6782290a2c1652156e3f932e65291abb2fcc52856a2cf0b4315c253c498690) , [BT\_MESH\_RPR\_SCAN\_SINGLE](group__bt__mesh__rpr.md#ggabdc6782290a2c1652156e3f932e65291a3e732d2c256ec0c45b30b3623354c0fd) } |
| enum | [bt\_mesh\_rpr\_node\_refresh](group__bt__mesh__rpr.md#gafef25a17e477638702ed742656b59573) { [BT\_MESH\_RPR\_NODE\_REFRESH\_DEVKEY](group__bt__mesh__rpr.md#ggafef25a17e477638702ed742656b59573a9723efd45622d3a9ba7a2ae07dddb574) , [BT\_MESH\_RPR\_NODE\_REFRESH\_ADDR](group__bt__mesh__rpr.md#ggafef25a17e477638702ed742656b59573a52ff469f64d554cd31ee2228c542b7bf) , [BT\_MESH\_RPR\_NODE\_REFRESH\_COMPOSITION](group__bt__mesh__rpr.md#ggafef25a17e477638702ed742656b59573a700c5b506c4c85d12e578c0c5e3016b6) } |
| enum | [bt\_mesh\_rpr\_link\_state](group__bt__mesh__rpr.md#ga0266611238d10f8e97f2b07156991f43) {     [BT\_MESH\_RPR\_LINK\_IDLE](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43a73441835adf51cd7c7cf57c36d4df4fb) , [BT\_MESH\_RPR\_LINK\_OPENING](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43aaf2850d86c8f176c1a00afd14f9f70a9) , [BT\_MESH\_RPR\_LINK\_ACTIVE](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43a8821935b6e6ea3dcf40a81c285a19c36) , [BT\_MESH\_RPR\_LINK\_SENDING](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43a6e0002cda37a86ecc1b4eb66c3b1cee7) ,     [BT\_MESH\_RPR\_LINK\_CLOSING](group__bt__mesh__rpr.md#gga0266611238d10f8e97f2b07156991f43a86e13d121f282d5b8e5ee7f2cd69d494)   } |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [rpr.h](rpr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
