---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/msi_8h_source.html
original_path: doxygen/html/msi_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

msi.h

[Go to the documentation of this file.](msi_8h.md)

1/\*

2 \* Copyright (c) 2019 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_MSI\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_MSI\_H\_

9

16

17#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

18#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

19#include <[stdbool.h](stdbool_8h.md)>

20

21#include <[zephyr/drivers/pcie/pcie.h](drivers_2pcie_2pcie_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

27#ifdef CONFIG\_PCIE\_CONTROLLER

28struct msi\_vector\_generic {

29 unsigned int irq;

30 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address;

31 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) eventid;

32 unsigned int priority;

33};

34

35typedef struct msi\_vector\_generic arch\_msi\_vector\_t;

36

37#define PCI\_DEVID(bus, dev, fn) ((((bus) & 0xff) << 8) | (((dev) & 0x1f) << 3) | ((fn) & 0x07))

38#define PCI\_BDF\_TO\_DEVID(bdf) PCI\_DEVID(PCIE\_BDF\_TO\_BUS(bdf), \

39 PCIE\_BDF\_TO\_DEV(bdf), \

40 PCIE\_BDF\_TO\_FUNC(bdf))

41

42#endif

43

[ 44](structmsix__vector.md)struct [msix\_vector](structmsix__vector.md) {

[ 45](structmsix__vector.md#a2c09a989a9ed99536d85c0e800283743) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [msg\_addr](structmsix__vector.md#a2c09a989a9ed99536d85c0e800283743);

[ 46](structmsix__vector.md#a908e2d095b43713f0b9682716cd4ae85) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [msg\_up\_addr](structmsix__vector.md#a908e2d095b43713f0b9682716cd4ae85);

[ 47](structmsix__vector.md#acd899f1dc388ef49f38d593083e0042d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [msg\_data](structmsix__vector.md#acd899f1dc388ef49f38d593083e0042d);

[ 48](structmsix__vector.md#ac4d0f7192cc8bcaffd4fac75589ca298) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vector\_ctrl](structmsix__vector.md#ac4d0f7192cc8bcaffd4fac75589ca298);

49} \_\_packed;

50

[ 51](structmsi__vector.md)struct [msi\_vector](structmsi__vector.md) {

[ 52](structmsi__vector.md#a643d712565f3464874efaab81b25b68a) [pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) [bdf](structmsi__vector.md#a643d712565f3464874efaab81b25b68a);

[ 53](structmsi__vector.md#aec3f368bdbe75d9e53d6bc9b0f6a18a7) arch\_msi\_vector\_t [arch](structmsi__vector.md#aec3f368bdbe75d9e53d6bc9b0f6a18a7);

54#ifdef CONFIG\_PCIE\_MSI\_X

55 struct [msix\_vector](structmsix__vector.md) \*[msix\_vector](structmsix__vector.md);

56 bool msix;

57#endif /\* CONFIG\_PCIE\_MSI\_X \*/

58};

59

[ 60](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231)typedef struct [msi\_vector](structmsi__vector.md) [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231);

61

62#ifdef CONFIG\_PCIE\_MSI\_MULTI\_VECTOR

63

74extern [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) pcie\_msi\_vectors\_allocate([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) [bdf](structmsi__vector.md#a643d712565f3464874efaab81b25b68a),

75 unsigned int priority,

76 [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231) \*vectors,

77 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_vector);

78

90extern bool pcie\_msi\_vector\_connect([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) [bdf](structmsi__vector.md#a643d712565f3464874efaab81b25b68a),

91 [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231) \*vector,

92 void (\*routine)(const void \*parameter),

93 const void \*parameter,

94 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9));

95

96#endif /\* CONFIG\_PCIE\_MSI\_MULTI\_VECTOR \*/

97

[ 108](group__pcie__host__msi__interface.md#ga2cdf2a32cb4c6e4d68290a1e9020f4ee)extern [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pcie\_msi\_map](group__pcie__host__msi__interface.md#ga2cdf2a32cb4c6e4d68290a1e9020f4ee)(unsigned int irq,

109 [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231) \*vector,

110 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_vector);

111

[ 121](group__pcie__host__msi__interface.md#gae89ee2177016ab1df94c7f453eb5c25d)extern [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [pcie\_msi\_mdr](group__pcie__host__msi__interface.md#gae89ee2177016ab1df94c7f453eb5c25d)(unsigned int irq,

122 [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231) \*vector);

123

[ 133](group__pcie__host__msi__interface.md#ga57226ef41cee2008a2c92098dd52af6b)extern bool [pcie\_msi\_enable](group__pcie__host__msi__interface.md#ga57226ef41cee2008a2c92098dd52af6b)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) [bdf](structmsi__vector.md#a643d712565f3464874efaab81b25b68a),

134 [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231) \*vectors,

135 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_vector,

136 unsigned int irq);

137

[ 144](group__pcie__host__msi__interface.md#gac16ef7e19d7584aa2fc3a839b1b8fb01)extern bool [pcie\_is\_msi](group__pcie__host__msi__interface.md#gac16ef7e19d7584aa2fc3a839b1b8fb01)([pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb) [bdf](structmsi__vector.md#a643d712565f3464874efaab81b25b68a));

145

146/\*

147 \* The first word of the MSI capability is shared with the

148 \* capability ID and list link. The high 16 bits are the MCR.

149 \*/

150

[ 151](group__pcie__host__msi__interface.md#ga6363ff201cdaf89434be7f7976218132)#define PCIE\_MSI\_MCR 0U

152

[ 153](group__pcie__host__msi__interface.md#ga6d4aa888ca0930998d49abfc21dfc4a0)#define PCIE\_MSI\_MCR\_EN 0x00010000U /\* enable MSI \*/

[ 154](group__pcie__host__msi__interface.md#ga273df548ce103502c69a2aaf32940270)#define PCIE\_MSI\_MCR\_MMC 0x000E0000U /\* Multi Messages Capable mask \*/

[ 155](group__pcie__host__msi__interface.md#gab0b4bed4d96cc135c38e1762922a6dfc)#define PCIE\_MSI\_MCR\_MMC\_SHIFT 17

[ 156](group__pcie__host__msi__interface.md#gae34c85b4346402d14ab7ade656f7874f)#define PCIE\_MSI\_MCR\_MME 0x00700000U /\* mask of # of enabled IRQs \*/

[ 157](group__pcie__host__msi__interface.md#ga933abb134aec549761f835f84c0caf53)#define PCIE\_MSI\_MCR\_MME\_SHIFT 20

[ 158](group__pcie__host__msi__interface.md#ga8496d1040f5f0388130f3550f27dbf67)#define PCIE\_MSI\_MCR\_64 0x00800000U /\* 64-bit MSI \*/

159

160/\*

161 \* The MAP follows the MCR. If PCIE\_MSI\_MCR\_64, then the MAP

162 \* is two words long. The MDR follows immediately after the MAP.

163 \*/

164

[ 165](group__pcie__host__msi__interface.md#gaf5b03bc395082366b0f4d8a6860753a3)#define PCIE\_MSI\_MAP0 1U

[ 166](group__pcie__host__msi__interface.md#ga7dc1045e58e9e99029d2876adf373f61)#define PCIE\_MSI\_MAP1\_64 2U

[ 167](group__pcie__host__msi__interface.md#ga72a3907f5cfba38103db25a8065efe5d)#define PCIE\_MSI\_MDR\_32 2U

[ 168](group__pcie__host__msi__interface.md#ga599d70864c7a8a8d12c56c302f963c75)#define PCIE\_MSI\_MDR\_64 3U

169

170/\*

171 \* As for MSI, he first word of the MSI-X capability is shared

172 \* with the capability ID and list link. The high 16 bits are the MCR.

173 \*/

174

[ 175](group__pcie__host__msi__interface.md#ga3f684fa1e9eaf5aad844b7f5c5232adb)#define PCIE\_MSIX\_MCR 0U

176

[ 177](group__pcie__host__msi__interface.md#gaf309bab15a0118cbc39b3a52354a8067)#define PCIE\_MSIX\_MCR\_EN 0x80000000U /\* Enable MSI-X \*/

[ 178](group__pcie__host__msi__interface.md#ga7186a5d811ab5f486c7eddbb0b2ecffe)#define PCIE\_MSIX\_MCR\_FMASK 0x40000000U /\* Function Mask \*/

[ 179](group__pcie__host__msi__interface.md#ga20e8351fd64d8308ff0c94ba02e7c688)#define PCIE\_MSIX\_MCR\_TSIZE 0x07FF0000U /\* Table size mask \*/

[ 180](group__pcie__host__msi__interface.md#gabb2e51e10229fe1b5953548a96892005)#define PCIE\_MSIX\_MCR\_TSIZE\_SHIFT 16

[ 181](group__pcie__host__msi__interface.md#ga0a403e859ea16d24267fed463c214e22)#define PCIE\_MSIR\_TABLE\_ENTRY\_SIZE 16

182

[ 183](group__pcie__host__msi__interface.md#ga701825e23994bdf4da4a86b8776c3248)#define PCIE\_MSIX\_TR 1U

[ 184](group__pcie__host__msi__interface.md#ga13e9132823fa2361ab25e53c75aa8896)#define PCIE\_MSIX\_TR\_BIR 0x00000007U /\* Table BIR mask \*/

[ 185](group__pcie__host__msi__interface.md#ga44875f9af4865a82438a6a4ec714c6a9)#define PCIE\_MSIX\_TR\_OFFSET 0xFFFFFFF8U /\* Offset mask \*/

186

[ 187](group__pcie__host__msi__interface.md#ga6e74db681568d7103100036233e3467d)#define PCIE\_MSIX\_PBA 2U

[ 188](group__pcie__host__msi__interface.md#gae259720d8a4af8b2aba0625b41d21d40)#define PCIE\_MSIX\_PBA\_BIR 0x00000007U /\* PBA BIR mask \*/

[ 189](group__pcie__host__msi__interface.md#ga388b54bd3c60cb46940e1b1defc42dad)#define PCIE\_MSIX\_PBA\_OFFSET 0xFFFFFFF8U /\* Offset mask \*/

190

[ 191](group__pcie__host__msi__interface.md#ga33adc70c295b3ba887529fc8f73f6cb4)#define PCIE\_VTBL\_MA 0U /\* Msg Address offset \*/

[ 192](group__pcie__host__msi__interface.md#ga5711b93de9c485b321a9dcd01ac53b05)#define PCIE\_VTBL\_MUA 4U /\* Msg Upper Address offset \*/

[ 193](group__pcie__host__msi__interface.md#gaf35ee6cb30ff29ae0f6804f3328a1d1d)#define PCIE\_VTBL\_MD 8U /\* Msg Data offset \*/

[ 194](group__pcie__host__msi__interface.md#gae354a23e4f62342cfd4e2572068b51a3)#define PCIE\_VTBL\_VCTRL 12U /\* Vector control offset \*/

195

196#ifdef \_\_cplusplus

197}

198#endif

199

203

204#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_MSI\_H\_ \*/

[pcie.h](drivers_2pcie_2pcie_8h.md)

[pcie\_bdf\_t](group__pcie__host__interface.md#gaf9748042a4f3c8d912d19df1ccf737fb)

uint32\_t pcie\_bdf\_t

A unique PCI(e) endpoint (bus, device, function).

**Definition** pcie.h:37

[pcie\_msi\_map](group__pcie__host__msi__interface.md#ga2cdf2a32cb4c6e4d68290a1e9020f4ee)

uint32\_t pcie\_msi\_map(unsigned int irq, msi\_vector\_t \*vector, uint8\_t n\_vector)

Compute the target address for an MSI posted write.

[pcie\_msi\_enable](group__pcie__host__msi__interface.md#ga57226ef41cee2008a2c92098dd52af6b)

bool pcie\_msi\_enable(pcie\_bdf\_t bdf, msi\_vector\_t \*vectors, uint8\_t n\_vector, unsigned int irq)

Configure the given PCI endpoint to generate MSIs.

[msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231)

struct msi\_vector msi\_vector\_t

**Definition** msi.h:60

[pcie\_is\_msi](group__pcie__host__msi__interface.md#gac16ef7e19d7584aa2fc3a839b1b8fb01)

bool pcie\_is\_msi(pcie\_bdf\_t bdf)

Check if the given PCI endpoint supports MSI/MSI-X.

[pcie\_msi\_mdr](group__pcie__host__msi__interface.md#gae89ee2177016ab1df94c7f453eb5c25d)

uint16\_t pcie\_msi\_mdr(unsigned int irq, msi\_vector\_t \*vector)

Compute the data for an MSI posted write.

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[msi\_vector](structmsi__vector.md)

**Definition** msi.h:51

[msi\_vector::bdf](structmsi__vector.md#a643d712565f3464874efaab81b25b68a)

pcie\_bdf\_t bdf

**Definition** msi.h:52

[msi\_vector::arch](structmsi__vector.md#aec3f368bdbe75d9e53d6bc9b0f6a18a7)

arch\_msi\_vector\_t arch

**Definition** msi.h:53

[msix\_vector](structmsix__vector.md)

**Definition** msi.h:44

[msix\_vector::msg\_addr](structmsix__vector.md#a2c09a989a9ed99536d85c0e800283743)

uint32\_t msg\_addr

**Definition** msi.h:45

[msix\_vector::msg\_up\_addr](structmsix__vector.md#a908e2d095b43713f0b9682716cd4ae85)

uint32\_t msg\_up\_addr

**Definition** msi.h:46

[msix\_vector::vector\_ctrl](structmsix__vector.md#ac4d0f7192cc8bcaffd4fac75589ca298)

uint32\_t vector\_ctrl

**Definition** msi.h:48

[msix\_vector::msg\_data](structmsix__vector.md#acd899f1dc388ef49f38d593083e0042d)

uint32\_t msg\_data

**Definition** msi.h:47

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pcie](dir_e35238db017d7f8b1976dc13f193be2d.md)
- [msi.h](msi_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
