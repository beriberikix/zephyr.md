---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/esp32s2-xtensa-intmux_8h.html
original_path: doxygen/html/esp32s2-xtensa-intmux_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32s2-xtensa-intmux.h File Reference

[Go to the source code of this file.](esp32s2-xtensa-intmux_8h_source.md)

| Macros | |
| --- | --- |
| #define | [WIFI\_MAC\_INTR\_SOURCE](#ad000d08efc3e8a5fc56da537973a5cb8)   0 /\* WiFi MAC, level \*/ |
| #define | [WIFI\_MAC\_NMI\_SOURCE](#abfc935ef2963ee54b6a1f1279b4887ff)   1 /\* WiFi MAC, NMI, use if MAC needs fix in NMI \*/ |
| #define | [WIFI\_PWR\_INTR\_SOURCE](#af3cef5f23f39a396dec2a356f395ef69)   2 |
| #define | [WIFI\_BB\_INTR\_SOURCE](#a5383f7fa77bc12a8301c54e0dfb66306)   3 /\* WiFi BB, level, we can do some calibration \*/ |
| #define | [BT\_MAC\_INTR\_SOURCE](#a0b48425e316b45db6f105daa6f2a0cff)   4 /\* will be cancelled \*/ |
| #define | [BT\_BB\_INTR\_SOURCE](#aca3a7357f242a4e91269736de6545470)   5 /\* BB, level \*/ |
| #define | [BT\_BB\_NMI\_SOURCE](#ab404d2ab995f39616675330f6462dd19)   6 /\* BT BB, NMI, use if BB have bug to fix in NMI \*/ |
| #define | [RWBT\_INTR\_SOURCE](#a14017a5bb9744f9c32138dbdcc09a786)   7 /\* RWBT, level \*/ |
| #define | [RWBLE\_INTR\_SOURCE](#a8cf7f44d512a2c0b215397ae4c37a4f1)   8 /\* RWBLE, level \*/ |
| #define | [RWBT\_NMI\_SOURCE](#a445a79e81929641c372257f4018127f6)   9 /\* RWBT, NMI, use if RWBT has bug to fix in NMI \*/ |
| #define | [RWBLE\_NMI\_SOURCE](#a3b9cef18112f398bd4ada544f3e2b5a0)   10 /\* RWBLE, NMI, use if RWBT has bug to fix in NMI \*/ |
| #define | [SLC0\_INTR\_SOURCE](#a24b7d137ebb32c58d60d5f84a3ce67db)   11 /\* SLC0, level \*/ |
| #define | [SLC1\_INTR\_SOURCE](#a8d8c7fb4a7206356ef7c7b41df4c1b7b)   12 /\* SLC1, level \*/ |
| #define | [UHCI0\_INTR\_SOURCE](#aa714005c0707aaf1ba5b4a033bcb8f81)   13 /\* UHCI0, level \*/ |
| #define | [UHCI1\_INTR\_SOURCE](#a0837c2b982c45380cd89c136d5e9fb2c)   14 /\* UHCI1, level \*/ |
| #define | [TG0\_T0\_LEVEL\_INTR\_SOURCE](#a22bf10410f0b99b9fe398accf66c51b1)   15 /\* TIMER\_GROUP0, TIMER0, level \*/ |
| #define | [TG0\_T1\_LEVEL\_INTR\_SOURCE](#a792cd371542eb8a60e4d381b168ae2b8)   16 /\* TIMER\_GROUP0, TIMER1, level \*/ |
| #define | [TG0\_WDT\_LEVEL\_INTR\_SOURCE](#afc23d5890e9c8029e7d417291193a559)   17 /\* TIMER\_GROUP0, WATCHDOG, level \*/ |
| #define | [TG0\_LACT\_LEVEL\_INTR\_SOURCE](#a8ab5e103356b484d48b68cbafa34d418)   18 /\* TIMER\_GROUP0, LACT, level \*/ |
| #define | [TG1\_T0\_LEVEL\_INTR\_SOURCE](#aee34beaabe47713742eb7633bd8430e3)   19 /\* TIMER\_GROUP1, TIMER0, level \*/ |
| #define | [TG1\_T1\_LEVEL\_INTR\_SOURCE](#a41b4592783755438167ac4444adcaade)   20 /\* TIMER\_GROUP1, TIMER1, level \*/ |
| #define | [TG1\_WDT\_LEVEL\_INTR\_SOURCE](#a68616a67d062b7e57dbe6dd59151b85c)   21 /\* TIMER\_GROUP1, WATCHDOG, level \*/ |
| #define | [TG1\_LACT\_LEVEL\_INTR\_SOURCE](#aa3aeef6dc970aa8c6f7aec839835a384)   22 /\* TIMER\_GROUP1, LACT, level \*/ |
| #define | [GPIO\_INTR\_SOURCE](#a64020d7c1f6557ef6da375f12acf68de)   23 /\* interrupt of GPIO, level \*/ |
| #define | [GPIO\_NMI\_SOURCE](#a23e7de652ab586c903ec999aa8e77e4e)   24 /\* interrupt of GPIO, NMI \*/ |
| #define | [GPIO\_INTR\_SOURCE2](#afb98fcf1a9be6030f5ca87dea6675974)   25 /\* interrupt of GPIO, level \*/ |
| #define | [GPIO\_NMI\_SOURCE2](#ad11e04bc97a0115966929013f06efa50)   26 /\* interrupt of GPIO, NMI \*/ |
| #define | [DEDICATED\_GPIO\_INTR\_SOURCE](#a5b31ad0ece8c26e3e1600837bc1121bb)   27 /\* interrupt of dedicated GPIO, level \*/ |
| #define | [FROM\_CPU\_INTR0\_SOURCE](#a47c9d4be8d21b6f389993db5dbe2883d)   28 /\* int0 from a CPU, level \*/ |
| #define | [FROM\_CPU\_INTR1\_SOURCE](#a2f704a24d6d56f2e13aed56e86e8fb55)   29 /\* int1 from a CPU, level \*/ |
| #define | [FROM\_CPU\_INTR2\_SOURCE](#a470d4f804a7ddb5d107f1cafe8f19308)   30 /\* int2 from a CPU, level, for DPORT Access \*/ |
| #define | [FROM\_CPU\_INTR3\_SOURCE](#a0b8897c96de3f23e794440ef2ef2f523)   31 /\* int3 from a CPU, level, for DPORT Access \*/ |
| #define | [SPI1\_INTR\_SOURCE](#a5779abc3d34c94cfad763d9ababebb9f)   32 /\* SPI1, level, flash [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)/w, do not use this \*/ |
| #define | [SPI2\_INTR\_SOURCE](#ac5d10660472f10fae0d0511f254b696d)   33 /\* SPI2, level \*/ |
| #define | [SPI3\_INTR\_SOURCE](#a95996e58c94e25db8b2d97de7595996f)   34 /\* SPI3, level \*/ |
| #define | [I2S0\_INTR\_SOURCE](#a6d41fd98988304b2ab82785c24140f8d)   35 /\* I2S0, level \*/ |
| #define | [I2S1\_INTR\_SOURCE](#a3b0877aad4fc7995be0cfb71fabb13a6)   36 /\* I2S1, level \*/ |
| #define | [UART0\_INTR\_SOURCE](#af4569e6b552e35100134e167cf11c7da)   37 /\* UART0, level \*/ |
| #define | [UART1\_INTR\_SOURCE](#ad6f7d29b71a32716058033727bd01dc2)   38 /\* UART1, level \*/ |
| #define | [UART2\_INTR\_SOURCE](#a4a7728c85b344ae5f62684286519f647)   39 /\* UART2, level \*/ |
| #define | [SDIO\_HOST\_INTR\_SOURCE](#a26ce888bf67587b5ab6392f2ea0157c6)   40 /\* SD/SDIO/MMC HOST, level \*/ |
| #define | [PWM0\_INTR\_SOURCE](#a29ff03b184368e0a9ad6caf0cc9288ca)   41 /\* PWM0, level, Reserved \*/ |
| #define | [PWM1\_INTR\_SOURCE](#ab9a0099e8acba4831c68af88a073e31d)   42 /\* PWM1, level, Reserved \*/ |
| #define | [PWM2\_INTR\_SOURCE](#a04211cd6f7671713ae845e451c5b008d)   43 /\* PWM2, level \*/ |
| #define | [PWM3\_INTR\_SOURCE](#a95fc4f3d268322f0c0951f188f7eff11)   44 /\* PWM3, level \*/ |
| #define | [LEDC\_INTR\_SOURCE](#a296f3d252d30615dbaea32d61cba9214)   45 /\* LED PWM, level \*/ |
| #define | [EFUSE\_INTR\_SOURCE](#aaf244ea4b63d912e0ce8d59795c79f9d)   46 /\* efuse, level, not likely to use \*/ |
| #define | [TWAI\_INTR\_SOURCE](#a3a56673ee10a809fb2e75065d84b6f8e)   47 /\* twai, level \*/ |
| #define | [USB\_INTR\_SOURCE](#a7a020da508049560356d36ab9607bca9)   48 /\* interrupt of USB, level \*/ |
| #define | [RTC\_CORE\_INTR\_SOURCE](#a80d2efc475574efe9250d0048a8a8c12)   49 /\* rtc core, level, include rtc watchdog \*/ |
| #define | [RMT\_INTR\_SOURCE](#ac6d02a2b0f009553a9e52e7842fa959d)   50 /\* remote controller, level \*/ |
| #define | [PCNT\_INTR\_SOURCE](#acfdc02f0268c6145e3ffd5221ce7152f)   51 /\* pulse count, level \*/ |
| #define | [I2C\_EXT0\_INTR\_SOURCE](#a7a706aa628e14e55247d20c9853d76a9)   52 /\* I2C controller1, level \*/ |
| #define | [I2C\_EXT1\_INTR\_SOURCE](#ac0e06a214b3990cb35fa4975e2a85e8e)   53 /\* I2C controller0, level \*/ |
| #define | [RSA\_INTR\_SOURCE](#accd4889d9e375ba16ea00489e7115c30)   54 /\* RSA accelerator, level \*/ |
| #define | [SHA\_INTR\_SOURCE](#a59f92ba6a2f4b3fa9454558f37ff3e24)   55 /\* interrupt of RSA accelerator, level \*/ |
| #define | [AES\_INTR\_SOURCE](#ad793803f54262a4dcf6b14140e9dc22b)   56 /\* interrupt of SHA accelerator, level \*/ |
| #define | [SPI2\_DMA\_INTR\_SOURCE](#a7036cef97de80d47ffbdeff6478ccbec)   57 /\* SPI2 DMA, level \*/ |
| #define | [SPI3\_DMA\_INTR\_SOURCE](#a1916307ca85215eb4c995bc4ae83eb50)   58 /\* interrupt of SPI3 DMA, level \*/ |
| #define | [WDT\_INTR\_SOURCE](#a407bd79d5c36e715bcd21a64d8f77c04)   59 /\* will be cancelled \*/ |
| #define | [TIMER1\_INTR\_SOURCE](#a9f5fed8c34c9b971830ab3e083316271)   60 /\* will be cancelled \*/ |
| #define | [TIMER2\_INTR\_SOURCE](#a792de801f5e8339f61a381172782ee06)   61 /\* will be cancelled \*/ |
| #define | [TG0\_T0\_EDGE\_INTR\_SOURCE](#a3930148480a70cd784d84618fcc6ca4d)   62 /\* TIMER\_GROUP0, TIMER0, EDGE \*/ |
| #define | [TG0\_T1\_EDGE\_INTR\_SOURCE](#af32f59d8128f02c0b104adfd84a0e484)   63 /\* TIMER\_GROUP0, TIMER1, EDGE \*/ |
| #define | [TG0\_WDT\_EDGE\_INTR\_SOURCE](#a6f69896f6b8b308d948856e624fc8da6)   64 /\* TIMER\_GROUP0, WATCH DOG, EDGE \*/ |
| #define | [TG0\_LACT\_EDGE\_INTR\_SOURCE](#aaf809080c506a114fe3b47d4d4911873)   65 /\* TIMER\_GROUP0, LACT, EDGE \*/ |
| #define | [TG1\_T0\_EDGE\_INTR\_SOURCE](#a0470cb4879bd92a67e5bd71522c79894)   66 /\* TIMER\_GROUP1, TIMER0, EDGE \*/ |
| #define | [TG1\_T1\_EDGE\_INTR\_SOURCE](#a7315915335a06cbd3302b26eb5056ea1)   67 /\* TIMER\_GROUP1, TIMER1, EDGE \*/ |
| #define | [TG1\_WDT\_EDGE\_INTR\_SOURCE](#a53372a881097f28f5c381879ad065796)   68 /\* TIMER\_GROUP1, WATCHDOG, EDGE \*/ |
| #define | [TG1\_LACT\_EDGE\_INTR\_SOURCE](#a4789654138f3c05bdf28370301971ade)   69 /\* TIMER\_GROUP0, LACT, EDGE \*/ |
| #define | [CACHE\_IA\_INTR\_SOURCE](#abc71e0e6d2e6ea7fc39d17297753e72e)   70 /\* Cache Invalid Access, level \*/ |
| #define | [SYSTIMER\_TARGET0\_EDGE\_INTR\_SOURCE](#a4cb07c15412c22b4939bb5a1e782f6e7)   71 /\* system timer 0, edge \*/ |
| #define | [SYSTIMER\_TARGET1\_EDGE\_INTR\_SOURCE](#a4ae5acb4be5a37cc87deb29ca61c8034)   72 /\* system timer 1, edge \*/ |
| #define | [SYSTIMER\_TARGET2\_EDGE\_INTR\_SOURCE](#a3c07aba15f9a2e9bc4a97031a241b512)   73 /\* system timer 2, edge \*/ |
| #define | [ASSIST\_DEBUG\_INTR\_SOURCE](#ab627766f8e6b851882c42596d7df540c)   74 /\* Assist debug module, level \*/ |
| #define | [PMS\_PRO\_IRAM0\_ILG\_INTR\_SOURCE](#aa7415869e67d460c0ed4c7e96810291a)   75 /\* illegal IRAM1 access, level \*/ |
| #define | [PMS\_PRO\_DRAM0\_ILG\_INTR\_SOURCE](#a7ab3b2f26d6ce8bc8f9ea83ff4c3a900)   76 /\* illegal DRAM0 access, level \*/ |
| #define | [PMS\_PRO\_DPORT\_ILG\_INTR\_SOURCE](#acf9bfdff3964eeacafede5571615bdd6)   77 /\* illegal DPORT access, level \*/ |
| #define | [PMS\_PRO\_AHB\_ILG\_INTR\_SOURCE](#ab4e4c60433d57d03b386d5bd9ab71370)   78 /\* illegal AHB access, level \*/ |
| #define | [PMS\_PRO\_CACHE\_ILG\_INTR\_SOURCE](#ab2491671f5770a21823adc01763af792)   79 /\* illegal CACHE access, level \*/ |
| #define | [PMS\_DMA\_APB\_I\_ILG\_INTR\_SOURCE](#a9c4f6388dd7312fdc4219cff984166a9)   80 /\* illegal APB access, level \*/ |
| #define | [PMS\_DMA\_RX\_I\_ILG\_INTR\_SOURCE](#a8d6a4e0e0994f8a55fd7ca4ce5a45399)   81 /\* illegal DMA RX access, level \*/ |
| #define | [PMS\_DMA\_TX\_I\_ILG\_INTR\_SOURCE](#aac17e93da6a160da2d85a43d4ddc8289)   82 /\* illegal DMA TX access, level \*/ |
| #define | [SPI\_MEM\_REJECT\_CACHE\_INTR\_SOURCE](#a36c488ff1605277f2772b1f80552f6ac) |
| #define | [DMA\_COPY\_INTR\_SOURCE](#a03fc7ea80cff3be1cdf02d5f97434c71)   84 /\* DMA copy, level \*/ |
| #define | [SPI4\_DMA\_INTR\_SOURCE](#a9f521721b77fef0f3c19bea05a12e850)   85 /\* SPI4 DMA, level \*/ |
| #define | [SPI4\_INTR\_SOURCE](#a334a2d6fa713f6df7c46c96465a2d6b9)   86 /\* SPI4, level \*/ |
| #define | [ICACHE\_PRELOAD\_INTR\_SOURCE](#a344601acd9e077b22b5f2d2627d9032e)   87 /\* ICache preload operation, level \*/ |
| #define | [DCACHE\_PRELOAD\_INTR\_SOURCE](#adecb822591c0c4bf063d67b2e74e9a40)   88 /\* DCache preload operation, level \*/ |
| #define | [APB\_ADC\_INTR\_SOURCE](#a68b408eb63057838c64c51718c5b1f7f)   89 /\* APB ADC, level \*/ |
| #define | [CRYPTO\_DMA\_INTR\_SOURCE](#ad81b659cea69558a9accb6cd9315b236)   90 /\* encrypted DMA, level \*/ |
| #define | [CPU\_PERI\_ERROR\_INTR\_SOURCE](#a1334dc20d35277646113e699619d8856)   91 /\* CPU peripherals error, level \*/ |
| #define | [APB\_PERI\_ERROR\_INTR\_SOURCE](#aefeb2487d77e00408d4b7f2faa4f840f)   92 /\* APB peripherals error, level \*/ |
| #define | [DCACHE\_SYNC\_INTR\_SOURCE](#a93a4db93be7bef5cdc22cc2854da84b6)   93 /\* data cache sync done, level \*/ |
| #define | [ICACHE\_SYNC\_INTR\_SOURCE](#a8299c36b90f9e08bc421e527f69545bb)   94 /\* instruction cache sync done, level \*/ |
| #define | [MAX\_INTR\_SOURCE](#ad57b1f253283c9a65fd95631a11d9532)   95 /\* total number of interrupt sources \*/ |
| #define | [IRQ\_DEFAULT\_PRIORITY](#a2dbeaa0c017cdff0982b381cc96f0a6c)   0 |
| #define | [ESP\_INTR\_FLAG\_SHARED](#afc7bfcea2e621d81336ea6dd23310363)   (1<<8) /\* Interrupt can be shared between ISRs \*/ |

