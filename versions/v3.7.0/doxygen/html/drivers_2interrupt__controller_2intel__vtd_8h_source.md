---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2interrupt__controller_2intel__vtd_8h_source.html
original_path: doxygen/html/drivers_2interrupt__controller_2intel__vtd_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intel\_vtd.h

[Go to the documentation of this file.](drivers_2interrupt__controller_2intel__vtd_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation

3 \* SPDX-License-Identifier: Apache-2.0

4 \*/

5

6#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_INTEL\_VTD\_H\_

7#define ZEPHYR\_INCLUDE\_DRIVERS\_INTEL\_VTD\_H\_

8

9#include <[zephyr/drivers/pcie/msi.h](msi_8h.md)>

10

[ 11](drivers_2interrupt__controller_2intel__vtd_8h.md#a3bded96a42bec41476ff6bc9f75676b4)typedef int (\*[vtd\_alloc\_entries\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a3bded96a42bec41476ff6bc9f75676b4))(const struct [device](structdevice.md) \*dev,

12 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_entries);

13

[ 14](drivers_2interrupt__controller_2intel__vtd_8h.md#aadb69e257884026693109510e20dc2b4)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[vtd\_remap\_msi\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#aadb69e257884026693109510e20dc2b4))(const struct [device](structdevice.md) \*dev,

15 [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231) \*vector,

16 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_vector);

17

[ 18](drivers_2interrupt__controller_2intel__vtd_8h.md#afefa59b2064053d90445127da9b64bfb)typedef int (\*[vtd\_remap\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#afefa59b2064053d90445127da9b64bfb))(const struct [device](structdevice.md) \*dev,

19 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx,

20 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector,

21 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

22 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) src\_id);

23

[ 24](drivers_2interrupt__controller_2intel__vtd_8h.md#a06190d6273d0adeb92e9e4e4fa79d9b4)typedef int (\*[vtd\_set\_irte\_vector\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a06190d6273d0adeb92e9e4e4fa79d9b4))(const struct [device](structdevice.md) \*dev,

25 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx,

26 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector);

27

[ 28](drivers_2interrupt__controller_2intel__vtd_8h.md#a944bfa2dc643fd3ff182eee12d836ae5)typedef int (\*[vtd\_get\_irte\_by\_vector\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a944bfa2dc643fd3ff182eee12d836ae5))(const struct [device](structdevice.md) \*dev,

29 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector);

30

[ 31](drivers_2interrupt__controller_2intel__vtd_8h.md#af3ddf5e22fcb4956e4887e1982fae28e)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) (\*[vtd\_get\_irte\_vector\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#af3ddf5e22fcb4956e4887e1982fae28e))(const struct [device](structdevice.md) \*dev,

32 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx);

33

[ 34](drivers_2interrupt__controller_2intel__vtd_8h.md#a63733309814847ba4204776e8ace9a85)typedef int (\*[vtd\_set\_irte\_irq\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a63733309814847ba4204776e8ace9a85))(const struct [device](structdevice.md) \*dev,

35 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx,

36 unsigned int irq);

37

[ 38](drivers_2interrupt__controller_2intel__vtd_8h.md#a0a2e483fe9159a46d6265b257841f43a)typedef int (\*[vtd\_get\_irte\_by\_irq\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a0a2e483fe9159a46d6265b257841f43a))(const struct [device](structdevice.md) \*dev,

39 unsigned int irq);

40

[ 41](drivers_2interrupt__controller_2intel__vtd_8h.md#a0118f224100f721a508ce00c3ae99698)typedef void (\*[vtd\_set\_irte\_msi\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a0118f224100f721a508ce00c3ae99698))(const struct [device](structdevice.md) \*dev,

42 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx,

43 bool msi);

44

[ 45](drivers_2interrupt__controller_2intel__vtd_8h.md#a622083e8841c3899ca7b7156f526581f)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[vtd\_irte\_is\_msi\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a622083e8841c3899ca7b7156f526581f))(const struct [device](structdevice.md) \*dev,

46 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx);

