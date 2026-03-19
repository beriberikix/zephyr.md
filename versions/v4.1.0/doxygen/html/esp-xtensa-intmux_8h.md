---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/esp-xtensa-intmux_8h.html
original_path: doxygen/html/esp-xtensa-intmux_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp-xtensa-intmux.h File Reference

[Go to the source code of this file.](esp-xtensa-intmux_8h_source.md)

| Macros | |
| --- | --- |
| #define | [WIFI\_MAC\_INTR\_SOURCE](#ad000d08efc3e8a5fc56da537973a5cb8)   0 /\* WiFi MAC, level \*/ |
| #define | [WIFI\_MAC\_NMI\_SOURCE](#abfc935ef2963ee54b6a1f1279b4887ff)   1 /\* WiFi MAC, NMI, use if MAC needs fix in NMI \*/ |
| #define | [WIFI\_BB\_INTR\_SOURCE](#a5383f7fa77bc12a8301c54e0dfb66306)   2 /\* WiFi BB, level, we can do some calibration \*/ |
| #define | [BT\_MAC\_INTR\_SOURCE](#a0b48425e316b45db6f105daa6f2a0cff)   3 /\* will be cancelled \*/ |
| #define | [BT\_BB\_INTR\_SOURCE](#aca3a7357f242a4e91269736de6545470)   4 /\* BB, level \*/ |
| #define | [BT\_BB\_NMI\_SOURCE](#ab404d2ab995f39616675330f6462dd19)   5 /\* BT BB, NMI, use if BB have bug to fix in NMI \*/ |
| #define | [RWBT\_INTR\_SOURCE](#a14017a5bb9744f9c32138dbdcc09a786)   6 /\* RWBT, level \*/ |
| #define | [RWBLE\_INTR\_SOURCE](#a8cf7f44d512a2c0b215397ae4c37a4f1)   7 /\* RWBLE, level \*/ |
| #define | [RWBT\_NMI\_SOURCE](#a445a79e81929641c372257f4018127f6)   8 /\* RWBT, NMI, use if RWBT has bug to fix in NMI \*/ |
| #define | [RWBLE\_NMI\_SOURCE](#a3b9cef18112f398bd4ada544f3e2b5a0)   9 /\* RWBLE, NMI, use if RWBT has bug to fix in NMI \*/ |
| #define | [SLC0\_INTR\_SOURCE](#a24b7d137ebb32c58d60d5f84a3ce67db)   10 /\* SLC0, level \*/ |
| #define | [SLC1\_INTR\_SOURCE](#a8d8c7fb4a7206356ef7c7b41df4c1b7b)   11 /\* SLC1, level \*/ |
| #define | [UHCI0\_INTR\_SOURCE](#aa714005c0707aaf1ba5b4a033bcb8f81)   12 /\* UHCI0, level \*/ |
| #define | [UHCI1\_INTR\_SOURCE](#a0837c2b982c45380cd89c136d5e9fb2c)   13 /\* UHCI1, level \*/ |
| #define | [TG0\_T0\_LEVEL\_INTR\_SOURCE](#a22bf10410f0b99b9fe398accf66c51b1)   14 /\* TIMER\_GROUP0, TIMER0, level \*/ |
| #define | [TG0\_T1\_LEVEL\_INTR\_SOURCE](#a792cd371542eb8a60e4d381b168ae2b8)   15 /\* TIMER\_GROUP0, TIMER1, level \*/ |
| #define | [TG0\_WDT\_LEVEL\_INTR\_SOURCE](#afc23d5890e9c8029e7d417291193a559)   16 /\* TIMER\_GROUP0, WATCHDOG, level \*/ |
| #define | [TG0\_LACT\_LEVEL\_INTR\_SOURCE](#a8ab5e103356b484d48b68cbafa34d418)   17 /\* TIMER\_GROUP0, LACT, level \*/ |
| #define | [TG1\_T0\_LEVEL\_INTR\_SOURCE](#aee34beaabe47713742eb7633bd8430e3)   18 /\* TIMER\_GROUP1, TIMER0, level \*/ |
| #define | [TG1\_T1\_LEVEL\_INTR\_SOURCE](#a41b4592783755438167ac4444adcaade)   19 /\* TIMER\_GROUP1, TIMER1, level \*/ |
| #define | [TG1\_WDT\_LEVEL\_INTR\_SOURCE](#a68616a67d062b7e57dbe6dd59151b85c)   20 /\* TIMER\_GROUP1, WATCHDOG, level \*/ |
| #define | [TG1\_LACT\_LEVEL\_INTR\_SOURCE](#aa3aeef6dc970aa8c6f7aec839835a384)   21 /\* TIMER\_GROUP1, LACT, level \*/ |
| #define | [GPIO\_INTR\_SOURCE](#a64020d7c1f6557ef6da375f12acf68de)   22 /\* interrupt of GPIO, level \*/ |
| #define | [GPIO\_NMI\_SOURCE](#a23e7de652ab586c903ec999aa8e77e4e)   23 /\* interrupt of GPIO, NMI \*/ |
| #define | [FROM\_CPU\_INTR0\_SOURCE](#a47c9d4be8d21b6f389993db5dbe2883d)   24 /\* int0 from a CPU, level \*/ |
| #define | [FROM\_CPU\_INTR1\_SOURCE](#a2f704a24d6d56f2e13aed56e86e8fb55)   25 /\* int1 from a CPU, level \*/ |
| #define | [FROM\_CPU\_INTR2\_SOURCE](#a470d4f804a7ddb5d107f1cafe8f19308)   26 /\* int2 from a CPU, level, for DPORT Access \*/ |
| #define | [FROM\_CPU\_INTR3\_SOURCE](#a0b8897c96de3f23e794440ef2ef2f523)   27 /\* int3 from a CPU, level, for DPORT Access \*/ |
| #define | [SPI0\_INTR\_SOURCE](#a68709f6f268cf15d132f19f282063e4c)   28 /\* SPI0, level, for $ Access, do not use this \*/ |
| #define | [SPI1\_INTR\_SOURCE](#a5779abc3d34c94cfad763d9ababebb9f)   29 /\* SPI1, level, flash [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)/w, do not use this \*/ |
| #define | [SPI2\_INTR\_SOURCE](#ac5d10660472f10fae0d0511f254b696d)   30 /\* SPI2, level \*/ |
| #define | [SPI3\_INTR\_SOURCE](#a95996e58c94e25db8b2d97de7595996f)   31 /\* SPI3, level \*/ |
| #define | [I2S0\_INTR\_SOURCE](#a6d41fd98988304b2ab82785c24140f8d)   32 /\* I2S0, level \*/ |
| #define | [I2S1\_INTR\_SOURCE](#a3b0877aad4fc7995be0cfb71fabb13a6)   33 /\* I2S1, level \*/ |
| #define | [UART0\_INTR\_SOURCE](#af4569e6b552e35100134e167cf11c7da)   34 /\* UART0, level \*/ |
| #define | [UART1\_INTR\_SOURCE](#ad6f7d29b71a32716058033727bd01dc2)   35 /\* UART1, level \*/ |
| #define | [UART2\_INTR\_SOURCE](#a4a7728c85b344ae5f62684286519f647)   36 /\* UART2, level \*/ |
| #define | [SDIO\_HOST\_INTR\_SOURCE](#a26ce888bf67587b5ab6392f2ea0157c6)   37 /\* SD/SDIO/MMC HOST, level \*/ |
| #define | [ETH\_MAC\_INTR\_SOURCE](#a9953ad6d2f47793c28ef67a280c18ebd)   38 /\* ethernet mac, level \*/ |
| #define | [PWM0\_INTR\_SOURCE](#a29ff03b184368e0a9ad6caf0cc9288ca)   39 /\* PWM0, level, Reserved \*/ |
| #define | [PWM1\_INTR\_SOURCE](#ab9a0099e8acba4831c68af88a073e31d)   40 /\* PWM1, level, Reserved \*/ |
| #define | [PWM2\_INTR\_SOURCE](#a04211cd6f7671713ae845e451c5b008d)   41 /\* PWM2, level \*/ |
| #define | [PWM3\_INTR\_SOURCE](#a95fc4f3d268322f0c0951f188f7eff11)   42 /\* PWM3, level \*/ |
| #define | [LEDC\_INTR\_SOURCE](#a296f3d252d30615dbaea32d61cba9214)   43 /\* LED PWM, level \*/ |
| #define | [EFUSE\_INTR\_SOURCE](#aaf244ea4b63d912e0ce8d59795c79f9d)   44 /\* efuse, level, not likely to use \*/ |
| #define | [TWAI\_INTR\_SOURCE](#a3a56673ee10a809fb2e75065d84b6f8e)   45 /\* twai, level \*/ |
| #define | [CAN\_INTR\_SOURCE](#ab61f6cd5397d79c3b654aef3585ff4a8)   [TWAI\_INTR\_SOURCE](#a3a56673ee10a809fb2e75065d84b6f8e) |
| #define | [RTC\_CORE\_INTR\_SOURCE](#a80d2efc475574efe9250d0048a8a8c12)   46 /\* rtc core, level, include rtc watchdog \*/ |
| #define | [RMT\_INTR\_SOURCE](#ac6d02a2b0f009553a9e52e7842fa959d)   47 /\* remote controller, level \*/ |
| #define | [PCNT\_INTR\_SOURCE](#acfdc02f0268c6145e3ffd5221ce7152f)   48 /\* pulse count, level \*/ |
| #define | [I2C\_EXT0\_INTR\_SOURCE](#a7a706aa628e14e55247d20c9853d76a9)   49 /\* I2C controller1, level \*/ |
| #define | [I2C\_EXT1\_INTR\_SOURCE](#ac0e06a214b3990cb35fa4975e2a85e8e)   50 /\* I2C controller0, level \*/ |
| #define | [RSA\_INTR\_SOURCE](#accd4889d9e375ba16ea00489e7115c30)   51 /\* RSA accelerator, level \*/ |
| #define | [SPI1\_DMA\_INTR\_SOURCE](#a1532868105af99387eb159c1e6e80fe5)   52 /\* SPI1 DMA, for flash [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)/w, do not use it \*/ |
| #define | [SPI2\_DMA\_INTR\_SOURCE](#a7036cef97de80d47ffbdeff6478ccbec)   53 /\* SPI2 DMA, level \*/ |
| #define | [SPI3\_DMA\_INTR\_SOURCE](#a1916307ca85215eb4c995bc4ae83eb50)   54 /\* interrupt of SPI3 DMA, level \*/ |
| #define | [WDT\_INTR\_SOURCE](#a407bd79d5c36e715bcd21a64d8f77c04)   55 /\* will be cancelled \*/ |
| #define | [TIMER1\_INTR\_SOURCE](#a9f5fed8c34c9b971830ab3e083316271)   56 /\* will be cancelled \*/ |
| #define | [TIMER2\_INTR\_SOURCE](#a792de801f5e8339f61a381172782ee06)   57 /\* will be cancelled \*/ |
| #define | [TG0\_T0\_EDGE\_INTR\_SOURCE](#a3930148480a70cd784d84618fcc6ca4d)   58 /\* TIMER\_GROUP0, TIMER0, EDGE \*/ |
| #define | [TG0\_T1\_EDGE\_INTR\_SOURCE](#af32f59d8128f02c0b104adfd84a0e484)   59 /\* TIMER\_GROUP0, TIMER1, EDGE \*/ |
| #define | [TG0\_WDT\_EDGE\_INTR\_SOURCE](#a6f69896f6b8b308d948856e624fc8da6)   60 /\* TIMER\_GROUP0, WATCH DOG, EDGE \*/ |
| #define | [TG0\_LACT\_EDGE\_INTR\_SOURCE](#aaf809080c506a114fe3b47d4d4911873)   61 /\* TIMER\_GROUP0, LACT, EDGE \*/ |
| #define | [TG1\_T0\_EDGE\_INTR\_SOURCE](#a0470cb4879bd92a67e5bd71522c79894)   62 /\* TIMER\_GROUP1, TIMER0, EDGE \*/ |
| #define | [TG1\_T1\_EDGE\_INTR\_SOURCE](#a7315915335a06cbd3302b26eb5056ea1)   63 /\* TIMER\_GROUP1, TIMER1, EDGE \*/ |
| #define | [TG1\_WDT\_EDGE\_INTR\_SOURCE](#a53372a881097f28f5c381879ad065796)   64 /\* TIMER\_GROUP1, WATCHDOG, EDGE \*/ |
| #define | [TG1\_LACT\_EDGE\_INTR\_SOURCE](#a4789654138f3c05bdf28370301971ade)   65 /\* TIMER\_GROUP0, LACT, EDGE \*/ |
| #define | [MMU\_IA\_INTR\_SOURCE](#ace5101394746eb3170217828730eae21)   66 /\* MMU Invalid Access, LEVEL \*/ |
| #define | [MPU\_IA\_INTR\_SOURCE](#af66ad44b93cebc47323913b312f0f020)   67 /\* MPU Invalid Access, LEVEL \*/ |
| #define | [CACHE\_IA\_INTR\_SOURCE](#abc71e0e6d2e6ea7fc39d17297753e72e)   68 /\* Cache Invalid Access, LEVEL \*/ |
| #define | [MAX\_INTR\_SOURCE](#ad57b1f253283c9a65fd95631a11d9532)   69 /\* total number of interrupt sources \*/ |
| #define | [IRQ\_DEFAULT\_PRIORITY](#a2dbeaa0c017cdff0982b381cc96f0a6c)   0 |
| #define | [ESP\_INTR\_FLAG\_SHARED](#afc7bfcea2e621d81336ea6dd23310363)   (1<<8) /\* Interrupt can be shared between ISRs \*/ |

