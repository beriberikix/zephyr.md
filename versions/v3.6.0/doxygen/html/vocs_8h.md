---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/vocs_8h.html
original_path: doxygen/html/vocs_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

vocs.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`

[Go to the source code of this file.](vocs_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_vocs\_register\_param](structbt__vocs__register__param.md) |
|  | Structure for registering a Volume Offset Control Service instance. [More...](structbt__vocs__register__param.md#details) |
| struct | [bt\_vocs\_discover\_param](structbt__vocs__discover__param.md) |
|  | Structure for discovering a Volume Offset Control Service instance. [More...](structbt__vocs__discover__param.md#details) |
| struct | [bt\_vocs\_cb](structbt__vocs__cb.md) |

| Macros | |
| --- | --- |
| #define | [BT\_VOCS\_ERR\_INVALID\_COUNTER](group__bt__gatt__vocs.md#ga17c81394b9b4d601768e72d8c360992f)   0x80 |
|  | Volume Offset Control Service Error codes. |
| #define | [BT\_VOCS\_ERR\_OP\_NOT\_SUPPORTED](group__bt__gatt__vocs.md#gadd01a04e3c4336a13a4760e2448131b1)   0x81 |
| #define | [BT\_VOCS\_ERR\_OUT\_OF\_RANGE](group__bt__gatt__vocs.md#ga2ecb7e0408bb1767c2d51c816f4b273d)   0x82 |
| #define | [BT\_VOCS\_MIN\_OFFSET](group__bt__gatt__vocs.md#ga64d4e32f9d92a58b3229b3aa2e8fcc4d)   -255 |
| #define | [BT\_VOCS\_MAX\_OFFSET](group__bt__gatt__vocs.md#ga800092562173fd37826b5537feaac3ae)   255 |

| Typedefs | |
| --- | --- |
| typedef void(\* | [bt\_vocs\_state\_cb](group__bt__gatt__vocs.md#gaa329fd8931add8fd4f6c59b48c91ef75)) (struct bt\_vocs \*inst, int err, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) offset) |
|  | Callback function for the offset state. |
| typedef void(\* | [bt\_vocs\_set\_offset\_cb](group__bt__gatt__vocs.md#ga2630344190f12f911bb2b01c4b95ded6)) (struct bt\_vocs \*inst, int err) |
|  | Callback function for setting offset. |
| typedef void(\* | [bt\_vocs\_location\_cb](group__bt__gatt__vocs.md#ga84983707e04eae75f18017072b647115)) (struct bt\_vocs \*inst, int err, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) location) |
|  | Callback function for the location. |
| typedef void(\* | [bt\_vocs\_description\_cb](group__bt__gatt__vocs.md#gaa351c3ab631b16272e27cbb837d9e49c)) (struct bt\_vocs \*inst, int err, char \*description) |
|  | Callback function for the description. |
| typedef void(\* | [bt\_vocs\_discover\_cb](group__bt__gatt__vocs.md#gad50fd539190b5c64b5262d3830699365)) (struct bt\_vocs \*inst, int err) |
|  | Callback function for bt\_vocs\_discover. |

| Functions | |
| --- | --- |
| struct bt\_vocs \* | [bt\_vocs\_free\_instance\_get](group__bt__gatt__vocs.md#gadde50c3eb90ea7b7aa9b9c4b3672710f) (void) |
|  | Get a free service instance of Volume Offset Control Service from the pool. |
| void \* | [bt\_vocs\_svc\_decl\_get](group__bt__gatt__vocs.md#ga9f7ff4c0521686ded011758ddd8ea95e) (struct bt\_vocs \*vocs) |
|  | Get the service declaration attribute. |
| int | [bt\_vocs\_client\_conn\_get](group__bt__gatt__vocs.md#gafcf7ecea73c8c199b38c7291ce4a648f) (const struct bt\_vocs \*vocs, struct bt\_conn \*\*conn) |
|  | Get the connection pointer of a client instance. |
| int | [bt\_vocs\_register](group__bt__gatt__vocs.md#gac011ddd93bb3240148a789f1ee9ef7da) (struct bt\_vocs \*vocs, const struct [bt\_vocs\_register\_param](structbt__vocs__register__param.md) \*param) |
|  | Register the Volume Offset Control Service instance. |
| int | [bt\_vocs\_state\_get](group__bt__gatt__vocs.md#ga6c835234a5530bae3bb0f5bd03a0bdd7) (struct bt\_vocs \*inst) |
|  | Read the Volume Offset Control Service offset state. |
| int | [bt\_vocs\_state\_set](group__bt__gatt__vocs.md#ga28ea337e439b5872abab8f5b98719da4) (struct bt\_vocs \*inst, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) offset) |
|  | Set the Volume Offset Control Service offset state. |
| int | [bt\_vocs\_location\_get](group__bt__gatt__vocs.md#ga90ba394e6be138d6052b95d73ab2f409) (struct bt\_vocs \*inst) |
|  | Read the Volume Offset Control Service location. |
| int | [bt\_vocs\_location\_set](group__bt__gatt__vocs.md#ga02b036f060eee947c8924bbea846bc29) (struct bt\_vocs \*inst, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) location) |
|  | Set the Volume Offset Control Service location. |
| int | [bt\_vocs\_description\_get](group__bt__gatt__vocs.md#gaac1c1292cae4c5845a376d2f4db3d661) (struct bt\_vocs \*inst) |
|  | Read the Volume Offset Control Service output description. |
| int | [bt\_vocs\_description\_set](group__bt__gatt__vocs.md#gac17cb7101233605834ec6b66d7417f91) (struct bt\_vocs \*inst, const char \*description) |
|  | Set the Volume Offset Control Service description. |
| void | [bt\_vocs\_client\_cb\_register](group__bt__gatt__vocs.md#gaace802556eca3d634a13dd8f2bf3c544) (struct bt\_vocs \*inst, struct [bt\_vocs\_cb](structbt__vocs__cb.md) \*cb) |
|  | Registers the callbacks for the Volume Offset Control Service client. |
| struct bt\_vocs \* | [bt\_vocs\_client\_free\_instance\_get](group__bt__gatt__vocs.md#ga6182120b1bece7f5851bb6295c81b562) (void) |
|  | Returns a pointer to a Volume Offset Control Service client instance. |
| int | [bt\_vocs\_discover](group__bt__gatt__vocs.md#ga45efa872e07ac8051379caf5aa8d0133) (struct bt\_conn \*conn, struct bt\_vocs \*inst, const struct [bt\_vocs\_discover\_param](structbt__vocs__discover__param.md) \*param) |
|  | Discover a Volume Offset Control Service. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [vocs.h](vocs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
