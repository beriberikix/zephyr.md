---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__mesh__dfd.html
original_path: doxygen/html/group__bt__mesh__dfd.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Firmware Distribution models

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

| Topics | |
| --- | --- |
|  | [Firmware Distribution Server model](group__bt__mesh__dfd__srv.md) |
|  | API for the Firmware Distribution Server model. |

| Enumerations | |
| --- | --- |
| enum | [bt\_mesh\_dfd\_status](#gaedd84b3b4bdde360c860d3cb04b301d5) {     [BT\_MESH\_DFD\_SUCCESS](#ggaedd84b3b4bdde360c860d3cb04b301d5a681abfc930c58bfdc1fd7faecd5be60f) , [BT\_MESH\_DFD\_ERR\_INSUFFICIENT\_RESOURCES](#ggaedd84b3b4bdde360c860d3cb04b301d5a7c26905cacc0746e9f0fd11c807dd9da) , [BT\_MESH\_DFD\_ERR\_WRONG\_PHASE](#ggaedd84b3b4bdde360c860d3cb04b301d5adfcf93ecff8e6311e59edc738824524f) , [BT\_MESH\_DFD\_ERR\_INTERNAL](#ggaedd84b3b4bdde360c860d3cb04b301d5a65eec1f5cc0601824736e182ea156ced) ,     [BT\_MESH\_DFD\_ERR\_FW\_NOT\_FOUND](#ggaedd84b3b4bdde360c860d3cb04b301d5a566680567a9b839760eb894014a9c99e) , [BT\_MESH\_DFD\_ERR\_INVALID\_APPKEY\_INDEX](#ggaedd84b3b4bdde360c860d3cb04b301d5ace8c218c64a45d321bfee5d3c56c6a65) , [BT\_MESH\_DFD\_ERR\_RECEIVERS\_LIST\_EMPTY](#ggaedd84b3b4bdde360c860d3cb04b301d5a0150d6c73adf0cb02dd466adbbd6879b) , [BT\_MESH\_DFD\_ERR\_BUSY\_WITH\_DISTRIBUTION](#ggaedd84b3b4bdde360c860d3cb04b301d5aff40a9a0293b44032fae6e609226437a) ,     [BT\_MESH\_DFD\_ERR\_BUSY\_WITH\_UPLOAD](#ggaedd84b3b4bdde360c860d3cb04b301d5aaec8424606d66809dbdf00dfe085a280) , [BT\_MESH\_DFD\_ERR\_URI\_NOT\_SUPPORTED](#ggaedd84b3b4bdde360c860d3cb04b301d5aac0df490cd27124e758cb5106de5af5c) , [BT\_MESH\_DFD\_ERR\_URI\_MALFORMED](#ggaedd84b3b4bdde360c860d3cb04b301d5a05d5814acf74f3242403b56387da8523) , [BT\_MESH\_DFD\_ERR\_URI\_UNREACHABLE](#ggaedd84b3b4bdde360c860d3cb04b301d5ad4f4b771ab3c826df309581a414c9256) ,     [BT\_MESH\_DFD\_ERR\_NEW\_FW\_NOT\_AVAILABLE](#ggaedd84b3b4bdde360c860d3cb04b301d5a560250c948218d82f30767deb730bdf7) , [BT\_MESH\_DFD\_ERR\_SUSPEND\_FAILED](#ggaedd84b3b4bdde360c860d3cb04b301d5a135b4f6fbb028f17eff69f7f6bbbef3e)   } |
|  | Firmware distribution status. [More...](#gaedd84b3b4bdde360c860d3cb04b301d5) |
| enum | [bt\_mesh\_dfd\_phase](#gab6562d62668ebcdb146be35b909c30c2) {     [BT\_MESH\_DFD\_PHASE\_IDLE](#ggab6562d62668ebcdb146be35b909c30c2ae449e405221a66ced3dfde401a398e93) , [BT\_MESH\_DFD\_PHASE\_TRANSFER\_ACTIVE](#ggab6562d62668ebcdb146be35b909c30c2a3b395af5b5ba7d5eb6f48230a18cd497) , [BT\_MESH\_DFD\_PHASE\_TRANSFER\_SUCCESS](#ggab6562d62668ebcdb146be35b909c30c2a45896fbd956bd968e02b93baeafbd32c) , [BT\_MESH\_DFD\_PHASE\_APPLYING\_UPDATE](#ggab6562d62668ebcdb146be35b909c30c2aef8954a9eaa299a178661834b0cdcadf) ,     [BT\_MESH\_DFD\_PHASE\_COMPLETED](#ggab6562d62668ebcdb146be35b909c30c2a83ac53111b35f568e35451542b1ab817) , [BT\_MESH\_DFD\_PHASE\_FAILED](#ggab6562d62668ebcdb146be35b909c30c2a6f3bf27d5d56a7b12fb4410bc2ce02ab) , [BT\_MESH\_DFD\_PHASE\_CANCELING\_UPDATE](#ggab6562d62668ebcdb146be35b909c30c2a7fcb7a64a38ab8f1fa183346b2622886) , [BT\_MESH\_DFD\_PHASE\_TRANSFER\_SUSPENDED](#ggab6562d62668ebcdb146be35b909c30c2ab0427fec0c21b1de0417be100c395f46)   } |
|  | Firmware distribution phases. [More...](#gab6562d62668ebcdb146be35b909c30c2) |
| enum | [bt\_mesh\_dfd\_upload\_phase](#ga1cce8331a0876c056b25175df32188fb) { [BT\_MESH\_DFD\_UPLOAD\_PHASE\_IDLE](#gga1cce8331a0876c056b25175df32188fba7d4e5bdc57606446e759c7c563afa06e) , [BT\_MESH\_DFD\_UPLOAD\_PHASE\_TRANSFER\_ACTIVE](#gga1cce8331a0876c056b25175df32188fba1e4f2505c3551bb7b36c22478c900a65) , [BT\_MESH\_DFD\_UPLOAD\_PHASE\_TRANSFER\_ERROR](#gga1cce8331a0876c056b25175df32188fbaa3c554767ecab3e601aef982bbb17d14) , [BT\_MESH\_DFD\_UPLOAD\_PHASE\_TRANSFER\_SUCCESS](#gga1cce8331a0876c056b25175df32188fbaffe3e8378ced39bcf39dd532bebb9ec0) } |
|  | Firmware upload phases. [More...](#ga1cce8331a0876c056b25175df32188fb) |

## Detailed Description

## Enumeration Type Documentation

## [◆ ](#gab6562d62668ebcdb146be35b909c30c2)bt\_mesh\_dfd\_phase

| enum [bt\_mesh\_dfd\_phase](#gab6562d62668ebcdb146be35b909c30c2) |
| --- |

`#include <[dfd.h](dfd_8h.md)>`

Firmware distribution phases.

| Enumerator | |
| --- | --- |
| BT\_MESH\_DFD\_PHASE\_IDLE | No firmware distribution is in progress. |
| BT\_MESH\_DFD\_PHASE\_TRANSFER\_ACTIVE | Firmware distribution is in progress. |
| BT\_MESH\_DFD\_PHASE\_TRANSFER\_SUCCESS | The Transfer BLOB procedure has completed successfully. |
| BT\_MESH\_DFD\_PHASE\_APPLYING\_UPDATE | The Apply Firmware on Target Nodes procedure is being executed. |
| BT\_MESH\_DFD\_PHASE\_COMPLETED | The Distribute Firmware procedure has completed successfully. |
| BT\_MESH\_DFD\_PHASE\_FAILED | The Distribute Firmware procedure has failed. |
| BT\_MESH\_DFD\_PHASE\_CANCELING\_UPDATE | The Cancel Firmware Update procedure is being executed. |
| BT\_MESH\_DFD\_PHASE\_TRANSFER\_SUSPENDED | The Transfer BLOB procedure is suspended. |

## [◆ ](#gaedd84b3b4bdde360c860d3cb04b301d5)bt\_mesh\_dfd\_status

| enum [bt\_mesh\_dfd\_status](#gaedd84b3b4bdde360c860d3cb04b301d5) |
| --- |

`#include <[dfd.h](dfd_8h.md)>`

Firmware distribution status.

| Enumerator | |
| --- | --- |
| BT\_MESH\_DFD\_SUCCESS | The message was processed successfully. |
| BT\_MESH\_DFD\_ERR\_INSUFFICIENT\_RESOURCES | Insufficient resources on the node. |
| BT\_MESH\_DFD\_ERR\_WRONG\_PHASE | The operation cannot be performed while the Server is in the current phase. |
| BT\_MESH\_DFD\_ERR\_INTERNAL | An internal error occurred on the node. |
| BT\_MESH\_DFD\_ERR\_FW\_NOT\_FOUND | The requested firmware image is not stored on the Distributor. |
| BT\_MESH\_DFD\_ERR\_INVALID\_APPKEY\_INDEX | The AppKey identified by the AppKey Index is not known to the node. |
| BT\_MESH\_DFD\_ERR\_RECEIVERS\_LIST\_EMPTY | There are no Target nodes in the Distribution Receivers List state. |
| BT\_MESH\_DFD\_ERR\_BUSY\_WITH\_DISTRIBUTION | Another firmware image distribution is in progress. |
| BT\_MESH\_DFD\_ERR\_BUSY\_WITH\_UPLOAD | Another upload is in progress. |
| BT\_MESH\_DFD\_ERR\_URI\_NOT\_SUPPORTED | The URI scheme name indicated by the Update URI is not supported. |
| BT\_MESH\_DFD\_ERR\_URI\_MALFORMED | The format of the Update URI is invalid. |
| BT\_MESH\_DFD\_ERR\_URI\_UNREACHABLE | The URI is currently unreachable. |
| BT\_MESH\_DFD\_ERR\_NEW\_FW\_NOT\_AVAILABLE | The Check Firmware OOB procedure did not find any new firmware. |
| BT\_MESH\_DFD\_ERR\_SUSPEND\_FAILED | The suspension of the Distribute Firmware procedure failed. |

## [◆ ](#ga1cce8331a0876c056b25175df32188fb)bt\_mesh\_dfd\_upload\_phase

| enum [bt\_mesh\_dfd\_upload\_phase](#ga1cce8331a0876c056b25175df32188fb) |
| --- |

`#include <[dfd.h](dfd_8h.md)>`

Firmware upload phases.

| Enumerator | |
| --- | --- |
| BT\_MESH\_DFD\_UPLOAD\_PHASE\_IDLE | No firmware upload is in progress. |
| BT\_MESH\_DFD\_UPLOAD\_PHASE\_TRANSFER\_ACTIVE | The Store Firmware procedure is being executed. |
| BT\_MESH\_DFD\_UPLOAD\_PHASE\_TRANSFER\_ERROR | The Store Firmware procedure or Store Firmware OOB procedure failed. |
| BT\_MESH\_DFD\_UPLOAD\_PHASE\_TRANSFER\_SUCCESS | The Store Firmware procedure or the Store Firmware OOB procedure completed successfully. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
