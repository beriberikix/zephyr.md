---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/grant__table_8h_source.html
original_path: doxygen/html/grant__table_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

grant\_table.h

[Go to the documentation of this file.](grant__table_8h.md)

1/\* SPDX-License-Identifier: MIT \*/

2

3/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

4 \* grant\_table.h

5 \*

6 \* Interface for granting foreign access to page frames, and receiving

7 \* page-ownership transfers.

8 \*

9 \* Permission is hereby granted, free of charge, to any person obtaining a copy

10 \* of this software and associated documentation files (the "Software"), to

11 \* deal in the Software without restriction, including without limitation the

12 \* rights to use, copy, modify, merge, publish, distribute, sublicense, and/or

13 \* sell copies of the Software, and to permit persons to whom the Software is

14 \* furnished to do so, subject to the following conditions:

15 \*

16 \* The above copyright notice and this permission notice shall be included in

17 \* all copies or substantial portions of the Software.

18 \*

19 \* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR

20 \* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,

21 \* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE

22 \* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER

23 \* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING

24 \* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER

25 \* DEALINGS IN THE SOFTWARE.

26 \*

27 \* Copyright (c) 2004, K A Fraser

28 \*/

29

30#ifndef \_\_XEN\_PUBLIC\_GRANT\_TABLE\_H\_\_

31#define \_\_XEN\_PUBLIC\_GRANT\_TABLE\_H\_\_

32

33#include "[xen.h](xen_8h.md)"

34

35/\*