## Macro Definition Documentation

## [◆ ](#aca3a7357f242a4e91269736de6545470)BT\_BB\_INTR\_SOURCE

| #define BT\_BB\_INTR\_SOURCE   4 /\* BB, level \*/ |
| --- |

## [◆ ](#ab404d2ab995f39616675330f6462dd19)BT\_BB\_NMI\_SOURCE

| #define BT\_BB\_NMI\_SOURCE   5 /\* BT BB, NMI, use if BB have bug to fix in NMI \*/ |
| --- |

## [◆ ](#a0b48425e316b45db6f105daa6f2a0cff)BT\_MAC\_INTR\_SOURCE

| #define BT\_MAC\_INTR\_SOURCE   3 /\* will be cancelled \*/ |
| --- |

## [◆ ](#abc71e0e6d2e6ea7fc39d17297753e72e)CACHE\_IA\_INTR\_SOURCE

| #define CACHE\_IA\_INTR\_SOURCE   68 /\* Cache Invalid Access, LEVEL \*/ |
| --- |

## [◆ ](#ab61f6cd5397d79c3b654aef3585ff4a8)CAN\_INTR\_SOURCE

| #define CAN\_INTR\_SOURCE   [TWAI\_INTR\_SOURCE](#a3a56673ee10a809fb2e75065d84b6f8e) |
| --- |

