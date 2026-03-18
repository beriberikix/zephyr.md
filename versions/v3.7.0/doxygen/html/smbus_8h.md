---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/smbus_8h.html
original_path: doxygen/html/smbus_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

smbus.h File Reference

Public SMBus Driver APIs.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/stats/stats.h](stats_2stats_8h_source.md)>`  
`#include <zephyr/syscalls/smbus.h>`

[Go to the source code of this file.](smbus_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [smbus\_callback](structsmbus__callback.md) |
|  | SMBus callback structure. [More...](structsmbus__callback.md#details) |
| struct | [smbus\_dt\_spec](structsmbus__dt__spec.md) |
|  | Complete SMBus DT information. [More...](structsmbus__dt__spec.md#details) |

| Macros | |
| --- | --- |
| #define | [SMBUS\_BLOCK\_BYTES\_MAX](group__smbus__interface.md#ga5ccde036931dc54e684ae5b955ff80d3)   32 |
|  | Maximum number of bytes in SMBus Block protocol. |
| #define | [SMBUS\_DT\_SPEC\_GET](group__smbus__interface.md#gaf489d1b6c6aaaa1b3b1e9db823b24241)(node\_id) |
|  | Structure initializer for [smbus\_dt\_spec](structsmbus__dt__spec.md "Complete SMBus DT information.") from devicetree. |
| #define | [SMBUS\_DT\_SPEC\_INST\_GET](group__smbus__interface.md#ga7e5bf5ecea7cbadf5d2a8b0c1e7a91af)(inst) |
|  | Structure initializer for [smbus\_dt\_spec](structsmbus__dt__spec.md "Complete SMBus DT information.") from devicetree instance. |
| #define | [SMBUS\_DEVICE\_DT\_DEFINE](group__smbus__interface.md#gaab024b741eb2c126d41d6db6e76333ee)(node\_id, init\_fn, [pm\_device](structpm__device.md), data\_ptr, cfg\_ptr, level, prio, api\_ptr, ...) |
|  | Like [DEVICE\_DT\_DEFINE()](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1 "Create a device object from a devicetree node identifier and set it up for boot time initialization.") with SMBus specifics. |
| #define | [SMBUS\_DEVICE\_DT\_INST\_DEFINE](group__smbus__interface.md#ga610bc9c96bb22741c850696127f16b92)(inst, ...) |
|  | Like [SMBUS\_DEVICE\_DT\_DEFINE()](group__smbus__interface.md#gaab024b741eb2c126d41d6db6e76333ee "Like DEVICE_DT_DEFINE() with SMBus specifics.") for an instance of a DT\_DRV\_COMPAT compatible. |
| SMBus Protocol commands | |
| SMBus Specification defines the following SMBus protocols operations | |
| #define | [SMBUS\_CMD\_QUICK](group__smbus__interface.md#ga7cf2e52d836b28041f9aeb7ac3c172e4)   0b000 |
|  | SMBus Quick protocol is a very simple command with no data sent or received. |
| #define | [SMBUS\_CMD\_BYTE](group__smbus__interface.md#gafa607ea7083ad73873716282e1f55c8e)   0b001 |
|  | SMBus Byte protocol can send or receive one byte of data. |
| #define | [SMBUS\_CMD\_BYTE\_DATA](group__smbus__interface.md#gabf5306ea95a2e8e5dc0270331218ea3d)   0b010 |
|  | SMBus Byte Data protocol sends the first byte (command) followed by read or write one byte. |
| #define | [SMBUS\_CMD\_WORD\_DATA](group__smbus__interface.md#ga70743c58b580018e567d2cb8595bea6f)   0b011 |
|  | SMBus Word Data protocol sends the first byte (command) followed by read or write two bytes. |
| #define | [SMBUS\_CMD\_PROC\_CALL](group__smbus__interface.md#ga4400135f39814e328cf5e8ae11f27e3c)   0b100 |
|  | SMBus Process Call protocol is Write Word followed by Read Word. |
| #define | [SMBUS\_CMD\_BLOCK](group__smbus__interface.md#gaa8d81258230e67e4f87b5908ab66b08d)   0b101 |
|  | SMBus Block protocol reads or writes a block of data up to 32 bytes. |
| #define | [SMBUS\_CMD\_BLOCK\_PROC](group__smbus__interface.md#ga9505b622875799e381c51f2df601c57a)   0b111 |
|  | SMBus Block Write - Block Read Process Call protocol is Block Write followed by Block Read. |
| SMBus device functionality | |
| The following parameters describe the functionality of the SMBus device | |
| #define | [SMBUS\_MODE\_CONTROLLER](group__smbus__interface.md#ga440a66ac32cf89d4a37782a0b51bda2c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Peripheral to act as Controller. |
| #define | [SMBUS\_MODE\_PEC](group__smbus__interface.md#ga6b9ddfb187688f3b1e1a3fdace9ecc76)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Support Packet Error Code (PEC) checking. |
| #define | [SMBUS\_MODE\_HOST\_NOTIFY](group__smbus__interface.md#ga0633fc1ff48d806b6ca0e408f29141fe)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Support Host Notify functionality. |
| #define | [SMBUS\_MODE\_SMBALERT](group__smbus__interface.md#ga7675e48d824e97df4c07c0e2496bee3d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Support SMBALERT signal functionality. |
| SMBus special reserved addresses | |
| The following addresses are reserved by SMBus specification | |
| #define | [SMBUS\_ADDRESS\_ARA](group__smbus__interface.md#ga1d282b18efccf83456acd14a8f4cd970)   0x0c |
|  | Alert Response Address (ARA). |

| Typedefs | |
| --- | --- |
| typedef void(\* | [smbus\_callback\_handler\_t](group__smbus__interface.md#ga6d6ee9d29de5c0007d34328eb7c9f7c9)) (const struct [device](structdevice.md) \*dev, struct [smbus\_callback](structsmbus__callback.md) \*cb, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
|  | Define SMBus callback handler function signature. |

| Enumerations | |
| --- | --- |
| SMBus read / write direction | |
| enum | [smbus\_direction](group__smbus__interface.md#gad0c28687977d0a7866bdea87aef88016) { [SMBUS\_MSG\_WRITE](group__smbus__interface.md#ggad0c28687977d0a7866bdea87aef88016a9c9dec19cbada732cef85784b0eedc54) = 0 , [SMBUS\_MSG\_READ](group__smbus__interface.md#ggad0c28687977d0a7866bdea87aef88016aa87094fdacefac89c0b1a03be1c0d22f) = 1 } |
|  | SMBus read / write direction. [More...](group__smbus__interface.md#gad0c28687977d0a7866bdea87aef88016) |

| Functions | |
| --- | --- |
| static void | [smbus\_xfer\_stats](group__smbus__interface.md#ga0a63b800c14f5831730372b9bad41864) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sent, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)) |
|  | Updates the SMBus stats. |
| int | [smbus\_configure](group__smbus__interface.md#ga517305aa7cc9c93ae449b3c548d6c835) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_config) |
|  | Configure operation of a SMBus host controller. |
| int | [smbus\_get\_config](group__smbus__interface.md#ga9ca38ca95c0576bdc75b7eb8d0ca29ef) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dev\_config) |
|  | Get configuration of a SMBus host controller. |
| static int | [smbus\_smbalert\_set\_cb](group__smbus__interface.md#gadff533a6bc198815ee56d03a36b949e0) (const struct [device](structdevice.md) \*dev, struct [smbus\_callback](structsmbus__callback.md) \*cb) |
|  | Add SMBUSALERT callback for a SMBus host controller. |
| int | [smbus\_smbalert\_remove\_cb](group__smbus__interface.md#gac79105d8a76bf543394d666a16ae8bdd) (const struct [device](structdevice.md) \*dev, struct [smbus\_callback](structsmbus__callback.md) \*cb) |
|  | Remove SMBUSALERT callback from a SMBus host controller. |
| static int | [smbus\_host\_notify\_set\_cb](group__smbus__interface.md#ga5054a6de634b015f54dacbe81427d0d2) (const struct [device](structdevice.md) \*dev, struct [smbus\_callback](structsmbus__callback.md) \*cb) |
|  | Add Host Notify callback for a SMBus host controller. |
| int | [smbus\_host\_notify\_remove\_cb](group__smbus__interface.md#gaa68f76bf02a13e0d45d05921cf3ca64d) (const struct [device](structdevice.md) \*dev, struct [smbus\_callback](structsmbus__callback.md) \*cb) |
|  | Remove Host Notify callback from a SMBus host controller. |
| int | [smbus\_quick](group__smbus__interface.md#gab008499bca4a4096672d5909fa71b21d) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, enum [smbus\_direction](group__smbus__interface.md#gad0c28687977d0a7866bdea87aef88016) direction) |
|  | Perform SMBus Quick operation. |
| int | [smbus\_byte\_write](group__smbus__interface.md#ga7dd01c1e00a0f8b0315e442707332251) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte) |
|  | Perform SMBus Byte Write operation. |
| int | [smbus\_byte\_read](group__smbus__interface.md#gadaef9dad3470a7e4d3360e0246271ca1) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*byte) |
|  | Perform SMBus Byte Read operation. |
| int | [smbus\_byte\_data\_write](group__smbus__interface.md#gadd7ec1eb3db981efceb8f959546a3b6a) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte) |
|  | Perform SMBus Byte Data Write operation. |
| int | [smbus\_byte\_data\_read](group__smbus__interface.md#ga1f1148a7cb92e0e0aef7ae3a84615c9b) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*byte) |
|  | Perform SMBus Byte Data Read operation. |
| int | [smbus\_word\_data\_write](group__smbus__interface.md#gade05f9bbbba609832df91fe804dd5d3c) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) word) |
|  | Perform SMBus Word Data Write operation. |
| int | [smbus\_word\_data\_read](group__smbus__interface.md#ga72a789110c7286a51c5cd5e2215abce1) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*word) |
|  | Perform SMBus Word Data Read operation. |
| int | [smbus\_pcall](group__smbus__interface.md#ga2c1369835d3783bb5b5c3cb3711fec92) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) send\_word, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*recv\_word) |
|  | Perform SMBus Process Call operation. |
| int | [smbus\_block\_write](group__smbus__interface.md#ga55a867cdcb504039f274abae2d1a99e4) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf) |
|  | Perform SMBus Block Write operation. |
| int | [smbus\_block\_read](group__smbus__interface.md#ga67603db9b44636b0b62a24fd623cfb1c) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf) |
|  | Perform SMBus Block Read operation. |
| int | [smbus\_block\_pcall](group__smbus__interface.md#ga680c3d713a615f4b62503d6f84de4290) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) snd\_count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*snd\_buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rcv\_count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rcv\_buf) |
|  | Perform SMBus Block Process Call operation. |

## Detailed Description

Public SMBus Driver APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [smbus.h](smbus_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
