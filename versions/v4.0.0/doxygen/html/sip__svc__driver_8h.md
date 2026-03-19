---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sip__svc__driver_8h.html
original_path: doxygen/html/sip__svc__driver_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sip\_svc\_driver.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/arch/arm64/arm-smccc.h](arm-smccc_8h_source.md)>`  
`#include <[zephyr/drivers/sip_svc/sip_svc_proto.h](sip__svc__proto_8h_source.md)>`  
`#include <[zephyr/sip_svc/sip_svc_controller.h](sip__svc__controller_8h_source.md)>`  
`#include <zephyr/syscalls/sip_svc_driver.h>`

[Go to the source code of this file.](sip__svc__driver_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [svc\_driver\_api](structsvc__driver__api.md) |
|  | API structure for sip\_svc driver. [More...](structsvc__driver__api.md#details) |

| Macros | |
| --- | --- |
| #define | [DEV\_API](#aeae219b400322b0926dd7251dc122bbd)(dev) |
| #define | [SVC\_CONDUIT\_NAME\_LENGTH](#a780bbf4be68a9ac867243823c0eb790e)   (4) |
|  | Length of SVC conduit name. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [sip\_supervisory\_call\_t](#a15714e3852882693de6c9c7f2229bcd1)) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long function\_id, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg0, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg1, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg2, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg3, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg4, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg5, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg6, struct [arm\_smccc\_res](structarm__smccc__res.md) \*res) |
|  | Callback API for executing the supervisory call See *[sip\_supervisory\_call()](#a881e3794f9e29e12c925cb5dbd443420)* for argument description. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [sip\_svc\_plat\_func\_id\_valid\_t](#ac5921c9cdc00604651696e1580f30797)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) command, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) func\_id) |
|  | Callback API for validating function id for the supervisory call. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [sip\_svc\_plat\_format\_trans\_id\_t](#a3cf78c760c6eae2091e92329e54b1a31)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) client\_idx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trans\_idx) |
|  | Callback API for generating the transaction id from client id. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [sip\_svc\_plat\_get\_trans\_idx\_t](#a35145ddf422e8782b4ec37270b04d98c)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trans\_id) |
|  | Callback API for retrieving client transaction id from transaction id See *[sip\_svc\_plat\_get\_trans\_idx()](#ad0e52f49e7db8cf51ff8cf95e1283994)* for argument description. |
| typedef void(\* | [sip\_svc\_plat\_update\_trans\_id\_t](#a9d61db0484e2aacce4515290ffb4450c)) (const struct [device](structdevice.md) \*dev, struct [sip\_svc\_request](structsip__svc__request.md) \*request, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trans\_id) |
|  | Callback API for updating transaction id for request packet for lower layer See *[sip\_svc\_plat\_update\_trans\_id()](#a095123f7aec80a3e51d75ef248990124)* for argument description. |
| typedef void(\* | [sip\_svc\_plat\_free\_async\_memory\_t](#ab32e31bdba00ff66303fab1b04cd0ebe)) (const struct [device](structdevice.md) \*dev, struct [sip\_svc\_request](structsip__svc__request.md) \*request) |
|  | Callback API for freeing command buffer in ASYNC packets See *[sip\_svc\_plat\_free\_async\_memory()](#aa4e44eb2af080207821a60f8b3442886)* for argument description. |
| typedef int(\* | [sip\_svc\_plat\_async\_res\_req\_t](#aa49a26b4b503e58d23fb5087ed701a0a)) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a0, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a1, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a2, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a3, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a4, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a5, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a6, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a7, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Callback API to construct Polling packet for ASYNC transaction. |
| typedef int(\* | [sip\_svc\_plat\_async\_res\_res\_t](#a54293f84f9bc86661f8a4bf717ad4754)) (const struct [device](structdevice.md) \*dev, struct [arm\_smccc\_res](structarm__smccc__res.md) \*res, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*trans\_id) |
|  | Callback API to check the response of polling request See *[sip\_svc\_plat\_async\_res\_res()](#a0a0577249c2a9f470cd6ec0a60b455c8)* for argument description. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* | [sip\_svc\_plat\_get\_error\_code\_t](#a926eeecea766b2131c03c57111a186f8)) (const struct [device](structdevice.md) \*dev, struct [arm\_smccc\_res](structarm__smccc__res.md) \*res) |
|  | Callback API for retrieving error code from a supervisory call response. |

| Functions | |
| --- | --- |
| void | [sip\_supervisory\_call](#a881e3794f9e29e12c925cb5dbd443420) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long function\_id, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg0, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg1, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg2, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg3, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg4, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg5, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg6, struct [arm\_smccc\_res](structarm__smccc__res.md) \*res) |
|  | supervisory call function which will execute the smc/hvc call |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [sip\_svc\_plat\_func\_id\_valid](#a8df36a218cce4c0904c147d498c1322d) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) command, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) func\_id) |
|  | Validate the function id for the supervisory call. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sip\_svc\_plat\_format\_trans\_id](#ae52dee0bbba688a73a9726dd4aa482d2) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) client\_idx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trans\_idx) |
|  | Formats and generates the transaction id from client id. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sip\_svc\_plat\_get\_trans\_idx](#ad0e52f49e7db8cf51ff8cf95e1283994) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trans\_id) |
|  | Retrieve client transaction id from packet transaction id. |
| void | [sip\_svc\_plat\_update\_trans\_id](#a095123f7aec80a3e51d75ef248990124) (const struct [device](structdevice.md) \*dev, struct [sip\_svc\_request](structsip__svc__request.md) \*request, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trans\_id) |
|  | Update transaction id for [sip\_svc\_request](structsip__svc__request.md "SiP Service communication protocol request format.") for lower layer. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sip\_svc\_plat\_get\_error\_code](#a3510743d8cf114376b740f3d297c583f) (const struct [device](structdevice.md) \*dev, struct [arm\_smccc\_res](structarm__smccc__res.md) \*res) |
|  | Retrieve the error code from [arm\_smccc\_res](structarm__smccc__res.md) response. |
| int | [sip\_svc\_plat\_async\_res\_req](#abb9ff6ec7dea6fc4e104db8cc5e7168b) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a0, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a1, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a2, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a3, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a4, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a5, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a6, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a7, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Set arguments for polling supervisory call. |
| int | [sip\_svc\_plat\_async\_res\_res](#a0a0577249c2a9f470cd6ec0a60b455c8) (const struct [device](structdevice.md) \*dev, struct [arm\_smccc\_res](structarm__smccc__res.md) \*res, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*trans\_id) |
|  | Check the response of polling supervisory call and retrieve the response size and transaction id. |
| void | [sip\_svc\_plat\_free\_async\_memory](#aa4e44eb2af080207821a60f8b3442886) (const struct [device](structdevice.md) \*dev, struct [sip\_svc\_request](structsip__svc__request.md) \*request) |
|  | Free the command buffer used for ASYNC packet after sending it to lower layers. |

## Macro Definition Documentation

## [◆ ](#aeae219b400322b0926dd7251dc122bbd)DEV\_API

| #define DEV\_API | ( |  | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((struct [svc\_driver\_api](structsvc__driver__api.md) \*)(dev)->api)

[svc\_driver\_api](structsvc__driver__api.md)

API structure for sip\_svc driver.

**Definition** sip\_svc\_driver.h:94

## [◆ ](#a780bbf4be68a9ac867243823c0eb790e)SVC\_CONDUIT\_NAME\_LENGTH

| #define SVC\_CONDUIT\_NAME\_LENGTH   (4) |
| --- |

Length of SVC conduit name.

## Typedef Documentation

## [◆ ](#a15714e3852882693de6c9c7f2229bcd1)sip\_supervisory\_call\_t

| typedef void(\* sip\_supervisory\_call\_t) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long function\_id, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg0, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg1, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg2, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg3, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg4, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg5, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long arg6, struct [arm\_smccc\_res](structarm__smccc__res.md) \*res) |
| --- |

Callback API for executing the supervisory call See *[sip\_supervisory\_call()](#a881e3794f9e29e12c925cb5dbd443420)* for argument description.

## [◆ ](#aa49a26b4b503e58d23fb5087ed701a0a)sip\_svc\_plat\_async\_res\_req\_t

| typedef int(\* sip\_svc\_plat\_async\_res\_req\_t) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a0, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a1, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a2, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a3, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a4, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a5, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a6, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \*a7, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
| --- |

Callback API to construct Polling packet for ASYNC transaction.

See *[sip\_svc\_plat\_async\_res\_req()](#abb9ff6ec7dea6fc4e104db8cc5e7168b)* for argument description

## [◆ ](#a54293f84f9bc86661f8a4bf717ad4754)sip\_svc\_plat\_async\_res\_res\_t

| typedef int(\* sip\_svc\_plat\_async\_res\_res\_t) (const struct [device](structdevice.md) \*dev, struct [arm\_smccc\_res](structarm__smccc__res.md) \*res, char \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*trans\_id) |
| --- |

Callback API to check the response of polling request See *[sip\_svc\_plat\_async\_res\_res()](#a0a0577249c2a9f470cd6ec0a60b455c8)* for argument description.

## [◆ ](#a3cf78c760c6eae2091e92329e54b1a31)sip\_svc\_plat\_format\_trans\_id\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* sip\_svc\_plat\_format\_trans\_id\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) client\_idx, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trans\_idx) |
| --- |

Callback API for generating the transaction id from client id.

See *[sip\_svc\_plat\_format\_trans\_id()](#ae52dee0bbba688a73a9726dd4aa482d2)* for argument description

## [◆ ](#ab32e31bdba00ff66303fab1b04cd0ebe)sip\_svc\_plat\_free\_async\_memory\_t

| typedef void(\* sip\_svc\_plat\_free\_async\_memory\_t) (const struct [device](structdevice.md) \*dev, struct [sip\_svc\_request](structsip__svc__request.md) \*request) |
| --- |

Callback API for freeing command buffer in ASYNC packets See *[sip\_svc\_plat\_free\_async\_memory()](#aa4e44eb2af080207821a60f8b3442886)* for argument description.

## [◆ ](#ac5921c9cdc00604651696e1580f30797)sip\_svc\_plat\_func\_id\_valid\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* sip\_svc\_plat\_func\_id\_valid\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) command, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) func\_id) |
| --- |

Callback API for validating function id for the supervisory call.

See *[sip\_svc\_plat\_func\_id\_valid()](#a8df36a218cce4c0904c147d498c1322d)* for argument description

## [◆ ](#a926eeecea766b2131c03c57111a186f8)sip\_svc\_plat\_get\_error\_code\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* sip\_svc\_plat\_get\_error\_code\_t) (const struct [device](structdevice.md) \*dev, struct [arm\_smccc\_res](structarm__smccc__res.md) \*res) |
| --- |

Callback API for retrieving error code from a supervisory call response.

See *[sip\_svc\_plat\_get\_error\_code()](#a3510743d8cf114376b740f3d297c583f)* for argument description.

## [◆ ](#a35145ddf422e8782b4ec37270b04d98c)sip\_svc\_plat\_get\_trans\_idx\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)(\* sip\_svc\_plat\_get\_trans\_idx\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trans\_id) |
| --- |

Callback API for retrieving client transaction id from transaction id See *[sip\_svc\_plat\_get\_trans\_idx()](#ad0e52f49e7db8cf51ff8cf95e1283994)* for argument description.

## [◆ ](#a9d61db0484e2aacce4515290ffb4450c)sip\_svc\_plat\_update\_trans\_id\_t

| typedef void(\* sip\_svc\_plat\_update\_trans\_id\_t) (const struct [device](structdevice.md) \*dev, struct [sip\_svc\_request](structsip__svc__request.md) \*request, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) trans\_id) |
| --- |

Callback API for updating transaction id for request packet for lower layer See *[sip\_svc\_plat\_update\_trans\_id()](#a095123f7aec80a3e51d75ef248990124)* for argument description.

## Function Documentation

## [◆ ](#a881e3794f9e29e12c925cb5dbd443420)sip\_supervisory\_call()

| void sip\_supervisory\_call | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *function\_id*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *arg0*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *arg1*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *arg2*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *arg3*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *arg4*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *arg5*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long | *arg6*, |
|  |  | struct [arm\_smccc\_res](structarm__smccc__res.md) \* | *res* ) |

supervisory call function which will execute the smc/hvc call

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | function\_id | Function identifier for the supervisory call. |
    | arg0 | Argument 0 for supervisory call. |
    | arg1 | Argument 1 for supervisory call. |
    | arg2 | Argument 2 for supervisory call. |
    | arg3 | Argument 3 for supervisory call. |
    | arg4 | Argument 4 for supervisory call. |
    | arg5 | Argument 5 for supervisory call. |
    | arg6 | Argument 6 for supervisory call. |
    | res | Pointer to response buffer for supervisory call. |

## [◆ ](#abb9ff6ec7dea6fc4e104db8cc5e7168b)sip\_svc\_plat\_async\_res\_req()

| int sip\_svc\_plat\_async\_res\_req | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \* | *a0*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \* | *a1*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \* | *a2*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \* | *a3*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \* | *a4*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \* | *a5*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \* | *a6*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) long \* | *a7*, |
|  |  | char \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size* ) |

Set arguments for polling supervisory call.

For ASYNC polling of response.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | a0 | Argument 0 for supervisory call. |
    | a1 | Argument 1 for supervisory call. |
    | a2 | Argument 2 for supervisory call. |
    | a3 | Argument 3 for supervisory call. |
    | a4 | Argument 4 for supervisory call. |
    | a5 | Argument 5 for supervisory call. |
    | a6 | Argument 6 for supervisory call. |
    | a7 | Argument 7 for supervisory call. |
    | buf | Pointer for response buffer. |
    | size | Size of response buffer. |

Return values
:   | 0 | on success |
    | --- | --- |

## [◆ ](#a0a0577249c2a9f470cd6ec0a60b455c8)sip\_svc\_plat\_async\_res\_res()

| int sip\_svc\_plat\_async\_res\_res | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [arm\_smccc\_res](structarm__smccc__res.md) \* | *res*, |
|  |  | char \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *size*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *trans\_id* ) |

Check the response of polling supervisory call and retrieve the response size and transaction id.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | res | Pointer to struct [arm\_smccc\_res](structarm__smccc__res.md) response. |
    | buf | Pointer to response buffer. |
    | size | Size of response in response buffer |
    | trans\_id | Transaction id of the response. |

Return values
:   | 0 | on getting a valid polling response from supervisory call. |
    | --- | --- |
    | -EINPROGRESS | on no valid polling response from supervisory call. |

## [◆ ](#ae52dee0bbba688a73a9726dd4aa482d2)sip\_svc\_plat\_format\_trans\_id()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sip\_svc\_plat\_format\_trans\_id | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *client\_idx*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *trans\_idx* ) |

Formats and generates the transaction id from client id.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | client\_idx | client index. |
    | trans\_idx | transaction index. |

Return values
:   | transaction | id, which is used for tracking each transaction. |
    | --- | --- |

## [◆ ](#aa4e44eb2af080207821a60f8b3442886)sip\_svc\_plat\_free\_async\_memory()

| void sip\_svc\_plat\_free\_async\_memory | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [sip\_svc\_request](structsip__svc__request.md) \* | *request* ) |

Free the command buffer used for ASYNC packet after sending it to lower layers.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | request | Pointer to [sip\_svc\_request](structsip__svc__request.md "SiP Service communication protocol request format.") packet. |

## [◆ ](#a8df36a218cce4c0904c147d498c1322d)sip\_svc\_plat\_func\_id\_valid()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sip\_svc\_plat\_func\_id\_valid | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *command*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *func\_id* ) |

Validate the function id for the supervisory call.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | command | Command which specify if the call is SYNC or ASYNC. |
    | func\_id | Function identifier |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if command and function identifiers are valid. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if command and function identifiers are invalid. |

## [◆ ](#a3510743d8cf114376b740f3d297c583f)sip\_svc\_plat\_get\_error\_code()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sip\_svc\_plat\_get\_error\_code | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [arm\_smccc\_res](structarm__smccc__res.md) \* | *res* ) |

Retrieve the error code from [arm\_smccc\_res](structarm__smccc__res.md) response.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | res | Pointer to struct [arm\_smccc\_res](structarm__smccc__res.md) response. |

Return values
:   | 0 | on success. |
    | --- | --- |
    | [SIP\_SVC\_ID\_INVALID](sip__svc__proto_8h.md#ad1cb9509a40e51809b13f1fccf0f35ba "Invalid id value.") | on failure |

## [◆ ](#ad0e52f49e7db8cf51ff8cf95e1283994)sip\_svc\_plat\_get\_trans\_idx()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sip\_svc\_plat\_get\_trans\_idx | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *trans\_id* ) |

Retrieve client transaction id from packet transaction id.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | trans\_id | transaction identifier if for a transaction. |

Return values
:   | client | transaction id form Transaction id. |
    | --- | --- |

## [◆ ](#a095123f7aec80a3e51d75ef248990124)sip\_svc\_plat\_update\_trans\_id()

| void sip\_svc\_plat\_update\_trans\_id | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [sip\_svc\_request](structsip__svc__request.md) \* | *request*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *trans\_id* ) |

Update transaction id for [sip\_svc\_request](structsip__svc__request.md "SiP Service communication protocol request format.") for lower layer.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | request | Pointer to [sip\_svc\_request](structsip__svc__request.md "SiP Service communication protocol request format.") structure. |
    | trans\_id | Transaction id. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [sip\_svc](dir_be59f4c2e7724c8d2ef47362c82e9052.md)
- [sip\_svc\_driver.h](sip__svc__driver_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