36 \* `incontents 150 gnttab Grant Tables

37 \*

38 \* Xen's grant tables provide a generic mechanism to memory sharing

39 \* between domains. This shared memory interface underpins the split

40 \* device drivers for block and network IO.

41 \*

42 \* Each domain has its own grant table. This is a data structure that

43 \* is shared with Xen; it allows the domain to tell Xen what kind of

44 \* permissions other domains have on its pages. Entries in the grant

45 \* table are identified by grant references. A grant reference is an

46 \* integer, which indexes into the grant table. It acts as a

47 \* capability which the grantee can use to perform operations on the

48 \* granter's memory.

49 \*

50 \* This capability-based system allows shared-memory communications

51 \* between unprivileged domains. A grant reference also encapsulates

52 \* the details of a shared page, removing the need for a domain to

53 \* know the real machine address of a page it is sharing. This makes

54 \* it possible to share memory correctly with domains running in

55 \* fully virtualised memory.

56 \*/

57

58/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

59 \* GRANT TABLE REPRESENTATION

60 \*/

61

62/\* Some rough guidelines on accessing and updating grant-table entries

63 \* in a concurrency-safe manner. For more information, Linux contains a

64 \* reference implementation for guest OSes (drivers/xen/grant\_table.c, see

65 \* http://git.kernel.org/?p=linux/kernel/git/torvalds/linux.git;a=blob;f=drivers/xen/grant-table.c;hb=HEAD

66 \*

67 \* NB. WMB is a no-op on current-generation x86 processors. However, a

68 \* compiler barrier will still be required.

69 \*

70 \* Introducing a valid entry into the grant table:

71 \* 1. Write ent->domid.

72 \* 2. Write ent->frame:

73 \* GTF\_permit\_access: Frame to which access is permitted.

74 \* GTF\_accept\_transfer: Pseudo-phys frame slot being filled by new

75 \* frame, or zero if none.

76 \* 3. Write memory barrier (WMB).

77 \* 4. Write ent->flags, inc. valid type.

78 \*

79 \* Invalidating an unused GTF\_permit\_access entry:

80 \* 1. flags = ent->flags.

81 \* 2. Observe that !(flags & (GTF\_reading|GTF\_writing)).

82 \* 3. Check result of SMP-safe CMPXCHG(&ent->flags, flags, 0).

83 \* NB. No need for WMB as reuse of entry is control-dependent on success of

84 \* step 3, and all architectures guarantee ordering of ctrl-dep writes.

85 \*

86 \* Invalidating an in-use GTF\_permit\_access entry:

87 \* This cannot be done directly. Request assistance from the domain controller

88 \* which can set a timeout on the use of a grant entry and take necessary

89 \* action. (NB. This is not yet implemented!).

90 \*

91 \* Invalidating an unused GTF\_accept\_transfer entry:

92 \* 1. flags = ent->flags.

93 \* 2. Observe that !(flags & GTF\_transfer\_committed). [\*]

94 \* 3. Check result of SMP-safe CMPXCHG(&ent->flags, flags, 0).

95 \* NB. No need for WMB as reuse of entry is control-dependent on success of

96 \* step 3, and all architectures guarantee ordering of ctrl-dep writes.

97 \* [\*] If GTF\_transfer\_committed is set then the grant entry is 'committed'.

98 \* The guest must /not/ modify the grant entry until the address of the

99 \* transferred frame is written. It is safe for the guest to spin waiting

100 \* for this to occur (detect by observing GTF\_transfer\_completed in

101 \* ent->flags).

102 \*

103 \* Invalidating a committed GTF\_accept\_transfer entry:

104 \* 1. Wait for (ent->flags & GTF\_transfer\_completed).

105 \*

106 \* Changing a GTF\_permit\_access from writable to read-only:

107 \* Use SMP-safe CMPXCHG to set GTF\_readonly, while checking !GTF\_writing.

108 \*

109 \* Changing a GTF\_permit\_access from read-only to writable:

110 \* Use SMP-safe bit-setting instruction.

111 \*/

112

113/\*

114 \* Reference to a grant entry in a specified domain's grant table.

115 \*/

[ 116](grant__table_8h.md#aee25f6c8ecefd1d7c52e49e4886aca3e)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [grant\_ref\_t](grant__table_8h.md#aee25f6c8ecefd1d7c52e49e4886aca3e);

117

118/\*

119 \* A grant table comprises a packed array of grant entries in one or more

120 \* page frames shared between Xen and a guest.

121 \* [XEN]: This field is written by Xen and read by the sharing guest.

122 \* [GST]: This field is written by the guest and read by Xen.

123 \*/

124

125/\*

126 \* Version 1 of the grant table entry structure is maintained purely

127 \* for backwards compatibility. New guests should use version 2.

128 \*/

129#if \_\_XEN\_INTERFACE\_VERSION\_\_ < 0x0003020a

[ 130](grant__table_8h.md#ae42428f85f6f40af58ce52d7cbb9a7bc)#define grant\_entry\_v1 grant\_entry

[ 131](grant__table_8h.md#ad463d080d89bce70aa065aec9d62a69a)#define grant\_entry\_v1\_t grant\_entry\_t

132#endif

[ 133](structgrant__entry.md)struct [grant\_entry\_v1](grant__table_8h.md#ae42428f85f6f40af58ce52d7cbb9a7bc) {

134 /\* GTF\_xxx: various type and flag information. [XEN,GST] \*/

[ 135](structgrant__entry.md#ae45f6989c80eff0ad6faf7bcc89edcc4) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structgrant__entry.md#ae45f6989c80eff0ad6faf7bcc89edcc4);

136 /\* The domain being granted foreign privileges. [GST] \*/

[ 137](structgrant__entry.md#a16a644be72a9cce14e4682745714f78b) [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) [domid](structgrant__entry.md#a16a644be72a9cce14e4682745714f78b);

138 /\*

139 \* GTF\_permit\_access: GFN that @domid is allowed to map and access. [GST]

140 \* GTF\_accept\_transfer: GFN that @domid is allowed to transfer into. [GST]

141 \* GTF\_transfer\_completed: MFN whose ownership transferred by @domid

142 \* (non-translated guests only). [XEN]

143 \*/

[ 144](structgrant__entry.md#a6fe4635ae57bc41ed9aa1c65848f6c9a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [frame](structgrant__entry.md#a6fe4635ae57bc41ed9aa1c65848f6c9a);

145};

[ 146](grant__table_8h.md#aebf4abc7c6cd5ce259ff90a874648ea0)typedef struct [grant\_entry\_v1](grant__table_8h.md#ae42428f85f6f40af58ce52d7cbb9a7bc) [grant\_entry\_v1\_t](grant__table_8h.md#ad463d080d89bce70aa065aec9d62a69a);

147

148/\* The first few grant table entries will be preserved across grant table

149 \* version changes and may be pre-populated at domain creation by tools.

150 \*/

[ 151](grant__table_8h.md#a3f007d8667fc2c664aaf30c70cfb4d40)#define GNTTAB\_NR\_RESERVED\_ENTRIES 8

[ 152](grant__table_8h.md#af66d8799c0f4320ced4788fe30527e6f)#define GNTTAB\_RESERVED\_CONSOLE 0

[ 153](grant__table_8h.md#a22163820f5f3fa6b8b80f54dc8f44ea7)#define GNTTAB\_RESERVED\_XENSTORE 1

154

155/\*

156 \* Type of grant entry.

157 \* GTF\_invalid: This grant entry grants no privileges.

158 \* GTF\_permit\_access: Allow @domid to map/access @frame.

159 \* GTF\_accept\_transfer: Allow @domid to transfer ownership of one page frame

160 \* to this guest. Xen writes the page number to @frame.

161 \* GTF\_transitive: Allow @domid to transitively access a subrange of

162 \* @trans\_grant in @trans\_domid. No mappings are allowed.

163 \*/

[ 164](grant__table_8h.md#a593da3ddbb1a89c6d5bac76cc0200aa3)#define GTF\_invalid (0U << 0)

[ 165](grant__table_8h.md#abae7c6625c8a57268e21b4ebccc24e42)#define GTF\_permit\_access (1U << 0)

[ 166](grant__table_8h.md#a3eaec7cfe8c1d8f10713872452d4ad2a)#define GTF\_accept\_transfer (2U << 0)

[ 167](grant__table_8h.md#aa3ed0b5c63d22ef4a430fb1598e7b26b)#define GTF\_transitive (3U << 0)

[ 168](grant__table_8h.md#ad8879d52107cc4b8f8a5624e1e0596b2)#define GTF\_type\_mask (3U << 0)

169

170/\*

171 \* Subflags for GTF\_permit\_access and GTF\_transitive.

172 \* GTF\_readonly: Restrict @domid to read-only mappings and accesses. [GST]

173 \* GTF\_reading: Grant entry is currently mapped for reading by @domid. [XEN]

174 \* GTF\_writing: Grant entry is currently mapped for writing by @domid. [XEN]

175 \* Further subflags for GTF\_permit\_access only.

176 \* GTF\_PAT, GTF\_PWT, GTF\_PCD: (x86) cache attribute flags to be used for

177 \* mappings of the grant [GST]

178 \* GTF\_sub\_page: Grant access to only a subrange of the page. @domid

179 \* will only be allowed to copy from the grant, and not

180 \* map it. [GST]

181 \*/

182#define \_GTF\_readonly (2)

[ 183](grant__table_8h.md#ad63f8c1a78d72993230a38bf0629cbee)#define GTF\_readonly (1U << \_GTF\_readonly)

184#define \_GTF\_reading (3)

[ 185](grant__table_8h.md#ae259cc06448990822e273039612f2577)#define GTF\_reading (1U << \_GTF\_reading)

186#define \_GTF\_writing (4)

[ 187](grant__table_8h.md#a9c49e42a4da40bca62a629e3fb84cfbf)#define GTF\_writing (1U << \_GTF\_writing)

188#define \_GTF\_PWT (5)

[ 189](grant__table_8h.md#a57cc188dc528a922f99a51ace84e381c)#define GTF\_PWT (1U << \_GTF\_PWT)

190#define \_GTF\_PCD (6)

[ 191](grant__table_8h.md#a847aaa27483a22bc2f483175a0c84360)#define GTF\_PCD (1U << \_GTF\_PCD)

192#define \_GTF\_PAT (7)

[ 193](grant__table_8h.md#ab9215b09013fc607a5b9b7ea14409f15)#define GTF\_PAT (1U << \_GTF\_PAT)

194#define \_GTF\_sub\_page (8)

[ 195](grant__table_8h.md#aee57df4b4bf9c9711efbb0652a47d16b)#define GTF\_sub\_page (1U << \_GTF\_sub\_page)

196

197/\*

198 \* Subflags for GTF\_accept\_transfer:

199 \* GTF\_transfer\_committed: Xen sets this flag to indicate that it is committed

200 \* to transferring ownership of a page frame. When a guest sees this flag

201 \* it must /not/ modify the grant entry until GTF\_transfer\_completed is

202 \* set by Xen.

203 \* GTF\_transfer\_completed: It is safe for the guest to spin-wait on this flag

204 \* after reading GTF\_transfer\_committed. Xen will always write the frame

205 \* address, followed by ORing this flag, in a timely manner.

206 \*/

207#define \_GTF\_transfer\_committed (2)

[ 208](grant__table_8h.md#a3138f5333992b3ddd30297dcd3268350)#define GTF\_transfer\_committed (1U << \_GTF\_transfer\_committed)

209#define \_GTF\_transfer\_completed (3)

[ 210](grant__table_8h.md#a093e8bcc1ff97e22f80fa4db38826783)#define GTF\_transfer\_completed (1U << \_GTF\_transfer\_completed)

211

212/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

213 \* GRANT TABLE QUERIES AND USES

214 \*/

215

216/\* ` enum neg\_errnoval

