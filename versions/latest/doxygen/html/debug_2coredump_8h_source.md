---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/debug_2coredump_8h_source.html
original_path: doxygen/html/debug_2coredump_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

14

23

24

[ 26](group__coredump__apis.md#ga26360cadb6b43f5c86b59332e66008f5)enum [coredump\_query\_id](group__coredump__apis.md#ga26360cadb6b43f5c86b59332e66008f5) {

[ 30](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5afa7363b57e57c55fffa8cc9e9050d6cb) [COREDUMP\_QUERY\_GET\_ERROR](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5afa7363b57e57c55fffa8cc9e9050d6cb),

31

[ 40](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5a89f3cc157e790b8aa324d76a01b73e83) [COREDUMP\_QUERY\_HAS\_STORED\_DUMP](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5a89f3cc157e790b8aa324d76a01b73e83),

41

[ 48](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5ac3e34206cd358efdc1ed7a2996b98483) [COREDUMP\_QUERY\_GET\_STORED\_DUMP\_SIZE](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5ac3e34206cd358efdc1ed7a2996b98483),

49

[ 53](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5ae4a1cdeb5c337eae17d59a1d1f1d1e2d) [COREDUMP\_QUERY\_MAX](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5ae4a1cdeb5c337eae17d59a1d1f1d1e2d)

54};

55

[ 57](group__coredump__apis.md#ga48765a88d430aaec373a2ce6e4796578)enum [coredump\_cmd\_id](group__coredump__apis.md#ga48765a88d430aaec373a2ce6e4796578) {

[ 63](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578aef8cf1d85b2dfb2c911cb2abb7e3b38f) [COREDUMP\_CMD\_CLEAR\_ERROR](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578aef8cf1d85b2dfb2c911cb2abb7e3b38f),

64

[ 74](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578ab8f6dd3e8062175c9790bfe5d2b2aeaa) [COREDUMP\_CMD\_VERIFY\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578ab8f6dd3e8062175c9790bfe5d2b2aeaa),

75

[ 84](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578ab46f9f907e75e1187a6b7a2efd7e54f6) [COREDUMP\_CMD\_ERASE\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578ab46f9f907e75e1187a6b7a2efd7e54f6),

85

[ 95](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578a0cc9387829efa1f3c6f802217adc3819) [COREDUMP\_CMD\_COPY\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578a0cc9387829efa1f3c6f802217adc3819),

96

[ 106](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578aa45b8520053c56075a29441c27e4e321) [COREDUMP\_CMD\_INVALIDATE\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578aa45b8520053c56075a29441c27e4e321),

107

[ 111](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578a1b35195ff848aa9803bdcb4136e386c6) [COREDUMP\_CMD\_MAX](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578a1b35195ff848aa9803bdcb4136e386c6)

112};

113

