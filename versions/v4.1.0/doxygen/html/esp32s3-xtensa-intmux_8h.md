---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/esp32s3-xtensa-intmux_8h.html
original_path: doxygen/html/esp32s3-xtensa-intmux_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32s3-xtensa-intmux.h File Reference

[Go to the source code of this file.](esp32s3-xtensa-intmux_8h_source.md)

| Macros | |
| --- | --- |
| #define | [WIFI\_MAC\_INTR\_SOURCE](#ad000d08efc3e8a5fc56da537973a5cb8)   0 /\* interrupt of WiFi MAC, level\*/ |
| #define | [WIFI\_MAC\_NMI\_SOURCE](#abfc935ef2963ee54b6a1f1279b4887ff)   1 /\* interrupt of WiFi MAC, NMI \*/ |
| #define | [WIFI\_PWR\_INTR\_SOURCE](#af3cef5f23f39a396dec2a356f395ef69)   2 |
| #define | [WIFI\_BB\_INTR\_SOURCE](#a5383f7fa77bc12a8301c54e0dfb66306)   3 /\* interrupt of WiFi BB, level\*/ |
| #define | [BT\_MAC\_INTR\_SOURCE](#a0b48425e316b45db6f105daa6f2a0cff)   4 /\* will be cancelled\*/ |
| #define | [BT\_BB\_INTR\_SOURCE](#aca3a7357f242a4e91269736de6545470)   5 /\* interrupt of BT BB, level\*/ |
| #define | [BT\_BB\_NMI\_SOURCE](#ab404d2ab995f39616675330f6462dd19)   6 /\* interrupt of BT BB, NMI\*/ |
| #define | [RWBT\_INTR\_SOURCE](#a14017a5bb9744f9c32138dbdcc09a786)   7 /\* interrupt of RWBT, level\*/ |
| #define | [RWBLE\_INTR\_SOURCE](#a8cf7f44d512a2c0b215397ae4c37a4f1)   8 /\* interrupt of RWBLE, level\*/ |
| #define | [RWBT\_NMI\_SOURCE](#a445a79e81929641c372257f4018127f6)   9 /\* interrupt of RWBT, NMI\*/ |
| #define | [RWBLE\_NMI\_SOURCE](#a3b9cef18112f398bd4ada544f3e2b5a0)   10 /\* interrupt of RWBLE, NMI\*/ |
| #define | [I2C\_MASTER\_SOURCE](#a8b38a0acf3511d0de89607d7eac8f537)   11 /\* interrupt of I2C Master, level\*/ |
| #define | [SLC0\_INTR\_SOURCE](#a24b7d137ebb32c58d60d5f84a3ce67db)   12 /\* interrupt of SLC0, level\*/ |
| #define | [SLC1\_INTR\_SOURCE](#a8d8c7fb4a7206356ef7c7b41df4c1b7b)   13 /\* interrupt of SLC1, level\*/ |
| #define | [UHCI0\_INTR\_SOURCE](#aa714005c0707aaf1ba5b4a033bcb8f81)   14 /\* interrupt of UHCI0, level\*/ |
| #define | [UHCI1\_INTR\_SOURCE](#a0837c2b982c45380cd89c136d5e9fb2c)   15 /\* interrupt of UHCI1, level\*/ |
| #define | [GPIO\_INTR\_SOURCE](#a64020d7c1f6557ef6da375f12acf68de)   16 /\* interrupt of GPIO, level\*/ |
| #define | [GPIO\_NMI\_SOURCE](#a23e7de652ab586c903ec999aa8e77e4e)   17 /\* interrupt of GPIO, NMI\*/ |
| #define | [GPIO\_INTR\_SOURCE2](#afb98fcf1a9be6030f5ca87dea6675974)   18 /\* interrupt of GPIO, level\*/ |
| #define | [GPIO\_NMI\_SOURCE2](#ad11e04bc97a0115966929013f06efa50)   19 /\* interrupt of GPIO, NMI\*/ |
| #define | [SPI1\_INTR\_SOURCE](#a5779abc3d34c94cfad763d9ababebb9f)   20 /\* interrupt of SPI1, level\*/ |
| #define | [SPI2\_INTR\_SOURCE](#ac5d10660472f10fae0d0511f254b696d)   21 /\* interrupt of SPI2, level\*/ |
| #define | [SPI3\_INTR\_SOURCE](#a95996e58c94e25db8b2d97de7595996f)   22 /\* interrupt of SPI3, level\*/ |
| #define | [LCD\_CAM\_INTR\_SOURCE](#a9632b36ac8096d9a56940be81637ade7)   24 /\* interrupt of LCD camera, level\*/ |
| #define | [I2S0\_INTR\_SOURCE](#a6d41fd98988304b2ab82785c24140f8d)   25 /\* interrupt of I2S0, level\*/ |
| #define | [I2S1\_INTR\_SOURCE](#a3b0877aad4fc7995be0cfb71fabb13a6)   26 /\* interrupt of I2S1, level\*/ |
| #define | [UART0\_INTR\_SOURCE](#af4569e6b552e35100134e167cf11c7da)   27 /\* interrupt of UART0, level\*/ |
| #define | [UART1\_INTR\_SOURCE](#ad6f7d29b71a32716058033727bd01dc2)   28 /\* interrupt of UART1, level\*/ |
| #define | [UART2\_INTR\_SOURCE](#a4a7728c85b344ae5f62684286519f647)   29 /\* interrupt of UART2, level\*/ |
| #define | [SDIO\_HOST\_INTR\_SOURCE](#a26ce888bf67587b5ab6392f2ea0157c6)   30 /\* interrupt of SD/SDIO/MMC HOST, level\*/ |
| #define | [PWM0\_INTR\_SOURCE](#a29ff03b184368e0a9ad6caf0cc9288ca)   31 /\* interrupt of PWM0, level, Reserved\*/ |
| #define | [PWM1\_INTR\_SOURCE](#ab9a0099e8acba4831c68af88a073e31d)   32 /\* interrupt of PWM1, level, Reserved\*/ |
| #define | [LEDC\_INTR\_SOURCE](#a296f3d252d30615dbaea32d61cba9214)   35 /\* interrupt of LED PWM, level\*/ |
| #define | [EFUSE\_INTR\_SOURCE](#aaf244ea4b63d912e0ce8d59795c79f9d)   36 /\* interrupt of efuse, level, not likely to use\*/ |
| #define | [TWAI\_INTR\_SOURCE](#a3a56673ee10a809fb2e75065d84b6f8e)   37 /\* interrupt of can, level\*/ |
| #define | [USB\_INTR\_SOURCE](#a7a020da508049560356d36ab9607bca9)   38 /\* interrupt of USB, level\*/ |
| #define | [RTC\_CORE\_INTR\_SOURCE](#a80d2efc475574efe9250d0048a8a8c12)   39 /\* interrupt of rtc core and watchdog, level\*/ |
| #define | [RMT\_INTR\_SOURCE](#ac6d02a2b0f009553a9e52e7842fa959d)   40 /\* interrupt of remote controller, level\*/ |
| #define | [PCNT\_INTR\_SOURCE](#acfdc02f0268c6145e3ffd5221ce7152f)   41 /\* interrupt of pulse count, level\*/ |
| #define | [I2C\_EXT0\_INTR\_SOURCE](#a7a706aa628e14e55247d20c9853d76a9)   42 /\* interrupt of I2C controller1, level\*/ |
| #define | [I2C\_EXT1\_INTR\_SOURCE](#ac0e06a214b3990cb35fa4975e2a85e8e)   43 /\* interrupt of I2C controller0, level\*/ |
| #define | [SPI2\_DMA\_INTR\_SOURCE](#a7036cef97de80d47ffbdeff6478ccbec)   44 /\* interrupt of SPI2 DMA, level\*/ |
| #define | [SPI3\_DMA\_INTR\_SOURCE](#a1916307ca85215eb4c995bc4ae83eb50)   45 /\* interrupt of SPI3 DMA, level\*/ |
| #define | [WDT\_INTR\_SOURCE](#a407bd79d5c36e715bcd21a64d8f77c04)   47 /\* will be cancelled\*/ |
| #define | [TIMER1\_INTR\_SOURCE](#a9f5fed8c34c9b971830ab3e083316271)   48 |
| #define | [TIMER2\_INTR\_SOURCE](#a792de801f5e8339f61a381172782ee06)   49 |
| #define | [TG0\_T0\_LEVEL\_INTR\_SOURCE](#a22bf10410f0b99b9fe398accf66c51b1)   50 /\* interrupt of TIMER\_GROUP0, TIMER0, EDGE\*/ |
| #define | [TG0\_T1\_LEVEL\_INTR\_SOURCE](#a792cd371542eb8a60e4d381b168ae2b8)   51 /\* interrupt of TIMER\_GROUP0, TIMER1, EDGE\*/ |
| #define | [TG0\_WDT\_LEVEL\_INTR\_SOURCE](#afc23d5890e9c8029e7d417291193a559)   52 /\* interrupt of TIMER\_GROUP0, WATCH DOG, EDGE\*/ |
| #define | [TG1\_T0\_LEVEL\_INTR\_SOURCE](#aee34beaabe47713742eb7633bd8430e3)   53 /\* interrupt of TIMER\_GROUP1, TIMER0, EDGE\*/ |
| #define | [TG1\_T1\_LEVEL\_INTR\_SOURCE](#a41b4592783755438167ac4444adcaade)   54 /\* interrupt of TIMER\_GROUP1, TIMER1, EDGE\*/ |
| #define | [TG1\_WDT\_LEVEL\_INTR\_SOURCE](#a68616a67d062b7e57dbe6dd59151b85c)   55 /\* interrupt of TIMER\_GROUP1, WATCHDOG, EDGE\*/ |
| #define | [CACHE\_IA\_INTR\_SOURCE](#abc71e0e6d2e6ea7fc39d17297753e72e)   56 /\* interrupt of Cache Invalid Access, LEVEL\*/ |
| #define | [SYSTIMER\_TARGET0\_EDGE\_INTR\_SOURCE](#a4cb07c15412c22b4939bb5a1e782f6e7)   57 /\* interrupt of system timer 0, EDGE\*/ |
| #define | [SYSTIMER\_TARGET1\_EDGE\_INTR\_SOURCE](#a4ae5acb4be5a37cc87deb29ca61c8034)   58 /\* interrupt of system timer 1, EDGE\*/ |
| #define | [SYSTIMER\_TARGET2\_EDGE\_INTR\_SOURCE](#a3c07aba15f9a2e9bc4a97031a241b512)   59 /\* interrupt of system timer 2, EDGE\*/ |
| #define | [SPI\_MEM\_REJECT\_CACHE\_INTR\_SOURCE](#a36c488ff1605277f2772b1f80552f6ac)   60 /\* interrupt of SPI0/SPI1 Cache/Rejected, LEVEL\*/ |
| #define | [DCACHE\_PRELOAD0\_INTR\_SOURCE](#a0bbd6ed9f1c48b0556d8c0655e627cea)   61 /\* interrupt of DCache preload operation, LEVEL\*/ |
| #define | [ICACHE\_PRELOAD0\_INTR\_SOURCE](#a83a3ce01a7cc1f3d4095d260f96705d1)   62 /\* interrupt of ICache perload operation, LEVEL\*/ |
| #define | [DCACHE\_SYNC0\_INTR\_SOURCE](#a1e4d7c3f4b201ef8e58b1fa1714124ae)   63 /\* interrupt of data cache sync done, LEVEL\*/ |
| #define | [ICACHE\_SYNC0\_INTR\_SOURCE](#ae62a038d99a1fbd095213f05adfd8f0f)   64 /\* interrupt of instr. cache sync done, LEVEL\*/ |
| #define | [APB\_ADC\_INTR\_SOURCE](#a68b408eb63057838c64c51718c5b1f7f)   65 /\* interrupt of APB ADC, LEVEL\*/ |
| #define | [DMA\_IN\_CH0\_INTR\_SOURCE](#acef66209252c6f17bac98dc2da2595b6)   66 /\* interrupt of general DMA RX channel 0, LEVEL\*/ |
| #define | [DMA\_IN\_CH1\_INTR\_SOURCE](#a4ab6c4d84a4ccfadbdf1cbf74cd7abe2)   67 /\* interrupt of general DMA RX channel 1, LEVEL\*/ |
| #define | [DMA\_IN\_CH2\_INTR\_SOURCE](#a090f29def5fb84f8925407b8d4df2b16)   68 /\* interrupt of general DMA RX channel 2, LEVEL\*/ |
| #define | [DMA\_IN\_CH3\_INTR\_SOURCE](#abab724f60c1226a009f8bc81e624e1bc)   69 /\* interrupt of general DMA RX channel 3, LEVEL\*/ |
| #define | [DMA\_IN\_CH4\_INTR\_SOURCE](#aa139ac344775a2d505b1d03da7a8f91d)   70 /\* interrupt of general DMA RX channel 4, LEVEL\*/ |
| #define | [DMA\_OUT\_CH0\_INTR\_SOURCE](#aef145a19eb3530127030eefcd93c0cc6)   71 /\* interrupt of general DMA TX channel 0, LEVEL\*/ |
| #define | [DMA\_OUT\_CH1\_INTR\_SOURCE](#a7b0e98e5146a26ea18f71dde60a335fd)   72 /\* interrupt of general DMA TX channel 1, LEVEL\*/ |
| #define | [DMA\_OUT\_CH2\_INTR\_SOURCE](#acfc5282861029aaa04b137749ba20676)   73 /\* interrupt of general DMA TX channel 2, LEVEL\*/ |
| #define | [DMA\_OUT\_CH3\_INTR\_SOURCE](#a7a832824047aee2c1d830223dafc7108)   74 /\* interrupt of general DMA TX channel 3, LEVEL\*/ |
| #define | [DMA\_OUT\_CH4\_INTR\_SOURCE](#ae81c0d07a9856dfdbd74a82ee217f279)   75 /\* interrupt of general DMA TX channel 4, LEVEL\*/ |
| #define | [RSA\_INTR\_SOURCE](#accd4889d9e375ba16ea00489e7115c30)   76 /\* interrupt of RSA accelerator, level\*/ |
| #define | [AES\_INTR\_SOURCE](#ad793803f54262a4dcf6b14140e9dc22b)   77 /\* interrupt of AES accelerator, level\*/ |
| #define | [SHA\_INTR\_SOURCE](#a59f92ba6a2f4b3fa9454558f37ff3e24)   78 /\* interrupt of SHA accelerator, level\*/ |
| #define | [FROM\_CPU\_INTR0\_SOURCE](#a47c9d4be8d21b6f389993db5dbe2883d)   79 /\* interrupt0 generated from a CPU, level\*/ |
| #define | [FROM\_CPU\_INTR1\_SOURCE](#a2f704a24d6d56f2e13aed56e86e8fb55)   80 /\* interrupt1 generated from a CPU, level\*/ |
| #define | [FROM\_CPU\_INTR2\_SOURCE](#a470d4f804a7ddb5d107f1cafe8f19308)   81 /\* interrupt2 generated from a CPU, level\*/ |
| #define | [FROM\_CPU\_INTR3\_SOURCE](#a0b8897c96de3f23e794440ef2ef2f523)   82 /\* interrupt3 generated from a CPU, level\*/ |
| #define | [ASSIST\_DEBUG\_INTR\_SOURCE](#ab627766f8e6b851882c42596d7df540c)   83 /\* interrupt of Assist debug module, LEVEL\*/ |
| #define | [DMA\_APBPERI\_PMS\_INTR\_SOURCE](#ac1b4f216b241ccb1ee89543a110795ac)   84 |
| #define | [CORE0\_IRAM0\_PMS\_INTR\_SOURCE](#ac01e0a43892a021afe21998a4594bc9c)   85 |
| #define | [CORE0\_DRAM0\_PMS\_INTR\_SOURCE](#a1e105d1f6e499662772ce1b78a6ad027)   86 |
| #define | [CORE0\_PIF\_PMS\_INTR\_SOURCE](#a0562484da17734d4f3848fe28261ceca)   87 |
| #define | [CORE0\_PIF\_PMS\_SIZE\_INTR\_SOURCE](#a83166cdc662aeb9d1de9c9f0d3e2c330)   88 |
| #define | [CORE1\_IRAM0\_PMS\_INTR\_SOURCE](#adb42ba778970c402ab5cb916ec3324f0)   89 |
| #define | [CORE1\_DRAM0\_PMS\_INTR\_SOURCE](#ab1fb705fe2cd1b17e7365b9501be2e8d)   90 |
| #define | [CORE1\_PIF\_PMS\_INTR\_SOURCE](#a1a592159bbecb02de45259d3af06cf46)   91 |
| #define | [CORE1\_PIF\_PMS\_SIZE\_INTR\_SOURCE](#ab1ed75a1f02dd846a8418d69c1f657d8)   92 |
| #define | [BACKUP\_PMS\_VIOLATE\_INTR\_SOURCE](#a0f236ecbe185a7008b2c5bdc61413dce)   93 |
| #define | [CACHE\_CORE0\_ACS\_INTR\_SOURCE](#acea509fed0c77dfdb5e0f0ea7b5826af)   94 |
| #define | [CACHE\_CORE1\_ACS\_INTR\_SOURCE](#a253daf8607f6268ca84bfac2e9e5b796)   95 |
| #define | [USB\_SERIAL\_JTAG\_INTR\_SOURCE](#a481f3447ba9cb1b05df5c8972d593f54)   96 |
| #define | [PREI\_BACKUP\_INTR\_SOURCE](#a414affc383ce7ef21a67367e8cdcd278)   97 |
| #define | [DMA\_EXTMEM\_REJECT\_SOURCE](#a95d0cd3450c800d5555fe4df3bc9b92e)   98 |
| #define | [MAX\_INTR\_SOURCE](#ad57b1f253283c9a65fd95631a11d9532)   99 /\* number of interrupt sources \*/ |
| #define | [IRQ\_DEFAULT\_PRIORITY](#a2dbeaa0c017cdff0982b381cc96f0a6c)   0 |
| #define | [ESP\_INTR\_FLAG\_SHARED](#afc7bfcea2e621d81336ea6dd23310363)   (1<<8) /\* Interrupt can be shared between ISRs \*/ |

