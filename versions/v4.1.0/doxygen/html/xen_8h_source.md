---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/xen_8h_source.html
original_path: doxygen/html/xen_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xen.h

[Go to the documentation of this file.](xen_8h.md)

1/\* SPDX-License-Identifier: MIT \*/

2

3/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

4 \* xen.h

5 \*

6 \* Guest OS interface to Xen.

7 \*

8 \* Permission is hereby granted, free of charge, to any person obtaining a copy

9 \* of this software and associated documentation files (the "Software"), to

10 \* deal in the Software without restriction, including without limitation the

11 \* rights to use, copy, modify, merge, publish, distribute, sublicense, and/or

12 \* sell copies of the Software, and to permit persons to whom the Software is

13 \* furnished to do so, subject to the following conditions:

14 \*

15 \* The above copyright notice and this permission notice shall be included in

16 \* all copies or substantial portions of the Software.

17 \*

18 \* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

19 \* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

20 \* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

21 \* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

22 \* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING

23 \* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER

24 \* DEALINGS IN THE SOFTWARE.

25 \*

26 \* Copyright (c) 2004, K A Fraser

27 \*/

28

29#ifndef \_\_XEN\_PUBLIC\_XEN\_H\_\_

30#define \_\_XEN\_PUBLIC\_XEN\_H\_\_

31

32#if defined(CONFIG\_ARM64)

33#include "[arch-arm.h](arch-arm_8h.md)"

34#else

35#error "Unsupported architecture"

36#endif

37

38#ifndef \_\_ASSEMBLY\_\_

39/\* Guest handles for primitive C types. \*/

