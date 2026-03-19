---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/mgmt_2mcumgr_2transport_2smp_8h.html
original_path: doxygen/html/mgmt_2mcumgr_2transport_2smp_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smp.h File Reference

`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](mgmt_2mcumgr_2transport_2smp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [smp\_transport\_api\_t](structsmp__transport__api__t.md) |
|  | Function pointers of SMP transport functions, if a handler is NULL then it is not supported/implemented. [More...](structsmp__transport__api__t.md#details) |
| struct | [smp\_transport](structsmp__transport.md) |
|  | SMP transport object for sending SMP responses. [More...](structsmp__transport.md#details) |
| struct | [smp\_client\_transport\_entry](structsmp__client__transport__entry.md) |
|  | SMP Client transport structure. [More...](structsmp__client__transport__entry.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [smp\_transport\_out\_fn](group__mcumgr__transport__smp.md#ga4da3579b031ba6a90448ad9248f52155)) (struct [net\_buf](structnet__buf.md) \*nb) |
|  | SMP transmit callback for transport. |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)(\* | [smp\_transport\_get\_mtu\_fn](group__mcumgr__transport__smp.md#ga2085e89b99428a61596d90e084d7c5e2)) (const struct [net\_buf](structnet__buf.md) \*nb) |
|  | SMP MTU query callback for transport. |
| typedef int(\* | [smp\_transport\_ud\_copy\_fn](group__mcumgr__transport__smp.md#ga840da7e00d590459b656dcbe0dd6f6f4)) (struct [net\_buf](structnet__buf.md) \*dst, const struct [net\_buf](structnet__buf.md) \*src) |
|  | SMP copy user\_data callback. |
| typedef void(\* | [smp\_transport\_ud\_free\_fn](group__mcumgr__transport__smp.md#ga0f249aa3fed3044d9bad811e92e4135c)) (void \*ud) |
|  | SMP free user\_data callback. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [smp\_transport\_query\_valid\_check\_fn](group__mcumgr__transport__smp.md#ga77d54c0bd6afc69f73613575b671e089)) (struct [net\_buf](structnet__buf.md) \*nb, void \*arg) |
|  | Function for checking if queued data is still valid. |

| Enumerations | |
| --- | --- |
| enum | [smp\_transport\_type](group__mcumgr__transport__smp.md#ga5d886a11df0c49ca18e23e246ab2fab9) {     [SMP\_SERIAL\_TRANSPORT](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9ab1660bb2a08be903905358e410761342) = 0 , [SMP\_BLUETOOTH\_TRANSPORT](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9a952714e2058663eb43695a9a3b65dcbe) , [SMP\_SHELL\_TRANSPORT](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9a71731051dadd60e06afe426da4ed7b43) , [SMP\_UDP\_IPV4\_TRANSPORT](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9adc8f1680bea910f7daaf191f3f07b74f) ,     [SMP\_UDP\_IPV6\_TRANSPORT](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9a1fbca254a684aac8d15c8b067aa994f7) , [SMP\_LORAWAN\_TRANSPORT](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9addcf3d287f359bad85104d2a37b4e5c8) , [SMP\_USER\_DEFINED\_TRANSPORT](group__mcumgr__transport__smp.md#gga5d886a11df0c49ca18e23e246ab2fab9aa25faa37d758689aa33a3c7d1320b863)   } |
|  | SMP transport type for client registration. [More...](group__mcumgr__transport__smp.md#ga5d886a11df0c49ca18e23e246ab2fab9) |

| Functions | |
| --- | --- |
| int | [smp\_transport\_init](group__mcumgr__transport__smp.md#gaf275034765327b52b900046d71c411ee) (struct [smp\_transport](structsmp__transport.md) \*smpt) |
|  | Initializes a Zephyr SMP transport object. |
| void | [smp\_rx\_remove\_invalid](group__mcumgr__transport__smp.md#ga87ccc623b5907d7d65b24ed99bd57ec5) (struct [smp\_transport](structsmp__transport.md) \*zst, void \*arg) |
|  | Used to remove queued requests for an SMP transport that are no longer valid. |
| void | [smp\_rx\_clear](group__mcumgr__transport__smp.md#ga662f893037193923610de1e8793fd971) (struct [smp\_transport](structsmp__transport.md) \*zst) |
|  | Used to clear pending queued requests for an SMP transport. |
| void | [smp\_client\_transport\_register](group__mcumgr__transport__smp.md#gafb488cd9854b74c8e5802db3c8fe6116) (struct [smp\_client\_transport\_entry](structsmp__client__transport__entry.md) \*entry) |
|  | Register a Zephyr SMP transport object for client. |
| struct [smp\_transport](structsmp__transport.md) \* | [smp\_client\_transport\_get](group__mcumgr__transport__smp.md#ga67c3481cdc81c20e0c35b4eaa185619e) (int smpt\_type) |
|  | Discover a registered SMP transport client object. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [transport](dir_9a3f12841ae237fd7345c80156d89ad0.md)
- [smp.h](mgmt_2mcumgr_2transport_2smp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
