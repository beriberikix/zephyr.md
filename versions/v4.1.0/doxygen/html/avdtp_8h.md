---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/avdtp_8h.html
original_path: doxygen/html/avdtp_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

avdtp.h File Reference

Audio/Video Distribution Transport Protocol header.
[More...](#details)

[Go to the source code of this file.](avdtp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_avdtp\_sep\_info](structbt__avdtp__sep__info.md) |
|  | AVDTP stream endpoint information. [More...](structbt__avdtp__sep__info.md#details) |
| struct | [bt\_avdtp\_sep](structbt__avdtp__sep.md) |
|  | AVDTP Stream End Point. [More...](structbt__avdtp__sep.md#details) |

| Enumerations | |
| --- | --- |
| enum | [bt\_avdtp\_err\_code](#affc7226c1b7795a3d2f51cb4ffaf6d21) {     [BT\_AVDTP\_SUCCESS](#affc7226c1b7795a3d2f51cb4ffaf6d21a15256eb00e75a0f4075a7bb93f3419af) = 0x00 , [BT\_AVDTP\_TIME\_OUT](#affc7226c1b7795a3d2f51cb4ffaf6d21a203030bcba53de65a3cee79a10f8e24a) = 0xFF , [BT\_AVDTP\_BAD\_HEADER\_FORMAT](#affc7226c1b7795a3d2f51cb4ffaf6d21a751370153f9c3f55ddce10b6353db49f) = 0x01 , [BT\_AVDTP\_BAD\_LENGTH](#affc7226c1b7795a3d2f51cb4ffaf6d21acb07c6cd131aa3bc77eb1cf32050c7e9) = 0x11 ,     [BT\_AVDTP\_BAD\_ACP\_SEID](#affc7226c1b7795a3d2f51cb4ffaf6d21accd5a3a315e7ebcb0da1364665494064) = 0x12 , [BT\_AVDTP\_SEP\_IN\_USE](#affc7226c1b7795a3d2f51cb4ffaf6d21a7a25b50bff50fff150a3bfb69a7d2aa8) = 0x13 , [BT\_AVDTP\_SEP\_NOT\_IN\_USE](#affc7226c1b7795a3d2f51cb4ffaf6d21aecefed33942c46624cdd26209a791445) = 0x14 , [BT\_AVDTP\_BAD\_SERV\_CATEGORY](#affc7226c1b7795a3d2f51cb4ffaf6d21a260b2bc259678f0d813e7b1a20c477e6) = 0x17 ,     [BT\_AVDTP\_BAD\_PAYLOAD\_FORMAT](#affc7226c1b7795a3d2f51cb4ffaf6d21a851fd25830e88e90706c2e3a8db45ba0) = 0x18 , [BT\_AVDTP\_NOT\_SUPPORTED\_COMMAND](#affc7226c1b7795a3d2f51cb4ffaf6d21a3599e6793991735508735f644a502e75) = 0x19 , [BT\_AVDTP\_INVALID\_CAPABILITIES](#affc7226c1b7795a3d2f51cb4ffaf6d21a4c85c064ea60c5d13000494f0f2abd20) = 0x1A , [BT\_AVDTP\_BAD\_RECOVERY\_TYPE](#affc7226c1b7795a3d2f51cb4ffaf6d21ad3c7ef84765610f59dea092aa1504eee) = 0x22 ,     [BT\_AVDTP\_BAD\_MEDIA\_TRANSPORT\_FORMAT](#affc7226c1b7795a3d2f51cb4ffaf6d21ac1c1575a5479fc41dba1534b03d21e35) = 0x23 , [BT\_AVDTP\_BAD\_RECOVERY\_FORMAT](#affc7226c1b7795a3d2f51cb4ffaf6d21a14ec5c7a6ab35e9b946395765a911099) = 0x25 , [BT\_AVDTP\_BAD\_ROHC\_FORMAT](#affc7226c1b7795a3d2f51cb4ffaf6d21a60cf8824a9c3a5b38bfb6b300d0e01d7) = 0x26 , [BT\_AVDTP\_BAD\_CP\_FORMAT](#affc7226c1b7795a3d2f51cb4ffaf6d21accb4c206f63e8ef78265bd83b25f52da) = 0x27 ,     [BT\_AVDTP\_BAD\_MULTIPLEXING\_FORMAT](#affc7226c1b7795a3d2f51cb4ffaf6d21a90f79a8847a33d5ad76a1ca339a33b14) = 0x28 , [BT\_AVDTP\_UNSUPPORTED\_CONFIGURAION](#affc7226c1b7795a3d2f51cb4ffaf6d21af4849400efd124a97a5e6b797efa1a44) = 0x29 , [BT\_AVDTP\_BAD\_STATE](#affc7226c1b7795a3d2f51cb4ffaf6d21a10e3d79ef76dcfefd5ac648e1fdf2818) = 0x31   } |
|  | AVDTP error code. [More...](#affc7226c1b7795a3d2f51cb4ffaf6d21) |
| enum | [bt\_avdtp\_sep\_type](#a28b828df32df5a40e8487dc4dee78757) { [BT\_AVDTP\_SOURCE](#a28b828df32df5a40e8487dc4dee78757a8652b3d997c0daec5b90be2aa046ae0f) = 0 , [BT\_AVDTP\_SINK](#a28b828df32df5a40e8487dc4dee78757a29ddb8e6ac9f3a5e15dcac7cafa0c8d9) = 1 } |
|  | Stream End Point Type. [More...](#a28b828df32df5a40e8487dc4dee78757) |
| enum | [bt\_avdtp\_media\_type](#a6e9f13217ede2687e206b6a8cbd9137f) { [BT\_AVDTP\_AUDIO](#a6e9f13217ede2687e206b6a8cbd9137faf77a41d832f11dfa01946a6dc7ceee58) = 0x00 , [BT\_AVDTP\_VIDEO](#a6e9f13217ede2687e206b6a8cbd9137fa383f8313252215e91846309eaebb96ee) = 0x01 , [BT\_AVDTP\_MULTIMEDIA](#a6e9f13217ede2687e206b6a8cbd9137fa6ecbf2cc869da3ca5cab0dac88718cf4) = 0x02 } |
|  | Stream End Point Media Type. [More...](#a6e9f13217ede2687e206b6a8cbd9137f) |
| enum | [bt\_avdtp\_service\_category](#a8427dfa4dcd3fe8ac6eaf2471bad7e51) {     [BT\_AVDTP\_SERVICE\_MEDIA\_TRANSPORT](#a8427dfa4dcd3fe8ac6eaf2471bad7e51ab1f6623b4d8205e0ca7119e2b4c1c40c) = 0x01 , [BT\_AVDTP\_SERVICE\_REPORTING](#a8427dfa4dcd3fe8ac6eaf2471bad7e51aa26e4aaa9a62ee539d6001f7af5c3b37) = 0x02 , [BT\_AVDTP\_SERVICE\_MEDIA\_RECOVERY](#a8427dfa4dcd3fe8ac6eaf2471bad7e51a071e2e6d18ed90fb1ec2df84449c1902) = 0x03 , [BT\_AVDTP\_SERVICE\_CONTENT\_PROTECTION](#a8427dfa4dcd3fe8ac6eaf2471bad7e51a53110f0946f0b8f1dde7c0913ae4d642) = 0x04 ,     [BT\_AVDTP\_SERVICE\_HEADER\_COMPRESSION](#a8427dfa4dcd3fe8ac6eaf2471bad7e51a2eaaefe841558fdcb6218d28e59a0b73) = 0x05 , [BT\_AVDTP\_SERVICE\_MULTIPLEXING](#a8427dfa4dcd3fe8ac6eaf2471bad7e51ab639cf078a6fa9012ee5ee5320203439) = 0x06 , [BT\_AVDTP\_SERVICE\_MEDIA\_CODEC](#a8427dfa4dcd3fe8ac6eaf2471bad7e51a84ae7f392441dead9cd57b3098fc6a5e) = 0x07 , [BT\_AVDTP\_SERVICE\_DELAY\_REPORTING](#a8427dfa4dcd3fe8ac6eaf2471bad7e51ad2a426bce39bfc9cf5451243ed26c6c0) = 0x08   } |
|  | service category Type [More...](#a8427dfa4dcd3fe8ac6eaf2471bad7e51) |

## Detailed Description

Audio/Video Distribution Transport Protocol header.

## Enumeration Type Documentation

## [◆ ](#affc7226c1b7795a3d2f51cb4ffaf6d21)bt\_avdtp\_err\_code

| enum [bt\_avdtp\_err\_code](#affc7226c1b7795a3d2f51cb4ffaf6d21) |
| --- |

AVDTP error code.

| Enumerator | |
| --- | --- |
| BT\_AVDTP\_SUCCESS | The response is success, it is not from avdtp spec. |
| BT\_AVDTP\_TIME\_OUT | The request is time out without response, it is not from avdtp spec. |
| BT\_AVDTP\_BAD\_HEADER\_FORMAT | The request packet header format error. |
| BT\_AVDTP\_BAD\_LENGTH | The request packet length is not match the assumed length. |
| BT\_AVDTP\_BAD\_ACP\_SEID | The requested command indicates an invalid ACP SEID (not addressable). |
| BT\_AVDTP\_SEP\_IN\_USE | The SEP is in use. |
| BT\_AVDTP\_SEP\_NOT\_IN\_USE | The SEP is not in use. |
| BT\_AVDTP\_BAD\_SERV\_CATEGORY | The value of Service Category in the request packet is not defined in AVDTP. |
| BT\_AVDTP\_BAD\_PAYLOAD\_FORMAT | The requested command has an incorrect payload format. |
| BT\_AVDTP\_NOT\_SUPPORTED\_COMMAND | The requested command is not supported by the device. |
| BT\_AVDTP\_INVALID\_CAPABILITIES | The reconfigure command is an attempt to reconfigure a transport service codec\_cap of the SEP.  Reconfigure is only permitted for application service codec\_cap |
| BT\_AVDTP\_BAD\_RECOVERY\_TYPE | The requested Recovery Type is not defined in AVDTP. |
| BT\_AVDTP\_BAD\_MEDIA\_TRANSPORT\_FORMAT | The format of Media Transport Capability is not correct. |
| BT\_AVDTP\_BAD\_RECOVERY\_FORMAT | The format of Recovery Service Capability is not correct. |
| BT\_AVDTP\_BAD\_ROHC\_FORMAT | The format of Header Compression Service Capability is not correct. |
| BT\_AVDTP\_BAD\_CP\_FORMAT | The format of Content Protection Service Capability is not correct. |
| BT\_AVDTP\_BAD\_MULTIPLEXING\_FORMAT | The format of Multiplexing Service Capability is not correct. |
| BT\_AVDTP\_UNSUPPORTED\_CONFIGURAION | Configuration not supported. |
| BT\_AVDTP\_BAD\_STATE | Indicates that the ACP state machine is in an invalid state in order to process the signal.  This also includes the situation when an INT receives a request for the same command that it is currently expecting a response |

## [◆ ](#a6e9f13217ede2687e206b6a8cbd9137f)bt\_avdtp\_media\_type

| enum [bt\_avdtp\_media\_type](#a6e9f13217ede2687e206b6a8cbd9137f) |
| --- |

Stream End Point Media Type.

| Enumerator | |
| --- | --- |
| BT\_AVDTP\_AUDIO | Audio Media Type. |
| BT\_AVDTP\_VIDEO | Video Media Type. |
| BT\_AVDTP\_MULTIMEDIA | Multimedia Media Type. |

## [◆ ](#a28b828df32df5a40e8487dc4dee78757)bt\_avdtp\_sep\_type

| enum [bt\_avdtp\_sep\_type](#a28b828df32df5a40e8487dc4dee78757) |
| --- |

Stream End Point Type.

| Enumerator | |
| --- | --- |
| BT\_AVDTP\_SOURCE | Source Role. |
| BT\_AVDTP\_SINK | Sink Role. |

## [◆ ](#a8427dfa4dcd3fe8ac6eaf2471bad7e51)bt\_avdtp\_service\_category

| enum [bt\_avdtp\_service\_category](#a8427dfa4dcd3fe8ac6eaf2471bad7e51) |
| --- |

service category Type

| Enumerator | |
| --- | --- |
| BT\_AVDTP\_SERVICE\_MEDIA\_TRANSPORT | Media Transport. |
| BT\_AVDTP\_SERVICE\_REPORTING | Reporting. |
| BT\_AVDTP\_SERVICE\_MEDIA\_RECOVERY | Recovery. |
| BT\_AVDTP\_SERVICE\_CONTENT\_PROTECTION | Content Protection. |
| BT\_AVDTP\_SERVICE\_HEADER\_COMPRESSION | Header Compression. |
| BT\_AVDTP\_SERVICE\_MULTIPLEXING | Multiplexing. |
| BT\_AVDTP\_SERVICE\_MEDIA\_CODEC | Media Codec. |
| BT\_AVDTP\_SERVICE\_DELAY\_REPORTING | Delay Reporting. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [avdtp.h](avdtp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