## Macro Definition Documentation

## [◆ ](#ad793803f54262a4dcf6b14140e9dc22b)AES\_INTR\_SOURCE

| #define AES\_INTR\_SOURCE   56 /\* interrupt of SHA accelerator, level \*/ |
| --- |

## [◆ ](#a68b408eb63057838c64c51718c5b1f7f)APB\_ADC\_INTR\_SOURCE

| #define APB\_ADC\_INTR\_SOURCE   89 /\* APB ADC, level \*/ |
| --- |

## [◆ ](#aefeb2487d77e00408d4b7f2faa4f840f)APB\_PERI\_ERROR\_INTR\_SOURCE

| #define APB\_PERI\_ERROR\_INTR\_SOURCE   92 /\* APB peripherals error, level \*/ |
| --- |

## [◆ ](#ab627766f8e6b851882c42596d7df540c)ASSIST\_DEBUG\_INTR\_SOURCE

| #define ASSIST\_DEBUG\_INTR\_SOURCE   74 /\* Assist debug module, level \*/ |
| --- |

## [◆ ](#aca3a7357f242a4e91269736de6545470)BT\_BB\_INTR\_SOURCE

| #define BT\_BB\_INTR\_SOURCE   5 /\* BB, level \*/ |
| --- |

## [◆ ](#ab404d2ab995f39616675330f6462dd19)BT\_BB\_NMI\_SOURCE

