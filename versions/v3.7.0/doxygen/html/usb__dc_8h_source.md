---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/usb__dc_8h_source.html
original_path: doxygen/html/usb__dc_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_dc.h

[Go to the documentation of this file.](usb__dc_8h.md)

1/\* usb\_dc.h - USB device controller driver interface \*/

2

3/\*

4 \* Copyright (c) 2016 Intel Corporation.

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

16

17#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_USB\_USB\_DC\_H\_

18#define ZEPHYR\_INCLUDE\_DRIVERS\_USB\_USB\_DC\_H\_

19

20#include <[zephyr/device.h](device_8h.md)>

21

27

[ 33](group____usb__device__controller__api.md#gac09e3e0af1a2b41a5bfbad91f900baf7)enum [usb\_dc\_status\_code](group____usb__device__controller__api.md#gac09e3e0af1a2b41a5bfbad91f900baf7) {

[ 35](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a8c34e2279a64268809170d6b7f08ed14) [USB\_DC\_ERROR](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a8c34e2279a64268809170d6b7f08ed14),

[ 37](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a6486b0e1a9f4c68fd3bc3b6b3354daa6) [USB\_DC\_RESET](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a6486b0e1a9f4c68fd3bc3b6b3354daa6),

[ 39](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a643918c145a481a36bda37ae5b36599f) [USB\_DC\_CONNECTED](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a643918c145a481a36bda37ae5b36599f),

[ 41](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a63372b97af29a434d58a970439afc23f) [USB\_DC\_CONFIGURED](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a63372b97af29a434d58a970439afc23f),

[ 43](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a3584740de2622bf915e67fee6104da4c) [USB\_DC\_DISCONNECTED](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a3584740de2622bf915e67fee6104da4c),

[ 45](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7afb40fc53f01c4e947a7d4c85a1a21c87) [USB\_DC\_SUSPEND](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7afb40fc53f01c4e947a7d4c85a1a21c87),

[ 47](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a306cbcf313be2111434f3e29b787de1d) [USB\_DC\_RESUME](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a306cbcf313be2111434f3e29b787de1d),

[ 49](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a65828d350f0cd42be7f8406624eb3828) [USB\_DC\_INTERFACE](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a65828d350f0cd42be7f8406624eb3828),

[ 51](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a426477e3ab4378cb0783523346e5ff23) [USB\_DC\_SET\_HALT](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a426477e3ab4378cb0783523346e5ff23),

[ 53](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a25d070f91c1e3ff0382b360f5ac2d501) [USB\_DC\_CLEAR\_HALT](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a25d070f91c1e3ff0382b360f5ac2d501),

[ 55](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7abe89e0ffc160ffd1d8ae88d3771fcbc0) [USB\_DC\_SOF](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7abe89e0ffc160ffd1d8ae88d3771fcbc0),

[ 57](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a8a0f6af1f3625530c9ecdfb2409205d9) [USB\_DC\_UNKNOWN](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a8a0f6af1f3625530c9ecdfb2409205d9)

58};

59