## [◆ ](#aaf244ea4b63d912e0ce8d59795c79f9d)EFUSE\_INTR\_SOURCE

| #define EFUSE\_INTR\_SOURCE   44 /\* efuse, level, not likely to use \*/ |
| --- |

## [◆ ](#afc7bfcea2e621d81336ea6dd23310363)ESP\_INTR\_FLAG\_SHARED

| #define ESP\_INTR\_FLAG\_SHARED   (1<<8) /\* Interrupt can be shared between ISRs \*/ |
| --- |

## [◆ ](#a9953ad6d2f47793c28ef67a280c18ebd)ETH\_MAC\_INTR\_SOURCE

| #define ETH\_MAC\_INTR\_SOURCE   38 /\* ethernet mac, level \*/ |
| --- |

## [◆ ](#a47c9d4be8d21b6f389993db5dbe2883d)FROM\_CPU\_INTR0\_SOURCE

| #define FROM\_CPU\_INTR0\_SOURCE   24 /\* int0 from a CPU, level \*/ |
| --- |

## [◆ ](#a2f704a24d6d56f2e13aed56e86e8fb55)FROM\_CPU\_INTR1\_SOURCE

| #define FROM\_CPU\_INTR1\_SOURCE   25 /\* int1 from a CPU, level \*/ |
| --- |

