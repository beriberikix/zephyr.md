---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/xen_8h.html
original_path: doxygen/html/xen_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xen.h File Reference

[Go to the source code of this file.](xen_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [vcpu\_time\_info](structvcpu__time__info.md) |
| struct | [vcpu\_info](structvcpu__info.md) |
| struct | [shared\_info](structshared__info.md) |
| struct | [xenctl\_bitmap](structxenctl__bitmap.md) |

| Macros | |
| --- | --- |
| #define | [XEN\_FLEX\_ARRAY\_DIM](#ae905e08d72e4466ea6a2ec669c3820e4)   1 /\* variable size \*/ |
| #define | [xen\_mk\_uint](#aa7b557e58ad4a375ce9dcccac60d7b14)(x) |
| #define | [xen\_mk\_ulong](#a81523e052b17db63279a60bef67924b4)(x) |
| #define | [xen\_mk\_ullong](#ad58e92795b2f6c186afd2848e04e39ad)(x) |
| #define | [CONSOLEIO\_write](#a37817ff1ba0005b425725c5b3cbc05e9)   0 |
| #define | [CONSOLEIO\_read](#ad4bd5e7f69e7deae12467bf88cf67556)   1 |
| #define | [DOMID\_FIRST\_RESERVED](#a9ac49a47125b5244077355a3cf2ec397)   [xen\_mk\_uint](#aa7b557e58ad4a375ce9dcccac60d7b14)(0x7FF0) |
| #define | [DOMID\_SELF](#a632d71fe6315d8b3dfcc2cad373fb7ec)   [xen\_mk\_uint](#aa7b557e58ad4a375ce9dcccac60d7b14)(0x7FF0) |
| #define | [DOMID\_IO](#ab0d934a6f32a8feb76959586dd66418c)   [xen\_mk\_uint](#aa7b557e58ad4a375ce9dcccac60d7b14)(0x7FF1) |
| #define | [DOMID\_XEN](#a4a604fcd4144dbd998b76cca7600d081)   [xen\_mk\_uint](#aa7b557e58ad4a375ce9dcccac60d7b14)(0x7FF2) |
| #define | [DOMID\_COW](#a51650c6e893bd06faf62c96c33d939d2)   [xen\_mk\_uint](#aa7b557e58ad4a375ce9dcccac60d7b14)(0x7FF3) |
| #define | [DOMID\_INVALID](#a14f066e67f10f6b886886a3befdfe6be)   [xen\_mk\_uint](#aa7b557e58ad4a375ce9dcccac60d7b14)(0x7FF4) |
| #define | [DOMID\_IDLE](#a346001069dbc3dacc7e34443b8b712b1)   [xen\_mk\_uint](#aa7b557e58ad4a375ce9dcccac60d7b14)(0x7FFF) |
| #define | [DOMID\_MASK](#a0010d63d23be20833baa50e50127bcb3)   [xen\_mk\_uint](#aa7b557e58ad4a375ce9dcccac60d7b14)(0x7FFF) |
| #define | [NR\_EVENT\_CHANNELS](#a0eaef6f49b471e8f6c9b3090ed65683a)   [EVTCHN\_2L\_NR\_CHANNELS](event__channel_8h.md#acdcf92372fa5ac60b219cd5e34d82fdf) |
| #define | [XEN\_PVCLOCK\_TSC\_STABLE\_BIT](#a3b6486848b8f26f7ebbdb4b2ac0b6f0c)   (1 << 0) |
| #define | [XEN\_PVCLOCK\_GUEST\_STOPPED](#aa63ac2404dfad1ac4828f973623896e4)   (1 << 1) |
| #define | [xen\_wc\_sec\_hi](#a9b01f685c203d17ebf84b1452d6c13fe)   wc\_sec\_hi |
| #define | [int64\_aligned\_t](#a8e346fda4301d9806f5b97d796af4d0c)   [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) |
| #define | [uint64\_aligned\_t](#ac94f3cee60964f8609932e5042590128)   [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |

| Typedefs | |
| --- | --- |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [domid\_t](#a52133e9b6faf803a509868928d1c0eee) |
| typedef struct [vcpu\_time\_info](structvcpu__time__info.md) | [vcpu\_time\_info\_t](#a46b8329725a49204352d786ce96d8b85) |
| typedef struct [vcpu\_info](structvcpu__info.md) | [vcpu\_info\_t](#a5d85cc76b763cb919c5c7d0e91d66d9f) |
| typedef struct [shared\_info](structshared__info.md) | [shared\_info\_t](#ad3890f69945f46e6904d389386df2ee1) |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [xen\_domain\_handle\_t](#a7be3933d71db9ec81444793055b5d9be)[16] |
| typedef struct [xenctl\_bitmap](structxenctl__bitmap.md) | [xenctl\_bitmap\_t](#a0b13d295ad2c74398b3430177ca6267a) |

| Functions | |
| --- | --- |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#a3271eb49ce50552a93325e44d0baea20) (char) |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#a4649270bf23be045659cecbdb6c984c5) (int) |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#aaa8e284b50677157bf7e14a060be46a3) (long) |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#a46a69b3cd5864a78bfc73762d5a2b517) (void) |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#a68bef499d4605a558eea3240a15e86ac) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)) |
|  | [DEFINE\_XEN\_GUEST\_HANDLE](#a69e56b135e0fd672f45a05b8de1b2db0) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)) |

## Macro Definition Documentation

## [◆ ](#ad4bd5e7f69e7deae12467bf88cf67556)CONSOLEIO\_read

| #define CONSOLEIO\_read   1 |
| --- |

## [◆ ](#a37817ff1ba0005b425725c5b3cbc05e9)CONSOLEIO\_write

| #define CONSOLEIO\_write   0 |
| --- |

## [◆ ](#a51650c6e893bd06faf62c96c33d939d2)DOMID\_COW

| #define DOMID\_COW   [xen\_mk\_uint](#aa7b557e58ad4a375ce9dcccac60d7b14)(0x7FF3) |
| --- |

## [◆ ](#a9ac49a47125b5244077355a3cf2ec397)DOMID\_FIRST\_RESERVED

| #define DOMID\_FIRST\_RESERVED   [xen\_mk\_uint](#aa7b557e58ad4a375ce9dcccac60d7b14)(0x7FF0) |
| --- |

## [◆ ](#a346001069dbc3dacc7e34443b8b712b1)DOMID\_IDLE

| #define DOMID\_IDLE   [xen\_mk\_uint](#aa7b557e58ad4a375ce9dcccac60d7b14)(0x7FFF) |
| --- |

## [◆ ](#a14f066e67f10f6b886886a3befdfe6be)DOMID\_INVALID

| #define DOMID\_INVALID   [xen\_mk\_uint](#aa7b557e58ad4a375ce9dcccac60d7b14)(0x7FF4) |
| --- |

## [◆ ](#ab0d934a6f32a8feb76959586dd66418c)DOMID\_IO

| #define DOMID\_IO   [xen\_mk\_uint](#aa7b557e58ad4a375ce9dcccac60d7b14)(0x7FF1) |
| --- |

## [◆ ](#a0010d63d23be20833baa50e50127bcb3)DOMID\_MASK

| #define DOMID\_MASK   [xen\_mk\_uint](#aa7b557e58ad4a375ce9dcccac60d7b14)(0x7FFF) |
| --- |

## [◆ ](#a632d71fe6315d8b3dfcc2cad373fb7ec)DOMID\_SELF

| #define DOMID\_SELF   [xen\_mk\_uint](#aa7b557e58ad4a375ce9dcccac60d7b14)(0x7FF0) |
| --- |

## [◆ ](#a4a604fcd4144dbd998b76cca7600d081)DOMID\_XEN

| #define DOMID\_XEN   [xen\_mk\_uint](#aa7b557e58ad4a375ce9dcccac60d7b14)(0x7FF2) |
| --- |

## [◆ ](#a8e346fda4301d9806f5b97d796af4d0c)int64\_aligned\_t

| #define int64\_aligned\_t   [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) |
| --- |

## [◆ ](#a0eaef6f49b471e8f6c9b3090ed65683a)NR\_EVENT\_CHANNELS

| #define NR\_EVENT\_CHANNELS   [EVTCHN\_2L\_NR\_CHANNELS](event__channel_8h.md#acdcf92372fa5ac60b219cd5e34d82fdf) |
| --- |

## [◆ ](#ac94f3cee60964f8609932e5042590128)uint64\_aligned\_t

| #define uint64\_aligned\_t   [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
| --- |

## [◆ ](#ae905e08d72e4466ea6a2ec669c3820e4)XEN\_FLEX\_ARRAY\_DIM

| #define XEN\_FLEX\_ARRAY\_DIM   1 /\* variable size \*/ |
| --- |

## [◆ ](#aa7b557e58ad4a375ce9dcccac60d7b14)xen\_mk\_uint

| #define xen\_mk\_uint | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_\_xen\_mk\_uint(x)

## [◆ ](#ad58e92795b2f6c186afd2848e04e39ad)xen\_mk\_ullong

| #define xen\_mk\_ullong | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_\_xen\_mk\_ullong(x)

## [◆ ](#a81523e052b17db63279a60bef67924b4)xen\_mk\_ulong

| #define xen\_mk\_ulong | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

\_\_xen\_mk\_ulong(x)

## [◆ ](#aa63ac2404dfad1ac4828f973623896e4)XEN\_PVCLOCK\_GUEST\_STOPPED

| #define XEN\_PVCLOCK\_GUEST\_STOPPED   (1 << 1) |
| --- |

## [◆ ](#a3b6486848b8f26f7ebbdb4b2ac0b6f0c)XEN\_PVCLOCK\_TSC\_STABLE\_BIT

| #define XEN\_PVCLOCK\_TSC\_STABLE\_BIT   (1 << 0) |
| --- |

## [◆ ](#a9b01f685c203d17ebf84b1452d6c13fe)xen\_wc\_sec\_hi

| #define xen\_wc\_sec\_hi   wc\_sec\_hi |
| --- |

## Typedef Documentation

## [◆ ](#a52133e9b6faf803a509868928d1c0eee)domid\_t

| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [domid\_t](#a52133e9b6faf803a509868928d1c0eee) |
| --- |

## [◆ ](#ad3890f69945f46e6904d389386df2ee1)shared\_info\_t

| typedef struct [shared\_info](structshared__info.md) [shared\_info\_t](#ad3890f69945f46e6904d389386df2ee1) |
| --- |

## [◆ ](#a5d85cc76b763cb919c5c7d0e91d66d9f)vcpu\_info\_t

| typedef struct [vcpu\_info](structvcpu__info.md) [vcpu\_info\_t](#a5d85cc76b763cb919c5c7d0e91d66d9f) |
| --- |

## [◆ ](#a46b8329725a49204352d786ce96d8b85)vcpu\_time\_info\_t

| typedef struct [vcpu\_time\_info](structvcpu__time__info.md) [vcpu\_time\_info\_t](#a46b8329725a49204352d786ce96d8b85) |
| --- |

## [◆ ](#a7be3933d71db9ec81444793055b5d9be)xen\_domain\_handle\_t

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) xen\_domain\_handle\_t[16] |
| --- |

## [◆ ](#a0b13d295ad2c74398b3430177ca6267a)xenctl\_bitmap\_t

| typedef struct [xenctl\_bitmap](structxenctl__bitmap.md) [xenctl\_bitmap\_t](#a0b13d295ad2c74398b3430177ca6267a) |
| --- |

## Function Documentation

## [◆ ](#a3271eb49ce50552a93325e44d0baea20)DEFINE\_XEN\_GUEST\_HANDLE() [1/6]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | char |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a4649270bf23be045659cecbdb6c984c5)DEFINE\_XEN\_GUEST\_HANDLE() [2/6]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | int |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#aaa8e284b50677157bf7e14a060be46a3)DEFINE\_XEN\_GUEST\_HANDLE() [3/6]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | long |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a69e56b135e0fd672f45a05b8de1b2db0)DEFINE\_XEN\_GUEST\_HANDLE() [4/6]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a68bef499d4605a558eea3240a15e86ac)DEFINE\_XEN\_GUEST\_HANDLE() [5/6]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a46a69b3cd5864a78bfc73762d5a2b517)DEFINE\_XEN\_GUEST\_HANDLE() [6/6]

| DEFINE\_XEN\_GUEST\_HANDLE | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [xen](dir_5d31353de41f154afd9f3c68bc3a8a3d.md)
- [public](dir_a9d090e3588b677c614b5c45cd68e13b.md)
- [xen.h](xen_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
