---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/public_2domctl_8h.html
original_path: doxygen/html/public_2domctl_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

domctl.h File Reference

`#include "[xen.h](xen_8h_source.md)"`  
`#include "[event_channel.h](event__channel_8h_source.md)"`  
`#include "[grant_table.h](grant__table_8h_source.md)"`  
`#include "[memory.h](public_2memory_8h_source.md)"`

[Go to the source code of this file.](public_2domctl_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [xen\_domctl\_createdomain](structxen__domctl__createdomain.md) |
| struct | [xen\_domctl\_getdomaininfo](structxen__domctl__getdomaininfo.md) |
| struct | [xen\_domctl\_shadow\_op\_stats](structxen__domctl__shadow__op__stats.md) |
| struct | [xen\_domctl\_shadow\_op](structxen__domctl__shadow__op.md) |
| struct | [xen\_domctl\_max\_mem](structxen__domctl__max__mem.md) |
| struct | [xen\_domctl\_vcpucontext](structxen__domctl__vcpucontext.md) |
| struct | [xen\_domctl\_max\_vcpus](structxen__domctl__max__vcpus.md) |
| struct | [xen\_domctl\_sched\_credit](structxen__domctl__sched__credit.md) |
| struct | [xen\_domctl\_sched\_credit2](structxen__domctl__sched__credit2.md) |
| struct | [xen\_domctl\_sched\_rtds](structxen__domctl__sched__rtds.md) |
| struct | [xen\_domctl\_schedparam\_vcpu](structxen__domctl__schedparam__vcpu.md) |
| struct | [xen\_domctl\_scheduler\_op](structxen__domctl__scheduler__op.md) |
| struct | [xen\_domctl\_iomem\_permission](structxen__domctl__iomem__permission.md) |
| struct | [xen\_domctl\_address\_size](structxen__domctl__address__size.md) |
| struct | [xen\_domctl\_assign\_device](structxen__domctl__assign__device.md) |
| struct | [xen\_domctl\_bind\_pt\_irq](structxen__domctl__bind__pt__irq.md) |
| struct | [xen\_domctl\_memory\_mapping](structxen__domctl__memory__mapping.md) |
| struct | [xen\_domctl\_cacheflush](structxen__domctl__cacheflush.md) |
| struct | [xen\_domctl\_paging\_mempool](structxen__domctl__paging__mempool.md) |
| struct | [xen\_domctl](structxen__domctl.md) |

| Macros | |
| --- | --- |
| #define | [XEN\_DOMCTL\_INTERFACE\_VERSION](#a1af9bebb704ccbf97d9ec79d3d860f58)   0x00000015 |
| #define | [XEN\_DOMCTL\_CDF\_hvm](#a260a9fbe6b758ec5db7e45209cd7dafb)   (1U << \_XEN\_DOMCTL\_CDF\_hvm) |
| #define | [XEN\_DOMCTL\_CDF\_hap](#a0850c8d7219c2ae8b1de1a2fab67886a)   (1U << \_XEN\_DOMCTL\_CDF\_hap) |
| #define | [XEN\_DOMCTL\_CDF\_s3\_integrity](#a42dd8479fcf148340790bdd3904e421e)   (1U << \_XEN\_DOMCTL\_CDF\_s3\_integrity) |
| #define | [XEN\_DOMCTL\_CDF\_oos\_off](#a4620d4dbc1f5334d4cf2c30edf3904f3)   (1U << \_XEN\_DOMCTL\_CDF\_oos\_off) |
| #define | [XEN\_DOMCTL\_CDF\_xs\_domain](#aa70feb5d0e5ee56f872fd0e497557b0d)   (1U << \_XEN\_DOMCTL\_CDF\_xs\_domain) |
| #define | [XEN\_DOMCTL\_CDF\_iommu](#a5562e6d41cdea2b7bdd4a5b0b7035109)   (1U << \_XEN\_DOMCTL\_CDF\_iommu) |
| #define | [XEN\_DOMCTL\_CDF\_nested\_virt](#aa837725af35d2c855080e4c413904457)   (1U << \_XEN\_DOMCTL\_CDF\_nested\_virt) |
| #define | [XEN\_DOMCTL\_CDF\_vpmu](#a7e9c55587080d25fdf1d6fc31030d27f)   (1U << 7) |
| #define | [XEN\_DOMCTL\_CDF\_MAX](#a7c6f925fdeb64bc84c6e5f18965b4d13)   [XEN\_DOMCTL\_CDF\_vpmu](#a7e9c55587080d25fdf1d6fc31030d27f) |
| #define | [XEN\_DOMCTL\_IOMMU\_no\_sharep](#a928664472460bf3656889afe3a381389)   (1U << \_XEN\_DOMCTL\_IOMMU\_no\_sharept) |
| #define | [XEN\_DOMCTL\_IOMMU\_MAX](#ab2313d4fcb94c8e6473d67ce9607da48)   XEN\_DOMCTL\_IOMMU\_no\_sharept |
| #define | [XEN\_DOMCTL\_GRANT\_version\_mask](#a6f5be8cef355d7bad22785dc29bd4dac)   0xf |
| #define | [XEN\_DOMCTL\_GRANT\_version](#aa38abb4809db00cbe963bcb41d61950a)(v) |
| #define | [XEN\_DOMINF\_dying](#afcdfc193f40faf980e2e23d485de4e79)   (1U << \_XEN\_DOMINF\_dying) |
| #define | [XEN\_DOMINF\_hvm\_guest](#a140d5075193daeba92f4b83a0c2f1e14)   (1U << \_XEN\_DOMINF\_hvm\_guest) |
| #define | [XEN\_DOMINF\_shutdown](#af49f7e9e048fafaa4ec004d46919d313)   (1U << \_XEN\_DOMINF\_shutdown) |
| #define | [XEN\_DOMINF\_paused](#a32c611154d6e6bb3c3b5d4ac9cab5e65)   (1U << \_XEN\_DOMINF\_paused) |
| #define | [XEN\_DOMINF\_blocked](#a34e24b31aaadfd78c585a6187fc89187)   (1U << \_XEN\_DOMINF\_blocked) |
| #define | [XEN\_DOMINF\_running](#a7e0f50072c881ded1670fa4efda493e0)   (1U << \_XEN\_DOMINF\_running) |
| #define | [XEN\_DOMINF\_debugged](#ade451ebb63161b5cdbfab6221cb9c4f0)   (1U << \_XEN\_DOMINF\_debugged) |
| #define | [XEN\_DOMINF\_xs\_domain](#a37e263699b64912d80697a374d127796)   (1U << \_XEN\_DOMINF\_xs\_domain) |
| #define | [XEN\_DOMINF\_hap](#a919137e7b6b084d368cca8766091754e)   (1U << \_XEN\_DOMINF\_hap) |
| #define | [XEN\_DOMINF\_shutdownmask](#a8e242d887ef91743672a2a3ae3bd74f2)   255 |
| #define | [XEN\_DOMINF\_shutdownshift](#af3cfe05618c9a1bd3dbe48f42e7cea04)   16 |
| #define | [XEN\_INVALID\_MAX\_VCPU\_ID](#a40c471099d055910f5bed2994efec643)   (~0U) /\* Domain has no vcpus? \*/ |
| #define | [XEN\_DOMCTL\_SHADOW\_OP\_GET\_ALLOCATION](#ae4aefb0671418197673fc3055b3e1aa0)   30 |
| #define | [XEN\_DOMCTL\_SHADOW\_OP\_SET\_ALLOCATION](#ad48421566046507c9773c91e0349e77b)   31 |
| #define | [XEN\_SCHEDULER\_CREDIT](#afee5561bd17af9ddba71e01697ee50d3)   5 |
| #define | [XEN\_SCHEDULER\_CREDIT2](#a560830bf6e1c6a96fae85d6788fffc7c)   6 |
| #define | [XEN\_SCHEDULER\_ARINC653](#a08dbd46725afbad5fe54879c9d0518c1)   7 |
| #define | [XEN\_SCHEDULER\_RTDS](#afaede03296414e2adaeed009bfd4d0e0)   8 |
| #define | [XEN\_SCHEDULER\_NULL](#ac0f58da75c220a8afef88585628874f2)   9 |
| #define | [XEN\_DOMCTL\_SCHEDRT\_extra](#ae765249383b5fc2e83d1474ac49b4fbd)   (1U<<\_XEN\_DOMCTL\_SCHEDRT\_extra) |
| #define | [XEN\_DOMCTL\_SCHEDOP\_putinfo](#a82c49a3fe9250e1e9f3cc4d5f5a74dee)   0 |
| #define | [XEN\_DOMCTL\_SCHEDOP\_getinfo](#a481dbdc86321a9f74ef259fad8d3da08)   1 |
| #define | [XEN\_DOMCTL\_SCHEDOP\_putvcpuinfo](#a6d6e95c97391261ef77dfbccf15de5ba)   2 |
| #define | [XEN\_DOMCTL\_SCHEDOP\_getvcpuinfo](#ad1db496f608988bae2fe8ef992416d9e)   3 |
| #define | [XEN\_DOMCTL\_DEV\_PCI](#a1399012c484a27f9ada6f35688d569d6)   0 |
| #define | [XEN\_DOMCTL\_DEV\_DT](#ac6ed84f27459969a769f558297cee32d)   1 |
| #define | [XEN\_DOMCTL\_DEV\_RDM\_RELAXED](#ab297d1aaab40b76132199166663b305b)   1 /\* assign only \*/ |
| #define | [XEN\_DOMCTL\_VMSI\_X86\_DEST\_ID\_MASK](#ad94911a72ecc25f10b2a58bd3c1fc091)   0x0000ff |
| #define | [XEN\_DOMCTL\_VMSI\_X86\_RH\_MASK](#ad337d528c4d9eb777d7dd1a438a98dc8)   0x000100 |
| #define | [XEN\_DOMCTL\_VMSI\_X86\_DM\_MASK](#a2377d6a66411ba1ca2a314965ef8c7be)   0x000200 |
| #define | [XEN\_DOMCTL\_VMSI\_X86\_DELIV\_MASK](#ac8d90b0cceefc508e8a56e59d4fa5ce3)   0x007000 |
| #define | [XEN\_DOMCTL\_VMSI\_X86\_TRIG\_MASK](#a5ca26c5c2b596e10104119d44b8c6f9a)   0x008000 |
| #define | [XEN\_DOMCTL\_VMSI\_X86\_UNMASKED](#a81cec14a8ea2e245bc664647e0bf70ab)   0x010000 |
| #define | [DPCI\_ADD\_MAPPING](#ab137fda9547e636f2a3685a3b88e9f01)   1 |
| #define | [DPCI\_REMOVE\_MAPPING](#a88012336e215a1710a575655f4d2b368)   0 |
| #define | [XEN\_DOMCTL\_createdomain](#abacb0e860ee863ddfeabbdd14b024fc0)   1 |
| #define | [XEN\_DOMCTL\_destroydomain](#a6c9f26d2531a20bffce112302be5196f)   2 |
| #define | [XEN\_DOMCTL\_pausedomain](#a6fc2629c1e6c4e882609e7e0e8214af7)   3 |
| #define | [XEN\_DOMCTL\_unpausedomain](#a7f759b8eba89d5387e880f8aca7fd357)   4 |
| #define | [XEN\_DOMCTL\_getdomaininfo](#add13342f48d90679c9eb941834278cce)   5 |
| #define | [XEN\_DOMCTL\_setvcpuaffinity](#a52f4ddee28622818b0d0ad3a660782e4)   9 |
| #define | [XEN\_DOMCTL\_shadow\_op](#ab310ee5729b47d317fb381ba4a7765b9)   10 |
| #define | [XEN\_DOMCTL\_max\_mem](#abc8af7f11bc93e5e335bda2ba00e770a)   11 |
| #define | [XEN\_DOMCTL\_setvcpucontext](#a8fff7d4989f605f73dec55d59b10f5db)   12 |
| #define | [XEN\_DOMCTL\_getvcpucontext](#af99e2f5c9a5b8a3ccd35a19961c0aa44)   13 |
| #define | [XEN\_DOMCTL\_getvcpuinfo](#abff3d223bd31c6f9b888c1293d7eaeca)   14 |
| #define | [XEN\_DOMCTL\_max\_vcpus](#ad32b3ac435a726f6eec3baa03e9d2cc6)   15 |
| #define | [XEN\_DOMCTL\_scheduler\_op](#a4e16878f8f098d4e5033b3d9c7c4fc66)   16 |
| #define | [XEN\_DOMCTL\_setdomainhandle](#aab5cf53258ae8b11262e5f1b288537f7)   17 |
| #define | [XEN\_DOMCTL\_setdebugging](#a74047cd87a9608188c8412712f43d2f5)   18 |
| #define | [XEN\_DOMCTL\_irq\_permission](#ab350564800ede51e81bd1efbe9d31433)   19 |
| #define | [XEN\_DOMCTL\_iomem\_permission](#ad3775642e389867857b9c7d33922deaf)   20 |
| #define | [XEN\_DOMCTL\_ioport\_permission](#ab00adfd7a0a99504c0d74fb9a730535e)   21 |
| #define | [XEN\_DOMCTL\_hypercall\_init](#a131e1409d1d50a9ba638b194430fd63e)   22 |
| #define | [XEN\_DOMCTL\_settimeoffset](#a4d75d1a4982ead6f6b2066d562f3137b)   24 |
| #define | [XEN\_DOMCTL\_getvcpuaffinity](#acd429b8834dc7284b33a66949c5b7ad0)   25 |
| #define | [XEN\_DOMCTL\_real\_mode\_area](#afb2feb24f3113dc5b924aaddf9095c10)   26 /\* Obsolete PPC only \*/ |
| #define | [XEN\_DOMCTL\_resumedomain](#aca08972618f6a931a3dffd924072e7f0)   27 |
| #define | [XEN\_DOMCTL\_sendtrigger](#a3f3aef1714b0d856bafe713ee9a0a096)   28 |
| #define | [XEN\_DOMCTL\_subscribe](#a25286953a431e6f3172ef9a5f90d18e4)   29 |
| #define | [XEN\_DOMCTL\_gethvmcontext](#a985b6a69f7cb7da875026aed4552aa6a)   33 |
| #define | [XEN\_DOMCTL\_sethvmcontext](#a6ea99b9477c9e698af222cea8eef8103)   34 |
| #define | [XEN\_DOMCTL\_set\_address\_size](#a3401578b5bb89676a5c5c2be96424ad7)   35 |
| #define | [XEN\_DOMCTL\_get\_address\_size](#a6d97e86f699b92655c72c182b82f1594)   36 |
| #define | [XEN\_DOMCTL\_assign\_device](#a5c896cf694ada3f5571e2011fbeb2cdc)   37 |
| #define | [XEN\_DOMCTL\_bind\_pt\_irq](#ac21ffc09b097b8a422680c72242c8019)   38 |
| #define | [XEN\_DOMCTL\_memory\_mapping](#a087034256c26c23fe8aa430224ed4f5e)   39 |
| #define | [XEN\_DOMCTL\_ioport\_mapping](#a8dc90189fb09c0500ab9831a7304258b)   40 |
| #define | [XEN\_DOMCTL\_set\_ext\_vcpucontext](#a0d0a882796436312ecede3dcfd9569f3)   42 |
| #define | [XEN\_DOMCTL\_get\_ext\_vcpucontext](#a9f0000d1c3ea8784f2d7ac91ee086243)   43 |
| #define | [XEN\_DOMCTL\_set\_opt\_feature](#adde0cd9f0afc1545bce1e7efe257479b)   44 /\* Obsolete IA64 only \*/ |
| #define | [XEN\_DOMCTL\_test\_assign\_device](#a71b8b60fc4a387b89b482f7c0ba6a24f)   45 |
| #define | [XEN\_DOMCTL\_set\_target](#a80d963c7a959b9116b27918bb19cce6b)   46 |
| #define | [XEN\_DOMCTL\_deassign\_device](#abc323304cdd608bf785af6421b05f3ee)   47 |
| #define | [XEN\_DOMCTL\_unbind\_pt\_irq](#a4a5a18f97beae00c8df5a27e8f58630b)   48 |
| #define | [XEN\_DOMCTL\_get\_device\_group](#a93ab2e12792f16f249bec06a31bcde29)   50 |
| #define | [XEN\_DOMCTL\_debug\_op](#ab86f756fc6cfcb537497de0745b75e53)   54 |
| #define | [XEN\_DOMCTL\_gethvmcontext\_partial](#a72b7300f5aeeba20c7cd3c3aba88e243)   55 |
| #define | [XEN\_DOMCTL\_vm\_event\_op](#a584b0146d9466c742cde954cf933a35e)   56 |
| #define | [XEN\_DOMCTL\_mem\_sharing\_op](#a2144e180680f2862fb3c5c4242ab81d1)   57 |
| #define | [XEN\_DOMCTL\_gettscinfo](#ac0c8fe09ca02e3d19ffa2253ec56c36a)   59 |
| #define | [XEN\_DOMCTL\_settscinfo](#a68f376046c9512b1ba0d536bf9f4da59)   60 |
| #define | [XEN\_DOMCTL\_getpageframeinfo3](#a9e543639c3b1bae35b54ca0e3ae18fcd)   61 |
| #define | [XEN\_DOMCTL\_setvcpuextstate](#a95967323209e42eaf73b092c76c1ed8f)   62 |
| #define | [XEN\_DOMCTL\_getvcpuextstate](#a20fcaf2b9a50516154f6664ecaba4310)   63 |
| #define | [XEN\_DOMCTL\_set\_access\_required](#a8e63ecac1fe62447de02590d81454c76)   64 |
| #define | [XEN\_DOMCTL\_audit\_p2m](#a64f85814d96a31362cca48e2220047ad)   65 |
| #define | [XEN\_DOMCTL\_set\_virq\_handler](#a3f56b7bdb2efe676716dca9a8303b502)   66 |
| #define | [XEN\_DOMCTL\_set\_broken\_page\_p2m](#af50563ae8af88f9de94f87986147f532)   67 |
| #define | [XEN\_DOMCTL\_setnodeaffinity](#a64def50fd26a62692718f14d34ac5056)   68 |
| #define | [XEN\_DOMCTL\_getnodeaffinity](#afcf17d5e7402b39f32b6c7e21bcb0caa)   69 |
| #define | [XEN\_DOMCTL\_cacheflush](#a7385beae0c2a015166962952029fafc9)   71 |
| #define | [XEN\_DOMCTL\_get\_vcpu\_msrs](#a154eebe2a910f858f89599f1facda875)   72 |
| #define | [XEN\_DOMCTL\_set\_vcpu\_msrs](#aa5227f853fed668e20d3c15a76278c1c)   73 |
| #define | [XEN\_DOMCTL\_setvnumainfo](#a33454734fa5e0f67818f763c0284bd0b)   74 |
| #define | [XEN\_DOMCTL\_psr\_cmt\_op](#ac27bce86ab62c437f2338a96f37a7d48)   75 |
| #define | [XEN\_DOMCTL\_monitor\_op](#af006015d33d0097664f6a6020873a82c)   77 |
| #define | [XEN\_DOMCTL\_psr\_alloc](#aad00fc3c420bef96edac0233ee94cd47)   78 |
| #define | [XEN\_DOMCTL\_soft\_reset](#aa33f73f1dda376298e235892d8322ba6)   79 |
| #define | [XEN\_DOMCTL\_vuart\_op](#a850fc8c65f70ad1ad1c9d000f94960ff)   81 |
| #define | [XEN\_DOMCTL\_get\_cpu\_policy](#a36432a25f78249e84192ca30f3b9e9e9)   82 |
| #define | [XEN\_DOMCTL\_set\_cpu\_policy](#ad537d2de47beed8d6f670a863a3d44d2)   83 |
| #define | [XEN\_DOMCTL\_vmtrace\_op](#a9794dd91afdd16869e3a42b6b3239ecd)   84 |
| #define | [XEN\_DOMCTL\_get\_paging\_mempool\_size](#a5cb0f5cd9e12260b996f7bd1df0ca4f0)   85 |
| #define | [XEN\_DOMCTL\_set\_paging\_mempool\_size](#ae35c3b2ead7567f169e79e786d2b915f)   86 |
| #define | [XEN\_DOMCTL\_gdbsx\_guestmemio](#a1202be0a9604f52b50539e5f44af9c39)   1000 |
| #define | [XEN\_DOMCTL\_gdbsx\_pausevcpu](#a398802362361a5fc1496baaa4b2f3664)   1001 |
| #define | [XEN\_DOMCTL\_gdbsx\_unpausevcpu](#a5edc650c7f3956bf6e1dfb441b393a83)   1002 |
| #define | [XEN\_DOMCTL\_gdbsx\_domstatus](#ac97072e148e5951b57ec0e730e621d29)   1003 |

| Typedefs | |
| --- | --- |
| typedef struct [xen\_domctl\_getdomaininfo](structxen__domctl__getdomaininfo.md) | [xen\_domctl\_getdomaininfo\_t](#a975bbf787336d78a2fe063f5f16766db) |
| typedef struct [xen\_domctl\_schedparam\_vcpu](structxen__domctl__schedparam__vcpu.md) | [xen\_domctl\_schedparam\_vcpu\_t](#adfbd6c6d40e27f06e00d39acd5be271e) |
| typedef struct [xen\_domctl](structxen__domctl.md) | [xen\_domctl\_t](#a739ed8d92302fb02b53f4f769d57d83e) |

| Enumerations | |
| --- | --- |
| enum | [pt\_irq\_type](#aa0ba08b170800d6d7723b694525ade07) {     [PT\_IRQ\_TYPE\_PCI](#aa0ba08b170800d6d7723b694525ade07a243f287f1e887559dad46c487d30dfb7) , [PT\_IRQ\_TYPE\_ISA](#aa0ba08b170800d6d7723b694525ade07a46633da322cceb9716d497db0a6c7684) , [PT\_IRQ\_TYPE\_MSI](#aa0ba08b170800d6d7723b694525ade07a378f677ce6b550e1f2dd1ce7e4a1cefb) , [PT\_IRQ\_TYPE\_MSI\_TRANSLATE](#aa0ba08b170800d6d7723b694525ade07ad8c9df22103d8549d00e3da9c0e3a607) ,     [PT\_IRQ\_TYPE\_SPI](#aa0ba08b170800d6d7723b694525ade07a55314f6bde5f058264c442506b23a818)   } |

| Functions | |
| --- | --- |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#a4e3858932ea51b98f6594ec863305eaa) ([xen\_domctl\_getdomaininfo\_t](#a975bbf787336d78a2fe063f5f16766db)) |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#a4bff168adfcb0ee8cc56f22a1b468112) ([xen\_domctl\_schedparam\_vcpu\_t](#adfbd6c6d40e27f06e00d39acd5be271e)) |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#a0d3b8859d3644f60cb1753391b03face) ([xen\_domctl\_t](#a739ed8d92302fb02b53f4f769d57d83e)) |

## Macro Definition Documentation

## [◆ ](#ab137fda9547e636f2a3685a3b88e9f01)DPCI\_ADD\_MAPPING

| #define DPCI\_ADD\_MAPPING   1 |
| --- |

## [◆ ](#a88012336e215a1710a575655f4d2b368)DPCI\_REMOVE\_MAPPING

| #define DPCI\_REMOVE\_MAPPING   0 |
| --- |

## [◆ ](#a5c896cf694ada3f5571e2011fbeb2cdc)XEN\_DOMCTL\_assign\_device

| #define XEN\_DOMCTL\_assign\_device   37 |
| --- |

## [◆ ](#a64f85814d96a31362cca48e2220047ad)XEN\_DOMCTL\_audit\_p2m

| #define XEN\_DOMCTL\_audit\_p2m   65 |
| --- |

## [◆ ](#ac21ffc09b097b8a422680c72242c8019)XEN\_DOMCTL\_bind\_pt\_irq

| #define XEN\_DOMCTL\_bind\_pt\_irq   38 |
| --- |

## [◆ ](#a7385beae0c2a015166962952029fafc9)XEN\_DOMCTL\_cacheflush

| #define XEN\_DOMCTL\_cacheflush   71 |
| --- |

## [◆ ](#a0850c8d7219c2ae8b1de1a2fab67886a)XEN\_DOMCTL\_CDF\_hap

| #define XEN\_DOMCTL\_CDF\_hap   (1U << \_XEN\_DOMCTL\_CDF\_hap) |
| --- |

## [◆ ](#a260a9fbe6b758ec5db7e45209cd7dafb)XEN\_DOMCTL\_CDF\_hvm

| #define XEN\_DOMCTL\_CDF\_hvm   (1U << \_XEN\_DOMCTL\_CDF\_hvm) |
| --- |

## [◆ ](#a5562e6d41cdea2b7bdd4a5b0b7035109)XEN\_DOMCTL\_CDF\_iommu

| #define XEN\_DOMCTL\_CDF\_iommu   (1U << \_XEN\_DOMCTL\_CDF\_iommu) |
| --- |

## [◆ ](#a7c6f925fdeb64bc84c6e5f18965b4d13)XEN\_DOMCTL\_CDF\_MAX

| #define XEN\_DOMCTL\_CDF\_MAX   [XEN\_DOMCTL\_CDF\_vpmu](#a7e9c55587080d25fdf1d6fc31030d27f) |
| --- |

## [◆ ](#aa837725af35d2c855080e4c413904457)XEN\_DOMCTL\_CDF\_nested\_virt

| #define XEN\_DOMCTL\_CDF\_nested\_virt   (1U << \_XEN\_DOMCTL\_CDF\_nested\_virt) |
| --- |

## [◆ ](#a4620d4dbc1f5334d4cf2c30edf3904f3)XEN\_DOMCTL\_CDF\_oos\_off

| #define XEN\_DOMCTL\_CDF\_oos\_off   (1U << \_XEN\_DOMCTL\_CDF\_oos\_off) |
| --- |

## [◆ ](#a42dd8479fcf148340790bdd3904e421e)XEN\_DOMCTL\_CDF\_s3\_integrity

| #define XEN\_DOMCTL\_CDF\_s3\_integrity   (1U << \_XEN\_DOMCTL\_CDF\_s3\_integrity) |
| --- |

## [◆ ](#a7e9c55587080d25fdf1d6fc31030d27f)XEN\_DOMCTL\_CDF\_vpmu

| #define XEN\_DOMCTL\_CDF\_vpmu   (1U << 7) |
| --- |

## [◆ ](#aa70feb5d0e5ee56f872fd0e497557b0d)XEN\_DOMCTL\_CDF\_xs\_domain

| #define XEN\_DOMCTL\_CDF\_xs\_domain   (1U << \_XEN\_DOMCTL\_CDF\_xs\_domain) |
| --- |

## [◆ ](#abacb0e860ee863ddfeabbdd14b024fc0)XEN\_DOMCTL\_createdomain

| #define XEN\_DOMCTL\_createdomain   1 |
| --- |

## [◆ ](#abc323304cdd608bf785af6421b05f3ee)XEN\_DOMCTL\_deassign\_device

| #define XEN\_DOMCTL\_deassign\_device   47 |
| --- |

## [◆ ](#ab86f756fc6cfcb537497de0745b75e53)XEN\_DOMCTL\_debug\_op

| #define XEN\_DOMCTL\_debug\_op   54 |
| --- |

## [◆ ](#a6c9f26d2531a20bffce112302be5196f)XEN\_DOMCTL\_destroydomain

| #define XEN\_DOMCTL\_destroydomain   2 |
| --- |

## [◆ ](#ac6ed84f27459969a769f558297cee32d)XEN\_DOMCTL\_DEV\_DT

| #define XEN\_DOMCTL\_DEV\_DT   1 |
| --- |

## [◆ ](#a1399012c484a27f9ada6f35688d569d6)XEN\_DOMCTL\_DEV\_PCI

| #define XEN\_DOMCTL\_DEV\_PCI   0 |
| --- |

## [◆ ](#ab297d1aaab40b76132199166663b305b)XEN\_DOMCTL\_DEV\_RDM\_RELAXED

| #define XEN\_DOMCTL\_DEV\_RDM\_RELAXED   1 /\* assign only \*/ |
| --- |

## [◆ ](#ac97072e148e5951b57ec0e730e621d29)XEN\_DOMCTL\_gdbsx\_domstatus

| #define XEN\_DOMCTL\_gdbsx\_domstatus   1003 |
| --- |

## [◆ ](#a1202be0a9604f52b50539e5f44af9c39)XEN\_DOMCTL\_gdbsx\_guestmemio

| #define XEN\_DOMCTL\_gdbsx\_guestmemio   1000 |
| --- |

## [◆ ](#a398802362361a5fc1496baaa4b2f3664)XEN\_DOMCTL\_gdbsx\_pausevcpu

| #define XEN\_DOMCTL\_gdbsx\_pausevcpu   1001 |
| --- |

## [◆ ](#a5edc650c7f3956bf6e1dfb441b393a83)XEN\_DOMCTL\_gdbsx\_unpausevcpu

| #define XEN\_DOMCTL\_gdbsx\_unpausevcpu   1002 |
| --- |

## [◆ ](#a6d97e86f699b92655c72c182b82f1594)XEN\_DOMCTL\_get\_address\_size

| #define XEN\_DOMCTL\_get\_address\_size   36 |
| --- |

## [◆ ](#a36432a25f78249e84192ca30f3b9e9e9)XEN\_DOMCTL\_get\_cpu\_policy

| #define XEN\_DOMCTL\_get\_cpu\_policy   82 |
| --- |

## [◆ ](#a93ab2e12792f16f249bec06a31bcde29)XEN\_DOMCTL\_get\_device\_group

| #define XEN\_DOMCTL\_get\_device\_group   50 |
| --- |

## [◆ ](#a9f0000d1c3ea8784f2d7ac91ee086243)XEN\_DOMCTL\_get\_ext\_vcpucontext

| #define XEN\_DOMCTL\_get\_ext\_vcpucontext   43 |
| --- |

## [◆ ](#a5cb0f5cd9e12260b996f7bd1df0ca4f0)XEN\_DOMCTL\_get\_paging\_mempool\_size

| #define XEN\_DOMCTL\_get\_paging\_mempool\_size   85 |
| --- |

## [◆ ](#a154eebe2a910f858f89599f1facda875)XEN\_DOMCTL\_get\_vcpu\_msrs

| #define XEN\_DOMCTL\_get\_vcpu\_msrs   72 |
| --- |

## [◆ ](#add13342f48d90679c9eb941834278cce)XEN\_DOMCTL\_getdomaininfo

| #define XEN\_DOMCTL\_getdomaininfo   5 |
| --- |

## [◆ ](#a985b6a69f7cb7da875026aed4552aa6a)XEN\_DOMCTL\_gethvmcontext

| #define XEN\_DOMCTL\_gethvmcontext   33 |
| --- |

## [◆ ](#a72b7300f5aeeba20c7cd3c3aba88e243)XEN\_DOMCTL\_gethvmcontext\_partial

| #define XEN\_DOMCTL\_gethvmcontext\_partial   55 |
| --- |

## [◆ ](#afcf17d5e7402b39f32b6c7e21bcb0caa)XEN\_DOMCTL\_getnodeaffinity

| #define XEN\_DOMCTL\_getnodeaffinity   69 |
| --- |

## [◆ ](#a9e543639c3b1bae35b54ca0e3ae18fcd)XEN\_DOMCTL\_getpageframeinfo3

| #define XEN\_DOMCTL\_getpageframeinfo3   61 |
| --- |

## [◆ ](#ac0c8fe09ca02e3d19ffa2253ec56c36a)XEN\_DOMCTL\_gettscinfo

| #define XEN\_DOMCTL\_gettscinfo   59 |
| --- |

## [◆ ](#acd429b8834dc7284b33a66949c5b7ad0)XEN\_DOMCTL\_getvcpuaffinity

| #define XEN\_DOMCTL\_getvcpuaffinity   25 |
| --- |

## [◆ ](#af99e2f5c9a5b8a3ccd35a19961c0aa44)XEN\_DOMCTL\_getvcpucontext

| #define XEN\_DOMCTL\_getvcpucontext   13 |
| --- |

## [◆ ](#a20fcaf2b9a50516154f6664ecaba4310)XEN\_DOMCTL\_getvcpuextstate

| #define XEN\_DOMCTL\_getvcpuextstate   63 |
| --- |

## [◆ ](#abff3d223bd31c6f9b888c1293d7eaeca)XEN\_DOMCTL\_getvcpuinfo

| #define XEN\_DOMCTL\_getvcpuinfo   14 |
| --- |

## [◆ ](#aa38abb4809db00cbe963bcb41d61950a)XEN\_DOMCTL\_GRANT\_version

| #define XEN\_DOMCTL\_GRANT\_version | ( |  | *v* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((v) & [XEN\_DOMCTL\_GRANT\_version\_mask](#a6f5be8cef355d7bad22785dc29bd4dac))

[XEN\_DOMCTL\_GRANT\_version\_mask](#a6f5be8cef355d7bad22785dc29bd4dac)

#define XEN\_DOMCTL\_GRANT\_version\_mask

**Definition** domctl.h:83

## [◆ ](#a6f5be8cef355d7bad22785dc29bd4dac)XEN\_DOMCTL\_GRANT\_version\_mask

| #define XEN\_DOMCTL\_GRANT\_version\_mask   0xf |
| --- |

## [◆ ](#a131e1409d1d50a9ba638b194430fd63e)XEN\_DOMCTL\_hypercall\_init

| #define XEN\_DOMCTL\_hypercall\_init   22 |
| --- |

## [◆ ](#a1af9bebb704ccbf97d9ec79d3d860f58)XEN\_DOMCTL\_INTERFACE\_VERSION

| #define XEN\_DOMCTL\_INTERFACE\_VERSION   0x00000015 |
| --- |

## [◆ ](#ad3775642e389867857b9c7d33922deaf)XEN\_DOMCTL\_iomem\_permission

| #define XEN\_DOMCTL\_iomem\_permission   20 |
| --- |

## [◆ ](#ab2313d4fcb94c8e6473d67ce9607da48)XEN\_DOMCTL\_IOMMU\_MAX

| #define XEN\_DOMCTL\_IOMMU\_MAX   XEN\_DOMCTL\_IOMMU\_no\_sharept |
| --- |

## [◆ ](#a928664472460bf3656889afe3a381389)XEN\_DOMCTL\_IOMMU\_no\_sharep

| #define XEN\_DOMCTL\_IOMMU\_no\_sharep   (1U << \_XEN\_DOMCTL\_IOMMU\_no\_sharept) |
| --- |

## [◆ ](#a8dc90189fb09c0500ab9831a7304258b)XEN\_DOMCTL\_ioport\_mapping

| #define XEN\_DOMCTL\_ioport\_mapping   40 |
| --- |

## [◆ ](#ab00adfd7a0a99504c0d74fb9a730535e)XEN\_DOMCTL\_ioport\_permission

| #define XEN\_DOMCTL\_ioport\_permission   21 |
| --- |

## [◆ ](#ab350564800ede51e81bd1efbe9d31433)XEN\_DOMCTL\_irq\_permission

| #define XEN\_DOMCTL\_irq\_permission   19 |
| --- |

## [◆ ](#abc8af7f11bc93e5e335bda2ba00e770a)XEN\_DOMCTL\_max\_mem

| #define XEN\_DOMCTL\_max\_mem   11 |
| --- |

## [◆ ](#ad32b3ac435a726f6eec3baa03e9d2cc6)XEN\_DOMCTL\_max\_vcpus

| #define XEN\_DOMCTL\_max\_vcpus   15 |
| --- |

## [◆ ](#a2144e180680f2862fb3c5c4242ab81d1)XEN\_DOMCTL\_mem\_sharing\_op

| #define XEN\_DOMCTL\_mem\_sharing\_op   57 |
| --- |

## [◆ ](#a087034256c26c23fe8aa430224ed4f5e)XEN\_DOMCTL\_memory\_mapping

| #define XEN\_DOMCTL\_memory\_mapping   39 |
| --- |

## [◆ ](#af006015d33d0097664f6a6020873a82c)XEN\_DOMCTL\_monitor\_op

| #define XEN\_DOMCTL\_monitor\_op   77 |
| --- |

## [◆ ](#a6fc2629c1e6c4e882609e7e0e8214af7)XEN\_DOMCTL\_pausedomain

| #define XEN\_DOMCTL\_pausedomain   3 |
| --- |

## [◆ ](#aad00fc3c420bef96edac0233ee94cd47)XEN\_DOMCTL\_psr\_alloc

| #define XEN\_DOMCTL\_psr\_alloc   78 |
| --- |

## [◆ ](#ac27bce86ab62c437f2338a96f37a7d48)XEN\_DOMCTL\_psr\_cmt\_op

| #define XEN\_DOMCTL\_psr\_cmt\_op   75 |
| --- |

## [◆ ](#afb2feb24f3113dc5b924aaddf9095c10)XEN\_DOMCTL\_real\_mode\_area

| #define XEN\_DOMCTL\_real\_mode\_area   26 /\* Obsolete PPC only \*/ |
| --- |

## [◆ ](#aca08972618f6a931a3dffd924072e7f0)XEN\_DOMCTL\_resumedomain

| #define XEN\_DOMCTL\_resumedomain   27 |
| --- |

## [◆ ](#a481dbdc86321a9f74ef259fad8d3da08)XEN\_DOMCTL\_SCHEDOP\_getinfo

| #define XEN\_DOMCTL\_SCHEDOP\_getinfo   1 |
| --- |

## [◆ ](#ad1db496f608988bae2fe8ef992416d9e)XEN\_DOMCTL\_SCHEDOP\_getvcpuinfo

| #define XEN\_DOMCTL\_SCHEDOP\_getvcpuinfo   3 |
| --- |

## [◆ ](#a82c49a3fe9250e1e9f3cc4d5f5a74dee)XEN\_DOMCTL\_SCHEDOP\_putinfo

| #define XEN\_DOMCTL\_SCHEDOP\_putinfo   0 |
| --- |

## [◆ ](#a6d6e95c97391261ef77dfbccf15de5ba)XEN\_DOMCTL\_SCHEDOP\_putvcpuinfo

| #define XEN\_DOMCTL\_SCHEDOP\_putvcpuinfo   2 |
| --- |

## [◆ ](#ae765249383b5fc2e83d1474ac49b4fbd)XEN\_DOMCTL\_SCHEDRT\_extra

| #define XEN\_DOMCTL\_SCHEDRT\_extra   (1U<<\_XEN\_DOMCTL\_SCHEDRT\_extra) |
| --- |

## [◆ ](#a4e16878f8f098d4e5033b3d9c7c4fc66)XEN\_DOMCTL\_scheduler\_op

| #define XEN\_DOMCTL\_scheduler\_op   16 |
| --- |

## [◆ ](#a3f3aef1714b0d856bafe713ee9a0a096)XEN\_DOMCTL\_sendtrigger

| #define XEN\_DOMCTL\_sendtrigger   28 |
| --- |

## [◆ ](#a8e63ecac1fe62447de02590d81454c76)XEN\_DOMCTL\_set\_access\_required

| #define XEN\_DOMCTL\_set\_access\_required   64 |
| --- |

## [◆ ](#a3401578b5bb89676a5c5c2be96424ad7)XEN\_DOMCTL\_set\_address\_size

| #define XEN\_DOMCTL\_set\_address\_size   35 |
| --- |

## [◆ ](#af50563ae8af88f9de94f87986147f532)XEN\_DOMCTL\_set\_broken\_page\_p2m

| #define XEN\_DOMCTL\_set\_broken\_page\_p2m   67 |
| --- |

## [◆ ](#ad537d2de47beed8d6f670a863a3d44d2)XEN\_DOMCTL\_set\_cpu\_policy

| #define XEN\_DOMCTL\_set\_cpu\_policy   83 |
| --- |

## [◆ ](#a0d0a882796436312ecede3dcfd9569f3)XEN\_DOMCTL\_set\_ext\_vcpucontext

| #define XEN\_DOMCTL\_set\_ext\_vcpucontext   42 |
| --- |

## [◆ ](#adde0cd9f0afc1545bce1e7efe257479b)XEN\_DOMCTL\_set\_opt\_feature

| #define XEN\_DOMCTL\_set\_opt\_feature   44 /\* Obsolete IA64 only \*/ |
| --- |

## [◆ ](#ae35c3b2ead7567f169e79e786d2b915f)XEN\_DOMCTL\_set\_paging\_mempool\_size

| #define XEN\_DOMCTL\_set\_paging\_mempool\_size   86 |
| --- |

## [◆ ](#a80d963c7a959b9116b27918bb19cce6b)XEN\_DOMCTL\_set\_target

| #define XEN\_DOMCTL\_set\_target   46 |
| --- |

## [◆ ](#aa5227f853fed668e20d3c15a76278c1c)XEN\_DOMCTL\_set\_vcpu\_msrs

| #define XEN\_DOMCTL\_set\_vcpu\_msrs   73 |
| --- |

## [◆ ](#a3f56b7bdb2efe676716dca9a8303b502)XEN\_DOMCTL\_set\_virq\_handler

| #define XEN\_DOMCTL\_set\_virq\_handler   66 |
| --- |

## [◆ ](#a74047cd87a9608188c8412712f43d2f5)XEN\_DOMCTL\_setdebugging

| #define XEN\_DOMCTL\_setdebugging   18 |
| --- |

## [◆ ](#aab5cf53258ae8b11262e5f1b288537f7)XEN\_DOMCTL\_setdomainhandle

| #define XEN\_DOMCTL\_setdomainhandle   17 |
| --- |

## [◆ ](#a6ea99b9477c9e698af222cea8eef8103)XEN\_DOMCTL\_sethvmcontext

| #define XEN\_DOMCTL\_sethvmcontext   34 |
| --- |

## [◆ ](#a64def50fd26a62692718f14d34ac5056)XEN\_DOMCTL\_setnodeaffinity

| #define XEN\_DOMCTL\_setnodeaffinity   68 |
| --- |

## [◆ ](#a4d75d1a4982ead6f6b2066d562f3137b)XEN\_DOMCTL\_settimeoffset

| #define XEN\_DOMCTL\_settimeoffset   24 |
| --- |

## [◆ ](#a68f376046c9512b1ba0d536bf9f4da59)XEN\_DOMCTL\_settscinfo

| #define XEN\_DOMCTL\_settscinfo   60 |
| --- |

## [◆ ](#a52f4ddee28622818b0d0ad3a660782e4)XEN\_DOMCTL\_setvcpuaffinity

| #define XEN\_DOMCTL\_setvcpuaffinity   9 |
| --- |

## [◆ ](#a8fff7d4989f605f73dec55d59b10f5db)XEN\_DOMCTL\_setvcpucontext

| #define XEN\_DOMCTL\_setvcpucontext   12 |
| --- |

## [◆ ](#a95967323209e42eaf73b092c76c1ed8f)XEN\_DOMCTL\_setvcpuextstate

| #define XEN\_DOMCTL\_setvcpuextstate   62 |
| --- |

## [◆ ](#a33454734fa5e0f67818f763c0284bd0b)XEN\_DOMCTL\_setvnumainfo

| #define XEN\_DOMCTL\_setvnumainfo   74 |
| --- |

## [◆ ](#ab310ee5729b47d317fb381ba4a7765b9)XEN\_DOMCTL\_shadow\_op

| #define XEN\_DOMCTL\_shadow\_op   10 |
| --- |

## [◆ ](#ae4aefb0671418197673fc3055b3e1aa0)XEN\_DOMCTL\_SHADOW\_OP\_GET\_ALLOCATION

| #define XEN\_DOMCTL\_SHADOW\_OP\_GET\_ALLOCATION   30 |
| --- |

## [◆ ](#ad48421566046507c9773c91e0349e77b)XEN\_DOMCTL\_SHADOW\_OP\_SET\_ALLOCATION

| #define XEN\_DOMCTL\_SHADOW\_OP\_SET\_ALLOCATION   31 |
| --- |

## [◆ ](#aa33f73f1dda376298e235892d8322ba6)XEN\_DOMCTL\_soft\_reset

| #define XEN\_DOMCTL\_soft\_reset   79 |
| --- |

## [◆ ](#a25286953a431e6f3172ef9a5f90d18e4)XEN\_DOMCTL\_subscribe

| #define XEN\_DOMCTL\_subscribe   29 |
| --- |

## [◆ ](#a71b8b60fc4a387b89b482f7c0ba6a24f)XEN\_DOMCTL\_test\_assign\_device

| #define XEN\_DOMCTL\_test\_assign\_device   45 |
| --- |

## [◆ ](#a4a5a18f97beae00c8df5a27e8f58630b)XEN\_DOMCTL\_unbind\_pt\_irq

| #define XEN\_DOMCTL\_unbind\_pt\_irq   48 |
| --- |

## [◆ ](#a7f759b8eba89d5387e880f8aca7fd357)XEN\_DOMCTL\_unpausedomain

| #define XEN\_DOMCTL\_unpausedomain   4 |
| --- |

## [◆ ](#a584b0146d9466c742cde954cf933a35e)XEN\_DOMCTL\_vm\_event\_op

| #define XEN\_DOMCTL\_vm\_event\_op   56 |
| --- |

## [◆ ](#ac8d90b0cceefc508e8a56e59d4fa5ce3)XEN\_DOMCTL\_VMSI\_X86\_DELIV\_MASK

| #define XEN\_DOMCTL\_VMSI\_X86\_DELIV\_MASK   0x007000 |
| --- |

## [◆ ](#ad94911a72ecc25f10b2a58bd3c1fc091)XEN\_DOMCTL\_VMSI\_X86\_DEST\_ID\_MASK

| #define XEN\_DOMCTL\_VMSI\_X86\_DEST\_ID\_MASK   0x0000ff |
| --- |

## [◆ ](#a2377d6a66411ba1ca2a314965ef8c7be)XEN\_DOMCTL\_VMSI\_X86\_DM\_MASK

| #define XEN\_DOMCTL\_VMSI\_X86\_DM\_MASK   0x000200 |
| --- |

## [◆ ](#ad337d528c4d9eb777d7dd1a438a98dc8)XEN\_DOMCTL\_VMSI\_X86\_RH\_MASK

| #define XEN\_DOMCTL\_VMSI\_X86\_RH\_MASK   0x000100 |
| --- |

## [◆ ](#a5ca26c5c2b596e10104119d44b8c6f9a)XEN\_DOMCTL\_VMSI\_X86\_TRIG\_MASK

| #define XEN\_DOMCTL\_VMSI\_X86\_TRIG\_MASK   0x008000 |
| --- |

## [◆ ](#a81cec14a8ea2e245bc664647e0bf70ab)XEN\_DOMCTL\_VMSI\_X86\_UNMASKED

| #define XEN\_DOMCTL\_VMSI\_X86\_UNMASKED   0x010000 |
| --- |

## [◆ ](#a9794dd91afdd16869e3a42b6b3239ecd)XEN\_DOMCTL\_vmtrace\_op

| #define XEN\_DOMCTL\_vmtrace\_op   84 |
| --- |

## [◆ ](#a850fc8c65f70ad1ad1c9d000f94960ff)XEN\_DOMCTL\_vuart\_op

| #define XEN\_DOMCTL\_vuart\_op   81 |
| --- |

## [◆ ](#a34e24b31aaadfd78c585a6187fc89187)XEN\_DOMINF\_blocked

| #define XEN\_DOMINF\_blocked   (1U << \_XEN\_DOMINF\_blocked) |
| --- |

## [◆ ](#ade451ebb63161b5cdbfab6221cb9c4f0)XEN\_DOMINF\_debugged

| #define XEN\_DOMINF\_debugged   (1U << \_XEN\_DOMINF\_debugged) |
| --- |

## [◆ ](#afcdfc193f40faf980e2e23d485de4e79)XEN\_DOMINF\_dying

| #define XEN\_DOMINF\_dying   (1U << \_XEN\_DOMINF\_dying) |
| --- |

## [◆ ](#a919137e7b6b084d368cca8766091754e)XEN\_DOMINF\_hap

| #define XEN\_DOMINF\_hap   (1U << \_XEN\_DOMINF\_hap) |
| --- |

## [◆ ](#a140d5075193daeba92f4b83a0c2f1e14)XEN\_DOMINF\_hvm\_guest

| #define XEN\_DOMINF\_hvm\_guest   (1U << \_XEN\_DOMINF\_hvm\_guest) |
| --- |

## [◆ ](#a32c611154d6e6bb3c3b5d4ac9cab5e65)XEN\_DOMINF\_paused

| #define XEN\_DOMINF\_paused   (1U << \_XEN\_DOMINF\_paused) |
| --- |

## [◆ ](#a7e0f50072c881ded1670fa4efda493e0)XEN\_DOMINF\_running

| #define XEN\_DOMINF\_running   (1U << \_XEN\_DOMINF\_running) |
| --- |

## [◆ ](#af49f7e9e048fafaa4ec004d46919d313)XEN\_DOMINF\_shutdown

| #define XEN\_DOMINF\_shutdown   (1U << \_XEN\_DOMINF\_shutdown) |
| --- |

## [◆ ](#a8e242d887ef91743672a2a3ae3bd74f2)XEN\_DOMINF\_shutdownmask

| #define XEN\_DOMINF\_shutdownmask   255 |
| --- |

## [◆ ](#af3cfe05618c9a1bd3dbe48f42e7cea04)XEN\_DOMINF\_shutdownshift

| #define XEN\_DOMINF\_shutdownshift   16 |
| --- |

## [◆ ](#a37e263699b64912d80697a374d127796)XEN\_DOMINF\_xs\_domain

| #define XEN\_DOMINF\_xs\_domain   (1U << \_XEN\_DOMINF\_xs\_domain) |
| --- |

## [◆ ](#a40c471099d055910f5bed2994efec643)XEN\_INVALID\_MAX\_VCPU\_ID

| #define XEN\_INVALID\_MAX\_VCPU\_ID   (~0U) /\* Domain has no vcpus? \*/ |
| --- |

## [◆ ](#a08dbd46725afbad5fe54879c9d0518c1)XEN\_SCHEDULER\_ARINC653

| #define XEN\_SCHEDULER\_ARINC653   7 |
| --- |

## [◆ ](#afee5561bd17af9ddba71e01697ee50d3)XEN\_SCHEDULER\_CREDIT

| #define XEN\_SCHEDULER\_CREDIT   5 |
| --- |

## [◆ ](#a560830bf6e1c6a96fae85d6788fffc7c)XEN\_SCHEDULER\_CREDIT2

| #define XEN\_SCHEDULER\_CREDIT2   6 |
| --- |

## [◆ ](#ac0f58da75c220a8afef88585628874f2)XEN\_SCHEDULER\_NULL

| #define XEN\_SCHEDULER\_NULL   9 |
| --- |

## [◆ ](#afaede03296414e2adaeed009bfd4d0e0)XEN\_SCHEDULER\_RTDS

| #define XEN\_SCHEDULER\_RTDS   8 |
| --- |

## Typedef Documentation

## [◆ ](#a975bbf787336d78a2fe063f5f16766db)xen\_domctl\_getdomaininfo\_t

| typedef struct [xen\_domctl\_getdomaininfo](structxen__domctl__getdomaininfo.md) [xen\_domctl\_getdomaininfo\_t](#a975bbf787336d78a2fe063f5f16766db) |
| --- |

## [◆ ](#adfbd6c6d40e27f06e00d39acd5be271e)xen\_domctl\_schedparam\_vcpu\_t

| typedef struct [xen\_domctl\_schedparam\_vcpu](structxen__domctl__schedparam__vcpu.md) [xen\_domctl\_schedparam\_vcpu\_t](#adfbd6c6d40e27f06e00d39acd5be271e) |
| --- |

## [◆ ](#a739ed8d92302fb02b53f4f769d57d83e)xen\_domctl\_t

| typedef struct [xen\_domctl](structxen__domctl.md) [xen\_domctl\_t](#a739ed8d92302fb02b53f4f769d57d83e) |
| --- |

## Enumeration Type Documentation

## [◆ ](#aa0ba08b170800d6d7723b694525ade07)pt\_irq\_type

| enum [pt\_irq\_type](#aa0ba08b170800d6d7723b694525ade07) |
| --- |

| Enumerator | |
| --- | --- |
| PT\_IRQ\_TYPE\_PCI |  |
| PT\_IRQ\_TYPE\_ISA |  |
| PT\_IRQ\_TYPE\_MSI |  |
| PT\_IRQ\_TYPE\_MSI\_TRANSLATE |  |
| PT\_IRQ\_TYPE\_SPI |  |

## Function Documentation

## [◆ ](#a4e3858932ea51b98f6594ec863305eaa)DEFINE\_XEN\_GUEST\_HANDLE() [1/3]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [xen\_domctl\_getdomaininfo\_t](#a975bbf787336d78a2fe063f5f16766db) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a4bff168adfcb0ee8cc56f22a1b468112)DEFINE\_XEN\_GUEST\_HANDLE() [2/3]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [xen\_domctl\_schedparam\_vcpu\_t](#adfbd6c6d40e27f06e00d39acd5be271e) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a0d3b8859d3644f60cb1753391b03face)DEFINE\_XEN\_GUEST\_HANDLE() [3/3]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [xen\_domctl\_t](#a739ed8d92302fb02b53f4f769d57d83e) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [public](dir_a9d090e3588b677c614b5c45cd68e13b.md)
- [domctl.h](public_2domctl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
