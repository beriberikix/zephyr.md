---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__pcie__host__interface.html
original_path: doxygen/html/group__pcie__host__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

PCIe Host Interface

[Device Driver APIs](group__io__interfaces.md)

PCIe Host Interface.
[More...](#details)

| Topics | |
| --- | --- |
|  | [PCIe Capabilities](group__pcie__capabilities.md) |
|  | [PCIe Host MSI Interface](group__pcie__host__msi__interface.md) |
|  | PCIe Host MSI Interface. |
|  | [PCIe Host PTM Interface](group__pcie__host__ptm__interface.md) |
|  | PCIe Host PTM Interface. |
|  | [PCIe Virtual Channel Host Interface](group__pcie__vc__host__interface.md) |
|  | PCIe Virtual Channel Host Interface. |

| Data Structures | |
| --- | --- |
| struct | [pcie\_dev](structpcie__dev.md) |
| struct | [pcie\_bar](structpcie__bar.md) |
| struct | [pcie\_scan\_opt](structpcie__scan__opt.md) |
|  | Options for performing a scan for PCI devices. [More...](structpcie__scan__opt.md#details) |

| Macros | |
| --- | --- |
| #define | [PCIE\_ID\_IS\_VALID](#gac7d5c41ea3c8999126d89d95961b430b)(id) |
| #define | [PCIE\_DT\_ID](#ga304228150cd8ec56aa24be468e9d79bf)(node\_id) |
|  | Get the PCIe Vendor and Device ID for a node. |
| #define | [PCIE\_DT\_INST\_ID](#ga3e89194346fa9b945f1873380c527cee)(inst) |
|  | Get the PCIe Vendor and Device ID for a node. |
| #define | [DEVICE\_PCIE\_DECLARE](#gad0b870d891458c4ebd7ab2ac1c372eec)(node\_id) |
|  | Declare a PCIe context variable for a DTS node. |
| #define | [DEVICE\_PCIE\_INST\_DECLARE](#gade2f1f53701b1d80b5593045e977e4d6)(inst) |
|  | Declare a PCIe context variable for a DTS node. |
| #define | [DEVICE\_PCIE\_INIT](#gab6c472838e13293980cd53c65aaa3c47)(node\_id, name) |
|  | Initialize a named struct member to point at a PCIe context. |
| #define | [DEVICE\_PCIE\_INST\_INIT](#gac175df702e85f599b28b7a567c64d146)(inst, name) |
|  | Initialize a named struct member to point at a PCIe context. |
| #define | [PCIE\_HOST\_CONTROLLER](#ga7b500200f090dc95322fe670bf64628d)(n) |
|  | Get the BDF for a given PCI host controller. |
| #define | [PCIE\_CONF\_CAPPTR](#gaad23a180cf411bd8fa10027b9f16eb91)   13U /\* capabilities pointer \*/ |
| #define | [PCIE\_CONF\_CAPPTR\_FIRST](#gabe5832ddf2b8399e8f672564ce85ad7e)(w) |
| #define | [PCIE\_CONF\_CAP\_ID](#gaa888f548db209011f1cf5c87b1f351b8)(w) |
| #define | [PCIE\_CONF\_CAP\_NEXT](#ga98476f56fe7d46b6bee505e0db1c1906)(w) |
| #define | [PCIE\_CONF\_EXT\_CAPPTR](#gabeb1434679b73c98f2ada475c8502e32)   64U |
| #define | [PCIE\_CONF\_EXT\_CAP\_ID](#ga491d796e2477816c8f8aac4c7b753e3d)(w) |
| #define | [PCIE\_CONF\_EXT\_CAP\_VER](#gaf22a73f116325d3509cde1f83b3d7900)(w) |
| #define | [PCIE\_CONF\_EXT\_CAP\_NEXT](#gad0fa4f22781b85d06321192338088073)(w) |
| #define | [PCIE\_CONF\_ID](#ga2b694e339f9be5982605ed53e022ae06)   0U |
| #define | [PCIE\_CONF\_CMDSTAT](#ga2fc046f15e216337194e41480518c982)   1U /\* command/status register \*/ |
| #define | [PCIE\_CONF\_CMDSTAT\_IO](#ga6a9008421671f66ea9a6f11f87edd514)   0x00000001U /\* I/O access enable \*/ |
| #define | [PCIE\_CONF\_CMDSTAT\_MEM](#ga24661608e9f66f79bbdcde9304b24820)   0x00000002U /\* mem access enable \*/ |
| #define | [PCIE\_CONF\_CMDSTAT\_MASTER](#ga8a770450f03bfb020f223e0fea96189d)   0x00000004U /\* bus master enable \*/ |
| #define | [PCIE\_CONF\_CMDSTAT\_INTERRUPT](#ga4712b7b75d9bf0098e6c80c69587ef86)   0x00080000U /\* interrupt status \*/ |
| #define | [PCIE\_CONF\_CMDSTAT\_CAPS](#ga7127f82d9c9b093b1056125ca1bb9d65)   0x00100000U /\* capabilities list \*/ |
| #define | [PCIE\_CONF\_CLASSREV](#ga6946589a87e364c4710fba1dded553dc)   2U /\* class/revision register \*/ |
| #define | [PCIE\_CONF\_CLASSREV\_CLASS](#gace40af940c01af2876e6fe8d599677bc)(w) |
| #define | [PCIE\_CONF\_CLASSREV\_SUBCLASS](#ga769e486c00a8ceda4ddb3f3eebc09c59)(w) |
| #define | [PCIE\_CONF\_CLASSREV\_PROGIF](#ga36f77d220a11a9a30c4656e7f616ec05)(w) |
| #define | [PCIE\_CONF\_CLASSREV\_REV](#gae102d89e2fb359c3c9dda6b35d9ecd4f)(w) |
| #define | [PCIE\_CONF\_TYPE](#ga43ad620ae5a3041f0d7553de03c6da84)   3U |
| #define | [PCIE\_CONF\_MULTIFUNCTION](#ga9462e002a9d4b49ef7e7c97942765215)(w) |
| #define | [PCIE\_CONF\_TYPE\_BRIDGE](#gab7c494d71f6490e483b642a02ef90930)(w) |
| #define | [PCIE\_CONF\_TYPE\_GET](#ga0580b798e6498097573c1eb0f2c6d2b1)(w) |
| #define | [PCIE\_CONF\_TYPE\_STANDARD](#ga8b76fee3c256914a5044313ff9805969)   0x0U |
| #define | [PCIE\_CONF\_TYPE\_PCI\_BRIDGE](#ga90e8a996bf491fda870ff29b119a5242)   0x1U |
| #define | [PCIE\_CONF\_TYPE\_CARDBUS\_BRIDGE](#gae9587843cac6247fcfb72f985ff4b030)   0x2U |
| #define | [PCIE\_CONF\_BAR0](#gadfd21197ccd78d7bfb549fbb6f7070ff)   4U |
| #define | [PCIE\_CONF\_BAR1](#ga77e43c6060febf8a5b8439c7fc940a1f)   5U |
| #define | [PCIE\_CONF\_BAR2](#ga90040a3b78c5f5563f2f123e9fb05dd8)   6U |
| #define | [PCIE\_CONF\_BAR3](#ga05b9be5537cf1a4f3994c1a2c82282a1)   7U |
| #define | [PCIE\_CONF\_BAR4](#ga51dbf953128b6a464bf50cfa459626e7)   8U |
| #define | [PCIE\_CONF\_BAR5](#ga84fb2d49dd14438a9ff12a8eeb5bca60)   9U |
| #define | [PCIE\_CONF\_BAR\_IO](#ga2f4020ce7fec0e3b5c9b121951468b70)(w) |
| #define | [PCIE\_CONF\_BAR\_MEM](#ga6018ef2d851fd6a64a1ad4dde956f4c9)(w) |
| #define | [PCIE\_CONF\_BAR\_64](#ga6d2644d85b7bfbf9a526e6d54096982d)(w) |
| #define | [PCIE\_CONF\_BAR\_ADDR](#gaf163a00f52cc96bc7694e4e7e7a8d1fe)(w) |
| #define | [PCIE\_CONF\_BAR\_IO\_ADDR](#gabe49cc62101a531ca9e26b0290218797)(w) |
| #define | [PCIE\_CONF\_BAR\_FLAGS](#ga23c45457ec77c6fd2e1977710f6edf28)(w) |
| #define | [PCIE\_CONF\_BAR\_NONE](#ga296141fc89700213899b6463e1166477)   0U |
| #define | [PCIE\_CONF\_BAR\_INVAL](#ga65e8ddebc6d25b51940ae647f81deca1)   0xFFFFFFF0U |
| #define | [PCIE\_CONF\_BAR\_INVAL64](#ga8e1968a28791ed0529d622f32e6fad6c)   0xFFFFFFFFFFFFFFF0UL |
| #define | [PCIE\_CONF\_BAR\_INVAL\_FLAGS](#gafd74fe08ef11c685775433236d0fd734)(w) |
| #define | [PCIE\_BUS\_NUMBER](#gaac6d5d5eb2ff10b6d85b3bb3efb0ce6e)   6U |
| #define | [PCIE\_BUS\_PRIMARY\_NUMBER](#ga4c0dbee39acf51c94b5ececba150f8d0)(w) |
| #define | [PCIE\_BUS\_SECONDARY\_NUMBER](#ga61cd874c47de3545ca2ffa1eecd7eb42)(w) |
| #define | [PCIE\_BUS\_SUBORDINATE\_NUMBER](#ga0be93727f18869b7a486e42eac47fa2d)(w) |
| #define | [PCIE\_SECONDARY\_LATENCY\_TIMER](#gaa05e49d0cafbe51b7742354470d07bd0)(w) |
| #define | [PCIE\_BUS\_NUMBER\_VAL](#ga784bc42d77fec195d794c29067bd988c)(prim, sec, sub, lat) |
| #define | [PCIE\_IO\_SEC\_STATUS](#ga111eab92400e240ec5b7f08caf1b8a87)   7U |
| #define | [PCIE\_IO\_BASE](#ga34f56e87ececf58b285e91341cd27d23)(w) |
| #define | [PCIE\_IO\_LIMIT](#ga4629a222d00917b2e3cad6aadbfd2ec1)(w) |
| #define | [PCIE\_SEC\_STATUS](#ga804b34fd47ba065287e0257fac84ac35)(w) |
| #define | [PCIE\_IO\_SEC\_STATUS\_VAL](#ga61f05b2c4cd5c672af43960b320e33bc)(iob, iol, sec\_status) |
| #define | [PCIE\_MEM\_BASE\_LIMIT](#ga6fbcd3f523deb069aa31bcd31973d00b)   8U |
| #define | [PCIE\_MEM\_BASE](#gacd6be1e38666a6a137b1654007cf293a)(w) |
| #define | [PCIE\_MEM\_LIMIT](#ga9f5d23ad0674aed0bf5c1869621de303)(w) |
| #define | [PCIE\_MEM\_BASE\_LIMIT\_VAL](#ga93a6dbe27d3d11be29397ae80c58a589)(memb, meml) |
| #define | [PCIE\_PREFETCH\_BASE\_LIMIT](#ga8dd5906e8d735210d9f8ca25d39684b4)   9U |
| #define | [PCIE\_PREFETCH\_BASE](#ga5f7aa0fc063ec072bf7e89fca603c825)(w) |
| #define | [PCIE\_PREFETCH\_LIMIT](#gaf0a18504a4eb2061d1afc90fc7b8ee21)(w) |
| #define | [PCIE\_PREFETCH\_BASE\_LIMIT\_VAL](#ga02b269663488e7c7469415622390ce55)(pmemb, pmeml) |
| #define | [PCIE\_PREFETCH\_BASE\_UPPER](#ga6ebdd02e0599f33becb6cf413be0a8cd)   10U |
| #define | [PCIE\_PREFETCH\_LIMIT\_UPPER](#gab0eda55fd8c2c4025dc4350ef946a61b)   11U |
| #define | [PCIE\_IO\_BASE\_LIMIT\_UPPER](#gafc1acf0ac9b46629497c7a552f5650ce)   12U |
| #define | [PCIE\_IO\_BASE\_UPPER](#ga8bf9a619d6d83cbb009a7f18b501db92)(w) |
| #define | [PCIE\_IO\_LIMIT\_UPPER](#ga76a59c926f2760a04c4d8439cb227fe2)(w) |
| #define | [PCIE\_IO\_BASE\_LIMIT\_UPPER\_VAL](#ga88669a9ca40294cee41bb163a908737f)(iobu, iolu) |
| #define | [PCIE\_CONF\_INTR](#gaa5a2c8849e4cac05ee584827aedbfb93)   15U |
| #define | [PCIE\_CONF\_INTR\_IRQ](#ga5c2f2d310dc6a73530b6909ce2c2536e)(w) |
| #define | [PCIE\_CONF\_INTR\_IRQ\_NONE](#ga995ca5b5146669c9234d3cdd596b715c)   0xFFU /\* no interrupt routed \*/ |
| #define | [PCIE\_MAX\_BUS](#ga1ce9e061b5a773f3ee74f78893174f9e)   (0xFFFFFFFFU & [PCIE\_BDF\_BUS\_MASK](dt-bindings_2pcie_2pcie_8h.md#a193dd359d7a96bdd904662717c7fbf6d)) |
| #define | [PCIE\_MAX\_DEV](#ga8809359a58c787a939d01f25e12ac51a)   (0xFFFFFFFFU & [PCIE\_BDF\_DEV\_MASK](dt-bindings_2pcie_2pcie_8h.md#a85cc69963a93046bda0f1594803af9eb)) |
| #define | [PCIE\_MAX\_FUNC](#gaee8ddb7b7b1354fd5c835b67321f286b)   (0xFFFFFFFFU & [PCIE\_BDF\_FUNC\_MASK](dt-bindings_2pcie_2pcie_8h.md#ab481360fa29cf086cc5369e6f1860a5f)) |
| #define | [PCIE\_IRQ\_CONNECT](#ga6616499a7be31d40af31bb8134aa4a51)(bdf\_p, irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) |
|  | Initialize an interrupt handler for a PCIe endpoint IRQ. |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) |
|  | A unique PCI(e) endpoint (bus, device, function). |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pcie\_id\_t](#ga30840d0e312e35f00790660193fd4c04) |
|  | A unique PCI(e) identifier (vendor ID, device ID). |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [pcie\_scan\_cb\_t](#ga922580e4fb6200ef75425bb54801ceda)) ([pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [pcie\_id\_t](#ga30840d0e312e35f00790660193fd4c04) id, void \*cb\_data) |
|  | Callback type used for scanning for PCI endpoints. |

| Enumerations | |
| --- | --- |
| enum | { [PCIE\_SCAN\_RECURSIVE](#ggabe00c00fc0af29786c3b42f22f82aecfa228932ef6533931a9ae55e37dc38f3c4) = BIT(0) , [PCIE\_SCAN\_CB\_ALL](#ggabe00c00fc0af29786c3b42f22f82aecfa3579c18ade658f55affd41bfd38f9072) = BIT(1) } |

| Functions | |
| --- | --- |
| [pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) | [pcie\_bdf\_lookup](#gaad76dbfd3d53d812db092e2029c65fea) ([pcie\_id\_t](#ga30840d0e312e35f00790660193fd4c04) id) |
|  | Look up the BDF based on PCI(e) vendor & device ID. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pcie\_conf\_read](#ga10ecc667c564548e4ddf3ca4374242b5) ([pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg) |
|  | Read a 32-bit word from an endpoint's configuration space. |
| void | [pcie\_conf\_write](#ga47a2e88935e04330d449db5463d9f21a) ([pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
|  | Write a 32-bit word to an endpoint's configuration space. |
| int | [pcie\_scan](#ga9a7b3c202f91d37fe8445d5016f4c6ab) (const struct [pcie\_scan\_opt](structpcie__scan__opt.md) \*opt) |
|  | Scan for PCIe devices. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_probe](#ga38df5e6054de59f1bc21e89a2701e998) ([pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [pcie\_id\_t](#ga30840d0e312e35f00790660193fd4c04) id) |
|  | Probe for the presence of a PCI(e) endpoint. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_get\_mbar](#gadeb891fbb5b900eb60de22d40afe355e) ([pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int bar\_index, struct [pcie\_bar](structpcie__bar.md) \*mbar) |
|  | Get the MBAR at a specific BAR index. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_probe\_mbar](#gad8463013e51c4ddcca7b5f805f918685) ([pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int index, struct [pcie\_bar](structpcie__bar.md) \*mbar) |
|  | Probe the nth MMIO address assigned to an endpoint. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_get\_iobar](#ga3523bbdfd67d4b56cf6cd86c98c830bf) ([pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int bar\_index, struct [pcie\_bar](structpcie__bar.md) \*iobar) |
|  | Get the I/O BAR at a specific BAR index. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_probe\_iobar](#gaa81d98a9ee58062c02be576fb0dfefd9) ([pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int index, struct [pcie\_bar](structpcie__bar.md) \*iobar) |
|  | Probe the nth I/O BAR address assigned to an endpoint. |
| void | [pcie\_set\_cmd](#ga3516fec89df75eb3d77f54193059fc5c) ([pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bits, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) on) |
|  | Set or reset bits in the endpoint command/status register. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [pcie\_alloc\_irq](#gad69ae431e5f91992f071dee9d7fa9110) ([pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) bdf) |
|  | Allocate an IRQ for an endpoint. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [pcie\_get\_irq](#gaed7fef462ba02a22b5875b1a2c0d965a) ([pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) bdf) |
|  | Return the IRQ assigned by the firmware/board to an endpoint. |
| void | [pcie\_irq\_enable](#gafb69216f9224a9040b1f0b58eb286196) ([pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Enable the PCI(e) endpoint to generate the specified IRQ. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pcie\_get\_cap](#ga56e724c9bfd7f44c550ccff1b46978a8) ([pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cap\_id) |
|  | Find a PCI(e) capability in an endpoint's configuration space. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pcie\_get\_ext\_cap](#ga5db0d2a5946d20406070b47a1a7acf21) ([pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cap\_id) |
|  | Find an Extended PCI(e) capability in an endpoint's configuration space. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_connect\_dynamic\_irq](#ga14970194de1024a1a4669b69f932a4f5) ([pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int priority, void(\*routine)(const void \*parameter), const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Dynamically connect a PCIe endpoint IRQ to an ISR handler. |

## Detailed Description

PCIe Host Interface.

## Macro Definition Documentation

## [◆ ](#gad0b870d891458c4ebd7ab2ac1c372eec)DEVICE\_PCIE\_DECLARE

| #define DEVICE\_PCIE\_DECLARE | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([pcie\_dev](structpcie__dev.md), Z\_DEVICE\_PCIE\_NAME(node\_id)) = { \

.bdf = [PCIE\_BDF\_NONE](dt-bindings_2pcie_2pcie_8h.md#a6268e6c107a85fbc6035eca5e6b3cfd6), \

.id = [PCIE\_DT\_ID](#ga304228150cd8ec56aa24be468e9d79bf)(node\_id), \

.class\_rev = [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, class\_rev, 0), \

.class\_rev\_mask = [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, class\_rev\_mask, 0), \

}

[PCIE\_BDF\_NONE](dt-bindings_2pcie_2pcie_8h.md#a6268e6c107a85fbc6035eca5e6b3cfd6)

#define PCIE\_BDF\_NONE

**Definition** pcie.h:38

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)

#define DT\_PROP\_OR(node\_id, prop, default\_value)

Like DT\_PROP(), but with a fallback to default\_value.

**Definition** devicetree.h:777

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[PCIE\_DT\_ID](#ga304228150cd8ec56aa24be468e9d79bf)

#define PCIE\_DT\_ID(node\_id)

Get the PCIe Vendor and Device ID for a node.

**Definition** pcie.h:74

[pcie\_dev](structpcie__dev.md)

**Definition** pcie.h:59

Declare a PCIe context variable for a DTS node.

Declares a PCIe context for a DTS node. This must be done before using the [DEVICE\_PCIE\_INIT()](#gab6c472838e13293980cd53c65aaa3c47) macro for the same node.

Parameters
:   | node\_id | DTS node identifier |
    | --- | --- |

## [◆ ](#gab6c472838e13293980cd53c65aaa3c47)DEVICE\_PCIE\_INIT

| #define DEVICE\_PCIE\_INIT | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

.name = &Z\_DEVICE\_PCIE\_NAME(node\_id)

Initialize a named struct member to point at a PCIe context.

Initialize PCIe-related information within a specific instance of a device config struct, using information from DTS. Using the macro requires having first created PCIe context struct using the [DEVICE\_PCIE\_DECLARE()](#gad0b870d891458c4ebd7ab2ac1c372eec) macro.

Example for an instance of a driver belonging to the "foo" subsystem

struct foo\_config { struct [pcie\_dev](structpcie__dev.md) \*pcie; ... };

DEVICE\_PCIE\_ID\_DECLARE(DT\_DRV\_INST(...)); struct foo\_config my\_config = { [DEVICE\_PCIE\_INIT(pcie, DT\_DRV\_INST(...))](#gab6c472838e13293980cd53c65aaa3c47), ... };

Parameters
:   | node\_id | DTS node identifier |
    | --- | --- |
    | name | Member name within config for the MMIO region |

## [◆ ](#gade2f1f53701b1d80b5593045e977e4d6)DEVICE\_PCIE\_INST\_DECLARE

| #define DEVICE\_PCIE\_INST\_DECLARE | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

[DEVICE\_PCIE\_DECLARE](#gad0b870d891458c4ebd7ab2ac1c372eec)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3410

[DEVICE\_PCIE\_DECLARE](#gad0b870d891458c4ebd7ab2ac1c372eec)

#define DEVICE\_PCIE\_DECLARE(node\_id)

Declare a PCIe context variable for a DTS node.

**Definition** pcie.h:96

Declare a PCIe context variable for a DTS node.

This is equivalent to [DEVICE\_PCIE\_DECLARE(DT\_DRV\_INST(inst))](#gad0b870d891458c4ebd7ab2ac1c372eec)

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |

## [◆ ](#gac175df702e85f599b28b7a567c64d146)DEVICE\_PCIE\_INST\_INIT

| #define DEVICE\_PCIE\_INST\_INIT | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

[DEVICE\_PCIE\_INIT](#gab6c472838e13293980cd53c65aaa3c47)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DEVICE\_PCIE\_INIT](#gab6c472838e13293980cd53c65aaa3c47)

#define DEVICE\_PCIE\_INIT(node\_id, name)

Initialize a named struct member to point at a PCIe context.

**Definition** pcie.h:138

Initialize a named struct member to point at a PCIe context.

This is equivalent to [DEVICE\_PCIE\_INIT(DT\_DRV\_INST(inst), name)](#gab6c472838e13293980cd53c65aaa3c47)

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |
    | name | Name of the struct member (of type struct [pcie\_dev](structpcie__dev.md) \*) |

## [◆ ](#gaac6d5d5eb2ff10b6d85b3bb3efb0ce6e)PCIE\_BUS\_NUMBER

| #define PCIE\_BUS\_NUMBER   6U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga784bc42d77fec195d794c29067bd988c)PCIE\_BUS\_NUMBER\_VAL

| #define PCIE\_BUS\_NUMBER\_VAL | ( |  | *prim*, |
| --- | --- | --- | --- |
|  |  |  | *sec*, |
|  |  |  | *sub*, |
|  |  |  | *lat* ) |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((prim) & 0xffUL) | \

(((sec) & 0xffUL) << 8) | \

(((sub) & 0xffUL) << 16) | \

(((lat) & 0xffUL) << 24))

## [◆ ](#ga4c0dbee39acf51c94b5ececba150f8d0)PCIE\_BUS\_PRIMARY\_NUMBER

| #define PCIE\_BUS\_PRIMARY\_NUMBER | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

((w) & 0xffUL)

## [◆ ](#ga61cd874c47de3545ca2ffa1eecd7eb42)PCIE\_BUS\_SECONDARY\_NUMBER

| #define PCIE\_BUS\_SECONDARY\_NUMBER | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) >> 8) & 0xffUL)

## [◆ ](#ga0be93727f18869b7a486e42eac47fa2d)PCIE\_BUS\_SUBORDINATE\_NUMBER

| #define PCIE\_BUS\_SUBORDINATE\_NUMBER | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) >> 16) & 0xffUL)

## [◆ ](#gadfd21197ccd78d7bfb549fbb6f7070ff)PCIE\_CONF\_BAR0

| #define PCIE\_CONF\_BAR0   4U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga77e43c6060febf8a5b8439c7fc940a1f)PCIE\_CONF\_BAR1

| #define PCIE\_CONF\_BAR1   5U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga90040a3b78c5f5563f2f123e9fb05dd8)PCIE\_CONF\_BAR2

| #define PCIE\_CONF\_BAR2   6U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga05b9be5537cf1a4f3994c1a2c82282a1)PCIE\_CONF\_BAR3

| #define PCIE\_CONF\_BAR3   7U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga51dbf953128b6a464bf50cfa459626e7)PCIE\_CONF\_BAR4

| #define PCIE\_CONF\_BAR4   8U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga84fb2d49dd14438a9ff12a8eeb5bca60)PCIE\_CONF\_BAR5

| #define PCIE\_CONF\_BAR5   9U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga6d2644d85b7bfbf9a526e6d54096982d)PCIE\_CONF\_BAR\_64

| #define PCIE\_CONF\_BAR\_64 | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) & 0x00000006U) == 0x00000004U)

## [◆ ](#gaf163a00f52cc96bc7694e4e7e7a8d1fe)PCIE\_CONF\_BAR\_ADDR

| #define PCIE\_CONF\_BAR\_ADDR | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

((w) & ~0xfUL)

## [◆ ](#ga23c45457ec77c6fd2e1977710f6edf28)PCIE\_CONF\_BAR\_FLAGS

| #define PCIE\_CONF\_BAR\_FLAGS | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

((w) & 0xfUL)

## [◆ ](#ga65e8ddebc6d25b51940ae647f81deca1)PCIE\_CONF\_BAR\_INVAL

| #define PCIE\_CONF\_BAR\_INVAL   0xFFFFFFF0U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga8e1968a28791ed0529d622f32e6fad6c)PCIE\_CONF\_BAR\_INVAL64

| #define PCIE\_CONF\_BAR\_INVAL64   0xFFFFFFFFFFFFFFF0UL |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#gafd74fe08ef11c685775433236d0fd734)PCIE\_CONF\_BAR\_INVAL\_FLAGS

| #define PCIE\_CONF\_BAR\_INVAL\_FLAGS | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

((((w) & 0x00000006U) == 0x00000006U) || \

(((w) & 0x00000006U) == 0x00000002U))

## [◆ ](#ga2f4020ce7fec0e3b5c9b121951468b70)PCIE\_CONF\_BAR\_IO

| #define PCIE\_CONF\_BAR\_IO | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) & 0x00000001U) == 0x00000001U)

## [◆ ](#gabe49cc62101a531ca9e26b0290218797)PCIE\_CONF\_BAR\_IO\_ADDR

| #define PCIE\_CONF\_BAR\_IO\_ADDR | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

((w) & ~0x3UL)

## [◆ ](#ga6018ef2d851fd6a64a1ad4dde956f4c9)PCIE\_CONF\_BAR\_MEM

| #define PCIE\_CONF\_BAR\_MEM | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) & 0x00000001U) != 0x00000001U)

## [◆ ](#ga296141fc89700213899b6463e1166477)PCIE\_CONF\_BAR\_NONE

| #define PCIE\_CONF\_BAR\_NONE   0U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#gaa888f548db209011f1cf5c87b1f351b8)PCIE\_CONF\_CAP\_ID

| #define PCIE\_CONF\_CAP\_ID | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

((w) & 0xFFU)

## [◆ ](#ga98476f56fe7d46b6bee505e0db1c1906)PCIE\_CONF\_CAP\_NEXT

| #define PCIE\_CONF\_CAP\_NEXT | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) >> 10) & 0x3FU)

## [◆ ](#gaad23a180cf411bd8fa10027b9f16eb91)PCIE\_CONF\_CAPPTR

| #define PCIE\_CONF\_CAPPTR   13U /\* capabilities pointer \*/ |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#gabe5832ddf2b8399e8f672564ce85ad7e)PCIE\_CONF\_CAPPTR\_FIRST

| #define PCIE\_CONF\_CAPPTR\_FIRST | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) >> 2) & 0x3FU)

## [◆ ](#ga6946589a87e364c4710fba1dded553dc)PCIE\_CONF\_CLASSREV

| #define PCIE\_CONF\_CLASSREV   2U /\* class/revision register \*/ |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#gace40af940c01af2876e6fe8d599677bc)PCIE\_CONF\_CLASSREV\_CLASS

| #define PCIE\_CONF\_CLASSREV\_CLASS | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) >> 24) & 0xFFU)

## [◆ ](#ga36f77d220a11a9a30c4656e7f616ec05)PCIE\_CONF\_CLASSREV\_PROGIF

| #define PCIE\_CONF\_CLASSREV\_PROGIF | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) >> 8) & 0xFFU)

## [◆ ](#gae102d89e2fb359c3c9dda6b35d9ecd4f)PCIE\_CONF\_CLASSREV\_REV

| #define PCIE\_CONF\_CLASSREV\_REV | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

((w) & 0xFFU)

## [◆ ](#ga769e486c00a8ceda4ddb3f3eebc09c59)PCIE\_CONF\_CLASSREV\_SUBCLASS

| #define PCIE\_CONF\_CLASSREV\_SUBCLASS | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) >> 16) & 0xFFU)

## [◆ ](#ga2fc046f15e216337194e41480518c982)PCIE\_CONF\_CMDSTAT

| #define PCIE\_CONF\_CMDSTAT   1U /\* command/status register \*/ |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga7127f82d9c9b093b1056125ca1bb9d65)PCIE\_CONF\_CMDSTAT\_CAPS

| #define PCIE\_CONF\_CMDSTAT\_CAPS   0x00100000U /\* capabilities list \*/ |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga4712b7b75d9bf0098e6c80c69587ef86)PCIE\_CONF\_CMDSTAT\_INTERRUPT

| #define PCIE\_CONF\_CMDSTAT\_INTERRUPT   0x00080000U /\* interrupt status \*/ |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga6a9008421671f66ea9a6f11f87edd514)PCIE\_CONF\_CMDSTAT\_IO

| #define PCIE\_CONF\_CMDSTAT\_IO   0x00000001U /\* I/O access enable \*/ |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga8a770450f03bfb020f223e0fea96189d)PCIE\_CONF\_CMDSTAT\_MASTER

| #define PCIE\_CONF\_CMDSTAT\_MASTER   0x00000004U /\* bus master enable \*/ |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga24661608e9f66f79bbdcde9304b24820)PCIE\_CONF\_CMDSTAT\_MEM

| #define PCIE\_CONF\_CMDSTAT\_MEM   0x00000002U /\* mem access enable \*/ |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga491d796e2477816c8f8aac4c7b753e3d)PCIE\_CONF\_EXT\_CAP\_ID

| #define PCIE\_CONF\_EXT\_CAP\_ID | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

((w) & 0xFFFFU)

## [◆ ](#gad0fa4f22781b85d06321192338088073)PCIE\_CONF\_EXT\_CAP\_NEXT

| #define PCIE\_CONF\_EXT\_CAP\_NEXT | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) >> 20) & 0xFFFU)

## [◆ ](#gaf22a73f116325d3509cde1f83b3d7900)PCIE\_CONF\_EXT\_CAP\_VER

| #define PCIE\_CONF\_EXT\_CAP\_VER | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) >> 16) & 0xFU)

## [◆ ](#gabeb1434679b73c98f2ada475c8502e32)PCIE\_CONF\_EXT\_CAPPTR

| #define PCIE\_CONF\_EXT\_CAPPTR   64U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga2b694e339f9be5982605ed53e022ae06)PCIE\_CONF\_ID

| #define PCIE\_CONF\_ID   0U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#gaa5a2c8849e4cac05ee584827aedbfb93)PCIE\_CONF\_INTR

| #define PCIE\_CONF\_INTR   15U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga5c2f2d310dc6a73530b6909ce2c2536e)PCIE\_CONF\_INTR\_IRQ

| #define PCIE\_CONF\_INTR\_IRQ | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

((w) & 0xFFU)

## [◆ ](#ga995ca5b5146669c9234d3cdd596b715c)PCIE\_CONF\_INTR\_IRQ\_NONE

| #define PCIE\_CONF\_INTR\_IRQ\_NONE   0xFFU /\* no interrupt routed \*/ |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga9462e002a9d4b49ef7e7c97942765215)PCIE\_CONF\_MULTIFUNCTION

| #define PCIE\_CONF\_MULTIFUNCTION | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) & 0x00800000U) != 0U)

## [◆ ](#ga43ad620ae5a3041f0d7553de03c6da84)PCIE\_CONF\_TYPE

| #define PCIE\_CONF\_TYPE   3U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#gab7c494d71f6490e483b642a02ef90930)PCIE\_CONF\_TYPE\_BRIDGE

| #define PCIE\_CONF\_TYPE\_BRIDGE | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) & 0x007F0000U) != 0U)

## [◆ ](#gae9587843cac6247fcfb72f985ff4b030)PCIE\_CONF\_TYPE\_CARDBUS\_BRIDGE

| #define PCIE\_CONF\_TYPE\_CARDBUS\_BRIDGE   0x2U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga0580b798e6498097573c1eb0f2c6d2b1)PCIE\_CONF\_TYPE\_GET

| #define PCIE\_CONF\_TYPE\_GET | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) >> 16) & 0x7F)

## [◆ ](#ga90e8a996bf491fda870ff29b119a5242)PCIE\_CONF\_TYPE\_PCI\_BRIDGE

| #define PCIE\_CONF\_TYPE\_PCI\_BRIDGE   0x1U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga8b76fee3c256914a5044313ff9805969)PCIE\_CONF\_TYPE\_STANDARD

| #define PCIE\_CONF\_TYPE\_STANDARD   0x0U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga304228150cd8ec56aa24be468e9d79bf)PCIE\_DT\_ID

| #define PCIE\_DT\_ID | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

[PCIE\_ID](dt-bindings_2pcie_2pcie_8h.md#af3107df4821c35c5f217a2b8bc49bce6)([DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, vendor\_id, 0xffff), \

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, device\_id, 0xffff))

[PCIE\_ID](dt-bindings_2pcie_2pcie_8h.md#af3107df4821c35c5f217a2b8bc49bce6)

#define PCIE\_ID(vend, dev)

**Definition** pcie.h:29

Get the PCIe Vendor and Device ID for a node.

Parameters
:   | node\_id | DTS node identifier |
    | --- | --- |

Returns
:   The VID/DID combination as [pcie\_id\_t](#ga30840d0e312e35f00790660193fd4c04)

## [◆ ](#ga3e89194346fa9b945f1873380c527cee)PCIE\_DT\_INST\_ID

| #define PCIE\_DT\_INST\_ID | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

[PCIE\_DT\_ID](#ga304228150cd8ec56aa24be468e9d79bf)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

Get the PCIe Vendor and Device ID for a node.

This is equivalent to [PCIE\_DT\_ID(DT\_DRV\_INST(inst))](#ga304228150cd8ec56aa24be468e9d79bf)

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |

Returns
:   The VID/DID combination as [pcie\_id\_t](#ga30840d0e312e35f00790660193fd4c04)

## [◆ ](#ga7b500200f090dc95322fe670bf64628d)PCIE\_HOST\_CONTROLLER

| #define PCIE\_HOST\_CONTROLLER | ( |  | *n* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

[PCIE\_BDF](dt-bindings_2pcie_2pcie_8h.md#a09a440a45623a282c23eaa2cfeef63d2)(0, 0, n)

[PCIE\_BDF](dt-bindings_2pcie_2pcie_8h.md#a09a440a45623a282c23eaa2cfeef63d2)

#define PCIE\_BDF(bus, dev, func)

**Definition** pcie.h:59

Get the BDF for a given PCI host controller.

This macro is useful when the PCI host controller behind [PCIE\_BDF(0, 0, 0)](dt-bindings_2pcie_2pcie_8h.md#a09a440a45623a282c23eaa2cfeef63d2) indicates a multifunction device. In such a case each function of this endpoint is a potential host controller itself.

Parameters
:   | n | Bus number |
    | --- | --- |

Returns
:   BDF value of the given host controller

## [◆ ](#gac7d5c41ea3c8999126d89d95961b430b)PCIE\_ID\_IS\_VALID

| #define PCIE\_ID\_IS\_VALID | ( |  | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

((id != [PCIE\_ID\_NONE](dt-bindings_2pcie_2pcie_8h.md#a23ce79d01609cb14f0cd4b2298e13b14)) && \

(id != [PCIE\_ID](dt-bindings_2pcie_2pcie_8h.md#af3107df4821c35c5f217a2b8bc49bce6)(0x0000, 0x0000)) && \

(id != [PCIE\_ID](dt-bindings_2pcie_2pcie_8h.md#af3107df4821c35c5f217a2b8bc49bce6)(0xFFFF, 0x0000)) && \

(id != [PCIE\_ID](dt-bindings_2pcie_2pcie_8h.md#af3107df4821c35c5f217a2b8bc49bce6)(0x0000, 0xFFFF)))

[PCIE\_ID\_NONE](dt-bindings_2pcie_2pcie_8h.md#a23ce79d01609cb14f0cd4b2298e13b14)

#define PCIE\_ID\_NONE

**Definition** pcie.h:36

## [◆ ](#ga34f56e87ececf58b285e91341cd27d23)PCIE\_IO\_BASE

| #define PCIE\_IO\_BASE | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

((w) & 0xffUL)

## [◆ ](#gafc1acf0ac9b46629497c7a552f5650ce)PCIE\_IO\_BASE\_LIMIT\_UPPER

| #define PCIE\_IO\_BASE\_LIMIT\_UPPER   12U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga88669a9ca40294cee41bb163a908737f)PCIE\_IO\_BASE\_LIMIT\_UPPER\_VAL

| #define PCIE\_IO\_BASE\_LIMIT\_UPPER\_VAL | ( |  | *iobu*, |
| --- | --- | --- | --- |
|  |  |  | *iolu* ) |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((iobu) & 0xffffUL) | \

(((iolu) & 0xffffUL) << 16))

## [◆ ](#ga8bf9a619d6d83cbb009a7f18b501db92)PCIE\_IO\_BASE\_UPPER

| #define PCIE\_IO\_BASE\_UPPER | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

((w) & 0xffffUL)

## [◆ ](#ga4629a222d00917b2e3cad6aadbfd2ec1)PCIE\_IO\_LIMIT

| #define PCIE\_IO\_LIMIT | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) >> 8) & 0xffUL)

## [◆ ](#ga76a59c926f2760a04c4d8439cb227fe2)PCIE\_IO\_LIMIT\_UPPER

| #define PCIE\_IO\_LIMIT\_UPPER | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) >> 16) & 0xffffUL)

## [◆ ](#ga111eab92400e240ec5b7f08caf1b8a87)PCIE\_IO\_SEC\_STATUS

| #define PCIE\_IO\_SEC\_STATUS   7U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga61f05b2c4cd5c672af43960b320e33bc)PCIE\_IO\_SEC\_STATUS\_VAL

| #define PCIE\_IO\_SEC\_STATUS\_VAL | ( |  | *iob*, |
| --- | --- | --- | --- |
|  |  |  | *iol*, |
|  |  |  | *sec\_status* ) |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((iob) & 0xffUL) | \

(((iol) & 0xffUL) << 8) | \

(((sec\_status) & 0xffffUL) << 16))

## [◆ ](#ga6616499a7be31d40af31bb8134aa4a51)PCIE\_IRQ\_CONNECT

| #define PCIE\_IRQ\_CONNECT | ( |  | *bdf\_p*, |
| --- | --- | --- | --- |
|  |  |  | *irq\_p*, |
|  |  |  | *priority\_p*, |
|  |  |  | *isr\_p*, |
|  |  |  | *isr\_param\_p*, |
|  |  |  | *flags\_p* ) |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

ARCH\_PCIE\_IRQ\_CONNECT(bdf\_p, irq\_p, priority\_p, \

isr\_p, isr\_param\_p, flags\_p)

Initialize an interrupt handler for a PCIe endpoint IRQ.

This routine is only meant to be used by drivers using PCIe bus and having fixed or MSI based IRQ (so no runtime detection of the IRQ). In case of runtime detection see [pcie\_connect\_dynamic\_irq()](#ga14970194de1024a1a4669b69f932a4f5)

Parameters
:   | bdf\_p | PCIe endpoint BDF |
    | --- | --- |
    | irq\_p | IRQ line number. |
    | priority\_p | Interrupt priority. |
    | isr\_p | Address of interrupt service routine. |
    | isr\_param\_p | Parameter passed to interrupt service routine. |
    | flags\_p | Architecture-specific IRQ configuration flags.. |

## [◆ ](#ga1ce9e061b5a773f3ee74f78893174f9e)PCIE\_MAX\_BUS

| #define PCIE\_MAX\_BUS   (0xFFFFFFFFU & [PCIE\_BDF\_BUS\_MASK](dt-bindings_2pcie_2pcie_8h.md#a193dd359d7a96bdd904662717c7fbf6d)) |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga8809359a58c787a939d01f25e12ac51a)PCIE\_MAX\_DEV

| #define PCIE\_MAX\_DEV   (0xFFFFFFFFU & [PCIE\_BDF\_DEV\_MASK](dt-bindings_2pcie_2pcie_8h.md#a85cc69963a93046bda0f1594803af9eb)) |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#gaee8ddb7b7b1354fd5c835b67321f286b)PCIE\_MAX\_FUNC

| #define PCIE\_MAX\_FUNC   (0xFFFFFFFFU & [PCIE\_BDF\_FUNC\_MASK](dt-bindings_2pcie_2pcie_8h.md#ab481360fa29cf086cc5369e6f1860a5f)) |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#gacd6be1e38666a6a137b1654007cf293a)PCIE\_MEM\_BASE

| #define PCIE\_MEM\_BASE | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

((w) & 0xffffUL)

## [◆ ](#ga6fbcd3f523deb069aa31bcd31973d00b)PCIE\_MEM\_BASE\_LIMIT

| #define PCIE\_MEM\_BASE\_LIMIT   8U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga93a6dbe27d3d11be29397ae80c58a589)PCIE\_MEM\_BASE\_LIMIT\_VAL

| #define PCIE\_MEM\_BASE\_LIMIT\_VAL | ( |  | *memb*, |
| --- | --- | --- | --- |
|  |  |  | *meml* ) |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((memb) & 0xffffUL) | \

(((meml) & 0xffffUL) << 16))

## [◆ ](#ga9f5d23ad0674aed0bf5c1869621de303)PCIE\_MEM\_LIMIT

| #define PCIE\_MEM\_LIMIT | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) >> 16) & 0xffffUL)

## [◆ ](#ga5f7aa0fc063ec072bf7e89fca603c825)PCIE\_PREFETCH\_BASE

| #define PCIE\_PREFETCH\_BASE | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

((w) & 0xffffUL)

## [◆ ](#ga8dd5906e8d735210d9f8ca25d39684b4)PCIE\_PREFETCH\_BASE\_LIMIT

| #define PCIE\_PREFETCH\_BASE\_LIMIT   9U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga02b269663488e7c7469415622390ce55)PCIE\_PREFETCH\_BASE\_LIMIT\_VAL

| #define PCIE\_PREFETCH\_BASE\_LIMIT\_VAL | ( |  | *pmemb*, |
| --- | --- | --- | --- |
|  |  |  | *pmeml* ) |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((pmemb) & 0xffffUL) | \

(((pmeml) & 0xffffUL) << 16))

## [◆ ](#ga6ebdd02e0599f33becb6cf413be0a8cd)PCIE\_PREFETCH\_BASE\_UPPER

| #define PCIE\_PREFETCH\_BASE\_UPPER   10U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#gaf0a18504a4eb2061d1afc90fc7b8ee21)PCIE\_PREFETCH\_LIMIT

| #define PCIE\_PREFETCH\_LIMIT | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) >> 16) & 0xffffUL)

## [◆ ](#gab0eda55fd8c2c4025dc4350ef946a61b)PCIE\_PREFETCH\_LIMIT\_UPPER

| #define PCIE\_PREFETCH\_LIMIT\_UPPER   11U |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

## [◆ ](#ga804b34fd47ba065287e0257fac84ac35)PCIE\_SEC\_STATUS

| #define PCIE\_SEC\_STATUS | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) >> 16) & 0xffffUL)

## [◆ ](#gaa05e49d0cafbe51b7742354470d07bd0)PCIE\_SECONDARY\_LATENCY\_TIMER

| #define PCIE\_SECONDARY\_LATENCY\_TIMER | ( |  | *w* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

**Value:**

(((w) >> 24) & 0xffUL)

## Typedef Documentation

## [◆ ](#gaf9748042a4f3c8d912d19df1ccf737fb)pcie\_bdf\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

A unique PCI(e) endpoint (bus, device, function).

A PCI(e) endpoint is uniquely identified topologically using a (bus, device, function) tuple. The internal structure is documented in include/dt-bindings/pcie/pcie.h: see [PCIE\_BDF()](dt-bindings_2pcie_2pcie_8h.md#a09a440a45623a282c23eaa2cfeef63d2) and friends, since these tuples are referenced from devicetree.

## [◆ ](#ga30840d0e312e35f00790660193fd4c04)pcie\_id\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pcie\_id\_t](#ga30840d0e312e35f00790660193fd4c04) |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

A unique PCI(e) identifier (vendor ID, device ID).

The PCIE\_CONF\_ID register for each endpoint is a (vendor ID, device ID) pair, which is meant to tell the system what the PCI(e) endpoint is. Again, look to PCIE\_ID\_\* macros in include/dt-bindings/pcie/pcie.h for more.

## [◆ ](#ga922580e4fb6200ef75425bb54801ceda)pcie\_scan\_cb\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* pcie\_scan\_cb\_t) ([pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [pcie\_id\_t](#ga30840d0e312e35f00790660193fd4c04) id, void \*cb\_data) |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

Callback type used for scanning for PCI endpoints.

Parameters
:   | bdf | BDF value for a found endpoint. |
    | --- | --- |
    | id | Vendor & Device ID for the found endpoint. |
    | cb\_data | Custom, use case specific data. |

Returns
:   true to continue scanning, false to stop scanning.

## Enumeration Type Documentation

## [◆ ](#gabe00c00fc0af29786c3b42f22f82aecf)anonymous enum

| anonymous enum |
| --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

| Enumerator | |
| --- | --- |
| PCIE\_SCAN\_RECURSIVE | Scan all available PCI host controllers and sub-busses. |
| PCIE\_SCAN\_CB\_ALL | Do the callback for all endpoint types, including bridges. |

## Function Documentation

## [◆ ](#gad69ae431e5f91992f071dee9d7fa9110)pcie\_alloc\_irq()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int pcie\_alloc\_irq | ( | [pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

Allocate an IRQ for an endpoint.

This function first checks the IRQ register and if it contains a valid value this is returned. If the register does not contain a valid value allocation of a new one is attempted. Such function is only exposed if CONFIG\_PCIE\_CONTROLLER is unset. It is thus available where architecture tied dynamic IRQ allocation for PCIe device makes sense.

Parameters
:   | bdf | the PCI(e) endpoint |
    | --- | --- |

Returns
:   the IRQ number, or PCIE\_CONF\_INTR\_IRQ\_NONE if allocation failed.

## [◆ ](#gaad76dbfd3d53d812db092e2029c65fea)pcie\_bdf\_lookup()

| | [pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) pcie\_bdf\_lookup | ( | [pcie\_id\_t](#ga30840d0e312e35f00790660193fd4c04) | *id* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

Look up the BDF based on PCI(e) vendor & device ID.

This function is used to look up the BDF for a device given its vendor and device ID.

**[Deprecated](deprecated.md#_deprecated000002)**

See also
:   [DEVICE\_PCIE\_DECLARE](#gad0b870d891458c4ebd7ab2ac1c372eec)

Parameters
:   | id | PCI(e) vendor & device ID encoded using [PCIE\_ID()](dt-bindings_2pcie_2pcie_8h.md#af3107df4821c35c5f217a2b8bc49bce6) |
    | --- | --- |

Returns
:   The BDF for the device, or PCIE\_BDF\_NONE if it was not found

## [◆ ](#ga10ecc667c564548e4ddf3ca4374242b5)pcie\_conf\_read()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pcie\_conf\_read | ( | [pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reg* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

Read a 32-bit word from an endpoint's configuration space.

This function is exported by the arch/SoC/board code.

Parameters
:   | bdf | PCI(e) endpoint |
    | --- | --- |
    | reg | the configuration word index (not address) |

Returns
:   the word read (0xFFFFFFFFU if nonexistent endpoint or word)

## [◆ ](#ga47a2e88935e04330d449db5463d9f21a)pcie\_conf\_write()

| | void pcie\_conf\_write | ( | [pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reg*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

Write a 32-bit word to an endpoint's configuration space.

This function is exported by the arch/SoC/board code.

Parameters
:   | bdf | PCI(e) endpoint |
    | --- | --- |
    | reg | the configuration word index (not address) |
    | data | the value to write |

## [◆ ](#ga14970194de1024a1a4669b69f932a4f5)pcie\_connect\_dynamic\_irq()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pcie\_connect\_dynamic\_irq | ( | [pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq*, | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *priority*, | |  |  | void(\* | *routine*)(const void \*parameter), | |  |  | const void \* | *parameter*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

Dynamically connect a PCIe endpoint IRQ to an ISR handler.

Parameters
:   | bdf | the PCI endpoint to examine |
    | --- | --- |
    | irq | the IRQ to connect (see [pcie\_alloc\_irq()](#gad69ae431e5f91992f071dee9d7fa9110)) |
    | priority | priority of the IRQ |
    | routine | the ISR handler to connect to the IRQ |
    | parameter | the parameter to provide to the handler |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | IRQ connection flags |

Returns
:   true if connected, false otherwise

## [◆ ](#ga56e724c9bfd7f44c550ccff1b46978a8)pcie\_get\_cap()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pcie\_get\_cap | ( | [pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *cap\_id* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

Find a PCI(e) capability in an endpoint's configuration space.

Parameters
:   | bdf | the PCI endpoint to examine |
    | --- | --- |
    | cap\_id | the capability ID of interest |

Returns
:   the index of the configuration word, or 0 if no capability.

## [◆ ](#ga5db0d2a5946d20406070b47a1a7acf21)pcie\_get\_ext\_cap()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pcie\_get\_ext\_cap | ( | [pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *cap\_id* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

Find an Extended PCI(e) capability in an endpoint's configuration space.

Parameters
:   | bdf | the PCI endpoint to examine |
    | --- | --- |
    | cap\_id | the capability ID of interest |

Returns
:   the index of the configuration word, or 0 if no capability.

## [◆ ](#ga3523bbdfd67d4b56cf6cd86c98c830bf)pcie\_get\_iobar()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pcie\_get\_iobar | ( | [pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *bar\_index*, | |  |  | struct [pcie\_bar](structpcie__bar.md) \* | *iobar* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

Get the I/O BAR at a specific BAR index.

Parameters
:   | bdf | the PCI(e) endpoint |
    | --- | --- |
    | bar\_index | 0-based BAR index |
    | iobar | Pointer to struct [pcie\_bar](structpcie__bar.md) |

Returns
:   true if the I/O BAR was found and is valid, false otherwise

## [◆ ](#gaed7fef462ba02a22b5875b1a2c0d965a)pcie\_get\_irq()

| | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int pcie\_get\_irq | ( | [pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf* | ) |  | | --- | --- | --- | --- | --- | --- | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

Return the IRQ assigned by the firmware/board to an endpoint.

Parameters
:   | bdf | the PCI(e) endpoint |
    | --- | --- |

Returns
:   the IRQ number, or PCIE\_CONF\_INTR\_IRQ\_NONE if unknown.

## [◆ ](#gadeb891fbb5b900eb60de22d40afe355e)pcie\_get\_mbar()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pcie\_get\_mbar | ( | [pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *bar\_index*, | |  |  | struct [pcie\_bar](structpcie__bar.md) \* | *mbar* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

Get the MBAR at a specific BAR index.

Parameters
:   | bdf | the PCI(e) endpoint |
    | --- | --- |
    | bar\_index | 0-based BAR index |
    | mbar | Pointer to struct [pcie\_bar](structpcie__bar.md) |

Returns
:   true if the mbar was found and is valid, false otherwise

## [◆ ](#gafb69216f9224a9040b1f0b58eb286196)pcie\_irq\_enable()

| | void pcie\_irq\_enable | ( | [pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *irq* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

Enable the PCI(e) endpoint to generate the specified IRQ.

Parameters
:   | bdf | the PCI(e) endpoint |
    | --- | --- |
    | irq | the IRQ to generate |

If MSI is enabled and the endpoint supports it, the endpoint will be configured to generate the specified IRQ via MSI. Otherwise, it is assumed that the IRQ has been routed by the boot firmware to the specified IRQ, and the IRQ is enabled (at the I/O APIC, or wherever appropriate).

## [◆ ](#ga38df5e6054de59f1bc21e89a2701e998)pcie\_probe()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pcie\_probe | ( | [pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, | | --- | --- | --- | --- | |  |  | [pcie\_id\_t](#ga30840d0e312e35f00790660193fd4c04) | *id* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

Probe for the presence of a PCI(e) endpoint.

**[Deprecated](deprecated.md#_deprecated000003)**

See also
:   [DEVICE\_PCIE\_DECLARE](#gad0b870d891458c4ebd7ab2ac1c372eec)

Parameters
:   | bdf | the endpoint to probe |
    | --- | --- |
    | id | the endpoint ID to expect, or PCIE\_ID\_NONE for "any device" |

Returns
:   true if the device is present, false otherwise

## [◆ ](#gaa81d98a9ee58062c02be576fb0dfefd9)pcie\_probe\_iobar()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pcie\_probe\_iobar | ( | [pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *index*, | |  |  | struct [pcie\_bar](structpcie__bar.md) \* | *iobar* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

Probe the nth I/O BAR address assigned to an endpoint.

Parameters
:   | bdf | the PCI(e) endpoint |
    | --- | --- |
    | index | (0-based) index |
    | iobar | Pointer to struct [pcie\_bar](structpcie__bar.md) |

Returns
:   true if the I/O BAR was found and is valid, false otherwise

A PCI(e) endpoint has 0 or more I/O regions. This function allows the caller to enumerate them by calling with index=0..n. Value of n has to be below 6, as there is a maximum of 6 BARs. The indices are order-preserving with respect to the endpoint BARs: e.g., index 0 will return the lowest-numbered I/O BAR on the endpoint.

## [◆ ](#gad8463013e51c4ddcca7b5f805f918685)pcie\_probe\_mbar()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) pcie\_probe\_mbar | ( | [pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, | | --- | --- | --- | --- | |  |  | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *index*, | |  |  | struct [pcie\_bar](structpcie__bar.md) \* | *mbar* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

Probe the nth MMIO address assigned to an endpoint.

Parameters
:   | bdf | the PCI(e) endpoint |
    | --- | --- |
    | index | (0-based) index |
    | mbar | Pointer to struct [pcie\_bar](structpcie__bar.md) |

Returns
:   true if the mbar was found and is valid, false otherwise

A PCI(e) endpoint has 0 or more memory-mapped regions. This function allows the caller to enumerate them by calling with index=0..n. Value of n has to be below 6, as there is a maximum of 6 BARs. The indices are order-preserving with respect to the endpoint BARs: e.g., index 0 will return the lowest-numbered memory BAR on the endpoint.

## [◆ ](#ga9a7b3c202f91d37fe8445d5016f4c6ab)pcie\_scan()

| int pcie\_scan | ( | const struct [pcie\_scan\_opt](structpcie__scan__opt.md) \* | *opt* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

Scan for PCIe devices.

Scan the PCI bus (or busses) for available endpoints.

Parameters
:   | opt | Options determining how to perform the scan. |
    | --- | --- |

Returns
:   0 on success, negative POSIX error number on failure.

## [◆ ](#ga3516fec89df75eb3d77f54193059fc5c)pcie\_set\_cmd()

| | void pcie\_set\_cmd | ( | [pcie\_bdf\_t](#gaf9748042a4f3c8d912d19df1ccf737fb) | *bdf*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *bits*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *on* ) | | extern |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[pcie.h](drivers_2pcie_2pcie_8h.md)>`

Set or reset bits in the endpoint command/status register.

Parameters
:   | bdf | the PCI(e) endpoint |
    | --- | --- |
    | bits | the powerset of bits of interest |
    | on | use true to set bits, false to reset them |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