## [◆ ](#a470d4f804a7ddb5d107f1cafe8f19308)FROM\_CPU\_INTR2\_SOURCE

| #define FROM\_CPU\_INTR2\_SOURCE   26 /\* int2 from a CPU, level, for DPORT Access \*/ |
| --- |

## [◆ ](#a0b8897c96de3f23e794440ef2ef2f523)FROM\_CPU\_INTR3\_SOURCE

| #define FROM\_CPU\_INTR3\_SOURCE   27 /\* int3 from a CPU, level, for DPORT Access \*/ |
| --- |

## [◆ ](#a64020d7c1f6557ef6da375f12acf68de)GPIO\_INTR\_SOURCE

| #define GPIO\_INTR\_SOURCE   22 /\* interrupt of GPIO, level \*/ |
| --- |

## [◆ ](#a23e7de652ab586c903ec999aa8e77e4e)GPIO\_NMI\_SOURCE

| #define GPIO\_NMI\_SOURCE   23 /\* interrupt of GPIO, NMI \*/ |
| --- |

## [◆ ](#a7a706aa628e14e55247d20c9853d76a9)I2C\_EXT0\_INTR\_SOURCE

| #define I2C\_EXT0\_INTR\_SOURCE   49 /\* I2C controller1, level \*/ |
| --- |