## Macro Definition Documentation

## [◆ ](#ad793803f54262a4dcf6b14140e9dc22b)AES\_INTR\_SOURCE

| #define AES\_INTR\_SOURCE   77 /\* interrupt of AES accelerator, level\*/ |
| --- |

## [◆ ](#a68b408eb63057838c64c51718c5b1f7f)APB\_ADC\_INTR\_SOURCE

| #define APB\_ADC\_INTR\_SOURCE   65 /\* interrupt of APB ADC, LEVEL\*/ |
| --- |

## [◆ ](#ab627766f8e6b851882c42596d7df540c)ASSIST\_DEBUG\_INTR\_SOURCE

| #define ASSIST\_DEBUG\_INTR\_SOURCE   83 /\* interrupt of Assist debug module, LEVEL\*/ |
| --- |

## [◆ ](#a0f236ecbe185a7008b2c5bdc61413dce)BACKUP\_PMS\_VIOLATE\_INTR\_SOURCE

| #define BACKUP\_PMS\_VIOLATE\_INTR\_SOURCE   93 |
| --- |

## [◆ ](#aca3a7357f242a4e91269736de6545470)BT\_BB\_INTR\_SOURCE

| #define BT\_BB\_INTR\_SOURCE   5 /\* interrupt of BT BB, level\*/ |
| --- |

