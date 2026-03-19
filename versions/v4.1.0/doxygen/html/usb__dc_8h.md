---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/usb__dc_8h.html
original_path: doxygen/html/usb__dc_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_dc.h File Reference

USB device controller APIs.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`

[Go to the source code of this file.](usb__dc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [usb\_dc\_ep\_cfg\_data](structusb__dc__ep__cfg__data.md) |
|  | USB Endpoint Configuration. [More...](structusb__dc__ep__cfg__data.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [usb\_dc\_ep\_callback](group____usb__device__controller__api.md#gad75ee35cdfb5dc4f1fad0e615067cb70)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, enum [usb\_dc\_ep\_cb\_status\_code](group____usb__device__controller__api.md#gaf7f083f61e1406e7d41513113dccd3bd) cb\_status) |
|  | Callback function signature for the USB Endpoint status. |
| typedef void(\* | [usb\_dc\_status\_callback](group____usb__device__controller__api.md#ga2ddb0b059b4e1e76473ed7f56d0cf2ee)) (enum [usb\_dc\_status\_code](group____usb__device__controller__api.md#gac09e3e0af1a2b41a5bfbad91f900baf7) cb\_status, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*param) |
|  | Callback function signature for the device. |

| Enumerations | |
| --- | --- |
| enum | [usb\_dc\_status\_code](group____usb__device__controller__api.md#gac09e3e0af1a2b41a5bfbad91f900baf7) {     [USB\_DC\_ERROR](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a8c34e2279a64268809170d6b7f08ed14) , [USB\_DC\_RESET](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a6486b0e1a9f4c68fd3bc3b6b3354daa6) , [USB\_DC\_CONNECTED](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a643918c145a481a36bda37ae5b36599f) , [USB\_DC\_CONFIGURED](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a63372b97af29a434d58a970439afc23f) ,     [USB\_DC\_DISCONNECTED](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a3584740de2622bf915e67fee6104da4c) , [USB\_DC\_SUSPEND](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7afb40fc53f01c4e947a7d4c85a1a21c87) , [USB\_DC\_RESUME](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a306cbcf313be2111434f3e29b787de1d) , [USB\_DC\_INTERFACE](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a65828d350f0cd42be7f8406624eb3828) ,     [USB\_DC\_SET\_HALT](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a426477e3ab4378cb0783523346e5ff23) , [USB\_DC\_CLEAR\_HALT](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a25d070f91c1e3ff0382b360f5ac2d501) , [USB\_DC\_SOF](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7abe89e0ffc160ffd1d8ae88d3771fcbc0) , [USB\_DC\_UNKNOWN](group____usb__device__controller__api.md#ggac09e3e0af1a2b41a5bfbad91f900baf7a8a0f6af1f3625530c9ecdfb2409205d9)   } |
|  | USB Driver Status Codes. [More...](group____usb__device__controller__api.md#gac09e3e0af1a2b41a5bfbad91f900baf7) |
| enum | [usb\_dc\_ep\_cb\_status\_code](group____usb__device__controller__api.md#gaf7f083f61e1406e7d41513113dccd3bd) { [USB\_DC\_EP\_SETUP](group____usb__device__controller__api.md#ggaf7f083f61e1406e7d41513113dccd3bdabeb0ca69354218c5efc14c4ddbdf1c27) , [USB\_DC\_EP\_DATA\_OUT](group____usb__device__controller__api.md#ggaf7f083f61e1406e7d41513113dccd3bda1801d1ba252ed6a0e573c46e76ae1f78) , [USB\_DC\_EP\_DATA\_IN](group____usb__device__controller__api.md#ggaf7f083f61e1406e7d41513113dccd3bdae2f497d34e18d6431ab886d120bd124c) } |
|  | USB Endpoint Callback Status Codes. [More...](group____usb__device__controller__api.md#gaf7f083f61e1406e7d41513113dccd3bd) |
| enum | [usb\_dc\_ep\_transfer\_type](group____usb__device__controller__api.md#gaca68e4a7c3c0a984d1df23794cfa7d87) { [USB\_DC\_EP\_CONTROL](group____usb__device__controller__api.md#ggaca68e4a7c3c0a984d1df23794cfa7d87a10c7e329a8eceb8cc693b77743f43681) = 0 , [USB\_DC\_EP\_ISOCHRONOUS](group____usb__device__controller__api.md#ggaca68e4a7c3c0a984d1df23794cfa7d87a75c49ff44a9729723af190640a710ab6) , [USB\_DC\_EP\_BULK](group____usb__device__controller__api.md#ggaca68e4a7c3c0a984d1df23794cfa7d87aa0ecbc47a337243efd86155cb4ca54fe) , [USB\_DC\_EP\_INTERRUPT](group____usb__device__controller__api.md#ggaca68e4a7c3c0a984d1df23794cfa7d87aa70b161209601f1d7a43c5ebcc197b73) } |
|  | USB Endpoint Transfer Type. [More...](group____usb__device__controller__api.md#gaca68e4a7c3c0a984d1df23794cfa7d87) |
| enum | [usb\_dc\_ep\_synchronozation\_type](group____usb__device__controller__api.md#gae247c1ce7213e35d7ce74598225fa428) { [USB\_DC\_EP\_NO\_SYNCHRONIZATION](group____usb__device__controller__api.md#ggae247c1ce7213e35d7ce74598225fa428a98061a0e90201b01c7b9b04b51eb0da8) = (0U << 2U) , [USB\_DC\_EP\_ASYNCHRONOUS](group____usb__device__controller__api.md#ggae247c1ce7213e35d7ce74598225fa428a8cb40e0f2b85da1adfc005fbd5f9f45d) = (1U << 2U) , [USB\_DC\_EP\_ADAPTIVE](group____usb__device__controller__api.md#ggae247c1ce7213e35d7ce74598225fa428a13e7d8970d0723b36a17ae8a29dc9151) = (2U << 2U) , [USB\_DC\_EP\_SYNCHRONOUS](group____usb__device__controller__api.md#ggae247c1ce7213e35d7ce74598225fa428a70976afffbf9a9ef89eb51453c4307c5) = (3U << 2U) } |
|  | USB Endpoint Synchronization Type. [More...](group____usb__device__controller__api.md#gae247c1ce7213e35d7ce74598225fa428) |

| Functions | |
| --- | --- |
| int | [usb\_dc\_attach](group____usb__device__controller__api.md#gaf78984e6103185c6ebadee2fcbdf62f7) (void) |
|  | Attach USB for device connection. |
| int | [usb\_dc\_detach](group____usb__device__controller__api.md#ga062b4c8b618f2e964984786baf635a93) (void) |
|  | Detach the USB device. |
| int | [usb\_dc\_reset](group____usb__device__controller__api.md#ga8a72b00cfa90dcde41daa228791b61da) (void) |
|  | Reset the USB device. |
| int | [usb\_dc\_set\_address](group____usb__device__controller__api.md#ga54a8280e4b011eff3640f6d21af1c292) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
|  | Set USB device address. |
| void | [usb\_dc\_set\_status\_callback](group____usb__device__controller__api.md#ga478eb2e57635ea816fd6acc8cb9a9424) (const [usb\_dc\_status\_callback](group____usb__device__controller__api.md#ga2ddb0b059b4e1e76473ed7f56d0cf2ee) cb) |
|  | Set USB device controller status callback. |
| int | [usb\_dc\_ep\_check\_cap](group____usb__device__controller__api.md#gab6b9ca74059ff2285bd301e9264df45b) (const struct [usb\_dc\_ep\_cfg\_data](structusb__dc__ep__cfg__data.md) \*const cfg) |
|  | check endpoint capabilities |
| int | [usb\_dc\_ep\_configure](group____usb__device__controller__api.md#ga858a4e1bf2c35f5a0ec333801e75b718) (const struct [usb\_dc\_ep\_cfg\_data](structusb__dc__ep__cfg__data.md) \*const cfg) |
|  | Configure endpoint. |
| int | [usb\_dc\_ep\_set\_stall](group____usb__device__controller__api.md#ga68fcfcfe36a36cef202586686c5d30e3) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Set stall condition for the selected endpoint. |
| int | [usb\_dc\_ep\_clear\_stall](group____usb__device__controller__api.md#gab89ebb3049f7fd7a1e764ffef16b1b64) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Clear stall condition for the selected endpoint. |
| int | [usb\_dc\_ep\_is\_stalled](group____usb__device__controller__api.md#gaff2d98b0b6d4ae409b9961a7a123b326) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const stalled) |
|  | Check if the selected endpoint is stalled. |
| int | [usb\_dc\_ep\_halt](group____usb__device__controller__api.md#ga821d65d9872ebb62bfaee79afbb80004) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Halt the selected endpoint. |
| int | [usb\_dc\_ep\_enable](group____usb__device__controller__api.md#ga199aaf51e878cadc0e4ad65007a5a622) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Enable the selected endpoint. |
| int | [usb\_dc\_ep\_disable](group____usb__device__controller__api.md#ga0154d6b5d462fa2a9db174a985259429) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Disable the selected endpoint. |
| int | [usb\_dc\_ep\_flush](group____usb__device__controller__api.md#ga8f702709dd2ed8257d61a8593c4c3b0d) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Flush the selected endpoint. |
| int | [usb\_dc\_ep\_write](group____usb__device__controller__api.md#gad0b822f08c4a29a46aaa8fa8b30d58ef) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const data, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*const ret\_bytes) |
|  | Write data to the specified endpoint. |
| int | [usb\_dc\_ep\_read](group____usb__device__controller__api.md#ga8b51a93295c7f9d3b15f4bfe8a09bb11) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const data, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*const read\_bytes) |
|  | Read data from the specified endpoint. |
| int | [usb\_dc\_ep\_set\_callback](group____usb__device__controller__api.md#gaba2134e2a7b8d870860903aead03b418) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [usb\_dc\_ep\_callback](group____usb__device__controller__api.md#gad75ee35cdfb5dc4f1fad0e615067cb70) cb) |
|  | Set callback function for the specified endpoint. |
| int | [usb\_dc\_ep\_read\_wait](group____usb__device__controller__api.md#ga012fb4d99870e1e30e0ecd4ac2b22312) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*read\_bytes) |
|  | Read data from the specified endpoint. |
| int | [usb\_dc\_ep\_read\_continue](group____usb__device__controller__api.md#ga9694ad0cc1ee84a4ed9de4f2860d4ae6) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Continue reading data from the endpoint. |
| int | [usb\_dc\_ep\_mps](group____usb__device__controller__api.md#ga6e97104269bfe6dd08f5d0bbb791390e) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Get endpoint max packet size. |
| int | [usb\_dc\_wakeup\_request](group____usb__device__controller__api.md#ga459110125c2a52da95b5b2c3c6fff096) (void) |
|  | Start the host wake up procedure. |

## Detailed Description

USB device controller APIs.

This file contains the USB device controller APIs. All device controller drivers should implement the APIs described in this file.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb](dir_8780870c85d3e97051f07cf376f058af.md)
- [usb\_dc.h](usb__dc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
