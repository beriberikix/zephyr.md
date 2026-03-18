---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/cdb_8h_source.html
original_path: doxygen/html/cdb_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cdb.h

[Go to the documentation of this file.](cdb_8h.md)

1/\*

2 \* Copyright (c) 2019 Tobias Svehagen

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_CDB\_H\_

7#define ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_CDB\_H\_

8

9#include <[stdbool.h](stdbool_8h.md)>

10#include <[stdint.h](stdint_8h.md)>

11

12#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

13#include <[zephyr/bluetooth/mesh.h](mesh_8h.md)>

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

19#if defined(CONFIG\_BT\_MESH\_CDB)

20#define NODE\_COUNT CONFIG\_BT\_MESH\_CDB\_NODE\_COUNT

21#define SUBNET\_COUNT CONFIG\_BT\_MESH\_CDB\_SUBNET\_COUNT

22#define APP\_KEY\_COUNT CONFIG\_BT\_MESH\_CDB\_APP\_KEY\_COUNT

23#else

[ 24](cdb_8h.md#ae49e5e1ae89eef30538ae9f45c772b64)#define NODE\_COUNT 0

[ 25](cdb_8h.md#a5ab07a907049974c089a4b0dd706ef77)#define SUBNET\_COUNT 0

[ 26](cdb_8h.md#aab65f293c17c657d670e802bbfe389d7)#define APP\_KEY\_COUNT 0

27#endif

28

29enum {

[ 30](cdb_8h.md#a159f4eec3bbcaed25a4369b67e6937f1aab4ca02f1d0d9f6a743bee9f66eeba12) [BT\_MESH\_CDB\_NODE\_CONFIGURED](cdb_8h.md#a159f4eec3bbcaed25a4369b67e6937f1aab4ca02f1d0d9f6a743bee9f66eeba12),

31

[ 32](cdb_8h.md#a159f4eec3bbcaed25a4369b67e6937f1a00449c6d1403f903b115c3de36a2a3bd) [BT\_MESH\_CDB\_NODE\_FLAG\_COUNT](cdb_8h.md#a159f4eec3bbcaed25a4369b67e6937f1a00449c6d1403f903b115c3de36a2a3bd)

33};

34

[ 35](structbt__mesh__cdb__node.md)struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) {

[ 36](structbt__mesh__cdb__node.md#a751671f52c4fdf3f42b6f71193976dd5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uuid](structbt__mesh__cdb__node.md#a751671f52c4fdf3f42b6f71193976dd5)[16];

[ 37](structbt__mesh__cdb__node.md#a8c9941929a8ce6228817d76fe4e2375c) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structbt__mesh__cdb__node.md#a8c9941929a8ce6228817d76fe4e2375c);

[ 38](structbt__mesh__cdb__node.md#aa936534676ef7e256670d356eff7ac17) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx](structbt__mesh__cdb__node.md#aa936534676ef7e256670d356eff7ac17);

[ 39](structbt__mesh__cdb__node.md#a2313e29b756344a493989f39ba1ec726) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_elem](structbt__mesh__cdb__node.md#a2313e29b756344a493989f39ba1ec726);

[ 40](structbt__mesh__cdb__node.md#a54e5130d7dabedf09e23419a40f6778b) struct bt\_mesh\_key [dev\_key](structbt__mesh__cdb__node.md#a54e5130d7dabedf09e23419a40f6778b);

41

[ 42](structbt__mesh__cdb__node.md#a3c7e6369501f577ede53a4071e257956) [ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)([flags](structbt__mesh__cdb__node.md#a3c7e6369501f577ede53a4071e257956), [BT\_MESH\_CDB\_NODE\_FLAG\_COUNT](cdb_8h.md#a159f4eec3bbcaed25a4369b67e6937f1a00449c6d1403f903b115c3de36a2a3bd));

43};

44

[ 45](structbt__mesh__cdb__subnet.md)struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) {

[ 46](structbt__mesh__cdb__subnet.md#a1010965e2030e1bef181920fc5f76116) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx](structbt__mesh__cdb__subnet.md#a1010965e2030e1bef181920fc5f76116);

47

[ 48](structbt__mesh__cdb__subnet.md#a07fbd0e52571cd9a16e876243483e98a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [kr\_phase](structbt__mesh__cdb__subnet.md#a07fbd0e52571cd9a16e876243483e98a);

49

50 struct {

[ 51](structbt__mesh__cdb__subnet.md#a40d47a7705f4d3a9ba9349972d11072a) struct bt\_mesh\_key [net\_key](structbt__mesh__cdb__subnet.md#a40d47a7705f4d3a9ba9349972d11072a);

[ 52](structbt__mesh__cdb__subnet.md#a2f04c34ebbb8ae1e33f6679f94690c9a) } [keys](structbt__mesh__cdb__subnet.md#a2f04c34ebbb8ae1e33f6679f94690c9a)[2];

53};

54

[ 55](structbt__mesh__cdb__app__key.md)struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) {

[ 56](structbt__mesh__cdb__app__key.md#afa234a0d5f0fb61513a97afb91986976) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx](structbt__mesh__cdb__app__key.md#afa234a0d5f0fb61513a97afb91986976);

[ 57](structbt__mesh__cdb__app__key.md#a2ef7f5d832b36736d3a1811a407b6fa6) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [app\_idx](structbt__mesh__cdb__app__key.md#a2ef7f5d832b36736d3a1811a407b6fa6);

58

59 struct {

[ 60](structbt__mesh__cdb__app__key.md#a2d685a7dd5e1f4678c34ea72be3fe6a2) struct bt\_mesh\_key [app\_key](structbt__mesh__cdb__app__key.md#a2d685a7dd5e1f4678c34ea72be3fe6a2);

[ 61](structbt__mesh__cdb__app__key.md#aa113eaa2a648cdabe21dc2c57b31bf65) } [keys](structbt__mesh__cdb__app__key.md#aa113eaa2a648cdabe21dc2c57b31bf65)[2];

62};

63

64enum {

[ 65](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5ad5a2fc5c15efc200ef31b8876eabc01d) [BT\_MESH\_CDB\_VALID](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5ad5a2fc5c15efc200ef31b8876eabc01d),

[ 66](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5a5d07a0f33a2544be141d1fb4c6130bdd) [BT\_MESH\_CDB\_SUBNET\_PENDING](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5a5d07a0f33a2544be141d1fb4c6130bdd),

[ 67](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5a62fc7baf49a7bf92a3b3c80eb57d8cf8) [BT\_MESH\_CDB\_KEYS\_PENDING](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5a62fc7baf49a7bf92a3b3c80eb57d8cf8),

[ 68](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5a3fe59a5bb698f65be4389345fe63ccc1) [BT\_MESH\_CDB\_NODES\_PENDING](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5a3fe59a5bb698f65be4389345fe63ccc1),

[ 69](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5a229d9bfcc277ea2cb81e991a1a30ceb6) [BT\_MESH\_CDB\_IVU\_IN\_PROGRESS](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5a229d9bfcc277ea2cb81e991a1a30ceb6),

70

[ 71](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5abf303893a5d3b399856b3670c4a7fd41) [BT\_MESH\_CDB\_FLAG\_COUNT](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5abf303893a5d3b399856b3670c4a7fd41),

72};

73

[ 74](structbt__mesh__cdb.md)struct [bt\_mesh\_cdb](structbt__mesh__cdb.md) {

[ 75](structbt__mesh__cdb.md#a48b3cf852a42b580f911e193a9764517) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [iv\_index](structbt__mesh__cdb.md#a48b3cf852a42b580f911e193a9764517);

[ 76](structbt__mesh__cdb.md#acb7f3ae85a5929b9cfc18531e1d98ab5) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [lowest\_avail\_addr](structbt__mesh__cdb.md#acb7f3ae85a5929b9cfc18531e1d98ab5);

77

[ 78](structbt__mesh__cdb.md#a24e2334468e9be08a435f4854af195f4) [ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)([flags](structbt__mesh__cdb.md#a24e2334468e9be08a435f4854af195f4), [BT\_MESH\_CDB\_FLAG\_COUNT](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5abf303893a5d3b399856b3670c4a7fd41));

79

[ 80](structbt__mesh__cdb.md#a7af2ac65c8919c594b8283ff57b5b7fc) struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) [nodes](structbt__mesh__cdb.md#a7af2ac65c8919c594b8283ff57b5b7fc)[[NODE\_COUNT](cdb_8h.md#ae49e5e1ae89eef30538ae9f45c772b64)];

[ 81](structbt__mesh__cdb.md#ae391c898d11257c484c4e8d1b38fd9dc) struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) [subnets](structbt__mesh__cdb.md#ae391c898d11257c484c4e8d1b38fd9dc)[[SUBNET\_COUNT](cdb_8h.md#a5ab07a907049974c089a4b0dd706ef77)];

[ 82](structbt__mesh__cdb.md#a59a130ffed26c362dc72d57d1ac7d7fd) struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) [app\_keys](structbt__mesh__cdb.md#a59a130ffed26c362dc72d57d1ac7d7fd)[[APP\_KEY\_COUNT](cdb_8h.md#aab65f293c17c657d670e802bbfe389d7)];

83};

84

85extern struct [bt\_mesh\_cdb](structbt__mesh__cdb.md) [bt\_mesh\_cdb](structbt__mesh__cdb.md);

86

[ 97](cdb_8h.md#a00490e69b96e88cdf7336ca22e63617d)int [bt\_mesh\_cdb\_create](cdb_8h.md#a00490e69b96e88cdf7336ca22e63617d)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) key[16]);

98

[ 105](cdb_8h.md#a4bf4f49fbd75ee33876ffd34f6c6f76f)void [bt\_mesh\_cdb\_clear](cdb_8h.md#a4bf4f49fbd75ee33876ffd34f6c6f76f)(void);

106

[ 118](cdb_8h.md#aa6d124339002c43fc35f301a9eef3e7c)void [bt\_mesh\_cdb\_iv\_update](cdb_8h.md#aa6d124339002c43fc35f301a9eef3e7c)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [iv\_index](structbt__mesh__cdb.md#a48b3cf852a42b580f911e193a9764517), bool iv\_update);

119

[ 138](cdb_8h.md#ab0dc86dd674f57a820aa3f5cebf77895)struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \*[bt\_mesh\_cdb\_node\_alloc](cdb_8h.md#ab0dc86dd674f57a820aa3f5cebf77895)(const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [uuid](structbt__mesh__cdb__node.md#a751671f52c4fdf3f42b6f71193976dd5)[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structbt__mesh__cdb__node.md#a8c9941929a8ce6228817d76fe4e2375c),

139 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_elem](structbt__mesh__cdb__node.md#a2313e29b756344a493989f39ba1ec726), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx](structbt__mesh__cdb__node.md#aa936534676ef7e256670d356eff7ac17));

140

[ 148](cdb_8h.md#aa10c4ec973e61626ba6424e443fb0b88)[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [bt\_mesh\_cdb\_free\_addr\_get](cdb_8h.md#aa10c4ec973e61626ba6424e443fb0b88)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_elem](structbt__mesh__cdb__node.md#a2313e29b756344a493989f39ba1ec726));

149

[ 161](cdb_8h.md#a6d9cc2d360075b6b3e939a4979e08895)void [bt\_mesh\_cdb\_node\_del](cdb_8h.md#a6d9cc2d360075b6b3e939a4979e08895)(struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \*node, bool store);

162

[ 172](cdb_8h.md#ad4333e02b866589f7ca2b155cf814ca4)void [bt\_mesh\_cdb\_node\_update](cdb_8h.md#ad4333e02b866589f7ca2b155cf814ca4)(struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \*node, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structbt__mesh__cdb__node.md#a8c9941929a8ce6228817d76fe4e2375c),

173 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [num\_elem](structbt__mesh__cdb__node.md#a2313e29b756344a493989f39ba1ec726));

174

[ 185](cdb_8h.md#a3d0034ec500d3964dd4b428e518abfb9)struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \*[bt\_mesh\_cdb\_node\_get](cdb_8h.md#a3d0034ec500d3964dd4b428e518abfb9)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [addr](structbt__mesh__cdb__node.md#a8c9941929a8ce6228817d76fe4e2375c));

186

[ 191](cdb_8h.md#ac775f3d1be745aeba2979b9ae4b42c4f)void [bt\_mesh\_cdb\_node\_store](cdb_8h.md#ac775f3d1be745aeba2979b9ae4b42c4f)(const struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \*node);

192

[ 204](cdb_8h.md#a26b1e5560998cc37e2a627c44326db62)int [bt\_mesh\_cdb\_node\_key\_import](cdb_8h.md#a26b1e5560998cc37e2a627c44326db62)(struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \*node, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) in[16]);

205

[ 217](cdb_8h.md#a4a0f7577f1a8df96e4dcab6f682abf23)int [bt\_mesh\_cdb\_node\_key\_export](cdb_8h.md#a4a0f7577f1a8df96e4dcab6f682abf23)(const struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \*node, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) out[16]);

218

219enum {

[ 220](cdb_8h.md#a2ec5612f827a95662f18bc9e012048cdaf2362ea16e4733a32e26138a3577e5fb) [BT\_MESH\_CDB\_ITER\_STOP](cdb_8h.md#a2ec5612f827a95662f18bc9e012048cdaf2362ea16e4733a32e26138a3577e5fb) = 0,

[ 221](cdb_8h.md#a2ec5612f827a95662f18bc9e012048cda6b057da4bd763f7c65e41410b7c72218) [BT\_MESH\_CDB\_ITER\_CONTINUE](cdb_8h.md#a2ec5612f827a95662f18bc9e012048cda6b057da4bd763f7c65e41410b7c72218),

222};

223

[ 233](cdb_8h.md#a5d00af9f4c971f31c3016824757ebf66)typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) (\*[bt\_mesh\_cdb\_node\_func\_t](cdb_8h.md#a5d00af9f4c971f31c3016824757ebf66))(struct [bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md) \*node,

234 void \*user\_data);

235

[ 244](cdb_8h.md#ae8ed0ef1a00e973d864c944c9d9400bc)void [bt\_mesh\_cdb\_node\_foreach](cdb_8h.md#ae8ed0ef1a00e973d864c944c9d9400bc)([bt\_mesh\_cdb\_node\_func\_t](cdb_8h.md#a5d00af9f4c971f31c3016824757ebf66) func, void \*user\_data);

245

[ 255](cdb_8h.md#aeba4ed506e30ab8d91746b36e7e5f968)struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \*[bt\_mesh\_cdb\_subnet\_alloc](cdb_8h.md#aeba4ed506e30ab8d91746b36e7e5f968)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx](structbt__mesh__cdb__subnet.md#a1010965e2030e1bef181920fc5f76116));

256

[ 264](cdb_8h.md#a66df2f6b6363af595181fe722122996d)void [bt\_mesh\_cdb\_subnet\_del](cdb_8h.md#a66df2f6b6363af595181fe722122996d)(struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \*sub, bool store);

265

[ 275](cdb_8h.md#a34dcf031e675235cdcbe0e1f76c00cf3)struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \*[bt\_mesh\_cdb\_subnet\_get](cdb_8h.md#a34dcf031e675235cdcbe0e1f76c00cf3)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx](structbt__mesh__cdb__subnet.md#a1010965e2030e1bef181920fc5f76116));

276

[ 281](cdb_8h.md#a59e6b7da8c91df35ce6f8268da35c933)void [bt\_mesh\_cdb\_subnet\_store](cdb_8h.md#a59e6b7da8c91df35ce6f8268da35c933)(const struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \*sub);

282

[ 289](cdb_8h.md#a121a30fd546ccb887c2c49ceef65c2d6)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_mesh\_cdb\_subnet\_flags](cdb_8h.md#a121a30fd546ccb887c2c49ceef65c2d6)(const struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \*sub);

290

[ 305](cdb_8h.md#aba737b508e0e40dfb5ad9da9d7b6fd11)int [bt\_mesh\_cdb\_subnet\_key\_import](cdb_8h.md#aba737b508e0e40dfb5ad9da9d7b6fd11)(struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \*sub, int key\_idx,

306 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) in[16]);

307

[ 322](cdb_8h.md#ac361a17a704195e852faecda09881203)int [bt\_mesh\_cdb\_subnet\_key\_export](cdb_8h.md#ac361a17a704195e852faecda09881203)(const struct [bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md) \*sub, int key\_idx,

323 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) out[16]);

324

[ 335](cdb_8h.md#ab82dcdf26d66ea4ab0df34bc23421f39)struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) \*[bt\_mesh\_cdb\_app\_key\_alloc](cdb_8h.md#ab82dcdf26d66ea4ab0df34bc23421f39)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [net\_idx](structbt__mesh__cdb__app__key.md#afa234a0d5f0fb61513a97afb91986976),

336 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [app\_idx](structbt__mesh__cdb__app__key.md#a2ef7f5d832b36736d3a1811a407b6fa6));

337

[ 345](cdb_8h.md#a692c6980c9b0d2da18e8f47d67757f07)void [bt\_mesh\_cdb\_app\_key\_del](cdb_8h.md#a692c6980c9b0d2da18e8f47d67757f07)(struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) \*key, bool store);

346

[ 356](cdb_8h.md#ab728a20fdb1535cc7059a39e8490a736)struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) \*[bt\_mesh\_cdb\_app\_key\_get](cdb_8h.md#ab728a20fdb1535cc7059a39e8490a736)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [app\_idx](structbt__mesh__cdb__app__key.md#a2ef7f5d832b36736d3a1811a407b6fa6));

357

[ 362](cdb_8h.md#a4e9470adfa797be85b7f4df43b63d6d2)void [bt\_mesh\_cdb\_app\_key\_store](cdb_8h.md#a4e9470adfa797be85b7f4df43b63d6d2)(const struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) \*key);

363

[ 378](cdb_8h.md#a9ad0651ccaa7ff1f86402ce8c05c9410)int [bt\_mesh\_cdb\_app\_key\_import](cdb_8h.md#a9ad0651ccaa7ff1f86402ce8c05c9410)(struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) \*key, int key\_idx, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) in[16]);

379

[ 394](cdb_8h.md#a87cfce7316efabe4c8b24be6c3b6d8b4)int [bt\_mesh\_cdb\_app\_key\_export](cdb_8h.md#a87cfce7316efabe4c8b24be6c3b6d8b4)(const struct [bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md) \*key, int key\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) out[16]);

395

396#ifdef \_\_cplusplus

397}

398#endif

399

400#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_MESH\_CDB\_H\_ \*/

[bt\_mesh\_cdb\_create](cdb_8h.md#a00490e69b96e88cdf7336ca22e63617d)

int bt\_mesh\_cdb\_create(const uint8\_t key[16])

Create the Mesh Configuration Database.

[BT\_MESH\_CDB\_IVU\_IN\_PROGRESS](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5a229d9bfcc277ea2cb81e991a1a30ceb6)

@ BT\_MESH\_CDB\_IVU\_IN\_PROGRESS

**Definition** cdb.h:69

[BT\_MESH\_CDB\_NODES\_PENDING](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5a3fe59a5bb698f65be4389345fe63ccc1)

@ BT\_MESH\_CDB\_NODES\_PENDING

**Definition** cdb.h:68

[BT\_MESH\_CDB\_SUBNET\_PENDING](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5a5d07a0f33a2544be141d1fb4c6130bdd)

@ BT\_MESH\_CDB\_SUBNET\_PENDING

**Definition** cdb.h:66

[BT\_MESH\_CDB\_KEYS\_PENDING](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5a62fc7baf49a7bf92a3b3c80eb57d8cf8)

@ BT\_MESH\_CDB\_KEYS\_PENDING

**Definition** cdb.h:67

[BT\_MESH\_CDB\_FLAG\_COUNT](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5abf303893a5d3b399856b3670c4a7fd41)

@ BT\_MESH\_CDB\_FLAG\_COUNT

**Definition** cdb.h:71

[BT\_MESH\_CDB\_VALID](cdb_8h.md#a0e45ffdd001e9fac31b74949a004e8f5ad5a2fc5c15efc200ef31b8876eabc01d)

@ BT\_MESH\_CDB\_VALID

**Definition** cdb.h:65

[bt\_mesh\_cdb\_subnet\_flags](cdb_8h.md#a121a30fd546ccb887c2c49ceef65c2d6)

uint8\_t bt\_mesh\_cdb\_subnet\_flags(const struct bt\_mesh\_cdb\_subnet \*sub)

Get the flags for a subnet.

[BT\_MESH\_CDB\_NODE\_FLAG\_COUNT](cdb_8h.md#a159f4eec3bbcaed25a4369b67e6937f1a00449c6d1403f903b115c3de36a2a3bd)

@ BT\_MESH\_CDB\_NODE\_FLAG\_COUNT

**Definition** cdb.h:32

[BT\_MESH\_CDB\_NODE\_CONFIGURED](cdb_8h.md#a159f4eec3bbcaed25a4369b67e6937f1aab4ca02f1d0d9f6a743bee9f66eeba12)

@ BT\_MESH\_CDB\_NODE\_CONFIGURED

**Definition** cdb.h:30

[bt\_mesh\_cdb\_node\_key\_import](cdb_8h.md#a26b1e5560998cc37e2a627c44326db62)

int bt\_mesh\_cdb\_node\_key\_import(struct bt\_mesh\_cdb\_node \*node, const uint8\_t in[16])

Import device key for selected node.

[BT\_MESH\_CDB\_ITER\_CONTINUE](cdb_8h.md#a2ec5612f827a95662f18bc9e012048cda6b057da4bd763f7c65e41410b7c72218)

@ BT\_MESH\_CDB\_ITER\_CONTINUE

**Definition** cdb.h:221

[BT\_MESH\_CDB\_ITER\_STOP](cdb_8h.md#a2ec5612f827a95662f18bc9e012048cdaf2362ea16e4733a32e26138a3577e5fb)

@ BT\_MESH\_CDB\_ITER\_STOP

**Definition** cdb.h:220

[bt\_mesh\_cdb\_subnet\_get](cdb_8h.md#a34dcf031e675235cdcbe0e1f76c00cf3)

struct bt\_mesh\_cdb\_subnet \* bt\_mesh\_cdb\_subnet\_get(uint16\_t net\_idx)

Get a subnet by NetIdx.

[bt\_mesh\_cdb\_node\_get](cdb_8h.md#a3d0034ec500d3964dd4b428e518abfb9)

struct bt\_mesh\_cdb\_node \* bt\_mesh\_cdb\_node\_get(uint16\_t addr)

Get a node by address.

[bt\_mesh\_cdb\_node\_key\_export](cdb_8h.md#a4a0f7577f1a8df96e4dcab6f682abf23)

int bt\_mesh\_cdb\_node\_key\_export(const struct bt\_mesh\_cdb\_node \*node, uint8\_t out[16])

Export device key from selected node.

[bt\_mesh\_cdb\_clear](cdb_8h.md#a4bf4f49fbd75ee33876ffd34f6c6f76f)

void bt\_mesh\_cdb\_clear(void)

Clear the Mesh Configuration Database.

[bt\_mesh\_cdb\_app\_key\_store](cdb_8h.md#a4e9470adfa797be85b7f4df43b63d6d2)

void bt\_mesh\_cdb\_app\_key\_store(const struct bt\_mesh\_cdb\_app\_key \*key)

Store application key to persistent storage.

[bt\_mesh\_cdb\_subnet\_store](cdb_8h.md#a59e6b7da8c91df35ce6f8268da35c933)

void bt\_mesh\_cdb\_subnet\_store(const struct bt\_mesh\_cdb\_subnet \*sub)

Store subnet to persistent storage.

[SUBNET\_COUNT](cdb_8h.md#a5ab07a907049974c089a4b0dd706ef77)

#define SUBNET\_COUNT

**Definition** cdb.h:25

[bt\_mesh\_cdb\_node\_func\_t](cdb_8h.md#a5d00af9f4c971f31c3016824757ebf66)

uint8\_t(\* bt\_mesh\_cdb\_node\_func\_t)(struct bt\_mesh\_cdb\_node \*node, void \*user\_data)

Node iterator callback.

**Definition** cdb.h:233

[bt\_mesh\_cdb\_subnet\_del](cdb_8h.md#a66df2f6b6363af595181fe722122996d)

void bt\_mesh\_cdb\_subnet\_del(struct bt\_mesh\_cdb\_subnet \*sub, bool store)

Delete a subnet.

[bt\_mesh\_cdb\_app\_key\_del](cdb_8h.md#a692c6980c9b0d2da18e8f47d67757f07)

void bt\_mesh\_cdb\_app\_key\_del(struct bt\_mesh\_cdb\_app\_key \*key, bool store)

Delete an application key.

[bt\_mesh\_cdb\_node\_del](cdb_8h.md#a6d9cc2d360075b6b3e939a4979e08895)

void bt\_mesh\_cdb\_node\_del(struct bt\_mesh\_cdb\_node \*node, bool store)

Delete a node.

[bt\_mesh\_cdb\_app\_key\_export](cdb_8h.md#a87cfce7316efabe4c8b24be6c3b6d8b4)

int bt\_mesh\_cdb\_app\_key\_export(const struct bt\_mesh\_cdb\_app\_key \*key, int key\_idx, uint8\_t out[16])

Export application key.

[bt\_mesh\_cdb\_app\_key\_import](cdb_8h.md#a9ad0651ccaa7ff1f86402ce8c05c9410)

int bt\_mesh\_cdb\_app\_key\_import(struct bt\_mesh\_cdb\_app\_key \*key, int key\_idx, const uint8\_t in[16])

Import application key.

[bt\_mesh\_cdb\_free\_addr\_get](cdb_8h.md#aa10c4ec973e61626ba6424e443fb0b88)

uint16\_t bt\_mesh\_cdb\_free\_addr\_get(uint8\_t num\_elem)

Get the first available address for the given element count.

[bt\_mesh\_cdb\_iv\_update](cdb_8h.md#aa6d124339002c43fc35f301a9eef3e7c)

void bt\_mesh\_cdb\_iv\_update(uint32\_t iv\_index, bool iv\_update)

Set and store the IV Index and IV Update flag.

[APP\_KEY\_COUNT](cdb_8h.md#aab65f293c17c657d670e802bbfe389d7)

#define APP\_KEY\_COUNT

**Definition** cdb.h:26

[bt\_mesh\_cdb\_node\_alloc](cdb_8h.md#ab0dc86dd674f57a820aa3f5cebf77895)

struct bt\_mesh\_cdb\_node \* bt\_mesh\_cdb\_node\_alloc(const uint8\_t uuid[16], uint16\_t addr, uint8\_t num\_elem, uint16\_t net\_idx)

Allocate a node.

[bt\_mesh\_cdb\_app\_key\_get](cdb_8h.md#ab728a20fdb1535cc7059a39e8490a736)

struct bt\_mesh\_cdb\_app\_key \* bt\_mesh\_cdb\_app\_key\_get(uint16\_t app\_idx)

Get an application key by AppIdx.

[bt\_mesh\_cdb\_app\_key\_alloc](cdb_8h.md#ab82dcdf26d66ea4ab0df34bc23421f39)

struct bt\_mesh\_cdb\_app\_key \* bt\_mesh\_cdb\_app\_key\_alloc(uint16\_t net\_idx, uint16\_t app\_idx)

Allocate an application key.

[bt\_mesh\_cdb\_subnet\_key\_import](cdb_8h.md#aba737b508e0e40dfb5ad9da9d7b6fd11)

int bt\_mesh\_cdb\_subnet\_key\_import(struct bt\_mesh\_cdb\_subnet \*sub, int key\_idx, const uint8\_t in[16])

Import network key for selected subnetwork.

[bt\_mesh\_cdb\_subnet\_key\_export](cdb_8h.md#ac361a17a704195e852faecda09881203)

int bt\_mesh\_cdb\_subnet\_key\_export(const struct bt\_mesh\_cdb\_subnet \*sub, int key\_idx, uint8\_t out[16])

Export network key from selected subnetwork.

[bt\_mesh\_cdb\_node\_store](cdb_8h.md#ac775f3d1be745aeba2979b9ae4b42c4f)

void bt\_mesh\_cdb\_node\_store(const struct bt\_mesh\_cdb\_node \*node)

Store node to persistent storage.

[bt\_mesh\_cdb\_node\_update](cdb_8h.md#ad4333e02b866589f7ca2b155cf814ca4)

void bt\_mesh\_cdb\_node\_update(struct bt\_mesh\_cdb\_node \*node, uint16\_t addr, uint8\_t num\_elem)

Update a node.

[NODE\_COUNT](cdb_8h.md#ae49e5e1ae89eef30538ae9f45c772b64)

#define NODE\_COUNT

**Definition** cdb.h:24

[bt\_mesh\_cdb\_node\_foreach](cdb_8h.md#ae8ed0ef1a00e973d864c944c9d9400bc)

void bt\_mesh\_cdb\_node\_foreach(bt\_mesh\_cdb\_node\_func\_t func, void \*user\_data)

Node iterator.

[bt\_mesh\_cdb\_subnet\_alloc](cdb_8h.md#aeba4ed506e30ab8d91746b36e7e5f968)

struct bt\_mesh\_cdb\_subnet \* bt\_mesh\_cdb\_subnet\_alloc(uint16\_t net\_idx)

Allocate a subnet.

[ATOMIC\_DEFINE](group__atomic__apis.md#ga249c575db9764486197709b327f7370e)

#define ATOMIC\_DEFINE(name, num\_bits)

Define an array of atomic variables.

**Definition** atomic.h:111

[mesh.h](mesh_8h.md)

Bluetooth Mesh Profile APIs.

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_mesh\_cdb\_app\_key](structbt__mesh__cdb__app__key.md)

**Definition** cdb.h:55

[bt\_mesh\_cdb\_app\_key::app\_key](structbt__mesh__cdb__app__key.md#a2d685a7dd5e1f4678c34ea72be3fe6a2)

struct bt\_mesh\_key app\_key

**Definition** cdb.h:60

[bt\_mesh\_cdb\_app\_key::app\_idx](structbt__mesh__cdb__app__key.md#a2ef7f5d832b36736d3a1811a407b6fa6)

uint16\_t app\_idx

**Definition** cdb.h:57

[bt\_mesh\_cdb\_app\_key::keys](structbt__mesh__cdb__app__key.md#aa113eaa2a648cdabe21dc2c57b31bf65)

struct bt\_mesh\_cdb\_app\_key::@274230372255300310212360360030147162313105141144 keys[2]

[bt\_mesh\_cdb\_app\_key::net\_idx](structbt__mesh__cdb__app__key.md#afa234a0d5f0fb61513a97afb91986976)

uint16\_t net\_idx

**Definition** cdb.h:56

[bt\_mesh\_cdb\_node](structbt__mesh__cdb__node.md)

**Definition** cdb.h:35

[bt\_mesh\_cdb\_node::num\_elem](structbt__mesh__cdb__node.md#a2313e29b756344a493989f39ba1ec726)

uint8\_t num\_elem

**Definition** cdb.h:39

[bt\_mesh\_cdb\_node::flags](structbt__mesh__cdb__node.md#a3c7e6369501f577ede53a4071e257956)

atomic\_t flags[ATOMIC\_BITMAP\_SIZE(BT\_MESH\_CDB\_NODE\_FLAG\_COUNT)]

**Definition** cdb.h:42

[bt\_mesh\_cdb\_node::dev\_key](structbt__mesh__cdb__node.md#a54e5130d7dabedf09e23419a40f6778b)

struct bt\_mesh\_key dev\_key

**Definition** cdb.h:40

[bt\_mesh\_cdb\_node::uuid](structbt__mesh__cdb__node.md#a751671f52c4fdf3f42b6f71193976dd5)

uint8\_t uuid[16]

**Definition** cdb.h:36

[bt\_mesh\_cdb\_node::addr](structbt__mesh__cdb__node.md#a8c9941929a8ce6228817d76fe4e2375c)

uint16\_t addr

**Definition** cdb.h:37

[bt\_mesh\_cdb\_node::net\_idx](structbt__mesh__cdb__node.md#aa936534676ef7e256670d356eff7ac17)

uint16\_t net\_idx

**Definition** cdb.h:38

[bt\_mesh\_cdb\_subnet](structbt__mesh__cdb__subnet.md)

**Definition** cdb.h:45

[bt\_mesh\_cdb\_subnet::kr\_phase](structbt__mesh__cdb__subnet.md#a07fbd0e52571cd9a16e876243483e98a)

uint8\_t kr\_phase

**Definition** cdb.h:48

[bt\_mesh\_cdb\_subnet::net\_idx](structbt__mesh__cdb__subnet.md#a1010965e2030e1bef181920fc5f76116)

uint16\_t net\_idx

**Definition** cdb.h:46

[bt\_mesh\_cdb\_subnet::keys](structbt__mesh__cdb__subnet.md#a2f04c34ebbb8ae1e33f6679f94690c9a)

struct bt\_mesh\_cdb\_subnet::@255320146034363322047346143277156274244242036001 keys[2]

[bt\_mesh\_cdb\_subnet::net\_key](structbt__mesh__cdb__subnet.md#a40d47a7705f4d3a9ba9349972d11072a)

struct bt\_mesh\_key net\_key

**Definition** cdb.h:51

[bt\_mesh\_cdb](structbt__mesh__cdb.md)

**Definition** cdb.h:74

[bt\_mesh\_cdb::flags](structbt__mesh__cdb.md#a24e2334468e9be08a435f4854af195f4)

atomic\_t flags[ATOMIC\_BITMAP\_SIZE(BT\_MESH\_CDB\_FLAG\_COUNT)]

**Definition** cdb.h:78

[bt\_mesh\_cdb::iv\_index](structbt__mesh__cdb.md#a48b3cf852a42b580f911e193a9764517)

uint32\_t iv\_index

**Definition** cdb.h:75

[bt\_mesh\_cdb::app\_keys](structbt__mesh__cdb.md#a59a130ffed26c362dc72d57d1ac7d7fd)

struct bt\_mesh\_cdb\_app\_key app\_keys[0]

**Definition** cdb.h:82

[bt\_mesh\_cdb::nodes](structbt__mesh__cdb.md#a7af2ac65c8919c594b8283ff57b5b7fc)

struct bt\_mesh\_cdb\_node nodes[0]

**Definition** cdb.h:80

[bt\_mesh\_cdb::lowest\_avail\_addr](structbt__mesh__cdb.md#acb7f3ae85a5929b9cfc18531e1d98ab5)

uint16\_t lowest\_avail\_addr

**Definition** cdb.h:76

[bt\_mesh\_cdb::subnets](structbt__mesh__cdb.md#ae391c898d11257c484c4e8d1b38fd9dc)

struct bt\_mesh\_cdb\_subnet subnets[0]

**Definition** cdb.h:81

[atomic.h](sys_2atomic_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [cdb.h](cdb_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