47

[ 48](structvtd__driver__api.md)\_\_subsystem struct [vtd\_driver\_api](structvtd__driver__api.md) {

[ 49](structvtd__driver__api.md#a3177c806bd86ebe4dc6c94141c9d5f04) [vtd\_alloc\_entries\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a3bded96a42bec41476ff6bc9f75676b4) [allocate\_entries](structvtd__driver__api.md#a3177c806bd86ebe4dc6c94141c9d5f04);

[ 50](structvtd__driver__api.md#a97f93762584ea000a149ded0d726a993) [vtd\_remap\_msi\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#aadb69e257884026693109510e20dc2b4) [remap\_msi](structvtd__driver__api.md#a97f93762584ea000a149ded0d726a993);

[ 51](structvtd__driver__api.md#ac03cd6690017568b51d1b4bedd1fea09) [vtd\_remap\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#afefa59b2064053d90445127da9b64bfb) [remap](structvtd__driver__api.md#ac03cd6690017568b51d1b4bedd1fea09);

[ 52](structvtd__driver__api.md#a03236811cfc87b4653ba1a2f53bc50a1) [vtd\_set\_irte\_vector\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a06190d6273d0adeb92e9e4e4fa79d9b4) [set\_irte\_vector](structvtd__driver__api.md#a03236811cfc87b4653ba1a2f53bc50a1);

[ 53](structvtd__driver__api.md#a39157ec0077a20a900bbe19f3cc8d1b1) [vtd\_get\_irte\_by\_vector\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a944bfa2dc643fd3ff182eee12d836ae5) [get\_irte\_by\_vector](structvtd__driver__api.md#a39157ec0077a20a900bbe19f3cc8d1b1);

[ 54](structvtd__driver__api.md#ac67dacb59216e44e55c832a26b87854f) [vtd\_get\_irte\_vector\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#af3ddf5e22fcb4956e4887e1982fae28e) [get\_irte\_vector](structvtd__driver__api.md#ac67dacb59216e44e55c832a26b87854f);

[ 55](structvtd__driver__api.md#acc5af4aaaeed8abb8768d21767c67c58) [vtd\_set\_irte\_irq\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a63733309814847ba4204776e8ace9a85) [set\_irte\_irq](structvtd__driver__api.md#acc5af4aaaeed8abb8768d21767c67c58);

[ 56](structvtd__driver__api.md#adf1c688b60ef445581dee2344a48c8b6) [vtd\_get\_irte\_by\_irq\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a0a2e483fe9159a46d6265b257841f43a) [get\_irte\_by\_irq](structvtd__driver__api.md#adf1c688b60ef445581dee2344a48c8b6);

[ 57](structvtd__driver__api.md#ac2fbdcfe7bcb0c9ef548aefe1c80b96b) [vtd\_set\_irte\_msi\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a0118f224100f721a508ce00c3ae99698) [set\_irte\_msi](structvtd__driver__api.md#ac2fbdcfe7bcb0c9ef548aefe1c80b96b);

[ 58](structvtd__driver__api.md#aac4ab98b9bf8a557cec22c685433888c) [vtd\_irte\_is\_msi\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a622083e8841c3899ca7b7156f526581f) [irte\_is\_msi](structvtd__driver__api.md#aac4ab98b9bf8a557cec22c685433888c);

59};

60

[ 71](drivers_2interrupt__controller_2intel__vtd_8h.md#a87b1cea7c86d724da0c379bfd3742879)static inline int [vtd\_allocate\_entries](drivers_2interrupt__controller_2intel__vtd_8h.md#a87b1cea7c86d724da0c379bfd3742879)(const struct [device](structdevice.md) \*dev,

72 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_entries)

73{

74 const struct [vtd\_driver\_api](structvtd__driver__api.md) \*api =

75 (const struct [vtd\_driver\_api](structvtd__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

76

77 return api->[allocate\_entries](structvtd__driver__api.md#a3177c806bd86ebe4dc6c94141c9d5f04)(dev, n\_entries);

78}

79

[ 89](drivers_2interrupt__controller_2intel__vtd_8h.md#ab7b8ad9dbee740c9e97021853f1131fc)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [vtd\_remap\_msi](drivers_2interrupt__controller_2intel__vtd_8h.md#ab7b8ad9dbee740c9e97021853f1131fc)(const struct [device](structdevice.md) \*dev,

90 [msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231) \*vector,

91 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) n\_vector)

92{

93 const struct [vtd\_driver\_api](structvtd__driver__api.md) \*api =

94 (const struct [vtd\_driver\_api](structvtd__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

95

96 return api->[remap\_msi](structvtd__driver__api.md#a97f93762584ea000a149ded0d726a993)(dev, vector, n\_vector);

97}

98

[ 110](drivers_2interrupt__controller_2intel__vtd_8h.md#a3cc5ff5183e80aeb18115d8b5a541546)static inline int [vtd\_remap](drivers_2interrupt__controller_2intel__vtd_8h.md#a3cc5ff5183e80aeb18115d8b5a541546)(const struct [device](structdevice.md) \*dev,

111 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx,

112 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector,

113 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9),

114 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) src\_id)

115{

116 const struct [vtd\_driver\_api](structvtd__driver__api.md) \*api =

117 (const struct [vtd\_driver\_api](structvtd__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

118

119 return api->[remap](structvtd__driver__api.md#ac03cd6690017568b51d1b4bedd1fea09)(dev, irte\_idx, vector, [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), src\_id);

120}

121

[ 131](drivers_2interrupt__controller_2intel__vtd_8h.md#a342e4745949ed1bd50b4d51de482be57)static inline int [vtd\_set\_irte\_vector](drivers_2interrupt__controller_2intel__vtd_8h.md#a342e4745949ed1bd50b4d51de482be57)(const struct [device](structdevice.md) \*dev,

132 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx,

133 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector)

134{

135 const struct [vtd\_driver\_api](structvtd__driver__api.md) \*api =

136 (const struct [vtd\_driver\_api](structvtd__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

137

138 return api->[set\_irte\_vector](structvtd__driver__api.md#a03236811cfc87b4653ba1a2f53bc50a1)(dev, irte\_idx, vector);

139}

140

[ 149](drivers_2interrupt__controller_2intel__vtd_8h.md#a4645558c4f9e461e86e6d0caf96311ad)static inline int [vtd\_get\_irte\_by\_vector](drivers_2interrupt__controller_2intel__vtd_8h.md#a4645558c4f9e461e86e6d0caf96311ad)(const struct [device](structdevice.md) \*dev,

150 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector)

151{

152 const struct [vtd\_driver\_api](structvtd__driver__api.md) \*api =

153 (const struct [vtd\_driver\_api](structvtd__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

154

155 return api->[get\_irte\_by\_vector](structvtd__driver__api.md#a39157ec0077a20a900bbe19f3cc8d1b1)(dev, vector);

156}

157

[ 166](drivers_2interrupt__controller_2intel__vtd_8h.md#a76d5a655a925c9ec9536e6c906c2192e)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [vtd\_get\_irte\_vector](drivers_2interrupt__controller_2intel__vtd_8h.md#a76d5a655a925c9ec9536e6c906c2192e)(const struct [device](structdevice.md) \*dev,

167 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx)

168{

169 const struct [vtd\_driver\_api](structvtd__driver__api.md) \*api =

170 (const struct [vtd\_driver\_api](structvtd__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

171

172 return api->[get\_irte\_vector](structvtd__driver__api.md#ac67dacb59216e44e55c832a26b87854f)(dev, irte\_idx);

173}

174

[ 184](drivers_2interrupt__controller_2intel__vtd_8h.md#ab067e306959a0774ee5e896eafab2132)static inline int [vtd\_set\_irte\_irq](drivers_2interrupt__controller_2intel__vtd_8h.md#ab067e306959a0774ee5e896eafab2132)(const struct [device](structdevice.md) \*dev,

185 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx,

186 unsigned int irq)

187{

188 const struct [vtd\_driver\_api](structvtd__driver__api.md) \*api =

189 (const struct [vtd\_driver\_api](structvtd__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

190

191 return api->[set\_irte\_irq](structvtd__driver__api.md#acc5af4aaaeed8abb8768d21767c67c58)(dev, irte\_idx, irq);

192}

193

[ 202](drivers_2interrupt__controller_2intel__vtd_8h.md#a214bd683e7331adbe5afbca41e3a6bc9)static inline int [vtd\_get\_irte\_by\_irq](drivers_2interrupt__controller_2intel__vtd_8h.md#a214bd683e7331adbe5afbca41e3a6bc9)(const struct [device](structdevice.md) \*dev,

203 unsigned int irq)

204{

205 const struct [vtd\_driver\_api](structvtd__driver__api.md) \*api =

206 (const struct [vtd\_driver\_api](structvtd__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

207

208 return api->[get\_irte\_by\_irq](structvtd__driver__api.md#adf1c688b60ef445581dee2344a48c8b6)(dev, irq);

209}

210

[ 211](drivers_2interrupt__controller_2intel__vtd_8h.md#ae81918a2c81e03cc4e02603781e8ca21)static inline void [vtd\_set\_irte\_msi](drivers_2interrupt__controller_2intel__vtd_8h.md#ae81918a2c81e03cc4e02603781e8ca21)(const struct [device](structdevice.md) \*dev,

212 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx,

213 bool msi)

214{

215 const struct [vtd\_driver\_api](structvtd__driver__api.md) \*api =

216 (const struct [vtd\_driver\_api](structvtd__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

217

218 return api->[set\_irte\_msi](structvtd__driver__api.md#ac2fbdcfe7bcb0c9ef548aefe1c80b96b)(dev, irte\_idx, msi);

219}

220

[ 221](drivers_2interrupt__controller_2intel__vtd_8h.md#a82018e41e5bbb12f98c16b0d416596fe)static inline bool [vtd\_irte\_is\_msi](drivers_2interrupt__controller_2intel__vtd_8h.md#a82018e41e5bbb12f98c16b0d416596fe)(const struct [device](structdevice.md) \*dev,

222 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) irte\_idx)

223{

224 const struct [vtd\_driver\_api](structvtd__driver__api.md) \*api =

225 (const struct [vtd\_driver\_api](structvtd__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

226

227 return api->[irte\_is\_msi](structvtd__driver__api.md#aac4ab98b9bf8a557cec22c685433888c)(dev, irte\_idx);

228}

229

230

231#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_INTEL\_VTD\_H\_ \*/

[vtd\_set\_irte\_msi\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a0118f224100f721a508ce00c3ae99698)

void(\* vtd\_set\_irte\_msi\_f)(const struct device \*dev, uint8\_t irte\_idx, bool msi)

**Definition** intel\_vtd.h:41

[vtd\_set\_irte\_vector\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a06190d6273d0adeb92e9e4e4fa79d9b4)

int(\* vtd\_set\_irte\_vector\_f)(const struct device \*dev, uint8\_t irte\_idx, uint16\_t vector)

**Definition** intel\_vtd.h:24

[vtd\_get\_irte\_by\_irq\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a0a2e483fe9159a46d6265b257841f43a)

int(\* vtd\_get\_irte\_by\_irq\_f)(const struct device \*dev, unsigned int irq)

**Definition** intel\_vtd.h:38

[vtd\_get\_irte\_by\_irq](drivers_2interrupt__controller_2intel__vtd_8h.md#a214bd683e7331adbe5afbca41e3a6bc9)

static int vtd\_get\_irte\_by\_irq(const struct device \*dev, unsigned int irq)

Get the irte allocated for the given irq.

**Definition** intel\_vtd.h:202

[vtd\_set\_irte\_vector](drivers_2interrupt__controller_2intel__vtd_8h.md#a342e4745949ed1bd50b4d51de482be57)

static int vtd\_set\_irte\_vector(const struct device \*dev, uint8\_t irte\_idx, uint16\_t vector)

Set the vector on the allocated irte.

**Definition** intel\_vtd.h:131

[vtd\_alloc\_entries\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a3bded96a42bec41476ff6bc9f75676b4)

int(\* vtd\_alloc\_entries\_f)(const struct device \*dev, uint8\_t n\_entries)

**Definition** intel\_vtd.h:11

[vtd\_remap](drivers_2interrupt__controller_2intel__vtd_8h.md#a3cc5ff5183e80aeb18115d8b5a541546)

static int vtd\_remap(const struct device \*dev, uint8\_t irte\_idx, uint16\_t vector, uint32\_t flags, uint16\_t src\_id)

Remap the given vector.

**Definition** intel\_vtd.h:110

[vtd\_get\_irte\_by\_vector](drivers_2interrupt__controller_2intel__vtd_8h.md#a4645558c4f9e461e86e6d0caf96311ad)

static int vtd\_get\_irte\_by\_vector(const struct device \*dev, uint16\_t vector)

Get the irte allocated for the given vector.

**Definition** intel\_vtd.h:149

[vtd\_irte\_is\_msi\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a622083e8841c3899ca7b7156f526581f)

bool(\* vtd\_irte\_is\_msi\_f)(const struct device \*dev, uint8\_t irte\_idx)

**Definition** intel\_vtd.h:45

[vtd\_set\_irte\_irq\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a63733309814847ba4204776e8ace9a85)

int(\* vtd\_set\_irte\_irq\_f)(const struct device \*dev, uint8\_t irte\_idx, unsigned int irq)

**Definition** intel\_vtd.h:34

[vtd\_get\_irte\_vector](drivers_2interrupt__controller_2intel__vtd_8h.md#a76d5a655a925c9ec9536e6c906c2192e)

static uint16\_t vtd\_get\_irte\_vector(const struct device \*dev, uint8\_t irte\_idx)

Get the vector given to the IRTE.

**Definition** intel\_vtd.h:166

[vtd\_irte\_is\_msi](drivers_2interrupt__controller_2intel__vtd_8h.md#a82018e41e5bbb12f98c16b0d416596fe)

static bool vtd\_irte\_is\_msi(const struct device \*dev, uint8\_t irte\_idx)

**Definition** intel\_vtd.h:221

[vtd\_allocate\_entries](drivers_2interrupt__controller_2intel__vtd_8h.md#a87b1cea7c86d724da0c379bfd3742879)

static int vtd\_allocate\_entries(const struct device \*dev, uint8\_t n\_entries)

Allocate contiguous IRTEs.

**Definition** intel\_vtd.h:71

[vtd\_get\_irte\_by\_vector\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#a944bfa2dc643fd3ff182eee12d836ae5)

int(\* vtd\_get\_irte\_by\_vector\_f)(const struct device \*dev, uint16\_t vector)

**Definition** intel\_vtd.h:28

[vtd\_remap\_msi\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#aadb69e257884026693109510e20dc2b4)

uint32\_t(\* vtd\_remap\_msi\_f)(const struct device \*dev, msi\_vector\_t \*vector, uint8\_t n\_vector)

**Definition** intel\_vtd.h:14

[vtd\_set\_irte\_irq](drivers_2interrupt__controller_2intel__vtd_8h.md#ab067e306959a0774ee5e896eafab2132)

static int vtd\_set\_irte\_irq(const struct device \*dev, uint8\_t irte\_idx, unsigned int irq)

Set the irq on the allocated irte.

**Definition** intel\_vtd.h:184

[vtd\_remap\_msi](drivers_2interrupt__controller_2intel__vtd_8h.md#ab7b8ad9dbee740c9e97021853f1131fc)

static uint32\_t vtd\_remap\_msi(const struct device \*dev, msi\_vector\_t \*vector, uint8\_t n\_vector)

Generate the MSI Message Address data for the given vector.

**Definition** intel\_vtd.h:89

[vtd\_set\_irte\_msi](drivers_2interrupt__controller_2intel__vtd_8h.md#ae81918a2c81e03cc4e02603781e8ca21)

static void vtd\_set\_irte\_msi(const struct device \*dev, uint8\_t irte\_idx, bool msi)

**Definition** intel\_vtd.h:211

[vtd\_get\_irte\_vector\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#af3ddf5e22fcb4956e4887e1982fae28e)

uint16\_t(\* vtd\_get\_irte\_vector\_f)(const struct device \*dev, uint8\_t irte\_idx)

**Definition** intel\_vtd.h:31

[vtd\_remap\_f](drivers_2interrupt__controller_2intel__vtd_8h.md#afefa59b2064053d90445127da9b64bfb)

int(\* vtd\_remap\_f)(const struct device \*dev, uint8\_t irte\_idx, uint16\_t vector, uint32\_t flags, uint16\_t src\_id)

**Definition** intel\_vtd.h:18

[msi\_vector\_t](group__pcie__host__msi__interface.md#ga9ede6a7a472ee62f0975256a1b5f1231)

struct msi\_vector msi\_vector\_t

**Definition** msi.h:60

[msi.h](msi_8h.md)

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:96

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[vtd\_driver\_api](structvtd__driver__api.md)

**Definition** intel\_vtd.h:48

[vtd\_driver\_api::set\_irte\_vector](structvtd__driver__api.md#a03236811cfc87b4653ba1a2f53bc50a1)

vtd\_set\_irte\_vector\_f set\_irte\_vector

**Definition** intel\_vtd.h:52

[vtd\_driver\_api::allocate\_entries](structvtd__driver__api.md#a3177c806bd86ebe4dc6c94141c9d5f04)

vtd\_alloc\_entries\_f allocate\_entries

**Definition** intel\_vtd.h:49

[vtd\_driver\_api::get\_irte\_by\_vector](structvtd__driver__api.md#a39157ec0077a20a900bbe19f3cc8d1b1)

vtd\_get\_irte\_by\_vector\_f get\_irte\_by\_vector

**Definition** intel\_vtd.h:53

[vtd\_driver\_api::remap\_msi](structvtd__driver__api.md#a97f93762584ea000a149ded0d726a993)

vtd\_remap\_msi\_f remap\_msi

**Definition** intel\_vtd.h:50

[vtd\_driver\_api::irte\_is\_msi](structvtd__driver__api.md#aac4ab98b9bf8a557cec22c685433888c)

vtd\_irte\_is\_msi\_f irte\_is\_msi

**Definition** intel\_vtd.h:58

[vtd\_driver\_api::remap](structvtd__driver__api.md#ac03cd6690017568b51d1b4bedd1fea09)

vtd\_remap\_f remap

**Definition** intel\_vtd.h:51

[vtd\_driver\_api::set\_irte\_msi](structvtd__driver__api.md#ac2fbdcfe7bcb0c9ef548aefe1c80b96b)

vtd\_set\_irte\_msi\_f set\_irte\_msi

**Definition** intel\_vtd.h:57

[vtd\_driver\_api::get\_irte\_vector](structvtd__driver__api.md#ac67dacb59216e44e55c832a26b87854f)

vtd\_get\_irte\_vector\_f get\_irte\_vector

**Definition** intel\_vtd.h:54

[vtd\_driver\_api::set\_irte\_irq](structvtd__driver__api.md#acc5af4aaaeed8abb8768d21767c67c58)

vtd\_set\_irte\_irq\_f set\_irte\_irq

**Definition** intel\_vtd.h:55

[vtd\_driver\_api::get\_irte\_by\_irq](structvtd__driver__api.md#adf1c688b60ef445581dee2344a48c8b6)

vtd\_get\_irte\_by\_irq\_f get\_irte\_by\_irq

**Definition** intel\_vtd.h:56

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [intel\_vtd.h](drivers_2interrupt__controller_2intel__vtd_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