## [◆ ](#ac0e06a214b3990cb35fa4975e2a85e8e)I2C\_EXT1\_INTR\_SOURCE

| #define I2C\_EXT1\_INTR\_SOURCE   50 /\* I2C controller0, level \*/ |
| --- |

## [◆ ](#a6d41fd98988304b2ab82785c24140f8d)I2S0\_INTR\_SOURCE

| #define I2S0\_INTR\_SOURCE   32 /\* I2S0, level \*/ |
| --- |

## [◆ ](#a3b0877aad4fc7995be0cfb71fabb13a6)I2S1\_INTR\_SOURCE

| #define I2S1\_INTR\_SOURCE   33 /\* I2S1, level \*/ |
| --- |

## [◆ ](#a2dbeaa0c017cdff0982b381cc96f0a6c)IRQ\_DEFAULT\_PRIORITY

| #define IRQ\_DEFAULT\_PRIORITY   0 |
| --- |

## [◆ ](#a296f3d252d30615dbaea32d61cba9214)LEDC\_INTR\_SOURCE

| #define LEDC\_INTR\_SOURCE   43 /\* LED PWM, level \*/ |
| --- |

## [◆ ](#ad57b1f253283c9a65fd95631a11d9532)MAX\_INTR\_SOURCE

| #define MAX\_INTR\_SOURCE   69 /\* total number of interrupt sources \*/ |
| --- |

## [◆ ](#ace5101394746eb3170217828730eae21)MMU\_IA\_INTR\_SOURCE

| #define MMU\_IA\_INTR\_SOURCE   66 /\* MMU Invalid Access, LEVEL \*/ |
| --- |

## [◆ ](#af66ad44b93cebc47323913b312f0f020)MPU\_IA\_INTR\_SOURCE

| #define MPU\_IA\_INTR\_SOURCE   67 /\* MPU Invalid Access, LEVEL \*/ |
| --- |

## [◆ ](#acfdc02f0268c6145e3ffd5221ce7152f)PCNT\_INTR\_SOURCE

| #define PCNT\_INTR\_SOURCE   48 /\* pulse count, level \*/ |
| --- |

## [◆ ](#a29ff03b184368e0a9ad6caf0cc9288ca)PWM0\_INTR\_SOURCE

| #define PWM0\_INTR\_SOURCE   39 /\* PWM0, level, Reserved \*/ |
| --- |

## [◆ ](#ab9a0099e8acba4831c68af88a073e31d)PWM1\_INTR\_SOURCE

| #define PWM1\_INTR\_SOURCE   40 /\* PWM1, level, Reserved \*/ |
| --- |

## [◆ ](#a04211cd6f7671713ae845e451c5b008d)PWM2\_INTR\_SOURCE

