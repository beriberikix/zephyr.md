---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/esp-esp32c6-intmux_8h.html
original_path: doxygen/html/esp-esp32c6-intmux_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp-esp32c6-intmux.h File Reference

[Go to the source code of this file.](esp-esp32c6-intmux_8h_source.md)

| Macros | |
| --- | --- |
| #define | [WIFI\_MAC\_INTR\_SOURCE](#ad000d08efc3e8a5fc56da537973a5cb8)   0 /\* interrupt of WiFi MAC, level\*/ |
| #define | [WIFI\_MAC\_NMI\_SOURCE](#abfc935ef2963ee54b6a1f1279b4887ff)   1 /\* interrupt of WiFi MAC, NMI\*/ |
| #define | [WIFI\_PWR\_INTR\_SOURCE](#af3cef5f23f39a396dec2a356f395ef69)   2 |
| #define | [WIFI\_BB\_INTR\_SOURCE](#a5383f7fa77bc12a8301c54e0dfb66306)   3 /\* interrupt of WiFi BB, level\*/ |
| #define | [BT\_MAC\_INTR\_SOURCE](#a0b48425e316b45db6f105daa6f2a0cff)   4 /\* will be cancelled\*/ |
| #define | [BT\_BB\_INTR\_SOURCE](#aca3a7357f242a4e91269736de6545470)   5 /\* interrupt of BT BB, level\*/ |
| #define | [BT\_BB\_NMI\_SOURCE](#ab404d2ab995f39616675330f6462dd19)   6 /\* interrupt of BT BB, NMI\*/ |
| #define | [LP\_TIMER\_INTR\_SOURCE](#ad03c6b1b20803d8b41a35f15bf7ddf4d)   7 |
| #define | [COEX\_INTR\_SOURCE](#a7dff8de43b99c2d24bc48f88a0afdae0)   8 |
| #define | [BLE\_TIMER\_INTR\_SOURCE](#adbc876ad874f671f39e35d196e8f7a6b)   9 |
| #define | [BLE\_SEC\_INTR\_SOURCE](#a111640b45d607cd611e7928f965537d4)   10 |
| #define | [I2C\_MASTER\_SOURCE](#a8b38a0acf3511d0de89607d7eac8f537)   11 /\* interrupt of I2C Master, level\*/ |
| #define | [ZB\_MAC\_SOURCE](#a3562ce23b1b55e367bc9165b68e6b937)   12 |
| #define | [PMU\_INTR\_SOURCE](#a1a3ba4507baef4ff4da50836708a90d5)   13 |
| #define | [EFUSE\_INTR\_SOURCE](#aaf244ea4b63d912e0ce8d59795c79f9d)   14 /\* interrupt of efuse, level, not likely to use\*/ |
| #define | [LP\_RTC\_TIMER\_INTR\_SOURCE](#ab8231886be224cfd7393b672377e8d65)   15 |
| #define | [LP\_UART\_INTR\_SOURCE](#a0a11e636f52c56d92deaf08b06b15d9d)   16 |
| #define | [LP\_I2C\_INTR\_SOURCE](#a5e3657824945848e65fafefa96033d8a)   17 |
| #define | [LP\_WDT\_INTR\_SOURCE](#a0575e1c89bfd864c0d2b54a0ec861037)   18 |
| #define | [LP\_PERI\_TIMEOUT\_INTR\_SOURCE](#a1b6615100454fa7836acd2d8d54a15ad)   19 |
| #define | [LP\_APM\_M0\_INTR\_SOURCE](#a0887b9c26ba83d8c04da11623484571c)   20 |
| #define | [LP\_APM\_M1\_INTR\_SOURCE](#ad68dafecd716c3b3b5af87048e70dc46)   21 |
| #define | [FROM\_CPU\_INTR0\_SOURCE](#a47c9d4be8d21b6f389993db5dbe2883d)   22 /\* interrupt0 generated from a CPU, level\*/ |
| #define | [FROM\_CPU\_INTR1\_SOURCE](#a2f704a24d6d56f2e13aed56e86e8fb55)   23 /\* interrupt1 generated from a CPU, level\*/ |
| #define | [FROM\_CPU\_INTR2\_SOURCE](#a470d4f804a7ddb5d107f1cafe8f19308)   24 /\* interrupt2 generated from a CPU, level\*/ |
| #define | [FROM\_CPU\_INTR3\_SOURCE](#a0b8897c96de3f23e794440ef2ef2f523)   25 /\* interrupt3 generated from a CPU, level\*/ |
| #define | [ASSIST\_DEBUG\_INTR\_SOURCE](#ab627766f8e6b851882c42596d7df540c)   26 /\* interrupt of Assist debug module, LEVEL\*/ |
| #define | [TRACE\_INTR\_SOURCE](#ad6312c1a757038238df60334c1777410)   27 |
| #define | [CACHE\_INTR\_SOURCE](#a102f4242826c646d8babb5b161a0c092)   28 |
| #define | [CPU\_PERI\_TIMEOUT\_INTR\_SOURCE](#a3a3b6cb7a8509d87c4565657b14e80c3)   29 |
| #define | [GPIO\_INTR\_SOURCE](#a64020d7c1f6557ef6da375f12acf68de)   30 /\* interrupt of GPIO, level\*/ |
| #define | [GPIO\_NMI\_SOURCE](#a23e7de652ab586c903ec999aa8e77e4e)   31 /\* interrupt of GPIO, NMI\*/ |
| #define | [PAU\_INTR\_SOURCE](#a9eb00cc7adbaba58008b1190cfe4d63b)   32 |
| #define | [HP\_PERI\_TIMEOUT\_INTR\_SOURCE](#a6c7756a44b101b5075aedac9baf733b9)   33 |
| #define | [MODEM\_PERI\_TIMEOUT\_INTR\_SOURCE](#a4a57355bb47da52cb90571f2efb405d8)   34 |
| #define | [HP\_APM\_M0\_INTR\_SOURCE](#aa38b79495b31783ef39d627c88ac158b)   35 |
| #define | [HP\_APM\_M1\_INTR\_SOURCE](#a0e5f1e66fb5502c426c42de7248f026f)   36 |
| #define | [HP\_APM\_M2\_INTR\_SOURCE](#a4ef1ca8c6b71640fdf5ca7c7eed845c5)   37 |
| #define | [HP\_APM\_M3\_INTR\_SOURCE](#a04a62fcb5b5ea0c0ab7029c5440a7a61)   38 |
| #define | [LP\_APM0\_INTR\_SOURCE](#a99a7a79ead0fe03a5cfbada6eee24a7a)   39 |
| #define | [MSPI\_INTR\_SOURCE](#a6c1065701cb5a46b1b686ab0ab67f279)   40 |
| #define | [I2S1\_INTR\_SOURCE](#a3b0877aad4fc7995be0cfb71fabb13a6)   41 /\* interrupt of I2S1, level\*/ |
| #define | [UHCI0\_INTR\_SOURCE](#aa714005c0707aaf1ba5b4a033bcb8f81)   42 /\* interrupt of UHCI0, level\*/ |
| #define | [UART0\_INTR\_SOURCE](#af4569e6b552e35100134e167cf11c7da)   43 /\* interrupt of UART0, level\*/ |
| #define | [UART1\_INTR\_SOURCE](#ad6f7d29b71a32716058033727bd01dc2)   44 /\* interrupt of UART1, level\*/ |
| #define | [LEDC\_INTR\_SOURCE](#a296f3d252d30615dbaea32d61cba9214)   45 /\* interrupt of LED PWM, level\*/ |
| #define | [TWAI0\_INTR\_SOURCE](#a55da996fa56498f1afbc1c33cf02b69f)   46 /\* interrupt of can0, level\*/ |
| #define | [TWAI1\_INTR\_SOURCE](#a18c1ae17b147afa71043a79c82f45c05)   47 /\* interrupt of can1, level\*/ |
| #define | [USB\_SERIAL\_JTAG\_INTR\_SOURCE](#a481f3447ba9cb1b05df5c8972d593f54)   48 /\* interrupt of USB, level\*/ |
| #define | [RMT\_INTR\_SOURCE](#ac6d02a2b0f009553a9e52e7842fa959d)   49 /\* interrupt of remote controller, level\*/ |
| #define | [I2C\_EXT0\_INTR\_SOURCE](#a7a706aa628e14e55247d20c9853d76a9)   50 /\* interrupt of I2C controller1, level\*/ |
| #define | [TG0\_T0\_LEVEL\_INTR\_SOURCE](#a22bf10410f0b99b9fe398accf66c51b1)   51 /\* interrupt of TIMER\_GROUP0, TIMER0, level\*/ |
| #define | [TG0\_T1\_LEVEL\_INTR\_SOURCE](#a792cd371542eb8a60e4d381b168ae2b8)   52 /\* interrupt of TIMER\_GROUP0, TIMER1, level\*/ |
| #define | [TG0\_WDT\_LEVEL\_INTR\_SOURCE](#afc23d5890e9c8029e7d417291193a559)   53 /\* interrupt of TIMER\_GROUP0, WATCH DOG, level\*/ |
| #define | [TG1\_T0\_LEVEL\_INTR\_SOURCE](#aee34beaabe47713742eb7633bd8430e3)   54 /\* interrupt of TIMER\_GROUP1, TIMER0, level\*/ |
| #define | [TG1\_T1\_LEVEL\_INTR\_SOURCE](#a41b4592783755438167ac4444adcaade)   55 /\* interrupt of TIMER\_GROUP1, TIMER1, level\*/ |
| #define | [TG1\_WDT\_LEVEL\_INTR\_SOURCE](#a68616a67d062b7e57dbe6dd59151b85c)   56 /\* interrupt of TIMER\_GROUP1, WATCHDOG, level\*/ |
| #define | [SYSTIMER\_TARGET0\_EDGE\_INTR\_SOURCE](#a4cb07c15412c22b4939bb5a1e782f6e7)   57 /\* interrupt of system timer 0, EDGE\*/ |
| #define | [SYSTIMER\_TARGET1\_EDGE\_INTR\_SOURCE](#a4ae5acb4be5a37cc87deb29ca61c8034)   58 /\* interrupt of system timer 1, EDGE\*/ |
| #define | [SYSTIMER\_TARGET2\_EDGE\_INTR\_SOURCE](#a3c07aba15f9a2e9bc4a97031a241b512)   59 /\* interrupt of system timer 2, EDGE\*/ |
| #define | [APB\_ADC\_INTR\_SOURCE](#a68b408eb63057838c64c51718c5b1f7f)   60 /\* interrupt of APB ADC, LEVEL\*/ |
| #define | [MCPWM0\_INTR\_SOURCE](#ac3db7d29241dd164d73565532e1505c5)   61 /\* interrupt of MCPWM0, LEVEL\*/ |
| #define | [PCNT\_INTR\_SOURCE](#acfdc02f0268c6145e3ffd5221ce7152f)   62 |
| #define | [PARL\_IO\_INTR\_SOURCE](#a52d986b2c7adde41251fd2085e3635c6)   63 |
| #define | [SLC0\_INTR\_SOURCE](#a24b7d137ebb32c58d60d5f84a3ce67db)   64 |
| #define | [SLC\_INTR\_SOURCE](#afab3ba0bfb48f7bc723065afc4894cbc)   65 |
| #define | [DMA\_IN\_CH0\_INTR\_SOURCE](#acef66209252c6f17bac98dc2da2595b6)   66 /\* interrupt of general DMA IN channel 0, LEVEL\*/ |
| #define | [DMA\_IN\_CH1\_INTR\_SOURCE](#a4ab6c4d84a4ccfadbdf1cbf74cd7abe2)   67 /\* interrupt of general DMA IN channel 1, LEVEL\*/ |
| #define | [DMA\_IN\_CH2\_INTR\_SOURCE](#a090f29def5fb84f8925407b8d4df2b16)   68 /\* interrupt of general DMA IN channel 2, LEVEL\*/ |
| #define | [DMA\_OUT\_CH0\_INTR\_SOURCE](#aef145a19eb3530127030eefcd93c0cc6)   69 /\* interrupt of general DMA OUT channel 0, LEVEL\*/ |
| #define | [DMA\_OUT\_CH1\_INTR\_SOURCE](#a7b0e98e5146a26ea18f71dde60a335fd)   70 /\* interrupt of general DMA OUT channel 1, LEVEL\*/ |
| #define | [DMA\_OUT\_CH2\_INTR\_SOURCE](#acfc5282861029aaa04b137749ba20676)   71 /\* interrupt of general DMA OUT channel 2, LEVEL\*/ |
| #define | [GSPI2\_INTR\_SOURCE](#ab9aa4535fd0bcff815bffa3fce8fe94b)   72 |
| #define | [AES\_INTR\_SOURCE](#ad793803f54262a4dcf6b14140e9dc22b)   73 /\* interrupt of AES accelerator, level\*/ |
| #define | [SHA\_INTR\_SOURCE](#a59f92ba6a2f4b3fa9454558f37ff3e24)   74 /\* interrupt of SHA accelerator, level\*/ |
| #define | [RSA\_INTR\_SOURCE](#accd4889d9e375ba16ea00489e7115c30)   75 /\* interrupt of RSA accelerator, level\*/ |
| #define | [ECC\_INTR\_SOURCE](#aa471b47ba3f4e7a17dac9702e250acf4)   76 /\* interrupt of ECC accelerator, level\*/ |
| #define | [MAX\_INTR\_SOURCE](#ad57b1f253283c9a65fd95631a11d9532)   77 |