## [◆ ](#ab404d2ab995f39616675330f6462dd19)BT\_BB\_NMI\_SOURCE

| #define BT\_BB\_NMI\_SOURCE   6 /\* interrupt of BT BB, NMI\*/ |
| --- |

## [◆ ](#a0b48425e316b45db6f105daa6f2a0cff)BT\_MAC\_INTR\_SOURCE

| #define BT\_MAC\_INTR\_SOURCE   4 /\* will be cancelled\*/ |
| --- |

## [◆ ](#acea509fed0c77dfdb5e0f0ea7b5826af)CACHE\_CORE0\_ACS\_INTR\_SOURCE

| #define CACHE\_CORE0\_ACS\_INTR\_SOURCE   94 |
| --- |

## [◆ ](#a253daf8607f6268ca84bfac2e9e5b796)CACHE\_CORE1\_ACS\_INTR\_SOURCE

| #define CACHE\_CORE1\_ACS\_INTR\_SOURCE   95 |
| --- |

## [◆ ](#abc71e0e6d2e6ea7fc39d17297753e72e)CACHE\_IA\_INTR\_SOURCE

| #define CACHE\_IA\_INTR\_SOURCE   56 /\* interrupt of Cache Invalid Access, LEVEL\*/ |
| --- |

## [◆ ](#a1e105d1f6e499662772ce1b78a6ad027)CORE0\_DRAM0\_PMS\_INTR\_SOURCE

