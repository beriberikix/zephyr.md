---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/4_2lib__helpers_8h.html
original_path: doxygen/html/4_2lib__helpers_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lib\_helpers.h File Reference

`#include <[zephyr/arch/arm64/cpu.h](arm64_2cpu_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](4_2lib__helpers_8h_source.md)

| Macros | |
| --- | --- |
| #define | [read\_sysreg](#abf4f1c14ffe7c2d5b2bfa605615e676d)(reg) |
| #define | [write\_sysreg](#adfcf211009c840e6f89530db728f9047)(val, reg) |
| #define | [zero\_sysreg](#a71bba9d3a17e4940df59c934c24910c2)(reg) |
| #define | [MAKE\_REG\_HELPER](#a3d4f0150b724754e8a1aaf8ca594eee1)(reg) |
| #define | [MAKE\_REG\_HELPER\_EL123](#ab0d7628d77ded016e77f75d46717ab5e)(reg) |
| #define | [sev](#a544cc6885da9c2a5fb66a2a788d2ae41)() |
| #define | [wfe](#aa97b536857f20cc5b809240da5c6b0b4)() |
| #define | [wfi](#a7a7ae42b8fd0fc5548e2bc49d20e14d3)() |

| Functions | |
| --- | --- |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_ccsidr\_el1](#ac1121f82e3e380c62f9a67c715ba8677) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_ccsidr\_el1](#a69d7c7f96e140c49b38b341c7e617af7) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_ccsidr\_el1](#a14cde62648f289f4e330653282068948) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_clidr\_el1](#a99653091c171cac6f776e2907ac3d650) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_clidr\_el1](#ae4d1fb97145fccf785ddeb98a14be5d9) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_clidr\_el1](#a5738a6628093de5b477a1fd686d1bad6) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_cntfrq\_el0](#a258a47c46f638d2d41b30cff783ac247) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_cntfrq\_el0](#a35d7aa0bb1afee4b04a3263a69551dac) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_cntfrq\_el0](#a83d8fbdb70b99aee5ab70df31ba63333) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_cnthctl\_el2](#a365533eca13537bbcc213bf3f81c99ca) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_cnthctl\_el2](#abb1a6ccdaf9971b1ee8b05980c339c77) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_cnthctl\_el2](#adc8984d71461fe51910e00372b53f5a8) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_cnthp\_ctl\_el2](#a92fe38d7dc9ff6dfe94cecd817e5e114) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_cnthp\_ctl\_el2](#a714024472aea33ecb5a5d95631dc6d75) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_cnthp\_ctl\_el2](#a448135ab8d154c27e5021e1bef0e9c1e) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_cnthps\_ctl\_el2](#a2541497f8943726a17bfc92a20db8c7b) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_cnthps\_ctl\_el2](#aadbfaf68810543c930596bfcfc58a868) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_cnthps\_ctl\_el2](#acea9c5d416e6fe66c38fcc718022782c) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_cntv\_ctl\_el0](#ab8455d86f57ccec61fa1ad6784c573f7) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_cntv\_ctl\_el0](#adf8ccef22b4bfa2378d27bbbbc13ad6e) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_cntv\_ctl\_el0](#aa8aa05240d19d14d5e70a99de4fb67f5) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_cntv\_cval\_el0](#abbcd760c3f58b5c7059fb3737532ea27) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_cntv\_cval\_el0](#afad9883e3416574fa1ddaddaf84b2c25) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_cntv\_cval\_el0](#a412856bdac39d9eed4b6ee9b317293da) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_cntvct\_el0](#a0e7c74f6816ea2107dca43a9d32de547) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_cntvct\_el0](#a45427d15cf62b055c4475e9e4e923a6b) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_cntvct\_el0](#a9cc0a9484766d3309a44e0ea12ef4b72) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_cntvoff\_el2](#a37f4664b1135f74548febe1277208d52) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_cntvoff\_el2](#a410ffdbec0b568bc91fb1af45d863b74) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_cntvoff\_el2](#a7291a4b003a0a0b51d5adefc8f6c5dca) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_currentel](#ab8bf450426e6ffd01784e74a89b368e5) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_currentel](#acc82b9473d47fe5d8b2b8a520113892d) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_currentel](#a0335454d266fe275bbfc1fb369dc180c) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_csselr\_el1](#a65b1b152322196bdbc0e62ed95d12232) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_csselr\_el1](#afe7e0a2787293ea5312ed24b2f0971aa) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_csselr\_el1](#acad4e29b5acfc5dd6de664e628b6ff0b) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_daif](#a973d6a3b1193bde3f6ac9a1724c6a00d) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_daif](#a3bbf7e8062793efc513ba6c055132263) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_daif](#a5c120f01dfacb589426c63149bbfdd59) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_hcr\_el2](#a89b8f2d4ea6411ec86d645ae1fb98aad) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_hcr\_el2](#a0a0c3d8f8fd6b314bd6c210bf1f2337d) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_hcr\_el2](#a57ad54df026a7de567ea5f38518635e8) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_id\_aa64pfr0\_el1](#a38462e114f3f2c73503e48cf02df81c6) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_id\_aa64pfr0\_el1](#ad9bc8ab4054f4bbffb46a131c0e344a8) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_id\_aa64pfr0\_el1](#a20de9972f3531bbfc5efdd18bc16ae66) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_id\_aa64mmfr0\_el1](#af4e219eb3d55882641f8094fac36b95b) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_id\_aa64mmfr0\_el1](#a4552e1a12a85044d69b6d134b7a18771) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_id\_aa64mmfr0\_el1](#a501b8e19a696c397e6c19d1ef39f8010) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_mpidr\_el1](#a91995e9b71b5f1f20dedbb03e936f72d) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_mpidr\_el1](#a487350e00ea82459f94979b398e9f088) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_mpidr\_el1](#a03fe05f9ce93c82be71057851d57833f) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_par\_el1](#a92d207ebc45d5dd145e55540c4cb9e36) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_par\_el1](#a87ce0e6b108903ab8875e324348da82c) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_par\_el1](#a0f9320e47d0b6e20fd894ecad7b486ae) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_scr\_el3](#a2ecebc3990ec0603018199b9682c0cc3) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_scr\_el3](#a325b043d46956cc563ca67a09f322daa) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_scr\_el3](#a6434e5b4d4406b1c7f946909e9192488) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_tpidrro\_el0](#a5d96400189d120420955eec6d7229490) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_tpidrro\_el0](#aee099683c4f758e63018094a6f221563) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_tpidrro\_el0](#a53ade2bfc6ec5e26f3ecd7fd75b3b277) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_vmpidr\_el2](#ae946a95c234051b71c028d2b7d9de0e8) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_vmpidr\_el2](#a4c3c4d5ad024916f9aa0fb1ad177b6ef) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_vmpidr\_el2](#ab5800085de000d3b0f0f0b1e09cacfe1) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_sp\_el0](#abe1d7328798802e0d21d2ff4872dcafe) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_sp\_el0](#a2cb8140538ac8390a5f72115512a8e07) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_sp\_el0](#aeede39e9c92abbeafe7226ce3e979b52) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_actlr\_el1](#a4c6d250f1d7fa3d6e29f2f2ba72e4814) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_actlr\_el1](#a8aa8fdcb8fe293d15f62b7f0deee8a41) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_actlr\_el1](#a9d0a4c92976b7169af4d8632cf76a908) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_actlr\_el2](#a9b690ee14a041d3815015db78ef2994c) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_actlr\_el2](#a8352b4da96bcee9bb718659eae3791ea) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_actlr\_el2](#a544291a0aed0b6fd63cbc10ca511dd4e) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_actlr\_el3](#a60b2891b3f4feccdafd89efff810132c) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_actlr\_el3](#ae1b8ab86193d13da31ce8609dffd2ffe) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_actlr\_el3](#ad4cbd8cea7f279d4556d18a5a0de035f) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_cpacr\_el1](#af51b5eb362da6a7b8a68d2fb2ddbe453) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_cpacr\_el1](#a69a917ab47af90eb5744623250446af5) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_cpacr\_el1](#afdab5fb96d87973187821af88ef6614a) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_cpacr\_el2](#a768c451e07a00a250ef22f50524dd35c) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_cpacr\_el2](#ac825cd67ad050c355733e55e39a2ecbc) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_cpacr\_el2](#a3d227735ad0ce38beba2a7b38f64a53e) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_cpacr\_el3](#a46f6ab26786a3515a5ddc9b761c07408) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_cpacr\_el3](#ae6485ccf2d334dc1e2b8a9161bcd6271) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_cpacr\_el3](#aba83d3adaa1a6f1ee0d7d16e85693164) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_cptr\_el1](#a349cf93efd70254bd3e5fbef197cc052) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_cptr\_el1](#a2a52b387093a15bc16372aa33913cb70) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_cptr\_el1](#af92cb1be4eabd19500705f4edad0e633) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_cptr\_el2](#ad1bfb1720637b0259c01bc3142851ffb) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_cptr\_el2](#af190b3db0352916f2809745e53487267) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_cptr\_el2](#afe907102e849035a4e7a6cbb45cb82cf) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_cptr\_el3](#a76819d2ea73b46842e751e194f976840) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_cptr\_el3](#a792fbf15e186506cab26eb22ccc9b2ec) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_cptr\_el3](#ab69b4a9149bda5f3749841dbd8565153) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_elr\_el1](#a2a485cffc625f93557920bf4133aece1) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_elr\_el1](#a62b89f6766e11b47d148f600ada1e0b7) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_elr\_el1](#aba615d905fb7dce97b21f2d3945160da) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_elr\_el2](#acb32272255120b6fb98cdf7afe9fc1f9) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_elr\_el2](#af52591ad36e3a834ad17792e9198e2b5) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_elr\_el2](#ad58df1b3866b2c56303367da1e0306a8) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_elr\_el3](#a5596c14a0cc28a56a1e77497afd412c8) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_elr\_el3](#ab8bfe0a084b886f6783f3fd8812e66f3) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_elr\_el3](#a7ddbe89d4f6dca3149b241ad63fd17a7) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_esr\_el1](#a76bd170ab59044a86a84104860eed913) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_esr\_el1](#a9f69d808c4f3f2d0b819f30785566a1c) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_esr\_el1](#ad567d2f1d4318e0ad33769bf57d4728a) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_esr\_el2](#a8b70971bea10abb4dc434a057f0bec47) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_esr\_el2](#aecfd7eb47152ba59bc1c30db588e46c7) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_esr\_el2](#a04965615eb6b62d5db385ecf5eb7ca5e) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_esr\_el3](#a09c58f75e62992ece44186546e4936c2) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_esr\_el3](#a2206ea96626169ee4e814dbbd1a542d9) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_esr\_el3](#aaa751dce577da4b34856a02ae07f70ce) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_far\_el1](#a79b816489c74dbd265c09756022c122b) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_far\_el1](#a53fb6d83968c448b7c539c74dba5b2af) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_far\_el1](#a80db586ae600d6b16c3bdeaa9a0bead5) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_far\_el2](#a3ad412c3b0c9bef70bfd01fe20d79344) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_far\_el2](#a28348f33d3a5dd8c4478eb42f798d4ab) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_far\_el2](#a4373a039fcb45de9ed994899ca3ea5fd) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_far\_el3](#ac6e6f9531e2fb93dc94c226a0ce93c49) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_far\_el3](#a80e46e553a7811f6c286deaed78a3d52) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_far\_el3](#add7899adce220589e834f1c96085a080) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_mair\_el1](#a84567a9ef9c0acae2f49504794f05d22) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_mair\_el1](#af569665d8e20d9c9a37cdc572cc217e7) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_mair\_el1](#a877cf34c4e464127d5d0f973c74e3bd2) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_mair\_el2](#ad24dfb569f7f6a235511d438f9aadc28) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_mair\_el2](#aecfebdc7395f961310597d1a33b97164) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_mair\_el2](#aef3c4bbd1bc5d0e35bcf237d91aff4bf) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_mair\_el3](#a0109ebab807b11a74dc01da6b5418820) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_mair\_el3](#a6ce57ebd1a955e7a1ec683342a425936) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_mair\_el3](#a55841460807ef7be743a01bd5fe79a85) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_sctlr\_el1](#a2c94db4a9a4365c193d8f62566777369) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_sctlr\_el1](#a89a094ead38316e3a7ee3f43ab186091) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_sctlr\_el1](#af22552720c6ce81f89e5723fe477b828) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_sctlr\_el2](#aa586788d9bb66c40643b57725a99aec9) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_sctlr\_el2](#a4deaeeb3074ba0d853f1b5c53b95bd80) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_sctlr\_el2](#a2a189bbf13c45fa8005fa7dc402e9f9f) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_sctlr\_el3](#a3291ccf18f214e63b2f56c257a6e2255) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_sctlr\_el3](#aae8f2906e499aa76c989314bddf8a45a) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_sctlr\_el3](#a75ea7c1920c095ed1ea51427d3b9f691) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_spsr\_el1](#ab4ca33b42893a69e295387244ff9ee66) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_spsr\_el1](#ae10a5978a5b0015eef62d9f487e8444f) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_spsr\_el1](#ac7909e27205fd526b6dc921d88e0aea8) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_spsr\_el2](#a260fc6052c73a2805579086ef33a7733) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_spsr\_el2](#a12d09c737b0e4b6537212bbf30117892) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_spsr\_el2](#a6400f2fb4d0c473db6bce81e6bcd8d18) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_spsr\_el3](#a85b1d0825098a77fea9cb567053df4d1) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_spsr\_el3](#a63ea0a62b8bc790ee5ba984494ee28bb) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_spsr\_el3](#aed0c4b734bb27fb8e439bdeee11b1a03) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_tcr\_el1](#a77716d5dbbee548d5c7864c48efd9929) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_tcr\_el1](#a371e0d676ade2055348ac018f7f091b6) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_tcr\_el1](#acadfba11f4bef94472510ba611f451d7) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_tcr\_el2](#ae617c61f5e18ac8caf03e0bd5b0f49fa) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_tcr\_el2](#a896dbe3a27e4b913ad6c8a35068d5c1c) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_tcr\_el2](#aa7dd303c9422ebfeacdecac6e3dae683) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_tcr\_el3](#ac6c620ea4b3ed8bf7af9733664adba8c) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_tcr\_el3](#a8ab8e25afe9fd91e8a407afb47d54508) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_tcr\_el3](#a0d6badd9b7e7349d96065fe766008912) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_ttbr0\_el1](#a90c8f409355b33084a8976c9cf88d957) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_ttbr0\_el1](#a47619879d80836f7f77a9ca59a246ab2) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_ttbr0\_el1](#a818f887e590c29f38e9f4bf4cba3b058) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_ttbr0\_el2](#a371af9697c0c4b59a03c7d27aade2ead) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_ttbr0\_el2](#a2b0654ef1f97f05daa093106b234b674) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_ttbr0\_el2](#a764d074cdadfc74bb2f5d8cb8a3dcf3a) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_ttbr0\_el3](#a023dc1e9efae5f2cbafc8dfe76bde84a) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_ttbr0\_el3](#a0480d1ddda7dc72f817fab5b3a77ed11) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_ttbr0\_el3](#ac7a66025567c1c99bc6618760e054b96) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_vbar\_el1](#a32582c152b47e0a3119ce4f2421850d9) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_vbar\_el1](#a94d9e0f3102f6fdfa5cf64ab69547415) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_vbar\_el1](#af090c3b30e472a3bacf168b495d4e61d) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_vbar\_el2](#aad58f52530f463606c8c1af4307e3451) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_vbar\_el2](#a874f08fb167087e04682f099f28f19fd) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_vbar\_el2](#ac4250db263683908b1b9390961d4a97b) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [read\_vbar\_el3](#ad9f172e0a58a7f40eed6ea16d470a654) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [write\_vbar\_el3](#a90788687be53ee9437f396d121b1a8c3) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [zero\_vbar\_el3](#a061496958b38c81bfad70838d76f186b) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [enable\_debug\_exceptions](#aa10827ab07d53a97a2a0eef88a34cdc1) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [disable\_debug\_exceptions](#a6124913695b3152818ca0c8338145522) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [enable\_serror\_exceptions](#ab6fafccc9d37b2b9af7ec37a4bbfea92) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [disable\_serror\_exceptions](#a316d3a4385241a3ff7032a8d34067a38) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [enable\_irq](#a9519288643c3060570256bc125cbbeaf) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [disable\_irq](#a86526fa2425a30ae46957d0480a09f25) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [enable\_fiq](#acca0372b859951afad2cc70c1ef9742f) (void) |
| static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void | [disable\_fiq](#a971a94499a6e9949d79305c234329a10) (void) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_el\_implemented](#a666bed8ddc768e8c5b75a1cb2d270df1) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int el) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_el\_highest\_implemented](#a819e9a0d12d5273f526f0485600e7c28) (void) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_el2\_sec\_supported](#aff5c60debe8b01feaf857df6940d9e28) (void) |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [is\_in\_secure\_state](#af264946ff140207b02cfca1957da610d) (void) |

## Macro Definition Documentation

## [◆ ](#a3d4f0150b724754e8a1aaf8ca594eee1)MAKE\_REG\_HELPER

| #define MAKE\_REG\_HELPER | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_##reg(void) \

{ \

return [read\_sysreg](cortex__a__r_2lib__helpers_8h.md#abf4f1c14ffe7c2d5b2bfa605615e676d)(reg); \

} \

static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_##reg([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val) \

{ \

write\_sysreg(val, reg); \

} \

static [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_##reg(void) \

{ \

zero\_sysreg(reg); \

}

[read\_sysreg](cortex__a__r_2lib__helpers_8h.md#abf4f1c14ffe7c2d5b2bfa605615e676d)

#define read\_sysreg(reg)

**Definition** lib\_helpers.h:100

[ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a)

#define ALWAYS\_INLINE

**Definition** common.h:129

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

## [◆ ](#ab0d7628d77ded016e77f75d46717ab5e)MAKE\_REG\_HELPER\_EL123

| #define MAKE\_REG\_HELPER\_EL123 | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)(reg##\_el1) \

MAKE\_REG\_HELPER(reg##\_el2) \

MAKE\_REG\_HELPER(reg##\_el3)

[MAKE\_REG\_HELPER](cortex__a__r_2lib__helpers_8h.md#a6aa1f7b9650628c6a24b348120916803)

#define MAKE\_REG\_HELPER(reg, op1, CRn, CRm, op2)

**Definition** lib\_helpers.h:45

## [◆ ](#abf4f1c14ffe7c2d5b2bfa605615e676d)read\_sysreg

| #define read\_sysreg | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

({ \

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) reg\_val; \

\_\_asm\_\_ volatile ("mrs %0, " [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(reg) \

: "=r" (reg\_val) :: "memory"); \

reg\_val; \

})

[STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

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

## [◆ ](#a7a7ae42b8fd0fc5548e2bc49d20e14d3)wfi

| #define wfi | ( |  | ) |  |
| --- | --- | --- | --- | --- |

**Value:**

\_\_asm\_\_ volatile("wfi" : : : "memory")

## [◆ ](#adfcf211009c840e6f89530db728f9047)write\_sysreg

| #define write\_sysreg | ( |  | *val*, |
| --- | --- | --- | --- |
|  |  |  | *reg* ) |

**Value:**

({ \

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) reg\_val = val; \

\_\_asm\_\_ volatile ("msr " [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(reg) ", %0" \

:: "r" (reg\_val) : "memory"); \

})

## [◆ ](#a71bba9d3a17e4940df59c934c24910c2)zero\_sysreg

| #define zero\_sysreg | ( |  | *reg* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

({ \

\_\_asm\_\_ volatile ("msr " [STRINGIFY](include_2zephyr_2toolchain_2common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(reg) ", xzr" \

::: "memory"); \

})

## Function Documentation

## [◆ ](#a6124913695b3152818ca0c8338145522)disable\_debug\_exceptions()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void disable\_debug\_exceptions | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a971a94499a6e9949d79305c234329a10)disable\_fiq()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void disable\_fiq | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a86526fa2425a30ae46957d0480a09f25)disable\_irq()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void disable\_irq | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a316d3a4385241a3ff7032a8d34067a38)disable\_serror\_exceptions()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void disable\_serror\_exceptions | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aa10827ab07d53a97a2a0eef88a34cdc1)enable\_debug\_exceptions()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void enable\_debug\_exceptions | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#acca0372b859951afad2cc70c1ef9742f)enable\_fiq()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void enable\_fiq | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a9519288643c3060570256bc125cbbeaf)enable\_irq()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void enable\_irq | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ab6fafccc9d37b2b9af7ec37a4bbfea92)enable\_serror\_exceptions()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void enable\_serror\_exceptions | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aff5c60debe8b01feaf857df6940d9e28)is\_el2\_sec\_supported()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_el2\_sec\_supported | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a819e9a0d12d5273f526f0485600e7c28)is\_el\_highest\_implemented()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_el\_highest\_implemented | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a666bed8ddc768e8c5b75a1cb2d270df1)is\_el\_implemented()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_el\_implemented | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *el* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af264946ff140207b02cfca1957da610d)is\_in\_secure\_state()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_in\_secure\_state | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a4c6d250f1d7fa3d6e29f2f2ba72e4814)read\_actlr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_actlr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a9b690ee14a041d3815015db78ef2994c)read\_actlr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_actlr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a60b2891b3f4feccdafd89efff810132c)read\_actlr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_actlr\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ac1121f82e3e380c62f9a67c715ba8677)read\_ccsidr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_ccsidr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a99653091c171cac6f776e2907ac3d650)read\_clidr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_clidr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a258a47c46f638d2d41b30cff783ac247)read\_cntfrq\_el0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_cntfrq\_el0 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a365533eca13537bbcc213bf3f81c99ca)read\_cnthctl\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_cnthctl\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a92fe38d7dc9ff6dfe94cecd817e5e114)read\_cnthp\_ctl\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_cnthp\_ctl\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a2541497f8943726a17bfc92a20db8c7b)read\_cnthps\_ctl\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_cnthps\_ctl\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ab8455d86f57ccec61fa1ad6784c573f7)read\_cntv\_ctl\_el0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_cntv\_ctl\_el0 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#abbcd760c3f58b5c7059fb3737532ea27)read\_cntv\_cval\_el0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_cntv\_cval\_el0 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a0e7c74f6816ea2107dca43a9d32de547)read\_cntvct\_el0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_cntvct\_el0 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a37f4664b1135f74548febe1277208d52)read\_cntvoff\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_cntvoff\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af51b5eb362da6a7b8a68d2fb2ddbe453)read\_cpacr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_cpacr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a768c451e07a00a250ef22f50524dd35c)read\_cpacr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_cpacr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a46f6ab26786a3515a5ddc9b761c07408)read\_cpacr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_cpacr\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a349cf93efd70254bd3e5fbef197cc052)read\_cptr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_cptr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ad1bfb1720637b0259c01bc3142851ffb)read\_cptr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_cptr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a76819d2ea73b46842e751e194f976840)read\_cptr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_cptr\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a65b1b152322196bdbc0e62ed95d12232)read\_csselr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_csselr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ab8bf450426e6ffd01784e74a89b368e5)read\_currentel()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_currentel | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a973d6a3b1193bde3f6ac9a1724c6a00d)read\_daif()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_daif | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a2a485cffc625f93557920bf4133aece1)read\_elr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_elr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#acb32272255120b6fb98cdf7afe9fc1f9)read\_elr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_elr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a5596c14a0cc28a56a1e77497afd412c8)read\_elr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_elr\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a76bd170ab59044a86a84104860eed913)read\_esr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_esr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a8b70971bea10abb4dc434a057f0bec47)read\_esr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_esr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a09c58f75e62992ece44186546e4936c2)read\_esr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_esr\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a79b816489c74dbd265c09756022c122b)read\_far\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_far\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a3ad412c3b0c9bef70bfd01fe20d79344)read\_far\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_far\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ac6e6f9531e2fb93dc94c226a0ce93c49)read\_far\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_far\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a89b8f2d4ea6411ec86d645ae1fb98aad)read\_hcr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_hcr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af4e219eb3d55882641f8094fac36b95b)read\_id\_aa64mmfr0\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_id\_aa64mmfr0\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a38462e114f3f2c73503e48cf02df81c6)read\_id\_aa64pfr0\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_id\_aa64pfr0\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a84567a9ef9c0acae2f49504794f05d22)read\_mair\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_mair\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ad24dfb569f7f6a235511d438f9aadc28)read\_mair\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_mair\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a0109ebab807b11a74dc01da6b5418820)read\_mair\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_mair\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a91995e9b71b5f1f20dedbb03e936f72d)read\_mpidr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_mpidr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a92d207ebc45d5dd145e55540c4cb9e36)read\_par\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_par\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a2ecebc3990ec0603018199b9682c0cc3)read\_scr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_scr\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a2c94db4a9a4365c193d8f62566777369)read\_sctlr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_sctlr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aa586788d9bb66c40643b57725a99aec9)read\_sctlr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_sctlr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a3291ccf18f214e63b2f56c257a6e2255)read\_sctlr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_sctlr\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#abe1d7328798802e0d21d2ff4872dcafe)read\_sp\_el0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_sp\_el0 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ab4ca33b42893a69e295387244ff9ee66)read\_spsr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_spsr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a260fc6052c73a2805579086ef33a7733)read\_spsr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_spsr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a85b1d0825098a77fea9cb567053df4d1)read\_spsr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_spsr\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a77716d5dbbee548d5c7864c48efd9929)read\_tcr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_tcr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ae617c61f5e18ac8caf03e0bd5b0f49fa)read\_tcr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_tcr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ac6c620ea4b3ed8bf7af9733664adba8c)read\_tcr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_tcr\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a5d96400189d120420955eec6d7229490)read\_tpidrro\_el0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_tpidrro\_el0 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a90c8f409355b33084a8976c9cf88d957)read\_ttbr0\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_ttbr0\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a371af9697c0c4b59a03c7d27aade2ead)read\_ttbr0\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_ttbr0\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a023dc1e9efae5f2cbafc8dfe76bde84a)read\_ttbr0\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_ttbr0\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a32582c152b47e0a3119ce4f2421850d9)read\_vbar\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_vbar\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aad58f52530f463606c8c1af4307e3451)read\_vbar\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_vbar\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ad9f172e0a58a7f40eed6ea16d470a654)read\_vbar\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_vbar\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ae946a95c234051b71c028d2b7d9de0e8)read\_vmpidr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) read\_vmpidr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a8aa8fdcb8fe293d15f62b7f0deee8a41)write\_actlr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_actlr\_el1 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a8352b4da96bcee9bb718659eae3791ea)write\_actlr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_actlr\_el2 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ae1b8ab86193d13da31ce8609dffd2ffe)write\_actlr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_actlr\_el3 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a69d7c7f96e140c49b38b341c7e617af7)write\_ccsidr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_ccsidr\_el1 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ae4d1fb97145fccf785ddeb98a14be5d9)write\_clidr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_clidr\_el1 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a35d7aa0bb1afee4b04a3263a69551dac)write\_cntfrq\_el0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_cntfrq\_el0 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#abb1a6ccdaf9971b1ee8b05980c339c77)write\_cnthctl\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_cnthctl\_el2 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a714024472aea33ecb5a5d95631dc6d75)write\_cnthp\_ctl\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_cnthp\_ctl\_el2 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aadbfaf68810543c930596bfcfc58a868)write\_cnthps\_ctl\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_cnthps\_ctl\_el2 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#adf8ccef22b4bfa2378d27bbbbc13ad6e)write\_cntv\_ctl\_el0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_cntv\_ctl\_el0 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#afad9883e3416574fa1ddaddaf84b2c25)write\_cntv\_cval\_el0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_cntv\_cval\_el0 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a45427d15cf62b055c4475e9e4e923a6b)write\_cntvct\_el0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_cntvct\_el0 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a410ffdbec0b568bc91fb1af45d863b74)write\_cntvoff\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_cntvoff\_el2 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a69a917ab47af90eb5744623250446af5)write\_cpacr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_cpacr\_el1 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ac825cd67ad050c355733e55e39a2ecbc)write\_cpacr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_cpacr\_el2 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ae6485ccf2d334dc1e2b8a9161bcd6271)write\_cpacr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_cpacr\_el3 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a2a52b387093a15bc16372aa33913cb70)write\_cptr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_cptr\_el1 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af190b3db0352916f2809745e53487267)write\_cptr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_cptr\_el2 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a792fbf15e186506cab26eb22ccc9b2ec)write\_cptr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_cptr\_el3 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#afe7e0a2787293ea5312ed24b2f0971aa)write\_csselr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_csselr\_el1 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#acc82b9473d47fe5d8b2b8a520113892d)write\_currentel()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_currentel | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a3bbf7e8062793efc513ba6c055132263)write\_daif()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_daif | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a62b89f6766e11b47d148f600ada1e0b7)write\_elr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_elr\_el1 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af52591ad36e3a834ad17792e9198e2b5)write\_elr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_elr\_el2 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ab8bfe0a084b886f6783f3fd8812e66f3)write\_elr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_elr\_el3 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a9f69d808c4f3f2d0b819f30785566a1c)write\_esr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_esr\_el1 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aecfd7eb47152ba59bc1c30db588e46c7)write\_esr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_esr\_el2 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a2206ea96626169ee4e814dbbd1a542d9)write\_esr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_esr\_el3 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a53fb6d83968c448b7c539c74dba5b2af)write\_far\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_far\_el1 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a28348f33d3a5dd8c4478eb42f798d4ab)write\_far\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_far\_el2 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a80e46e553a7811f6c286deaed78a3d52)write\_far\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_far\_el3 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a0a0c3d8f8fd6b314bd6c210bf1f2337d)write\_hcr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_hcr\_el2 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a4552e1a12a85044d69b6d134b7a18771)write\_id\_aa64mmfr0\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_id\_aa64mmfr0\_el1 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ad9bc8ab4054f4bbffb46a131c0e344a8)write\_id\_aa64pfr0\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_id\_aa64pfr0\_el1 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af569665d8e20d9c9a37cdc572cc217e7)write\_mair\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_mair\_el1 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aecfebdc7395f961310597d1a33b97164)write\_mair\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_mair\_el2 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a6ce57ebd1a955e7a1ec683342a425936)write\_mair\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_mair\_el3 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a487350e00ea82459f94979b398e9f088)write\_mpidr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_mpidr\_el1 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a87ce0e6b108903ab8875e324348da82c)write\_par\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_par\_el1 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a325b043d46956cc563ca67a09f322daa)write\_scr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_scr\_el3 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a89a094ead38316e3a7ee3f43ab186091)write\_sctlr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_sctlr\_el1 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a4deaeeb3074ba0d853f1b5c53b95bd80)write\_sctlr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_sctlr\_el2 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aae8f2906e499aa76c989314bddf8a45a)write\_sctlr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_sctlr\_el3 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a2cb8140538ac8390a5f72115512a8e07)write\_sp\_el0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_sp\_el0 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ae10a5978a5b0015eef62d9f487e8444f)write\_spsr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_spsr\_el1 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a12d09c737b0e4b6537212bbf30117892)write\_spsr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_spsr\_el2 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a63ea0a62b8bc790ee5ba984494ee28bb)write\_spsr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_spsr\_el3 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a371e0d676ade2055348ac018f7f091b6)write\_tcr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_tcr\_el1 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a896dbe3a27e4b913ad6c8a35068d5c1c)write\_tcr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_tcr\_el2 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a8ab8e25afe9fd91e8a407afb47d54508)write\_tcr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_tcr\_el3 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aee099683c4f758e63018094a6f221563)write\_tpidrro\_el0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_tpidrro\_el0 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a47619879d80836f7f77a9ca59a246ab2)write\_ttbr0\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_ttbr0\_el1 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a2b0654ef1f97f05daa093106b234b674)write\_ttbr0\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_ttbr0\_el2 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a0480d1ddda7dc72f817fab5b3a77ed11)write\_ttbr0\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_ttbr0\_el3 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a94d9e0f3102f6fdfa5cf64ab69547415)write\_vbar\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_vbar\_el1 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a874f08fb167087e04682f099f28f19fd)write\_vbar\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_vbar\_el2 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a90788687be53ee9437f396d121b1a8c3)write\_vbar\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_vbar\_el3 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a4c3c4d5ad024916f9aa0fb1ad177b6ef)write\_vmpidr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void write\_vmpidr\_el2 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val* | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a9d0a4c92976b7169af4d8632cf76a908)zero\_actlr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_actlr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a544291a0aed0b6fd63cbc10ca511dd4e)zero\_actlr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_actlr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ad4cbd8cea7f279d4556d18a5a0de035f)zero\_actlr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_actlr\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a14cde62648f289f4e330653282068948)zero\_ccsidr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_ccsidr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a5738a6628093de5b477a1fd686d1bad6)zero\_clidr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_clidr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a83d8fbdb70b99aee5ab70df31ba63333)zero\_cntfrq\_el0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_cntfrq\_el0 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#adc8984d71461fe51910e00372b53f5a8)zero\_cnthctl\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_cnthctl\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a448135ab8d154c27e5021e1bef0e9c1e)zero\_cnthp\_ctl\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_cnthp\_ctl\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#acea9c5d416e6fe66c38fcc718022782c)zero\_cnthps\_ctl\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_cnthps\_ctl\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aa8aa05240d19d14d5e70a99de4fb67f5)zero\_cntv\_ctl\_el0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_cntv\_ctl\_el0 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a412856bdac39d9eed4b6ee9b317293da)zero\_cntv\_cval\_el0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_cntv\_cval\_el0 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a9cc0a9484766d3309a44e0ea12ef4b72)zero\_cntvct\_el0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_cntvct\_el0 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a7291a4b003a0a0b51d5adefc8f6c5dca)zero\_cntvoff\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_cntvoff\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#afdab5fb96d87973187821af88ef6614a)zero\_cpacr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_cpacr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a3d227735ad0ce38beba2a7b38f64a53e)zero\_cpacr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_cpacr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aba83d3adaa1a6f1ee0d7d16e85693164)zero\_cpacr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_cpacr\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af92cb1be4eabd19500705f4edad0e633)zero\_cptr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_cptr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#afe907102e849035a4e7a6cbb45cb82cf)zero\_cptr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_cptr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ab69b4a9149bda5f3749841dbd8565153)zero\_cptr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_cptr\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#acad4e29b5acfc5dd6de664e628b6ff0b)zero\_csselr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_csselr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a0335454d266fe275bbfc1fb369dc180c)zero\_currentel()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_currentel | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a5c120f01dfacb589426c63149bbfdd59)zero\_daif()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_daif | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aba615d905fb7dce97b21f2d3945160da)zero\_elr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_elr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ad58df1b3866b2c56303367da1e0306a8)zero\_elr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_elr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a7ddbe89d4f6dca3149b241ad63fd17a7)zero\_elr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_elr\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ad567d2f1d4318e0ad33769bf57d4728a)zero\_esr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_esr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a04965615eb6b62d5db385ecf5eb7ca5e)zero\_esr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_esr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aaa751dce577da4b34856a02ae07f70ce)zero\_esr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_esr\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a80db586ae600d6b16c3bdeaa9a0bead5)zero\_far\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_far\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a4373a039fcb45de9ed994899ca3ea5fd)zero\_far\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_far\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#add7899adce220589e834f1c96085a080)zero\_far\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_far\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a57ad54df026a7de567ea5f38518635e8)zero\_hcr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_hcr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a501b8e19a696c397e6c19d1ef39f8010)zero\_id\_aa64mmfr0\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_id\_aa64mmfr0\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a20de9972f3531bbfc5efdd18bc16ae66)zero\_id\_aa64pfr0\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_id\_aa64pfr0\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a877cf34c4e464127d5d0f973c74e3bd2)zero\_mair\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_mair\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aef3c4bbd1bc5d0e35bcf237d91aff4bf)zero\_mair\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_mair\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a55841460807ef7be743a01bd5fe79a85)zero\_mair\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_mair\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a03fe05f9ce93c82be71057851d57833f)zero\_mpidr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_mpidr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a0f9320e47d0b6e20fd894ecad7b486ae)zero\_par\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_par\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a6434e5b4d4406b1c7f946909e9192488)zero\_scr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_scr\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af22552720c6ce81f89e5723fe477b828)zero\_sctlr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_sctlr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a2a189bbf13c45fa8005fa7dc402e9f9f)zero\_sctlr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_sctlr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a75ea7c1920c095ed1ea51427d3b9f691)zero\_sctlr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_sctlr\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aeede39e9c92abbeafe7226ce3e979b52)zero\_sp\_el0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_sp\_el0 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ac7909e27205fd526b6dc921d88e0aea8)zero\_spsr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_spsr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a6400f2fb4d0c473db6bce81e6bcd8d18)zero\_spsr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_spsr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aed0c4b734bb27fb8e439bdeee11b1a03)zero\_spsr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_spsr\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#acadfba11f4bef94472510ba611f451d7)zero\_tcr\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_tcr\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#aa7dd303c9422ebfeacdecac6e3dae683)zero\_tcr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_tcr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a0d6badd9b7e7349d96065fe766008912)zero\_tcr\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_tcr\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a53ade2bfc6ec5e26f3ecd7fd75b3b277)zero\_tpidrro\_el0()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_tpidrro\_el0 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a818f887e590c29f38e9f4bf4cba3b058)zero\_ttbr0\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_ttbr0\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a764d074cdadfc74bb2f5d8cb8a3dcf3a)zero\_ttbr0\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_ttbr0\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ac7a66025567c1c99bc6618760e054b96)zero\_ttbr0\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_ttbr0\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#af090c3b30e472a3bacf168b495d4e61d)zero\_vbar\_el1()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_vbar\_el1 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ac4250db263683908b1b9390961d4a97b)zero\_vbar\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_vbar\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a061496958b38c81bfad70838d76f186b)zero\_vbar\_el3()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_vbar\_el3 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ab5800085de000d3b0f0f0b1e09cacfe1)zero\_vmpidr\_el2()

| | [ALWAYS\_INLINE](include_2zephyr_2toolchain_2common_8h.md#aa1dec568e79152c892dcf63f445cbd7a) void zero\_vmpidr\_el2 | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | static |
| --- | --- | --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm64](dir_6230441082867cc38c6cd25597cf0dd8.md)
- [lib\_helpers.h](4_2lib__helpers_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