217 \* ` HYPERVISOR\_grant\_table\_op(enum grant\_table\_op cmd,

218 \* ` void \*args,

219 \* ` unsigned int count)

220 \* `

221 \*

222 \* @args points to an array of a per-command data structure. The array

223 \* has @count members

224 \*/

225

226/\* ` enum grant\_table\_op { // GNTTABOP\_\* => struct gnttab\_\* \*/

[ 227](grant__table_8h.md#a0858861609126a45f682483cdb8c3c71)#define GNTTABOP\_map\_grant\_ref 0

[ 228](grant__table_8h.md#ae6b083e36a9b34bec9a00871ef2d8ba1)#define GNTTABOP\_unmap\_grant\_ref 1

[ 229](grant__table_8h.md#af3334c569ceddf0d578c11d5e3598e21)#define GNTTABOP\_setup\_table 2

[ 230](grant__table_8h.md#a36c577d4392ab9c2c0d0308ee511fe49)#define GNTTABOP\_dump\_table 3

[ 231](grant__table_8h.md#ac7ac76506dd75412a382b6255014a16d)#define GNTTABOP\_transfer 4

[ 232](grant__table_8h.md#aedb6d63bc0e6fe8f2d34363dffbdc6a8)#define GNTTABOP\_copy 5

[ 233](grant__table_8h.md#af6e54f747b849e7c7466b4352c3ea18e)#define GNTTABOP\_query\_size 6

[ 234](grant__table_8h.md#aa2da39ca5f693bdbb024676a7d0093e9)#define GNTTABOP\_unmap\_and\_replace 7

235#if \_\_XEN\_INTERFACE\_VERSION\_\_ >= 0x0003020a

236#define GNTTABOP\_set\_version 8

237#define GNTTABOP\_get\_status\_frames 9

238#define GNTTABOP\_get\_version 10

239#define GNTTABOP\_swap\_grant\_ref 11

240#define GNTTABOP\_cache\_flush 12

241#endif /\* \_\_XEN\_INTERFACE\_VERSION\_\_ \*/

242/\* ` } \*/