[ 40](xen_8h.md#a3271eb49ce50552a93325e44d0baea20)[DEFINE\_XEN\_GUEST\_HANDLE](xen_8h.md#a46a69b3cd5864a78bfc73762d5a2b517)(char);

41\_\_DEFINE\_XEN\_GUEST\_HANDLE(uchar, unsigned char);

[ 42](xen_8h.md#a4649270bf23be045659cecbdb6c984c5)[DEFINE\_XEN\_GUEST\_HANDLE](xen_8h.md#a46a69b3cd5864a78bfc73762d5a2b517)(int);

43\_\_DEFINE\_XEN\_GUEST\_HANDLE(uint, unsigned int);

44#if CONFIG\_XEN\_INTERFACE\_VERSION < 0x00040300

[ 45](xen_8h.md#aaa8e284b50677157bf7e14a060be46a3)[DEFINE\_XEN\_GUEST\_HANDLE](xen_8h.md#a46a69b3cd5864a78bfc73762d5a2b517)(long);

46\_\_DEFINE\_XEN\_GUEST\_HANDLE(ulong, unsigned long);

47#endif

[ 48](xen_8h.md#a46a69b3cd5864a78bfc73762d5a2b517)[DEFINE\_XEN\_GUEST\_HANDLE](xen_8h.md#a46a69b3cd5864a78bfc73762d5a2b517)(void);

49

[ 50](xen_8h.md#a68bef499d4605a558eea3240a15e86ac)[DEFINE\_XEN\_GUEST\_HANDLE](xen_8h.md#a46a69b3cd5864a78bfc73762d5a2b517)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d));

[ 51](xen_8h.md#a69e56b135e0fd672f45a05b8de1b2db0)[DEFINE\_XEN\_GUEST\_HANDLE](xen_8h.md#a46a69b3cd5864a78bfc73762d5a2b517)([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1));

52[DEFINE\_XEN\_GUEST\_HANDLE](xen_8h.md#a46a69b3cd5864a78bfc73762d5a2b517)([xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226));

53[DEFINE\_XEN\_GUEST\_HANDLE](xen_8h.md#a46a69b3cd5864a78bfc73762d5a2b517)([xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc));

54

55/\* Define a variable length array (depends on compiler). \*/

56#if defined(\_\_STDC\_VERSION\_\_) && \_\_STDC\_VERSION\_\_ >= 199901L

57#define XEN\_FLEX\_ARRAY\_DIM

58#elif defined(\_\_GNUC\_\_)

59#define XEN\_FLEX\_ARRAY\_DIM 0

60#else

[ 61](xen_8h.md#ae905e08d72e4466ea6a2ec669c3820e4)#define XEN\_FLEX\_ARRAY\_DIM 1 /\* variable size \*/

62#endif

63

64/\* Turn a plain number into a C unsigned (long (long)) constant. \*/

65#define \_\_xen\_mk\_uint(x) x ## U

66#define \_\_xen\_mk\_ulong(x) x ## UL

67#ifndef \_\_xen\_mk\_ullong

68#define \_\_xen\_mk\_ullong(x) x ## ULL

69#endif

[ 70](xen_8h.md#aa7b557e58ad4a375ce9dcccac60d7b14)#define xen\_mk\_uint(x) \_\_xen\_mk\_uint(x)

[ 71](xen_8h.md#a81523e052b17db63279a60bef67924b4)#define xen\_mk\_ulong(x) \_\_xen\_mk\_ulong(x)

[ 72](xen_8h.md#ad58e92795b2f6c186afd2848e04e39ad)#define xen\_mk\_ullong(x) \_\_xen\_mk\_ullong(x)

73

74#else

75

76/\* In assembly code we cannot use C numeric constant suffixes. \*/

77#define xen\_mk\_uint(x) x

78#define xen\_mk\_ulong(x) x

79#define xen\_mk\_ullong(x) x

80

81#endif

82

83/\*

84 \* HYPERCALLS

85 \*/

86

87/\* `incontents 100 hcalls List of hypercalls

88 \* ` enum hypercall\_num { // \_\_HYPERVISOR\_\* => HYPERVISOR\_\*()

89 \*/

90

91#define \_\_HYPERVISOR\_set\_trap\_table 0

92#define \_\_HYPERVISOR\_mmu\_update 1

93#define \_\_HYPERVISOR\_set\_gdt 2

94#define \_\_HYPERVISOR\_stack\_switch 3

95#define \_\_HYPERVISOR\_set\_callbacks 4

96#define \_\_HYPERVISOR\_fpu\_taskswitch 5

97

98/\* compat since 0x00030101 \*/

99#define \_\_HYPERVISOR\_sched\_op\_compat 6

100#define \_\_HYPERVISOR\_platform\_op 7

101#define \_\_HYPERVISOR\_set\_debugreg 8

102#define \_\_HYPERVISOR\_get\_debugreg 9

103#define \_\_HYPERVISOR\_update\_descriptor 10

104#define \_\_HYPERVISOR\_memory\_op 12

105#define \_\_HYPERVISOR\_multicall 13

106#define \_\_HYPERVISOR\_update\_va\_mapping 14

107#define \_\_HYPERVISOR\_set\_timer\_op 15

108

109/\* compat since 0x00030202 \*/

110#define \_\_HYPERVISOR\_event\_channel\_op\_compat 16

111#define \_\_HYPERVISOR\_xen\_version 17

112#define \_\_HYPERVISOR\_console\_io 18

113

114/\* compat since 0x00030202 \*/

115#define \_\_HYPERVISOR\_physdev\_op\_compat 19

116#define \_\_HYPERVISOR\_grant\_table\_op 20

117#define \_\_HYPERVISOR\_vm\_assist 21

118#define \_\_HYPERVISOR\_update\_va\_mapping\_otherdomain 22

119

120/\* x86 only \*/

121#define \_\_HYPERVISOR\_iret 23

122#define \_\_HYPERVISOR\_vcpu\_op 24

123

124/\* x86/64 only \*/

125#define \_\_HYPERVISOR\_set\_segment\_base 25

126#define \_\_HYPERVISOR\_mmuext\_op 26

127#define \_\_HYPERVISOR\_xsm\_op 27

128#define \_\_HYPERVISOR\_nmi\_op 28

129#define \_\_HYPERVISOR\_sched\_op 29

130#define \_\_HYPERVISOR\_callback\_op 30

131#define \_\_HYPERVISOR\_xenoprof\_op 31

132#define \_\_HYPERVISOR\_event\_channel\_op 32

133#define \_\_HYPERVISOR\_physdev\_op 33

134#define \_\_HYPERVISOR\_hvm\_op 34

135#define \_\_HYPERVISOR\_sysctl 35

136#define \_\_HYPERVISOR\_domctl 36

137#define \_\_HYPERVISOR\_kexec\_op 37

138#define \_\_HYPERVISOR\_tmem\_op 38

139#define \_\_HYPERVISOR\_argo\_op 39

140#define \_\_HYPERVISOR\_xenpmu\_op 40

141#define \_\_HYPERVISOR\_dm\_op 41

142#define \_\_HYPERVISOR\_hypfs\_op 42

143

144/\*

145 \* ` int

146 \* ` HYPERVISOR\_console\_io(unsigned int cmd,

147 \* ` unsigned int count,

148 \* ` char buffer[]);

149 \*

150 \* @cmd: Command (see below)

151 \* @count: Size of the buffer to read/write

152 \* @buffer: Pointer in the guest memory

153 \*

154 \* List of commands:

155 \*

156 \* \* CONSOLEIO\_write: Write the buffer to Xen console.

157 \* For the hardware domain, all the characters in the buffer will

158 \* be written. Characters will be printed directly to the console.

159 \* For all the other domains, only the printable characters will be

160 \* written. Characters may be buffered until a newline (i.e '\n') is

161 \* found.

162 \* @return 0 on success, otherwise return an error code.

163 \* \* CONSOLEIO\_read: Attempts to read up to @count characters from Xen

164 \* console. The maximum buffer size (i.e. @count) supported is 2GB.

165 \* @return the number of characters read on success, otherwise return

166 \* an error code.

167 \*/

[ 168](xen_8h.md#a37817ff1ba0005b425725c5b3cbc05e9)#define CONSOLEIO\_write 0

[ 169](xen_8h.md#ad4bd5e7f69e7deae12467bf88cf67556)#define CONSOLEIO\_read 1

170

171/\* Domain ids >= DOMID\_FIRST\_RESERVED cannot be used for ordinary domains. \*/

[ 172](xen_8h.md#a9ac49a47125b5244077355a3cf2ec397)#define DOMID\_FIRST\_RESERVED xen\_mk\_uint(0x7FF0)

173

174/\* DOMID\_SELF is used in certain contexts to refer to oneself. \*/

[ 175](xen_8h.md#a632d71fe6315d8b3dfcc2cad373fb7ec)#define DOMID\_SELF xen\_mk\_uint(0x7FF0)

176

177/\*

178 \* DOMID\_IO is used to restrict page-table updates to mapping I/O memory.

179 \* Although no Foreign Domain need be specified to map I/O pages, DOMID\_IO

180 \* is useful to ensure that no mappings to the OS's own heap are accidentally

181 \* installed. (e.g., in Linux this could cause havoc as reference counts

182 \* aren't adjusted on the I/O-mapping code path).

183 \* This only makes sense as HYPERVISOR\_mmu\_update()'s and

184 \* HYPERVISOR\_update\_va\_mapping\_otherdomain()'s "foreigndom" argument. For

185 \* HYPERVISOR\_mmu\_update() context it can be specified by any calling domain,

186 \* otherwise it's only permitted if the caller is privileged.

187 \*/

[ 188](xen_8h.md#ab0d934a6f32a8feb76959586dd66418c)#define DOMID\_IO xen\_mk\_uint(0x7FF1)

189

190/\*

191 \* DOMID\_XEN is used to allow privileged domains to map restricted parts of

192 \* Xen's heap space (e.g., the machine\_to\_phys table).

193 \* This only makes sense as

194 \* - HYPERVISOR\_mmu\_update()'s, HYPERVISOR\_mmuext\_op()'s, or

195 \* HYPERVISOR\_update\_va\_mapping\_otherdomain()'s "foreigndom" argument,

196 \* - with XENMAPSPACE\_gmfn\_foreign,

197 \* and is only permitted if the caller is privileged.

198 \*/

[ 199](xen_8h.md#a4a604fcd4144dbd998b76cca7600d081)#define DOMID\_XEN xen\_mk\_uint(0x7FF2)

200

201/\*

202 \* DOMID\_COW is used as the owner of sharable pages.

203 \*/

[ 204](xen_8h.md#a51650c6e893bd06faf62c96c33d939d2)#define DOMID\_COW xen\_mk\_uint(0x7FF3)

205

206/\* DOMID\_INVALID is used to identify pages with unknown owner. \*/

[ 207](xen_8h.md#a14f066e67f10f6b886886a3befdfe6be)#define DOMID\_INVALID xen\_mk\_uint(0x7FF4)

208

209/\* Idle domain. \*/

[ 210](xen_8h.md#a346001069dbc3dacc7e34443b8b712b1)#define DOMID\_IDLE xen\_mk\_uint(0x7FFF)

211

212/\* Mask for valid domain id values \*/

[ 213](xen_8h.md#a0010d63d23be20833baa50e50127bcb3)#define DOMID\_MASK xen\_mk\_uint(0x7FFF)

214

215#ifndef \_\_ASSEMBLY\_\_

216

[ 217](xen_8h.md#a52133e9b6faf803a509868928d1c0eee)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee);

218

219#if CONFIG\_XEN\_INTERFACE\_VERSION < 0x00040400

220/\*

221 \* Event channel endpoints per domain (when using the 2-level ABI):

222 \* 1024 if a long is 32 bits; 4096 if a long is 64 bits.

223 \*/

[ 224](xen_8h.md#a0eaef6f49b471e8f6c9b3090ed65683a)#define NR\_EVENT\_CHANNELS EVTCHN\_2L\_NR\_CHANNELS

225#endif

226

[ 227](structvcpu__time__info.md)struct [vcpu\_time\_info](structvcpu__time__info.md) {

228 /\*

229 \* Updates to the following values are preceded and followed by an

230 \* increment of 'version'. The guest can therefore detect updates by

231 \* looking for changes to 'version'. If the least-significant bit of

232 \* the version number is set then an update is in progress and the

233 \* guest must wait to read a consistent set of values.

234 \* The correct way to interact with the version number is similar to

235 \* Linux's seqlock: see the implementations of

236 \* read\_seqbegin/read\_seqretry.

237 \*/

[ 238](structvcpu__time__info.md#a82f016f109904dd5effa7c87c8cc35fb) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [version](structvcpu__time__info.md#a82f016f109904dd5effa7c87c8cc35fb);

[ 239](structvcpu__time__info.md#a20339e02cb0bd2993e6d4a293c6f8d3b) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [pad0](structvcpu__time__info.md#a20339e02cb0bd2993e6d4a293c6f8d3b);

[ 240](structvcpu__time__info.md#a3bcf2b4d3f246bef1f1c90ceeef6c774) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [tsc\_timestamp](structvcpu__time__info.md#a3bcf2b4d3f246bef1f1c90ceeef6c774); /\* TSC at last update of time vals. \*/

[ 241](structvcpu__time__info.md#a8963a462f7e7ab7f3833d43adc60e06f) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [system\_time](structvcpu__time__info.md#a8963a462f7e7ab7f3833d43adc60e06f); /\* Time, in nanosecs, since boot.\*/

242 /\*

243 \* Current system time:

244 \* system\_time +

245 \* ((((tsc - tsc\_timestamp) << tsc\_shift) \* tsc\_to\_system\_mul) >> 32)

246 \* CPU frequency (Hz):

247 \* ((10^9 << 32) / tsc\_to\_system\_mul) >> tsc\_shift

248 \*/

[ 249](structvcpu__time__info.md#a11b2973a6d58b5cfa31a3306d1a9ff84) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [tsc\_to\_system\_mul](structvcpu__time__info.md#a11b2973a6d58b5cfa31a3306d1a9ff84);

[ 250](structvcpu__time__info.md#af7d9bee0e8e4eab21b4388f60b4febb7) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [tsc\_shift](structvcpu__time__info.md#af7d9bee0e8e4eab21b4388f60b4febb7);

251#if CONFIG\_XEN\_INTERFACE\_VERSION > 0x040600

252 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9);

253 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pad1](structvcpu__time__info.md#a871e2e15e0a3707c4662456b62d14677)[2];

254#else

[ 255](structvcpu__time__info.md#a871e2e15e0a3707c4662456b62d14677) [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) [pad1](structvcpu__time__info.md#a871e2e15e0a3707c4662456b62d14677)[3];

256#endif

257}; /\* 32 bytes \*/

[ 258](xen_8h.md#a46b8329725a49204352d786ce96d8b85)typedef struct [vcpu\_time\_info](structvcpu__time__info.md) [vcpu\_time\_info\_t](xen_8h.md#a46b8329725a49204352d786ce96d8b85);

259

[ 260](xen_8h.md#a3b6486848b8f26f7ebbdb4b2ac0b6f0c)#define XEN\_PVCLOCK\_TSC\_STABLE\_BIT (1 << 0)

[ 261](xen_8h.md#aa63ac2404dfad1ac4828f973623896e4)#define XEN\_PVCLOCK\_GUEST\_STOPPED (1 << 1)

262

[ 263](structvcpu__info.md)struct [vcpu\_info](structvcpu__info.md) {

264 /\*

265 \* 'evtchn\_upcall\_pending' is written non-zero by Xen to indicate

266 \* a pending notification for a particular VCPU. It is then cleared

267 \* by the guest OS /before/ checking for pending work, thus avoiding

268 \* a set-and-check race. Note that the mask is only accessed by Xen

269 \* on the CPU that is currently hosting the VCPU. This means that the

270 \* pending and mask flags can be updated by the guest without special

271 \* synchronisation (i.e., no need for the x86 LOCK prefix).

272 \* This may seem suboptimal because if the pending flag is set by

273 \* a different CPU then an IPI may be scheduled even when the mask

274 \* is set. However, note:

275 \* 1. The task of 'interrupt holdoff' is covered by the per-event-

276 \* channel mask bits. A 'noisy' event that is continually being

277 \* triggered can be masked at source at this very precise

278 \* granularity.

279 \* 2. The main purpose of the per-VCPU mask is therefore to restrict

280 \* reentrant execution: whether for concurrency control, or to

281 \* prevent unbounded stack usage. Whatever the purpose, we expect

282 \* that the mask will be asserted only for short periods at a time,

283 \* and so the likelihood of a 'spurious' IPI is suitably small.

284 \* The mask is read before making an event upcall to the guest: a

285 \* non-zero mask therefore guarantees that the VCPU will not receive

286 \* an upcall activation. The mask is cleared when the VCPU requests

287 \* to block: this avoids wakeup-waiting races.

288 \*/

[ 289](structvcpu__info.md#a36147b6f38a5398d4226ddcd1fd8b0e3) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [evtchn\_upcall\_pending](structvcpu__info.md#a36147b6f38a5398d4226ddcd1fd8b0e3);

290#ifdef XEN\_HAVE\_PV\_UPCALL\_MASK

291 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) evtchn\_upcall\_mask;

292#else /\* XEN\_HAVE\_PV\_UPCALL\_MASK \*/

[ 293](structvcpu__info.md#a2f48138d80da05071cbf64a7d334eefe) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [pad0](structvcpu__info.md#a2f48138d80da05071cbf64a7d334eefe);

294#endif /\* XEN\_HAVE\_PV\_UPCALL\_MASK \*/

[ 295](structvcpu__info.md#a34f154443856775657a7ce8ef77a7156) [xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc) [evtchn\_pending\_sel](structvcpu__info.md#a34f154443856775657a7ce8ef77a7156);

[ 296](structvcpu__info.md#a433f67b9e1c989e316d04d5976804c0a) struct [arch\_vcpu\_info](structarch__vcpu__info.md) [arch](structvcpu__info.md#a433f67b9e1c989e316d04d5976804c0a);

[ 297](structvcpu__info.md#af4a9ddd9cf24c74364df924c0a815231) [vcpu\_time\_info\_t](xen_8h.md#a46b8329725a49204352d786ce96d8b85) [time](structvcpu__info.md#af4a9ddd9cf24c74364df924c0a815231);

298}; /\* 64 bytes (x86) \*/

299#ifndef \_\_XEN\_\_

[ 300](xen_8h.md#a5d85cc76b763cb919c5c7d0e91d66d9f)typedef struct [vcpu\_info](structvcpu__info.md) [vcpu\_info\_t](xen_8h.md#a5d85cc76b763cb919c5c7d0e91d66d9f);

301#endif

302

303/\*

304 \* `incontents 200 startofday\_shared Start-of-day shared data structure

305 \* Xen/kernel shared data -- pointer provided in start\_info.

306 \*

307 \* This structure is defined to be both smaller than a page, and the

308 \* only data on the shared page, but may vary in actual size even within

309 \* compatible Xen versions; guests should not rely on the size

310 \* of this structure remaining constant.

311 \*/

[ 312](structshared__info.md)struct [shared\_info](structshared__info.md) {

[ 313](structshared__info.md#ac2546d512495d021e8e22d3eae260153) struct [vcpu\_info](structshared__info.md#ac2546d512495d021e8e22d3eae260153) [vcpu\_info](structshared__info.md#ac2546d512495d021e8e22d3eae260153)[[XEN\_LEGACY\_MAX\_VCPUS](arch-arm_8h.md#a57246b966cc182f34ca4f9bfa101e449)];

314

315 /\*

316 \* A domain can create "event channels" on which it can send and receive

317 \* asynchronous event notifications. There are three classes of event that

318 \* are delivered by this mechanism:

319 \* 1. Bi-directional inter- and intra-domain connections. Domains must

320 \* arrange out-of-band to set up a connection (usually by allocating

321 \* an unbound 'listener' port and advertising that via a storage service

322 \* such as xenstore).

323 \* 2. Physical interrupts. A domain with suitable hardware-access

324 \* privileges can bind an event-channel port to a physical interrupt

325 \* source.

326 \* 3. Virtual interrupts ('events'). A domain can bind an event-channel

327 \* port to a virtual interrupt source, such as the virtual-timer

328 \* device or the emergency console.

329 \*

330 \* Event channels are addressed by a "port index". Each channel is

331 \* associated with two bits of information:

332 \* 1. PENDING -- notifies the domain that there is a pending notification

333 \* to be processed. This bit is cleared by the guest.

334 \* 2. MASK -- if this bit is clear then a 0->1 transition of PENDING

335 \* will cause an asynchronous upcall to be scheduled. This bit is only

336 \* updated by the guest. It is read-only within Xen. If a channel

337 \* becomes pending while the channel is masked then the 'edge' is lost

338 \* (i.e., when the channel is unmasked, the guest must manually handle

339 \* pending notifications as no upcall will be scheduled by Xen).

340 \*

341 \* To expedite scanning of pending notifications, any 0->1 pending

342 \* transition on an unmasked channel causes a corresponding bit in a

343 \* per-vcpu selector word to be set. Each bit in the selector covers a

344 \* 'C long' in the PENDING bitfield array.

345 \*/

[ 346](structshared__info.md#a7911652d7ce578705e852d4518d1abb9) [xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc) [evtchn\_pending](structshared__info.md#a7911652d7ce578705e852d4518d1abb9)[sizeof([xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc)) \* 8];

[ 347](structshared__info.md#a45398e8bb0df581eedb48cd9902f811d) [xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc) [evtchn\_mask](structshared__info.md#a45398e8bb0df581eedb48cd9902f811d)[sizeof([xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc)) \* 8];

348

349 /\*

350 \* Wallclock time: updated by control software or RTC emulation.

351 \* Guests should base their gettimeofday() syscall on this

352 \* wallclock-base value.

353 \* The values of wc\_sec and wc\_nsec are offsets from the Unix epoch

354 \* adjusted by the domain's 'time offset' (in seconds) as set either

355 \* by XEN\_DOMCTL\_settimeoffset, or adjusted via a guest write to the

356 \* emulated RTC.

357 \*/

[ 358](structshared__info.md#aca3778d0bbd570d4ced2634b4da8a046) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [wc\_version](structshared__info.md#aca3778d0bbd570d4ced2634b4da8a046); /\* Version counter: see vcpu\_time\_info\_t. \*/

[ 359](structshared__info.md#a29cb80aa1a44985e5a84b4dcaf035708) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [wc\_sec](structshared__info.md#a29cb80aa1a44985e5a84b4dcaf035708);

[ 360](structshared__info.md#a29699e4b3d1953edfc3d836d5f582cf0) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [wc\_nsec](structshared__info.md#a29699e4b3d1953edfc3d836d5f582cf0);

361#if !defined(\_\_i386\_\_)

[ 362](structshared__info.md#a22add85abac7eae2240a9ef088772b15) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [wc\_sec\_hi](structshared__info.md#a22add85abac7eae2240a9ef088772b15);

[ 363](xen_8h.md#a9b01f685c203d17ebf84b1452d6c13fe)# define xen\_wc\_sec\_hi wc\_sec\_hi

364#elif !defined(\_\_XEN\_\_) && !defined(\_\_XEN\_TOOLS\_\_)

365# define xen\_wc\_sec\_hi arch.wc\_sec\_hi

366#endif

367

[ 368](structshared__info.md#a4eab2a6ca5ab006c3d3d0cd938dfa7f7) struct [arch\_shared\_info](structarch__shared__info.md) [arch](structshared__info.md#a4eab2a6ca5ab006c3d3d0cd938dfa7f7);

369

370};

371#ifndef \_\_XEN\_\_

[ 372](xen_8h.md#ad3890f69945f46e6904d389386df2ee1)typedef struct [shared\_info](structshared__info.md) [shared\_info\_t](xen_8h.md#ad3890f69945f46e6904d389386df2ee1);

373#endif

374

[ 375](xen_8h.md#a7be3933d71db9ec81444793055b5d9be)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [xen\_domain\_handle\_t](xen_8h.md#a7be3933d71db9ec81444793055b5d9be)[16];

376

377#ifndef int64\_aligned\_t

[ 378](xen_8h.md#a8e346fda4301d9806f5b97d796af4d0c)#define int64\_aligned\_t int64\_t

379#endif

380#ifndef uint64\_aligned\_t

[ 381](xen_8h.md#ac94f3cee60964f8609932e5042590128)#define uint64\_aligned\_t uint64\_t

382#endif

383#ifndef XEN\_GUEST\_HANDLE\_64

384#define XEN\_GUEST\_HANDLE\_64(name) XEN\_GUEST\_HANDLE(name)

385#endif

386

387#ifndef \_\_ASSEMBLY\_\_

[ 388](structxenctl__bitmap.md)struct [xenctl\_bitmap](structxenctl__bitmap.md) {

[ 389](structxenctl__bitmap.md#ac5b0fda202e274a8daff643ca0fc73ca) XEN\_GUEST\_HANDLE\_64([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)) [bitmap](structxenctl__bitmap.md#ac5b0fda202e274a8daff643ca0fc73ca);

[ 390](structxenctl__bitmap.md#a61606755569f953f067863bb07b522ab) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nr\_bits](structxenctl__bitmap.md#a61606755569f953f067863bb07b522ab);

391};

[ 392](xen_8h.md#a0b13d295ad2c74398b3430177ca6267a)typedef struct [xenctl\_bitmap](structxenctl__bitmap.md) [xenctl\_bitmap\_t](xen_8h.md#a0b13d295ad2c74398b3430177ca6267a);

393#endif

394

395#endif /\* !\_\_ASSEMBLY\_\_ \*/

396

397#endif /\* \_\_XEN\_PUBLIC\_XEN\_H\_\_ \*/

[arch-arm.h](arch-arm_8h.md)

[xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226)

uint64\_t xen\_pfn\_t

**Definition** arch-arm.h:204

[XEN\_LEGACY\_MAX\_VCPUS](arch-arm_8h.md#a57246b966cc182f34ca4f9bfa101e449)

#define XEN\_LEGACY\_MAX\_VCPUS

**Definition** arch-arm.h:212

[xen\_ulong\_t](arch-arm_8h.md#a9dd3dbb4741d391e0fff3f0e7d55cccc)

uint64\_t xen\_ulong\_t

**Definition** arch-arm.h:214

[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

flags

**Definition** parser.h:97

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6)

\_\_INT8\_TYPE\_\_ int8\_t

**Definition** stdint.h:72

[arch\_shared\_info](structarch__shared__info.md)

**Definition** arch-arm.h:344

[arch\_vcpu\_info](structarch__vcpu__info.md)

**Definition** arch-arm.h:340

[shared\_info](structshared__info.md)

**Definition** xen.h:312

[shared\_info::wc\_sec\_hi](structshared__info.md#a22add85abac7eae2240a9ef088772b15)

uint32\_t wc\_sec\_hi

**Definition** xen.h:362

[shared\_info::wc\_nsec](structshared__info.md#a29699e4b3d1953edfc3d836d5f582cf0)

uint32\_t wc\_nsec

**Definition** xen.h:360

[shared\_info::wc\_sec](structshared__info.md#a29cb80aa1a44985e5a84b4dcaf035708)

uint32\_t wc\_sec

**Definition** xen.h:359

[shared\_info::evtchn\_mask](structshared__info.md#a45398e8bb0df581eedb48cd9902f811d)

xen\_ulong\_t evtchn\_mask[sizeof(xen\_ulong\_t) \*8]

**Definition** xen.h:347

[shared\_info::arch](structshared__info.md#a4eab2a6ca5ab006c3d3d0cd938dfa7f7)

struct arch\_shared\_info arch

**Definition** xen.h:368

[shared\_info::evtchn\_pending](structshared__info.md#a7911652d7ce578705e852d4518d1abb9)

xen\_ulong\_t evtchn\_pending[sizeof(xen\_ulong\_t) \*8]

**Definition** xen.h:346

[shared\_info::vcpu\_info](structshared__info.md#ac2546d512495d021e8e22d3eae260153)

struct vcpu\_info vcpu\_info[XEN\_LEGACY\_MAX\_VCPUS]

**Definition** xen.h:313

[shared\_info::wc\_version](structshared__info.md#aca3778d0bbd570d4ced2634b4da8a046)

uint32\_t wc\_version

**Definition** xen.h:358

[vcpu\_info](structvcpu__info.md)

**Definition** xen.h:263

[vcpu\_info::pad0](structvcpu__info.md#a2f48138d80da05071cbf64a7d334eefe)

uint8\_t pad0

**Definition** xen.h:293

[vcpu\_info::evtchn\_pending\_sel](structvcpu__info.md#a34f154443856775657a7ce8ef77a7156)

xen\_ulong\_t evtchn\_pending\_sel

**Definition** xen.h:295

[vcpu\_info::evtchn\_upcall\_pending](structvcpu__info.md#a36147b6f38a5398d4226ddcd1fd8b0e3)

uint8\_t evtchn\_upcall\_pending

**Definition** xen.h:289

[vcpu\_info::arch](structvcpu__info.md#a433f67b9e1c989e316d04d5976804c0a)

struct arch\_vcpu\_info arch

**Definition** xen.h:296

[vcpu\_info::time](structvcpu__info.md#af4a9ddd9cf24c74364df924c0a815231)

vcpu\_time\_info\_t time

**Definition** xen.h:297

[vcpu\_time\_info](structvcpu__time__info.md)

**Definition** xen.h:227

[vcpu\_time\_info::tsc\_to\_system\_mul](structvcpu__time__info.md#a11b2973a6d58b5cfa31a3306d1a9ff84)

uint32\_t tsc\_to\_system\_mul

**Definition** xen.h:249

[vcpu\_time\_info::pad0](structvcpu__time__info.md#a20339e02cb0bd2993e6d4a293c6f8d3b)

uint32\_t pad0

**Definition** xen.h:239

[vcpu\_time\_info::tsc\_timestamp](structvcpu__time__info.md#a3bcf2b4d3f246bef1f1c90ceeef6c774)

uint64\_t tsc\_timestamp

**Definition** xen.h:240

[vcpu\_time\_info::version](structvcpu__time__info.md#a82f016f109904dd5effa7c87c8cc35fb)

uint32\_t version

**Definition** xen.h:238

[vcpu\_time\_info::pad1](structvcpu__time__info.md#a871e2e15e0a3707c4662456b62d14677)

int8\_t pad1[3]

**Definition** xen.h:255

[vcpu\_time\_info::system\_time](structvcpu__time__info.md#a8963a462f7e7ab7f3833d43adc60e06f)

uint64\_t system\_time

**Definition** xen.h:241

[vcpu\_time\_info::tsc\_shift](structvcpu__time__info.md#af7d9bee0e8e4eab21b4388f60b4febb7)

int8\_t tsc\_shift

**Definition** xen.h:250

[xenctl\_bitmap](structxenctl__bitmap.md)

**Definition** xen.h:388

[xenctl\_bitmap::nr\_bits](structxenctl__bitmap.md#a61606755569f953f067863bb07b522ab)

uint32\_t nr\_bits

**Definition** xen.h:390

[xenctl\_bitmap::bitmap](structxenctl__bitmap.md#ac5b0fda202e274a8daff643ca0fc73ca)

bitmap

**Definition** xen.h:389

[xenctl\_bitmap\_t](xen_8h.md#a0b13d295ad2c74398b3430177ca6267a)

struct xenctl\_bitmap xenctl\_bitmap\_t

**Definition** xen.h:392

[DEFINE\_XEN\_GUEST\_HANDLE](xen_8h.md#a46a69b3cd5864a78bfc73762d5a2b517)

DEFINE\_XEN\_GUEST\_HANDLE(void)

[vcpu\_time\_info\_t](xen_8h.md#a46b8329725a49204352d786ce96d8b85)

struct vcpu\_time\_info vcpu\_time\_info\_t

**Definition** xen.h:258

[domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee)

uint16\_t domid\_t

**Definition** xen.h:217

[vcpu\_info\_t](xen_8h.md#a5d85cc76b763cb919c5c7d0e91d66d9f)

struct vcpu\_info vcpu\_info\_t

**Definition** xen.h:300

[xen\_domain\_handle\_t](xen_8h.md#a7be3933d71db9ec81444793055b5d9be)

uint8\_t xen\_domain\_handle\_t[16]

**Definition** xen.h:375

[shared\_info\_t](xen_8h.md#ad3890f69945f46e6904d389386df2ee1)

struct shared\_info shared\_info\_t

**Definition** xen.h:372

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [public](dir_a9d090e3588b677c614b5c45cd68e13b.md)
- [xen.h](xen_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
