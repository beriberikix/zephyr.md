---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group____usb__device__controller__api.html
original_path: doxygen/html/group____usb__device__controller__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

USB Device Controller API

USB Device Controller API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [usb\_dc\_ep\_cfg\_data](structusb__dc__ep__cfg__data.md) |
|  | USB Endpoint Configuration. [More...](structusb__dc__ep__cfg__data.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [usb\_dc\_ep\_callback](#gad75ee35cdfb5dc4f1fad0e615067cb70)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, enum [usb\_dc\_ep\_cb\_status\_code](#gaf7f083f61e1406e7d41513113dccd3bd) cb\_status) |
|  | Callback function signature for the USB Endpoint status. |
| typedef void(\* | [usb\_dc\_status\_callback](#ga2ddb0b059b4e1e76473ed7f56d0cf2ee)) (enum [usb\_dc\_status\_code](#gac09e3e0af1a2b41a5bfbad91f900baf7) cb\_status, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*param) |
|  | Callback function signature for the device. |

| Enumerations | |
| --- | --- |
| enum | [usb\_dc\_status\_code](#gac09e3e0af1a2b41a5bfbad91f900baf7) {     [USB\_DC\_ERROR](#ggac09e3e0af1a2b41a5bfbad91f900baf7a8c34e2279a64268809170d6b7f08ed14) , [USB\_DC\_RESET](#ggac09e3e0af1a2b41a5bfbad91f900baf7a6486b0e1a9f4c68fd3bc3b6b3354daa6) , [USB\_DC\_CONNECTED](#ggac09e3e0af1a2b41a5bfbad91f900baf7a643918c145a481a36bda37ae5b36599f) , [USB\_DC\_CONFIGURED](#ggac09e3e0af1a2b41a5bfbad91f900baf7a63372b97af29a434d58a970439afc23f) ,     [USB\_DC\_DISCONNECTED](#ggac09e3e0af1a2b41a5bfbad91f900baf7a3584740de2622bf915e67fee6104da4c) , [USB\_DC\_SUSPEND](#ggac09e3e0af1a2b41a5bfbad91f900baf7afb40fc53f01c4e947a7d4c85a1a21c87) , [USB\_DC\_RESUME](#ggac09e3e0af1a2b41a5bfbad91f900baf7a306cbcf313be2111434f3e29b787de1d) , [USB\_DC\_INTERFACE](#ggac09e3e0af1a2b41a5bfbad91f900baf7a65828d350f0cd42be7f8406624eb3828) ,     [USB\_DC\_SET\_HALT](#ggac09e3e0af1a2b41a5bfbad91f900baf7a426477e3ab4378cb0783523346e5ff23) , [USB\_DC\_CLEAR\_HALT](#ggac09e3e0af1a2b41a5bfbad91f900baf7a25d070f91c1e3ff0382b360f5ac2d501) , [USB\_DC\_SOF](#ggac09e3e0af1a2b41a5bfbad91f900baf7abe89e0ffc160ffd1d8ae88d3771fcbc0) , [USB\_DC\_UNKNOWN](#ggac09e3e0af1a2b41a5bfbad91f900baf7a8a0f6af1f3625530c9ecdfb2409205d9)   } |
|  | USB Driver Status Codes. [More...](#gac09e3e0af1a2b41a5bfbad91f900baf7) |
| enum | [usb\_dc\_ep\_cb\_status\_code](#gaf7f083f61e1406e7d41513113dccd3bd) { [USB\_DC\_EP\_SETUP](#ggaf7f083f61e1406e7d41513113dccd3bdabeb0ca69354218c5efc14c4ddbdf1c27) , [USB\_DC\_EP\_DATA\_OUT](#ggaf7f083f61e1406e7d41513113dccd3bda1801d1ba252ed6a0e573c46e76ae1f78) , [USB\_DC\_EP\_DATA\_IN](#ggaf7f083f61e1406e7d41513113dccd3bdae2f497d34e18d6431ab886d120bd124c) } |
|  | USB Endpoint Callback Status Codes. [More...](#gaf7f083f61e1406e7d41513113dccd3bd) |
| enum | [usb\_dc\_ep\_transfer\_type](#gaca68e4a7c3c0a984d1df23794cfa7d87) { [USB\_DC\_EP\_CONTROL](#ggaca68e4a7c3c0a984d1df23794cfa7d87a10c7e329a8eceb8cc693b77743f43681) = 0 , [USB\_DC\_EP\_ISOCHRONOUS](#ggaca68e4a7c3c0a984d1df23794cfa7d87a75c49ff44a9729723af190640a710ab6) , [USB\_DC\_EP\_BULK](#ggaca68e4a7c3c0a984d1df23794cfa7d87aa0ecbc47a337243efd86155cb4ca54fe) , [USB\_DC\_EP\_INTERRUPT](#ggaca68e4a7c3c0a984d1df23794cfa7d87aa70b161209601f1d7a43c5ebcc197b73) } |
|  | USB Endpoint Transfer Type. [More...](#gaca68e4a7c3c0a984d1df23794cfa7d87) |
| enum | [usb\_dc\_ep\_synchronozation\_type](#gae247c1ce7213e35d7ce74598225fa428) { [USB\_DC\_EP\_NO\_SYNCHRONIZATION](#ggae247c1ce7213e35d7ce74598225fa428a98061a0e90201b01c7b9b04b51eb0da8) = (0U << 2U) , [USB\_DC\_EP\_ASYNCHRONOUS](#ggae247c1ce7213e35d7ce74598225fa428a8cb40e0f2b85da1adfc005fbd5f9f45d) = (1U << 2U) , [USB\_DC\_EP\_ADAPTIVE](#ggae247c1ce7213e35d7ce74598225fa428a13e7d8970d0723b36a17ae8a29dc9151) = (2U << 2U) , [USB\_DC\_EP\_SYNCHRONOUS](#ggae247c1ce7213e35d7ce74598225fa428a70976afffbf9a9ef89eb51453c4307c5) = (3U << 2U) } |
|  | USB Endpoint Synchronization Type. [More...](#gae247c1ce7213e35d7ce74598225fa428) |

| Functions | |
| --- | --- |
| int | [usb\_dc\_attach](#gaf78984e6103185c6ebadee2fcbdf62f7) (void) |
|  | Attach USB for device connection. |
| int | [usb\_dc\_detach](#ga062b4c8b618f2e964984786baf635a93) (void) |
|  | Detach the USB device. |
| int | [usb\_dc\_reset](#ga8a72b00cfa90dcde41daa228791b61da) (void) |
|  | Reset the USB device. |
| int | [usb\_dc\_set\_address](#ga54a8280e4b011eff3640f6d21af1c292) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
|  | Set USB device address. |
| void | [usb\_dc\_set\_status\_callback](#ga478eb2e57635ea816fd6acc8cb9a9424) (const [usb\_dc\_status\_callback](#ga2ddb0b059b4e1e76473ed7f56d0cf2ee) cb) |
|  | Set USB device controller status callback. |
| int | [usb\_dc\_ep\_check\_cap](#gab6b9ca74059ff2285bd301e9264df45b) (const struct [usb\_dc\_ep\_cfg\_data](structusb__dc__ep__cfg__data.md) \*const cfg) |
|  | check endpoint capabilities |
| int | [usb\_dc\_ep\_configure](#ga858a4e1bf2c35f5a0ec333801e75b718) (const struct [usb\_dc\_ep\_cfg\_data](structusb__dc__ep__cfg__data.md) \*const cfg) |
|  | Configure endpoint. |
| int | [usb\_dc\_ep\_set\_stall](#ga68fcfcfe36a36cef202586686c5d30e3) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Set stall condition for the selected endpoint. |
| int | [usb\_dc\_ep\_clear\_stall](#gab89ebb3049f7fd7a1e764ffef16b1b64) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Clear stall condition for the selected endpoint. |
| int | [usb\_dc\_ep\_is\_stalled](#gaff2d98b0b6d4ae409b9961a7a123b326) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const stalled) |
|  | Check if the selected endpoint is stalled. |
| int | [usb\_dc\_ep\_halt](#ga821d65d9872ebb62bfaee79afbb80004) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Halt the selected endpoint. |
| int | [usb\_dc\_ep\_enable](#ga199aaf51e878cadc0e4ad65007a5a622) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Enable the selected endpoint. |
| int | [usb\_dc\_ep\_disable](#ga0154d6b5d462fa2a9db174a985259429) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Disable the selected endpoint. |
| int | [usb\_dc\_ep\_flush](#ga8f702709dd2ed8257d61a8593c4c3b0d) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Flush the selected endpoint. |
| int | [usb\_dc\_ep\_write](#gad0b822f08c4a29a46aaa8fa8b30d58ef) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const data, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*const ret\_bytes) |
|  | Write data to the specified endpoint. |
| int | [usb\_dc\_ep\_read](#ga8b51a93295c7f9d3b15f4bfe8a09bb11) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const data, const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*const read\_bytes) |
|  | Read data from the specified endpoint. |
| int | [usb\_dc\_ep\_set\_callback](#gaba2134e2a7b8d870860903aead03b418) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [usb\_dc\_ep\_callback](#gad75ee35cdfb5dc4f1fad0e615067cb70) cb) |
|  | Set callback function for the specified endpoint. |
| int | [usb\_dc\_ep\_read\_wait](#ga012fb4d99870e1e30e0ecd4ac2b22312) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*read\_bytes) |
|  | Read data from the specified endpoint. |
| int | [usb\_dc\_ep\_read\_continue](#ga9694ad0cc1ee84a4ed9de4f2860d4ae6) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Continue reading data from the endpoint. |
| int | [usb\_dc\_ep\_mps](#ga6e97104269bfe6dd08f5d0bbb791390e) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Get endpoint max packet size. |
| int | [usb\_dc\_wakeup\_request](#ga459110125c2a52da95b5b2c3c6fff096) (void) |
|  | Start the host wake up procedure. |

## Detailed Description

USB Device Controller API.

## Typedef Documentation

## [◆ ](#gad75ee35cdfb5dc4f1fad0e615067cb70)usb\_dc\_ep\_callback

| typedef void(\* usb\_dc\_ep\_callback) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, enum [usb\_dc\_ep\_cb\_status\_code](#gaf7f083f61e1406e7d41513113dccd3bd) cb\_status) |
| --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Callback function signature for the USB Endpoint status.

## [◆ ](#ga2ddb0b059b4e1e76473ed7f56d0cf2ee)usb\_dc\_status\_callback

| typedef void(\* usb\_dc\_status\_callback) (enum [usb\_dc\_status\_code](#gac09e3e0af1a2b41a5bfbad91f900baf7) cb\_status, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*param) |
| --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Callback function signature for the device.

## Enumeration Type Documentation

## [◆ ](#gaf7f083f61e1406e7d41513113dccd3bd)usb\_dc\_ep\_cb\_status\_code

| enum [usb\_dc\_ep\_cb\_status\_code](#gaf7f083f61e1406e7d41513113dccd3bd) |
| --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

USB Endpoint Callback Status Codes.

Status Codes reported by the registered endpoint callback.

| Enumerator | |
| --- | --- |
| USB\_DC\_EP\_SETUP | SETUP received. |
| USB\_DC\_EP\_DATA\_OUT | Out transaction on this EP, data is available for read. |
| USB\_DC\_EP\_DATA\_IN | In transaction done on this EP. |

## [◆ ](#gae247c1ce7213e35d7ce74598225fa428)usb\_dc\_ep\_synchronozation\_type

| enum [usb\_dc\_ep\_synchronozation\_type](#gae247c1ce7213e35d7ce74598225fa428) |
| --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

USB Endpoint Synchronization Type.

Note
:   Valid only for Isochronous Endpoints

| Enumerator | |
| --- | --- |
| USB\_DC\_EP\_NO\_SYNCHRONIZATION | No Synchronization. |
| USB\_DC\_EP\_ASYNCHRONOUS | Asynchronous. |
| USB\_DC\_EP\_ADAPTIVE | Adaptive. |
| USB\_DC\_EP\_SYNCHRONOUS | Synchronous. |

## [◆ ](#gaca68e4a7c3c0a984d1df23794cfa7d87)usb\_dc\_ep\_transfer\_type

| enum [usb\_dc\_ep\_transfer\_type](#gaca68e4a7c3c0a984d1df23794cfa7d87) |
| --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

USB Endpoint Transfer Type.

| Enumerator | |
| --- | --- |
| USB\_DC\_EP\_CONTROL | Control type endpoint. |
| USB\_DC\_EP\_ISOCHRONOUS | Isochronous type endpoint. |
| USB\_DC\_EP\_BULK | Bulk type endpoint. |
| USB\_DC\_EP\_INTERRUPT | Interrupt type endpoint. |

## [◆ ](#gac09e3e0af1a2b41a5bfbad91f900baf7)usb\_dc\_status\_code

| enum [usb\_dc\_status\_code](#gac09e3e0af1a2b41a5bfbad91f900baf7) |
| --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

USB Driver Status Codes.

Status codes reported by the registered device status callback.

| Enumerator | |
| --- | --- |
| USB\_DC\_ERROR | USB error reported by the controller. |
| USB\_DC\_RESET | USB reset. |
| USB\_DC\_CONNECTED | USB connection established, hardware enumeration is completed. |
| USB\_DC\_CONFIGURED | USB configuration done. |
| USB\_DC\_DISCONNECTED | USB connection lost. |
| USB\_DC\_SUSPEND | USB connection suspended by the HOST. |
| USB\_DC\_RESUME | USB connection resumed by the HOST. |
| USB\_DC\_INTERFACE | USB interface selected. |
| USB\_DC\_SET\_HALT | Set Feature ENDPOINT\_HALT received. |
| USB\_DC\_CLEAR\_HALT | Clear Feature ENDPOINT\_HALT received. |
| USB\_DC\_SOF | Start of Frame received. |
| USB\_DC\_UNKNOWN | Initial USB connection status. |

## Function Documentation

## [◆ ](#gaf78984e6103185c6ebadee2fcbdf62f7)usb\_dc\_attach()

| int usb\_dc\_attach | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Attach USB for device connection.

Function to attach USB for device connection. Upon success, the USB PLL is enabled, and the USB device is now capable of transmitting and receiving on the USB bus and of generating interrupts.

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga062b4c8b618f2e964984786baf635a93)usb\_dc\_detach()

| int usb\_dc\_detach | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Detach the USB device.

Function to detach the USB device. Upon success, the USB hardware PLL is powered down and USB communication is disabled.

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#gab6b9ca74059ff2285bd301e9264df45b)usb\_dc\_ep\_check\_cap()

| int usb\_dc\_ep\_check\_cap | ( | const struct [usb\_dc\_ep\_cfg\_data](structusb__dc__ep__cfg__data.md) \*const | *cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

check endpoint capabilities

Function to check capabilities of an endpoint. [usb\_dc\_ep\_cfg\_data](structusb__dc__ep__cfg__data.md "USB Endpoint Configuration.") structure provides the endpoint configuration parameters: endpoint address, endpoint maximum packet size and endpoint type. The driver should check endpoint capabilities and return 0 if the endpoint configuration is possible.

Parameters
:   | [in] | cfg | Endpoint config |
    | --- | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#gab89ebb3049f7fd7a1e764ffef16b1b64)usb\_dc\_ep\_clear\_stall()

| int usb\_dc\_ep\_clear\_stall | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Clear stall condition for the selected endpoint.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga858a4e1bf2c35f5a0ec333801e75b718)usb\_dc\_ep\_configure()

| int usb\_dc\_ep\_configure | ( | const struct [usb\_dc\_ep\_cfg\_data](structusb__dc__ep__cfg__data.md) \*const | *cfg* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Configure endpoint.

Function to configure an endpoint. [usb\_dc\_ep\_cfg\_data](structusb__dc__ep__cfg__data.md "USB Endpoint Configuration.") structure provides the endpoint configuration parameters: endpoint address, endpoint maximum packet size and endpoint type.

Parameters
:   | [in] | cfg | Endpoint config |
    | --- | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga0154d6b5d462fa2a9db174a985259429)usb\_dc\_ep\_disable()

| int usb\_dc\_ep\_disable | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Disable the selected endpoint.

Function to disable the selected endpoint. Upon success interrupts are disabled for the corresponding endpoint and the endpoint is no longer able for transmitting/receiving data.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga199aaf51e878cadc0e4ad65007a5a622)usb\_dc\_ep\_enable()

| int usb\_dc\_ep\_enable | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Enable the selected endpoint.

Function to enable the selected endpoint. Upon success interrupts are enabled for the corresponding endpoint and the endpoint is ready for transmitting/receiving data.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga8f702709dd2ed8257d61a8593c4c3b0d)usb\_dc\_ep\_flush()

| int usb\_dc\_ep\_flush | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Flush the selected endpoint.

This function flushes the FIFOs for the selected endpoint.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga821d65d9872ebb62bfaee79afbb80004)usb\_dc\_ep\_halt()

| int usb\_dc\_ep\_halt | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Halt the selected endpoint.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#gaff2d98b0b6d4ae409b9961a7a123b326)usb\_dc\_ep\_is\_stalled()

| int usb\_dc\_ep\_is\_stalled | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const | *stalled* ) |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Check if the selected endpoint is stalled.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |
    | [out] | stalled | Endpoint stall status |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga6e97104269bfe6dd08f5d0bbb791390e)usb\_dc\_ep\_mps()

| int usb\_dc\_ep\_mps | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Get endpoint max packet size.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |

Returns
:   Endpoint max packet size (mps)

## [◆ ](#ga8b51a93295c7f9d3b15f4bfe8a09bb11)usb\_dc\_ep\_read()

| int usb\_dc\_ep\_read | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const | *data*, |
|  |  | const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *max\_data\_len*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*const | *read\_bytes* ) |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Read data from the specified endpoint.

This function is called by the endpoint handler function, after an OUT interrupt has been received for that EP. The application must only call this function through the supplied [usb\_ep\_callback](group____usb__device__core__api.md#ga9a45db26a9be295640ed122533427725 "Callback function signature for the USB Endpoint status.") function. This function clears the ENDPOINT NAK, if all data in the endpoint FIFO has been read, so as to accept more data from host.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |
    | [in] | data | Pointer to data buffer to write to |
    | [in] | max\_data\_len | Max length of data to read |
    | [out] | read\_bytes | Number of bytes read. If data is NULL and max\_data\_len is 0 the number of bytes available for read should be returned. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga9694ad0cc1ee84a4ed9de4f2860d4ae6)usb\_dc\_ep\_read\_continue()

| int usb\_dc\_ep\_read\_continue | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Continue reading data from the endpoint.

Clear the endpoint NAK and enable the endpoint to accept more data from the host. Usually called after [usb\_dc\_ep\_read\_wait()](#ga012fb4d99870e1e30e0ecd4ac2b22312) when the consumer is fine to accept more data. Thus these calls together act as a flow control mechanism.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga012fb4d99870e1e30e0ecd4ac2b22312)usb\_dc\_ep\_read\_wait()

| int usb\_dc\_ep\_read\_wait | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *max\_data\_len*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *read\_bytes* ) |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Read data from the specified endpoint.

This is similar to usb\_dc\_ep\_read, the difference being that, it doesn't clear the endpoint NAKs so that the consumer is not bogged down by further upcalls till he is done with the processing of the data. The caller should reactivate ep by invoking [usb\_dc\_ep\_read\_continue()](#ga9694ad0cc1ee84a4ed9de4f2860d4ae6) do so.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |
    | [in] | data | Pointer to data buffer to write to |
    | [in] | max\_data\_len | Max length of data to read |
    | [out] | read\_bytes | Number of bytes read. If data is NULL and max\_data\_len is 0 the number of bytes available for read should be returned. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#gaba2134e2a7b8d870860903aead03b418)usb\_dc\_ep\_set\_callback()

| int usb\_dc\_ep\_set\_callback | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep*, |
| --- | --- | --- | --- |
|  |  | const [usb\_dc\_ep\_callback](#gad75ee35cdfb5dc4f1fad0e615067cb70) | *cb* ) |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Set callback function for the specified endpoint.

Function to set callback function for notification of data received and available to application or transmit done on the selected endpoint, NULL if callback not required by application code. The callback status code is described by [usb\_dc\_ep\_cb\_status\_code](#gaf7f083f61e1406e7d41513113dccd3bd).

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |
    | [in] | cb | Callback function |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga68fcfcfe36a36cef202586686c5d30e3)usb\_dc\_ep\_set\_stall()

| int usb\_dc\_ep\_set\_stall | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Set stall condition for the selected endpoint.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#gad0b822f08c4a29a46aaa8fa8b30d58ef)usb\_dc\_ep\_write()

| int usb\_dc\_ep\_write | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const | *data*, |
|  |  | const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data\_len*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*const | *ret\_bytes* ) |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Write data to the specified endpoint.

This function is called to write data to the specified endpoint. The supplied [usb\_ep\_callback](group____usb__device__core__api.md#ga9a45db26a9be295640ed122533427725 "Callback function signature for the USB Endpoint status.") function will be called when data is transmitted out.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |
    | [in] | data | Pointer to data to write |
    | [in] | data\_len | Length of the data requested to write. This may be zero for a zero length status packet. |
    | [out] | ret\_bytes | Bytes scheduled for transmission. This value may be NULL if the application expects all bytes to be written |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga8a72b00cfa90dcde41daa228791b61da)usb\_dc\_reset()

| int usb\_dc\_reset | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Reset the USB device.

This function returns the USB device and firmware back to it's initial state. N.B. the USB PLL is handled by the usb\_detach function

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga54a8280e4b011eff3640f6d21af1c292)usb\_dc\_set\_address()

| int usb\_dc\_set\_address | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *addr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Set USB device address.

Parameters
:   | [in] | addr | Device address |
    | --- | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga478eb2e57635ea816fd6acc8cb9a9424)usb\_dc\_set\_status\_callback()

| void usb\_dc\_set\_status\_callback | ( | const [usb\_dc\_status\_callback](#ga2ddb0b059b4e1e76473ed7f56d0cf2ee) | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Set USB device controller status callback.

Function to set USB device controller status callback. The registered callback is used to report changes in the status of the device controller. The status code are described by the [usb\_dc\_status\_code](#gac09e3e0af1a2b41a5bfbad91f900baf7) enumeration.

Parameters
:   | [in] | cb | Callback function |
    | --- | --- | --- |

## [◆ ](#ga459110125c2a52da95b5b2c3c6fff096)usb\_dc\_wakeup\_request()

| int usb\_dc\_wakeup\_request | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_dc.h](usb__dc_8h.md)>`

Start the host wake up procedure.

Function to wake up the host if it's currently in sleep mode.

Returns
:   0 on success, negative errno code on fail.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