243

244/\*

245 \* Handle to track a mapping created via a grant reference.

246 \*/

[ 247](grant__table_8h.md#a1eade3c86c0fd0e71217eefaa3b38cd1)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [grant\_handle\_t](grant__table_8h.md#a1eade3c86c0fd0e71217eefaa3b38cd1);

248

249/\*

250 \* GNTTABOP\_map\_grant\_ref: Map the grant entry (<dom>,<ref>) for access

251 \* by devices and/or host CPUs. If successful, <handle> is a tracking number

252 \* that must be presented later to destroy the mapping(s). On error, <status>

253 \* is a negative status code.

254 \* NOTES:

255 \* 1. If GNTMAP\_device\_map is specified then <dev\_bus\_addr> is the address

256 \* via which I/O devices may access the granted frame.

257 \* 2. If GNTMAP\_host\_map is specified then a mapping will be added at

258 \* either a host virtual address in the current address space, or at

259 \* a PTE at the specified machine address. The type of mapping to

260 \* perform is selected through the GNTMAP\_contains\_pte flag, and the

261 \* address is specified in <host\_addr>.

262 \* 3. Mappings should only be destroyed via GNTTABOP\_unmap\_grant\_ref. If a

263 \* host mapping is destroyed by other means then it is \*NOT\* guaranteed

264 \* to be accounted to the correct grant reference!

265 \*/

[ 266](structgnttab__map__grant__ref.md)struct [gnttab\_map\_grant\_ref](structgnttab__map__grant__ref.md) {

267 /\* IN parameters. \*/

[ 268](structgnttab__map__grant__ref.md#a2c811c2986d6d7d5236a261c50c3492c) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [host\_addr](structgnttab__map__grant__ref.md#a2c811c2986d6d7d5236a261c50c3492c);

[ 269](structgnttab__map__grant__ref.md#a0db5af518a433b4441729019e65e1e3d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](structgnttab__map__grant__ref.md#a0db5af518a433b4441729019e65e1e3d); /\* GNTMAP\_\* \*/

[ 270](structgnttab__map__grant__ref.md#aff19dc5005ea1082cc9b5cd6bb89a2d7) [grant\_ref\_t](grant__table_8h.md#aee25f6c8ecefd1d7c52e49e4886aca3e) [ref](structgnttab__map__grant__ref.md#aff19dc5005ea1082cc9b5cd6bb89a2d7);

[ 271](structgnttab__map__grant__ref.md#a14efe928545333fb0f3544cdf98dc0ab) [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) [dom](structgnttab__map__grant__ref.md#a14efe928545333fb0f3544cdf98dc0ab);

272 /\* OUT parameters. \*/

[ 273](structgnttab__map__grant__ref.md#a738c22fab57008dcd5dac3651cfab66c) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [status](structgnttab__map__grant__ref.md#a738c22fab57008dcd5dac3651cfab66c); /\* => enum grant\_status \*/

[ 274](structgnttab__map__grant__ref.md#a6c0ce65e16e117c0678d635a2ee1d3f0) [grant\_handle\_t](grant__table_8h.md#a1eade3c86c0fd0e71217eefaa3b38cd1) [handle](structgnttab__map__grant__ref.md#a6c0ce65e16e117c0678d635a2ee1d3f0);

[ 275](structgnttab__map__grant__ref.md#ac90b06b676c85d65f8311fb72f0cfa5a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [dev\_bus\_addr](structgnttab__map__grant__ref.md#ac90b06b676c85d65f8311fb72f0cfa5a);

276};

[ 277](grant__table_8h.md#ac6ace01635e3b886a7f74d4e9ae3db78)typedef struct [gnttab\_map\_grant\_ref](structgnttab__map__grant__ref.md) [gnttab\_map\_grant\_ref\_t](grant__table_8h.md#ac6ace01635e3b886a7f74d4e9ae3db78);

[ 278](grant__table_8h.md#a01396c3aadef6f69b8c03735840c8bb9)[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)([gnttab\_map\_grant\_ref\_t](grant__table_8h.md#ac6ace01635e3b886a7f74d4e9ae3db78));

279

280/\*

281 \* GNTTABOP\_unmap\_grant\_ref: Destroy one or more grant-reference mappings

282 \* tracked by <handle>. If <host\_addr> or <dev\_bus\_addr> is zero, that

283 \* field is ignored. If non-zero, they must refer to a device/host mapping

284 \* that is tracked by <handle>

285 \* NOTES:

286 \* 1. The call may fail in an undefined manner if either mapping is not

287 \* tracked by <handle>.

288 \* 3. After executing a batch of unmaps, it is guaranteed that no stale

289 \* mappings will remain in the device or host TLBs.

290 \*/

[ 291](structgnttab__unmap__grant__ref.md)struct [gnttab\_unmap\_grant\_ref](structgnttab__unmap__grant__ref.md) {

292 /\* IN parameters. \*/

[ 293](structgnttab__unmap__grant__ref.md#a378f5d746e702ca1ceff2171f345f5e6) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [host\_addr](structgnttab__unmap__grant__ref.md#a378f5d746e702ca1ceff2171f345f5e6);

[ 294](structgnttab__unmap__grant__ref.md#a4a2c5b458a51146d838519bcff6a515b) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [dev\_bus\_addr](structgnttab__unmap__grant__ref.md#a4a2c5b458a51146d838519bcff6a515b);

[ 295](structgnttab__unmap__grant__ref.md#a25caf3cd55321745a94588299e396156) [grant\_handle\_t](grant__table_8h.md#a1eade3c86c0fd0e71217eefaa3b38cd1) [handle](structgnttab__unmap__grant__ref.md#a25caf3cd55321745a94588299e396156);

296 /\* OUT parameters. \*/

[ 297](structgnttab__unmap__grant__ref.md#a606704496ead790a42d6d5cbcb9aac2e) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [status](structgnttab__unmap__grant__ref.md#a606704496ead790a42d6d5cbcb9aac2e); /\* => enum grant\_status \*/

298};

[ 299](grant__table_8h.md#ab6f946404db417d188cafe0f68580130)typedef struct [gnttab\_unmap\_grant\_ref](structgnttab__unmap__grant__ref.md) [gnttab\_unmap\_grant\_ref\_t](grant__table_8h.md#ab6f946404db417d188cafe0f68580130);

[ 300](grant__table_8h.md#a35aae9b9d970900cb87ff8ebfc5b720e)[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)([gnttab\_unmap\_grant\_ref\_t](grant__table_8h.md#ab6f946404db417d188cafe0f68580130));

301

302/\*

303 \* GNTTABOP\_setup\_table: Set up a grant table for <dom> comprising at least

304 \* <nr\_frames> pages. The frame addresses are written to the <frame\_list>.

305 \* Only <nr\_frames> addresses are written, even if the table is larger.

306 \* NOTES:

307 \* 1. <dom> may be specified as DOMID\_SELF.

308 \* 2. Only a sufficiently-privileged domain may specify <dom> != DOMID\_SELF.

309 \* 3. Xen may not support more than a single grant-table page per domain.

310 \*/

[ 311](structgnttab__setup__table.md)struct [gnttab\_setup\_table](structgnttab__setup__table.md) {

312 /\* IN parameters. \*/

[ 313](structgnttab__setup__table.md#acc7c6d1538fce7c04b287aa8118c7f69) [domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee) [dom](structgnttab__setup__table.md#acc7c6d1538fce7c04b287aa8118c7f69);

[ 314](structgnttab__setup__table.md#a57230635fcfd9e67fd1e503fbf7ec556) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [nr\_frames](structgnttab__setup__table.md#a57230635fcfd9e67fd1e503fbf7ec556);

315

316 /\* OUT parameters. \*/

[ 317](structgnttab__setup__table.md#ad73acf13a59e6c92c0d6ba6db6e6aedf) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [status](structgnttab__setup__table.md#ad73acf13a59e6c92c0d6ba6db6e6aedf); /\* => enum grant\_status \*/

318#if \_\_XEN\_INTERFACE\_VERSION\_\_ < 0x00040300

[ 319](structgnttab__setup__table.md#ad0056cc36b6574210f3e9b1b4da2cb35) [XEN\_GUEST\_HANDLE](structgnttab__setup__table.md#ad0056cc36b6574210f3e9b1b4da2cb35)(ulong) frame\_list;

320#else

321 [XEN\_GUEST\_HANDLE](arch-arm_8h.md#a59eac5b471e486c9cdb4743017fdfc20)([xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226)) frame\_list;

322#endif

323};

[ 324](grant__table_8h.md#ab7eab2489bbe46dec87a6b8d88ad41f9)typedef struct [gnttab\_setup\_table](structgnttab__setup__table.md) [gnttab\_setup\_table\_t](grant__table_8h.md#ab7eab2489bbe46dec87a6b8d88ad41f9);

[ 325](grant__table_8h.md#a58aa81b1014416c6f7665e51c348d015)[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)([gnttab\_setup\_table\_t](grant__table_8h.md#ab7eab2489bbe46dec87a6b8d88ad41f9));

326

327

328

329/\*

330 \* Bitfield values for gnttab\_map\_grant\_ref.flags.

331 \*/

332 /\* Map the grant entry for access by I/O devices. \*/

333#define \_GNTMAP\_device\_map (0)

[ 334](grant__table_8h.md#aae559e2f8155b38e032db211f2fb89fd)#define GNTMAP\_device\_map (1<<\_GNTMAP\_device\_map)

335 /\* Map the grant entry for access by host CPUs. \*/

336#define \_GNTMAP\_host\_map (1)

[ 337](grant__table_8h.md#a12fced9de545a35fe5d8982e8da565e2)#define GNTMAP\_host\_map (1<<\_GNTMAP\_host\_map)

338 /\* Accesses to the granted frame will be restricted to read-only access. \*/

339#define \_GNTMAP\_readonly (2)

[ 340](grant__table_8h.md#a00a2a7a5e3310500419b9cd0c765f268)#define GNTMAP\_readonly (1<<\_GNTMAP\_readonly)

341 /\*

342 \* GNTMAP\_host\_map subflag:

343 \* 0 => The host mapping is usable only by the guest OS.

344 \* 1 => The host mapping is usable by guest OS + current application.

345 \*/

346#define \_GNTMAP\_application\_map (3)

[ 347](grant__table_8h.md#acd1b7e44453bd81909a756e5dd2929d6)#define GNTMAP\_application\_map (1<<\_GNTMAP\_application\_map)

348

349 /\*

350 \* GNTMAP\_contains\_pte subflag:

351 \* 0 => This map request contains a host virtual address.

352 \* 1 => This map request contains the machine addess of the PTE to update.

353 \*/

354#define \_GNTMAP\_contains\_pte (4)

[ 355](grant__table_8h.md#a97e8e1150ee8ae0c6cf9101dd98f8f3d)#define GNTMAP\_contains\_pte (1<<\_GNTMAP\_contains\_pte)

356

357/\*

358 \* Bits to be placed in guest kernel available PTE bits (architecture

359 \* dependent; only supported when XENFEAT\_gnttab\_map\_avail\_bits is set).

360 \*/

361#define \_GNTMAP\_guest\_avail0 (16)

[ 362](grant__table_8h.md#ac4d9a6ba14cb3fe5b1a7daa035e6c84e)#define GNTMAP\_guest\_avail\_mask ((uint32\_t)~0 << \_GNTMAP\_guest\_avail0)

363

364/\*

365 \* Values for error status returns. All errors are -ve.

366 \*/

367/\* ` enum grant\_status { \*/

[ 368](grant__table_8h.md#a8b346596e565a7bfcc84c43dad1b5b4e)#define GNTST\_okay (0) /\* Normal return \*/

[ 369](grant__table_8h.md#a0f4d62b7f6986db7f1565c4842d44c2c)#define GNTST\_general\_error (-1) /\* General undefined error \*/

[ 370](grant__table_8h.md#acef8aeb07dfd790b304aee2b8037388d)#define GNTST\_bad\_domain (-2) /\* Unrecognsed domain id \*/

[ 371](grant__table_8h.md#aa95a512fed439a4d77d6b0fea66e7e34)#define GNTST\_bad\_gntref (-3) /\* Unrecognised or inappropriate gntref \*/

[ 372](grant__table_8h.md#afb88ba813ad01e706cfadf4d44a4e941)#define GNTST\_bad\_handle (-4) /\* Unrecognised or inappropriate handle \*/

[ 373](grant__table_8h.md#a8edfdaba9b072bab54894601f5e53157)#define GNTST\_bad\_virt\_addr (-5) /\* Inappropriate virtual address to map \*/

[ 374](grant__table_8h.md#a759747d060b61d7b0c8dbe2bd1772f73)#define GNTST\_bad\_dev\_addr (-6) /\* Inappropriate device address to unmap \*/

[ 375](grant__table_8h.md#a12d565fb321125c35c26b6c580bf778a)#define GNTST\_no\_device\_space (-7) /\* Out of space in I/O MMU \*/

[ 376](grant__table_8h.md#aab89203e7f7f4d18b999ba49167595ae)#define GNTST\_permission\_denied (-8) /\* Not enough privilege for operation \*/

[ 377](grant__table_8h.md#a669e9b8bed7a88bf0d2f09e5e6a6b011)#define GNTST\_bad\_page (-9) /\* Specified page was invalid for op \*/

[ 378](grant__table_8h.md#a6e675b4ef4a1477c9b4c6e29a207c900)#define GNTST\_bad\_copy\_arg (-10) /\* copy arguments cross page boundary \*/

[ 379](grant__table_8h.md#a514d6b98e5285c4e098aafebddb2597c)#define GNTST\_address\_too\_big (-11) /\* transfer page address too large \*/

[ 380](grant__table_8h.md#aa6dd5fbc418afb794115441ba78ba92f)#define GNTST\_eagain (-12) /\* Operation not done; try agains \*/

381/\* ` } \*/

382

[ 383](grant__table_8h.md#a164e86151574733f6739c37c8f6b9f70)#define GNTTABOP\_error\_msgs { \

384 "okay", \

385 "undefined error", \

386 "unrecognised domain id", \

387 "invalid grant reference", \

388 "invalid mapping handle", \

389 "invalid virtual address", \

390 "invalid device address", \

391 "no spare translation slot in the I/O MMU", \

392 "permission denied", \

393 "bad page", \

394 "copy arguments cross page boundary", \

395 "page address size too large", \

396 "operation not done; try again" \

397}

398

399#endif /\* \_\_XEN\_PUBLIC\_GRANT\_TABLE\_H\_\_ \*/

[xen\_pfn\_t](arch-arm_8h.md#a564b8052e6905461f66db791246d2226)

uint64\_t xen\_pfn\_t

**Definition** arch-arm.h:204

[XEN\_GUEST\_HANDLE](arch-arm_8h.md#a59eac5b471e486c9cdb4743017fdfc20)

#define XEN\_GUEST\_HANDLE(name)

**Definition** arch-arm.h:194

[DEFINE\_XEN\_GUEST\_HANDLE](arch-arm_8h.md#ae74e9f15fb9a0b53b9d10a529b84e121)

#define DEFINE\_XEN\_GUEST\_HANDLE(name)

**Definition** arch-arm.h:192

[grant\_handle\_t](grant__table_8h.md#a1eade3c86c0fd0e71217eefaa3b38cd1)

uint32\_t grant\_handle\_t

**Definition** grant\_table.h:247

[gnttab\_unmap\_grant\_ref\_t](grant__table_8h.md#ab6f946404db417d188cafe0f68580130)

struct gnttab\_unmap\_grant\_ref gnttab\_unmap\_grant\_ref\_t

**Definition** grant\_table.h:299

[gnttab\_setup\_table\_t](grant__table_8h.md#ab7eab2489bbe46dec87a6b8d88ad41f9)

struct gnttab\_setup\_table gnttab\_setup\_table\_t

**Definition** grant\_table.h:324

[gnttab\_map\_grant\_ref\_t](grant__table_8h.md#ac6ace01635e3b886a7f74d4e9ae3db78)

struct gnttab\_map\_grant\_ref gnttab\_map\_grant\_ref\_t

**Definition** grant\_table.h:277

[grant\_entry\_v1\_t](grant__table_8h.md#ad463d080d89bce70aa065aec9d62a69a)

#define grant\_entry\_v1\_t

**Definition** grant\_table.h:131

[grant\_entry\_v1](grant__table_8h.md#ae42428f85f6f40af58ce52d7cbb9a7bc)

#define grant\_entry\_v1

**Definition** grant\_table.h:130

[grant\_ref\_t](grant__table_8h.md#aee25f6c8ecefd1d7c52e49e4886aca3e)

uint32\_t grant\_ref\_t

**Definition** grant\_table.h:116

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[gnttab\_map\_grant\_ref](structgnttab__map__grant__ref.md)

**Definition** grant\_table.h:266

[gnttab\_map\_grant\_ref::flags](structgnttab__map__grant__ref.md#a0db5af518a433b4441729019e65e1e3d)

uint32\_t flags

**Definition** grant\_table.h:269

[gnttab\_map\_grant\_ref::dom](structgnttab__map__grant__ref.md#a14efe928545333fb0f3544cdf98dc0ab)

domid\_t dom

**Definition** grant\_table.h:271

[gnttab\_map\_grant\_ref::host\_addr](structgnttab__map__grant__ref.md#a2c811c2986d6d7d5236a261c50c3492c)

uint64\_t host\_addr

**Definition** grant\_table.h:268

[gnttab\_map\_grant\_ref::handle](structgnttab__map__grant__ref.md#a6c0ce65e16e117c0678d635a2ee1d3f0)

grant\_handle\_t handle

**Definition** grant\_table.h:274

[gnttab\_map\_grant\_ref::status](structgnttab__map__grant__ref.md#a738c22fab57008dcd5dac3651cfab66c)

int16\_t status

**Definition** grant\_table.h:273

[gnttab\_map\_grant\_ref::dev\_bus\_addr](structgnttab__map__grant__ref.md#ac90b06b676c85d65f8311fb72f0cfa5a)

uint64\_t dev\_bus\_addr

**Definition** grant\_table.h:275

[gnttab\_map\_grant\_ref::ref](structgnttab__map__grant__ref.md#aff19dc5005ea1082cc9b5cd6bb89a2d7)

grant\_ref\_t ref

**Definition** grant\_table.h:270

[gnttab\_setup\_table](structgnttab__setup__table.md)

**Definition** grant\_table.h:311

[gnttab\_setup\_table::nr\_frames](structgnttab__setup__table.md#a57230635fcfd9e67fd1e503fbf7ec556)

uint32\_t nr\_frames

**Definition** grant\_table.h:314

[gnttab\_setup\_table::dom](structgnttab__setup__table.md#acc7c6d1538fce7c04b287aa8118c7f69)

domid\_t dom

**Definition** grant\_table.h:313

[gnttab\_setup\_table::XEN\_GUEST\_HANDLE](structgnttab__setup__table.md#ad0056cc36b6574210f3e9b1b4da2cb35)

XEN\_GUEST\_HANDLE(ulong) frame\_list

[gnttab\_setup\_table::status](structgnttab__setup__table.md#ad73acf13a59e6c92c0d6ba6db6e6aedf)

int16\_t status

**Definition** grant\_table.h:317

[gnttab\_unmap\_grant\_ref](structgnttab__unmap__grant__ref.md)

**Definition** grant\_table.h:291

[gnttab\_unmap\_grant\_ref::handle](structgnttab__unmap__grant__ref.md#a25caf3cd55321745a94588299e396156)

grant\_handle\_t handle

**Definition** grant\_table.h:295

[gnttab\_unmap\_grant\_ref::host\_addr](structgnttab__unmap__grant__ref.md#a378f5d746e702ca1ceff2171f345f5e6)

uint64\_t host\_addr

**Definition** grant\_table.h:293

[gnttab\_unmap\_grant\_ref::dev\_bus\_addr](structgnttab__unmap__grant__ref.md#a4a2c5b458a51146d838519bcff6a515b)

uint64\_t dev\_bus\_addr

**Definition** grant\_table.h:294

[gnttab\_unmap\_grant\_ref::status](structgnttab__unmap__grant__ref.md#a606704496ead790a42d6d5cbcb9aac2e)

int16\_t status

**Definition** grant\_table.h:297

[grant\_entry::domid](structgrant__entry.md#a16a644be72a9cce14e4682745714f78b)

domid\_t domid

**Definition** grant\_table.h:137

[grant\_entry::frame](structgrant__entry.md#a6fe4635ae57bc41ed9aa1c65848f6c9a)

uint32\_t frame

**Definition** grant\_table.h:144

[grant\_entry::flags](structgrant__entry.md#ae45f6989c80eff0ad6faf7bcc89edcc4)

uint16\_t flags

**Definition** grant\_table.h:135

[xen.h](xen_8h.md)

[domid\_t](xen_8h.md#a52133e9b6faf803a509868928d1c0eee)

uint16\_t domid\_t

**Definition** xen.h:217

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [public](dir_a9d090e3588b677c614b5c45cd68e13b.md)
- [grant\_table.h](grant__table_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
