---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/xg24-pinctrl_8h.html
original_path: doxygen/html/xg24-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xg24-pinctrl.h File Reference

`#include <[dt-bindings/pinctrl/silabs-pinctrl-dbus.h](silabs-pinctrl-dbus_8h_source.md)>`

[Go to the source code of this file.](xg24-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(port, pin) |
| #define | [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(port, pin) |
| #define | [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(port, pin) |
| #define | [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(port, pin) |
| #define | [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(port, pin) |
| #define | [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(port, pin) |
| #define | [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(port, pin) |
| #define | [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(port, pin) |
| #define | [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(port, pin) |
| #define | [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(port, pin) |
| #define | [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(port, pin) |
| #define | [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(port, pin) |
| #define | [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(port, pin) |
| #define | [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(port, pin) |
| #define | [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(port, pin) |
| #define | [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(port, pin) |
| #define | [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(port, pin) |
| #define | [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(port, pin) |
| #define | [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(port, pin) |
| #define | [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(port, pin) |
| #define | [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(port, pin) |
| #define | [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(port, pin) |
| #define | [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(port, pin) |
| #define | [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(port, pin) |
| #define | [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(port, pin) |
| #define | [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(port, pin) |
| #define | [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(port, pin) |
| #define | [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(port, pin) |
| #define | [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(port, pin) |
| #define | [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(port, pin) |
| #define | [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(port, pin) |
| #define | [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(port, pin) |
| #define | [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(port, pin) |
| #define | [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(port, pin) |
| #define | [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(port, pin) |
| #define | [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(port, pin) |
| #define | [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(port, pin) |
| #define | [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(port, pin) |
| #define | [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(port, pin) |
| #define | [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(port, pin) |
| #define | [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(port, pin) |
| #define | [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(port, pin) |
| #define | [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(port, pin) |
| #define | [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(port, pin) |
| #define | [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(port, pin) |
| #define | [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(port, pin) |
| #define | [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(port, pin) |
| #define | [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(port, pin) |
| #define | [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(port, pin) |
| #define | [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(port, pin) |
| #define | [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(port, pin) |
| #define | [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(port, pin) |
| #define | [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(port, pin) |
| #define | [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(port, pin) |
| #define | [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(port, pin) |
| #define | [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(port, pin) |
| #define | [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(port, pin) |
| #define | [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(port, pin) |
| #define | [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(port, pin) |
| #define | [SILABS\_DBUS\_RAC\_LNAEN](#a3c1e00721fae8d8a77341fd56fbbc09c)(port, pin) |
| #define | [SILABS\_DBUS\_RAC\_PAEN](#ab1282918e0b9bbe140c852b951260348)(port, pin) |
| #define | [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(port, pin) |
| #define | [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(port, pin) |
| #define | [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(port, pin) |
| #define | [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(port, pin) |
| #define | [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(port, pin) |
| #define | [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(port, pin) |
| #define | [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(port, pin) |
| #define | [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(port, pin) |
| #define | [ACMP0\_ACMPOUT\_PA0](#aedfa1c8d8e52b69e24b4c5ae55906dc6)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x0) |
| #define | [ACMP0\_ACMPOUT\_PA1](#afc43fb1cb74d95db1aceffc3b55fe017)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x1) |
| #define | [ACMP0\_ACMPOUT\_PA2](#ad609c06187830519865e977ad663e8a9)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x2) |
| #define | [ACMP0\_ACMPOUT\_PA3](#ab46e5bad6ae8864f903d86d60c3b08b2)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x3) |
| #define | [ACMP0\_ACMPOUT\_PA4](#acb82f83c6665cac86a44ffb88689e1f8)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x4) |
| #define | [ACMP0\_ACMPOUT\_PA5](#ae3d76d092e7875eac30dbc243b3ded51)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x5) |
| #define | [ACMP0\_ACMPOUT\_PA6](#a83b7f7e01fea7985ff1b739474e57015)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x6) |
| #define | [ACMP0\_ACMPOUT\_PA7](#ae42719fd5ec147180ae465dd40175867)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x7) |
| #define | [ACMP0\_ACMPOUT\_PA8](#a2e14f2d26d737657b252e5c6764d28af)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x8) |
| #define | [ACMP0\_ACMPOUT\_PA9](#a3f8caec7c93f1f90e507259873143715)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x9) |
| #define | [ACMP0\_ACMPOUT\_PB0](#a36b9f71114e84ffb46fc8d52b7a87046)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x1, 0x0) |
| #define | [ACMP0\_ACMPOUT\_PB1](#ad7205c69934692bea6a1c31e9b374eef)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x1, 0x1) |
| #define | [ACMP0\_ACMPOUT\_PB2](#a17952d489dca95115341cf1052e9dc40)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x1, 0x2) |
| #define | [ACMP0\_ACMPOUT\_PB3](#a7455d069c13e82b9ef92b9cf82d4528a)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x1, 0x3) |
| #define | [ACMP0\_ACMPOUT\_PB4](#a9c5d85ede4da946e89f0a28bd78ce723)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x1, 0x4) |
| #define | [ACMP0\_ACMPOUT\_PB5](#a075c5cbd27027e4eab08230f9bf49d26)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x1, 0x5) |
| #define | [ACMP0\_ACMPOUT\_PC0](#a5b32e3f7e8bfdc37a87a1e5400897df8)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x0) |
| #define | [ACMP0\_ACMPOUT\_PC1](#a8c6a859a56f83fe76898e7e5d251d0b3)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x1) |
| #define | [ACMP0\_ACMPOUT\_PC2](#abc756f46419f529864d1f5373df967fa)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x2) |
| #define | [ACMP0\_ACMPOUT\_PC3](#acf2975d5be55d86f12c69c12dd257c02)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x3) |
| #define | [ACMP0\_ACMPOUT\_PC4](#a3e87af3956c8d9b54f210c3c9ce25fe2)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x4) |
| #define | [ACMP0\_ACMPOUT\_PC5](#a02cb0bfeb435f2d76adf0624c9acc380)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x5) |
| #define | [ACMP0\_ACMPOUT\_PC6](#a38b79026393006be7b6e6f57e90f194c)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x6) |
| #define | [ACMP0\_ACMPOUT\_PC7](#a8d166fe3ba9340f393a6f43167c70d1f)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x7) |
| #define | [ACMP0\_ACMPOUT\_PC8](#ac8934c49c62c45fb2679b7faea22b8cd)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x8) |
| #define | [ACMP0\_ACMPOUT\_PC9](#a4c4ed2c8940129833454a9dbb3a23f05)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x9) |
| #define | [ACMP0\_ACMPOUT\_PD0](#a196c859ab39c4e7fea903085f0091f38)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x3, 0x0) |
| #define | [ACMP0\_ACMPOUT\_PD1](#aabae5292f25eac5b7f235c1613a4abfe)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x3, 0x1) |
| #define | [ACMP0\_ACMPOUT\_PD2](#af0c00ac6edb9696207c0688dd902889c)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x3, 0x2) |
| #define | [ACMP0\_ACMPOUT\_PD3](#a22cc57aac83e922695ce9765daca5a22)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x3, 0x3) |
| #define | [ACMP0\_ACMPOUT\_PD4](#a046027b3929f25e781e6f294783bc1a0)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x3, 0x4) |
| #define | [ACMP0\_ACMPOUT\_PD5](#a4dbdab365c718b1f64adc02a23d5bf4a)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x3, 0x5) |
| #define | [ACMP1\_ACMPOUT\_PA0](#a04aca20b5e493a872ba32bbd78b47a5a)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x0) |
| #define | [ACMP1\_ACMPOUT\_PA1](#aaa76825f32591d5e0921624dc9c7a547)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x1) |
| #define | [ACMP1\_ACMPOUT\_PA2](#a7e6b677b9f6fdf424146fe7bd16b8ab6)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x2) |
| #define | [ACMP1\_ACMPOUT\_PA3](#a519bb19bf1c5adb7a4c236260e19cb93)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x3) |
| #define | [ACMP1\_ACMPOUT\_PA4](#ae5cd234e221d2b8308334d877bc27e05)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x4) |
| #define | [ACMP1\_ACMPOUT\_PA5](#ae03013868fb1238d33b1c584509d891e)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x5) |
| #define | [ACMP1\_ACMPOUT\_PA6](#a541b4fdb8b53c3d920a588376126a7f2)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x6) |
| #define | [ACMP1\_ACMPOUT\_PA7](#a9693060d6ad6e4dbae35d88c03bbb040)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x7) |
| #define | [ACMP1\_ACMPOUT\_PA8](#a83aa9f91e580282d4aabc94eadc6e432)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x8) |
| #define | [ACMP1\_ACMPOUT\_PA9](#aff7884ab918b0a75ec62bcd2c9b7a44e)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x9) |
| #define | [ACMP1\_ACMPOUT\_PB0](#a84f6c6945835113f9918687cb295093b)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x1, 0x0) |
| #define | [ACMP1\_ACMPOUT\_PB1](#ac7ddbcf4f3906bc2e71b21b0ebada790)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x1, 0x1) |
| #define | [ACMP1\_ACMPOUT\_PB2](#a1e450275c12cc32003c239bb81741130)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x1, 0x2) |
| #define | [ACMP1\_ACMPOUT\_PB3](#a67d1e01a6af363373919428beb5780c5)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x1, 0x3) |
| #define | [ACMP1\_ACMPOUT\_PB4](#af896153a63d5ac12600afd9899647efa)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x1, 0x4) |
| #define | [ACMP1\_ACMPOUT\_PB5](#a97f817f9966a9a08d8ab5cd3e7ba0ba9)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x1, 0x5) |
| #define | [ACMP1\_ACMPOUT\_PC0](#aa98b56734d6c562982b62d2fae788a64)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x0) |
| #define | [ACMP1\_ACMPOUT\_PC1](#a623a2fbee184e239f5c4c1899b80b146)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x1) |
| #define | [ACMP1\_ACMPOUT\_PC2](#a9c1ad020fb2a75438324fca26e791d19)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x2) |
| #define | [ACMP1\_ACMPOUT\_PC3](#acbfcff70ab4cc6aec772a8f5f6a5c559)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x3) |
| #define | [ACMP1\_ACMPOUT\_PC4](#aeeef7ef4dfcb0a12adacd9718f04f43b)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x4) |
| #define | [ACMP1\_ACMPOUT\_PC5](#a4b15ffe9e4ecd23d7242b062e5cbc082)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x5) |
| #define | [ACMP1\_ACMPOUT\_PC6](#ad4db37359084a42fea18f9c2521496c8)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x6) |
| #define | [ACMP1\_ACMPOUT\_PC7](#ad030633794a7f05c0cee0c06bb81d087)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x7) |
| #define | [ACMP1\_ACMPOUT\_PC8](#abde1f8f36169f539391976f6a589ab8f)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x8) |
| #define | [ACMP1\_ACMPOUT\_PC9](#a59cb718dc4a0eaf46715ce9bfae59fdb)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x9) |
| #define | [ACMP1\_ACMPOUT\_PD0](#a0ca6370f146e12eece2dc87e0e322f62)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x3, 0x0) |
| #define | [ACMP1\_ACMPOUT\_PD1](#ae49cd1f217b75138cca0f43b8770b1bc)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x3, 0x1) |
| #define | [ACMP1\_ACMPOUT\_PD2](#ad9a1898895b78944b14493df85e3ee21)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x3, 0x2) |
| #define | [ACMP1\_ACMPOUT\_PD3](#a02fa7898cc55e75ac1bd8634cf4bd859)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x3, 0x3) |
| #define | [ACMP1\_ACMPOUT\_PD4](#ab46a58b4ccb7b62fabb73110eb2b8e46)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x3, 0x4) |
| #define | [ACMP1\_ACMPOUT\_PD5](#aac3861fba05ede584b08637cc9214a62)   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x3, 0x5) |
| #define | [CMU\_CLKOUT0\_PC0](#a750738e1a4c7ed8bfb4d2f9151267da6)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x0) |
| #define | [CMU\_CLKOUT0\_PC1](#a31916418c44431216dea609cb5aef35a)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x1) |
| #define | [CMU\_CLKOUT0\_PC2](#a90c69d0d98a225b058598397e960c41d)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x2) |
| #define | [CMU\_CLKOUT0\_PC3](#a502a3e471c068d2ae94fc2255b3680dd)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x3) |
| #define | [CMU\_CLKOUT0\_PC4](#a0af75594d7d55c0bf77021f81b058ef6)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x4) |
| #define | [CMU\_CLKOUT0\_PC5](#a3bfddaaeba9558824977b108319c26b1)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x5) |
| #define | [CMU\_CLKOUT0\_PC6](#a7c63df02e41810547afb13b879dbf602)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x6) |
| #define | [CMU\_CLKOUT0\_PC7](#aa219ec0869e6e96ce5a84ed7dbba3d06)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x7) |
| #define | [CMU\_CLKOUT0\_PC8](#aab39df8a873b3e6c0900d5e791a3f867)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x8) |
| #define | [CMU\_CLKOUT0\_PC9](#ad3f15ec5c750f7ffc8ba8ab07167e802)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x9) |
| #define | [CMU\_CLKOUT0\_PD0](#a1afed05e5d9d89ad251e77f94f1e745d)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x3, 0x0) |
| #define | [CMU\_CLKOUT0\_PD1](#a4cc3f9b8c22e11a9ffd40149c990d09d)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x3, 0x1) |
| #define | [CMU\_CLKOUT0\_PD2](#a823b6e29d70a1313ed81cae432648f73)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x3, 0x2) |
| #define | [CMU\_CLKOUT0\_PD3](#a4223cab1734f1dadac546c956ae17f66)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x3, 0x3) |
| #define | [CMU\_CLKOUT0\_PD4](#a45bd684b5ac8c0899bfce5901e372aa3)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x3, 0x4) |
| #define | [CMU\_CLKOUT0\_PD5](#a788945f76f25d0bdb52a0386ac0bd8bb)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x3, 0x5) |
| #define | [CMU\_CLKOUT1\_PC0](#a7b57f126203047b4cb82d0eff5c1ba8f)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x0) |
| #define | [CMU\_CLKOUT1\_PC1](#a7742937a9e0afe5ae4859f9fe6373ca3)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x1) |
| #define | [CMU\_CLKOUT1\_PC2](#ae634d0e26da5dd095bf98854cd95e6c9)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x2) |
| #define | [CMU\_CLKOUT1\_PC3](#afecc3d613acceb752470037c6c253759)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x3) |
| #define | [CMU\_CLKOUT1\_PC4](#a2d21eabc4603c5cfd93cd0eed5708565)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x4) |
| #define | [CMU\_CLKOUT1\_PC5](#a8287c02ea2823803c7f3415597aeb0f8)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x5) |
| #define | [CMU\_CLKOUT1\_PC6](#aed9fe929699b234ddcd9c5d814d309fc)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x6) |
| #define | [CMU\_CLKOUT1\_PC7](#af72caa6a5612d497402a76ac0d5e2d12)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x7) |
| #define | [CMU\_CLKOUT1\_PC8](#a04edc510b099491995f03e3c6bd160f6)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x8) |
| #define | [CMU\_CLKOUT1\_PC9](#ac3693e451d931359dbc2c79ec323a4b6)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x9) |
| #define | [CMU\_CLKOUT1\_PD0](#a9041e78bd2f530d25db4d36d783e04ff)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x3, 0x0) |
| #define | [CMU\_CLKOUT1\_PD1](#a65ab333bdb97055f6e69f17a46cc76ca)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x3, 0x1) |
| #define | [CMU\_CLKOUT1\_PD2](#ad6f97e49e9ed6808c2631547fae12fd0)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x3, 0x2) |
| #define | [CMU\_CLKOUT1\_PD3](#afc01df4895e8d3e104bbff29227824a8)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x3, 0x3) |
| #define | [CMU\_CLKOUT1\_PD4](#afd198f9e83c2b18208b42bb5f196ddb5)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x3, 0x4) |
| #define | [CMU\_CLKOUT1\_PD5](#a9a691758e704ccc7312ea85e620c4796)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x3, 0x5) |
| #define | [CMU\_CLKOUT2\_PA0](#a515401133e23f38d0c7babc3b8cffb18)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x0) |
| #define | [CMU\_CLKOUT2\_PA1](#ae765fe590bab12a1671c57b20b69e354)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x1) |
| #define | [CMU\_CLKOUT2\_PA2](#a4183040a304b3d85d3b382d28176da03)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x2) |
| #define | [CMU\_CLKOUT2\_PA3](#a65e82802fc3e2e3eb089eaa3bb4b1207)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x3) |
| #define | [CMU\_CLKOUT2\_PA4](#a9345663284354ee2c4b5ebd6a4124234)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x4) |
| #define | [CMU\_CLKOUT2\_PA5](#ac1767819afb4418dfb8de4ec2114144f)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x5) |
| #define | [CMU\_CLKOUT2\_PA6](#a078e7abf21f63f21617ea47fd565fcc0)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x6) |
| #define | [CMU\_CLKOUT2\_PA7](#a0ad411783ff7e13b2965931269fc8c8b)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x7) |
| #define | [CMU\_CLKOUT2\_PA8](#a0ea1041e58653ac225cacb25cd747970)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x8) |
| #define | [CMU\_CLKOUT2\_PA9](#a36754f6ea866cf3f6f6df6366946948a)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x9) |
| #define | [CMU\_CLKOUT2\_PB0](#a7f82072ef8014d5497df30c927b0d6f9)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x1, 0x0) |
| #define | [CMU\_CLKOUT2\_PB1](#af815e3c4392ba1686e4f77dc0b6911f1)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x1, 0x1) |
| #define | [CMU\_CLKOUT2\_PB2](#a9613c5b45ba73bc69011086baafad84c)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x1, 0x2) |
| #define | [CMU\_CLKOUT2\_PB3](#ac8e00ea8020085f156d66e741d7fa185)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x1, 0x3) |
| #define | [CMU\_CLKOUT2\_PB4](#a003c45e0a49fdb695df7d930f16ff20b)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x1, 0x4) |
| #define | [CMU\_CLKOUT2\_PB5](#a1128af6c3950b3e6eedea125be964f22)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x1, 0x5) |
| #define | [CMU\_CLKIN0\_PC0](#a4aaa42a036d18c3f1acb7def83fb9f05)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x0) |
| #define | [CMU\_CLKIN0\_PC1](#ad099af25ca0f801ff85e3071a1cda472)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x1) |
| #define | [CMU\_CLKIN0\_PC2](#add3b048d2455419255aedcef16aed776)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x2) |
| #define | [CMU\_CLKIN0\_PC3](#a59c6d813c66884cb9db67d4e6c1cd8d4)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x3) |
| #define | [CMU\_CLKIN0\_PC4](#a4528f4ea777e78b8f27bd604bfeaf59e)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x4) |
| #define | [CMU\_CLKIN0\_PC5](#a5f79eddd69ce5550c1fd8ee07ce0ad9c)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x5) |
| #define | [CMU\_CLKIN0\_PC6](#ab3ac5c61d6e2ba07c8d17e313ff61631)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x6) |
| #define | [CMU\_CLKIN0\_PC7](#a50bb44be738315ef4409c4310d93f7aa)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x7) |
| #define | [CMU\_CLKIN0\_PC8](#aa6fd2707f5f441a5f3b02425b400a155)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x8) |
| #define | [CMU\_CLKIN0\_PC9](#a577cbe545692020844b1756af5dd0bc7)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x9) |
| #define | [CMU\_CLKIN0\_PD0](#a8d96e9e617c1f18f2bd0a2ac65e98ae1)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x3, 0x0) |
| #define | [CMU\_CLKIN0\_PD1](#aa780fb9850bc6efcb36d8dd19770ec27)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x3, 0x1) |
| #define | [CMU\_CLKIN0\_PD2](#ad27e93b39cdcd25b3d3ba89f01a05019)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x3, 0x2) |
| #define | [CMU\_CLKIN0\_PD3](#aec9648fbe6bece6f7cec5b3942eda3a0)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x3, 0x3) |
| #define | [CMU\_CLKIN0\_PD4](#a9791109179057e8535cccfb2292ea5cd)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x3, 0x4) |
| #define | [CMU\_CLKIN0\_PD5](#ae2fddef4c421ea232fdb57927c928723)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x3, 0x5) |
| #define | [EUSART0\_CS\_PA0](#a100647c82cfce4ed946cb9f18472af15)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x0) |
| #define | [EUSART0\_CS\_PA1](#aad3c475c7949c55fc7ac69dcb9e9dfe3)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x1) |
| #define | [EUSART0\_CS\_PA2](#a521ddcc2db980c3e31ddcb847980ca73)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x2) |
| #define | [EUSART0\_CS\_PA3](#aff497e4a1f5d0f650a1a75d995740e5f)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x3) |
| #define | [EUSART0\_CS\_PA4](#a852775bf4cc8faa4191b618c12690c07)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x4) |
| #define | [EUSART0\_CS\_PA5](#a494590522337ea1dc294d8e30bdce4a0)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x5) |
| #define | [EUSART0\_CS\_PA6](#a3324f29622d78fbdf0d6a3b7931fee92)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x6) |
| #define | [EUSART0\_CS\_PA7](#a0aff0e33c99569acdff8882c376ab733)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x7) |
| #define | [EUSART0\_CS\_PA8](#aecff621fa71796d796b02908db5f0305)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x8) |
| #define | [EUSART0\_CS\_PA9](#a996818e2a513b1dde0b29cbafe3e5fb0)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x9) |
| #define | [EUSART0\_CS\_PB0](#a7ace842a3a572ea81be1245e0ed3da90)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x1, 0x0) |
| #define | [EUSART0\_CS\_PB1](#ad6557ba2b6c3d89732c097dc0c1df74b)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x1, 0x1) |
| #define | [EUSART0\_CS\_PB2](#ad601437b58f8f23ad6ad052ea9176547)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x1, 0x2) |
| #define | [EUSART0\_CS\_PB3](#a15627a1b7477e5079ebcdbf77e08283c)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x1, 0x3) |
| #define | [EUSART0\_CS\_PB4](#a94f843865ca0025d3436c71e86ef9c34)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x1, 0x4) |
| #define | [EUSART0\_CS\_PB5](#aa033023f7156fd751ed72b695d5f0467)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x1, 0x5) |
| #define | [EUSART0\_RTS\_PA0](#a4e8066ef85c98c6311cdff1ea85c0b0e)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x0) |
| #define | [EUSART0\_RTS\_PA1](#a8fb4dee00cdbb65ef6b771e1f6923333)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x1) |
| #define | [EUSART0\_RTS\_PA2](#af65566f1bbb87d7a789a558b7ba99905)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x2) |
| #define | [EUSART0\_RTS\_PA3](#a0cfcb844b17fb5054cdb97bd380d75c8)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x3) |
| #define | [EUSART0\_RTS\_PA4](#a1a144a6bd83a1872b99f6efadc3b9521)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x4) |
| #define | [EUSART0\_RTS\_PA5](#a870cd278a7c1a757f2189d07171b9f99)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x5) |
| #define | [EUSART0\_RTS\_PA6](#a579aa029440d7705d0648a7b0bacfcb3)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x6) |
| #define | [EUSART0\_RTS\_PA7](#adced5ad51aca90ec512b6206a83ad2cc)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x7) |
| #define | [EUSART0\_RTS\_PA8](#acd2ec0a2bbec98d10b7e30f0e576763c)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x8) |
| #define | [EUSART0\_RTS\_PA9](#a7fab8db0707d81e3456333c5474eb44b)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x9) |
| #define | [EUSART0\_RTS\_PB0](#a4ceaf57a7bf9921f8095d32de5f0ab66)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x1, 0x0) |
| #define | [EUSART0\_RTS\_PB1](#a2249a367a7276af293997584be24dad2)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x1, 0x1) |
| #define | [EUSART0\_RTS\_PB2](#adf3dac7572179dcc0766f81f7bd648cf)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x1, 0x2) |
| #define | [EUSART0\_RTS\_PB3](#a04c83284f28797c089ca46d4a432e905)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x1, 0x3) |
| #define | [EUSART0\_RTS\_PB4](#a953d9ef327a7b0eb5dedd69eba7b0b9a)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x1, 0x4) |
| #define | [EUSART0\_RTS\_PB5](#a23a1eab8002288306e26a2925365df1b)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x1, 0x5) |
| #define | [EUSART0\_RX\_PA0](#a2b46bf2b099bf87941bbd4c29b77fee8)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x0) |
| #define | [EUSART0\_RX\_PA1](#a22bfbf4a894d55b3c59983a0a60fdb00)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x1) |
| #define | [EUSART0\_RX\_PA2](#a529e5bbdda4e497f5a71a78dd2628c91)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x2) |
| #define | [EUSART0\_RX\_PA3](#a7ffae82c7d17cebc1d662a65b6d44a59)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x3) |
| #define | [EUSART0\_RX\_PA4](#afab762ebf79c6816237382f135e88820)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x4) |
| #define | [EUSART0\_RX\_PA5](#a346155c0747c9bbbdf254bbea5c37408)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x5) |
| #define | [EUSART0\_RX\_PA6](#a90cca23bf07a59ad80d47e3c52683224)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x6) |
| #define | [EUSART0\_RX\_PA7](#a5ef7abc333b9450ec72e144384a2369d)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x7) |
| #define | [EUSART0\_RX\_PA8](#a05989116473a2986fd70707a2a41c869)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x8) |
| #define | [EUSART0\_RX\_PA9](#a06945aeff3f352e71804082c6afd234e)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x9) |
| #define | [EUSART0\_RX\_PB0](#a1a59a7ed291e816ece0bc12cffd98f39)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x1, 0x0) |
| #define | [EUSART0\_RX\_PB1](#a1bb9368d71f3b8140274beed383a465f)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x1, 0x1) |
| #define | [EUSART0\_RX\_PB2](#ac684b9dbb5433cf963027fd3ab0cd1fb)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x1, 0x2) |
| #define | [EUSART0\_RX\_PB3](#afb6d2142c3766fdede31602e56e1281a)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x1, 0x3) |
| #define | [EUSART0\_RX\_PB4](#aa4cb55bd34f6f1ae67e46e0bbbfed055)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x1, 0x4) |
| #define | [EUSART0\_RX\_PB5](#a9b922bbda2db8c0f13455c2a8916cc3b)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x1, 0x5) |
| #define | [EUSART0\_SCLK\_PA0](#a0a19d2153b70b8ef0e074fb8daadba20)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x0) |
| #define | [EUSART0\_SCLK\_PA1](#aca8e4898f56d57aff5909b5e8f56eee0)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x1) |
| #define | [EUSART0\_SCLK\_PA2](#abbc7ccc93b8fe675a34aea51b63f52ef)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x2) |
| #define | [EUSART0\_SCLK\_PA3](#a08190aaeb8a375f69bc3af20b6cea6bf)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x3) |
| #define | [EUSART0\_SCLK\_PA4](#a4e49a5735fc4f636e31c770b01960242)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x4) |
| #define | [EUSART0\_SCLK\_PA5](#a5bb9d1463e97d8683ff98741b989f82c)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x5) |
| #define | [EUSART0\_SCLK\_PA6](#a2465c3c97ea670afb2f6e579ba7e2db3)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x6) |
| #define | [EUSART0\_SCLK\_PA7](#a038e6fb8ad493dee10235499595210d8)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x7) |
| #define | [EUSART0\_SCLK\_PA8](#aa5c4e4ec06af3d9212e1fc8200a28639)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x8) |
| #define | [EUSART0\_SCLK\_PA9](#a237b1078b65f552cd9501ba9e97e72f6)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x9) |
| #define | [EUSART0\_SCLK\_PB0](#ad1159b33436207a1b896cd71f51730dd)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x1, 0x0) |
| #define | [EUSART0\_SCLK\_PB1](#a2253345ed59d0d340c7b077ae8d689b4)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x1, 0x1) |
| #define | [EUSART0\_SCLK\_PB2](#a1dbc32ec456a7c882c71dddf254dec53)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x1, 0x2) |
| #define | [EUSART0\_SCLK\_PB3](#a27cc8d09e0ca7ac92e6022ed35fc2549)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x1, 0x3) |
| #define | [EUSART0\_SCLK\_PB4](#aeb794afde863684b4166b657b797f837)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x1, 0x4) |
| #define | [EUSART0\_SCLK\_PB5](#a02bd951a8041d26a50ed6d3dac3a1435)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x1, 0x5) |
| #define | [EUSART0\_TX\_PA0](#ad1d73b89a55be3c3b76309827c392e70)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x0) |
| #define | [EUSART0\_TX\_PA1](#a01b89a42fcc33bd36f8c419017a473ec)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x1) |
| #define | [EUSART0\_TX\_PA2](#a84c240d7825740c4b18aebe068e788d6)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x2) |
| #define | [EUSART0\_TX\_PA3](#aafac5282dba172a3e073c31d29085d10)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x3) |
| #define | [EUSART0\_TX\_PA4](#a7889459ce02255a24f9cc968c1bc0e1c)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x4) |
| #define | [EUSART0\_TX\_PA5](#ab2845f805e7c75787b24d924dcccfe68)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x5) |
| #define | [EUSART0\_TX\_PA6](#ab129226f0405530f5cd911cd423fc1b9)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x6) |
| #define | [EUSART0\_TX\_PA7](#a26eba150ba1aaf50e9a6059588aeaf1a)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x7) |
| #define | [EUSART0\_TX\_PA8](#a318a4670d6912095c2dba8c6dd8c9623)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x8) |
| #define | [EUSART0\_TX\_PA9](#af3761eef1a29ecb641f39ff9244a4e13)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x9) |
| #define | [EUSART0\_TX\_PB0](#a8d6a3ec6a9d1076b9174a66023685407)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x1, 0x0) |
| #define | [EUSART0\_TX\_PB1](#a77c5c04618ba4ce29cb1ccdb0624bf36)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x1, 0x1) |
| #define | [EUSART0\_TX\_PB2](#a8ec4a7e6c0d3eb4d66b25495c4e339f5)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x1, 0x2) |
| #define | [EUSART0\_TX\_PB3](#a3c0337cddda08df662dae06438bb0330)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x1, 0x3) |
| #define | [EUSART0\_TX\_PB4](#aede0d7fee53f6b2f345752bf9fdba30c)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x1, 0x4) |
| #define | [EUSART0\_TX\_PB5](#a2cbf95c30f80d05041caabc3cc03e4b4)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x1, 0x5) |
| #define | [EUSART0\_CTS\_PA0](#aa78640d4f3389404bbe47f35bbb1c02a)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x0) |
| #define | [EUSART0\_CTS\_PA1](#a43cbc88ff21700a62c42b35e8f67c0b1)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x1) |
| #define | [EUSART0\_CTS\_PA2](#a9e7c4aa3a487cbfa8019667b06e01ed9)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x2) |
| #define | [EUSART0\_CTS\_PA3](#a200ad378e054581fc0af32901db945d9)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x3) |
| #define | [EUSART0\_CTS\_PA4](#aba12ae15b468c70e21089ddbb4228bb2)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x4) |
| #define | [EUSART0\_CTS\_PA5](#a3eefe0f1fcafd901fc9ab7d90d57f5ce)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x5) |
| #define | [EUSART0\_CTS\_PA6](#a1f097826e960d3358db147f4a324ee49)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x6) |
| #define | [EUSART0\_CTS\_PA7](#a9d74f4aa54f500f1ff4839eaf1f29b3f)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x7) |
| #define | [EUSART0\_CTS\_PA8](#af31e2b373140e3eb7f01b90067847104)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x8) |
| #define | [EUSART0\_CTS\_PA9](#abfa5ad8998c88fa5304388413ad3fb62)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x9) |
| #define | [EUSART0\_CTS\_PB0](#ae41b867ca4046c838fa20049b685de44)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x1, 0x0) |
| #define | [EUSART0\_CTS\_PB1](#a06e7277edcf4f30266d9dc9b9bcddb9d)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x1, 0x1) |
| #define | [EUSART0\_CTS\_PB2](#a7908f6ee431528d7c4d4345b78c0c0c1)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x1, 0x2) |
| #define | [EUSART0\_CTS\_PB3](#a453f6ccc79c1145a755f667f0d716364)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x1, 0x3) |
| #define | [EUSART0\_CTS\_PB4](#a292c1725298cb2fe05ccf9c610c9a971)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x1, 0x4) |
| #define | [EUSART0\_CTS\_PB5](#a9f99e0775d7c0b53a7c06307efe5f548)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x1, 0x5) |
| #define | [EUSART1\_CS\_PA0](#a40f82c8c64899e7d6814527efbbebe93)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x0) |
| #define | [EUSART1\_CS\_PA1](#af63951a9525443f244715b5a955c6653)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x1) |
| #define | [EUSART1\_CS\_PA2](#a888362b3adc4669f5a60462d0ae73334)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x2) |
| #define | [EUSART1\_CS\_PA3](#accc804e7c4664309a021a7a8c591af6c)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x3) |
| #define | [EUSART1\_CS\_PA4](#a770e6e5582d1e29c8b23a90628b3e57c)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x4) |
| #define | [EUSART1\_CS\_PA5](#ae3ef936bb7be77cfdce700627f231ec7)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x5) |
| #define | [EUSART1\_CS\_PA6](#a4a45381fe7d897de6e53043fb47ef13e)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x6) |
| #define | [EUSART1\_CS\_PA7](#a637c7be3f82194e942972cde56bbb686)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x7) |
| #define | [EUSART1\_CS\_PA8](#a3f561023c637eba25ac1d46c36e20a80)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x8) |
| #define | [EUSART1\_CS\_PA9](#a08375c829f9d68aeff931ec481429fb3)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x9) |
| #define | [EUSART1\_CS\_PB0](#acdbe2339b99a4fe502bba246a626d5c2)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x1, 0x0) |
| #define | [EUSART1\_CS\_PB1](#a7f14f23f53baa612f22609dea451f445)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x1, 0x1) |
| #define | [EUSART1\_CS\_PB2](#a619bea931dfb9441abd013c5f3f70be7)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x1, 0x2) |
| #define | [EUSART1\_CS\_PB3](#a620516494e3be49f80bb70a9c0da28ac)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x1, 0x3) |
| #define | [EUSART1\_CS\_PB4](#afd07cc566c75f403760a1754ec784e92)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x1, 0x4) |
| #define | [EUSART1\_CS\_PB5](#a2a06250d6353f8e710e429414896e828)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x1, 0x5) |
| #define | [EUSART1\_CS\_PC0](#a015e088a759762fcf0c47c9b4033b66c)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x0) |
| #define | [EUSART1\_CS\_PC1](#a176087a622c1e9f7bf968bd59381691b)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x1) |
| #define | [EUSART1\_CS\_PC2](#a6c4faf990cacd9a0d8e17c2aa23ed236)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x2) |
| #define | [EUSART1\_CS\_PC3](#a63386d40b9a59051bb744d043b2cce5c)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x3) |
| #define | [EUSART1\_CS\_PC4](#aa8a89563cdaff202bd581204799e6454)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x4) |
| #define | [EUSART1\_CS\_PC5](#a101b25d7d37e7b9fca411811df2662a9)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x5) |
| #define | [EUSART1\_CS\_PC6](#a55c0377bef97b860796d28a5257b04e6)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x6) |
| #define | [EUSART1\_CS\_PC7](#a847321a3e9924fb48574629393a9e777)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x7) |
| #define | [EUSART1\_CS\_PC8](#ad6bae311c5b34b86f4a5f33a2f97fae8)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x8) |
| #define | [EUSART1\_CS\_PC9](#a9d063c8af1204995448f3fa1d51d1fb4)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x9) |
| #define | [EUSART1\_CS\_PD0](#abaf2f2d1169cde30d7cc29eb843f5ed8)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x3, 0x0) |
| #define | [EUSART1\_CS\_PD1](#aa4b4634c5f80cdd71c0b806ffc72df65)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x3, 0x1) |
| #define | [EUSART1\_CS\_PD2](#af38ecf13151c02150a2313cd3b9ddf7f)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x3, 0x2) |
| #define | [EUSART1\_CS\_PD3](#a8b9a6da38263a9cd3585a3bee8ae937d)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x3, 0x3) |
| #define | [EUSART1\_CS\_PD4](#a4ee8e0542529402fc418e7096431e376)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x3, 0x4) |
| #define | [EUSART1\_CS\_PD5](#a122e1f8045702616fe121e37f329e0f0)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x3, 0x5) |
| #define | [EUSART1\_RTS\_PA0](#abc1f657ca7df682bd31439ae830e1c6b)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x0) |
| #define | [EUSART1\_RTS\_PA1](#ae0269aec4dd2413b32ed157eeec8e810)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x1) |
| #define | [EUSART1\_RTS\_PA2](#a562cacf73b6eca2f6feffb7e494ec806)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x2) |
| #define | [EUSART1\_RTS\_PA3](#ac832d962a34bd67b3d6874629191f3d8)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x3) |
| #define | [EUSART1\_RTS\_PA4](#a59c071c3b6b1940bfc67b537be8f9d03)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x4) |
| #define | [EUSART1\_RTS\_PA5](#a60a05e2ee467a334f4acba3032724efd)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x5) |
| #define | [EUSART1\_RTS\_PA6](#a9070e646c606ad24ea2a49024e93d2ec)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x6) |
| #define | [EUSART1\_RTS\_PA7](#ab692bb94e9ffe0930767caeae52a1bc9)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x7) |
| #define | [EUSART1\_RTS\_PA8](#a4eac1cef4c4df24f56c4422ff00e540b)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x8) |
| #define | [EUSART1\_RTS\_PA9](#ab3785305b7008e1abbaf35451cd764d8)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x9) |
| #define | [EUSART1\_RTS\_PB0](#a7b73f6a89a0a8707e7d3caf7c9e1bfcf)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x1, 0x0) |
| #define | [EUSART1\_RTS\_PB1](#a3ee5218e6cd62cf429ed39483dad68b0)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x1, 0x1) |
| #define | [EUSART1\_RTS\_PB2](#ad6a72d46a8632364b669d57f425c97b7)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x1, 0x2) |
| #define | [EUSART1\_RTS\_PB3](#ad964d10c49afb6b27ccff6537e1f92e8)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x1, 0x3) |
| #define | [EUSART1\_RTS\_PB4](#af1faa3155f2eb599cb02114bf58484b0)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x1, 0x4) |
| #define | [EUSART1\_RTS\_PB5](#a24d3939624d3bcdd1ea8ccd4c652581c)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x1, 0x5) |
| #define | [EUSART1\_RTS\_PC0](#acc9df99d6f67349407eab1963962329a)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x0) |
| #define | [EUSART1\_RTS\_PC1](#aa65ef7ad286ee25997d57b0c94cdcecb)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x1) |
| #define | [EUSART1\_RTS\_PC2](#a45dd8df05c9c5cfc7aa94ed8591eabe8)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x2) |
| #define | [EUSART1\_RTS\_PC3](#a38af1c47914e8c7a0823ceb0ccb25e6e)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x3) |
| #define | [EUSART1\_RTS\_PC4](#a6bc896f9f3261271d490611c1379db44)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x4) |
| #define | [EUSART1\_RTS\_PC5](#a7a5842461fe1b84f540380ec07e1822d)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x5) |
| #define | [EUSART1\_RTS\_PC6](#a5371f435ba7b54049797c8e4d57c263d)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x6) |
| #define | [EUSART1\_RTS\_PC7](#a8ed175732bc35f35c6e7487be8b903d2)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x7) |
| #define | [EUSART1\_RTS\_PC8](#ad54ae2dd1d6dcd8caaee35411927f88e)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x8) |
| #define | [EUSART1\_RTS\_PC9](#a51dd015eade83c61357a4599bbf60a10)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x9) |
| #define | [EUSART1\_RTS\_PD0](#a28ef23be5d09659645516e832ed6f65f)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x3, 0x0) |
| #define | [EUSART1\_RTS\_PD1](#a94be5cf6daa2de7b415b78c5b0e1547f)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x3, 0x1) |
| #define | [EUSART1\_RTS\_PD2](#aa8dac982c8de064268697d4bb9460973)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x3, 0x2) |
| #define | [EUSART1\_RTS\_PD3](#acb2eb162bdf3ccfdd69e17eb047a2188)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x3, 0x3) |
| #define | [EUSART1\_RTS\_PD4](#a8f6e57cd14447b3a19e5221a773c1af6)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x3, 0x4) |
| #define | [EUSART1\_RTS\_PD5](#a3cd4f764e0e73ac98673cb79e6b03f6f)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x3, 0x5) |
| #define | [EUSART1\_RX\_PA0](#a2c1a7ed0cc467841cebcf24d44d2f258)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x0) |
| #define | [EUSART1\_RX\_PA1](#a7e33ba392cb53d219f1eda52d67a6944)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x1) |
| #define | [EUSART1\_RX\_PA2](#a3c0f7f785f61504faf51fd3155ff02d6)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x2) |
| #define | [EUSART1\_RX\_PA3](#ad40833154f299658986ad7ad63ec1b96)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x3) |
| #define | [EUSART1\_RX\_PA4](#a6c41b67649a5c2d1e861fe316e0ef533)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x4) |
| #define | [EUSART1\_RX\_PA5](#af0868cbd1c8abf3e71227bfb70f46f22)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x5) |
| #define | [EUSART1\_RX\_PA6](#a8245e0aca9ea584f0490aee19687c067)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x6) |
| #define | [EUSART1\_RX\_PA7](#a7b51646c08b9fc0ba688c99c623b5d18)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x7) |
| #define | [EUSART1\_RX\_PA8](#af00e3232320d0c3fd07e60c9aa13f55e)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x8) |
| #define | [EUSART1\_RX\_PA9](#a00c0fc9b40bd7d8865a9d8da174cc38b)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x9) |
| #define | [EUSART1\_RX\_PB0](#a6b070084786fd60d676b2c2f75c1f98e)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x1, 0x0) |
| #define | [EUSART1\_RX\_PB1](#a77554a2b4ae43d009a9e15fd3f4028e3)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x1, 0x1) |
| #define | [EUSART1\_RX\_PB2](#ac2fa1d52ab0de981d47e9b65ab9665cb)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x1, 0x2) |
| #define | [EUSART1\_RX\_PB3](#ae0ee1a1afcf0079d4a9283bdd3e60588)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x1, 0x3) |
| #define | [EUSART1\_RX\_PB4](#aaec2f1281d66ce906061624d4917baa6)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x1, 0x4) |
| #define | [EUSART1\_RX\_PB5](#a1e542f9e26793dff053ab53cb32b08f1)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x1, 0x5) |
| #define | [EUSART1\_RX\_PC0](#aa98270d29aa5350d603b6801b81e061e)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x0) |
| #define | [EUSART1\_RX\_PC1](#a03ee872913b0d67c65f8dc385fb4e91a)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x1) |
| #define | [EUSART1\_RX\_PC2](#ac4aadea1a819cf4e285f89d27718552f)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x2) |
| #define | [EUSART1\_RX\_PC3](#a83b13f35d15a557bf9a53bb4a439805f)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x3) |
| #define | [EUSART1\_RX\_PC4](#a70d814531178d1d9b15c789076835b1e)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x4) |
| #define | [EUSART1\_RX\_PC5](#a458e9dbc13a3dab016b5507d65ab6292)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x5) |
| #define | [EUSART1\_RX\_PC6](#a5b74541abae3c7c46603704b893c8f77)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x6) |
| #define | [EUSART1\_RX\_PC7](#a64abe91c5e0ee069f4e7cd9f1988408a)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x7) |
| #define | [EUSART1\_RX\_PC8](#aaedbd57fd7ea06c37bc76fead37a8cca)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x8) |
| #define | [EUSART1\_RX\_PC9](#a1c742aedd3c09961965f08a26a899339)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x9) |
| #define | [EUSART1\_RX\_PD0](#a98f3d4c0fd1c382b3e74de148239493b)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x3, 0x0) |
| #define | [EUSART1\_RX\_PD1](#a2bcf22654333629b1512b192fafaabf8)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x3, 0x1) |
| #define | [EUSART1\_RX\_PD2](#a23ec89755383423270053f9d62cb3052)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x3, 0x2) |
| #define | [EUSART1\_RX\_PD3](#a3b66d7466704954a9c4f7d114cc3948b)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x3, 0x3) |
| #define | [EUSART1\_RX\_PD4](#a642ec25a709db3727086999a94e10518)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x3, 0x4) |
| #define | [EUSART1\_RX\_PD5](#a99b0e129557e42a51fafdad86034c5d3)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x3, 0x5) |
| #define | [EUSART1\_SCLK\_PA0](#a1866dd8e210ba1ab2877a58fed00c93e)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x0) |
| #define | [EUSART1\_SCLK\_PA1](#a48c98c4dadaf125f1a227ef37bbf9738)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x1) |
| #define | [EUSART1\_SCLK\_PA2](#a1f529ea54ec4efcdc13c99ccf42b3db9)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x2) |
| #define | [EUSART1\_SCLK\_PA3](#a576b277096ee6c9b14a99627e77720d3)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x3) |
| #define | [EUSART1\_SCLK\_PA4](#ac13a88d3cd2571fdc2a57284e6d62c09)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x4) |
| #define | [EUSART1\_SCLK\_PA5](#adbce8bccdef55112969e797c7b6639dd)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x5) |
| #define | [EUSART1\_SCLK\_PA6](#a7c77e84e1434e302f03737b24d1ff079)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x6) |
| #define | [EUSART1\_SCLK\_PA7](#aaf42811c16b367f1abf8e6bc160a8c20)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x7) |
| #define | [EUSART1\_SCLK\_PA8](#aebab59d6a37e8c841da4f390387897ab)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x8) |
| #define | [EUSART1\_SCLK\_PA9](#a00c2d9101c157ff6a294b0b79f295365)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x9) |
| #define | [EUSART1\_SCLK\_PB0](#a203c4398d642eada6bda1cc7bf80bfbe)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x1, 0x0) |
| #define | [EUSART1\_SCLK\_PB1](#abd4a43cfc4b84a8b2e1c4097771d7a59)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x1, 0x1) |
| #define | [EUSART1\_SCLK\_PB2](#abe989ab643fbe91732fc5d85c4b8c560)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x1, 0x2) |
| #define | [EUSART1\_SCLK\_PB3](#afb4913ed4eb217a972c17821c2eafc27)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x1, 0x3) |
| #define | [EUSART1\_SCLK\_PB4](#a640a1a6ece43715d2122cb4ced70543a)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x1, 0x4) |
| #define | [EUSART1\_SCLK\_PB5](#ab6152389b3d34387306a4cd554b4d573)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x1, 0x5) |
| #define | [EUSART1\_SCLK\_PC0](#a7d65400748ea9527510a0e34f410b8c3)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x0) |
| #define | [EUSART1\_SCLK\_PC1](#a7ea3f4ca3c6e8f920c68e7a9bd4f58cb)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x1) |
| #define | [EUSART1\_SCLK\_PC2](#ad2998e2a2182b75f088ca5bcbc95753a)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x2) |
| #define | [EUSART1\_SCLK\_PC3](#ab26cf07e0496f46713893e36521d8cc1)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x3) |
| #define | [EUSART1\_SCLK\_PC4](#acc5b977ae91e36cb79a4274f06d185f3)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x4) |
| #define | [EUSART1\_SCLK\_PC5](#aee5ca21dcd28e168927431e40848d6f5)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x5) |
| #define | [EUSART1\_SCLK\_PC6](#aaf2c62839097ad29f904dd4022f0b27c)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x6) |
| #define | [EUSART1\_SCLK\_PC7](#a78cf96f19e780387646d3e3cdf32deef)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x7) |
| #define | [EUSART1\_SCLK\_PC8](#a6779aeaccb85a2c1fd6f14ad649c4441)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x8) |
| #define | [EUSART1\_SCLK\_PC9](#af6eb3759c39650e9ce7c74c302c8c118)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x9) |
| #define | [EUSART1\_SCLK\_PD0](#a9b74e299bdafb94c3f419e003aea18df)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x3, 0x0) |
| #define | [EUSART1\_SCLK\_PD1](#a8f314da8501571ed1fb5d9043a48f022)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x3, 0x1) |
| #define | [EUSART1\_SCLK\_PD2](#a2ca42149963e87a955e9bc529ba1764e)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x3, 0x2) |
| #define | [EUSART1\_SCLK\_PD3](#a408f40e7306530450a58ad4135df0401)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x3, 0x3) |
| #define | [EUSART1\_SCLK\_PD4](#a2e59776258bebc0ce491a8a4f8357606)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x3, 0x4) |
| #define | [EUSART1\_SCLK\_PD5](#a6ffd1010e2bd742569fc4c3a4c3b7bbb)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x3, 0x5) |
| #define | [EUSART1\_TX\_PA0](#ab28778a5ee4f114285190a082c927118)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x0) |
| #define | [EUSART1\_TX\_PA1](#a073c517a0afd9587386870a630518cbd)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x1) |
| #define | [EUSART1\_TX\_PA2](#a806e7fc362384bc93b618a12af2473f8)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x2) |
| #define | [EUSART1\_TX\_PA3](#a1702c830397c60f0b30b2b9fd9952f0d)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x3) |
| #define | [EUSART1\_TX\_PA4](#a6f0b72325d6aafe9f875e9742a8c8042)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x4) |
| #define | [EUSART1\_TX\_PA5](#ad0cde738ee0488057252b99b667ad00d)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x5) |
| #define | [EUSART1\_TX\_PA6](#a448daaeb0e09d7e8ed1629f93c909539)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x6) |
| #define | [EUSART1\_TX\_PA7](#aea3b8d30b2e1e43348278c7e33e33aa5)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x7) |
| #define | [EUSART1\_TX\_PA8](#a01920e5d24b2a800d5a1b0d0341b9b1b)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x8) |
| #define | [EUSART1\_TX\_PA9](#a0323bbaaef73d01d2a1321ccc8faba4b)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x9) |
| #define | [EUSART1\_TX\_PB0](#ab39ba8c4be315f5a2222e168f474642d)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x1, 0x0) |
| #define | [EUSART1\_TX\_PB1](#a71460a9b69af5340d0a13823fde821ec)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x1, 0x1) |
| #define | [EUSART1\_TX\_PB2](#ae589d9854e598c01eeb5f660d4b07a61)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x1, 0x2) |
| #define | [EUSART1\_TX\_PB3](#a8387994c7648c19dd755c09827923d8f)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x1, 0x3) |
| #define | [EUSART1\_TX\_PB4](#a30635d481b97dd113d97f53faf8fcfe2)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x1, 0x4) |
| #define | [EUSART1\_TX\_PB5](#a02a498c823ba30dbd5144e3f97da331c)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x1, 0x5) |
| #define | [EUSART1\_TX\_PC0](#af974aba626dbdc04f04bcc6f13243b94)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x0) |
| #define | [EUSART1\_TX\_PC1](#aa7802a5b57a1024764ffbe73b6b5ac39)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x1) |
| #define | [EUSART1\_TX\_PC2](#a0c9b5f28eb50a9731a117ad5f366e92b)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x2) |
| #define | [EUSART1\_TX\_PC3](#a6a348ac2b04733efa6c0ebe34ceb5d4b)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x3) |
| #define | [EUSART1\_TX\_PC4](#a54dfb623abae97d99fa141c8a0bb0ea3)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x4) |
| #define | [EUSART1\_TX\_PC5](#a1100968240942c988f4905912c28aa11)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x5) |
| #define | [EUSART1\_TX\_PC6](#a6e8d91efe4ac6f8224907e3ee500051c)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x6) |
| #define | [EUSART1\_TX\_PC7](#aed9ea236a9a98dbcc9516c4517cb04ed)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x7) |
| #define | [EUSART1\_TX\_PC8](#ac017586ff569895b658de00f8d60043c)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x8) |
| #define | [EUSART1\_TX\_PC9](#a342a564672104c6a47d12b75a3c4b726)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x9) |
| #define | [EUSART1\_TX\_PD0](#a21666ee324c7d8339c10ee3a5841413b)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x3, 0x0) |
| #define | [EUSART1\_TX\_PD1](#a63920c4b35211b7a2db371b6db68fe34)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x3, 0x1) |
| #define | [EUSART1\_TX\_PD2](#a196cf0e44c04a0b39c143d89f674bc7d)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x3, 0x2) |
| #define | [EUSART1\_TX\_PD3](#acd2c8e123057d490ba2e60b8dbac8836)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x3, 0x3) |
| #define | [EUSART1\_TX\_PD4](#a5dcbf90a838018015ab60c8f480aa341)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x3, 0x4) |
| #define | [EUSART1\_TX\_PD5](#a2cd212d6d8646fd8a6b0ea295a0e0426)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x3, 0x5) |
| #define | [EUSART1\_CTS\_PA0](#a8d81221acf4017c05ca56c5a98d58552)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x0) |
| #define | [EUSART1\_CTS\_PA1](#a5d4da4feea93c4b06110ca1e3610659a)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x1) |
| #define | [EUSART1\_CTS\_PA2](#af8e1f1909c844d7c2f4b531c82f5c7cb)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x2) |
| #define | [EUSART1\_CTS\_PA3](#a69bd0b952644909144e49f6542d88c92)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x3) |
| #define | [EUSART1\_CTS\_PA4](#a36ce96157ce9be04de043bb2c04cef82)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x4) |
| #define | [EUSART1\_CTS\_PA5](#aa6351a3c82698810d1041413513553fc)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x5) |
| #define | [EUSART1\_CTS\_PA6](#a76dfe398fdb4ed75ae511b29a1d347b0)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x6) |
| #define | [EUSART1\_CTS\_PA7](#ab84cf2fc8ac1a7f5666769f283ec3e49)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x7) |
| #define | [EUSART1\_CTS\_PA8](#aeb09839ecbdd7f2c608e25602a302752)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x8) |
| #define | [EUSART1\_CTS\_PA9](#a46ecc03c0f9a382360aed7344ae35eb4)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x9) |
| #define | [EUSART1\_CTS\_PB0](#a883da4be324d198cbc34ea41676a9ddf)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x1, 0x0) |
| #define | [EUSART1\_CTS\_PB1](#acc196631f4adce64be8891275c851cc8)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x1, 0x1) |
| #define | [EUSART1\_CTS\_PB2](#ad56423043df1ba928037fb8ad7996a0a)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x1, 0x2) |
| #define | [EUSART1\_CTS\_PB3](#aaf246a8e049ac1b6f0ea6bff0f77d361)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x1, 0x3) |
| #define | [EUSART1\_CTS\_PB4](#a8d541570c6ca67dd288bf96afaa86d00)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x1, 0x4) |
| #define | [EUSART1\_CTS\_PB5](#a250c70e460b2087d794ea42380ce871e)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x1, 0x5) |
| #define | [EUSART1\_CTS\_PC0](#a71b2e656c782b69d56a103e73b464730)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x0) |
| #define | [EUSART1\_CTS\_PC1](#a3de408c7045ed45e7dc371443c370c23)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x1) |
| #define | [EUSART1\_CTS\_PC2](#a448af5a813508ad8dd8e5d6e5df4b43b)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x2) |
| #define | [EUSART1\_CTS\_PC3](#a5bca4e376d8315ef91f8574ced26eb16)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x3) |
| #define | [EUSART1\_CTS\_PC4](#aa72d1c30858bde17689ed0dfc57069bb)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x4) |
| #define | [EUSART1\_CTS\_PC5](#a70ecbc7c78a15bcdc81b997d720b0b0c)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x5) |
| #define | [EUSART1\_CTS\_PC6](#aa6fc0b0cd1690dd9d8e898b4177deb1f)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x6) |
| #define | [EUSART1\_CTS\_PC7](#a9f21efe766114885dc079c88593fc66a)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x7) |
| #define | [EUSART1\_CTS\_PC8](#a611caa47f0896dc5f8bd552e27b7e887)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x8) |
| #define | [EUSART1\_CTS\_PC9](#ad6bea69f152a00c80b5a6170f714b802)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x9) |
| #define | [EUSART1\_CTS\_PD0](#ae2238ef628fa06b7eb97f58b86bf011b)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x3, 0x0) |
| #define | [EUSART1\_CTS\_PD1](#ae15d8faf92ba3b2b4c07eddf5d6fd274)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x3, 0x1) |
| #define | [EUSART1\_CTS\_PD2](#aef76a9fbbcbd9a4e8d254773bba07126)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x3, 0x2) |
| #define | [EUSART1\_CTS\_PD3](#aa32ab3b05dc99adbfb5b3a84642b6403)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x3, 0x3) |
| #define | [EUSART1\_CTS\_PD4](#af0c7e457f0de9267f6bf4c2e1a5e0f3f)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x3, 0x4) |
| #define | [EUSART1\_CTS\_PD5](#ab4fe681884230878b055e04a23eb9ec3)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x3, 0x5) |
| #define | [PTI\_DCLK\_PC0](#a5bdf4f259033a31adaa4e25fe84604ed)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x0) |
| #define | [PTI\_DCLK\_PC1](#aa4e24633e84b6487f85a598419ea7e7d)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x1) |
| #define | [PTI\_DCLK\_PC2](#a53fa8c98bed45c485839c1d86d343733)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x2) |
| #define | [PTI\_DCLK\_PC3](#a930a4ba462ce768196265ec5a53557ba)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x3) |
| #define | [PTI\_DCLK\_PC4](#ae90e5e4841b04412ca3768216d0efaf1)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x4) |
| #define | [PTI\_DCLK\_PC5](#a27b9c07fbbc05a0bd69dd74cc17db0d0)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x5) |
| #define | [PTI\_DCLK\_PC6](#ae36628394c440c14e85b42db8095cba6)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x6) |
| #define | [PTI\_DCLK\_PC7](#a024f81027127cdacccc05c4b49cf99c0)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x7) |
| #define | [PTI\_DCLK\_PC8](#a8429fb0338b35f58958dafd47ad1112c)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x8) |
| #define | [PTI\_DCLK\_PC9](#afe7de2b591c78a6f71d5cb7192cfb16a)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x9) |
| #define | [PTI\_DCLK\_PD0](#a354b3eb4fe4c5e11e1c944761bf00095)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x3, 0x0) |
| #define | [PTI\_DCLK\_PD1](#a14260512bf2682c2fb84fa96f00de9ba)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x3, 0x1) |
| #define | [PTI\_DCLK\_PD2](#af96542673625d7a20712ad4c31953d4b)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x3, 0x2) |
| #define | [PTI\_DCLK\_PD3](#ab234da9210beb7b1f94b75aa9ecf52ca)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x3, 0x3) |
| #define | [PTI\_DCLK\_PD4](#ab16f467d07715a204580f48ed0affd78)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x3, 0x4) |
| #define | [PTI\_DCLK\_PD5](#a5ed7f92ba37daf241ff2d2cd2b91ad5a)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x3, 0x5) |
| #define | [PTI\_DFRAME\_PC0](#aaa3fdc625a5f096099d23c1760980055)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x0) |
| #define | [PTI\_DFRAME\_PC1](#a23de813c7f0e88b8397ebcc34eb21552)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x1) |
| #define | [PTI\_DFRAME\_PC2](#a667adbc7570cf85833284a141de5fa2d)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x2) |
| #define | [PTI\_DFRAME\_PC3](#afea8ff0ad63b50a277e69f305b64e7cd)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x3) |
| #define | [PTI\_DFRAME\_PC4](#a97019cfae35bfc913e7ed2456a816ab5)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x4) |
| #define | [PTI\_DFRAME\_PC5](#a15d67770385d695409d975ba26d5d0e4)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x5) |
| #define | [PTI\_DFRAME\_PC6](#a318fe553b5da2adc9ce35e2571934bc2)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x6) |
| #define | [PTI\_DFRAME\_PC7](#a0e8e93d43d78096c24db5c4483ee68e1)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x7) |
| #define | [PTI\_DFRAME\_PC8](#ad45d6ab1196c50158fa81f54208fb789)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x8) |
| #define | [PTI\_DFRAME\_PC9](#a40af15964e0e47783a6a1855066201f5)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x9) |
| #define | [PTI\_DFRAME\_PD0](#ac6a830947b330b10ae2c9e3cdc1887b4)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x3, 0x0) |
| #define | [PTI\_DFRAME\_PD1](#a1f08a23bacafb3dae71d143c2c5ab863)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x3, 0x1) |
| #define | [PTI\_DFRAME\_PD2](#acafc4bcb7af54f59dbacb7d9ce8712ce)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x3, 0x2) |
| #define | [PTI\_DFRAME\_PD3](#aee415d6eae1beab453af125a316f549c)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x3, 0x3) |
| #define | [PTI\_DFRAME\_PD4](#a63eda1bcb309b3dfea7a3130fd2d8460)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x3, 0x4) |
| #define | [PTI\_DFRAME\_PD5](#acc221e5c9278b3e45f86dc8338599b5a)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x3, 0x5) |
| #define | [PTI\_DOUT\_PC0](#a9413ff462e44dcf3b76204629c524a73)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x0) |
| #define | [PTI\_DOUT\_PC1](#a49ef267b8afcafa1da426058b4f94d9f)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x1) |
| #define | [PTI\_DOUT\_PC2](#a8563048b51841f44cbd35c573131bf18)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x2) |
| #define | [PTI\_DOUT\_PC3](#aa4304d8154383f012e4a3b53a070b120)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x3) |
| #define | [PTI\_DOUT\_PC4](#a715e7ceca236771ae00bb36143a586d2)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x4) |
| #define | [PTI\_DOUT\_PC5](#aa2bb4223540e03b6ef7c21b05b76b380)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x5) |
| #define | [PTI\_DOUT\_PC6](#a746b97fe77bb360b3048d3cc1730b607)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x6) |
| #define | [PTI\_DOUT\_PC7](#a3e939dfef6c7f5f04abe8e32d0a866a2)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x7) |
| #define | [PTI\_DOUT\_PC8](#a5aa40ec22bb634ae3425d3badf0fb9f0)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x8) |
| #define | [PTI\_DOUT\_PC9](#aea6fe0d36dfddc5414d5e48df89c1a62)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x9) |
| #define | [PTI\_DOUT\_PD0](#a569a588da9acdad8c7b18c6d7ee83681)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x3, 0x0) |
| #define | [PTI\_DOUT\_PD1](#aac9876e72b5e68eb3d7138c72e7ac25b)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x3, 0x1) |
| #define | [PTI\_DOUT\_PD2](#a447f3b579538e9a44615dfe77e8ace24)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x3, 0x2) |
| #define | [PTI\_DOUT\_PD3](#ad80593f470c79948e0b9845cad0b739b)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x3, 0x3) |
| #define | [PTI\_DOUT\_PD4](#a33b1e16afcb1e3b391e60dbe29b3bd1c)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x3, 0x4) |
| #define | [PTI\_DOUT\_PD5](#a641c634d830b9ee090f0ad85e361c8ff)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x3, 0x5) |
| #define | [I2C0\_SCL\_PA0](#a23ced15df4b090058198bd06541b5885)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x0) |
| #define | [I2C0\_SCL\_PA1](#a695c8fa25220070f883a7866019132a5)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x1) |
| #define | [I2C0\_SCL\_PA2](#a59521028aaeca25d19dce77adf76f9b7)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x2) |
| #define | [I2C0\_SCL\_PA3](#a68f1a22cb1cf1445f9d94d230b7d81e6)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x3) |
| #define | [I2C0\_SCL\_PA4](#aefbf0c45fe8a1215f17a6d31c5948889)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x4) |
| #define | [I2C0\_SCL\_PA5](#ae334a06857e99d806213ccb6b6e582d3)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x5) |
| #define | [I2C0\_SCL\_PA6](#a912dd4938a0b0cda381360467d635fc8)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x6) |
| #define | [I2C0\_SCL\_PA7](#a843a8a1e536a19115dad9b821e09fc35)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x7) |
| #define | [I2C0\_SCL\_PA8](#a5d5194c66eaa75401ef86ae1b702c882)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x8) |
| #define | [I2C0\_SCL\_PA9](#aa8f0bedfe23ff1a8610fd95182a3e37d)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x9) |
| #define | [I2C0\_SCL\_PB0](#a66acedca2ec779cfe23f1d9c6e2fc129)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x1, 0x0) |
| #define | [I2C0\_SCL\_PB1](#a5af9487dc5b440644597f549fb4775e2)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x1, 0x1) |
| #define | [I2C0\_SCL\_PB2](#a9bf6c40a60c458dcf38ab7eff6d90768)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x1, 0x2) |
| #define | [I2C0\_SCL\_PB3](#a7cda95585deaad597713feece27a1a03)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x1, 0x3) |
| #define | [I2C0\_SCL\_PB4](#add039d286e25d19092fcee79fac5c168)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x1, 0x4) |
| #define | [I2C0\_SCL\_PB5](#a15a20ff8ec4b637e9fc1a2a892fd595d)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x1, 0x5) |
| #define | [I2C0\_SCL\_PC0](#afda900994567b6303959e4f666fceaf1)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x0) |
| #define | [I2C0\_SCL\_PC1](#aecced4d0cc1f98a1f8e87d09cceff92a)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x1) |
| #define | [I2C0\_SCL\_PC2](#ab376247e3dbd84ccfd2b94af9c07505a)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x2) |
| #define | [I2C0\_SCL\_PC3](#a9a9354d74c5e9c6ebad7e646f6b8ee63)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x3) |
| #define | [I2C0\_SCL\_PC4](#aafe4a6c9133c8213940f026568866b9d)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x4) |
| #define | [I2C0\_SCL\_PC5](#a93ad2564f0ad899a336521853e3c5f35)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x5) |
| #define | [I2C0\_SCL\_PC6](#a45d40464f74efe9babb464d9e72ac0e1)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x6) |
| #define | [I2C0\_SCL\_PC7](#aef0e85e86050336cd4112241ef60dad5)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x7) |
| #define | [I2C0\_SCL\_PC8](#a9526c92c7e0e45214d4dc62cef77541e)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x8) |
| #define | [I2C0\_SCL\_PC9](#a8a38516741fb879e1cfb2c501b3643b3)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x9) |
| #define | [I2C0\_SCL\_PD0](#ab5e0b9a784779a5e92ab1fa79c9aa6cc)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x3, 0x0) |
| #define | [I2C0\_SCL\_PD1](#a3d7b2816e4c4f01aba45a339bc77feea)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x3, 0x1) |
| #define | [I2C0\_SCL\_PD2](#a487c9ff099c2dabf34d65f0377e5e195)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x3, 0x2) |
| #define | [I2C0\_SCL\_PD3](#a2c36512ca362cf14654d72a59e4de079)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x3, 0x3) |
| #define | [I2C0\_SCL\_PD4](#ae728f208472d11bf16da3eb76a64d152)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x3, 0x4) |
| #define | [I2C0\_SCL\_PD5](#ac809898617970351e262e056c49dc0de)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x3, 0x5) |
| #define | [I2C0\_SDA\_PA0](#aaf8bcb4a387404aa356da60c0e9cc869)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x0) |
| #define | [I2C0\_SDA\_PA1](#a6f74ca01f25bdded002e45e679240275)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x1) |
| #define | [I2C0\_SDA\_PA2](#acdc71a141f1ba40bb5c3ec9f06bd35e6)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x2) |
| #define | [I2C0\_SDA\_PA3](#a401989601987cfb72944453f11918e2a)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x3) |
| #define | [I2C0\_SDA\_PA4](#a66dad3b35dd2a650a186933abb43f6c3)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x4) |
| #define | [I2C0\_SDA\_PA5](#a1fdfea195e2831a05d2ad42a091aa53b)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x5) |
| #define | [I2C0\_SDA\_PA6](#a0c5573f60342f026d0553797a636a488)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x6) |
| #define | [I2C0\_SDA\_PA7](#a35d947fc846c9fbe828b92169dbc30bd)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x7) |
| #define | [I2C0\_SDA\_PA8](#a2bafe8f8b3424002354a87423c7564ff)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x8) |
| #define | [I2C0\_SDA\_PA9](#a00b7f8f28847880fdd61b025eb224a44)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x9) |
| #define | [I2C0\_SDA\_PB0](#a9e333616419f1afb29657e239ebf9b12)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x1, 0x0) |
| #define | [I2C0\_SDA\_PB1](#a25bba68392534791cad2bc692a141782)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x1, 0x1) |
| #define | [I2C0\_SDA\_PB2](#a36d3f871769d46038f7305c590f4da44)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x1, 0x2) |
| #define | [I2C0\_SDA\_PB3](#af28ae3cd9556f78d2a9e9cbec5eea822)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x1, 0x3) |
| #define | [I2C0\_SDA\_PB4](#aa0dfa7701ac813cb33f6b192e724c028)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x1, 0x4) |
| #define | [I2C0\_SDA\_PB5](#aaca942a6078f9071a43a5a72bf2e290f)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x1, 0x5) |
| #define | [I2C0\_SDA\_PC0](#acb9a1287a10a954e1ff0bf82478f3bf8)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x0) |
| #define | [I2C0\_SDA\_PC1](#a0c89a72767592385a9a625d72c90f824)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x1) |
| #define | [I2C0\_SDA\_PC2](#a0e115e41c26b45de04ee71a95cd5b87c)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x2) |
| #define | [I2C0\_SDA\_PC3](#afbad7695056556b776533aafc47b0299)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x3) |
| #define | [I2C0\_SDA\_PC4](#a603f80b261cded3f838f85ad889a4b88)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x4) |
| #define | [I2C0\_SDA\_PC5](#a5864615c0e7063fc4f1acb8e4e3a05d2)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x5) |
| #define | [I2C0\_SDA\_PC6](#a9e461e560cc99ba58586c4a4b9085c53)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x6) |
| #define | [I2C0\_SDA\_PC7](#a1f6044bad1b47007a0250a99e778a7f4)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x7) |
| #define | [I2C0\_SDA\_PC8](#a04887e1ba3314748ec246c534c0f1815)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x8) |
| #define | [I2C0\_SDA\_PC9](#ac2e3516c9ce167083e4263fb7e78ecb6)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x9) |
| #define | [I2C0\_SDA\_PD0](#a610731cb645ab65d802d95bb65437d8c)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x3, 0x0) |
| #define | [I2C0\_SDA\_PD1](#a86eade4a55994ce4285b81cf29c93883)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x3, 0x1) |
| #define | [I2C0\_SDA\_PD2](#a5d3416853673a2192ec5f5712921d370)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x3, 0x2) |
| #define | [I2C0\_SDA\_PD3](#a096b74cd9e2842c5d4ff8d7a7186106a)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x3, 0x3) |
| #define | [I2C0\_SDA\_PD4](#a39c83c73c763c0afc7e9041fab4549fd)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x3, 0x4) |
| #define | [I2C0\_SDA\_PD5](#a031fdc04063f9f244527f159c098c8b7)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x3, 0x5) |
| #define | [I2C1\_SCL\_PC0](#a356ddb78378e70250e07992cf92dd8b7)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x0) |
| #define | [I2C1\_SCL\_PC1](#ad327d495abfaa2bb7ae3344a163f052f)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x1) |
| #define | [I2C1\_SCL\_PC2](#aa89ddd739af59624f4a176443aa17636)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x2) |
| #define | [I2C1\_SCL\_PC3](#af0e6baea8d2c35eb8991706946ffc05b)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x3) |
| #define | [I2C1\_SCL\_PC4](#a346b20cbc89a5af4dfffe00c9ef41e92)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x4) |
| #define | [I2C1\_SCL\_PC5](#aec416779b37e6a51e48e3fcadfca591a)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x5) |
| #define | [I2C1\_SCL\_PC6](#a7e3349a10010f0f54657e0fb5e92ffe2)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x6) |
| #define | [I2C1\_SCL\_PC7](#a2c5373d8cd0dfc39e30c9460552201ef)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x7) |
| #define | [I2C1\_SCL\_PC8](#ad58c7138909480a48e097484cdddf818)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x8) |
| #define | [I2C1\_SCL\_PC9](#adef41b41e7e00135ae28db22c8bc6995)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x9) |
| #define | [I2C1\_SCL\_PD0](#a865b5c341b794b96daba59c14807c057)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x3, 0x0) |
| #define | [I2C1\_SCL\_PD1](#a9f3ebaefe248d5aa292ade2727a11ee9)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x3, 0x1) |
| #define | [I2C1\_SCL\_PD2](#a7eb71571b0e15669fb353a0bd65f2c72)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x3, 0x2) |
| #define | [I2C1\_SCL\_PD3](#a6a86266c8ab637b0b31244cbf0636ab0)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x3, 0x3) |
| #define | [I2C1\_SCL\_PD4](#a575a4a9e08a65805c5d9fa3591f563bb)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x3, 0x4) |
| #define | [I2C1\_SCL\_PD5](#aa3327376858c7599a6b95c2e0be85bb8)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x3, 0x5) |
| #define | [I2C1\_SDA\_PC0](#a7239b0bfd8b71b2ee9e85e8cb2e6eaaf)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x0) |
| #define | [I2C1\_SDA\_PC1](#afe966c9b62cc1e0d598ea6ea92d663b8)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x1) |
| #define | [I2C1\_SDA\_PC2](#af3ba02992276ed2088a6652b695d270d)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x2) |
| #define | [I2C1\_SDA\_PC3](#a424670a07eab18c7e3ce3db2d68d44f6)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x3) |
| #define | [I2C1\_SDA\_PC4](#ad7eebe896b02c99e7f27340a8ea01a8f)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x4) |
| #define | [I2C1\_SDA\_PC5](#a12822294913c78002356a6be7b698e2e)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x5) |
| #define | [I2C1\_SDA\_PC6](#a9af96f372e04b931184d7a9bd716b733)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x6) |
| #define | [I2C1\_SDA\_PC7](#a766136e7b677f8c4ddcc6053b0527eee)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x7) |
| #define | [I2C1\_SDA\_PC8](#aaaae2fcde9dc48a4917da54216304dc4)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x8) |
| #define | [I2C1\_SDA\_PC9](#a2b0f34f00795ef75bf9e7cf1e85db5fc)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x9) |
| #define | [I2C1\_SDA\_PD0](#a58f45546c69325b13cd062ca7a238c7a)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x3, 0x0) |
| #define | [I2C1\_SDA\_PD1](#aa7cf52519a05cd49aef954ce5191a377)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x3, 0x1) |
| #define | [I2C1\_SDA\_PD2](#ad779ebeed2865070af9e56244e9c43d0)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x3, 0x2) |
| #define | [I2C1\_SDA\_PD3](#a77b0c5734afd5123fd3ae520f10a8da8)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x3, 0x3) |
| #define | [I2C1\_SDA\_PD4](#acc6ad96c0e1645c02ca291c641ba06dd)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x3, 0x4) |
| #define | [I2C1\_SDA\_PD5](#aa358107fadec4f7d22d77a490c01b6d6)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x3, 0x5) |
| #define | [KEYSCAN\_COLOUT0\_PA0](#a5a52c17c2d01b0d927d1f1789799baa0)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x0) |
| #define | [KEYSCAN\_COLOUT0\_PA1](#a9fff3683d3c03b4838665acece21a2b9)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x1) |
| #define | [KEYSCAN\_COLOUT0\_PA2](#ab94c7fd6fff04ec1f58ccf71a3f64d71)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x2) |
| #define | [KEYSCAN\_COLOUT0\_PA3](#a15b8ef2e967e747c47089c6063b05b0c)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x3) |
| #define | [KEYSCAN\_COLOUT0\_PA4](#a5144e066ae5582d32c35077d35561b5d)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x4) |
| #define | [KEYSCAN\_COLOUT0\_PA5](#ae24656b03d1c97af530ec70aba4a3dd0)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x5) |
| #define | [KEYSCAN\_COLOUT0\_PA6](#a1bfd896f4a8cfc3c9fc7728e605da898)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x6) |
| #define | [KEYSCAN\_COLOUT0\_PA7](#ad801588fc6185834de0756b4cc7ad515)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x7) |
| #define | [KEYSCAN\_COLOUT0\_PA8](#a4b4d69573db9515dae391c6b50c034f3)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x8) |
| #define | [KEYSCAN\_COLOUT0\_PA9](#abd423f23fddf4ebf57217456c3119a15)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x9) |
| #define | [KEYSCAN\_COLOUT0\_PB0](#ab0c4a297a4c6ed9773b553f60888a909)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x1, 0x0) |
| #define | [KEYSCAN\_COLOUT0\_PB1](#a12803bfebb31fdf51abff7e8b5493cdb)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x1, 0x1) |
| #define | [KEYSCAN\_COLOUT0\_PB2](#a4e8586a0245688807f04309a918db99f)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x1, 0x2) |
| #define | [KEYSCAN\_COLOUT0\_PB3](#a1cadf61f842c48b554b81aebc8cb9fc7)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x1, 0x3) |
| #define | [KEYSCAN\_COLOUT0\_PB4](#a8f2661a33400963325b8ac00bfba742a)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x1, 0x4) |
| #define | [KEYSCAN\_COLOUT0\_PB5](#adbafd9459e27053eeea0bba9bccc0963)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x1, 0x5) |
| #define | [KEYSCAN\_COLOUT0\_PC0](#abb524534a587b5743914ebc4dc739146)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x0) |
| #define | [KEYSCAN\_COLOUT0\_PC1](#aad7e9172ac7d76e534c7da9b7b66089e)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x1) |
| #define | [KEYSCAN\_COLOUT0\_PC2](#a9afcd7a32f9104f7cf51469e2aebef82)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x2) |
| #define | [KEYSCAN\_COLOUT0\_PC3](#a5707925aec785899730a8bfeaf394603)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x3) |
| #define | [KEYSCAN\_COLOUT0\_PC4](#a0080f5ba8da300d83288f8e5f430f397)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x4) |
| #define | [KEYSCAN\_COLOUT0\_PC5](#a2abef42db8dcce330fe2c97f20e1bf9f)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x5) |
| #define | [KEYSCAN\_COLOUT0\_PC6](#a9cc0d32219cc4ec9906eea216ba59fc6)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x6) |
| #define | [KEYSCAN\_COLOUT0\_PC7](#ab009d348c504d64e8ff6efda0648628b)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x7) |
| #define | [KEYSCAN\_COLOUT0\_PC8](#ab22d970887a912d0ca9b48bcb984fafc)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x8) |
| #define | [KEYSCAN\_COLOUT0\_PC9](#afbbf0bc01441a4ef05d408803ed785af)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x9) |
| #define | [KEYSCAN\_COLOUT0\_PD0](#ad2e95f939a9cb0a63b5a761f5172c4eb)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x3, 0x0) |
| #define | [KEYSCAN\_COLOUT0\_PD1](#a7b08c7c464bc45efe7b8a6321eab7d0a)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x3, 0x1) |
| #define | [KEYSCAN\_COLOUT0\_PD2](#a07c5cca743ef9e9116f5f052be296614)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x3, 0x2) |
| #define | [KEYSCAN\_COLOUT0\_PD3](#a4ba404af21d187ee3b2acee0bbb45b80)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x3, 0x3) |
| #define | [KEYSCAN\_COLOUT0\_PD4](#a81d01d684c85901328abae65477e8c85)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x3, 0x4) |
| #define | [KEYSCAN\_COLOUT0\_PD5](#a9e0a39cf0ea3697a658f14336b07e21a)   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x3, 0x5) |
| #define | [KEYSCAN\_COLOUT1\_PA0](#a585e4b13c4c2a32cde5e1f224e02f7ef)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x0) |
| #define | [KEYSCAN\_COLOUT1\_PA1](#a23e571b563a9b17f3995e196920ed787)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x1) |
| #define | [KEYSCAN\_COLOUT1\_PA2](#a2e2f89a8c1789ac9263d314507e9e73a)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x2) |
| #define | [KEYSCAN\_COLOUT1\_PA3](#acdad26c2b77719f828d3f880249c02e5)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x3) |
| #define | [KEYSCAN\_COLOUT1\_PA4](#a7f4d0e3b279df6d292530be268d2071b)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x4) |
| #define | [KEYSCAN\_COLOUT1\_PA5](#a8b302968635f80d94e72be44a299d27c)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x5) |
| #define | [KEYSCAN\_COLOUT1\_PA6](#a70d0d23bac357d94df02565a5425d638)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x6) |
| #define | [KEYSCAN\_COLOUT1\_PA7](#ae24777bf7cb160303784ef61983260b3)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x7) |
| #define | [KEYSCAN\_COLOUT1\_PA8](#acdb13af3e9e2a95af259e77c6dbb6c6f)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x8) |
| #define | [KEYSCAN\_COLOUT1\_PA9](#a8a5e8de7629558a6828faa47489e02d4)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x9) |
| #define | [KEYSCAN\_COLOUT1\_PB0](#aeeb75a748919caf477f64db4608c24d1)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x1, 0x0) |
| #define | [KEYSCAN\_COLOUT1\_PB1](#ac239f7a9cd68a765869ee273e055f682)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x1, 0x1) |
| #define | [KEYSCAN\_COLOUT1\_PB2](#addcb4f9d603cc3ad5f66fac5d15f5eaf)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x1, 0x2) |
| #define | [KEYSCAN\_COLOUT1\_PB3](#ae68a56d183ec317f20f4e45afb27d0a9)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x1, 0x3) |
| #define | [KEYSCAN\_COLOUT1\_PB4](#a1560ccbed329f572422ce3c9611a1bf9)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x1, 0x4) |
| #define | [KEYSCAN\_COLOUT1\_PB5](#a5599a02f156e263bdf22cb8d1aa54f05)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x1, 0x5) |
| #define | [KEYSCAN\_COLOUT1\_PC0](#a932a022eee08bafd1095c84493ae8269)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x0) |
| #define | [KEYSCAN\_COLOUT1\_PC1](#a03f0a2736a653f56eed67716b4e2e139)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x1) |
| #define | [KEYSCAN\_COLOUT1\_PC2](#a1dd0502f99367c9604216df6598f317b)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x2) |
| #define | [KEYSCAN\_COLOUT1\_PC3](#a198e72a8d977191639703245ed2bd8dc)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x3) |
| #define | [KEYSCAN\_COLOUT1\_PC4](#a5a967a7c71870a65ad9d079c7bfbaab0)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x4) |
| #define | [KEYSCAN\_COLOUT1\_PC5](#a8fe532890f0eb93e3286a8a8edf2b93f)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x5) |
| #define | [KEYSCAN\_COLOUT1\_PC6](#a15888722bdfb0bbbef8c31a4cf9c8985)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x6) |
| #define | [KEYSCAN\_COLOUT1\_PC7](#a160e29c849558b4c6999268886fb4c23)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x7) |
| #define | [KEYSCAN\_COLOUT1\_PC8](#a0fa0481356cb6b6318fcac34cb509841)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x8) |
| #define | [KEYSCAN\_COLOUT1\_PC9](#ad0cb6a921e60c3a82ea15bbaacb8774b)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x9) |
| #define | [KEYSCAN\_COLOUT1\_PD0](#a93d2ba7842a3d86906ef7e4df9749080)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x3, 0x0) |
| #define | [KEYSCAN\_COLOUT1\_PD1](#a8b422e4deb2ec1d01c2aac2f6af6bc67)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x3, 0x1) |
| #define | [KEYSCAN\_COLOUT1\_PD2](#a87d3c63729eea7683037e6654c1774cf)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x3, 0x2) |
| #define | [KEYSCAN\_COLOUT1\_PD3](#a43e07d12179fcd36df7a76153d44be01)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x3, 0x3) |
| #define | [KEYSCAN\_COLOUT1\_PD4](#a76e7168783cbdb2358839659b30a5bdc)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x3, 0x4) |
| #define | [KEYSCAN\_COLOUT1\_PD5](#aa0b8adae419c63895b1bb7d2c15be3c3)   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x3, 0x5) |
| #define | [KEYSCAN\_COLOUT2\_PA0](#a6be8610a8244eea2604a70095a1c4295)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x0) |
| #define | [KEYSCAN\_COLOUT2\_PA1](#a6603cb0d0414111622dddf2b61f3b591)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x1) |
| #define | [KEYSCAN\_COLOUT2\_PA2](#a81a89ec570413274e429f227cf538a6e)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x2) |
| #define | [KEYSCAN\_COLOUT2\_PA3](#a793b58a63d42ab849c0f8bbc86bee96c)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x3) |
| #define | [KEYSCAN\_COLOUT2\_PA4](#ad857e03569550385d2aacee030a9b544)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x4) |
| #define | [KEYSCAN\_COLOUT2\_PA5](#a3f89b59444a1cf1e18de80aa6d4b38b8)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x5) |
| #define | [KEYSCAN\_COLOUT2\_PA6](#a01768786f5ca06503028551896f969bf)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x6) |
| #define | [KEYSCAN\_COLOUT2\_PA7](#a3637bc9d929a1432ab1ede17fae1d7a4)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x7) |
| #define | [KEYSCAN\_COLOUT2\_PA8](#ae436e26a420b29f2d750b817facd0fb8)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x8) |
| #define | [KEYSCAN\_COLOUT2\_PA9](#a0c2e1f78e65657580e7d96990b93cf56)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x9) |
| #define | [KEYSCAN\_COLOUT2\_PB0](#a365aab802299270c6de27adf800dd87c)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x1, 0x0) |
| #define | [KEYSCAN\_COLOUT2\_PB1](#a2919c4881170222fc5b0ab36e238bb1c)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x1, 0x1) |
| #define | [KEYSCAN\_COLOUT2\_PB2](#acabdbd88d881e9e13ad0d63408655254)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x1, 0x2) |
| #define | [KEYSCAN\_COLOUT2\_PB3](#a27a4f418d6e94cc3a84985d21472da82)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x1, 0x3) |
| #define | [KEYSCAN\_COLOUT2\_PB4](#aa9f88e831fae771d58b15f2025becb6e)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x1, 0x4) |
| #define | [KEYSCAN\_COLOUT2\_PB5](#a2c9ebc343266b5ef73679be5b8f8f813)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x1, 0x5) |
| #define | [KEYSCAN\_COLOUT2\_PC0](#ace40c834a7c4f5278d0d3b7f9fc2494f)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x0) |
| #define | [KEYSCAN\_COLOUT2\_PC1](#af2ef81e0fd7e325580445028c001e6e8)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x1) |
| #define | [KEYSCAN\_COLOUT2\_PC2](#a03aec2318a85899434ad83e876306695)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x2) |
| #define | [KEYSCAN\_COLOUT2\_PC3](#ac0724d8d3da62eb8a1ada017f4db7559)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x3) |
| #define | [KEYSCAN\_COLOUT2\_PC4](#a8268180b2bdc425f74de1a9963f80860)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x4) |
| #define | [KEYSCAN\_COLOUT2\_PC5](#a7102c14ca84bd45f08b287984c8bb235)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x5) |
| #define | [KEYSCAN\_COLOUT2\_PC6](#a0b50ad00c28a65aeedf64dd7a9b74d6a)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x6) |
| #define | [KEYSCAN\_COLOUT2\_PC7](#a36856803b55973f9609f98cc1285deb5)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x7) |
| #define | [KEYSCAN\_COLOUT2\_PC8](#ac4b08b6179b8fe4543a853da3c95f9f9)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x8) |
| #define | [KEYSCAN\_COLOUT2\_PC9](#abc9bce5051ca6bbd875721bd5e707d11)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x9) |
| #define | [KEYSCAN\_COLOUT2\_PD0](#ace5b1670761e6a066cdea315262ca30b)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x3, 0x0) |
| #define | [KEYSCAN\_COLOUT2\_PD1](#ab66177ddf55f90cd43f8ee3d3f516ce5)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x3, 0x1) |
| #define | [KEYSCAN\_COLOUT2\_PD2](#a9757fbcc8516b46adf632109f0061da4)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x3, 0x2) |
| #define | [KEYSCAN\_COLOUT2\_PD3](#a181443f7f56e88e47a570943402478d3)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x3, 0x3) |
| #define | [KEYSCAN\_COLOUT2\_PD4](#aa31ea9f7edaabac76fc260248bb942f0)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x3, 0x4) |
| #define | [KEYSCAN\_COLOUT2\_PD5](#a0572022128c37c99d4a96b712dabbc27)   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x3, 0x5) |
| #define | [KEYSCAN\_COLOUT3\_PA0](#a51c859388a817c10421d8f57aa4c3518)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x0) |
| #define | [KEYSCAN\_COLOUT3\_PA1](#a8d13e69bcdc4e1892ceaea8d42665b99)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x1) |
| #define | [KEYSCAN\_COLOUT3\_PA2](#ac1be0018ccc29a2708e72acb75d51158)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x2) |
| #define | [KEYSCAN\_COLOUT3\_PA3](#a01fe6c4c242f6c330434123fd734da83)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x3) |
| #define | [KEYSCAN\_COLOUT3\_PA4](#a6b6c8fdd388d9058a89a1ba983851ead)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x4) |
| #define | [KEYSCAN\_COLOUT3\_PA5](#af2b736e90ed10f923d78c00e7106c0dd)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x5) |
| #define | [KEYSCAN\_COLOUT3\_PA6](#aa3d560b392fd6808579f02e8e4fa593d)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x6) |
| #define | [KEYSCAN\_COLOUT3\_PA7](#abf1f603bcf07b715ec3592b9898eaaaf)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x7) |
| #define | [KEYSCAN\_COLOUT3\_PA8](#a231728ec3f628502a13009e5b22fa60f)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x8) |
| #define | [KEYSCAN\_COLOUT3\_PA9](#a2be978ee87b3ecaf4f05cc90c01f9a65)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x9) |
| #define | [KEYSCAN\_COLOUT3\_PB0](#a7b60f0f663b3e15a1647be43970b33d9)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x1, 0x0) |
| #define | [KEYSCAN\_COLOUT3\_PB1](#a3c3ddd9ed7588b19bcb67d20051b6907)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x1, 0x1) |
| #define | [KEYSCAN\_COLOUT3\_PB2](#a582697e0b5c3235325b8769ac5a6bae5)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x1, 0x2) |
| #define | [KEYSCAN\_COLOUT3\_PB3](#a67632e0b8e6a5097d57cab38e4ded747)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x1, 0x3) |
| #define | [KEYSCAN\_COLOUT3\_PB4](#aed301ef0f03969a3955c10413b7a7f45)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x1, 0x4) |
| #define | [KEYSCAN\_COLOUT3\_PB5](#a02bb5d3ad9c153987999579d174ea167)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x1, 0x5) |
| #define | [KEYSCAN\_COLOUT3\_PC0](#a14d9ca34a9975ae9ea2a2c13be3c90e3)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x0) |
| #define | [KEYSCAN\_COLOUT3\_PC1](#a8c0874eb69aa803c0ef1f2d047eccd2b)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x1) |
| #define | [KEYSCAN\_COLOUT3\_PC2](#ac17fc25a532f9d104e27080f31e892e8)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x2) |
| #define | [KEYSCAN\_COLOUT3\_PC3](#a7dccd1b112a71187973000077527a63d)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x3) |
| #define | [KEYSCAN\_COLOUT3\_PC4](#a3c97b3a952101dc9f34b72106d5a87a3)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x4) |
| #define | [KEYSCAN\_COLOUT3\_PC5](#a7d4670705a96667b595135bf7b69b27a)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x5) |
| #define | [KEYSCAN\_COLOUT3\_PC6](#ad0b6eeec83a80bd3eefc6ec9c795f211)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x6) |
| #define | [KEYSCAN\_COLOUT3\_PC7](#a07e11db7d66d0f47a800d437d1451c7b)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x7) |
| #define | [KEYSCAN\_COLOUT3\_PC8](#ac9e57d422d9d2b636a7482744894b43c)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x8) |
| #define | [KEYSCAN\_COLOUT3\_PC9](#ad0737dc2ebdc663e17e677574cb5ccec)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x9) |
| #define | [KEYSCAN\_COLOUT3\_PD0](#a88f98c3d74687422cf458864da9fb5a7)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x3, 0x0) |
| #define | [KEYSCAN\_COLOUT3\_PD1](#aae40661805acf791be1c66d3a2dfa63a)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x3, 0x1) |
| #define | [KEYSCAN\_COLOUT3\_PD2](#a26ebcb6f8957068bfeb1cbe8f3e82349)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x3, 0x2) |
| #define | [KEYSCAN\_COLOUT3\_PD3](#aa60f7d0f40d5be380e767430fda26b42)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x3, 0x3) |
| #define | [KEYSCAN\_COLOUT3\_PD4](#adc07cf653f0c8b39c809ec7cdf12589f)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x3, 0x4) |
| #define | [KEYSCAN\_COLOUT3\_PD5](#a336fd8f6980b4c439412327e29659665)   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x3, 0x5) |
| #define | [KEYSCAN\_COLOUT4\_PA0](#a78e1f197ada2e32957011566ac1a5aa3)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x0) |
| #define | [KEYSCAN\_COLOUT4\_PA1](#a515e07048d2b6beee5e58dd6e64cabc8)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x1) |
| #define | [KEYSCAN\_COLOUT4\_PA2](#a48b7ad094af7fec9cb41211e35ea24a8)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x2) |
| #define | [KEYSCAN\_COLOUT4\_PA3](#ae23d4333a8f2ea922dfec0fdc5274265)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x3) |
| #define | [KEYSCAN\_COLOUT4\_PA4](#a70de53b11ca989b53ec574f1d9b5a9a1)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x4) |
| #define | [KEYSCAN\_COLOUT4\_PA5](#abf320f9d9237887c80804d4cae80be1f)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x5) |
| #define | [KEYSCAN\_COLOUT4\_PA6](#a932ab9b651ef171d8770ee91f755f310)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x6) |
| #define | [KEYSCAN\_COLOUT4\_PA7](#ac78d413a4efb4d86e2a50e7b72be4d26)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x7) |
| #define | [KEYSCAN\_COLOUT4\_PA8](#af6b8b35c91aa7f7803bbcc5fb075727f)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x8) |
| #define | [KEYSCAN\_COLOUT4\_PA9](#a8f3aac47e0f1f915f1c5b23a4c27dd2f)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x9) |
| #define | [KEYSCAN\_COLOUT4\_PB0](#a11987f6b9850ca37854294dcb905dc7c)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x1, 0x0) |
| #define | [KEYSCAN\_COLOUT4\_PB1](#ae40bf07cf4c0df647eaae88e5be92524)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x1, 0x1) |
| #define | [KEYSCAN\_COLOUT4\_PB2](#a2676eb0f189c13d62f6f3a47ff91460f)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x1, 0x2) |
| #define | [KEYSCAN\_COLOUT4\_PB3](#a10623259e7aab23eed36d024ec2db492)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x1, 0x3) |
| #define | [KEYSCAN\_COLOUT4\_PB4](#a90de9bcd11d5e22753492defd2d466eb)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x1, 0x4) |
| #define | [KEYSCAN\_COLOUT4\_PB5](#a79fb2103fd195dc0acc79f4a781fcc35)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x1, 0x5) |
| #define | [KEYSCAN\_COLOUT4\_PC0](#a8e70447c091ba747df500037c1730443)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x0) |
| #define | [KEYSCAN\_COLOUT4\_PC1](#ad2b86c50f1170c709965981baccf6f8c)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x1) |
| #define | [KEYSCAN\_COLOUT4\_PC2](#a06ecfd3d8a4d8e790eba4b1e75893d5d)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x2) |
| #define | [KEYSCAN\_COLOUT4\_PC3](#a72427d0eead38a6b0546d0f2b120b719)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x3) |
| #define | [KEYSCAN\_COLOUT4\_PC4](#a2b41f30aafad5a904e4f9ac0224154c9)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x4) |
| #define | [KEYSCAN\_COLOUT4\_PC5](#ac0193ef4b3165a422579786f2bdd3d56)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x5) |
| #define | [KEYSCAN\_COLOUT4\_PC6](#a0516f93e064fe7240ea8acad8181dfab)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x6) |
| #define | [KEYSCAN\_COLOUT4\_PC7](#a48854348d92e762a887528e2dad40ea3)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x7) |
| #define | [KEYSCAN\_COLOUT4\_PC8](#a7fea996f4cb54dc4aa532ebc826f93c2)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x8) |
| #define | [KEYSCAN\_COLOUT4\_PC9](#a6fb8ab1beade87394c928d16c7c82d74)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x9) |
| #define | [KEYSCAN\_COLOUT4\_PD0](#a11dbe6c22a64853ebf77d63a39559686)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x3, 0x0) |
| #define | [KEYSCAN\_COLOUT4\_PD1](#ac404c0c86e9854cd160c23f7fd5064c9)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x3, 0x1) |
| #define | [KEYSCAN\_COLOUT4\_PD2](#afabf35d508aa714ebbb349504b8eda37)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x3, 0x2) |
| #define | [KEYSCAN\_COLOUT4\_PD3](#a18755054cce4073be50b10dd0ca6eb21)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x3, 0x3) |
| #define | [KEYSCAN\_COLOUT4\_PD4](#ac5e1a649a0ae05c780de197299fbb7dd)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x3, 0x4) |
| #define | [KEYSCAN\_COLOUT4\_PD5](#ae6a0a3db5f80b4b0cac57444f163a585)   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x3, 0x5) |
| #define | [KEYSCAN\_COLOUT5\_PA0](#a445da127fb2362507a565aed11eeeba0)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x0) |
| #define | [KEYSCAN\_COLOUT5\_PA1](#a3bc9a083d15fef5d3d79cda126d08906)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x1) |
| #define | [KEYSCAN\_COLOUT5\_PA2](#a6811845fa1e873338d55c312688bab86)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x2) |
| #define | [KEYSCAN\_COLOUT5\_PA3](#a6d6e8462f2dded71fd2beda3d8a4dde3)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x3) |
| #define | [KEYSCAN\_COLOUT5\_PA4](#a5b28158eeda0bc1d96457e7894a5ffdc)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x4) |
| #define | [KEYSCAN\_COLOUT5\_PA5](#a249cadf259b05e1504108c51dc17c25a)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x5) |
| #define | [KEYSCAN\_COLOUT5\_PA6](#a7514bf4b2ef744b83d1ed2722fabf94e)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x6) |
| #define | [KEYSCAN\_COLOUT5\_PA7](#aa2290f8cad94843957d0931d71eb6ce1)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x7) |
| #define | [KEYSCAN\_COLOUT5\_PA8](#a9b17f8d47d3a9eb28c822f1b6a776435)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x8) |
| #define | [KEYSCAN\_COLOUT5\_PA9](#a868d0142dd4a0c150b2274abf7aa6ff0)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x9) |
| #define | [KEYSCAN\_COLOUT5\_PB0](#a66892269bf6807fee61920130c800600)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x1, 0x0) |
| #define | [KEYSCAN\_COLOUT5\_PB1](#a4d733004f15bf6d3ff23ec47bd9768ad)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x1, 0x1) |
| #define | [KEYSCAN\_COLOUT5\_PB2](#a2003238f3634bcd0f67592d60d7fcaef)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x1, 0x2) |
| #define | [KEYSCAN\_COLOUT5\_PB3](#a4b05943cd8dc5b50c74393a9fb044461)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x1, 0x3) |
| #define | [KEYSCAN\_COLOUT5\_PB4](#aaef1601c48afde7ae05971f482b5c7c1)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x1, 0x4) |
| #define | [KEYSCAN\_COLOUT5\_PB5](#aed0250bb5950ddd89f943fa8e80389ee)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x1, 0x5) |
| #define | [KEYSCAN\_COLOUT5\_PC0](#acfac4f2b95912c513b1b284c31a0b0f6)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x0) |
| #define | [KEYSCAN\_COLOUT5\_PC1](#ae70fbb4c97527a55a721e88de8b980fb)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x1) |
| #define | [KEYSCAN\_COLOUT5\_PC2](#a1c779495a8b3cfc1ddf6061be7291e79)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x2) |
| #define | [KEYSCAN\_COLOUT5\_PC3](#a33988f610eb6e5c070f902b7b873da51)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x3) |
| #define | [KEYSCAN\_COLOUT5\_PC4](#abde9e625846e6e01c1757da031fcf714)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x4) |
| #define | [KEYSCAN\_COLOUT5\_PC5](#a8947e96addd21760d8231582af772151)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x5) |
| #define | [KEYSCAN\_COLOUT5\_PC6](#abd7fb9e69d19fb382fed755eee87ffda)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x6) |
| #define | [KEYSCAN\_COLOUT5\_PC7](#a5e82bc559b41f162f3919d791981e66e)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x7) |
| #define | [KEYSCAN\_COLOUT5\_PC8](#a6e14479a3cbb0e5b423b9db48d231d2d)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x8) |
| #define | [KEYSCAN\_COLOUT5\_PC9](#a6a73c599f9728431a35756c4986654f5)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x9) |
| #define | [KEYSCAN\_COLOUT5\_PD0](#a34b02d2d2ffe5c3048f473115713515d)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x3, 0x0) |
| #define | [KEYSCAN\_COLOUT5\_PD1](#a5199171ce63cf8ca7675772b2321fad3)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x3, 0x1) |
| #define | [KEYSCAN\_COLOUT5\_PD2](#a540317a1bb80f621e72a08cd85fe41d0)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x3, 0x2) |
| #define | [KEYSCAN\_COLOUT5\_PD3](#a77d7ba8e76bdc6d526ca3f69717ce51a)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x3, 0x3) |
| #define | [KEYSCAN\_COLOUT5\_PD4](#a8ba90046cd580e02a7c13baa8266fe22)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x3, 0x4) |
| #define | [KEYSCAN\_COLOUT5\_PD5](#a877555ebc2ee02d897d9e1fb31b1956e)   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x3, 0x5) |
| #define | [KEYSCAN\_COLOUT6\_PA0](#a1015bc110150ce9a8dfde554c231ac94)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x0) |
| #define | [KEYSCAN\_COLOUT6\_PA1](#a164d2c40932914047b57116fb6fd5a03)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x1) |
| #define | [KEYSCAN\_COLOUT6\_PA2](#a3377f0ae72a775e8703f49ff9a3cffe9)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x2) |
| #define | [KEYSCAN\_COLOUT6\_PA3](#a9728b9714b9f6f6c457dd8cc7336ebed)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x3) |
| #define | [KEYSCAN\_COLOUT6\_PA4](#ab1205ba33526d8fdd22c90965c200ab2)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x4) |
| #define | [KEYSCAN\_COLOUT6\_PA5](#ae982f5aaa9101ac5615a4561b8270658)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x5) |
| #define | [KEYSCAN\_COLOUT6\_PA6](#adfe14ef51e16649cff7d9a364d33d54e)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x6) |
| #define | [KEYSCAN\_COLOUT6\_PA7](#a40a7388734dc2397993054adf8eb43f1)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x7) |
| #define | [KEYSCAN\_COLOUT6\_PA8](#ad246eb368b6e2db727ce989204da7eb0)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x8) |
| #define | [KEYSCAN\_COLOUT6\_PA9](#a002826f7446b3b832ba04c7adf8a937a)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x9) |
| #define | [KEYSCAN\_COLOUT6\_PB0](#a976bec944ecaf0cfade1d67ddd176ee0)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x1, 0x0) |
| #define | [KEYSCAN\_COLOUT6\_PB1](#ad18b480857c0b6e51cdc700e4886fce5)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x1, 0x1) |
| #define | [KEYSCAN\_COLOUT6\_PB2](#ada236816df191c833373e4360763a768)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x1, 0x2) |
| #define | [KEYSCAN\_COLOUT6\_PB3](#ae61862815dad0d58bdfbdadaec43852d)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x1, 0x3) |
| #define | [KEYSCAN\_COLOUT6\_PB4](#a8136ee96abebd75e9ae9c182ddfc1d69)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x1, 0x4) |
| #define | [KEYSCAN\_COLOUT6\_PB5](#ab519393460d3afee34c2c296ecdaa728)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x1, 0x5) |
| #define | [KEYSCAN\_COLOUT6\_PC0](#a6ca408b5dbea309195594e1eaabd7a39)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x0) |
| #define | [KEYSCAN\_COLOUT6\_PC1](#ab8d2c741cf89baa479ffd00b02f95b1e)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x1) |
| #define | [KEYSCAN\_COLOUT6\_PC2](#af74ca2782fbc8ace8ac7ab3df032333f)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x2) |
| #define | [KEYSCAN\_COLOUT6\_PC3](#ae664ac159cd0225a2940c9bef2a8fd48)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x3) |
| #define | [KEYSCAN\_COLOUT6\_PC4](#a5ac714fbdb09307163c0bf5b8618e48e)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x4) |
| #define | [KEYSCAN\_COLOUT6\_PC5](#a804aff870bf653bd128578352a599fe7)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x5) |
| #define | [KEYSCAN\_COLOUT6\_PC6](#a1321d5994882b85ac825fcbe36ce0f17)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x6) |
| #define | [KEYSCAN\_COLOUT6\_PC7](#a6e2015159c39cb1646318d8d63fd071c)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x7) |
| #define | [KEYSCAN\_COLOUT6\_PC8](#a8f6dd892722632a45e052dd51c2fa6f3)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x8) |
| #define | [KEYSCAN\_COLOUT6\_PC9](#a45bfc62ed3b18cb0f85fc4cadab6281a)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x9) |
| #define | [KEYSCAN\_COLOUT6\_PD0](#ad7e7da0911664b6a29c17af882647fdf)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x3, 0x0) |
| #define | [KEYSCAN\_COLOUT6\_PD1](#ac205720916fc5f4466f6bf94d7df9ff4)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x3, 0x1) |
| #define | [KEYSCAN\_COLOUT6\_PD2](#a1f90116aed6f2bbb6d49c7683acd525c)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x3, 0x2) |
| #define | [KEYSCAN\_COLOUT6\_PD3](#a76381728fb3c51794708f0235d6726dd)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x3, 0x3) |
| #define | [KEYSCAN\_COLOUT6\_PD4](#a86c12dd4b7435a5151cf598369356229)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x3, 0x4) |
| #define | [KEYSCAN\_COLOUT6\_PD5](#a69d7a1f11082904af7c6a94e309d30cc)   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x3, 0x5) |
| #define | [KEYSCAN\_COLOUT7\_PA0](#a2c2077051cec44334ca9f24f01d9c30f)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x0) |
| #define | [KEYSCAN\_COLOUT7\_PA1](#a738421f5a4f4b1eb477303acdcebd14c)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x1) |
| #define | [KEYSCAN\_COLOUT7\_PA2](#aebf2a80a6a5dde233b36a8fb8d579911)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x2) |
| #define | [KEYSCAN\_COLOUT7\_PA3](#a466d3fc5a3bc404fbfa550e019cc62d7)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x3) |
| #define | [KEYSCAN\_COLOUT7\_PA4](#a39df7281dab8a01ef199f28f832e6e87)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x4) |
| #define | [KEYSCAN\_COLOUT7\_PA5](#a3379e32f32ca7e4690965d6cf5246584)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x5) |
| #define | [KEYSCAN\_COLOUT7\_PA6](#a762c113dc69ca9a54c06951b0afec2ad)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x6) |
| #define | [KEYSCAN\_COLOUT7\_PA7](#a4dce38f25f57d77f353b825a347218d7)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x7) |
| #define | [KEYSCAN\_COLOUT7\_PA8](#a5d0ebe96584d8a404c919b0384048712)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x8) |
| #define | [KEYSCAN\_COLOUT7\_PA9](#a2cd7ce9bec05887045f6fb332eceb01f)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x9) |
| #define | [KEYSCAN\_COLOUT7\_PB0](#a3a9ac7724de26dc7d7863a9c464f3b8e)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x1, 0x0) |
| #define | [KEYSCAN\_COLOUT7\_PB1](#a34f6c1e9f8a112dd4dffc5a4bcd62923)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x1, 0x1) |
| #define | [KEYSCAN\_COLOUT7\_PB2](#ab0e561a2c2df7cd8aac7bfb9cc28ebe5)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x1, 0x2) |
| #define | [KEYSCAN\_COLOUT7\_PB3](#a82e0512ef6c164040dce7118125a0b44)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x1, 0x3) |
| #define | [KEYSCAN\_COLOUT7\_PB4](#a06a9141b57439ef6a5050d49198722c3)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x1, 0x4) |
| #define | [KEYSCAN\_COLOUT7\_PB5](#a3950d363f113758c76bfd2043c811733)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x1, 0x5) |
| #define | [KEYSCAN\_COLOUT7\_PC0](#a1b765b491b755de95da126789fdcc5c3)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x0) |
| #define | [KEYSCAN\_COLOUT7\_PC1](#aadbb6155733bed3501712a35f90cb044)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x1) |
| #define | [KEYSCAN\_COLOUT7\_PC2](#a1dbb118c9b76a300bb722db3b68d6b84)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x2) |
| #define | [KEYSCAN\_COLOUT7\_PC3](#aa91a9034fde73e0704eff4b4ea087f5f)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x3) |
| #define | [KEYSCAN\_COLOUT7\_PC4](#ab2f6a222ecb44740a2bc5d0c9910df35)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x4) |
| #define | [KEYSCAN\_COLOUT7\_PC5](#a1a0cb3350162aab843868bf8acb27f57)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x5) |
| #define | [KEYSCAN\_COLOUT7\_PC6](#a4e05623227d433e89b2d21a2de694447)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x6) |
| #define | [KEYSCAN\_COLOUT7\_PC7](#a3bc3ec5f42c0c02b4fe33409a951ae00)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x7) |
| #define | [KEYSCAN\_COLOUT7\_PC8](#a7a40074edaaa3b77e7a4bc7af3631e4c)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x8) |
| #define | [KEYSCAN\_COLOUT7\_PC9](#af8874c8534bb7195961524edd4a9ec58)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x9) |
| #define | [KEYSCAN\_COLOUT7\_PD0](#a5d9b11b5cc466f175592dbde1721f769)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x3, 0x0) |
| #define | [KEYSCAN\_COLOUT7\_PD1](#a250d43085e7ae24a1b142db5d4baf918)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x3, 0x1) |
| #define | [KEYSCAN\_COLOUT7\_PD2](#adc18708ffe2821fa512de99ea16713af)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x3, 0x2) |
| #define | [KEYSCAN\_COLOUT7\_PD3](#a0e75e731910d6a5e80f9ff1be66f729d)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x3, 0x3) |
| #define | [KEYSCAN\_COLOUT7\_PD4](#a440d923db1ccbb88b729d6f903cf6f06)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x3, 0x4) |
| #define | [KEYSCAN\_COLOUT7\_PD5](#a829fcc9a471a8b860f6b572b43aad369)   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x3, 0x5) |
| #define | [KEYSCAN\_ROWSENSE0\_PA0](#a67991dff6fcb794562cc961b7be4ab19)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x0) |
| #define | [KEYSCAN\_ROWSENSE0\_PA1](#a339a54f1955567a0bce2aebee0b943a9)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x1) |
| #define | [KEYSCAN\_ROWSENSE0\_PA2](#a4fdc77d680dfc73289c4ad497ce067f7)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x2) |
| #define | [KEYSCAN\_ROWSENSE0\_PA3](#ad1e2f6e6b2507f0e3c047ab5384ee6cd)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x3) |
| #define | [KEYSCAN\_ROWSENSE0\_PA4](#a31b40c144d14649874a70e1198077cb9)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x4) |
| #define | [KEYSCAN\_ROWSENSE0\_PA5](#a42919482bfc6aca98335cd5ca5133bcf)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x5) |
| #define | [KEYSCAN\_ROWSENSE0\_PA6](#a91c93b98d8018df61c6e31d7c4fde9d2)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x6) |
| #define | [KEYSCAN\_ROWSENSE0\_PA7](#a25157ca32ecace6d08fbcb09b0d8e13f)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x7) |
| #define | [KEYSCAN\_ROWSENSE0\_PA8](#ad01b8f98c3228b100d9806d01d3a72f7)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x8) |
| #define | [KEYSCAN\_ROWSENSE0\_PA9](#a0f52c8016ffe4bc9d849c241f7b49eba)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x9) |
| #define | [KEYSCAN\_ROWSENSE0\_PB0](#afabf7d00424badf10c342d4f4eb56f9f)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x1, 0x0) |
| #define | [KEYSCAN\_ROWSENSE0\_PB1](#abde18a3ba51a69a81c268075ad8eb0fc)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x1, 0x1) |
| #define | [KEYSCAN\_ROWSENSE0\_PB2](#a24f463069c92d9fae0b58beb2ad5fc35)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x1, 0x2) |
| #define | [KEYSCAN\_ROWSENSE0\_PB3](#ad1b979a16fcf92f08f6aa0836be8f040)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x1, 0x3) |
| #define | [KEYSCAN\_ROWSENSE0\_PB4](#a2f5b585a89277c6571be738f8aa3f034)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x1, 0x4) |
| #define | [KEYSCAN\_ROWSENSE0\_PB5](#a1af0700d0fe6e65566675861682919a2)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x1, 0x5) |
| #define | [KEYSCAN\_ROWSENSE1\_PA0](#a2b99dc18c2ea2ca460ac90aed73caba5)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x0) |
| #define | [KEYSCAN\_ROWSENSE1\_PA1](#ab043e248ed5d80ec70ee62fbabd53447)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x1) |
| #define | [KEYSCAN\_ROWSENSE1\_PA2](#a4cbe09e947c26123a341e9402706a1cb)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x2) |
| #define | [KEYSCAN\_ROWSENSE1\_PA3](#a62bdd05aae2bca8be772fec9864e6b68)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x3) |
| #define | [KEYSCAN\_ROWSENSE1\_PA4](#afd4f5e56d0b5e6dc7f134407181e65a8)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x4) |
| #define | [KEYSCAN\_ROWSENSE1\_PA5](#a8eafb57db7cd8eb914ddd261082a557d)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x5) |
| #define | [KEYSCAN\_ROWSENSE1\_PA6](#a547b11aec9663d60bc655e73f0e36a23)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x6) |
| #define | [KEYSCAN\_ROWSENSE1\_PA7](#ae32c46f38591fd583715cdb966917afd)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x7) |
| #define | [KEYSCAN\_ROWSENSE1\_PA8](#a81633497cd9ea043c2d0edf1433e1f8a)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x8) |
| #define | [KEYSCAN\_ROWSENSE1\_PA9](#a77b62ab5186da780fbcc04b6493275ee)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x9) |
| #define | [KEYSCAN\_ROWSENSE1\_PB0](#a91714fa64b28935dfc304a9c96ee6463)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x1, 0x0) |
| #define | [KEYSCAN\_ROWSENSE1\_PB1](#a19666eb8fad7afe29304d989d27d7900)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x1, 0x1) |
| #define | [KEYSCAN\_ROWSENSE1\_PB2](#a3e98b13c576d22efd869ed96b980d2fc)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x1, 0x2) |
| #define | [KEYSCAN\_ROWSENSE1\_PB3](#a8d8ef254fe361607f0f03213242cc935)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x1, 0x3) |
| #define | [KEYSCAN\_ROWSENSE1\_PB4](#a1d20159431da0732584309cca0c3bb21)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x1, 0x4) |
| #define | [KEYSCAN\_ROWSENSE1\_PB5](#ae117dc227927f05c57fcf3cb4e36e135)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x1, 0x5) |
| #define | [KEYSCAN\_ROWSENSE2\_PA0](#a81797c1a41b453e99c904d13abc1dfaa)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x0) |
| #define | [KEYSCAN\_ROWSENSE2\_PA1](#a827162fd46a929d469e58991add10d87)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x1) |
| #define | [KEYSCAN\_ROWSENSE2\_PA2](#ada62ed625f76f6f4ba7ef03aeed09afc)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x2) |
| #define | [KEYSCAN\_ROWSENSE2\_PA3](#a5a4144e1842c452a99d055c62d56df64)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x3) |
| #define | [KEYSCAN\_ROWSENSE2\_PA4](#a648c8d982b6e31a74bb4018f38cdd4a0)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x4) |
| #define | [KEYSCAN\_ROWSENSE2\_PA5](#ada178e730cde0696ebeda57915abfe69)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x5) |
| #define | [KEYSCAN\_ROWSENSE2\_PA6](#a6449748c9123fdc703993d98149bb127)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x6) |
| #define | [KEYSCAN\_ROWSENSE2\_PA7](#ab091b88a0fe636a1f1be4fbf3877083a)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x7) |
| #define | [KEYSCAN\_ROWSENSE2\_PA8](#a591262d395412f79aca0ca3c33bb71a6)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x8) |
| #define | [KEYSCAN\_ROWSENSE2\_PA9](#a0000c7bde424893f75fa88a2fa46618c)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x9) |
| #define | [KEYSCAN\_ROWSENSE2\_PB0](#ac324e44a5781c26c7b5b8295639bddb3)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x1, 0x0) |
| #define | [KEYSCAN\_ROWSENSE2\_PB1](#a5bcc10bfaf92f92fbf63343979758be8)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x1, 0x1) |
| #define | [KEYSCAN\_ROWSENSE2\_PB2](#a565524f72fc269654c3f21ad55d22984)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x1, 0x2) |
| #define | [KEYSCAN\_ROWSENSE2\_PB3](#aa87f2b0f63628e540d7cab6819f23b1c)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x1, 0x3) |
| #define | [KEYSCAN\_ROWSENSE2\_PB4](#a126fbb54622a6f9145314e37ac40faf0)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x1, 0x4) |
| #define | [KEYSCAN\_ROWSENSE2\_PB5](#a2b0719a6d0116cca241bdcfc55865b6f)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x1, 0x5) |
| #define | [KEYSCAN\_ROWSENSE3\_PA0](#aea8e269e57c0462a3ef0dced0ad01379)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x0) |
| #define | [KEYSCAN\_ROWSENSE3\_PA1](#a1a1e4fba3105aaccdd5eb39b6cb676ca)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x1) |
| #define | [KEYSCAN\_ROWSENSE3\_PA2](#a4ce45d5aa7155da9b41dfc1aa1cd8bb3)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x2) |
| #define | [KEYSCAN\_ROWSENSE3\_PA3](#a2eb6f87d5342f841258d59b95b1d7549)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x3) |
| #define | [KEYSCAN\_ROWSENSE3\_PA4](#a52730c327d1243f617e65778fe6a1cb5)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x4) |
| #define | [KEYSCAN\_ROWSENSE3\_PA5](#a620eb41deb110f6f7e20ff5800fb1b98)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x5) |
| #define | [KEYSCAN\_ROWSENSE3\_PA6](#a3d03dfd87e53036d8ed9b3cedf9557d1)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x6) |
| #define | [KEYSCAN\_ROWSENSE3\_PA7](#a5d9a8c0a94a153e54ce5e9f558d4f1d4)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x7) |
| #define | [KEYSCAN\_ROWSENSE3\_PA8](#adc003516a88f3beac0f3246f120f7464)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x8) |
| #define | [KEYSCAN\_ROWSENSE3\_PA9](#a128c9d56c6915c58014726204d4b71ad)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x9) |
| #define | [KEYSCAN\_ROWSENSE3\_PB0](#a57e4c4b0f2458f74874c4c09f5c4be11)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x1, 0x0) |
| #define | [KEYSCAN\_ROWSENSE3\_PB1](#ad72c30d85b22ed6a11214b3fd4d93fb4)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x1, 0x1) |
| #define | [KEYSCAN\_ROWSENSE3\_PB2](#a546c198566ccf3c91b2fc8aa64fb2443)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x1, 0x2) |
| #define | [KEYSCAN\_ROWSENSE3\_PB3](#acdeb49a1b6cd15f10bf5b52a87b45d01)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x1, 0x3) |
| #define | [KEYSCAN\_ROWSENSE3\_PB4](#a002ab804bc35bd15b6a5faa302de29e3)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x1, 0x4) |
| #define | [KEYSCAN\_ROWSENSE3\_PB5](#a81503561bb605822d16aadb1c6aae53d)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x1, 0x5) |
| #define | [KEYSCAN\_ROWSENSE4\_PA0](#a148727ae1c844e126c467e53628283e1)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x0) |
| #define | [KEYSCAN\_ROWSENSE4\_PA1](#aa9a5202d34d97778b6f24c28f4aab7ec)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x1) |
| #define | [KEYSCAN\_ROWSENSE4\_PA2](#a4eebe03193902292d76f2e2181b69c26)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x2) |
| #define | [KEYSCAN\_ROWSENSE4\_PA3](#a8ef724c7e7dd3c6c0e97b9bc656a0da7)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x3) |
| #define | [KEYSCAN\_ROWSENSE4\_PA4](#ae460ceb2d0dea8dfb06a38370a837dcd)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x4) |
| #define | [KEYSCAN\_ROWSENSE4\_PA5](#a44f7c4f24a64683e3e6f00d040deec14)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x5) |
| #define | [KEYSCAN\_ROWSENSE4\_PA6](#a01c3835cf1c841b4caa81a7c6f62226d)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x6) |
| #define | [KEYSCAN\_ROWSENSE4\_PA7](#a29edbb560fa201628e43798bb20d281d)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x7) |
| #define | [KEYSCAN\_ROWSENSE4\_PA8](#a83bd1d1ca180035fa2348b0a8c577b49)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x8) |
| #define | [KEYSCAN\_ROWSENSE4\_PA9](#ae92e0a4be0d7515915900a552d57b742)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x9) |
| #define | [KEYSCAN\_ROWSENSE4\_PB0](#a7af7b960d806a3e6304a2f2c04aef647)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x1, 0x0) |
| #define | [KEYSCAN\_ROWSENSE4\_PB1](#ae62e1398b6d59687257fbfaddd65f6a5)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x1, 0x1) |
| #define | [KEYSCAN\_ROWSENSE4\_PB2](#a29e968ac626b5fcc8b08e5d9e2f15fc0)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x1, 0x2) |
| #define | [KEYSCAN\_ROWSENSE4\_PB3](#a822bb66e2dc40a181126aa9938a7c833)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x1, 0x3) |
| #define | [KEYSCAN\_ROWSENSE4\_PB4](#a7eb3f3fcc2993908e32cb4fa2250b19d)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x1, 0x4) |
| #define | [KEYSCAN\_ROWSENSE4\_PB5](#a13bb5c17c76d1cb758653bdb130ff90b)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x1, 0x5) |
| #define | [KEYSCAN\_ROWSENSE5\_PA0](#a1b62e75eac6ac228f9dab9defde9a2e1)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x0) |
| #define | [KEYSCAN\_ROWSENSE5\_PA1](#a9a4a7e80809a3f35d04c2276f8b220b9)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x1) |
| #define | [KEYSCAN\_ROWSENSE5\_PA2](#af6297695161b54edbb9b158df3a3b59e)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x2) |
| #define | [KEYSCAN\_ROWSENSE5\_PA3](#a087a37402663309e5c81c1bda63aed00)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x3) |
| #define | [KEYSCAN\_ROWSENSE5\_PA4](#ab3074863aa5f863f53f5c2fce912f223)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x4) |
| #define | [KEYSCAN\_ROWSENSE5\_PA5](#a9247d882fae3024aa8e5ff4d1b14eae5)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x5) |
| #define | [KEYSCAN\_ROWSENSE5\_PA6](#a3e52fe29e22f22e95c97c0e080a764e2)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x6) |
| #define | [KEYSCAN\_ROWSENSE5\_PA7](#a0c8953bd67945bf491a512f02e3773ee)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x7) |
| #define | [KEYSCAN\_ROWSENSE5\_PA8](#a9bd8611e430026502d208a037877360d)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x8) |
| #define | [KEYSCAN\_ROWSENSE5\_PA9](#af333321891e6259db4896ccaeb616146)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x9) |
| #define | [KEYSCAN\_ROWSENSE5\_PB0](#a8e97a56858b8ddb95242a63579ff3ba3)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x1, 0x0) |
| #define | [KEYSCAN\_ROWSENSE5\_PB1](#a1b99dd7c60b9e211119cf81221ea1265)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x1, 0x1) |
| #define | [KEYSCAN\_ROWSENSE5\_PB2](#a3498d5610cd6afae4e9a15fae40cbbbb)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x1, 0x2) |
| #define | [KEYSCAN\_ROWSENSE5\_PB3](#ad53595710be18bf6403c093dbd1a89aa)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x1, 0x3) |
| #define | [KEYSCAN\_ROWSENSE5\_PB4](#ab074a6202bdc5102875597faf3cf85c3)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x1, 0x4) |
| #define | [KEYSCAN\_ROWSENSE5\_PB5](#a670967a9f35b7a1822fc6e4e9706facd)   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x1, 0x5) |
| #define | [LETIMER0\_OUT0\_PA0](#a352e584caede1a83b786463abf8e8ffc)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x0) |
| #define | [LETIMER0\_OUT0\_PA1](#a237d004885f30f207a78f3fce4380476)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x1) |
| #define | [LETIMER0\_OUT0\_PA2](#a25d0f59297bd6c10acc7714b06af99ca)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x2) |
| #define | [LETIMER0\_OUT0\_PA3](#a9120e73b07bfa093065ec040045eb61d)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x3) |
| #define | [LETIMER0\_OUT0\_PA4](#a4f0e8db2242fed71b78c6b0679a6ff76)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x4) |
| #define | [LETIMER0\_OUT0\_PA5](#a26a82422ca3e7fbd558caa46b4c6705d)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x5) |
| #define | [LETIMER0\_OUT0\_PA6](#a808e50c2f7823f703795dfbe5d5ef50e)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x6) |
| #define | [LETIMER0\_OUT0\_PA7](#a0f5833c4d88f979f1cdd7a1375a8074b)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x7) |
| #define | [LETIMER0\_OUT0\_PA8](#a0cf57fda500379c7e91c98a05d1e17ec)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x8) |
| #define | [LETIMER0\_OUT0\_PA9](#a185efdff17a0d5f18467184004071f92)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x9) |
| #define | [LETIMER0\_OUT0\_PB0](#ad81eda4d47fbc7265b325b09eb47232c)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x1, 0x0) |
| #define | [LETIMER0\_OUT0\_PB1](#a20d0230e58f46869e37b9acfe0e5fb0d)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x1, 0x1) |
| #define | [LETIMER0\_OUT0\_PB2](#a79820d41c14965a475c0f58982670e34)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x1, 0x2) |
| #define | [LETIMER0\_OUT0\_PB3](#a31d042f62545423b84bb0de3be30bdcb)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x1, 0x3) |
| #define | [LETIMER0\_OUT0\_PB4](#a433315136fec0480d99d198e5241915a)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x1, 0x4) |
| #define | [LETIMER0\_OUT0\_PB5](#ad6ea95686ae38777db2ef238079227e2)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x1, 0x5) |
| #define | [LETIMER0\_OUT1\_PA0](#a3cab629b6e9cd573b30f8e45a747e819)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x0) |
| #define | [LETIMER0\_OUT1\_PA1](#a2e90dd7d7686acf9665182356fba429d)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x1) |
| #define | [LETIMER0\_OUT1\_PA2](#a1ded3647217b200c7d49bf6f99df8800)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x2) |
| #define | [LETIMER0\_OUT1\_PA3](#ab329e7913b209f11eaba0a2623358976)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x3) |
| #define | [LETIMER0\_OUT1\_PA4](#a0e0dc57036750466e500d46d9f2f8674)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x4) |
| #define | [LETIMER0\_OUT1\_PA5](#a2c211216042c0ab444cf3e1b54d4e2f7)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x5) |
| #define | [LETIMER0\_OUT1\_PA6](#a0aebcc5748062062d09dec35c4baa61f)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x6) |
| #define | [LETIMER0\_OUT1\_PA7](#aabd4bbcd01e67aa31a1a06b6bbe16edc)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x7) |
| #define | [LETIMER0\_OUT1\_PA8](#af89df3c0b1d281356ed2316c88ceaa46)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x8) |
| #define | [LETIMER0\_OUT1\_PA9](#a9bb0b8b5cd8b3d7bff98ac70a6350074)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x9) |
| #define | [LETIMER0\_OUT1\_PB0](#a5501b8d6e668ef58a71e19bfe0d620b8)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x1, 0x0) |
| #define | [LETIMER0\_OUT1\_PB1](#a8e4b46c768114f20ee1002820ee4d583)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x1, 0x1) |
| #define | [LETIMER0\_OUT1\_PB2](#aa1a23a819291f5ab445f4d3db17c78b6)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x1, 0x2) |
| #define | [LETIMER0\_OUT1\_PB3](#a87c4b33f802fa34191489db40f674684)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x1, 0x3) |
| #define | [LETIMER0\_OUT1\_PB4](#a0f9c9dcc043629fd8a8bfebf710f3e10)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x1, 0x4) |
| #define | [LETIMER0\_OUT1\_PB5](#ab40a825d337cec70f62dc987d468216c)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x1, 0x5) |
| #define | [MODEM\_ANT0\_PA0](#a7f276456c2949e4151a1b2a734f8885c)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x0) |
| #define | [MODEM\_ANT0\_PA1](#a79c6f7c43dfc9adab0c8eeb974842745)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x1) |
| #define | [MODEM\_ANT0\_PA2](#ae187f6726ed20849cb327fbdddd44aca)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x2) |
| #define | [MODEM\_ANT0\_PA3](#a45bcc15c32caaa653434df7b01274283)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x3) |
| #define | [MODEM\_ANT0\_PA4](#a2378348e1cf6d527113895ad243cc58d)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x4) |
| #define | [MODEM\_ANT0\_PA5](#a722db9c869f2f89794bcc1ae32318ad4)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x5) |
| #define | [MODEM\_ANT0\_PA6](#a4bffa8d5ecfb474a91ff85afc315043a)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x6) |
| #define | [MODEM\_ANT0\_PA7](#a894653787f083faf2185f138b1a77551)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x7) |
| #define | [MODEM\_ANT0\_PA8](#a0ed9a2f3ae0b7b8edb0cfd28233a8489)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x8) |
| #define | [MODEM\_ANT0\_PA9](#abf541871de6c3a19d265e8ef4ce7a491)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x9) |
| #define | [MODEM\_ANT0\_PB0](#a509466c0511355374b0ee3ece106acd6)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x1, 0x0) |
| #define | [MODEM\_ANT0\_PB1](#a4c2864f003ccf1355fdbb2be9df0d2ec)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x1, 0x1) |
| #define | [MODEM\_ANT0\_PB2](#a63d38e8d680f24158d34a6bff19028b1)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x1, 0x2) |
| #define | [MODEM\_ANT0\_PB3](#addd2df0103ce62bea89bea865ad6294a)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x1, 0x3) |
| #define | [MODEM\_ANT0\_PB4](#a90d1b1b9472b551710f7ca062750d1c6)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x1, 0x4) |
| #define | [MODEM\_ANT0\_PB5](#ae149e31e9640504f96e24f71fbaeb978)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x1, 0x5) |
| #define | [MODEM\_ANT0\_PC0](#a6b06e4cb9c997d609b19d7fb7639bf8d)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x0) |
| #define | [MODEM\_ANT0\_PC1](#a000751139691af8d66623ad0bd43fc9b)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x1) |
| #define | [MODEM\_ANT0\_PC2](#afd5bc8540d8e3e5b0d182312520517be)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x2) |
| #define | [MODEM\_ANT0\_PC3](#a33b690ae2e28b1b08b691aa4742d84d7)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x3) |
| #define | [MODEM\_ANT0\_PC4](#ac22d54cd6c263a39f33caedf7cb09a0e)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x4) |
| #define | [MODEM\_ANT0\_PC5](#a6982c06cdd7b783257ed5f3a74c735c7)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x5) |
| #define | [MODEM\_ANT0\_PC6](#a8d28c8701b26924dd7038b6794a97a26)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x6) |
| #define | [MODEM\_ANT0\_PC7](#ad9e7f4a18a0eeedadedbefbf81c0449c)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x7) |
| #define | [MODEM\_ANT0\_PC8](#a72353908562e64f1f386cf48c9d6f8cc)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x8) |
| #define | [MODEM\_ANT0\_PC9](#ad18f643fc180d2fb50ee67bc02105fae)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x9) |
| #define | [MODEM\_ANT0\_PD0](#a01730221498f5de5590dbe8f6a293702)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x3, 0x0) |
| #define | [MODEM\_ANT0\_PD1](#a968474651d6fc8ced22a693a55d8bf4d)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x3, 0x1) |
| #define | [MODEM\_ANT0\_PD2](#a6bee8cd789f6922130830688cf586971)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x3, 0x2) |
| #define | [MODEM\_ANT0\_PD3](#aef59bb3ec42a534ffe32a53fb26e1656)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x3, 0x3) |
| #define | [MODEM\_ANT0\_PD4](#aba70f4135f5bcc3e10525c27f2f25021)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x3, 0x4) |
| #define | [MODEM\_ANT0\_PD5](#ae55b27dcb0ec6c1ad7ee2f3c877a7926)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x3, 0x5) |
| #define | [MODEM\_ANT1\_PA0](#a983f562f1f690bbec27d868c3d6b2b1a)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x0) |
| #define | [MODEM\_ANT1\_PA1](#a1c8d37c5145858068556a032983680d1)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x1) |
| #define | [MODEM\_ANT1\_PA2](#a9a879a4511af923143f8dc6e7710f0be)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x2) |
| #define | [MODEM\_ANT1\_PA3](#a5753d0d0ab943103f54d6ad9ea76bccf)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x3) |
| #define | [MODEM\_ANT1\_PA4](#a164fc42c8f2bc81bc70453af7bf82402)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x4) |
| #define | [MODEM\_ANT1\_PA5](#a790e4407942a7fb6fed5972b59bf12c9)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x5) |
| #define | [MODEM\_ANT1\_PA6](#a908cd5b571ab7ec4ba04581f3bf67166)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x6) |
| #define | [MODEM\_ANT1\_PA7](#a5c272c67918110b0cd323ed0228370bb)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x7) |
| #define | [MODEM\_ANT1\_PA8](#a1ab7e1ea92808eb14c818516aaa3295a)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x8) |
| #define | [MODEM\_ANT1\_PA9](#a013a26a517f5f339fc199affb5e7bb8d)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x9) |
| #define | [MODEM\_ANT1\_PB0](#adbe918778efba6fe712e7043457c43bb)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x1, 0x0) |
| #define | [MODEM\_ANT1\_PB1](#a6c5a484675c81a07f3709cb391113c22)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x1, 0x1) |
| #define | [MODEM\_ANT1\_PB2](#acbc03ad5136cb7715b10956805d851ad)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x1, 0x2) |
| #define | [MODEM\_ANT1\_PB3](#ac9db3cba6b213aba7b2e75913d7793b0)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x1, 0x3) |
| #define | [MODEM\_ANT1\_PB4](#a3772761615fb1f6b9427d09f40de1cb0)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x1, 0x4) |
| #define | [MODEM\_ANT1\_PB5](#a745f8f8c26db2c13b989a729f7b8da4b)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x1, 0x5) |
| #define | [MODEM\_ANT1\_PC0](#a5718fbbd7d66e6c775b8904b50b14aec)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x0) |
| #define | [MODEM\_ANT1\_PC1](#a25315b04583ee4d44f2e1835003679e9)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x1) |
| #define | [MODEM\_ANT1\_PC2](#a7480d21cbb697630fd83f494f671b030)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x2) |
| #define | [MODEM\_ANT1\_PC3](#aa6ba89e0d2c7347f10a1a18d461986db)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x3) |
| #define | [MODEM\_ANT1\_PC4](#a293042adb906716b25453e23c66932ee)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x4) |
| #define | [MODEM\_ANT1\_PC5](#aa699042d4cec5024da6439e6fa629c5f)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x5) |
| #define | [MODEM\_ANT1\_PC6](#a6f4b41d3971310c038878142c59d1375)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x6) |
| #define | [MODEM\_ANT1\_PC7](#aa48104a69c4edacb22f41bd14e717640)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x7) |
| #define | [MODEM\_ANT1\_PC8](#a08a181d182cb8ac110791185e150ac93)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x8) |
| #define | [MODEM\_ANT1\_PC9](#ac90a33371364c2d3b43b6ecd20202992)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x9) |
| #define | [MODEM\_ANT1\_PD0](#a1ebb5a0437c033fa7d567000c0b8c383)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x3, 0x0) |
| #define | [MODEM\_ANT1\_PD1](#a1cc580714150e9383e280946b2863b31)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x3, 0x1) |
| #define | [MODEM\_ANT1\_PD2](#ac3322bcfcef6e6a680cf4611d0b363ef)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x3, 0x2) |
| #define | [MODEM\_ANT1\_PD3](#abfdb37fc77643dc2853d87009c2425d6)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x3, 0x3) |
| #define | [MODEM\_ANT1\_PD4](#abd04eb50b1a4d87042b59362e4b8758d)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x3, 0x4) |
| #define | [MODEM\_ANT1\_PD5](#aa37f9ee08275da5c7c423460324c6f00)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x3, 0x5) |
| #define | [MODEM\_ANTROLLOVER\_PC0](#ace2bae83851b3aab46a81ef1a6c636b4)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x0) |
| #define | [MODEM\_ANTROLLOVER\_PC1](#a85ff56d69539994de2a84edf12f8a2be)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x1) |
| #define | [MODEM\_ANTROLLOVER\_PC2](#ae6601ed4b1dc45fad0deb09610797610)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x2) |
| #define | [MODEM\_ANTROLLOVER\_PC3](#a53fceeed6e44ab7bc81698d3c4c16207)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x3) |
| #define | [MODEM\_ANTROLLOVER\_PC4](#ac253adc5e51912ed5f4407447c81f473)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x4) |
| #define | [MODEM\_ANTROLLOVER\_PC5](#a60f405f65313e35ba59eca8fa208ed2c)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x5) |
| #define | [MODEM\_ANTROLLOVER\_PC6](#ad39de8c7dff7e3297e5beca22e2034f4)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x6) |
| #define | [MODEM\_ANTROLLOVER\_PC7](#a50b0007df6bc2de4b9200cbb1b79acf0)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x7) |
| #define | [MODEM\_ANTROLLOVER\_PC8](#acb5cec62092f3cb2a1dbe8cab74ade40)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x8) |
| #define | [MODEM\_ANTROLLOVER\_PC9](#a4d74f01cef772f0e097ff431b9b04542)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x9) |
| #define | [MODEM\_ANTROLLOVER\_PD0](#a88bb19ac23eb8bcc2868bf22bd4a12af)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x3, 0x0) |
| #define | [MODEM\_ANTROLLOVER\_PD1](#a92aeed47b01736dac03935ac699b9727)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x3, 0x1) |
| #define | [MODEM\_ANTROLLOVER\_PD2](#a603e14d84a8b13b7d4ee5bdab126cdae)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x3, 0x2) |
| #define | [MODEM\_ANTROLLOVER\_PD3](#a506855980f4dda9c5de58b11d76f7b4f)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x3, 0x3) |
| #define | [MODEM\_ANTROLLOVER\_PD4](#adfb16e607ee78520fc2579516f49a90b)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x3, 0x4) |
| #define | [MODEM\_ANTROLLOVER\_PD5](#a738a7352b0fdb0654efa643fab795675)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x3, 0x5) |
| #define | [MODEM\_ANTRR0\_PC0](#a72a1f767f29b37e2f0975efb930aabdc)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x0) |
| #define | [MODEM\_ANTRR0\_PC1](#a7465a3a4cf1cd92249001733145da7ed)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x1) |
| #define | [MODEM\_ANTRR0\_PC2](#a1b109adfe9e7699e7cb1a1fb46aa132c)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x2) |
| #define | [MODEM\_ANTRR0\_PC3](#a4109515cd008205b323edb06d2a19607)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x3) |
| #define | [MODEM\_ANTRR0\_PC4](#a56971ab62d7131e5aba024260d295153)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x4) |
| #define | [MODEM\_ANTRR0\_PC5](#a4de029d596f34060bde0d63982b171b3)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x5) |
| #define | [MODEM\_ANTRR0\_PC6](#a3a438458ac921a00c90a85d343ea1f90)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x6) |
| #define | [MODEM\_ANTRR0\_PC7](#a68f15a8b8a2acd73ff7b772aa529c0d9)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x7) |
| #define | [MODEM\_ANTRR0\_PC8](#af71e0d4d99fcf43095b57a0a8ba89629)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x8) |
| #define | [MODEM\_ANTRR0\_PC9](#a0cbcfb4610c61e741525b3cff7c6b988)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x9) |
| #define | [MODEM\_ANTRR0\_PD0](#a78f716f923dadb2a1df8eebc07c1a1ba)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x3, 0x0) |
| #define | [MODEM\_ANTRR0\_PD1](#ab46244ef8e98b0e13a0874b8831d1c9e)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x3, 0x1) |
| #define | [MODEM\_ANTRR0\_PD2](#ad652d37f429c634eaed147b962b1f81c)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x3, 0x2) |
| #define | [MODEM\_ANTRR0\_PD3](#a1cf6846a778c4a5820d42d1a8b9a6cef)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x3, 0x3) |
| #define | [MODEM\_ANTRR0\_PD4](#a084f75e9ebb22c162b28eff741c0997f)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x3, 0x4) |
| #define | [MODEM\_ANTRR0\_PD5](#aeba1b8f1af14062395a1cb161b46246b)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x3, 0x5) |
| #define | [MODEM\_ANTRR1\_PC0](#a5b77d7b22d3ba5fc6ccadceb8fd784e5)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x0) |
| #define | [MODEM\_ANTRR1\_PC1](#a79bc69a44835cf383b1de6037c8fae63)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x1) |
| #define | [MODEM\_ANTRR1\_PC2](#aa7cd2fde356a617651a7b518f9558709)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x2) |
| #define | [MODEM\_ANTRR1\_PC3](#ac12248a293d8a3c328df438370024a12)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x3) |
| #define | [MODEM\_ANTRR1\_PC4](#a6067448e7e46ae003e07b75ec4f22ddf)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x4) |
| #define | [MODEM\_ANTRR1\_PC5](#afb89ffed0de8306a2b3b2ff8a09db4eb)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x5) |
| #define | [MODEM\_ANTRR1\_PC6](#a2b02ddcbecd53f862993644a685928df)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x6) |
| #define | [MODEM\_ANTRR1\_PC7](#a5d14286b67618916e103c98ccaab6652)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x7) |
| #define | [MODEM\_ANTRR1\_PC8](#ad91019ee3e5cf685239a7de514d06b68)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x8) |
| #define | [MODEM\_ANTRR1\_PC9](#ae0ee67d5c53f010f3ee7194690a44c78)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x9) |
| #define | [MODEM\_ANTRR1\_PD0](#a3d4c45786676da1e67017a4cdb048449)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x3, 0x0) |
| #define | [MODEM\_ANTRR1\_PD1](#a74ac37ba6d806625dadd63c1af681a84)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x3, 0x1) |
| #define | [MODEM\_ANTRR1\_PD2](#a5c4e16526937500b8cc70a6b844ee832)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x3, 0x2) |
| #define | [MODEM\_ANTRR1\_PD3](#a79878ca6c07ea72a02c23a7321832b29)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x3, 0x3) |
| #define | [MODEM\_ANTRR1\_PD4](#a560cf5fe4d967d7577c63ecd4aaf7cfb)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x3, 0x4) |
| #define | [MODEM\_ANTRR1\_PD5](#a37fd0719bec33fe2c68d64ebd9697cf9)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x3, 0x5) |
| #define | [MODEM\_ANTRR2\_PC0](#a86532fa3d12fd905879905f4df67d954)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x0) |
| #define | [MODEM\_ANTRR2\_PC1](#a6e586c76b41f2ecf6384a6257390ee22)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x1) |
| #define | [MODEM\_ANTRR2\_PC2](#af57b2e22e3079c5825638bf1556d5f63)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x2) |
| #define | [MODEM\_ANTRR2\_PC3](#a43e57733d4b8bebe91750a3041245789)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x3) |
| #define | [MODEM\_ANTRR2\_PC4](#aa31ca6e6610920deaa06c77f7deaf40c)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x4) |
| #define | [MODEM\_ANTRR2\_PC5](#af3df188180c0609f2cb4c63f1ff77ff1)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x5) |
| #define | [MODEM\_ANTRR2\_PC6](#a69bb0899e1d7201561638d287612708c)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x6) |
| #define | [MODEM\_ANTRR2\_PC7](#a0696c2885355b5c7b13bef2e51d7188f)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x7) |
| #define | [MODEM\_ANTRR2\_PC8](#aa509860c7999d11e76d56b4dc7bbc6f6)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x8) |
| #define | [MODEM\_ANTRR2\_PC9](#acedaf796ecf36a0ec3d91b83a95ee1c0)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x9) |
| #define | [MODEM\_ANTRR2\_PD0](#a368c3325d067b5f5f93d67ad59cf04a9)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x3, 0x0) |
| #define | [MODEM\_ANTRR2\_PD1](#a019e9b59d7ebf97b06ea3deb84eb8a9d)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x3, 0x1) |
| #define | [MODEM\_ANTRR2\_PD2](#a591f45f9fa102e7e5ce0281003eb7ba9)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x3, 0x2) |
| #define | [MODEM\_ANTRR2\_PD3](#a341ce7ea3431fe6a6b04f88ba4cd4521)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x3, 0x3) |
| #define | [MODEM\_ANTRR2\_PD4](#a0cfade0fe329ae4d261ce8dd4d3c1d86)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x3, 0x4) |
| #define | [MODEM\_ANTRR2\_PD5](#af598bd2d0e6dd17957b092c2e4a73a1a)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x3, 0x5) |
| #define | [MODEM\_ANTRR3\_PC0](#a2fa9d157e9749343083524dcddd1f1d1)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x0) |
| #define | [MODEM\_ANTRR3\_PC1](#a8c1d56d6692fefbffd9ca60e9f6d45ac)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x1) |
| #define | [MODEM\_ANTRR3\_PC2](#a678e2cb9f2ac53e8630a25bec6841fd0)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x2) |
| #define | [MODEM\_ANTRR3\_PC3](#a4b8cd19ab9ff53e0b51ffcf6beea247b)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x3) |
| #define | [MODEM\_ANTRR3\_PC4](#ab4586b72a654c124f6c5c7097c9902c7)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x4) |
| #define | [MODEM\_ANTRR3\_PC5](#abc7d9d9c03ae387c0a3b028f09858b79)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x5) |
| #define | [MODEM\_ANTRR3\_PC6](#a28641556808bb4359216027d35cb3e6c)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x6) |
| #define | [MODEM\_ANTRR3\_PC7](#aec4c5821f3a602b6a15d6861bb116f22)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x7) |
| #define | [MODEM\_ANTRR3\_PC8](#a325f2e26a25e9775ce3422dee8c80355)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x8) |
| #define | [MODEM\_ANTRR3\_PC9](#ad156d5e1d6a6804e60c5621fbd3439a2)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x9) |
| #define | [MODEM\_ANTRR3\_PD0](#a3fb63d9e07fc0c63605bde31a8288b57)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x3, 0x0) |
| #define | [MODEM\_ANTRR3\_PD1](#ae8e6d95bcc501a226c2ae7cf26974ae4)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x3, 0x1) |
| #define | [MODEM\_ANTRR3\_PD2](#a203100da0081cb15ba56e28b13164d2e)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x3, 0x2) |
| #define | [MODEM\_ANTRR3\_PD3](#af02994437b5f5b545ddf48b4adb1b475)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x3, 0x3) |
| #define | [MODEM\_ANTRR3\_PD4](#a02fb9def34402666d02b843a5f5794e4)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x3, 0x4) |
| #define | [MODEM\_ANTRR3\_PD5](#a7f660712ed2ff14db606e8bdc3db8558)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x3, 0x5) |
| #define | [MODEM\_ANTRR4\_PC0](#ac9f090be13e72088bb72bf1c75094e76)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x0) |
| #define | [MODEM\_ANTRR4\_PC1](#ac4ed6ce8ae1be803f08f5fe066521cc9)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x1) |
| #define | [MODEM\_ANTRR4\_PC2](#af477f9423d354cfb59ab51fdd086cce2)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x2) |
| #define | [MODEM\_ANTRR4\_PC3](#a21f70b645f9642fb79fe2646384dfb62)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x3) |
| #define | [MODEM\_ANTRR4\_PC4](#aee6646a5a12bad19280806cd1e805cc3)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x4) |
| #define | [MODEM\_ANTRR4\_PC5](#a82cbd5d4704cd282a9cbae9109505066)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x5) |
| #define | [MODEM\_ANTRR4\_PC6](#a2cf72bdc82e898d02a4d50f8e25e764f)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x6) |
| #define | [MODEM\_ANTRR4\_PC7](#ab58e49c260c123e08f8d59f1c309560b)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x7) |
| #define | [MODEM\_ANTRR4\_PC8](#a349966b78912bc5d1bd4a177666e4cb8)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x8) |
| #define | [MODEM\_ANTRR4\_PC9](#a3c3ba01f2d9d0bc0ad672a0e7d2cceba)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x9) |
| #define | [MODEM\_ANTRR4\_PD0](#a10f6578c47953ee7d5f052e9726ee8d3)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x3, 0x0) |
| #define | [MODEM\_ANTRR4\_PD1](#ad4adb3ecb506a24bf919c524513a913c)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x3, 0x1) |
| #define | [MODEM\_ANTRR4\_PD2](#ad2ab7abbd3e49703350ae7be2d2e01b8)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x3, 0x2) |
| #define | [MODEM\_ANTRR4\_PD3](#a815940c71002bc123b8b48ac6c5cda20)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x3, 0x3) |
| #define | [MODEM\_ANTRR4\_PD4](#a3fad44fa71039513644549a88ac0a7d4)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x3, 0x4) |
| #define | [MODEM\_ANTRR4\_PD5](#adf521d37e1fe758426f06a4db451d22b)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x3, 0x5) |
| #define | [MODEM\_ANTRR5\_PC0](#aa59209d310467981d68fc8ec63856bc6)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x0) |
| #define | [MODEM\_ANTRR5\_PC1](#ae28a87908fd594ba99d726c7cd56f348)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x1) |
| #define | [MODEM\_ANTRR5\_PC2](#a51d8ba60291e9f51cc34f5826b07a336)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x2) |
| #define | [MODEM\_ANTRR5\_PC3](#a4760c7eeb47e12e62db8fac47e779c05)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x3) |
| #define | [MODEM\_ANTRR5\_PC4](#ad723f7203c93c76019adb70110860402)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x4) |
| #define | [MODEM\_ANTRR5\_PC5](#a71833f446bf584b32654327734733059)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x5) |
| #define | [MODEM\_ANTRR5\_PC6](#a8c24d68ddf4c4b644781781ed0af0f0f)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x6) |
| #define | [MODEM\_ANTRR5\_PC7](#aa599783a6852570f4719190d992eff58)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x7) |
| #define | [MODEM\_ANTRR5\_PC8](#a09791dc6a09774a53cbee6c3c78f0bc7)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x8) |
| #define | [MODEM\_ANTRR5\_PC9](#ae409168c3aab50b55d8f6cc55f18c0b2)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x9) |
| #define | [MODEM\_ANTRR5\_PD0](#a404392cc5769ad92662f7448e6458d05)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x3, 0x0) |
| #define | [MODEM\_ANTRR5\_PD1](#a88da3eca1fcd6f67c5a0c9e590c78dcf)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x3, 0x1) |
| #define | [MODEM\_ANTRR5\_PD2](#a6f6234ac85f4a3e3095672b20cd2f636)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x3, 0x2) |
| #define | [MODEM\_ANTRR5\_PD3](#a32dc3957baa49edb10e49d5914b46c14)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x3, 0x3) |
| #define | [MODEM\_ANTRR5\_PD4](#acfb8af84df8cd5036cc697ff4a225311)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x3, 0x4) |
| #define | [MODEM\_ANTRR5\_PD5](#a60065f832cefcdd2ecf5c0d6015b8943)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x3, 0x5) |
| #define | [MODEM\_ANTSWEN\_PC0](#a93c921b96501eca162c6eee962c60f57)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x0) |
| #define | [MODEM\_ANTSWEN\_PC1](#ac4ceffe68747645a764487912dc1ac16)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x1) |
| #define | [MODEM\_ANTSWEN\_PC2](#ace5d141a804e6f73e77a0fcff81e4c56)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x2) |
| #define | [MODEM\_ANTSWEN\_PC3](#a1e59daa60e50af30180144363f4f1300)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x3) |
| #define | [MODEM\_ANTSWEN\_PC4](#a2a7fa90f1a78c16a6e6cad15ff2183f0)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x4) |
| #define | [MODEM\_ANTSWEN\_PC5](#aa7767d9a2806a0843c892fddcacd7600)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x5) |
| #define | [MODEM\_ANTSWEN\_PC6](#ae3c784f6e183cadf0dee817c5b9ba192)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x6) |
| #define | [MODEM\_ANTSWEN\_PC7](#aa8ac7404cee302c171ed8646e8573a8a)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x7) |
| #define | [MODEM\_ANTSWEN\_PC8](#a41335d21a9e37772deafd2b06e9ae545)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x8) |
| #define | [MODEM\_ANTSWEN\_PC9](#a98c97461ddd331655edfccdbd1038338)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x9) |
| #define | [MODEM\_ANTSWEN\_PD0](#a6910c237541dc3d1d3c6a658aa259bb0)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x3, 0x0) |
| #define | [MODEM\_ANTSWEN\_PD1](#ab91df7c7ff2dd05a15844f0b223a4a9e)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x3, 0x1) |
| #define | [MODEM\_ANTSWEN\_PD2](#a5df0df918051e5a4c530c3b46c328e5f)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x3, 0x2) |
| #define | [MODEM\_ANTSWEN\_PD3](#aed4a6536e2515502a852bb782730081f)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x3, 0x3) |
| #define | [MODEM\_ANTSWEN\_PD4](#a9712e57526a5590d9feabdfbdd2e06e0)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x3, 0x4) |
| #define | [MODEM\_ANTSWEN\_PD5](#aad4ceb43804ecb0b5c1283254c942261)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x3, 0x5) |
| #define | [MODEM\_ANTSWUS\_PC0](#a35403ecde9ec6d51d0647558624c1755)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x0) |
| #define | [MODEM\_ANTSWUS\_PC1](#ac302424df9d075a5546b11e3a2f5a362)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x1) |
| #define | [MODEM\_ANTSWUS\_PC2](#a4c756e71ee82c7fbe41ec5ba5b33a0bd)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x2) |
| #define | [MODEM\_ANTSWUS\_PC3](#aff74d3e1d4ae4fd44a05f4d291a1f550)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x3) |
| #define | [MODEM\_ANTSWUS\_PC4](#af73c92cf63826be7cc6a1fe3e03b181d)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x4) |
| #define | [MODEM\_ANTSWUS\_PC5](#a294c8a1ce79d365a9d29717db3942107)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x5) |
| #define | [MODEM\_ANTSWUS\_PC6](#afad4a0c9a58b16b48cb06279fd7db652)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x6) |
| #define | [MODEM\_ANTSWUS\_PC7](#a6f86a2ef7edfbe782b7700efae544a48)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x7) |
| #define | [MODEM\_ANTSWUS\_PC8](#a6a470c8cd7b56a56b1be748427bd326c)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x8) |
| #define | [MODEM\_ANTSWUS\_PC9](#ad94ab3184202a103d96e35f4f3658bdf)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x9) |
| #define | [MODEM\_ANTSWUS\_PD0](#aa47c88d6d4e2cc38e891b7e03e699756)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x3, 0x0) |
| #define | [MODEM\_ANTSWUS\_PD1](#a72a8e4b8a5ac8c3fe74eb26cd08e312b)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x3, 0x1) |
| #define | [MODEM\_ANTSWUS\_PD2](#a6852ed7e65ee6e22f96ecddbe0bcc05d)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x3, 0x2) |
| #define | [MODEM\_ANTSWUS\_PD3](#ab3e009ff6d5427f43e9fbf4743098520)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x3, 0x3) |
| #define | [MODEM\_ANTSWUS\_PD4](#a4b7a96b271c947e02a2261da3959588d)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x3, 0x4) |
| #define | [MODEM\_ANTSWUS\_PD5](#ad5f74a2313abda0899378de0de5480f6)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x3, 0x5) |
| #define | [MODEM\_ANTTRIG\_PC0](#a0b75979323bdd89b0cc9d10469b0095c)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x0) |
| #define | [MODEM\_ANTTRIG\_PC1](#a93518da86e975b51c00c957f0bb95ab0)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x1) |
| #define | [MODEM\_ANTTRIG\_PC2](#a27622d1c3e77514a6c175f88ba67b2f6)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x2) |
| #define | [MODEM\_ANTTRIG\_PC3](#afe612f9d7068a7d8f3f27950a3db07e5)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x3) |
| #define | [MODEM\_ANTTRIG\_PC4](#aa4e5df434329d0121c13dc72c90c9c13)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x4) |
| #define | [MODEM\_ANTTRIG\_PC5](#a0c7cd91aef9412c36340e43a41b95fbe)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x5) |
| #define | [MODEM\_ANTTRIG\_PC6](#a6bbd8a93a130ac08292335b664803e3b)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x6) |
| #define | [MODEM\_ANTTRIG\_PC7](#a69b763a9d3a015481424995589a80c3f)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x7) |
| #define | [MODEM\_ANTTRIG\_PC8](#a6845de25ca254d6d61e404f9e2847bff)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x8) |
| #define | [MODEM\_ANTTRIG\_PC9](#ab3cf955809a2bc320ac95fd7eae4f77c)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x9) |
| #define | [MODEM\_ANTTRIG\_PD0](#abc60b310f524562dc1252fec0238dbdf)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x3, 0x0) |
| #define | [MODEM\_ANTTRIG\_PD1](#ac437bf9340d8c56595543e8de7b9157e)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x3, 0x1) |
| #define | [MODEM\_ANTTRIG\_PD2](#a6b33477ce6327abad3ce4bcbba3eec9a)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x3, 0x2) |
| #define | [MODEM\_ANTTRIG\_PD3](#a132e606271a453be558397a95d72c17e)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x3, 0x3) |
| #define | [MODEM\_ANTTRIG\_PD4](#a34eeb11f04820ff36f7730e2a49ffa07)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x3, 0x4) |
| #define | [MODEM\_ANTTRIG\_PD5](#ac21df5f70a16ed217b29668eb66b6844)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x3, 0x5) |
| #define | [MODEM\_ANTTRIGSTOP\_PC0](#af7e05b86331a8d9c02cd27a4e2dc84b7)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x0) |
| #define | [MODEM\_ANTTRIGSTOP\_PC1](#aa658e7c0b2ec76108d710ce93e1d787a)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x1) |
| #define | [MODEM\_ANTTRIGSTOP\_PC2](#a9770ce38a0f236ecd2a7f6cd56e1eff4)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x2) |
| #define | [MODEM\_ANTTRIGSTOP\_PC3](#a61b3ce65ad555f6ad8b69a182626d90e)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x3) |
| #define | [MODEM\_ANTTRIGSTOP\_PC4](#a65384fc71c75bf574740388627bca46f)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x4) |
| #define | [MODEM\_ANTTRIGSTOP\_PC5](#a4c123cd5fca0b4e4e0bc79fbb77292f5)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x5) |
| #define | [MODEM\_ANTTRIGSTOP\_PC6](#a98d91dafafd9175fbdd1074e9526ceaf)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x6) |
| #define | [MODEM\_ANTTRIGSTOP\_PC7](#a26f49d68743f2c7df6e22be7354ffb7f)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x7) |
| #define | [MODEM\_ANTTRIGSTOP\_PC8](#a9ea34515036f5cb0913983c8d5de9a6b)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x8) |
| #define | [MODEM\_ANTTRIGSTOP\_PC9](#a29fa566ce5a4754c4fd809763061c8c6)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x9) |
| #define | [MODEM\_ANTTRIGSTOP\_PD0](#a2689b6b9d9286a13b7b6d2ead8c3993a)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x3, 0x0) |
| #define | [MODEM\_ANTTRIGSTOP\_PD1](#a09410c6d05c79937b0385a8552c292f2)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x3, 0x1) |
| #define | [MODEM\_ANTTRIGSTOP\_PD2](#a413c60ac3ae878a6e4e70e39c6c85fd9)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x3, 0x2) |
| #define | [MODEM\_ANTTRIGSTOP\_PD3](#a20053bb1092ce80cc23cd88aa88fc30d)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x3, 0x3) |
| #define | [MODEM\_ANTTRIGSTOP\_PD4](#ab1007c53ed7798c259ddf55945cd31d1)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x3, 0x4) |
| #define | [MODEM\_ANTTRIGSTOP\_PD5](#ad695401164a6065e3bd39d94098d1dd8)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x3, 0x5) |
| #define | [MODEM\_DCLK\_PA0](#a08ca0610796eea5484d295a978221196)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x0) |
| #define | [MODEM\_DCLK\_PA1](#a405e18321ac14727b470918f185f923c)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x1) |
| #define | [MODEM\_DCLK\_PA2](#a2e7d5bc810c26a1194a846663607762d)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x2) |
| #define | [MODEM\_DCLK\_PA3](#a483f89509d4d25fe14f3d8cff618289d)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x3) |
| #define | [MODEM\_DCLK\_PA4](#a8e3916287d03243cca904f41ce1f9dae)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x4) |
| #define | [MODEM\_DCLK\_PA5](#afd75314e866b5c47e838556d866d5883)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x5) |
| #define | [MODEM\_DCLK\_PA6](#acf3a1e4e5b714d53ff82edbf02575ec5)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x6) |
| #define | [MODEM\_DCLK\_PA7](#ab339753673d17ab957324821a8933d94)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x7) |
| #define | [MODEM\_DCLK\_PA8](#a4ffefd11c83ed290890ffb7657507a1e)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x8) |
| #define | [MODEM\_DCLK\_PA9](#a786f180681731e9e3819170d4ae306a0)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x9) |
| #define | [MODEM\_DCLK\_PB0](#a19236a132524a68b08b88a2b71b74b7b)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x1, 0x0) |
| #define | [MODEM\_DCLK\_PB1](#a862abc8858bae8ba0af6b0f8fbbaae37)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x1, 0x1) |
| #define | [MODEM\_DCLK\_PB2](#aefcf9c6de61eb621830516b3de6cf348)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x1, 0x2) |
| #define | [MODEM\_DCLK\_PB3](#ad15e63bf8718d8705673620a730009c7)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x1, 0x3) |
| #define | [MODEM\_DCLK\_PB4](#a76a21531211dfe45e53ceae776c396b6)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x1, 0x4) |
| #define | [MODEM\_DCLK\_PB5](#a659fe2d7a1d06ddd921e2d00b5d84efa)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x1, 0x5) |
| #define | [MODEM\_DOUT\_PA0](#ac3823581963866285b9f6143d16d9c38)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x0) |
| #define | [MODEM\_DOUT\_PA1](#ae4c319e1bba60e4a5a891edf88b1e968)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x1) |
| #define | [MODEM\_DOUT\_PA2](#a8dabb728396cf206afac2cfbe49a5b02)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x2) |
| #define | [MODEM\_DOUT\_PA3](#ae5963b1e2305ae53f11a90b0d76a99a3)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x3) |
| #define | [MODEM\_DOUT\_PA4](#a06061dfed7797c0e29bb9cb5a6d49f88)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x4) |
| #define | [MODEM\_DOUT\_PA5](#a117ead5a3ea011c4ad9d37fc96de2bba)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x5) |
| #define | [MODEM\_DOUT\_PA6](#aeda2e59bc16dda7ee3d83a2504a04f05)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x6) |
| #define | [MODEM\_DOUT\_PA7](#a1d0857025a77fb254ea0e2f7594471f5)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x7) |
| #define | [MODEM\_DOUT\_PA8](#a399d0cc64e37dbf683cbcacf14f2d870)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x8) |
| #define | [MODEM\_DOUT\_PA9](#ad7f20d72a11d1423459e6a2f5dc9d870)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x9) |
| #define | [MODEM\_DOUT\_PB0](#abe0c4060d5f35e9cf8e002676f3c238c)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x1, 0x0) |
| #define | [MODEM\_DOUT\_PB1](#aff30fef58eb6dbd17426f7e175c8f4ae)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x1, 0x1) |
| #define | [MODEM\_DOUT\_PB2](#ac013e04b2f5d3b419c24f2b1b7f27bad)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x1, 0x2) |
| #define | [MODEM\_DOUT\_PB3](#a9011320165978614b4933f9194d45892)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x1, 0x3) |
| #define | [MODEM\_DOUT\_PB4](#aabf2e613152cd24a321ad3711cc3c30e)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x1, 0x4) |
| #define | [MODEM\_DOUT\_PB5](#ab4d26059a5cc7ebdb19ca77c4bbb4ac7)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x1, 0x5) |
| #define | [MODEM\_DIN\_PA0](#a3e0e16cfb9e9ad19a8e76e07e458d676)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x0) |
| #define | [MODEM\_DIN\_PA1](#a3770dcebe1ad3c30c3fbcdcc9e1e61ac)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x1) |
| #define | [MODEM\_DIN\_PA2](#aed7868ce54670b163ae60f645e353e10)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x2) |
| #define | [MODEM\_DIN\_PA3](#a55004a63d39356caf5bda66e005a25f3)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x3) |
| #define | [MODEM\_DIN\_PA4](#a1c13babd5d2f16d4d56257f847e84f40)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x4) |
| #define | [MODEM\_DIN\_PA5](#a4f09d7e3de2cde036a6ddfcfe35bc96a)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x5) |
| #define | [MODEM\_DIN\_PA6](#aa310c43126dfd99d7f967141340934c2)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x6) |
| #define | [MODEM\_DIN\_PA7](#a201de78e9064b3467b2bbdc0a93ae4b2)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x7) |
| #define | [MODEM\_DIN\_PA8](#a12d5bed446ee0a12698d247f187835ed)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x8) |
| #define | [MODEM\_DIN\_PA9](#ab53ce7a305b3676b6ff0adb149fc2312)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x9) |
| #define | [MODEM\_DIN\_PB0](#a87a115f7d2707bf513e218401f2d10fd)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x1, 0x0) |
| #define | [MODEM\_DIN\_PB1](#a4484f366718daefbdd23d72248a1ba0d)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x1, 0x1) |
| #define | [MODEM\_DIN\_PB2](#a9513dd16e152b54918b10a3ca7b2bddd)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x1, 0x2) |
| #define | [MODEM\_DIN\_PB3](#a4ff611638d1c08ae3412e8df31d45e2c)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x1, 0x3) |
| #define | [MODEM\_DIN\_PB4](#abfd0c609a7621aac4e345fa264776629)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x1, 0x4) |
| #define | [MODEM\_DIN\_PB5](#a9a3b3307b9ed3b722798678e9c72b842)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x1, 0x5) |
| #define | [PCNT0\_S0IN\_PA0](#a6f33d3b2bff583fd32a0cdab0b18cb86)   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x0) |
| #define | [PCNT0\_S0IN\_PA1](#ae5ac22184b51df9b1e1faafa9533e59c)   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x1) |
| #define | [PCNT0\_S0IN\_PA2](#a0604ebad29651279e423afba646dfb58)   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x2) |
| #define | [PCNT0\_S0IN\_PA3](#a841091dc34bc7e16418a89190db3b15a)   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x3) |
| #define | [PCNT0\_S0IN\_PA4](#ae5fd092cc2df7f9b52ece05e38a217da)   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x4) |
| #define | [PCNT0\_S0IN\_PA5](#a95ac0aa1f1af4a615a2dc3c7f9512c83)   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x5) |
| #define | [PCNT0\_S0IN\_PA6](#aa8a5beba997a1af2cfd55cc90e62c08a)   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x6) |
| #define | [PCNT0\_S0IN\_PA7](#a9e69a57169a3e1698c8980dfe3189705)   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x7) |
| #define | [PCNT0\_S0IN\_PA8](#a07910d5ea15530f07109f589a71b1a35)   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x8) |
| #define | [PCNT0\_S0IN\_PA9](#a9459850934983e2f7a2521f7f06d2e4c)   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x9) |
| #define | [PCNT0\_S0IN\_PB0](#a9ff535d912f08e887963a392bd377247)   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x1, 0x0) |
| #define | [PCNT0\_S0IN\_PB1](#a305fa64123cc206b67fabbd020a4b665)   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x1, 0x1) |
| #define | [PCNT0\_S0IN\_PB2](#a3d91c6a4cc9fb9819912e33b9fa9d190)   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x1, 0x2) |
| #define | [PCNT0\_S0IN\_PB3](#a37ddc5da1d667f70a626d61f6831f4e1)   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x1, 0x3) |
| #define | [PCNT0\_S0IN\_PB4](#a223a1fc3d272027257b9023233a0fe7d)   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x1, 0x4) |
| #define | [PCNT0\_S0IN\_PB5](#a94df2d91a7055e2a0a05f9ebaa188922)   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x1, 0x5) |
| #define | [PCNT0\_S1IN\_PA0](#a7225c02a0bf7ac0257d56326403e00f5)   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x0) |
| #define | [PCNT0\_S1IN\_PA1](#a2bf0eec0a8e51aca6df3956edcc5af02)   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x1) |
| #define | [PCNT0\_S1IN\_PA2](#aed7e3df711ccdd37ced4405246867b41)   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x2) |
| #define | [PCNT0\_S1IN\_PA3](#a0fc69216ccf38893b398e20795b45203)   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x3) |
| #define | [PCNT0\_S1IN\_PA4](#a9b18d46d7c00f9440ae6ead1f7071bbb)   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x4) |
| #define | [PCNT0\_S1IN\_PA5](#acec4b827bd7ab080e1f770ce064b0f60)   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x5) |
| #define | [PCNT0\_S1IN\_PA6](#ad9267387f1c65fcdaf368bca61f26db6)   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x6) |
| #define | [PCNT0\_S1IN\_PA7](#ad652d68108d9c607b8f210ddcf830694)   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x7) |
| #define | [PCNT0\_S1IN\_PA8](#ab8ad1e725b2ba90915ba35e8494b6804)   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x8) |
| #define | [PCNT0\_S1IN\_PA9](#aa97493aef428388b49c5cb0dafd83474)   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x9) |
| #define | [PCNT0\_S1IN\_PB0](#a9d9e33c9279d6bf9ec430d655fa0b4ac)   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x1, 0x0) |
| #define | [PCNT0\_S1IN\_PB1](#ae663132285843f7983adf5f0a3dec3cd)   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x1, 0x1) |
| #define | [PCNT0\_S1IN\_PB2](#a7895b597ddbea56c1ea51ea9361a7c0e)   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x1, 0x2) |
| #define | [PCNT0\_S1IN\_PB3](#a63821a509b711209d91ebc80553db2cb)   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x1, 0x3) |
| #define | [PCNT0\_S1IN\_PB4](#a11a9f343a105826bc90054c8d8cb220c)   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x1, 0x4) |
| #define | [PCNT0\_S1IN\_PB5](#a084532ef7c32bd35298aeabf0b3f376b)   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x1, 0x5) |
| #define | [PRS0\_ASYNCH0\_PA0](#af1dcdc8d0ea9b8671a240ce03d80d434)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x0) |
| #define | [PRS0\_ASYNCH0\_PA1](#af712c40bafb6ba29d062f47a47ef4445)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x1) |
| #define | [PRS0\_ASYNCH0\_PA2](#a4a95bfd98958b7944ef58c010df91d83)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x2) |
| #define | [PRS0\_ASYNCH0\_PA3](#ab912f56311db65e5316e921180f46589)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x3) |
| #define | [PRS0\_ASYNCH0\_PA4](#ac1e05749654ec2bee09aa75a951bcd57)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x4) |
| #define | [PRS0\_ASYNCH0\_PA5](#a15788b1a1cdce57fddf0d58e884e37bc)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x5) |
| #define | [PRS0\_ASYNCH0\_PA6](#af071c0ad0ca5a54d74c7fa4e2f7eea6c)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x6) |
| #define | [PRS0\_ASYNCH0\_PA7](#accc5ad5ffa51459772c03387f67f6db1)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x7) |
| #define | [PRS0\_ASYNCH0\_PA8](#af170d0ff0c56bdf3bd13eaa00f2f3fea)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x8) |
| #define | [PRS0\_ASYNCH0\_PA9](#aabb6361fee457b8d9f787e1333ee340b)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x9) |
| #define | [PRS0\_ASYNCH0\_PB0](#a590472d980647bc2a513ee516c9c4f1b)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x1, 0x0) |
| #define | [PRS0\_ASYNCH0\_PB1](#af4ee1a5d6ccadd510de798cf41f973ee)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x1, 0x1) |
| #define | [PRS0\_ASYNCH0\_PB2](#a0517d6b5213d9f8ebfb445e7aa0cf2e7)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x1, 0x2) |
| #define | [PRS0\_ASYNCH0\_PB3](#a0b229da2aec9ffb51c50e0ca19e1a45d)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x1, 0x3) |
| #define | [PRS0\_ASYNCH0\_PB4](#a281aa5d676ea7ac358df567ab98663b3)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x1, 0x4) |
| #define | [PRS0\_ASYNCH0\_PB5](#abfeaa99e158b38cae62b01dfcd7338ab)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x1, 0x5) |
| #define | [PRS0\_ASYNCH1\_PA0](#aa7c8c749fddaf4b2e22e3791d9e8921a)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x0) |
| #define | [PRS0\_ASYNCH1\_PA1](#a8f998569835e3b8688423cf9b4e81810)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x1) |
| #define | [PRS0\_ASYNCH1\_PA2](#a5f2d980e4505820849c42fdc36c1b5a9)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x2) |
| #define | [PRS0\_ASYNCH1\_PA3](#a4b66d13c4589bb2663661e6cfb8c0274)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x3) |
| #define | [PRS0\_ASYNCH1\_PA4](#aec6f34dc1716b25b0fcc0628b18cbf86)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x4) |
| #define | [PRS0\_ASYNCH1\_PA5](#a0be6148e1124f7e8dc6773f59dfd8ceb)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x5) |
| #define | [PRS0\_ASYNCH1\_PA6](#a4d1894b5f84e0e7c81a5dbb2bfe8318f)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x6) |
| #define | [PRS0\_ASYNCH1\_PA7](#a95455187a1575a8e8249d1e4178131c5)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x7) |
| #define | [PRS0\_ASYNCH1\_PA8](#a85428a0cef95ef5674719cfbac44eed5)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x8) |
| #define | [PRS0\_ASYNCH1\_PA9](#ad6db6ce8273bbd9701f7e0880973d395)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x9) |
| #define | [PRS0\_ASYNCH1\_PB0](#a76487417602321711041f2d5d721e8ae)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x1, 0x0) |
| #define | [PRS0\_ASYNCH1\_PB1](#a1626bdc4551620aaccbfacd8aa0c0cdf)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x1, 0x1) |
| #define | [PRS0\_ASYNCH1\_PB2](#ac68d7c6b3b4607a2eb07926ceb42b0b3)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x1, 0x2) |
| #define | [PRS0\_ASYNCH1\_PB3](#a5b843903080dcfb8d654248f04b56bb1)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x1, 0x3) |
| #define | [PRS0\_ASYNCH1\_PB4](#ae1a66f7dff2089736cc20cee277a5cd4)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x1, 0x4) |
| #define | [PRS0\_ASYNCH1\_PB5](#aa2b7e3b1f891e86d34ef2faed3bde83c)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x1, 0x5) |
| #define | [PRS0\_ASYNCH2\_PA0](#ab9115b54fff36f0449722af1659860fb)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x0) |
| #define | [PRS0\_ASYNCH2\_PA1](#a82e86536168f11e5b02c4fac703128b1)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x1) |
| #define | [PRS0\_ASYNCH2\_PA2](#af3124f46d26efbb18047172d5d5accbc)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x2) |
| #define | [PRS0\_ASYNCH2\_PA3](#a57857d486b2fc1db0770a7d1e198ed95)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x3) |
| #define | [PRS0\_ASYNCH2\_PA4](#a3d91108c838d4684846d56816aee5fe1)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x4) |
| #define | [PRS0\_ASYNCH2\_PA5](#a8e7b151ff1870ccfc66a34096b4aebae)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x5) |
| #define | [PRS0\_ASYNCH2\_PA6](#a7f536e8d1d66285820ab8e3808e49a0f)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x6) |
| #define | [PRS0\_ASYNCH2\_PA7](#a41efde6eb746e07baf306e05197a8948)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x7) |
| #define | [PRS0\_ASYNCH2\_PA8](#a95b452fe92602af5bff499d14f1cae11)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x8) |
| #define | [PRS0\_ASYNCH2\_PA9](#ae90ff17ea0c75c4e35b2f7fdfe87260f)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x9) |
| #define | [PRS0\_ASYNCH2\_PB0](#a81bf0662053265b1d9cc03c101d4a353)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x1, 0x0) |
| #define | [PRS0\_ASYNCH2\_PB1](#a026322616f156126afcbcebc25d104c0)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x1, 0x1) |
| #define | [PRS0\_ASYNCH2\_PB2](#a6a39b350109c932587f1c1623898d178)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x1, 0x2) |
| #define | [PRS0\_ASYNCH2\_PB3](#a30b84121b903ca053238c3a1110fd247)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x1, 0x3) |
| #define | [PRS0\_ASYNCH2\_PB4](#a68e5aa33a7ccd7af8abe83550bc9fcf2)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x1, 0x4) |
| #define | [PRS0\_ASYNCH2\_PB5](#ad6152fcacafb28c981e8f349557fcc43)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x1, 0x5) |
| #define | [PRS0\_ASYNCH3\_PA0](#a94b5b779374768ed16ad8cc396f756aa)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x0) |
| #define | [PRS0\_ASYNCH3\_PA1](#aa947bb280b4891081e7a4de9dba44ae5)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x1) |
| #define | [PRS0\_ASYNCH3\_PA2](#a9bc4d14c37fd2724643735c13cc9a25d)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x2) |
| #define | [PRS0\_ASYNCH3\_PA3](#afa101472245a7df51d906f31093ce640)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x3) |
| #define | [PRS0\_ASYNCH3\_PA4](#a1e433ac2a9a5c1b9240b157033e8fdc1)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x4) |
| #define | [PRS0\_ASYNCH3\_PA5](#a4af0e3dc3303ec055fcce97399ccf4ba)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x5) |
| #define | [PRS0\_ASYNCH3\_PA6](#ad905e3cca4ec1b92f1fd6b0ca18b8c06)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x6) |
| #define | [PRS0\_ASYNCH3\_PA7](#a64d14cae622fb5814402d3bf6c042a47)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x7) |
| #define | [PRS0\_ASYNCH3\_PA8](#a0ceb4585c15bf959906dd93aed744f0d)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x8) |
| #define | [PRS0\_ASYNCH3\_PA9](#ae48735563ea7be3be49285f230231bf3)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x9) |
| #define | [PRS0\_ASYNCH3\_PB0](#a5cb1e7fbb39adfdfca2516715f0cc1ac)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x1, 0x0) |
| #define | [PRS0\_ASYNCH3\_PB1](#aa09fe8bc9d5c277db64c0912b55e9651)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x1, 0x1) |
| #define | [PRS0\_ASYNCH3\_PB2](#a8fd4c8b45bb5366691e3ea98b20ca580)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x1, 0x2) |
| #define | [PRS0\_ASYNCH3\_PB3](#a92ac18184efd55f90aecf9763b1d93b9)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x1, 0x3) |
| #define | [PRS0\_ASYNCH3\_PB4](#a3b96ce5680cf373ff511249aec0d4ea3)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x1, 0x4) |
| #define | [PRS0\_ASYNCH3\_PB5](#a895aabf3809c957da7438989e9fadc3a)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x1, 0x5) |
| #define | [PRS0\_ASYNCH4\_PA0](#a016d312ee53e23e053e5322038c218e8)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x0) |
| #define | [PRS0\_ASYNCH4\_PA1](#ac08b73b2d1c8340a46b2b4321d258bbf)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x1) |
| #define | [PRS0\_ASYNCH4\_PA2](#a6d468079dce68ad1a80a09411eed3c61)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x2) |
| #define | [PRS0\_ASYNCH4\_PA3](#a2901f5a1abe787afaaf8c04a6aafa57f)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x3) |
| #define | [PRS0\_ASYNCH4\_PA4](#a599e583eb87879b76f1a889093ca1db7)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x4) |
| #define | [PRS0\_ASYNCH4\_PA5](#a50cd729844356a327a34588ab70c9f51)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x5) |
| #define | [PRS0\_ASYNCH4\_PA6](#a15672ea11df2224289fc84c07abddbce)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x6) |
| #define | [PRS0\_ASYNCH4\_PA7](#a765447cc275c70881ae23b795c7fc53c)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x7) |
| #define | [PRS0\_ASYNCH4\_PA8](#a9ce8837d29bbd43cf040ade45311b569)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x8) |
| #define | [PRS0\_ASYNCH4\_PA9](#a1ab7c845d070ad001ec1af11fa70453e)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x9) |
| #define | [PRS0\_ASYNCH4\_PB0](#ab0da5394e8fceec3a24c8ca362a6a73f)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x1, 0x0) |
| #define | [PRS0\_ASYNCH4\_PB1](#a95e9e61ebc91932e32cf3683ba99beb7)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x1, 0x1) |
| #define | [PRS0\_ASYNCH4\_PB2](#a9b7b2081e0a38e0e6ab9f2d3ca3654d8)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x1, 0x2) |
| #define | [PRS0\_ASYNCH4\_PB3](#a0516f5991ffed91ba799d6d463f05945)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x1, 0x3) |
| #define | [PRS0\_ASYNCH4\_PB4](#a8b217bac132dc7c18930e4fe8c4e58db)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x1, 0x4) |
| #define | [PRS0\_ASYNCH4\_PB5](#a135d877dcee477d815fa6ee27dffe09f)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x1, 0x5) |
| #define | [PRS0\_ASYNCH5\_PA0](#a6cac49a6aeefd56ad4ba7e4cba8910bf)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x0) |
| #define | [PRS0\_ASYNCH5\_PA1](#a8442fb1410b80fcd20c78b7cc44608eb)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x1) |
| #define | [PRS0\_ASYNCH5\_PA2](#aa3e3bbc87f46c7f0b9016518266e1fb2)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x2) |
| #define | [PRS0\_ASYNCH5\_PA3](#a269678c70e29d05e9d67b82b1d5dcfd2)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x3) |
| #define | [PRS0\_ASYNCH5\_PA4](#a7a314bb07eab261a850420ac2d6a2618)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x4) |
| #define | [PRS0\_ASYNCH5\_PA5](#ac01e6bde894c73d5e965b7fe6ed03f53)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x5) |
| #define | [PRS0\_ASYNCH5\_PA6](#ae3d6e3ae9d6d9d7c41ca233ad101b025)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x6) |
| #define | [PRS0\_ASYNCH5\_PA7](#a769160beeaa4ca59cae64a1c61b5c90e)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x7) |
| #define | [PRS0\_ASYNCH5\_PA8](#a7485b4e8b8b2eca4594481533f547997)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x8) |
| #define | [PRS0\_ASYNCH5\_PA9](#afd07ce0874b05616058dc214ded43b1a)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x9) |
| #define | [PRS0\_ASYNCH5\_PB0](#adb08d0b33060e185431fb336110899c9)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x1, 0x0) |
| #define | [PRS0\_ASYNCH5\_PB1](#a82b599c4956aeea92802694032b4b55a)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x1, 0x1) |
| #define | [PRS0\_ASYNCH5\_PB2](#a26b4fa1b83e7857071e5f5d434055a6a)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x1, 0x2) |
| #define | [PRS0\_ASYNCH5\_PB3](#a0fbf5258e9f5d24e164a31dbdb40443e)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x1, 0x3) |
| #define | [PRS0\_ASYNCH5\_PB4](#a7de3a9532a4e4fdf5380046737950e18)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x1, 0x4) |
| #define | [PRS0\_ASYNCH5\_PB5](#aea378afb137f62f3f01b3a87c09dcd4f)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x1, 0x5) |
| #define | [PRS0\_ASYNCH6\_PC0](#a5c7910d134b9fe6ddf1da299dfb2cfa0)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x0) |
| #define | [PRS0\_ASYNCH6\_PC1](#a713321693f2cfd7cda27d1c36fc9b74b)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x1) |
| #define | [PRS0\_ASYNCH6\_PC2](#a907d3ee7390b6ebcb5cac75724b6c587)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x2) |
| #define | [PRS0\_ASYNCH6\_PC3](#a5eebd47a62e87b938b530113cd048481)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x3) |
| #define | [PRS0\_ASYNCH6\_PC4](#a2d0d89b1abadc95ec02a88916330bab4)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x4) |
| #define | [PRS0\_ASYNCH6\_PC5](#aaa44b81b3421197bff7df84a5e90a566)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x5) |
| #define | [PRS0\_ASYNCH6\_PC6](#aaeaba294a765ca9892f4591acb3dd83e)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x6) |
| #define | [PRS0\_ASYNCH6\_PC7](#a0d95bb763b051fb232dc8805ad6d643e)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x7) |
| #define | [PRS0\_ASYNCH6\_PC8](#a153f3fcc748dc54f64c23f8c23d9db39)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x8) |
| #define | [PRS0\_ASYNCH6\_PC9](#a6de52f879778b33cc6fa14060dbccaec)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x9) |
| #define | [PRS0\_ASYNCH6\_PD0](#a0db829680023f49ec8b84b8418994f57)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x3, 0x0) |
| #define | [PRS0\_ASYNCH6\_PD1](#a41989b05cfd244afef8a6c359de6f6cb)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x3, 0x1) |
| #define | [PRS0\_ASYNCH6\_PD2](#ad70491288162b935edc6602844fbad73)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x3, 0x2) |
| #define | [PRS0\_ASYNCH6\_PD3](#a03cdfe05c93c94a99e457fc34be7adb3)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x3, 0x3) |
| #define | [PRS0\_ASYNCH6\_PD4](#a6c74cc2ba56d399a25378ecccef3005f)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x3, 0x4) |
| #define | [PRS0\_ASYNCH6\_PD5](#a907ff75410116fd75163bbb7ad72a14d)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x3, 0x5) |
| #define | [PRS0\_ASYNCH7\_PC0](#a263dcb3077d0d1e3a58730140042046d)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x0) |
| #define | [PRS0\_ASYNCH7\_PC1](#aa49bafce35b9bb4b59c8c9c22f06a739)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x1) |
| #define | [PRS0\_ASYNCH7\_PC2](#ae0305282eab2df6979c235c8d5d00ac7)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x2) |
| #define | [PRS0\_ASYNCH7\_PC3](#a05355f9a968579fd8a931b7458d37960)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x3) |
| #define | [PRS0\_ASYNCH7\_PC4](#acb9a2a6531dd263cfe56858aa9c77791)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x4) |
| #define | [PRS0\_ASYNCH7\_PC5](#af504334eb99bab375e929f662ee6091a)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x5) |
| #define | [PRS0\_ASYNCH7\_PC6](#a770b593af51ec2f1fae3694e1a29cdef)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x6) |
| #define | [PRS0\_ASYNCH7\_PC7](#a96d44dd7e3fb6c4a68e5c2f029d0e3d4)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x7) |
| #define | [PRS0\_ASYNCH7\_PC8](#a7eb775f790ebbe32f93c2cdc2630cd0a)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x8) |
| #define | [PRS0\_ASYNCH7\_PC9](#a6af238ef897be1e90e2cd8de910cd0eb)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x9) |
| #define | [PRS0\_ASYNCH7\_PD0](#a4e38e496fe8a602726a9fcfac5c9553b)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x3, 0x0) |
| #define | [PRS0\_ASYNCH7\_PD1](#a8a5617fb6a01d979b5754bb30438ef11)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x3, 0x1) |
| #define | [PRS0\_ASYNCH7\_PD2](#ae44270558459c4a31a9d8db2216b6a47)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x3, 0x2) |
| #define | [PRS0\_ASYNCH7\_PD3](#a19e5fc23eb4c5edbe4cc2be54508038a)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x3, 0x3) |
| #define | [PRS0\_ASYNCH7\_PD4](#a6f3cf739f48f52265c18a437b40c919f)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x3, 0x4) |
| #define | [PRS0\_ASYNCH7\_PD5](#ae6eae6f47a075d75a1ea7e258696ac7c)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x3, 0x5) |
| #define | [PRS0\_ASYNCH8\_PC0](#a01aee008d4ae0969e81630224253732c)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x0) |
| #define | [PRS0\_ASYNCH8\_PC1](#a1020e0f439015d77aad3a4ad6761745f)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x1) |
| #define | [PRS0\_ASYNCH8\_PC2](#a78ac7a7a23787837c2d45b7fb619d973)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x2) |
| #define | [PRS0\_ASYNCH8\_PC3](#a21d56ee2bba901bb0ad42fe00fd47126)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x3) |
| #define | [PRS0\_ASYNCH8\_PC4](#ab38e8e6ebf5f7b8cf9db913835c77fdf)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x4) |
| #define | [PRS0\_ASYNCH8\_PC5](#a034b8fafc8f80d4aa749ace8d383aa42)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x5) |
| #define | [PRS0\_ASYNCH8\_PC6](#a9b6282a03652ffd9886abf001018942e)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x6) |
| #define | [PRS0\_ASYNCH8\_PC7](#a7a33bde9021e0d8f1a4c331064369169)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x7) |
| #define | [PRS0\_ASYNCH8\_PC8](#a6e2a2dad2c91c6f53235eca30fbbcb71)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x8) |
| #define | [PRS0\_ASYNCH8\_PC9](#adfc74b9cf0bc54094e44eb498174baf2)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x9) |
| #define | [PRS0\_ASYNCH8\_PD0](#a3c4c1e1e2ed6aad821543605099c464e)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x3, 0x0) |
| #define | [PRS0\_ASYNCH8\_PD1](#a7a96c3dddcf49a09ab3941a19e33dd2b)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x3, 0x1) |
| #define | [PRS0\_ASYNCH8\_PD2](#a045129ec46f95f26ba665876216df09a)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x3, 0x2) |
| #define | [PRS0\_ASYNCH8\_PD3](#abf899559efdca73abc5e1f3e058280dc)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x3, 0x3) |
| #define | [PRS0\_ASYNCH8\_PD4](#aa41526f1e85b40d4d9f30444542c19e2)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x3, 0x4) |
| #define | [PRS0\_ASYNCH8\_PD5](#ae7d962af59b6c3577581a675b2cbb3ee)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x3, 0x5) |
| #define | [PRS0\_ASYNCH9\_PC0](#ad6900f2865fce19423ba5bce65e6f6ec)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x0) |
| #define | [PRS0\_ASYNCH9\_PC1](#a21a22ddcc1d1b8c05250ea00bfaf2c46)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x1) |
| #define | [PRS0\_ASYNCH9\_PC2](#a7dcb713d1f7f8457e30812454272c360)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x2) |
| #define | [PRS0\_ASYNCH9\_PC3](#ac6eeb711fa526a794104a43142cedc8d)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x3) |
| #define | [PRS0\_ASYNCH9\_PC4](#a87ada6898e2eeddcaeead80835a3800b)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x4) |
| #define | [PRS0\_ASYNCH9\_PC5](#a6b5b3ca2088cb2c43fbebf99cd4e9ad3)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x5) |
| #define | [PRS0\_ASYNCH9\_PC6](#a4383c5af531fd312831c4116e60bec7e)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x6) |
| #define | [PRS0\_ASYNCH9\_PC7](#a59c911b1c45a061480e83d081796f84b)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x7) |
| #define | [PRS0\_ASYNCH9\_PC8](#ad17efaa7728c44ad44f68631501b5041)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x8) |
| #define | [PRS0\_ASYNCH9\_PC9](#adbd9075be51a80c7102f9a873af230c1)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x9) |
| #define | [PRS0\_ASYNCH9\_PD0](#a89cd80ad72079b3a20917cc722fed3c3)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x3, 0x0) |
| #define | [PRS0\_ASYNCH9\_PD1](#aa9433d94ee912ff578dc1f3753bca9b5)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x3, 0x1) |
| #define | [PRS0\_ASYNCH9\_PD2](#a1dfa38b0754566f3586712b7474ce13f)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x3, 0x2) |
| #define | [PRS0\_ASYNCH9\_PD3](#a48c2477430954a1f5ebefcd625132b34)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x3, 0x3) |
| #define | [PRS0\_ASYNCH9\_PD4](#a3f32b54daa1e09ccb97ad447facd5076)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x3, 0x4) |
| #define | [PRS0\_ASYNCH9\_PD5](#a7e8227352546862fba1996f7a5c13e5c)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x3, 0x5) |
| #define | [PRS0\_ASYNCH10\_PC0](#af096e7ffddaaf21a0886246861e94cf0)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x0) |
| #define | [PRS0\_ASYNCH10\_PC1](#ab2e7c25b6faf577e7ee8197ae806a979)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x1) |
| #define | [PRS0\_ASYNCH10\_PC2](#a22dd84a911044fe555ee09be1ee255e6)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x2) |
| #define | [PRS0\_ASYNCH10\_PC3](#a4285722719da53788c48b4fc1f563e78)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x3) |
| #define | [PRS0\_ASYNCH10\_PC4](#a5fde4317aee5f5e514d31b0a02013e85)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x4) |
| #define | [PRS0\_ASYNCH10\_PC5](#ac3e04e87a2e22a0e5852c25cd42f5bfd)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x5) |
| #define | [PRS0\_ASYNCH10\_PC6](#a112632637b58df9fa0b0f1a4090f4360)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x6) |
| #define | [PRS0\_ASYNCH10\_PC7](#abe1145f2e2eb3620f7329a03e66f0a5b)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x7) |
| #define | [PRS0\_ASYNCH10\_PC8](#ac322660bf45aae79d9dfc97d4855ab61)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x8) |
| #define | [PRS0\_ASYNCH10\_PC9](#a194bca6a084988c323ae32c17ad9e148)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x9) |
| #define | [PRS0\_ASYNCH10\_PD0](#a86d5340c5133d3193351104663683d0e)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x3, 0x0) |
| #define | [PRS0\_ASYNCH10\_PD1](#a00af6bec878e4ea3f6ff297ac35f91ed)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x3, 0x1) |
| #define | [PRS0\_ASYNCH10\_PD2](#a0117d03759e58b8a40f3e32e65c1daff)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x3, 0x2) |
| #define | [PRS0\_ASYNCH10\_PD3](#ac26c97f76181aa0d4d334061599e549b)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x3, 0x3) |
| #define | [PRS0\_ASYNCH10\_PD4](#a56d5659d935d78961dd5ab8f56af296b)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x3, 0x4) |
| #define | [PRS0\_ASYNCH10\_PD5](#aa527f2dea4ccab311915bcd310ae062f)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x3, 0x5) |
| #define | [PRS0\_ASYNCH11\_PC0](#a1ba16c8c6da7e3129c03eb546df4c993)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x0) |
| #define | [PRS0\_ASYNCH11\_PC1](#a4780077af0f3eac79ac458382dfdd9ce)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x1) |
| #define | [PRS0\_ASYNCH11\_PC2](#a32ed7a6cd5db3336ee370d6cf9d8e989)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x2) |
| #define | [PRS0\_ASYNCH11\_PC3](#ada09802928473e1a5360709b259ce87e)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x3) |
| #define | [PRS0\_ASYNCH11\_PC4](#aa83823870ce109c570db56a0d7bf4197)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x4) |
| #define | [PRS0\_ASYNCH11\_PC5](#a06db00a9ba09d6f16e8ab4423b98edb8)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x5) |
| #define | [PRS0\_ASYNCH11\_PC6](#abf891c76454cd7dcccf81062e03e49c0)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x6) |
| #define | [PRS0\_ASYNCH11\_PC7](#ac19cc8092d5117eac5d57e0b9ef75408)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x7) |
| #define | [PRS0\_ASYNCH11\_PC8](#a110c98c7774b500a68ec08d99654812a)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x8) |
| #define | [PRS0\_ASYNCH11\_PC9](#a56db9c74fb03262f83f575b15e6041ba)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x9) |
| #define | [PRS0\_ASYNCH11\_PD0](#a4d64f2e728e07b761372b682a6732ea9)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x3, 0x0) |
| #define | [PRS0\_ASYNCH11\_PD1](#aa62c6365ff4d4c6e9ac8952c9bc50d1d)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x3, 0x1) |
| #define | [PRS0\_ASYNCH11\_PD2](#a6d8321e7ba25db410748817cd169d45a)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x3, 0x2) |
| #define | [PRS0\_ASYNCH11\_PD3](#aafe8d7f49fead257b9a5065f68727c1a)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x3, 0x3) |
| #define | [PRS0\_ASYNCH11\_PD4](#a8e5caa0af696c8dc3445350a1f11cf45)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x3, 0x4) |
| #define | [PRS0\_ASYNCH11\_PD5](#a09b6b220b72d01845d9e5ebf17f7d07a)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x3, 0x5) |
| #define | [PRS0\_ASYNCH12\_PA0](#a10aacd21afb9491740ad75536204af47)   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x0) |
| #define | [PRS0\_ASYNCH12\_PA1](#a0f5547f8b6e433bb489d3802cc2f54ee)   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x1) |
| #define | [PRS0\_ASYNCH12\_PA2](#a8c7c23cb0e9bfe0d3abbbfb4647c619f)   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x2) |
| #define | [PRS0\_ASYNCH12\_PA3](#a0a0ab32d5093e5ec80f9bbbabcaccecb)   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x3) |
| #define | [PRS0\_ASYNCH12\_PA4](#a07610c348913142d48f24cbf80748159)   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x4) |
| #define | [PRS0\_ASYNCH12\_PA5](#a91ed32dc798b252b2117e8c84fc26631)   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x5) |
| #define | [PRS0\_ASYNCH12\_PA6](#a272eed302053d41c214077eee7b64720)   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x6) |
| #define | [PRS0\_ASYNCH12\_PA7](#ae90459802859961117786b795abdfb59)   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x7) |
| #define | [PRS0\_ASYNCH12\_PA8](#a3c1b4709507d6b1f400f749b052cc91e)   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x8) |
| #define | [PRS0\_ASYNCH12\_PA9](#af2fd8d924c3441d1018d8570858d0def)   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x9) |
| #define | [PRS0\_ASYNCH12\_PB0](#ab83cbe92b306386bbb4407065dfadcc5)   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x1, 0x0) |
| #define | [PRS0\_ASYNCH12\_PB1](#a921c83b51c6c31b46c62858f3be92c02)   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x1, 0x1) |
| #define | [PRS0\_ASYNCH12\_PB2](#abf3db716f8c5dbfebbf271206a405ba4)   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x1, 0x2) |
| #define | [PRS0\_ASYNCH12\_PB3](#a1f17a507786154e23b1741d0262aa504)   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x1, 0x3) |
| #define | [PRS0\_ASYNCH12\_PB4](#a797d2617d88745b9ab6536e80c76b1c8)   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x1, 0x4) |
| #define | [PRS0\_ASYNCH12\_PB5](#a449120ce58891824a1372319bd857932)   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x1, 0x5) |
| #define | [PRS0\_ASYNCH13\_PA0](#a550ee44aff84f53b7f368cc358222569)   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x0) |
| #define | [PRS0\_ASYNCH13\_PA1](#a6b3b72ec6c37a633e858555be9d741cb)   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x1) |
| #define | [PRS0\_ASYNCH13\_PA2](#a305b6d5056b0caabf68ed88a5a053a97)   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x2) |
| #define | [PRS0\_ASYNCH13\_PA3](#af98fa87e2143f31dffe610a72a06d3d7)   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x3) |
| #define | [PRS0\_ASYNCH13\_PA4](#ab8ccfba67837dde10457210e5f1c297a)   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x4) |
| #define | [PRS0\_ASYNCH13\_PA5](#aa7d5640b3bd5a0d4d2467ec3ce9abdcb)   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x5) |
| #define | [PRS0\_ASYNCH13\_PA6](#a0906b42ac77f924116d258c7a769b685)   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x6) |
| #define | [PRS0\_ASYNCH13\_PA7](#a9e74ccf92743c1b61335148b3a98cd77)   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x7) |
| #define | [PRS0\_ASYNCH13\_PA8](#adc726e9153975c1786f436ca7ddd0474)   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x8) |
| #define | [PRS0\_ASYNCH13\_PA9](#a41887405f8190f76c720346e87ea2b74)   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x9) |
| #define | [PRS0\_ASYNCH13\_PB0](#a9969cb5e529162e9a1a3fd5f30d478d5)   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x1, 0x0) |
| #define | [PRS0\_ASYNCH13\_PB1](#ac63069b8115b299ae6bb625644a245db)   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x1, 0x1) |
| #define | [PRS0\_ASYNCH13\_PB2](#aba2942821c775b1b2682b0ec06e43d87)   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x1, 0x2) |
| #define | [PRS0\_ASYNCH13\_PB3](#a09eccaaa1fd092b0a95cb50ee5ef3cd3)   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x1, 0x3) |
| #define | [PRS0\_ASYNCH13\_PB4](#a6542baa6e14878b554061e2e99dd0006)   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x1, 0x4) |
| #define | [PRS0\_ASYNCH13\_PB5](#a10907dbd3b54c45e60b98c394c9a10b7)   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x1, 0x5) |
| #define | [PRS0\_ASYNCH14\_PA0](#a73fcba463211ef0886a60b7414b59c6f)   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x0) |
| #define | [PRS0\_ASYNCH14\_PA1](#a78c2478d7e52c12eac37098b4bf8f7f6)   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x1) |
| #define | [PRS0\_ASYNCH14\_PA2](#ad37be4d15fc3753f4025897dc9d99cd9)   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x2) |
| #define | [PRS0\_ASYNCH14\_PA3](#a5412d1e5a08b3d1157ce3d190414e4cd)   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x3) |
| #define | [PRS0\_ASYNCH14\_PA4](#acf062f80109a4dd8cd9b91a9b7322743)   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x4) |
| #define | [PRS0\_ASYNCH14\_PA5](#a989a7b01e77cb258df5882957c813d2f)   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x5) |
| #define | [PRS0\_ASYNCH14\_PA6](#a220f5415ec1ccc603b97d22d80a654f2)   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x6) |
| #define | [PRS0\_ASYNCH14\_PA7](#af68b224ede411b9145e953af0619d32a)   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x7) |
| #define | [PRS0\_ASYNCH14\_PA8](#ac7e7a030a8fc81faddffdcd77f66707b)   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x8) |
| #define | [PRS0\_ASYNCH14\_PA9](#afbb45b1487696d98f875f4a168a485e5)   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x9) |
| #define | [PRS0\_ASYNCH14\_PB0](#a425101e0c4768eb96759828051fdbce6)   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x1, 0x0) |
| #define | [PRS0\_ASYNCH14\_PB1](#a7c9726953c4d6948ad020828ebf99f4e)   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x1, 0x1) |
| #define | [PRS0\_ASYNCH14\_PB2](#aadbdd407c7067db273e38512b1d7d2a5)   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x1, 0x2) |
| #define | [PRS0\_ASYNCH14\_PB3](#a3f3d95d09d7ee0abb27fbfbfc33c3398)   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x1, 0x3) |
| #define | [PRS0\_ASYNCH14\_PB4](#ab41d1ee71db4b2f716586c42e26ce0c0)   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x1, 0x4) |
| #define | [PRS0\_ASYNCH14\_PB5](#ab3f36548a4f6c955344567dcd6176c69)   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x1, 0x5) |
| #define | [PRS0\_ASYNCH15\_PA0](#a1c4013acfa21c77182df39165729a351)   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x0) |
| #define | [PRS0\_ASYNCH15\_PA1](#a2a2ee681ddbc8967b87e3060c7f41adb)   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x1) |
| #define | [PRS0\_ASYNCH15\_PA2](#a47b6621fc06df0a7ca9d3e7f6a694950)   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x2) |
| #define | [PRS0\_ASYNCH15\_PA3](#abaa53f0e9ad81a391406459411e68bae)   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x3) |
| #define | [PRS0\_ASYNCH15\_PA4](#a2e273906005064680a1682fc7af9ed46)   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x4) |
| #define | [PRS0\_ASYNCH15\_PA5](#ae5520676b7309658fd3c98e3fab0a94b)   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x5) |
| #define | [PRS0\_ASYNCH15\_PA6](#a2e1dd8e0287f670aaae04eeee24d2900)   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x6) |
| #define | [PRS0\_ASYNCH15\_PA7](#aa9f87aa222cbf925208efdc1dbb993fc)   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x7) |
| #define | [PRS0\_ASYNCH15\_PA8](#a44bb6cf5cf586aee06ad5355cbcc4d92)   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x8) |
| #define | [PRS0\_ASYNCH15\_PA9](#a99a844d50090c54d2a74f6fcd3714b3c)   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x9) |
| #define | [PRS0\_ASYNCH15\_PB0](#ab67d37a6ae0ff2fd14f3f7805cbae585)   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x1, 0x0) |
| #define | [PRS0\_ASYNCH15\_PB1](#a41a6ff0b05882aa37aed79ea693a26bf)   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x1, 0x1) |
| #define | [PRS0\_ASYNCH15\_PB2](#aea795286053e3cd00be0a2ec5fa2125d)   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x1, 0x2) |
| #define | [PRS0\_ASYNCH15\_PB3](#af4ef7cc6eb3c8dc0bf191f87b3689d36)   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x1, 0x3) |
| #define | [PRS0\_ASYNCH15\_PB4](#a6e7505cfce669cf337cad3a06409a9ed)   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x1, 0x4) |
| #define | [PRS0\_ASYNCH15\_PB5](#a993a29e36de209eabac71d2fa3b581f8)   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x1, 0x5) |
| #define | [PRS0\_SYNCH0\_PA0](#a2c5a579f02ffd8ca34ce4f12cb30c8f0)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x0) |
| #define | [PRS0\_SYNCH0\_PA1](#a5f853596173978c14b0b85059afa8a5a)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x1) |
| #define | [PRS0\_SYNCH0\_PA2](#a7c8f6f55ba3e60c6a160f83f324442f0)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x2) |
| #define | [PRS0\_SYNCH0\_PA3](#a8b8697e5c71b52686ea68726a1c033dd)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x3) |
| #define | [PRS0\_SYNCH0\_PA4](#a509796448ccd2509eeb7fbf9b4432267)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x4) |
| #define | [PRS0\_SYNCH0\_PA5](#afd80bdbc61c9bddb37851b1c9b7b6fa6)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x5) |
| #define | [PRS0\_SYNCH0\_PA6](#abd86045f5ef93089158a28dd7f3aa4c2)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x6) |
| #define | [PRS0\_SYNCH0\_PA7](#ae4f987b0bca7d9d9b12a61f99cec5262)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x7) |
| #define | [PRS0\_SYNCH0\_PA8](#a9158c2302ee19ed733f624dea5b4b39a)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x8) |
| #define | [PRS0\_SYNCH0\_PA9](#aac770fa7d69626ab2575cf1144757e13)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x9) |
| #define | [PRS0\_SYNCH0\_PB0](#a736a7ad4a31b1d6dc0c548d628da9d97)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x1, 0x0) |
| #define | [PRS0\_SYNCH0\_PB1](#a10e121857131802c71c42f1fbad81970)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x1, 0x1) |
| #define | [PRS0\_SYNCH0\_PB2](#a73be353f9ce6f94984b0e1c804c97e07)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x1, 0x2) |
| #define | [PRS0\_SYNCH0\_PB3](#acd5b4f55607cae70abe6fb9e6b361f53)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x1, 0x3) |
| #define | [PRS0\_SYNCH0\_PB4](#a9e5fc4aa547c95e8dc34bb89c384a35f)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x1, 0x4) |
| #define | [PRS0\_SYNCH0\_PB5](#ac2ff0fc249cc517d39917aced695b58e)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x1, 0x5) |
| #define | [PRS0\_SYNCH0\_PC0](#aed0f68fd0e4029e96d08fb24876f88b5)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x0) |
| #define | [PRS0\_SYNCH0\_PC1](#ae52c949f3917be619b0f5f2365c2e8ba)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x1) |
| #define | [PRS0\_SYNCH0\_PC2](#aac10f668835b732d019a50c3cfc47e37)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x2) |
| #define | [PRS0\_SYNCH0\_PC3](#aa9c52d637e33202df2ace78c13c9555f)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x3) |
| #define | [PRS0\_SYNCH0\_PC4](#adcaec5a2fb5dd33e72e486587daa1f4e)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x4) |
| #define | [PRS0\_SYNCH0\_PC5](#aebbdc8a0ced784325db8374db6a1f16c)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x5) |
| #define | [PRS0\_SYNCH0\_PC6](#aedadba37735c1e29b357461908d0c22f)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x6) |
| #define | [PRS0\_SYNCH0\_PC7](#a0b2e975e8a9e48c1e0b64d10b0d4776f)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x7) |
| #define | [PRS0\_SYNCH0\_PC8](#ad35c7c7af4263b200a8761baa45ec6f1)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x8) |
| #define | [PRS0\_SYNCH0\_PC9](#abd7d76599d153aa57da78a12e5854caf)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x9) |
| #define | [PRS0\_SYNCH0\_PD0](#a5f8dea11049e64bae1e4e27baf9e1b31)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x3, 0x0) |
| #define | [PRS0\_SYNCH0\_PD1](#a27144719fce957df87cb1434bd78c53b)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x3, 0x1) |
| #define | [PRS0\_SYNCH0\_PD2](#a014112c01a441ca65ee77b693e22bcf5)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x3, 0x2) |
| #define | [PRS0\_SYNCH0\_PD3](#a9ace1d40d2d50bc683ef0c57cc7863e0)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x3, 0x3) |
| #define | [PRS0\_SYNCH0\_PD4](#aade7486bb4853a67abea630973058c25)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x3, 0x4) |
| #define | [PRS0\_SYNCH0\_PD5](#afd5f1e060b3c0836c7de21742af8ab7f)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x3, 0x5) |
| #define | [PRS0\_SYNCH1\_PA0](#adedbd9cd1918a6d9543c886660eced9d)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x0) |
| #define | [PRS0\_SYNCH1\_PA1](#a1083f73ff99ca1b3bf4446081e2addd7)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x1) |
| #define | [PRS0\_SYNCH1\_PA2](#a1ea1179bbedea21d7d5ba85c489b88e1)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x2) |
| #define | [PRS0\_SYNCH1\_PA3](#a18fe9b252631cc7ba936c99d6206294c)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x3) |
| #define | [PRS0\_SYNCH1\_PA4](#ae5b32510b0bfea666dfb424ecad5e926)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x4) |
| #define | [PRS0\_SYNCH1\_PA5](#a990491e0b9b76fc29c692ab11429d1bf)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x5) |
| #define | [PRS0\_SYNCH1\_PA6](#accd2f4d5864cea8337d9436d6f946f2d)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x6) |
| #define | [PRS0\_SYNCH1\_PA7](#aceb6e7687dc5a74ba0da121a26529409)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x7) |
| #define | [PRS0\_SYNCH1\_PA8](#ab59c19f19a428b50ddf674bd46c4e07f)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x8) |
| #define | [PRS0\_SYNCH1\_PA9](#a26cdef2fd84b7a927495c690a69837e1)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x9) |
| #define | [PRS0\_SYNCH1\_PB0](#aa19c3a0e0e8ce1868f1a89f7bd2e703a)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x1, 0x0) |
| #define | [PRS0\_SYNCH1\_PB1](#ab5cf7a7aacec81e75db1643c99958fa3)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x1, 0x1) |
| #define | [PRS0\_SYNCH1\_PB2](#a7487f16738d5b7fa4b19224e4eeab36d)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x1, 0x2) |
| #define | [PRS0\_SYNCH1\_PB3](#aaff1a467a07bc3301c63667057cb4b2d)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x1, 0x3) |
| #define | [PRS0\_SYNCH1\_PB4](#a167f92235a6d97f9ecd421e65b18e7f7)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x1, 0x4) |
| #define | [PRS0\_SYNCH1\_PB5](#abfd339a1a42f0672089fcf249b24f51b)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x1, 0x5) |
| #define | [PRS0\_SYNCH1\_PC0](#ab3036a275379a79acb9c9186172036be)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x0) |
| #define | [PRS0\_SYNCH1\_PC1](#ae726abd2298409738d8deba2708508be)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x1) |
| #define | [PRS0\_SYNCH1\_PC2](#a9aec203bbc1ecd06760f7262a53c2b3e)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x2) |
| #define | [PRS0\_SYNCH1\_PC3](#a87e88cfd739e57c6b2832ddc579e9007)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x3) |
| #define | [PRS0\_SYNCH1\_PC4](#a5ff140aeb080678501e5a49e5a17238e)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x4) |
| #define | [PRS0\_SYNCH1\_PC5](#ad4e38b8812f7c0d4a071c56033ea29b6)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x5) |
| #define | [PRS0\_SYNCH1\_PC6](#ae5fd5f17e4c57e6d27e4771b9d697412)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x6) |
| #define | [PRS0\_SYNCH1\_PC7](#a73df027a983ad91140837b7823cf457b)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x7) |
| #define | [PRS0\_SYNCH1\_PC8](#ae291d2ca20075eb4c69c212bef91dd64)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x8) |
| #define | [PRS0\_SYNCH1\_PC9](#a56124bf24e9a29162e498f308de783f7)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x9) |
| #define | [PRS0\_SYNCH1\_PD0](#ac3d3b0681c6f881fdf67d75330d2ad15)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x3, 0x0) |
| #define | [PRS0\_SYNCH1\_PD1](#a856e585175b99140059f56bbb485002c)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x3, 0x1) |
| #define | [PRS0\_SYNCH1\_PD2](#a40bd508ace349e81a5d0c155ca89970d)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x3, 0x2) |
| #define | [PRS0\_SYNCH1\_PD3](#a0619050cb1a04b75b610788e2de0390e)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x3, 0x3) |
| #define | [PRS0\_SYNCH1\_PD4](#a9a804e3cdb2e284489233d28577e1fc4)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x3, 0x4) |
| #define | [PRS0\_SYNCH1\_PD5](#a23abf1b2534882338fc00f11be349d01)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x3, 0x5) |
| #define | [PRS0\_SYNCH2\_PA0](#a30eedcbcb9ef6aa04facebe8e1cc1093)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x0) |
| #define | [PRS0\_SYNCH2\_PA1](#a8ec3379386547e7712ad3c900ec6814c)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x1) |
| #define | [PRS0\_SYNCH2\_PA2](#a770727e399810443ff27f6a2023c65ee)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x2) |
| #define | [PRS0\_SYNCH2\_PA3](#afa5e0ddfe140d74f0dd76d8e7edda691)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x3) |
| #define | [PRS0\_SYNCH2\_PA4](#a2cf89814fec476f61882164cdf99b537)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x4) |
| #define | [PRS0\_SYNCH2\_PA5](#a8a48ec9e994929feacba66e0509ad3e1)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x5) |
| #define | [PRS0\_SYNCH2\_PA6](#a117da23bb4f9f0aa2110437ffefc365a)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x6) |
| #define | [PRS0\_SYNCH2\_PA7](#a08847c5400ec84819a9b68b2c61bb501)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x7) |
| #define | [PRS0\_SYNCH2\_PA8](#ac874a823e48f1cce54ed84337b174833)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x8) |
| #define | [PRS0\_SYNCH2\_PA9](#a6a7f96cb800833e9fbe8172b48de42a4)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x9) |
| #define | [PRS0\_SYNCH2\_PB0](#a3246953945006183dfbc3b12a5e86d61)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x1, 0x0) |
| #define | [PRS0\_SYNCH2\_PB1](#a0dec289423a72a3226f883db9921b0b2)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x1, 0x1) |
| #define | [PRS0\_SYNCH2\_PB2](#a5c36bbbb8c205c06b05cb1786f91f34f)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x1, 0x2) |
| #define | [PRS0\_SYNCH2\_PB3](#a4e5c98830a60d5e00602e4e7f4348b6f)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x1, 0x3) |
| #define | [PRS0\_SYNCH2\_PB4](#aa06a6017287b483a4a47b128043b7217)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x1, 0x4) |
| #define | [PRS0\_SYNCH2\_PB5](#acbc14c00c46035fea317e32213d6c2c3)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x1, 0x5) |
| #define | [PRS0\_SYNCH2\_PC0](#ac9ab782f8cda90916bd9cb751753144a)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x0) |
| #define | [PRS0\_SYNCH2\_PC1](#a71fb98a3d5355af02d2c46d69c7f6edc)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x1) |
| #define | [PRS0\_SYNCH2\_PC2](#a50b30cf886dedec9e7cd761d9596d7f6)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x2) |
| #define | [PRS0\_SYNCH2\_PC3](#ab8725b1678b453d17551cf0daea10f57)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x3) |
| #define | [PRS0\_SYNCH2\_PC4](#a012f52b7a7cc4babe7f8e14b27125790)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x4) |
| #define | [PRS0\_SYNCH2\_PC5](#a5ce775779214b9341aede3162d4e381a)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x5) |
| #define | [PRS0\_SYNCH2\_PC6](#a151b6197cf1bb336dcdecf41cfdc90fc)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x6) |
| #define | [PRS0\_SYNCH2\_PC7](#a49b69f4a2a409147dec4247b891e2d0e)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x7) |
| #define | [PRS0\_SYNCH2\_PC8](#ae7703f340b5da2fba4e1269049d21119)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x8) |
| #define | [PRS0\_SYNCH2\_PC9](#a96c416b5297ffd7e7ddeed55f31c658c)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x9) |
| #define | [PRS0\_SYNCH2\_PD0](#af8c37706e65ff4f9f6f90f01ce507040)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x3, 0x0) |
| #define | [PRS0\_SYNCH2\_PD1](#ac83a6c15c88a8662ce8b9ba58d60772a)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x3, 0x1) |
| #define | [PRS0\_SYNCH2\_PD2](#ad8d312030ac50620b851c24cfb90b8c0)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x3, 0x2) |
| #define | [PRS0\_SYNCH2\_PD3](#a3462ed2558a059ff7b2c81471bb30adf)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x3, 0x3) |
| #define | [PRS0\_SYNCH2\_PD4](#a98dc3a73329ab25a00dd293e05c8ebeb)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x3, 0x4) |
| #define | [PRS0\_SYNCH2\_PD5](#a8ff5ea4512864a5ae3c26341d7a8c8f9)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x3, 0x5) |
| #define | [PRS0\_SYNCH3\_PA0](#a3d8a4990b1f1b2c03152d2d0ee88afc3)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x0) |
| #define | [PRS0\_SYNCH3\_PA1](#a13b0ade04e1c64d1438afe98588fe2d2)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x1) |
| #define | [PRS0\_SYNCH3\_PA2](#a270b6759ebfa8c61efefbc57fa10b3a3)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x2) |
| #define | [PRS0\_SYNCH3\_PA3](#a6d223baeec1045d533966d37adeaa1fd)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x3) |
| #define | [PRS0\_SYNCH3\_PA4](#a0e17834640a0fa86e9cc0d166b41051e)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x4) |
| #define | [PRS0\_SYNCH3\_PA5](#a49a035319ad597aca7e0fcfa1abd0f01)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x5) |
| #define | [PRS0\_SYNCH3\_PA6](#a13e3aaaec3efb457103bb8159cb4de31)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x6) |
| #define | [PRS0\_SYNCH3\_PA7](#aad295ab8444f14fd8a7f01225d8d028d)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x7) |
| #define | [PRS0\_SYNCH3\_PA8](#a1ee67f1e40e56d7ce7b6e2dfc3c6d60d)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x8) |
| #define | [PRS0\_SYNCH3\_PA9](#ab895d6126fa54fb4878597a945f74dec)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x9) |
| #define | [PRS0\_SYNCH3\_PB0](#ab17a4fca8c86667da92478553626bba6)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x1, 0x0) |
| #define | [PRS0\_SYNCH3\_PB1](#a88fff8ac2df69413d6fddc5ec152e31b)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x1, 0x1) |
| #define | [PRS0\_SYNCH3\_PB2](#ae56538fc7c8d0ca774ed366e51675230)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x1, 0x2) |
| #define | [PRS0\_SYNCH3\_PB3](#acc237ffc92de8a4b0003dd9f7e09c690)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x1, 0x3) |
| #define | [PRS0\_SYNCH3\_PB4](#a1579ef24d96f575092d727d1ea82af8e)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x1, 0x4) |
| #define | [PRS0\_SYNCH3\_PB5](#a3d08c5cfdb1e23bcd9de7f5b4c941aa0)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x1, 0x5) |
| #define | [PRS0\_SYNCH3\_PC0](#a5b3ca0959f268e1977ab4fcb0333b282)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x0) |
| #define | [PRS0\_SYNCH3\_PC1](#a322705abcca1fb83fdffcf16252c35d4)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x1) |
| #define | [PRS0\_SYNCH3\_PC2](#ad45be94cb4581dbc5c9474d2da892aa0)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x2) |
| #define | [PRS0\_SYNCH3\_PC3](#af541dc086b57060761678fba2145d5fc)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x3) |
| #define | [PRS0\_SYNCH3\_PC4](#aa8cc93aafe5498f4cc5a26d1fa37599e)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x4) |
| #define | [PRS0\_SYNCH3\_PC5](#a05496c3ac6cbd4310245f30c0810afbe)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x5) |
| #define | [PRS0\_SYNCH3\_PC6](#a6f198140e1506fd09800ff26f6223823)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x6) |
| #define | [PRS0\_SYNCH3\_PC7](#aedd84533e1397a94ca85f73644083d7d)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x7) |
| #define | [PRS0\_SYNCH3\_PC8](#ac149001c5cf25e43d4a72627b0f7168a)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x8) |
| #define | [PRS0\_SYNCH3\_PC9](#a5edaed4c458260db93f6a7190aed2375)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x9) |
| #define | [PRS0\_SYNCH3\_PD0](#a028ffbfde62bf2f28a08c99884d6fbb6)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x3, 0x0) |
| #define | [PRS0\_SYNCH3\_PD1](#a0d0ee2b67b86c4b2615f24e673966465)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x3, 0x1) |
| #define | [PRS0\_SYNCH3\_PD2](#a8dc61e39bff0c335982b5a775c9b000c)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x3, 0x2) |
| #define | [PRS0\_SYNCH3\_PD3](#a10deabf90e836f5bd478ad2a6483d2c8)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x3, 0x3) |
| #define | [PRS0\_SYNCH3\_PD4](#abf691edac97faf842650ff032300c7f2)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x3, 0x4) |
| #define | [PRS0\_SYNCH3\_PD5](#a89dcc2c57c15a6304f9e512b8fa7ae17)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x3, 0x5) |
| #define | [HFXO0\_BUFOUTREQINASYNC\_PA0](#af3d9d425c19fc9f1c56b16a2ce3ca69b)   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x0) |
| #define | [HFXO0\_BUFOUTREQINASYNC\_PA1](#ae0120388287c3f60a6190eda52121f0e)   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x1) |
| #define | [HFXO0\_BUFOUTREQINASYNC\_PA2](#af4852125e31ddddd1fed1fdacf153e02)   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x2) |
| #define | [HFXO0\_BUFOUTREQINASYNC\_PA3](#a25681d36b593b30263243a6cc5a319b1)   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x3) |
| #define | [HFXO0\_BUFOUTREQINASYNC\_PA4](#a25093f4fd8152b2a499f78117b860d0c)   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x4) |
| #define | [HFXO0\_BUFOUTREQINASYNC\_PA5](#aa6ce87ffb49361ab8876afa308d75777)   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x5) |
| #define | [HFXO0\_BUFOUTREQINASYNC\_PA6](#ae0b89336110416cebaa0a1e899daa562)   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x6) |
| #define | [HFXO0\_BUFOUTREQINASYNC\_PA7](#a4fe6a622e71c24bd3203fcb7f1ee0037)   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x7) |
| #define | [HFXO0\_BUFOUTREQINASYNC\_PA8](#a26c5fbf9b20f95ea89a36640e4cad757)   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x8) |
| #define | [HFXO0\_BUFOUTREQINASYNC\_PA9](#a35a6e2e7cf644a3b80df8d1739ef35da)   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x9) |
| #define | [HFXO0\_BUFOUTREQINASYNC\_PB0](#adc4fb29901bb4530d24f18598041e248)   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x1, 0x0) |
| #define | [HFXO0\_BUFOUTREQINASYNC\_PB1](#a30174f1bc16727689379ce617ffa2696)   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x1, 0x1) |
| #define | [HFXO0\_BUFOUTREQINASYNC\_PB2](#aca249022c7464cf1062124bd3ab7d399)   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x1, 0x2) |
| #define | [HFXO0\_BUFOUTREQINASYNC\_PB3](#a0b069b62a4387a9819b03652bf123130)   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x1, 0x3) |
| #define | [HFXO0\_BUFOUTREQINASYNC\_PB4](#a3959e7648de41ada54851249af0e776f)   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x1, 0x4) |
| #define | [HFXO0\_BUFOUTREQINASYNC\_PB5](#aacf5c309e16b253413b98de57e5640ba)   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x1, 0x5) |
| #define | [TIMER0\_CC0\_PA0](#a643451fe929eaf497b28b23570152dfa)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x0) |
| #define | [TIMER0\_CC0\_PA1](#a257ab281a2a05ec0cc41ad2e3b548dfb)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x1) |
| #define | [TIMER0\_CC0\_PA2](#a1382ce3a810d4e7056919091fe9514f5)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x2) |
| #define | [TIMER0\_CC0\_PA3](#a9a9109ad50309f2200302915ea5a2654)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x3) |
| #define | [TIMER0\_CC0\_PA4](#a035c1f38daa2aca747ced020035bd292)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x4) |
| #define | [TIMER0\_CC0\_PA5](#a4bfcb9dec6df42cdf9a1fe979354ae57)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x5) |
| #define | [TIMER0\_CC0\_PA6](#ad1a677a1839ff4de6cc82e6e17b5aae2)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x6) |
| #define | [TIMER0\_CC0\_PA7](#a83713df06a69164162a4b734434bccc5)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x7) |
| #define | [TIMER0\_CC0\_PA8](#ab20dff18cf40da11a2ebcc405819c7e8)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x8) |
| #define | [TIMER0\_CC0\_PA9](#a571a5fe0360d6539be28fa6c4fb552b5)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x9) |
| #define | [TIMER0\_CC0\_PB0](#a18fb1529d6c032c6755f3d5a0abf9c76)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x1, 0x0) |
| #define | [TIMER0\_CC0\_PB1](#adf86b7c1c4b41eaf900d8a02e912f7c2)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x1, 0x1) |
| #define | [TIMER0\_CC0\_PB2](#ab01379b7fede12eae4bf2dcd1415d360)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x1, 0x2) |
| #define | [TIMER0\_CC0\_PB3](#abad5725bf78d847e54ad1bed240eca11)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x1, 0x3) |
| #define | [TIMER0\_CC0\_PB4](#a6cac16610a7cff74400e55edd20ebc76)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x1, 0x4) |
| #define | [TIMER0\_CC0\_PB5](#ae1e296c30691bdcc024c791e02ab02a9)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x1, 0x5) |
| #define | [TIMER0\_CC0\_PC0](#af01197ecb61c8e13ed760c4f036d555f)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x0) |
| #define | [TIMER0\_CC0\_PC1](#ae82052a9a3803c36b447e75e30db22b5)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x1) |
| #define | [TIMER0\_CC0\_PC2](#a89bade3c8848eeccc253f9752b16790c)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x2) |
| #define | [TIMER0\_CC0\_PC3](#a8b2ec4704842a1824c29fba1f700292e)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x3) |
| #define | [TIMER0\_CC0\_PC4](#acd56df092cae914b4e416e932e2b9f59)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x4) |
| #define | [TIMER0\_CC0\_PC5](#a17bbebdef205a11b6021b510d62ff3b8)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x5) |
| #define | [TIMER0\_CC0\_PC6](#a183d951a3ba6704d8056c1f16658a81f)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x6) |
| #define | [TIMER0\_CC0\_PC7](#ae5baae49155bdc86220399e4c80d57e3)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x7) |
| #define | [TIMER0\_CC0\_PC8](#ab0fbe13863fbd23ca2e2a6e427bda4c7)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x8) |
| #define | [TIMER0\_CC0\_PC9](#a10493f4bdb0fd03110e1291ad8942adc)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x9) |
| #define | [TIMER0\_CC0\_PD0](#a3db86be83a2cf8932a653abbf93aed00)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x3, 0x0) |
| #define | [TIMER0\_CC0\_PD1](#a4350a7968647bb2f25b6b2637fef6ad1)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x3, 0x1) |
| #define | [TIMER0\_CC0\_PD2](#a4c8e3e5bdf2d6582e6182f3df56f606b)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x3, 0x2) |
| #define | [TIMER0\_CC0\_PD3](#a695f1eba6df77776fb45e9f69a6fd57a)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x3, 0x3) |
| #define | [TIMER0\_CC0\_PD4](#a36230412046558d27c68f98b3ad6bd17)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x3, 0x4) |
| #define | [TIMER0\_CC0\_PD5](#a81fd1dfd02ac2ca4daebf5ef99497979)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x3, 0x5) |
| #define | [TIMER0\_CC1\_PA0](#aa74131bdc087fb80e597e3d497ab9796)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x0) |
| #define | [TIMER0\_CC1\_PA1](#a4a841ee625298d042db41bc0cd385796)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x1) |
| #define | [TIMER0\_CC1\_PA2](#a69b83d879f0cb485ba4af8b3cf4844a1)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x2) |
| #define | [TIMER0\_CC1\_PA3](#a0b3cce5e9df6245edce583e307c70b7f)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x3) |
| #define | [TIMER0\_CC1\_PA4](#ae6724c9762d1a9ae311d902e930b337c)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x4) |
| #define | [TIMER0\_CC1\_PA5](#a2354f1d78e8686d9ea3c44dd9bac5b38)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x5) |
| #define | [TIMER0\_CC1\_PA6](#a1b634a95c42a9065c7307c1a13461f39)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x6) |
| #define | [TIMER0\_CC1\_PA7](#abd19b057060c325aa1fa13af9121671d)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x7) |
| #define | [TIMER0\_CC1\_PA8](#ac005d8b7842095517fc151d18aa0b649)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x8) |
| #define | [TIMER0\_CC1\_PA9](#a28fae7750ea6bbf6aebd2ff1c98827ed)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x9) |
| #define | [TIMER0\_CC1\_PB0](#a6b0f1898a3246e0dd5915d5f5014b53e)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x1, 0x0) |
| #define | [TIMER0\_CC1\_PB1](#a812c3aa15e23b7be5d70f052259722dc)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x1, 0x1) |
| #define | [TIMER0\_CC1\_PB2](#ab12ee18043cd8f1ac0050cc7f706c712)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x1, 0x2) |
| #define | [TIMER0\_CC1\_PB3](#a988e56db008ca4cfd5b6ef5072b2e78f)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x1, 0x3) |
| #define | [TIMER0\_CC1\_PB4](#ad7bf61540cbd3e042da81a14a3c7c51f)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x1, 0x4) |
| #define | [TIMER0\_CC1\_PB5](#ac2ce68f224599c5c9113185d822b07bd)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x1, 0x5) |
| #define | [TIMER0\_CC1\_PC0](#a5787f33a274113239c4f5e8abecdf9a2)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x0) |
| #define | [TIMER0\_CC1\_PC1](#a14c64ec2717df0534956326f806de22a)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x1) |
| #define | [TIMER0\_CC1\_PC2](#ad7ffea850def6f7001ed2471ce3a13b6)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x2) |
| #define | [TIMER0\_CC1\_PC3](#a3f40aa2528d1f936a0e6734c0227afb2)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x3) |
| #define | [TIMER0\_CC1\_PC4](#a72ab00cdfc58ff9f2aef06c5ee9e1e13)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x4) |
| #define | [TIMER0\_CC1\_PC5](#a7a0b8714592092cb219e214cd28da4c5)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x5) |
| #define | [TIMER0\_CC1\_PC6](#aa48fdfed86985e0415468b7488c9d38c)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x6) |
| #define | [TIMER0\_CC1\_PC7](#a29e63d266965c64f0903cc309f20cb22)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x7) |
| #define | [TIMER0\_CC1\_PC8](#aa6ea846d04a3405926cc2b9aae39ca3a)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x8) |
| #define | [TIMER0\_CC1\_PC9](#aacb2904fae1307f64016f45a4ae93adb)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x9) |
| #define | [TIMER0\_CC1\_PD0](#ad721fa41b15556e529252a63302e8320)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x3, 0x0) |
| #define | [TIMER0\_CC1\_PD1](#abdc57a8f13e515d62d84684433f4c399)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x3, 0x1) |
| #define | [TIMER0\_CC1\_PD2](#a6a00214723619c929a860d4d5fa82d70)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x3, 0x2) |
| #define | [TIMER0\_CC1\_PD3](#ab5fe2a23145e40055ae0f532309c45a4)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x3, 0x3) |
| #define | [TIMER0\_CC1\_PD4](#ad0bf7e8d2c24c8ebe7c2b594d99c9ead)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x3, 0x4) |
| #define | [TIMER0\_CC1\_PD5](#acfae72ccde9456c2300b98b14fc0c4e9)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x3, 0x5) |
| #define | [TIMER0\_CC2\_PA0](#a10518d21844ab1a787009973ac06ce22)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x0) |
| #define | [TIMER0\_CC2\_PA1](#a40b5d230cec35f97648678731d970520)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x1) |
| #define | [TIMER0\_CC2\_PA2](#a5183b3c3cec8352c11edef376fc346ad)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x2) |
| #define | [TIMER0\_CC2\_PA3](#aec173f24a643f2d50e4e2fe44b0d1dc8)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x3) |
| #define | [TIMER0\_CC2\_PA4](#a4df67f53e8e2501bed3fd9565a49c0d6)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x4) |
| #define | [TIMER0\_CC2\_PA5](#a0529c6f8022ee408363ecc6452ac2c44)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x5) |
| #define | [TIMER0\_CC2\_PA6](#a1e0f169ebf24d5954b875bd824b86de1)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x6) |
| #define | [TIMER0\_CC2\_PA7](#a59bb4e9a92765847c5c2a5173df27f1e)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x7) |
| #define | [TIMER0\_CC2\_PA8](#a4a131dbd8f75a91809fece6cba85fcc5)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x8) |
| #define | [TIMER0\_CC2\_PA9](#a2ae1d1ad9ad7658df2a0f667af493c52)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x9) |
| #define | [TIMER0\_CC2\_PB0](#ad7a7916ae90b8345be7279e50f18c190)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x1, 0x0) |
| #define | [TIMER0\_CC2\_PB1](#a36ccb83c4230c2f3d14accbb965b08cd)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x1, 0x1) |
| #define | [TIMER0\_CC2\_PB2](#ad02263c57d4f083872708a7c91ee515f)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x1, 0x2) |
| #define | [TIMER0\_CC2\_PB3](#aaeb96f9ff0dc83edf33cfef5c95430f6)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x1, 0x3) |
| #define | [TIMER0\_CC2\_PB4](#a5aa2d1d44c749859ed1f1e6e468e099e)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x1, 0x4) |
| #define | [TIMER0\_CC2\_PB5](#ac471bba7cb11d1561198d21869bcd7c5)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x1, 0x5) |
| #define | [TIMER0\_CC2\_PC0](#afe51827dd65359061f88753af6868eb5)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x0) |
| #define | [TIMER0\_CC2\_PC1](#ae3d14c1aa4739ba2be209c8490e05b9b)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x1) |
| #define | [TIMER0\_CC2\_PC2](#a12baff93c97c64f74538b1995171fab7)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x2) |
| #define | [TIMER0\_CC2\_PC3](#a96fe3aa3622573210ac344515718962f)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x3) |
| #define | [TIMER0\_CC2\_PC4](#ad70b84d782f9af43d146a34c1533f08a)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x4) |
| #define | [TIMER0\_CC2\_PC5](#a8bebf51e280fec4baea6e545ba0e8576)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x5) |
| #define | [TIMER0\_CC2\_PC6](#ab088658e226c6a3f754574378fa59fdc)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x6) |
| #define | [TIMER0\_CC2\_PC7](#a3248786ef86b22d8f8e6de854160ff6a)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x7) |
| #define | [TIMER0\_CC2\_PC8](#ab7744630c2e1590791b60272fefdfa8b)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x8) |
| #define | [TIMER0\_CC2\_PC9](#a5d487cfdd44d02257ccc3d2a02d48e72)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x9) |
| #define | [TIMER0\_CC2\_PD0](#a29a4b811b779721b8ab98976d0af976c)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x3, 0x0) |
| #define | [TIMER0\_CC2\_PD1](#a21d070a5f412c7a77e53f69c87c57997)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x3, 0x1) |
| #define | [TIMER0\_CC2\_PD2](#a419e2b988ac821a7b4e40fb925da5916)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x3, 0x2) |
| #define | [TIMER0\_CC2\_PD3](#aae16cb8df6cc099c3344c5740fd31e69)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x3, 0x3) |
| #define | [TIMER0\_CC2\_PD4](#ae97c73876fb35531996feaad9d43217f)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x3, 0x4) |
| #define | [TIMER0\_CC2\_PD5](#a012caa64d0e1ca3d85f6d0a68ea57c25)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x3, 0x5) |
| #define | [TIMER0\_CDTI0\_PA0](#a583547311775fdf98f4d19afb149ac6c)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x0) |
| #define | [TIMER0\_CDTI0\_PA1](#a8005c42773c60dd5aec6e3ee8f4b7491)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x1) |
| #define | [TIMER0\_CDTI0\_PA2](#a78955dc51203c015d86b442978ad260e)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x2) |
| #define | [TIMER0\_CDTI0\_PA3](#a291a17c15340c09f32a3c63e3da95a9c)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x3) |
| #define | [TIMER0\_CDTI0\_PA4](#ab3b70d25fa01aaade758c277465c9639)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x4) |
| #define | [TIMER0\_CDTI0\_PA5](#a025bd51e6c211605497795d76e175510)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x5) |
| #define | [TIMER0\_CDTI0\_PA6](#a17617cf4fecd500e152bc39ef84e009b)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x6) |
| #define | [TIMER0\_CDTI0\_PA7](#aee12a8ee669b0201ff7557c15b2fc6d5)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x7) |
| #define | [TIMER0\_CDTI0\_PA8](#add042bfe988b01b650b3855a407e71cf)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x8) |
| #define | [TIMER0\_CDTI0\_PA9](#a7d3dd78baac35ece4d59da8f277bb3ce)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x9) |
| #define | [TIMER0\_CDTI0\_PB0](#ac08f3bf826c3d909d06c67c2acb418ef)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x1, 0x0) |
| #define | [TIMER0\_CDTI0\_PB1](#aaf1bd6f6922c1316131edb6cb0f3de9e)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x1, 0x1) |
| #define | [TIMER0\_CDTI0\_PB2](#af8a99eb0ed525295713c0158c7c0325f)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x1, 0x2) |
| #define | [TIMER0\_CDTI0\_PB3](#addeeb5046eef54b417ce88ff5938efac)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x1, 0x3) |
| #define | [TIMER0\_CDTI0\_PB4](#a45b93c4fd05e5bf784cc1ed50162df94)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x1, 0x4) |
| #define | [TIMER0\_CDTI0\_PB5](#a4e7041a6a34a7f48464cdd161cd0ac9b)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x1, 0x5) |
| #define | [TIMER0\_CDTI0\_PC0](#a5f22a6e89d3fb5e3bb7925fdbe1c2e38)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x0) |
| #define | [TIMER0\_CDTI0\_PC1](#a72ef54f11ed78d2e16f007d394030955)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x1) |
| #define | [TIMER0\_CDTI0\_PC2](#a3f65837c636c8b483c7130555c34a54c)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x2) |
| #define | [TIMER0\_CDTI0\_PC3](#acbf891b0c24b9af901264aba00b84f64)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x3) |
| #define | [TIMER0\_CDTI0\_PC4](#adf859e578ce341428c887d8267d962bf)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x4) |
| #define | [TIMER0\_CDTI0\_PC5](#ae57392b6eb47339eb4e5bd89840d19a9)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x5) |
| #define | [TIMER0\_CDTI0\_PC6](#a5da4268d82621edce0d73e495eeaeffc)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x6) |
| #define | [TIMER0\_CDTI0\_PC7](#a18354cd70447a811e3cfeb92e6300aaf)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x7) |
| #define | [TIMER0\_CDTI0\_PC8](#a15ceb91e88d25022c336d56444eb106f)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x8) |
| #define | [TIMER0\_CDTI0\_PC9](#a9e47ff2f69c353ec76af5964c5ba70fd)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x9) |
| #define | [TIMER0\_CDTI0\_PD0](#abe060cc518151861fccab2604541e238)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x3, 0x0) |
| #define | [TIMER0\_CDTI0\_PD1](#a0925901af2c13317cf4f43c50e01d83a)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x3, 0x1) |
| #define | [TIMER0\_CDTI0\_PD2](#aed6dd4aa21be7afbe03d984356d36e32)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x3, 0x2) |
| #define | [TIMER0\_CDTI0\_PD3](#aa52d4d7a010abe242632b4574332349b)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x3, 0x3) |
| #define | [TIMER0\_CDTI0\_PD4](#ae8b70f7461db674d1d9c3f2ea91701cc)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x3, 0x4) |
| #define | [TIMER0\_CDTI0\_PD5](#aadc1f7305d8c880746d39c607414346b)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x3, 0x5) |
| #define | [TIMER0\_CDTI1\_PA0](#a757add3c35ee9b20b8bb75363620e57f)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x0) |
| #define | [TIMER0\_CDTI1\_PA1](#a39b01d816f29ff5114ac045475ad1c80)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x1) |
| #define | [TIMER0\_CDTI1\_PA2](#a648e126ee7e0bdf5faff238a097c6e5e)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x2) |
| #define | [TIMER0\_CDTI1\_PA3](#a0e36cbcf42a86fa70f9561b1a817831d)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x3) |
| #define | [TIMER0\_CDTI1\_PA4](#a12661cbedaeab2177edf943b1f752b6b)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x4) |
| #define | [TIMER0\_CDTI1\_PA5](#a9012c36cbc093ebb308af9118eabfde9)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x5) |
| #define | [TIMER0\_CDTI1\_PA6](#ac4ab807c106f7b9bc718e931d517c791)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x6) |
| #define | [TIMER0\_CDTI1\_PA7](#ada3087b05c215a2484cf068cdc1494f7)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x7) |
| #define | [TIMER0\_CDTI1\_PA8](#a5c0a03d2f318b94a19795fb40e767285)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x8) |
| #define | [TIMER0\_CDTI1\_PA9](#a63d88961b85a0fdc91f6df0ac6dbf069)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x9) |
| #define | [TIMER0\_CDTI1\_PB0](#a8b1c6a4724744e459918508925be254e)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x1, 0x0) |
| #define | [TIMER0\_CDTI1\_PB1](#a9206a9ae50fbe6a063df918f0dc7d9b5)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x1, 0x1) |
| #define | [TIMER0\_CDTI1\_PB2](#a7ca452eeecf6b0b1a6f833b5332244cf)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x1, 0x2) |
| #define | [TIMER0\_CDTI1\_PB3](#ae206d9477b7cad08f2fc30af80bc08f8)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x1, 0x3) |
| #define | [TIMER0\_CDTI1\_PB4](#ad1d178e1d6fb8768959e4b8b04ab18e3)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x1, 0x4) |
| #define | [TIMER0\_CDTI1\_PB5](#aa98d1c28a8531bfbbd82fe7bf6d9727d)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x1, 0x5) |
| #define | [TIMER0\_CDTI1\_PC0](#ad5eb7a31fde2301a819d1f7fb3fa4120)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x0) |
| #define | [TIMER0\_CDTI1\_PC1](#a67c242881dc443329a04f2148b5d3171)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x1) |
| #define | [TIMER0\_CDTI1\_PC2](#a6e61b116d02e63455d54f16e29168dfe)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x2) |
| #define | [TIMER0\_CDTI1\_PC3](#a904d89c160a99cc883673a11164eb00a)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x3) |
| #define | [TIMER0\_CDTI1\_PC4](#afa348bc98e1aa83ec82924c1c49a5970)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x4) |
| #define | [TIMER0\_CDTI1\_PC5](#a43e280a63df1054883f731736d864712)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x5) |
| #define | [TIMER0\_CDTI1\_PC6](#a7ffd35a5c906b6416b44621024daec1f)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x6) |
| #define | [TIMER0\_CDTI1\_PC7](#a7001978e8da4cd34b0da45ca39fda8f1)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x7) |
| #define | [TIMER0\_CDTI1\_PC8](#aa8259c92e23f5eabef443bde8ddc7f76)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x8) |
| #define | [TIMER0\_CDTI1\_PC9](#aaefdbc2277ffe2c275e7c77b1bfb90cf)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x9) |
| #define | [TIMER0\_CDTI1\_PD0](#a713013e442d42bf60f0f8a2df0e178de)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x3, 0x0) |
| #define | [TIMER0\_CDTI1\_PD1](#a28cc02c56e4eb397f3fc9d106db59dd3)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x3, 0x1) |
| #define | [TIMER0\_CDTI1\_PD2](#a7a3ee64de9bcf3d3e05cad7c0eb51492)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x3, 0x2) |
| #define | [TIMER0\_CDTI1\_PD3](#ac0570e1fa46ef8d9015c9e41cede4394)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x3, 0x3) |
| #define | [TIMER0\_CDTI1\_PD4](#a159917b90b0f5f1040afe53b172ca26f)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x3, 0x4) |
| #define | [TIMER0\_CDTI1\_PD5](#a13e86004fc3aa0f53c5f2b9404d46703)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x3, 0x5) |
| #define | [TIMER0\_CDTI2\_PA0](#a723140878fb318fc60e62886e8e4bb6b)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x0) |
| #define | [TIMER0\_CDTI2\_PA1](#a69ea746a21b0305be02db15ba8ced4dc)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x1) |
| #define | [TIMER0\_CDTI2\_PA2](#a63e2744f17ec7b868e38010999a5b99e)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x2) |
| #define | [TIMER0\_CDTI2\_PA3](#ad9c1f9c457c63b9f7ee15cedb89c8b29)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x3) |
| #define | [TIMER0\_CDTI2\_PA4](#ac5e02eb43bbc85c4e07976539d1c7b66)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x4) |
| #define | [TIMER0\_CDTI2\_PA5](#a17440dab813cdc7a4b58682db3c0aa3c)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x5) |
| #define | [TIMER0\_CDTI2\_PA6](#a967cbd605349c15eada5527602a05fc9)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x6) |
| #define | [TIMER0\_CDTI2\_PA7](#a3ee02bd72164f5ddab71818f5dc34616)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x7) |
| #define | [TIMER0\_CDTI2\_PA8](#a9e6862b3fbfa9272f0401ed722a7452c)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x8) |
| #define | [TIMER0\_CDTI2\_PA9](#a5e30587d905a27e406a3e5956ba0a9be)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x9) |
| #define | [TIMER0\_CDTI2\_PB0](#a4a53984105a683a6807ad0a26e13a60d)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x1, 0x0) |
| #define | [TIMER0\_CDTI2\_PB1](#a12ffd91f7201f73e0d75c2298d5abce9)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x1, 0x1) |
| #define | [TIMER0\_CDTI2\_PB2](#a211506e052690ec459d7225ac9ec2dd1)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x1, 0x2) |
| #define | [TIMER0\_CDTI2\_PB3](#a6639dc47e82cbc98ba1aae88605e8c63)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x1, 0x3) |
| #define | [TIMER0\_CDTI2\_PB4](#a3cdd0a6bcde7f01a695284e11fe5946d)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x1, 0x4) |
| #define | [TIMER0\_CDTI2\_PB5](#a8485eeaa0e92fcb4a58048b40a19d8f3)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x1, 0x5) |
| #define | [TIMER0\_CDTI2\_PC0](#a11f7ac3b39604c06f639dc4b925ee93d)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x0) |
| #define | [TIMER0\_CDTI2\_PC1](#a2b6fa7363ef650a2847113779b5b36a7)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x1) |
| #define | [TIMER0\_CDTI2\_PC2](#a3d39899e0d3f88f22feffcd6752b2507)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x2) |
| #define | [TIMER0\_CDTI2\_PC3](#a0f6d66f601b1eaeae268c7ed2b0874ae)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x3) |
| #define | [TIMER0\_CDTI2\_PC4](#ab91374950c6d3774d25c5e6ee6068ce0)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x4) |
| #define | [TIMER0\_CDTI2\_PC5](#a2c76eb69ea9ed92aa328126bbad507d1)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x5) |
| #define | [TIMER0\_CDTI2\_PC6](#abbc57fb5b68e9956483bf9122e985bf2)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x6) |
| #define | [TIMER0\_CDTI2\_PC7](#ab4ee38f2ae41e0c6dfea802960c06146)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x7) |
| #define | [TIMER0\_CDTI2\_PC8](#ac7d002926fe9a298f1dfacb69f295d3f)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x8) |
| #define | [TIMER0\_CDTI2\_PC9](#af5a9b96754b28693de2ddd05994ddd2d)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x9) |
| #define | [TIMER0\_CDTI2\_PD0](#a038cef314d102bb50e58612327d456c6)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x3, 0x0) |
| #define | [TIMER0\_CDTI2\_PD1](#a008dea92e72e9d337f5a6d38aaf33661)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x3, 0x1) |
| #define | [TIMER0\_CDTI2\_PD2](#a7bf636029c51b394d749774c4961aeba)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x3, 0x2) |
| #define | [TIMER0\_CDTI2\_PD3](#a48403324a419bb99f173f8a5198d55a0)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x3, 0x3) |
| #define | [TIMER0\_CDTI2\_PD4](#ad15de743c118e7443cf6edf793243995)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x3, 0x4) |
| #define | [TIMER0\_CDTI2\_PD5](#a77d1bf1e082a09e8fbd78e9be93f0f39)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x3, 0x5) |
| #define | [TIMER1\_CC0\_PA0](#a4b3085c41f4ed8706a3b39755e5b132c)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x0) |
| #define | [TIMER1\_CC0\_PA1](#a5daa5510f5bab9cea855b3d3303daaaf)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x1) |
| #define | [TIMER1\_CC0\_PA2](#abc2afde49650332d28db97653adc501d)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x2) |
| #define | [TIMER1\_CC0\_PA3](#a2df5bd9733330e9a973732a8cc222ee9)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x3) |
| #define | [TIMER1\_CC0\_PA4](#a514654049642c780cd7eae508e0620b9)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x4) |
| #define | [TIMER1\_CC0\_PA5](#a4dd5a3457f09f46922941de990dc9933)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x5) |
| #define | [TIMER1\_CC0\_PA6](#a13520009a8fee0808443df4d4018e0cb)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x6) |
| #define | [TIMER1\_CC0\_PA7](#ade96dcb9354b034ea97b40758e27db1d)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x7) |
| #define | [TIMER1\_CC0\_PA8](#a783d899451987bcaf749652127c1ebb4)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x8) |
| #define | [TIMER1\_CC0\_PA9](#a7d8ea431d027df42da39f6ed4f0f877e)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x9) |
| #define | [TIMER1\_CC0\_PB0](#a0cda060bbc98a77e19ed36b4d01cfec2)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x1, 0x0) |
| #define | [TIMER1\_CC0\_PB1](#ac2c9847727308a1fed2e7b21c718a92c)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x1, 0x1) |
| #define | [TIMER1\_CC0\_PB2](#a400b3582d5c7bdbbcdd6d9f101d3bf1e)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x1, 0x2) |
| #define | [TIMER1\_CC0\_PB3](#a07e5e02a684ac91a1251bcfcf18a2ff5)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x1, 0x3) |
| #define | [TIMER1\_CC0\_PB4](#ac15f3e270a2f1d2a07eaf5e3b34869a4)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x1, 0x4) |
| #define | [TIMER1\_CC0\_PB5](#a2cb498db84033c2350ebe7be68ca13f0)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x1, 0x5) |
| #define | [TIMER1\_CC0\_PC0](#a47cdc8781bd255cf8392426ab34cb042)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x0) |
| #define | [TIMER1\_CC0\_PC1](#a41a0a7812419a3a757be7899f30acfde)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x1) |
| #define | [TIMER1\_CC0\_PC2](#a322dee774195678afc5f7066d126e4c7)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x2) |
| #define | [TIMER1\_CC0\_PC3](#a458b636db4779031722ec89e4c8fc0b8)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x3) |
| #define | [TIMER1\_CC0\_PC4](#a59f20ef361658d0cc27c9694c30d2e55)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x4) |
| #define | [TIMER1\_CC0\_PC5](#a510dc66c39d8a79666d1a3d9e6c0e3ad)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x5) |
| #define | [TIMER1\_CC0\_PC6](#adcddd8bdcd941ec6e83d060d4c3cdb9e)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x6) |
| #define | [TIMER1\_CC0\_PC7](#a59678105bf2c365d44d7f138804809e9)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x7) |
| #define | [TIMER1\_CC0\_PC8](#af37a59f6bb9aed9bd57aee73f998d173)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x8) |
| #define | [TIMER1\_CC0\_PC9](#a4e4890e7da8bbb307ea0d040abca0968)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x9) |
| #define | [TIMER1\_CC0\_PD0](#aa61ecf9a9f2f6b3ce46bc96d3e3b224c)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x3, 0x0) |
| #define | [TIMER1\_CC0\_PD1](#af69bd23d5eaf09cfa8e4ac6dc815c071)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x3, 0x1) |
| #define | [TIMER1\_CC0\_PD2](#ae35d1bbefce3501c063039f88ed558a2)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x3, 0x2) |
| #define | [TIMER1\_CC0\_PD3](#a27518cd582fa2f5266da488e386783d7)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x3, 0x3) |
| #define | [TIMER1\_CC0\_PD4](#af91f86a0f39fbb4df669d036b80f97c8)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x3, 0x4) |
| #define | [TIMER1\_CC0\_PD5](#a2e26b3f9da4b70504c2fd18cb17ce829)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x3, 0x5) |
| #define | [TIMER1\_CC1\_PA0](#ab0467e6e3dafc5340b516304672d0c35)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x0) |
| #define | [TIMER1\_CC1\_PA1](#ab56f3b43b16780006b73b6b67c7fc99c)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x1) |
| #define | [TIMER1\_CC1\_PA2](#a884b7041fab46641ac127f3526d1d6aa)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x2) |
| #define | [TIMER1\_CC1\_PA3](#a97b8069d8cf397b2da2cc011e946cc97)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x3) |
| #define | [TIMER1\_CC1\_PA4](#a01aacbb9315e69096d8c64b78a49b66e)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x4) |
| #define | [TIMER1\_CC1\_PA5](#a7b12d90d7a871b5843843f20b6318fd8)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x5) |
| #define | [TIMER1\_CC1\_PA6](#ac4909134633b306a24982fd780870ff6)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x6) |
| #define | [TIMER1\_CC1\_PA7](#adfa0d8586a7e98878562b2b08bafbfe2)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x7) |
| #define | [TIMER1\_CC1\_PA8](#a30769801f476e980ed12cd966644b77d)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x8) |
| #define | [TIMER1\_CC1\_PA9](#a46cd5cc0ad78d97da58da67005509efd)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x9) |
| #define | [TIMER1\_CC1\_PB0](#a48bff42d940d3d8a4bae06df47255dca)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x1, 0x0) |
| #define | [TIMER1\_CC1\_PB1](#a72b3f2ffb3e69fa3347b782450ee1bf6)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x1, 0x1) |
| #define | [TIMER1\_CC1\_PB2](#a4a119352b728b61375f56621909c6491)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x1, 0x2) |
| #define | [TIMER1\_CC1\_PB3](#a661948aeb7bf6303f6876bad5478e9e0)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x1, 0x3) |
| #define | [TIMER1\_CC1\_PB4](#aaef1ec6432b26aa96d8ada688182fbd7)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x1, 0x4) |
| #define | [TIMER1\_CC1\_PB5](#a45f54068e0137b9ce2b69f58c6dee860)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x1, 0x5) |
| #define | [TIMER1\_CC1\_PC0](#addaacb911a618cabc51f96bec3690174)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x0) |
| #define | [TIMER1\_CC1\_PC1](#ac8fab9c34e0b1dc6f168573f34d81bba)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x1) |
| #define | [TIMER1\_CC1\_PC2](#adc420cc552323a6db6ac08b76ada22d4)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x2) |
| #define | [TIMER1\_CC1\_PC3](#a52d6b873c40ba4c37eb80089b14abf59)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x3) |
| #define | [TIMER1\_CC1\_PC4](#abb9cd68c18a6c07dc753a10471310e8d)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x4) |
| #define | [TIMER1\_CC1\_PC5](#a93aa2304008369a86392b6a98592ccac)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x5) |
| #define | [TIMER1\_CC1\_PC6](#a311a8f743e1df0e2d257ba4aa71f91a4)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x6) |
| #define | [TIMER1\_CC1\_PC7](#a24c47edc39daf607df7e6b4d37caf769)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x7) |
| #define | [TIMER1\_CC1\_PC8](#aa8eaf731dd1ce605afde974af78b6b41)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x8) |
| #define | [TIMER1\_CC1\_PC9](#acc48838987530c78b16856a3d261850c)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x9) |
| #define | [TIMER1\_CC1\_PD0](#a1294b47b68006e1da3c1bcf3afa1735b)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x3, 0x0) |
| #define | [TIMER1\_CC1\_PD1](#addf0cad7ebe2b5d0dcb15ee2860aa037)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x3, 0x1) |
| #define | [TIMER1\_CC1\_PD2](#aff68d222f67741f6d81518e502686cab)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x3, 0x2) |
| #define | [TIMER1\_CC1\_PD3](#a8a7f0101160dbc45889575bb975dcad8)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x3, 0x3) |
| #define | [TIMER1\_CC1\_PD4](#a42265ecc8251fe6745cd225fb14cae35)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x3, 0x4) |
| #define | [TIMER1\_CC1\_PD5](#ac7d88abd26fe19e66437c96e26af2598)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x3, 0x5) |
| #define | [TIMER1\_CC2\_PA0](#a8134a1d2f64747b5fd66aa6da49db081)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x0) |
| #define | [TIMER1\_CC2\_PA1](#af865342309d6355e05de4a3736e73a65)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x1) |
| #define | [TIMER1\_CC2\_PA2](#af329d80cea63f60045ea71156c4d9d6b)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x2) |
| #define | [TIMER1\_CC2\_PA3](#a1eb4626f10a12c5f6b1539fe897e0df0)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x3) |
| #define | [TIMER1\_CC2\_PA4](#abac33f1fd8502f1356107d20958e9ebb)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x4) |
| #define | [TIMER1\_CC2\_PA5](#ab1ba6969141f0ba0ed17a5e3bd6ac2d7)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x5) |
| #define | [TIMER1\_CC2\_PA6](#a46c2801cd73d8663d493fa62300a0188)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x6) |
| #define | [TIMER1\_CC2\_PA7](#a879a43e390d7a577150f00cb53ebf65c)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x7) |
| #define | [TIMER1\_CC2\_PA8](#aaf3995fdd63448a607fdb1f654c9f75b)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x8) |
| #define | [TIMER1\_CC2\_PA9](#abf299bd012798984301356e20438d3e2)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x9) |
| #define | [TIMER1\_CC2\_PB0](#ad1ba82a4e75e024cc9f19d66f691c4a1)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x1, 0x0) |
| #define | [TIMER1\_CC2\_PB1](#a4da4366632a0e029856f048d0953b6b2)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x1, 0x1) |
| #define | [TIMER1\_CC2\_PB2](#a758d4ed1cfb60bad3e5226aa3da3a250)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x1, 0x2) |
| #define | [TIMER1\_CC2\_PB3](#aec809925fc33d82ccbdc64200073bffb)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x1, 0x3) |
| #define | [TIMER1\_CC2\_PB4](#ab320f142f9af0a3bec92d8a421b3c7cb)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x1, 0x4) |
| #define | [TIMER1\_CC2\_PB5](#af62217be3c7a101fd2a681b3ed38c713)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x1, 0x5) |
| #define | [TIMER1\_CC2\_PC0](#a9d3402f1ed1c7030fb0a1af512425ae2)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x0) |
| #define | [TIMER1\_CC2\_PC1](#a939a814b29112f312ba5085449fe9b8c)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x1) |
| #define | [TIMER1\_CC2\_PC2](#a22ffd1572810e3da8a83f7cc4ccf1386)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x2) |
| #define | [TIMER1\_CC2\_PC3](#afcb1d543010489ffe23a92875fafb326)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x3) |
| #define | [TIMER1\_CC2\_PC4](#a1a34258c1ad068a3474e0114b1e3ac37)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x4) |
| #define | [TIMER1\_CC2\_PC5](#a4b3b5917e7881eeb6a191c095f0df29a)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x5) |
| #define | [TIMER1\_CC2\_PC6](#ab66a57d9d50c0f3492a4ccd7fae0a725)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x6) |
| #define | [TIMER1\_CC2\_PC7](#a46f776103efbd3d5cda86c02bd1c6ee1)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x7) |
| #define | [TIMER1\_CC2\_PC8](#a0f8c1e2acdb2423abb4f95aa1b5fe962)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x8) |
| #define | [TIMER1\_CC2\_PC9](#a63eaac923797fb8b68c08eeb4dd42ce1)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x9) |
| #define | [TIMER1\_CC2\_PD0](#a0bb950575d698e83b4a7b055928d4b02)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x3, 0x0) |
| #define | [TIMER1\_CC2\_PD1](#a9f92d850417b9d521c2c2515fbeb8c52)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x3, 0x1) |
| #define | [TIMER1\_CC2\_PD2](#ac5f369d207dbe8da77b94ed7c2ee1e89)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x3, 0x2) |
| #define | [TIMER1\_CC2\_PD3](#aa1c5e07b9ff3373d65a73b3fc916c226)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x3, 0x3) |
| #define | [TIMER1\_CC2\_PD4](#adfa6b132aa5c4c006185ebf5170aa38d)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x3, 0x4) |
| #define | [TIMER1\_CC2\_PD5](#a73affe121ba3b16a8aa04f57cc2ea053)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x3, 0x5) |
| #define | [TIMER1\_CDTI0\_PA0](#a76552704f3b8c28588c6073b170a6bbb)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x0) |
| #define | [TIMER1\_CDTI0\_PA1](#a06ea543c9f00b58b7eb4e162a7c3f427)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x1) |
| #define | [TIMER1\_CDTI0\_PA2](#ace53011f7d140ea6892946ac0d246006)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x2) |
| #define | [TIMER1\_CDTI0\_PA3](#a9b740fb70a98203b6a736fb3e3af97d1)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x3) |
| #define | [TIMER1\_CDTI0\_PA4](#adf79eddb39e5a3a28e98da92323cead4)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x4) |
| #define | [TIMER1\_CDTI0\_PA5](#a1c025b319acd53ac15e023a964b684d4)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x5) |
| #define | [TIMER1\_CDTI0\_PA6](#afed1694b73910fdb222e7ac95c7700a6)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x6) |
| #define | [TIMER1\_CDTI0\_PA7](#a16baa7d86f92039e49b2419f2c6920fe)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x7) |
| #define | [TIMER1\_CDTI0\_PA8](#a52ac2c6692f7362bef618cb7d5f0e47c)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x8) |
| #define | [TIMER1\_CDTI0\_PA9](#a5bac5b45e58c97eb8575bfa35358ec0e)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x9) |
| #define | [TIMER1\_CDTI0\_PB0](#a3f2880efd1d31b43e1fbbd840a535330)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x1, 0x0) |
| #define | [TIMER1\_CDTI0\_PB1](#a3f243ab2322faa708a8c0531a3fb15fe)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x1, 0x1) |
| #define | [TIMER1\_CDTI0\_PB2](#adf3c676ce682f3c923108b655457d517)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x1, 0x2) |
| #define | [TIMER1\_CDTI0\_PB3](#af950bfe52b44c7e24ffe22ef76719f82)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x1, 0x3) |
| #define | [TIMER1\_CDTI0\_PB4](#a9651bb0408184ebddd6b56bc0b84294c)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x1, 0x4) |
| #define | [TIMER1\_CDTI0\_PB5](#ac08854c7fbc83a84934c4dc3dfcb348e)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x1, 0x5) |
| #define | [TIMER1\_CDTI0\_PC0](#a7da42fba55aa964b5af1f0e996e10dfd)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x0) |
| #define | [TIMER1\_CDTI0\_PC1](#a90f5a73378a61a3144cb3be626acf0c3)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x1) |
| #define | [TIMER1\_CDTI0\_PC2](#ac7083129b89cd513468ea9a936cd2a60)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x2) |
| #define | [TIMER1\_CDTI0\_PC3](#ac480c190767e6bf9e64e2581617388d7)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x3) |
| #define | [TIMER1\_CDTI0\_PC4](#a80619df142e179bb585569b51f906b85)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x4) |
| #define | [TIMER1\_CDTI0\_PC5](#af24c550e1fcf0b93ca210c59884dd895)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x5) |
| #define | [TIMER1\_CDTI0\_PC6](#a6006a6fa136154c9f64c65a851a50b2a)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x6) |
| #define | [TIMER1\_CDTI0\_PC7](#af1951b25ec7b89a7dccceb94847fc37f)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x7) |
| #define | [TIMER1\_CDTI0\_PC8](#afe8f874a39e8c957bbc6491ff5b4309e)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x8) |
| #define | [TIMER1\_CDTI0\_PC9](#ab9e56e2b63c3ae33438060fe68376747)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x9) |
| #define | [TIMER1\_CDTI0\_PD0](#aeafc7272c0cf6bed9dcb09fe8802bd1f)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x3, 0x0) |
| #define | [TIMER1\_CDTI0\_PD1](#a15c83b7661113ab00fc830c832a63ad5)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x3, 0x1) |
| #define | [TIMER1\_CDTI0\_PD2](#af02751809240508c57a914bf47bc929b)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x3, 0x2) |
| #define | [TIMER1\_CDTI0\_PD3](#a36ad9aa1e2ca755919bd18f1461fd9fd)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x3, 0x3) |
| #define | [TIMER1\_CDTI0\_PD4](#a694a3359d922f9aeca292c10db75cae7)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x3, 0x4) |
| #define | [TIMER1\_CDTI0\_PD5](#ad142a654bba95812c67a92c812914604)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x3, 0x5) |
| #define | [TIMER1\_CDTI1\_PA0](#a0c90975d990014c0a70d8fe8a01bed61)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x0) |
| #define | [TIMER1\_CDTI1\_PA1](#a063202bd4d4d5c420613ccbdf41c08ac)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x1) |
| #define | [TIMER1\_CDTI1\_PA2](#a03c893bbd5151dc4bf1f08a8c197982d)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x2) |
| #define | [TIMER1\_CDTI1\_PA3](#a13fea81e86713c5839372ae17ffa5b2a)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x3) |
| #define | [TIMER1\_CDTI1\_PA4](#a3b63381e36f0f67eecdb0e613e082acd)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x4) |
| #define | [TIMER1\_CDTI1\_PA5](#ae29404facb1a5712a8d3654c32abac03)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x5) |
| #define | [TIMER1\_CDTI1\_PA6](#a041c492c18debf15659b54a4d1acda45)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x6) |
| #define | [TIMER1\_CDTI1\_PA7](#ad2a111a49ac82b431c221b9b38a7eac2)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x7) |
| #define | [TIMER1\_CDTI1\_PA8](#a61f6fe07be3fdc75f7a137652ff6180b)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x8) |
| #define | [TIMER1\_CDTI1\_PA9](#afd14a9f0b3f68baf645fdbedb8b9a636)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x9) |
| #define | [TIMER1\_CDTI1\_PB0](#afe513e7286648f7e0dfdcd5831a158cb)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x1, 0x0) |
| #define | [TIMER1\_CDTI1\_PB1](#a231c7d9bddd4e56226c51a3ca0516290)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x1, 0x1) |
| #define | [TIMER1\_CDTI1\_PB2](#a5670dfed8891e8a39a4747b6a7536fa4)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x1, 0x2) |
| #define | [TIMER1\_CDTI1\_PB3](#aef5f7b0ad2e48af91779080e32da44b4)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x1, 0x3) |
| #define | [TIMER1\_CDTI1\_PB4](#aef8297dce3f2193d4367df88ab5bf20d)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x1, 0x4) |
| #define | [TIMER1\_CDTI1\_PB5](#a8b771498d29d4f8f733a421686289f9f)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x1, 0x5) |
| #define | [TIMER1\_CDTI1\_PC0](#a26cc959057976169dd4e4a4330bb34ff)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x0) |
| #define | [TIMER1\_CDTI1\_PC1](#a5be334fd1d01d68ebc4fbf77394adc03)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x1) |
| #define | [TIMER1\_CDTI1\_PC2](#a153d9a304ad237e9f99bf2fd97cb5ca3)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x2) |
| #define | [TIMER1\_CDTI1\_PC3](#ae1d146285574814c26941837ae32cf33)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x3) |
| #define | [TIMER1\_CDTI1\_PC4](#aadc34ad6a076211bfe55a1cecba057ed)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x4) |
| #define | [TIMER1\_CDTI1\_PC5](#a89667e375454960fd56fa87fd46a1cf0)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x5) |
| #define | [TIMER1\_CDTI1\_PC6](#ad60737f6dd9fe3c6f3d5039b3da8ffa5)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x6) |
| #define | [TIMER1\_CDTI1\_PC7](#ac285ce787120af33a48a91397f7e5d59)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x7) |
| #define | [TIMER1\_CDTI1\_PC8](#a31be9bbfc736c4f10dba501580adff7c)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x8) |
| #define | [TIMER1\_CDTI1\_PC9](#abdfe1aab871eeb9c4c701f6bc8a14409)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x9) |
| #define | [TIMER1\_CDTI1\_PD0](#a9a83a5c25369e4dc286c219f9be05a08)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x3, 0x0) |
| #define | [TIMER1\_CDTI1\_PD1](#ae2d334d95e5a2f65c92562727a87520b)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x3, 0x1) |
| #define | [TIMER1\_CDTI1\_PD2](#af1a5a15c236edb1c77acce4cb8d8b894)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x3, 0x2) |
| #define | [TIMER1\_CDTI1\_PD3](#a8b00bb8a1bbb8cc97e1e1997cd5ed10b)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x3, 0x3) |
| #define | [TIMER1\_CDTI1\_PD4](#a7db403c434a33b41eefe0278890da8ca)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x3, 0x4) |
| #define | [TIMER1\_CDTI1\_PD5](#a9c8c263c15cce651e686d9f5de758be9)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x3, 0x5) |
| #define | [TIMER1\_CDTI2\_PA0](#ac959ddf75f8afe8179b53148e90a0cd3)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x0) |
| #define | [TIMER1\_CDTI2\_PA1](#a03028d392b456dbce8ce5c7325f52b87)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x1) |
| #define | [TIMER1\_CDTI2\_PA2](#a3282e1d97d899e3010b59e952aa12429)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x2) |
| #define | [TIMER1\_CDTI2\_PA3](#a249a669752eb8cfca1a9dee28e0fa5b9)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x3) |
| #define | [TIMER1\_CDTI2\_PA4](#acab3d281ca3eb0fc97c1c296beacb302)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x4) |
| #define | [TIMER1\_CDTI2\_PA5](#a1b4f4b4f2f84c99855ddfbdd829a0814)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x5) |
| #define | [TIMER1\_CDTI2\_PA6](#a4008736ae0d99019066eb6435864a043)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x6) |
| #define | [TIMER1\_CDTI2\_PA7](#ae07b3d64a4947e03736ac08ac816940f)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x7) |
| #define | [TIMER1\_CDTI2\_PA8](#a52cfa50fafa8bb77eb3d1a5b9e6c1c35)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x8) |
| #define | [TIMER1\_CDTI2\_PA9](#a4b78d1149e4b0ac25deefdf83b1d5f33)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x9) |
| #define | [TIMER1\_CDTI2\_PB0](#a4ff755a9d12285c868a4dc0e5d9de281)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x1, 0x0) |
| #define | [TIMER1\_CDTI2\_PB1](#a94cb965aa4d6a7fb7a31acbd363f54ee)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x1, 0x1) |
| #define | [TIMER1\_CDTI2\_PB2](#a2b30a5c071a113e0c7693b1723aa0534)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x1, 0x2) |
| #define | [TIMER1\_CDTI2\_PB3](#ab41614ba724866ec0e55ae0837b4dc46)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x1, 0x3) |
| #define | [TIMER1\_CDTI2\_PB4](#a1388e138cdc0a50b805b4188aed036a0)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x1, 0x4) |
| #define | [TIMER1\_CDTI2\_PB5](#aa42127e04b4c560efd4ea02ca24f7cb6)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x1, 0x5) |
| #define | [TIMER1\_CDTI2\_PC0](#ab37f717d7232493a31424e87d242c2a8)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x0) |
| #define | [TIMER1\_CDTI2\_PC1](#a6a306946717970eb62df4307de771fef)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x1) |
| #define | [TIMER1\_CDTI2\_PC2](#a248af2da57a57600d4a144c71f860006)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x2) |
| #define | [TIMER1\_CDTI2\_PC3](#ae1c48f4b069d6c7e410511b1e95a7def)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x3) |
| #define | [TIMER1\_CDTI2\_PC4](#af91af878bbab4422378cf31a711055ff)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x4) |
| #define | [TIMER1\_CDTI2\_PC5](#ac16216ae2977f9696075b3a6d8c64aa0)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x5) |
| #define | [TIMER1\_CDTI2\_PC6](#aa59451e0e343327c7c1775367c4d9194)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x6) |
| #define | [TIMER1\_CDTI2\_PC7](#a6303e70615390644193cea172c375b4a)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x7) |
| #define | [TIMER1\_CDTI2\_PC8](#ad347901cc3f14d83aba6ff02c5018a24)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x8) |
| #define | [TIMER1\_CDTI2\_PC9](#a508e041f8ca4d6b4c22609f78c867615)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x9) |
| #define | [TIMER1\_CDTI2\_PD0](#ae362330bff63d204299a6a33f4c4f191)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x3, 0x0) |
| #define | [TIMER1\_CDTI2\_PD1](#a6559a7e28febb9e31fca6847e11cdb1a)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x3, 0x1) |
| #define | [TIMER1\_CDTI2\_PD2](#a8a53201b17d025911ca41f86e3d13a66)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x3, 0x2) |
| #define | [TIMER1\_CDTI2\_PD3](#a254d9132271304cd62f61184a40471d6)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x3, 0x3) |
| #define | [TIMER1\_CDTI2\_PD4](#acf43810574237c108aba907ba113d6ba)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x3, 0x4) |
| #define | [TIMER1\_CDTI2\_PD5](#a325a0c29bdccc1bb5c9f5438b1c967e7)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x3, 0x5) |
| #define | [TIMER2\_CC0\_PA0](#a67e6f27f89e7e121cce88e0186ab5010)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x0) |
| #define | [TIMER2\_CC0\_PA1](#a545f09892c0762da7a55cdc8d16e8e6f)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x1) |
| #define | [TIMER2\_CC0\_PA2](#aee905018c0d9aa48c14e415474c03f62)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x2) |
| #define | [TIMER2\_CC0\_PA3](#ad7327f8fa42b7aa1875d2b57769330eb)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x3) |
| #define | [TIMER2\_CC0\_PA4](#acab7bd67fc01c7fa8b3c40d75f725a0a)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x4) |
| #define | [TIMER2\_CC0\_PA5](#ac846d48997b6bdbb2b7665a62a6505e3)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x5) |
| #define | [TIMER2\_CC0\_PA6](#a987c36e9761389522505ac50952ed04a)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x6) |
| #define | [TIMER2\_CC0\_PA7](#ae2170865d853ff19f2822feef4adb237)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x7) |
| #define | [TIMER2\_CC0\_PA8](#a76ee3427d6e4a4a9bba02acb045fc34c)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x8) |
| #define | [TIMER2\_CC0\_PA9](#a5e2a34f5dccec5291ae1424aba054ca6)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x9) |
| #define | [TIMER2\_CC0\_PB0](#a2a9776f698e90b570e177a6a0059b15b)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x1, 0x0) |
| #define | [TIMER2\_CC0\_PB1](#a55d9652dbf9c89d894162860c56459dd)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x1, 0x1) |
| #define | [TIMER2\_CC0\_PB2](#a0c9bb962ddacf136ff3625459e3d7671)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x1, 0x2) |
| #define | [TIMER2\_CC0\_PB3](#a738b1a7965ce7945a6123c0b97606ac5)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x1, 0x3) |
| #define | [TIMER2\_CC0\_PB4](#aa0dcc265ed171092f14a0e54e7be712d)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x1, 0x4) |
| #define | [TIMER2\_CC0\_PB5](#a965309ec5b9aa35bcf030f28d2930dcd)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x1, 0x5) |
| #define | [TIMER2\_CC1\_PA0](#a1164a4f1a0cfbf0cb157eeb7be84bd28)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x0) |
| #define | [TIMER2\_CC1\_PA1](#a1bca4d4f43da2d564d68622dcb0e5d9e)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x1) |
| #define | [TIMER2\_CC1\_PA2](#adec2ad20e72e0b8fd02b6476685f5155)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x2) |
| #define | [TIMER2\_CC1\_PA3](#a8a42dfc04580c2dba2b961509d03ff43)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x3) |
| #define | [TIMER2\_CC1\_PA4](#a89a293610575367134548bc2ccd0c47e)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x4) |
| #define | [TIMER2\_CC1\_PA5](#acdbcff934f4bac5a2b0f03a33e44138b)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x5) |
| #define | [TIMER2\_CC1\_PA6](#a4c420a0fc98b352544416bbfa8216ae6)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x6) |
| #define | [TIMER2\_CC1\_PA7](#a458c07160c2f3c3b6f12444c8f498167)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x7) |
| #define | [TIMER2\_CC1\_PA8](#ae91c030e51c7e07691257667d671d56e)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x8) |
| #define | [TIMER2\_CC1\_PA9](#a8409e21ef524a3cb805443759a3df758)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x9) |
| #define | [TIMER2\_CC1\_PB0](#ac7397d7ebe41f5c2b732bece2b63f793)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x1, 0x0) |
| #define | [TIMER2\_CC1\_PB1](#a0d597a9083a41c950f29bbbf7e148ef7)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x1, 0x1) |
| #define | [TIMER2\_CC1\_PB2](#a45aeb569507fbd649e081575c136eb4a)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x1, 0x2) |
| #define | [TIMER2\_CC1\_PB3](#afb1a90f5d59b6ce2df0a231b4c6cd75c)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x1, 0x3) |
| #define | [TIMER2\_CC1\_PB4](#a833c1470f9dec67fe7e0d7b57c0c1dee)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x1, 0x4) |
| #define | [TIMER2\_CC1\_PB5](#a3166b5021d74a953023c75c2707e5a47)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x1, 0x5) |
| #define | [TIMER2\_CC2\_PA0](#a2d62e330c22411c86274caefb099cf19)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x0) |
| #define | [TIMER2\_CC2\_PA1](#aab60fb88a625e320ce64ea10133311df)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x1) |
| #define | [TIMER2\_CC2\_PA2](#a4bf049cdc3017e816165effd4cff7d35)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x2) |
| #define | [TIMER2\_CC2\_PA3](#a00eafe61a794b07af52d028ab4dd1adf)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x3) |
| #define | [TIMER2\_CC2\_PA4](#aedbc75bcf6c733bcd3deadb3c8ce0f21)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x4) |
| #define | [TIMER2\_CC2\_PA5](#a490ca0f07b93c2cd68351c6afb4a9819)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x5) |
| #define | [TIMER2\_CC2\_PA6](#abd8592d55f4ff8bd546adb9efc7ee922)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x6) |
| #define | [TIMER2\_CC2\_PA7](#a9d34e2111c7b45d5d7b36d0df3c80629)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x7) |
| #define | [TIMER2\_CC2\_PA8](#af969ac3be731d012befc6f7d2aef5fbe)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x8) |
| #define | [TIMER2\_CC2\_PA9](#aab5539df46520dbb522526753d2cd567)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x9) |
| #define | [TIMER2\_CC2\_PB0](#a59ed3f774f4d21a9f1fbc9d71cb57fe4)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x1, 0x0) |
| #define | [TIMER2\_CC2\_PB1](#abaf434275a10efbc0b32f7d859d51912)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x1, 0x1) |
| #define | [TIMER2\_CC2\_PB2](#ac4c83f10ee7ec2978b3612b8fdd8c6cb)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x1, 0x2) |
| #define | [TIMER2\_CC2\_PB3](#acc8b352f48014e5fd8a14f5d1d79d681)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x1, 0x3) |
| #define | [TIMER2\_CC2\_PB4](#a9add0713ccac926ac0a079bd7cd69aae)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x1, 0x4) |
| #define | [TIMER2\_CC2\_PB5](#a803f2b5d5157805d478efa8e93310443)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x1, 0x5) |
| #define | [TIMER2\_CDTI0\_PA0](#a6cb932cba841a0987d78da39e11cadba)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x0) |
| #define | [TIMER2\_CDTI0\_PA1](#a9cde27e9bdb4e6157afe1149d35e8dbd)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x1) |
| #define | [TIMER2\_CDTI0\_PA2](#a5906c55b37b73111550ea2eb75681575)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x2) |
| #define | [TIMER2\_CDTI0\_PA3](#afa16ff7cf30f5cc4d2fe967263b9b2b0)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x3) |
| #define | [TIMER2\_CDTI0\_PA4](#ac0d736392f3d098ec5789189dc37036b)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x4) |
| #define | [TIMER2\_CDTI0\_PA5](#aa8c2a2712578b133cdbd8d07f1f37c24)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x5) |
| #define | [TIMER2\_CDTI0\_PA6](#a801b4531b9bb956d267c53f15b47a872)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x6) |
| #define | [TIMER2\_CDTI0\_PA7](#a36d14f2c4b029f787c6d474e41dd3dd8)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x7) |
| #define | [TIMER2\_CDTI0\_PA8](#ae1f424e362c402dcd38f0aaea7d059ac)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x8) |
| #define | [TIMER2\_CDTI0\_PA9](#aa9e2852c734a0f92a7ecc1a95b60d5e7)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x9) |
| #define | [TIMER2\_CDTI0\_PB0](#ad1c011c5437d75b74c56ebbb00e9dd65)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x1, 0x0) |
| #define | [TIMER2\_CDTI0\_PB1](#afedfcd3a53de2251bb61ccfed3af4a5f)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x1, 0x1) |
| #define | [TIMER2\_CDTI0\_PB2](#aab462dbb772296080bcfa7c0c9cb80fa)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x1, 0x2) |
| #define | [TIMER2\_CDTI0\_PB3](#adc08d2d352d4b14d201a11b6df7a64c9)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x1, 0x3) |
| #define | [TIMER2\_CDTI0\_PB4](#af02e9de67604ab16812a2b464cde99ae)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x1, 0x4) |
| #define | [TIMER2\_CDTI0\_PB5](#ac354ef57259735403dc4f781888e948d)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x1, 0x5) |
| #define | [TIMER2\_CDTI1\_PA0](#ae901259c744451af8a8ded388dfe9f5d)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x0) |
| #define | [TIMER2\_CDTI1\_PA1](#a9e6e2fc9804d67ec073460ddf34fdd02)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x1) |
| #define | [TIMER2\_CDTI1\_PA2](#a7ac971aa8206899b4623057140243357)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x2) |
| #define | [TIMER2\_CDTI1\_PA3](#af174d0f8740b9d33ae66dba3e34b6031)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x3) |
| #define | [TIMER2\_CDTI1\_PA4](#afbda2d057823f529835a894ff9ad8629)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x4) |
| #define | [TIMER2\_CDTI1\_PA5](#a5b02e4c0ceb352d283a0e99cb05fddab)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x5) |
| #define | [TIMER2\_CDTI1\_PA6](#a5a930f094a10216d1b43a4eab6a359b7)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x6) |
| #define | [TIMER2\_CDTI1\_PA7](#add09acbb0fe8df1b64222f324163396b)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x7) |
| #define | [TIMER2\_CDTI1\_PA8](#a7f376eb3ffe07f95fa562c13244f3dd4)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x8) |
| #define | [TIMER2\_CDTI1\_PA9](#afcad730fd054bba3e3ee54b66983fb0e)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x9) |
| #define | [TIMER2\_CDTI1\_PB0](#a542b9626fdc82bd0444ecd2518031406)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x1, 0x0) |
| #define | [TIMER2\_CDTI1\_PB1](#a3600b995f1e40289444081210ad8430f)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x1, 0x1) |
| #define | [TIMER2\_CDTI1\_PB2](#ad87b20ae7e6e5876d5988a95be42720f)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x1, 0x2) |
| #define | [TIMER2\_CDTI1\_PB3](#a3174683951113d5d144bb0338014cbfd)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x1, 0x3) |
| #define | [TIMER2\_CDTI1\_PB4](#aaa89be3aa5b5b9cdbd4a693c5c9ffabe)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x1, 0x4) |
| #define | [TIMER2\_CDTI1\_PB5](#aba96c577d13b3234b8469a40120d9754)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x1, 0x5) |
| #define | [TIMER2\_CDTI2\_PA0](#a70028435f4fa81dc8504d6fb5562480c)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x0) |
| #define | [TIMER2\_CDTI2\_PA1](#af71768a49adaf60e74a77ff629b3ebd2)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x1) |
| #define | [TIMER2\_CDTI2\_PA2](#a56efa7077f3f025446f2c1937b833093)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x2) |
| #define | [TIMER2\_CDTI2\_PA3](#a288823b89fcc8c89d73c6865f8f69cc8)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x3) |
| #define | [TIMER2\_CDTI2\_PA4](#ab34c2728b9bc0054c854960165408494)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x4) |
| #define | [TIMER2\_CDTI2\_PA5](#af55eb46eaa2657c75df8b7c92119588c)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x5) |
| #define | [TIMER2\_CDTI2\_PA6](#a98e606b3b4ba2b0118736951d32b48ad)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x6) |
| #define | [TIMER2\_CDTI2\_PA7](#a1d1543914dacf30872f9d0bdeead7ce7)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x7) |
| #define | [TIMER2\_CDTI2\_PA8](#a8846303a4f61f979c77da532908f7f7b)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x8) |
| #define | [TIMER2\_CDTI2\_PA9](#a00c86bb7e91f80f28e82b9a90c18ebb2)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x9) |
| #define | [TIMER2\_CDTI2\_PB0](#abd0220954a47f2fcf85f72971f2e7f8c)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x1, 0x0) |
| #define | [TIMER2\_CDTI2\_PB1](#ad82071aa4bb174e39da29be3a98e06f4)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x1, 0x1) |
| #define | [TIMER2\_CDTI2\_PB2](#a761808819fa59b8246ead762ee6dc88f)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x1, 0x2) |
| #define | [TIMER2\_CDTI2\_PB3](#af996eab47687d2ef9206856fe10266f8)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x1, 0x3) |
| #define | [TIMER2\_CDTI2\_PB4](#ad66c79e81d41281df4969d775c1e54c6)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x1, 0x4) |
| #define | [TIMER2\_CDTI2\_PB5](#a48946d98ba43063c5c3772f398556f3d)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x1, 0x5) |
| #define | [TIMER3\_CC0\_PC0](#adaa89be7653ebbb82d77f6ccd3ba117a)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x0) |
| #define | [TIMER3\_CC0\_PC1](#ac49977cf88186dd85de660d7dca24093)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x1) |
| #define | [TIMER3\_CC0\_PC2](#a943818c0b36e315772740e9260777e98)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x2) |
| #define | [TIMER3\_CC0\_PC3](#a3b4277fa7886db498357df495e7d0f5b)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x3) |
| #define | [TIMER3\_CC0\_PC4](#afef97dfceb1266dad39f3c06a28cccde)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x4) |
| #define | [TIMER3\_CC0\_PC5](#a850b7d20c5e78b8609f0b4ab737fb59e)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x5) |
| #define | [TIMER3\_CC0\_PC6](#a06fb13b5ae7a9758c47f1d12f54bb643)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x6) |
| #define | [TIMER3\_CC0\_PC7](#aba2b4f6a903913dd21c7f919ee2d4bfd)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x7) |
| #define | [TIMER3\_CC0\_PC8](#afe2a5c724fc88c73ddcc1ec385e0582e)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x8) |
| #define | [TIMER3\_CC0\_PC9](#afab0c54879a2d089d2f5302ddf1f7462)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x9) |
| #define | [TIMER3\_CC0\_PD0](#a05f49738ea2e4cac6cff7b921761da01)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x3, 0x0) |
| #define | [TIMER3\_CC0\_PD1](#a4bf238e512342fc49c7a7d3fa1a13ee7)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x3, 0x1) |
| #define | [TIMER3\_CC0\_PD2](#a01e72605da25e5a408a0c3467be59205)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x3, 0x2) |
| #define | [TIMER3\_CC0\_PD3](#a3216588bd129dc8f82c27de826acb69b)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x3, 0x3) |
| #define | [TIMER3\_CC0\_PD4](#a0775d2d03fc98ce82fba4e19100e3b96)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x3, 0x4) |
| #define | [TIMER3\_CC0\_PD5](#a8a2faefb01867dbdc07a5d8d7844c043)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x3, 0x5) |
| #define | [TIMER3\_CC1\_PC0](#a0911c0d09d2d62526ee7d69a0abf0206)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x0) |
| #define | [TIMER3\_CC1\_PC1](#afc5b3d4f06f9392ff91d1a04039cc106)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x1) |
| #define | [TIMER3\_CC1\_PC2](#a841b61a51502f96b4b4db51f1747ddc2)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x2) |
| #define | [TIMER3\_CC1\_PC3](#abe25ec49b962f68c7e0b782fe8b31e0c)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x3) |
| #define | [TIMER3\_CC1\_PC4](#aafcf7edadba216092137ea9ce0c0da17)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x4) |
| #define | [TIMER3\_CC1\_PC5](#ac24430c7e08b2e0fe7bc63f92c01f9b5)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x5) |
| #define | [TIMER3\_CC1\_PC6](#a3400ddc7e6f8c607251d0b8f049cc0f1)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x6) |
| #define | [TIMER3\_CC1\_PC7](#a440e269a870fa8411ca1584a653df6e8)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x7) |
| #define | [TIMER3\_CC1\_PC8](#ad810dd127fc37f8e79e563203d4a2907)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x8) |
| #define | [TIMER3\_CC1\_PC9](#a755c761c565792dfec62073a02f79d0c)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x9) |
| #define | [TIMER3\_CC1\_PD0](#acb2b010357d2dd7e82266e1f530d93fc)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x3, 0x0) |
| #define | [TIMER3\_CC1\_PD1](#ac1cffc60caba52ee6ab100837b2b6cb3)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x3, 0x1) |
| #define | [TIMER3\_CC1\_PD2](#ac07495ddce953166e53c19d0a4f928fc)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x3, 0x2) |
| #define | [TIMER3\_CC1\_PD3](#a23644731303d1f1e527a7174ccef3e4a)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x3, 0x3) |
| #define | [TIMER3\_CC1\_PD4](#a06ed13488197cb82712911d67eb16b3e)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x3, 0x4) |
| #define | [TIMER3\_CC1\_PD5](#aef8394f92d0d255ee7cb41fd33f56cc6)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x3, 0x5) |
| #define | [TIMER3\_CC2\_PC0](#a7bf47abf6ea4ddf3f3e8dd71dcabc9f8)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x0) |
| #define | [TIMER3\_CC2\_PC1](#a2a2021e1cc5ec1156b6e3e8432a56dee)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x1) |
| #define | [TIMER3\_CC2\_PC2](#ad74e77cefd62c22a97737ab3eb7ce658)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x2) |
| #define | [TIMER3\_CC2\_PC3](#ab80ddb4234db5937e1244204d980e951)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x3) |
| #define | [TIMER3\_CC2\_PC4](#a717ccb54d7b93e7d4341f15ae10944cb)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x4) |
| #define | [TIMER3\_CC2\_PC5](#af10e6860473870cd0555e03907220ba7)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x5) |
| #define | [TIMER3\_CC2\_PC6](#aa221b71494071d6af232f0d8f9050aa7)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x6) |
| #define | [TIMER3\_CC2\_PC7](#adce105bc3d6134d45f130dfd77cfd59e)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x7) |
| #define | [TIMER3\_CC2\_PC8](#ae3a479466816d04e5ff040e1cfe59df0)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x8) |
| #define | [TIMER3\_CC2\_PC9](#ae9d00a013feb2612a01d773b73841035)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x9) |
| #define | [TIMER3\_CC2\_PD0](#a457c25d6e6cb832e66753dfc84d189f3)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x3, 0x0) |
| #define | [TIMER3\_CC2\_PD1](#adbeb6aa8891fdfe6510584bc8e5b5ced)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x3, 0x1) |
| #define | [TIMER3\_CC2\_PD2](#aa6524ad51bd80ac04276af0e722c5047)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x3, 0x2) |
| #define | [TIMER3\_CC2\_PD3](#ae94118e07443fa220d9162ad681c1a19)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x3, 0x3) |
| #define | [TIMER3\_CC2\_PD4](#a0a4d56c8f26bb269a10888e29cd0df4e)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x3, 0x4) |
| #define | [TIMER3\_CC2\_PD5](#a144c5d6fa9829dbf9d07b0693df2e52e)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x3, 0x5) |
| #define | [TIMER3\_CDTI0\_PC0](#a68db08edab7a0f208661895888ad0f4a)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x0) |
| #define | [TIMER3\_CDTI0\_PC1](#a3ae3f2df52006b2a53b70f7e940b8ed9)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x1) |
| #define | [TIMER3\_CDTI0\_PC2](#a1e3e29f3208cc7253d081b7c589632c1)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x2) |
| #define | [TIMER3\_CDTI0\_PC3](#a8ee6bc60c7704e1437c5d175df34d0a0)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x3) |
| #define | [TIMER3\_CDTI0\_PC4](#a6f98e4a7f4269972296fe587e83d0d7a)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x4) |
| #define | [TIMER3\_CDTI0\_PC5](#a348b50033a138bbc11ef6e99188fb023)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x5) |
| #define | [TIMER3\_CDTI0\_PC6](#aa744875bc8bbc9d504edf1022da599fd)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x6) |
| #define | [TIMER3\_CDTI0\_PC7](#a769a76d9258e7bdfdf7a8b21b70da011)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x7) |
| #define | [TIMER3\_CDTI0\_PC8](#aff387c44f16e275bae07a4f8ac81d16e)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x8) |
| #define | [TIMER3\_CDTI0\_PC9](#a235827cf9b740c57a808b180ab9a84ca)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x9) |
| #define | [TIMER3\_CDTI0\_PD0](#ae67b96fbcd3994e67f72d03f29690c02)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x3, 0x0) |
| #define | [TIMER3\_CDTI0\_PD1](#a477f3adb9d6430be9ef0746cba23b9fb)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x3, 0x1) |
| #define | [TIMER3\_CDTI0\_PD2](#a3ca82d8f98012743293a033b4c9c93be)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x3, 0x2) |
| #define | [TIMER3\_CDTI0\_PD3](#a3115a35f39b0b3f35120c728fc5c8c2f)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x3, 0x3) |
| #define | [TIMER3\_CDTI0\_PD4](#a5a5a79c390c93f0cceaca0668890ec8a)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x3, 0x4) |
| #define | [TIMER3\_CDTI0\_PD5](#ad4e7264378623d9e4eec2b1af05ad841)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x3, 0x5) |
| #define | [TIMER3\_CDTI1\_PC0](#a5dd1fea7f7ab7ee15a030b96a40d1114)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x0) |
| #define | [TIMER3\_CDTI1\_PC1](#aca7f55259fe2f36061078af791f3de4b)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x1) |
| #define | [TIMER3\_CDTI1\_PC2](#a03b1888fffa0036b1a9d92357d161cc7)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x2) |
| #define | [TIMER3\_CDTI1\_PC3](#a336444e4a0e7068e3e25e6908628c40c)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x3) |
| #define | [TIMER3\_CDTI1\_PC4](#a7c48bb98bfbace4681c6a1267d681e45)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x4) |
| #define | [TIMER3\_CDTI1\_PC5](#afa7ade2fc1198c66cd4812ac29befdf4)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x5) |
| #define | [TIMER3\_CDTI1\_PC6](#ad9ac8ee5259d40afead5b762ce90f4e6)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x6) |
| #define | [TIMER3\_CDTI1\_PC7](#af45d8db4d1da4526cce601e204743670)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x7) |
| #define | [TIMER3\_CDTI1\_PC8](#a922de5863e94bc01cc203fb0d09d075a)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x8) |
| #define | [TIMER3\_CDTI1\_PC9](#a5ad16b119b01a2279e2e14fc43b14744)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x9) |
| #define | [TIMER3\_CDTI1\_PD0](#a984b05d5d53c1068a86614a550995fc0)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x3, 0x0) |
| #define | [TIMER3\_CDTI1\_PD1](#a377c5ee038e274db1ddead0ad0fa7bf1)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x3, 0x1) |
| #define | [TIMER3\_CDTI1\_PD2](#a57207da12d6fa72e566b728371f4f402)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x3, 0x2) |
| #define | [TIMER3\_CDTI1\_PD3](#a18850fb5d2583d3652f7c43ea1d0ac39)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x3, 0x3) |
| #define | [TIMER3\_CDTI1\_PD4](#a419139192559d7484a6496741f780682)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x3, 0x4) |
| #define | [TIMER3\_CDTI1\_PD5](#a3d6af6e3bfb3e3f448584ae751dcf1ae)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x3, 0x5) |
| #define | [TIMER3\_CDTI2\_PC0](#a4a21cc75bb143d4fa1a84eb243fccc36)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x0) |
| #define | [TIMER3\_CDTI2\_PC1](#a881ccb7ad41ecf73423b97e8c489a6d0)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x1) |
| #define | [TIMER3\_CDTI2\_PC2](#aefbbc0a5e8e7673ccacdf399c288903e)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x2) |
| #define | [TIMER3\_CDTI2\_PC3](#abc867b08524924b26a2ed326a2b12155)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x3) |
| #define | [TIMER3\_CDTI2\_PC4](#a0befb875610ff387c2c1ac06f88d7b79)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x4) |
| #define | [TIMER3\_CDTI2\_PC5](#aea7c0881164e98c21fcf30d689deb592)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x5) |
| #define | [TIMER3\_CDTI2\_PC6](#a2a4909305fd0dbde0c3caba5f32fc896)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x6) |
| #define | [TIMER3\_CDTI2\_PC7](#a481f5eb7e5d4c148bc2be3d958973577)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x7) |
| #define | [TIMER3\_CDTI2\_PC8](#ae0de2380f85df6c295d5c88388e0bdec)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x8) |
| #define | [TIMER3\_CDTI2\_PC9](#ab8860f00495817a94f59ff502e4d4d44)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x9) |
| #define | [TIMER3\_CDTI2\_PD0](#a228392afbba95bbb69a65aae20dbb2d1)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x3, 0x0) |
| #define | [TIMER3\_CDTI2\_PD1](#a162d7a8c85197e047bc65cef7235a591)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x3, 0x1) |
| #define | [TIMER3\_CDTI2\_PD2](#a7f3873fb6abfaf970024318529fcfcd5)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x3, 0x2) |
| #define | [TIMER3\_CDTI2\_PD3](#a0c3fc7049d7dacfedfc4a04ced71202f)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x3, 0x3) |
| #define | [TIMER3\_CDTI2\_PD4](#adbfbccad761957506d72eb5b5f774ddc)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x3, 0x4) |
| #define | [TIMER3\_CDTI2\_PD5](#a676eb78dc7d678ce8080912279c42f87)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x3, 0x5) |
| #define | [TIMER4\_CC0\_PA0](#aa0c6e5e3f769ae31848239ea16fc8c26)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x0) |
| #define | [TIMER4\_CC0\_PA1](#ac49460d333f18f30fe332cad4ead4719)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x1) |
| #define | [TIMER4\_CC0\_PA2](#a92254bd9362d97e1fe55f8e9a7036857)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x2) |
| #define | [TIMER4\_CC0\_PA3](#a5c83b195cb0fd5344c2ec05a8547a063)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x3) |
| #define | [TIMER4\_CC0\_PA4](#a0daf9dc92bab78111bfc9425c38ba671)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x4) |
| #define | [TIMER4\_CC0\_PA5](#aebea07333a9390eb469f7efc8d4e773c)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x5) |
| #define | [TIMER4\_CC0\_PA6](#a88bab7bd85be0c93a81f359d872e65f2)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x6) |
| #define | [TIMER4\_CC0\_PA7](#ab527597383a746f75328fd7877d96389)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x7) |
| #define | [TIMER4\_CC0\_PA8](#af7ef30e6d27885e8f6eacdced332012d)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x8) |
| #define | [TIMER4\_CC0\_PA9](#a269be5490c9194daa1f56680597227f4)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x9) |
| #define | [TIMER4\_CC0\_PB0](#a6a53b58cd4ff5c60b736cbe9d25954fa)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x1, 0x0) |
| #define | [TIMER4\_CC0\_PB1](#a778ea39ff864aad8a92e35859bb1ec97)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x1, 0x1) |
| #define | [TIMER4\_CC0\_PB2](#a2fecff946d39c7745e061f2a4a4a03b7)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x1, 0x2) |
| #define | [TIMER4\_CC0\_PB3](#a1e7beb8ae86e28ef5a122118644a0b6d)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x1, 0x3) |
| #define | [TIMER4\_CC0\_PB4](#a99a47cb9b6cb9273332d2a8f6598a52f)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x1, 0x4) |
| #define | [TIMER4\_CC0\_PB5](#a627ec43ac8af76e99e57c6c79de245e4)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x1, 0x5) |
| #define | [TIMER4\_CC1\_PA0](#a0a20fe004087b6d6599f775aefac56f2)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x0) |
| #define | [TIMER4\_CC1\_PA1](#a044a7b8e14be441705f29e4b6015ee08)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x1) |
| #define | [TIMER4\_CC1\_PA2](#adbd211cd9344a88c6301462a5e3edc51)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x2) |
| #define | [TIMER4\_CC1\_PA3](#a5a04fcf2fff3afd10e98cb2e31509cc5)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x3) |
| #define | [TIMER4\_CC1\_PA4](#a8d301ec962fe2cce8ba002f274988559)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x4) |
| #define | [TIMER4\_CC1\_PA5](#a102bc4ebc9988c58529e288cbae2dcf5)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x5) |
| #define | [TIMER4\_CC1\_PA6](#a3ea21e7b459ab219ee593f4ded6423d6)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x6) |
| #define | [TIMER4\_CC1\_PA7](#afbf528e09cd5f8416ad6a21bf15e6dc7)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x7) |
| #define | [TIMER4\_CC1\_PA8](#a5b53aae41cdc44147d6333ce5d7c28aa)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x8) |
| #define | [TIMER4\_CC1\_PA9](#ace92b6394b1909d14dd0be0567787c95)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x9) |
| #define | [TIMER4\_CC1\_PB0](#a65dd111e27e3d7ba7cec249ea3354ff4)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x1, 0x0) |
| #define | [TIMER4\_CC1\_PB1](#ac64bc36ec5794d92ac2bf256147645f5)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x1, 0x1) |
| #define | [TIMER4\_CC1\_PB2](#a38afb957c997a8378e3aebb6141f7426)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x1, 0x2) |
| #define | [TIMER4\_CC1\_PB3](#a280bb1ebea122956c890dcb8d84b2241)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x1, 0x3) |
| #define | [TIMER4\_CC1\_PB4](#a767e437a09fa17b72c8c3f9c7dfdbf60)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x1, 0x4) |
| #define | [TIMER4\_CC1\_PB5](#a3e3d6d3817651318f5aca14244f06153)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x1, 0x5) |
| #define | [TIMER4\_CC2\_PA0](#a777870e82a20af4a6a6e71a5b636fca6)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x0) |
| #define | [TIMER4\_CC2\_PA1](#a85d5e0d8c945839bbda1cdcfb1c27952)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x1) |
| #define | [TIMER4\_CC2\_PA2](#a1e87cfdb2f81b1168fd9fd61e4451103)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x2) |
| #define | [TIMER4\_CC2\_PA3](#a3a16aab894717ffae5bcb0ab14cc6dbb)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x3) |
| #define | [TIMER4\_CC2\_PA4](#a2dfa60f8a9d458a782ab2df7f2209976)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x4) |
| #define | [TIMER4\_CC2\_PA5](#a8a3aac099645db504605942c9e86083f)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x5) |
| #define | [TIMER4\_CC2\_PA6](#a73ab6a5f63c5e2c778913a196c49915f)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x6) |
| #define | [TIMER4\_CC2\_PA7](#a1f5ce55fa587d01d50b1f8496b4c2640)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x7) |
| #define | [TIMER4\_CC2\_PA8](#a13b0916acd52e39c467b2ae7c8f08e22)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x8) |
| #define | [TIMER4\_CC2\_PA9](#ae20b7bb781c40b3a48930ec2741a35ab)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x9) |
| #define | [TIMER4\_CC2\_PB0](#a1965744950bba0b98b124ef7fd308538)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x1, 0x0) |
| #define | [TIMER4\_CC2\_PB1](#af51b2d503e11e751815cc9e46c777cc8)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x1, 0x1) |
| #define | [TIMER4\_CC2\_PB2](#a9ae5f6cda5ee8fc6551a58bc1dea1b6a)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x1, 0x2) |
| #define | [TIMER4\_CC2\_PB3](#a4033b892135db2f425c041fb353dd94e)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x1, 0x3) |
| #define | [TIMER4\_CC2\_PB4](#ab9f0f4839c1db0ff24c71e8a43bca20b)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x1, 0x4) |
| #define | [TIMER4\_CC2\_PB5](#ad09a118179644890178c1ae4504a0bf4)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x1, 0x5) |
| #define | [TIMER4\_CDTI0\_PA0](#a7a3baa51540b54c8677085fce6fdff99)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x0) |
| #define | [TIMER4\_CDTI0\_PA1](#a46ad78924a9aebe629236e072c1c013b)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x1) |
| #define | [TIMER4\_CDTI0\_PA2](#ab302b8f1cc1c0b103e4a315173af2455)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x2) |
| #define | [TIMER4\_CDTI0\_PA3](#a6cabbf3093dc73c82ab34ffd0a979b9e)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x3) |
| #define | [TIMER4\_CDTI0\_PA4](#a228a5febbceec760f773b1114a978c12)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x4) |
| #define | [TIMER4\_CDTI0\_PA5](#a44b20d92c88a15471c81f3f408126476)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x5) |
| #define | [TIMER4\_CDTI0\_PA6](#a2c06384e73db9a53f2a46c79991f022e)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x6) |
| #define | [TIMER4\_CDTI0\_PA7](#a1ccb51b05ade839e65eb898115a09a1f)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x7) |
| #define | [TIMER4\_CDTI0\_PA8](#aec88b0761fc5162dfa63daaaf0d8dd80)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x8) |
| #define | [TIMER4\_CDTI0\_PA9](#a363db5107db42dbd9e512cf4d4890883)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x9) |
| #define | [TIMER4\_CDTI0\_PB0](#a7417d210f904b5448a079950b92d7e85)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x1, 0x0) |
| #define | [TIMER4\_CDTI0\_PB1](#a5943529095abd138015248fc122f0af1)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x1, 0x1) |
| #define | [TIMER4\_CDTI0\_PB2](#aeffc25dbbbc7d1eb199cd29b7cf7e0a0)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x1, 0x2) |
| #define | [TIMER4\_CDTI0\_PB3](#aeda432d234c691de7a000702c9e13ba4)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x1, 0x3) |
| #define | [TIMER4\_CDTI0\_PB4](#a128f18c80a9343d189b856d1d4f3b128)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x1, 0x4) |
| #define | [TIMER4\_CDTI0\_PB5](#a19aef3f3f90b44d98df95ddbf6a60e76)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x1, 0x5) |
| #define | [TIMER4\_CDTI1\_PA0](#a2c8f5c89e8e8d8acf768efc55c2c1557)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x0) |
| #define | [TIMER4\_CDTI1\_PA1](#aeec9e93ade4349a932987805b56427ea)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x1) |
| #define | [TIMER4\_CDTI1\_PA2](#a5504301d2109fd9b938b6d2183e1e23f)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x2) |
| #define | [TIMER4\_CDTI1\_PA3](#a9baa482a3d5caf216a47294c2b74b060)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x3) |
| #define | [TIMER4\_CDTI1\_PA4](#a84c9ec2e762283faf0804fdc2d4b8e67)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x4) |
| #define | [TIMER4\_CDTI1\_PA5](#abc07eda4d4f0a0a189628e9e2e7eed05)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x5) |
| #define | [TIMER4\_CDTI1\_PA6](#a1b72f464803bcaa51f912a41e0d92023)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x6) |
| #define | [TIMER4\_CDTI1\_PA7](#a8c6b70c5db7bf891a3fb608f7f50e3f1)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x7) |
| #define | [TIMER4\_CDTI1\_PA8](#ac2bab95ab6f8067049fc144683ce0e77)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x8) |
| #define | [TIMER4\_CDTI1\_PA9](#a225ed569ec2351827f71df73c35b9659)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x9) |
| #define | [TIMER4\_CDTI1\_PB0](#a9897ffcb326b237d2258b7fbd32111c9)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x1, 0x0) |
| #define | [TIMER4\_CDTI1\_PB1](#a8ffdf1e7b414a675d6ea582e30047251)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x1, 0x1) |
| #define | [TIMER4\_CDTI1\_PB2](#a8bc164f77d9311ae19c11eb993724a96)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x1, 0x2) |
| #define | [TIMER4\_CDTI1\_PB3](#a2feb1f73241aaedd10d1f30a8402fb6f)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x1, 0x3) |
| #define | [TIMER4\_CDTI1\_PB4](#a1a7a79e99bf52e3f2c6241608c7fc814)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x1, 0x4) |
| #define | [TIMER4\_CDTI1\_PB5](#a26c42742eb2923f24fa10ffc1fe11600)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x1, 0x5) |
| #define | [TIMER4\_CDTI2\_PA0](#a0167c1d5682489dcfdd9d60fa1a2cc44)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x0) |
| #define | [TIMER4\_CDTI2\_PA1](#a8c51fb1efbd523ef8d5b57b66d65060f)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x1) |
| #define | [TIMER4\_CDTI2\_PA2](#aea7d724240277e0a0b3c2334063e6b6a)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x2) |
| #define | [TIMER4\_CDTI2\_PA3](#ab8588c060f8671f5696a0e2529394a37)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x3) |
| #define | [TIMER4\_CDTI2\_PA4](#a4c566e93e8f5375744be6303f5049840)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x4) |
| #define | [TIMER4\_CDTI2\_PA5](#a4218800d01dc2d8e767d1e03e28c00e4)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x5) |
| #define | [TIMER4\_CDTI2\_PA6](#af9c15b67b7e09875d5a9991dac81222f)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x6) |
| #define | [TIMER4\_CDTI2\_PA7](#a664bd862ef44614302fe82a809d1f148)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x7) |
| #define | [TIMER4\_CDTI2\_PA8](#ad20202f301b5e59f477ab02d6ee37546)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x8) |
| #define | [TIMER4\_CDTI2\_PA9](#aa5262ec786fc475be010ce5c1b3ed78c)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x9) |
| #define | [TIMER4\_CDTI2\_PB0](#a35aa90b994c639d68f2a8bbd65903494)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x1, 0x0) |
| #define | [TIMER4\_CDTI2\_PB1](#a20970e543f42e4785409f8f391d6daa9)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x1, 0x1) |
| #define | [TIMER4\_CDTI2\_PB2](#aee236ba0af0b2d08871f15ca7d78cd2c)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x1, 0x2) |
| #define | [TIMER4\_CDTI2\_PB3](#a976af94ec2e61f8b59edebf73e3222f0)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x1, 0x3) |
| #define | [TIMER4\_CDTI2\_PB4](#a03b1a79e2c32ed563d6ebf81b9741d14)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x1, 0x4) |
| #define | [TIMER4\_CDTI2\_PB5](#ab02f811798eba69b02445ad1ea459e0e)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x1, 0x5) |
| #define | [USART0\_CS\_PA0](#a8b31d0e72dc71f813f3ae21da1b064dc)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x0) |
| #define | [USART0\_CS\_PA1](#affbbbbf6348af411b5392e462304edee)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x1) |
| #define | [USART0\_CS\_PA2](#a70d22cbabea10e31293a21262f6a64b3)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x2) |
| #define | [USART0\_CS\_PA3](#a2a80bc71c923ed7c6fd2865d869864fc)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x3) |
| #define | [USART0\_CS\_PA4](#af24e43481767fe27cdd78f5e27f15d7f)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x4) |
| #define | [USART0\_CS\_PA5](#a7cb722df10819495d5059933ddf122a4)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x5) |
| #define | [USART0\_CS\_PA6](#a94d45fdffdc79cc92994105238c9f0f8)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x6) |
| #define | [USART0\_CS\_PA7](#a75603bdb24ba0f19a841a1ed7b3fc683)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x7) |
| #define | [USART0\_CS\_PA8](#a2eb48dfecd71b07998cff24d69052360)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x8) |
| #define | [USART0\_CS\_PA9](#a296a14e4ef77412fd396a4e2ded0b3b3)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x9) |
| #define | [USART0\_CS\_PB0](#a5f92c862131c6dfd2dc95146cdfa09aa)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x1, 0x0) |
| #define | [USART0\_CS\_PB1](#aa45d4cfe63813c6c8aa8602e0783f7fb)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x1, 0x1) |
| #define | [USART0\_CS\_PB2](#a8d25b8c147a7d0777e023a56bc47b5ea)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x1, 0x2) |
| #define | [USART0\_CS\_PB3](#a8a749535093e7817f27396459ee97d72)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x1, 0x3) |
| #define | [USART0\_CS\_PB4](#a25fa64c3232371544eba09423fb0c765)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x1, 0x4) |
| #define | [USART0\_CS\_PB5](#a07b913ebc5b03c4519fdd4136f907021)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x1, 0x5) |
| #define | [USART0\_CS\_PC0](#a2372be5754b13cafcef6a63d63548924)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x0) |
| #define | [USART0\_CS\_PC1](#a0033eb0ea09f9dab2ab5a20d185ba0e0)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x1) |
| #define | [USART0\_CS\_PC2](#afdc21300ca9ab485a7d97fa344ee3292)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x2) |
| #define | [USART0\_CS\_PC3](#acc373a1b4402c4f4f229524837a4c3ac)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x3) |
| #define | [USART0\_CS\_PC4](#a3bb143a83558aaa91fad609259a13044)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x4) |
| #define | [USART0\_CS\_PC5](#ab4ae79a567d023b7f886019e3d5518b1)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x5) |
| #define | [USART0\_CS\_PC6](#a8ad8102bed214716bdcf82c1747e2ce3)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x6) |
| #define | [USART0\_CS\_PC7](#a3f1d10140e34a916172f4ccfeb086fea)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x7) |
| #define | [USART0\_CS\_PC8](#a3167008284cd4666dc930bdb47e104a1)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x8) |
| #define | [USART0\_CS\_PC9](#ac25117b1cb234416a65c9ccb6a52b385)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x9) |
| #define | [USART0\_CS\_PD0](#a4d2ef2ccd5f3dbefa048e37f2bb40b8b)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x3, 0x0) |
| #define | [USART0\_CS\_PD1](#a1f6089f92cf5168cbd9a6daa0f336ebb)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x3, 0x1) |
| #define | [USART0\_CS\_PD2](#a4e54dcbabdbebe60f309a31c7acbe30f)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x3, 0x2) |
| #define | [USART0\_CS\_PD3](#a00073504dbe55119dc3dac466c5f816f)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x3, 0x3) |
| #define | [USART0\_CS\_PD4](#adc4cf5aa4e7acad165031376bf0e2551)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x3, 0x4) |
| #define | [USART0\_CS\_PD5](#a03e9928b1089537c453bdf46854a1921)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x3, 0x5) |
| #define | [USART0\_RTS\_PA0](#a104b44454bfafbbdd54fe6b53c2dff33)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x0) |
| #define | [USART0\_RTS\_PA1](#abbaf9c9b55c0673fc774610b83aca313)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x1) |
| #define | [USART0\_RTS\_PA2](#abaae8c12c4daa90d49e9f327f16a6691)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x2) |
| #define | [USART0\_RTS\_PA3](#a4ba035c607b639dfef668323a43a3f7f)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x3) |
| #define | [USART0\_RTS\_PA4](#a234727fb3ae07a22c350d4a0a58c30cb)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x4) |
| #define | [USART0\_RTS\_PA5](#a0f8ad339a81f02d95e747a82aefe699e)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x5) |
| #define | [USART0\_RTS\_PA6](#afcab39462b0cc95e3984b4a10e54b587)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x6) |
| #define | [USART0\_RTS\_PA7](#ae4f01f02accb203b696d25f69e4d1c2a)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x7) |
| #define | [USART0\_RTS\_PA8](#a3894dc798fe8561bba8836323f63aea4)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x8) |
| #define | [USART0\_RTS\_PA9](#a574cd147790bad9eb28767973741f066)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x9) |
| #define | [USART0\_RTS\_PB0](#a9808fc5b30607e6d0cbc3172369b818d)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x1, 0x0) |
| #define | [USART0\_RTS\_PB1](#a44240f09f67e09e58d28f82c43aff37d)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x1, 0x1) |
| #define | [USART0\_RTS\_PB2](#aa09ddd73916db94f88c710526689253d)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x1, 0x2) |
| #define | [USART0\_RTS\_PB3](#a7db53ff445baf566a0fcb7ce25532bb8)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x1, 0x3) |
| #define | [USART0\_RTS\_PB4](#ad1f91a8c2838f4b2f25240330b3144c3)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x1, 0x4) |
| #define | [USART0\_RTS\_PB5](#aebf7dec589dd49edacb06e3068c43289)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x1, 0x5) |
| #define | [USART0\_RTS\_PC0](#a2023f5afe82a2b2ff9b6c00bb249367b)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x0) |
| #define | [USART0\_RTS\_PC1](#a59cd7521827677160d85555c25430a9b)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x1) |
| #define | [USART0\_RTS\_PC2](#af7675ade342b55e04078f3d53306ca45)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x2) |
| #define | [USART0\_RTS\_PC3](#a42798ba22452bc2850007c9871d9daee)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x3) |
| #define | [USART0\_RTS\_PC4](#ae54415286b298aceaebdddcb3d008f5b)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x4) |
| #define | [USART0\_RTS\_PC5](#a6490fddb874c99a2cc293342c1b58dfc)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x5) |
| #define | [USART0\_RTS\_PC6](#ac72929dbdc13592ff0c46515bfc9169b)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x6) |
| #define | [USART0\_RTS\_PC7](#a88f8735b06c99e4851ee982a6ced5412)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x7) |
| #define | [USART0\_RTS\_PC8](#a6df814f12464adac6f44d998150dee99)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x8) |
| #define | [USART0\_RTS\_PC9](#a82db1fdbd8a2f9a418d28c87867342d3)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x9) |
| #define | [USART0\_RTS\_PD0](#a705598d6a60acd8936d6b7d0aa18cba2)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x3, 0x0) |
| #define | [USART0\_RTS\_PD1](#af77229ee4cf9eac56cc2fb134bc805c4)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x3, 0x1) |
| #define | [USART0\_RTS\_PD2](#a6a6bf570ad629ce3c81b37d31ffa2efe)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x3, 0x2) |
| #define | [USART0\_RTS\_PD3](#a0f8639b93ef710b631309b9388fbcb50)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x3, 0x3) |
| #define | [USART0\_RTS\_PD4](#ad9efbfbd3c62b51abf94fbbb8d9a493a)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x3, 0x4) |
| #define | [USART0\_RTS\_PD5](#af1677dba75a6a276fd2bba61dff06b78)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x3, 0x5) |
| #define | [USART0\_RX\_PA0](#aacdc76948ed8f1e54f8e260e62c89f61)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x0) |
| #define | [USART0\_RX\_PA1](#af41b4722d7b89c28645c24ac8e9a5eb4)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x1) |
| #define | [USART0\_RX\_PA2](#a4da72ddcfaf102aa817eb2bc6e0c5cbb)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x2) |
| #define | [USART0\_RX\_PA3](#a0a9b80333130d05d11bf88c78434221a)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x3) |
| #define | [USART0\_RX\_PA4](#ac992577a6d9d5e0730eaaaa2086d5802)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x4) |
| #define | [USART0\_RX\_PA5](#a8203de9111610660eea0c49ef51a9f6a)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x5) |
| #define | [USART0\_RX\_PA6](#a84a42fda6d1b7a2269c357e2929b8219)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x6) |
| #define | [USART0\_RX\_PA7](#a2f2a30bbb2a5b9e4d99ffb78545bbf3b)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x7) |
| #define | [USART0\_RX\_PA8](#af982046455e2567919abe51956e83c10)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x8) |
| #define | [USART0\_RX\_PA9](#a368a626b18b5d68929a859d06fbf673b)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x9) |
| #define | [USART0\_RX\_PB0](#ab6691b3280f611c94c8690302bce85d5)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x1, 0x0) |
| #define | [USART0\_RX\_PB1](#ab23c92ad1cb6a8cafe055baade2e8b87)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x1, 0x1) |
| #define | [USART0\_RX\_PB2](#ace83f4be0c630151d9e59c4c21a40109)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x1, 0x2) |
| #define | [USART0\_RX\_PB3](#ad2268a788d647414dd9ef5dba5bbed19)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x1, 0x3) |
| #define | [USART0\_RX\_PB4](#ab17af03ccdc989dd4c8e28173d1a3b39)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x1, 0x4) |
| #define | [USART0\_RX\_PB5](#a0a597070bf11931433fef8ae1e90b632)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x1, 0x5) |
| #define | [USART0\_RX\_PC0](#aee4369f8682feee79f184c83d80274da)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x0) |
| #define | [USART0\_RX\_PC1](#a9350586833a3d5c48baefd1610c13f62)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x1) |
| #define | [USART0\_RX\_PC2](#a0a895e2c1e4a38b1fe6ebd5da7d525e5)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x2) |
| #define | [USART0\_RX\_PC3](#a437d4a2cea5c64fc92b6c99b87bf5e8c)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x3) |
| #define | [USART0\_RX\_PC4](#a75a6d4f4d7656eea8244bfb0d030ca79)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x4) |
| #define | [USART0\_RX\_PC5](#a869fb6d64ec0e62beecb34dd0279f202)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x5) |
| #define | [USART0\_RX\_PC6](#ad6902172e17c7f2c920e4658151182cd)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x6) |
| #define | [USART0\_RX\_PC7](#ab5f98edf5748c59adffddbe6c3e032d6)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x7) |
| #define | [USART0\_RX\_PC8](#ad5357505fc27282348572e648fe427c6)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x8) |
| #define | [USART0\_RX\_PC9](#af0db0630d2887cafe0a0711b4d785da5)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x9) |
| #define | [USART0\_RX\_PD0](#a823861421794933ab4e682de63e49cc4)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x3, 0x0) |
| #define | [USART0\_RX\_PD1](#a408c8b04c4e9598c9bb139446244810f)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x3, 0x1) |
| #define | [USART0\_RX\_PD2](#ad11874063a494e22191887fbd29d0189)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x3, 0x2) |
| #define | [USART0\_RX\_PD3](#a0dbbdc55667cd4c32262a7e91298cf95)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x3, 0x3) |
| #define | [USART0\_RX\_PD4](#a95c9f4c6e85f0d9cf050e7554cc41074)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x3, 0x4) |
| #define | [USART0\_RX\_PD5](#ad4351007ac9fac08290be8409e28474a)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x3, 0x5) |
| #define | [USART0\_CLK\_PA0](#a16af201487286a8bad218c94245a88c7)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x0) |
| #define | [USART0\_CLK\_PA1](#a1c3041ba213cdbcb2796dbffa01b8571)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x1) |
| #define | [USART0\_CLK\_PA2](#a1e546e7130f7012f29d6d2aad3e97b39)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x2) |
| #define | [USART0\_CLK\_PA3](#aa78910cf4b3c816508e2e97288489f16)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x3) |
| #define | [USART0\_CLK\_PA4](#a76684ba202fa4fb3b5e545a031f0c841)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x4) |
| #define | [USART0\_CLK\_PA5](#a92cda8774c81ce2539654516c2b62dd6)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x5) |
| #define | [USART0\_CLK\_PA6](#a6c67ed947caacf669665e133327a7e00)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x6) |
| #define | [USART0\_CLK\_PA7](#af8f2d47db5aa651708f0d2dea2e39c48)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x7) |
| #define | [USART0\_CLK\_PA8](#a06fdcd2c3ae7b6162aff6a3fbeac94a8)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x8) |
| #define | [USART0\_CLK\_PA9](#a1151deef40a267aa9d8ad1b76f86d74e)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x9) |
| #define | [USART0\_CLK\_PB0](#a80303adbfa7489fdefcbf14b38c25194)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x1, 0x0) |
| #define | [USART0\_CLK\_PB1](#a242754151600f954e6c9063254862537)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x1, 0x1) |
| #define | [USART0\_CLK\_PB2](#a8ed2cedbe7fd2daf10bee286f2bb6468)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x1, 0x2) |
| #define | [USART0\_CLK\_PB3](#abe23ca58f25d6bfa5b939cf58d7a0dee)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x1, 0x3) |
| #define | [USART0\_CLK\_PB4](#abac165e111f292793ab41b4411ad847c)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x1, 0x4) |
| #define | [USART0\_CLK\_PB5](#a2fae78dc9ec493c981eb6d582916086e)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x1, 0x5) |
| #define | [USART0\_CLK\_PC0](#a9504215a474950cdc3ae3e76bb0ee428)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x0) |
| #define | [USART0\_CLK\_PC1](#aa03060eb71eadfc578315d600f297665)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x1) |
| #define | [USART0\_CLK\_PC2](#afd46249fb73936581af6f762bf749096)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x2) |
| #define | [USART0\_CLK\_PC3](#a39fd0a4cefb1903103818add5272cb69)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x3) |
| #define | [USART0\_CLK\_PC4](#a86e90f6c37f90fb2c79d163239123815)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x4) |
| #define | [USART0\_CLK\_PC5](#a13955f88c0655104ccceaf72d8fcc000)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x5) |
| #define | [USART0\_CLK\_PC6](#acd2b16c2082f7bbb996a7ba08a9339f6)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x6) |
| #define | [USART0\_CLK\_PC7](#af26cd974218fae8b631ed6bbc3505da6)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x7) |
| #define | [USART0\_CLK\_PC8](#a0a63d69334e7948f1eb02efe67272b6f)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x8) |
| #define | [USART0\_CLK\_PC9](#a11f0d43044117367cd5649c574288a06)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x9) |
| #define | [USART0\_CLK\_PD0](#aa5dd3eff1b983555e7437c815d69d6c1)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x3, 0x0) |
| #define | [USART0\_CLK\_PD1](#a808576a293b84b259f0b749099ee53f0)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x3, 0x1) |
| #define | [USART0\_CLK\_PD2](#aba6f9004672cd8fcc046036c5a5e385d)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x3, 0x2) |
| #define | [USART0\_CLK\_PD3](#acf11ed64457d633e70ba8551caaad511)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x3, 0x3) |
| #define | [USART0\_CLK\_PD4](#a8fa68ae31cbf6041854bd1de35efa747)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x3, 0x4) |
| #define | [USART0\_CLK\_PD5](#ac152b5f4693f5ca67901b7ce5b1f74c7)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x3, 0x5) |
| #define | [USART0\_TX\_PA0](#a4691259ca7c910831f70cff06b9737ac)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x0) |
| #define | [USART0\_TX\_PA1](#af4e1c897ae049a4b223e09ab587f116d)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x1) |
| #define | [USART0\_TX\_PA2](#acc13e25bcc1953b93e76521966cd1b39)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x2) |
| #define | [USART0\_TX\_PA3](#a2ccdea01de2b8da884a33ddc1a81982f)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x3) |
| #define | [USART0\_TX\_PA4](#a28450d0bc2dcbe2ead4d36cf3800eb03)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x4) |
| #define | [USART0\_TX\_PA5](#ab3851360e615c31434f53597b8012217)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x5) |
| #define | [USART0\_TX\_PA6](#a50d32b162eb8cfaee3228b4dd1aa2aef)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x6) |
| #define | [USART0\_TX\_PA7](#a237580d1c4d056bd0008418d21d8f1b3)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x7) |
| #define | [USART0\_TX\_PA8](#ae63baa716abe02654ea80133e8c84bd9)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x8) |
| #define | [USART0\_TX\_PA9](#a30e713d1552e2b140c92493463890e81)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x9) |
| #define | [USART0\_TX\_PB0](#a7af0455dce2acd605ef61cdc726c3177)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x1, 0x0) |
| #define | [USART0\_TX\_PB1](#a6ccc48b5e17aca0e2aefe341f9519ae9)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x1, 0x1) |
| #define | [USART0\_TX\_PB2](#a76f27605a95ea657c40e6911019756ec)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x1, 0x2) |
| #define | [USART0\_TX\_PB3](#a820d4c384913206beec9312430e68f9a)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x1, 0x3) |
| #define | [USART0\_TX\_PB4](#a3e2d2b7e3a0f2da1fd63cab3943aec5e)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x1, 0x4) |
| #define | [USART0\_TX\_PB5](#a633c75e84a048f8db768fde374cb2d0e)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x1, 0x5) |
| #define | [USART0\_TX\_PC0](#a63c1a984a64cb3c40643a7e38c20caaa)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x0) |
| #define | [USART0\_TX\_PC1](#ac501027215a6551a637bacf8d1d406fa)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x1) |
| #define | [USART0\_TX\_PC2](#ac1b7aad7c958ba2d2cfa2622318ac3c2)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x2) |
| #define | [USART0\_TX\_PC3](#aa215f604dc67f092f495c472de9a7ed5)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x3) |
| #define | [USART0\_TX\_PC4](#a1d49c843687f02f806c122059ac08a0c)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x4) |
| #define | [USART0\_TX\_PC5](#a03580c3dc9b22d031f78a0a3051b25de)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x5) |
| #define | [USART0\_TX\_PC6](#a3dc09745738d16673493a74870e6df5b)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x6) |
| #define | [USART0\_TX\_PC7](#a9c846b6972a8263d37ea9473b022f2dc)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x7) |
| #define | [USART0\_TX\_PC8](#a084114632892592ef47b04aa10862bc2)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x8) |
| #define | [USART0\_TX\_PC9](#a9ed42a0cb76a787a142496cd670aba2e)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x9) |
| #define | [USART0\_TX\_PD0](#a6756b78da6f6228f331b11a1a17be09d)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x3, 0x0) |
| #define | [USART0\_TX\_PD1](#a1a2e17d5a9daefa68e67b96957271b67)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x3, 0x1) |
| #define | [USART0\_TX\_PD2](#af52dcac08d3d9e0757048dbe7e0394b2)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x3, 0x2) |
| #define | [USART0\_TX\_PD3](#a51ef7d6af85db7597dd27a68c75fe4e9)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x3, 0x3) |
| #define | [USART0\_TX\_PD4](#a1d3a6020b34c9e101d510678ba45e28a)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x3, 0x4) |
| #define | [USART0\_TX\_PD5](#a23b627f9a203d88710c72107e3945349)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x3, 0x5) |
| #define | [USART0\_CTS\_PA0](#ac3ca642f56ef830b82675e79f7741f3b)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x0) |
| #define | [USART0\_CTS\_PA1](#afe282cc2c0b48daca846099518f85197)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x1) |
| #define | [USART0\_CTS\_PA2](#abb4ee35f35c67053d9e499b9b6586848)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x2) |
| #define | [USART0\_CTS\_PA3](#ac7c103a6f291a3ba02c78b56cda7522e)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x3) |
| #define | [USART0\_CTS\_PA4](#adf4ae6f16534af5c18b924890e70b909)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x4) |
| #define | [USART0\_CTS\_PA5](#a375e4336fc59220a304beb9e818038a8)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x5) |
| #define | [USART0\_CTS\_PA6](#a34bdfb80ac61bcde4828b64e5ab7bc6a)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x6) |
| #define | [USART0\_CTS\_PA7](#afe45fe9337ee945b705d60efd975071a)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x7) |
| #define | [USART0\_CTS\_PA8](#a45cbf3ce6396ad5caf50bca5bb336f04)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x8) |
| #define | [USART0\_CTS\_PA9](#aa310cb8173b02179e08e717af5117e6b)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x9) |
| #define | [USART0\_CTS\_PB0](#a5e6fd192eef4cb50593c5f8f225607db)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x1, 0x0) |
| #define | [USART0\_CTS\_PB1](#a8ba9df244ac2a7e580a45372c6db1496)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x1, 0x1) |
| #define | [USART0\_CTS\_PB2](#ac99b8ee386e51b37acfe825e4111dbd4)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x1, 0x2) |
| #define | [USART0\_CTS\_PB3](#a0c63835444cc57f402820f473de55618)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x1, 0x3) |
| #define | [USART0\_CTS\_PB4](#a2da02e86c7776fb1674ad0235c3c342a)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x1, 0x4) |
| #define | [USART0\_CTS\_PB5](#aab146714b510ce9d438cf61b25cee79e)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x1, 0x5) |
| #define | [USART0\_CTS\_PC0](#a176d8e361297cf55c78d425fed824f1f)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x0) |
| #define | [USART0\_CTS\_PC1](#acae624423e070b271d7c62019dc19ca6)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x1) |
| #define | [USART0\_CTS\_PC2](#a11af346f3b4cd506e5f42d802eeaa7fa)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x2) |
| #define | [USART0\_CTS\_PC3](#acde9eb8d5c61ec7fa0c66248de8acdb3)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x3) |
| #define | [USART0\_CTS\_PC4](#a0c7d39bd6f59e8a9281d68560e3ea0cc)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x4) |
| #define | [USART0\_CTS\_PC5](#aa2c0ec406645422286f3099c880051e8)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x5) |
| #define | [USART0\_CTS\_PC6](#a8886647e93011bfd9253bf57af7451f0)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x6) |
| #define | [USART0\_CTS\_PC7](#a8fc778b9808ef6cad5104cdee4c8b305)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x7) |
| #define | [USART0\_CTS\_PC8](#adfcf13e69aea1f02cb6874dce97dce31)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x8) |
| #define | [USART0\_CTS\_PC9](#a61b23cd8cf28189943376ef6787794b4)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x9) |
| #define | [USART0\_CTS\_PD0](#ad8f9198b67b3777baf4d6fa6771c2a40)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x3, 0x0) |
| #define | [USART0\_CTS\_PD1](#acf9112247d4fa36974b7e221d156b27c)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x3, 0x1) |
| #define | [USART0\_CTS\_PD2](#a86617a975bc950800ea9deba65ffaa19)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x3, 0x2) |
| #define | [USART0\_CTS\_PD3](#abf78324d648e5c035d29a33b4b93dd82)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x3, 0x3) |
| #define | [USART0\_CTS\_PD4](#a24a47d714bae303a53b15303fcc73855)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x3, 0x4) |
| #define | [USART0\_CTS\_PD5](#aaffa82b5324dfbac09e720731b7c7387)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x3, 0x5) |
| #define | [ABUS\_AEVEN0\_IADC0](#ad10d010cbdef8a32f14837ade41debfc)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x0, 0x1) |
| #define | [ABUS\_AEVEN0\_ACMP0](#a62a9951e869147c72fbe9c1e77e874fa)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x0, 0x2) |
| #define | [ABUS\_AEVEN0\_ACMP1](#a733fcfbe554356b950a5ccb44b5f16e2)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x0, 0x3) |
| #define | [ABUS\_AEVEN0\_VDAC0CH0](#af057b99023d4ad1119c1156fa84f8c7c)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x0, 0x4) |
| #define | [ABUS\_AEVEN0\_VDAC1CH0](#a53c309177b97c8b4f664cf17215cad28)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x0, 0x5) |
| #define | [ABUS\_AEVEN1\_IADC0](#a2a1cae8649645c367738b43ded59f749)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x1, 0x1) |
| #define | [ABUS\_AEVEN1\_ACMP0](#a8fde714bdb414359ff3619c3cb4dcad6)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x1, 0x2) |
| #define | [ABUS\_AEVEN1\_ACMP1](#a9e47fb539d308ac53088462e895a102c)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x1, 0x3) |
| #define | [ABUS\_AEVEN1\_VDAC0CH1](#ad3fdb11d275aa97a576cf502f88d3c1c)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x1, 0x4) |
| #define | [ABUS\_AEVEN1\_VDAC1CH1](#a7366d2b0b5e26be2037aba41d5bb2fa2)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x1, 0x5) |
| #define | [ABUS\_AODD0\_IADC0](#a566e8d018410bda1e988452fb5304441)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x2, 0x1) |
| #define | [ABUS\_AODD0\_ACMP0](#a23efcbf1afd4c5f08b8a01816879787b)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x2, 0x2) |
| #define | [ABUS\_AODD0\_ACMP1](#a0573c0fd5a1b22625e5985a8079bdfde)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x2, 0x3) |
| #define | [ABUS\_AODD0\_VDAC0CH0](#a28e43d0bc68d686a72b7b995bacd4602)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x2, 0x4) |
| #define | [ABUS\_AODD0\_VDAC1CH0](#a1631e3b1905c5ec8767611e1cac56041)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x2, 0x5) |
| #define | [ABUS\_AODD1\_IADC0](#aaa4617b296badc53ea3d2e297283c808)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x3, 0x1) |
| #define | [ABUS\_AODD1\_ACMP0](#abd2169342442333b350e32f881eff995)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x3, 0x2) |
| #define | [ABUS\_AODD1\_ACMP1](#a733a9a8b48bb7c0e35fa4c51ce6541af)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x3, 0x3) |
| #define | [ABUS\_AODD1\_VDAC0CH1](#a71f25b58a9ca52a961c209926441e54f)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x3, 0x4) |
| #define | [ABUS\_AODD1\_VDAC1CH1](#ac6fabf5ab0356c60b82e64e69dbd0cea)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x3, 0x5) |
| #define | [ABUS\_BEVEN0\_IADC0](#a2c5cafb1e8cc088300cbe61d33611daa)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x0, 0x1) |
| #define | [ABUS\_BEVEN0\_ACMP0](#a331630c1c48db7a35089f3a799eda1cb)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x0, 0x2) |
| #define | [ABUS\_BEVEN0\_ACMP1](#ac62950c7a5f0e549586ee6448c0c275e)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x0, 0x3) |
| #define | [ABUS\_BEVEN0\_VDAC0CH0](#af45cb77856c1b832ecc18d3ad292445f)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x0, 0x4) |
| #define | [ABUS\_BEVEN0\_VDAC1CH0](#a9052c4c346b04b9aa41cb2db465f01b6)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x0, 0x5) |
| #define | [ABUS\_BEVEN1\_IADC0](#a88d851648e8e5ed855ad2fa6c973284e)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x1, 0x1) |
| #define | [ABUS\_BEVEN1\_ACMP0](#aa920748827ffa55e353d0c1d3b6dd56a)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x1, 0x2) |
| #define | [ABUS\_BEVEN1\_ACMP1](#a6f85869fee80963d116a9cb8fb5191d6)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x1, 0x3) |
| #define | [ABUS\_BEVEN1\_VDAC0CH1](#a7d2db5c9f0d486efac010ff70b599a36)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x1, 0x4) |
| #define | [ABUS\_BEVEN1\_VDAC1CH1](#aafac1b9534ef3dcde45c04eb8007afdc)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x1, 0x5) |
| #define | [ABUS\_BODD0\_IADC0](#a8c77789600eea5e975b7d2b24c89f864)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x2, 0x1) |
| #define | [ABUS\_BODD0\_ACMP0](#a11259cd5a424085be1d843f934c82a15)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x2, 0x2) |
| #define | [ABUS\_BODD0\_ACMP1](#a523c439342947ae93bf8219322228af3)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x2, 0x3) |
| #define | [ABUS\_BODD0\_VDAC0CH0](#a1cbaab13ca704a4c7bada3ab64fbff1b)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x2, 0x4) |
| #define | [ABUS\_BODD0\_VDAC1CH0](#ac6b023702252f71ae7e4991ed669812a)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x2, 0x5) |
| #define | [ABUS\_BODD1\_IADC0](#aa5b85245f2fa86535920bd7d2ea837d1)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x3, 0x1) |
| #define | [ABUS\_BODD1\_ACMP0](#a4db6c1d2216c35ce68a76ff799d50138)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x3, 0x2) |
| #define | [ABUS\_BODD1\_ACMP1](#a14305213b34b0477f246b54b34328111)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x3, 0x3) |
| #define | [ABUS\_BODD1\_VDAC0CH1](#a602d4d62759643e6e97b0ca8a7d00f42)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x3, 0x4) |
| #define | [ABUS\_BODD1\_VDAC1CH1](#a6d3840868c15239d3bd403b1d73531fd)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x3, 0x5) |
| #define | [ABUS\_CDEVEN0\_IADC0](#af5928f28259fae0be44a365ba0a82cfe)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x0, 0x1) |
| #define | [ABUS\_CDEVEN0\_ACMP0](#a31e97c0380604db9ca894fb9805eb181)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x0, 0x2) |
| #define | [ABUS\_CDEVEN0\_ACMP1](#a992ea9f7d9e35327db0b8c31f903a735)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x0, 0x3) |
| #define | [ABUS\_CDEVEN0\_VDAC0CH0](#ad2edc248664688a578f52087ccdf13f5)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x0, 0x4) |
| #define | [ABUS\_CDEVEN0\_VDAC1CH0](#af1c0152b67a2c785dc6a0cebd4b3c2b1)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x0, 0x5) |
| #define | [ABUS\_CDEVEN1\_IADC0](#a7a2fc86a1027011d729324239a1858d4)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x1, 0x1) |
| #define | [ABUS\_CDEVEN1\_ACMP0](#a9c0f4b146a86a1031b59d7ab608c0374)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x1, 0x2) |
| #define | [ABUS\_CDEVEN1\_ACMP1](#af638e2cd7bd3a139bed94c7886938a11)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x1, 0x3) |
| #define | [ABUS\_CDEVEN1\_VDAC0CH1](#aa8d12343c7bd6f0e91fc3c65ab5d9845)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x1, 0x4) |
| #define | [ABUS\_CDEVEN1\_VDAC1CH1](#a15addcb2be19c465f6ef855fc86301dd)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x1, 0x5) |
| #define | [ABUS\_CDODD0\_IADC0](#a233653a6dffa4feece57164e50df6fc1)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x2, 0x1) |
| #define | [ABUS\_CDODD0\_ACMP0](#a79225667aa65dff641c32173f97dd8bc)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x2, 0x2) |
| #define | [ABUS\_CDODD0\_ACMP1](#a47795d1c947727f4ca611cbf9ff2cc68)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x2, 0x3) |
| #define | [ABUS\_CDODD0\_VDAC0CH0](#a671ba381410788d172f4f088fa6a53ff)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x2, 0x4) |
| #define | [ABUS\_CDODD0\_VDAC1CH0](#a86d70b3e8c84d9dc01965a239f92da85)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x2, 0x5) |
| #define | [ABUS\_CDODD1\_IADC0](#a4fc002977cffebe3a4d840f009d2afa2)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x3, 0x1) |
| #define | [ABUS\_CDODD1\_ACMP0](#aaac7b83053516a362770c72f813fd8ad)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x3, 0x2) |
| #define | [ABUS\_CDODD1\_ACMP1](#a10a761ac0260f4ee892a768405fa88c7)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x3, 0x3) |
| #define | [ABUS\_CDODD1\_VDAC0CH1](#aef7a3debf2fcaa34cfd68b062408ceb4)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x3, 0x4) |
| #define | [ABUS\_CDODD1\_VDAC1CH1](#a1b60a43921f58336a38b77ed7995c365)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x3, 0x5) |

## Macro Definition Documentation

## [◆ ](#a62a9951e869147c72fbe9c1e77e874fa)ABUS\_AEVEN0\_ACMP0

| #define ABUS\_AEVEN0\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x0, 0x2) |
| --- |

## [◆ ](#a733fcfbe554356b950a5ccb44b5f16e2)ABUS\_AEVEN0\_ACMP1

| #define ABUS\_AEVEN0\_ACMP1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x0, 0x3) |
| --- |

## [◆ ](#ad10d010cbdef8a32f14837ade41debfc)ABUS\_AEVEN0\_IADC0

| #define ABUS\_AEVEN0\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x0, 0x1) |
| --- |

## [◆ ](#af057b99023d4ad1119c1156fa84f8c7c)ABUS\_AEVEN0\_VDAC0CH0

| #define ABUS\_AEVEN0\_VDAC0CH0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x0, 0x4) |
| --- |

## [◆ ](#a53c309177b97c8b4f664cf17215cad28)ABUS\_AEVEN0\_VDAC1CH0

| #define ABUS\_AEVEN0\_VDAC1CH0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x0, 0x5) |
| --- |

## [◆ ](#a8fde714bdb414359ff3619c3cb4dcad6)ABUS\_AEVEN1\_ACMP0

| #define ABUS\_AEVEN1\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x1, 0x2) |
| --- |

## [◆ ](#a9e47fb539d308ac53088462e895a102c)ABUS\_AEVEN1\_ACMP1

| #define ABUS\_AEVEN1\_ACMP1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x1, 0x3) |
| --- |

## [◆ ](#a2a1cae8649645c367738b43ded59f749)ABUS\_AEVEN1\_IADC0

| #define ABUS\_AEVEN1\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x1, 0x1) |
| --- |

## [◆ ](#ad3fdb11d275aa97a576cf502f88d3c1c)ABUS\_AEVEN1\_VDAC0CH1

| #define ABUS\_AEVEN1\_VDAC0CH1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x1, 0x4) |
| --- |

## [◆ ](#a7366d2b0b5e26be2037aba41d5bb2fa2)ABUS\_AEVEN1\_VDAC1CH1

| #define ABUS\_AEVEN1\_VDAC1CH1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x1, 0x5) |
| --- |

## [◆ ](#a23efcbf1afd4c5f08b8a01816879787b)ABUS\_AODD0\_ACMP0

| #define ABUS\_AODD0\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x2, 0x2) |
| --- |

## [◆ ](#a0573c0fd5a1b22625e5985a8079bdfde)ABUS\_AODD0\_ACMP1

| #define ABUS\_AODD0\_ACMP1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x2, 0x3) |
| --- |

## [◆ ](#a566e8d018410bda1e988452fb5304441)ABUS\_AODD0\_IADC0

| #define ABUS\_AODD0\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x2, 0x1) |
| --- |

## [◆ ](#a28e43d0bc68d686a72b7b995bacd4602)ABUS\_AODD0\_VDAC0CH0

| #define ABUS\_AODD0\_VDAC0CH0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x2, 0x4) |
| --- |

## [◆ ](#a1631e3b1905c5ec8767611e1cac56041)ABUS\_AODD0\_VDAC1CH0

| #define ABUS\_AODD0\_VDAC1CH0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x2, 0x5) |
| --- |

## [◆ ](#abd2169342442333b350e32f881eff995)ABUS\_AODD1\_ACMP0

| #define ABUS\_AODD1\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x3, 0x2) |
| --- |

## [◆ ](#a733a9a8b48bb7c0e35fa4c51ce6541af)ABUS\_AODD1\_ACMP1

| #define ABUS\_AODD1\_ACMP1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x3, 0x3) |
| --- |

## [◆ ](#aaa4617b296badc53ea3d2e297283c808)ABUS\_AODD1\_IADC0

| #define ABUS\_AODD1\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x3, 0x1) |
| --- |

## [◆ ](#a71f25b58a9ca52a961c209926441e54f)ABUS\_AODD1\_VDAC0CH1

| #define ABUS\_AODD1\_VDAC0CH1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x3, 0x4) |
| --- |

## [◆ ](#ac6fabf5ab0356c60b82e64e69dbd0cea)ABUS\_AODD1\_VDAC1CH1

| #define ABUS\_AODD1\_VDAC1CH1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x3, 0x5) |
| --- |

## [◆ ](#a331630c1c48db7a35089f3a799eda1cb)ABUS\_BEVEN0\_ACMP0

| #define ABUS\_BEVEN0\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x0, 0x2) |
| --- |

## [◆ ](#ac62950c7a5f0e549586ee6448c0c275e)ABUS\_BEVEN0\_ACMP1

| #define ABUS\_BEVEN0\_ACMP1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x0, 0x3) |
| --- |

## [◆ ](#a2c5cafb1e8cc088300cbe61d33611daa)ABUS\_BEVEN0\_IADC0

| #define ABUS\_BEVEN0\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x0, 0x1) |
| --- |

## [◆ ](#af45cb77856c1b832ecc18d3ad292445f)ABUS\_BEVEN0\_VDAC0CH0

| #define ABUS\_BEVEN0\_VDAC0CH0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x0, 0x4) |
| --- |

## [◆ ](#a9052c4c346b04b9aa41cb2db465f01b6)ABUS\_BEVEN0\_VDAC1CH0

| #define ABUS\_BEVEN0\_VDAC1CH0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x0, 0x5) |
| --- |

## [◆ ](#aa920748827ffa55e353d0c1d3b6dd56a)ABUS\_BEVEN1\_ACMP0

| #define ABUS\_BEVEN1\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x1, 0x2) |
| --- |

## [◆ ](#a6f85869fee80963d116a9cb8fb5191d6)ABUS\_BEVEN1\_ACMP1

| #define ABUS\_BEVEN1\_ACMP1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x1, 0x3) |
| --- |

## [◆ ](#a88d851648e8e5ed855ad2fa6c973284e)ABUS\_BEVEN1\_IADC0

| #define ABUS\_BEVEN1\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x1, 0x1) |
| --- |

## [◆ ](#a7d2db5c9f0d486efac010ff70b599a36)ABUS\_BEVEN1\_VDAC0CH1

| #define ABUS\_BEVEN1\_VDAC0CH1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x1, 0x4) |
| --- |

## [◆ ](#aafac1b9534ef3dcde45c04eb8007afdc)ABUS\_BEVEN1\_VDAC1CH1

| #define ABUS\_BEVEN1\_VDAC1CH1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x1, 0x5) |
| --- |

## [◆ ](#a11259cd5a424085be1d843f934c82a15)ABUS\_BODD0\_ACMP0

| #define ABUS\_BODD0\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x2, 0x2) |
| --- |

## [◆ ](#a523c439342947ae93bf8219322228af3)ABUS\_BODD0\_ACMP1

| #define ABUS\_BODD0\_ACMP1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x2, 0x3) |
| --- |

## [◆ ](#a8c77789600eea5e975b7d2b24c89f864)ABUS\_BODD0\_IADC0

| #define ABUS\_BODD0\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x2, 0x1) |
| --- |

## [◆ ](#a1cbaab13ca704a4c7bada3ab64fbff1b)ABUS\_BODD0\_VDAC0CH0

| #define ABUS\_BODD0\_VDAC0CH0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x2, 0x4) |
| --- |

## [◆ ](#ac6b023702252f71ae7e4991ed669812a)ABUS\_BODD0\_VDAC1CH0

| #define ABUS\_BODD0\_VDAC1CH0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x2, 0x5) |
| --- |

## [◆ ](#a4db6c1d2216c35ce68a76ff799d50138)ABUS\_BODD1\_ACMP0

| #define ABUS\_BODD1\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x3, 0x2) |
| --- |

## [◆ ](#a14305213b34b0477f246b54b34328111)ABUS\_BODD1\_ACMP1

| #define ABUS\_BODD1\_ACMP1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x3, 0x3) |
| --- |

## [◆ ](#aa5b85245f2fa86535920bd7d2ea837d1)ABUS\_BODD1\_IADC0

| #define ABUS\_BODD1\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x3, 0x1) |
| --- |

## [◆ ](#a602d4d62759643e6e97b0ca8a7d00f42)ABUS\_BODD1\_VDAC0CH1

| #define ABUS\_BODD1\_VDAC0CH1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x3, 0x4) |
| --- |

## [◆ ](#a6d3840868c15239d3bd403b1d73531fd)ABUS\_BODD1\_VDAC1CH1

| #define ABUS\_BODD1\_VDAC1CH1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x3, 0x5) |
| --- |

## [◆ ](#a31e97c0380604db9ca894fb9805eb181)ABUS\_CDEVEN0\_ACMP0

| #define ABUS\_CDEVEN0\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x0, 0x2) |
| --- |

## [◆ ](#a992ea9f7d9e35327db0b8c31f903a735)ABUS\_CDEVEN0\_ACMP1

| #define ABUS\_CDEVEN0\_ACMP1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x0, 0x3) |
| --- |

## [◆ ](#af5928f28259fae0be44a365ba0a82cfe)ABUS\_CDEVEN0\_IADC0

| #define ABUS\_CDEVEN0\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x0, 0x1) |
| --- |

## [◆ ](#ad2edc248664688a578f52087ccdf13f5)ABUS\_CDEVEN0\_VDAC0CH0

| #define ABUS\_CDEVEN0\_VDAC0CH0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x0, 0x4) |
| --- |

## [◆ ](#af1c0152b67a2c785dc6a0cebd4b3c2b1)ABUS\_CDEVEN0\_VDAC1CH0

| #define ABUS\_CDEVEN0\_VDAC1CH0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x0, 0x5) |
| --- |

## [◆ ](#a9c0f4b146a86a1031b59d7ab608c0374)ABUS\_CDEVEN1\_ACMP0

| #define ABUS\_CDEVEN1\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x1, 0x2) |
| --- |

## [◆ ](#af638e2cd7bd3a139bed94c7886938a11)ABUS\_CDEVEN1\_ACMP1

| #define ABUS\_CDEVEN1\_ACMP1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x1, 0x3) |
| --- |

## [◆ ](#a7a2fc86a1027011d729324239a1858d4)ABUS\_CDEVEN1\_IADC0

| #define ABUS\_CDEVEN1\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x1, 0x1) |
| --- |

## [◆ ](#aa8d12343c7bd6f0e91fc3c65ab5d9845)ABUS\_CDEVEN1\_VDAC0CH1

| #define ABUS\_CDEVEN1\_VDAC0CH1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x1, 0x4) |
| --- |

## [◆ ](#a15addcb2be19c465f6ef855fc86301dd)ABUS\_CDEVEN1\_VDAC1CH1

| #define ABUS\_CDEVEN1\_VDAC1CH1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x1, 0x5) |
| --- |

## [◆ ](#a79225667aa65dff641c32173f97dd8bc)ABUS\_CDODD0\_ACMP0

| #define ABUS\_CDODD0\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x2, 0x2) |
| --- |

## [◆ ](#a47795d1c947727f4ca611cbf9ff2cc68)ABUS\_CDODD0\_ACMP1

| #define ABUS\_CDODD0\_ACMP1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x2, 0x3) |
| --- |

## [◆ ](#a233653a6dffa4feece57164e50df6fc1)ABUS\_CDODD0\_IADC0

| #define ABUS\_CDODD0\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x2, 0x1) |
| --- |

## [◆ ](#a671ba381410788d172f4f088fa6a53ff)ABUS\_CDODD0\_VDAC0CH0

| #define ABUS\_CDODD0\_VDAC0CH0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x2, 0x4) |
| --- |

## [◆ ](#a86d70b3e8c84d9dc01965a239f92da85)ABUS\_CDODD0\_VDAC1CH0

| #define ABUS\_CDODD0\_VDAC1CH0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x2, 0x5) |
| --- |

## [◆ ](#aaac7b83053516a362770c72f813fd8ad)ABUS\_CDODD1\_ACMP0

| #define ABUS\_CDODD1\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x3, 0x2) |
| --- |

## [◆ ](#a10a761ac0260f4ee892a768405fa88c7)ABUS\_CDODD1\_ACMP1

| #define ABUS\_CDODD1\_ACMP1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x3, 0x3) |
| --- |

## [◆ ](#a4fc002977cffebe3a4d840f009d2afa2)ABUS\_CDODD1\_IADC0

| #define ABUS\_CDODD1\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x3, 0x1) |
| --- |

## [◆ ](#aef7a3debf2fcaa34cfd68b062408ceb4)ABUS\_CDODD1\_VDAC0CH1

| #define ABUS\_CDODD1\_VDAC0CH1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x3, 0x4) |
| --- |

## [◆ ](#a1b60a43921f58336a38b77ed7995c365)ABUS\_CDODD1\_VDAC1CH1

| #define ABUS\_CDODD1\_VDAC1CH1   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x3, 0x5) |
| --- |

## [◆ ](#aedfa1c8d8e52b69e24b4c5ae55906dc6)ACMP0\_ACMPOUT\_PA0

| #define ACMP0\_ACMPOUT\_PA0   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x0) |
| --- |

## [◆ ](#afc43fb1cb74d95db1aceffc3b55fe017)ACMP0\_ACMPOUT\_PA1

| #define ACMP0\_ACMPOUT\_PA1   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x1) |
| --- |

## [◆ ](#ad609c06187830519865e977ad663e8a9)ACMP0\_ACMPOUT\_PA2

| #define ACMP0\_ACMPOUT\_PA2   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x2) |
| --- |

## [◆ ](#ab46e5bad6ae8864f903d86d60c3b08b2)ACMP0\_ACMPOUT\_PA3

| #define ACMP0\_ACMPOUT\_PA3   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x3) |
| --- |

## [◆ ](#acb82f83c6665cac86a44ffb88689e1f8)ACMP0\_ACMPOUT\_PA4

| #define ACMP0\_ACMPOUT\_PA4   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x4) |
| --- |

## [◆ ](#ae3d76d092e7875eac30dbc243b3ded51)ACMP0\_ACMPOUT\_PA5

| #define ACMP0\_ACMPOUT\_PA5   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x5) |
| --- |

## [◆ ](#a83b7f7e01fea7985ff1b739474e57015)ACMP0\_ACMPOUT\_PA6

| #define ACMP0\_ACMPOUT\_PA6   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x6) |
| --- |

## [◆ ](#ae42719fd5ec147180ae465dd40175867)ACMP0\_ACMPOUT\_PA7

| #define ACMP0\_ACMPOUT\_PA7   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x7) |
| --- |

## [◆ ](#a2e14f2d26d737657b252e5c6764d28af)ACMP0\_ACMPOUT\_PA8

| #define ACMP0\_ACMPOUT\_PA8   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x8) |
| --- |

## [◆ ](#a3f8caec7c93f1f90e507259873143715)ACMP0\_ACMPOUT\_PA9

| #define ACMP0\_ACMPOUT\_PA9   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x9) |
| --- |

## [◆ ](#a36b9f71114e84ffb46fc8d52b7a87046)ACMP0\_ACMPOUT\_PB0

| #define ACMP0\_ACMPOUT\_PB0   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x1, 0x0) |
| --- |

## [◆ ](#ad7205c69934692bea6a1c31e9b374eef)ACMP0\_ACMPOUT\_PB1

| #define ACMP0\_ACMPOUT\_PB1   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x1, 0x1) |
| --- |

## [◆ ](#a17952d489dca95115341cf1052e9dc40)ACMP0\_ACMPOUT\_PB2

| #define ACMP0\_ACMPOUT\_PB2   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x1, 0x2) |
| --- |

## [◆ ](#a7455d069c13e82b9ef92b9cf82d4528a)ACMP0\_ACMPOUT\_PB3

| #define ACMP0\_ACMPOUT\_PB3   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x1, 0x3) |
| --- |

## [◆ ](#a9c5d85ede4da946e89f0a28bd78ce723)ACMP0\_ACMPOUT\_PB4

| #define ACMP0\_ACMPOUT\_PB4   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x1, 0x4) |
| --- |

## [◆ ](#a075c5cbd27027e4eab08230f9bf49d26)ACMP0\_ACMPOUT\_PB5

| #define ACMP0\_ACMPOUT\_PB5   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x1, 0x5) |
| --- |

## [◆ ](#a5b32e3f7e8bfdc37a87a1e5400897df8)ACMP0\_ACMPOUT\_PC0

| #define ACMP0\_ACMPOUT\_PC0   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x0) |
| --- |

## [◆ ](#a8c6a859a56f83fe76898e7e5d251d0b3)ACMP0\_ACMPOUT\_PC1

| #define ACMP0\_ACMPOUT\_PC1   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x1) |
| --- |

## [◆ ](#abc756f46419f529864d1f5373df967fa)ACMP0\_ACMPOUT\_PC2

| #define ACMP0\_ACMPOUT\_PC2   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x2) |
| --- |

## [◆ ](#acf2975d5be55d86f12c69c12dd257c02)ACMP0\_ACMPOUT\_PC3

| #define ACMP0\_ACMPOUT\_PC3   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x3) |
| --- |

## [◆ ](#a3e87af3956c8d9b54f210c3c9ce25fe2)ACMP0\_ACMPOUT\_PC4

| #define ACMP0\_ACMPOUT\_PC4   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x4) |
| --- |

## [◆ ](#a02cb0bfeb435f2d76adf0624c9acc380)ACMP0\_ACMPOUT\_PC5

| #define ACMP0\_ACMPOUT\_PC5   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x5) |
| --- |

## [◆ ](#a38b79026393006be7b6e6f57e90f194c)ACMP0\_ACMPOUT\_PC6

| #define ACMP0\_ACMPOUT\_PC6   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x6) |
| --- |

## [◆ ](#a8d166fe3ba9340f393a6f43167c70d1f)ACMP0\_ACMPOUT\_PC7

| #define ACMP0\_ACMPOUT\_PC7   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x7) |
| --- |

## [◆ ](#ac8934c49c62c45fb2679b7faea22b8cd)ACMP0\_ACMPOUT\_PC8

| #define ACMP0\_ACMPOUT\_PC8   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x8) |
| --- |

## [◆ ](#a4c4ed2c8940129833454a9dbb3a23f05)ACMP0\_ACMPOUT\_PC9

| #define ACMP0\_ACMPOUT\_PC9   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x9) |
| --- |

## [◆ ](#a196c859ab39c4e7fea903085f0091f38)ACMP0\_ACMPOUT\_PD0

| #define ACMP0\_ACMPOUT\_PD0   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x3, 0x0) |
| --- |

## [◆ ](#aabae5292f25eac5b7f235c1613a4abfe)ACMP0\_ACMPOUT\_PD1

| #define ACMP0\_ACMPOUT\_PD1   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x3, 0x1) |
| --- |

## [◆ ](#af0c00ac6edb9696207c0688dd902889c)ACMP0\_ACMPOUT\_PD2

| #define ACMP0\_ACMPOUT\_PD2   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x3, 0x2) |
| --- |

## [◆ ](#a22cc57aac83e922695ce9765daca5a22)ACMP0\_ACMPOUT\_PD3

| #define ACMP0\_ACMPOUT\_PD3   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x3, 0x3) |
| --- |

## [◆ ](#a046027b3929f25e781e6f294783bc1a0)ACMP0\_ACMPOUT\_PD4

| #define ACMP0\_ACMPOUT\_PD4   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x3, 0x4) |
| --- |

## [◆ ](#a4dbdab365c718b1f64adc02a23d5bf4a)ACMP0\_ACMPOUT\_PD5

| #define ACMP0\_ACMPOUT\_PD5   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x3, 0x5) |
| --- |

## [◆ ](#a04aca20b5e493a872ba32bbd78b47a5a)ACMP1\_ACMPOUT\_PA0

| #define ACMP1\_ACMPOUT\_PA0   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x0) |
| --- |

## [◆ ](#aaa76825f32591d5e0921624dc9c7a547)ACMP1\_ACMPOUT\_PA1

| #define ACMP1\_ACMPOUT\_PA1   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x1) |
| --- |

## [◆ ](#a7e6b677b9f6fdf424146fe7bd16b8ab6)ACMP1\_ACMPOUT\_PA2

| #define ACMP1\_ACMPOUT\_PA2   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x2) |
| --- |

## [◆ ](#a519bb19bf1c5adb7a4c236260e19cb93)ACMP1\_ACMPOUT\_PA3

| #define ACMP1\_ACMPOUT\_PA3   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x3) |
| --- |

## [◆ ](#ae5cd234e221d2b8308334d877bc27e05)ACMP1\_ACMPOUT\_PA4

| #define ACMP1\_ACMPOUT\_PA4   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x4) |
| --- |

## [◆ ](#ae03013868fb1238d33b1c584509d891e)ACMP1\_ACMPOUT\_PA5

| #define ACMP1\_ACMPOUT\_PA5   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x5) |
| --- |

## [◆ ](#a541b4fdb8b53c3d920a588376126a7f2)ACMP1\_ACMPOUT\_PA6

| #define ACMP1\_ACMPOUT\_PA6   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x6) |
| --- |

## [◆ ](#a9693060d6ad6e4dbae35d88c03bbb040)ACMP1\_ACMPOUT\_PA7

| #define ACMP1\_ACMPOUT\_PA7   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x7) |
| --- |

## [◆ ](#a83aa9f91e580282d4aabc94eadc6e432)ACMP1\_ACMPOUT\_PA8

| #define ACMP1\_ACMPOUT\_PA8   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x8) |
| --- |

## [◆ ](#aff7884ab918b0a75ec62bcd2c9b7a44e)ACMP1\_ACMPOUT\_PA9

| #define ACMP1\_ACMPOUT\_PA9   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x0, 0x9) |
| --- |

## [◆ ](#a84f6c6945835113f9918687cb295093b)ACMP1\_ACMPOUT\_PB0

| #define ACMP1\_ACMPOUT\_PB0   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x1, 0x0) |
| --- |

## [◆ ](#ac7ddbcf4f3906bc2e71b21b0ebada790)ACMP1\_ACMPOUT\_PB1

| #define ACMP1\_ACMPOUT\_PB1   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x1, 0x1) |
| --- |

## [◆ ](#a1e450275c12cc32003c239bb81741130)ACMP1\_ACMPOUT\_PB2

| #define ACMP1\_ACMPOUT\_PB2   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x1, 0x2) |
| --- |

## [◆ ](#a67d1e01a6af363373919428beb5780c5)ACMP1\_ACMPOUT\_PB3

| #define ACMP1\_ACMPOUT\_PB3   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x1, 0x3) |
| --- |

## [◆ ](#af896153a63d5ac12600afd9899647efa)ACMP1\_ACMPOUT\_PB4

| #define ACMP1\_ACMPOUT\_PB4   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x1, 0x4) |
| --- |

## [◆ ](#a97f817f9966a9a08d8ab5cd3e7ba0ba9)ACMP1\_ACMPOUT\_PB5

| #define ACMP1\_ACMPOUT\_PB5   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x1, 0x5) |
| --- |

## [◆ ](#aa98b56734d6c562982b62d2fae788a64)ACMP1\_ACMPOUT\_PC0

| #define ACMP1\_ACMPOUT\_PC0   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x0) |
| --- |

## [◆ ](#a623a2fbee184e239f5c4c1899b80b146)ACMP1\_ACMPOUT\_PC1

| #define ACMP1\_ACMPOUT\_PC1   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x1) |
| --- |

## [◆ ](#a9c1ad020fb2a75438324fca26e791d19)ACMP1\_ACMPOUT\_PC2

| #define ACMP1\_ACMPOUT\_PC2   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x2) |
| --- |

## [◆ ](#acbfcff70ab4cc6aec772a8f5f6a5c559)ACMP1\_ACMPOUT\_PC3

| #define ACMP1\_ACMPOUT\_PC3   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x3) |
| --- |

## [◆ ](#aeeef7ef4dfcb0a12adacd9718f04f43b)ACMP1\_ACMPOUT\_PC4

| #define ACMP1\_ACMPOUT\_PC4   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x4) |
| --- |

## [◆ ](#a4b15ffe9e4ecd23d7242b062e5cbc082)ACMP1\_ACMPOUT\_PC5

| #define ACMP1\_ACMPOUT\_PC5   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x5) |
| --- |

## [◆ ](#ad4db37359084a42fea18f9c2521496c8)ACMP1\_ACMPOUT\_PC6

| #define ACMP1\_ACMPOUT\_PC6   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x6) |
| --- |

## [◆ ](#ad030633794a7f05c0cee0c06bb81d087)ACMP1\_ACMPOUT\_PC7

| #define ACMP1\_ACMPOUT\_PC7   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x7) |
| --- |

## [◆ ](#abde1f8f36169f539391976f6a589ab8f)ACMP1\_ACMPOUT\_PC8

| #define ACMP1\_ACMPOUT\_PC8   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x8) |
| --- |

## [◆ ](#a59cb718dc4a0eaf46715ce9bfae59fdb)ACMP1\_ACMPOUT\_PC9

| #define ACMP1\_ACMPOUT\_PC9   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x2, 0x9) |
| --- |

## [◆ ](#a0ca6370f146e12eece2dc87e0e322f62)ACMP1\_ACMPOUT\_PD0

| #define ACMP1\_ACMPOUT\_PD0   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x3, 0x0) |
| --- |

## [◆ ](#ae49cd1f217b75138cca0f43b8770b1bc)ACMP1\_ACMPOUT\_PD1

| #define ACMP1\_ACMPOUT\_PD1   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x3, 0x1) |
| --- |

## [◆ ](#ad9a1898895b78944b14493df85e3ee21)ACMP1\_ACMPOUT\_PD2

| #define ACMP1\_ACMPOUT\_PD2   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x3, 0x2) |
| --- |

## [◆ ](#a02fa7898cc55e75ac1bd8634cf4bd859)ACMP1\_ACMPOUT\_PD3

| #define ACMP1\_ACMPOUT\_PD3   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x3, 0x3) |
| --- |

## [◆ ](#ab46a58b4ccb7b62fabb73110eb2b8e46)ACMP1\_ACMPOUT\_PD4

| #define ACMP1\_ACMPOUT\_PD4   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x3, 0x4) |
| --- |

## [◆ ](#aac3861fba05ede584b08637cc9214a62)ACMP1\_ACMPOUT\_PD5

| #define ACMP1\_ACMPOUT\_PD5   [SILABS\_DBUS\_ACMP1\_ACMPOUT](#a12ac63e4d5ed67a2a3f7425b751cdec3)(0x3, 0x5) |
| --- |

## [◆ ](#a4aaa42a036d18c3f1acb7def83fb9f05)CMU\_CLKIN0\_PC0

| #define CMU\_CLKIN0\_PC0   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x0) |
| --- |

## [◆ ](#ad099af25ca0f801ff85e3071a1cda472)CMU\_CLKIN0\_PC1

| #define CMU\_CLKIN0\_PC1   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x1) |
| --- |

## [◆ ](#add3b048d2455419255aedcef16aed776)CMU\_CLKIN0\_PC2

| #define CMU\_CLKIN0\_PC2   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x2) |
| --- |

## [◆ ](#a59c6d813c66884cb9db67d4e6c1cd8d4)CMU\_CLKIN0\_PC3

| #define CMU\_CLKIN0\_PC3   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x3) |
| --- |

## [◆ ](#a4528f4ea777e78b8f27bd604bfeaf59e)CMU\_CLKIN0\_PC4

| #define CMU\_CLKIN0\_PC4   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x4) |
| --- |

## [◆ ](#a5f79eddd69ce5550c1fd8ee07ce0ad9c)CMU\_CLKIN0\_PC5

| #define CMU\_CLKIN0\_PC5   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x5) |
| --- |

## [◆ ](#ab3ac5c61d6e2ba07c8d17e313ff61631)CMU\_CLKIN0\_PC6

| #define CMU\_CLKIN0\_PC6   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x6) |
| --- |

## [◆ ](#a50bb44be738315ef4409c4310d93f7aa)CMU\_CLKIN0\_PC7

| #define CMU\_CLKIN0\_PC7   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x7) |
| --- |

## [◆ ](#aa6fd2707f5f441a5f3b02425b400a155)CMU\_CLKIN0\_PC8

| #define CMU\_CLKIN0\_PC8   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x8) |
| --- |

## [◆ ](#a577cbe545692020844b1756af5dd0bc7)CMU\_CLKIN0\_PC9

| #define CMU\_CLKIN0\_PC9   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x9) |
| --- |

## [◆ ](#a8d96e9e617c1f18f2bd0a2ac65e98ae1)CMU\_CLKIN0\_PD0

| #define CMU\_CLKIN0\_PD0   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x3, 0x0) |
| --- |

## [◆ ](#aa780fb9850bc6efcb36d8dd19770ec27)CMU\_CLKIN0\_PD1

| #define CMU\_CLKIN0\_PD1   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x3, 0x1) |
| --- |

## [◆ ](#ad27e93b39cdcd25b3d3ba89f01a05019)CMU\_CLKIN0\_PD2

| #define CMU\_CLKIN0\_PD2   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x3, 0x2) |
| --- |

## [◆ ](#aec9648fbe6bece6f7cec5b3942eda3a0)CMU\_CLKIN0\_PD3

| #define CMU\_CLKIN0\_PD3   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x3, 0x3) |
| --- |

## [◆ ](#a9791109179057e8535cccfb2292ea5cd)CMU\_CLKIN0\_PD4

| #define CMU\_CLKIN0\_PD4   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x3, 0x4) |
| --- |

## [◆ ](#ae2fddef4c421ea232fdb57927c928723)CMU\_CLKIN0\_PD5

| #define CMU\_CLKIN0\_PD5   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x3, 0x5) |
| --- |

## [◆ ](#a750738e1a4c7ed8bfb4d2f9151267da6)CMU\_CLKOUT0\_PC0

| #define CMU\_CLKOUT0\_PC0   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x0) |
| --- |

## [◆ ](#a31916418c44431216dea609cb5aef35a)CMU\_CLKOUT0\_PC1

| #define CMU\_CLKOUT0\_PC1   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x1) |
| --- |

## [◆ ](#a90c69d0d98a225b058598397e960c41d)CMU\_CLKOUT0\_PC2

| #define CMU\_CLKOUT0\_PC2   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x2) |
| --- |

## [◆ ](#a502a3e471c068d2ae94fc2255b3680dd)CMU\_CLKOUT0\_PC3

| #define CMU\_CLKOUT0\_PC3   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x3) |
| --- |

## [◆ ](#a0af75594d7d55c0bf77021f81b058ef6)CMU\_CLKOUT0\_PC4

| #define CMU\_CLKOUT0\_PC4   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x4) |
| --- |

## [◆ ](#a3bfddaaeba9558824977b108319c26b1)CMU\_CLKOUT0\_PC5

| #define CMU\_CLKOUT0\_PC5   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x5) |
| --- |

## [◆ ](#a7c63df02e41810547afb13b879dbf602)CMU\_CLKOUT0\_PC6

| #define CMU\_CLKOUT0\_PC6   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x6) |
| --- |

## [◆ ](#aa219ec0869e6e96ce5a84ed7dbba3d06)CMU\_CLKOUT0\_PC7

| #define CMU\_CLKOUT0\_PC7   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x7) |
| --- |

## [◆ ](#aab39df8a873b3e6c0900d5e791a3f867)CMU\_CLKOUT0\_PC8

| #define CMU\_CLKOUT0\_PC8   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x8) |
| --- |

## [◆ ](#ad3f15ec5c750f7ffc8ba8ab07167e802)CMU\_CLKOUT0\_PC9

| #define CMU\_CLKOUT0\_PC9   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x9) |
| --- |

## [◆ ](#a1afed05e5d9d89ad251e77f94f1e745d)CMU\_CLKOUT0\_PD0

| #define CMU\_CLKOUT0\_PD0   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x3, 0x0) |
| --- |

## [◆ ](#a4cc3f9b8c22e11a9ffd40149c990d09d)CMU\_CLKOUT0\_PD1

| #define CMU\_CLKOUT0\_PD1   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x3, 0x1) |
| --- |

## [◆ ](#a823b6e29d70a1313ed81cae432648f73)CMU\_CLKOUT0\_PD2

| #define CMU\_CLKOUT0\_PD2   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x3, 0x2) |
| --- |

## [◆ ](#a4223cab1734f1dadac546c956ae17f66)CMU\_CLKOUT0\_PD3

| #define CMU\_CLKOUT0\_PD3   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x3, 0x3) |
| --- |

## [◆ ](#a45bd684b5ac8c0899bfce5901e372aa3)CMU\_CLKOUT0\_PD4

| #define CMU\_CLKOUT0\_PD4   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x3, 0x4) |
| --- |

## [◆ ](#a788945f76f25d0bdb52a0386ac0bd8bb)CMU\_CLKOUT0\_PD5

| #define CMU\_CLKOUT0\_PD5   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x3, 0x5) |
| --- |

## [◆ ](#a7b57f126203047b4cb82d0eff5c1ba8f)CMU\_CLKOUT1\_PC0

| #define CMU\_CLKOUT1\_PC0   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x0) |
| --- |

## [◆ ](#a7742937a9e0afe5ae4859f9fe6373ca3)CMU\_CLKOUT1\_PC1

| #define CMU\_CLKOUT1\_PC1   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x1) |
| --- |

## [◆ ](#ae634d0e26da5dd095bf98854cd95e6c9)CMU\_CLKOUT1\_PC2

| #define CMU\_CLKOUT1\_PC2   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x2) |
| --- |

## [◆ ](#afecc3d613acceb752470037c6c253759)CMU\_CLKOUT1\_PC3

| #define CMU\_CLKOUT1\_PC3   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x3) |
| --- |

## [◆ ](#a2d21eabc4603c5cfd93cd0eed5708565)CMU\_CLKOUT1\_PC4

| #define CMU\_CLKOUT1\_PC4   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x4) |
| --- |

## [◆ ](#a8287c02ea2823803c7f3415597aeb0f8)CMU\_CLKOUT1\_PC5

| #define CMU\_CLKOUT1\_PC5   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x5) |
| --- |

## [◆ ](#aed9fe929699b234ddcd9c5d814d309fc)CMU\_CLKOUT1\_PC6

| #define CMU\_CLKOUT1\_PC6   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x6) |
| --- |

## [◆ ](#af72caa6a5612d497402a76ac0d5e2d12)CMU\_CLKOUT1\_PC7

| #define CMU\_CLKOUT1\_PC7   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x7) |
| --- |

## [◆ ](#a04edc510b099491995f03e3c6bd160f6)CMU\_CLKOUT1\_PC8

| #define CMU\_CLKOUT1\_PC8   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x8) |
| --- |

## [◆ ](#ac3693e451d931359dbc2c79ec323a4b6)CMU\_CLKOUT1\_PC9

| #define CMU\_CLKOUT1\_PC9   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x9) |
| --- |

## [◆ ](#a9041e78bd2f530d25db4d36d783e04ff)CMU\_CLKOUT1\_PD0

| #define CMU\_CLKOUT1\_PD0   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x3, 0x0) |
| --- |

## [◆ ](#a65ab333bdb97055f6e69f17a46cc76ca)CMU\_CLKOUT1\_PD1

| #define CMU\_CLKOUT1\_PD1   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x3, 0x1) |
| --- |

## [◆ ](#ad6f97e49e9ed6808c2631547fae12fd0)CMU\_CLKOUT1\_PD2

| #define CMU\_CLKOUT1\_PD2   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x3, 0x2) |
| --- |

## [◆ ](#afc01df4895e8d3e104bbff29227824a8)CMU\_CLKOUT1\_PD3

| #define CMU\_CLKOUT1\_PD3   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x3, 0x3) |
| --- |

## [◆ ](#afd198f9e83c2b18208b42bb5f196ddb5)CMU\_CLKOUT1\_PD4

| #define CMU\_CLKOUT1\_PD4   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x3, 0x4) |
| --- |

## [◆ ](#a9a691758e704ccc7312ea85e620c4796)CMU\_CLKOUT1\_PD5

| #define CMU\_CLKOUT1\_PD5   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x3, 0x5) |
| --- |

## [◆ ](#a515401133e23f38d0c7babc3b8cffb18)CMU\_CLKOUT2\_PA0

| #define CMU\_CLKOUT2\_PA0   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x0) |
| --- |

## [◆ ](#ae765fe590bab12a1671c57b20b69e354)CMU\_CLKOUT2\_PA1

| #define CMU\_CLKOUT2\_PA1   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x1) |
| --- |

## [◆ ](#a4183040a304b3d85d3b382d28176da03)CMU\_CLKOUT2\_PA2

| #define CMU\_CLKOUT2\_PA2   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x2) |
| --- |

## [◆ ](#a65e82802fc3e2e3eb089eaa3bb4b1207)CMU\_CLKOUT2\_PA3

| #define CMU\_CLKOUT2\_PA3   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x3) |
| --- |

## [◆ ](#a9345663284354ee2c4b5ebd6a4124234)CMU\_CLKOUT2\_PA4

| #define CMU\_CLKOUT2\_PA4   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x4) |
| --- |

## [◆ ](#ac1767819afb4418dfb8de4ec2114144f)CMU\_CLKOUT2\_PA5

| #define CMU\_CLKOUT2\_PA5   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x5) |
| --- |

## [◆ ](#a078e7abf21f63f21617ea47fd565fcc0)CMU\_CLKOUT2\_PA6

| #define CMU\_CLKOUT2\_PA6   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x6) |
| --- |

## [◆ ](#a0ad411783ff7e13b2965931269fc8c8b)CMU\_CLKOUT2\_PA7

| #define CMU\_CLKOUT2\_PA7   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x7) |
| --- |

## [◆ ](#a0ea1041e58653ac225cacb25cd747970)CMU\_CLKOUT2\_PA8

| #define CMU\_CLKOUT2\_PA8   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x8) |
| --- |

## [◆ ](#a36754f6ea866cf3f6f6df6366946948a)CMU\_CLKOUT2\_PA9

| #define CMU\_CLKOUT2\_PA9   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x9) |
| --- |

## [◆ ](#a7f82072ef8014d5497df30c927b0d6f9)CMU\_CLKOUT2\_PB0

| #define CMU\_CLKOUT2\_PB0   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x1, 0x0) |
| --- |

## [◆ ](#af815e3c4392ba1686e4f77dc0b6911f1)CMU\_CLKOUT2\_PB1

| #define CMU\_CLKOUT2\_PB1   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x1, 0x1) |
| --- |

## [◆ ](#a9613c5b45ba73bc69011086baafad84c)CMU\_CLKOUT2\_PB2

| #define CMU\_CLKOUT2\_PB2   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x1, 0x2) |
| --- |

## [◆ ](#ac8e00ea8020085f156d66e741d7fa185)CMU\_CLKOUT2\_PB3

| #define CMU\_CLKOUT2\_PB3   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x1, 0x3) |
| --- |

## [◆ ](#a003c45e0a49fdb695df7d930f16ff20b)CMU\_CLKOUT2\_PB4

| #define CMU\_CLKOUT2\_PB4   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x1, 0x4) |
| --- |

## [◆ ](#a1128af6c3950b3e6eedea125be964f22)CMU\_CLKOUT2\_PB5

| #define CMU\_CLKOUT2\_PB5   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x1, 0x5) |
| --- |

## [◆ ](#a100647c82cfce4ed946cb9f18472af15)EUSART0\_CS\_PA0

| #define EUSART0\_CS\_PA0   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x0) |
| --- |

## [◆ ](#aad3c475c7949c55fc7ac69dcb9e9dfe3)EUSART0\_CS\_PA1

| #define EUSART0\_CS\_PA1   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x1) |
| --- |

## [◆ ](#a521ddcc2db980c3e31ddcb847980ca73)EUSART0\_CS\_PA2

| #define EUSART0\_CS\_PA2   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x2) |
| --- |

## [◆ ](#aff497e4a1f5d0f650a1a75d995740e5f)EUSART0\_CS\_PA3

| #define EUSART0\_CS\_PA3   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x3) |
| --- |

## [◆ ](#a852775bf4cc8faa4191b618c12690c07)EUSART0\_CS\_PA4

| #define EUSART0\_CS\_PA4   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x4) |
| --- |

## [◆ ](#a494590522337ea1dc294d8e30bdce4a0)EUSART0\_CS\_PA5

| #define EUSART0\_CS\_PA5   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x5) |
| --- |

## [◆ ](#a3324f29622d78fbdf0d6a3b7931fee92)EUSART0\_CS\_PA6

| #define EUSART0\_CS\_PA6   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x6) |
| --- |

## [◆ ](#a0aff0e33c99569acdff8882c376ab733)EUSART0\_CS\_PA7

| #define EUSART0\_CS\_PA7   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x7) |
| --- |

## [◆ ](#aecff621fa71796d796b02908db5f0305)EUSART0\_CS\_PA8

| #define EUSART0\_CS\_PA8   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x8) |
| --- |

## [◆ ](#a996818e2a513b1dde0b29cbafe3e5fb0)EUSART0\_CS\_PA9

| #define EUSART0\_CS\_PA9   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x9) |
| --- |

## [◆ ](#a7ace842a3a572ea81be1245e0ed3da90)EUSART0\_CS\_PB0

| #define EUSART0\_CS\_PB0   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x1, 0x0) |
| --- |

## [◆ ](#ad6557ba2b6c3d89732c097dc0c1df74b)EUSART0\_CS\_PB1

| #define EUSART0\_CS\_PB1   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x1, 0x1) |
| --- |

## [◆ ](#ad601437b58f8f23ad6ad052ea9176547)EUSART0\_CS\_PB2

| #define EUSART0\_CS\_PB2   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x1, 0x2) |
| --- |

## [◆ ](#a15627a1b7477e5079ebcdbf77e08283c)EUSART0\_CS\_PB3

| #define EUSART0\_CS\_PB3   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x1, 0x3) |
| --- |

## [◆ ](#a94f843865ca0025d3436c71e86ef9c34)EUSART0\_CS\_PB4

| #define EUSART0\_CS\_PB4   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x1, 0x4) |
| --- |

## [◆ ](#aa033023f7156fd751ed72b695d5f0467)EUSART0\_CS\_PB5

| #define EUSART0\_CS\_PB5   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x1, 0x5) |
| --- |

## [◆ ](#aa78640d4f3389404bbe47f35bbb1c02a)EUSART0\_CTS\_PA0

| #define EUSART0\_CTS\_PA0   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x0) |
| --- |

## [◆ ](#a43cbc88ff21700a62c42b35e8f67c0b1)EUSART0\_CTS\_PA1

| #define EUSART0\_CTS\_PA1   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x1) |
| --- |

## [◆ ](#a9e7c4aa3a487cbfa8019667b06e01ed9)EUSART0\_CTS\_PA2

| #define EUSART0\_CTS\_PA2   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x2) |
| --- |

## [◆ ](#a200ad378e054581fc0af32901db945d9)EUSART0\_CTS\_PA3

| #define EUSART0\_CTS\_PA3   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x3) |
| --- |

## [◆ ](#aba12ae15b468c70e21089ddbb4228bb2)EUSART0\_CTS\_PA4

| #define EUSART0\_CTS\_PA4   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x4) |
| --- |

## [◆ ](#a3eefe0f1fcafd901fc9ab7d90d57f5ce)EUSART0\_CTS\_PA5

| #define EUSART0\_CTS\_PA5   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x5) |
| --- |

## [◆ ](#a1f097826e960d3358db147f4a324ee49)EUSART0\_CTS\_PA6

| #define EUSART0\_CTS\_PA6   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x6) |
| --- |

## [◆ ](#a9d74f4aa54f500f1ff4839eaf1f29b3f)EUSART0\_CTS\_PA7

| #define EUSART0\_CTS\_PA7   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x7) |
| --- |

## [◆ ](#af31e2b373140e3eb7f01b90067847104)EUSART0\_CTS\_PA8

| #define EUSART0\_CTS\_PA8   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x8) |
| --- |

## [◆ ](#abfa5ad8998c88fa5304388413ad3fb62)EUSART0\_CTS\_PA9

| #define EUSART0\_CTS\_PA9   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x9) |
| --- |

## [◆ ](#ae41b867ca4046c838fa20049b685de44)EUSART0\_CTS\_PB0

| #define EUSART0\_CTS\_PB0   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x1, 0x0) |
| --- |

## [◆ ](#a06e7277edcf4f30266d9dc9b9bcddb9d)EUSART0\_CTS\_PB1

| #define EUSART0\_CTS\_PB1   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x1, 0x1) |
| --- |

## [◆ ](#a7908f6ee431528d7c4d4345b78c0c0c1)EUSART0\_CTS\_PB2

| #define EUSART0\_CTS\_PB2   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x1, 0x2) |
| --- |

## [◆ ](#a453f6ccc79c1145a755f667f0d716364)EUSART0\_CTS\_PB3

| #define EUSART0\_CTS\_PB3   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x1, 0x3) |
| --- |

## [◆ ](#a292c1725298cb2fe05ccf9c610c9a971)EUSART0\_CTS\_PB4

| #define EUSART0\_CTS\_PB4   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x1, 0x4) |
| --- |

## [◆ ](#a9f99e0775d7c0b53a7c06307efe5f548)EUSART0\_CTS\_PB5

| #define EUSART0\_CTS\_PB5   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x1, 0x5) |
| --- |

## [◆ ](#a4e8066ef85c98c6311cdff1ea85c0b0e)EUSART0\_RTS\_PA0

| #define EUSART0\_RTS\_PA0   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x0) |
| --- |

## [◆ ](#a8fb4dee00cdbb65ef6b771e1f6923333)EUSART0\_RTS\_PA1

| #define EUSART0\_RTS\_PA1   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x1) |
| --- |

## [◆ ](#af65566f1bbb87d7a789a558b7ba99905)EUSART0\_RTS\_PA2

| #define EUSART0\_RTS\_PA2   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x2) |
| --- |

## [◆ ](#a0cfcb844b17fb5054cdb97bd380d75c8)EUSART0\_RTS\_PA3

| #define EUSART0\_RTS\_PA3   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x3) |
| --- |

## [◆ ](#a1a144a6bd83a1872b99f6efadc3b9521)EUSART0\_RTS\_PA4

| #define EUSART0\_RTS\_PA4   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x4) |
| --- |

## [◆ ](#a870cd278a7c1a757f2189d07171b9f99)EUSART0\_RTS\_PA5

| #define EUSART0\_RTS\_PA5   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x5) |
| --- |

## [◆ ](#a579aa029440d7705d0648a7b0bacfcb3)EUSART0\_RTS\_PA6

| #define EUSART0\_RTS\_PA6   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x6) |
| --- |

## [◆ ](#adced5ad51aca90ec512b6206a83ad2cc)EUSART0\_RTS\_PA7

| #define EUSART0\_RTS\_PA7   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x7) |
| --- |

## [◆ ](#acd2ec0a2bbec98d10b7e30f0e576763c)EUSART0\_RTS\_PA8

| #define EUSART0\_RTS\_PA8   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x8) |
| --- |

## [◆ ](#a7fab8db0707d81e3456333c5474eb44b)EUSART0\_RTS\_PA9

| #define EUSART0\_RTS\_PA9   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x9) |
| --- |

## [◆ ](#a4ceaf57a7bf9921f8095d32de5f0ab66)EUSART0\_RTS\_PB0

| #define EUSART0\_RTS\_PB0   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x1, 0x0) |
| --- |

## [◆ ](#a2249a367a7276af293997584be24dad2)EUSART0\_RTS\_PB1

| #define EUSART0\_RTS\_PB1   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x1, 0x1) |
| --- |

## [◆ ](#adf3dac7572179dcc0766f81f7bd648cf)EUSART0\_RTS\_PB2

| #define EUSART0\_RTS\_PB2   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x1, 0x2) |
| --- |

## [◆ ](#a04c83284f28797c089ca46d4a432e905)EUSART0\_RTS\_PB3

| #define EUSART0\_RTS\_PB3   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x1, 0x3) |
| --- |

## [◆ ](#a953d9ef327a7b0eb5dedd69eba7b0b9a)EUSART0\_RTS\_PB4

| #define EUSART0\_RTS\_PB4   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x1, 0x4) |
| --- |

## [◆ ](#a23a1eab8002288306e26a2925365df1b)EUSART0\_RTS\_PB5

| #define EUSART0\_RTS\_PB5   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x1, 0x5) |
| --- |

## [◆ ](#a2b46bf2b099bf87941bbd4c29b77fee8)EUSART0\_RX\_PA0

| #define EUSART0\_RX\_PA0   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x0) |
| --- |

## [◆ ](#a22bfbf4a894d55b3c59983a0a60fdb00)EUSART0\_RX\_PA1

| #define EUSART0\_RX\_PA1   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x1) |
| --- |

## [◆ ](#a529e5bbdda4e497f5a71a78dd2628c91)EUSART0\_RX\_PA2

| #define EUSART0\_RX\_PA2   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x2) |
| --- |

## [◆ ](#a7ffae82c7d17cebc1d662a65b6d44a59)EUSART0\_RX\_PA3

| #define EUSART0\_RX\_PA3   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x3) |
| --- |

## [◆ ](#afab762ebf79c6816237382f135e88820)EUSART0\_RX\_PA4

| #define EUSART0\_RX\_PA4   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x4) |
| --- |

## [◆ ](#a346155c0747c9bbbdf254bbea5c37408)EUSART0\_RX\_PA5

| #define EUSART0\_RX\_PA5   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x5) |
| --- |

## [◆ ](#a90cca23bf07a59ad80d47e3c52683224)EUSART0\_RX\_PA6

| #define EUSART0\_RX\_PA6   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x6) |
| --- |

## [◆ ](#a5ef7abc333b9450ec72e144384a2369d)EUSART0\_RX\_PA7

| #define EUSART0\_RX\_PA7   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x7) |
| --- |

## [◆ ](#a05989116473a2986fd70707a2a41c869)EUSART0\_RX\_PA8

| #define EUSART0\_RX\_PA8   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x8) |
| --- |

## [◆ ](#a06945aeff3f352e71804082c6afd234e)EUSART0\_RX\_PA9

| #define EUSART0\_RX\_PA9   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x9) |
| --- |

## [◆ ](#a1a59a7ed291e816ece0bc12cffd98f39)EUSART0\_RX\_PB0

| #define EUSART0\_RX\_PB0   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x1, 0x0) |
| --- |

## [◆ ](#a1bb9368d71f3b8140274beed383a465f)EUSART0\_RX\_PB1

| #define EUSART0\_RX\_PB1   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x1, 0x1) |
| --- |

## [◆ ](#ac684b9dbb5433cf963027fd3ab0cd1fb)EUSART0\_RX\_PB2

| #define EUSART0\_RX\_PB2   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x1, 0x2) |
| --- |

## [◆ ](#afb6d2142c3766fdede31602e56e1281a)EUSART0\_RX\_PB3

| #define EUSART0\_RX\_PB3   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x1, 0x3) |
| --- |

## [◆ ](#aa4cb55bd34f6f1ae67e46e0bbbfed055)EUSART0\_RX\_PB4

| #define EUSART0\_RX\_PB4   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x1, 0x4) |
| --- |

## [◆ ](#a9b922bbda2db8c0f13455c2a8916cc3b)EUSART0\_RX\_PB5

| #define EUSART0\_RX\_PB5   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x1, 0x5) |
| --- |

## [◆ ](#a0a19d2153b70b8ef0e074fb8daadba20)EUSART0\_SCLK\_PA0

| #define EUSART0\_SCLK\_PA0   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x0) |
| --- |

## [◆ ](#aca8e4898f56d57aff5909b5e8f56eee0)EUSART0\_SCLK\_PA1

| #define EUSART0\_SCLK\_PA1   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x1) |
| --- |

## [◆ ](#abbc7ccc93b8fe675a34aea51b63f52ef)EUSART0\_SCLK\_PA2

| #define EUSART0\_SCLK\_PA2   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x2) |
| --- |

## [◆ ](#a08190aaeb8a375f69bc3af20b6cea6bf)EUSART0\_SCLK\_PA3

| #define EUSART0\_SCLK\_PA3   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x3) |
| --- |

## [◆ ](#a4e49a5735fc4f636e31c770b01960242)EUSART0\_SCLK\_PA4

| #define EUSART0\_SCLK\_PA4   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x4) |
| --- |

## [◆ ](#a5bb9d1463e97d8683ff98741b989f82c)EUSART0\_SCLK\_PA5

| #define EUSART0\_SCLK\_PA5   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x5) |
| --- |

## [◆ ](#a2465c3c97ea670afb2f6e579ba7e2db3)EUSART0\_SCLK\_PA6

| #define EUSART0\_SCLK\_PA6   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x6) |
| --- |

## [◆ ](#a038e6fb8ad493dee10235499595210d8)EUSART0\_SCLK\_PA7

| #define EUSART0\_SCLK\_PA7   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x7) |
| --- |

## [◆ ](#aa5c4e4ec06af3d9212e1fc8200a28639)EUSART0\_SCLK\_PA8

| #define EUSART0\_SCLK\_PA8   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x8) |
| --- |

## [◆ ](#a237b1078b65f552cd9501ba9e97e72f6)EUSART0\_SCLK\_PA9

| #define EUSART0\_SCLK\_PA9   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x9) |
| --- |

## [◆ ](#ad1159b33436207a1b896cd71f51730dd)EUSART0\_SCLK\_PB0

| #define EUSART0\_SCLK\_PB0   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x1, 0x0) |
| --- |

## [◆ ](#a2253345ed59d0d340c7b077ae8d689b4)EUSART0\_SCLK\_PB1

| #define EUSART0\_SCLK\_PB1   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x1, 0x1) |
| --- |

## [◆ ](#a1dbc32ec456a7c882c71dddf254dec53)EUSART0\_SCLK\_PB2

| #define EUSART0\_SCLK\_PB2   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x1, 0x2) |
| --- |

## [◆ ](#a27cc8d09e0ca7ac92e6022ed35fc2549)EUSART0\_SCLK\_PB3

| #define EUSART0\_SCLK\_PB3   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x1, 0x3) |
| --- |

## [◆ ](#aeb794afde863684b4166b657b797f837)EUSART0\_SCLK\_PB4

| #define EUSART0\_SCLK\_PB4   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x1, 0x4) |
| --- |

## [◆ ](#a02bd951a8041d26a50ed6d3dac3a1435)EUSART0\_SCLK\_PB5

| #define EUSART0\_SCLK\_PB5   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x1, 0x5) |
| --- |

## [◆ ](#ad1d73b89a55be3c3b76309827c392e70)EUSART0\_TX\_PA0

| #define EUSART0\_TX\_PA0   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x0) |
| --- |

## [◆ ](#a01b89a42fcc33bd36f8c419017a473ec)EUSART0\_TX\_PA1

| #define EUSART0\_TX\_PA1   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x1) |
| --- |

## [◆ ](#a84c240d7825740c4b18aebe068e788d6)EUSART0\_TX\_PA2

| #define EUSART0\_TX\_PA2   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x2) |
| --- |

## [◆ ](#aafac5282dba172a3e073c31d29085d10)EUSART0\_TX\_PA3

| #define EUSART0\_TX\_PA3   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x3) |
| --- |

## [◆ ](#a7889459ce02255a24f9cc968c1bc0e1c)EUSART0\_TX\_PA4

| #define EUSART0\_TX\_PA4   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x4) |
| --- |

## [◆ ](#ab2845f805e7c75787b24d924dcccfe68)EUSART0\_TX\_PA5

| #define EUSART0\_TX\_PA5   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x5) |
| --- |

## [◆ ](#ab129226f0405530f5cd911cd423fc1b9)EUSART0\_TX\_PA6

| #define EUSART0\_TX\_PA6   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x6) |
| --- |

## [◆ ](#a26eba150ba1aaf50e9a6059588aeaf1a)EUSART0\_TX\_PA7

| #define EUSART0\_TX\_PA7   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x7) |
| --- |

## [◆ ](#a318a4670d6912095c2dba8c6dd8c9623)EUSART0\_TX\_PA8

| #define EUSART0\_TX\_PA8   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x8) |
| --- |

## [◆ ](#af3761eef1a29ecb641f39ff9244a4e13)EUSART0\_TX\_PA9

| #define EUSART0\_TX\_PA9   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x9) |
| --- |

## [◆ ](#a8d6a3ec6a9d1076b9174a66023685407)EUSART0\_TX\_PB0

| #define EUSART0\_TX\_PB0   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x1, 0x0) |
| --- |

## [◆ ](#a77c5c04618ba4ce29cb1ccdb0624bf36)EUSART0\_TX\_PB1

| #define EUSART0\_TX\_PB1   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x1, 0x1) |
| --- |

## [◆ ](#a8ec4a7e6c0d3eb4d66b25495c4e339f5)EUSART0\_TX\_PB2

| #define EUSART0\_TX\_PB2   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x1, 0x2) |
| --- |

## [◆ ](#a3c0337cddda08df662dae06438bb0330)EUSART0\_TX\_PB3

| #define EUSART0\_TX\_PB3   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x1, 0x3) |
| --- |

## [◆ ](#aede0d7fee53f6b2f345752bf9fdba30c)EUSART0\_TX\_PB4

| #define EUSART0\_TX\_PB4   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x1, 0x4) |
| --- |

## [◆ ](#a2cbf95c30f80d05041caabc3cc03e4b4)EUSART0\_TX\_PB5

| #define EUSART0\_TX\_PB5   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x1, 0x5) |
| --- |

## [◆ ](#a40f82c8c64899e7d6814527efbbebe93)EUSART1\_CS\_PA0

| #define EUSART1\_CS\_PA0   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x0) |
| --- |

## [◆ ](#af63951a9525443f244715b5a955c6653)EUSART1\_CS\_PA1

| #define EUSART1\_CS\_PA1   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x1) |
| --- |

## [◆ ](#a888362b3adc4669f5a60462d0ae73334)EUSART1\_CS\_PA2

| #define EUSART1\_CS\_PA2   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x2) |
| --- |

## [◆ ](#accc804e7c4664309a021a7a8c591af6c)EUSART1\_CS\_PA3

| #define EUSART1\_CS\_PA3   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x3) |
| --- |

## [◆ ](#a770e6e5582d1e29c8b23a90628b3e57c)EUSART1\_CS\_PA4

| #define EUSART1\_CS\_PA4   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x4) |
| --- |

## [◆ ](#ae3ef936bb7be77cfdce700627f231ec7)EUSART1\_CS\_PA5

| #define EUSART1\_CS\_PA5   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x5) |
| --- |

## [◆ ](#a4a45381fe7d897de6e53043fb47ef13e)EUSART1\_CS\_PA6

| #define EUSART1\_CS\_PA6   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x6) |
| --- |

## [◆ ](#a637c7be3f82194e942972cde56bbb686)EUSART1\_CS\_PA7

| #define EUSART1\_CS\_PA7   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x7) |
| --- |

## [◆ ](#a3f561023c637eba25ac1d46c36e20a80)EUSART1\_CS\_PA8

| #define EUSART1\_CS\_PA8   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x8) |
| --- |

## [◆ ](#a08375c829f9d68aeff931ec481429fb3)EUSART1\_CS\_PA9

| #define EUSART1\_CS\_PA9   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x9) |
| --- |

## [◆ ](#acdbe2339b99a4fe502bba246a626d5c2)EUSART1\_CS\_PB0

| #define EUSART1\_CS\_PB0   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x1, 0x0) |
| --- |

## [◆ ](#a7f14f23f53baa612f22609dea451f445)EUSART1\_CS\_PB1

| #define EUSART1\_CS\_PB1   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x1, 0x1) |
| --- |

## [◆ ](#a619bea931dfb9441abd013c5f3f70be7)EUSART1\_CS\_PB2

| #define EUSART1\_CS\_PB2   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x1, 0x2) |
| --- |

## [◆ ](#a620516494e3be49f80bb70a9c0da28ac)EUSART1\_CS\_PB3

| #define EUSART1\_CS\_PB3   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x1, 0x3) |
| --- |

## [◆ ](#afd07cc566c75f403760a1754ec784e92)EUSART1\_CS\_PB4

| #define EUSART1\_CS\_PB4   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x1, 0x4) |
| --- |

## [◆ ](#a2a06250d6353f8e710e429414896e828)EUSART1\_CS\_PB5

| #define EUSART1\_CS\_PB5   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x1, 0x5) |
| --- |

## [◆ ](#a015e088a759762fcf0c47c9b4033b66c)EUSART1\_CS\_PC0

| #define EUSART1\_CS\_PC0   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x0) |
| --- |

## [◆ ](#a176087a622c1e9f7bf968bd59381691b)EUSART1\_CS\_PC1

| #define EUSART1\_CS\_PC1   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x1) |
| --- |

## [◆ ](#a6c4faf990cacd9a0d8e17c2aa23ed236)EUSART1\_CS\_PC2

| #define EUSART1\_CS\_PC2   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x2) |
| --- |

## [◆ ](#a63386d40b9a59051bb744d043b2cce5c)EUSART1\_CS\_PC3

| #define EUSART1\_CS\_PC3   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x3) |
| --- |

## [◆ ](#aa8a89563cdaff202bd581204799e6454)EUSART1\_CS\_PC4

| #define EUSART1\_CS\_PC4   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x4) |
| --- |

## [◆ ](#a101b25d7d37e7b9fca411811df2662a9)EUSART1\_CS\_PC5

| #define EUSART1\_CS\_PC5   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x5) |
| --- |

## [◆ ](#a55c0377bef97b860796d28a5257b04e6)EUSART1\_CS\_PC6

| #define EUSART1\_CS\_PC6   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x6) |
| --- |

## [◆ ](#a847321a3e9924fb48574629393a9e777)EUSART1\_CS\_PC7

| #define EUSART1\_CS\_PC7   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x7) |
| --- |

## [◆ ](#ad6bae311c5b34b86f4a5f33a2f97fae8)EUSART1\_CS\_PC8

| #define EUSART1\_CS\_PC8   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x8) |
| --- |

## [◆ ](#a9d063c8af1204995448f3fa1d51d1fb4)EUSART1\_CS\_PC9

| #define EUSART1\_CS\_PC9   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x9) |
| --- |

## [◆ ](#abaf2f2d1169cde30d7cc29eb843f5ed8)EUSART1\_CS\_PD0

| #define EUSART1\_CS\_PD0   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x3, 0x0) |
| --- |

## [◆ ](#aa4b4634c5f80cdd71c0b806ffc72df65)EUSART1\_CS\_PD1

| #define EUSART1\_CS\_PD1   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x3, 0x1) |
| --- |

## [◆ ](#af38ecf13151c02150a2313cd3b9ddf7f)EUSART1\_CS\_PD2

| #define EUSART1\_CS\_PD2   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x3, 0x2) |
| --- |

## [◆ ](#a8b9a6da38263a9cd3585a3bee8ae937d)EUSART1\_CS\_PD3

| #define EUSART1\_CS\_PD3   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x3, 0x3) |
| --- |

## [◆ ](#a4ee8e0542529402fc418e7096431e376)EUSART1\_CS\_PD4

| #define EUSART1\_CS\_PD4   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x3, 0x4) |
| --- |

## [◆ ](#a122e1f8045702616fe121e37f329e0f0)EUSART1\_CS\_PD5

| #define EUSART1\_CS\_PD5   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x3, 0x5) |
| --- |

## [◆ ](#a8d81221acf4017c05ca56c5a98d58552)EUSART1\_CTS\_PA0

| #define EUSART1\_CTS\_PA0   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x0) |
| --- |

## [◆ ](#a5d4da4feea93c4b06110ca1e3610659a)EUSART1\_CTS\_PA1

| #define EUSART1\_CTS\_PA1   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x1) |
| --- |

## [◆ ](#af8e1f1909c844d7c2f4b531c82f5c7cb)EUSART1\_CTS\_PA2

| #define EUSART1\_CTS\_PA2   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x2) |
| --- |

## [◆ ](#a69bd0b952644909144e49f6542d88c92)EUSART1\_CTS\_PA3

| #define EUSART1\_CTS\_PA3   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x3) |
| --- |

## [◆ ](#a36ce96157ce9be04de043bb2c04cef82)EUSART1\_CTS\_PA4

| #define EUSART1\_CTS\_PA4   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x4) |
| --- |

## [◆ ](#aa6351a3c82698810d1041413513553fc)EUSART1\_CTS\_PA5

| #define EUSART1\_CTS\_PA5   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x5) |
| --- |

## [◆ ](#a76dfe398fdb4ed75ae511b29a1d347b0)EUSART1\_CTS\_PA6

| #define EUSART1\_CTS\_PA6   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x6) |
| --- |

## [◆ ](#ab84cf2fc8ac1a7f5666769f283ec3e49)EUSART1\_CTS\_PA7

| #define EUSART1\_CTS\_PA7   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x7) |
| --- |

## [◆ ](#aeb09839ecbdd7f2c608e25602a302752)EUSART1\_CTS\_PA8

| #define EUSART1\_CTS\_PA8   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x8) |
| --- |

## [◆ ](#a46ecc03c0f9a382360aed7344ae35eb4)EUSART1\_CTS\_PA9

| #define EUSART1\_CTS\_PA9   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x9) |
| --- |

## [◆ ](#a883da4be324d198cbc34ea41676a9ddf)EUSART1\_CTS\_PB0

| #define EUSART1\_CTS\_PB0   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x1, 0x0) |
| --- |

## [◆ ](#acc196631f4adce64be8891275c851cc8)EUSART1\_CTS\_PB1

| #define EUSART1\_CTS\_PB1   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x1, 0x1) |
| --- |

## [◆ ](#ad56423043df1ba928037fb8ad7996a0a)EUSART1\_CTS\_PB2

| #define EUSART1\_CTS\_PB2   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x1, 0x2) |
| --- |

## [◆ ](#aaf246a8e049ac1b6f0ea6bff0f77d361)EUSART1\_CTS\_PB3

| #define EUSART1\_CTS\_PB3   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x1, 0x3) |
| --- |

## [◆ ](#a8d541570c6ca67dd288bf96afaa86d00)EUSART1\_CTS\_PB4

| #define EUSART1\_CTS\_PB4   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x1, 0x4) |
| --- |

## [◆ ](#a250c70e460b2087d794ea42380ce871e)EUSART1\_CTS\_PB5

| #define EUSART1\_CTS\_PB5   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x1, 0x5) |
| --- |

## [◆ ](#a71b2e656c782b69d56a103e73b464730)EUSART1\_CTS\_PC0

| #define EUSART1\_CTS\_PC0   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x0) |
| --- |

## [◆ ](#a3de408c7045ed45e7dc371443c370c23)EUSART1\_CTS\_PC1

| #define EUSART1\_CTS\_PC1   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x1) |
| --- |

## [◆ ](#a448af5a813508ad8dd8e5d6e5df4b43b)EUSART1\_CTS\_PC2

| #define EUSART1\_CTS\_PC2   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x2) |
| --- |

## [◆ ](#a5bca4e376d8315ef91f8574ced26eb16)EUSART1\_CTS\_PC3

| #define EUSART1\_CTS\_PC3   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x3) |
| --- |

## [◆ ](#aa72d1c30858bde17689ed0dfc57069bb)EUSART1\_CTS\_PC4

| #define EUSART1\_CTS\_PC4   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x4) |
| --- |

## [◆ ](#a70ecbc7c78a15bcdc81b997d720b0b0c)EUSART1\_CTS\_PC5

| #define EUSART1\_CTS\_PC5   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x5) |
| --- |

## [◆ ](#aa6fc0b0cd1690dd9d8e898b4177deb1f)EUSART1\_CTS\_PC6

| #define EUSART1\_CTS\_PC6   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x6) |
| --- |

## [◆ ](#a9f21efe766114885dc079c88593fc66a)EUSART1\_CTS\_PC7

| #define EUSART1\_CTS\_PC7   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x7) |
| --- |

## [◆ ](#a611caa47f0896dc5f8bd552e27b7e887)EUSART1\_CTS\_PC8

| #define EUSART1\_CTS\_PC8   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x8) |
| --- |

## [◆ ](#ad6bea69f152a00c80b5a6170f714b802)EUSART1\_CTS\_PC9

| #define EUSART1\_CTS\_PC9   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x9) |
| --- |

## [◆ ](#ae2238ef628fa06b7eb97f58b86bf011b)EUSART1\_CTS\_PD0

| #define EUSART1\_CTS\_PD0   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x3, 0x0) |
| --- |

## [◆ ](#ae15d8faf92ba3b2b4c07eddf5d6fd274)EUSART1\_CTS\_PD1

| #define EUSART1\_CTS\_PD1   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x3, 0x1) |
| --- |

## [◆ ](#aef76a9fbbcbd9a4e8d254773bba07126)EUSART1\_CTS\_PD2

| #define EUSART1\_CTS\_PD2   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x3, 0x2) |
| --- |

## [◆ ](#aa32ab3b05dc99adbfb5b3a84642b6403)EUSART1\_CTS\_PD3

| #define EUSART1\_CTS\_PD3   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x3, 0x3) |
| --- |

## [◆ ](#af0c7e457f0de9267f6bf4c2e1a5e0f3f)EUSART1\_CTS\_PD4

| #define EUSART1\_CTS\_PD4   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x3, 0x4) |
| --- |

## [◆ ](#ab4fe681884230878b055e04a23eb9ec3)EUSART1\_CTS\_PD5

| #define EUSART1\_CTS\_PD5   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x3, 0x5) |
| --- |

## [◆ ](#abc1f657ca7df682bd31439ae830e1c6b)EUSART1\_RTS\_PA0

| #define EUSART1\_RTS\_PA0   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x0) |
| --- |

## [◆ ](#ae0269aec4dd2413b32ed157eeec8e810)EUSART1\_RTS\_PA1

| #define EUSART1\_RTS\_PA1   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x1) |
| --- |

## [◆ ](#a562cacf73b6eca2f6feffb7e494ec806)EUSART1\_RTS\_PA2

| #define EUSART1\_RTS\_PA2   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x2) |
| --- |

## [◆ ](#ac832d962a34bd67b3d6874629191f3d8)EUSART1\_RTS\_PA3

| #define EUSART1\_RTS\_PA3   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x3) |
| --- |

## [◆ ](#a59c071c3b6b1940bfc67b537be8f9d03)EUSART1\_RTS\_PA4

| #define EUSART1\_RTS\_PA4   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x4) |
| --- |

## [◆ ](#a60a05e2ee467a334f4acba3032724efd)EUSART1\_RTS\_PA5

| #define EUSART1\_RTS\_PA5   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x5) |
| --- |

## [◆ ](#a9070e646c606ad24ea2a49024e93d2ec)EUSART1\_RTS\_PA6

| #define EUSART1\_RTS\_PA6   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x6) |
| --- |

## [◆ ](#ab692bb94e9ffe0930767caeae52a1bc9)EUSART1\_RTS\_PA7

| #define EUSART1\_RTS\_PA7   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x7) |
| --- |

## [◆ ](#a4eac1cef4c4df24f56c4422ff00e540b)EUSART1\_RTS\_PA8

| #define EUSART1\_RTS\_PA8   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x8) |
| --- |

## [◆ ](#ab3785305b7008e1abbaf35451cd764d8)EUSART1\_RTS\_PA9

| #define EUSART1\_RTS\_PA9   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x9) |
| --- |

## [◆ ](#a7b73f6a89a0a8707e7d3caf7c9e1bfcf)EUSART1\_RTS\_PB0

| #define EUSART1\_RTS\_PB0   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x1, 0x0) |
| --- |

## [◆ ](#a3ee5218e6cd62cf429ed39483dad68b0)EUSART1\_RTS\_PB1

| #define EUSART1\_RTS\_PB1   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x1, 0x1) |
| --- |

## [◆ ](#ad6a72d46a8632364b669d57f425c97b7)EUSART1\_RTS\_PB2

| #define EUSART1\_RTS\_PB2   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x1, 0x2) |
| --- |

## [◆ ](#ad964d10c49afb6b27ccff6537e1f92e8)EUSART1\_RTS\_PB3

| #define EUSART1\_RTS\_PB3   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x1, 0x3) |
| --- |

## [◆ ](#af1faa3155f2eb599cb02114bf58484b0)EUSART1\_RTS\_PB4

| #define EUSART1\_RTS\_PB4   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x1, 0x4) |
| --- |

## [◆ ](#a24d3939624d3bcdd1ea8ccd4c652581c)EUSART1\_RTS\_PB5

| #define EUSART1\_RTS\_PB5   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x1, 0x5) |
| --- |

## [◆ ](#acc9df99d6f67349407eab1963962329a)EUSART1\_RTS\_PC0

| #define EUSART1\_RTS\_PC0   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x0) |
| --- |

## [◆ ](#aa65ef7ad286ee25997d57b0c94cdcecb)EUSART1\_RTS\_PC1

| #define EUSART1\_RTS\_PC1   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x1) |
| --- |

## [◆ ](#a45dd8df05c9c5cfc7aa94ed8591eabe8)EUSART1\_RTS\_PC2

| #define EUSART1\_RTS\_PC2   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x2) |
| --- |

## [◆ ](#a38af1c47914e8c7a0823ceb0ccb25e6e)EUSART1\_RTS\_PC3

| #define EUSART1\_RTS\_PC3   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x3) |
| --- |

## [◆ ](#a6bc896f9f3261271d490611c1379db44)EUSART1\_RTS\_PC4

| #define EUSART1\_RTS\_PC4   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x4) |
| --- |

## [◆ ](#a7a5842461fe1b84f540380ec07e1822d)EUSART1\_RTS\_PC5

| #define EUSART1\_RTS\_PC5   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x5) |
| --- |

## [◆ ](#a5371f435ba7b54049797c8e4d57c263d)EUSART1\_RTS\_PC6

| #define EUSART1\_RTS\_PC6   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x6) |
| --- |

## [◆ ](#a8ed175732bc35f35c6e7487be8b903d2)EUSART1\_RTS\_PC7

| #define EUSART1\_RTS\_PC7   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x7) |
| --- |

## [◆ ](#ad54ae2dd1d6dcd8caaee35411927f88e)EUSART1\_RTS\_PC8

| #define EUSART1\_RTS\_PC8   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x8) |
| --- |

## [◆ ](#a51dd015eade83c61357a4599bbf60a10)EUSART1\_RTS\_PC9

| #define EUSART1\_RTS\_PC9   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x9) |
| --- |

## [◆ ](#a28ef23be5d09659645516e832ed6f65f)EUSART1\_RTS\_PD0

| #define EUSART1\_RTS\_PD0   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x3, 0x0) |
| --- |

## [◆ ](#a94be5cf6daa2de7b415b78c5b0e1547f)EUSART1\_RTS\_PD1

| #define EUSART1\_RTS\_PD1   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x3, 0x1) |
| --- |

## [◆ ](#aa8dac982c8de064268697d4bb9460973)EUSART1\_RTS\_PD2

| #define EUSART1\_RTS\_PD2   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x3, 0x2) |
| --- |

## [◆ ](#acb2eb162bdf3ccfdd69e17eb047a2188)EUSART1\_RTS\_PD3

| #define EUSART1\_RTS\_PD3   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x3, 0x3) |
| --- |

## [◆ ](#a8f6e57cd14447b3a19e5221a773c1af6)EUSART1\_RTS\_PD4

| #define EUSART1\_RTS\_PD4   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x3, 0x4) |
| --- |

## [◆ ](#a3cd4f764e0e73ac98673cb79e6b03f6f)EUSART1\_RTS\_PD5

| #define EUSART1\_RTS\_PD5   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x3, 0x5) |
| --- |

## [◆ ](#a2c1a7ed0cc467841cebcf24d44d2f258)EUSART1\_RX\_PA0

| #define EUSART1\_RX\_PA0   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x0) |
| --- |

## [◆ ](#a7e33ba392cb53d219f1eda52d67a6944)EUSART1\_RX\_PA1

| #define EUSART1\_RX\_PA1   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x1) |
| --- |

## [◆ ](#a3c0f7f785f61504faf51fd3155ff02d6)EUSART1\_RX\_PA2

| #define EUSART1\_RX\_PA2   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x2) |
| --- |

## [◆ ](#ad40833154f299658986ad7ad63ec1b96)EUSART1\_RX\_PA3

| #define EUSART1\_RX\_PA3   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x3) |
| --- |

## [◆ ](#a6c41b67649a5c2d1e861fe316e0ef533)EUSART1\_RX\_PA4

| #define EUSART1\_RX\_PA4   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x4) |
| --- |

## [◆ ](#af0868cbd1c8abf3e71227bfb70f46f22)EUSART1\_RX\_PA5

| #define EUSART1\_RX\_PA5   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x5) |
| --- |

## [◆ ](#a8245e0aca9ea584f0490aee19687c067)EUSART1\_RX\_PA6

| #define EUSART1\_RX\_PA6   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x6) |
| --- |

## [◆ ](#a7b51646c08b9fc0ba688c99c623b5d18)EUSART1\_RX\_PA7

| #define EUSART1\_RX\_PA7   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x7) |
| --- |

## [◆ ](#af00e3232320d0c3fd07e60c9aa13f55e)EUSART1\_RX\_PA8

| #define EUSART1\_RX\_PA8   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x8) |
| --- |

## [◆ ](#a00c0fc9b40bd7d8865a9d8da174cc38b)EUSART1\_RX\_PA9

| #define EUSART1\_RX\_PA9   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x9) |
| --- |

## [◆ ](#a6b070084786fd60d676b2c2f75c1f98e)EUSART1\_RX\_PB0

| #define EUSART1\_RX\_PB0   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x1, 0x0) |
| --- |

## [◆ ](#a77554a2b4ae43d009a9e15fd3f4028e3)EUSART1\_RX\_PB1

| #define EUSART1\_RX\_PB1   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x1, 0x1) |
| --- |

## [◆ ](#ac2fa1d52ab0de981d47e9b65ab9665cb)EUSART1\_RX\_PB2

| #define EUSART1\_RX\_PB2   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x1, 0x2) |
| --- |

## [◆ ](#ae0ee1a1afcf0079d4a9283bdd3e60588)EUSART1\_RX\_PB3

| #define EUSART1\_RX\_PB3   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x1, 0x3) |
| --- |

## [◆ ](#aaec2f1281d66ce906061624d4917baa6)EUSART1\_RX\_PB4

| #define EUSART1\_RX\_PB4   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x1, 0x4) |
| --- |

## [◆ ](#a1e542f9e26793dff053ab53cb32b08f1)EUSART1\_RX\_PB5

| #define EUSART1\_RX\_PB5   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x1, 0x5) |
| --- |

## [◆ ](#aa98270d29aa5350d603b6801b81e061e)EUSART1\_RX\_PC0

| #define EUSART1\_RX\_PC0   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x0) |
| --- |

## [◆ ](#a03ee872913b0d67c65f8dc385fb4e91a)EUSART1\_RX\_PC1

| #define EUSART1\_RX\_PC1   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x1) |
| --- |

## [◆ ](#ac4aadea1a819cf4e285f89d27718552f)EUSART1\_RX\_PC2

| #define EUSART1\_RX\_PC2   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x2) |
| --- |

## [◆ ](#a83b13f35d15a557bf9a53bb4a439805f)EUSART1\_RX\_PC3

| #define EUSART1\_RX\_PC3   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x3) |
| --- |

## [◆ ](#a70d814531178d1d9b15c789076835b1e)EUSART1\_RX\_PC4

| #define EUSART1\_RX\_PC4   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x4) |
| --- |

## [◆ ](#a458e9dbc13a3dab016b5507d65ab6292)EUSART1\_RX\_PC5

| #define EUSART1\_RX\_PC5   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x5) |
| --- |

## [◆ ](#a5b74541abae3c7c46603704b893c8f77)EUSART1\_RX\_PC6

| #define EUSART1\_RX\_PC6   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x6) |
| --- |

## [◆ ](#a64abe91c5e0ee069f4e7cd9f1988408a)EUSART1\_RX\_PC7

| #define EUSART1\_RX\_PC7   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x7) |
| --- |

## [◆ ](#aaedbd57fd7ea06c37bc76fead37a8cca)EUSART1\_RX\_PC8

| #define EUSART1\_RX\_PC8   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x8) |
| --- |

## [◆ ](#a1c742aedd3c09961965f08a26a899339)EUSART1\_RX\_PC9

| #define EUSART1\_RX\_PC9   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x9) |
| --- |

## [◆ ](#a98f3d4c0fd1c382b3e74de148239493b)EUSART1\_RX\_PD0

| #define EUSART1\_RX\_PD0   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x3, 0x0) |
| --- |

## [◆ ](#a2bcf22654333629b1512b192fafaabf8)EUSART1\_RX\_PD1

| #define EUSART1\_RX\_PD1   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x3, 0x1) |
| --- |

## [◆ ](#a23ec89755383423270053f9d62cb3052)EUSART1\_RX\_PD2

| #define EUSART1\_RX\_PD2   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x3, 0x2) |
| --- |

## [◆ ](#a3b66d7466704954a9c4f7d114cc3948b)EUSART1\_RX\_PD3

| #define EUSART1\_RX\_PD3   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x3, 0x3) |
| --- |

## [◆ ](#a642ec25a709db3727086999a94e10518)EUSART1\_RX\_PD4

| #define EUSART1\_RX\_PD4   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x3, 0x4) |
| --- |

## [◆ ](#a99b0e129557e42a51fafdad86034c5d3)EUSART1\_RX\_PD5

| #define EUSART1\_RX\_PD5   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x3, 0x5) |
| --- |

## [◆ ](#a1866dd8e210ba1ab2877a58fed00c93e)EUSART1\_SCLK\_PA0

| #define EUSART1\_SCLK\_PA0   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x0) |
| --- |

## [◆ ](#a48c98c4dadaf125f1a227ef37bbf9738)EUSART1\_SCLK\_PA1

| #define EUSART1\_SCLK\_PA1   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x1) |
| --- |

## [◆ ](#a1f529ea54ec4efcdc13c99ccf42b3db9)EUSART1\_SCLK\_PA2

| #define EUSART1\_SCLK\_PA2   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x2) |
| --- |

## [◆ ](#a576b277096ee6c9b14a99627e77720d3)EUSART1\_SCLK\_PA3

| #define EUSART1\_SCLK\_PA3   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x3) |
| --- |

## [◆ ](#ac13a88d3cd2571fdc2a57284e6d62c09)EUSART1\_SCLK\_PA4

| #define EUSART1\_SCLK\_PA4   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x4) |
| --- |

## [◆ ](#adbce8bccdef55112969e797c7b6639dd)EUSART1\_SCLK\_PA5

| #define EUSART1\_SCLK\_PA5   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x5) |
| --- |

## [◆ ](#a7c77e84e1434e302f03737b24d1ff079)EUSART1\_SCLK\_PA6

| #define EUSART1\_SCLK\_PA6   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x6) |
| --- |

## [◆ ](#aaf42811c16b367f1abf8e6bc160a8c20)EUSART1\_SCLK\_PA7

| #define EUSART1\_SCLK\_PA7   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x7) |
| --- |

## [◆ ](#aebab59d6a37e8c841da4f390387897ab)EUSART1\_SCLK\_PA8

| #define EUSART1\_SCLK\_PA8   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x8) |
| --- |

## [◆ ](#a00c2d9101c157ff6a294b0b79f295365)EUSART1\_SCLK\_PA9

| #define EUSART1\_SCLK\_PA9   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x9) |
| --- |

## [◆ ](#a203c4398d642eada6bda1cc7bf80bfbe)EUSART1\_SCLK\_PB0

| #define EUSART1\_SCLK\_PB0   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x1, 0x0) |
| --- |

## [◆ ](#abd4a43cfc4b84a8b2e1c4097771d7a59)EUSART1\_SCLK\_PB1

| #define EUSART1\_SCLK\_PB1   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x1, 0x1) |
| --- |

## [◆ ](#abe989ab643fbe91732fc5d85c4b8c560)EUSART1\_SCLK\_PB2

| #define EUSART1\_SCLK\_PB2   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x1, 0x2) |
| --- |

## [◆ ](#afb4913ed4eb217a972c17821c2eafc27)EUSART1\_SCLK\_PB3

| #define EUSART1\_SCLK\_PB3   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x1, 0x3) |
| --- |

## [◆ ](#a640a1a6ece43715d2122cb4ced70543a)EUSART1\_SCLK\_PB4

| #define EUSART1\_SCLK\_PB4   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x1, 0x4) |
| --- |

## [◆ ](#ab6152389b3d34387306a4cd554b4d573)EUSART1\_SCLK\_PB5

| #define EUSART1\_SCLK\_PB5   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x1, 0x5) |
| --- |

## [◆ ](#a7d65400748ea9527510a0e34f410b8c3)EUSART1\_SCLK\_PC0

| #define EUSART1\_SCLK\_PC0   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x0) |
| --- |

## [◆ ](#a7ea3f4ca3c6e8f920c68e7a9bd4f58cb)EUSART1\_SCLK\_PC1

| #define EUSART1\_SCLK\_PC1   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x1) |
| --- |

## [◆ ](#ad2998e2a2182b75f088ca5bcbc95753a)EUSART1\_SCLK\_PC2

| #define EUSART1\_SCLK\_PC2   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x2) |
| --- |

## [◆ ](#ab26cf07e0496f46713893e36521d8cc1)EUSART1\_SCLK\_PC3

| #define EUSART1\_SCLK\_PC3   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x3) |
| --- |

## [◆ ](#acc5b977ae91e36cb79a4274f06d185f3)EUSART1\_SCLK\_PC4

| #define EUSART1\_SCLK\_PC4   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x4) |
| --- |

## [◆ ](#aee5ca21dcd28e168927431e40848d6f5)EUSART1\_SCLK\_PC5

| #define EUSART1\_SCLK\_PC5   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x5) |
| --- |

## [◆ ](#aaf2c62839097ad29f904dd4022f0b27c)EUSART1\_SCLK\_PC6

| #define EUSART1\_SCLK\_PC6   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x6) |
| --- |

## [◆ ](#a78cf96f19e780387646d3e3cdf32deef)EUSART1\_SCLK\_PC7

| #define EUSART1\_SCLK\_PC7   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x7) |
| --- |

## [◆ ](#a6779aeaccb85a2c1fd6f14ad649c4441)EUSART1\_SCLK\_PC8

| #define EUSART1\_SCLK\_PC8   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x8) |
| --- |

## [◆ ](#af6eb3759c39650e9ce7c74c302c8c118)EUSART1\_SCLK\_PC9

| #define EUSART1\_SCLK\_PC9   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x9) |
| --- |

## [◆ ](#a9b74e299bdafb94c3f419e003aea18df)EUSART1\_SCLK\_PD0

| #define EUSART1\_SCLK\_PD0   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x3, 0x0) |
| --- |

## [◆ ](#a8f314da8501571ed1fb5d9043a48f022)EUSART1\_SCLK\_PD1

| #define EUSART1\_SCLK\_PD1   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x3, 0x1) |
| --- |

## [◆ ](#a2ca42149963e87a955e9bc529ba1764e)EUSART1\_SCLK\_PD2

| #define EUSART1\_SCLK\_PD2   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x3, 0x2) |
| --- |

## [◆ ](#a408f40e7306530450a58ad4135df0401)EUSART1\_SCLK\_PD3

| #define EUSART1\_SCLK\_PD3   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x3, 0x3) |
| --- |

## [◆ ](#a2e59776258bebc0ce491a8a4f8357606)EUSART1\_SCLK\_PD4

| #define EUSART1\_SCLK\_PD4   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x3, 0x4) |
| --- |

## [◆ ](#a6ffd1010e2bd742569fc4c3a4c3b7bbb)EUSART1\_SCLK\_PD5

| #define EUSART1\_SCLK\_PD5   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x3, 0x5) |
| --- |

## [◆ ](#ab28778a5ee4f114285190a082c927118)EUSART1\_TX\_PA0

| #define EUSART1\_TX\_PA0   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x0) |
| --- |

## [◆ ](#a073c517a0afd9587386870a630518cbd)EUSART1\_TX\_PA1

| #define EUSART1\_TX\_PA1   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x1) |
| --- |

## [◆ ](#a806e7fc362384bc93b618a12af2473f8)EUSART1\_TX\_PA2

| #define EUSART1\_TX\_PA2   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x2) |
| --- |

## [◆ ](#a1702c830397c60f0b30b2b9fd9952f0d)EUSART1\_TX\_PA3

| #define EUSART1\_TX\_PA3   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x3) |
| --- |

## [◆ ](#a6f0b72325d6aafe9f875e9742a8c8042)EUSART1\_TX\_PA4

| #define EUSART1\_TX\_PA4   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x4) |
| --- |

## [◆ ](#ad0cde738ee0488057252b99b667ad00d)EUSART1\_TX\_PA5

| #define EUSART1\_TX\_PA5   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x5) |
| --- |

## [◆ ](#a448daaeb0e09d7e8ed1629f93c909539)EUSART1\_TX\_PA6

| #define EUSART1\_TX\_PA6   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x6) |
| --- |

## [◆ ](#aea3b8d30b2e1e43348278c7e33e33aa5)EUSART1\_TX\_PA7

| #define EUSART1\_TX\_PA7   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x7) |
| --- |

## [◆ ](#a01920e5d24b2a800d5a1b0d0341b9b1b)EUSART1\_TX\_PA8

| #define EUSART1\_TX\_PA8   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x8) |
| --- |

## [◆ ](#a0323bbaaef73d01d2a1321ccc8faba4b)EUSART1\_TX\_PA9

| #define EUSART1\_TX\_PA9   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x9) |
| --- |

## [◆ ](#ab39ba8c4be315f5a2222e168f474642d)EUSART1\_TX\_PB0

| #define EUSART1\_TX\_PB0   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x1, 0x0) |
| --- |

## [◆ ](#a71460a9b69af5340d0a13823fde821ec)EUSART1\_TX\_PB1

| #define EUSART1\_TX\_PB1   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x1, 0x1) |
| --- |

## [◆ ](#ae589d9854e598c01eeb5f660d4b07a61)EUSART1\_TX\_PB2

| #define EUSART1\_TX\_PB2   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x1, 0x2) |
| --- |

## [◆ ](#a8387994c7648c19dd755c09827923d8f)EUSART1\_TX\_PB3

| #define EUSART1\_TX\_PB3   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x1, 0x3) |
| --- |

## [◆ ](#a30635d481b97dd113d97f53faf8fcfe2)EUSART1\_TX\_PB4

| #define EUSART1\_TX\_PB4   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x1, 0x4) |
| --- |

## [◆ ](#a02a498c823ba30dbd5144e3f97da331c)EUSART1\_TX\_PB5

| #define EUSART1\_TX\_PB5   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x1, 0x5) |
| --- |

## [◆ ](#af974aba626dbdc04f04bcc6f13243b94)EUSART1\_TX\_PC0

| #define EUSART1\_TX\_PC0   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x0) |
| --- |

## [◆ ](#aa7802a5b57a1024764ffbe73b6b5ac39)EUSART1\_TX\_PC1

| #define EUSART1\_TX\_PC1   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x1) |
| --- |

## [◆ ](#a0c9b5f28eb50a9731a117ad5f366e92b)EUSART1\_TX\_PC2

| #define EUSART1\_TX\_PC2   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x2) |
| --- |

## [◆ ](#a6a348ac2b04733efa6c0ebe34ceb5d4b)EUSART1\_TX\_PC3

| #define EUSART1\_TX\_PC3   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x3) |
| --- |

## [◆ ](#a54dfb623abae97d99fa141c8a0bb0ea3)EUSART1\_TX\_PC4

| #define EUSART1\_TX\_PC4   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x4) |
| --- |

## [◆ ](#a1100968240942c988f4905912c28aa11)EUSART1\_TX\_PC5

| #define EUSART1\_TX\_PC5   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x5) |
| --- |

## [◆ ](#a6e8d91efe4ac6f8224907e3ee500051c)EUSART1\_TX\_PC6

| #define EUSART1\_TX\_PC6   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x6) |
| --- |

## [◆ ](#aed9ea236a9a98dbcc9516c4517cb04ed)EUSART1\_TX\_PC7

| #define EUSART1\_TX\_PC7   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x7) |
| --- |

## [◆ ](#ac017586ff569895b658de00f8d60043c)EUSART1\_TX\_PC8

| #define EUSART1\_TX\_PC8   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x8) |
| --- |

## [◆ ](#a342a564672104c6a47d12b75a3c4b726)EUSART1\_TX\_PC9

| #define EUSART1\_TX\_PC9   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x9) |
| --- |

## [◆ ](#a21666ee324c7d8339c10ee3a5841413b)EUSART1\_TX\_PD0

| #define EUSART1\_TX\_PD0   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x3, 0x0) |
| --- |

## [◆ ](#a63920c4b35211b7a2db371b6db68fe34)EUSART1\_TX\_PD1

| #define EUSART1\_TX\_PD1   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x3, 0x1) |
| --- |

## [◆ ](#a196cf0e44c04a0b39c143d89f674bc7d)EUSART1\_TX\_PD2

| #define EUSART1\_TX\_PD2   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x3, 0x2) |
| --- |

## [◆ ](#acd2c8e123057d490ba2e60b8dbac8836)EUSART1\_TX\_PD3

| #define EUSART1\_TX\_PD3   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x3, 0x3) |
| --- |

## [◆ ](#a5dcbf90a838018015ab60c8f480aa341)EUSART1\_TX\_PD4

| #define EUSART1\_TX\_PD4   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x3, 0x4) |
| --- |

## [◆ ](#a2cd212d6d8646fd8a6b0ea295a0e0426)EUSART1\_TX\_PD5

| #define EUSART1\_TX\_PD5   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x3, 0x5) |
| --- |

## [◆ ](#af3d9d425c19fc9f1c56b16a2ce3ca69b)HFXO0\_BUFOUTREQINASYNC\_PA0

| #define HFXO0\_BUFOUTREQINASYNC\_PA0   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x0) |
| --- |

## [◆ ](#ae0120388287c3f60a6190eda52121f0e)HFXO0\_BUFOUTREQINASYNC\_PA1

| #define HFXO0\_BUFOUTREQINASYNC\_PA1   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x1) |
| --- |

## [◆ ](#af4852125e31ddddd1fed1fdacf153e02)HFXO0\_BUFOUTREQINASYNC\_PA2

| #define HFXO0\_BUFOUTREQINASYNC\_PA2   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x2) |
| --- |

## [◆ ](#a25681d36b593b30263243a6cc5a319b1)HFXO0\_BUFOUTREQINASYNC\_PA3

| #define HFXO0\_BUFOUTREQINASYNC\_PA3   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x3) |
| --- |

## [◆ ](#a25093f4fd8152b2a499f78117b860d0c)HFXO0\_BUFOUTREQINASYNC\_PA4

| #define HFXO0\_BUFOUTREQINASYNC\_PA4   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x4) |
| --- |

## [◆ ](#aa6ce87ffb49361ab8876afa308d75777)HFXO0\_BUFOUTREQINASYNC\_PA5

| #define HFXO0\_BUFOUTREQINASYNC\_PA5   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x5) |
| --- |

## [◆ ](#ae0b89336110416cebaa0a1e899daa562)HFXO0\_BUFOUTREQINASYNC\_PA6

| #define HFXO0\_BUFOUTREQINASYNC\_PA6   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x6) |
| --- |

## [◆ ](#a4fe6a622e71c24bd3203fcb7f1ee0037)HFXO0\_BUFOUTREQINASYNC\_PA7

| #define HFXO0\_BUFOUTREQINASYNC\_PA7   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x7) |
| --- |

## [◆ ](#a26c5fbf9b20f95ea89a36640e4cad757)HFXO0\_BUFOUTREQINASYNC\_PA8

| #define HFXO0\_BUFOUTREQINASYNC\_PA8   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x8) |
| --- |

## [◆ ](#a35a6e2e7cf644a3b80df8d1739ef35da)HFXO0\_BUFOUTREQINASYNC\_PA9

| #define HFXO0\_BUFOUTREQINASYNC\_PA9   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x0, 0x9) |
| --- |

## [◆ ](#adc4fb29901bb4530d24f18598041e248)HFXO0\_BUFOUTREQINASYNC\_PB0

| #define HFXO0\_BUFOUTREQINASYNC\_PB0   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x1, 0x0) |
| --- |

## [◆ ](#a30174f1bc16727689379ce617ffa2696)HFXO0\_BUFOUTREQINASYNC\_PB1

| #define HFXO0\_BUFOUTREQINASYNC\_PB1   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x1, 0x1) |
| --- |

## [◆ ](#aca249022c7464cf1062124bd3ab7d399)HFXO0\_BUFOUTREQINASYNC\_PB2

| #define HFXO0\_BUFOUTREQINASYNC\_PB2   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x1, 0x2) |
| --- |

## [◆ ](#a0b069b62a4387a9819b03652bf123130)HFXO0\_BUFOUTREQINASYNC\_PB3

| #define HFXO0\_BUFOUTREQINASYNC\_PB3   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x1, 0x3) |
| --- |

## [◆ ](#a3959e7648de41ada54851249af0e776f)HFXO0\_BUFOUTREQINASYNC\_PB4

| #define HFXO0\_BUFOUTREQINASYNC\_PB4   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x1, 0x4) |
| --- |

## [◆ ](#aacf5c309e16b253413b98de57e5640ba)HFXO0\_BUFOUTREQINASYNC\_PB5

| #define HFXO0\_BUFOUTREQINASYNC\_PB5   [SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC](#a9e2c3084524d9b100defb0a6c9c62c4e)(0x1, 0x5) |
| --- |

## [◆ ](#a23ced15df4b090058198bd06541b5885)I2C0\_SCL\_PA0

| #define I2C0\_SCL\_PA0   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x0) |
| --- |

## [◆ ](#a695c8fa25220070f883a7866019132a5)I2C0\_SCL\_PA1

| #define I2C0\_SCL\_PA1   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x1) |
| --- |

## [◆ ](#a59521028aaeca25d19dce77adf76f9b7)I2C0\_SCL\_PA2

| #define I2C0\_SCL\_PA2   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x2) |
| --- |

## [◆ ](#a68f1a22cb1cf1445f9d94d230b7d81e6)I2C0\_SCL\_PA3

| #define I2C0\_SCL\_PA3   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x3) |
| --- |

## [◆ ](#aefbf0c45fe8a1215f17a6d31c5948889)I2C0\_SCL\_PA4

| #define I2C0\_SCL\_PA4   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x4) |
| --- |

## [◆ ](#ae334a06857e99d806213ccb6b6e582d3)I2C0\_SCL\_PA5

| #define I2C0\_SCL\_PA5   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x5) |
| --- |

## [◆ ](#a912dd4938a0b0cda381360467d635fc8)I2C0\_SCL\_PA6

| #define I2C0\_SCL\_PA6   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x6) |
| --- |

## [◆ ](#a843a8a1e536a19115dad9b821e09fc35)I2C0\_SCL\_PA7

| #define I2C0\_SCL\_PA7   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x7) |
| --- |

## [◆ ](#a5d5194c66eaa75401ef86ae1b702c882)I2C0\_SCL\_PA8

| #define I2C0\_SCL\_PA8   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x8) |
| --- |

## [◆ ](#aa8f0bedfe23ff1a8610fd95182a3e37d)I2C0\_SCL\_PA9

| #define I2C0\_SCL\_PA9   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x9) |
| --- |

## [◆ ](#a66acedca2ec779cfe23f1d9c6e2fc129)I2C0\_SCL\_PB0

| #define I2C0\_SCL\_PB0   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x1, 0x0) |
| --- |

## [◆ ](#a5af9487dc5b440644597f549fb4775e2)I2C0\_SCL\_PB1

| #define I2C0\_SCL\_PB1   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x1, 0x1) |
| --- |

## [◆ ](#a9bf6c40a60c458dcf38ab7eff6d90768)I2C0\_SCL\_PB2

| #define I2C0\_SCL\_PB2   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x1, 0x2) |
| --- |

## [◆ ](#a7cda95585deaad597713feece27a1a03)I2C0\_SCL\_PB3

| #define I2C0\_SCL\_PB3   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x1, 0x3) |
| --- |

## [◆ ](#add039d286e25d19092fcee79fac5c168)I2C0\_SCL\_PB4

| #define I2C0\_SCL\_PB4   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x1, 0x4) |
| --- |

## [◆ ](#a15a20ff8ec4b637e9fc1a2a892fd595d)I2C0\_SCL\_PB5

| #define I2C0\_SCL\_PB5   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x1, 0x5) |
| --- |

## [◆ ](#afda900994567b6303959e4f666fceaf1)I2C0\_SCL\_PC0

| #define I2C0\_SCL\_PC0   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x0) |
| --- |

## [◆ ](#aecced4d0cc1f98a1f8e87d09cceff92a)I2C0\_SCL\_PC1

| #define I2C0\_SCL\_PC1   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x1) |
| --- |

## [◆ ](#ab376247e3dbd84ccfd2b94af9c07505a)I2C0\_SCL\_PC2

| #define I2C0\_SCL\_PC2   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x2) |
| --- |

## [◆ ](#a9a9354d74c5e9c6ebad7e646f6b8ee63)I2C0\_SCL\_PC3

| #define I2C0\_SCL\_PC3   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x3) |
| --- |

## [◆ ](#aafe4a6c9133c8213940f026568866b9d)I2C0\_SCL\_PC4

| #define I2C0\_SCL\_PC4   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x4) |
| --- |

## [◆ ](#a93ad2564f0ad899a336521853e3c5f35)I2C0\_SCL\_PC5

| #define I2C0\_SCL\_PC5   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x5) |
| --- |

## [◆ ](#a45d40464f74efe9babb464d9e72ac0e1)I2C0\_SCL\_PC6

| #define I2C0\_SCL\_PC6   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x6) |
| --- |

## [◆ ](#aef0e85e86050336cd4112241ef60dad5)I2C0\_SCL\_PC7

| #define I2C0\_SCL\_PC7   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x7) |
| --- |

## [◆ ](#a9526c92c7e0e45214d4dc62cef77541e)I2C0\_SCL\_PC8

| #define I2C0\_SCL\_PC8   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x8) |
| --- |

## [◆ ](#a8a38516741fb879e1cfb2c501b3643b3)I2C0\_SCL\_PC9

| #define I2C0\_SCL\_PC9   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x9) |
| --- |

## [◆ ](#ab5e0b9a784779a5e92ab1fa79c9aa6cc)I2C0\_SCL\_PD0

| #define I2C0\_SCL\_PD0   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x3, 0x0) |
| --- |

## [◆ ](#a3d7b2816e4c4f01aba45a339bc77feea)I2C0\_SCL\_PD1

| #define I2C0\_SCL\_PD1   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x3, 0x1) |
| --- |

## [◆ ](#a487c9ff099c2dabf34d65f0377e5e195)I2C0\_SCL\_PD2

| #define I2C0\_SCL\_PD2   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x3, 0x2) |
| --- |

## [◆ ](#a2c36512ca362cf14654d72a59e4de079)I2C0\_SCL\_PD3

| #define I2C0\_SCL\_PD3   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x3, 0x3) |
| --- |

## [◆ ](#ae728f208472d11bf16da3eb76a64d152)I2C0\_SCL\_PD4

| #define I2C0\_SCL\_PD4   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x3, 0x4) |
| --- |

## [◆ ](#ac809898617970351e262e056c49dc0de)I2C0\_SCL\_PD5

| #define I2C0\_SCL\_PD5   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x3, 0x5) |
| --- |

## [◆ ](#aaf8bcb4a387404aa356da60c0e9cc869)I2C0\_SDA\_PA0

| #define I2C0\_SDA\_PA0   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x0) |
| --- |

## [◆ ](#a6f74ca01f25bdded002e45e679240275)I2C0\_SDA\_PA1

| #define I2C0\_SDA\_PA1   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x1) |
| --- |

## [◆ ](#acdc71a141f1ba40bb5c3ec9f06bd35e6)I2C0\_SDA\_PA2

| #define I2C0\_SDA\_PA2   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x2) |
| --- |

## [◆ ](#a401989601987cfb72944453f11918e2a)I2C0\_SDA\_PA3

| #define I2C0\_SDA\_PA3   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x3) |
| --- |

## [◆ ](#a66dad3b35dd2a650a186933abb43f6c3)I2C0\_SDA\_PA4

| #define I2C0\_SDA\_PA4   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x4) |
| --- |

## [◆ ](#a1fdfea195e2831a05d2ad42a091aa53b)I2C0\_SDA\_PA5

| #define I2C0\_SDA\_PA5   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x5) |
| --- |

## [◆ ](#a0c5573f60342f026d0553797a636a488)I2C0\_SDA\_PA6

| #define I2C0\_SDA\_PA6   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x6) |
| --- |

## [◆ ](#a35d947fc846c9fbe828b92169dbc30bd)I2C0\_SDA\_PA7

| #define I2C0\_SDA\_PA7   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x7) |
| --- |

## [◆ ](#a2bafe8f8b3424002354a87423c7564ff)I2C0\_SDA\_PA8

| #define I2C0\_SDA\_PA8   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x8) |
| --- |

## [◆ ](#a00b7f8f28847880fdd61b025eb224a44)I2C0\_SDA\_PA9

| #define I2C0\_SDA\_PA9   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x9) |
| --- |

## [◆ ](#a9e333616419f1afb29657e239ebf9b12)I2C0\_SDA\_PB0

| #define I2C0\_SDA\_PB0   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x1, 0x0) |
| --- |

## [◆ ](#a25bba68392534791cad2bc692a141782)I2C0\_SDA\_PB1

| #define I2C0\_SDA\_PB1   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x1, 0x1) |
| --- |

## [◆ ](#a36d3f871769d46038f7305c590f4da44)I2C0\_SDA\_PB2

| #define I2C0\_SDA\_PB2   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x1, 0x2) |
| --- |

## [◆ ](#af28ae3cd9556f78d2a9e9cbec5eea822)I2C0\_SDA\_PB3

| #define I2C0\_SDA\_PB3   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x1, 0x3) |
| --- |

## [◆ ](#aa0dfa7701ac813cb33f6b192e724c028)I2C0\_SDA\_PB4

| #define I2C0\_SDA\_PB4   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x1, 0x4) |
| --- |

## [◆ ](#aaca942a6078f9071a43a5a72bf2e290f)I2C0\_SDA\_PB5

| #define I2C0\_SDA\_PB5   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x1, 0x5) |
| --- |

## [◆ ](#acb9a1287a10a954e1ff0bf82478f3bf8)I2C0\_SDA\_PC0

| #define I2C0\_SDA\_PC0   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x0) |
| --- |

## [◆ ](#a0c89a72767592385a9a625d72c90f824)I2C0\_SDA\_PC1

| #define I2C0\_SDA\_PC1   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x1) |
| --- |

## [◆ ](#a0e115e41c26b45de04ee71a95cd5b87c)I2C0\_SDA\_PC2

| #define I2C0\_SDA\_PC2   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x2) |
| --- |

## [◆ ](#afbad7695056556b776533aafc47b0299)I2C0\_SDA\_PC3

| #define I2C0\_SDA\_PC3   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x3) |
| --- |

## [◆ ](#a603f80b261cded3f838f85ad889a4b88)I2C0\_SDA\_PC4

| #define I2C0\_SDA\_PC4   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x4) |
| --- |

## [◆ ](#a5864615c0e7063fc4f1acb8e4e3a05d2)I2C0\_SDA\_PC5

| #define I2C0\_SDA\_PC5   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x5) |
| --- |

## [◆ ](#a9e461e560cc99ba58586c4a4b9085c53)I2C0\_SDA\_PC6

| #define I2C0\_SDA\_PC6   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x6) |
| --- |

## [◆ ](#a1f6044bad1b47007a0250a99e778a7f4)I2C0\_SDA\_PC7

| #define I2C0\_SDA\_PC7   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x7) |
| --- |

## [◆ ](#a04887e1ba3314748ec246c534c0f1815)I2C0\_SDA\_PC8

| #define I2C0\_SDA\_PC8   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x8) |
| --- |

## [◆ ](#ac2e3516c9ce167083e4263fb7e78ecb6)I2C0\_SDA\_PC9

| #define I2C0\_SDA\_PC9   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x9) |
| --- |

## [◆ ](#a610731cb645ab65d802d95bb65437d8c)I2C0\_SDA\_PD0

| #define I2C0\_SDA\_PD0   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x3, 0x0) |
| --- |

## [◆ ](#a86eade4a55994ce4285b81cf29c93883)I2C0\_SDA\_PD1

| #define I2C0\_SDA\_PD1   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x3, 0x1) |
| --- |

## [◆ ](#a5d3416853673a2192ec5f5712921d370)I2C0\_SDA\_PD2

| #define I2C0\_SDA\_PD2   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x3, 0x2) |
| --- |

## [◆ ](#a096b74cd9e2842c5d4ff8d7a7186106a)I2C0\_SDA\_PD3

| #define I2C0\_SDA\_PD3   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x3, 0x3) |
| --- |

## [◆ ](#a39c83c73c763c0afc7e9041fab4549fd)I2C0\_SDA\_PD4

| #define I2C0\_SDA\_PD4   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x3, 0x4) |
| --- |

## [◆ ](#a031fdc04063f9f244527f159c098c8b7)I2C0\_SDA\_PD5

| #define I2C0\_SDA\_PD5   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x3, 0x5) |
| --- |

## [◆ ](#a356ddb78378e70250e07992cf92dd8b7)I2C1\_SCL\_PC0

| #define I2C1\_SCL\_PC0   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x0) |
| --- |

## [◆ ](#ad327d495abfaa2bb7ae3344a163f052f)I2C1\_SCL\_PC1

| #define I2C1\_SCL\_PC1   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x1) |
| --- |

## [◆ ](#aa89ddd739af59624f4a176443aa17636)I2C1\_SCL\_PC2

| #define I2C1\_SCL\_PC2   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x2) |
| --- |

## [◆ ](#af0e6baea8d2c35eb8991706946ffc05b)I2C1\_SCL\_PC3

| #define I2C1\_SCL\_PC3   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x3) |
| --- |

## [◆ ](#a346b20cbc89a5af4dfffe00c9ef41e92)I2C1\_SCL\_PC4

| #define I2C1\_SCL\_PC4   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x4) |
| --- |

## [◆ ](#aec416779b37e6a51e48e3fcadfca591a)I2C1\_SCL\_PC5

| #define I2C1\_SCL\_PC5   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x5) |
| --- |

## [◆ ](#a7e3349a10010f0f54657e0fb5e92ffe2)I2C1\_SCL\_PC6

| #define I2C1\_SCL\_PC6   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x6) |
| --- |

## [◆ ](#a2c5373d8cd0dfc39e30c9460552201ef)I2C1\_SCL\_PC7

| #define I2C1\_SCL\_PC7   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x7) |
| --- |

## [◆ ](#ad58c7138909480a48e097484cdddf818)I2C1\_SCL\_PC8

| #define I2C1\_SCL\_PC8   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x8) |
| --- |

## [◆ ](#adef41b41e7e00135ae28db22c8bc6995)I2C1\_SCL\_PC9

| #define I2C1\_SCL\_PC9   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x9) |
| --- |

## [◆ ](#a865b5c341b794b96daba59c14807c057)I2C1\_SCL\_PD0

| #define I2C1\_SCL\_PD0   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x3, 0x0) |
| --- |

## [◆ ](#a9f3ebaefe248d5aa292ade2727a11ee9)I2C1\_SCL\_PD1

| #define I2C1\_SCL\_PD1   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x3, 0x1) |
| --- |

## [◆ ](#a7eb71571b0e15669fb353a0bd65f2c72)I2C1\_SCL\_PD2

| #define I2C1\_SCL\_PD2   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x3, 0x2) |
| --- |

## [◆ ](#a6a86266c8ab637b0b31244cbf0636ab0)I2C1\_SCL\_PD3

| #define I2C1\_SCL\_PD3   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x3, 0x3) |
| --- |

## [◆ ](#a575a4a9e08a65805c5d9fa3591f563bb)I2C1\_SCL\_PD4

| #define I2C1\_SCL\_PD4   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x3, 0x4) |
| --- |

## [◆ ](#aa3327376858c7599a6b95c2e0be85bb8)I2C1\_SCL\_PD5

| #define I2C1\_SCL\_PD5   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x3, 0x5) |
| --- |

## [◆ ](#a7239b0bfd8b71b2ee9e85e8cb2e6eaaf)I2C1\_SDA\_PC0

| #define I2C1\_SDA\_PC0   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x0) |
| --- |

## [◆ ](#afe966c9b62cc1e0d598ea6ea92d663b8)I2C1\_SDA\_PC1

| #define I2C1\_SDA\_PC1   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x1) |
| --- |

## [◆ ](#af3ba02992276ed2088a6652b695d270d)I2C1\_SDA\_PC2

| #define I2C1\_SDA\_PC2   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x2) |
| --- |

## [◆ ](#a424670a07eab18c7e3ce3db2d68d44f6)I2C1\_SDA\_PC3

| #define I2C1\_SDA\_PC3   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x3) |
| --- |

## [◆ ](#ad7eebe896b02c99e7f27340a8ea01a8f)I2C1\_SDA\_PC4

| #define I2C1\_SDA\_PC4   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x4) |
| --- |

## [◆ ](#a12822294913c78002356a6be7b698e2e)I2C1\_SDA\_PC5

| #define I2C1\_SDA\_PC5   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x5) |
| --- |

## [◆ ](#a9af96f372e04b931184d7a9bd716b733)I2C1\_SDA\_PC6

| #define I2C1\_SDA\_PC6   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x6) |
| --- |

## [◆ ](#a766136e7b677f8c4ddcc6053b0527eee)I2C1\_SDA\_PC7

| #define I2C1\_SDA\_PC7   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x7) |
| --- |

## [◆ ](#aaaae2fcde9dc48a4917da54216304dc4)I2C1\_SDA\_PC8

| #define I2C1\_SDA\_PC8   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x8) |
| --- |

## [◆ ](#a2b0f34f00795ef75bf9e7cf1e85db5fc)I2C1\_SDA\_PC9

| #define I2C1\_SDA\_PC9   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x9) |
| --- |

## [◆ ](#a58f45546c69325b13cd062ca7a238c7a)I2C1\_SDA\_PD0

| #define I2C1\_SDA\_PD0   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x3, 0x0) |
| --- |

## [◆ ](#aa7cf52519a05cd49aef954ce5191a377)I2C1\_SDA\_PD1

| #define I2C1\_SDA\_PD1   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x3, 0x1) |
| --- |

## [◆ ](#ad779ebeed2865070af9e56244e9c43d0)I2C1\_SDA\_PD2

| #define I2C1\_SDA\_PD2   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x3, 0x2) |
| --- |

## [◆ ](#a77b0c5734afd5123fd3ae520f10a8da8)I2C1\_SDA\_PD3

| #define I2C1\_SDA\_PD3   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x3, 0x3) |
| --- |

## [◆ ](#acc6ad96c0e1645c02ca291c641ba06dd)I2C1\_SDA\_PD4

| #define I2C1\_SDA\_PD4   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x3, 0x4) |
| --- |

## [◆ ](#aa358107fadec4f7d22d77a490c01b6d6)I2C1\_SDA\_PD5

| #define I2C1\_SDA\_PD5   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x3, 0x5) |
| --- |

## [◆ ](#a5a52c17c2d01b0d927d1f1789799baa0)KEYSCAN\_COLOUT0\_PA0

| #define KEYSCAN\_COLOUT0\_PA0   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x0) |
| --- |

## [◆ ](#a9fff3683d3c03b4838665acece21a2b9)KEYSCAN\_COLOUT0\_PA1

| #define KEYSCAN\_COLOUT0\_PA1   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x1) |
| --- |

## [◆ ](#ab94c7fd6fff04ec1f58ccf71a3f64d71)KEYSCAN\_COLOUT0\_PA2

| #define KEYSCAN\_COLOUT0\_PA2   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x2) |
| --- |

## [◆ ](#a15b8ef2e967e747c47089c6063b05b0c)KEYSCAN\_COLOUT0\_PA3

| #define KEYSCAN\_COLOUT0\_PA3   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x3) |
| --- |

## [◆ ](#a5144e066ae5582d32c35077d35561b5d)KEYSCAN\_COLOUT0\_PA4

| #define KEYSCAN\_COLOUT0\_PA4   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x4) |
| --- |

## [◆ ](#ae24656b03d1c97af530ec70aba4a3dd0)KEYSCAN\_COLOUT0\_PA5

| #define KEYSCAN\_COLOUT0\_PA5   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x5) |
| --- |

## [◆ ](#a1bfd896f4a8cfc3c9fc7728e605da898)KEYSCAN\_COLOUT0\_PA6

| #define KEYSCAN\_COLOUT0\_PA6   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x6) |
| --- |

## [◆ ](#ad801588fc6185834de0756b4cc7ad515)KEYSCAN\_COLOUT0\_PA7

| #define KEYSCAN\_COLOUT0\_PA7   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x7) |
| --- |

## [◆ ](#a4b4d69573db9515dae391c6b50c034f3)KEYSCAN\_COLOUT0\_PA8

| #define KEYSCAN\_COLOUT0\_PA8   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x8) |
| --- |

## [◆ ](#abd423f23fddf4ebf57217456c3119a15)KEYSCAN\_COLOUT0\_PA9

| #define KEYSCAN\_COLOUT0\_PA9   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x0, 0x9) |
| --- |

## [◆ ](#ab0c4a297a4c6ed9773b553f60888a909)KEYSCAN\_COLOUT0\_PB0

| #define KEYSCAN\_COLOUT0\_PB0   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x1, 0x0) |
| --- |

## [◆ ](#a12803bfebb31fdf51abff7e8b5493cdb)KEYSCAN\_COLOUT0\_PB1

| #define KEYSCAN\_COLOUT0\_PB1   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x1, 0x1) |
| --- |

## [◆ ](#a4e8586a0245688807f04309a918db99f)KEYSCAN\_COLOUT0\_PB2

| #define KEYSCAN\_COLOUT0\_PB2   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x1, 0x2) |
| --- |

## [◆ ](#a1cadf61f842c48b554b81aebc8cb9fc7)KEYSCAN\_COLOUT0\_PB3

| #define KEYSCAN\_COLOUT0\_PB3   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x1, 0x3) |
| --- |

## [◆ ](#a8f2661a33400963325b8ac00bfba742a)KEYSCAN\_COLOUT0\_PB4

| #define KEYSCAN\_COLOUT0\_PB4   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x1, 0x4) |
| --- |

## [◆ ](#adbafd9459e27053eeea0bba9bccc0963)KEYSCAN\_COLOUT0\_PB5

| #define KEYSCAN\_COLOUT0\_PB5   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x1, 0x5) |
| --- |

## [◆ ](#abb524534a587b5743914ebc4dc739146)KEYSCAN\_COLOUT0\_PC0

| #define KEYSCAN\_COLOUT0\_PC0   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x0) |
| --- |

## [◆ ](#aad7e9172ac7d76e534c7da9b7b66089e)KEYSCAN\_COLOUT0\_PC1

| #define KEYSCAN\_COLOUT0\_PC1   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x1) |
| --- |

## [◆ ](#a9afcd7a32f9104f7cf51469e2aebef82)KEYSCAN\_COLOUT0\_PC2

| #define KEYSCAN\_COLOUT0\_PC2   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x2) |
| --- |

## [◆ ](#a5707925aec785899730a8bfeaf394603)KEYSCAN\_COLOUT0\_PC3

| #define KEYSCAN\_COLOUT0\_PC3   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x3) |
| --- |

## [◆ ](#a0080f5ba8da300d83288f8e5f430f397)KEYSCAN\_COLOUT0\_PC4

| #define KEYSCAN\_COLOUT0\_PC4   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x4) |
| --- |

## [◆ ](#a2abef42db8dcce330fe2c97f20e1bf9f)KEYSCAN\_COLOUT0\_PC5

| #define KEYSCAN\_COLOUT0\_PC5   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x5) |
| --- |

## [◆ ](#a9cc0d32219cc4ec9906eea216ba59fc6)KEYSCAN\_COLOUT0\_PC6

| #define KEYSCAN\_COLOUT0\_PC6   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x6) |
| --- |

## [◆ ](#ab009d348c504d64e8ff6efda0648628b)KEYSCAN\_COLOUT0\_PC7

| #define KEYSCAN\_COLOUT0\_PC7   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x7) |
| --- |

## [◆ ](#ab22d970887a912d0ca9b48bcb984fafc)KEYSCAN\_COLOUT0\_PC8

| #define KEYSCAN\_COLOUT0\_PC8   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x8) |
| --- |

## [◆ ](#afbbf0bc01441a4ef05d408803ed785af)KEYSCAN\_COLOUT0\_PC9

| #define KEYSCAN\_COLOUT0\_PC9   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x2, 0x9) |
| --- |

## [◆ ](#ad2e95f939a9cb0a63b5a761f5172c4eb)KEYSCAN\_COLOUT0\_PD0

| #define KEYSCAN\_COLOUT0\_PD0   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x3, 0x0) |
| --- |

## [◆ ](#a7b08c7c464bc45efe7b8a6321eab7d0a)KEYSCAN\_COLOUT0\_PD1

| #define KEYSCAN\_COLOUT0\_PD1   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x3, 0x1) |
| --- |

## [◆ ](#a07c5cca743ef9e9116f5f052be296614)KEYSCAN\_COLOUT0\_PD2

| #define KEYSCAN\_COLOUT0\_PD2   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x3, 0x2) |
| --- |

## [◆ ](#a4ba404af21d187ee3b2acee0bbb45b80)KEYSCAN\_COLOUT0\_PD3

| #define KEYSCAN\_COLOUT0\_PD3   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x3, 0x3) |
| --- |

## [◆ ](#a81d01d684c85901328abae65477e8c85)KEYSCAN\_COLOUT0\_PD4

| #define KEYSCAN\_COLOUT0\_PD4   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x3, 0x4) |
| --- |

## [◆ ](#a9e0a39cf0ea3697a658f14336b07e21a)KEYSCAN\_COLOUT0\_PD5

| #define KEYSCAN\_COLOUT0\_PD5   [SILABS\_DBUS\_KEYSCAN\_COLOUT0](#a8debbf4560f2146abebba2cab72a0b95)(0x3, 0x5) |
| --- |

## [◆ ](#a585e4b13c4c2a32cde5e1f224e02f7ef)KEYSCAN\_COLOUT1\_PA0

| #define KEYSCAN\_COLOUT1\_PA0   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x0) |
| --- |

## [◆ ](#a23e571b563a9b17f3995e196920ed787)KEYSCAN\_COLOUT1\_PA1

| #define KEYSCAN\_COLOUT1\_PA1   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x1) |
| --- |

## [◆ ](#a2e2f89a8c1789ac9263d314507e9e73a)KEYSCAN\_COLOUT1\_PA2

| #define KEYSCAN\_COLOUT1\_PA2   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x2) |
| --- |

## [◆ ](#acdad26c2b77719f828d3f880249c02e5)KEYSCAN\_COLOUT1\_PA3

| #define KEYSCAN\_COLOUT1\_PA3   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x3) |
| --- |

## [◆ ](#a7f4d0e3b279df6d292530be268d2071b)KEYSCAN\_COLOUT1\_PA4

| #define KEYSCAN\_COLOUT1\_PA4   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x4) |
| --- |

## [◆ ](#a8b302968635f80d94e72be44a299d27c)KEYSCAN\_COLOUT1\_PA5

| #define KEYSCAN\_COLOUT1\_PA5   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x5) |
| --- |

## [◆ ](#a70d0d23bac357d94df02565a5425d638)KEYSCAN\_COLOUT1\_PA6

| #define KEYSCAN\_COLOUT1\_PA6   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x6) |
| --- |

## [◆ ](#ae24777bf7cb160303784ef61983260b3)KEYSCAN\_COLOUT1\_PA7

| #define KEYSCAN\_COLOUT1\_PA7   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x7) |
| --- |

## [◆ ](#acdb13af3e9e2a95af259e77c6dbb6c6f)KEYSCAN\_COLOUT1\_PA8

| #define KEYSCAN\_COLOUT1\_PA8   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x8) |
| --- |

## [◆ ](#a8a5e8de7629558a6828faa47489e02d4)KEYSCAN\_COLOUT1\_PA9

| #define KEYSCAN\_COLOUT1\_PA9   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x0, 0x9) |
| --- |

## [◆ ](#aeeb75a748919caf477f64db4608c24d1)KEYSCAN\_COLOUT1\_PB0

| #define KEYSCAN\_COLOUT1\_PB0   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x1, 0x0) |
| --- |

## [◆ ](#ac239f7a9cd68a765869ee273e055f682)KEYSCAN\_COLOUT1\_PB1

| #define KEYSCAN\_COLOUT1\_PB1   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x1, 0x1) |
| --- |

## [◆ ](#addcb4f9d603cc3ad5f66fac5d15f5eaf)KEYSCAN\_COLOUT1\_PB2

| #define KEYSCAN\_COLOUT1\_PB2   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x1, 0x2) |
| --- |

## [◆ ](#ae68a56d183ec317f20f4e45afb27d0a9)KEYSCAN\_COLOUT1\_PB3

| #define KEYSCAN\_COLOUT1\_PB3   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x1, 0x3) |
| --- |

## [◆ ](#a1560ccbed329f572422ce3c9611a1bf9)KEYSCAN\_COLOUT1\_PB4

| #define KEYSCAN\_COLOUT1\_PB4   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x1, 0x4) |
| --- |

## [◆ ](#a5599a02f156e263bdf22cb8d1aa54f05)KEYSCAN\_COLOUT1\_PB5

| #define KEYSCAN\_COLOUT1\_PB5   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x1, 0x5) |
| --- |

## [◆ ](#a932a022eee08bafd1095c84493ae8269)KEYSCAN\_COLOUT1\_PC0

| #define KEYSCAN\_COLOUT1\_PC0   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x0) |
| --- |

## [◆ ](#a03f0a2736a653f56eed67716b4e2e139)KEYSCAN\_COLOUT1\_PC1

| #define KEYSCAN\_COLOUT1\_PC1   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x1) |
| --- |

## [◆ ](#a1dd0502f99367c9604216df6598f317b)KEYSCAN\_COLOUT1\_PC2

| #define KEYSCAN\_COLOUT1\_PC2   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x2) |
| --- |

## [◆ ](#a198e72a8d977191639703245ed2bd8dc)KEYSCAN\_COLOUT1\_PC3

| #define KEYSCAN\_COLOUT1\_PC3   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x3) |
| --- |

## [◆ ](#a5a967a7c71870a65ad9d079c7bfbaab0)KEYSCAN\_COLOUT1\_PC4

| #define KEYSCAN\_COLOUT1\_PC4   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x4) |
| --- |

## [◆ ](#a8fe532890f0eb93e3286a8a8edf2b93f)KEYSCAN\_COLOUT1\_PC5

| #define KEYSCAN\_COLOUT1\_PC5   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x5) |
| --- |

## [◆ ](#a15888722bdfb0bbbef8c31a4cf9c8985)KEYSCAN\_COLOUT1\_PC6

| #define KEYSCAN\_COLOUT1\_PC6   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x6) |
| --- |

## [◆ ](#a160e29c849558b4c6999268886fb4c23)KEYSCAN\_COLOUT1\_PC7

| #define KEYSCAN\_COLOUT1\_PC7   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x7) |
| --- |

## [◆ ](#a0fa0481356cb6b6318fcac34cb509841)KEYSCAN\_COLOUT1\_PC8

| #define KEYSCAN\_COLOUT1\_PC8   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x8) |
| --- |

## [◆ ](#ad0cb6a921e60c3a82ea15bbaacb8774b)KEYSCAN\_COLOUT1\_PC9

| #define KEYSCAN\_COLOUT1\_PC9   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x2, 0x9) |
| --- |

## [◆ ](#a93d2ba7842a3d86906ef7e4df9749080)KEYSCAN\_COLOUT1\_PD0

| #define KEYSCAN\_COLOUT1\_PD0   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x3, 0x0) |
| --- |

## [◆ ](#a8b422e4deb2ec1d01c2aac2f6af6bc67)KEYSCAN\_COLOUT1\_PD1

| #define KEYSCAN\_COLOUT1\_PD1   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x3, 0x1) |
| --- |

## [◆ ](#a87d3c63729eea7683037e6654c1774cf)KEYSCAN\_COLOUT1\_PD2

| #define KEYSCAN\_COLOUT1\_PD2   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x3, 0x2) |
| --- |

## [◆ ](#a43e07d12179fcd36df7a76153d44be01)KEYSCAN\_COLOUT1\_PD3

| #define KEYSCAN\_COLOUT1\_PD3   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x3, 0x3) |
| --- |

## [◆ ](#a76e7168783cbdb2358839659b30a5bdc)KEYSCAN\_COLOUT1\_PD4

| #define KEYSCAN\_COLOUT1\_PD4   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x3, 0x4) |
| --- |

## [◆ ](#aa0b8adae419c63895b1bb7d2c15be3c3)KEYSCAN\_COLOUT1\_PD5

| #define KEYSCAN\_COLOUT1\_PD5   [SILABS\_DBUS\_KEYSCAN\_COLOUT1](#a64f28976cada3adedec8c5009842bf36)(0x3, 0x5) |
| --- |

## [◆ ](#a6be8610a8244eea2604a70095a1c4295)KEYSCAN\_COLOUT2\_PA0

| #define KEYSCAN\_COLOUT2\_PA0   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x0) |
| --- |

## [◆ ](#a6603cb0d0414111622dddf2b61f3b591)KEYSCAN\_COLOUT2\_PA1

| #define KEYSCAN\_COLOUT2\_PA1   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x1) |
| --- |

## [◆ ](#a81a89ec570413274e429f227cf538a6e)KEYSCAN\_COLOUT2\_PA2

| #define KEYSCAN\_COLOUT2\_PA2   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x2) |
| --- |

## [◆ ](#a793b58a63d42ab849c0f8bbc86bee96c)KEYSCAN\_COLOUT2\_PA3

| #define KEYSCAN\_COLOUT2\_PA3   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x3) |
| --- |

## [◆ ](#ad857e03569550385d2aacee030a9b544)KEYSCAN\_COLOUT2\_PA4

| #define KEYSCAN\_COLOUT2\_PA4   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x4) |
| --- |

## [◆ ](#a3f89b59444a1cf1e18de80aa6d4b38b8)KEYSCAN\_COLOUT2\_PA5

| #define KEYSCAN\_COLOUT2\_PA5   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x5) |
| --- |

## [◆ ](#a01768786f5ca06503028551896f969bf)KEYSCAN\_COLOUT2\_PA6

| #define KEYSCAN\_COLOUT2\_PA6   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x6) |
| --- |

## [◆ ](#a3637bc9d929a1432ab1ede17fae1d7a4)KEYSCAN\_COLOUT2\_PA7

| #define KEYSCAN\_COLOUT2\_PA7   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x7) |
| --- |

## [◆ ](#ae436e26a420b29f2d750b817facd0fb8)KEYSCAN\_COLOUT2\_PA8

| #define KEYSCAN\_COLOUT2\_PA8   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x8) |
| --- |

## [◆ ](#a0c2e1f78e65657580e7d96990b93cf56)KEYSCAN\_COLOUT2\_PA9

| #define KEYSCAN\_COLOUT2\_PA9   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x0, 0x9) |
| --- |

## [◆ ](#a365aab802299270c6de27adf800dd87c)KEYSCAN\_COLOUT2\_PB0

| #define KEYSCAN\_COLOUT2\_PB0   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x1, 0x0) |
| --- |

## [◆ ](#a2919c4881170222fc5b0ab36e238bb1c)KEYSCAN\_COLOUT2\_PB1

| #define KEYSCAN\_COLOUT2\_PB1   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x1, 0x1) |
| --- |

## [◆ ](#acabdbd88d881e9e13ad0d63408655254)KEYSCAN\_COLOUT2\_PB2

| #define KEYSCAN\_COLOUT2\_PB2   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x1, 0x2) |
| --- |

## [◆ ](#a27a4f418d6e94cc3a84985d21472da82)KEYSCAN\_COLOUT2\_PB3

| #define KEYSCAN\_COLOUT2\_PB3   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x1, 0x3) |
| --- |

## [◆ ](#aa9f88e831fae771d58b15f2025becb6e)KEYSCAN\_COLOUT2\_PB4

| #define KEYSCAN\_COLOUT2\_PB4   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x1, 0x4) |
| --- |

## [◆ ](#a2c9ebc343266b5ef73679be5b8f8f813)KEYSCAN\_COLOUT2\_PB5

| #define KEYSCAN\_COLOUT2\_PB5   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x1, 0x5) |
| --- |

## [◆ ](#ace40c834a7c4f5278d0d3b7f9fc2494f)KEYSCAN\_COLOUT2\_PC0

| #define KEYSCAN\_COLOUT2\_PC0   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x0) |
| --- |

## [◆ ](#af2ef81e0fd7e325580445028c001e6e8)KEYSCAN\_COLOUT2\_PC1

| #define KEYSCAN\_COLOUT2\_PC1   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x1) |
| --- |

## [◆ ](#a03aec2318a85899434ad83e876306695)KEYSCAN\_COLOUT2\_PC2

| #define KEYSCAN\_COLOUT2\_PC2   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x2) |
| --- |

## [◆ ](#ac0724d8d3da62eb8a1ada017f4db7559)KEYSCAN\_COLOUT2\_PC3

| #define KEYSCAN\_COLOUT2\_PC3   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x3) |
| --- |

## [◆ ](#a8268180b2bdc425f74de1a9963f80860)KEYSCAN\_COLOUT2\_PC4

| #define KEYSCAN\_COLOUT2\_PC4   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x4) |
| --- |

## [◆ ](#a7102c14ca84bd45f08b287984c8bb235)KEYSCAN\_COLOUT2\_PC5

| #define KEYSCAN\_COLOUT2\_PC5   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x5) |
| --- |

## [◆ ](#a0b50ad00c28a65aeedf64dd7a9b74d6a)KEYSCAN\_COLOUT2\_PC6

| #define KEYSCAN\_COLOUT2\_PC6   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x6) |
| --- |

## [◆ ](#a36856803b55973f9609f98cc1285deb5)KEYSCAN\_COLOUT2\_PC7

| #define KEYSCAN\_COLOUT2\_PC7   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x7) |
| --- |

## [◆ ](#ac4b08b6179b8fe4543a853da3c95f9f9)KEYSCAN\_COLOUT2\_PC8

| #define KEYSCAN\_COLOUT2\_PC8   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x8) |
| --- |

## [◆ ](#abc9bce5051ca6bbd875721bd5e707d11)KEYSCAN\_COLOUT2\_PC9

| #define KEYSCAN\_COLOUT2\_PC9   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x2, 0x9) |
| --- |

## [◆ ](#ace5b1670761e6a066cdea315262ca30b)KEYSCAN\_COLOUT2\_PD0

| #define KEYSCAN\_COLOUT2\_PD0   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x3, 0x0) |
| --- |

## [◆ ](#ab66177ddf55f90cd43f8ee3d3f516ce5)KEYSCAN\_COLOUT2\_PD1

| #define KEYSCAN\_COLOUT2\_PD1   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x3, 0x1) |
| --- |

## [◆ ](#a9757fbcc8516b46adf632109f0061da4)KEYSCAN\_COLOUT2\_PD2

| #define KEYSCAN\_COLOUT2\_PD2   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x3, 0x2) |
| --- |

## [◆ ](#a181443f7f56e88e47a570943402478d3)KEYSCAN\_COLOUT2\_PD3

| #define KEYSCAN\_COLOUT2\_PD3   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x3, 0x3) |
| --- |

## [◆ ](#aa31ea9f7edaabac76fc260248bb942f0)KEYSCAN\_COLOUT2\_PD4

| #define KEYSCAN\_COLOUT2\_PD4   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x3, 0x4) |
| --- |

## [◆ ](#a0572022128c37c99d4a96b712dabbc27)KEYSCAN\_COLOUT2\_PD5

| #define KEYSCAN\_COLOUT2\_PD5   [SILABS\_DBUS\_KEYSCAN\_COLOUT2](#a5647a9273865ecbe7da48783a8b3c121)(0x3, 0x5) |
| --- |

## [◆ ](#a51c859388a817c10421d8f57aa4c3518)KEYSCAN\_COLOUT3\_PA0

| #define KEYSCAN\_COLOUT3\_PA0   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x0) |
| --- |

## [◆ ](#a8d13e69bcdc4e1892ceaea8d42665b99)KEYSCAN\_COLOUT3\_PA1

| #define KEYSCAN\_COLOUT3\_PA1   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x1) |
| --- |

## [◆ ](#ac1be0018ccc29a2708e72acb75d51158)KEYSCAN\_COLOUT3\_PA2

| #define KEYSCAN\_COLOUT3\_PA2   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x2) |
| --- |

## [◆ ](#a01fe6c4c242f6c330434123fd734da83)KEYSCAN\_COLOUT3\_PA3

| #define KEYSCAN\_COLOUT3\_PA3   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x3) |
| --- |

## [◆ ](#a6b6c8fdd388d9058a89a1ba983851ead)KEYSCAN\_COLOUT3\_PA4

| #define KEYSCAN\_COLOUT3\_PA4   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x4) |
| --- |

## [◆ ](#af2b736e90ed10f923d78c00e7106c0dd)KEYSCAN\_COLOUT3\_PA5

| #define KEYSCAN\_COLOUT3\_PA5   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x5) |
| --- |

## [◆ ](#aa3d560b392fd6808579f02e8e4fa593d)KEYSCAN\_COLOUT3\_PA6

| #define KEYSCAN\_COLOUT3\_PA6   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x6) |
| --- |

## [◆ ](#abf1f603bcf07b715ec3592b9898eaaaf)KEYSCAN\_COLOUT3\_PA7

| #define KEYSCAN\_COLOUT3\_PA7   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x7) |
| --- |

## [◆ ](#a231728ec3f628502a13009e5b22fa60f)KEYSCAN\_COLOUT3\_PA8

| #define KEYSCAN\_COLOUT3\_PA8   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x8) |
| --- |

## [◆ ](#a2be978ee87b3ecaf4f05cc90c01f9a65)KEYSCAN\_COLOUT3\_PA9

| #define KEYSCAN\_COLOUT3\_PA9   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x0, 0x9) |
| --- |

## [◆ ](#a7b60f0f663b3e15a1647be43970b33d9)KEYSCAN\_COLOUT3\_PB0

| #define KEYSCAN\_COLOUT3\_PB0   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x1, 0x0) |
| --- |

## [◆ ](#a3c3ddd9ed7588b19bcb67d20051b6907)KEYSCAN\_COLOUT3\_PB1

| #define KEYSCAN\_COLOUT3\_PB1   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x1, 0x1) |
| --- |

## [◆ ](#a582697e0b5c3235325b8769ac5a6bae5)KEYSCAN\_COLOUT3\_PB2

| #define KEYSCAN\_COLOUT3\_PB2   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x1, 0x2) |
| --- |

## [◆ ](#a67632e0b8e6a5097d57cab38e4ded747)KEYSCAN\_COLOUT3\_PB3

| #define KEYSCAN\_COLOUT3\_PB3   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x1, 0x3) |
| --- |

## [◆ ](#aed301ef0f03969a3955c10413b7a7f45)KEYSCAN\_COLOUT3\_PB4

| #define KEYSCAN\_COLOUT3\_PB4   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x1, 0x4) |
| --- |

## [◆ ](#a02bb5d3ad9c153987999579d174ea167)KEYSCAN\_COLOUT3\_PB5

| #define KEYSCAN\_COLOUT3\_PB5   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x1, 0x5) |
| --- |

## [◆ ](#a14d9ca34a9975ae9ea2a2c13be3c90e3)KEYSCAN\_COLOUT3\_PC0

| #define KEYSCAN\_COLOUT3\_PC0   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x0) |
| --- |

## [◆ ](#a8c0874eb69aa803c0ef1f2d047eccd2b)KEYSCAN\_COLOUT3\_PC1

| #define KEYSCAN\_COLOUT3\_PC1   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x1) |
| --- |

## [◆ ](#ac17fc25a532f9d104e27080f31e892e8)KEYSCAN\_COLOUT3\_PC2

| #define KEYSCAN\_COLOUT3\_PC2   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x2) |
| --- |

## [◆ ](#a7dccd1b112a71187973000077527a63d)KEYSCAN\_COLOUT3\_PC3

| #define KEYSCAN\_COLOUT3\_PC3   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x3) |
| --- |

## [◆ ](#a3c97b3a952101dc9f34b72106d5a87a3)KEYSCAN\_COLOUT3\_PC4

| #define KEYSCAN\_COLOUT3\_PC4   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x4) |
| --- |

## [◆ ](#a7d4670705a96667b595135bf7b69b27a)KEYSCAN\_COLOUT3\_PC5

| #define KEYSCAN\_COLOUT3\_PC5   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x5) |
| --- |

## [◆ ](#ad0b6eeec83a80bd3eefc6ec9c795f211)KEYSCAN\_COLOUT3\_PC6

| #define KEYSCAN\_COLOUT3\_PC6   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x6) |
| --- |

## [◆ ](#a07e11db7d66d0f47a800d437d1451c7b)KEYSCAN\_COLOUT3\_PC7

| #define KEYSCAN\_COLOUT3\_PC7   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x7) |
| --- |

## [◆ ](#ac9e57d422d9d2b636a7482744894b43c)KEYSCAN\_COLOUT3\_PC8

| #define KEYSCAN\_COLOUT3\_PC8   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x8) |
| --- |

## [◆ ](#ad0737dc2ebdc663e17e677574cb5ccec)KEYSCAN\_COLOUT3\_PC9

| #define KEYSCAN\_COLOUT3\_PC9   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x2, 0x9) |
| --- |

## [◆ ](#a88f98c3d74687422cf458864da9fb5a7)KEYSCAN\_COLOUT3\_PD0

| #define KEYSCAN\_COLOUT3\_PD0   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x3, 0x0) |
| --- |

## [◆ ](#aae40661805acf791be1c66d3a2dfa63a)KEYSCAN\_COLOUT3\_PD1

| #define KEYSCAN\_COLOUT3\_PD1   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x3, 0x1) |
| --- |

## [◆ ](#a26ebcb6f8957068bfeb1cbe8f3e82349)KEYSCAN\_COLOUT3\_PD2

| #define KEYSCAN\_COLOUT3\_PD2   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x3, 0x2) |
| --- |

## [◆ ](#aa60f7d0f40d5be380e767430fda26b42)KEYSCAN\_COLOUT3\_PD3

| #define KEYSCAN\_COLOUT3\_PD3   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x3, 0x3) |
| --- |

## [◆ ](#adc07cf653f0c8b39c809ec7cdf12589f)KEYSCAN\_COLOUT3\_PD4

| #define KEYSCAN\_COLOUT3\_PD4   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x3, 0x4) |
| --- |

## [◆ ](#a336fd8f6980b4c439412327e29659665)KEYSCAN\_COLOUT3\_PD5

| #define KEYSCAN\_COLOUT3\_PD5   [SILABS\_DBUS\_KEYSCAN\_COLOUT3](#afa0c224603ec9ec120dac7bc6a4feadf)(0x3, 0x5) |
| --- |

## [◆ ](#a78e1f197ada2e32957011566ac1a5aa3)KEYSCAN\_COLOUT4\_PA0

| #define KEYSCAN\_COLOUT4\_PA0   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x0) |
| --- |

## [◆ ](#a515e07048d2b6beee5e58dd6e64cabc8)KEYSCAN\_COLOUT4\_PA1

| #define KEYSCAN\_COLOUT4\_PA1   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x1) |
| --- |

## [◆ ](#a48b7ad094af7fec9cb41211e35ea24a8)KEYSCAN\_COLOUT4\_PA2

| #define KEYSCAN\_COLOUT4\_PA2   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x2) |
| --- |

## [◆ ](#ae23d4333a8f2ea922dfec0fdc5274265)KEYSCAN\_COLOUT4\_PA3

| #define KEYSCAN\_COLOUT4\_PA3   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x3) |
| --- |

## [◆ ](#a70de53b11ca989b53ec574f1d9b5a9a1)KEYSCAN\_COLOUT4\_PA4

| #define KEYSCAN\_COLOUT4\_PA4   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x4) |
| --- |

## [◆ ](#abf320f9d9237887c80804d4cae80be1f)KEYSCAN\_COLOUT4\_PA5

| #define KEYSCAN\_COLOUT4\_PA5   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x5) |
| --- |

## [◆ ](#a932ab9b651ef171d8770ee91f755f310)KEYSCAN\_COLOUT4\_PA6

| #define KEYSCAN\_COLOUT4\_PA6   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x6) |
| --- |

## [◆ ](#ac78d413a4efb4d86e2a50e7b72be4d26)KEYSCAN\_COLOUT4\_PA7

| #define KEYSCAN\_COLOUT4\_PA7   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x7) |
| --- |

## [◆ ](#af6b8b35c91aa7f7803bbcc5fb075727f)KEYSCAN\_COLOUT4\_PA8

| #define KEYSCAN\_COLOUT4\_PA8   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x8) |
| --- |

## [◆ ](#a8f3aac47e0f1f915f1c5b23a4c27dd2f)KEYSCAN\_COLOUT4\_PA9

| #define KEYSCAN\_COLOUT4\_PA9   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x0, 0x9) |
| --- |

## [◆ ](#a11987f6b9850ca37854294dcb905dc7c)KEYSCAN\_COLOUT4\_PB0

| #define KEYSCAN\_COLOUT4\_PB0   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x1, 0x0) |
| --- |

## [◆ ](#ae40bf07cf4c0df647eaae88e5be92524)KEYSCAN\_COLOUT4\_PB1

| #define KEYSCAN\_COLOUT4\_PB1   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x1, 0x1) |
| --- |

## [◆ ](#a2676eb0f189c13d62f6f3a47ff91460f)KEYSCAN\_COLOUT4\_PB2

| #define KEYSCAN\_COLOUT4\_PB2   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x1, 0x2) |
| --- |

## [◆ ](#a10623259e7aab23eed36d024ec2db492)KEYSCAN\_COLOUT4\_PB3

| #define KEYSCAN\_COLOUT4\_PB3   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x1, 0x3) |
| --- |

## [◆ ](#a90de9bcd11d5e22753492defd2d466eb)KEYSCAN\_COLOUT4\_PB4

| #define KEYSCAN\_COLOUT4\_PB4   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x1, 0x4) |
| --- |

## [◆ ](#a79fb2103fd195dc0acc79f4a781fcc35)KEYSCAN\_COLOUT4\_PB5

| #define KEYSCAN\_COLOUT4\_PB5   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x1, 0x5) |
| --- |

## [◆ ](#a8e70447c091ba747df500037c1730443)KEYSCAN\_COLOUT4\_PC0

| #define KEYSCAN\_COLOUT4\_PC0   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x0) |
| --- |

## [◆ ](#ad2b86c50f1170c709965981baccf6f8c)KEYSCAN\_COLOUT4\_PC1

| #define KEYSCAN\_COLOUT4\_PC1   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x1) |
| --- |

## [◆ ](#a06ecfd3d8a4d8e790eba4b1e75893d5d)KEYSCAN\_COLOUT4\_PC2

| #define KEYSCAN\_COLOUT4\_PC2   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x2) |
| --- |

## [◆ ](#a72427d0eead38a6b0546d0f2b120b719)KEYSCAN\_COLOUT4\_PC3

| #define KEYSCAN\_COLOUT4\_PC3   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x3) |
| --- |

## [◆ ](#a2b41f30aafad5a904e4f9ac0224154c9)KEYSCAN\_COLOUT4\_PC4

| #define KEYSCAN\_COLOUT4\_PC4   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x4) |
| --- |

## [◆ ](#ac0193ef4b3165a422579786f2bdd3d56)KEYSCAN\_COLOUT4\_PC5

| #define KEYSCAN\_COLOUT4\_PC5   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x5) |
| --- |

## [◆ ](#a0516f93e064fe7240ea8acad8181dfab)KEYSCAN\_COLOUT4\_PC6

| #define KEYSCAN\_COLOUT4\_PC6   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x6) |
| --- |

## [◆ ](#a48854348d92e762a887528e2dad40ea3)KEYSCAN\_COLOUT4\_PC7

| #define KEYSCAN\_COLOUT4\_PC7   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x7) |
| --- |

## [◆ ](#a7fea996f4cb54dc4aa532ebc826f93c2)KEYSCAN\_COLOUT4\_PC8

| #define KEYSCAN\_COLOUT4\_PC8   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x8) |
| --- |

## [◆ ](#a6fb8ab1beade87394c928d16c7c82d74)KEYSCAN\_COLOUT4\_PC9

| #define KEYSCAN\_COLOUT4\_PC9   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x2, 0x9) |
| --- |

## [◆ ](#a11dbe6c22a64853ebf77d63a39559686)KEYSCAN\_COLOUT4\_PD0

| #define KEYSCAN\_COLOUT4\_PD0   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x3, 0x0) |
| --- |

## [◆ ](#ac404c0c86e9854cd160c23f7fd5064c9)KEYSCAN\_COLOUT4\_PD1

| #define KEYSCAN\_COLOUT4\_PD1   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x3, 0x1) |
| --- |

## [◆ ](#afabf35d508aa714ebbb349504b8eda37)KEYSCAN\_COLOUT4\_PD2

| #define KEYSCAN\_COLOUT4\_PD2   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x3, 0x2) |
| --- |

## [◆ ](#a18755054cce4073be50b10dd0ca6eb21)KEYSCAN\_COLOUT4\_PD3

| #define KEYSCAN\_COLOUT4\_PD3   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x3, 0x3) |
| --- |

## [◆ ](#ac5e1a649a0ae05c780de197299fbb7dd)KEYSCAN\_COLOUT4\_PD4

| #define KEYSCAN\_COLOUT4\_PD4   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x3, 0x4) |
| --- |

## [◆ ](#ae6a0a3db5f80b4b0cac57444f163a585)KEYSCAN\_COLOUT4\_PD5

| #define KEYSCAN\_COLOUT4\_PD5   [SILABS\_DBUS\_KEYSCAN\_COLOUT4](#a05d4eb11707be913f27fecd9b1cac85c)(0x3, 0x5) |
| --- |

## [◆ ](#a445da127fb2362507a565aed11eeeba0)KEYSCAN\_COLOUT5\_PA0

| #define KEYSCAN\_COLOUT5\_PA0   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x0) |
| --- |

## [◆ ](#a3bc9a083d15fef5d3d79cda126d08906)KEYSCAN\_COLOUT5\_PA1

| #define KEYSCAN\_COLOUT5\_PA1   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x1) |
| --- |

## [◆ ](#a6811845fa1e873338d55c312688bab86)KEYSCAN\_COLOUT5\_PA2

| #define KEYSCAN\_COLOUT5\_PA2   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x2) |
| --- |

## [◆ ](#a6d6e8462f2dded71fd2beda3d8a4dde3)KEYSCAN\_COLOUT5\_PA3

| #define KEYSCAN\_COLOUT5\_PA3   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x3) |
| --- |

## [◆ ](#a5b28158eeda0bc1d96457e7894a5ffdc)KEYSCAN\_COLOUT5\_PA4

| #define KEYSCAN\_COLOUT5\_PA4   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x4) |
| --- |

## [◆ ](#a249cadf259b05e1504108c51dc17c25a)KEYSCAN\_COLOUT5\_PA5

| #define KEYSCAN\_COLOUT5\_PA5   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x5) |
| --- |

## [◆ ](#a7514bf4b2ef744b83d1ed2722fabf94e)KEYSCAN\_COLOUT5\_PA6

| #define KEYSCAN\_COLOUT5\_PA6   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x6) |
| --- |

## [◆ ](#aa2290f8cad94843957d0931d71eb6ce1)KEYSCAN\_COLOUT5\_PA7

| #define KEYSCAN\_COLOUT5\_PA7   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x7) |
| --- |

## [◆ ](#a9b17f8d47d3a9eb28c822f1b6a776435)KEYSCAN\_COLOUT5\_PA8

| #define KEYSCAN\_COLOUT5\_PA8   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x8) |
| --- |

## [◆ ](#a868d0142dd4a0c150b2274abf7aa6ff0)KEYSCAN\_COLOUT5\_PA9

| #define KEYSCAN\_COLOUT5\_PA9   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x0, 0x9) |
| --- |

## [◆ ](#a66892269bf6807fee61920130c800600)KEYSCAN\_COLOUT5\_PB0

| #define KEYSCAN\_COLOUT5\_PB0   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x1, 0x0) |
| --- |

## [◆ ](#a4d733004f15bf6d3ff23ec47bd9768ad)KEYSCAN\_COLOUT5\_PB1

| #define KEYSCAN\_COLOUT5\_PB1   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x1, 0x1) |
| --- |

## [◆ ](#a2003238f3634bcd0f67592d60d7fcaef)KEYSCAN\_COLOUT5\_PB2

| #define KEYSCAN\_COLOUT5\_PB2   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x1, 0x2) |
| --- |

## [◆ ](#a4b05943cd8dc5b50c74393a9fb044461)KEYSCAN\_COLOUT5\_PB3

| #define KEYSCAN\_COLOUT5\_PB3   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x1, 0x3) |
| --- |

## [◆ ](#aaef1601c48afde7ae05971f482b5c7c1)KEYSCAN\_COLOUT5\_PB4

| #define KEYSCAN\_COLOUT5\_PB4   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x1, 0x4) |
| --- |

## [◆ ](#aed0250bb5950ddd89f943fa8e80389ee)KEYSCAN\_COLOUT5\_PB5

| #define KEYSCAN\_COLOUT5\_PB5   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x1, 0x5) |
| --- |

## [◆ ](#acfac4f2b95912c513b1b284c31a0b0f6)KEYSCAN\_COLOUT5\_PC0

| #define KEYSCAN\_COLOUT5\_PC0   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x0) |
| --- |

## [◆ ](#ae70fbb4c97527a55a721e88de8b980fb)KEYSCAN\_COLOUT5\_PC1

| #define KEYSCAN\_COLOUT5\_PC1   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x1) |
| --- |

## [◆ ](#a1c779495a8b3cfc1ddf6061be7291e79)KEYSCAN\_COLOUT5\_PC2

| #define KEYSCAN\_COLOUT5\_PC2   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x2) |
| --- |

## [◆ ](#a33988f610eb6e5c070f902b7b873da51)KEYSCAN\_COLOUT5\_PC3

| #define KEYSCAN\_COLOUT5\_PC3   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x3) |
| --- |

## [◆ ](#abde9e625846e6e01c1757da031fcf714)KEYSCAN\_COLOUT5\_PC4

| #define KEYSCAN\_COLOUT5\_PC4   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x4) |
| --- |

## [◆ ](#a8947e96addd21760d8231582af772151)KEYSCAN\_COLOUT5\_PC5

| #define KEYSCAN\_COLOUT5\_PC5   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x5) |
| --- |

## [◆ ](#abd7fb9e69d19fb382fed755eee87ffda)KEYSCAN\_COLOUT5\_PC6

| #define KEYSCAN\_COLOUT5\_PC6   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x6) |
| --- |

## [◆ ](#a5e82bc559b41f162f3919d791981e66e)KEYSCAN\_COLOUT5\_PC7

| #define KEYSCAN\_COLOUT5\_PC7   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x7) |
| --- |

## [◆ ](#a6e14479a3cbb0e5b423b9db48d231d2d)KEYSCAN\_COLOUT5\_PC8

| #define KEYSCAN\_COLOUT5\_PC8   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x8) |
| --- |

## [◆ ](#a6a73c599f9728431a35756c4986654f5)KEYSCAN\_COLOUT5\_PC9

| #define KEYSCAN\_COLOUT5\_PC9   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x2, 0x9) |
| --- |

## [◆ ](#a34b02d2d2ffe5c3048f473115713515d)KEYSCAN\_COLOUT5\_PD0

| #define KEYSCAN\_COLOUT5\_PD0   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x3, 0x0) |
| --- |

## [◆ ](#a5199171ce63cf8ca7675772b2321fad3)KEYSCAN\_COLOUT5\_PD1

| #define KEYSCAN\_COLOUT5\_PD1   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x3, 0x1) |
| --- |

## [◆ ](#a540317a1bb80f621e72a08cd85fe41d0)KEYSCAN\_COLOUT5\_PD2

| #define KEYSCAN\_COLOUT5\_PD2   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x3, 0x2) |
| --- |

## [◆ ](#a77d7ba8e76bdc6d526ca3f69717ce51a)KEYSCAN\_COLOUT5\_PD3

| #define KEYSCAN\_COLOUT5\_PD3   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x3, 0x3) |
| --- |

## [◆ ](#a8ba90046cd580e02a7c13baa8266fe22)KEYSCAN\_COLOUT5\_PD4

| #define KEYSCAN\_COLOUT5\_PD4   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x3, 0x4) |
| --- |

## [◆ ](#a877555ebc2ee02d897d9e1fb31b1956e)KEYSCAN\_COLOUT5\_PD5

| #define KEYSCAN\_COLOUT5\_PD5   [SILABS\_DBUS\_KEYSCAN\_COLOUT5](#aeee19264cf4f46f09af1ffb8f168c81d)(0x3, 0x5) |
| --- |

## [◆ ](#a1015bc110150ce9a8dfde554c231ac94)KEYSCAN\_COLOUT6\_PA0

| #define KEYSCAN\_COLOUT6\_PA0   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x0) |
| --- |

## [◆ ](#a164d2c40932914047b57116fb6fd5a03)KEYSCAN\_COLOUT6\_PA1

| #define KEYSCAN\_COLOUT6\_PA1   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x1) |
| --- |

## [◆ ](#a3377f0ae72a775e8703f49ff9a3cffe9)KEYSCAN\_COLOUT6\_PA2

| #define KEYSCAN\_COLOUT6\_PA2   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x2) |
| --- |

## [◆ ](#a9728b9714b9f6f6c457dd8cc7336ebed)KEYSCAN\_COLOUT6\_PA3

| #define KEYSCAN\_COLOUT6\_PA3   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x3) |
| --- |

## [◆ ](#ab1205ba33526d8fdd22c90965c200ab2)KEYSCAN\_COLOUT6\_PA4

| #define KEYSCAN\_COLOUT6\_PA4   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x4) |
| --- |

## [◆ ](#ae982f5aaa9101ac5615a4561b8270658)KEYSCAN\_COLOUT6\_PA5

| #define KEYSCAN\_COLOUT6\_PA5   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x5) |
| --- |

## [◆ ](#adfe14ef51e16649cff7d9a364d33d54e)KEYSCAN\_COLOUT6\_PA6

| #define KEYSCAN\_COLOUT6\_PA6   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x6) |
| --- |

## [◆ ](#a40a7388734dc2397993054adf8eb43f1)KEYSCAN\_COLOUT6\_PA7

| #define KEYSCAN\_COLOUT6\_PA7   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x7) |
| --- |

## [◆ ](#ad246eb368b6e2db727ce989204da7eb0)KEYSCAN\_COLOUT6\_PA8

| #define KEYSCAN\_COLOUT6\_PA8   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x8) |
| --- |

## [◆ ](#a002826f7446b3b832ba04c7adf8a937a)KEYSCAN\_COLOUT6\_PA9

| #define KEYSCAN\_COLOUT6\_PA9   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x0, 0x9) |
| --- |

## [◆ ](#a976bec944ecaf0cfade1d67ddd176ee0)KEYSCAN\_COLOUT6\_PB0

| #define KEYSCAN\_COLOUT6\_PB0   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x1, 0x0) |
| --- |

## [◆ ](#ad18b480857c0b6e51cdc700e4886fce5)KEYSCAN\_COLOUT6\_PB1

| #define KEYSCAN\_COLOUT6\_PB1   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x1, 0x1) |
| --- |

## [◆ ](#ada236816df191c833373e4360763a768)KEYSCAN\_COLOUT6\_PB2

| #define KEYSCAN\_COLOUT6\_PB2   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x1, 0x2) |
| --- |

## [◆ ](#ae61862815dad0d58bdfbdadaec43852d)KEYSCAN\_COLOUT6\_PB3

| #define KEYSCAN\_COLOUT6\_PB3   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x1, 0x3) |
| --- |

## [◆ ](#a8136ee96abebd75e9ae9c182ddfc1d69)KEYSCAN\_COLOUT6\_PB4

| #define KEYSCAN\_COLOUT6\_PB4   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x1, 0x4) |
| --- |

## [◆ ](#ab519393460d3afee34c2c296ecdaa728)KEYSCAN\_COLOUT6\_PB5

| #define KEYSCAN\_COLOUT6\_PB5   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x1, 0x5) |
| --- |

## [◆ ](#a6ca408b5dbea309195594e1eaabd7a39)KEYSCAN\_COLOUT6\_PC0

| #define KEYSCAN\_COLOUT6\_PC0   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x0) |
| --- |

## [◆ ](#ab8d2c741cf89baa479ffd00b02f95b1e)KEYSCAN\_COLOUT6\_PC1

| #define KEYSCAN\_COLOUT6\_PC1   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x1) |
| --- |

## [◆ ](#af74ca2782fbc8ace8ac7ab3df032333f)KEYSCAN\_COLOUT6\_PC2

| #define KEYSCAN\_COLOUT6\_PC2   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x2) |
| --- |

## [◆ ](#ae664ac159cd0225a2940c9bef2a8fd48)KEYSCAN\_COLOUT6\_PC3

| #define KEYSCAN\_COLOUT6\_PC3   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x3) |
| --- |

## [◆ ](#a5ac714fbdb09307163c0bf5b8618e48e)KEYSCAN\_COLOUT6\_PC4

| #define KEYSCAN\_COLOUT6\_PC4   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x4) |
| --- |

## [◆ ](#a804aff870bf653bd128578352a599fe7)KEYSCAN\_COLOUT6\_PC5

| #define KEYSCAN\_COLOUT6\_PC5   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x5) |
| --- |

## [◆ ](#a1321d5994882b85ac825fcbe36ce0f17)KEYSCAN\_COLOUT6\_PC6

| #define KEYSCAN\_COLOUT6\_PC6   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x6) |
| --- |

## [◆ ](#a6e2015159c39cb1646318d8d63fd071c)KEYSCAN\_COLOUT6\_PC7

| #define KEYSCAN\_COLOUT6\_PC7   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x7) |
| --- |

## [◆ ](#a8f6dd892722632a45e052dd51c2fa6f3)KEYSCAN\_COLOUT6\_PC8

| #define KEYSCAN\_COLOUT6\_PC8   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x8) |
| --- |

## [◆ ](#a45bfc62ed3b18cb0f85fc4cadab6281a)KEYSCAN\_COLOUT6\_PC9

| #define KEYSCAN\_COLOUT6\_PC9   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x2, 0x9) |
| --- |

## [◆ ](#ad7e7da0911664b6a29c17af882647fdf)KEYSCAN\_COLOUT6\_PD0

| #define KEYSCAN\_COLOUT6\_PD0   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x3, 0x0) |
| --- |

## [◆ ](#ac205720916fc5f4466f6bf94d7df9ff4)KEYSCAN\_COLOUT6\_PD1

| #define KEYSCAN\_COLOUT6\_PD1   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x3, 0x1) |
| --- |

## [◆ ](#a1f90116aed6f2bbb6d49c7683acd525c)KEYSCAN\_COLOUT6\_PD2

| #define KEYSCAN\_COLOUT6\_PD2   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x3, 0x2) |
| --- |

## [◆ ](#a76381728fb3c51794708f0235d6726dd)KEYSCAN\_COLOUT6\_PD3

| #define KEYSCAN\_COLOUT6\_PD3   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x3, 0x3) |
| --- |

## [◆ ](#a86c12dd4b7435a5151cf598369356229)KEYSCAN\_COLOUT6\_PD4

| #define KEYSCAN\_COLOUT6\_PD4   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x3, 0x4) |
| --- |

## [◆ ](#a69d7a1f11082904af7c6a94e309d30cc)KEYSCAN\_COLOUT6\_PD5

| #define KEYSCAN\_COLOUT6\_PD5   [SILABS\_DBUS\_KEYSCAN\_COLOUT6](#afdfdf17591fe03c49b32ee3432529e3b)(0x3, 0x5) |
| --- |

## [◆ ](#a2c2077051cec44334ca9f24f01d9c30f)KEYSCAN\_COLOUT7\_PA0

| #define KEYSCAN\_COLOUT7\_PA0   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x0) |
| --- |

## [◆ ](#a738421f5a4f4b1eb477303acdcebd14c)KEYSCAN\_COLOUT7\_PA1

| #define KEYSCAN\_COLOUT7\_PA1   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x1) |
| --- |

## [◆ ](#aebf2a80a6a5dde233b36a8fb8d579911)KEYSCAN\_COLOUT7\_PA2

| #define KEYSCAN\_COLOUT7\_PA2   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x2) |
| --- |

## [◆ ](#a466d3fc5a3bc404fbfa550e019cc62d7)KEYSCAN\_COLOUT7\_PA3

| #define KEYSCAN\_COLOUT7\_PA3   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x3) |
| --- |

## [◆ ](#a39df7281dab8a01ef199f28f832e6e87)KEYSCAN\_COLOUT7\_PA4

| #define KEYSCAN\_COLOUT7\_PA4   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x4) |
| --- |

## [◆ ](#a3379e32f32ca7e4690965d6cf5246584)KEYSCAN\_COLOUT7\_PA5

| #define KEYSCAN\_COLOUT7\_PA5   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x5) |
| --- |

## [◆ ](#a762c113dc69ca9a54c06951b0afec2ad)KEYSCAN\_COLOUT7\_PA6

| #define KEYSCAN\_COLOUT7\_PA6   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x6) |
| --- |

## [◆ ](#a4dce38f25f57d77f353b825a347218d7)KEYSCAN\_COLOUT7\_PA7

| #define KEYSCAN\_COLOUT7\_PA7   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x7) |
| --- |

## [◆ ](#a5d0ebe96584d8a404c919b0384048712)KEYSCAN\_COLOUT7\_PA8

| #define KEYSCAN\_COLOUT7\_PA8   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x8) |
| --- |

## [◆ ](#a2cd7ce9bec05887045f6fb332eceb01f)KEYSCAN\_COLOUT7\_PA9

| #define KEYSCAN\_COLOUT7\_PA9   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x0, 0x9) |
| --- |

## [◆ ](#a3a9ac7724de26dc7d7863a9c464f3b8e)KEYSCAN\_COLOUT7\_PB0

| #define KEYSCAN\_COLOUT7\_PB0   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x1, 0x0) |
| --- |

## [◆ ](#a34f6c1e9f8a112dd4dffc5a4bcd62923)KEYSCAN\_COLOUT7\_PB1

| #define KEYSCAN\_COLOUT7\_PB1   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x1, 0x1) |
| --- |

## [◆ ](#ab0e561a2c2df7cd8aac7bfb9cc28ebe5)KEYSCAN\_COLOUT7\_PB2

| #define KEYSCAN\_COLOUT7\_PB2   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x1, 0x2) |
| --- |

## [◆ ](#a82e0512ef6c164040dce7118125a0b44)KEYSCAN\_COLOUT7\_PB3

| #define KEYSCAN\_COLOUT7\_PB3   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x1, 0x3) |
| --- |

## [◆ ](#a06a9141b57439ef6a5050d49198722c3)KEYSCAN\_COLOUT7\_PB4

| #define KEYSCAN\_COLOUT7\_PB4   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x1, 0x4) |
| --- |

## [◆ ](#a3950d363f113758c76bfd2043c811733)KEYSCAN\_COLOUT7\_PB5

| #define KEYSCAN\_COLOUT7\_PB5   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x1, 0x5) |
| --- |

## [◆ ](#a1b765b491b755de95da126789fdcc5c3)KEYSCAN\_COLOUT7\_PC0

| #define KEYSCAN\_COLOUT7\_PC0   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x0) |
| --- |

## [◆ ](#aadbb6155733bed3501712a35f90cb044)KEYSCAN\_COLOUT7\_PC1

| #define KEYSCAN\_COLOUT7\_PC1   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x1) |
| --- |

## [◆ ](#a1dbb118c9b76a300bb722db3b68d6b84)KEYSCAN\_COLOUT7\_PC2

| #define KEYSCAN\_COLOUT7\_PC2   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x2) |
| --- |

## [◆ ](#aa91a9034fde73e0704eff4b4ea087f5f)KEYSCAN\_COLOUT7\_PC3

| #define KEYSCAN\_COLOUT7\_PC3   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x3) |
| --- |

## [◆ ](#ab2f6a222ecb44740a2bc5d0c9910df35)KEYSCAN\_COLOUT7\_PC4

| #define KEYSCAN\_COLOUT7\_PC4   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x4) |
| --- |

## [◆ ](#a1a0cb3350162aab843868bf8acb27f57)KEYSCAN\_COLOUT7\_PC5

| #define KEYSCAN\_COLOUT7\_PC5   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x5) |
| --- |

## [◆ ](#a4e05623227d433e89b2d21a2de694447)KEYSCAN\_COLOUT7\_PC6

| #define KEYSCAN\_COLOUT7\_PC6   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x6) |
| --- |

## [◆ ](#a3bc3ec5f42c0c02b4fe33409a951ae00)KEYSCAN\_COLOUT7\_PC7

| #define KEYSCAN\_COLOUT7\_PC7   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x7) |
| --- |

## [◆ ](#a7a40074edaaa3b77e7a4bc7af3631e4c)KEYSCAN\_COLOUT7\_PC8

| #define KEYSCAN\_COLOUT7\_PC8   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x8) |
| --- |

## [◆ ](#af8874c8534bb7195961524edd4a9ec58)KEYSCAN\_COLOUT7\_PC9

| #define KEYSCAN\_COLOUT7\_PC9   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x2, 0x9) |
| --- |

## [◆ ](#a5d9b11b5cc466f175592dbde1721f769)KEYSCAN\_COLOUT7\_PD0

| #define KEYSCAN\_COLOUT7\_PD0   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x3, 0x0) |
| --- |

## [◆ ](#a250d43085e7ae24a1b142db5d4baf918)KEYSCAN\_COLOUT7\_PD1

| #define KEYSCAN\_COLOUT7\_PD1   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x3, 0x1) |
| --- |

## [◆ ](#adc18708ffe2821fa512de99ea16713af)KEYSCAN\_COLOUT7\_PD2

| #define KEYSCAN\_COLOUT7\_PD2   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x3, 0x2) |
| --- |

## [◆ ](#a0e75e731910d6a5e80f9ff1be66f729d)KEYSCAN\_COLOUT7\_PD3

| #define KEYSCAN\_COLOUT7\_PD3   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x3, 0x3) |
| --- |

## [◆ ](#a440d923db1ccbb88b729d6f903cf6f06)KEYSCAN\_COLOUT7\_PD4

| #define KEYSCAN\_COLOUT7\_PD4   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x3, 0x4) |
| --- |

## [◆ ](#a829fcc9a471a8b860f6b572b43aad369)KEYSCAN\_COLOUT7\_PD5

| #define KEYSCAN\_COLOUT7\_PD5   [SILABS\_DBUS\_KEYSCAN\_COLOUT7](#a3c331cf1aa193f1a80192cc460229d95)(0x3, 0x5) |
| --- |

## [◆ ](#a67991dff6fcb794562cc961b7be4ab19)KEYSCAN\_ROWSENSE0\_PA0

| #define KEYSCAN\_ROWSENSE0\_PA0   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x0) |
| --- |

## [◆ ](#a339a54f1955567a0bce2aebee0b943a9)KEYSCAN\_ROWSENSE0\_PA1

| #define KEYSCAN\_ROWSENSE0\_PA1   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x1) |
| --- |

## [◆ ](#a4fdc77d680dfc73289c4ad497ce067f7)KEYSCAN\_ROWSENSE0\_PA2

| #define KEYSCAN\_ROWSENSE0\_PA2   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x2) |
| --- |

## [◆ ](#ad1e2f6e6b2507f0e3c047ab5384ee6cd)KEYSCAN\_ROWSENSE0\_PA3

| #define KEYSCAN\_ROWSENSE0\_PA3   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x3) |
| --- |

## [◆ ](#a31b40c144d14649874a70e1198077cb9)KEYSCAN\_ROWSENSE0\_PA4

| #define KEYSCAN\_ROWSENSE0\_PA4   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x4) |
| --- |

## [◆ ](#a42919482bfc6aca98335cd5ca5133bcf)KEYSCAN\_ROWSENSE0\_PA5

| #define KEYSCAN\_ROWSENSE0\_PA5   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x5) |
| --- |

## [◆ ](#a91c93b98d8018df61c6e31d7c4fde9d2)KEYSCAN\_ROWSENSE0\_PA6

| #define KEYSCAN\_ROWSENSE0\_PA6   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x6) |
| --- |

## [◆ ](#a25157ca32ecace6d08fbcb09b0d8e13f)KEYSCAN\_ROWSENSE0\_PA7

| #define KEYSCAN\_ROWSENSE0\_PA7   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x7) |
| --- |

## [◆ ](#ad01b8f98c3228b100d9806d01d3a72f7)KEYSCAN\_ROWSENSE0\_PA8

| #define KEYSCAN\_ROWSENSE0\_PA8   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x8) |
| --- |

## [◆ ](#a0f52c8016ffe4bc9d849c241f7b49eba)KEYSCAN\_ROWSENSE0\_PA9

| #define KEYSCAN\_ROWSENSE0\_PA9   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x0, 0x9) |
| --- |

## [◆ ](#afabf7d00424badf10c342d4f4eb56f9f)KEYSCAN\_ROWSENSE0\_PB0

| #define KEYSCAN\_ROWSENSE0\_PB0   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x1, 0x0) |
| --- |

## [◆ ](#abde18a3ba51a69a81c268075ad8eb0fc)KEYSCAN\_ROWSENSE0\_PB1

| #define KEYSCAN\_ROWSENSE0\_PB1   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x1, 0x1) |
| --- |

## [◆ ](#a24f463069c92d9fae0b58beb2ad5fc35)KEYSCAN\_ROWSENSE0\_PB2

| #define KEYSCAN\_ROWSENSE0\_PB2   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x1, 0x2) |
| --- |

## [◆ ](#ad1b979a16fcf92f08f6aa0836be8f040)KEYSCAN\_ROWSENSE0\_PB3

| #define KEYSCAN\_ROWSENSE0\_PB3   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x1, 0x3) |
| --- |

## [◆ ](#a2f5b585a89277c6571be738f8aa3f034)KEYSCAN\_ROWSENSE0\_PB4

| #define KEYSCAN\_ROWSENSE0\_PB4   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x1, 0x4) |
| --- |

## [◆ ](#a1af0700d0fe6e65566675861682919a2)KEYSCAN\_ROWSENSE0\_PB5

| #define KEYSCAN\_ROWSENSE0\_PB5   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE0](#a2015d499c18fa403414add3e314f10cc)(0x1, 0x5) |
| --- |

## [◆ ](#a2b99dc18c2ea2ca460ac90aed73caba5)KEYSCAN\_ROWSENSE1\_PA0

| #define KEYSCAN\_ROWSENSE1\_PA0   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x0) |
| --- |

## [◆ ](#ab043e248ed5d80ec70ee62fbabd53447)KEYSCAN\_ROWSENSE1\_PA1

| #define KEYSCAN\_ROWSENSE1\_PA1   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x1) |
| --- |

## [◆ ](#a4cbe09e947c26123a341e9402706a1cb)KEYSCAN\_ROWSENSE1\_PA2

| #define KEYSCAN\_ROWSENSE1\_PA2   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x2) |
| --- |

## [◆ ](#a62bdd05aae2bca8be772fec9864e6b68)KEYSCAN\_ROWSENSE1\_PA3

| #define KEYSCAN\_ROWSENSE1\_PA3   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x3) |
| --- |

## [◆ ](#afd4f5e56d0b5e6dc7f134407181e65a8)KEYSCAN\_ROWSENSE1\_PA4

| #define KEYSCAN\_ROWSENSE1\_PA4   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x4) |
| --- |

## [◆ ](#a8eafb57db7cd8eb914ddd261082a557d)KEYSCAN\_ROWSENSE1\_PA5

| #define KEYSCAN\_ROWSENSE1\_PA5   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x5) |
| --- |

## [◆ ](#a547b11aec9663d60bc655e73f0e36a23)KEYSCAN\_ROWSENSE1\_PA6

| #define KEYSCAN\_ROWSENSE1\_PA6   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x6) |
| --- |

## [◆ ](#ae32c46f38591fd583715cdb966917afd)KEYSCAN\_ROWSENSE1\_PA7

| #define KEYSCAN\_ROWSENSE1\_PA7   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x7) |
| --- |

## [◆ ](#a81633497cd9ea043c2d0edf1433e1f8a)KEYSCAN\_ROWSENSE1\_PA8

| #define KEYSCAN\_ROWSENSE1\_PA8   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x8) |
| --- |

## [◆ ](#a77b62ab5186da780fbcc04b6493275ee)KEYSCAN\_ROWSENSE1\_PA9

| #define KEYSCAN\_ROWSENSE1\_PA9   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x0, 0x9) |
| --- |

## [◆ ](#a91714fa64b28935dfc304a9c96ee6463)KEYSCAN\_ROWSENSE1\_PB0

| #define KEYSCAN\_ROWSENSE1\_PB0   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x1, 0x0) |
| --- |

## [◆ ](#a19666eb8fad7afe29304d989d27d7900)KEYSCAN\_ROWSENSE1\_PB1

| #define KEYSCAN\_ROWSENSE1\_PB1   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x1, 0x1) |
| --- |

## [◆ ](#a3e98b13c576d22efd869ed96b980d2fc)KEYSCAN\_ROWSENSE1\_PB2

| #define KEYSCAN\_ROWSENSE1\_PB2   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x1, 0x2) |
| --- |

## [◆ ](#a8d8ef254fe361607f0f03213242cc935)KEYSCAN\_ROWSENSE1\_PB3

| #define KEYSCAN\_ROWSENSE1\_PB3   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x1, 0x3) |
| --- |

## [◆ ](#a1d20159431da0732584309cca0c3bb21)KEYSCAN\_ROWSENSE1\_PB4

| #define KEYSCAN\_ROWSENSE1\_PB4   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x1, 0x4) |
| --- |

## [◆ ](#ae117dc227927f05c57fcf3cb4e36e135)KEYSCAN\_ROWSENSE1\_PB5

| #define KEYSCAN\_ROWSENSE1\_PB5   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE1](#a9add4d6cdd61c94ac66169eb15dfed48)(0x1, 0x5) |
| --- |

## [◆ ](#a81797c1a41b453e99c904d13abc1dfaa)KEYSCAN\_ROWSENSE2\_PA0

| #define KEYSCAN\_ROWSENSE2\_PA0   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x0) |
| --- |

## [◆ ](#a827162fd46a929d469e58991add10d87)KEYSCAN\_ROWSENSE2\_PA1

| #define KEYSCAN\_ROWSENSE2\_PA1   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x1) |
| --- |

## [◆ ](#ada62ed625f76f6f4ba7ef03aeed09afc)KEYSCAN\_ROWSENSE2\_PA2

| #define KEYSCAN\_ROWSENSE2\_PA2   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x2) |
| --- |

## [◆ ](#a5a4144e1842c452a99d055c62d56df64)KEYSCAN\_ROWSENSE2\_PA3

| #define KEYSCAN\_ROWSENSE2\_PA3   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x3) |
| --- |

## [◆ ](#a648c8d982b6e31a74bb4018f38cdd4a0)KEYSCAN\_ROWSENSE2\_PA4

| #define KEYSCAN\_ROWSENSE2\_PA4   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x4) |
| --- |

## [◆ ](#ada178e730cde0696ebeda57915abfe69)KEYSCAN\_ROWSENSE2\_PA5

| #define KEYSCAN\_ROWSENSE2\_PA5   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x5) |
| --- |

## [◆ ](#a6449748c9123fdc703993d98149bb127)KEYSCAN\_ROWSENSE2\_PA6

| #define KEYSCAN\_ROWSENSE2\_PA6   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x6) |
| --- |

## [◆ ](#ab091b88a0fe636a1f1be4fbf3877083a)KEYSCAN\_ROWSENSE2\_PA7

| #define KEYSCAN\_ROWSENSE2\_PA7   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x7) |
| --- |

## [◆ ](#a591262d395412f79aca0ca3c33bb71a6)KEYSCAN\_ROWSENSE2\_PA8

| #define KEYSCAN\_ROWSENSE2\_PA8   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x8) |
| --- |

## [◆ ](#a0000c7bde424893f75fa88a2fa46618c)KEYSCAN\_ROWSENSE2\_PA9

| #define KEYSCAN\_ROWSENSE2\_PA9   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x0, 0x9) |
| --- |

## [◆ ](#ac324e44a5781c26c7b5b8295639bddb3)KEYSCAN\_ROWSENSE2\_PB0

| #define KEYSCAN\_ROWSENSE2\_PB0   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x1, 0x0) |
| --- |

## [◆ ](#a5bcc10bfaf92f92fbf63343979758be8)KEYSCAN\_ROWSENSE2\_PB1

| #define KEYSCAN\_ROWSENSE2\_PB1   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x1, 0x1) |
| --- |

## [◆ ](#a565524f72fc269654c3f21ad55d22984)KEYSCAN\_ROWSENSE2\_PB2

| #define KEYSCAN\_ROWSENSE2\_PB2   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x1, 0x2) |
| --- |

## [◆ ](#aa87f2b0f63628e540d7cab6819f23b1c)KEYSCAN\_ROWSENSE2\_PB3

| #define KEYSCAN\_ROWSENSE2\_PB3   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x1, 0x3) |
| --- |

## [◆ ](#a126fbb54622a6f9145314e37ac40faf0)KEYSCAN\_ROWSENSE2\_PB4

| #define KEYSCAN\_ROWSENSE2\_PB4   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x1, 0x4) |
| --- |

## [◆ ](#a2b0719a6d0116cca241bdcfc55865b6f)KEYSCAN\_ROWSENSE2\_PB5

| #define KEYSCAN\_ROWSENSE2\_PB5   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE2](#a5666436f80195c2c336196fc688ee2dd)(0x1, 0x5) |
| --- |

## [◆ ](#aea8e269e57c0462a3ef0dced0ad01379)KEYSCAN\_ROWSENSE3\_PA0

| #define KEYSCAN\_ROWSENSE3\_PA0   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x0) |
| --- |

## [◆ ](#a1a1e4fba3105aaccdd5eb39b6cb676ca)KEYSCAN\_ROWSENSE3\_PA1

| #define KEYSCAN\_ROWSENSE3\_PA1   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x1) |
| --- |

## [◆ ](#a4ce45d5aa7155da9b41dfc1aa1cd8bb3)KEYSCAN\_ROWSENSE3\_PA2

| #define KEYSCAN\_ROWSENSE3\_PA2   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x2) |
| --- |

## [◆ ](#a2eb6f87d5342f841258d59b95b1d7549)KEYSCAN\_ROWSENSE3\_PA3

| #define KEYSCAN\_ROWSENSE3\_PA3   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x3) |
| --- |

## [◆ ](#a52730c327d1243f617e65778fe6a1cb5)KEYSCAN\_ROWSENSE3\_PA4

| #define KEYSCAN\_ROWSENSE3\_PA4   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x4) |
| --- |

## [◆ ](#a620eb41deb110f6f7e20ff5800fb1b98)KEYSCAN\_ROWSENSE3\_PA5

| #define KEYSCAN\_ROWSENSE3\_PA5   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x5) |
| --- |

## [◆ ](#a3d03dfd87e53036d8ed9b3cedf9557d1)KEYSCAN\_ROWSENSE3\_PA6

| #define KEYSCAN\_ROWSENSE3\_PA6   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x6) |
| --- |

## [◆ ](#a5d9a8c0a94a153e54ce5e9f558d4f1d4)KEYSCAN\_ROWSENSE3\_PA7

| #define KEYSCAN\_ROWSENSE3\_PA7   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x7) |
| --- |

## [◆ ](#adc003516a88f3beac0f3246f120f7464)KEYSCAN\_ROWSENSE3\_PA8

| #define KEYSCAN\_ROWSENSE3\_PA8   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x8) |
| --- |

## [◆ ](#a128c9d56c6915c58014726204d4b71ad)KEYSCAN\_ROWSENSE3\_PA9

| #define KEYSCAN\_ROWSENSE3\_PA9   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x0, 0x9) |
| --- |

## [◆ ](#a57e4c4b0f2458f74874c4c09f5c4be11)KEYSCAN\_ROWSENSE3\_PB0

| #define KEYSCAN\_ROWSENSE3\_PB0   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x1, 0x0) |
| --- |

## [◆ ](#ad72c30d85b22ed6a11214b3fd4d93fb4)KEYSCAN\_ROWSENSE3\_PB1

| #define KEYSCAN\_ROWSENSE3\_PB1   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x1, 0x1) |
| --- |

## [◆ ](#a546c198566ccf3c91b2fc8aa64fb2443)KEYSCAN\_ROWSENSE3\_PB2

| #define KEYSCAN\_ROWSENSE3\_PB2   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x1, 0x2) |
| --- |

## [◆ ](#acdeb49a1b6cd15f10bf5b52a87b45d01)KEYSCAN\_ROWSENSE3\_PB3

| #define KEYSCAN\_ROWSENSE3\_PB3   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x1, 0x3) |
| --- |

## [◆ ](#a002ab804bc35bd15b6a5faa302de29e3)KEYSCAN\_ROWSENSE3\_PB4

| #define KEYSCAN\_ROWSENSE3\_PB4   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x1, 0x4) |
| --- |

## [◆ ](#a81503561bb605822d16aadb1c6aae53d)KEYSCAN\_ROWSENSE3\_PB5

| #define KEYSCAN\_ROWSENSE3\_PB5   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE3](#a7e2c4eb1db1321a1f7810af45b5cd52c)(0x1, 0x5) |
| --- |

## [◆ ](#a148727ae1c844e126c467e53628283e1)KEYSCAN\_ROWSENSE4\_PA0

| #define KEYSCAN\_ROWSENSE4\_PA0   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x0) |
| --- |

## [◆ ](#aa9a5202d34d97778b6f24c28f4aab7ec)KEYSCAN\_ROWSENSE4\_PA1

| #define KEYSCAN\_ROWSENSE4\_PA1   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x1) |
| --- |

## [◆ ](#a4eebe03193902292d76f2e2181b69c26)KEYSCAN\_ROWSENSE4\_PA2

| #define KEYSCAN\_ROWSENSE4\_PA2   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x2) |
| --- |

## [◆ ](#a8ef724c7e7dd3c6c0e97b9bc656a0da7)KEYSCAN\_ROWSENSE4\_PA3

| #define KEYSCAN\_ROWSENSE4\_PA3   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x3) |
| --- |

## [◆ ](#ae460ceb2d0dea8dfb06a38370a837dcd)KEYSCAN\_ROWSENSE4\_PA4

| #define KEYSCAN\_ROWSENSE4\_PA4   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x4) |
| --- |

## [◆ ](#a44f7c4f24a64683e3e6f00d040deec14)KEYSCAN\_ROWSENSE4\_PA5

| #define KEYSCAN\_ROWSENSE4\_PA5   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x5) |
| --- |

## [◆ ](#a01c3835cf1c841b4caa81a7c6f62226d)KEYSCAN\_ROWSENSE4\_PA6

| #define KEYSCAN\_ROWSENSE4\_PA6   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x6) |
| --- |

## [◆ ](#a29edbb560fa201628e43798bb20d281d)KEYSCAN\_ROWSENSE4\_PA7

| #define KEYSCAN\_ROWSENSE4\_PA7   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x7) |
| --- |

## [◆ ](#a83bd1d1ca180035fa2348b0a8c577b49)KEYSCAN\_ROWSENSE4\_PA8

| #define KEYSCAN\_ROWSENSE4\_PA8   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x8) |
| --- |

## [◆ ](#ae92e0a4be0d7515915900a552d57b742)KEYSCAN\_ROWSENSE4\_PA9

| #define KEYSCAN\_ROWSENSE4\_PA9   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x0, 0x9) |
| --- |

## [◆ ](#a7af7b960d806a3e6304a2f2c04aef647)KEYSCAN\_ROWSENSE4\_PB0

| #define KEYSCAN\_ROWSENSE4\_PB0   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x1, 0x0) |
| --- |

## [◆ ](#ae62e1398b6d59687257fbfaddd65f6a5)KEYSCAN\_ROWSENSE4\_PB1

| #define KEYSCAN\_ROWSENSE4\_PB1   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x1, 0x1) |
| --- |

## [◆ ](#a29e968ac626b5fcc8b08e5d9e2f15fc0)KEYSCAN\_ROWSENSE4\_PB2

| #define KEYSCAN\_ROWSENSE4\_PB2   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x1, 0x2) |
| --- |

## [◆ ](#a822bb66e2dc40a181126aa9938a7c833)KEYSCAN\_ROWSENSE4\_PB3

| #define KEYSCAN\_ROWSENSE4\_PB3   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x1, 0x3) |
| --- |

## [◆ ](#a7eb3f3fcc2993908e32cb4fa2250b19d)KEYSCAN\_ROWSENSE4\_PB4

| #define KEYSCAN\_ROWSENSE4\_PB4   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x1, 0x4) |
| --- |

## [◆ ](#a13bb5c17c76d1cb758653bdb130ff90b)KEYSCAN\_ROWSENSE4\_PB5

| #define KEYSCAN\_ROWSENSE4\_PB5   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE4](#a5cacf707c77181c179dca5145050962e)(0x1, 0x5) |
| --- |

## [◆ ](#a1b62e75eac6ac228f9dab9defde9a2e1)KEYSCAN\_ROWSENSE5\_PA0

| #define KEYSCAN\_ROWSENSE5\_PA0   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x0) |
| --- |

## [◆ ](#a9a4a7e80809a3f35d04c2276f8b220b9)KEYSCAN\_ROWSENSE5\_PA1

| #define KEYSCAN\_ROWSENSE5\_PA1   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x1) |
| --- |

## [◆ ](#af6297695161b54edbb9b158df3a3b59e)KEYSCAN\_ROWSENSE5\_PA2

| #define KEYSCAN\_ROWSENSE5\_PA2   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x2) |
| --- |

## [◆ ](#a087a37402663309e5c81c1bda63aed00)KEYSCAN\_ROWSENSE5\_PA3

| #define KEYSCAN\_ROWSENSE5\_PA3   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x3) |
| --- |

## [◆ ](#ab3074863aa5f863f53f5c2fce912f223)KEYSCAN\_ROWSENSE5\_PA4

| #define KEYSCAN\_ROWSENSE5\_PA4   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x4) |
| --- |

## [◆ ](#a9247d882fae3024aa8e5ff4d1b14eae5)KEYSCAN\_ROWSENSE5\_PA5

| #define KEYSCAN\_ROWSENSE5\_PA5   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x5) |
| --- |

## [◆ ](#a3e52fe29e22f22e95c97c0e080a764e2)KEYSCAN\_ROWSENSE5\_PA6

| #define KEYSCAN\_ROWSENSE5\_PA6   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x6) |
| --- |

## [◆ ](#a0c8953bd67945bf491a512f02e3773ee)KEYSCAN\_ROWSENSE5\_PA7

| #define KEYSCAN\_ROWSENSE5\_PA7   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x7) |
| --- |

## [◆ ](#a9bd8611e430026502d208a037877360d)KEYSCAN\_ROWSENSE5\_PA8

| #define KEYSCAN\_ROWSENSE5\_PA8   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x8) |
| --- |

## [◆ ](#af333321891e6259db4896ccaeb616146)KEYSCAN\_ROWSENSE5\_PA9

| #define KEYSCAN\_ROWSENSE5\_PA9   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x0, 0x9) |
| --- |

## [◆ ](#a8e97a56858b8ddb95242a63579ff3ba3)KEYSCAN\_ROWSENSE5\_PB0

| #define KEYSCAN\_ROWSENSE5\_PB0   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x1, 0x0) |
| --- |

## [◆ ](#a1b99dd7c60b9e211119cf81221ea1265)KEYSCAN\_ROWSENSE5\_PB1

| #define KEYSCAN\_ROWSENSE5\_PB1   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x1, 0x1) |
| --- |

## [◆ ](#a3498d5610cd6afae4e9a15fae40cbbbb)KEYSCAN\_ROWSENSE5\_PB2

| #define KEYSCAN\_ROWSENSE5\_PB2   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x1, 0x2) |
| --- |

## [◆ ](#ad53595710be18bf6403c093dbd1a89aa)KEYSCAN\_ROWSENSE5\_PB3

| #define KEYSCAN\_ROWSENSE5\_PB3   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x1, 0x3) |
| --- |

## [◆ ](#ab074a6202bdc5102875597faf3cf85c3)KEYSCAN\_ROWSENSE5\_PB4

| #define KEYSCAN\_ROWSENSE5\_PB4   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x1, 0x4) |
| --- |

## [◆ ](#a670967a9f35b7a1822fc6e4e9706facd)KEYSCAN\_ROWSENSE5\_PB5

| #define KEYSCAN\_ROWSENSE5\_PB5   [SILABS\_DBUS\_KEYSCAN\_ROWSENSE5](#a9fed939ba0fda9f26a468e54c46b0f28)(0x1, 0x5) |
| --- |

## [◆ ](#a352e584caede1a83b786463abf8e8ffc)LETIMER0\_OUT0\_PA0

| #define LETIMER0\_OUT0\_PA0   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x0) |
| --- |

## [◆ ](#a237d004885f30f207a78f3fce4380476)LETIMER0\_OUT0\_PA1

| #define LETIMER0\_OUT0\_PA1   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x1) |
| --- |

## [◆ ](#a25d0f59297bd6c10acc7714b06af99ca)LETIMER0\_OUT0\_PA2

| #define LETIMER0\_OUT0\_PA2   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x2) |
| --- |

## [◆ ](#a9120e73b07bfa093065ec040045eb61d)LETIMER0\_OUT0\_PA3

| #define LETIMER0\_OUT0\_PA3   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x3) |
| --- |

## [◆ ](#a4f0e8db2242fed71b78c6b0679a6ff76)LETIMER0\_OUT0\_PA4

| #define LETIMER0\_OUT0\_PA4   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x4) |
| --- |

## [◆ ](#a26a82422ca3e7fbd558caa46b4c6705d)LETIMER0\_OUT0\_PA5

| #define LETIMER0\_OUT0\_PA5   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x5) |
| --- |

## [◆ ](#a808e50c2f7823f703795dfbe5d5ef50e)LETIMER0\_OUT0\_PA6

| #define LETIMER0\_OUT0\_PA6   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x6) |
| --- |

## [◆ ](#a0f5833c4d88f979f1cdd7a1375a8074b)LETIMER0\_OUT0\_PA7

| #define LETIMER0\_OUT0\_PA7   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x7) |
| --- |

## [◆ ](#a0cf57fda500379c7e91c98a05d1e17ec)LETIMER0\_OUT0\_PA8

| #define LETIMER0\_OUT0\_PA8   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x8) |
| --- |

## [◆ ](#a185efdff17a0d5f18467184004071f92)LETIMER0\_OUT0\_PA9

| #define LETIMER0\_OUT0\_PA9   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x9) |
| --- |

## [◆ ](#ad81eda4d47fbc7265b325b09eb47232c)LETIMER0\_OUT0\_PB0

| #define LETIMER0\_OUT0\_PB0   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x1, 0x0) |
| --- |

## [◆ ](#a20d0230e58f46869e37b9acfe0e5fb0d)LETIMER0\_OUT0\_PB1

| #define LETIMER0\_OUT0\_PB1   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x1, 0x1) |
| --- |

## [◆ ](#a79820d41c14965a475c0f58982670e34)LETIMER0\_OUT0\_PB2

| #define LETIMER0\_OUT0\_PB2   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x1, 0x2) |
| --- |

## [◆ ](#a31d042f62545423b84bb0de3be30bdcb)LETIMER0\_OUT0\_PB3

| #define LETIMER0\_OUT0\_PB3   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x1, 0x3) |
| --- |

## [◆ ](#a433315136fec0480d99d198e5241915a)LETIMER0\_OUT0\_PB4

| #define LETIMER0\_OUT0\_PB4   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x1, 0x4) |
| --- |

## [◆ ](#ad6ea95686ae38777db2ef238079227e2)LETIMER0\_OUT0\_PB5

| #define LETIMER0\_OUT0\_PB5   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x1, 0x5) |
| --- |

## [◆ ](#a3cab629b6e9cd573b30f8e45a747e819)LETIMER0\_OUT1\_PA0

| #define LETIMER0\_OUT1\_PA0   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x0) |
| --- |

## [◆ ](#a2e90dd7d7686acf9665182356fba429d)LETIMER0\_OUT1\_PA1

| #define LETIMER0\_OUT1\_PA1   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x1) |
| --- |

## [◆ ](#a1ded3647217b200c7d49bf6f99df8800)LETIMER0\_OUT1\_PA2

| #define LETIMER0\_OUT1\_PA2   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x2) |
| --- |

## [◆ ](#ab329e7913b209f11eaba0a2623358976)LETIMER0\_OUT1\_PA3

| #define LETIMER0\_OUT1\_PA3   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x3) |
| --- |

## [◆ ](#a0e0dc57036750466e500d46d9f2f8674)LETIMER0\_OUT1\_PA4

| #define LETIMER0\_OUT1\_PA4   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x4) |
| --- |

## [◆ ](#a2c211216042c0ab444cf3e1b54d4e2f7)LETIMER0\_OUT1\_PA5

| #define LETIMER0\_OUT1\_PA5   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x5) |
| --- |

## [◆ ](#a0aebcc5748062062d09dec35c4baa61f)LETIMER0\_OUT1\_PA6

| #define LETIMER0\_OUT1\_PA6   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x6) |
| --- |

## [◆ ](#aabd4bbcd01e67aa31a1a06b6bbe16edc)LETIMER0\_OUT1\_PA7

| #define LETIMER0\_OUT1\_PA7   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x7) |
| --- |

## [◆ ](#af89df3c0b1d281356ed2316c88ceaa46)LETIMER0\_OUT1\_PA8

| #define LETIMER0\_OUT1\_PA8   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x8) |
| --- |

## [◆ ](#a9bb0b8b5cd8b3d7bff98ac70a6350074)LETIMER0\_OUT1\_PA9

| #define LETIMER0\_OUT1\_PA9   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x9) |
| --- |

## [◆ ](#a5501b8d6e668ef58a71e19bfe0d620b8)LETIMER0\_OUT1\_PB0

| #define LETIMER0\_OUT1\_PB0   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x1, 0x0) |
| --- |

## [◆ ](#a8e4b46c768114f20ee1002820ee4d583)LETIMER0\_OUT1\_PB1

| #define LETIMER0\_OUT1\_PB1   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x1, 0x1) |
| --- |

## [◆ ](#aa1a23a819291f5ab445f4d3db17c78b6)LETIMER0\_OUT1\_PB2

| #define LETIMER0\_OUT1\_PB2   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x1, 0x2) |
| --- |

## [◆ ](#a87c4b33f802fa34191489db40f674684)LETIMER0\_OUT1\_PB3

| #define LETIMER0\_OUT1\_PB3   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x1, 0x3) |
| --- |

## [◆ ](#a0f9c9dcc043629fd8a8bfebf710f3e10)LETIMER0\_OUT1\_PB4

| #define LETIMER0\_OUT1\_PB4   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x1, 0x4) |
| --- |

## [◆ ](#ab40a825d337cec70f62dc987d468216c)LETIMER0\_OUT1\_PB5

| #define LETIMER0\_OUT1\_PB5   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x1, 0x5) |
| --- |

## [◆ ](#a7f276456c2949e4151a1b2a734f8885c)MODEM\_ANT0\_PA0

| #define MODEM\_ANT0\_PA0   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x0) |
| --- |

## [◆ ](#a79c6f7c43dfc9adab0c8eeb974842745)MODEM\_ANT0\_PA1

| #define MODEM\_ANT0\_PA1   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x1) |
| --- |

## [◆ ](#ae187f6726ed20849cb327fbdddd44aca)MODEM\_ANT0\_PA2

| #define MODEM\_ANT0\_PA2   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x2) |
| --- |

## [◆ ](#a45bcc15c32caaa653434df7b01274283)MODEM\_ANT0\_PA3

| #define MODEM\_ANT0\_PA3   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x3) |
| --- |

## [◆ ](#a2378348e1cf6d527113895ad243cc58d)MODEM\_ANT0\_PA4

| #define MODEM\_ANT0\_PA4   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x4) |
| --- |

## [◆ ](#a722db9c869f2f89794bcc1ae32318ad4)MODEM\_ANT0\_PA5

| #define MODEM\_ANT0\_PA5   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x5) |
| --- |

## [◆ ](#a4bffa8d5ecfb474a91ff85afc315043a)MODEM\_ANT0\_PA6

| #define MODEM\_ANT0\_PA6   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x6) |
| --- |

## [◆ ](#a894653787f083faf2185f138b1a77551)MODEM\_ANT0\_PA7

| #define MODEM\_ANT0\_PA7   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x7) |
| --- |

## [◆ ](#a0ed9a2f3ae0b7b8edb0cfd28233a8489)MODEM\_ANT0\_PA8

| #define MODEM\_ANT0\_PA8   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x8) |
| --- |

## [◆ ](#abf541871de6c3a19d265e8ef4ce7a491)MODEM\_ANT0\_PA9

| #define MODEM\_ANT0\_PA9   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x9) |
| --- |

## [◆ ](#a509466c0511355374b0ee3ece106acd6)MODEM\_ANT0\_PB0

| #define MODEM\_ANT0\_PB0   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x1, 0x0) |
| --- |

## [◆ ](#a4c2864f003ccf1355fdbb2be9df0d2ec)MODEM\_ANT0\_PB1

| #define MODEM\_ANT0\_PB1   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x1, 0x1) |
| --- |

## [◆ ](#a63d38e8d680f24158d34a6bff19028b1)MODEM\_ANT0\_PB2

| #define MODEM\_ANT0\_PB2   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x1, 0x2) |
| --- |

## [◆ ](#addd2df0103ce62bea89bea865ad6294a)MODEM\_ANT0\_PB3

| #define MODEM\_ANT0\_PB3   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x1, 0x3) |
| --- |

## [◆ ](#a90d1b1b9472b551710f7ca062750d1c6)MODEM\_ANT0\_PB4

| #define MODEM\_ANT0\_PB4   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x1, 0x4) |
| --- |

## [◆ ](#ae149e31e9640504f96e24f71fbaeb978)MODEM\_ANT0\_PB5

| #define MODEM\_ANT0\_PB5   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x1, 0x5) |
| --- |

## [◆ ](#a6b06e4cb9c997d609b19d7fb7639bf8d)MODEM\_ANT0\_PC0

| #define MODEM\_ANT0\_PC0   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x0) |
| --- |

## [◆ ](#a000751139691af8d66623ad0bd43fc9b)MODEM\_ANT0\_PC1

| #define MODEM\_ANT0\_PC1   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x1) |
| --- |

## [◆ ](#afd5bc8540d8e3e5b0d182312520517be)MODEM\_ANT0\_PC2

| #define MODEM\_ANT0\_PC2   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x2) |
| --- |

## [◆ ](#a33b690ae2e28b1b08b691aa4742d84d7)MODEM\_ANT0\_PC3

| #define MODEM\_ANT0\_PC3   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x3) |
| --- |

## [◆ ](#ac22d54cd6c263a39f33caedf7cb09a0e)MODEM\_ANT0\_PC4

| #define MODEM\_ANT0\_PC4   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x4) |
| --- |

## [◆ ](#a6982c06cdd7b783257ed5f3a74c735c7)MODEM\_ANT0\_PC5

| #define MODEM\_ANT0\_PC5   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x5) |
| --- |

## [◆ ](#a8d28c8701b26924dd7038b6794a97a26)MODEM\_ANT0\_PC6

| #define MODEM\_ANT0\_PC6   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x6) |
| --- |

## [◆ ](#ad9e7f4a18a0eeedadedbefbf81c0449c)MODEM\_ANT0\_PC7

| #define MODEM\_ANT0\_PC7   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x7) |
| --- |

## [◆ ](#a72353908562e64f1f386cf48c9d6f8cc)MODEM\_ANT0\_PC8

| #define MODEM\_ANT0\_PC8   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x8) |
| --- |

## [◆ ](#ad18f643fc180d2fb50ee67bc02105fae)MODEM\_ANT0\_PC9

| #define MODEM\_ANT0\_PC9   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x9) |
| --- |

## [◆ ](#a01730221498f5de5590dbe8f6a293702)MODEM\_ANT0\_PD0

| #define MODEM\_ANT0\_PD0   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x3, 0x0) |
| --- |

## [◆ ](#a968474651d6fc8ced22a693a55d8bf4d)MODEM\_ANT0\_PD1

| #define MODEM\_ANT0\_PD1   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x3, 0x1) |
| --- |

## [◆ ](#a6bee8cd789f6922130830688cf586971)MODEM\_ANT0\_PD2

| #define MODEM\_ANT0\_PD2   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x3, 0x2) |
| --- |

## [◆ ](#aef59bb3ec42a534ffe32a53fb26e1656)MODEM\_ANT0\_PD3

| #define MODEM\_ANT0\_PD3   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x3, 0x3) |
| --- |

## [◆ ](#aba70f4135f5bcc3e10525c27f2f25021)MODEM\_ANT0\_PD4

| #define MODEM\_ANT0\_PD4   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x3, 0x4) |
| --- |

## [◆ ](#ae55b27dcb0ec6c1ad7ee2f3c877a7926)MODEM\_ANT0\_PD5

| #define MODEM\_ANT0\_PD5   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x3, 0x5) |
| --- |

## [◆ ](#a983f562f1f690bbec27d868c3d6b2b1a)MODEM\_ANT1\_PA0

| #define MODEM\_ANT1\_PA0   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x0) |
| --- |

## [◆ ](#a1c8d37c5145858068556a032983680d1)MODEM\_ANT1\_PA1

| #define MODEM\_ANT1\_PA1   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x1) |
| --- |

## [◆ ](#a9a879a4511af923143f8dc6e7710f0be)MODEM\_ANT1\_PA2

| #define MODEM\_ANT1\_PA2   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x2) |
| --- |

## [◆ ](#a5753d0d0ab943103f54d6ad9ea76bccf)MODEM\_ANT1\_PA3

| #define MODEM\_ANT1\_PA3   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x3) |
| --- |

## [◆ ](#a164fc42c8f2bc81bc70453af7bf82402)MODEM\_ANT1\_PA4

| #define MODEM\_ANT1\_PA4   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x4) |
| --- |

## [◆ ](#a790e4407942a7fb6fed5972b59bf12c9)MODEM\_ANT1\_PA5

| #define MODEM\_ANT1\_PA5   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x5) |
| --- |

## [◆ ](#a908cd5b571ab7ec4ba04581f3bf67166)MODEM\_ANT1\_PA6

| #define MODEM\_ANT1\_PA6   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x6) |
| --- |

## [◆ ](#a5c272c67918110b0cd323ed0228370bb)MODEM\_ANT1\_PA7

| #define MODEM\_ANT1\_PA7   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x7) |
| --- |

## [◆ ](#a1ab7e1ea92808eb14c818516aaa3295a)MODEM\_ANT1\_PA8

| #define MODEM\_ANT1\_PA8   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x8) |
| --- |

## [◆ ](#a013a26a517f5f339fc199affb5e7bb8d)MODEM\_ANT1\_PA9

| #define MODEM\_ANT1\_PA9   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x9) |
| --- |

## [◆ ](#adbe918778efba6fe712e7043457c43bb)MODEM\_ANT1\_PB0

| #define MODEM\_ANT1\_PB0   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x1, 0x0) |
| --- |

## [◆ ](#a6c5a484675c81a07f3709cb391113c22)MODEM\_ANT1\_PB1

| #define MODEM\_ANT1\_PB1   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x1, 0x1) |
| --- |

## [◆ ](#acbc03ad5136cb7715b10956805d851ad)MODEM\_ANT1\_PB2

| #define MODEM\_ANT1\_PB2   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x1, 0x2) |
| --- |

## [◆ ](#ac9db3cba6b213aba7b2e75913d7793b0)MODEM\_ANT1\_PB3

| #define MODEM\_ANT1\_PB3   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x1, 0x3) |
| --- |

## [◆ ](#a3772761615fb1f6b9427d09f40de1cb0)MODEM\_ANT1\_PB4

| #define MODEM\_ANT1\_PB4   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x1, 0x4) |
| --- |

## [◆ ](#a745f8f8c26db2c13b989a729f7b8da4b)MODEM\_ANT1\_PB5

| #define MODEM\_ANT1\_PB5   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x1, 0x5) |
| --- |

## [◆ ](#a5718fbbd7d66e6c775b8904b50b14aec)MODEM\_ANT1\_PC0

| #define MODEM\_ANT1\_PC0   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x0) |
| --- |

## [◆ ](#a25315b04583ee4d44f2e1835003679e9)MODEM\_ANT1\_PC1

| #define MODEM\_ANT1\_PC1   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x1) |
| --- |

## [◆ ](#a7480d21cbb697630fd83f494f671b030)MODEM\_ANT1\_PC2

| #define MODEM\_ANT1\_PC2   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x2) |
| --- |

## [◆ ](#aa6ba89e0d2c7347f10a1a18d461986db)MODEM\_ANT1\_PC3

| #define MODEM\_ANT1\_PC3   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x3) |
| --- |

## [◆ ](#a293042adb906716b25453e23c66932ee)MODEM\_ANT1\_PC4

| #define MODEM\_ANT1\_PC4   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x4) |
| --- |

## [◆ ](#aa699042d4cec5024da6439e6fa629c5f)MODEM\_ANT1\_PC5

| #define MODEM\_ANT1\_PC5   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x5) |
| --- |

## [◆ ](#a6f4b41d3971310c038878142c59d1375)MODEM\_ANT1\_PC6

| #define MODEM\_ANT1\_PC6   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x6) |
| --- |

## [◆ ](#aa48104a69c4edacb22f41bd14e717640)MODEM\_ANT1\_PC7

| #define MODEM\_ANT1\_PC7   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x7) |
| --- |

## [◆ ](#a08a181d182cb8ac110791185e150ac93)MODEM\_ANT1\_PC8

| #define MODEM\_ANT1\_PC8   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x8) |
| --- |

## [◆ ](#ac90a33371364c2d3b43b6ecd20202992)MODEM\_ANT1\_PC9

| #define MODEM\_ANT1\_PC9   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x9) |
| --- |

## [◆ ](#a1ebb5a0437c033fa7d567000c0b8c383)MODEM\_ANT1\_PD0

| #define MODEM\_ANT1\_PD0   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x3, 0x0) |
| --- |

## [◆ ](#a1cc580714150e9383e280946b2863b31)MODEM\_ANT1\_PD1

| #define MODEM\_ANT1\_PD1   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x3, 0x1) |
| --- |

## [◆ ](#ac3322bcfcef6e6a680cf4611d0b363ef)MODEM\_ANT1\_PD2

| #define MODEM\_ANT1\_PD2   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x3, 0x2) |
| --- |

## [◆ ](#abfdb37fc77643dc2853d87009c2425d6)MODEM\_ANT1\_PD3

| #define MODEM\_ANT1\_PD3   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x3, 0x3) |
| --- |

## [◆ ](#abd04eb50b1a4d87042b59362e4b8758d)MODEM\_ANT1\_PD4

| #define MODEM\_ANT1\_PD4   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x3, 0x4) |
| --- |

## [◆ ](#aa37f9ee08275da5c7c423460324c6f00)MODEM\_ANT1\_PD5

| #define MODEM\_ANT1\_PD5   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x3, 0x5) |
| --- |

## [◆ ](#ace2bae83851b3aab46a81ef1a6c636b4)MODEM\_ANTROLLOVER\_PC0

| #define MODEM\_ANTROLLOVER\_PC0   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x0) |
| --- |

## [◆ ](#a85ff56d69539994de2a84edf12f8a2be)MODEM\_ANTROLLOVER\_PC1

| #define MODEM\_ANTROLLOVER\_PC1   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x1) |
| --- |

## [◆ ](#ae6601ed4b1dc45fad0deb09610797610)MODEM\_ANTROLLOVER\_PC2

| #define MODEM\_ANTROLLOVER\_PC2   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x2) |
| --- |

## [◆ ](#a53fceeed6e44ab7bc81698d3c4c16207)MODEM\_ANTROLLOVER\_PC3

| #define MODEM\_ANTROLLOVER\_PC3   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x3) |
| --- |

## [◆ ](#ac253adc5e51912ed5f4407447c81f473)MODEM\_ANTROLLOVER\_PC4

| #define MODEM\_ANTROLLOVER\_PC4   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x4) |
| --- |

## [◆ ](#a60f405f65313e35ba59eca8fa208ed2c)MODEM\_ANTROLLOVER\_PC5

| #define MODEM\_ANTROLLOVER\_PC5   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x5) |
| --- |

## [◆ ](#ad39de8c7dff7e3297e5beca22e2034f4)MODEM\_ANTROLLOVER\_PC6

| #define MODEM\_ANTROLLOVER\_PC6   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x6) |
| --- |

## [◆ ](#a50b0007df6bc2de4b9200cbb1b79acf0)MODEM\_ANTROLLOVER\_PC7

| #define MODEM\_ANTROLLOVER\_PC7   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x7) |
| --- |

## [◆ ](#acb5cec62092f3cb2a1dbe8cab74ade40)MODEM\_ANTROLLOVER\_PC8

| #define MODEM\_ANTROLLOVER\_PC8   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x8) |
| --- |

## [◆ ](#a4d74f01cef772f0e097ff431b9b04542)MODEM\_ANTROLLOVER\_PC9

| #define MODEM\_ANTROLLOVER\_PC9   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x9) |
| --- |

## [◆ ](#a88bb19ac23eb8bcc2868bf22bd4a12af)MODEM\_ANTROLLOVER\_PD0

| #define MODEM\_ANTROLLOVER\_PD0   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x3, 0x0) |
| --- |

## [◆ ](#a92aeed47b01736dac03935ac699b9727)MODEM\_ANTROLLOVER\_PD1

| #define MODEM\_ANTROLLOVER\_PD1   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x3, 0x1) |
| --- |

## [◆ ](#a603e14d84a8b13b7d4ee5bdab126cdae)MODEM\_ANTROLLOVER\_PD2

| #define MODEM\_ANTROLLOVER\_PD2   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x3, 0x2) |
| --- |

## [◆ ](#a506855980f4dda9c5de58b11d76f7b4f)MODEM\_ANTROLLOVER\_PD3

| #define MODEM\_ANTROLLOVER\_PD3   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x3, 0x3) |
| --- |

## [◆ ](#adfb16e607ee78520fc2579516f49a90b)MODEM\_ANTROLLOVER\_PD4

| #define MODEM\_ANTROLLOVER\_PD4   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x3, 0x4) |
| --- |

## [◆ ](#a738a7352b0fdb0654efa643fab795675)MODEM\_ANTROLLOVER\_PD5

| #define MODEM\_ANTROLLOVER\_PD5   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x3, 0x5) |
| --- |

## [◆ ](#a72a1f767f29b37e2f0975efb930aabdc)MODEM\_ANTRR0\_PC0

| #define MODEM\_ANTRR0\_PC0   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x0) |
| --- |

## [◆ ](#a7465a3a4cf1cd92249001733145da7ed)MODEM\_ANTRR0\_PC1

| #define MODEM\_ANTRR0\_PC1   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x1) |
| --- |

## [◆ ](#a1b109adfe9e7699e7cb1a1fb46aa132c)MODEM\_ANTRR0\_PC2

| #define MODEM\_ANTRR0\_PC2   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x2) |
| --- |

## [◆ ](#a4109515cd008205b323edb06d2a19607)MODEM\_ANTRR0\_PC3

| #define MODEM\_ANTRR0\_PC3   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x3) |
| --- |

## [◆ ](#a56971ab62d7131e5aba024260d295153)MODEM\_ANTRR0\_PC4

| #define MODEM\_ANTRR0\_PC4   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x4) |
| --- |

## [◆ ](#a4de029d596f34060bde0d63982b171b3)MODEM\_ANTRR0\_PC5

| #define MODEM\_ANTRR0\_PC5   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x5) |
| --- |

## [◆ ](#a3a438458ac921a00c90a85d343ea1f90)MODEM\_ANTRR0\_PC6

| #define MODEM\_ANTRR0\_PC6   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x6) |
| --- |

## [◆ ](#a68f15a8b8a2acd73ff7b772aa529c0d9)MODEM\_ANTRR0\_PC7

| #define MODEM\_ANTRR0\_PC7   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x7) |
| --- |

## [◆ ](#af71e0d4d99fcf43095b57a0a8ba89629)MODEM\_ANTRR0\_PC8

| #define MODEM\_ANTRR0\_PC8   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x8) |
| --- |

## [◆ ](#a0cbcfb4610c61e741525b3cff7c6b988)MODEM\_ANTRR0\_PC9

| #define MODEM\_ANTRR0\_PC9   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x9) |
| --- |

## [◆ ](#a78f716f923dadb2a1df8eebc07c1a1ba)MODEM\_ANTRR0\_PD0

| #define MODEM\_ANTRR0\_PD0   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x3, 0x0) |
| --- |

## [◆ ](#ab46244ef8e98b0e13a0874b8831d1c9e)MODEM\_ANTRR0\_PD1

| #define MODEM\_ANTRR0\_PD1   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x3, 0x1) |
| --- |

## [◆ ](#ad652d37f429c634eaed147b962b1f81c)MODEM\_ANTRR0\_PD2

| #define MODEM\_ANTRR0\_PD2   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x3, 0x2) |
| --- |

## [◆ ](#a1cf6846a778c4a5820d42d1a8b9a6cef)MODEM\_ANTRR0\_PD3

| #define MODEM\_ANTRR0\_PD3   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x3, 0x3) |
| --- |

## [◆ ](#a084f75e9ebb22c162b28eff741c0997f)MODEM\_ANTRR0\_PD4

| #define MODEM\_ANTRR0\_PD4   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x3, 0x4) |
| --- |

## [◆ ](#aeba1b8f1af14062395a1cb161b46246b)MODEM\_ANTRR0\_PD5

| #define MODEM\_ANTRR0\_PD5   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x3, 0x5) |
| --- |

## [◆ ](#a5b77d7b22d3ba5fc6ccadceb8fd784e5)MODEM\_ANTRR1\_PC0

| #define MODEM\_ANTRR1\_PC0   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x0) |
| --- |

## [◆ ](#a79bc69a44835cf383b1de6037c8fae63)MODEM\_ANTRR1\_PC1

| #define MODEM\_ANTRR1\_PC1   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x1) |
| --- |

## [◆ ](#aa7cd2fde356a617651a7b518f9558709)MODEM\_ANTRR1\_PC2

| #define MODEM\_ANTRR1\_PC2   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x2) |
| --- |

## [◆ ](#ac12248a293d8a3c328df438370024a12)MODEM\_ANTRR1\_PC3

| #define MODEM\_ANTRR1\_PC3   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x3) |
| --- |

## [◆ ](#a6067448e7e46ae003e07b75ec4f22ddf)MODEM\_ANTRR1\_PC4

| #define MODEM\_ANTRR1\_PC4   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x4) |
| --- |

## [◆ ](#afb89ffed0de8306a2b3b2ff8a09db4eb)MODEM\_ANTRR1\_PC5

| #define MODEM\_ANTRR1\_PC5   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x5) |
| --- |

## [◆ ](#a2b02ddcbecd53f862993644a685928df)MODEM\_ANTRR1\_PC6

| #define MODEM\_ANTRR1\_PC6   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x6) |
| --- |

## [◆ ](#a5d14286b67618916e103c98ccaab6652)MODEM\_ANTRR1\_PC7

| #define MODEM\_ANTRR1\_PC7   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x7) |
| --- |

## [◆ ](#ad91019ee3e5cf685239a7de514d06b68)MODEM\_ANTRR1\_PC8

| #define MODEM\_ANTRR1\_PC8   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x8) |
| --- |

## [◆ ](#ae0ee67d5c53f010f3ee7194690a44c78)MODEM\_ANTRR1\_PC9

| #define MODEM\_ANTRR1\_PC9   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x9) |
| --- |

## [◆ ](#a3d4c45786676da1e67017a4cdb048449)MODEM\_ANTRR1\_PD0

| #define MODEM\_ANTRR1\_PD0   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x3, 0x0) |
| --- |

## [◆ ](#a74ac37ba6d806625dadd63c1af681a84)MODEM\_ANTRR1\_PD1

| #define MODEM\_ANTRR1\_PD1   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x3, 0x1) |
| --- |

## [◆ ](#a5c4e16526937500b8cc70a6b844ee832)MODEM\_ANTRR1\_PD2

| #define MODEM\_ANTRR1\_PD2   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x3, 0x2) |
| --- |

## [◆ ](#a79878ca6c07ea72a02c23a7321832b29)MODEM\_ANTRR1\_PD3

| #define MODEM\_ANTRR1\_PD3   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x3, 0x3) |
| --- |

## [◆ ](#a560cf5fe4d967d7577c63ecd4aaf7cfb)MODEM\_ANTRR1\_PD4

| #define MODEM\_ANTRR1\_PD4   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x3, 0x4) |
| --- |

## [◆ ](#a37fd0719bec33fe2c68d64ebd9697cf9)MODEM\_ANTRR1\_PD5

| #define MODEM\_ANTRR1\_PD5   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x3, 0x5) |
| --- |

## [◆ ](#a86532fa3d12fd905879905f4df67d954)MODEM\_ANTRR2\_PC0

| #define MODEM\_ANTRR2\_PC0   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x0) |
| --- |

## [◆ ](#a6e586c76b41f2ecf6384a6257390ee22)MODEM\_ANTRR2\_PC1

| #define MODEM\_ANTRR2\_PC1   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x1) |
| --- |

## [◆ ](#af57b2e22e3079c5825638bf1556d5f63)MODEM\_ANTRR2\_PC2

| #define MODEM\_ANTRR2\_PC2   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x2) |
| --- |

## [◆ ](#a43e57733d4b8bebe91750a3041245789)MODEM\_ANTRR2\_PC3

| #define MODEM\_ANTRR2\_PC3   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x3) |
| --- |

## [◆ ](#aa31ca6e6610920deaa06c77f7deaf40c)MODEM\_ANTRR2\_PC4

| #define MODEM\_ANTRR2\_PC4   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x4) |
| --- |

## [◆ ](#af3df188180c0609f2cb4c63f1ff77ff1)MODEM\_ANTRR2\_PC5

| #define MODEM\_ANTRR2\_PC5   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x5) |
| --- |

## [◆ ](#a69bb0899e1d7201561638d287612708c)MODEM\_ANTRR2\_PC6

| #define MODEM\_ANTRR2\_PC6   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x6) |
| --- |

## [◆ ](#a0696c2885355b5c7b13bef2e51d7188f)MODEM\_ANTRR2\_PC7

| #define MODEM\_ANTRR2\_PC7   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x7) |
| --- |

## [◆ ](#aa509860c7999d11e76d56b4dc7bbc6f6)MODEM\_ANTRR2\_PC8

| #define MODEM\_ANTRR2\_PC8   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x8) |
| --- |

## [◆ ](#acedaf796ecf36a0ec3d91b83a95ee1c0)MODEM\_ANTRR2\_PC9

| #define MODEM\_ANTRR2\_PC9   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x9) |
| --- |

## [◆ ](#a368c3325d067b5f5f93d67ad59cf04a9)MODEM\_ANTRR2\_PD0

| #define MODEM\_ANTRR2\_PD0   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x3, 0x0) |
| --- |

## [◆ ](#a019e9b59d7ebf97b06ea3deb84eb8a9d)MODEM\_ANTRR2\_PD1

| #define MODEM\_ANTRR2\_PD1   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x3, 0x1) |
| --- |

## [◆ ](#a591f45f9fa102e7e5ce0281003eb7ba9)MODEM\_ANTRR2\_PD2

| #define MODEM\_ANTRR2\_PD2   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x3, 0x2) |
| --- |

## [◆ ](#a341ce7ea3431fe6a6b04f88ba4cd4521)MODEM\_ANTRR2\_PD3

| #define MODEM\_ANTRR2\_PD3   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x3, 0x3) |
| --- |

## [◆ ](#a0cfade0fe329ae4d261ce8dd4d3c1d86)MODEM\_ANTRR2\_PD4

| #define MODEM\_ANTRR2\_PD4   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x3, 0x4) |
| --- |

## [◆ ](#af598bd2d0e6dd17957b092c2e4a73a1a)MODEM\_ANTRR2\_PD5

| #define MODEM\_ANTRR2\_PD5   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x3, 0x5) |
| --- |

## [◆ ](#a2fa9d157e9749343083524dcddd1f1d1)MODEM\_ANTRR3\_PC0

| #define MODEM\_ANTRR3\_PC0   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x0) |
| --- |

## [◆ ](#a8c1d56d6692fefbffd9ca60e9f6d45ac)MODEM\_ANTRR3\_PC1

| #define MODEM\_ANTRR3\_PC1   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x1) |
| --- |

## [◆ ](#a678e2cb9f2ac53e8630a25bec6841fd0)MODEM\_ANTRR3\_PC2

| #define MODEM\_ANTRR3\_PC2   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x2) |
| --- |

## [◆ ](#a4b8cd19ab9ff53e0b51ffcf6beea247b)MODEM\_ANTRR3\_PC3

| #define MODEM\_ANTRR3\_PC3   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x3) |
| --- |

## [◆ ](#ab4586b72a654c124f6c5c7097c9902c7)MODEM\_ANTRR3\_PC4

| #define MODEM\_ANTRR3\_PC4   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x4) |
| --- |

## [◆ ](#abc7d9d9c03ae387c0a3b028f09858b79)MODEM\_ANTRR3\_PC5

| #define MODEM\_ANTRR3\_PC5   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x5) |
| --- |

## [◆ ](#a28641556808bb4359216027d35cb3e6c)MODEM\_ANTRR3\_PC6

| #define MODEM\_ANTRR3\_PC6   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x6) |
| --- |

## [◆ ](#aec4c5821f3a602b6a15d6861bb116f22)MODEM\_ANTRR3\_PC7

| #define MODEM\_ANTRR3\_PC7   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x7) |
| --- |

## [◆ ](#a325f2e26a25e9775ce3422dee8c80355)MODEM\_ANTRR3\_PC8

| #define MODEM\_ANTRR3\_PC8   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x8) |
| --- |

## [◆ ](#ad156d5e1d6a6804e60c5621fbd3439a2)MODEM\_ANTRR3\_PC9

| #define MODEM\_ANTRR3\_PC9   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x9) |
| --- |

## [◆ ](#a3fb63d9e07fc0c63605bde31a8288b57)MODEM\_ANTRR3\_PD0

| #define MODEM\_ANTRR3\_PD0   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x3, 0x0) |
| --- |

## [◆ ](#ae8e6d95bcc501a226c2ae7cf26974ae4)MODEM\_ANTRR3\_PD1

| #define MODEM\_ANTRR3\_PD1   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x3, 0x1) |
| --- |

## [◆ ](#a203100da0081cb15ba56e28b13164d2e)MODEM\_ANTRR3\_PD2

| #define MODEM\_ANTRR3\_PD2   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x3, 0x2) |
| --- |

## [◆ ](#af02994437b5f5b545ddf48b4adb1b475)MODEM\_ANTRR3\_PD3

| #define MODEM\_ANTRR3\_PD3   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x3, 0x3) |
| --- |

## [◆ ](#a02fb9def34402666d02b843a5f5794e4)MODEM\_ANTRR3\_PD4

| #define MODEM\_ANTRR3\_PD4   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x3, 0x4) |
| --- |

## [◆ ](#a7f660712ed2ff14db606e8bdc3db8558)MODEM\_ANTRR3\_PD5

| #define MODEM\_ANTRR3\_PD5   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x3, 0x5) |
| --- |

## [◆ ](#ac9f090be13e72088bb72bf1c75094e76)MODEM\_ANTRR4\_PC0

| #define MODEM\_ANTRR4\_PC0   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x0) |
| --- |

## [◆ ](#ac4ed6ce8ae1be803f08f5fe066521cc9)MODEM\_ANTRR4\_PC1

| #define MODEM\_ANTRR4\_PC1   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x1) |
| --- |

## [◆ ](#af477f9423d354cfb59ab51fdd086cce2)MODEM\_ANTRR4\_PC2

| #define MODEM\_ANTRR4\_PC2   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x2) |
| --- |

## [◆ ](#a21f70b645f9642fb79fe2646384dfb62)MODEM\_ANTRR4\_PC3

| #define MODEM\_ANTRR4\_PC3   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x3) |
| --- |

## [◆ ](#aee6646a5a12bad19280806cd1e805cc3)MODEM\_ANTRR4\_PC4

| #define MODEM\_ANTRR4\_PC4   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x4) |
| --- |

## [◆ ](#a82cbd5d4704cd282a9cbae9109505066)MODEM\_ANTRR4\_PC5

| #define MODEM\_ANTRR4\_PC5   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x5) |
| --- |

## [◆ ](#a2cf72bdc82e898d02a4d50f8e25e764f)MODEM\_ANTRR4\_PC6

| #define MODEM\_ANTRR4\_PC6   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x6) |
| --- |

## [◆ ](#ab58e49c260c123e08f8d59f1c309560b)MODEM\_ANTRR4\_PC7

| #define MODEM\_ANTRR4\_PC7   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x7) |
| --- |

## [◆ ](#a349966b78912bc5d1bd4a177666e4cb8)MODEM\_ANTRR4\_PC8

| #define MODEM\_ANTRR4\_PC8   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x8) |
| --- |

## [◆ ](#a3c3ba01f2d9d0bc0ad672a0e7d2cceba)MODEM\_ANTRR4\_PC9

| #define MODEM\_ANTRR4\_PC9   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x9) |
| --- |

## [◆ ](#a10f6578c47953ee7d5f052e9726ee8d3)MODEM\_ANTRR4\_PD0

| #define MODEM\_ANTRR4\_PD0   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x3, 0x0) |
| --- |

## [◆ ](#ad4adb3ecb506a24bf919c524513a913c)MODEM\_ANTRR4\_PD1

| #define MODEM\_ANTRR4\_PD1   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x3, 0x1) |
| --- |

## [◆ ](#ad2ab7abbd3e49703350ae7be2d2e01b8)MODEM\_ANTRR4\_PD2

| #define MODEM\_ANTRR4\_PD2   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x3, 0x2) |
| --- |

## [◆ ](#a815940c71002bc123b8b48ac6c5cda20)MODEM\_ANTRR4\_PD3

| #define MODEM\_ANTRR4\_PD3   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x3, 0x3) |
| --- |

## [◆ ](#a3fad44fa71039513644549a88ac0a7d4)MODEM\_ANTRR4\_PD4

| #define MODEM\_ANTRR4\_PD4   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x3, 0x4) |
| --- |

## [◆ ](#adf521d37e1fe758426f06a4db451d22b)MODEM\_ANTRR4\_PD5

| #define MODEM\_ANTRR4\_PD5   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x3, 0x5) |
| --- |

## [◆ ](#aa59209d310467981d68fc8ec63856bc6)MODEM\_ANTRR5\_PC0

| #define MODEM\_ANTRR5\_PC0   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x0) |
| --- |

## [◆ ](#ae28a87908fd594ba99d726c7cd56f348)MODEM\_ANTRR5\_PC1

| #define MODEM\_ANTRR5\_PC1   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x1) |
| --- |

## [◆ ](#a51d8ba60291e9f51cc34f5826b07a336)MODEM\_ANTRR5\_PC2

| #define MODEM\_ANTRR5\_PC2   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x2) |
| --- |

## [◆ ](#a4760c7eeb47e12e62db8fac47e779c05)MODEM\_ANTRR5\_PC3

| #define MODEM\_ANTRR5\_PC3   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x3) |
| --- |

## [◆ ](#ad723f7203c93c76019adb70110860402)MODEM\_ANTRR5\_PC4

| #define MODEM\_ANTRR5\_PC4   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x4) |
| --- |

## [◆ ](#a71833f446bf584b32654327734733059)MODEM\_ANTRR5\_PC5

| #define MODEM\_ANTRR5\_PC5   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x5) |
| --- |

## [◆ ](#a8c24d68ddf4c4b644781781ed0af0f0f)MODEM\_ANTRR5\_PC6

| #define MODEM\_ANTRR5\_PC6   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x6) |
| --- |

## [◆ ](#aa599783a6852570f4719190d992eff58)MODEM\_ANTRR5\_PC7

| #define MODEM\_ANTRR5\_PC7   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x7) |
| --- |

## [◆ ](#a09791dc6a09774a53cbee6c3c78f0bc7)MODEM\_ANTRR5\_PC8

| #define MODEM\_ANTRR5\_PC8   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x8) |
| --- |

## [◆ ](#ae409168c3aab50b55d8f6cc55f18c0b2)MODEM\_ANTRR5\_PC9

| #define MODEM\_ANTRR5\_PC9   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x9) |
| --- |

## [◆ ](#a404392cc5769ad92662f7448e6458d05)MODEM\_ANTRR5\_PD0

| #define MODEM\_ANTRR5\_PD0   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x3, 0x0) |
| --- |

## [◆ ](#a88da3eca1fcd6f67c5a0c9e590c78dcf)MODEM\_ANTRR5\_PD1

| #define MODEM\_ANTRR5\_PD1   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x3, 0x1) |
| --- |

## [◆ ](#a6f6234ac85f4a3e3095672b20cd2f636)MODEM\_ANTRR5\_PD2

| #define MODEM\_ANTRR5\_PD2   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x3, 0x2) |
| --- |

## [◆ ](#a32dc3957baa49edb10e49d5914b46c14)MODEM\_ANTRR5\_PD3

| #define MODEM\_ANTRR5\_PD3   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x3, 0x3) |
| --- |

## [◆ ](#acfb8af84df8cd5036cc697ff4a225311)MODEM\_ANTRR5\_PD4

| #define MODEM\_ANTRR5\_PD4   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x3, 0x4) |
| --- |

## [◆ ](#a60065f832cefcdd2ecf5c0d6015b8943)MODEM\_ANTRR5\_PD5

| #define MODEM\_ANTRR5\_PD5   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x3, 0x5) |
| --- |

## [◆ ](#a93c921b96501eca162c6eee962c60f57)MODEM\_ANTSWEN\_PC0

| #define MODEM\_ANTSWEN\_PC0   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x0) |
| --- |

## [◆ ](#ac4ceffe68747645a764487912dc1ac16)MODEM\_ANTSWEN\_PC1

| #define MODEM\_ANTSWEN\_PC1   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x1) |
| --- |

## [◆ ](#ace5d141a804e6f73e77a0fcff81e4c56)MODEM\_ANTSWEN\_PC2

| #define MODEM\_ANTSWEN\_PC2   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x2) |
| --- |

## [◆ ](#a1e59daa60e50af30180144363f4f1300)MODEM\_ANTSWEN\_PC3

| #define MODEM\_ANTSWEN\_PC3   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x3) |
| --- |

## [◆ ](#a2a7fa90f1a78c16a6e6cad15ff2183f0)MODEM\_ANTSWEN\_PC4

| #define MODEM\_ANTSWEN\_PC4   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x4) |
| --- |

## [◆ ](#aa7767d9a2806a0843c892fddcacd7600)MODEM\_ANTSWEN\_PC5

| #define MODEM\_ANTSWEN\_PC5   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x5) |
| --- |

## [◆ ](#ae3c784f6e183cadf0dee817c5b9ba192)MODEM\_ANTSWEN\_PC6

| #define MODEM\_ANTSWEN\_PC6   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x6) |
| --- |

## [◆ ](#aa8ac7404cee302c171ed8646e8573a8a)MODEM\_ANTSWEN\_PC7

| #define MODEM\_ANTSWEN\_PC7   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x7) |
| --- |

## [◆ ](#a41335d21a9e37772deafd2b06e9ae545)MODEM\_ANTSWEN\_PC8

| #define MODEM\_ANTSWEN\_PC8   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x8) |
| --- |

## [◆ ](#a98c97461ddd331655edfccdbd1038338)MODEM\_ANTSWEN\_PC9

| #define MODEM\_ANTSWEN\_PC9   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x9) |
| --- |

## [◆ ](#a6910c237541dc3d1d3c6a658aa259bb0)MODEM\_ANTSWEN\_PD0

| #define MODEM\_ANTSWEN\_PD0   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x3, 0x0) |
| --- |

## [◆ ](#ab91df7c7ff2dd05a15844f0b223a4a9e)MODEM\_ANTSWEN\_PD1

| #define MODEM\_ANTSWEN\_PD1   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x3, 0x1) |
| --- |

## [◆ ](#a5df0df918051e5a4c530c3b46c328e5f)MODEM\_ANTSWEN\_PD2

| #define MODEM\_ANTSWEN\_PD2   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x3, 0x2) |
| --- |

## [◆ ](#aed4a6536e2515502a852bb782730081f)MODEM\_ANTSWEN\_PD3

| #define MODEM\_ANTSWEN\_PD3   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x3, 0x3) |
| --- |

## [◆ ](#a9712e57526a5590d9feabdfbdd2e06e0)MODEM\_ANTSWEN\_PD4

| #define MODEM\_ANTSWEN\_PD4   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x3, 0x4) |
| --- |

## [◆ ](#aad4ceb43804ecb0b5c1283254c942261)MODEM\_ANTSWEN\_PD5

| #define MODEM\_ANTSWEN\_PD5   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x3, 0x5) |
| --- |

## [◆ ](#a35403ecde9ec6d51d0647558624c1755)MODEM\_ANTSWUS\_PC0

| #define MODEM\_ANTSWUS\_PC0   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x0) |
| --- |

## [◆ ](#ac302424df9d075a5546b11e3a2f5a362)MODEM\_ANTSWUS\_PC1

| #define MODEM\_ANTSWUS\_PC1   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x1) |
| --- |

## [◆ ](#a4c756e71ee82c7fbe41ec5ba5b33a0bd)MODEM\_ANTSWUS\_PC2

| #define MODEM\_ANTSWUS\_PC2   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x2) |
| --- |

## [◆ ](#aff74d3e1d4ae4fd44a05f4d291a1f550)MODEM\_ANTSWUS\_PC3

| #define MODEM\_ANTSWUS\_PC3   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x3) |
| --- |

## [◆ ](#af73c92cf63826be7cc6a1fe3e03b181d)MODEM\_ANTSWUS\_PC4

| #define MODEM\_ANTSWUS\_PC4   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x4) |
| --- |

## [◆ ](#a294c8a1ce79d365a9d29717db3942107)MODEM\_ANTSWUS\_PC5

| #define MODEM\_ANTSWUS\_PC5   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x5) |
| --- |

## [◆ ](#afad4a0c9a58b16b48cb06279fd7db652)MODEM\_ANTSWUS\_PC6

| #define MODEM\_ANTSWUS\_PC6   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x6) |
| --- |

## [◆ ](#a6f86a2ef7edfbe782b7700efae544a48)MODEM\_ANTSWUS\_PC7

| #define MODEM\_ANTSWUS\_PC7   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x7) |
| --- |

## [◆ ](#a6a470c8cd7b56a56b1be748427bd326c)MODEM\_ANTSWUS\_PC8

| #define MODEM\_ANTSWUS\_PC8   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x8) |
| --- |

## [◆ ](#ad94ab3184202a103d96e35f4f3658bdf)MODEM\_ANTSWUS\_PC9

| #define MODEM\_ANTSWUS\_PC9   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x9) |
| --- |

## [◆ ](#aa47c88d6d4e2cc38e891b7e03e699756)MODEM\_ANTSWUS\_PD0

| #define MODEM\_ANTSWUS\_PD0   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x3, 0x0) |
| --- |

## [◆ ](#a72a8e4b8a5ac8c3fe74eb26cd08e312b)MODEM\_ANTSWUS\_PD1

| #define MODEM\_ANTSWUS\_PD1   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x3, 0x1) |
| --- |

## [◆ ](#a6852ed7e65ee6e22f96ecddbe0bcc05d)MODEM\_ANTSWUS\_PD2

| #define MODEM\_ANTSWUS\_PD2   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x3, 0x2) |
| --- |

## [◆ ](#ab3e009ff6d5427f43e9fbf4743098520)MODEM\_ANTSWUS\_PD3

| #define MODEM\_ANTSWUS\_PD3   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x3, 0x3) |
| --- |

## [◆ ](#a4b7a96b271c947e02a2261da3959588d)MODEM\_ANTSWUS\_PD4

| #define MODEM\_ANTSWUS\_PD4   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x3, 0x4) |
| --- |

## [◆ ](#ad5f74a2313abda0899378de0de5480f6)MODEM\_ANTSWUS\_PD5

| #define MODEM\_ANTSWUS\_PD5   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x3, 0x5) |
| --- |

## [◆ ](#a0b75979323bdd89b0cc9d10469b0095c)MODEM\_ANTTRIG\_PC0

| #define MODEM\_ANTTRIG\_PC0   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x0) |
| --- |

## [◆ ](#a93518da86e975b51c00c957f0bb95ab0)MODEM\_ANTTRIG\_PC1

| #define MODEM\_ANTTRIG\_PC1   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x1) |
| --- |

## [◆ ](#a27622d1c3e77514a6c175f88ba67b2f6)MODEM\_ANTTRIG\_PC2

| #define MODEM\_ANTTRIG\_PC2   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x2) |
| --- |

## [◆ ](#afe612f9d7068a7d8f3f27950a3db07e5)MODEM\_ANTTRIG\_PC3

| #define MODEM\_ANTTRIG\_PC3   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x3) |
| --- |

## [◆ ](#aa4e5df434329d0121c13dc72c90c9c13)MODEM\_ANTTRIG\_PC4

| #define MODEM\_ANTTRIG\_PC4   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x4) |
| --- |

## [◆ ](#a0c7cd91aef9412c36340e43a41b95fbe)MODEM\_ANTTRIG\_PC5

| #define MODEM\_ANTTRIG\_PC5   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x5) |
| --- |

## [◆ ](#a6bbd8a93a130ac08292335b664803e3b)MODEM\_ANTTRIG\_PC6

| #define MODEM\_ANTTRIG\_PC6   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x6) |
| --- |

## [◆ ](#a69b763a9d3a015481424995589a80c3f)MODEM\_ANTTRIG\_PC7

| #define MODEM\_ANTTRIG\_PC7   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x7) |
| --- |

## [◆ ](#a6845de25ca254d6d61e404f9e2847bff)MODEM\_ANTTRIG\_PC8

| #define MODEM\_ANTTRIG\_PC8   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x8) |
| --- |

## [◆ ](#ab3cf955809a2bc320ac95fd7eae4f77c)MODEM\_ANTTRIG\_PC9

| #define MODEM\_ANTTRIG\_PC9   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x9) |
| --- |

## [◆ ](#abc60b310f524562dc1252fec0238dbdf)MODEM\_ANTTRIG\_PD0

| #define MODEM\_ANTTRIG\_PD0   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x3, 0x0) |
| --- |

## [◆ ](#ac437bf9340d8c56595543e8de7b9157e)MODEM\_ANTTRIG\_PD1

| #define MODEM\_ANTTRIG\_PD1   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x3, 0x1) |
| --- |

## [◆ ](#a6b33477ce6327abad3ce4bcbba3eec9a)MODEM\_ANTTRIG\_PD2

| #define MODEM\_ANTTRIG\_PD2   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x3, 0x2) |
| --- |

## [◆ ](#a132e606271a453be558397a95d72c17e)MODEM\_ANTTRIG\_PD3

| #define MODEM\_ANTTRIG\_PD3   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x3, 0x3) |
| --- |

## [◆ ](#a34eeb11f04820ff36f7730e2a49ffa07)MODEM\_ANTTRIG\_PD4

| #define MODEM\_ANTTRIG\_PD4   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x3, 0x4) |
| --- |

## [◆ ](#ac21df5f70a16ed217b29668eb66b6844)MODEM\_ANTTRIG\_PD5

| #define MODEM\_ANTTRIG\_PD5   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x3, 0x5) |
| --- |

## [◆ ](#af7e05b86331a8d9c02cd27a4e2dc84b7)MODEM\_ANTTRIGSTOP\_PC0

| #define MODEM\_ANTTRIGSTOP\_PC0   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x0) |
| --- |

## [◆ ](#aa658e7c0b2ec76108d710ce93e1d787a)MODEM\_ANTTRIGSTOP\_PC1

| #define MODEM\_ANTTRIGSTOP\_PC1   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x1) |
| --- |

## [◆ ](#a9770ce38a0f236ecd2a7f6cd56e1eff4)MODEM\_ANTTRIGSTOP\_PC2

| #define MODEM\_ANTTRIGSTOP\_PC2   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x2) |
| --- |

## [◆ ](#a61b3ce65ad555f6ad8b69a182626d90e)MODEM\_ANTTRIGSTOP\_PC3

| #define MODEM\_ANTTRIGSTOP\_PC3   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x3) |
| --- |

## [◆ ](#a65384fc71c75bf574740388627bca46f)MODEM\_ANTTRIGSTOP\_PC4

| #define MODEM\_ANTTRIGSTOP\_PC4   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x4) |
| --- |

## [◆ ](#a4c123cd5fca0b4e4e0bc79fbb77292f5)MODEM\_ANTTRIGSTOP\_PC5

| #define MODEM\_ANTTRIGSTOP\_PC5   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x5) |
| --- |

## [◆ ](#a98d91dafafd9175fbdd1074e9526ceaf)MODEM\_ANTTRIGSTOP\_PC6

| #define MODEM\_ANTTRIGSTOP\_PC6   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x6) |
| --- |

## [◆ ](#a26f49d68743f2c7df6e22be7354ffb7f)MODEM\_ANTTRIGSTOP\_PC7

| #define MODEM\_ANTTRIGSTOP\_PC7   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x7) |
| --- |

## [◆ ](#a9ea34515036f5cb0913983c8d5de9a6b)MODEM\_ANTTRIGSTOP\_PC8

| #define MODEM\_ANTTRIGSTOP\_PC8   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x8) |
| --- |

## [◆ ](#a29fa566ce5a4754c4fd809763061c8c6)MODEM\_ANTTRIGSTOP\_PC9

| #define MODEM\_ANTTRIGSTOP\_PC9   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x9) |
| --- |

## [◆ ](#a2689b6b9d9286a13b7b6d2ead8c3993a)MODEM\_ANTTRIGSTOP\_PD0

| #define MODEM\_ANTTRIGSTOP\_PD0   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x3, 0x0) |
| --- |

## [◆ ](#a09410c6d05c79937b0385a8552c292f2)MODEM\_ANTTRIGSTOP\_PD1

| #define MODEM\_ANTTRIGSTOP\_PD1   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x3, 0x1) |
| --- |

## [◆ ](#a413c60ac3ae878a6e4e70e39c6c85fd9)MODEM\_ANTTRIGSTOP\_PD2

| #define MODEM\_ANTTRIGSTOP\_PD2   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x3, 0x2) |
| --- |

## [◆ ](#a20053bb1092ce80cc23cd88aa88fc30d)MODEM\_ANTTRIGSTOP\_PD3

| #define MODEM\_ANTTRIGSTOP\_PD3   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x3, 0x3) |
| --- |

## [◆ ](#ab1007c53ed7798c259ddf55945cd31d1)MODEM\_ANTTRIGSTOP\_PD4

| #define MODEM\_ANTTRIGSTOP\_PD4   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x3, 0x4) |
| --- |

## [◆ ](#ad695401164a6065e3bd39d94098d1dd8)MODEM\_ANTTRIGSTOP\_PD5

| #define MODEM\_ANTTRIGSTOP\_PD5   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x3, 0x5) |
| --- |

## [◆ ](#a08ca0610796eea5484d295a978221196)MODEM\_DCLK\_PA0

| #define MODEM\_DCLK\_PA0   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x0) |
| --- |

## [◆ ](#a405e18321ac14727b470918f185f923c)MODEM\_DCLK\_PA1

| #define MODEM\_DCLK\_PA1   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x1) |
| --- |

## [◆ ](#a2e7d5bc810c26a1194a846663607762d)MODEM\_DCLK\_PA2

| #define MODEM\_DCLK\_PA2   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x2) |
| --- |

## [◆ ](#a483f89509d4d25fe14f3d8cff618289d)MODEM\_DCLK\_PA3

| #define MODEM\_DCLK\_PA3   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x3) |
| --- |

## [◆ ](#a8e3916287d03243cca904f41ce1f9dae)MODEM\_DCLK\_PA4

| #define MODEM\_DCLK\_PA4   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x4) |
| --- |

## [◆ ](#afd75314e866b5c47e838556d866d5883)MODEM\_DCLK\_PA5

| #define MODEM\_DCLK\_PA5   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x5) |
| --- |

## [◆ ](#acf3a1e4e5b714d53ff82edbf02575ec5)MODEM\_DCLK\_PA6

| #define MODEM\_DCLK\_PA6   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x6) |
| --- |

## [◆ ](#ab339753673d17ab957324821a8933d94)MODEM\_DCLK\_PA7

| #define MODEM\_DCLK\_PA7   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x7) |
| --- |

## [◆ ](#a4ffefd11c83ed290890ffb7657507a1e)MODEM\_DCLK\_PA8

| #define MODEM\_DCLK\_PA8   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x8) |
| --- |

## [◆ ](#a786f180681731e9e3819170d4ae306a0)MODEM\_DCLK\_PA9

| #define MODEM\_DCLK\_PA9   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x9) |
| --- |

## [◆ ](#a19236a132524a68b08b88a2b71b74b7b)MODEM\_DCLK\_PB0

| #define MODEM\_DCLK\_PB0   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x1, 0x0) |
| --- |

## [◆ ](#a862abc8858bae8ba0af6b0f8fbbaae37)MODEM\_DCLK\_PB1

| #define MODEM\_DCLK\_PB1   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x1, 0x1) |
| --- |

## [◆ ](#aefcf9c6de61eb621830516b3de6cf348)MODEM\_DCLK\_PB2

| #define MODEM\_DCLK\_PB2   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x1, 0x2) |
| --- |

## [◆ ](#ad15e63bf8718d8705673620a730009c7)MODEM\_DCLK\_PB3

| #define MODEM\_DCLK\_PB3   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x1, 0x3) |
| --- |

## [◆ ](#a76a21531211dfe45e53ceae776c396b6)MODEM\_DCLK\_PB4

| #define MODEM\_DCLK\_PB4   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x1, 0x4) |
| --- |

## [◆ ](#a659fe2d7a1d06ddd921e2d00b5d84efa)MODEM\_DCLK\_PB5

| #define MODEM\_DCLK\_PB5   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x1, 0x5) |
| --- |

## [◆ ](#a3e0e16cfb9e9ad19a8e76e07e458d676)MODEM\_DIN\_PA0

| #define MODEM\_DIN\_PA0   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x0) |
| --- |

## [◆ ](#a3770dcebe1ad3c30c3fbcdcc9e1e61ac)MODEM\_DIN\_PA1

| #define MODEM\_DIN\_PA1   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x1) |
| --- |

## [◆ ](#aed7868ce54670b163ae60f645e353e10)MODEM\_DIN\_PA2

| #define MODEM\_DIN\_PA2   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x2) |
| --- |

## [◆ ](#a55004a63d39356caf5bda66e005a25f3)MODEM\_DIN\_PA3

| #define MODEM\_DIN\_PA3   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x3) |
| --- |

## [◆ ](#a1c13babd5d2f16d4d56257f847e84f40)MODEM\_DIN\_PA4

| #define MODEM\_DIN\_PA4   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x4) |
| --- |

## [◆ ](#a4f09d7e3de2cde036a6ddfcfe35bc96a)MODEM\_DIN\_PA5

| #define MODEM\_DIN\_PA5   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x5) |
| --- |

## [◆ ](#aa310c43126dfd99d7f967141340934c2)MODEM\_DIN\_PA6

| #define MODEM\_DIN\_PA6   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x6) |
| --- |

## [◆ ](#a201de78e9064b3467b2bbdc0a93ae4b2)MODEM\_DIN\_PA7

| #define MODEM\_DIN\_PA7   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x7) |
| --- |

## [◆ ](#a12d5bed446ee0a12698d247f187835ed)MODEM\_DIN\_PA8

| #define MODEM\_DIN\_PA8   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x8) |
| --- |

## [◆ ](#ab53ce7a305b3676b6ff0adb149fc2312)MODEM\_DIN\_PA9

| #define MODEM\_DIN\_PA9   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x9) |
| --- |

## [◆ ](#a87a115f7d2707bf513e218401f2d10fd)MODEM\_DIN\_PB0

| #define MODEM\_DIN\_PB0   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x1, 0x0) |
| --- |

## [◆ ](#a4484f366718daefbdd23d72248a1ba0d)MODEM\_DIN\_PB1

| #define MODEM\_DIN\_PB1   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x1, 0x1) |
| --- |

## [◆ ](#a9513dd16e152b54918b10a3ca7b2bddd)MODEM\_DIN\_PB2

| #define MODEM\_DIN\_PB2   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x1, 0x2) |
| --- |

## [◆ ](#a4ff611638d1c08ae3412e8df31d45e2c)MODEM\_DIN\_PB3

| #define MODEM\_DIN\_PB3   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x1, 0x3) |
| --- |

## [◆ ](#abfd0c609a7621aac4e345fa264776629)MODEM\_DIN\_PB4

| #define MODEM\_DIN\_PB4   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x1, 0x4) |
| --- |

## [◆ ](#a9a3b3307b9ed3b722798678e9c72b842)MODEM\_DIN\_PB5

| #define MODEM\_DIN\_PB5   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x1, 0x5) |
| --- |

## [◆ ](#ac3823581963866285b9f6143d16d9c38)MODEM\_DOUT\_PA0

| #define MODEM\_DOUT\_PA0   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x0) |
| --- |

## [◆ ](#ae4c319e1bba60e4a5a891edf88b1e968)MODEM\_DOUT\_PA1

| #define MODEM\_DOUT\_PA1   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x1) |
| --- |

## [◆ ](#a8dabb728396cf206afac2cfbe49a5b02)MODEM\_DOUT\_PA2

| #define MODEM\_DOUT\_PA2   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x2) |
| --- |

## [◆ ](#ae5963b1e2305ae53f11a90b0d76a99a3)MODEM\_DOUT\_PA3

| #define MODEM\_DOUT\_PA3   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x3) |
| --- |

## [◆ ](#a06061dfed7797c0e29bb9cb5a6d49f88)MODEM\_DOUT\_PA4

| #define MODEM\_DOUT\_PA4   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x4) |
| --- |

## [◆ ](#a117ead5a3ea011c4ad9d37fc96de2bba)MODEM\_DOUT\_PA5

| #define MODEM\_DOUT\_PA5   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x5) |
| --- |

## [◆ ](#aeda2e59bc16dda7ee3d83a2504a04f05)MODEM\_DOUT\_PA6

| #define MODEM\_DOUT\_PA6   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x6) |
| --- |

## [◆ ](#a1d0857025a77fb254ea0e2f7594471f5)MODEM\_DOUT\_PA7

| #define MODEM\_DOUT\_PA7   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x7) |
| --- |

## [◆ ](#a399d0cc64e37dbf683cbcacf14f2d870)MODEM\_DOUT\_PA8

| #define MODEM\_DOUT\_PA8   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x8) |
| --- |

## [◆ ](#ad7f20d72a11d1423459e6a2f5dc9d870)MODEM\_DOUT\_PA9

| #define MODEM\_DOUT\_PA9   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x9) |
| --- |

## [◆ ](#abe0c4060d5f35e9cf8e002676f3c238c)MODEM\_DOUT\_PB0

| #define MODEM\_DOUT\_PB0   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x1, 0x0) |
| --- |

## [◆ ](#aff30fef58eb6dbd17426f7e175c8f4ae)MODEM\_DOUT\_PB1

| #define MODEM\_DOUT\_PB1   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x1, 0x1) |
| --- |

## [◆ ](#ac013e04b2f5d3b419c24f2b1b7f27bad)MODEM\_DOUT\_PB2

| #define MODEM\_DOUT\_PB2   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x1, 0x2) |
| --- |

## [◆ ](#a9011320165978614b4933f9194d45892)MODEM\_DOUT\_PB3

| #define MODEM\_DOUT\_PB3   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x1, 0x3) |
| --- |

## [◆ ](#aabf2e613152cd24a321ad3711cc3c30e)MODEM\_DOUT\_PB4

| #define MODEM\_DOUT\_PB4   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x1, 0x4) |
| --- |

## [◆ ](#ab4d26059a5cc7ebdb19ca77c4bbb4ac7)MODEM\_DOUT\_PB5

| #define MODEM\_DOUT\_PB5   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x1, 0x5) |
| --- |

## [◆ ](#a6f33d3b2bff583fd32a0cdab0b18cb86)PCNT0\_S0IN\_PA0

| #define PCNT0\_S0IN\_PA0   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x0) |
| --- |

## [◆ ](#ae5ac22184b51df9b1e1faafa9533e59c)PCNT0\_S0IN\_PA1

| #define PCNT0\_S0IN\_PA1   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x1) |
| --- |

## [◆ ](#a0604ebad29651279e423afba646dfb58)PCNT0\_S0IN\_PA2

| #define PCNT0\_S0IN\_PA2   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x2) |
| --- |

## [◆ ](#a841091dc34bc7e16418a89190db3b15a)PCNT0\_S0IN\_PA3

| #define PCNT0\_S0IN\_PA3   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x3) |
| --- |

## [◆ ](#ae5fd092cc2df7f9b52ece05e38a217da)PCNT0\_S0IN\_PA4

| #define PCNT0\_S0IN\_PA4   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x4) |
| --- |

## [◆ ](#a95ac0aa1f1af4a615a2dc3c7f9512c83)PCNT0\_S0IN\_PA5

| #define PCNT0\_S0IN\_PA5   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x5) |
| --- |

## [◆ ](#aa8a5beba997a1af2cfd55cc90e62c08a)PCNT0\_S0IN\_PA6

| #define PCNT0\_S0IN\_PA6   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x6) |
| --- |

## [◆ ](#a9e69a57169a3e1698c8980dfe3189705)PCNT0\_S0IN\_PA7

| #define PCNT0\_S0IN\_PA7   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x7) |
| --- |

## [◆ ](#a07910d5ea15530f07109f589a71b1a35)PCNT0\_S0IN\_PA8

| #define PCNT0\_S0IN\_PA8   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x8) |
| --- |

## [◆ ](#a9459850934983e2f7a2521f7f06d2e4c)PCNT0\_S0IN\_PA9

| #define PCNT0\_S0IN\_PA9   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x0, 0x9) |
| --- |

## [◆ ](#a9ff535d912f08e887963a392bd377247)PCNT0\_S0IN\_PB0

| #define PCNT0\_S0IN\_PB0   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x1, 0x0) |
| --- |

## [◆ ](#a305fa64123cc206b67fabbd020a4b665)PCNT0\_S0IN\_PB1

| #define PCNT0\_S0IN\_PB1   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x1, 0x1) |
| --- |

## [◆ ](#a3d91c6a4cc9fb9819912e33b9fa9d190)PCNT0\_S0IN\_PB2

| #define PCNT0\_S0IN\_PB2   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x1, 0x2) |
| --- |

## [◆ ](#a37ddc5da1d667f70a626d61f6831f4e1)PCNT0\_S0IN\_PB3

| #define PCNT0\_S0IN\_PB3   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x1, 0x3) |
| --- |

## [◆ ](#a223a1fc3d272027257b9023233a0fe7d)PCNT0\_S0IN\_PB4

| #define PCNT0\_S0IN\_PB4   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x1, 0x4) |
| --- |

## [◆ ](#a94df2d91a7055e2a0a05f9ebaa188922)PCNT0\_S0IN\_PB5

| #define PCNT0\_S0IN\_PB5   [SILABS\_DBUS\_PCNT0\_S0IN](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)(0x1, 0x5) |
| --- |

## [◆ ](#a7225c02a0bf7ac0257d56326403e00f5)PCNT0\_S1IN\_PA0

| #define PCNT0\_S1IN\_PA0   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x0) |
| --- |

## [◆ ](#a2bf0eec0a8e51aca6df3956edcc5af02)PCNT0\_S1IN\_PA1

| #define PCNT0\_S1IN\_PA1   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x1) |
| --- |

## [◆ ](#aed7e3df711ccdd37ced4405246867b41)PCNT0\_S1IN\_PA2

| #define PCNT0\_S1IN\_PA2   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x2) |
| --- |

## [◆ ](#a0fc69216ccf38893b398e20795b45203)PCNT0\_S1IN\_PA3

| #define PCNT0\_S1IN\_PA3   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x3) |
| --- |

## [◆ ](#a9b18d46d7c00f9440ae6ead1f7071bbb)PCNT0\_S1IN\_PA4

| #define PCNT0\_S1IN\_PA4   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x4) |
| --- |

## [◆ ](#acec4b827bd7ab080e1f770ce064b0f60)PCNT0\_S1IN\_PA5

| #define PCNT0\_S1IN\_PA5   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x5) |
| --- |

## [◆ ](#ad9267387f1c65fcdaf368bca61f26db6)PCNT0\_S1IN\_PA6

| #define PCNT0\_S1IN\_PA6   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x6) |
| --- |

## [◆ ](#ad652d68108d9c607b8f210ddcf830694)PCNT0\_S1IN\_PA7

| #define PCNT0\_S1IN\_PA7   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x7) |
| --- |

## [◆ ](#ab8ad1e725b2ba90915ba35e8494b6804)PCNT0\_S1IN\_PA8

| #define PCNT0\_S1IN\_PA8   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x8) |
| --- |

## [◆ ](#aa97493aef428388b49c5cb0dafd83474)PCNT0\_S1IN\_PA9

| #define PCNT0\_S1IN\_PA9   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x0, 0x9) |
| --- |

## [◆ ](#a9d9e33c9279d6bf9ec430d655fa0b4ac)PCNT0\_S1IN\_PB0

| #define PCNT0\_S1IN\_PB0   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x1, 0x0) |
| --- |

## [◆ ](#ae663132285843f7983adf5f0a3dec3cd)PCNT0\_S1IN\_PB1

| #define PCNT0\_S1IN\_PB1   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x1, 0x1) |
| --- |

## [◆ ](#a7895b597ddbea56c1ea51ea9361a7c0e)PCNT0\_S1IN\_PB2

| #define PCNT0\_S1IN\_PB2   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x1, 0x2) |
| --- |

## [◆ ](#a63821a509b711209d91ebc80553db2cb)PCNT0\_S1IN\_PB3

| #define PCNT0\_S1IN\_PB3   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x1, 0x3) |
| --- |

## [◆ ](#a11a9f343a105826bc90054c8d8cb220c)PCNT0\_S1IN\_PB4

| #define PCNT0\_S1IN\_PB4   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x1, 0x4) |
| --- |

## [◆ ](#a084532ef7c32bd35298aeabf0b3f376b)PCNT0\_S1IN\_PB5

| #define PCNT0\_S1IN\_PB5   [SILABS\_DBUS\_PCNT0\_S1IN](#ab083a5eb205a0db7773d74aa506cb8bd)(0x1, 0x5) |
| --- |

## [◆ ](#af1dcdc8d0ea9b8671a240ce03d80d434)PRS0\_ASYNCH0\_PA0

| #define PRS0\_ASYNCH0\_PA0   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x0) |
| --- |

## [◆ ](#af712c40bafb6ba29d062f47a47ef4445)PRS0\_ASYNCH0\_PA1

| #define PRS0\_ASYNCH0\_PA1   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x1) |
| --- |

## [◆ ](#a4a95bfd98958b7944ef58c010df91d83)PRS0\_ASYNCH0\_PA2

| #define PRS0\_ASYNCH0\_PA2   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x2) |
| --- |

## [◆ ](#ab912f56311db65e5316e921180f46589)PRS0\_ASYNCH0\_PA3

| #define PRS0\_ASYNCH0\_PA3   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x3) |
| --- |

## [◆ ](#ac1e05749654ec2bee09aa75a951bcd57)PRS0\_ASYNCH0\_PA4

| #define PRS0\_ASYNCH0\_PA4   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x4) |
| --- |

## [◆ ](#a15788b1a1cdce57fddf0d58e884e37bc)PRS0\_ASYNCH0\_PA5

| #define PRS0\_ASYNCH0\_PA5   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x5) |
| --- |

## [◆ ](#af071c0ad0ca5a54d74c7fa4e2f7eea6c)PRS0\_ASYNCH0\_PA6

| #define PRS0\_ASYNCH0\_PA6   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x6) |
| --- |

## [◆ ](#accc5ad5ffa51459772c03387f67f6db1)PRS0\_ASYNCH0\_PA7

| #define PRS0\_ASYNCH0\_PA7   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x7) |
| --- |

## [◆ ](#af170d0ff0c56bdf3bd13eaa00f2f3fea)PRS0\_ASYNCH0\_PA8

| #define PRS0\_ASYNCH0\_PA8   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x8) |
| --- |

## [◆ ](#aabb6361fee457b8d9f787e1333ee340b)PRS0\_ASYNCH0\_PA9

| #define PRS0\_ASYNCH0\_PA9   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x9) |
| --- |

## [◆ ](#a590472d980647bc2a513ee516c9c4f1b)PRS0\_ASYNCH0\_PB0

| #define PRS0\_ASYNCH0\_PB0   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x1, 0x0) |
| --- |

## [◆ ](#af4ee1a5d6ccadd510de798cf41f973ee)PRS0\_ASYNCH0\_PB1

| #define PRS0\_ASYNCH0\_PB1   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x1, 0x1) |
| --- |

## [◆ ](#a0517d6b5213d9f8ebfb445e7aa0cf2e7)PRS0\_ASYNCH0\_PB2

| #define PRS0\_ASYNCH0\_PB2   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x1, 0x2) |
| --- |

## [◆ ](#a0b229da2aec9ffb51c50e0ca19e1a45d)PRS0\_ASYNCH0\_PB3

| #define PRS0\_ASYNCH0\_PB3   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x1, 0x3) |
| --- |

## [◆ ](#a281aa5d676ea7ac358df567ab98663b3)PRS0\_ASYNCH0\_PB4

| #define PRS0\_ASYNCH0\_PB4   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x1, 0x4) |
| --- |

## [◆ ](#abfeaa99e158b38cae62b01dfcd7338ab)PRS0\_ASYNCH0\_PB5

| #define PRS0\_ASYNCH0\_PB5   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x1, 0x5) |
| --- |

## [◆ ](#af096e7ffddaaf21a0886246861e94cf0)PRS0\_ASYNCH10\_PC0

| #define PRS0\_ASYNCH10\_PC0   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x0) |
| --- |

## [◆ ](#ab2e7c25b6faf577e7ee8197ae806a979)PRS0\_ASYNCH10\_PC1

| #define PRS0\_ASYNCH10\_PC1   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x1) |
| --- |

## [◆ ](#a22dd84a911044fe555ee09be1ee255e6)PRS0\_ASYNCH10\_PC2

| #define PRS0\_ASYNCH10\_PC2   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x2) |
| --- |

## [◆ ](#a4285722719da53788c48b4fc1f563e78)PRS0\_ASYNCH10\_PC3

| #define PRS0\_ASYNCH10\_PC3   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x3) |
| --- |

## [◆ ](#a5fde4317aee5f5e514d31b0a02013e85)PRS0\_ASYNCH10\_PC4

| #define PRS0\_ASYNCH10\_PC4   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x4) |
| --- |

## [◆ ](#ac3e04e87a2e22a0e5852c25cd42f5bfd)PRS0\_ASYNCH10\_PC5

| #define PRS0\_ASYNCH10\_PC5   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x5) |
| --- |

## [◆ ](#a112632637b58df9fa0b0f1a4090f4360)PRS0\_ASYNCH10\_PC6

| #define PRS0\_ASYNCH10\_PC6   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x6) |
| --- |

## [◆ ](#abe1145f2e2eb3620f7329a03e66f0a5b)PRS0\_ASYNCH10\_PC7

| #define PRS0\_ASYNCH10\_PC7   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x7) |
| --- |

## [◆ ](#ac322660bf45aae79d9dfc97d4855ab61)PRS0\_ASYNCH10\_PC8

| #define PRS0\_ASYNCH10\_PC8   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x8) |
| --- |

## [◆ ](#a194bca6a084988c323ae32c17ad9e148)PRS0\_ASYNCH10\_PC9

| #define PRS0\_ASYNCH10\_PC9   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x9) |
| --- |

## [◆ ](#a86d5340c5133d3193351104663683d0e)PRS0\_ASYNCH10\_PD0

| #define PRS0\_ASYNCH10\_PD0   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x3, 0x0) |
| --- |

## [◆ ](#a00af6bec878e4ea3f6ff297ac35f91ed)PRS0\_ASYNCH10\_PD1

| #define PRS0\_ASYNCH10\_PD1   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x3, 0x1) |
| --- |

## [◆ ](#a0117d03759e58b8a40f3e32e65c1daff)PRS0\_ASYNCH10\_PD2

| #define PRS0\_ASYNCH10\_PD2   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x3, 0x2) |
| --- |

## [◆ ](#ac26c97f76181aa0d4d334061599e549b)PRS0\_ASYNCH10\_PD3

| #define PRS0\_ASYNCH10\_PD3   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x3, 0x3) |
| --- |

## [◆ ](#a56d5659d935d78961dd5ab8f56af296b)PRS0\_ASYNCH10\_PD4

| #define PRS0\_ASYNCH10\_PD4   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x3, 0x4) |
| --- |

## [◆ ](#aa527f2dea4ccab311915bcd310ae062f)PRS0\_ASYNCH10\_PD5

| #define PRS0\_ASYNCH10\_PD5   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x3, 0x5) |
| --- |

## [◆ ](#a1ba16c8c6da7e3129c03eb546df4c993)PRS0\_ASYNCH11\_PC0

| #define PRS0\_ASYNCH11\_PC0   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x0) |
| --- |

## [◆ ](#a4780077af0f3eac79ac458382dfdd9ce)PRS0\_ASYNCH11\_PC1

| #define PRS0\_ASYNCH11\_PC1   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x1) |
| --- |

## [◆ ](#a32ed7a6cd5db3336ee370d6cf9d8e989)PRS0\_ASYNCH11\_PC2

| #define PRS0\_ASYNCH11\_PC2   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x2) |
| --- |

## [◆ ](#ada09802928473e1a5360709b259ce87e)PRS0\_ASYNCH11\_PC3

| #define PRS0\_ASYNCH11\_PC3   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x3) |
| --- |

## [◆ ](#aa83823870ce109c570db56a0d7bf4197)PRS0\_ASYNCH11\_PC4

| #define PRS0\_ASYNCH11\_PC4   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x4) |
| --- |

## [◆ ](#a06db00a9ba09d6f16e8ab4423b98edb8)PRS0\_ASYNCH11\_PC5

| #define PRS0\_ASYNCH11\_PC5   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x5) |
| --- |

## [◆ ](#abf891c76454cd7dcccf81062e03e49c0)PRS0\_ASYNCH11\_PC6

| #define PRS0\_ASYNCH11\_PC6   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x6) |
| --- |

## [◆ ](#ac19cc8092d5117eac5d57e0b9ef75408)PRS0\_ASYNCH11\_PC7

| #define PRS0\_ASYNCH11\_PC7   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x7) |
| --- |

## [◆ ](#a110c98c7774b500a68ec08d99654812a)PRS0\_ASYNCH11\_PC8

| #define PRS0\_ASYNCH11\_PC8   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x8) |
| --- |

## [◆ ](#a56db9c74fb03262f83f575b15e6041ba)PRS0\_ASYNCH11\_PC9

| #define PRS0\_ASYNCH11\_PC9   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x9) |
| --- |

## [◆ ](#a4d64f2e728e07b761372b682a6732ea9)PRS0\_ASYNCH11\_PD0

| #define PRS0\_ASYNCH11\_PD0   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x3, 0x0) |
| --- |

## [◆ ](#aa62c6365ff4d4c6e9ac8952c9bc50d1d)PRS0\_ASYNCH11\_PD1

| #define PRS0\_ASYNCH11\_PD1   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x3, 0x1) |
| --- |

## [◆ ](#a6d8321e7ba25db410748817cd169d45a)PRS0\_ASYNCH11\_PD2

| #define PRS0\_ASYNCH11\_PD2   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x3, 0x2) |
| --- |

## [◆ ](#aafe8d7f49fead257b9a5065f68727c1a)PRS0\_ASYNCH11\_PD3

| #define PRS0\_ASYNCH11\_PD3   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x3, 0x3) |
| --- |

## [◆ ](#a8e5caa0af696c8dc3445350a1f11cf45)PRS0\_ASYNCH11\_PD4

| #define PRS0\_ASYNCH11\_PD4   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x3, 0x4) |
| --- |

## [◆ ](#a09b6b220b72d01845d9e5ebf17f7d07a)PRS0\_ASYNCH11\_PD5

| #define PRS0\_ASYNCH11\_PD5   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x3, 0x5) |
| --- |

## [◆ ](#a10aacd21afb9491740ad75536204af47)PRS0\_ASYNCH12\_PA0

| #define PRS0\_ASYNCH12\_PA0   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x0) |
| --- |

## [◆ ](#a0f5547f8b6e433bb489d3802cc2f54ee)PRS0\_ASYNCH12\_PA1

| #define PRS0\_ASYNCH12\_PA1   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x1) |
| --- |

## [◆ ](#a8c7c23cb0e9bfe0d3abbbfb4647c619f)PRS0\_ASYNCH12\_PA2

| #define PRS0\_ASYNCH12\_PA2   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x2) |
| --- |

## [◆ ](#a0a0ab32d5093e5ec80f9bbbabcaccecb)PRS0\_ASYNCH12\_PA3

| #define PRS0\_ASYNCH12\_PA3   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x3) |
| --- |

## [◆ ](#a07610c348913142d48f24cbf80748159)PRS0\_ASYNCH12\_PA4

| #define PRS0\_ASYNCH12\_PA4   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x4) |
| --- |

## [◆ ](#a91ed32dc798b252b2117e8c84fc26631)PRS0\_ASYNCH12\_PA5

| #define PRS0\_ASYNCH12\_PA5   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x5) |
| --- |

## [◆ ](#a272eed302053d41c214077eee7b64720)PRS0\_ASYNCH12\_PA6

| #define PRS0\_ASYNCH12\_PA6   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x6) |
| --- |

## [◆ ](#ae90459802859961117786b795abdfb59)PRS0\_ASYNCH12\_PA7

| #define PRS0\_ASYNCH12\_PA7   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x7) |
| --- |

## [◆ ](#a3c1b4709507d6b1f400f749b052cc91e)PRS0\_ASYNCH12\_PA8

| #define PRS0\_ASYNCH12\_PA8   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x8) |
| --- |

## [◆ ](#af2fd8d924c3441d1018d8570858d0def)PRS0\_ASYNCH12\_PA9

| #define PRS0\_ASYNCH12\_PA9   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x0, 0x9) |
| --- |

## [◆ ](#ab83cbe92b306386bbb4407065dfadcc5)PRS0\_ASYNCH12\_PB0

| #define PRS0\_ASYNCH12\_PB0   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x1, 0x0) |
| --- |

## [◆ ](#a921c83b51c6c31b46c62858f3be92c02)PRS0\_ASYNCH12\_PB1

| #define PRS0\_ASYNCH12\_PB1   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x1, 0x1) |
| --- |

## [◆ ](#abf3db716f8c5dbfebbf271206a405ba4)PRS0\_ASYNCH12\_PB2

| #define PRS0\_ASYNCH12\_PB2   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x1, 0x2) |
| --- |

## [◆ ](#a1f17a507786154e23b1741d0262aa504)PRS0\_ASYNCH12\_PB3

| #define PRS0\_ASYNCH12\_PB3   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x1, 0x3) |
| --- |

## [◆ ](#a797d2617d88745b9ab6536e80c76b1c8)PRS0\_ASYNCH12\_PB4

| #define PRS0\_ASYNCH12\_PB4   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x1, 0x4) |
| --- |

## [◆ ](#a449120ce58891824a1372319bd857932)PRS0\_ASYNCH12\_PB5

| #define PRS0\_ASYNCH12\_PB5   [SILABS\_DBUS\_PRS0\_ASYNCH12](#a242292a4e61aa48e75fde0fe4d079f8c)(0x1, 0x5) |
| --- |

## [◆ ](#a550ee44aff84f53b7f368cc358222569)PRS0\_ASYNCH13\_PA0

| #define PRS0\_ASYNCH13\_PA0   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x0) |
| --- |

## [◆ ](#a6b3b72ec6c37a633e858555be9d741cb)PRS0\_ASYNCH13\_PA1

| #define PRS0\_ASYNCH13\_PA1   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x1) |
| --- |

## [◆ ](#a305b6d5056b0caabf68ed88a5a053a97)PRS0\_ASYNCH13\_PA2

| #define PRS0\_ASYNCH13\_PA2   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x2) |
| --- |

## [◆ ](#af98fa87e2143f31dffe610a72a06d3d7)PRS0\_ASYNCH13\_PA3

| #define PRS0\_ASYNCH13\_PA3   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x3) |
| --- |

## [◆ ](#ab8ccfba67837dde10457210e5f1c297a)PRS0\_ASYNCH13\_PA4

| #define PRS0\_ASYNCH13\_PA4   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x4) |
| --- |

## [◆ ](#aa7d5640b3bd5a0d4d2467ec3ce9abdcb)PRS0\_ASYNCH13\_PA5

| #define PRS0\_ASYNCH13\_PA5   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x5) |
| --- |

## [◆ ](#a0906b42ac77f924116d258c7a769b685)PRS0\_ASYNCH13\_PA6

| #define PRS0\_ASYNCH13\_PA6   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x6) |
| --- |

## [◆ ](#a9e74ccf92743c1b61335148b3a98cd77)PRS0\_ASYNCH13\_PA7

| #define PRS0\_ASYNCH13\_PA7   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x7) |
| --- |

## [◆ ](#adc726e9153975c1786f436ca7ddd0474)PRS0\_ASYNCH13\_PA8

| #define PRS0\_ASYNCH13\_PA8   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x8) |
| --- |

## [◆ ](#a41887405f8190f76c720346e87ea2b74)PRS0\_ASYNCH13\_PA9

| #define PRS0\_ASYNCH13\_PA9   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x0, 0x9) |
| --- |

## [◆ ](#a9969cb5e529162e9a1a3fd5f30d478d5)PRS0\_ASYNCH13\_PB0

| #define PRS0\_ASYNCH13\_PB0   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x1, 0x0) |
| --- |

## [◆ ](#ac63069b8115b299ae6bb625644a245db)PRS0\_ASYNCH13\_PB1

| #define PRS0\_ASYNCH13\_PB1   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x1, 0x1) |
| --- |

## [◆ ](#aba2942821c775b1b2682b0ec06e43d87)PRS0\_ASYNCH13\_PB2

| #define PRS0\_ASYNCH13\_PB2   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x1, 0x2) |
| --- |

## [◆ ](#a09eccaaa1fd092b0a95cb50ee5ef3cd3)PRS0\_ASYNCH13\_PB3

| #define PRS0\_ASYNCH13\_PB3   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x1, 0x3) |
| --- |

## [◆ ](#a6542baa6e14878b554061e2e99dd0006)PRS0\_ASYNCH13\_PB4

| #define PRS0\_ASYNCH13\_PB4   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x1, 0x4) |
| --- |

## [◆ ](#a10907dbd3b54c45e60b98c394c9a10b7)PRS0\_ASYNCH13\_PB5

| #define PRS0\_ASYNCH13\_PB5   [SILABS\_DBUS\_PRS0\_ASYNCH13](#a147c1004a0bb3cb7a3b4577081362d8d)(0x1, 0x5) |
| --- |

## [◆ ](#a73fcba463211ef0886a60b7414b59c6f)PRS0\_ASYNCH14\_PA0

| #define PRS0\_ASYNCH14\_PA0   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x0) |
| --- |

## [◆ ](#a78c2478d7e52c12eac37098b4bf8f7f6)PRS0\_ASYNCH14\_PA1

| #define PRS0\_ASYNCH14\_PA1   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x1) |
| --- |

## [◆ ](#ad37be4d15fc3753f4025897dc9d99cd9)PRS0\_ASYNCH14\_PA2

| #define PRS0\_ASYNCH14\_PA2   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x2) |
| --- |

## [◆ ](#a5412d1e5a08b3d1157ce3d190414e4cd)PRS0\_ASYNCH14\_PA3

| #define PRS0\_ASYNCH14\_PA3   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x3) |
| --- |

## [◆ ](#acf062f80109a4dd8cd9b91a9b7322743)PRS0\_ASYNCH14\_PA4

| #define PRS0\_ASYNCH14\_PA4   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x4) |
| --- |

## [◆ ](#a989a7b01e77cb258df5882957c813d2f)PRS0\_ASYNCH14\_PA5

| #define PRS0\_ASYNCH14\_PA5   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x5) |
| --- |

## [◆ ](#a220f5415ec1ccc603b97d22d80a654f2)PRS0\_ASYNCH14\_PA6

| #define PRS0\_ASYNCH14\_PA6   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x6) |
| --- |

## [◆ ](#af68b224ede411b9145e953af0619d32a)PRS0\_ASYNCH14\_PA7

| #define PRS0\_ASYNCH14\_PA7   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x7) |
| --- |

## [◆ ](#ac7e7a030a8fc81faddffdcd77f66707b)PRS0\_ASYNCH14\_PA8

| #define PRS0\_ASYNCH14\_PA8   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x8) |
| --- |

## [◆ ](#afbb45b1487696d98f875f4a168a485e5)PRS0\_ASYNCH14\_PA9

| #define PRS0\_ASYNCH14\_PA9   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x0, 0x9) |
| --- |

## [◆ ](#a425101e0c4768eb96759828051fdbce6)PRS0\_ASYNCH14\_PB0

| #define PRS0\_ASYNCH14\_PB0   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x1, 0x0) |
| --- |

## [◆ ](#a7c9726953c4d6948ad020828ebf99f4e)PRS0\_ASYNCH14\_PB1

| #define PRS0\_ASYNCH14\_PB1   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x1, 0x1) |
| --- |

## [◆ ](#aadbdd407c7067db273e38512b1d7d2a5)PRS0\_ASYNCH14\_PB2

| #define PRS0\_ASYNCH14\_PB2   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x1, 0x2) |
| --- |

## [◆ ](#a3f3d95d09d7ee0abb27fbfbfc33c3398)PRS0\_ASYNCH14\_PB3

| #define PRS0\_ASYNCH14\_PB3   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x1, 0x3) |
| --- |

## [◆ ](#ab41d1ee71db4b2f716586c42e26ce0c0)PRS0\_ASYNCH14\_PB4

| #define PRS0\_ASYNCH14\_PB4   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x1, 0x4) |
| --- |

## [◆ ](#ab3f36548a4f6c955344567dcd6176c69)PRS0\_ASYNCH14\_PB5

| #define PRS0\_ASYNCH14\_PB5   [SILABS\_DBUS\_PRS0\_ASYNCH14](#aeea99277adc04a38c1ed7adf6120c8f6)(0x1, 0x5) |
| --- |

## [◆ ](#a1c4013acfa21c77182df39165729a351)PRS0\_ASYNCH15\_PA0

| #define PRS0\_ASYNCH15\_PA0   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x0) |
| --- |

## [◆ ](#a2a2ee681ddbc8967b87e3060c7f41adb)PRS0\_ASYNCH15\_PA1

| #define PRS0\_ASYNCH15\_PA1   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x1) |
| --- |

## [◆ ](#a47b6621fc06df0a7ca9d3e7f6a694950)PRS0\_ASYNCH15\_PA2

| #define PRS0\_ASYNCH15\_PA2   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x2) |
| --- |

## [◆ ](#abaa53f0e9ad81a391406459411e68bae)PRS0\_ASYNCH15\_PA3

| #define PRS0\_ASYNCH15\_PA3   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x3) |
| --- |

## [◆ ](#a2e273906005064680a1682fc7af9ed46)PRS0\_ASYNCH15\_PA4

| #define PRS0\_ASYNCH15\_PA4   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x4) |
| --- |

## [◆ ](#ae5520676b7309658fd3c98e3fab0a94b)PRS0\_ASYNCH15\_PA5

| #define PRS0\_ASYNCH15\_PA5   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x5) |
| --- |

## [◆ ](#a2e1dd8e0287f670aaae04eeee24d2900)PRS0\_ASYNCH15\_PA6

| #define PRS0\_ASYNCH15\_PA6   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x6) |
| --- |

## [◆ ](#aa9f87aa222cbf925208efdc1dbb993fc)PRS0\_ASYNCH15\_PA7

| #define PRS0\_ASYNCH15\_PA7   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x7) |
| --- |

## [◆ ](#a44bb6cf5cf586aee06ad5355cbcc4d92)PRS0\_ASYNCH15\_PA8

| #define PRS0\_ASYNCH15\_PA8   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x8) |
| --- |

## [◆ ](#a99a844d50090c54d2a74f6fcd3714b3c)PRS0\_ASYNCH15\_PA9

| #define PRS0\_ASYNCH15\_PA9   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x0, 0x9) |
| --- |

## [◆ ](#ab67d37a6ae0ff2fd14f3f7805cbae585)PRS0\_ASYNCH15\_PB0

| #define PRS0\_ASYNCH15\_PB0   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x1, 0x0) |
| --- |

## [◆ ](#a41a6ff0b05882aa37aed79ea693a26bf)PRS0\_ASYNCH15\_PB1

| #define PRS0\_ASYNCH15\_PB1   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x1, 0x1) |
| --- |

## [◆ ](#aea795286053e3cd00be0a2ec5fa2125d)PRS0\_ASYNCH15\_PB2

| #define PRS0\_ASYNCH15\_PB2   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x1, 0x2) |
| --- |

## [◆ ](#af4ef7cc6eb3c8dc0bf191f87b3689d36)PRS0\_ASYNCH15\_PB3

| #define PRS0\_ASYNCH15\_PB3   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x1, 0x3) |
| --- |

## [◆ ](#a6e7505cfce669cf337cad3a06409a9ed)PRS0\_ASYNCH15\_PB4

| #define PRS0\_ASYNCH15\_PB4   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x1, 0x4) |
| --- |

## [◆ ](#a993a29e36de209eabac71d2fa3b581f8)PRS0\_ASYNCH15\_PB5

| #define PRS0\_ASYNCH15\_PB5   [SILABS\_DBUS\_PRS0\_ASYNCH15](#a2b0d1abf6d9dda91662191f12e941574)(0x1, 0x5) |
| --- |

## [◆ ](#aa7c8c749fddaf4b2e22e3791d9e8921a)PRS0\_ASYNCH1\_PA0

| #define PRS0\_ASYNCH1\_PA0   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x0) |
| --- |

## [◆ ](#a8f998569835e3b8688423cf9b4e81810)PRS0\_ASYNCH1\_PA1

| #define PRS0\_ASYNCH1\_PA1   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x1) |
| --- |

## [◆ ](#a5f2d980e4505820849c42fdc36c1b5a9)PRS0\_ASYNCH1\_PA2

| #define PRS0\_ASYNCH1\_PA2   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x2) |
| --- |

## [◆ ](#a4b66d13c4589bb2663661e6cfb8c0274)PRS0\_ASYNCH1\_PA3

| #define PRS0\_ASYNCH1\_PA3   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x3) |
| --- |

## [◆ ](#aec6f34dc1716b25b0fcc0628b18cbf86)PRS0\_ASYNCH1\_PA4

| #define PRS0\_ASYNCH1\_PA4   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x4) |
| --- |

## [◆ ](#a0be6148e1124f7e8dc6773f59dfd8ceb)PRS0\_ASYNCH1\_PA5

| #define PRS0\_ASYNCH1\_PA5   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x5) |
| --- |

## [◆ ](#a4d1894b5f84e0e7c81a5dbb2bfe8318f)PRS0\_ASYNCH1\_PA6

| #define PRS0\_ASYNCH1\_PA6   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x6) |
| --- |

## [◆ ](#a95455187a1575a8e8249d1e4178131c5)PRS0\_ASYNCH1\_PA7

| #define PRS0\_ASYNCH1\_PA7   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x7) |
| --- |

## [◆ ](#a85428a0cef95ef5674719cfbac44eed5)PRS0\_ASYNCH1\_PA8

| #define PRS0\_ASYNCH1\_PA8   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x8) |
| --- |

## [◆ ](#ad6db6ce8273bbd9701f7e0880973d395)PRS0\_ASYNCH1\_PA9

| #define PRS0\_ASYNCH1\_PA9   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x9) |
| --- |

## [◆ ](#a76487417602321711041f2d5d721e8ae)PRS0\_ASYNCH1\_PB0

| #define PRS0\_ASYNCH1\_PB0   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x1, 0x0) |
| --- |

## [◆ ](#a1626bdc4551620aaccbfacd8aa0c0cdf)PRS0\_ASYNCH1\_PB1

| #define PRS0\_ASYNCH1\_PB1   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x1, 0x1) |
| --- |

## [◆ ](#ac68d7c6b3b4607a2eb07926ceb42b0b3)PRS0\_ASYNCH1\_PB2

| #define PRS0\_ASYNCH1\_PB2   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x1, 0x2) |
| --- |

## [◆ ](#a5b843903080dcfb8d654248f04b56bb1)PRS0\_ASYNCH1\_PB3

| #define PRS0\_ASYNCH1\_PB3   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x1, 0x3) |
| --- |

## [◆ ](#ae1a66f7dff2089736cc20cee277a5cd4)PRS0\_ASYNCH1\_PB4

| #define PRS0\_ASYNCH1\_PB4   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x1, 0x4) |
| --- |

## [◆ ](#aa2b7e3b1f891e86d34ef2faed3bde83c)PRS0\_ASYNCH1\_PB5

| #define PRS0\_ASYNCH1\_PB5   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x1, 0x5) |
| --- |

## [◆ ](#ab9115b54fff36f0449722af1659860fb)PRS0\_ASYNCH2\_PA0

| #define PRS0\_ASYNCH2\_PA0   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x0) |
| --- |

## [◆ ](#a82e86536168f11e5b02c4fac703128b1)PRS0\_ASYNCH2\_PA1

| #define PRS0\_ASYNCH2\_PA1   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x1) |
| --- |

## [◆ ](#af3124f46d26efbb18047172d5d5accbc)PRS0\_ASYNCH2\_PA2

| #define PRS0\_ASYNCH2\_PA2   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x2) |
| --- |

## [◆ ](#a57857d486b2fc1db0770a7d1e198ed95)PRS0\_ASYNCH2\_PA3

| #define PRS0\_ASYNCH2\_PA3   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x3) |
| --- |

## [◆ ](#a3d91108c838d4684846d56816aee5fe1)PRS0\_ASYNCH2\_PA4

| #define PRS0\_ASYNCH2\_PA4   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x4) |
| --- |

## [◆ ](#a8e7b151ff1870ccfc66a34096b4aebae)PRS0\_ASYNCH2\_PA5

| #define PRS0\_ASYNCH2\_PA5   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x5) |
| --- |

## [◆ ](#a7f536e8d1d66285820ab8e3808e49a0f)PRS0\_ASYNCH2\_PA6

| #define PRS0\_ASYNCH2\_PA6   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x6) |
| --- |

## [◆ ](#a41efde6eb746e07baf306e05197a8948)PRS0\_ASYNCH2\_PA7

| #define PRS0\_ASYNCH2\_PA7   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x7) |
| --- |

## [◆ ](#a95b452fe92602af5bff499d14f1cae11)PRS0\_ASYNCH2\_PA8

| #define PRS0\_ASYNCH2\_PA8   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x8) |
| --- |

## [◆ ](#ae90ff17ea0c75c4e35b2f7fdfe87260f)PRS0\_ASYNCH2\_PA9

| #define PRS0\_ASYNCH2\_PA9   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x9) |
| --- |

## [◆ ](#a81bf0662053265b1d9cc03c101d4a353)PRS0\_ASYNCH2\_PB0

| #define PRS0\_ASYNCH2\_PB0   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x1, 0x0) |
| --- |

## [◆ ](#a026322616f156126afcbcebc25d104c0)PRS0\_ASYNCH2\_PB1

| #define PRS0\_ASYNCH2\_PB1   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x1, 0x1) |
| --- |

## [◆ ](#a6a39b350109c932587f1c1623898d178)PRS0\_ASYNCH2\_PB2

| #define PRS0\_ASYNCH2\_PB2   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x1, 0x2) |
| --- |

## [◆ ](#a30b84121b903ca053238c3a1110fd247)PRS0\_ASYNCH2\_PB3

| #define PRS0\_ASYNCH2\_PB3   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x1, 0x3) |
| --- |

## [◆ ](#a68e5aa33a7ccd7af8abe83550bc9fcf2)PRS0\_ASYNCH2\_PB4

| #define PRS0\_ASYNCH2\_PB4   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x1, 0x4) |
| --- |

## [◆ ](#ad6152fcacafb28c981e8f349557fcc43)PRS0\_ASYNCH2\_PB5

| #define PRS0\_ASYNCH2\_PB5   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x1, 0x5) |
| --- |

## [◆ ](#a94b5b779374768ed16ad8cc396f756aa)PRS0\_ASYNCH3\_PA0

| #define PRS0\_ASYNCH3\_PA0   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x0) |
| --- |

## [◆ ](#aa947bb280b4891081e7a4de9dba44ae5)PRS0\_ASYNCH3\_PA1

| #define PRS0\_ASYNCH3\_PA1   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x1) |
| --- |

## [◆ ](#a9bc4d14c37fd2724643735c13cc9a25d)PRS0\_ASYNCH3\_PA2

| #define PRS0\_ASYNCH3\_PA2   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x2) |
| --- |

## [◆ ](#afa101472245a7df51d906f31093ce640)PRS0\_ASYNCH3\_PA3

| #define PRS0\_ASYNCH3\_PA3   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x3) |
| --- |

## [◆ ](#a1e433ac2a9a5c1b9240b157033e8fdc1)PRS0\_ASYNCH3\_PA4

| #define PRS0\_ASYNCH3\_PA4   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x4) |
| --- |

## [◆ ](#a4af0e3dc3303ec055fcce97399ccf4ba)PRS0\_ASYNCH3\_PA5

| #define PRS0\_ASYNCH3\_PA5   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x5) |
| --- |

## [◆ ](#ad905e3cca4ec1b92f1fd6b0ca18b8c06)PRS0\_ASYNCH3\_PA6

| #define PRS0\_ASYNCH3\_PA6   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x6) |
| --- |

## [◆ ](#a64d14cae622fb5814402d3bf6c042a47)PRS0\_ASYNCH3\_PA7

| #define PRS0\_ASYNCH3\_PA7   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x7) |
| --- |

## [◆ ](#a0ceb4585c15bf959906dd93aed744f0d)PRS0\_ASYNCH3\_PA8

| #define PRS0\_ASYNCH3\_PA8   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x8) |
| --- |

## [◆ ](#ae48735563ea7be3be49285f230231bf3)PRS0\_ASYNCH3\_PA9

| #define PRS0\_ASYNCH3\_PA9   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x9) |
| --- |

## [◆ ](#a5cb1e7fbb39adfdfca2516715f0cc1ac)PRS0\_ASYNCH3\_PB0

| #define PRS0\_ASYNCH3\_PB0   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x1, 0x0) |
| --- |

## [◆ ](#aa09fe8bc9d5c277db64c0912b55e9651)PRS0\_ASYNCH3\_PB1

| #define PRS0\_ASYNCH3\_PB1   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x1, 0x1) |
| --- |

## [◆ ](#a8fd4c8b45bb5366691e3ea98b20ca580)PRS0\_ASYNCH3\_PB2

| #define PRS0\_ASYNCH3\_PB2   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x1, 0x2) |
| --- |

## [◆ ](#a92ac18184efd55f90aecf9763b1d93b9)PRS0\_ASYNCH3\_PB3

| #define PRS0\_ASYNCH3\_PB3   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x1, 0x3) |
| --- |

## [◆ ](#a3b96ce5680cf373ff511249aec0d4ea3)PRS0\_ASYNCH3\_PB4

| #define PRS0\_ASYNCH3\_PB4   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x1, 0x4) |
| --- |

## [◆ ](#a895aabf3809c957da7438989e9fadc3a)PRS0\_ASYNCH3\_PB5

| #define PRS0\_ASYNCH3\_PB5   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x1, 0x5) |
| --- |

## [◆ ](#a016d312ee53e23e053e5322038c218e8)PRS0\_ASYNCH4\_PA0

| #define PRS0\_ASYNCH4\_PA0   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x0) |
| --- |

## [◆ ](#ac08b73b2d1c8340a46b2b4321d258bbf)PRS0\_ASYNCH4\_PA1

| #define PRS0\_ASYNCH4\_PA1   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x1) |
| --- |

## [◆ ](#a6d468079dce68ad1a80a09411eed3c61)PRS0\_ASYNCH4\_PA2

| #define PRS0\_ASYNCH4\_PA2   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x2) |
| --- |

## [◆ ](#a2901f5a1abe787afaaf8c04a6aafa57f)PRS0\_ASYNCH4\_PA3

| #define PRS0\_ASYNCH4\_PA3   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x3) |
| --- |

## [◆ ](#a599e583eb87879b76f1a889093ca1db7)PRS0\_ASYNCH4\_PA4

| #define PRS0\_ASYNCH4\_PA4   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x4) |
| --- |

## [◆ ](#a50cd729844356a327a34588ab70c9f51)PRS0\_ASYNCH4\_PA5

| #define PRS0\_ASYNCH4\_PA5   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x5) |
| --- |

## [◆ ](#a15672ea11df2224289fc84c07abddbce)PRS0\_ASYNCH4\_PA6

| #define PRS0\_ASYNCH4\_PA6   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x6) |
| --- |

## [◆ ](#a765447cc275c70881ae23b795c7fc53c)PRS0\_ASYNCH4\_PA7

| #define PRS0\_ASYNCH4\_PA7   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x7) |
| --- |

## [◆ ](#a9ce8837d29bbd43cf040ade45311b569)PRS0\_ASYNCH4\_PA8

| #define PRS0\_ASYNCH4\_PA8   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x8) |
| --- |

## [◆ ](#a1ab7c845d070ad001ec1af11fa70453e)PRS0\_ASYNCH4\_PA9

| #define PRS0\_ASYNCH4\_PA9   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x9) |
| --- |

## [◆ ](#ab0da5394e8fceec3a24c8ca362a6a73f)PRS0\_ASYNCH4\_PB0

| #define PRS0\_ASYNCH4\_PB0   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x1, 0x0) |
| --- |

## [◆ ](#a95e9e61ebc91932e32cf3683ba99beb7)PRS0\_ASYNCH4\_PB1

| #define PRS0\_ASYNCH4\_PB1   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x1, 0x1) |
| --- |

## [◆ ](#a9b7b2081e0a38e0e6ab9f2d3ca3654d8)PRS0\_ASYNCH4\_PB2

| #define PRS0\_ASYNCH4\_PB2   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x1, 0x2) |
| --- |

## [◆ ](#a0516f5991ffed91ba799d6d463f05945)PRS0\_ASYNCH4\_PB3

| #define PRS0\_ASYNCH4\_PB3   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x1, 0x3) |
| --- |

## [◆ ](#a8b217bac132dc7c18930e4fe8c4e58db)PRS0\_ASYNCH4\_PB4

| #define PRS0\_ASYNCH4\_PB4   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x1, 0x4) |
| --- |

## [◆ ](#a135d877dcee477d815fa6ee27dffe09f)PRS0\_ASYNCH4\_PB5

| #define PRS0\_ASYNCH4\_PB5   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x1, 0x5) |
| --- |

## [◆ ](#a6cac49a6aeefd56ad4ba7e4cba8910bf)PRS0\_ASYNCH5\_PA0

| #define PRS0\_ASYNCH5\_PA0   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x0) |
| --- |

## [◆ ](#a8442fb1410b80fcd20c78b7cc44608eb)PRS0\_ASYNCH5\_PA1

| #define PRS0\_ASYNCH5\_PA1   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x1) |
| --- |

## [◆ ](#aa3e3bbc87f46c7f0b9016518266e1fb2)PRS0\_ASYNCH5\_PA2

| #define PRS0\_ASYNCH5\_PA2   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x2) |
| --- |

## [◆ ](#a269678c70e29d05e9d67b82b1d5dcfd2)PRS0\_ASYNCH5\_PA3

| #define PRS0\_ASYNCH5\_PA3   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x3) |
| --- |

## [◆ ](#a7a314bb07eab261a850420ac2d6a2618)PRS0\_ASYNCH5\_PA4

| #define PRS0\_ASYNCH5\_PA4   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x4) |
| --- |

## [◆ ](#ac01e6bde894c73d5e965b7fe6ed03f53)PRS0\_ASYNCH5\_PA5

| #define PRS0\_ASYNCH5\_PA5   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x5) |
| --- |

## [◆ ](#ae3d6e3ae9d6d9d7c41ca233ad101b025)PRS0\_ASYNCH5\_PA6

| #define PRS0\_ASYNCH5\_PA6   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x6) |
| --- |

## [◆ ](#a769160beeaa4ca59cae64a1c61b5c90e)PRS0\_ASYNCH5\_PA7

| #define PRS0\_ASYNCH5\_PA7   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x7) |
| --- |

## [◆ ](#a7485b4e8b8b2eca4594481533f547997)PRS0\_ASYNCH5\_PA8

| #define PRS0\_ASYNCH5\_PA8   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x8) |
| --- |

## [◆ ](#afd07ce0874b05616058dc214ded43b1a)PRS0\_ASYNCH5\_PA9

| #define PRS0\_ASYNCH5\_PA9   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x9) |
| --- |

## [◆ ](#adb08d0b33060e185431fb336110899c9)PRS0\_ASYNCH5\_PB0

| #define PRS0\_ASYNCH5\_PB0   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x1, 0x0) |
| --- |

## [◆ ](#a82b599c4956aeea92802694032b4b55a)PRS0\_ASYNCH5\_PB1

| #define PRS0\_ASYNCH5\_PB1   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x1, 0x1) |
| --- |

## [◆ ](#a26b4fa1b83e7857071e5f5d434055a6a)PRS0\_ASYNCH5\_PB2

| #define PRS0\_ASYNCH5\_PB2   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x1, 0x2) |
| --- |

## [◆ ](#a0fbf5258e9f5d24e164a31dbdb40443e)PRS0\_ASYNCH5\_PB3

| #define PRS0\_ASYNCH5\_PB3   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x1, 0x3) |
| --- |

## [◆ ](#a7de3a9532a4e4fdf5380046737950e18)PRS0\_ASYNCH5\_PB4

| #define PRS0\_ASYNCH5\_PB4   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x1, 0x4) |
| --- |

## [◆ ](#aea378afb137f62f3f01b3a87c09dcd4f)PRS0\_ASYNCH5\_PB5

| #define PRS0\_ASYNCH5\_PB5   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x1, 0x5) |
| --- |

## [◆ ](#a5c7910d134b9fe6ddf1da299dfb2cfa0)PRS0\_ASYNCH6\_PC0

| #define PRS0\_ASYNCH6\_PC0   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x0) |
| --- |

## [◆ ](#a713321693f2cfd7cda27d1c36fc9b74b)PRS0\_ASYNCH6\_PC1

| #define PRS0\_ASYNCH6\_PC1   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x1) |
| --- |

## [◆ ](#a907d3ee7390b6ebcb5cac75724b6c587)PRS0\_ASYNCH6\_PC2

| #define PRS0\_ASYNCH6\_PC2   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x2) |
| --- |

## [◆ ](#a5eebd47a62e87b938b530113cd048481)PRS0\_ASYNCH6\_PC3

| #define PRS0\_ASYNCH6\_PC3   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x3) |
| --- |

## [◆ ](#a2d0d89b1abadc95ec02a88916330bab4)PRS0\_ASYNCH6\_PC4

| #define PRS0\_ASYNCH6\_PC4   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x4) |
| --- |

## [◆ ](#aaa44b81b3421197bff7df84a5e90a566)PRS0\_ASYNCH6\_PC5

| #define PRS0\_ASYNCH6\_PC5   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x5) |
| --- |

## [◆ ](#aaeaba294a765ca9892f4591acb3dd83e)PRS0\_ASYNCH6\_PC6

| #define PRS0\_ASYNCH6\_PC6   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x6) |
| --- |

## [◆ ](#a0d95bb763b051fb232dc8805ad6d643e)PRS0\_ASYNCH6\_PC7

| #define PRS0\_ASYNCH6\_PC7   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x7) |
| --- |

## [◆ ](#a153f3fcc748dc54f64c23f8c23d9db39)PRS0\_ASYNCH6\_PC8

| #define PRS0\_ASYNCH6\_PC8   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x8) |
| --- |

## [◆ ](#a6de52f879778b33cc6fa14060dbccaec)PRS0\_ASYNCH6\_PC9

| #define PRS0\_ASYNCH6\_PC9   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x9) |
| --- |

## [◆ ](#a0db829680023f49ec8b84b8418994f57)PRS0\_ASYNCH6\_PD0

| #define PRS0\_ASYNCH6\_PD0   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x3, 0x0) |
| --- |

## [◆ ](#a41989b05cfd244afef8a6c359de6f6cb)PRS0\_ASYNCH6\_PD1

| #define PRS0\_ASYNCH6\_PD1   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x3, 0x1) |
| --- |

## [◆ ](#ad70491288162b935edc6602844fbad73)PRS0\_ASYNCH6\_PD2

| #define PRS0\_ASYNCH6\_PD2   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x3, 0x2) |
| --- |

## [◆ ](#a03cdfe05c93c94a99e457fc34be7adb3)PRS0\_ASYNCH6\_PD3

| #define PRS0\_ASYNCH6\_PD3   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x3, 0x3) |
| --- |

## [◆ ](#a6c74cc2ba56d399a25378ecccef3005f)PRS0\_ASYNCH6\_PD4

| #define PRS0\_ASYNCH6\_PD4   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x3, 0x4) |
| --- |

## [◆ ](#a907ff75410116fd75163bbb7ad72a14d)PRS0\_ASYNCH6\_PD5

| #define PRS0\_ASYNCH6\_PD5   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x3, 0x5) |
| --- |

## [◆ ](#a263dcb3077d0d1e3a58730140042046d)PRS0\_ASYNCH7\_PC0

| #define PRS0\_ASYNCH7\_PC0   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x0) |
| --- |

## [◆ ](#aa49bafce35b9bb4b59c8c9c22f06a739)PRS0\_ASYNCH7\_PC1

| #define PRS0\_ASYNCH7\_PC1   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x1) |
| --- |

## [◆ ](#ae0305282eab2df6979c235c8d5d00ac7)PRS0\_ASYNCH7\_PC2

| #define PRS0\_ASYNCH7\_PC2   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x2) |
| --- |

## [◆ ](#a05355f9a968579fd8a931b7458d37960)PRS0\_ASYNCH7\_PC3

| #define PRS0\_ASYNCH7\_PC3   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x3) |
| --- |

## [◆ ](#acb9a2a6531dd263cfe56858aa9c77791)PRS0\_ASYNCH7\_PC4

| #define PRS0\_ASYNCH7\_PC4   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x4) |
| --- |

## [◆ ](#af504334eb99bab375e929f662ee6091a)PRS0\_ASYNCH7\_PC5

| #define PRS0\_ASYNCH7\_PC5   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x5) |
| --- |

## [◆ ](#a770b593af51ec2f1fae3694e1a29cdef)PRS0\_ASYNCH7\_PC6

| #define PRS0\_ASYNCH7\_PC6   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x6) |
| --- |

## [◆ ](#a96d44dd7e3fb6c4a68e5c2f029d0e3d4)PRS0\_ASYNCH7\_PC7

| #define PRS0\_ASYNCH7\_PC7   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x7) |
| --- |

## [◆ ](#a7eb775f790ebbe32f93c2cdc2630cd0a)PRS0\_ASYNCH7\_PC8

| #define PRS0\_ASYNCH7\_PC8   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x8) |
| --- |

## [◆ ](#a6af238ef897be1e90e2cd8de910cd0eb)PRS0\_ASYNCH7\_PC9

| #define PRS0\_ASYNCH7\_PC9   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x9) |
| --- |

## [◆ ](#a4e38e496fe8a602726a9fcfac5c9553b)PRS0\_ASYNCH7\_PD0

| #define PRS0\_ASYNCH7\_PD0   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x3, 0x0) |
| --- |

## [◆ ](#a8a5617fb6a01d979b5754bb30438ef11)PRS0\_ASYNCH7\_PD1

| #define PRS0\_ASYNCH7\_PD1   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x3, 0x1) |
| --- |

## [◆ ](#ae44270558459c4a31a9d8db2216b6a47)PRS0\_ASYNCH7\_PD2

| #define PRS0\_ASYNCH7\_PD2   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x3, 0x2) |
| --- |

## [◆ ](#a19e5fc23eb4c5edbe4cc2be54508038a)PRS0\_ASYNCH7\_PD3

| #define PRS0\_ASYNCH7\_PD3   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x3, 0x3) |
| --- |

## [◆ ](#a6f3cf739f48f52265c18a437b40c919f)PRS0\_ASYNCH7\_PD4

| #define PRS0\_ASYNCH7\_PD4   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x3, 0x4) |
| --- |

## [◆ ](#ae6eae6f47a075d75a1ea7e258696ac7c)PRS0\_ASYNCH7\_PD5

| #define PRS0\_ASYNCH7\_PD5   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x3, 0x5) |
| --- |

## [◆ ](#a01aee008d4ae0969e81630224253732c)PRS0\_ASYNCH8\_PC0

| #define PRS0\_ASYNCH8\_PC0   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x0) |
| --- |

## [◆ ](#a1020e0f439015d77aad3a4ad6761745f)PRS0\_ASYNCH8\_PC1

| #define PRS0\_ASYNCH8\_PC1   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x1) |
| --- |

## [◆ ](#a78ac7a7a23787837c2d45b7fb619d973)PRS0\_ASYNCH8\_PC2

| #define PRS0\_ASYNCH8\_PC2   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x2) |
| --- |

## [◆ ](#a21d56ee2bba901bb0ad42fe00fd47126)PRS0\_ASYNCH8\_PC3

| #define PRS0\_ASYNCH8\_PC3   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x3) |
| --- |

## [◆ ](#ab38e8e6ebf5f7b8cf9db913835c77fdf)PRS0\_ASYNCH8\_PC4

| #define PRS0\_ASYNCH8\_PC4   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x4) |
| --- |

## [◆ ](#a034b8fafc8f80d4aa749ace8d383aa42)PRS0\_ASYNCH8\_PC5

| #define PRS0\_ASYNCH8\_PC5   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x5) |
| --- |

## [◆ ](#a9b6282a03652ffd9886abf001018942e)PRS0\_ASYNCH8\_PC6

| #define PRS0\_ASYNCH8\_PC6   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x6) |
| --- |

## [◆ ](#a7a33bde9021e0d8f1a4c331064369169)PRS0\_ASYNCH8\_PC7

| #define PRS0\_ASYNCH8\_PC7   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x7) |
| --- |

## [◆ ](#a6e2a2dad2c91c6f53235eca30fbbcb71)PRS0\_ASYNCH8\_PC8

| #define PRS0\_ASYNCH8\_PC8   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x8) |
| --- |

## [◆ ](#adfc74b9cf0bc54094e44eb498174baf2)PRS0\_ASYNCH8\_PC9

| #define PRS0\_ASYNCH8\_PC9   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x9) |
| --- |

## [◆ ](#a3c4c1e1e2ed6aad821543605099c464e)PRS0\_ASYNCH8\_PD0

| #define PRS0\_ASYNCH8\_PD0   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x3, 0x0) |
| --- |

## [◆ ](#a7a96c3dddcf49a09ab3941a19e33dd2b)PRS0\_ASYNCH8\_PD1

| #define PRS0\_ASYNCH8\_PD1   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x3, 0x1) |
| --- |

## [◆ ](#a045129ec46f95f26ba665876216df09a)PRS0\_ASYNCH8\_PD2

| #define PRS0\_ASYNCH8\_PD2   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x3, 0x2) |
| --- |

## [◆ ](#abf899559efdca73abc5e1f3e058280dc)PRS0\_ASYNCH8\_PD3

| #define PRS0\_ASYNCH8\_PD3   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x3, 0x3) |
| --- |

## [◆ ](#aa41526f1e85b40d4d9f30444542c19e2)PRS0\_ASYNCH8\_PD4

| #define PRS0\_ASYNCH8\_PD4   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x3, 0x4) |
| --- |

## [◆ ](#ae7d962af59b6c3577581a675b2cbb3ee)PRS0\_ASYNCH8\_PD5

| #define PRS0\_ASYNCH8\_PD5   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x3, 0x5) |
| --- |

## [◆ ](#ad6900f2865fce19423ba5bce65e6f6ec)PRS0\_ASYNCH9\_PC0

| #define PRS0\_ASYNCH9\_PC0   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x0) |
| --- |

## [◆ ](#a21a22ddcc1d1b8c05250ea00bfaf2c46)PRS0\_ASYNCH9\_PC1

| #define PRS0\_ASYNCH9\_PC1   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x1) |
| --- |

## [◆ ](#a7dcb713d1f7f8457e30812454272c360)PRS0\_ASYNCH9\_PC2

| #define PRS0\_ASYNCH9\_PC2   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x2) |
| --- |

## [◆ ](#ac6eeb711fa526a794104a43142cedc8d)PRS0\_ASYNCH9\_PC3

| #define PRS0\_ASYNCH9\_PC3   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x3) |
| --- |

## [◆ ](#a87ada6898e2eeddcaeead80835a3800b)PRS0\_ASYNCH9\_PC4

| #define PRS0\_ASYNCH9\_PC4   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x4) |
| --- |

## [◆ ](#a6b5b3ca2088cb2c43fbebf99cd4e9ad3)PRS0\_ASYNCH9\_PC5

| #define PRS0\_ASYNCH9\_PC5   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x5) |
| --- |

## [◆ ](#a4383c5af531fd312831c4116e60bec7e)PRS0\_ASYNCH9\_PC6

| #define PRS0\_ASYNCH9\_PC6   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x6) |
| --- |

## [◆ ](#a59c911b1c45a061480e83d081796f84b)PRS0\_ASYNCH9\_PC7

| #define PRS0\_ASYNCH9\_PC7   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x7) |
| --- |

## [◆ ](#ad17efaa7728c44ad44f68631501b5041)PRS0\_ASYNCH9\_PC8

| #define PRS0\_ASYNCH9\_PC8   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x8) |
| --- |

## [◆ ](#adbd9075be51a80c7102f9a873af230c1)PRS0\_ASYNCH9\_PC9

| #define PRS0\_ASYNCH9\_PC9   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x9) |
| --- |

## [◆ ](#a89cd80ad72079b3a20917cc722fed3c3)PRS0\_ASYNCH9\_PD0

| #define PRS0\_ASYNCH9\_PD0   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x3, 0x0) |
| --- |

## [◆ ](#aa9433d94ee912ff578dc1f3753bca9b5)PRS0\_ASYNCH9\_PD1

| #define PRS0\_ASYNCH9\_PD1   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x3, 0x1) |
| --- |

## [◆ ](#a1dfa38b0754566f3586712b7474ce13f)PRS0\_ASYNCH9\_PD2

| #define PRS0\_ASYNCH9\_PD2   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x3, 0x2) |
| --- |

## [◆ ](#a48c2477430954a1f5ebefcd625132b34)PRS0\_ASYNCH9\_PD3

| #define PRS0\_ASYNCH9\_PD3   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x3, 0x3) |
| --- |

## [◆ ](#a3f32b54daa1e09ccb97ad447facd5076)PRS0\_ASYNCH9\_PD4

| #define PRS0\_ASYNCH9\_PD4   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x3, 0x4) |
| --- |

## [◆ ](#a7e8227352546862fba1996f7a5c13e5c)PRS0\_ASYNCH9\_PD5

| #define PRS0\_ASYNCH9\_PD5   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x3, 0x5) |
| --- |

## [◆ ](#a2c5a579f02ffd8ca34ce4f12cb30c8f0)PRS0\_SYNCH0\_PA0

| #define PRS0\_SYNCH0\_PA0   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x0) |
| --- |

## [◆ ](#a5f853596173978c14b0b85059afa8a5a)PRS0\_SYNCH0\_PA1

| #define PRS0\_SYNCH0\_PA1   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x1) |
| --- |

## [◆ ](#a7c8f6f55ba3e60c6a160f83f324442f0)PRS0\_SYNCH0\_PA2

| #define PRS0\_SYNCH0\_PA2   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x2) |
| --- |

## [◆ ](#a8b8697e5c71b52686ea68726a1c033dd)PRS0\_SYNCH0\_PA3

| #define PRS0\_SYNCH0\_PA3   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x3) |
| --- |

## [◆ ](#a509796448ccd2509eeb7fbf9b4432267)PRS0\_SYNCH0\_PA4

| #define PRS0\_SYNCH0\_PA4   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x4) |
| --- |

## [◆ ](#afd80bdbc61c9bddb37851b1c9b7b6fa6)PRS0\_SYNCH0\_PA5

| #define PRS0\_SYNCH0\_PA5   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x5) |
| --- |

## [◆ ](#abd86045f5ef93089158a28dd7f3aa4c2)PRS0\_SYNCH0\_PA6

| #define PRS0\_SYNCH0\_PA6   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x6) |
| --- |

## [◆ ](#ae4f987b0bca7d9d9b12a61f99cec5262)PRS0\_SYNCH0\_PA7

| #define PRS0\_SYNCH0\_PA7   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x7) |
| --- |

## [◆ ](#a9158c2302ee19ed733f624dea5b4b39a)PRS0\_SYNCH0\_PA8

| #define PRS0\_SYNCH0\_PA8   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x8) |
| --- |

## [◆ ](#aac770fa7d69626ab2575cf1144757e13)PRS0\_SYNCH0\_PA9

| #define PRS0\_SYNCH0\_PA9   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x9) |
| --- |

## [◆ ](#a736a7ad4a31b1d6dc0c548d628da9d97)PRS0\_SYNCH0\_PB0

| #define PRS0\_SYNCH0\_PB0   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x1, 0x0) |
| --- |

## [◆ ](#a10e121857131802c71c42f1fbad81970)PRS0\_SYNCH0\_PB1

| #define PRS0\_SYNCH0\_PB1   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x1, 0x1) |
| --- |

## [◆ ](#a73be353f9ce6f94984b0e1c804c97e07)PRS0\_SYNCH0\_PB2

| #define PRS0\_SYNCH0\_PB2   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x1, 0x2) |
| --- |

## [◆ ](#acd5b4f55607cae70abe6fb9e6b361f53)PRS0\_SYNCH0\_PB3

| #define PRS0\_SYNCH0\_PB3   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x1, 0x3) |
| --- |

## [◆ ](#a9e5fc4aa547c95e8dc34bb89c384a35f)PRS0\_SYNCH0\_PB4

| #define PRS0\_SYNCH0\_PB4   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x1, 0x4) |
| --- |

## [◆ ](#ac2ff0fc249cc517d39917aced695b58e)PRS0\_SYNCH0\_PB5

| #define PRS0\_SYNCH0\_PB5   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x1, 0x5) |
| --- |

## [◆ ](#aed0f68fd0e4029e96d08fb24876f88b5)PRS0\_SYNCH0\_PC0

| #define PRS0\_SYNCH0\_PC0   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x0) |
| --- |

## [◆ ](#ae52c949f3917be619b0f5f2365c2e8ba)PRS0\_SYNCH0\_PC1

| #define PRS0\_SYNCH0\_PC1   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x1) |
| --- |

## [◆ ](#aac10f668835b732d019a50c3cfc47e37)PRS0\_SYNCH0\_PC2

| #define PRS0\_SYNCH0\_PC2   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x2) |
| --- |

## [◆ ](#aa9c52d637e33202df2ace78c13c9555f)PRS0\_SYNCH0\_PC3

| #define PRS0\_SYNCH0\_PC3   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x3) |
| --- |

## [◆ ](#adcaec5a2fb5dd33e72e486587daa1f4e)PRS0\_SYNCH0\_PC4

| #define PRS0\_SYNCH0\_PC4   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x4) |
| --- |

## [◆ ](#aebbdc8a0ced784325db8374db6a1f16c)PRS0\_SYNCH0\_PC5

| #define PRS0\_SYNCH0\_PC5   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x5) |
| --- |

## [◆ ](#aedadba37735c1e29b357461908d0c22f)PRS0\_SYNCH0\_PC6

| #define PRS0\_SYNCH0\_PC6   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x6) |
| --- |

## [◆ ](#a0b2e975e8a9e48c1e0b64d10b0d4776f)PRS0\_SYNCH0\_PC7

| #define PRS0\_SYNCH0\_PC7   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x7) |
| --- |

## [◆ ](#ad35c7c7af4263b200a8761baa45ec6f1)PRS0\_SYNCH0\_PC8

| #define PRS0\_SYNCH0\_PC8   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x8) |
| --- |

## [◆ ](#abd7d76599d153aa57da78a12e5854caf)PRS0\_SYNCH0\_PC9

| #define PRS0\_SYNCH0\_PC9   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x9) |
| --- |

## [◆ ](#a5f8dea11049e64bae1e4e27baf9e1b31)PRS0\_SYNCH0\_PD0

| #define PRS0\_SYNCH0\_PD0   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x3, 0x0) |
| --- |

## [◆ ](#a27144719fce957df87cb1434bd78c53b)PRS0\_SYNCH0\_PD1

| #define PRS0\_SYNCH0\_PD1   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x3, 0x1) |
| --- |

## [◆ ](#a014112c01a441ca65ee77b693e22bcf5)PRS0\_SYNCH0\_PD2

| #define PRS0\_SYNCH0\_PD2   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x3, 0x2) |
| --- |

## [◆ ](#a9ace1d40d2d50bc683ef0c57cc7863e0)PRS0\_SYNCH0\_PD3

| #define PRS0\_SYNCH0\_PD3   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x3, 0x3) |
| --- |

## [◆ ](#aade7486bb4853a67abea630973058c25)PRS0\_SYNCH0\_PD4

| #define PRS0\_SYNCH0\_PD4   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x3, 0x4) |
| --- |

## [◆ ](#afd5f1e060b3c0836c7de21742af8ab7f)PRS0\_SYNCH0\_PD5

| #define PRS0\_SYNCH0\_PD5   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x3, 0x5) |
| --- |

## [◆ ](#adedbd9cd1918a6d9543c886660eced9d)PRS0\_SYNCH1\_PA0

| #define PRS0\_SYNCH1\_PA0   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x0) |
| --- |

## [◆ ](#a1083f73ff99ca1b3bf4446081e2addd7)PRS0\_SYNCH1\_PA1

| #define PRS0\_SYNCH1\_PA1   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x1) |
| --- |

## [◆ ](#a1ea1179bbedea21d7d5ba85c489b88e1)PRS0\_SYNCH1\_PA2

| #define PRS0\_SYNCH1\_PA2   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x2) |
| --- |

## [◆ ](#a18fe9b252631cc7ba936c99d6206294c)PRS0\_SYNCH1\_PA3

| #define PRS0\_SYNCH1\_PA3   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x3) |
| --- |

## [◆ ](#ae5b32510b0bfea666dfb424ecad5e926)PRS0\_SYNCH1\_PA4

| #define PRS0\_SYNCH1\_PA4   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x4) |
| --- |

## [◆ ](#a990491e0b9b76fc29c692ab11429d1bf)PRS0\_SYNCH1\_PA5

| #define PRS0\_SYNCH1\_PA5   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x5) |
| --- |

## [◆ ](#accd2f4d5864cea8337d9436d6f946f2d)PRS0\_SYNCH1\_PA6

| #define PRS0\_SYNCH1\_PA6   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x6) |
| --- |

## [◆ ](#aceb6e7687dc5a74ba0da121a26529409)PRS0\_SYNCH1\_PA7

| #define PRS0\_SYNCH1\_PA7   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x7) |
| --- |

## [◆ ](#ab59c19f19a428b50ddf674bd46c4e07f)PRS0\_SYNCH1\_PA8

| #define PRS0\_SYNCH1\_PA8   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x8) |
| --- |

## [◆ ](#a26cdef2fd84b7a927495c690a69837e1)PRS0\_SYNCH1\_PA9

| #define PRS0\_SYNCH1\_PA9   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x9) |
| --- |

## [◆ ](#aa19c3a0e0e8ce1868f1a89f7bd2e703a)PRS0\_SYNCH1\_PB0

| #define PRS0\_SYNCH1\_PB0   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x1, 0x0) |
| --- |

## [◆ ](#ab5cf7a7aacec81e75db1643c99958fa3)PRS0\_SYNCH1\_PB1

| #define PRS0\_SYNCH1\_PB1   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x1, 0x1) |
| --- |

## [◆ ](#a7487f16738d5b7fa4b19224e4eeab36d)PRS0\_SYNCH1\_PB2

| #define PRS0\_SYNCH1\_PB2   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x1, 0x2) |
| --- |

## [◆ ](#aaff1a467a07bc3301c63667057cb4b2d)PRS0\_SYNCH1\_PB3

| #define PRS0\_SYNCH1\_PB3   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x1, 0x3) |
| --- |

## [◆ ](#a167f92235a6d97f9ecd421e65b18e7f7)PRS0\_SYNCH1\_PB4

| #define PRS0\_SYNCH1\_PB4   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x1, 0x4) |
| --- |

## [◆ ](#abfd339a1a42f0672089fcf249b24f51b)PRS0\_SYNCH1\_PB5

| #define PRS0\_SYNCH1\_PB5   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x1, 0x5) |
| --- |

## [◆ ](#ab3036a275379a79acb9c9186172036be)PRS0\_SYNCH1\_PC0

| #define PRS0\_SYNCH1\_PC0   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x0) |
| --- |

## [◆ ](#ae726abd2298409738d8deba2708508be)PRS0\_SYNCH1\_PC1

| #define PRS0\_SYNCH1\_PC1   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x1) |
| --- |

## [◆ ](#a9aec203bbc1ecd06760f7262a53c2b3e)PRS0\_SYNCH1\_PC2

| #define PRS0\_SYNCH1\_PC2   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x2) |
| --- |

## [◆ ](#a87e88cfd739e57c6b2832ddc579e9007)PRS0\_SYNCH1\_PC3

| #define PRS0\_SYNCH1\_PC3   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x3) |
| --- |

## [◆ ](#a5ff140aeb080678501e5a49e5a17238e)PRS0\_SYNCH1\_PC4

| #define PRS0\_SYNCH1\_PC4   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x4) |
| --- |

## [◆ ](#ad4e38b8812f7c0d4a071c56033ea29b6)PRS0\_SYNCH1\_PC5

| #define PRS0\_SYNCH1\_PC5   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x5) |
| --- |

## [◆ ](#ae5fd5f17e4c57e6d27e4771b9d697412)PRS0\_SYNCH1\_PC6

| #define PRS0\_SYNCH1\_PC6   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x6) |
| --- |

## [◆ ](#a73df027a983ad91140837b7823cf457b)PRS0\_SYNCH1\_PC7

| #define PRS0\_SYNCH1\_PC7   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x7) |
| --- |

## [◆ ](#ae291d2ca20075eb4c69c212bef91dd64)PRS0\_SYNCH1\_PC8

| #define PRS0\_SYNCH1\_PC8   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x8) |
| --- |

## [◆ ](#a56124bf24e9a29162e498f308de783f7)PRS0\_SYNCH1\_PC9

| #define PRS0\_SYNCH1\_PC9   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x9) |
| --- |

## [◆ ](#ac3d3b0681c6f881fdf67d75330d2ad15)PRS0\_SYNCH1\_PD0

| #define PRS0\_SYNCH1\_PD0   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x3, 0x0) |
| --- |

## [◆ ](#a856e585175b99140059f56bbb485002c)PRS0\_SYNCH1\_PD1

| #define PRS0\_SYNCH1\_PD1   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x3, 0x1) |
| --- |

## [◆ ](#a40bd508ace349e81a5d0c155ca89970d)PRS0\_SYNCH1\_PD2

| #define PRS0\_SYNCH1\_PD2   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x3, 0x2) |
| --- |

## [◆ ](#a0619050cb1a04b75b610788e2de0390e)PRS0\_SYNCH1\_PD3

| #define PRS0\_SYNCH1\_PD3   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x3, 0x3) |
| --- |

## [◆ ](#a9a804e3cdb2e284489233d28577e1fc4)PRS0\_SYNCH1\_PD4

| #define PRS0\_SYNCH1\_PD4   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x3, 0x4) |
| --- |

## [◆ ](#a23abf1b2534882338fc00f11be349d01)PRS0\_SYNCH1\_PD5

| #define PRS0\_SYNCH1\_PD5   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x3, 0x5) |
| --- |

## [◆ ](#a30eedcbcb9ef6aa04facebe8e1cc1093)PRS0\_SYNCH2\_PA0

| #define PRS0\_SYNCH2\_PA0   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x0) |
| --- |

## [◆ ](#a8ec3379386547e7712ad3c900ec6814c)PRS0\_SYNCH2\_PA1

| #define PRS0\_SYNCH2\_PA1   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x1) |
| --- |

## [◆ ](#a770727e399810443ff27f6a2023c65ee)PRS0\_SYNCH2\_PA2

| #define PRS0\_SYNCH2\_PA2   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x2) |
| --- |

## [◆ ](#afa5e0ddfe140d74f0dd76d8e7edda691)PRS0\_SYNCH2\_PA3

| #define PRS0\_SYNCH2\_PA3   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x3) |
| --- |

## [◆ ](#a2cf89814fec476f61882164cdf99b537)PRS0\_SYNCH2\_PA4

| #define PRS0\_SYNCH2\_PA4   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x4) |
| --- |

## [◆ ](#a8a48ec9e994929feacba66e0509ad3e1)PRS0\_SYNCH2\_PA5

| #define PRS0\_SYNCH2\_PA5   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x5) |
| --- |

## [◆ ](#a117da23bb4f9f0aa2110437ffefc365a)PRS0\_SYNCH2\_PA6

| #define PRS0\_SYNCH2\_PA6   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x6) |
| --- |

## [◆ ](#a08847c5400ec84819a9b68b2c61bb501)PRS0\_SYNCH2\_PA7

| #define PRS0\_SYNCH2\_PA7   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x7) |
| --- |

## [◆ ](#ac874a823e48f1cce54ed84337b174833)PRS0\_SYNCH2\_PA8

| #define PRS0\_SYNCH2\_PA8   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x8) |
| --- |

## [◆ ](#a6a7f96cb800833e9fbe8172b48de42a4)PRS0\_SYNCH2\_PA9

| #define PRS0\_SYNCH2\_PA9   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x9) |
| --- |

## [◆ ](#a3246953945006183dfbc3b12a5e86d61)PRS0\_SYNCH2\_PB0

| #define PRS0\_SYNCH2\_PB0   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x1, 0x0) |
| --- |

## [◆ ](#a0dec289423a72a3226f883db9921b0b2)PRS0\_SYNCH2\_PB1

| #define PRS0\_SYNCH2\_PB1   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x1, 0x1) |
| --- |

## [◆ ](#a5c36bbbb8c205c06b05cb1786f91f34f)PRS0\_SYNCH2\_PB2

| #define PRS0\_SYNCH2\_PB2   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x1, 0x2) |
| --- |

## [◆ ](#a4e5c98830a60d5e00602e4e7f4348b6f)PRS0\_SYNCH2\_PB3

| #define PRS0\_SYNCH2\_PB3   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x1, 0x3) |
| --- |

## [◆ ](#aa06a6017287b483a4a47b128043b7217)PRS0\_SYNCH2\_PB4

| #define PRS0\_SYNCH2\_PB4   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x1, 0x4) |
| --- |

## [◆ ](#acbc14c00c46035fea317e32213d6c2c3)PRS0\_SYNCH2\_PB5

| #define PRS0\_SYNCH2\_PB5   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x1, 0x5) |
| --- |

## [◆ ](#ac9ab782f8cda90916bd9cb751753144a)PRS0\_SYNCH2\_PC0

| #define PRS0\_SYNCH2\_PC0   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x0) |
| --- |

## [◆ ](#a71fb98a3d5355af02d2c46d69c7f6edc)PRS0\_SYNCH2\_PC1

| #define PRS0\_SYNCH2\_PC1   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x1) |
| --- |

## [◆ ](#a50b30cf886dedec9e7cd761d9596d7f6)PRS0\_SYNCH2\_PC2

| #define PRS0\_SYNCH2\_PC2   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x2) |
| --- |

## [◆ ](#ab8725b1678b453d17551cf0daea10f57)PRS0\_SYNCH2\_PC3

| #define PRS0\_SYNCH2\_PC3   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x3) |
| --- |

## [◆ ](#a012f52b7a7cc4babe7f8e14b27125790)PRS0\_SYNCH2\_PC4

| #define PRS0\_SYNCH2\_PC4   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x4) |
| --- |

## [◆ ](#a5ce775779214b9341aede3162d4e381a)PRS0\_SYNCH2\_PC5

| #define PRS0\_SYNCH2\_PC5   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x5) |
| --- |

## [◆ ](#a151b6197cf1bb336dcdecf41cfdc90fc)PRS0\_SYNCH2\_PC6

| #define PRS0\_SYNCH2\_PC6   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x6) |
| --- |

## [◆ ](#a49b69f4a2a409147dec4247b891e2d0e)PRS0\_SYNCH2\_PC7

| #define PRS0\_SYNCH2\_PC7   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x7) |
| --- |

## [◆ ](#ae7703f340b5da2fba4e1269049d21119)PRS0\_SYNCH2\_PC8

| #define PRS0\_SYNCH2\_PC8   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x8) |
| --- |

## [◆ ](#a96c416b5297ffd7e7ddeed55f31c658c)PRS0\_SYNCH2\_PC9

| #define PRS0\_SYNCH2\_PC9   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x9) |
| --- |

## [◆ ](#af8c37706e65ff4f9f6f90f01ce507040)PRS0\_SYNCH2\_PD0

| #define PRS0\_SYNCH2\_PD0   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x3, 0x0) |
| --- |

## [◆ ](#ac83a6c15c88a8662ce8b9ba58d60772a)PRS0\_SYNCH2\_PD1

| #define PRS0\_SYNCH2\_PD1   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x3, 0x1) |
| --- |

## [◆ ](#ad8d312030ac50620b851c24cfb90b8c0)PRS0\_SYNCH2\_PD2

| #define PRS0\_SYNCH2\_PD2   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x3, 0x2) |
| --- |

## [◆ ](#a3462ed2558a059ff7b2c81471bb30adf)PRS0\_SYNCH2\_PD3

| #define PRS0\_SYNCH2\_PD3   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x3, 0x3) |
| --- |

## [◆ ](#a98dc3a73329ab25a00dd293e05c8ebeb)PRS0\_SYNCH2\_PD4

| #define PRS0\_SYNCH2\_PD4   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x3, 0x4) |
| --- |

## [◆ ](#a8ff5ea4512864a5ae3c26341d7a8c8f9)PRS0\_SYNCH2\_PD5

| #define PRS0\_SYNCH2\_PD5   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x3, 0x5) |
| --- |

## [◆ ](#a3d8a4990b1f1b2c03152d2d0ee88afc3)PRS0\_SYNCH3\_PA0

| #define PRS0\_SYNCH3\_PA0   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x0) |
| --- |

## [◆ ](#a13b0ade04e1c64d1438afe98588fe2d2)PRS0\_SYNCH3\_PA1

| #define PRS0\_SYNCH3\_PA1   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x1) |
| --- |

## [◆ ](#a270b6759ebfa8c61efefbc57fa10b3a3)PRS0\_SYNCH3\_PA2

| #define PRS0\_SYNCH3\_PA2   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x2) |
| --- |

## [◆ ](#a6d223baeec1045d533966d37adeaa1fd)PRS0\_SYNCH3\_PA3

| #define PRS0\_SYNCH3\_PA3   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x3) |
| --- |

## [◆ ](#a0e17834640a0fa86e9cc0d166b41051e)PRS0\_SYNCH3\_PA4

| #define PRS0\_SYNCH3\_PA4   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x4) |
| --- |

## [◆ ](#a49a035319ad597aca7e0fcfa1abd0f01)PRS0\_SYNCH3\_PA5

| #define PRS0\_SYNCH3\_PA5   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x5) |
| --- |

## [◆ ](#a13e3aaaec3efb457103bb8159cb4de31)PRS0\_SYNCH3\_PA6

| #define PRS0\_SYNCH3\_PA6   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x6) |
| --- |

## [◆ ](#aad295ab8444f14fd8a7f01225d8d028d)PRS0\_SYNCH3\_PA7

| #define PRS0\_SYNCH3\_PA7   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x7) |
| --- |

## [◆ ](#a1ee67f1e40e56d7ce7b6e2dfc3c6d60d)PRS0\_SYNCH3\_PA8

| #define PRS0\_SYNCH3\_PA8   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x8) |
| --- |

## [◆ ](#ab895d6126fa54fb4878597a945f74dec)PRS0\_SYNCH3\_PA9

| #define PRS0\_SYNCH3\_PA9   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x9) |
| --- |

## [◆ ](#ab17a4fca8c86667da92478553626bba6)PRS0\_SYNCH3\_PB0

| #define PRS0\_SYNCH3\_PB0   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x1, 0x0) |
| --- |

## [◆ ](#a88fff8ac2df69413d6fddc5ec152e31b)PRS0\_SYNCH3\_PB1

| #define PRS0\_SYNCH3\_PB1   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x1, 0x1) |
| --- |

## [◆ ](#ae56538fc7c8d0ca774ed366e51675230)PRS0\_SYNCH3\_PB2

| #define PRS0\_SYNCH3\_PB2   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x1, 0x2) |
| --- |

## [◆ ](#acc237ffc92de8a4b0003dd9f7e09c690)PRS0\_SYNCH3\_PB3

| #define PRS0\_SYNCH3\_PB3   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x1, 0x3) |
| --- |

## [◆ ](#a1579ef24d96f575092d727d1ea82af8e)PRS0\_SYNCH3\_PB4

| #define PRS0\_SYNCH3\_PB4   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x1, 0x4) |
| --- |

## [◆ ](#a3d08c5cfdb1e23bcd9de7f5b4c941aa0)PRS0\_SYNCH3\_PB5

| #define PRS0\_SYNCH3\_PB5   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x1, 0x5) |
| --- |

## [◆ ](#a5b3ca0959f268e1977ab4fcb0333b282)PRS0\_SYNCH3\_PC0

| #define PRS0\_SYNCH3\_PC0   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x0) |
| --- |

## [◆ ](#a322705abcca1fb83fdffcf16252c35d4)PRS0\_SYNCH3\_PC1

| #define PRS0\_SYNCH3\_PC1   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x1) |
| --- |

## [◆ ](#ad45be94cb4581dbc5c9474d2da892aa0)PRS0\_SYNCH3\_PC2

| #define PRS0\_SYNCH3\_PC2   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x2) |
| --- |

## [◆ ](#af541dc086b57060761678fba2145d5fc)PRS0\_SYNCH3\_PC3

| #define PRS0\_SYNCH3\_PC3   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x3) |
| --- |

## [◆ ](#aa8cc93aafe5498f4cc5a26d1fa37599e)PRS0\_SYNCH3\_PC4

| #define PRS0\_SYNCH3\_PC4   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x4) |
| --- |

## [◆ ](#a05496c3ac6cbd4310245f30c0810afbe)PRS0\_SYNCH3\_PC5

| #define PRS0\_SYNCH3\_PC5   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x5) |
| --- |

## [◆ ](#a6f198140e1506fd09800ff26f6223823)PRS0\_SYNCH3\_PC6

| #define PRS0\_SYNCH3\_PC6   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x6) |
| --- |

## [◆ ](#aedd84533e1397a94ca85f73644083d7d)PRS0\_SYNCH3\_PC7

| #define PRS0\_SYNCH3\_PC7   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x7) |
| --- |

## [◆ ](#ac149001c5cf25e43d4a72627b0f7168a)PRS0\_SYNCH3\_PC8

| #define PRS0\_SYNCH3\_PC8   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x8) |
| --- |

## [◆ ](#a5edaed4c458260db93f6a7190aed2375)PRS0\_SYNCH3\_PC9

| #define PRS0\_SYNCH3\_PC9   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x9) |
| --- |

## [◆ ](#a028ffbfde62bf2f28a08c99884d6fbb6)PRS0\_SYNCH3\_PD0

| #define PRS0\_SYNCH3\_PD0   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x3, 0x0) |
| --- |

## [◆ ](#a0d0ee2b67b86c4b2615f24e673966465)PRS0\_SYNCH3\_PD1

| #define PRS0\_SYNCH3\_PD1   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x3, 0x1) |
| --- |

## [◆ ](#a8dc61e39bff0c335982b5a775c9b000c)PRS0\_SYNCH3\_PD2

| #define PRS0\_SYNCH3\_PD2   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x3, 0x2) |
| --- |

## [◆ ](#a10deabf90e836f5bd478ad2a6483d2c8)PRS0\_SYNCH3\_PD3

| #define PRS0\_SYNCH3\_PD3   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x3, 0x3) |
| --- |

## [◆ ](#abf691edac97faf842650ff032300c7f2)PRS0\_SYNCH3\_PD4

| #define PRS0\_SYNCH3\_PD4   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x3, 0x4) |
| --- |

## [◆ ](#a89dcc2c57c15a6304f9e512b8fa7ae17)PRS0\_SYNCH3\_PD5

| #define PRS0\_SYNCH3\_PD5   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x3, 0x5) |
| --- |

## [◆ ](#a5bdf4f259033a31adaa4e25fe84604ed)PTI\_DCLK\_PC0

| #define PTI\_DCLK\_PC0   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x0) |
| --- |

## [◆ ](#aa4e24633e84b6487f85a598419ea7e7d)PTI\_DCLK\_PC1

| #define PTI\_DCLK\_PC1   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x1) |
| --- |

## [◆ ](#a53fa8c98bed45c485839c1d86d343733)PTI\_DCLK\_PC2

| #define PTI\_DCLK\_PC2   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x2) |
| --- |

## [◆ ](#a930a4ba462ce768196265ec5a53557ba)PTI\_DCLK\_PC3

| #define PTI\_DCLK\_PC3   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x3) |
| --- |

## [◆ ](#ae90e5e4841b04412ca3768216d0efaf1)PTI\_DCLK\_PC4

| #define PTI\_DCLK\_PC4   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x4) |
| --- |

## [◆ ](#a27b9c07fbbc05a0bd69dd74cc17db0d0)PTI\_DCLK\_PC5

| #define PTI\_DCLK\_PC5   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x5) |
| --- |

## [◆ ](#ae36628394c440c14e85b42db8095cba6)PTI\_DCLK\_PC6

| #define PTI\_DCLK\_PC6   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x6) |
| --- |

## [◆ ](#a024f81027127cdacccc05c4b49cf99c0)PTI\_DCLK\_PC7

| #define PTI\_DCLK\_PC7   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x7) |
| --- |

## [◆ ](#a8429fb0338b35f58958dafd47ad1112c)PTI\_DCLK\_PC8

| #define PTI\_DCLK\_PC8   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x8) |
| --- |

## [◆ ](#afe7de2b591c78a6f71d5cb7192cfb16a)PTI\_DCLK\_PC9

| #define PTI\_DCLK\_PC9   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x9) |
| --- |

## [◆ ](#a354b3eb4fe4c5e11e1c944761bf00095)PTI\_DCLK\_PD0

| #define PTI\_DCLK\_PD0   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x3, 0x0) |
| --- |

## [◆ ](#a14260512bf2682c2fb84fa96f00de9ba)PTI\_DCLK\_PD1

| #define PTI\_DCLK\_PD1   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x3, 0x1) |
| --- |

## [◆ ](#af96542673625d7a20712ad4c31953d4b)PTI\_DCLK\_PD2

| #define PTI\_DCLK\_PD2   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x3, 0x2) |
| --- |

## [◆ ](#ab234da9210beb7b1f94b75aa9ecf52ca)PTI\_DCLK\_PD3

| #define PTI\_DCLK\_PD3   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x3, 0x3) |
| --- |

## [◆ ](#ab16f467d07715a204580f48ed0affd78)PTI\_DCLK\_PD4

| #define PTI\_DCLK\_PD4   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x3, 0x4) |
| --- |

## [◆ ](#a5ed7f92ba37daf241ff2d2cd2b91ad5a)PTI\_DCLK\_PD5

| #define PTI\_DCLK\_PD5   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x3, 0x5) |
| --- |

## [◆ ](#aaa3fdc625a5f096099d23c1760980055)PTI\_DFRAME\_PC0

| #define PTI\_DFRAME\_PC0   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x0) |
| --- |

## [◆ ](#a23de813c7f0e88b8397ebcc34eb21552)PTI\_DFRAME\_PC1

| #define PTI\_DFRAME\_PC1   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x1) |
| --- |

## [◆ ](#a667adbc7570cf85833284a141de5fa2d)PTI\_DFRAME\_PC2

| #define PTI\_DFRAME\_PC2   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x2) |
| --- |

## [◆ ](#afea8ff0ad63b50a277e69f305b64e7cd)PTI\_DFRAME\_PC3

| #define PTI\_DFRAME\_PC3   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x3) |
| --- |

## [◆ ](#a97019cfae35bfc913e7ed2456a816ab5)PTI\_DFRAME\_PC4

| #define PTI\_DFRAME\_PC4   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x4) |
| --- |

## [◆ ](#a15d67770385d695409d975ba26d5d0e4)PTI\_DFRAME\_PC5

| #define PTI\_DFRAME\_PC5   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x5) |
| --- |

## [◆ ](#a318fe553b5da2adc9ce35e2571934bc2)PTI\_DFRAME\_PC6

| #define PTI\_DFRAME\_PC6   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x6) |
| --- |

## [◆ ](#a0e8e93d43d78096c24db5c4483ee68e1)PTI\_DFRAME\_PC7

| #define PTI\_DFRAME\_PC7   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x7) |
| --- |

## [◆ ](#ad45d6ab1196c50158fa81f54208fb789)PTI\_DFRAME\_PC8

| #define PTI\_DFRAME\_PC8   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x8) |
| --- |

## [◆ ](#a40af15964e0e47783a6a1855066201f5)PTI\_DFRAME\_PC9

| #define PTI\_DFRAME\_PC9   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x9) |
| --- |

## [◆ ](#ac6a830947b330b10ae2c9e3cdc1887b4)PTI\_DFRAME\_PD0

| #define PTI\_DFRAME\_PD0   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x3, 0x0) |
| --- |

## [◆ ](#a1f08a23bacafb3dae71d143c2c5ab863)PTI\_DFRAME\_PD1

| #define PTI\_DFRAME\_PD1   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x3, 0x1) |
| --- |

## [◆ ](#acafc4bcb7af54f59dbacb7d9ce8712ce)PTI\_DFRAME\_PD2

| #define PTI\_DFRAME\_PD2   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x3, 0x2) |
| --- |

## [◆ ](#aee415d6eae1beab453af125a316f549c)PTI\_DFRAME\_PD3

| #define PTI\_DFRAME\_PD3   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x3, 0x3) |
| --- |

## [◆ ](#a63eda1bcb309b3dfea7a3130fd2d8460)PTI\_DFRAME\_PD4

| #define PTI\_DFRAME\_PD4   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x3, 0x4) |
| --- |

## [◆ ](#acc221e5c9278b3e45f86dc8338599b5a)PTI\_DFRAME\_PD5

| #define PTI\_DFRAME\_PD5   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x3, 0x5) |
| --- |

## [◆ ](#a9413ff462e44dcf3b76204629c524a73)PTI\_DOUT\_PC0

| #define PTI\_DOUT\_PC0   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x0) |
| --- |

## [◆ ](#a49ef267b8afcafa1da426058b4f94d9f)PTI\_DOUT\_PC1

| #define PTI\_DOUT\_PC1   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x1) |
| --- |

## [◆ ](#a8563048b51841f44cbd35c573131bf18)PTI\_DOUT\_PC2

| #define PTI\_DOUT\_PC2   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x2) |
| --- |

## [◆ ](#aa4304d8154383f012e4a3b53a070b120)PTI\_DOUT\_PC3

| #define PTI\_DOUT\_PC3   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x3) |
| --- |

## [◆ ](#a715e7ceca236771ae00bb36143a586d2)PTI\_DOUT\_PC4

| #define PTI\_DOUT\_PC4   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x4) |
| --- |

## [◆ ](#aa2bb4223540e03b6ef7c21b05b76b380)PTI\_DOUT\_PC5

| #define PTI\_DOUT\_PC5   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x5) |
| --- |

## [◆ ](#a746b97fe77bb360b3048d3cc1730b607)PTI\_DOUT\_PC6

| #define PTI\_DOUT\_PC6   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x6) |
| --- |

## [◆ ](#a3e939dfef6c7f5f04abe8e32d0a866a2)PTI\_DOUT\_PC7

| #define PTI\_DOUT\_PC7   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x7) |
| --- |

## [◆ ](#a5aa40ec22bb634ae3425d3badf0fb9f0)PTI\_DOUT\_PC8

| #define PTI\_DOUT\_PC8   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x8) |
| --- |

## [◆ ](#aea6fe0d36dfddc5414d5e48df89c1a62)PTI\_DOUT\_PC9

| #define PTI\_DOUT\_PC9   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x9) |
| --- |

## [◆ ](#a569a588da9acdad8c7b18c6d7ee83681)PTI\_DOUT\_PD0

| #define PTI\_DOUT\_PD0   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x3, 0x0) |
| --- |

## [◆ ](#aac9876e72b5e68eb3d7138c72e7ac25b)PTI\_DOUT\_PD1

| #define PTI\_DOUT\_PD1   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x3, 0x1) |
| --- |

## [◆ ](#a447f3b579538e9a44615dfe77e8ace24)PTI\_DOUT\_PD2

| #define PTI\_DOUT\_PD2   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x3, 0x2) |
| --- |

## [◆ ](#ad80593f470c79948e0b9845cad0b739b)PTI\_DOUT\_PD3

| #define PTI\_DOUT\_PD3   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x3, 0x3) |
| --- |

## [◆ ](#a33b1e16afcb1e3b391e60dbe29b3bd1c)PTI\_DOUT\_PD4

| #define PTI\_DOUT\_PD4   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x3, 0x4) |
| --- |

## [◆ ](#a641c634d830b9ee090f0ad85e361c8ff)PTI\_DOUT\_PD5

| #define PTI\_DOUT\_PD5   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x3, 0x5) |
| --- |

## [◆ ](#a1f03fc6bcf9a20f2f39b4d91cf302d63)SILABS\_DBUS\_ACMP0\_ACMPOUT

| #define SILABS\_DBUS\_ACMP0\_ACMPOUT | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 4, 1, 0, 1)

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)

#define SILABS\_DBUS(port, pin, periph\_base, en\_present, en\_bit, route)

**Definition** silabs-pinctrl-dbus.h:47

## [◆ ](#a12ac63e4d5ed67a2a3f7425b751cdec3)SILABS\_DBUS\_ACMP1\_ACMPOUT

| #define SILABS\_DBUS\_ACMP1\_ACMPOUT | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 7, 1, 0, 1)

## [◆ ](#a19d73eca7da5c8b8622b3cb155ab4e6c)SILABS\_DBUS\_CMU\_CLKIN0

| #define SILABS\_DBUS\_CMU\_CLKIN0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 10, 0, 0, 1)

## [◆ ](#a6d193d353f76cad0e7da5c584625e996)SILABS\_DBUS\_CMU\_CLKOUT0

| #define SILABS\_DBUS\_CMU\_CLKOUT0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 10, 1, 0, 2)

## [◆ ](#a3f7ded37227446a05137a47c9a466894)SILABS\_DBUS\_CMU\_CLKOUT1

| #define SILABS\_DBUS\_CMU\_CLKOUT1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 10, 1, 1, 3)

## [◆ ](#a67d6fb886df9d589e447bd9332252d62)SILABS\_DBUS\_CMU\_CLKOUT2

| #define SILABS\_DBUS\_CMU\_CLKOUT2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 10, 1, 2, 4)

## [◆ ](#ab4cc7cd42d85332e7b423dae99d2b50e)SILABS\_DBUS\_EUSART0\_CS

| #define SILABS\_DBUS\_EUSART0\_CS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 21, 1, 0, 1)

## [◆ ](#ae1a52ec67ff061f1550ee177f83a0ea7)SILABS\_DBUS\_EUSART0\_CTS

| #define SILABS\_DBUS\_EUSART0\_CTS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 21, 0, 0, 2)

## [◆ ](#a9641ae53cb0f49b6bad7814adf078508)SILABS\_DBUS\_EUSART0\_RTS

| #define SILABS\_DBUS\_EUSART0\_RTS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 21, 1, 1, 3)

## [◆ ](#afc8334b04cee683c97518ae5a1ae34d4)SILABS\_DBUS\_EUSART0\_RX

| #define SILABS\_DBUS\_EUSART0\_RX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 21, 1, 2, 4)

## [◆ ](#a8a3d16b25db63819d80b010beb7d47ef)SILABS\_DBUS\_EUSART0\_SCLK

| #define SILABS\_DBUS\_EUSART0\_SCLK | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 21, 1, 3, 5)

## [◆ ](#a931fcc8e3c2da7642467f93f7fff0e71)SILABS\_DBUS\_EUSART0\_TX

| #define SILABS\_DBUS\_EUSART0\_TX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 21, 1, 4, 6)

## [◆ ](#ac3e145872ad81776dafad7dd8145f9b1)SILABS\_DBUS\_EUSART1\_CS

| #define SILABS\_DBUS\_EUSART1\_CS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 29, 1, 0, 1)

## [◆ ](#ad059fbad09ad887f644c51fc1963f4df)SILABS\_DBUS\_EUSART1\_CTS

| #define SILABS\_DBUS\_EUSART1\_CTS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 29, 0, 0, 2)

## [◆ ](#a3d9d1df82dd7e8a060d36353bbb00f18)SILABS\_DBUS\_EUSART1\_RTS

| #define SILABS\_DBUS\_EUSART1\_RTS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 29, 1, 1, 3)

## [◆ ](#af1675cdac7ef1fbf39f79665746a74c9)SILABS\_DBUS\_EUSART1\_RX

| #define SILABS\_DBUS\_EUSART1\_RX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 29, 1, 2, 4)

## [◆ ](#a8f10a814a0b2af37cc01f4b93780c12f)SILABS\_DBUS\_EUSART1\_SCLK

| #define SILABS\_DBUS\_EUSART1\_SCLK | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 29, 1, 3, 5)

## [◆ ](#adb612d2f22dc57f485e22fe674efb442)SILABS\_DBUS\_EUSART1\_TX

| #define SILABS\_DBUS\_EUSART1\_TX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 29, 1, 4, 6)

## [◆ ](#a9e2c3084524d9b100defb0a6c9c62c4e)SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC

| #define SILABS\_DBUS\_HFXO0\_BUFOUTREQINASYNC | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 142, 0, 0, 0)

## [◆ ](#a652b5412868f09aff727d2a84ce5efd6)SILABS\_DBUS\_I2C0\_SCL

| #define SILABS\_DBUS\_I2C0\_SCL | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 42, 1, 0, 1)

## [◆ ](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)SILABS\_DBUS\_I2C0\_SDA

| #define SILABS\_DBUS\_I2C0\_SDA | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 42, 1, 1, 2)

## [◆ ](#aa55669252ab4d30ff2044a7ac5e8fad1)SILABS\_DBUS\_I2C1\_SCL

| #define SILABS\_DBUS\_I2C1\_SCL | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 46, 1, 0, 1)

## [◆ ](#a0c32c2f4351441d0a97a445627912904)SILABS\_DBUS\_I2C1\_SDA

| #define SILABS\_DBUS\_I2C1\_SDA | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 46, 1, 1, 2)

## [◆ ](#a8debbf4560f2146abebba2cab72a0b95)SILABS\_DBUS\_KEYSCAN\_COLOUT0

| #define SILABS\_DBUS\_KEYSCAN\_COLOUT0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 50, 1, 0, 1)

## [◆ ](#a64f28976cada3adedec8c5009842bf36)SILABS\_DBUS\_KEYSCAN\_COLOUT1

| #define SILABS\_DBUS\_KEYSCAN\_COLOUT1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 50, 1, 1, 2)

## [◆ ](#a5647a9273865ecbe7da48783a8b3c121)SILABS\_DBUS\_KEYSCAN\_COLOUT2

| #define SILABS\_DBUS\_KEYSCAN\_COLOUT2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 50, 1, 2, 3)

## [◆ ](#afa0c224603ec9ec120dac7bc6a4feadf)SILABS\_DBUS\_KEYSCAN\_COLOUT3

| #define SILABS\_DBUS\_KEYSCAN\_COLOUT3 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 50, 1, 3, 4)

## [◆ ](#a05d4eb11707be913f27fecd9b1cac85c)SILABS\_DBUS\_KEYSCAN\_COLOUT4

| #define SILABS\_DBUS\_KEYSCAN\_COLOUT4 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 50, 1, 4, 5)

## [◆ ](#aeee19264cf4f46f09af1ffb8f168c81d)SILABS\_DBUS\_KEYSCAN\_COLOUT5

| #define SILABS\_DBUS\_KEYSCAN\_COLOUT5 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 50, 1, 5, 6)

## [◆ ](#afdfdf17591fe03c49b32ee3432529e3b)SILABS\_DBUS\_KEYSCAN\_COLOUT6

| #define SILABS\_DBUS\_KEYSCAN\_COLOUT6 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 50, 1, 6, 7)

## [◆ ](#a3c331cf1aa193f1a80192cc460229d95)SILABS\_DBUS\_KEYSCAN\_COLOUT7

| #define SILABS\_DBUS\_KEYSCAN\_COLOUT7 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 50, 1, 7, 8)

## [◆ ](#a2015d499c18fa403414add3e314f10cc)SILABS\_DBUS\_KEYSCAN\_ROWSENSE0

| #define SILABS\_DBUS\_KEYSCAN\_ROWSENSE0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 50, 0, 0, 9)

## [◆ ](#a9add4d6cdd61c94ac66169eb15dfed48)SILABS\_DBUS\_KEYSCAN\_ROWSENSE1

| #define SILABS\_DBUS\_KEYSCAN\_ROWSENSE1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 50, 0, 0, 10)

## [◆ ](#a5666436f80195c2c336196fc688ee2dd)SILABS\_DBUS\_KEYSCAN\_ROWSENSE2

| #define SILABS\_DBUS\_KEYSCAN\_ROWSENSE2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 50, 0, 0, 11)

## [◆ ](#a7e2c4eb1db1321a1f7810af45b5cd52c)SILABS\_DBUS\_KEYSCAN\_ROWSENSE3

| #define SILABS\_DBUS\_KEYSCAN\_ROWSENSE3 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 50, 0, 0, 12)

## [◆ ](#a5cacf707c77181c179dca5145050962e)SILABS\_DBUS\_KEYSCAN\_ROWSENSE4

| #define SILABS\_DBUS\_KEYSCAN\_ROWSENSE4 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 50, 0, 0, 13)

## [◆ ](#a9fed939ba0fda9f26a468e54c46b0f28)SILABS\_DBUS\_KEYSCAN\_ROWSENSE5

| #define SILABS\_DBUS\_KEYSCAN\_ROWSENSE5 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 50, 0, 0, 14)

## [◆ ](#ab81ce78522519bd5a5e257c8f4f2c27f)SILABS\_DBUS\_LETIMER0\_OUT0

| #define SILABS\_DBUS\_LETIMER0\_OUT0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 66, 1, 0, 1)

## [◆ ](#a2effaa50da9b899d91eb127cdf554098)SILABS\_DBUS\_LETIMER0\_OUT1

| #define SILABS\_DBUS\_LETIMER0\_OUT1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 66, 1, 1, 2)

## [◆ ](#a0225f18d061c851599210b56aeb42231)SILABS\_DBUS\_MODEM\_ANT0

| #define SILABS\_DBUS\_MODEM\_ANT0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 70, 1, 0, 1)

## [◆ ](#aaff7073911479298cda7729646f6990e)SILABS\_DBUS\_MODEM\_ANT1

| #define SILABS\_DBUS\_MODEM\_ANT1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 70, 1, 1, 2)

## [◆ ](#ac618ed85f554e3e852ad256d20ad95d5)SILABS\_DBUS\_MODEM\_ANTROLLOVER

| #define SILABS\_DBUS\_MODEM\_ANTROLLOVER | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 70, 1, 2, 3)

## [◆ ](#a076fd7a7e8083517d750f0ef332faefe)SILABS\_DBUS\_MODEM\_ANTRR0

| #define SILABS\_DBUS\_MODEM\_ANTRR0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 70, 1, 3, 4)

## [◆ ](#a4415eef2a0f03f68eeec9f39cfa00772)SILABS\_DBUS\_MODEM\_ANTRR1

| #define SILABS\_DBUS\_MODEM\_ANTRR1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 70, 1, 4, 5)

## [◆ ](#a1913f830f7d6a4234ffb12e0701b0019)SILABS\_DBUS\_MODEM\_ANTRR2

| #define SILABS\_DBUS\_MODEM\_ANTRR2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 70, 1, 5, 6)

## [◆ ](#ab9c8e475b9d5d1a9dae206aaa9b639b1)SILABS\_DBUS\_MODEM\_ANTRR3

| #define SILABS\_DBUS\_MODEM\_ANTRR3 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 70, 1, 6, 7)

## [◆ ](#a8da1060fdb49bad378f130183b73dd13)SILABS\_DBUS\_MODEM\_ANTRR4

| #define SILABS\_DBUS\_MODEM\_ANTRR4 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 70, 1, 7, 8)

## [◆ ](#aab2d172c20010568167c80096a97da23)SILABS\_DBUS\_MODEM\_ANTRR5

| #define SILABS\_DBUS\_MODEM\_ANTRR5 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 70, 1, 8, 9)

## [◆ ](#a7af41447a0035cf8fb73804c40eb3502)SILABS\_DBUS\_MODEM\_ANTSWEN

| #define SILABS\_DBUS\_MODEM\_ANTSWEN | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 70, 1, 9, 10)

## [◆ ](#ab828720727a5b918ca11b9ff3a119b44)SILABS\_DBUS\_MODEM\_ANTSWUS

| #define SILABS\_DBUS\_MODEM\_ANTSWUS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 70, 1, 10, 11)

## [◆ ](#a548bcbbd7ee4b87c6611d4fdb348984e)SILABS\_DBUS\_MODEM\_ANTTRIG

| #define SILABS\_DBUS\_MODEM\_ANTTRIG | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 70, 1, 11, 12)

## [◆ ](#a07822fe9a1f6febeaf3745361b47d57b)SILABS\_DBUS\_MODEM\_ANTTRIGSTOP

| #define SILABS\_DBUS\_MODEM\_ANTTRIGSTOP | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 70, 1, 12, 13)

## [◆ ](#a7d3926059c8b0c608d6d2bce035555b6)SILABS\_DBUS\_MODEM\_DCLK

| #define SILABS\_DBUS\_MODEM\_DCLK | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 70, 1, 13, 14)

## [◆ ](#a82dfdd0e9ad82ab0c75f4a530620d34b)SILABS\_DBUS\_MODEM\_DIN

| #define SILABS\_DBUS\_MODEM\_DIN | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 70, 0, 0, 15)

## [◆ ](#a48c49cff2ed723238703ff1b75ba8ae7)SILABS\_DBUS\_MODEM\_DOUT

| #define SILABS\_DBUS\_MODEM\_DOUT | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 70, 1, 14, 16)

## [◆ ](#af0b9dac0e0dc17c7f7e0e5e6151df0a2)SILABS\_DBUS\_PCNT0\_S0IN

| #define SILABS\_DBUS\_PCNT0\_S0IN | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 89, 0, 0, 0)

## [◆ ](#ab083a5eb205a0db7773d74aa506cb8bd)SILABS\_DBUS\_PCNT0\_S1IN

| #define SILABS\_DBUS\_PCNT0\_S1IN | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 89, 0, 0, 1)

## [◆ ](#a55a10636beb81ba5bf195c83c45cc994)SILABS\_DBUS\_PRS0\_ASYNCH0

| #define SILABS\_DBUS\_PRS0\_ASYNCH0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 0, 1)

## [◆ ](#a8502ee8adb62210f0c02abdf38a54019)SILABS\_DBUS\_PRS0\_ASYNCH1

| #define SILABS\_DBUS\_PRS0\_ASYNCH1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 1, 2)

## [◆ ](#a48a4d109c810311436ee8add40794aba)SILABS\_DBUS\_PRS0\_ASYNCH10

| #define SILABS\_DBUS\_PRS0\_ASYNCH10 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 10, 11)

## [◆ ](#a7acd670bc40ebc057369a7c577a0b0c2)SILABS\_DBUS\_PRS0\_ASYNCH11

| #define SILABS\_DBUS\_PRS0\_ASYNCH11 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 11, 12)

## [◆ ](#a242292a4e61aa48e75fde0fe4d079f8c)SILABS\_DBUS\_PRS0\_ASYNCH12

| #define SILABS\_DBUS\_PRS0\_ASYNCH12 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 12, 13)

## [◆ ](#a147c1004a0bb3cb7a3b4577081362d8d)SILABS\_DBUS\_PRS0\_ASYNCH13

| #define SILABS\_DBUS\_PRS0\_ASYNCH13 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 13, 14)

## [◆ ](#aeea99277adc04a38c1ed7adf6120c8f6)SILABS\_DBUS\_PRS0\_ASYNCH14

| #define SILABS\_DBUS\_PRS0\_ASYNCH14 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 14, 15)

## [◆ ](#a2b0d1abf6d9dda91662191f12e941574)SILABS\_DBUS\_PRS0\_ASYNCH15

| #define SILABS\_DBUS\_PRS0\_ASYNCH15 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 15, 16)

## [◆ ](#a8065a08661b02239f79db443c11afac8)SILABS\_DBUS\_PRS0\_ASYNCH2

| #define SILABS\_DBUS\_PRS0\_ASYNCH2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 2, 3)

## [◆ ](#a39cb285c6310012108f37d510db7a86c)SILABS\_DBUS\_PRS0\_ASYNCH3

| #define SILABS\_DBUS\_PRS0\_ASYNCH3 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 3, 4)

## [◆ ](#ac419288481edbfee2df8711b0c037ba2)SILABS\_DBUS\_PRS0\_ASYNCH4

| #define SILABS\_DBUS\_PRS0\_ASYNCH4 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 4, 5)

## [◆ ](#a6d7577bd45bc2c6043463ef6df86e8a7)SILABS\_DBUS\_PRS0\_ASYNCH5

| #define SILABS\_DBUS\_PRS0\_ASYNCH5 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 5, 6)

## [◆ ](#afa3017107df002534d41165b790891dd)SILABS\_DBUS\_PRS0\_ASYNCH6

| #define SILABS\_DBUS\_PRS0\_ASYNCH6 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 6, 7)

## [◆ ](#ae5af1968989cc643d315e310eb840dcc)SILABS\_DBUS\_PRS0\_ASYNCH7

| #define SILABS\_DBUS\_PRS0\_ASYNCH7 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 7, 8)

## [◆ ](#a0d062ef8d1ababa72b60d08265ff7e25)SILABS\_DBUS\_PRS0\_ASYNCH8

| #define SILABS\_DBUS\_PRS0\_ASYNCH8 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 8, 9)

## [◆ ](#af0617799b4044665a4996276fcf1e2bf)SILABS\_DBUS\_PRS0\_ASYNCH9

| #define SILABS\_DBUS\_PRS0\_ASYNCH9 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 9, 10)

## [◆ ](#a1b8e171cd761535148063c9b81ed3ee0)SILABS\_DBUS\_PRS0\_SYNCH0

| #define SILABS\_DBUS\_PRS0\_SYNCH0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 16, 17)

## [◆ ](#a85d7bbcc208a977d14aa286a9576b432)SILABS\_DBUS\_PRS0\_SYNCH1

| #define SILABS\_DBUS\_PRS0\_SYNCH1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 17, 18)

## [◆ ](#a7340c07baee2cad6d5b685929c48151b)SILABS\_DBUS\_PRS0\_SYNCH2

| #define SILABS\_DBUS\_PRS0\_SYNCH2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 18, 19)

## [◆ ](#a131fc4f34da4d410665642dfd51b733b)SILABS\_DBUS\_PRS0\_SYNCH3

| #define SILABS\_DBUS\_PRS0\_SYNCH3 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 92, 1, 19, 20)

## [◆ ](#a3165d7b2623b12308b38c9abcf900642)SILABS\_DBUS\_PTI\_DCLK

| #define SILABS\_DBUS\_PTI\_DCLK | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 37, 1, 0, 1)

## [◆ ](#a12a23ec2045680c0521b20f50d421881)SILABS\_DBUS\_PTI\_DFRAME

| #define SILABS\_DBUS\_PTI\_DFRAME | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 37, 1, 1, 2)

## [◆ ](#ae418c8c258cc10d03e4d36b741827f82)SILABS\_DBUS\_PTI\_DOUT

| #define SILABS\_DBUS\_PTI\_DOUT | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 37, 1, 2, 3)

## [◆ ](#a3c1e00721fae8d8a77341fd56fbbc09c)SILABS\_DBUS\_RAC\_LNAEN

| #define SILABS\_DBUS\_RAC\_LNAEN | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 114, 1, 0, 1)

## [◆ ](#ab1282918e0b9bbe140c852b951260348)SILABS\_DBUS\_RAC\_PAEN

| #define SILABS\_DBUS\_RAC\_PAEN | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 114, 1, 1, 2)

## [◆ ](#ad1f44a36026d8dd0f50d48e95fc9e5b3)SILABS\_DBUS\_TIMER0\_CC0

| #define SILABS\_DBUS\_TIMER0\_CC0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 144, 1, 0, 1)

## [◆ ](#a1eb30c3f4f87f98b3da18bc2a602e7e6)SILABS\_DBUS\_TIMER0\_CC1

| #define SILABS\_DBUS\_TIMER0\_CC1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 144, 1, 1, 2)

## [◆ ](#a23896bac158177558e7f179e8f3382a6)SILABS\_DBUS\_TIMER0\_CC2

| #define SILABS\_DBUS\_TIMER0\_CC2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 144, 1, 2, 3)

## [◆ ](#a44f0ed489cab3a50241d605931d579b0)SILABS\_DBUS\_TIMER0\_CDTI0

| #define SILABS\_DBUS\_TIMER0\_CDTI0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 144, 1, 3, 4)

## [◆ ](#ae13240899cbf48ec4f6710bcabc4ded8)SILABS\_DBUS\_TIMER0\_CDTI1

| #define SILABS\_DBUS\_TIMER0\_CDTI1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 144, 1, 4, 5)

## [◆ ](#a38b6cbc6d13fa4030cb07f1e2fc59003)SILABS\_DBUS\_TIMER0\_CDTI2

| #define SILABS\_DBUS\_TIMER0\_CDTI2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 144, 1, 5, 6)

## [◆ ](#a67fb3b7635c0b3408ee6bdea0b861bd3)SILABS\_DBUS\_TIMER1\_CC0

| #define SILABS\_DBUS\_TIMER1\_CC0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 152, 1, 0, 1)

## [◆ ](#a2aa7458fe116434331629b24cf0e45f0)SILABS\_DBUS\_TIMER1\_CC1

| #define SILABS\_DBUS\_TIMER1\_CC1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 152, 1, 1, 2)

## [◆ ](#a237c2bb8f6da0300cb10b73fab4c7ec4)SILABS\_DBUS\_TIMER1\_CC2

| #define SILABS\_DBUS\_TIMER1\_CC2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 152, 1, 2, 3)

## [◆ ](#afd03aef40bfd2fcfec51db90b50a4ebf)SILABS\_DBUS\_TIMER1\_CDTI0

| #define SILABS\_DBUS\_TIMER1\_CDTI0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 152, 1, 3, 4)

## [◆ ](#aff14e83dc5f27682d1d76ddb75d8b08c)SILABS\_DBUS\_TIMER1\_CDTI1

| #define SILABS\_DBUS\_TIMER1\_CDTI1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 152, 1, 4, 5)

## [◆ ](#a33328da36cd2df624ded688165f9f319)SILABS\_DBUS\_TIMER1\_CDTI2

| #define SILABS\_DBUS\_TIMER1\_CDTI2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 152, 1, 5, 6)

## [◆ ](#a6f8eec2f0d2289a845062b5fe14a59b7)SILABS\_DBUS\_TIMER2\_CC0

| #define SILABS\_DBUS\_TIMER2\_CC0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 160, 1, 0, 1)

## [◆ ](#a1a5af09f79ed3f743efa31ec03d87cc6)SILABS\_DBUS\_TIMER2\_CC1

| #define SILABS\_DBUS\_TIMER2\_CC1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 160, 1, 1, 2)

## [◆ ](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)SILABS\_DBUS\_TIMER2\_CC2

| #define SILABS\_DBUS\_TIMER2\_CC2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 160, 1, 2, 3)

## [◆ ](#a648ec3c8dafb7f88dba23ea50dba4e8b)SILABS\_DBUS\_TIMER2\_CDTI0

| #define SILABS\_DBUS\_TIMER2\_CDTI0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 160, 1, 3, 4)

## [◆ ](#ab124eb8882de0913d017f81a32eae6d8)SILABS\_DBUS\_TIMER2\_CDTI1

| #define SILABS\_DBUS\_TIMER2\_CDTI1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 160, 1, 4, 5)

## [◆ ](#aac5b26da22ac4ef8f1f08354f8339130)SILABS\_DBUS\_TIMER2\_CDTI2

| #define SILABS\_DBUS\_TIMER2\_CDTI2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 160, 1, 5, 6)

## [◆ ](#adb617def54a24017bdcaafe228697dd5)SILABS\_DBUS\_TIMER3\_CC0

| #define SILABS\_DBUS\_TIMER3\_CC0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 168, 1, 0, 1)

## [◆ ](#ac522d8a27bbe4fcfba1e0cc282dee7c0)SILABS\_DBUS\_TIMER3\_CC1

| #define SILABS\_DBUS\_TIMER3\_CC1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 168, 1, 1, 2)

## [◆ ](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)SILABS\_DBUS\_TIMER3\_CC2

| #define SILABS\_DBUS\_TIMER3\_CC2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 168, 1, 2, 3)

## [◆ ](#abb9fc38bdcf044af8e89f8b5bd4eb339)SILABS\_DBUS\_TIMER3\_CDTI0

| #define SILABS\_DBUS\_TIMER3\_CDTI0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 168, 1, 3, 4)

## [◆ ](#a2c50f79deaf5192c644bb0b52832352d)SILABS\_DBUS\_TIMER3\_CDTI1

| #define SILABS\_DBUS\_TIMER3\_CDTI1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 168, 1, 4, 5)

## [◆ ](#a5f8e118916558ec753791e59baeefef0)SILABS\_DBUS\_TIMER3\_CDTI2

| #define SILABS\_DBUS\_TIMER3\_CDTI2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 168, 1, 5, 6)

## [◆ ](#ab5f1949dfc60e6afa576f77ac645a367)SILABS\_DBUS\_TIMER4\_CC0

| #define SILABS\_DBUS\_TIMER4\_CC0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 176, 1, 0, 1)

## [◆ ](#a9de72de2effcb9f9efdecf8925cbbf57)SILABS\_DBUS\_TIMER4\_CC1

| #define SILABS\_DBUS\_TIMER4\_CC1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 176, 1, 1, 2)

## [◆ ](#ae37d483d35f11fd70fa4cd48a7718ab9)SILABS\_DBUS\_TIMER4\_CC2

| #define SILABS\_DBUS\_TIMER4\_CC2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 176, 1, 2, 3)

## [◆ ](#a7a9532d9136447f798581c3f11f6608f)SILABS\_DBUS\_TIMER4\_CDTI0

| #define SILABS\_DBUS\_TIMER4\_CDTI0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 176, 1, 3, 4)

## [◆ ](#aa3a6b5984b119e066af677767169f2f8)SILABS\_DBUS\_TIMER4\_CDTI1

| #define SILABS\_DBUS\_TIMER4\_CDTI1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 176, 1, 4, 5)

## [◆ ](#ae21486ec9db5e77200e89be6227e33af)SILABS\_DBUS\_TIMER4\_CDTI2

| #define SILABS\_DBUS\_TIMER4\_CDTI2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 176, 1, 5, 6)

## [◆ ](#a14f60bd84a682fe99ccd93607ca87d6b)SILABS\_DBUS\_USART0\_CLK

| #define SILABS\_DBUS\_USART0\_CLK | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 184, 1, 3, 5)

## [◆ ](#acc127783c3de46fa1efd6bf86f632807)SILABS\_DBUS\_USART0\_CS

| #define SILABS\_DBUS\_USART0\_CS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 184, 1, 0, 1)

## [◆ ](#a0be14ba61b5fc707ef02e7ac6ba779cf)SILABS\_DBUS\_USART0\_CTS

| #define SILABS\_DBUS\_USART0\_CTS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 184, 0, 0, 2)

## [◆ ](#afb90351e31f6da6446c2fc3f5aaaf394)SILABS\_DBUS\_USART0\_RTS

| #define SILABS\_DBUS\_USART0\_RTS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 184, 1, 1, 3)

## [◆ ](#a8d9bee07c90a69ada0a392fbd15c9e44)SILABS\_DBUS\_USART0\_RX

| #define SILABS\_DBUS\_USART0\_RX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 184, 1, 2, 4)

## [◆ ](#aca2a3d6b7903947d127d8b6ea5d8c84a)SILABS\_DBUS\_USART0\_TX

| #define SILABS\_DBUS\_USART0\_TX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 184, 1, 4, 6)

## [◆ ](#a643451fe929eaf497b28b23570152dfa)TIMER0\_CC0\_PA0

| #define TIMER0\_CC0\_PA0   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x0) |
| --- |

## [◆ ](#a257ab281a2a05ec0cc41ad2e3b548dfb)TIMER0\_CC0\_PA1

| #define TIMER0\_CC0\_PA1   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x1) |
| --- |

## [◆ ](#a1382ce3a810d4e7056919091fe9514f5)TIMER0\_CC0\_PA2

| #define TIMER0\_CC0\_PA2   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x2) |
| --- |

## [◆ ](#a9a9109ad50309f2200302915ea5a2654)TIMER0\_CC0\_PA3

| #define TIMER0\_CC0\_PA3   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x3) |
| --- |

## [◆ ](#a035c1f38daa2aca747ced020035bd292)TIMER0\_CC0\_PA4

| #define TIMER0\_CC0\_PA4   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x4) |
| --- |

## [◆ ](#a4bfcb9dec6df42cdf9a1fe979354ae57)TIMER0\_CC0\_PA5

| #define TIMER0\_CC0\_PA5   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x5) |
| --- |

## [◆ ](#ad1a677a1839ff4de6cc82e6e17b5aae2)TIMER0\_CC0\_PA6

| #define TIMER0\_CC0\_PA6   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x6) |
| --- |

## [◆ ](#a83713df06a69164162a4b734434bccc5)TIMER0\_CC0\_PA7

| #define TIMER0\_CC0\_PA7   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x7) |
| --- |

## [◆ ](#ab20dff18cf40da11a2ebcc405819c7e8)TIMER0\_CC0\_PA8

| #define TIMER0\_CC0\_PA8   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x8) |
| --- |

## [◆ ](#a571a5fe0360d6539be28fa6c4fb552b5)TIMER0\_CC0\_PA9

| #define TIMER0\_CC0\_PA9   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x9) |
| --- |

## [◆ ](#a18fb1529d6c032c6755f3d5a0abf9c76)TIMER0\_CC0\_PB0

| #define TIMER0\_CC0\_PB0   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x1, 0x0) |
| --- |

## [◆ ](#adf86b7c1c4b41eaf900d8a02e912f7c2)TIMER0\_CC0\_PB1

| #define TIMER0\_CC0\_PB1   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x1, 0x1) |
| --- |

## [◆ ](#ab01379b7fede12eae4bf2dcd1415d360)TIMER0\_CC0\_PB2

| #define TIMER0\_CC0\_PB2   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x1, 0x2) |
| --- |

## [◆ ](#abad5725bf78d847e54ad1bed240eca11)TIMER0\_CC0\_PB3

| #define TIMER0\_CC0\_PB3   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x1, 0x3) |
| --- |

## [◆ ](#a6cac16610a7cff74400e55edd20ebc76)TIMER0\_CC0\_PB4

| #define TIMER0\_CC0\_PB4   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x1, 0x4) |
| --- |

## [◆ ](#ae1e296c30691bdcc024c791e02ab02a9)TIMER0\_CC0\_PB5

| #define TIMER0\_CC0\_PB5   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x1, 0x5) |
| --- |

## [◆ ](#af01197ecb61c8e13ed760c4f036d555f)TIMER0\_CC0\_PC0

| #define TIMER0\_CC0\_PC0   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x0) |
| --- |

## [◆ ](#ae82052a9a3803c36b447e75e30db22b5)TIMER0\_CC0\_PC1

| #define TIMER0\_CC0\_PC1   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x1) |
| --- |

## [◆ ](#a89bade3c8848eeccc253f9752b16790c)TIMER0\_CC0\_PC2

| #define TIMER0\_CC0\_PC2   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x2) |
| --- |

## [◆ ](#a8b2ec4704842a1824c29fba1f700292e)TIMER0\_CC0\_PC3

| #define TIMER0\_CC0\_PC3   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x3) |
| --- |

## [◆ ](#acd56df092cae914b4e416e932e2b9f59)TIMER0\_CC0\_PC4

| #define TIMER0\_CC0\_PC4   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x4) |
| --- |

## [◆ ](#a17bbebdef205a11b6021b510d62ff3b8)TIMER0\_CC0\_PC5

| #define TIMER0\_CC0\_PC5   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x5) |
| --- |

## [◆ ](#a183d951a3ba6704d8056c1f16658a81f)TIMER0\_CC0\_PC6

| #define TIMER0\_CC0\_PC6   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x6) |
| --- |

## [◆ ](#ae5baae49155bdc86220399e4c80d57e3)TIMER0\_CC0\_PC7

| #define TIMER0\_CC0\_PC7   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x7) |
| --- |

## [◆ ](#ab0fbe13863fbd23ca2e2a6e427bda4c7)TIMER0\_CC0\_PC8

| #define TIMER0\_CC0\_PC8   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x8) |
| --- |

## [◆ ](#a10493f4bdb0fd03110e1291ad8942adc)TIMER0\_CC0\_PC9

| #define TIMER0\_CC0\_PC9   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x9) |
| --- |

## [◆ ](#a3db86be83a2cf8932a653abbf93aed00)TIMER0\_CC0\_PD0

| #define TIMER0\_CC0\_PD0   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x3, 0x0) |
| --- |

## [◆ ](#a4350a7968647bb2f25b6b2637fef6ad1)TIMER0\_CC0\_PD1

| #define TIMER0\_CC0\_PD1   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x3, 0x1) |
| --- |

## [◆ ](#a4c8e3e5bdf2d6582e6182f3df56f606b)TIMER0\_CC0\_PD2

| #define TIMER0\_CC0\_PD2   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x3, 0x2) |
| --- |

## [◆ ](#a695f1eba6df77776fb45e9f69a6fd57a)TIMER0\_CC0\_PD3

| #define TIMER0\_CC0\_PD3   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x3, 0x3) |
| --- |

## [◆ ](#a36230412046558d27c68f98b3ad6bd17)TIMER0\_CC0\_PD4

| #define TIMER0\_CC0\_PD4   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x3, 0x4) |
| --- |

## [◆ ](#a81fd1dfd02ac2ca4daebf5ef99497979)TIMER0\_CC0\_PD5

| #define TIMER0\_CC0\_PD5   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x3, 0x5) |
| --- |

## [◆ ](#aa74131bdc087fb80e597e3d497ab9796)TIMER0\_CC1\_PA0

| #define TIMER0\_CC1\_PA0   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x0) |
| --- |

## [◆ ](#a4a841ee625298d042db41bc0cd385796)TIMER0\_CC1\_PA1

| #define TIMER0\_CC1\_PA1   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x1) |
| --- |

## [◆ ](#a69b83d879f0cb485ba4af8b3cf4844a1)TIMER0\_CC1\_PA2

| #define TIMER0\_CC1\_PA2   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x2) |
| --- |

## [◆ ](#a0b3cce5e9df6245edce583e307c70b7f)TIMER0\_CC1\_PA3

| #define TIMER0\_CC1\_PA3   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x3) |
| --- |

## [◆ ](#ae6724c9762d1a9ae311d902e930b337c)TIMER0\_CC1\_PA4

| #define TIMER0\_CC1\_PA4   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x4) |
| --- |

## [◆ ](#a2354f1d78e8686d9ea3c44dd9bac5b38)TIMER0\_CC1\_PA5

| #define TIMER0\_CC1\_PA5   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x5) |
| --- |

## [◆ ](#a1b634a95c42a9065c7307c1a13461f39)TIMER0\_CC1\_PA6

| #define TIMER0\_CC1\_PA6   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x6) |
| --- |

## [◆ ](#abd19b057060c325aa1fa13af9121671d)TIMER0\_CC1\_PA7

| #define TIMER0\_CC1\_PA7   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x7) |
| --- |

## [◆ ](#ac005d8b7842095517fc151d18aa0b649)TIMER0\_CC1\_PA8

| #define TIMER0\_CC1\_PA8   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x8) |
| --- |

## [◆ ](#a28fae7750ea6bbf6aebd2ff1c98827ed)TIMER0\_CC1\_PA9

| #define TIMER0\_CC1\_PA9   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x9) |
| --- |

## [◆ ](#a6b0f1898a3246e0dd5915d5f5014b53e)TIMER0\_CC1\_PB0

| #define TIMER0\_CC1\_PB0   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x1, 0x0) |
| --- |

## [◆ ](#a812c3aa15e23b7be5d70f052259722dc)TIMER0\_CC1\_PB1

| #define TIMER0\_CC1\_PB1   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x1, 0x1) |
| --- |

## [◆ ](#ab12ee18043cd8f1ac0050cc7f706c712)TIMER0\_CC1\_PB2

| #define TIMER0\_CC1\_PB2   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x1, 0x2) |
| --- |

## [◆ ](#a988e56db008ca4cfd5b6ef5072b2e78f)TIMER0\_CC1\_PB3

| #define TIMER0\_CC1\_PB3   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x1, 0x3) |
| --- |

## [◆ ](#ad7bf61540cbd3e042da81a14a3c7c51f)TIMER0\_CC1\_PB4

| #define TIMER0\_CC1\_PB4   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x1, 0x4) |
| --- |

## [◆ ](#ac2ce68f224599c5c9113185d822b07bd)TIMER0\_CC1\_PB5

| #define TIMER0\_CC1\_PB5   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x1, 0x5) |
| --- |

## [◆ ](#a5787f33a274113239c4f5e8abecdf9a2)TIMER0\_CC1\_PC0

| #define TIMER0\_CC1\_PC0   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x0) |
| --- |

## [◆ ](#a14c64ec2717df0534956326f806de22a)TIMER0\_CC1\_PC1

| #define TIMER0\_CC1\_PC1   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x1) |
| --- |

## [◆ ](#ad7ffea850def6f7001ed2471ce3a13b6)TIMER0\_CC1\_PC2

| #define TIMER0\_CC1\_PC2   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x2) |
| --- |

## [◆ ](#a3f40aa2528d1f936a0e6734c0227afb2)TIMER0\_CC1\_PC3

| #define TIMER0\_CC1\_PC3   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x3) |
| --- |

## [◆ ](#a72ab00cdfc58ff9f2aef06c5ee9e1e13)TIMER0\_CC1\_PC4

| #define TIMER0\_CC1\_PC4   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x4) |
| --- |

## [◆ ](#a7a0b8714592092cb219e214cd28da4c5)TIMER0\_CC1\_PC5

| #define TIMER0\_CC1\_PC5   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x5) |
| --- |

## [◆ ](#aa48fdfed86985e0415468b7488c9d38c)TIMER0\_CC1\_PC6

| #define TIMER0\_CC1\_PC6   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x6) |
| --- |

## [◆ ](#a29e63d266965c64f0903cc309f20cb22)TIMER0\_CC1\_PC7

| #define TIMER0\_CC1\_PC7   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x7) |
| --- |

## [◆ ](#aa6ea846d04a3405926cc2b9aae39ca3a)TIMER0\_CC1\_PC8

| #define TIMER0\_CC1\_PC8   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x8) |
| --- |

## [◆ ](#aacb2904fae1307f64016f45a4ae93adb)TIMER0\_CC1\_PC9

| #define TIMER0\_CC1\_PC9   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x9) |
| --- |

## [◆ ](#ad721fa41b15556e529252a63302e8320)TIMER0\_CC1\_PD0

| #define TIMER0\_CC1\_PD0   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x3, 0x0) |
| --- |

## [◆ ](#abdc57a8f13e515d62d84684433f4c399)TIMER0\_CC1\_PD1

| #define TIMER0\_CC1\_PD1   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x3, 0x1) |
| --- |

## [◆ ](#a6a00214723619c929a860d4d5fa82d70)TIMER0\_CC1\_PD2

| #define TIMER0\_CC1\_PD2   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x3, 0x2) |
| --- |

## [◆ ](#ab5fe2a23145e40055ae0f532309c45a4)TIMER0\_CC1\_PD3

| #define TIMER0\_CC1\_PD3   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x3, 0x3) |
| --- |

## [◆ ](#ad0bf7e8d2c24c8ebe7c2b594d99c9ead)TIMER0\_CC1\_PD4

| #define TIMER0\_CC1\_PD4   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x3, 0x4) |
| --- |

## [◆ ](#acfae72ccde9456c2300b98b14fc0c4e9)TIMER0\_CC1\_PD5

| #define TIMER0\_CC1\_PD5   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x3, 0x5) |
| --- |

## [◆ ](#a10518d21844ab1a787009973ac06ce22)TIMER0\_CC2\_PA0

| #define TIMER0\_CC2\_PA0   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x0) |
| --- |

## [◆ ](#a40b5d230cec35f97648678731d970520)TIMER0\_CC2\_PA1

| #define TIMER0\_CC2\_PA1   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x1) |
| --- |

## [◆ ](#a5183b3c3cec8352c11edef376fc346ad)TIMER0\_CC2\_PA2

| #define TIMER0\_CC2\_PA2   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x2) |
| --- |

## [◆ ](#aec173f24a643f2d50e4e2fe44b0d1dc8)TIMER0\_CC2\_PA3

| #define TIMER0\_CC2\_PA3   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x3) |
| --- |

## [◆ ](#a4df67f53e8e2501bed3fd9565a49c0d6)TIMER0\_CC2\_PA4

| #define TIMER0\_CC2\_PA4   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x4) |
| --- |

## [◆ ](#a0529c6f8022ee408363ecc6452ac2c44)TIMER0\_CC2\_PA5

| #define TIMER0\_CC2\_PA5   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x5) |
| --- |

## [◆ ](#a1e0f169ebf24d5954b875bd824b86de1)TIMER0\_CC2\_PA6

| #define TIMER0\_CC2\_PA6   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x6) |
| --- |

## [◆ ](#a59bb4e9a92765847c5c2a5173df27f1e)TIMER0\_CC2\_PA7

| #define TIMER0\_CC2\_PA7   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x7) |
| --- |

## [◆ ](#a4a131dbd8f75a91809fece6cba85fcc5)TIMER0\_CC2\_PA8

| #define TIMER0\_CC2\_PA8   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x8) |
| --- |

## [◆ ](#a2ae1d1ad9ad7658df2a0f667af493c52)TIMER0\_CC2\_PA9

| #define TIMER0\_CC2\_PA9   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x9) |
| --- |

## [◆ ](#ad7a7916ae90b8345be7279e50f18c190)TIMER0\_CC2\_PB0

| #define TIMER0\_CC2\_PB0   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x1, 0x0) |
| --- |

## [◆ ](#a36ccb83c4230c2f3d14accbb965b08cd)TIMER0\_CC2\_PB1

| #define TIMER0\_CC2\_PB1   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x1, 0x1) |
| --- |

## [◆ ](#ad02263c57d4f083872708a7c91ee515f)TIMER0\_CC2\_PB2

| #define TIMER0\_CC2\_PB2   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x1, 0x2) |
| --- |

## [◆ ](#aaeb96f9ff0dc83edf33cfef5c95430f6)TIMER0\_CC2\_PB3

| #define TIMER0\_CC2\_PB3   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x1, 0x3) |
| --- |

## [◆ ](#a5aa2d1d44c749859ed1f1e6e468e099e)TIMER0\_CC2\_PB4

| #define TIMER0\_CC2\_PB4   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x1, 0x4) |
| --- |

## [◆ ](#ac471bba7cb11d1561198d21869bcd7c5)TIMER0\_CC2\_PB5

| #define TIMER0\_CC2\_PB5   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x1, 0x5) |
| --- |

## [◆ ](#afe51827dd65359061f88753af6868eb5)TIMER0\_CC2\_PC0

| #define TIMER0\_CC2\_PC0   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x0) |
| --- |

## [◆ ](#ae3d14c1aa4739ba2be209c8490e05b9b)TIMER0\_CC2\_PC1

| #define TIMER0\_CC2\_PC1   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x1) |
| --- |

## [◆ ](#a12baff93c97c64f74538b1995171fab7)TIMER0\_CC2\_PC2

| #define TIMER0\_CC2\_PC2   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x2) |
| --- |

## [◆ ](#a96fe3aa3622573210ac344515718962f)TIMER0\_CC2\_PC3

| #define TIMER0\_CC2\_PC3   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x3) |
| --- |

## [◆ ](#ad70b84d782f9af43d146a34c1533f08a)TIMER0\_CC2\_PC4

| #define TIMER0\_CC2\_PC4   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x4) |
| --- |

## [◆ ](#a8bebf51e280fec4baea6e545ba0e8576)TIMER0\_CC2\_PC5

| #define TIMER0\_CC2\_PC5   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x5) |
| --- |

## [◆ ](#ab088658e226c6a3f754574378fa59fdc)TIMER0\_CC2\_PC6

| #define TIMER0\_CC2\_PC6   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x6) |
| --- |

## [◆ ](#a3248786ef86b22d8f8e6de854160ff6a)TIMER0\_CC2\_PC7

| #define TIMER0\_CC2\_PC7   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x7) |
| --- |

## [◆ ](#ab7744630c2e1590791b60272fefdfa8b)TIMER0\_CC2\_PC8

| #define TIMER0\_CC2\_PC8   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x8) |
| --- |

## [◆ ](#a5d487cfdd44d02257ccc3d2a02d48e72)TIMER0\_CC2\_PC9

| #define TIMER0\_CC2\_PC9   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x9) |
| --- |

## [◆ ](#a29a4b811b779721b8ab98976d0af976c)TIMER0\_CC2\_PD0

| #define TIMER0\_CC2\_PD0   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x3, 0x0) |
| --- |

## [◆ ](#a21d070a5f412c7a77e53f69c87c57997)TIMER0\_CC2\_PD1

| #define TIMER0\_CC2\_PD1   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x3, 0x1) |
| --- |

## [◆ ](#a419e2b988ac821a7b4e40fb925da5916)TIMER0\_CC2\_PD2

| #define TIMER0\_CC2\_PD2   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x3, 0x2) |
| --- |

## [◆ ](#aae16cb8df6cc099c3344c5740fd31e69)TIMER0\_CC2\_PD3

| #define TIMER0\_CC2\_PD3   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x3, 0x3) |
| --- |

## [◆ ](#ae97c73876fb35531996feaad9d43217f)TIMER0\_CC2\_PD4

| #define TIMER0\_CC2\_PD4   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x3, 0x4) |
| --- |

## [◆ ](#a012caa64d0e1ca3d85f6d0a68ea57c25)TIMER0\_CC2\_PD5

| #define TIMER0\_CC2\_PD5   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x3, 0x5) |
| --- |

## [◆ ](#a583547311775fdf98f4d19afb149ac6c)TIMER0\_CDTI0\_PA0

| #define TIMER0\_CDTI0\_PA0   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x0) |
| --- |

## [◆ ](#a8005c42773c60dd5aec6e3ee8f4b7491)TIMER0\_CDTI0\_PA1

| #define TIMER0\_CDTI0\_PA1   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x1) |
| --- |

## [◆ ](#a78955dc51203c015d86b442978ad260e)TIMER0\_CDTI0\_PA2

| #define TIMER0\_CDTI0\_PA2   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x2) |
| --- |

## [◆ ](#a291a17c15340c09f32a3c63e3da95a9c)TIMER0\_CDTI0\_PA3

| #define TIMER0\_CDTI0\_PA3   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x3) |
| --- |

## [◆ ](#ab3b70d25fa01aaade758c277465c9639)TIMER0\_CDTI0\_PA4

| #define TIMER0\_CDTI0\_PA4   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x4) |
| --- |

## [◆ ](#a025bd51e6c211605497795d76e175510)TIMER0\_CDTI0\_PA5

| #define TIMER0\_CDTI0\_PA5   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x5) |
| --- |

## [◆ ](#a17617cf4fecd500e152bc39ef84e009b)TIMER0\_CDTI0\_PA6

| #define TIMER0\_CDTI0\_PA6   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x6) |
| --- |

## [◆ ](#aee12a8ee669b0201ff7557c15b2fc6d5)TIMER0\_CDTI0\_PA7

| #define TIMER0\_CDTI0\_PA7   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x7) |
| --- |

## [◆ ](#add042bfe988b01b650b3855a407e71cf)TIMER0\_CDTI0\_PA8

| #define TIMER0\_CDTI0\_PA8   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x8) |
| --- |

## [◆ ](#a7d3dd78baac35ece4d59da8f277bb3ce)TIMER0\_CDTI0\_PA9

| #define TIMER0\_CDTI0\_PA9   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x9) |
| --- |

## [◆ ](#ac08f3bf826c3d909d06c67c2acb418ef)TIMER0\_CDTI0\_PB0

| #define TIMER0\_CDTI0\_PB0   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x1, 0x0) |
| --- |

## [◆ ](#aaf1bd6f6922c1316131edb6cb0f3de9e)TIMER0\_CDTI0\_PB1

| #define TIMER0\_CDTI0\_PB1   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x1, 0x1) |
| --- |

## [◆ ](#af8a99eb0ed525295713c0158c7c0325f)TIMER0\_CDTI0\_PB2

| #define TIMER0\_CDTI0\_PB2   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x1, 0x2) |
| --- |

## [◆ ](#addeeb5046eef54b417ce88ff5938efac)TIMER0\_CDTI0\_PB3

| #define TIMER0\_CDTI0\_PB3   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x1, 0x3) |
| --- |

## [◆ ](#a45b93c4fd05e5bf784cc1ed50162df94)TIMER0\_CDTI0\_PB4

| #define TIMER0\_CDTI0\_PB4   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x1, 0x4) |
| --- |

## [◆ ](#a4e7041a6a34a7f48464cdd161cd0ac9b)TIMER0\_CDTI0\_PB5

| #define TIMER0\_CDTI0\_PB5   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x1, 0x5) |
| --- |

## [◆ ](#a5f22a6e89d3fb5e3bb7925fdbe1c2e38)TIMER0\_CDTI0\_PC0

| #define TIMER0\_CDTI0\_PC0   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x0) |
| --- |

## [◆ ](#a72ef54f11ed78d2e16f007d394030955)TIMER0\_CDTI0\_PC1

| #define TIMER0\_CDTI0\_PC1   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x1) |
| --- |

## [◆ ](#a3f65837c636c8b483c7130555c34a54c)TIMER0\_CDTI0\_PC2

| #define TIMER0\_CDTI0\_PC2   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x2) |
| --- |

## [◆ ](#acbf891b0c24b9af901264aba00b84f64)TIMER0\_CDTI0\_PC3

| #define TIMER0\_CDTI0\_PC3   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x3) |
| --- |

## [◆ ](#adf859e578ce341428c887d8267d962bf)TIMER0\_CDTI0\_PC4

| #define TIMER0\_CDTI0\_PC4   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x4) |
| --- |

## [◆ ](#ae57392b6eb47339eb4e5bd89840d19a9)TIMER0\_CDTI0\_PC5

| #define TIMER0\_CDTI0\_PC5   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x5) |
| --- |

## [◆ ](#a5da4268d82621edce0d73e495eeaeffc)TIMER0\_CDTI0\_PC6

| #define TIMER0\_CDTI0\_PC6   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x6) |
| --- |

## [◆ ](#a18354cd70447a811e3cfeb92e6300aaf)TIMER0\_CDTI0\_PC7

| #define TIMER0\_CDTI0\_PC7   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x7) |
| --- |

## [◆ ](#a15ceb91e88d25022c336d56444eb106f)TIMER0\_CDTI0\_PC8

| #define TIMER0\_CDTI0\_PC8   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x8) |
| --- |

## [◆ ](#a9e47ff2f69c353ec76af5964c5ba70fd)TIMER0\_CDTI0\_PC9

| #define TIMER0\_CDTI0\_PC9   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x9) |
| --- |

## [◆ ](#abe060cc518151861fccab2604541e238)TIMER0\_CDTI0\_PD0

| #define TIMER0\_CDTI0\_PD0   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x3, 0x0) |
| --- |

## [◆ ](#a0925901af2c13317cf4f43c50e01d83a)TIMER0\_CDTI0\_PD1

| #define TIMER0\_CDTI0\_PD1   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x3, 0x1) |
| --- |

## [◆ ](#aed6dd4aa21be7afbe03d984356d36e32)TIMER0\_CDTI0\_PD2

| #define TIMER0\_CDTI0\_PD2   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x3, 0x2) |
| --- |

## [◆ ](#aa52d4d7a010abe242632b4574332349b)TIMER0\_CDTI0\_PD3

| #define TIMER0\_CDTI0\_PD3   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x3, 0x3) |
| --- |

## [◆ ](#ae8b70f7461db674d1d9c3f2ea91701cc)TIMER0\_CDTI0\_PD4

| #define TIMER0\_CDTI0\_PD4   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x3, 0x4) |
| --- |

## [◆ ](#aadc1f7305d8c880746d39c607414346b)TIMER0\_CDTI0\_PD5

| #define TIMER0\_CDTI0\_PD5   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x3, 0x5) |
| --- |

## [◆ ](#a757add3c35ee9b20b8bb75363620e57f)TIMER0\_CDTI1\_PA0

| #define TIMER0\_CDTI1\_PA0   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x0) |
| --- |

## [◆ ](#a39b01d816f29ff5114ac045475ad1c80)TIMER0\_CDTI1\_PA1

| #define TIMER0\_CDTI1\_PA1   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x1) |
| --- |

## [◆ ](#a648e126ee7e0bdf5faff238a097c6e5e)TIMER0\_CDTI1\_PA2

| #define TIMER0\_CDTI1\_PA2   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x2) |
| --- |

## [◆ ](#a0e36cbcf42a86fa70f9561b1a817831d)TIMER0\_CDTI1\_PA3

| #define TIMER0\_CDTI1\_PA3   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x3) |
| --- |

## [◆ ](#a12661cbedaeab2177edf943b1f752b6b)TIMER0\_CDTI1\_PA4

| #define TIMER0\_CDTI1\_PA4   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x4) |
| --- |

## [◆ ](#a9012c36cbc093ebb308af9118eabfde9)TIMER0\_CDTI1\_PA5

| #define TIMER0\_CDTI1\_PA5   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x5) |
| --- |

## [◆ ](#ac4ab807c106f7b9bc718e931d517c791)TIMER0\_CDTI1\_PA6

| #define TIMER0\_CDTI1\_PA6   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x6) |
| --- |

## [◆ ](#ada3087b05c215a2484cf068cdc1494f7)TIMER0\_CDTI1\_PA7

| #define TIMER0\_CDTI1\_PA7   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x7) |
| --- |

## [◆ ](#a5c0a03d2f318b94a19795fb40e767285)TIMER0\_CDTI1\_PA8

| #define TIMER0\_CDTI1\_PA8   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x8) |
| --- |

## [◆ ](#a63d88961b85a0fdc91f6df0ac6dbf069)TIMER0\_CDTI1\_PA9

| #define TIMER0\_CDTI1\_PA9   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x9) |
| --- |

## [◆ ](#a8b1c6a4724744e459918508925be254e)TIMER0\_CDTI1\_PB0

| #define TIMER0\_CDTI1\_PB0   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x1, 0x0) |
| --- |

## [◆ ](#a9206a9ae50fbe6a063df918f0dc7d9b5)TIMER0\_CDTI1\_PB1

| #define TIMER0\_CDTI1\_PB1   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x1, 0x1) |
| --- |

## [◆ ](#a7ca452eeecf6b0b1a6f833b5332244cf)TIMER0\_CDTI1\_PB2

| #define TIMER0\_CDTI1\_PB2   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x1, 0x2) |
| --- |

## [◆ ](#ae206d9477b7cad08f2fc30af80bc08f8)TIMER0\_CDTI1\_PB3

| #define TIMER0\_CDTI1\_PB3   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x1, 0x3) |
| --- |

## [◆ ](#ad1d178e1d6fb8768959e4b8b04ab18e3)TIMER0\_CDTI1\_PB4

| #define TIMER0\_CDTI1\_PB4   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x1, 0x4) |
| --- |

## [◆ ](#aa98d1c28a8531bfbbd82fe7bf6d9727d)TIMER0\_CDTI1\_PB5

| #define TIMER0\_CDTI1\_PB5   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x1, 0x5) |
| --- |

## [◆ ](#ad5eb7a31fde2301a819d1f7fb3fa4120)TIMER0\_CDTI1\_PC0

| #define TIMER0\_CDTI1\_PC0   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x0) |
| --- |

## [◆ ](#a67c242881dc443329a04f2148b5d3171)TIMER0\_CDTI1\_PC1

| #define TIMER0\_CDTI1\_PC1   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x1) |
| --- |

## [◆ ](#a6e61b116d02e63455d54f16e29168dfe)TIMER0\_CDTI1\_PC2

| #define TIMER0\_CDTI1\_PC2   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x2) |
| --- |

## [◆ ](#a904d89c160a99cc883673a11164eb00a)TIMER0\_CDTI1\_PC3

| #define TIMER0\_CDTI1\_PC3   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x3) |
| --- |

## [◆ ](#afa348bc98e1aa83ec82924c1c49a5970)TIMER0\_CDTI1\_PC4

| #define TIMER0\_CDTI1\_PC4   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x4) |
| --- |

## [◆ ](#a43e280a63df1054883f731736d864712)TIMER0\_CDTI1\_PC5

| #define TIMER0\_CDTI1\_PC5   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x5) |
| --- |

## [◆ ](#a7ffd35a5c906b6416b44621024daec1f)TIMER0\_CDTI1\_PC6

| #define TIMER0\_CDTI1\_PC6   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x6) |
| --- |

## [◆ ](#a7001978e8da4cd34b0da45ca39fda8f1)TIMER0\_CDTI1\_PC7

| #define TIMER0\_CDTI1\_PC7   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x7) |
| --- |

## [◆ ](#aa8259c92e23f5eabef443bde8ddc7f76)TIMER0\_CDTI1\_PC8

| #define TIMER0\_CDTI1\_PC8   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x8) |
| --- |

## [◆ ](#aaefdbc2277ffe2c275e7c77b1bfb90cf)TIMER0\_CDTI1\_PC9

| #define TIMER0\_CDTI1\_PC9   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x9) |
| --- |

## [◆ ](#a713013e442d42bf60f0f8a2df0e178de)TIMER0\_CDTI1\_PD0

| #define TIMER0\_CDTI1\_PD0   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x3, 0x0) |
| --- |

## [◆ ](#a28cc02c56e4eb397f3fc9d106db59dd3)TIMER0\_CDTI1\_PD1

| #define TIMER0\_CDTI1\_PD1   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x3, 0x1) |
| --- |

## [◆ ](#a7a3ee64de9bcf3d3e05cad7c0eb51492)TIMER0\_CDTI1\_PD2

| #define TIMER0\_CDTI1\_PD2   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x3, 0x2) |
| --- |

## [◆ ](#ac0570e1fa46ef8d9015c9e41cede4394)TIMER0\_CDTI1\_PD3

| #define TIMER0\_CDTI1\_PD3   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x3, 0x3) |
| --- |

## [◆ ](#a159917b90b0f5f1040afe53b172ca26f)TIMER0\_CDTI1\_PD4

| #define TIMER0\_CDTI1\_PD4   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x3, 0x4) |
| --- |

## [◆ ](#a13e86004fc3aa0f53c5f2b9404d46703)TIMER0\_CDTI1\_PD5

| #define TIMER0\_CDTI1\_PD5   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x3, 0x5) |
| --- |

## [◆ ](#a723140878fb318fc60e62886e8e4bb6b)TIMER0\_CDTI2\_PA0

| #define TIMER0\_CDTI2\_PA0   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x0) |
| --- |

## [◆ ](#a69ea746a21b0305be02db15ba8ced4dc)TIMER0\_CDTI2\_PA1

| #define TIMER0\_CDTI2\_PA1   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x1) |
| --- |

## [◆ ](#a63e2744f17ec7b868e38010999a5b99e)TIMER0\_CDTI2\_PA2

| #define TIMER0\_CDTI2\_PA2   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x2) |
| --- |

## [◆ ](#ad9c1f9c457c63b9f7ee15cedb89c8b29)TIMER0\_CDTI2\_PA3

| #define TIMER0\_CDTI2\_PA3   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x3) |
| --- |

## [◆ ](#ac5e02eb43bbc85c4e07976539d1c7b66)TIMER0\_CDTI2\_PA4

| #define TIMER0\_CDTI2\_PA4   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x4) |
| --- |

## [◆ ](#a17440dab813cdc7a4b58682db3c0aa3c)TIMER0\_CDTI2\_PA5

| #define TIMER0\_CDTI2\_PA5   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x5) |
| --- |

## [◆ ](#a967cbd605349c15eada5527602a05fc9)TIMER0\_CDTI2\_PA6

| #define TIMER0\_CDTI2\_PA6   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x6) |
| --- |

## [◆ ](#a3ee02bd72164f5ddab71818f5dc34616)TIMER0\_CDTI2\_PA7

| #define TIMER0\_CDTI2\_PA7   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x7) |
| --- |

## [◆ ](#a9e6862b3fbfa9272f0401ed722a7452c)TIMER0\_CDTI2\_PA8

| #define TIMER0\_CDTI2\_PA8   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x8) |
| --- |

## [◆ ](#a5e30587d905a27e406a3e5956ba0a9be)TIMER0\_CDTI2\_PA9

| #define TIMER0\_CDTI2\_PA9   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x9) |
| --- |

## [◆ ](#a4a53984105a683a6807ad0a26e13a60d)TIMER0\_CDTI2\_PB0

| #define TIMER0\_CDTI2\_PB0   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x1, 0x0) |
| --- |

## [◆ ](#a12ffd91f7201f73e0d75c2298d5abce9)TIMER0\_CDTI2\_PB1

| #define TIMER0\_CDTI2\_PB1   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x1, 0x1) |
| --- |

## [◆ ](#a211506e052690ec459d7225ac9ec2dd1)TIMER0\_CDTI2\_PB2

| #define TIMER0\_CDTI2\_PB2   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x1, 0x2) |
| --- |

## [◆ ](#a6639dc47e82cbc98ba1aae88605e8c63)TIMER0\_CDTI2\_PB3

| #define TIMER0\_CDTI2\_PB3   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x1, 0x3) |
| --- |

## [◆ ](#a3cdd0a6bcde7f01a695284e11fe5946d)TIMER0\_CDTI2\_PB4

| #define TIMER0\_CDTI2\_PB4   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x1, 0x4) |
| --- |

## [◆ ](#a8485eeaa0e92fcb4a58048b40a19d8f3)TIMER0\_CDTI2\_PB5

| #define TIMER0\_CDTI2\_PB5   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x1, 0x5) |
| --- |

## [◆ ](#a11f7ac3b39604c06f639dc4b925ee93d)TIMER0\_CDTI2\_PC0

| #define TIMER0\_CDTI2\_PC0   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x0) |
| --- |

## [◆ ](#a2b6fa7363ef650a2847113779b5b36a7)TIMER0\_CDTI2\_PC1

| #define TIMER0\_CDTI2\_PC1   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x1) |
| --- |

## [◆ ](#a3d39899e0d3f88f22feffcd6752b2507)TIMER0\_CDTI2\_PC2

| #define TIMER0\_CDTI2\_PC2   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x2) |
| --- |

## [◆ ](#a0f6d66f601b1eaeae268c7ed2b0874ae)TIMER0\_CDTI2\_PC3

| #define TIMER0\_CDTI2\_PC3   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x3) |
| --- |

## [◆ ](#ab91374950c6d3774d25c5e6ee6068ce0)TIMER0\_CDTI2\_PC4

| #define TIMER0\_CDTI2\_PC4   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x4) |
| --- |

## [◆ ](#a2c76eb69ea9ed92aa328126bbad507d1)TIMER0\_CDTI2\_PC5

| #define TIMER0\_CDTI2\_PC5   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x5) |
| --- |

## [◆ ](#abbc57fb5b68e9956483bf9122e985bf2)TIMER0\_CDTI2\_PC6

| #define TIMER0\_CDTI2\_PC6   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x6) |
| --- |

## [◆ ](#ab4ee38f2ae41e0c6dfea802960c06146)TIMER0\_CDTI2\_PC7

| #define TIMER0\_CDTI2\_PC7   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x7) |
| --- |

## [◆ ](#ac7d002926fe9a298f1dfacb69f295d3f)TIMER0\_CDTI2\_PC8

| #define TIMER0\_CDTI2\_PC8   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x8) |
| --- |

## [◆ ](#af5a9b96754b28693de2ddd05994ddd2d)TIMER0\_CDTI2\_PC9

| #define TIMER0\_CDTI2\_PC9   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x9) |
| --- |

## [◆ ](#a038cef314d102bb50e58612327d456c6)TIMER0\_CDTI2\_PD0

| #define TIMER0\_CDTI2\_PD0   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x3, 0x0) |
| --- |

## [◆ ](#a008dea92e72e9d337f5a6d38aaf33661)TIMER0\_CDTI2\_PD1

| #define TIMER0\_CDTI2\_PD1   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x3, 0x1) |
| --- |

## [◆ ](#a7bf636029c51b394d749774c4961aeba)TIMER0\_CDTI2\_PD2

| #define TIMER0\_CDTI2\_PD2   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x3, 0x2) |
| --- |

## [◆ ](#a48403324a419bb99f173f8a5198d55a0)TIMER0\_CDTI2\_PD3

| #define TIMER0\_CDTI2\_PD3   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x3, 0x3) |
| --- |

## [◆ ](#ad15de743c118e7443cf6edf793243995)TIMER0\_CDTI2\_PD4

| #define TIMER0\_CDTI2\_PD4   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x3, 0x4) |
| --- |

## [◆ ](#a77d1bf1e082a09e8fbd78e9be93f0f39)TIMER0\_CDTI2\_PD5

| #define TIMER0\_CDTI2\_PD5   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x3, 0x5) |
| --- |

## [◆ ](#a4b3085c41f4ed8706a3b39755e5b132c)TIMER1\_CC0\_PA0

| #define TIMER1\_CC0\_PA0   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x0) |
| --- |

## [◆ ](#a5daa5510f5bab9cea855b3d3303daaaf)TIMER1\_CC0\_PA1

| #define TIMER1\_CC0\_PA1   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x1) |
| --- |

## [◆ ](#abc2afde49650332d28db97653adc501d)TIMER1\_CC0\_PA2

| #define TIMER1\_CC0\_PA2   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x2) |
| --- |

## [◆ ](#a2df5bd9733330e9a973732a8cc222ee9)TIMER1\_CC0\_PA3

| #define TIMER1\_CC0\_PA3   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x3) |
| --- |

## [◆ ](#a514654049642c780cd7eae508e0620b9)TIMER1\_CC0\_PA4

| #define TIMER1\_CC0\_PA4   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x4) |
| --- |

## [◆ ](#a4dd5a3457f09f46922941de990dc9933)TIMER1\_CC0\_PA5

| #define TIMER1\_CC0\_PA5   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x5) |
| --- |

## [◆ ](#a13520009a8fee0808443df4d4018e0cb)TIMER1\_CC0\_PA6

| #define TIMER1\_CC0\_PA6   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x6) |
| --- |

## [◆ ](#ade96dcb9354b034ea97b40758e27db1d)TIMER1\_CC0\_PA7

| #define TIMER1\_CC0\_PA7   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x7) |
| --- |

## [◆ ](#a783d899451987bcaf749652127c1ebb4)TIMER1\_CC0\_PA8

| #define TIMER1\_CC0\_PA8   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x8) |
| --- |

## [◆ ](#a7d8ea431d027df42da39f6ed4f0f877e)TIMER1\_CC0\_PA9

| #define TIMER1\_CC0\_PA9   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x9) |
| --- |

## [◆ ](#a0cda060bbc98a77e19ed36b4d01cfec2)TIMER1\_CC0\_PB0

| #define TIMER1\_CC0\_PB0   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x1, 0x0) |
| --- |

## [◆ ](#ac2c9847727308a1fed2e7b21c718a92c)TIMER1\_CC0\_PB1

| #define TIMER1\_CC0\_PB1   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x1, 0x1) |
| --- |

## [◆ ](#a400b3582d5c7bdbbcdd6d9f101d3bf1e)TIMER1\_CC0\_PB2

| #define TIMER1\_CC0\_PB2   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x1, 0x2) |
| --- |

## [◆ ](#a07e5e02a684ac91a1251bcfcf18a2ff5)TIMER1\_CC0\_PB3

| #define TIMER1\_CC0\_PB3   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x1, 0x3) |
| --- |

## [◆ ](#ac15f3e270a2f1d2a07eaf5e3b34869a4)TIMER1\_CC0\_PB4

| #define TIMER1\_CC0\_PB4   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x1, 0x4) |
| --- |

## [◆ ](#a2cb498db84033c2350ebe7be68ca13f0)TIMER1\_CC0\_PB5

| #define TIMER1\_CC0\_PB5   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x1, 0x5) |
| --- |

## [◆ ](#a47cdc8781bd255cf8392426ab34cb042)TIMER1\_CC0\_PC0

| #define TIMER1\_CC0\_PC0   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x0) |
| --- |

## [◆ ](#a41a0a7812419a3a757be7899f30acfde)TIMER1\_CC0\_PC1

| #define TIMER1\_CC0\_PC1   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x1) |
| --- |

## [◆ ](#a322dee774195678afc5f7066d126e4c7)TIMER1\_CC0\_PC2

| #define TIMER1\_CC0\_PC2   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x2) |
| --- |

## [◆ ](#a458b636db4779031722ec89e4c8fc0b8)TIMER1\_CC0\_PC3

| #define TIMER1\_CC0\_PC3   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x3) |
| --- |

## [◆ ](#a59f20ef361658d0cc27c9694c30d2e55)TIMER1\_CC0\_PC4

| #define TIMER1\_CC0\_PC4   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x4) |
| --- |

## [◆ ](#a510dc66c39d8a79666d1a3d9e6c0e3ad)TIMER1\_CC0\_PC5

| #define TIMER1\_CC0\_PC5   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x5) |
| --- |

## [◆ ](#adcddd8bdcd941ec6e83d060d4c3cdb9e)TIMER1\_CC0\_PC6

| #define TIMER1\_CC0\_PC6   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x6) |
| --- |

## [◆ ](#a59678105bf2c365d44d7f138804809e9)TIMER1\_CC0\_PC7

| #define TIMER1\_CC0\_PC7   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x7) |
| --- |

## [◆ ](#af37a59f6bb9aed9bd57aee73f998d173)TIMER1\_CC0\_PC8

| #define TIMER1\_CC0\_PC8   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x8) |
| --- |

## [◆ ](#a4e4890e7da8bbb307ea0d040abca0968)TIMER1\_CC0\_PC9

| #define TIMER1\_CC0\_PC9   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x9) |
| --- |

## [◆ ](#aa61ecf9a9f2f6b3ce46bc96d3e3b224c)TIMER1\_CC0\_PD0

| #define TIMER1\_CC0\_PD0   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x3, 0x0) |
| --- |

## [◆ ](#af69bd23d5eaf09cfa8e4ac6dc815c071)TIMER1\_CC0\_PD1

| #define TIMER1\_CC0\_PD1   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x3, 0x1) |
| --- |

## [◆ ](#ae35d1bbefce3501c063039f88ed558a2)TIMER1\_CC0\_PD2

| #define TIMER1\_CC0\_PD2   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x3, 0x2) |
| --- |

## [◆ ](#a27518cd582fa2f5266da488e386783d7)TIMER1\_CC0\_PD3

| #define TIMER1\_CC0\_PD3   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x3, 0x3) |
| --- |

## [◆ ](#af91f86a0f39fbb4df669d036b80f97c8)TIMER1\_CC0\_PD4

| #define TIMER1\_CC0\_PD4   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x3, 0x4) |
| --- |

## [◆ ](#a2e26b3f9da4b70504c2fd18cb17ce829)TIMER1\_CC0\_PD5

| #define TIMER1\_CC0\_PD5   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x3, 0x5) |
| --- |

## [◆ ](#ab0467e6e3dafc5340b516304672d0c35)TIMER1\_CC1\_PA0

| #define TIMER1\_CC1\_PA0   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x0) |
| --- |

## [◆ ](#ab56f3b43b16780006b73b6b67c7fc99c)TIMER1\_CC1\_PA1

| #define TIMER1\_CC1\_PA1   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x1) |
| --- |

## [◆ ](#a884b7041fab46641ac127f3526d1d6aa)TIMER1\_CC1\_PA2

| #define TIMER1\_CC1\_PA2   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x2) |
| --- |

## [◆ ](#a97b8069d8cf397b2da2cc011e946cc97)TIMER1\_CC1\_PA3

| #define TIMER1\_CC1\_PA3   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x3) |
| --- |

## [◆ ](#a01aacbb9315e69096d8c64b78a49b66e)TIMER1\_CC1\_PA4

| #define TIMER1\_CC1\_PA4   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x4) |
| --- |

## [◆ ](#a7b12d90d7a871b5843843f20b6318fd8)TIMER1\_CC1\_PA5

| #define TIMER1\_CC1\_PA5   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x5) |
| --- |

## [◆ ](#ac4909134633b306a24982fd780870ff6)TIMER1\_CC1\_PA6

| #define TIMER1\_CC1\_PA6   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x6) |
| --- |

## [◆ ](#adfa0d8586a7e98878562b2b08bafbfe2)TIMER1\_CC1\_PA7

| #define TIMER1\_CC1\_PA7   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x7) |
| --- |

## [◆ ](#a30769801f476e980ed12cd966644b77d)TIMER1\_CC1\_PA8

| #define TIMER1\_CC1\_PA8   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x8) |
| --- |

## [◆ ](#a46cd5cc0ad78d97da58da67005509efd)TIMER1\_CC1\_PA9

| #define TIMER1\_CC1\_PA9   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x9) |
| --- |

## [◆ ](#a48bff42d940d3d8a4bae06df47255dca)TIMER1\_CC1\_PB0

| #define TIMER1\_CC1\_PB0   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x1, 0x0) |
| --- |

## [◆ ](#a72b3f2ffb3e69fa3347b782450ee1bf6)TIMER1\_CC1\_PB1

| #define TIMER1\_CC1\_PB1   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x1, 0x1) |
| --- |

## [◆ ](#a4a119352b728b61375f56621909c6491)TIMER1\_CC1\_PB2

| #define TIMER1\_CC1\_PB2   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x1, 0x2) |
| --- |

## [◆ ](#a661948aeb7bf6303f6876bad5478e9e0)TIMER1\_CC1\_PB3

| #define TIMER1\_CC1\_PB3   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x1, 0x3) |
| --- |

## [◆ ](#aaef1ec6432b26aa96d8ada688182fbd7)TIMER1\_CC1\_PB4

| #define TIMER1\_CC1\_PB4   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x1, 0x4) |
| --- |

## [◆ ](#a45f54068e0137b9ce2b69f58c6dee860)TIMER1\_CC1\_PB5

| #define TIMER1\_CC1\_PB5   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x1, 0x5) |
| --- |

## [◆ ](#addaacb911a618cabc51f96bec3690174)TIMER1\_CC1\_PC0

| #define TIMER1\_CC1\_PC0   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x0) |
| --- |

## [◆ ](#ac8fab9c34e0b1dc6f168573f34d81bba)TIMER1\_CC1\_PC1

| #define TIMER1\_CC1\_PC1   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x1) |
| --- |

## [◆ ](#adc420cc552323a6db6ac08b76ada22d4)TIMER1\_CC1\_PC2

| #define TIMER1\_CC1\_PC2   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x2) |
| --- |

## [◆ ](#a52d6b873c40ba4c37eb80089b14abf59)TIMER1\_CC1\_PC3

| #define TIMER1\_CC1\_PC3   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x3) |
| --- |

## [◆ ](#abb9cd68c18a6c07dc753a10471310e8d)TIMER1\_CC1\_PC4

| #define TIMER1\_CC1\_PC4   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x4) |
| --- |

## [◆ ](#a93aa2304008369a86392b6a98592ccac)TIMER1\_CC1\_PC5

| #define TIMER1\_CC1\_PC5   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x5) |
| --- |

## [◆ ](#a311a8f743e1df0e2d257ba4aa71f91a4)TIMER1\_CC1\_PC6

| #define TIMER1\_CC1\_PC6   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x6) |
| --- |

## [◆ ](#a24c47edc39daf607df7e6b4d37caf769)TIMER1\_CC1\_PC7

| #define TIMER1\_CC1\_PC7   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x7) |
| --- |

## [◆ ](#aa8eaf731dd1ce605afde974af78b6b41)TIMER1\_CC1\_PC8

| #define TIMER1\_CC1\_PC8   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x8) |
| --- |

## [◆ ](#acc48838987530c78b16856a3d261850c)TIMER1\_CC1\_PC9

| #define TIMER1\_CC1\_PC9   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x9) |
| --- |

## [◆ ](#a1294b47b68006e1da3c1bcf3afa1735b)TIMER1\_CC1\_PD0

| #define TIMER1\_CC1\_PD0   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x3, 0x0) |
| --- |

## [◆ ](#addf0cad7ebe2b5d0dcb15ee2860aa037)TIMER1\_CC1\_PD1

| #define TIMER1\_CC1\_PD1   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x3, 0x1) |
| --- |

## [◆ ](#aff68d222f67741f6d81518e502686cab)TIMER1\_CC1\_PD2

| #define TIMER1\_CC1\_PD2   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x3, 0x2) |
| --- |

## [◆ ](#a8a7f0101160dbc45889575bb975dcad8)TIMER1\_CC1\_PD3

| #define TIMER1\_CC1\_PD3   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x3, 0x3) |
| --- |

## [◆ ](#a42265ecc8251fe6745cd225fb14cae35)TIMER1\_CC1\_PD4

| #define TIMER1\_CC1\_PD4   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x3, 0x4) |
| --- |

## [◆ ](#ac7d88abd26fe19e66437c96e26af2598)TIMER1\_CC1\_PD5

| #define TIMER1\_CC1\_PD5   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x3, 0x5) |
| --- |

## [◆ ](#a8134a1d2f64747b5fd66aa6da49db081)TIMER1\_CC2\_PA0

| #define TIMER1\_CC2\_PA0   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x0) |
| --- |

## [◆ ](#af865342309d6355e05de4a3736e73a65)TIMER1\_CC2\_PA1

| #define TIMER1\_CC2\_PA1   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x1) |
| --- |

## [◆ ](#af329d80cea63f60045ea71156c4d9d6b)TIMER1\_CC2\_PA2

| #define TIMER1\_CC2\_PA2   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x2) |
| --- |

## [◆ ](#a1eb4626f10a12c5f6b1539fe897e0df0)TIMER1\_CC2\_PA3

| #define TIMER1\_CC2\_PA3   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x3) |
| --- |

## [◆ ](#abac33f1fd8502f1356107d20958e9ebb)TIMER1\_CC2\_PA4

| #define TIMER1\_CC2\_PA4   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x4) |
| --- |

## [◆ ](#ab1ba6969141f0ba0ed17a5e3bd6ac2d7)TIMER1\_CC2\_PA5

| #define TIMER1\_CC2\_PA5   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x5) |
| --- |

## [◆ ](#a46c2801cd73d8663d493fa62300a0188)TIMER1\_CC2\_PA6

| #define TIMER1\_CC2\_PA6   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x6) |
| --- |

## [◆ ](#a879a43e390d7a577150f00cb53ebf65c)TIMER1\_CC2\_PA7

| #define TIMER1\_CC2\_PA7   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x7) |
| --- |

## [◆ ](#aaf3995fdd63448a607fdb1f654c9f75b)TIMER1\_CC2\_PA8

| #define TIMER1\_CC2\_PA8   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x8) |
| --- |

## [◆ ](#abf299bd012798984301356e20438d3e2)TIMER1\_CC2\_PA9

| #define TIMER1\_CC2\_PA9   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x9) |
| --- |

## [◆ ](#ad1ba82a4e75e024cc9f19d66f691c4a1)TIMER1\_CC2\_PB0

| #define TIMER1\_CC2\_PB0   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x1, 0x0) |
| --- |

## [◆ ](#a4da4366632a0e029856f048d0953b6b2)TIMER1\_CC2\_PB1

| #define TIMER1\_CC2\_PB1   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x1, 0x1) |
| --- |

## [◆ ](#a758d4ed1cfb60bad3e5226aa3da3a250)TIMER1\_CC2\_PB2

| #define TIMER1\_CC2\_PB2   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x1, 0x2) |
| --- |

## [◆ ](#aec809925fc33d82ccbdc64200073bffb)TIMER1\_CC2\_PB3

| #define TIMER1\_CC2\_PB3   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x1, 0x3) |
| --- |

## [◆ ](#ab320f142f9af0a3bec92d8a421b3c7cb)TIMER1\_CC2\_PB4

| #define TIMER1\_CC2\_PB4   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x1, 0x4) |
| --- |

## [◆ ](#af62217be3c7a101fd2a681b3ed38c713)TIMER1\_CC2\_PB5

| #define TIMER1\_CC2\_PB5   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x1, 0x5) |
| --- |

## [◆ ](#a9d3402f1ed1c7030fb0a1af512425ae2)TIMER1\_CC2\_PC0

| #define TIMER1\_CC2\_PC0   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x0) |
| --- |

## [◆ ](#a939a814b29112f312ba5085449fe9b8c)TIMER1\_CC2\_PC1

| #define TIMER1\_CC2\_PC1   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x1) |
| --- |

## [◆ ](#a22ffd1572810e3da8a83f7cc4ccf1386)TIMER1\_CC2\_PC2

| #define TIMER1\_CC2\_PC2   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x2) |
| --- |

## [◆ ](#afcb1d543010489ffe23a92875fafb326)TIMER1\_CC2\_PC3

| #define TIMER1\_CC2\_PC3   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x3) |
| --- |

## [◆ ](#a1a34258c1ad068a3474e0114b1e3ac37)TIMER1\_CC2\_PC4

| #define TIMER1\_CC2\_PC4   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x4) |
| --- |

## [◆ ](#a4b3b5917e7881eeb6a191c095f0df29a)TIMER1\_CC2\_PC5

| #define TIMER1\_CC2\_PC5   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x5) |
| --- |

## [◆ ](#ab66a57d9d50c0f3492a4ccd7fae0a725)TIMER1\_CC2\_PC6

| #define TIMER1\_CC2\_PC6   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x6) |
| --- |

## [◆ ](#a46f776103efbd3d5cda86c02bd1c6ee1)TIMER1\_CC2\_PC7

| #define TIMER1\_CC2\_PC7   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x7) |
| --- |

## [◆ ](#a0f8c1e2acdb2423abb4f95aa1b5fe962)TIMER1\_CC2\_PC8

| #define TIMER1\_CC2\_PC8   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x8) |
| --- |

## [◆ ](#a63eaac923797fb8b68c08eeb4dd42ce1)TIMER1\_CC2\_PC9

| #define TIMER1\_CC2\_PC9   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x9) |
| --- |

## [◆ ](#a0bb950575d698e83b4a7b055928d4b02)TIMER1\_CC2\_PD0

| #define TIMER1\_CC2\_PD0   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x3, 0x0) |
| --- |

## [◆ ](#a9f92d850417b9d521c2c2515fbeb8c52)TIMER1\_CC2\_PD1

| #define TIMER1\_CC2\_PD1   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x3, 0x1) |
| --- |

## [◆ ](#ac5f369d207dbe8da77b94ed7c2ee1e89)TIMER1\_CC2\_PD2

| #define TIMER1\_CC2\_PD2   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x3, 0x2) |
| --- |

## [◆ ](#aa1c5e07b9ff3373d65a73b3fc916c226)TIMER1\_CC2\_PD3

| #define TIMER1\_CC2\_PD3   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x3, 0x3) |
| --- |

## [◆ ](#adfa6b132aa5c4c006185ebf5170aa38d)TIMER1\_CC2\_PD4

| #define TIMER1\_CC2\_PD4   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x3, 0x4) |
| --- |

## [◆ ](#a73affe121ba3b16a8aa04f57cc2ea053)TIMER1\_CC2\_PD5

| #define TIMER1\_CC2\_PD5   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x3, 0x5) |
| --- |

## [◆ ](#a76552704f3b8c28588c6073b170a6bbb)TIMER1\_CDTI0\_PA0

| #define TIMER1\_CDTI0\_PA0   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x0) |
| --- |

## [◆ ](#a06ea543c9f00b58b7eb4e162a7c3f427)TIMER1\_CDTI0\_PA1

| #define TIMER1\_CDTI0\_PA1   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x1) |
| --- |

## [◆ ](#ace53011f7d140ea6892946ac0d246006)TIMER1\_CDTI0\_PA2

| #define TIMER1\_CDTI0\_PA2   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x2) |
| --- |

## [◆ ](#a9b740fb70a98203b6a736fb3e3af97d1)TIMER1\_CDTI0\_PA3

| #define TIMER1\_CDTI0\_PA3   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x3) |
| --- |

## [◆ ](#adf79eddb39e5a3a28e98da92323cead4)TIMER1\_CDTI0\_PA4

| #define TIMER1\_CDTI0\_PA4   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x4) |
| --- |

## [◆ ](#a1c025b319acd53ac15e023a964b684d4)TIMER1\_CDTI0\_PA5

| #define TIMER1\_CDTI0\_PA5   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x5) |
| --- |

## [◆ ](#afed1694b73910fdb222e7ac95c7700a6)TIMER1\_CDTI0\_PA6

| #define TIMER1\_CDTI0\_PA6   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x6) |
| --- |

## [◆ ](#a16baa7d86f92039e49b2419f2c6920fe)TIMER1\_CDTI0\_PA7

| #define TIMER1\_CDTI0\_PA7   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x7) |
| --- |

## [◆ ](#a52ac2c6692f7362bef618cb7d5f0e47c)TIMER1\_CDTI0\_PA8

| #define TIMER1\_CDTI0\_PA8   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x8) |
| --- |

## [◆ ](#a5bac5b45e58c97eb8575bfa35358ec0e)TIMER1\_CDTI0\_PA9

| #define TIMER1\_CDTI0\_PA9   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x9) |
| --- |

## [◆ ](#a3f2880efd1d31b43e1fbbd840a535330)TIMER1\_CDTI0\_PB0

| #define TIMER1\_CDTI0\_PB0   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x1, 0x0) |
| --- |

## [◆ ](#a3f243ab2322faa708a8c0531a3fb15fe)TIMER1\_CDTI0\_PB1

| #define TIMER1\_CDTI0\_PB1   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x1, 0x1) |
| --- |

## [◆ ](#adf3c676ce682f3c923108b655457d517)TIMER1\_CDTI0\_PB2

| #define TIMER1\_CDTI0\_PB2   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x1, 0x2) |
| --- |

## [◆ ](#af950bfe52b44c7e24ffe22ef76719f82)TIMER1\_CDTI0\_PB3

| #define TIMER1\_CDTI0\_PB3   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x1, 0x3) |
| --- |

## [◆ ](#a9651bb0408184ebddd6b56bc0b84294c)TIMER1\_CDTI0\_PB4

| #define TIMER1\_CDTI0\_PB4   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x1, 0x4) |
| --- |

## [◆ ](#ac08854c7fbc83a84934c4dc3dfcb348e)TIMER1\_CDTI0\_PB5

| #define TIMER1\_CDTI0\_PB5   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x1, 0x5) |
| --- |

## [◆ ](#a7da42fba55aa964b5af1f0e996e10dfd)TIMER1\_CDTI0\_PC0

| #define TIMER1\_CDTI0\_PC0   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x0) |
| --- |

## [◆ ](#a90f5a73378a61a3144cb3be626acf0c3)TIMER1\_CDTI0\_PC1

| #define TIMER1\_CDTI0\_PC1   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x1) |
| --- |

## [◆ ](#ac7083129b89cd513468ea9a936cd2a60)TIMER1\_CDTI0\_PC2

| #define TIMER1\_CDTI0\_PC2   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x2) |
| --- |

## [◆ ](#ac480c190767e6bf9e64e2581617388d7)TIMER1\_CDTI0\_PC3

| #define TIMER1\_CDTI0\_PC3   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x3) |
| --- |

## [◆ ](#a80619df142e179bb585569b51f906b85)TIMER1\_CDTI0\_PC4

| #define TIMER1\_CDTI0\_PC4   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x4) |
| --- |

## [◆ ](#af24c550e1fcf0b93ca210c59884dd895)TIMER1\_CDTI0\_PC5

| #define TIMER1\_CDTI0\_PC5   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x5) |
| --- |

## [◆ ](#a6006a6fa136154c9f64c65a851a50b2a)TIMER1\_CDTI0\_PC6

| #define TIMER1\_CDTI0\_PC6   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x6) |
| --- |

## [◆ ](#af1951b25ec7b89a7dccceb94847fc37f)TIMER1\_CDTI0\_PC7

| #define TIMER1\_CDTI0\_PC7   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x7) |
| --- |

## [◆ ](#afe8f874a39e8c957bbc6491ff5b4309e)TIMER1\_CDTI0\_PC8

| #define TIMER1\_CDTI0\_PC8   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x8) |
| --- |

## [◆ ](#ab9e56e2b63c3ae33438060fe68376747)TIMER1\_CDTI0\_PC9

| #define TIMER1\_CDTI0\_PC9   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x9) |
| --- |

## [◆ ](#aeafc7272c0cf6bed9dcb09fe8802bd1f)TIMER1\_CDTI0\_PD0

| #define TIMER1\_CDTI0\_PD0   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x3, 0x0) |
| --- |

## [◆ ](#a15c83b7661113ab00fc830c832a63ad5)TIMER1\_CDTI0\_PD1

| #define TIMER1\_CDTI0\_PD1   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x3, 0x1) |
| --- |

## [◆ ](#af02751809240508c57a914bf47bc929b)TIMER1\_CDTI0\_PD2

| #define TIMER1\_CDTI0\_PD2   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x3, 0x2) |
| --- |

## [◆ ](#a36ad9aa1e2ca755919bd18f1461fd9fd)TIMER1\_CDTI0\_PD3

| #define TIMER1\_CDTI0\_PD3   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x3, 0x3) |
| --- |

## [◆ ](#a694a3359d922f9aeca292c10db75cae7)TIMER1\_CDTI0\_PD4

| #define TIMER1\_CDTI0\_PD4   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x3, 0x4) |
| --- |

## [◆ ](#ad142a654bba95812c67a92c812914604)TIMER1\_CDTI0\_PD5

| #define TIMER1\_CDTI0\_PD5   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x3, 0x5) |
| --- |

## [◆ ](#a0c90975d990014c0a70d8fe8a01bed61)TIMER1\_CDTI1\_PA0

| #define TIMER1\_CDTI1\_PA0   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x0) |
| --- |

## [◆ ](#a063202bd4d4d5c420613ccbdf41c08ac)TIMER1\_CDTI1\_PA1

| #define TIMER1\_CDTI1\_PA1   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x1) |
| --- |

## [◆ ](#a03c893bbd5151dc4bf1f08a8c197982d)TIMER1\_CDTI1\_PA2

| #define TIMER1\_CDTI1\_PA2   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x2) |
| --- |

## [◆ ](#a13fea81e86713c5839372ae17ffa5b2a)TIMER1\_CDTI1\_PA3

| #define TIMER1\_CDTI1\_PA3   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x3) |
| --- |

## [◆ ](#a3b63381e36f0f67eecdb0e613e082acd)TIMER1\_CDTI1\_PA4

| #define TIMER1\_CDTI1\_PA4   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x4) |
| --- |

## [◆ ](#ae29404facb1a5712a8d3654c32abac03)TIMER1\_CDTI1\_PA5

| #define TIMER1\_CDTI1\_PA5   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x5) |
| --- |

## [◆ ](#a041c492c18debf15659b54a4d1acda45)TIMER1\_CDTI1\_PA6

| #define TIMER1\_CDTI1\_PA6   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x6) |
| --- |

## [◆ ](#ad2a111a49ac82b431c221b9b38a7eac2)TIMER1\_CDTI1\_PA7

| #define TIMER1\_CDTI1\_PA7   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x7) |
| --- |

## [◆ ](#a61f6fe07be3fdc75f7a137652ff6180b)TIMER1\_CDTI1\_PA8

| #define TIMER1\_CDTI1\_PA8   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x8) |
| --- |

## [◆ ](#afd14a9f0b3f68baf645fdbedb8b9a636)TIMER1\_CDTI1\_PA9

| #define TIMER1\_CDTI1\_PA9   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x9) |
| --- |

## [◆ ](#afe513e7286648f7e0dfdcd5831a158cb)TIMER1\_CDTI1\_PB0

| #define TIMER1\_CDTI1\_PB0   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x1, 0x0) |
| --- |

## [◆ ](#a231c7d9bddd4e56226c51a3ca0516290)TIMER1\_CDTI1\_PB1

| #define TIMER1\_CDTI1\_PB1   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x1, 0x1) |
| --- |

## [◆ ](#a5670dfed8891e8a39a4747b6a7536fa4)TIMER1\_CDTI1\_PB2

| #define TIMER1\_CDTI1\_PB2   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x1, 0x2) |
| --- |

## [◆ ](#aef5f7b0ad2e48af91779080e32da44b4)TIMER1\_CDTI1\_PB3

| #define TIMER1\_CDTI1\_PB3   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x1, 0x3) |
| --- |

## [◆ ](#aef8297dce3f2193d4367df88ab5bf20d)TIMER1\_CDTI1\_PB4

| #define TIMER1\_CDTI1\_PB4   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x1, 0x4) |
| --- |

## [◆ ](#a8b771498d29d4f8f733a421686289f9f)TIMER1\_CDTI1\_PB5

| #define TIMER1\_CDTI1\_PB5   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x1, 0x5) |
| --- |

## [◆ ](#a26cc959057976169dd4e4a4330bb34ff)TIMER1\_CDTI1\_PC0

| #define TIMER1\_CDTI1\_PC0   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x0) |
| --- |

## [◆ ](#a5be334fd1d01d68ebc4fbf77394adc03)TIMER1\_CDTI1\_PC1

| #define TIMER1\_CDTI1\_PC1   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x1) |
| --- |

## [◆ ](#a153d9a304ad237e9f99bf2fd97cb5ca3)TIMER1\_CDTI1\_PC2

| #define TIMER1\_CDTI1\_PC2   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x2) |
| --- |

## [◆ ](#ae1d146285574814c26941837ae32cf33)TIMER1\_CDTI1\_PC3

| #define TIMER1\_CDTI1\_PC3   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x3) |
| --- |

## [◆ ](#aadc34ad6a076211bfe55a1cecba057ed)TIMER1\_CDTI1\_PC4

| #define TIMER1\_CDTI1\_PC4   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x4) |
| --- |

## [◆ ](#a89667e375454960fd56fa87fd46a1cf0)TIMER1\_CDTI1\_PC5

| #define TIMER1\_CDTI1\_PC5   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x5) |
| --- |

## [◆ ](#ad60737f6dd9fe3c6f3d5039b3da8ffa5)TIMER1\_CDTI1\_PC6

| #define TIMER1\_CDTI1\_PC6   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x6) |
| --- |

## [◆ ](#ac285ce787120af33a48a91397f7e5d59)TIMER1\_CDTI1\_PC7

| #define TIMER1\_CDTI1\_PC7   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x7) |
| --- |

## [◆ ](#a31be9bbfc736c4f10dba501580adff7c)TIMER1\_CDTI1\_PC8

| #define TIMER1\_CDTI1\_PC8   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x8) |
| --- |

## [◆ ](#abdfe1aab871eeb9c4c701f6bc8a14409)TIMER1\_CDTI1\_PC9

| #define TIMER1\_CDTI1\_PC9   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x9) |
| --- |

## [◆ ](#a9a83a5c25369e4dc286c219f9be05a08)TIMER1\_CDTI1\_PD0

| #define TIMER1\_CDTI1\_PD0   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x3, 0x0) |
| --- |

## [◆ ](#ae2d334d95e5a2f65c92562727a87520b)TIMER1\_CDTI1\_PD1

| #define TIMER1\_CDTI1\_PD1   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x3, 0x1) |
| --- |

## [◆ ](#af1a5a15c236edb1c77acce4cb8d8b894)TIMER1\_CDTI1\_PD2

| #define TIMER1\_CDTI1\_PD2   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x3, 0x2) |
| --- |

## [◆ ](#a8b00bb8a1bbb8cc97e1e1997cd5ed10b)TIMER1\_CDTI1\_PD3

| #define TIMER1\_CDTI1\_PD3   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x3, 0x3) |
| --- |

## [◆ ](#a7db403c434a33b41eefe0278890da8ca)TIMER1\_CDTI1\_PD4

| #define TIMER1\_CDTI1\_PD4   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x3, 0x4) |
| --- |

## [◆ ](#a9c8c263c15cce651e686d9f5de758be9)TIMER1\_CDTI1\_PD5

| #define TIMER1\_CDTI1\_PD5   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x3, 0x5) |
| --- |

## [◆ ](#ac959ddf75f8afe8179b53148e90a0cd3)TIMER1\_CDTI2\_PA0

| #define TIMER1\_CDTI2\_PA0   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x0) |
| --- |

## [◆ ](#a03028d392b456dbce8ce5c7325f52b87)TIMER1\_CDTI2\_PA1

| #define TIMER1\_CDTI2\_PA1   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x1) |
| --- |

## [◆ ](#a3282e1d97d899e3010b59e952aa12429)TIMER1\_CDTI2\_PA2

| #define TIMER1\_CDTI2\_PA2   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x2) |
| --- |

## [◆ ](#a249a669752eb8cfca1a9dee28e0fa5b9)TIMER1\_CDTI2\_PA3

| #define TIMER1\_CDTI2\_PA3   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x3) |
| --- |

## [◆ ](#acab3d281ca3eb0fc97c1c296beacb302)TIMER1\_CDTI2\_PA4

| #define TIMER1\_CDTI2\_PA4   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x4) |
| --- |

## [◆ ](#a1b4f4b4f2f84c99855ddfbdd829a0814)TIMER1\_CDTI2\_PA5

| #define TIMER1\_CDTI2\_PA5   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x5) |
| --- |

## [◆ ](#a4008736ae0d99019066eb6435864a043)TIMER1\_CDTI2\_PA6

| #define TIMER1\_CDTI2\_PA6   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x6) |
| --- |

## [◆ ](#ae07b3d64a4947e03736ac08ac816940f)TIMER1\_CDTI2\_PA7

| #define TIMER1\_CDTI2\_PA7   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x7) |
| --- |

## [◆ ](#a52cfa50fafa8bb77eb3d1a5b9e6c1c35)TIMER1\_CDTI2\_PA8

| #define TIMER1\_CDTI2\_PA8   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x8) |
| --- |

## [◆ ](#a4b78d1149e4b0ac25deefdf83b1d5f33)TIMER1\_CDTI2\_PA9

| #define TIMER1\_CDTI2\_PA9   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x9) |
| --- |

## [◆ ](#a4ff755a9d12285c868a4dc0e5d9de281)TIMER1\_CDTI2\_PB0

| #define TIMER1\_CDTI2\_PB0   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x1, 0x0) |
| --- |

## [◆ ](#a94cb965aa4d6a7fb7a31acbd363f54ee)TIMER1\_CDTI2\_PB1

| #define TIMER1\_CDTI2\_PB1   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x1, 0x1) |
| --- |

## [◆ ](#a2b30a5c071a113e0c7693b1723aa0534)TIMER1\_CDTI2\_PB2

| #define TIMER1\_CDTI2\_PB2   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x1, 0x2) |
| --- |

## [◆ ](#ab41614ba724866ec0e55ae0837b4dc46)TIMER1\_CDTI2\_PB3

| #define TIMER1\_CDTI2\_PB3   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x1, 0x3) |
| --- |

## [◆ ](#a1388e138cdc0a50b805b4188aed036a0)TIMER1\_CDTI2\_PB4

| #define TIMER1\_CDTI2\_PB4   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x1, 0x4) |
| --- |

## [◆ ](#aa42127e04b4c560efd4ea02ca24f7cb6)TIMER1\_CDTI2\_PB5

| #define TIMER1\_CDTI2\_PB5   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x1, 0x5) |
| --- |

## [◆ ](#ab37f717d7232493a31424e87d242c2a8)TIMER1\_CDTI2\_PC0

| #define TIMER1\_CDTI2\_PC0   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x0) |
| --- |

## [◆ ](#a6a306946717970eb62df4307de771fef)TIMER1\_CDTI2\_PC1

| #define TIMER1\_CDTI2\_PC1   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x1) |
| --- |

## [◆ ](#a248af2da57a57600d4a144c71f860006)TIMER1\_CDTI2\_PC2

| #define TIMER1\_CDTI2\_PC2   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x2) |
| --- |

## [◆ ](#ae1c48f4b069d6c7e410511b1e95a7def)TIMER1\_CDTI2\_PC3

| #define TIMER1\_CDTI2\_PC3   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x3) |
| --- |

## [◆ ](#af91af878bbab4422378cf31a711055ff)TIMER1\_CDTI2\_PC4

| #define TIMER1\_CDTI2\_PC4   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x4) |
| --- |

## [◆ ](#ac16216ae2977f9696075b3a6d8c64aa0)TIMER1\_CDTI2\_PC5

| #define TIMER1\_CDTI2\_PC5   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x5) |
| --- |

## [◆ ](#aa59451e0e343327c7c1775367c4d9194)TIMER1\_CDTI2\_PC6

| #define TIMER1\_CDTI2\_PC6   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x6) |
| --- |

## [◆ ](#a6303e70615390644193cea172c375b4a)TIMER1\_CDTI2\_PC7

| #define TIMER1\_CDTI2\_PC7   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x7) |
| --- |

## [◆ ](#ad347901cc3f14d83aba6ff02c5018a24)TIMER1\_CDTI2\_PC8

| #define TIMER1\_CDTI2\_PC8   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x8) |
| --- |

## [◆ ](#a508e041f8ca4d6b4c22609f78c867615)TIMER1\_CDTI2\_PC9

| #define TIMER1\_CDTI2\_PC9   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x9) |
| --- |

## [◆ ](#ae362330bff63d204299a6a33f4c4f191)TIMER1\_CDTI2\_PD0

| #define TIMER1\_CDTI2\_PD0   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x3, 0x0) |
| --- |

## [◆ ](#a6559a7e28febb9e31fca6847e11cdb1a)TIMER1\_CDTI2\_PD1

| #define TIMER1\_CDTI2\_PD1   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x3, 0x1) |
| --- |

## [◆ ](#a8a53201b17d025911ca41f86e3d13a66)TIMER1\_CDTI2\_PD2

| #define TIMER1\_CDTI2\_PD2   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x3, 0x2) |
| --- |

## [◆ ](#a254d9132271304cd62f61184a40471d6)TIMER1\_CDTI2\_PD3

| #define TIMER1\_CDTI2\_PD3   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x3, 0x3) |
| --- |

## [◆ ](#acf43810574237c108aba907ba113d6ba)TIMER1\_CDTI2\_PD4

| #define TIMER1\_CDTI2\_PD4   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x3, 0x4) |
| --- |

## [◆ ](#a325a0c29bdccc1bb5c9f5438b1c967e7)TIMER1\_CDTI2\_PD5

| #define TIMER1\_CDTI2\_PD5   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x3, 0x5) |
| --- |

## [◆ ](#a67e6f27f89e7e121cce88e0186ab5010)TIMER2\_CC0\_PA0

| #define TIMER2\_CC0\_PA0   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x0) |
| --- |

## [◆ ](#a545f09892c0762da7a55cdc8d16e8e6f)TIMER2\_CC0\_PA1

| #define TIMER2\_CC0\_PA1   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x1) |
| --- |

## [◆ ](#aee905018c0d9aa48c14e415474c03f62)TIMER2\_CC0\_PA2

| #define TIMER2\_CC0\_PA2   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x2) |
| --- |

## [◆ ](#ad7327f8fa42b7aa1875d2b57769330eb)TIMER2\_CC0\_PA3

| #define TIMER2\_CC0\_PA3   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x3) |
| --- |

## [◆ ](#acab7bd67fc01c7fa8b3c40d75f725a0a)TIMER2\_CC0\_PA4

| #define TIMER2\_CC0\_PA4   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x4) |
| --- |

## [◆ ](#ac846d48997b6bdbb2b7665a62a6505e3)TIMER2\_CC0\_PA5

| #define TIMER2\_CC0\_PA5   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x5) |
| --- |

## [◆ ](#a987c36e9761389522505ac50952ed04a)TIMER2\_CC0\_PA6

| #define TIMER2\_CC0\_PA6   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x6) |
| --- |

## [◆ ](#ae2170865d853ff19f2822feef4adb237)TIMER2\_CC0\_PA7

| #define TIMER2\_CC0\_PA7   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x7) |
| --- |

## [◆ ](#a76ee3427d6e4a4a9bba02acb045fc34c)TIMER2\_CC0\_PA8

| #define TIMER2\_CC0\_PA8   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x8) |
| --- |

## [◆ ](#a5e2a34f5dccec5291ae1424aba054ca6)TIMER2\_CC0\_PA9

| #define TIMER2\_CC0\_PA9   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x9) |
| --- |

## [◆ ](#a2a9776f698e90b570e177a6a0059b15b)TIMER2\_CC0\_PB0

| #define TIMER2\_CC0\_PB0   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x1, 0x0) |
| --- |

## [◆ ](#a55d9652dbf9c89d894162860c56459dd)TIMER2\_CC0\_PB1

| #define TIMER2\_CC0\_PB1   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x1, 0x1) |
| --- |

## [◆ ](#a0c9bb962ddacf136ff3625459e3d7671)TIMER2\_CC0\_PB2

| #define TIMER2\_CC0\_PB2   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x1, 0x2) |
| --- |

## [◆ ](#a738b1a7965ce7945a6123c0b97606ac5)TIMER2\_CC0\_PB3

| #define TIMER2\_CC0\_PB3   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x1, 0x3) |
| --- |

## [◆ ](#aa0dcc265ed171092f14a0e54e7be712d)TIMER2\_CC0\_PB4

| #define TIMER2\_CC0\_PB4   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x1, 0x4) |
| --- |

## [◆ ](#a965309ec5b9aa35bcf030f28d2930dcd)TIMER2\_CC0\_PB5

| #define TIMER2\_CC0\_PB5   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x1, 0x5) |
| --- |

## [◆ ](#a1164a4f1a0cfbf0cb157eeb7be84bd28)TIMER2\_CC1\_PA0

| #define TIMER2\_CC1\_PA0   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x0) |
| --- |

## [◆ ](#a1bca4d4f43da2d564d68622dcb0e5d9e)TIMER2\_CC1\_PA1

| #define TIMER2\_CC1\_PA1   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x1) |
| --- |

## [◆ ](#adec2ad20e72e0b8fd02b6476685f5155)TIMER2\_CC1\_PA2

| #define TIMER2\_CC1\_PA2   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x2) |
| --- |

## [◆ ](#a8a42dfc04580c2dba2b961509d03ff43)TIMER2\_CC1\_PA3

| #define TIMER2\_CC1\_PA3   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x3) |
| --- |

## [◆ ](#a89a293610575367134548bc2ccd0c47e)TIMER2\_CC1\_PA4

| #define TIMER2\_CC1\_PA4   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x4) |
| --- |

## [◆ ](#acdbcff934f4bac5a2b0f03a33e44138b)TIMER2\_CC1\_PA5

| #define TIMER2\_CC1\_PA5   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x5) |
| --- |

## [◆ ](#a4c420a0fc98b352544416bbfa8216ae6)TIMER2\_CC1\_PA6

| #define TIMER2\_CC1\_PA6   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x6) |
| --- |

## [◆ ](#a458c07160c2f3c3b6f12444c8f498167)TIMER2\_CC1\_PA7

| #define TIMER2\_CC1\_PA7   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x7) |
| --- |

## [◆ ](#ae91c030e51c7e07691257667d671d56e)TIMER2\_CC1\_PA8

| #define TIMER2\_CC1\_PA8   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x8) |
| --- |

## [◆ ](#a8409e21ef524a3cb805443759a3df758)TIMER2\_CC1\_PA9

| #define TIMER2\_CC1\_PA9   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x9) |
| --- |

## [◆ ](#ac7397d7ebe41f5c2b732bece2b63f793)TIMER2\_CC1\_PB0

| #define TIMER2\_CC1\_PB0   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x1, 0x0) |
| --- |

## [◆ ](#a0d597a9083a41c950f29bbbf7e148ef7)TIMER2\_CC1\_PB1

| #define TIMER2\_CC1\_PB1   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x1, 0x1) |
| --- |

## [◆ ](#a45aeb569507fbd649e081575c136eb4a)TIMER2\_CC1\_PB2

| #define TIMER2\_CC1\_PB2   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x1, 0x2) |
| --- |

## [◆ ](#afb1a90f5d59b6ce2df0a231b4c6cd75c)TIMER2\_CC1\_PB3

| #define TIMER2\_CC1\_PB3   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x1, 0x3) |
| --- |

## [◆ ](#a833c1470f9dec67fe7e0d7b57c0c1dee)TIMER2\_CC1\_PB4

| #define TIMER2\_CC1\_PB4   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x1, 0x4) |
| --- |

## [◆ ](#a3166b5021d74a953023c75c2707e5a47)TIMER2\_CC1\_PB5

| #define TIMER2\_CC1\_PB5   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x1, 0x5) |
| --- |

## [◆ ](#a2d62e330c22411c86274caefb099cf19)TIMER2\_CC2\_PA0

| #define TIMER2\_CC2\_PA0   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x0) |
| --- |

## [◆ ](#aab60fb88a625e320ce64ea10133311df)TIMER2\_CC2\_PA1

| #define TIMER2\_CC2\_PA1   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x1) |
| --- |

## [◆ ](#a4bf049cdc3017e816165effd4cff7d35)TIMER2\_CC2\_PA2

| #define TIMER2\_CC2\_PA2   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x2) |
| --- |

## [◆ ](#a00eafe61a794b07af52d028ab4dd1adf)TIMER2\_CC2\_PA3

| #define TIMER2\_CC2\_PA3   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x3) |
| --- |

## [◆ ](#aedbc75bcf6c733bcd3deadb3c8ce0f21)TIMER2\_CC2\_PA4

| #define TIMER2\_CC2\_PA4   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x4) |
| --- |

## [◆ ](#a490ca0f07b93c2cd68351c6afb4a9819)TIMER2\_CC2\_PA5

| #define TIMER2\_CC2\_PA5   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x5) |
| --- |

## [◆ ](#abd8592d55f4ff8bd546adb9efc7ee922)TIMER2\_CC2\_PA6

| #define TIMER2\_CC2\_PA6   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x6) |
| --- |

## [◆ ](#a9d34e2111c7b45d5d7b36d0df3c80629)TIMER2\_CC2\_PA7

| #define TIMER2\_CC2\_PA7   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x7) |
| --- |

## [◆ ](#af969ac3be731d012befc6f7d2aef5fbe)TIMER2\_CC2\_PA8

| #define TIMER2\_CC2\_PA8   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x8) |
| --- |

## [◆ ](#aab5539df46520dbb522526753d2cd567)TIMER2\_CC2\_PA9

| #define TIMER2\_CC2\_PA9   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x9) |
| --- |

## [◆ ](#a59ed3f774f4d21a9f1fbc9d71cb57fe4)TIMER2\_CC2\_PB0

| #define TIMER2\_CC2\_PB0   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x1, 0x0) |
| --- |

## [◆ ](#abaf434275a10efbc0b32f7d859d51912)TIMER2\_CC2\_PB1

| #define TIMER2\_CC2\_PB1   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x1, 0x1) |
| --- |

## [◆ ](#ac4c83f10ee7ec2978b3612b8fdd8c6cb)TIMER2\_CC2\_PB2

| #define TIMER2\_CC2\_PB2   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x1, 0x2) |
| --- |

## [◆ ](#acc8b352f48014e5fd8a14f5d1d79d681)TIMER2\_CC2\_PB3

| #define TIMER2\_CC2\_PB3   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x1, 0x3) |
| --- |

## [◆ ](#a9add0713ccac926ac0a079bd7cd69aae)TIMER2\_CC2\_PB4

| #define TIMER2\_CC2\_PB4   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x1, 0x4) |
| --- |

## [◆ ](#a803f2b5d5157805d478efa8e93310443)TIMER2\_CC2\_PB5

| #define TIMER2\_CC2\_PB5   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x1, 0x5) |
| --- |

## [◆ ](#a6cb932cba841a0987d78da39e11cadba)TIMER2\_CDTI0\_PA0

| #define TIMER2\_CDTI0\_PA0   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x0) |
| --- |

## [◆ ](#a9cde27e9bdb4e6157afe1149d35e8dbd)TIMER2\_CDTI0\_PA1

| #define TIMER2\_CDTI0\_PA1   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x1) |
| --- |

## [◆ ](#a5906c55b37b73111550ea2eb75681575)TIMER2\_CDTI0\_PA2

| #define TIMER2\_CDTI0\_PA2   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x2) |
| --- |

## [◆ ](#afa16ff7cf30f5cc4d2fe967263b9b2b0)TIMER2\_CDTI0\_PA3

| #define TIMER2\_CDTI0\_PA3   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x3) |
| --- |

## [◆ ](#ac0d736392f3d098ec5789189dc37036b)TIMER2\_CDTI0\_PA4

| #define TIMER2\_CDTI0\_PA4   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x4) |
| --- |

## [◆ ](#aa8c2a2712578b133cdbd8d07f1f37c24)TIMER2\_CDTI0\_PA5

| #define TIMER2\_CDTI0\_PA5   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x5) |
| --- |

## [◆ ](#a801b4531b9bb956d267c53f15b47a872)TIMER2\_CDTI0\_PA6

| #define TIMER2\_CDTI0\_PA6   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x6) |
| --- |

## [◆ ](#a36d14f2c4b029f787c6d474e41dd3dd8)TIMER2\_CDTI0\_PA7

| #define TIMER2\_CDTI0\_PA7   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x7) |
| --- |

## [◆ ](#ae1f424e362c402dcd38f0aaea7d059ac)TIMER2\_CDTI0\_PA8

| #define TIMER2\_CDTI0\_PA8   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x8) |
| --- |

## [◆ ](#aa9e2852c734a0f92a7ecc1a95b60d5e7)TIMER2\_CDTI0\_PA9

| #define TIMER2\_CDTI0\_PA9   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x9) |
| --- |

## [◆ ](#ad1c011c5437d75b74c56ebbb00e9dd65)TIMER2\_CDTI0\_PB0

| #define TIMER2\_CDTI0\_PB0   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x1, 0x0) |
| --- |

## [◆ ](#afedfcd3a53de2251bb61ccfed3af4a5f)TIMER2\_CDTI0\_PB1

| #define TIMER2\_CDTI0\_PB1   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x1, 0x1) |
| --- |

## [◆ ](#aab462dbb772296080bcfa7c0c9cb80fa)TIMER2\_CDTI0\_PB2

| #define TIMER2\_CDTI0\_PB2   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x1, 0x2) |
| --- |

## [◆ ](#adc08d2d352d4b14d201a11b6df7a64c9)TIMER2\_CDTI0\_PB3

| #define TIMER2\_CDTI0\_PB3   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x1, 0x3) |
| --- |

## [◆ ](#af02e9de67604ab16812a2b464cde99ae)TIMER2\_CDTI0\_PB4

| #define TIMER2\_CDTI0\_PB4   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x1, 0x4) |
| --- |

## [◆ ](#ac354ef57259735403dc4f781888e948d)TIMER2\_CDTI0\_PB5

| #define TIMER2\_CDTI0\_PB5   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x1, 0x5) |
| --- |

## [◆ ](#ae901259c744451af8a8ded388dfe9f5d)TIMER2\_CDTI1\_PA0

| #define TIMER2\_CDTI1\_PA0   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x0) |
| --- |

## [◆ ](#a9e6e2fc9804d67ec073460ddf34fdd02)TIMER2\_CDTI1\_PA1

| #define TIMER2\_CDTI1\_PA1   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x1) |
| --- |

## [◆ ](#a7ac971aa8206899b4623057140243357)TIMER2\_CDTI1\_PA2

| #define TIMER2\_CDTI1\_PA2   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x2) |
| --- |

## [◆ ](#af174d0f8740b9d33ae66dba3e34b6031)TIMER2\_CDTI1\_PA3

| #define TIMER2\_CDTI1\_PA3   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x3) |
| --- |

## [◆ ](#afbda2d057823f529835a894ff9ad8629)TIMER2\_CDTI1\_PA4

| #define TIMER2\_CDTI1\_PA4   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x4) |
| --- |

## [◆ ](#a5b02e4c0ceb352d283a0e99cb05fddab)TIMER2\_CDTI1\_PA5

| #define TIMER2\_CDTI1\_PA5   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x5) |
| --- |

## [◆ ](#a5a930f094a10216d1b43a4eab6a359b7)TIMER2\_CDTI1\_PA6

| #define TIMER2\_CDTI1\_PA6   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x6) |
| --- |

## [◆ ](#add09acbb0fe8df1b64222f324163396b)TIMER2\_CDTI1\_PA7

| #define TIMER2\_CDTI1\_PA7   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x7) |
| --- |

## [◆ ](#a7f376eb3ffe07f95fa562c13244f3dd4)TIMER2\_CDTI1\_PA8

| #define TIMER2\_CDTI1\_PA8   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x8) |
| --- |

## [◆ ](#afcad730fd054bba3e3ee54b66983fb0e)TIMER2\_CDTI1\_PA9

| #define TIMER2\_CDTI1\_PA9   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x9) |
| --- |

## [◆ ](#a542b9626fdc82bd0444ecd2518031406)TIMER2\_CDTI1\_PB0

| #define TIMER2\_CDTI1\_PB0   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x1, 0x0) |
| --- |

## [◆ ](#a3600b995f1e40289444081210ad8430f)TIMER2\_CDTI1\_PB1

| #define TIMER2\_CDTI1\_PB1   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x1, 0x1) |
| --- |

## [◆ ](#ad87b20ae7e6e5876d5988a95be42720f)TIMER2\_CDTI1\_PB2

| #define TIMER2\_CDTI1\_PB2   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x1, 0x2) |
| --- |

## [◆ ](#a3174683951113d5d144bb0338014cbfd)TIMER2\_CDTI1\_PB3

| #define TIMER2\_CDTI1\_PB3   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x1, 0x3) |
| --- |

## [◆ ](#aaa89be3aa5b5b9cdbd4a693c5c9ffabe)TIMER2\_CDTI1\_PB4

| #define TIMER2\_CDTI1\_PB4   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x1, 0x4) |
| --- |

## [◆ ](#aba96c577d13b3234b8469a40120d9754)TIMER2\_CDTI1\_PB5

| #define TIMER2\_CDTI1\_PB5   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x1, 0x5) |
| --- |

## [◆ ](#a70028435f4fa81dc8504d6fb5562480c)TIMER2\_CDTI2\_PA0

| #define TIMER2\_CDTI2\_PA0   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x0) |
| --- |

## [◆ ](#af71768a49adaf60e74a77ff629b3ebd2)TIMER2\_CDTI2\_PA1

| #define TIMER2\_CDTI2\_PA1   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x1) |
| --- |

## [◆ ](#a56efa7077f3f025446f2c1937b833093)TIMER2\_CDTI2\_PA2

| #define TIMER2\_CDTI2\_PA2   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x2) |
| --- |

## [◆ ](#a288823b89fcc8c89d73c6865f8f69cc8)TIMER2\_CDTI2\_PA3

| #define TIMER2\_CDTI2\_PA3   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x3) |
| --- |

## [◆ ](#ab34c2728b9bc0054c854960165408494)TIMER2\_CDTI2\_PA4

| #define TIMER2\_CDTI2\_PA4   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x4) |
| --- |

## [◆ ](#af55eb46eaa2657c75df8b7c92119588c)TIMER2\_CDTI2\_PA5

| #define TIMER2\_CDTI2\_PA5   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x5) |
| --- |

## [◆ ](#a98e606b3b4ba2b0118736951d32b48ad)TIMER2\_CDTI2\_PA6

| #define TIMER2\_CDTI2\_PA6   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x6) |
| --- |

## [◆ ](#a1d1543914dacf30872f9d0bdeead7ce7)TIMER2\_CDTI2\_PA7

| #define TIMER2\_CDTI2\_PA7   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x7) |
| --- |

## [◆ ](#a8846303a4f61f979c77da532908f7f7b)TIMER2\_CDTI2\_PA8

| #define TIMER2\_CDTI2\_PA8   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x8) |
| --- |

## [◆ ](#a00c86bb7e91f80f28e82b9a90c18ebb2)TIMER2\_CDTI2\_PA9

| #define TIMER2\_CDTI2\_PA9   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x9) |
| --- |

## [◆ ](#abd0220954a47f2fcf85f72971f2e7f8c)TIMER2\_CDTI2\_PB0

| #define TIMER2\_CDTI2\_PB0   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x1, 0x0) |
| --- |

## [◆ ](#ad82071aa4bb174e39da29be3a98e06f4)TIMER2\_CDTI2\_PB1

| #define TIMER2\_CDTI2\_PB1   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x1, 0x1) |
| --- |

## [◆ ](#a761808819fa59b8246ead762ee6dc88f)TIMER2\_CDTI2\_PB2

| #define TIMER2\_CDTI2\_PB2   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x1, 0x2) |
| --- |

## [◆ ](#af996eab47687d2ef9206856fe10266f8)TIMER2\_CDTI2\_PB3

| #define TIMER2\_CDTI2\_PB3   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x1, 0x3) |
| --- |

## [◆ ](#ad66c79e81d41281df4969d775c1e54c6)TIMER2\_CDTI2\_PB4

| #define TIMER2\_CDTI2\_PB4   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x1, 0x4) |
| --- |

## [◆ ](#a48946d98ba43063c5c3772f398556f3d)TIMER2\_CDTI2\_PB5

| #define TIMER2\_CDTI2\_PB5   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x1, 0x5) |
| --- |

## [◆ ](#adaa89be7653ebbb82d77f6ccd3ba117a)TIMER3\_CC0\_PC0

| #define TIMER3\_CC0\_PC0   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x0) |
| --- |

## [◆ ](#ac49977cf88186dd85de660d7dca24093)TIMER3\_CC0\_PC1

| #define TIMER3\_CC0\_PC1   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x1) |
| --- |

## [◆ ](#a943818c0b36e315772740e9260777e98)TIMER3\_CC0\_PC2

| #define TIMER3\_CC0\_PC2   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x2) |
| --- |

## [◆ ](#a3b4277fa7886db498357df495e7d0f5b)TIMER3\_CC0\_PC3

| #define TIMER3\_CC0\_PC3   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x3) |
| --- |

## [◆ ](#afef97dfceb1266dad39f3c06a28cccde)TIMER3\_CC0\_PC4

| #define TIMER3\_CC0\_PC4   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x4) |
| --- |

## [◆ ](#a850b7d20c5e78b8609f0b4ab737fb59e)TIMER3\_CC0\_PC5

| #define TIMER3\_CC0\_PC5   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x5) |
| --- |

## [◆ ](#a06fb13b5ae7a9758c47f1d12f54bb643)TIMER3\_CC0\_PC6

| #define TIMER3\_CC0\_PC6   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x6) |
| --- |

## [◆ ](#aba2b4f6a903913dd21c7f919ee2d4bfd)TIMER3\_CC0\_PC7

| #define TIMER3\_CC0\_PC7   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x7) |
| --- |

## [◆ ](#afe2a5c724fc88c73ddcc1ec385e0582e)TIMER3\_CC0\_PC8

| #define TIMER3\_CC0\_PC8   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x8) |
| --- |

## [◆ ](#afab0c54879a2d089d2f5302ddf1f7462)TIMER3\_CC0\_PC9

| #define TIMER3\_CC0\_PC9   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x9) |
| --- |

## [◆ ](#a05f49738ea2e4cac6cff7b921761da01)TIMER3\_CC0\_PD0

| #define TIMER3\_CC0\_PD0   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x3, 0x0) |
| --- |

## [◆ ](#a4bf238e512342fc49c7a7d3fa1a13ee7)TIMER3\_CC0\_PD1

| #define TIMER3\_CC0\_PD1   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x3, 0x1) |
| --- |

## [◆ ](#a01e72605da25e5a408a0c3467be59205)TIMER3\_CC0\_PD2

| #define TIMER3\_CC0\_PD2   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x3, 0x2) |
| --- |

## [◆ ](#a3216588bd129dc8f82c27de826acb69b)TIMER3\_CC0\_PD3

| #define TIMER3\_CC0\_PD3   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x3, 0x3) |
| --- |

## [◆ ](#a0775d2d03fc98ce82fba4e19100e3b96)TIMER3\_CC0\_PD4

| #define TIMER3\_CC0\_PD4   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x3, 0x4) |
| --- |

## [◆ ](#a8a2faefb01867dbdc07a5d8d7844c043)TIMER3\_CC0\_PD5

| #define TIMER3\_CC0\_PD5   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x3, 0x5) |
| --- |

## [◆ ](#a0911c0d09d2d62526ee7d69a0abf0206)TIMER3\_CC1\_PC0

| #define TIMER3\_CC1\_PC0   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x0) |
| --- |

## [◆ ](#afc5b3d4f06f9392ff91d1a04039cc106)TIMER3\_CC1\_PC1

| #define TIMER3\_CC1\_PC1   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x1) |
| --- |

## [◆ ](#a841b61a51502f96b4b4db51f1747ddc2)TIMER3\_CC1\_PC2

| #define TIMER3\_CC1\_PC2   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x2) |
| --- |

## [◆ ](#abe25ec49b962f68c7e0b782fe8b31e0c)TIMER3\_CC1\_PC3

| #define TIMER3\_CC1\_PC3   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x3) |
| --- |

## [◆ ](#aafcf7edadba216092137ea9ce0c0da17)TIMER3\_CC1\_PC4

| #define TIMER3\_CC1\_PC4   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x4) |
| --- |

## [◆ ](#ac24430c7e08b2e0fe7bc63f92c01f9b5)TIMER3\_CC1\_PC5

| #define TIMER3\_CC1\_PC5   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x5) |
| --- |

## [◆ ](#a3400ddc7e6f8c607251d0b8f049cc0f1)TIMER3\_CC1\_PC6

| #define TIMER3\_CC1\_PC6   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x6) |
| --- |

## [◆ ](#a440e269a870fa8411ca1584a653df6e8)TIMER3\_CC1\_PC7

| #define TIMER3\_CC1\_PC7   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x7) |
| --- |

## [◆ ](#ad810dd127fc37f8e79e563203d4a2907)TIMER3\_CC1\_PC8

| #define TIMER3\_CC1\_PC8   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x8) |
| --- |

## [◆ ](#a755c761c565792dfec62073a02f79d0c)TIMER3\_CC1\_PC9

| #define TIMER3\_CC1\_PC9   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x9) |
| --- |

## [◆ ](#acb2b010357d2dd7e82266e1f530d93fc)TIMER3\_CC1\_PD0

| #define TIMER3\_CC1\_PD0   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x3, 0x0) |
| --- |

## [◆ ](#ac1cffc60caba52ee6ab100837b2b6cb3)TIMER3\_CC1\_PD1

| #define TIMER3\_CC1\_PD1   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x3, 0x1) |
| --- |

## [◆ ](#ac07495ddce953166e53c19d0a4f928fc)TIMER3\_CC1\_PD2

| #define TIMER3\_CC1\_PD2   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x3, 0x2) |
| --- |

## [◆ ](#a23644731303d1f1e527a7174ccef3e4a)TIMER3\_CC1\_PD3

| #define TIMER3\_CC1\_PD3   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x3, 0x3) |
| --- |

## [◆ ](#a06ed13488197cb82712911d67eb16b3e)TIMER3\_CC1\_PD4

| #define TIMER3\_CC1\_PD4   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x3, 0x4) |
| --- |

## [◆ ](#aef8394f92d0d255ee7cb41fd33f56cc6)TIMER3\_CC1\_PD5

| #define TIMER3\_CC1\_PD5   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x3, 0x5) |
| --- |

## [◆ ](#a7bf47abf6ea4ddf3f3e8dd71dcabc9f8)TIMER3\_CC2\_PC0

| #define TIMER3\_CC2\_PC0   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x0) |
| --- |

## [◆ ](#a2a2021e1cc5ec1156b6e3e8432a56dee)TIMER3\_CC2\_PC1

| #define TIMER3\_CC2\_PC1   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x1) |
| --- |

## [◆ ](#ad74e77cefd62c22a97737ab3eb7ce658)TIMER3\_CC2\_PC2

| #define TIMER3\_CC2\_PC2   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x2) |
| --- |

## [◆ ](#ab80ddb4234db5937e1244204d980e951)TIMER3\_CC2\_PC3

| #define TIMER3\_CC2\_PC3   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x3) |
| --- |

## [◆ ](#a717ccb54d7b93e7d4341f15ae10944cb)TIMER3\_CC2\_PC4

| #define TIMER3\_CC2\_PC4   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x4) |
| --- |

## [◆ ](#af10e6860473870cd0555e03907220ba7)TIMER3\_CC2\_PC5

| #define TIMER3\_CC2\_PC5   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x5) |
| --- |

## [◆ ](#aa221b71494071d6af232f0d8f9050aa7)TIMER3\_CC2\_PC6

| #define TIMER3\_CC2\_PC6   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x6) |
| --- |

## [◆ ](#adce105bc3d6134d45f130dfd77cfd59e)TIMER3\_CC2\_PC7

| #define TIMER3\_CC2\_PC7   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x7) |
| --- |

## [◆ ](#ae3a479466816d04e5ff040e1cfe59df0)TIMER3\_CC2\_PC8

| #define TIMER3\_CC2\_PC8   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x8) |
| --- |

## [◆ ](#ae9d00a013feb2612a01d773b73841035)TIMER3\_CC2\_PC9

| #define TIMER3\_CC2\_PC9   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x9) |
| --- |

## [◆ ](#a457c25d6e6cb832e66753dfc84d189f3)TIMER3\_CC2\_PD0

| #define TIMER3\_CC2\_PD0   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x3, 0x0) |
| --- |

## [◆ ](#adbeb6aa8891fdfe6510584bc8e5b5ced)TIMER3\_CC2\_PD1

| #define TIMER3\_CC2\_PD1   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x3, 0x1) |
| --- |

## [◆ ](#aa6524ad51bd80ac04276af0e722c5047)TIMER3\_CC2\_PD2

| #define TIMER3\_CC2\_PD2   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x3, 0x2) |
| --- |

## [◆ ](#ae94118e07443fa220d9162ad681c1a19)TIMER3\_CC2\_PD3

| #define TIMER3\_CC2\_PD3   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x3, 0x3) |
| --- |

## [◆ ](#a0a4d56c8f26bb269a10888e29cd0df4e)TIMER3\_CC2\_PD4

| #define TIMER3\_CC2\_PD4   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x3, 0x4) |
| --- |

## [◆ ](#a144c5d6fa9829dbf9d07b0693df2e52e)TIMER3\_CC2\_PD5

| #define TIMER3\_CC2\_PD5   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x3, 0x5) |
| --- |

## [◆ ](#a68db08edab7a0f208661895888ad0f4a)TIMER3\_CDTI0\_PC0

| #define TIMER3\_CDTI0\_PC0   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x0) |
| --- |

## [◆ ](#a3ae3f2df52006b2a53b70f7e940b8ed9)TIMER3\_CDTI0\_PC1

| #define TIMER3\_CDTI0\_PC1   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x1) |
| --- |

## [◆ ](#a1e3e29f3208cc7253d081b7c589632c1)TIMER3\_CDTI0\_PC2

| #define TIMER3\_CDTI0\_PC2   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x2) |
| --- |

## [◆ ](#a8ee6bc60c7704e1437c5d175df34d0a0)TIMER3\_CDTI0\_PC3

| #define TIMER3\_CDTI0\_PC3   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x3) |
| --- |

## [◆ ](#a6f98e4a7f4269972296fe587e83d0d7a)TIMER3\_CDTI0\_PC4

| #define TIMER3\_CDTI0\_PC4   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x4) |
| --- |

## [◆ ](#a348b50033a138bbc11ef6e99188fb023)TIMER3\_CDTI0\_PC5

| #define TIMER3\_CDTI0\_PC5   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x5) |
| --- |

## [◆ ](#aa744875bc8bbc9d504edf1022da599fd)TIMER3\_CDTI0\_PC6

| #define TIMER3\_CDTI0\_PC6   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x6) |
| --- |

## [◆ ](#a769a76d9258e7bdfdf7a8b21b70da011)TIMER3\_CDTI0\_PC7

| #define TIMER3\_CDTI0\_PC7   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x7) |
| --- |

## [◆ ](#aff387c44f16e275bae07a4f8ac81d16e)TIMER3\_CDTI0\_PC8

| #define TIMER3\_CDTI0\_PC8   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x8) |
| --- |

## [◆ ](#a235827cf9b740c57a808b180ab9a84ca)TIMER3\_CDTI0\_PC9

| #define TIMER3\_CDTI0\_PC9   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x9) |
| --- |

## [◆ ](#ae67b96fbcd3994e67f72d03f29690c02)TIMER3\_CDTI0\_PD0

| #define TIMER3\_CDTI0\_PD0   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x3, 0x0) |
| --- |

## [◆ ](#a477f3adb9d6430be9ef0746cba23b9fb)TIMER3\_CDTI0\_PD1

| #define TIMER3\_CDTI0\_PD1   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x3, 0x1) |
| --- |

## [◆ ](#a3ca82d8f98012743293a033b4c9c93be)TIMER3\_CDTI0\_PD2

| #define TIMER3\_CDTI0\_PD2   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x3, 0x2) |
| --- |

## [◆ ](#a3115a35f39b0b3f35120c728fc5c8c2f)TIMER3\_CDTI0\_PD3

| #define TIMER3\_CDTI0\_PD3   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x3, 0x3) |
| --- |

## [◆ ](#a5a5a79c390c93f0cceaca0668890ec8a)TIMER3\_CDTI0\_PD4

| #define TIMER3\_CDTI0\_PD4   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x3, 0x4) |
| --- |

## [◆ ](#ad4e7264378623d9e4eec2b1af05ad841)TIMER3\_CDTI0\_PD5

| #define TIMER3\_CDTI0\_PD5   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x3, 0x5) |
| --- |

## [◆ ](#a5dd1fea7f7ab7ee15a030b96a40d1114)TIMER3\_CDTI1\_PC0

| #define TIMER3\_CDTI1\_PC0   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x0) |
| --- |

## [◆ ](#aca7f55259fe2f36061078af791f3de4b)TIMER3\_CDTI1\_PC1

| #define TIMER3\_CDTI1\_PC1   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x1) |
| --- |

## [◆ ](#a03b1888fffa0036b1a9d92357d161cc7)TIMER3\_CDTI1\_PC2

| #define TIMER3\_CDTI1\_PC2   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x2) |
| --- |

## [◆ ](#a336444e4a0e7068e3e25e6908628c40c)TIMER3\_CDTI1\_PC3

| #define TIMER3\_CDTI1\_PC3   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x3) |
| --- |

## [◆ ](#a7c48bb98bfbace4681c6a1267d681e45)TIMER3\_CDTI1\_PC4

| #define TIMER3\_CDTI1\_PC4   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x4) |
| --- |

## [◆ ](#afa7ade2fc1198c66cd4812ac29befdf4)TIMER3\_CDTI1\_PC5

| #define TIMER3\_CDTI1\_PC5   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x5) |
| --- |

## [◆ ](#ad9ac8ee5259d40afead5b762ce90f4e6)TIMER3\_CDTI1\_PC6

| #define TIMER3\_CDTI1\_PC6   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x6) |
| --- |

## [◆ ](#af45d8db4d1da4526cce601e204743670)TIMER3\_CDTI1\_PC7

| #define TIMER3\_CDTI1\_PC7   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x7) |
| --- |

## [◆ ](#a922de5863e94bc01cc203fb0d09d075a)TIMER3\_CDTI1\_PC8

| #define TIMER3\_CDTI1\_PC8   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x8) |
| --- |

## [◆ ](#a5ad16b119b01a2279e2e14fc43b14744)TIMER3\_CDTI1\_PC9

| #define TIMER3\_CDTI1\_PC9   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x9) |
| --- |

## [◆ ](#a984b05d5d53c1068a86614a550995fc0)TIMER3\_CDTI1\_PD0

| #define TIMER3\_CDTI1\_PD0   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x3, 0x0) |
| --- |

## [◆ ](#a377c5ee038e274db1ddead0ad0fa7bf1)TIMER3\_CDTI1\_PD1

| #define TIMER3\_CDTI1\_PD1   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x3, 0x1) |
| --- |

## [◆ ](#a57207da12d6fa72e566b728371f4f402)TIMER3\_CDTI1\_PD2

| #define TIMER3\_CDTI1\_PD2   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x3, 0x2) |
| --- |

## [◆ ](#a18850fb5d2583d3652f7c43ea1d0ac39)TIMER3\_CDTI1\_PD3

| #define TIMER3\_CDTI1\_PD3   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x3, 0x3) |
| --- |

## [◆ ](#a419139192559d7484a6496741f780682)TIMER3\_CDTI1\_PD4

| #define TIMER3\_CDTI1\_PD4   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x3, 0x4) |
| --- |

## [◆ ](#a3d6af6e3bfb3e3f448584ae751dcf1ae)TIMER3\_CDTI1\_PD5

| #define TIMER3\_CDTI1\_PD5   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x3, 0x5) |
| --- |

## [◆ ](#a4a21cc75bb143d4fa1a84eb243fccc36)TIMER3\_CDTI2\_PC0

| #define TIMER3\_CDTI2\_PC0   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x0) |
| --- |

## [◆ ](#a881ccb7ad41ecf73423b97e8c489a6d0)TIMER3\_CDTI2\_PC1

| #define TIMER3\_CDTI2\_PC1   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x1) |
| --- |

## [◆ ](#aefbbc0a5e8e7673ccacdf399c288903e)TIMER3\_CDTI2\_PC2

| #define TIMER3\_CDTI2\_PC2   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x2) |
| --- |

## [◆ ](#abc867b08524924b26a2ed326a2b12155)TIMER3\_CDTI2\_PC3

| #define TIMER3\_CDTI2\_PC3   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x3) |
| --- |

## [◆ ](#a0befb875610ff387c2c1ac06f88d7b79)TIMER3\_CDTI2\_PC4

| #define TIMER3\_CDTI2\_PC4   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x4) |
| --- |

## [◆ ](#aea7c0881164e98c21fcf30d689deb592)TIMER3\_CDTI2\_PC5

| #define TIMER3\_CDTI2\_PC5   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x5) |
| --- |

## [◆ ](#a2a4909305fd0dbde0c3caba5f32fc896)TIMER3\_CDTI2\_PC6

| #define TIMER3\_CDTI2\_PC6   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x6) |
| --- |

## [◆ ](#a481f5eb7e5d4c148bc2be3d958973577)TIMER3\_CDTI2\_PC7

| #define TIMER3\_CDTI2\_PC7   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x7) |
| --- |

## [◆ ](#ae0de2380f85df6c295d5c88388e0bdec)TIMER3\_CDTI2\_PC8

| #define TIMER3\_CDTI2\_PC8   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x8) |
| --- |

## [◆ ](#ab8860f00495817a94f59ff502e4d4d44)TIMER3\_CDTI2\_PC9

| #define TIMER3\_CDTI2\_PC9   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x9) |
| --- |

## [◆ ](#a228392afbba95bbb69a65aae20dbb2d1)TIMER3\_CDTI2\_PD0

| #define TIMER3\_CDTI2\_PD0   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x3, 0x0) |
| --- |

## [◆ ](#a162d7a8c85197e047bc65cef7235a591)TIMER3\_CDTI2\_PD1

| #define TIMER3\_CDTI2\_PD1   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x3, 0x1) |
| --- |

## [◆ ](#a7f3873fb6abfaf970024318529fcfcd5)TIMER3\_CDTI2\_PD2

| #define TIMER3\_CDTI2\_PD2   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x3, 0x2) |
| --- |

## [◆ ](#a0c3fc7049d7dacfedfc4a04ced71202f)TIMER3\_CDTI2\_PD3

| #define TIMER3\_CDTI2\_PD3   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x3, 0x3) |
| --- |

## [◆ ](#adbfbccad761957506d72eb5b5f774ddc)TIMER3\_CDTI2\_PD4

| #define TIMER3\_CDTI2\_PD4   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x3, 0x4) |
| --- |

## [◆ ](#a676eb78dc7d678ce8080912279c42f87)TIMER3\_CDTI2\_PD5

| #define TIMER3\_CDTI2\_PD5   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x3, 0x5) |
| --- |

## [◆ ](#aa0c6e5e3f769ae31848239ea16fc8c26)TIMER4\_CC0\_PA0

| #define TIMER4\_CC0\_PA0   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x0) |
| --- |

## [◆ ](#ac49460d333f18f30fe332cad4ead4719)TIMER4\_CC0\_PA1

| #define TIMER4\_CC0\_PA1   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x1) |
| --- |

## [◆ ](#a92254bd9362d97e1fe55f8e9a7036857)TIMER4\_CC0\_PA2

| #define TIMER4\_CC0\_PA2   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x2) |
| --- |

## [◆ ](#a5c83b195cb0fd5344c2ec05a8547a063)TIMER4\_CC0\_PA3

| #define TIMER4\_CC0\_PA3   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x3) |
| --- |

## [◆ ](#a0daf9dc92bab78111bfc9425c38ba671)TIMER4\_CC0\_PA4

| #define TIMER4\_CC0\_PA4   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x4) |
| --- |

## [◆ ](#aebea07333a9390eb469f7efc8d4e773c)TIMER4\_CC0\_PA5

| #define TIMER4\_CC0\_PA5   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x5) |
| --- |

## [◆ ](#a88bab7bd85be0c93a81f359d872e65f2)TIMER4\_CC0\_PA6

| #define TIMER4\_CC0\_PA6   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x6) |
| --- |

## [◆ ](#ab527597383a746f75328fd7877d96389)TIMER4\_CC0\_PA7

| #define TIMER4\_CC0\_PA7   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x7) |
| --- |

## [◆ ](#af7ef30e6d27885e8f6eacdced332012d)TIMER4\_CC0\_PA8

| #define TIMER4\_CC0\_PA8   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x8) |
| --- |

## [◆ ](#a269be5490c9194daa1f56680597227f4)TIMER4\_CC0\_PA9

| #define TIMER4\_CC0\_PA9   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x9) |
| --- |

## [◆ ](#a6a53b58cd4ff5c60b736cbe9d25954fa)TIMER4\_CC0\_PB0

| #define TIMER4\_CC0\_PB0   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x1, 0x0) |
| --- |

## [◆ ](#a778ea39ff864aad8a92e35859bb1ec97)TIMER4\_CC0\_PB1

| #define TIMER4\_CC0\_PB1   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x1, 0x1) |
| --- |

## [◆ ](#a2fecff946d39c7745e061f2a4a4a03b7)TIMER4\_CC0\_PB2

| #define TIMER4\_CC0\_PB2   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x1, 0x2) |
| --- |

## [◆ ](#a1e7beb8ae86e28ef5a122118644a0b6d)TIMER4\_CC0\_PB3

| #define TIMER4\_CC0\_PB3   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x1, 0x3) |
| --- |

## [◆ ](#a99a47cb9b6cb9273332d2a8f6598a52f)TIMER4\_CC0\_PB4

| #define TIMER4\_CC0\_PB4   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x1, 0x4) |
| --- |

## [◆ ](#a627ec43ac8af76e99e57c6c79de245e4)TIMER4\_CC0\_PB5

| #define TIMER4\_CC0\_PB5   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x1, 0x5) |
| --- |

## [◆ ](#a0a20fe004087b6d6599f775aefac56f2)TIMER4\_CC1\_PA0

| #define TIMER4\_CC1\_PA0   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x0) |
| --- |

## [◆ ](#a044a7b8e14be441705f29e4b6015ee08)TIMER4\_CC1\_PA1

| #define TIMER4\_CC1\_PA1   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x1) |
| --- |

## [◆ ](#adbd211cd9344a88c6301462a5e3edc51)TIMER4\_CC1\_PA2

| #define TIMER4\_CC1\_PA2   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x2) |
| --- |

## [◆ ](#a5a04fcf2fff3afd10e98cb2e31509cc5)TIMER4\_CC1\_PA3

| #define TIMER4\_CC1\_PA3   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x3) |
| --- |

## [◆ ](#a8d301ec962fe2cce8ba002f274988559)TIMER4\_CC1\_PA4

| #define TIMER4\_CC1\_PA4   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x4) |
| --- |

## [◆ ](#a102bc4ebc9988c58529e288cbae2dcf5)TIMER4\_CC1\_PA5

| #define TIMER4\_CC1\_PA5   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x5) |
| --- |

## [◆ ](#a3ea21e7b459ab219ee593f4ded6423d6)TIMER4\_CC1\_PA6

| #define TIMER4\_CC1\_PA6   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x6) |
| --- |

## [◆ ](#afbf528e09cd5f8416ad6a21bf15e6dc7)TIMER4\_CC1\_PA7

| #define TIMER4\_CC1\_PA7   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x7) |
| --- |

## [◆ ](#a5b53aae41cdc44147d6333ce5d7c28aa)TIMER4\_CC1\_PA8

| #define TIMER4\_CC1\_PA8   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x8) |
| --- |

## [◆ ](#ace92b6394b1909d14dd0be0567787c95)TIMER4\_CC1\_PA9

| #define TIMER4\_CC1\_PA9   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x9) |
| --- |

## [◆ ](#a65dd111e27e3d7ba7cec249ea3354ff4)TIMER4\_CC1\_PB0

| #define TIMER4\_CC1\_PB0   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x1, 0x0) |
| --- |

## [◆ ](#ac64bc36ec5794d92ac2bf256147645f5)TIMER4\_CC1\_PB1

| #define TIMER4\_CC1\_PB1   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x1, 0x1) |
| --- |

## [◆ ](#a38afb957c997a8378e3aebb6141f7426)TIMER4\_CC1\_PB2

| #define TIMER4\_CC1\_PB2   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x1, 0x2) |
| --- |

## [◆ ](#a280bb1ebea122956c890dcb8d84b2241)TIMER4\_CC1\_PB3

| #define TIMER4\_CC1\_PB3   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x1, 0x3) |
| --- |

## [◆ ](#a767e437a09fa17b72c8c3f9c7dfdbf60)TIMER4\_CC1\_PB4

| #define TIMER4\_CC1\_PB4   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x1, 0x4) |
| --- |

## [◆ ](#a3e3d6d3817651318f5aca14244f06153)TIMER4\_CC1\_PB5

| #define TIMER4\_CC1\_PB5   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x1, 0x5) |
| --- |

## [◆ ](#a777870e82a20af4a6a6e71a5b636fca6)TIMER4\_CC2\_PA0

| #define TIMER4\_CC2\_PA0   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x0) |
| --- |

## [◆ ](#a85d5e0d8c945839bbda1cdcfb1c27952)TIMER4\_CC2\_PA1

| #define TIMER4\_CC2\_PA1   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x1) |
| --- |

## [◆ ](#a1e87cfdb2f81b1168fd9fd61e4451103)TIMER4\_CC2\_PA2

| #define TIMER4\_CC2\_PA2   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x2) |
| --- |

## [◆ ](#a3a16aab894717ffae5bcb0ab14cc6dbb)TIMER4\_CC2\_PA3

| #define TIMER4\_CC2\_PA3   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x3) |
| --- |

## [◆ ](#a2dfa60f8a9d458a782ab2df7f2209976)TIMER4\_CC2\_PA4

| #define TIMER4\_CC2\_PA4   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x4) |
| --- |

## [◆ ](#a8a3aac099645db504605942c9e86083f)TIMER4\_CC2\_PA5

| #define TIMER4\_CC2\_PA5   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x5) |
| --- |

## [◆ ](#a73ab6a5f63c5e2c778913a196c49915f)TIMER4\_CC2\_PA6

| #define TIMER4\_CC2\_PA6   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x6) |
| --- |

## [◆ ](#a1f5ce55fa587d01d50b1f8496b4c2640)TIMER4\_CC2\_PA7

| #define TIMER4\_CC2\_PA7   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x7) |
| --- |

## [◆ ](#a13b0916acd52e39c467b2ae7c8f08e22)TIMER4\_CC2\_PA8

| #define TIMER4\_CC2\_PA8   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x8) |
| --- |

## [◆ ](#ae20b7bb781c40b3a48930ec2741a35ab)TIMER4\_CC2\_PA9

| #define TIMER4\_CC2\_PA9   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x9) |
| --- |

## [◆ ](#a1965744950bba0b98b124ef7fd308538)TIMER4\_CC2\_PB0

| #define TIMER4\_CC2\_PB0   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x1, 0x0) |
| --- |

## [◆ ](#af51b2d503e11e751815cc9e46c777cc8)TIMER4\_CC2\_PB1

| #define TIMER4\_CC2\_PB1   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x1, 0x1) |
| --- |

## [◆ ](#a9ae5f6cda5ee8fc6551a58bc1dea1b6a)TIMER4\_CC2\_PB2

| #define TIMER4\_CC2\_PB2   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x1, 0x2) |
| --- |

## [◆ ](#a4033b892135db2f425c041fb353dd94e)TIMER4\_CC2\_PB3

| #define TIMER4\_CC2\_PB3   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x1, 0x3) |
| --- |

## [◆ ](#ab9f0f4839c1db0ff24c71e8a43bca20b)TIMER4\_CC2\_PB4

| #define TIMER4\_CC2\_PB4   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x1, 0x4) |
| --- |

## [◆ ](#ad09a118179644890178c1ae4504a0bf4)TIMER4\_CC2\_PB5

| #define TIMER4\_CC2\_PB5   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x1, 0x5) |
| --- |

## [◆ ](#a7a3baa51540b54c8677085fce6fdff99)TIMER4\_CDTI0\_PA0

| #define TIMER4\_CDTI0\_PA0   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x0) |
| --- |

## [◆ ](#a46ad78924a9aebe629236e072c1c013b)TIMER4\_CDTI0\_PA1

| #define TIMER4\_CDTI0\_PA1   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x1) |
| --- |

## [◆ ](#ab302b8f1cc1c0b103e4a315173af2455)TIMER4\_CDTI0\_PA2

| #define TIMER4\_CDTI0\_PA2   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x2) |
| --- |

## [◆ ](#a6cabbf3093dc73c82ab34ffd0a979b9e)TIMER4\_CDTI0\_PA3

| #define TIMER4\_CDTI0\_PA3   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x3) |
| --- |

## [◆ ](#a228a5febbceec760f773b1114a978c12)TIMER4\_CDTI0\_PA4

| #define TIMER4\_CDTI0\_PA4   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x4) |
| --- |

## [◆ ](#a44b20d92c88a15471c81f3f408126476)TIMER4\_CDTI0\_PA5

| #define TIMER4\_CDTI0\_PA5   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x5) |
| --- |

## [◆ ](#a2c06384e73db9a53f2a46c79991f022e)TIMER4\_CDTI0\_PA6

| #define TIMER4\_CDTI0\_PA6   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x6) |
| --- |

## [◆ ](#a1ccb51b05ade839e65eb898115a09a1f)TIMER4\_CDTI0\_PA7

| #define TIMER4\_CDTI0\_PA7   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x7) |
| --- |

## [◆ ](#aec88b0761fc5162dfa63daaaf0d8dd80)TIMER4\_CDTI0\_PA8

| #define TIMER4\_CDTI0\_PA8   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x8) |
| --- |

## [◆ ](#a363db5107db42dbd9e512cf4d4890883)TIMER4\_CDTI0\_PA9

| #define TIMER4\_CDTI0\_PA9   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x9) |
| --- |

## [◆ ](#a7417d210f904b5448a079950b92d7e85)TIMER4\_CDTI0\_PB0

| #define TIMER4\_CDTI0\_PB0   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x1, 0x0) |
| --- |

## [◆ ](#a5943529095abd138015248fc122f0af1)TIMER4\_CDTI0\_PB1

| #define TIMER4\_CDTI0\_PB1   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x1, 0x1) |
| --- |

## [◆ ](#aeffc25dbbbc7d1eb199cd29b7cf7e0a0)TIMER4\_CDTI0\_PB2

| #define TIMER4\_CDTI0\_PB2   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x1, 0x2) |
| --- |

## [◆ ](#aeda432d234c691de7a000702c9e13ba4)TIMER4\_CDTI0\_PB3

| #define TIMER4\_CDTI0\_PB3   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x1, 0x3) |
| --- |

## [◆ ](#a128f18c80a9343d189b856d1d4f3b128)TIMER4\_CDTI0\_PB4

| #define TIMER4\_CDTI0\_PB4   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x1, 0x4) |
| --- |

## [◆ ](#a19aef3f3f90b44d98df95ddbf6a60e76)TIMER4\_CDTI0\_PB5

| #define TIMER4\_CDTI0\_PB5   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x1, 0x5) |
| --- |

## [◆ ](#a2c8f5c89e8e8d8acf768efc55c2c1557)TIMER4\_CDTI1\_PA0

| #define TIMER4\_CDTI1\_PA0   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x0) |
| --- |

## [◆ ](#aeec9e93ade4349a932987805b56427ea)TIMER4\_CDTI1\_PA1

| #define TIMER4\_CDTI1\_PA1   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x1) |
| --- |

## [◆ ](#a5504301d2109fd9b938b6d2183e1e23f)TIMER4\_CDTI1\_PA2

| #define TIMER4\_CDTI1\_PA2   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x2) |
| --- |

## [◆ ](#a9baa482a3d5caf216a47294c2b74b060)TIMER4\_CDTI1\_PA3

| #define TIMER4\_CDTI1\_PA3   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x3) |
| --- |

## [◆ ](#a84c9ec2e762283faf0804fdc2d4b8e67)TIMER4\_CDTI1\_PA4

| #define TIMER4\_CDTI1\_PA4   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x4) |
| --- |

## [◆ ](#abc07eda4d4f0a0a189628e9e2e7eed05)TIMER4\_CDTI1\_PA5

| #define TIMER4\_CDTI1\_PA5   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x5) |
| --- |

## [◆ ](#a1b72f464803bcaa51f912a41e0d92023)TIMER4\_CDTI1\_PA6

| #define TIMER4\_CDTI1\_PA6   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x6) |
| --- |

## [◆ ](#a8c6b70c5db7bf891a3fb608f7f50e3f1)TIMER4\_CDTI1\_PA7

| #define TIMER4\_CDTI1\_PA7   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x7) |
| --- |

## [◆ ](#ac2bab95ab6f8067049fc144683ce0e77)TIMER4\_CDTI1\_PA8

| #define TIMER4\_CDTI1\_PA8   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x8) |
| --- |

## [◆ ](#a225ed569ec2351827f71df73c35b9659)TIMER4\_CDTI1\_PA9

| #define TIMER4\_CDTI1\_PA9   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x9) |
| --- |

## [◆ ](#a9897ffcb326b237d2258b7fbd32111c9)TIMER4\_CDTI1\_PB0

| #define TIMER4\_CDTI1\_PB0   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x1, 0x0) |
| --- |

## [◆ ](#a8ffdf1e7b414a675d6ea582e30047251)TIMER4\_CDTI1\_PB1

| #define TIMER4\_CDTI1\_PB1   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x1, 0x1) |
| --- |

## [◆ ](#a8bc164f77d9311ae19c11eb993724a96)TIMER4\_CDTI1\_PB2

| #define TIMER4\_CDTI1\_PB2   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x1, 0x2) |
| --- |

## [◆ ](#a2feb1f73241aaedd10d1f30a8402fb6f)TIMER4\_CDTI1\_PB3

| #define TIMER4\_CDTI1\_PB3   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x1, 0x3) |
| --- |

## [◆ ](#a1a7a79e99bf52e3f2c6241608c7fc814)TIMER4\_CDTI1\_PB4

| #define TIMER4\_CDTI1\_PB4   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x1, 0x4) |
| --- |

## [◆ ](#a26c42742eb2923f24fa10ffc1fe11600)TIMER4\_CDTI1\_PB5

| #define TIMER4\_CDTI1\_PB5   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x1, 0x5) |
| --- |

## [◆ ](#a0167c1d5682489dcfdd9d60fa1a2cc44)TIMER4\_CDTI2\_PA0

| #define TIMER4\_CDTI2\_PA0   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x0) |
| --- |

## [◆ ](#a8c51fb1efbd523ef8d5b57b66d65060f)TIMER4\_CDTI2\_PA1

| #define TIMER4\_CDTI2\_PA1   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x1) |
| --- |

## [◆ ](#aea7d724240277e0a0b3c2334063e6b6a)TIMER4\_CDTI2\_PA2

| #define TIMER4\_CDTI2\_PA2   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x2) |
| --- |

## [◆ ](#ab8588c060f8671f5696a0e2529394a37)TIMER4\_CDTI2\_PA3

| #define TIMER4\_CDTI2\_PA3   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x3) |
| --- |

## [◆ ](#a4c566e93e8f5375744be6303f5049840)TIMER4\_CDTI2\_PA4

| #define TIMER4\_CDTI2\_PA4   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x4) |
| --- |

## [◆ ](#a4218800d01dc2d8e767d1e03e28c00e4)TIMER4\_CDTI2\_PA5

| #define TIMER4\_CDTI2\_PA5   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x5) |
| --- |

## [◆ ](#af9c15b67b7e09875d5a9991dac81222f)TIMER4\_CDTI2\_PA6

| #define TIMER4\_CDTI2\_PA6   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x6) |
| --- |

## [◆ ](#a664bd862ef44614302fe82a809d1f148)TIMER4\_CDTI2\_PA7

| #define TIMER4\_CDTI2\_PA7   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x7) |
| --- |

## [◆ ](#ad20202f301b5e59f477ab02d6ee37546)TIMER4\_CDTI2\_PA8

| #define TIMER4\_CDTI2\_PA8   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x8) |
| --- |

## [◆ ](#aa5262ec786fc475be010ce5c1b3ed78c)TIMER4\_CDTI2\_PA9

| #define TIMER4\_CDTI2\_PA9   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x9) |
| --- |

## [◆ ](#a35aa90b994c639d68f2a8bbd65903494)TIMER4\_CDTI2\_PB0

| #define TIMER4\_CDTI2\_PB0   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x1, 0x0) |
| --- |

## [◆ ](#a20970e543f42e4785409f8f391d6daa9)TIMER4\_CDTI2\_PB1

| #define TIMER4\_CDTI2\_PB1   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x1, 0x1) |
| --- |

## [◆ ](#aee236ba0af0b2d08871f15ca7d78cd2c)TIMER4\_CDTI2\_PB2

| #define TIMER4\_CDTI2\_PB2   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x1, 0x2) |
| --- |

## [◆ ](#a976af94ec2e61f8b59edebf73e3222f0)TIMER4\_CDTI2\_PB3

| #define TIMER4\_CDTI2\_PB3   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x1, 0x3) |
| --- |

## [◆ ](#a03b1a79e2c32ed563d6ebf81b9741d14)TIMER4\_CDTI2\_PB4

| #define TIMER4\_CDTI2\_PB4   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x1, 0x4) |
| --- |

## [◆ ](#ab02f811798eba69b02445ad1ea459e0e)TIMER4\_CDTI2\_PB5

| #define TIMER4\_CDTI2\_PB5   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x1, 0x5) |
| --- |

## [◆ ](#a16af201487286a8bad218c94245a88c7)USART0\_CLK\_PA0

| #define USART0\_CLK\_PA0   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x0) |
| --- |

## [◆ ](#a1c3041ba213cdbcb2796dbffa01b8571)USART0\_CLK\_PA1

| #define USART0\_CLK\_PA1   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x1) |
| --- |

## [◆ ](#a1e546e7130f7012f29d6d2aad3e97b39)USART0\_CLK\_PA2

| #define USART0\_CLK\_PA2   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x2) |
| --- |

## [◆ ](#aa78910cf4b3c816508e2e97288489f16)USART0\_CLK\_PA3

| #define USART0\_CLK\_PA3   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x3) |
| --- |

## [◆ ](#a76684ba202fa4fb3b5e545a031f0c841)USART0\_CLK\_PA4

| #define USART0\_CLK\_PA4   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x4) |
| --- |

## [◆ ](#a92cda8774c81ce2539654516c2b62dd6)USART0\_CLK\_PA5

| #define USART0\_CLK\_PA5   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x5) |
| --- |

## [◆ ](#a6c67ed947caacf669665e133327a7e00)USART0\_CLK\_PA6

| #define USART0\_CLK\_PA6   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x6) |
| --- |

## [◆ ](#af8f2d47db5aa651708f0d2dea2e39c48)USART0\_CLK\_PA7

| #define USART0\_CLK\_PA7   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x7) |
| --- |

## [◆ ](#a06fdcd2c3ae7b6162aff6a3fbeac94a8)USART0\_CLK\_PA8

| #define USART0\_CLK\_PA8   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x8) |
| --- |

## [◆ ](#a1151deef40a267aa9d8ad1b76f86d74e)USART0\_CLK\_PA9

| #define USART0\_CLK\_PA9   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x9) |
| --- |

## [◆ ](#a80303adbfa7489fdefcbf14b38c25194)USART0\_CLK\_PB0

| #define USART0\_CLK\_PB0   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x1, 0x0) |
| --- |

## [◆ ](#a242754151600f954e6c9063254862537)USART0\_CLK\_PB1

| #define USART0\_CLK\_PB1   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x1, 0x1) |
| --- |

## [◆ ](#a8ed2cedbe7fd2daf10bee286f2bb6468)USART0\_CLK\_PB2

| #define USART0\_CLK\_PB2   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x1, 0x2) |
| --- |

## [◆ ](#abe23ca58f25d6bfa5b939cf58d7a0dee)USART0\_CLK\_PB3

| #define USART0\_CLK\_PB3   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x1, 0x3) |
| --- |

## [◆ ](#abac165e111f292793ab41b4411ad847c)USART0\_CLK\_PB4

| #define USART0\_CLK\_PB4   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x1, 0x4) |
| --- |

## [◆ ](#a2fae78dc9ec493c981eb6d582916086e)USART0\_CLK\_PB5

| #define USART0\_CLK\_PB5   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x1, 0x5) |
| --- |

## [◆ ](#a9504215a474950cdc3ae3e76bb0ee428)USART0\_CLK\_PC0

| #define USART0\_CLK\_PC0   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x0) |
| --- |

## [◆ ](#aa03060eb71eadfc578315d600f297665)USART0\_CLK\_PC1

| #define USART0\_CLK\_PC1   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x1) |
| --- |

## [◆ ](#afd46249fb73936581af6f762bf749096)USART0\_CLK\_PC2

| #define USART0\_CLK\_PC2   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x2) |
| --- |

## [◆ ](#a39fd0a4cefb1903103818add5272cb69)USART0\_CLK\_PC3

| #define USART0\_CLK\_PC3   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x3) |
| --- |

## [◆ ](#a86e90f6c37f90fb2c79d163239123815)USART0\_CLK\_PC4

| #define USART0\_CLK\_PC4   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x4) |
| --- |

## [◆ ](#a13955f88c0655104ccceaf72d8fcc000)USART0\_CLK\_PC5

| #define USART0\_CLK\_PC5   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x5) |
| --- |

## [◆ ](#acd2b16c2082f7bbb996a7ba08a9339f6)USART0\_CLK\_PC6

| #define USART0\_CLK\_PC6   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x6) |
| --- |

## [◆ ](#af26cd974218fae8b631ed6bbc3505da6)USART0\_CLK\_PC7

| #define USART0\_CLK\_PC7   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x7) |
| --- |

## [◆ ](#a0a63d69334e7948f1eb02efe67272b6f)USART0\_CLK\_PC8

| #define USART0\_CLK\_PC8   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x8) |
| --- |

## [◆ ](#a11f0d43044117367cd5649c574288a06)USART0\_CLK\_PC9

| #define USART0\_CLK\_PC9   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x9) |
| --- |

## [◆ ](#aa5dd3eff1b983555e7437c815d69d6c1)USART0\_CLK\_PD0

| #define USART0\_CLK\_PD0   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x3, 0x0) |
| --- |

## [◆ ](#a808576a293b84b259f0b749099ee53f0)USART0\_CLK\_PD1

| #define USART0\_CLK\_PD1   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x3, 0x1) |
| --- |

## [◆ ](#aba6f9004672cd8fcc046036c5a5e385d)USART0\_CLK\_PD2

| #define USART0\_CLK\_PD2   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x3, 0x2) |
| --- |

## [◆ ](#acf11ed64457d633e70ba8551caaad511)USART0\_CLK\_PD3

| #define USART0\_CLK\_PD3   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x3, 0x3) |
| --- |

## [◆ ](#a8fa68ae31cbf6041854bd1de35efa747)USART0\_CLK\_PD4

| #define USART0\_CLK\_PD4   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x3, 0x4) |
| --- |

## [◆ ](#ac152b5f4693f5ca67901b7ce5b1f74c7)USART0\_CLK\_PD5

| #define USART0\_CLK\_PD5   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x3, 0x5) |
| --- |

## [◆ ](#a8b31d0e72dc71f813f3ae21da1b064dc)USART0\_CS\_PA0

| #define USART0\_CS\_PA0   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x0) |
| --- |

## [◆ ](#affbbbbf6348af411b5392e462304edee)USART0\_CS\_PA1

| #define USART0\_CS\_PA1   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x1) |
| --- |

## [◆ ](#a70d22cbabea10e31293a21262f6a64b3)USART0\_CS\_PA2

| #define USART0\_CS\_PA2   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x2) |
| --- |

## [◆ ](#a2a80bc71c923ed7c6fd2865d869864fc)USART0\_CS\_PA3

| #define USART0\_CS\_PA3   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x3) |
| --- |

## [◆ ](#af24e43481767fe27cdd78f5e27f15d7f)USART0\_CS\_PA4

| #define USART0\_CS\_PA4   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x4) |
| --- |

## [◆ ](#a7cb722df10819495d5059933ddf122a4)USART0\_CS\_PA5

| #define USART0\_CS\_PA5   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x5) |
| --- |

## [◆ ](#a94d45fdffdc79cc92994105238c9f0f8)USART0\_CS\_PA6

| #define USART0\_CS\_PA6   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x6) |
| --- |

## [◆ ](#a75603bdb24ba0f19a841a1ed7b3fc683)USART0\_CS\_PA7

| #define USART0\_CS\_PA7   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x7) |
| --- |

## [◆ ](#a2eb48dfecd71b07998cff24d69052360)USART0\_CS\_PA8

| #define USART0\_CS\_PA8   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x8) |
| --- |

## [◆ ](#a296a14e4ef77412fd396a4e2ded0b3b3)USART0\_CS\_PA9

| #define USART0\_CS\_PA9   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x9) |
| --- |

## [◆ ](#a5f92c862131c6dfd2dc95146cdfa09aa)USART0\_CS\_PB0

| #define USART0\_CS\_PB0   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x1, 0x0) |
| --- |

## [◆ ](#aa45d4cfe63813c6c8aa8602e0783f7fb)USART0\_CS\_PB1

| #define USART0\_CS\_PB1   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x1, 0x1) |
| --- |

## [◆ ](#a8d25b8c147a7d0777e023a56bc47b5ea)USART0\_CS\_PB2

| #define USART0\_CS\_PB2   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x1, 0x2) |
| --- |

## [◆ ](#a8a749535093e7817f27396459ee97d72)USART0\_CS\_PB3

| #define USART0\_CS\_PB3   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x1, 0x3) |
| --- |

## [◆ ](#a25fa64c3232371544eba09423fb0c765)USART0\_CS\_PB4

| #define USART0\_CS\_PB4   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x1, 0x4) |
| --- |

## [◆ ](#a07b913ebc5b03c4519fdd4136f907021)USART0\_CS\_PB5

| #define USART0\_CS\_PB5   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x1, 0x5) |
| --- |

## [◆ ](#a2372be5754b13cafcef6a63d63548924)USART0\_CS\_PC0

| #define USART0\_CS\_PC0   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x0) |
| --- |

## [◆ ](#a0033eb0ea09f9dab2ab5a20d185ba0e0)USART0\_CS\_PC1

| #define USART0\_CS\_PC1   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x1) |
| --- |

## [◆ ](#afdc21300ca9ab485a7d97fa344ee3292)USART0\_CS\_PC2

| #define USART0\_CS\_PC2   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x2) |
| --- |

## [◆ ](#acc373a1b4402c4f4f229524837a4c3ac)USART0\_CS\_PC3

| #define USART0\_CS\_PC3   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x3) |
| --- |

## [◆ ](#a3bb143a83558aaa91fad609259a13044)USART0\_CS\_PC4

| #define USART0\_CS\_PC4   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x4) |
| --- |

## [◆ ](#ab4ae79a567d023b7f886019e3d5518b1)USART0\_CS\_PC5

| #define USART0\_CS\_PC5   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x5) |
| --- |

## [◆ ](#a8ad8102bed214716bdcf82c1747e2ce3)USART0\_CS\_PC6

| #define USART0\_CS\_PC6   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x6) |
| --- |

## [◆ ](#a3f1d10140e34a916172f4ccfeb086fea)USART0\_CS\_PC7

| #define USART0\_CS\_PC7   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x7) |
| --- |

## [◆ ](#a3167008284cd4666dc930bdb47e104a1)USART0\_CS\_PC8

| #define USART0\_CS\_PC8   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x8) |
| --- |

## [◆ ](#ac25117b1cb234416a65c9ccb6a52b385)USART0\_CS\_PC9

| #define USART0\_CS\_PC9   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x9) |
| --- |

## [◆ ](#a4d2ef2ccd5f3dbefa048e37f2bb40b8b)USART0\_CS\_PD0

| #define USART0\_CS\_PD0   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x3, 0x0) |
| --- |

## [◆ ](#a1f6089f92cf5168cbd9a6daa0f336ebb)USART0\_CS\_PD1

| #define USART0\_CS\_PD1   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x3, 0x1) |
| --- |

## [◆ ](#a4e54dcbabdbebe60f309a31c7acbe30f)USART0\_CS\_PD2

| #define USART0\_CS\_PD2   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x3, 0x2) |
| --- |

## [◆ ](#a00073504dbe55119dc3dac466c5f816f)USART0\_CS\_PD3

| #define USART0\_CS\_PD3   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x3, 0x3) |
| --- |

## [◆ ](#adc4cf5aa4e7acad165031376bf0e2551)USART0\_CS\_PD4

| #define USART0\_CS\_PD4   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x3, 0x4) |
| --- |

## [◆ ](#a03e9928b1089537c453bdf46854a1921)USART0\_CS\_PD5

| #define USART0\_CS\_PD5   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x3, 0x5) |
| --- |

## [◆ ](#ac3ca642f56ef830b82675e79f7741f3b)USART0\_CTS\_PA0

| #define USART0\_CTS\_PA0   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x0) |
| --- |

## [◆ ](#afe282cc2c0b48daca846099518f85197)USART0\_CTS\_PA1

| #define USART0\_CTS\_PA1   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x1) |
| --- |

## [◆ ](#abb4ee35f35c67053d9e499b9b6586848)USART0\_CTS\_PA2

| #define USART0\_CTS\_PA2   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x2) |
| --- |

## [◆ ](#ac7c103a6f291a3ba02c78b56cda7522e)USART0\_CTS\_PA3

| #define USART0\_CTS\_PA3   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x3) |
| --- |

## [◆ ](#adf4ae6f16534af5c18b924890e70b909)USART0\_CTS\_PA4

| #define USART0\_CTS\_PA4   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x4) |
| --- |

## [◆ ](#a375e4336fc59220a304beb9e818038a8)USART0\_CTS\_PA5

| #define USART0\_CTS\_PA5   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x5) |
| --- |

## [◆ ](#a34bdfb80ac61bcde4828b64e5ab7bc6a)USART0\_CTS\_PA6

| #define USART0\_CTS\_PA6   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x6) |
| --- |

## [◆ ](#afe45fe9337ee945b705d60efd975071a)USART0\_CTS\_PA7

| #define USART0\_CTS\_PA7   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x7) |
| --- |

## [◆ ](#a45cbf3ce6396ad5caf50bca5bb336f04)USART0\_CTS\_PA8

| #define USART0\_CTS\_PA8   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x8) |
| --- |

## [◆ ](#aa310cb8173b02179e08e717af5117e6b)USART0\_CTS\_PA9

| #define USART0\_CTS\_PA9   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x9) |
| --- |

## [◆ ](#a5e6fd192eef4cb50593c5f8f225607db)USART0\_CTS\_PB0

| #define USART0\_CTS\_PB0   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x1, 0x0) |
| --- |

## [◆ ](#a8ba9df244ac2a7e580a45372c6db1496)USART0\_CTS\_PB1

| #define USART0\_CTS\_PB1   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x1, 0x1) |
| --- |

## [◆ ](#ac99b8ee386e51b37acfe825e4111dbd4)USART0\_CTS\_PB2

| #define USART0\_CTS\_PB2   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x1, 0x2) |
| --- |

## [◆ ](#a0c63835444cc57f402820f473de55618)USART0\_CTS\_PB3

| #define USART0\_CTS\_PB3   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x1, 0x3) |
| --- |

## [◆ ](#a2da02e86c7776fb1674ad0235c3c342a)USART0\_CTS\_PB4

| #define USART0\_CTS\_PB4   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x1, 0x4) |
| --- |

## [◆ ](#aab146714b510ce9d438cf61b25cee79e)USART0\_CTS\_PB5

| #define USART0\_CTS\_PB5   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x1, 0x5) |
| --- |

## [◆ ](#a176d8e361297cf55c78d425fed824f1f)USART0\_CTS\_PC0

| #define USART0\_CTS\_PC0   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x0) |
| --- |

## [◆ ](#acae624423e070b271d7c62019dc19ca6)USART0\_CTS\_PC1

| #define USART0\_CTS\_PC1   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x1) |
| --- |

## [◆ ](#a11af346f3b4cd506e5f42d802eeaa7fa)USART0\_CTS\_PC2

| #define USART0\_CTS\_PC2   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x2) |
| --- |

## [◆ ](#acde9eb8d5c61ec7fa0c66248de8acdb3)USART0\_CTS\_PC3

| #define USART0\_CTS\_PC3   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x3) |
| --- |

## [◆ ](#a0c7d39bd6f59e8a9281d68560e3ea0cc)USART0\_CTS\_PC4

| #define USART0\_CTS\_PC4   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x4) |
| --- |

## [◆ ](#aa2c0ec406645422286f3099c880051e8)USART0\_CTS\_PC5

| #define USART0\_CTS\_PC5   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x5) |
| --- |

## [◆ ](#a8886647e93011bfd9253bf57af7451f0)USART0\_CTS\_PC6

| #define USART0\_CTS\_PC6   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x6) |
| --- |

## [◆ ](#a8fc778b9808ef6cad5104cdee4c8b305)USART0\_CTS\_PC7

| #define USART0\_CTS\_PC7   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x7) |
| --- |

## [◆ ](#adfcf13e69aea1f02cb6874dce97dce31)USART0\_CTS\_PC8

| #define USART0\_CTS\_PC8   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x8) |
| --- |

## [◆ ](#a61b23cd8cf28189943376ef6787794b4)USART0\_CTS\_PC9

| #define USART0\_CTS\_PC9   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x9) |
| --- |

## [◆ ](#ad8f9198b67b3777baf4d6fa6771c2a40)USART0\_CTS\_PD0

| #define USART0\_CTS\_PD0   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x3, 0x0) |
| --- |

## [◆ ](#acf9112247d4fa36974b7e221d156b27c)USART0\_CTS\_PD1

| #define USART0\_CTS\_PD1   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x3, 0x1) |
| --- |

## [◆ ](#a86617a975bc950800ea9deba65ffaa19)USART0\_CTS\_PD2

| #define USART0\_CTS\_PD2   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x3, 0x2) |
| --- |

## [◆ ](#abf78324d648e5c035d29a33b4b93dd82)USART0\_CTS\_PD3

| #define USART0\_CTS\_PD3   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x3, 0x3) |
| --- |

## [◆ ](#a24a47d714bae303a53b15303fcc73855)USART0\_CTS\_PD4

| #define USART0\_CTS\_PD4   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x3, 0x4) |
| --- |

## [◆ ](#aaffa82b5324dfbac09e720731b7c7387)USART0\_CTS\_PD5

| #define USART0\_CTS\_PD5   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x3, 0x5) |
| --- |

## [◆ ](#a104b44454bfafbbdd54fe6b53c2dff33)USART0\_RTS\_PA0

| #define USART0\_RTS\_PA0   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x0) |
| --- |

## [◆ ](#abbaf9c9b55c0673fc774610b83aca313)USART0\_RTS\_PA1

| #define USART0\_RTS\_PA1   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x1) |
| --- |

## [◆ ](#abaae8c12c4daa90d49e9f327f16a6691)USART0\_RTS\_PA2

| #define USART0\_RTS\_PA2   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x2) |
| --- |

## [◆ ](#a4ba035c607b639dfef668323a43a3f7f)USART0\_RTS\_PA3

| #define USART0\_RTS\_PA3   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x3) |
| --- |

## [◆ ](#a234727fb3ae07a22c350d4a0a58c30cb)USART0\_RTS\_PA4

| #define USART0\_RTS\_PA4   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x4) |
| --- |

## [◆ ](#a0f8ad339a81f02d95e747a82aefe699e)USART0\_RTS\_PA5

| #define USART0\_RTS\_PA5   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x5) |
| --- |

## [◆ ](#afcab39462b0cc95e3984b4a10e54b587)USART0\_RTS\_PA6

| #define USART0\_RTS\_PA6   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x6) |
| --- |

## [◆ ](#ae4f01f02accb203b696d25f69e4d1c2a)USART0\_RTS\_PA7

| #define USART0\_RTS\_PA7   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x7) |
| --- |

## [◆ ](#a3894dc798fe8561bba8836323f63aea4)USART0\_RTS\_PA8

| #define USART0\_RTS\_PA8   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x8) |
| --- |

## [◆ ](#a574cd147790bad9eb28767973741f066)USART0\_RTS\_PA9

| #define USART0\_RTS\_PA9   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x9) |
| --- |

## [◆ ](#a9808fc5b30607e6d0cbc3172369b818d)USART0\_RTS\_PB0

| #define USART0\_RTS\_PB0   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x1, 0x0) |
| --- |

## [◆ ](#a44240f09f67e09e58d28f82c43aff37d)USART0\_RTS\_PB1

| #define USART0\_RTS\_PB1   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x1, 0x1) |
| --- |

## [◆ ](#aa09ddd73916db94f88c710526689253d)USART0\_RTS\_PB2

| #define USART0\_RTS\_PB2   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x1, 0x2) |
| --- |

## [◆ ](#a7db53ff445baf566a0fcb7ce25532bb8)USART0\_RTS\_PB3

| #define USART0\_RTS\_PB3   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x1, 0x3) |
| --- |

## [◆ ](#ad1f91a8c2838f4b2f25240330b3144c3)USART0\_RTS\_PB4

| #define USART0\_RTS\_PB4   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x1, 0x4) |
| --- |

## [◆ ](#aebf7dec589dd49edacb06e3068c43289)USART0\_RTS\_PB5

| #define USART0\_RTS\_PB5   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x1, 0x5) |
| --- |

## [◆ ](#a2023f5afe82a2b2ff9b6c00bb249367b)USART0\_RTS\_PC0

| #define USART0\_RTS\_PC0   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x0) |
| --- |

## [◆ ](#a59cd7521827677160d85555c25430a9b)USART0\_RTS\_PC1

| #define USART0\_RTS\_PC1   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x1) |
| --- |

## [◆ ](#af7675ade342b55e04078f3d53306ca45)USART0\_RTS\_PC2

| #define USART0\_RTS\_PC2   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x2) |
| --- |

## [◆ ](#a42798ba22452bc2850007c9871d9daee)USART0\_RTS\_PC3

| #define USART0\_RTS\_PC3   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x3) |
| --- |

## [◆ ](#ae54415286b298aceaebdddcb3d008f5b)USART0\_RTS\_PC4

| #define USART0\_RTS\_PC4   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x4) |
| --- |

## [◆ ](#a6490fddb874c99a2cc293342c1b58dfc)USART0\_RTS\_PC5

| #define USART0\_RTS\_PC5   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x5) |
| --- |

## [◆ ](#ac72929dbdc13592ff0c46515bfc9169b)USART0\_RTS\_PC6

| #define USART0\_RTS\_PC6   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x6) |
| --- |

## [◆ ](#a88f8735b06c99e4851ee982a6ced5412)USART0\_RTS\_PC7

| #define USART0\_RTS\_PC7   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x7) |
| --- |

## [◆ ](#a6df814f12464adac6f44d998150dee99)USART0\_RTS\_PC8

| #define USART0\_RTS\_PC8   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x8) |
| --- |

## [◆ ](#a82db1fdbd8a2f9a418d28c87867342d3)USART0\_RTS\_PC9

| #define USART0\_RTS\_PC9   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x9) |
| --- |

## [◆ ](#a705598d6a60acd8936d6b7d0aa18cba2)USART0\_RTS\_PD0

| #define USART0\_RTS\_PD0   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x3, 0x0) |
| --- |

## [◆ ](#af77229ee4cf9eac56cc2fb134bc805c4)USART0\_RTS\_PD1

| #define USART0\_RTS\_PD1   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x3, 0x1) |
| --- |

## [◆ ](#a6a6bf570ad629ce3c81b37d31ffa2efe)USART0\_RTS\_PD2

| #define USART0\_RTS\_PD2   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x3, 0x2) |
| --- |

## [◆ ](#a0f8639b93ef710b631309b9388fbcb50)USART0\_RTS\_PD3

| #define USART0\_RTS\_PD3   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x3, 0x3) |
| --- |

## [◆ ](#ad9efbfbd3c62b51abf94fbbb8d9a493a)USART0\_RTS\_PD4

| #define USART0\_RTS\_PD4   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x3, 0x4) |
| --- |

## [◆ ](#af1677dba75a6a276fd2bba61dff06b78)USART0\_RTS\_PD5

| #define USART0\_RTS\_PD5   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x3, 0x5) |
| --- |

## [◆ ](#aacdc76948ed8f1e54f8e260e62c89f61)USART0\_RX\_PA0

| #define USART0\_RX\_PA0   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x0) |
| --- |

## [◆ ](#af41b4722d7b89c28645c24ac8e9a5eb4)USART0\_RX\_PA1

| #define USART0\_RX\_PA1   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x1) |
| --- |

## [◆ ](#a4da72ddcfaf102aa817eb2bc6e0c5cbb)USART0\_RX\_PA2

| #define USART0\_RX\_PA2   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x2) |
| --- |

## [◆ ](#a0a9b80333130d05d11bf88c78434221a)USART0\_RX\_PA3

| #define USART0\_RX\_PA3   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x3) |
| --- |

## [◆ ](#ac992577a6d9d5e0730eaaaa2086d5802)USART0\_RX\_PA4

| #define USART0\_RX\_PA4   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x4) |
| --- |

## [◆ ](#a8203de9111610660eea0c49ef51a9f6a)USART0\_RX\_PA5

| #define USART0\_RX\_PA5   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x5) |
| --- |

## [◆ ](#a84a42fda6d1b7a2269c357e2929b8219)USART0\_RX\_PA6

| #define USART0\_RX\_PA6   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x6) |
| --- |

## [◆ ](#a2f2a30bbb2a5b9e4d99ffb78545bbf3b)USART0\_RX\_PA7

| #define USART0\_RX\_PA7   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x7) |
| --- |

## [◆ ](#af982046455e2567919abe51956e83c10)USART0\_RX\_PA8

| #define USART0\_RX\_PA8   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x8) |
| --- |

## [◆ ](#a368a626b18b5d68929a859d06fbf673b)USART0\_RX\_PA9

| #define USART0\_RX\_PA9   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x9) |
| --- |

## [◆ ](#ab6691b3280f611c94c8690302bce85d5)USART0\_RX\_PB0

| #define USART0\_RX\_PB0   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x1, 0x0) |
| --- |

## [◆ ](#ab23c92ad1cb6a8cafe055baade2e8b87)USART0\_RX\_PB1

| #define USART0\_RX\_PB1   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x1, 0x1) |
| --- |

## [◆ ](#ace83f4be0c630151d9e59c4c21a40109)USART0\_RX\_PB2

| #define USART0\_RX\_PB2   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x1, 0x2) |
| --- |

## [◆ ](#ad2268a788d647414dd9ef5dba5bbed19)USART0\_RX\_PB3

| #define USART0\_RX\_PB3   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x1, 0x3) |
| --- |

## [◆ ](#ab17af03ccdc989dd4c8e28173d1a3b39)USART0\_RX\_PB4

| #define USART0\_RX\_PB4   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x1, 0x4) |
| --- |

## [◆ ](#a0a597070bf11931433fef8ae1e90b632)USART0\_RX\_PB5

| #define USART0\_RX\_PB5   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x1, 0x5) |
| --- |

## [◆ ](#aee4369f8682feee79f184c83d80274da)USART0\_RX\_PC0

| #define USART0\_RX\_PC0   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x0) |
| --- |

## [◆ ](#a9350586833a3d5c48baefd1610c13f62)USART0\_RX\_PC1

| #define USART0\_RX\_PC1   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x1) |
| --- |

## [◆ ](#a0a895e2c1e4a38b1fe6ebd5da7d525e5)USART0\_RX\_PC2

| #define USART0\_RX\_PC2   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x2) |
| --- |

## [◆ ](#a437d4a2cea5c64fc92b6c99b87bf5e8c)USART0\_RX\_PC3

| #define USART0\_RX\_PC3   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x3) |
| --- |

## [◆ ](#a75a6d4f4d7656eea8244bfb0d030ca79)USART0\_RX\_PC4

| #define USART0\_RX\_PC4   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x4) |
| --- |

## [◆ ](#a869fb6d64ec0e62beecb34dd0279f202)USART0\_RX\_PC5

| #define USART0\_RX\_PC5   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x5) |
| --- |

## [◆ ](#ad6902172e17c7f2c920e4658151182cd)USART0\_RX\_PC6

| #define USART0\_RX\_PC6   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x6) |
| --- |

## [◆ ](#ab5f98edf5748c59adffddbe6c3e032d6)USART0\_RX\_PC7

| #define USART0\_RX\_PC7   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x7) |
| --- |

## [◆ ](#ad5357505fc27282348572e648fe427c6)USART0\_RX\_PC8

| #define USART0\_RX\_PC8   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x8) |
| --- |

## [◆ ](#af0db0630d2887cafe0a0711b4d785da5)USART0\_RX\_PC9

| #define USART0\_RX\_PC9   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x9) |
| --- |

## [◆ ](#a823861421794933ab4e682de63e49cc4)USART0\_RX\_PD0

| #define USART0\_RX\_PD0   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x3, 0x0) |
| --- |

## [◆ ](#a408c8b04c4e9598c9bb139446244810f)USART0\_RX\_PD1

| #define USART0\_RX\_PD1   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x3, 0x1) |
| --- |

## [◆ ](#ad11874063a494e22191887fbd29d0189)USART0\_RX\_PD2

| #define USART0\_RX\_PD2   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x3, 0x2) |
| --- |

## [◆ ](#a0dbbdc55667cd4c32262a7e91298cf95)USART0\_RX\_PD3

| #define USART0\_RX\_PD3   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x3, 0x3) |
| --- |

## [◆ ](#a95c9f4c6e85f0d9cf050e7554cc41074)USART0\_RX\_PD4

| #define USART0\_RX\_PD4   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x3, 0x4) |
| --- |

## [◆ ](#ad4351007ac9fac08290be8409e28474a)USART0\_RX\_PD5

| #define USART0\_RX\_PD5   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x3, 0x5) |
| --- |

## [◆ ](#a4691259ca7c910831f70cff06b9737ac)USART0\_TX\_PA0

| #define USART0\_TX\_PA0   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x0) |
| --- |

## [◆ ](#af4e1c897ae049a4b223e09ab587f116d)USART0\_TX\_PA1

| #define USART0\_TX\_PA1   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x1) |
| --- |

## [◆ ](#acc13e25bcc1953b93e76521966cd1b39)USART0\_TX\_PA2

| #define USART0\_TX\_PA2   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x2) |
| --- |

## [◆ ](#a2ccdea01de2b8da884a33ddc1a81982f)USART0\_TX\_PA3

| #define USART0\_TX\_PA3   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x3) |
| --- |

## [◆ ](#a28450d0bc2dcbe2ead4d36cf3800eb03)USART0\_TX\_PA4

| #define USART0\_TX\_PA4   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x4) |
| --- |

## [◆ ](#ab3851360e615c31434f53597b8012217)USART0\_TX\_PA5

| #define USART0\_TX\_PA5   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x5) |
| --- |

## [◆ ](#a50d32b162eb8cfaee3228b4dd1aa2aef)USART0\_TX\_PA6

| #define USART0\_TX\_PA6   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x6) |
| --- |

## [◆ ](#a237580d1c4d056bd0008418d21d8f1b3)USART0\_TX\_PA7

| #define USART0\_TX\_PA7   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x7) |
| --- |

## [◆ ](#ae63baa716abe02654ea80133e8c84bd9)USART0\_TX\_PA8

| #define USART0\_TX\_PA8   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x8) |
| --- |

## [◆ ](#a30e713d1552e2b140c92493463890e81)USART0\_TX\_PA9

| #define USART0\_TX\_PA9   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x9) |
| --- |

## [◆ ](#a7af0455dce2acd605ef61cdc726c3177)USART0\_TX\_PB0

| #define USART0\_TX\_PB0   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x1, 0x0) |
| --- |

## [◆ ](#a6ccc48b5e17aca0e2aefe341f9519ae9)USART0\_TX\_PB1

| #define USART0\_TX\_PB1   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x1, 0x1) |
| --- |

## [◆ ](#a76f27605a95ea657c40e6911019756ec)USART0\_TX\_PB2

| #define USART0\_TX\_PB2   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x1, 0x2) |
| --- |

## [◆ ](#a820d4c384913206beec9312430e68f9a)USART0\_TX\_PB3

| #define USART0\_TX\_PB3   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x1, 0x3) |
| --- |

## [◆ ](#a3e2d2b7e3a0f2da1fd63cab3943aec5e)USART0\_TX\_PB4

| #define USART0\_TX\_PB4   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x1, 0x4) |
| --- |

## [◆ ](#a633c75e84a048f8db768fde374cb2d0e)USART0\_TX\_PB5

| #define USART0\_TX\_PB5   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x1, 0x5) |
| --- |

## [◆ ](#a63c1a984a64cb3c40643a7e38c20caaa)USART0\_TX\_PC0

| #define USART0\_TX\_PC0   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x0) |
| --- |

## [◆ ](#ac501027215a6551a637bacf8d1d406fa)USART0\_TX\_PC1

| #define USART0\_TX\_PC1   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x1) |
| --- |

## [◆ ](#ac1b7aad7c958ba2d2cfa2622318ac3c2)USART0\_TX\_PC2

| #define USART0\_TX\_PC2   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x2) |
| --- |

## [◆ ](#aa215f604dc67f092f495c472de9a7ed5)USART0\_TX\_PC3

| #define USART0\_TX\_PC3   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x3) |
| --- |

## [◆ ](#a1d49c843687f02f806c122059ac08a0c)USART0\_TX\_PC4

| #define USART0\_TX\_PC4   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x4) |
| --- |

## [◆ ](#a03580c3dc9b22d031f78a0a3051b25de)USART0\_TX\_PC5

| #define USART0\_TX\_PC5   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x5) |
| --- |

## [◆ ](#a3dc09745738d16673493a74870e6df5b)USART0\_TX\_PC6

| #define USART0\_TX\_PC6   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x6) |
| --- |

## [◆ ](#a9c846b6972a8263d37ea9473b022f2dc)USART0\_TX\_PC7

| #define USART0\_TX\_PC7   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x7) |
| --- |

## [◆ ](#a084114632892592ef47b04aa10862bc2)USART0\_TX\_PC8

| #define USART0\_TX\_PC8   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x8) |
| --- |

## [◆ ](#a9ed42a0cb76a787a142496cd670aba2e)USART0\_TX\_PC9

| #define USART0\_TX\_PC9   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x9) |
| --- |

## [◆ ](#a6756b78da6f6228f331b11a1a17be09d)USART0\_TX\_PD0

| #define USART0\_TX\_PD0   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x3, 0x0) |
| --- |

## [◆ ](#a1a2e17d5a9daefa68e67b96957271b67)USART0\_TX\_PD1

| #define USART0\_TX\_PD1   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x3, 0x1) |
| --- |

## [◆ ](#af52dcac08d3d9e0757048dbe7e0394b2)USART0\_TX\_PD2

| #define USART0\_TX\_PD2   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x3, 0x2) |
| --- |

## [◆ ](#a51ef7d6af85db7597dd27a68c75fe4e9)USART0\_TX\_PD3

| #define USART0\_TX\_PD3   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x3, 0x3) |
| --- |

## [◆ ](#a1d3a6020b34c9e101d510678ba45e28a)USART0\_TX\_PD4

| #define USART0\_TX\_PD4   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x3, 0x4) |
| --- |

## [◆ ](#a23b627f9a203d88710c72107e3945349)USART0\_TX\_PD5

| #define USART0\_TX\_PD5   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x3, 0x5) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [silabs](dir_fa47ec1716313d52a64832478c9daea4.md)
- [xg24-pinctrl.h](xg24-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
