---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ccc_8h.html
original_path: doxygen/html/ccc_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ccc.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/sys/util.h](util_8h_source.md)>`

[Go to the source code of this file.](ccc_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [i3c\_ccc\_target\_payload](structi3c__ccc__target__payload.md) |
|  | Payload structure for Direct CCC to one target. [More...](structi3c__ccc__target__payload.md#details) |
| struct | [i3c\_ccc\_payload](structi3c__ccc__payload.md) |
|  | Payload structure for one CCC transaction. [More...](structi3c__ccc__payload.md#details) |
| struct | [i3c\_ccc\_events](structi3c__ccc__events.md) |
|  | Payload for ENEC/DISEC CCC (Target Events Command). [More...](structi3c__ccc__events.md#details) |
| struct | [i3c\_ccc\_mwl](structi3c__ccc__mwl.md) |
|  | Payload for SETMWL/GETMWL CCC (Set/Get Maximum Write Length). [More...](structi3c__ccc__mwl.md#details) |
| struct | [i3c\_ccc\_mrl](structi3c__ccc__mrl.md) |
|  | Payload for SETMRL/GETMRL CCC (Set/Get Maximum Read Length). [More...](structi3c__ccc__mrl.md#details) |
| struct | [i3c\_ccc\_deftgts\_active\_controller](structi3c__ccc__deftgts__active__controller.md) |
|  | The active controller part of payload for DEFTGTS CCC. [More...](structi3c__ccc__deftgts__active__controller.md#details) |
| struct | [i3c\_ccc\_deftgts\_target](structi3c__ccc__deftgts__target.md) |
|  | The target device part of payload for DEFTGTS CCC. [More...](structi3c__ccc__deftgts__target.md#details) |
| struct | [i3c\_ccc\_deftgts](structi3c__ccc__deftgts.md) |
|  | Payload for DEFTGTS CCC (Define List of Targets). [More...](structi3c__ccc__deftgts.md#details) |
| struct | [i3c\_ccc\_address](structi3c__ccc__address.md) |
|  | Payload for a single device address. [More...](structi3c__ccc__address.md#details) |
| struct | [i3c\_ccc\_getpid](structi3c__ccc__getpid.md) |
|  | Payload for GETPID CCC (Get Provisioned ID). [More...](structi3c__ccc__getpid.md#details) |
| struct | [i3c\_ccc\_getbcr](structi3c__ccc__getbcr.md) |
|  | Payload for GETBCR CCC (Get Bus Characteristics Register). [More...](structi3c__ccc__getbcr.md#details) |
| struct | [i3c\_ccc\_getdcr](structi3c__ccc__getdcr.md) |
|  | Payload for GETDCR CCC (Get Device Characteristics Register). [More...](structi3c__ccc__getdcr.md#details) |
| union | [i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md) |
|  | Payload for GETSTATUS CCC (Get Device Status). [More...](unioni3c__ccc__getstatus.md#details) |
| struct | [i3c\_ccc\_setbrgtgt\_tgt](structi3c__ccc__setbrgtgt__tgt.md) |
|  | One Bridged Target for SETBRGTGT payload. [More...](structi3c__ccc__setbrgtgt__tgt.md#details) |
| struct | [i3c\_ccc\_setbrgtgt](structi3c__ccc__setbrgtgt.md) |
|  | Payload for SETBRGTGT CCC (Set Bridge Targets). [More...](structi3c__ccc__setbrgtgt.md#details) |
| union | [i3c\_ccc\_getmxds](unioni3c__ccc__getmxds.md) |
|  | Payload for GETMXDS CCC (Get Max Data Speed). [More...](unioni3c__ccc__getmxds.md#details) |
| union | [i3c\_ccc\_getcaps](unioni3c__ccc__getcaps.md) |
|  | Payload for GETCAPS CCC (Get Optional Feature Capabilities). [More...](unioni3c__ccc__getcaps.md#details) |

| Macros | |
| --- | --- |
| #define | [I3C\_CCC\_BROADCAST\_MAX\_ID](group__i3c__ccc.md#gaf7b1cbdc790aa1d2c307e1f4ba773ba2)   0x7FU |
|  | Maximum CCC ID for broadcast. |
| #define | [I3C\_CCC\_ENEC](group__i3c__ccc.md#ga06fc2296ada6198ab7a00646804ad5ed)(broadcast) |
|  | Enable Events Command. |
| #define | [I3C\_CCC\_DISEC](group__i3c__ccc.md#ga8798591746e72a8ae1f901e97d45b810)(broadcast) |
|  | Disable Events Command. |
| #define | [I3C\_CCC\_ENTAS](group__i3c__ccc.md#ga213102b3a8dbd490b02c3c89843c8d2a)([as](asm-macro-32-bit-gnu_8h.md#ac93d5f4341d561a6bd9864e880cffcf4), broadcast) |
|  | Enter Activity State. |
| #define | [I3C\_CCC\_ENTAS0](group__i3c__ccc.md#ga364ce54e30957f7871e56cd82c1f825c)(broadcast) |
|  | Enter Activity State 0. |
| #define | [I3C\_CCC\_ENTAS1](group__i3c__ccc.md#ga21c57ce34fe60255c9c8b28dac0a7a85)(broadcast) |
|  | Enter Activity State 1. |
| #define | [I3C\_CCC\_ENTAS2](group__i3c__ccc.md#ga3adea01f66748ae2b153bf7eb9eab1eb)(broadcast) |
|  | Enter Activity State 2. |
| #define | [I3C\_CCC\_ENTAS3](group__i3c__ccc.md#ga4dba9093fe562e3d09470610ab393f21)(broadcast) |
|  | Enter Activity State 3. |
| #define | [I3C\_CCC\_RSTDAA](group__i3c__ccc.md#gaed94df1e670fc3670970f261865d6f63)   0x06U |
|  | Reset Dynamic Address Assignment (Broadcast). |
| #define | [I3C\_CCC\_ENTDAA](group__i3c__ccc.md#gad6663cfa56be6bba2187a1d42d64be7b)   0x07U |
|  | Enter Dynamic Address Assignment (Broadcast). |
| #define | [I3C\_CCC\_DEFTGTS](group__i3c__ccc.md#ga17e63ffe790f279a3e6eb8235c936604)   0x08U |
|  | Define List of Targets (Broadcast). |
| #define | [I3C\_CCC\_SETMWL](group__i3c__ccc.md#gaab1ccf6cd47dfecee24811501e123802)(broadcast) |
|  | Set Max Write Length (Broadcast or Direct). |
| #define | [I3C\_CCC\_SETMRL](group__i3c__ccc.md#ga97fd874b2e6c918f2e1262f7600bfd64)(broadcast) |
|  | Set Max Read Length (Broadcast or Direct). |
| #define | [I3C\_CCC\_ENTTM](group__i3c__ccc.md#gace2b7fc835d31ade916aad3126eb0c6c)   0x0BU |
|  | Enter Test Mode (Broadcast). |
| #define | [I3C\_CCC\_SETBUSCON](group__i3c__ccc.md#gac0f85a020956e3ee1ae8da899a9e06a6)   0x0CU |
|  | Set Bus Context (Broadcast). |
| #define | [I3C\_CCC\_ENDXFER](group__i3c__ccc.md#ga4f331e7c21f15dd211a70c1a01c49738)(broadcast) |
|  | Data Transfer Ending Procedure Control. |
| #define | [I3C\_CCC\_ENTHDR](group__i3c__ccc.md#gae213fc68bf723d8f7aee8c41cb9156c3)(x) |
|  | Enter HDR Mode (HDR-DDR) (Broadcast). |
| #define | [I3C\_CCC\_ENTHDR0](group__i3c__ccc.md#gae88e44e9469891609ece0b8711162b9d)   0x20U |
|  | Enter HDR Mode 0 (HDR-DDR) (Broadcast). |
| #define | [I3C\_CCC\_ENTHDR1](group__i3c__ccc.md#gae5319f3916df262579ecaac7497ed006)   0x21U |
|  | Enter HDR Mode 1 (HDR-TSP) (Broadcast). |
| #define | [I3C\_CCC\_ENTHDR2](group__i3c__ccc.md#gaeff48ef5d76e4ea051f5aee1d1e4fc40)   0x22U |
|  | Enter HDR Mode 2 (HDR-TSL) (Broadcast). |
| #define | [I3C\_CCC\_ENTHDR3](group__i3c__ccc.md#ga24eaa0af83a4a2223f4f84c3c67e05fe)   0x23U |
|  | Enter HDR Mode 3 (HDR-BT) (Broadcast). |
| #define | [I3C\_CCC\_ENTHDR4](group__i3c__ccc.md#gaf15d188164c8fa9c0bf589eb7c5622d0)   0x24U |
|  | Enter HDR Mode 4 (Broadcast). |
| #define | [I3C\_CCC\_ENTHDR5](group__i3c__ccc.md#gaafcad6bfacab1e42f22c8ee941ed6441)   0x25U |
|  | Enter HDR Mode 5 (Broadcast). |
| #define | [I3C\_CCC\_ENTHDR6](group__i3c__ccc.md#gae55615887425917b202818bb0b7c5ac5)   0x26U |
|  | Enter HDR Mode 6 (Broadcast). |
| #define | [I3C\_CCC\_ENTHDR7](group__i3c__ccc.md#ga9ab8c02bb5a80913024a43077fb97ffb)   0x27U |
|  | Enter HDR Mode 7 (Broadcast). |
| #define | [I3C\_CCC\_SETXTIME](group__i3c__ccc.md#ga4203d5fdd9e9ca253803359934f22524)(broadcast) |
|  | Exchange Timing Information (Broadcast or Direct). |
| #define | [I3C\_CCC\_SETAASA](group__i3c__ccc.md#gae995ef9e94beb26932b47136bdf89b57)   0x29U |
|  | Set All Addresses to Static Addresses (Broadcast). |
| #define | [I3C\_CCC\_RSTACT](group__i3c__ccc.md#ga424cb224727d33c1ab18e4149bbea232)(broadcast) |
|  | Target Reset Action. |
| #define | [I3C\_CCC\_DEFGRPA](group__i3c__ccc.md#ga89f8f72a7c7e8c9cb4fe8ece75ad78cf)   0x2BU |
|  | Define List of Group Address (Broadcast). |
| #define | [I3C\_CCC\_RSTGRPA](group__i3c__ccc.md#ga46611eab0c82b74c615a7a7435f79d85)(broadcast) |
|  | Reset Group Address. |
| #define | [I3C\_CCC\_MLANE](group__i3c__ccc.md#ga290cc5511d95b5be31c2c4cfea929085)(broadcast) |
|  | Multi-Lane Data Transfer Control (Broadcast). |
| #define | [I3C\_CCC\_VENDOR](group__i3c__ccc.md#gaee5fb96b2d54df3b1b7aadefd54a608d)(broadcast, id) |
|  | Vendor/Standard Extension. |
| #define | [I3C\_CCC\_SETDASA](group__i3c__ccc.md#ga134d5948b056144c83b133f93083a0f8)   0x87U |
|  | Set Dynamic Address from Static Address (Direct). |
| #define | [I3C\_CCC\_SETNEWDA](group__i3c__ccc.md#gae0d6d0047f2c6e73e49e5019ec8d9ff0)   0x88U |
|  | Set New Dynamic Address (Direct). |
| #define | [I3C\_CCC\_GETMWL](group__i3c__ccc.md#gae74935317b7ca471c09b767acf359e34)   0x8BU |
|  | Get Max Write Length (Direct). |
| #define | [I3C\_CCC\_GETMRL](group__i3c__ccc.md#ga92e89b1ba719fbb8833c6e32fe4ef1dc)   0x8CU |
|  | Get Max Read Length (Direct). |
| #define | [I3C\_CCC\_GETPID](group__i3c__ccc.md#ga04f7386d55742e935fa4dbfeb0120124)   0x8DU |
|  | Get Provisioned ID (Direct). |
| #define | [I3C\_CCC\_GETBCR](group__i3c__ccc.md#ga1d7d49ab48098e4c2d5f63bd91d005e1)   0x8EU |
|  | Get Bus Characteristics Register (Direct). |
| #define | [I3C\_CCC\_GETDCR](group__i3c__ccc.md#ga04ab6d4f0b2bf9d7f195132c0959225c)   0x8FU |
|  | Get Device Characteristics Register (Direct). |
| #define | [I3C\_CCC\_GETSTATUS](group__i3c__ccc.md#ga858603dfc251b684b9d049b90119993d)   0x90U |
|  | Get Device Status (Direct). |
| #define | [I3C\_CCC\_GETACCCR](group__i3c__ccc.md#gaa6807d3113c9c4d19b6fd27db32b3698)   0x91U |
|  | Get Accept Controller Role (Direct). |
| #define | [I3C\_CCC\_SETBRGTGT](group__i3c__ccc.md#gab3cac5de39903cc2331a38ac66c4ff14)   0x93U |
|  | Set Bridge Targets (Direct). |
| #define | [I3C\_CCC\_GETMXDS](group__i3c__ccc.md#ga2c078bf24e36689f34ad90979dd5c687)   0x94U |
|  | Get Max Data Speed (Direct). |
| #define | [I3C\_CCC\_GETCAPS](group__i3c__ccc.md#gaa913844f97ee35405e9bf50c61a161a8)   0x95U |
|  | Get Optional Feature Capabilities (Direct). |
| #define | [I3C\_CCC\_SETROUTE](group__i3c__ccc.md#ga5cf5cdb40299d4f8203b8035dacac17a)   0x96U |
|  | Set Route (Direct). |
| #define | [I3C\_CCC\_D2DXFER](group__i3c__ccc.md#gaa2d86faed4f7c36939ce754be852751a)   0x97U |
|  | Device to Device(s) Tunneling Control (Direct). |
| #define | [I3C\_CCC\_GETXTIME](group__i3c__ccc.md#ga66bb5e8027b103298f882f413f8ee6e8)   0x99U |
|  | Get Exchange Timing Information (Direct). |
| #define | [I3C\_CCC\_SETGRPA](group__i3c__ccc.md#gaa0bef5d42c9bf2a21e888e5d5998d5cb)   0x9BU |
|  | Set Group Address (Direct). |
| #define | [I3C\_CCC\_ENEC\_EVT\_ENINTR](group__i3c__ccc.md#gafe40d9b2ccedca40071c47929ff66e65)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Enable Events (ENEC) - Target Interrupt Requests. |
| #define | [I3C\_CCC\_ENEC\_EVT\_ENCR](group__i3c__ccc.md#gad73e2e9f31f3a02f52b20d77e64671ff)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Enable Events (ENEC) - Controller Role Requests. |
| #define | [I3C\_CCC\_ENEC\_EVT\_ENHJ](group__i3c__ccc.md#ga7e705ac95643d0462ac4275eed42153a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Enable Events (ENEC) - Hot-Join Event. |
| #define | [I3C\_CCC\_ENEC\_EVT\_ALL](group__i3c__ccc.md#ga7860289b621c4243401e1df21cd84d66)   ([I3C\_CCC\_ENEC\_EVT\_ENINTR](group__i3c__ccc.md#gafe40d9b2ccedca40071c47929ff66e65) | [I3C\_CCC\_ENEC\_EVT\_ENCR](group__i3c__ccc.md#gad73e2e9f31f3a02f52b20d77e64671ff) | [I3C\_CCC\_ENEC\_EVT\_ENHJ](group__i3c__ccc.md#ga7e705ac95643d0462ac4275eed42153a)) |
| #define | [I3C\_CCC\_DISEC\_EVT\_DISINTR](group__i3c__ccc.md#gaf6da0458f1ae2d45ae7337cd4e576484)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Disable Events (DISEC) - Target Interrupt Requests. |
| #define | [I3C\_CCC\_DISEC\_EVT\_DISCR](group__i3c__ccc.md#ga1f1612a16d2cb68b66f1ca85ba6f450a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Disable Events (DISEC) - Controller Role Requests. |
| #define | [I3C\_CCC\_DISEC\_EVT\_DISHJ](group__i3c__ccc.md#gac3ffda84f683f99a0d4e0ad67adfd675)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Disable Events (DISEC) - Hot-Join Event. |
| #define | [I3C\_CCC\_DISEC\_EVT\_ALL](group__i3c__ccc.md#gaf177b8fcb7412671a3b8c418336ddde4)   ([I3C\_CCC\_DISEC\_EVT\_DISINTR](group__i3c__ccc.md#gaf6da0458f1ae2d45ae7337cd4e576484) | [I3C\_CCC\_DISEC\_EVT\_DISCR](group__i3c__ccc.md#ga1f1612a16d2cb68b66f1ca85ba6f450a) | [I3C\_CCC\_DISEC\_EVT\_DISHJ](group__i3c__ccc.md#gac3ffda84f683f99a0d4e0ad67adfd675)) |
| #define | [I3C\_CCC\_EVT\_INTR](group__i3c__ccc.md#ga14cbf3628627f965336ac3740858aeea)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Events - Target Interrupt Requests. |
| #define | [I3C\_CCC\_EVT\_CR](group__i3c__ccc.md#gad515a978c4912ef0c0444f14e51d8e8f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Events - Controller Role Requests. |
| #define | [I3C\_CCC\_EVT\_HJ](group__i3c__ccc.md#gaedf65a98d59de51a533ff3d2f8cf075a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Events - Hot-Join Event. |
| #define | [I3C\_CCC\_EVT\_ALL](group__i3c__ccc.md#ga8ff2055f745c4970bd41850bfd5b2aff)   ([I3C\_CCC\_EVT\_INTR](group__i3c__ccc.md#ga14cbf3628627f965336ac3740858aeea) | [I3C\_CCC\_EVT\_CR](group__i3c__ccc.md#gad515a978c4912ef0c0444f14e51d8e8f) | [I3C\_CCC\_EVT\_HJ](group__i3c__ccc.md#gaedf65a98d59de51a533ff3d2f8cf075a)) |
|  | Bitmask for all events. |
| #define | [I3C\_CCC\_GETSTATUS\_PROTOCOL\_ERR](group__i3c__ccc.md#gaee3dd61e9ac723a90868c610d0179b7d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | GETSTATUS Format 1 - Protocol Error bit. |
| #define | [I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_SHIFT](group__i3c__ccc.md#ga8aca4592e579411a2c17f80ad682d93f)   6 |
|  | GETSTATUS Format 1 - Activity Mode bit shift value. |
| #define | [I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_MASK](group__i3c__ccc.md#ga1006146ca810c06674fbee0ee1f66286)   (0x03U << [I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_SHIFT](group__i3c__ccc.md#ga8aca4592e579411a2c17f80ad682d93f)) |
|  | GETSTATUS Format 1 - Activity Mode bitmask. |
| #define | [I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE](group__i3c__ccc.md#ga660e179384e9426b498cd62da5665b15)(status) |
|  | GETSTATUS Format 1 - Activity Mode. |
| #define | [I3C\_CCC\_GETSTATUS\_NUM\_INT\_SHIFT](group__i3c__ccc.md#ga1c07ae6c80088b8336f7f2d728487606)   0 |
|  | GETSTATUS Format 1 - Number of Pending Interrupts bit shift value. |
| #define | [I3C\_CCC\_GETSTATUS\_NUM\_INT\_MASK](group__i3c__ccc.md#gae0bcc3ea13a34f63b073d63569d2e53a)   (0x0FU << [I3C\_CCC\_GETSTATUS\_NUM\_INT\_SHIFT](group__i3c__ccc.md#ga1c07ae6c80088b8336f7f2d728487606)) |
|  | GETSTATUS Format 1 - Number of Pending Interrupts bitmask. |
| #define | [I3C\_CCC\_GETSTATUS\_NUM\_INT](group__i3c__ccc.md#ga1436dc4b9f71c6f61fd3e3331857f3bd)(status) |
|  | GETSTATUS Format 1 - Number of Pending Interrupts. |
| #define | [I3C\_CCC\_GETSTATUS\_PRECR\_DEEP\_SLEEP\_DETECTED](group__i3c__ccc.md#ga94afb0ebcfce55b85fc4a81953b4178a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | GETSTATUS Format 2 - PERCR - Deep Sleep Detected bit. |
| #define | [I3C\_CCC\_GETSTATUS\_PRECR\_HANDOFF\_DELAY\_NACK](group__i3c__ccc.md#gadda1781cae312f4e588c3d3dcfa74f38)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | GETSTATUS Format 2 - PERCR - Handoff Delay NACK. |
| #define | [I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_MAX](group__i3c__ccc.md#ga65ed8d5c2e6f562215674217f974d608)   0 |
|  | Get Max Data Speed (GETMXDS) - Default Max Sustained Data Rate. |
| #define | [I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_8MHZ](group__i3c__ccc.md#gaac6dec9aee1e1d5a56c964a4d1fe32b1)   1 |
|  | Get Max Data Speed (GETMXDS) - 8MHz Max Sustained Data Rate. |
| #define | [I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_6MHZ](group__i3c__ccc.md#gae1ff27ad2b8c9119e2efa88c0a696555)   2 |
|  | Get Max Data Speed (GETMXDS) - 6MHz Max Sustained Data Rate. |
| #define | [I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_4MHZ](group__i3c__ccc.md#ga409666d6a17b53e518d702863826eb28)   3 |
|  | Get Max Data Speed (GETMXDS) - 4MHz Max Sustained Data Rate. |
| #define | [I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_2MHZ](group__i3c__ccc.md#ga5a329b3fa12ecafd6958b05bab163a5c)   4 |
|  | Get Max Data Speed (GETMXDS) - 2MHz Max Sustained Data Rate. |
| #define | [I3C\_CCC\_GETMXDS\_TSCO\_8NS](group__i3c__ccc.md#gad5e417bc3cabf8a915d1e7938415125a)   0 |
|  | Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 8ns. |
| #define | [I3C\_CCC\_GETMXDS\_TSCO\_9NS](group__i3c__ccc.md#gaaee475f82f3a3759c7d62bb48082ebc2)   1 |
|  | Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 9ns. |
| #define | [I3C\_CCC\_GETMXDS\_TSCO\_10NS](group__i3c__ccc.md#ga5e264e39aa2d4b602ec5e3218708e2f6)   2 |
|  | Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 10ns. |
| #define | [I3C\_CCC\_GETMXDS\_TSCO\_11NS](group__i3c__ccc.md#ga2b27c9023f447da9c474c078091cf580)   3 |
|  | Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 11ns. |
| #define | [I3C\_CCC\_GETMXDS\_TSCO\_12NS](group__i3c__ccc.md#ga06d33d1884a30d179aace82af956d62d)   4 |
|  | Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 12ns. |
| #define | [I3C\_CCC\_GETMXDS\_TSCO\_GT\_12NS](group__i3c__ccc.md#ga5be034f241ccfb59534ae247d2e31d85)   7 |
|  | Get Max Data Speed (GETMXDS) - Clock to Data Turnaround > 12ns. |
| #define | [I3C\_CCC\_GETMXDS\_MAXWR\_DEFINING\_BYTE\_SUPPORT](group__i3c__ccc.md#ga43fa03b6fea48cca06d07e962c5c04ef)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Get Max Data Speed (GETMXDS) - maxWr - Optional Defining Byte Support. |
| #define | [I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_SHIFT](group__i3c__ccc.md#ga9bfab32baa69d2e437167afa31a6b428)   0 |
|  | Get Max Data Speed (GETMXDS) - Max Sustained Data Rate bit shift value. |
| #define | [I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_MASK](group__i3c__ccc.md#ga5f4c6dde339c3467bdb3aea0d680d01f)   (0x07U << [I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_SHIFT](group__i3c__ccc.md#ga9bfab32baa69d2e437167afa31a6b428)) |
|  | Get Max Data Speed (GETMXDS) - Max Sustained Data Rate bitmask. |
| #define | [I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL](group__i3c__ccc.md#gae61b18d964e575809a1ebe2189aae028)(maxwr) |
|  | Get Max Data Speed (GETMXDS) - maxWr - Max Sustained Data Rate. |
| #define | [I3C\_CCC\_GETMXDS\_MAXRD\_W2R\_PERMITS\_STOP\_BETWEEN](group__i3c__ccc.md#gaf5b95266cc911a37a3e46565b7601970)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Get Max Data Speed (GETMXDS) - maxRd - Write-to-Read Permits Stop Between. |
| #define | [I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_SHIFT](group__i3c__ccc.md#gaf9c4764b0953c28af83b4fe06df0ebc3)   3 |
|  | Get Max Data Speed (GETMXDS) - maxRd - Clock to Data Turnaround bit shift value. |
| #define | [I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_MASK](group__i3c__ccc.md#ga41958f7756cc5dec1c0546e7832b764a)   (0x07U << [I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_SHIFT](group__i3c__ccc.md#gaf9c4764b0953c28af83b4fe06df0ebc3)) |
|  | Get Max Data Speed (GETMXDS) - maxRd - Clock to Data Turnaround bitmask. |
| #define | [I3C\_CCC\_GETMXDS\_MAXRD\_TSCO](group__i3c__ccc.md#ga8284130d363dd1898de44c572b3d566c)(maxrd) |
|  | Get Max Data Speed (GETMXDS) - maxRd - Clock to Data Turnaround. |
| #define | [I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_SHIFT](group__i3c__ccc.md#ga474f4d9ec309436863bdf0d7151de95f)   0 |
|  | Get Max Data Speed (GETMXDS) - maxRd - Max Sustained Data Rate bit shift value. |
| #define | [I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_MASK](group__i3c__ccc.md#gad8b14f71cc1d5c1a0daa27703ab0c774)   (0x07U << [I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_SHIFT](group__i3c__ccc.md#ga474f4d9ec309436863bdf0d7151de95f)) |
|  | Get Max Data Speed (GETMXDS) - maxRd - Max Sustained Data Rate bitmask. |
| #define | [I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL](group__i3c__ccc.md#gaf5ac7364357e1e123adddcbfc134a0be)(maxrd) |
|  | Get Max Data Speed (GETMXDS) - maxRd - Max Sustained Data Rate. |
| #define | [I3C\_CCC\_GETMXDS\_CRDHLY1\_SET\_BUS\_ACT\_STATE](group__i3c__ccc.md#ga9aa4eaf8a537323883d242e9ebb9a985)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Get Max Data Speed (GETMXDS) - CRDHLY1 - Set Bus Activity State bit shift value. |
| #define | [I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE\_SHIFT](group__i3c__ccc.md#ga7853f150811ae69b09520628d774a033)   0 |
|  | Get Max Data Speed (GETMXDS) - CRDHLY1 - Controller Handoff Activity State bit shift value. |
| #define | [I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE\_MASK](group__i3c__ccc.md#ga9ad046b7ec49bbca3f70a5a30fb1524b)   (0x03U << [I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE\_SHIFT](group__i3c__ccc.md#ga7853f150811ae69b09520628d774a033)) |
|  | Get Max Data Speed (GETMXDS) - CRDHLY1 - Controller Handoff Activity State bitmask. |
| #define | [I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE](group__i3c__ccc.md#gab43a5adbcf158086d23c5d796a7e9399)(crhdly1) |
|  | Get Max Data Speed (GETMXDS) - CRDHLY1 - Controller Handoff Activity State. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_DDR](group__i3c__ccc.md#gab984c6a18a555e4a3c0552684083e330)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR-DDR mode bit. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_TSP](group__i3c__ccc.md#gafe33491b778aa806977a98c3bd12a339)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR-TSP mode bit. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_TSL](group__i3c__ccc.md#gae9b98ab62745f041e4fe6e89ecd3b0e6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR-TSL mode bit. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_BT](group__i3c__ccc.md#gaac01f085ed1af56d686a33694744081c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR-BT mode bit. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_MODE](group__i3c__ccc.md#gaae9483f4d5de3ba092b870b20e6b5f4a)(x) |
|  | Get Optional Feature Capabilities Byte 1 (GETCAPS) - HDR Mode. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_MODE0](group__i3c__ccc.md#gad1389fc52c3fec4d6206bc56566bbf5d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR Mode 0. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_MODE1](group__i3c__ccc.md#gacfd20baf528fcceca7f71719e15d5ea0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR Mode 1. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_MODE2](group__i3c__ccc.md#ga9e5581743cbbe7363bb0919b95148d85)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR Mode 2. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_MODE3](group__i3c__ccc.md#ga97b146596467f410ce9f063365ac9aaf)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR Mode 3. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_MODE4](group__i3c__ccc.md#ga0dd98eeb74f493bfb04aeb698e656772)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR Mode 4. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_MODE5](group__i3c__ccc.md#ga99bff02c40ccb15797dcf10c6dc00e87)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR Mode 5. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_MODE6](group__i3c__ccc.md#ga12cead0a8ceb518a5c897f22b1d3dd64)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR Mode 6. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_MODE7](group__i3c__ccc.md#ga8b3373f18c0e3b365cc199c19ae82fb0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Get Optional Feature Capabilities Byte 1 (GETCAPS) Format 1 - HDR Mode 7. |
| #define | [I3C\_CCC\_GETCAPS2\_HDRDDR\_WRITE\_ABORT](group__i3c__ccc.md#ga1c2ceeaa44ee641c3d05176baf7e681d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Get Optional Feature Capabilities Byte 2 (GETCAPS) Format 1 - HDR-DDR Write Abort bit. |
| #define | [I3C\_CCC\_GETCAPS2\_HDRDDR\_ABORT\_CRC](group__i3c__ccc.md#ga8faf5ff5b2542a309f114ce4d6d11640)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Get Optional Feature Capabilities Byte 2 (GETCAPS) Format 1 - HDR-DDR Abort CRC bit. |
| #define | [I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_SHIFT](group__i3c__ccc.md#ga9ad0caec4913cd9454fa4c939555ad32)   4 |
|  | Get Optional Feature Capabilities Byte 2 (GETCAPS) Format 1 - Group Address Capabilities bit shift value. |
| #define | [I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_MASK](group__i3c__ccc.md#ga64f58d1aaf847cf4a7811b20cca13b55)   (0x03U << [I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_SHIFT](group__i3c__ccc.md#ga9ad0caec4913cd9454fa4c939555ad32)) |
|  | Get Optional Feature Capabilities Byte 2 (GETCAPS) Format 1 - Group Address Capabilities bitmask. |
| #define | [I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP](group__i3c__ccc.md#gabeb9acdabd6dce2117e9f5830673b2ed)(getcaps2) |
|  | Get Optional Feature Capabilities Byte 2 (GETCAPS) Format 1 - Group Address Capabilities. |
| #define | [I3C\_CCC\_GETCAPS2\_SPEC\_VER\_SHIFT](group__i3c__ccc.md#ga558dc49b9856d49ccd77bfac88fbfc7c)   0 |
|  | Get Optional Feature Capabilities Byte 2 (GETCAPS) Format 1 - I3C 1.x Specification Version bit shift value. |
| #define | [I3C\_CCC\_GETCAPS2\_SPEC\_VER\_MASK](group__i3c__ccc.md#gae0015aa7768a8d5c18426a47cdbb67f8)   (0x0FU << [I3C\_CCC\_GETCAPS2\_SPEC\_VER\_SHIFT](group__i3c__ccc.md#ga558dc49b9856d49ccd77bfac88fbfc7c)) |
|  | Get Optional Feature Capabilities Byte 2 (GETCAPS) Format 1 - I3C 1.x Specification Version bitmask. |
| #define | [I3C\_CCC\_GETCAPS2\_SPEC\_VER](group__i3c__ccc.md#ga093449c1cf029bddf1a25181cbfed570)(getcaps2) |
|  | Get Optional Feature Capabilities Byte 2 (GETCAPS) Format 1 - I3C 1.x Specification Version. |
| #define | [I3C\_CCC\_GETCAPS3\_MLANE\_SUPPORT](group__i3c__ccc.md#gaf0a2358f0f5f46c5fa1c084373f09be1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Get Optional Feature Capabilities Byte 3 (GETCAPS) Format 1 - Multi-Lane Data Transfer Support bit. |
| #define | [I3C\_CCC\_GETCAPS3\_D2DXFER\_SUPPORT](group__i3c__ccc.md#ga08cc3c3976195642282e00ba00c1b283)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Get Optional Feature Capabilities Byte 3 (GETCAPS) Format 1 - Device to Device Transfer (D2DXFER) Support bit. |
| #define | [I3C\_CCC\_GETCAPS3\_D2DXFER\_IBI\_CAPABLE](group__i3c__ccc.md#ga73829cd436decbe55d2290dc750b3918)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Get Optional Feature Capabilities Byte 3 (GETCAPS) Format 1 - Device to Device Transfer (D2DXFER) IBI Capable bit. |
| #define | [I3C\_CCC\_GETCAPS3\_GETCAPS\_DEFINING\_BYTE\_SUPPORT](group__i3c__ccc.md#gaf40cc6cc08619363056e9650453a9a26)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Get Optional Feature Capabilities Byte 3 (GETCAPS) Format 1 - Defining Byte Support in GETCAPS bit. |
| #define | [I3C\_CCC\_GETCAPS3\_GETSTATUS\_DEFINING\_BYTE\_SUPPORT](group__i3c__ccc.md#gafbf1e9c947c40d70ae1c45991d093570)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Get Optional Feature Capabilities Byte 3 (GETCAPS) Format 1 - Defining Byte Support in GETSTATUS bit. |
| #define | [I3C\_CCC\_GETCAPS3\_HDRBT\_CRC32\_SUPPORT](group__i3c__ccc.md#ga3575eb8aa6fc3b49f2115104dcdfaeec)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Get Optional Feature Capabilities Byte 3 (GETCAPS) Format 1 - HDR-BT CRC-32 Support bit. |
| #define | [I3C\_CCC\_GETCAPS3\_IBI\_MDR\_PENDING\_READ\_NOTIFICATION](group__i3c__ccc.md#gac13d1465aa4222be0acccbf5303f3f3e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Get Optional Feature Capabilities Byte 3 (GETCAPS) Format 1 - IBI MDB Support for Pending Read Notification bit. |
| #define | [I3C\_CCC\_GETCAPS\_TESTPAT1](group__i3c__ccc.md#ga541ed236f06c20ca98e32d5a17788754)   0xA5 |
|  | Get Fixed Test Pattern (GETCAPS) Format 2 - Fixed Test Pattern Byte 1. |
| #define | [I3C\_CCC\_GETCAPS\_TESTPAT2](group__i3c__ccc.md#gafdb7ed7cc72efeb7cd62435084b1b40f)   0x5A |
|  | Get Fixed Test Pattern (GETCAPS) Format 2 - Fixed Test Pattern Byte 2. |
| #define | [I3C\_CCC\_GETCAPS\_TESTPAT3](group__i3c__ccc.md#ga1720b3f54ade943f627b6a4e7284139a)   0xA5 |
|  | Get Fixed Test Pattern (GETCAPS) Format 2 - Fixed Test Pattern Byte 3. |
| #define | [I3C\_CCC\_GETCAPS\_TESTPAT4](group__i3c__ccc.md#ga2391e23e0b17351e3c28048b85d98ea6)   0x5A |
|  | Get Fixed Test Pattern (GETCAPS) Format 2 - Fixed Test Pattern Byte 4. |
| #define | [I3C\_CCC\_GETCAPS\_TESTPAT](group__i3c__ccc.md#ga98ee1cc4c436219b9639c5710fa6911b)   0xA55AA55A |
|  | Get Fixed Test Pattern (GETCAPS) Format 2 - Fixed Test Pattern Word in Big Endian. |
| #define | [I3C\_CCC\_GETCAPS\_CRCAPS1\_HJ\_SUPPORT](group__i3c__ccc.md#gad833335c6edb018edb66b99e1dfc16f7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Get Controller Handoff Capabilities Byte 1 (GETCAPS) Format 2 - Hot-Join Support. |
| #define | [I3C\_CCC\_GETCAPS\_CRCAPS1\_GRP\_MANAGEMENT\_SUPPORT](group__i3c__ccc.md#ga86b22acbba045b037b4ae14abf4b6e5c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Get Controller Handoff Capabilities Byte 1 (GETCAPS) Format 2 - Group Management Support. |
| #define | [I3C\_CCC\_GETCAPS\_CRCAPS1\_ML\_SUPPORT](group__i3c__ccc.md#ga438621df282f451083e9ab9b1b59a2e3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Get Controller Handoff Capabilities Byte 1 (GETCAPS) Format 2 - Multi-Lane Support. |
| #define | [I3C\_CCC\_GETCAPS\_CRCAPS2\_IBI\_TIR\_SUPPORT](group__i3c__ccc.md#ga5bedcb1cb3769ae69779c0b2125b4b21)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Get Controller Handoff Capabilities Byte 2 (GETCAPS) Format 2 - In-Band Interrupt Support. |
| #define | [I3C\_CCC\_GETCAPS\_CRCAPS2\_CONTROLLER\_PASSBACK](group__i3c__ccc.md#ga3a49b8a44676888fe600aa6b42cc52c6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Get Controller Handoff Capabilities Byte 2 (GETCAPS) Format 2 - Controller Pass-Back. |
| #define | [I3C\_CCC\_GETCAPS\_CRCAPS2\_DEEP\_SLEEP\_CAPABLE](group__i3c__ccc.md#gad81d9a56d02db7e8a87279d8772adbec)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Get Controller Handoff Capabilities Byte 2 (GETCAPS) Format 2 - Deep Sleep Capable. |
| #define | [I3C\_CCC\_GETCAPS\_CRCAPS2\_DELAYED\_CONTROLLER\_HANDOFF](group__i3c__ccc.md#gada1a84b1394d6a72dd49e1c87307fbef)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Get Controller Handoff Capabilities Byte 2 (GETCAPS) Format 2 - Deep Sleep Capable. |
| #define | [I3C\_CCC\_GETCAPS\_VTCAP1\_VITRUAL\_TARGET\_TYPE\_SHIFT](group__i3c__ccc.md#ga378e451327b212275c748480ada15a31)   0 |
|  | Get Capabilities (GETCAPS) - VTCAP1 - Virtual Target Type bit shift value. |
| #define | [I3C\_CCC\_GETCAPS\_VTCAP1\_VITRUAL\_TARGET\_TYPE\_MASK](group__i3c__ccc.md#ga382e8db432a701a8b2f6c8be6aba81a8)   (0x07U << [I3C\_CCC\_GETCAPS\_VTCAP1\_VITRUAL\_TARGET\_TYPE\_SHIFT](group__i3c__ccc.md#ga378e451327b212275c748480ada15a31)) |
|  | Get Capabilities (GETCAPS) - VTCAP1 - Virtual Target Type bitmask. |
| #define | [I3C\_CCC\_GETCAPS\_VTCAP1\_VITRUAL\_TARGET\_TYPE](group__i3c__ccc.md#ga9d0153d2e0b01a045e59e4acf4446206)(vtcap1) |
|  | Get Capabilities (GETCAPS) - VTCAP1 - Virtual Target Type. |
| #define | [I3C\_CCC\_GETCAPS\_VTCAP1\_SIDE\_EFFECTS](group__i3c__ccc.md#gaca37ffb4f223c7b723a1b2ed881d28f7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Get Virtual Target Capabilities Byte 1 (GETCAPS) Format 2 - Side Effects. |
| #define | [I3C\_CCC\_GETCAPS\_VTCAP1\_SHARED\_PERIPH\_DETECT](group__i3c__ccc.md#gad1c0b63bb26be245e781e5d32d75dd15)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Get Virtual Target Capabilities Byte 1 (GETCAPS) Format 2 - Shared Peripheral Detect. |
| #define | [I3C\_CCC\_GETCAPS\_VTCAP2\_INTERRUPT\_REQUESTS\_SHIFT](group__i3c__ccc.md#gafbd58c1713c93692b49e06508089397c)   0 |
|  | Get Capabilities (GETCAPS) - VTCAP2 - Interrupt Requests bit shift value. |
| #define | [I3C\_CCC\_GETCAPS\_VTCAP2\_INTERRUPT\_REQUESTS\_MASK](group__i3c__ccc.md#gad39e1c3d38b29937166345133ad373d1)   (0x03U << [I3C\_CCC\_GETCAPS\_VTCAP2\_INTERRUPT\_REQUESTS\_SHIFT](group__i3c__ccc.md#gafbd58c1713c93692b49e06508089397c)) |
|  | Get Capabilities (GETCAPS) - VTCAP2 - Interrupt Requests bitmask. |
| #define | [I3C\_CCC\_GETCAPS\_VTCAP2\_INTERRUPT\_REQUESTS](group__i3c__ccc.md#ga8ee2a538a2b5efa2e02540aac392c685)(vtcap2) |
|  | Get Capabilities (GETCAPS) - VTCAP2 - Interrupt Requests. |
| #define | [I3C\_CCC\_GETCAPS\_VTCAP2\_ADDRESS\_REMAPPING](group__i3c__ccc.md#ga1b7562342dbf9fe443386943527d5f29)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Get Virtual Target Capabilities Byte 2 (GETCAPS) Format 2 - Address Remapping. |
| #define | [I3C\_CCC\_GETCAPS\_VTCAP2\_BUS\_CONTEXT\_AND\_COND\_SHIFT](group__i3c__ccc.md#gadada56c704f75606cbf4548c79981756)   3 |
|  | Get Capabilities (GETCAPS) - VTCAP2 - Bus Context and Condition bit shift value. |
| #define | [I3C\_CCC\_GETCAPS\_VTCAP2\_BUS\_CONTEXT\_AND\_COND\_MASK](group__i3c__ccc.md#gadc61e60fbc59aca1ff813098f51ca56e)   (0x03U << [I3C\_CCC\_GETCAPS\_VTCAP2\_BUS\_CONTEXT\_AND\_COND\_SHIFT](group__i3c__ccc.md#gadada56c704f75606cbf4548c79981756)) |
|  | Get Capabilities (GETCAPS) - VTCAP2 - Bus Context and Condition bitmask. |
| #define | [I3C\_CCC\_GETCAPS\_VTCAP2\_BUS\_CONTEXT\_AND\_COND](group__i3c__ccc.md#ga56112189be57287691d64eabfaa32910)(vtcap2) |
|  | Get Capabilities (GETCAPS) - VTCAP2 - Bus Context and Condition. |

| Enumerations | |
| --- | --- |
| enum | [i3c\_ccc\_getstatus\_fmt](group__i3c__ccc.md#ga75934ea02ef8eb1c737da3ebfd368648) { [GETSTATUS\_FORMAT\_1](group__i3c__ccc.md#gga75934ea02ef8eb1c737da3ebfd368648ae42215e3898baa40cc90e35c5777b57b) , [GETSTATUS\_FORMAT\_2](group__i3c__ccc.md#gga75934ea02ef8eb1c737da3ebfd368648a08af2d5d884af32b46b7e0f2f429c68f) } |
|  | Indicate which format of GETSTATUS to use. [More...](group__i3c__ccc.md#ga75934ea02ef8eb1c737da3ebfd368648) |
| enum | [i3c\_ccc\_getstatus\_defbyte](group__i3c__ccc.md#ga1977f86d4865a97047119e5b3fbcb172) { [GETSTATUS\_FORMAT\_2\_TGTSTAT](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172ac485e9d12c2a4855fd40ddcb6ab938eb) = 0x00U , [GETSTATUS\_FORMAT\_2\_PRECR](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172a536a82ce39767e0cd3c25ebc56974877) = 0x91U , [GETSTATUS\_FORMAT\_2\_INVALID](group__i3c__ccc.md#gga1977f86d4865a97047119e5b3fbcb172a83ccf53b5520866ec71e2c0824347e19) = 0x100U } |
|  | Defining byte values for GETSTATUS Format 2. [More...](group__i3c__ccc.md#ga1977f86d4865a97047119e5b3fbcb172) |
| enum | [i3c\_ccc\_getcaps\_fmt](group__i3c__ccc.md#gaa22cc011b619b1819416b0aa26f85958) { [GETCAPS\_FORMAT\_1](group__i3c__ccc.md#ggaa22cc011b619b1819416b0aa26f85958a4d5d9ad0745a71bddbea1da09f0b49a0) , [GETCAPS\_FORMAT\_2](group__i3c__ccc.md#ggaa22cc011b619b1819416b0aa26f85958a6bb52959483be5cfc0ddc31f9a574620) } |
|  | Indicate which format of GETCAPS to use. [More...](group__i3c__ccc.md#gaa22cc011b619b1819416b0aa26f85958) |
| enum | [i3c\_ccc\_getcaps\_defbyte](group__i3c__ccc.md#gadf1c0363ec0d6db7634cb03bd2d402c2) {     [GETCAPS\_FORMAT\_2\_TGTCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a494b6a8c368d34d96433041de7e7448e) = 0x00U , [GETCAPS\_FORMAT\_2\_TESTPAT](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2ae4cd2f2c4638057ae8fdcceb9d7ba740) = 0x5AU , [GETCAPS\_FORMAT\_2\_CRCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a2081a7f62d3175a8b84454daf54f3484) = 0x91U , [GETCAPS\_FORMAT\_2\_VTCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2ab37ceea59619902ac073183694852984) = 0x93U ,     [GETCAPS\_FORMAT\_2\_DBGCAPS](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2aaf97763f5fe2819c502e3923501c86d0) = 0xD7U , [GETCAPS\_FORMAT\_2\_INVALID](group__i3c__ccc.md#ggadf1c0363ec0d6db7634cb03bd2d402c2a2cd7e3a4d3bce532dfda07e9f9ae8c86) = 0x100   } |
|  | Enum for I3C Get Capabilities (GETCAPS) Format 2 Defining Byte Values. [More...](group__i3c__ccc.md#gadf1c0363ec0d6db7634cb03bd2d402c2) |
| enum | [i3c\_ccc\_rstact\_defining\_byte](group__i3c__ccc.md#ga61e1a1945a39b374edee5b75fbeb27d1) {     [I3C\_CCC\_RSTACT\_NO\_RESET](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1aaba42ef747745ca61cf3aa91068fe7c2) = 0x00U , [I3C\_CCC\_RSTACT\_PERIPHERAL\_ONLY](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a5875b237e23a0a2ad01051ca1d612476) = 0x01U , [I3C\_CCC\_RSTACT\_RESET\_WHOLE\_TARGET](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1af7b7e39dd7a9b214e13f1bdc7f869879) = 0x02U , [I3C\_CCC\_RSTACT\_DEBUG\_NETWORK\_ADAPTER](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1a860a409d86fdb60d9d03df670a724519) = 0x03U ,     [I3C\_CCC\_RSTACT\_VIRTUAL\_TARGET\_DETECT](group__i3c__ccc.md#gga61e1a1945a39b374edee5b75fbeb27d1ac56441fa6318702856ca6d2ae5ea328e) = 0x04U   } |
|  | Enum for I3C Reset Action (RSTACT) Defining Byte Values. [More...](group__i3c__ccc.md#ga61e1a1945a39b374edee5b75fbeb27d1) |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [i3c\_ccc\_is\_payload\_broadcast](group__i3c__ccc.md#gaaf692d0b89fd62a61d93f1577b25ce25) (const struct [i3c\_ccc\_payload](structi3c__ccc__payload.md) \*payload) |
|  | Test if I3C CCC payload is for broadcast. |
| int | [i3c\_ccc\_do\_getbcr](group__i3c__ccc.md#ga7d5bb9c8fd88721b858180f503c1af4c) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, struct [i3c\_ccc\_getbcr](structi3c__ccc__getbcr.md) \*bcr) |
|  | Get BCR from a target. |
| int | [i3c\_ccc\_do\_getdcr](group__i3c__ccc.md#ga7f886c0dbe0afec07f5678b574dc1101) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, struct [i3c\_ccc\_getdcr](structi3c__ccc__getdcr.md) \*dcr) |
|  | Get DCR from a target. |
| int | [i3c\_ccc\_do\_getpid](group__i3c__ccc.md#ga949810a9a7c862d00ce4eec7e2c4d7df) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, struct [i3c\_ccc\_getpid](structi3c__ccc__getpid.md) \*pid) |
|  | Get PID from a target. |
| int | [i3c\_ccc\_do\_rstact\_all](group__i3c__ccc.md#ga40294e43357f46338a6542f9a03d7ce7) (const struct [device](structdevice.md) \*controller, enum [i3c\_ccc\_rstact\_defining\_byte](group__i3c__ccc.md#ga61e1a1945a39b374edee5b75fbeb27d1) action) |
|  | Broadcast RSTACT to reset I3C Peripheral. |
| int | [i3c\_ccc\_do\_rstdaa\_all](group__i3c__ccc.md#gab1102467bb92a2aff7c9c1a66dd273a7) (const struct [device](structdevice.md) \*controller) |
|  | Broadcast RSTDAA to reset dynamic addresses for all targets. |
| int | [i3c\_ccc\_do\_setdasa](group__i3c__ccc.md#gae4be97aae166be3b6e794fd77c8be6f8) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Set Dynamic Address from Static Address for a target. |
| int | [i3c\_ccc\_do\_setnewda](group__i3c__ccc.md#ga6d19dc9d3b421b4c936c6183977c4eec) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, struct [i3c\_ccc\_address](structi3c__ccc__address.md) new\_da) |
|  | Set New Dynamic Address for a target. |
| int | [i3c\_ccc\_do\_events\_all\_set](group__i3c__ccc.md#gaf5fbaf2108053df855c95233181dc580) (const struct [device](structdevice.md) \*controller, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable, struct [i3c\_ccc\_events](structi3c__ccc__events.md) \*events) |
|  | Broadcast ENEC/DISEC to enable/disable target events. |
| int | [i3c\_ccc\_do\_events\_set](group__i3c__ccc.md#gaf6575647b4b8f858f90bf2785a0f0d49) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable, struct [i3c\_ccc\_events](structi3c__ccc__events.md) \*events) |
|  | Direct CCC ENEC/DISEC to enable/disable target events. |
| int | [i3c\_ccc\_do\_setmwl\_all](group__i3c__ccc.md#ga66c8c6318134d6287f4a14f6c31af02d) (const struct [device](structdevice.md) \*controller, const struct [i3c\_ccc\_mwl](structi3c__ccc__mwl.md) \*mwl) |
|  | Broadcast SETMWL to Set Maximum Write Length. |
| int | [i3c\_ccc\_do\_setmwl](group__i3c__ccc.md#gab3de109c73dd58f6d2cf0a9229408f49) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, const struct [i3c\_ccc\_mwl](structi3c__ccc__mwl.md) \*mwl) |
|  | Single target SETMWL to Set Maximum Write Length. |
| int | [i3c\_ccc\_do\_getmwl](group__i3c__ccc.md#gaf1077e3d6cf8a7e1f0e02e985058e507) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, struct [i3c\_ccc\_mwl](structi3c__ccc__mwl.md) \*mwl) |
|  | Single target GETMWL to Get Maximum Write Length. |
| int | [i3c\_ccc\_do\_setmrl\_all](group__i3c__ccc.md#ga2542f4ebcc0c2bb31bc8e334955620b0) (const struct [device](structdevice.md) \*controller, const struct [i3c\_ccc\_mrl](structi3c__ccc__mrl.md) \*mrl, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) has\_ibi\_size) |
|  | Broadcast SETMRL to Set Maximum Read Length. |
| int | [i3c\_ccc\_do\_setmrl](group__i3c__ccc.md#ga6e4f26d23919a619c89624b15d16390a) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, const struct [i3c\_ccc\_mrl](structi3c__ccc__mrl.md) \*mrl) |
|  | Single target SETMRL to Set Maximum Read Length. |
| int | [i3c\_ccc\_do\_getmrl](group__i3c__ccc.md#gac4331a4c7dbb7af0eaea63b01bb08485) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, struct [i3c\_ccc\_mrl](structi3c__ccc__mrl.md) \*mrl) |
|  | Single target GETMRL to Get Maximum Read Length. |
| int | [i3c\_ccc\_do\_getstatus](group__i3c__ccc.md#ga4fe9d056a5ac78ff83513763a71c7dfe) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, union [i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md) \*status, enum [i3c\_ccc\_getstatus\_fmt](group__i3c__ccc.md#ga75934ea02ef8eb1c737da3ebfd368648) fmt, enum [i3c\_ccc\_getstatus\_defbyte](group__i3c__ccc.md#ga1977f86d4865a97047119e5b3fbcb172) defbyte) |
|  | Single target GETSTATUS to Get Target Status. |
| static int | [i3c\_ccc\_do\_getstatus\_fmt1](group__i3c__ccc.md#ga1cb2804fc7dcbb322cd26001d7953c95) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, union [i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md) \*status) |
|  | Single target GETSTATUS to Get Target Status (Format 1). |
| static int | [i3c\_ccc\_do\_getstatus\_fmt2](group__i3c__ccc.md#ga4eaaaf7b7e9f2f8dd657d4f6a0de8bfb) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, union [i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md) \*status, enum [i3c\_ccc\_getstatus\_defbyte](group__i3c__ccc.md#ga1977f86d4865a97047119e5b3fbcb172) defbyte) |
|  | Single target GETSTATUS to Get Target Status (Format 2). |
| int | [i3c\_ccc\_do\_getcaps](group__i3c__ccc.md#ga94df3bbf8d0de54edd57e2ab4d44474e) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, union [i3c\_ccc\_getcaps](unioni3c__ccc__getcaps.md) \*caps, enum [i3c\_ccc\_getcaps\_fmt](group__i3c__ccc.md#gaa22cc011b619b1819416b0aa26f85958) fmt, enum [i3c\_ccc\_getcaps\_defbyte](group__i3c__ccc.md#gadf1c0363ec0d6db7634cb03bd2d402c2) defbyte) |
|  | Single target GETCAPS to Get Target Status. |
| static int | [i3c\_ccc\_do\_getcaps\_fmt1](group__i3c__ccc.md#gaeca8e7c74ee867cdeedf586f5af07a89) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, union [i3c\_ccc\_getcaps](unioni3c__ccc__getcaps.md) \*caps) |
|  | Single target GETCAPS to Get Capabilities (Format 1). |
| static int | [i3c\_ccc\_do\_getcaps\_fmt2](group__i3c__ccc.md#gaaa684ac58000e05316eac016a7f048cd) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, union [i3c\_ccc\_getcaps](unioni3c__ccc__getcaps.md) \*caps, enum [i3c\_ccc\_getcaps\_defbyte](group__i3c__ccc.md#gadf1c0363ec0d6db7634cb03bd2d402c2) defbyte) |
|  | Single target GETCAPS to Get Capabilities (Format 2). |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [ccc.h](ccc_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