## Macro Definition Documentation

## [◆ ](#ad793803f54262a4dcf6b14140e9dc22b)AES\_INTR\_SOURCE

| #define AES\_INTR\_SOURCE   73 /\* interrupt of AES accelerator, level\*/ |
| --- |

## [◆ ](#a68b408eb63057838c64c51718c5b1f7f)APB\_ADC\_INTR\_SOURCE

| #define APB\_ADC\_INTR\_SOURCE   60 /\* interrupt of APB ADC, LEVEL\*/ |
| --- |

## [◆ ](#ab627766f8e6b851882c42596d7df540c)ASSIST\_DEBUG\_INTR\_SOURCE

| #define ASSIST\_DEBUG\_INTR\_SOURCE   26 /\* interrupt of Assist debug module, LEVEL\*/ |
| --- |

## [◆ ](#a111640b45d607cd611e7928f965537d4)BLE\_SEC\_INTR\_SOURCE

| #define BLE\_SEC\_INTR\_SOURCE   10 |
| --- |

## [◆ ](#adbc876ad874f671f39e35d196e8f7a6b)BLE\_TIMER\_INTR\_SOURCE

| #define BLE\_TIMER\_INTR\_SOURCE   9 |
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

## [◆ ](#a102f4242826c646d8babb5b161a0c092)CACHE\_INTR\_SOURCE

