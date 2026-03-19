---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/lsm6dsv16x_8h.html
original_path: doxygen/html/lsm6dsv16x_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
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
| #define | [LSM6DSV16X\_DT\_XL\_NOT\_BATCHED](#a4ef4f13c41aa295be449873b24c05f9c)   0x0 |
| #define | [LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_1Hz875](#adf6c8ffc133f1378d93ebfd06db51421)   0x1 |
| #define | [LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_7Hz5](#a61aab608d630df418dbda1e07f1ef59c)   0x2 |
| #define | [LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_15Hz](#a0fbabfdc2567db259f0b20101359d2f9)   0x3 |
| #define | [LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_30Hz](#a5ae8341f1afd0dcf0eb57a848ee3e858)   0x4 |
| #define | [LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_60Hz](#a9e33dc1dbe6f3174e384b40593522991)   0x5 |
| #define | [LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_120Hz](#a95474384a2628c70dc3ebea4d4e1b506)   0x6 |
| #define | [LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_240Hz](#ac9c6e6e83c2f65b5e96517c474d2d5e1)   0x7 |
| #define | [LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_480Hz](#a8ef8c856d92fd2354d288635ca8b9257)   0x8 |
| #define | [LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_960Hz](#acf5fe0be8745dd5980f91e924e422f43)   0x9 |
| #define | [LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_1920Hz](#a38847f0caf107ca88a4b2abf9940c425)   0xa |
| #define | [LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_3840Hz](#a3a1a00ad577aede4ed2fcc961ed960bc)   0xb |
| #define | [LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_7680Hz](#a32bd8c6d3b54fef541cdeadbfd34de96)   0xc |
| #define | [LSM6DSV16X\_DT\_GY\_NOT\_BATCHED](#a0805396bb4287ceb7afb52d3a9050b9a)   0x0 |
| #define | [LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_1Hz875](#a542a32ac0a25cac670f23225b1309e25)   0x1 |
| #define | [LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_7Hz5](#a7bd4e5d535e70450ec097298e6b34f4b)   0x2 |
| #define | [LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_15Hz](#a60d78a7a0640b0f5f977a7af5b35160f)   0x3 |
| #define | [LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_30Hz](#a8d7b90c563ec26ef63120b39db208f9e)   0x4 |
| #define | [LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_60Hz](#a6d91f98f62bf25fbfb4c8a80a02fe590)   0x5 |
| #define | [LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_120Hz](#ad514e99fcd6951ceae37e15fa30bd56a)   0x6 |
| #define | [LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_240Hz](#aee057f81eec4ea3c9b97118b2029889d)   0x7 |
| #define | [LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_480Hz](#a61e8fe8cc642c818906a4a0905818453)   0x8 |
| #define | [LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_960Hz](#a3d3faee9ca754ac9b8d43bf42b15369e)   0x9 |
| #define | [LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_1920Hz](#addf5efdd37d6dc7a2ec016b96853696b)   0xa |
| #define | [LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_3840Hz](#a5102eb772bbfff3718d8691d89743169)   0xb |
| #define | [LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_7680Hz](#a43005c15632a48a218ef26c71ccc5fc4)   0xc |
| #define | [LSM6DSV16X\_DT\_TEMP\_NOT\_BATCHED](#a1d01297fd684f9baa36cde4c740a7805)   0x0 |
| #define | [LSM6DSV16X\_DT\_TEMP\_BATCHED\_AT\_1Hz875](#a9b0f2f7f6f41d59b31c50eb73fe48186)   0x1 |
| #define | [LSM6DSV16X\_DT\_TEMP\_BATCHED\_AT\_15Hz](#a7557d711268e0db453913e2b4a761801)   0x2 |
| #define | [LSM6DSV16X\_DT\_TEMP\_BATCHED\_AT\_60Hz](#aca5c0f34e41602a89925930a668b9811)   0x3 |
| #define | [LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_15Hz](#a8efcfdc7f0bd2c8161698dce91733fda)   0x0 |
| #define | [LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_30Hz](#ab58b04372359a2676fbdf491f6e057e3)   0x1 |
| #define | [LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_60Hz](#a357ede63697d797a4eccb0059c7a0796)   0x2 |
| #define | [LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_120Hz](#a88efe57bf97af9d3818ca9701eb05bd1)   0x3 |
| #define | [LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_240Hz](#ac9498844ce5357f85430f56234a35c43)   0x4 |
| #define | [LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_480Hz](#a7f3fd0ec24d25ee9cc82bb328276f5ff)   0x5 |
| #define | [LSM6DSV16X\_DT\_SFLP\_FIFO\_OFF](#a3754cdaa4af134dfb0e474057b59dc2a)   0x0 |
| #define | [LSM6DSV16X\_DT\_SFLP\_FIFO\_GAME\_ROTATION](#a435cca9b30698e3eb75312d2fe59adbc)   0x1 |
| #define | [LSM6DSV16X\_DT\_SFLP\_FIFO\_GRAVITY](#a8ce1813524567fae1a1ffaba524b1234)   0x2 |
| #define | [LSM6DSV16X\_DT\_SFLP\_FIFO\_GAME\_ROTATION\_GRAVITY](#a7ae44c60e8a17870abd9e6d6fd78e22c)   0x3 |
| #define | [LSM6DSV16X\_DT\_SFLP\_FIFO\_GBIAS](#ac901645248e2b892c05aa6fb01ca8569)   0x4 |
| #define | [LSM6DSV16X\_DT\_SFLP\_FIFO\_GAME\_ROTATION\_GBIAS](#a4851a7f7f1eccffbdf7ba630a0c54db9)   0x5 |
| #define | [LSM6DSV16X\_DT\_SFLP\_FIFO\_GRAVITY\_GBIAS](#aa745b4ad6353c5ab492d80e09479291b)   0x6 |
| #define | [LSM6DSV16X\_DT\_SFLP\_FIFO\_GAME\_ROTATION\_GRAVITY\_GBIAS](#a237a051673771c476a66f6b22dbee47d)   0x7 |

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

