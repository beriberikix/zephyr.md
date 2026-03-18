---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/debug_2coredump_8h_source.html
original_path: doxygen/html/debug_2coredump_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

coredump.h

[Go to the documentation of this file.](debug_2coredump_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DEBUG\_COREDUMP\_H\_

8#define ZEPHYR\_INCLUDE\_DEBUG\_COREDUMP\_H\_

9

10#include <stddef.h>

11#include <[stdint.h](stdint_8h.md)>

12#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

13

14/\*

15 \* Define COREDUMP\_\*\_STR as public to allow coredump\_backend\_other to re-use

16 \* these strings if necessary

17 \*/

[ 18](debug_2coredump_8h.md#acc9e7259fd50fc8e2fb9cbbccb6b0638)#define COREDUMP\_BEGIN\_STR "BEGIN#"

[ 19](debug_2coredump_8h.md#a93ebd2883ffe26c5352c3b429fa62688)#define COREDUMP\_END\_STR "END#"

[ 20](debug_2coredump_8h.md#a2a1d82ed80cd3a715dd489beddbce57f)#define COREDUMP\_ERROR\_STR "ERROR CANNOT DUMP#"

21

22/\*

23 \* Need to prefix coredump strings to make it easier to parse

24 \* as log module adds its own prefixes.

25 \*/

[ 26](debug_2coredump_8h.md#a0a42d70f4a13d3b7c43627259992ba39)#define COREDUMP\_PREFIX\_STR "#CD:"

27

36

37

[ 39](group__coredump__apis.md#ga26360cadb6b43f5c86b59332e66008f5)enum [coredump\_query\_id](group__coredump__apis.md#ga26360cadb6b43f5c86b59332e66008f5) {

[ 43](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5afa7363b57e57c55fffa8cc9e9050d6cb) [COREDUMP\_QUERY\_GET\_ERROR](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5afa7363b57e57c55fffa8cc9e9050d6cb),

44

[ 53](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5a89f3cc157e790b8aa324d76a01b73e83) [COREDUMP\_QUERY\_HAS\_STORED\_DUMP](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5a89f3cc157e790b8aa324d76a01b73e83),

54

[ 61](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5ac3e34206cd358efdc1ed7a2996b98483) [COREDUMP\_QUERY\_GET\_STORED\_DUMP\_SIZE](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5ac3e34206cd358efdc1ed7a2996b98483),

62

[ 66](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5ae4a1cdeb5c337eae17d59a1d1f1d1e2d) [COREDUMP\_QUERY\_MAX](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5ae4a1cdeb5c337eae17d59a1d1f1d1e2d)

67};

68

[ 70](group__coredump__apis.md#ga48765a88d430aaec373a2ce6e4796578)enum [coredump\_cmd\_id](group__coredump__apis.md#ga48765a88d430aaec373a2ce6e4796578) {

[ 76](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578aef8cf1d85b2dfb2c911cb2abb7e3b38f) [COREDUMP\_CMD\_CLEAR\_ERROR](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578aef8cf1d85b2dfb2c911cb2abb7e3b38f),

77

[ 87](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578ab8f6dd3e8062175c9790bfe5d2b2aeaa) [COREDUMP\_CMD\_VERIFY\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578ab8f6dd3e8062175c9790bfe5d2b2aeaa),

88

[ 97](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578ab46f9f907e75e1187a6b7a2efd7e54f6) [COREDUMP\_CMD\_ERASE\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578ab46f9f907e75e1187a6b7a2efd7e54f6),

98

[ 108](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578a0cc9387829efa1f3c6f802217adc3819) [COREDUMP\_CMD\_COPY\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578a0cc9387829efa1f3c6f802217adc3819),

109

[ 119](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578aa45b8520053c56075a29441c27e4e321) [COREDUMP\_CMD\_INVALIDATE\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578aa45b8520053c56075a29441c27e4e321),

120

[ 124](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578a1b35195ff848aa9803bdcb4136e386c6) [COREDUMP\_CMD\_MAX](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578a1b35195ff848aa9803bdcb4136e386c6)

125};

126

[ 128](structcoredump__cmd__copy__arg.md)struct [coredump\_cmd\_copy\_arg](structcoredump__cmd__copy__arg.md) {

[ 130](structcoredump__cmd__copy__arg.md#a724583bd7203d16cc46f06698acfc6ef) [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [offset](structcoredump__cmd__copy__arg.md#a724583bd7203d16cc46f06698acfc6ef);

131

[ 133](structcoredump__cmd__copy__arg.md#a74495abb94670f983a3f136274485c40) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buffer](structcoredump__cmd__copy__arg.md#a74495abb94670f983a3f136274485c40);

134

[ 136](structcoredump__cmd__copy__arg.md#ae9266221235083dcf6efd7aba2177a75) size\_t [length](structcoredump__cmd__copy__arg.md#ae9266221235083dcf6efd7aba2177a75);

137};

138

139#ifdef CONFIG\_DEBUG\_COREDUMP

140

141#include <[zephyr/toolchain.h](toolchain_8h.md)>

142#include <[zephyr/arch/cpu.h](cpu_8h.md)>

143#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h.md)>

144

145#define COREDUMP\_HDR\_VER 1

146

147#define COREDUMP\_ARCH\_HDR\_ID 'A'

148

149#define COREDUMP\_MEM\_HDR\_ID 'M'

150#define COREDUMP\_MEM\_HDR\_VER 1

151

152/\* Target code \*/

153enum coredump\_tgt\_code {

154 COREDUMP\_TGT\_UNKNOWN = 0,

155 COREDUMP\_TGT\_X86,

156 COREDUMP\_TGT\_X86\_64,

157 COREDUMP\_TGT\_ARM\_CORTEX\_M,

158 COREDUMP\_TGT\_RISC\_V,

159 COREDUMP\_TGT\_XTENSA,

160 COREDUMP\_TGT\_ARM64,

161};

162

163/\* Coredump header \*/

164struct coredump\_hdr\_t {

165 /\* 'Z', 'E' \*/

166 char id[2];

167

168 /\* Header version \*/

169 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) hdr\_version;

170

171 /\* Target code \*/

172 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tgt\_code;

173

174 /\* Pointer size in Log2 \*/

175 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ptr\_size\_bits;

176

177 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) flag;

178

179 /\* Coredump Reason given \*/

180 unsigned int reason;

181} \_\_packed;

182

183/\* Architecture-specific block header \*/

184struct coredump\_arch\_hdr\_t {

185 /\* COREDUMP\_ARCH\_HDR\_ID \*/

186 char id;

187

188 /\* Header version \*/

189 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) hdr\_version;

190

191 /\* Number of bytes in this block (excluding header) \*/

192 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_bytes;

193} \_\_packed;

194

195/\* Memory block header \*/

196struct coredump\_mem\_hdr\_t {

197 /\* COREDUMP\_MEM\_HDR\_ID \*/

198 char id;

199

200 /\* Header version \*/

201 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) hdr\_version;

202

203 /\* Address of start of memory region \*/

204 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) start;

205

206 /\* Address of end of memory region \*/

207 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) end;

208} \_\_packed;

209

210typedef void (\*coredump\_backend\_start\_t)(void);

211typedef void (\*coredump\_backend\_end\_t)(void);

212typedef void (\*coredump\_backend\_buffer\_output\_t)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen);

213typedef int (\*coredump\_backend\_query\_t)(enum [coredump\_query\_id](group__coredump__apis.md#ga26360cadb6b43f5c86b59332e66008f5) query\_id,

214 void \*arg);

215typedef int (\*coredump\_backend\_cmd\_t)(enum [coredump\_cmd\_id](group__coredump__apis.md#ga48765a88d430aaec373a2ce6e4796578) cmd\_id,

216 void \*arg);

217

218struct coredump\_backend\_api {

219 /\* Signal to backend of the start of coredump. \*/

220 coredump\_backend\_start\_t start;

221

222 /\* Signal to backend of the end of coredump. \*/

223 coredump\_backend\_end\_t end;

224

225 /\* Raw buffer output \*/

226 coredump\_backend\_buffer\_output\_t buffer\_output;

227

228 /\* Perform query on backend \*/

229 coredump\_backend\_query\_t query;

230

231 /\* Perform command on backend \*/

232 coredump\_backend\_cmd\_t [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615);

233};

234

235void [coredump](group__coredump__apis.md#gab97503d4de13bdde139fe0880947379a)(unsigned int reason, const struct [arch\_esf](structarch__esf.md) \*esf,

236 struct [k\_thread](structk__thread.md) \*thread);

237void [coredump\_memory\_dump](group__coredump__apis.md#gab8823860579eee41380da8b7a4d93cd0)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) start\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) end\_addr);

238void [coredump\_buffer\_output](group__coredump__apis.md#gabe58e47cc733572a6650d3fd2cfc7d9d)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen);

239

240int [coredump\_query](group__coredump__apis.md#ga772697785da4247a7a8c3fccdbe921ce)(enum [coredump\_query\_id](group__coredump__apis.md#ga26360cadb6b43f5c86b59332e66008f5) query\_id, void \*arg);

241int [coredump\_cmd](group__coredump__apis.md#ga5c7f6fb24c724ede550d2c54f7ce2336)(enum [coredump\_cmd\_id](group__coredump__apis.md#ga48765a88d430aaec373a2ce6e4796578) cmd\_id, void \*arg);

242

243#else

244

[ 245](group__coredump__apis.md#gab97503d4de13bdde139fe0880947379a)static inline void [coredump](group__coredump__apis.md#gab97503d4de13bdde139fe0880947379a)(unsigned int reason, const struct [arch\_esf](structarch__esf.md) \*esf,

246 struct [k\_thread](structk__thread.md) \*thread)

247{

248 ARG\_UNUSED(reason);

249 ARG\_UNUSED(esf);

250 ARG\_UNUSED(thread);

251}

252

[ 253](group__coredump__apis.md#gab8823860579eee41380da8b7a4d93cd0)static inline void [coredump\_memory\_dump](group__coredump__apis.md#gab8823860579eee41380da8b7a4d93cd0)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) start\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) end\_addr)

254{

255 ARG\_UNUSED(start\_addr);

256 ARG\_UNUSED(end\_addr);

257}

258

[ 259](group__coredump__apis.md#gabe58e47cc733572a6650d3fd2cfc7d9d)static inline void [coredump\_buffer\_output](group__coredump__apis.md#gabe58e47cc733572a6650d3fd2cfc7d9d)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen)

260{

261 ARG\_UNUSED(buf);

262 ARG\_UNUSED(buflen);

263}

264

[ 265](group__coredump__apis.md#ga772697785da4247a7a8c3fccdbe921ce)static inline int [coredump\_query](group__coredump__apis.md#ga772697785da4247a7a8c3fccdbe921ce)(enum [coredump\_query\_id](group__coredump__apis.md#ga26360cadb6b43f5c86b59332e66008f5) query\_id, void \*arg)

266{

267 ARG\_UNUSED(query\_id);

268 ARG\_UNUSED(arg);

269 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

270}

271

[ 272](group__coredump__apis.md#ga5c7f6fb24c724ede550d2c54f7ce2336)static inline int [coredump\_cmd](group__coredump__apis.md#ga5c7f6fb24c724ede550d2c54f7ce2336)(enum [coredump\_cmd\_id](group__coredump__apis.md#ga48765a88d430aaec373a2ce6e4796578) query\_id, void \*arg)

273{

274 ARG\_UNUSED(query\_id);

275 ARG\_UNUSED(arg);

276 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

277}

278

279#endif /\* CONFIG\_DEBUG\_COREDUMP \*/

280

293

301

313

325

337

341

342#endif /\* ZEPHYR\_INCLUDE\_DEBUG\_COREDUMP\_H\_ \*/

[cpu.h](cpu_8h.md)

[coredump\_query\_id](group__coredump__apis.md#ga26360cadb6b43f5c86b59332e66008f5)

coredump\_query\_id

Query ID.

**Definition** coredump.h:39

[coredump\_cmd\_id](group__coredump__apis.md#ga48765a88d430aaec373a2ce6e4796578)

coredump\_cmd\_id

Command ID.

**Definition** coredump.h:70

[coredump\_cmd](group__coredump__apis.md#ga5c7f6fb24c724ede550d2c54f7ce2336)

static int coredump\_cmd(enum coredump\_cmd\_id query\_id, void \*arg)

Perform command on coredump subsystem.

**Definition** coredump.h:272

[coredump\_query](group__coredump__apis.md#ga772697785da4247a7a8c3fccdbe921ce)

static int coredump\_query(enum coredump\_query\_id query\_id, void \*arg)

Perform query on coredump subsystem.

**Definition** coredump.h:265

[coredump\_memory\_dump](group__coredump__apis.md#gab8823860579eee41380da8b7a4d93cd0)

static void coredump\_memory\_dump(uintptr\_t start\_addr, uintptr\_t end\_addr)

Dump memory region.

**Definition** coredump.h:253

[coredump](group__coredump__apis.md#gab97503d4de13bdde139fe0880947379a)

static void coredump(unsigned int reason, const struct arch\_esf \*esf, struct k\_thread \*thread)

Perform coredump.

**Definition** coredump.h:245

[coredump\_buffer\_output](group__coredump__apis.md#gabe58e47cc733572a6650d3fd2cfc7d9d)

static void coredump\_buffer\_output(uint8\_t \*buf, size\_t buflen)

Output the buffer via coredump.

**Definition** coredump.h:259

[COREDUMP\_QUERY\_HAS\_STORED\_DUMP](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5a89f3cc157e790b8aa324d76a01b73e83)

@ COREDUMP\_QUERY\_HAS\_STORED\_DUMP

Check if there is a stored coredump from backend.

**Definition** coredump.h:53

[COREDUMP\_QUERY\_GET\_STORED\_DUMP\_SIZE](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5ac3e34206cd358efdc1ed7a2996b98483)

@ COREDUMP\_QUERY\_GET\_STORED\_DUMP\_SIZE

Returns:

**Definition** coredump.h:61

[COREDUMP\_QUERY\_MAX](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5ae4a1cdeb5c337eae17d59a1d1f1d1e2d)

@ COREDUMP\_QUERY\_MAX

Max value for query ID.

**Definition** coredump.h:66

[COREDUMP\_QUERY\_GET\_ERROR](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5afa7363b57e57c55fffa8cc9e9050d6cb)

@ COREDUMP\_QUERY\_GET\_ERROR

Returns error code from backend.

**Definition** coredump.h:43

[COREDUMP\_CMD\_COPY\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578a0cc9387829efa1f3c6f802217adc3819)

@ COREDUMP\_CMD\_COPY\_STORED\_DUMP

Copy the raw stored coredump.

**Definition** coredump.h:108

[COREDUMP\_CMD\_MAX](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578a1b35195ff848aa9803bdcb4136e386c6)

@ COREDUMP\_CMD\_MAX

Max value for command ID.

**Definition** coredump.h:124

[COREDUMP\_CMD\_INVALIDATE\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578aa45b8520053c56075a29441c27e4e321)

@ COREDUMP\_CMD\_INVALIDATE\_STORED\_DUMP

Invalidate the stored coredump.

**Definition** coredump.h:119

[COREDUMP\_CMD\_ERASE\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578ab46f9f907e75e1187a6b7a2efd7e54f6)

@ COREDUMP\_CMD\_ERASE\_STORED\_DUMP

Erase the stored coredump.

**Definition** coredump.h:97

[COREDUMP\_CMD\_VERIFY\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578ab8f6dd3e8062175c9790bfe5d2b2aeaa)

@ COREDUMP\_CMD\_VERIFY\_STORED\_DUMP

Verify that the stored coredump is valid.

**Definition** coredump.h:87

[COREDUMP\_CMD\_CLEAR\_ERROR](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578aef8cf1d85b2dfb2c911cb2abb7e3b38f)

@ COREDUMP\_CMD\_CLEAR\_ERROR

Clear error code from backend.

**Definition** coredump.h:76

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:114

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f)

\_\_INTPTR\_TYPE\_\_ off\_t

**Definition** types.h:36

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[arch\_esf](structarch__esf.md)

Exception Stack Frame.

**Definition** exception.h:57

[coredump\_cmd\_copy\_arg](structcoredump__cmd__copy__arg.md)

Coredump copy command (COREDUMP\_CMD\_COPY\_STORED\_DUMP) argument definition.

**Definition** coredump.h:128

[coredump\_cmd\_copy\_arg::offset](structcoredump__cmd__copy__arg.md#a724583bd7203d16cc46f06698acfc6ef)

off\_t offset

Copy offset.

**Definition** coredump.h:130

[coredump\_cmd\_copy\_arg::buffer](structcoredump__cmd__copy__arg.md#a74495abb94670f983a3f136274485c40)

uint8\_t \* buffer

Copy destination buffer.

**Definition** coredump.h:133

[coredump\_cmd\_copy\_arg::length](structcoredump__cmd__copy__arg.md#ae9266221235083dcf6efd7aba2177a75)

size\_t length

Copy length.

**Definition** coredump.h:136

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:259

[byteorder.h](sys_2byteorder_8h.md)

Byte order helpers.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [coredump.h](debug_2coredump_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
