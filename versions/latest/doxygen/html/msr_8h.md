---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/msr_8h.html
original_path: doxygen/html/msr_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

msr.h File Reference

[Go to the source code of this file.](msr_8h_source.md)

| Macros | |
| --- | --- |
| #define | [X86\_TIME\_STAMP\_COUNTER\_MSR](#a6a8159994070c5d75a390f81ae460dee)   0x00000010 |
| #define | [X86\_SPEC\_CTRL\_MSR](#ab89835f2b734a80195db70d28749e7c1)   0x00000048 |
| #define | [X86\_SPEC\_CTRL\_MSR\_IBRS](#aa7de592375a86f19136972a5bd4c8453)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [X86\_SPEC\_CTRL\_MSR\_SSBD](#aa267e6d482addf97eb630f208281000d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [X86\_APIC\_BASE\_MSR](#a0083758907f732a480f8a9ec2ccb3778)   0x0000001b |
| #define | [X86\_APIC\_BASE\_MSR\_X2APIC](#a940221ed627aad8120e2abb0c12ff196)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| #define | [X86\_MTRR\_DEF\_TYPE\_MSR](#aa5479ba3ca3bbda70d35819b67d3583f)   0x000002ff |
| #define | [X86\_MTRR\_DEF\_TYPE\_MSR\_ENABLE](#a2c5d224b53d927e325b710484ebfb2a0)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| #define | [X86\_X2APIC\_BASE\_MSR](#ab5ccd444077064e6b7a399ceb3d61f9f)   0x00000800 /\* .. thru 0x00000BFF \*/ |
| #define | [X86\_EFER\_MSR](#a4226ff6b5ecc23277e9cb0433b0d6c22)   0xC0000080U |
| #define | [X86\_EFER\_MSR\_SCE](#ae20fe7661b62a20885d6cef7f83e917e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [X86\_EFER\_MSR\_LME](#a4484482d4a9eee0288970fb8a6fc70f5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| #define | [X86\_EFER\_MSR\_NXE](#a410a6e81d01226d399b8e24d5506013d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| #define | [X86\_STAR\_MSR](#a48b0da8dc9cdd319cf75ac0d5933ce0f)   0xC0000081U |
| #define | [X86\_LSTAR\_MSR](#a64cac416a2f72c129bd8e01fd885aaea)   0xC0000082U |
| #define | [X86\_FMASK\_MSR](#af28b1c23c69f1658384a5de5b9461c64)   0xC0000084U |
| #define | [X86\_FS\_BASE](#a935167aeb9bc9b1f4e73d8001c3c72f0)   0xC0000100U |
| #define | [X86\_GS\_BASE](#a263e74097e9162fd54f5d05af74f4aa1)   0xC0000101U |
| #define | [X86\_KERNEL\_GS\_BASE](#af832b3ce587c52ff9764d42fbd1c1b25)   0xC0000102U |

## Macro Definition Documentation

## [◆ ](#a0083758907f732a480f8a9ec2ccb3778)X86\_APIC\_BASE\_MSR

| #define X86\_APIC\_BASE\_MSR   0x0000001b |
| --- |

## [◆ ](#a940221ed627aad8120e2abb0c12ff196)X86\_APIC\_BASE\_MSR\_X2APIC

| #define X86\_APIC\_BASE\_MSR\_X2APIC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

## [◆ ](#a4226ff6b5ecc23277e9cb0433b0d6c22)X86\_EFER\_MSR

| #define X86\_EFER\_MSR   0xC0000080U |
| --- |

## [◆ ](#a4484482d4a9eee0288970fb8a6fc70f5)X86\_EFER\_MSR\_LME

| #define X86\_EFER\_MSR\_LME   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

## [◆ ](#a410a6e81d01226d399b8e24d5506013d)X86\_EFER\_MSR\_NXE

| #define X86\_EFER\_MSR\_NXE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

## [◆ ](#ae20fe7661b62a20885d6cef7f83e917e)X86\_EFER\_MSR\_SCE

| #define X86\_EFER\_MSR\_SCE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#af28b1c23c69f1658384a5de5b9461c64)X86\_FMASK\_MSR

| #define X86\_FMASK\_MSR   0xC0000084U |
| --- |

## [◆ ](#a935167aeb9bc9b1f4e73d8001c3c72f0)X86\_FS\_BASE

| #define X86\_FS\_BASE   0xC0000100U |
| --- |

## [◆ ](#a263e74097e9162fd54f5d05af74f4aa1)X86\_GS\_BASE

| #define X86\_GS\_BASE   0xC0000101U |
| --- |

## [◆ ](#af832b3ce587c52ff9764d42fbd1c1b25)X86\_KERNEL\_GS\_BASE

| #define X86\_KERNEL\_GS\_BASE   0xC0000102U |
| --- |

## [◆ ](#a64cac416a2f72c129bd8e01fd885aaea)X86\_LSTAR\_MSR

| #define X86\_LSTAR\_MSR   0xC0000082U |
| --- |

## [◆ ](#aa5479ba3ca3bbda70d35819b67d3583f)X86\_MTRR\_DEF\_TYPE\_MSR

| #define X86\_MTRR\_DEF\_TYPE\_MSR   0x000002ff |
| --- |

## [◆ ](#a2c5d224b53d927e325b710484ebfb2a0)X86\_MTRR\_DEF\_TYPE\_MSR\_ENABLE

| #define X86\_MTRR\_DEF\_TYPE\_MSR\_ENABLE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

## [◆ ](#ab89835f2b734a80195db70d28749e7c1)X86\_SPEC\_CTRL\_MSR

| #define X86\_SPEC\_CTRL\_MSR   0x00000048 |
| --- |

## [◆ ](#aa7de592375a86f19136972a5bd4c8453)X86\_SPEC\_CTRL\_MSR\_IBRS

| #define X86\_SPEC\_CTRL\_MSR\_IBRS   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#aa267e6d482addf97eb630f208281000d)X86\_SPEC\_CTRL\_MSR\_SSBD

| #define X86\_SPEC\_CTRL\_MSR\_SSBD   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a48b0da8dc9cdd319cf75ac0d5933ce0f)X86\_STAR\_MSR

| #define X86\_STAR\_MSR   0xC0000081U |
| --- |

## [◆ ](#a6a8159994070c5d75a390f81ae460dee)X86\_TIME\_STAMP\_COUNTER\_MSR

| #define X86\_TIME\_STAMP\_COUNTER\_MSR   0x00000010 |
| --- |

## [◆ ](#ab5ccd444077064e6b7a399ceb3d61f9f)X86\_X2APIC\_BASE\_MSR

| #define X86\_X2APIC\_BASE\_MSR   0x00000800 /\* .. thru 0x00000BFF \*/ |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [x86](dir_0c2b2a40388d14bf987ab4c9c60eb89c.md)
- [msr.h](msr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