[ 65](group____usb__device__controller__api.md#gaf7f083f61e1406e7d41513113dccd3bd)enum [usb\_dc\_ep\_cb\_status\_code](group____usb__device__controller__api.md#gaf7f083f61e1406e7d41513113dccd3bd) {

[ 67](group____usb__device__controller__api.md#ggaf7f083f61e1406e7d41513113dccd3bdabeb0ca69354218c5efc14c4ddbdf1c27) [USB\_DC\_EP\_SETUP](group____usb__device__controller__api.md#ggaf7f083f61e1406e7d41513113dccd3bdabeb0ca69354218c5efc14c4ddbdf1c27),

[ 69](group____usb__device__controller__api.md#ggaf7f083f61e1406e7d41513113dccd3bda1801d1ba252ed6a0e573c46e76ae1f78) [USB\_DC\_EP\_DATA\_OUT](group____usb__device__controller__api.md#ggaf7f083f61e1406e7d41513113dccd3bda1801d1ba252ed6a0e573c46e76ae1f78),

[ 71](group____usb__device__controller__api.md#ggaf7f083f61e1406e7d41513113dccd3bdae2f497d34e18d6431ab886d120bd124c) [USB\_DC\_EP\_DATA\_IN](group____usb__device__controller__api.md#ggaf7f083f61e1406e7d41513113dccd3bdae2f497d34e18d6431ab886d120bd124c)

72};

73

[ 77](group____usb__device__controller__api.md#gaca68e4a7c3c0a984d1df23794cfa7d87)enum [usb\_dc\_ep\_transfer\_type](group____usb__device__controller__api.md#gaca68e4a7c3c0a984d1df23794cfa7d87) {

[ 79](group____usb__device__controller__api.md#ggaca68e4a7c3c0a984d1df23794cfa7d87a10c7e329a8eceb8cc693b77743f43681) [USB\_DC\_EP\_CONTROL](group____usb__device__controller__api.md#ggaca68e4a7c3c0a984d1df23794cfa7d87a10c7e329a8eceb8cc693b77743f43681) = 0,

[ 81](group____usb__device__controller__api.md#ggaca68e4a7c3c0a984d1df23794cfa7d87a75c49ff44a9729723af190640a710ab6) [USB\_DC\_EP\_ISOCHRONOUS](group____usb__device__controller__api.md#ggaca68e4a7c3c0a984d1df23794cfa7d87a75c49ff44a9729723af190640a710ab6),

[ 83](group____usb__device__controller__api.md#ggaca68e4a7c3c0a984d1df23794cfa7d87aa0ecbc47a337243efd86155cb4ca54fe) [USB\_DC\_EP\_BULK](group____usb__device__controller__api.md#ggaca68e4a7c3c0a984d1df23794cfa7d87aa0ecbc47a337243efd86155cb4ca54fe),

[ 85](group____usb__device__controller__api.md#ggaca68e4a7c3c0a984d1df23794cfa7d87aa70b161209601f1d7a43c5ebcc197b73) [USB\_DC\_EP\_INTERRUPT](group____usb__device__controller__api.md#ggaca68e4a7c3c0a984d1df23794cfa7d87aa70b161209601f1d7a43c5ebcc197b73)

86};

87

[ 93](group____usb__device__controller__api.md#gae247c1ce7213e35d7ce74598225fa428)enum [usb\_dc\_ep\_synchronozation\_type](group____usb__device__controller__api.md#gae247c1ce7213e35d7ce74598225fa428) {

[ 95](group____usb__device__controller__api.md#ggae247c1ce7213e35d7ce74598225fa428a98061a0e90201b01c7b9b04b51eb0da8) [USB\_DC\_EP\_NO\_SYNCHRONIZATION](group____usb__device__controller__api.md#ggae247c1ce7213e35d7ce74598225fa428a98061a0e90201b01c7b9b04b51eb0da8) = (0U << 2U),

[ 97](group____usb__device__controller__api.md#ggae247c1ce7213e35d7ce74598225fa428a8cb40e0f2b85da1adfc005fbd5f9f45d) [USB\_DC\_EP\_ASYNCHRONOUS](group____usb__device__controller__api.md#ggae247c1ce7213e35d7ce74598225fa428a8cb40e0f2b85da1adfc005fbd5f9f45d) = (1U << 2U),

[ 99](group____usb__device__controller__api.md#ggae247c1ce7213e35d7ce74598225fa428a13e7d8970d0723b36a17ae8a29dc9151) [USB\_DC\_EP\_ADAPTIVE](group____usb__device__controller__api.md#ggae247c1ce7213e35d7ce74598225fa428a13e7d8970d0723b36a17ae8a29dc9151) = (2U << 2U),

[ 101](group____usb__device__controller__api.md#ggae247c1ce7213e35d7ce74598225fa428a70976afffbf9a9ef89eb51453c4307c5) [USB\_DC\_EP\_SYNCHRONOUS](group____usb__device__controller__api.md#ggae247c1ce7213e35d7ce74598225fa428a70976afffbf9a9ef89eb51453c4307c5) = (3U << 2U)

102};

103

[ 109](structusb__dc__ep__cfg__data.md)struct [usb\_dc\_ep\_cfg\_data](structusb__dc__ep__cfg__data.md) {

[ 115](structusb__dc__ep__cfg__data.md#aba57a59450c93db5935e2ca08c94aa8b) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [ep\_addr](structusb__dc__ep__cfg__data.md#aba57a59450c93db5935e2ca08c94aa8b);

[ 117](structusb__dc__ep__cfg__data.md#a497bc16439e98415f383a680a0c4d008) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ep\_mps](structusb__dc__ep__cfg__data.md#a497bc16439e98415f383a680a0c4d008);

[ 121](structusb__dc__ep__cfg__data.md#a689682e1df951fd2fd492dda5e03cf08) enum [usb\_dc\_ep\_transfer\_type](group____usb__device__controller__api.md#gaca68e4a7c3c0a984d1df23794cfa7d87) [ep\_type](structusb__dc__ep__cfg__data.md#a689682e1df951fd2fd492dda5e03cf08);

122};

123

[ 127](group____usb__device__controller__api.md#gad75ee35cdfb5dc4f1fad0e615067cb70)typedef void (\*[usb\_dc\_ep\_callback](group____usb__device__controller__api.md#gad75ee35cdfb5dc4f1fad0e615067cb70))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep,

128 enum [usb\_dc\_ep\_cb\_status\_code](group____usb__device__controller__api.md#gaf7f083f61e1406e7d41513113dccd3bd) cb\_status);

129

[ 133](group____usb__device__controller__api.md#ga2ddb0b059b4e1e76473ed7f56d0cf2ee)typedef void (\*[usb\_dc\_status\_callback](group____usb__device__controller__api.md#ga2ddb0b059b4e1e76473ed7f56d0cf2ee))(enum [usb\_dc\_status\_code](group____usb__device__controller__api.md#gac09e3e0af1a2b41a5bfbad91f900baf7) cb\_status,

134 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*param);

135

[ 145](group____usb__device__controller__api.md#gaf78984e6103185c6ebadee2fcbdf62f7)int [usb\_dc\_attach](group____usb__device__controller__api.md#gaf78984e6103185c6ebadee2fcbdf62f7)(void);

146

[ 155](group____usb__device__controller__api.md#ga062b4c8b618f2e964984786baf635a93)int [usb\_dc\_detach](group____usb__device__controller__api.md#ga062b4c8b618f2e964984786baf635a93)(void);

156

[ 165](group____usb__device__controller__api.md#ga8a72b00cfa90dcde41daa228791b61da)int [usb\_dc\_reset](group____usb__device__controller__api.md#ga8a72b00cfa90dcde41daa228791b61da)(void);

166

[ 174](group____usb__device__controller__api.md#ga54a8280e4b011eff3640f6d21af1c292)int [usb\_dc\_set\_address](group____usb__device__controller__api.md#ga54a8280e4b011eff3640f6d21af1c292)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr);

175

[ 185](group____usb__device__controller__api.md#ga478eb2e57635ea816fd6acc8cb9a9424)void [usb\_dc\_set\_status\_callback](group____usb__device__controller__api.md#ga478eb2e57635ea816fd6acc8cb9a9424)(const [usb\_dc\_status\_callback](group____usb__device__controller__api.md#ga2ddb0b059b4e1e76473ed7f56d0cf2ee) cb);

186

[ 200](group____usb__device__controller__api.md#gab6b9ca74059ff2285bd301e9264df45b)int [usb\_dc\_ep\_check\_cap](group____usb__device__controller__api.md#gab6b9ca74059ff2285bd301e9264df45b)(const struct [usb\_dc\_ep\_cfg\_data](structusb__dc__ep__cfg__data.md) \* const cfg);

201

[ 213](group____usb__device__controller__api.md#ga858a4e1bf2c35f5a0ec333801e75b718)int [usb\_dc\_ep\_configure](group____usb__device__controller__api.md#ga858a4e1bf2c35f5a0ec333801e75b718)(const struct [usb\_dc\_ep\_cfg\_data](structusb__dc__ep__cfg__data.md) \* const cfg);

214

[ 223](group____usb__device__controller__api.md#ga68fcfcfe36a36cef202586686c5d30e3)int [usb\_dc\_ep\_set\_stall](group____usb__device__controller__api.md#ga68fcfcfe36a36cef202586686c5d30e3)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

224

[ 233](group____usb__device__controller__api.md#gab89ebb3049f7fd7a1e764ffef16b1b64)int [usb\_dc\_ep\_clear\_stall](group____usb__device__controller__api.md#gab89ebb3049f7fd7a1e764ffef16b1b64)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

234

[ 244](group____usb__device__controller__api.md#gaff2d98b0b6d4ae409b9961a7a123b326)int [usb\_dc\_ep\_is\_stalled](group____usb__device__controller__api.md#gaff2d98b0b6d4ae409b9961a7a123b326)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const stalled);

245

[ 254](group____usb__device__controller__api.md#ga821d65d9872ebb62bfaee79afbb80004)int [usb\_dc\_ep\_halt](group____usb__device__controller__api.md#ga821d65d9872ebb62bfaee79afbb80004)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

255

[ 268](group____usb__device__controller__api.md#ga199aaf51e878cadc0e4ad65007a5a622)int [usb\_dc\_ep\_enable](group____usb__device__controller__api.md#ga199aaf51e878cadc0e4ad65007a5a622)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

269

[ 282](group____usb__device__controller__api.md#ga0154d6b5d462fa2a9db174a985259429)int [usb\_dc\_ep\_disable](group____usb__device__controller__api.md#ga0154d6b5d462fa2a9db174a985259429)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

283

[ 294](group____usb__device__controller__api.md#ga8f702709dd2ed8257d61a8593c4c3b0d)int [usb\_dc\_ep\_flush](group____usb__device__controller__api.md#ga8f702709dd2ed8257d61a8593c4c3b0d)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

295

[ 314](group____usb__device__controller__api.md#gad0b822f08c4a29a46aaa8fa8b30d58ef)int [usb\_dc\_ep\_write](group____usb__device__controller__api.md#gad0b822f08c4a29a46aaa8fa8b30d58ef)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const data,

315 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* const ret\_bytes);

316

[ 336](group____usb__device__controller__api.md#ga8b51a93295c7f9d3b15f4bfe8a09bb11)int [usb\_dc\_ep\_read](group____usb__device__controller__api.md#ga8b51a93295c7f9d3b15f4bfe8a09bb11)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const data,

337 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*const read\_bytes);

338

[ 353](group____usb__device__controller__api.md#gaba2134e2a7b8d870860903aead03b418)int [usb\_dc\_ep\_set\_callback](group____usb__device__controller__api.md#gaba2134e2a7b8d870860903aead03b418)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [usb\_dc\_ep\_callback](group____usb__device__controller__api.md#gad75ee35cdfb5dc4f1fad0e615067cb70) cb);

354

[ 373](group____usb__device__controller__api.md#ga012fb4d99870e1e30e0ecd4ac2b22312)int [usb\_dc\_ep\_read\_wait](group____usb__device__controller__api.md#ga012fb4d99870e1e30e0ecd4ac2b22312)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_data\_len,

374 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*read\_bytes);

375

[ 389](group____usb__device__controller__api.md#ga9694ad0cc1ee84a4ed9de4f2860d4ae6)int [usb\_dc\_ep\_read\_continue](group____usb__device__controller__api.md#ga9694ad0cc1ee84a4ed9de4f2860d4ae6)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

390

[ 399](group____usb__device__controller__api.md#ga6e97104269bfe6dd08f5d0bbb791390e)int [usb\_dc\_ep\_mps](group____usb__device__controller__api.md#ga6e97104269bfe6dd08f5d0bbb791390e)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep);

400

[ 408](group____usb__device__controller__api.md#ga459110125c2a52da95b5b2c3c6fff096)int [usb\_dc\_wakeup\_request](group____usb__device__controller__api.md#ga459110125c2a52da95b5b2c3c6fff096)(void);

409

413

414#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_USB\_USB\_DC\_H\_ \*/

[device.h](device_8h.md)

[usb\_dc\_ep\_read\_wait](group____usb__device__controller__api.md#ga012fb4d99870e1e30e0ecd4ac2b22312)

int usb\_dc\_ep\_read\_wait(uint8\_t ep, uint8\_t \*data, uint32\_t max\_data\_len, uint32\_t \*read\_bytes)

Read data from the specified endpoint.

[usb\_dc\_ep\_disable](group____usb__device__controller__api.md#ga0154d6b5d462fa2a9db174a985259429)

int usb\_dc\_ep\_disable(const uint8\_t ep)

Disable the selected endpoint.

[usb\_dc\_detach](group____usb__device__controller__api.md#ga062b4c8b618f2e964984786baf635a93)

int usb\_dc\_detach(void)

Detach the USB device.

[usb\_dc\_ep\_enable](group____usb__device__controller__api.md#ga199aaf51e878cadc0e4ad65007a5a622)

int usb\_dc\_ep\_enable(const uint8\_t ep)

Enable the selected endpoint.

[usb\_dc\_status\_callback](group____usb__device__controller__api.md#ga2ddb0b059b4e1e76473ed7f56d0cf2ee)

void(\* usb\_dc\_status\_callback)(enum usb\_dc\_status\_code cb\_status, const uint8\_t \*param)

Callback function signature for the device.

**Definition** usb\_dc.h:133

[usb\_dc\_wakeup\_request](group____usb__device__controller__api.md#ga459110125c2a52da95b5b2c3c6fff096)

int usb\_dc\_wakeup\_request(void)

Start the host wake up procedure.

[usb\_dc\_set\_status\_callback](group____usb__device__controller__api.md#ga478eb2e57635ea816fd6acc8cb9a9424)

void usb\_dc\_set\_status\_callback(const usb\_dc\_status\_callback cb)

Set USB device controller status callback.

[usb\_dc\_set\_address](group____usb__device__controller__api.md#ga54a8280e4b011eff3640f6d21af1c292)

int usb\_dc\_set\_address(const uint8\_t addr)

Set USB device address.

[usb\_dc\_ep\_set\_stall](group____usb__device__controller__api.md#ga68fcfcfe36a36cef202586686c5d30e3)

int usb\_dc\_ep\_set\_stall(const uint8\_t ep)

Set stall condition for the selected endpoint.

[usb\_dc\_ep\_mps](group____usb__device__controller__api.md#ga6e97104269bfe6dd08f5d0bbb791390e)

int usb\_dc\_ep\_mps(uint8\_t ep)

Get endpoint max packet size.

[usb\_dc\_ep\_halt](group____usb__device__controller__api.md#ga821d65d9872ebb62bfaee79afbb80004)

int usb\_dc\_ep\_halt(const uint8\_t ep)

Halt the selected endpoint.

[usb\_dc\_ep\_configure](group____usb__device__controller__api.md#ga858a4e1bf2c35f5a0ec333801e75b718)

int usb\_dc\_ep\_configure(const struct usb\_dc\_ep\_cfg\_data \*const cfg)

Configure endpoint.

[usb\_dc\_reset](group____usb__device__controller__api.md#ga8a72b00cfa90dcde41daa228791b61da)

int usb\_dc\_reset(void)

Reset the USB device.

[usb\_dc\_ep\_read](group____usb__device__controller__api.md#ga8b51a93295c7f9d3b15f4bfe8a09bb11)

int usb\_dc\_ep\_read(const uint8\_t ep, uint8\_t \*const data, const uint32\_t max\_data\_len, uint32\_t \*const read\_bytes)

Read data from the specified endpoint.

[usb\_dc\_ep\_flush](group____usb__device__controller__api.md#ga8f702709dd2ed8257d61a8593c4c3b0d)

int usb\_dc\_ep\_flush(const uint8\_t ep)

Flush the selected endpoint.

[usb\_dc\_ep\_read\_continue](group____usb__device__controller__api.md#ga9694ad0cc1ee84a4ed9de4f2860d4ae6)

int usb\_dc\_ep\_read\_continue(uint8\_t ep)

Continue reading data from the endpoint.

[usb\_dc\_ep\_check\_cap](group____usb__device__controller__api.md#gab6b9ca74059ff2285bd301e9264df45b)

int usb\_dc\_ep\_check\_cap(const struct usb\_dc\_ep\_cfg\_data \*const cfg)

check endpoint capabilities

[usb\_dc\_ep\_clear\_stall](group____usb__device__controller__api.md#gab89ebb3049f7fd7a1e764ffef16b1b64)

int usb\_dc\_ep\_clear\_stall(const uint8\_t ep)

Clear stall condition for the selected endpoint.

[usb\_dc\_ep\_set\_callback](group____usb__device__controller__api.md#gaba2134e2a7b8d870860903aead03b418)

int usb\_dc\_ep\_set\_callback(const uint8\_t ep, const usb\_dc\_ep\_callback cb)

Set callback function for the specified endpoint.

[usb\_dc\_status\_code](group____usb__device__controller__api.md#gac09e3e0af1a2b41a5bfbad91f900baf7)

usb\_dc\_status\_code

USB Driver Status Codes.

**Definition** usb\_dc.h:33

[usb\_dc\_ep\_transfer\_type](group____usb__device__controller__api.md#gaca68e4a7c3c0a984d1df23794cfa7d87)

usb\_dc\_ep\_transfer\_type

USB Endpoint Transfer Type.

**Definition** usb\_dc.h:77

[usb\_dc\_ep\_write](group____usb__device__controller__api.md#gad0b822f08c4a29a46aaa8fa8b30d58ef)

int usb\_dc\_ep\_write(const uint8\_t ep, const uint8\_t \*const data, const uint32\_t data\_len, uint32\_t \*const ret\_bytes)

Write data to the specified endpoint.

[usb\_dc\_ep\_callback](group____usb__device__controller__api.md#gad75ee35cdfb5dc4f1fad0e615067cb70)

void(\* usb\_dc\_ep\_callback)(uint8\_t ep, enum usb\_dc\_ep\_cb\_status\_code cb\_status)

Callback function signature for the USB Endpoint status.

**Definition** usb\_dc.h:127

[usb\_dc\_ep\_synchronozation\_type](group____usb__device__controller__api.md#gae247c1ce7213e35d7ce74598225fa428)

usb\_dc\_ep\_synchronozation\_type

USB Endpoint Synchronization Type.

**Definition** usb\_dc.h:93

[usb\_dc\_attach](group____usb__device__controller__api.md#gaf78984e6103185c6ebadee2fcbdf62f7)

int usb\_dc\_attach(void)

Attach USB for device connection.

[usb\_dc\_ep\_cb\_status\_code](group____usb__device__controller__api.md#gaf7f083f61e1406e7d41513113dccd3bd)

usb\_dc\_ep\_cb\_status\_code

USB Endpoint Callback Status Codes.

**Definition** usb\_dc.h:65

[usb\_dc\_ep\_is\_stalled](group____usb__device__controller__api.md#gaff2d98b0b6d4ae409b9961a7a123b326)

int usb\_dc\_ep\_is\_stalled(const uint8\_t ep, uint8\_t \*const stalled)

Check if the selected endpoint is stalled.

[USB\_DC\_CLEAR\_HALT](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a25d070f91c1e3ff0382b360f5ac2d501)

@ USB\_DC\_CLEAR\_HALT

Clear Feature ENDPOINT\_HALT received.

**Definition** usb\_dc.h:53

[USB\_DC\_RESUME](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a306cbcf313be2111434f3e29b787de1d)

@ USB\_DC\_RESUME

USB connection resumed by the HOST.

**Definition** usb\_dc.h:47

[USB\_DC\_DISCONNECTED](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a3584740de2622bf915e67fee6104da4c)

@ USB\_DC\_DISCONNECTED

USB connection lost.

**Definition** usb\_dc.h:43

[USB\_DC\_SET\_HALT](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a426477e3ab4378cb0783523346e5ff23)

@ USB\_DC\_SET\_HALT

Set Feature ENDPOINT\_HALT received.

**Definition** usb\_dc.h:51

[USB\_DC\_CONFIGURED](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a63372b97af29a434d58a970439afc23f)

@ USB\_DC\_CONFIGURED

USB configuration done.

**Definition** usb\_dc.h:41

[USB\_DC\_CONNECTED](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a643918c145a481a36bda37ae5b36599f)

@ USB\_DC\_CONNECTED

USB connection established, hardware enumeration is completed.

**Definition** usb\_dc.h:39

[USB\_DC\_RESET](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a6486b0e1a9f4c68fd3bc3b6b3354daa6)

@ USB\_DC\_RESET

USB reset.

**Definition** usb\_dc.h:37

[USB\_DC\_INTERFACE](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a65828d350f0cd42be7f8406624eb3828)

@ USB\_DC\_INTERFACE

USB interface selected.

**Definition** usb\_dc.h:49

[USB\_DC\_UNKNOWN](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a8a0f6af1f3625530c9ecdfb2409205d9)

@ USB\_DC\_UNKNOWN

Initial USB connection status.

**Definition** usb\_dc.h:57

[USB\_DC\_ERROR](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a8c34e2279a64268809170d6b7f08ed14)

@ USB\_DC\_ERROR

USB error reported by the controller.

**Definition** usb\_dc.h:35

[USB\_DC\_SOF](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7abe89e0ffc160ffd1d8ae88d3771fcbc0)

@ USB\_DC\_SOF

Start of Frame received.

**Definition** usb\_dc.h:55

[USB\_DC\_SUSPEND](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7afb40fc53f01c4e947a7d4c85a1a21c87)

@ USB\_DC\_SUSPEND

USB connection suspended by the HOST.

**Definition** usb\_dc.h:45

[USB\_DC\_EP\_CONTROL](group____usb__device__controller__api.md#ggaca68e4a7c3c0a984d1df23794cfa7d87a10c7e329a8eceb8cc693b77743f43681)

@ USB\_DC\_EP\_CONTROL

Control type endpoint.

**Definition** usb\_dc.h:79

[USB\_DC\_EP\_ISOCHRONOUS](group____usb__device__controller__api.md#ggaca68e4a7c3c0a984d1df23794cfa7d87a75c49ff44a9729723af190640a710ab6)

@ USB\_DC\_EP\_ISOCHRONOUS

Isochronous type endpoint.

**Definition** usb\_dc.h:81

[USB\_DC\_EP\_BULK](group____usb__device__controller__api.md#ggaca68e4a7c3c0a984d1df23794cfa7d87aa0ecbc47a337243efd86155cb4ca54fe)

@ USB\_DC\_EP\_BULK

Bulk type endpoint.

**Definition** usb\_dc.h:83

[USB\_DC\_EP\_INTERRUPT](group____usb__device__controller__api.md#ggaca68e4a7c3c0a984d1df23794cfa7d87aa70b161209601f1d7a43c5ebcc197b73)

@ USB\_DC\_EP\_INTERRUPT

Interrupt type endpoint.

**Definition** usb\_dc.h:85

[USB\_DC\_EP\_ADAPTIVE](group____usb__device__controller__api.md#ggae247c1ce7213e35d7ce74598225fa428a13e7d8970d0723b36a17ae8a29dc9151)

@ USB\_DC\_EP\_ADAPTIVE

Adaptive.

**Definition** usb\_dc.h:99

[USB\_DC\_EP\_SYNCHRONOUS](group____usb__device__controller__api.md#ggae247c1ce7213e35d7ce74598225fa428a70976afffbf9a9ef89eb51453c4307c5)

@ USB\_DC\_EP\_SYNCHRONOUS

Synchronous.

**Definition** usb\_dc.h:101

[USB\_DC\_EP\_ASYNCHRONOUS](group____usb__device__controller__api.md#ggae247c1ce7213e35d7ce74598225fa428a8cb40e0f2b85da1adfc005fbd5f9f45d)

@ USB\_DC\_EP\_ASYNCHRONOUS

Asynchronous.

**Definition** usb\_dc.h:97

[USB\_DC\_EP\_NO\_SYNCHRONIZATION](group____usb__device__controller__api.md#ggae247c1ce7213e35d7ce74598225fa428a98061a0e90201b01c7b9b04b51eb0da8)

@ USB\_DC\_EP\_NO\_SYNCHRONIZATION

No Synchronization.

**Definition** usb\_dc.h:95

[USB\_DC\_EP\_DATA\_OUT](group____usb__device__controller__api.md#ggaf7f083f61e1406e7d41513113dccd3bda1801d1ba252ed6a0e573c46e76ae1f78)

@ USB\_DC\_EP\_DATA\_OUT

Out transaction on this EP, data is available for read.

**Definition** usb\_dc.h:69

[USB\_DC\_EP\_SETUP](group____usb__device__controller__api.md#ggaf7f083f61e1406e7d41513113dccd3bdabeb0ca69354218c5efc14c4ddbdf1c27)

@ USB\_DC\_EP\_SETUP

SETUP received.

**Definition** usb\_dc.h:67

[USB\_DC\_EP\_DATA\_IN](group____usb__device__controller__api.md#ggaf7f083f61e1406e7d41513113dccd3bdae2f497d34e18d6431ab886d120bd124c)

@ USB\_DC\_EP\_DATA\_IN

In transaction done on this EP.

**Definition** usb\_dc.h:71

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[usb\_dc\_ep\_cfg\_data](structusb__dc__ep__cfg__data.md)

USB Endpoint Configuration.

**Definition** usb\_dc.h:109

[usb\_dc\_ep\_cfg\_data::ep\_mps](structusb__dc__ep__cfg__data.md#a497bc16439e98415f383a680a0c4d008)

uint16\_t ep\_mps

Endpoint max packet size.

**Definition** usb\_dc.h:117

[usb\_dc\_ep\_cfg\_data::ep\_type](structusb__dc__ep__cfg__data.md#a689682e1df951fd2fd492dda5e03cf08)

enum usb\_dc\_ep\_transfer\_type ep\_type

Endpoint Transfer Type.

**Definition** usb\_dc.h:121

[usb\_dc\_ep\_cfg\_data::ep\_addr](structusb__dc__ep__cfg__data.md#aba57a59450c93db5935e2ca08c94aa8b)

uint8\_t ep\_addr

The number associated with the EP in the device configuration structure IN EP = 0x80 | <endpoint numb...

**Definition** usb\_dc.h:115

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb](dir_8780870c85d3e97051f07cf376f058af.md)
- [usb\_dc.h](usb__dc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
