---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/include_2zephyr_2arch_2arm64_2cpu_8h.html
original_path: doxygen/html/include_2zephyr_2arch_2arm64_2cpu_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cpu.h File Reference

`#include <[zephyr/sys/util_macro.h](util__macro_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`

[Go to the source code of this file.](include_2zephyr_2arch_2arm64_2cpu_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DAIFSET\_FIQ\_BIT](#a53fb1a3ffce153d445525392fb411687)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [DAIFSET\_IRQ\_BIT](#a22d4cee27b78fddece088591958ca037)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [DAIFSET\_ABT\_BIT](#a4a9605b3286e62a9d878c7cfdccbf6f6)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [DAIFSET\_DBG\_BIT](#ae8f3edaddcaaf22a1155da424838b326)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [DAIFCLR\_FIQ\_BIT](#abf5cf8b639767836af6967f6d07e07b3)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [DAIFCLR\_IRQ\_BIT](#a6f6ae405bbde72ffef083bca9448269b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [DAIFCLR\_ABT\_BIT](#a21a0f602ba0c8b87cc082e3e13aa5d98)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [DAIFCLR\_DBG\_BIT](#afb4bae58d424e6460802949ef0355d21)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [DAIF\_FIQ\_BIT](#a5e04c9f2838f5bb1741bffa1444c299e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [DAIF\_IRQ\_BIT](#ad4a89cfde4c1112886aaa11b1004e2db)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [DAIF\_ABT\_BIT](#a6a85c27138f0c3925e1c51e9d6768cfd)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| #define | [DAIF\_DBG\_BIT](#a3293a3a9e486e835a22439820cffb06d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| #define | [SPSR\_DAIF\_SHIFT](#a193071e5757a40fc372e0d1ab10f280f)   (6) |
| #define | [SPSR\_DAIF\_MASK](#af5444cb52ad93024bf6bfd6487a9de46)   (0xf << [SPSR\_DAIF\_SHIFT](#a193071e5757a40fc372e0d1ab10f280f)) |
| #define | [SPSR\_MODE\_EL0T](#a5ac2f987d02999da93878c4b7b6a39ce)   (0x0) |
| #define | [SPSR\_MODE\_EL1T](#a440d11721e78f76bd7022cc8aef83aca)   (0x4) |
| #define | [SPSR\_MODE\_EL1H](#afb0eeebb254ef2cd71960f9e77af181e)   (0x5) |
| #define | [SPSR\_MODE\_EL2T](#a5c065c9fe9bbeefc64dcdda2f6c4b5bd)   (0x8) |
| #define | [SPSR\_MODE\_EL2H](#a3ad33c29d57e86dc7f416a6bf267d257)   (0x9) |
| #define | [SPSR\_MODE\_MASK](#ad42eefed5f9728f8dd454d2fad321ae3)   (0xf) |
| #define | [SCTLR\_EL3\_RES1](#aa5f1069250ab50a42e788f8eb655e0a7) |
| #define | [SCTLR\_EL2\_RES1](#acee5ccd8b0a2f885465442ef777c964a) |
| #define | [SCTLR\_EL1\_RES1](#ac53a7152c26719a8bb4d9cafdfca2045) |
| #define | [SCTLR\_M\_BIT](#a223e38830566f400f6d592a6bb7dd361)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [SCTLR\_A\_BIT](#ad9dc6fc20549b11dc1b2cc5ed02d5ee7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [SCTLR\_C\_BIT](#a752ac38bb53a96c6749fbfc09a1fb88d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [SCTLR\_SA\_BIT](#a7a33d6c6dc85bc5aef0aebafa1f2f223)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [SCTLR\_I\_BIT](#ac9fd86e6613531ab567031f4c02a2900)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| #define | [SCTLR\_BR\_BIT](#a6bbbc667734e9749f0cbb63cc3ff4341)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17) |
| #define | [CPACR\_EL1\_FPEN\_NOTRAP](#a93a25e810ffc65f91f94c8ed389b4138)   (0x3 << 20) |
| #define | [SCR\_NS\_BIT](#a3356501dba79206460819c2b99617a8e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [SCR\_IRQ\_BIT](#aae3302d2a8466a2b9a771721548e5263)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [SCR\_FIQ\_BIT](#a819b23e7868c4662bd4b3d19fa6eed5d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [SCR\_EA\_BIT](#ae86fa2091d1dbac36137aa064eee7d4e)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [SCR\_SMD\_BIT](#a7c0a0c7d1d0865d4454b88f4ae14f45f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| #define | [SCR\_HCE\_BIT](#a547675dd8352ffb1fcfb6dec5914225a)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| #define | [SCR\_RW\_BIT](#a1ab9bded034ce4f46ead5d01b59674be)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| #define | [SCR\_ST\_BIT](#a9497ad7be55a9e2afcd3033d2c2e6d03)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| #define | [SCR\_EEL2\_BIT](#ad912faedaeee2519ec8207ed2d0a4704)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18) |
| #define | [SCR\_RES1](#a4596599ea8aa7c7d7be74cb60319535d)   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5)) |
| #define | [MPIDR\_AFFLVL\_MASK](#a9bce40a5c0fceea5298a899b174c3e1c)   (0xffULL) |
| #define | [MPIDR\_AFF0\_SHIFT](#a7a2087ca83455cf2759a5aee220105e2)   (0) |
| #define | [MPIDR\_AFF1\_SHIFT](#a3a7ffd9f7a014257a725513d531edab2)   (8) |
| #define | [MPIDR\_AFF2\_SHIFT](#a61d65102667e48cb00b7f9133dcd60f2)   (16) |
| #define | [MPIDR\_AFF3\_SHIFT](#adcd8397ffe05b55aec4ae2505879eed5)   (32) |
| #define | [MPIDR\_AFF\_MASK](#aa64dd15e6bcb1b034ccadf54f358f02d)   ([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(23, 0) | [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(39, 32)) |
| #define | [MPIDR\_AFFLVL](#a35278aa57b0b98cd0cb541cfea58b177)(mpidr, aff\_level) |
| #define | [GET\_MPIDR](#a958d9c5f047f5dc318ecf4b171a68949)() |
| #define | [MPIDR\_TO\_CORE](#a850e9ad6314a72da4ef5ff09d5e1e024)(mpidr) |
| #define | [MODE\_EL\_SHIFT](#a22ce702a54ad18a7b76edb2fb665f8fd)   (0x2) |
| #define | [MODE\_EL\_MASK](#af57f4ebf8044288140b76f1063de6d6d)   (0x3) |
| #define | [MODE\_EL3](#ad51a9827564f8457d36f167593de7b83)   (0x3) |
| #define | [MODE\_EL2](#a8c3515664794ffdcd08191f5c48c3ed0)   (0x2) |
| #define | [MODE\_EL1](#ad3372878ec0c895ae1c791b0ef2d24c0)   (0x1) |
| #define | [MODE\_EL0](#affee69f2502d7e1b743d1fc79dd78c1d)   (0x0) |
| #define | [GET\_EL](#a16a04b233cad3fb65cb16dbeff32f8f2)(\_mode) |
| #define | [ESR\_EC\_SHIFT](#a6b4d7e44bdb5912494cb830ba3e09641)   (26) |
| #define | [ESR\_EC\_MASK](#a423881002388f48bd9c18ee87d4186ef)   [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(6) |
| #define | [ESR\_ISS\_SHIFT](#a18f0cf88a43e06fd81ed66905c039add)   (0) |
| #define | [ESR\_ISS\_MASK](#a011b740985880817c10c3bee7bdb3af8)   [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(25) |
| #define | [ESR\_IL\_SHIFT](#a8b063b9a94bd5e3a0a52d60be5875637)   (25) |
| #define | [ESR\_IL\_MASK](#a705fbfa04a5eb82c44d0a6dc3db9c43c)   [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(1) |
| #define | [GET\_ESR\_EC](#a25719cf4bed7192f43a897085dae1dc1)(esr) |
| #define | [GET\_ESR\_IL](#a93440f95cef11bffbbcec8a8bea3eb21)(esr) |
| #define | [GET\_ESR\_ISS](#a2dc6b6b21a499764da19b26839bbc2b5)(esr) |
| #define | [CNTV\_CTL\_ENABLE\_BIT](#a0001886233fa8459922ad8338eba1dc8)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [CNTV\_CTL\_IMASK\_BIT](#a382fbb7831e299acfd89e9f03c08aebb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [ID\_AA64PFR0\_EL0\_SHIFT](#aacb0fe06a7e7a04c95ce845448c6d436)   (0) |
| #define | [ID\_AA64PFR0\_EL1\_SHIFT](#a9add6e194aac9e74e71c2dc2dd025eb7)   (4) |
| #define | [ID\_AA64PFR0\_EL2\_SHIFT](#a22dea24f7bdc4ae44c39f5aa4bcc5615)   (8) |
| #define | [ID\_AA64PFR0\_EL3\_SHIFT](#a77322f61c0e4e872809b46b769e2ec51)   (12) |
| #define | [ID\_AA64PFR0\_ELX\_MASK](#ad296dae475a3598559cb5f53d74a62b0)   (0xf) |
| #define | [ID\_AA64PFR0\_SEL2\_SHIFT](#a7ebf5636fdc14822cb8bbe10c7f2e1b4)   (36) |
| #define | [ID\_AA64PFR0\_SEL2\_MASK](#a233d4971a3bcb773cfe17e4dbe0ee750)   (0xf) |
| #define | [ACTLR\_EL3\_CPUACTLR\_BIT](#ac50b16ec53bcc4bdf8e7aef09cb335bf)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [ACTLR\_EL3\_CPUECTLR\_BIT](#a685f4f4eaee539caa215a539c7f14c74)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [ACTLR\_EL3\_L2CTLR\_BIT](#a7be92abd63f3a3915495f497460bc89b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [ACTLR\_EL3\_L2ECTLR\_BIT](#a73da30b946e047bf4b736deb26270571)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [ACTLR\_EL3\_L2ACTLR\_BIT](#ae1d807d116307b1321d75ed0917f912d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| #define | [CPTR\_EZ\_BIT](#aff636f95d6e6c2eb2e2c447606c7504f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| #define | [CPTR\_TFP\_BIT](#ab772d9f0f8054ae06af80cc85b956dc7)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| #define | [CPTR\_TTA\_BIT](#a5935d340bf480b94c8268209d8528530)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20) |
| #define | [CPTR\_TCPAC\_BIT](#af3ee0801abd2c3c7aff03daad16222ea)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31) |
| #define | [CPTR\_EL2\_RES1](#a671504449ea674af44e47995678f0a5b)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) | (0xff) |
| #define | [HCR\_FMO\_BIT](#a223d70f2acad7d361ee6fb7b44bdb2e5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [HCR\_IMO\_BIT](#a1792be817d3129a78d60d8bf0d1e5689)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [HCR\_AMO\_BIT](#ad67b4ccd0f2888823525fcc71ea76419)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [HCR\_TGE\_BIT](#a5d2f11fc2059239829db563c8a2bbafe)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(27) |
| #define | [HCR\_RW\_BIT](#a2ecb1fa994da111656e57828a2fb5015)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31) |
| #define | [ICC\_IGRPEN1\_EL1](#aeb7f0f2d77b8c2015a23e12982e35a01)   S3\_0\_C12\_C12\_7 |
| #define | [ICC\_SGI1R](#ae36e32afe169a9173e3294a807af3234)   S3\_0\_C12\_C11\_5 |
| #define | [ICC\_SRE\_EL1](#a178411409386d40d5927250161b2c3d3)   S3\_0\_C12\_C12\_5 |
| #define | [ICC\_SRE\_EL2](#a57664b4d9a0768fd26e0f9e79271d775)   S3\_4\_C12\_C9\_5 |
| #define | [ICC\_SRE\_EL3](#a2aae8716b04b563cfabdeb549ec76b11)   S3\_6\_C12\_C12\_5 |
| #define | [ICC\_CTLR\_EL1](#a24b75fc3f9337d1a0fa0570b5e9a5681)   S3\_0\_C12\_C12\_4 |
| #define | [ICC\_CTLR\_EL3](#ae4ef3359d57cb8862bd140ed52a169a2)   S3\_6\_C12\_C12\_4 |
| #define | [ICC\_PMR\_EL1](#a569e3c45407957f8e9b6786441dd1954)   S3\_0\_C4\_C6\_0 |
| #define | [ICC\_RPR\_EL1](#ac6b780289029a1bfa5f1597272e92087)   S3\_0\_C12\_C11\_3 |
| #define | [ICC\_IGRPEN1\_EL3](#a75ffb5b6ea7d3a96e5d9efae9969773d)   S3\_6\_C12\_C12\_7 |
| #define | [ICC\_IGRPEN0\_EL1](#ae1e035983563d473d79be122004f6d4a)   S3\_0\_C12\_C12\_6 |
| #define | [ICC\_HPPIR0\_EL1](#a1537602c3ecea4f1ce6488a94403ca17)   S3\_0\_C12\_C8\_2 |
| #define | [ICC\_HPPIR1\_EL1](#a5c52945c05fec71d2879ac109a6367db)   S3\_0\_C12\_C12\_2 |
| #define | [ICC\_IAR0\_EL1](#ab617bac1549d87e76f6aa4f7bccb484a)   S3\_0\_C12\_C8\_0 |
| #define | [ICC\_IAR1\_EL1](#a35f0be43473c740c83e32af88e2d0625)   S3\_0\_C12\_C12\_0 |
| #define | [ICC\_EOIR0\_EL1](#af3c07fa13d6f7c298954276bd7e162ba)   S3\_0\_C12\_C8\_1 |
| #define | [ICC\_EOIR1\_EL1](#a5dbe3c5dfb9ff381fac5c1a004116592)   S3\_0\_C12\_C12\_1 |
| #define | [ICC\_SGI0R\_EL1](#a6a15fbfb9c3de076e12f6dedc1c8736b)   S3\_0\_C12\_C11\_7 |
| #define | [ICC\_SRE\_ELx\_SRE\_BIT](#a581240d06f8f27d299a303941934d0a9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [ICC\_SRE\_ELx\_DFB\_BIT](#a54ea5ad3d9d0c66c5787b4c10feaeffb)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [ICC\_SRE\_ELx\_DIB\_BIT](#a6464acd03121adf32b11764b8e16a59f)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [ICC\_SRE\_EL3\_EN\_BIT](#a89642941ffefc853013b0f92cc80f131)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [SGIR\_TGT\_MASK](#aef12617a687736364283ba5fc45eb29a)   (0xffff) |
| #define | [SGIR\_AFF1\_SHIFT](#a54fd53204f64c9081d7c0c9fc3209c37)   (16) |
| #define | [SGIR\_AFF2\_SHIFT](#afcb9746b2d5edfd88af4af2759c931d7)   (32) |
| #define | [SGIR\_AFF3\_SHIFT](#ac4364d68d92dd7b7e1bb7ffac6e81eef)   (48) |
| #define | [SGIR\_AFF\_MASK](#aaebf9f7f5e67965fac91a7eb0336f3e4)   (0xf) |
| #define | [SGIR\_INTID\_SHIFT](#a9bd0096ceb2f20d31173b61127dc5bd3)   (24) |
| #define | [SGIR\_INTID\_MASK](#a6e5a1e0b98322addaa87188e4d9a03f1)   (0xf) |
| #define | [SGIR\_IRM\_SHIFT](#a0a9ae05724f25a9f9e55e664823eeb6b)   (40) |
| #define | [SGIR\_IRM\_MASK](#a31c2a71ebf8c2e296f0c8417012ca7f4)   (0x1) |
| #define | [SGIR\_IRM\_TO\_AFF](#a410f4b9c7089a847d01bc6592335871f)   (0) |
| #define | [GICV3\_SGIR\_VALUE](#a2df77921af208fb2202cb6d03a9ea004)(\_aff3, \_aff2, \_aff1, \_intid, \_irm, \_tgt) |
| #define | [L1\_CACHE\_SHIFT](#a29cd99f347d3f9cfccf2ea01d64b2117)   (6) |
| #define | [L1\_CACHE\_BYTES](#a9400cc2ba37e33279bdbc510a6311fb4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([L1\_CACHE\_SHIFT](#a29cd99f347d3f9cfccf2ea01d64b2117)) |
| #define | [ARM64\_CPU\_INIT\_SIZE](#ab5541d63dd4db4182ab1da587f29189a)   [L1\_CACHE\_BYTES](#a9400cc2ba37e33279bdbc510a6311fb4) |

## Macro Definition Documentation

## [◆ ](#ac50b16ec53bcc4bdf8e7aef09cb335bf)ACTLR\_EL3\_CPUACTLR\_BIT

| #define ACTLR\_EL3\_CPUACTLR\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a685f4f4eaee539caa215a539c7f14c74)ACTLR\_EL3\_CPUECTLR\_BIT

| #define ACTLR\_EL3\_CPUECTLR\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#ae1d807d116307b1321d75ed0917f912d)ACTLR\_EL3\_L2ACTLR\_BIT

| #define ACTLR\_EL3\_L2ACTLR\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#a7be92abd63f3a3915495f497460bc89b)ACTLR\_EL3\_L2CTLR\_BIT

| #define ACTLR\_EL3\_L2CTLR\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a73da30b946e047bf4b736deb26270571)ACTLR\_EL3\_L2ECTLR\_BIT

| #define ACTLR\_EL3\_L2ECTLR\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#ab5541d63dd4db4182ab1da587f29189a)ARM64\_CPU\_INIT\_SIZE

| #define ARM64\_CPU\_INIT\_SIZE   [L1\_CACHE\_BYTES](#a9400cc2ba37e33279bdbc510a6311fb4) |
| --- |

## [◆ ](#a0001886233fa8459922ad8338eba1dc8)CNTV\_CTL\_ENABLE\_BIT

| #define CNTV\_CTL\_ENABLE\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a382fbb7831e299acfd89e9f03c08aebb)CNTV\_CTL\_IMASK\_BIT

| #define CNTV\_CTL\_IMASK\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a93a25e810ffc65f91f94c8ed389b4138)CPACR\_EL1\_FPEN\_NOTRAP

| #define CPACR\_EL1\_FPEN\_NOTRAP   (0x3 << 20) |
| --- |

## [◆ ](#a671504449ea674af44e47995678f0a5b)CPTR\_EL2\_RES1

| #define CPTR\_EL2\_RES1   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(13) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) | (0xff) |
| --- |

## [◆ ](#aff636f95d6e6c2eb2e2c447606c7504f)CPTR\_EZ\_BIT

| #define CPTR\_EZ\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

## [◆ ](#af3ee0801abd2c3c7aff03daad16222ea)CPTR\_TCPAC\_BIT

| #define CPTR\_TCPAC\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31) |
| --- |

## [◆ ](#ab772d9f0f8054ae06af80cc85b956dc7)CPTR\_TFP\_BIT

| #define CPTR\_TFP\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

## [◆ ](#a5935d340bf480b94c8268209d8528530)CPTR\_TTA\_BIT

| #define CPTR\_TTA\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20) |
| --- |

## [◆ ](#a6a85c27138f0c3925e1c51e9d6768cfd)DAIF\_ABT\_BIT

| #define DAIF\_ABT\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

## [◆ ](#a3293a3a9e486e835a22439820cffb06d)DAIF\_DBG\_BIT

| #define DAIF\_DBG\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(9) |
| --- |

## [◆ ](#a5e04c9f2838f5bb1741bffa1444c299e)DAIF\_FIQ\_BIT

| #define DAIF\_FIQ\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(6) |
| --- |

## [◆ ](#ad4a89cfde4c1112886aaa11b1004e2db)DAIF\_IRQ\_BIT

| #define DAIF\_IRQ\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#a21a0f602ba0c8b87cc082e3e13aa5d98)DAIFCLR\_ABT\_BIT

| #define DAIFCLR\_ABT\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#afb4bae58d424e6460802949ef0355d21)DAIFCLR\_DBG\_BIT

| #define DAIFCLR\_DBG\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#abf5cf8b639767836af6967f6d07e07b3)DAIFCLR\_FIQ\_BIT

| #define DAIFCLR\_FIQ\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a6f6ae405bbde72ffef083bca9448269b)DAIFCLR\_IRQ\_BIT

| #define DAIFCLR\_IRQ\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a4a9605b3286e62a9d878c7cfdccbf6f6)DAIFSET\_ABT\_BIT

| #define DAIFSET\_ABT\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#ae8f3edaddcaaf22a1155da424838b326)DAIFSET\_DBG\_BIT

| #define DAIFSET\_DBG\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a53fb1a3ffce153d445525392fb411687)DAIFSET\_FIQ\_BIT

| #define DAIFSET\_FIQ\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a22d4cee27b78fddece088591958ca037)DAIFSET\_IRQ\_BIT

| #define DAIFSET\_IRQ\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a423881002388f48bd9c18ee87d4186ef)ESR\_EC\_MASK

| #define ESR\_EC\_MASK   [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(6) |
| --- |

## [◆ ](#a6b4d7e44bdb5912494cb830ba3e09641)ESR\_EC\_SHIFT

| #define ESR\_EC\_SHIFT   (26) |
| --- |

## [◆ ](#a705fbfa04a5eb82c44d0a6dc3db9c43c)ESR\_IL\_MASK

| #define ESR\_IL\_MASK   [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(1) |
| --- |

## [◆ ](#a8b063b9a94bd5e3a0a52d60be5875637)ESR\_IL\_SHIFT

| #define ESR\_IL\_SHIFT   (25) |
| --- |

## [◆ ](#a011b740985880817c10c3bee7bdb3af8)ESR\_ISS\_MASK

| #define ESR\_ISS\_MASK   [BIT\_MASK](dt-bindings_2adc_2adc_8h.md#a3c12c6d36ad0aa481a3436923d21f4f8)(25) |
| --- |

## [◆ ](#a18f0cf88a43e06fd81ed66905c039add)ESR\_ISS\_SHIFT

| #define ESR\_ISS\_SHIFT   (0) |
| --- |

## [◆ ](#a16a04b233cad3fb65cb16dbeff32f8f2)GET\_EL

| #define GET\_EL | ( |  | *\_mode* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((\_mode) >> [MODE\_EL\_SHIFT](#a22ce702a54ad18a7b76edb2fb665f8fd)) & [MODE\_EL\_MASK](#af57f4ebf8044288140b76f1063de6d6d))

[MODE\_EL\_SHIFT](#a22ce702a54ad18a7b76edb2fb665f8fd)

#define MODE\_EL\_SHIFT

**Definition** cpu.h:87

[MODE\_EL\_MASK](#af57f4ebf8044288140b76f1063de6d6d)

#define MODE\_EL\_MASK

**Definition** cpu.h:88

## [◆ ](#a25719cf4bed7192f43a897085dae1dc1)GET\_ESR\_EC

| #define GET\_ESR\_EC | ( |  | *esr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((esr) >> [ESR\_EC\_SHIFT](#a6b4d7e44bdb5912494cb830ba3e09641)) & [ESR\_EC\_MASK](#a423881002388f48bd9c18ee87d4186ef))

[ESR\_EC\_MASK](#a423881002388f48bd9c18ee87d4186ef)

#define ESR\_EC\_MASK

**Definition** cpu.h:98

[ESR\_EC\_SHIFT](#a6b4d7e44bdb5912494cb830ba3e09641)

#define ESR\_EC\_SHIFT

**Definition** cpu.h:97

## [◆ ](#a93440f95cef11bffbbcec8a8bea3eb21)GET\_ESR\_IL

| #define GET\_ESR\_IL | ( |  | *esr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((esr) >> [ESR\_IL\_SHIFT](#a8b063b9a94bd5e3a0a52d60be5875637)) & [ESR\_IL\_MASK](#a705fbfa04a5eb82c44d0a6dc3db9c43c))

[ESR\_IL\_MASK](#a705fbfa04a5eb82c44d0a6dc3db9c43c)

#define ESR\_IL\_MASK

**Definition** cpu.h:102

[ESR\_IL\_SHIFT](#a8b063b9a94bd5e3a0a52d60be5875637)

#define ESR\_IL\_SHIFT

**Definition** cpu.h:101

## [◆ ](#a2dc6b6b21a499764da19b26839bbc2b5)GET\_ESR\_ISS

| #define GET\_ESR\_ISS | ( |  | *esr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(((esr) >> [ESR\_ISS\_SHIFT](#a18f0cf88a43e06fd81ed66905c039add)) & [ESR\_ISS\_MASK](#a011b740985880817c10c3bee7bdb3af8))

[ESR\_ISS\_MASK](#a011b740985880817c10c3bee7bdb3af8)

#define ESR\_ISS\_MASK

**Definition** cpu.h:100

[ESR\_ISS\_SHIFT](#a18f0cf88a43e06fd81ed66905c039add)

#define ESR\_ISS\_SHIFT

**Definition** cpu.h:99

## [◆ ](#a958d9c5f047f5dc318ecf4b171a68949)GET\_MPIDR

| #define GET\_MPIDR | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

[read\_sysreg](cortex__a__r_2lib__helpers_8h.md#abf4f1c14ffe7c2d5b2bfa605615e676d)(mpidr\_el1)

[read\_sysreg](cortex__a__r_2lib__helpers_8h.md#abf4f1c14ffe7c2d5b2bfa605615e676d)

#define read\_sysreg(reg)

**Definition** lib\_helpers.h:100

## [◆ ](#a2df77921af208fb2202cb6d03a9ea004)GICV3\_SGIR\_VALUE

| #define GICV3\_SGIR\_VALUE | ( |  | *\_aff3*, |
| --- | --- | --- | --- |
|  |  |  | *\_aff2*, |
|  |  |  | *\_aff1*, |
|  |  |  | *\_intid*, |
|  |  |  | *\_irm*, |
|  |  |  | *\_tgt* ) |

**Value:**

(((([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)) (\_aff3) & [SGIR\_AFF\_MASK](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#aaebf9f7f5e67965fac91a7eb0336f3e4)) << [SGIR\_AFF3\_SHIFT](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#ac4364d68d92dd7b7e1bb7ffac6e81eef)) | \

((([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)) (\_irm) & [SGIR\_IRM\_MASK](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#a31c2a71ebf8c2e296f0c8417012ca7f4)) << [SGIR\_IRM\_SHIFT](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#a0a9ae05724f25a9f9e55e664823eeb6b)) | \

((([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)) (\_aff2) & [SGIR\_AFF\_MASK](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#aaebf9f7f5e67965fac91a7eb0336f3e4)) << [SGIR\_AFF2\_SHIFT](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#afcb9746b2d5edfd88af4af2759c931d7)) | \

(((\_intid) & [SGIR\_INTID\_MASK](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#a6e5a1e0b98322addaa87188e4d9a03f1)) << [SGIR\_INTID\_SHIFT](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#a9bd0096ceb2f20d31173b61127dc5bd3)) | \

(((\_aff1) & [SGIR\_AFF\_MASK](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#aaebf9f7f5e67965fac91a7eb0336f3e4)) << [SGIR\_AFF1\_SHIFT](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#a54fd53204f64c9081d7c0c9fc3209c37)) | \

((\_tgt) & [SGIR\_TGT\_MASK](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#aef12617a687736364283ba5fc45eb29a)))

[SGIR\_IRM\_SHIFT](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#a0a9ae05724f25a9f9e55e664823eeb6b)

#define SGIR\_IRM\_SHIFT

**Definition** cpu.h:107

[SGIR\_IRM\_MASK](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#a31c2a71ebf8c2e296f0c8417012ca7f4)

#define SGIR\_IRM\_MASK

**Definition** cpu.h:108

[SGIR\_AFF1\_SHIFT](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#a54fd53204f64c9081d7c0c9fc3209c37)

#define SGIR\_AFF1\_SHIFT

**Definition** cpu.h:101

[SGIR\_INTID\_MASK](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#a6e5a1e0b98322addaa87188e4d9a03f1)

#define SGIR\_INTID\_MASK

**Definition** cpu.h:106

[SGIR\_INTID\_SHIFT](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#a9bd0096ceb2f20d31173b61127dc5bd3)

#define SGIR\_INTID\_SHIFT

**Definition** cpu.h:105

[SGIR\_AFF\_MASK](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#aaebf9f7f5e67965fac91a7eb0336f3e4)

#define SGIR\_AFF\_MASK

**Definition** cpu.h:104

[SGIR\_AFF3\_SHIFT](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#ac4364d68d92dd7b7e1bb7ffac6e81eef)

#define SGIR\_AFF3\_SHIFT

**Definition** cpu.h:103

[SGIR\_TGT\_MASK](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#aef12617a687736364283ba5fc45eb29a)

#define SGIR\_TGT\_MASK

**Definition** cpu.h:100

[SGIR\_AFF2\_SHIFT](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#afcb9746b2d5edfd88af4af2759c931d7)

#define SGIR\_AFF2\_SHIFT

**Definition** cpu.h:102

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

## [◆ ](#ad67b4ccd0f2888823525fcc71ea76419)HCR\_AMO\_BIT

| #define HCR\_AMO\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

## [◆ ](#a223d70f2acad7d361ee6fb7b44bdb2e5)HCR\_FMO\_BIT

| #define HCR\_FMO\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a1792be817d3129a78d60d8bf0d1e5689)HCR\_IMO\_BIT

| #define HCR\_IMO\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

## [◆ ](#a2ecb1fa994da111656e57828a2fb5015)HCR\_RW\_BIT

| #define HCR\_RW\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(31) |
| --- |

## [◆ ](#a5d2f11fc2059239829db563c8a2bbafe)HCR\_TGE\_BIT

| #define HCR\_TGE\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(27) |
| --- |

## [◆ ](#a24b75fc3f9337d1a0fa0570b5e9a5681)ICC\_CTLR\_EL1

| #define ICC\_CTLR\_EL1   S3\_0\_C12\_C12\_4 |
| --- |

## [◆ ](#ae4ef3359d57cb8862bd140ed52a169a2)ICC\_CTLR\_EL3

| #define ICC\_CTLR\_EL3   S3\_6\_C12\_C12\_4 |
| --- |

## [◆ ](#af3c07fa13d6f7c298954276bd7e162ba)ICC\_EOIR0\_EL1

| #define ICC\_EOIR0\_EL1   S3\_0\_C12\_C8\_1 |
| --- |

## [◆ ](#a5dbe3c5dfb9ff381fac5c1a004116592)ICC\_EOIR1\_EL1

| #define ICC\_EOIR1\_EL1   S3\_0\_C12\_C12\_1 |
| --- |

## [◆ ](#a1537602c3ecea4f1ce6488a94403ca17)ICC\_HPPIR0\_EL1

| #define ICC\_HPPIR0\_EL1   S3\_0\_C12\_C8\_2 |
| --- |

## [◆ ](#a5c52945c05fec71d2879ac109a6367db)ICC\_HPPIR1\_EL1

| #define ICC\_HPPIR1\_EL1   S3\_0\_C12\_C12\_2 |
| --- |

## [◆ ](#ab617bac1549d87e76f6aa4f7bccb484a)ICC\_IAR0\_EL1

| #define ICC\_IAR0\_EL1   S3\_0\_C12\_C8\_0 |
| --- |

## [◆ ](#a35f0be43473c740c83e32af88e2d0625)ICC\_IAR1\_EL1

| #define ICC\_IAR1\_EL1   S3\_0\_C12\_C12\_0 |
| --- |

## [◆ ](#ae1e035983563d473d79be122004f6d4a)ICC\_IGRPEN0\_EL1

| #define ICC\_IGRPEN0\_EL1   S3\_0\_C12\_C12\_6 |
| --- |

## [◆ ](#aeb7f0f2d77b8c2015a23e12982e35a01)ICC\_IGRPEN1\_EL1

| #define ICC\_IGRPEN1\_EL1   S3\_0\_C12\_C12\_7 |
| --- |

## [◆ ](#a75ffb5b6ea7d3a96e5d9efae9969773d)ICC\_IGRPEN1\_EL3

| #define ICC\_IGRPEN1\_EL3   S3\_6\_C12\_C12\_7 |
| --- |

## [◆ ](#a569e3c45407957f8e9b6786441dd1954)ICC\_PMR\_EL1

| #define ICC\_PMR\_EL1   S3\_0\_C4\_C6\_0 |
| --- |

## [◆ ](#ac6b780289029a1bfa5f1597272e92087)ICC\_RPR\_EL1

| #define ICC\_RPR\_EL1   S3\_0\_C12\_C11\_3 |
| --- |

## [◆ ](#a6a15fbfb9c3de076e12f6dedc1c8736b)ICC\_SGI0R\_EL1

| #define ICC\_SGI0R\_EL1   S3\_0\_C12\_C11\_7 |
| --- |

## [◆ ](#ae36e32afe169a9173e3294a807af3234)ICC\_SGI1R

| #define ICC\_SGI1R   S3\_0\_C12\_C11\_5 |
| --- |

## [◆ ](#a178411409386d40d5927250161b2c3d3)ICC\_SRE\_EL1

| #define ICC\_SRE\_EL1   S3\_0\_C12\_C12\_5 |
| --- |

## [◆ ](#a57664b4d9a0768fd26e0f9e79271d775)ICC\_SRE\_EL2

| #define ICC\_SRE\_EL2   S3\_4\_C12\_C9\_5 |
| --- |

## [◆ ](#a2aae8716b04b563cfabdeb549ec76b11)ICC\_SRE\_EL3

| #define ICC\_SRE\_EL3   S3\_6\_C12\_C12\_5 |
| --- |

## [◆ ](#a89642941ffefc853013b0f92cc80f131)ICC\_SRE\_EL3\_EN\_BIT

| #define ICC\_SRE\_EL3\_EN\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a54ea5ad3d9d0c66c5787b4c10feaeffb)ICC\_SRE\_ELx\_DFB\_BIT

| #define ICC\_SRE\_ELx\_DFB\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a6464acd03121adf32b11764b8e16a59f)ICC\_SRE\_ELx\_DIB\_BIT

| #define ICC\_SRE\_ELx\_DIB\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a581240d06f8f27d299a303941934d0a9)ICC\_SRE\_ELx\_SRE\_BIT

| #define ICC\_SRE\_ELx\_SRE\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#aacb0fe06a7e7a04c95ce845448c6d436)ID\_AA64PFR0\_EL0\_SHIFT

| #define ID\_AA64PFR0\_EL0\_SHIFT   (0) |
| --- |

## [◆ ](#a9add6e194aac9e74e71c2dc2dd025eb7)ID\_AA64PFR0\_EL1\_SHIFT

| #define ID\_AA64PFR0\_EL1\_SHIFT   (4) |
| --- |

## [◆ ](#a22dea24f7bdc4ae44c39f5aa4bcc5615)ID\_AA64PFR0\_EL2\_SHIFT

| #define ID\_AA64PFR0\_EL2\_SHIFT   (8) |
| --- |

## [◆ ](#a77322f61c0e4e872809b46b769e2ec51)ID\_AA64PFR0\_EL3\_SHIFT

| #define ID\_AA64PFR0\_EL3\_SHIFT   (12) |
| --- |

## [◆ ](#ad296dae475a3598559cb5f53d74a62b0)ID\_AA64PFR0\_ELX\_MASK

| #define ID\_AA64PFR0\_ELX\_MASK   (0xf) |
| --- |

## [◆ ](#a233d4971a3bcb773cfe17e4dbe0ee750)ID\_AA64PFR0\_SEL2\_MASK

| #define ID\_AA64PFR0\_SEL2\_MASK   (0xf) |
| --- |

## [◆ ](#a7ebf5636fdc14822cb8bbe10c7f2e1b4)ID\_AA64PFR0\_SEL2\_SHIFT

| #define ID\_AA64PFR0\_SEL2\_SHIFT   (36) |
| --- |

## [◆ ](#a9400cc2ba37e33279bdbc510a6311fb4)L1\_CACHE\_BYTES

| #define L1\_CACHE\_BYTES   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([L1\_CACHE\_SHIFT](#a29cd99f347d3f9cfccf2ea01d64b2117)) |
| --- |

## [◆ ](#a29cd99f347d3f9cfccf2ea01d64b2117)L1\_CACHE\_SHIFT

| #define L1\_CACHE\_SHIFT   (6) |
| --- |

## [◆ ](#affee69f2502d7e1b743d1fc79dd78c1d)MODE\_EL0

| #define MODE\_EL0   (0x0) |
| --- |

## [◆ ](#ad3372878ec0c895ae1c791b0ef2d24c0)MODE\_EL1

| #define MODE\_EL1   (0x1) |
| --- |

## [◆ ](#a8c3515664794ffdcd08191f5c48c3ed0)MODE\_EL2

| #define MODE\_EL2   (0x2) |
| --- |

## [◆ ](#ad51a9827564f8457d36f167593de7b83)MODE\_EL3

| #define MODE\_EL3   (0x3) |
| --- |

## [◆ ](#af57f4ebf8044288140b76f1063de6d6d)MODE\_EL\_MASK

| #define MODE\_EL\_MASK   (0x3) |
| --- |

## [◆ ](#a22ce702a54ad18a7b76edb2fb665f8fd)MODE\_EL\_SHIFT

| #define MODE\_EL\_SHIFT   (0x2) |
| --- |

## [◆ ](#a7a2087ca83455cf2759a5aee220105e2)MPIDR\_AFF0\_SHIFT

| #define MPIDR\_AFF0\_SHIFT   (0) |
| --- |

## [◆ ](#a3a7ffd9f7a014257a725513d531edab2)MPIDR\_AFF1\_SHIFT

| #define MPIDR\_AFF1\_SHIFT   (8) |
| --- |

## [◆ ](#a61d65102667e48cb00b7f9133dcd60f2)MPIDR\_AFF2\_SHIFT

| #define MPIDR\_AFF2\_SHIFT   (16) |
| --- |

## [◆ ](#adcd8397ffe05b55aec4ae2505879eed5)MPIDR\_AFF3\_SHIFT

| #define MPIDR\_AFF3\_SHIFT   (32) |
| --- |

## [◆ ](#aa64dd15e6bcb1b034ccadf54f358f02d)MPIDR\_AFF\_MASK

| #define MPIDR\_AFF\_MASK   ([GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(23, 0) | [GENMASK](group__sys-util.md#ga58530d20924859d16358c7400c37738d)(39, 32)) |
| --- |

## [◆ ](#a35278aa57b0b98cd0cb541cfea58b177)MPIDR\_AFFLVL

| #define MPIDR\_AFFLVL | ( |  | *mpidr*, |
| --- | --- | --- | --- |
|  |  |  | *aff\_level* ) |

**Value:**

(((mpidr) >> MPIDR\_AFF##aff\_level##\_SHIFT) & [MPIDR\_AFFLVL\_MASK](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#a9bce40a5c0fceea5298a899b174c3e1c))

[MPIDR\_AFFLVL\_MASK](include_2zephyr_2arch_2arm_2cortex__a__r_2cpu_8h.md#a9bce40a5c0fceea5298a899b174c3e1c)

#define MPIDR\_AFFLVL\_MASK

**Definition** cpu.h:87

## [◆ ](#a9bce40a5c0fceea5298a899b174c3e1c)MPIDR\_AFFLVL\_MASK

| #define MPIDR\_AFFLVL\_MASK   (0xffULL) |
| --- |

## [◆ ](#a850e9ad6314a72da4ef5ff09d5e1e024)MPIDR\_TO\_CORE

| #define MPIDR\_TO\_CORE | ( |  | *mpidr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(mpidr & [MPIDR\_AFF\_MASK](#aa64dd15e6bcb1b034ccadf54f358f02d))

[MPIDR\_AFF\_MASK](#aa64dd15e6bcb1b034ccadf54f358f02d)

#define MPIDR\_AFF\_MASK

**Definition** cpu.h:79

## [◆ ](#ae86fa2091d1dbac36137aa064eee7d4e)SCR\_EA\_BIT

| #define SCR\_EA\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#ad912faedaeee2519ec8207ed2d0a4704)SCR\_EEL2\_BIT

| #define SCR\_EEL2\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18) |
| --- |

## [◆ ](#a819b23e7868c4662bd4b3d19fa6eed5d)SCR\_FIQ\_BIT

| #define SCR\_FIQ\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#a547675dd8352ffb1fcfb6dec5914225a)SCR\_HCE\_BIT

| #define SCR\_HCE\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(8) |
| --- |

## [◆ ](#aae3302d2a8466a2b9a771721548e5263)SCR\_IRQ\_BIT

| #define SCR\_IRQ\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a3356501dba79206460819c2b99617a8e)SCR\_NS\_BIT

| #define SCR\_NS\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a4596599ea8aa7c7d7be74cb60319535d)SCR\_RES1

| #define SCR\_RES1   ([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5)) |
| --- |

## [◆ ](#a1ab9bded034ce4f46ead5d01b59674be)SCR\_RW\_BIT

| #define SCR\_RW\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(10) |
| --- |

## [◆ ](#a7c0a0c7d1d0865d4454b88f4ae14f45f)SCR\_SMD\_BIT

| #define SCR\_SMD\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(7) |
| --- |

## [◆ ](#a9497ad7be55a9e2afcd3033d2c2e6d03)SCR\_ST\_BIT

| #define SCR\_ST\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11) |
| --- |

## [◆ ](#ad9dc6fc20549b11dc1b2cc5ed02d5ee7)SCTLR\_A\_BIT

| #define SCTLR\_A\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

## [◆ ](#a6bbbc667734e9749f0cbb63cc3ff4341)SCTLR\_BR\_BIT

| #define SCTLR\_BR\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(17) |
| --- |

## [◆ ](#a752ac38bb53a96c6749fbfc09a1fb88d)SCTLR\_C\_BIT

| #define SCTLR\_C\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

## [◆ ](#ac53a7152c26719a8bb4d9cafdfca2045)SCTLR\_EL1\_RES1

| #define SCTLR\_EL1\_RES1 |
| --- |

**Value:**

([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(29) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(28) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23) | \

BIT(22) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(20) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(11))

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

## [◆ ](#acee5ccd8b0a2f885465442ef777c964a)SCTLR\_EL2\_RES1

| #define SCTLR\_EL2\_RES1 |
| --- |

**Value:**

([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(29) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(28) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23) | \

BIT(22) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) | \

BIT(11) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4))

## [◆ ](#aa5f1069250ab50a42e788f8eb655e0a7)SCTLR\_EL3\_RES1

| #define SCTLR\_EL3\_RES1 |
| --- |

**Value:**

([BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(29) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(28) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(23) | \

BIT(22) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(18) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(16) | \

BIT(11) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) | [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4))

## [◆ ](#ac9fd86e6613531ab567031f4c02a2900)SCTLR\_I\_BIT

| #define SCTLR\_I\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(12) |
| --- |

## [◆ ](#a223e38830566f400f6d592a6bb7dd361)SCTLR\_M\_BIT

| #define SCTLR\_M\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

## [◆ ](#a7a33d6c6dc85bc5aef0aebafa1f2f223)SCTLR\_SA\_BIT

| #define SCTLR\_SA\_BIT   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

## [◆ ](#a54fd53204f64c9081d7c0c9fc3209c37)SGIR\_AFF1\_SHIFT

| #define SGIR\_AFF1\_SHIFT   (16) |
| --- |

## [◆ ](#afcb9746b2d5edfd88af4af2759c931d7)SGIR\_AFF2\_SHIFT

| #define SGIR\_AFF2\_SHIFT   (32) |
| --- |

## [◆ ](#ac4364d68d92dd7b7e1bb7ffac6e81eef)SGIR\_AFF3\_SHIFT

| #define SGIR\_AFF3\_SHIFT   (48) |
| --- |

## [◆ ](#aaebf9f7f5e67965fac91a7eb0336f3e4)SGIR\_AFF\_MASK

| #define SGIR\_AFF\_MASK   (0xf) |
| --- |

## [◆ ](#a6e5a1e0b98322addaa87188e4d9a03f1)SGIR\_INTID\_MASK

| #define SGIR\_INTID\_MASK   (0xf) |
| --- |

## [◆ ](#a9bd0096ceb2f20d31173b61127dc5bd3)SGIR\_INTID\_SHIFT

| #define SGIR\_INTID\_SHIFT   (24) |
| --- |

## [◆ ](#a31c2a71ebf8c2e296f0c8417012ca7f4)SGIR\_IRM\_MASK

| #define SGIR\_IRM\_MASK   (0x1) |
| --- |

## [◆ ](#a0a9ae05724f25a9f9e55e664823eeb6b)SGIR\_IRM\_SHIFT

| #define SGIR\_IRM\_SHIFT   (40) |
| --- |

## [◆ ](#a410f4b9c7089a847d01bc6592335871f)SGIR\_IRM\_TO\_AFF

| #define SGIR\_IRM\_TO\_AFF   (0) |
| --- |

## [◆ ](#aef12617a687736364283ba5fc45eb29a)SGIR\_TGT\_MASK

| #define SGIR\_TGT\_MASK   (0xffff) |
| --- |

## [◆ ](#af5444cb52ad93024bf6bfd6487a9de46)SPSR\_DAIF\_MASK

| #define SPSR\_DAIF\_MASK   (0xf << [SPSR\_DAIF\_SHIFT](#a193071e5757a40fc372e0d1ab10f280f)) |
| --- |

## [◆ ](#a193071e5757a40fc372e0d1ab10f280f)SPSR\_DAIF\_SHIFT

| #define SPSR\_DAIF\_SHIFT   (6) |
| --- |

## [◆ ](#a5ac2f987d02999da93878c4b7b6a39ce)SPSR\_MODE\_EL0T

| #define SPSR\_MODE\_EL0T   (0x0) |
| --- |

## [◆ ](#afb0eeebb254ef2cd71960f9e77af181e)SPSR\_MODE\_EL1H

| #define SPSR\_MODE\_EL1H   (0x5) |
| --- |

## [◆ ](#a440d11721e78f76bd7022cc8aef83aca)SPSR\_MODE\_EL1T

| #define SPSR\_MODE\_EL1T   (0x4) |
| --- |

## [◆ ](#a3ad33c29d57e86dc7f416a6bf267d257)SPSR\_MODE\_EL2H

| #define SPSR\_MODE\_EL2H   (0x9) |
| --- |

## [◆ ](#a5c065c9fe9bbeefc64dcdda2f6c4b5bd)SPSR\_MODE\_EL2T

| #define SPSR\_MODE\_EL2T   (0x8) |
| --- |

## [◆ ](#ad42eefed5f9728f8dd454d2fad321ae3)SPSR\_MODE\_MASK

| #define SPSR\_MODE\_MASK   (0xf) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [cpu.h](include_2zephyr_2arch_2arm64_2cpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