[ 115](structcoredump__cmd__copy__arg.md)struct [coredump\_cmd\_copy\_arg](structcoredump__cmd__copy__arg.md) {

[ 117](structcoredump__cmd__copy__arg.md#a724583bd7203d16cc46f06698acfc6ef) [off\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a98a5cc5f4a350bf5652565021a2f239f) [offset](structcoredump__cmd__copy__arg.md#a724583bd7203d16cc46f06698acfc6ef);

118

[ 120](structcoredump__cmd__copy__arg.md#a74495abb94670f983a3f136274485c40) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buffer](structcoredump__cmd__copy__arg.md#a74495abb94670f983a3f136274485c40);

121

[ 123](structcoredump__cmd__copy__arg.md#ae9266221235083dcf6efd7aba2177a75) size\_t [length](structcoredump__cmd__copy__arg.md#ae9266221235083dcf6efd7aba2177a75);

124};

125

126#ifdef CONFIG\_DEBUG\_COREDUMP

127

128#include <[zephyr/toolchain.h](toolchain_8h.md)>

129#include <zephyr/arch/cpu.h>

130#include <[zephyr/sys/byteorder.h](sys_2byteorder_8h.md)>

131

132#define COREDUMP\_HDR\_VER 1

133

134#define COREDUMP\_ARCH\_HDR\_ID 'A'

135

136#define COREDUMP\_MEM\_HDR\_ID 'M'

137#define COREDUMP\_MEM\_HDR\_VER 1

138

139/\* Target code \*/

140enum coredump\_tgt\_code {

141 COREDUMP\_TGT\_UNKNOWN = 0,

142 COREDUMP\_TGT\_X86,

143 COREDUMP\_TGT\_X86\_64,

144 COREDUMP\_TGT\_ARM\_CORTEX\_M,

145 COREDUMP\_TGT\_RISC\_V,

146 COREDUMP\_TGT\_XTENSA,

147 COREDUMP\_TGT\_ARM64,

148};

149

150/\* Coredump header \*/

151struct coredump\_hdr\_t {

152 /\* 'Z', 'E' \*/

153 char id[2];

154

155 /\* Header version \*/

156 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) hdr\_version;

157

158 /\* Target code \*/

159 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tgt\_code;

160

161 /\* Pointer size in Log2 \*/

162 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ptr\_size\_bits;

163

164 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) flag;

165

166 /\* Coredump Reason given \*/

167 unsigned int reason;

168} \_\_packed;

169

170/\* Architecture-specific block header \*/

171struct coredump\_arch\_hdr\_t {

172 /\* COREDUMP\_ARCH\_HDR\_ID \*/

173 char id;

174

175 /\* Header version \*/

176 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) hdr\_version;

177

178 /\* Number of bytes in this block (excluding header) \*/

179 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_bytes;

180} \_\_packed;

181

182/\* Memory block header \*/

183struct coredump\_mem\_hdr\_t {

184 /\* COREDUMP\_MEM\_HDR\_ID \*/

185 char id;

186

187 /\* Header version \*/

188 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) hdr\_version;

189

190 /\* Address of start of memory region \*/

191 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) start;

192

193 /\* Address of end of memory region \*/

194 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) end;

195} \_\_packed;

196

197typedef void (\*coredump\_backend\_start\_t)(void);

198typedef void (\*coredump\_backend\_end\_t)(void);

199typedef void (\*coredump\_backend\_buffer\_output\_t)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen);

