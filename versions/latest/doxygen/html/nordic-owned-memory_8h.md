---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nordic-owned-memory_8h.html
original_path: doxygen/html/nordic-owned-memory_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nordic-owned-memory.h File Reference

`#include <[zephyr/dt-bindings/dt-util.h](dt-util_8h_source.md)>`

[Go to the source code of this file.](nordic-owned-memory_8h_source.md)

| Macros | |
| --- | --- |
| Basic memory permission flags. | |
| #define | [NRF\_PERM\_R](#af64e25183317e21ccb2499c97d9afdff)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Readable. |
| #define | [NRF\_PERM\_W](#a0c02f911d592b79403024ff6ae924dad)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | Writable. |
| #define | [NRF\_PERM\_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Executable. |
| #define | [NRF\_PERM\_S](#a8e96aeef751fbb1c3bf2bdee474ea097)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Secure-only. |
| #define | [NRF\_PERM\_NSC](#a758490f83493121bfc04445af185efed)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
|  | Non-secure-callable. |
| Memory permission flag combinations. | |
| Note  NRF\_PERM\_NSC overrides all other flags, so it is not included here. | |
| #define | [NRF\_PERM\_RW](#ae977886b6f509bcda34b3864cf5b06e2)   ([NRF\_PERM\_R](#af64e25183317e21ccb2499c97d9afdff) | [NRF\_PERM\_W](#a0c02f911d592b79403024ff6ae924dad)) |
| #define | [NRF\_PERM\_RX](#a7de269dc15b92b49d3b865cd00dcb66e)   ([NRF\_PERM\_R](#af64e25183317e21ccb2499c97d9afdff) | [NRF\_PERM\_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2)) |
| #define | [NRF\_PERM\_RS](#adbc1087aa45ce5a82562b76e703422f6)   ([NRF\_PERM\_R](#af64e25183317e21ccb2499c97d9afdff) | [NRF\_PERM\_S](#a8e96aeef751fbb1c3bf2bdee474ea097)) |
| #define | [NRF\_PERM\_WX](#af7f291c2ca6d2c9366f123b229dcddeb)   ([NRF\_PERM\_W](#a0c02f911d592b79403024ff6ae924dad) | [NRF\_PERM\_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2)) |
| #define | [NRF\_PERM\_WS](#af7592990797753acf9e035e9a226b20a)   ([NRF\_PERM\_W](#a0c02f911d592b79403024ff6ae924dad) | [NRF\_PERM\_S](#a8e96aeef751fbb1c3bf2bdee474ea097)) |
| #define | [NRF\_PERM\_XS](#a98ec396cd8e0918c730607ee100bf76c)   ([NRF\_PERM\_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2) | [NRF\_PERM\_S](#a8e96aeef751fbb1c3bf2bdee474ea097)) |
| #define | [NRF\_PERM\_RWX](#a5e83619291670695a30b72232ba51d2d)   ([NRF\_PERM\_R](#af64e25183317e21ccb2499c97d9afdff) | [NRF\_PERM\_W](#a0c02f911d592b79403024ff6ae924dad) | [NRF\_PERM\_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2)) |
| #define | [NRF\_PERM\_RWS](#a0967ce2b4641901b0f002eb3d0134eed)   ([NRF\_PERM\_R](#af64e25183317e21ccb2499c97d9afdff) | [NRF\_PERM\_W](#a0c02f911d592b79403024ff6ae924dad) | [NRF\_PERM\_S](#a8e96aeef751fbb1c3bf2bdee474ea097)) |
| #define | [NRF\_PERM\_RXS](#aee7d5b93a610deca9a6aa66314ed664c)   ([NRF\_PERM\_R](#af64e25183317e21ccb2499c97d9afdff) | [NRF\_PERM\_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2) | [NRF\_PERM\_S](#a8e96aeef751fbb1c3bf2bdee474ea097)) |
| #define | [NRF\_PERM\_WXS](#a4b8d7cae0009bbaa43b181389ae37d01)   ([NRF\_PERM\_W](#a0c02f911d592b79403024ff6ae924dad) | [NRF\_PERM\_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2) | [NRF\_PERM\_S](#a8e96aeef751fbb1c3bf2bdee474ea097)) |
| #define | [NRF\_PERM\_RWXS](#a5ef62494ad09d23f0f2d35ffc7d7c91e)   ([NRF\_PERM\_R](#af64e25183317e21ccb2499c97d9afdff) | [NRF\_PERM\_W](#a0c02f911d592b79403024ff6ae924dad) | [NRF\_PERM\_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2) | [NRF\_PERM\_S](#a8e96aeef751fbb1c3bf2bdee474ea097)) |

## Macro Definition Documentation

## [◆ ](#a758490f83493121bfc04445af185efed)NRF\_PERM\_NSC

| #define NRF\_PERM\_NSC   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

Non-secure-callable.

## [◆ ](#af64e25183317e21ccb2499c97d9afdff)NRF\_PERM\_R

