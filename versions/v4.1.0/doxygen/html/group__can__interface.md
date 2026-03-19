---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__can__interface.html
original_path: doxygen/html/group__can__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

CAN Interface

[Device Driver APIs](group__io__interfaces.md)

CAN Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [can\_frame](structcan__frame.md) |
|  | CAN frame structure. [More...](structcan__frame.md#details) |
| struct | [can\_filter](structcan__filter.md) |
|  | CAN filter structure. [More...](structcan__filter.md#details) |
| struct | [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) |
|  | CAN controller error counters. [More...](structcan__bus__err__cnt.md#details) |
| struct | [can\_timing](structcan__timing.md) |
|  | CAN bus timing structure. [More...](structcan__timing.md#details) |
| struct | [can\_device\_state](structcan__device__state.md) |
|  | CAN specific device state which allows for CAN device class specific additions. [More...](structcan__device__state.md#details) |

| Macros | |
| --- | --- |
| #define | [CAN\_STATS\_BIT\_ERROR\_INC](#gaf6f7efa9d99f44af6f58352f558d7fec)(dev\_) |
|  | Increment the bit error counter for a CAN device. |
| #define | [CAN\_STATS\_BIT0\_ERROR\_INC](#ga120a37d5ae5064dcbf116e488f733764)(dev\_) |
|  | Increment the bit0 error counter for a CAN device. |
| #define | [CAN\_STATS\_BIT1\_ERROR\_INC](#ga678b74039632302efcb5ef80f0e3a90b)(dev\_) |
|  | Increment the bit1 (recessive) error counter for a CAN device. |
| #define | [CAN\_STATS\_STUFF\_ERROR\_INC](#gae4146843944b7ffb1c96636e889282f7)(dev\_) |
|  | Increment the stuffing error counter for a CAN device. |
| #define | [CAN\_STATS\_CRC\_ERROR\_INC](#ga125ce05d40881476f5f156ad5e28c664)(dev\_) |
|  | Increment the CRC error counter for a CAN device. |
| #define | [CAN\_STATS\_FORM\_ERROR\_INC](#gac5809b3f5e1a463822e76921cddc9909)(dev\_) |
|  | Increment the form error counter for a CAN device. |
| #define | [CAN\_STATS\_ACK\_ERROR\_INC](#ga15f7ca18badbbe2fe24be68cacce6171)(dev\_) |
|  | Increment the acknowledge error counter for a CAN device. |
| #define | [CAN\_STATS\_RX\_OVERRUN\_INC](#ga95fe455780b38c7202b48bc6004e6f4d)(dev\_) |
|  | Increment the RX overrun counter for a CAN device. |
| #define | [CAN\_STATS\_RESET](#ga06a9058924901e2d960858fb9e3a4a02)(dev\_) |
|  | Zero all statistics for a CAN device. |
| #define | [CAN\_DEVICE\_DT\_DEFINE](#ga599d0695abe481411660d7af2893f4a5)(node\_id, init\_fn, pm, data, config, level, prio, api, ...) |
|  | Like [DEVICE\_DT\_DEFINE()](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1 "Create a device object from a devicetree node identifier and set it up for boot time initialization.") with CAN device specifics. |
| #define | [CAN\_DEVICE\_DT\_INST\_DEFINE](#ga20266dc5e962922144e078b85ccb8351)(inst, ...) |
|  | Like [CAN\_DEVICE\_DT\_DEFINE()](#ga599d0695abe481411660d7af2893f4a5) for an instance of a DT\_DRV\_COMPAT compatible. |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_mode\_t](#ga0b2a1456e66f4522a30cf1400fdfced7) |
|  | Provides a type to hold CAN controller configuration flags. |
| typedef void(\* | [can\_tx\_callback\_t](#gab3675297d3e528bf19e2072f6a84bfca)) (const struct [device](structdevice.md) \*dev, int error, void \*user\_data) |
|  | Defines the application callback handler function signature. |
| typedef void(\* | [can\_rx\_callback\_t](#gaab9525fafab78c0da0a78a2dae39bd6f)) (const struct [device](structdevice.md) \*dev, struct [can\_frame](structcan__frame.md) \*frame, void \*user\_data) |
|  | Defines the application callback handler function signature for receiving. |
| typedef void(\* | [can\_state\_change\_callback\_t](#ga002ff7ba1f5be374510a902459dd9d3d)) (const struct [device](structdevice.md) \*dev, enum [can\_state](#gac7ec472c26c564dd7067c49f67c8d2f7) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) err\_cnt, void \*user\_data) |
|  | Defines the state change callback handler function signature. |

| Enumerations | |
| --- | --- |
| enum | [can\_state](#gac7ec472c26c564dd7067c49f67c8d2f7) {     [CAN\_STATE\_ERROR\_ACTIVE](#ggac7ec472c26c564dd7067c49f67c8d2f7a026154ef3a7f9cb633e43ab7e63d769c) , [CAN\_STATE\_ERROR\_WARNING](#ggac7ec472c26c564dd7067c49f67c8d2f7a15263a89961afbc4e813c7ccfc59e5ff) , [CAN\_STATE\_ERROR\_PASSIVE](#ggac7ec472c26c564dd7067c49f67c8d2f7ac2cd08cde738273c5e5df8306c48d8ae) , [CAN\_STATE\_BUS\_OFF](#ggac7ec472c26c564dd7067c49f67c8d2f7a679935a8710667fcb99423d217cd9959) ,     [CAN\_STATE\_STOPPED](#ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8)   } |
|  | Defines the state of the CAN controller. [More...](#gac7ec472c26c564dd7067c49f67c8d2f7) |

| CAN controller configuration | |
| --- | --- |
| int | [can\_get\_core\_clock](#ga4af6d0d9ab72b195909f511ac65cb8fa) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate) |
|  | Get the CAN core clock rate. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_get\_bitrate\_min](#ga343456749eec6144a91bacae0d94b114) (const struct [device](structdevice.md) \*dev) |
|  | Get minimum supported bitrate. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_get\_bitrate\_max](#ga1e6dc8026e4d922bce4d398d9f32a457) (const struct [device](structdevice.md) \*dev) |
|  | Get maximum supported bitrate. |
| const struct [can\_timing](structcan__timing.md) \* | [can\_get\_timing\_min](#ga5a57627de4764f0bd3b4bafe07f56e6f) (const struct [device](structdevice.md) \*dev) |
|  | Get the minimum supported timing parameter values. |
| const struct [can\_timing](structcan__timing.md) \* | [can\_get\_timing\_max](#gabe385d0f003b1e990c78ef7a2a3f9616) (const struct [device](structdevice.md) \*dev) |
|  | Get the maximum supported timing parameter values. |
| int | [can\_calc\_timing](#gac27fe64142603f0d32d422594356b2d7) (const struct [device](structdevice.md) \*dev, struct [can\_timing](structcan__timing.md) \*res, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sample\_pnt) |
|  | Calculate timing parameters from bitrate and sample point. |
| const struct [can\_timing](structcan__timing.md) \* | [can\_get\_timing\_data\_min](#ga6399ef0cefdab3da738136f8a5c59c2f) (const struct [device](structdevice.md) \*dev) |
|  | Get the minimum supported timing parameter values for the data phase. |
| const struct [can\_timing](structcan__timing.md) \* | [can\_get\_timing\_data\_max](#ga47a2f6d6b42121b390aa92160c833b80) (const struct [device](structdevice.md) \*dev) |
|  | Get the maximum supported timing parameter values for the data phase. |
| int | [can\_calc\_timing\_data](#ga358cd73ed59c2099f4b2c6ceb397ca11) (const struct [device](structdevice.md) \*dev, struct [can\_timing](structcan__timing.md) \*res, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sample\_pnt) |
|  | Calculate timing parameters for the data phase. |
| int | [can\_set\_timing\_data](#ga606cf9fda4c66a0f4abf74e1d357eac2) (const struct [device](structdevice.md) \*dev, const struct [can\_timing](structcan__timing.md) \*timing\_data) |
|  | Configure the bus timing for the data phase of a CAN FD controller. |
| int | [can\_set\_bitrate\_data](#ga0afd2c446fc5e685370641a1678f87b7) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate\_data) |
|  | Set the bitrate for the data phase of the CAN FD controller. |
| int | [can\_set\_timing](#ga1b134af5d6286ea0fee130b6da5217da) (const struct [device](structdevice.md) \*dev, const struct [can\_timing](structcan__timing.md) \*timing) |
|  | Configure the bus timing of a CAN controller. |
| int | [can\_get\_capabilities](#ga4afd7776c5039dec8acb089499dc1168) (const struct [device](structdevice.md) \*dev, [can\_mode\_t](#ga0b2a1456e66f4522a30cf1400fdfced7) \*cap) |
|  | Get the supported modes of the CAN controller. |
| const struct [device](structdevice.md) \* | [can\_get\_transceiver](#gae012d26711c2a7ce1419d21c38cae63a) (const struct [device](structdevice.md) \*dev) |
|  | Get the CAN transceiver associated with the CAN controller. |
| int | [can\_start](#gae48dfa8bc5b52f233b9b1a08aac2675a) (const struct [device](structdevice.md) \*dev) |
|  | Start the CAN controller. |
| int | [can\_stop](#ga1b0ac9185341cb0bde85ec64e4c490a5) (const struct [device](structdevice.md) \*dev) |
|  | Stop the CAN controller. |
| int | [can\_set\_mode](#gae04c3c884b3ed26dfea4745b7dff2c5f) (const struct [device](structdevice.md) \*dev, [can\_mode\_t](#ga0b2a1456e66f4522a30cf1400fdfced7) mode) |
|  | Set the CAN controller to the given operation mode. |
| [can\_mode\_t](#ga0b2a1456e66f4522a30cf1400fdfced7) | [can\_get\_mode](#gabd201b5b1fca54048985a8a24dd51e55) (const struct [device](structdevice.md) \*dev) |
|  | Get the operation mode of the CAN controller. |
| int | [can\_set\_bitrate](#ga0685ebfacfb79d33131167ac3aaa6f9b) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate) |
|  | Set the bitrate of the CAN controller. |

| Transmitting CAN frames | |
| --- | --- |
| int | [can\_send](#ga446ee31913699de3c80be05d837b5fd5) (const struct [device](structdevice.md) \*dev, const struct [can\_frame](structcan__frame.md) \*frame, [k\_timeout\_t](structk__timeout__t.md) timeout, [can\_tx\_callback\_t](#gab3675297d3e528bf19e2072f6a84bfca) callback, void \*user\_data) |
|  | Queue a CAN frame for transmission on the CAN bus. |

| Receiving CAN frames | |
| --- | --- |
| int | [can\_add\_rx\_filter](#gae9dd69a13b960f773ab07bb0bb13b5e9) (const struct [device](structdevice.md) \*dev, [can\_rx\_callback\_t](#gaab9525fafab78c0da0a78a2dae39bd6f) callback, void \*user\_data, const struct [can\_filter](structcan__filter.md) \*filter) |
|  | Add a callback function for a given CAN filter. |
| int | [can\_add\_rx\_filter\_msgq](#gaaac20a068b7f32d2f38d1601d588b35c) (const struct [device](structdevice.md) \*dev, struct [k\_msgq](structk__msgq.md) \*msgq, const struct [can\_filter](structcan__filter.md) \*filter) |
|  | Simple wrapper function for adding a message queue for a given filter. |
| void | [can\_remove\_rx\_filter](#ga822aa3142ea01582d5cfb8b478fb2847) (const struct [device](structdevice.md) \*dev, int filter\_id) |
|  | Remove a CAN RX filter. |
| int | [can\_get\_max\_filters](#ga526c08539094486f07dc52aad8ed0dcc) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ide) |
|  | Get maximum number of RX filters. |
| #define | [CAN\_MSGQ\_DEFINE](#ga7af0acdfbdad07fc3eba4cbd29bc090b)(name, max\_frames) |
|  | Statically define and initialize a CAN RX message queue. |

| CAN bus error reporting and handling | |
| --- | --- |
| int | [can\_get\_state](#gab98c121578c8349d9dfb41d60f356857) (const struct [device](structdevice.md) \*dev, enum [can\_state](#gac7ec472c26c564dd7067c49f67c8d2f7) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*err\_cnt) |
|  | Get current CAN controller state. |
| int | [can\_recover](#gac474e56a50685736a1c25dca277aab5e) (const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Recover from bus-off state. |
| static void | [can\_set\_state\_change\_callback](#gad322da0dad328abb50de23bef6882d8e) (const struct [device](structdevice.md) \*dev, [can\_state\_change\_callback\_t](#ga002ff7ba1f5be374510a902459dd9d3d) callback, void \*user\_data) |
|  | Set a callback for CAN controller state change events. |

| CAN statistics | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_stats\_get\_bit\_errors](#ga27b277f3b5146590f159171f602904db) (const struct [device](structdevice.md) \*dev) |
|  | Get the bit error counter for a CAN device. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_stats\_get\_bit0\_errors](#ga7c380f6c4a529e5b5e6010ab4e6c7680) (const struct [device](structdevice.md) \*dev) |
|  | Get the bit0 error counter for a CAN device. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_stats\_get\_bit1\_errors](#ga4c7d40951a2ae6eaa72e5d1f7a26ac75) (const struct [device](structdevice.md) \*dev) |
|  | Get the bit1 error counter for a CAN device. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_stats\_get\_stuff\_errors](#ga162fde4e622fb06dcbbcf2f31bb35d38) (const struct [device](structdevice.md) \*dev) |
|  | Get the stuffing error counter for a CAN device. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_stats\_get\_crc\_errors](#ga31692aef7962172532f8200fed7aecd2) (const struct [device](structdevice.md) \*dev) |
|  | Get the CRC error counter for a CAN device. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_stats\_get\_form\_errors](#gabf9ce221f4f6a8dbaafcff9b7a5c5a10) (const struct [device](structdevice.md) \*dev) |
|  | Get the form error counter for a CAN device. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_stats\_get\_ack\_errors](#ga4f8414d64b75d4d1ffb7a0feff36f698) (const struct [device](structdevice.md) \*dev) |
|  | Get the acknowledge error counter for a CAN device. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_stats\_get\_rx\_overruns](#ga8664fbaa13f4bb89540493264d2a041d) (const struct [device](structdevice.md) \*dev) |
|  | Get the RX overrun counter for a CAN device. |

| CAN utility functions | |
| --- | --- |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [can\_dlc\_to\_bytes](#gaa1d866167c0c23f8d5c0c15385589601) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dlc) |
|  | Convert from Data Length Code (DLC) to the number of data bytes. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [can\_bytes\_to\_dlc](#ga8314716fe2b66d567b3fd377b8ee9dc3) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_bytes) |
|  | Convert from number of bytes to Data Length Code (DLC). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [can\_frame\_matches\_filter](#gaafc54ac799e3a3a098a9f6941d7f2ea8) (const struct [can\_frame](structcan__frame.md) \*frame, const struct [can\_filter](structcan__filter.md) \*filter) |
|  | Check if a CAN frame matches a CAN filter. |

| CAN frame definitions | |
| --- | --- |
| #define | [CAN\_STD\_ID\_MASK](#ga4cd8ce34887b90baeeaa6a4aa048b398)   0x7FFU |
|  | Bit mask for a standard (11-bit) CAN identifier. |
| #define | [CAN\_EXT\_ID\_MASK](#ga15ee71e8abcf51008925585049125986)   0x1FFFFFFFU |
|  | Bit mask for an extended (29-bit) CAN identifier. |
| #define | [CAN\_MAX\_DLC](#gadc209a027ee700faf10461e2417bee50)   8U |
|  | Maximum data length code for CAN 2.0A/2.0B. |
| #define | [CANFD\_MAX\_DLC](#gad4b7310536c7e3252c2056abe64c0333)   15U |
|  | Maximum data length code for CAN FD. |

| CAN controller mode flags | |
| --- | --- |
|  | |
| #define | [CAN\_MODE\_NORMAL](#ga89cd5ea2e9d70a51bc12b100be28ca3d)   0 |
|  | Normal mode. |
| #define | [CAN\_MODE\_LOOPBACK](#ga891031afc77974a041accb3d0ceb21bb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Controller is in loopback mode (receives own frames). |
| #define | [CAN\_MODE\_LISTENONLY](#ga117d04b9118a1b3f839c557ef6b596cb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Controller is not allowed to send dominant bits. |
| #define | [CAN\_MODE\_FD](#gabb4d99736d8386a5ab62a5e44374d13a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Controller allows transmitting/receiving CAN FD frames. |
| #define | [CAN\_MODE\_ONE\_SHOT](#ga033d7ade1966299c7e6249b945f38202)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Controller does not retransmit in case of lost arbitration or missing ACK. |
| #define | [CAN\_MODE\_3\_SAMPLES](#gaf0821983174ad781e1bb63a976a18fab)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Controller uses triple sampling mode. |
| #define | [CAN\_MODE\_MANUAL\_RECOVERY](#ga3d8675253125b2af2bd22f0b2cc60cdd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Controller requires manual recovery after entering bus-off state. |

| CAN frame flags | |
| --- | --- |
|  | |
| #define | [CAN\_FRAME\_IDE](#ga9ed5a06a97db2c955a7db4b6e386d5e3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Frame uses extended (29-bit) CAN ID. |
| #define | [CAN\_FRAME\_RTR](#gaed376ef16b84cd1974255fbb26dc3d7f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Frame is a Remote Transmission Request (RTR). |
| #define | [CAN\_FRAME\_FDF](#ga22f85e1d16b93e46200f9673abdbb589)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Frame uses CAN FD format (FDF). |
| #define | [CAN\_FRAME\_BRS](#ga1fdf15ce4a3b333488f9b630ec836d52)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Frame uses CAN FD Baud Rate Switch (BRS). |
| #define | [CAN\_FRAME\_ESI](#ga83f8b7af6eb45e43aaac355de3e69e52)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | CAN FD Error State Indicator (ESI). |

| CAN filter flags | |
| --- | --- |
|  | |
| #define | [CAN\_FILTER\_IDE](#gafa40c165d016955ec0c856a7fd53168f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Filter matches frames with extended (29-bit) CAN IDs. |

## Detailed Description

CAN Interface.

Since
:   1.12

Version
:   1.1.0

## Macro Definition Documentation

## [◆ ](#ga599d0695abe481411660d7af2893f4a5)CAN\_DEVICE\_DT\_DEFINE

| #define CAN\_DEVICE\_DT\_DEFINE | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *init\_fn*, |
|  |  |  | *pm*, |
|  |  |  | *data*, |
|  |  |  | *config*, |
|  |  |  | *level*, |
|  |  |  | *prio*, |
|  |  |  | *api*, |
|  |  |  | ... ) |

`#include <[can.h](drivers_2can_8h.md)>`

**Value:**

Z\_CAN\_DEVICE\_STATE\_DEFINE(Z\_DEVICE\_DT\_DEV\_ID(node\_id)); \

Z\_CAN\_INIT\_FN(Z\_DEVICE\_DT\_DEV\_ID(node\_id), init\_fn) \

Z\_DEVICE\_DEFINE(node\_id, Z\_DEVICE\_DT\_DEV\_ID(node\_id), \

[DEVICE\_DT\_NAME](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)(node\_id), \

&[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(Z\_DEVICE\_DT\_DEV\_ID(node\_id), \_init), \

pm, data, config, level, prio, api, \

&(Z\_DEVICE\_STATE\_NAME(Z\_DEVICE\_DT\_DEV\_ID(node\_id)).devstate), \

\_\_VA\_ARGS\_\_)

[DEVICE\_DT\_NAME](group__device__model.md#gad864d7a50ee45285dacd68be1e5a49ce)

#define DEVICE\_DT\_NAME(node\_id)

Return a string name for a devicetree node.

**Definition** device.h:185

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)

#define UTIL\_CAT(a,...)

**Definition** util\_internal.h:104

Like [DEVICE\_DT\_DEFINE()](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1 "Create a device object from a devicetree node identifier and set it up for boot time initialization.") with CAN device specifics.

Defines a device which implements the CAN API. May generate a custom [device\_state](structdevice__state.md "Runtime device dynamic structure (in RAM) per driver instance.") container struct and init\_fn wrapper when needed depending on `CONFIG_CAN_STATS`.

Parameters
:   | node\_id | The devicetree node identifier. |
    | --- | --- |
    | init\_fn | Name of the init function of the driver. |
    | pm | PM device resources reference (NULL if device does not use PM). |
    | data | Pointer to the device's private data. |
    | config | The address to the structure containing the configuration information for this instance of the driver. |
    | level | The initialization level. See [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") for details. |
    | prio | Priority within the selected initialization level. See [SYS\_INIT()](group__sys__init.md#gaf507cc0613add8113c41896bd631254f "Register an initialization function.") for details. |
    | api | Provides an initial pointer to the API function struct used by the driver. Can be NULL. |

## [◆ ](#ga20266dc5e962922144e078b85ccb8351)CAN\_DEVICE\_DT\_INST\_DEFINE

| #define CAN\_DEVICE\_DT\_INST\_DEFINE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[can.h](drivers_2can_8h.md)>`

**Value:**

[CAN\_DEVICE\_DT\_DEFINE](#ga599d0695abe481411660d7af2893f4a5)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), \_\_VA\_ARGS\_\_)

[CAN\_DEVICE\_DT\_DEFINE](#ga599d0695abe481411660d7af2893f4a5)

#define CAN\_DEVICE\_DT\_DEFINE(node\_id, init\_fn, pm, data, config, level, prio, api,...)

Like DEVICE\_DT\_DEFINE() with CAN device specifics.

**Definition** can.h:757

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3909

Like [CAN\_DEVICE\_DT\_DEFINE()](#ga599d0695abe481411660d7af2893f4a5) for an instance of a DT\_DRV\_COMPAT compatible.

Parameters
:   | inst | Instance number. This is replaced by DT\_DRV\_COMPAT(inst) in the call to [CAN\_DEVICE\_DT\_DEFINE()](#ga599d0695abe481411660d7af2893f4a5). |
    | --- | --- |
    | ... | Other parameters as expected by [CAN\_DEVICE\_DT\_DEFINE()](#ga599d0695abe481411660d7af2893f4a5). |

## [◆ ](#ga15ee71e8abcf51008925585049125986)CAN\_EXT\_ID\_MASK

| #define CAN\_EXT\_ID\_MASK   0x1FFFFFFFU |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Bit mask for an extended (29-bit) CAN identifier.

## [◆ ](#gafa40c165d016955ec0c856a7fd53168f)CAN\_FILTER\_IDE

| #define CAN\_FILTER\_IDE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Filter matches frames with extended (29-bit) CAN IDs.

## [◆ ](#ga1fdf15ce4a3b333488f9b630ec836d52)CAN\_FRAME\_BRS

| #define CAN\_FRAME\_BRS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Frame uses CAN FD Baud Rate Switch (BRS).

Only valid in combination with [CAN\_FRAME\_FDF](#ga22f85e1d16b93e46200f9673abdbb589).

## [◆ ](#ga83f8b7af6eb45e43aaac355de3e69e52)CAN\_FRAME\_ESI

| #define CAN\_FRAME\_ESI   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

CAN FD Error State Indicator (ESI).

Indicates that the transmitting node is in error-passive state. Only valid in combination with [CAN\_FRAME\_FDF](#ga22f85e1d16b93e46200f9673abdbb589).

## [◆ ](#ga22f85e1d16b93e46200f9673abdbb589)CAN\_FRAME\_FDF

| #define CAN\_FRAME\_FDF   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Frame uses CAN FD format (FDF).

## [◆ ](#ga9ed5a06a97db2c955a7db4b6e386d5e3)CAN\_FRAME\_IDE

| #define CAN\_FRAME\_IDE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Frame uses extended (29-bit) CAN ID.

## [◆ ](#gaed376ef16b84cd1974255fbb26dc3d7f)CAN\_FRAME\_RTR

| #define CAN\_FRAME\_RTR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Frame is a Remote Transmission Request (RTR).

## [◆ ](#gadc209a027ee700faf10461e2417bee50)CAN\_MAX\_DLC

| #define CAN\_MAX\_DLC   8U |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Maximum data length code for CAN 2.0A/2.0B.

## [◆ ](#gaf0821983174ad781e1bb63a976a18fab)CAN\_MODE\_3\_SAMPLES

| #define CAN\_MODE\_3\_SAMPLES   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Controller uses triple sampling mode.

## [◆ ](#gabb4d99736d8386a5ab62a5e44374d13a)CAN\_MODE\_FD

| #define CAN\_MODE\_FD   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Controller allows transmitting/receiving CAN FD frames.

## [◆ ](#ga117d04b9118a1b3f839c557ef6b596cb)CAN\_MODE\_LISTENONLY

| #define CAN\_MODE\_LISTENONLY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Controller is not allowed to send dominant bits.

## [◆ ](#ga891031afc77974a041accb3d0ceb21bb)CAN\_MODE\_LOOPBACK

| #define CAN\_MODE\_LOOPBACK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Controller is in loopback mode (receives own frames).

## [◆ ](#ga3d8675253125b2af2bd22f0b2cc60cdd)CAN\_MODE\_MANUAL\_RECOVERY

| #define CAN\_MODE\_MANUAL\_RECOVERY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Controller requires manual recovery after entering bus-off state.

## [◆ ](#ga89cd5ea2e9d70a51bc12b100be28ca3d)CAN\_MODE\_NORMAL

| #define CAN\_MODE\_NORMAL   0 |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Normal mode.

## [◆ ](#ga033d7ade1966299c7e6249b945f38202)CAN\_MODE\_ONE\_SHOT

| #define CAN\_MODE\_ONE\_SHOT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Controller does not retransmit in case of lost arbitration or missing ACK.

## [◆ ](#ga7af0acdfbdad07fc3eba4cbd29bc090b)CAN\_MSGQ\_DEFINE

| #define CAN\_MSGQ\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *max\_frames* ) |

`#include <[can.h](drivers_2can_8h.md)>`

**Value:**

[K\_MSGQ\_DEFINE](group__msgq__apis.md#ga95ef93002766901511d09c8cd8f8293b)(name, sizeof(struct [can\_frame](structcan__frame.md)), max\_frames, 4)

[K\_MSGQ\_DEFINE](group__msgq__apis.md#ga95ef93002766901511d09c8cd8f8293b)

#define K\_MSGQ\_DEFINE(q\_name, q\_msg\_size, q\_max\_msgs, q\_align)

Statically define and initialize a message queue.

**Definition** kernel.h:4639

[can\_frame](structcan__frame.md)

CAN frame structure.

**Definition** can.h:163

Statically define and initialize a CAN RX message queue.

The message queue's ring buffer contains space for *max\_frames* CAN frames.

See also
:   [can\_add\_rx\_filter\_msgq()](#gaaac20a068b7f32d2f38d1601d588b35c)

Parameters
:   | name | Name of the message queue. |
    | --- | --- |
    | max\_frames | Maximum number of CAN frames that can be queued. |

## [◆ ](#ga15f7ca18badbbe2fe24be68cacce6171)CAN\_STATS\_ACK\_ERROR\_INC

| #define CAN\_STATS\_ACK\_ERROR\_INC | ( |  | *dev\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

**Value:**

[STATS\_INC](stats_2stats_8h.md#a725e1bf6b2c486de9603954974d6315a)(Z\_CAN\_GET\_STATS(dev\_), ack\_error)

[STATS\_INC](stats_2stats_8h.md#a725e1bf6b2c486de9603954974d6315a)

#define STATS\_INC(group\_\_, var\_\_)

**Definition** stats.h:364

Increment the acknowledge error counter for a CAN device.

The acknowledge error counter is incremented when the CAN controller does not monitor a dominant bit in the ACK slot.

Parameters
:   | dev\_ | Pointer to the device structure for the driver instance. |
    | --- | --- |

## [◆ ](#ga120a37d5ae5064dcbf116e488f733764)CAN\_STATS\_BIT0\_ERROR\_INC

| #define CAN\_STATS\_BIT0\_ERROR\_INC | ( |  | *dev\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

**Value:**

do { \

STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), bit0\_error); \

CAN\_STATS\_BIT\_ERROR\_INC(dev\_); \

} while (0)

Increment the bit0 error counter for a CAN device.

The bit0 error counter is incremented when the CAN controller is unable to transmit a dominant bit.

Incrementing this counter will automatically increment the bit error counter.

See also
:   [CAN\_STATS\_BIT\_ERROR\_INC()](#gaf6f7efa9d99f44af6f58352f558d7fec)

Parameters
:   | dev\_ | Pointer to the device structure for the driver instance. |
    | --- | --- |

## [◆ ](#ga678b74039632302efcb5ef80f0e3a90b)CAN\_STATS\_BIT1\_ERROR\_INC

| #define CAN\_STATS\_BIT1\_ERROR\_INC | ( |  | *dev\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

**Value:**

do { \

STATS\_INC(Z\_CAN\_GET\_STATS(dev\_), bit1\_error); \

CAN\_STATS\_BIT\_ERROR\_INC(dev\_); \

} while (0)

Increment the bit1 (recessive) error counter for a CAN device.

The bit1 error counter is incremented when the CAN controller is unable to transmit a recessive bit.

Incrementing this counter will automatically increment the bit error counter.

See also
:   [CAN\_STATS\_BIT\_ERROR\_INC()](#gaf6f7efa9d99f44af6f58352f558d7fec)

Parameters
:   | dev\_ | Pointer to the device structure for the driver instance. |
    | --- | --- |

## [◆ ](#gaf6f7efa9d99f44af6f58352f558d7fec)CAN\_STATS\_BIT\_ERROR\_INC

| #define CAN\_STATS\_BIT\_ERROR\_INC | ( |  | *dev\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

**Value:**

[STATS\_INC](stats_2stats_8h.md#a725e1bf6b2c486de9603954974d6315a)(Z\_CAN\_GET\_STATS(dev\_), bit\_error)

Increment the bit error counter for a CAN device.

The bit error counter is incremented when the CAN controller is unable to transmit either a dominant or a recessive bit.

Note
:   This error counter should only be incremented if the CAN controller is unable to distinguish between failure to transmit a dominant versus failure to transmit a recessive bit. If the CAN controller supports distinguishing between the two, the bit0 or bit1 error counter shall be incremented instead.

See also
:   [CAN\_STATS\_BIT0\_ERROR\_INC()](#ga120a37d5ae5064dcbf116e488f733764)
:   [CAN\_STATS\_BIT1\_ERROR\_INC()](#ga678b74039632302efcb5ef80f0e3a90b)

Parameters
:   | dev\_ | Pointer to the device structure for the driver instance. |
    | --- | --- |

## [◆ ](#ga125ce05d40881476f5f156ad5e28c664)CAN\_STATS\_CRC\_ERROR\_INC

| #define CAN\_STATS\_CRC\_ERROR\_INC | ( |  | *dev\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

**Value:**

[STATS\_INC](stats_2stats_8h.md#a725e1bf6b2c486de9603954974d6315a)(Z\_CAN\_GET\_STATS(dev\_), crc\_error)

Increment the CRC error counter for a CAN device.

The CRC error counter is incremented when the CAN controller detects a frame with an invalid CRC.

Parameters
:   | dev\_ | Pointer to the device structure for the driver instance. |
    | --- | --- |

## [◆ ](#gac5809b3f5e1a463822e76921cddc9909)CAN\_STATS\_FORM\_ERROR\_INC

| #define CAN\_STATS\_FORM\_ERROR\_INC | ( |  | *dev\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

**Value:**

[STATS\_INC](stats_2stats_8h.md#a725e1bf6b2c486de9603954974d6315a)(Z\_CAN\_GET\_STATS(dev\_), form\_error)

Increment the form error counter for a CAN device.

The form error counter is incremented when the CAN controller detects a fixed-form bit field containing illegal bits.

Parameters
:   | dev\_ | Pointer to the device structure for the driver instance. |
    | --- | --- |

## [◆ ](#ga06a9058924901e2d960858fb9e3a4a02)CAN\_STATS\_RESET

| #define CAN\_STATS\_RESET | ( |  | *dev\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

**Value:**

stats\_reset(&(Z\_CAN\_GET\_STATS(dev\_).s\_hdr))

Zero all statistics for a CAN device.

The driver is responsible for resetting the statistics before starting the CAN controller.

Parameters
:   | dev\_ | Pointer to the device structure for the driver instance. |
    | --- | --- |

## [◆ ](#ga95fe455780b38c7202b48bc6004e6f4d)CAN\_STATS\_RX\_OVERRUN\_INC

| #define CAN\_STATS\_RX\_OVERRUN\_INC | ( |  | *dev\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

**Value:**

[STATS\_INC](stats_2stats_8h.md#a725e1bf6b2c486de9603954974d6315a)(Z\_CAN\_GET\_STATS(dev\_), rx\_overrun)

Increment the RX overrun counter for a CAN device.

The RX overrun counter is incremented when the CAN controller receives a CAN frame matching an installed filter but lacks the capacity to store it (either due to an already full RX mailbox or a full RX FIFO).

Parameters
:   | dev\_ | Pointer to the device structure for the driver instance. |
    | --- | --- |

## [◆ ](#gae4146843944b7ffb1c96636e889282f7)CAN\_STATS\_STUFF\_ERROR\_INC

| #define CAN\_STATS\_STUFF\_ERROR\_INC | ( |  | *dev\_* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

**Value:**

[STATS\_INC](stats_2stats_8h.md#a725e1bf6b2c486de9603954974d6315a)(Z\_CAN\_GET\_STATS(dev\_), stuff\_error)

Increment the stuffing error counter for a CAN device.

The stuffing error counter is incremented when the CAN controller detects a bit stuffing error.

Parameters
:   | dev\_ | Pointer to the device structure for the driver instance. |
    | --- | --- |

## [◆ ](#ga4cd8ce34887b90baeeaa6a4aa048b398)CAN\_STD\_ID\_MASK

| #define CAN\_STD\_ID\_MASK   0x7FFU |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Bit mask for a standard (11-bit) CAN identifier.

## [◆ ](#gad4b7310536c7e3252c2056abe64c0333)CANFD\_MAX\_DLC

| #define CANFD\_MAX\_DLC   15U |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Maximum data length code for CAN FD.

## Typedef Documentation

## [◆ ](#ga0b2a1456e66f4522a30cf1400fdfced7)can\_mode\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [can\_mode\_t](#ga0b2a1456e66f4522a30cf1400fdfced7) |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Provides a type to hold CAN controller configuration flags.

The lower 24 bits are reserved for common CAN controller mode flags. The upper 8 bits are reserved for CAN controller/driver specific flags.

See also
:   [CAN\_MODE\_FLAGS](#CAN_MODE_FLAGS).

## [◆ ](#gaab9525fafab78c0da0a78a2dae39bd6f)can\_rx\_callback\_t

| typedef void(\* can\_rx\_callback\_t) (const struct [device](structdevice.md) \*dev, struct [can\_frame](structcan__frame.md) \*frame, void \*user\_data) |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Defines the application callback handler function signature for receiving.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | frame | Received frame. |
    | user\_data | User data provided when the filter was added. |

## [◆ ](#ga002ff7ba1f5be374510a902459dd9d3d)can\_state\_change\_callback\_t

| typedef void(\* can\_state\_change\_callback\_t) (const struct [device](structdevice.md) \*dev, enum [can\_state](#gac7ec472c26c564dd7067c49f67c8d2f7) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) err\_cnt, void \*user\_data) |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Defines the state change callback handler function signature.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | State of the CAN controller. |
    | err\_cnt | CAN controller error counter values. |
    | user\_data | User data provided the callback was set. |

## [◆ ](#gab3675297d3e528bf19e2072f6a84bfca)can\_tx\_callback\_t

| typedef void(\* can\_tx\_callback\_t) (const struct [device](structdevice.md) \*dev, int error, void \*user\_data) |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Defines the application callback handler function signature.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | error | Status of the performed send operation. See the list of return values for *[can\_send()](#ga446ee31913699de3c80be05d837b5fd5)* for value descriptions. |
    | user\_data | User data provided when the frame was sent. |

## Enumeration Type Documentation

## [◆ ](#gac7ec472c26c564dd7067c49f67c8d2f7)can\_state

| enum [can\_state](#gac7ec472c26c564dd7067c49f67c8d2f7) |
| --- |

`#include <[can.h](drivers_2can_8h.md)>`

Defines the state of the CAN controller.

| Enumerator | |
| --- | --- |
| CAN\_STATE\_ERROR\_ACTIVE | Error-active state (RX/TX error count < 96). |
| CAN\_STATE\_ERROR\_WARNING | Error-warning state (RX/TX error count < 128). |
| CAN\_STATE\_ERROR\_PASSIVE | Error-passive state (RX/TX error count < 256). |
| CAN\_STATE\_BUS\_OFF | Bus-off state (RX/TX error count >= 256). |
| CAN\_STATE\_STOPPED | CAN controller is stopped and does not participate in CAN communication. |

## Function Documentation

## [◆ ](#gae9dd69a13b960f773ab07bb0bb13b5e9)can\_add\_rx\_filter()

| int can\_add\_rx\_filter | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [can\_rx\_callback\_t](#gaab9525fafab78c0da0a78a2dae39bd6f) | *callback*, |
|  |  | void \* | *user\_data*, |
|  |  | const struct [can\_filter](structcan__filter.md) \* | *filter* ) |

`#include <[can.h](drivers_2can_8h.md)>`

Add a callback function for a given CAN filter.

Add a callback to CAN identifiers specified by a filter. When a received CAN frame matching the filter is received by the CAN controller, the callback function is called in interrupt context.

If a received frame matches more than one filter (i.e., the filter IDs/masks or flags overlap), the priority of the match is hardware dependent.

The same callback function can be used for multiple filters.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | callback | This function is called by the CAN controller driver whenever a frame matching the filter is received. |
    | user\_data | User data to pass to callback function. |
    | filter | Pointer to a *[can\_filter](structcan__filter.md "CAN filter structure.")* structure defining the filter. |

Return values
:   | filter\_id | on success. |
    | --- | --- |
    | -ENOSPC | if there are no free filters. |
    | -EINVAL | if the requested filter type is invalid. |
    | -ENOTSUP | if the requested filter type is not supported. |

## [◆ ](#gaaac20a068b7f32d2f38d1601d588b35c)can\_add\_rx\_filter\_msgq()

| int can\_add\_rx\_filter\_msgq | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [k\_msgq](structk__msgq.md) \* | *msgq*, |
|  |  | const struct [can\_filter](structcan__filter.md) \* | *filter* ) |

`#include <[can.h](drivers_2can_8h.md)>`

Simple wrapper function for adding a message queue for a given filter.

Wrapper function for *[can\_add\_rx\_filter()](#gae9dd69a13b960f773ab07bb0bb13b5e9)* which puts received CAN frames matching the filter in a message queue instead of calling a callback.

If a received frame matches more than one filter (i.e., the filter IDs/masks or flags overlap), the priority of the match is hardware dependent.

The same message queue can be used for multiple filters.

Note
:   The message queue must be initialized before calling this function and the caller must have appropriate permissions on it.

Warning
:   Message queue overruns are silently ignored and overrun frames discarded. Custom error handling can be implemented by using *[can\_add\_rx\_filter()](#gae9dd69a13b960f773ab07bb0bb13b5e9)* and *[k\_msgq\_put()](group__msgq__apis.md#ga54e96aaaea5462a1f963b7fd5ca82bfe "Send a message to a message queue.")* directly.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | msgq | Pointer to the already initialized *[k\_msgq](structk__msgq.md "Message Queue Structure.")* struct. |
    | filter | Pointer to a *[can\_filter](structcan__filter.md "CAN filter structure.")* structure defining the filter. |

Return values
:   | filter\_id | on success. |
    | --- | --- |
    | -ENOSPC | if there are no free filters. |
    | -ENOTSUP | if the requested filter type is not supported. |

## [◆ ](#ga8314716fe2b66d567b3fd377b8ee9dc3)can\_bytes\_to\_dlc()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_bytes\_to\_dlc | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *num\_bytes* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Convert from number of bytes to Data Length Code (DLC).

Parameters
:   | num\_bytes | Number of bytes. |
    | --- | --- |

Return values
:   | Data | Length Code (DLC). |
    | --- | --- |

## [◆ ](#gac27fe64142603f0d32d422594356b2d7)can\_calc\_timing()

| int can\_calc\_timing | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [can\_timing](structcan__timing.md) \* | *res*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *bitrate*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *sample\_pnt* ) |

`#include <[can.h](drivers_2can_8h.md)>`

Calculate timing parameters from bitrate and sample point.

Calculate the timing parameters from a given bitrate in bits/s and the sampling point in permill (1/1000) of the entire bit time. The bitrate must always match perfectly. If no result can be reached for the given parameters, -EINVAL is returned.

If the sample point is set to 0, this function defaults to a sample point of 75.0% for bitrates over 800 kbit/s, 80.0% for bitrates over 500 kbit/s, and 87.5% for all other bitrates.

Note
:   The requested sample\_pnt will not always be matched perfectly. The algorithm calculates the best possible match.

Parameters
:   |  | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    | [out] | res | Result is written into the *[can\_timing](structcan__timing.md "CAN bus timing structure.")* struct provided. |
    |  | bitrate | Target bitrate in bits/s. |
    |  | sample\_pnt | Sample point in permille of the entire bit time or 0 for automatic sample point location. |

Return values
:   | 0 | or positive sample point error on success. |
    | --- | --- |
    | -EINVAL | if the requested bitrate or sample point is out of range. |
    | -ENOTSUP | if the requested bitrate is not supported. |
    | -EIO | if *[can\_get\_core\_clock()](#ga4af6d0d9ab72b195909f511ac65cb8fa)* is not available. |

## [◆ ](#ga358cd73ed59c2099f4b2c6ceb397ca11)can\_calc\_timing\_data()

| int can\_calc\_timing\_data | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | struct [can\_timing](structcan__timing.md) \* | *res*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *bitrate*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *sample\_pnt* ) |

`#include <[can.h](drivers_2can_8h.md)>`

Calculate timing parameters for the data phase.

Same as *[can\_calc\_timing()](#gac27fe64142603f0d32d422594356b2d7)* but with the maximum and minimum values from the data phase.

Note
:   `CONFIG_CAN_FD_MODE` must be selected for this function to be available.

Parameters
:   |  | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    | [out] | res | Result is written into the *[can\_timing](structcan__timing.md "CAN bus timing structure.")* struct provided. |
    |  | bitrate | Target bitrate for the data phase in bits/s |
    |  | sample\_pnt | Sample point for the data phase in permille of the entire bit time or 0 for automatic sample point location. |

Return values
:   | 0 | or positive sample point error on success. |
    | --- | --- |
    | -EINVAL | if the requested bitrate or sample point is out of range. |
    | -ENOTSUP | if the requested bitrate is not supported. |
    | -EIO | if *[can\_get\_core\_clock()](#ga4af6d0d9ab72b195909f511ac65cb8fa)* is not available. |

## [◆ ](#gaa1d866167c0c23f8d5c0c15385589601)can\_dlc\_to\_bytes()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) can\_dlc\_to\_bytes | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *dlc* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Convert from Data Length Code (DLC) to the number of data bytes.

Parameters
:   | dlc | Data Length Code (DLC). |
    | --- | --- |

Return values
:   | Number | of bytes. |
    | --- | --- |

## [◆ ](#gaafc54ac799e3a3a098a9f6941d7f2ea8)can\_frame\_matches\_filter()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) can\_frame\_matches\_filter | ( | const struct [can\_frame](structcan__frame.md) \* | *frame*, | | --- | --- | --- | --- | |  |  | const struct [can\_filter](structcan__filter.md) \* | *filter* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Check if a CAN frame matches a CAN filter.

Parameters
:   | frame | CAN frame. |
    | --- | --- |
    | filter | CAN filter. |

Returns
:   true if the CAN frame matches the CAN filter, false otherwise

## [◆ ](#ga1e6dc8026e4d922bce4d398d9f32a457)can\_get\_bitrate\_max()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_get\_bitrate\_max | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Get maximum supported bitrate.

Get the maximum supported bitrate for the CAN controller/transceiver combination.

Note
:   The maximum bitrate represents limitations of the CAN controller/transceiver combination. Whether the CAN controller can achieve this bitrate depends on the CAN core clock rate and the maximum CAN timing limits.

See also
:   [can\_get\_core\_clock()](#ga4af6d0d9ab72b195909f511ac65cb8fa)
:   [can\_get\_timing\_max()](#gabe385d0f003b1e990c78ef7a2a3f9616)
:   [can\_get\_timing\_data\_max()](#ga47a2f6d6b42121b390aa92160c833b80)

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   Maximum supported bitrate in bits/s

## [◆ ](#ga343456749eec6144a91bacae0d94b114)can\_get\_bitrate\_min()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_get\_bitrate\_min | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Get minimum supported bitrate.

Get the minimum supported bitrate for the CAN controller/transceiver combination.

Note
:   The minimum bitrate represents limitations of the CAN controller/transceiver combination. Whether the CAN controller can achieve this bitrate depends on the CAN core clock rate and the minimum CAN timing limits.

See also
:   [can\_get\_core\_clock()](#ga4af6d0d9ab72b195909f511ac65cb8fa)
:   [can\_get\_timing\_min()](#ga5a57627de4764f0bd3b4bafe07f56e6f)
:   [can\_get\_timing\_data\_min()](#ga6399ef0cefdab3da738136f8a5c59c2f)

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   Minimum supported bitrate in bits/s. A value of 0 means the lower limit is unspecified.

## [◆ ](#ga4afd7776c5039dec8acb089499dc1168)can\_get\_capabilities()

| int can\_get\_capabilities | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [can\_mode\_t](#ga0b2a1456e66f4522a30cf1400fdfced7) \* | *cap* ) |

`#include <[can.h](drivers_2can_8h.md)>`

Get the supported modes of the CAN controller.

The returned capabilities may not necessarily be supported at the same time (e.g. some CAN controllers support both [CAN\_MODE\_LOOPBACK](#ga891031afc77974a041accb3d0ceb21bb) and [CAN\_MODE\_LISTENONLY](#ga117d04b9118a1b3f839c557ef6b596cb), but not at the same time).

Parameters
:   |  | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    | [out] | cap | Supported capabilities. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input/output error, failed to get capabilities. |

## [◆ ](#ga4af6d0d9ab72b195909f511ac65cb8fa)can\_get\_core\_clock()

| int can\_get\_core\_clock | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *rate* ) |

`#include <[can.h](drivers_2can_8h.md)>`

Get the CAN core clock rate.

Returns the CAN core clock rate. One minimum time quantum (mtq) is 1/(core clock rate). The CAN core clock can be further divided by the CAN clock prescaler (see the *[can\_timing](structcan__timing.md "CAN bus timing structure.")* struct), providing the time quantum (tq).

Parameters
:   |  | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    | [out] | rate | CAN core clock rate in Hz. |

Returns
:   0 on success, or a negative error code on error

## [◆ ](#ga526c08539094486f07dc52aad8ed0dcc)can\_get\_max\_filters()

| int can\_get\_max\_filters | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *ide* ) |

`#include <[can.h](drivers_2can_8h.md)>`

Get maximum number of RX filters.

Get the maximum number of concurrent RX filters for the CAN controller.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | ide | Get the maximum standard (11-bit) CAN ID filters if false, or extended (29-bit) CAN ID filters if true. |

Return values
:   | Positive | number of maximum concurrent filters. |
    | --- | --- |
    | -EIO | General input/output error. |
    | -ENOSYS | If this function is not implemented by the driver. |

## [◆ ](#gabd201b5b1fca54048985a8a24dd51e55)can\_get\_mode()

| [can\_mode\_t](#ga0b2a1456e66f4522a30cf1400fdfced7) can\_get\_mode | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Get the operation mode of the CAN controller.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   Current operation mode.

## [◆ ](#gab98c121578c8349d9dfb41d60f356857)can\_get\_state()

| int can\_get\_state | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | enum [can\_state](#gac7ec472c26c564dd7067c49f67c8d2f7) \* | *state*, |
|  |  | struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \* | *err\_cnt* ) |

`#include <[can.h](drivers_2can_8h.md)>`

Get current CAN controller state.

Returns the current state and optionally the error counter values of the CAN controller.

Parameters
:   |  | dev | Pointer to the device structure for the driver instance. |
    | --- | --- | --- |
    | [out] | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | Pointer to the state destination enum or NULL. |
    | [out] | err\_cnt | Pointer to the err\_cnt destination structure or NULL. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | General input/output error, failed to get state. |

## [◆ ](#ga47a2f6d6b42121b390aa92160c833b80)can\_get\_timing\_data\_max()

| const struct [can\_timing](structcan__timing.md) \* can\_get\_timing\_data\_max | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Get the maximum supported timing parameter values for the data phase.

Same as *[can\_get\_timing\_max()](#gabe385d0f003b1e990c78ef7a2a3f9616)* but for the maximum values for the data phase.

Note
:   `CONFIG_CAN_FD_MODE` must be selected for this function to be available.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   Pointer to the maximum supported timing parameter values, or NULL if CAN FD support is not implemented by the driver.

## [◆ ](#ga6399ef0cefdab3da738136f8a5c59c2f)can\_get\_timing\_data\_min()

| const struct [can\_timing](structcan__timing.md) \* can\_get\_timing\_data\_min | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Get the minimum supported timing parameter values for the data phase.

Same as *[can\_get\_timing\_min()](#ga5a57627de4764f0bd3b4bafe07f56e6f)* but for the minimum values for the data phase.

Note
:   `CONFIG_CAN_FD_MODE` must be selected for this function to be available.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   Pointer to the minimum supported timing parameter values, or NULL if CAN FD support is not implemented by the driver.

## [◆ ](#gabe385d0f003b1e990c78ef7a2a3f9616)can\_get\_timing\_max()

| const struct [can\_timing](structcan__timing.md) \* can\_get\_timing\_max | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Get the maximum supported timing parameter values.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   Pointer to the maximum supported timing parameter values.

## [◆ ](#ga5a57627de4764f0bd3b4bafe07f56e6f)can\_get\_timing\_min()

| const struct [can\_timing](structcan__timing.md) \* can\_get\_timing\_min | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Get the minimum supported timing parameter values.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   Pointer to the minimum supported timing parameter values.

## [◆ ](#gae012d26711c2a7ce1419d21c38cae63a)can\_get\_transceiver()

| const struct [device](structdevice.md) \* can\_get\_transceiver | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Get the CAN transceiver associated with the CAN controller.

Get a pointer to the device structure for the CAN transceiver associated with the CAN controller.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   Pointer to the device structure for the associated CAN transceiver driver instance, or NULL if no transceiver is associated.

## [◆ ](#gac474e56a50685736a1c25dca277aab5e)can\_recover()

| int can\_recover | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout* ) |

`#include <[can.h](drivers_2can_8h.md)>`

Recover from bus-off state.

Recover the CAN controller from bus-off state to error-active state.

Note
:   `CONFIG_CAN_MANUAL_RECOVERY_MODE` must be enabled for this function to be available.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | timeout | Timeout for waiting for the recovery or [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca "Generate infinite timeout delay."). |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -ENOTSUP | if the CAN controller is not in manual recovery mode. |
    | -ENETDOWN | if the CAN controller is in stopped state. |
    | -EAGAIN | on timeout. |
    | -ENOSYS | If this function is not implemented by the driver. |

## [◆ ](#ga822aa3142ea01582d5cfb8b478fb2847)can\_remove\_rx\_filter()

| void can\_remove\_rx\_filter | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | int | *filter\_id* ) |

`#include <[can.h](drivers_2can_8h.md)>`

Remove a CAN RX filter.

This routine removes a CAN RX filter based on the filter ID returned by *[can\_add\_rx\_filter()](#gae9dd69a13b960f773ab07bb0bb13b5e9)* or *[can\_add\_rx\_filter\_msgq()](#gaaac20a068b7f32d2f38d1601d588b35c)*.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | filter\_id | Filter ID |

## [◆ ](#ga446ee31913699de3c80be05d837b5fd5)can\_send()

| int can\_send | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [can\_frame](structcan__frame.md) \* | *frame*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *timeout*, |
|  |  | [can\_tx\_callback\_t](#gab3675297d3e528bf19e2072f6a84bfca) | *callback*, |
|  |  | void \* | *user\_data* ) |

`#include <[can.h](drivers_2can_8h.md)>`

Queue a CAN frame for transmission on the CAN bus.

Queue a CAN frame for transmission on the CAN bus with optional timeout and completion callback function.

Queued CAN frames are transmitted in order according to the their priority:

- The lower the CAN-ID, the higher the priority.
- Data frames have higher priority than Remote Transmission Request (RTR) frames with identical CAN-IDs.
- Frames with standard (11-bit) identifiers have higher priority than frames with extended (29-bit) identifiers with identical base IDs (the higher 11 bits of the extended identifier).
- Transmission order for queued frames with the same priority is hardware dependent.

Note
:   If transmitting segmented messages spanning multiple CAN frames with identical CAN-IDs, the sender must ensure to only queue one frame at a time if FIFO order is required.

By default, the CAN controller will automatically retry transmission in case of lost bus arbitration or missing acknowledge. Some CAN controllers support disabling automatic retransmissions via [CAN\_MODE\_ONE\_SHOT](#ga033d7ade1966299c7e6249b945f38202).

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | frame | CAN frame to transmit. |
    | timeout | Timeout waiting for a empty TX mailbox or [K\_FOREVER](group__clock__apis.md#ga0bb4b83f0222193b21a8910311bab0ca "Generate infinite timeout delay."). |
    | callback | Optional callback for when the frame was sent or a transmission error occurred. If [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), this function is blocking until frame is sent. The callback must be [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) if called from user mode. |
    | user\_data | User data to pass to callback function. |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | -EINVAL | if an invalid parameter was passed to the function. |
    | -ENOTSUP | if an unsupported parameter was passed to the function. |
    | -ENETDOWN | if the CAN controller is in stopped state. |
    | -ENETUNREACH | if the CAN controller is in bus-off state. |
    | -EBUSY | if CAN bus arbitration was lost (only applicable if automatic retransmissions are disabled). |
    | -EIO | if a general transmit error occurred (e.g. missing ACK if automatic retransmissions are disabled). |
    | -EAGAIN | on timeout. |

## [◆ ](#ga0685ebfacfb79d33131167ac3aaa6f9b)can\_set\_bitrate()

| int can\_set\_bitrate | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *bitrate* ) |

`#include <[can.h](drivers_2can_8h.md)>`

Set the bitrate of the CAN controller.

CAN in Automation (CiA) 301 v4.2.0 recommends a sample point location of 87.5% percent for all bitrates. However, some CAN controllers have difficulties meeting this for higher bitrates.

This function defaults to using a sample point of 75.0% for bitrates over 800 kbit/s, 80.0% for bitrates over 500 kbit/s, and 87.5% for all other bitrates. This is in line with the sample point locations used by the Linux kernel.

See also
:   [can\_set\_bitrate\_data()](#ga0afd2c446fc5e685370641a1678f87b7)

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | bitrate | Desired arbitration phase bitrate. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | if the CAN controller is not in stopped state. |
    | -EINVAL | if the requested bitrate is out of range. |
    | -ENOTSUP | if the requested bitrate not supported by the CAN controller/transceiver combination. |
    | -ERANGE | if the resulting sample point is off by more than +/- 5%. |
    | -EIO | General input/output error, failed to set bitrate. |

## [◆ ](#ga0afd2c446fc5e685370641a1678f87b7)can\_set\_bitrate\_data()

| int can\_set\_bitrate\_data | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *bitrate\_data* ) |

`#include <[can.h](drivers_2can_8h.md)>`

Set the bitrate for the data phase of the CAN FD controller.

CAN in Automation (CiA) 301 v4.2.0 recommends a sample point location of 87.5% percent for all bitrates. However, some CAN controllers have difficulties meeting this for higher bitrates.

This function defaults to using a sample point of 75.0% for bitrates over 800 kbit/s, 80.0% for bitrates over 500 kbit/s, and 87.5% for all other bitrates. This is in line with the sample point locations used by the Linux kernel.

Note
:   `CONFIG_CAN_FD_MODE` must be selected for this function to be available.

See also
:   [can\_set\_bitrate()](#ga0685ebfacfb79d33131167ac3aaa6f9b)

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | bitrate\_data | Desired data phase bitrate. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | if the CAN controller is not in stopped state. |
    | -EINVAL | if the requested bitrate is out of range. |
    | -ENOTSUP | if the requested bitrate not supported by the CAN controller/transceiver combination. |
    | -ERANGE | if the resulting sample point is off by more than +/- 5%. |
    | -EIO | General input/output error, failed to set bitrate. |

## [◆ ](#gae04c3c884b3ed26dfea4745b7dff2c5f)can\_set\_mode()

| int can\_set\_mode | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | [can\_mode\_t](#ga0b2a1456e66f4522a30cf1400fdfced7) | *mode* ) |

`#include <[can.h](drivers_2can_8h.md)>`

Set the CAN controller to the given operation mode.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | mode | Operation mode. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | if the CAN controller is not in stopped state. |
    | -EIO | General input/output error, failed to configure device. |

## [◆ ](#gad322da0dad328abb50de23bef6882d8e)can\_set\_state\_change\_callback()

| | void can\_set\_state\_change\_callback | ( | const struct [device](structdevice.md) \* | *dev*, | | --- | --- | --- | --- | |  |  | [can\_state\_change\_callback\_t](#ga002ff7ba1f5be374510a902459dd9d3d) | *callback*, | |  |  | void \* | *user\_data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Set a callback for CAN controller state change events.

Set the callback for CAN controller state change events. The callback function will be called in interrupt context.

Only one callback can be registered per controller. Calling this function again overrides any previously registered callback.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | callback | Callback function. |
    | user\_data | User data to pass to callback function. |

## [◆ ](#ga1b134af5d6286ea0fee130b6da5217da)can\_set\_timing()

| int can\_set\_timing | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [can\_timing](structcan__timing.md) \* | *timing* ) |

`#include <[can.h](drivers_2can_8h.md)>`

Configure the bus timing of a CAN controller.

See also
:   [can\_set\_timing\_data()](#ga606cf9fda4c66a0f4abf74e1d357eac2)

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | timing | Bus timings. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | if the CAN controller is not in stopped state. |
    | -ENOTSUP | if the timing parameters are not supported by the driver. |
    | -EIO | General input/output error, failed to configure device. |

## [◆ ](#ga606cf9fda4c66a0f4abf74e1d357eac2)can\_set\_timing\_data()

| int can\_set\_timing\_data | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [can\_timing](structcan__timing.md) \* | *timing\_data* ) |

`#include <[can.h](drivers_2can_8h.md)>`

Configure the bus timing for the data phase of a CAN FD controller.

Note
:   `CONFIG_CAN_FD_MODE` must be selected for this function to be available.

See also
:   [can\_set\_timing()](#ga1b134af5d6286ea0fee130b6da5217da)

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | timing\_data | Bus timings for data phase |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EBUSY | if the CAN controller is not in stopped state. |
    | -EIO | General input/output error, failed to configure device. |
    | -ENOTSUP | if the timing parameters are not supported by the driver. |
    | -ENOSYS | if CAN FD support is not implemented by the driver. |

## [◆ ](#gae48dfa8bc5b52f233b9b1a08aac2675a)can\_start()

| int can\_start | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Start the CAN controller.

Bring the CAN controller out of [CAN\_STATE\_STOPPED](#ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8). This will reset the RX/TX error counters, enable the CAN controller to participate in CAN communication, and enable the CAN transceiver, if supported.

Starting the CAN controller resets all the CAN controller statistics.

See also
:   [can\_stop()](#ga1b0ac9185341cb0bde85ec64e4c490a5)
:   [can\_transceiver\_enable()](group__can__transceiver.md#ga0d0e87150b49198c41e2782a17cfd694 "Enable CAN transceiver.")

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | -EALREADY | if the device is already started. |
    | -EIO | General input/output error, failed to start device. |

## [◆ ](#ga4f8414d64b75d4d1ffb7a0feff36f698)can\_stats\_get\_ack\_errors()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_stats\_get\_ack\_errors | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Get the acknowledge error counter for a CAN device.

The acknowledge error counter is incremented when the CAN controller does not monitor a dominant bit in the ACK slot.

Note
:   `CONFIG_CAN_STATS` must be selected for this function to be available.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   acknowledge error counter

## [◆ ](#ga7c380f6c4a529e5b5e6010ab4e6c7680)can\_stats\_get\_bit0\_errors()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_stats\_get\_bit0\_errors | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Get the bit0 error counter for a CAN device.

The bit0 error counter is incremented when the CAN controller is unable to transmit a dominant bit.

Note
:   `CONFIG_CAN_STATS` must be selected for this function to be available.

See also
:   [can\_stats\_get\_bit\_errors()](#ga27b277f3b5146590f159171f602904db)

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   bit0 error counter

## [◆ ](#ga4c7d40951a2ae6eaa72e5d1f7a26ac75)can\_stats\_get\_bit1\_errors()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_stats\_get\_bit1\_errors | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Get the bit1 error counter for a CAN device.

The bit1 error counter is incremented when the CAN controller is unable to transmit a recessive bit.

Note
:   `CONFIG_CAN_STATS` must be selected for this function to be available.

See also
:   [can\_stats\_get\_bit\_errors()](#ga27b277f3b5146590f159171f602904db)

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   bit1 error counter

## [◆ ](#ga27b277f3b5146590f159171f602904db)can\_stats\_get\_bit\_errors()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_stats\_get\_bit\_errors | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Get the bit error counter for a CAN device.

The bit error counter is incremented when the CAN controller is unable to transmit either a dominant or a recessive bit.

Note
:   `CONFIG_CAN_STATS` must be selected for this function to be available.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   bit error counter

## [◆ ](#ga31692aef7962172532f8200fed7aecd2)can\_stats\_get\_crc\_errors()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_stats\_get\_crc\_errors | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Get the CRC error counter for a CAN device.

The CRC error counter is incremented when the CAN controller detects a frame with an invalid CRC.

Note
:   `CONFIG_CAN_STATS` must be selected for this function to be available.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   CRC error counter

## [◆ ](#gabf9ce221f4f6a8dbaafcff9b7a5c5a10)can\_stats\_get\_form\_errors()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_stats\_get\_form\_errors | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Get the form error counter for a CAN device.

The form error counter is incremented when the CAN controller detects a fixed-form bit field containing illegal bits.

Note
:   `CONFIG_CAN_STATS` must be selected for this function to be available.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   form error counter

## [◆ ](#ga8664fbaa13f4bb89540493264d2a041d)can\_stats\_get\_rx\_overruns()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_stats\_get\_rx\_overruns | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Get the RX overrun counter for a CAN device.

The RX overrun counter is incremented when the CAN controller receives a CAN frame matching an installed filter but lacks the capacity to store it (either due to an already full RX mailbox or a full RX FIFO).

Note
:   `CONFIG_CAN_STATS` must be selected for this function to be available.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   RX overrun counter

## [◆ ](#ga162fde4e622fb06dcbbcf2f31bb35d38)can\_stats\_get\_stuff\_errors()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) can\_stats\_get\_stuff\_errors | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Get the stuffing error counter for a CAN device.

The stuffing error counter is incremented when the CAN controller detects a bit stuffing error.

Note
:   `CONFIG_CAN_STATS` must be selected for this function to be available.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Returns
:   stuffing error counter

## [◆ ](#ga1b0ac9185341cb0bde85ec64e4c490a5)can\_stop()

| int can\_stop | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[can.h](drivers_2can_8h.md)>`

Stop the CAN controller.

Bring the CAN controller into [CAN\_STATE\_STOPPED](#ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8). This will disallow the CAN controller from participating in CAN communication, abort any pending CAN frame transmissions, and disable the CAN transceiver, if supported.

See also
:   [can\_start()](#gae48dfa8bc5b52f233b9b1a08aac2675a)
:   [can\_transceiver\_disable()](group__can__transceiver.md#ga7509ca0b6ece81b4038b7d128af961be "Disable CAN transceiver.")

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Return values
:   | 0 | if successful. |
    | --- | --- |
    | -EALREADY | if the device is already stopped. |
    | -EIO | General input/output error, failed to stop device. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
