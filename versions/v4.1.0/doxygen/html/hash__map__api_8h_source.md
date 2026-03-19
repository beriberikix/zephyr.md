---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/hash__map__api_8h_source.html
original_path: doxygen/html/hash__map__api_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hash\_map\_api.h

[Go to the documentation of this file.](hash__map__api_8h.md)

1/\*

2 \* Copyright (c) 2022 Meta

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_SYS\_HASHMAP\_API\_H\_

8#define ZEPHYR\_INCLUDE\_SYS\_HASHMAP\_API\_H\_

9

10#include <[stdbool.h](stdbool_8h.md)>

11#include <stddef.h>

12#include <[stdint.h](stdint_8h.md)>

13

14#include <[zephyr/sys/hash\_function.h](hash__function_8h.md)>

15#include <[zephyr/sys/util.h](sys_2util_8h.md)>

16

17#ifdef \_\_cplusplus

18extern "C" {

19#endif

20

37

[ 44](structsys__hashmap__iterator.md)struct [sys\_hashmap\_iterator](structsys__hashmap__iterator.md) {

[ 46](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c) const struct [sys\_hashmap](structsys__hashmap.md) \*[map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c);

[ 48](structsys__hashmap__iterator.md#a8c79527ba05d0dcfe2f13e0fe387efa4) void (\*[next](structsys__hashmap__iterator.md#a8c79527ba05d0dcfe2f13e0fe387efa4))(struct [sys\_hashmap\_iterator](structsys__hashmap__iterator.md) \*it);

[ 50](structsys__hashmap__iterator.md#a19938b219d6b249721968cce1abece9e) void \*[state](structsys__hashmap__iterator.md#a19938b219d6b249721968cce1abece9e);

[ 52](structsys__hashmap__iterator.md#a47684d01a30deca036f58b98b845e958) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [key](structsys__hashmap__iterator.md#a47684d01a30deca036f58b98b845e958);

[ 54](structsys__hashmap__iterator.md#a9987d100e22822f07182278cbb431b24) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [value](structsys__hashmap__iterator.md#a9987d100e22822f07182278cbb431b24);

[ 56](structsys__hashmap__iterator.md#a4145137c2d1c95a7658902287cea2096) const size\_t [size](structsys__hashmap__iterator.md#a4145137c2d1c95a7658902287cea2096);

[ 58](structsys__hashmap__iterator.md#a0bc36e419dcb98e120342be0dba1604d) size\_t [pos](structsys__hashmap__iterator.md#a0bc36e419dcb98e120342be0dba1604d);

59};

60

[ 68](group__hashmap__apis.md#ga15020630e76f826893c58faded3737ed)static inline bool [sys\_hashmap\_iterator\_has\_next](group__hashmap__apis.md#ga15020630e76f826893c58faded3737ed)(const struct [sys\_hashmap\_iterator](structsys__hashmap__iterator.md) \*it)

69{

70 return it->[pos](structsys__hashmap__iterator.md#a0bc36e419dcb98e120342be0dba1604d) < it->[size](structsys__hashmap__iterator.md#a4145137c2d1c95a7658902287cea2096);

71}

72

[ 84](group__hashmap__apis.md#ga813a4f65e3672651ef37c06dccdcfebc)typedef void \*(\*sys\_hashmap\_allocator\_t)(void \*ptr, size\_t new\_size);

85

[ 94](group__hashmap__apis.md#gaffc18fa6c36de71c94a836dff30f4dba)typedef void (\*[sys\_hashmap\_iterator\_t](group__hashmap__apis.md#gaffc18fa6c36de71c94a836dff30f4dba))(const struct [sys\_hashmap](structsys__hashmap.md) \*map,

95 struct [sys\_hashmap\_iterator](structsys__hashmap__iterator.md) \*it);

96

[ 106](group__hashmap__apis.md#ga6e813ebb133febdcac0bd2e6b552a0d1)typedef void (\*[sys\_hashmap\_callback\_t](group__hashmap__apis.md#ga6e813ebb133febdcac0bd2e6b552a0d1))([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [key](structsys__hashmap__iterator.md#a47684d01a30deca036f58b98b845e958), [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) [value](structsys__hashmap__iterator.md#a9987d100e22822f07182278cbb431b24), void \*cookie);

107

[ 117](group__hashmap__apis.md#gac5c7ec25ad44115e83cda666d8175c79)typedef void (\*[sys\_hashmap\_clear\_t](group__hashmap__apis.md#gac5c7ec25ad44115e83cda666d8175c79))(struct [sys\_hashmap](structsys__hashmap.md) \*map, [sys\_hashmap\_callback\_t](group__hashmap__apis.md#ga6e813ebb133febdcac0bd2e6b552a0d1) cb,

118 void \*cookie);

119

[ 134](group__hashmap__apis.md#gacbd944beac0fd5377a19c662f444b50b)typedef int (\*[sys\_hashmap\_insert\_t](group__hashmap__apis.md#gacbd944beac0fd5377a19c662f444b50b))(struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value,

135 [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*old\_value);

136

[ 149](group__hashmap__apis.md#ga8ee3886c08a1e0635db3a43858f76055)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[sys\_hashmap\_remove\_t](group__hashmap__apis.md#ga8ee3886c08a1e0635db3a43858f76055))(struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value);

150

[ 163](group__hashmap__apis.md#gab24ce66e67e900d24c6fe3dde10a6cac)typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[sys\_hashmap\_get\_t](group__hashmap__apis.md#gab24ce66e67e900d24c6fe3dde10a6cac))(const struct [sys\_hashmap](structsys__hashmap.md) \*map, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) key, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value);

164

[ 168](structsys__hashmap__api.md)struct [sys\_hashmap\_api](structsys__hashmap__api.md) {

[ 170](structsys__hashmap__api.md#a1487c726730c010f286609d5cc77a109) [sys\_hashmap\_iterator\_t](group__hashmap__apis.md#gaffc18fa6c36de71c94a836dff30f4dba) [iter](structsys__hashmap__api.md#a1487c726730c010f286609d5cc77a109);

[ 172](structsys__hashmap__api.md#a7b39c2920e8a65d7c4e01912a3ea4136) [sys\_hashmap\_clear\_t](group__hashmap__apis.md#gac5c7ec25ad44115e83cda666d8175c79) [clear](structsys__hashmap__api.md#a7b39c2920e8a65d7c4e01912a3ea4136);

[ 174](structsys__hashmap__api.md#acdf4df23107858b3a1d891b3ce437dad) [sys\_hashmap\_insert\_t](group__hashmap__apis.md#gacbd944beac0fd5377a19c662f444b50b) [insert](structsys__hashmap__api.md#acdf4df23107858b3a1d891b3ce437dad);

[ 176](structsys__hashmap__api.md#a20443bacc5669e724ac74573539f0fb7) [sys\_hashmap\_remove\_t](group__hashmap__apis.md#ga8ee3886c08a1e0635db3a43858f76055) [remove](structsys__hashmap__api.md#a20443bacc5669e724ac74573539f0fb7);

[ 178](structsys__hashmap__api.md#af014aabea50f5b0568316104986de41d) [sys\_hashmap\_get\_t](group__hashmap__apis.md#gab24ce66e67e900d24c6fe3dde10a6cac) [get](structsys__hashmap__api.md#af014aabea50f5b0568316104986de41d);

179};

180

[ 197](structsys__hashmap__config.md)struct [sys\_hashmap\_config](structsys__hashmap__config.md) {

[ 199](structsys__hashmap__config.md#a5ee7a97a936d1b9b97e0669561cc0689) size\_t [max\_size](structsys__hashmap__config.md#a5ee7a97a936d1b9b97e0669561cc0689);

[ 201](structsys__hashmap__config.md#a5a8683d82932ae397b92722269385baa) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [load\_factor](structsys__hashmap__config.md#a5a8683d82932ae397b92722269385baa);

[ 203](structsys__hashmap__config.md#a0a9911024bfc4c55f4a1fc179eaa6e10) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [initial\_n\_buckets](structsys__hashmap__config.md#a0a9911024bfc4c55f4a1fc179eaa6e10);

204};

205

[ 214](group__hashmap__apis.md#ga9cabdd6d7577372220065db79983f006)#define SYS\_HASHMAP\_CONFIG(\_max\_size, \_load\_factor) \

215 { \

216 .max\_size = (size\_t)\_max\_size, .load\_factor = (uint8\_t)\_load\_factor, \

217 .initial\_n\_buckets = NHPOT(DIV\_ROUND\_UP(100, \_load\_factor)), \

218 }

219

[ 225](structsys__hashmap__data.md)struct [sys\_hashmap\_data](structsys__hashmap__data.md) {

[ 227](structsys__hashmap__data.md#ad6f00cc9bfa4e654a3bdcd5c8803f326) void \*[buckets](structsys__hashmap__data.md#ad6f00cc9bfa4e654a3bdcd5c8803f326);

[ 229](structsys__hashmap__data.md#a79892de2c54612860f0dd48bce88aeea) size\_t [n\_buckets](structsys__hashmap__data.md#a79892de2c54612860f0dd48bce88aeea);

[ 231](structsys__hashmap__data.md#ac453e2dc52f989617feebedc6eeb2929) size\_t [size](structsys__hashmap__data.md#ac453e2dc52f989617feebedc6eeb2929);

232};

233

235

236#ifdef \_\_cplusplus

237}

238#endif

239

240#endif /\* ZEPHYR\_INCLUDE\_SYS\_HASHMAP\_API\_H\_ \*/

[sys\_hashmap\_iterator\_has\_next](group__hashmap__apis.md#ga15020630e76f826893c58faded3737ed)

static bool sys\_hashmap\_iterator\_has\_next(const struct sys\_hashmap\_iterator \*it)

Check if a Hashmap iterator has a next entry.

**Definition** hash\_map\_api.h:68

[sys\_hashmap\_callback\_t](group__hashmap__apis.md#ga6e813ebb133febdcac0bd2e6b552a0d1)

void(\* sys\_hashmap\_callback\_t)(uint64\_t key, uint64\_t value, void \*cookie)

Callback interface for sys\_hashmap.

**Definition** hash\_map\_api.h:106

[sys\_hashmap\_remove\_t](group__hashmap__apis.md#ga8ee3886c08a1e0635db3a43858f76055)

bool(\* sys\_hashmap\_remove\_t)(struct sys\_hashmap \*map, uint64\_t key, uint64\_t \*value)

Remove an entry from a sys\_hashmap.

**Definition** hash\_map\_api.h:149

[sys\_hashmap\_get\_t](group__hashmap__apis.md#gab24ce66e67e900d24c6fe3dde10a6cac)

bool(\* sys\_hashmap\_get\_t)(const struct sys\_hashmap \*map, uint64\_t key, uint64\_t \*value)

Get a value from a sys\_hashmap.

**Definition** hash\_map\_api.h:163

[sys\_hashmap\_clear\_t](group__hashmap__apis.md#gac5c7ec25ad44115e83cda666d8175c79)

void(\* sys\_hashmap\_clear\_t)(struct sys\_hashmap \*map, sys\_hashmap\_callback\_t cb, void \*cookie)

Clear all entries contained in a sys\_hashmap.

**Definition** hash\_map\_api.h:117

[sys\_hashmap\_insert\_t](group__hashmap__apis.md#gacbd944beac0fd5377a19c662f444b50b)

int(\* sys\_hashmap\_insert\_t)(struct sys\_hashmap \*map, uint64\_t key, uint64\_t value, uint64\_t \*old\_value)

Insert a new entry into a sys\_hashmap.

**Definition** hash\_map\_api.h:134

[sys\_hashmap\_iterator\_t](group__hashmap__apis.md#gaffc18fa6c36de71c94a836dff30f4dba)

void(\* sys\_hashmap\_iterator\_t)(const struct sys\_hashmap \*map, struct sys\_hashmap\_iterator \*it)

In-place iterator constructor for sys\_hashmap.

**Definition** hash\_map\_api.h:94

[hash\_function.h](hash__function_8h.md)

[stdbool.h](stdbool_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[stdint.h](stdint_8h.md)

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[sys\_hashmap\_api](structsys__hashmap__api.md)

Generic Hashmap API.

**Definition** hash\_map\_api.h:168

[sys\_hashmap\_api::iter](structsys__hashmap__api.md#a1487c726730c010f286609d5cc77a109)

sys\_hashmap\_iterator\_t iter

Iterator constructor (in-place).

**Definition** hash\_map\_api.h:170

[sys\_hashmap\_api::remove](structsys__hashmap__api.md#a20443bacc5669e724ac74573539f0fb7)

sys\_hashmap\_remove\_t remove

Remove a key-value pair from the Hashmap.

**Definition** hash\_map\_api.h:176

[sys\_hashmap\_api::clear](structsys__hashmap__api.md#a7b39c2920e8a65d7c4e01912a3ea4136)

sys\_hashmap\_clear\_t clear

Clear the hash table, freeing all resources.

**Definition** hash\_map\_api.h:172

[sys\_hashmap\_api::insert](structsys__hashmap__api.md#acdf4df23107858b3a1d891b3ce437dad)

sys\_hashmap\_insert\_t insert

Insert a key-value pair into the Hashmap.

**Definition** hash\_map\_api.h:174

[sys\_hashmap\_api::get](structsys__hashmap__api.md#af014aabea50f5b0568316104986de41d)

sys\_hashmap\_get\_t get

Retrieve the value associated with a given key from the Hashmap.

**Definition** hash\_map\_api.h:178

[sys\_hashmap\_config](structsys__hashmap__config.md)

Generic Hashmap configuration.

**Definition** hash\_map\_api.h:197

[sys\_hashmap\_config::initial\_n\_buckets](structsys__hashmap__config.md#a0a9911024bfc4c55f4a1fc179eaa6e10)

uint8\_t initial\_n\_buckets

Initial number of buckets to allocate.

**Definition** hash\_map\_api.h:203

[sys\_hashmap\_config::load\_factor](structsys__hashmap__config.md#a5a8683d82932ae397b92722269385baa)

uint8\_t load\_factor

Maximum load factor expressed in hundredths.

**Definition** hash\_map\_api.h:201

[sys\_hashmap\_config::max\_size](structsys__hashmap__config.md#a5ee7a97a936d1b9b97e0669561cc0689)

size\_t max\_size

Maximum number of entries.

**Definition** hash\_map\_api.h:199

[sys\_hashmap\_data](structsys__hashmap__data.md)

Generic Hashmap data.

**Definition** hash\_map\_api.h:225

[sys\_hashmap\_data::n\_buckets](structsys__hashmap__data.md#a79892de2c54612860f0dd48bce88aeea)

size\_t n\_buckets

The number of buckets currently allocated.

**Definition** hash\_map\_api.h:229

[sys\_hashmap\_data::size](structsys__hashmap__data.md#ac453e2dc52f989617feebedc6eeb2929)

size\_t size

The number of entries currently in the Hashmap.

**Definition** hash\_map\_api.h:231

[sys\_hashmap\_data::buckets](structsys__hashmap__data.md#ad6f00cc9bfa4e654a3bdcd5c8803f326)

void \* buckets

Pointer for implementation-specific Hashmap storage.

**Definition** hash\_map\_api.h:227

[sys\_hashmap\_iterator](structsys__hashmap__iterator.md)

Generic Hashmap iterator interface.

**Definition** hash\_map\_api.h:44

[sys\_hashmap\_iterator::pos](structsys__hashmap__iterator.md#a0bc36e419dcb98e120342be0dba1604d)

size\_t pos

Number of entries already iterated.

**Definition** hash\_map\_api.h:58

[sys\_hashmap\_iterator::map](structsys__hashmap__iterator.md#a0e868afd37b06566caff62be0fd4290c)

const struct sys\_hashmap \* map

Pointer to the associated Hashmap.

**Definition** hash\_map\_api.h:46

[sys\_hashmap\_iterator::state](structsys__hashmap__iterator.md#a19938b219d6b249721968cce1abece9e)

void \* state

Implementation-specific iterator state.

**Definition** hash\_map\_api.h:50

[sys\_hashmap\_iterator::size](structsys__hashmap__iterator.md#a4145137c2d1c95a7658902287cea2096)

const size\_t size

Number of entries in the map.

**Definition** hash\_map\_api.h:56

[sys\_hashmap\_iterator::key](structsys__hashmap__iterator.md#a47684d01a30deca036f58b98b845e958)

uint64\_t key

Key associated with the current entry.

**Definition** hash\_map\_api.h:52

[sys\_hashmap\_iterator::next](structsys__hashmap__iterator.md#a8c79527ba05d0dcfe2f13e0fe387efa4)

void(\* next)(struct sys\_hashmap\_iterator \*it)

Modify the iterator in-place to point to the next Hashmap entry.

**Definition** hash\_map\_api.h:48

[sys\_hashmap\_iterator::value](structsys__hashmap__iterator.md#a9987d100e22822f07182278cbb431b24)

uint64\_t value

Value associated with the current entry.

**Definition** hash\_map\_api.h:54

[sys\_hashmap](structsys__hashmap.md)

Generic Hashmap.

**Definition** hash\_map.h:125

[util.h](sys_2util_8h.md)

Misc utilities.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [hash\_map\_api.h](hash__map__api_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