| #define CACHE\_INTR\_SOURCE   28 |
| --- |

## [◆ ](#a7dff8de43b99c2d24bc48f88a0afdae0)COEX\_INTR\_SOURCE

| #define COEX\_INTR\_SOURCE   8 |
| --- |

## [◆ ](#a3a3b6cb7a8509d87c4565657b14e80c3)CPU\_PERI\_TIMEOUT\_INTR\_SOURCE

| #define CPU\_PERI\_TIMEOUT\_INTR\_SOURCE   29 |
| --- |

## [◆ ](#acef66209252c6f17bac98dc2da2595b6)DMA\_IN\_CH0\_INTR\_SOURCE

| #define DMA\_IN\_CH0\_INTR\_SOURCE   66 /\* interrupt of general DMA IN channel 0, LEVEL\*/ |
| --- |

## [◆ ](#a4ab6c4d84a4ccfadbdf1cbf74cd7abe2)DMA\_IN\_CH1\_INTR\_SOURCE

| #define DMA\_IN\_CH1\_INTR\_SOURCE   67 /\* interrupt of general DMA IN channel 1, LEVEL\*/ |
| --- |

## [◆ ](#a090f29def5fb84f8925407b8d4df2b16)DMA\_IN\_CH2\_INTR\_SOURCE

