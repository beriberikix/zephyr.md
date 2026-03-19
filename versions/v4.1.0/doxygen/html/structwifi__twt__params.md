---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structwifi__twt__params.html
original_path: doxygen/html/structwifi__twt__params.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_twt\_params Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi TWT parameters.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| enum [wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3) | [operation](#a6f0483861a387651c9c89ba182e064bd) |
|  | TWT operation, see enum [wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3 "Wi-Fi Target Wake Time (TWT) operations."). |
| enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) | [negotiation\_type](#a5fd269328f68838b8a7e3a0b93eed894) |
|  | TWT negotiation type, see enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8 "Wi-Fi Target Wake Time (TWT) negotiation types."). |
| enum [wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022) | [setup\_cmd](#a347f8cff73ee6b6ba6d15ddf6f376a2d) |
|  | TWT setup command, see enum [wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022 "Wi-Fi Target Wake Time (TWT) setup commands."). |
| enum [wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a) | [resp\_status](#a805a23284ed4afa46b84efcd43329beb) |
|  | TWT setup response status, see enum [wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a "Wi-Fi Target Wake Time (TWT) negotiation status."). |
| enum [wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989) | [teardown\_status](#a9faff59e577775b3fe53f2139462ac71) |
|  | TWT teardown cmd status, see enum [wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989 "Wi-Fi Target Wake Time (TWT) teradown status."). |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [dialog\_token](#adda47e302a87a766f18e28016963a561) |
|  | Dialog token, used to map requests to responses. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flow\_id](#a95ec4b32d37309efa47256ae1ea865da) |
|  | Flow ID, used to map setup with teardown. |
| union { |  |
| struct { |  |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)   [twt\_interval](#ab92fe571559fcd5d97cdf7e6b7d86681) |  |
|  | Interval = Wake up time + Sleeping time. [More...](#ab92fe571559fcd5d97cdf7e6b7d86681) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [responder](#ae547c6fc1c7cbad15bebcfdaa43f59e7) |  |
|  | Requestor or responder. [More...](#ae547c6fc1c7cbad15bebcfdaa43f59e7) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [trigger](#a4e822c04b52fe6a9489e48e26b8f9382) |  |
|  | Trigger enabled or disabled. [More...](#a4e822c04b52fe6a9489e48e26b8f9382) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [implicit](#a8ea1e2501c8b69dc3fa606eb360f8678) |  |
|  | Implicit or explicit. [More...](#a8ea1e2501c8b69dc3fa606eb360f8678) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [announce](#a02f2d822d530e5376f256503439a54f9) |  |
|  | Announced or unannounced. [More...](#a02f2d822d530e5376f256503439a54f9) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [twt\_wake\_interval](#a7c297459a17ed2fd232c62cca63e952f) |  |
|  | Wake up time. [More...](#a7c297459a17ed2fd232c62cca63e952f) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)   [twt\_wake\_ahead\_duration](#a6f907ca412251fdd7391f29bfa6d7713) |  |
|  | Wake ahead notification is sent earlier than TWT Service period (SP) start based on this duration. [More...](#a6f907ca412251fdd7391f29bfa6d7713) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [twt\_info\_disable](#ac02eab9593b1ec2c9a0453a67076df88) |  |
|  | TWT info enabled or disable. [More...](#ac02eab9593b1ec2c9a0453a67076df88) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [twt\_exponent](#aabb77296f007cb055f78fa1ec3d155a3) |  |
|  | TWT exponent. [More...](#aabb77296f007cb055f78fa1ec3d155a3) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [twt\_mantissa](#aadad4556e2e5405b0703ebb4233a4d17) |  |
|  | TWT Mantissa Range: [0-sizeof(UINT16)]. [More...](#aadad4556e2e5405b0703ebb4233a4d17) |
| }   [setup](#aee57c0189b210cfcc18e213e35b9479c) |
|  | Setup specific parameters. [More...](#aee57c0189b210cfcc18e213e35b9479c) |
| struct { |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [sub\_id](#acc7234fa321938e48dd9be23b4bcbade) |  |
|  | Broadcast TWT AP config. [More...](#acc7234fa321938e48dd9be23b4bcbade) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [nominal\_wake](#a91637cecaa940422b08a40f4b830a3d2) |  |
|  | Range 64-255. [More...](#a91637cecaa940422b08a40f4b830a3d2) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [max\_sta\_support](#a1de9544f9bfd441df166ba2413cf11c3) |  |
|  | Max STA support. [More...](#a1de9544f9bfd441df166ba2413cf11c3) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [twt\_mantissa](#aadad4556e2e5405b0703ebb4233a4d17) |  |
|  | TWT mantissa. [More...](#aadad4556e2e5405b0703ebb4233a4d17) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [twt\_offset](#a22323b963a01399f26bb02aa95975728) |  |
|  | TWT offset. [More...](#a22323b963a01399f26bb02aa95975728) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [twt\_exponent](#aabb77296f007cb055f78fa1ec3d155a3) |  |
|  | TWT exponent. [More...](#aabb77296f007cb055f78fa1ec3d155a3) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [sp\_gap](#ada6919e0b201cec5f2c97eeaab46bec7) |  |
|  | SP gap. [More...](#ada6919e0b201cec5f2c97eeaab46bec7) |
| }   [btwt](#a72ab809144b1dd3e7e121e489ef399e2) |
|  | Setup specific parameters. [More...](#a72ab809144b1dd3e7e121e489ef399e2) |
| struct { |  |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)   [teardown\_all](#a26d6bda00452f77832f69f4465c13efb) |  |
|  | Teardown all flows. [More...](#a26d6bda00452f77832f69f4465c13efb) |
| }   [teardown](#aadf62f6386359ad15491d0073c9065bf) |
|  | Teardown specific parameters. [More...](#aadf62f6386359ad15491d0073c9065bf) |
| }; |  |
| enum [wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6) | [fail\_reason](#a70f58b502bb67ef3b2068ded2160b612) |
|  | TWT fail reason, see enum [wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6 "Target Wake Time (TWT) error codes."). |

## Detailed Description

Wi-Fi TWT parameters.

## Field Documentation

## [◆ ](#ae3a691d30d5d5bd54ba9d4d0efc51923)[union]

| union { ... } [wifi\_twt\_params](structwifi__twt__params.md) |
| --- |

## [◆ ](#a02f2d822d530e5376f256503439a54f9)announce

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_twt\_params::announce |
| --- |

Announced or unannounced.

## [◆ ](#a72ab809144b1dd3e7e121e489ef399e2)[struct]

| struct { ... } wifi\_twt\_params::btwt |
| --- |

Setup specific parameters.

## [◆ ](#adda47e302a87a766f18e28016963a561)dialog\_token

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_twt\_params::dialog\_token |
| --- |

Dialog token, used to map requests to responses.

## [◆ ](#a70f58b502bb67ef3b2068ded2160b612)fail\_reason

| enum [wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6) wifi\_twt\_params::fail\_reason |
| --- |

TWT fail reason, see enum [wifi\_twt\_fail\_reason](group__wifi__mgmt.md#ga97fa304f9a1db2294a93cccd4c93bcf6 "Target Wake Time (TWT) error codes.").

## [◆ ](#a95ec4b32d37309efa47256ae1ea865da)flow\_id

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_twt\_params::flow\_id |
| --- |

Flow ID, used to map setup with teardown.

## [◆ ](#a8ea1e2501c8b69dc3fa606eb360f8678)implicit

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_twt\_params::implicit |
| --- |

Implicit or explicit.

## [◆ ](#a1de9544f9bfd441df166ba2413cf11c3)max\_sta\_support

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_twt\_params::max\_sta\_support |
| --- |

Max STA support.

## [◆ ](#a5fd269328f68838b8a7e3a0b93eed894)negotiation\_type

| enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8) wifi\_twt\_params::negotiation\_type |
| --- |

TWT negotiation type, see enum [wifi\_twt\_negotiation\_type](group__wifi__mgmt.md#ga695123cd534e2499f516a07fdc5cafa8 "Wi-Fi Target Wake Time (TWT) negotiation types.").

## [◆ ](#a91637cecaa940422b08a40f4b830a3d2)nominal\_wake

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_twt\_params::nominal\_wake |
| --- |

Range 64-255.

## [◆ ](#a6f0483861a387651c9c89ba182e064bd)operation

| enum [wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3) wifi\_twt\_params::operation |
| --- |

TWT operation, see enum [wifi\_twt\_operation](group__wifi__mgmt.md#gad0e998aeb1b27c4f203ca76339d323a3 "Wi-Fi Target Wake Time (TWT) operations.").

## [◆ ](#a805a23284ed4afa46b84efcd43329beb)resp\_status

| enum [wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a) wifi\_twt\_params::resp\_status |
| --- |

TWT setup response status, see enum [wifi\_twt\_setup\_resp\_status](group__wifi__mgmt.md#ga4d03aedac13ee4512d7717ac624f319a "Wi-Fi Target Wake Time (TWT) negotiation status.").

## [◆ ](#ae547c6fc1c7cbad15bebcfdaa43f59e7)responder

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_twt\_params::responder |
| --- |

Requestor or responder.

## [◆ ](#aee57c0189b210cfcc18e213e35b9479c)[struct]

| struct { ... } wifi\_twt\_params::setup |
| --- |

Setup specific parameters.

## [◆ ](#a347f8cff73ee6b6ba6d15ddf6f376a2d)setup\_cmd

| enum [wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022) wifi\_twt\_params::setup\_cmd |
| --- |

TWT setup command, see enum [wifi\_twt\_setup\_cmd](group__wifi__mgmt.md#ga31c78afc89bfdc4b54cee177843f8022 "Wi-Fi Target Wake Time (TWT) setup commands.").

## [◆ ](#ada6919e0b201cec5f2c97eeaab46bec7)sp\_gap

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_twt\_params::sp\_gap |
| --- |

SP gap.

## [◆ ](#acc7234fa321938e48dd9be23b4bcbade)sub\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) wifi\_twt\_params::sub\_id |
| --- |

Broadcast TWT AP config.

## [◆ ](#aadf62f6386359ad15491d0073c9065bf)[struct]

| struct { ... } wifi\_twt\_params::teardown |
| --- |

Teardown specific parameters.

## [◆ ](#a26d6bda00452f77832f69f4465c13efb)teardown\_all

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_twt\_params::teardown\_all |
| --- |

Teardown all flows.

## [◆ ](#a9faff59e577775b3fe53f2139462ac71)teardown\_status

| enum [wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989) wifi\_twt\_params::teardown\_status |
| --- |

TWT teardown cmd status, see enum [wifi\_twt\_teardown\_status](group__wifi__mgmt.md#gad3709d07aaa3ed59b48f9dd7bd181989 "Wi-Fi Target Wake Time (TWT) teradown status.").

## [◆ ](#a4e822c04b52fe6a9489e48e26b8f9382)trigger

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_twt\_params::trigger |
| --- |

Trigger enabled or disabled.

## [◆ ](#aabb77296f007cb055f78fa1ec3d155a3)twt\_exponent

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wifi\_twt\_params::twt\_exponent |
| --- |

TWT exponent.

## [◆ ](#ac02eab9593b1ec2c9a0453a67076df88)twt\_info\_disable

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_twt\_params::twt\_info\_disable |
| --- |

TWT info enabled or disable.

## [◆ ](#ab92fe571559fcd5d97cdf7e6b7d86681)twt\_interval

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) wifi\_twt\_params::twt\_interval |
| --- |

Interval = Wake up time + Sleeping time.

## [◆ ](#aadad4556e2e5405b0703ebb4233a4d17)twt\_mantissa

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) wifi\_twt\_params::twt\_mantissa |
| --- |

TWT Mantissa Range: [0-sizeof(UINT16)].

TWT mantissa.

## [◆ ](#a22323b963a01399f26bb02aa95975728)twt\_offset

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) wifi\_twt\_params::twt\_offset |
| --- |

TWT offset.

## [◆ ](#a6f907ca412251fdd7391f29bfa6d7713)twt\_wake\_ahead\_duration

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wifi\_twt\_params::twt\_wake\_ahead\_duration |
| --- |

Wake ahead notification is sent earlier than TWT Service period (SP) start based on this duration.

This should give applications ample time to prepare the data before TWT SP starts.

## [◆ ](#a7c297459a17ed2fd232c62cca63e952f)twt\_wake\_interval

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) wifi\_twt\_params::twt\_wake\_interval |
| --- |

Wake up time.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_twt\_params](structwifi__twt__params.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
