---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/lsm6dsv16x_8h.html
original_path: doxygen/html/lsm6dsv16x_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lsm6dsv16x.h File Reference

[Go to the source code of this file.](lsm6dsv16x_8h_source.md)

| Macros | |
| --- | --- |
| #define | [LSM6DSV16X\_DT\_FS\_2G](#a0062d4a16bf431f8429ae06c1926dd13)   0 |
| #define | [LSM6DSV16X\_DT\_FS\_4G](#a90b5d8955a2e8d4cfc1741f426433668)   1 |
| #define | [LSM6DSV16X\_DT\_FS\_8G](#a5416be4ee0699ccf0994c7decfd9637f)   2 |
| #define | [LSM6DSV16X\_DT\_FS\_16G](#a8106285e2a93c6dfc3b9c704166938e7)   3 |
| #define | [LSM6DSV16X\_DT\_FS\_125DPS](#aba0ad1e516dc73ce4f610474db2cf8f0)   0x0 |
| #define | [LSM6DSV16X\_DT\_FS\_250DPS](#a4b908bb6e1684b69e3023a9b3056461d)   0x1 |
| #define | [LSM6DSV16X\_DT\_FS\_500DPS](#a02d9fa7e2f077d98c4f6882555f74162)   0x2 |
| #define | [LSM6DSV16X\_DT\_FS\_1000DPS](#a062069e117674a493a3100369c6bae0c)   0x3 |
| #define | [LSM6DSV16X\_DT\_FS\_2000DPS](#a7568fcc223af82319d884138ff43fcaa)   0x4 |
| #define | [LSM6DSV16X\_DT\_FS\_4000DPS](#aad0a2d26bab54aff65bcf922db56d5dd)   0xc |
| #define | [LSM6DSV16X\_DT\_ODR\_OFF](#a0b11f0f939bc10587ca0f8cc1e8da7d0)   0x0 |
| #define | [LSM6DSV16X\_DT\_ODR\_AT\_1Hz875](#a51ad08e5e99e7da94cb4948f04cb7931)   0x1 |
| #define | [LSM6DSV16X\_DT\_ODR\_AT\_7Hz5](#a908f07f0e822f1776f0e59166986fb43)   0x2 |
| #define | [LSM6DSV16X\_DT\_ODR\_AT\_15Hz](#af25ef10ac9e3183392ea6f3b4c8872ad)   0x3 |
| #define | [LSM6DSV16X\_DT\_ODR\_AT\_30Hz](#acb735ed313c5813c26206dc0a8c649a0)   0x4 |
| #define | [LSM6DSV16X\_DT\_ODR\_AT\_60Hz](#ac4763e79340953fdec46a2557cc3a7e9)   0x5 |
| #define | [LSM6DSV16X\_DT\_ODR\_AT\_120Hz](#a4a8d2eb4eef9d6137b02aab5cf60d9b3)   0x6 |
| #define | [LSM6DSV16X\_DT\_ODR\_AT\_240Hz](#a6cc44855f1c9ba6a44063c59204ab6e7)   0x7 |
| #define | [LSM6DSV16X\_DT\_ODR\_AT\_480Hz](#a3814c412b7314efc062a8ed31a95a530)   0x8 |
| #define | [LSM6DSV16X\_DT\_ODR\_AT\_960Hz](#abd274f980523545640e31b5e8fa373b0)   0x9 |
| #define | [LSM6DSV16X\_DT\_ODR\_AT\_1920Hz](#ae0d6b562ee0cb8523a1a9b974332f74c)   0xA |
| #define | [LSM6DSV16X\_DT\_ODR\_AT\_3840Hz](#a349976f99ae8bd144054eb4b6d5601a6)   0xB |
| #define | [LSM6DSV16X\_DT\_ODR\_AT\_7680Hz](#a7adb88cac62df5b3e63b9cf647ddfea3)   0xC |
| #define | [LSM6DSV16X\_DT\_ODR\_HA01\_AT\_15Hz625](#af7f63bb894b71c67c933651539f370fa)   0x13 |
| #define | [LSM6DSV16X\_DT\_ODR\_HA01\_AT\_31Hz25](#ab3da725c6833f45b7a33afa55cfc40b3)   0x14 |
| #define | [LSM6DSV16X\_DT\_ODR\_HA01\_AT\_62Hz5](#ab024dfe5fc460ce2a9001732e21d9f05)   0x15 |
| #define | [LSM6DSV16X\_DT\_ODR\_HA01\_AT\_125Hz](#a23da2ed6467ffb0cd1f2ab9ae9584ec8)   0x16 |
| #define | [LSM6DSV16X\_DT\_ODR\_HA01\_AT\_250Hz](#a62eaf6164a041b9280933dc50e3dca89)   0x17 |
| #define | [LSM6DSV16X\_DT\_ODR\_HA01\_AT\_500Hz](#a5875eadae47c3b41ee32c6571f5fd7e9)   0x18 |
| #define | [LSM6DSV16X\_DT\_ODR\_HA01\_AT\_1000Hz](#a37a462e9411d24b07ffa0266baf4b0e8)   0x19 |
| #define | [LSM6DSV16X\_DT\_ODR\_HA01\_AT\_2000Hz](#a797db8e4aa3fa0ceae95f9af0a720767)   0x1A |
| #define | [LSM6DSV16X\_DT\_ODR\_HA01\_AT\_4000Hz](#a312e7af10f7387764d4760017c8d19fd)   0x1B |
| #define | [LSM6DSV16X\_DT\_ODR\_HA01\_AT\_8000Hz](#a490ba6a741e42ab2cf6a8260c1481bf7)   0x1C |
| #define | [LSM6DSV16X\_DT\_ODR\_HA02\_AT\_12Hz5](#ae9f6bae9e1bec8194d9ce6a42e30f472)   0x23 |
| #define | [LSM6DSV16X\_DT\_ODR\_HA02\_AT\_25Hz](#a3996f051df14448dfa2b91864ee0e951)   0x24 |
| #define | [LSM6DSV16X\_DT\_ODR\_HA02\_AT\_50Hz](#a76bee41aedef974a0db131751047db55)   0x25 |
| #define | [LSM6DSV16X\_DT\_ODR\_HA02\_AT\_100Hz](#adfc3e88f261d411102538e9e73352b55)   0x26 |
| #define | [LSM6DSV16X\_DT\_ODR\_HA02\_AT\_200Hz](#a30137882a4c78ddb51cff91a3775780c)   0x27 |
| #define | [LSM6DSV16X\_DT\_ODR\_HA02\_AT\_400Hz](#a2b30fdf564d398b52d8f0ca7ab39ec92)   0x28 |
| #define | [LSM6DSV16X\_DT\_ODR\_HA02\_AT\_800Hz](#adc01cf297fde9fa86865c80343107e6c)   0x29 |
| #define | [LSM6DSV16X\_DT\_ODR\_HA02\_AT\_1600Hz](#ae2f10f581548e9c1b91680f044b70815)   0x2A |
| #define | [LSM6DSV16X\_DT\_ODR\_HA02\_AT\_3200Hz](#a0685e049b46f34e3cff3590827a4cd04)   0x2B |
| #define | [LSM6DSV16X\_DT\_ODR\_HA02\_AT\_6400Hz](#ae52f4d001cefe4730ff81224871821c7)   0x2C |