| #define DMA\_IN\_CH2\_INTR\_SOURCE   68 /\* interrupt of general DMA IN channel 2, LEVEL\*/ |
| --- |

## [◆ ](#aef145a19eb3530127030eefcd93c0cc6)DMA\_OUT\_CH0\_INTR\_SOURCE

| #define DMA\_OUT\_CH0\_INTR\_SOURCE   69 /\* interrupt of general DMA OUT channel 0, LEVEL\*/ |
| --- |

## [◆ ](#a7b0e98e5146a26ea18f71dde60a335fd)DMA\_OUT\_CH1\_INTR\_SOURCE

| #define DMA\_OUT\_CH1\_INTR\_SOURCE   70 /\* interrupt of general DMA OUT channel 1, LEVEL\*/ |
| --- |

## [◆ ](#acfc5282861029aaa04b137749ba20676)DMA\_OUT\_CH2\_INTR\_SOURCE

| #define DMA\_OUT\_CH2\_INTR\_SOURCE   71 /\* interrupt of general DMA OUT channel 2, LEVEL\*/ |
| --- |

## [◆ ](#aa471b47ba3f4e7a17dac9702e250acf4)ECC\_INTR\_SOURCE

| #define ECC\_INTR\_SOURCE   76 /\* interrupt of ECC accelerator, level\*/ |
| --- |

