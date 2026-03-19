---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/csr_8h_source.html
original_path: doxygen/html/csr_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

csr.h

[Go to the documentation of this file.](csr_8h.md)

1/\*

2 \* Copyright (c) 2020 Michael Schaffner

3 \* Copyright (c) 2020 BayLibre, SAS

4 \*

5 \* SPDX-License-Identifier: SHL-0.51

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#ifndef CSR\_H\_

10#define CSR\_H\_

11

[ 12](csr_8h.md#a3f4df6dc4219593cb6e8bd13d636e844)#define MSTATUS\_UIE 0x00000001

[ 13](csr_8h.md#a29a63dca3cfcf13877a0c354dc081505)#define MSTATUS\_SIE 0x00000002

[ 14](csr_8h.md#ab549408c2d03c2e09fbfab2898683097)#define MSTATUS\_HIE 0x00000004

[ 15](csr_8h.md#a225cb34e3b991318fa87f090cfc3fc5f)#define MSTATUS\_MIE 0x00000008

[ 16](csr_8h.md#a17711b78183c43687036c60962c278cb)#define MSTATUS\_UPIE 0x00000010

[ 17](csr_8h.md#ac7fef7988d408f1f4ebe9e3849d68bb2)#define MSTATUS\_SPIE 0x00000020

[ 18](csr_8h.md#aa0f7327c94aa1210a819f1d47d3e1700)#define MSTATUS\_HPIE 0x00000040

[ 19](csr_8h.md#a05fc511bb3d22b5e1abe8b9ccb30e7b3)#define MSTATUS\_MPIE 0x00000080

[ 20](csr_8h.md#ad4b09023ff5bcbb14192e845c0532944)#define MSTATUS\_SPP 0x00000100

[ 21](csr_8h.md#ad980a627f9de5aed42de70d2ec617a70)#define MSTATUS\_HPP 0x00000600

[ 22](csr_8h.md#a2acf460f4ceda869c88c00878cb44314)#define MSTATUS\_MPP 0x00001800

[ 23](csr_8h.md#ab7b9c10a700f7570d44c49f369b6fcce)#define MSTATUS\_FS 0x00006000

[ 24](csr_8h.md#a768db67b06c8341a4da264abcb7f3cfe)#define MSTATUS\_XS 0x00018000

[ 25](csr_8h.md#afa733f6d7aadab5b3c0318d005745a98)#define MSTATUS\_MPRV 0x00020000

[ 26](csr_8h.md#a656346a0a53639f2d60ca8e56506d60a)#define MSTATUS\_SUM 0x00040000

[ 27](csr_8h.md#a8f4b37cdd71162f5b7adb583010443cb)#define MSTATUS\_MXR 0x00080000

[ 28](csr_8h.md#a9d5bb2ea5f82f54c8b9b5363e3d9a9e2)#define MSTATUS\_TVM 0x00100000

[ 29](csr_8h.md#a8e19c878576b1c77490cdfa10796acb0)#define MSTATUS\_TW 0x00200000

[ 30](csr_8h.md#a2507709e2a407afba032f882939b9502)#define MSTATUS\_TSR 0x00400000

[ 31](csr_8h.md#acca6e5c4f8af666a9b299af295f43348)#define MSTATUS32\_SD 0x80000000

[ 32](csr_8h.md#ad2f3eafd02e6788c7a1310db259bd136)#define MSTATUS\_UXL 0x0000000300000000

[ 33](csr_8h.md#aac0dae4a6c4f6decfb2e2845cd1b3c00)#define MSTATUS\_SXL 0x0000000C00000000

[ 34](csr_8h.md#a9d7df82e40e8cf00821e97a0bb8db04e)#define MSTATUS64\_SD 0x8000000000000000

35

[ 36](csr_8h.md#a431c67f7f0e4b5dbdf2048310ad814e0)#define SSTATUS\_UIE 0x00000001

[ 37](csr_8h.md#a1c1f1da0ecfca5bc4fc4db3acadf1bc8)#define SSTATUS\_SIE 0x00000002

[ 38](csr_8h.md#a796ad1a8b2314776082e72e13f4a30cf)#define SSTATUS\_UPIE 0x00000010

[ 39](csr_8h.md#a3f9373ba6db2ce5e5c7ea28c2a5b3df9)#define SSTATUS\_SPIE 0x00000020

[ 40](csr_8h.md#a4d0820d6a8b0c5b0fef6875a985d3370)#define SSTATUS\_SPP 0x00000100

[ 41](csr_8h.md#aff201911cccf15e446c43ba67b0f1aa7)#define SSTATUS\_FS 0x00006000

[ 42](csr_8h.md#a2abef254823774927e3bf6b029fbad9d)#define SSTATUS\_XS 0x00018000

[ 43](csr_8h.md#ac8726a0a74700feb038f6b74dbb3dc0f)#define SSTATUS\_SUM 0x00040000

[ 44](csr_8h.md#a3387d409543279220628618c0909fe55)#define SSTATUS\_MXR 0x00080000

[ 45](csr_8h.md#a5f2248b3f4a648ce63c0468a92132971)#define SSTATUS32\_SD 0x80000000

[ 46](csr_8h.md#a66d79e7ab75a06dbbd7d7f36d0c1c52a)#define SSTATUS\_UXL 0x0000000300000000

[ 47](csr_8h.md#a517c9ab9421f99b99f5da4d549177f38)#define SSTATUS64\_SD 0x8000000000000000

48

[ 49](csr_8h.md#a966a5f66e8f82245a23754d953272e26)#define DCSR\_XDEBUGVER (3U<<30)

[ 50](csr_8h.md#a70f0772b052aba7d37433a6abc524a05)#define DCSR\_NDRESET (1<<29)

[ 51](csr_8h.md#ae0060c3218daba2cfe6b3a74eaa8004e)#define DCSR\_FULLRESET (1<<28)

[ 52](csr_8h.md#aee469b64e88766dd85645de42b9f2a5c)#define DCSR\_EBREAKM (1<<15)

[ 53](csr_8h.md#a113e941ee7b34c40b794e5b39638f79c)#define DCSR\_EBREAKH (1<<14)

[ 54](csr_8h.md#aa06fd020c5e6a4bc5e97715763eb85ff)#define DCSR\_EBREAKS (1<<13)

[ 55](csr_8h.md#ac6c4bbab3051160066b73951e0c58e84)#define DCSR\_EBREAKU (1<<12)

[ 56](csr_8h.md#a7367ccfe98195ecdf126ea1f26f85b37)#define DCSR\_STOPCYCLE (1<<10)

[ 57](csr_8h.md#a8e011fbc15f29c25a9197e306eefc4bc)#define DCSR\_STOPTIME (1<<9)

[ 58](csr_8h.md#a81c7d48193a62ce9c189bb0d2d104230)#define DCSR\_CAUSE (7<<6)

[ 59](csr_8h.md#abf604fa800bf4ef6aa8e58e662c34317)#define DCSR\_DEBUGINT (1<<5)

[ 60](csr_8h.md#a1a6de95ef85a1337a6c9bbfb8588d137)#define DCSR\_HALT (1<<3)

[ 61](csr_8h.md#a5136c4da715d2aa79f23dab172db4fea)#define DCSR\_STEP (1<<2)

[ 62](csr_8h.md#a110f30f7c9d25c057e2dfe1477e5b742)#define DCSR\_PRV (3<<0)

63

[ 64](csr_8h.md#a4cf6a474d1cc251a206f9ab512794581)#define DCSR\_CAUSE\_NONE 0

[ 65](csr_8h.md#a0ca8d97eb41a31351ea471e87a6cb383)#define DCSR\_CAUSE\_SWBP 1

[ 66](csr_8h.md#a73fbd946de0ee961a37aef9cf0113c10)#define DCSR\_CAUSE\_HWBP 2

[ 67](csr_8h.md#a28fc94b1080dd0151ad942fd38ecf04d)#define DCSR\_CAUSE\_DEBUGINT 3

[ 68](csr_8h.md#a47955acab2f0d71bde8d2dbacebc1ce1)#define DCSR\_CAUSE\_STEP 4

[ 69](csr_8h.md#abbe672c98c7614d6346e83e80ee0df18)#define DCSR\_CAUSE\_HALT 5

70

[ 71](csr_8h.md#a4be6cc72618e21a3011b626aff83eae8)#define MCONTROL\_TYPE(xlen) (0xfULL<<((xlen)-4))

[ 72](csr_8h.md#ab0c4b6681fe0b3fba6d512a084e318b2)#define MCONTROL\_DMODE(xlen) (1ULL<<((xlen)-5))

[ 73](csr_8h.md#a9d2d58a19b42feb156d060c4860773e3)#define MCONTROL\_MASKMAX(xlen) (0x3fULL<<((xlen)-11))

74

[ 75](csr_8h.md#ae3271344364caa6fdeedf62cad06ec32)#define MCONTROL\_SELECT (1<<19)

[ 76](csr_8h.md#a05f32197da7d4f4da6cd9ffd706f0181)#define MCONTROL\_TIMING (1<<18)

[ 77](csr_8h.md#aa00ebcbad8ef4fd0b082ae955c70159a)#define MCONTROL\_ACTION (0x3f<<12)

[ 78](csr_8h.md#a1ab44c2e81a1a31e766ec682cad96ea9)#define MCONTROL\_CHAIN (1<<11)

[ 79](csr_8h.md#a29db79af22f38eb123f1bf1c11c4c92a)#define MCONTROL\_MATCH (0xf<<7)

[ 80](csr_8h.md#a0b9146969080ec187962cbe3ee3f5aba)#define MCONTROL\_M (1<<6)

[ 81](csr_8h.md#a02a3db7fdab9947d0c8239c011d1274e)#define MCONTROL\_H (1<<5)

[ 82](csr_8h.md#ac9c0ad84304e51a07e42a9a70c210c95)#define MCONTROL\_S (1<<4)

[ 83](csr_8h.md#a13c4a265729f4de2d9e7319e5aa29d8d)#define MCONTROL\_U (1<<3)

[ 84](csr_8h.md#a16ef1fd919fc1d8cce3e064aaf606a06)#define MCONTROL\_EXECUTE (1<<2)

[ 85](csr_8h.md#aeddbbc18f165aa8764e3b201e57958f7)#define MCONTROL\_STORE (1<<1)

[ 86](csr_8h.md#a77472c8d179d5bf165e420aec140d1ad)#define MCONTROL\_LOAD (1<<0)

87

[ 88](csr_8h.md#a90057d3240f345a4c152667f336bb50f)#define MCONTROL\_TYPE\_NONE 0

[ 89](csr_8h.md#a510525cf4b02311be0f97070a0867e8e)#define MCONTROL\_TYPE\_MATCH 2

90

[ 91](csr_8h.md#a48f74b38a5f172d576549d6ed3c2e9b0)#define MCONTROL\_ACTION\_DEBUG\_EXCEPTION 0

[ 92](csr_8h.md#a283b3199ea4bb5f6c27ccbe880d426df)#define MCONTROL\_ACTION\_DEBUG\_MODE 1

[ 93](csr_8h.md#a40674423a8d52e03f26a535f6833ebed)#define MCONTROL\_ACTION\_TRACE\_START 2

[ 94](csr_8h.md#ad3f67c74ef8b33dbfcca678a3c381e62)#define MCONTROL\_ACTION\_TRACE\_STOP 3

[ 95](csr_8h.md#a227b2447936cd8f134d9ca084a233fe2)#define MCONTROL\_ACTION\_TRACE\_EMIT 4

96

[ 97](csr_8h.md#a9b67fcfd9cce0df82d2862dbf4e6e1e6)#define MCONTROL\_MATCH\_EQUAL 0

[ 98](csr_8h.md#a529552f378149e8b6a1d940f1279367b)#define MCONTROL\_MATCH\_NAPOT 1

[ 99](csr_8h.md#a161f7167c606c9e867af1bcba0cb8eab)#define MCONTROL\_MATCH\_GE 2

[ 100](csr_8h.md#afd67f3e374a7f912ec48d02a40730a1d)#define MCONTROL\_MATCH\_LT 3

[ 101](csr_8h.md#a9a5c571a197a84c425a54bfeeab76503)#define MCONTROL\_MATCH\_MASK\_LOW 4

[ 102](csr_8h.md#ad53872401bc83df4c67017323ff47c29)#define MCONTROL\_MATCH\_MASK\_HIGH 5

103

[ 104](csr_8h.md#a0bda37d26a2a610c14486b0cd367becc)#define MIP\_SSIP (1 << IRQ\_S\_SOFT)

[ 105](csr_8h.md#ab8226593c790568a432eeb8ca7bb4270)#define MIP\_HSIP (1 << IRQ\_H\_SOFT)

[ 106](csr_8h.md#a09c2dda94121d966560ac22fe6becdb3)#define MIP\_MSIP (1 << IRQ\_M\_SOFT)

[ 107](csr_8h.md#a40a54377f1fdb317c3f7397043874cae)#define MIP\_STIP (1 << IRQ\_S\_TIMER)

[ 108](csr_8h.md#a15a22cfcd6f41aea04b9943a71d0a2ff)#define MIP\_HTIP (1 << IRQ\_H\_TIMER)

[ 109](csr_8h.md#a51c044e20264a9e2a875b17482e8ff11)#define MIP\_MTIP (1 << IRQ\_M\_TIMER)

[ 110](csr_8h.md#a3fdf03c28e7d1baba8fa6bb11eae8561)#define MIP\_SEIP (1 << IRQ\_S\_EXT)

[ 111](csr_8h.md#a1c1ae7b718753753a5c99292450df837)#define MIP\_HEIP (1 << IRQ\_H\_EXT)

[ 112](csr_8h.md#aa0b390526aa02e969ae64235b983069a)#define MIP\_MEIP (1 << IRQ\_M\_EXT)

113

[ 114](csr_8h.md#acdfe2a4376d4c9873b865b878c6d5d2e)#define SIP\_SSIP MIP\_SSIP

[ 115](csr_8h.md#aa32b89e7176c6d37caa3ad78a600f4a1)#define SIP\_STIP MIP\_STIP

116

[ 117](csr_8h.md#a0584431e22db30065abffb94459477c4)#define PRV\_U 0

[ 118](csr_8h.md#a3131c9addf7b5ecc1da9f7b0eff9815d)#define PRV\_S 1

[ 119](csr_8h.md#af11d40d5f172d3095bf39a23ba714552)#define PRV\_H 2

[ 120](csr_8h.md#afee966c8a48cb4075680eb0cc08ab32e)#define PRV\_M 3

121

[ 122](csr_8h.md#ab288573db6fbd0bc09681f033971c892)#define SATP32\_MODE 0x80000000

[ 123](csr_8h.md#a0cb3acb8d313b5fffdf4a562dc19ae15)#define SATP32\_ASID 0x7FC00000

[ 124](csr_8h.md#a1feca7bca79664d5d53c284b8a078f5a)#define SATP32\_PPN 0x003FFFFF

[ 125](csr_8h.md#a7fceced1f54fd0e3b2ae6bace3ae30cf)#define SATP64\_MODE 0xF000000000000000

[ 126](csr_8h.md#ae887d5205d95a9de7f7c33381105ecb0)#define SATP64\_ASID 0x0FFFF00000000000

[ 127](csr_8h.md#ade3d29abc4e227334b8c47725131ba0e)#define SATP64\_PPN 0x00000FFFFFFFFFFF

128

[ 129](csr_8h.md#acda96055d5d29a3cb3900b41e1b4410f)#define SATP\_MODE\_OFF 0

[ 130](csr_8h.md#a889f093e7004e76a1edbd106bfe10986)#define SATP\_MODE\_SV32 1

[ 131](csr_8h.md#a8b39454e1fcc5204db5a6772f73bc6a1)#define SATP\_MODE\_SV39 8

[ 132](csr_8h.md#aaf4e2614414d57a362260f5647dcd6ad)#define SATP\_MODE\_SV48 9

[ 133](csr_8h.md#ad7db356d5f561db9cff03caa6bc9f249)#define SATP\_MODE\_SV57 10

[ 134](csr_8h.md#a6b96c8df00f46270747521c710fd70be)#define SATP\_MODE\_SV64 11

135

[ 136](csr_8h.md#a383d3ee4d5727ef3fb4437d954be3b21)#define PMP\_R 0x01

[ 137](csr_8h.md#a5f34c98b252436e69ad95e766abf8482)#define PMP\_W 0x02

[ 138](csr_8h.md#aabfce7f7dde3e93eb596074b4d107bec)#define PMP\_X 0x04

[ 139](csr_8h.md#a47df3f6548f6106ad54d3def500db71f)#define PMP\_A 0x18

[ 140](csr_8h.md#a68f26499e9a07ee23940bcd1ff49e51d)#define PMP\_L 0x80

[ 141](csr_8h.md#af5a33910ca1e7603b2c483a2966e2d53)#define PMP\_SHIFT 2

142

[ 143](csr_8h.md#a0c34c467a11c27392fdaa5901d8b6361)#define PMP\_TOR 0x08

[ 144](csr_8h.md#a1530fe241c9693a40ba2d54f97757d28)#define PMP\_NA4 0x10

[ 145](csr_8h.md#a2ebfc3724e055e0777d3d3562d9c6367)#define PMP\_NAPOT 0x18

146

[ 147](csr_8h.md#a1f426d6231a15fe1801b3206c712cf76)#define IRQ\_S\_SOFT 1

[ 148](csr_8h.md#ac3fe3deef5576f320abc55464c9fb980)#define IRQ\_H\_SOFT 2

[ 149](csr_8h.md#a02e2db32b33eb8cf23622150ac372200)#define IRQ\_M\_SOFT 3

[ 150](csr_8h.md#ac7acfa6b0f632b9cd762a0e0abd1df08)#define IRQ\_S\_TIMER 5

[ 151](csr_8h.md#a9ea3c09e4c1dde4b1c9d1be6d7d82528)#define IRQ\_H\_TIMER 6

[ 152](csr_8h.md#aa5b87ef0a6024ad69009faff8fd6a9d5)#define IRQ\_M\_TIMER 7

[ 153](csr_8h.md#aedc582eeff2cc10dcb000c5f08dda3c3)#define IRQ\_S\_EXT 9

[ 154](csr_8h.md#aa09fee2ca390c169c63b0c52475e38f7)#define IRQ\_H\_EXT 10

[ 155](csr_8h.md#a43fba639eb8d7ee37648cc0af12cf59b)#define IRQ\_M\_EXT 11

[ 156](csr_8h.md#a26e341b99075274d38face5be46579a6)#define IRQ\_COP 12

[ 157](csr_8h.md#ab12a3e27140376a52c9f9999404a73f6)#define IRQ\_HOST 13

158

[ 159](csr_8h.md#a325a70437a7ebec841da1fc84384c14c)#define DEFAULT\_RSTVEC 0x00001000

[ 160](csr_8h.md#adf17cca244ad8b81238cb56911c09c6e)#define CLINT\_BASE 0x02000000

[ 161](csr_8h.md#a6e8c33caacb405a8bde39c35c02928d0)#define CLINT\_SIZE 0x000c0000

[ 162](csr_8h.md#aa200ded9184ef068f4fdbb302e7203d9)#define EXT\_IO\_BASE 0x40000000

[ 163](csr_8h.md#af664e1a9045803369e50e29fdc1ca530)#define DRAM\_BASE 0x80000000

164

165/\* page table entry (PTE) fields \*/

[ 166](csr_8h.md#a9a3c738182007bee471e44aae04c386f)#define PTE\_V 0x001 /\* Valid \*/

[ 167](csr_8h.md#a3a188134a2cbd69e161521fb169ecd08)#define PTE\_R 0x002 /\* Read \*/

[ 168](csr_8h.md#a058fcbcc3e1eab2c09c68b3e5221c545)#define PTE\_W 0x004 /\* Write \*/

[ 169](csr_8h.md#ae20c834a93867eedc88007621c74ad55)#define PTE\_X 0x008 /\* Execute \*/

[ 170](csr_8h.md#adced9836a1dc98d72849361e6ab03cda)#define PTE\_U 0x010 /\* User \*/

[ 171](csr_8h.md#a50cfccabb1927e67c7a0e3b90e8b0635)#define PTE\_G 0x020 /\* Global \*/

[ 172](csr_8h.md#af2d908a8af1d94a6aaf803ab40fe0951)#define PTE\_A 0x040 /\* Accessed \*/

[ 173](csr_8h.md#ae80b38f12787d02087c4575c48c36d88)#define PTE\_D 0x080 /\* Dirty \*/

[ 174](csr_8h.md#a8e71d0b15291edc78a3240cc667f9ad8)#define PTE\_SOFT 0x300 /\* Reserved for Software \*/

175

[ 176](csr_8h.md#a5b5b713a1ec901153c786686d5962574)#define PTE\_PPN\_SHIFT 10

177

[ 178](csr_8h.md#aa0a707cf44e82dc9efa94304582586a6)#define PTE\_TABLE(PTE) (((PTE) & (PTE\_V | PTE\_R | PTE\_W | PTE\_X)) == PTE\_V)

179

[ 180](csr_8h.md#a3c9ccd5ef4dec9e513f488c6e2c26cc2)#define INSERT\_FIELD(val, which, fieldval) \

181( \

182 ((val) & ~(which)) | ((fieldval) \* ((which) & ~((which)-1))) \

183) \

184

[ 185](csr_8h.md#a1b19216c67cb23fc1c46136325b732d9)#define csr\_read(csr) \

186({ \

187 register unsigned long \_\_rv; \

188 \_\_asm\_\_ volatile ("csrr %0, " STRINGIFY(csr) \

189 : "=r" (\_\_rv)); \

190 \_\_rv; \

191})

192

[ 193](csr_8h.md#ae4f751778cfb2bd0b2af00b78f8fe978)#define csr\_write(csr, val) \

194({ \

195 unsigned long \_\_wv = (unsigned long)(val); \

196 \_\_asm\_\_ volatile ("csrw " STRINGIFY(csr) ", %0" \

197 : : "rK" (\_\_wv) \

198 : "memory"); \

199})

200

201

[ 202](csr_8h.md#ace392a09e4bfaade8272beed4067ecf7)#define csr\_read\_set(csr, val) \

203({ \

204 unsigned long \_\_rsv = (unsigned long)(val); \

205 \_\_asm\_\_ volatile ("csrrs %0, " STRINGIFY(csr) ", %1" \

206 : "=r" (\_\_rsv) : "rK" (\_\_rsv) \

207 : "memory"); \

208 \_\_rsv; \

209})

210

[ 211](csr_8h.md#a217429a8671c8fae6d11b3e9c3fa405d)#define csr\_set(csr, val) \

212({ \

213 unsigned long \_\_sv = (unsigned long)(val); \

214 \_\_asm\_\_ volatile ("csrs " STRINGIFY(csr) ", %0" \

215 : : "rK" (\_\_sv) \

216 : "memory"); \

217})

218

[ 219](csr_8h.md#ab23f430909beb00d5e72185ce88cb403)#define csr\_read\_clear(csr, val) \

220({ \

221 unsigned long \_\_rcv = (unsigned long)(val); \

222 \_\_asm\_\_ volatile ("csrrc %0, " STRINGIFY(csr) ", %1" \

223 : "=r" (\_\_rcv) : "rK" (\_\_rcv) \

224 : "memory"); \

225 \_\_rcv; \

226})

227

[ 228](csr_8h.md#a1bb400f4225ecdbd577a45515100d4e0)#define csr\_clear(csr, val) \

229({ \

230 unsigned long \_\_cv = (unsigned long)(val); \

231 \_\_asm\_\_ volatile ("csrc " STRINGIFY(csr) ", %0" \

232 : : "rK" (\_\_cv) \

233 : "memory"); \

234})

235

236#endif /\* CSR\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [riscv](dir_e840f8ec4c8f41e913ceb572466dc8a4.md)
- [csr.h](csr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
