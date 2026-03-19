---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/lorawan_8h.html
original_path: doxygen/html/lorawan_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lorawan.h File Reference

Public LoRaWAN APIs.
[More...](#details)

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`

[Go to the source code of this file.](lorawan_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [lorawan\_join\_otaa](structlorawan__join__otaa.md) |
|  | LoRaWAN join parameters for over-the-Air activation (OTAA). [More...](structlorawan__join__otaa.md#details) |
| struct | [lorawan\_join\_abp](structlorawan__join__abp.md) |
|  | LoRaWAN join parameters for activation by personalization (ABP). [More...](structlorawan__join__abp.md#details) |
| struct | [lorawan\_join\_config](structlorawan__join__config.md) |
|  | LoRaWAN join parameters. [More...](structlorawan__join__config.md#details) |
| struct | [lorawan\_downlink\_cb](structlorawan__downlink__cb.md) |
|  | LoRaWAN downlink callback parameters. [More...](structlorawan__downlink__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [LW\_RECV\_PORT\_ANY](group__lorawan__api.md#ga83dbf2575eaae85f1837567e9fb729a4)   [UINT16\_MAX](stdint_8h.md#a3ea490c9b3617d4479bd80ef93cd5602) |
|  | Flag to indicate receiving on any port. |

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [lorawan\_battery\_level\_cb\_t](group__lorawan__api.md#ga17a7a2e1dbfa19b9f7e18a81be5514dd)) (void) |
|  | Defines the battery level callback handler function signature. |
| typedef void(\* | [lorawan\_dr\_changed\_cb\_t](group__lorawan__api.md#ga87a8d911f1c825bcf8c77ada568f3ed4)) (enum [lorawan\_datarate](group__lorawan__api.md#ga276e66fb8ce88f853d1987686e31fc86) dr) |
|  | Defines the datarate changed callback handler function signature. |

| Enumerations | |
| --- | --- |
| enum | [lorawan\_class](group__lorawan__api.md#ga88b65799c3f1d98fbce80927218c0837) { [LORAWAN\_CLASS\_A](group__lorawan__api.md#gga88b65799c3f1d98fbce80927218c0837a538e56348e6d5b506e661e3af18aee6c) = 0x00 , [LORAWAN\_CLASS\_B](group__lorawan__api.md#gga88b65799c3f1d98fbce80927218c0837a79a9c205ac583051b2e072389491c7cb) = 0x01 , [LORAWAN\_CLASS\_C](group__lorawan__api.md#gga88b65799c3f1d98fbce80927218c0837ad158a1985688bbe54b20a8a808774547) = 0x02 } |
|  | LoRaWAN class types. [More...](group__lorawan__api.md#ga88b65799c3f1d98fbce80927218c0837) |
| enum | [lorawan\_act\_type](group__lorawan__api.md#ga2bf50442214ecdc717f1a24dc058a338) { [LORAWAN\_ACT\_OTAA](group__lorawan__api.md#gga2bf50442214ecdc717f1a24dc058a338a5f262e334bc46278bec491cd022b612a) = 0 , [LORAWAN\_ACT\_ABP](group__lorawan__api.md#gga2bf50442214ecdc717f1a24dc058a338a13bb2a28232081844e36308977ec6701) } |
|  | LoRaWAN activation types. [More...](group__lorawan__api.md#ga2bf50442214ecdc717f1a24dc058a338) |
| enum | [lorawan\_channels\_mask\_size](group__lorawan__api.md#ga0635d19612db9009775eae8e527d4897) {     [LORAWAN\_CHANNELS\_MASK\_SIZE\_AS923](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a577c304c4c1998916203e9ec7ae6e1be) = 1 , [LORAWAN\_CHANNELS\_MASK\_SIZE\_AU915](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a1bc4cacfd02a630226f629ed61f4e1ca) = 6 , [LORAWAN\_CHANNELS\_MASK\_SIZE\_CN470](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a2bdaecd6f1f853cd370ba89b465a9ee1) = 6 , [LORAWAN\_CHANNELS\_MASK\_SIZE\_CN779](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a8f2f25b3ab1167f69aa594a034b27180) = 1 ,     [LORAWAN\_CHANNELS\_MASK\_SIZE\_EU433](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a3b7968012bf2c8fa7adef454fc33124a) = 1 , [LORAWAN\_CHANNELS\_MASK\_SIZE\_EU868](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a3bc215c41b7fb5652c6729756b8f979a) = 1 , [LORAWAN\_CHANNELS\_MASK\_SIZE\_KR920](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a7443e6adbaaf4f7cb2037d8f3e42d86a) = 1 , [LORAWAN\_CHANNELS\_MASK\_SIZE\_IN865](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a9564d246e39448f478412861a3a87b7e) = 1 ,     [LORAWAN\_CHANNELS\_MASK\_SIZE\_US915](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897a054ebab376354c8a9e6a5f4e9f6f78ee) = 6 , [LORAWAN\_CHANNELS\_MASK\_SIZE\_RU864](group__lorawan__api.md#gga0635d19612db9009775eae8e527d4897aaa05e08a24aded2ada511fd2d1f4cebd) = 1   } |
|  | LoRaWAN channels mask sizes. [More...](group__lorawan__api.md#ga0635d19612db9009775eae8e527d4897) |
| enum | [lorawan\_datarate](group__lorawan__api.md#ga276e66fb8ce88f853d1987686e31fc86) {     [LORAWAN\_DR\_0](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a4b60b8eb52c07b40cbaaf94a4c56e1f6) = 0 , [LORAWAN\_DR\_1](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86ade4655b32ca976c317fa9f44ac8b148a) , [LORAWAN\_DR\_2](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a941f8a603aeb54560be7125a55c74159) , [LORAWAN\_DR\_3](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a4ac565dbaae0c6ad4e62dc34ca0c013a) ,     [LORAWAN\_DR\_4](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a6f6cd4ecd247f67cad08ede84649a939) , [LORAWAN\_DR\_5](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a08f879f1054ca54e488180b07d7ff952) , [LORAWAN\_DR\_6](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86acc624ccf8a9585889c3685217f56099f) , [LORAWAN\_DR\_7](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86aac8afba95d7187f0829aae7abda894d5) ,     [LORAWAN\_DR\_8](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a080b31031f5a2b54d84ed49b133b0a86) , [LORAWAN\_DR\_9](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86afbc8d04236410a6107cccfd71ba4bace) , [LORAWAN\_DR\_10](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a0a18193e15d268d262d58897d39993b3) , [LORAWAN\_DR\_11](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a2a631e746ffc5c4378e39b7a90dd44e2) ,     [LORAWAN\_DR\_12](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a0df057cf1505ba94876deaeddd515548) , [LORAWAN\_DR\_13](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a18bfd63ae262f992d9d12f8d56cc217e) , [LORAWAN\_DR\_14](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a1ad3be15c2e60d0bb2f3c12faf279efa) , [LORAWAN\_DR\_15](group__lorawan__api.md#gga276e66fb8ce88f853d1987686e31fc86a4738baf87e0cb2e64d9c525e40dd6e0a)   } |
|  | LoRaWAN datarate types. [More...](group__lorawan__api.md#ga276e66fb8ce88f853d1987686e31fc86) |
| enum | [lorawan\_region](group__lorawan__api.md#gacb8efaa0761f8761146a0e913dcb627d) {     [LORAWAN\_REGION\_AS923](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da6a1ba05859d575a28095437436c8e6a6) , [LORAWAN\_REGION\_AU915](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da2744fe63701f5a5f23706b6f37672c70) , [LORAWAN\_REGION\_CN470](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da52d67181588c94d2a423040b4b5a1de4) , [LORAWAN\_REGION\_CN779](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627dadb106a189c4c647e5e3af89cc753e0d8) ,     [LORAWAN\_REGION\_EU433](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627dabcb9529d8f449bcb85a893fdd20f9180) , [LORAWAN\_REGION\_EU868](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da404530e5008260260131de051283f7ba) , [LORAWAN\_REGION\_KR920](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627dafae64ea9dd2c2ee7e897fc0f94484da5) , [LORAWAN\_REGION\_IN865](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da9113b34d94da40149442f432fd97e86c) ,     [LORAWAN\_REGION\_US915](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627da70e25dd006efc115617631f64cc34c88) , [LORAWAN\_REGION\_RU864](group__lorawan__api.md#ggacb8efaa0761f8761146a0e913dcb627dad30a636d45def6889e2b5cbf60f28c0e)   } |
|  | LoRaWAN region types. [More...](group__lorawan__api.md#gacb8efaa0761f8761146a0e913dcb627d) |
| enum | [lorawan\_message\_type](group__lorawan__api.md#ga5d78efba3f8e62ccd6317aed8af4bc54) { [LORAWAN\_MSG\_UNCONFIRMED](group__lorawan__api.md#gga5d78efba3f8e62ccd6317aed8af4bc54a9855d8332363a554db9dde446cc409b7) = 0 , [LORAWAN\_MSG\_CONFIRMED](group__lorawan__api.md#gga5d78efba3f8e62ccd6317aed8af4bc54a40ee76ac8d0b40d06903fc06a7ef1989) } |
|  | LoRaWAN message types. [More...](group__lorawan__api.md#ga5d78efba3f8e62ccd6317aed8af4bc54) |
| enum | [lorawan\_dl\_flags](group__lorawan__api.md#gab28a9f22482069b2246892e4ee31660d) { [LORAWAN\_DATA\_PENDING](group__lorawan__api.md#ggab28a9f22482069b2246892e4ee31660da01aee480c4308ac7abb6bf909478cce2) = BIT(0) , [LORAWAN\_TIME\_UPDATED](group__lorawan__api.md#ggab28a9f22482069b2246892e4ee31660dad272f787e193c2397e1b670ced4ba1b8) = BIT(1) } |
|  | LoRaWAN downlink flags. [More...](group__lorawan__api.md#gab28a9f22482069b2246892e4ee31660d) |

| Functions | |
| --- | --- |
| void | [lorawan\_register\_battery\_level\_callback](group__lorawan__api.md#ga9771704a8bcab778dd30653a0fbdeb2f) ([lorawan\_battery\_level\_cb\_t](group__lorawan__api.md#ga17a7a2e1dbfa19b9f7e18a81be5514dd) cb) |
|  | Register a battery level callback function. |
| void | [lorawan\_register\_downlink\_callback](group__lorawan__api.md#gab91f31477cd44e10692ca9d56d137ae2) (struct [lorawan\_downlink\_cb](structlorawan__downlink__cb.md) \*cb) |
|  | Register a callback to be run on downlink packets. |
| void | [lorawan\_register\_dr\_changed\_callback](group__lorawan__api.md#ga505e8d27bc7bc029feb93bbe4982d329) ([lorawan\_dr\_changed\_cb\_t](group__lorawan__api.md#ga87a8d911f1c825bcf8c77ada568f3ed4) cb) |
|  | Register a callback to be called when the datarate changes. |
| int | [lorawan\_join](group__lorawan__api.md#ga5b2c7543c45801c9d0d7f46546771f17) (const struct [lorawan\_join\_config](structlorawan__join__config.md) \*config) |
|  | Join the LoRaWAN network. |
| int | [lorawan\_start](group__lorawan__api.md#ga640d93930e09327ee87563597f919725) (void) |
|  | Start the LoRaWAN stack. |
| int | [lorawan\_send](group__lorawan__api.md#ga23758c3225e3ebf62bbe91b7589b67d7) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) port, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len, enum [lorawan\_message\_type](group__lorawan__api.md#ga5d78efba3f8e62ccd6317aed8af4bc54) type) |
|  | Send data to the LoRaWAN network. |
| int | [lorawan\_set\_class](group__lorawan__api.md#gab9768bad8d0c18410f6b8e946e89cbbe) (enum [lorawan\_class](group__lorawan__api.md#ga88b65799c3f1d98fbce80927218c0837) dev\_class) |
|  | Set the current device class. |
| int | [lorawan\_set\_conf\_msg\_tries](group__lorawan__api.md#ga14f9cb6a11c585f9ac4e9986735a82c3) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tries) |
|  | Set the number of tries used for transmissions. |
| void | [lorawan\_enable\_adr](group__lorawan__api.md#ga432929bd5911e04e57ef178b65e1beaa) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable Adaptive Data Rate (ADR). |
| int | [lorawan\_set\_channels\_mask](group__lorawan__api.md#ga243c3200693ae9c81dea238068afc7dd) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*channels\_mask, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) channels\_mask\_size) |
|  | Set the channels mask. |
| int | [lorawan\_set\_datarate](group__lorawan__api.md#gaaa70ba5aa545b59233bc906948a4030d) (enum [lorawan\_datarate](group__lorawan__api.md#ga276e66fb8ce88f853d1987686e31fc86) dr) |
|  | Set the default data rate. |
| enum [lorawan\_datarate](group__lorawan__api.md#ga276e66fb8ce88f853d1987686e31fc86) | [lorawan\_get\_min\_datarate](group__lorawan__api.md#ga6d1b45c5543473ff4fbcef473a8e0e35) (void) |
|  | Get the minimum possible datarate. |
| void | [lorawan\_get\_payload\_sizes](group__lorawan__api.md#ga94e3c282537618efae65e8ada1f88e81) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*max\_next\_payload\_size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*max\_payload\_size) |
|  | Get the current payload sizes. |
| int | [lorawan\_set\_region](group__lorawan__api.md#gaaf60e8b09d6f8d3a89aa2089c137fd3f) (enum [lorawan\_region](group__lorawan__api.md#gacb8efaa0761f8761146a0e913dcb627d) region) |
|  | Set the region and frequency to be used. |
| int | [lorawan\_request\_device\_time](group__lorawan__api.md#ga980f1650e9cceba19da453d4937273cb) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) force\_request) |
|  | Request for time according to DeviceTimeReq MAC cmd. |
| int | [lorawan\_device\_time\_get](group__lorawan__api.md#ga88c22a7e83437688039c05f9c7c1e7d4) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*gps\_time) |
|  | Retrieve the current time from LoRaWAN stack updated by DeviceTimeAns on MAC layer. |

## Detailed Description

Public LoRaWAN APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [lorawan](dir_025fd8c7c9e823719407606758d0c447.md)
- [lorawan.h](lorawan_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