| #define CORE0\_DRAM0\_PMS\_INTR\_SOURCE   86 |
| --- |

## [◆ ](#ac01e0a43892a021afe21998a4594bc9c)CORE0\_IRAM0\_PMS\_INTR\_SOURCE

| #define CORE0\_IRAM0\_PMS\_INTR\_SOURCE   85 |
| --- |

## [◆ ](#a0562484da17734d4f3848fe28261ceca)CORE0\_PIF\_PMS\_INTR\_SOURCE

| #define CORE0\_PIF\_PMS\_INTR\_SOURCE   87 |
| --- |

## [◆ ](#a83166cdc662aeb9d1de9c9f0d3e2c330)CORE0\_PIF\_PMS\_SIZE\_INTR\_SOURCE

| #define CORE0\_PIF\_PMS\_SIZE\_INTR\_SOURCE   88 |
| --- |

## [◆ ](#ab1fb705fe2cd1b17e7365b9501be2e8d)CORE1\_DRAM0\_PMS\_INTR\_SOURCE

| #define CORE1\_DRAM0\_PMS\_INTR\_SOURCE   90 |
| --- |

## [◆ ](#adb42ba778970c402ab5cb916ec3324f0)CORE1\_IRAM0\_PMS\_INTR\_SOURCE

| #define CORE1\_IRAM0\_PMS\_INTR\_SOURCE   89 |
| --- |

