---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__smbus__interface.html
original_path: doxygen/html/group__smbus__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

SMBus Interface

[Device Driver APIs](group__io__interfaces.md)

SMBus Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [smbus\_callback](structsmbus__callback.md) |
|  | SMBus callback structure. [More...](structsmbus__callback.md#details) |
| struct | [smbus\_dt\_spec](structsmbus__dt__spec.md) |
|  | Complete SMBus DT information. [More...](structsmbus__dt__spec.md#details) |

| Macros | |
| --- | --- |
| #define | [SMBUS\_BLOCK\_BYTES\_MAX](#ga5ccde036931dc54e684ae5b955ff80d3)   32 |
|  | Maximum number of bytes in SMBus Block protocol. |
| #define | [SMBUS\_DT\_SPEC\_GET](#gaf489d1b6c6aaaa1b3b1e9db823b24241)(node\_id) |
|  | Structure initializer for [smbus\_dt\_spec](structsmbus__dt__spec.md "Complete SMBus DT information.") from devicetree. |
| #define | [SMBUS\_DT\_SPEC\_INST\_GET](#ga7e5bf5ecea7cbadf5d2a8b0c1e7a91af)(inst) |
|  | Structure initializer for [smbus\_dt\_spec](structsmbus__dt__spec.md "Complete SMBus DT information.") from devicetree instance. |
| #define | [SMBUS\_DEVICE\_DT\_DEFINE](#gaab024b741eb2c126d41d6db6e76333ee)(node\_id, init\_fn, [pm\_device](structpm__device.md), data\_ptr, cfg\_ptr, level, prio, api\_ptr, ...) |
|  | Like [DEVICE\_DT\_DEFINE()](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1 "Create a device object from a devicetree node identifier and set it up for boot time initialization.") with SMBus specifics. |
| #define | [SMBUS\_DEVICE\_DT\_INST\_DEFINE](#ga610bc9c96bb22741c850696127f16b92)(inst, ...) |
|  | Like [SMBUS\_DEVICE\_DT\_DEFINE()](#gaab024b741eb2c126d41d6db6e76333ee) for an instance of a DT\_DRV\_COMPAT compatible. |

| Typedefs | |
| --- | --- |
| typedef void(\* | [smbus\_callback\_handler\_t](#ga6d6ee9d29de5c0007d34328eb7c9f7c9)) (const struct [device](structdevice.md) \*dev, struct [smbus\_callback](structsmbus__callback.md) \*cb, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
|  | Define SMBus callback handler function signature. |

| Functions | |
| --- | --- |
| static void | [smbus\_xfer\_stats](#ga0a63b800c14f5831730372b9bad41864) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) sent, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)) |
|  | Updates the SMBus stats. |
| int | [smbus\_configure](#ga517305aa7cc9c93ae449b3c548d6c835) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) dev\_config) |
|  | Configure operation of a SMBus host controller. |
| int | [smbus\_get\_config](#ga9ca38ca95c0576bdc75b7eb8d0ca29ef) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*dev\_config) |
|  | Get configuration of a SMBus host controller. |
| static int | [smbus\_smbalert\_set\_cb](#gadff533a6bc198815ee56d03a36b949e0) (const struct [device](structdevice.md) \*dev, struct [smbus\_callback](structsmbus__callback.md) \*cb) |
|  | Add SMBUSALERT callback for a SMBus host controller. |
| int | [smbus\_smbalert\_remove\_cb](#gac79105d8a76bf543394d666a16ae8bdd) (const struct [device](structdevice.md) \*dev, struct [smbus\_callback](structsmbus__callback.md) \*cb) |
|  | Remove SMBUSALERT callback from a SMBus host controller. |
| static int | [smbus\_host\_notify\_set\_cb](#ga5054a6de634b015f54dacbe81427d0d2) (const struct [device](structdevice.md) \*dev, struct [smbus\_callback](structsmbus__callback.md) \*cb) |
|  | Add Host Notify callback for a SMBus host controller. |
| int | [smbus\_host\_notify\_remove\_cb](#gaa68f76bf02a13e0d45d05921cf3ca64d) (const struct [device](structdevice.md) \*dev, struct [smbus\_callback](structsmbus__callback.md) \*cb) |
|  | Remove Host Notify callback from a SMBus host controller. |
| int | [smbus\_quick](#gab008499bca4a4096672d5909fa71b21d) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, enum [smbus\_direction](#gad0c28687977d0a7866bdea87aef88016) direction) |
|  | Perform SMBus Quick operation. |
| int | [smbus\_byte\_write](#ga7dd01c1e00a0f8b0315e442707332251) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte) |
|  | Perform SMBus Byte Write operation. |
| int | [smbus\_byte\_read](#gadaef9dad3470a7e4d3360e0246271ca1) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*byte) |
|  | Perform SMBus Byte Read operation. |
| int | [smbus\_byte\_data\_write](#gadd7ec1eb3db981efceb8f959546a3b6a) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) byte) |
|  | Perform SMBus Byte Data Write operation. |
| int | [smbus\_byte\_data\_read](#ga1f1148a7cb92e0e0aef7ae3a84615c9b) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*byte) |
|  | Perform SMBus Byte Data Read operation. |
| int | [smbus\_word\_data\_write](#gade05f9bbbba609832df91fe804dd5d3c) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) word) |
|  | Perform SMBus Word Data Write operation. |
| int | [smbus\_word\_data\_read](#ga72a789110c7286a51c5cd5e2215abce1) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*word) |
|  | Perform SMBus Word Data Read operation. |
| int | [smbus\_pcall](#ga2c1369835d3783bb5b5c3cb3711fec92) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) send\_word, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*recv\_word) |
|  | Perform SMBus Process Call operation. |
| int | [smbus\_block\_write](#ga55a867cdcb504039f274abae2d1a99e4) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf) |
|  | Perform SMBus Block Write operation. |
| int | [smbus\_block\_read](#ga67603db9b44636b0b62a24fd623cfb1c) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf) |
|  | Perform SMBus Block Read operation. |
| int | [smbus\_block\_pcall](#ga680c3d713a615f4b62503d6f84de4290) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) snd\_count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*snd\_buf, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rcv\_count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rcv\_buf) |
|  | Perform SMBus Block Process Call operation. |

| SMBus read / write direction | |
| --- | --- |
| enum | [smbus\_direction](#gad0c28687977d0a7866bdea87aef88016) { [SMBUS\_MSG\_WRITE](#ggad0c28687977d0a7866bdea87aef88016a9c9dec19cbada732cef85784b0eedc54) = 0 , [SMBUS\_MSG\_READ](#ggad0c28687977d0a7866bdea87aef88016aa87094fdacefac89c0b1a03be1c0d22f) = 1 } |
|  | SMBus read / write direction. [More...](#gad0c28687977d0a7866bdea87aef88016) |

| SMBus Protocol commands | |
| --- | --- |
| SMBus Specification defines the following SMBus protocols operations | |
| #define | [SMBUS\_CMD\_QUICK](#ga7cf2e52d836b28041f9aeb7ac3c172e4)   0b000 |
|  | SMBus Quick protocol is a very simple command with no data sent or received. |
| #define | [SMBUS\_CMD\_BYTE](#gafa607ea7083ad73873716282e1f55c8e)   0b001 |
|  | SMBus Byte protocol can send or receive one byte of data. |
| #define | [SMBUS\_CMD\_BYTE\_DATA](#gabf5306ea95a2e8e5dc0270331218ea3d)   0b010 |
|  | SMBus Byte Data protocol sends the first byte (command) followed by read or write one byte. |
| #define | [SMBUS\_CMD\_WORD\_DATA](#ga70743c58b580018e567d2cb8595bea6f)   0b011 |
|  | SMBus Word Data protocol sends the first byte (command) followed by read or write two bytes. |
| #define | [SMBUS\_CMD\_PROC\_CALL](#ga4400135f39814e328cf5e8ae11f27e3c)   0b100 |
|  | SMBus Process Call protocol is Write Word followed by Read Word. |
| #define | [SMBUS\_CMD\_BLOCK](#gaa8d81258230e67e4f87b5908ab66b08d)   0b101 |
|  | SMBus Block protocol reads or writes a block of data up to 32 bytes. |
| #define | [SMBUS\_CMD\_BLOCK\_PROC](#ga9505b622875799e381c51f2df601c57a)   0b111 |
|  | SMBus Block Write - Block Read Process Call protocol is Block Write followed by Block Read. |

| SMBus device functionality | |
| --- | --- |
| The following parameters describe the functionality of the SMBus device | |
| #define | [SMBUS\_MODE\_CONTROLLER](#ga440a66ac32cf89d4a37782a0b51bda2c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Peripheral to act as Controller. |
| #define | [SMBUS\_MODE\_PEC](#ga6b9ddfb187688f3b1e1a3fdace9ecc76)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Support Packet Error Code (PEC) checking. |
| #define | [SMBUS\_MODE\_HOST\_NOTIFY](#ga0633fc1ff48d806b6ca0e408f29141fe)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Support Host Notify functionality. |
| #define | [SMBUS\_MODE\_SMBALERT](#ga7675e48d824e97df4c07c0e2496bee3d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Support SMBALERT signal functionality. |

| SMBus special reserved addresses | |
| --- | --- |
| The following addresses are reserved by SMBus specification | |
| #define | [SMBUS\_ADDRESS\_ARA](#ga1d282b18efccf83456acd14a8f4cd970)   0x0c |
|  | Alert Response Address (ARA). |

## Detailed Description

SMBus Interface.

## Macro Definition Documentation

## [◆ ](#ga1d282b18efccf83456acd14a8f4cd970)SMBUS\_ADDRESS\_ARA

| #define SMBUS\_ADDRESS\_ARA   0x0c |
| --- |

`#include <[smbus.h](smbus_8h.md)>`

Alert Response Address (ARA).

A broadcast address used by the system host as part of the Alert Response Protocol.

## [◆ ](#ga5ccde036931dc54e684ae5b955ff80d3)SMBUS\_BLOCK\_BYTES\_MAX

| #define SMBUS\_BLOCK\_BYTES\_MAX   32 |
| --- |

`#include <[smbus.h](smbus_8h.md)>`

Maximum number of bytes in SMBus Block protocol.

## [◆ ](#gaa8d81258230e67e4f87b5908ab66b08d)SMBUS\_CMD\_BLOCK

| #define SMBUS\_CMD\_BLOCK   0b101 |
| --- |

`#include <[smbus.h](smbus_8h.md)>`

SMBus Block protocol reads or writes a block of data up to 32 bytes.

The Count byte specifies the amount of data.

SMBus Block Write

0 1 2

0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

|S| Periph Addr |W|A| Command code |A| Send Count=N |A|

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

| Data Write 1 |A| ... |A| Data Write N |A|P|

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

SMBus Block Read

0 1 2

0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

|S| Periph Addr |W|A| Command code |A|S| Periph Addr |R|

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

|A| Recv Count=N |A| Data Read 1 |A| ... |A|

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

| Data Read N |N|P|

+-+-+-+-+-+-+-+-+-+-+

## [◆ ](#ga9505b622875799e381c51f2df601c57a)SMBUS\_CMD\_BLOCK\_PROC

| #define SMBUS\_CMD\_BLOCK\_PROC   0b111 |
| --- |

`#include <[smbus.h](smbus_8h.md)>`

SMBus Block Write - Block Read Process Call protocol is Block Write followed by Block Read.

0 1 2

0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

|S| Periph Addr |W|A| Command code |A| Count = N |A|

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

| Data Write 1 |A| ... |A| Data Write N |A|S|

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

| Periph Addr |R|A| Recv Count=N |A| Data Read 1 |A| |

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

| ... |A| Data Read N |N|P|

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

## [◆ ](#gafa607ea7083ad73873716282e1f55c8e)SMBUS\_CMD\_BYTE

| #define SMBUS\_CMD\_BYTE   0b001 |
| --- |

`#include <[smbus.h](smbus_8h.md)>`

SMBus Byte protocol can send or receive one byte of data.

Byte Write

0 1 2

0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

|S| Periph Addr |W|A| Command code |A|P|

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

Byte Read

0 1 2

0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

|S| Periph Addr |R|A| Byte received |N|P|

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

## [◆ ](#gabf5306ea95a2e8e5dc0270331218ea3d)SMBUS\_CMD\_BYTE\_DATA

| #define SMBUS\_CMD\_BYTE\_DATA   0b010 |
| --- |

`#include <[smbus.h](smbus_8h.md)>`

SMBus Byte Data protocol sends the first byte (command) followed by read or write one byte.

Byte Data Write

0 1 2

0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

|S| Periph Addr |W|A| Command code |A| Data Write |A|P|

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

Byte Data Read

0 1 2

0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

|S| Periph Addr |W|A| Command code |A|S| Periph Addr |R|A|

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

| Data Read |N|P|

+-+-+-+-+-+-+-+-+-+-+

## [◆ ](#ga4400135f39814e328cf5e8ae11f27e3c)SMBUS\_CMD\_PROC\_CALL

| #define SMBUS\_CMD\_PROC\_CALL   0b100 |
| --- |

`#include <[smbus.h](smbus_8h.md)>`

SMBus Process Call protocol is Write Word followed by Read Word.

It is named so because the command sends data and waits for the peripheral to return a reply.

0 1 2

0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

|S| Periph Addr |W|A| Command code |A| Data Write Low|A|

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

| Data Write Hi |A|S| Periph Addr |R|A| Data Read Low |A|

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

| Data Read Hi |N|P|

+-+-+-+-+-+-+-+-+-+-+

## [◆ ](#ga7cf2e52d836b28041f9aeb7ac3c172e4)SMBUS\_CMD\_QUICK

| #define SMBUS\_CMD\_QUICK   0b000 |
| --- |

`#include <[smbus.h](smbus_8h.md)>`

SMBus Quick protocol is a very simple command with no data sent or received.

Peripheral may denote only R/W bit, which can still be used for the peripheral management, for example to switch peripheral On/Off. Quick protocol can also be used for peripheral devices scanning.

0 1

0 1 2 3 4 5 6 7 8 9 0

+-+-+-+-+-+-+-+-+-+-+-+

|S| Periph Addr |D|A|P|

+-+-+-+-+-+-+-+-+-+-+-+

## [◆ ](#ga70743c58b580018e567d2cb8595bea6f)SMBUS\_CMD\_WORD\_DATA

| #define SMBUS\_CMD\_WORD\_DATA   0b011 |
| --- |

`#include <[smbus.h](smbus_8h.md)>`

SMBus Word Data protocol sends the first byte (command) followed by read or write two bytes.

Word Data Write

0 1 2

0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

|S| Periph Addr |W|A| Command code |A| Data Write Low|A|

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

| Data Write Hi |A|P|

+-+-+-+-+-+-+-+-+-+-+

Word Data Read

0 1 2

0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

|S| Periph Addr |W|A| Command code |A|S| Periph Addr |R|

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

|A| Data Read Low |A| Data Read Hi |N|P|

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

## [◆ ](#gaab024b741eb2c126d41d6db6e76333ee)SMBUS\_DEVICE\_DT\_DEFINE

| #define SMBUS\_DEVICE\_DT\_DEFINE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *init\_fn*, |
|  |  |  | *[pm\_device](structpm__device.md)*, |
|  |  |  | *data\_ptr*, |
|  |  |  | *cfg\_ptr*, |
|  |  |  | *level*, |
|  |  |  | *prio*, |
|  |  |  | *api\_ptr*, |
|  |  |  | ... ) |

`#include <[smbus.h](smbus_8h.md)>`

**Value:**

Z\_SMBUS\_DEVICE\_STATE\_DEFINE(node\_id, \

Z\_DEVICE\_DT\_DEV\_NAME(node\_id)); \

Z\_SMBUS\_INIT\_FN(Z\_DEVICE\_DT\_DEV\_NAME(node\_id), init\_fn) \

Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_NAME(node\_id), \

[DEVICE\_DT\_NAME](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)(node\_id), \

&[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(Z\_DEVICE\_DT\_DEV\_NAME(node\_id), \_init),\

[pm\_device](structpm__device.md), \

data\_ptr, cfg\_ptr, level, prio, \

api\_ptr, \

&(Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_NAME \

(node\_id)).devstate), \

\_\_VA\_ARGS\_\_)

[DEVICE\_DT\_NAME](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)

#define DEVICE\_DT\_NAME(node\_id)

Return a string name for a devicetree node.

**Definition** device.h:149

[pm\_device](structpm__device.md)

Runtime PM info for device with generic PM.

**Definition** device.h:165

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)

#define UTIL\_CAT(a,...)

**Definition** util\_internal.h:104

Like [DEVICE\_DT\_DEFINE()](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1 "Create a device object from a devicetree node identifier and set it up for boot time initialization.") with SMBus specifics.

Defines a device which implements the SMBus API. May generate a custom [device\_state](structdevice__state.md "Runtime device dynamic structure (in RAM) per driver instance.") container struct and init\_fn wrapper when needed depending on SMBus `CONFIG_SMBUS_STATS` .

Parameters
:   | node\_id | The devicetree node identifier. |
    | --- | --- |
    | init\_fn | Name of the init function of the driver. |
    | [pm\_device](structpm__device.md "Runtime PM info for device with generic PM.") | PM device resources reference (NULL if device does not use PM). |
    | data\_ptr | Pointer to the device's private data. |
    | cfg\_ptr | The address to the structure containing the configuration information for this instance of the driver. |
    | level | The initialization level. See [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") for details. |
    | prio | Priority within the selected initialization level. See [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") for details. |
    | api\_ptr | Provides an initial pointer to the API function struct used by the driver. Can be NULL. |

## [◆ ](#ga610bc9c96bb22741c850696127f16b92)SMBUS\_DEVICE\_DT\_INST\_DEFINE

| #define SMBUS\_DEVICE\_DT\_INST\_DEFINE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[smbus.h](smbus_8h.md)>`

**Value:**

[SMBUS\_DEVICE\_DT\_DEFINE](#gaab024b741eb2c126d41d6db6e76333ee)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), \_\_VA\_ARGS\_\_)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3410

[SMBUS\_DEVICE\_DT\_DEFINE](#gaab024b741eb2c126d41d6db6e76333ee)

#define SMBUS\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm\_device, data\_ptr, cfg\_ptr, level, prio, api\_ptr,...)

Like DEVICE\_DT\_DEFINE() with SMBus specifics.

**Definition** smbus.h:502

Like [SMBUS\_DEVICE\_DT\_DEFINE()](#gaab024b741eb2c126d41d6db6e76333ee) for an instance of a DT\_DRV\_COMPAT compatible.

Parameters
:   | inst | instance number. This is replaced by DT\_DRV\_COMPAT(inst) in the call to [SMBUS\_DEVICE\_DT\_DEFINE()](#gaab024b741eb2c126d41d6db6e76333ee). |
    | --- | --- |
    | ... | other parameters as expected by [SMBUS\_DEVICE\_DT\_DEFINE()](#gaab024b741eb2c126d41d6db6e76333ee). |

## [◆ ](#gaf489d1b6c6aaaa1b3b1e9db823b24241)SMBUS\_DT\_SPEC\_GET

| #define SMBUS\_DT\_SPEC\_GET | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[smbus.h](smbus_8h.md)>`

**Value:**

{ \

.bus = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)(node\_id)), \

.addr = [DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)(node\_id) \

}

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:233

[DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)

#define DT\_BUS(node\_id)

Node's bus controller.

**Definition** devicetree.h:3362

[DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)

#define DT\_REG\_ADDR(node\_id)

Get a node's (only) register block address.

**Definition** devicetree.h:2214

Structure initializer for [smbus\_dt\_spec](structsmbus__dt__spec.md "Complete SMBus DT information.") from devicetree.

This helper macro expands to a static initializer for a struct
[smbus\_dt\_spec](structsmbus__dt__spec.md "Complete SMBus DT information.") by reading the relevant bus and address data from the devicetree.

Parameters
:   | node\_id | Devicetree node identifier for the SMBus device whose struct [smbus\_dt\_spec](structsmbus__dt__spec.md "Complete SMBus DT information.") to create an initializer for |
    | --- | --- |

## [◆ ](#ga7e5bf5ecea7cbadf5d2a8b0c1e7a91af)SMBUS\_DT\_SPEC\_INST\_GET

| #define SMBUS\_DT\_SPEC\_INST\_GET | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[smbus.h](smbus_8h.md)>`

**Value:**

[SMBUS\_DT\_SPEC\_GET](#gaf489d1b6c6aaaa1b3b1e9db823b24241)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[SMBUS\_DT\_SPEC\_GET](#gaf489d1b6c6aaaa1b3b1e9db823b24241)

#define SMBUS\_DT\_SPEC\_GET(node\_id)

Structure initializer for smbus\_dt\_spec from devicetree.

**Definition** smbus.h:316

Structure initializer for [smbus\_dt\_spec](structsmbus__dt__spec.md "Complete SMBus DT information.") from devicetree instance.

This is equivalent to [SMBUS\_DT\_SPEC\_GET(DT\_DRV\_INST(inst))](#gaf489d1b6c6aaaa1b3b1e9db823b24241).

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |

## [◆ ](#ga440a66ac32cf89d4a37782a0b51bda2c)SMBUS\_MODE\_CONTROLLER

| #define SMBUS\_MODE\_CONTROLLER   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[smbus.h](smbus_8h.md)>`

Peripheral to act as Controller.

## [◆ ](#ga0633fc1ff48d806b6ca0e408f29141fe)SMBUS\_MODE\_HOST\_NOTIFY

| #define SMBUS\_MODE\_HOST\_NOTIFY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[smbus.h](smbus_8h.md)>`

Support Host Notify functionality.

## [◆ ](#ga6b9ddfb187688f3b1e1a3fdace9ecc76)SMBUS\_MODE\_PEC

| #define SMBUS\_MODE\_PEC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[smbus.h](smbus_8h.md)>`

Support Packet Error Code (PEC) checking.

## [◆ ](#ga7675e48d824e97df4c07c0e2496bee3d)SMBUS\_MODE\_SMBALERT

| #define SMBUS\_MODE\_SMBALERT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[smbus.h](smbus_8h.md)>`

Support SMBALERT signal functionality.

## Typedef Documentation

## [◆ ](#ga6d6ee9d29de5c0007d34328eb7c9f7c9)smbus\_callback\_handler\_t

| typedef void(\* smbus\_callback\_handler\_t) (const struct [device](structdevice.md) \*dev, struct [smbus\_callback](structsmbus__callback.md) \*cb, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) addr) |
| --- |

`#include <[smbus.h](smbus_8h.md)>`

Define SMBus callback handler function signature.

Parameters
:   | dev | Pointer to the device structure for the SMBus driver instance. |
    | --- | --- |
    | cb | Structure [smbus\_callback](structsmbus__callback.md "SMBus callback structure.") owning this handler. |
    | addr | Address of the SMBus peripheral device. |

## Enumeration Type Documentation

## [◆ ](#gad0c28687977d0a7866bdea87aef88016)smbus\_direction

| enum [smbus\_direction](#gad0c28687977d0a7866bdea87aef88016) |
| --- |

`#include <[smbus.h](smbus_8h.md)>`

SMBus read / write direction.

| Enumerator | |
| --- | --- |
| SMBUS\_MSG\_WRITE | Write a message to SMBus peripheral. |
| SMBUS\_MSG\_READ | Read a message from SMBus peripheral. |

## Function Documentation

## [◆ ](#ga680c3d713a615f4b62503d6f84de4290)smbus\_block\_pcall()

| int smbus\_block\_pcall | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cmd*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *snd\_count*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *snd\_buf*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *rcv\_count*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *rcv\_buf* ) |

`#include <[smbus.h](smbus_8h.md)>`

Perform SMBus Block Process Call operation.

This routine provides a generic interface to perform SMBus Block Process Call operation. This operation is basically Block Write followed by Block Read.

Parameters
:   | dev | Pointer to the device structure for the SMBus driver instance. |
    | --- | --- |
    | addr | Address of the SMBus peripheral device. |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | Command byte which is sent to peripheral device first. |
    | snd\_count | Size of the data block buffer to send. |
    | snd\_buf | Data block buffer send to the peripheral device. |
    | rcv\_count | Size of the data peripheral sent. |
    | rcv\_buf | Data block buffer received from the peripheral device. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ENOSYS | If function [smbus\_block\_pcall()](#ga680c3d713a615f4b62503d6f84de4290) is not implemented by the driver. |

## [◆ ](#ga67603db9b44636b0b62a24fd623cfb1c)smbus\_block\_read()

| int smbus\_block\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cmd*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *count*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf* ) |

`#include <[smbus.h](smbus_8h.md)>`

Perform SMBus Block Read operation.

This routine provides a generic interface to perform SMBus Block Read operation.

Parameters
:   | dev | Pointer to the device structure for the SMBus driver instance. |
    | --- | --- |
    | addr | Address of the SMBus peripheral device. |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | Command byte which is sent to peripheral device first. |
    | count | Size of the data peripheral sent. Maximum 32 bytes. |
    | buf | Data block buffer received from the peripheral device. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ENOSYS | If function [smbus\_block\_read()](#ga67603db9b44636b0b62a24fd623cfb1c) is not implemented by the driver. |

## [◆ ](#ga55a867cdcb504039f274abae2d1a99e4)smbus\_block\_write()

| int smbus\_block\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cmd*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *count*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *buf* ) |

`#include <[smbus.h](smbus_8h.md)>`

Perform SMBus Block Write operation.

This routine provides a generic interface to perform SMBus Block Write operation.

Parameters
:   | dev | Pointer to the device structure for the SMBus driver instance. |
    | --- | --- |
    | addr | Address of the SMBus peripheral device. |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | Command byte which is sent to peripheral device first. |
    | count | Size of the data block buffer. Maximum 32 bytes. |
    | buf | Data block buffer to be sent to the peripheral device. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ENOSYS | If function [smbus\_block\_write()](#ga55a867cdcb504039f274abae2d1a99e4) is not implemented by the driver. |

## [◆ ](#ga1f1148a7cb92e0e0aef7ae3a84615c9b)smbus\_byte\_data\_read()

| int smbus\_byte\_data\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cmd*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *byte* ) |

`#include <[smbus.h](smbus_8h.md)>`

Perform SMBus Byte Data Read operation.

This routine provides a generic interface to perform SMBus Byte Data Read operation.

Parameters
:   | dev | Pointer to the device structure for the SMBus driver instance. |
    | --- | --- |
    | addr | Address of the SMBus peripheral device. |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | Command byte which is sent to peripheral device first. |
    | byte | Byte received from the peripheral device. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ENOSYS | If function [smbus\_byte\_data\_read()](#ga1f1148a7cb92e0e0aef7ae3a84615c9b) is not implemented by the driver. |

## [◆ ](#gadd7ec1eb3db981efceb8f959546a3b6a)smbus\_byte\_data\_write()

| int smbus\_byte\_data\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cmd*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *byte* ) |

`#include <[smbus.h](smbus_8h.md)>`

Perform SMBus Byte Data Write operation.

This routine provides a generic interface to perform SMBus Byte Data Write operation.

Parameters
:   | dev | Pointer to the device structure for the SMBus driver instance. |
    | --- | --- |
    | addr | Address of the SMBus peripheral device. |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | Command byte which is sent to peripheral device first. |
    | byte | Byte to be sent to the peripheral device. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ENOSYS | If function [smbus\_byte\_data\_write()](#gadd7ec1eb3db981efceb8f959546a3b6a) is not implemented by the driver. |

## [◆ ](#gadaef9dad3470a7e4d3360e0246271ca1)smbus\_byte\_read()

| int smbus\_byte\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *byte* ) |

`#include <[smbus.h](smbus_8h.md)>`

Perform SMBus Byte Read operation.

This routine provides a generic interface to perform SMBus Byte Read operation.

Parameters
:   | dev | Pointer to the device structure for the SMBus driver instance. |
    | --- | --- |
    | addr | Address of the SMBus peripheral device. |
    | byte | Byte received from the peripheral device. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ENOSYS | If function [smbus\_byte\_read()](#gadaef9dad3470a7e4d3360e0246271ca1) is not implemented by the driver. |

## [◆ ](#ga7dd01c1e00a0f8b0315e442707332251)smbus\_byte\_write()

| int smbus\_byte\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *byte* ) |

`#include <[smbus.h](smbus_8h.md)>`

Perform SMBus Byte Write operation.

This routine provides a generic interface to perform SMBus Byte Write operation.

Parameters
:   | dev | Pointer to the device structure for the SMBus driver instance. |
    | --- | --- |
    | addr | Address of the SMBus peripheral device. |
    | byte | Byte to be sent to the peripheral device. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ENOSYS | If function [smbus\_byte\_write()](#ga7dd01c1e00a0f8b0315e442707332251) is not implemented by the driver. |

## [◆ ](#ga517305aa7cc9c93ae449b3c548d6c835)smbus\_configure()

| int smbus\_configure | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *dev\_config* ) |

`#include <[smbus.h](smbus_8h.md)>`

Configure operation of a SMBus host controller.

Parameters
:   | dev | Pointer to the device structure for the SMBus driver instance. |
    | --- | --- |
    | dev\_config | Bit-packed 32-bit value to the device runtime configuration for the SMBus controller. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |

## [◆ ](#ga9ca38ca95c0576bdc75b7eb8d0ca29ef)smbus\_get\_config()

| int smbus\_get\_config | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *dev\_config* ) |

`#include <[smbus.h](smbus_8h.md)>`

Get configuration of a SMBus host controller.

This routine provides a way to get current configuration. It is allowed to call the function before smbus\_configure, because some SMBus ports can be configured during init process. However, if the SMBus port is not configured, smbus\_get\_config returns an error.

smbus\_get\_config can return cached config or probe hardware, but it has to be up to date with current configuration.

Parameters
:   | dev | Pointer to the device structure for the SMBus driver instance. |
    | --- | --- |
    | dev\_config | Pointer to return bit-packed 32-bit value of the SMBus controller configuration. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ENOSYS | If function [smbus\_get\_config()](#ga9ca38ca95c0576bdc75b7eb8d0ca29ef) is not implemented by the driver. |

## [◆ ](#gaa68f76bf02a13e0d45d05921cf3ca64d)smbus\_host\_notify\_remove\_cb()

| int smbus\_host\_notify\_remove\_cb | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [smbus\_callback](structsmbus__callback.md) \* | *cb* ) |

`#include <[smbus.h](smbus_8h.md)>`

Remove Host Notify callback from a SMBus host controller.

Parameters
:   | dev | Pointer to the device structure for the SMBus driver instance. |
    | --- | --- |
    | cb | Pointer to a callback structure. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ENOSYS | If function [smbus\_host\_notify\_remove\_cb()](#gaa68f76bf02a13e0d45d05921cf3ca64d) is not implemented by the driver. |

## [◆ ](#ga5054a6de634b015f54dacbe81427d0d2)smbus\_host\_notify\_set\_cb()

| | int smbus\_host\_notify\_set\_cb | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [smbus\_callback](structsmbus__callback.md) \* | *cb* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[smbus.h](smbus_8h.md)>`

Add Host Notify callback for a SMBus host controller.

Parameters
:   | dev | Pointer to the device structure for the SMBus driver instance. |
    | --- | --- |
    | cb | Pointer to a callback structure. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ENOSYS | If function [smbus\_host\_notify\_set\_cb()](#ga5054a6de634b015f54dacbe81427d0d2) is not implemented by the driver. |

## [◆ ](#ga2c1369835d3783bb5b5c3cb3711fec92)smbus\_pcall()

| int smbus\_pcall | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cmd*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *send\_word*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *recv\_word* ) |

`#include <[smbus.h](smbus_8h.md)>`

Perform SMBus Process Call operation.

This routine provides a generic interface to perform SMBus Process Call operation, which means Write 2 bytes following by Read 2 bytes.

Parameters
:   | dev | Pointer to the device structure for the SMBus driver instance. |
    | --- | --- |
    | addr | Address of the SMBus peripheral device. |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | Command byte which is sent to peripheral device first. |
    | send\_word | Word (16-bit) to be sent to the peripheral device. |
    | recv\_word | Word (16-bit) received from the peripheral device. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ENOSYS | If function [smbus\_pcall()](#ga2c1369835d3783bb5b5c3cb3711fec92) is not implemented by the driver. |

## [◆ ](#gab008499bca4a4096672d5909fa71b21d)smbus\_quick()

| int smbus\_quick | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | enum [smbus\_direction](#gad0c28687977d0a7866bdea87aef88016) | *direction* ) |

`#include <[smbus.h](smbus_8h.md)>`

Perform SMBus Quick operation.

This routine provides a generic interface to perform SMBus Quick operation.

Parameters
:   | dev | Pointer to the device structure for the SMBus driver instance. driver configured in controller mode. |
    | --- | --- |
    | addr | Address of the SMBus peripheral device. |
    | direction | Direction Read or Write. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ENOSYS | If function [smbus\_quick()](#gab008499bca4a4096672d5909fa71b21d) is not implemented by the driver. |

## [◆ ](#gac79105d8a76bf543394d666a16ae8bdd)smbus\_smbalert\_remove\_cb()

| int smbus\_smbalert\_remove\_cb | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [smbus\_callback](structsmbus__callback.md) \* | *cb* ) |

`#include <[smbus.h](smbus_8h.md)>`

Remove SMBUSALERT callback from a SMBus host controller.

Parameters
:   | dev | Pointer to the device structure for the SMBus driver instance. |
    | --- | --- |
    | cb | Pointer to a callback structure. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ENOSYS | If function [smbus\_smbalert\_remove\_cb()](#gac79105d8a76bf543394d666a16ae8bdd) is not implemented by the driver. |

## [◆ ](#gadff533a6bc198815ee56d03a36b949e0)smbus\_smbalert\_set\_cb()

| | int smbus\_smbalert\_set\_cb | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | struct [smbus\_callback](structsmbus__callback.md) \* | *cb* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[smbus.h](smbus_8h.md)>`

Add SMBUSALERT callback for a SMBus host controller.

Parameters
:   | dev | Pointer to the device structure for the SMBus driver instance. |
    | --- | --- |
    | cb | Pointer to a callback structure. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ENOSYS | If function [smbus\_smbalert\_set\_cb()](#gadff533a6bc198815ee56d03a36b949e0) is not implemented by the driver. |

## [◆ ](#ga72a789110c7286a51c5cd5e2215abce1)smbus\_word\_data\_read()

| int smbus\_word\_data\_read | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cmd*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *word* ) |

`#include <[smbus.h](smbus_8h.md)>`

Perform SMBus Word Data Read operation.

This routine provides a generic interface to perform SMBus Word Data Read operation.

Parameters
:   | dev | Pointer to the device structure for the SMBus driver instance. |
    | --- | --- |
    | addr | Address of the SMBus peripheral device. |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | Command byte which is sent to peripheral device first. |
    | word | Word (16-bit) received from the peripheral device. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ENOSYS | If function [smbus\_word\_data\_read()](#ga72a789110c7286a51c5cd5e2215abce1) is not implemented by the driver. |

## [◆ ](#gade05f9bbbba609832df91fe804dd5d3c)smbus\_word\_data\_write()

| int smbus\_word\_data\_write | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *cmd*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *word* ) |

`#include <[smbus.h](smbus_8h.md)>`

Perform SMBus Word Data Write operation.

This routine provides a generic interface to perform SMBus Word Data Write operation.

Parameters
:   | dev | Pointer to the device structure for the SMBus driver instance. |
    | --- | --- |
    | addr | Address of the SMBus peripheral device. |
    | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615 "Execute a display list command by co-processor engine.") | Command byte which is sent to peripheral device first. |
    | word | Word (16-bit) to be sent to the peripheral device. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input / output error. |
    | -ENOSYS | If function [smbus\_word\_data\_write()](#gade05f9bbbba609832df91fe804dd5d3c) is not implemented by the driver. |

## [◆ ](#ga0a63b800c14f5831730372b9bad41864)smbus\_xfer\_stats()

| | void smbus\_xfer\_stats | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *sent*, | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *recv* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[smbus.h](smbus_8h.md)>`

Updates the SMBus stats.

Parameters
:   | dev | Pointer to the device structure for the SMBus driver instance to update stats for. |
    | --- | --- |
    | sent | Number of bytes sent |
    | [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40 "POSIX wrapper for zsock_recv.") | Number of bytes received |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
