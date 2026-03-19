---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/usb__hub_8h.html
original_path: doxygen/html/usb__hub_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

usb\_hub.h File Reference

USB Hub Class device API header.
[More...](#details)

[Go to the source code of this file.](usb__hub_8h_source.md)

| Macros | |
| --- | --- |
| #define | [USB\_HCFS\_C\_HUB\_LOCAL\_POWER](#a997b8615c74e9aa88f8e273b6a3a61fc)   0x00 |
|  | USB Hub Class Feature Selectors defined in spec. |
| #define | [USB\_HCFS\_C\_HUB\_OVER\_CURRENT](#a0b1a392fe6a9e5932158c1cdca43f4bf)   0x01 |
| #define | [USB\_HCFS\_PORT\_CONNECTION](#ad2d66d4f6f517ea0d3dd76da62742552)   0x00 |
| #define | [USB\_HCFS\_PORT\_ENABLE](#a5c8ba71161b59bae12afb5dde7728808)   0x01 |
| #define | [USB\_HCFS\_PORT\_SUSPEND](#a8cd0227e68d424b758e13f470d838868)   0x02 |
| #define | [USB\_HCFS\_PORT\_OVER\_CURRENT](#ae1c71c8da58b67ed5f12f640827b9d77)   0x03 |
| #define | [USB\_HCFS\_PORT\_RESET](#ae4fd5c849765661c61b4212f0bfe495e)   0x04 |
| #define | [USB\_HCFS\_PORT\_POWER](#a1fe915a2e5569480f4fc24e69f24228c)   0x08 |
| #define | [USB\_HCFS\_PORT\_LOW\_SPEED](#ab3dc8ec69e15379c606e7e58980617ca)   0x09 |
| #define | [USB\_HCFS\_C\_PORT\_CONNECTION](#a75e8cf42cfd77add9f306a20fe6bb14f)   0x10 |
| #define | [USB\_HCFS\_C\_PORT\_ENABLE](#a71f79a0dbf15b792ffd93305145de316)   0x11 |
| #define | [USB\_HCFS\_C\_PORT\_SUSPEND](#a84c40b25ec588b86131300a4dbc765bd)   0x12 |
| #define | [USB\_HCFS\_C\_PORT\_OVER\_CURRENT](#aa3273e27d90c343899c4cb1f722c2878)   0x13 |
| #define | [USB\_HCFS\_C\_PORT\_RESET](#ad53ce209e4472d86b6643c7d391b7f24)   0x14 |
| #define | [USB\_HCFS\_PORT\_TEST](#a94a24ef58ab59d399a0dfa0f0903dfb0)   0x15 |
| #define | [USB\_HCFS\_PORT\_INDICATOR](#a2e049932c995b1fe489c38ed0cf09049)   0x16 |
| #define | [USB\_HCREQ\_GET\_STATUS](#a91ad2acf2c5316d20738f4d65d68ee14)   0x00 |
|  | USB Hub Class Request Codes defined in spec. |
| #define | [USB\_HCREQ\_CLEAR\_FEATURE](#a3fc30c26205b41f2ca3abeef815917fa)   0x01 |
| #define | [USB\_HCREQ\_SET\_FEATURE](#a7b4f58864afb11d881929e81aa4843bd)   0x03 |
| #define | [USB\_HCREQ\_GET\_DESCRIPTOR](#a5c13eb60a311c0bf7c1f5e9fa1f66f2b)   0x06 |
| #define | [USB\_HCREQ\_SET\_DESCRIPTOR](#af632ce62b30de5103c799171d08b0f08)   0x07 |
| #define | [USB\_HCREQ\_CLEAR\_TT\_BUFFER](#a479c4d6fe6691d3cda5d4ba6f868cb2f)   0x08 |
| #define | [USB\_HCREQ\_RESET\_TT](#a09990d8d948aef82115489f60a83250b)   0x09 |
| #define | [USB\_HCREQ\_GET\_TT\_STATE](#a4cafe5c744f8e73e1477791c1b64d650)   0x0A |
| #define | [USB\_HCREQ\_STOP\_TT](#aacc155cfc273b57e73d2893d1693bfd1)   0x0B |

## Detailed Description

USB Hub Class device API header.

## Macro Definition Documentation

## [◆ ](#a997b8615c74e9aa88f8e273b6a3a61fc)USB\_HCFS\_C\_HUB\_LOCAL\_POWER

| #define USB\_HCFS\_C\_HUB\_LOCAL\_POWER   0x00 |
| --- |

USB Hub Class Feature Selectors defined in spec.

Table 11-17

## [◆ ](#a0b1a392fe6a9e5932158c1cdca43f4bf)USB\_HCFS\_C\_HUB\_OVER\_CURRENT

| #define USB\_HCFS\_C\_HUB\_OVER\_CURRENT   0x01 |
| --- |

## [◆ ](#a75e8cf42cfd77add9f306a20fe6bb14f)USB\_HCFS\_C\_PORT\_CONNECTION

| #define USB\_HCFS\_C\_PORT\_CONNECTION   0x10 |
| --- |

## [◆ ](#a71f79a0dbf15b792ffd93305145de316)USB\_HCFS\_C\_PORT\_ENABLE

| #define USB\_HCFS\_C\_PORT\_ENABLE   0x11 |
| --- |

## [◆ ](#aa3273e27d90c343899c4cb1f722c2878)USB\_HCFS\_C\_PORT\_OVER\_CURRENT

| #define USB\_HCFS\_C\_PORT\_OVER\_CURRENT   0x13 |
| --- |

## [◆ ](#ad53ce209e4472d86b6643c7d391b7f24)USB\_HCFS\_C\_PORT\_RESET

| #define USB\_HCFS\_C\_PORT\_RESET   0x14 |
| --- |

## [◆ ](#a84c40b25ec588b86131300a4dbc765bd)USB\_HCFS\_C\_PORT\_SUSPEND

| #define USB\_HCFS\_C\_PORT\_SUSPEND   0x12 |
| --- |

## [◆ ](#ad2d66d4f6f517ea0d3dd76da62742552)USB\_HCFS\_PORT\_CONNECTION

| #define USB\_HCFS\_PORT\_CONNECTION   0x00 |
| --- |

## [◆ ](#a5c8ba71161b59bae12afb5dde7728808)USB\_HCFS\_PORT\_ENABLE

| #define USB\_HCFS\_PORT\_ENABLE   0x01 |
| --- |

## [◆ ](#a2e049932c995b1fe489c38ed0cf09049)USB\_HCFS\_PORT\_INDICATOR

| #define USB\_HCFS\_PORT\_INDICATOR   0x16 |
| --- |

## [◆ ](#ab3dc8ec69e15379c606e7e58980617ca)USB\_HCFS\_PORT\_LOW\_SPEED

| #define USB\_HCFS\_PORT\_LOW\_SPEED   0x09 |
| --- |

## [◆ ](#ae1c71c8da58b67ed5f12f640827b9d77)USB\_HCFS\_PORT\_OVER\_CURRENT

| #define USB\_HCFS\_PORT\_OVER\_CURRENT   0x03 |
| --- |

## [◆ ](#a1fe915a2e5569480f4fc24e69f24228c)USB\_HCFS\_PORT\_POWER

| #define USB\_HCFS\_PORT\_POWER   0x08 |
| --- |

## [◆ ](#ae4fd5c849765661c61b4212f0bfe495e)USB\_HCFS\_PORT\_RESET

| #define USB\_HCFS\_PORT\_RESET   0x04 |
| --- |

## [◆ ](#a8cd0227e68d424b758e13f470d838868)USB\_HCFS\_PORT\_SUSPEND

| #define USB\_HCFS\_PORT\_SUSPEND   0x02 |
| --- |

## [◆ ](#a94a24ef58ab59d399a0dfa0f0903dfb0)USB\_HCFS\_PORT\_TEST

| #define USB\_HCFS\_PORT\_TEST   0x15 |
| --- |

## [◆ ](#a3fc30c26205b41f2ca3abeef815917fa)USB\_HCREQ\_CLEAR\_FEATURE

| #define USB\_HCREQ\_CLEAR\_FEATURE   0x01 |
| --- |

## [◆ ](#a479c4d6fe6691d3cda5d4ba6f868cb2f)USB\_HCREQ\_CLEAR\_TT\_BUFFER

| #define USB\_HCREQ\_CLEAR\_TT\_BUFFER   0x08 |
| --- |

## [◆ ](#a5c13eb60a311c0bf7c1f5e9fa1f66f2b)USB\_HCREQ\_GET\_DESCRIPTOR

| #define USB\_HCREQ\_GET\_DESCRIPTOR   0x06 |
| --- |

## [◆ ](#a91ad2acf2c5316d20738f4d65d68ee14)USB\_HCREQ\_GET\_STATUS

| #define USB\_HCREQ\_GET\_STATUS   0x00 |
| --- |

USB Hub Class Request Codes defined in spec.

Table 11-16

## [◆ ](#a4cafe5c744f8e73e1477791c1b64d650)USB\_HCREQ\_GET\_TT\_STATE

| #define USB\_HCREQ\_GET\_TT\_STATE   0x0A |
| --- |

## [◆ ](#a09990d8d948aef82115489f60a83250b)USB\_HCREQ\_RESET\_TT

| #define USB\_HCREQ\_RESET\_TT   0x09 |
| --- |

## [◆ ](#af632ce62b30de5103c799171d08b0f08)USB\_HCREQ\_SET\_DESCRIPTOR

| #define USB\_HCREQ\_SET\_DESCRIPTOR   0x07 |
| --- |

## [◆ ](#a7b4f58864afb11d881929e81aa4843bd)USB\_HCREQ\_SET\_FEATURE

| #define USB\_HCREQ\_SET\_FEATURE   0x03 |
| --- |

## [◆ ](#aacc155cfc273b57e73d2893d1693bfd1)USB\_HCREQ\_STOP\_TT

| #define USB\_HCREQ\_STOP\_TT   0x0B |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [usb](dir_d8285a9da4e2f530d10dd4c17d446a84.md)
- [class](dir_c68ea25cffcb2672410964c117624aed.md)
- [usb\_hub.h](usb__hub_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
