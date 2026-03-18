---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/espi_8h_source.html
original_path: doxygen/html/espi_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

espi.h

[Go to the documentation of this file.](espi_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_ESPI\_H\_

13#define ZEPHYR\_INCLUDE\_ESPI\_H\_

14

15#include <[errno.h](errno_8h.md)>

16

17#include <[zephyr/sys/\_\_assert.h](____assert_8h.md)>

18#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

19#include <[zephyr/device.h](device_8h.md)>

20#include <[zephyr/sys/slist.h](slist_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

32

[ 36](group__espi__interface.md#ga0d7c61f1f4ec611d0c8a67ba73e2b4f0)enum [espi\_io\_mode](group__espi__interface.md#ga0d7c61f1f4ec611d0c8a67ba73e2b4f0) {

[ 37](group__espi__interface.md#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a9f47188ebd9bb4cb6e426d0bc0b6595c) [ESPI\_IO\_MODE\_SINGLE\_LINE](group__espi__interface.md#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a9f47188ebd9bb4cb6e426d0bc0b6595c) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 38](group__espi__interface.md#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0af766582d28d16af7c5aff6372e4ee243) [ESPI\_IO\_MODE\_DUAL\_LINES](group__espi__interface.md#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0af766582d28d16af7c5aff6372e4ee243) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 39](group__espi__interface.md#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a87e70bb0f5c4f6a3a21ca1bcfa4540fc) [ESPI\_IO\_MODE\_QUAD\_LINES](group__espi__interface.md#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a87e70bb0f5c4f6a3a21ca1bcfa4540fc) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

40};

41

91

[ 102](group__espi__interface.md#gafaa3f7d54503c901ab23bd79a7f8a755)enum [espi\_channel](group__espi__interface.md#gafaa3f7d54503c901ab23bd79a7f8a755) {

[ 103](group__espi__interface.md#ggafaa3f7d54503c901ab23bd79a7f8a755a32f636bbad2618a6b1554656d3b53206) [ESPI\_CHANNEL\_PERIPHERAL](group__espi__interface.md#ggafaa3f7d54503c901ab23bd79a7f8a755a32f636bbad2618a6b1554656d3b53206) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 104](group__espi__interface.md#ggafaa3f7d54503c901ab23bd79a7f8a755ac2e84a127870ff50359cf96528c9a7c6) [ESPI\_CHANNEL\_VWIRE](group__espi__interface.md#ggafaa3f7d54503c901ab23bd79a7f8a755ac2e84a127870ff50359cf96528c9a7c6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 105](group__espi__interface.md#ggafaa3f7d54503c901ab23bd79a7f8a755a0ccb80544cbda501cc90ea0c3b868e54) [ESPI\_CHANNEL\_OOB](group__espi__interface.md#ggafaa3f7d54503c901ab23bd79a7f8a755a0ccb80544cbda501cc90ea0c3b868e54) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 106](group__espi__interface.md#ggafaa3f7d54503c901ab23bd79a7f8a755a5616bf2bf49a8c457fcc2f27d9fe0518) [ESPI\_CHANNEL\_FLASH](group__espi__interface.md#ggafaa3f7d54503c901ab23bd79a7f8a755a5616bf2bf49a8c457fcc2f27d9fe0518) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

107};

108

[ 114](group__espi__interface.md#ga36ac3fbf9813f78bad90f047e1eb1128)enum [espi\_bus\_event](group__espi__interface.md#ga36ac3fbf9813f78bad90f047e1eb1128) {

[ 115](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128ae6d4d43eded0d8a368c90ea653a60956) [ESPI\_BUS\_RESET](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128ae6d4d43eded0d8a368c90ea653a60956) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 116](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128a996aee0a8f8ba0cead11cea0d39d2973) [ESPI\_BUS\_EVENT\_CHANNEL\_READY](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128a996aee0a8f8ba0cead11cea0d39d2973) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

[ 117](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128aa09f7dcd4b2d3addfaddbad5b8f2e5a2) [ESPI\_BUS\_EVENT\_VWIRE\_RECEIVED](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128aa09f7dcd4b2d3addfaddbad5b8f2e5a2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2),

[ 118](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128a3b5e529d1d0ba11c59172ab01c30e203) [ESPI\_BUS\_EVENT\_OOB\_RECEIVED](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128a3b5e529d1d0ba11c59172ab01c30e203) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3),

[ 119](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128a9ac837699f302bd10332814c7014adea) [ESPI\_BUS\_PERIPHERAL\_NOTIFICATION](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128a9ac837699f302bd10332814c7014adea) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4),

[ 120](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128a8bd46c68d9aa33c42aa098110b6f0ae4) [ESPI\_BUS\_SAF\_NOTIFICATION](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128a8bd46c68d9aa33c42aa098110b6f0ae4) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5),

121};

122