| #define BT\_BB\_NMI\_SOURCE   6 /\* BT BB, NMI, use if BB have bug to fix in NMI \*/ |
| --- |

## [◆ ](#a0b48425e316b45db6f105daa6f2a0cff)BT\_MAC\_INTR\_SOURCE

| #define BT\_MAC\_INTR\_SOURCE   4 /\* will be cancelled \*/ |
| --- |

## [◆ ](#abc71e0e6d2e6ea7fc39d17297753e72e)CACHE\_IA\_INTR\_SOURCE

| #define CACHE\_IA\_INTR\_SOURCE   70 /\* Cache Invalid Access, level \*/ |
| --- |

## [◆ ](#a1334dc20d35277646113e699619d8856)CPU\_PERI\_ERROR\_INTR\_SOURCE

| #define CPU\_PERI\_ERROR\_INTR\_SOURCE   91 /\* CPU peripherals error, level \*/ |
| --- |

## [◆ ](#ad81b659cea69558a9accb6cd9315b236)CRYPTO\_DMA\_INTR\_SOURCE

| #define CRYPTO\_DMA\_INTR\_SOURCE   90 /\* encrypted DMA, level \*/ |
| --- |

## [◆ ](#adecb822591c0c4bf063d67b2e74e9a40)DCACHE\_PRELOAD\_INTR\_SOURCE

