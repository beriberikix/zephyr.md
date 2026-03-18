---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__tee__interface.html
original_path: doxygen/html/group__tee__interface.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

TEE Interface

[Device Driver APIs](group__io__interfaces.md)

Trusted Execution Environment Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [tee\_version\_info](structtee__version__info.md) |
|  | TEE version. [More...](structtee__version__info.md#details) |
| struct | [tee\_open\_session\_arg](structtee__open__session__arg.md) |
|  | - Open session argument  [More...](structtee__open__session__arg.md#details) |
| struct | [tee\_param](structtee__param.md) |
|  | Tee parameter. [More...](structtee__param.md#details) |
| struct | [tee\_invoke\_func\_arg](structtee__invoke__func__arg.md) |
|  | Invokes a function in a Trusted Application. [More...](structtee__invoke__func__arg.md#details) |
| struct | [tee\_shm](structtee__shm.md) |
|  | Tee shared memory structure. [More...](structtee__shm.md#details) |
| struct | [tee\_driver\_api](structtee__driver__api.md) |

| Macros | |
| --- | --- |
| #define | [TEE\_UUID\_LEN](#ga79ff2ca70757daf8e677b42002f4aeac)   16 |
| #define | [TEE\_GEN\_CAP\_GP](#ga2eb5a95c2f50e08bbb6235fa47253f10)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) /\* GlobalPlatform compliant TEE \*/ |
| #define | [TEE\_GEN\_CAP\_PRIVILEGED](#ga15e96022b209b84d29c29f213aab0331)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) /\* Privileged [device](structdevice.md) (for supplicant) \*/ |
| #define | [TEE\_GEN\_CAP\_REG\_MEM](#gae661041c8b0f0638891a5a82b74aa928)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) /\* Supports registering shared memory \*/ |
| #define | [TEE\_GEN\_CAP\_MEMREF\_NULL](#ga4cd66a4425e312338823061e561638de)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) /\* Support NULL MemRef \*/ |
| #define | [TEE\_SHM\_REGISTER](#ga2fac25b74105b1ddfb15db51598b89c8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [TEE\_SHM\_ALLOC](#ga85fd3e6e6b596da02c97661a35c9814c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [TEE\_PARAM\_ATTR\_TYPE\_NONE](#gad3f8bf86812e0e5befa873389235ddd9)   0 /\* parameter not used \*/ |
| #define | [TEE\_PARAM\_ATTR\_TYPE\_VALUE\_INPUT](#ga5304d0bdbfb80563bdf3bd801cc72613)   1 |
| #define | [TEE\_PARAM\_ATTR\_TYPE\_VALUE\_OUTPUT](#gaf66e35aefb70c34cba93eeb5f3cb0f8a)   2 |
| #define | [TEE\_PARAM\_ATTR\_TYPE\_VALUE\_INOUT](#ga925026258aed48470a015a655f25b270)   3 /\* input and output \*/ |
| #define | [TEE\_PARAM\_ATTR\_TYPE\_MEMREF\_INPUT](#ga0c7f0c79fd599a2d5ec2759230bff6e7)   5 |
| #define | [TEE\_PARAM\_ATTR\_TYPE\_MEMREF\_OUTPUT](#ga5305a53edb649a22c774731bf2f53987)   6 |
| #define | [TEE\_PARAM\_ATTR\_TYPE\_MEMREF\_INOUT](#ga43fcdc052991d21fc7fde3720256ef2c)   7 /\* input and output \*/ |
| #define | [TEE\_PARAM\_ATTR\_TYPE\_MASK](#ga8e2dca32129d730d9394f0798d578ce7)   0xff |
| #define | [TEE\_PARAM\_ATTR\_META](#ga42e96de713673837d60ac3b938373206)   0x100 |
| #define | [TEE\_PARAM\_ATTR\_MASK](#ga15358e8f86ca9a2b6aca9899ee982542)   ([TEE\_PARAM\_ATTR\_TYPE\_MASK](#ga8e2dca32129d730d9394f0798d578ce7) | [TEE\_PARAM\_ATTR\_META](#ga42e96de713673837d60ac3b938373206)) |
| #define | [TEEC\_ORIGIN\_API](#ga6040bf64a72a13c675681c99112f7f69)   0x00000001 |
|  | Function error origins, of type TEEC\_ErrorOrigin. |
| #define | [TEEC\_ORIGIN\_COMMS](#ga668c5799e8360e3e885a908784805578)   0x00000002 |
| #define | [TEEC\_ORIGIN\_TEE](#gabebf4008dbbf440ac352d510675c9433)   0x00000003 |
| #define | [TEEC\_ORIGIN\_TRUSTED\_APP](#gaebb73e90a25eeecc5ac274c2c396f32f)   0x00000004 |
| #define | [TEEC\_SUCCESS](#gae000299e1a48b8e9c807c8e1b7e62aed)   0x00000000 |
|  | Return values. |
| #define | [TEEC\_ERROR\_STORAGE\_NOT\_AVAILABLE](#gad9e7d08ba6637d86cf611952b9842568)   0xF0100003 |
| #define | [TEEC\_ERROR\_GENERIC](#ga13c7ed6f37eba36870e4b138b661b61f)   0xFFFF0000 |
| #define | [TEEC\_ERROR\_ACCESS\_DENIED](#gad7c7cd2ed537347d60276bd08375ca30)   0xFFFF0001 |
| #define | [TEEC\_ERROR\_CANCEL](#ga8cbe25a679add519a048c85c03be1ede)   0xFFFF0002 |
| #define | [TEEC\_ERROR\_ACCESS\_CONFLICT](#ga65a8bd0582ef42f84e85704bab5a85fe)   0xFFFF0003 |
| #define | [TEEC\_ERROR\_EXCESS\_DATA](#gad8825a36962871ac2006386d18a821e7)   0xFFFF0004 |
| #define | [TEEC\_ERROR\_BAD\_FORMAT](#ga0e08a22cf7abe05ae2d0cfd7fe92b0e7)   0xFFFF0005 |
| #define | [TEEC\_ERROR\_BAD\_PARAMETERS](#ga79b607eb603bef58b3065a3014ee7117)   0xFFFF0006 |
| #define | [TEEC\_ERROR\_BAD\_STATE](#ga19c6e3eb278dd58fa49b7de3dff8b7ac)   0xFFFF0007 |
| #define | [TEEC\_ERROR\_ITEM\_NOT\_FOUND](#ga805299b26fda6bb38a97cf6a0825431d)   0xFFFF0008 |
| #define | [TEEC\_ERROR\_NOT\_IMPLEMENTED](#gaa7ef60306699f14fa7f3bcd6ed744633)   0xFFFF0009 |
| #define | [TEEC\_ERROR\_NOT\_SUPPORTED](#ga17041726bc43fb2a1aa3ddc927ac6cef)   0xFFFF000A |
| #define | [TEEC\_ERROR\_NO\_DATA](#gaf515dfd970be2caf575be186dd32afd7)   0xFFFF000B |
| #define | [TEEC\_ERROR\_OUT\_OF\_MEMORY](#gac7aaf1249147ecd63d6fba179e26ad33)   0xFFFF000C |
| #define | [TEEC\_ERROR\_BUSY](#ga28d244820db7caa7cb829ed3469f5961)   0xFFFF000D |
| #define | [TEEC\_ERROR\_COMMUNICATION](#ga0a3047b67556c437e80c308853705de2)   0xFFFF000E |
| #define | [TEEC\_ERROR\_SECURITY](#gaae2b6bb8d476d422f782e7ac226de21b)   0xFFFF000F |
| #define | [TEEC\_ERROR\_SHORT\_BUFFER](#ga511a0747fab1c307a5263a07ce396962)   0xFFFF0010 |
| #define | [TEEC\_ERROR\_EXTERNAL\_CANCEL](#ga10e9a718e8ce09e6fe117bc0b002a3d6)   0xFFFF0011 |
| #define | [TEEC\_ERROR\_TARGET\_DEAD](#ga6aa8da2d81b77fb8d2ec16f4e3a27528)   0xFFFF3024 |
| #define | [TEEC\_ERROR\_STORAGE\_NO\_SPACE](#ga6229f84eb575bf10c14b40f02495b46e)   0xFFFF3041 |
| #define | [TEEC\_LOGIN\_PUBLIC](#ga16baa8eb95393514c6035c957ad55a6b)   0x00000000 |
|  | Session login methods, for use in [tee\_open\_session()](#gad7c66e32d5b02c42c698bd422cf43523) as parameter connectionMethod. |
| #define | [TEEC\_LOGIN\_USER](#gab6940dd1f636aa67e74a8615e8544f85)   0x00000001 |
| #define | [TEEC\_LOGIN\_GROUP](#ga8cdd4a2102e18a60d0624d610ef3619e)   0x00000002 |
| #define | [TEEC\_LOGIN\_APPLICATION](#gae803496f14c6cc84b7f56174006c16a6)   0x00000004 |
| #define | [TEEC\_LOGIN\_USER\_APPLICATION](#ga37fbb624e8c289d400cd69948bf8b505)   0x00000005 |
| #define | [TEEC\_LOGIN\_GROUP\_APPLICATION](#gad1da184306fe0283fc1e618f829119e3)   0x00000006 |

| Typedefs | |
| --- | --- |
| typedef int(\* | [tee\_get\_version\_t](#gac533d9e85d65857c0d984506024a55b4)) (const struct [device](structdevice.md) \*dev, struct [tee\_version\_info](structtee__version__info.md) \*info) |
|  | Callback API to get current tee version. |
| typedef int(\* | [tee\_open\_session\_t](#gaf972199fcdbd892688dc141ddba6e6aa)) (const struct [device](structdevice.md) \*dev, struct [tee\_open\_session\_arg](structtee__open__session__arg.md) \*arg, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int num\_param, struct [tee\_param](structtee__param.md) \*param, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*session\_id) |
|  | Callback API to open session to Trusted Application. |
| typedef int(\* | [tee\_close\_session\_t](#gac412f57a3da187e6e272857d5bdaaaeb)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) session\_id) |
|  | Callback API to close session to TA. |
| typedef int(\* | [tee\_cancel\_t](#gad4cd5b65cac3eb7b4338fd99eeb13a93)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) session\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cancel\_id) |
|  | Callback API to cancel open session of invoke function to TA. |
| typedef int(\* | [tee\_invoke\_func\_t](#gac3695e51dc8b08bb5e5c5d984c402b0e)) (const struct [device](structdevice.md) \*dev, struct [tee\_invoke\_func\_arg](structtee__invoke__func__arg.md) \*arg, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int num\_param, struct [tee\_param](structtee__param.md) \*param) |
|  | Callback API to invoke function to TA. |
| typedef int(\* | [tee\_shm\_register\_t](#ga9e2807d34d580c012129a2fc1f5a425a)) (const struct [device](structdevice.md) \*dev, struct [tee\_shm](structtee__shm.md) \*shm) |
|  | Callback API to register shared memory. |
| typedef int(\* | [tee\_shm\_unregister\_t](#ga2ea18e713a101a6ca715baa04c2f4185)) (const struct [device](structdevice.md) \*dev, struct [tee\_shm](structtee__shm.md) \*shm) |
|  | Callback API to unregister shared memory. |
| typedef int(\* | [tee\_suppl\_recv\_t](#gaae68677cbff1e831fadc3d188c8588ff)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*func, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int \*num\_params, struct [tee\_param](structtee__param.md) \*param) |
|  | Callback API to receive a request for TEE supplicant. |
| typedef int(\* | [tee\_suppl\_send\_t](#ga3e8ec4e17ed48cb90bb0cbb1e9ddbb20)) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int ret, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int num\_params, struct [tee\_param](structtee__param.md) \*param) |
|  | Callback API to send a request for TEE supplicant. |

| Functions | |
| --- | --- |
| int | [tee\_get\_version](#gadaaec6b6ea29d81f36943bbe5bcb305e) (const struct [device](structdevice.md) \*dev, struct [tee\_version\_info](structtee__version__info.md) \*info) |
|  | Get the current TEE version info. |
| int | [tee\_open\_session](#gad7c66e32d5b02c42c698bd422cf43523) (const struct [device](structdevice.md) \*dev, struct [tee\_open\_session\_arg](structtee__open__session__arg.md) \*arg, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int num\_param, struct [tee\_param](structtee__param.md) \*param, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*session\_id) |
|  | Open session for Trusted Environment. |
| int | [tee\_close\_session](#gacb1d58002378a11d92361a149d451241) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) session\_id) |
|  | Close session for Trusted Environment. |
| int | [tee\_cancel](#ga34fbbfe48a07541041ffddb9e318332a) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) session\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cancel\_id) |
|  | Cancel session or invoke function for Trusted Environment. |
| int | [tee\_invoke\_func](#gae1337f293febcecc7dbc79ac064e7824) (const struct [device](structdevice.md) \*dev, struct [tee\_invoke\_func\_arg](structtee__invoke__func__arg.md) \*arg, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int num\_param, struct [tee\_param](structtee__param.md) \*param) |
|  | Invoke function for Trusted Environment Application. |
| int | [tee\_add\_shm](#gade7fdbece8b0bd47f5d148572016c4ef) (const struct [device](structdevice.md) \*dev, void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct [tee\_shm](structtee__shm.md) \*\*shmp) |
|  | Helper function to allocate and register shared memory. |
| int | [tee\_rm\_shm](#gaf53521a3e3a36a9827753716bef1434f) (const struct [device](structdevice.md) \*dev, struct [tee\_shm](structtee__shm.md) \*shm) |
|  | Helper function to remove and unregister shared memory. |
| int | [tee\_shm\_register](#ga1565c23104792203ede9d9cb388ff782) (const struct [device](structdevice.md) \*dev, void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct [tee\_shm](structtee__shm.md) \*\*shm) |
|  | Register shared memory for Trusted Environment. |
| int | [tee\_shm\_unregister](#gade2c0e7d89e3594707637b62a1901bac) (const struct [device](structdevice.md) \*dev, struct [tee\_shm](structtee__shm.md) \*shm) |
|  | Unregister shared memory for Trusted Environment. |
| int | [tee\_shm\_alloc](#ga47f7403e2b136f755432159c7bd679a5) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct [tee\_shm](structtee__shm.md) \*\*shm) |
|  | Allocate shared memory region for Trusted Environment. |
| int | [tee\_shm\_free](#ga346d8d67a18542c097f1254c0ace8726) (const struct [device](structdevice.md) \*dev, struct [tee\_shm](structtee__shm.md) \*shm) |
|  | Free shared memory region for Trusted Environment. |
| int | [tee\_suppl\_recv](#ga2213f63da1f080beaedc169e13531a37) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*func, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int \*num\_params, struct [tee\_param](structtee__param.md) \*param) |
|  | Receive a request for TEE Supplicant. |
| int | [tee\_suppl\_send](#ga93cccfa446983be704f364760bf7567b) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int ret, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int num\_params, struct [tee\_param](structtee__param.md) \*param) |
|  | Send a request for TEE Supplicant function. |

## Detailed Description

Trusted Execution Environment Interface.

The generic interface to work with Trusted Execution Environment (TEE). TEE is Trusted OS, running in the Secure Space, such as TrustZone in ARM cpus. It also can be presented as the separate secure co-processors. It allows system to implement logic, separated from the Normal World.

Using TEE syscalls:

- [tee\_get\_version()](#gadaaec6b6ea29d81f36943bbe5bcb305e) to get current TEE capabilities
- [tee\_open\_session()](#gad7c66e32d5b02c42c698bd422cf43523) to open new session to the TA
- [tee\_close\_session()](#gacb1d58002378a11d92361a149d451241) to close session to the TA
- [tee\_cancel()](#ga34fbbfe48a07541041ffddb9e318332a) to cancel session or invoke function
- [tee\_invoke\_func()](#gae1337f293febcecc7dbc79ac064e7824) to invoke function to the TA
- [tee\_shm\_register()](#ga1565c23104792203ede9d9cb388ff782) to register shared memory region
- [tee\_shm\_unregister()](#gade2c0e7d89e3594707637b62a1901bac) to unregister shared memory region
- [tee\_shm\_alloc()](#ga47f7403e2b136f755432159c7bd679a5) to allocate shared memory region
- [tee\_shm\_free()](#ga346d8d67a18542c097f1254c0ace8726) to free shared memory region

## Macro Definition Documentation

## [◆ ](#ga2eb5a95c2f50e08bbb6235fa47253f10)TEE\_GEN\_CAP\_GP

| #define TEE\_GEN\_CAP\_GP   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) /\* GlobalPlatform compliant TEE \*/ |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga4cd66a4425e312338823061e561638de)TEE\_GEN\_CAP\_MEMREF\_NULL

| #define TEE\_GEN\_CAP\_MEMREF\_NULL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) /\* Support NULL MemRef \*/ |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga15e96022b209b84d29c29f213aab0331)TEE\_GEN\_CAP\_PRIVILEGED

| #define TEE\_GEN\_CAP\_PRIVILEGED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) /\* Privileged [device](structdevice.md) (for supplicant) \*/ |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#gae661041c8b0f0638891a5a82b74aa928)TEE\_GEN\_CAP\_REG\_MEM

| #define TEE\_GEN\_CAP\_REG\_MEM   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) /\* Supports registering shared memory \*/ |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga15358e8f86ca9a2b6aca9899ee982542)TEE\_PARAM\_ATTR\_MASK

| #define TEE\_PARAM\_ATTR\_MASK   ([TEE\_PARAM\_ATTR\_TYPE\_MASK](#ga8e2dca32129d730d9394f0798d578ce7) | [TEE\_PARAM\_ATTR\_META](#ga42e96de713673837d60ac3b938373206)) |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga42e96de713673837d60ac3b938373206)TEE\_PARAM\_ATTR\_META

| #define TEE\_PARAM\_ATTR\_META   0x100 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga8e2dca32129d730d9394f0798d578ce7)TEE\_PARAM\_ATTR\_TYPE\_MASK

| #define TEE\_PARAM\_ATTR\_TYPE\_MASK   0xff |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga43fcdc052991d21fc7fde3720256ef2c)TEE\_PARAM\_ATTR\_TYPE\_MEMREF\_INOUT

| #define TEE\_PARAM\_ATTR\_TYPE\_MEMREF\_INOUT   7 /\* input and output \*/ |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga0c7f0c79fd599a2d5ec2759230bff6e7)TEE\_PARAM\_ATTR\_TYPE\_MEMREF\_INPUT

| #define TEE\_PARAM\_ATTR\_TYPE\_MEMREF\_INPUT   5 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga5305a53edb649a22c774731bf2f53987)TEE\_PARAM\_ATTR\_TYPE\_MEMREF\_OUTPUT

| #define TEE\_PARAM\_ATTR\_TYPE\_MEMREF\_OUTPUT   6 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#gad3f8bf86812e0e5befa873389235ddd9)TEE\_PARAM\_ATTR\_TYPE\_NONE

| #define TEE\_PARAM\_ATTR\_TYPE\_NONE   0 /\* parameter not used \*/ |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga925026258aed48470a015a655f25b270)TEE\_PARAM\_ATTR\_TYPE\_VALUE\_INOUT

| #define TEE\_PARAM\_ATTR\_TYPE\_VALUE\_INOUT   3 /\* input and output \*/ |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga5304d0bdbfb80563bdf3bd801cc72613)TEE\_PARAM\_ATTR\_TYPE\_VALUE\_INPUT

| #define TEE\_PARAM\_ATTR\_TYPE\_VALUE\_INPUT   1 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#gaf66e35aefb70c34cba93eeb5f3cb0f8a)TEE\_PARAM\_ATTR\_TYPE\_VALUE\_OUTPUT

| #define TEE\_PARAM\_ATTR\_TYPE\_VALUE\_OUTPUT   2 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga85fd3e6e6b596da02c97661a35c9814c)TEE\_SHM\_ALLOC

| #define TEE\_SHM\_ALLOC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga2fac25b74105b1ddfb15db51598b89c8)TEE\_SHM\_REGISTER

| #define TEE\_SHM\_REGISTER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga79ff2ca70757daf8e677b42002f4aeac)TEE\_UUID\_LEN

| #define TEE\_UUID\_LEN   16 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga65a8bd0582ef42f84e85704bab5a85fe)TEEC\_ERROR\_ACCESS\_CONFLICT

| #define TEEC\_ERROR\_ACCESS\_CONFLICT   0xFFFF0003 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#gad7c7cd2ed537347d60276bd08375ca30)TEEC\_ERROR\_ACCESS\_DENIED

| #define TEEC\_ERROR\_ACCESS\_DENIED   0xFFFF0001 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga0e08a22cf7abe05ae2d0cfd7fe92b0e7)TEEC\_ERROR\_BAD\_FORMAT

| #define TEEC\_ERROR\_BAD\_FORMAT   0xFFFF0005 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga79b607eb603bef58b3065a3014ee7117)TEEC\_ERROR\_BAD\_PARAMETERS

| #define TEEC\_ERROR\_BAD\_PARAMETERS   0xFFFF0006 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga19c6e3eb278dd58fa49b7de3dff8b7ac)TEEC\_ERROR\_BAD\_STATE

| #define TEEC\_ERROR\_BAD\_STATE   0xFFFF0007 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga28d244820db7caa7cb829ed3469f5961)TEEC\_ERROR\_BUSY

| #define TEEC\_ERROR\_BUSY   0xFFFF000D |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga8cbe25a679add519a048c85c03be1ede)TEEC\_ERROR\_CANCEL

| #define TEEC\_ERROR\_CANCEL   0xFFFF0002 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga0a3047b67556c437e80c308853705de2)TEEC\_ERROR\_COMMUNICATION

| #define TEEC\_ERROR\_COMMUNICATION   0xFFFF000E |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#gad8825a36962871ac2006386d18a821e7)TEEC\_ERROR\_EXCESS\_DATA

| #define TEEC\_ERROR\_EXCESS\_DATA   0xFFFF0004 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga10e9a718e8ce09e6fe117bc0b002a3d6)TEEC\_ERROR\_EXTERNAL\_CANCEL

| #define TEEC\_ERROR\_EXTERNAL\_CANCEL   0xFFFF0011 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga13c7ed6f37eba36870e4b138b661b61f)TEEC\_ERROR\_GENERIC

| #define TEEC\_ERROR\_GENERIC   0xFFFF0000 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga805299b26fda6bb38a97cf6a0825431d)TEEC\_ERROR\_ITEM\_NOT\_FOUND

| #define TEEC\_ERROR\_ITEM\_NOT\_FOUND   0xFFFF0008 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#gaf515dfd970be2caf575be186dd32afd7)TEEC\_ERROR\_NO\_DATA

| #define TEEC\_ERROR\_NO\_DATA   0xFFFF000B |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#gaa7ef60306699f14fa7f3bcd6ed744633)TEEC\_ERROR\_NOT\_IMPLEMENTED

| #define TEEC\_ERROR\_NOT\_IMPLEMENTED   0xFFFF0009 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga17041726bc43fb2a1aa3ddc927ac6cef)TEEC\_ERROR\_NOT\_SUPPORTED

| #define TEEC\_ERROR\_NOT\_SUPPORTED   0xFFFF000A |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#gac7aaf1249147ecd63d6fba179e26ad33)TEEC\_ERROR\_OUT\_OF\_MEMORY

| #define TEEC\_ERROR\_OUT\_OF\_MEMORY   0xFFFF000C |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#gaae2b6bb8d476d422f782e7ac226de21b)TEEC\_ERROR\_SECURITY

| #define TEEC\_ERROR\_SECURITY   0xFFFF000F |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga511a0747fab1c307a5263a07ce396962)TEEC\_ERROR\_SHORT\_BUFFER

| #define TEEC\_ERROR\_SHORT\_BUFFER   0xFFFF0010 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga6229f84eb575bf10c14b40f02495b46e)TEEC\_ERROR\_STORAGE\_NO\_SPACE

| #define TEEC\_ERROR\_STORAGE\_NO\_SPACE   0xFFFF3041 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#gad9e7d08ba6637d86cf611952b9842568)TEEC\_ERROR\_STORAGE\_NOT\_AVAILABLE

| #define TEEC\_ERROR\_STORAGE\_NOT\_AVAILABLE   0xF0100003 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga6aa8da2d81b77fb8d2ec16f4e3a27528)TEEC\_ERROR\_TARGET\_DEAD

| #define TEEC\_ERROR\_TARGET\_DEAD   0xFFFF3024 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#gae803496f14c6cc84b7f56174006c16a6)TEEC\_LOGIN\_APPLICATION

| #define TEEC\_LOGIN\_APPLICATION   0x00000004 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga8cdd4a2102e18a60d0624d610ef3619e)TEEC\_LOGIN\_GROUP

| #define TEEC\_LOGIN\_GROUP   0x00000002 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#gad1da184306fe0283fc1e618f829119e3)TEEC\_LOGIN\_GROUP\_APPLICATION

| #define TEEC\_LOGIN\_GROUP\_APPLICATION   0x00000006 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga16baa8eb95393514c6035c957ad55a6b)TEEC\_LOGIN\_PUBLIC

| #define TEEC\_LOGIN\_PUBLIC   0x00000000 |
| --- |

`#include <[tee.h](tee_8h.md)>`

Session login methods, for use in [tee\_open\_session()](#gad7c66e32d5b02c42c698bd422cf43523) as parameter connectionMethod.

Type is [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f).

TEEC\_LOGIN\_PUBLIC No login data is provided. TEEC\_LOGIN\_USER Login data about the user running the Client Application process is provided. TEEC\_LOGIN\_GROUP Login data about the group running the Client Application process is provided. TEEC\_LOGIN\_APPLICATION Login data about the running Client Application itself is provided. TEEC\_LOGIN\_USER\_APPLICATION Login data about the user and the running Client Application itself is provided. TEEC\_LOGIN\_GROUP\_APPLICATION Login data about the group and the running Client Application itself is provided.

## [◆ ](#gab6940dd1f636aa67e74a8615e8544f85)TEEC\_LOGIN\_USER

| #define TEEC\_LOGIN\_USER   0x00000001 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga37fbb624e8c289d400cd69948bf8b505)TEEC\_LOGIN\_USER\_APPLICATION

| #define TEEC\_LOGIN\_USER\_APPLICATION   0x00000005 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#ga6040bf64a72a13c675681c99112f7f69)TEEC\_ORIGIN\_API

| #define TEEC\_ORIGIN\_API   0x00000001 |
| --- |

`#include <[tee.h](tee_8h.md)>`

Function error origins, of type TEEC\_ErrorOrigin.

These indicate where in the software stack a particular return value originates from.

TEEC\_ORIGIN\_API The error originated within the TEE Client API implementation. TEEC\_ORIGIN\_COMMS The error originated within the underlying communications stack linking the rich OS with the TEE. TEEC\_ORIGIN\_TEE The error originated within the common TEE code. TEEC\_ORIGIN\_TRUSTED\_APP The error originated within the Trusted Application code.

## [◆ ](#ga668c5799e8360e3e885a908784805578)TEEC\_ORIGIN\_COMMS

| #define TEEC\_ORIGIN\_COMMS   0x00000002 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#gabebf4008dbbf440ac352d510675c9433)TEEC\_ORIGIN\_TEE

| #define TEEC\_ORIGIN\_TEE   0x00000003 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#gaebb73e90a25eeecc5ac274c2c396f32f)TEEC\_ORIGIN\_TRUSTED\_APP

| #define TEEC\_ORIGIN\_TRUSTED\_APP   0x00000004 |
| --- |

`#include <[tee.h](tee_8h.md)>`

## [◆ ](#gae000299e1a48b8e9c807c8e1b7e62aed)TEEC\_SUCCESS

| #define TEEC\_SUCCESS   0x00000000 |
| --- |

`#include <[tee.h](tee_8h.md)>`

Return values.

Type is TEEC\_Result

TEEC\_SUCCESS The operation was successful. TEEC\_ERROR\_GENERIC Non-specific cause. TEEC\_ERROR\_ACCESS\_DENIED Access privileges are not sufficient. TEEC\_ERROR\_CANCEL The operation was canceled. TEEC\_ERROR\_ACCESS\_CONFLICT Concurrent accesses caused conflict. TEEC\_ERROR\_EXCESS\_DATA Too much data for the requested operation was passed. TEEC\_ERROR\_BAD\_FORMAT Input data was of invalid format. TEEC\_ERROR\_BAD\_PARAMETERS Input parameters were invalid. TEEC\_ERROR\_BAD\_STATE Operation is not valid in the current state. TEEC\_ERROR\_ITEM\_NOT\_FOUND The requested data item is not found. TEEC\_ERROR\_NOT\_IMPLEMENTED The requested operation should exist but is not yet implemented. TEEC\_ERROR\_NOT\_SUPPORTED The requested operation is valid but is not supported in this implementation. TEEC\_ERROR\_NO\_DATA Expected data was missing. TEEC\_ERROR\_OUT\_OF\_MEMORY System ran out of resources. TEEC\_ERROR\_BUSY The system is busy working on something else. TEEC\_ERROR\_COMMUNICATION Communication with a remote party failed. TEEC\_ERROR\_SECURITY A security fault was detected. TEEC\_ERROR\_SHORT\_BUFFER The supplied buffer is too short for the generated output. TEEC\_ERROR\_TARGET\_DEAD Trusted Application has panicked during the operation. Standard defined error codes.

## Typedef Documentation

## [◆ ](#gad4cd5b65cac3eb7b4338fd99eeb13a93)tee\_cancel\_t

| typedef int(\* tee\_cancel\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) session\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cancel\_id) |
| --- |

`#include <[tee.h](tee_8h.md)>`

Callback API to cancel open session of invoke function to TA.

See *[tee\_cancel()](#ga34fbbfe48a07541041ffddb9e318332a)* for argument definitions.

## [◆ ](#gac412f57a3da187e6e272857d5bdaaaeb)tee\_close\_session\_t

| typedef int(\* tee\_close\_session\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) session\_id) |
| --- |

`#include <[tee.h](tee_8h.md)>`

Callback API to close session to TA.

See *[tee\_close\_session()](#gacb1d58002378a11d92361a149d451241)* for argument definitions.

## [◆ ](#gac533d9e85d65857c0d984506024a55b4)tee\_get\_version\_t

| typedef int(\* tee\_get\_version\_t) (const struct [device](structdevice.md) \*dev, struct [tee\_version\_info](structtee__version__info.md) \*info) |
| --- |

`#include <[tee.h](tee_8h.md)>`

Callback API to get current tee version.

See *tee\_version\_get()* for argument definitions.

## [◆ ](#gac3695e51dc8b08bb5e5c5d984c402b0e)tee\_invoke\_func\_t

| typedef int(\* tee\_invoke\_func\_t) (const struct [device](structdevice.md) \*dev, struct [tee\_invoke\_func\_arg](structtee__invoke__func__arg.md) \*arg, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int num\_param, struct [tee\_param](structtee__param.md) \*param) |
| --- |

`#include <[tee.h](tee_8h.md)>`

Callback API to invoke function to TA.

See *[tee\_invoke\_func()](#gae1337f293febcecc7dbc79ac064e7824)* for argument definitions.

## [◆ ](#gaf972199fcdbd892688dc141ddba6e6aa)tee\_open\_session\_t

| typedef int(\* tee\_open\_session\_t) (const struct [device](structdevice.md) \*dev, struct [tee\_open\_session\_arg](structtee__open__session__arg.md) \*arg, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int num\_param, struct [tee\_param](structtee__param.md) \*param, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*session\_id) |
| --- |

`#include <[tee.h](tee_8h.md)>`

Callback API to open session to Trusted Application.

See *[tee\_open\_session()](#gad7c66e32d5b02c42c698bd422cf43523)* for argument definitions.

## [◆ ](#ga9e2807d34d580c012129a2fc1f5a425a)tee\_shm\_register\_t

| typedef int(\* tee\_shm\_register\_t) (const struct [device](structdevice.md) \*dev, struct [tee\_shm](structtee__shm.md) \*shm) |
| --- |

`#include <[tee.h](tee_8h.md)>`

Callback API to register shared memory.

See *[tee\_shm\_register()](#ga1565c23104792203ede9d9cb388ff782)* for argument definitions.

## [◆ ](#ga2ea18e713a101a6ca715baa04c2f4185)tee\_shm\_unregister\_t

| typedef int(\* tee\_shm\_unregister\_t) (const struct [device](structdevice.md) \*dev, struct [tee\_shm](structtee__shm.md) \*shm) |
| --- |

`#include <[tee.h](tee_8h.md)>`

Callback API to unregister shared memory.

See *[tee\_shm\_unregister()](#gade2c0e7d89e3594707637b62a1901bac)* for argument definitions.

## [◆ ](#gaae68677cbff1e831fadc3d188c8588ff)tee\_suppl\_recv\_t

| typedef int(\* tee\_suppl\_recv\_t) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*func, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int \*num\_params, struct [tee\_param](structtee__param.md) \*param) |
| --- |

`#include <[tee.h](tee_8h.md)>`

Callback API to receive a request for TEE supplicant.

See *[tee\_suppl\_recv()](#ga2213f63da1f080beaedc169e13531a37)* for argument definitions.

## [◆ ](#ga3e8ec4e17ed48cb90bb0cbb1e9ddbb20)tee\_suppl\_send\_t

| typedef int(\* tee\_suppl\_send\_t) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int ret, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int num\_params, struct [tee\_param](structtee__param.md) \*param) |
| --- |

`#include <[tee.h](tee_8h.md)>`

Callback API to send a request for TEE supplicant.

See *[tee\_suppl\_send()](#ga93cccfa446983be704f364760bf7567b)* for argument definitions.

## Function Documentation

## [◆ ](#gade7fdbece8b0bd47f5d148572016c4ef)tee\_add\_shm()

| int tee\_add\_shm | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | void \* | *addr*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *align*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags*, |
|  |  | struct [tee\_shm](structtee__shm.md) \*\* | *shmp* ) |

`#include <[tee.h](tee_8h.md)>`

Helper function to allocate and register shared memory.

Allocates and registers shared memory for TEE

Parameters
:   | dev | TEE device |
    | --- | --- |
    | addr | Address of the shared memory |
    | align | Region alignment |
    | size | Size of the shared memory region |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags to set registering parameters |
    | shmp | Return shared memory structure |

Return values
:   | 0 | On success, negative on error |
    | --- | --- |

## [◆ ](#ga34fbbfe48a07541041ffddb9e318332a)tee\_cancel()

| int tee\_cancel | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *session\_id*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *cancel\_id* ) |

`#include <[tee.h](tee_8h.md)>`

Cancel session or invoke function for Trusted Environment.

Cancels session or invoke function for TA

Parameters
:   | dev | TEE device |
    | --- | --- |
    | session\_id | session to close |
    | cancel\_id | cancel reason |

Return values
:   | -ENOSYS | If callback was not implemented |
    | --- | --- |
    | 0 | On success, negative on error |

## [◆ ](#gacb1d58002378a11d92361a149d451241)tee\_close\_session()

| int tee\_close\_session | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *session\_id* ) |

`#include <[tee.h](tee_8h.md)>`

Close session for Trusted Environment.

Closes session to the Trusted Environment

Parameters
:   | dev | TEE device |
    | --- | --- |
    | session\_id | session to close |

Return values
:   | -ENOSYS | If callback was not implemented |
    | --- | --- |
    | 0 | On success, negative on error |

## [◆ ](#gadaaec6b6ea29d81f36943bbe5bcb305e)tee\_get\_version()

| int tee\_get\_version | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [tee\_version\_info](structtee__version__info.md) \* | *info* ) |

`#include <[tee.h](tee_8h.md)>`

Get the current TEE version info.

Returns info as tee version info which includes capabilities description

Parameters
:   | dev | TEE device |
    | --- | --- |
    | info | Structure to return the capabilities |

Return values
:   | -ENOSYS | If callback was not implemented |
    | --- | --- |
    | 0 | On success, negative on error |

## [◆ ](#gae1337f293febcecc7dbc79ac064e7824)tee\_invoke\_func()

| int tee\_invoke\_func | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [tee\_invoke\_func\_arg](structtee__invoke__func__arg.md) \* | *arg*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *num\_param*, |
|  |  | struct [tee\_param](structtee__param.md) \* | *param* ) |

`#include <[tee.h](tee_8h.md)>`

Invoke function for Trusted Environment Application.

Invokes function to the TA

Parameters
:   | dev | TEE device |
    | --- | --- |
    | arg | Structure with the invoke function arguments |
    | num\_param | Number of the additional params to be passed |
    | param | List of the params to pass to open\_session call |

Return values
:   | -ENOSYS | If callback was not implemented |
    | --- | --- |
    | 0 | On success, negative on error |

## [◆ ](#gad7c66e32d5b02c42c698bd422cf43523)tee\_open\_session()

| int tee\_open\_session | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [tee\_open\_session\_arg](structtee__open__session__arg.md) \* | *arg*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *num\_param*, |
|  |  | struct [tee\_param](structtee__param.md) \* | *param*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *session\_id* ) |

`#include <[tee.h](tee_8h.md)>`

Open session for Trusted Environment.

Opens the new session to the Trusted Environment

Parameters
:   | dev | TEE device |
    | --- | --- |
    | arg | Structure with the session arguments |
    | num\_param | Number of the additional params to be passed |
    | param | List of the params to pass to open\_session call |
    | session\_id | Returns id of the created session |

Return values
:   | -ENOSYS | If callback was not implemented |
    | --- | --- |
    | 0 | On success, negative on error |

## [◆ ](#gaf53521a3e3a36a9827753716bef1434f)tee\_rm\_shm()

| int tee\_rm\_shm | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [tee\_shm](structtee__shm.md) \* | *shm* ) |

`#include <[tee.h](tee_8h.md)>`

Helper function to remove and unregister shared memory.

Removes and unregisters shared memory for TEE

Parameters
:   | dev | TEE device |
    | --- | --- |
    | shm | Pointer to [tee\_shm](structtee__shm.md "Tee shared memory structure.") structure |

Return values
:   | 0 | On success, negative on error |
    | --- | --- |

## [◆ ](#ga47f7403e2b136f755432159c7bd679a5)tee\_shm\_alloc()

| int tee\_shm\_alloc | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags*, |
|  |  | struct [tee\_shm](structtee__shm.md) \*\* | *shm* ) |

`#include <[tee.h](tee_8h.md)>`

Allocate shared memory region for Trusted Environment.

Allocate shared memory for TEE

Parameters
:   | dev | TEE device |
    | --- | --- |
    | size | Region size |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | to allocate region |
    | shm | Return shared memory structure |

Return values
:   | -ENOSYS | If callback was not implemented |
    | --- | --- |
    | 0 | On success, negative on error |

## [◆ ](#ga346d8d67a18542c097f1254c0ace8726)tee\_shm\_free()

| int tee\_shm\_free | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [tee\_shm](structtee__shm.md) \* | *shm* ) |

`#include <[tee.h](tee_8h.md)>`

Free shared memory region for Trusted Environment.

Frees shared memory for TEE

Parameters
:   | dev | TEE device |
    | --- | --- |
    | shm | Shared memory structure |

Return values
:   | -ENOSYS | If callback was not implemented |
    | --- | --- |
    | 0 | On success, negative on error |

## [◆ ](#ga1565c23104792203ede9d9cb388ff782)tee\_shm\_register()

| int tee\_shm\_register | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | void \* | *addr*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *size*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags*, |
|  |  | struct [tee\_shm](structtee__shm.md) \*\* | *shm* ) |

`#include <[tee.h](tee_8h.md)>`

Register shared memory for Trusted Environment.

Registers shared memory for TEE

Parameters
:   | dev | TEE device |
    | --- | --- |
    | addr | Address of the shared memory |
    | size | Size of the shared memory region |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags to set registering parameters |
    | shm | Return shared memory structure |

Return values
:   | -ENOSYS | If callback was not implemented |
    | --- | --- |
    | 0 | On success, negative on error |

## [◆ ](#gade2c0e7d89e3594707637b62a1901bac)tee\_shm\_unregister()

| int tee\_shm\_unregister | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [tee\_shm](structtee__shm.md) \* | *shm* ) |

`#include <[tee.h](tee_8h.md)>`

Unregister shared memory for Trusted Environment.

Unregisters shared memory for TEE

Parameters
:   | dev | TEE device |
    | --- | --- |
    | shm | Shared memory structure |

Return values
:   | -ENOSYS | If callback was not implemented |
    | --- | --- |
    | 0 | On success, negative on error |

## [◆ ](#ga2213f63da1f080beaedc169e13531a37)tee\_suppl\_recv()

| int tee\_suppl\_recv | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *func*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int \* | *num\_params*, |
|  |  | struct [tee\_param](structtee__param.md) \* | *param* ) |

`#include <[tee.h](tee_8h.md)>`

Receive a request for TEE Supplicant.

Parameters
:   | dev | TEE device |
    | --- | --- |
    | func | Supplicant function |
    | num\_params | Number of parameters to be passed |
    | param | List of the params for send/receive |

Return values
:   | -ENOSYS | If callback was not implemented |
    | --- | --- |
    | 0 | On success, negative on error |

## [◆ ](#ga93cccfa446983be704f364760bf7567b)tee\_suppl\_send()

| int tee\_suppl\_send | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *ret*, |
|  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *num\_params*, |
|  |  | struct [tee\_param](structtee__param.md) \* | *param* ) |

`#include <[tee.h](tee_8h.md)>`

Send a request for TEE Supplicant function.

Parameters
:   | dev | TEE device |
    | --- | --- |
    | ret | supplicant return code |
    | num\_params | Number of parameters to be passed |
    | param | List of the params for send/receive |

Return values
:   | -ENOSYS | If callback was not implemented |
    | --- | --- |
    | Return | value for sent request |
    | 0 | On success, negative on error |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