[ 128](group__espi__interface.md#gac55098842dd9d181144ac4b4122a610e)enum [espi\_pc\_event](group__espi__interface.md#gac55098842dd9d181144ac4b4122a610e) {

[ 129](group__espi__interface.md#ggac55098842dd9d181144ac4b4122a610ea68ecb52b04ffddcc93fbcc77d3643687) [ESPI\_PC\_EVT\_BUS\_CHANNEL\_READY](group__espi__interface.md#ggac55098842dd9d181144ac4b4122a610ea68ecb52b04ffddcc93fbcc77d3643687) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 130](group__espi__interface.md#ggac55098842dd9d181144ac4b4122a610ea0e245cbeef479218d4e6c9bec57e40d1) [ESPI\_PC\_EVT\_BUS\_MASTER\_ENABLE](group__espi__interface.md#ggac55098842dd9d181144ac4b4122a610ea0e245cbeef479218d4e6c9bec57e40d1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

131};

132

137#define ESPI\_PERIPHERAL\_INDEX\_0 0ul

138#define ESPI\_PERIPHERAL\_INDEX\_1 1ul

139#define ESPI\_PERIPHERAL\_INDEX\_2 2ul

140

141#define ESPI\_SLAVE\_TO\_MASTER 0ul

142#define ESPI\_MASTER\_TO\_SLAVE 1ul

143

144#define ESPI\_VWIRE\_SRC\_ID0 0ul

145#define ESPI\_VWIRE\_SRC\_ID1 1ul

146#define ESPI\_VWIRE\_SRC\_ID2 2ul

147#define ESPI\_VWIRE\_SRC\_ID3 3ul

148#define ESPI\_VWIRE\_SRC\_ID\_MAX 4ul

149

150#define ESPI\_PERIPHERAL\_NODATA 0ul

151

152#define E8042\_START\_OPCODE 0x50

153#define E8042\_MAX\_OPCODE 0x5F

154

155#define EACPI\_START\_OPCODE 0x60

156#define EACPI\_MAX\_OPCODE 0x6F

157

158#define ECUSTOM\_START\_OPCODE 0xF0

159#define ECUSTOM\_MAX\_OPCODE 0xFF

160

162

[ 169](group__espi__interface.md#ga2629a5518a94f031419eeccd05f07373)enum [espi\_virtual\_peripheral](group__espi__interface.md#ga2629a5518a94f031419eeccd05f07373) {

[ 170](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373a24478711945fd5258d8ca86bbb79b867) [ESPI\_PERIPHERAL\_UART](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373a24478711945fd5258d8ca86bbb79b867),

[ 171](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373aaea75bb5ab8a5ff31dd6b8787f44df30) [ESPI\_PERIPHERAL\_8042\_KBC](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373aaea75bb5ab8a5ff31dd6b8787f44df30),

[ 172](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373a8948a6f18bfbe87859a529d5f6e669b8) [ESPI\_PERIPHERAL\_HOST\_IO](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373a8948a6f18bfbe87859a529d5f6e669b8),

[ 173](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373af51b7171cf6085fa7946333ff32fe2f0) [ESPI\_PERIPHERAL\_DEBUG\_PORT80](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373af51b7171cf6085fa7946333ff32fe2f0),

[ 174](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373aa217b4786d7b8bacbaa4ec740550e71e) [ESPI\_PERIPHERAL\_HOST\_IO\_PVT](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373aa217b4786d7b8bacbaa4ec740550e71e),

175#if defined(CONFIG\_ESPI\_PERIPHERAL\_EC\_HOST\_CMD)

176 ESPI\_PERIPHERAL\_EC\_HOST\_CMD,

177#endif /\* CONFIG\_ESPI\_PERIPHERAL\_EC\_HOST\_CMD \*/

178};

179

[ 183](group__espi__interface.md#ga3e52615f244d7fa8ccda495ab8ec8a5b)enum [espi\_cycle\_type](group__espi__interface.md#ga3e52615f244d7fa8ccda495ab8ec8a5b) {

[ 184](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba5b480e093a58849d4181bba22d5868a5) [ESPI\_CYCLE\_MEMORY\_READ32](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba5b480e093a58849d4181bba22d5868a5),

[ 185](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5bac8ec7673b4466b278dfb5e468f7a4d79) [ESPI\_CYCLE\_MEMORY\_READ64](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5bac8ec7673b4466b278dfb5e468f7a4d79),

[ 186](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba2e5a736cf8a63491ee13d51ae4f8f073) [ESPI\_CYCLE\_MEMORY\_WRITE32](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba2e5a736cf8a63491ee13d51ae4f8f073),

[ 187](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba54c11e63fcfe3f859af57e65af3f31f7) [ESPI\_CYCLE\_MEMORY\_WRITE64](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba54c11e63fcfe3f859af57e65af3f31f7),

[ 188](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba5f2ae0575ca4e9b61c0acd7d4f08ee82) [ESPI\_CYCLE\_MESSAGE\_NODATA](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba5f2ae0575ca4e9b61c0acd7d4f08ee82),

[ 189](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba380e3d4e6b5579c8bb94e792fcb7d71f) [ESPI\_CYCLE\_MESSAGE\_DATA](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba380e3d4e6b5579c8bb94e792fcb7d71f),

[ 190](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba0335f2d34fab46960939e2d2c1c12e3f) [ESPI\_CYCLE\_OK\_COMPLETION\_NODATA](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba0335f2d34fab46960939e2d2c1c12e3f),

[ 191](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5baf3dbc2bcc0ed883bc4d4160c21e6934f) [ESPI\_CYCLE\_OKCOMPLETION\_DATA](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5baf3dbc2bcc0ed883bc4d4160c21e6934f),

[ 192](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba0edb306e5fabcbf8b009375cde6a8a2b) [ESPI\_CYCLE\_NOK\_COMPLETION\_NODATA](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba0edb306e5fabcbf8b009375cde6a8a2b),

193};

194

[ 199](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35)enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) {

200 /\* Virtual wires that can only be send from master to slave \*/

[ 201](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ab880a7156e489d5f7b8f78550e72b166) [ESPI\_VWIRE\_SIGNAL\_SLP\_S3](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ab880a7156e489d5f7b8f78550e72b166),

[ 202](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a4ef1fe12bd09be0875864d6c32164f73) [ESPI\_VWIRE\_SIGNAL\_SLP\_S4](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a4ef1fe12bd09be0875864d6c32164f73),

[ 203](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ac4b4e30c097a4ef49f21549a799e1e13) [ESPI\_VWIRE\_SIGNAL\_SLP\_S5](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ac4b4e30c097a4ef49f21549a799e1e13),

[ 204](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a2f3f97b51b750050cd98e887e39431d1) [ESPI\_VWIRE\_SIGNAL\_OOB\_RST\_WARN](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a2f3f97b51b750050cd98e887e39431d1),

[ 205](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a0bafcd0bb7f592f0e308dcfce39bcd08) [ESPI\_VWIRE\_SIGNAL\_PLTRST](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a0bafcd0bb7f592f0e308dcfce39bcd08),

[ 206](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a0e13f250ba0c5a37451c7f3b0e98e663) [ESPI\_VWIRE\_SIGNAL\_SUS\_STAT](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a0e13f250ba0c5a37451c7f3b0e98e663),

[ 207](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ad14b4b7a25141346bfefc507c588a238) [ESPI\_VWIRE\_SIGNAL\_NMIOUT](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ad14b4b7a25141346bfefc507c588a238),

[ 208](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a1d54a71c6d2e52cb66cfaa0b55b61152) [ESPI\_VWIRE\_SIGNAL\_SMIOUT](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a1d54a71c6d2e52cb66cfaa0b55b61152),

[ 209](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35af44250de6f60eabf9b0d85b8860ac56e) [ESPI\_VWIRE\_SIGNAL\_HOST\_RST\_WARN](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35af44250de6f60eabf9b0d85b8860ac56e),

[ 210](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aa4c8c69475b48d88302066823d2f3592) [ESPI\_VWIRE\_SIGNAL\_SLP\_A](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aa4c8c69475b48d88302066823d2f3592),

[ 211](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ab4f0bedd5717660cc8cac2d85c6c3d18) [ESPI\_VWIRE\_SIGNAL\_SUS\_PWRDN\_ACK](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ab4f0bedd5717660cc8cac2d85c6c3d18),

[ 212](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a9e32eee077aaa1668c356fe1d4ab1cc5) [ESPI\_VWIRE\_SIGNAL\_SUS\_WARN](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a9e32eee077aaa1668c356fe1d4ab1cc5),

[ 213](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a3d95f095ae41bba9ef916fc68ddd4779) [ESPI\_VWIRE\_SIGNAL\_SLP\_WLAN](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a3d95f095ae41bba9ef916fc68ddd4779),

[ 214](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aba8b891a643ca567966d091963be4615) [ESPI\_VWIRE\_SIGNAL\_SLP\_LAN](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aba8b891a643ca567966d091963be4615),

[ 215](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ab9deb0dd6d4e878eff6413ddc34bb36c) [ESPI\_VWIRE\_SIGNAL\_HOST\_C10](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ab9deb0dd6d4e878eff6413ddc34bb36c),

[ 216](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a923f3e602d9f8ac821ece2a625183146) [ESPI\_VWIRE\_SIGNAL\_DNX\_WARN](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a923f3e602d9f8ac821ece2a625183146),

217 /\* Virtual wires that can only be sent from slave to master \*/

[ 218](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aa87af5b5de184238e5f371851aaee692) [ESPI\_VWIRE\_SIGNAL\_PME](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aa87af5b5de184238e5f371851aaee692),

[ 219](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a736724f8229aebc356c2720a34a0143f) [ESPI\_VWIRE\_SIGNAL\_WAKE](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a736724f8229aebc356c2720a34a0143f),

[ 220](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a8e15df6f8159b4c275dc4b20aaec352e) [ESPI\_VWIRE\_SIGNAL\_OOB\_RST\_ACK](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a8e15df6f8159b4c275dc4b20aaec352e),

[ 221](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ae47cb1e53323e2fd42d7f40c21cd583d) [ESPI\_VWIRE\_SIGNAL\_SLV\_BOOT\_STS](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ae47cb1e53323e2fd42d7f40c21cd583d),

[ 222](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a504ae332b89262f70a0bf1a9c8b6f527) [ESPI\_VWIRE\_SIGNAL\_ERR\_NON\_FATAL](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a504ae332b89262f70a0bf1a9c8b6f527),

[ 223](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aae0a3fd882c5765db33a4e7bd05e1ab1) [ESPI\_VWIRE\_SIGNAL\_ERR\_FATAL](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aae0a3fd882c5765db33a4e7bd05e1ab1),

[ 224](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aa90439bef2746a982cac6eb3ea2c515d) [ESPI\_VWIRE\_SIGNAL\_SLV\_BOOT\_DONE](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aa90439bef2746a982cac6eb3ea2c515d),

[ 225](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a89420628ae26df4c45ef7fba04a3a85e) [ESPI\_VWIRE\_SIGNAL\_HOST\_RST\_ACK](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a89420628ae26df4c45ef7fba04a3a85e),

[ 226](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a19c40230e0bb4cee7b6ee42580c28a8d) [ESPI\_VWIRE\_SIGNAL\_RST\_CPU\_INIT](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a19c40230e0bb4cee7b6ee42580c28a8d),

227 /\* System management interrupt \*/

[ 228](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a2d9b2eef499d1bfd13bec1d2caa0e2f3) [ESPI\_VWIRE\_SIGNAL\_SMI](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a2d9b2eef499d1bfd13bec1d2caa0e2f3),

229 /\* System control interrupt \*/

[ 230](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35afa1f99a7e45b306c6736888e280f527c) [ESPI\_VWIRE\_SIGNAL\_SCI](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35afa1f99a7e45b306c6736888e280f527c),

[ 231](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a58280c68c980476aabefa16e0509dd1c) [ESPI\_VWIRE\_SIGNAL\_DNX\_ACK](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a58280c68c980476aabefa16e0509dd1c),

[ 232](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35abe28432b566619d8c6cce5e5034e5333) [ESPI\_VWIRE\_SIGNAL\_SUS\_ACK](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35abe28432b566619d8c6cce5e5034e5333),

233 /\*

234 \* Virtual wire GPIOs that can be sent from slave to master for

235 \* platform specific usage.

236 \*/

[ 237](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a7e7d23a32779cc3a786cc17e97bed167) [ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_0](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a7e7d23a32779cc3a786cc17e97bed167),

[ 238](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a66e16dfc37e6c1f3d09ee4b5abc4264e) [ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_1](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a66e16dfc37e6c1f3d09ee4b5abc4264e),

[ 239](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a3f4ee544ee9319d1ea4f59c25b5ab978) [ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_2](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a3f4ee544ee9319d1ea4f59c25b5ab978),

[ 240](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aa3bf67d616ea21733b1b7a4bc8ecf671) [ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_3](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aa3bf67d616ea21733b1b7a4bc8ecf671),

[ 241](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a8a68fbaffa51abdd858b72c6e59e89ba) [ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_4](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a8a68fbaffa51abdd858b72c6e59e89ba),

[ 242](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a491455d416d15d3a9009094afb96198f) [ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_5](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a491455d416d15d3a9009094afb96198f),

[ 243](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ae72c7e72a3ec597027040bf676e6e85e) [ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_6](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ae72c7e72a3ec597027040bf676e6e85e),

[ 244](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aad603524796723906f74b14ddd0c3761) [ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_7](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aad603524796723906f74b14ddd0c3761),

[ 245](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ac47a5b18a1e913325e15f224f60af886) [ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_8](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ac47a5b18a1e913325e15f224f60af886),

[ 246](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ae07575e3c8a86be20d2f7279e2a25c1e) [ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_9](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ae07575e3c8a86be20d2f7279e2a25c1e),

[ 247](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a7be307fed04fe1e3226516ab55b81c38) [ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_10](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a7be307fed04fe1e3226516ab55b81c38),

[ 248](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a982e97289cdcbf23274c78c8cb49b7b0) [ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_11](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a982e97289cdcbf23274c78c8cb49b7b0),

249

250 /\* Number of Virtual Wires \*/

[ 251](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ad3319083735295454bc59b742988cfca) [ESPI\_VWIRE\_SIGNAL\_COUNT](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ad3319083735295454bc59b742988cfca)

252};

253

254/\* USB-C port over current \*/