200typedef int (\*coredump\_backend\_query\_t)(enum [coredump\_query\_id](group__coredump__apis.md#ga26360cadb6b43f5c86b59332e66008f5) query\_id,

201 void \*arg);

202typedef int (\*coredump\_backend\_cmd\_t)(enum [coredump\_cmd\_id](group__coredump__apis.md#ga48765a88d430aaec373a2ce6e4796578) cmd\_id,

203 void \*arg);

204

205struct coredump\_backend\_api {

206 /\* Signal to backend of the start of coredump. \*/

207 coredump\_backend\_start\_t start;

208

209 /\* Signal to backend of the end of coredump. \*/

210 coredump\_backend\_end\_t end;

211

212 /\* Raw buffer output \*/

213 coredump\_backend\_buffer\_output\_t buffer\_output;

214

215 /\* Perform query on backend \*/

216 coredump\_backend\_query\_t query;

217

218 /\* Perform command on backend \*/

219 coredump\_backend\_cmd\_t [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615);

220};

221

222void [coredump](group__coredump__apis.md#gac8e7b27f4bbef5120b745677d5c64200)(unsigned int reason, const z\_arch\_esf\_t \*esf,

223 struct [k\_thread](structk__thread.md) \*thread);

224void [coredump\_memory\_dump](group__coredump__apis.md#ga835467b2517f871b0092f0dd7757f14b)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) start\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) end\_addr);

225void [coredump\_buffer\_output](group__coredump__apis.md#ga00bc832d1a9fb7d23d63c09abcf313eb)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen);

226

227int [coredump\_query](group__coredump__apis.md#gad521f35e7b487cbaed553f8f8e4a9e27)(enum [coredump\_query\_id](group__coredump__apis.md#ga26360cadb6b43f5c86b59332e66008f5) query\_id, void \*arg);

228int [coredump\_cmd](group__coredump__apis.md#ga9ebe60f88decfba5b798736984b4c496)(enum [coredump\_cmd\_id](group__coredump__apis.md#ga48765a88d430aaec373a2ce6e4796578) cmd\_id, void \*arg);

229

230#else

231

[ 232](group__coredump__apis.md#gac8e7b27f4bbef5120b745677d5c64200)void [coredump](group__coredump__apis.md#gac8e7b27f4bbef5120b745677d5c64200)(unsigned int reason, const z\_arch\_esf\_t \*esf,

233 struct [k\_thread](structk__thread.md) \*thread)

234{

235 ARG\_UNUSED(reason);

236 ARG\_UNUSED(esf);

237 ARG\_UNUSED(thread);

238}

239

[ 240](group__coredump__apis.md#ga835467b2517f871b0092f0dd7757f14b)void [coredump\_memory\_dump](group__coredump__apis.md#ga835467b2517f871b0092f0dd7757f14b)([uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) start\_addr, [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) end\_addr)

241{

242 ARG\_UNUSED(start\_addr);

243 ARG\_UNUSED(end\_addr);

244}

245

[ 246](group__coredump__apis.md#ga00bc832d1a9fb7d23d63c09abcf313eb)void [coredump\_buffer\_output](group__coredump__apis.md#ga00bc832d1a9fb7d23d63c09abcf313eb)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, size\_t buflen)

247{

248 ARG\_UNUSED(buf);

249 ARG\_UNUSED(buflen);

250}

251

[ 252](group__coredump__apis.md#gad521f35e7b487cbaed553f8f8e4a9e27)int [coredump\_query](group__coredump__apis.md#gad521f35e7b487cbaed553f8f8e4a9e27)(enum [coredump\_query\_id](group__coredump__apis.md#ga26360cadb6b43f5c86b59332e66008f5) query\_id, void \*arg)

253{

254 ARG\_UNUSED(query\_id);

255 ARG\_UNUSED(arg);

256 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

257}

258

[ 259](group__coredump__apis.md#ga9ebe60f88decfba5b798736984b4c496)int [coredump\_cmd](group__coredump__apis.md#ga9ebe60f88decfba5b798736984b4c496)(enum [coredump\_cmd\_id](group__coredump__apis.md#ga48765a88d430aaec373a2ce6e4796578) query\_id, void \*arg)

260{

261 ARG\_UNUSED(query\_id);

262 ARG\_UNUSED(arg);

263 return -[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33);

264}

265

266#endif /\* CONFIG\_DEBUG\_COREDUMP \*/

267

280

288

300

312

324

328

329#endif /\* ZEPHYR\_INCLUDE\_DEBUG\_COREDUMP\_H\_ \*/

[coredump\_buffer\_output](group__coredump__apis.md#ga00bc832d1a9fb7d23d63c09abcf313eb)

void coredump\_buffer\_output(uint8\_t \*buf, size\_t buflen)

Output the buffer via coredump.

**Definition** coredump.h:246

[coredump\_query\_id](group__coredump__apis.md#ga26360cadb6b43f5c86b59332e66008f5)

coredump\_query\_id

Query ID.

**Definition** coredump.h:26

[coredump\_cmd\_id](group__coredump__apis.md#ga48765a88d430aaec373a2ce6e4796578)

coredump\_cmd\_id

Command ID.

**Definition** coredump.h:57

[coredump\_memory\_dump](group__coredump__apis.md#ga835467b2517f871b0092f0dd7757f14b)

void coredump\_memory\_dump(uintptr\_t start\_addr, uintptr\_t end\_addr)

Dump memory region.

**Definition** coredump.h:240

[coredump\_cmd](group__coredump__apis.md#ga9ebe60f88decfba5b798736984b4c496)

int coredump\_cmd(enum coredump\_cmd\_id query\_id, void \*arg)

Perform command on coredump subsystem.

**Definition** coredump.h:259

[coredump](group__coredump__apis.md#gac8e7b27f4bbef5120b745677d5c64200)

void coredump(unsigned int reason, const z\_arch\_esf\_t \*esf, struct k\_thread \*thread)

Perform coredump.

**Definition** coredump.h:232

[coredump\_query](group__coredump__apis.md#gad521f35e7b487cbaed553f8f8e4a9e27)

int coredump\_query(enum coredump\_query\_id query\_id, void \*arg)

Perform query on coredump subsystem.

**Definition** coredump.h:252

[COREDUMP\_QUERY\_HAS\_STORED\_DUMP](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5a89f3cc157e790b8aa324d76a01b73e83)

@ COREDUMP\_QUERY\_HAS\_STORED\_DUMP

Check if there is a stored coredump from backend.

**Definition** coredump.h:40

[COREDUMP\_QUERY\_GET\_STORED\_DUMP\_SIZE](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5ac3e34206cd358efdc1ed7a2996b98483)

@ COREDUMP\_QUERY\_GET\_STORED\_DUMP\_SIZE

Returns:

**Definition** coredump.h:48

[COREDUMP\_QUERY\_MAX](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5ae4a1cdeb5c337eae17d59a1d1f1d1e2d)

@ COREDUMP\_QUERY\_MAX

Max value for query ID.

**Definition** coredump.h:53

[COREDUMP\_QUERY\_GET\_ERROR](group__coredump__apis.md#gga26360cadb6b43f5c86b59332e66008f5afa7363b57e57c55fffa8cc9e9050d6cb)

@ COREDUMP\_QUERY\_GET\_ERROR

Returns error code from backend.

**Definition** coredump.h:30

[COREDUMP\_CMD\_COPY\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578a0cc9387829efa1f3c6f802217adc3819)

@ COREDUMP\_CMD\_COPY\_STORED\_DUMP

Copy the raw stored coredump.

**Definition** coredump.h:95

[COREDUMP\_CMD\_MAX](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578a1b35195ff848aa9803bdcb4136e386c6)

@ COREDUMP\_CMD\_MAX

Max value for command ID.

**Definition** coredump.h:111

[COREDUMP\_CMD\_INVALIDATE\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578aa45b8520053c56075a29441c27e4e321)

@ COREDUMP\_CMD\_INVALIDATE\_STORED\_DUMP

Invalidate the stored coredump.

**Definition** coredump.h:106

[COREDUMP\_CMD\_ERASE\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578ab46f9f907e75e1187a6b7a2efd7e54f6)

@ COREDUMP\_CMD\_ERASE\_STORED\_DUMP

Erase the stored coredump.

**Definition** coredump.h:84

[COREDUMP\_CMD\_VERIFY\_STORED\_DUMP](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578ab8f6dd3e8062175c9790bfe5d2b2aeaa)

@ COREDUMP\_CMD\_VERIFY\_STORED\_DUMP

Verify that the stored coredump is valid.

**Definition** coredump.h:74

[COREDUMP\_CMD\_CLEAR\_ERROR](group__coredump__apis.md#gga48765a88d430aaec373a2ce6e4796578aef8cf1d85b2dfb2c911cb2abb7e3b38f)

@ COREDUMP\_CMD\_CLEAR\_ERROR

Clear error code from backend.

**Definition** coredump.h:63

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[ENOTSUP](group__system__errno.md#ga91457bbf35f0f1085619a99423bb1f33)

#define ENOTSUP

Unsupported value.

**Definition** errno.h:115

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

[coredump\_cmd\_copy\_arg](structcoredump__cmd__copy__arg.md)

Coredump copy command (COREDUMP\_CMD\_COPY\_STORED\_DUMP) argument definition.

**Definition** coredump.h:115

[coredump\_cmd\_copy\_arg::offset](structcoredump__cmd__copy__arg.md#a724583bd7203d16cc46f06698acfc6ef)

off\_t offset

Copy offset.

**Definition** coredump.h:117

[coredump\_cmd\_copy\_arg::buffer](structcoredump__cmd__copy__arg.md#a74495abb94670f983a3f136274485c40)

uint8\_t \* buffer

Copy destination buffer.

**Definition** coredump.h:120

[coredump\_cmd\_copy\_arg::length](structcoredump__cmd__copy__arg.md#ae9266221235083dcf6efd7aba2177a75)

size\_t length

Copy length.

**Definition** coredump.h:123

[k\_thread](structk__thread.md)

Thread Structure.

**Definition** thread.h:250

[byteorder.h](sys_2byteorder_8h.md)

Byte order helpers.

[toolchain.h](toolchain_8h.md)

Macros to abstract toolchain specific capabilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [coredump.h](debug_2coredump_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