## [◆ ](#aaf244ea4b63d912e0ce8d59795c79f9d)EFUSE\_INTR\_SOURCE

| #define EFUSE\_INTR\_SOURCE   14 /\* interrupt of efuse, level, not likely to use\*/ |
| --- |

## [◆ ](#a47c9d4be8d21b6f389993db5dbe2883d)FROM\_CPU\_INTR0\_SOURCE

| #define FROM\_CPU\_INTR0\_SOURCE   22 /\* interrupt0 generated from a CPU, level\*/ |
| --- |

## [◆ ](#a2f704a24d6d56f2e13aed56e86e8fb55)FROM\_CPU\_INTR1\_SOURCE

| #define FROM\_CPU\_INTR1\_SOURCE   23 /\* interrupt1 generated from a CPU, level\*/ |
| --- |

## [◆ ](#a470d4f804a7ddb5d107f1cafe8f19308)FROM\_CPU\_INTR2\_SOURCE

| #define FROM\_CPU\_INTR2\_SOURCE   24 /\* interrupt2 generated from a CPU, level\*/ |
| --- |

## [◆ ](#a0b8897c96de3f23e794440ef2ef2f523)FROM\_CPU\_INTR3\_SOURCE

| #define FROM\_CPU\_INTR3\_SOURCE   25 /\* interrupt3 generated from a CPU, level\*/ |
| --- |

## [◆ ](#a64020d7c1f6557ef6da375f12acf68de)GPIO\_INTR\_SOURCE

| #define GPIO\_INTR\_SOURCE   30 /\* interrupt of GPIO, level\*/ |
| --- |

## [◆ ](#a23e7de652ab586c903ec999aa8e77e4e)GPIO\_NMI\_SOURCE

| #define GPIO\_NMI\_SOURCE   31 /\* interrupt of GPIO, NMI\*/ |
| --- |

## [◆ ](#ab9aa4535fd0bcff815bffa3fce8fe94b)GSPI2\_INTR\_SOURCE

