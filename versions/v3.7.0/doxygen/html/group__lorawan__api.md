---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__lorawan__api.html
original_path: doxygen/html/group__lorawan__api.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

LoRaWAN APIs

[Connectivity](group__connectivity.md)

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
| #define | [LW\_RECV\_PORT\_ANY](#ga83dbf2575eaae85f1837567e9fb729a4)   [UINT16\_MAX](stdint_8h.md#a3ea490c9b3617d4479bd80ef93cd5602) |
|  | Flag to indicate receiving on any port. |

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [lorawan\_battery\_level\_cb\_t](#ga17a7a2e1dbfa19b9f7e18a81be5514dd)) (void) |
|  | Defines the battery level callback handler function signature. |
| typedef void(\* | [lorawan\_dr\_changed\_cb\_t](#ga87a8d911f1c825bcf8c77ada568f3ed4)) (enum [lorawan\_datarate](#ga276e66fb8ce88f853d1987686e31fc86) dr) |
|  | Defines the datarate changed callback handler function signature. |

| Enumerations | |
| --- | --- |
| enum | [lorawan\_class](#ga88b65799c3f1d98fbce80927218c0837) { [LORAWAN\_CLASS\_A](#gga88b65799c3f1d98fbce80927218c0837a538e56348e6d5b506e661e3af18aee6c) = 0x00 , [LORAWAN\_CLASS\_B](#gga88b65799c3f1d98fbce80927218c0837a79a9c205ac583051b2e072389491c7cb) = 0x01 , [LORAWAN\_CLASS\_C](#gga88b65799c3f1d98fbce80927218c0837ad158a1985688bbe54b20a8a808774547) = 0x02 } |
|  | LoRaWAN class types. [More...](#ga88b65799c3f1d98fbce80927218c0837) |
| enum | [lorawan\_act\_type](#ga2bf50442214ecdc717f1a24dc058a338) { [LORAWAN\_ACT\_OTAA](#gga2bf50442214ecdc717f1a24dc058a338a5f262e334bc46278bec491cd022b612a) = 0 , [LORAWAN\_ACT\_ABP](#gga2bf50442214ecdc717f1a24dc058a338a13bb2a28232081844e36308977ec6701) } |
|  | LoRaWAN activation types. [More...](#ga2bf50442214ecdc717f1a24dc058a338) |
| enum | [lorawan\_channels\_mask\_size](#ga0635d19612db9009775eae8e527d4897) {     [LORAWAN\_CHANNELS\_MASK\_SIZE\_AS923](#gga0635d19612db9009775eae8e527d4897a577c304c4c1998916203e9ec7ae6e1be) = 1 , [LORAWAN\_CHANNELS\_MASK\_SIZE\_AU915](#gga0635d19612db9009775eae8e527d4897a1bc4cacfd02a630226f629ed61f4e1ca) = 6 , [LORAWAN\_CHANNELS\_MASK\_SIZE\_CN470](#gga0635d19612db9009775eae8e527d4897a2bdaecd6f1f853cd370ba89b465a9ee1) = 6 , [LORAWAN\_CHANNELS\_MASK\_SIZE\_CN779](#gga0635d19612db9009775eae8e527d4897a8f2f25b3ab1167f69aa594a034b27180) = 1 ,     [LORAWAN\_CHANNELS\_MASK\_SIZE\_EU433](#gga0635d19612db9009775eae8e527d4897a3b7968012bf2c8fa7adef454fc33124a) = 1 , [LORAWAN\_CHANNELS\_MASK\_SIZE\_EU868](#gga0635d19612db9009775eae8e527d4897a3bc215c41b7fb5652c6729756b8f979a) = 1 , [LORAWAN\_CHANNELS\_MASK\_SIZE\_KR920](#gga0635d19612db9009775eae8e527d4897a7443e6adbaaf4f7cb2037d8f3e42d86a) = 1 , [LORAWAN\_CHANNELS\_MASK\_SIZE\_IN865](#gga0635d19612db9009775eae8e527d4897a9564d246e39448f478412861a3a87b7e) = 1 ,     [LORAWAN\_CHANNELS\_MASK\_SIZE\_US915](#gga0635d19612db9009775eae8e527d4897a054ebab376354c8a9e6a5f4e9f6f78ee) = 6 , [LORAWAN\_CHANNELS\_MASK\_SIZE\_RU864](#gga0635d19612db9009775eae8e527d4897aaa05e08a24aded2ada511fd2d1f4cebd) = 1   } |
|  | LoRaWAN channels mask sizes. [More...](#ga0635d19612db9009775eae8e527d4897) |
| enum | [lorawan\_datarate](#ga276e66fb8ce88f853d1987686e31fc86) {     [LORAWAN\_DR\_0](#gga276e66fb8ce88f853d1987686e31fc86a4b60b8eb52c07b40cbaaf94a4c56e1f6) = 0 , [LORAWAN\_DR\_1](#gga276e66fb8ce88f853d1987686e31fc86ade4655b32ca976c317fa9f44ac8b148a) , [LORAWAN\_DR\_2](#gga276e66fb8ce88f853d1987686e31fc86a941f8a603aeb54560be7125a55c74159) , [LORAWAN\_DR\_3](#gga276e66fb8ce88f853d1987686e31fc86a4ac565dbaae0c6ad4e62dc34ca0c013a) ,     [LORAWAN\_DR\_4](#gga276e66fb8ce88f853d1987686e31fc86a6f6cd4ecd247f67cad08ede84649a939) , [LORAWAN\_DR\_5](#gga276e66fb8ce88f853d1987686e31fc86a08f879f1054ca54e488180b07d7ff952) , [LORAWAN\_DR\_6](#gga276e66fb8ce88f853d1987686e31fc86acc624ccf8a9585889c3685217f56099f) , [LORAWAN\_DR\_7](#gga276e66fb8ce88f853d1987686e31fc86aac8afba95d7187f0829aae7abda894d5) ,     [LORAWAN\_DR\_8](#gga276e66fb8ce88f853d1987686e31fc86a080b31031f5a2b54d84ed49b133b0a86) , [LORAWAN\_DR\_9](#gga276e66fb8ce88f853d1987686e31fc86afbc8d04236410a6107cccfd71ba4bace) , [LORAWAN\_DR\_10](#gga276e66fb8ce88f853d1987686e31fc86a0a18193e15d268d262d58897d39993b3) , [LORAWAN\_DR\_11](#gga276e66fb8ce88f853d1987686e31fc86a2a631e746ffc5c4378e39b7a90dd44e2) ,     [LORAWAN\_DR\_12](#gga276e66fb8ce88f853d1987686e31fc86a0df057cf1505ba94876deaeddd515548) , [LORAWAN\_DR\_13](#gga276e66fb8ce88f853d1987686e31fc86a18bfd63ae262f992d9d12f8d56cc217e) , [LORAWAN\_DR\_14](#gga276e66fb8ce88f853d1987686e31fc86a1ad3be15c2e60d0bb2f3c12faf279efa) , [LORAWAN\_DR\_15](#gga276e66fb8ce88f853d1987686e31fc86a4738baf87e0cb2e64d9c525e40dd6e0a)   } |
|  | LoRaWAN datarate types. [More...](#ga276e66fb8ce88f853d1987686e31fc86) |
| enum | [lorawan\_region](#gacb8efaa0761f8761146a0e913dcb627d) {     [LORAWAN\_REGION\_AS923](#ggacb8efaa0761f8761146a0e913dcb627da6a1ba05859d575a28095437436c8e6a6) , [LORAWAN\_REGION\_AU915](#ggacb8efaa0761f8761146a0e913dcb627da2744fe63701f5a5f23706b6f37672c70) , [LORAWAN\_REGION\_CN470](#ggacb8efaa0761f8761146a0e913dcb627da52d67181588c94d2a423040b4b5a1de4) , [LORAWAN\_REGION\_CN779](#ggacb8efaa0761f8761146a0e913dcb627dadb106a189c4c647e5e3af89cc753e0d8) ,     [LORAWAN\_REGION\_EU433](#ggacb8efaa0761f8761146a0e913dcb627dabcb9529d8f449bcb85a893fdd20f9180) , [LORAWAN\_REGION\_EU868](#ggacb8efaa0761f8761146a0e913dcb627da404530e5008260260131de051283f7ba) , [LORAWAN\_REGION\_KR920](#ggacb8efaa0761f8761146a0e913dcb627dafae64ea9dd2c2ee7e897fc0f94484da5) , [LORAWAN\_REGION\_IN865](#ggacb8efaa0761f8761146a0e913dcb627da9113b34d94da40149442f432fd97e86c) ,     [LORAWAN\_REGION\_US915](#ggacb8efaa0761f8761146a0e913dcb627da70e25dd006efc115617631f64cc34c88) , [LORAWAN\_REGION\_RU864](#ggacb8efaa0761f8761146a0e913dcb627dad30a636d45def6889e2b5cbf60f28c0e)   } |
|  | LoRaWAN region types. [More...](#gacb8efaa0761f8761146a0e913dcb627d) |
| enum | [lorawan\_message\_type](#ga5d78efba3f8e62ccd6317aed8af4bc54) { [LORAWAN\_MSG\_UNCONFIRMED](#gga5d78efba3f8e62ccd6317aed8af4bc54a9855d8332363a554db9dde446cc409b7) = 0 , [LORAWAN\_MSG\_CONFIRMED](#gga5d78efba3f8e62ccd6317aed8af4bc54a40ee76ac8d0b40d06903fc06a7ef1989) } |
|  | LoRaWAN message types. [More...](#ga5d78efba3f8e62ccd6317aed8af4bc54) |

| Functions | |
| --- | --- |
| void | [lorawan\_register\_battery\_level\_callback](#ga9771704a8bcab778dd30653a0fbdeb2f) ([lorawan\_battery\_level\_cb\_t](#ga17a7a2e1dbfa19b9f7e18a81be5514dd) cb) |
|  | Register a battery level callback function. |
| void | [lorawan\_register\_downlink\_callback](#gab91f31477cd44e10692ca9d56d137ae2) (struct [lorawan\_downlink\_cb](structlorawan__downlink__cb.md) \*cb) |
|  | Register a callback to be run on downlink packets. |
| void | [lorawan\_register\_dr\_changed\_callback](#ga505e8d27bc7bc029feb93bbe4982d329) ([lorawan\_dr\_changed\_cb\_t](#ga87a8d911f1c825bcf8c77ada568f3ed4) cb) |
|  | Register a callback to be called when the datarate changes. |
| int | [lorawan\_join](#ga5b2c7543c45801c9d0d7f46546771f17) (const struct [lorawan\_join\_config](structlorawan__join__config.md) \*config) |
|  | Join the LoRaWAN network. |
| int | [lorawan\_start](#ga640d93930e09327ee87563597f919725) (void) |
|  | Start the LoRaWAN stack. |
| int | [lorawan\_send](#ga23758c3225e3ebf62bbe91b7589b67d7) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) port, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len, enum [lorawan\_message\_type](#ga5d78efba3f8e62ccd6317aed8af4bc54) type) |
|  | Send data to the LoRaWAN network. |
| int | [lorawan\_set\_class](#gab9768bad8d0c18410f6b8e946e89cbbe) (enum [lorawan\_class](#ga88b65799c3f1d98fbce80927218c0837) dev\_class) |
|  | Set the current device class. |
| int | [lorawan\_set\_conf\_msg\_tries](#ga14f9cb6a11c585f9ac4e9986735a82c3) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tries) |
|  | Set the number of tries used for transmissions. |
| void | [lorawan\_enable\_adr](#ga432929bd5911e04e57ef178b65e1beaa) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Enable Adaptive Data Rate (ADR). |
| int | [lorawan\_set\_channels\_mask](#ga243c3200693ae9c81dea238068afc7dd) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*channels\_mask, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) channels\_mask\_size) |
|  | Set the channels mask. |
| int | [lorawan\_set\_datarate](#gaaa70ba5aa545b59233bc906948a4030d) (enum [lorawan\_datarate](#ga276e66fb8ce88f853d1987686e31fc86) dr) |
|  | Set the default data rate. |
| enum [lorawan\_datarate](#ga276e66fb8ce88f853d1987686e31fc86) | [lorawan\_get\_min\_datarate](#ga6d1b45c5543473ff4fbcef473a8e0e35) (void) |
|  | Get the minimum possible datarate. |
| void | [lorawan\_get\_payload\_sizes](#ga94e3c282537618efae65e8ada1f88e81) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*max\_next\_payload\_size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*max\_payload\_size) |
|  | Get the current payload sizes. |
| int | [lorawan\_set\_region](#gaaf60e8b09d6f8d3a89aa2089c137fd3f) (enum [lorawan\_region](#gacb8efaa0761f8761146a0e913dcb627d) region) |
|  | Set the region and frequency to be used. |

## Detailed Description

Since
:   2.5

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga83dbf2575eaae85f1837567e9fb729a4)LW\_RECV\_PORT\_ANY

| #define LW\_RECV\_PORT\_ANY   [UINT16\_MAX](stdint_8h.md#a3ea490c9b3617d4479bd80ef93cd5602) |
| --- |

`#include <[lorawan.h](lorawan_8h.md)>`

Flag to indicate receiving on any port.

## Typedef Documentation

## [◆ ](#ga17a7a2e1dbfa19b9f7e18a81be5514dd)lorawan\_battery\_level\_cb\_t

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* lorawan\_battery\_level\_cb\_t) (void) |
| --- |

`#include <[lorawan.h](lorawan_8h.md)>`

Defines the battery level callback handler function signature.

Return values
:   | 0 | if the node is connected to an external power source |
    | --- | --- |
    | 1..254 | battery level, where 1 is the minimum and 254 is the maximum value |
    | 255 | if the node was not able to measure the battery level |

## [◆ ](#ga87a8d911f1c825bcf8c77ada568f3ed4)lorawan\_dr\_changed\_cb\_t

| typedef void(\* lorawan\_dr\_changed\_cb\_t) (enum [lorawan\_datarate](#ga276e66fb8ce88f853d1987686e31fc86) dr) |
| --- |

`#include <[lorawan.h](lorawan_8h.md)>`

Defines the datarate changed callback handler function signature.

Parameters
:   | dr | Updated datarate. |
    | --- | --- |

## Enumeration Type Documentation

## [◆ ](#ga2bf50442214ecdc717f1a24dc058a338)lorawan\_act\_type

| enum [lorawan\_act\_type](#ga2bf50442214ecdc717f1a24dc058a338) |
| --- |

`#include <[lorawan.h](lorawan_8h.md)>`

LoRaWAN activation types.

| Enumerator | |
| --- | --- |
| LORAWAN\_ACT\_OTAA | Over-the-Air Activation (OTAA). |
| LORAWAN\_ACT\_ABP | Activation by Personalization (ABP). |

## [◆ ](#ga0635d19612db9009775eae8e527d4897)lorawan\_channels\_mask\_size

| enum [lorawan\_channels\_mask\_size](#ga0635d19612db9009775eae8e527d4897) |
| --- |

`#include <[lorawan.h](lorawan_8h.md)>`

LoRaWAN channels mask sizes.

| Enumerator | |
| --- | --- |
| LORAWAN\_CHANNELS\_MASK\_SIZE\_AS923 | Region AS923 mask size. |
| LORAWAN\_CHANNELS\_MASK\_SIZE\_AU915 | Region AU915 mask size. |
| LORAWAN\_CHANNELS\_MASK\_SIZE\_CN470 | Region CN470 mask size. |
| LORAWAN\_CHANNELS\_MASK\_SIZE\_CN779 | Region CN779 mask size. |
| LORAWAN\_CHANNELS\_MASK\_SIZE\_EU433 | Region EU433 mask size. |
| LORAWAN\_CHANNELS\_MASK\_SIZE\_EU868 | Region EU868 mask size. |
| LORAWAN\_CHANNELS\_MASK\_SIZE\_KR920 | Region KR920 mask size. |
| LORAWAN\_CHANNELS\_MASK\_SIZE\_IN865 | Region IN865 mask size. |
| LORAWAN\_CHANNELS\_MASK\_SIZE\_US915 | Region US915 mask size. |
| LORAWAN\_CHANNELS\_MASK\_SIZE\_RU864 | Region RU864 mask size. |

## [◆ ](#ga88b65799c3f1d98fbce80927218c0837)lorawan\_class

| enum [lorawan\_class](#ga88b65799c3f1d98fbce80927218c0837) |
| --- |

`#include <[lorawan.h](lorawan_8h.md)>`

LoRaWAN class types.

| Enumerator | |
| --- | --- |
| LORAWAN\_CLASS\_A | Class A device. |
| LORAWAN\_CLASS\_B | Class B device. |
| LORAWAN\_CLASS\_C | Class C device. |

## [◆ ](#ga276e66fb8ce88f853d1987686e31fc86)lorawan\_datarate

| enum [lorawan\_datarate](#ga276e66fb8ce88f853d1987686e31fc86) |
| --- |

`#include <[lorawan.h](lorawan_8h.md)>`

LoRaWAN datarate types.

| Enumerator | |
| --- | --- |
| LORAWAN\_DR\_0 | DR0 data rate. |
| LORAWAN\_DR\_1 | DR1 data rate. |
| LORAWAN\_DR\_2 | DR2 data rate. |
| LORAWAN\_DR\_3 | DR3 data rate. |
| LORAWAN\_DR\_4 | DR4 data rate. |
| LORAWAN\_DR\_5 | DR5 data rate. |
| LORAWAN\_DR\_6 | DR6 data rate. |
| LORAWAN\_DR\_7 | DR7 data rate. |
| LORAWAN\_DR\_8 | DR8 data rate. |
| LORAWAN\_DR\_9 | DR9 data rate. |
| LORAWAN\_DR\_10 | DR10 data rate. |
| LORAWAN\_DR\_11 | DR11 data rate. |
| LORAWAN\_DR\_12 | DR12 data rate. |
| LORAWAN\_DR\_13 | DR13 data rate. |
| LORAWAN\_DR\_14 | DR14 data rate. |
| LORAWAN\_DR\_15 | DR15 data rate. |

## [◆ ](#ga5d78efba3f8e62ccd6317aed8af4bc54)lorawan\_message\_type

| enum [lorawan\_message\_type](#ga5d78efba3f8e62ccd6317aed8af4bc54) |
| --- |

`#include <[lorawan.h](lorawan_8h.md)>`

LoRaWAN message types.

| Enumerator | |
| --- | --- |
| LORAWAN\_MSG\_UNCONFIRMED | Unconfirmed message. |
| LORAWAN\_MSG\_CONFIRMED | Confirmed message. |

## [◆ ](#gacb8efaa0761f8761146a0e913dcb627d)lorawan\_region

| enum [lorawan\_region](#gacb8efaa0761f8761146a0e913dcb627d) |
| --- |

`#include <[lorawan.h](lorawan_8h.md)>`

LoRaWAN region types.

| Enumerator | |
| --- | --- |
| LORAWAN\_REGION\_AS923 | Asia 923 MHz frequency band. |
| LORAWAN\_REGION\_AU915 | Australia 915 MHz frequency band. |
| LORAWAN\_REGION\_CN470 | China 470 MHz frequency band. |
| LORAWAN\_REGION\_CN779 | China 779 MHz frequency band. |
| LORAWAN\_REGION\_EU433 | Europe 433 MHz frequency band. |
| LORAWAN\_REGION\_EU868 | Europe 868 MHz frequency band. |
| LORAWAN\_REGION\_KR920 | South Korea 920 MHz frequency band. |
| LORAWAN\_REGION\_IN865 | India 865 MHz frequency band. |
| LORAWAN\_REGION\_US915 | United States 915 MHz frequency band. |
| LORAWAN\_REGION\_RU864 | Russia 864 MHz frequency band. |

## Function Documentation

## [◆ ](#ga432929bd5911e04e57ef178b65e1beaa)lorawan\_enable\_adr()

| void lorawan\_enable\_adr | ( | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *enable* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lorawan.h](lorawan_8h.md)>`

Enable Adaptive Data Rate (ADR).

Control whether adaptive data rate (ADR) is enabled. When ADR is enabled, the data rate is treated as a default data rate that will be used if the ADR algorithm has not established a data rate. ADR should normally only be enabled for devices with stable RF conditions (i.e., devices in a mostly static location).

Parameters
:   | enable | Enable or Disable adaptive data rate. |
    | --- | --- |

## [◆ ](#ga6d1b45c5543473ff4fbcef473a8e0e35)lorawan\_get\_min\_datarate()

| enum [lorawan\_datarate](#ga276e66fb8ce88f853d1987686e31fc86) lorawan\_get\_min\_datarate | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lorawan.h](lorawan_8h.md)>`

Get the minimum possible datarate.

The minimum possible datarate may change in response to a TxParamSetupReq command from the network server.

Returns
:   Minimum possible data rate

## [◆ ](#ga94e3c282537618efae65e8ada1f88e81)lorawan\_get\_payload\_sizes()

| void lorawan\_get\_payload\_sizes | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *max\_next\_payload\_size*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *max\_payload\_size* ) |

`#include <[lorawan.h](lorawan_8h.md)>`

Get the current payload sizes.

Query the current payload sizes. The maximum payload size varies with datarate, while the current payload size can be less due to MAC layer commands which are inserted into uplink packets.

Parameters
:   | max\_next\_payload\_size | Maximum payload size for the next transmission |
    | --- | --- |
    | max\_payload\_size | Maximum payload size for this datarate |

## [◆ ](#ga5b2c7543c45801c9d0d7f46546771f17)lorawan\_join()

| int lorawan\_join | ( | const struct [lorawan\_join\_config](structlorawan__join__config.md) \* | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lorawan.h](lorawan_8h.md)>`

Join the LoRaWAN network.

Join the LoRaWAN network using OTAA or AWB.

Parameters
:   | config | Configuration to be used |
    | --- | --- |

Returns
:   0 if successful, negative errno code if failure

## [◆ ](#ga9771704a8bcab778dd30653a0fbdeb2f)lorawan\_register\_battery\_level\_callback()

| void lorawan\_register\_battery\_level\_callback | ( | [lorawan\_battery\_level\_cb\_t](#ga17a7a2e1dbfa19b9f7e18a81be5514dd) | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lorawan.h](lorawan_8h.md)>`

Register a battery level callback function.

Provide the LoRaWAN stack with a function to be called whenever a battery level needs to be read.

Should no callback be provided the lorawan backend will report 255.

Parameters
:   | cb | Pointer to the battery level function |
    | --- | --- |

## [◆ ](#gab91f31477cd44e10692ca9d56d137ae2)lorawan\_register\_downlink\_callback()

| void lorawan\_register\_downlink\_callback | ( | struct [lorawan\_downlink\_cb](structlorawan__downlink__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lorawan.h](lorawan_8h.md)>`

Register a callback to be run on downlink packets.

Parameters
:   | cb | Pointer to structure containing callback parameters |
    | --- | --- |

## [◆ ](#ga505e8d27bc7bc029feb93bbe4982d329)lorawan\_register\_dr\_changed\_callback()

| void lorawan\_register\_dr\_changed\_callback | ( | [lorawan\_dr\_changed\_cb\_t](#ga87a8d911f1c825bcf8c77ada568f3ed4) | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lorawan.h](lorawan_8h.md)>`

Register a callback to be called when the datarate changes.

The callback is called once upon successfully joining a network and again each time the datarate changes due to ADR.

Parameters
:   | cb | Pointer to datarate update callback |
    | --- | --- |

## [◆ ](#ga23758c3225e3ebf62bbe91b7589b67d7)lorawan\_send()

| int lorawan\_send | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *port*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *len*, |
|  |  | enum [lorawan\_message\_type](#ga5d78efba3f8e62ccd6317aed8af4bc54) | *type* ) |

`#include <[lorawan.h](lorawan_8h.md)>`

Send data to the LoRaWAN network.

Send data to the connected LoRaWAN network.

Parameters
:   | port | Port to be used for sending data. Must be set if the payload is not empty. |
    | --- | --- |
    | data | Data buffer to be sent |
    | len | Length of the buffer to be sent. Maximum length of this buffer is 255 bytes but the actual payload size varies with region and datarate. |
    | type | Specifies if the message shall be confirmed or unconfirmed. Must be one of [lorawan\_message\_type](#ga5d78efba3f8e62ccd6317aed8af4bc54). |

Returns
:   0 if successful, negative errno code if failure

## [◆ ](#ga243c3200693ae9c81dea238068afc7dd)lorawan\_set\_channels\_mask()

| int lorawan\_set\_channels\_mask | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *channels\_mask*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *channels\_mask\_size* ) |

`#include <[lorawan.h](lorawan_8h.md)>`

Set the channels mask.

Change the default channels mask. When mask is not changed, all the channels can be used for data transmission. Some Network Servers don't use all the channels, in this case, the channels mask must be provided.

Parameters
:   | channels\_mask | Buffer with channels mask to be used. |
    | --- | --- |
    | channels\_mask\_size | Size of channels mask buffer. |

Return values
:   | 0 | successful |
    | --- | --- |
    | -EINVAL | channels mask or channels mask size is wrong |

## [◆ ](#gab9768bad8d0c18410f6b8e946e89cbbe)lorawan\_set\_class()

| int lorawan\_set\_class | ( | enum [lorawan\_class](#ga88b65799c3f1d98fbce80927218c0837) | *dev\_class* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lorawan.h](lorawan_8h.md)>`

Set the current device class.

Change the current device class. This function may be called before or after a network connection has been established.

Parameters
:   | dev\_class | New device class |
    | --- | --- |

Returns
:   0 if successful, negative errno code if failure

## [◆ ](#ga14f9cb6a11c585f9ac4e9986735a82c3)lorawan\_set\_conf\_msg\_tries()

| int lorawan\_set\_conf\_msg\_tries | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *tries* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lorawan.h](lorawan_8h.md)>`

Set the number of tries used for transmissions.

Parameters
:   | tries | Number of tries to be used |
    | --- | --- |

Returns
:   0 if successful, negative errno code if failure

## [◆ ](#gaaa70ba5aa545b59233bc906948a4030d)lorawan\_set\_datarate()

| int lorawan\_set\_datarate | ( | enum [lorawan\_datarate](#ga276e66fb8ce88f853d1987686e31fc86) | *dr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lorawan.h](lorawan_8h.md)>`

Set the default data rate.

Change the default data rate.

Parameters
:   | dr | Data rate used for transmissions |
    | --- | --- |

Returns
:   0 if successful, negative errno code if failure

## [◆ ](#gaaf60e8b09d6f8d3a89aa2089c137fd3f)lorawan\_set\_region()

| int lorawan\_set\_region | ( | enum [lorawan\_region](#gacb8efaa0761f8761146a0e913dcb627d) | *region* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lorawan.h](lorawan_8h.md)>`

Set the region and frequency to be used.

Control the LoRa region and frequency settings. This should be called before *[lorawan\_start()](#ga640d93930e09327ee87563597f919725)*. If you only have support for a single region selected via Kconfig, this function does not need to be called at all.

Parameters
:   | region | The region to be selected |
    | --- | --- |

Returns
:   0 if successful, negative errno otherwise

## [◆ ](#ga640d93930e09327ee87563597f919725)lorawan\_start()

| int lorawan\_start | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[lorawan.h](lorawan_8h.md)>`

Start the LoRaWAN stack.

This function need to be called before joining the network.

Returns
:   0 if successful, negative errno code if failure

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
