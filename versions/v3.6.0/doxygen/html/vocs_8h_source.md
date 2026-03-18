---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/vocs_8h_source.html
original_path: doxygen/html/vocs_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

vocs.h

[Go to the documentation of this file.](vocs_8h.md)

1/\*

2 \* Copyright (c) 2020 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_VOCS\_H\_

8#define ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_VOCS\_H\_

9

28

29#include <[stdint.h](stdint_8h.md)>

30#include <[stdbool.h](stdbool_8h.md)>

31

32#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

33

34#ifdef \_\_cplusplus

35extern "C" {

36#endif

37

[ 39](group__bt__gatt__vocs.md#ga17c81394b9b4d601768e72d8c360992f)#define BT\_VOCS\_ERR\_INVALID\_COUNTER 0x80

[ 40](group__bt__gatt__vocs.md#gadd01a04e3c4336a13a4760e2448131b1)#define BT\_VOCS\_ERR\_OP\_NOT\_SUPPORTED 0x81

[ 41](group__bt__gatt__vocs.md#ga2ecb7e0408bb1767c2d51c816f4b273d)#define BT\_VOCS\_ERR\_OUT\_OF\_RANGE 0x82

42

[ 43](group__bt__gatt__vocs.md#ga64d4e32f9d92a58b3229b3aa2e8fcc4d)#define BT\_VOCS\_MIN\_OFFSET -255

[ 44](group__bt__gatt__vocs.md#ga800092562173fd37826b5537feaac3ae)#define BT\_VOCS\_MAX\_OFFSET 255

45

47struct bt\_vocs;

48

[ 50](structbt__vocs__register__param.md)struct [bt\_vocs\_register\_param](structbt__vocs__register__param.md) {

[ 52](structbt__vocs__register__param.md#a0572c60319c8984e2437e596584c46f5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [location](structbt__vocs__register__param.md#a0572c60319c8984e2437e596584c46f5);

53

[ 55](structbt__vocs__register__param.md#a6919f965abfa1fec39a3c8e0f29c04f3) bool [location\_writable](structbt__vocs__register__param.md#a6919f965abfa1fec39a3c8e0f29c04f3);

56

[ 58](structbt__vocs__register__param.md#ac1c2475cd390f5acf840f92ea45c6d31) [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) [offset](structbt__vocs__register__param.md#ac1c2475cd390f5acf840f92ea45c6d31);

59

[ 61](structbt__vocs__register__param.md#a1f6baed09dc35b974d06f1426b671e05) char \*[output\_desc](structbt__vocs__register__param.md#a1f6baed09dc35b974d06f1426b671e05);

62

[ 64](structbt__vocs__register__param.md#aace5987e890c8b4dbf3e01fa5c2a4432) bool [desc\_writable](structbt__vocs__register__param.md#aace5987e890c8b4dbf3e01fa5c2a4432);

65

[ 67](structbt__vocs__register__param.md#a306ad3c712bb5a5109f3afb4912d590b) struct [bt\_vocs\_cb](structbt__vocs__cb.md) \*[cb](structbt__vocs__register__param.md#a306ad3c712bb5a5109f3afb4912d590b);

68};

69

[ 71](structbt__vocs__discover__param.md)struct [bt\_vocs\_discover\_param](structbt__vocs__discover__param.md) {

[ 77](structbt__vocs__discover__param.md#aca830a50436def0f422d05eba34273ed) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [start\_handle](structbt__vocs__discover__param.md#aca830a50436def0f422d05eba34273ed);

[ 83](structbt__vocs__discover__param.md#a3811da3035bb1f0ff5d290eb60fb2fda) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [end\_handle](structbt__vocs__discover__param.md#a3811da3035bb1f0ff5d290eb60fb2fda);

84};

85

[ 91](group__bt__gatt__vocs.md#gadde50c3eb90ea7b7aa9b9c4b3672710f)struct bt\_vocs \*[bt\_vocs\_free\_instance\_get](group__bt__gatt__vocs.md#gadde50c3eb90ea7b7aa9b9c4b3672710f)(void);

92

[ 102](group__bt__gatt__vocs.md#ga9f7ff4c0521686ded011758ddd8ea95e)void \*[bt\_vocs\_svc\_decl\_get](group__bt__gatt__vocs.md#ga9f7ff4c0521686ded011758ddd8ea95e)(struct bt\_vocs \*vocs);

103

[ 115](group__bt__gatt__vocs.md#gafcf7ecea73c8c199b38c7291ce4a648f)int [bt\_vocs\_client\_conn\_get](group__bt__gatt__vocs.md#gafcf7ecea73c8c199b38c7291ce4a648f)(const struct bt\_vocs \*vocs, struct bt\_conn \*\*conn);

116

[ 125](group__bt__gatt__vocs.md#gac011ddd93bb3240148a789f1ee9ef7da)int [bt\_vocs\_register](group__bt__gatt__vocs.md#gac011ddd93bb3240148a789f1ee9ef7da)(struct bt\_vocs \*vocs,

126 const struct [bt\_vocs\_register\_param](structbt__vocs__register__param.md) \*param);

127

[ 139](group__bt__gatt__vocs.md#gaa329fd8931add8fd4f6c59b48c91ef75)typedef void (\*[bt\_vocs\_state\_cb](group__bt__gatt__vocs.md#gaa329fd8931add8fd4f6c59b48c91ef75))(struct bt\_vocs \*inst, int err, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) offset);

140

[ 148](group__bt__gatt__vocs.md#ga2630344190f12f911bb2b01c4b95ded6)typedef void (\*[bt\_vocs\_set\_offset\_cb](group__bt__gatt__vocs.md#ga2630344190f12f911bb2b01c4b95ded6))(struct bt\_vocs \*inst, int err);

149

[ 161](group__bt__gatt__vocs.md#ga84983707e04eae75f18017072b647115)typedef void (\*[bt\_vocs\_location\_cb](group__bt__gatt__vocs.md#ga84983707e04eae75f18017072b647115))(struct bt\_vocs \*inst, int err,

162 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) location);

163

[ 175](group__bt__gatt__vocs.md#gaa351c3ab631b16272e27cbb837d9e49c)typedef void (\*[bt\_vocs\_description\_cb](group__bt__gatt__vocs.md#gaa351c3ab631b16272e27cbb837d9e49c))(struct bt\_vocs \*inst, int err,

176 char \*description);

177

[ 190](group__bt__gatt__vocs.md#gad50fd539190b5c64b5262d3830699365)typedef void (\*[bt\_vocs\_discover\_cb](group__bt__gatt__vocs.md#gad50fd539190b5c64b5262d3830699365))(struct bt\_vocs \*inst, int err);

191

[ 192](structbt__vocs__cb.md)struct [bt\_vocs\_cb](structbt__vocs__cb.md) {

[ 193](structbt__vocs__cb.md#ae633c1f6cd8aa03d89287e783179460e) [bt\_vocs\_state\_cb](group__bt__gatt__vocs.md#gaa329fd8931add8fd4f6c59b48c91ef75) [state](structbt__vocs__cb.md#ae633c1f6cd8aa03d89287e783179460e);

[ 194](structbt__vocs__cb.md#a50d1d429089456267b06d4450712b897) [bt\_vocs\_location\_cb](group__bt__gatt__vocs.md#ga84983707e04eae75f18017072b647115) [location](structbt__vocs__cb.md#a50d1d429089456267b06d4450712b897);

[ 195](structbt__vocs__cb.md#ac508b1e6dda00c607aa1cbe52423ec52) [bt\_vocs\_description\_cb](group__bt__gatt__vocs.md#gaa351c3ab631b16272e27cbb837d9e49c) [description](structbt__vocs__cb.md#ac508b1e6dda00c607aa1cbe52423ec52);

196

197#if defined(CONFIG\_BT\_VOCS\_CLIENT)

198 /\* Client only \*/

199 [bt\_vocs\_discover\_cb](group__bt__gatt__vocs.md#gad50fd539190b5c64b5262d3830699365) discover;

200 [bt\_vocs\_set\_offset\_cb](group__bt__gatt__vocs.md#ga2630344190f12f911bb2b01c4b95ded6) set\_offset;

201#endif /\* CONFIG\_BT\_VOCS\_CLIENT \*/

202};

203

[ 213](group__bt__gatt__vocs.md#ga6c835234a5530bae3bb0f5bd03a0bdd7)int [bt\_vocs\_state\_get](group__bt__gatt__vocs.md#ga6c835234a5530bae3bb0f5bd03a0bdd7)(struct bt\_vocs \*inst);

214

[ 223](group__bt__gatt__vocs.md#ga28ea337e439b5872abab8f5b98719da4)int [bt\_vocs\_state\_set](group__bt__gatt__vocs.md#ga28ea337e439b5872abab8f5b98719da4)(struct bt\_vocs \*inst, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) offset);

224

[ 234](group__bt__gatt__vocs.md#ga90ba394e6be138d6052b95d73ab2f409)int [bt\_vocs\_location\_get](group__bt__gatt__vocs.md#ga90ba394e6be138d6052b95d73ab2f409)(struct bt\_vocs \*inst);

235

[ 244](group__bt__gatt__vocs.md#ga02b036f060eee947c8924bbea846bc29)int [bt\_vocs\_location\_set](group__bt__gatt__vocs.md#ga02b036f060eee947c8924bbea846bc29)(struct bt\_vocs \*inst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) location);

245

[ 255](group__bt__gatt__vocs.md#gaac1c1292cae4c5845a376d2f4db3d661)int [bt\_vocs\_description\_get](group__bt__gatt__vocs.md#gaac1c1292cae4c5845a376d2f4db3d661)(struct bt\_vocs \*inst);

256

[ 265](group__bt__gatt__vocs.md#gac17cb7101233605834ec6b66d7417f91)int [bt\_vocs\_description\_set](group__bt__gatt__vocs.md#gac17cb7101233605834ec6b66d7417f91)(struct bt\_vocs \*inst, const char \*description);

266

[ 273](group__bt__gatt__vocs.md#gaace802556eca3d634a13dd8f2bf3c544)void [bt\_vocs\_client\_cb\_register](group__bt__gatt__vocs.md#gaace802556eca3d634a13dd8f2bf3c544)(struct bt\_vocs \*inst, struct [bt\_vocs\_cb](structbt__vocs__cb.md) \*cb);

274

[ 280](group__bt__gatt__vocs.md#ga6182120b1bece7f5851bb6295c81b562)struct bt\_vocs \*[bt\_vocs\_client\_free\_instance\_get](group__bt__gatt__vocs.md#ga6182120b1bece7f5851bb6295c81b562)(void);

281

[ 293](group__bt__gatt__vocs.md#ga45efa872e07ac8051379caf5aa8d0133)int [bt\_vocs\_discover](group__bt__gatt__vocs.md#ga45efa872e07ac8051379caf5aa8d0133)(struct bt\_conn \*conn, struct bt\_vocs \*inst,

294 const struct [bt\_vocs\_discover\_param](structbt__vocs__discover__param.md) \*param);

295

296#ifdef \_\_cplusplus

297}

298#endif

299

303

304#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_SERVICES\_VOCS\_H\_ \*/

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_vocs\_location\_set](group__bt__gatt__vocs.md#ga02b036f060eee947c8924bbea846bc29)

int bt\_vocs\_location\_set(struct bt\_vocs \*inst, uint32\_t location)

Set the Volume Offset Control Service location.

[bt\_vocs\_set\_offset\_cb](group__bt__gatt__vocs.md#ga2630344190f12f911bb2b01c4b95ded6)

void(\* bt\_vocs\_set\_offset\_cb)(struct bt\_vocs \*inst, int err)

Callback function for setting offset.

**Definition** vocs.h:148

[bt\_vocs\_state\_set](group__bt__gatt__vocs.md#ga28ea337e439b5872abab8f5b98719da4)

int bt\_vocs\_state\_set(struct bt\_vocs \*inst, int16\_t offset)

Set the Volume Offset Control Service offset state.

[bt\_vocs\_discover](group__bt__gatt__vocs.md#ga45efa872e07ac8051379caf5aa8d0133)

int bt\_vocs\_discover(struct bt\_conn \*conn, struct bt\_vocs \*inst, const struct bt\_vocs\_discover\_param \*param)

Discover a Volume Offset Control Service.

[bt\_vocs\_client\_free\_instance\_get](group__bt__gatt__vocs.md#ga6182120b1bece7f5851bb6295c81b562)

struct bt\_vocs \* bt\_vocs\_client\_free\_instance\_get(void)

Returns a pointer to a Volume Offset Control Service client instance.

[bt\_vocs\_state\_get](group__bt__gatt__vocs.md#ga6c835234a5530bae3bb0f5bd03a0bdd7)

int bt\_vocs\_state\_get(struct bt\_vocs \*inst)

Read the Volume Offset Control Service offset state.

[bt\_vocs\_location\_cb](group__bt__gatt__vocs.md#ga84983707e04eae75f18017072b647115)

void(\* bt\_vocs\_location\_cb)(struct bt\_vocs \*inst, int err, uint32\_t location)

Callback function for the location.

**Definition** vocs.h:161

[bt\_vocs\_location\_get](group__bt__gatt__vocs.md#ga90ba394e6be138d6052b95d73ab2f409)

int bt\_vocs\_location\_get(struct bt\_vocs \*inst)

Read the Volume Offset Control Service location.

[bt\_vocs\_svc\_decl\_get](group__bt__gatt__vocs.md#ga9f7ff4c0521686ded011758ddd8ea95e)

void \* bt\_vocs\_svc\_decl\_get(struct bt\_vocs \*vocs)

Get the service declaration attribute.

[bt\_vocs\_state\_cb](group__bt__gatt__vocs.md#gaa329fd8931add8fd4f6c59b48c91ef75)

void(\* bt\_vocs\_state\_cb)(struct bt\_vocs \*inst, int err, int16\_t offset)

Callback function for the offset state.

**Definition** vocs.h:139

[bt\_vocs\_description\_cb](group__bt__gatt__vocs.md#gaa351c3ab631b16272e27cbb837d9e49c)

void(\* bt\_vocs\_description\_cb)(struct bt\_vocs \*inst, int err, char \*description)

Callback function for the description.

**Definition** vocs.h:175

[bt\_vocs\_description\_get](group__bt__gatt__vocs.md#gaac1c1292cae4c5845a376d2f4db3d661)

int bt\_vocs\_description\_get(struct bt\_vocs \*inst)

Read the Volume Offset Control Service output description.

[bt\_vocs\_client\_cb\_register](group__bt__gatt__vocs.md#gaace802556eca3d634a13dd8f2bf3c544)

void bt\_vocs\_client\_cb\_register(struct bt\_vocs \*inst, struct bt\_vocs\_cb \*cb)

Registers the callbacks for the Volume Offset Control Service client.

[bt\_vocs\_register](group__bt__gatt__vocs.md#gac011ddd93bb3240148a789f1ee9ef7da)

int bt\_vocs\_register(struct bt\_vocs \*vocs, const struct bt\_vocs\_register\_param \*param)

Register the Volume Offset Control Service instance.

[bt\_vocs\_description\_set](group__bt__gatt__vocs.md#gac17cb7101233605834ec6b66d7417f91)

int bt\_vocs\_description\_set(struct bt\_vocs \*inst, const char \*description)

Set the Volume Offset Control Service description.

[bt\_vocs\_discover\_cb](group__bt__gatt__vocs.md#gad50fd539190b5c64b5262d3830699365)

void(\* bt\_vocs\_discover\_cb)(struct bt\_vocs \*inst, int err)

Callback function for bt\_vocs\_discover.

**Definition** vocs.h:190

[bt\_vocs\_free\_instance\_get](group__bt__gatt__vocs.md#gadde50c3eb90ea7b7aa9b9c4b3672710f)

struct bt\_vocs \* bt\_vocs\_free\_instance\_get(void)

Get a free service instance of Volume Offset Control Service from the pool.

[bt\_vocs\_client\_conn\_get](group__bt__gatt__vocs.md#gafcf7ecea73c8c199b38c7291ce4a648f)

int bt\_vocs\_client\_conn\_get(const struct bt\_vocs \*vocs, struct bt\_conn \*\*conn)

Get the connection pointer of a client instance.

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

[bt\_vocs\_cb](structbt__vocs__cb.md)

**Definition** vocs.h:192

[bt\_vocs\_cb::location](structbt__vocs__cb.md#a50d1d429089456267b06d4450712b897)

bt\_vocs\_location\_cb location

**Definition** vocs.h:194

[bt\_vocs\_cb::description](structbt__vocs__cb.md#ac508b1e6dda00c607aa1cbe52423ec52)

bt\_vocs\_description\_cb description

**Definition** vocs.h:195

[bt\_vocs\_cb::state](structbt__vocs__cb.md#ae633c1f6cd8aa03d89287e783179460e)

bt\_vocs\_state\_cb state

**Definition** vocs.h:193

[bt\_vocs\_discover\_param](structbt__vocs__discover__param.md)

Structure for discovering a Volume Offset Control Service instance.

**Definition** vocs.h:71

[bt\_vocs\_discover\_param::end\_handle](structbt__vocs__discover__param.md#a3811da3035bb1f0ff5d290eb60fb2fda)

uint16\_t end\_handle

The end handle of the discovering.

**Definition** vocs.h:83

[bt\_vocs\_discover\_param::start\_handle](structbt__vocs__discover__param.md#aca830a50436def0f422d05eba34273ed)

uint16\_t start\_handle

The start handle of the discovering.

**Definition** vocs.h:77

[bt\_vocs\_register\_param](structbt__vocs__register__param.md)

Structure for registering a Volume Offset Control Service instance.

**Definition** vocs.h:50

[bt\_vocs\_register\_param::location](structbt__vocs__register__param.md#a0572c60319c8984e2437e596584c46f5)

uint32\_t location

Audio Location bitmask.

**Definition** vocs.h:52

[bt\_vocs\_register\_param::output\_desc](structbt__vocs__register__param.md#a1f6baed09dc35b974d06f1426b671e05)

char \* output\_desc

Initial audio output description.

**Definition** vocs.h:61

[bt\_vocs\_register\_param::cb](structbt__vocs__register__param.md#a306ad3c712bb5a5109f3afb4912d590b)

struct bt\_vocs\_cb \* cb

Pointer to the callback structure.

**Definition** vocs.h:67

[bt\_vocs\_register\_param::location\_writable](structbt__vocs__register__param.md#a6919f965abfa1fec39a3c8e0f29c04f3)

bool location\_writable

Boolean to set whether the location is writable by clients.

**Definition** vocs.h:55

[bt\_vocs\_register\_param::desc\_writable](structbt__vocs__register__param.md#aace5987e890c8b4dbf3e01fa5c2a4432)

bool desc\_writable

Boolean to set whether the description is writable by clients.

**Definition** vocs.h:64

[bt\_vocs\_register\_param::offset](structbt__vocs__register__param.md#ac1c2475cd390f5acf840f92ea45c6d31)

int16\_t offset

Initial volume offset (-255 to 255).

**Definition** vocs.h:58

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [vocs.h](vocs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