| #define DCACHE\_PRELOAD\_INTR\_SOURCE   88 /\* DCache preload operation, level \*/ |
| --- |

## [◆ ](#a93a4db93be7bef5cdc22cc2854da84b6)DCACHE\_SYNC\_INTR\_SOURCE

| #define DCACHE\_SYNC\_INTR\_SOURCE   93 /\* data cache sync done, level \*/ |
| --- |

## [◆ ](#a5b31ad0ece8c26e3e1600837bc1121bb)DEDICATED\_GPIO\_INTR\_SOURCE

| #define DEDICATED\_GPIO\_INTR\_SOURCE   27 /\* interrupt of dedicated GPIO, level \*/ |
| --- |

## [◆ ](#a03fc7ea80cff3be1cdf02d5f97434c71)DMA\_COPY\_INTR\_SOURCE

| #define DMA\_COPY\_INTR\_SOURCE   84 /\* DMA copy, level \*/ |
| --- |

## [◆ ](#aaf244ea4b63d912e0ce8d59795c79f9d)EFUSE\_INTR\_SOURCE

| #define EFUSE\_INTR\_SOURCE   46 /\* efuse, level, not likely to use \*/ |
| --- |

## [◆ ](#afc7bfcea2e621d81336ea6dd23310363)ESP\_INTR\_FLAG\_SHARED