| #define GSPI2\_INTR\_SOURCE   72 |
| --- |

## [◆ ](#aa38b79495b31783ef39d627c88ac158b)HP\_APM\_M0\_INTR\_SOURCE

| #define HP\_APM\_M0\_INTR\_SOURCE   35 |
| --- |

## [◆ ](#a0e5f1e66fb5502c426c42de7248f026f)HP\_APM\_M1\_INTR\_SOURCE

| #define HP\_APM\_M1\_INTR\_SOURCE   36 |
| --- |

## [◆ ](#a4ef1ca8c6b71640fdf5ca7c7eed845c5)HP\_APM\_M2\_INTR\_SOURCE

| #define HP\_APM\_M2\_INTR\_SOURCE   37 |
| --- |

## [◆ ](#a04a62fcb5b5ea0c0ab7029c5440a7a61)HP\_APM\_M3\_INTR\_SOURCE

| #define HP\_APM\_M3\_INTR\_SOURCE   38 |
| --- |

## [◆ ](#a6c7756a44b101b5075aedac9baf733b9)HP\_PERI\_TIMEOUT\_INTR\_SOURCE

| #define HP\_PERI\_TIMEOUT\_INTR\_SOURCE   33 |
| --- |

## [◆ ](#a7a706aa628e14e55247d20c9853d76a9)I2C\_EXT0\_INTR\_SOURCE

| #define I2C\_EXT0\_INTR\_SOURCE   50 /\* interrupt of I2C controller1, level\*/ |
| --- |

## [◆ ](#a8b38a0acf3511d0de89607d7eac8f537)I2C\_MASTER\_SOURCE

| #define I2C\_MASTER\_SOURCE   11 /\* interrupt of I2C Master, level\*/ |
| --- |

## [◆ ](#a3b0877aad4fc7995be0cfb71fabb13a6)I2S1\_INTR\_SOURCE

| #define I2S1\_INTR\_SOURCE   41 /\* interrupt of I2S1, level\*/ |
| --- |

## [◆ ](#a296f3d252d30615dbaea32d61cba9214)LEDC\_INTR\_SOURCE

| #define LEDC\_INTR\_SOURCE   45 /\* interrupt of LED PWM, level\*/ |
| --- |

## [◆ ](#a99a7a79ead0fe03a5cfbada6eee24a7a)LP\_APM0\_INTR\_SOURCE

| #define LP\_APM0\_INTR\_SOURCE   39 |
| --- |

## [◆ ](#a0887b9c26ba83d8c04da11623484571c)LP\_APM\_M0\_INTR\_SOURCE

| #define LP\_APM\_M0\_INTR\_SOURCE   20 |
| --- |

## [◆ ](#ad68dafecd716c3b3b5af87048e70dc46)LP\_APM\_M1\_INTR\_SOURCE

| #define LP\_APM\_M1\_INTR\_SOURCE   21 |
| --- |

## [◆ ](#a5e3657824945848e65fafefa96033d8a)LP\_I2C\_INTR\_SOURCE

| #define LP\_I2C\_INTR\_SOURCE   17 |
| --- |

## [◆ ](#a1b6615100454fa7836acd2d8d54a15ad)LP\_PERI\_TIMEOUT\_INTR\_SOURCE

| #define LP\_PERI\_TIMEOUT\_INTR\_SOURCE   19 |
| --- |

## [◆ ](#ab8231886be224cfd7393b672377e8d65)LP\_RTC\_TIMER\_INTR\_SOURCE

| #define LP\_RTC\_TIMER\_INTR\_SOURCE   15 |
| --- |

## [◆ ](#ad03c6b1b20803d8b41a35f15bf7ddf4d)LP\_TIMER\_INTR\_SOURCE

| #define LP\_TIMER\_INTR\_SOURCE   7 |
| --- |

## [◆ ](#a0a11e636f52c56d92deaf08b06b15d9d)LP\_UART\_INTR\_SOURCE

