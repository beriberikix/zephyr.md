---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/dt-bindings_2pcie_2pcie_8h_source.html
original_path: doxygen/html/dt-bindings_2pcie_2pcie_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pcie.h

[Go to the documentation of this file.](dt-bindings_2pcie_2pcie_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PCIE\_PCIE\_H\_

8#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PCIE\_PCIE\_H\_

9

10/\*

11 \* Set the device's IRQ (in devicetree, or whatever) to PCIE\_IRQ\_DETECT

12 \* if the device doesn't support MSI and we don't/can't know the wired IRQ

13 \* allocated by the firmware ahead of time. Use of this functionality will

14 \* generally also require CONFIG\_DYNAMIC\_INTERRUPTS.

15 \*/

16

[ 17](dt-bindings_2pcie_2pcie_8h.md#af0887b3d40d4ea7e2c45b750428c7268)#define PCIE\_IRQ\_DETECT 0xFFFFFFFU

18

19/\*

20 \* We represent a PCI device ID as [31:16] device ID, [15:0] vendor ID. Not

21 \* coincidentally, this is same representation used in PCI configuration space.

22 \*/

23

[ 24](dt-bindings_2pcie_2pcie_8h.md#a1c7936d783359e8fa84236dfa852c701)#define PCIE\_ID\_VEND\_SHIFT 0U

[ 25](dt-bindings_2pcie_2pcie_8h.md#a4d9c60447a305f7f969f0f49d04afba6)#define PCIE\_ID\_VEND\_MASK 0xFFFFU

[ 26](dt-bindings_2pcie_2pcie_8h.md#ab6c544956c1bdc670bd3ce8f541b8807)#define PCIE\_ID\_DEV\_SHIFT 16U

[ 27](dt-bindings_2pcie_2pcie_8h.md#a6ebb481752bacbea6d7b3febb4a8ad5c)#define PCIE\_ID\_DEV\_MASK 0xFFFFU

28

29#ifdef \_\_DTS\_\_

30#define CAST(type, v) (v)

31#else

[ 32](dt-bindings_2pcie_2pcie_8h.md#a5cc7a8d3810218cc9582df360ad58cb8)#define CAST(type, v) ((type)(v))

33#endif

34

[ 35](dt-bindings_2pcie_2pcie_8h.md#af3107df4821c35c5f217a2b8bc49bce6)#define PCIE\_ID(vend, dev) \

36 ((((vend) & PCIE\_ID\_VEND\_MASK) << PCIE\_ID\_VEND\_SHIFT) | \

37 (CAST(uint32\_t, (dev) & PCIE\_ID\_DEV\_MASK) << PCIE\_ID\_DEV\_SHIFT))

38

[ 39](dt-bindings_2pcie_2pcie_8h.md#aa99534d1e5bfed4e1a57d8534a534045)#define PCIE\_ID\_TO\_VEND(id) (((id) >> PCIE\_ID\_VEND\_SHIFT) & PCIE\_ID\_VEND\_MASK)

[ 40](dt-bindings_2pcie_2pcie_8h.md#aa2198fcdc69f0d86d120355342781a62)#define PCIE\_ID\_TO\_DEV(id) (((id) >> PCIE\_ID\_DEV\_SHIFT) & PCIE\_ID\_DEV\_MASK)

41

[ 42](dt-bindings_2pcie_2pcie_8h.md#a23ce79d01609cb14f0cd4b2298e13b14)#define PCIE\_ID\_NONE PCIE\_ID(0xFFFF, 0xFFFF)

43

[ 44](dt-bindings_2pcie_2pcie_8h.md#a6268e6c107a85fbc6035eca5e6b3cfd6)#define PCIE\_BDF\_NONE 0xFFFFFFFFU

45

46/\*

47 \* Since our internal representation of bus/device/function is arbitrary,

48 \* we choose the same format employed in the x86 Configuration Address Port:

49 \*

50 \* [23:16] bus number, [15:11] device number, [10:8] function number

51 \*

52 \* All other bits must be zero.

53 \*

54 \* The x86 (the only arch, at present, that supports PCI) takes advantage

55 \* of this shared format to avoid unnecessary layers of abstraction.

56 \*/

57

[ 58](dt-bindings_2pcie_2pcie_8h.md#ada4a5da3eabff1240e651b18e8b10ca7)#define PCIE\_BDF\_BUS\_SHIFT 16U

[ 59](dt-bindings_2pcie_2pcie_8h.md#a193dd359d7a96bdd904662717c7fbf6d)#define PCIE\_BDF\_BUS\_MASK 0xFFU

[ 60](dt-bindings_2pcie_2pcie_8h.md#a7b6be889b801a52f7a713cbf7f2924f6)#define PCIE\_BDF\_DEV\_SHIFT 11U

[ 61](dt-bindings_2pcie_2pcie_8h.md#a85cc69963a93046bda0f1594803af9eb)#define PCIE\_BDF\_DEV\_MASK 0x1FU

[ 62](dt-bindings_2pcie_2pcie_8h.md#aa14155ded76c4587c49d0a71e25166cc)#define PCIE\_BDF\_FUNC\_SHIFT 8U

[ 63](dt-bindings_2pcie_2pcie_8h.md#ab481360fa29cf086cc5369e6f1860a5f)#define PCIE\_BDF\_FUNC\_MASK 0x7U

64

[ 65](dt-bindings_2pcie_2pcie_8h.md#a09a440a45623a282c23eaa2cfeef63d2)#define PCIE\_BDF(bus, dev, func) \

66 ((((bus) & PCIE\_BDF\_BUS\_MASK) << PCIE\_BDF\_BUS\_SHIFT) | \

67 (((dev) & PCIE\_BDF\_DEV\_MASK) << PCIE\_BDF\_DEV\_SHIFT) | \

68 (((func) & PCIE\_BDF\_FUNC\_MASK) << PCIE\_BDF\_FUNC\_SHIFT))

69

[ 70](dt-bindings_2pcie_2pcie_8h.md#a1c5051a72c50d6ee6cb72cd8d5c41a16)#define PCIE\_BDF\_TO\_BUS(bdf) (((bdf) >> PCIE\_BDF\_BUS\_SHIFT) & PCIE\_BDF\_BUS\_MASK)

[ 71](dt-bindings_2pcie_2pcie_8h.md#ad97fbff75fe4aa3bacad0f952e7349e9)#define PCIE\_BDF\_TO\_DEV(bdf) (((bdf) >> PCIE\_BDF\_DEV\_SHIFT) & PCIE\_BDF\_DEV\_MASK)

72

[ 73](dt-bindings_2pcie_2pcie_8h.md#ab5faa8800faa83015623439447dc0fe7)#define PCIE\_BDF\_TO\_FUNC(bdf) \

74 (((bdf) >> PCIE\_BDF\_FUNC\_SHIFT) & PCIE\_BDF\_FUNC\_MASK)

75

76#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_PCIE\_PCIE\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pcie](dir_f9fb0c2f559a5655635ae30044ebff42.md)
- [pcie.h](dt-bindings_2pcie_2pcie_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