[ 255](group__espi__interface.md#gae4855b6cf8049de8aa6d67763f1be8c3)#define ESPI\_VWIRE\_SIGNAL\_OCB\_0 ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_0

[ 256](group__espi__interface.md#ga2ed490939e0249ff8196f77a74967727)#define ESPI\_VWIRE\_SIGNAL\_OCB\_1 ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_1

[ 257](group__espi__interface.md#gaf35d03bc041dc6baefe35b74c163d73b)#define ESPI\_VWIRE\_SIGNAL\_OCB\_2 ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_2

[ 258](group__espi__interface.md#gaeae1765d801cd298c27404c173a94707)#define ESPI\_VWIRE\_SIGNAL\_OCB\_3 ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_3

259

260/\* eSPI LPC peripherals. \*/

[ 261](group__espi__interface.md#gad00b6a22843e5df9c6d6945d0d82310e)enum [lpc\_peripheral\_opcode](group__espi__interface.md#gad00b6a22843e5df9c6d6945d0d82310e) {

262 /\* Read transactions \*/

[ 263](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eac172afb38cb38970ef6242a4f45132f9) [E8042\_OBF\_HAS\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eac172afb38cb38970ef6242a4f45132f9) = 0x50,

[ 264](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eab70684413d736c8583f3dc53f14b7c7a) [E8042\_IBF\_HAS\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eab70684413d736c8583f3dc53f14b7c7a),

265 /\* Write transactions \*/

[ 266](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eaa9135a5ea9a5ebd9d25660c37983c5d6) [E8042\_WRITE\_KB\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eaa9135a5ea9a5ebd9d25660c37983c5d6),

[ 267](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eaaef0649f867424ec0c7889acb7354911) [E8042\_WRITE\_MB\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eaaef0649f867424ec0c7889acb7354911),

268 /\* Write transactions without input parameters \*/

[ 269](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eac5b666b3319dc2ef0fc571684c2ea198) [E8042\_RESUME\_IRQ](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eac5b666b3319dc2ef0fc571684c2ea198),

[ 270](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea5e7205b5f1371f1a0f2eaed299389475) [E8042\_PAUSE\_IRQ](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea5e7205b5f1371f1a0f2eaed299389475),

[ 271](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eacdeb74a9534310f5dab3f1bfb5def534) [E8042\_CLEAR\_OBF](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eacdeb74a9534310f5dab3f1bfb5def534),

272 /\* Status transactions \*/

[ 273](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea8c62cd1266681c88aa0cb1af65ab551b) [E8042\_READ\_KB\_STS](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea8c62cd1266681c88aa0cb1af65ab551b),

[ 274](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea83266d88740588d45be6667a4034c447) [E8042\_SET\_FLAG](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea83266d88740588d45be6667a4034c447),

[ 275](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea5c592b1cad381b296cde832c67264cd1) [E8042\_CLEAR\_FLAG](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea5c592b1cad381b296cde832c67264cd1),

276 /\* ACPI read transactions \*/

[ 277](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea3cce8bd0205691ecda53fc469606929d) [EACPI\_OBF\_HAS\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea3cce8bd0205691ecda53fc469606929d) = EACPI\_START\_OPCODE,

[ 278](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea09f241a3f6ffcb5b7839c81c7fc4ea6e) [EACPI\_IBF\_HAS\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea09f241a3f6ffcb5b7839c81c7fc4ea6e),

279 /\* ACPI write transactions \*/

[ 280](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea689643f6feb724a303d3b790ff2899f7) [EACPI\_WRITE\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea689643f6feb724a303d3b790ff2899f7),

281 /\* ACPI status transactions \*/

[ 282](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea02bf8538a66f633e3d2ec094f57c6173) [EACPI\_READ\_STS](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea02bf8538a66f633e3d2ec094f57c6173),

[ 283](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea02c7b1c69d803a5c45304260786afb6f) [EACPI\_WRITE\_STS](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea02c7b1c69d803a5c45304260786afb6f),

284#if defined(CONFIG\_ESPI\_PERIPHERAL\_ACPI\_SHM\_REGION)

285 /\* Shared memory region support to return the ACPI response data \*/

286 EACPI\_GET\_SHARED\_MEMORY,

287#endif /\* CONFIG\_ESPI\_PERIPHERAL\_ACPI\_SHM\_REGION \*/

288#if defined(CONFIG\_ESPI\_PERIPHERAL\_CUSTOM\_OPCODE)

289 /\* Other customized transactions \*/

290 ECUSTOM\_HOST\_SUBS\_INTERRUPT\_EN = ECUSTOM\_START\_OPCODE,

291 ECUSTOM\_HOST\_CMD\_GET\_PARAM\_MEMORY,

292 ECUSTOM\_HOST\_CMD\_GET\_PARAM\_MEMORY\_SIZE,

293 ECUSTOM\_HOST\_CMD\_SEND\_RESULT,

294#endif /\* CONFIG\_ESPI\_PERIPHERAL\_CUSTOM\_OPCODE \*/

295};

296

297/\* KBC 8042 event: Input Buffer Full \*/

[ 298](group__espi__interface.md#gaa0807c908666cdcbb3a85f310bfbfccc)#define HOST\_KBC\_EVT\_IBF BIT(0)

299/\* KBC 8042 event: Output Buffer Empty \*/

[ 300](group__espi__interface.md#ga807bb75027f24e040cd28eba4bc1002c)#define HOST\_KBC\_EVT\_OBE BIT(1)

[ 304](structespi__evt__data__kbc.md)struct [espi\_evt\_data\_kbc](structespi__evt__data__kbc.md) {

[ 305](structespi__evt__data__kbc.md#a75294f9d88f6dfad7bb56e5af5613c64) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [type](structespi__evt__data__kbc.md#a75294f9d88f6dfad7bb56e5af5613c64):8;

[ 306](structespi__evt__data__kbc.md#a5f56bd66943cc82825bb1725bf8a2966) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data](structespi__evt__data__kbc.md#a5f56bd66943cc82825bb1725bf8a2966):8;

[ 307](structespi__evt__data__kbc.md#a55e94583f10481a2cdc34ad7ba388f2f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [evt](structespi__evt__data__kbc.md#a55e94583f10481a2cdc34ad7ba388f2f):8;

[ 308](structespi__evt__data__kbc.md#a0c17b320752b11dc04926df2965807b2) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved](structespi__evt__data__kbc.md#a0c17b320752b11dc04926df2965807b2):8;

309};

310

[ 314](structespi__evt__data__acpi.md)struct [espi\_evt\_data\_acpi](structespi__evt__data__acpi.md) {

[ 315](structespi__evt__data__acpi.md#aa5d1e0b548e9be6b65daf67316df8bfe) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [type](structespi__evt__data__acpi.md#aa5d1e0b548e9be6b65daf67316df8bfe):8;

[ 316](structespi__evt__data__acpi.md#a8fb3633a97b1af7618b391539f576c6f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [data](structespi__evt__data__acpi.md#a8fb3633a97b1af7618b391539f576c6f):8;

[ 317](structespi__evt__data__acpi.md#acb291c371bb201d0ceb739fca7e22d3b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [reserved](structespi__evt__data__acpi.md#acb291c371bb201d0ceb739fca7e22d3b):16;

318};

319

[ 323](structespi__event.md)struct [espi\_event](structespi__event.md) {

[ 325](structespi__event.md#acac75eb1d2b384aa337a5240825b635f) enum [espi\_bus\_event](group__espi__interface.md#ga36ac3fbf9813f78bad90f047e1eb1128) [evt\_type](structespi__event.md#acac75eb1d2b384aa337a5240825b635f);

[ 327](structespi__event.md#aea36925bd3f599c1481c9cc867795c33) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [evt\_details](structespi__event.md#aea36925bd3f599c1481c9cc867795c33);

[ 329](structespi__event.md#aa0491cbed5bec091721dfa14898b7277) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [evt\_data](structespi__event.md#aa0491cbed5bec091721dfa14898b7277);

330};

331

[ 335](structespi__cfg.md)struct [espi\_cfg](structespi__cfg.md) {

[ 337](structespi__cfg.md#a75175c60a31c3a88c83772b99c2a5c34) enum [espi\_io\_mode](group__espi__interface.md#ga0d7c61f1f4ec611d0c8a67ba73e2b4f0) [io\_caps](structespi__cfg.md#a75175c60a31c3a88c83772b99c2a5c34);

[ 339](structespi__cfg.md#abb24c88ecc977d8116973d44a7e7cb94) enum [espi\_channel](group__espi__interface.md#gafaa3f7d54503c901ab23bd79a7f8a755) [channel\_caps](structespi__cfg.md#abb24c88ecc977d8116973d44a7e7cb94);

[ 341](structespi__cfg.md#aed88dd6fc8028a7c281260e7fa29ce21) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [max\_freq](structespi__cfg.md#aed88dd6fc8028a7c281260e7fa29ce21);

342};

343

[ 347](structespi__request__packet.md)struct [espi\_request\_packet](structespi__request__packet.md) {

[ 348](structespi__request__packet.md#a9b474155dfa0c74d0bd55e4b831b383a) enum [espi\_cycle\_type](group__espi__interface.md#ga3e52615f244d7fa8ccda495ab8ec8a5b) [cycle\_type](structespi__request__packet.md#a9b474155dfa0c74d0bd55e4b831b383a);

[ 349](structespi__request__packet.md#a22a0111e338827125eaf79ce8516b744) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tag](structespi__request__packet.md#a22a0111e338827125eaf79ce8516b744);

[ 350](structespi__request__packet.md#ae8b7dc12b04f469b5689ad27cc4f0643) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structespi__request__packet.md#ae8b7dc12b04f469b5689ad27cc4f0643);

[ 351](structespi__request__packet.md#a4ac2d50786fdc4c4bd8da88bde28f77d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [address](structespi__request__packet.md#a4ac2d50786fdc4c4bd8da88bde28f77d);

[ 352](structespi__request__packet.md#a6f808763faf949ff7ef83d68fb71e7ba) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[data](structespi__request__packet.md#a6f808763faf949ff7ef83d68fb71e7ba);

353};

354

[ 358](structespi__oob__packet.md)struct [espi\_oob\_packet](structespi__oob__packet.md) {

[ 359](structespi__oob__packet.md#a0b19890b5e63ecbd1b95eef57fd9263f) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structespi__oob__packet.md#a0b19890b5e63ecbd1b95eef57fd9263f);

[ 360](structespi__oob__packet.md#adf45a10c88a171df8e7138929958b346) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structespi__oob__packet.md#adf45a10c88a171df8e7138929958b346);

361};

362

[ 366](structespi__flash__packet.md)struct [espi\_flash\_packet](structespi__flash__packet.md) {

[ 367](structespi__flash__packet.md#a22244bc4063618707eea571f170bdfde) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structespi__flash__packet.md#a22244bc4063618707eea571f170bdfde);

[ 368](structespi__flash__packet.md#ac638c0b5d0d98e15ab66850afc394cec) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flash\_addr](structespi__flash__packet.md#ac638c0b5d0d98e15ab66850afc394cec);

[ 369](structespi__flash__packet.md#adade51336ae37a519c06b12bf19fc86d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structespi__flash__packet.md#adade51336ae37a519c06b12bf19fc86d);

370};

371

372struct espi\_callback;

373

[ 383](group__espi__interface.md#ga9d848c7e367cf277230f365f73c15c46)typedef void (\*[espi\_callback\_handler\_t](group__espi__interface.md#ga9d848c7e367cf277230f365f73c15c46)) (const struct [device](structdevice.md) \*dev,

384 struct espi\_callback \*cb,

385 struct [espi\_event](structespi__event.md) espi\_evt);

386

397struct espi\_callback {

399 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

400

402 [espi\_callback\_handler\_t](group__espi__interface.md#ga9d848c7e367cf277230f365f73c15c46) handler;

403

409 enum [espi\_bus\_event](group__espi__interface.md#ga36ac3fbf9813f78bad90f047e1eb1128) evt\_type;

410};

412

420typedef int (\*espi\_api\_config)(const struct [device](structdevice.md) \*dev, struct [espi\_cfg](structespi__cfg.md) \*cfg);

421typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*espi\_api\_get\_channel\_status)(const struct [device](structdevice.md) \*dev,

422 enum [espi\_channel](group__espi__interface.md#gafaa3f7d54503c901ab23bd79a7f8a755) ch);

423/\* Logical Channel 0 APIs \*/

424typedef int (\*espi\_api\_read\_request)(const struct [device](structdevice.md) \*dev,

425 struct [espi\_request\_packet](structespi__request__packet.md) \*req);

426typedef int (\*espi\_api\_write\_request)(const struct [device](structdevice.md) \*dev,

427 struct [espi\_request\_packet](structespi__request__packet.md) \*req);

428typedef int (\*espi\_api\_lpc\_read\_request)(const struct [device](structdevice.md) \*dev,

429 enum [lpc\_peripheral\_opcode](group__espi__interface.md#gad00b6a22843e5df9c6d6945d0d82310e) op,

430 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

431typedef int (\*espi\_api\_lpc\_write\_request)(const struct [device](structdevice.md) \*dev,

432 enum [lpc\_peripheral\_opcode](group__espi__interface.md#gad00b6a22843e5df9c6d6945d0d82310e) op,

433 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e));

434/\* Logical Channel 1 APIs \*/

435typedef int (\*espi\_api\_send\_vwire)(const struct [device](structdevice.md) \*dev,

436 enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) vw,

437 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level);

438typedef int (\*espi\_api\_receive\_vwire)(const struct [device](structdevice.md) \*dev,

439 enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) vw,

440 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*level);

441/\* Logical Channel 2 APIs \*/

442typedef int (\*espi\_api\_send\_oob)(const struct [device](structdevice.md) \*dev,

443 struct [espi\_oob\_packet](structespi__oob__packet.md) \*pckt);

444typedef int (\*espi\_api\_receive\_oob)(const struct [device](structdevice.md) \*dev,

445 struct [espi\_oob\_packet](structespi__oob__packet.md) \*pckt);

446/\* Logical Channel 3 APIs \*/

447typedef int (\*espi\_api\_flash\_read)(const struct [device](structdevice.md) \*dev,

448 struct [espi\_flash\_packet](structespi__flash__packet.md) \*pckt);

449typedef int (\*espi\_api\_flash\_write)(const struct [device](structdevice.md) \*dev,

450 struct [espi\_flash\_packet](structespi__flash__packet.md) \*pckt);

451typedef int (\*espi\_api\_flash\_erase)(const struct [device](structdevice.md) \*dev,

452 struct [espi\_flash\_packet](structespi__flash__packet.md) \*pckt);

453/\* Callbacks and traffic intercept \*/

454typedef int (\*espi\_api\_manage\_callback)(const struct [device](structdevice.md) \*dev,

455 struct espi\_callback \*callback,

456 bool set);

457

458\_\_subsystem struct espi\_driver\_api {

459 espi\_api\_config config;

460 espi\_api\_get\_channel\_status get\_channel\_status;

461 espi\_api\_read\_request read\_request;

462 espi\_api\_write\_request write\_request;

463 espi\_api\_lpc\_read\_request read\_lpc\_request;

464 espi\_api\_lpc\_write\_request write\_lpc\_request;

465 espi\_api\_send\_vwire send\_vwire;

466 espi\_api\_receive\_vwire receive\_vwire;

467 espi\_api\_send\_oob send\_oob;

468 espi\_api\_receive\_oob receive\_oob;

469 espi\_api\_flash\_read [flash\_read](group__flash__interface.md#gaa7c9382796aad64da0da683f54600b5f);

470 espi\_api\_flash\_write [flash\_write](group__flash__interface.md#ga76d7880cc5e18ca40237736d3bd94324);

471 espi\_api\_flash\_erase [flash\_erase](group__flash__interface.md#ga05f9c8b0c1ff7273f71797e7ff799c95);

472 espi\_api\_manage\_callback manage\_callback;

473};

474

478

[ 527](group__espi__interface.md#ga7227c53d384eb0dc666361261f069f68)\_\_syscall int [espi\_config](group__espi__interface.md#ga7227c53d384eb0dc666361261f069f68)(const struct [device](structdevice.md) \*dev, struct [espi\_cfg](structespi__cfg.md) \*cfg);

528

529static inline int z\_impl\_espi\_config(const struct [device](structdevice.md) \*dev,

530 struct [espi\_cfg](structespi__cfg.md) \*cfg)

531{

532 const struct espi\_driver\_api \*api =

533 (const struct espi\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

534

535 return api->config(dev, cfg);

536}

537

[ 550](group__espi__interface.md#ga869551e20fc2c3be4311c21c3c53999d)\_\_syscall bool [espi\_get\_channel\_status](group__espi__interface.md#ga869551e20fc2c3be4311c21c3c53999d)(const struct [device](structdevice.md) \*dev,

551 enum [espi\_channel](group__espi__interface.md#gafaa3f7d54503c901ab23bd79a7f8a755) ch);

552

553static inline bool z\_impl\_espi\_get\_channel\_status(const struct [device](structdevice.md) \*dev,

554 enum [espi\_channel](group__espi__interface.md#gafaa3f7d54503c901ab23bd79a7f8a755) ch)

555{

556 const struct espi\_driver\_api \*api =

557 (const struct espi\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

558

559 return api->get\_channel\_status(dev, ch);

560}

561

[ 576](group__espi__interface.md#ga112f7554ba614c8e5f239b1319b4a763)\_\_syscall int [espi\_read\_request](group__espi__interface.md#ga112f7554ba614c8e5f239b1319b4a763)(const struct [device](structdevice.md) \*dev,

577 struct [espi\_request\_packet](structespi__request__packet.md) \*req);

578

579static inline int z\_impl\_espi\_read\_request(const struct [device](structdevice.md) \*dev,

580 struct [espi\_request\_packet](structespi__request__packet.md) \*req)

581{

582 const struct espi\_driver\_api \*api =

583 (const struct espi\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

584

585 if (!api->read\_request) {

586 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

587 }

588

589 return api->read\_request(dev, req);

590}

591

[ 606](group__espi__interface.md#ga143ed88b1f220f9582c809165fd983fd)\_\_syscall int [espi\_write\_request](group__espi__interface.md#ga143ed88b1f220f9582c809165fd983fd)(const struct [device](structdevice.md) \*dev,

607 struct [espi\_request\_packet](structespi__request__packet.md) \*req);

608

609static inline int z\_impl\_espi\_write\_request(const struct [device](structdevice.md) \*dev,

610 struct [espi\_request\_packet](structespi__request__packet.md) \*req)

611{

612 const struct espi\_driver\_api \*api =

613 (const struct espi\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

614

615 if (!api->write\_request) {

616 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

617 }

618

619 return api->write\_request(dev, req);

620}

621

[ 638](group__espi__interface.md#gaeaae20afa90d9d825d80997369f31465)\_\_syscall int [espi\_read\_lpc\_request](group__espi__interface.md#gaeaae20afa90d9d825d80997369f31465)(const struct [device](structdevice.md) \*dev,

639 enum [lpc\_peripheral\_opcode](group__espi__interface.md#gad00b6a22843e5df9c6d6945d0d82310e) op,

640 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data);

641

642static inline int z\_impl\_espi\_read\_lpc\_request(const struct [device](structdevice.md) \*dev,

643 enum [lpc\_peripheral\_opcode](group__espi__interface.md#gad00b6a22843e5df9c6d6945d0d82310e) op,

644 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data)

645{

646 const struct espi\_driver\_api \*api =

647 (const struct espi\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

648

649 if (!api->read\_lpc\_request) {

650 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

651 }

652

653 return api->read\_lpc\_request(dev, op, data);

654}

655

[ 671](group__espi__interface.md#ga880b6b04824f9f0deea10e8018573b88)\_\_syscall int [espi\_write\_lpc\_request](group__espi__interface.md#ga880b6b04824f9f0deea10e8018573b88)(const struct [device](structdevice.md) \*dev,

672 enum [lpc\_peripheral\_opcode](group__espi__interface.md#gad00b6a22843e5df9c6d6945d0d82310e) op,

673 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data);

674

675static inline int z\_impl\_espi\_write\_lpc\_request(const struct [device](structdevice.md) \*dev,

676 enum [lpc\_peripheral\_opcode](group__espi__interface.md#gad00b6a22843e5df9c6d6945d0d82310e) op,

677 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data)

678{

679 const struct espi\_driver\_api \*api =

680 (const struct espi\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

681

682 if (!api->write\_lpc\_request) {

683 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

684 }

685

686 return api->write\_lpc\_request(dev, op, data);

687}

688

[ 702](group__espi__interface.md#gacab2b3bff7d940e71ee1c2a9fdedf782)\_\_syscall int [espi\_send\_vwire](group__espi__interface.md#gacab2b3bff7d940e71ee1c2a9fdedf782)(const struct [device](structdevice.md) \*dev,

703 enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) signal,

704 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level);

705

706static inline int z\_impl\_espi\_send\_vwire(const struct [device](structdevice.md) \*dev,

707 enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) signal,

708 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level)

709{

710 const struct espi\_driver\_api \*api =

711 (const struct espi\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

712

713 return api->send\_vwire(dev, signal, level);

714}

715

[ 728](group__espi__interface.md#gaa8bb48b5592c4b49d27c9b8a42432410)\_\_syscall int [espi\_receive\_vwire](group__espi__interface.md#gaa8bb48b5592c4b49d27c9b8a42432410)(const struct [device](structdevice.md) \*dev,

729 enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) signal,

730 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*level);

731

732static inline int z\_impl\_espi\_receive\_vwire(const struct [device](structdevice.md) \*dev,

733 enum [espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35) signal,

734 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*level)

735{

736 const struct espi\_driver\_api \*api =

737 (const struct espi\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

738

739 return api->receive\_vwire(dev, signal, level);

740}

741

[ 753](group__espi__interface.md#ga2557cfc7a38f669d14e9826e3fb0fdee)\_\_syscall int [espi\_send\_oob](group__espi__interface.md#ga2557cfc7a38f669d14e9826e3fb0fdee)(const struct [device](structdevice.md) \*dev,

754 struct [espi\_oob\_packet](structespi__oob__packet.md) \*pckt);

755

756static inline int z\_impl\_espi\_send\_oob(const struct [device](structdevice.md) \*dev,

757 struct [espi\_oob\_packet](structespi__oob__packet.md) \*pckt)

758{

759 const struct espi\_driver\_api \*api =

760 (const struct espi\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

761

762 if (!api->send\_oob) {

763 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

764 }

765

766 return api->send\_oob(dev, pckt);

767}

768

[ 780](group__espi__interface.md#ga4b8f4fbf66a2b2ae394e00b16500f70d)\_\_syscall int [espi\_receive\_oob](group__espi__interface.md#ga4b8f4fbf66a2b2ae394e00b16500f70d)(const struct [device](structdevice.md) \*dev,

781 struct [espi\_oob\_packet](structespi__oob__packet.md) \*pckt);

782

783static inline int z\_impl\_espi\_receive\_oob(const struct [device](structdevice.md) \*dev,

784 struct [espi\_oob\_packet](structespi__oob__packet.md) \*pckt)

785{

786 const struct espi\_driver\_api \*api =

787 (const struct espi\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

788

789 if (!api->receive\_oob) {

790 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

791 }

792

793 return api->receive\_oob(dev, pckt);

794}

795

[ 809](group__espi__interface.md#ga0a97d11167367342283bfe6b6d66726e)\_\_syscall int [espi\_read\_flash](group__espi__interface.md#ga0a97d11167367342283bfe6b6d66726e)(const struct [device](structdevice.md) \*dev,

810 struct [espi\_flash\_packet](structespi__flash__packet.md) \*pckt);

811

812static inline int z\_impl\_espi\_read\_flash(const struct [device](structdevice.md) \*dev,

813 struct [espi\_flash\_packet](structespi__flash__packet.md) \*pckt)

814{

815 const struct espi\_driver\_api \*api =

816 (const struct espi\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

817

818 if (!api->flash\_read) {

819 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

820 }

821

822 return api->flash\_read(dev, pckt);

823}

824

[ 838](group__espi__interface.md#gab02d46fd690e33875cc1b2433c976891)\_\_syscall int [espi\_write\_flash](group__espi__interface.md#gab02d46fd690e33875cc1b2433c976891)(const struct [device](structdevice.md) \*dev,

839 struct [espi\_flash\_packet](structespi__flash__packet.md) \*pckt);

840

841static inline int z\_impl\_espi\_write\_flash(const struct [device](structdevice.md) \*dev,

842 struct [espi\_flash\_packet](structespi__flash__packet.md) \*pckt)

843{

844 const struct espi\_driver\_api \*api =

845 (const struct espi\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

846

847 if (!api->flash\_write) {

848 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

849 }

850

851 return api->flash\_write(dev, pckt);

852}

853

[ 867](group__espi__interface.md#gab42be7c76c4523cea96365aa77fd18be)\_\_syscall int [espi\_flash\_erase](group__espi__interface.md#gab42be7c76c4523cea96365aa77fd18be)(const struct [device](structdevice.md) \*dev,

868 struct [espi\_flash\_packet](structespi__flash__packet.md) \*pckt);

869

870static inline int z\_impl\_espi\_flash\_erase(const struct [device](structdevice.md) \*dev,

871 struct [espi\_flash\_packet](structespi__flash__packet.md) \*pckt)

872{

873 const struct espi\_driver\_api \*api =

874 (const struct espi\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

875

876 if (!api->flash\_erase) {

877 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

878 }

879

880 return api->flash\_erase(dev, pckt);

881}

882

944

[ 953](group__espi__interface.md#ga8d88e4e3893d610713195e5352ec2565)static inline void [espi\_init\_callback](group__espi__interface.md#ga8d88e4e3893d610713195e5352ec2565)(struct espi\_callback \*callback,

954 [espi\_callback\_handler\_t](group__espi__interface.md#ga9d848c7e367cf277230f365f73c15c46) handler,

955 enum [espi\_bus\_event](group__espi__interface.md#ga36ac3fbf9813f78bad90f047e1eb1128) evt\_type)

956{

957 \_\_ASSERT(callback, "Callback pointer should not be NULL");

958 \_\_ASSERT(handler, "Callback handler pointer should not be NULL");

959

960 callback->handler = handler;

961 callback->evt\_type = evt\_type;

962}

963

[ 976](group__espi__interface.md#gabf5f0ea01ec8ed5345b2e119181c2313)static inline int [espi\_add\_callback](group__espi__interface.md#gabf5f0ea01ec8ed5345b2e119181c2313)(const struct [device](structdevice.md) \*dev,

977 struct espi\_callback \*callback)

978{

979 const struct espi\_driver\_api \*api =

980 (const struct espi\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

981

982 if (!api->manage\_callback) {

983 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

984 }

985

986 return api->manage\_callback(dev, callback, true);

987}

988

[ 1005](group__espi__interface.md#ga7f04f98ea6a4671b821cf6ddf6bbf2a6)static inline int [espi\_remove\_callback](group__espi__interface.md#ga7f04f98ea6a4671b821cf6ddf6bbf2a6)(const struct [device](structdevice.md) \*dev,

1006 struct espi\_callback \*callback)

1007{

1008 const struct espi\_driver\_api \*api =

1009 (const struct espi\_driver\_api \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

1010

1011 if (!api->manage\_callback) {

1012 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

1013 }

1014

1015 return api->manage\_callback(dev, callback, false);

1016}

1017

1018#ifdef \_\_cplusplus

1019}

1020#endif

1021

1025#include <syscalls/espi.h>

1026#endif /\* ZEPHYR\_INCLUDE\_ESPI\_H\_ \*/

[\_\_assert.h](____assert_8h.md)

[device.h](device_8h.md)

[errno.h](errno_8h.md)

System error numbers.

[espi\_read\_flash](group__espi__interface.md#ga0a97d11167367342283bfe6b6d66726e)

int espi\_read\_flash(const struct device \*dev, struct espi\_flash\_packet \*pckt)

Sends a read request packet for shared flash.

[espi\_io\_mode](group__espi__interface.md#ga0d7c61f1f4ec611d0c8a67ba73e2b4f0)

espi\_io\_mode

eSPI I/O mode capabilities

**Definition** espi.h:36

[espi\_read\_request](group__espi__interface.md#ga112f7554ba614c8e5f239b1319b4a763)

int espi\_read\_request(const struct device \*dev, struct espi\_request\_packet \*req)

Sends memory, I/O or message read request over eSPI.

[espi\_write\_request](group__espi__interface.md#ga143ed88b1f220f9582c809165fd983fd)

int espi\_write\_request(const struct device \*dev, struct espi\_request\_packet \*req)

Sends memory, I/O or message write request over eSPI.

[espi\_send\_oob](group__espi__interface.md#ga2557cfc7a38f669d14e9826e3fb0fdee)

int espi\_send\_oob(const struct device \*dev, struct espi\_oob\_packet \*pckt)

Sends SMBus transaction (out-of-band) packet over eSPI bus.

[espi\_virtual\_peripheral](group__espi__interface.md#ga2629a5518a94f031419eeccd05f07373)

espi\_virtual\_peripheral

eSPI peripheral notification type.

**Definition** espi.h:169

[espi\_bus\_event](group__espi__interface.md#ga36ac3fbf9813f78bad90f047e1eb1128)

espi\_bus\_event

eSPI bus event.

**Definition** espi.h:114

[espi\_cycle\_type](group__espi__interface.md#ga3e52615f244d7fa8ccda495ab8ec8a5b)

espi\_cycle\_type

eSPI cycle types supported over eSPI peripheral channel

**Definition** espi.h:183

[espi\_receive\_oob](group__espi__interface.md#ga4b8f4fbf66a2b2ae394e00b16500f70d)

int espi\_receive\_oob(const struct device \*dev, struct espi\_oob\_packet \*pckt)

Receives SMBus transaction (out-of-band) packet from eSPI bus.

[espi\_config](group__espi__interface.md#ga7227c53d384eb0dc666361261f069f68)

int espi\_config(const struct device \*dev, struct espi\_cfg \*cfg)

Configure operation of a eSPI controller.

[espi\_remove\_callback](group__espi__interface.md#ga7f04f98ea6a4671b821cf6ddf6bbf2a6)

static int espi\_remove\_callback(const struct device \*dev, struct espi\_callback \*callback)

Remove an application callback.

**Definition** espi.h:1005

[espi\_get\_channel\_status](group__espi__interface.md#ga869551e20fc2c3be4311c21c3c53999d)

bool espi\_get\_channel\_status(const struct device \*dev, enum espi\_channel ch)

Query to see if it a channel is ready.

[espi\_write\_lpc\_request](group__espi__interface.md#ga880b6b04824f9f0deea10e8018573b88)

int espi\_write\_lpc\_request(const struct device \*dev, enum lpc\_peripheral\_opcode op, uint32\_t \*data)

Writes data to a LPC peripheral which generates an eSPI transaction.

[espi\_init\_callback](group__espi__interface.md#ga8d88e4e3893d610713195e5352ec2565)

static void espi\_init\_callback(struct espi\_callback \*callback, espi\_callback\_handler\_t handler, enum espi\_bus\_event evt\_type)

Callback model.

**Definition** espi.h:953

[espi\_callback\_handler\_t](group__espi__interface.md#ga9d848c7e367cf277230f365f73c15c46)

void(\* espi\_callback\_handler\_t)(const struct device \*dev, struct espi\_callback \*cb, struct espi\_event espi\_evt)

Define the application callback handler function signature.

**Definition** espi.h:383

[espi\_receive\_vwire](group__espi__interface.md#gaa8bb48b5592c4b49d27c9b8a42432410)

int espi\_receive\_vwire(const struct device \*dev, enum espi\_vwire\_signal signal, uint8\_t \*level)

Retrieves level status for a signal encapsulated in a virtual wire.

[espi\_write\_flash](group__espi__interface.md#gab02d46fd690e33875cc1b2433c976891)

int espi\_write\_flash(const struct device \*dev, struct espi\_flash\_packet \*pckt)

Sends a write request packet for shared flash.

[espi\_flash\_erase](group__espi__interface.md#gab42be7c76c4523cea96365aa77fd18be)

int espi\_flash\_erase(const struct device \*dev, struct espi\_flash\_packet \*pckt)

Sends a write request packet for shared flash.

[espi\_vwire\_signal](group__espi__interface.md#gab65a0951a8912d9de398cfec0aef7d35)

espi\_vwire\_signal

eSPI system platform signals that can be send or receive through virtual wire channel

**Definition** espi.h:199

[espi\_add\_callback](group__espi__interface.md#gabf5f0ea01ec8ed5345b2e119181c2313)

static int espi\_add\_callback(const struct device \*dev, struct espi\_callback \*callback)

Add an application callback.

**Definition** espi.h:976

[espi\_pc\_event](group__espi__interface.md#gac55098842dd9d181144ac4b4122a610e)

espi\_pc\_event

eSPI peripheral channel events.

**Definition** espi.h:128

[espi\_send\_vwire](group__espi__interface.md#gacab2b3bff7d940e71ee1c2a9fdedf782)

int espi\_send\_vwire(const struct device \*dev, enum espi\_vwire\_signal signal, uint8\_t level)

Sends system/platform signal as a virtual wire packet.

[lpc\_peripheral\_opcode](group__espi__interface.md#gad00b6a22843e5df9c6d6945d0d82310e)

lpc\_peripheral\_opcode

**Definition** espi.h:261

[espi\_read\_lpc\_request](group__espi__interface.md#gaeaae20afa90d9d825d80997369f31465)

int espi\_read\_lpc\_request(const struct device \*dev, enum lpc\_peripheral\_opcode op, uint32\_t \*data)

Reads SOC data from a LPC peripheral with information updated over eSPI.

[espi\_channel](group__espi__interface.md#gafaa3f7d54503c901ab23bd79a7f8a755)

espi\_channel

eSPI channel.

**Definition** espi.h:102

[ESPI\_IO\_MODE\_QUAD\_LINES](group__espi__interface.md#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a87e70bb0f5c4f6a3a21ca1bcfa4540fc)

@ ESPI\_IO\_MODE\_QUAD\_LINES

**Definition** espi.h:39

[ESPI\_IO\_MODE\_SINGLE\_LINE](group__espi__interface.md#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0a9f47188ebd9bb4cb6e426d0bc0b6595c)

@ ESPI\_IO\_MODE\_SINGLE\_LINE

**Definition** espi.h:37

[ESPI\_IO\_MODE\_DUAL\_LINES](group__espi__interface.md#gga0d7c61f1f4ec611d0c8a67ba73e2b4f0af766582d28d16af7c5aff6372e4ee243)

@ ESPI\_IO\_MODE\_DUAL\_LINES

**Definition** espi.h:38

[ESPI\_PERIPHERAL\_UART](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373a24478711945fd5258d8ca86bbb79b867)

@ ESPI\_PERIPHERAL\_UART

**Definition** espi.h:170

[ESPI\_PERIPHERAL\_HOST\_IO](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373a8948a6f18bfbe87859a529d5f6e669b8)

@ ESPI\_PERIPHERAL\_HOST\_IO

**Definition** espi.h:172

[ESPI\_PERIPHERAL\_HOST\_IO\_PVT](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373aa217b4786d7b8bacbaa4ec740550e71e)

@ ESPI\_PERIPHERAL\_HOST\_IO\_PVT

**Definition** espi.h:174

[ESPI\_PERIPHERAL\_8042\_KBC](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373aaea75bb5ab8a5ff31dd6b8787f44df30)

@ ESPI\_PERIPHERAL\_8042\_KBC

**Definition** espi.h:171

[ESPI\_PERIPHERAL\_DEBUG\_PORT80](group__espi__interface.md#gga2629a5518a94f031419eeccd05f07373af51b7171cf6085fa7946333ff32fe2f0)

@ ESPI\_PERIPHERAL\_DEBUG\_PORT80

**Definition** espi.h:173

[ESPI\_BUS\_EVENT\_OOB\_RECEIVED](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128a3b5e529d1d0ba11c59172ab01c30e203)

@ ESPI\_BUS\_EVENT\_OOB\_RECEIVED

**Definition** espi.h:118

[ESPI\_BUS\_SAF\_NOTIFICATION](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128a8bd46c68d9aa33c42aa098110b6f0ae4)

@ ESPI\_BUS\_SAF\_NOTIFICATION

**Definition** espi.h:120

[ESPI\_BUS\_EVENT\_CHANNEL\_READY](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128a996aee0a8f8ba0cead11cea0d39d2973)

@ ESPI\_BUS\_EVENT\_CHANNEL\_READY

**Definition** espi.h:116

[ESPI\_BUS\_PERIPHERAL\_NOTIFICATION](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128a9ac837699f302bd10332814c7014adea)

@ ESPI\_BUS\_PERIPHERAL\_NOTIFICATION

**Definition** espi.h:119

[ESPI\_BUS\_EVENT\_VWIRE\_RECEIVED](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128aa09f7dcd4b2d3addfaddbad5b8f2e5a2)

@ ESPI\_BUS\_EVENT\_VWIRE\_RECEIVED

**Definition** espi.h:117

[ESPI\_BUS\_RESET](group__espi__interface.md#gga36ac3fbf9813f78bad90f047e1eb1128ae6d4d43eded0d8a368c90ea653a60956)

@ ESPI\_BUS\_RESET

**Definition** espi.h:115

[ESPI\_CYCLE\_OK\_COMPLETION\_NODATA](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba0335f2d34fab46960939e2d2c1c12e3f)

@ ESPI\_CYCLE\_OK\_COMPLETION\_NODATA

**Definition** espi.h:190

[ESPI\_CYCLE\_NOK\_COMPLETION\_NODATA](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba0edb306e5fabcbf8b009375cde6a8a2b)

@ ESPI\_CYCLE\_NOK\_COMPLETION\_NODATA

**Definition** espi.h:192

[ESPI\_CYCLE\_MEMORY\_WRITE32](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba2e5a736cf8a63491ee13d51ae4f8f073)

@ ESPI\_CYCLE\_MEMORY\_WRITE32

**Definition** espi.h:186

[ESPI\_CYCLE\_MESSAGE\_DATA](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba380e3d4e6b5579c8bb94e792fcb7d71f)

@ ESPI\_CYCLE\_MESSAGE\_DATA

**Definition** espi.h:189

[ESPI\_CYCLE\_MEMORY\_WRITE64](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba54c11e63fcfe3f859af57e65af3f31f7)

@ ESPI\_CYCLE\_MEMORY\_WRITE64

**Definition** espi.h:187

[ESPI\_CYCLE\_MEMORY\_READ32](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba5b480e093a58849d4181bba22d5868a5)

@ ESPI\_CYCLE\_MEMORY\_READ32

**Definition** espi.h:184

[ESPI\_CYCLE\_MESSAGE\_NODATA](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5ba5f2ae0575ca4e9b61c0acd7d4f08ee82)

@ ESPI\_CYCLE\_MESSAGE\_NODATA

**Definition** espi.h:188

[ESPI\_CYCLE\_MEMORY\_READ64](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5bac8ec7673b4466b278dfb5e468f7a4d79)

@ ESPI\_CYCLE\_MEMORY\_READ64

**Definition** espi.h:185

[ESPI\_CYCLE\_OKCOMPLETION\_DATA](group__espi__interface.md#gga3e52615f244d7fa8ccda495ab8ec8a5baf3dbc2bcc0ed883bc4d4160c21e6934f)

@ ESPI\_CYCLE\_OKCOMPLETION\_DATA

**Definition** espi.h:191

[ESPI\_VWIRE\_SIGNAL\_PLTRST](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a0bafcd0bb7f592f0e308dcfce39bcd08)

@ ESPI\_VWIRE\_SIGNAL\_PLTRST

**Definition** espi.h:205

[ESPI\_VWIRE\_SIGNAL\_SUS\_STAT](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a0e13f250ba0c5a37451c7f3b0e98e663)

@ ESPI\_VWIRE\_SIGNAL\_SUS\_STAT

**Definition** espi.h:206

[ESPI\_VWIRE\_SIGNAL\_RST\_CPU\_INIT](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a19c40230e0bb4cee7b6ee42580c28a8d)

@ ESPI\_VWIRE\_SIGNAL\_RST\_CPU\_INIT

**Definition** espi.h:226

[ESPI\_VWIRE\_SIGNAL\_SMIOUT](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a1d54a71c6d2e52cb66cfaa0b55b61152)

@ ESPI\_VWIRE\_SIGNAL\_SMIOUT

**Definition** espi.h:208

[ESPI\_VWIRE\_SIGNAL\_SMI](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a2d9b2eef499d1bfd13bec1d2caa0e2f3)

@ ESPI\_VWIRE\_SIGNAL\_SMI

**Definition** espi.h:228

[ESPI\_VWIRE\_SIGNAL\_OOB\_RST\_WARN](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a2f3f97b51b750050cd98e887e39431d1)

@ ESPI\_VWIRE\_SIGNAL\_OOB\_RST\_WARN

**Definition** espi.h:204

[ESPI\_VWIRE\_SIGNAL\_SLP\_WLAN](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a3d95f095ae41bba9ef916fc68ddd4779)

@ ESPI\_VWIRE\_SIGNAL\_SLP\_WLAN

**Definition** espi.h:213

[ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_2](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a3f4ee544ee9319d1ea4f59c25b5ab978)

@ ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_2

**Definition** espi.h:239

[ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_5](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a491455d416d15d3a9009094afb96198f)

@ ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_5

**Definition** espi.h:242

[ESPI\_VWIRE\_SIGNAL\_SLP\_S4](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a4ef1fe12bd09be0875864d6c32164f73)

@ ESPI\_VWIRE\_SIGNAL\_SLP\_S4

**Definition** espi.h:202

[ESPI\_VWIRE\_SIGNAL\_ERR\_NON\_FATAL](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a504ae332b89262f70a0bf1a9c8b6f527)

@ ESPI\_VWIRE\_SIGNAL\_ERR\_NON\_FATAL

**Definition** espi.h:222

[ESPI\_VWIRE\_SIGNAL\_DNX\_ACK](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a58280c68c980476aabefa16e0509dd1c)

@ ESPI\_VWIRE\_SIGNAL\_DNX\_ACK

**Definition** espi.h:231

[ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_1](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a66e16dfc37e6c1f3d09ee4b5abc4264e)

@ ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_1

**Definition** espi.h:238

[ESPI\_VWIRE\_SIGNAL\_WAKE](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a736724f8229aebc356c2720a34a0143f)

@ ESPI\_VWIRE\_SIGNAL\_WAKE

**Definition** espi.h:219

[ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_10](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a7be307fed04fe1e3226516ab55b81c38)

@ ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_10

**Definition** espi.h:247

[ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_0](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a7e7d23a32779cc3a786cc17e97bed167)

@ ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_0

**Definition** espi.h:237

[ESPI\_VWIRE\_SIGNAL\_HOST\_RST\_ACK](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a89420628ae26df4c45ef7fba04a3a85e)

@ ESPI\_VWIRE\_SIGNAL\_HOST\_RST\_ACK

**Definition** espi.h:225

[ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_4](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a8a68fbaffa51abdd858b72c6e59e89ba)

@ ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_4

**Definition** espi.h:241

[ESPI\_VWIRE\_SIGNAL\_OOB\_RST\_ACK](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a8e15df6f8159b4c275dc4b20aaec352e)

@ ESPI\_VWIRE\_SIGNAL\_OOB\_RST\_ACK

**Definition** espi.h:220

[ESPI\_VWIRE\_SIGNAL\_DNX\_WARN](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a923f3e602d9f8ac821ece2a625183146)

@ ESPI\_VWIRE\_SIGNAL\_DNX\_WARN

**Definition** espi.h:216

[ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_11](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a982e97289cdcbf23274c78c8cb49b7b0)

@ ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_11

**Definition** espi.h:248

[ESPI\_VWIRE\_SIGNAL\_SUS\_WARN](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35a9e32eee077aaa1668c356fe1d4ab1cc5)

@ ESPI\_VWIRE\_SIGNAL\_SUS\_WARN

**Definition** espi.h:212

[ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_3](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aa3bf67d616ea21733b1b7a4bc8ecf671)

@ ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_3

**Definition** espi.h:240

[ESPI\_VWIRE\_SIGNAL\_SLP\_A](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aa4c8c69475b48d88302066823d2f3592)

@ ESPI\_VWIRE\_SIGNAL\_SLP\_A

**Definition** espi.h:210

[ESPI\_VWIRE\_SIGNAL\_PME](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aa87af5b5de184238e5f371851aaee692)

@ ESPI\_VWIRE\_SIGNAL\_PME

**Definition** espi.h:218

[ESPI\_VWIRE\_SIGNAL\_SLV\_BOOT\_DONE](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aa90439bef2746a982cac6eb3ea2c515d)

@ ESPI\_VWIRE\_SIGNAL\_SLV\_BOOT\_DONE

**Definition** espi.h:224

[ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_7](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aad603524796723906f74b14ddd0c3761)

@ ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_7

**Definition** espi.h:244

[ESPI\_VWIRE\_SIGNAL\_ERR\_FATAL](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aae0a3fd882c5765db33a4e7bd05e1ab1)

@ ESPI\_VWIRE\_SIGNAL\_ERR\_FATAL

**Definition** espi.h:223

[ESPI\_VWIRE\_SIGNAL\_SUS\_PWRDN\_ACK](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ab4f0bedd5717660cc8cac2d85c6c3d18)

@ ESPI\_VWIRE\_SIGNAL\_SUS\_PWRDN\_ACK

**Definition** espi.h:211

[ESPI\_VWIRE\_SIGNAL\_SLP\_S3](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ab880a7156e489d5f7b8f78550e72b166)

@ ESPI\_VWIRE\_SIGNAL\_SLP\_S3

**Definition** espi.h:201

[ESPI\_VWIRE\_SIGNAL\_HOST\_C10](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ab9deb0dd6d4e878eff6413ddc34bb36c)

@ ESPI\_VWIRE\_SIGNAL\_HOST\_C10

**Definition** espi.h:215

[ESPI\_VWIRE\_SIGNAL\_SLP\_LAN](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35aba8b891a643ca567966d091963be4615)

@ ESPI\_VWIRE\_SIGNAL\_SLP\_LAN

**Definition** espi.h:214

[ESPI\_VWIRE\_SIGNAL\_SUS\_ACK](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35abe28432b566619d8c6cce5e5034e5333)

@ ESPI\_VWIRE\_SIGNAL\_SUS\_ACK

**Definition** espi.h:232

[ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_8](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ac47a5b18a1e913325e15f224f60af886)

@ ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_8

**Definition** espi.h:245

[ESPI\_VWIRE\_SIGNAL\_SLP\_S5](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ac4b4e30c097a4ef49f21549a799e1e13)

@ ESPI\_VWIRE\_SIGNAL\_SLP\_S5

**Definition** espi.h:203

[ESPI\_VWIRE\_SIGNAL\_NMIOUT](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ad14b4b7a25141346bfefc507c588a238)

@ ESPI\_VWIRE\_SIGNAL\_NMIOUT

**Definition** espi.h:207

[ESPI\_VWIRE\_SIGNAL\_COUNT](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ad3319083735295454bc59b742988cfca)

@ ESPI\_VWIRE\_SIGNAL\_COUNT

**Definition** espi.h:251

[ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_9](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ae07575e3c8a86be20d2f7279e2a25c1e)

@ ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_9

**Definition** espi.h:246

[ESPI\_VWIRE\_SIGNAL\_SLV\_BOOT\_STS](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ae47cb1e53323e2fd42d7f40c21cd583d)

@ ESPI\_VWIRE\_SIGNAL\_SLV\_BOOT\_STS

**Definition** espi.h:221

[ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_6](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35ae72c7e72a3ec597027040bf676e6e85e)

@ ESPI\_VWIRE\_SIGNAL\_SLV\_GPIO\_6

**Definition** espi.h:243

[ESPI\_VWIRE\_SIGNAL\_HOST\_RST\_WARN](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35af44250de6f60eabf9b0d85b8860ac56e)

@ ESPI\_VWIRE\_SIGNAL\_HOST\_RST\_WARN

**Definition** espi.h:209

[ESPI\_VWIRE\_SIGNAL\_SCI](group__espi__interface.md#ggab65a0951a8912d9de398cfec0aef7d35afa1f99a7e45b306c6736888e280f527c)

@ ESPI\_VWIRE\_SIGNAL\_SCI

**Definition** espi.h:230

[ESPI\_PC\_EVT\_BUS\_MASTER\_ENABLE](group__espi__interface.md#ggac55098842dd9d181144ac4b4122a610ea0e245cbeef479218d4e6c9bec57e40d1)

@ ESPI\_PC\_EVT\_BUS\_MASTER\_ENABLE

**Definition** espi.h:130

[ESPI\_PC\_EVT\_BUS\_CHANNEL\_READY](group__espi__interface.md#ggac55098842dd9d181144ac4b4122a610ea68ecb52b04ffddcc93fbcc77d3643687)

@ ESPI\_PC\_EVT\_BUS\_CHANNEL\_READY

**Definition** espi.h:129

[EACPI\_READ\_STS](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea02bf8538a66f633e3d2ec094f57c6173)

@ EACPI\_READ\_STS

**Definition** espi.h:282

[EACPI\_WRITE\_STS](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea02c7b1c69d803a5c45304260786afb6f)

@ EACPI\_WRITE\_STS

**Definition** espi.h:283

[EACPI\_IBF\_HAS\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea09f241a3f6ffcb5b7839c81c7fc4ea6e)

@ EACPI\_IBF\_HAS\_CHAR

**Definition** espi.h:278

[EACPI\_OBF\_HAS\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea3cce8bd0205691ecda53fc469606929d)

@ EACPI\_OBF\_HAS\_CHAR

**Definition** espi.h:277

[E8042\_CLEAR\_FLAG](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea5c592b1cad381b296cde832c67264cd1)

@ E8042\_CLEAR\_FLAG

**Definition** espi.h:275

[E8042\_PAUSE\_IRQ](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea5e7205b5f1371f1a0f2eaed299389475)

@ E8042\_PAUSE\_IRQ

**Definition** espi.h:270

[EACPI\_WRITE\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea689643f6feb724a303d3b790ff2899f7)

@ EACPI\_WRITE\_CHAR

**Definition** espi.h:280

[E8042\_SET\_FLAG](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea83266d88740588d45be6667a4034c447)

@ E8042\_SET\_FLAG

**Definition** espi.h:274

[E8042\_READ\_KB\_STS](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310ea8c62cd1266681c88aa0cb1af65ab551b)

@ E8042\_READ\_KB\_STS

**Definition** espi.h:273

[E8042\_WRITE\_KB\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eaa9135a5ea9a5ebd9d25660c37983c5d6)

@ E8042\_WRITE\_KB\_CHAR

**Definition** espi.h:266

[E8042\_WRITE\_MB\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eaaef0649f867424ec0c7889acb7354911)

@ E8042\_WRITE\_MB\_CHAR

**Definition** espi.h:267

[E8042\_IBF\_HAS\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eab70684413d736c8583f3dc53f14b7c7a)

@ E8042\_IBF\_HAS\_CHAR

**Definition** espi.h:264

[E8042\_OBF\_HAS\_CHAR](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eac172afb38cb38970ef6242a4f45132f9)

@ E8042\_OBF\_HAS\_CHAR

**Definition** espi.h:263

[E8042\_RESUME\_IRQ](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eac5b666b3319dc2ef0fc571684c2ea198)

@ E8042\_RESUME\_IRQ

**Definition** espi.h:269

[E8042\_CLEAR\_OBF](group__espi__interface.md#ggad00b6a22843e5df9c6d6945d0d82310eacdeb74a9534310f5dab3f1bfb5def534)

@ E8042\_CLEAR\_OBF

**Definition** espi.h:271

[ESPI\_CHANNEL\_OOB](group__espi__interface.md#ggafaa3f7d54503c901ab23bd79a7f8a755a0ccb80544cbda501cc90ea0c3b868e54)

@ ESPI\_CHANNEL\_OOB

**Definition** espi.h:105

[ESPI\_CHANNEL\_PERIPHERAL](group__espi__interface.md#ggafaa3f7d54503c901ab23bd79a7f8a755a32f636bbad2618a6b1554656d3b53206)

@ ESPI\_CHANNEL\_PERIPHERAL

**Definition** espi.h:103

[ESPI\_CHANNEL\_FLASH](group__espi__interface.md#ggafaa3f7d54503c901ab23bd79a7f8a755a5616bf2bf49a8c457fcc2f27d9fe0518)

@ ESPI\_CHANNEL\_FLASH

**Definition** espi.h:106

[ESPI\_CHANNEL\_VWIRE](group__espi__interface.md#ggafaa3f7d54503c901ab23bd79a7f8a755ac2e84a127870ff50359cf96528c9a7c6)

@ ESPI\_CHANNEL\_VWIRE

**Definition** espi.h:104

[flash\_erase](group__flash__interface.md#ga05f9c8b0c1ff7273f71797e7ff799c95)

int flash\_erase(const struct device \*dev, off\_t offset, size\_t size)

Erase part or all of a flash memory.

[flash\_write](group__flash__interface.md#ga76d7880cc5e18ca40237736d3bd94324)

int flash\_write(const struct device \*dev, off\_t offset, const void \*data, size\_t len)

Write buffer into flash memory.

[flash\_read](group__flash__interface.md#gaa7c9382796aad64da0da683f54600b5f)

int flash\_read(const struct device \*dev, off\_t offset, void \*data, size\_t len)

Read data from flash.

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:115

[types.h](include_2zephyr_2types_8h.md)

[slist.h](slist_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:397

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:393

[espi\_cfg](structespi__cfg.md)

eSPI bus configuration parameters

**Definition** espi.h:335

[espi\_cfg::io\_caps](structespi__cfg.md#a75175c60a31c3a88c83772b99c2a5c34)

enum espi\_io\_mode io\_caps

Supported I/O mode.

**Definition** espi.h:337

[espi\_cfg::channel\_caps](structespi__cfg.md#abb24c88ecc977d8116973d44a7e7cb94)

enum espi\_channel channel\_caps

Supported channels.

**Definition** espi.h:339

[espi\_cfg::max\_freq](structespi__cfg.md#aed88dd6fc8028a7c281260e7fa29ce21)

uint8\_t max\_freq

Maximum supported frequency in MHz.

**Definition** espi.h:341

[espi\_event](structespi__event.md)

eSPI event

**Definition** espi.h:323

[espi\_event::evt\_data](structespi__event.md#aa0491cbed5bec091721dfa14898b7277)

uint32\_t evt\_data

Data associated to the event.

**Definition** espi.h:329

[espi\_event::evt\_type](structespi__event.md#acac75eb1d2b384aa337a5240825b635f)

enum espi\_bus\_event evt\_type

Event type.

**Definition** espi.h:325

[espi\_event::evt\_details](structespi__event.md#aea36925bd3f599c1481c9cc867795c33)

uint32\_t evt\_details

Additional details for bus event type.

**Definition** espi.h:327

[espi\_evt\_data\_acpi](structespi__evt__data__acpi.md)

Bit field definition of evt\_data in struct espi\_event for ACPI.

**Definition** espi.h:314

[espi\_evt\_data\_acpi::data](structespi__evt__data__acpi.md#a8fb3633a97b1af7618b391539f576c6f)

uint32\_t data

**Definition** espi.h:316

[espi\_evt\_data\_acpi::type](structespi__evt__data__acpi.md#aa5d1e0b548e9be6b65daf67316df8bfe)

uint32\_t type

**Definition** espi.h:315

[espi\_evt\_data\_acpi::reserved](structespi__evt__data__acpi.md#acb291c371bb201d0ceb739fca7e22d3b)

uint32\_t reserved

**Definition** espi.h:317

[espi\_evt\_data\_kbc](structespi__evt__data__kbc.md)

Bit field definition of evt\_data in struct espi\_event for KBC.

**Definition** espi.h:304

[espi\_evt\_data\_kbc::reserved](structespi__evt__data__kbc.md#a0c17b320752b11dc04926df2965807b2)

uint32\_t reserved

**Definition** espi.h:308

[espi\_evt\_data\_kbc::evt](structespi__evt__data__kbc.md#a55e94583f10481a2cdc34ad7ba388f2f)

uint32\_t evt

**Definition** espi.h:307

[espi\_evt\_data\_kbc::data](structespi__evt__data__kbc.md#a5f56bd66943cc82825bb1725bf8a2966)

uint32\_t data

**Definition** espi.h:306

[espi\_evt\_data\_kbc::type](structespi__evt__data__kbc.md#a75294f9d88f6dfad7bb56e5af5613c64)

uint32\_t type

**Definition** espi.h:305

[espi\_flash\_packet](structespi__flash__packet.md)

eSPI flash transactions packet format

**Definition** espi.h:366

[espi\_flash\_packet::buf](structespi__flash__packet.md#a22244bc4063618707eea571f170bdfde)

uint8\_t \* buf

**Definition** espi.h:367

[espi\_flash\_packet::flash\_addr](structespi__flash__packet.md#ac638c0b5d0d98e15ab66850afc394cec)

uint32\_t flash\_addr

**Definition** espi.h:368

[espi\_flash\_packet::len](structespi__flash__packet.md#adade51336ae37a519c06b12bf19fc86d)

uint16\_t len

**Definition** espi.h:369

[espi\_oob\_packet](structespi__oob__packet.md)

eSPI out-of-band transaction packet format

**Definition** espi.h:358

[espi\_oob\_packet::buf](structespi__oob__packet.md#a0b19890b5e63ecbd1b95eef57fd9263f)

uint8\_t \* buf

**Definition** espi.h:359

[espi\_oob\_packet::len](structespi__oob__packet.md#adf45a10c88a171df8e7138929958b346)

uint16\_t len

**Definition** espi.h:360

[espi\_request\_packet](structespi__request__packet.md)

eSPI peripheral request packet format

**Definition** espi.h:347

[espi\_request\_packet::tag](structespi__request__packet.md#a22a0111e338827125eaf79ce8516b744)

uint8\_t tag

**Definition** espi.h:349

[espi\_request\_packet::address](structespi__request__packet.md#a4ac2d50786fdc4c4bd8da88bde28f77d)

uint32\_t address

**Definition** espi.h:351

[espi\_request\_packet::data](structespi__request__packet.md#a6f808763faf949ff7ef83d68fb71e7ba)

uint8\_t \* data

**Definition** espi.h:352

[espi\_request\_packet::cycle\_type](structespi__request__packet.md#a9b474155dfa0c74d0bd55e4b831b383a)

enum espi\_cycle\_type cycle\_type

**Definition** espi.h:348

[espi\_request\_packet::len](structespi__request__packet.md#ae8b7dc12b04f469b5689ad27cc4f0643)

uint16\_t len

**Definition** espi.h:350

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [espi.h](espi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
