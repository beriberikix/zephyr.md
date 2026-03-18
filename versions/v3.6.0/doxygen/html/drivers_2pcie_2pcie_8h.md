---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2pcie_2pcie_8h.html
original_path: doxygen/html/drivers_2pcie_2pcie_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pcie.h File Reference

`#include <stddef.h>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`  
`#include <[zephyr/dt-bindings/pcie/pcie.h](dt-bindings_2pcie_2pcie_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](drivers_2pcie_2pcie_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [pcie\_dev](structpcie__dev.md) |
| struct | [pcie\_bar](structpcie__bar.md) |
| struct | [pcie\_scan\_opt](structpcie__scan__opt.md) |
|  | Options for performing a scan for PCI devices. [More...](structpcie__scan__opt.md#details) |

| Macros | |
| --- | --- |
| #define | [PCIE\_ID\_IS\_VALID](group__pcie__host__interface.md#gac7d5c41ea3c8999126d89d95961b430b)(id) |
| #define | [PCIE\_DT\_ID](group__pcie__host__interface.md#ga304228150cd8ec56aa24be468e9d79bf)(node\_id) |
|  | Get the PCIe Vendor and Device ID for a node. |
| #define | [PCIE\_DT\_INST\_ID](group__pcie__host__interface.md#ga3e89194346fa9b945f1873380c527cee)(inst) |
|  | Get the PCIe Vendor and Device ID for a node. |
| #define | [DEVICE\_PCIE\_DECLARE](group__pcie__host__interface.md#gad0b870d891458c4ebd7ab2ac1c372eec)(node\_id) |
|  | Declare a PCIe context variable for a DTS node. |
| #define | [DEVICE\_PCIE\_INST\_DECLARE](group__pcie__host__interface.md#gade2f1f53701b1d80b5593045e977e4d6)(inst) |
|  | Declare a PCIe context variable for a DTS node. |
| #define | [DEVICE\_PCIE\_INIT](group__pcie__host__interface.md#gab6c472838e13293980cd53c65aaa3c47)(node\_id, name) |
|  | Initialize a named struct member to point at a PCIe context. |
| #define | [DEVICE\_PCIE\_INST\_INIT](group__pcie__host__interface.md#gac175df702e85f599b28b7a567c64d146)(inst, name) |
|  | Initialize a named struct member to point at a PCIe context. |
| #define | [PCIE\_HOST\_CONTROLLER](group__pcie__host__interface.md#ga7b500200f090dc95322fe670bf64628d)(n) |
|  | Get the BDF for a given PCI host controller. |
| #define | [PCIE\_CONF\_CAPPTR](group__pcie__host__interface.md#gaad23a180cf411bd8fa10027b9f16eb91)   13U /\* capabilities pointer \*/ |
| #define | [PCIE\_CONF\_CAPPTR\_FIRST](group__pcie__host__interface.md#gabe5832ddf2b8399e8f672564ce85ad7e)(w) |
| #define | [PCIE\_CONF\_CAP\_ID](group__pcie__host__interface.md#gaa888f548db209011f1cf5c87b1f351b8)(w) |
| #define | [PCIE\_CONF\_CAP\_NEXT](group__pcie__host__interface.md#ga98476f56fe7d46b6bee505e0db1c1906)(w) |
| #define | [PCIE\_CONF\_EXT\_CAPPTR](group__pcie__host__interface.md#gabeb1434679b73c98f2ada475c8502e32)   64U |
| #define | [PCIE\_CONF\_EXT\_CAP\_ID](group__pcie__host__interface.md#ga491d796e2477816c8f8aac4c7b753e3d)(w) |
| #define | [PCIE\_CONF\_EXT\_CAP\_VER](group__pcie__host__interface.md#gaf22a73f116325d3509cde1f83b3d7900)(w) |
| #define | [PCIE\_CONF\_EXT\_CAP\_NEXT](group__pcie__host__interface.md#gad0fa4f22781b85d06321192338088073)(w) |
| #define | [PCIE\_CONF\_ID](group__pcie__host__interface.md#ga2b694e339f9be5982605ed53e022ae06)   0U |
| #define | [PCIE\_CONF\_CMDSTAT](group__pcie__host__interface.md#ga2fc046f15e216337194e41480518c982)   1U /\* command/status register \*/ |
| #define | [PCIE\_CONF\_CMDSTAT\_IO](group__pcie__host__interface.md#ga6a9008421671f66ea9a6f11f87edd514)   0x00000001U /\* I/O access enable \*/ |
| #define | [PCIE\_CONF\_CMDSTAT\_MEM](group__pcie__host__interface.md#ga24661608e9f66f79bbdcde9304b24820)   0x00000002U /\* mem access enable \*/ |
| #define | [PCIE\_CONF\_CMDSTAT\_MASTER](group__pcie__host__interface.md#ga8a770450f03bfb020f223e0fea96189d)   0x00000004U /\* bus master enable \*/ |
| #define | [PCIE\_CONF\_CMDSTAT\_INTERRUPT](group__pcie__host__interface.md#ga4712b7b75d9bf0098e6c80c69587ef86)   0x00080000U /\* interrupt status \*/ |
| #define | [PCIE\_CONF\_CMDSTAT\_CAPS](group__pcie__host__interface.md#ga7127f82d9c9b093b1056125ca1bb9d65)   0x00100000U /\* capabilities list \*/ |
| #define | [PCIE\_CONF\_CLASSREV](group__pcie__host__interface.md#ga6946589a87e364c4710fba1dded553dc)   2U /\* class/revision register \*/ |
| #define | [PCIE\_CONF\_CLASSREV\_CLASS](group__pcie__host__interface.md#gace40af940c01af2876e6fe8d599677bc)(w) |
| #define | [PCIE\_CONF\_CLASSREV\_SUBCLASS](group__pcie__host__interface.md#ga769e486c00a8ceda4ddb3f3eebc09c59)(w) |
| #define | [PCIE\_CONF\_CLASSREV\_PROGIF](group__pcie__host__interface.md#ga36f77d220a11a9a30c4656e7f616ec05)(w) |
| #define | [PCIE\_CONF\_CLASSREV\_REV](group__pcie__host__interface.md#gae102d89e2fb359c3c9dda6b35d9ecd4f)(w) |
| #define | [PCIE\_CONF\_TYPE](group__pcie__host__interface.md#ga43ad620ae5a3041f0d7553de03c6da84)   3U |
| #define | [PCIE\_CONF\_MULTIFUNCTION](group__pcie__host__interface.md#ga9462e002a9d4b49ef7e7c97942765215)(w) |
| #define | [PCIE\_CONF\_TYPE\_BRIDGE](group__pcie__host__interface.md#gab7c494d71f6490e483b642a02ef90930)(w) |
| #define | [PCIE\_CONF\_TYPE\_GET](group__pcie__host__interface.md#ga0580b798e6498097573c1eb0f2c6d2b1)(w) |
| #define | [PCIE\_CONF\_TYPE\_STANDARD](group__pcie__host__interface.md#ga8b76fee3c256914a5044313ff9805969)   0x0U |
| #define | [PCIE\_CONF\_TYPE\_PCI\_BRIDGE](group__pcie__host__interface.md#ga90e8a996bf491fda870ff29b119a5242)   0x1U |
| #define | [PCIE\_CONF\_TYPE\_CARDBUS\_BRIDGE](group__pcie__host__interface.md#gae9587843cac6247fcfb72f985ff4b030)   0x2U |
| #define | [PCIE\_CONF\_BAR0](group__pcie__host__interface.md#gadfd21197ccd78d7bfb549fbb6f7070ff)   4U |
| #define | [PCIE\_CONF\_BAR1](group__pcie__host__interface.md#ga77e43c6060febf8a5b8439c7fc940a1f)   5U |
| #define | [PCIE\_CONF\_BAR2](group__pcie__host__interface.md#ga90040a3b78c5f5563f2f123e9fb05dd8)   6U |
| #define | [PCIE\_CONF\_BAR3](group__pcie__host__interface.md#ga05b9be5537cf1a4f3994c1a2c82282a1)   7U |
| #define | [PCIE\_CONF\_BAR4](group__pcie__host__interface.md#ga51dbf953128b6a464bf50cfa459626e7)   8U |
| #define | [PCIE\_CONF\_BAR5](group__pcie__host__interface.md#ga84fb2d49dd14438a9ff12a8eeb5bca60)   9U |
| #define | [PCIE\_CONF\_BAR\_IO](group__pcie__host__interface.md#ga2f4020ce7fec0e3b5c9b121951468b70)(w) |
| #define | [PCIE\_CONF\_BAR\_MEM](group__pcie__host__interface.md#ga6018ef2d851fd6a64a1ad4dde956f4c9)(w) |
| #define | [PCIE\_CONF\_BAR\_64](group__pcie__host__interface.md#ga6d2644d85b7bfbf9a526e6d54096982d)(w) |
| #define | [PCIE\_CONF\_BAR\_ADDR](group__pcie__host__interface.md#gaf163a00f52cc96bc7694e4e7e7a8d1fe)(w) |
| #define | [PCIE\_CONF\_BAR\_IO\_ADDR](group__pcie__host__interface.md#gabe49cc62101a531ca9e26b0290218797)(w) |
| #define | [PCIE\_CONF\_BAR\_FLAGS](group__pcie__host__interface.md#ga23c45457ec77c6fd2e1977710f6edf28)(w) |
| #define | [PCIE\_CONF\_BAR\_NONE](group__pcie__host__interface.md#ga296141fc89700213899b6463e1166477)   0U |
| #define | [PCIE\_CONF\_BAR\_INVAL](group__pcie__host__interface.md#ga65e8ddebc6d25b51940ae647f81deca1)   0xFFFFFFF0U |
| #define | [PCIE\_CONF\_BAR\_INVAL64](group__pcie__host__interface.md#ga8e1968a28791ed0529d622f32e6fad6c)   0xFFFFFFFFFFFFFFF0UL |
| #define | [PCIE\_CONF\_BAR\_INVAL\_FLAGS](group__pcie__host__interface.md#gafd74fe08ef11c685775433236d0fd734)(w) |
| #define | [PCIE\_BUS\_NUMBER](group__pcie__host__interface.md#gaac6d5d5eb2ff10b6d85b3bb3efb0ce6e)   6U |
| #define | [PCIE\_BUS\_PRIMARY\_NUMBER](group__pcie__host__interface.md#ga4c0dbee39acf51c94b5ececba150f8d0)(w) |
| #define | [PCIE\_BUS\_SECONDARY\_NUMBER](group__pcie__host__interface.md#ga61cd874c47de3545ca2ffa1eecd7eb42)(w) |
| #define | [PCIE\_BUS\_SUBORDINATE\_NUMBER](group__pcie__host__interface.md#ga0be93727f18869b7a486e42eac47fa2d)(w) |
| #define | [PCIE\_SECONDARY\_LATENCY\_TIMER](group__pcie__host__interface.md#gaa05e49d0cafbe51b7742354470d07bd0)(w) |
| #define | [PCIE\_BUS\_NUMBER\_VAL](group__pcie__host__interface.md#ga784bc42d77fec195d794c29067bd988c)(prim, sec, sub, lat) |
| #define | [PCIE\_IO\_SEC\_STATUS](group__pcie__host__interface.md#ga111eab92400e240ec5b7f08caf1b8a87)   7U |
| #define | [PCIE\_IO\_BASE](group__pcie__host__interface.md#ga34f56e87ececf58b285e91341cd27d23)(w) |
| #define | [PCIE\_IO\_LIMIT](group__pcie__host__interface.md#ga4629a222d00917b2e3cad6aadbfd2ec1)(w) |
| #define | [PCIE\_SEC\_STATUS](group__pcie__host__interface.md#ga804b34fd47ba065287e0257fac84ac35)(w) |
| #define | [PCIE\_IO\_SEC\_STATUS\_VAL](group__pcie__host__interface.md#ga61f05b2c4cd5c672af43960b320e33bc)(iob, iol, sec\_status) |
| #define | [PCIE\_MEM\_BASE\_LIMIT](group__pcie__host__interface.md#ga6fbcd3f523deb069aa31bcd31973d00b)   8U |
| #define | [PCIE\_MEM\_BASE](group__pcie__host__interface.md#gacd6be1e38666a6a137b1654007cf293a)(w) |
| #define | [PCIE\_MEM\_LIMIT](group__pcie__host__interface.md#ga9f5d23ad0674aed0bf5c1869621de303)(w) |
| #define | [PCIE\_MEM\_BASE\_LIMIT\_VAL](group__pcie__host__interface.md#ga93a6dbe27d3d11be29397ae80c58a589)(memb, meml) |
| #define | [PCIE\_PREFETCH\_BASE\_LIMIT](group__pcie__host__interface.md#ga8dd5906e8d735210d9f8ca25d39684b4)   9U |
| #define | [PCIE\_PREFETCH\_BASE](group__pcie__host__interface.md#ga5f7aa0fc063ec072bf7e89fca603c825)(w) |
| #define | [PCIE\_PREFETCH\_LIMIT](group__pcie__host__interface.md#gaf0a18504a4eb2061d1afc90fc7b8ee21)(w) |
| #define | [PCIE\_PREFETCH\_BASE\_LIMIT\_VAL](group__pcie__host__interface.md#ga02b269663488e7c7469415622390ce55)(pmemb, pmeml) |
| #define | [PCIE\_PREFETCH\_BASE\_UPPER](group__pcie__host__interface.md#ga6ebdd02e0599f33becb6cf413be0a8cd)   10U |
| #define | [PCIE\_PREFETCH\_LIMIT\_UPPER](group__pcie__host__interface.md#gab0eda55fd8c2c4025dc4350ef946a61b)   11U |
| #define | [PCIE\_IO\_BASE\_LIMIT\_UPPER](group__pcie__host__interface.md#gafc1acf0ac9b46629497c7a552f5650ce)   12U |
| #define | [PCIE\_IO\_BASE\_UPPER](group__pcie__host__interface.md#ga8bf9a619d6d83cbb009a7f18b501db92)(w) |
| #define | [PCIE\_IO\_LIMIT\_UPPER](group__pcie__host__interface.md#ga76a59c926f2760a04c4d8439cb227fe2)(w) |
| #define | [PCIE\_IO\_BASE\_LIMIT\_UPPER\_VAL](group__pcie__host__interface.md#ga88669a9ca40294cee41bb163a908737f)(iobu, iolu) |
| #define | [PCIE\_CONF\_INTR](group__pcie__host__interface.md#gaa5a2c8849e4cac05ee584827aedbfb93)   15U |
| #define | [PCIE\_CONF\_INTR\_IRQ](group__pcie__host__interface.md#ga5c2f2d310dc6a73530b6909ce2c2536e)(w) |
| #define | [PCIE\_CONF\_INTR\_IRQ\_NONE](group__pcie__host__interface.md#ga995ca5b5146669c9234d3cdd596b715c)   0xFFU /\* no interrupt routed \*/ |
| #define | [PCIE\_MAX\_BUS](group__pcie__host__interface.md#ga1ce9e061b5a773f3ee74f78893174f9e)   (0xFFFFFFFFU & [PCIE\_BDF\_BUS\_MASK](dt-bindings_2pcie_2pcie_8h.md#a193dd359d7a96bdd904662717c7fbf6d)) |
| #define | [PCIE\_MAX\_DEV](group__pcie__host__interface.md#ga8809359a58c787a939d01f25e12ac51a)   (0xFFFFFFFFU & [PCIE\_BDF\_DEV\_MASK](dt-bindings_2pcie_2pcie_8h.md#a85cc69963a93046bda0f1594803af9eb)) |
| #define | [PCIE\_MAX\_FUNC](group__pcie__host__interface.md#gaee8ddb7b7b1354fd5c835b67321f286b)   (0xFFFFFFFFU & [PCIE\_BDF\_FUNC\_MASK](dt-bindings_2pcie_2pcie_8h.md#ab481360fa29cf086cc5369e6f1860a5f)) |
| #define | [PCIE\_IRQ\_CONNECT](group__pcie__host__interface.md#ga6616499a7be31d40af31bb8134aa4a51)(bdf\_p, irq\_p, priority\_p, isr\_p, isr\_param\_p, flags\_p) |
|  | Initialize an interrupt handler for a PCIe endpoint IRQ. |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) |
|  | A unique PCI(e) endpoint (bus, device, function). |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pcie\_id\_t](group__pcie__host__interface.md#ga30840d0e312e35f00790660193fd4c04) |
|  | A unique PCI(e) identifier (vendor ID, device ID). |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [pcie\_scan\_cb\_t](group__pcie__host__interface.md#ga922580e4fb6200ef75425bb54801ceda)) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [pcie\_id\_t](group__pcie__host__interface.md#ga30840d0e312e35f00790660193fd4c04) id, void \*cb\_data) |
|  | Callback type used for scanning for PCI endpoints. |

| Enumerations | |
| --- | --- |
| enum | { [PCIE\_SCAN\_RECURSIVE](group__pcie__host__interface.md#ggabe00c00fc0af29786c3b42f22f82aecfa228932ef6533931a9ae55e37dc38f3c4) = BIT(0) , [PCIE\_SCAN\_CB\_ALL](group__pcie__host__interface.md#ggabe00c00fc0af29786c3b42f22f82aecfa3579c18ade658f55affd41bfd38f9072) = BIT(1) } |

| Functions | |
| --- | --- |
| [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) | [pcie\_bdf\_lookup](group__pcie__host__interface.md#gaad76dbfd3d53d812db092e2029c65fea) ([pcie\_id\_t](group__pcie__host__interface.md#ga30840d0e312e35f00790660193fd4c04) id) |
|  | Look up the BDF based on PCI(e) vendor & device ID. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pcie\_conf\_read](group__pcie__host__interface.md#ga10ecc667c564548e4ddf3ca4374242b5) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg) |
|  | Read a 32-bit word from an endpoint's configuration space. |
| void | [pcie\_conf\_write](group__pcie__host__interface.md#ga47a2e88935e04330d449db5463d9f21a) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reg, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
|  | Write a 32-bit word to an endpoint's configuration space. |
| int | [pcie\_scan](group__pcie__host__interface.md#ga9a7b3c202f91d37fe8445d5016f4c6ab) (const struct [pcie\_scan\_opt](structpcie__scan__opt.md) \*opt) |
|  | Scan for PCIe devices. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_probe](group__pcie__host__interface.md#ga38df5e6054de59f1bc21e89a2701e998) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [pcie\_id\_t](group__pcie__host__interface.md#ga30840d0e312e35f00790660193fd4c04) id) |
|  | Probe for the presence of a PCI(e) endpoint. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_get\_mbar](group__pcie__host__interface.md#gadeb891fbb5b900eb60de22d40afe355e) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int bar\_index, struct [pcie\_bar](structpcie__bar.md) \*mbar) |
|  | Get the MBAR at a specific BAR index. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_probe\_mbar](group__pcie__host__interface.md#gad8463013e51c4ddcca7b5f805f918685) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int index, struct [pcie\_bar](structpcie__bar.md) \*mbar) |
|  | Probe the nth MMIO address assigned to an endpoint. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_get\_iobar](group__pcie__host__interface.md#ga3523bbdfd67d4b56cf6cd86c98c830bf) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int bar\_index, struct [pcie\_bar](structpcie__bar.md) \*iobar) |
|  | Get the I/O BAR at a specific BAR index. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_probe\_iobar](group__pcie__host__interface.md#gaa81d98a9ee58062c02be576fb0dfefd9) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int index, struct [pcie\_bar](structpcie__bar.md) \*iobar) |
|  | Probe the nth I/O BAR address assigned to an endpoint. |
| void | [pcie\_set\_cmd](group__pcie__host__interface.md#ga3516fec89df75eb3d77f54193059fc5c) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bits, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) on) |
|  | Set or reset bits in the endpoint command/status register. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [pcie\_alloc\_irq](group__pcie__host__interface.md#gad69ae431e5f91992f071dee9d7fa9110) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf) |
|  | Allocate an IRQ for an endpoint. |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [pcie\_get\_irq](group__pcie__host__interface.md#gaed7fef462ba02a22b5875b1a2c0d965a) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf) |
|  | Return the IRQ assigned by the firmware/board to an endpoint. |
| void | [pcie\_irq\_enable](group__pcie__host__interface.md#gafb69216f9224a9040b1f0b58eb286196) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq) |
|  | Enable the PCI(e) endpoint to generate the specified IRQ. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pcie\_get\_cap](group__pcie__host__interface.md#ga56e724c9bfd7f44c550ccff1b46978a8) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cap\_id) |
|  | Find a PCI(e) capability in an endpoint's configuration space. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [pcie\_get\_ext\_cap](group__pcie__host__interface.md#ga5db0d2a5946d20406070b47a1a7acf21) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) cap\_id) |
|  | Find an Extended PCI(e) capability in an endpoint's configuration space. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [pcie\_connect\_dynamic\_irq](group__pcie__host__interface.md#ga14970194de1024a1a4669b69f932a4f5) ([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) bdf, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int irq, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int priority, void(\*routine)(const void \*parameter), const void \*parameter, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Dynamically connect a PCIe endpoint IRQ to an ISR handler. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pcie](dir_e35238db017d7f8b1976dc13f193be2d.md)
- [pcie.h](drivers_2pcie_2pcie_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
