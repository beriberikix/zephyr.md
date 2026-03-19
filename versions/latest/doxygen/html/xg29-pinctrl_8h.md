---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/xg29-pinctrl_8h.html
original_path: doxygen/html/xg29-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

xg29-pinctrl.h File Reference

`#include <[dt-bindings/pinctrl/silabs-pinctrl-dbus.h](silabs-pinctrl-dbus_8h_source.md)>`

[Go to the source code of this file.](xg29-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(port, pin) |
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
| #define | [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(port, pin) |
| #define | [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(port, pin) |
| #define | [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(port, pin) |
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
| #define | [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(port, pin) |
| #define | [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(port, pin) |
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
| #define | [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(port, pin) |
| #define | [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(port, pin) |
| #define | [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(port, pin) |
| #define | [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(port, pin) |
| #define | [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(port, pin) |
| #define | [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(port, pin) |
| #define | [ACMP0\_ACMPOUT\_PA0](#aedfa1c8d8e52b69e24b4c5ae55906dc6)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x0) |
| #define | [ACMP0\_ACMPOUT\_PA1](#afc43fb1cb74d95db1aceffc3b55fe017)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x1) |
| #define | [ACMP0\_ACMPOUT\_PA2](#ad609c06187830519865e977ad663e8a9)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x2) |
| #define | [ACMP0\_ACMPOUT\_PA3](#ab46e5bad6ae8864f903d86d60c3b08b2)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x3) |
| #define | [ACMP0\_ACMPOUT\_PA4](#acb82f83c6665cac86a44ffb88689e1f8)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x4) |
| #define | [ACMP0\_ACMPOUT\_PA5](#ae3d76d092e7875eac30dbc243b3ded51)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x5) |
| #define | [ACMP0\_ACMPOUT\_PA6](#a83b7f7e01fea7985ff1b739474e57015)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x6) |
| #define | [ACMP0\_ACMPOUT\_PA7](#ae42719fd5ec147180ae465dd40175867)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x7) |
| #define | [ACMP0\_ACMPOUT\_PA8](#a2e14f2d26d737657b252e5c6764d28af)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x0, 0x8) |
| #define | [ACMP0\_ACMPOUT\_PB0](#a36b9f71114e84ffb46fc8d52b7a87046)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x1, 0x0) |
| #define | [ACMP0\_ACMPOUT\_PB1](#ad7205c69934692bea6a1c31e9b374eef)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x1, 0x1) |
| #define | [ACMP0\_ACMPOUT\_PB2](#a17952d489dca95115341cf1052e9dc40)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x1, 0x2) |
| #define | [ACMP0\_ACMPOUT\_PB3](#a7455d069c13e82b9ef92b9cf82d4528a)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x1, 0x3) |
| #define | [ACMP0\_ACMPOUT\_PB4](#a9c5d85ede4da946e89f0a28bd78ce723)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x1, 0x4) |
| #define | [ACMP0\_ACMPOUT\_PC0](#a5b32e3f7e8bfdc37a87a1e5400897df8)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x0) |
| #define | [ACMP0\_ACMPOUT\_PC1](#a8c6a859a56f83fe76898e7e5d251d0b3)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x1) |
| #define | [ACMP0\_ACMPOUT\_PC2](#abc756f46419f529864d1f5373df967fa)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x2) |
| #define | [ACMP0\_ACMPOUT\_PC3](#acf2975d5be55d86f12c69c12dd257c02)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x3) |
| #define | [ACMP0\_ACMPOUT\_PC4](#a3e87af3956c8d9b54f210c3c9ce25fe2)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x4) |
| #define | [ACMP0\_ACMPOUT\_PC5](#a02cb0bfeb435f2d76adf0624c9acc380)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x5) |
| #define | [ACMP0\_ACMPOUT\_PC6](#a38b79026393006be7b6e6f57e90f194c)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x6) |
| #define | [ACMP0\_ACMPOUT\_PC7](#a8d166fe3ba9340f393a6f43167c70d1f)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x2, 0x7) |
| #define | [ACMP0\_ACMPOUT\_PD0](#a196c859ab39c4e7fea903085f0091f38)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x3, 0x0) |
| #define | [ACMP0\_ACMPOUT\_PD1](#aabae5292f25eac5b7f235c1613a4abfe)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x3, 0x1) |
| #define | [ACMP0\_ACMPOUT\_PD2](#af0c00ac6edb9696207c0688dd902889c)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x3, 0x2) |
| #define | [ACMP0\_ACMPOUT\_PD3](#a22cc57aac83e922695ce9765daca5a22)   [SILABS\_DBUS\_ACMP0\_ACMPOUT](#a1f03fc6bcf9a20f2f39b4d91cf302d63)(0x3, 0x3) |
| #define | [CMU\_CLKOUT0\_PC0](#a750738e1a4c7ed8bfb4d2f9151267da6)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x0) |
| #define | [CMU\_CLKOUT0\_PC1](#a31916418c44431216dea609cb5aef35a)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x1) |
| #define | [CMU\_CLKOUT0\_PC2](#a90c69d0d98a225b058598397e960c41d)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x2) |
| #define | [CMU\_CLKOUT0\_PC3](#a502a3e471c068d2ae94fc2255b3680dd)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x3) |
| #define | [CMU\_CLKOUT0\_PC4](#a0af75594d7d55c0bf77021f81b058ef6)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x4) |
| #define | [CMU\_CLKOUT0\_PC5](#a3bfddaaeba9558824977b108319c26b1)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x5) |
| #define | [CMU\_CLKOUT0\_PC6](#a7c63df02e41810547afb13b879dbf602)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x6) |
| #define | [CMU\_CLKOUT0\_PC7](#aa219ec0869e6e96ce5a84ed7dbba3d06)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x2, 0x7) |
| #define | [CMU\_CLKOUT0\_PD0](#a1afed05e5d9d89ad251e77f94f1e745d)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x3, 0x0) |
| #define | [CMU\_CLKOUT0\_PD1](#a4cc3f9b8c22e11a9ffd40149c990d09d)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x3, 0x1) |
| #define | [CMU\_CLKOUT0\_PD2](#a823b6e29d70a1313ed81cae432648f73)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x3, 0x2) |
| #define | [CMU\_CLKOUT0\_PD3](#a4223cab1734f1dadac546c956ae17f66)   [SILABS\_DBUS\_CMU\_CLKOUT0](#a6d193d353f76cad0e7da5c584625e996)(0x3, 0x3) |
| #define | [CMU\_CLKOUT1\_PC0](#a7b57f126203047b4cb82d0eff5c1ba8f)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x0) |
| #define | [CMU\_CLKOUT1\_PC1](#a7742937a9e0afe5ae4859f9fe6373ca3)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x1) |
| #define | [CMU\_CLKOUT1\_PC2](#ae634d0e26da5dd095bf98854cd95e6c9)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x2) |
| #define | [CMU\_CLKOUT1\_PC3](#afecc3d613acceb752470037c6c253759)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x3) |
| #define | [CMU\_CLKOUT1\_PC4](#a2d21eabc4603c5cfd93cd0eed5708565)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x4) |
| #define | [CMU\_CLKOUT1\_PC5](#a8287c02ea2823803c7f3415597aeb0f8)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x5) |
| #define | [CMU\_CLKOUT1\_PC6](#aed9fe929699b234ddcd9c5d814d309fc)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x6) |
| #define | [CMU\_CLKOUT1\_PC7](#af72caa6a5612d497402a76ac0d5e2d12)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x2, 0x7) |
| #define | [CMU\_CLKOUT1\_PD0](#a9041e78bd2f530d25db4d36d783e04ff)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x3, 0x0) |
| #define | [CMU\_CLKOUT1\_PD1](#a65ab333bdb97055f6e69f17a46cc76ca)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x3, 0x1) |
| #define | [CMU\_CLKOUT1\_PD2](#ad6f97e49e9ed6808c2631547fae12fd0)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x3, 0x2) |
| #define | [CMU\_CLKOUT1\_PD3](#afc01df4895e8d3e104bbff29227824a8)   [SILABS\_DBUS\_CMU\_CLKOUT1](#a3f7ded37227446a05137a47c9a466894)(0x3, 0x3) |
| #define | [CMU\_CLKOUT2\_PA0](#a515401133e23f38d0c7babc3b8cffb18)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x0) |
| #define | [CMU\_CLKOUT2\_PA1](#ae765fe590bab12a1671c57b20b69e354)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x1) |
| #define | [CMU\_CLKOUT2\_PA2](#a4183040a304b3d85d3b382d28176da03)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x2) |
| #define | [CMU\_CLKOUT2\_PA3](#a65e82802fc3e2e3eb089eaa3bb4b1207)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x3) |
| #define | [CMU\_CLKOUT2\_PA4](#a9345663284354ee2c4b5ebd6a4124234)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x4) |
| #define | [CMU\_CLKOUT2\_PA5](#ac1767819afb4418dfb8de4ec2114144f)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x5) |
| #define | [CMU\_CLKOUT2\_PA6](#a078e7abf21f63f21617ea47fd565fcc0)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x6) |
| #define | [CMU\_CLKOUT2\_PA7](#a0ad411783ff7e13b2965931269fc8c8b)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x7) |
| #define | [CMU\_CLKOUT2\_PA8](#a0ea1041e58653ac225cacb25cd747970)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x0, 0x8) |
| #define | [CMU\_CLKOUT2\_PB0](#a7f82072ef8014d5497df30c927b0d6f9)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x1, 0x0) |
| #define | [CMU\_CLKOUT2\_PB1](#af815e3c4392ba1686e4f77dc0b6911f1)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x1, 0x1) |
| #define | [CMU\_CLKOUT2\_PB2](#a9613c5b45ba73bc69011086baafad84c)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x1, 0x2) |
| #define | [CMU\_CLKOUT2\_PB3](#ac8e00ea8020085f156d66e741d7fa185)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x1, 0x3) |
| #define | [CMU\_CLKOUT2\_PB4](#a003c45e0a49fdb695df7d930f16ff20b)   [SILABS\_DBUS\_CMU\_CLKOUT2](#a67d6fb886df9d589e447bd9332252d62)(0x1, 0x4) |
| #define | [CMU\_CLKIN0\_PC0](#a4aaa42a036d18c3f1acb7def83fb9f05)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x0) |
| #define | [CMU\_CLKIN0\_PC1](#ad099af25ca0f801ff85e3071a1cda472)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x1) |
| #define | [CMU\_CLKIN0\_PC2](#add3b048d2455419255aedcef16aed776)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x2) |
| #define | [CMU\_CLKIN0\_PC3](#a59c6d813c66884cb9db67d4e6c1cd8d4)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x3) |
| #define | [CMU\_CLKIN0\_PC4](#a4528f4ea777e78b8f27bd604bfeaf59e)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x4) |
| #define | [CMU\_CLKIN0\_PC5](#a5f79eddd69ce5550c1fd8ee07ce0ad9c)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x5) |
| #define | [CMU\_CLKIN0\_PC6](#ab3ac5c61d6e2ba07c8d17e313ff61631)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x6) |
| #define | [CMU\_CLKIN0\_PC7](#a50bb44be738315ef4409c4310d93f7aa)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x2, 0x7) |
| #define | [CMU\_CLKIN0\_PD0](#a8d96e9e617c1f18f2bd0a2ac65e98ae1)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x3, 0x0) |
| #define | [CMU\_CLKIN0\_PD1](#aa780fb9850bc6efcb36d8dd19770ec27)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x3, 0x1) |
| #define | [CMU\_CLKIN0\_PD2](#ad27e93b39cdcd25b3d3ba89f01a05019)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x3, 0x2) |
| #define | [CMU\_CLKIN0\_PD3](#aec9648fbe6bece6f7cec5b3942eda3a0)   [SILABS\_DBUS\_CMU\_CLKIN0](#a19d73eca7da5c8b8622b3cb155ab4e6c)(0x3, 0x3) |
| #define | [EUSART0\_CS\_PA0](#a100647c82cfce4ed946cb9f18472af15)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x0) |
| #define | [EUSART0\_CS\_PA1](#aad3c475c7949c55fc7ac69dcb9e9dfe3)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x1) |
| #define | [EUSART0\_CS\_PA2](#a521ddcc2db980c3e31ddcb847980ca73)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x2) |
| #define | [EUSART0\_CS\_PA3](#aff497e4a1f5d0f650a1a75d995740e5f)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x3) |
| #define | [EUSART0\_CS\_PA4](#a852775bf4cc8faa4191b618c12690c07)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x4) |
| #define | [EUSART0\_CS\_PA5](#a494590522337ea1dc294d8e30bdce4a0)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x5) |
| #define | [EUSART0\_CS\_PA6](#a3324f29622d78fbdf0d6a3b7931fee92)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x6) |
| #define | [EUSART0\_CS\_PA7](#a0aff0e33c99569acdff8882c376ab733)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x7) |
| #define | [EUSART0\_CS\_PA8](#aecff621fa71796d796b02908db5f0305)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x0, 0x8) |
| #define | [EUSART0\_CS\_PB0](#a7ace842a3a572ea81be1245e0ed3da90)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x1, 0x0) |
| #define | [EUSART0\_CS\_PB1](#ad6557ba2b6c3d89732c097dc0c1df74b)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x1, 0x1) |
| #define | [EUSART0\_CS\_PB2](#ad601437b58f8f23ad6ad052ea9176547)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x1, 0x2) |
| #define | [EUSART0\_CS\_PB3](#a15627a1b7477e5079ebcdbf77e08283c)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x1, 0x3) |
| #define | [EUSART0\_CS\_PB4](#a94f843865ca0025d3436c71e86ef9c34)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x1, 0x4) |
| #define | [EUSART0\_CS\_PC0](#aed8fa49f3eb9671881b3991c01105ff6)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x2, 0x0) |
| #define | [EUSART0\_CS\_PC1](#accad121c30ac5b90f161ada15a181a0e)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x2, 0x1) |
| #define | [EUSART0\_CS\_PC2](#a038e1a231493a32b4dc8e1017045d4de)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x2, 0x2) |
| #define | [EUSART0\_CS\_PC3](#ab55727982406dae06bfc6d4817311e84)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x2, 0x3) |
| #define | [EUSART0\_CS\_PC4](#a9e313135bb2478404e9075aaa2e97365)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x2, 0x4) |
| #define | [EUSART0\_CS\_PC5](#ac9b7036e8e6aa9e910a6f9ff4ead91a8)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x2, 0x5) |
| #define | [EUSART0\_CS\_PC6](#a09261a943a59ec343e4c473518d9af71)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x2, 0x6) |
| #define | [EUSART0\_CS\_PC7](#ac9b0f742fed5deed319e3ced35da509f)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x2, 0x7) |
| #define | [EUSART0\_CS\_PD0](#a50f458970cc99a933780e51f340bbbfc)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x3, 0x0) |
| #define | [EUSART0\_CS\_PD1](#a614ddd72337ca49b570b01d97e02a5ab)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x3, 0x1) |
| #define | [EUSART0\_CS\_PD2](#afca145acee686cb673080d165608869c)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x3, 0x2) |
| #define | [EUSART0\_CS\_PD3](#a0fec9ee2f5eb601f7ecd07f427fe12d9)   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x3, 0x3) |
| #define | [EUSART0\_RTS\_PA0](#a4e8066ef85c98c6311cdff1ea85c0b0e)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x0) |
| #define | [EUSART0\_RTS\_PA1](#a8fb4dee00cdbb65ef6b771e1f6923333)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x1) |
| #define | [EUSART0\_RTS\_PA2](#af65566f1bbb87d7a789a558b7ba99905)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x2) |
| #define | [EUSART0\_RTS\_PA3](#a0cfcb844b17fb5054cdb97bd380d75c8)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x3) |
| #define | [EUSART0\_RTS\_PA4](#a1a144a6bd83a1872b99f6efadc3b9521)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x4) |
| #define | [EUSART0\_RTS\_PA5](#a870cd278a7c1a757f2189d07171b9f99)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x5) |
| #define | [EUSART0\_RTS\_PA6](#a579aa029440d7705d0648a7b0bacfcb3)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x6) |
| #define | [EUSART0\_RTS\_PA7](#adced5ad51aca90ec512b6206a83ad2cc)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x7) |
| #define | [EUSART0\_RTS\_PA8](#acd2ec0a2bbec98d10b7e30f0e576763c)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x0, 0x8) |
| #define | [EUSART0\_RTS\_PB0](#a4ceaf57a7bf9921f8095d32de5f0ab66)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x1, 0x0) |
| #define | [EUSART0\_RTS\_PB1](#a2249a367a7276af293997584be24dad2)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x1, 0x1) |
| #define | [EUSART0\_RTS\_PB2](#adf3dac7572179dcc0766f81f7bd648cf)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x1, 0x2) |
| #define | [EUSART0\_RTS\_PB3](#a04c83284f28797c089ca46d4a432e905)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x1, 0x3) |
| #define | [EUSART0\_RTS\_PB4](#a953d9ef327a7b0eb5dedd69eba7b0b9a)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x1, 0x4) |
| #define | [EUSART0\_RTS\_PC0](#a825eb0a0ddbb7153c0c0a358164e17cc)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x2, 0x0) |
| #define | [EUSART0\_RTS\_PC1](#a342ddc29fafafaa7cabf46579b9f2135)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x2, 0x1) |
| #define | [EUSART0\_RTS\_PC2](#a9de85c0cea5ad13eb9542be9f9c1fecd)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x2, 0x2) |
| #define | [EUSART0\_RTS\_PC3](#aba46cf1f481e82d8c36b2e3924d56299)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x2, 0x3) |
| #define | [EUSART0\_RTS\_PC4](#a94bf3eeaf8970ef628c827f6d5ad6deb)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x2, 0x4) |
| #define | [EUSART0\_RTS\_PC5](#a1a43b2077d6da1cabc7179ef9d21138c)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x2, 0x5) |
| #define | [EUSART0\_RTS\_PC6](#a7b8ffd905edd49f61c10820c23f90ca6)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x2, 0x6) |
| #define | [EUSART0\_RTS\_PC7](#ae46d3ff4e405d9e8d63ffefb26f7d8f8)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x2, 0x7) |
| #define | [EUSART0\_RTS\_PD0](#a88c2dfec826dfb5ad0be6b63132e345d)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x3, 0x0) |
| #define | [EUSART0\_RTS\_PD1](#a4774365c9a89e81f776bcb83f62f26d0)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x3, 0x1) |
| #define | [EUSART0\_RTS\_PD2](#a3943f055fa037d9020a3251972e3ccef)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x3, 0x2) |
| #define | [EUSART0\_RTS\_PD3](#ad9cd7fd50ce835c6384623b4cfd04c9f)   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x3, 0x3) |
| #define | [EUSART0\_RX\_PA0](#a2b46bf2b099bf87941bbd4c29b77fee8)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x0) |
| #define | [EUSART0\_RX\_PA1](#a22bfbf4a894d55b3c59983a0a60fdb00)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x1) |
| #define | [EUSART0\_RX\_PA2](#a529e5bbdda4e497f5a71a78dd2628c91)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x2) |
| #define | [EUSART0\_RX\_PA3](#a7ffae82c7d17cebc1d662a65b6d44a59)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x3) |
| #define | [EUSART0\_RX\_PA4](#afab762ebf79c6816237382f135e88820)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x4) |
| #define | [EUSART0\_RX\_PA5](#a346155c0747c9bbbdf254bbea5c37408)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x5) |
| #define | [EUSART0\_RX\_PA6](#a90cca23bf07a59ad80d47e3c52683224)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x6) |
| #define | [EUSART0\_RX\_PA7](#a5ef7abc333b9450ec72e144384a2369d)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x7) |
| #define | [EUSART0\_RX\_PA8](#a05989116473a2986fd70707a2a41c869)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x0, 0x8) |
| #define | [EUSART0\_RX\_PB0](#a1a59a7ed291e816ece0bc12cffd98f39)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x1, 0x0) |
| #define | [EUSART0\_RX\_PB1](#a1bb9368d71f3b8140274beed383a465f)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x1, 0x1) |
| #define | [EUSART0\_RX\_PB2](#ac684b9dbb5433cf963027fd3ab0cd1fb)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x1, 0x2) |
| #define | [EUSART0\_RX\_PB3](#afb6d2142c3766fdede31602e56e1281a)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x1, 0x3) |
| #define | [EUSART0\_RX\_PB4](#aa4cb55bd34f6f1ae67e46e0bbbfed055)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x1, 0x4) |
| #define | [EUSART0\_RX\_PC0](#ab43573513fde6a68d9914f6cc422664c)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x2, 0x0) |
| #define | [EUSART0\_RX\_PC1](#a397196ba429fc31426bb06135aad607d)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x2, 0x1) |
| #define | [EUSART0\_RX\_PC2](#a3958b897fce5b24aec711db28532c9b1)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x2, 0x2) |
| #define | [EUSART0\_RX\_PC3](#afd71895c0bb4699536f8b27207024444)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x2, 0x3) |
| #define | [EUSART0\_RX\_PC4](#a17a0b3453db06718a90764d1c98b3673)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x2, 0x4) |
| #define | [EUSART0\_RX\_PC5](#a0eba541db8e29efc4a9349d1d5fece98)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x2, 0x5) |
| #define | [EUSART0\_RX\_PC6](#ad14eee491ec56c41c6066a646152d19b)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x2, 0x6) |
| #define | [EUSART0\_RX\_PC7](#aa7040c8e3d027dc7def3b3a07306f9c8)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x2, 0x7) |
| #define | [EUSART0\_RX\_PD0](#a26f2a17606c1f10ad647e9d7be27f5fb)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x3, 0x0) |
| #define | [EUSART0\_RX\_PD1](#ad83e83b257b520defe2d667b70bb301b)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x3, 0x1) |
| #define | [EUSART0\_RX\_PD2](#a8da013cc702e3895b2eedc65fde8b4b0)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x3, 0x2) |
| #define | [EUSART0\_RX\_PD3](#ab5ec704003949c54b6f683e33d998f1a)   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x3, 0x3) |
| #define | [EUSART0\_SCLK\_PA0](#a0a19d2153b70b8ef0e074fb8daadba20)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x0) |
| #define | [EUSART0\_SCLK\_PA1](#aca8e4898f56d57aff5909b5e8f56eee0)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x1) |
| #define | [EUSART0\_SCLK\_PA2](#abbc7ccc93b8fe675a34aea51b63f52ef)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x2) |
| #define | [EUSART0\_SCLK\_PA3](#a08190aaeb8a375f69bc3af20b6cea6bf)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x3) |
| #define | [EUSART0\_SCLK\_PA4](#a4e49a5735fc4f636e31c770b01960242)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x4) |
| #define | [EUSART0\_SCLK\_PA5](#a5bb9d1463e97d8683ff98741b989f82c)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x5) |
| #define | [EUSART0\_SCLK\_PA6](#a2465c3c97ea670afb2f6e579ba7e2db3)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x6) |
| #define | [EUSART0\_SCLK\_PA7](#a038e6fb8ad493dee10235499595210d8)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x7) |
| #define | [EUSART0\_SCLK\_PA8](#aa5c4e4ec06af3d9212e1fc8200a28639)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x0, 0x8) |
| #define | [EUSART0\_SCLK\_PB0](#ad1159b33436207a1b896cd71f51730dd)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x1, 0x0) |
| #define | [EUSART0\_SCLK\_PB1](#a2253345ed59d0d340c7b077ae8d689b4)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x1, 0x1) |
| #define | [EUSART0\_SCLK\_PB2](#a1dbc32ec456a7c882c71dddf254dec53)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x1, 0x2) |
| #define | [EUSART0\_SCLK\_PB3](#a27cc8d09e0ca7ac92e6022ed35fc2549)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x1, 0x3) |
| #define | [EUSART0\_SCLK\_PB4](#aeb794afde863684b4166b657b797f837)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x1, 0x4) |
| #define | [EUSART0\_SCLK\_PC0](#a1078589030256c2dcfc07a08bbb87c4d)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x2, 0x0) |
| #define | [EUSART0\_SCLK\_PC1](#a5edbc59cef4a7d2e1410f02049149426)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x2, 0x1) |
| #define | [EUSART0\_SCLK\_PC2](#a452d7f6b0e64db7dfc5cc08b0c8d3d1b)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x2, 0x2) |
| #define | [EUSART0\_SCLK\_PC3](#a3d47bd24e5f3d57dad33b7de29db889e)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x2, 0x3) |
| #define | [EUSART0\_SCLK\_PC4](#a5c22d3590c171aae25635e62b43d1ad5)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x2, 0x4) |
| #define | [EUSART0\_SCLK\_PC5](#a50f069238ddce48a050dadd16dc2e08d)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x2, 0x5) |
| #define | [EUSART0\_SCLK\_PC6](#aeb6ec6c0706bdb69cc25f8bd54818b2a)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x2, 0x6) |
| #define | [EUSART0\_SCLK\_PC7](#ab3c184119f4bfa1ccf5669955fa3747d)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x2, 0x7) |
| #define | [EUSART0\_SCLK\_PD0](#ae02e824020415b9917f19a443a032894)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x3, 0x0) |
| #define | [EUSART0\_SCLK\_PD1](#a98983e81af06d6c1b2f7f00d951dfd4e)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x3, 0x1) |
| #define | [EUSART0\_SCLK\_PD2](#ad01090a81a9e2e2f7fc0aab98b981651)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x3, 0x2) |
| #define | [EUSART0\_SCLK\_PD3](#a4d0cdc0b2724c2d8bb9d5df172827617)   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x3, 0x3) |
| #define | [EUSART0\_TX\_PA0](#ad1d73b89a55be3c3b76309827c392e70)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x0) |
| #define | [EUSART0\_TX\_PA1](#a01b89a42fcc33bd36f8c419017a473ec)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x1) |
| #define | [EUSART0\_TX\_PA2](#a84c240d7825740c4b18aebe068e788d6)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x2) |
| #define | [EUSART0\_TX\_PA3](#aafac5282dba172a3e073c31d29085d10)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x3) |
| #define | [EUSART0\_TX\_PA4](#a7889459ce02255a24f9cc968c1bc0e1c)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x4) |
| #define | [EUSART0\_TX\_PA5](#ab2845f805e7c75787b24d924dcccfe68)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x5) |
| #define | [EUSART0\_TX\_PA6](#ab129226f0405530f5cd911cd423fc1b9)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x6) |
| #define | [EUSART0\_TX\_PA7](#a26eba150ba1aaf50e9a6059588aeaf1a)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x7) |
| #define | [EUSART0\_TX\_PA8](#a318a4670d6912095c2dba8c6dd8c9623)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x0, 0x8) |
| #define | [EUSART0\_TX\_PB0](#a8d6a3ec6a9d1076b9174a66023685407)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x1, 0x0) |
| #define | [EUSART0\_TX\_PB1](#a77c5c04618ba4ce29cb1ccdb0624bf36)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x1, 0x1) |
| #define | [EUSART0\_TX\_PB2](#a8ec4a7e6c0d3eb4d66b25495c4e339f5)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x1, 0x2) |
| #define | [EUSART0\_TX\_PB3](#a3c0337cddda08df662dae06438bb0330)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x1, 0x3) |
| #define | [EUSART0\_TX\_PB4](#aede0d7fee53f6b2f345752bf9fdba30c)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x1, 0x4) |
| #define | [EUSART0\_TX\_PC0](#af63c951ca47dcda1de1deadf0916395a)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x2, 0x0) |
| #define | [EUSART0\_TX\_PC1](#a1f1dd917913a93cea9c4f4a30e188289)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x2, 0x1) |
| #define | [EUSART0\_TX\_PC2](#a2b10800da7ec93c986d863e4a316aa9b)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x2, 0x2) |
| #define | [EUSART0\_TX\_PC3](#a3520e59def513d6fffa9f38f207570b6)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x2, 0x3) |
| #define | [EUSART0\_TX\_PC4](#a49af2dadf031ad5deccf82a39c9f4e9c)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x2, 0x4) |
| #define | [EUSART0\_TX\_PC5](#ae2f02d0b2116fa3be868195f7f7f8a55)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x2, 0x5) |
| #define | [EUSART0\_TX\_PC6](#ad18f194c3eb96f83768617c98fe16069)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x2, 0x6) |
| #define | [EUSART0\_TX\_PC7](#aaa9ef38e04a4756ee56412e21933046d)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x2, 0x7) |
| #define | [EUSART0\_TX\_PD0](#ad274833f35683527ee3e9ad95ad1409b)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x3, 0x0) |
| #define | [EUSART0\_TX\_PD1](#af0b2b96f98ec0b156ed55e3a0df7bf49)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x3, 0x1) |
| #define | [EUSART0\_TX\_PD2](#a1ff0c2f5cf0037337bc748f19f8c2755)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x3, 0x2) |
| #define | [EUSART0\_TX\_PD3](#a651410e3284f3a14c116fc89304ab848)   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x3, 0x3) |
| #define | [EUSART0\_CTS\_PA0](#aa78640d4f3389404bbe47f35bbb1c02a)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x0) |
| #define | [EUSART0\_CTS\_PA1](#a43cbc88ff21700a62c42b35e8f67c0b1)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x1) |
| #define | [EUSART0\_CTS\_PA2](#a9e7c4aa3a487cbfa8019667b06e01ed9)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x2) |
| #define | [EUSART0\_CTS\_PA3](#a200ad378e054581fc0af32901db945d9)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x3) |
| #define | [EUSART0\_CTS\_PA4](#aba12ae15b468c70e21089ddbb4228bb2)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x4) |
| #define | [EUSART0\_CTS\_PA5](#a3eefe0f1fcafd901fc9ab7d90d57f5ce)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x5) |
| #define | [EUSART0\_CTS\_PA6](#a1f097826e960d3358db147f4a324ee49)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x6) |
| #define | [EUSART0\_CTS\_PA7](#a9d74f4aa54f500f1ff4839eaf1f29b3f)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x7) |
| #define | [EUSART0\_CTS\_PA8](#af31e2b373140e3eb7f01b90067847104)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x0, 0x8) |
| #define | [EUSART0\_CTS\_PB0](#ae41b867ca4046c838fa20049b685de44)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x1, 0x0) |
| #define | [EUSART0\_CTS\_PB1](#a06e7277edcf4f30266d9dc9b9bcddb9d)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x1, 0x1) |
| #define | [EUSART0\_CTS\_PB2](#a7908f6ee431528d7c4d4345b78c0c0c1)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x1, 0x2) |
| #define | [EUSART0\_CTS\_PB3](#a453f6ccc79c1145a755f667f0d716364)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x1, 0x3) |
| #define | [EUSART0\_CTS\_PB4](#a292c1725298cb2fe05ccf9c610c9a971)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x1, 0x4) |
| #define | [EUSART0\_CTS\_PC0](#a12f93c05aa8eee84560122e11433dff9)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x2, 0x0) |
| #define | [EUSART0\_CTS\_PC1](#aa96ca5ef6f6b4221e0e8cdaacc2c0419)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x2, 0x1) |
| #define | [EUSART0\_CTS\_PC2](#ab65aef137530bff24284785786a11413)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x2, 0x2) |
| #define | [EUSART0\_CTS\_PC3](#a0a8251ba020c3db8eefff12e4b1ee723)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x2, 0x3) |
| #define | [EUSART0\_CTS\_PC4](#aa99f745ad1eee19ed42ea9c6f18d8b1f)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x2, 0x4) |
| #define | [EUSART0\_CTS\_PC5](#ab63fbab0b6b7f355a44ff32d7adae7e8)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x2, 0x5) |
| #define | [EUSART0\_CTS\_PC6](#a641ac3b8b404f53c7303bac894ab0d7e)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x2, 0x6) |
| #define | [EUSART0\_CTS\_PC7](#aeecf8c0a1903f81003f57a099ab5ec68)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x2, 0x7) |
| #define | [EUSART0\_CTS\_PD0](#a4c8975cd656f4a945f94d313c1ed0631)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x3, 0x0) |
| #define | [EUSART0\_CTS\_PD1](#a24e996e1a6a4f04276ac94d2218921bd)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x3, 0x1) |
| #define | [EUSART0\_CTS\_PD2](#af00a1053965630bc5be8aff8a7663b81)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x3, 0x2) |
| #define | [EUSART0\_CTS\_PD3](#ab94c51b8230e3b650af4433bf444ff5b)   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x3, 0x3) |
| #define | [EUSART1\_CS\_PA0](#a40f82c8c64899e7d6814527efbbebe93)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x0) |
| #define | [EUSART1\_CS\_PA1](#af63951a9525443f244715b5a955c6653)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x1) |
| #define | [EUSART1\_CS\_PA2](#a888362b3adc4669f5a60462d0ae73334)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x2) |
| #define | [EUSART1\_CS\_PA3](#accc804e7c4664309a021a7a8c591af6c)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x3) |
| #define | [EUSART1\_CS\_PA4](#a770e6e5582d1e29c8b23a90628b3e57c)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x4) |
| #define | [EUSART1\_CS\_PA5](#ae3ef936bb7be77cfdce700627f231ec7)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x5) |
| #define | [EUSART1\_CS\_PA6](#a4a45381fe7d897de6e53043fb47ef13e)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x6) |
| #define | [EUSART1\_CS\_PA7](#a637c7be3f82194e942972cde56bbb686)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x7) |
| #define | [EUSART1\_CS\_PA8](#a3f561023c637eba25ac1d46c36e20a80)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x0, 0x8) |
| #define | [EUSART1\_CS\_PB0](#acdbe2339b99a4fe502bba246a626d5c2)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x1, 0x0) |
| #define | [EUSART1\_CS\_PB1](#a7f14f23f53baa612f22609dea451f445)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x1, 0x1) |
| #define | [EUSART1\_CS\_PB2](#a619bea931dfb9441abd013c5f3f70be7)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x1, 0x2) |
| #define | [EUSART1\_CS\_PB3](#a620516494e3be49f80bb70a9c0da28ac)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x1, 0x3) |
| #define | [EUSART1\_CS\_PB4](#afd07cc566c75f403760a1754ec784e92)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x1, 0x4) |
| #define | [EUSART1\_CS\_PC0](#a015e088a759762fcf0c47c9b4033b66c)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x0) |
| #define | [EUSART1\_CS\_PC1](#a176087a622c1e9f7bf968bd59381691b)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x1) |
| #define | [EUSART1\_CS\_PC2](#a6c4faf990cacd9a0d8e17c2aa23ed236)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x2) |
| #define | [EUSART1\_CS\_PC3](#a63386d40b9a59051bb744d043b2cce5c)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x3) |
| #define | [EUSART1\_CS\_PC4](#aa8a89563cdaff202bd581204799e6454)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x4) |
| #define | [EUSART1\_CS\_PC5](#a101b25d7d37e7b9fca411811df2662a9)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x5) |
| #define | [EUSART1\_CS\_PC6](#a55c0377bef97b860796d28a5257b04e6)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x6) |
| #define | [EUSART1\_CS\_PC7](#a847321a3e9924fb48574629393a9e777)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x2, 0x7) |
| #define | [EUSART1\_CS\_PD0](#abaf2f2d1169cde30d7cc29eb843f5ed8)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x3, 0x0) |
| #define | [EUSART1\_CS\_PD1](#aa4b4634c5f80cdd71c0b806ffc72df65)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x3, 0x1) |
| #define | [EUSART1\_CS\_PD2](#af38ecf13151c02150a2313cd3b9ddf7f)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x3, 0x2) |
| #define | [EUSART1\_CS\_PD3](#a8b9a6da38263a9cd3585a3bee8ae937d)   [SILABS\_DBUS\_EUSART1\_CS](#ac3e145872ad81776dafad7dd8145f9b1)(0x3, 0x3) |
| #define | [EUSART1\_RTS\_PA0](#abc1f657ca7df682bd31439ae830e1c6b)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x0) |
| #define | [EUSART1\_RTS\_PA1](#ae0269aec4dd2413b32ed157eeec8e810)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x1) |
| #define | [EUSART1\_RTS\_PA2](#a562cacf73b6eca2f6feffb7e494ec806)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x2) |
| #define | [EUSART1\_RTS\_PA3](#ac832d962a34bd67b3d6874629191f3d8)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x3) |
| #define | [EUSART1\_RTS\_PA4](#a59c071c3b6b1940bfc67b537be8f9d03)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x4) |
| #define | [EUSART1\_RTS\_PA5](#a60a05e2ee467a334f4acba3032724efd)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x5) |
| #define | [EUSART1\_RTS\_PA6](#a9070e646c606ad24ea2a49024e93d2ec)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x6) |
| #define | [EUSART1\_RTS\_PA7](#ab692bb94e9ffe0930767caeae52a1bc9)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x7) |
| #define | [EUSART1\_RTS\_PA8](#a4eac1cef4c4df24f56c4422ff00e540b)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x0, 0x8) |
| #define | [EUSART1\_RTS\_PB0](#a7b73f6a89a0a8707e7d3caf7c9e1bfcf)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x1, 0x0) |
| #define | [EUSART1\_RTS\_PB1](#a3ee5218e6cd62cf429ed39483dad68b0)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x1, 0x1) |
| #define | [EUSART1\_RTS\_PB2](#ad6a72d46a8632364b669d57f425c97b7)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x1, 0x2) |
| #define | [EUSART1\_RTS\_PB3](#ad964d10c49afb6b27ccff6537e1f92e8)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x1, 0x3) |
| #define | [EUSART1\_RTS\_PB4](#af1faa3155f2eb599cb02114bf58484b0)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x1, 0x4) |
| #define | [EUSART1\_RTS\_PC0](#acc9df99d6f67349407eab1963962329a)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x0) |
| #define | [EUSART1\_RTS\_PC1](#aa65ef7ad286ee25997d57b0c94cdcecb)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x1) |
| #define | [EUSART1\_RTS\_PC2](#a45dd8df05c9c5cfc7aa94ed8591eabe8)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x2) |
| #define | [EUSART1\_RTS\_PC3](#a38af1c47914e8c7a0823ceb0ccb25e6e)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x3) |
| #define | [EUSART1\_RTS\_PC4](#a6bc896f9f3261271d490611c1379db44)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x4) |
| #define | [EUSART1\_RTS\_PC5](#a7a5842461fe1b84f540380ec07e1822d)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x5) |
| #define | [EUSART1\_RTS\_PC6](#a5371f435ba7b54049797c8e4d57c263d)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x6) |
| #define | [EUSART1\_RTS\_PC7](#a8ed175732bc35f35c6e7487be8b903d2)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x2, 0x7) |
| #define | [EUSART1\_RTS\_PD0](#a28ef23be5d09659645516e832ed6f65f)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x3, 0x0) |
| #define | [EUSART1\_RTS\_PD1](#a94be5cf6daa2de7b415b78c5b0e1547f)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x3, 0x1) |
| #define | [EUSART1\_RTS\_PD2](#aa8dac982c8de064268697d4bb9460973)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x3, 0x2) |
| #define | [EUSART1\_RTS\_PD3](#acb2eb162bdf3ccfdd69e17eb047a2188)   [SILABS\_DBUS\_EUSART1\_RTS](#a3d9d1df82dd7e8a060d36353bbb00f18)(0x3, 0x3) |
| #define | [EUSART1\_RX\_PA0](#a2c1a7ed0cc467841cebcf24d44d2f258)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x0) |
| #define | [EUSART1\_RX\_PA1](#a7e33ba392cb53d219f1eda52d67a6944)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x1) |
| #define | [EUSART1\_RX\_PA2](#a3c0f7f785f61504faf51fd3155ff02d6)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x2) |
| #define | [EUSART1\_RX\_PA3](#ad40833154f299658986ad7ad63ec1b96)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x3) |
| #define | [EUSART1\_RX\_PA4](#a6c41b67649a5c2d1e861fe316e0ef533)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x4) |
| #define | [EUSART1\_RX\_PA5](#af0868cbd1c8abf3e71227bfb70f46f22)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x5) |
| #define | [EUSART1\_RX\_PA6](#a8245e0aca9ea584f0490aee19687c067)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x6) |
| #define | [EUSART1\_RX\_PA7](#a7b51646c08b9fc0ba688c99c623b5d18)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x7) |
| #define | [EUSART1\_RX\_PA8](#af00e3232320d0c3fd07e60c9aa13f55e)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x0, 0x8) |
| #define | [EUSART1\_RX\_PB0](#a6b070084786fd60d676b2c2f75c1f98e)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x1, 0x0) |
| #define | [EUSART1\_RX\_PB1](#a77554a2b4ae43d009a9e15fd3f4028e3)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x1, 0x1) |
| #define | [EUSART1\_RX\_PB2](#ac2fa1d52ab0de981d47e9b65ab9665cb)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x1, 0x2) |
| #define | [EUSART1\_RX\_PB3](#ae0ee1a1afcf0079d4a9283bdd3e60588)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x1, 0x3) |
| #define | [EUSART1\_RX\_PB4](#aaec2f1281d66ce906061624d4917baa6)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x1, 0x4) |
| #define | [EUSART1\_RX\_PC0](#aa98270d29aa5350d603b6801b81e061e)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x0) |
| #define | [EUSART1\_RX\_PC1](#a03ee872913b0d67c65f8dc385fb4e91a)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x1) |
| #define | [EUSART1\_RX\_PC2](#ac4aadea1a819cf4e285f89d27718552f)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x2) |
| #define | [EUSART1\_RX\_PC3](#a83b13f35d15a557bf9a53bb4a439805f)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x3) |
| #define | [EUSART1\_RX\_PC4](#a70d814531178d1d9b15c789076835b1e)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x4) |
| #define | [EUSART1\_RX\_PC5](#a458e9dbc13a3dab016b5507d65ab6292)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x5) |
| #define | [EUSART1\_RX\_PC6](#a5b74541abae3c7c46603704b893c8f77)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x6) |
| #define | [EUSART1\_RX\_PC7](#a64abe91c5e0ee069f4e7cd9f1988408a)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x2, 0x7) |
| #define | [EUSART1\_RX\_PD0](#a98f3d4c0fd1c382b3e74de148239493b)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x3, 0x0) |
| #define | [EUSART1\_RX\_PD1](#a2bcf22654333629b1512b192fafaabf8)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x3, 0x1) |
| #define | [EUSART1\_RX\_PD2](#a23ec89755383423270053f9d62cb3052)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x3, 0x2) |
| #define | [EUSART1\_RX\_PD3](#a3b66d7466704954a9c4f7d114cc3948b)   [SILABS\_DBUS\_EUSART1\_RX](#af1675cdac7ef1fbf39f79665746a74c9)(0x3, 0x3) |
| #define | [EUSART1\_SCLK\_PA0](#a1866dd8e210ba1ab2877a58fed00c93e)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x0) |
| #define | [EUSART1\_SCLK\_PA1](#a48c98c4dadaf125f1a227ef37bbf9738)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x1) |
| #define | [EUSART1\_SCLK\_PA2](#a1f529ea54ec4efcdc13c99ccf42b3db9)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x2) |
| #define | [EUSART1\_SCLK\_PA3](#a576b277096ee6c9b14a99627e77720d3)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x3) |
| #define | [EUSART1\_SCLK\_PA4](#ac13a88d3cd2571fdc2a57284e6d62c09)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x4) |
| #define | [EUSART1\_SCLK\_PA5](#adbce8bccdef55112969e797c7b6639dd)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x5) |
| #define | [EUSART1\_SCLK\_PA6](#a7c77e84e1434e302f03737b24d1ff079)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x6) |
| #define | [EUSART1\_SCLK\_PA7](#aaf42811c16b367f1abf8e6bc160a8c20)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x7) |
| #define | [EUSART1\_SCLK\_PA8](#aebab59d6a37e8c841da4f390387897ab)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x0, 0x8) |
| #define | [EUSART1\_SCLK\_PB0](#a203c4398d642eada6bda1cc7bf80bfbe)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x1, 0x0) |
| #define | [EUSART1\_SCLK\_PB1](#abd4a43cfc4b84a8b2e1c4097771d7a59)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x1, 0x1) |
| #define | [EUSART1\_SCLK\_PB2](#abe989ab643fbe91732fc5d85c4b8c560)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x1, 0x2) |
| #define | [EUSART1\_SCLK\_PB3](#afb4913ed4eb217a972c17821c2eafc27)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x1, 0x3) |
| #define | [EUSART1\_SCLK\_PB4](#a640a1a6ece43715d2122cb4ced70543a)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x1, 0x4) |
| #define | [EUSART1\_SCLK\_PC0](#a7d65400748ea9527510a0e34f410b8c3)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x0) |
| #define | [EUSART1\_SCLK\_PC1](#a7ea3f4ca3c6e8f920c68e7a9bd4f58cb)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x1) |
| #define | [EUSART1\_SCLK\_PC2](#ad2998e2a2182b75f088ca5bcbc95753a)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x2) |
| #define | [EUSART1\_SCLK\_PC3](#ab26cf07e0496f46713893e36521d8cc1)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x3) |
| #define | [EUSART1\_SCLK\_PC4](#acc5b977ae91e36cb79a4274f06d185f3)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x4) |
| #define | [EUSART1\_SCLK\_PC5](#aee5ca21dcd28e168927431e40848d6f5)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x5) |
| #define | [EUSART1\_SCLK\_PC6](#aaf2c62839097ad29f904dd4022f0b27c)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x6) |
| #define | [EUSART1\_SCLK\_PC7](#a78cf96f19e780387646d3e3cdf32deef)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x2, 0x7) |
| #define | [EUSART1\_SCLK\_PD0](#a9b74e299bdafb94c3f419e003aea18df)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x3, 0x0) |
| #define | [EUSART1\_SCLK\_PD1](#a8f314da8501571ed1fb5d9043a48f022)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x3, 0x1) |
| #define | [EUSART1\_SCLK\_PD2](#a2ca42149963e87a955e9bc529ba1764e)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x3, 0x2) |
| #define | [EUSART1\_SCLK\_PD3](#a408f40e7306530450a58ad4135df0401)   [SILABS\_DBUS\_EUSART1\_SCLK](#a8f10a814a0b2af37cc01f4b93780c12f)(0x3, 0x3) |
| #define | [EUSART1\_TX\_PA0](#ab28778a5ee4f114285190a082c927118)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x0) |
| #define | [EUSART1\_TX\_PA1](#a073c517a0afd9587386870a630518cbd)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x1) |
| #define | [EUSART1\_TX\_PA2](#a806e7fc362384bc93b618a12af2473f8)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x2) |
| #define | [EUSART1\_TX\_PA3](#a1702c830397c60f0b30b2b9fd9952f0d)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x3) |
| #define | [EUSART1\_TX\_PA4](#a6f0b72325d6aafe9f875e9742a8c8042)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x4) |
| #define | [EUSART1\_TX\_PA5](#ad0cde738ee0488057252b99b667ad00d)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x5) |
| #define | [EUSART1\_TX\_PA6](#a448daaeb0e09d7e8ed1629f93c909539)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x6) |
| #define | [EUSART1\_TX\_PA7](#aea3b8d30b2e1e43348278c7e33e33aa5)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x7) |
| #define | [EUSART1\_TX\_PA8](#a01920e5d24b2a800d5a1b0d0341b9b1b)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x0, 0x8) |
| #define | [EUSART1\_TX\_PB0](#ab39ba8c4be315f5a2222e168f474642d)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x1, 0x0) |
| #define | [EUSART1\_TX\_PB1](#a71460a9b69af5340d0a13823fde821ec)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x1, 0x1) |
| #define | [EUSART1\_TX\_PB2](#ae589d9854e598c01eeb5f660d4b07a61)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x1, 0x2) |
| #define | [EUSART1\_TX\_PB3](#a8387994c7648c19dd755c09827923d8f)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x1, 0x3) |
| #define | [EUSART1\_TX\_PB4](#a30635d481b97dd113d97f53faf8fcfe2)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x1, 0x4) |
| #define | [EUSART1\_TX\_PC0](#af974aba626dbdc04f04bcc6f13243b94)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x0) |
| #define | [EUSART1\_TX\_PC1](#aa7802a5b57a1024764ffbe73b6b5ac39)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x1) |
| #define | [EUSART1\_TX\_PC2](#a0c9b5f28eb50a9731a117ad5f366e92b)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x2) |
| #define | [EUSART1\_TX\_PC3](#a6a348ac2b04733efa6c0ebe34ceb5d4b)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x3) |
| #define | [EUSART1\_TX\_PC4](#a54dfb623abae97d99fa141c8a0bb0ea3)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x4) |
| #define | [EUSART1\_TX\_PC5](#a1100968240942c988f4905912c28aa11)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x5) |
| #define | [EUSART1\_TX\_PC6](#a6e8d91efe4ac6f8224907e3ee500051c)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x6) |
| #define | [EUSART1\_TX\_PC7](#aed9ea236a9a98dbcc9516c4517cb04ed)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x2, 0x7) |
| #define | [EUSART1\_TX\_PD0](#a21666ee324c7d8339c10ee3a5841413b)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x3, 0x0) |
| #define | [EUSART1\_TX\_PD1](#a63920c4b35211b7a2db371b6db68fe34)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x3, 0x1) |
| #define | [EUSART1\_TX\_PD2](#a196cf0e44c04a0b39c143d89f674bc7d)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x3, 0x2) |
| #define | [EUSART1\_TX\_PD3](#acd2c8e123057d490ba2e60b8dbac8836)   [SILABS\_DBUS\_EUSART1\_TX](#adb612d2f22dc57f485e22fe674efb442)(0x3, 0x3) |
| #define | [EUSART1\_CTS\_PA0](#a8d81221acf4017c05ca56c5a98d58552)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x0) |
| #define | [EUSART1\_CTS\_PA1](#a5d4da4feea93c4b06110ca1e3610659a)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x1) |
| #define | [EUSART1\_CTS\_PA2](#af8e1f1909c844d7c2f4b531c82f5c7cb)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x2) |
| #define | [EUSART1\_CTS\_PA3](#a69bd0b952644909144e49f6542d88c92)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x3) |
| #define | [EUSART1\_CTS\_PA4](#a36ce96157ce9be04de043bb2c04cef82)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x4) |
| #define | [EUSART1\_CTS\_PA5](#aa6351a3c82698810d1041413513553fc)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x5) |
| #define | [EUSART1\_CTS\_PA6](#a76dfe398fdb4ed75ae511b29a1d347b0)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x6) |
| #define | [EUSART1\_CTS\_PA7](#ab84cf2fc8ac1a7f5666769f283ec3e49)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x7) |
| #define | [EUSART1\_CTS\_PA8](#aeb09839ecbdd7f2c608e25602a302752)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x0, 0x8) |
| #define | [EUSART1\_CTS\_PB0](#a883da4be324d198cbc34ea41676a9ddf)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x1, 0x0) |
| #define | [EUSART1\_CTS\_PB1](#acc196631f4adce64be8891275c851cc8)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x1, 0x1) |
| #define | [EUSART1\_CTS\_PB2](#ad56423043df1ba928037fb8ad7996a0a)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x1, 0x2) |
| #define | [EUSART1\_CTS\_PB3](#aaf246a8e049ac1b6f0ea6bff0f77d361)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x1, 0x3) |
| #define | [EUSART1\_CTS\_PB4](#a8d541570c6ca67dd288bf96afaa86d00)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x1, 0x4) |
| #define | [EUSART1\_CTS\_PC0](#a71b2e656c782b69d56a103e73b464730)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x0) |
| #define | [EUSART1\_CTS\_PC1](#a3de408c7045ed45e7dc371443c370c23)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x1) |
| #define | [EUSART1\_CTS\_PC2](#a448af5a813508ad8dd8e5d6e5df4b43b)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x2) |
| #define | [EUSART1\_CTS\_PC3](#a5bca4e376d8315ef91f8574ced26eb16)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x3) |
| #define | [EUSART1\_CTS\_PC4](#aa72d1c30858bde17689ed0dfc57069bb)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x4) |
| #define | [EUSART1\_CTS\_PC5](#a70ecbc7c78a15bcdc81b997d720b0b0c)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x5) |
| #define | [EUSART1\_CTS\_PC6](#aa6fc0b0cd1690dd9d8e898b4177deb1f)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x6) |
| #define | [EUSART1\_CTS\_PC7](#a9f21efe766114885dc079c88593fc66a)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x2, 0x7) |
| #define | [EUSART1\_CTS\_PD0](#ae2238ef628fa06b7eb97f58b86bf011b)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x3, 0x0) |
| #define | [EUSART1\_CTS\_PD1](#ae15d8faf92ba3b2b4c07eddf5d6fd274)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x3, 0x1) |
| #define | [EUSART1\_CTS\_PD2](#aef76a9fbbcbd9a4e8d254773bba07126)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x3, 0x2) |
| #define | [EUSART1\_CTS\_PD3](#aa32ab3b05dc99adbfb5b3a84642b6403)   [SILABS\_DBUS\_EUSART1\_CTS](#ad059fbad09ad887f644c51fc1963f4df)(0x3, 0x3) |
| #define | [PTI\_DCLK\_PC0](#a5bdf4f259033a31adaa4e25fe84604ed)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x0) |
| #define | [PTI\_DCLK\_PC1](#aa4e24633e84b6487f85a598419ea7e7d)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x1) |
| #define | [PTI\_DCLK\_PC2](#a53fa8c98bed45c485839c1d86d343733)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x2) |
| #define | [PTI\_DCLK\_PC3](#a930a4ba462ce768196265ec5a53557ba)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x3) |
| #define | [PTI\_DCLK\_PC4](#ae90e5e4841b04412ca3768216d0efaf1)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x4) |
| #define | [PTI\_DCLK\_PC5](#a27b9c07fbbc05a0bd69dd74cc17db0d0)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x5) |
| #define | [PTI\_DCLK\_PC6](#ae36628394c440c14e85b42db8095cba6)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x6) |
| #define | [PTI\_DCLK\_PC7](#a024f81027127cdacccc05c4b49cf99c0)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x2, 0x7) |
| #define | [PTI\_DCLK\_PD0](#a354b3eb4fe4c5e11e1c944761bf00095)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x3, 0x0) |
| #define | [PTI\_DCLK\_PD1](#a14260512bf2682c2fb84fa96f00de9ba)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x3, 0x1) |
| #define | [PTI\_DCLK\_PD2](#af96542673625d7a20712ad4c31953d4b)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x3, 0x2) |
| #define | [PTI\_DCLK\_PD3](#ab234da9210beb7b1f94b75aa9ecf52ca)   [SILABS\_DBUS\_PTI\_DCLK](#a3165d7b2623b12308b38c9abcf900642)(0x3, 0x3) |
| #define | [PTI\_DFRAME\_PC0](#aaa3fdc625a5f096099d23c1760980055)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x0) |
| #define | [PTI\_DFRAME\_PC1](#a23de813c7f0e88b8397ebcc34eb21552)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x1) |
| #define | [PTI\_DFRAME\_PC2](#a667adbc7570cf85833284a141de5fa2d)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x2) |
| #define | [PTI\_DFRAME\_PC3](#afea8ff0ad63b50a277e69f305b64e7cd)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x3) |
| #define | [PTI\_DFRAME\_PC4](#a97019cfae35bfc913e7ed2456a816ab5)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x4) |
| #define | [PTI\_DFRAME\_PC5](#a15d67770385d695409d975ba26d5d0e4)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x5) |
| #define | [PTI\_DFRAME\_PC6](#a318fe553b5da2adc9ce35e2571934bc2)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x6) |
| #define | [PTI\_DFRAME\_PC7](#a0e8e93d43d78096c24db5c4483ee68e1)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x2, 0x7) |
| #define | [PTI\_DFRAME\_PD0](#ac6a830947b330b10ae2c9e3cdc1887b4)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x3, 0x0) |
| #define | [PTI\_DFRAME\_PD1](#a1f08a23bacafb3dae71d143c2c5ab863)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x3, 0x1) |
| #define | [PTI\_DFRAME\_PD2](#acafc4bcb7af54f59dbacb7d9ce8712ce)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x3, 0x2) |
| #define | [PTI\_DFRAME\_PD3](#aee415d6eae1beab453af125a316f549c)   [SILABS\_DBUS\_PTI\_DFRAME](#a12a23ec2045680c0521b20f50d421881)(0x3, 0x3) |
| #define | [PTI\_DOUT\_PC0](#a9413ff462e44dcf3b76204629c524a73)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x0) |
| #define | [PTI\_DOUT\_PC1](#a49ef267b8afcafa1da426058b4f94d9f)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x1) |
| #define | [PTI\_DOUT\_PC2](#a8563048b51841f44cbd35c573131bf18)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x2) |
| #define | [PTI\_DOUT\_PC3](#aa4304d8154383f012e4a3b53a070b120)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x3) |
| #define | [PTI\_DOUT\_PC4](#a715e7ceca236771ae00bb36143a586d2)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x4) |
| #define | [PTI\_DOUT\_PC5](#aa2bb4223540e03b6ef7c21b05b76b380)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x5) |
| #define | [PTI\_DOUT\_PC6](#a746b97fe77bb360b3048d3cc1730b607)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x6) |
| #define | [PTI\_DOUT\_PC7](#a3e939dfef6c7f5f04abe8e32d0a866a2)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x2, 0x7) |
| #define | [PTI\_DOUT\_PD0](#a569a588da9acdad8c7b18c6d7ee83681)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x3, 0x0) |
| #define | [PTI\_DOUT\_PD1](#aac9876e72b5e68eb3d7138c72e7ac25b)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x3, 0x1) |
| #define | [PTI\_DOUT\_PD2](#a447f3b579538e9a44615dfe77e8ace24)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x3, 0x2) |
| #define | [PTI\_DOUT\_PD3](#ad80593f470c79948e0b9845cad0b739b)   [SILABS\_DBUS\_PTI\_DOUT](#ae418c8c258cc10d03e4d36b741827f82)(0x3, 0x3) |
| #define | [I2C0\_SCL\_PA0](#a23ced15df4b090058198bd06541b5885)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x0) |
| #define | [I2C0\_SCL\_PA1](#a695c8fa25220070f883a7866019132a5)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x1) |
| #define | [I2C0\_SCL\_PA2](#a59521028aaeca25d19dce77adf76f9b7)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x2) |
| #define | [I2C0\_SCL\_PA3](#a68f1a22cb1cf1445f9d94d230b7d81e6)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x3) |
| #define | [I2C0\_SCL\_PA4](#aefbf0c45fe8a1215f17a6d31c5948889)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x4) |
| #define | [I2C0\_SCL\_PA5](#ae334a06857e99d806213ccb6b6e582d3)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x5) |
| #define | [I2C0\_SCL\_PA6](#a912dd4938a0b0cda381360467d635fc8)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x6) |
| #define | [I2C0\_SCL\_PA7](#a843a8a1e536a19115dad9b821e09fc35)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x7) |
| #define | [I2C0\_SCL\_PA8](#a5d5194c66eaa75401ef86ae1b702c882)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x0, 0x8) |
| #define | [I2C0\_SCL\_PB0](#a66acedca2ec779cfe23f1d9c6e2fc129)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x1, 0x0) |
| #define | [I2C0\_SCL\_PB1](#a5af9487dc5b440644597f549fb4775e2)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x1, 0x1) |
| #define | [I2C0\_SCL\_PB2](#a9bf6c40a60c458dcf38ab7eff6d90768)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x1, 0x2) |
| #define | [I2C0\_SCL\_PB3](#a7cda95585deaad597713feece27a1a03)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x1, 0x3) |
| #define | [I2C0\_SCL\_PB4](#add039d286e25d19092fcee79fac5c168)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x1, 0x4) |
| #define | [I2C0\_SCL\_PC0](#afda900994567b6303959e4f666fceaf1)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x0) |
| #define | [I2C0\_SCL\_PC1](#aecced4d0cc1f98a1f8e87d09cceff92a)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x1) |
| #define | [I2C0\_SCL\_PC2](#ab376247e3dbd84ccfd2b94af9c07505a)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x2) |
| #define | [I2C0\_SCL\_PC3](#a9a9354d74c5e9c6ebad7e646f6b8ee63)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x3) |
| #define | [I2C0\_SCL\_PC4](#aafe4a6c9133c8213940f026568866b9d)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x4) |
| #define | [I2C0\_SCL\_PC5](#a93ad2564f0ad899a336521853e3c5f35)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x5) |
| #define | [I2C0\_SCL\_PC6](#a45d40464f74efe9babb464d9e72ac0e1)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x6) |
| #define | [I2C0\_SCL\_PC7](#aef0e85e86050336cd4112241ef60dad5)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x2, 0x7) |
| #define | [I2C0\_SCL\_PD0](#ab5e0b9a784779a5e92ab1fa79c9aa6cc)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x3, 0x0) |
| #define | [I2C0\_SCL\_PD1](#a3d7b2816e4c4f01aba45a339bc77feea)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x3, 0x1) |
| #define | [I2C0\_SCL\_PD2](#a487c9ff099c2dabf34d65f0377e5e195)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x3, 0x2) |
| #define | [I2C0\_SCL\_PD3](#a2c36512ca362cf14654d72a59e4de079)   [SILABS\_DBUS\_I2C0\_SCL](#a652b5412868f09aff727d2a84ce5efd6)(0x3, 0x3) |
| #define | [I2C0\_SDA\_PA0](#aaf8bcb4a387404aa356da60c0e9cc869)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x0) |
| #define | [I2C0\_SDA\_PA1](#a6f74ca01f25bdded002e45e679240275)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x1) |
| #define | [I2C0\_SDA\_PA2](#acdc71a141f1ba40bb5c3ec9f06bd35e6)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x2) |
| #define | [I2C0\_SDA\_PA3](#a401989601987cfb72944453f11918e2a)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x3) |
| #define | [I2C0\_SDA\_PA4](#a66dad3b35dd2a650a186933abb43f6c3)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x4) |
| #define | [I2C0\_SDA\_PA5](#a1fdfea195e2831a05d2ad42a091aa53b)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x5) |
| #define | [I2C0\_SDA\_PA6](#a0c5573f60342f026d0553797a636a488)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x6) |
| #define | [I2C0\_SDA\_PA7](#a35d947fc846c9fbe828b92169dbc30bd)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x7) |
| #define | [I2C0\_SDA\_PA8](#a2bafe8f8b3424002354a87423c7564ff)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x0, 0x8) |
| #define | [I2C0\_SDA\_PB0](#a9e333616419f1afb29657e239ebf9b12)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x1, 0x0) |
| #define | [I2C0\_SDA\_PB1](#a25bba68392534791cad2bc692a141782)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x1, 0x1) |
| #define | [I2C0\_SDA\_PB2](#a36d3f871769d46038f7305c590f4da44)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x1, 0x2) |
| #define | [I2C0\_SDA\_PB3](#af28ae3cd9556f78d2a9e9cbec5eea822)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x1, 0x3) |
| #define | [I2C0\_SDA\_PB4](#aa0dfa7701ac813cb33f6b192e724c028)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x1, 0x4) |
| #define | [I2C0\_SDA\_PC0](#acb9a1287a10a954e1ff0bf82478f3bf8)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x0) |
| #define | [I2C0\_SDA\_PC1](#a0c89a72767592385a9a625d72c90f824)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x1) |
| #define | [I2C0\_SDA\_PC2](#a0e115e41c26b45de04ee71a95cd5b87c)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x2) |
| #define | [I2C0\_SDA\_PC3](#afbad7695056556b776533aafc47b0299)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x3) |
| #define | [I2C0\_SDA\_PC4](#a603f80b261cded3f838f85ad889a4b88)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x4) |
| #define | [I2C0\_SDA\_PC5](#a5864615c0e7063fc4f1acb8e4e3a05d2)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x5) |
| #define | [I2C0\_SDA\_PC6](#a9e461e560cc99ba58586c4a4b9085c53)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x6) |
| #define | [I2C0\_SDA\_PC7](#a1f6044bad1b47007a0250a99e778a7f4)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x2, 0x7) |
| #define | [I2C0\_SDA\_PD0](#a610731cb645ab65d802d95bb65437d8c)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x3, 0x0) |
| #define | [I2C0\_SDA\_PD1](#a86eade4a55994ce4285b81cf29c93883)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x3, 0x1) |
| #define | [I2C0\_SDA\_PD2](#a5d3416853673a2192ec5f5712921d370)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x3, 0x2) |
| #define | [I2C0\_SDA\_PD3](#a096b74cd9e2842c5d4ff8d7a7186106a)   [SILABS\_DBUS\_I2C0\_SDA](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)(0x3, 0x3) |
| #define | [I2C1\_SCL\_PC0](#a356ddb78378e70250e07992cf92dd8b7)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x0) |
| #define | [I2C1\_SCL\_PC1](#ad327d495abfaa2bb7ae3344a163f052f)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x1) |
| #define | [I2C1\_SCL\_PC2](#aa89ddd739af59624f4a176443aa17636)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x2) |
| #define | [I2C1\_SCL\_PC3](#af0e6baea8d2c35eb8991706946ffc05b)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x3) |
| #define | [I2C1\_SCL\_PC4](#a346b20cbc89a5af4dfffe00c9ef41e92)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x4) |
| #define | [I2C1\_SCL\_PC5](#aec416779b37e6a51e48e3fcadfca591a)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x5) |
| #define | [I2C1\_SCL\_PC6](#a7e3349a10010f0f54657e0fb5e92ffe2)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x6) |
| #define | [I2C1\_SCL\_PC7](#a2c5373d8cd0dfc39e30c9460552201ef)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x2, 0x7) |
| #define | [I2C1\_SCL\_PD0](#a865b5c341b794b96daba59c14807c057)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x3, 0x0) |
| #define | [I2C1\_SCL\_PD1](#a9f3ebaefe248d5aa292ade2727a11ee9)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x3, 0x1) |
| #define | [I2C1\_SCL\_PD2](#a7eb71571b0e15669fb353a0bd65f2c72)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x3, 0x2) |
| #define | [I2C1\_SCL\_PD3](#a6a86266c8ab637b0b31244cbf0636ab0)   [SILABS\_DBUS\_I2C1\_SCL](#aa55669252ab4d30ff2044a7ac5e8fad1)(0x3, 0x3) |
| #define | [I2C1\_SDA\_PC0](#a7239b0bfd8b71b2ee9e85e8cb2e6eaaf)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x0) |
| #define | [I2C1\_SDA\_PC1](#afe966c9b62cc1e0d598ea6ea92d663b8)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x1) |
| #define | [I2C1\_SDA\_PC2](#af3ba02992276ed2088a6652b695d270d)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x2) |
| #define | [I2C1\_SDA\_PC3](#a424670a07eab18c7e3ce3db2d68d44f6)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x3) |
| #define | [I2C1\_SDA\_PC4](#ad7eebe896b02c99e7f27340a8ea01a8f)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x4) |
| #define | [I2C1\_SDA\_PC5](#a12822294913c78002356a6be7b698e2e)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x5) |
| #define | [I2C1\_SDA\_PC6](#a9af96f372e04b931184d7a9bd716b733)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x6) |
| #define | [I2C1\_SDA\_PC7](#a766136e7b677f8c4ddcc6053b0527eee)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x2, 0x7) |
| #define | [I2C1\_SDA\_PD0](#a58f45546c69325b13cd062ca7a238c7a)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x3, 0x0) |
| #define | [I2C1\_SDA\_PD1](#aa7cf52519a05cd49aef954ce5191a377)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x3, 0x1) |
| #define | [I2C1\_SDA\_PD2](#ad779ebeed2865070af9e56244e9c43d0)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x3, 0x2) |
| #define | [I2C1\_SDA\_PD3](#a77b0c5734afd5123fd3ae520f10a8da8)   [SILABS\_DBUS\_I2C1\_SDA](#a0c32c2f4351441d0a97a445627912904)(0x3, 0x3) |
| #define | [LETIMER0\_OUT0\_PA0](#a352e584caede1a83b786463abf8e8ffc)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x0) |
| #define | [LETIMER0\_OUT0\_PA1](#a237d004885f30f207a78f3fce4380476)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x1) |
| #define | [LETIMER0\_OUT0\_PA2](#a25d0f59297bd6c10acc7714b06af99ca)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x2) |
| #define | [LETIMER0\_OUT0\_PA3](#a9120e73b07bfa093065ec040045eb61d)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x3) |
| #define | [LETIMER0\_OUT0\_PA4](#a4f0e8db2242fed71b78c6b0679a6ff76)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x4) |
| #define | [LETIMER0\_OUT0\_PA5](#a26a82422ca3e7fbd558caa46b4c6705d)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x5) |
| #define | [LETIMER0\_OUT0\_PA6](#a808e50c2f7823f703795dfbe5d5ef50e)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x6) |
| #define | [LETIMER0\_OUT0\_PA7](#a0f5833c4d88f979f1cdd7a1375a8074b)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x7) |
| #define | [LETIMER0\_OUT0\_PA8](#a0cf57fda500379c7e91c98a05d1e17ec)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x0, 0x8) |
| #define | [LETIMER0\_OUT0\_PB0](#ad81eda4d47fbc7265b325b09eb47232c)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x1, 0x0) |
| #define | [LETIMER0\_OUT0\_PB1](#a20d0230e58f46869e37b9acfe0e5fb0d)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x1, 0x1) |
| #define | [LETIMER0\_OUT0\_PB2](#a79820d41c14965a475c0f58982670e34)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x1, 0x2) |
| #define | [LETIMER0\_OUT0\_PB3](#a31d042f62545423b84bb0de3be30bdcb)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x1, 0x3) |
| #define | [LETIMER0\_OUT0\_PB4](#a433315136fec0480d99d198e5241915a)   [SILABS\_DBUS\_LETIMER0\_OUT0](#ab81ce78522519bd5a5e257c8f4f2c27f)(0x1, 0x4) |
| #define | [LETIMER0\_OUT1\_PA0](#a3cab629b6e9cd573b30f8e45a747e819)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x0) |
| #define | [LETIMER0\_OUT1\_PA1](#a2e90dd7d7686acf9665182356fba429d)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x1) |
| #define | [LETIMER0\_OUT1\_PA2](#a1ded3647217b200c7d49bf6f99df8800)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x2) |
| #define | [LETIMER0\_OUT1\_PA3](#ab329e7913b209f11eaba0a2623358976)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x3) |
| #define | [LETIMER0\_OUT1\_PA4](#a0e0dc57036750466e500d46d9f2f8674)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x4) |
| #define | [LETIMER0\_OUT1\_PA5](#a2c211216042c0ab444cf3e1b54d4e2f7)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x5) |
| #define | [LETIMER0\_OUT1\_PA6](#a0aebcc5748062062d09dec35c4baa61f)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x6) |
| #define | [LETIMER0\_OUT1\_PA7](#aabd4bbcd01e67aa31a1a06b6bbe16edc)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x7) |
| #define | [LETIMER0\_OUT1\_PA8](#af89df3c0b1d281356ed2316c88ceaa46)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x0, 0x8) |
| #define | [LETIMER0\_OUT1\_PB0](#a5501b8d6e668ef58a71e19bfe0d620b8)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x1, 0x0) |
| #define | [LETIMER0\_OUT1\_PB1](#a8e4b46c768114f20ee1002820ee4d583)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x1, 0x1) |
| #define | [LETIMER0\_OUT1\_PB2](#aa1a23a819291f5ab445f4d3db17c78b6)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x1, 0x2) |
| #define | [LETIMER0\_OUT1\_PB3](#a87c4b33f802fa34191489db40f674684)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x1, 0x3) |
| #define | [LETIMER0\_OUT1\_PB4](#a0f9c9dcc043629fd8a8bfebf710f3e10)   [SILABS\_DBUS\_LETIMER0\_OUT1](#a2effaa50da9b899d91eb127cdf554098)(0x1, 0x4) |
| #define | [MODEM\_ANT0\_PA0](#a7f276456c2949e4151a1b2a734f8885c)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x0) |
| #define | [MODEM\_ANT0\_PA1](#a79c6f7c43dfc9adab0c8eeb974842745)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x1) |
| #define | [MODEM\_ANT0\_PA2](#ae187f6726ed20849cb327fbdddd44aca)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x2) |
| #define | [MODEM\_ANT0\_PA3](#a45bcc15c32caaa653434df7b01274283)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x3) |
| #define | [MODEM\_ANT0\_PA4](#a2378348e1cf6d527113895ad243cc58d)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x4) |
| #define | [MODEM\_ANT0\_PA5](#a722db9c869f2f89794bcc1ae32318ad4)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x5) |
| #define | [MODEM\_ANT0\_PA6](#a4bffa8d5ecfb474a91ff85afc315043a)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x6) |
| #define | [MODEM\_ANT0\_PA7](#a894653787f083faf2185f138b1a77551)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x7) |
| #define | [MODEM\_ANT0\_PA8](#a0ed9a2f3ae0b7b8edb0cfd28233a8489)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x0, 0x8) |
| #define | [MODEM\_ANT0\_PB0](#a509466c0511355374b0ee3ece106acd6)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x1, 0x0) |
| #define | [MODEM\_ANT0\_PB1](#a4c2864f003ccf1355fdbb2be9df0d2ec)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x1, 0x1) |
| #define | [MODEM\_ANT0\_PB2](#a63d38e8d680f24158d34a6bff19028b1)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x1, 0x2) |
| #define | [MODEM\_ANT0\_PB3](#addd2df0103ce62bea89bea865ad6294a)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x1, 0x3) |
| #define | [MODEM\_ANT0\_PB4](#a90d1b1b9472b551710f7ca062750d1c6)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x1, 0x4) |
| #define | [MODEM\_ANT0\_PC0](#a6b06e4cb9c997d609b19d7fb7639bf8d)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x0) |
| #define | [MODEM\_ANT0\_PC1](#a000751139691af8d66623ad0bd43fc9b)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x1) |
| #define | [MODEM\_ANT0\_PC2](#afd5bc8540d8e3e5b0d182312520517be)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x2) |
| #define | [MODEM\_ANT0\_PC3](#a33b690ae2e28b1b08b691aa4742d84d7)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x3) |
| #define | [MODEM\_ANT0\_PC4](#ac22d54cd6c263a39f33caedf7cb09a0e)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x4) |
| #define | [MODEM\_ANT0\_PC5](#a6982c06cdd7b783257ed5f3a74c735c7)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x5) |
| #define | [MODEM\_ANT0\_PC6](#a8d28c8701b26924dd7038b6794a97a26)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x6) |
| #define | [MODEM\_ANT0\_PC7](#ad9e7f4a18a0eeedadedbefbf81c0449c)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x2, 0x7) |
| #define | [MODEM\_ANT0\_PD0](#a01730221498f5de5590dbe8f6a293702)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x3, 0x0) |
| #define | [MODEM\_ANT0\_PD1](#a968474651d6fc8ced22a693a55d8bf4d)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x3, 0x1) |
| #define | [MODEM\_ANT0\_PD2](#a6bee8cd789f6922130830688cf586971)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x3, 0x2) |
| #define | [MODEM\_ANT0\_PD3](#aef59bb3ec42a534ffe32a53fb26e1656)   [SILABS\_DBUS\_MODEM\_ANT0](#a0225f18d061c851599210b56aeb42231)(0x3, 0x3) |
| #define | [MODEM\_ANT1\_PA0](#a983f562f1f690bbec27d868c3d6b2b1a)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x0) |
| #define | [MODEM\_ANT1\_PA1](#a1c8d37c5145858068556a032983680d1)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x1) |
| #define | [MODEM\_ANT1\_PA2](#a9a879a4511af923143f8dc6e7710f0be)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x2) |
| #define | [MODEM\_ANT1\_PA3](#a5753d0d0ab943103f54d6ad9ea76bccf)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x3) |
| #define | [MODEM\_ANT1\_PA4](#a164fc42c8f2bc81bc70453af7bf82402)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x4) |
| #define | [MODEM\_ANT1\_PA5](#a790e4407942a7fb6fed5972b59bf12c9)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x5) |
| #define | [MODEM\_ANT1\_PA6](#a908cd5b571ab7ec4ba04581f3bf67166)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x6) |
| #define | [MODEM\_ANT1\_PA7](#a5c272c67918110b0cd323ed0228370bb)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x7) |
| #define | [MODEM\_ANT1\_PA8](#a1ab7e1ea92808eb14c818516aaa3295a)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x0, 0x8) |
| #define | [MODEM\_ANT1\_PB0](#adbe918778efba6fe712e7043457c43bb)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x1, 0x0) |
| #define | [MODEM\_ANT1\_PB1](#a6c5a484675c81a07f3709cb391113c22)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x1, 0x1) |
| #define | [MODEM\_ANT1\_PB2](#acbc03ad5136cb7715b10956805d851ad)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x1, 0x2) |
| #define | [MODEM\_ANT1\_PB3](#ac9db3cba6b213aba7b2e75913d7793b0)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x1, 0x3) |
| #define | [MODEM\_ANT1\_PB4](#a3772761615fb1f6b9427d09f40de1cb0)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x1, 0x4) |
| #define | [MODEM\_ANT1\_PC0](#a5718fbbd7d66e6c775b8904b50b14aec)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x0) |
| #define | [MODEM\_ANT1\_PC1](#a25315b04583ee4d44f2e1835003679e9)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x1) |
| #define | [MODEM\_ANT1\_PC2](#a7480d21cbb697630fd83f494f671b030)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x2) |
| #define | [MODEM\_ANT1\_PC3](#aa6ba89e0d2c7347f10a1a18d461986db)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x3) |
| #define | [MODEM\_ANT1\_PC4](#a293042adb906716b25453e23c66932ee)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x4) |
| #define | [MODEM\_ANT1\_PC5](#aa699042d4cec5024da6439e6fa629c5f)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x5) |
| #define | [MODEM\_ANT1\_PC6](#a6f4b41d3971310c038878142c59d1375)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x6) |
| #define | [MODEM\_ANT1\_PC7](#aa48104a69c4edacb22f41bd14e717640)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x2, 0x7) |
| #define | [MODEM\_ANT1\_PD0](#a1ebb5a0437c033fa7d567000c0b8c383)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x3, 0x0) |
| #define | [MODEM\_ANT1\_PD1](#a1cc580714150e9383e280946b2863b31)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x3, 0x1) |
| #define | [MODEM\_ANT1\_PD2](#ac3322bcfcef6e6a680cf4611d0b363ef)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x3, 0x2) |
| #define | [MODEM\_ANT1\_PD3](#abfdb37fc77643dc2853d87009c2425d6)   [SILABS\_DBUS\_MODEM\_ANT1](#aaff7073911479298cda7729646f6990e)(0x3, 0x3) |
| #define | [MODEM\_ANTROLLOVER\_PC0](#ace2bae83851b3aab46a81ef1a6c636b4)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x0) |
| #define | [MODEM\_ANTROLLOVER\_PC1](#a85ff56d69539994de2a84edf12f8a2be)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x1) |
| #define | [MODEM\_ANTROLLOVER\_PC2](#ae6601ed4b1dc45fad0deb09610797610)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x2) |
| #define | [MODEM\_ANTROLLOVER\_PC3](#a53fceeed6e44ab7bc81698d3c4c16207)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x3) |
| #define | [MODEM\_ANTROLLOVER\_PC4](#ac253adc5e51912ed5f4407447c81f473)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x4) |
| #define | [MODEM\_ANTROLLOVER\_PC5](#a60f405f65313e35ba59eca8fa208ed2c)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x5) |
| #define | [MODEM\_ANTROLLOVER\_PC6](#ad39de8c7dff7e3297e5beca22e2034f4)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x6) |
| #define | [MODEM\_ANTROLLOVER\_PC7](#a50b0007df6bc2de4b9200cbb1b79acf0)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x2, 0x7) |
| #define | [MODEM\_ANTROLLOVER\_PD0](#a88bb19ac23eb8bcc2868bf22bd4a12af)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x3, 0x0) |
| #define | [MODEM\_ANTROLLOVER\_PD1](#a92aeed47b01736dac03935ac699b9727)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x3, 0x1) |
| #define | [MODEM\_ANTROLLOVER\_PD2](#a603e14d84a8b13b7d4ee5bdab126cdae)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x3, 0x2) |
| #define | [MODEM\_ANTROLLOVER\_PD3](#a506855980f4dda9c5de58b11d76f7b4f)   [SILABS\_DBUS\_MODEM\_ANTROLLOVER](#ac618ed85f554e3e852ad256d20ad95d5)(0x3, 0x3) |
| #define | [MODEM\_ANTRR0\_PC0](#a72a1f767f29b37e2f0975efb930aabdc)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x0) |
| #define | [MODEM\_ANTRR0\_PC1](#a7465a3a4cf1cd92249001733145da7ed)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x1) |
| #define | [MODEM\_ANTRR0\_PC2](#a1b109adfe9e7699e7cb1a1fb46aa132c)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x2) |
| #define | [MODEM\_ANTRR0\_PC3](#a4109515cd008205b323edb06d2a19607)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x3) |
| #define | [MODEM\_ANTRR0\_PC4](#a56971ab62d7131e5aba024260d295153)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x4) |
| #define | [MODEM\_ANTRR0\_PC5](#a4de029d596f34060bde0d63982b171b3)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x5) |
| #define | [MODEM\_ANTRR0\_PC6](#a3a438458ac921a00c90a85d343ea1f90)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x6) |
| #define | [MODEM\_ANTRR0\_PC7](#a68f15a8b8a2acd73ff7b772aa529c0d9)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x2, 0x7) |
| #define | [MODEM\_ANTRR0\_PD0](#a78f716f923dadb2a1df8eebc07c1a1ba)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x3, 0x0) |
| #define | [MODEM\_ANTRR0\_PD1](#ab46244ef8e98b0e13a0874b8831d1c9e)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x3, 0x1) |
| #define | [MODEM\_ANTRR0\_PD2](#ad652d37f429c634eaed147b962b1f81c)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x3, 0x2) |
| #define | [MODEM\_ANTRR0\_PD3](#a1cf6846a778c4a5820d42d1a8b9a6cef)   [SILABS\_DBUS\_MODEM\_ANTRR0](#a076fd7a7e8083517d750f0ef332faefe)(0x3, 0x3) |
| #define | [MODEM\_ANTRR1\_PC0](#a5b77d7b22d3ba5fc6ccadceb8fd784e5)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x0) |
| #define | [MODEM\_ANTRR1\_PC1](#a79bc69a44835cf383b1de6037c8fae63)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x1) |
| #define | [MODEM\_ANTRR1\_PC2](#aa7cd2fde356a617651a7b518f9558709)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x2) |
| #define | [MODEM\_ANTRR1\_PC3](#ac12248a293d8a3c328df438370024a12)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x3) |
| #define | [MODEM\_ANTRR1\_PC4](#a6067448e7e46ae003e07b75ec4f22ddf)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x4) |
| #define | [MODEM\_ANTRR1\_PC5](#afb89ffed0de8306a2b3b2ff8a09db4eb)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x5) |
| #define | [MODEM\_ANTRR1\_PC6](#a2b02ddcbecd53f862993644a685928df)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x6) |
| #define | [MODEM\_ANTRR1\_PC7](#a5d14286b67618916e103c98ccaab6652)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x2, 0x7) |
| #define | [MODEM\_ANTRR1\_PD0](#a3d4c45786676da1e67017a4cdb048449)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x3, 0x0) |
| #define | [MODEM\_ANTRR1\_PD1](#a74ac37ba6d806625dadd63c1af681a84)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x3, 0x1) |
| #define | [MODEM\_ANTRR1\_PD2](#a5c4e16526937500b8cc70a6b844ee832)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x3, 0x2) |
| #define | [MODEM\_ANTRR1\_PD3](#a79878ca6c07ea72a02c23a7321832b29)   [SILABS\_DBUS\_MODEM\_ANTRR1](#a4415eef2a0f03f68eeec9f39cfa00772)(0x3, 0x3) |
| #define | [MODEM\_ANTRR2\_PC0](#a86532fa3d12fd905879905f4df67d954)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x0) |
| #define | [MODEM\_ANTRR2\_PC1](#a6e586c76b41f2ecf6384a6257390ee22)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x1) |
| #define | [MODEM\_ANTRR2\_PC2](#af57b2e22e3079c5825638bf1556d5f63)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x2) |
| #define | [MODEM\_ANTRR2\_PC3](#a43e57733d4b8bebe91750a3041245789)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x3) |
| #define | [MODEM\_ANTRR2\_PC4](#aa31ca6e6610920deaa06c77f7deaf40c)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x4) |
| #define | [MODEM\_ANTRR2\_PC5](#af3df188180c0609f2cb4c63f1ff77ff1)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x5) |
| #define | [MODEM\_ANTRR2\_PC6](#a69bb0899e1d7201561638d287612708c)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x6) |
| #define | [MODEM\_ANTRR2\_PC7](#a0696c2885355b5c7b13bef2e51d7188f)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x2, 0x7) |
| #define | [MODEM\_ANTRR2\_PD0](#a368c3325d067b5f5f93d67ad59cf04a9)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x3, 0x0) |
| #define | [MODEM\_ANTRR2\_PD1](#a019e9b59d7ebf97b06ea3deb84eb8a9d)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x3, 0x1) |
| #define | [MODEM\_ANTRR2\_PD2](#a591f45f9fa102e7e5ce0281003eb7ba9)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x3, 0x2) |
| #define | [MODEM\_ANTRR2\_PD3](#a341ce7ea3431fe6a6b04f88ba4cd4521)   [SILABS\_DBUS\_MODEM\_ANTRR2](#a1913f830f7d6a4234ffb12e0701b0019)(0x3, 0x3) |
| #define | [MODEM\_ANTRR3\_PC0](#a2fa9d157e9749343083524dcddd1f1d1)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x0) |
| #define | [MODEM\_ANTRR3\_PC1](#a8c1d56d6692fefbffd9ca60e9f6d45ac)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x1) |
| #define | [MODEM\_ANTRR3\_PC2](#a678e2cb9f2ac53e8630a25bec6841fd0)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x2) |
| #define | [MODEM\_ANTRR3\_PC3](#a4b8cd19ab9ff53e0b51ffcf6beea247b)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x3) |
| #define | [MODEM\_ANTRR3\_PC4](#ab4586b72a654c124f6c5c7097c9902c7)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x4) |
| #define | [MODEM\_ANTRR3\_PC5](#abc7d9d9c03ae387c0a3b028f09858b79)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x5) |
| #define | [MODEM\_ANTRR3\_PC6](#a28641556808bb4359216027d35cb3e6c)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x6) |
| #define | [MODEM\_ANTRR3\_PC7](#aec4c5821f3a602b6a15d6861bb116f22)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x2, 0x7) |
| #define | [MODEM\_ANTRR3\_PD0](#a3fb63d9e07fc0c63605bde31a8288b57)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x3, 0x0) |
| #define | [MODEM\_ANTRR3\_PD1](#ae8e6d95bcc501a226c2ae7cf26974ae4)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x3, 0x1) |
| #define | [MODEM\_ANTRR3\_PD2](#a203100da0081cb15ba56e28b13164d2e)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x3, 0x2) |
| #define | [MODEM\_ANTRR3\_PD3](#af02994437b5f5b545ddf48b4adb1b475)   [SILABS\_DBUS\_MODEM\_ANTRR3](#ab9c8e475b9d5d1a9dae206aaa9b639b1)(0x3, 0x3) |
| #define | [MODEM\_ANTRR4\_PC0](#ac9f090be13e72088bb72bf1c75094e76)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x0) |
| #define | [MODEM\_ANTRR4\_PC1](#ac4ed6ce8ae1be803f08f5fe066521cc9)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x1) |
| #define | [MODEM\_ANTRR4\_PC2](#af477f9423d354cfb59ab51fdd086cce2)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x2) |
| #define | [MODEM\_ANTRR4\_PC3](#a21f70b645f9642fb79fe2646384dfb62)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x3) |
| #define | [MODEM\_ANTRR4\_PC4](#aee6646a5a12bad19280806cd1e805cc3)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x4) |
| #define | [MODEM\_ANTRR4\_PC5](#a82cbd5d4704cd282a9cbae9109505066)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x5) |
| #define | [MODEM\_ANTRR4\_PC6](#a2cf72bdc82e898d02a4d50f8e25e764f)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x6) |
| #define | [MODEM\_ANTRR4\_PC7](#ab58e49c260c123e08f8d59f1c309560b)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x2, 0x7) |
| #define | [MODEM\_ANTRR4\_PD0](#a10f6578c47953ee7d5f052e9726ee8d3)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x3, 0x0) |
| #define | [MODEM\_ANTRR4\_PD1](#ad4adb3ecb506a24bf919c524513a913c)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x3, 0x1) |
| #define | [MODEM\_ANTRR4\_PD2](#ad2ab7abbd3e49703350ae7be2d2e01b8)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x3, 0x2) |
| #define | [MODEM\_ANTRR4\_PD3](#a815940c71002bc123b8b48ac6c5cda20)   [SILABS\_DBUS\_MODEM\_ANTRR4](#a8da1060fdb49bad378f130183b73dd13)(0x3, 0x3) |
| #define | [MODEM\_ANTRR5\_PC0](#aa59209d310467981d68fc8ec63856bc6)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x0) |
| #define | [MODEM\_ANTRR5\_PC1](#ae28a87908fd594ba99d726c7cd56f348)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x1) |
| #define | [MODEM\_ANTRR5\_PC2](#a51d8ba60291e9f51cc34f5826b07a336)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x2) |
| #define | [MODEM\_ANTRR5\_PC3](#a4760c7eeb47e12e62db8fac47e779c05)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x3) |
| #define | [MODEM\_ANTRR5\_PC4](#ad723f7203c93c76019adb70110860402)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x4) |
| #define | [MODEM\_ANTRR5\_PC5](#a71833f446bf584b32654327734733059)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x5) |
| #define | [MODEM\_ANTRR5\_PC6](#a8c24d68ddf4c4b644781781ed0af0f0f)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x6) |
| #define | [MODEM\_ANTRR5\_PC7](#aa599783a6852570f4719190d992eff58)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x2, 0x7) |
| #define | [MODEM\_ANTRR5\_PD0](#a404392cc5769ad92662f7448e6458d05)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x3, 0x0) |
| #define | [MODEM\_ANTRR5\_PD1](#a88da3eca1fcd6f67c5a0c9e590c78dcf)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x3, 0x1) |
| #define | [MODEM\_ANTRR5\_PD2](#a6f6234ac85f4a3e3095672b20cd2f636)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x3, 0x2) |
| #define | [MODEM\_ANTRR5\_PD3](#a32dc3957baa49edb10e49d5914b46c14)   [SILABS\_DBUS\_MODEM\_ANTRR5](#aab2d172c20010568167c80096a97da23)(0x3, 0x3) |
| #define | [MODEM\_ANTSWEN\_PC0](#a93c921b96501eca162c6eee962c60f57)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x0) |
| #define | [MODEM\_ANTSWEN\_PC1](#ac4ceffe68747645a764487912dc1ac16)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x1) |
| #define | [MODEM\_ANTSWEN\_PC2](#ace5d141a804e6f73e77a0fcff81e4c56)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x2) |
| #define | [MODEM\_ANTSWEN\_PC3](#a1e59daa60e50af30180144363f4f1300)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x3) |
| #define | [MODEM\_ANTSWEN\_PC4](#a2a7fa90f1a78c16a6e6cad15ff2183f0)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x4) |
| #define | [MODEM\_ANTSWEN\_PC5](#aa7767d9a2806a0843c892fddcacd7600)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x5) |
| #define | [MODEM\_ANTSWEN\_PC6](#ae3c784f6e183cadf0dee817c5b9ba192)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x6) |
| #define | [MODEM\_ANTSWEN\_PC7](#aa8ac7404cee302c171ed8646e8573a8a)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x2, 0x7) |
| #define | [MODEM\_ANTSWEN\_PD0](#a6910c237541dc3d1d3c6a658aa259bb0)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x3, 0x0) |
| #define | [MODEM\_ANTSWEN\_PD1](#ab91df7c7ff2dd05a15844f0b223a4a9e)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x3, 0x1) |
| #define | [MODEM\_ANTSWEN\_PD2](#a5df0df918051e5a4c530c3b46c328e5f)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x3, 0x2) |
| #define | [MODEM\_ANTSWEN\_PD3](#aed4a6536e2515502a852bb782730081f)   [SILABS\_DBUS\_MODEM\_ANTSWEN](#a7af41447a0035cf8fb73804c40eb3502)(0x3, 0x3) |
| #define | [MODEM\_ANTSWUS\_PC0](#a35403ecde9ec6d51d0647558624c1755)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x0) |
| #define | [MODEM\_ANTSWUS\_PC1](#ac302424df9d075a5546b11e3a2f5a362)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x1) |
| #define | [MODEM\_ANTSWUS\_PC2](#a4c756e71ee82c7fbe41ec5ba5b33a0bd)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x2) |
| #define | [MODEM\_ANTSWUS\_PC3](#aff74d3e1d4ae4fd44a05f4d291a1f550)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x3) |
| #define | [MODEM\_ANTSWUS\_PC4](#af73c92cf63826be7cc6a1fe3e03b181d)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x4) |
| #define | [MODEM\_ANTSWUS\_PC5](#a294c8a1ce79d365a9d29717db3942107)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x5) |
| #define | [MODEM\_ANTSWUS\_PC6](#afad4a0c9a58b16b48cb06279fd7db652)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x6) |
| #define | [MODEM\_ANTSWUS\_PC7](#a6f86a2ef7edfbe782b7700efae544a48)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x2, 0x7) |
| #define | [MODEM\_ANTSWUS\_PD0](#aa47c88d6d4e2cc38e891b7e03e699756)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x3, 0x0) |
| #define | [MODEM\_ANTSWUS\_PD1](#a72a8e4b8a5ac8c3fe74eb26cd08e312b)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x3, 0x1) |
| #define | [MODEM\_ANTSWUS\_PD2](#a6852ed7e65ee6e22f96ecddbe0bcc05d)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x3, 0x2) |
| #define | [MODEM\_ANTSWUS\_PD3](#ab3e009ff6d5427f43e9fbf4743098520)   [SILABS\_DBUS\_MODEM\_ANTSWUS](#ab828720727a5b918ca11b9ff3a119b44)(0x3, 0x3) |
| #define | [MODEM\_ANTTRIG\_PC0](#a0b75979323bdd89b0cc9d10469b0095c)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x0) |
| #define | [MODEM\_ANTTRIG\_PC1](#a93518da86e975b51c00c957f0bb95ab0)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x1) |
| #define | [MODEM\_ANTTRIG\_PC2](#a27622d1c3e77514a6c175f88ba67b2f6)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x2) |
| #define | [MODEM\_ANTTRIG\_PC3](#afe612f9d7068a7d8f3f27950a3db07e5)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x3) |
| #define | [MODEM\_ANTTRIG\_PC4](#aa4e5df434329d0121c13dc72c90c9c13)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x4) |
| #define | [MODEM\_ANTTRIG\_PC5](#a0c7cd91aef9412c36340e43a41b95fbe)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x5) |
| #define | [MODEM\_ANTTRIG\_PC6](#a6bbd8a93a130ac08292335b664803e3b)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x6) |
| #define | [MODEM\_ANTTRIG\_PC7](#a69b763a9d3a015481424995589a80c3f)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x2, 0x7) |
| #define | [MODEM\_ANTTRIG\_PD0](#abc60b310f524562dc1252fec0238dbdf)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x3, 0x0) |
| #define | [MODEM\_ANTTRIG\_PD1](#ac437bf9340d8c56595543e8de7b9157e)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x3, 0x1) |
| #define | [MODEM\_ANTTRIG\_PD2](#a6b33477ce6327abad3ce4bcbba3eec9a)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x3, 0x2) |
| #define | [MODEM\_ANTTRIG\_PD3](#a132e606271a453be558397a95d72c17e)   [SILABS\_DBUS\_MODEM\_ANTTRIG](#a548bcbbd7ee4b87c6611d4fdb348984e)(0x3, 0x3) |
| #define | [MODEM\_ANTTRIGSTOP\_PC0](#af7e05b86331a8d9c02cd27a4e2dc84b7)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x0) |
| #define | [MODEM\_ANTTRIGSTOP\_PC1](#aa658e7c0b2ec76108d710ce93e1d787a)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x1) |
| #define | [MODEM\_ANTTRIGSTOP\_PC2](#a9770ce38a0f236ecd2a7f6cd56e1eff4)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x2) |
| #define | [MODEM\_ANTTRIGSTOP\_PC3](#a61b3ce65ad555f6ad8b69a182626d90e)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x3) |
| #define | [MODEM\_ANTTRIGSTOP\_PC4](#a65384fc71c75bf574740388627bca46f)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x4) |
| #define | [MODEM\_ANTTRIGSTOP\_PC5](#a4c123cd5fca0b4e4e0bc79fbb77292f5)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x5) |
| #define | [MODEM\_ANTTRIGSTOP\_PC6](#a98d91dafafd9175fbdd1074e9526ceaf)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x6) |
| #define | [MODEM\_ANTTRIGSTOP\_PC7](#a26f49d68743f2c7df6e22be7354ffb7f)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x2, 0x7) |
| #define | [MODEM\_ANTTRIGSTOP\_PD0](#a2689b6b9d9286a13b7b6d2ead8c3993a)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x3, 0x0) |
| #define | [MODEM\_ANTTRIGSTOP\_PD1](#a09410c6d05c79937b0385a8552c292f2)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x3, 0x1) |
| #define | [MODEM\_ANTTRIGSTOP\_PD2](#a413c60ac3ae878a6e4e70e39c6c85fd9)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x3, 0x2) |
| #define | [MODEM\_ANTTRIGSTOP\_PD3](#a20053bb1092ce80cc23cd88aa88fc30d)   [SILABS\_DBUS\_MODEM\_ANTTRIGSTOP](#a07822fe9a1f6febeaf3745361b47d57b)(0x3, 0x3) |
| #define | [MODEM\_DCLK\_PA0](#a08ca0610796eea5484d295a978221196)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x0) |
| #define | [MODEM\_DCLK\_PA1](#a405e18321ac14727b470918f185f923c)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x1) |
| #define | [MODEM\_DCLK\_PA2](#a2e7d5bc810c26a1194a846663607762d)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x2) |
| #define | [MODEM\_DCLK\_PA3](#a483f89509d4d25fe14f3d8cff618289d)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x3) |
| #define | [MODEM\_DCLK\_PA4](#a8e3916287d03243cca904f41ce1f9dae)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x4) |
| #define | [MODEM\_DCLK\_PA5](#afd75314e866b5c47e838556d866d5883)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x5) |
| #define | [MODEM\_DCLK\_PA6](#acf3a1e4e5b714d53ff82edbf02575ec5)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x6) |
| #define | [MODEM\_DCLK\_PA7](#ab339753673d17ab957324821a8933d94)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x7) |
| #define | [MODEM\_DCLK\_PA8](#a4ffefd11c83ed290890ffb7657507a1e)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x0, 0x8) |
| #define | [MODEM\_DCLK\_PB0](#a19236a132524a68b08b88a2b71b74b7b)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x1, 0x0) |
| #define | [MODEM\_DCLK\_PB1](#a862abc8858bae8ba0af6b0f8fbbaae37)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x1, 0x1) |
| #define | [MODEM\_DCLK\_PB2](#aefcf9c6de61eb621830516b3de6cf348)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x1, 0x2) |
| #define | [MODEM\_DCLK\_PB3](#ad15e63bf8718d8705673620a730009c7)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x1, 0x3) |
| #define | [MODEM\_DCLK\_PB4](#a76a21531211dfe45e53ceae776c396b6)   [SILABS\_DBUS\_MODEM\_DCLK](#a7d3926059c8b0c608d6d2bce035555b6)(0x1, 0x4) |
| #define | [MODEM\_DOUT\_PA0](#ac3823581963866285b9f6143d16d9c38)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x0) |
| #define | [MODEM\_DOUT\_PA1](#ae4c319e1bba60e4a5a891edf88b1e968)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x1) |
| #define | [MODEM\_DOUT\_PA2](#a8dabb728396cf206afac2cfbe49a5b02)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x2) |
| #define | [MODEM\_DOUT\_PA3](#ae5963b1e2305ae53f11a90b0d76a99a3)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x3) |
| #define | [MODEM\_DOUT\_PA4](#a06061dfed7797c0e29bb9cb5a6d49f88)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x4) |
| #define | [MODEM\_DOUT\_PA5](#a117ead5a3ea011c4ad9d37fc96de2bba)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x5) |
| #define | [MODEM\_DOUT\_PA6](#aeda2e59bc16dda7ee3d83a2504a04f05)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x6) |
| #define | [MODEM\_DOUT\_PA7](#a1d0857025a77fb254ea0e2f7594471f5)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x7) |
| #define | [MODEM\_DOUT\_PA8](#a399d0cc64e37dbf683cbcacf14f2d870)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x0, 0x8) |
| #define | [MODEM\_DOUT\_PB0](#abe0c4060d5f35e9cf8e002676f3c238c)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x1, 0x0) |
| #define | [MODEM\_DOUT\_PB1](#aff30fef58eb6dbd17426f7e175c8f4ae)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x1, 0x1) |
| #define | [MODEM\_DOUT\_PB2](#ac013e04b2f5d3b419c24f2b1b7f27bad)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x1, 0x2) |
| #define | [MODEM\_DOUT\_PB3](#a9011320165978614b4933f9194d45892)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x1, 0x3) |
| #define | [MODEM\_DOUT\_PB4](#aabf2e613152cd24a321ad3711cc3c30e)   [SILABS\_DBUS\_MODEM\_DOUT](#a48c49cff2ed723238703ff1b75ba8ae7)(0x1, 0x4) |
| #define | [MODEM\_DIN\_PA0](#a3e0e16cfb9e9ad19a8e76e07e458d676)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x0) |
| #define | [MODEM\_DIN\_PA1](#a3770dcebe1ad3c30c3fbcdcc9e1e61ac)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x1) |
| #define | [MODEM\_DIN\_PA2](#aed7868ce54670b163ae60f645e353e10)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x2) |
| #define | [MODEM\_DIN\_PA3](#a55004a63d39356caf5bda66e005a25f3)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x3) |
| #define | [MODEM\_DIN\_PA4](#a1c13babd5d2f16d4d56257f847e84f40)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x4) |
| #define | [MODEM\_DIN\_PA5](#a4f09d7e3de2cde036a6ddfcfe35bc96a)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x5) |
| #define | [MODEM\_DIN\_PA6](#aa310c43126dfd99d7f967141340934c2)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x6) |
| #define | [MODEM\_DIN\_PA7](#a201de78e9064b3467b2bbdc0a93ae4b2)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x7) |
| #define | [MODEM\_DIN\_PA8](#a12d5bed446ee0a12698d247f187835ed)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x0, 0x8) |
| #define | [MODEM\_DIN\_PB0](#a87a115f7d2707bf513e218401f2d10fd)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x1, 0x0) |
| #define | [MODEM\_DIN\_PB1](#a4484f366718daefbdd23d72248a1ba0d)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x1, 0x1) |
| #define | [MODEM\_DIN\_PB2](#a9513dd16e152b54918b10a3ca7b2bddd)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x1, 0x2) |
| #define | [MODEM\_DIN\_PB3](#a4ff611638d1c08ae3412e8df31d45e2c)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x1, 0x3) |
| #define | [MODEM\_DIN\_PB4](#abfd0c609a7621aac4e345fa264776629)   [SILABS\_DBUS\_MODEM\_DIN](#a82dfdd0e9ad82ab0c75f4a530620d34b)(0x1, 0x4) |
| #define | [PDM\_CLK\_PA0](#a17da237abad4fa377fe34a56e22f7994)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x0, 0x0) |
| #define | [PDM\_CLK\_PA1](#a30ebd03a19f9811c314f8e1845f50ad9)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x0, 0x1) |
| #define | [PDM\_CLK\_PA2](#ae6adaa8523f3173e32239c4e9b9b2fd1)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x0, 0x2) |
| #define | [PDM\_CLK\_PA3](#acac34f27db1a3d2ec31df358674fa131)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x0, 0x3) |
| #define | [PDM\_CLK\_PA4](#ad37a0874cbe049c72632c6f2179d1cdd)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x0, 0x4) |
| #define | [PDM\_CLK\_PA5](#ae0e222d832684fced0532a4327496c25)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x0, 0x5) |
| #define | [PDM\_CLK\_PA6](#a065d9974c4f5a53dfa8f5f1671df9fc6)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x0, 0x6) |
| #define | [PDM\_CLK\_PA7](#ac5f913eea970639ecfcda0de352dcc43)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x0, 0x7) |
| #define | [PDM\_CLK\_PA8](#a73233d7b85b39f5acf81eb3bef623e73)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x0, 0x8) |
| #define | [PDM\_CLK\_PB0](#a16c0497c54578a79b86dc789c748fee2)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x1, 0x0) |
| #define | [PDM\_CLK\_PB1](#a14417c07902532890f54f8fe21b0956c)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x1, 0x1) |
| #define | [PDM\_CLK\_PB2](#ad925c34c175014c7c07358549323dbe4)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x1, 0x2) |
| #define | [PDM\_CLK\_PB3](#a0826c43ece683f511bc3dbf27fc01927)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x1, 0x3) |
| #define | [PDM\_CLK\_PB4](#a5c6d93cd903d7c780ecda20bcec72ac4)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x1, 0x4) |
| #define | [PDM\_CLK\_PC0](#a1750f23968b042aae8205a9e45334734)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x2, 0x0) |
| #define | [PDM\_CLK\_PC1](#a634829cbe2f8f494a5e4c3d747199a67)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x2, 0x1) |
| #define | [PDM\_CLK\_PC2](#a4a0059bd0b5be4ac96db3482f8407ebf)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x2, 0x2) |
| #define | [PDM\_CLK\_PC3](#a6bd1bc850a90979bb7c36e129c3d39a2)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x2, 0x3) |
| #define | [PDM\_CLK\_PC4](#afa3f9103181ab9b8b26495125e3991f5)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x2, 0x4) |
| #define | [PDM\_CLK\_PC5](#a383f7fe2d6f1385986dc08d1342bdbae)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x2, 0x5) |
| #define | [PDM\_CLK\_PC6](#a3864b096ca291ed4ce6e2e609384d297)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x2, 0x6) |
| #define | [PDM\_CLK\_PC7](#a45db6fe2c22dddb9c131b81a51a265e1)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x2, 0x7) |
| #define | [PDM\_CLK\_PD0](#ae0bd60a7a78c4eb57f276cf1f6f478be)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x3, 0x0) |
| #define | [PDM\_CLK\_PD1](#a3331b3b655dca5f27eda7b9a5edec57e)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x3, 0x1) |
| #define | [PDM\_CLK\_PD2](#a59e99a2875165982fb12ec8e71bea000)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x3, 0x2) |
| #define | [PDM\_CLK\_PD3](#a1c2cb950f01e7c29dbd16dc9b73ce497)   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x3, 0x3) |
| #define | [PDM\_DAT0\_PA0](#a8076cde51878a20f5391bc3c7844dab3)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x0, 0x0) |
| #define | [PDM\_DAT0\_PA1](#ac7a9f1aca581e062a433809395238812)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x0, 0x1) |
| #define | [PDM\_DAT0\_PA2](#a7e9a14ddb5e3c79831635d8ab4634fd1)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x0, 0x2) |
| #define | [PDM\_DAT0\_PA3](#a361db81d9510397b97d471b85d293247)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x0, 0x3) |
| #define | [PDM\_DAT0\_PA4](#ae8827de80cb0f00b7c0c28897a446672)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x0, 0x4) |
| #define | [PDM\_DAT0\_PA5](#af1c2f379b0dd1b5b5c2f0dcc02e66a18)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x0, 0x5) |
| #define | [PDM\_DAT0\_PA6](#adc98dacaec34e0bc7b5111cf4a5cae6a)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x0, 0x6) |
| #define | [PDM\_DAT0\_PA7](#a10f7155fb07e6ee74db22f4982a3386e)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x0, 0x7) |
| #define | [PDM\_DAT0\_PA8](#acefda5f922c7fd820079fbe3596a76f5)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x0, 0x8) |
| #define | [PDM\_DAT0\_PB0](#a1aaf675c35776b909986481ed0e9cac0)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x1, 0x0) |
| #define | [PDM\_DAT0\_PB1](#a2813b125ed458746140490ac24fd4326)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x1, 0x1) |
| #define | [PDM\_DAT0\_PB2](#a6fa34019aa25bdfa705139c8f0d9d826)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x1, 0x2) |
| #define | [PDM\_DAT0\_PB3](#aeb3b2a38f75a2db5f032ef21314a0ea0)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x1, 0x3) |
| #define | [PDM\_DAT0\_PB4](#a8453dd053f8278aca863c3033a8b29d4)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x1, 0x4) |
| #define | [PDM\_DAT0\_PC0](#ab9987b7a24c8195e35e0ca238817fe6b)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x2, 0x0) |
| #define | [PDM\_DAT0\_PC1](#a1db5ed56336a70d82c2f88b11dc5ae3c)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x2, 0x1) |
| #define | [PDM\_DAT0\_PC2](#a4ce1e6985c2e168c0d8f2ce76fd7b53a)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x2, 0x2) |
| #define | [PDM\_DAT0\_PC3](#a5855f905cdc824df96bc5c41ea492242)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x2, 0x3) |
| #define | [PDM\_DAT0\_PC4](#a12991c4bb5704770a3ec24d470a7de41)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x2, 0x4) |
| #define | [PDM\_DAT0\_PC5](#a746f9df3b772fb53bed1c3745b902dc8)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x2, 0x5) |
| #define | [PDM\_DAT0\_PC6](#a7a59060917dac0ed6a379c29d5ccd355)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x2, 0x6) |
| #define | [PDM\_DAT0\_PC7](#a5348f9e1d87746a8a98cb87b4df64937)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x2, 0x7) |
| #define | [PDM\_DAT0\_PD0](#acf90e3c92b6cb54e783c14578df6dea0)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x3, 0x0) |
| #define | [PDM\_DAT0\_PD1](#a62b3aa330ecbeb720ea654edb6b70c4d)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x3, 0x1) |
| #define | [PDM\_DAT0\_PD2](#aeaee63c71a856370c07ad40f1f9c099e)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x3, 0x2) |
| #define | [PDM\_DAT0\_PD3](#a888efdeb39811dd330592978fcec4f63)   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x3, 0x3) |
| #define | [PDM\_DAT1\_PA0](#a2e9b856688c2d8eadb9283adb15d07ec)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x0, 0x0) |
| #define | [PDM\_DAT1\_PA1](#ac33beea0c269de70b662a58cfd10c25e)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x0, 0x1) |
| #define | [PDM\_DAT1\_PA2](#a336bbd623362b37e192eea1ec8da1315)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x0, 0x2) |
| #define | [PDM\_DAT1\_PA3](#a712778b19527024cca05630251103095)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x0, 0x3) |
| #define | [PDM\_DAT1\_PA4](#ad59e6a2f0c431fdfa8a2aad9d0ee12ca)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x0, 0x4) |
| #define | [PDM\_DAT1\_PA5](#aa880de680c84604c10a15c80fc592aa3)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x0, 0x5) |
| #define | [PDM\_DAT1\_PA6](#a999ce72cee2c3c5bdab055dba6008cf9)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x0, 0x6) |
| #define | [PDM\_DAT1\_PA7](#a3a7ba5e8b55bf168b9250d0e1a7c992b)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x0, 0x7) |
| #define | [PDM\_DAT1\_PA8](#aad4d4f8b8548163442aa489af3f3ccd8)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x0, 0x8) |
| #define | [PDM\_DAT1\_PB0](#a79b1395b0600a359ccf7168741e159a7)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x1, 0x0) |
| #define | [PDM\_DAT1\_PB1](#a4f3fe9e22ab662d160fd385583c32980)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x1, 0x1) |
| #define | [PDM\_DAT1\_PB2](#a20aac187e72e0d127453b2201ec38aab)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x1, 0x2) |
| #define | [PDM\_DAT1\_PB3](#a245af246ec5bb7545b44e46291a5407f)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x1, 0x3) |
| #define | [PDM\_DAT1\_PB4](#ad55ee30074e511e8e38fcbf298f4b573)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x1, 0x4) |
| #define | [PDM\_DAT1\_PC0](#a766b87b6f397b34821ee6c3da39313ae)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x2, 0x0) |
| #define | [PDM\_DAT1\_PC1](#ab8beb7afd902e3726167ba905dfc4920)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x2, 0x1) |
| #define | [PDM\_DAT1\_PC2](#a03dd4fdb93626d4849bedc2e14a69e5a)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x2, 0x2) |
| #define | [PDM\_DAT1\_PC3](#a0d42cfb3c8a3f7ffc56f61ffee0339c3)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x2, 0x3) |
| #define | [PDM\_DAT1\_PC4](#af1131ca951092591193e95b4b6740b43)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x2, 0x4) |
| #define | [PDM\_DAT1\_PC5](#aadeb4540d495a19ecb989ac61fedeb6e)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x2, 0x5) |
| #define | [PDM\_DAT1\_PC6](#acbeec6663ffc7b4c265ae1fac2e6b585)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x2, 0x6) |
| #define | [PDM\_DAT1\_PC7](#a653a61290ca92e497c920de5c9baab3d)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x2, 0x7) |
| #define | [PDM\_DAT1\_PD0](#aa64a2b39a12d19f074cf30fd37746640)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x3, 0x0) |
| #define | [PDM\_DAT1\_PD1](#a419241477ba85a002471be3bfc6a0b5c)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x3, 0x1) |
| #define | [PDM\_DAT1\_PD2](#afa2865841cb633083f38aa4492bcf107)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x3, 0x2) |
| #define | [PDM\_DAT1\_PD3](#aaef465d544e19e6a5fea47a23cfa75c5)   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x3, 0x3) |
| #define | [PRS0\_ASYNCH0\_PA0](#af1dcdc8d0ea9b8671a240ce03d80d434)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x0) |
| #define | [PRS0\_ASYNCH0\_PA1](#af712c40bafb6ba29d062f47a47ef4445)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x1) |
| #define | [PRS0\_ASYNCH0\_PA2](#a4a95bfd98958b7944ef58c010df91d83)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x2) |
| #define | [PRS0\_ASYNCH0\_PA3](#ab912f56311db65e5316e921180f46589)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x3) |
| #define | [PRS0\_ASYNCH0\_PA4](#ac1e05749654ec2bee09aa75a951bcd57)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x4) |
| #define | [PRS0\_ASYNCH0\_PA5](#a15788b1a1cdce57fddf0d58e884e37bc)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x5) |
| #define | [PRS0\_ASYNCH0\_PA6](#af071c0ad0ca5a54d74c7fa4e2f7eea6c)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x6) |
| #define | [PRS0\_ASYNCH0\_PA7](#accc5ad5ffa51459772c03387f67f6db1)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x7) |
| #define | [PRS0\_ASYNCH0\_PA8](#af170d0ff0c56bdf3bd13eaa00f2f3fea)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x0, 0x8) |
| #define | [PRS0\_ASYNCH0\_PB0](#a590472d980647bc2a513ee516c9c4f1b)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x1, 0x0) |
| #define | [PRS0\_ASYNCH0\_PB1](#af4ee1a5d6ccadd510de798cf41f973ee)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x1, 0x1) |
| #define | [PRS0\_ASYNCH0\_PB2](#a0517d6b5213d9f8ebfb445e7aa0cf2e7)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x1, 0x2) |
| #define | [PRS0\_ASYNCH0\_PB3](#a0b229da2aec9ffb51c50e0ca19e1a45d)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x1, 0x3) |
| #define | [PRS0\_ASYNCH0\_PB4](#a281aa5d676ea7ac358df567ab98663b3)   [SILABS\_DBUS\_PRS0\_ASYNCH0](#a55a10636beb81ba5bf195c83c45cc994)(0x1, 0x4) |
| #define | [PRS0\_ASYNCH1\_PA0](#aa7c8c749fddaf4b2e22e3791d9e8921a)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x0) |
| #define | [PRS0\_ASYNCH1\_PA1](#a8f998569835e3b8688423cf9b4e81810)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x1) |
| #define | [PRS0\_ASYNCH1\_PA2](#a5f2d980e4505820849c42fdc36c1b5a9)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x2) |
| #define | [PRS0\_ASYNCH1\_PA3](#a4b66d13c4589bb2663661e6cfb8c0274)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x3) |
| #define | [PRS0\_ASYNCH1\_PA4](#aec6f34dc1716b25b0fcc0628b18cbf86)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x4) |
| #define | [PRS0\_ASYNCH1\_PA5](#a0be6148e1124f7e8dc6773f59dfd8ceb)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x5) |
| #define | [PRS0\_ASYNCH1\_PA6](#a4d1894b5f84e0e7c81a5dbb2bfe8318f)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x6) |
| #define | [PRS0\_ASYNCH1\_PA7](#a95455187a1575a8e8249d1e4178131c5)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x7) |
| #define | [PRS0\_ASYNCH1\_PA8](#a85428a0cef95ef5674719cfbac44eed5)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x0, 0x8) |
| #define | [PRS0\_ASYNCH1\_PB0](#a76487417602321711041f2d5d721e8ae)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x1, 0x0) |
| #define | [PRS0\_ASYNCH1\_PB1](#a1626bdc4551620aaccbfacd8aa0c0cdf)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x1, 0x1) |
| #define | [PRS0\_ASYNCH1\_PB2](#ac68d7c6b3b4607a2eb07926ceb42b0b3)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x1, 0x2) |
| #define | [PRS0\_ASYNCH1\_PB3](#a5b843903080dcfb8d654248f04b56bb1)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x1, 0x3) |
| #define | [PRS0\_ASYNCH1\_PB4](#ae1a66f7dff2089736cc20cee277a5cd4)   [SILABS\_DBUS\_PRS0\_ASYNCH1](#a8502ee8adb62210f0c02abdf38a54019)(0x1, 0x4) |
| #define | [PRS0\_ASYNCH2\_PA0](#ab9115b54fff36f0449722af1659860fb)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x0) |
| #define | [PRS0\_ASYNCH2\_PA1](#a82e86536168f11e5b02c4fac703128b1)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x1) |
| #define | [PRS0\_ASYNCH2\_PA2](#af3124f46d26efbb18047172d5d5accbc)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x2) |
| #define | [PRS0\_ASYNCH2\_PA3](#a57857d486b2fc1db0770a7d1e198ed95)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x3) |
| #define | [PRS0\_ASYNCH2\_PA4](#a3d91108c838d4684846d56816aee5fe1)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x4) |
| #define | [PRS0\_ASYNCH2\_PA5](#a8e7b151ff1870ccfc66a34096b4aebae)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x5) |
| #define | [PRS0\_ASYNCH2\_PA6](#a7f536e8d1d66285820ab8e3808e49a0f)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x6) |
| #define | [PRS0\_ASYNCH2\_PA7](#a41efde6eb746e07baf306e05197a8948)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x7) |
| #define | [PRS0\_ASYNCH2\_PA8](#a95b452fe92602af5bff499d14f1cae11)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x0, 0x8) |
| #define | [PRS0\_ASYNCH2\_PB0](#a81bf0662053265b1d9cc03c101d4a353)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x1, 0x0) |
| #define | [PRS0\_ASYNCH2\_PB1](#a026322616f156126afcbcebc25d104c0)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x1, 0x1) |
| #define | [PRS0\_ASYNCH2\_PB2](#a6a39b350109c932587f1c1623898d178)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x1, 0x2) |
| #define | [PRS0\_ASYNCH2\_PB3](#a30b84121b903ca053238c3a1110fd247)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x1, 0x3) |
| #define | [PRS0\_ASYNCH2\_PB4](#a68e5aa33a7ccd7af8abe83550bc9fcf2)   [SILABS\_DBUS\_PRS0\_ASYNCH2](#a8065a08661b02239f79db443c11afac8)(0x1, 0x4) |
| #define | [PRS0\_ASYNCH3\_PA0](#a94b5b779374768ed16ad8cc396f756aa)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x0) |
| #define | [PRS0\_ASYNCH3\_PA1](#aa947bb280b4891081e7a4de9dba44ae5)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x1) |
| #define | [PRS0\_ASYNCH3\_PA2](#a9bc4d14c37fd2724643735c13cc9a25d)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x2) |
| #define | [PRS0\_ASYNCH3\_PA3](#afa101472245a7df51d906f31093ce640)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x3) |
| #define | [PRS0\_ASYNCH3\_PA4](#a1e433ac2a9a5c1b9240b157033e8fdc1)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x4) |
| #define | [PRS0\_ASYNCH3\_PA5](#a4af0e3dc3303ec055fcce97399ccf4ba)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x5) |
| #define | [PRS0\_ASYNCH3\_PA6](#ad905e3cca4ec1b92f1fd6b0ca18b8c06)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x6) |
| #define | [PRS0\_ASYNCH3\_PA7](#a64d14cae622fb5814402d3bf6c042a47)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x7) |
| #define | [PRS0\_ASYNCH3\_PA8](#a0ceb4585c15bf959906dd93aed744f0d)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x0, 0x8) |
| #define | [PRS0\_ASYNCH3\_PB0](#a5cb1e7fbb39adfdfca2516715f0cc1ac)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x1, 0x0) |
| #define | [PRS0\_ASYNCH3\_PB1](#aa09fe8bc9d5c277db64c0912b55e9651)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x1, 0x1) |
| #define | [PRS0\_ASYNCH3\_PB2](#a8fd4c8b45bb5366691e3ea98b20ca580)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x1, 0x2) |
| #define | [PRS0\_ASYNCH3\_PB3](#a92ac18184efd55f90aecf9763b1d93b9)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x1, 0x3) |
| #define | [PRS0\_ASYNCH3\_PB4](#a3b96ce5680cf373ff511249aec0d4ea3)   [SILABS\_DBUS\_PRS0\_ASYNCH3](#a39cb285c6310012108f37d510db7a86c)(0x1, 0x4) |
| #define | [PRS0\_ASYNCH4\_PA0](#a016d312ee53e23e053e5322038c218e8)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x0) |
| #define | [PRS0\_ASYNCH4\_PA1](#ac08b73b2d1c8340a46b2b4321d258bbf)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x1) |
| #define | [PRS0\_ASYNCH4\_PA2](#a6d468079dce68ad1a80a09411eed3c61)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x2) |
| #define | [PRS0\_ASYNCH4\_PA3](#a2901f5a1abe787afaaf8c04a6aafa57f)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x3) |
| #define | [PRS0\_ASYNCH4\_PA4](#a599e583eb87879b76f1a889093ca1db7)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x4) |
| #define | [PRS0\_ASYNCH4\_PA5](#a50cd729844356a327a34588ab70c9f51)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x5) |
| #define | [PRS0\_ASYNCH4\_PA6](#a15672ea11df2224289fc84c07abddbce)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x6) |
| #define | [PRS0\_ASYNCH4\_PA7](#a765447cc275c70881ae23b795c7fc53c)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x7) |
| #define | [PRS0\_ASYNCH4\_PA8](#a9ce8837d29bbd43cf040ade45311b569)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x0, 0x8) |
| #define | [PRS0\_ASYNCH4\_PB0](#ab0da5394e8fceec3a24c8ca362a6a73f)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x1, 0x0) |
| #define | [PRS0\_ASYNCH4\_PB1](#a95e9e61ebc91932e32cf3683ba99beb7)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x1, 0x1) |
| #define | [PRS0\_ASYNCH4\_PB2](#a9b7b2081e0a38e0e6ab9f2d3ca3654d8)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x1, 0x2) |
| #define | [PRS0\_ASYNCH4\_PB3](#a0516f5991ffed91ba799d6d463f05945)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x1, 0x3) |
| #define | [PRS0\_ASYNCH4\_PB4](#a8b217bac132dc7c18930e4fe8c4e58db)   [SILABS\_DBUS\_PRS0\_ASYNCH4](#ac419288481edbfee2df8711b0c037ba2)(0x1, 0x4) |
| #define | [PRS0\_ASYNCH5\_PA0](#a6cac49a6aeefd56ad4ba7e4cba8910bf)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x0) |
| #define | [PRS0\_ASYNCH5\_PA1](#a8442fb1410b80fcd20c78b7cc44608eb)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x1) |
| #define | [PRS0\_ASYNCH5\_PA2](#aa3e3bbc87f46c7f0b9016518266e1fb2)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x2) |
| #define | [PRS0\_ASYNCH5\_PA3](#a269678c70e29d05e9d67b82b1d5dcfd2)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x3) |
| #define | [PRS0\_ASYNCH5\_PA4](#a7a314bb07eab261a850420ac2d6a2618)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x4) |
| #define | [PRS0\_ASYNCH5\_PA5](#ac01e6bde894c73d5e965b7fe6ed03f53)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x5) |
| #define | [PRS0\_ASYNCH5\_PA6](#ae3d6e3ae9d6d9d7c41ca233ad101b025)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x6) |
| #define | [PRS0\_ASYNCH5\_PA7](#a769160beeaa4ca59cae64a1c61b5c90e)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x7) |
| #define | [PRS0\_ASYNCH5\_PA8](#a7485b4e8b8b2eca4594481533f547997)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x0, 0x8) |
| #define | [PRS0\_ASYNCH5\_PB0](#adb08d0b33060e185431fb336110899c9)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x1, 0x0) |
| #define | [PRS0\_ASYNCH5\_PB1](#a82b599c4956aeea92802694032b4b55a)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x1, 0x1) |
| #define | [PRS0\_ASYNCH5\_PB2](#a26b4fa1b83e7857071e5f5d434055a6a)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x1, 0x2) |
| #define | [PRS0\_ASYNCH5\_PB3](#a0fbf5258e9f5d24e164a31dbdb40443e)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x1, 0x3) |
| #define | [PRS0\_ASYNCH5\_PB4](#a7de3a9532a4e4fdf5380046737950e18)   [SILABS\_DBUS\_PRS0\_ASYNCH5](#a6d7577bd45bc2c6043463ef6df86e8a7)(0x1, 0x4) |
| #define | [PRS0\_ASYNCH6\_PC0](#a5c7910d134b9fe6ddf1da299dfb2cfa0)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x0) |
| #define | [PRS0\_ASYNCH6\_PC1](#a713321693f2cfd7cda27d1c36fc9b74b)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x1) |
| #define | [PRS0\_ASYNCH6\_PC2](#a907d3ee7390b6ebcb5cac75724b6c587)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x2) |
| #define | [PRS0\_ASYNCH6\_PC3](#a5eebd47a62e87b938b530113cd048481)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x3) |
| #define | [PRS0\_ASYNCH6\_PC4](#a2d0d89b1abadc95ec02a88916330bab4)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x4) |
| #define | [PRS0\_ASYNCH6\_PC5](#aaa44b81b3421197bff7df84a5e90a566)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x5) |
| #define | [PRS0\_ASYNCH6\_PC6](#aaeaba294a765ca9892f4591acb3dd83e)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x6) |
| #define | [PRS0\_ASYNCH6\_PC7](#a0d95bb763b051fb232dc8805ad6d643e)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x2, 0x7) |
| #define | [PRS0\_ASYNCH6\_PD0](#a0db829680023f49ec8b84b8418994f57)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x3, 0x0) |
| #define | [PRS0\_ASYNCH6\_PD1](#a41989b05cfd244afef8a6c359de6f6cb)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x3, 0x1) |
| #define | [PRS0\_ASYNCH6\_PD2](#ad70491288162b935edc6602844fbad73)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x3, 0x2) |
| #define | [PRS0\_ASYNCH6\_PD3](#a03cdfe05c93c94a99e457fc34be7adb3)   [SILABS\_DBUS\_PRS0\_ASYNCH6](#afa3017107df002534d41165b790891dd)(0x3, 0x3) |
| #define | [PRS0\_ASYNCH7\_PC0](#a263dcb3077d0d1e3a58730140042046d)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x0) |
| #define | [PRS0\_ASYNCH7\_PC1](#aa49bafce35b9bb4b59c8c9c22f06a739)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x1) |
| #define | [PRS0\_ASYNCH7\_PC2](#ae0305282eab2df6979c235c8d5d00ac7)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x2) |
| #define | [PRS0\_ASYNCH7\_PC3](#a05355f9a968579fd8a931b7458d37960)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x3) |
| #define | [PRS0\_ASYNCH7\_PC4](#acb9a2a6531dd263cfe56858aa9c77791)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x4) |
| #define | [PRS0\_ASYNCH7\_PC5](#af504334eb99bab375e929f662ee6091a)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x5) |
| #define | [PRS0\_ASYNCH7\_PC6](#a770b593af51ec2f1fae3694e1a29cdef)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x6) |
| #define | [PRS0\_ASYNCH7\_PC7](#a96d44dd7e3fb6c4a68e5c2f029d0e3d4)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x2, 0x7) |
| #define | [PRS0\_ASYNCH7\_PD0](#a4e38e496fe8a602726a9fcfac5c9553b)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x3, 0x0) |
| #define | [PRS0\_ASYNCH7\_PD1](#a8a5617fb6a01d979b5754bb30438ef11)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x3, 0x1) |
| #define | [PRS0\_ASYNCH7\_PD2](#ae44270558459c4a31a9d8db2216b6a47)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x3, 0x2) |
| #define | [PRS0\_ASYNCH7\_PD3](#a19e5fc23eb4c5edbe4cc2be54508038a)   [SILABS\_DBUS\_PRS0\_ASYNCH7](#ae5af1968989cc643d315e310eb840dcc)(0x3, 0x3) |
| #define | [PRS0\_ASYNCH8\_PC0](#a01aee008d4ae0969e81630224253732c)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x0) |
| #define | [PRS0\_ASYNCH8\_PC1](#a1020e0f439015d77aad3a4ad6761745f)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x1) |
| #define | [PRS0\_ASYNCH8\_PC2](#a78ac7a7a23787837c2d45b7fb619d973)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x2) |
| #define | [PRS0\_ASYNCH8\_PC3](#a21d56ee2bba901bb0ad42fe00fd47126)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x3) |
| #define | [PRS0\_ASYNCH8\_PC4](#ab38e8e6ebf5f7b8cf9db913835c77fdf)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x4) |
| #define | [PRS0\_ASYNCH8\_PC5](#a034b8fafc8f80d4aa749ace8d383aa42)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x5) |
| #define | [PRS0\_ASYNCH8\_PC6](#a9b6282a03652ffd9886abf001018942e)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x6) |
| #define | [PRS0\_ASYNCH8\_PC7](#a7a33bde9021e0d8f1a4c331064369169)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x2, 0x7) |
| #define | [PRS0\_ASYNCH8\_PD0](#a3c4c1e1e2ed6aad821543605099c464e)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x3, 0x0) |
| #define | [PRS0\_ASYNCH8\_PD1](#a7a96c3dddcf49a09ab3941a19e33dd2b)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x3, 0x1) |
| #define | [PRS0\_ASYNCH8\_PD2](#a045129ec46f95f26ba665876216df09a)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x3, 0x2) |
| #define | [PRS0\_ASYNCH8\_PD3](#abf899559efdca73abc5e1f3e058280dc)   [SILABS\_DBUS\_PRS0\_ASYNCH8](#a0d062ef8d1ababa72b60d08265ff7e25)(0x3, 0x3) |
| #define | [PRS0\_ASYNCH9\_PC0](#ad6900f2865fce19423ba5bce65e6f6ec)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x0) |
| #define | [PRS0\_ASYNCH9\_PC1](#a21a22ddcc1d1b8c05250ea00bfaf2c46)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x1) |
| #define | [PRS0\_ASYNCH9\_PC2](#a7dcb713d1f7f8457e30812454272c360)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x2) |
| #define | [PRS0\_ASYNCH9\_PC3](#ac6eeb711fa526a794104a43142cedc8d)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x3) |
| #define | [PRS0\_ASYNCH9\_PC4](#a87ada6898e2eeddcaeead80835a3800b)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x4) |
| #define | [PRS0\_ASYNCH9\_PC5](#a6b5b3ca2088cb2c43fbebf99cd4e9ad3)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x5) |
| #define | [PRS0\_ASYNCH9\_PC6](#a4383c5af531fd312831c4116e60bec7e)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x6) |
| #define | [PRS0\_ASYNCH9\_PC7](#a59c911b1c45a061480e83d081796f84b)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x2, 0x7) |
| #define | [PRS0\_ASYNCH9\_PD0](#a89cd80ad72079b3a20917cc722fed3c3)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x3, 0x0) |
| #define | [PRS0\_ASYNCH9\_PD1](#aa9433d94ee912ff578dc1f3753bca9b5)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x3, 0x1) |
| #define | [PRS0\_ASYNCH9\_PD2](#a1dfa38b0754566f3586712b7474ce13f)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x3, 0x2) |
| #define | [PRS0\_ASYNCH9\_PD3](#a48c2477430954a1f5ebefcd625132b34)   [SILABS\_DBUS\_PRS0\_ASYNCH9](#af0617799b4044665a4996276fcf1e2bf)(0x3, 0x3) |
| #define | [PRS0\_ASYNCH10\_PC0](#af096e7ffddaaf21a0886246861e94cf0)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x0) |
| #define | [PRS0\_ASYNCH10\_PC1](#ab2e7c25b6faf577e7ee8197ae806a979)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x1) |
| #define | [PRS0\_ASYNCH10\_PC2](#a22dd84a911044fe555ee09be1ee255e6)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x2) |
| #define | [PRS0\_ASYNCH10\_PC3](#a4285722719da53788c48b4fc1f563e78)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x3) |
| #define | [PRS0\_ASYNCH10\_PC4](#a5fde4317aee5f5e514d31b0a02013e85)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x4) |
| #define | [PRS0\_ASYNCH10\_PC5](#ac3e04e87a2e22a0e5852c25cd42f5bfd)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x5) |
| #define | [PRS0\_ASYNCH10\_PC6](#a112632637b58df9fa0b0f1a4090f4360)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x6) |
| #define | [PRS0\_ASYNCH10\_PC7](#abe1145f2e2eb3620f7329a03e66f0a5b)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x2, 0x7) |
| #define | [PRS0\_ASYNCH10\_PD0](#a86d5340c5133d3193351104663683d0e)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x3, 0x0) |
| #define | [PRS0\_ASYNCH10\_PD1](#a00af6bec878e4ea3f6ff297ac35f91ed)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x3, 0x1) |
| #define | [PRS0\_ASYNCH10\_PD2](#a0117d03759e58b8a40f3e32e65c1daff)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x3, 0x2) |
| #define | [PRS0\_ASYNCH10\_PD3](#ac26c97f76181aa0d4d334061599e549b)   [SILABS\_DBUS\_PRS0\_ASYNCH10](#a48a4d109c810311436ee8add40794aba)(0x3, 0x3) |
| #define | [PRS0\_ASYNCH11\_PC0](#a1ba16c8c6da7e3129c03eb546df4c993)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x0) |
| #define | [PRS0\_ASYNCH11\_PC1](#a4780077af0f3eac79ac458382dfdd9ce)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x1) |
| #define | [PRS0\_ASYNCH11\_PC2](#a32ed7a6cd5db3336ee370d6cf9d8e989)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x2) |
| #define | [PRS0\_ASYNCH11\_PC3](#ada09802928473e1a5360709b259ce87e)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x3) |
| #define | [PRS0\_ASYNCH11\_PC4](#aa83823870ce109c570db56a0d7bf4197)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x4) |
| #define | [PRS0\_ASYNCH11\_PC5](#a06db00a9ba09d6f16e8ab4423b98edb8)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x5) |
| #define | [PRS0\_ASYNCH11\_PC6](#abf891c76454cd7dcccf81062e03e49c0)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x6) |
| #define | [PRS0\_ASYNCH11\_PC7](#ac19cc8092d5117eac5d57e0b9ef75408)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x2, 0x7) |
| #define | [PRS0\_ASYNCH11\_PD0](#a4d64f2e728e07b761372b682a6732ea9)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x3, 0x0) |
| #define | [PRS0\_ASYNCH11\_PD1](#aa62c6365ff4d4c6e9ac8952c9bc50d1d)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x3, 0x1) |
| #define | [PRS0\_ASYNCH11\_PD2](#a6d8321e7ba25db410748817cd169d45a)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x3, 0x2) |
| #define | [PRS0\_ASYNCH11\_PD3](#aafe8d7f49fead257b9a5065f68727c1a)   [SILABS\_DBUS\_PRS0\_ASYNCH11](#a7acd670bc40ebc057369a7c577a0b0c2)(0x3, 0x3) |
| #define | [PRS0\_SYNCH0\_PA0](#a2c5a579f02ffd8ca34ce4f12cb30c8f0)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x0) |
| #define | [PRS0\_SYNCH0\_PA1](#a5f853596173978c14b0b85059afa8a5a)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x1) |
| #define | [PRS0\_SYNCH0\_PA2](#a7c8f6f55ba3e60c6a160f83f324442f0)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x2) |
| #define | [PRS0\_SYNCH0\_PA3](#a8b8697e5c71b52686ea68726a1c033dd)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x3) |
| #define | [PRS0\_SYNCH0\_PA4](#a509796448ccd2509eeb7fbf9b4432267)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x4) |
| #define | [PRS0\_SYNCH0\_PA5](#afd80bdbc61c9bddb37851b1c9b7b6fa6)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x5) |
| #define | [PRS0\_SYNCH0\_PA6](#abd86045f5ef93089158a28dd7f3aa4c2)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x6) |
| #define | [PRS0\_SYNCH0\_PA7](#ae4f987b0bca7d9d9b12a61f99cec5262)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x7) |
| #define | [PRS0\_SYNCH0\_PA8](#a9158c2302ee19ed733f624dea5b4b39a)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x0, 0x8) |
| #define | [PRS0\_SYNCH0\_PB0](#a736a7ad4a31b1d6dc0c548d628da9d97)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x1, 0x0) |
| #define | [PRS0\_SYNCH0\_PB1](#a10e121857131802c71c42f1fbad81970)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x1, 0x1) |
| #define | [PRS0\_SYNCH0\_PB2](#a73be353f9ce6f94984b0e1c804c97e07)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x1, 0x2) |
| #define | [PRS0\_SYNCH0\_PB3](#acd5b4f55607cae70abe6fb9e6b361f53)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x1, 0x3) |
| #define | [PRS0\_SYNCH0\_PB4](#a9e5fc4aa547c95e8dc34bb89c384a35f)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x1, 0x4) |
| #define | [PRS0\_SYNCH0\_PC0](#aed0f68fd0e4029e96d08fb24876f88b5)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x0) |
| #define | [PRS0\_SYNCH0\_PC1](#ae52c949f3917be619b0f5f2365c2e8ba)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x1) |
| #define | [PRS0\_SYNCH0\_PC2](#aac10f668835b732d019a50c3cfc47e37)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x2) |
| #define | [PRS0\_SYNCH0\_PC3](#aa9c52d637e33202df2ace78c13c9555f)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x3) |
| #define | [PRS0\_SYNCH0\_PC4](#adcaec5a2fb5dd33e72e486587daa1f4e)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x4) |
| #define | [PRS0\_SYNCH0\_PC5](#aebbdc8a0ced784325db8374db6a1f16c)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x5) |
| #define | [PRS0\_SYNCH0\_PC6](#aedadba37735c1e29b357461908d0c22f)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x6) |
| #define | [PRS0\_SYNCH0\_PC7](#a0b2e975e8a9e48c1e0b64d10b0d4776f)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x2, 0x7) |
| #define | [PRS0\_SYNCH0\_PD0](#a5f8dea11049e64bae1e4e27baf9e1b31)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x3, 0x0) |
| #define | [PRS0\_SYNCH0\_PD1](#a27144719fce957df87cb1434bd78c53b)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x3, 0x1) |
| #define | [PRS0\_SYNCH0\_PD2](#a014112c01a441ca65ee77b693e22bcf5)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x3, 0x2) |
| #define | [PRS0\_SYNCH0\_PD3](#a9ace1d40d2d50bc683ef0c57cc7863e0)   [SILABS\_DBUS\_PRS0\_SYNCH0](#a1b8e171cd761535148063c9b81ed3ee0)(0x3, 0x3) |
| #define | [PRS0\_SYNCH1\_PA0](#adedbd9cd1918a6d9543c886660eced9d)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x0) |
| #define | [PRS0\_SYNCH1\_PA1](#a1083f73ff99ca1b3bf4446081e2addd7)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x1) |
| #define | [PRS0\_SYNCH1\_PA2](#a1ea1179bbedea21d7d5ba85c489b88e1)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x2) |
| #define | [PRS0\_SYNCH1\_PA3](#a18fe9b252631cc7ba936c99d6206294c)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x3) |
| #define | [PRS0\_SYNCH1\_PA4](#ae5b32510b0bfea666dfb424ecad5e926)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x4) |
| #define | [PRS0\_SYNCH1\_PA5](#a990491e0b9b76fc29c692ab11429d1bf)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x5) |
| #define | [PRS0\_SYNCH1\_PA6](#accd2f4d5864cea8337d9436d6f946f2d)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x6) |
| #define | [PRS0\_SYNCH1\_PA7](#aceb6e7687dc5a74ba0da121a26529409)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x7) |
| #define | [PRS0\_SYNCH1\_PA8](#ab59c19f19a428b50ddf674bd46c4e07f)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x0, 0x8) |
| #define | [PRS0\_SYNCH1\_PB0](#aa19c3a0e0e8ce1868f1a89f7bd2e703a)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x1, 0x0) |
| #define | [PRS0\_SYNCH1\_PB1](#ab5cf7a7aacec81e75db1643c99958fa3)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x1, 0x1) |
| #define | [PRS0\_SYNCH1\_PB2](#a7487f16738d5b7fa4b19224e4eeab36d)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x1, 0x2) |
| #define | [PRS0\_SYNCH1\_PB3](#aaff1a467a07bc3301c63667057cb4b2d)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x1, 0x3) |
| #define | [PRS0\_SYNCH1\_PB4](#a167f92235a6d97f9ecd421e65b18e7f7)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x1, 0x4) |
| #define | [PRS0\_SYNCH1\_PC0](#ab3036a275379a79acb9c9186172036be)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x0) |
| #define | [PRS0\_SYNCH1\_PC1](#ae726abd2298409738d8deba2708508be)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x1) |
| #define | [PRS0\_SYNCH1\_PC2](#a9aec203bbc1ecd06760f7262a53c2b3e)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x2) |
| #define | [PRS0\_SYNCH1\_PC3](#a87e88cfd739e57c6b2832ddc579e9007)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x3) |
| #define | [PRS0\_SYNCH1\_PC4](#a5ff140aeb080678501e5a49e5a17238e)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x4) |
| #define | [PRS0\_SYNCH1\_PC5](#ad4e38b8812f7c0d4a071c56033ea29b6)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x5) |
| #define | [PRS0\_SYNCH1\_PC6](#ae5fd5f17e4c57e6d27e4771b9d697412)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x6) |
| #define | [PRS0\_SYNCH1\_PC7](#a73df027a983ad91140837b7823cf457b)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x2, 0x7) |
| #define | [PRS0\_SYNCH1\_PD0](#ac3d3b0681c6f881fdf67d75330d2ad15)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x3, 0x0) |
| #define | [PRS0\_SYNCH1\_PD1](#a856e585175b99140059f56bbb485002c)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x3, 0x1) |
| #define | [PRS0\_SYNCH1\_PD2](#a40bd508ace349e81a5d0c155ca89970d)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x3, 0x2) |
| #define | [PRS0\_SYNCH1\_PD3](#a0619050cb1a04b75b610788e2de0390e)   [SILABS\_DBUS\_PRS0\_SYNCH1](#a85d7bbcc208a977d14aa286a9576b432)(0x3, 0x3) |
| #define | [PRS0\_SYNCH2\_PA0](#a30eedcbcb9ef6aa04facebe8e1cc1093)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x0) |
| #define | [PRS0\_SYNCH2\_PA1](#a8ec3379386547e7712ad3c900ec6814c)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x1) |
| #define | [PRS0\_SYNCH2\_PA2](#a770727e399810443ff27f6a2023c65ee)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x2) |
| #define | [PRS0\_SYNCH2\_PA3](#afa5e0ddfe140d74f0dd76d8e7edda691)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x3) |
| #define | [PRS0\_SYNCH2\_PA4](#a2cf89814fec476f61882164cdf99b537)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x4) |
| #define | [PRS0\_SYNCH2\_PA5](#a8a48ec9e994929feacba66e0509ad3e1)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x5) |
| #define | [PRS0\_SYNCH2\_PA6](#a117da23bb4f9f0aa2110437ffefc365a)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x6) |
| #define | [PRS0\_SYNCH2\_PA7](#a08847c5400ec84819a9b68b2c61bb501)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x7) |
| #define | [PRS0\_SYNCH2\_PA8](#ac874a823e48f1cce54ed84337b174833)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x0, 0x8) |
| #define | [PRS0\_SYNCH2\_PB0](#a3246953945006183dfbc3b12a5e86d61)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x1, 0x0) |
| #define | [PRS0\_SYNCH2\_PB1](#a0dec289423a72a3226f883db9921b0b2)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x1, 0x1) |
| #define | [PRS0\_SYNCH2\_PB2](#a5c36bbbb8c205c06b05cb1786f91f34f)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x1, 0x2) |
| #define | [PRS0\_SYNCH2\_PB3](#a4e5c98830a60d5e00602e4e7f4348b6f)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x1, 0x3) |
| #define | [PRS0\_SYNCH2\_PB4](#aa06a6017287b483a4a47b128043b7217)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x1, 0x4) |
| #define | [PRS0\_SYNCH2\_PC0](#ac9ab782f8cda90916bd9cb751753144a)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x0) |
| #define | [PRS0\_SYNCH2\_PC1](#a71fb98a3d5355af02d2c46d69c7f6edc)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x1) |
| #define | [PRS0\_SYNCH2\_PC2](#a50b30cf886dedec9e7cd761d9596d7f6)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x2) |
| #define | [PRS0\_SYNCH2\_PC3](#ab8725b1678b453d17551cf0daea10f57)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x3) |
| #define | [PRS0\_SYNCH2\_PC4](#a012f52b7a7cc4babe7f8e14b27125790)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x4) |
| #define | [PRS0\_SYNCH2\_PC5](#a5ce775779214b9341aede3162d4e381a)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x5) |
| #define | [PRS0\_SYNCH2\_PC6](#a151b6197cf1bb336dcdecf41cfdc90fc)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x6) |
| #define | [PRS0\_SYNCH2\_PC7](#a49b69f4a2a409147dec4247b891e2d0e)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x2, 0x7) |
| #define | [PRS0\_SYNCH2\_PD0](#af8c37706e65ff4f9f6f90f01ce507040)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x3, 0x0) |
| #define | [PRS0\_SYNCH2\_PD1](#ac83a6c15c88a8662ce8b9ba58d60772a)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x3, 0x1) |
| #define | [PRS0\_SYNCH2\_PD2](#ad8d312030ac50620b851c24cfb90b8c0)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x3, 0x2) |
| #define | [PRS0\_SYNCH2\_PD3](#a3462ed2558a059ff7b2c81471bb30adf)   [SILABS\_DBUS\_PRS0\_SYNCH2](#a7340c07baee2cad6d5b685929c48151b)(0x3, 0x3) |
| #define | [PRS0\_SYNCH3\_PA0](#a3d8a4990b1f1b2c03152d2d0ee88afc3)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x0) |
| #define | [PRS0\_SYNCH3\_PA1](#a13b0ade04e1c64d1438afe98588fe2d2)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x1) |
| #define | [PRS0\_SYNCH3\_PA2](#a270b6759ebfa8c61efefbc57fa10b3a3)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x2) |
| #define | [PRS0\_SYNCH3\_PA3](#a6d223baeec1045d533966d37adeaa1fd)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x3) |
| #define | [PRS0\_SYNCH3\_PA4](#a0e17834640a0fa86e9cc0d166b41051e)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x4) |
| #define | [PRS0\_SYNCH3\_PA5](#a49a035319ad597aca7e0fcfa1abd0f01)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x5) |
| #define | [PRS0\_SYNCH3\_PA6](#a13e3aaaec3efb457103bb8159cb4de31)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x6) |
| #define | [PRS0\_SYNCH3\_PA7](#aad295ab8444f14fd8a7f01225d8d028d)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x7) |
| #define | [PRS0\_SYNCH3\_PA8](#a1ee67f1e40e56d7ce7b6e2dfc3c6d60d)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x0, 0x8) |
| #define | [PRS0\_SYNCH3\_PB0](#ab17a4fca8c86667da92478553626bba6)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x1, 0x0) |
| #define | [PRS0\_SYNCH3\_PB1](#a88fff8ac2df69413d6fddc5ec152e31b)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x1, 0x1) |
| #define | [PRS0\_SYNCH3\_PB2](#ae56538fc7c8d0ca774ed366e51675230)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x1, 0x2) |
| #define | [PRS0\_SYNCH3\_PB3](#acc237ffc92de8a4b0003dd9f7e09c690)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x1, 0x3) |
| #define | [PRS0\_SYNCH3\_PB4](#a1579ef24d96f575092d727d1ea82af8e)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x1, 0x4) |
| #define | [PRS0\_SYNCH3\_PC0](#a5b3ca0959f268e1977ab4fcb0333b282)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x0) |
| #define | [PRS0\_SYNCH3\_PC1](#a322705abcca1fb83fdffcf16252c35d4)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x1) |
| #define | [PRS0\_SYNCH3\_PC2](#ad45be94cb4581dbc5c9474d2da892aa0)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x2) |
| #define | [PRS0\_SYNCH3\_PC3](#af541dc086b57060761678fba2145d5fc)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x3) |
| #define | [PRS0\_SYNCH3\_PC4](#aa8cc93aafe5498f4cc5a26d1fa37599e)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x4) |
| #define | [PRS0\_SYNCH3\_PC5](#a05496c3ac6cbd4310245f30c0810afbe)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x5) |
| #define | [PRS0\_SYNCH3\_PC6](#a6f198140e1506fd09800ff26f6223823)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x6) |
| #define | [PRS0\_SYNCH3\_PC7](#aedd84533e1397a94ca85f73644083d7d)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x2, 0x7) |
| #define | [PRS0\_SYNCH3\_PD0](#a028ffbfde62bf2f28a08c99884d6fbb6)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x3, 0x0) |
| #define | [PRS0\_SYNCH3\_PD1](#a0d0ee2b67b86c4b2615f24e673966465)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x3, 0x1) |
| #define | [PRS0\_SYNCH3\_PD2](#a8dc61e39bff0c335982b5a775c9b000c)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x3, 0x2) |
| #define | [PRS0\_SYNCH3\_PD3](#a10deabf90e836f5bd478ad2a6483d2c8)   [SILABS\_DBUS\_PRS0\_SYNCH3](#a131fc4f34da4d410665642dfd51b733b)(0x3, 0x3) |
| #define | [TIMER0\_CC0\_PA0](#a643451fe929eaf497b28b23570152dfa)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x0) |
| #define | [TIMER0\_CC0\_PA1](#a257ab281a2a05ec0cc41ad2e3b548dfb)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x1) |
| #define | [TIMER0\_CC0\_PA2](#a1382ce3a810d4e7056919091fe9514f5)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x2) |
| #define | [TIMER0\_CC0\_PA3](#a9a9109ad50309f2200302915ea5a2654)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x3) |
| #define | [TIMER0\_CC0\_PA4](#a035c1f38daa2aca747ced020035bd292)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x4) |
| #define | [TIMER0\_CC0\_PA5](#a4bfcb9dec6df42cdf9a1fe979354ae57)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x5) |
| #define | [TIMER0\_CC0\_PA6](#ad1a677a1839ff4de6cc82e6e17b5aae2)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x6) |
| #define | [TIMER0\_CC0\_PA7](#a83713df06a69164162a4b734434bccc5)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x7) |
| #define | [TIMER0\_CC0\_PA8](#ab20dff18cf40da11a2ebcc405819c7e8)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x0, 0x8) |
| #define | [TIMER0\_CC0\_PB0](#a18fb1529d6c032c6755f3d5a0abf9c76)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x1, 0x0) |
| #define | [TIMER0\_CC0\_PB1](#adf86b7c1c4b41eaf900d8a02e912f7c2)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x1, 0x1) |
| #define | [TIMER0\_CC0\_PB2](#ab01379b7fede12eae4bf2dcd1415d360)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x1, 0x2) |
| #define | [TIMER0\_CC0\_PB3](#abad5725bf78d847e54ad1bed240eca11)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x1, 0x3) |
| #define | [TIMER0\_CC0\_PB4](#a6cac16610a7cff74400e55edd20ebc76)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x1, 0x4) |
| #define | [TIMER0\_CC0\_PC0](#af01197ecb61c8e13ed760c4f036d555f)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x0) |
| #define | [TIMER0\_CC0\_PC1](#ae82052a9a3803c36b447e75e30db22b5)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x1) |
| #define | [TIMER0\_CC0\_PC2](#a89bade3c8848eeccc253f9752b16790c)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x2) |
| #define | [TIMER0\_CC0\_PC3](#a8b2ec4704842a1824c29fba1f700292e)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x3) |
| #define | [TIMER0\_CC0\_PC4](#acd56df092cae914b4e416e932e2b9f59)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x4) |
| #define | [TIMER0\_CC0\_PC5](#a17bbebdef205a11b6021b510d62ff3b8)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x5) |
| #define | [TIMER0\_CC0\_PC6](#a183d951a3ba6704d8056c1f16658a81f)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x6) |
| #define | [TIMER0\_CC0\_PC7](#ae5baae49155bdc86220399e4c80d57e3)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x2, 0x7) |
| #define | [TIMER0\_CC0\_PD0](#a3db86be83a2cf8932a653abbf93aed00)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x3, 0x0) |
| #define | [TIMER0\_CC0\_PD1](#a4350a7968647bb2f25b6b2637fef6ad1)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x3, 0x1) |
| #define | [TIMER0\_CC0\_PD2](#a4c8e3e5bdf2d6582e6182f3df56f606b)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x3, 0x2) |
| #define | [TIMER0\_CC0\_PD3](#a695f1eba6df77776fb45e9f69a6fd57a)   [SILABS\_DBUS\_TIMER0\_CC0](#ad1f44a36026d8dd0f50d48e95fc9e5b3)(0x3, 0x3) |
| #define | [TIMER0\_CC1\_PA0](#aa74131bdc087fb80e597e3d497ab9796)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x0) |
| #define | [TIMER0\_CC1\_PA1](#a4a841ee625298d042db41bc0cd385796)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x1) |
| #define | [TIMER0\_CC1\_PA2](#a69b83d879f0cb485ba4af8b3cf4844a1)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x2) |
| #define | [TIMER0\_CC1\_PA3](#a0b3cce5e9df6245edce583e307c70b7f)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x3) |
| #define | [TIMER0\_CC1\_PA4](#ae6724c9762d1a9ae311d902e930b337c)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x4) |
| #define | [TIMER0\_CC1\_PA5](#a2354f1d78e8686d9ea3c44dd9bac5b38)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x5) |
| #define | [TIMER0\_CC1\_PA6](#a1b634a95c42a9065c7307c1a13461f39)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x6) |
| #define | [TIMER0\_CC1\_PA7](#abd19b057060c325aa1fa13af9121671d)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x7) |
| #define | [TIMER0\_CC1\_PA8](#ac005d8b7842095517fc151d18aa0b649)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x0, 0x8) |
| #define | [TIMER0\_CC1\_PB0](#a6b0f1898a3246e0dd5915d5f5014b53e)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x1, 0x0) |
| #define | [TIMER0\_CC1\_PB1](#a812c3aa15e23b7be5d70f052259722dc)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x1, 0x1) |
| #define | [TIMER0\_CC1\_PB2](#ab12ee18043cd8f1ac0050cc7f706c712)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x1, 0x2) |
| #define | [TIMER0\_CC1\_PB3](#a988e56db008ca4cfd5b6ef5072b2e78f)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x1, 0x3) |
| #define | [TIMER0\_CC1\_PB4](#ad7bf61540cbd3e042da81a14a3c7c51f)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x1, 0x4) |
| #define | [TIMER0\_CC1\_PC0](#a5787f33a274113239c4f5e8abecdf9a2)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x0) |
| #define | [TIMER0\_CC1\_PC1](#a14c64ec2717df0534956326f806de22a)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x1) |
| #define | [TIMER0\_CC1\_PC2](#ad7ffea850def6f7001ed2471ce3a13b6)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x2) |
| #define | [TIMER0\_CC1\_PC3](#a3f40aa2528d1f936a0e6734c0227afb2)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x3) |
| #define | [TIMER0\_CC1\_PC4](#a72ab00cdfc58ff9f2aef06c5ee9e1e13)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x4) |
| #define | [TIMER0\_CC1\_PC5](#a7a0b8714592092cb219e214cd28da4c5)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x5) |
| #define | [TIMER0\_CC1\_PC6](#aa48fdfed86985e0415468b7488c9d38c)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x6) |
| #define | [TIMER0\_CC1\_PC7](#a29e63d266965c64f0903cc309f20cb22)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x2, 0x7) |
| #define | [TIMER0\_CC1\_PD0](#ad721fa41b15556e529252a63302e8320)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x3, 0x0) |
| #define | [TIMER0\_CC1\_PD1](#abdc57a8f13e515d62d84684433f4c399)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x3, 0x1) |
| #define | [TIMER0\_CC1\_PD2](#a6a00214723619c929a860d4d5fa82d70)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x3, 0x2) |
| #define | [TIMER0\_CC1\_PD3](#ab5fe2a23145e40055ae0f532309c45a4)   [SILABS\_DBUS\_TIMER0\_CC1](#a1eb30c3f4f87f98b3da18bc2a602e7e6)(0x3, 0x3) |
| #define | [TIMER0\_CC2\_PA0](#a10518d21844ab1a787009973ac06ce22)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x0) |
| #define | [TIMER0\_CC2\_PA1](#a40b5d230cec35f97648678731d970520)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x1) |
| #define | [TIMER0\_CC2\_PA2](#a5183b3c3cec8352c11edef376fc346ad)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x2) |
| #define | [TIMER0\_CC2\_PA3](#aec173f24a643f2d50e4e2fe44b0d1dc8)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x3) |
| #define | [TIMER0\_CC2\_PA4](#a4df67f53e8e2501bed3fd9565a49c0d6)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x4) |
| #define | [TIMER0\_CC2\_PA5](#a0529c6f8022ee408363ecc6452ac2c44)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x5) |
| #define | [TIMER0\_CC2\_PA6](#a1e0f169ebf24d5954b875bd824b86de1)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x6) |
| #define | [TIMER0\_CC2\_PA7](#a59bb4e9a92765847c5c2a5173df27f1e)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x7) |
| #define | [TIMER0\_CC2\_PA8](#a4a131dbd8f75a91809fece6cba85fcc5)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x0, 0x8) |
| #define | [TIMER0\_CC2\_PB0](#ad7a7916ae90b8345be7279e50f18c190)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x1, 0x0) |
| #define | [TIMER0\_CC2\_PB1](#a36ccb83c4230c2f3d14accbb965b08cd)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x1, 0x1) |
| #define | [TIMER0\_CC2\_PB2](#ad02263c57d4f083872708a7c91ee515f)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x1, 0x2) |
| #define | [TIMER0\_CC2\_PB3](#aaeb96f9ff0dc83edf33cfef5c95430f6)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x1, 0x3) |
| #define | [TIMER0\_CC2\_PB4](#a5aa2d1d44c749859ed1f1e6e468e099e)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x1, 0x4) |
| #define | [TIMER0\_CC2\_PC0](#afe51827dd65359061f88753af6868eb5)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x0) |
| #define | [TIMER0\_CC2\_PC1](#ae3d14c1aa4739ba2be209c8490e05b9b)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x1) |
| #define | [TIMER0\_CC2\_PC2](#a12baff93c97c64f74538b1995171fab7)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x2) |
| #define | [TIMER0\_CC2\_PC3](#a96fe3aa3622573210ac344515718962f)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x3) |
| #define | [TIMER0\_CC2\_PC4](#ad70b84d782f9af43d146a34c1533f08a)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x4) |
| #define | [TIMER0\_CC2\_PC5](#a8bebf51e280fec4baea6e545ba0e8576)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x5) |
| #define | [TIMER0\_CC2\_PC6](#ab088658e226c6a3f754574378fa59fdc)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x6) |
| #define | [TIMER0\_CC2\_PC7](#a3248786ef86b22d8f8e6de854160ff6a)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x2, 0x7) |
| #define | [TIMER0\_CC2\_PD0](#a29a4b811b779721b8ab98976d0af976c)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x3, 0x0) |
| #define | [TIMER0\_CC2\_PD1](#a21d070a5f412c7a77e53f69c87c57997)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x3, 0x1) |
| #define | [TIMER0\_CC2\_PD2](#a419e2b988ac821a7b4e40fb925da5916)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x3, 0x2) |
| #define | [TIMER0\_CC2\_PD3](#aae16cb8df6cc099c3344c5740fd31e69)   [SILABS\_DBUS\_TIMER0\_CC2](#a23896bac158177558e7f179e8f3382a6)(0x3, 0x3) |
| #define | [TIMER0\_CDTI0\_PA0](#a583547311775fdf98f4d19afb149ac6c)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x0) |
| #define | [TIMER0\_CDTI0\_PA1](#a8005c42773c60dd5aec6e3ee8f4b7491)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x1) |
| #define | [TIMER0\_CDTI0\_PA2](#a78955dc51203c015d86b442978ad260e)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x2) |
| #define | [TIMER0\_CDTI0\_PA3](#a291a17c15340c09f32a3c63e3da95a9c)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x3) |
| #define | [TIMER0\_CDTI0\_PA4](#ab3b70d25fa01aaade758c277465c9639)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x4) |
| #define | [TIMER0\_CDTI0\_PA5](#a025bd51e6c211605497795d76e175510)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x5) |
| #define | [TIMER0\_CDTI0\_PA6](#a17617cf4fecd500e152bc39ef84e009b)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x6) |
| #define | [TIMER0\_CDTI0\_PA7](#aee12a8ee669b0201ff7557c15b2fc6d5)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x7) |
| #define | [TIMER0\_CDTI0\_PA8](#add042bfe988b01b650b3855a407e71cf)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x0, 0x8) |
| #define | [TIMER0\_CDTI0\_PB0](#ac08f3bf826c3d909d06c67c2acb418ef)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x1, 0x0) |
| #define | [TIMER0\_CDTI0\_PB1](#aaf1bd6f6922c1316131edb6cb0f3de9e)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x1, 0x1) |
| #define | [TIMER0\_CDTI0\_PB2](#af8a99eb0ed525295713c0158c7c0325f)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x1, 0x2) |
| #define | [TIMER0\_CDTI0\_PB3](#addeeb5046eef54b417ce88ff5938efac)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x1, 0x3) |
| #define | [TIMER0\_CDTI0\_PB4](#a45b93c4fd05e5bf784cc1ed50162df94)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x1, 0x4) |
| #define | [TIMER0\_CDTI0\_PC0](#a5f22a6e89d3fb5e3bb7925fdbe1c2e38)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x0) |
| #define | [TIMER0\_CDTI0\_PC1](#a72ef54f11ed78d2e16f007d394030955)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x1) |
| #define | [TIMER0\_CDTI0\_PC2](#a3f65837c636c8b483c7130555c34a54c)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x2) |
| #define | [TIMER0\_CDTI0\_PC3](#acbf891b0c24b9af901264aba00b84f64)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x3) |
| #define | [TIMER0\_CDTI0\_PC4](#adf859e578ce341428c887d8267d962bf)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x4) |
| #define | [TIMER0\_CDTI0\_PC5](#ae57392b6eb47339eb4e5bd89840d19a9)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x5) |
| #define | [TIMER0\_CDTI0\_PC6](#a5da4268d82621edce0d73e495eeaeffc)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x6) |
| #define | [TIMER0\_CDTI0\_PC7](#a18354cd70447a811e3cfeb92e6300aaf)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x2, 0x7) |
| #define | [TIMER0\_CDTI0\_PD0](#abe060cc518151861fccab2604541e238)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x3, 0x0) |
| #define | [TIMER0\_CDTI0\_PD1](#a0925901af2c13317cf4f43c50e01d83a)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x3, 0x1) |
| #define | [TIMER0\_CDTI0\_PD2](#aed6dd4aa21be7afbe03d984356d36e32)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x3, 0x2) |
| #define | [TIMER0\_CDTI0\_PD3](#aa52d4d7a010abe242632b4574332349b)   [SILABS\_DBUS\_TIMER0\_CDTI0](#a44f0ed489cab3a50241d605931d579b0)(0x3, 0x3) |
| #define | [TIMER0\_CDTI1\_PA0](#a757add3c35ee9b20b8bb75363620e57f)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x0) |
| #define | [TIMER0\_CDTI1\_PA1](#a39b01d816f29ff5114ac045475ad1c80)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x1) |
| #define | [TIMER0\_CDTI1\_PA2](#a648e126ee7e0bdf5faff238a097c6e5e)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x2) |
| #define | [TIMER0\_CDTI1\_PA3](#a0e36cbcf42a86fa70f9561b1a817831d)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x3) |
| #define | [TIMER0\_CDTI1\_PA4](#a12661cbedaeab2177edf943b1f752b6b)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x4) |
| #define | [TIMER0\_CDTI1\_PA5](#a9012c36cbc093ebb308af9118eabfde9)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x5) |
| #define | [TIMER0\_CDTI1\_PA6](#ac4ab807c106f7b9bc718e931d517c791)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x6) |
| #define | [TIMER0\_CDTI1\_PA7](#ada3087b05c215a2484cf068cdc1494f7)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x7) |
| #define | [TIMER0\_CDTI1\_PA8](#a5c0a03d2f318b94a19795fb40e767285)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x0, 0x8) |
| #define | [TIMER0\_CDTI1\_PB0](#a8b1c6a4724744e459918508925be254e)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x1, 0x0) |
| #define | [TIMER0\_CDTI1\_PB1](#a9206a9ae50fbe6a063df918f0dc7d9b5)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x1, 0x1) |
| #define | [TIMER0\_CDTI1\_PB2](#a7ca452eeecf6b0b1a6f833b5332244cf)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x1, 0x2) |
| #define | [TIMER0\_CDTI1\_PB3](#ae206d9477b7cad08f2fc30af80bc08f8)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x1, 0x3) |
| #define | [TIMER0\_CDTI1\_PB4](#ad1d178e1d6fb8768959e4b8b04ab18e3)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x1, 0x4) |
| #define | [TIMER0\_CDTI1\_PC0](#ad5eb7a31fde2301a819d1f7fb3fa4120)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x0) |
| #define | [TIMER0\_CDTI1\_PC1](#a67c242881dc443329a04f2148b5d3171)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x1) |
| #define | [TIMER0\_CDTI1\_PC2](#a6e61b116d02e63455d54f16e29168dfe)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x2) |
| #define | [TIMER0\_CDTI1\_PC3](#a904d89c160a99cc883673a11164eb00a)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x3) |
| #define | [TIMER0\_CDTI1\_PC4](#afa348bc98e1aa83ec82924c1c49a5970)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x4) |
| #define | [TIMER0\_CDTI1\_PC5](#a43e280a63df1054883f731736d864712)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x5) |
| #define | [TIMER0\_CDTI1\_PC6](#a7ffd35a5c906b6416b44621024daec1f)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x6) |
| #define | [TIMER0\_CDTI1\_PC7](#a7001978e8da4cd34b0da45ca39fda8f1)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x2, 0x7) |
| #define | [TIMER0\_CDTI1\_PD0](#a713013e442d42bf60f0f8a2df0e178de)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x3, 0x0) |
| #define | [TIMER0\_CDTI1\_PD1](#a28cc02c56e4eb397f3fc9d106db59dd3)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x3, 0x1) |
| #define | [TIMER0\_CDTI1\_PD2](#a7a3ee64de9bcf3d3e05cad7c0eb51492)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x3, 0x2) |
| #define | [TIMER0\_CDTI1\_PD3](#ac0570e1fa46ef8d9015c9e41cede4394)   [SILABS\_DBUS\_TIMER0\_CDTI1](#ae13240899cbf48ec4f6710bcabc4ded8)(0x3, 0x3) |
| #define | [TIMER0\_CDTI2\_PA0](#a723140878fb318fc60e62886e8e4bb6b)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x0) |
| #define | [TIMER0\_CDTI2\_PA1](#a69ea746a21b0305be02db15ba8ced4dc)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x1) |
| #define | [TIMER0\_CDTI2\_PA2](#a63e2744f17ec7b868e38010999a5b99e)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x2) |
| #define | [TIMER0\_CDTI2\_PA3](#ad9c1f9c457c63b9f7ee15cedb89c8b29)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x3) |
| #define | [TIMER0\_CDTI2\_PA4](#ac5e02eb43bbc85c4e07976539d1c7b66)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x4) |
| #define | [TIMER0\_CDTI2\_PA5](#a17440dab813cdc7a4b58682db3c0aa3c)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x5) |
| #define | [TIMER0\_CDTI2\_PA6](#a967cbd605349c15eada5527602a05fc9)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x6) |
| #define | [TIMER0\_CDTI2\_PA7](#a3ee02bd72164f5ddab71818f5dc34616)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x7) |
| #define | [TIMER0\_CDTI2\_PA8](#a9e6862b3fbfa9272f0401ed722a7452c)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x0, 0x8) |
| #define | [TIMER0\_CDTI2\_PB0](#a4a53984105a683a6807ad0a26e13a60d)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x1, 0x0) |
| #define | [TIMER0\_CDTI2\_PB1](#a12ffd91f7201f73e0d75c2298d5abce9)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x1, 0x1) |
| #define | [TIMER0\_CDTI2\_PB2](#a211506e052690ec459d7225ac9ec2dd1)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x1, 0x2) |
| #define | [TIMER0\_CDTI2\_PB3](#a6639dc47e82cbc98ba1aae88605e8c63)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x1, 0x3) |
| #define | [TIMER0\_CDTI2\_PB4](#a3cdd0a6bcde7f01a695284e11fe5946d)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x1, 0x4) |
| #define | [TIMER0\_CDTI2\_PC0](#a11f7ac3b39604c06f639dc4b925ee93d)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x0) |
| #define | [TIMER0\_CDTI2\_PC1](#a2b6fa7363ef650a2847113779b5b36a7)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x1) |
| #define | [TIMER0\_CDTI2\_PC2](#a3d39899e0d3f88f22feffcd6752b2507)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x2) |
| #define | [TIMER0\_CDTI2\_PC3](#a0f6d66f601b1eaeae268c7ed2b0874ae)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x3) |
| #define | [TIMER0\_CDTI2\_PC4](#ab91374950c6d3774d25c5e6ee6068ce0)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x4) |
| #define | [TIMER0\_CDTI2\_PC5](#a2c76eb69ea9ed92aa328126bbad507d1)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x5) |
| #define | [TIMER0\_CDTI2\_PC6](#abbc57fb5b68e9956483bf9122e985bf2)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x6) |
| #define | [TIMER0\_CDTI2\_PC7](#ab4ee38f2ae41e0c6dfea802960c06146)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x2, 0x7) |
| #define | [TIMER0\_CDTI2\_PD0](#a038cef314d102bb50e58612327d456c6)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x3, 0x0) |
| #define | [TIMER0\_CDTI2\_PD1](#a008dea92e72e9d337f5a6d38aaf33661)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x3, 0x1) |
| #define | [TIMER0\_CDTI2\_PD2](#a7bf636029c51b394d749774c4961aeba)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x3, 0x2) |
| #define | [TIMER0\_CDTI2\_PD3](#a48403324a419bb99f173f8a5198d55a0)   [SILABS\_DBUS\_TIMER0\_CDTI2](#a38b6cbc6d13fa4030cb07f1e2fc59003)(0x3, 0x3) |
| #define | [TIMER1\_CC0\_PA0](#a4b3085c41f4ed8706a3b39755e5b132c)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x0) |
| #define | [TIMER1\_CC0\_PA1](#a5daa5510f5bab9cea855b3d3303daaaf)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x1) |
| #define | [TIMER1\_CC0\_PA2](#abc2afde49650332d28db97653adc501d)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x2) |
| #define | [TIMER1\_CC0\_PA3](#a2df5bd9733330e9a973732a8cc222ee9)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x3) |
| #define | [TIMER1\_CC0\_PA4](#a514654049642c780cd7eae508e0620b9)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x4) |
| #define | [TIMER1\_CC0\_PA5](#a4dd5a3457f09f46922941de990dc9933)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x5) |
| #define | [TIMER1\_CC0\_PA6](#a13520009a8fee0808443df4d4018e0cb)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x6) |
| #define | [TIMER1\_CC0\_PA7](#ade96dcb9354b034ea97b40758e27db1d)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x7) |
| #define | [TIMER1\_CC0\_PA8](#a783d899451987bcaf749652127c1ebb4)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x0, 0x8) |
| #define | [TIMER1\_CC0\_PB0](#a0cda060bbc98a77e19ed36b4d01cfec2)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x1, 0x0) |
| #define | [TIMER1\_CC0\_PB1](#ac2c9847727308a1fed2e7b21c718a92c)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x1, 0x1) |
| #define | [TIMER1\_CC0\_PB2](#a400b3582d5c7bdbbcdd6d9f101d3bf1e)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x1, 0x2) |
| #define | [TIMER1\_CC0\_PB3](#a07e5e02a684ac91a1251bcfcf18a2ff5)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x1, 0x3) |
| #define | [TIMER1\_CC0\_PB4](#ac15f3e270a2f1d2a07eaf5e3b34869a4)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x1, 0x4) |
| #define | [TIMER1\_CC0\_PC0](#a47cdc8781bd255cf8392426ab34cb042)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x0) |
| #define | [TIMER1\_CC0\_PC1](#a41a0a7812419a3a757be7899f30acfde)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x1) |
| #define | [TIMER1\_CC0\_PC2](#a322dee774195678afc5f7066d126e4c7)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x2) |
| #define | [TIMER1\_CC0\_PC3](#a458b636db4779031722ec89e4c8fc0b8)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x3) |
| #define | [TIMER1\_CC0\_PC4](#a59f20ef361658d0cc27c9694c30d2e55)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x4) |
| #define | [TIMER1\_CC0\_PC5](#a510dc66c39d8a79666d1a3d9e6c0e3ad)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x5) |
| #define | [TIMER1\_CC0\_PC6](#adcddd8bdcd941ec6e83d060d4c3cdb9e)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x6) |
| #define | [TIMER1\_CC0\_PC7](#a59678105bf2c365d44d7f138804809e9)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x2, 0x7) |
| #define | [TIMER1\_CC0\_PD0](#aa61ecf9a9f2f6b3ce46bc96d3e3b224c)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x3, 0x0) |
| #define | [TIMER1\_CC0\_PD1](#af69bd23d5eaf09cfa8e4ac6dc815c071)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x3, 0x1) |
| #define | [TIMER1\_CC0\_PD2](#ae35d1bbefce3501c063039f88ed558a2)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x3, 0x2) |
| #define | [TIMER1\_CC0\_PD3](#a27518cd582fa2f5266da488e386783d7)   [SILABS\_DBUS\_TIMER1\_CC0](#a67fb3b7635c0b3408ee6bdea0b861bd3)(0x3, 0x3) |
| #define | [TIMER1\_CC1\_PA0](#ab0467e6e3dafc5340b516304672d0c35)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x0) |
| #define | [TIMER1\_CC1\_PA1](#ab56f3b43b16780006b73b6b67c7fc99c)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x1) |
| #define | [TIMER1\_CC1\_PA2](#a884b7041fab46641ac127f3526d1d6aa)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x2) |
| #define | [TIMER1\_CC1\_PA3](#a97b8069d8cf397b2da2cc011e946cc97)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x3) |
| #define | [TIMER1\_CC1\_PA4](#a01aacbb9315e69096d8c64b78a49b66e)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x4) |
| #define | [TIMER1\_CC1\_PA5](#a7b12d90d7a871b5843843f20b6318fd8)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x5) |
| #define | [TIMER1\_CC1\_PA6](#ac4909134633b306a24982fd780870ff6)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x6) |
| #define | [TIMER1\_CC1\_PA7](#adfa0d8586a7e98878562b2b08bafbfe2)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x7) |
| #define | [TIMER1\_CC1\_PA8](#a30769801f476e980ed12cd966644b77d)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x0, 0x8) |
| #define | [TIMER1\_CC1\_PB0](#a48bff42d940d3d8a4bae06df47255dca)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x1, 0x0) |
| #define | [TIMER1\_CC1\_PB1](#a72b3f2ffb3e69fa3347b782450ee1bf6)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x1, 0x1) |
| #define | [TIMER1\_CC1\_PB2](#a4a119352b728b61375f56621909c6491)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x1, 0x2) |
| #define | [TIMER1\_CC1\_PB3](#a661948aeb7bf6303f6876bad5478e9e0)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x1, 0x3) |
| #define | [TIMER1\_CC1\_PB4](#aaef1ec6432b26aa96d8ada688182fbd7)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x1, 0x4) |
| #define | [TIMER1\_CC1\_PC0](#addaacb911a618cabc51f96bec3690174)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x0) |
| #define | [TIMER1\_CC1\_PC1](#ac8fab9c34e0b1dc6f168573f34d81bba)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x1) |
| #define | [TIMER1\_CC1\_PC2](#adc420cc552323a6db6ac08b76ada22d4)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x2) |
| #define | [TIMER1\_CC1\_PC3](#a52d6b873c40ba4c37eb80089b14abf59)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x3) |
| #define | [TIMER1\_CC1\_PC4](#abb9cd68c18a6c07dc753a10471310e8d)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x4) |
| #define | [TIMER1\_CC1\_PC5](#a93aa2304008369a86392b6a98592ccac)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x5) |
| #define | [TIMER1\_CC1\_PC6](#a311a8f743e1df0e2d257ba4aa71f91a4)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x6) |
| #define | [TIMER1\_CC1\_PC7](#a24c47edc39daf607df7e6b4d37caf769)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x2, 0x7) |
| #define | [TIMER1\_CC1\_PD0](#a1294b47b68006e1da3c1bcf3afa1735b)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x3, 0x0) |
| #define | [TIMER1\_CC1\_PD1](#addf0cad7ebe2b5d0dcb15ee2860aa037)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x3, 0x1) |
| #define | [TIMER1\_CC1\_PD2](#aff68d222f67741f6d81518e502686cab)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x3, 0x2) |
| #define | [TIMER1\_CC1\_PD3](#a8a7f0101160dbc45889575bb975dcad8)   [SILABS\_DBUS\_TIMER1\_CC1](#a2aa7458fe116434331629b24cf0e45f0)(0x3, 0x3) |
| #define | [TIMER1\_CC2\_PA0](#a8134a1d2f64747b5fd66aa6da49db081)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x0) |
| #define | [TIMER1\_CC2\_PA1](#af865342309d6355e05de4a3736e73a65)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x1) |
| #define | [TIMER1\_CC2\_PA2](#af329d80cea63f60045ea71156c4d9d6b)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x2) |
| #define | [TIMER1\_CC2\_PA3](#a1eb4626f10a12c5f6b1539fe897e0df0)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x3) |
| #define | [TIMER1\_CC2\_PA4](#abac33f1fd8502f1356107d20958e9ebb)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x4) |
| #define | [TIMER1\_CC2\_PA5](#ab1ba6969141f0ba0ed17a5e3bd6ac2d7)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x5) |
| #define | [TIMER1\_CC2\_PA6](#a46c2801cd73d8663d493fa62300a0188)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x6) |
| #define | [TIMER1\_CC2\_PA7](#a879a43e390d7a577150f00cb53ebf65c)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x7) |
| #define | [TIMER1\_CC2\_PA8](#aaf3995fdd63448a607fdb1f654c9f75b)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x0, 0x8) |
| #define | [TIMER1\_CC2\_PB0](#ad1ba82a4e75e024cc9f19d66f691c4a1)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x1, 0x0) |
| #define | [TIMER1\_CC2\_PB1](#a4da4366632a0e029856f048d0953b6b2)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x1, 0x1) |
| #define | [TIMER1\_CC2\_PB2](#a758d4ed1cfb60bad3e5226aa3da3a250)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x1, 0x2) |
| #define | [TIMER1\_CC2\_PB3](#aec809925fc33d82ccbdc64200073bffb)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x1, 0x3) |
| #define | [TIMER1\_CC2\_PB4](#ab320f142f9af0a3bec92d8a421b3c7cb)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x1, 0x4) |
| #define | [TIMER1\_CC2\_PC0](#a9d3402f1ed1c7030fb0a1af512425ae2)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x0) |
| #define | [TIMER1\_CC2\_PC1](#a939a814b29112f312ba5085449fe9b8c)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x1) |
| #define | [TIMER1\_CC2\_PC2](#a22ffd1572810e3da8a83f7cc4ccf1386)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x2) |
| #define | [TIMER1\_CC2\_PC3](#afcb1d543010489ffe23a92875fafb326)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x3) |
| #define | [TIMER1\_CC2\_PC4](#a1a34258c1ad068a3474e0114b1e3ac37)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x4) |
| #define | [TIMER1\_CC2\_PC5](#a4b3b5917e7881eeb6a191c095f0df29a)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x5) |
| #define | [TIMER1\_CC2\_PC6](#ab66a57d9d50c0f3492a4ccd7fae0a725)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x6) |
| #define | [TIMER1\_CC2\_PC7](#a46f776103efbd3d5cda86c02bd1c6ee1)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x2, 0x7) |
| #define | [TIMER1\_CC2\_PD0](#a0bb950575d698e83b4a7b055928d4b02)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x3, 0x0) |
| #define | [TIMER1\_CC2\_PD1](#a9f92d850417b9d521c2c2515fbeb8c52)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x3, 0x1) |
| #define | [TIMER1\_CC2\_PD2](#ac5f369d207dbe8da77b94ed7c2ee1e89)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x3, 0x2) |
| #define | [TIMER1\_CC2\_PD3](#aa1c5e07b9ff3373d65a73b3fc916c226)   [SILABS\_DBUS\_TIMER1\_CC2](#a237c2bb8f6da0300cb10b73fab4c7ec4)(0x3, 0x3) |
| #define | [TIMER1\_CDTI0\_PA0](#a76552704f3b8c28588c6073b170a6bbb)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x0) |
| #define | [TIMER1\_CDTI0\_PA1](#a06ea543c9f00b58b7eb4e162a7c3f427)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x1) |
| #define | [TIMER1\_CDTI0\_PA2](#ace53011f7d140ea6892946ac0d246006)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x2) |
| #define | [TIMER1\_CDTI0\_PA3](#a9b740fb70a98203b6a736fb3e3af97d1)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x3) |
| #define | [TIMER1\_CDTI0\_PA4](#adf79eddb39e5a3a28e98da92323cead4)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x4) |
| #define | [TIMER1\_CDTI0\_PA5](#a1c025b319acd53ac15e023a964b684d4)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x5) |
| #define | [TIMER1\_CDTI0\_PA6](#afed1694b73910fdb222e7ac95c7700a6)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x6) |
| #define | [TIMER1\_CDTI0\_PA7](#a16baa7d86f92039e49b2419f2c6920fe)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x7) |
| #define | [TIMER1\_CDTI0\_PA8](#a52ac2c6692f7362bef618cb7d5f0e47c)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x0, 0x8) |
| #define | [TIMER1\_CDTI0\_PB0](#a3f2880efd1d31b43e1fbbd840a535330)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x1, 0x0) |
| #define | [TIMER1\_CDTI0\_PB1](#a3f243ab2322faa708a8c0531a3fb15fe)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x1, 0x1) |
| #define | [TIMER1\_CDTI0\_PB2](#adf3c676ce682f3c923108b655457d517)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x1, 0x2) |
| #define | [TIMER1\_CDTI0\_PB3](#af950bfe52b44c7e24ffe22ef76719f82)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x1, 0x3) |
| #define | [TIMER1\_CDTI0\_PB4](#a9651bb0408184ebddd6b56bc0b84294c)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x1, 0x4) |
| #define | [TIMER1\_CDTI0\_PC0](#a7da42fba55aa964b5af1f0e996e10dfd)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x0) |
| #define | [TIMER1\_CDTI0\_PC1](#a90f5a73378a61a3144cb3be626acf0c3)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x1) |
| #define | [TIMER1\_CDTI0\_PC2](#ac7083129b89cd513468ea9a936cd2a60)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x2) |
| #define | [TIMER1\_CDTI0\_PC3](#ac480c190767e6bf9e64e2581617388d7)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x3) |
| #define | [TIMER1\_CDTI0\_PC4](#a80619df142e179bb585569b51f906b85)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x4) |
| #define | [TIMER1\_CDTI0\_PC5](#af24c550e1fcf0b93ca210c59884dd895)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x5) |
| #define | [TIMER1\_CDTI0\_PC6](#a6006a6fa136154c9f64c65a851a50b2a)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x6) |
| #define | [TIMER1\_CDTI0\_PC7](#af1951b25ec7b89a7dccceb94847fc37f)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x2, 0x7) |
| #define | [TIMER1\_CDTI0\_PD0](#aeafc7272c0cf6bed9dcb09fe8802bd1f)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x3, 0x0) |
| #define | [TIMER1\_CDTI0\_PD1](#a15c83b7661113ab00fc830c832a63ad5)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x3, 0x1) |
| #define | [TIMER1\_CDTI0\_PD2](#af02751809240508c57a914bf47bc929b)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x3, 0x2) |
| #define | [TIMER1\_CDTI0\_PD3](#a36ad9aa1e2ca755919bd18f1461fd9fd)   [SILABS\_DBUS\_TIMER1\_CDTI0](#afd03aef40bfd2fcfec51db90b50a4ebf)(0x3, 0x3) |
| #define | [TIMER1\_CDTI1\_PA0](#a0c90975d990014c0a70d8fe8a01bed61)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x0) |
| #define | [TIMER1\_CDTI1\_PA1](#a063202bd4d4d5c420613ccbdf41c08ac)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x1) |
| #define | [TIMER1\_CDTI1\_PA2](#a03c893bbd5151dc4bf1f08a8c197982d)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x2) |
| #define | [TIMER1\_CDTI1\_PA3](#a13fea81e86713c5839372ae17ffa5b2a)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x3) |
| #define | [TIMER1\_CDTI1\_PA4](#a3b63381e36f0f67eecdb0e613e082acd)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x4) |
| #define | [TIMER1\_CDTI1\_PA5](#ae29404facb1a5712a8d3654c32abac03)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x5) |
| #define | [TIMER1\_CDTI1\_PA6](#a041c492c18debf15659b54a4d1acda45)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x6) |
| #define | [TIMER1\_CDTI1\_PA7](#ad2a111a49ac82b431c221b9b38a7eac2)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x7) |
| #define | [TIMER1\_CDTI1\_PA8](#a61f6fe07be3fdc75f7a137652ff6180b)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x0, 0x8) |
| #define | [TIMER1\_CDTI1\_PB0](#afe513e7286648f7e0dfdcd5831a158cb)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x1, 0x0) |
| #define | [TIMER1\_CDTI1\_PB1](#a231c7d9bddd4e56226c51a3ca0516290)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x1, 0x1) |
| #define | [TIMER1\_CDTI1\_PB2](#a5670dfed8891e8a39a4747b6a7536fa4)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x1, 0x2) |
| #define | [TIMER1\_CDTI1\_PB3](#aef5f7b0ad2e48af91779080e32da44b4)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x1, 0x3) |
| #define | [TIMER1\_CDTI1\_PB4](#aef8297dce3f2193d4367df88ab5bf20d)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x1, 0x4) |
| #define | [TIMER1\_CDTI1\_PC0](#a26cc959057976169dd4e4a4330bb34ff)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x0) |
| #define | [TIMER1\_CDTI1\_PC1](#a5be334fd1d01d68ebc4fbf77394adc03)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x1) |
| #define | [TIMER1\_CDTI1\_PC2](#a153d9a304ad237e9f99bf2fd97cb5ca3)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x2) |
| #define | [TIMER1\_CDTI1\_PC3](#ae1d146285574814c26941837ae32cf33)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x3) |
| #define | [TIMER1\_CDTI1\_PC4](#aadc34ad6a076211bfe55a1cecba057ed)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x4) |
| #define | [TIMER1\_CDTI1\_PC5](#a89667e375454960fd56fa87fd46a1cf0)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x5) |
| #define | [TIMER1\_CDTI1\_PC6](#ad60737f6dd9fe3c6f3d5039b3da8ffa5)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x6) |
| #define | [TIMER1\_CDTI1\_PC7](#ac285ce787120af33a48a91397f7e5d59)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x2, 0x7) |
| #define | [TIMER1\_CDTI1\_PD0](#a9a83a5c25369e4dc286c219f9be05a08)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x3, 0x0) |
| #define | [TIMER1\_CDTI1\_PD1](#ae2d334d95e5a2f65c92562727a87520b)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x3, 0x1) |
| #define | [TIMER1\_CDTI1\_PD2](#af1a5a15c236edb1c77acce4cb8d8b894)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x3, 0x2) |
| #define | [TIMER1\_CDTI1\_PD3](#a8b00bb8a1bbb8cc97e1e1997cd5ed10b)   [SILABS\_DBUS\_TIMER1\_CDTI1](#aff14e83dc5f27682d1d76ddb75d8b08c)(0x3, 0x3) |
| #define | [TIMER1\_CDTI2\_PA0](#ac959ddf75f8afe8179b53148e90a0cd3)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x0) |
| #define | [TIMER1\_CDTI2\_PA1](#a03028d392b456dbce8ce5c7325f52b87)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x1) |
| #define | [TIMER1\_CDTI2\_PA2](#a3282e1d97d899e3010b59e952aa12429)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x2) |
| #define | [TIMER1\_CDTI2\_PA3](#a249a669752eb8cfca1a9dee28e0fa5b9)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x3) |
| #define | [TIMER1\_CDTI2\_PA4](#acab3d281ca3eb0fc97c1c296beacb302)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x4) |
| #define | [TIMER1\_CDTI2\_PA5](#a1b4f4b4f2f84c99855ddfbdd829a0814)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x5) |
| #define | [TIMER1\_CDTI2\_PA6](#a4008736ae0d99019066eb6435864a043)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x6) |
| #define | [TIMER1\_CDTI2\_PA7](#ae07b3d64a4947e03736ac08ac816940f)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x7) |
| #define | [TIMER1\_CDTI2\_PA8](#a52cfa50fafa8bb77eb3d1a5b9e6c1c35)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x0, 0x8) |
| #define | [TIMER1\_CDTI2\_PB0](#a4ff755a9d12285c868a4dc0e5d9de281)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x1, 0x0) |
| #define | [TIMER1\_CDTI2\_PB1](#a94cb965aa4d6a7fb7a31acbd363f54ee)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x1, 0x1) |
| #define | [TIMER1\_CDTI2\_PB2](#a2b30a5c071a113e0c7693b1723aa0534)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x1, 0x2) |
| #define | [TIMER1\_CDTI2\_PB3](#ab41614ba724866ec0e55ae0837b4dc46)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x1, 0x3) |
| #define | [TIMER1\_CDTI2\_PB4](#a1388e138cdc0a50b805b4188aed036a0)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x1, 0x4) |
| #define | [TIMER1\_CDTI2\_PC0](#ab37f717d7232493a31424e87d242c2a8)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x0) |
| #define | [TIMER1\_CDTI2\_PC1](#a6a306946717970eb62df4307de771fef)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x1) |
| #define | [TIMER1\_CDTI2\_PC2](#a248af2da57a57600d4a144c71f860006)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x2) |
| #define | [TIMER1\_CDTI2\_PC3](#ae1c48f4b069d6c7e410511b1e95a7def)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x3) |
| #define | [TIMER1\_CDTI2\_PC4](#af91af878bbab4422378cf31a711055ff)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x4) |
| #define | [TIMER1\_CDTI2\_PC5](#ac16216ae2977f9696075b3a6d8c64aa0)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x5) |
| #define | [TIMER1\_CDTI2\_PC6](#aa59451e0e343327c7c1775367c4d9194)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x6) |
| #define | [TIMER1\_CDTI2\_PC7](#a6303e70615390644193cea172c375b4a)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x2, 0x7) |
| #define | [TIMER1\_CDTI2\_PD0](#ae362330bff63d204299a6a33f4c4f191)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x3, 0x0) |
| #define | [TIMER1\_CDTI2\_PD1](#a6559a7e28febb9e31fca6847e11cdb1a)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x3, 0x1) |
| #define | [TIMER1\_CDTI2\_PD2](#a8a53201b17d025911ca41f86e3d13a66)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x3, 0x2) |
| #define | [TIMER1\_CDTI2\_PD3](#a254d9132271304cd62f61184a40471d6)   [SILABS\_DBUS\_TIMER1\_CDTI2](#a33328da36cd2df624ded688165f9f319)(0x3, 0x3) |
| #define | [TIMER2\_CC0\_PA0](#a67e6f27f89e7e121cce88e0186ab5010)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x0) |
| #define | [TIMER2\_CC0\_PA1](#a545f09892c0762da7a55cdc8d16e8e6f)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x1) |
| #define | [TIMER2\_CC0\_PA2](#aee905018c0d9aa48c14e415474c03f62)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x2) |
| #define | [TIMER2\_CC0\_PA3](#ad7327f8fa42b7aa1875d2b57769330eb)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x3) |
| #define | [TIMER2\_CC0\_PA4](#acab7bd67fc01c7fa8b3c40d75f725a0a)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x4) |
| #define | [TIMER2\_CC0\_PA5](#ac846d48997b6bdbb2b7665a62a6505e3)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x5) |
| #define | [TIMER2\_CC0\_PA6](#a987c36e9761389522505ac50952ed04a)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x6) |
| #define | [TIMER2\_CC0\_PA7](#ae2170865d853ff19f2822feef4adb237)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x7) |
| #define | [TIMER2\_CC0\_PA8](#a76ee3427d6e4a4a9bba02acb045fc34c)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x0, 0x8) |
| #define | [TIMER2\_CC0\_PB0](#a2a9776f698e90b570e177a6a0059b15b)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x1, 0x0) |
| #define | [TIMER2\_CC0\_PB1](#a55d9652dbf9c89d894162860c56459dd)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x1, 0x1) |
| #define | [TIMER2\_CC0\_PB2](#a0c9bb962ddacf136ff3625459e3d7671)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x1, 0x2) |
| #define | [TIMER2\_CC0\_PB3](#a738b1a7965ce7945a6123c0b97606ac5)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x1, 0x3) |
| #define | [TIMER2\_CC0\_PB4](#aa0dcc265ed171092f14a0e54e7be712d)   [SILABS\_DBUS\_TIMER2\_CC0](#a6f8eec2f0d2289a845062b5fe14a59b7)(0x1, 0x4) |
| #define | [TIMER2\_CC1\_PA0](#a1164a4f1a0cfbf0cb157eeb7be84bd28)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x0) |
| #define | [TIMER2\_CC1\_PA1](#a1bca4d4f43da2d564d68622dcb0e5d9e)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x1) |
| #define | [TIMER2\_CC1\_PA2](#adec2ad20e72e0b8fd02b6476685f5155)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x2) |
| #define | [TIMER2\_CC1\_PA3](#a8a42dfc04580c2dba2b961509d03ff43)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x3) |
| #define | [TIMER2\_CC1\_PA4](#a89a293610575367134548bc2ccd0c47e)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x4) |
| #define | [TIMER2\_CC1\_PA5](#acdbcff934f4bac5a2b0f03a33e44138b)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x5) |
| #define | [TIMER2\_CC1\_PA6](#a4c420a0fc98b352544416bbfa8216ae6)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x6) |
| #define | [TIMER2\_CC1\_PA7](#a458c07160c2f3c3b6f12444c8f498167)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x7) |
| #define | [TIMER2\_CC1\_PA8](#ae91c030e51c7e07691257667d671d56e)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x0, 0x8) |
| #define | [TIMER2\_CC1\_PB0](#ac7397d7ebe41f5c2b732bece2b63f793)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x1, 0x0) |
| #define | [TIMER2\_CC1\_PB1](#a0d597a9083a41c950f29bbbf7e148ef7)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x1, 0x1) |
| #define | [TIMER2\_CC1\_PB2](#a45aeb569507fbd649e081575c136eb4a)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x1, 0x2) |
| #define | [TIMER2\_CC1\_PB3](#afb1a90f5d59b6ce2df0a231b4c6cd75c)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x1, 0x3) |
| #define | [TIMER2\_CC1\_PB4](#a833c1470f9dec67fe7e0d7b57c0c1dee)   [SILABS\_DBUS\_TIMER2\_CC1](#a1a5af09f79ed3f743efa31ec03d87cc6)(0x1, 0x4) |
| #define | [TIMER2\_CC2\_PA0](#a2d62e330c22411c86274caefb099cf19)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x0) |
| #define | [TIMER2\_CC2\_PA1](#aab60fb88a625e320ce64ea10133311df)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x1) |
| #define | [TIMER2\_CC2\_PA2](#a4bf049cdc3017e816165effd4cff7d35)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x2) |
| #define | [TIMER2\_CC2\_PA3](#a00eafe61a794b07af52d028ab4dd1adf)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x3) |
| #define | [TIMER2\_CC2\_PA4](#aedbc75bcf6c733bcd3deadb3c8ce0f21)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x4) |
| #define | [TIMER2\_CC2\_PA5](#a490ca0f07b93c2cd68351c6afb4a9819)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x5) |
| #define | [TIMER2\_CC2\_PA6](#abd8592d55f4ff8bd546adb9efc7ee922)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x6) |
| #define | [TIMER2\_CC2\_PA7](#a9d34e2111c7b45d5d7b36d0df3c80629)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x7) |
| #define | [TIMER2\_CC2\_PA8](#af969ac3be731d012befc6f7d2aef5fbe)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x0, 0x8) |
| #define | [TIMER2\_CC2\_PB0](#a59ed3f774f4d21a9f1fbc9d71cb57fe4)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x1, 0x0) |
| #define | [TIMER2\_CC2\_PB1](#abaf434275a10efbc0b32f7d859d51912)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x1, 0x1) |
| #define | [TIMER2\_CC2\_PB2](#ac4c83f10ee7ec2978b3612b8fdd8c6cb)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x1, 0x2) |
| #define | [TIMER2\_CC2\_PB3](#acc8b352f48014e5fd8a14f5d1d79d681)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x1, 0x3) |
| #define | [TIMER2\_CC2\_PB4](#a9add0713ccac926ac0a079bd7cd69aae)   [SILABS\_DBUS\_TIMER2\_CC2](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)(0x1, 0x4) |
| #define | [TIMER2\_CDTI0\_PA0](#a6cb932cba841a0987d78da39e11cadba)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x0) |
| #define | [TIMER2\_CDTI0\_PA1](#a9cde27e9bdb4e6157afe1149d35e8dbd)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x1) |
| #define | [TIMER2\_CDTI0\_PA2](#a5906c55b37b73111550ea2eb75681575)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x2) |
| #define | [TIMER2\_CDTI0\_PA3](#afa16ff7cf30f5cc4d2fe967263b9b2b0)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x3) |
| #define | [TIMER2\_CDTI0\_PA4](#ac0d736392f3d098ec5789189dc37036b)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x4) |
| #define | [TIMER2\_CDTI0\_PA5](#aa8c2a2712578b133cdbd8d07f1f37c24)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x5) |
| #define | [TIMER2\_CDTI0\_PA6](#a801b4531b9bb956d267c53f15b47a872)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x6) |
| #define | [TIMER2\_CDTI0\_PA7](#a36d14f2c4b029f787c6d474e41dd3dd8)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x7) |
| #define | [TIMER2\_CDTI0\_PA8](#ae1f424e362c402dcd38f0aaea7d059ac)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x0, 0x8) |
| #define | [TIMER2\_CDTI0\_PB0](#ad1c011c5437d75b74c56ebbb00e9dd65)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x1, 0x0) |
| #define | [TIMER2\_CDTI0\_PB1](#afedfcd3a53de2251bb61ccfed3af4a5f)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x1, 0x1) |
| #define | [TIMER2\_CDTI0\_PB2](#aab462dbb772296080bcfa7c0c9cb80fa)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x1, 0x2) |
| #define | [TIMER2\_CDTI0\_PB3](#adc08d2d352d4b14d201a11b6df7a64c9)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x1, 0x3) |
| #define | [TIMER2\_CDTI0\_PB4](#af02e9de67604ab16812a2b464cde99ae)   [SILABS\_DBUS\_TIMER2\_CDTI0](#a648ec3c8dafb7f88dba23ea50dba4e8b)(0x1, 0x4) |
| #define | [TIMER2\_CDTI1\_PA0](#ae901259c744451af8a8ded388dfe9f5d)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x0) |
| #define | [TIMER2\_CDTI1\_PA1](#a9e6e2fc9804d67ec073460ddf34fdd02)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x1) |
| #define | [TIMER2\_CDTI1\_PA2](#a7ac971aa8206899b4623057140243357)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x2) |
| #define | [TIMER2\_CDTI1\_PA3](#af174d0f8740b9d33ae66dba3e34b6031)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x3) |
| #define | [TIMER2\_CDTI1\_PA4](#afbda2d057823f529835a894ff9ad8629)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x4) |
| #define | [TIMER2\_CDTI1\_PA5](#a5b02e4c0ceb352d283a0e99cb05fddab)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x5) |
| #define | [TIMER2\_CDTI1\_PA6](#a5a930f094a10216d1b43a4eab6a359b7)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x6) |
| #define | [TIMER2\_CDTI1\_PA7](#add09acbb0fe8df1b64222f324163396b)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x7) |
| #define | [TIMER2\_CDTI1\_PA8](#a7f376eb3ffe07f95fa562c13244f3dd4)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x0, 0x8) |
| #define | [TIMER2\_CDTI1\_PB0](#a542b9626fdc82bd0444ecd2518031406)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x1, 0x0) |
| #define | [TIMER2\_CDTI1\_PB1](#a3600b995f1e40289444081210ad8430f)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x1, 0x1) |
| #define | [TIMER2\_CDTI1\_PB2](#ad87b20ae7e6e5876d5988a95be42720f)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x1, 0x2) |
| #define | [TIMER2\_CDTI1\_PB3](#a3174683951113d5d144bb0338014cbfd)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x1, 0x3) |
| #define | [TIMER2\_CDTI1\_PB4](#aaa89be3aa5b5b9cdbd4a693c5c9ffabe)   [SILABS\_DBUS\_TIMER2\_CDTI1](#ab124eb8882de0913d017f81a32eae6d8)(0x1, 0x4) |
| #define | [TIMER2\_CDTI2\_PA0](#a70028435f4fa81dc8504d6fb5562480c)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x0) |
| #define | [TIMER2\_CDTI2\_PA1](#af71768a49adaf60e74a77ff629b3ebd2)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x1) |
| #define | [TIMER2\_CDTI2\_PA2](#a56efa7077f3f025446f2c1937b833093)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x2) |
| #define | [TIMER2\_CDTI2\_PA3](#a288823b89fcc8c89d73c6865f8f69cc8)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x3) |
| #define | [TIMER2\_CDTI2\_PA4](#ab34c2728b9bc0054c854960165408494)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x4) |
| #define | [TIMER2\_CDTI2\_PA5](#af55eb46eaa2657c75df8b7c92119588c)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x5) |
| #define | [TIMER2\_CDTI2\_PA6](#a98e606b3b4ba2b0118736951d32b48ad)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x6) |
| #define | [TIMER2\_CDTI2\_PA7](#a1d1543914dacf30872f9d0bdeead7ce7)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x7) |
| #define | [TIMER2\_CDTI2\_PA8](#a8846303a4f61f979c77da532908f7f7b)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x0, 0x8) |
| #define | [TIMER2\_CDTI2\_PB0](#abd0220954a47f2fcf85f72971f2e7f8c)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x1, 0x0) |
| #define | [TIMER2\_CDTI2\_PB1](#ad82071aa4bb174e39da29be3a98e06f4)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x1, 0x1) |
| #define | [TIMER2\_CDTI2\_PB2](#a761808819fa59b8246ead762ee6dc88f)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x1, 0x2) |
| #define | [TIMER2\_CDTI2\_PB3](#af996eab47687d2ef9206856fe10266f8)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x1, 0x3) |
| #define | [TIMER2\_CDTI2\_PB4](#ad66c79e81d41281df4969d775c1e54c6)   [SILABS\_DBUS\_TIMER2\_CDTI2](#aac5b26da22ac4ef8f1f08354f8339130)(0x1, 0x4) |
| #define | [TIMER3\_CC0\_PC0](#adaa89be7653ebbb82d77f6ccd3ba117a)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x0) |
| #define | [TIMER3\_CC0\_PC1](#ac49977cf88186dd85de660d7dca24093)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x1) |
| #define | [TIMER3\_CC0\_PC2](#a943818c0b36e315772740e9260777e98)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x2) |
| #define | [TIMER3\_CC0\_PC3](#a3b4277fa7886db498357df495e7d0f5b)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x3) |
| #define | [TIMER3\_CC0\_PC4](#afef97dfceb1266dad39f3c06a28cccde)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x4) |
| #define | [TIMER3\_CC0\_PC5](#a850b7d20c5e78b8609f0b4ab737fb59e)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x5) |
| #define | [TIMER3\_CC0\_PC6](#a06fb13b5ae7a9758c47f1d12f54bb643)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x6) |
| #define | [TIMER3\_CC0\_PC7](#aba2b4f6a903913dd21c7f919ee2d4bfd)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x2, 0x7) |
| #define | [TIMER3\_CC0\_PD0](#a05f49738ea2e4cac6cff7b921761da01)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x3, 0x0) |
| #define | [TIMER3\_CC0\_PD1](#a4bf238e512342fc49c7a7d3fa1a13ee7)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x3, 0x1) |
| #define | [TIMER3\_CC0\_PD2](#a01e72605da25e5a408a0c3467be59205)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x3, 0x2) |
| #define | [TIMER3\_CC0\_PD3](#a3216588bd129dc8f82c27de826acb69b)   [SILABS\_DBUS\_TIMER3\_CC0](#adb617def54a24017bdcaafe228697dd5)(0x3, 0x3) |
| #define | [TIMER3\_CC1\_PC0](#a0911c0d09d2d62526ee7d69a0abf0206)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x0) |
| #define | [TIMER3\_CC1\_PC1](#afc5b3d4f06f9392ff91d1a04039cc106)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x1) |
| #define | [TIMER3\_CC1\_PC2](#a841b61a51502f96b4b4db51f1747ddc2)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x2) |
| #define | [TIMER3\_CC1\_PC3](#abe25ec49b962f68c7e0b782fe8b31e0c)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x3) |
| #define | [TIMER3\_CC1\_PC4](#aafcf7edadba216092137ea9ce0c0da17)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x4) |
| #define | [TIMER3\_CC1\_PC5](#ac24430c7e08b2e0fe7bc63f92c01f9b5)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x5) |
| #define | [TIMER3\_CC1\_PC6](#a3400ddc7e6f8c607251d0b8f049cc0f1)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x6) |
| #define | [TIMER3\_CC1\_PC7](#a440e269a870fa8411ca1584a653df6e8)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x2, 0x7) |
| #define | [TIMER3\_CC1\_PD0](#acb2b010357d2dd7e82266e1f530d93fc)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x3, 0x0) |
| #define | [TIMER3\_CC1\_PD1](#ac1cffc60caba52ee6ab100837b2b6cb3)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x3, 0x1) |
| #define | [TIMER3\_CC1\_PD2](#ac07495ddce953166e53c19d0a4f928fc)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x3, 0x2) |
| #define | [TIMER3\_CC1\_PD3](#a23644731303d1f1e527a7174ccef3e4a)   [SILABS\_DBUS\_TIMER3\_CC1](#ac522d8a27bbe4fcfba1e0cc282dee7c0)(0x3, 0x3) |
| #define | [TIMER3\_CC2\_PC0](#a7bf47abf6ea4ddf3f3e8dd71dcabc9f8)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x0) |
| #define | [TIMER3\_CC2\_PC1](#a2a2021e1cc5ec1156b6e3e8432a56dee)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x1) |
| #define | [TIMER3\_CC2\_PC2](#ad74e77cefd62c22a97737ab3eb7ce658)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x2) |
| #define | [TIMER3\_CC2\_PC3](#ab80ddb4234db5937e1244204d980e951)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x3) |
| #define | [TIMER3\_CC2\_PC4](#a717ccb54d7b93e7d4341f15ae10944cb)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x4) |
| #define | [TIMER3\_CC2\_PC5](#af10e6860473870cd0555e03907220ba7)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x5) |
| #define | [TIMER3\_CC2\_PC6](#aa221b71494071d6af232f0d8f9050aa7)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x6) |
| #define | [TIMER3\_CC2\_PC7](#adce105bc3d6134d45f130dfd77cfd59e)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x2, 0x7) |
| #define | [TIMER3\_CC2\_PD0](#a457c25d6e6cb832e66753dfc84d189f3)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x3, 0x0) |
| #define | [TIMER3\_CC2\_PD1](#adbeb6aa8891fdfe6510584bc8e5b5ced)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x3, 0x1) |
| #define | [TIMER3\_CC2\_PD2](#aa6524ad51bd80ac04276af0e722c5047)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x3, 0x2) |
| #define | [TIMER3\_CC2\_PD3](#ae94118e07443fa220d9162ad681c1a19)   [SILABS\_DBUS\_TIMER3\_CC2](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)(0x3, 0x3) |
| #define | [TIMER3\_CDTI0\_PC0](#a68db08edab7a0f208661895888ad0f4a)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x0) |
| #define | [TIMER3\_CDTI0\_PC1](#a3ae3f2df52006b2a53b70f7e940b8ed9)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x1) |
| #define | [TIMER3\_CDTI0\_PC2](#a1e3e29f3208cc7253d081b7c589632c1)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x2) |
| #define | [TIMER3\_CDTI0\_PC3](#a8ee6bc60c7704e1437c5d175df34d0a0)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x3) |
| #define | [TIMER3\_CDTI0\_PC4](#a6f98e4a7f4269972296fe587e83d0d7a)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x4) |
| #define | [TIMER3\_CDTI0\_PC5](#a348b50033a138bbc11ef6e99188fb023)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x5) |
| #define | [TIMER3\_CDTI0\_PC6](#aa744875bc8bbc9d504edf1022da599fd)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x6) |
| #define | [TIMER3\_CDTI0\_PC7](#a769a76d9258e7bdfdf7a8b21b70da011)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x2, 0x7) |
| #define | [TIMER3\_CDTI0\_PD0](#ae67b96fbcd3994e67f72d03f29690c02)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x3, 0x0) |
| #define | [TIMER3\_CDTI0\_PD1](#a477f3adb9d6430be9ef0746cba23b9fb)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x3, 0x1) |
| #define | [TIMER3\_CDTI0\_PD2](#a3ca82d8f98012743293a033b4c9c93be)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x3, 0x2) |
| #define | [TIMER3\_CDTI0\_PD3](#a3115a35f39b0b3f35120c728fc5c8c2f)   [SILABS\_DBUS\_TIMER3\_CDTI0](#abb9fc38bdcf044af8e89f8b5bd4eb339)(0x3, 0x3) |
| #define | [TIMER3\_CDTI1\_PC0](#a5dd1fea7f7ab7ee15a030b96a40d1114)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x0) |
| #define | [TIMER3\_CDTI1\_PC1](#aca7f55259fe2f36061078af791f3de4b)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x1) |
| #define | [TIMER3\_CDTI1\_PC2](#a03b1888fffa0036b1a9d92357d161cc7)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x2) |
| #define | [TIMER3\_CDTI1\_PC3](#a336444e4a0e7068e3e25e6908628c40c)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x3) |
| #define | [TIMER3\_CDTI1\_PC4](#a7c48bb98bfbace4681c6a1267d681e45)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x4) |
| #define | [TIMER3\_CDTI1\_PC5](#afa7ade2fc1198c66cd4812ac29befdf4)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x5) |
| #define | [TIMER3\_CDTI1\_PC6](#ad9ac8ee5259d40afead5b762ce90f4e6)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x6) |
| #define | [TIMER3\_CDTI1\_PC7](#af45d8db4d1da4526cce601e204743670)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x2, 0x7) |
| #define | [TIMER3\_CDTI1\_PD0](#a984b05d5d53c1068a86614a550995fc0)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x3, 0x0) |
| #define | [TIMER3\_CDTI1\_PD1](#a377c5ee038e274db1ddead0ad0fa7bf1)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x3, 0x1) |
| #define | [TIMER3\_CDTI1\_PD2](#a57207da12d6fa72e566b728371f4f402)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x3, 0x2) |
| #define | [TIMER3\_CDTI1\_PD3](#a18850fb5d2583d3652f7c43ea1d0ac39)   [SILABS\_DBUS\_TIMER3\_CDTI1](#a2c50f79deaf5192c644bb0b52832352d)(0x3, 0x3) |
| #define | [TIMER3\_CDTI2\_PC0](#a4a21cc75bb143d4fa1a84eb243fccc36)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x0) |
| #define | [TIMER3\_CDTI2\_PC1](#a881ccb7ad41ecf73423b97e8c489a6d0)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x1) |
| #define | [TIMER3\_CDTI2\_PC2](#aefbbc0a5e8e7673ccacdf399c288903e)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x2) |
| #define | [TIMER3\_CDTI2\_PC3](#abc867b08524924b26a2ed326a2b12155)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x3) |
| #define | [TIMER3\_CDTI2\_PC4](#a0befb875610ff387c2c1ac06f88d7b79)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x4) |
| #define | [TIMER3\_CDTI2\_PC5](#aea7c0881164e98c21fcf30d689deb592)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x5) |
| #define | [TIMER3\_CDTI2\_PC6](#a2a4909305fd0dbde0c3caba5f32fc896)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x6) |
| #define | [TIMER3\_CDTI2\_PC7](#a481f5eb7e5d4c148bc2be3d958973577)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x2, 0x7) |
| #define | [TIMER3\_CDTI2\_PD0](#a228392afbba95bbb69a65aae20dbb2d1)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x3, 0x0) |
| #define | [TIMER3\_CDTI2\_PD1](#a162d7a8c85197e047bc65cef7235a591)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x3, 0x1) |
| #define | [TIMER3\_CDTI2\_PD2](#a7f3873fb6abfaf970024318529fcfcd5)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x3, 0x2) |
| #define | [TIMER3\_CDTI2\_PD3](#a0c3fc7049d7dacfedfc4a04ced71202f)   [SILABS\_DBUS\_TIMER3\_CDTI2](#a5f8e118916558ec753791e59baeefef0)(0x3, 0x3) |
| #define | [TIMER4\_CC0\_PA0](#aa0c6e5e3f769ae31848239ea16fc8c26)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x0) |
| #define | [TIMER4\_CC0\_PA1](#ac49460d333f18f30fe332cad4ead4719)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x1) |
| #define | [TIMER4\_CC0\_PA2](#a92254bd9362d97e1fe55f8e9a7036857)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x2) |
| #define | [TIMER4\_CC0\_PA3](#a5c83b195cb0fd5344c2ec05a8547a063)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x3) |
| #define | [TIMER4\_CC0\_PA4](#a0daf9dc92bab78111bfc9425c38ba671)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x4) |
| #define | [TIMER4\_CC0\_PA5](#aebea07333a9390eb469f7efc8d4e773c)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x5) |
| #define | [TIMER4\_CC0\_PA6](#a88bab7bd85be0c93a81f359d872e65f2)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x6) |
| #define | [TIMER4\_CC0\_PA7](#ab527597383a746f75328fd7877d96389)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x7) |
| #define | [TIMER4\_CC0\_PA8](#af7ef30e6d27885e8f6eacdced332012d)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x0, 0x8) |
| #define | [TIMER4\_CC0\_PB0](#a6a53b58cd4ff5c60b736cbe9d25954fa)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x1, 0x0) |
| #define | [TIMER4\_CC0\_PB1](#a778ea39ff864aad8a92e35859bb1ec97)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x1, 0x1) |
| #define | [TIMER4\_CC0\_PB2](#a2fecff946d39c7745e061f2a4a4a03b7)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x1, 0x2) |
| #define | [TIMER4\_CC0\_PB3](#a1e7beb8ae86e28ef5a122118644a0b6d)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x1, 0x3) |
| #define | [TIMER4\_CC0\_PB4](#a99a47cb9b6cb9273332d2a8f6598a52f)   [SILABS\_DBUS\_TIMER4\_CC0](#ab5f1949dfc60e6afa576f77ac645a367)(0x1, 0x4) |
| #define | [TIMER4\_CC1\_PA0](#a0a20fe004087b6d6599f775aefac56f2)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x0) |
| #define | [TIMER4\_CC1\_PA1](#a044a7b8e14be441705f29e4b6015ee08)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x1) |
| #define | [TIMER4\_CC1\_PA2](#adbd211cd9344a88c6301462a5e3edc51)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x2) |
| #define | [TIMER4\_CC1\_PA3](#a5a04fcf2fff3afd10e98cb2e31509cc5)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x3) |
| #define | [TIMER4\_CC1\_PA4](#a8d301ec962fe2cce8ba002f274988559)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x4) |
| #define | [TIMER4\_CC1\_PA5](#a102bc4ebc9988c58529e288cbae2dcf5)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x5) |
| #define | [TIMER4\_CC1\_PA6](#a3ea21e7b459ab219ee593f4ded6423d6)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x6) |
| #define | [TIMER4\_CC1\_PA7](#afbf528e09cd5f8416ad6a21bf15e6dc7)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x7) |
| #define | [TIMER4\_CC1\_PA8](#a5b53aae41cdc44147d6333ce5d7c28aa)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x0, 0x8) |
| #define | [TIMER4\_CC1\_PB0](#a65dd111e27e3d7ba7cec249ea3354ff4)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x1, 0x0) |
| #define | [TIMER4\_CC1\_PB1](#ac64bc36ec5794d92ac2bf256147645f5)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x1, 0x1) |
| #define | [TIMER4\_CC1\_PB2](#a38afb957c997a8378e3aebb6141f7426)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x1, 0x2) |
| #define | [TIMER4\_CC1\_PB3](#a280bb1ebea122956c890dcb8d84b2241)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x1, 0x3) |
| #define | [TIMER4\_CC1\_PB4](#a767e437a09fa17b72c8c3f9c7dfdbf60)   [SILABS\_DBUS\_TIMER4\_CC1](#a9de72de2effcb9f9efdecf8925cbbf57)(0x1, 0x4) |
| #define | [TIMER4\_CC2\_PA0](#a777870e82a20af4a6a6e71a5b636fca6)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x0) |
| #define | [TIMER4\_CC2\_PA1](#a85d5e0d8c945839bbda1cdcfb1c27952)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x1) |
| #define | [TIMER4\_CC2\_PA2](#a1e87cfdb2f81b1168fd9fd61e4451103)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x2) |
| #define | [TIMER4\_CC2\_PA3](#a3a16aab894717ffae5bcb0ab14cc6dbb)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x3) |
| #define | [TIMER4\_CC2\_PA4](#a2dfa60f8a9d458a782ab2df7f2209976)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x4) |
| #define | [TIMER4\_CC2\_PA5](#a8a3aac099645db504605942c9e86083f)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x5) |
| #define | [TIMER4\_CC2\_PA6](#a73ab6a5f63c5e2c778913a196c49915f)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x6) |
| #define | [TIMER4\_CC2\_PA7](#a1f5ce55fa587d01d50b1f8496b4c2640)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x7) |
| #define | [TIMER4\_CC2\_PA8](#a13b0916acd52e39c467b2ae7c8f08e22)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x0, 0x8) |
| #define | [TIMER4\_CC2\_PB0](#a1965744950bba0b98b124ef7fd308538)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x1, 0x0) |
| #define | [TIMER4\_CC2\_PB1](#af51b2d503e11e751815cc9e46c777cc8)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x1, 0x1) |
| #define | [TIMER4\_CC2\_PB2](#a9ae5f6cda5ee8fc6551a58bc1dea1b6a)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x1, 0x2) |
| #define | [TIMER4\_CC2\_PB3](#a4033b892135db2f425c041fb353dd94e)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x1, 0x3) |
| #define | [TIMER4\_CC2\_PB4](#ab9f0f4839c1db0ff24c71e8a43bca20b)   [SILABS\_DBUS\_TIMER4\_CC2](#ae37d483d35f11fd70fa4cd48a7718ab9)(0x1, 0x4) |
| #define | [TIMER4\_CDTI0\_PA0](#a7a3baa51540b54c8677085fce6fdff99)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x0) |
| #define | [TIMER4\_CDTI0\_PA1](#a46ad78924a9aebe629236e072c1c013b)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x1) |
| #define | [TIMER4\_CDTI0\_PA2](#ab302b8f1cc1c0b103e4a315173af2455)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x2) |
| #define | [TIMER4\_CDTI0\_PA3](#a6cabbf3093dc73c82ab34ffd0a979b9e)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x3) |
| #define | [TIMER4\_CDTI0\_PA4](#a228a5febbceec760f773b1114a978c12)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x4) |
| #define | [TIMER4\_CDTI0\_PA5](#a44b20d92c88a15471c81f3f408126476)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x5) |
| #define | [TIMER4\_CDTI0\_PA6](#a2c06384e73db9a53f2a46c79991f022e)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x6) |
| #define | [TIMER4\_CDTI0\_PA7](#a1ccb51b05ade839e65eb898115a09a1f)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x7) |
| #define | [TIMER4\_CDTI0\_PA8](#aec88b0761fc5162dfa63daaaf0d8dd80)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x0, 0x8) |
| #define | [TIMER4\_CDTI0\_PB0](#a7417d210f904b5448a079950b92d7e85)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x1, 0x0) |
| #define | [TIMER4\_CDTI0\_PB1](#a5943529095abd138015248fc122f0af1)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x1, 0x1) |
| #define | [TIMER4\_CDTI0\_PB2](#aeffc25dbbbc7d1eb199cd29b7cf7e0a0)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x1, 0x2) |
| #define | [TIMER4\_CDTI0\_PB3](#aeda432d234c691de7a000702c9e13ba4)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x1, 0x3) |
| #define | [TIMER4\_CDTI0\_PB4](#a128f18c80a9343d189b856d1d4f3b128)   [SILABS\_DBUS\_TIMER4\_CDTI0](#a7a9532d9136447f798581c3f11f6608f)(0x1, 0x4) |
| #define | [TIMER4\_CDTI1\_PA0](#a2c8f5c89e8e8d8acf768efc55c2c1557)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x0) |
| #define | [TIMER4\_CDTI1\_PA1](#aeec9e93ade4349a932987805b56427ea)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x1) |
| #define | [TIMER4\_CDTI1\_PA2](#a5504301d2109fd9b938b6d2183e1e23f)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x2) |
| #define | [TIMER4\_CDTI1\_PA3](#a9baa482a3d5caf216a47294c2b74b060)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x3) |
| #define | [TIMER4\_CDTI1\_PA4](#a84c9ec2e762283faf0804fdc2d4b8e67)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x4) |
| #define | [TIMER4\_CDTI1\_PA5](#abc07eda4d4f0a0a189628e9e2e7eed05)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x5) |
| #define | [TIMER4\_CDTI1\_PA6](#a1b72f464803bcaa51f912a41e0d92023)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x6) |
| #define | [TIMER4\_CDTI1\_PA7](#a8c6b70c5db7bf891a3fb608f7f50e3f1)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x7) |
| #define | [TIMER4\_CDTI1\_PA8](#ac2bab95ab6f8067049fc144683ce0e77)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x0, 0x8) |
| #define | [TIMER4\_CDTI1\_PB0](#a9897ffcb326b237d2258b7fbd32111c9)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x1, 0x0) |
| #define | [TIMER4\_CDTI1\_PB1](#a8ffdf1e7b414a675d6ea582e30047251)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x1, 0x1) |
| #define | [TIMER4\_CDTI1\_PB2](#a8bc164f77d9311ae19c11eb993724a96)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x1, 0x2) |
| #define | [TIMER4\_CDTI1\_PB3](#a2feb1f73241aaedd10d1f30a8402fb6f)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x1, 0x3) |
| #define | [TIMER4\_CDTI1\_PB4](#a1a7a79e99bf52e3f2c6241608c7fc814)   [SILABS\_DBUS\_TIMER4\_CDTI1](#aa3a6b5984b119e066af677767169f2f8)(0x1, 0x4) |
| #define | [TIMER4\_CDTI2\_PA0](#a0167c1d5682489dcfdd9d60fa1a2cc44)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x0) |
| #define | [TIMER4\_CDTI2\_PA1](#a8c51fb1efbd523ef8d5b57b66d65060f)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x1) |
| #define | [TIMER4\_CDTI2\_PA2](#aea7d724240277e0a0b3c2334063e6b6a)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x2) |
| #define | [TIMER4\_CDTI2\_PA3](#ab8588c060f8671f5696a0e2529394a37)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x3) |
| #define | [TIMER4\_CDTI2\_PA4](#a4c566e93e8f5375744be6303f5049840)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x4) |
| #define | [TIMER4\_CDTI2\_PA5](#a4218800d01dc2d8e767d1e03e28c00e4)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x5) |
| #define | [TIMER4\_CDTI2\_PA6](#af9c15b67b7e09875d5a9991dac81222f)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x6) |
| #define | [TIMER4\_CDTI2\_PA7](#a664bd862ef44614302fe82a809d1f148)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x7) |
| #define | [TIMER4\_CDTI2\_PA8](#ad20202f301b5e59f477ab02d6ee37546)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x0, 0x8) |
| #define | [TIMER4\_CDTI2\_PB0](#a35aa90b994c639d68f2a8bbd65903494)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x1, 0x0) |
| #define | [TIMER4\_CDTI2\_PB1](#a20970e543f42e4785409f8f391d6daa9)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x1, 0x1) |
| #define | [TIMER4\_CDTI2\_PB2](#aee236ba0af0b2d08871f15ca7d78cd2c)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x1, 0x2) |
| #define | [TIMER4\_CDTI2\_PB3](#a976af94ec2e61f8b59edebf73e3222f0)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x1, 0x3) |
| #define | [TIMER4\_CDTI2\_PB4](#a03b1a79e2c32ed563d6ebf81b9741d14)   [SILABS\_DBUS\_TIMER4\_CDTI2](#ae21486ec9db5e77200e89be6227e33af)(0x1, 0x4) |
| #define | [USART0\_CS\_PA0](#a8b31d0e72dc71f813f3ae21da1b064dc)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x0) |
| #define | [USART0\_CS\_PA1](#affbbbbf6348af411b5392e462304edee)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x1) |
| #define | [USART0\_CS\_PA2](#a70d22cbabea10e31293a21262f6a64b3)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x2) |
| #define | [USART0\_CS\_PA3](#a2a80bc71c923ed7c6fd2865d869864fc)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x3) |
| #define | [USART0\_CS\_PA4](#af24e43481767fe27cdd78f5e27f15d7f)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x4) |
| #define | [USART0\_CS\_PA5](#a7cb722df10819495d5059933ddf122a4)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x5) |
| #define | [USART0\_CS\_PA6](#a94d45fdffdc79cc92994105238c9f0f8)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x6) |
| #define | [USART0\_CS\_PA7](#a75603bdb24ba0f19a841a1ed7b3fc683)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x7) |
| #define | [USART0\_CS\_PA8](#a2eb48dfecd71b07998cff24d69052360)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x0, 0x8) |
| #define | [USART0\_CS\_PB0](#a5f92c862131c6dfd2dc95146cdfa09aa)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x1, 0x0) |
| #define | [USART0\_CS\_PB1](#aa45d4cfe63813c6c8aa8602e0783f7fb)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x1, 0x1) |
| #define | [USART0\_CS\_PB2](#a8d25b8c147a7d0777e023a56bc47b5ea)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x1, 0x2) |
| #define | [USART0\_CS\_PB3](#a8a749535093e7817f27396459ee97d72)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x1, 0x3) |
| #define | [USART0\_CS\_PB4](#a25fa64c3232371544eba09423fb0c765)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x1, 0x4) |
| #define | [USART0\_CS\_PC0](#a2372be5754b13cafcef6a63d63548924)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x0) |
| #define | [USART0\_CS\_PC1](#a0033eb0ea09f9dab2ab5a20d185ba0e0)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x1) |
| #define | [USART0\_CS\_PC2](#afdc21300ca9ab485a7d97fa344ee3292)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x2) |
| #define | [USART0\_CS\_PC3](#acc373a1b4402c4f4f229524837a4c3ac)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x3) |
| #define | [USART0\_CS\_PC4](#a3bb143a83558aaa91fad609259a13044)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x4) |
| #define | [USART0\_CS\_PC5](#ab4ae79a567d023b7f886019e3d5518b1)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x5) |
| #define | [USART0\_CS\_PC6](#a8ad8102bed214716bdcf82c1747e2ce3)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x6) |
| #define | [USART0\_CS\_PC7](#a3f1d10140e34a916172f4ccfeb086fea)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x2, 0x7) |
| #define | [USART0\_CS\_PD0](#a4d2ef2ccd5f3dbefa048e37f2bb40b8b)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x3, 0x0) |
| #define | [USART0\_CS\_PD1](#a1f6089f92cf5168cbd9a6daa0f336ebb)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x3, 0x1) |
| #define | [USART0\_CS\_PD2](#a4e54dcbabdbebe60f309a31c7acbe30f)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x3, 0x2) |
| #define | [USART0\_CS\_PD3](#a00073504dbe55119dc3dac466c5f816f)   [SILABS\_DBUS\_USART0\_CS](#acc127783c3de46fa1efd6bf86f632807)(0x3, 0x3) |
| #define | [USART0\_RTS\_PA0](#a104b44454bfafbbdd54fe6b53c2dff33)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x0) |
| #define | [USART0\_RTS\_PA1](#abbaf9c9b55c0673fc774610b83aca313)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x1) |
| #define | [USART0\_RTS\_PA2](#abaae8c12c4daa90d49e9f327f16a6691)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x2) |
| #define | [USART0\_RTS\_PA3](#a4ba035c607b639dfef668323a43a3f7f)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x3) |
| #define | [USART0\_RTS\_PA4](#a234727fb3ae07a22c350d4a0a58c30cb)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x4) |
| #define | [USART0\_RTS\_PA5](#a0f8ad339a81f02d95e747a82aefe699e)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x5) |
| #define | [USART0\_RTS\_PA6](#afcab39462b0cc95e3984b4a10e54b587)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x6) |
| #define | [USART0\_RTS\_PA7](#ae4f01f02accb203b696d25f69e4d1c2a)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x7) |
| #define | [USART0\_RTS\_PA8](#a3894dc798fe8561bba8836323f63aea4)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x0, 0x8) |
| #define | [USART0\_RTS\_PB0](#a9808fc5b30607e6d0cbc3172369b818d)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x1, 0x0) |
| #define | [USART0\_RTS\_PB1](#a44240f09f67e09e58d28f82c43aff37d)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x1, 0x1) |
| #define | [USART0\_RTS\_PB2](#aa09ddd73916db94f88c710526689253d)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x1, 0x2) |
| #define | [USART0\_RTS\_PB3](#a7db53ff445baf566a0fcb7ce25532bb8)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x1, 0x3) |
| #define | [USART0\_RTS\_PB4](#ad1f91a8c2838f4b2f25240330b3144c3)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x1, 0x4) |
| #define | [USART0\_RTS\_PC0](#a2023f5afe82a2b2ff9b6c00bb249367b)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x0) |
| #define | [USART0\_RTS\_PC1](#a59cd7521827677160d85555c25430a9b)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x1) |
| #define | [USART0\_RTS\_PC2](#af7675ade342b55e04078f3d53306ca45)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x2) |
| #define | [USART0\_RTS\_PC3](#a42798ba22452bc2850007c9871d9daee)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x3) |
| #define | [USART0\_RTS\_PC4](#ae54415286b298aceaebdddcb3d008f5b)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x4) |
| #define | [USART0\_RTS\_PC5](#a6490fddb874c99a2cc293342c1b58dfc)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x5) |
| #define | [USART0\_RTS\_PC6](#ac72929dbdc13592ff0c46515bfc9169b)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x6) |
| #define | [USART0\_RTS\_PC7](#a88f8735b06c99e4851ee982a6ced5412)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x2, 0x7) |
| #define | [USART0\_RTS\_PD0](#a705598d6a60acd8936d6b7d0aa18cba2)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x3, 0x0) |
| #define | [USART0\_RTS\_PD1](#af77229ee4cf9eac56cc2fb134bc805c4)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x3, 0x1) |
| #define | [USART0\_RTS\_PD2](#a6a6bf570ad629ce3c81b37d31ffa2efe)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x3, 0x2) |
| #define | [USART0\_RTS\_PD3](#a0f8639b93ef710b631309b9388fbcb50)   [SILABS\_DBUS\_USART0\_RTS](#afb90351e31f6da6446c2fc3f5aaaf394)(0x3, 0x3) |
| #define | [USART0\_RX\_PA0](#aacdc76948ed8f1e54f8e260e62c89f61)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x0) |
| #define | [USART0\_RX\_PA1](#af41b4722d7b89c28645c24ac8e9a5eb4)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x1) |
| #define | [USART0\_RX\_PA2](#a4da72ddcfaf102aa817eb2bc6e0c5cbb)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x2) |
| #define | [USART0\_RX\_PA3](#a0a9b80333130d05d11bf88c78434221a)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x3) |
| #define | [USART0\_RX\_PA4](#ac992577a6d9d5e0730eaaaa2086d5802)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x4) |
| #define | [USART0\_RX\_PA5](#a8203de9111610660eea0c49ef51a9f6a)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x5) |
| #define | [USART0\_RX\_PA6](#a84a42fda6d1b7a2269c357e2929b8219)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x6) |
| #define | [USART0\_RX\_PA7](#a2f2a30bbb2a5b9e4d99ffb78545bbf3b)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x7) |
| #define | [USART0\_RX\_PA8](#af982046455e2567919abe51956e83c10)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x0, 0x8) |
| #define | [USART0\_RX\_PB0](#ab6691b3280f611c94c8690302bce85d5)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x1, 0x0) |
| #define | [USART0\_RX\_PB1](#ab23c92ad1cb6a8cafe055baade2e8b87)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x1, 0x1) |
| #define | [USART0\_RX\_PB2](#ace83f4be0c630151d9e59c4c21a40109)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x1, 0x2) |
| #define | [USART0\_RX\_PB3](#ad2268a788d647414dd9ef5dba5bbed19)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x1, 0x3) |
| #define | [USART0\_RX\_PB4](#ab17af03ccdc989dd4c8e28173d1a3b39)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x1, 0x4) |
| #define | [USART0\_RX\_PC0](#aee4369f8682feee79f184c83d80274da)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x0) |
| #define | [USART0\_RX\_PC1](#a9350586833a3d5c48baefd1610c13f62)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x1) |
| #define | [USART0\_RX\_PC2](#a0a895e2c1e4a38b1fe6ebd5da7d525e5)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x2) |
| #define | [USART0\_RX\_PC3](#a437d4a2cea5c64fc92b6c99b87bf5e8c)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x3) |
| #define | [USART0\_RX\_PC4](#a75a6d4f4d7656eea8244bfb0d030ca79)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x4) |
| #define | [USART0\_RX\_PC5](#a869fb6d64ec0e62beecb34dd0279f202)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x5) |
| #define | [USART0\_RX\_PC6](#ad6902172e17c7f2c920e4658151182cd)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x6) |
| #define | [USART0\_RX\_PC7](#ab5f98edf5748c59adffddbe6c3e032d6)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x2, 0x7) |
| #define | [USART0\_RX\_PD0](#a823861421794933ab4e682de63e49cc4)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x3, 0x0) |
| #define | [USART0\_RX\_PD1](#a408c8b04c4e9598c9bb139446244810f)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x3, 0x1) |
| #define | [USART0\_RX\_PD2](#ad11874063a494e22191887fbd29d0189)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x3, 0x2) |
| #define | [USART0\_RX\_PD3](#a0dbbdc55667cd4c32262a7e91298cf95)   [SILABS\_DBUS\_USART0\_RX](#a8d9bee07c90a69ada0a392fbd15c9e44)(0x3, 0x3) |
| #define | [USART0\_CLK\_PA0](#a16af201487286a8bad218c94245a88c7)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x0) |
| #define | [USART0\_CLK\_PA1](#a1c3041ba213cdbcb2796dbffa01b8571)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x1) |
| #define | [USART0\_CLK\_PA2](#a1e546e7130f7012f29d6d2aad3e97b39)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x2) |
| #define | [USART0\_CLK\_PA3](#aa78910cf4b3c816508e2e97288489f16)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x3) |
| #define | [USART0\_CLK\_PA4](#a76684ba202fa4fb3b5e545a031f0c841)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x4) |
| #define | [USART0\_CLK\_PA5](#a92cda8774c81ce2539654516c2b62dd6)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x5) |
| #define | [USART0\_CLK\_PA6](#a6c67ed947caacf669665e133327a7e00)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x6) |
| #define | [USART0\_CLK\_PA7](#af8f2d47db5aa651708f0d2dea2e39c48)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x7) |
| #define | [USART0\_CLK\_PA8](#a06fdcd2c3ae7b6162aff6a3fbeac94a8)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x0, 0x8) |
| #define | [USART0\_CLK\_PB0](#a80303adbfa7489fdefcbf14b38c25194)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x1, 0x0) |
| #define | [USART0\_CLK\_PB1](#a242754151600f954e6c9063254862537)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x1, 0x1) |
| #define | [USART0\_CLK\_PB2](#a8ed2cedbe7fd2daf10bee286f2bb6468)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x1, 0x2) |
| #define | [USART0\_CLK\_PB3](#abe23ca58f25d6bfa5b939cf58d7a0dee)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x1, 0x3) |
| #define | [USART0\_CLK\_PB4](#abac165e111f292793ab41b4411ad847c)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x1, 0x4) |
| #define | [USART0\_CLK\_PC0](#a9504215a474950cdc3ae3e76bb0ee428)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x0) |
| #define | [USART0\_CLK\_PC1](#aa03060eb71eadfc578315d600f297665)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x1) |
| #define | [USART0\_CLK\_PC2](#afd46249fb73936581af6f762bf749096)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x2) |
| #define | [USART0\_CLK\_PC3](#a39fd0a4cefb1903103818add5272cb69)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x3) |
| #define | [USART0\_CLK\_PC4](#a86e90f6c37f90fb2c79d163239123815)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x4) |
| #define | [USART0\_CLK\_PC5](#a13955f88c0655104ccceaf72d8fcc000)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x5) |
| #define | [USART0\_CLK\_PC6](#acd2b16c2082f7bbb996a7ba08a9339f6)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x6) |
| #define | [USART0\_CLK\_PC7](#af26cd974218fae8b631ed6bbc3505da6)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x2, 0x7) |
| #define | [USART0\_CLK\_PD0](#aa5dd3eff1b983555e7437c815d69d6c1)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x3, 0x0) |
| #define | [USART0\_CLK\_PD1](#a808576a293b84b259f0b749099ee53f0)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x3, 0x1) |
| #define | [USART0\_CLK\_PD2](#aba6f9004672cd8fcc046036c5a5e385d)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x3, 0x2) |
| #define | [USART0\_CLK\_PD3](#acf11ed64457d633e70ba8551caaad511)   [SILABS\_DBUS\_USART0\_CLK](#a14f60bd84a682fe99ccd93607ca87d6b)(0x3, 0x3) |
| #define | [USART0\_TX\_PA0](#a4691259ca7c910831f70cff06b9737ac)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x0) |
| #define | [USART0\_TX\_PA1](#af4e1c897ae049a4b223e09ab587f116d)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x1) |
| #define | [USART0\_TX\_PA2](#acc13e25bcc1953b93e76521966cd1b39)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x2) |
| #define | [USART0\_TX\_PA3](#a2ccdea01de2b8da884a33ddc1a81982f)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x3) |
| #define | [USART0\_TX\_PA4](#a28450d0bc2dcbe2ead4d36cf3800eb03)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x4) |
| #define | [USART0\_TX\_PA5](#ab3851360e615c31434f53597b8012217)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x5) |
| #define | [USART0\_TX\_PA6](#a50d32b162eb8cfaee3228b4dd1aa2aef)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x6) |
| #define | [USART0\_TX\_PA7](#a237580d1c4d056bd0008418d21d8f1b3)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x7) |
| #define | [USART0\_TX\_PA8](#ae63baa716abe02654ea80133e8c84bd9)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x0, 0x8) |
| #define | [USART0\_TX\_PB0](#a7af0455dce2acd605ef61cdc726c3177)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x1, 0x0) |
| #define | [USART0\_TX\_PB1](#a6ccc48b5e17aca0e2aefe341f9519ae9)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x1, 0x1) |
| #define | [USART0\_TX\_PB2](#a76f27605a95ea657c40e6911019756ec)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x1, 0x2) |
| #define | [USART0\_TX\_PB3](#a820d4c384913206beec9312430e68f9a)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x1, 0x3) |
| #define | [USART0\_TX\_PB4](#a3e2d2b7e3a0f2da1fd63cab3943aec5e)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x1, 0x4) |
| #define | [USART0\_TX\_PC0](#a63c1a984a64cb3c40643a7e38c20caaa)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x0) |
| #define | [USART0\_TX\_PC1](#ac501027215a6551a637bacf8d1d406fa)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x1) |
| #define | [USART0\_TX\_PC2](#ac1b7aad7c958ba2d2cfa2622318ac3c2)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x2) |
| #define | [USART0\_TX\_PC3](#aa215f604dc67f092f495c472de9a7ed5)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x3) |
| #define | [USART0\_TX\_PC4](#a1d49c843687f02f806c122059ac08a0c)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x4) |
| #define | [USART0\_TX\_PC5](#a03580c3dc9b22d031f78a0a3051b25de)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x5) |
| #define | [USART0\_TX\_PC6](#a3dc09745738d16673493a74870e6df5b)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x6) |
| #define | [USART0\_TX\_PC7](#a9c846b6972a8263d37ea9473b022f2dc)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x2, 0x7) |
| #define | [USART0\_TX\_PD0](#a6756b78da6f6228f331b11a1a17be09d)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x3, 0x0) |
| #define | [USART0\_TX\_PD1](#a1a2e17d5a9daefa68e67b96957271b67)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x3, 0x1) |
| #define | [USART0\_TX\_PD2](#af52dcac08d3d9e0757048dbe7e0394b2)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x3, 0x2) |
| #define | [USART0\_TX\_PD3](#a51ef7d6af85db7597dd27a68c75fe4e9)   [SILABS\_DBUS\_USART0\_TX](#aca2a3d6b7903947d127d8b6ea5d8c84a)(0x3, 0x3) |
| #define | [USART0\_CTS\_PA0](#ac3ca642f56ef830b82675e79f7741f3b)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x0) |
| #define | [USART0\_CTS\_PA1](#afe282cc2c0b48daca846099518f85197)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x1) |
| #define | [USART0\_CTS\_PA2](#abb4ee35f35c67053d9e499b9b6586848)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x2) |
| #define | [USART0\_CTS\_PA3](#ac7c103a6f291a3ba02c78b56cda7522e)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x3) |
| #define | [USART0\_CTS\_PA4](#adf4ae6f16534af5c18b924890e70b909)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x4) |
| #define | [USART0\_CTS\_PA5](#a375e4336fc59220a304beb9e818038a8)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x5) |
| #define | [USART0\_CTS\_PA6](#a34bdfb80ac61bcde4828b64e5ab7bc6a)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x6) |
| #define | [USART0\_CTS\_PA7](#afe45fe9337ee945b705d60efd975071a)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x7) |
| #define | [USART0\_CTS\_PA8](#a45cbf3ce6396ad5caf50bca5bb336f04)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x0, 0x8) |
| #define | [USART0\_CTS\_PB0](#a5e6fd192eef4cb50593c5f8f225607db)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x1, 0x0) |
| #define | [USART0\_CTS\_PB1](#a8ba9df244ac2a7e580a45372c6db1496)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x1, 0x1) |
| #define | [USART0\_CTS\_PB2](#ac99b8ee386e51b37acfe825e4111dbd4)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x1, 0x2) |
| #define | [USART0\_CTS\_PB3](#a0c63835444cc57f402820f473de55618)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x1, 0x3) |
| #define | [USART0\_CTS\_PB4](#a2da02e86c7776fb1674ad0235c3c342a)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x1, 0x4) |
| #define | [USART0\_CTS\_PC0](#a176d8e361297cf55c78d425fed824f1f)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x0) |
| #define | [USART0\_CTS\_PC1](#acae624423e070b271d7c62019dc19ca6)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x1) |
| #define | [USART0\_CTS\_PC2](#a11af346f3b4cd506e5f42d802eeaa7fa)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x2) |
| #define | [USART0\_CTS\_PC3](#acde9eb8d5c61ec7fa0c66248de8acdb3)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x3) |
| #define | [USART0\_CTS\_PC4](#a0c7d39bd6f59e8a9281d68560e3ea0cc)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x4) |
| #define | [USART0\_CTS\_PC5](#aa2c0ec406645422286f3099c880051e8)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x5) |
| #define | [USART0\_CTS\_PC6](#a8886647e93011bfd9253bf57af7451f0)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x6) |
| #define | [USART0\_CTS\_PC7](#a8fc778b9808ef6cad5104cdee4c8b305)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x2, 0x7) |
| #define | [USART0\_CTS\_PD0](#ad8f9198b67b3777baf4d6fa6771c2a40)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x3, 0x0) |
| #define | [USART0\_CTS\_PD1](#acf9112247d4fa36974b7e221d156b27c)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x3, 0x1) |
| #define | [USART0\_CTS\_PD2](#a86617a975bc950800ea9deba65ffaa19)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x3, 0x2) |
| #define | [USART0\_CTS\_PD3](#abf78324d648e5c035d29a33b4b93dd82)   [SILABS\_DBUS\_USART0\_CTS](#a0be14ba61b5fc707ef02e7ac6ba779cf)(0x3, 0x3) |
| #define | [USART1\_CS\_PA0](#ad3e622bf87194cc1b199a28fbf82c922)   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x0, 0x0) |
| #define | [USART1\_CS\_PA1](#ac44b9afd3f4aacf4b5d77a6ffed82c31)   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x0, 0x1) |
| #define | [USART1\_CS\_PA2](#ab2817f18abf86707ce4224b96defad19)   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x0, 0x2) |
| #define | [USART1\_CS\_PA3](#a2b840a1cb7d57509620f6735d100721d)   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x0, 0x3) |
| #define | [USART1\_CS\_PA4](#a8a60ef6d1e4b99f5723a3ad13be87e27)   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x0, 0x4) |
| #define | [USART1\_CS\_PA5](#a8a5c35f83c96ddf3b7a77780e2f1c1c4)   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x0, 0x5) |
| #define | [USART1\_CS\_PA6](#ad09f63306f81c19e089740e73b7c5ca3)   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x0, 0x6) |
| #define | [USART1\_CS\_PA7](#a5e4bcedb6aa6f737c59d7fbc90600914)   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x0, 0x7) |
| #define | [USART1\_CS\_PA8](#ae498c676478180f9d03ef7658fec450d)   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x0, 0x8) |
| #define | [USART1\_CS\_PB0](#a85135b8ccf3ebf77ddc568d9b52f5094)   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x1, 0x0) |
| #define | [USART1\_CS\_PB1](#a0246376c47db0d08b13f7a025626ca87)   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x1, 0x1) |
| #define | [USART1\_CS\_PB2](#ad05621a528ebb076ef80b755fb78d978)   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x1, 0x2) |
| #define | [USART1\_CS\_PB3](#abc8173b944f7432db3a97c73d92b6552)   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x1, 0x3) |
| #define | [USART1\_CS\_PB4](#aa7ae45108c0a2f3774a280bbe7a99d6e)   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x1, 0x4) |
| #define | [USART1\_RTS\_PA0](#adb1892bd6bbe15436ebe8d87009a07cb)   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x0, 0x0) |
| #define | [USART1\_RTS\_PA1](#a26b0c827b5f3dbad42fe4c88182feb9e)   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x0, 0x1) |
| #define | [USART1\_RTS\_PA2](#a17f90a324b77e892691df314e360e963)   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x0, 0x2) |
| #define | [USART1\_RTS\_PA3](#abf5b408be99508e62dfbcb898a80e7ac)   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x0, 0x3) |
| #define | [USART1\_RTS\_PA4](#a8e25d0018b9d8dae670d9d9300b83af7)   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x0, 0x4) |
| #define | [USART1\_RTS\_PA5](#a84e98aafd9109ac79850651a5d146916)   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x0, 0x5) |
| #define | [USART1\_RTS\_PA6](#aa03434ec66cb7eff576fa185022785e1)   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x0, 0x6) |
| #define | [USART1\_RTS\_PA7](#aa269f7d4e3f5ed2277613925f5121a7f)   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x0, 0x7) |
| #define | [USART1\_RTS\_PA8](#a7dcd395c60fd8731801305a296152c87)   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x0, 0x8) |
| #define | [USART1\_RTS\_PB0](#a52fd2e9de7f7818ab1b46df1c8d90c97)   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x1, 0x0) |
| #define | [USART1\_RTS\_PB1](#a04f167919a0613138e75321f67966c53)   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x1, 0x1) |
| #define | [USART1\_RTS\_PB2](#a6312b639f209d510aeb2cf3c69c9dd78)   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x1, 0x2) |
| #define | [USART1\_RTS\_PB3](#a1dd8e150d7b8942bf6d5720a94055d86)   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x1, 0x3) |
| #define | [USART1\_RTS\_PB4](#a43bfaa41fb4d5764c7c20472dc78b910)   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x1, 0x4) |
| #define | [USART1\_RX\_PA0](#a1344d4b7bc318d0fd2a49f01b2505dae)   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x0, 0x0) |
| #define | [USART1\_RX\_PA1](#a584f5b976fccf459dd41984b87d98681)   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x0, 0x1) |
| #define | [USART1\_RX\_PA2](#a3c33c7b93cf4d0e5f732eabd7dea291a)   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x0, 0x2) |
| #define | [USART1\_RX\_PA3](#aa099336238b9ee2f60131f8874965ad8)   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x0, 0x3) |
| #define | [USART1\_RX\_PA4](#a483eec1a4dd0267e961a224ec9ed8b84)   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x0, 0x4) |
| #define | [USART1\_RX\_PA5](#a286c64ca6230b6b77cb08c33aea08aed)   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x0, 0x5) |
| #define | [USART1\_RX\_PA6](#a82275dfce6dca7f5d0839ff935d07ccc)   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x0, 0x6) |
| #define | [USART1\_RX\_PA7](#a96d092df3d1cc14f341e286ea317b472)   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x0, 0x7) |
| #define | [USART1\_RX\_PA8](#aac6af6b6b32a8dcaa559198f05b5a47f)   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x0, 0x8) |
| #define | [USART1\_RX\_PB0](#aa098eecd8faf98926c9d2bb8967f1ae2)   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x1, 0x0) |
| #define | [USART1\_RX\_PB1](#a83da59b1fad652e6b37d8c78ba863e4a)   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x1, 0x1) |
| #define | [USART1\_RX\_PB2](#aba4860939dbd4ff3183262cb930b72ae)   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x1, 0x2) |
| #define | [USART1\_RX\_PB3](#ad4a239cdd1dee0f2d639d89f2e44cbde)   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x1, 0x3) |
| #define | [USART1\_RX\_PB4](#af0288216e877a710b3362b633cef07ba)   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x1, 0x4) |
| #define | [USART1\_CLK\_PA0](#a6273503644f26d0e7fdea92bfad483b5)   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x0, 0x0) |
| #define | [USART1\_CLK\_PA1](#acdf47d0f1e701024dae47f456f7f33cb)   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x0, 0x1) |
| #define | [USART1\_CLK\_PA2](#ab2e8d3b4244d357f94872db24ed16927)   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x0, 0x2) |
| #define | [USART1\_CLK\_PA3](#ac2b16123044b93c6284fc09ea7307aea)   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x0, 0x3) |
| #define | [USART1\_CLK\_PA4](#aef6a2ecc146aa23576b096a14fff6a71)   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x0, 0x4) |
| #define | [USART1\_CLK\_PA5](#a348b6d13cd6c1fd972844f246208c418)   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x0, 0x5) |
| #define | [USART1\_CLK\_PA6](#a02f5bf254e9e3e1d975dcf0e94dee3ff)   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x0, 0x6) |
| #define | [USART1\_CLK\_PA7](#af16d9576f0ce2a75c7e04acf90154df0)   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x0, 0x7) |
| #define | [USART1\_CLK\_PA8](#a4ae6ad259d7439b48be122c006cd7a70)   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x0, 0x8) |
| #define | [USART1\_CLK\_PB0](#a5f3a85cc7c7b38a151737d28fee5ee7c)   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x1, 0x0) |
| #define | [USART1\_CLK\_PB1](#a4f5d16e2e67f49adee3bc194bd64cdb5)   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x1, 0x1) |
| #define | [USART1\_CLK\_PB2](#ac5eafbf67c4fbf68d2004d3832b36fd2)   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x1, 0x2) |
| #define | [USART1\_CLK\_PB3](#a8c5f904b0d4bd158af4538491d6a9cae)   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x1, 0x3) |
| #define | [USART1\_CLK\_PB4](#a1ee4fd4b12c1e3a4493e393457f663d0)   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x1, 0x4) |
| #define | [USART1\_TX\_PA0](#a719e46bd04807b305447b999b4782375)   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x0, 0x0) |
| #define | [USART1\_TX\_PA1](#a42b48b97f3273ff42eece98916e60630)   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x0, 0x1) |
| #define | [USART1\_TX\_PA2](#a90383d542c7aad9b15775b11bd264910)   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x0, 0x2) |
| #define | [USART1\_TX\_PA3](#a83db4685e72e840bc03e199379a7091c)   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x0, 0x3) |
| #define | [USART1\_TX\_PA4](#aaa9c6660b9d802d891bafd1e46c6f636)   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x0, 0x4) |
| #define | [USART1\_TX\_PA5](#aa07e04d88a4a9cc4548400bd132fc983)   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x0, 0x5) |
| #define | [USART1\_TX\_PA6](#a62b940162d89200c43e0bfdfcebdc328)   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x0, 0x6) |
| #define | [USART1\_TX\_PA7](#a3a73fda10b8231c5b68b71d701b5c22d)   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x0, 0x7) |
| #define | [USART1\_TX\_PA8](#a85db663b9e4dd87fa5f42d086fe271d3)   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x0, 0x8) |
| #define | [USART1\_TX\_PB0](#a64045a6952ae9268787f7e74035dabd2)   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x1, 0x0) |
| #define | [USART1\_TX\_PB1](#ac26399945006e5b812ed776b3bde9c94)   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x1, 0x1) |
| #define | [USART1\_TX\_PB2](#ab053a8b1f357c93e16e05246129fb287)   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x1, 0x2) |
| #define | [USART1\_TX\_PB3](#a22d9a25dccc08c9857907ee64205dd49)   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x1, 0x3) |
| #define | [USART1\_TX\_PB4](#ad2c1c4e313eb032924141290fe7d7b6b)   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x1, 0x4) |
| #define | [USART1\_CTS\_PA0](#ab8f436c89c7f71271cd70e896f6cd7eb)   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x0, 0x0) |
| #define | [USART1\_CTS\_PA1](#a0894716787e9a09d997f744f07d31723)   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x0, 0x1) |
| #define | [USART1\_CTS\_PA2](#a2722c60724d7b70b208eb7813533542d)   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x0, 0x2) |
| #define | [USART1\_CTS\_PA3](#a37178b8015441a63a2d5f0f4e29a5997)   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x0, 0x3) |
| #define | [USART1\_CTS\_PA4](#a398faa6da0bb297d1c52ee25a0e4fa3b)   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x0, 0x4) |
| #define | [USART1\_CTS\_PA5](#ab7480c291b286bf76cd6af604392e8df)   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x0, 0x5) |
| #define | [USART1\_CTS\_PA6](#a0df6cd090c6f551b231e0c299be9aff7)   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x0, 0x6) |
| #define | [USART1\_CTS\_PA7](#af6d968f5f19e43661b67d957feb325f4)   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x0, 0x7) |
| #define | [USART1\_CTS\_PA8](#af8dbd4a98eafc9d13abefe6297358fb1)   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x0, 0x8) |
| #define | [USART1\_CTS\_PB0](#af8129b9ac85e75bf06ff65fc2bdcdbc1)   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x1, 0x0) |
| #define | [USART1\_CTS\_PB1](#a6835005577ea5a786174c5e3e27c0dff)   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x1, 0x1) |
| #define | [USART1\_CTS\_PB2](#af4533814f41de47f0cac542ca9de9aab)   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x1, 0x2) |
| #define | [USART1\_CTS\_PB3](#afc9159697ecb98cd36fb72b426c00b41)   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x1, 0x3) |
| #define | [USART1\_CTS\_PB4](#a3ff692acebbeed736a4799348753c60d)   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x1, 0x4) |
| #define | [ABUS\_AEVEN0\_IADC0](#ad10d010cbdef8a32f14837ade41debfc)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x0, 0x1) |
| #define | [ABUS\_AEVEN0\_ACMP0](#a62a9951e869147c72fbe9c1e77e874fa)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x0, 0x2) |
| #define | [ABUS\_AEVEN1\_IADC0](#a2a1cae8649645c367738b43ded59f749)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x1, 0x1) |
| #define | [ABUS\_AEVEN1\_ACMP0](#a8fde714bdb414359ff3619c3cb4dcad6)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x1, 0x2) |
| #define | [ABUS\_AODD0\_IADC0](#a566e8d018410bda1e988452fb5304441)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x2, 0x1) |
| #define | [ABUS\_AODD0\_ACMP0](#a23efcbf1afd4c5f08b8a01816879787b)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x2, 0x2) |
| #define | [ABUS\_AODD1\_IADC0](#aaa4617b296badc53ea3d2e297283c808)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x3, 0x1) |
| #define | [ABUS\_AODD1\_ACMP0](#abd2169342442333b350e32f881eff995)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x3, 0x2) |
| #define | [ABUS\_BEVEN0\_IADC0](#a2c5cafb1e8cc088300cbe61d33611daa)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x0, 0x1) |
| #define | [ABUS\_BEVEN0\_ACMP0](#a331630c1c48db7a35089f3a799eda1cb)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x0, 0x2) |
| #define | [ABUS\_BEVEN1\_IADC0](#a88d851648e8e5ed855ad2fa6c973284e)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x1, 0x1) |
| #define | [ABUS\_BEVEN1\_ACMP0](#aa920748827ffa55e353d0c1d3b6dd56a)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x1, 0x2) |
| #define | [ABUS\_BODD0\_IADC0](#a8c77789600eea5e975b7d2b24c89f864)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x2, 0x1) |
| #define | [ABUS\_BODD0\_ACMP0](#a11259cd5a424085be1d843f934c82a15)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x2, 0x2) |
| #define | [ABUS\_BODD1\_IADC0](#aa5b85245f2fa86535920bd7d2ea837d1)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x3, 0x1) |
| #define | [ABUS\_BODD1\_ACMP0](#a4db6c1d2216c35ce68a76ff799d50138)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x3, 0x2) |
| #define | [ABUS\_CDEVEN0\_IADC0](#af5928f28259fae0be44a365ba0a82cfe)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x0, 0x1) |
| #define | [ABUS\_CDEVEN0\_ACMP0](#a31e97c0380604db9ca894fb9805eb181)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x0, 0x2) |
| #define | [ABUS\_CDEVEN1\_IADC0](#a7a2fc86a1027011d729324239a1858d4)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x1, 0x1) |
| #define | [ABUS\_CDEVEN1\_ACMP0](#a9c0f4b146a86a1031b59d7ab608c0374)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x1, 0x2) |
| #define | [ABUS\_CDODD0\_IADC0](#a233653a6dffa4feece57164e50df6fc1)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x2, 0x1) |
| #define | [ABUS\_CDODD0\_ACMP0](#a79225667aa65dff641c32173f97dd8bc)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x2, 0x2) |
| #define | [ABUS\_CDODD1\_IADC0](#a4fc002977cffebe3a4d840f009d2afa2)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x3, 0x1) |
| #define | [ABUS\_CDODD1\_ACMP0](#aaac7b83053516a362770c72f813fd8ad)   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x3, 0x2) |

## Macro Definition Documentation

## [◆ ](#a62a9951e869147c72fbe9c1e77e874fa)ABUS\_AEVEN0\_ACMP0

| #define ABUS\_AEVEN0\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x0, 0x2) |
| --- |

## [◆ ](#ad10d010cbdef8a32f14837ade41debfc)ABUS\_AEVEN0\_IADC0

| #define ABUS\_AEVEN0\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x0, 0x1) |
| --- |

## [◆ ](#a8fde714bdb414359ff3619c3cb4dcad6)ABUS\_AEVEN1\_ACMP0

| #define ABUS\_AEVEN1\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x1, 0x2) |
| --- |

## [◆ ](#a2a1cae8649645c367738b43ded59f749)ABUS\_AEVEN1\_IADC0

| #define ABUS\_AEVEN1\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x1, 0x1) |
| --- |

## [◆ ](#a23efcbf1afd4c5f08b8a01816879787b)ABUS\_AODD0\_ACMP0

| #define ABUS\_AODD0\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x2, 0x2) |
| --- |

## [◆ ](#a566e8d018410bda1e988452fb5304441)ABUS\_AODD0\_IADC0

| #define ABUS\_AODD0\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x2, 0x1) |
| --- |

## [◆ ](#abd2169342442333b350e32f881eff995)ABUS\_AODD1\_ACMP0

| #define ABUS\_AODD1\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x3, 0x2) |
| --- |

## [◆ ](#aaa4617b296badc53ea3d2e297283c808)ABUS\_AODD1\_IADC0

| #define ABUS\_AODD1\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x0, 0x3, 0x1) |
| --- |

## [◆ ](#a331630c1c48db7a35089f3a799eda1cb)ABUS\_BEVEN0\_ACMP0

| #define ABUS\_BEVEN0\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x0, 0x2) |
| --- |

## [◆ ](#a2c5cafb1e8cc088300cbe61d33611daa)ABUS\_BEVEN0\_IADC0

| #define ABUS\_BEVEN0\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x0, 0x1) |
| --- |

## [◆ ](#aa920748827ffa55e353d0c1d3b6dd56a)ABUS\_BEVEN1\_ACMP0

| #define ABUS\_BEVEN1\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x1, 0x2) |
| --- |

## [◆ ](#a88d851648e8e5ed855ad2fa6c973284e)ABUS\_BEVEN1\_IADC0

| #define ABUS\_BEVEN1\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x1, 0x1) |
| --- |

## [◆ ](#a11259cd5a424085be1d843f934c82a15)ABUS\_BODD0\_ACMP0

| #define ABUS\_BODD0\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x2, 0x2) |
| --- |

## [◆ ](#a8c77789600eea5e975b7d2b24c89f864)ABUS\_BODD0\_IADC0

| #define ABUS\_BODD0\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x2, 0x1) |
| --- |

## [◆ ](#a4db6c1d2216c35ce68a76ff799d50138)ABUS\_BODD1\_ACMP0

| #define ABUS\_BODD1\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x3, 0x2) |
| --- |

## [◆ ](#aa5b85245f2fa86535920bd7d2ea837d1)ABUS\_BODD1\_IADC0

| #define ABUS\_BODD1\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x1, 0x3, 0x1) |
| --- |

## [◆ ](#a31e97c0380604db9ca894fb9805eb181)ABUS\_CDEVEN0\_ACMP0

| #define ABUS\_CDEVEN0\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x0, 0x2) |
| --- |

## [◆ ](#af5928f28259fae0be44a365ba0a82cfe)ABUS\_CDEVEN0\_IADC0

| #define ABUS\_CDEVEN0\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x0, 0x1) |
| --- |

## [◆ ](#a9c0f4b146a86a1031b59d7ab608c0374)ABUS\_CDEVEN1\_ACMP0

| #define ABUS\_CDEVEN1\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x1, 0x2) |
| --- |

## [◆ ](#a7a2fc86a1027011d729324239a1858d4)ABUS\_CDEVEN1\_IADC0

| #define ABUS\_CDEVEN1\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x1, 0x1) |
| --- |

## [◆ ](#a79225667aa65dff641c32173f97dd8bc)ABUS\_CDODD0\_ACMP0

| #define ABUS\_CDODD0\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x2, 0x2) |
| --- |

## [◆ ](#a233653a6dffa4feece57164e50df6fc1)ABUS\_CDODD0\_IADC0

| #define ABUS\_CDODD0\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x2, 0x1) |
| --- |

## [◆ ](#aaac7b83053516a362770c72f813fd8ad)ABUS\_CDODD1\_ACMP0

| #define ABUS\_CDODD1\_ACMP0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x3, 0x2) |
| --- |

## [◆ ](#a4fc002977cffebe3a4d840f009d2afa2)ABUS\_CDODD1\_IADC0

| #define ABUS\_CDODD1\_IADC0   [SILABS\_ABUS](silabs-pinctrl-dbus_8h.md#ac9851f435704e7b096478bca454faf6c)(0x2, 0x3, 0x1) |
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

## [◆ ](#aed8fa49f3eb9671881b3991c01105ff6)EUSART0\_CS\_PC0

| #define EUSART0\_CS\_PC0   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x2, 0x0) |
| --- |

## [◆ ](#accad121c30ac5b90f161ada15a181a0e)EUSART0\_CS\_PC1

| #define EUSART0\_CS\_PC1   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x2, 0x1) |
| --- |

## [◆ ](#a038e1a231493a32b4dc8e1017045d4de)EUSART0\_CS\_PC2

| #define EUSART0\_CS\_PC2   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x2, 0x2) |
| --- |

## [◆ ](#ab55727982406dae06bfc6d4817311e84)EUSART0\_CS\_PC3

| #define EUSART0\_CS\_PC3   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x2, 0x3) |
| --- |

## [◆ ](#a9e313135bb2478404e9075aaa2e97365)EUSART0\_CS\_PC4

| #define EUSART0\_CS\_PC4   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x2, 0x4) |
| --- |

## [◆ ](#ac9b7036e8e6aa9e910a6f9ff4ead91a8)EUSART0\_CS\_PC5

| #define EUSART0\_CS\_PC5   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x2, 0x5) |
| --- |

## [◆ ](#a09261a943a59ec343e4c473518d9af71)EUSART0\_CS\_PC6

| #define EUSART0\_CS\_PC6   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x2, 0x6) |
| --- |

## [◆ ](#ac9b0f742fed5deed319e3ced35da509f)EUSART0\_CS\_PC7

| #define EUSART0\_CS\_PC7   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x2, 0x7) |
| --- |

## [◆ ](#a50f458970cc99a933780e51f340bbbfc)EUSART0\_CS\_PD0

| #define EUSART0\_CS\_PD0   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x3, 0x0) |
| --- |

## [◆ ](#a614ddd72337ca49b570b01d97e02a5ab)EUSART0\_CS\_PD1

| #define EUSART0\_CS\_PD1   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x3, 0x1) |
| --- |

## [◆ ](#afca145acee686cb673080d165608869c)EUSART0\_CS\_PD2

| #define EUSART0\_CS\_PD2   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x3, 0x2) |
| --- |

## [◆ ](#a0fec9ee2f5eb601f7ecd07f427fe12d9)EUSART0\_CS\_PD3

| #define EUSART0\_CS\_PD3   [SILABS\_DBUS\_EUSART0\_CS](#ab4cc7cd42d85332e7b423dae99d2b50e)(0x3, 0x3) |
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

## [◆ ](#a12f93c05aa8eee84560122e11433dff9)EUSART0\_CTS\_PC0

| #define EUSART0\_CTS\_PC0   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x2, 0x0) |
| --- |

## [◆ ](#aa96ca5ef6f6b4221e0e8cdaacc2c0419)EUSART0\_CTS\_PC1

| #define EUSART0\_CTS\_PC1   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x2, 0x1) |
| --- |

## [◆ ](#ab65aef137530bff24284785786a11413)EUSART0\_CTS\_PC2

| #define EUSART0\_CTS\_PC2   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x2, 0x2) |
| --- |

## [◆ ](#a0a8251ba020c3db8eefff12e4b1ee723)EUSART0\_CTS\_PC3

| #define EUSART0\_CTS\_PC3   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x2, 0x3) |
| --- |

## [◆ ](#aa99f745ad1eee19ed42ea9c6f18d8b1f)EUSART0\_CTS\_PC4

| #define EUSART0\_CTS\_PC4   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x2, 0x4) |
| --- |

## [◆ ](#ab63fbab0b6b7f355a44ff32d7adae7e8)EUSART0\_CTS\_PC5

| #define EUSART0\_CTS\_PC5   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x2, 0x5) |
| --- |

## [◆ ](#a641ac3b8b404f53c7303bac894ab0d7e)EUSART0\_CTS\_PC6

| #define EUSART0\_CTS\_PC6   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x2, 0x6) |
| --- |

## [◆ ](#aeecf8c0a1903f81003f57a099ab5ec68)EUSART0\_CTS\_PC7

| #define EUSART0\_CTS\_PC7   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x2, 0x7) |
| --- |

## [◆ ](#a4c8975cd656f4a945f94d313c1ed0631)EUSART0\_CTS\_PD0

| #define EUSART0\_CTS\_PD0   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x3, 0x0) |
| --- |

## [◆ ](#a24e996e1a6a4f04276ac94d2218921bd)EUSART0\_CTS\_PD1

| #define EUSART0\_CTS\_PD1   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x3, 0x1) |
| --- |

## [◆ ](#af00a1053965630bc5be8aff8a7663b81)EUSART0\_CTS\_PD2

| #define EUSART0\_CTS\_PD2   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x3, 0x2) |
| --- |

## [◆ ](#ab94c51b8230e3b650af4433bf444ff5b)EUSART0\_CTS\_PD3

| #define EUSART0\_CTS\_PD3   [SILABS\_DBUS\_EUSART0\_CTS](#ae1a52ec67ff061f1550ee177f83a0ea7)(0x3, 0x3) |
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

## [◆ ](#a825eb0a0ddbb7153c0c0a358164e17cc)EUSART0\_RTS\_PC0

| #define EUSART0\_RTS\_PC0   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x2, 0x0) |
| --- |

## [◆ ](#a342ddc29fafafaa7cabf46579b9f2135)EUSART0\_RTS\_PC1

| #define EUSART0\_RTS\_PC1   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x2, 0x1) |
| --- |

## [◆ ](#a9de85c0cea5ad13eb9542be9f9c1fecd)EUSART0\_RTS\_PC2

| #define EUSART0\_RTS\_PC2   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x2, 0x2) |
| --- |

## [◆ ](#aba46cf1f481e82d8c36b2e3924d56299)EUSART0\_RTS\_PC3

| #define EUSART0\_RTS\_PC3   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x2, 0x3) |
| --- |

## [◆ ](#a94bf3eeaf8970ef628c827f6d5ad6deb)EUSART0\_RTS\_PC4

| #define EUSART0\_RTS\_PC4   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x2, 0x4) |
| --- |

## [◆ ](#a1a43b2077d6da1cabc7179ef9d21138c)EUSART0\_RTS\_PC5

| #define EUSART0\_RTS\_PC5   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x2, 0x5) |
| --- |

## [◆ ](#a7b8ffd905edd49f61c10820c23f90ca6)EUSART0\_RTS\_PC6

| #define EUSART0\_RTS\_PC6   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x2, 0x6) |
| --- |

## [◆ ](#ae46d3ff4e405d9e8d63ffefb26f7d8f8)EUSART0\_RTS\_PC7

| #define EUSART0\_RTS\_PC7   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x2, 0x7) |
| --- |

## [◆ ](#a88c2dfec826dfb5ad0be6b63132e345d)EUSART0\_RTS\_PD0

| #define EUSART0\_RTS\_PD0   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x3, 0x0) |
| --- |

## [◆ ](#a4774365c9a89e81f776bcb83f62f26d0)EUSART0\_RTS\_PD1

| #define EUSART0\_RTS\_PD1   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x3, 0x1) |
| --- |

## [◆ ](#a3943f055fa037d9020a3251972e3ccef)EUSART0\_RTS\_PD2

| #define EUSART0\_RTS\_PD2   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x3, 0x2) |
| --- |

## [◆ ](#ad9cd7fd50ce835c6384623b4cfd04c9f)EUSART0\_RTS\_PD3

| #define EUSART0\_RTS\_PD3   [SILABS\_DBUS\_EUSART0\_RTS](#a9641ae53cb0f49b6bad7814adf078508)(0x3, 0x3) |
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

## [◆ ](#ab43573513fde6a68d9914f6cc422664c)EUSART0\_RX\_PC0

| #define EUSART0\_RX\_PC0   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x2, 0x0) |
| --- |

## [◆ ](#a397196ba429fc31426bb06135aad607d)EUSART0\_RX\_PC1

| #define EUSART0\_RX\_PC1   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x2, 0x1) |
| --- |

## [◆ ](#a3958b897fce5b24aec711db28532c9b1)EUSART0\_RX\_PC2

| #define EUSART0\_RX\_PC2   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x2, 0x2) |
| --- |

## [◆ ](#afd71895c0bb4699536f8b27207024444)EUSART0\_RX\_PC3

| #define EUSART0\_RX\_PC3   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x2, 0x3) |
| --- |

## [◆ ](#a17a0b3453db06718a90764d1c98b3673)EUSART0\_RX\_PC4

| #define EUSART0\_RX\_PC4   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x2, 0x4) |
| --- |

## [◆ ](#a0eba541db8e29efc4a9349d1d5fece98)EUSART0\_RX\_PC5

| #define EUSART0\_RX\_PC5   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x2, 0x5) |
| --- |

## [◆ ](#ad14eee491ec56c41c6066a646152d19b)EUSART0\_RX\_PC6

| #define EUSART0\_RX\_PC6   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x2, 0x6) |
| --- |

## [◆ ](#aa7040c8e3d027dc7def3b3a07306f9c8)EUSART0\_RX\_PC7

| #define EUSART0\_RX\_PC7   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x2, 0x7) |
| --- |

## [◆ ](#a26f2a17606c1f10ad647e9d7be27f5fb)EUSART0\_RX\_PD0

| #define EUSART0\_RX\_PD0   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x3, 0x0) |
| --- |

## [◆ ](#ad83e83b257b520defe2d667b70bb301b)EUSART0\_RX\_PD1

| #define EUSART0\_RX\_PD1   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x3, 0x1) |
| --- |

## [◆ ](#a8da013cc702e3895b2eedc65fde8b4b0)EUSART0\_RX\_PD2

| #define EUSART0\_RX\_PD2   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x3, 0x2) |
| --- |

## [◆ ](#ab5ec704003949c54b6f683e33d998f1a)EUSART0\_RX\_PD3

| #define EUSART0\_RX\_PD3   [SILABS\_DBUS\_EUSART0\_RX](#afc8334b04cee683c97518ae5a1ae34d4)(0x3, 0x3) |
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

## [◆ ](#a1078589030256c2dcfc07a08bbb87c4d)EUSART0\_SCLK\_PC0

| #define EUSART0\_SCLK\_PC0   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x2, 0x0) |
| --- |

## [◆ ](#a5edbc59cef4a7d2e1410f02049149426)EUSART0\_SCLK\_PC1

| #define EUSART0\_SCLK\_PC1   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x2, 0x1) |
| --- |

## [◆ ](#a452d7f6b0e64db7dfc5cc08b0c8d3d1b)EUSART0\_SCLK\_PC2

| #define EUSART0\_SCLK\_PC2   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x2, 0x2) |
| --- |

## [◆ ](#a3d47bd24e5f3d57dad33b7de29db889e)EUSART0\_SCLK\_PC3

| #define EUSART0\_SCLK\_PC3   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x2, 0x3) |
| --- |

## [◆ ](#a5c22d3590c171aae25635e62b43d1ad5)EUSART0\_SCLK\_PC4

| #define EUSART0\_SCLK\_PC4   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x2, 0x4) |
| --- |

## [◆ ](#a50f069238ddce48a050dadd16dc2e08d)EUSART0\_SCLK\_PC5

| #define EUSART0\_SCLK\_PC5   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x2, 0x5) |
| --- |

## [◆ ](#aeb6ec6c0706bdb69cc25f8bd54818b2a)EUSART0\_SCLK\_PC6

| #define EUSART0\_SCLK\_PC6   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x2, 0x6) |
| --- |

## [◆ ](#ab3c184119f4bfa1ccf5669955fa3747d)EUSART0\_SCLK\_PC7

| #define EUSART0\_SCLK\_PC7   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x2, 0x7) |
| --- |

## [◆ ](#ae02e824020415b9917f19a443a032894)EUSART0\_SCLK\_PD0

| #define EUSART0\_SCLK\_PD0   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x3, 0x0) |
| --- |

## [◆ ](#a98983e81af06d6c1b2f7f00d951dfd4e)EUSART0\_SCLK\_PD1

| #define EUSART0\_SCLK\_PD1   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x3, 0x1) |
| --- |

## [◆ ](#ad01090a81a9e2e2f7fc0aab98b981651)EUSART0\_SCLK\_PD2

| #define EUSART0\_SCLK\_PD2   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x3, 0x2) |
| --- |

## [◆ ](#a4d0cdc0b2724c2d8bb9d5df172827617)EUSART0\_SCLK\_PD3

| #define EUSART0\_SCLK\_PD3   [SILABS\_DBUS\_EUSART0\_SCLK](#a8a3d16b25db63819d80b010beb7d47ef)(0x3, 0x3) |
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

## [◆ ](#af63c951ca47dcda1de1deadf0916395a)EUSART0\_TX\_PC0

| #define EUSART0\_TX\_PC0   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x2, 0x0) |
| --- |

## [◆ ](#a1f1dd917913a93cea9c4f4a30e188289)EUSART0\_TX\_PC1

| #define EUSART0\_TX\_PC1   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x2, 0x1) |
| --- |

## [◆ ](#a2b10800da7ec93c986d863e4a316aa9b)EUSART0\_TX\_PC2

| #define EUSART0\_TX\_PC2   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x2, 0x2) |
| --- |

## [◆ ](#a3520e59def513d6fffa9f38f207570b6)EUSART0\_TX\_PC3

| #define EUSART0\_TX\_PC3   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x2, 0x3) |
| --- |

## [◆ ](#a49af2dadf031ad5deccf82a39c9f4e9c)EUSART0\_TX\_PC4

| #define EUSART0\_TX\_PC4   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x2, 0x4) |
| --- |

## [◆ ](#ae2f02d0b2116fa3be868195f7f7f8a55)EUSART0\_TX\_PC5

| #define EUSART0\_TX\_PC5   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x2, 0x5) |
| --- |

## [◆ ](#ad18f194c3eb96f83768617c98fe16069)EUSART0\_TX\_PC6

| #define EUSART0\_TX\_PC6   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x2, 0x6) |
| --- |

## [◆ ](#aaa9ef38e04a4756ee56412e21933046d)EUSART0\_TX\_PC7

| #define EUSART0\_TX\_PC7   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x2, 0x7) |
| --- |

## [◆ ](#ad274833f35683527ee3e9ad95ad1409b)EUSART0\_TX\_PD0

| #define EUSART0\_TX\_PD0   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x3, 0x0) |
| --- |

## [◆ ](#af0b2b96f98ec0b156ed55e3a0df7bf49)EUSART0\_TX\_PD1

| #define EUSART0\_TX\_PD1   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x3, 0x1) |
| --- |

## [◆ ](#a1ff0c2f5cf0037337bc748f19f8c2755)EUSART0\_TX\_PD2

| #define EUSART0\_TX\_PD2   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x3, 0x2) |
| --- |

## [◆ ](#a651410e3284f3a14c116fc89304ab848)EUSART0\_TX\_PD3

| #define EUSART0\_TX\_PD3   [SILABS\_DBUS\_EUSART0\_TX](#a931fcc8e3c2da7642467f93f7fff0e71)(0x3, 0x3) |
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

## [◆ ](#a17da237abad4fa377fe34a56e22f7994)PDM\_CLK\_PA0

| #define PDM\_CLK\_PA0   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x0, 0x0) |
| --- |

## [◆ ](#a30ebd03a19f9811c314f8e1845f50ad9)PDM\_CLK\_PA1

| #define PDM\_CLK\_PA1   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x0, 0x1) |
| --- |

## [◆ ](#ae6adaa8523f3173e32239c4e9b9b2fd1)PDM\_CLK\_PA2

| #define PDM\_CLK\_PA2   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x0, 0x2) |
| --- |

## [◆ ](#acac34f27db1a3d2ec31df358674fa131)PDM\_CLK\_PA3

| #define PDM\_CLK\_PA3   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x0, 0x3) |
| --- |

## [◆ ](#ad37a0874cbe049c72632c6f2179d1cdd)PDM\_CLK\_PA4

| #define PDM\_CLK\_PA4   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x0, 0x4) |
| --- |

## [◆ ](#ae0e222d832684fced0532a4327496c25)PDM\_CLK\_PA5

| #define PDM\_CLK\_PA5   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x0, 0x5) |
| --- |

## [◆ ](#a065d9974c4f5a53dfa8f5f1671df9fc6)PDM\_CLK\_PA6

| #define PDM\_CLK\_PA6   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x0, 0x6) |
| --- |

## [◆ ](#ac5f913eea970639ecfcda0de352dcc43)PDM\_CLK\_PA7

| #define PDM\_CLK\_PA7   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x0, 0x7) |
| --- |

## [◆ ](#a73233d7b85b39f5acf81eb3bef623e73)PDM\_CLK\_PA8

| #define PDM\_CLK\_PA8   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x0, 0x8) |
| --- |

## [◆ ](#a16c0497c54578a79b86dc789c748fee2)PDM\_CLK\_PB0

| #define PDM\_CLK\_PB0   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x1, 0x0) |
| --- |

## [◆ ](#a14417c07902532890f54f8fe21b0956c)PDM\_CLK\_PB1

| #define PDM\_CLK\_PB1   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x1, 0x1) |
| --- |

## [◆ ](#ad925c34c175014c7c07358549323dbe4)PDM\_CLK\_PB2

| #define PDM\_CLK\_PB2   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x1, 0x2) |
| --- |

## [◆ ](#a0826c43ece683f511bc3dbf27fc01927)PDM\_CLK\_PB3

| #define PDM\_CLK\_PB3   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x1, 0x3) |
| --- |

## [◆ ](#a5c6d93cd903d7c780ecda20bcec72ac4)PDM\_CLK\_PB4

| #define PDM\_CLK\_PB4   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x1, 0x4) |
| --- |

## [◆ ](#a1750f23968b042aae8205a9e45334734)PDM\_CLK\_PC0

| #define PDM\_CLK\_PC0   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x2, 0x0) |
| --- |

## [◆ ](#a634829cbe2f8f494a5e4c3d747199a67)PDM\_CLK\_PC1

| #define PDM\_CLK\_PC1   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x2, 0x1) |
| --- |

## [◆ ](#a4a0059bd0b5be4ac96db3482f8407ebf)PDM\_CLK\_PC2

| #define PDM\_CLK\_PC2   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x2, 0x2) |
| --- |

## [◆ ](#a6bd1bc850a90979bb7c36e129c3d39a2)PDM\_CLK\_PC3

| #define PDM\_CLK\_PC3   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x2, 0x3) |
| --- |

## [◆ ](#afa3f9103181ab9b8b26495125e3991f5)PDM\_CLK\_PC4

| #define PDM\_CLK\_PC4   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x2, 0x4) |
| --- |

## [◆ ](#a383f7fe2d6f1385986dc08d1342bdbae)PDM\_CLK\_PC5

| #define PDM\_CLK\_PC5   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x2, 0x5) |
| --- |

## [◆ ](#a3864b096ca291ed4ce6e2e609384d297)PDM\_CLK\_PC6

| #define PDM\_CLK\_PC6   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x2, 0x6) |
| --- |

## [◆ ](#a45db6fe2c22dddb9c131b81a51a265e1)PDM\_CLK\_PC7

| #define PDM\_CLK\_PC7   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x2, 0x7) |
| --- |

## [◆ ](#ae0bd60a7a78c4eb57f276cf1f6f478be)PDM\_CLK\_PD0

| #define PDM\_CLK\_PD0   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x3, 0x0) |
| --- |

## [◆ ](#a3331b3b655dca5f27eda7b9a5edec57e)PDM\_CLK\_PD1

| #define PDM\_CLK\_PD1   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x3, 0x1) |
| --- |

## [◆ ](#a59e99a2875165982fb12ec8e71bea000)PDM\_CLK\_PD2

| #define PDM\_CLK\_PD2   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x3, 0x2) |
| --- |

## [◆ ](#a1c2cb950f01e7c29dbd16dc9b73ce497)PDM\_CLK\_PD3

| #define PDM\_CLK\_PD3   [SILABS\_DBUS\_PDM\_CLK](#a7c8d36abf53d7929d13eeff70abcabc2)(0x3, 0x3) |
| --- |

## [◆ ](#a8076cde51878a20f5391bc3c7844dab3)PDM\_DAT0\_PA0

| #define PDM\_DAT0\_PA0   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x0, 0x0) |
| --- |

## [◆ ](#ac7a9f1aca581e062a433809395238812)PDM\_DAT0\_PA1

| #define PDM\_DAT0\_PA1   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x0, 0x1) |
| --- |

## [◆ ](#a7e9a14ddb5e3c79831635d8ab4634fd1)PDM\_DAT0\_PA2

| #define PDM\_DAT0\_PA2   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x0, 0x2) |
| --- |

## [◆ ](#a361db81d9510397b97d471b85d293247)PDM\_DAT0\_PA3

| #define PDM\_DAT0\_PA3   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x0, 0x3) |
| --- |

## [◆ ](#ae8827de80cb0f00b7c0c28897a446672)PDM\_DAT0\_PA4

| #define PDM\_DAT0\_PA4   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x0, 0x4) |
| --- |

## [◆ ](#af1c2f379b0dd1b5b5c2f0dcc02e66a18)PDM\_DAT0\_PA5

| #define PDM\_DAT0\_PA5   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x0, 0x5) |
| --- |

## [◆ ](#adc98dacaec34e0bc7b5111cf4a5cae6a)PDM\_DAT0\_PA6

| #define PDM\_DAT0\_PA6   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x0, 0x6) |
| --- |

## [◆ ](#a10f7155fb07e6ee74db22f4982a3386e)PDM\_DAT0\_PA7

| #define PDM\_DAT0\_PA7   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x0, 0x7) |
| --- |

## [◆ ](#acefda5f922c7fd820079fbe3596a76f5)PDM\_DAT0\_PA8

| #define PDM\_DAT0\_PA8   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x0, 0x8) |
| --- |

## [◆ ](#a1aaf675c35776b909986481ed0e9cac0)PDM\_DAT0\_PB0

| #define PDM\_DAT0\_PB0   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x1, 0x0) |
| --- |

## [◆ ](#a2813b125ed458746140490ac24fd4326)PDM\_DAT0\_PB1

| #define PDM\_DAT0\_PB1   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x1, 0x1) |
| --- |

## [◆ ](#a6fa34019aa25bdfa705139c8f0d9d826)PDM\_DAT0\_PB2

| #define PDM\_DAT0\_PB2   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x1, 0x2) |
| --- |

## [◆ ](#aeb3b2a38f75a2db5f032ef21314a0ea0)PDM\_DAT0\_PB3

| #define PDM\_DAT0\_PB3   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x1, 0x3) |
| --- |

## [◆ ](#a8453dd053f8278aca863c3033a8b29d4)PDM\_DAT0\_PB4

| #define PDM\_DAT0\_PB4   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x1, 0x4) |
| --- |

## [◆ ](#ab9987b7a24c8195e35e0ca238817fe6b)PDM\_DAT0\_PC0

| #define PDM\_DAT0\_PC0   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x2, 0x0) |
| --- |

## [◆ ](#a1db5ed56336a70d82c2f88b11dc5ae3c)PDM\_DAT0\_PC1

| #define PDM\_DAT0\_PC1   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x2, 0x1) |
| --- |

## [◆ ](#a4ce1e6985c2e168c0d8f2ce76fd7b53a)PDM\_DAT0\_PC2

| #define PDM\_DAT0\_PC2   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x2, 0x2) |
| --- |

## [◆ ](#a5855f905cdc824df96bc5c41ea492242)PDM\_DAT0\_PC3

| #define PDM\_DAT0\_PC3   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x2, 0x3) |
| --- |

## [◆ ](#a12991c4bb5704770a3ec24d470a7de41)PDM\_DAT0\_PC4

| #define PDM\_DAT0\_PC4   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x2, 0x4) |
| --- |

## [◆ ](#a746f9df3b772fb53bed1c3745b902dc8)PDM\_DAT0\_PC5

| #define PDM\_DAT0\_PC5   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x2, 0x5) |
| --- |

## [◆ ](#a7a59060917dac0ed6a379c29d5ccd355)PDM\_DAT0\_PC6

| #define PDM\_DAT0\_PC6   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x2, 0x6) |
| --- |

## [◆ ](#a5348f9e1d87746a8a98cb87b4df64937)PDM\_DAT0\_PC7

| #define PDM\_DAT0\_PC7   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x2, 0x7) |
| --- |

## [◆ ](#acf90e3c92b6cb54e783c14578df6dea0)PDM\_DAT0\_PD0

| #define PDM\_DAT0\_PD0   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x3, 0x0) |
| --- |

## [◆ ](#a62b3aa330ecbeb720ea654edb6b70c4d)PDM\_DAT0\_PD1

| #define PDM\_DAT0\_PD1   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x3, 0x1) |
| --- |

## [◆ ](#aeaee63c71a856370c07ad40f1f9c099e)PDM\_DAT0\_PD2

| #define PDM\_DAT0\_PD2   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x3, 0x2) |
| --- |

## [◆ ](#a888efdeb39811dd330592978fcec4f63)PDM\_DAT0\_PD3

| #define PDM\_DAT0\_PD3   [SILABS\_DBUS\_PDM\_DAT0](#a921644a66709fd45814c7bfbe42deee3)(0x3, 0x3) |
| --- |

## [◆ ](#a2e9b856688c2d8eadb9283adb15d07ec)PDM\_DAT1\_PA0

| #define PDM\_DAT1\_PA0   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x0, 0x0) |
| --- |

## [◆ ](#ac33beea0c269de70b662a58cfd10c25e)PDM\_DAT1\_PA1

| #define PDM\_DAT1\_PA1   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x0, 0x1) |
| --- |

## [◆ ](#a336bbd623362b37e192eea1ec8da1315)PDM\_DAT1\_PA2

| #define PDM\_DAT1\_PA2   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x0, 0x2) |
| --- |

## [◆ ](#a712778b19527024cca05630251103095)PDM\_DAT1\_PA3

| #define PDM\_DAT1\_PA3   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x0, 0x3) |
| --- |

## [◆ ](#ad59e6a2f0c431fdfa8a2aad9d0ee12ca)PDM\_DAT1\_PA4

| #define PDM\_DAT1\_PA4   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x0, 0x4) |
| --- |

## [◆ ](#aa880de680c84604c10a15c80fc592aa3)PDM\_DAT1\_PA5

| #define PDM\_DAT1\_PA5   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x0, 0x5) |
| --- |

## [◆ ](#a999ce72cee2c3c5bdab055dba6008cf9)PDM\_DAT1\_PA6

| #define PDM\_DAT1\_PA6   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x0, 0x6) |
| --- |

## [◆ ](#a3a7ba5e8b55bf168b9250d0e1a7c992b)PDM\_DAT1\_PA7

| #define PDM\_DAT1\_PA7   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x0, 0x7) |
| --- |

## [◆ ](#aad4d4f8b8548163442aa489af3f3ccd8)PDM\_DAT1\_PA8

| #define PDM\_DAT1\_PA8   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x0, 0x8) |
| --- |

## [◆ ](#a79b1395b0600a359ccf7168741e159a7)PDM\_DAT1\_PB0

| #define PDM\_DAT1\_PB0   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x1, 0x0) |
| --- |

## [◆ ](#a4f3fe9e22ab662d160fd385583c32980)PDM\_DAT1\_PB1

| #define PDM\_DAT1\_PB1   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x1, 0x1) |
| --- |

## [◆ ](#a20aac187e72e0d127453b2201ec38aab)PDM\_DAT1\_PB2

| #define PDM\_DAT1\_PB2   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x1, 0x2) |
| --- |

## [◆ ](#a245af246ec5bb7545b44e46291a5407f)PDM\_DAT1\_PB3

| #define PDM\_DAT1\_PB3   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x1, 0x3) |
| --- |

## [◆ ](#ad55ee30074e511e8e38fcbf298f4b573)PDM\_DAT1\_PB4

| #define PDM\_DAT1\_PB4   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x1, 0x4) |
| --- |

## [◆ ](#a766b87b6f397b34821ee6c3da39313ae)PDM\_DAT1\_PC0

| #define PDM\_DAT1\_PC0   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x2, 0x0) |
| --- |

## [◆ ](#ab8beb7afd902e3726167ba905dfc4920)PDM\_DAT1\_PC1

| #define PDM\_DAT1\_PC1   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x2, 0x1) |
| --- |

## [◆ ](#a03dd4fdb93626d4849bedc2e14a69e5a)PDM\_DAT1\_PC2

| #define PDM\_DAT1\_PC2   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x2, 0x2) |
| --- |

## [◆ ](#a0d42cfb3c8a3f7ffc56f61ffee0339c3)PDM\_DAT1\_PC3

| #define PDM\_DAT1\_PC3   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x2, 0x3) |
| --- |

## [◆ ](#af1131ca951092591193e95b4b6740b43)PDM\_DAT1\_PC4

| #define PDM\_DAT1\_PC4   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x2, 0x4) |
| --- |

## [◆ ](#aadeb4540d495a19ecb989ac61fedeb6e)PDM\_DAT1\_PC5

| #define PDM\_DAT1\_PC5   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x2, 0x5) |
| --- |

## [◆ ](#acbeec6663ffc7b4c265ae1fac2e6b585)PDM\_DAT1\_PC6

| #define PDM\_DAT1\_PC6   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x2, 0x6) |
| --- |

## [◆ ](#a653a61290ca92e497c920de5c9baab3d)PDM\_DAT1\_PC7

| #define PDM\_DAT1\_PC7   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x2, 0x7) |
| --- |

## [◆ ](#aa64a2b39a12d19f074cf30fd37746640)PDM\_DAT1\_PD0

| #define PDM\_DAT1\_PD0   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x3, 0x0) |
| --- |

## [◆ ](#a419241477ba85a002471be3bfc6a0b5c)PDM\_DAT1\_PD1

| #define PDM\_DAT1\_PD1   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x3, 0x1) |
| --- |

## [◆ ](#afa2865841cb633083f38aa4492bcf107)PDM\_DAT1\_PD2

| #define PDM\_DAT1\_PD2   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x3, 0x2) |
| --- |

## [◆ ](#aaef465d544e19e6a5fea47a23cfa75c5)PDM\_DAT1\_PD3

| #define PDM\_DAT1\_PD3   [SILABS\_DBUS\_PDM\_DAT1](#ad3003a9d19f7b887685a497e7faf1068)(0x3, 0x3) |
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

## [◆ ](#a1f03fc6bcf9a20f2f39b4d91cf302d63)SILABS\_DBUS\_ACMP0\_ACMPOUT

| #define SILABS\_DBUS\_ACMP0\_ACMPOUT | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 4, 1, 0, 1)

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)

#define SILABS\_DBUS(port, pin, periph\_base, en\_present, en\_bit, route)

**Definition** silabs-pinctrl-dbus.h:47

## [◆ ](#a19d73eca7da5c8b8622b3cb155ab4e6c)SILABS\_DBUS\_CMU\_CLKIN0

| #define SILABS\_DBUS\_CMU\_CLKIN0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 7, 0, 0, 1)

## [◆ ](#a6d193d353f76cad0e7da5c584625e996)SILABS\_DBUS\_CMU\_CLKOUT0

| #define SILABS\_DBUS\_CMU\_CLKOUT0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 7, 1, 0, 2)

## [◆ ](#a3f7ded37227446a05137a47c9a466894)SILABS\_DBUS\_CMU\_CLKOUT1

| #define SILABS\_DBUS\_CMU\_CLKOUT1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 7, 1, 1, 3)

## [◆ ](#a67d6fb886df9d589e447bd9332252d62)SILABS\_DBUS\_CMU\_CLKOUT2

| #define SILABS\_DBUS\_CMU\_CLKOUT2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 7, 1, 2, 4)

## [◆ ](#ab4cc7cd42d85332e7b423dae99d2b50e)SILABS\_DBUS\_EUSART0\_CS

| #define SILABS\_DBUS\_EUSART0\_CS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 19, 1, 0, 1)

## [◆ ](#ae1a52ec67ff061f1550ee177f83a0ea7)SILABS\_DBUS\_EUSART0\_CTS

| #define SILABS\_DBUS\_EUSART0\_CTS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 19, 0, 0, 2)

## [◆ ](#a9641ae53cb0f49b6bad7814adf078508)SILABS\_DBUS\_EUSART0\_RTS

| #define SILABS\_DBUS\_EUSART0\_RTS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 19, 1, 1, 3)

## [◆ ](#afc8334b04cee683c97518ae5a1ae34d4)SILABS\_DBUS\_EUSART0\_RX

| #define SILABS\_DBUS\_EUSART0\_RX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 19, 1, 2, 4)

## [◆ ](#a8a3d16b25db63819d80b010beb7d47ef)SILABS\_DBUS\_EUSART0\_SCLK

| #define SILABS\_DBUS\_EUSART0\_SCLK | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 19, 1, 3, 5)

## [◆ ](#a931fcc8e3c2da7642467f93f7fff0e71)SILABS\_DBUS\_EUSART0\_TX

| #define SILABS\_DBUS\_EUSART0\_TX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 19, 1, 4, 6)

## [◆ ](#ac3e145872ad81776dafad7dd8145f9b1)SILABS\_DBUS\_EUSART1\_CS

| #define SILABS\_DBUS\_EUSART1\_CS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 27, 1, 0, 1)

## [◆ ](#ad059fbad09ad887f644c51fc1963f4df)SILABS\_DBUS\_EUSART1\_CTS

| #define SILABS\_DBUS\_EUSART1\_CTS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 27, 0, 0, 2)

## [◆ ](#a3d9d1df82dd7e8a060d36353bbb00f18)SILABS\_DBUS\_EUSART1\_RTS

| #define SILABS\_DBUS\_EUSART1\_RTS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 27, 1, 1, 3)

## [◆ ](#af1675cdac7ef1fbf39f79665746a74c9)SILABS\_DBUS\_EUSART1\_RX

| #define SILABS\_DBUS\_EUSART1\_RX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 27, 1, 2, 4)

## [◆ ](#a8f10a814a0b2af37cc01f4b93780c12f)SILABS\_DBUS\_EUSART1\_SCLK

| #define SILABS\_DBUS\_EUSART1\_SCLK | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 27, 1, 3, 5)

## [◆ ](#adb612d2f22dc57f485e22fe674efb442)SILABS\_DBUS\_EUSART1\_TX

| #define SILABS\_DBUS\_EUSART1\_TX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 27, 1, 4, 6)

## [◆ ](#a652b5412868f09aff727d2a84ce5efd6)SILABS\_DBUS\_I2C0\_SCL

| #define SILABS\_DBUS\_I2C0\_SCL | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 40, 1, 0, 1)

## [◆ ](#a5c3eac01e4153cd7adfdd4d8c50f2fa9)SILABS\_DBUS\_I2C0\_SDA

| #define SILABS\_DBUS\_I2C0\_SDA | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 40, 1, 1, 2)

## [◆ ](#aa55669252ab4d30ff2044a7ac5e8fad1)SILABS\_DBUS\_I2C1\_SCL

| #define SILABS\_DBUS\_I2C1\_SCL | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 44, 1, 0, 1)

## [◆ ](#a0c32c2f4351441d0a97a445627912904)SILABS\_DBUS\_I2C1\_SDA

| #define SILABS\_DBUS\_I2C1\_SDA | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 44, 1, 1, 2)

## [◆ ](#ab81ce78522519bd5a5e257c8f4f2c27f)SILABS\_DBUS\_LETIMER0\_OUT0

| #define SILABS\_DBUS\_LETIMER0\_OUT0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 48, 1, 0, 1)

## [◆ ](#a2effaa50da9b899d91eb127cdf554098)SILABS\_DBUS\_LETIMER0\_OUT1

| #define SILABS\_DBUS\_LETIMER0\_OUT1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 48, 1, 1, 2)

## [◆ ](#a0225f18d061c851599210b56aeb42231)SILABS\_DBUS\_MODEM\_ANT0

| #define SILABS\_DBUS\_MODEM\_ANT0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 52, 1, 0, 1)

## [◆ ](#aaff7073911479298cda7729646f6990e)SILABS\_DBUS\_MODEM\_ANT1

| #define SILABS\_DBUS\_MODEM\_ANT1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 52, 1, 1, 2)

## [◆ ](#ac618ed85f554e3e852ad256d20ad95d5)SILABS\_DBUS\_MODEM\_ANTROLLOVER

| #define SILABS\_DBUS\_MODEM\_ANTROLLOVER | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 52, 1, 2, 3)

## [◆ ](#a076fd7a7e8083517d750f0ef332faefe)SILABS\_DBUS\_MODEM\_ANTRR0

| #define SILABS\_DBUS\_MODEM\_ANTRR0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 52, 1, 3, 4)

## [◆ ](#a4415eef2a0f03f68eeec9f39cfa00772)SILABS\_DBUS\_MODEM\_ANTRR1

| #define SILABS\_DBUS\_MODEM\_ANTRR1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 52, 1, 4, 5)

## [◆ ](#a1913f830f7d6a4234ffb12e0701b0019)SILABS\_DBUS\_MODEM\_ANTRR2

| #define SILABS\_DBUS\_MODEM\_ANTRR2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 52, 1, 5, 6)

## [◆ ](#ab9c8e475b9d5d1a9dae206aaa9b639b1)SILABS\_DBUS\_MODEM\_ANTRR3

| #define SILABS\_DBUS\_MODEM\_ANTRR3 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 52, 1, 6, 7)

## [◆ ](#a8da1060fdb49bad378f130183b73dd13)SILABS\_DBUS\_MODEM\_ANTRR4

| #define SILABS\_DBUS\_MODEM\_ANTRR4 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 52, 1, 7, 8)

## [◆ ](#aab2d172c20010568167c80096a97da23)SILABS\_DBUS\_MODEM\_ANTRR5

| #define SILABS\_DBUS\_MODEM\_ANTRR5 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 52, 1, 8, 9)

## [◆ ](#a7af41447a0035cf8fb73804c40eb3502)SILABS\_DBUS\_MODEM\_ANTSWEN

| #define SILABS\_DBUS\_MODEM\_ANTSWEN | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 52, 1, 9, 10)

## [◆ ](#ab828720727a5b918ca11b9ff3a119b44)SILABS\_DBUS\_MODEM\_ANTSWUS

| #define SILABS\_DBUS\_MODEM\_ANTSWUS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 52, 1, 10, 11)

## [◆ ](#a548bcbbd7ee4b87c6611d4fdb348984e)SILABS\_DBUS\_MODEM\_ANTTRIG

| #define SILABS\_DBUS\_MODEM\_ANTTRIG | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 52, 1, 11, 12)

## [◆ ](#a07822fe9a1f6febeaf3745361b47d57b)SILABS\_DBUS\_MODEM\_ANTTRIGSTOP

| #define SILABS\_DBUS\_MODEM\_ANTTRIGSTOP | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 52, 1, 12, 13)

## [◆ ](#a7d3926059c8b0c608d6d2bce035555b6)SILABS\_DBUS\_MODEM\_DCLK

| #define SILABS\_DBUS\_MODEM\_DCLK | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 52, 1, 13, 14)

## [◆ ](#a82dfdd0e9ad82ab0c75f4a530620d34b)SILABS\_DBUS\_MODEM\_DIN

| #define SILABS\_DBUS\_MODEM\_DIN | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 52, 0, 0, 15)

## [◆ ](#a48c49cff2ed723238703ff1b75ba8ae7)SILABS\_DBUS\_MODEM\_DOUT

| #define SILABS\_DBUS\_MODEM\_DOUT | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 52, 1, 14, 16)

## [◆ ](#a7c8d36abf53d7929d13eeff70abcabc2)SILABS\_DBUS\_PDM\_CLK

| #define SILABS\_DBUS\_PDM\_CLK | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 70, 1, 0, 1)

## [◆ ](#a921644a66709fd45814c7bfbe42deee3)SILABS\_DBUS\_PDM\_DAT0

| #define SILABS\_DBUS\_PDM\_DAT0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 70, 0, 0, 2)

## [◆ ](#ad3003a9d19f7b887685a497e7faf1068)SILABS\_DBUS\_PDM\_DAT1

| #define SILABS\_DBUS\_PDM\_DAT1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 70, 0, 0, 3)

## [◆ ](#a55a10636beb81ba5bf195c83c45cc994)SILABS\_DBUS\_PRS0\_ASYNCH0

| #define SILABS\_DBUS\_PRS0\_ASYNCH0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 75, 1, 0, 1)

## [◆ ](#a8502ee8adb62210f0c02abdf38a54019)SILABS\_DBUS\_PRS0\_ASYNCH1

| #define SILABS\_DBUS\_PRS0\_ASYNCH1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 75, 1, 1, 2)

## [◆ ](#a48a4d109c810311436ee8add40794aba)SILABS\_DBUS\_PRS0\_ASYNCH10

| #define SILABS\_DBUS\_PRS0\_ASYNCH10 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 75, 1, 10, 11)

## [◆ ](#a7acd670bc40ebc057369a7c577a0b0c2)SILABS\_DBUS\_PRS0\_ASYNCH11

| #define SILABS\_DBUS\_PRS0\_ASYNCH11 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 75, 1, 11, 12)

## [◆ ](#a8065a08661b02239f79db443c11afac8)SILABS\_DBUS\_PRS0\_ASYNCH2

| #define SILABS\_DBUS\_PRS0\_ASYNCH2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 75, 1, 2, 3)

## [◆ ](#a39cb285c6310012108f37d510db7a86c)SILABS\_DBUS\_PRS0\_ASYNCH3

| #define SILABS\_DBUS\_PRS0\_ASYNCH3 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 75, 1, 3, 4)

## [◆ ](#ac419288481edbfee2df8711b0c037ba2)SILABS\_DBUS\_PRS0\_ASYNCH4

| #define SILABS\_DBUS\_PRS0\_ASYNCH4 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 75, 1, 4, 5)

## [◆ ](#a6d7577bd45bc2c6043463ef6df86e8a7)SILABS\_DBUS\_PRS0\_ASYNCH5

| #define SILABS\_DBUS\_PRS0\_ASYNCH5 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 75, 1, 5, 6)

## [◆ ](#afa3017107df002534d41165b790891dd)SILABS\_DBUS\_PRS0\_ASYNCH6

| #define SILABS\_DBUS\_PRS0\_ASYNCH6 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 75, 1, 6, 7)

## [◆ ](#ae5af1968989cc643d315e310eb840dcc)SILABS\_DBUS\_PRS0\_ASYNCH7

| #define SILABS\_DBUS\_PRS0\_ASYNCH7 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 75, 1, 7, 8)

## [◆ ](#a0d062ef8d1ababa72b60d08265ff7e25)SILABS\_DBUS\_PRS0\_ASYNCH8

| #define SILABS\_DBUS\_PRS0\_ASYNCH8 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 75, 1, 8, 9)

## [◆ ](#af0617799b4044665a4996276fcf1e2bf)SILABS\_DBUS\_PRS0\_ASYNCH9

| #define SILABS\_DBUS\_PRS0\_ASYNCH9 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 75, 1, 9, 10)

## [◆ ](#a1b8e171cd761535148063c9b81ed3ee0)SILABS\_DBUS\_PRS0\_SYNCH0

| #define SILABS\_DBUS\_PRS0\_SYNCH0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 75, 1, 12, 13)

## [◆ ](#a85d7bbcc208a977d14aa286a9576b432)SILABS\_DBUS\_PRS0\_SYNCH1

| #define SILABS\_DBUS\_PRS0\_SYNCH1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 75, 1, 13, 14)

## [◆ ](#a7340c07baee2cad6d5b685929c48151b)SILABS\_DBUS\_PRS0\_SYNCH2

| #define SILABS\_DBUS\_PRS0\_SYNCH2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 75, 1, 14, 15)

## [◆ ](#a131fc4f34da4d410665642dfd51b733b)SILABS\_DBUS\_PRS0\_SYNCH3

| #define SILABS\_DBUS\_PRS0\_SYNCH3 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 75, 1, 15, 16)

## [◆ ](#a3165d7b2623b12308b38c9abcf900642)SILABS\_DBUS\_PTI\_DCLK

| #define SILABS\_DBUS\_PTI\_DCLK | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 35, 1, 0, 1)

## [◆ ](#a12a23ec2045680c0521b20f50d421881)SILABS\_DBUS\_PTI\_DFRAME

| #define SILABS\_DBUS\_PTI\_DFRAME | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 35, 1, 1, 2)

## [◆ ](#ae418c8c258cc10d03e4d36b741827f82)SILABS\_DBUS\_PTI\_DOUT

| #define SILABS\_DBUS\_PTI\_DOUT | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 35, 1, 2, 3)

## [◆ ](#ad1f44a36026d8dd0f50d48e95fc9e5b3)SILABS\_DBUS\_TIMER0\_CC0

| #define SILABS\_DBUS\_TIMER0\_CC0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 93, 1, 0, 1)

## [◆ ](#a1eb30c3f4f87f98b3da18bc2a602e7e6)SILABS\_DBUS\_TIMER0\_CC1

| #define SILABS\_DBUS\_TIMER0\_CC1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 93, 1, 1, 2)

## [◆ ](#a23896bac158177558e7f179e8f3382a6)SILABS\_DBUS\_TIMER0\_CC2

| #define SILABS\_DBUS\_TIMER0\_CC2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 93, 1, 2, 3)

## [◆ ](#a44f0ed489cab3a50241d605931d579b0)SILABS\_DBUS\_TIMER0\_CDTI0

| #define SILABS\_DBUS\_TIMER0\_CDTI0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 93, 1, 3, 4)

## [◆ ](#ae13240899cbf48ec4f6710bcabc4ded8)SILABS\_DBUS\_TIMER0\_CDTI1

| #define SILABS\_DBUS\_TIMER0\_CDTI1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 93, 1, 4, 5)

## [◆ ](#a38b6cbc6d13fa4030cb07f1e2fc59003)SILABS\_DBUS\_TIMER0\_CDTI2

| #define SILABS\_DBUS\_TIMER0\_CDTI2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 93, 1, 5, 6)

## [◆ ](#a67fb3b7635c0b3408ee6bdea0b861bd3)SILABS\_DBUS\_TIMER1\_CC0

| #define SILABS\_DBUS\_TIMER1\_CC0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 101, 1, 0, 1)

## [◆ ](#a2aa7458fe116434331629b24cf0e45f0)SILABS\_DBUS\_TIMER1\_CC1

| #define SILABS\_DBUS\_TIMER1\_CC1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 101, 1, 1, 2)

## [◆ ](#a237c2bb8f6da0300cb10b73fab4c7ec4)SILABS\_DBUS\_TIMER1\_CC2

| #define SILABS\_DBUS\_TIMER1\_CC2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 101, 1, 2, 3)

## [◆ ](#afd03aef40bfd2fcfec51db90b50a4ebf)SILABS\_DBUS\_TIMER1\_CDTI0

| #define SILABS\_DBUS\_TIMER1\_CDTI0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 101, 1, 3, 4)

## [◆ ](#aff14e83dc5f27682d1d76ddb75d8b08c)SILABS\_DBUS\_TIMER1\_CDTI1

| #define SILABS\_DBUS\_TIMER1\_CDTI1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 101, 1, 4, 5)

## [◆ ](#a33328da36cd2df624ded688165f9f319)SILABS\_DBUS\_TIMER1\_CDTI2

| #define SILABS\_DBUS\_TIMER1\_CDTI2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 101, 1, 5, 6)

## [◆ ](#a6f8eec2f0d2289a845062b5fe14a59b7)SILABS\_DBUS\_TIMER2\_CC0

| #define SILABS\_DBUS\_TIMER2\_CC0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 109, 1, 0, 1)

## [◆ ](#a1a5af09f79ed3f743efa31ec03d87cc6)SILABS\_DBUS\_TIMER2\_CC1

| #define SILABS\_DBUS\_TIMER2\_CC1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 109, 1, 1, 2)

## [◆ ](#a1d6da86f7d7e4099e9bb47e38d3c4e9c)SILABS\_DBUS\_TIMER2\_CC2

| #define SILABS\_DBUS\_TIMER2\_CC2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 109, 1, 2, 3)

## [◆ ](#a648ec3c8dafb7f88dba23ea50dba4e8b)SILABS\_DBUS\_TIMER2\_CDTI0

| #define SILABS\_DBUS\_TIMER2\_CDTI0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 109, 1, 3, 4)

## [◆ ](#ab124eb8882de0913d017f81a32eae6d8)SILABS\_DBUS\_TIMER2\_CDTI1

| #define SILABS\_DBUS\_TIMER2\_CDTI1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 109, 1, 4, 5)

## [◆ ](#aac5b26da22ac4ef8f1f08354f8339130)SILABS\_DBUS\_TIMER2\_CDTI2

| #define SILABS\_DBUS\_TIMER2\_CDTI2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 109, 1, 5, 6)

## [◆ ](#adb617def54a24017bdcaafe228697dd5)SILABS\_DBUS\_TIMER3\_CC0

| #define SILABS\_DBUS\_TIMER3\_CC0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 117, 1, 0, 1)

## [◆ ](#ac522d8a27bbe4fcfba1e0cc282dee7c0)SILABS\_DBUS\_TIMER3\_CC1

| #define SILABS\_DBUS\_TIMER3\_CC1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 117, 1, 1, 2)

## [◆ ](#a9a558be5b3c2f7ecb9bf66d83b8ee60c)SILABS\_DBUS\_TIMER3\_CC2

| #define SILABS\_DBUS\_TIMER3\_CC2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 117, 1, 2, 3)

## [◆ ](#abb9fc38bdcf044af8e89f8b5bd4eb339)SILABS\_DBUS\_TIMER3\_CDTI0

| #define SILABS\_DBUS\_TIMER3\_CDTI0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 117, 1, 3, 4)

## [◆ ](#a2c50f79deaf5192c644bb0b52832352d)SILABS\_DBUS\_TIMER3\_CDTI1

| #define SILABS\_DBUS\_TIMER3\_CDTI1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 117, 1, 4, 5)

## [◆ ](#a5f8e118916558ec753791e59baeefef0)SILABS\_DBUS\_TIMER3\_CDTI2

| #define SILABS\_DBUS\_TIMER3\_CDTI2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 117, 1, 5, 6)

## [◆ ](#ab5f1949dfc60e6afa576f77ac645a367)SILABS\_DBUS\_TIMER4\_CC0

| #define SILABS\_DBUS\_TIMER4\_CC0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 125, 1, 0, 1)

## [◆ ](#a9de72de2effcb9f9efdecf8925cbbf57)SILABS\_DBUS\_TIMER4\_CC1

| #define SILABS\_DBUS\_TIMER4\_CC1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 125, 1, 1, 2)

## [◆ ](#ae37d483d35f11fd70fa4cd48a7718ab9)SILABS\_DBUS\_TIMER4\_CC2

| #define SILABS\_DBUS\_TIMER4\_CC2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 125, 1, 2, 3)

## [◆ ](#a7a9532d9136447f798581c3f11f6608f)SILABS\_DBUS\_TIMER4\_CDTI0

| #define SILABS\_DBUS\_TIMER4\_CDTI0 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 125, 1, 3, 4)

## [◆ ](#aa3a6b5984b119e066af677767169f2f8)SILABS\_DBUS\_TIMER4\_CDTI1

| #define SILABS\_DBUS\_TIMER4\_CDTI1 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 125, 1, 4, 5)

## [◆ ](#ae21486ec9db5e77200e89be6227e33af)SILABS\_DBUS\_TIMER4\_CDTI2

| #define SILABS\_DBUS\_TIMER4\_CDTI2 | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 125, 1, 5, 6)

## [◆ ](#a14f60bd84a682fe99ccd93607ca87d6b)SILABS\_DBUS\_USART0\_CLK

| #define SILABS\_DBUS\_USART0\_CLK | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 133, 1, 3, 5)

## [◆ ](#acc127783c3de46fa1efd6bf86f632807)SILABS\_DBUS\_USART0\_CS

| #define SILABS\_DBUS\_USART0\_CS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 133, 1, 0, 1)

## [◆ ](#a0be14ba61b5fc707ef02e7ac6ba779cf)SILABS\_DBUS\_USART0\_CTS

| #define SILABS\_DBUS\_USART0\_CTS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 133, 0, 0, 2)

## [◆ ](#afb90351e31f6da6446c2fc3f5aaaf394)SILABS\_DBUS\_USART0\_RTS

| #define SILABS\_DBUS\_USART0\_RTS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 133, 1, 1, 3)

## [◆ ](#a8d9bee07c90a69ada0a392fbd15c9e44)SILABS\_DBUS\_USART0\_RX

| #define SILABS\_DBUS\_USART0\_RX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 133, 1, 2, 4)

## [◆ ](#aca2a3d6b7903947d127d8b6ea5d8c84a)SILABS\_DBUS\_USART0\_TX

| #define SILABS\_DBUS\_USART0\_TX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 133, 1, 4, 6)

## [◆ ](#a1a4d85614e1e5ee7915d8eb87f75bfff)SILABS\_DBUS\_USART1\_CLK

| #define SILABS\_DBUS\_USART1\_CLK | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 141, 1, 3, 5)

## [◆ ](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)SILABS\_DBUS\_USART1\_CS

| #define SILABS\_DBUS\_USART1\_CS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 141, 1, 0, 1)

## [◆ ](#a765b10a8cee3cdea20421ef5da5aeb9d)SILABS\_DBUS\_USART1\_CTS

| #define SILABS\_DBUS\_USART1\_CTS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 141, 0, 0, 2)

## [◆ ](#a6ccc43376c75561508f0af5fbff43bff)SILABS\_DBUS\_USART1\_RTS

| #define SILABS\_DBUS\_USART1\_RTS | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 141, 1, 1, 3)

## [◆ ](#a5ccc39d740aa3ccbda884891cb348200)SILABS\_DBUS\_USART1\_RX

| #define SILABS\_DBUS\_USART1\_RX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 141, 1, 2, 4)

## [◆ ](#a4e38656e72cb7b91821d4217015fb624)SILABS\_DBUS\_USART1\_TX

| #define SILABS\_DBUS\_USART1\_TX | ( |  | *port*, |
| --- | --- | --- | --- |
|  |  |  | *pin* ) |

**Value:**

[SILABS\_DBUS](silabs-pinctrl-dbus_8h.md#ad25567dd5ed53d2ffb37dc1d6cf3d898)(port, pin, 141, 1, 4, 6)

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

## [◆ ](#a6273503644f26d0e7fdea92bfad483b5)USART1\_CLK\_PA0

| #define USART1\_CLK\_PA0   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x0, 0x0) |
| --- |

## [◆ ](#acdf47d0f1e701024dae47f456f7f33cb)USART1\_CLK\_PA1

| #define USART1\_CLK\_PA1   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x0, 0x1) |
| --- |

## [◆ ](#ab2e8d3b4244d357f94872db24ed16927)USART1\_CLK\_PA2

| #define USART1\_CLK\_PA2   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x0, 0x2) |
| --- |

## [◆ ](#ac2b16123044b93c6284fc09ea7307aea)USART1\_CLK\_PA3

| #define USART1\_CLK\_PA3   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x0, 0x3) |
| --- |

## [◆ ](#aef6a2ecc146aa23576b096a14fff6a71)USART1\_CLK\_PA4

| #define USART1\_CLK\_PA4   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x0, 0x4) |
| --- |

## [◆ ](#a348b6d13cd6c1fd972844f246208c418)USART1\_CLK\_PA5

| #define USART1\_CLK\_PA5   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x0, 0x5) |
| --- |

## [◆ ](#a02f5bf254e9e3e1d975dcf0e94dee3ff)USART1\_CLK\_PA6

| #define USART1\_CLK\_PA6   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x0, 0x6) |
| --- |

## [◆ ](#af16d9576f0ce2a75c7e04acf90154df0)USART1\_CLK\_PA7

| #define USART1\_CLK\_PA7   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x0, 0x7) |
| --- |

## [◆ ](#a4ae6ad259d7439b48be122c006cd7a70)USART1\_CLK\_PA8

| #define USART1\_CLK\_PA8   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x0, 0x8) |
| --- |

## [◆ ](#a5f3a85cc7c7b38a151737d28fee5ee7c)USART1\_CLK\_PB0

| #define USART1\_CLK\_PB0   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x1, 0x0) |
| --- |

## [◆ ](#a4f5d16e2e67f49adee3bc194bd64cdb5)USART1\_CLK\_PB1

| #define USART1\_CLK\_PB1   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x1, 0x1) |
| --- |

## [◆ ](#ac5eafbf67c4fbf68d2004d3832b36fd2)USART1\_CLK\_PB2

| #define USART1\_CLK\_PB2   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x1, 0x2) |
| --- |

## [◆ ](#a8c5f904b0d4bd158af4538491d6a9cae)USART1\_CLK\_PB3

| #define USART1\_CLK\_PB3   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x1, 0x3) |
| --- |

## [◆ ](#a1ee4fd4b12c1e3a4493e393457f663d0)USART1\_CLK\_PB4

| #define USART1\_CLK\_PB4   [SILABS\_DBUS\_USART1\_CLK](#a1a4d85614e1e5ee7915d8eb87f75bfff)(0x1, 0x4) |
| --- |

## [◆ ](#ad3e622bf87194cc1b199a28fbf82c922)USART1\_CS\_PA0

| #define USART1\_CS\_PA0   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x0, 0x0) |
| --- |

## [◆ ](#ac44b9afd3f4aacf4b5d77a6ffed82c31)USART1\_CS\_PA1

| #define USART1\_CS\_PA1   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x0, 0x1) |
| --- |

## [◆ ](#ab2817f18abf86707ce4224b96defad19)USART1\_CS\_PA2

| #define USART1\_CS\_PA2   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x0, 0x2) |
| --- |

## [◆ ](#a2b840a1cb7d57509620f6735d100721d)USART1\_CS\_PA3

| #define USART1\_CS\_PA3   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x0, 0x3) |
| --- |

## [◆ ](#a8a60ef6d1e4b99f5723a3ad13be87e27)USART1\_CS\_PA4

| #define USART1\_CS\_PA4   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x0, 0x4) |
| --- |

## [◆ ](#a8a5c35f83c96ddf3b7a77780e2f1c1c4)USART1\_CS\_PA5

| #define USART1\_CS\_PA5   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x0, 0x5) |
| --- |

## [◆ ](#ad09f63306f81c19e089740e73b7c5ca3)USART1\_CS\_PA6

| #define USART1\_CS\_PA6   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x0, 0x6) |
| --- |

## [◆ ](#a5e4bcedb6aa6f737c59d7fbc90600914)USART1\_CS\_PA7

| #define USART1\_CS\_PA7   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x0, 0x7) |
| --- |

## [◆ ](#ae498c676478180f9d03ef7658fec450d)USART1\_CS\_PA8

| #define USART1\_CS\_PA8   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x0, 0x8) |
| --- |

## [◆ ](#a85135b8ccf3ebf77ddc568d9b52f5094)USART1\_CS\_PB0

| #define USART1\_CS\_PB0   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x1, 0x0) |
| --- |

## [◆ ](#a0246376c47db0d08b13f7a025626ca87)USART1\_CS\_PB1

| #define USART1\_CS\_PB1   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x1, 0x1) |
| --- |

## [◆ ](#ad05621a528ebb076ef80b755fb78d978)USART1\_CS\_PB2

| #define USART1\_CS\_PB2   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x1, 0x2) |
| --- |

## [◆ ](#abc8173b944f7432db3a97c73d92b6552)USART1\_CS\_PB3

| #define USART1\_CS\_PB3   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x1, 0x3) |
| --- |

## [◆ ](#aa7ae45108c0a2f3774a280bbe7a99d6e)USART1\_CS\_PB4

| #define USART1\_CS\_PB4   [SILABS\_DBUS\_USART1\_CS](#aa1ab7ac67b4f9b90c23a7d5ed85e7b7b)(0x1, 0x4) |
| --- |

## [◆ ](#ab8f436c89c7f71271cd70e896f6cd7eb)USART1\_CTS\_PA0

| #define USART1\_CTS\_PA0   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x0, 0x0) |
| --- |

## [◆ ](#a0894716787e9a09d997f744f07d31723)USART1\_CTS\_PA1

| #define USART1\_CTS\_PA1   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x0, 0x1) |
| --- |

## [◆ ](#a2722c60724d7b70b208eb7813533542d)USART1\_CTS\_PA2

| #define USART1\_CTS\_PA2   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x0, 0x2) |
| --- |

## [◆ ](#a37178b8015441a63a2d5f0f4e29a5997)USART1\_CTS\_PA3

| #define USART1\_CTS\_PA3   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x0, 0x3) |
| --- |

## [◆ ](#a398faa6da0bb297d1c52ee25a0e4fa3b)USART1\_CTS\_PA4

| #define USART1\_CTS\_PA4   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x0, 0x4) |
| --- |

## [◆ ](#ab7480c291b286bf76cd6af604392e8df)USART1\_CTS\_PA5

| #define USART1\_CTS\_PA5   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x0, 0x5) |
| --- |

## [◆ ](#a0df6cd090c6f551b231e0c299be9aff7)USART1\_CTS\_PA6

| #define USART1\_CTS\_PA6   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x0, 0x6) |
| --- |

## [◆ ](#af6d968f5f19e43661b67d957feb325f4)USART1\_CTS\_PA7

| #define USART1\_CTS\_PA7   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x0, 0x7) |
| --- |

## [◆ ](#af8dbd4a98eafc9d13abefe6297358fb1)USART1\_CTS\_PA8

| #define USART1\_CTS\_PA8   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x0, 0x8) |
| --- |

## [◆ ](#af8129b9ac85e75bf06ff65fc2bdcdbc1)USART1\_CTS\_PB0

| #define USART1\_CTS\_PB0   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x1, 0x0) |
| --- |

## [◆ ](#a6835005577ea5a786174c5e3e27c0dff)USART1\_CTS\_PB1

| #define USART1\_CTS\_PB1   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x1, 0x1) |
| --- |

## [◆ ](#af4533814f41de47f0cac542ca9de9aab)USART1\_CTS\_PB2

| #define USART1\_CTS\_PB2   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x1, 0x2) |
| --- |

## [◆ ](#afc9159697ecb98cd36fb72b426c00b41)USART1\_CTS\_PB3

| #define USART1\_CTS\_PB3   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x1, 0x3) |
| --- |

## [◆ ](#a3ff692acebbeed736a4799348753c60d)USART1\_CTS\_PB4

| #define USART1\_CTS\_PB4   [SILABS\_DBUS\_USART1\_CTS](#a765b10a8cee3cdea20421ef5da5aeb9d)(0x1, 0x4) |
| --- |

## [◆ ](#adb1892bd6bbe15436ebe8d87009a07cb)USART1\_RTS\_PA0

| #define USART1\_RTS\_PA0   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x0, 0x0) |
| --- |

## [◆ ](#a26b0c827b5f3dbad42fe4c88182feb9e)USART1\_RTS\_PA1

| #define USART1\_RTS\_PA1   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x0, 0x1) |
| --- |

## [◆ ](#a17f90a324b77e892691df314e360e963)USART1\_RTS\_PA2

| #define USART1\_RTS\_PA2   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x0, 0x2) |
| --- |

## [◆ ](#abf5b408be99508e62dfbcb898a80e7ac)USART1\_RTS\_PA3

| #define USART1\_RTS\_PA3   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x0, 0x3) |
| --- |

## [◆ ](#a8e25d0018b9d8dae670d9d9300b83af7)USART1\_RTS\_PA4

| #define USART1\_RTS\_PA4   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x0, 0x4) |
| --- |

## [◆ ](#a84e98aafd9109ac79850651a5d146916)USART1\_RTS\_PA5

| #define USART1\_RTS\_PA5   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x0, 0x5) |
| --- |

## [◆ ](#aa03434ec66cb7eff576fa185022785e1)USART1\_RTS\_PA6

| #define USART1\_RTS\_PA6   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x0, 0x6) |
| --- |

## [◆ ](#aa269f7d4e3f5ed2277613925f5121a7f)USART1\_RTS\_PA7

| #define USART1\_RTS\_PA7   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x0, 0x7) |
| --- |

## [◆ ](#a7dcd395c60fd8731801305a296152c87)USART1\_RTS\_PA8

| #define USART1\_RTS\_PA8   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x0, 0x8) |
| --- |

## [◆ ](#a52fd2e9de7f7818ab1b46df1c8d90c97)USART1\_RTS\_PB0

| #define USART1\_RTS\_PB0   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x1, 0x0) |
| --- |

## [◆ ](#a04f167919a0613138e75321f67966c53)USART1\_RTS\_PB1

| #define USART1\_RTS\_PB1   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x1, 0x1) |
| --- |

## [◆ ](#a6312b639f209d510aeb2cf3c69c9dd78)USART1\_RTS\_PB2

| #define USART1\_RTS\_PB2   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x1, 0x2) |
| --- |

## [◆ ](#a1dd8e150d7b8942bf6d5720a94055d86)USART1\_RTS\_PB3

| #define USART1\_RTS\_PB3   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x1, 0x3) |
| --- |

## [◆ ](#a43bfaa41fb4d5764c7c20472dc78b910)USART1\_RTS\_PB4

| #define USART1\_RTS\_PB4   [SILABS\_DBUS\_USART1\_RTS](#a6ccc43376c75561508f0af5fbff43bff)(0x1, 0x4) |
| --- |

## [◆ ](#a1344d4b7bc318d0fd2a49f01b2505dae)USART1\_RX\_PA0

| #define USART1\_RX\_PA0   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x0, 0x0) |
| --- |

## [◆ ](#a584f5b976fccf459dd41984b87d98681)USART1\_RX\_PA1

| #define USART1\_RX\_PA1   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x0, 0x1) |
| --- |

## [◆ ](#a3c33c7b93cf4d0e5f732eabd7dea291a)USART1\_RX\_PA2

| #define USART1\_RX\_PA2   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x0, 0x2) |
| --- |

## [◆ ](#aa099336238b9ee2f60131f8874965ad8)USART1\_RX\_PA3

| #define USART1\_RX\_PA3   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x0, 0x3) |
| --- |

## [◆ ](#a483eec1a4dd0267e961a224ec9ed8b84)USART1\_RX\_PA4

| #define USART1\_RX\_PA4   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x0, 0x4) |
| --- |

## [◆ ](#a286c64ca6230b6b77cb08c33aea08aed)USART1\_RX\_PA5

| #define USART1\_RX\_PA5   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x0, 0x5) |
| --- |

## [◆ ](#a82275dfce6dca7f5d0839ff935d07ccc)USART1\_RX\_PA6

| #define USART1\_RX\_PA6   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x0, 0x6) |
| --- |

## [◆ ](#a96d092df3d1cc14f341e286ea317b472)USART1\_RX\_PA7

| #define USART1\_RX\_PA7   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x0, 0x7) |
| --- |

## [◆ ](#aac6af6b6b32a8dcaa559198f05b5a47f)USART1\_RX\_PA8

| #define USART1\_RX\_PA8   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x0, 0x8) |
| --- |

## [◆ ](#aa098eecd8faf98926c9d2bb8967f1ae2)USART1\_RX\_PB0

| #define USART1\_RX\_PB0   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x1, 0x0) |
| --- |

## [◆ ](#a83da59b1fad652e6b37d8c78ba863e4a)USART1\_RX\_PB1

| #define USART1\_RX\_PB1   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x1, 0x1) |
| --- |

## [◆ ](#aba4860939dbd4ff3183262cb930b72ae)USART1\_RX\_PB2

| #define USART1\_RX\_PB2   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x1, 0x2) |
| --- |

## [◆ ](#ad4a239cdd1dee0f2d639d89f2e44cbde)USART1\_RX\_PB3

| #define USART1\_RX\_PB3   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x1, 0x3) |
| --- |

## [◆ ](#af0288216e877a710b3362b633cef07ba)USART1\_RX\_PB4

| #define USART1\_RX\_PB4   [SILABS\_DBUS\_USART1\_RX](#a5ccc39d740aa3ccbda884891cb348200)(0x1, 0x4) |
| --- |

## [◆ ](#a719e46bd04807b305447b999b4782375)USART1\_TX\_PA0

| #define USART1\_TX\_PA0   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x0, 0x0) |
| --- |

## [◆ ](#a42b48b97f3273ff42eece98916e60630)USART1\_TX\_PA1

| #define USART1\_TX\_PA1   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x0, 0x1) |
| --- |

## [◆ ](#a90383d542c7aad9b15775b11bd264910)USART1\_TX\_PA2

| #define USART1\_TX\_PA2   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x0, 0x2) |
| --- |

## [◆ ](#a83db4685e72e840bc03e199379a7091c)USART1\_TX\_PA3

| #define USART1\_TX\_PA3   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x0, 0x3) |
| --- |

## [◆ ](#aaa9c6660b9d802d891bafd1e46c6f636)USART1\_TX\_PA4

| #define USART1\_TX\_PA4   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x0, 0x4) |
| --- |

## [◆ ](#aa07e04d88a4a9cc4548400bd132fc983)USART1\_TX\_PA5

| #define USART1\_TX\_PA5   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x0, 0x5) |
| --- |

## [◆ ](#a62b940162d89200c43e0bfdfcebdc328)USART1\_TX\_PA6

| #define USART1\_TX\_PA6   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x0, 0x6) |
| --- |

## [◆ ](#a3a73fda10b8231c5b68b71d701b5c22d)USART1\_TX\_PA7

| #define USART1\_TX\_PA7   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x0, 0x7) |
| --- |

## [◆ ](#a85db663b9e4dd87fa5f42d086fe271d3)USART1\_TX\_PA8

| #define USART1\_TX\_PA8   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x0, 0x8) |
| --- |

## [◆ ](#a64045a6952ae9268787f7e74035dabd2)USART1\_TX\_PB0

| #define USART1\_TX\_PB0   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x1, 0x0) |
| --- |

## [◆ ](#ac26399945006e5b812ed776b3bde9c94)USART1\_TX\_PB1

| #define USART1\_TX\_PB1   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x1, 0x1) |
| --- |

## [◆ ](#ab053a8b1f357c93e16e05246129fb287)USART1\_TX\_PB2

| #define USART1\_TX\_PB2   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x1, 0x2) |
| --- |

## [◆ ](#a22d9a25dccc08c9857907ee64205dd49)USART1\_TX\_PB3

| #define USART1\_TX\_PB3   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x1, 0x3) |
| --- |

## [◆ ](#ad2c1c4e313eb032924141290fe7d7b6b)USART1\_TX\_PB4

| #define USART1\_TX\_PB4   [SILABS\_DBUS\_USART1\_TX](#a4e38656e72cb7b91821d4217015fb624)(0x1, 0x4) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [silabs](dir_fa47ec1716313d52a64832478c9daea4.md)
- [xg29-pinctrl.h](xg29-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
