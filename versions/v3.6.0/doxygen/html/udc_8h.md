---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/udc_8h.html
original_path: doxygen/html/udc_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

udc.h File Reference

New USB device controller (UDC) driver API.
[More...](#details)

`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/net/buf.h](net_2buf_8h_source.md)>`  
`#include <[zephyr/sys/atomic.h](atomic_8h_source.md)>`  
`#include <[zephyr/usb/usb_ch9.h](usb__ch9_8h_source.md)>`

[Go to the source code of this file.](udc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [udc\_device\_caps](structudc__device__caps.md) |
|  | USB device controller capabilities. [More...](structudc__device__caps.md#details) |
| struct | [udc\_ep\_caps](structudc__ep__caps.md) |
|  | USB device controller endpoint capabilities. [More...](structudc__ep__caps.md#details) |
| struct | [udc\_ep\_stat](structudc__ep__stat.md) |
|  | USB device controller endpoint status. [More...](structudc__ep__stat.md#details) |
| struct | [udc\_ep\_config](structudc__ep__config.md) |
|  | USB device controller endpoint configuration. [More...](structudc__ep__config.md#details) |
| struct | [udc\_event](structudc__event.md) |
|  | USB device controller event. [More...](structudc__event.md#details) |
| struct | [udc\_buf\_info](structudc__buf__info.md) |
|  | UDC endpoint buffer info. [More...](structudc__buf__info.md#details) |
| struct | [udc\_api](structudc__api.md) |
|  | UDC driver API This is the mandatory API any USB device controller driver needs to expose with exception of: [device\_speed()](structudc__api.md#adf2b8f76158d7bd2d3918628c8a9fc22), [test\_mode()](structudc__api.md#ab06839ded48cbc671b2b915fe0010959) are only required for HS controllers. [More...](structudc__api.md#details) |
| struct | [udc\_data](structudc__data.md) |
|  | Common UDC driver data structure. [More...](structudc__data.md#details) |

| Macros | |
| --- | --- |
| #define | [UDC\_STATUS\_INITIALIZED](#a8c96946734085924e2afc591ac502551)   0 |
|  | Controller is initialized by [udc\_init()](group__udc__api.md#gab365e4326d53ccba92fd167e3710ed7c "Initialize USB device controller.") and can generate the VBUS events, if capable, but shall not be recognizable by host. |
| #define | [UDC\_STATUS\_ENABLED](#ad10596af54465c3cb10cc59ae9a507d2)   1 |
|  | Controller is enabled and all API functions are available, controller is recognizable by host. |
| #define | [UDC\_STATUS\_SUSPENDED](#ac3a36aa8cb3aab95d7931cb602631c36)   2 |
|  | Controller is suspended by the host. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [udc\_event\_cb\_t](#aa3ff247fd5234f65d91f84ebc38e384a)) (const struct [device](structdevice.md) \*dev, const struct [udc\_event](structudc__event.md) \*const event) |
|  | Callback to submit UDC event to higher layer. |

| Enumerations | |
| --- | --- |
| enum | [udc\_mps0](#ac254f8a970f890d14e35c43474c915fd) { [UDC\_MPS0\_8](#ac254f8a970f890d14e35c43474c915fdad961e13d52b708c9e6b8d951affd31bb) , [UDC\_MPS0\_16](#ac254f8a970f890d14e35c43474c915fda4a8ba94e9dced296d0e269390931e85a) , [UDC\_MPS0\_32](#ac254f8a970f890d14e35c43474c915fda1930322c1c7b053f3b9da2e319ed11e7) , [UDC\_MPS0\_64](#ac254f8a970f890d14e35c43474c915fdab481546bd71839266d4d881d6610633a) } |
|  | Maximum packet size of control endpoint supported by the controller. [More...](#ac254f8a970f890d14e35c43474c915fd) |
| enum | [udc\_bus\_speed](#a32d61ab6dbb734009102b5239a834d1b) { [UDC\_BUS\_UNKNOWN](#a32d61ab6dbb734009102b5239a834d1ba872aa49861a213ad970012f43db7d35d) , [UDC\_BUS\_SPEED\_FS](#a32d61ab6dbb734009102b5239a834d1ba8177d4c8e8cb0456f9c2a553c76dc0d5) , [UDC\_BUS\_SPEED\_HS](#a32d61ab6dbb734009102b5239a834d1ba9fc26a4b4ba8db446731274b67182599) , [UDC\_BUS\_SPEED\_SS](#a32d61ab6dbb734009102b5239a834d1ba71b0e0a870859cf1f0c11380833f790a) } |
|  | USB device actual speed. [More...](#a32d61ab6dbb734009102b5239a834d1b) |
| enum | [udc\_event\_type](#a03749f5acb64ff8cfddc3c0b6b81a040) {     [UDC\_EVT\_VBUS\_READY](#a03749f5acb64ff8cfddc3c0b6b81a040a010cfc9f43a6faf68323201ae02fa00d) , [UDC\_EVT\_VBUS\_REMOVED](#a03749f5acb64ff8cfddc3c0b6b81a040a4bdf374daa2aeb4f7b6b6c5fe2a46432) , [UDC\_EVT\_RESUME](#a03749f5acb64ff8cfddc3c0b6b81a040a0e0da320fe601eb1de24c142fc60f332) , [UDC\_EVT\_SUSPEND](#a03749f5acb64ff8cfddc3c0b6b81a040a120dc649618040f41da7542bf639159f) ,     [UDC\_EVT\_RESET](#a03749f5acb64ff8cfddc3c0b6b81a040aa174f33c3802cec8d6c37606bc5ba9bb) , [UDC\_EVT\_SOF](#a03749f5acb64ff8cfddc3c0b6b81a040af20153f2fde8ea2bb1a985f2e17a2f78) , [UDC\_EVT\_EP\_REQUEST](#a03749f5acb64ff8cfddc3c0b6b81a040a52bb5ea941db9a025ccb73de3fc6d55b) , [UDC\_EVT\_ERROR](#a03749f5acb64ff8cfddc3c0b6b81a040a8ff69c0bc684eb113f1d4e0ec02dd70d)   } |
|  | USB device controller event types. [More...](#a03749f5acb64ff8cfddc3c0b6b81a040) |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [udc\_is\_initialized](group__udc__api.md#ga40e50cf79b40d3792513e8fea3347f59) (const struct [device](structdevice.md) \*dev) |
|  | Checks whether the controller is initialized. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [udc\_is\_enabled](group__udc__api.md#ga2c09f2a1e89c91527a8492019089d13f) (const struct [device](structdevice.md) \*dev) |
|  | Checks whether the controller is enabled. |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [udc\_is\_suspended](group__udc__api.md#ga88786eda763fce5c2a51521650ccc9f4) (const struct [device](structdevice.md) \*dev) |
|  | Checks whether the controller is suspended. |
| int | [udc\_init](group__udc__api.md#gab365e4326d53ccba92fd167e3710ed7c) (const struct [device](structdevice.md) \*dev, [udc\_event\_cb\_t](#aa3ff247fd5234f65d91f84ebc38e384a) event\_cb) |
|  | Initialize USB device controller. |
| int | [udc\_enable](group__udc__api.md#gafbb0dec089f83fd674bd19670a882c65) (const struct [device](structdevice.md) \*dev) |
|  | Enable USB device controller. |
| int | [udc\_disable](group__udc__api.md#gaa7c2eaa52bdbe1d763b2961124570e8a) (const struct [device](structdevice.md) \*dev) |
|  | Disable USB device controller. |
| int | [udc\_shutdown](group__udc__api.md#ga59a92eb60575ca80d205cc29b4fb4f21) (const struct [device](structdevice.md) \*dev) |
|  | Poweroff USB device controller. |
| static struct [udc\_device\_caps](structudc__device__caps.md) | [udc\_caps](group__udc__api.md#ga3ee738bad8e1ee3928d32f57f82bef70) (const struct [device](structdevice.md) \*dev) |
|  | Get USB device controller capabilities. |
| enum [udc\_bus\_speed](#a32d61ab6dbb734009102b5239a834d1b) | [udc\_device\_speed](group__udc__api.md#gab936f04015b0fee584756bcdf40d2f50) (const struct [device](structdevice.md) \*dev) |
|  | Get actual USB device speed. |
| static int | [udc\_set\_address](group__udc__api.md#ga6feb32a2263307bdde9acc63d3c2ebb1) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
|  | Set USB device address. |
| static int | [udc\_test\_mode](group__udc__api.md#ga7f575b548833cc1e5109e0d919630b3f) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) dryrun) |
|  | Enable Test Mode. |
| static int | [udc\_host\_wakeup](group__udc__api.md#ga075edc81fb3e39c2b377fc56c8c0915c) (const struct [device](structdevice.md) \*dev) |
|  | Initiate host wakeup procedure. |
| int | [udc\_ep\_try\_config](group__udc__api.md#ga81307ae4ab17ccd86be64bdf1653df0e) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attributes, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const mps, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) interval) |
|  | Try an endpoint configuration. |
| int | [udc\_ep\_enable](group__udc__api.md#gacc4b5c127532c994406df30bacab5684) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attributes, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mps, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) interval) |
|  | Configure and enable endpoint. |
| int | [udc\_ep\_disable](group__udc__api.md#ga52da2366ac5da1a695caa8826b342cbc) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Disable endpoint. |
| int | [udc\_ep\_set\_halt](group__udc__api.md#ga19488ec4c93d81592bb5ffccfc1eadc4) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Halt endpoint. |
| int | [udc\_ep\_clear\_halt](group__udc__api.md#gadec9c8af89b28984028fd8e0b1a8c776) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Clear endpoint halt. |
| int | [udc\_ep\_enqueue](group__udc__api.md#gacb2dc96353f1cffcc3d5e9710133fc0d) (const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Queue USB device controller request. |
| int | [udc\_ep\_dequeue](group__udc__api.md#ga6e6fb62fb8ebceca7e8e6b590c32efc2) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep) |
|  | Remove all USB device controller requests from endpoint queue. |
| struct [net\_buf](structnet__buf.md) \* | [udc\_ep\_buf\_alloc](group__udc__api.md#gad3fb1d64b6e0cf051627011ce673bb1e) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ep, const [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Allocate UDC request buffer. |
| int | [udc\_ep\_buf\_free](group__udc__api.md#gaedd615defad234b001e74448f89488e1) (const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Free UDC request buffer. |
| static void | [udc\_ep\_buf\_set\_zlp](group__udc__api.md#ga50f6bde28b6a5fcab6b685107570e081) (struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Set ZLP flag in requests metadata. |
| static struct [udc\_buf\_info](structudc__buf__info.md) \* | [udc\_get\_buf\_info](group__udc__api.md#ga073a51222ac639d3c70af7b57970b42a) (const struct [net\_buf](structnet__buf.md) \*const buf) |
|  | Get requests metadata. |

## Detailed Description

New USB device controller (UDC) driver API.

## Macro Definition Documentation

## [◆ ](#ad10596af54465c3cb10cc59ae9a507d2)UDC\_STATUS\_ENABLED

| #define UDC\_STATUS\_ENABLED   1 |
| --- |

Controller is enabled and all API functions are available, controller is recognizable by host.

## [◆ ](#a8c96946734085924e2afc591ac502551)UDC\_STATUS\_INITIALIZED

| #define UDC\_STATUS\_INITIALIZED   0 |
| --- |

Controller is initialized by [udc\_init()](group__udc__api.md#gab365e4326d53ccba92fd167e3710ed7c "Initialize USB device controller.") and can generate the VBUS events, if capable, but shall not be recognizable by host.

## [◆ ](#ac3a36aa8cb3aab95d7931cb602631c36)UDC\_STATUS\_SUSPENDED

| #define UDC\_STATUS\_SUSPENDED   2 |
| --- |

Controller is suspended by the host.

## Typedef Documentation

## [◆ ](#aa3ff247fd5234f65d91f84ebc38e384a)udc\_event\_cb\_t

| typedef int(\* udc\_event\_cb\_t) (const struct [device](structdevice.md) \*dev, const struct [udc\_event](structudc__event.md) \*const event) |
| --- |

Callback to submit UDC event to higher layer.

At the higher level, the event is to be inserted into a message queue. (TBD) Maybe it is better to provide a pointer to [k\_msgq](structk__msgq.md "Message Queue Structure.") passed during initialization.

Parameters
:   | [in] | dev | Pointer to device struct of the driver instance |
    | --- | --- | --- |
    | [in] | event | Point to event structure |

Returns
:   0 on success, all other values should be treated as error.

## Enumeration Type Documentation

## [◆ ](#a32d61ab6dbb734009102b5239a834d1b)udc\_bus\_speed

| enum [udc\_bus\_speed](#a32d61ab6dbb734009102b5239a834d1b) |
| --- |

USB device actual speed.

| Enumerator | |
| --- | --- |
| UDC\_BUS\_UNKNOWN | Device is probably not connected. |
| UDC\_BUS\_SPEED\_FS | Device is connected to a full speed bus. |
| UDC\_BUS\_SPEED\_HS | Device is connected to a high speed bus. |
| UDC\_BUS\_SPEED\_SS | Device is connected to a super speed bus. |

## [◆ ](#a03749f5acb64ff8cfddc3c0b6b81a040)udc\_event\_type

| enum [udc\_event\_type](#a03749f5acb64ff8cfddc3c0b6b81a040) |
| --- |

USB device controller event types.

| Enumerator | |
| --- | --- |
| UDC\_EVT\_VBUS\_READY | VBUS ready event.  Signals that VBUS is in stable condition. |
| UDC\_EVT\_VBUS\_REMOVED | VBUS removed event.  Signals that VBUS is below the valid range. |
| UDC\_EVT\_RESUME | Device resume event. |
| UDC\_EVT\_SUSPEND | Device suspended event. |
| UDC\_EVT\_RESET | Port reset detected. |
| UDC\_EVT\_SOF | Start of Frame event. |
| UDC\_EVT\_EP\_REQUEST | Endpoint request result event. |
| UDC\_EVT\_ERROR | Non-correctable error event, requires attention from higher levels or application. |

## [◆ ](#ac254f8a970f890d14e35c43474c915fd)udc\_mps0

| enum [udc\_mps0](#ac254f8a970f890d14e35c43474c915fd) |
| --- |

Maximum packet size of control endpoint supported by the controller.

| Enumerator | |
| --- | --- |
| UDC\_MPS0\_8 |  |
| UDC\_MPS0\_16 |  |
| UDC\_MPS0\_32 |  |
| UDC\_MPS0\_64 |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [usb](dir_8780870c85d3e97051f07cf376f058af.md)
- [udc.h](udc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