## [◆ ](#a1a592159bbecb02de45259d3af06cf46)CORE1\_PIF\_PMS\_INTR\_SOURCE

| #define CORE1\_PIF\_PMS\_INTR\_SOURCE   91 |
| --- |

## [◆ ](#ab1ed75a1f02dd846a8418d69c1f657d8)CORE1\_PIF\_PMS\_SIZE\_INTR\_SOURCE

| #define CORE1\_PIF\_PMS\_SIZE\_INTR\_SOURCE   92 |
| --- |

## [◆ ](#a0bbd6ed9f1c48b0556d8c0655e627cea)DCACHE\_PRELOAD0\_INTR\_SOURCE

| #define DCACHE\_PRELOAD0\_INTR\_SOURCE   61 /\* interrupt of DCache preload operation, LEVEL\*/ |
| --- |

## [◆ ](#a1e4d7c3f4b201ef8e58b1fa1714124ae)DCACHE\_SYNC0\_INTR\_SOURCE

| #define DCACHE\_SYNC0\_INTR\_SOURCE   63 /\* interrupt of data cache sync done, LEVEL\*/ |
| --- |

## [◆ ](#ac1b4f216b241ccb1ee89543a110795ac)DMA\_APBPERI\_PMS\_INTR\_SOURCE

| #define DMA\_APBPERI\_PMS\_INTR\_SOURCE   84 |
| --- |

## [◆ ](#a95d0cd3450c800d5555fe4df3bc9b92e)DMA\_EXTMEM\_REJECT\_SOURCE

| #define DMA\_EXTMEM\_REJECT\_SOURCE   98 |
| --- |

## [◆ ](#acef66209252c6f17bac98dc2da2595b6)DMA\_IN\_CH0\_INTR\_SOURCE

| #define DMA\_IN\_CH0\_INTR\_SOURCE   66 /\* interrupt of general DMA RX channel 0, LEVEL\*/ |
| --- |

## [◆ ](#a4ab6c4d84a4ccfadbdf1cbf74cd7abe2)DMA\_IN\_CH1\_INTR\_SOURCE

| #define DMA\_IN\_CH1\_INTR\_SOURCE   67 /\* interrupt of general DMA RX channel 1, LEVEL\*/ |
| --- |

## [◆ ](#a090f29def5fb84f8925407b8d4df2b16)DMA\_IN\_CH2\_INTR\_SOURCE

| #define DMA\_IN\_CH2\_INTR\_SOURCE   68 /\* interrupt of general DMA RX channel 2, LEVEL\*/ |
| --- |

## [◆ ](#abab724f60c1226a009f8bc81e624e1bc)DMA\_IN\_CH3\_INTR\_SOURCE

| #define DMA\_IN\_CH3\_INTR\_SOURCE   69 /\* interrupt of general DMA RX channel 3, LEVEL\*/ |
| --- |

## [◆ ](#aa139ac344775a2d505b1d03da7a8f91d)DMA\_IN\_CH4\_INTR\_SOURCE

| #define DMA\_IN\_CH4\_INTR\_SOURCE   70 /\* interrupt of general DMA RX channel 4, LEVEL\*/ |
| --- |

## [◆ ](#aef145a19eb3530127030eefcd93c0cc6)DMA\_OUT\_CH0\_INTR\_SOURCE

| #define DMA\_OUT\_CH0\_INTR\_SOURCE   71 /\* interrupt of general DMA TX channel 0, LEVEL\*/ |
| --- |

## [◆ ](#a7b0e98e5146a26ea18f71dde60a335fd)DMA\_OUT\_CH1\_INTR\_SOURCE

| #define DMA\_OUT\_CH1\_INTR\_SOURCE   72 /\* interrupt of general DMA TX channel 1, LEVEL\*/ |
| --- |

## [◆ ](#acfc5282861029aaa04b137749ba20676)DMA\_OUT\_CH2\_INTR\_SOURCE

| #define DMA\_OUT\_CH2\_INTR\_SOURCE   73 /\* interrupt of general DMA TX channel 2, LEVEL\*/ |
| --- |

## [◆ ](#a7a832824047aee2c1d830223dafc7108)DMA\_OUT\_CH3\_INTR\_SOURCE

| #define DMA\_OUT\_CH3\_INTR\_SOURCE   74 /\* interrupt of general DMA TX channel 3, LEVEL\*/ |
| --- |

## [◆ ](#ae81c0d07a9856dfdbd74a82ee217f279)DMA\_OUT\_CH4\_INTR\_SOURCE

| #define DMA\_OUT\_CH4\_INTR\_SOURCE   75 /\* interrupt of general DMA TX channel 4, LEVEL\*/ |
| --- |

## [◆ ](#aaf244ea4b63d912e0ce8d59795c79f9d)EFUSE\_INTR\_SOURCE

| #define EFUSE\_INTR\_SOURCE   36 /\* interrupt of efuse, level, not likely to use\*/ |
| --- |

## [◆ ](#afc7bfcea2e621d81336ea6dd23310363)ESP\_INTR\_FLAG\_SHARED

| #define ESP\_INTR\_FLAG\_SHARED   (1<<8) /\* Interrupt can be shared between ISRs \*/ |
| --- |

