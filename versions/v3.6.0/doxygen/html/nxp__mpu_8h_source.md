---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/nxp__mpu_8h_source.html
original_path: doxygen/html/nxp__mpu_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nxp\_mpu.h

[Go to the documentation of this file.](nxp__mpu_8h.md)

1/\*

2 \* Copyright (c) 2017 Linaro Limited.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_ARCH\_ARM\_MPU\_NXP\_MPU\_H\_

7#define ZEPHYR\_INCLUDE\_ARCH\_ARM\_MPU\_NXP\_MPU\_H\_

8

9#ifndef \_ASMLANGUAGE

10

[ 11](nxp__mpu_8h.md#a21a1ac0d36f7afb791f73b4266c29f70)#define NXP\_MPU\_REGION\_NUMBER 12

12

13/\* Bus Master User Mode Access \*/

[ 14](nxp__mpu_8h.md#a7b4052cfa2a098b33448fd381ce154a9)#define UM\_READ 4

[ 15](nxp__mpu_8h.md#aef84434979e31bb7c9b90ddaa17b4ffd)#define UM\_WRITE 2

[ 16](nxp__mpu_8h.md#ab5140794b05a3c2331d97ba4a3c4ed26)#define UM\_EXEC 1

17

[ 18](nxp__mpu_8h.md#a827ffa4bfa173421765be3af7d732b7d)#define BM0\_UM\_SHIFT 0

[ 19](nxp__mpu_8h.md#ab241d9fcbae38cab7dae9f38c5ec69f6)#define BM1\_UM\_SHIFT 6

[ 20](nxp__mpu_8h.md#a43b74013e6cc3fd0263efd3dfb2083fc)#define BM2\_UM\_SHIFT 12

[ 21](nxp__mpu_8h.md#a398f479f1d9a9085d75b1b5cdf62968b)#define BM3\_UM\_SHIFT 18

22

23/\* Bus Master Supervisor Mode Access \*/

[ 24](nxp__mpu_8h.md#aeec3e5dfce7d167654f6073a0dac731e)#define SM\_RWX\_ALLOW 0

[ 25](nxp__mpu_8h.md#a15ac6f38d430aa401c2df437a095e8af)#define SM\_RX\_ALLOW 1

[ 26](nxp__mpu_8h.md#ac834b1a3618a4a361a766de8d8d9b729)#define SM\_RW\_ALLOW 2

[ 27](nxp__mpu_8h.md#a9c450188b4f476319609a5eff9981013)#define SM\_SAME\_AS\_UM 3

28

[ 29](nxp__mpu_8h.md#a9a682bd5d2dfd42b17a251e7d75df108)#define BM0\_SM\_SHIFT 3

[ 30](nxp__mpu_8h.md#ab37c2c0b12942cb036dab45b213446fd)#define BM1\_SM\_SHIFT 9

[ 31](nxp__mpu_8h.md#a1a07f20ecd6d1b553477a4d1b689e215)#define BM2\_SM\_SHIFT 15

[ 32](nxp__mpu_8h.md#ac4701e5b2dabd074952b8a146f2752bb)#define BM3\_SM\_SHIFT 21

33

[ 34](nxp__mpu_8h.md#a1bf58e90c0e0c756d46a312e49d257ac)#define BM4\_WE\_SHIFT 24

[ 35](nxp__mpu_8h.md#a1eb38fe0712d071cb776310123402946)#define BM4\_RE\_SHIFT 25

36

37#if CONFIG\_USB\_KINETIS || CONFIG\_UDC\_KINETIS

38#define BM4\_PERMISSIONS ((1 << BM4\_RE\_SHIFT) | (1 << BM4\_WE\_SHIFT))

39#else

[ 40](nxp__mpu_8h.md#a5714f056c45e223a683a59a7fc6997a7)#define BM4\_PERMISSIONS 0

41#endif

42

43/\* Read Attribute \*/

[ 44](nxp__mpu_8h.md#aaf9c10295c149cc7f843d52a9993bc6e)#define MPU\_REGION\_READ ((UM\_READ << BM0\_UM\_SHIFT) | \

45 (UM\_READ << BM1\_UM\_SHIFT) | \

46 (UM\_READ << BM2\_UM\_SHIFT) | \

47 (UM\_READ << BM3\_UM\_SHIFT))

48

49/\* Write Attribute \*/

[ 50](nxp__mpu_8h.md#a0c9f505077068c3466e0c5a147a77874)#define MPU\_REGION\_WRITE ((UM\_WRITE << BM0\_UM\_SHIFT) | \

51 (UM\_WRITE << BM1\_UM\_SHIFT) | \

52 (UM\_WRITE << BM2\_UM\_SHIFT) | \

53 (UM\_WRITE << BM3\_UM\_SHIFT))

54

55/\* Execute Attribute \*/

[ 56](nxp__mpu_8h.md#aecde7abc56ba1104be002a478cb68c52)#define MPU\_REGION\_EXEC ((UM\_EXEC << BM0\_UM\_SHIFT) | \

57 (UM\_EXEC << BM1\_UM\_SHIFT) | \

58 (UM\_EXEC << BM2\_UM\_SHIFT) | \

59 (UM\_EXEC << BM3\_UM\_SHIFT))

60

61/\* Super User Attributes \*/

[ 62](nxp__mpu_8h.md#a9efc4e45f22f3dab38d72bd45ff98019)#define MPU\_REGION\_SU ((SM\_SAME\_AS\_UM << BM0\_SM\_SHIFT) | \

63 (SM\_SAME\_AS\_UM << BM1\_SM\_SHIFT) | \

64 (SM\_SAME\_AS\_UM << BM2\_SM\_SHIFT) | \

65 (SM\_SAME\_AS\_UM << BM3\_SM\_SHIFT))

66

[ 67](nxp__mpu_8h.md#a95d67eb3ec1451fdb29f8d813719a349)#define MPU\_REGION\_SU\_RX ((SM\_RX\_ALLOW << BM0\_SM\_SHIFT) | \

68 (SM\_RX\_ALLOW << BM1\_SM\_SHIFT) | \

69 (SM\_RX\_ALLOW << BM2\_SM\_SHIFT) | \

70 (SM\_RX\_ALLOW << BM3\_SM\_SHIFT))

71

[ 72](nxp__mpu_8h.md#afe53263c929f7b16590ce575b813a810)#define MPU\_REGION\_SU\_RW ((SM\_RW\_ALLOW << BM0\_SM\_SHIFT) | \

73 (SM\_RW\_ALLOW << BM1\_SM\_SHIFT) | \

74 (SM\_RW\_ALLOW << BM2\_SM\_SHIFT) | \

75 (SM\_RW\_ALLOW << BM3\_SM\_SHIFT))

76

[ 77](nxp__mpu_8h.md#ab385c5e2584e7397e1664233d0e1a88b)#define MPU\_REGION\_SU\_RWX ((SM\_RWX\_ALLOW << BM0\_SM\_SHIFT) | \

78 (SM\_RWX\_ALLOW << BM1\_SM\_SHIFT) | \

79 (SM\_RWX\_ALLOW << BM2\_SM\_SHIFT) | \

80 (SM\_RWX\_ALLOW << BM3\_SM\_SHIFT))

81

82/\* The ENDADDR field has the last 5 bit reserved and set to 1 \*/

[ 83](nxp__mpu_8h.md#a754d89dc3b794e45d432b48a6f65919e)#define ENDADDR\_ROUND(x) (x - 0x1F)

84

[ 85](nxp__mpu_8h.md#a83037f3495bf5755e88d39bbf4a259aa)#define REGION\_USER\_MODE\_ATTR {(MPU\_REGION\_READ | \

86 MPU\_REGION\_WRITE | \

87 MPU\_REGION\_SU)}

88

89/\* Some helper defines for common regions \*/

90#if defined(CONFIG\_MPU\_ALLOW\_FLASH\_WRITE)

91#define REGION\_RAM\_ATTR {((MPU\_REGION\_SU\_RWX) | \

92 ((UM\_READ | UM\_WRITE | UM\_EXEC) << BM3\_UM\_SHIFT) | \

93 (BM4\_PERMISSIONS))}

94

95#define REGION\_FLASH\_ATTR {(MPU\_REGION\_SU\_RWX)}

96

97#else

[ 98](nxp__mpu_8h.md#a859d811feecb32c788b16a413e1b4781)#define REGION\_RAM\_ATTR {((MPU\_REGION\_SU\_RW) | \

99 ((UM\_READ | UM\_WRITE) << BM3\_UM\_SHIFT) | \

100 (BM4\_PERMISSIONS))}

101

[ 102](nxp__mpu_8h.md#aef333777108782979d84344af4bc51d6)#define REGION\_FLASH\_ATTR {(MPU\_REGION\_READ | \

103 MPU\_REGION\_EXEC | \

104 MPU\_REGION\_SU)}

105#endif

106

[ 107](nxp__mpu_8h.md#a4ce0d123898b8cb22cb161c8d69c411f)#define REGION\_IO\_ATTR {(MPU\_REGION\_READ | \

108 MPU\_REGION\_WRITE | \

109 MPU\_REGION\_EXEC | \

110 MPU\_REGION\_SU)}

111

[ 112](nxp__mpu_8h.md#af0fd70c24b3a61a7587a486c8035f305)#define REGION\_RO\_ATTR {(MPU\_REGION\_READ | MPU\_REGION\_SU)}

113

[ 114](nxp__mpu_8h.md#aa0fe2dcd3799fe21fa51d87f7ce0e28f)#define REGION\_USER\_RO\_ATTR {(MPU\_REGION\_READ | \

115 MPU\_REGION\_SU)}

116

117/\* ENET (Master 3) and USB (Master 4) devices will not be able

118to access RAM when the region is dynamically disabled in NXP MPU.

119DEBUGGER (Master 1) can't be disabled in Region 0. \*/

[ 120](nxp__mpu_8h.md#adf8f684a3f851ee1915f7d11cb44fc77)#define REGION\_DEBUGGER\_AND\_DEVICE\_ATTR {((MPU\_REGION\_SU) | \

121 ((UM\_READ | UM\_WRITE) << BM3\_UM\_SHIFT) | \

122 (BM4\_PERMISSIONS))}

123

[ 124](nxp__mpu_8h.md#a92c302d8df1ca631080e48e30e5ce14d)#define REGION\_DEBUG\_ATTR {MPU\_REGION\_SU}

125

[ 126](nxp__mpu_8h.md#a96b453ef40506d7d33e28cd48bcc6de3)#define REGION\_BACKGROUND\_ATTR {MPU\_REGION\_SU\_RW}

127

[ 128](structnxp__mpu__region__attr.md)struct [nxp\_mpu\_region\_attr](structnxp__mpu__region__attr.md) {

129 /\* NXP MPU region access permission attributes \*/

[ 130](structnxp__mpu__region__attr.md#aed105c7df45c7b9dd4c2a0bf89f6b16f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [attr](structnxp__mpu__region__attr.md#aed105c7df45c7b9dd4c2a0bf89f6b16f);

131};

132

[ 133](nxp__mpu_8h.md#ab9cc02d4320ccbc4385061ce7b92ced0)typedef struct [nxp\_mpu\_region\_attr](structnxp__mpu__region__attr.md) [nxp\_mpu\_region\_attr\_t](nxp__mpu_8h.md#ab9cc02d4320ccbc4385061ce7b92ced0);

134

135/\* Typedef for the k\_mem\_partition attribute\*/

136typedef struct {

[ 137](structk__mem__partition__attr__t.md#aeb16f8a8402a7190081ac96093189f27) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ap\_attr](structk__mem__partition__attr__t.md#aeb16f8a8402a7190081ac96093189f27);

138} [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md);

139

140/\* Kernel macros for memory attribution

141 \* (access permissions and cache-ability).

142 \*

143 \* The macros are to be stored in k\_mem\_partition\_attr\_t

144 \* objects.

145 \*/

146

147/\* Read-Write access permission attributes \*/

[ 148](nxp__mpu_8h.md#a73bc6803ccf24aad395089a4395bd22f)#define K\_MEM\_PARTITION\_P\_NA\_U\_NA ((k\_mem\_partition\_attr\_t) \

149 {(MPU\_REGION\_SU)})

[ 150](nxp__mpu_8h.md#a9b7cc3c51f518517031d76807470aa10)#define K\_MEM\_PARTITION\_P\_RW\_U\_RW ((k\_mem\_partition\_attr\_t) \

151 {(MPU\_REGION\_READ | MPU\_REGION\_WRITE | MPU\_REGION\_SU)})

[ 152](nxp__mpu_8h.md#a6636a59c913e035646a1a9e5ed61559d)#define K\_MEM\_PARTITION\_P\_RW\_U\_RO ((k\_mem\_partition\_attr\_t) \

153 {(MPU\_REGION\_READ | MPU\_REGION\_SU\_RW)})

[ 154](nxp__mpu_8h.md#a3c52d13e42a66beb72d088ac56388951)#define K\_MEM\_PARTITION\_P\_RW\_U\_NA ((k\_mem\_partition\_attr\_t) \

155 {(MPU\_REGION\_SU\_RW)})

[ 156](nxp__mpu_8h.md#a708338371e91b5a3f2d44f9ae48849db)#define K\_MEM\_PARTITION\_P\_RO\_U\_RO ((k\_mem\_partition\_attr\_t) \

157 {(MPU\_REGION\_READ | MPU\_REGION\_SU)})

[ 158](nxp__mpu_8h.md#a706eaa9c515f1cc859d97ef8455b2f2f)#define K\_MEM\_PARTITION\_P\_RO\_U\_NA ((k\_mem\_partition\_attr\_t) \

159 {(MPU\_REGION\_SU\_RX)})

160

161/\* Execution-allowed attributes \*/

[ 162](nxp__mpu_8h.md#a29db5fb48087c0cae596ff212989ed24)#define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX ((k\_mem\_partition\_attr\_t) \

163 {(MPU\_REGION\_READ | MPU\_REGION\_WRITE | \

164 MPU\_REGION\_EXEC | MPU\_REGION\_SU)})

[ 165](nxp__mpu_8h.md#a81878d7a3177ef4c37ea3046da004c9a)#define K\_MEM\_PARTITION\_P\_RWX\_U\_RX ((k\_mem\_partition\_attr\_t) \

166 {(MPU\_REGION\_READ | MPU\_REGION\_EXEC | MPU\_REGION\_SU\_RWX)})

[ 167](nxp__mpu_8h.md#a78f9b21aa8b5c894db28328f5a1e2641)#define K\_MEM\_PARTITION\_P\_RX\_U\_RX ((k\_mem\_partition\_attr\_t) \

168 {(MPU\_REGION\_READ | MPU\_REGION\_EXEC | MPU\_REGION\_SU)})

169

170/\*

171 \* @brief Evaluate Write-ability

172 \*

173 \* Evaluate whether the access permissions include write-ability.

174 \*

175 \* @param attr The k\_mem\_partition\_attr\_t object holding the

176 \* MPU attributes to be checked against write-ability.

177 \*/

[ 178](nxp__mpu_8h.md#a7879968909ce2f0e33763ae1e2fc9d84)#define K\_MEM\_PARTITION\_IS\_WRITABLE(attr) \

179 ({ \

180 int \_\_is\_writable\_\_; \

181 switch (attr.ap\_attr) { \

182 case MPU\_REGION\_WRITE: \

183 case MPU\_REGION\_SU\_RW: \

184 \_\_is\_writable\_\_ = 1; \

185 break; \

186 default: \

187 \_\_is\_writable\_\_ = 0; \

188 } \

189 \_\_is\_writable\_\_; \

190 })

191

192/\*

193 \* @brief Evaluate Execution allowance

194 \*

195 \* Evaluate whether the access permissions include execution.

196 \*

197 \* @param attr The k\_mem\_partition\_attr\_t object holding the

198 \* MPU attributes to be checked against execution

199 \* allowance.

200 \*/

[ 201](nxp__mpu_8h.md#ab6fb9b9c6c1c968a11ae80bfd70fec26)#define K\_MEM\_PARTITION\_IS\_EXECUTABLE(attr) \

202 ({ \

203 int \_\_is\_executable\_\_; \

204 switch (attr.ap\_attr) { \

205 case MPU\_REGION\_SU\_RX: \

206 case MPU\_REGION\_EXEC: \

207 \_\_is\_executable\_\_ = 1; \

208 break; \

209 default: \

210 \_\_is\_executable\_\_ = 0; \

211 } \

212 \_\_is\_executable\_\_; \

213 })

214

215

216/\* Region definition data structure \*/

[ 217](structnxp__mpu__region.md)struct [nxp\_mpu\_region](structnxp__mpu__region.md) {

218 /\* Region Base Address \*/

[ 219](structnxp__mpu__region.md#a3289584e6804b01dae4c48cf0d747b24) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [base](structnxp__mpu__region.md#a3289584e6804b01dae4c48cf0d747b24);

220 /\* Region End Address \*/

[ 221](structnxp__mpu__region.md#aa983eb7eab91684bbd4748aad8157de6) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [end](structnxp__mpu__region.md#aa983eb7eab91684bbd4748aad8157de6);

222 /\* Region Name \*/

[ 223](structnxp__mpu__region.md#a406476152c7d20e03129e7fe7c9ea21d) const char \*[name](structnxp__mpu__region.md#a406476152c7d20e03129e7fe7c9ea21d);

224 /\* Region Attributes \*/

[ 225](structnxp__mpu__region.md#ae65b1431b50409b1db810dd7f286e286) [nxp\_mpu\_region\_attr\_t](nxp__mpu_8h.md#ab9cc02d4320ccbc4385061ce7b92ced0) [attr](structnxp__mpu__region.md#ae65b1431b50409b1db810dd7f286e286);

226};

227

[ 228](nxp__mpu_8h.md#aa8d5b264821eea9086eadc256c1af90f)#define MPU\_REGION\_ENTRY(\_name, \_base, \_end, \_attr) \

229 {\

230 .name = \_name, \

231 .base = \_base, \

232 .end = \_end, \

233 .attr = \_attr, \

234 }

235

236/\* MPU configuration data structure \*/

[ 237](structnxp__mpu__config.md)struct [nxp\_mpu\_config](structnxp__mpu__config.md) {

238 /\* Number of regions \*/

[ 239](structnxp__mpu__config.md#ad51325039b504a0e74c59d4d87e0ed33) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [num\_regions](structnxp__mpu__config.md#ad51325039b504a0e74c59d4d87e0ed33);

240 /\* Regions \*/

[ 241](structnxp__mpu__config.md#a6d352013a71a0fc84d0d2736157dc05b) const struct [nxp\_mpu\_region](structnxp__mpu__region.md) \*[mpu\_regions](structnxp__mpu__config.md#a6d352013a71a0fc84d0d2736157dc05b);

242 /\* SRAM Region \*/

[ 243](structnxp__mpu__config.md#a455003984c04d83251e3324ad56715fa) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sram\_region](structnxp__mpu__config.md#a455003984c04d83251e3324ad56715fa);

244};

245

246/\* Reference to the MPU configuration.

247 \*

248 \* This struct is defined and populated for each SoC (in the SoC definition),

249 \* and holds the build-time configuration information for the fixed MPU

250 \* regions enabled during kernel initialization. Dynamic MPU regions (e.g.

251 \* for Thread Stack, Stack Guards, etc.) are programmed during runtime, thus,

252 \* not kept here.

253 \*/

254extern const struct [nxp\_mpu\_config](structnxp__mpu__config.md) [mpu\_config](arc__mpu_8h.md#a347b2bb6c23b874d7a20d4b5ce4d23b1);

255

256#endif /\* \_ASMLANGUAGE \*/

257

258#define \_ARCH\_MEM\_PARTITION\_ALIGN\_CHECK(start, size) \

259 BUILD\_ASSERT((size) % \

260 CONFIG\_ARM\_MPU\_REGION\_MIN\_ALIGN\_AND\_SIZE == 0 && \

261 (size) >= CONFIG\_ARM\_MPU\_REGION\_MIN\_ALIGN\_AND\_SIZE && \

262 (uint32\_t)(start) % CONFIG\_ARM\_MPU\_REGION\_MIN\_ALIGN\_AND\_SIZE == 0, \

263 "the size of the partition must align with minimum MPU \

264 region size" \

265 " and greater than or equal to minimum MPU region size." \

266 "start address of the partition must align with minimum MPU \

267 region size.")

268

269#endif /\* ZEPHYR\_INCLUDE\_ARCH\_ARM\_MPU\_NXP\_MPU\_H\_ \*/

[mpu\_config](arc__mpu_8h.md#a347b2bb6c23b874d7a20d4b5ce4d23b1)

struct arc\_mpu\_config mpu\_config

[nxp\_mpu\_region\_attr\_t](nxp__mpu_8h.md#ab9cc02d4320ccbc4385061ce7b92ced0)

struct nxp\_mpu\_region\_attr nxp\_mpu\_region\_attr\_t

**Definition** nxp\_mpu.h:133

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:160

[k\_mem\_partition\_attr\_t::ap\_attr](structk__mem__partition__attr__t.md#aeb16f8a8402a7190081ac96093189f27)

uint32\_t ap\_attr

**Definition** nxp\_mpu.h:137

[nxp\_mpu\_config](structnxp__mpu__config.md)

**Definition** nxp\_mpu.h:237

[nxp\_mpu\_config::sram\_region](structnxp__mpu__config.md#a455003984c04d83251e3324ad56715fa)

uint32\_t sram\_region

**Definition** nxp\_mpu.h:243

[nxp\_mpu\_config::mpu\_regions](structnxp__mpu__config.md#a6d352013a71a0fc84d0d2736157dc05b)

const struct nxp\_mpu\_region \* mpu\_regions

**Definition** nxp\_mpu.h:241

[nxp\_mpu\_config::num\_regions](structnxp__mpu__config.md#ad51325039b504a0e74c59d4d87e0ed33)

uint32\_t num\_regions

**Definition** nxp\_mpu.h:239

[nxp\_mpu\_region\_attr](structnxp__mpu__region__attr.md)

**Definition** nxp\_mpu.h:128

[nxp\_mpu\_region\_attr::attr](structnxp__mpu__region__attr.md#aed105c7df45c7b9dd4c2a0bf89f6b16f)

uint32\_t attr

**Definition** nxp\_mpu.h:130

[nxp\_mpu\_region](structnxp__mpu__region.md)

**Definition** nxp\_mpu.h:217

[nxp\_mpu\_region::base](structnxp__mpu__region.md#a3289584e6804b01dae4c48cf0d747b24)

uint32\_t base

**Definition** nxp\_mpu.h:219

[nxp\_mpu\_region::name](structnxp__mpu__region.md#a406476152c7d20e03129e7fe7c9ea21d)

const char \* name

**Definition** nxp\_mpu.h:223

[nxp\_mpu\_region::end](structnxp__mpu__region.md#aa983eb7eab91684bbd4748aad8157de6)

uint32\_t end

**Definition** nxp\_mpu.h:221

[nxp\_mpu\_region::attr](structnxp__mpu__region.md#ae65b1431b50409b1db810dd7f286e286)

nxp\_mpu\_region\_attr\_t attr

**Definition** nxp\_mpu.h:225

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [mpu](dir_56106ba8e9de679e2771f91f794159ff.md)
- [nxp\_mpu.h](nxp__mpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