| #define LP\_UART\_INTR\_SOURCE   16 |
| --- |

## [◆ ](#a0575e1c89bfd864c0d2b54a0ec861037)LP\_WDT\_INTR\_SOURCE

| #define LP\_WDT\_INTR\_SOURCE   18 |
| --- |

## [◆ ](#ad57b1f253283c9a65fd95631a11d9532)MAX\_INTR\_SOURCE

| #define MAX\_INTR\_SOURCE   77 |
| --- |

## [◆ ](#ac3db7d29241dd164d73565532e1505c5)MCPWM0\_INTR\_SOURCE

| #define MCPWM0\_INTR\_SOURCE   61 /\* interrupt of MCPWM0, LEVEL\*/ |
| --- |

## [◆ ](#a4a57355bb47da52cb90571f2efb405d8)MODEM\_PERI\_TIMEOUT\_INTR\_SOURCE

| #define MODEM\_PERI\_TIMEOUT\_INTR\_SOURCE   34 |
| --- |

## [◆ ](#a6c1065701cb5a46b1b686ab0ab67f279)MSPI\_INTR\_SOURCE

| #define MSPI\_INTR\_SOURCE   40 |
| --- |

## [◆ ](#a52d986b2c7adde41251fd2085e3635c6)PARL\_IO\_INTR\_SOURCE

| #define PARL\_IO\_INTR\_SOURCE   63 |
| --- |

## [◆ ](#a9eb00cc7adbaba58008b1190cfe4d63b)PAU\_INTR\_SOURCE

| #define PAU\_INTR\_SOURCE   32 |
| --- |

## [◆ ](#acfdc02f0268c6145e3ffd5221ce7152f)PCNT\_INTR\_SOURCE

| #define PCNT\_INTR\_SOURCE   62 |
| --- |

## [◆ ](#a1a3ba4507baef4ff4da50836708a90d5)PMU\_INTR\_SOURCE

| #define PMU\_INTR\_SOURCE   13 |
| --- |

## [◆ ](#ac6d02a2b0f009553a9e52e7842fa959d)RMT\_INTR\_SOURCE

| #define RMT\_INTR\_SOURCE   49 /\* interrupt of remote controller, level\*/ |
| --- |

## [◆ ](#accd4889d9e375ba16ea00489e7115c30)RSA\_INTR\_SOURCE

| #define RSA\_INTR\_SOURCE   75 /\* interrupt of RSA accelerator, level\*/ |
| --- |

## [◆ ](#a59f92ba6a2f4b3fa9454558f37ff3e24)SHA\_INTR\_SOURCE

| #define SHA\_INTR\_SOURCE   74 /\* interrupt of SHA accelerator, level\*/ |
| --- |

## [◆ ](#a24b7d137ebb32c58d60d5f84a3ce67db)SLC0\_INTR\_SOURCE

| #define SLC0\_INTR\_SOURCE   64 |
| --- |

## [◆ ](#afab3ba0bfb48f7bc723065afc4894cbc)SLC\_INTR\_SOURCE

| #define SLC\_INTR\_SOURCE   65 |
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

| #define TG0\_T0\_LEVEL\_INTR\_SOURCE   51 /\* interrupt of TIMER\_GROUP0, TIMER0, level\*/ |
| --- |

## [◆ ](#a792cd371542eb8a60e4d381b168ae2b8)TG0\_T1\_LEVEL\_INTR\_SOURCE

| #define TG0\_T1\_LEVEL\_INTR\_SOURCE   52 /\* interrupt of TIMER\_GROUP0, TIMER1, level\*/ |
| --- |

## [◆ ](#afc23d5890e9c8029e7d417291193a559)TG0\_WDT\_LEVEL\_INTR\_SOURCE

| #define TG0\_WDT\_LEVEL\_INTR\_SOURCE   53 /\* interrupt of TIMER\_GROUP0, WATCH DOG, level\*/ |
| --- |

