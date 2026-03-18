---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/aics_8h.html
original_path: doxygen/html/aics_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

aics.h File Reference

`#include <[zephyr/bluetooth/bluetooth.h](bluetooth_8h_source.md)>`

[Go to the source code of this file.](aics_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_aics\_register\_param](structbt__aics__register__param.md) |
|  | Structure for initializing a Audio Input Control Service instance. [More...](structbt__aics__register__param.md#details) |
| struct | [bt\_aics\_discover\_param](structbt__aics__discover__param.md) |
|  | Structure for discovering a Audio Input Control Service instance. [More...](structbt__aics__discover__param.md#details) |
| struct | [bt\_aics\_cb](structbt__aics__cb.md) |

| Macros | |
| --- | --- |
| #define | [BT\_AICS\_STATE\_UNMUTED](group__bt__gatt__aics.md#ga47436e2df23067ce86dc761d77ed14b7)   0x00 |
|  | Audio Input Control Service mute states. |
| #define | [BT\_AICS\_STATE\_MUTED](group__bt__gatt__aics.md#ga1572eaaffea5412b496eb714d64aa981)   0x01 |
| #define | [BT\_AICS\_STATE\_MUTE\_DISABLED](group__bt__gatt__aics.md#gad0063d0e0b622b4093607e5485897214)   0x02 |
| #define | [BT\_AICS\_MODE\_MANUAL\_ONLY](group__bt__gatt__aics.md#gaecb9365a5e390111311d1b415a2cee79)   0x00 |
|  | Audio Input Control Service input modes. |
| #define | [BT\_AICS\_MODE\_AUTO\_ONLY](group__bt__gatt__aics.md#ga6b536bdcab602ccaccfafe3b37258890)   0x01 |
| #define | [BT\_AICS\_MODE\_MANUAL](group__bt__gatt__aics.md#ga7cf0508dd7407ec3bb92dec71cc00816)   0x02 |
| #define | [BT\_AICS\_MODE\_AUTO](group__bt__gatt__aics.md#ga0ac3a583dd7ca58a0d356d9f60797517)   0x03 |
| #define | [BT\_AICS\_INPUT\_TYPE\_UNSPECIFIED](group__bt__gatt__aics.md#ga2204f35b5f1aa41c27f62b8f0dcf74b6)   0x00 |
|  | Audio Input Control Service input types. |
| #define | [BT\_AICS\_INPUT\_TYPE\_BLUETOOTH](group__bt__gatt__aics.md#gac8ebf643f9a4101ea8da18827577bf5d)   0x01 |
| #define | [BT\_AICS\_INPUT\_TYPE\_MICROPHONE](group__bt__gatt__aics.md#ga7fcb5aefacb641a8ef7db4e9a554a65d)   0x02 |
| #define | [BT\_AICS\_INPUT\_TYPE\_ANALOG](group__bt__gatt__aics.md#ga525b361d1d555f20d292cf1aded0d046)   0x03 |
| #define | [BT\_AICS\_INPUT\_TYPE\_DIGITAL](group__bt__gatt__aics.md#ga688605eb9eb5b27ca62fac9b85fde472)   0x04 |
| #define | [BT\_AICS\_INPUT\_TYPE\_RADIO](group__bt__gatt__aics.md#ga3b878b41ab30067bceefc0cd72340376)   0x05 |
| #define | [BT\_AICS\_INPUT\_TYPE\_STREAMING](group__bt__gatt__aics.md#ga43a02e2025e3cb3e10bc2ee2128ee877)   0x06 |
| #define | [BT\_AICS\_ERR\_INVALID\_COUNTER](group__bt__gatt__aics.md#gae54199f78ff7d7380353f3950bd03a39)   0x80 |
|  | Audio Input Control Service Error codes. |
| #define | [BT\_AICS\_ERR\_OP\_NOT\_SUPPORTED](group__bt__gatt__aics.md#ga00c0942dab2bf25c680278927aa49af8)   0x81 |
| #define | [BT\_AICS\_ERR\_MUTE\_DISABLED](group__bt__gatt__aics.md#ga1efb1f6a4c24c2a20fc7136928abac6b)   0x82 |
| #define | [BT\_AICS\_ERR\_OUT\_OF\_RANGE](group__bt__gatt__aics.md#ga2f3806b8056ea8ed43b2a7cd52ffa4f3)   0x83 |
| #define | [BT\_AICS\_ERR\_GAIN\_MODE\_NOT\_ALLOWED](group__bt__gatt__aics.md#ga6673570f7679322bfa4719bf6e41e299)   0x84 |

| Typedefs | |
| --- | --- |
| typedef void(\* | [bt\_aics\_write\_cb](group__bt__gatt__aics.md#ga36991fe1dee5168db618518d094d80ef)) (struct bt\_aics \*inst, int err) |
|  | Callback function for writes. |
| typedef void(\* | [bt\_aics\_state\_cb](group__bt__gatt__aics.md#ga2e851f49f9c7e71a18376468a13fdf4f)) (struct bt\_aics \*inst, int err, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) gain, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mute, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) mode) |
|  | Callback function for the input state. |
| typedef void(\* | [bt\_aics\_gain\_setting\_cb](group__bt__gatt__aics.md#ga11da08c010f4aa849c2e3725dc5cbaeb)) (struct bt\_aics \*inst, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) units, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) minimum, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) maximum) |
|  | Callback function for the gain settings. |
| typedef void(\* | [bt\_aics\_type\_cb](group__bt__gatt__aics.md#ga6e76b9f2de4cdbcd7539c76f6a347fa5)) (struct bt\_aics \*inst, int err, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type) |
|  | Callback function for the input type. |
| typedef void(\* | [bt\_aics\_status\_cb](group__bt__gatt__aics.md#ga044d92a4273c6537a9cdf20922352ed6)) (struct bt\_aics \*inst, int err, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) active) |
|  | Callback function for the input status. |
| typedef void(\* | [bt\_aics\_description\_cb](group__bt__gatt__aics.md#ga98b142ea7a66de5577c44aa90d507930)) (struct bt\_aics \*inst, int err, char \*description) |
|  | Callback function for the description. |
| typedef void(\* | [bt\_aics\_discover\_cb](group__bt__gatt__aics.md#ga9fda39f8410308e05eb928eeb7267e83)) (struct bt\_aics \*inst, int err) |
|  | Callback function for bt\_aics\_discover. |

| Functions | |
| --- | --- |
| struct bt\_aics \* | [bt\_aics\_free\_instance\_get](group__bt__gatt__aics.md#gab10ad3599f5b602cdf5504bc92508109) (void) |
|  | Get a free instance of Audio Input Control Service from the pool. |
| void \* | [bt\_aics\_svc\_decl\_get](group__bt__gatt__aics.md#ga8b415343e7ecf399ecfd0dcaa49bd1ee) (struct bt\_aics \*aics) |
|  | Get the service declaration attribute. |
| int | [bt\_aics\_client\_conn\_get](group__bt__gatt__aics.md#ga0e088e26cf73f1f3b918660d4acdebb9) (const struct bt\_aics \*aics, struct bt\_conn \*\*conn) |
|  | Get the connection pointer of a client instance. |
| int | [bt\_aics\_register](group__bt__gatt__aics.md#ga008ef5cebfcb9b4a3084f411fa81238e) (struct bt\_aics \*aics, struct [bt\_aics\_register\_param](structbt__aics__register__param.md) \*param) |
|  | Initialize the Audio Input Control Service instance. |
| int | [bt\_aics\_discover](group__bt__gatt__aics.md#gad16d296462af2f61a893bda8d25cc9de) (struct bt\_conn \*conn, struct bt\_aics \*inst, const struct [bt\_aics\_discover\_param](structbt__aics__discover__param.md) \*param) |
|  | Discover a Audio Input Control Service. |
| int | [bt\_aics\_deactivate](group__bt__gatt__aics.md#ga4be4c4e3c74aa55fbf599157aa1c2098) (struct bt\_aics \*inst) |
|  | Deactivates a Audio Input Control Service instance. |
| int | [bt\_aics\_activate](group__bt__gatt__aics.md#gac46268949fa7cbbb827d149a3a904daa) (struct bt\_aics \*inst) |
|  | Activates a Audio Input Control Service instance. |
| int | [bt\_aics\_state\_get](group__bt__gatt__aics.md#ga23bbc1393d21fe38f501813935b25b3d) (struct bt\_aics \*inst) |
|  | Read the Audio Input Control Service input state. |
| int | [bt\_aics\_gain\_setting\_get](group__bt__gatt__aics.md#ga38d7131397d7762d3bd53e152a6c6130) (struct bt\_aics \*inst) |
|  | Read the Audio Input Control Service gain settings. |
| int | [bt\_aics\_type\_get](group__bt__gatt__aics.md#gaf57896e2096a5e96ec46a56cdf216159) (struct bt\_aics \*inst) |
|  | Read the Audio Input Control Service input type. |
| int | [bt\_aics\_status\_get](group__bt__gatt__aics.md#gade387c52d201ce10b39ef52157dae83d) (struct bt\_aics \*inst) |
|  | Read the Audio Input Control Service input status. |
| int | [bt\_aics\_disable\_mute](group__bt__gatt__aics.md#ga5a1ad98afe45da9ffbb7247671385d40) (struct bt\_aics \*inst) |
|  | Disable mute in the Audio Input Control Service. |
| int | [bt\_aics\_unmute](group__bt__gatt__aics.md#ga43396d2d4b3bd9cdd0c82275fafeadfc) (struct bt\_aics \*inst) |
|  | Unmute the Audio Input Control Service input. |
| int | [bt\_aics\_mute](group__bt__gatt__aics.md#ga5345254eaf099560e609d97044b39a97) (struct bt\_aics \*inst) |
|  | Mute the Audio Input Control Service input. |
| int | [bt\_aics\_gain\_set\_manual\_only](group__bt__gatt__aics.md#ga0460e82d4277a2c4b14964799ad5f2b0) (struct bt\_aics \*inst) |
|  | Set manual only gain mode in Audio Input Control Service. |
| int | [bt\_aics\_gain\_set\_auto\_only](group__bt__gatt__aics.md#ga22869d8a62eb59bc4aad25946da8f9cf) (struct bt\_aics \*inst) |
|  | Set automatic only gain mode in Audio Input Control Service. |
| int | [bt\_aics\_manual\_gain\_set](group__bt__gatt__aics.md#ga7ddb93125f6275fc7c99fbf448e24f0c) (struct bt\_aics \*inst) |
|  | Set input gain to manual. |
| int | [bt\_aics\_automatic\_gain\_set](group__bt__gatt__aics.md#ga759712886cd3c4c025ea360dcb663c59) (struct bt\_aics \*inst) |
|  | Set the input gain to automatic. |
| int | [bt\_aics\_gain\_set](group__bt__gatt__aics.md#ga20f3a178788ec6aef593034159793b94) (struct bt\_aics \*inst, [int8\_t](stdint_8h.md#accbd6432732c88ad6adc5365800433b6) gain) |
|  | Set the input gain. |
| int | [bt\_aics\_description\_get](group__bt__gatt__aics.md#gaf0b659698aa6a6a79143d4f591f67e09) (struct bt\_aics \*inst) |
|  | Read the Audio Input Control Service description. |
| int | [bt\_aics\_description\_set](group__bt__gatt__aics.md#ga7de5ffd2eb61ca562b9773b37470ebd9) (struct bt\_aics \*inst, const char \*description) |
|  | Set the Audio Input Control Service description. |
| struct bt\_aics \* | [bt\_aics\_client\_free\_instance\_get](group__bt__gatt__aics.md#ga913838aa0d5bff239c2faef4d8a8b36b) (void) |
|  | Get a new Audio Input Control Service client instance. |
| void | [bt\_aics\_client\_cb\_register](group__bt__gatt__aics.md#gabd6bdcdad0dd5a4c509f9e7cabb3e601) (struct bt\_aics \*inst, struct [bt\_aics\_cb](structbt__aics__cb.md) \*cb) |
|  | Registers the callbacks for the Audio Input Control Service client. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [audio](dir_8efd337b27f0cf68bd11ab0b8a371a18.md)
- [aics.h](aics_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