## [◆ ](#a47c9d4be8d21b6f389993db5dbe2883d)FROM\_CPU\_INTR0\_SOURCE

| #define FROM\_CPU\_INTR0\_SOURCE   79 /\* interrupt0 generated from a CPU, level\*/ |
| --- |

## [◆ ](#a2f704a24d6d56f2e13aed56e86e8fb55)FROM\_CPU\_INTR1\_SOURCE

| #define FROM\_CPU\_INTR1\_SOURCE   80 /\* interrupt1 generated from a CPU, level\*/ |
| --- |

## [◆ ](#a470d4f804a7ddb5d107f1cafe8f19308)FROM\_CPU\_INTR2\_SOURCE

| #define FROM\_CPU\_INTR2\_SOURCE   81 /\* interrupt2 generated from a CPU, level\*/ |
| --- |

## [◆ ](#a0b8897c96de3f23e794440ef2ef2f523)FROM\_CPU\_INTR3\_SOURCE

| #define FROM\_CPU\_INTR3\_SOURCE   82 /\* interrupt3 generated from a CPU, level\*/ |
| --- |

## [◆ ](#a64020d7c1f6557ef6da375f12acf68de)GPIO\_INTR\_SOURCE

| #define GPIO\_INTR\_SOURCE   16 /\* interrupt of GPIO, level\*/ |
| --- |

## [◆ ](#afb98fcf1a9be6030f5ca87dea6675974)GPIO\_INTR\_SOURCE2

| #define GPIO\_INTR\_SOURCE2   18 /\* interrupt of GPIO, level\*/ |
| --- |

## [◆ ](#a23e7de652ab586c903ec999aa8e77e4e)GPIO\_NMI\_SOURCE

| #define GPIO\_NMI\_SOURCE   17 /\* interrupt of GPIO, NMI\*/ |
| --- |

## [◆ ](#ad11e04bc97a0115966929013f06efa50)GPIO\_NMI\_SOURCE2

| #define GPIO\_NMI\_SOURCE2   19 /\* interrupt of GPIO, NMI\*/ |
| --- |

## [◆ ](#a7a706aa628e14e55247d20c9853d76a9)I2C\_EXT0\_INTR\_SOURCE

| #define I2C\_EXT0\_INTR\_SOURCE   42 /\* interrupt of I2C controller1, level\*/ |
| --- |

## [◆ ](#ac0e06a214b3990cb35fa4975e2a85e8e)I2C\_EXT1\_INTR\_SOURCE

| #define I2C\_EXT1\_INTR\_SOURCE   43 /\* interrupt of I2C controller0, level\*/ |
| --- |

## [◆ ](#a8b38a0acf3511d0de89607d7eac8f537)I2C\_MASTER\_SOURCE

| #define I2C\_MASTER\_SOURCE   11 /\* interrupt of I2C Master, level\*/ |
| --- |

## [◆ ](#a6d41fd98988304b2ab82785c24140f8d)I2S0\_INTR\_SOURCE

| #define I2S0\_INTR\_SOURCE   25 /\* interrupt of I2S0, level\*/ |
| --- |

## [◆ ](#a3b0877aad4fc7995be0cfb71fabb13a6)I2S1\_INTR\_SOURCE

| #define I2S1\_INTR\_SOURCE   26 /\* interrupt of I2S1, level\*/ |
| --- |

## [◆ ](#a83a3ce01a7cc1f3d4095d260f96705d1)ICACHE\_PRELOAD0\_INTR\_SOURCE

| #define ICACHE\_PRELOAD0\_INTR\_SOURCE   62 /\* interrupt of ICache perload operation, LEVEL\*/ |
| --- |

## [◆ ](#ae62a038d99a1fbd095213f05adfd8f0f)ICACHE\_SYNC0\_INTR\_SOURCE

| #define ICACHE\_SYNC0\_INTR\_SOURCE   64 /\* interrupt of instr. cache sync done, LEVEL\*/ |
| --- |

## [◆ ](#a2dbeaa0c017cdff0982b381cc96f0a6c)IRQ\_DEFAULT\_PRIORITY

| #define IRQ\_DEFAULT\_PRIORITY   0 |
| --- |

## [◆ ](#a9632b36ac8096d9a56940be81637ade7)LCD\_CAM\_INTR\_SOURCE

| #define LCD\_CAM\_INTR\_SOURCE   24 /\* interrupt of LCD camera, level\*/ |
| --- |

## [◆ ](#a296f3d252d30615dbaea32d61cba9214)LEDC\_INTR\_SOURCE

| #define LEDC\_INTR\_SOURCE   35 /\* interrupt of LED PWM, level\*/ |
| --- |

## [◆ ](#ad57b1f253283c9a65fd95631a11d9532)MAX\_INTR\_SOURCE

| #define MAX\_INTR\_SOURCE   99 /\* number of interrupt sources \*/ |
| --- |

## [◆ ](#acfdc02f0268c6145e3ffd5221ce7152f)PCNT\_INTR\_SOURCE

| #define PCNT\_INTR\_SOURCE   41 /\* interrupt of pulse count, level\*/ |
| --- |

## [◆ ](#a414affc383ce7ef21a67367e8cdcd278)PREI\_BACKUP\_INTR\_SOURCE

| #define PREI\_BACKUP\_INTR\_SOURCE   97 |
| --- |

## [◆ ](#a29ff03b184368e0a9ad6caf0cc9288ca)PWM0\_INTR\_SOURCE

| #define PWM0\_INTR\_SOURCE   31 /\* interrupt of PWM0, level, Reserved\*/ |
| --- |

