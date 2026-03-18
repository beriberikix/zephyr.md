---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/device__mmio_8h_source.html
original_path: doxygen/html/device__mmio_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

device\_mmio.h

[Go to the documentation of this file.](device__mmio_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_SYS\_DEVICE\_MMIO\_H

7#define ZEPHYR\_INCLUDE\_SYS\_DEVICE\_MMIO\_H

8

9#include <[zephyr/toolchain.h](toolchain_8h.md)>

10#include <[zephyr/linker/sections.h](sections_8h.md)>

11

27

28/\* Storing MMIO addresses in RAM is a system-wide decision based on

29 \* configuration. This is just used to simplify some other definitions.

30 \*

31 \* If we have an MMU enabled, all physical MMIO regions must be mapped into

32 \* the kernel's virtual address space at runtime, this is a hard requirement.

33 \*

34 \* If we have PCIE enabled, this does mean that non-PCIE drivers may waste

35 \* a bit of RAM, but systems with PCI express are not RAM constrained.

36 \*/

37#if defined(CONFIG\_MMU) || defined(CONFIG\_PCIE) || defined(CONFIG\_EXTERNAL\_ADDRESS\_TRANSLATION)

[ 38](group__device-mmio.md#gabdae30483b01d470c357571e088dc51a)#define DEVICE\_MMIO\_IS\_IN\_RAM

39#endif

40

41#if defined(CONFIG\_EXTERNAL\_ADDRESS\_TRANSLATION)

42#include <[zephyr/drivers/mm/system\_mm.h](system__mm_8h.md)>

43#endif

44

45#ifndef \_ASMLANGUAGE

46#include <[stdint.h](stdint_8h.md)>

47#include <stddef.h>

48#include <[zephyr/kernel/mm.h](kernel_2mm_8h.md)>

49#include <[zephyr/sys/sys\_io.h](sys_2sys__io_8h.md)>

50

51#ifdef DEVICE\_MMIO\_IS\_IN\_RAM

52/\* Store the physical address and size from DTS, we'll memory

53 \* map into the virtual address space at runtime. This is not applicable

54 \* to PCIe devices, which must query the bus for BAR information.

55 \*/

56struct z\_device\_mmio\_rom {

58 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys\_addr;

59

61 size\_t size;

62};

63

64#define Z\_DEVICE\_MMIO\_ROM\_INITIALIZER(node\_id) \

65 { \

66 .phys\_addr = DT\_REG\_ADDR(node\_id), \

67 .size = DT\_REG\_SIZE(node\_id) \

68 }

69

70#define Z\_DEVICE\_MMIO\_NAMED\_ROM\_INITIALIZER(name, node\_id) \

71 { \

72 .phys\_addr = DT\_REG\_ADDR\_BY\_NAME(node\_id, name), \

73 .size = DT\_REG\_SIZE\_BY\_NAME(node\_id, name) \

74 }

75

96\_\_boot\_func

[ 97](group__device-mmio.md#ga6b4a9841a5176104e1b63f7475d3d2a2)static inline void [device\_map](group__device-mmio.md#ga6b4a9841a5176104e1b63f7475d3d2a2)([mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) \*virt\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) phys\_addr,

98 size\_t size, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9))

99{

100#ifdef CONFIG\_MMU

101 /\* Pass along flags and add that we want supervisor mode

102 \* read-write access.

103 \*/

104 [k\_mem\_map\_phys\_bare](group__kernel__mm__internal__apis.md#gaa2c52222198f4c7362c183e1397a4e5c)(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\*)virt\_addr, phys\_addr, size,

105 [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | [K\_MEM\_PERM\_RW](group__kernel__memory__management.md#gab9ea94b7155e276f0b653bc1a081866e));

106#else

107 ARG\_UNUSED(size);

108 ARG\_UNUSED([flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

109#ifdef CONFIG\_EXTERNAL\_ADDRESS\_TRANSLATION

110 [sys\_mm\_drv\_page\_phys\_get](group__mm__drv__apis.md#gaabbc2184a44f8c5c8cd98bf09a2cdc0f)((void \*) phys\_addr, virt\_addr);

111#else

112 \*virt\_addr = phys\_addr;

113#endif /\* CONFIG\_EXTERNAL\_ADDRESS\_TRANSLATION \*/

114#endif /\* CONFIG\_MMU \*/

115}

116#else

117/\* No MMU or PCIe. Just store the address from DTS and treat as a linear

118 \* address

119 \*/

120struct z\_device\_mmio\_rom {

122 [mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0) addr;

123};

124

125#define Z\_DEVICE\_MMIO\_ROM\_INITIALIZER(node\_id) \

126 { \

127 .addr = (mm\_reg\_t)DT\_REG\_ADDR\_U64(node\_id) \

128 }

129

130#define Z\_DEVICE\_MMIO\_NAMED\_ROM\_INITIALIZER(name, node\_id) \

131 { \

132 .addr = (mm\_reg\_t)DT\_REG\_ADDR\_BY\_NAME\_U64(node\_id, name) \

133 }

134

135#endif /\* DEVICE\_MMIO\_IS\_IN\_RAM \*/

136#endif /\* !\_ASMLANGUAGE \*/

138

148

180#ifdef DEVICE\_MMIO\_IS\_IN\_RAM

[ 181](group__device-mmio-single.md#ga47e037f86108c8da12d8a9b9a35e6ad5)#define DEVICE\_MMIO\_RAM mm\_reg\_t \_mmio

182#else

183#define DEVICE\_MMIO\_RAM

184#endif

185

186#ifdef DEVICE\_MMIO\_IS\_IN\_RAM

[ 197](group__device-mmio-single.md#ga63f871dc2ec4c89839a1782e86e292bf)#define DEVICE\_MMIO\_RAM\_PTR(device) (mm\_reg\_t \*)((device)->data)

198#endif /\* DEVICE\_MMIO\_IS\_IN\_RAM \*/

199

[ 230](group__device-mmio-single.md#ga1dfb620f6b3c7ee9b2bc54044d0bc875)#define DEVICE\_MMIO\_ROM struct z\_device\_mmio\_rom \_mmio

231

[ 241](group__device-mmio-single.md#ga6246f4c8bc1542d8960d3bda99a592e5)#define DEVICE\_MMIO\_ROM\_PTR(dev) \

242 ((struct z\_device\_mmio\_rom \*)((dev)->config))

243

[ 266](group__device-mmio-single.md#ga023516c60725f8c6d62110f74af22549)#define DEVICE\_MMIO\_ROM\_INIT(node\_id) \

267 .\_mmio = Z\_DEVICE\_MMIO\_ROM\_INITIALIZER(node\_id)

268

285#ifdef DEVICE\_MMIO\_IS\_IN\_RAM

[ 286](group__device-mmio-single.md#ga8e15770c4ec118edbefc1ef95f1ace80)#define DEVICE\_MMIO\_MAP(dev, flags) \

287 device\_map(DEVICE\_MMIO\_RAM\_PTR(dev), \

288 DEVICE\_MMIO\_ROM\_PTR(dev)->phys\_addr, \

289 DEVICE\_MMIO\_ROM\_PTR(dev)->size, \

290 (flags))

291#else

292#define DEVICE\_MMIO\_MAP(dev, flags) do { } while (false)

293#endif

294

314#ifdef DEVICE\_MMIO\_IS\_IN\_RAM

[ 315](group__device-mmio-single.md#ga8cb49d87ef6dc3b017d5b68860530b63)#define DEVICE\_MMIO\_GET(dev) (\*DEVICE\_MMIO\_RAM\_PTR(dev))

316#else

317#define DEVICE\_MMIO\_GET(dev) (DEVICE\_MMIO\_ROM\_PTR(dev)->addr)

318#endif

320

330

365#ifdef DEVICE\_MMIO\_IS\_IN\_RAM

[ 366](group__device-mmio-named.md#ga92b6570b0f7bd370bbdfbc4e474151e4)#define DEVICE\_MMIO\_NAMED\_RAM(name) mm\_reg\_t name

367#else

368#define DEVICE\_MMIO\_NAMED\_RAM(name)

369#endif /\* DEVICE\_MMIO\_IS\_IN\_RAM \*/

370

371#ifdef DEVICE\_MMIO\_IS\_IN\_RAM

[ 382](group__device-mmio-named.md#ga42737f178f205bd90d4e523ae5d67a09)#define DEVICE\_MMIO\_NAMED\_RAM\_PTR(dev, name) \

383 (&(DEV\_DATA(dev)->name))

384#endif /\* DEVICE\_MMIO\_IS\_IN\_RAM \*/

385

[ 421](group__device-mmio-named.md#gae3ad012160f657451a3f47487510bffb)#define DEVICE\_MMIO\_NAMED\_ROM(name) struct z\_device\_mmio\_rom name

422

[ 435](group__device-mmio-named.md#ga7f018db0d820b72a782759a4b674de94)#define DEVICE\_MMIO\_NAMED\_ROM\_PTR(dev, name) (&(DEV\_CFG(dev)->name))

436

[ 463](group__device-mmio-named.md#ga727a1946d2a315af720706a9c9e80465)#define DEVICE\_MMIO\_NAMED\_ROM\_INIT(name, node\_id) \

464 .name = Z\_DEVICE\_MMIO\_ROM\_INITIALIZER(node\_id)

465

[ 504](group__device-mmio-named.md#gada46ff611e373bdb26a9473ec7cb0380)#define DEVICE\_MMIO\_NAMED\_ROM\_INIT\_BY\_NAME(name, node\_id) \

505 .name = Z\_DEVICE\_MMIO\_NAMED\_ROM\_INITIALIZER(name, node\_id)

506

533#ifdef DEVICE\_MMIO\_IS\_IN\_RAM

[ 534](group__device-mmio-named.md#ga1059bb0020656ce6597e29c7dd6680c1)#define DEVICE\_MMIO\_NAMED\_MAP(dev, name, flags) \

535 device\_map(DEVICE\_MMIO\_NAMED\_RAM\_PTR((dev), name), \

536 (DEVICE\_MMIO\_NAMED\_ROM\_PTR((dev), name)->phys\_addr), \

537 (DEVICE\_MMIO\_NAMED\_ROM\_PTR((dev), name)->size), \

538 (flags))

539#else

540#define DEVICE\_MMIO\_NAMED\_MAP(dev, name, flags) do { } while (false)

541#endif

542

564#ifdef DEVICE\_MMIO\_IS\_IN\_RAM

[ 565](group__device-mmio-named.md#ga5ca4b0cf0637f475b5da3b1ec0a7c995)#define DEVICE\_MMIO\_NAMED\_GET(dev, name) \

566 (\*DEVICE\_MMIO\_NAMED\_RAM\_PTR((dev), name))

567#else

568#define DEVICE\_MMIO\_NAMED\_GET(dev, name) \

569 ((DEVICE\_MMIO\_NAMED\_ROM\_PTR((dev), name))->addr)

570#endif /\* DEVICE\_MMIO\_IS\_IN\_RAM \*/

571

573

590

591 #define Z\_TOPLEVEL\_ROM\_NAME(name) \_CONCAT(z\_mmio\_rom\_\_, name)

592 #define Z\_TOPLEVEL\_RAM\_NAME(name) \_CONCAT(z\_mmio\_ram\_\_, name)

593

609#ifdef DEVICE\_MMIO\_IS\_IN\_RAM

[ 610](group__device-mmio-toplevel.md#gad60e6840b8a9c18c19693da0028c2488)#define DEVICE\_MMIO\_TOPLEVEL(name, node\_id) \

611 \_\_pinned\_bss \

612 mm\_reg\_t Z\_TOPLEVEL\_RAM\_NAME(name); \

613 \_\_pinned\_rodata \

614 const struct z\_device\_mmio\_rom Z\_TOPLEVEL\_ROM\_NAME(name) = \

615 Z\_DEVICE\_MMIO\_ROM\_INITIALIZER(node\_id)

616#else

617#define DEVICE\_MMIO\_TOPLEVEL(name, node\_id) \

618 \_\_pinned\_rodata \

619 const struct z\_device\_mmio\_rom Z\_TOPLEVEL\_ROM\_NAME(name) = \

620 Z\_DEVICE\_MMIO\_ROM\_INITIALIZER(node\_id)

621#endif /\* DEVICE\_MMIO\_IS\_IN\_RAM \*/

622

636

637#ifdef DEVICE\_MMIO\_IS\_IN\_RAM

[ 638](group__device-mmio-toplevel.md#ga8a712886defe59972f4cf00bb2266f95)#define DEVICE\_MMIO\_TOPLEVEL\_DECLARE(name) \

639 extern mm\_reg\_t Z\_TOPLEVEL\_RAM\_NAME(name); \

640 extern const struct z\_device\_mmio\_rom Z\_TOPLEVEL\_ROM\_NAME(name)

641#else

642#define DEVICE\_MMIO\_TOPLEVEL\_DECLARE(name) \

643 extern const struct z\_device\_mmio\_rom Z\_TOPLEVEL\_ROM\_NAME(name)

644#endif /\* DEVICE\_MMIO\_IS\_IN\_RAM \*/

645

660#ifdef DEVICE\_MMIO\_IS\_IN\_RAM

[ 661](group__device-mmio-toplevel.md#ga80456633db67dbb23d32e2ae7cc93512)#define DEVICE\_MMIO\_TOPLEVEL\_STATIC(name, node\_id) \

662 \_\_pinned\_bss \

663 static mm\_reg\_t Z\_TOPLEVEL\_RAM\_NAME(name); \

664 \_\_pinned\_rodata \

665 static const struct z\_device\_mmio\_rom Z\_TOPLEVEL\_ROM\_NAME(name) = \

666 Z\_DEVICE\_MMIO\_ROM\_INITIALIZER(node\_id)

667#else

668#define DEVICE\_MMIO\_TOPLEVEL\_STATIC(name, node\_id) \

669 \_\_pinned\_rodata \

670 static const struct z\_device\_mmio\_rom Z\_TOPLEVEL\_ROM\_NAME(name) = \

671 Z\_DEVICE\_MMIO\_ROM\_INITIALIZER(node\_id)

672#endif /\* DEVICE\_MMIO\_IS\_IN\_RAM \*/

673

674#ifdef DEVICE\_MMIO\_IS\_IN\_RAM

[ 682](group__device-mmio-toplevel.md#ga746bfe0c817dbd60f1c1f60d47f1560e)#define DEVICE\_MMIO\_TOPLEVEL\_RAM\_PTR(name) &Z\_TOPLEVEL\_RAM\_NAME(name)

683#endif /\* DEVICE\_MMIO\_IS\_IN\_RAM \*/

684

[ 691](group__device-mmio-toplevel.md#ga2877cda5f9780ecff45a4abe150e2504)#define DEVICE\_MMIO\_TOPLEVEL\_ROM\_PTR(name) &Z\_TOPLEVEL\_ROM\_NAME(name)

692

714#ifdef DEVICE\_MMIO\_IS\_IN\_RAM

[ 715](group__device-mmio-toplevel.md#ga6533dfab1e1bab2a11654abf4231379b)#define DEVICE\_MMIO\_TOPLEVEL\_MAP(name, flags) \

716 device\_map(&Z\_TOPLEVEL\_RAM\_NAME(name), \

717 Z\_TOPLEVEL\_ROM\_NAME(name).phys\_addr, \

718 Z\_TOPLEVEL\_ROM\_NAME(name).size, (flags))

719#else

720#define DEVICE\_MMIO\_TOPLEVEL\_MAP(name, flags) do { } while (false)

721#endif

722

733#ifdef DEVICE\_MMIO\_IS\_IN\_RAM

[ 734](group__device-mmio-toplevel.md#gaad7ad99277cf2be684bd70c46d358338)#define DEVICE\_MMIO\_TOPLEVEL\_GET(name) \

735 ((mm\_reg\_t)Z\_TOPLEVEL\_RAM\_NAME(name))

736#else

737#define DEVICE\_MMIO\_TOPLEVEL\_GET(name) \

738 ((mm\_reg\_t)Z\_TOPLEVEL\_ROM\_NAME(name).addr)

739#endif

741

742#endif /\* ZEPHYR\_INCLUDE\_SYS\_DEVICE\_MMIO\_H \*/

[device\_map](group__device-mmio.md#ga6b4a9841a5176104e1b63f7475d3d2a2)

static \_\_boot\_func void device\_map(mm\_reg\_t \*virt\_addr, uintptr\_t phys\_addr, size\_t size, uint32\_t flags)

Set linear address for device MMIO access.

**Definition** device\_mmio.h:97

[K\_MEM\_PERM\_RW](group__kernel__memory__management.md#gab9ea94b7155e276f0b653bc1a081866e)

#define K\_MEM\_PERM\_RW

Region will have read/write access (and not read-only).

**Definition** mm.h:61

[k\_mem\_map\_phys\_bare](group__kernel__mm__internal__apis.md#gaa2c52222198f4c7362c183e1397a4e5c)

void k\_mem\_map\_phys\_bare(uint8\_t \*\*virt\_ptr, uintptr\_t phys, size\_t size, uint32\_t flags)

Map a physical memory region into the kernel's virtual address space.

[sys\_mm\_drv\_page\_phys\_get](group__mm__drv__apis.md#gaabbc2184a44f8c5c8cd98bf09a2cdc0f)

int sys\_mm\_drv\_page\_phys\_get(void \*virt, uintptr\_t \*phys)

Get the mapped physical memory address from virtual address.

[mm.h](kernel_2mm_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[sections.h](sections_8h.md)

Definitions of various linker Sections.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[sys\_io.h](sys_2sys__io_8h.md)

[mm\_reg\_t](sys_2sys__io_8h.md#a7bcfa789a44940bccc5b9b98642744b0)

uintptr\_t mm\_reg\_t

**Definition** sys\_io.h:20

[system\_mm.h](system__mm_8h.md)

Memory Management Driver APIs.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [device\_mmio.h](device__mmio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
