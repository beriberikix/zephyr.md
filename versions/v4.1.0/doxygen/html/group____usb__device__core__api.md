---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group____usb__device__core__api.html
original_path: doxygen/html/group____usb__device__core__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

USB Device Core API

USB Device Core Layer API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [usb\_ep\_cfg\_data](structusb__ep__cfg__data.md) |
|  | USB Endpoint Configuration. [More...](structusb__ep__cfg__data.md#details) |
| struct | [usb\_interface\_cfg\_data](structusb__interface__cfg__data.md) |
|  | USB Interface Configuration. [More...](structusb__interface__cfg__data.md#details) |
| struct | [usb\_cfg\_data](structusb__cfg__data.md) |
|  | USB device configuration. [More...](structusb__cfg__data.md#details) |

| Macros | |
| --- | --- |
| #define | [USB\_TRANS\_READ](#gabb531b022f5d2d859227a7b35d593d80)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) /\*\* Read transfer flag \*/ |
| #define | [USB\_TRANS\_WRITE](#ga163ee39a47b0a3d9fe3697cc4f24e787)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) /\*\* Write transfer flag \*/ |
| #define | [USB\_TRANS\_NO\_ZLP](#ga81c618544f27e0dc0e556021b0418c40)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) /\*\* No zero-length packet flag \*/ |
| #define | [USB\_DEVICE\_BOS\_DESC\_DEFINE\_CAP](#ga40975f1b023ea36118137e86e099e649)   static \_\_in\_section(usb, bos\_desc\_area, 1) \_\_aligned(1) \_\_used |
|  | Helper macro to place the BOS compatibility descriptor in the right memory section. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [usb\_ep\_callback](#ga9a45db26a9be295640ed122533427725)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, enum [usb\_dc\_ep\_cb\_status\_code](group____usb__device__controller__api.md#gaf7f083f61e1406e7d41513113dccd3bd) cb\_status) |
|  | Callback function signature for the USB Endpoint status. |
| typedef int(\* | [usb\_request\_handler](#gaddacbff094a41c885c3041af72fa6804)) (struct [usb\_setup\_packet](structusb__setup__packet.md) \*setup, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*transfer\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*payload\_data) |
|  | Callback function signature for class specific requests. |
| typedef void(\* | [usb\_interface\_config](#ga3439af9464471b3acdc21f4359efb53a)) (struct [usb\_desc\_header](structusb__desc__header.md) \*head, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bInterfaceNumber) |
|  | Function for interface runtime configuration. |
| typedef void(\* | [usb\_transfer\_callback](#ga2e599eb20f647d9bb2369d76a7dc51db)) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, int tsize, void \*priv) |
|  | Callback function signature for transfer completion. |

| Functions | |
| --- | --- |
| int | [usb\_set\_config](#ga28783e727e35db1a651309a7f9f5444a) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*usb\_descriptor) |
|  | Configure USB controller. |
| int | [usb\_deconfig](#ga2d485c77055dd975f3170fbaea7f2bdf) (void) |
|  | Deconfigure USB controller. |
| int | [usb\_enable](#gad1fa5e491d93c2bd1fe7967c12148902) ([usb\_dc\_status\_callback](group____usb__device__controller__api.md#ga2ddb0b059b4e1e76473ed7f56d0cf2ee) status\_cb) |
|  | Enable the USB subsystem and associated hardware. |
| int | [usb\_disable](#ga65723c9469a12c87e5554169396f8e76) (void) |
|  | Disable the USB device. |
| int | [usb\_write](#ga6d4b568f2f3aac4f099c35393fb601b3) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*bytes\_ret) |
|  | Write data to the specified endpoint. |
| int | [usb\_read](#gab2c21738baa839b483654d1d5baf2981) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*ret\_bytes) |
|  | Read data from the specified endpoint. |
| int | [usb\_ep\_set\_stall](#gaaf206afaf32bde1b8d77d04bc6ec091f) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Set STALL condition on the specified endpoint. |
| int | [usb\_ep\_clear\_stall](#gae7bc410d0db8a6d2142992153bb1424d) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Clears STALL condition on the specified endpoint. |
| int | [usb\_ep\_read\_wait](#ga4c919f7e993f80150bdde2d7fab254ee) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_data\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*read\_bytes) |
|  | Read data from the specified endpoint. |
| int | [usb\_ep\_read\_continue](#gaab17b8c523ac211ff308c8dc774ba092) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Continue reading data from the endpoint. |
| void | [usb\_transfer\_ep\_callback](#ga3485c3d1c3fa7259de32fd57d303bc77) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, enum [usb\_dc\_ep\_cb\_status\_code](group____usb__device__controller__api.md#gaf7f083f61e1406e7d41513113dccd3bd)) |
|  | Transfer management endpoint callback. |
| int | [usb\_transfer](#ga27c3040dca474b5b45e6bea63a500cce) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dlen, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [usb\_transfer\_callback](#ga2e599eb20f647d9bb2369d76a7dc51db) cb, void \*priv) |
|  | Start a transfer. |
| int | [usb\_transfer\_sync](#ga1060e3a473a7f0bc71763a413e91ab56) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) dlen, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Start a transfer and block-wait for completion. |
| void | [usb\_cancel\_transfer](#gab399dc4a43a99c927ee7588a57c49211) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Cancel any ongoing transfer on the specified endpoint. |
| void | [usb\_cancel\_transfers](#ga758a63b22c48d2ae9d025adb92ed5925) (void) |
|  | Cancel all ongoing transfers. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [usb\_transfer\_is\_busy](#ga6292a473cffc1f8683da902c2a85d653) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Check that transfer is ongoing for the endpoint. |
| int | [usb\_wakeup\_request](#ga7d67c8d49b52fb33818d654ca647c1e5) (void) |
|  | Start the USB remote wakeup procedure. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [usb\_get\_remote\_wakeup\_status](#ga577018c415eec38ef5038cdb2f45ed2f) (void) |
|  | Get status of the USB remote wakeup feature. |
| void | [usb\_bos\_register\_cap](#ga1bf8ec88cf752e98234d9f8bb57f976a) (void \*hdr) |
|  | Register BOS capability descriptor. |

## Detailed Description

USB Device Core Layer API.

Since
:   1.5

Version
:   1.0.0

## Macro Definition Documentation

## [◆ ](#ga40975f1b023ea36118137e86e099e649)USB\_DEVICE\_BOS\_DESC\_DEFINE\_CAP

| #define USB\_DEVICE\_BOS\_DESC\_DEFINE\_CAP   static \_\_in\_section(usb, bos\_desc\_area, 1) \_\_aligned(1) \_\_used |
| --- |

`#include <[usb_device.h](usb__device_8h.md)>`

Helper macro to place the BOS compatibility descriptor in the right memory section.

## [◆ ](#ga81c618544f27e0dc0e556021b0418c40)USB\_TRANS\_NO\_ZLP

| #define USB\_TRANS\_NO\_ZLP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) /\*\* No zero-length packet flag \*/ |
| --- |

`#include <[usb_device.h](usb__device_8h.md)>`

## [◆ ](#gabb531b022f5d2d859227a7b35d593d80)USB\_TRANS\_READ

| #define USB\_TRANS\_READ   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) /\*\* Read transfer flag \*/ |
| --- |

`#include <[usb_device.h](usb__device_8h.md)>`

## [◆ ](#ga163ee39a47b0a3d9fe3697cc4f24e787)USB\_TRANS\_WRITE

| #define USB\_TRANS\_WRITE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) /\*\* Write transfer flag \*/ |
| --- |

`#include <[usb_device.h](usb__device_8h.md)>`

## Typedef Documentation

## [◆ ](#ga9a45db26a9be295640ed122533427725)usb\_ep\_callback

| typedef void(\* usb\_ep\_callback) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, enum [usb\_dc\_ep\_cb\_status\_code](group____usb__device__controller__api.md#gaf7f083f61e1406e7d41513113dccd3bd) cb\_status) |
| --- |

`#include <[usb_device.h](usb__device_8h.md)>`

Callback function signature for the USB Endpoint status.

## [◆ ](#ga3439af9464471b3acdc21f4359efb53a)usb\_interface\_config

| typedef void(\* usb\_interface\_config) (struct [usb\_desc\_header](structusb__desc__header.md) \*head, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bInterfaceNumber) |
| --- |

`#include <[usb_device.h](usb__device_8h.md)>`

Function for interface runtime configuration.

## [◆ ](#gaddacbff094a41c885c3041af72fa6804)usb\_request\_handler

| typedef int(\* usb\_request\_handler) (struct [usb\_setup\_packet](structusb__setup__packet.md) \*setup, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*transfer\_len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*payload\_data) |
| --- |

`#include <[usb_device.h](usb__device_8h.md)>`

Callback function signature for class specific requests.

Function which handles Class specific requests corresponding to an interface number specified in the device descriptor table. For host to device direction the 'len' and 'payload\_data' contain the length of the received data and the pointer to the received data respectively. For device to host class requests, 'len' and 'payload\_data' should be set by the callback function with the length and the address of the data to be transmitted buffer respectively.

## [◆ ](#ga2e599eb20f647d9bb2369d76a7dc51db)usb\_transfer\_callback

| typedef void(\* usb\_transfer\_callback) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, int tsize, void \*priv) |
| --- |

`#include <[usb_device.h](usb__device_8h.md)>`

Callback function signature for transfer completion.

## Function Documentation

## [◆ ](#ga1bf8ec88cf752e98234d9f8bb57f976a)usb\_bos\_register\_cap()

| void usb\_bos\_register\_cap | ( | void \* | *hdr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_device.h](usb__device_8h.md)>`

Register BOS capability descriptor.

This function should be used by the application to register BOS capability descriptors before the USB device stack is enabled.

Parameters
:   | [in] | hdr | Pointer to BOS capability descriptor |
    | --- | --- | --- |

## [◆ ](#gab399dc4a43a99c927ee7588a57c49211)usb\_cancel\_transfer()

| void usb\_cancel\_transfer | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_device.h](usb__device_8h.md)>`

Cancel any ongoing transfer on the specified endpoint.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |

## [◆ ](#ga758a63b22c48d2ae9d025adb92ed5925)usb\_cancel\_transfers()

| void usb\_cancel\_transfers | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_device.h](usb__device_8h.md)>`

Cancel all ongoing transfers.

## [◆ ](#ga2d485c77055dd975f3170fbaea7f2bdf)usb\_deconfig()

| int usb\_deconfig | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_device.h](usb__device_8h.md)>`

Deconfigure USB controller.

This function returns the USB device to it's initial state

Returns
:   0 on success, negative errno code on fail

## [◆ ](#ga65723c9469a12c87e5554169396f8e76)usb\_disable()

| int usb\_disable | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_device.h](usb__device_8h.md)>`

Disable the USB device.

Function to disable the USB device. Upon success, the specified USB interface is clock gated in hardware, it is no longer capable of generating interrupts.

Returns
:   0 on success, negative errno code on fail

## [◆ ](#gad1fa5e491d93c2bd1fe7967c12148902)usb\_enable()

| int usb\_enable | ( | [usb\_dc\_status\_callback](group____usb__device__controller__api.md#ga2ddb0b059b4e1e76473ed7f56d0cf2ee) | *status\_cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_device.h](usb__device_8h.md)>`

Enable the USB subsystem and associated hardware.

This function initializes the USB core subsystem and enables the corresponding hardware so that it can begin transmitting and receiving on the USB bus, as well as generating interrupts.

Class-specific initialization and registration must be performed by the user before invoking this, so that any data or events on the bus are processed correctly by the associated class handling code.

Parameters
:   | [in] | status\_cb | Callback registered by user to notify about USB device controller state. |
    | --- | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#gae7bc410d0db8a6d2142992153bb1424d)usb\_ep\_clear\_stall()

| int usb\_ep\_clear\_stall | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_device.h](usb__device_8h.md)>`

Clears STALL condition on the specified endpoint.

This function is called by USB device class handler code to clear stall condition on endpoint.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |

Returns
:   0 on success, negative errno code on fail

## [◆ ](#gaab17b8c523ac211ff308c8dc774ba092)usb\_ep\_read\_continue()

| int usb\_ep\_read\_continue | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_device.h](usb__device_8h.md)>`

Continue reading data from the endpoint.

Clear the endpoint NAK and enable the endpoint to accept more data from the host. Usually called after [usb\_ep\_read\_wait()](#ga4c919f7e993f80150bdde2d7fab254ee) when the consumer is fine to accept more data. Thus these calls together acts as flow control mechanism.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga4c919f7e993f80150bdde2d7fab254ee)usb\_ep\_read\_wait()

| int usb\_ep\_read\_wait | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *max\_data\_len*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *read\_bytes* ) |

`#include <[usb_device.h](usb__device_8h.md)>`

Read data from the specified endpoint.

This is similar to usb\_ep\_read, the difference being that, it doesn't clear the endpoint NAKs so that the consumer is not bogged down by further upcalls till he is done with the processing of the data. The caller should reactivate ep by invoking [usb\_ep\_read\_continue()](#gaab17b8c523ac211ff308c8dc774ba092) do so.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |
    | [in] | data | pointer to data buffer to write to |
    | [in] | max\_data\_len | max length of data to read |
    | [out] | read\_bytes | Number of bytes read. If data is NULL and max\_data\_len is 0 the number of bytes available for read should be returned. |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#gaaf206afaf32bde1b8d77d04bc6ec091f)usb\_ep\_set\_stall()

| int usb\_ep\_set\_stall | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_device.h](usb__device_8h.md)>`

Set STALL condition on the specified endpoint.

This function is called by USB device class handler code to set stall condition on endpoint.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |

Returns
:   0 on success, negative errno code on fail

## [◆ ](#ga577018c415eec38ef5038cdb2f45ed2f)usb\_get\_remote\_wakeup\_status()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) usb\_get\_remote\_wakeup\_status | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_device.h](usb__device_8h.md)>`

Get status of the USB remote wakeup feature.

Returns
:   true if remote wakeup has been enabled by the host, false otherwise.

## [◆ ](#gab2c21738baa839b483654d1d5baf2981)usb\_read()

| int usb\_read | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *max\_data\_len*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *ret\_bytes* ) |

`#include <[usb_device.h](usb__device_8h.md)>`

Read data from the specified endpoint.

This function is called by the Endpoint handler function, after an OUT interrupt has been received for that EP. The application must only call this function through the supplied [usb\_ep\_callback](#ga9a45db26a9be295640ed122533427725) function.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |
    | [in] | data | Pointer to data buffer to write to |
    | [in] | max\_data\_len | Max length of data to read |
    | [out] | ret\_bytes | Number of bytes read. If data is NULL and max\_data\_len is 0 the number of bytes available for read is returned. |

Returns
:   0 on success, negative errno code on fail

## [◆ ](#ga28783e727e35db1a651309a7f9f5444a)usb\_set\_config()

| int usb\_set\_config | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *usb\_descriptor* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_device.h](usb__device_8h.md)>`

Configure USB controller.

Function to configure USB controller. Configuration parameters must be valid or an error is returned

Parameters
:   | [in] | usb\_descriptor | USB descriptor table |
    | --- | --- | --- |

Returns
:   0 on success, negative errno code on fail

## [◆ ](#ga27c3040dca474b5b45e6bea63a500cce)usb\_transfer()

| int usb\_transfer | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *dlen*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *flags*, |
|  |  | [usb\_transfer\_callback](#ga2e599eb20f647d9bb2369d76a7dc51db) | *cb*, |
|  |  | void \* | *priv* ) |

`#include <[usb_device.h](usb__device_8h.md)>`

Start a transfer.

Start a usb transfer to/from the data buffer. This function is asynchronous and can be executed in IRQ context. The provided callback will be called on transfer completion (or error) in thread context.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |
    | [in] | data | Pointer to data buffer to write-to/read-from |
    | [in] | dlen | Size of data buffer |
    | [in] | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Transfer flags (USB\_TRANS\_READ, USB\_TRANS\_WRITE...) |
    | [in] | cb | Function called on transfer completion/failure |
    | [in] | priv | Data passed back to the transfer completion callback |

Returns
:   0 on success, negative errno code on fail.

## [◆ ](#ga3485c3d1c3fa7259de32fd57d303bc77)usb\_transfer\_ep\_callback()

| void usb\_transfer\_ep\_callback | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep*, |
| --- | --- | --- | --- |
|  |  | enum | *usb\_dc\_ep\_cb\_status\_code* ) |

`#include <[usb_device.h](usb__device_8h.md)>`

Transfer management endpoint callback.

If a USB class driver wants to use high-level transfer functions, driver needs to register this callback as usb endpoint callback.

## [◆ ](#ga6292a473cffc1f8683da902c2a85d653)usb\_transfer\_is\_busy()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) usb\_transfer\_is\_busy | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_device.h](usb__device_8h.md)>`

Check that transfer is ongoing for the endpoint.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |

Returns
:   true if transfer is ongoing, false otherwise.

## [◆ ](#ga1060e3a473a7f0bc71763a413e91ab56)usb\_transfer\_sync()

| int usb\_transfer\_sync | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *dlen*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *flags* ) |

`#include <[usb_device.h](usb__device_8h.md)>`

Start a transfer and block-wait for completion.

Synchronous version of usb\_transfer, wait for transfer completion before returning. A return value of zero can also mean that transfer was cancelled or that the endpoint is not ready. This is due to the design of transfers and usb\_dc API.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |
    | [in] | data | Pointer to data buffer to write-to/read-from |
    | [in] | dlen | Size of data buffer |
    | [in] | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Transfer flags |

Returns
:   number of bytes transferred on success, negative errno code on fail.

## [◆ ](#ga7d67c8d49b52fb33818d654ca647c1e5)usb\_wakeup\_request()

| int usb\_wakeup\_request | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[usb_device.h](usb__device_8h.md)>`

Start the USB remote wakeup procedure.

Function to request a remote wakeup. This feature must be enabled in configuration, otherwise it will always return -ENOTSUP error.

Returns
:   0 on success, negative errno code on fail, i.e. when the bus is already active.

## [◆ ](#ga6d4b568f2f3aac4f099c35393fb601b3)usb\_write()

| int usb\_write | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *ep*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data\_len*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *bytes\_ret* ) |

`#include <[usb_device.h](usb__device_8h.md)>`

Write data to the specified endpoint.

Function to write data to the specified endpoint. The supplied [usb\_ep\_callback](#ga9a45db26a9be295640ed122533427725) will be called when transmission is done.

Parameters
:   | [in] | ep | Endpoint address corresponding to the one listed in the device configuration table |
    | --- | --- | --- |
    | [in] | data | Pointer to data to write |
    | [in] | data\_len | Length of data requested to write. This may be zero for a zero length status packet. |
    | [out] | bytes\_ret | Bytes written to the EP FIFO. This value may be NULL if the application expects all bytes to be written |

Returns
:   0 on success, negative errno code on fail

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
