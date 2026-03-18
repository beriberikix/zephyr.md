---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__i3c__ccc.html
original_path: doxygen/html/group__i3c__ccc.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

I3C Common Command Codes

[Device Driver APIs](group__io__interfaces.md) » [I3C Interface](group__i3c__interface.md)

I3C Common Command Codes.
[More...](#details)

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
| struct | [i3c\_ccc\_getcaps](structi3c__ccc__getcaps.md) |
|  | Payload for GETCAPS CCC (Get Optional Feature Capabilities). [More...](structi3c__ccc__getcaps.md#details) |

| Macros | |
| --- | --- |
| #define | [I3C\_CCC\_BROADCAST\_MAX\_ID](#gaf7b1cbdc790aa1d2c307e1f4ba773ba2)   0x7FU |
|  | Maximum CCC ID for broadcast. |
| #define | [I3C\_CCC\_ENEC](#ga06fc2296ada6198ab7a00646804ad5ed)(broadcast) |
|  | Enable Events Command. |
| #define | [I3C\_CCC\_DISEC](#ga8798591746e72a8ae1f901e97d45b810)(broadcast) |
|  | Disable Events Command. |
| #define | [I3C\_CCC\_ENTAS](#ga213102b3a8dbd490b02c3c89843c8d2a)([as](asm-macro-32-bit-gnu_8h.md#ac93d5f4341d561a6bd9864e880cffcf4), broadcast) |
|  | Enter Activity State. |
| #define | [I3C\_CCC\_ENTAS0](#ga364ce54e30957f7871e56cd82c1f825c)(broadcast) |
|  | Enter Activity State 0. |
| #define | [I3C\_CCC\_ENTAS1](#ga21c57ce34fe60255c9c8b28dac0a7a85)(broadcast) |
|  | Enter Activity State 1. |
| #define | [I3C\_CCC\_ENTAS2](#ga3adea01f66748ae2b153bf7eb9eab1eb)(broadcast) |
|  | Enter Activity State 2. |
| #define | [I3C\_CCC\_ENTAS3](#ga4dba9093fe562e3d09470610ab393f21)(broadcast) |
|  | Enter Activity State 3. |
| #define | [I3C\_CCC\_RSTDAA](#gaed94df1e670fc3670970f261865d6f63)   0x06U |
|  | Reset Dynamic Address Assignment (Broadcast). |
| #define | [I3C\_CCC\_ENTDAA](#gad6663cfa56be6bba2187a1d42d64be7b)   0x07U |
|  | Enter Dynamic Address Assignment (Broadcast). |
| #define | [I3C\_CCC\_DEFTGTS](#ga17e63ffe790f279a3e6eb8235c936604)   0x08U |
|  | Define List of Targets (Broadcast). |
| #define | [I3C\_CCC\_SETMWL](#gaab1ccf6cd47dfecee24811501e123802)(broadcast) |
|  | Set Max Write Length (Broadcast or Direct). |
| #define | [I3C\_CCC\_SETMRL](#ga97fd874b2e6c918f2e1262f7600bfd64)(broadcast) |
|  | Set Max Read Length (Broadcast or Direct). |
| #define | [I3C\_CCC\_ENTTM](#gace2b7fc835d31ade916aad3126eb0c6c)   0x0BU |
|  | Enter Test Mode (Broadcast). |
| #define | [I3C\_CCC\_SETBUSCON](#gac0f85a020956e3ee1ae8da899a9e06a6)   0x0CU |
|  | Set Bus Context (Broadcast). |
| #define | [I3C\_CCC\_ENDXFER](#ga4f331e7c21f15dd211a70c1a01c49738)(broadcast) |
|  | Data Transfer Ending Procedure Control. |
| #define | [I3C\_CCC\_ENTHDR](#gae213fc68bf723d8f7aee8c41cb9156c3)(x) |
|  | Enter HDR Mode (HDR-DDR) (Broadcast). |
| #define | [I3C\_CCC\_ENTHDR0](#gae88e44e9469891609ece0b8711162b9d)   0x20U |
|  | Enter HDR Mode 0 (HDR-DDR) (Broadcast). |
| #define | [I3C\_CCC\_ENTHDR1](#gae5319f3916df262579ecaac7497ed006)   0x21U |
|  | Enter HDR Mode 1 (HDR-TSP) (Broadcast). |
| #define | [I3C\_CCC\_ENTHDR2](#gaeff48ef5d76e4ea051f5aee1d1e4fc40)   0x22U |
|  | Enter HDR Mode 2 (HDR-TSL) (Broadcast). |
| #define | [I3C\_CCC\_ENTHDR3](#ga24eaa0af83a4a2223f4f84c3c67e05fe)   0x23U |
|  | Enter HDR Mode 3 (HDR-BT) (Broadcast). |
| #define | [I3C\_CCC\_ENTHDR4](#gaf15d188164c8fa9c0bf589eb7c5622d0)   0x24U |
|  | Enter HDR Mode 4 (Broadcast). |
| #define | [I3C\_CCC\_ENTHDR5](#gaafcad6bfacab1e42f22c8ee941ed6441)   0x25U |
|  | Enter HDR Mode 5 (Broadcast). |
| #define | [I3C\_CCC\_ENTHDR6](#gae55615887425917b202818bb0b7c5ac5)   0x26U |
|  | Enter HDR Mode 6 (Broadcast). |
| #define | [I3C\_CCC\_ENTHDR7](#ga9ab8c02bb5a80913024a43077fb97ffb)   0x27U |
|  | Enter HDR Mode 7 (Broadcast). |
| #define | [I3C\_CCC\_SETXTIME](#ga4203d5fdd9e9ca253803359934f22524)(broadcast) |
|  | Exchange Timing Information (Broadcast or Direct). |
| #define | [I3C\_CCC\_SETAASA](#gae995ef9e94beb26932b47136bdf89b57)   0x29U |
|  | Set All Addresses to Static Addresses (Broadcast). |
| #define | [I3C\_CCC\_RSTACT](#ga424cb224727d33c1ab18e4149bbea232)(broadcast) |
|  | Target Reset Action. |
| #define | [I3C\_CCC\_DEFGRPA](#ga89f8f72a7c7e8c9cb4fe8ece75ad78cf)   0x2BU |
|  | Define List of Group Address (Broadcast). |
| #define | [I3C\_CCC\_RSTGRPA](#ga46611eab0c82b74c615a7a7435f79d85)(broadcast) |
|  | Reset Group Address. |
| #define | [I3C\_CCC\_MLANE](#ga290cc5511d95b5be31c2c4cfea929085)(broadcast) |
|  | Multi-Lane Data Transfer Control (Broadcast). |
| #define | [I3C\_CCC\_VENDOR](#gaee5fb96b2d54df3b1b7aadefd54a608d)(broadcast, id) |
|  | Vendor/Standard Extension. |
| #define | [I3C\_CCC\_SETDASA](#ga134d5948b056144c83b133f93083a0f8)   0x87U |
|  | Set Dynamic Address from Static Address (Direct). |
| #define | [I3C\_CCC\_SETNEWDA](#gae0d6d0047f2c6e73e49e5019ec8d9ff0)   0x88U |
|  | Set New Dynamic Address (Direct). |
| #define | [I3C\_CCC\_GETMWL](#gae74935317b7ca471c09b767acf359e34)   0x8BU |
|  | Get Max Write Length (Direct). |
| #define | [I3C\_CCC\_GETMRL](#ga92e89b1ba719fbb8833c6e32fe4ef1dc)   0x8CU |
|  | Get Max Read Length (Direct). |
| #define | [I3C\_CCC\_GETPID](#ga04f7386d55742e935fa4dbfeb0120124)   0x8DU |
|  | Get Provisioned ID (Direct). |
| #define | [I3C\_CCC\_GETBCR](#ga1d7d49ab48098e4c2d5f63bd91d005e1)   0x8EU |
|  | Get Bus Characteristics Register (Direct). |
| #define | [I3C\_CCC\_GETDCR](#ga04ab6d4f0b2bf9d7f195132c0959225c)   0x8FU |
|  | Get Device Characteristics Register (Direct). |
| #define | [I3C\_CCC\_GETSTATUS](#ga858603dfc251b684b9d049b90119993d)   0x90U |
|  | Get Device Status (Direct). |
| #define | [I3C\_CCC\_GETACCCR](#gaa6807d3113c9c4d19b6fd27db32b3698)   0x91U |
|  | Get Accept Controller Role (Direct). |
| #define | [I3C\_CCC\_SETBRGTGT](#gab3cac5de39903cc2331a38ac66c4ff14)   0x93U |
|  | Set Bridge Targets (Direct). |
| #define | [I3C\_CCC\_GETMXDS](#ga2c078bf24e36689f34ad90979dd5c687)   0x94U |
|  | Get Max Data Speed (Direct). |
| #define | [I3C\_CCC\_GETCAPS](#gaa913844f97ee35405e9bf50c61a161a8)   0x95U |
|  | Get Optional Feature Capabilities (Direct). |
| #define | [I3C\_CCC\_SETROUTE](#ga5cf5cdb40299d4f8203b8035dacac17a)   0x96U |
|  | Set Route (Direct). |
| #define | [I3C\_CCC\_D2DXFER](#gaa2d86faed4f7c36939ce754be852751a)   0x97U |
|  | Device to Device(s) Tunneling Control (Direct). |
| #define | [I3C\_CCC\_GETXTIME](#ga66bb5e8027b103298f882f413f8ee6e8)   0x99U |
|  | Get Exchange Timing Information (Direct). |
| #define | [I3C\_CCC\_SETGRPA](#gaa0bef5d42c9bf2a21e888e5d5998d5cb)   0x9BU |
|  | Set Group Address (Direct). |
| #define | [I3C\_CCC\_ENEC\_EVT\_ENINTR](#gafe40d9b2ccedca40071c47929ff66e65)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Enable Events (ENEC) - Target Interrupt Requests. |
| #define | [I3C\_CCC\_ENEC\_EVT\_ENCR](#gad73e2e9f31f3a02f52b20d77e64671ff)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Enable Events (ENEC) - Controller Role Requests. |
| #define | [I3C\_CCC\_ENEC\_EVT\_ENHJ](#ga7e705ac95643d0462ac4275eed42153a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Enable Events (ENEC) - Hot-Join Event. |
| #define | [I3C\_CCC\_ENEC\_EVT\_ALL](#ga7860289b621c4243401e1df21cd84d66)   ([I3C\_CCC\_ENEC\_EVT\_ENINTR](#gafe40d9b2ccedca40071c47929ff66e65) | [I3C\_CCC\_ENEC\_EVT\_ENCR](#gad73e2e9f31f3a02f52b20d77e64671ff) | [I3C\_CCC\_ENEC\_EVT\_ENHJ](#ga7e705ac95643d0462ac4275eed42153a)) |
| #define | [I3C\_CCC\_DISEC\_EVT\_DISINTR](#gaf6da0458f1ae2d45ae7337cd4e576484)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Disable Events (DISEC) - Target Interrupt Requests. |
| #define | [I3C\_CCC\_DISEC\_EVT\_DISCR](#ga1f1612a16d2cb68b66f1ca85ba6f450a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Disable Events (DISEC) - Controller Role Requests. |
| #define | [I3C\_CCC\_DISEC\_EVT\_DISHJ](#gac3ffda84f683f99a0d4e0ad67adfd675)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Disable Events (DISEC) - Hot-Join Event. |
| #define | [I3C\_CCC\_DISEC\_EVT\_ALL](#gaf177b8fcb7412671a3b8c418336ddde4)   ([I3C\_CCC\_DISEC\_EVT\_DISINTR](#gaf6da0458f1ae2d45ae7337cd4e576484) | [I3C\_CCC\_DISEC\_EVT\_DISCR](#ga1f1612a16d2cb68b66f1ca85ba6f450a) | [I3C\_CCC\_DISEC\_EVT\_DISHJ](#gac3ffda84f683f99a0d4e0ad67adfd675)) |
| #define | [I3C\_CCC\_EVT\_INTR](#ga14cbf3628627f965336ac3740858aeea)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Events - Target Interrupt Requests. |
| #define | [I3C\_CCC\_EVT\_CR](#gad515a978c4912ef0c0444f14e51d8e8f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Events - Controller Role Requests. |
| #define | [I3C\_CCC\_EVT\_HJ](#gaedf65a98d59de51a533ff3d2f8cf075a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Events - Hot-Join Event. |
| #define | [I3C\_CCC\_EVT\_ALL](#ga8ff2055f745c4970bd41850bfd5b2aff)   ([I3C\_CCC\_EVT\_INTR](#ga14cbf3628627f965336ac3740858aeea) | [I3C\_CCC\_EVT\_CR](#gad515a978c4912ef0c0444f14e51d8e8f) | [I3C\_CCC\_EVT\_HJ](#gaedf65a98d59de51a533ff3d2f8cf075a)) |
|  | Bitmask for all events. |
| #define | [I3C\_CCC\_GETSTATUS\_PROTOCOL\_ERR](#gaee3dd61e9ac723a90868c610d0179b7d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | GETSTATUS Format 1 - Protocol Error bit. |
| #define | [I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_SHIFT](#ga8aca4592e579411a2c17f80ad682d93f)   6 |
|  | GETSTATUS Format 1 - Activity Mode bit shift value. |
| #define | [I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_MASK](#ga1006146ca810c06674fbee0ee1f66286)   (0x03U << [I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_SHIFT](#ga8aca4592e579411a2c17f80ad682d93f)) |
|  | GETSTATUS Format 1 - Activity Mode bitmask. |
| #define | [I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE](#ga660e179384e9426b498cd62da5665b15)(status) |
|  | GETSTATUS Format 1 - Activity Mode. |
| #define | [I3C\_CCC\_GETSTATUS\_NUM\_INT\_SHIFT](#ga1c07ae6c80088b8336f7f2d728487606)   0 |
|  | GETSTATUS Format 1 - Number of Pending Interrupts bit shift value. |
| #define | [I3C\_CCC\_GETSTATUS\_NUM\_INT\_MASK](#gae0bcc3ea13a34f63b073d63569d2e53a)   (0x0FU << [I3C\_CCC\_GETSTATUS\_NUM\_INT\_SHIFT](#ga1c07ae6c80088b8336f7f2d728487606)) |
|  | GETSTATUS Format 1 - Number of Pending Interrupts bitmask. |
| #define | [I3C\_CCC\_GETSTATUS\_NUM\_INT](#ga1436dc4b9f71c6f61fd3e3331857f3bd)(status) |
|  | GETSTATUS Format 1 - Number of Pending Interrupts. |
| #define | [I3C\_CCC\_GETSTATUS\_PRECR\_DEEP\_SLEEP\_DETECTED](#ga94afb0ebcfce55b85fc4a81953b4178a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | GETSTATUS Format 2 - PERCR - Deep Sleep Detected bit. |
| #define | [I3C\_CCC\_GETSTATUS\_PRECR\_HANDOFF\_DELAY\_NACK](#gadda1781cae312f4e588c3d3dcfa74f38)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | GETSTATUS Format 2 - PERCR - Handoff Delay NACK. |
| #define | [I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_MAX](#ga65ed8d5c2e6f562215674217f974d608)   0 |
|  | Get Max Data Speed (GETMXDS) - Default Max Sustained Data Rate. |
| #define | [I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_8MHZ](#gaac6dec9aee1e1d5a56c964a4d1fe32b1)   1 |
|  | Get Max Data Speed (GETMXDS) - 8MHz Max Sustained Data Rate. |
| #define | [I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_6MHZ](#gae1ff27ad2b8c9119e2efa88c0a696555)   2 |
|  | Get Max Data Speed (GETMXDS) - 6MHz Max Sustained Data Rate. |
| #define | [I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_4MHZ](#ga409666d6a17b53e518d702863826eb28)   3 |
|  | Get Max Data Speed (GETMXDS) - 4MHz Max Sustained Data Rate. |
| #define | [I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_2MHZ](#ga5a329b3fa12ecafd6958b05bab163a5c)   4 |
|  | Get Max Data Speed (GETMXDS) - 2MHz Max Sustained Data Rate. |
| #define | [I3C\_CCC\_GETMXDS\_TSCO\_8NS](#gad5e417bc3cabf8a915d1e7938415125a)   0 |
|  | Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 8ns. |
| #define | [I3C\_CCC\_GETMXDS\_TSCO\_9NS](#gaaee475f82f3a3759c7d62bb48082ebc2)   1 |
|  | Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 9ns. |
| #define | [I3C\_CCC\_GETMXDS\_TSCO\_10NS](#ga5e264e39aa2d4b602ec5e3218708e2f6)   2 |
|  | Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 10ns. |
| #define | [I3C\_CCC\_GETMXDS\_TSCO\_11NS](#ga2b27c9023f447da9c474c078091cf580)   3 |
|  | Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 11ns. |
| #define | [I3C\_CCC\_GETMXDS\_TSCO\_12NS](#ga06d33d1884a30d179aace82af956d62d)   4 |
|  | Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 12ns. |
| #define | [I3C\_CCC\_GETMXDS\_TSCO\_GT\_12NS](#ga5be034f241ccfb59534ae247d2e31d85)   7 |
|  | Get Max Data Speed (GETMXDS) - Clock to Data Turnaround > 12ns. |
| #define | [I3C\_CCC\_GETMXDS\_MAXWR\_DEFINING\_BYTE\_SUPPORT](#ga43fa03b6fea48cca06d07e962c5c04ef)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Get Max Data Speed (GETMXDS) - maxWr - Optional Defining Byte Support. |
| #define | [I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_SHIFT](#ga9bfab32baa69d2e437167afa31a6b428)   0 |
|  | Get Max Data Speed (GETMXDS) - Max Sustained Data Rate bit shift value. |
| #define | [I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_MASK](#ga5f4c6dde339c3467bdb3aea0d680d01f)   (0x07U << I3C\_CCC\_GET\_MXDS\_MAXWR\_MAX\_SDR\_FSCL\_SHIFT) |
|  | Get Max Data Speed (GETMXDS) - Max Sustained Data Rate bitmask. |
| #define | [I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL](#gae61b18d964e575809a1ebe2189aae028)(maxwr) |
|  | Get Max Data Speed (GETMXDS) - maxWr - Max Sustained Data Rate. |
| #define | [I3C\_CCC\_GETMXDS\_MAXRD\_W2R\_PERMITS\_STOP\_BETWEEN](#gaf5b95266cc911a37a3e46565b7601970)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Get Max Data Speed (GETMXDS) - maxRd - Write-to-Read Permits Stop Between. |
| #define | [I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_SHIFT](#gaf9c4764b0953c28af83b4fe06df0ebc3)   3 |
|  | Get Max Data Speed (GETMXDS) - maxRd - Clock to Data Turnaround bit shift value. |
| #define | [I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_MASK](#ga41958f7756cc5dec1c0546e7832b764a)   (0x07U << [I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_SHIFT](#gaf9c4764b0953c28af83b4fe06df0ebc3)) |
|  | Get Max Data Speed (GETMXDS) - maxRd - Clock to Data Turnaround bitmask. |
| #define | [I3C\_CCC\_GETMXDS\_MAXRD\_TSCO](#ga8284130d363dd1898de44c572b3d566c)(maxrd) |
|  | Get Max Data Speed (GETMXDS) - maxRd - Clock to Data Turnaround. |
| #define | [I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_SHIFT](#ga474f4d9ec309436863bdf0d7151de95f)   0 |
|  | Get Max Data Speed (GETMXDS) - maxRd - Max Sustained Data Rate bit shift value. |
| #define | [I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_MASK](#gad8b14f71cc1d5c1a0daa27703ab0c774)   (0x07U << I3C\_CCC\_GET\_MXDS\_MAXRD\_MAX\_SDR\_FSCL\_SHIFT) |
|  | Get Max Data Speed (GETMXDS) - maxRd - Max Sustained Data Rate bitmask. |
| #define | [I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL](#gaf5ac7364357e1e123adddcbfc134a0be)(maxrd) |
|  | Get Max Data Speed (GETMXDS) - maxRd - Max Sustained Data Rate. |
| #define | [I3C\_CCC\_GETMXDS\_CRDHLY1\_SET\_BUS\_ACT\_STATE](#ga9aa4eaf8a537323883d242e9ebb9a985)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Get Max Data Speed (GETMXDS) - CRDHLY1 - Set Bus Activity State bit shift value. |
| #define | [I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE\_SHIFT](#ga7853f150811ae69b09520628d774a033)   0 |
|  | Get Max Data Speed (GETMXDS) - CRDHLY1 - Controller Handoff Activity State bit shift value. |
| #define | [I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE\_MASK](#ga9ad046b7ec49bbca3f70a5a30fb1524b)   (0x03U << I3C\_CCC\_GETMXDS\_CRDHLY1\_SET\_BUS\_ACT\_STATE\_SHIFT) |
|  | Get Max Data Speed (GETMXDS) - CRDHLY1 - Controller Handoff Activity State bitmask. |
| #define | [I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE](#gab43a5adbcf158086d23c5d796a7e9399)(crhdly1) |
|  | Get Max Data Speed (GETMXDS) - CRDHLY1 - Controller Handoff Activity State. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_DDR](#gab984c6a18a555e4a3c0552684083e330)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR-DDR mode bit. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_BT](#gaac01f085ed1af56d686a33694744081c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR-BT mode bit. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_MODE](#gaae9483f4d5de3ba092b870b20e6b5f4a)(x) |
|  | Get Optional Feature Capabilities (GETCAPS) - HDR Mode. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_MODE0](#gad1389fc52c3fec4d6206bc56566bbf5d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR Mode 0. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_MODE1](#gacfd20baf528fcceca7f71719e15d5ea0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR Mode 1. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_MODE2](#ga9e5581743cbbe7363bb0919b95148d85)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR Mode 2. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_MODE3](#ga97b146596467f410ce9f063365ac9aaf)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR Mode 3. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_MODE4](#ga0dd98eeb74f493bfb04aeb698e656772)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR Mode 4. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_MODE5](#ga99bff02c40ccb15797dcf10c6dc00e87)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR Mode 5. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_MODE6](#ga12cead0a8ceb518a5c897f22b1d3dd64)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR Mode 6. |
| #define | [I3C\_CCC\_GETCAPS1\_HDR\_MODE7](#ga8b3373f18c0e3b365cc199c19ae82fb0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR Mode 7. |
| #define | [I3C\_CCC\_GETCAPS2\_HDRDDR\_WRITE\_ABORT](#ga1c2ceeaa44ee641c3d05176baf7e681d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 2 - HDR-DDR Write Abort bit. |
| #define | [I3C\_CCC\_GETCAPS2\_HDRDDR\_ABORT\_CRC](#ga8faf5ff5b2542a309f114ce4d6d11640)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 2 - HDR-DDR Abort CRC bit. |
| #define | [I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_SHIFT](#ga9ad0caec4913cd9454fa4c939555ad32)   4 |
|  | Get Optional Feature Capabilities (GETCAPS) Format 2 - Group Address Capabilities bit shift value. |
| #define | [I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_MASK](#ga64f58d1aaf847cf4a7811b20cca13b55)   (0x03U << [I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_SHIFT](#ga9ad0caec4913cd9454fa4c939555ad32)) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 2 - Group Address Capabilities bitmask. |
| #define | [I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP](#gabeb9acdabd6dce2117e9f5830673b2ed)(getcaps2) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 2 - Group Address Capabilities. |
| #define | [I3C\_CCC\_GETCAPS2\_SPEC\_VER\_SHIFT](#ga558dc49b9856d49ccd77bfac88fbfc7c)   0 |
|  | Get Optional Feature Capabilities (GETCAPS) Format 2 - I3C 1.x Specification Version bit shift value. |
| #define | [I3C\_CCC\_GETCAPS2\_SPEC\_VER\_MASK](#gae0015aa7768a8d5c18426a47cdbb67f8)   (0x0FU << [I3C\_CCC\_GETCAPS2\_SPEC\_VER\_SHIFT](#ga558dc49b9856d49ccd77bfac88fbfc7c)) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 2 - I3C 1.x Specification Version bitmask. |
| #define | [I3C\_CCC\_GETCAPS2\_SPEC\_VER](#ga093449c1cf029bddf1a25181cbfed570)(getcaps2) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 2 - I3C 1.x Specification Version. |
| #define | [I3C\_CCC\_GETCAPS3\_MLANE\_SUPPORT](#gaf0a2358f0f5f46c5fa1c084373f09be1)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 3 - Multi-Lane Data Transfer Support bit. |
| #define | [I3C\_CCC\_GETCAPS3\_D2DXFER\_SUPPORT](#ga08cc3c3976195642282e00ba00c1b283)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 3 - Device to Device Transfer (D2DXFER) Support bit. |
| #define | [I3C\_CCC\_GETCAPS3\_D2DXFER\_IBI\_CAPABLE](#ga73829cd436decbe55d2290dc750b3918)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 3 - Device to Device Transfer (D2DXFER) IBI Capable bit. |
| #define | [I3C\_CCC\_GETCAPS3\_GETCAPS\_DEFINING\_BYTE\_SUPPORT](#gaf40cc6cc08619363056e9650453a9a26)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 3 - Defining Byte Support in GETCAPS bit. |
| #define | [I3C\_CCC\_GETCAPS3\_GETSTATUS\_DEFINING\_BYTE\_SUPPORT](#gafbf1e9c947c40d70ae1c45991d093570)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 3 - Defining Byte Support in GETSTATUS bit. |
| #define | [I3C\_CCC\_GETCAPS3\_HDRBT\_CRC32\_SUPPORT](#ga3575eb8aa6fc3b49f2115104dcdfaeec)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 3 - HDR-BT CRC-32 Support bit. |
| #define | [I3C\_CCC\_GETCAPS3\_IBI\_MDR\_PENDING\_READ\_NOTIFICATION](#gac13d1465aa4222be0acccbf5303f3f3e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
|  | Get Optional Feature Capabilities (GETCAPS) Format 3 - IBI MDB Support for Pending Read Notification bit. |

| Enumerations | |
| --- | --- |
| enum | [i3c\_ccc\_getstatus\_fmt](#ga75934ea02ef8eb1c737da3ebfd368648) { [GETSTATUS\_FORMAT\_1](#gga75934ea02ef8eb1c737da3ebfd368648ae42215e3898baa40cc90e35c5777b57b) , [GETSTATUS\_FORMAT\_2](#gga75934ea02ef8eb1c737da3ebfd368648a08af2d5d884af32b46b7e0f2f429c68f) } |
|  | Indicate which format of GETSTATUS to use. [More...](#ga75934ea02ef8eb1c737da3ebfd368648) |
| enum | [i3c\_ccc\_getstatus\_defbyte](#ga1977f86d4865a97047119e5b3fbcb172) { [GETSTATUS\_FORMAT\_2\_TGTSTAT](#gga1977f86d4865a97047119e5b3fbcb172ac485e9d12c2a4855fd40ddcb6ab938eb) = 0x00U , [GETSTATUS\_FORMAT\_2\_PRECR](#gga1977f86d4865a97047119e5b3fbcb172a536a82ce39767e0cd3c25ebc56974877) = 0x91U , [GETSTATUS\_FORMAT\_2\_INVALID](#gga1977f86d4865a97047119e5b3fbcb172a83ccf53b5520866ec71e2c0824347e19) = 0x100U } |
|  | Defining byte values for GETSTATUS Format 2. [More...](#ga1977f86d4865a97047119e5b3fbcb172) |
| enum | [i3c\_ccc\_rstact\_defining\_byte](#ga61e1a1945a39b374edee5b75fbeb27d1) {     [I3C\_CCC\_RSTACT\_NO\_RESET](#gga61e1a1945a39b374edee5b75fbeb27d1aaba42ef747745ca61cf3aa91068fe7c2) = 0x00U , [I3C\_CCC\_RSTACT\_PERIPHERAL\_ONLY](#gga61e1a1945a39b374edee5b75fbeb27d1a5875b237e23a0a2ad01051ca1d612476) = 0x01U , [I3C\_CCC\_RSTACT\_RESET\_WHOLE\_TARGET](#gga61e1a1945a39b374edee5b75fbeb27d1af7b7e39dd7a9b214e13f1bdc7f869879) = 0x02U , [I3C\_CCC\_RSTACT\_DEBUG\_NETWORK\_ADAPTER](#gga61e1a1945a39b374edee5b75fbeb27d1a860a409d86fdb60d9d03df670a724519) = 0x03U ,     [I3C\_CCC\_RSTACT\_VIRTUAL\_TARGET\_DETECT](#gga61e1a1945a39b374edee5b75fbeb27d1ac56441fa6318702856ca6d2ae5ea328e) = 0x04U   } |
|  | Enum for I3C Reset Action (RSTACT) Defining Byte Values. [More...](#ga61e1a1945a39b374edee5b75fbeb27d1) |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [i3c\_ccc\_is\_payload\_broadcast](#gaaf692d0b89fd62a61d93f1577b25ce25) (const struct [i3c\_ccc\_payload](structi3c__ccc__payload.md) \*payload) |
|  | Test if I3C CCC payload is for broadcast. |
| int | [i3c\_ccc\_do\_getbcr](#ga7d5bb9c8fd88721b858180f503c1af4c) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, struct [i3c\_ccc\_getbcr](structi3c__ccc__getbcr.md) \*bcr) |
|  | Get BCR from a target. |
| int | [i3c\_ccc\_do\_getdcr](#ga7f886c0dbe0afec07f5678b574dc1101) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, struct [i3c\_ccc\_getdcr](structi3c__ccc__getdcr.md) \*dcr) |
|  | Get DCR from a target. |
| int | [i3c\_ccc\_do\_getpid](#ga949810a9a7c862d00ce4eec7e2c4d7df) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, struct [i3c\_ccc\_getpid](structi3c__ccc__getpid.md) \*pid) |
|  | Get PID from a target. |
| int | [i3c\_ccc\_do\_rstact\_all](#ga40294e43357f46338a6542f9a03d7ce7) (const struct [device](structdevice.md) \*controller, enum [i3c\_ccc\_rstact\_defining\_byte](#ga61e1a1945a39b374edee5b75fbeb27d1) action) |
|  | Broadcast RSTACT to reset I3C Peripheral. |
| int | [i3c\_ccc\_do\_rstdaa\_all](#gab1102467bb92a2aff7c9c1a66dd273a7) (const struct [device](structdevice.md) \*controller) |
|  | Broadcast RSTDAA to reset dynamic addresses for all targets. |
| int | [i3c\_ccc\_do\_setdasa](#gae4be97aae166be3b6e794fd77c8be6f8) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target) |
|  | Set Dynamic Address from Static Address for a target. |
| int | [i3c\_ccc\_do\_setnewda](#ga6d19dc9d3b421b4c936c6183977c4eec) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, struct [i3c\_ccc\_address](structi3c__ccc__address.md) new\_da) |
|  | Set New Dynamic Address for a target. |
| int | [i3c\_ccc\_do\_events\_all\_set](#gaf5fbaf2108053df855c95233181dc580) (const struct [device](structdevice.md) \*controller, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable, struct [i3c\_ccc\_events](structi3c__ccc__events.md) \*events) |
|  | Broadcast ENEC/DISEC to enable/disable target events. |
| int | [i3c\_ccc\_do\_events\_set](#gaf6575647b4b8f858f90bf2785a0f0d49) (struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable, struct [i3c\_ccc\_events](structi3c__ccc__events.md) \*events) |
|  | Direct CCC ENEC/DISEC to enable/disable target events. |
| int | [i3c\_ccc\_do\_setmwl\_all](#ga66c8c6318134d6287f4a14f6c31af02d) (const struct [device](structdevice.md) \*controller, const struct [i3c\_ccc\_mwl](structi3c__ccc__mwl.md) \*mwl) |
|  | Broadcast SETMWL to Set Maximum Write Length. |
| int | [i3c\_ccc\_do\_setmwl](#gab3de109c73dd58f6d2cf0a9229408f49) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, const struct [i3c\_ccc\_mwl](structi3c__ccc__mwl.md) \*mwl) |
|  | Single target SETMWL to Set Maximum Write Length. |
| int | [i3c\_ccc\_do\_getmwl](#gaf1077e3d6cf8a7e1f0e02e985058e507) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, struct [i3c\_ccc\_mwl](structi3c__ccc__mwl.md) \*mwl) |
|  | Single target GETMWL to Get Maximum Write Length. |
| int | [i3c\_ccc\_do\_setmrl\_all](#ga2542f4ebcc0c2bb31bc8e334955620b0) (const struct [device](structdevice.md) \*controller, const struct [i3c\_ccc\_mrl](structi3c__ccc__mrl.md) \*mrl, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) has\_ibi\_size) |
|  | Broadcast SETMRL to Set Maximum Read Length. |
| int | [i3c\_ccc\_do\_setmrl](#ga6e4f26d23919a619c89624b15d16390a) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, const struct [i3c\_ccc\_mrl](structi3c__ccc__mrl.md) \*mrl) |
|  | Single target SETMRL to Set Maximum Read Length. |
| int | [i3c\_ccc\_do\_getmrl](#gac4331a4c7dbb7af0eaea63b01bb08485) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, struct [i3c\_ccc\_mrl](structi3c__ccc__mrl.md) \*mrl) |
|  | Single target GETMRL to Get Maximum Read Length. |
| int | [i3c\_ccc\_do\_getstatus](#ga4fe9d056a5ac78ff83513763a71c7dfe) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, union [i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md) \*status, enum [i3c\_ccc\_getstatus\_fmt](#ga75934ea02ef8eb1c737da3ebfd368648) fmt, enum [i3c\_ccc\_getstatus\_defbyte](#ga1977f86d4865a97047119e5b3fbcb172) defbyte) |
|  | Single target GETSTATUS to Get Target Status. |
| static int | [i3c\_ccc\_do\_getstatus\_fmt1](#ga1cb2804fc7dcbb322cd26001d7953c95) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, union [i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md) \*status) |
|  | Single target GETSTATUS to Get Target Status (Format 1). |
| static int | [i3c\_ccc\_do\_getstatus\_fmt2](#ga4eaaaf7b7e9f2f8dd657d4f6a0de8bfb) (const struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, union [i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md) \*status, enum [i3c\_ccc\_getstatus\_defbyte](#ga1977f86d4865a97047119e5b3fbcb172) defbyte) |
|  | Single target GETSTATUS to Get Target Status (Format 2). |

## Detailed Description

I3C Common Command Codes.

## Macro Definition Documentation

## [◆ ](#gaf7b1cbdc790aa1d2c307e1f4ba773ba2)I3C\_CCC\_BROADCAST\_MAX\_ID

| #define I3C\_CCC\_BROADCAST\_MAX\_ID   0x7FU |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Maximum CCC ID for broadcast.

## [◆ ](#gaa2d86faed4f7c36939ce754be852751a)I3C\_CCC\_D2DXFER

| #define I3C\_CCC\_D2DXFER   0x97U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Device to Device(s) Tunneling Control (Direct).

## [◆ ](#ga89f8f72a7c7e8c9cb4fe8ece75ad78cf)I3C\_CCC\_DEFGRPA

| #define I3C\_CCC\_DEFGRPA   0x2BU |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Define List of Group Address (Broadcast).

## [◆ ](#ga17e63ffe790f279a3e6eb8235c936604)I3C\_CCC\_DEFTGTS

| #define I3C\_CCC\_DEFTGTS   0x08U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Define List of Targets (Broadcast).

## [◆ ](#ga8798591746e72a8ae1f901e97d45b810)I3C\_CCC\_DISEC

| #define I3C\_CCC\_DISEC | ( |  | *broadcast* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

((broadcast) ? 0x01U : 0x81U)

Disable Events Command.

Parameters
:   | broadcast | True if broadcast, false if direct. |
    | --- | --- |

## [◆ ](#gaf177b8fcb7412671a3b8c418336ddde4)I3C\_CCC\_DISEC\_EVT\_ALL

| #define I3C\_CCC\_DISEC\_EVT\_ALL   ([I3C\_CCC\_DISEC\_EVT\_DISINTR](#gaf6da0458f1ae2d45ae7337cd4e576484) | [I3C\_CCC\_DISEC\_EVT\_DISCR](#ga1f1612a16d2cb68b66f1ca85ba6f450a) | [I3C\_CCC\_DISEC\_EVT\_DISHJ](#gac3ffda84f683f99a0d4e0ad67adfd675)) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

## [◆ ](#ga1f1612a16d2cb68b66f1ca85ba6f450a)I3C\_CCC\_DISEC\_EVT\_DISCR

| #define I3C\_CCC\_DISEC\_EVT\_DISCR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Disable Events (DISEC) - Controller Role Requests.

## [◆ ](#gac3ffda84f683f99a0d4e0ad67adfd675)I3C\_CCC\_DISEC\_EVT\_DISHJ

| #define I3C\_CCC\_DISEC\_EVT\_DISHJ   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Disable Events (DISEC) - Hot-Join Event.

## [◆ ](#gaf6da0458f1ae2d45ae7337cd4e576484)I3C\_CCC\_DISEC\_EVT\_DISINTR

| #define I3C\_CCC\_DISEC\_EVT\_DISINTR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Disable Events (DISEC) - Target Interrupt Requests.

## [◆ ](#ga4f331e7c21f15dd211a70c1a01c49738)I3C\_CCC\_ENDXFER

| #define I3C\_CCC\_ENDXFER | ( |  | *broadcast* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

((broadcast) ? 0x12U : 0x92U)

Data Transfer Ending Procedure Control.

Parameters
:   | broadcast | True if broadcast, false if direct. |
    | --- | --- |

## [◆ ](#ga06fc2296ada6198ab7a00646804ad5ed)I3C\_CCC\_ENEC

| #define I3C\_CCC\_ENEC | ( |  | *broadcast* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

((broadcast) ? 0x00U : 0x80U)

Enable Events Command.

Parameters
:   | broadcast | True if broadcast, false if direct. |
    | --- | --- |

## [◆ ](#ga7860289b621c4243401e1df21cd84d66)I3C\_CCC\_ENEC\_EVT\_ALL

| #define I3C\_CCC\_ENEC\_EVT\_ALL   ([I3C\_CCC\_ENEC\_EVT\_ENINTR](#gafe40d9b2ccedca40071c47929ff66e65) | [I3C\_CCC\_ENEC\_EVT\_ENCR](#gad73e2e9f31f3a02f52b20d77e64671ff) | [I3C\_CCC\_ENEC\_EVT\_ENHJ](#ga7e705ac95643d0462ac4275eed42153a)) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

## [◆ ](#gad73e2e9f31f3a02f52b20d77e64671ff)I3C\_CCC\_ENEC\_EVT\_ENCR

| #define I3C\_CCC\_ENEC\_EVT\_ENCR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Enable Events (ENEC) - Controller Role Requests.

## [◆ ](#ga7e705ac95643d0462ac4275eed42153a)I3C\_CCC\_ENEC\_EVT\_ENHJ

| #define I3C\_CCC\_ENEC\_EVT\_ENHJ   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Enable Events (ENEC) - Hot-Join Event.

## [◆ ](#gafe40d9b2ccedca40071c47929ff66e65)I3C\_CCC\_ENEC\_EVT\_ENINTR

| #define I3C\_CCC\_ENEC\_EVT\_ENINTR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Enable Events (ENEC) - Target Interrupt Requests.

## [◆ ](#ga213102b3a8dbd490b02c3c89843c8d2a)I3C\_CCC\_ENTAS

| #define I3C\_CCC\_ENTAS | ( |  | *[as](asm-macro-32-bit-gnu_8h.md#ac93d5f4341d561a6bd9864e880cffcf4)*, |
| --- | --- | --- | --- |
|  |  |  | *broadcast* ) |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

(((broadcast) ? 0x02U : 0x82U) + ([as](asm-macro-32-bit-gnu_8h.md#ac93d5f4341d561a6bd9864e880cffcf4)))

[as](asm-macro-32-bit-gnu_8h.md#ac93d5f4341d561a6bd9864e880cffcf4)

irp nz macro MOVR cc s mov cc s endm endr irp as

**Definition** asm-macro-32-bit-gnu.h:16

Enter Activity State.

Parameters
:   | [as](asm-macro-32-bit-gnu_8h.md#ac93d5f4341d561a6bd9864e880cffcf4) | Desired activity state |
    | --- | --- |
    | broadcast | True if broadcast, false if direct. |

## [◆ ](#ga364ce54e30957f7871e56cd82c1f825c)I3C\_CCC\_ENTAS0

| #define I3C\_CCC\_ENTAS0 | ( |  | *broadcast* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

[I3C\_CCC\_ENTAS](#ga213102b3a8dbd490b02c3c89843c8d2a)(0, broadcast)

[I3C\_CCC\_ENTAS](#ga213102b3a8dbd490b02c3c89843c8d2a)

#define I3C\_CCC\_ENTAS(as, broadcast)

Enter Activity State.

**Definition** ccc.h:50

Enter Activity State 0.

Parameters
:   | broadcast | True if broadcast, false if direct. |
    | --- | --- |

## [◆ ](#ga21c57ce34fe60255c9c8b28dac0a7a85)I3C\_CCC\_ENTAS1

| #define I3C\_CCC\_ENTAS1 | ( |  | *broadcast* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

[I3C\_CCC\_ENTAS](#ga213102b3a8dbd490b02c3c89843c8d2a)(1, broadcast)

Enter Activity State 1.

Parameters
:   | broadcast | True if broadcast, false if direct. |
    | --- | --- |

## [◆ ](#ga3adea01f66748ae2b153bf7eb9eab1eb)I3C\_CCC\_ENTAS2

| #define I3C\_CCC\_ENTAS2 | ( |  | *broadcast* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

[I3C\_CCC\_ENTAS](#ga213102b3a8dbd490b02c3c89843c8d2a)(2, broadcast)

Enter Activity State 2.

Parameters
:   | broadcast | True if broadcast, false if direct. |
    | --- | --- |

## [◆ ](#ga4dba9093fe562e3d09470610ab393f21)I3C\_CCC\_ENTAS3

| #define I3C\_CCC\_ENTAS3 | ( |  | *broadcast* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

[I3C\_CCC\_ENTAS](#ga213102b3a8dbd490b02c3c89843c8d2a)(3, broadcast)

Enter Activity State 3.

Parameters
:   | broadcast | True if broadcast, false if direct. |
    | --- | --- |

## [◆ ](#gad6663cfa56be6bba2187a1d42d64be7b)I3C\_CCC\_ENTDAA

| #define I3C\_CCC\_ENTDAA   0x07U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Enter Dynamic Address Assignment (Broadcast).

## [◆ ](#gae213fc68bf723d8f7aee8c41cb9156c3)I3C\_CCC\_ENTHDR

| #define I3C\_CCC\_ENTHDR | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

(0x20U + (x))

Enter HDR Mode (HDR-DDR) (Broadcast).

## [◆ ](#gae88e44e9469891609ece0b8711162b9d)I3C\_CCC\_ENTHDR0

| #define I3C\_CCC\_ENTHDR0   0x20U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Enter HDR Mode 0 (HDR-DDR) (Broadcast).

## [◆ ](#gae5319f3916df262579ecaac7497ed006)I3C\_CCC\_ENTHDR1

| #define I3C\_CCC\_ENTHDR1   0x21U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Enter HDR Mode 1 (HDR-TSP) (Broadcast).

## [◆ ](#gaeff48ef5d76e4ea051f5aee1d1e4fc40)I3C\_CCC\_ENTHDR2

| #define I3C\_CCC\_ENTHDR2   0x22U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Enter HDR Mode 2 (HDR-TSL) (Broadcast).

## [◆ ](#ga24eaa0af83a4a2223f4f84c3c67e05fe)I3C\_CCC\_ENTHDR3

| #define I3C\_CCC\_ENTHDR3   0x23U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Enter HDR Mode 3 (HDR-BT) (Broadcast).

## [◆ ](#gaf15d188164c8fa9c0bf589eb7c5622d0)I3C\_CCC\_ENTHDR4

| #define I3C\_CCC\_ENTHDR4   0x24U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Enter HDR Mode 4 (Broadcast).

## [◆ ](#gaafcad6bfacab1e42f22c8ee941ed6441)I3C\_CCC\_ENTHDR5

| #define I3C\_CCC\_ENTHDR5   0x25U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Enter HDR Mode 5 (Broadcast).

## [◆ ](#gae55615887425917b202818bb0b7c5ac5)I3C\_CCC\_ENTHDR6

| #define I3C\_CCC\_ENTHDR6   0x26U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Enter HDR Mode 6 (Broadcast).

## [◆ ](#ga9ab8c02bb5a80913024a43077fb97ffb)I3C\_CCC\_ENTHDR7

| #define I3C\_CCC\_ENTHDR7   0x27U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Enter HDR Mode 7 (Broadcast).

## [◆ ](#gace2b7fc835d31ade916aad3126eb0c6c)I3C\_CCC\_ENTTM

| #define I3C\_CCC\_ENTTM   0x0BU |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Enter Test Mode (Broadcast).

## [◆ ](#ga8ff2055f745c4970bd41850bfd5b2aff)I3C\_CCC\_EVT\_ALL

| #define I3C\_CCC\_EVT\_ALL   ([I3C\_CCC\_EVT\_INTR](#ga14cbf3628627f965336ac3740858aeea) | [I3C\_CCC\_EVT\_CR](#gad515a978c4912ef0c0444f14e51d8e8f) | [I3C\_CCC\_EVT\_HJ](#gaedf65a98d59de51a533ff3d2f8cf075a)) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Bitmask for all events.

## [◆ ](#gad515a978c4912ef0c0444f14e51d8e8f)I3C\_CCC\_EVT\_CR

| #define I3C\_CCC\_EVT\_CR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Events - Controller Role Requests.

## [◆ ](#gaedf65a98d59de51a533ff3d2f8cf075a)I3C\_CCC\_EVT\_HJ

| #define I3C\_CCC\_EVT\_HJ   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Events - Hot-Join Event.

## [◆ ](#ga14cbf3628627f965336ac3740858aeea)I3C\_CCC\_EVT\_INTR

| #define I3C\_CCC\_EVT\_INTR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Events - Target Interrupt Requests.

## [◆ ](#gaa6807d3113c9c4d19b6fd27db32b3698)I3C\_CCC\_GETACCCR

| #define I3C\_CCC\_GETACCCR   0x91U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Accept Controller Role (Direct).

## [◆ ](#ga1d7d49ab48098e4c2d5f63bd91d005e1)I3C\_CCC\_GETBCR

| #define I3C\_CCC\_GETBCR   0x8EU |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Bus Characteristics Register (Direct).

## [◆ ](#gaa913844f97ee35405e9bf50c61a161a8)I3C\_CCC\_GETCAPS

| #define I3C\_CCC\_GETCAPS   0x95U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (Direct).

## [◆ ](#gaac01f085ed1af56d686a33694744081c)I3C\_CCC\_GETCAPS1\_HDR\_BT

| #define I3C\_CCC\_GETCAPS1\_HDR\_BT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR-BT mode bit.

## [◆ ](#gab984c6a18a555e4a3c0552684083e330)I3C\_CCC\_GETCAPS1\_HDR\_DDR

| #define I3C\_CCC\_GETCAPS1\_HDR\_DDR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR-DDR mode bit.

## [◆ ](#gaae9483f4d5de3ba092b870b20e6b5f4a)I3C\_CCC\_GETCAPS1\_HDR\_MODE

| #define I3C\_CCC\_GETCAPS1\_HDR\_MODE | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(x)

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

Get Optional Feature Capabilities (GETCAPS) - HDR Mode.

Get the bit corresponding to HDR mode.

Parameters
:   | x | HDR mode |
    | --- | --- |

## [◆ ](#gad1389fc52c3fec4d6206bc56566bbf5d)I3C\_CCC\_GETCAPS1\_HDR\_MODE0

| #define I3C\_CCC\_GETCAPS1\_HDR\_MODE0   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR Mode 0.

## [◆ ](#gacfd20baf528fcceca7f71719e15d5ea0)I3C\_CCC\_GETCAPS1\_HDR\_MODE1

| #define I3C\_CCC\_GETCAPS1\_HDR\_MODE1   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR Mode 1.

## [◆ ](#ga9e5581743cbbe7363bb0919b95148d85)I3C\_CCC\_GETCAPS1\_HDR\_MODE2

| #define I3C\_CCC\_GETCAPS1\_HDR\_MODE2   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR Mode 2.

## [◆ ](#ga97b146596467f410ce9f063365ac9aaf)I3C\_CCC\_GETCAPS1\_HDR\_MODE3

| #define I3C\_CCC\_GETCAPS1\_HDR\_MODE3   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR Mode 3.

## [◆ ](#ga0dd98eeb74f493bfb04aeb698e656772)I3C\_CCC\_GETCAPS1\_HDR\_MODE4

| #define I3C\_CCC\_GETCAPS1\_HDR\_MODE4   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR Mode 4.

## [◆ ](#ga99bff02c40ccb15797dcf10c6dc00e87)I3C\_CCC\_GETCAPS1\_HDR\_MODE5

| #define I3C\_CCC\_GETCAPS1\_HDR\_MODE5   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR Mode 5.

## [◆ ](#ga12cead0a8ceb518a5c897f22b1d3dd64)I3C\_CCC\_GETCAPS1\_HDR\_MODE6

| #define I3C\_CCC\_GETCAPS1\_HDR\_MODE6   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR Mode 6.

## [◆ ](#ga8b3373f18c0e3b365cc199c19ae82fb0)I3C\_CCC\_GETCAPS1\_HDR\_MODE7

| #define I3C\_CCC\_GETCAPS1\_HDR\_MODE7   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 1 - HDR Mode 7.

## [◆ ](#gabeb9acdabd6dce2117e9f5830673b2ed)I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP

| #define I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP | ( |  | *getcaps2* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

(((getcaps2) & \

[I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_MASK](#ga64f58d1aaf847cf4a7811b20cca13b55)) \

>> I3C\_CCC\_GETCAPS\_GRPADDR\_CAP\_SHIFT)

[I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_MASK](#ga64f58d1aaf847cf4a7811b20cca13b55)

#define I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_MASK

Get Optional Feature Capabilities (GETCAPS) Format 2 - Group Address Capabilities bitmask.

**Definition** ccc.h:911

Get Optional Feature Capabilities (GETCAPS) Format 2 - Group Address Capabilities.

Obtain Group Address Capabilities value from GETCAPS Format 2 value obtained via GETCAPS.

Parameters
:   | getcaps2 | GETCAPS2 value. |
    | --- | --- |

## [◆ ](#ga64f58d1aaf847cf4a7811b20cca13b55)I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_MASK

| #define I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_MASK   (0x03U << [I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_SHIFT](#ga9ad0caec4913cd9454fa4c939555ad32)) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 2 - Group Address Capabilities bitmask.

## [◆ ](#ga9ad0caec4913cd9454fa4c939555ad32)I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_SHIFT

| #define I3C\_CCC\_GETCAPS2\_GRPADDR\_CAP\_SHIFT   4 |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 2 - Group Address Capabilities bit shift value.

## [◆ ](#ga8faf5ff5b2542a309f114ce4d6d11640)I3C\_CCC\_GETCAPS2\_HDRDDR\_ABORT\_CRC

| #define I3C\_CCC\_GETCAPS2\_HDRDDR\_ABORT\_CRC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 2 - HDR-DDR Abort CRC bit.

## [◆ ](#ga1c2ceeaa44ee641c3d05176baf7e681d)I3C\_CCC\_GETCAPS2\_HDRDDR\_WRITE\_ABORT

| #define I3C\_CCC\_GETCAPS2\_HDRDDR\_WRITE\_ABORT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 2 - HDR-DDR Write Abort bit.

## [◆ ](#ga093449c1cf029bddf1a25181cbfed570)I3C\_CCC\_GETCAPS2\_SPEC\_VER

| #define I3C\_CCC\_GETCAPS2\_SPEC\_VER | ( |  | *getcaps2* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

(((getcaps2) & \

[I3C\_CCC\_GETCAPS2\_SPEC\_VER\_MASK](#gae0015aa7768a8d5c18426a47cdbb67f8)) \

>> I3C\_CCC\_GETCAPS\_SPEC\_VER\_SHIFT)

[I3C\_CCC\_GETCAPS2\_SPEC\_VER\_MASK](#gae0015aa7768a8d5c18426a47cdbb67f8)

#define I3C\_CCC\_GETCAPS2\_SPEC\_VER\_MASK

Get Optional Feature Capabilities (GETCAPS) Format 2 - I3C 1.x Specification Version bitmask.

**Definition** ccc.h:937

Get Optional Feature Capabilities (GETCAPS) Format 2 - I3C 1.x Specification Version.

Obtain I3C 1.x Specification Version value from GETCAPS Format 2 value obtained via GETCAPS.

Parameters
:   | getcaps2 | GETCAPS2 value. |
    | --- | --- |

## [◆ ](#gae0015aa7768a8d5c18426a47cdbb67f8)I3C\_CCC\_GETCAPS2\_SPEC\_VER\_MASK

| #define I3C\_CCC\_GETCAPS2\_SPEC\_VER\_MASK   (0x0FU << [I3C\_CCC\_GETCAPS2\_SPEC\_VER\_SHIFT](#ga558dc49b9856d49ccd77bfac88fbfc7c)) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 2 - I3C 1.x Specification Version bitmask.

## [◆ ](#ga558dc49b9856d49ccd77bfac88fbfc7c)I3C\_CCC\_GETCAPS2\_SPEC\_VER\_SHIFT

| #define I3C\_CCC\_GETCAPS2\_SPEC\_VER\_SHIFT   0 |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 2 - I3C 1.x Specification Version bit shift value.

## [◆ ](#ga73829cd436decbe55d2290dc750b3918)I3C\_CCC\_GETCAPS3\_D2DXFER\_IBI\_CAPABLE

| #define I3C\_CCC\_GETCAPS3\_D2DXFER\_IBI\_CAPABLE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 3 - Device to Device Transfer (D2DXFER) IBI Capable bit.

## [◆ ](#ga08cc3c3976195642282e00ba00c1b283)I3C\_CCC\_GETCAPS3\_D2DXFER\_SUPPORT

| #define I3C\_CCC\_GETCAPS3\_D2DXFER\_SUPPORT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 3 - Device to Device Transfer (D2DXFER) Support bit.

## [◆ ](#gaf40cc6cc08619363056e9650453a9a26)I3C\_CCC\_GETCAPS3\_GETCAPS\_DEFINING\_BYTE\_SUPPORT

| #define I3C\_CCC\_GETCAPS3\_GETCAPS\_DEFINING\_BYTE\_SUPPORT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 3 - Defining Byte Support in GETCAPS bit.

## [◆ ](#gafbf1e9c947c40d70ae1c45991d093570)I3C\_CCC\_GETCAPS3\_GETSTATUS\_DEFINING\_BYTE\_SUPPORT

| #define I3C\_CCC\_GETCAPS3\_GETSTATUS\_DEFINING\_BYTE\_SUPPORT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 3 - Defining Byte Support in GETSTATUS bit.

## [◆ ](#ga3575eb8aa6fc3b49f2115104dcdfaeec)I3C\_CCC\_GETCAPS3\_HDRBT\_CRC32\_SUPPORT

| #define I3C\_CCC\_GETCAPS3\_HDRBT\_CRC32\_SUPPORT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 3 - HDR-BT CRC-32 Support bit.

## [◆ ](#gac13d1465aa4222be0acccbf5303f3f3e)I3C\_CCC\_GETCAPS3\_IBI\_MDR\_PENDING\_READ\_NOTIFICATION

| #define I3C\_CCC\_GETCAPS3\_IBI\_MDR\_PENDING\_READ\_NOTIFICATION   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 3 - IBI MDB Support for Pending Read Notification bit.

## [◆ ](#gaf0a2358f0f5f46c5fa1c084373f09be1)I3C\_CCC\_GETCAPS3\_MLANE\_SUPPORT

| #define I3C\_CCC\_GETCAPS3\_MLANE\_SUPPORT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Optional Feature Capabilities (GETCAPS) Format 3 - Multi-Lane Data Transfer Support bit.

## [◆ ](#ga04ab6d4f0b2bf9d7f195132c0959225c)I3C\_CCC\_GETDCR

| #define I3C\_CCC\_GETDCR   0x8FU |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Device Characteristics Register (Direct).

## [◆ ](#ga92e89b1ba719fbb8833c6e32fe4ef1dc)I3C\_CCC\_GETMRL

| #define I3C\_CCC\_GETMRL   0x8CU |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Read Length (Direct).

## [◆ ](#gae74935317b7ca471c09b767acf359e34)I3C\_CCC\_GETMWL

| #define I3C\_CCC\_GETMWL   0x8BU |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Write Length (Direct).

## [◆ ](#ga2c078bf24e36689f34ad90979dd5c687)I3C\_CCC\_GETMXDS

| #define I3C\_CCC\_GETMXDS   0x94U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (Direct).

## [◆ ](#gab43a5adbcf158086d23c5d796a7e9399)I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE

| #define I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE | ( |  | *crhdly1* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

(((crhdly1) & \

I3C\_CCC\_GETMXDS\_CRDHLY1\_SET\_BUS\_ACT\_STATE\_MASK) \

>> I3C\_CCC\_GETMXDS\_CRDHLY1\_SET\_BUS\_ACT\_STATE\_SHIFT)

Get Max Data Speed (GETMXDS) - CRDHLY1 - Controller Handoff Activity State.

Obtain Controller Handoff Activity State value from GETMXDS value obtained via GETMXDS.

Parameters
:   | crhdly1 | GETMXDS value. |
    | --- | --- |

## [◆ ](#ga9ad046b7ec49bbca3f70a5a30fb1524b)I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE\_MASK

| #define I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE\_MASK   (0x03U << I3C\_CCC\_GETMXDS\_CRDHLY1\_SET\_BUS\_ACT\_STATE\_SHIFT) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - CRDHLY1 - Controller Handoff Activity State bitmask.

## [◆ ](#ga7853f150811ae69b09520628d774a033)I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE\_SHIFT

| #define I3C\_CCC\_GETMXDS\_CRDHLY1\_CTRL\_HANDOFF\_ACT\_STATE\_SHIFT   0 |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - CRDHLY1 - Controller Handoff Activity State bit shift value.

## [◆ ](#ga9aa4eaf8a537323883d242e9ebb9a985)I3C\_CCC\_GETMXDS\_CRDHLY1\_SET\_BUS\_ACT\_STATE

| #define I3C\_CCC\_GETMXDS\_CRDHLY1\_SET\_BUS\_ACT\_STATE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - CRDHLY1 - Set Bus Activity State bit shift value.

## [◆ ](#ga5a329b3fa12ecafd6958b05bab163a5c)I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_2MHZ

| #define I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_2MHZ   4 |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - 2MHz Max Sustained Data Rate.

## [◆ ](#ga409666d6a17b53e518d702863826eb28)I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_4MHZ

| #define I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_4MHZ   3 |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - 4MHz Max Sustained Data Rate.

## [◆ ](#gae1ff27ad2b8c9119e2efa88c0a696555)I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_6MHZ

| #define I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_6MHZ   2 |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - 6MHz Max Sustained Data Rate.

## [◆ ](#gaac6dec9aee1e1d5a56c964a4d1fe32b1)I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_8MHZ

| #define I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_8MHZ   1 |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - 8MHz Max Sustained Data Rate.

## [◆ ](#ga65ed8d5c2e6f562215674217f974d608)I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_MAX

| #define I3C\_CCC\_GETMXDS\_MAX\_SDR\_FSCL\_MAX   0 |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - Default Max Sustained Data Rate.

## [◆ ](#gaf5ac7364357e1e123adddcbfc134a0be)I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL

| #define I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL | ( |  | *maxrd* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

(((maxrd) & \

[I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_MASK](#gad8b14f71cc1d5c1a0daa27703ab0c774)) \

>> [I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_SHIFT](#ga474f4d9ec309436863bdf0d7151de95f))

[I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_SHIFT](#ga474f4d9ec309436863bdf0d7151de95f)

#define I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_SHIFT

Get Max Data Speed (GETMXDS) - maxRd - Max Sustained Data Rate bit shift value.

**Definition** ccc.h:802

[I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_MASK](#gad8b14f71cc1d5c1a0daa27703ab0c774)

#define I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_MASK

Get Max Data Speed (GETMXDS) - maxRd - Max Sustained Data Rate bitmask.

**Definition** ccc.h:805

Get Max Data Speed (GETMXDS) - maxRd - Max Sustained Data Rate.

Obtain Max Sustained Data Rate value from GETMXDS maxRd value obtained via GETMXDS.

Parameters
:   | maxrd | GETMXDS maxRd value. |
    | --- | --- |

## [◆ ](#gad8b14f71cc1d5c1a0daa27703ab0c774)I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_MASK

| #define I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_MASK   (0x07U << I3C\_CCC\_GET\_MXDS\_MAXRD\_MAX\_SDR\_FSCL\_SHIFT) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - maxRd - Max Sustained Data Rate bitmask.

## [◆ ](#ga474f4d9ec309436863bdf0d7151de95f)I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_SHIFT

| #define I3C\_CCC\_GETMXDS\_MAXRD\_MAX\_SDR\_FSCL\_SHIFT   0 |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - maxRd - Max Sustained Data Rate bit shift value.

## [◆ ](#ga8284130d363dd1898de44c572b3d566c)I3C\_CCC\_GETMXDS\_MAXRD\_TSCO

| #define I3C\_CCC\_GETMXDS\_MAXRD\_TSCO | ( |  | *maxrd* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

(((maxrd) & [I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_MASK](#ga41958f7756cc5dec1c0546e7832b764a)) \

>> [I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_SHIFT](#gaf9c4764b0953c28af83b4fe06df0ebc3))

[I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_MASK](#ga41958f7756cc5dec1c0546e7832b764a)

#define I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_MASK

Get Max Data Speed (GETMXDS) - maxRd - Clock to Data Turnaround bitmask.

**Definition** ccc.h:786

[I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_SHIFT](#gaf9c4764b0953c28af83b4fe06df0ebc3)

#define I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_SHIFT

Get Max Data Speed (GETMXDS) - maxRd - Clock to Data Turnaround bit shift value.

**Definition** ccc.h:783

Get Max Data Speed (GETMXDS) - maxRd - Clock to Data Turnaround.

Obtain Clock to Data Turnaround value from GETMXDS maxRd value obtained via GETMXDS.

Parameters
:   | maxrd | GETMXDS maxRd value. |
    | --- | --- |

## [◆ ](#ga41958f7756cc5dec1c0546e7832b764a)I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_MASK

| #define I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_MASK   (0x07U << [I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_SHIFT](#gaf9c4764b0953c28af83b4fe06df0ebc3)) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - maxRd - Clock to Data Turnaround bitmask.

## [◆ ](#gaf9c4764b0953c28af83b4fe06df0ebc3)I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_SHIFT

| #define I3C\_CCC\_GETMXDS\_MAXRD\_TSCO\_SHIFT   3 |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - maxRd - Clock to Data Turnaround bit shift value.

## [◆ ](#gaf5b95266cc911a37a3e46565b7601970)I3C\_CCC\_GETMXDS\_MAXRD\_W2R\_PERMITS\_STOP\_BETWEEN

| #define I3C\_CCC\_GETMXDS\_MAXRD\_W2R\_PERMITS\_STOP\_BETWEEN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - maxRd - Write-to-Read Permits Stop Between.

## [◆ ](#ga43fa03b6fea48cca06d07e962c5c04ef)I3C\_CCC\_GETMXDS\_MAXWR\_DEFINING\_BYTE\_SUPPORT

| #define I3C\_CCC\_GETMXDS\_MAXWR\_DEFINING\_BYTE\_SUPPORT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - maxWr - Optional Defining Byte Support.

## [◆ ](#gae61b18d964e575809a1ebe2189aae028)I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL

| #define I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL | ( |  | *maxwr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

(((maxwr) & \

[I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_MASK](#ga5f4c6dde339c3467bdb3aea0d680d01f)) \

>> [I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_SHIFT](#ga9bfab32baa69d2e437167afa31a6b428))

[I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_MASK](#ga5f4c6dde339c3467bdb3aea0d680d01f)

#define I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_MASK

Get Max Data Speed (GETMXDS) - Max Sustained Data Rate bitmask.

**Definition** ccc.h:763

[I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_SHIFT](#ga9bfab32baa69d2e437167afa31a6b428)

#define I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_SHIFT

Get Max Data Speed (GETMXDS) - Max Sustained Data Rate bit shift value.

**Definition** ccc.h:760

Get Max Data Speed (GETMXDS) - maxWr - Max Sustained Data Rate.

Obtain Max Sustained Data Rate value from GETMXDS maxWr value obtained via GETMXDS.

Parameters
:   | maxwr | GETMXDS maxWr value. |
    | --- | --- |

## [◆ ](#ga5f4c6dde339c3467bdb3aea0d680d01f)I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_MASK

| #define I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_MASK   (0x07U << I3C\_CCC\_GET\_MXDS\_MAXWR\_MAX\_SDR\_FSCL\_SHIFT) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - Max Sustained Data Rate bitmask.

## [◆ ](#ga9bfab32baa69d2e437167afa31a6b428)I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_SHIFT

| #define I3C\_CCC\_GETMXDS\_MAXWR\_MAX\_SDR\_FSCL\_SHIFT   0 |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - Max Sustained Data Rate bit shift value.

## [◆ ](#ga5e264e39aa2d4b602ec5e3218708e2f6)I3C\_CCC\_GETMXDS\_TSCO\_10NS

| #define I3C\_CCC\_GETMXDS\_TSCO\_10NS   2 |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 10ns.

## [◆ ](#ga2b27c9023f447da9c474c078091cf580)I3C\_CCC\_GETMXDS\_TSCO\_11NS

| #define I3C\_CCC\_GETMXDS\_TSCO\_11NS   3 |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 11ns.

## [◆ ](#ga06d33d1884a30d179aace82af956d62d)I3C\_CCC\_GETMXDS\_TSCO\_12NS

| #define I3C\_CCC\_GETMXDS\_TSCO\_12NS   4 |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 12ns.

## [◆ ](#gad5e417bc3cabf8a915d1e7938415125a)I3C\_CCC\_GETMXDS\_TSCO\_8NS

| #define I3C\_CCC\_GETMXDS\_TSCO\_8NS   0 |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 8ns.

## [◆ ](#gaaee475f82f3a3759c7d62bb48082ebc2)I3C\_CCC\_GETMXDS\_TSCO\_9NS

| #define I3C\_CCC\_GETMXDS\_TSCO\_9NS   1 |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - Clock to Data Turnaround <= 9ns.

## [◆ ](#ga5be034f241ccfb59534ae247d2e31d85)I3C\_CCC\_GETMXDS\_TSCO\_GT\_12NS

| #define I3C\_CCC\_GETMXDS\_TSCO\_GT\_12NS   7 |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Max Data Speed (GETMXDS) - Clock to Data Turnaround > 12ns.

## [◆ ](#ga04f7386d55742e935fa4dbfeb0120124)I3C\_CCC\_GETPID

| #define I3C\_CCC\_GETPID   0x8DU |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Provisioned ID (Direct).

## [◆ ](#ga858603dfc251b684b9d049b90119993d)I3C\_CCC\_GETSTATUS

| #define I3C\_CCC\_GETSTATUS   0x90U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Device Status (Direct).

## [◆ ](#ga660e179384e9426b498cd62da5665b15)I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE

| #define I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE | ( |  | *status* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

(((status) & [I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_MASK](#ga1006146ca810c06674fbee0ee1f66286)) \

>> [I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_SHIFT](#ga8aca4592e579411a2c17f80ad682d93f))

[I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_MASK](#ga1006146ca810c06674fbee0ee1f66286)

#define I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_MASK

GETSTATUS Format 1 - Activity Mode bitmask.

**Definition** ccc.h:599

[I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_SHIFT](#ga8aca4592e579411a2c17f80ad682d93f)

#define I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_SHIFT

GETSTATUS Format 1 - Activity Mode bit shift value.

**Definition** ccc.h:596

GETSTATUS Format 1 - Activity Mode.

Obtain Activity Mode from GETSTATUS Format 1 value obtained via GETSTATUS.

Parameters
:   | status | GETSTATUS Format 1 value |
    | --- | --- |

## [◆ ](#ga1006146ca810c06674fbee0ee1f66286)I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_MASK

| #define I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_MASK   (0x03U << [I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_SHIFT](#ga8aca4592e579411a2c17f80ad682d93f)) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

GETSTATUS Format 1 - Activity Mode bitmask.

## [◆ ](#ga8aca4592e579411a2c17f80ad682d93f)I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_SHIFT

| #define I3C\_CCC\_GETSTATUS\_ACTIVITY\_MODE\_SHIFT   6 |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

GETSTATUS Format 1 - Activity Mode bit shift value.

## [◆ ](#ga1436dc4b9f71c6f61fd3e3331857f3bd)I3C\_CCC\_GETSTATUS\_NUM\_INT

| #define I3C\_CCC\_GETSTATUS\_NUM\_INT | ( |  | *status* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

(((status) & [I3C\_CCC\_GETSTATUS\_NUM\_INT\_MASK](#gae0bcc3ea13a34f63b073d63569d2e53a)) \

>> [I3C\_CCC\_GETSTATUS\_NUM\_INT\_SHIFT](#ga1c07ae6c80088b8336f7f2d728487606))

[I3C\_CCC\_GETSTATUS\_NUM\_INT\_SHIFT](#ga1c07ae6c80088b8336f7f2d728487606)

#define I3C\_CCC\_GETSTATUS\_NUM\_INT\_SHIFT

GETSTATUS Format 1 - Number of Pending Interrupts bit shift value.

**Definition** ccc.h:615

[I3C\_CCC\_GETSTATUS\_NUM\_INT\_MASK](#gae0bcc3ea13a34f63b073d63569d2e53a)

#define I3C\_CCC\_GETSTATUS\_NUM\_INT\_MASK

GETSTATUS Format 1 - Number of Pending Interrupts bitmask.

**Definition** ccc.h:618

GETSTATUS Format 1 - Number of Pending Interrupts.

Obtain Number of Pending Interrupts from GETSTATUS Format 1 value obtained via GETSTATUS.

Parameters
:   | status | GETSTATUS Format 1 value |
    | --- | --- |

## [◆ ](#gae0bcc3ea13a34f63b073d63569d2e53a)I3C\_CCC\_GETSTATUS\_NUM\_INT\_MASK

| #define I3C\_CCC\_GETSTATUS\_NUM\_INT\_MASK   (0x0FU << [I3C\_CCC\_GETSTATUS\_NUM\_INT\_SHIFT](#ga1c07ae6c80088b8336f7f2d728487606)) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

GETSTATUS Format 1 - Number of Pending Interrupts bitmask.

## [◆ ](#ga1c07ae6c80088b8336f7f2d728487606)I3C\_CCC\_GETSTATUS\_NUM\_INT\_SHIFT

| #define I3C\_CCC\_GETSTATUS\_NUM\_INT\_SHIFT   0 |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

GETSTATUS Format 1 - Number of Pending Interrupts bit shift value.

## [◆ ](#ga94afb0ebcfce55b85fc4a81953b4178a)I3C\_CCC\_GETSTATUS\_PRECR\_DEEP\_SLEEP\_DETECTED

| #define I3C\_CCC\_GETSTATUS\_PRECR\_DEEP\_SLEEP\_DETECTED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

GETSTATUS Format 2 - PERCR - Deep Sleep Detected bit.

## [◆ ](#gadda1781cae312f4e588c3d3dcfa74f38)I3C\_CCC\_GETSTATUS\_PRECR\_HANDOFF\_DELAY\_NACK

| #define I3C\_CCC\_GETSTATUS\_PRECR\_HANDOFF\_DELAY\_NACK   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

GETSTATUS Format 2 - PERCR - Handoff Delay NACK.

## [◆ ](#gaee3dd61e9ac723a90868c610d0179b7d)I3C\_CCC\_GETSTATUS\_PROTOCOL\_ERR

| #define I3C\_CCC\_GETSTATUS\_PROTOCOL\_ERR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

GETSTATUS Format 1 - Protocol Error bit.

## [◆ ](#ga66bb5e8027b103298f882f413f8ee6e8)I3C\_CCC\_GETXTIME

| #define I3C\_CCC\_GETXTIME   0x99U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Get Exchange Timing Information (Direct).

## [◆ ](#ga290cc5511d95b5be31c2c4cfea929085)I3C\_CCC\_MLANE

| #define I3C\_CCC\_MLANE | ( |  | *broadcast* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

((broadcast) ? 0x2DU : 0x9DU)

Multi-Lane Data Transfer Control (Broadcast).

## [◆ ](#ga424cb224727d33c1ab18e4149bbea232)I3C\_CCC\_RSTACT

| #define I3C\_CCC\_RSTACT | ( |  | *broadcast* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

((broadcast) ? 0x2AU : 0x9AU)

Target Reset Action.

Parameters
:   | broadcast | True if broadcast, false if direct. |
    | --- | --- |

## [◆ ](#gaed94df1e670fc3670970f261865d6f63)I3C\_CCC\_RSTDAA

| #define I3C\_CCC\_RSTDAA   0x06U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Reset Dynamic Address Assignment (Broadcast).

## [◆ ](#ga46611eab0c82b74c615a7a7435f79d85)I3C\_CCC\_RSTGRPA

| #define I3C\_CCC\_RSTGRPA | ( |  | *broadcast* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

((broadcast) ? 0x2CU : 0x9CU)

Reset Group Address.

Parameters
:   | broadcast | True if broadcast, false if direct. |
    | --- | --- |

## [◆ ](#gae995ef9e94beb26932b47136bdf89b57)I3C\_CCC\_SETAASA

| #define I3C\_CCC\_SETAASA   0x29U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Set All Addresses to Static Addresses (Broadcast).

## [◆ ](#gab3cac5de39903cc2331a38ac66c4ff14)I3C\_CCC\_SETBRGTGT

| #define I3C\_CCC\_SETBRGTGT   0x93U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Set Bridge Targets (Direct).

## [◆ ](#gac0f85a020956e3ee1ae8da899a9e06a6)I3C\_CCC\_SETBUSCON

| #define I3C\_CCC\_SETBUSCON   0x0CU |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Set Bus Context (Broadcast).

## [◆ ](#ga134d5948b056144c83b133f93083a0f8)I3C\_CCC\_SETDASA

| #define I3C\_CCC\_SETDASA   0x87U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Set Dynamic Address from Static Address (Direct).

## [◆ ](#gaa0bef5d42c9bf2a21e888e5d5998d5cb)I3C\_CCC\_SETGRPA

| #define I3C\_CCC\_SETGRPA   0x9BU |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Set Group Address (Direct).

## [◆ ](#ga97fd874b2e6c918f2e1262f7600bfd64)I3C\_CCC\_SETMRL

| #define I3C\_CCC\_SETMRL | ( |  | *broadcast* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

((broadcast) ? 0x0AU : 0x8AU)

Set Max Read Length (Broadcast or Direct).

Parameters
:   | broadcast | True if broadcast, false if direct. |
    | --- | --- |

## [◆ ](#gaab1ccf6cd47dfecee24811501e123802)I3C\_CCC\_SETMWL

| #define I3C\_CCC\_SETMWL | ( |  | *broadcast* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

((broadcast) ? 0x09U : 0x89U)

Set Max Write Length (Broadcast or Direct).

Parameters
:   | broadcast | True if broadcast, false if direct. |
    | --- | --- |

## [◆ ](#gae0d6d0047f2c6e73e49e5019ec8d9ff0)I3C\_CCC\_SETNEWDA

| #define I3C\_CCC\_SETNEWDA   0x88U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Set New Dynamic Address (Direct).

## [◆ ](#ga5cf5cdb40299d4f8203b8035dacac17a)I3C\_CCC\_SETROUTE

| #define I3C\_CCC\_SETROUTE   0x96U |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Set Route (Direct).

## [◆ ](#ga4203d5fdd9e9ca253803359934f22524)I3C\_CCC\_SETXTIME

| #define I3C\_CCC\_SETXTIME | ( |  | *broadcast* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

((broadcast) ? 0x28U : 0x98U)

Exchange Timing Information (Broadcast or Direct).

Parameters
:   | broadcast | True if broadcast, false if direct. |
    | --- | --- |

## [◆ ](#gaee5fb96b2d54df3b1b7aadefd54a608d)I3C\_CCC\_VENDOR

| #define I3C\_CCC\_VENDOR | ( |  | *broadcast*, |
| --- | --- | --- | --- |
|  |  |  | *id* ) |

`#include <[ccc.h](ccc_8h.md)>`

**Value:**

((id) + ((broadcast) ? 0x61U : 0xE0U))

Vendor/Standard Extension.

Parameters
:   | broadcast | True if broadcast, false if direct. |
    | --- | --- |
    | id | Extension ID. |

## Enumeration Type Documentation

## [◆ ](#ga1977f86d4865a97047119e5b3fbcb172)i3c\_ccc\_getstatus\_defbyte

| enum [i3c\_ccc\_getstatus\_defbyte](#ga1977f86d4865a97047119e5b3fbcb172) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Defining byte values for GETSTATUS Format 2.

| Enumerator | |
| --- | --- |
| GETSTATUS\_FORMAT\_2\_TGTSTAT | Target status. |
| GETSTATUS\_FORMAT\_2\_PRECR | PRECR - Alternate status format describing Controller-capable device. |
| GETSTATUS\_FORMAT\_2\_INVALID | Invalid defining byte. |

## [◆ ](#ga75934ea02ef8eb1c737da3ebfd368648)i3c\_ccc\_getstatus\_fmt

| enum [i3c\_ccc\_getstatus\_fmt](#ga75934ea02ef8eb1c737da3ebfd368648) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Indicate which format of GETSTATUS to use.

| Enumerator | |
| --- | --- |
| GETSTATUS\_FORMAT\_1 | GETSTATUS Format 1. |
| GETSTATUS\_FORMAT\_2 | GETSTATUS Format 2. |

## [◆ ](#ga61e1a1945a39b374edee5b75fbeb27d1)i3c\_ccc\_rstact\_defining\_byte

| enum [i3c\_ccc\_rstact\_defining\_byte](#ga61e1a1945a39b374edee5b75fbeb27d1) |
| --- |

`#include <[ccc.h](ccc_8h.md)>`

Enum for I3C Reset Action (RSTACT) Defining Byte Values.

| Enumerator | |
| --- | --- |
| I3C\_CCC\_RSTACT\_NO\_RESET | No Reset on Target Reset Pattern. |
| I3C\_CCC\_RSTACT\_PERIPHERAL\_ONLY | Reset the I3C Peripheral Only. |
| I3C\_CCC\_RSTACT\_RESET\_WHOLE\_TARGET | Reset the Whole Target. |
| I3C\_CCC\_RSTACT\_DEBUG\_NETWORK\_ADAPTER | Debug Network Adapter Reset. |
| I3C\_CCC\_RSTACT\_VIRTUAL\_TARGET\_DETECT | Virtual Target Detect. |

## Function Documentation

## [◆ ](#gaf5fbaf2108053df855c95233181dc580)i3c\_ccc\_do\_events\_all\_set()

| int i3c\_ccc\_do\_events\_all\_set | ( | const struct [device](structdevice.md) \* | *controller*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable*, |
|  |  | struct [i3c\_ccc\_events](structi3c__ccc__events.md) \* | *events* ) |

`#include <[ccc.h](ccc_8h.md)>`

Broadcast ENEC/DISEC to enable/disable target events.

Helper function to broadcast Target Events Command to enable or disable target events (ENEC/DISEC).

Parameters
:   | [in] | controller | Pointer to the controller device driver instance. |
    | --- | --- | --- |
    | [in] | enable | ENEC if true, DISEC if false. |
    | [in] | events | Pointer to the event struct. |

Returns

See also
:   [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862 "Send CCC to the bus.")

## [◆ ](#gaf6575647b4b8f858f90bf2785a0f0d49)i3c\_ccc\_do\_events\_set()

| int i3c\_ccc\_do\_events\_set | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable*, |
|  |  | struct [i3c\_ccc\_events](structi3c__ccc__events.md) \* | *events* ) |

`#include <[ccc.h](ccc_8h.md)>`

Direct CCC ENEC/DISEC to enable/disable target events.

Helper function to send Target Events Command to enable or disable target events (ENEC/DISEC) on a single target.

Parameters
:   | [in] | target | Pointer to the target device descriptor. |
    | --- | --- | --- |
    | [in] | enable | ENEC if true, DISEC if false. |
    | [in] | events | Pointer to the event struct. |

Returns

See also
:   [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862 "Send CCC to the bus.")

## [◆ ](#ga7d5bb9c8fd88721b858180f503c1af4c)i3c\_ccc\_do\_getbcr()

| int i3c\_ccc\_do\_getbcr | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, |
| --- | --- | --- | --- |
|  |  | struct [i3c\_ccc\_getbcr](structi3c__ccc__getbcr.md) \* | *bcr* ) |

`#include <[ccc.h](ccc_8h.md)>`

Get BCR from a target.

Helper function to get BCR (Bus Characteristic Register) from target device.

Parameters
:   | [in] | target | Pointer to the target device descriptor. |
    | --- | --- | --- |
    | [out] | bcr | Pointer to the BCR payload structure. |

Returns

See also
:   [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862 "Send CCC to the bus.")

## [◆ ](#ga7f886c0dbe0afec07f5678b574dc1101)i3c\_ccc\_do\_getdcr()

| int i3c\_ccc\_do\_getdcr | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, |
| --- | --- | --- | --- |
|  |  | struct [i3c\_ccc\_getdcr](structi3c__ccc__getdcr.md) \* | *dcr* ) |

`#include <[ccc.h](ccc_8h.md)>`

Get DCR from a target.

Helper function to get DCR (Device Characteristic Register) from target device.

Parameters
:   | [in] | target | Pointer to the target device descriptor. |
    | --- | --- | --- |
    | [out] | dcr | Pointer to the DCR payload structure. |

Returns

See also
:   [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862 "Send CCC to the bus.")

## [◆ ](#gac4331a4c7dbb7af0eaea63b01bb08485)i3c\_ccc\_do\_getmrl()

| int i3c\_ccc\_do\_getmrl | ( | const struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, |
| --- | --- | --- | --- |
|  |  | struct [i3c\_ccc\_mrl](structi3c__ccc__mrl.md) \* | *mrl* ) |

`#include <[ccc.h](ccc_8h.md)>`

Single target GETMRL to Get Maximum Read Length.

Helper function to do GETMRL (Get Maximum Read Length) of one target.

Note this uses the BCR of the target to determine whether to send the optional IBI payload size.

Parameters
:   | [in] | target | Pointer to the target device descriptor. |
    | --- | --- | --- |
    | [out] | mrl | Pointer to GETMRL payload. |

Returns

See also
:   [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862 "Send CCC to the bus.")

## [◆ ](#gaf1077e3d6cf8a7e1f0e02e985058e507)i3c\_ccc\_do\_getmwl()

| int i3c\_ccc\_do\_getmwl | ( | const struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, |
| --- | --- | --- | --- |
|  |  | struct [i3c\_ccc\_mwl](structi3c__ccc__mwl.md) \* | *mwl* ) |

`#include <[ccc.h](ccc_8h.md)>`

Single target GETMWL to Get Maximum Write Length.

Helper function to do GETMWL (Get Maximum Write Length) of one target.

Parameters
:   | [in] | target | Pointer to the target device descriptor. |
    | --- | --- | --- |
    | [out] | mwl | Pointer to GETMWL payload. |

Returns

See also
:   [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862 "Send CCC to the bus.")

## [◆ ](#ga949810a9a7c862d00ce4eec7e2c4d7df)i3c\_ccc\_do\_getpid()

| int i3c\_ccc\_do\_getpid | ( | struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, |
| --- | --- | --- | --- |
|  |  | struct [i3c\_ccc\_getpid](structi3c__ccc__getpid.md) \* | *pid* ) |

`#include <[ccc.h](ccc_8h.md)>`

Get PID from a target.

Helper function to get PID (Provisioned ID) from target device.

Parameters
:   | [in] | target | Pointer to the target device descriptor. |
    | --- | --- | --- |
    | [out] | pid | Pointer to the PID payload structure. |

Returns

See also
:   [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862 "Send CCC to the bus.")

## [◆ ](#ga4fe9d056a5ac78ff83513763a71c7dfe)i3c\_ccc\_do\_getstatus()

| int i3c\_ccc\_do\_getstatus | ( | const struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, |
| --- | --- | --- | --- |
|  |  | union [i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md) \* | *status*, |
|  |  | enum [i3c\_ccc\_getstatus\_fmt](#ga75934ea02ef8eb1c737da3ebfd368648) | *fmt*, |
|  |  | enum [i3c\_ccc\_getstatus\_defbyte](#ga1977f86d4865a97047119e5b3fbcb172) | *defbyte* ) |

`#include <[ccc.h](ccc_8h.md)>`

Single target GETSTATUS to Get Target Status.

Helper function to do GETSTATUS (Get Target Status) of one target.

Note this uses the BCR of the target to determine whether to send the optional IBI payload size.

Parameters
:   | [in] | target | Pointer to the target device descriptor. |
    | --- | --- | --- |
    | [out] | status | Pointer to GETSTATUS payload. |
    | [in] | fmt | Which GETSTATUS to use. |
    | [in] | defbyte | Defining Byte if using format 2. |

Returns

See also
:   [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862 "Send CCC to the bus.")

## [◆ ](#ga1cb2804fc7dcbb322cd26001d7953c95)i3c\_ccc\_do\_getstatus\_fmt1()

| | int i3c\_ccc\_do\_getstatus\_fmt1 | ( | const struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, | | --- | --- | --- | --- | |  |  | union [i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md) \* | *status* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

Single target GETSTATUS to Get Target Status (Format 1).

Helper function to do GETSTATUS (Get Target Status, format 1) of one target.

Parameters
:   | [in] | target | Pointer to the target device descriptor. |
    | --- | --- | --- |
    | [out] | status | Pointer to GETSTATUS payload. |

Returns

See also
:   [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862 "Send CCC to the bus.")

## [◆ ](#ga4eaaaf7b7e9f2f8dd657d4f6a0de8bfb)i3c\_ccc\_do\_getstatus\_fmt2()

| | int i3c\_ccc\_do\_getstatus\_fmt2 | ( | const struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, | | --- | --- | --- | --- | |  |  | union [i3c\_ccc\_getstatus](unioni3c__ccc__getstatus.md) \* | *status*, | |  |  | enum [i3c\_ccc\_getstatus\_defbyte](#ga1977f86d4865a97047119e5b3fbcb172) | *defbyte* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

Single target GETSTATUS to Get Target Status (Format 2).

Helper function to do GETSTATUS (Get Target Status, format 2) of one target.

Parameters
:   | [in] | target | Pointer to the target device descriptor. |
    | --- | --- | --- |
    | [out] | status | Pointer to GETSTATUS payload. |
    | [in] | defbyte | Defining Byte for GETSTATUS format 2. |

Returns

See also
:   [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862 "Send CCC to the bus.")

## [◆ ](#ga40294e43357f46338a6542f9a03d7ce7)i3c\_ccc\_do\_rstact\_all()

| int i3c\_ccc\_do\_rstact\_all | ( | const struct [device](structdevice.md) \* | *controller*, |
| --- | --- | --- | --- |
|  |  | enum [i3c\_ccc\_rstact\_defining\_byte](#ga61e1a1945a39b374edee5b75fbeb27d1) | *action* ) |

`#include <[ccc.h](ccc_8h.md)>`

Broadcast RSTACT to reset I3C Peripheral.

Helper function to broadcast Target Reset Action (RSTACT) to all connected targets to Reset the I3C Peripheral Only (0x01).

Parameters
:   | [in] | controller | Pointer to the controller device driver instance. |
    | --- | --- | --- |
    | [in] | action | What reset action to perform. |

Returns

See also
:   [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862 "Send CCC to the bus.")

## [◆ ](#gab1102467bb92a2aff7c9c1a66dd273a7)i3c\_ccc\_do\_rstdaa\_all()

| int i3c\_ccc\_do\_rstdaa\_all | ( | const struct [device](structdevice.md) \* | *controller* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

Broadcast RSTDAA to reset dynamic addresses for all targets.

Helper function to reset dynamic addresses of all connected targets.

Parameters
:   | [in] | controller | Pointer to the controller device driver instance. |
    | --- | --- | --- |

Returns

See also
:   [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862 "Send CCC to the bus.")

## [◆ ](#gae4be97aae166be3b6e794fd77c8be6f8)i3c\_ccc\_do\_setdasa()

| int i3c\_ccc\_do\_setdasa | ( | const struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

Set Dynamic Address from Static Address for a target.

Helper function to do SETDASA (Set Dynamic Address from Static Address) for a particular target.

Note this does not update `target` with the new dynamic address.

Parameters
:   | [in] | target | Pointer to the target device descriptor where the device is configured with a static address. |
    | --- | --- | --- |

Returns

See also
:   [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862 "Send CCC to the bus.")

## [◆ ](#ga6e4f26d23919a619c89624b15d16390a)i3c\_ccc\_do\_setmrl()

| int i3c\_ccc\_do\_setmrl | ( | const struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, |
| --- | --- | --- | --- |
|  |  | const struct [i3c\_ccc\_mrl](structi3c__ccc__mrl.md) \* | *mrl* ) |

`#include <[ccc.h](ccc_8h.md)>`

Single target SETMRL to Set Maximum Read Length.

Helper function to do SETMRL (Set Maximum Read Length) to one target.

Note this uses the BCR of the target to determine whether to send the optional IBI payload size.

Parameters
:   | [in] | target | Pointer to the target device descriptor. |
    | --- | --- | --- |
    | [in] | mrl | Pointer to SETMRL payload. |

Returns

See also
:   [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862 "Send CCC to the bus.")

## [◆ ](#ga2542f4ebcc0c2bb31bc8e334955620b0)i3c\_ccc\_do\_setmrl\_all()

| int i3c\_ccc\_do\_setmrl\_all | ( | const struct [device](structdevice.md) \* | *controller*, |
| --- | --- | --- | --- |
|  |  | const struct [i3c\_ccc\_mrl](structi3c__ccc__mrl.md) \* | *mrl*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *has\_ibi\_size* ) |

`#include <[ccc.h](ccc_8h.md)>`

Broadcast SETMRL to Set Maximum Read Length.

Helper function to do SETMRL (Set Maximum Read Length) to all connected targets.

Parameters
:   | [in] | controller | Pointer to the controller device driver instance. |
    | --- | --- | --- |
    | [in] | mrl | Pointer to SETMRL payload. |
    | [in] | has\_ibi\_size | True if also sending the optional IBI payload size. False if not sending. |

Returns

See also
:   [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862 "Send CCC to the bus.")

## [◆ ](#gab3de109c73dd58f6d2cf0a9229408f49)i3c\_ccc\_do\_setmwl()

| int i3c\_ccc\_do\_setmwl | ( | const struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, |
| --- | --- | --- | --- |
|  |  | const struct [i3c\_ccc\_mwl](structi3c__ccc__mwl.md) \* | *mwl* ) |

`#include <[ccc.h](ccc_8h.md)>`

Single target SETMWL to Set Maximum Write Length.

Helper function to do SETMWL (Set Maximum Write Length) to one target.

Parameters
:   | [in] | target | Pointer to the target device descriptor. |
    | --- | --- | --- |
    | [in] | mwl | Pointer to SETMWL payload. |

Returns

See also
:   [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862 "Send CCC to the bus.")

## [◆ ](#ga66c8c6318134d6287f4a14f6c31af02d)i3c\_ccc\_do\_setmwl\_all()

| int i3c\_ccc\_do\_setmwl\_all | ( | const struct [device](structdevice.md) \* | *controller*, |
| --- | --- | --- | --- |
|  |  | const struct [i3c\_ccc\_mwl](structi3c__ccc__mwl.md) \* | *mwl* ) |

`#include <[ccc.h](ccc_8h.md)>`

Broadcast SETMWL to Set Maximum Write Length.

Helper function to do SETMWL (Set Maximum Write Length) to all connected targets.

Parameters
:   | [in] | controller | Pointer to the controller device driver instance. |
    | --- | --- | --- |
    | [in] | mwl | Pointer to SETMWL payload. |

Returns

See also
:   [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862 "Send CCC to the bus.")

## [◆ ](#ga6d19dc9d3b421b4c936c6183977c4eec)i3c\_ccc\_do\_setnewda()

| int i3c\_ccc\_do\_setnewda | ( | const struct [i3c\_device\_desc](structi3c__device__desc.md) \* | *target*, |
| --- | --- | --- | --- |
|  |  | struct [i3c\_ccc\_address](structi3c__ccc__address.md) | *new\_da* ) |

`#include <[ccc.h](ccc_8h.md)>`

Set New Dynamic Address for a target.

Helper function to do SETNEWDA(Set New Dynamic Address) for a particular target.

Note this does not update `target` with the new dynamic address.

Parameters
:   | [in] | target | Pointer to the target device descriptor where the device is configured with a static address. |
    | --- | --- | --- |
    | [in] | new\_da | Pointer to the new\_da struct. |

Returns

See also
:   [i3c\_do\_ccc](group__i3c__interface.md#gaa6d5445489bfc8611c98b93f49305862 "Send CCC to the bus.")

## [◆ ](#gaaf692d0b89fd62a61d93f1577b25ce25)i3c\_ccc\_is\_payload\_broadcast()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) i3c\_ccc\_is\_payload\_broadcast | ( | const struct [i3c\_ccc\_payload](structi3c__ccc__payload.md) \* | *payload* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ccc.h](ccc_8h.md)>`

Test if I3C CCC payload is for broadcast.

This tests if the CCC payload is for broadcast.

Parameters
:   | [in] | payload | Pointer to the CCC payload. |
    | --- | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if payload target is broadcast |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if payload target is direct |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
