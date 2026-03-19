---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/tee_8h.html
original_path: doxygen/html/tee_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tee.h File Reference

Public APIs for the tee driver.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <zephyr/syscalls/tee.h>`

[Go to the source code of this file.](tee_8h_source.md)

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
| #define | [TEE\_UUID\_LEN](group__tee__interface.md#ga79ff2ca70757daf8e677b42002f4aeac)   16 |
| #define | [TEE\_GEN\_CAP\_GP](group__tee__interface.md#ga2eb5a95c2f50e08bbb6235fa47253f10)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) /\* GlobalPlatform compliant TEE \*/ |
| #define | [TEE\_GEN\_CAP\_PRIVILEGED](group__tee__interface.md#ga15e96022b209b84d29c29f213aab0331)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) /\* Privileged [device](structdevice.md) (for supplicant) \*/ |
| #define | [TEE\_GEN\_CAP\_REG\_MEM](group__tee__interface.md#gae661041c8b0f0638891a5a82b74aa928)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) /\* Supports registering shared memory \*/ |
| #define | [TEE\_GEN\_CAP\_MEMREF\_NULL](group__tee__interface.md#ga4cd66a4425e312338823061e561638de)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) /\* Support NULL MemRef \*/ |
| #define | [TEE\_SHM\_REGISTER](group__tee__interface.md#ga2fac25b74105b1ddfb15db51598b89c8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [TEE\_SHM\_ALLOC](group__tee__interface.md#ga85fd3e6e6b596da02c97661a35c9814c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [TEE\_PARAM\_ATTR\_TYPE\_NONE](group__tee__interface.md#gad3f8bf86812e0e5befa873389235ddd9)   0 /\* parameter not used \*/ |
| #define | [TEE\_PARAM\_ATTR\_TYPE\_VALUE\_INPUT](group__tee__interface.md#ga5304d0bdbfb80563bdf3bd801cc72613)   1 |
| #define | [TEE\_PARAM\_ATTR\_TYPE\_VALUE\_OUTPUT](group__tee__interface.md#gaf66e35aefb70c34cba93eeb5f3cb0f8a)   2 |
| #define | [TEE\_PARAM\_ATTR\_TYPE\_VALUE\_INOUT](group__tee__interface.md#ga925026258aed48470a015a655f25b270)   3 /\* input and output \*/ |
| #define | [TEE\_PARAM\_ATTR\_TYPE\_MEMREF\_INPUT](group__tee__interface.md#ga0c7f0c79fd599a2d5ec2759230bff6e7)   5 |
| #define | [TEE\_PARAM\_ATTR\_TYPE\_MEMREF\_OUTPUT](group__tee__interface.md#ga5305a53edb649a22c774731bf2f53987)   6 |
| #define | [TEE\_PARAM\_ATTR\_TYPE\_MEMREF\_INOUT](group__tee__interface.md#ga43fcdc052991d21fc7fde3720256ef2c)   7 /\* input and output \*/ |
| #define | [TEE\_PARAM\_ATTR\_TYPE\_MASK](group__tee__interface.md#ga8e2dca32129d730d9394f0798d578ce7)   0xff |
| #define | [TEE\_PARAM\_ATTR\_META](group__tee__interface.md#ga42e96de713673837d60ac3b938373206)   0x100 |
| #define | [TEE\_PARAM\_ATTR\_MASK](group__tee__interface.md#ga15358e8f86ca9a2b6aca9899ee982542)   ([TEE\_PARAM\_ATTR\_TYPE\_MASK](group__tee__interface.md#ga8e2dca32129d730d9394f0798d578ce7) | [TEE\_PARAM\_ATTR\_META](group__tee__interface.md#ga42e96de713673837d60ac3b938373206)) |
| #define | [TEEC\_ORIGIN\_API](group__tee__interface.md#ga6040bf64a72a13c675681c99112f7f69)   0x00000001 |
|  | Function error origins, of type TEEC\_ErrorOrigin. |
| #define | [TEEC\_ORIGIN\_COMMS](group__tee__interface.md#ga668c5799e8360e3e885a908784805578)   0x00000002 |
| #define | [TEEC\_ORIGIN\_TEE](group__tee__interface.md#gabebf4008dbbf440ac352d510675c9433)   0x00000003 |
| #define | [TEEC\_ORIGIN\_TRUSTED\_APP](group__tee__interface.md#gaebb73e90a25eeecc5ac274c2c396f32f)   0x00000004 |
| #define | [TEEC\_SUCCESS](group__tee__interface.md#gae000299e1a48b8e9c807c8e1b7e62aed)   0x00000000 |
|  | Return values. |
| #define | [TEEC\_ERROR\_STORAGE\_NOT\_AVAILABLE](group__tee__interface.md#gad9e7d08ba6637d86cf611952b9842568)   0xF0100003 |
| #define | [TEEC\_ERROR\_GENERIC](group__tee__interface.md#ga13c7ed6f37eba36870e4b138b661b61f)   0xFFFF0000 |
| #define | [TEEC\_ERROR\_ACCESS\_DENIED](group__tee__interface.md#gad7c7cd2ed537347d60276bd08375ca30)   0xFFFF0001 |
| #define | [TEEC\_ERROR\_CANCEL](group__tee__interface.md#ga8cbe25a679add519a048c85c03be1ede)   0xFFFF0002 |
| #define | [TEEC\_ERROR\_ACCESS\_CONFLICT](group__tee__interface.md#ga65a8bd0582ef42f84e85704bab5a85fe)   0xFFFF0003 |
| #define | [TEEC\_ERROR\_EXCESS\_DATA](group__tee__interface.md#gad8825a36962871ac2006386d18a821e7)   0xFFFF0004 |
| #define | [TEEC\_ERROR\_BAD\_FORMAT](group__tee__interface.md#ga0e08a22cf7abe05ae2d0cfd7fe92b0e7)   0xFFFF0005 |
| #define | [TEEC\_ERROR\_BAD\_PARAMETERS](group__tee__interface.md#ga79b607eb603bef58b3065a3014ee7117)   0xFFFF0006 |
| #define | [TEEC\_ERROR\_BAD\_STATE](group__tee__interface.md#ga19c6e3eb278dd58fa49b7de3dff8b7ac)   0xFFFF0007 |
| #define | [TEEC\_ERROR\_ITEM\_NOT\_FOUND](group__tee__interface.md#ga805299b26fda6bb38a97cf6a0825431d)   0xFFFF0008 |
| #define | [TEEC\_ERROR\_NOT\_IMPLEMENTED](group__tee__interface.md#gaa7ef60306699f14fa7f3bcd6ed744633)   0xFFFF0009 |
| #define | [TEEC\_ERROR\_NOT\_SUPPORTED](group__tee__interface.md#ga17041726bc43fb2a1aa3ddc927ac6cef)   0xFFFF000A |
| #define | [TEEC\_ERROR\_NO\_DATA](group__tee__interface.md#gaf515dfd970be2caf575be186dd32afd7)   0xFFFF000B |
| #define | [TEEC\_ERROR\_OUT\_OF\_MEMORY](group__tee__interface.md#gac7aaf1249147ecd63d6fba179e26ad33)   0xFFFF000C |
| #define | [TEEC\_ERROR\_BUSY](group__tee__interface.md#ga28d244820db7caa7cb829ed3469f5961)   0xFFFF000D |
| #define | [TEEC\_ERROR\_COMMUNICATION](group__tee__interface.md#ga0a3047b67556c437e80c308853705de2)   0xFFFF000E |
| #define | [TEEC\_ERROR\_SECURITY](group__tee__interface.md#gaae2b6bb8d476d422f782e7ac226de21b)   0xFFFF000F |
| #define | [TEEC\_ERROR\_SHORT\_BUFFER](group__tee__interface.md#ga511a0747fab1c307a5263a07ce396962)   0xFFFF0010 |
| #define | [TEEC\_ERROR\_EXTERNAL\_CANCEL](group__tee__interface.md#ga10e9a718e8ce09e6fe117bc0b002a3d6)   0xFFFF0011 |
| #define | [TEEC\_ERROR\_TARGET\_DEAD](group__tee__interface.md#ga6aa8da2d81b77fb8d2ec16f4e3a27528)   0xFFFF3024 |
| #define | [TEEC\_ERROR\_STORAGE\_NO\_SPACE](group__tee__interface.md#ga6229f84eb575bf10c14b40f02495b46e)   0xFFFF3041 |
| #define | [TEEC\_LOGIN\_PUBLIC](group__tee__interface.md#ga16baa8eb95393514c6035c957ad55a6b)   0x00000000 |
|  | Session login methods, for use in [tee\_open\_session()](group__tee__interface.md#gad7c66e32d5b02c42c698bd422cf43523 "Open session for Trusted Environment.") as parameter connectionMethod. |
| #define | [TEEC\_LOGIN\_USER](group__tee__interface.md#gab6940dd1f636aa67e74a8615e8544f85)   0x00000001 |
| #define | [TEEC\_LOGIN\_GROUP](group__tee__interface.md#ga8cdd4a2102e18a60d0624d610ef3619e)   0x00000002 |
| #define | [TEEC\_LOGIN\_APPLICATION](group__tee__interface.md#gae803496f14c6cc84b7f56174006c16a6)   0x00000004 |
| #define | [TEEC\_LOGIN\_USER\_APPLICATION](group__tee__interface.md#ga37fbb624e8c289d400cd69948bf8b505)   0x00000005 |
| #define | [TEEC\_LOGIN\_GROUP\_APPLICATION](group__tee__interface.md#gad1da184306fe0283fc1e618f829119e3)   0x00000006 |

| Typedefs | |
| --- | --- |
| typedef int(\* | [tee\_get\_version\_t](group__tee__interface.md#gac533d9e85d65857c0d984506024a55b4)) (const struct [device](structdevice.md) \*dev, struct [tee\_version\_info](structtee__version__info.md) \*info) |
|  | Callback API to get current tee version. |
| typedef int(\* | [tee\_open\_session\_t](group__tee__interface.md#gaf972199fcdbd892688dc141ddba6e6aa)) (const struct [device](structdevice.md) \*dev, struct [tee\_open\_session\_arg](structtee__open__session__arg.md) \*arg, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int num\_param, struct [tee\_param](structtee__param.md) \*param, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*session\_id) |
|  | Callback API to open session to Trusted Application. |
| typedef int(\* | [tee\_close\_session\_t](group__tee__interface.md#gac412f57a3da187e6e272857d5bdaaaeb)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) session\_id) |
|  | Callback API to close session to TA. |
| typedef int(\* | [tee\_cancel\_t](group__tee__interface.md#gad4cd5b65cac3eb7b4338fd99eeb13a93)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) session\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cancel\_id) |
|  | Callback API to cancel open session of invoke function to TA. |
| typedef int(\* | [tee\_invoke\_func\_t](group__tee__interface.md#gac3695e51dc8b08bb5e5c5d984c402b0e)) (const struct [device](structdevice.md) \*dev, struct [tee\_invoke\_func\_arg](structtee__invoke__func__arg.md) \*arg, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int num\_param, struct [tee\_param](structtee__param.md) \*param) |
|  | Callback API to invoke function to TA. |
| typedef int(\* | [tee\_shm\_register\_t](group__tee__interface.md#ga9e2807d34d580c012129a2fc1f5a425a)) (const struct [device](structdevice.md) \*dev, struct [tee\_shm](structtee__shm.md) \*shm) |
|  | Callback API to register shared memory. |
| typedef int(\* | [tee\_shm\_unregister\_t](group__tee__interface.md#ga2ea18e713a101a6ca715baa04c2f4185)) (const struct [device](structdevice.md) \*dev, struct [tee\_shm](structtee__shm.md) \*shm) |
|  | Callback API to unregister shared memory. |
| typedef int(\* | [tee\_suppl\_recv\_t](group__tee__interface.md#gaae68677cbff1e831fadc3d188c8588ff)) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*func, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int \*num\_params, struct [tee\_param](structtee__param.md) \*param) |
|  | Callback API to receive a request for TEE supplicant. |
| typedef int(\* | [tee\_suppl\_send\_t](group__tee__interface.md#ga3e8ec4e17ed48cb90bb0cbb1e9ddbb20)) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int ret, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int num\_params, struct [tee\_param](structtee__param.md) \*param) |
|  | Callback API to send a request for TEE supplicant. |

| Functions | |
| --- | --- |
| int | [tee\_get\_version](group__tee__interface.md#gadaaec6b6ea29d81f36943bbe5bcb305e) (const struct [device](structdevice.md) \*dev, struct [tee\_version\_info](structtee__version__info.md) \*info) |
|  | Get the current TEE version info. |
| int | [tee\_open\_session](group__tee__interface.md#gad7c66e32d5b02c42c698bd422cf43523) (const struct [device](structdevice.md) \*dev, struct [tee\_open\_session\_arg](structtee__open__session__arg.md) \*arg, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int num\_param, struct [tee\_param](structtee__param.md) \*param, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*session\_id) |
|  | Open session for Trusted Environment. |
| int | [tee\_close\_session](group__tee__interface.md#gacb1d58002378a11d92361a149d451241) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) session\_id) |
|  | Close session for Trusted Environment. |
| int | [tee\_cancel](group__tee__interface.md#ga34fbbfe48a07541041ffddb9e318332a) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) session\_id, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cancel\_id) |
|  | Cancel session or invoke function for Trusted Environment. |
| int | [tee\_invoke\_func](group__tee__interface.md#gae1337f293febcecc7dbc79ac064e7824) (const struct [device](structdevice.md) \*dev, struct [tee\_invoke\_func\_arg](structtee__invoke__func__arg.md) \*arg, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int num\_param, struct [tee\_param](structtee__param.md) \*param) |
|  | Invoke function for Trusted Environment Application. |
| int | [tee\_add\_shm](group__tee__interface.md#gade7fdbece8b0bd47f5d148572016c4ef) (const struct [device](structdevice.md) \*dev, void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) align, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct [tee\_shm](structtee__shm.md) \*\*shmp) |
|  | Helper function to allocate and register shared memory. |
| int | [tee\_rm\_shm](group__tee__interface.md#gaf53521a3e3a36a9827753716bef1434f) (const struct [device](structdevice.md) \*dev, struct [tee\_shm](structtee__shm.md) \*shm) |
|  | Helper function to remove and unregister shared memory. |
| int | [tee\_shm\_register](group__tee__interface.md#ga1565c23104792203ede9d9cb388ff782) (const struct [device](structdevice.md) \*dev, void \*addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct [tee\_shm](structtee__shm.md) \*\*shm) |
|  | Register shared memory for Trusted Environment. |
| int | [tee\_shm\_unregister](group__tee__interface.md#gade2c0e7d89e3594707637b62a1901bac) (const struct [device](structdevice.md) \*dev, struct [tee\_shm](structtee__shm.md) \*shm) |
|  | Unregister shared memory for Trusted Environment. |
| int | [tee\_shm\_alloc](group__tee__interface.md#ga47f7403e2b136f755432159c7bd679a5) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), struct [tee\_shm](structtee__shm.md) \*\*shm) |
|  | Allocate shared memory region for Trusted Environment. |
| int | [tee\_shm\_free](group__tee__interface.md#ga346d8d67a18542c097f1254c0ace8726) (const struct [device](structdevice.md) \*dev, struct [tee\_shm](structtee__shm.md) \*shm) |
|  | Free shared memory region for Trusted Environment. |
| int | [tee\_suppl\_recv](group__tee__interface.md#ga2213f63da1f080beaedc169e13531a37) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*func, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int \*num\_params, struct [tee\_param](structtee__param.md) \*param) |
|  | Receive a request for TEE Supplicant. |
| int | [tee\_suppl\_send](group__tee__interface.md#ga93cccfa446983be704f364760bf7567b) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int ret, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int num\_params, struct [tee\_param](structtee__param.md) \*param) |
|  | Send a request for TEE Supplicant function. |

## Detailed Description

Public APIs for the tee driver.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [tee.h](tee_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