| #define NRF\_PERM\_R   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

Readable.

## [◆ ](#adbc1087aa45ce5a82562b76e703422f6)NRF\_PERM\_RS

| #define NRF\_PERM\_RS   ([NRF\_PERM\_R](#af64e25183317e21ccb2499c97d9afdff) | [NRF\_PERM\_S](#a8e96aeef751fbb1c3bf2bdee474ea097)) |
| --- |

## [◆ ](#ae977886b6f509bcda34b3864cf5b06e2)NRF\_PERM\_RW

| #define NRF\_PERM\_RW   ([NRF\_PERM\_R](#af64e25183317e21ccb2499c97d9afdff) | [NRF\_PERM\_W](#a0c02f911d592b79403024ff6ae924dad)) |
| --- |

## [◆ ](#a0967ce2b4641901b0f002eb3d0134eed)NRF\_PERM\_RWS

| #define NRF\_PERM\_RWS   ([NRF\_PERM\_R](#af64e25183317e21ccb2499c97d9afdff) | [NRF\_PERM\_W](#a0c02f911d592b79403024ff6ae924dad) | [NRF\_PERM\_S](#a8e96aeef751fbb1c3bf2bdee474ea097)) |
| --- |

## [◆ ](#a5e83619291670695a30b72232ba51d2d)NRF\_PERM\_RWX

| #define NRF\_PERM\_RWX   ([NRF\_PERM\_R](#af64e25183317e21ccb2499c97d9afdff) | [NRF\_PERM\_W](#a0c02f911d592b79403024ff6ae924dad) | [NRF\_PERM\_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2)) |
| --- |

## [◆ ](#a5ef62494ad09d23f0f2d35ffc7d7c91e)NRF\_PERM\_RWXS

| #define NRF\_PERM\_RWXS   ([NRF\_PERM\_R](#af64e25183317e21ccb2499c97d9afdff) | [NRF\_PERM\_W](#a0c02f911d592b79403024ff6ae924dad) | [NRF\_PERM\_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2) | [NRF\_PERM\_S](#a8e96aeef751fbb1c3bf2bdee474ea097)) |
| --- |

## [◆ ](#a7de269dc15b92b49d3b865cd00dcb66e)NRF\_PERM\_RX

| #define NRF\_PERM\_RX   ([NRF\_PERM\_R](#af64e25183317e21ccb2499c97d9afdff) | [NRF\_PERM\_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2)) |
| --- |

## [◆ ](#aee7d5b93a610deca9a6aa66314ed664c)NRF\_PERM\_RXS

| #define NRF\_PERM\_RXS   ([NRF\_PERM\_R](#af64e25183317e21ccb2499c97d9afdff) | [NRF\_PERM\_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2) | [NRF\_PERM\_S](#a8e96aeef751fbb1c3bf2bdee474ea097)) |
| --- |

## [◆ ](#a8e96aeef751fbb1c3bf2bdee474ea097)NRF\_PERM\_S

| #define NRF\_PERM\_S   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

Secure-only.

## [◆ ](#a0c02f911d592b79403024ff6ae924dad)NRF\_PERM\_W

| #define NRF\_PERM\_W   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

Writable.

## [◆ ](#af7592990797753acf9e035e9a226b20a)NRF\_PERM\_WS

| #define NRF\_PERM\_WS   ([NRF\_PERM\_W](#a0c02f911d592b79403024ff6ae924dad) | [NRF\_PERM\_S](#a8e96aeef751fbb1c3bf2bdee474ea097)) |
| --- |

## [◆ ](#af7f291c2ca6d2c9366f123b229dcddeb)NRF\_PERM\_WX

| #define NRF\_PERM\_WX   ([NRF\_PERM\_W](#a0c02f911d592b79403024ff6ae924dad) | [NRF\_PERM\_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2)) |
| --- |

## [◆ ](#a4b8d7cae0009bbaa43b181389ae37d01)NRF\_PERM\_WXS

| #define NRF\_PERM\_WXS   ([NRF\_PERM\_W](#a0c02f911d592b79403024ff6ae924dad) | [NRF\_PERM\_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2) | [NRF\_PERM\_S](#a8e96aeef751fbb1c3bf2bdee474ea097)) |
| --- |

## [◆ ](#a5e9cae0aa74888ed91dd7c3ffef23ec2)NRF\_PERM\_X

| #define NRF\_PERM\_X   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

Executable.

## [◆ ](#a98ec396cd8e0918c730607ee100bf76c)NRF\_PERM\_XS

| #define NRF\_PERM\_XS   ([NRF\_PERM\_X](#a5e9cae0aa74888ed91dd7c3ffef23ec2) | [NRF\_PERM\_S](#a8e96aeef751fbb1c3bf2bdee474ea097)) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reserved-memory](dir_94de8f1f6a225c49dc7403fa9fb5eacb.md)
- [nordic-owned-memory.h](nordic-owned-memory_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