## Macro Definition Documentation

## [◆ ](#a062069e117674a493a3100369c6bae0c)LSM6DSV16X\_DT\_FS\_1000DPS

| #define LSM6DSV16X\_DT\_FS\_1000DPS   0x3 |
| --- |

## [◆ ](#aba0ad1e516dc73ce4f610474db2cf8f0)LSM6DSV16X\_DT\_FS\_125DPS

| #define LSM6DSV16X\_DT\_FS\_125DPS   0x0 |
| --- |

## [◆ ](#a8106285e2a93c6dfc3b9c704166938e7)LSM6DSV16X\_DT\_FS\_16G

| #define LSM6DSV16X\_DT\_FS\_16G   3 |
| --- |

## [◆ ](#a7568fcc223af82319d884138ff43fcaa)LSM6DSV16X\_DT\_FS\_2000DPS

| #define LSM6DSV16X\_DT\_FS\_2000DPS   0x4 |
| --- |

## [◆ ](#a4b908bb6e1684b69e3023a9b3056461d)LSM6DSV16X\_DT\_FS\_250DPS

| #define LSM6DSV16X\_DT\_FS\_250DPS   0x1 |
| --- |

## [◆ ](#a0062d4a16bf431f8429ae06c1926dd13)LSM6DSV16X\_DT\_FS\_2G

| #define LSM6DSV16X\_DT\_FS\_2G   0 |
| --- |