| #define PWM2\_INTR\_SOURCE   41 /\* PWM2, level \*/ |
| --- |

## [◆ ](#a95fc4f3d268322f0c0951f188f7eff11)PWM3\_INTR\_SOURCE

| #define PWM3\_INTR\_SOURCE   42 /\* PWM3, level \*/ |
| --- |

## [◆ ](#ac6d02a2b0f009553a9e52e7842fa959d)RMT\_INTR\_SOURCE

| #define RMT\_INTR\_SOURCE   47 /\* remote controller, level \*/ |
| --- |

## [◆ ](#accd4889d9e375ba16ea00489e7115c30)RSA\_INTR\_SOURCE

| #define RSA\_INTR\_SOURCE   51 /\* RSA accelerator, level \*/ |
| --- |

## [◆ ](#a80d2efc475574efe9250d0048a8a8c12)RTC\_CORE\_INTR\_SOURCE

| #define RTC\_CORE\_INTR\_SOURCE   46 /\* rtc core, level, include rtc watchdog \*/ |
| --- |

## [◆ ](#a8cf7f44d512a2c0b215397ae4c37a4f1)RWBLE\_INTR\_SOURCE

| #define RWBLE\_INTR\_SOURCE   7 /\* RWBLE, level \*/ |
| --- |

## [◆ ](#a3b9cef18112f398bd4ada544f3e2b5a0)RWBLE\_NMI\_SOURCE

| #define RWBLE\_NMI\_SOURCE   9 /\* RWBLE, NMI, use if RWBT has bug to fix in NMI \*/ |
| --- |

## [◆ ](#a14017a5bb9744f9c32138dbdcc09a786)RWBT\_INTR\_SOURCE

| #define RWBT\_INTR\_SOURCE   6 /\* RWBT, level \*/ |
| --- |

## [◆ ](#a445a79e81929641c372257f4018127f6)RWBT\_NMI\_SOURCE

| #define RWBT\_NMI\_SOURCE   8 /\* RWBT, NMI, use if RWBT has bug to fix in NMI \*/ |
| --- |

## [◆ ](#a26ce888bf67587b5ab6392f2ea0157c6)SDIO\_HOST\_INTR\_SOURCE

| #define SDIO\_HOST\_INTR\_SOURCE   37 /\* SD/SDIO/MMC HOST, level \*/ |
| --- |

## [◆ ](#a24b7d137ebb32c58d60d5f84a3ce67db)SLC0\_INTR\_SOURCE

| #define SLC0\_INTR\_SOURCE   10 /\* SLC0, level \*/ |
| --- |

## [◆ ](#a8d8c7fb4a7206356ef7c7b41df4c1b7b)SLC1\_INTR\_SOURCE

| #define SLC1\_INTR\_SOURCE   11 /\* SLC1, level \*/ |
| --- |

## [◆ ](#a68709f6f268cf15d132f19f282063e4c)SPI0\_INTR\_SOURCE

| #define SPI0\_INTR\_SOURCE   28 /\* SPI0, level, for $ Access, do not use this \*/ |
| --- |

## [◆ ](#a1532868105af99387eb159c1e6e80fe5)SPI1\_DMA\_INTR\_SOURCE

| #define SPI1\_DMA\_INTR\_SOURCE   52 /\* SPI1 DMA, for flash [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)/w, do not use it \*/ |
| --- |

## [◆ ](#a5779abc3d34c94cfad763d9ababebb9f)SPI1\_INTR\_SOURCE

| #define SPI1\_INTR\_SOURCE   29 /\* SPI1, level, flash [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)/w, do not use this \*/ |
| --- |

## [◆ ](#a7036cef97de80d47ffbdeff6478ccbec)SPI2\_DMA\_INTR\_SOURCE

| #define SPI2\_DMA\_INTR\_SOURCE   53 /\* SPI2 DMA, level \*/ |
| --- |

## [◆ ](#ac5d10660472f10fae0d0511f254b696d)SPI2\_INTR\_SOURCE

| #define SPI2\_INTR\_SOURCE   30 /\* SPI2, level \*/ |
| --- |

## [◆ ](#a1916307ca85215eb4c995bc4ae83eb50)SPI3\_DMA\_INTR\_SOURCE