| #define ESP\_INTR\_FLAG\_SHARED   (1<<8) /\* Interrupt can be shared between ISRs \*/ |
| --- |

## [◆ ](#a47c9d4be8d21b6f389993db5dbe2883d)FROM\_CPU\_INTR0\_SOURCE

| #define FROM\_CPU\_INTR0\_SOURCE   28 /\* int0 from a CPU, level \*/ |
| --- |

## [◆ ](#a2f704a24d6d56f2e13aed56e86e8fb55)FROM\_CPU\_INTR1\_SOURCE

| #define FROM\_CPU\_INTR1\_SOURCE   29 /\* int1 from a CPU, level \*/ |
| --- |

## [◆ ](#a470d4f804a7ddb5d107f1cafe8f19308)FROM\_CPU\_INTR2\_SOURCE

| #define FROM\_CPU\_INTR2\_SOURCE   30 /\* int2 from a CPU, level, for DPORT Access \*/ |
| --- |

## [◆ ](#a0b8897c96de3f23e794440ef2ef2f523)FROM\_CPU\_INTR3\_SOURCE

| #define FROM\_CPU\_INTR3\_SOURCE   31 /\* int3 from a CPU, level, for DPORT Access \*/ |
| --- |

## [◆ ](#a64020d7c1f6557ef6da375f12acf68de)GPIO\_INTR\_SOURCE

| #define GPIO\_INTR\_SOURCE   23 /\* interrupt of GPIO, level \*/ |
| --- |

## [◆ ](#afb98fcf1a9be6030f5ca87dea6675974)GPIO\_INTR\_SOURCE2

| #define GPIO\_INTR\_SOURCE2   25 /\* interrupt of GPIO, level \*/ |
| --- |

## [◆ ](#a23e7de652ab586c903ec999aa8e77e4e)GPIO\_NMI\_SOURCE

| #define GPIO\_NMI\_SOURCE   24 /\* interrupt of GPIO, NMI \*/ |
| --- |

## [◆ ](#ad11e04bc97a0115966929013f06efa50)GPIO\_NMI\_SOURCE2

| #define GPIO\_NMI\_SOURCE2   26 /\* interrupt of GPIO, NMI \*/ |
| --- |

## [◆ ](#a7a706aa628e14e55247d20c9853d76a9)I2C\_EXT0\_INTR\_SOURCE

| #define I2C\_EXT0\_INTR\_SOURCE   52 /\* I2C controller1, level \*/ |
| --- |

## [◆ ](#ac0e06a214b3990cb35fa4975e2a85e8e)I2C\_EXT1\_INTR\_SOURCE

| #define I2C\_EXT1\_INTR\_SOURCE   53 /\* I2C controller0, level \*/ |
| --- |

## [◆ ](#a6d41fd98988304b2ab82785c24140f8d)I2S0\_INTR\_SOURCE

| #define I2S0\_INTR\_SOURCE   35 /\* I2S0, level \*/ |
| --- |

## [◆ ](#a3b0877aad4fc7995be0cfb71fabb13a6)I2S1\_INTR\_SOURCE

| #define I2S1\_INTR\_SOURCE   36 /\* I2S1, level \*/ |
| --- |

## [◆ ](#a344601acd9e077b22b5f2d2627d9032e)ICACHE\_PRELOAD\_INTR\_SOURCE

| #define ICACHE\_PRELOAD\_INTR\_SOURCE   87 /\* ICache preload operation, level \*/ |
| --- |

## [◆ ](#a8299c36b90f9e08bc421e527f69545bb)ICACHE\_SYNC\_INTR\_SOURCE

| #define ICACHE\_SYNC\_INTR\_SOURCE   94 /\* instruction cache sync done, level \*/ |
| --- |

## [◆ ](#a2dbeaa0c017cdff0982b381cc96f0a6c)IRQ\_DEFAULT\_PRIORITY

| #define IRQ\_DEFAULT\_PRIORITY   0 |
| --- |

## [◆ ](#a296f3d252d30615dbaea32d61cba9214)LEDC\_INTR\_SOURCE

| #define LEDC\_INTR\_SOURCE   45 /\* LED PWM, level \*/ |
| --- |

## [◆ ](#ad57b1f253283c9a65fd95631a11d9532)MAX\_INTR\_SOURCE

| #define MAX\_INTR\_SOURCE   95 /\* total number of interrupt sources \*/ |
| --- |

## [◆ ](#acfdc02f0268c6145e3ffd5221ce7152f)PCNT\_INTR\_SOURCE

| #define PCNT\_INTR\_SOURCE   51 /\* pulse count, level \*/ |
| --- |

## [◆ ](#a9c4f6388dd7312fdc4219cff984166a9)PMS\_DMA\_APB\_I\_ILG\_INTR\_SOURCE

| #define PMS\_DMA\_APB\_I\_ILG\_INTR\_SOURCE   80 /\* illegal APB access, level \*/ |
| --- |

## [◆ ](#a8d6a4e0e0994f8a55fd7ca4ce5a45399)PMS\_DMA\_RX\_I\_ILG\_INTR\_SOURCE

| #define PMS\_DMA\_RX\_I\_ILG\_INTR\_SOURCE   81 /\* illegal DMA RX access, level \*/ |
| --- |

## [◆ ](#aac17e93da6a160da2d85a43d4ddc8289)PMS\_DMA\_TX\_I\_ILG\_INTR\_SOURCE