## [◆ ](#ad514e99fcd6951ceae37e15fa30bd56a)LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_120Hz

| #define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_120Hz   0x6 |
| --- |

## [◆ ](#a60d78a7a0640b0f5f977a7af5b35160f)LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_15Hz

| #define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_15Hz   0x3 |
| --- |

## [◆ ](#addf5efdd37d6dc7a2ec016b96853696b)LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_1920Hz

| #define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_1920Hz   0xa |
| --- |

## [◆ ](#a542a32ac0a25cac670f23225b1309e25)LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_1Hz875

| #define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_1Hz875   0x1 |
| --- |

## [◆ ](#aee057f81eec4ea3c9b97118b2029889d)LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_240Hz

| #define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_240Hz   0x7 |
| --- |

## [◆ ](#a8d7b90c563ec26ef63120b39db208f9e)LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_30Hz

| #define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_30Hz   0x4 |
| --- |

## [◆ ](#a5102eb772bbfff3718d8691d89743169)LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_3840Hz

| #define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_3840Hz   0xb |
| --- |

## [◆ ](#a61e8fe8cc642c818906a4a0905818453)LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_480Hz

| #define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_480Hz   0x8 |
| --- |

## [◆ ](#a6d91f98f62bf25fbfb4c8a80a02fe590)LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_60Hz

| #define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_60Hz   0x5 |
| --- |

## [◆ ](#a43005c15632a48a218ef26c71ccc5fc4)LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_7680Hz

| #define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_7680Hz   0xc |
| --- |

## [◆ ](#a7bd4e5d535e70450ec097298e6b34f4b)LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_7Hz5

| #define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_7Hz5   0x2 |
| --- |

## [◆ ](#a3d3faee9ca754ac9b8d43bf42b15369e)LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_960Hz

| #define LSM6DSV16X\_DT\_GY\_BATCHED\_AT\_960Hz   0x9 |
| --- |

## [◆ ](#a0805396bb4287ceb7afb52d3a9050b9a)LSM6DSV16X\_DT\_GY\_NOT\_BATCHED

| #define LSM6DSV16X\_DT\_GY\_NOT\_BATCHED   0x0 |
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

## [◆ ](#a435cca9b30698e3eb75312d2fe59adbc)LSM6DSV16X\_DT\_SFLP\_FIFO\_GAME\_ROTATION

| #define LSM6DSV16X\_DT\_SFLP\_FIFO\_GAME\_ROTATION   0x1 |
| --- |

## [◆ ](#a4851a7f7f1eccffbdf7ba630a0c54db9)LSM6DSV16X\_DT\_SFLP\_FIFO\_GAME\_ROTATION\_GBIAS

| #define LSM6DSV16X\_DT\_SFLP\_FIFO\_GAME\_ROTATION\_GBIAS   0x5 |
| --- |

## [◆ ](#a7ae44c60e8a17870abd9e6d6fd78e22c)LSM6DSV16X\_DT\_SFLP\_FIFO\_GAME\_ROTATION\_GRAVITY

| #define LSM6DSV16X\_DT\_SFLP\_FIFO\_GAME\_ROTATION\_GRAVITY   0x3 |
| --- |

## [◆ ](#a237a051673771c476a66f6b22dbee47d)LSM6DSV16X\_DT\_SFLP\_FIFO\_GAME\_ROTATION\_GRAVITY\_GBIAS

| #define LSM6DSV16X\_DT\_SFLP\_FIFO\_GAME\_ROTATION\_GRAVITY\_GBIAS   0x7 |
| --- |

## [◆ ](#ac901645248e2b892c05aa6fb01ca8569)LSM6DSV16X\_DT\_SFLP\_FIFO\_GBIAS

| #define LSM6DSV16X\_DT\_SFLP\_FIFO\_GBIAS   0x4 |
| --- |

## [◆ ](#a8ce1813524567fae1a1ffaba524b1234)LSM6DSV16X\_DT\_SFLP\_FIFO\_GRAVITY