## [◆ ](#aad0a2d26bab54aff65bcf922db56d5dd)LSM6DSV16X\_DT\_FS\_4000DPS

| #define LSM6DSV16X\_DT\_FS\_4000DPS   0xc |
| --- |

## [◆ ](#a90b5d8955a2e8d4cfc1741f426433668)LSM6DSV16X\_DT\_FS\_4G

| #define LSM6DSV16X\_DT\_FS\_4G   1 |
| --- |

## [◆ ](#a02d9fa7e2f077d98c4f6882555f74162)LSM6DSV16X\_DT\_FS\_500DPS

| #define LSM6DSV16X\_DT\_FS\_500DPS   0x2 |
| --- |

## [◆ ](#a5416be4ee0699ccf0994c7decfd9637f)LSM6DSV16X\_DT\_FS\_8G

| #define LSM6DSV16X\_DT\_FS\_8G   2 |
| --- |

## [◆ ](#a4a8d2eb4eef9d6137b02aab5cf60d9b3)LSM6DSV16X\_DT\_ODR\_AT\_120Hz

| #define LSM6DSV16X\_DT\_ODR\_AT\_120Hz   0x6 |
| --- |

## [◆ ](#af25ef10ac9e3183392ea6f3b4c8872ad)LSM6DSV16X\_DT\_ODR\_AT\_15Hz

| #define LSM6DSV16X\_DT\_ODR\_AT\_15Hz   0x3 |
| --- |

## [◆ ](#ae0d6b562ee0cb8523a1a9b974332f74c)LSM6DSV16X\_DT\_ODR\_AT\_1920Hz

| #define LSM6DSV16X\_DT\_ODR\_AT\_1920Hz   0xA |
| --- |

## [◆ ](#a51ad08e5e99e7da94cb4948f04cb7931)LSM6DSV16X\_DT\_ODR\_AT\_1Hz875

| #define LSM6DSV16X\_DT\_ODR\_AT\_1Hz875   0x1 |
| --- |

## [◆ ](#a6cc44855f1c9ba6a44063c59204ab6e7)LSM6DSV16X\_DT\_ODR\_AT\_240Hz

| #define LSM6DSV16X\_DT\_ODR\_AT\_240Hz   0x7 |
| --- |

## [◆ ](#acb735ed313c5813c26206dc0a8c649a0)LSM6DSV16X\_DT\_ODR\_AT\_30Hz

| #define LSM6DSV16X\_DT\_ODR\_AT\_30Hz   0x4 |
| --- |

## [◆ ](#a349976f99ae8bd144054eb4b6d5601a6)LSM6DSV16X\_DT\_ODR\_AT\_3840Hz

| #define LSM6DSV16X\_DT\_ODR\_AT\_3840Hz   0xB |
| --- |

## [◆ ](#a3814c412b7314efc062a8ed31a95a530)LSM6DSV16X\_DT\_ODR\_AT\_480Hz

| #define LSM6DSV16X\_DT\_ODR\_AT\_480Hz   0x8 |
| --- |

## [◆ ](#ac4763e79340953fdec46a2557cc3a7e9)LSM6DSV16X\_DT\_ODR\_AT\_60Hz

| #define LSM6DSV16X\_DT\_ODR\_AT\_60Hz   0x5 |
| --- |

## [◆ ](#a7adb88cac62df5b3e63b9cf647ddfea3)LSM6DSV16X\_DT\_ODR\_AT\_7680Hz

| #define LSM6DSV16X\_DT\_ODR\_AT\_7680Hz   0xC |
| --- |

## [◆ ](#a908f07f0e822f1776f0e59166986fb43)LSM6DSV16X\_DT\_ODR\_AT\_7Hz5

| #define LSM6DSV16X\_DT\_ODR\_AT\_7Hz5   0x2 |
| --- |

## [◆ ](#abd274f980523545640e31b5e8fa373b0)LSM6DSV16X\_DT\_ODR\_AT\_960Hz

| #define LSM6DSV16X\_DT\_ODR\_AT\_960Hz   0x9 |
| --- |

## [◆ ](#a37a462e9411d24b07ffa0266baf4b0e8)LSM6DSV16X\_DT\_ODR\_HA01\_AT\_1000Hz

| #define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_1000Hz   0x19 |
| --- |

## [◆ ](#a23da2ed6467ffb0cd1f2ab9ae9584ec8)LSM6DSV16X\_DT\_ODR\_HA01\_AT\_125Hz

