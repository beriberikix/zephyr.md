---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arm_2cortex__a__r_2mpu_8h.html
original_path: doxygen/html/arm_2cortex__a__r_2mpu_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mpu.h File Reference

[Go to the source code of this file.](arm_2cortex__a__r_2mpu_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MPU\_RBAR\_ADDR\_Msk](#a33905dca89aa5b5bb9aa9518094b8b80)   (~0x1f) |
| #define | [MPU\_RASR\_ENABLE\_Msk](#af6c4850fc33a5f13a42cf25dbce72646)   (1) |
| #define | [MPU\_RASR\_SIZE\_Pos](#ad90549193db0d2b7e70d3d52cb902710)   1U |
| #define | [MPU\_RASR\_SIZE\_Msk](#a222e237e51f20d0e8a8c249295e77298)   (0x1FUL << [MPU\_RASR\_SIZE\_Pos](#ad90549193db0d2b7e70d3d52cb902710)) |
| #define | [MPU\_TYPE\_DREGION\_Pos](#a4d090ef632d2ba3a6ae4078c2594d6d3)   8U |
| #define | [MPU\_TYPE\_DREGION\_Msk](#a3a5d2e6871b1518dca61e28b18aec6cb)   (0xFFUL << [MPU\_TYPE\_DREGION\_Pos](#a4d090ef632d2ba3a6ae4078c2594d6d3)) |
| #define | [MPU\_RASR\_XN\_Pos](#aa02d0a5dd8b96fb9500cb5f31c9ea67b)   12 |
| #define | [MPU\_RASR\_XN\_Msk](#a4f8afc5cc7fca2ada211f8b09c76802e)   (1UL << [MPU\_RASR\_XN\_Pos](#aa02d0a5dd8b96fb9500cb5f31c9ea67b)) |
| #define | [MPU\_RASR\_AP\_Pos](#ac919b25b709081bac1fe1d30e6ca53d7)   8 |
| #define | [MPU\_RASR\_AP\_Msk](#a81da5e9383eca09414642d65fcbc14de)   (0x7UL << [MPU\_RASR\_AP\_Pos](#ac919b25b709081bac1fe1d30e6ca53d7)) |
| #define | [MPU\_RASR\_TEX\_Pos](#a340f1c91469c5bb4ee91bc29ad21c631)   3 |
| #define | [MPU\_RASR\_TEX\_Msk](#a94f4b4a368986c1955b92743046a1f4e)   (0x7UL << [MPU\_RASR\_TEX\_Pos](#a340f1c91469c5bb4ee91bc29ad21c631)) |
| #define | [MPU\_RASR\_S\_Pos](#a1820e125a5aa584cd49ede44c742985c)   2 |
| #define | [MPU\_RASR\_S\_Msk](#a872c0922578c2e74304886579e9a2361)   (1UL << [MPU\_RASR\_S\_Pos](#a1820e125a5aa584cd49ede44c742985c)) |
| #define | [MPU\_RASR\_C\_Pos](#a3a1631f2c85c66ead1d6d4cea9c16a52)   1 |
| #define | [MPU\_RASR\_C\_Msk](#af841f9bee5046fece4f513ecf707a3c1)   (1UL << [MPU\_RASR\_C\_Pos](#a3a1631f2c85c66ead1d6d4cea9c16a52)) |
| #define | [MPU\_RASR\_B\_Pos](#ae9ea3c456f66c56040a2e55793c63cf5)   0 |
| #define | [MPU\_RASR\_B\_Msk](#af97de2b86316d5b29931fc6f70b3cba1)   (1UL << [MPU\_RASR\_B\_Pos](#ae9ea3c456f66c56040a2e55793c63cf5)) |
| #define | [ARM\_MPU\_REGION\_SIZE\_256B](#ad9d8775a432b076a44a93cbf725e8619)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x07U) |
| #define | [ARM\_MPU\_REGION\_SIZE\_512B](#a79a3000f14a4d30b77e513c4db53cbe5)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x08U) |
| #define | [ARM\_MPU\_REGION\_SIZE\_1KB](#ae5bf2b5255a76ff6b62dfaed01580e9d)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x09U) |
| #define | [ARM\_MPU\_REGION\_SIZE\_2KB](#ad4d916f22b3737207c55b8d0d165caee)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x0aU) |
| #define | [ARM\_MPU\_REGION\_SIZE\_4KB](#a0612fe51de2b25b49692290d072d829c)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x0bU) |
| #define | [ARM\_MPU\_REGION\_SIZE\_8KB](#a4ce38a1ed6641648a2d2a66f48dbcb24)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x0cU) |
| #define | [ARM\_MPU\_REGION\_SIZE\_16KB](#af7a1b511ea419cb40777e0eaf32cc7e2)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x0dU) |
| #define | [ARM\_MPU\_REGION\_SIZE\_32KB](#a4d0d0ebcc97c9f24618808b66847056a)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x0eU) |
| #define | [ARM\_MPU\_REGION\_SIZE\_64KB](#ad0c79b123d9c7954c48fda30ef25b609)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x0fU) |
| #define | [ARM\_MPU\_REGION\_SIZE\_128KB](#a362c22f584b2822b8f451e356cba39d4)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x10U) |
| #define | [ARM\_MPU\_REGION\_SIZE\_256KB](#ac489a9c4e5b9cdf9acd7748c9616499b)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x11U) |
| #define | [ARM\_MPU\_REGION\_SIZE\_512KB](#a074f11c22a2c6e4deaf1e8f78717730d)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x12U) |
| #define | [ARM\_MPU\_REGION\_SIZE\_1MB](#aa2f3cf8222d50742ff33c94b7c8b3612)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x13U) |
| #define | [ARM\_MPU\_REGION\_SIZE\_2MB](#a2109105e7e283d5a5cf88772b776e441)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x14U) |
| #define | [ARM\_MPU\_REGION\_SIZE\_4MB](#a5d38b84546726a09a19c28f8de770b11)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x15U) |
| #define | [ARM\_MPU\_REGION\_SIZE\_8MB](#a62bebf6281c66f54f1d35ca43429c631)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x16U) |
| #define | [ARM\_MPU\_REGION\_SIZE\_16MB](#af3f56fa6ceeede9a0106d7f98b27a31e)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x17U) |
| #define | [ARM\_MPU\_REGION\_SIZE\_32MB](#a8b5fabd9bb7508e14e1bae69529a5853)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x18U) |
| #define | [ARM\_MPU\_REGION\_SIZE\_64MB](#a8fb3e1bb94b66387331a84c5c488286a)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x19U) |
| #define | [ARM\_MPU\_REGION\_SIZE\_128MB](#ae8fd2daf98ba641d02ff7ca3978a3ad9)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x1aU) |
| #define | [ARM\_MPU\_REGION\_SIZE\_256MB](#acce8e377f172943311b6268118bfcfdf)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x1bU) |
| #define | [ARM\_MPU\_REGION\_SIZE\_512MB](#a55ee4d5868b59de98bad7107243c2a95)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x1cU) |
| #define | [ARM\_MPU\_REGION\_SIZE\_1GB](#ac8d05ede24fdfca60537ca47f86dce1d)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x1dU) |
| #define | [ARM\_MPU\_REGION\_SIZE\_2GB](#a8f5d28ac5a55d84a4d0cf271e06bbb19)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x1eU) |
| #define | [ARM\_MPU\_REGION\_SIZE\_4GB](#ace58a7f0428b94180b8e61e29564f408)   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x1fU) |

## Macro Definition Documentation

## [◆ ](#a362c22f584b2822b8f451e356cba39d4)ARM\_MPU\_REGION\_SIZE\_128KB

| #define ARM\_MPU\_REGION\_SIZE\_128KB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x10U) |
| --- |

## [◆ ](#ae8fd2daf98ba641d02ff7ca3978a3ad9)ARM\_MPU\_REGION\_SIZE\_128MB

| #define ARM\_MPU\_REGION\_SIZE\_128MB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x1aU) |
| --- |

## [◆ ](#af7a1b511ea419cb40777e0eaf32cc7e2)ARM\_MPU\_REGION\_SIZE\_16KB

| #define ARM\_MPU\_REGION\_SIZE\_16KB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x0dU) |
| --- |

## [◆ ](#af3f56fa6ceeede9a0106d7f98b27a31e)ARM\_MPU\_REGION\_SIZE\_16MB

| #define ARM\_MPU\_REGION\_SIZE\_16MB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x17U) |
| --- |

## [◆ ](#ac8d05ede24fdfca60537ca47f86dce1d)ARM\_MPU\_REGION\_SIZE\_1GB

| #define ARM\_MPU\_REGION\_SIZE\_1GB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x1dU) |
| --- |

## [◆ ](#ae5bf2b5255a76ff6b62dfaed01580e9d)ARM\_MPU\_REGION\_SIZE\_1KB

| #define ARM\_MPU\_REGION\_SIZE\_1KB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x09U) |
| --- |

## [◆ ](#aa2f3cf8222d50742ff33c94b7c8b3612)ARM\_MPU\_REGION\_SIZE\_1MB

| #define ARM\_MPU\_REGION\_SIZE\_1MB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x13U) |
| --- |

## [◆ ](#ad9d8775a432b076a44a93cbf725e8619)ARM\_MPU\_REGION\_SIZE\_256B

| #define ARM\_MPU\_REGION\_SIZE\_256B   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x07U) |
| --- |

## [◆ ](#ac489a9c4e5b9cdf9acd7748c9616499b)ARM\_MPU\_REGION\_SIZE\_256KB

| #define ARM\_MPU\_REGION\_SIZE\_256KB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x11U) |
| --- |

## [◆ ](#acce8e377f172943311b6268118bfcfdf)ARM\_MPU\_REGION\_SIZE\_256MB

| #define ARM\_MPU\_REGION\_SIZE\_256MB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x1bU) |
| --- |

## [◆ ](#a8f5d28ac5a55d84a4d0cf271e06bbb19)ARM\_MPU\_REGION\_SIZE\_2GB

| #define ARM\_MPU\_REGION\_SIZE\_2GB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x1eU) |
| --- |

## [◆ ](#ad4d916f22b3737207c55b8d0d165caee)ARM\_MPU\_REGION\_SIZE\_2KB

| #define ARM\_MPU\_REGION\_SIZE\_2KB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x0aU) |
| --- |

## [◆ ](#a2109105e7e283d5a5cf88772b776e441)ARM\_MPU\_REGION\_SIZE\_2MB

| #define ARM\_MPU\_REGION\_SIZE\_2MB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x14U) |
| --- |

## [◆ ](#a4d0d0ebcc97c9f24618808b66847056a)ARM\_MPU\_REGION\_SIZE\_32KB

| #define ARM\_MPU\_REGION\_SIZE\_32KB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x0eU) |
| --- |

## [◆ ](#a8b5fabd9bb7508e14e1bae69529a5853)ARM\_MPU\_REGION\_SIZE\_32MB

| #define ARM\_MPU\_REGION\_SIZE\_32MB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x18U) |
| --- |

## [◆ ](#ace58a7f0428b94180b8e61e29564f408)ARM\_MPU\_REGION\_SIZE\_4GB

| #define ARM\_MPU\_REGION\_SIZE\_4GB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x1fU) |
| --- |

## [◆ ](#a0612fe51de2b25b49692290d072d829c)ARM\_MPU\_REGION\_SIZE\_4KB

| #define ARM\_MPU\_REGION\_SIZE\_4KB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x0bU) |
| --- |

## [◆ ](#a5d38b84546726a09a19c28f8de770b11)ARM\_MPU\_REGION\_SIZE\_4MB

| #define ARM\_MPU\_REGION\_SIZE\_4MB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x15U) |
| --- |

## [◆ ](#a79a3000f14a4d30b77e513c4db53cbe5)ARM\_MPU\_REGION\_SIZE\_512B

| #define ARM\_MPU\_REGION\_SIZE\_512B   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x08U) |
| --- |

## [◆ ](#a074f11c22a2c6e4deaf1e8f78717730d)ARM\_MPU\_REGION\_SIZE\_512KB

| #define ARM\_MPU\_REGION\_SIZE\_512KB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x12U) |
| --- |

## [◆ ](#a55ee4d5868b59de98bad7107243c2a95)ARM\_MPU\_REGION\_SIZE\_512MB

| #define ARM\_MPU\_REGION\_SIZE\_512MB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x1cU) |
| --- |

## [◆ ](#ad0c79b123d9c7954c48fda30ef25b609)ARM\_MPU\_REGION\_SIZE\_64KB

| #define ARM\_MPU\_REGION\_SIZE\_64KB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x0fU) |
| --- |

## [◆ ](#a8fb3e1bb94b66387331a84c5c488286a)ARM\_MPU\_REGION\_SIZE\_64MB

| #define ARM\_MPU\_REGION\_SIZE\_64MB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x19U) |
| --- |

## [◆ ](#a4ce38a1ed6641648a2d2a66f48dbcb24)ARM\_MPU\_REGION\_SIZE\_8KB

| #define ARM\_MPU\_REGION\_SIZE\_8KB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x0cU) |
| --- |

## [◆ ](#a62bebf6281c66f54f1d35ca43429c631)ARM\_MPU\_REGION\_SIZE\_8MB

| #define ARM\_MPU\_REGION\_SIZE\_8MB   (([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d))0x16U) |
| --- |

## [◆ ](#a81da5e9383eca09414642d65fcbc14de)MPU\_RASR\_AP\_Msk

| #define MPU\_RASR\_AP\_Msk   (0x7UL << [MPU\_RASR\_AP\_Pos](#ac919b25b709081bac1fe1d30e6ca53d7)) |
| --- |

## [◆ ](#ac919b25b709081bac1fe1d30e6ca53d7)MPU\_RASR\_AP\_Pos

| #define MPU\_RASR\_AP\_Pos   8 |
| --- |

## [◆ ](#af97de2b86316d5b29931fc6f70b3cba1)MPU\_RASR\_B\_Msk

| #define MPU\_RASR\_B\_Msk   (1UL << [MPU\_RASR\_B\_Pos](#ae9ea3c456f66c56040a2e55793c63cf5)) |
| --- |

## [◆ ](#ae9ea3c456f66c56040a2e55793c63cf5)MPU\_RASR\_B\_Pos

| #define MPU\_RASR\_B\_Pos   0 |
| --- |

## [◆ ](#af841f9bee5046fece4f513ecf707a3c1)MPU\_RASR\_C\_Msk

| #define MPU\_RASR\_C\_Msk   (1UL << [MPU\_RASR\_C\_Pos](#a3a1631f2c85c66ead1d6d4cea9c16a52)) |
| --- |

## [◆ ](#a3a1631f2c85c66ead1d6d4cea9c16a52)MPU\_RASR\_C\_Pos

| #define MPU\_RASR\_C\_Pos   1 |
| --- |

## [◆ ](#af6c4850fc33a5f13a42cf25dbce72646)MPU\_RASR\_ENABLE\_Msk

| #define MPU\_RASR\_ENABLE\_Msk   (1) |
| --- |

## [◆ ](#a872c0922578c2e74304886579e9a2361)MPU\_RASR\_S\_Msk

| #define MPU\_RASR\_S\_Msk   (1UL << [MPU\_RASR\_S\_Pos](#a1820e125a5aa584cd49ede44c742985c)) |
| --- |

## [◆ ](#a1820e125a5aa584cd49ede44c742985c)MPU\_RASR\_S\_Pos

| #define MPU\_RASR\_S\_Pos   2 |
| --- |

## [◆ ](#a222e237e51f20d0e8a8c249295e77298)MPU\_RASR\_SIZE\_Msk

| #define MPU\_RASR\_SIZE\_Msk   (0x1FUL << [MPU\_RASR\_SIZE\_Pos](#ad90549193db0d2b7e70d3d52cb902710)) |
| --- |

## [◆ ](#ad90549193db0d2b7e70d3d52cb902710)MPU\_RASR\_SIZE\_Pos

| #define MPU\_RASR\_SIZE\_Pos   1U |
| --- |

## [◆ ](#a94f4b4a368986c1955b92743046a1f4e)MPU\_RASR\_TEX\_Msk

| #define MPU\_RASR\_TEX\_Msk   (0x7UL << [MPU\_RASR\_TEX\_Pos](#a340f1c91469c5bb4ee91bc29ad21c631)) |
| --- |

## [◆ ](#a340f1c91469c5bb4ee91bc29ad21c631)MPU\_RASR\_TEX\_Pos

| #define MPU\_RASR\_TEX\_Pos   3 |
| --- |

## [◆ ](#a4f8afc5cc7fca2ada211f8b09c76802e)MPU\_RASR\_XN\_Msk

| #define MPU\_RASR\_XN\_Msk   (1UL << [MPU\_RASR\_XN\_Pos](#aa02d0a5dd8b96fb9500cb5f31c9ea67b)) |
| --- |

## [◆ ](#aa02d0a5dd8b96fb9500cb5f31c9ea67b)MPU\_RASR\_XN\_Pos

| #define MPU\_RASR\_XN\_Pos   12 |
| --- |

## [◆ ](#a33905dca89aa5b5bb9aa9518094b8b80)MPU\_RBAR\_ADDR\_Msk

| #define MPU\_RBAR\_ADDR\_Msk   (~0x1f) |
| --- |

## [◆ ](#a3a5d2e6871b1518dca61e28b18aec6cb)MPU\_TYPE\_DREGION\_Msk

| #define MPU\_TYPE\_DREGION\_Msk   (0xFFUL << [MPU\_TYPE\_DREGION\_Pos](#a4d090ef632d2ba3a6ae4078c2594d6d3)) |
| --- |

## [◆ ](#a4d090ef632d2ba3a6ae4078c2594d6d3)MPU\_TYPE\_DREGION\_Pos

| #define MPU\_TYPE\_DREGION\_Pos   8U |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_a\_r](dir_cde462911e3dbfe61dba09f2df37ee97.md)
- [mpu.h](arm_2cortex__a__r_2mpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
