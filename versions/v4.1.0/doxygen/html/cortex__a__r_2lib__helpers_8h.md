---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/cortex__a__r_2lib__helpers_8h.html
original_path: doxygen/html/cortex__a__r_2lib__helpers_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lib\_helpers.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](cortex__a__r_2lib__helpers_8h_source.md)

| Macros | |
| --- | --- |
| #define | [read\_sysreg32](#a8bd3d2e84fbd96daba2f99d0c318bf5c)([op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd), CRn, CRm, op2) |
| #define | [write\_sysreg32](#a2334d77203a5d5db697773ef588839c2)(val, [op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd), CRn, CRm, op2) |
| #define | [read\_sysreg64](#a292c132843b32eae185818aeddb1cd48)([op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd), CRm) |
| #define | [write\_sysreg64](#a596118b721eb1e3184b351a2b4383485)(val, [op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd), CRm) |
| #define | [MAKE\_REG\_HELPER](#a6aa1f7b9650628c6a24b348120916803)(reg, [op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd), CRn, CRm, op2) |
| #define | [MAKE\_REG64\_HELPER](#aecef30202db40ce61d5ebb5bf4907971)(reg, [op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd), CRm) |
| #define | [write\_sysreg](#adfcf211009c840e6f89530db728f9047)(val, reg) |
| #define | [read\_sysreg](#abf4f1c14ffe7c2d5b2bfa605615e676d)(reg) |
| #define | [sev](#a544cc6885da9c2a5fb66a2a788d2ae41)() |
| #define | [wfe](#aa97b536857f20cc5b809240da5c6b0b4)() |

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [read\_mpuir](#a7c1906a10ebfe46fc20b8ded1a838f2c) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_mpuir](#aa054d6d952d2255288a58ae315f4ea0f) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [read\_mpidr](#a91b417a13806edaa706288547de78ca7) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_mpidr](#a50365519bb5082996782e33c4a288d8a) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [read\_sctlr](#aadf14247e4ae2390a06c7c198a4ee064) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_sctlr](#ac3d7864646c351c5a4d58e79d82e5701) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [read\_prselr](#a5067072ffc6359b9a0e990d60a87cb90) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_prselr](#a2e0e813eb72f5c197b8ebcbdee332d4a) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [read\_prbar](#a49d03d7caeb4025cfbe60974c42e1221) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_prbar](#a6441f60d95c4529f90d76b75d8763831) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [read\_prlar](#ab98fe50c068572436318524d47b39e8f) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_prlar](#a034c4e701cb44d2d6313d62456caa0f2) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [read\_mair0](#aff11460b159e63e224c49c1010a6e1f0) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_mair0](#a70227a021f654f610e4cbd6f9a85c9ac) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [read\_vbar](#ab9cc0f92c805971f92aa7e7ecb6c2a2f) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_vbar](#af4fb14510fe3fbca5ff6b1a04a9495df) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [read\_cntv\_ctl](#a260cf183f5aa1745e5439626e9480f48) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_cntv\_ctl](#a34fb23d53a92012ecd4c6f6a776983b4) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [read\_ctr](#ad3d02a5e9e30eac6fb4a6be8b08110c8) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_ctr](#aa79a71f23b34a15bd7c06a28e92eace8) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [read\_tpidruro](#af410cde5864b6e4997a31e2162e4873d) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_tpidruro](#ae51f64fff2bf697496af4c4053a08b85) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_ICC\_SGI1R](#aa15690fa7f43f5699611f07cd07b52aa) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_ICC\_SGI1R](#acdae584a900dbdc6ebd79814d8c3c083) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_cntvct](#aadc1c2db15fb0074e0acfb554cb26d8b) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_cntvct](#a2c5d86d059a905d92ea7820c567954da) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_cntv\_cval](#ae286bdd594c272fb2493e838ca927975) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_cntv\_cval](#a8929efdf8cc97e99983a4e3b3a32bf4b) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [read\_ICC\_PMR\_EL1](#aa8c18af48a651032f050ac9218066030) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_ICC\_PMR\_EL1](#a566c630a64b6a7933b8928c3c06b3289) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [read\_ICC\_IAR1\_EL1](#a8162a3562d7c787b977c21ae15c30301) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_ICC\_IAR1\_EL1](#a60169a3733424515bdb991d40be23deb) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [read\_ICC\_EOIR1\_EL1](#a309e98780104b76bb98ab5b1dbf867ac) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_ICC\_EOIR1\_EL1](#a9524ce710820650ee5badb3708213f59) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [read\_ICC\_SRE\_EL1](#adb4c0847f09d9601162f53b5870f573a) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_ICC\_SRE\_EL1](#a9abc55af44091bb461d5c536d5b81655) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [read\_ICC\_IGRPEN1\_EL1](#afa5bbc906e90bd7a522ea4f96be14bc0) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_ICC\_IGRPEN1\_EL1](#a1ff5837348d2f74c0ff914de29234fa3) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |

## Macro Definition Documentation

## [◆ ](#aecef30202db40ce61d5ebb5bf4907971)MAKE\_REG64\_HELPER

| #define MAKE\_REG64\_HELPER | ( |  | *reg*, |
| --- | --- | --- | --- |
|  |  |  | *[op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd)*, |
|  |  |  | *CRm* ) |