| #define PMS\_DMA\_TX\_I\_ILG\_INTR\_SOURCE   82 /\* illegal DMA TX access, level \*/ |
| --- |

## [◆ ](#ab4e4c60433d57d03b386d5bd9ab71370)PMS\_PRO\_AHB\_ILG\_INTR\_SOURCE

| #define PMS\_PRO\_AHB\_ILG\_INTR\_SOURCE   78 /\* illegal AHB access, level \*/ |
| --- |

## [◆ ](#ab2491671f5770a21823adc01763af792)PMS\_PRO\_CACHE\_ILG\_INTR\_SOURCE

| #define PMS\_PRO\_CACHE\_ILG\_INTR\_SOURCE   79 /\* illegal CACHE access, level \*/ |
| --- |

## [◆ ](#acf9bfdff3964eeacafede5571615bdd6)PMS\_PRO\_DPORT\_ILG\_INTR\_SOURCE

| #define PMS\_PRO\_DPORT\_ILG\_INTR\_SOURCE   77 /\* illegal DPORT access, level \*/ |
| --- |

## [◆ ](#a7ab3b2f26d6ce8bc8f9ea83ff4c3a900)PMS\_PRO\_DRAM0\_ILG\_INTR\_SOURCE

| #define PMS\_PRO\_DRAM0\_ILG\_INTR\_SOURCE   76 /\* illegal DRAM0 access, level \*/ |
| --- |

## [◆ ](#aa7415869e67d460c0ed4c7e96810291a)PMS\_PRO\_IRAM0\_ILG\_INTR\_SOURCE

| #define PMS\_PRO\_IRAM0\_ILG\_INTR\_SOURCE   75 /\* illegal IRAM1 access, level \*/ |
| --- |

## [◆ ](#a29ff03b184368e0a9ad6caf0cc9288ca)PWM0\_INTR\_SOURCE

| #define PWM0\_INTR\_SOURCE   41 /\* PWM0, level, Reserved \*/ |
| --- |

## [◆ ](#ab9a0099e8acba4831c68af88a073e31d)PWM1\_INTR\_SOURCE

| #define PWM1\_INTR\_SOURCE   42 /\* PWM1, level, Reserved \*/ |
| --- |

## [◆ ](#a04211cd6f7671713ae845e451c5b008d)PWM2\_INTR\_SOURCE

| #define PWM2\_INTR\_SOURCE   43 /\* PWM2, level \*/ |
| --- |

## [◆ ](#a95fc4f3d268322f0c0951f188f7eff11)PWM3\_INTR\_SOURCE

| #define PWM3\_INTR\_SOURCE   44 /\* PWM3, level \*/ |
| --- |

## [◆ ](#ac6d02a2b0f009553a9e52e7842fa959d)RMT\_INTR\_SOURCE

| #define RMT\_INTR\_SOURCE   50 /\* remote controller, level \*/ |
| --- |

## [◆ ](#accd4889d9e375ba16ea00489e7115c30)RSA\_INTR\_SOURCE

| #define RSA\_INTR\_SOURCE   54 /\* RSA accelerator, level \*/ |
| --- |

## [◆ ](#a80d2efc475574efe9250d0048a8a8c12)RTC\_CORE\_INTR\_SOURCE

| #define RTC\_CORE\_INTR\_SOURCE   49 /\* rtc core, level, include rtc watchdog \*/ |
| --- |

## [◆ ](#a8cf7f44d512a2c0b215397ae4c37a4f1)RWBLE\_INTR\_SOURCE

| #define RWBLE\_INTR\_SOURCE   8 /\* RWBLE, level \*/ |
| --- |

## [◆ ](#a3b9cef18112f398bd4ada544f3e2b5a0)RWBLE\_NMI\_SOURCE

| #define RWBLE\_NMI\_SOURCE   10 /\* RWBLE, NMI, use if RWBT has bug to fix in NMI \*/ |
| --- |

## [◆ ](#a14017a5bb9744f9c32138dbdcc09a786)RWBT\_INTR\_SOURCE

| #define RWBT\_INTR\_SOURCE   7 /\* RWBT, level \*/ |
| --- |

## [◆ ](#a445a79e81929641c372257f4018127f6)RWBT\_NMI\_SOURCE

| #define RWBT\_NMI\_SOURCE   9 /\* RWBT, NMI, use if RWBT has bug to fix in NMI \*/ |
| --- |

## [◆ ](#a26ce888bf67587b5ab6392f2ea0157c6)SDIO\_HOST\_INTR\_SOURCE

| #define SDIO\_HOST\_INTR\_SOURCE   40 /\* SD/SDIO/MMC HOST, level \*/ |
| --- |

## [◆ ](#a59f92ba6a2f4b3fa9454558f37ff3e24)SHA\_INTR\_SOURCE

| #define SHA\_INTR\_SOURCE   55 /\* interrupt of RSA accelerator, level \*/ |
| --- |

## [◆ ](#a24b7d137ebb32c58d60d5f84a3ce67db)SLC0\_INTR\_SOURCE

| #define SLC0\_INTR\_SOURCE   11 /\* SLC0, level \*/ |
| --- |

## [◆ ](#a8d8c7fb4a7206356ef7c7b41df4c1b7b)SLC1\_INTR\_SOURCE

| #define SLC1\_INTR\_SOURCE   12 /\* SLC1, level \*/ |
| --- |

## [◆ ](#a5779abc3d34c94cfad763d9ababebb9f)SPI1\_INTR\_SOURCE

