---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/rtc__ds3231_8h.html
original_path: doxygen/html/rtc__ds3231_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

rtc\_ds3231.h File Reference

[Go to the source code of this file.](rtc__ds3231_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DS3231\_REG\_TIME\_SECONDS](#a187993c430c68d3841b312cddd4fe14c)   0x00 |
| #define | [DS3231\_REG\_TIME\_MINUTES](#ac66924e0c5c3dc095c8cf6c9666571fd)   0x01 |
| #define | [DS3231\_REG\_TIME\_HOURS](#ae5e85807525a616b6b49979c7615ae4a)   0x02 |
| #define | [DS3231\_REG\_TIME\_DAY\_OF\_WEEK](#abe540c9bcdc7bd43898220dd836c074c)   0x03 |
| #define | [DS3231\_REG\_TIME\_DATE](#aac944d073c221f89d3fc00fdccc2dec7)   0x04 |
| #define | [DS3231\_REG\_TIME\_MONTH](#a141283f5923a36019c2064fb60f56326)   0x05 |
| #define | [DS3231\_REG\_TIME\_YEAR](#af1e20c0549eaf16de73814c9bb93135d)   0x06 |
| #define | [DS3231\_REG\_ALARM\_1\_SECONDS](#a337349639f9eeac901ecd5c9fbcb8998)   0x07 |
| #define | [DS3231\_REG\_ALARM\_1\_MINUTES](#a8e7495a5790b651ec35dc5f8d6a46e95)   0x08 |
| #define | [DS3231\_REG\_ALARM\_1\_HOURS](#aab48f5a7f301d470047f4410f406224c)   0x09 |
| #define | [DS3231\_REG\_ALARM\_1\_DATE](#a89d12b2aa1a5412ed394080531c04c8c)   0x0A |
| #define | [DS3231\_REG\_ALARM\_2\_MINUTES](#aa03fe6e862f1e5094f05e06ae4bbf108)   0x0B |
| #define | [DS3231\_REG\_ALARM\_2\_HOURS](#a0f374dcba3ebc59daf345f6ecaa59f16)   0x0C |
| #define | [DS3231\_REG\_ALARM\_2\_DATE](#a6fc6b9519ca96bed9d62a253199af1f0)   0x0D |
| #define | [DS3231\_REG\_CTRL](#aea14f214d3c7c4feaa29c2632fd92371)   0x0E |
| #define | [DS3231\_REG\_CTRL\_STS](#a6d2cfdba50a2f834cd5f2e372c46a0a2)   0x0F |
| #define | [DS3231\_REG\_AGING\_OFFSET](#a2c630e7f3a057480946da744449d2eb3)   0x10 |
| #define | [DS3231\_BITS\_TIME\_SECONDS](#af1a6735d3f31fdd3ac2892437e7322df)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(6, 0) |
| #define | [DS3231\_BITS\_TIME\_MINUTES](#a3d4c98bdf335837ce0780176b8e08119)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(6, 0) |
| #define | [DS3231\_BITS\_TIME\_HOURS](#aee073fea577330d4ecbd37f1da498dd3)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 0) |
| #define | [DS3231\_BITS\_TIME\_PM](#a1050727c51f29cf040196d76c171a30b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [DS3231\_BITS\_TIME\_12HR](#a52613d566dcd8497b39ad4c154d95b28)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [DS3231\_BITS\_TIME\_DAY\_OF\_WEEK](#a7d917b52957e4b61ef0c933ce9fd73c7)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(2, 0) |
| #define | [DS3231\_BITS\_TIME\_DATE](#abeab153561c71060cdd8ab82b20207f7)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 0) |
| #define | [DS3231\_BITS\_TIME\_MONTH](#a65dea42153d17bd5163b2c35296e54fb)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(4, 0) |
| #define | [DS3231\_BITS\_TIME\_CENTURY](#a65fd40e64760a2178c4fc82bf2d8a060)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [DS3231\_BITS\_TIME\_YEAR](#a95db7b4dc81d7951205d78fcfc041fa5)   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 0) |
| #define | [DS3231\_BITS\_ALARM\_RATE](#ad1fdc4e68cdaa52333c3e62b63f0ab83)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [DS3231\_BITS\_ALARM\_DATE\_W\_OR\_M](#a793f06ed1fa6530cb5f670d047b6f11b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [DS3231\_BITS\_SIGN](#a6c3c187e805d1690fc95b8cf28464dfe)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [DS3231\_BITS\_CTRL\_EOSC](#a8af0c897cfc7b5e14b0e41b79f19cd4d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) /\* enable oscillator, active low \*/ |
| #define | [DS3231\_BITS\_CTRL\_BBSQW](#a700ff940db5f1cb1deda9807c6ea789a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) /\* enable battery-backed square-wave \*/ |
| #define | [DS3231\_BITS\_CTRL\_CONV](#a67e01c51fc4d1f0615d00f276eede03a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [DS3231\_BITS\_CTRL\_RS2](#ae1601b168cd49a5dc4fe49fe0c46817d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [DS3231\_BITS\_CTRL\_RS1](#ac0a14b3ee52a170089213d13fa661698)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [DS3231\_BITS\_CTRL\_INTCTRL](#a725674abd8a3b0df46057d92a90d4e9c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [DS3231\_BITS\_CTRL\_ALARM\_2\_EN](#a98081c1e726f3d61c9fa4cc96f2e5896)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [DS3231\_BITS\_CTRL\_ALARM\_1\_EN](#a6b4e6afb16cf51e06891c3b9f8e4471e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [DS3231\_BITS\_CTRL\_STS\_OSF](#aac6acc5700a872e9819642a404f01c1b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) /\* oscillator stop flag \*/ /\* read only \*/ |
| #define | [DS3231\_BITS\_CTRL\_STS\_32\_EN](#a30d036ea3357246e979870687436fb63)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) /\* 32kHz square-wave \*/ |
| #define | [DS3231\_BITS\_CTRL\_STS\_BSY](#a175dc0d5e5780fa9c3ab27f461c0088f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [DS3231\_BITS\_CTRL\_STS\_ALARM\_2\_FLAG](#a112b3f339727a4239707564438e90566)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) /\* can only be set to 0 \*/ |
| #define | [DS3231\_BITS\_CTRL\_STS\_ALARM\_1\_FLAG](#a56b77005b72874a2dffc3ff9d7691254)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) /\* can only be set to 0 \*/ |
| #define | [DS3231\_BITS\_DATA](#a07b1af46954b37add67cb3fdf975af5a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6, 0) |
| #define | [DS3231\_BITS\_STS\_OSC](#a701b74da1c41863195f36d0779c543c9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [DS3231\_BITS\_STS\_INTCTRL](#afa345544f3a610bcce7a0fdd68a3d553)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [DS3231\_BITS\_STS\_SQW](#a18c98b9dcd706f8f2bb25d38e8d1d9f8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [DS3231\_BITS\_STS\_32KHZ](#ad1b79e60328b65a381873c42ca5247dd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [DS3231\_BITS\_STS\_ALARM\_1](#a3cd872a940476ef5918324f23680e4d5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [DS3231\_BITS\_STS\_ALARM\_2](#a6e4f4fbd24d13165fa24b41bbfc410fe)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |

## Macro Definition Documentation

## [◆ ](#a793f06ed1fa6530cb5f670d047b6f11b)DS3231\_BITS\_ALARM\_DATE\_W\_OR\_M

| #define DS3231\_BITS\_ALARM\_DATE\_W\_OR\_M   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#ad1fdc4e68cdaa52333c3e62b63f0ab83)DS3231\_BITS\_ALARM\_RATE

| #define DS3231\_BITS\_ALARM\_RATE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#a6b4e6afb16cf51e06891c3b9f8e4471e)DS3231\_BITS\_CTRL\_ALARM\_1\_EN

| #define DS3231\_BITS\_CTRL\_ALARM\_1\_EN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a98081c1e726f3d61c9fa4cc96f2e5896)DS3231\_BITS\_CTRL\_ALARM\_2\_EN

| #define DS3231\_BITS\_CTRL\_ALARM\_2\_EN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a700ff940db5f1cb1deda9807c6ea789a)DS3231\_BITS\_CTRL\_BBSQW

| #define DS3231\_BITS\_CTRL\_BBSQW   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) /\* enable battery-backed square-wave \*/ |
| --- |

## [◆ ](#a67e01c51fc4d1f0615d00f276eede03a)DS3231\_BITS\_CTRL\_CONV

| #define DS3231\_BITS\_CTRL\_CONV   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#a8af0c897cfc7b5e14b0e41b79f19cd4d)DS3231\_BITS\_CTRL\_EOSC

| #define DS3231\_BITS\_CTRL\_EOSC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) /\* enable oscillator, active low \*/ |
| --- |

## [◆ ](#a725674abd8a3b0df46057d92a90d4e9c)DS3231\_BITS\_CTRL\_INTCTRL

| #define DS3231\_BITS\_CTRL\_INTCTRL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#ac0a14b3ee52a170089213d13fa661698)DS3231\_BITS\_CTRL\_RS1

| #define DS3231\_BITS\_CTRL\_RS1   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#ae1601b168cd49a5dc4fe49fe0c46817d)DS3231\_BITS\_CTRL\_RS2

| #define DS3231\_BITS\_CTRL\_RS2   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a30d036ea3357246e979870687436fb63)DS3231\_BITS\_CTRL\_STS\_32\_EN

| #define DS3231\_BITS\_CTRL\_STS\_32\_EN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) /\* 32kHz square-wave \*/ |
| --- |

## [◆ ](#a56b77005b72874a2dffc3ff9d7691254)DS3231\_BITS\_CTRL\_STS\_ALARM\_1\_FLAG

| #define DS3231\_BITS\_CTRL\_STS\_ALARM\_1\_FLAG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) /\* can only be set to 0 \*/ |
| --- |

## [◆ ](#a112b3f339727a4239707564438e90566)DS3231\_BITS\_CTRL\_STS\_ALARM\_2\_FLAG

| #define DS3231\_BITS\_CTRL\_STS\_ALARM\_2\_FLAG   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) /\* can only be set to 0 \*/ |
| --- |

## [◆ ](#a175dc0d5e5780fa9c3ab27f461c0088f)DS3231\_BITS\_CTRL\_STS\_BSY

| #define DS3231\_BITS\_CTRL\_STS\_BSY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#aac6acc5700a872e9819642a404f01c1b)DS3231\_BITS\_CTRL\_STS\_OSF

| #define DS3231\_BITS\_CTRL\_STS\_OSF   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) /\* oscillator stop flag \*/ /\* read only \*/ |
| --- |

## [◆ ](#a07b1af46954b37add67cb3fdf975af5a)DS3231\_BITS\_DATA

| #define DS3231\_BITS\_DATA   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6, 0) |
| --- |

## [◆ ](#a6c3c187e805d1690fc95b8cf28464dfe)DS3231\_BITS\_SIGN

| #define DS3231\_BITS\_SIGN   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#ad1b79e60328b65a381873c42ca5247dd)DS3231\_BITS\_STS\_32KHZ

| #define DS3231\_BITS\_STS\_32KHZ   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a3cd872a940476ef5918324f23680e4d5)DS3231\_BITS\_STS\_ALARM\_1

| #define DS3231\_BITS\_STS\_ALARM\_1   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a6e4f4fbd24d13165fa24b41bbfc410fe)DS3231\_BITS\_STS\_ALARM\_2

| #define DS3231\_BITS\_STS\_ALARM\_2   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#afa345544f3a610bcce7a0fdd68a3d553)DS3231\_BITS\_STS\_INTCTRL

| #define DS3231\_BITS\_STS\_INTCTRL   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a701b74da1c41863195f36d0779c543c9)DS3231\_BITS\_STS\_OSC

| #define DS3231\_BITS\_STS\_OSC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a18c98b9dcd706f8f2bb25d38e8d1d9f8)DS3231\_BITS\_STS\_SQW

| #define DS3231\_BITS\_STS\_SQW   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a52613d566dcd8497b39ad4c154d95b28)DS3231\_BITS\_TIME\_12HR

| #define DS3231\_BITS\_TIME\_12HR   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#a65fd40e64760a2178c4fc82bf2d8a060)DS3231\_BITS\_TIME\_CENTURY

| #define DS3231\_BITS\_TIME\_CENTURY   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#abeab153561c71060cdd8ab82b20207f7)DS3231\_BITS\_TIME\_DATE

| #define DS3231\_BITS\_TIME\_DATE   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 0) |
| --- |

## [◆ ](#a7d917b52957e4b61ef0c933ce9fd73c7)DS3231\_BITS\_TIME\_DAY\_OF\_WEEK

| #define DS3231\_BITS\_TIME\_DAY\_OF\_WEEK   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(2, 0) |
| --- |

## [◆ ](#aee073fea577330d4ecbd37f1da498dd3)DS3231\_BITS\_TIME\_HOURS

| #define DS3231\_BITS\_TIME\_HOURS   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(5, 0) |
| --- |

## [◆ ](#a3d4c98bdf335837ce0780176b8e08119)DS3231\_BITS\_TIME\_MINUTES

| #define DS3231\_BITS\_TIME\_MINUTES   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(6, 0) |
| --- |

## [◆ ](#a65dea42153d17bd5163b2c35296e54fb)DS3231\_BITS\_TIME\_MONTH

| #define DS3231\_BITS\_TIME\_MONTH   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(4, 0) |
| --- |

## [◆ ](#a1050727c51f29cf040196d76c171a30b)DS3231\_BITS\_TIME\_PM

| #define DS3231\_BITS\_TIME\_PM   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#af1a6735d3f31fdd3ac2892437e7322df)DS3231\_BITS\_TIME\_SECONDS

| #define DS3231\_BITS\_TIME\_SECONDS   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(6, 0) |
| --- |

## [◆ ](#a95db7b4dc81d7951205d78fcfc041fa5)DS3231\_BITS\_TIME\_YEAR

| #define DS3231\_BITS\_TIME\_YEAR   [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(7, 0) |
| --- |

## [◆ ](#a2c630e7f3a057480946da744449d2eb3)DS3231\_REG\_AGING\_OFFSET

| #define DS3231\_REG\_AGING\_OFFSET   0x10 |
| --- |

## [◆ ](#a89d12b2aa1a5412ed394080531c04c8c)DS3231\_REG\_ALARM\_1\_DATE

| #define DS3231\_REG\_ALARM\_1\_DATE   0x0A |
| --- |

## [◆ ](#aab48f5a7f301d470047f4410f406224c)DS3231\_REG\_ALARM\_1\_HOURS

| #define DS3231\_REG\_ALARM\_1\_HOURS   0x09 |
| --- |

## [◆ ](#a8e7495a5790b651ec35dc5f8d6a46e95)DS3231\_REG\_ALARM\_1\_MINUTES

| #define DS3231\_REG\_ALARM\_1\_MINUTES   0x08 |
| --- |

## [◆ ](#a337349639f9eeac901ecd5c9fbcb8998)DS3231\_REG\_ALARM\_1\_SECONDS

| #define DS3231\_REG\_ALARM\_1\_SECONDS   0x07 |
| --- |

## [◆ ](#a6fc6b9519ca96bed9d62a253199af1f0)DS3231\_REG\_ALARM\_2\_DATE

| #define DS3231\_REG\_ALARM\_2\_DATE   0x0D |
| --- |

## [◆ ](#a0f374dcba3ebc59daf345f6ecaa59f16)DS3231\_REG\_ALARM\_2\_HOURS

| #define DS3231\_REG\_ALARM\_2\_HOURS   0x0C |
| --- |

## [◆ ](#aa03fe6e862f1e5094f05e06ae4bbf108)DS3231\_REG\_ALARM\_2\_MINUTES

| #define DS3231\_REG\_ALARM\_2\_MINUTES   0x0B |
| --- |

## [◆ ](#aea14f214d3c7c4feaa29c2632fd92371)DS3231\_REG\_CTRL

| #define DS3231\_REG\_CTRL   0x0E |
| --- |

## [◆ ](#a6d2cfdba50a2f834cd5f2e372c46a0a2)DS3231\_REG\_CTRL\_STS

| #define DS3231\_REG\_CTRL\_STS   0x0F |
| --- |

## [◆ ](#aac944d073c221f89d3fc00fdccc2dec7)DS3231\_REG\_TIME\_DATE

| #define DS3231\_REG\_TIME\_DATE   0x04 |
| --- |

## [◆ ](#abe540c9bcdc7bd43898220dd836c074c)DS3231\_REG\_TIME\_DAY\_OF\_WEEK

| #define DS3231\_REG\_TIME\_DAY\_OF\_WEEK   0x03 |
| --- |

## [◆ ](#ae5e85807525a616b6b49979c7615ae4a)DS3231\_REG\_TIME\_HOURS

| #define DS3231\_REG\_TIME\_HOURS   0x02 |
| --- |

## [◆ ](#ac66924e0c5c3dc095c8cf6c9666571fd)DS3231\_REG\_TIME\_MINUTES

| #define DS3231\_REG\_TIME\_MINUTES   0x01 |
| --- |

## [◆ ](#a141283f5923a36019c2064fb60f56326)DS3231\_REG\_TIME\_MONTH

| #define DS3231\_REG\_TIME\_MONTH   0x05 |
| --- |

## [◆ ](#a187993c430c68d3841b312cddd4fe14c)DS3231\_REG\_TIME\_SECONDS

| #define DS3231\_REG\_TIME\_SECONDS   0x00 |
| --- |

## [◆ ](#af1e20c0549eaf16de73814c9bb93135d)DS3231\_REG\_TIME\_YEAR

| #define DS3231\_REG\_TIME\_YEAR   0x06 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [rtc](dir_fe6de79d2b035e3fa4834af86b312149.md)
- [rtc\_ds3231.h](rtc__ds3231_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
