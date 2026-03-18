---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dfd_8h.html
original_path: doxygen/html/dfd_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dfd.h File Reference

`#include <[zephyr/bluetooth/mesh.h](mesh_8h_source.md)>`

[Go to the source code of this file.](dfd_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [bt\_mesh\_dfd\_status](group__bt__mesh__dfd.md#gaedd84b3b4bdde360c860d3cb04b301d5) {     [BT\_MESH\_DFD\_SUCCESS](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a681abfc930c58bfdc1fd7faecd5be60f) , [BT\_MESH\_DFD\_ERR\_INSUFFICIENT\_RESOURCES](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a7c26905cacc0746e9f0fd11c807dd9da) , [BT\_MESH\_DFD\_ERR\_WRONG\_PHASE](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5adfcf93ecff8e6311e59edc738824524f) , [BT\_MESH\_DFD\_ERR\_INTERNAL](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a65eec1f5cc0601824736e182ea156ced) ,     [BT\_MESH\_DFD\_ERR\_FW\_NOT\_FOUND](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a566680567a9b839760eb894014a9c99e) , [BT\_MESH\_DFD\_ERR\_INVALID\_APPKEY\_INDEX](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5ace8c218c64a45d321bfee5d3c56c6a65) , [BT\_MESH\_DFD\_ERR\_RECEIVERS\_LIST\_EMPTY](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a0150d6c73adf0cb02dd466adbbd6879b) , [BT\_MESH\_DFD\_ERR\_BUSY\_WITH\_DISTRIBUTION](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5aff40a9a0293b44032fae6e609226437a) ,     [BT\_MESH\_DFD\_ERR\_BUSY\_WITH\_UPLOAD](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5aaec8424606d66809dbdf00dfe085a280) , [BT\_MESH\_DFD\_ERR\_URI\_NOT\_SUPPORTED](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5aac0df490cd27124e758cb5106de5af5c) , [BT\_MESH\_DFD\_ERR\_URI\_MALFORMED](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a05d5814acf74f3242403b56387da8523) , [BT\_MESH\_DFD\_ERR\_URI\_UNREACHABLE](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5ad4f4b771ab3c826df309581a414c9256) ,     [BT\_MESH\_DFD\_ERR\_NEW\_FW\_NOT\_AVAILABLE](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a560250c948218d82f30767deb730bdf7) , [BT\_MESH\_DFD\_ERR\_SUSPEND\_FAILED](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a135b4f6fbb028f17eff69f7f6bbbef3e)   } |
|  | Firmware distribution status. [More...](group__bt__mesh__dfd.md#gaedd84b3b4bdde360c860d3cb04b301d5) |
| enum | [bt\_mesh\_dfd\_phase](group__bt__mesh__dfd.md#gab6562d62668ebcdb146be35b909c30c2) {     [BT\_MESH\_DFD\_PHASE\_IDLE](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2ae449e405221a66ced3dfde401a398e93) , [BT\_MESH\_DFD\_PHASE\_TRANSFER\_ACTIVE](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a3b395af5b5ba7d5eb6f48230a18cd497) , [BT\_MESH\_DFD\_PHASE\_TRANSFER\_SUCCESS](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a45896fbd956bd968e02b93baeafbd32c) , [BT\_MESH\_DFD\_PHASE\_APPLYING\_UPDATE](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2aef8954a9eaa299a178661834b0cdcadf) ,     [BT\_MESH\_DFD\_PHASE\_COMPLETED](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a83ac53111b35f568e35451542b1ab817) , [BT\_MESH\_DFD\_PHASE\_FAILED](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a6f3bf27d5d56a7b12fb4410bc2ce02ab) , [BT\_MESH\_DFD\_PHASE\_CANCELING\_UPDATE](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a7fcb7a64a38ab8f1fa183346b2622886) , [BT\_MESH\_DFD\_PHASE\_TRANSFER\_SUSPENDED](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2ab0427fec0c21b1de0417be100c395f46)   } |
|  | Firmware distribution phases. [More...](group__bt__mesh__dfd.md#gab6562d62668ebcdb146be35b909c30c2) |
| enum | [bt\_mesh\_dfd\_upload\_phase](group__bt__mesh__dfd.md#ga1cce8331a0876c056b25175df32188fb) { [BT\_MESH\_DFD\_UPLOAD\_PHASE\_IDLE](group__bt__mesh__dfd.md#gga1cce8331a0876c056b25175df32188fba7d4e5bdc57606446e759c7c563afa06e) , [BT\_MESH\_DFD\_UPLOAD\_PHASE\_TRANSFER\_ACTIVE](group__bt__mesh__dfd.md#gga1cce8331a0876c056b25175df32188fba1e4f2505c3551bb7b36c22478c900a65) , [BT\_MESH\_DFD\_UPLOAD\_PHASE\_TRANSFER\_ERROR](group__bt__mesh__dfd.md#gga1cce8331a0876c056b25175df32188fbaa3c554767ecab3e601aef982bbb17d14) , [BT\_MESH\_DFD\_UPLOAD\_PHASE\_TRANSFER\_SUCCESS](group__bt__mesh__dfd.md#gga1cce8331a0876c056b25175df32188fbaffe3e8378ced39bcf39dd532bebb9ec0) } |
|  | Firmware upload phases. [More...](group__bt__mesh__dfd.md#ga1cce8331a0876c056b25175df32188fb) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [dfd.h](dfd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