## [◆ ](#ab9a0099e8acba4831c68af88a073e31d)PWM1\_INTR\_SOURCE

| #define PWM1\_INTR\_SOURCE   32 /\* interrupt of PWM1, level, Reserved\*/ |
| --- |

## [◆ ](#ac6d02a2b0f009553a9e52e7842fa959d)RMT\_INTR\_SOURCE

| #define RMT\_INTR\_SOURCE   40 /\* interrupt of remote controller, level\*/ |
| --- |

## [◆ ](#accd4889d9e375ba16ea00489e7115c30)RSA\_INTR\_SOURCE

| #define RSA\_INTR\_SOURCE   76 /\* interrupt of RSA accelerator, level\*/ |
| --- |

## [◆ ](#a80d2efc475574efe9250d0048a8a8c12)RTC\_CORE\_INTR\_SOURCE

| #define RTC\_CORE\_INTR\_SOURCE   39 /\* interrupt of rtc core and watchdog, level\*/ |
| --- |

## [◆ ](#a8cf7f44d512a2c0b215397ae4c37a4f1)RWBLE\_INTR\_SOURCE

| #define RWBLE\_INTR\_SOURCE   8 /\* interrupt of RWBLE, level\*/ |
| --- |

## [◆ ](#a3b9cef18112f398bd4ada544f3e2b5a0)RWBLE\_NMI\_SOURCE

| #define RWBLE\_NMI\_SOURCE   10 /\* interrupt of RWBLE, NMI\*/ |
| --- |

## [◆ ](#a14017a5bb9744f9c32138dbdcc09a786)RWBT\_INTR\_SOURCE

| #define RWBT\_INTR\_SOURCE   7 /\* interrupt of RWBT, level\*/ |
| --- |

## [◆ ](#a445a79e81929641c372257f4018127f6)RWBT\_NMI\_SOURCE

| #define RWBT\_NMI\_SOURCE   9 /\* interrupt of RWBT, NMI\*/ |
| --- |

## [◆ ](#a26ce888bf67587b5ab6392f2ea0157c6)SDIO\_HOST\_INTR\_SOURCE

| #define SDIO\_HOST\_INTR\_SOURCE   30 /\* interrupt of SD/SDIO/MMC HOST, level\*/ |
| --- |

## [◆ ](#a59f92ba6a2f4b3fa9454558f37ff3e24)SHA\_INTR\_SOURCE

| #define SHA\_INTR\_SOURCE   78 /\* interrupt of SHA accelerator, level\*/ |
| --- |

## [◆ ](#a24b7d137ebb32c58d60d5f84a3ce67db)SLC0\_INTR\_SOURCE

| #define SLC0\_INTR\_SOURCE   12 /\* interrupt of SLC0, level\*/ |
| --- |

## [◆ ](#a8d8c7fb4a7206356ef7c7b41df4c1b7b)SLC1\_INTR\_SOURCE

| #define SLC1\_INTR\_SOURCE   13 /\* interrupt of SLC1, level\*/ |
| --- |

## [◆ ](#a5779abc3d34c94cfad763d9ababebb9f)SPI1\_INTR\_SOURCE

| #define SPI1\_INTR\_SOURCE   20 /\* interrupt of SPI1, level\*/ |
| --- |

## [◆ ](#a7036cef97de80d47ffbdeff6478ccbec)SPI2\_DMA\_INTR\_SOURCE

| #define SPI2\_DMA\_INTR\_SOURCE   44 /\* interrupt of SPI2 DMA, level\*/ |
| --- |

## [◆ ](#ac5d10660472f10fae0d0511f254b696d)SPI2\_INTR\_SOURCE

| #define SPI2\_INTR\_SOURCE   21 /\* interrupt of SPI2, level\*/ |
| --- |

## [◆ ](#a1916307ca85215eb4c995bc4ae83eb50)SPI3\_DMA\_INTR\_SOURCE

| #define SPI3\_DMA\_INTR\_SOURCE   45 /\* interrupt of SPI3 DMA, level\*/ |
| --- |

## [◆ ](#a95996e58c94e25db8b2d97de7595996f)SPI3\_INTR\_SOURCE

| #define SPI3\_INTR\_SOURCE   22 /\* interrupt of SPI3, level\*/ |
| --- |

## [◆ ](#a36c488ff1605277f2772b1f80552f6ac)SPI\_MEM\_REJECT\_CACHE\_INTR\_SOURCE

| #define SPI\_MEM\_REJECT\_CACHE\_INTR\_SOURCE   60 /\* interrupt of SPI0/SPI1 Cache/Rejected, LEVEL\*/ |
| --- |

## [◆ ](#a4cb07c15412c22b4939bb5a1e782f6e7)SYSTIMER\_TARGET0\_EDGE\_INTR\_SOURCE

| #define SYSTIMER\_TARGET0\_EDGE\_INTR\_SOURCE   57 /\* interrupt of system timer 0, EDGE\*/ |
| --- |

## [◆ ](#a4ae5acb4be5a37cc87deb29ca61c8034)SYSTIMER\_TARGET1\_EDGE\_INTR\_SOURCE

| #define SYSTIMER\_TARGET1\_EDGE\_INTR\_SOURCE   58 /\* interrupt of system timer 1, EDGE\*/ |
| --- |

## [◆ ](#a3c07aba15f9a2e9bc4a97031a241b512)SYSTIMER\_TARGET2\_EDGE\_INTR\_SOURCE

| #define SYSTIMER\_TARGET2\_EDGE\_INTR\_SOURCE   59 /\* interrupt of system timer 2, EDGE\*/ |
| --- |

