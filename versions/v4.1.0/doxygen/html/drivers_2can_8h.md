---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/drivers_2can_8h.html
original_path: doxygen/html/drivers_2can_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can.h File Reference

Controller Area Network (CAN) driver API.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[string.h](string_8h_source.md)>`  
`#include <[zephyr/sys_clock.h](sys__clock_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/stats/stats.h](stats_2stats_8h_source.md)>`  
`#include <zephyr/syscalls/can.h>`

[Go to the source code of this file.](drivers_2can_8h_source.md)

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
| #define | [CAN\_STATS\_BIT\_ERROR\_INC](group__can__interface.md#gaf6f7efa9d99f44af6f58352f558d7fec)(dev\_) |
|  | Increment the bit error counter for a CAN device. |
| #define | [CAN\_STATS\_BIT0\_ERROR\_INC](group__can__interface.md#ga120a37d5ae5064dcbf116e488f733764)(dev\_) |
|  | Increment the bit0 error counter for a CAN device. |
| #define | [CAN\_STATS\_BIT1\_ERROR\_INC](group__can__interface.md#ga678b74039632302efcb5ef80f0e3a90b)(dev\_) |
|  | Increment the bit1 (recessive) error counter for a CAN device. |
| #define | [CAN\_STATS\_STUFF\_ERROR\_INC](group__can__interface.md#gae4146843944b7ffb1c96636e889282f7)(dev\_) |
|  | Increment the stuffing error counter for a CAN device. |
| #define | [CAN\_STATS\_CRC\_ERROR\_INC](group__can__interface.md#ga125ce05d40881476f5f156ad5e28c664)(dev\_) |
|  | Increment the CRC error counter for a CAN device. |
| #define | [CAN\_STATS\_FORM\_ERROR\_INC](group__can__interface.md#gac5809b3f5e1a463822e76921cddc9909)(dev\_) |
|  | Increment the form error counter for a CAN device. |
| #define | [CAN\_STATS\_ACK\_ERROR\_INC](group__can__interface.md#ga15f7ca18badbbe2fe24be68cacce6171)(dev\_) |
|  | Increment the acknowledge error counter for a CAN device. |
| #define | [CAN\_STATS\_RX\_OVERRUN\_INC](group__can__interface.md#ga95fe455780b38c7202b48bc6004e6f4d)(dev\_) |
|  | Increment the RX overrun counter for a CAN device. |
| #define | [CAN\_STATS\_RESET](group__can__interface.md#ga06a9058924901e2d960858fb9e3a4a02)(dev\_) |
|  | Zero all statistics for a CAN device. |
| #define | [CAN\_DEVICE\_DT\_DEFINE](group__can__interface.md#ga599d0695abe481411660d7af2893f4a5)(node\_id, init\_fn, pm, data, config, level, prio, api, ...) |
|  | Like [DEVICE\_DT\_DEFINE()](group__device__model.md#gac49e26fbe91a14307d5ea08d41561dd1 "Create a device object from a devicetree node identifier and set it up for boot time initialization.") with CAN device specifics. |
| #define | [CAN\_DEVICE\_DT\_INST\_DEFINE](group__can__interface.md#ga20266dc5e962922144e078b85ccb8351)(inst, ...) |
|  | Like [CAN\_DEVICE\_DT\_DEFINE()](group__can__interface.md#ga599d0695abe481411660d7af2893f4a5 "Like DEVICE_DT_DEFINE() with CAN device specifics.") for an instance of a DT\_DRV\_COMPAT compatible. |
| CAN frame definitions | |
| #define | [CAN\_STD\_ID\_MASK](group__can__interface.md#ga4cd8ce34887b90baeeaa6a4aa048b398)   0x7FFU |
|  | Bit mask for a standard (11-bit) CAN identifier. |
| #define | [CAN\_EXT\_ID\_MASK](group__can__interface.md#ga15ee71e8abcf51008925585049125986)   0x1FFFFFFFU |
|  | Bit mask for an extended (29-bit) CAN identifier. |
| #define | [CAN\_MAX\_DLC](group__can__interface.md#gadc209a027ee700faf10461e2417bee50)   8U |
|  | Maximum data length code for CAN 2.0A/2.0B. |
| #define | [CANFD\_MAX\_DLC](group__can__interface.md#gad4b7310536c7e3252c2056abe64c0333)   15U |
|  | Maximum data length code for CAN FD. |
| CAN controller mode flags | |
|  | |
| #define | [CAN\_MODE\_NORMAL](group__can__interface.md#ga89cd5ea2e9d70a51bc12b100be28ca3d)   0 |
|  | Normal mode. |
| #define | [CAN\_MODE\_LOOPBACK](group__can__interface.md#ga891031afc77974a041accb3d0ceb21bb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Controller is in loopback mode (receives own frames). |
| #define | [CAN\_MODE\_LISTENONLY](group__can__interface.md#ga117d04b9118a1b3f839c557ef6b596cb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Controller is not allowed to send dominant bits. |
| #define | [CAN\_MODE\_FD](group__can__interface.md#gabb4d99736d8386a5ab62a5e44374d13a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Controller allows transmitting/receiving CAN FD frames. |
| #define | [CAN\_MODE\_ONE\_SHOT](group__can__interface.md#ga033d7ade1966299c7e6249b945f38202)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Controller does not retransmit in case of lost arbitration or missing ACK. |
| #define | [CAN\_MODE\_3\_SAMPLES](group__can__interface.md#gaf0821983174ad781e1bb63a976a18fab)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Controller uses triple sampling mode. |
| #define | [CAN\_MODE\_MANUAL\_RECOVERY](group__can__interface.md#ga3d8675253125b2af2bd22f0b2cc60cdd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Controller requires manual recovery after entering bus-off state. |
| CAN frame flags | |
|  | |
| #define | [CAN\_FRAME\_IDE](group__can__interface.md#ga9ed5a06a97db2c955a7db4b6e386d5e3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Frame uses extended (29-bit) CAN ID. |
| #define | [CAN\_FRAME\_RTR](group__can__interface.md#gaed376ef16b84cd1974255fbb26dc3d7f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Frame is a Remote Transmission Request (RTR). |
| #define | [CAN\_FRAME\_FDF](group__can__interface.md#ga22f85e1d16b93e46200f9673abdbb589)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Frame uses CAN FD format (FDF). |
| #define | [CAN\_FRAME\_BRS](group__can__interface.md#ga1fdf15ce4a3b333488f9b630ec836d52)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Frame uses CAN FD Baud Rate Switch (BRS). |
| #define | [CAN\_FRAME\_ESI](group__can__interface.md#ga83f8b7af6eb45e43aaac355de3e69e52)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | CAN FD Error State Indicator (ESI). |
| CAN filter flags | |
|  | |
| #define | [CAN\_FILTER\_IDE](group__can__interface.md#gafa40c165d016955ec0c856a7fd53168f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Filter matches frames with extended (29-bit) CAN IDs. |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) |
|  | Provides a type to hold CAN controller configuration flags. |
| typedef void(\* | [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca)) (const struct [device](structdevice.md) \*dev, int error, void \*user\_data) |
|  | Defines the application callback handler function signature. |
| typedef void(\* | [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f)) (const struct [device](structdevice.md) \*dev, struct [can\_frame](structcan__frame.md) \*frame, void \*user\_data) |
|  | Defines the application callback handler function signature for receiving. |
| typedef void(\* | [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d)) (const struct [device](structdevice.md) \*dev, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) err\_cnt, void \*user\_data) |
|  | Defines the state change callback handler function signature. |

| Enumerations | |
| --- | --- |
| enum | [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) {     [CAN\_STATE\_ERROR\_ACTIVE](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a026154ef3a7f9cb633e43ab7e63d769c) , [CAN\_STATE\_ERROR\_WARNING](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a15263a89961afbc4e813c7ccfc59e5ff) , [CAN\_STATE\_ERROR\_PASSIVE](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7ac2cd08cde738273c5e5df8306c48d8ae) , [CAN\_STATE\_BUS\_OFF](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a679935a8710667fcb99423d217cd9959) ,     [CAN\_STATE\_STOPPED](group__can__interface.md#ggac7ec472c26c564dd7067c49f67c8d2f7a644e7a441f2e607b93528d3128508cc8)   } |
|  | Defines the state of the CAN controller. [More...](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) |

| Functions | |
| --- | --- |
| CAN controller configuration | |
| int | [can\_get\_core\_clock](group__can__interface.md#ga4af6d0d9ab72b195909f511ac65cb8fa) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*rate) |
|  | Get the CAN core clock rate. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_get\_bitrate\_min](group__can__interface.md#ga343456749eec6144a91bacae0d94b114) (const struct [device](structdevice.md) \*dev) |
|  | Get minimum supported bitrate. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_get\_bitrate\_max](group__can__interface.md#ga1e6dc8026e4d922bce4d398d9f32a457) (const struct [device](structdevice.md) \*dev) |
|  | Get maximum supported bitrate. |
| const struct [can\_timing](structcan__timing.md) \* | [can\_get\_timing\_min](group__can__interface.md#ga5a57627de4764f0bd3b4bafe07f56e6f) (const struct [device](structdevice.md) \*dev) |
|  | Get the minimum supported timing parameter values. |
| const struct [can\_timing](structcan__timing.md) \* | [can\_get\_timing\_max](group__can__interface.md#gabe385d0f003b1e990c78ef7a2a3f9616) (const struct [device](structdevice.md) \*dev) |
|  | Get the maximum supported timing parameter values. |
| int | [can\_calc\_timing](group__can__interface.md#gac27fe64142603f0d32d422594356b2d7) (const struct [device](structdevice.md) \*dev, struct [can\_timing](structcan__timing.md) \*res, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sample\_pnt) |
|  | Calculate timing parameters from bitrate and sample point. |
| const struct [can\_timing](structcan__timing.md) \* | [can\_get\_timing\_data\_min](group__can__interface.md#ga6399ef0cefdab3da738136f8a5c59c2f) (const struct [device](structdevice.md) \*dev) |
|  | Get the minimum supported timing parameter values for the data phase. |
| const struct [can\_timing](structcan__timing.md) \* | [can\_get\_timing\_data\_max](group__can__interface.md#ga47a2f6d6b42121b390aa92160c833b80) (const struct [device](structdevice.md) \*dev) |
|  | Get the maximum supported timing parameter values for the data phase. |
| int | [can\_calc\_timing\_data](group__can__interface.md#ga358cd73ed59c2099f4b2c6ceb397ca11) (const struct [device](structdevice.md) \*dev, struct [can\_timing](structcan__timing.md) \*res, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sample\_pnt) |
|  | Calculate timing parameters for the data phase. |
| int | [can\_set\_timing\_data](group__can__interface.md#ga606cf9fda4c66a0f4abf74e1d357eac2) (const struct [device](structdevice.md) \*dev, const struct [can\_timing](structcan__timing.md) \*timing\_data) |
|  | Configure the bus timing for the data phase of a CAN FD controller. |
| int | [can\_set\_bitrate\_data](group__can__interface.md#ga0afd2c446fc5e685370641a1678f87b7) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate\_data) |
|  | Set the bitrate for the data phase of the CAN FD controller. |
| int | [can\_set\_timing](group__can__interface.md#ga1b134af5d6286ea0fee130b6da5217da) (const struct [device](structdevice.md) \*dev, const struct [can\_timing](structcan__timing.md) \*timing) |
|  | Configure the bus timing of a CAN controller. |
| int | [can\_get\_capabilities](group__can__interface.md#ga4afd7776c5039dec8acb089499dc1168) (const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*cap) |
|  | Get the supported modes of the CAN controller. |
| const struct [device](structdevice.md) \* | [can\_get\_transceiver](group__can__interface.md#gae012d26711c2a7ce1419d21c38cae63a) (const struct [device](structdevice.md) \*dev) |
|  | Get the CAN transceiver associated with the CAN controller. |
| int | [can\_start](group__can__interface.md#gae48dfa8bc5b52f233b9b1a08aac2675a) (const struct [device](structdevice.md) \*dev) |
|  | Start the CAN controller. |
| int | [can\_stop](group__can__interface.md#ga1b0ac9185341cb0bde85ec64e4c490a5) (const struct [device](structdevice.md) \*dev) |
|  | Stop the CAN controller. |
| int | [can\_set\_mode](group__can__interface.md#gae04c3c884b3ed26dfea4745b7dff2c5f) (const struct [device](structdevice.md) \*dev, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) mode) |
|  | Set the CAN controller to the given operation mode. |
| [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) | [can\_get\_mode](group__can__interface.md#gabd201b5b1fca54048985a8a24dd51e55) (const struct [device](structdevice.md) \*dev) |
|  | Get the operation mode of the CAN controller. |
| int | [can\_set\_bitrate](group__can__interface.md#ga0685ebfacfb79d33131167ac3aaa6f9b) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bitrate) |
|  | Set the bitrate of the CAN controller. |
| Transmitting CAN frames | |
| int | [can\_send](group__can__interface.md#ga446ee31913699de3c80be05d837b5fd5) (const struct [device](structdevice.md) \*dev, const struct [can\_frame](structcan__frame.md) \*frame, [k\_timeout\_t](structk__timeout__t.md) timeout, [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) callback, void \*user\_data) |
|  | Queue a CAN frame for transmission on the CAN bus. |
| CAN bus error reporting and handling | |
| int | [can\_get\_state](group__can__interface.md#gab98c121578c8349d9dfb41d60f356857) (const struct [device](structdevice.md) \*dev, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*err\_cnt) |
|  | Get current CAN controller state. |
| int | [can\_recover](group__can__interface.md#gac474e56a50685736a1c25dca277aab5e) (const struct [device](structdevice.md) \*dev, [k\_timeout\_t](structk__timeout__t.md) timeout) |
|  | Recover from bus-off state. |
| static void | [can\_set\_state\_change\_callback](group__can__interface.md#gad322da0dad328abb50de23bef6882d8e) (const struct [device](structdevice.md) \*dev, [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) callback, void \*user\_data) |
|  | Set a callback for CAN controller state change events. |
| CAN statistics | |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_stats\_get\_bit\_errors](group__can__interface.md#ga27b277f3b5146590f159171f602904db) (const struct [device](structdevice.md) \*dev) |
|  | Get the bit error counter for a CAN device. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_stats\_get\_bit0\_errors](group__can__interface.md#ga7c380f6c4a529e5b5e6010ab4e6c7680) (const struct [device](structdevice.md) \*dev) |
|  | Get the bit0 error counter for a CAN device. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_stats\_get\_bit1\_errors](group__can__interface.md#ga4c7d40951a2ae6eaa72e5d1f7a26ac75) (const struct [device](structdevice.md) \*dev) |
|  | Get the bit1 error counter for a CAN device. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_stats\_get\_stuff\_errors](group__can__interface.md#ga162fde4e622fb06dcbbcf2f31bb35d38) (const struct [device](structdevice.md) \*dev) |
|  | Get the stuffing error counter for a CAN device. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_stats\_get\_crc\_errors](group__can__interface.md#ga31692aef7962172532f8200fed7aecd2) (const struct [device](structdevice.md) \*dev) |
|  | Get the CRC error counter for a CAN device. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_stats\_get\_form\_errors](group__can__interface.md#gabf9ce221f4f6a8dbaafcff9b7a5c5a10) (const struct [device](structdevice.md) \*dev) |
|  | Get the form error counter for a CAN device. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_stats\_get\_ack\_errors](group__can__interface.md#ga4f8414d64b75d4d1ffb7a0feff36f698) (const struct [device](structdevice.md) \*dev) |
|  | Get the acknowledge error counter for a CAN device. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [can\_stats\_get\_rx\_overruns](group__can__interface.md#ga8664fbaa13f4bb89540493264d2a041d) (const struct [device](structdevice.md) \*dev) |
|  | Get the RX overrun counter for a CAN device. |
| CAN utility functions | |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [can\_dlc\_to\_bytes](group__can__interface.md#gaa1d866167c0c23f8d5c0c15385589601) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dlc) |
|  | Convert from Data Length Code (DLC) to the number of data bytes. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [can\_bytes\_to\_dlc](group__can__interface.md#ga8314716fe2b66d567b3fd377b8ee9dc3) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_bytes) |
|  | Convert from number of bytes to Data Length Code (DLC). |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [can\_frame\_matches\_filter](group__can__interface.md#gaafc54ac799e3a3a098a9f6941d7f2ea8) (const struct [can\_frame](structcan__frame.md) \*frame, const struct [can\_filter](structcan__filter.md) \*filter) |
|  | Check if a CAN frame matches a CAN filter. |

| Receiving CAN frames | |
| --- | --- |
| #define | [CAN\_MSGQ\_DEFINE](group__can__interface.md#ga7af0acdfbdad07fc3eba4cbd29bc090b)(name, max\_frames) |
|  | Statically define and initialize a CAN RX message queue. |
| int | [can\_add\_rx\_filter](group__can__interface.md#gae9dd69a13b960f773ab07bb0bb13b5e9) (const struct [device](structdevice.md) \*dev, [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) callback, void \*user\_data, const struct [can\_filter](structcan__filter.md) \*filter) |
|  | Add a callback function for a given CAN filter. |
| int | [can\_add\_rx\_filter\_msgq](group__can__interface.md#gaaac20a068b7f32d2f38d1601d588b35c) (const struct [device](structdevice.md) \*dev, struct [k\_msgq](structk__msgq.md) \*msgq, const struct [can\_filter](structcan__filter.md) \*filter) |
|  | Simple wrapper function for adding a message queue for a given filter. |
| void | [can\_remove\_rx\_filter](group__can__interface.md#ga822aa3142ea01582d5cfb8b478fb2847) (const struct [device](structdevice.md) \*dev, int filter\_id) |
|  | Remove a CAN RX filter. |
| int | [can\_get\_max\_filters](group__can__interface.md#ga526c08539094486f07dc52aad8ed0dcc) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) ide) |
|  | Get maximum number of RX filters. |

## Detailed Description

Controller Area Network (CAN) driver API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [can.h](drivers_2can_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