| #define SPI3\_DMA\_INTR\_SOURCE   54 /\* interrupt of SPI3 DMA, level \*/ |
| --- |

## [◆ ](#a95996e58c94e25db8b2d97de7595996f)SPI3\_INTR\_SOURCE

| #define SPI3\_INTR\_SOURCE   31 /\* SPI3, level \*/ |
| --- |

## [◆ ](#aaf809080c506a114fe3b47d4d4911873)TG0\_LACT\_EDGE\_INTR\_SOURCE

| #define TG0\_LACT\_EDGE\_INTR\_SOURCE   61 /\* TIMER\_GROUP0, LACT, EDGE \*/ |
| --- |

## [◆ ](#a8ab5e103356b484d48b68cbafa34d418)TG0\_LACT\_LEVEL\_INTR\_SOURCE

| #define TG0\_LACT\_LEVEL\_INTR\_SOURCE   17 /\* TIMER\_GROUP0, LACT, level \*/ |
| --- |

## [◆ ](#a3930148480a70cd784d84618fcc6ca4d)TG0\_T0\_EDGE\_INTR\_SOURCE

| #define TG0\_T0\_EDGE\_INTR\_SOURCE   58 /\* TIMER\_GROUP0, TIMER0, EDGE \*/ |
| --- |

## [◆ ](#a22bf10410f0b99b9fe398accf66c51b1)TG0\_T0\_LEVEL\_INTR\_SOURCE

| #define TG0\_T0\_LEVEL\_INTR\_SOURCE   14 /\* TIMER\_GROUP0, TIMER0, level \*/ |
| --- |

## [◆ ](#af32f59d8128f02c0b104adfd84a0e484)TG0\_T1\_EDGE\_INTR\_SOURCE

| #define TG0\_T1\_EDGE\_INTR\_SOURCE   59 /\* TIMER\_GROUP0, TIMER1, EDGE \*/ |
| --- |

## [◆ ](#a792cd371542eb8a60e4d381b168ae2b8)TG0\_T1\_LEVEL\_INTR\_SOURCE

| #define TG0\_T1\_LEVEL\_INTR\_SOURCE   15 /\* TIMER\_GROUP0, TIMER1, level \*/ |
| --- |

## [◆ ](#a6f69896f6b8b308d948856e624fc8da6)TG0\_WDT\_EDGE\_INTR\_SOURCE

| #define TG0\_WDT\_EDGE\_INTR\_SOURCE   60 /\* TIMER\_GROUP0, WATCH DOG, EDGE \*/ |
| --- |

## [◆ ](#afc23d5890e9c8029e7d417291193a559)TG0\_WDT\_LEVEL\_INTR\_SOURCE

| #define TG0\_WDT\_LEVEL\_INTR\_SOURCE   16 /\* TIMER\_GROUP0, WATCHDOG, level \*/ |
| --- |

## [◆ ](#a4789654138f3c05bdf28370301971ade)TG1\_LACT\_EDGE\_INTR\_SOURCE

| #define TG1\_LACT\_EDGE\_INTR\_SOURCE   65 /\* TIMER\_GROUP0, LACT, EDGE \*/ |
| --- |

## [◆ ](#aa3aeef6dc970aa8c6f7aec839835a384)TG1\_LACT\_LEVEL\_INTR\_SOURCE

| #define TG1\_LACT\_LEVEL\_INTR\_SOURCE   21 /\* TIMER\_GROUP1, LACT, level \*/ |
| --- |

## [◆ ](#a0470cb4879bd92a67e5bd71522c79894)TG1\_T0\_EDGE\_INTR\_SOURCE

| #define TG1\_T0\_EDGE\_INTR\_SOURCE   62 /\* TIMER\_GROUP1, TIMER0, EDGE \*/ |
| --- |

## [◆ ](#aee34beaabe47713742eb7633bd8430e3)TG1\_T0\_LEVEL\_INTR\_SOURCE

| #define TG1\_T0\_LEVEL\_INTR\_SOURCE   18 /\* TIMER\_GROUP1, TIMER0, level \*/ |
| --- |