| #define SPI1\_INTR\_SOURCE   32 /\* SPI1, level, flash [r](asm-macro-32-bit-gnu_8h.md#af16d2973cfd145a2ebdbf9528d5d9ae2)/w, do not use this \*/ |
| --- |

## [◆ ](#a7036cef97de80d47ffbdeff6478ccbec)SPI2\_DMA\_INTR\_SOURCE

| #define SPI2\_DMA\_INTR\_SOURCE   57 /\* SPI2 DMA, level \*/ |
| --- |

## [◆ ](#ac5d10660472f10fae0d0511f254b696d)SPI2\_INTR\_SOURCE

| #define SPI2\_INTR\_SOURCE   33 /\* SPI2, level \*/ |
| --- |

## [◆ ](#a1916307ca85215eb4c995bc4ae83eb50)SPI3\_DMA\_INTR\_SOURCE

| #define SPI3\_DMA\_INTR\_SOURCE   58 /\* interrupt of SPI3 DMA, level \*/ |
| --- |

## [◆ ](#a95996e58c94e25db8b2d97de7595996f)SPI3\_INTR\_SOURCE

| #define SPI3\_INTR\_SOURCE   34 /\* SPI3, level \*/ |
| --- |

## [◆ ](#a9f521721b77fef0f3c19bea05a12e850)SPI4\_DMA\_INTR\_SOURCE

| #define SPI4\_DMA\_INTR\_SOURCE   85 /\* SPI4 DMA, level \*/ |
| --- |

## [◆ ](#a334a2d6fa713f6df7c46c96465a2d6b9)SPI4\_INTR\_SOURCE

| #define SPI4\_INTR\_SOURCE   86 /\* SPI4, level \*/ |
| --- |

## [◆ ](#a36c488ff1605277f2772b1f80552f6ac)SPI\_MEM\_REJECT\_CACHE\_INTR\_SOURCE

| #define SPI\_MEM\_REJECT\_CACHE\_INTR\_SOURCE |
| --- |

**Value:**

83 /\* SPI0 Cache access and

\* SPI1 access rejected, level

\*/

## [◆ ](#a4cb07c15412c22b4939bb5a1e782f6e7)SYSTIMER\_TARGET0\_EDGE\_INTR\_SOURCE

| #define SYSTIMER\_TARGET0\_EDGE\_INTR\_SOURCE   71 /\* system timer 0, edge \*/ |
| --- |

## [◆ ](#a4ae5acb4be5a37cc87deb29ca61c8034)SYSTIMER\_TARGET1\_EDGE\_INTR\_SOURCE

| #define SYSTIMER\_TARGET1\_EDGE\_INTR\_SOURCE   72 /\* system timer 1, edge \*/ |
| --- |

## [◆ ](#a3c07aba15f9a2e9bc4a97031a241b512)SYSTIMER\_TARGET2\_EDGE\_INTR\_SOURCE

| #define SYSTIMER\_TARGET2\_EDGE\_INTR\_SOURCE   73 /\* system timer 2, edge \*/ |
| --- |

## [◆ ](#aaf809080c506a114fe3b47d4d4911873)TG0\_LACT\_EDGE\_INTR\_SOURCE

| #define TG0\_LACT\_EDGE\_INTR\_SOURCE   65 /\* TIMER\_GROUP0, LACT, EDGE \*/ |
| --- |

## [◆ ](#a8ab5e103356b484d48b68cbafa34d418)TG0\_LACT\_LEVEL\_INTR\_SOURCE

| #define TG0\_LACT\_LEVEL\_INTR\_SOURCE   18 /\* TIMER\_GROUP0, LACT, level \*/ |
| --- |

## [◆ ](#a3930148480a70cd784d84618fcc6ca4d)TG0\_T0\_EDGE\_INTR\_SOURCE

| #define TG0\_T0\_EDGE\_INTR\_SOURCE   62 /\* TIMER\_GROUP0, TIMER0, EDGE \*/ |
| --- |

## [◆ ](#a22bf10410f0b99b9fe398accf66c51b1)TG0\_T0\_LEVEL\_INTR\_SOURCE

| #define TG0\_T0\_LEVEL\_INTR\_SOURCE   15 /\* TIMER\_GROUP0, TIMER0, level \*/ |
| --- |

## [◆ ](#af32f59d8128f02c0b104adfd84a0e484)TG0\_T1\_EDGE\_INTR\_SOURCE

| #define TG0\_T1\_EDGE\_INTR\_SOURCE   63 /\* TIMER\_GROUP0, TIMER1, EDGE \*/ |
| --- |

## [◆ ](#a792cd371542eb8a60e4d381b168ae2b8)TG0\_T1\_LEVEL\_INTR\_SOURCE

| #define TG0\_T1\_LEVEL\_INTR\_SOURCE   16 /\* TIMER\_GROUP0, TIMER1, level \*/ |
| --- |

## [◆ ](#a6f69896f6b8b308d948856e624fc8da6)TG0\_WDT\_EDGE\_INTR\_SOURCE

| #define TG0\_WDT\_EDGE\_INTR\_SOURCE   64 /\* TIMER\_GROUP0, WATCH DOG, EDGE \*/ |
| --- |

## [◆ ](#afc23d5890e9c8029e7d417291193a559)TG0\_WDT\_LEVEL\_INTR\_SOURCE

| #define TG0\_WDT\_LEVEL\_INTR\_SOURCE   17 /\* TIMER\_GROUP0, WATCHDOG, level \*/ |
| --- |

## [◆ ](#a4789654138f3c05bdf28370301971ade)TG1\_LACT\_EDGE\_INTR\_SOURCE

