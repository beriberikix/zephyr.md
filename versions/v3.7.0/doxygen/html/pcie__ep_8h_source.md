---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/pcie__ep_8h_source.html
original_path: doxygen/html/pcie__ep_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

pcie\_ep.h

[Go to the documentation of this file.](pcie__ep_8h.md)

1

6

7/\*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*

10 \* Copyright 2020 Broadcom

11 \*

12 \*/

13#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_EP\_H\_

14#define ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_EP\_H\_

15

16#include <[zephyr/device.h](device_8h.md)>

17#include <[zephyr/init.h](init_8h.md)>

18#include <[zephyr/kernel.h](kernel_8h.md)>

19#include <[stdint.h](stdint_8h.md)>

20

[ 21](pcie__ep_8h.md#aa7c51648c5a1663dd4dec689727a510b)enum [pcie\_ob\_mem\_type](pcie__ep_8h.md#aa7c51648c5a1663dd4dec689727a510b) {

[ 22](pcie__ep_8h.md#aa7c51648c5a1663dd4dec689727a510ba52b8bd55168f44c7c4a6a3d36824d286) [PCIE\_OB\_ANYMEM](pcie__ep_8h.md#aa7c51648c5a1663dd4dec689727a510ba52b8bd55168f44c7c4a6a3d36824d286),

[ 23](pcie__ep_8h.md#aa7c51648c5a1663dd4dec689727a510ba5312fb052e8dafaab224a4b554292e74) [PCIE\_OB\_LOWMEM](pcie__ep_8h.md#aa7c51648c5a1663dd4dec689727a510ba5312fb052e8dafaab224a4b554292e74),

[ 24](pcie__ep_8h.md#aa7c51648c5a1663dd4dec689727a510ba13da19c9fa1732e72fa8add58da33ebb) [PCIE\_OB\_HIGHMEM](pcie__ep_8h.md#aa7c51648c5a1663dd4dec689727a510ba13da19c9fa1732e72fa8add58da33ebb),

25};

26

[ 27](pcie__ep_8h.md#aba0e572125869b246d4968ee164f3800)enum [pci\_ep\_irq\_type](pcie__ep_8h.md#aba0e572125869b246d4968ee164f3800) {

[ 28](pcie__ep_8h.md#aba0e572125869b246d4968ee164f3800ad90da0a62096ef8a4fc7d230afd0d44d) [PCIE\_EP\_IRQ\_LEGACY](pcie__ep_8h.md#aba0e572125869b246d4968ee164f3800ad90da0a62096ef8a4fc7d230afd0d44d),

[ 29](pcie__ep_8h.md#aba0e572125869b246d4968ee164f3800a267b658ad2587fd0d57664197daeb318) [PCIE\_EP\_IRQ\_MSI](pcie__ep_8h.md#aba0e572125869b246d4968ee164f3800a267b658ad2587fd0d57664197daeb318),

[ 30](pcie__ep_8h.md#aba0e572125869b246d4968ee164f3800a55cad2c5812c9c7c14476ff000199ad4) [PCIE\_EP\_IRQ\_MSIX](pcie__ep_8h.md#aba0e572125869b246d4968ee164f3800a55cad2c5812c9c7c14476ff000199ad4),

31};

32

[ 33](pcie__ep_8h.md#acd2605f2fb5676ded5f125712681d458)enum [xfer\_direction](pcie__ep_8h.md#acd2605f2fb5676ded5f125712681d458) {

[ 34](pcie__ep_8h.md#acd2605f2fb5676ded5f125712681d458af2c2a8166d85d21e036a4a2015df803e) [HOST\_TO\_DEVICE](pcie__ep_8h.md#acd2605f2fb5676ded5f125712681d458af2c2a8166d85d21e036a4a2015df803e),

[ 35](pcie__ep_8h.md#acd2605f2fb5676ded5f125712681d458a4c419a2c450c4d954c3768631870480a) [DEVICE\_TO\_HOST](pcie__ep_8h.md#acd2605f2fb5676ded5f125712681d458a4c419a2c450c4d954c3768631870480a),

36};

37

[ 38](pcie__ep_8h.md#a7b0f0f4693b7d11b973bfd62ac1b35cd)enum [pcie\_reset](pcie__ep_8h.md#a7b0f0f4693b7d11b973bfd62ac1b35cd) {

[ 39](pcie__ep_8h.md#a7b0f0f4693b7d11b973bfd62ac1b35cda532057b4dab53d2e86701394ead62ea7) [PCIE\_PERST](pcie__ep_8h.md#a7b0f0f4693b7d11b973bfd62ac1b35cda532057b4dab53d2e86701394ead62ea7),

[ 40](pcie__ep_8h.md#a7b0f0f4693b7d11b973bfd62ac1b35cda7d94ae3f1fbdd486102559a450f01dee) [PCIE\_PERST\_INB](pcie__ep_8h.md#a7b0f0f4693b7d11b973bfd62ac1b35cda7d94ae3f1fbdd486102559a450f01dee),

[ 41](pcie__ep_8h.md#a7b0f0f4693b7d11b973bfd62ac1b35cda6dcb2d2f5ad3624bda5ca25d2e38a47a) [PCIE\_FLR](pcie__ep_8h.md#a7b0f0f4693b7d11b973bfd62ac1b35cda6dcb2d2f5ad3624bda5ca25d2e38a47a),

[ 42](pcie__ep_8h.md#a7b0f0f4693b7d11b973bfd62ac1b35cda2c60bd39ac112aad31d1299900f0795a) [PCIE\_RESET\_MAX](pcie__ep_8h.md#a7b0f0f4693b7d11b973bfd62ac1b35cda2c60bd39ac112aad31d1299900f0795a)

43};

44

56

[ 57](pcie__ep_8h.md#afcde72dd6977ee7de9ebf4146113f912)typedef void (\*[pcie\_ep\_reset\_callback\_t](pcie__ep_8h.md#afcde72dd6977ee7de9ebf4146113f912))(void \*arg);

58

[ 59](structpcie__ep__driver__api.md)\_\_subsystem struct [pcie\_ep\_driver\_api](structpcie__ep__driver__api.md) {

[ 60](structpcie__ep__driver__api.md#aa5f508a7ab546c862f3aa65b480a45cc) int (\*[conf\_read](structpcie__ep__driver__api.md#aa5f508a7ab546c862f3aa65b480a45cc))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset,

61 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data);

[ 62](structpcie__ep__driver__api.md#acc1262a07dd079842c9c95708a2c6004) void (\*[conf\_write](structpcie__ep__driver__api.md#acc1262a07dd079842c9c95708a2c6004))(const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset,

63 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data);

[ 64](structpcie__ep__driver__api.md#a444198e899d6a1353a7f8e3828f76643) int (\*[map\_addr](structpcie__ep__driver__api.md#a444198e899d6a1353a7f8e3828f76643))(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) pcie\_addr,

65 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*mapped\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size,

66 enum [pcie\_ob\_mem\_type](pcie__ep_8h.md#aa7c51648c5a1663dd4dec689727a510b) ob\_mem\_type);

[ 67](structpcie__ep__driver__api.md#a82d9766067a066d83b25390ad5903534) void (\*[unmap\_addr](structpcie__ep__driver__api.md#a82d9766067a066d83b25390ad5903534))(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mapped\_addr);

[ 68](structpcie__ep__driver__api.md#a83ef7d357174e55364660b53924b0017) int (\*[raise\_irq](structpcie__ep__driver__api.md#a83ef7d357174e55364660b53924b0017))(const struct [device](structdevice.md) \*dev,

69 enum [pci\_ep\_irq\_type](pcie__ep_8h.md#aba0e572125869b246d4968ee164f3800) irq\_type,

70 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq\_num);

[ 71](structpcie__ep__driver__api.md#adb5f2ea78cc5e9b0f61461a036c746eb) int (\*[register\_reset\_cb](structpcie__ep__driver__api.md#adb5f2ea78cc5e9b0f61461a036c746eb))(const struct [device](structdevice.md) \*dev,

72 enum [pcie\_reset](pcie__ep_8h.md#a7b0f0f4693b7d11b973bfd62ac1b35cd) reset,

73 [pcie\_ep\_reset\_callback\_t](pcie__ep_8h.md#afcde72dd6977ee7de9ebf4146113f912) cb, void \*arg);

[ 74](structpcie__ep__driver__api.md#ab816f2aad307f0b4a8181a7711d565bc) int (\*[dma\_xfer](structpcie__ep__driver__api.md#ab816f2aad307f0b4a8181a7711d565bc))(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mapped\_addr,

75 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) local\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size,

76 enum [xfer\_direction](pcie__ep_8h.md#acd2605f2fb5676ded5f125712681d458) dir);

77};

78

90

[ 91](pcie__ep_8h.md#ad35d42579500a959bb3275cd65b04a42)static inline int [pcie\_ep\_conf\_read](pcie__ep_8h.md#ad35d42579500a959bb3275cd65b04a42)(const struct [device](structdevice.md) \*dev,

92 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e))

93{

94 const struct [pcie\_ep\_driver\_api](structpcie__ep__driver__api.md) \*api =

95 (const struct [pcie\_ep\_driver\_api](structpcie__ep__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

96

97 return api->[conf\_read](structpcie__ep__driver__api.md#aa5f508a7ab546c862f3aa65b480a45cc)(dev, offset, data);

98}

99

109

[ 110](pcie__ep_8h.md#a8d3f4de13956fbd7ed71acbd387f781a)static inline void [pcie\_ep\_conf\_write](pcie__ep_8h.md#a8d3f4de13956fbd7ed71acbd387f781a)(const struct [device](structdevice.md) \*dev,

111 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) offset, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data)

112{

113 const struct [pcie\_ep\_driver\_api](structpcie__ep__driver__api.md) \*api =

114 (const struct [pcie\_ep\_driver\_api](structpcie__ep__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

115

116 api->[conf\_write](structpcie__ep__driver__api.md#acc1262a07dd079842c9c95708a2c6004)(dev, offset, data);

117}

118

143

[ 144](pcie__ep_8h.md#a7bcff5f22fd32e0b2c3c3c509038b2db)static inline int [pcie\_ep\_map\_addr](pcie__ep_8h.md#a7bcff5f22fd32e0b2c3c3c509038b2db)(const struct [device](structdevice.md) \*dev,

145 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) pcie\_addr,

146 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*mapped\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size,

147 enum [pcie\_ob\_mem\_type](pcie__ep_8h.md#aa7c51648c5a1663dd4dec689727a510b) ob\_mem\_type)

148{

149 const struct [pcie\_ep\_driver\_api](structpcie__ep__driver__api.md) \*api =

150 (const struct [pcie\_ep\_driver\_api](structpcie__ep__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

151

152 return api->[map\_addr](structpcie__ep__driver__api.md#a444198e899d6a1353a7f8e3828f76643)(dev, pcie\_addr, mapped\_addr, size, ob\_mem\_type);

153}

154

165

[ 166](pcie__ep_8h.md#a07ee4ed9ceb42462c95da8bbf3dfc8f7)static inline void [pcie\_ep\_unmap\_addr](pcie__ep_8h.md#a07ee4ed9ceb42462c95da8bbf3dfc8f7)(const struct [device](structdevice.md) \*dev,

167 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mapped\_addr)

168{

169 const struct [pcie\_ep\_driver\_api](structpcie__ep__driver__api.md) \*api =

170 (const struct [pcie\_ep\_driver\_api](structpcie__ep__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

171

172 api->[unmap\_addr](structpcie__ep__driver__api.md#a82d9766067a066d83b25390ad5903534)(dev, mapped\_addr);

173}

174

186

[ 187](pcie__ep_8h.md#aec421e689d4d72b0bf8a34fe8303b103)static inline int [pcie\_ep\_raise\_irq](pcie__ep_8h.md#aec421e689d4d72b0bf8a34fe8303b103)(const struct [device](structdevice.md) \*dev,

188 enum [pci\_ep\_irq\_type](pcie__ep_8h.md#aba0e572125869b246d4968ee164f3800) irq\_type,

189 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) irq\_num)

190{

191 const struct [pcie\_ep\_driver\_api](structpcie__ep__driver__api.md) \*api =

192 (const struct [pcie\_ep\_driver\_api](structpcie__ep__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

193 return api->[raise\_irq](structpcie__ep__driver__api.md#a83ef7d357174e55364660b53924b0017)(dev, irq\_type, irq\_num);

194}

195

210

[ 211](pcie__ep_8h.md#a4e9cc8364703bb58e96642d1250dc410)static inline int [pcie\_ep\_register\_reset\_cb](pcie__ep_8h.md#a4e9cc8364703bb58e96642d1250dc410)(const struct [device](structdevice.md) \*dev,

212 enum [pcie\_reset](pcie__ep_8h.md#a7b0f0f4693b7d11b973bfd62ac1b35cd) reset,

213 [pcie\_ep\_reset\_callback\_t](pcie__ep_8h.md#afcde72dd6977ee7de9ebf4146113f912) cb,

214 void \*arg)

215{

216 const struct [pcie\_ep\_driver\_api](structpcie__ep__driver__api.md) \*api =

217 (const struct [pcie\_ep\_driver\_api](structpcie__ep__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

218

219 if (api->[register\_reset\_cb](structpcie__ep__driver__api.md#adb5f2ea78cc5e9b0f61461a036c746eb)) {

220 return api->[register\_reset\_cb](structpcie__ep__driver__api.md#adb5f2ea78cc5e9b0f61461a036c746eb)(dev, reset, cb, arg);

221 }

222

223 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

224}

225

245

[ 246](pcie__ep_8h.md#a7c450e4f9d65aade3f912b72b38ed04d)static inline int [pcie\_ep\_dma\_xfer](pcie__ep_8h.md#a7c450e4f9d65aade3f912b72b38ed04d)(const struct [device](structdevice.md) \*dev,

247 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) mapped\_addr,

248 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) local\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size,

249 const enum [xfer\_direction](pcie__ep_8h.md#acd2605f2fb5676ded5f125712681d458) dir)

250{

251 const struct [pcie\_ep\_driver\_api](structpcie__ep__driver__api.md) \*api =

252 (const struct [pcie\_ep\_driver\_api](structpcie__ep__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

253

254 if (api->[dma\_xfer](structpcie__ep__driver__api.md#ab816f2aad307f0b4a8181a7711d565bc)) {

255 return api->[dma\_xfer](structpcie__ep__driver__api.md#ab816f2aad307f0b4a8181a7711d565bc)(dev, mapped\_addr, local\_addr, size, dir);

256 }

257

258 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

259}

260

[ 279](pcie__ep_8h.md#ac7e46d51c49ce6cb6b0c7ad7f8010292)int [pcie\_ep\_xfer\_data\_memcpy](pcie__ep_8h.md#ac7e46d51c49ce6cb6b0c7ad7f8010292)(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) pcie\_addr,

280 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*local\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size,

281 enum [pcie\_ob\_mem\_type](pcie__ep_8h.md#aa7c51648c5a1663dd4dec689727a510b) ob\_mem\_type,

282 enum [xfer\_direction](pcie__ep_8h.md#acd2605f2fb5676ded5f125712681d458) dir);

283

[ 301](pcie__ep_8h.md#acfe495f60e94341e88cc267a879918fc)int [pcie\_ep\_xfer\_data\_dma](pcie__ep_8h.md#acfe495f60e94341e88cc267a879918fc)(const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) pcie\_addr,

302 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*local\_addr, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) size,

303 enum [pcie\_ob\_mem\_type](pcie__ep_8h.md#aa7c51648c5a1663dd4dec689727a510b) ob\_mem\_type,

304 enum [xfer\_direction](pcie__ep_8h.md#acd2605f2fb5676ded5f125712681d458) dir);

305

306#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_PCIE\_EP\_H\_ \*/

[device.h](device_8h.md)

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[init.h](init_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[pcie\_ep\_unmap\_addr](pcie__ep_8h.md#a07ee4ed9ceb42462c95da8bbf3dfc8f7)

static void pcie\_ep\_unmap\_addr(const struct device \*dev, uint64\_t mapped\_addr)

Remove mapping to PCIe outbound region.

**Definition** pcie\_ep.h:166

[pcie\_ep\_register\_reset\_cb](pcie__ep_8h.md#a4e9cc8364703bb58e96642d1250dc410)

static int pcie\_ep\_register\_reset\_cb(const struct device \*dev, enum pcie\_reset reset, pcie\_ep\_reset\_callback\_t cb, void \*arg)

Register callback function for reset interrupts.

**Definition** pcie\_ep.h:211

[pcie\_reset](pcie__ep_8h.md#a7b0f0f4693b7d11b973bfd62ac1b35cd)

pcie\_reset

**Definition** pcie\_ep.h:38

[PCIE\_RESET\_MAX](pcie__ep_8h.md#a7b0f0f4693b7d11b973bfd62ac1b35cda2c60bd39ac112aad31d1299900f0795a)

@ PCIE\_RESET\_MAX

**Definition** pcie\_ep.h:42

[PCIE\_PERST](pcie__ep_8h.md#a7b0f0f4693b7d11b973bfd62ac1b35cda532057b4dab53d2e86701394ead62ea7)

@ PCIE\_PERST

Cold reset.

**Definition** pcie\_ep.h:39

[PCIE\_FLR](pcie__ep_8h.md#a7b0f0f4693b7d11b973bfd62ac1b35cda6dcb2d2f5ad3624bda5ca25d2e38a47a)

@ PCIE\_FLR

Functional Level Reset.

**Definition** pcie\_ep.h:41

[PCIE\_PERST\_INB](pcie__ep_8h.md#a7b0f0f4693b7d11b973bfd62ac1b35cda7d94ae3f1fbdd486102559a450f01dee)

@ PCIE\_PERST\_INB

Inband hot reset.

**Definition** pcie\_ep.h:40

[pcie\_ep\_map\_addr](pcie__ep_8h.md#a7bcff5f22fd32e0b2c3c3c509038b2db)

static int pcie\_ep\_map\_addr(const struct device \*dev, uint64\_t pcie\_addr, uint64\_t \*mapped\_addr, uint32\_t size, enum pcie\_ob\_mem\_type ob\_mem\_type)

Map a host memory buffer to PCIe outbound region.

**Definition** pcie\_ep.h:144

[pcie\_ep\_dma\_xfer](pcie__ep_8h.md#a7c450e4f9d65aade3f912b72b38ed04d)

static int pcie\_ep\_dma\_xfer(const struct device \*dev, uint64\_t mapped\_addr, uintptr\_t local\_addr, uint32\_t size, const enum xfer\_direction dir)

Data transfer between mapped Host memory and device memory with "System DMA".

**Definition** pcie\_ep.h:246

[pcie\_ep\_conf\_write](pcie__ep_8h.md#a8d3f4de13956fbd7ed71acbd387f781a)

static void pcie\_ep\_conf\_write(const struct device \*dev, uint32\_t offset, uint32\_t data)

Write PCIe EP configuration space.

**Definition** pcie\_ep.h:110

[pcie\_ob\_mem\_type](pcie__ep_8h.md#aa7c51648c5a1663dd4dec689727a510b)

pcie\_ob\_mem\_type

**Definition** pcie\_ep.h:21

[PCIE\_OB\_HIGHMEM](pcie__ep_8h.md#aa7c51648c5a1663dd4dec689727a510ba13da19c9fa1732e72fa8add58da33ebb)

@ PCIE\_OB\_HIGHMEM

PCIe OB window above 32-bit address range.

**Definition** pcie\_ep.h:24

[PCIE\_OB\_ANYMEM](pcie__ep_8h.md#aa7c51648c5a1663dd4dec689727a510ba52b8bd55168f44c7c4a6a3d36824d286)

@ PCIE\_OB\_ANYMEM

PCIe OB window within any address range.

**Definition** pcie\_ep.h:22

[PCIE\_OB\_LOWMEM](pcie__ep_8h.md#aa7c51648c5a1663dd4dec689727a510ba5312fb052e8dafaab224a4b554292e74)

@ PCIE\_OB\_LOWMEM

PCIe OB window within 32-bit address range.

**Definition** pcie\_ep.h:23

[pci\_ep\_irq\_type](pcie__ep_8h.md#aba0e572125869b246d4968ee164f3800)

pci\_ep\_irq\_type

**Definition** pcie\_ep.h:27

[PCIE\_EP\_IRQ\_MSI](pcie__ep_8h.md#aba0e572125869b246d4968ee164f3800a267b658ad2587fd0d57664197daeb318)

@ PCIE\_EP\_IRQ\_MSI

Raise MSI interrupt.

**Definition** pcie\_ep.h:29

[PCIE\_EP\_IRQ\_MSIX](pcie__ep_8h.md#aba0e572125869b246d4968ee164f3800a55cad2c5812c9c7c14476ff000199ad4)

@ PCIE\_EP\_IRQ\_MSIX

Raise MSIX interrupt.

**Definition** pcie\_ep.h:30

[PCIE\_EP\_IRQ\_LEGACY](pcie__ep_8h.md#aba0e572125869b246d4968ee164f3800ad90da0a62096ef8a4fc7d230afd0d44d)

@ PCIE\_EP\_IRQ\_LEGACY

Raise Legacy interrupt.

**Definition** pcie\_ep.h:28

[pcie\_ep\_xfer\_data\_memcpy](pcie__ep_8h.md#ac7e46d51c49ce6cb6b0c7ad7f8010292)

int pcie\_ep\_xfer\_data\_memcpy(const struct device \*dev, uint64\_t pcie\_addr, uintptr\_t \*local\_addr, uint32\_t size, enum pcie\_ob\_mem\_type ob\_mem\_type, enum xfer\_direction dir)

Data transfer using memcpy.

[xfer\_direction](pcie__ep_8h.md#acd2605f2fb5676ded5f125712681d458)

xfer\_direction

**Definition** pcie\_ep.h:33

[DEVICE\_TO\_HOST](pcie__ep_8h.md#acd2605f2fb5676ded5f125712681d458a4c419a2c450c4d954c3768631870480a)

@ DEVICE\_TO\_HOST

Write to Host.

**Definition** pcie\_ep.h:35

[HOST\_TO\_DEVICE](pcie__ep_8h.md#acd2605f2fb5676ded5f125712681d458af2c2a8166d85d21e036a4a2015df803e)

@ HOST\_TO\_DEVICE

Read from Host.

**Definition** pcie\_ep.h:34

[pcie\_ep\_xfer\_data\_dma](pcie__ep_8h.md#acfe495f60e94341e88cc267a879918fc)

int pcie\_ep\_xfer\_data\_dma(const struct device \*dev, uint64\_t pcie\_addr, uintptr\_t \*local\_addr, uint32\_t size, enum pcie\_ob\_mem\_type ob\_mem\_type, enum xfer\_direction dir)

Data transfer using system DMA.

[pcie\_ep\_conf\_read](pcie__ep_8h.md#ad35d42579500a959bb3275cd65b04a42)

static int pcie\_ep\_conf\_read(const struct device \*dev, uint32\_t offset, uint32\_t \*data)

Read PCIe EP configuration space.

**Definition** pcie\_ep.h:91

[pcie\_ep\_raise\_irq](pcie__ep_8h.md#aec421e689d4d72b0bf8a34fe8303b103)

static int pcie\_ep\_raise\_irq(const struct device \*dev, enum pci\_ep\_irq\_type irq\_type, uint32\_t irq\_num)

Raise interrupt to Host.

**Definition** pcie\_ep.h:187

[pcie\_ep\_reset\_callback\_t](pcie__ep_8h.md#afcde72dd6977ee7de9ebf4146113f912)

void(\* pcie\_ep\_reset\_callback\_t)(void \*arg)

Callback API for PCIe reset interrupts.

**Definition** pcie\_ep.h:57

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::data](structdevice.md#a27573cbd10ee145f8bb1396242b27a3e)

void \* data

Address of the device instance private data.

**Definition** device.h:413

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[pcie\_ep\_driver\_api](structpcie__ep__driver__api.md)

**Definition** pcie\_ep.h:59

[pcie\_ep\_driver\_api::map\_addr](structpcie__ep__driver__api.md#a444198e899d6a1353a7f8e3828f76643)

int(\* map\_addr)(const struct device \*dev, uint64\_t pcie\_addr, uint64\_t \*mapped\_addr, uint32\_t size, enum pcie\_ob\_mem\_type ob\_mem\_type)

**Definition** pcie\_ep.h:64

[pcie\_ep\_driver\_api::unmap\_addr](structpcie__ep__driver__api.md#a82d9766067a066d83b25390ad5903534)

void(\* unmap\_addr)(const struct device \*dev, uint64\_t mapped\_addr)

**Definition** pcie\_ep.h:67

[pcie\_ep\_driver\_api::raise\_irq](structpcie__ep__driver__api.md#a83ef7d357174e55364660b53924b0017)

int(\* raise\_irq)(const struct device \*dev, enum pci\_ep\_irq\_type irq\_type, uint32\_t irq\_num)

**Definition** pcie\_ep.h:68

[pcie\_ep\_driver\_api::conf\_read](structpcie__ep__driver__api.md#aa5f508a7ab546c862f3aa65b480a45cc)

int(\* conf\_read)(const struct device \*dev, uint32\_t offset, uint32\_t \*data)

**Definition** pcie\_ep.h:60

[pcie\_ep\_driver\_api::dma\_xfer](structpcie__ep__driver__api.md#ab816f2aad307f0b4a8181a7711d565bc)

int(\* dma\_xfer)(const struct device \*dev, uint64\_t mapped\_addr, uintptr\_t local\_addr, uint32\_t size, enum xfer\_direction dir)

**Definition** pcie\_ep.h:74

[pcie\_ep\_driver\_api::conf\_write](structpcie__ep__driver__api.md#acc1262a07dd079842c9c95708a2c6004)

void(\* conf\_write)(const struct device \*dev, uint32\_t offset, uint32\_t data)

**Definition** pcie\_ep.h:62

[pcie\_ep\_driver\_api::register\_reset\_cb](structpcie__ep__driver__api.md#adb5f2ea78cc5e9b0f61461a036c746eb)

int(\* register\_reset\_cb)(const struct device \*dev, enum pcie\_reset reset, pcie\_ep\_reset\_callback\_t cb, void \*arg)

**Definition** pcie\_ep.h:71

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [pcie](dir_e35238db017d7f8b1976dc13f193be2d.md)
- [endpoint](dir_5013992ccf7d366f81bc518f84f7b0b5.md)
- [pcie\_ep.h](pcie__ep_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