| #define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_125Hz   0x16 |
| --- |

## [◆ ](#af7f63bb894b71c67c933651539f370fa)LSM6DSV16X\_DT\_ODR\_HA01\_AT\_15Hz625

| #define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_15Hz625   0x13 |
| --- |

## [◆ ](#a797db8e4aa3fa0ceae95f9af0a720767)LSM6DSV16X\_DT\_ODR\_HA01\_AT\_2000Hz

| #define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_2000Hz   0x1A |
| --- |

## [◆ ](#a62eaf6164a041b9280933dc50e3dca89)LSM6DSV16X\_DT\_ODR\_HA01\_AT\_250Hz

| #define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_250Hz   0x17 |
| --- |

## [◆ ](#ab3da725c6833f45b7a33afa55cfc40b3)LSM6DSV16X\_DT\_ODR\_HA01\_AT\_31Hz25

| #define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_31Hz25   0x14 |
| --- |

## [◆ ](#a312e7af10f7387764d4760017c8d19fd)LSM6DSV16X\_DT\_ODR\_HA01\_AT\_4000Hz

| #define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_4000Hz   0x1B |
| --- |

## [◆ ](#a5875eadae47c3b41ee32c6571f5fd7e9)LSM6DSV16X\_DT\_ODR\_HA01\_AT\_500Hz

| #define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_500Hz   0x18 |
| --- |

## [◆ ](#ab024dfe5fc460ce2a9001732e21d9f05)LSM6DSV16X\_DT\_ODR\_HA01\_AT\_62Hz5

| #define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_62Hz5   0x15 |
| --- |

## [◆ ](#a490ba6a741e42ab2cf6a8260c1481bf7)LSM6DSV16X\_DT\_ODR\_HA01\_AT\_8000Hz

| #define LSM6DSV16X\_DT\_ODR\_HA01\_AT\_8000Hz   0x1C |
| --- |

## [◆ ](#adfc3e88f261d411102538e9e73352b55)LSM6DSV16X\_DT\_ODR\_HA02\_AT\_100Hz

| #define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_100Hz   0x26 |
| --- |

## [◆ ](#ae9f6bae9e1bec8194d9ce6a42e30f472)LSM6DSV16X\_DT\_ODR\_HA02\_AT\_12Hz5

| #define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_12Hz5   0x23 |
| --- |

## [◆ ](#ae2f10f581548e9c1b91680f044b70815)LSM6DSV16X\_DT\_ODR\_HA02\_AT\_1600Hz

| #define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_1600Hz   0x2A |
| --- |

## [◆ ](#a30137882a4c78ddb51cff91a3775780c)LSM6DSV16X\_DT\_ODR\_HA02\_AT\_200Hz

| #define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_200Hz   0x27 |
| --- |

## [◆ ](#a3996f051df14448dfa2b91864ee0e951)LSM6DSV16X\_DT\_ODR\_HA02\_AT\_25Hz

| #define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_25Hz   0x24 |
| --- |

## [◆ ](#a0685e049b46f34e3cff3590827a4cd04)LSM6DSV16X\_DT\_ODR\_HA02\_AT\_3200Hz

| #define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_3200Hz   0x2B |
| --- |

## [◆ ](#a2b30fdf564d398b52d8f0ca7ab39ec92)LSM6DSV16X\_DT\_ODR\_HA02\_AT\_400Hz

| #define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_400Hz   0x28 |
| --- |

## [◆ ](#a76bee41aedef974a0db131751047db55)LSM6DSV16X\_DT\_ODR\_HA02\_AT\_50Hz

| #define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_50Hz   0x25 |
| --- |

## [◆ ](#ae52f4d001cefe4730ff81224871821c7)LSM6DSV16X\_DT\_ODR\_HA02\_AT\_6400Hz

| #define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_6400Hz   0x2C |
| --- |

## [◆ ](#adc01cf297fde9fa86865c80343107e6c)LSM6DSV16X\_DT\_ODR\_HA02\_AT\_800Hz

| #define LSM6DSV16X\_DT\_ODR\_HA02\_AT\_800Hz   0x29 |
| --- |

## [◆ ](#a0b11f0f939bc10587ca0f8cc1e8da7d0)LSM6DSV16X\_DT\_ODR\_OFF

| #define LSM6DSV16X\_DT\_ODR\_OFF   0x0 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lsm6dsv16x.h](lsm6dsv16x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
