---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ivshmem_8h_source.html
original_path: doxygen/html/ivshmem_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ivshmem.h

[Go to the documentation of this file.](ivshmem_8h.md)

1/\*

2 \* Copyright (c) 2020 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_VIRTUALIZATION\_IVSHMEM\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_VIRTUALIZATION\_IVSHMEM\_H\_

9

16

17#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

18#include <stddef.h>

19#include <[zephyr/device.h](device_8h.md)>

20#include <[zephyr/kernel.h](kernel_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

[ 26](group__ivshmem.md#gad1a29cd2df2107001a3461947032db6c)#define IVSHMEM\_V2\_PROTO\_UNDEFINED 0x0000

[ 27](group__ivshmem.md#gae65765ef159aa70ebed6db295a01ce00)#define IVSHMEM\_V2\_PROTO\_NET 0x0001

28

[ 29](group__ivshmem.md#gaf8f761888728090ab6adb11f3b700057)typedef [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) (\*[ivshmem\_get\_mem\_f](group__ivshmem.md#gaf8f761888728090ab6adb11f3b700057))(const struct [device](structdevice.md) \*dev,

30 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*memmap);

31

[ 32](group__ivshmem.md#ga8a6f4c145426f8a28c0f3a52875b7ea1)typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[ivshmem\_get\_id\_f](group__ivshmem.md#ga8a6f4c145426f8a28c0f3a52875b7ea1))(const struct [device](structdevice.md) \*dev);

33

[ 34](group__ivshmem.md#ga7e25f5db9ac889a2ff05694f60f66e39)typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) (\*[ivshmem\_get\_vectors\_f](group__ivshmem.md#ga7e25f5db9ac889a2ff05694f60f66e39))(const struct [device](structdevice.md) \*dev);

35

[ 36](group__ivshmem.md#ga1af6d005fac141c84716b18705219bfd)typedef int (\*[ivshmem\_int\_peer\_f](group__ivshmem.md#ga1af6d005fac141c84716b18705219bfd))(const struct [device](structdevice.md) \*dev,

37 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peer\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector);

38

[ 39](group__ivshmem.md#ga842bee3ff990f166665593c384c6bb21)typedef int (\*[ivshmem\_register\_handler\_f](group__ivshmem.md#ga842bee3ff990f166665593c384c6bb21))(const struct [device](structdevice.md) \*dev,

40 struct [k\_poll\_signal](structk__poll__signal.md) \*[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69),

41 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector);

42

43#ifdef CONFIG\_IVSHMEM\_V2

44

45typedef [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) (\*ivshmem\_get\_rw\_mem\_section\_f)(const struct [device](structdevice.md) \*dev,

46 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*memmap);

47

48typedef [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) (\*ivshmem\_get\_output\_mem\_section\_f)(const struct [device](structdevice.md) \*dev,

49 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peer\_id,

50 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*memmap);

51

52typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*ivshmem\_get\_state\_f)(const struct [device](structdevice.md) \*dev,

53 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peer\_id);

54

55typedef int (\*ivshmem\_set\_state\_f)(const struct [device](structdevice.md) \*dev,

56 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

57

58typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*ivshmem\_get\_max\_peers\_f)(const struct [device](structdevice.md) \*dev);

59

60typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) (\*ivshmem\_get\_protocol\_f)(const struct [device](structdevice.md) \*dev);

61

62typedef int (\*ivshmem\_enable\_interrupts\_f)(const struct [device](structdevice.md) \*dev,

63 bool enable);

64

65#endif /\* CONFIG\_IVSHMEM\_V2 \*/

66

[ 67](structivshmem__driver__api.md)\_\_subsystem struct [ivshmem\_driver\_api](structivshmem__driver__api.md) {

[ 68](structivshmem__driver__api.md#afd4fc50b7cdf91ab1ed56193799d0e47) [ivshmem\_get\_mem\_f](group__ivshmem.md#gaf8f761888728090ab6adb11f3b700057) [get\_mem](structivshmem__driver__api.md#afd4fc50b7cdf91ab1ed56193799d0e47);

[ 69](structivshmem__driver__api.md#a9b689bd1d35adb9f806a16bba14d6810) [ivshmem\_get\_id\_f](group__ivshmem.md#ga8a6f4c145426f8a28c0f3a52875b7ea1) [get\_id](structivshmem__driver__api.md#a9b689bd1d35adb9f806a16bba14d6810);

[ 70](structivshmem__driver__api.md#ab302c92b722d88c281fd57a26389f58b) [ivshmem\_get\_vectors\_f](group__ivshmem.md#ga7e25f5db9ac889a2ff05694f60f66e39) [get\_vectors](structivshmem__driver__api.md#ab302c92b722d88c281fd57a26389f58b);

[ 71](structivshmem__driver__api.md#aa10ef98079775f56b4763f31c2e6654d) [ivshmem\_int\_peer\_f](group__ivshmem.md#ga1af6d005fac141c84716b18705219bfd) [int\_peer](structivshmem__driver__api.md#aa10ef98079775f56b4763f31c2e6654d);

[ 72](structivshmem__driver__api.md#a083b127047c28175c250fa0af9080ec8) [ivshmem\_register\_handler\_f](group__ivshmem.md#ga842bee3ff990f166665593c384c6bb21) [register\_handler](structivshmem__driver__api.md#a083b127047c28175c250fa0af9080ec8);

73#ifdef CONFIG\_IVSHMEM\_V2

74 ivshmem\_get\_rw\_mem\_section\_f get\_rw\_mem\_section;

75 ivshmem\_get\_output\_mem\_section\_f get\_output\_mem\_section;

76 ivshmem\_get\_state\_f get\_state;

77 ivshmem\_set\_state\_f set\_state;

78 ivshmem\_get\_max\_peers\_f get\_max\_peers;

79 ivshmem\_get\_protocol\_f get\_protocol;

80 ivshmem\_enable\_interrupts\_f enable\_interrupts;

81#endif

82};

83

[ 98](group__ivshmem.md#gaef043cbfbe0aa5061db57f9bbae02eca)\_\_syscall size\_t [ivshmem\_get\_mem](group__ivshmem.md#gaef043cbfbe0aa5061db57f9bbae02eca)(const struct [device](structdevice.md) \*dev,

99 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*memmap);

100

101static inline size\_t z\_impl\_ivshmem\_get\_mem(const struct [device](structdevice.md) \*dev,

102 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*memmap)

103{

104 const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*api =

105 (const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

106

107 return api->get\_mem(dev, memmap);

108}

109

[ 117](group__ivshmem.md#gab2f0ccd5a2b8203a54ee5707b3afd6cc)\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [ivshmem\_get\_id](group__ivshmem.md#gab2f0ccd5a2b8203a54ee5707b3afd6cc)(const struct [device](structdevice.md) \*dev);

118

119static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_ivshmem\_get\_id(const struct [device](structdevice.md) \*dev)

120{

121 const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*api =

122 (const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

123

124 return api->get\_id(dev);

125}

126

[ 134](group__ivshmem.md#gafee360f2c35abb9a203dd9f4838b8846)\_\_syscall [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ivshmem\_get\_vectors](group__ivshmem.md#gafee360f2c35abb9a203dd9f4838b8846)(const struct [device](structdevice.md) \*dev);

135

136static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) z\_impl\_ivshmem\_get\_vectors(const struct [device](structdevice.md) \*dev)

137{

138 const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*api =

139 (const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

140

141 return api->get\_vectors(dev);

142}

143

[ 153](group__ivshmem.md#gab4e02271f8b854c783c359aca240d20c)\_\_syscall int [ivshmem\_int\_peer](group__ivshmem.md#gab4e02271f8b854c783c359aca240d20c)(const struct [device](structdevice.md) \*dev,

154 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peer\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector);

155

156static inline int z\_impl\_ivshmem\_int\_peer(const struct [device](structdevice.md) \*dev,

157 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peer\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector)

158{

159 const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*api =

160 (const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

161

162 return api->int\_peer(dev, peer\_id, vector);

163}

164

[ 180](group__ivshmem.md#ga88aacb71bff0375c10fdb48e34b359fe)\_\_syscall int [ivshmem\_register\_handler](group__ivshmem.md#ga88aacb71bff0375c10fdb48e34b359fe)(const struct [device](structdevice.md) \*dev,

181 struct [k\_poll\_signal](structk__poll__signal.md) \*[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69),

182 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector);

183

184static inline int z\_impl\_ivshmem\_register\_handler(const struct [device](structdevice.md) \*dev,

185 struct [k\_poll\_signal](structk__poll__signal.md) \*[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69),

186 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) vector)

187{

188 const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*api =

189 (const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

190

191 return api->register\_handler(dev, [signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69), vector);

192}

193

194#ifdef CONFIG\_IVSHMEM\_V2

195

204\_\_syscall size\_t ivshmem\_get\_rw\_mem\_section(const struct [device](structdevice.md) \*dev,

205 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*memmap);

206

207static inline size\_t z\_impl\_ivshmem\_get\_rw\_mem\_section(const struct [device](structdevice.md) \*dev,

208 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*memmap)

209{

210 const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*api =

211 (const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

212

213 return api->get\_rw\_mem\_section(dev, memmap);

214}

215

225\_\_syscall size\_t ivshmem\_get\_output\_mem\_section(const struct [device](structdevice.md) \*dev,

226 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peer\_id,

227 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*memmap);

228

229static inline size\_t z\_impl\_ivshmem\_get\_output\_mem\_section(const struct [device](structdevice.md) \*dev,

230 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peer\_id,

231 [uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808) \*memmap)

232{

233 const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*api =

234 (const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

235

236 return api->get\_output\_mem\_section(dev, peer\_id, memmap);

237}

238

247\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ivshmem\_get\_state(const struct [device](structdevice.md) \*dev,

248 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peer\_id);

249

250static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_ivshmem\_get\_state(const struct [device](structdevice.md) \*dev,

251 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) peer\_id)

252{

253 const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*api =

254 (const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

255

256 return api->get\_state(dev, peer\_id);

257}

258

267\_\_syscall int ivshmem\_set\_state(const struct [device](structdevice.md) \*dev,

268 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

269

270static inline int z\_impl\_ivshmem\_set\_state(const struct [device](structdevice.md) \*dev,

271 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90))

272{

273 const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*api =

274 (const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

275

276 return api->set\_state(dev, [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90));

277}

278

286\_\_syscall [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ivshmem\_get\_max\_peers(const struct [device](structdevice.md) \*dev);

287

288static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) z\_impl\_ivshmem\_get\_max\_peers(const struct [device](structdevice.md) \*dev)

289{

290 const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*api =

291 (const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

292

293 return api->get\_max\_peers(dev);

294}

295

303\_\_syscall [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ivshmem\_get\_protocol(const struct [device](structdevice.md) \*dev);

304

305static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) z\_impl\_ivshmem\_get\_protocol(const struct [device](structdevice.md) \*dev)

306{

307 const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*api =

308 (const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

309

310 return api->get\_protocol(dev);

311}

312

321\_\_syscall int ivshmem\_enable\_interrupts(const struct [device](structdevice.md) \*dev,

322 bool enable);

323

324static inline int z\_impl\_ivshmem\_enable\_interrupts(const struct [device](structdevice.md) \*dev,

325 bool enable)

326{

327 const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*api =

328 (const struct [ivshmem\_driver\_api](structivshmem__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

329

330 return api->enable\_interrupts(dev, enable);

331}

332

333#endif /\* CONFIG\_IVSHMEM\_V2 \*/

334

335#ifdef \_\_cplusplus

336}

337#endif

338

342

343#include <zephyr/syscalls/ivshmem.h>

344

345#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_VIRTUALIZATION\_IVSHMEM\_H\_ \*/

[device.h](device_8h.md)

[ivshmem\_int\_peer\_f](group__ivshmem.md#ga1af6d005fac141c84716b18705219bfd)

int(\* ivshmem\_int\_peer\_f)(const struct device \*dev, uint32\_t peer\_id, uint16\_t vector)

**Definition** ivshmem.h:36

[ivshmem\_get\_vectors\_f](group__ivshmem.md#ga7e25f5db9ac889a2ff05694f60f66e39)

uint16\_t(\* ivshmem\_get\_vectors\_f)(const struct device \*dev)

**Definition** ivshmem.h:34

[ivshmem\_register\_handler\_f](group__ivshmem.md#ga842bee3ff990f166665593c384c6bb21)

int(\* ivshmem\_register\_handler\_f)(const struct device \*dev, struct k\_poll\_signal \*signal, uint16\_t vector)

**Definition** ivshmem.h:39

[ivshmem\_register\_handler](group__ivshmem.md#ga88aacb71bff0375c10fdb48e34b359fe)

int ivshmem\_register\_handler(const struct device \*dev, struct k\_poll\_signal \*signal, uint16\_t vector)

Register a vector notification (interrupt) handler.

[ivshmem\_get\_id\_f](group__ivshmem.md#ga8a6f4c145426f8a28c0f3a52875b7ea1)

uint32\_t(\* ivshmem\_get\_id\_f)(const struct device \*dev)

**Definition** ivshmem.h:32

[ivshmem\_get\_id](group__ivshmem.md#gab2f0ccd5a2b8203a54ee5707b3afd6cc)

uint32\_t ivshmem\_get\_id(const struct device \*dev)

Get our VM ID.

[ivshmem\_int\_peer](group__ivshmem.md#gab4e02271f8b854c783c359aca240d20c)

int ivshmem\_int\_peer(const struct device \*dev, uint32\_t peer\_id, uint16\_t vector)

Interrupt another VM.

[ivshmem\_get\_mem](group__ivshmem.md#gaef043cbfbe0aa5061db57f9bbae02eca)

size\_t ivshmem\_get\_mem(const struct device \*dev, uintptr\_t \*memmap)

Get the inter-VM shared memory.

[ivshmem\_get\_mem\_f](group__ivshmem.md#gaf8f761888728090ab6adb11f3b700057)

size\_t(\* ivshmem\_get\_mem\_f)(const struct device \*dev, uintptr\_t \*memmap)

**Definition** ivshmem.h:29

[ivshmem\_get\_vectors](group__ivshmem.md#gafee360f2c35abb9a203dd9f4838b8846)

uint16\_t ivshmem\_get\_vectors(const struct device \*dev)

Get the number of interrupt vectors we can use.

[signal](include_2zephyr_2posix_2signal_8h.md#ad9d7c8d68836c635e8ec915507f49b69)

sighandler\_t signal(int signo, sighandler\_t handler)

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9)

Size of off\_t must be equal or less than size of size\_t

**Definition** retained\_mem.h:28

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uintptr\_t](stdint_8h.md#a4788399d1d0b37ccf098a7da82254808)

\_\_UINTPTR\_TYPE\_\_ uintptr\_t

**Definition** stdint.h:105

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:459

[ivshmem\_driver\_api](structivshmem__driver__api.md)

**Definition** ivshmem.h:67

[ivshmem\_driver\_api::register\_handler](structivshmem__driver__api.md#a083b127047c28175c250fa0af9080ec8)

ivshmem\_register\_handler\_f register\_handler

**Definition** ivshmem.h:72

[ivshmem\_driver\_api::get\_id](structivshmem__driver__api.md#a9b689bd1d35adb9f806a16bba14d6810)

ivshmem\_get\_id\_f get\_id

**Definition** ivshmem.h:69

[ivshmem\_driver\_api::int\_peer](structivshmem__driver__api.md#aa10ef98079775f56b4763f31c2e6654d)

ivshmem\_int\_peer\_f int\_peer

**Definition** ivshmem.h:71

[ivshmem\_driver\_api::get\_vectors](structivshmem__driver__api.md#ab302c92b722d88c281fd57a26389f58b)

ivshmem\_get\_vectors\_f get\_vectors

**Definition** ivshmem.h:70

[ivshmem\_driver\_api::get\_mem](structivshmem__driver__api.md#afd4fc50b7cdf91ab1ed56193799d0e47)

ivshmem\_get\_mem\_f get\_mem

**Definition** ivshmem.h:68

[k\_poll\_signal](structk__poll__signal.md)

**Definition** kernel.h:5964

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [virtualization](dir_9d22dc9b22b8050a5a1558ed6b8fdf63.md)
- [ivshmem.h](ivshmem_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