| #define LSM6DSV16X\_DT\_SFLP\_FIFO\_GRAVITY   0x2 |
| --- |

## [◆ ](#aa745b4ad6353c5ab492d80e09479291b)LSM6DSV16X\_DT\_SFLP\_FIFO\_GRAVITY\_GBIAS

| #define LSM6DSV16X\_DT\_SFLP\_FIFO\_GRAVITY\_GBIAS   0x6 |
| --- |

## [◆ ](#a3754cdaa4af134dfb0e474057b59dc2a)LSM6DSV16X\_DT\_SFLP\_FIFO\_OFF

| #define LSM6DSV16X\_DT\_SFLP\_FIFO\_OFF   0x0 |
| --- |

## [◆ ](#a88efe57bf97af9d3818ca9701eb05bd1)LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_120Hz

| #define LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_120Hz   0x3 |
| --- |

## [◆ ](#a8efcfdc7f0bd2c8161698dce91733fda)LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_15Hz

| #define LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_15Hz   0x0 |
| --- |

## [◆ ](#ac9498844ce5357f85430f56234a35c43)LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_240Hz

| #define LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_240Hz   0x4 |
| --- |

## [◆ ](#ab58b04372359a2676fbdf491f6e057e3)LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_30Hz

| #define LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_30Hz   0x1 |
| --- |

## [◆ ](#a7f3fd0ec24d25ee9cc82bb328276f5ff)LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_480Hz

| #define LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_480Hz   0x5 |
| --- |

## [◆ ](#a357ede63697d797a4eccb0059c7a0796)LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_60Hz

| #define LSM6DSV16X\_DT\_SFLP\_ODR\_AT\_60Hz   0x2 |
| --- |

## [◆ ](#a7557d711268e0db453913e2b4a761801)LSM6DSV16X\_DT\_TEMP\_BATCHED\_AT\_15Hz

| #define LSM6DSV16X\_DT\_TEMP\_BATCHED\_AT\_15Hz   0x2 |
| --- |

## [◆ ](#a9b0f2f7f6f41d59b31c50eb73fe48186)LSM6DSV16X\_DT\_TEMP\_BATCHED\_AT\_1Hz875

| #define LSM6DSV16X\_DT\_TEMP\_BATCHED\_AT\_1Hz875   0x1 |
| --- |

## [◆ ](#aca5c0f34e41602a89925930a668b9811)LSM6DSV16X\_DT\_TEMP\_BATCHED\_AT\_60Hz

| #define LSM6DSV16X\_DT\_TEMP\_BATCHED\_AT\_60Hz   0x3 |
| --- |

## [◆ ](#a1d01297fd684f9baa36cde4c740a7805)LSM6DSV16X\_DT\_TEMP\_NOT\_BATCHED

| #define LSM6DSV16X\_DT\_TEMP\_NOT\_BATCHED   0x0 |
| --- |

## [◆ ](#a95474384a2628c70dc3ebea4d4e1b506)LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_120Hz

| #define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_120Hz   0x6 |
| --- |

## [◆ ](#a0fbabfdc2567db259f0b20101359d2f9)LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_15Hz

| #define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_15Hz   0x3 |
| --- |

## [◆ ](#a38847f0caf107ca88a4b2abf9940c425)LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_1920Hz

| #define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_1920Hz   0xa |
| --- |

## [◆ ](#adf6c8ffc133f1378d93ebfd06db51421)LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_1Hz875

| #define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_1Hz875   0x1 |
| --- |

## [◆ ](#ac9c6e6e83c2f65b5e96517c474d2d5e1)LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_240Hz

| #define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_240Hz   0x7 |
| --- |

## [◆ ](#a5ae8341f1afd0dcf0eb57a848ee3e858)LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_30Hz

| #define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_30Hz   0x4 |
| --- |

## [◆ ](#a3a1a00ad577aede4ed2fcc961ed960bc)LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_3840Hz

| #define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_3840Hz   0xb |
| --- |

## [◆ ](#a8ef8c856d92fd2354d288635ca8b9257)LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_480Hz

| #define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_480Hz   0x8 |
| --- |

## [◆ ](#a9e33dc1dbe6f3174e384b40593522991)LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_60Hz

| #define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_60Hz   0x5 |
| --- |

## [◆ ](#a32bd8c6d3b54fef541cdeadbfd34de96)LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_7680Hz

| #define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_7680Hz   0xc |
| --- |

## [◆ ](#a61aab608d630df418dbda1e07f1ef59c)LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_7Hz5

| #define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_7Hz5   0x2 |
| --- |

## [◆ ](#acf5fe0be8745dd5980f91e924e422f43)LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_960Hz

| #define LSM6DSV16X\_DT\_XL\_BATCHED\_AT\_960Hz   0x9 |
| --- |

## [◆ ](#a4ef4f13c41aa295be449873b24c05f9c)LSM6DSV16X\_DT\_XL\_NOT\_BATCHED

| #define LSM6DSV16X\_DT\_XL\_NOT\_BATCHED   0x0 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lsm6dsv16x.h](lsm6dsv16x_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