## [◆ ](#a22bf10410f0b99b9fe398accf66c51b1)TG0\_T0\_LEVEL\_INTR\_SOURCE

| #define TG0\_T0\_LEVEL\_INTR\_SOURCE   50 /\* interrupt of TIMER\_GROUP0, TIMER0, EDGE\*/ |
| --- |

## [◆ ](#a792cd371542eb8a60e4d381b168ae2b8)TG0\_T1\_LEVEL\_INTR\_SOURCE

| #define TG0\_T1\_LEVEL\_INTR\_SOURCE   51 /\* interrupt of TIMER\_GROUP0, TIMER1, EDGE\*/ |
| --- |

## [◆ ](#afc23d5890e9c8029e7d417291193a559)TG0\_WDT\_LEVEL\_INTR\_SOURCE

| #define TG0\_WDT\_LEVEL\_INTR\_SOURCE   52 /\* interrupt of TIMER\_GROUP0, WATCH DOG, EDGE\*/ |
| --- |

## [◆ ](#aee34beaabe47713742eb7633bd8430e3)TG1\_T0\_LEVEL\_INTR\_SOURCE

| #define TG1\_T0\_LEVEL\_INTR\_SOURCE   53 /\* interrupt of TIMER\_GROUP1, TIMER0, EDGE\*/ |
| --- |

## [◆ ](#a41b4592783755438167ac4444adcaade)TG1\_T1\_LEVEL\_INTR\_SOURCE

| #define TG1\_T1\_LEVEL\_INTR\_SOURCE   54 /\* interrupt of TIMER\_GROUP1, TIMER1, EDGE\*/ |
| --- |

## [◆ ](#a68616a67d062b7e57dbe6dd59151b85c)TG1\_WDT\_LEVEL\_INTR\_SOURCE

| #define TG1\_WDT\_LEVEL\_INTR\_SOURCE   55 /\* interrupt of TIMER\_GROUP1, WATCHDOG, EDGE\*/ |
| --- |

## [◆ ](#a9f5fed8c34c9b971830ab3e083316271)TIMER1\_INTR\_SOURCE

| #define TIMER1\_INTR\_SOURCE   48 |
| --- |

## [◆ ](#a792de801f5e8339f61a381172782ee06)TIMER2\_INTR\_SOURCE

| #define TIMER2\_INTR\_SOURCE   49 |
| --- |

## [◆ ](#a3a56673ee10a809fb2e75065d84b6f8e)TWAI\_INTR\_SOURCE

| #define TWAI\_INTR\_SOURCE   37 /\* interrupt of can, level\*/ |
| --- |

## [◆ ](#af4569e6b552e35100134e167cf11c7da)UART0\_INTR\_SOURCE

| #define UART0\_INTR\_SOURCE   27 /\* interrupt of UART0, level\*/ |
| --- |

## [◆ ](#ad6f7d29b71a32716058033727bd01dc2)UART1\_INTR\_SOURCE

| #define UART1\_INTR\_SOURCE   28 /\* interrupt of UART1, level\*/ |
| --- |

## [◆ ](#a4a7728c85b344ae5f62684286519f647)UART2\_INTR\_SOURCE

| #define UART2\_INTR\_SOURCE   29 /\* interrupt of UART2, level\*/ |
| --- |

## [◆ ](#aa714005c0707aaf1ba5b4a033bcb8f81)UHCI0\_INTR\_SOURCE

| #define UHCI0\_INTR\_SOURCE   14 /\* interrupt of UHCI0, level\*/ |
| --- |

## [◆ ](#a0837c2b982c45380cd89c136d5e9fb2c)UHCI1\_INTR\_SOURCE

| #define UHCI1\_INTR\_SOURCE   15 /\* interrupt of UHCI1, level\*/ |
| --- |

## [◆ ](#a7a020da508049560356d36ab9607bca9)USB\_INTR\_SOURCE

| #define USB\_INTR\_SOURCE   38 /\* interrupt of USB, level\*/ |
| --- |

## [◆ ](#a481f3447ba9cb1b05df5c8972d593f54)USB\_SERIAL\_JTAG\_INTR\_SOURCE

| #define USB\_SERIAL\_JTAG\_INTR\_SOURCE   96 |
| --- |

## [◆ ](#a407bd79d5c36e715bcd21a64d8f77c04)WDT\_INTR\_SOURCE

| #define WDT\_INTR\_SOURCE   47 /\* will be cancelled\*/ |
| --- |

## [◆ ](#a5383f7fa77bc12a8301c54e0dfb66306)WIFI\_BB\_INTR\_SOURCE

| #define WIFI\_BB\_INTR\_SOURCE   3 /\* interrupt of WiFi BB, level\*/ |
| --- |

## [◆ ](#ad000d08efc3e8a5fc56da537973a5cb8)WIFI\_MAC\_INTR\_SOURCE

| #define WIFI\_MAC\_INTR\_SOURCE   0 /\* interrupt of WiFi MAC, level\*/ |
| --- |

## [◆ ](#abfc935ef2963ee54b6a1f1279b4887ff)WIFI\_MAC\_NMI\_SOURCE

| #define WIFI\_MAC\_NMI\_SOURCE   1 /\* interrupt of WiFi MAC, NMI \*/ |
| --- |

## [◆ ](#af3cef5f23f39a396dec2a356f395ef69)WIFI\_PWR\_INTR\_SOURCE

| #define WIFI\_PWR\_INTR\_SOURCE   2 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [esp32s3-xtensa-intmux.h](esp32s3-xtensa-intmux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
