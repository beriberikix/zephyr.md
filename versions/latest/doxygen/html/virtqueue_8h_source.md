---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/virtqueue_8h_source.html
original_path: doxygen/html/virtqueue_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

virtqueue.h

[Go to the documentation of this file.](virtqueue_8h.md)

1/\*

2 \* Copyright (c) 2024 Antmicro <www.antmicro.com>

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_VIRTIO\_VIRTQUEUE\_H\_

8#define ZEPHYR\_VIRTIO\_VIRTQUEUE\_H\_

9#include <[stdint.h](stdint_8h.md)>

10#include <stddef.h>

11#include <[zephyr/kernel.h](kernel_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

17/\*

18 \* Based on Virtual I/O Device (VIRTIO) Version 1.3 specification:

19 \* https://docs.oasis-open.org/virtio/virtio/v1.3/csd01/virtio-v1.3-csd01.pdf

20 \*/

21

28

[ 32](group__virtqueue__interface.md#ga20e010fee3553a39ff6af7a5cc2837c2)#define VIRTQ\_DESC\_F\_NEXT 1

[ 36](group__virtqueue__interface.md#ga208ab0e95f24325454621095b80fcf27)#define VIRTQ\_DESC\_F\_WRITE 2

37

[ 43](structvirtq__desc.md)struct [virtq\_desc](structvirtq__desc.md) {

[ 47](structvirtq__desc.md#a1d5146808360ff5e359673c193fe4d53) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [addr](structvirtq__desc.md#a1d5146808360ff5e359673c193fe4d53);

[ 51](structvirtq__desc.md#a1dcd1400d72aa7b628920258e226a7ce) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [len](structvirtq__desc.md#a1dcd1400d72aa7b628920258e226a7ce);

[ 55](structvirtq__desc.md#a9731d25acdd201e07e4362f79fb5ba9e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structvirtq__desc.md#a9731d25acdd201e07e4362f79fb5ba9e);

[ 59](structvirtq__desc.md#a2703fcd4eb5bf97530687444203e8ee6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [next](structvirtq__desc.md#a2703fcd4eb5bf97530687444203e8ee6);

60};

61

[ 67](structvirtq__avail.md)struct [virtq\_avail](structvirtq__avail.md) {

[ 71](structvirtq__avail.md#ab013600ebaa7a4c855112599755ce607) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structvirtq__avail.md#ab013600ebaa7a4c855112599755ce607);

[ 75](structvirtq__avail.md#a70caebae8d3a86d05cb718c5e0a9f88d) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [idx](structvirtq__avail.md#a70caebae8d3a86d05cb718c5e0a9f88d);

[ 79](structvirtq__avail.md#a03f0bc25a3459316bd166f3cbf9a66c3) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [ring](structvirtq__avail.md#a03f0bc25a3459316bd166f3cbf9a66c3)[];

80};

81

[ 87](structvirtq__used__elem.md)struct [virtq\_used\_elem](structvirtq__used__elem.md) {

[ 91](structvirtq__used__elem.md#a7f1f8b4bc3590a00e85bed3657a9fbdc) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [id](structvirtq__used__elem.md#a7f1f8b4bc3590a00e85bed3657a9fbdc);

[ 95](structvirtq__used__elem.md#ad61ce7642ec40dba74c2f8ffd28ba8ed) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [len](structvirtq__used__elem.md#ad61ce7642ec40dba74c2f8ffd28ba8ed);

96};

97

[ 103](structvirtq__used.md)struct [virtq\_used](structvirtq__used.md) {

[ 107](structvirtq__used.md#a77e64d4bc15ae058515aa96987794f90) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [flags](structvirtq__used.md#a77e64d4bc15ae058515aa96987794f90);

[ 111](structvirtq__used.md#ad3e466c8aee5efcfef250e907717e656) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [idx](structvirtq__used.md#ad3e466c8aee5efcfef250e907717e656);

[ 115](structvirtq__used.md#a36575313c28554dda228a32ed58156e8) struct [virtq\_used\_elem](structvirtq__used__elem.md) [ring](structvirtq__used.md#a36575313c28554dda228a32ed58156e8)[];

116};

117

[ 124](group__virtqueue__interface.md#ga311909fbebf3cb96ace6c751fabcf708)typedef void (\*[virtq\_receive\_callback](group__virtqueue__interface.md#ga311909fbebf3cb96ace6c751fabcf708))(void \*opaque, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) used\_len);

125

[ 132](structvirtq__receive__callback__entry.md)struct [virtq\_receive\_callback\_entry](structvirtq__receive__callback__entry.md) {

[ 136](structvirtq__receive__callback__entry.md#ae892b29ffebb17cba4154e342278908d) [virtq\_receive\_callback](group__virtqueue__interface.md#ga311909fbebf3cb96ace6c751fabcf708) [cb](structvirtq__receive__callback__entry.md#ae892b29ffebb17cba4154e342278908d);

[ 140](structvirtq__receive__callback__entry.md#adc164ebec52cd00cc15839b1cda4be56) void \*[opaque](structvirtq__receive__callback__entry.md#adc164ebec52cd00cc15839b1cda4be56);

141};

142

[ 148](structvirtq.md)struct [virtq](structvirtq.md) {

[ 152](structvirtq.md#aa4a4101177743201210ec1267df31b57) struct [k\_spinlock](structk__spinlock.md) [lock](structvirtq.md#aa4a4101177743201210ec1267df31b57);

153

[ 157](structvirtq.md#afeb3f726fe78a18574d7ddd77a1837f9) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [num](structvirtq.md#afeb3f726fe78a18574d7ddd77a1837f9);

[ 161](structvirtq.md#aa299da6b7d7b4ede53423d17d3973a92) struct [virtq\_desc](structvirtq__desc.md) \*[desc](structvirtq.md#aa299da6b7d7b4ede53423d17d3973a92);

[ 165](structvirtq.md#a872b79dd002eb3adf0f680c252323346) struct [virtq\_avail](structvirtq__avail.md) \*[avail](structvirtq.md#a872b79dd002eb3adf0f680c252323346);

[ 169](structvirtq.md#a7f12283618d0acc418d378a8d554215d) struct [virtq\_used](structvirtq__used.md) \*[used](structvirtq.md#a7f12283618d0acc418d378a8d554215d);

170

[ 175](structvirtq.md#a811241bbc1032b299f303c96e45e39c8) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [last\_used\_idx](structvirtq.md#a811241bbc1032b299f303c96e45e39c8);

[ 183](structvirtq.md#a441e32c89c78d6b432469957cb38db25) struct k\_stack [free\_desc\_stack](structvirtq.md#a441e32c89c78d6b432469957cb38db25);

184

[ 188](structvirtq.md#a540cc380e0e9ec5fc92cf1ea7f3252fe) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [free\_desc\_n](structvirtq.md#a540cc380e0e9ec5fc92cf1ea7f3252fe);

189

[ 193](structvirtq.md#a2cd048d18e1f8f30a197f33f24f53575) struct [virtq\_receive\_callback\_entry](structvirtq__receive__callback__entry.md) \*[recv\_cbs](structvirtq.md#a2cd048d18e1f8f30a197f33f24f53575);

194};

195

196

[ 204](group__virtqueue__interface.md#ga3dce3b5099fc117a94da63a24571b6c3)int [virtq\_create](group__virtqueue__interface.md#ga3dce3b5099fc117a94da63a24571b6c3)(struct [virtq](structvirtq.md) \*v, size\_t size);

205

[ 211](group__virtqueue__interface.md#ga9443eb15529fa16d1024a70075daca28)void [virtq\_free](group__virtqueue__interface.md#ga9443eb15529fa16d1024a70075daca28)(struct [virtq](structvirtq.md) \*v);

212

[ 216](structvirtq__buf.md)struct [virtq\_buf](structvirtq__buf.md) {

[ 220](structvirtq__buf.md#ad05060db8d467017fca4af593bab9417) void \*[addr](structvirtq__buf.md#ad05060db8d467017fca4af593bab9417);

[ 224](structvirtq__buf.md#aaa047b4296f5c104d5a8f5eaf48aaaac) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [len](structvirtq__buf.md#aaa047b4296f5c104d5a8f5eaf48aaaac);

225};

226

[ 245](group__virtqueue__interface.md#ga5e01b141e28aec876c298047f8d623a6)int [virtq\_add\_buffer\_chain](group__virtqueue__interface.md#ga5e01b141e28aec876c298047f8d623a6)(

246 struct [virtq](structvirtq.md) \*v, struct [virtq\_buf](structvirtq__buf.md) \*bufs, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bufs\_size,

247 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) device\_readable\_count, [virtq\_receive\_callback](group__virtqueue__interface.md#ga311909fbebf3cb96ace6c751fabcf708) cb, void \*cb\_opaque,

248 [k\_timeout\_t](structk__timeout__t.md) timeout

249);

250

[ 257](group__virtqueue__interface.md#ga55abe7b8204cf0b57cd1c2380dcd66fb)void [virtq\_add\_free\_desc](group__virtqueue__interface.md#ga55abe7b8204cf0b57cd1c2380dcd66fb)(struct [virtq](structvirtq.md) \*v, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) desc\_idx);

258

[ 268](group__virtqueue__interface.md#ga79b1b54f0ea6fe8b5110712488f663eb)int [virtq\_get\_free\_desc](group__virtqueue__interface.md#ga79b1b54f0ea6fe8b5110712488f663eb)(struct [virtq](structvirtq.md) \*v, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*desc\_idx, [k\_timeout\_t](structk__timeout__t.md) timeout);

269

273

274#ifdef \_\_cplusplus

275}

276#endif

277

278#endif /\* ZEPHYR\_VIRTIO\_VIRTQUEUE\_H\_ \*/

[virtq\_receive\_callback](group__virtqueue__interface.md#ga311909fbebf3cb96ace6c751fabcf708)

void(\* virtq\_receive\_callback)(void \*opaque, uint32\_t used\_len)

receive callback function type

**Definition** virtqueue.h:124

[virtq\_create](group__virtqueue__interface.md#ga3dce3b5099fc117a94da63a24571b6c3)

int virtq\_create(struct virtq \*v, size\_t size)

creates virtqueue

[virtq\_add\_free\_desc](group__virtqueue__interface.md#ga55abe7b8204cf0b57cd1c2380dcd66fb)

void virtq\_add\_free\_desc(struct virtq \*v, uint16\_t desc\_idx)

adds free descriptor back

[virtq\_add\_buffer\_chain](group__virtqueue__interface.md#ga5e01b141e28aec876c298047f8d623a6)

int virtq\_add\_buffer\_chain(struct virtq \*v, struct virtq\_buf \*bufs, uint16\_t bufs\_size, uint16\_t device\_readable\_count, virtq\_receive\_callback cb, void \*cb\_opaque, k\_timeout\_t timeout)

adds chain of buffers to the virtqueue

[virtq\_get\_free\_desc](group__virtqueue__interface.md#ga79b1b54f0ea6fe8b5110712488f663eb)

int virtq\_get\_free\_desc(struct virtq \*v, uint16\_t \*desc\_idx, k\_timeout\_t timeout)

gets next free descriptor

[virtq\_free](group__virtqueue__interface.md#ga9443eb15529fa16d1024a70075daca28)

void virtq\_free(struct virtq \*v)

frees virtqueue

[kernel.h](kernel_8h.md)

Public kernel APIs.

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[k\_spinlock](structk__spinlock.md)

Kernel Spin Lock.

**Definition** spinlock.h:45

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** clock.h:65

[virtq\_avail](structvirtq__avail.md)

virtqueue available ring

**Definition** virtqueue.h:67

[virtq\_avail::ring](structvirtq__avail.md#a03f0bc25a3459316bd166f3cbf9a66c3)

uint16\_t ring[]

ring with indexes of descriptors

**Definition** virtqueue.h:79

[virtq\_avail::idx](structvirtq__avail.md#a70caebae8d3a86d05cb718c5e0a9f88d)

uint16\_t idx

head of the ring, by increasing it newly added descriptors are committed

**Definition** virtqueue.h:75

[virtq\_avail::flags](structvirtq__avail.md#ab013600ebaa7a4c855112599755ce607)

uint16\_t flags

ring flags, e.g.

**Definition** virtqueue.h:71

[virtq\_buf](structvirtq__buf.md)

single buffer passed to virtq\_add\_buffer\_chain

**Definition** virtqueue.h:216

[virtq\_buf::len](structvirtq__buf.md#aaa047b4296f5c104d5a8f5eaf48aaaac)

uint32\_t len

length of the buffer

**Definition** virtqueue.h:224

[virtq\_buf::addr](structvirtq__buf.md#ad05060db8d467017fca4af593bab9417)

void \* addr

virtual address of the buffer

**Definition** virtqueue.h:220

[virtq\_desc](structvirtq__desc.md)

virtqueue descriptor

**Definition** virtqueue.h:43

[virtq\_desc::addr](structvirtq__desc.md#a1d5146808360ff5e359673c193fe4d53)

uint64\_t addr

physical address of the buffer

**Definition** virtqueue.h:47

[virtq\_desc::len](structvirtq__desc.md#a1dcd1400d72aa7b628920258e226a7ce)

uint32\_t len

length of the buffer

**Definition** virtqueue.h:51

[virtq\_desc::next](structvirtq__desc.md#a2703fcd4eb5bf97530687444203e8ee6)

uint16\_t next

chaining next descriptor, valid if flags & VIRTQ\_DESC\_F\_NEXT

**Definition** virtqueue.h:59

[virtq\_desc::flags](structvirtq__desc.md#a9731d25acdd201e07e4362f79fb5ba9e)

uint16\_t flags

buffer flags

**Definition** virtqueue.h:55

[virtq\_receive\_callback\_entry](structvirtq__receive__callback__entry.md)

callback descriptor

**Definition** virtqueue.h:132

[virtq\_receive\_callback\_entry::opaque](structvirtq__receive__callback__entry.md#adc164ebec52cd00cc15839b1cda4be56)

void \* opaque

argument passed to the callback function

**Definition** virtqueue.h:140

[virtq\_receive\_callback\_entry::cb](structvirtq__receive__callback__entry.md#ae892b29ffebb17cba4154e342278908d)

virtq\_receive\_callback cb

callback function pointer

**Definition** virtqueue.h:136

[virtq\_used\_elem](structvirtq__used__elem.md)

used descriptor chain

**Definition** virtqueue.h:87

[virtq\_used\_elem::id](structvirtq__used__elem.md#a7f1f8b4bc3590a00e85bed3657a9fbdc)

uint32\_t id

index of the head of descriptor chain

**Definition** virtqueue.h:91

[virtq\_used\_elem::len](structvirtq__used__elem.md#ad61ce7642ec40dba74c2f8ffd28ba8ed)

uint32\_t len

total amount of bytes written to descriptor chain by the virtio device

**Definition** virtqueue.h:95

[virtq\_used](structvirtq__used.md)

virtqueue used ring

**Definition** virtqueue.h:103

[virtq\_used::ring](structvirtq__used.md#a36575313c28554dda228a32ed58156e8)

struct virtq\_used\_elem ring[]

ring of struct virtq\_used\_elem

**Definition** virtqueue.h:115

[virtq\_used::flags](structvirtq__used.md#a77e64d4bc15ae058515aa96987794f90)

uint16\_t flags

ring flags, e.g.

**Definition** virtqueue.h:107

[virtq\_used::idx](structvirtq__used.md#ad3e466c8aee5efcfef250e907717e656)

uint16\_t idx

head of the ring

**Definition** virtqueue.h:111

[virtq](structvirtq.md)

virtqueue

**Definition** virtqueue.h:148

[virtq::recv\_cbs](structvirtq.md#a2cd048d18e1f8f30a197f33f24f53575)

struct virtq\_receive\_callback\_entry \* recv\_cbs

array with callbacks invoked after receiving buffers back from the device

**Definition** virtqueue.h:193

[virtq::free\_desc\_stack](structvirtq.md#a441e32c89c78d6b432469957cb38db25)

struct k\_stack free\_desc\_stack

Stack containing indexes of free descriptors.

**Definition** virtqueue.h:183

[virtq::free\_desc\_n](structvirtq.md#a540cc380e0e9ec5fc92cf1ea7f3252fe)

uint16\_t free\_desc\_n

amount of free descriptors in the free\_desc\_stack

**Definition** virtqueue.h:188

[virtq::used](structvirtq.md#a7f12283618d0acc418d378a8d554215d)

struct virtq\_used \* used

used ring

**Definition** virtqueue.h:169

[virtq::last\_used\_idx](structvirtq.md#a811241bbc1032b299f303c96e45e39c8)

uint16\_t last\_used\_idx

last seen idx in used ring, used to determine first descriptor to process after receiving virtqueue i...

**Definition** virtqueue.h:175

[virtq::avail](structvirtq.md#a872b79dd002eb3adf0f680c252323346)

struct virtq\_avail \* avail

available ring

**Definition** virtqueue.h:165

[virtq::desc](structvirtq.md#aa299da6b7d7b4ede53423d17d3973a92)

struct virtq\_desc \* desc

array with descriptors

**Definition** virtqueue.h:161

[virtq::lock](structvirtq.md#aa4a4101177743201210ec1267df31b57)

struct k\_spinlock lock

lock used to synchronize operations on virtqueue

**Definition** virtqueue.h:152

[virtq::num](structvirtq.md#afeb3f726fe78a18574d7ddd77a1837f9)

uint16\_t num

size of virtqueue

**Definition** virtqueue.h:157

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [virtio](dir_219496648d5efa24b2239bdfe387791d.md)
- [virtqueue.h](virtqueue_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