| #define TG1\_LACT\_EDGE\_INTR\_SOURCE   69 /\* TIMER\_GROUP0, LACT, EDGE \*/ |
| --- |

## [◆ ](#aa3aeef6dc970aa8c6f7aec839835a384)TG1\_LACT\_LEVEL\_INTR\_SOURCE

| #define TG1\_LACT\_LEVEL\_INTR\_SOURCE   22 /\* TIMER\_GROUP1, LACT, level \*/ |
| --- |

## [◆ ](#a0470cb4879bd92a67e5bd71522c79894)TG1\_T0\_EDGE\_INTR\_SOURCE

| #define TG1\_T0\_EDGE\_INTR\_SOURCE   66 /\* TIMER\_GROUP1, TIMER0, EDGE \*/ |
| --- |

## [◆ ](#aee34beaabe47713742eb7633bd8430e3)TG1\_T0\_LEVEL\_INTR\_SOURCE

| #define TG1\_T0\_LEVEL\_INTR\_SOURCE   19 /\* TIMER\_GROUP1, TIMER0, level \*/ |
| --- |

## [◆ ](#a7315915335a06cbd3302b26eb5056ea1)TG1\_T1\_EDGE\_INTR\_SOURCE

| #define TG1\_T1\_EDGE\_INTR\_SOURCE   67 /\* TIMER\_GROUP1, TIMER1, EDGE \*/ |
| --- |

## [◆ ](#a41b4592783755438167ac4444adcaade)TG1\_T1\_LEVEL\_INTR\_SOURCE

| #define TG1\_T1\_LEVEL\_INTR\_SOURCE   20 /\* TIMER\_GROUP1, TIMER1, level \*/ |
| --- |

## [◆ ](#a53372a881097f28f5c381879ad065796)TG1\_WDT\_EDGE\_INTR\_SOURCE

| #define TG1\_WDT\_EDGE\_INTR\_SOURCE   68 /\* TIMER\_GROUP1, WATCHDOG, EDGE \*/ |
| --- |

## [◆ ](#a68616a67d062b7e57dbe6dd59151b85c)TG1\_WDT\_LEVEL\_INTR\_SOURCE

| #define TG1\_WDT\_LEVEL\_INTR\_SOURCE   21 /\* TIMER\_GROUP1, WATCHDOG, level \*/ |
| --- |

## [◆ ](#a9f5fed8c34c9b971830ab3e083316271)TIMER1\_INTR\_SOURCE

| #define TIMER1\_INTR\_SOURCE   60 /\* will be cancelled \*/ |
| --- |

## [◆ ](#a792de801f5e8339f61a381172782ee06)TIMER2\_INTR\_SOURCE

| #define TIMER2\_INTR\_SOURCE   61 /\* will be cancelled \*/ |
| --- |

## [◆ ](#a3a56673ee10a809fb2e75065d84b6f8e)TWAI\_INTR\_SOURCE

| #define TWAI\_INTR\_SOURCE   47 /\* twai, level \*/ |
| --- |

## [◆ ](#af4569e6b552e35100134e167cf11c7da)UART0\_INTR\_SOURCE

| #define UART0\_INTR\_SOURCE   37 /\* UART0, level \*/ |
| --- |

## [◆ ](#ad6f7d29b71a32716058033727bd01dc2)UART1\_INTR\_SOURCE

| #define UART1\_INTR\_SOURCE   38 /\* UART1, level \*/ |
| --- |

## [◆ ](#a4a7728c85b344ae5f62684286519f647)UART2\_INTR\_SOURCE

| #define UART2\_INTR\_SOURCE   39 /\* UART2, level \*/ |
| --- |

## [◆ ](#aa714005c0707aaf1ba5b4a033bcb8f81)UHCI0\_INTR\_SOURCE

| #define UHCI0\_INTR\_SOURCE   13 /\* UHCI0, level \*/ |
| --- |

## [◆ ](#a0837c2b982c45380cd89c136d5e9fb2c)UHCI1\_INTR\_SOURCE

| #define UHCI1\_INTR\_SOURCE   14 /\* UHCI1, level \*/ |
| --- |

## [◆ ](#a7a020da508049560356d36ab9607bca9)USB\_INTR\_SOURCE

| #define USB\_INTR\_SOURCE   48 /\* interrupt of USB, level \*/ |
| --- |

## [◆ ](#a407bd79d5c36e715bcd21a64d8f77c04)WDT\_INTR\_SOURCE

| #define WDT\_INTR\_SOURCE   59 /\* will be cancelled \*/ |
| --- |

## [◆ ](#a5383f7fa77bc12a8301c54e0dfb66306)WIFI\_BB\_INTR\_SOURCE

| #define WIFI\_BB\_INTR\_SOURCE   3 /\* WiFi BB, level, we can do some calibration \*/ |
| --- |

## [◆ ](#ad000d08efc3e8a5fc56da537973a5cb8)WIFI\_MAC\_INTR\_SOURCE

| #define WIFI\_MAC\_INTR\_SOURCE   0 /\* WiFi MAC, level \*/ |
| --- |

## [◆ ](#abfc935ef2963ee54b6a1f1279b4887ff)WIFI\_MAC\_NMI\_SOURCE

| #define WIFI\_MAC\_NMI\_SOURCE   1 /\* WiFi MAC, NMI, use if MAC needs fix in NMI \*/ |
| --- |

## [◆ ](#af3cef5f23f39a396dec2a356f395ef69)WIFI\_PWR\_INTR\_SOURCE

| #define WIFI\_PWR\_INTR\_SOURCE   2 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [esp32s2-xtensa-intmux.h](esp32s2-xtensa-intmux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