## [◆ ](#a7315915335a06cbd3302b26eb5056ea1)TG1\_T1\_EDGE\_INTR\_SOURCE

| #define TG1\_T1\_EDGE\_INTR\_SOURCE   63 /\* TIMER\_GROUP1, TIMER1, EDGE \*/ |
| --- |

## [◆ ](#a41b4592783755438167ac4444adcaade)TG1\_T1\_LEVEL\_INTR\_SOURCE

| #define TG1\_T1\_LEVEL\_INTR\_SOURCE   19 /\* TIMER\_GROUP1, TIMER1, level \*/ |
| --- |

## [◆ ](#a53372a881097f28f5c381879ad065796)TG1\_WDT\_EDGE\_INTR\_SOURCE

| #define TG1\_WDT\_EDGE\_INTR\_SOURCE   64 /\* TIMER\_GROUP1, WATCHDOG, EDGE \*/ |
| --- |

## [◆ ](#a68616a67d062b7e57dbe6dd59151b85c)TG1\_WDT\_LEVEL\_INTR\_SOURCE

| #define TG1\_WDT\_LEVEL\_INTR\_SOURCE   20 /\* TIMER\_GROUP1, WATCHDOG, level \*/ |
| --- |

## [◆ ](#a9f5fed8c34c9b971830ab3e083316271)TIMER1\_INTR\_SOURCE

| #define TIMER1\_INTR\_SOURCE   56 /\* will be cancelled \*/ |
| --- |

## [◆ ](#a792de801f5e8339f61a381172782ee06)TIMER2\_INTR\_SOURCE

| #define TIMER2\_INTR\_SOURCE   57 /\* will be cancelled \*/ |
| --- |

## [◆ ](#a3a56673ee10a809fb2e75065d84b6f8e)TWAI\_INTR\_SOURCE

| #define TWAI\_INTR\_SOURCE   45 /\* twai, level \*/ |
| --- |

## [◆ ](#af4569e6b552e35100134e167cf11c7da)UART0\_INTR\_SOURCE

| #define UART0\_INTR\_SOURCE   34 /\* UART0, level \*/ |
| --- |

## [◆ ](#ad6f7d29b71a32716058033727bd01dc2)UART1\_INTR\_SOURCE

| #define UART1\_INTR\_SOURCE   35 /\* UART1, level \*/ |
| --- |

## [◆ ](#a4a7728c85b344ae5f62684286519f647)UART2\_INTR\_SOURCE

| #define UART2\_INTR\_SOURCE   36 /\* UART2, level \*/ |
| --- |

## [◆ ](#aa714005c0707aaf1ba5b4a033bcb8f81)UHCI0\_INTR\_SOURCE

| #define UHCI0\_INTR\_SOURCE   12 /\* UHCI0, level \*/ |
| --- |

## [◆ ](#a0837c2b982c45380cd89c136d5e9fb2c)UHCI1\_INTR\_SOURCE

| #define UHCI1\_INTR\_SOURCE   13 /\* UHCI1, level \*/ |
| --- |

## [◆ ](#a407bd79d5c36e715bcd21a64d8f77c04)WDT\_INTR\_SOURCE

| #define WDT\_INTR\_SOURCE   55 /\* will be cancelled \*/ |
| --- |

## [◆ ](#a5383f7fa77bc12a8301c54e0dfb66306)WIFI\_BB\_INTR\_SOURCE

| #define WIFI\_BB\_INTR\_SOURCE   2 /\* WiFi BB, level, we can do some calibration \*/ |
| --- |

## [◆ ](#ad000d08efc3e8a5fc56da537973a5cb8)WIFI\_MAC\_INTR\_SOURCE

| #define WIFI\_MAC\_INTR\_SOURCE   0 /\* WiFi MAC, level \*/ |
| --- |

## [◆ ](#abfc935ef2963ee54b6a1f1279b4887ff)WIFI\_MAC\_NMI\_SOURCE

| #define WIFI\_MAC\_NMI\_SOURCE   1 /\* WiFi MAC, NMI, use if MAC needs fix in NMI \*/ |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [esp-xtensa-intmux.h](esp-xtensa-intmux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