**Value:**

static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_##reg(void) \

{ \

return [read\_sysreg64](#a292c132843b32eae185818aeddb1cd48)([op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd), CRm); \

} \

static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_##reg([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) \

{ \

write\_sysreg64(val, [op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd), CRm); \

}

[op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd)

workaround assembler barfing for ST if else st aa endif endm endr macro PUSHR r push r endm macro POPR r pop r endm macro LRR aux lr aux endm macro SRR aux sr aux endm irp nz macro ADDR cc v add cc v endm endr irp nz macro ADD2R cc v add2 cc v endm endr macro ADD3R v add3 v endm macro SUBR v sub v endm macro BMSKNR v bmskn v endm macro LSRR v lsr v endm macro ASLR v asl v endm macro ANDR v and v endm macro v or v endm irp eq macro BRR cc lbl br cc lbl endm endr macro BREQR lbl breq lbl endm macro CMPR op1

**Definition** asm-macro-32-bit-gnu.h:99

[read\_sysreg64](#a292c132843b32eae185818aeddb1cd48)

#define read\_sysreg64(op1, CRm)

**Definition** lib\_helpers.h:31

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

## [◆ ](#a6aa1f7b9650628c6a24b348120916803)MAKE\_REG\_HELPER

| #define MAKE\_REG\_HELPER | ( |  | *reg*, |
| --- | --- | --- | --- |
|  |  |  | *[op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd)*, |
|  |  |  | *CRn*, |
|  |  |  | *CRm*, |
|  |  |  | *op2* ) |

**Value:**

static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) read\_##reg(void) \

{ \

return [read\_sysreg32](#a8bd3d2e84fbd96daba2f99d0c318bf5c)([op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd), CRn, CRm, op2); \

} \

static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_##reg([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) \

{ \

write\_sysreg32(val, [op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd), CRn, CRm, op2); \

}

[read\_sysreg32](#a8bd3d2e84fbd96daba2f99d0c318bf5c)

#define read\_sysreg32(op1, CRn, CRm, op2)

**Definition** lib\_helpers.h:17

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

## [◆ ](#abf4f1c14ffe7c2d5b2bfa605615e676d)read\_sysreg

| #define read\_sysreg | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

read\_##reg()

## [◆ ](#a8bd3d2e84fbd96daba2f99d0c318bf5c)read\_sysreg32

| #define read\_sysreg32 | ( |  | *[op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd)*, |
| --- | --- | --- | --- |
|  |  |  | *CRn*, |
|  |  |  | *CRm*, |
|  |  |  | *op2* ) |

**Value:**

({ \

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val; \

\_\_asm\_\_ volatile ("mrc p15, " #[op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd) ", %0, c" #CRn ", c" \

#CRm ", " #op2 : "=r" (val) :: "memory"); \

val; \

})

## [◆ ](#a292c132843b32eae185818aeddb1cd48)read\_sysreg64

| #define read\_sysreg64 | ( |  | *[op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd)*, |
| --- | --- | --- | --- |
|  |  |  | *CRm* ) |

**Value:**

({ \

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val; \

\_\_asm\_\_ volatile ("mrrc p15, " #[op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd) ", %Q0, %R0, c" \

#CRm : "=r" (val) :: "memory"); \

val; \

})

## [◆ ](#a544cc6885da9c2a5fb66a2a788d2ae41)sev

| #define sev | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

\_\_asm\_\_ volatile("sev" : : : "memory")

## [◆ ](#aa97b536857f20cc5b809240da5c6b0b4)wfe

| #define wfe | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

\_\_asm\_\_ volatile("wfe" : : : "memory")

## [◆ ](#adfcf211009c840e6f89530db728f9047)write\_sysreg

| #define write\_sysreg | ( |  | *val*, |
| --- | --- | --- | --- |
|  |  |  | *reg* ) |

**Value:**

write\_##reg(val)

## [◆ ](#a2334d77203a5d5db697773ef588839c2)write\_sysreg32

| #define write\_sysreg32 | ( |  | *val*, |
| --- | --- | --- | --- |
|  |  |  | *[op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd)*, |
|  |  |  | *CRn*, |
|  |  |  | *CRm*, |
|  |  |  | *op2* ) |

**Value:**

({ \

\_\_asm\_\_ volatile ("mcr p15, " #[op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd) ", %0, c" #CRn ", c" \

#CRm ", " #op2 :: "r" (val) : "memory"); \

})

## [◆ ](#a596118b721eb1e3184b351a2b4383485)write\_sysreg64

| #define write\_sysreg64 | ( |  | *val*, |
| --- | --- | --- | --- |
|  |  |  | *[op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd)*, |
|  |  |  | *CRm* ) |