## [◆ ](#aee34beaabe47713742eb7633bd8430e3)TG1\_T0\_LEVEL\_INTR\_SOURCE

| #define TG1\_T0\_LEVEL\_INTR\_SOURCE   54 /\* interrupt of TIMER\_GROUP1, TIMER0, level\*/ |
| --- |

## [◆ ](#a41b4592783755438167ac4444adcaade)TG1\_T1\_LEVEL\_INTR\_SOURCE

| #define TG1\_T1\_LEVEL\_INTR\_SOURCE   55 /\* interrupt of TIMER\_GROUP1, TIMER1, level\*/ |
| --- |

## [◆ ](#a68616a67d062b7e57dbe6dd59151b85c)TG1\_WDT\_LEVEL\_INTR\_SOURCE

| #define TG1\_WDT\_LEVEL\_INTR\_SOURCE   56 /\* interrupt of TIMER\_GROUP1, WATCHDOG, level\*/ |
| --- |

## [◆ ](#ad6312c1a757038238df60334c1777410)TRACE\_INTR\_SOURCE

| #define TRACE\_INTR\_SOURCE   27 |
| --- |

## [◆ ](#a55da996fa56498f1afbc1c33cf02b69f)TWAI0\_INTR\_SOURCE

| #define TWAI0\_INTR\_SOURCE   46 /\* interrupt of can0, level\*/ |
| --- |

## [◆ ](#a18c1ae17b147afa71043a79c82f45c05)TWAI1\_INTR\_SOURCE

| #define TWAI1\_INTR\_SOURCE   47 /\* interrupt of can1, level\*/ |
| --- |

## [◆ ](#af4569e6b552e35100134e167cf11c7da)UART0\_INTR\_SOURCE

| #define UART0\_INTR\_SOURCE   43 /\* interrupt of UART0, level\*/ |
| --- |

## [◆ ](#ad6f7d29b71a32716058033727bd01dc2)UART1\_INTR\_SOURCE

| #define UART1\_INTR\_SOURCE   44 /\* interrupt of UART1, level\*/ |
| --- |

## [◆ ](#aa714005c0707aaf1ba5b4a033bcb8f81)UHCI0\_INTR\_SOURCE

| #define UHCI0\_INTR\_SOURCE   42 /\* interrupt of UHCI0, level\*/ |
| --- |

## [◆ ](#a481f3447ba9cb1b05df5c8972d593f54)USB\_SERIAL\_JTAG\_INTR\_SOURCE

| #define USB\_SERIAL\_JTAG\_INTR\_SOURCE   48 /\* interrupt of USB, level\*/ |
| --- |

## [◆ ](#a5383f7fa77bc12a8301c54e0dfb66306)WIFI\_BB\_INTR\_SOURCE

| #define WIFI\_BB\_INTR\_SOURCE   3 /\* interrupt of WiFi BB, level\*/ |
| --- |

## [◆ ](#ad000d08efc3e8a5fc56da537973a5cb8)WIFI\_MAC\_INTR\_SOURCE

| #define WIFI\_MAC\_INTR\_SOURCE   0 /\* interrupt of WiFi MAC, level\*/ |
| --- |

## [◆ ](#abfc935ef2963ee54b6a1f1279b4887ff)WIFI\_MAC\_NMI\_SOURCE

| #define WIFI\_MAC\_NMI\_SOURCE   1 /\* interrupt of WiFi MAC, NMI\*/ |
| --- |

## [◆ ](#af3cef5f23f39a396dec2a356f395ef69)WIFI\_PWR\_INTR\_SOURCE

| #define WIFI\_PWR\_INTR\_SOURCE   2 |
| --- |

## [◆ ](#a3562ce23b1b55e367bc9165b68e6b937)ZB\_MAC\_SOURCE

| #define ZB\_MAC\_SOURCE   12 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [interrupt-controller](dir_f11fd9ad294c5739f2cbe07a93c59a1b.md)
- [esp-esp32c6-intmux.h](esp-esp32c6-intmux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
