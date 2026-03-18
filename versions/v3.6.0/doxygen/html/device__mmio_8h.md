---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/device__mmio_8h.html
original_path: doxygen/html/device__mmio_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

device\_mmio.h File Reference

`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/linker/sections.h](sections_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/kernel/mm.h](kernel_2mm_8h_source.md)>`  
`#include <[zephyr/sys/sys_io.h](sys_2sys__io_8h_source.md)>`

[Go to the source code of this file.](device__mmio_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DEVICE\_MMIO\_IS\_IN\_RAM](group__device-mmio.md#gabdae30483b01d470c357571e088dc51a) |
| #define | [DEVICE\_MMIO\_RAM](group__device-mmio-single.md#ga47e037f86108c8da12d8a9b9a35e6ad5)   [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) \_mmio |
|  | Declare storage for MMIO information within a device's dev\_data struct. |
| #define | [DEVICE\_MMIO\_RAM\_PTR](group__device-mmio-single.md#ga63f871dc2ec4c89839a1782e86e292bf)([device](structdevice.md)) |
|  | Return a pointer to the RAM-based storage area for a device's MMIO address. |
| #define | [DEVICE\_MMIO\_ROM](group__device-mmio-single.md#ga1dfb620f6b3c7ee9b2bc54044d0bc875)   struct z\_device\_mmio\_rom \_mmio |
|  | Declare storage for MMIO data within a device's config struct. |
| #define | [DEVICE\_MMIO\_ROM\_PTR](group__device-mmio-single.md#ga6246f4c8bc1542d8960d3bda99a592e5)(dev) |
|  | Return a pointer to the ROM-based storage area for a device's MMIO information. |
| #define | [DEVICE\_MMIO\_ROM\_INIT](group__device-mmio-single.md#ga023516c60725f8c6d62110f74af22549)(node\_id) |
|  | Initialize a DEVICE\_MMIO\_ROM member. |
| #define | [DEVICE\_MMIO\_MAP](group__device-mmio-single.md#ga8e15770c4ec118edbefc1ef95f1ace80)(dev, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Map MMIO memory into the address space. |
| #define | [DEVICE\_MMIO\_GET](group__device-mmio-single.md#ga8cb49d87ef6dc3b017d5b68860530b63)(dev) |
|  | Obtain the MMIO address for a device. |
| #define | [DEVICE\_MMIO\_NAMED\_RAM](group__device-mmio-named.md#ga92b6570b0f7bd370bbdfbc4e474151e4)(name) |
|  | Declare storage for MMIO data within a device's dev\_data struct. |
| #define | [DEVICE\_MMIO\_NAMED\_RAM\_PTR](group__device-mmio-named.md#ga42737f178f205bd90d4e523ae5d67a09)(dev, name) |
|  | Return a pointer to the RAM storage for a device's named MMIO address. |
| #define | [DEVICE\_MMIO\_NAMED\_ROM](group__device-mmio-named.md#gae3ad012160f657451a3f47487510bffb)(name) |
|  | Declare storage for MMIO data within a device's config struct. |
| #define | [DEVICE\_MMIO\_NAMED\_ROM\_PTR](group__device-mmio-named.md#ga7f018db0d820b72a782759a4b674de94)(dev, name) |
|  | Return a pointer to the ROM-based storage area for a device's MMIO information. |
| #define | [DEVICE\_MMIO\_NAMED\_ROM\_INIT](group__device-mmio-named.md#ga727a1946d2a315af720706a9c9e80465)(name, node\_id) |
|  | Initialize a named DEVICE\_MMIO\_NAMED\_ROM member. |
| #define | [DEVICE\_MMIO\_NAMED\_ROM\_INIT\_BY\_NAME](group__device-mmio-named.md#gada46ff611e373bdb26a9473ec7cb0380)(name, node\_id) |
|  | Initialize a named DEVICE\_MMIO\_NAMED\_ROM member using a named DT reg property. |
| #define | [DEVICE\_MMIO\_NAMED\_MAP](group__device-mmio-named.md#ga1059bb0020656ce6597e29c7dd6680c1)(dev, name, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Set up memory for a named MMIO region. |
| #define | [DEVICE\_MMIO\_NAMED\_GET](group__device-mmio-named.md#ga5ca4b0cf0637f475b5da3b1ec0a7c995)(dev, name) |
|  | Obtain a named MMIO address for a device. |
| #define | [DEVICE\_MMIO\_TOPLEVEL](group__device-mmio-toplevel.md#gad60e6840b8a9c18c19693da0028c2488)(name, node\_id) |
|  | Declare top-level storage for MMIO information, global scope. |
| #define | [DEVICE\_MMIO\_TOPLEVEL\_DECLARE](group__device-mmio-toplevel.md#ga8a712886defe59972f4cf00bb2266f95)(name) |
|  | Provide an extern reference to a top-level MMIO region. |
| #define | [DEVICE\_MMIO\_TOPLEVEL\_STATIC](group__device-mmio-toplevel.md#ga80456633db67dbb23d32e2ae7cc93512)(name, node\_id) |
|  | Declare top-level storage for MMIO information, static scope. |
| #define | [DEVICE\_MMIO\_TOPLEVEL\_RAM\_PTR](group__device-mmio-toplevel.md#ga746bfe0c817dbd60f1c1f60d47f1560e)(name) |
|  | Return a pointer to the RAM storage for a device's toplevel MMIO address. |
| #define | [DEVICE\_MMIO\_TOPLEVEL\_ROM\_PTR](group__device-mmio-toplevel.md#ga2877cda5f9780ecff45a4abe150e2504)(name) |
|  | Return a pointer to the ROM-based storage area for a toplevel MMIO region. |
| #define | [DEVICE\_MMIO\_TOPLEVEL\_MAP](group__device-mmio-toplevel.md#ga6533dfab1e1bab2a11654abf4231379b)(name, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Set up memory for a driver'sMMIO region. |
| #define | [DEVICE\_MMIO\_TOPLEVEL\_GET](group__device-mmio-toplevel.md#gaad7ad99277cf2be684bd70c46d358338)(name) |
|  | Obtain the MMIO address for a device declared top-level. |

| Functions | |
| --- | --- |
| static \_\_boot\_func void | [device\_map](group__device-mmio.md#ga6b4a9841a5176104e1b63f7475d3d2a2) ([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) \*virt\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys\_addr, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Set linear address for device MMIO access. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [device\_mmio.h](device__mmio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
