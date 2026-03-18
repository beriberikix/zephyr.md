---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/dfd_8h_source.html
original_path: doxygen/html/dfd_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dfd.h

[Go to the documentation of this file.](dfd_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_DFD\_H\_\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_DFD\_H\_\_

9

10#include <[zephyr/bluetooth/mesh.h](mesh_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

21

[ 23](group__bt__mesh__dfd.md#gaedd84b3b4bdde360c860d3cb04b301d5)enum [bt\_mesh\_dfd\_status](group__bt__mesh__dfd.md#gaedd84b3b4bdde360c860d3cb04b301d5) {

[ 25](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a681abfc930c58bfdc1fd7faecd5be60f) [BT\_MESH\_DFD\_SUCCESS](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a681abfc930c58bfdc1fd7faecd5be60f),

26

[ 28](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a7c26905cacc0746e9f0fd11c807dd9da) [BT\_MESH\_DFD\_ERR\_INSUFFICIENT\_RESOURCES](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a7c26905cacc0746e9f0fd11c807dd9da),

29

[ 33](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5adfcf93ecff8e6311e59edc738824524f) [BT\_MESH\_DFD\_ERR\_WRONG\_PHASE](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5adfcf93ecff8e6311e59edc738824524f),

34

[ 36](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a65eec1f5cc0601824736e182ea156ced) [BT\_MESH\_DFD\_ERR\_INTERNAL](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a65eec1f5cc0601824736e182ea156ced),

37

[ 39](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a566680567a9b839760eb894014a9c99e) [BT\_MESH\_DFD\_ERR\_FW\_NOT\_FOUND](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a566680567a9b839760eb894014a9c99e),

40

[ 43](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5ace8c218c64a45d321bfee5d3c56c6a65) [BT\_MESH\_DFD\_ERR\_INVALID\_APPKEY\_INDEX](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5ace8c218c64a45d321bfee5d3c56c6a65),

44

[ 48](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a0150d6c73adf0cb02dd466adbbd6879b) [BT\_MESH\_DFD\_ERR\_RECEIVERS\_LIST\_EMPTY](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a0150d6c73adf0cb02dd466adbbd6879b),

49

[ 51](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5aff40a9a0293b44032fae6e609226437a) [BT\_MESH\_DFD\_ERR\_BUSY\_WITH\_DISTRIBUTION](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5aff40a9a0293b44032fae6e609226437a),

52

[ 54](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5aaec8424606d66809dbdf00dfe085a280) [BT\_MESH\_DFD\_ERR\_BUSY\_WITH\_UPLOAD](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5aaec8424606d66809dbdf00dfe085a280),

55

[ 57](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5aac0df490cd27124e758cb5106de5af5c) [BT\_MESH\_DFD\_ERR\_URI\_NOT\_SUPPORTED](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5aac0df490cd27124e758cb5106de5af5c),

58

[ 60](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a05d5814acf74f3242403b56387da8523) [BT\_MESH\_DFD\_ERR\_URI\_MALFORMED](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a05d5814acf74f3242403b56387da8523),

61

[ 63](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5ad4f4b771ab3c826df309581a414c9256) [BT\_MESH\_DFD\_ERR\_URI\_UNREACHABLE](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5ad4f4b771ab3c826df309581a414c9256),

64

[ 66](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a560250c948218d82f30767deb730bdf7) [BT\_MESH\_DFD\_ERR\_NEW\_FW\_NOT\_AVAILABLE](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a560250c948218d82f30767deb730bdf7),

67

[ 69](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a135b4f6fbb028f17eff69f7f6bbbef3e) [BT\_MESH\_DFD\_ERR\_SUSPEND\_FAILED](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a135b4f6fbb028f17eff69f7f6bbbef3e),

70};

71

[ 73](group__bt__mesh__dfd.md#gab6562d62668ebcdb146be35b909c30c2)enum [bt\_mesh\_dfd\_phase](group__bt__mesh__dfd.md#gab6562d62668ebcdb146be35b909c30c2) {

[ 75](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2ae449e405221a66ced3dfde401a398e93) [BT\_MESH\_DFD\_PHASE\_IDLE](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2ae449e405221a66ced3dfde401a398e93),

76

[ 78](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a3b395af5b5ba7d5eb6f48230a18cd497) [BT\_MESH\_DFD\_PHASE\_TRANSFER\_ACTIVE](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a3b395af5b5ba7d5eb6f48230a18cd497),

79

[ 81](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a45896fbd956bd968e02b93baeafbd32c) [BT\_MESH\_DFD\_PHASE\_TRANSFER\_SUCCESS](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a45896fbd956bd968e02b93baeafbd32c),

82

[ 84](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2aef8954a9eaa299a178661834b0cdcadf) [BT\_MESH\_DFD\_PHASE\_APPLYING\_UPDATE](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2aef8954a9eaa299a178661834b0cdcadf),

85

[ 87](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a83ac53111b35f568e35451542b1ab817) [BT\_MESH\_DFD\_PHASE\_COMPLETED](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a83ac53111b35f568e35451542b1ab817),

88

[ 90](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a6f3bf27d5d56a7b12fb4410bc2ce02ab) [BT\_MESH\_DFD\_PHASE\_FAILED](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a6f3bf27d5d56a7b12fb4410bc2ce02ab),

91

[ 93](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a7fcb7a64a38ab8f1fa183346b2622886) [BT\_MESH\_DFD\_PHASE\_CANCELING\_UPDATE](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a7fcb7a64a38ab8f1fa183346b2622886),

94

[ 96](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2ab0427fec0c21b1de0417be100c395f46) [BT\_MESH\_DFD\_PHASE\_TRANSFER\_SUSPENDED](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2ab0427fec0c21b1de0417be100c395f46),

97};

98

[ 100](group__bt__mesh__dfd.md#ga1cce8331a0876c056b25175df32188fb)enum [bt\_mesh\_dfd\_upload\_phase](group__bt__mesh__dfd.md#ga1cce8331a0876c056b25175df32188fb) {

[ 102](group__bt__mesh__dfd.md#gga1cce8331a0876c056b25175df32188fba7d4e5bdc57606446e759c7c563afa06e) [BT\_MESH\_DFD\_UPLOAD\_PHASE\_IDLE](group__bt__mesh__dfd.md#gga1cce8331a0876c056b25175df32188fba7d4e5bdc57606446e759c7c563afa06e),

103

[ 105](group__bt__mesh__dfd.md#gga1cce8331a0876c056b25175df32188fba1e4f2505c3551bb7b36c22478c900a65) [BT\_MESH\_DFD\_UPLOAD\_PHASE\_TRANSFER\_ACTIVE](group__bt__mesh__dfd.md#gga1cce8331a0876c056b25175df32188fba1e4f2505c3551bb7b36c22478c900a65),

106

[ 109](group__bt__mesh__dfd.md#gga1cce8331a0876c056b25175df32188fbaa3c554767ecab3e601aef982bbb17d14) [BT\_MESH\_DFD\_UPLOAD\_PHASE\_TRANSFER\_ERROR](group__bt__mesh__dfd.md#gga1cce8331a0876c056b25175df32188fbaa3c554767ecab3e601aef982bbb17d14),

110

[ 114](group__bt__mesh__dfd.md#gga1cce8331a0876c056b25175df32188fbaffe3e8378ced39bcf39dd532bebb9ec0) [BT\_MESH\_DFD\_UPLOAD\_PHASE\_TRANSFER\_SUCCESS](group__bt__mesh__dfd.md#gga1cce8331a0876c056b25175df32188fbaffe3e8378ced39bcf39dd532bebb9ec0),

115};

116

118

119#ifdef \_\_cplusplus

120}

121#endif

122

123#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_DFD\_H\_\_ \*/

[bt\_mesh\_dfd\_upload\_phase](group__bt__mesh__dfd.md#ga1cce8331a0876c056b25175df32188fb)

bt\_mesh\_dfd\_upload\_phase

Firmware upload phases.

**Definition** dfd.h:100

[bt\_mesh\_dfd\_phase](group__bt__mesh__dfd.md#gab6562d62668ebcdb146be35b909c30c2)

bt\_mesh\_dfd\_phase

Firmware distribution phases.

**Definition** dfd.h:73

[bt\_mesh\_dfd\_status](group__bt__mesh__dfd.md#gaedd84b3b4bdde360c860d3cb04b301d5)

bt\_mesh\_dfd\_status

Firmware distribution status.

**Definition** dfd.h:23

[BT\_MESH\_DFD\_UPLOAD\_PHASE\_TRANSFER\_ACTIVE](group__bt__mesh__dfd.md#gga1cce8331a0876c056b25175df32188fba1e4f2505c3551bb7b36c22478c900a65)

@ BT\_MESH\_DFD\_UPLOAD\_PHASE\_TRANSFER\_ACTIVE

The Store Firmware procedure is being executed.

**Definition** dfd.h:105

[BT\_MESH\_DFD\_UPLOAD\_PHASE\_IDLE](group__bt__mesh__dfd.md#gga1cce8331a0876c056b25175df32188fba7d4e5bdc57606446e759c7c563afa06e)

@ BT\_MESH\_DFD\_UPLOAD\_PHASE\_IDLE

No firmware upload is in progress.

**Definition** dfd.h:102

[BT\_MESH\_DFD\_UPLOAD\_PHASE\_TRANSFER\_ERROR](group__bt__mesh__dfd.md#gga1cce8331a0876c056b25175df32188fbaa3c554767ecab3e601aef982bbb17d14)

@ BT\_MESH\_DFD\_UPLOAD\_PHASE\_TRANSFER\_ERROR

The Store Firmware procedure or Store Firmware OOB procedure failed.

**Definition** dfd.h:109

[BT\_MESH\_DFD\_UPLOAD\_PHASE\_TRANSFER\_SUCCESS](group__bt__mesh__dfd.md#gga1cce8331a0876c056b25175df32188fbaffe3e8378ced39bcf39dd532bebb9ec0)

@ BT\_MESH\_DFD\_UPLOAD\_PHASE\_TRANSFER\_SUCCESS

The Store Firmware procedure or the Store Firmware OOB procedure completed successfully.

**Definition** dfd.h:114

[BT\_MESH\_DFD\_PHASE\_TRANSFER\_ACTIVE](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a3b395af5b5ba7d5eb6f48230a18cd497)

@ BT\_MESH\_DFD\_PHASE\_TRANSFER\_ACTIVE

Firmware distribution is in progress.

**Definition** dfd.h:78

[BT\_MESH\_DFD\_PHASE\_TRANSFER\_SUCCESS](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a45896fbd956bd968e02b93baeafbd32c)

@ BT\_MESH\_DFD\_PHASE\_TRANSFER\_SUCCESS

The Transfer BLOB procedure has completed successfully.

**Definition** dfd.h:81

[BT\_MESH\_DFD\_PHASE\_FAILED](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a6f3bf27d5d56a7b12fb4410bc2ce02ab)

@ BT\_MESH\_DFD\_PHASE\_FAILED

The Distribute Firmware procedure has failed.

**Definition** dfd.h:90

[BT\_MESH\_DFD\_PHASE\_CANCELING\_UPDATE](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a7fcb7a64a38ab8f1fa183346b2622886)

@ BT\_MESH\_DFD\_PHASE\_CANCELING\_UPDATE

The Cancel Firmware Update procedure is being executed.

**Definition** dfd.h:93

[BT\_MESH\_DFD\_PHASE\_COMPLETED](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2a83ac53111b35f568e35451542b1ab817)

@ BT\_MESH\_DFD\_PHASE\_COMPLETED

The Distribute Firmware procedure has completed successfully.

**Definition** dfd.h:87

[BT\_MESH\_DFD\_PHASE\_TRANSFER\_SUSPENDED](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2ab0427fec0c21b1de0417be100c395f46)

@ BT\_MESH\_DFD\_PHASE\_TRANSFER\_SUSPENDED

The Transfer BLOB procedure is suspended.

**Definition** dfd.h:96

[BT\_MESH\_DFD\_PHASE\_IDLE](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2ae449e405221a66ced3dfde401a398e93)

@ BT\_MESH\_DFD\_PHASE\_IDLE

No firmware distribution is in progress.

**Definition** dfd.h:75

[BT\_MESH\_DFD\_PHASE\_APPLYING\_UPDATE](group__bt__mesh__dfd.md#ggab6562d62668ebcdb146be35b909c30c2aef8954a9eaa299a178661834b0cdcadf)

@ BT\_MESH\_DFD\_PHASE\_APPLYING\_UPDATE

The Apply Firmware on Target Nodes procedure is being executed.

**Definition** dfd.h:84

[BT\_MESH\_DFD\_ERR\_RECEIVERS\_LIST\_EMPTY](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a0150d6c73adf0cb02dd466adbbd6879b)

@ BT\_MESH\_DFD\_ERR\_RECEIVERS\_LIST\_EMPTY

There are no Target nodes in the Distribution Receivers List state.

**Definition** dfd.h:48

[BT\_MESH\_DFD\_ERR\_URI\_MALFORMED](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a05d5814acf74f3242403b56387da8523)

@ BT\_MESH\_DFD\_ERR\_URI\_MALFORMED

The format of the Update URI is invalid.

**Definition** dfd.h:60

[BT\_MESH\_DFD\_ERR\_SUSPEND\_FAILED](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a135b4f6fbb028f17eff69f7f6bbbef3e)

@ BT\_MESH\_DFD\_ERR\_SUSPEND\_FAILED

The suspension of the Distribute Firmware procedure failed.

**Definition** dfd.h:69

[BT\_MESH\_DFD\_ERR\_NEW\_FW\_NOT\_AVAILABLE](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a560250c948218d82f30767deb730bdf7)

@ BT\_MESH\_DFD\_ERR\_NEW\_FW\_NOT\_AVAILABLE

The Check Firmware OOB procedure did not find any new firmware.

**Definition** dfd.h:66

[BT\_MESH\_DFD\_ERR\_FW\_NOT\_FOUND](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a566680567a9b839760eb894014a9c99e)

@ BT\_MESH\_DFD\_ERR\_FW\_NOT\_FOUND

The requested firmware image is not stored on the Distributor.

**Definition** dfd.h:39

[BT\_MESH\_DFD\_ERR\_INTERNAL](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a65eec1f5cc0601824736e182ea156ced)

@ BT\_MESH\_DFD\_ERR\_INTERNAL

An internal error occurred on the node.

**Definition** dfd.h:36

[BT\_MESH\_DFD\_SUCCESS](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a681abfc930c58bfdc1fd7faecd5be60f)

@ BT\_MESH\_DFD\_SUCCESS

The message was processed successfully.

**Definition** dfd.h:25

[BT\_MESH\_DFD\_ERR\_INSUFFICIENT\_RESOURCES](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5a7c26905cacc0746e9f0fd11c807dd9da)

@ BT\_MESH\_DFD\_ERR\_INSUFFICIENT\_RESOURCES

Insufficient resources on the node.

**Definition** dfd.h:28

[BT\_MESH\_DFD\_ERR\_URI\_NOT\_SUPPORTED](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5aac0df490cd27124e758cb5106de5af5c)

@ BT\_MESH\_DFD\_ERR\_URI\_NOT\_SUPPORTED

The URI scheme name indicated by the Update URI is not supported.

**Definition** dfd.h:57

[BT\_MESH\_DFD\_ERR\_BUSY\_WITH\_UPLOAD](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5aaec8424606d66809dbdf00dfe085a280)

@ BT\_MESH\_DFD\_ERR\_BUSY\_WITH\_UPLOAD

Another upload is in progress.

**Definition** dfd.h:54

[BT\_MESH\_DFD\_ERR\_INVALID\_APPKEY\_INDEX](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5ace8c218c64a45d321bfee5d3c56c6a65)

@ BT\_MESH\_DFD\_ERR\_INVALID\_APPKEY\_INDEX

The AppKey identified by the AppKey Index is not known to the node.

**Definition** dfd.h:43

[BT\_MESH\_DFD\_ERR\_URI\_UNREACHABLE](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5ad4f4b771ab3c826df309581a414c9256)

@ BT\_MESH\_DFD\_ERR\_URI\_UNREACHABLE

The URI is currently unreachable.

**Definition** dfd.h:63

[BT\_MESH\_DFD\_ERR\_WRONG\_PHASE](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5adfcf93ecff8e6311e59edc738824524f)

@ BT\_MESH\_DFD\_ERR\_WRONG\_PHASE

The operation cannot be performed while the Server is in the current phase.

**Definition** dfd.h:33

[BT\_MESH\_DFD\_ERR\_BUSY\_WITH\_DISTRIBUTION](group__bt__mesh__dfd.md#ggaedd84b3b4bdde360c860d3cb04b301d5aff40a9a0293b44032fae6e609226437a)

@ BT\_MESH\_DFD\_ERR\_BUSY\_WITH\_DISTRIBUTION

Another firmware image distribution is in progress.

**Definition** dfd.h:51

[mesh.h](mesh_8h.md)

Bluetooth Mesh Profile APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [dfd.h](dfd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
