---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/cellular_8h.html
original_path: doxygen/html/cellular_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cellular.h File Reference

Public cellular network API.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`

[Go to the source code of this file.](cellular_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [cellular\_network](structcellular__network.md) |
|  | Cellular network structure. [More...](structcellular__network.md#details) |
| struct | [cellular\_driver\_api](structcellular__driver__api.md) |
|  | Cellular driver API. [More...](structcellular__driver__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [cellular\_api\_configure\_networks](group__cellular__interface.md#ga71ddc5b9e09da398d02caadc91ef3cfc)) (const struct [device](structdevice.md) \*dev, const struct [cellular\_network](structcellular__network.md) \*networks, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size) |
|  | API for configuring networks. |
| typedef int(\* | [cellular\_api\_get\_supported\_networks](group__cellular__interface.md#ga6aa2c51fa80d5420593021c35444308a)) (const struct [device](structdevice.md) \*dev, const struct [cellular\_network](structcellular__network.md) \*\*networks, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*size) |
|  | API for getting supported networks. |
| typedef int(\* | [cellular\_api\_get\_signal](group__cellular__interface.md#ga75cac77838970288d4d23647eaafd30b)) (const struct [device](structdevice.md) \*dev, const enum [cellular\_signal\_type](group__cellular__interface.md#ga746c0862b9a5da7c766e42e4d6025f47) type, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*value) |
|  | API for getting network signal strength. |
| typedef int(\* | [cellular\_api\_get\_modem\_info](group__cellular__interface.md#ga03095206ae2b77ce232dd05b172bd56d)) (const struct [device](structdevice.md) \*dev, const enum [cellular\_modem\_info\_type](group__cellular__interface.md#gad6e38e31d82075c51933fcbb2ff2de30) type, char \*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | API for getting modem information. |
| typedef int(\* | [cellular\_api\_get\_registration\_status](group__cellular__interface.md#ga08a0966933caa70d7044342ed2ad8eb6)) (const struct [device](structdevice.md) \*dev, enum [cellular\_access\_technology](group__cellular__interface.md#ga168002533ce39996e68bda2c2e92428e) tech, enum [cellular\_registration\_status](group__cellular__interface.md#ga7309390ed507748fdb72cf078b8e08a4) \*status) |
|  | API for getting registration status. |

| Enumerations | |
| --- | --- |
| enum | [cellular\_access\_technology](group__cellular__interface.md#ga168002533ce39996e68bda2c2e92428e) {     [CELLULAR\_ACCESS\_TECHNOLOGY\_GSM](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea9bcd1016388c265e1d20a7fcdfa37255) = 0 , [CELLULAR\_ACCESS\_TECHNOLOGY\_GPRS](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea7c1911e14140b58340092891879d6048) , [CELLULAR\_ACCESS\_TECHNOLOGY\_UMTS](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea3edbbd5543a26bb12a28ac131e97da0f) , [CELLULAR\_ACCESS\_TECHNOLOGY\_EDGE](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428eab205ca0387de08ea4b6f5612fcabbef4) ,     [CELLULAR\_ACCESS\_TECHNOLOGY\_LTE](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea0e441c38a4166e9ff807f809cee48ebc) , [CELLULAR\_ACCESS\_TECHNOLOGY\_LTE\_CAT\_M1](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428eaf2844e36d3bcaf8adb67e153ee8203dc) , [CELLULAR\_ACCESS\_TECHNOLOGY\_LTE\_CAT\_M2](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea89be8003f89a2079275b8ed95a68d7e1) , [CELLULAR\_ACCESS\_TECHNOLOGY\_NB\_IOT](group__cellular__interface.md#gga168002533ce39996e68bda2c2e92428ea6f06e534f995b27f5856f57673890a3d)   } |
|  | Cellular access technologies. [More...](group__cellular__interface.md#ga168002533ce39996e68bda2c2e92428e) |
| enum | [cellular\_signal\_type](group__cellular__interface.md#ga746c0862b9a5da7c766e42e4d6025f47) { [CELLULAR\_SIGNAL\_RSSI](group__cellular__interface.md#gga746c0862b9a5da7c766e42e4d6025f47afa617b15b16f73ae0f9717b86ef8fa4a) , [CELLULAR\_SIGNAL\_RSRP](group__cellular__interface.md#gga746c0862b9a5da7c766e42e4d6025f47ae442515aa0176fd207864d8f673bff6a) , [CELLULAR\_SIGNAL\_RSRQ](group__cellular__interface.md#gga746c0862b9a5da7c766e42e4d6025f47a2b4e39a72ac12182dd4386e72af62338) } |
|  | Cellular signal type. [More...](group__cellular__interface.md#ga746c0862b9a5da7c766e42e4d6025f47) |
| enum | [cellular\_modem\_info\_type](group__cellular__interface.md#gad6e38e31d82075c51933fcbb2ff2de30) {     [CELLULAR\_MODEM\_INFO\_IMEI](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30aec77c2ed582a9e9002d0be26837864de) , [CELLULAR\_MODEM\_INFO\_MODEL\_ID](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30a6fa8d55ae35e04e8f0d68a6d3cd002c8) , [CELLULAR\_MODEM\_INFO\_MANUFACTURER](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30a57c4dde28d72170528954cd7cc21a0e1) , [CELLULAR\_MODEM\_INFO\_FW\_VERSION](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30acef002318e29733d68a9286fd133c027) ,     [CELLULAR\_MODEM\_INFO\_SIM\_IMSI](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30a06207052e9bcebcbd37d22aa2715d245) , [CELLULAR\_MODEM\_INFO\_SIM\_ICCID](group__cellular__interface.md#ggad6e38e31d82075c51933fcbb2ff2de30ac4969f42b98300317e2406916031d77d)   } |
|  | Cellular modem info type. [More...](group__cellular__interface.md#gad6e38e31d82075c51933fcbb2ff2de30) |
| enum | [cellular\_registration\_status](group__cellular__interface.md#ga7309390ed507748fdb72cf078b8e08a4) {     [CELLULAR\_REGISTRATION\_NOT\_REGISTERED](group__cellular__interface.md#gga7309390ed507748fdb72cf078b8e08a4ac7dc9f39e18a20b44fe35229dffbbf27) = 0 , [CELLULAR\_REGISTRATION\_REGISTERED\_HOME](group__cellular__interface.md#gga7309390ed507748fdb72cf078b8e08a4aba7597c5d5325f5a4ed0912a514b3cbe) , [CELLULAR\_REGISTRATION\_SEARCHING](group__cellular__interface.md#gga7309390ed507748fdb72cf078b8e08a4a46fbd7b29f66aa33f05176eadfe3a175) , [CELLULAR\_REGISTRATION\_DENIED](group__cellular__interface.md#gga7309390ed507748fdb72cf078b8e08a4a64b4da980b161a28ff716f605aeb0a0e) ,     [CELLULAR\_REGISTRATION\_UNKNOWN](group__cellular__interface.md#gga7309390ed507748fdb72cf078b8e08a4a08f82068a7cd83a0ca706bc1072ea9a1) , [CELLULAR\_REGISTRATION\_REGISTERED\_ROAMING](group__cellular__interface.md#gga7309390ed507748fdb72cf078b8e08a4afe6ca91267d3b9bc28b3ea57b8d8545d)   } |

| Functions | |
| --- | --- |
| static int | [cellular\_configure\_networks](group__cellular__interface.md#gaa53d52e58221c998eec272a4d063bdd4) (const struct [device](structdevice.md) \*dev, const struct [cellular\_network](structcellular__network.md) \*networks, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size) |
|  | Configure cellular networks for the device. |
| static int | [cellular\_get\_supported\_networks](group__cellular__interface.md#ga70340d22df56665b1d113abc8b314a95) (const struct [device](structdevice.md) \*dev, const struct [cellular\_network](structcellular__network.md) \*\*networks, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*size) |
|  | Get supported cellular networks for the device. |
| static int | [cellular\_get\_signal](group__cellular__interface.md#ga022eb4eecc300b14110107a46824cac0) (const struct [device](structdevice.md) \*dev, const enum [cellular\_signal\_type](group__cellular__interface.md#ga746c0862b9a5da7c766e42e4d6025f47) type, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) \*value) |
|  | Get signal for the device. |
| static int | [cellular\_get\_modem\_info](group__cellular__interface.md#ga757f0802fd72d61d035a81057f23d5ca) (const struct [device](structdevice.md) \*dev, const enum [cellular\_modem\_info\_type](group__cellular__interface.md#gad6e38e31d82075c51933fcbb2ff2de30) type, char \*info, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size) |
|  | Get modem info for the device. |
| static int | [cellular\_get\_registration\_status](group__cellular__interface.md#gae0ca6816f75b89055aa31370196e2c98) (const struct [device](structdevice.md) \*dev, enum [cellular\_access\_technology](group__cellular__interface.md#ga168002533ce39996e68bda2c2e92428e) tech, enum [cellular\_registration\_status](group__cellular__interface.md#ga7309390ed507748fdb72cf078b8e08a4) \*status) |
|  | Get network registration status for the device. |

## Detailed Description

Public cellular network API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [cellular.h](cellular_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