**Value:**

({ \

\_\_asm\_\_ volatile ("mcrr p15, " #[op1](asm-macro-32-bit-gnu_8h.md#a1b3df9ba4c3032118bbf49c7c7e28edd) ", %Q0, %R0, c" \

#CRm :: "r" (val) : "memory"); \

})

## Function Documentation

## [◆ ](#a260cf183f5aa1745e5439626e9480f48)read\_cntv\_ctl()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) read\_cntv\_ctl | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ae286bdd594c272fb2493e838ca927975)read\_cntv\_cval()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_cntv\_cval | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aadc1c2db15fb0074e0acfb554cb26d8b)read\_cntvct()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_cntvct | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ad3d02a5e9e30eac6fb4a6be8b08110c8)read\_ctr()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) read\_ctr | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a309e98780104b76bb98ab5b1dbf867ac)read\_ICC\_EOIR1\_EL1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) read\_ICC\_EOIR1\_EL1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a8162a3562d7c787b977c21ae15c30301)read\_ICC\_IAR1\_EL1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) read\_ICC\_IAR1\_EL1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#afa5bbc906e90bd7a522ea4f96be14bc0)read\_ICC\_IGRPEN1\_EL1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) read\_ICC\_IGRPEN1\_EL1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aa8c18af48a651032f050ac9218066030)read\_ICC\_PMR\_EL1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) read\_ICC\_PMR\_EL1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aa15690fa7f43f5699611f07cd07b52aa)read\_ICC\_SGI1R()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_ICC\_SGI1R | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#adb4c0847f09d9601162f53b5870f573a)read\_ICC\_SRE\_EL1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) read\_ICC\_SRE\_EL1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aff11460b159e63e224c49c1010a6e1f0)read\_mair0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) read\_mair0 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a91b417a13806edaa706288547de78ca7)read\_mpidr()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) read\_mpidr | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a7c1906a10ebfe46fc20b8ded1a838f2c)read\_mpuir()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) read\_mpuir | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a49d03d7caeb4025cfbe60974c42e1221)read\_prbar()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) read\_prbar | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ab98fe50c068572436318524d47b39e8f)read\_prlar()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) read\_prlar | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a5067072ffc6359b9a0e990d60a87cb90)read\_prselr()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) read\_prselr | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aadf14247e4ae2390a06c7c198a4ee064)read\_sctlr()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) read\_sctlr | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af410cde5864b6e4997a31e2162e4873d)read\_tpidruro()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) read\_tpidruro | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ab9cc0f92c805971f92aa7e7ecb6c2a2f)read\_vbar()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) read\_vbar | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a34fb23d53a92012ecd4c6f6a776983b4)write\_cntv\_ctl()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_cntv\_ctl | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a8929efdf8cc97e99983a4e3b3a32bf4b)write\_cntv\_cval()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_cntv\_cval | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a2c5d86d059a905d92ea7820c567954da)write\_cntvct()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_cntvct | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aa79a71f23b34a15bd7c06a28e92eace8)write\_ctr()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_ctr | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a9524ce710820650ee5badb3708213f59)write\_ICC\_EOIR1\_EL1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_ICC\_EOIR1\_EL1 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a60169a3733424515bdb991d40be23deb)write\_ICC\_IAR1\_EL1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_ICC\_IAR1\_EL1 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a1ff5837348d2f74c0ff914de29234fa3)write\_ICC\_IGRPEN1\_EL1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_ICC\_IGRPEN1\_EL1 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a566c630a64b6a7933b8928c3c06b3289)write\_ICC\_PMR\_EL1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_ICC\_PMR\_EL1 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#acdae584a900dbdc6ebd79814d8c3c083)write\_ICC\_SGI1R()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_ICC\_SGI1R | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a9abc55af44091bb461d5c536d5b81655)write\_ICC\_SRE\_EL1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_ICC\_SRE\_EL1 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a70227a021f654f610e4cbd6f9a85c9ac)write\_mair0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_mair0 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a50365519bb5082996782e33c4a288d8a)write\_mpidr()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_mpidr | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aa054d6d952d2255288a58ae315f4ea0f)write\_mpuir()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_mpuir | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a6441f60d95c4529f90d76b75d8763831)write\_prbar()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_prbar | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a034c4e701cb44d2d6313d62456caa0f2)write\_prlar()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_prlar | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a2e0e813eb72f5c197b8ebcbdee332d4a)write\_prselr()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_prselr | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ac3d7864646c351c5a4d58e79d82e5701)write\_sctlr()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_sctlr | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ae51f64fff2bf697496af4c4053a08b85)write\_tpidruro()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_tpidruro | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af4fb14510fe3fbca5ff6b1a04a9495df)write\_vbar()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_vbar | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_a\_r](dir_cde462911e3dbfe61dba09f2df37ee97.md)
- [lib\_helpers.h](cortex__a__r_2lib__helpers_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
