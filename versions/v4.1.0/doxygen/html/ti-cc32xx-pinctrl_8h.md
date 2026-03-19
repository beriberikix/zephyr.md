---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ti-cc32xx-pinctrl_8h.html
original_path: doxygen/html/ti-cc32xx-pinctrl_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ti-cc32xx-pinctrl.h File Reference

[Go to the source code of this file.](ti-cc32xx-pinctrl_8h_source.md)

| Macros | |
| --- | --- |
| #define | [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(pin, mux) |
|  | Utility macro to build TI CC32XX pinmux property entry. |
| TI CC32XX pin configuration bit field positions and masks. | |
| #define | [TI\_CC32XX\_PIN\_MSK](#a40cc14e2a5969a01d7a764fb5bdb84a7)   0x3FU |
| #define | [TI\_CC32XX\_PIN\_POS](#aea6f7d34537febd574f9ea0db1fbf3f3)   16U |
| #define | [TI\_CC32XX\_MUX\_MSK](#a381590ba2880c42636058c248f7e0e2e)   0xFU |
| #define | [TI\_CC32XX\_MUX\_POS](#ac9e2e00ac00ddd1eaf84331d18806339)   0U |
| TI CC32XX pinctrl pin functions (reference: SWRU465). | |
| #define | [GPIO10\_P1](#a89f97aa766818f7482c3131b39fc57c6)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(1U, 0U) |
| #define | [I2C\_SCL\_P1](#abd05f625495d2ea978dd73f2163ac895)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(1U, 1U) |
| #define | [GT\_PWM06\_P1](#a1b2e5aea3aad1cf49a0c9ed9c1abd0ac)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(1U, 3U) |
| #define | [UART1\_TX\_P1](#a995c80839609dc2f99440020c4b376c4)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(1U, 7U) |
| #define | [SDCARD\_CLK\_P1](#a0348e53054efacbcc5f4b36f5983b483)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(1U, 6U) |
| #define | [GT\_CCP01\_P1](#a41832e073da75fce278ea3f3a10c7981)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(1U, 12U) |
| #define | [GPIO11\_P2](#a092456dadbe48fb30ca448f893ff182d)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(2U, 0U) |
| #define | [I2C\_SDA\_P2](#a38fbe2595b40a64618809999d9ff7e88)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(2U, 1U) |
| #define | [GT\_PWM07\_P2](#a158549be521c32cbadd7fd94a59bc945)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(2U, 3U) |
| #define | [PXCLK\_P2](#af0194d8218ffae6e4ca6afdc1b75184c)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(2U, 4U) |
| #define | [SDCARD\_CMD\_P2](#af4b6115dd55265aa56f4fd0e4519449d)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(2U, 6U) |
| #define | [UART1\_RX\_P2](#a6c343f9636e9d3b43d19b3d0fe9f00b1)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(2U, 7U) |
| #define | [GT\_CCP02\_P2](#a29f1d9fd07affc428b9ec13021951496)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(2U, 12U) |
| #define | [MCAFSX\_P2](#af81018b6a0cfba2b48bcdc9cf864d609)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(2U, 13U) |
| #define | [GPIO12\_P3](#aa7fe336032aa6ad0cc8377bef839c249)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(3U, 0U) |
| #define | [MCACLK\_P3](#a449900e101576c23577ae8731ff6d832)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(3U, 3U) |
| #define | [PVS\_P3](#a040fa03ccf78c01cf8353dfafaed4363)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(3U, 4U) |
| #define | [I2C\_SCL\_P3](#a7f43eaa1290d1c51ad8dd0eead54eac8)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(3U, 5U) |
| #define | [UART0\_TX\_P3](#a0a31d5b2068953d90f7e152cfdeec235)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(3U, 7U) |
| #define | [GT\_CCP03\_P3](#a11be8733f58686a917f33eebc3f83f9f)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(3U, 12U) |
| #define | [GPIO13\_P4](#aa63a6fa68392be5d91f17f1512bca933)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(4U, 0U) |
| #define | [I2C\_SDA\_P4](#a2ac054fb4527be70688dfbad814da263)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(4U, 5U) |
| #define | [PHS\_P4](#a784b4247574d785820e1960b77d243f8)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(4U, 4U) |
| #define | [UART0\_RX\_P4](#a8526e278e737f86b5416d2432e06a961)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(4U, 7U) |
| #define | [GT\_CCP04\_P4](#a469f19224eef6881cc1247eed19c94a9)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(4U, 12U) |
| #define | [GPIO14\_P5](#a9c9da9f7d6f9b370c7548f936fe70b65)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(5U, 0U) |
| #define | [I2C\_SCL\_P5](#a4894dca0ecb760732bf032d80a6d8a13)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(5U, 5U) |
| #define | [GSPI\_CLK\_P5](#a0835204b6761fdb5da07401588cb60a8)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(5U, 7U) |
| #define | [PDATA8\_P5](#a420084bc2bed97ccfa6cabbdcea111b8)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(5U, 4U) |
| #define | [GT\_CCP05\_P5](#a85dd880198761cbddb32b2d482247bfa)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(5U, 12U) |
| #define | [GPIO15\_P6](#a0b94b2938ede1a6d84b397b12399aa58)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(6U, 0U) |
| #define | [I2C\_SDA\_P6](#ac8ded51ba9587b17cf1c2565f635a8a2)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(6U, 5U) |
| #define | [GSPI\_MISO\_P6](#a2e33fd1fd267afccbef0ca274336708d)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(6U, 7U) |
| #define | [PDATA9\_P6](#a74f7003fe754549a7abd536ce7ca18e0)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(6U, 4U) |
| #define | [SDCARD\_DATA3\_P6](#a1f11274609e837c40dbfcf3f4bb2c65b)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(6U, 8U) |
| #define | [GT\_CCP06\_P6](#a912c145e14635c2fade2b206d71df0a3)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(6U, 13U) |
| #define | [GPIO16\_P7](#a48e7884a7dfad77efe683eea6e678e1b)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(7U, 0U) |
| #define | [GSPI\_MOSI\_P7](#a06cd1b5b0df08a309fc7d9d0eb176948)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(7U, 7U) |
| #define | [PDATA10\_P7](#a4ba12e404845b1777c7fc27673a358c6)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(7U, 4U) |
| #define | [UART1\_TX\_P7](#a3e9e600bebc357ff182f42317b4fbc5f)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(7U, 5U) |
| #define | [SDCARD\_CLK\_P7](#ad19d6a6d4e575fdedc182d95c426ef7a)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(7U, 8U) |
| #define | [GT\_CCP07\_P7](#a2688169c0aa3bfc4333550d77b03f301)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(7U, 13U) |
| #define | [GPIO17\_P8](#a499b75b5acdf56015bc34363e8770625)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(8U, 0U) |
| #define | [UART1\_RX\_P8](#a9f7daa4bf7f1e01439d84c58da7c7235)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(8U, 5U) |
| #define | [GSPI\_CS\_P8](#a4a2c3ec59d144e1e20147f3fac31c7cf)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(8U, 7U) |
| #define | [SDCARD\_CMD\_P8](#a23c36223a0811761121eb6992e733191)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(8U, 8U) |
| #define | [PDATA11\_P8](#aec9421895f489defea513f9451f19a59)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(8U, 4U) |
| #define | [GPIO22\_P15](#a7bccf18256e2c16eeb9c2712b4123bed)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(15U, 0U) |
| #define | [MCAFSX\_P15](#ae4a09b647c36db2a78d4d8a128d47ac5)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(15U, 7U) |
| #define | [GT\_CCP04\_P15](#a93a7b969c1094f0c7a4811218a6d6b05)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(15U, 5U) |
| #define | [GPIO23\_P16](#a6e86e11b2fa406cf3d0a0ec57d1e856f)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(16U, 0U) |
| #define | [TDI\_P16](#aa8b475c426b332c82e21567727bb482a)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(16U, 1U) |
| #define | [UART1\_TX\_P16](#af2bdaab6fc0f793aee2bc8821869aad6)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(16U, 2U) |
| #define | [I2C\_SCL\_P16](#a8267f2892d868a33b27c68ae6673f239)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(16U, 9U) |
| #define | [GPIO24\_P17](#a80df0d9d7b3c95e556dd6f82f4551f0b)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(17U, 0U) |
| #define | [TDO\_P17](#a16ea3f7a2cb062dcdab07e50b4f5c049)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(17U, 1U) |
| #define | [PWM0\_P17](#a6c881b3b5ceb937e8441bd0cd3b449e8)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(17U, 5U) |
| #define | [UART1\_RX\_P17](#a632c817fbe28a138a9916a4946ee9da5)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(17U, 2U) |
| #define | [I2C\_SDA\_P17](#a0b1353bc11a6e1a156c6dbe4e59f74d0)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(17U, 9U) |
| #define | [GT\_CCP06\_P17](#a3ba8bacb70f2bcadaa6dfd786a673bd7)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(17U, 4U) |
| #define | [MCAFSX\_P17](#a082b74a8cdfc05bef2c377e8d271bac3)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(17U, 6U) |
| #define | [GPIO28\_P18](#a91221a9648fa4d08c5b4f928a9756c50)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(18U, 0U) |
| #define | [TCK\_P19](#af651d7aa9e7ee9ed0f39ea4ea72d6c3b)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(19U, 1U) |
| #define | [GT\_PWM03\_P19](#a7c7fb987ccc55419a645a4a04b30e200)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(19U, 8U) |
| #define | [GPIO29\_P20](#abcec00f5b87b8c75cedc5d73ad7107d3)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(20U, 0U) |
| #define | [TMS\_P20](#a5d14159904ec1c4f56c911e643a7eed4)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(20U, 1U) |
| #define | [GPIO25\_P21](#ab316bbdba3762342b3823d9eee34809d)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(21U, 0U) |
| #define | [GT\_PWM02\_P21](#aa34e4da30d6f3b91df53e14b195650bc)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(21U, 9U) |
| #define | [MCASFX\_P21](#ad0767fcefbfc59f576341422ab3c466f)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(21U, 2U) |
| #define | [ANTSEL1\_P29](#ae4b7bd32af0c430944caa10343c7ba89)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(29U, 0U) |
| #define | [ANTSEL2\_P30](#a637bd5bc2080ed718ed875255907ab81)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(30U, 0U) |
| #define | [GPIO31\_P45](#a0ad70dd2e46b8e463283999c065b1031)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(45U, 0U) |
| #define | [UART0\_RX\_P45](#aec30ecff2290ff162f4940376f092f77)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(45U, 9U) |
| #define | [MCAFSX\_P45](#a0c5127de54dfe7be823dbba91260eeb8)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(45U, 12U) |
| #define | [UART1\_RX\_P45](#ac379119f98304c790ab8cbba4752feec)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(45U, 2U) |
| #define | [MCAXR0\_P45](#a93408262bf38798525fc1ed43b759759)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(45U, 6U) |
| #define | [GSPI\_CLK\_P45](#a41607ce5c19fb904cef1b5b9ff065bca)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(45U, 7U) |
| #define | [GPIO0\_P50](#a0023dcef0f950996fb69b99ae6cb7529)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(50U, 0U) |
| #define | [UART0\_CTSN\_P50](#aa8acf830a7e0ba5aef12422b0f594999)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(50U, 12U) |
| #define | [MCAXR1\_P50](#a2c2f38b43528c3d2ed0d909cb276a834)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(50U, 6U) |
| #define | [GT\_CCP00\_P50](#a4b59e68f954e26a5a22a946c83c7b35c)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(50U, 7U) |
| #define | [GSPI\_CS\_P50](#a9531166ec008c53ebcb3bb7770bc9cfb)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(50U, 9U) |
| #define | [UART1\_RTS\_P50](#afc79f99843ab6ec1fcc46e475516d3ea)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(50U, 10U) |
| #define | [UART0\_RTS\_P50](#a202ce4d02639e2277dc70f8c34e96796)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(50U, 3U) |
| #define | [MCAXR0\_P50](#a92fa65531018efc9a2fe37d1920d609e)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(50U, 4U) |
| #define | [GPIO32\_P52](#a6f73c352c071329e8b51d62272e6b597)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(52U, 0U) |
| #define | [MCACLK\_P52](#a4de157ff760a13c620d8bc5730166dfd)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(52U, 2U) |
| #define | [MCAXR0\_P52](#a85e3fa7f05e7b0f8d2b58741d42e90bc)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(52U, 4U) |
| #define | [UART0\_RTS\_P52](#ae3dd30595d8647e48844b8b9a204eee4)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(52U, 6U) |
| #define | [GSPI\_MOSI\_P52](#a0472ccf0e3dde61e9b10c4ee44034a05)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(52U, 8U) |
| #define | [GPIO30\_P53](#af1056beafa7c3f45e3096c66e1631096)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(53U, 0U) |
| #define | [UART0\_TX\_P53](#afa26fef4c910605bfc58516bba2b0446)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(53U, 9U) |
| #define | [MCACLK\_P53](#ad2986e8a3004f19836aaf1264bbb052d)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(53U, 2U) |
| #define | [MCAFSX\_P53](#a8433ec0dd136e712bcffc99562d77a13)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(53U, 3U) |
| #define | [GT\_CCP05\_P53](#ac91e88a5f0e186cea7cf4c1089a93e7e)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(53U, 4U) |
| #define | [GSPI\_MISO\_P53](#aaadb7b665b0adb1eed8d7a632c361910)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(53U, 7U) |
| #define | [GPIO1\_P55](#a581e291b3887f522a35a7529db6c6a9b)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(55U, 0U) |
| #define | [UART0\_TX\_P55](#ae02a8d280e708f2b28314c565b8368c7)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(55U, 3U) |
| #define | [PCLK\_P55](#acd84f05bdec8c70ee04acb87020286a1)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(55U, 4U) |
| #define | [UART1\_TX\_P55](#a06c9f6cc98ffdc8b53495a785fbcb3bd)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(55U, 6U) |
| #define | [GT\_CCP01\_P55](#a8d323feb4cf8d2264da5f94853acfcd2)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(55U, 7U) |
| #define | [GPIO2\_P57](#ad92d7838cfa819c6ba4a896101d4ffca)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(57U, 0U) |
| #define | [UART0\_RX\_P57](#a9220f19106cb9f8840a1b90607948dcc)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(57U, 3U) |
| #define | [UART1\_RX\_P57](#a2a67e698005d5be4baf74216341adf8e)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(57U, 6U) |
| #define | [GT\_CCP02\_P57](#af126c52c2ae52c91b68e9184004cfdcf)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(57U, 7U) |
| #define | [GPIO3\_P58](#a70ea8f18a9106a3c5d43bbee1d8af546)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(58U, 0U) |
| #define | [UART1\_TX\_P58](#a33fe230e16d7b9ddfc5c4e5f6affa32d)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(58U, 6U) |
| #define | [PDATA7\_P58](#a97849d9928b913f404d1a7be447051bf)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(58U, 7U) |
| #define | [GPIO5\_P59](#aa189b623df8558a6438d176fc406abc2)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(59U, 0U) |
| #define | [UART1\_RX\_P59](#a20c1984c49c52b45fb9024d45a0bdb27)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(59U, 6U) |
| #define | [PDATA6\_P59](#aa631c65c36a4db5ba54f9603427911d3)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(59U, 4U) |
| #define | [GPIO5\_P60](#ae248cf8dc867d6f9114cd3aaa51b06ca)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(60U, 0U) |
| #define | [PDATA5\_P60](#a0a03dacfa4378314839df59511f7af27)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(60U, 4U) |
| #define | [MCAXR1\_P60](#a7f6eb41b90608548c67fe52ac7285678)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(60U, 6U) |
| #define | [GT\_CCP05\_P60](#adcfc77087d75e8f687ca40cf102c5672)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(60U, 7U) |
| #define | [GPIO6\_P61](#a9fdaf32c4cf8469a4965405f564066dc)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(61U, 0U) |
| #define | [UART0\_RTS\_P61](#a68e13f52aab072bee8eed2de25737730)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(61U, 5U) |
| #define | [PDATA4\_P61](#aca1510ae9b35a8c0f75d486bcd219feb)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(61U, 4U) |
| #define | [UART1\_CTS\_P61](#a182be28929eb2e11c780d3f7bd3914a6)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(61U, 3U) |
| #define | [UART0\_CTS\_P61](#abebbd1dd7206417c61aff603dc0d3c3a)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(61U, 6U) |
| #define | [GT\_CCP06\_P61](#a1de5f909c12eadb029562bf14197ffc7)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(61U, 7U) |
| #define | [GPIO7\_P62](#a0a6f11f997a0e220dfff39bb2b419219)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(62U, 0U) |
| #define | [MCACLKX\_P62](#a900e65546f481f00fc2cb80218063bfd)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(62U, 13U) |
| #define | [UART1\_RTS\_P62](#a2f6c6154904c3dce5496d8c837e4fbf0)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(62U, 3U) |
| #define | [UART0\_RTS\_P62](#af4ef5b36c0c036734bd924586fabc519)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(62U, 10U) |
| #define | [UART0\_TX\_P62](#a29e0564a1b5101a50836a9cfa97a7a63)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(62U, 11U) |
| #define | [GPIO8\_P63](#ad36e2c84424950a91028054c3499b579)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(63U, 0U) |
| #define | [SDCARD\_IRQ\_P63](#a2edc3859ba96c9902d3c5eb2298a86ca)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(63U, 6U) |
| #define | [MCAFSX\_P63](#a24efd787cbb04117197d27289eab0d83)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(63U, 7U) |
| #define | [GT\_CCP06\_P63](#af36b5558e59ca508f363a52c3fb180a0)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(63U, 12U) |
| #define | [GPIO9\_P64](#a25a3031376018d5d679597770b0552f0)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(64U, 0U) |
| #define | [GT\_PWM05\_P64](#a4a276c8f1545d3b817ced42811b934f7)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(64U, 3U) |
| #define | [SDCARD\_DATA\_P64](#a18587659510c1d7f7a3fc761b021999d)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(64U, 6U) |
| #define | [MCAXR0\_P64](#a98e96c0252ec68f37144096625e1492d)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(64U, 7U) |
| #define | [GT\_CCP00\_P64](#a45b13479b3cdedf5488f122a3b3ec288)   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(64U, 12U) |

## Macro Definition Documentation

## [◆ ](#ae4b7bd32af0c430944caa10343c7ba89)ANTSEL1\_P29

| #define ANTSEL1\_P29   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(29U, 0U) |
| --- |

## [◆ ](#a637bd5bc2080ed718ed875255907ab81)ANTSEL2\_P30

| #define ANTSEL2\_P30   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(30U, 0U) |
| --- |

## [◆ ](#a0023dcef0f950996fb69b99ae6cb7529)GPIO0\_P50

| #define GPIO0\_P50   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(50U, 0U) |
| --- |

## [◆ ](#a89f97aa766818f7482c3131b39fc57c6)GPIO10\_P1

| #define GPIO10\_P1   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(1U, 0U) |
| --- |

## [◆ ](#a092456dadbe48fb30ca448f893ff182d)GPIO11\_P2

| #define GPIO11\_P2   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(2U, 0U) |
| --- |

## [◆ ](#aa7fe336032aa6ad0cc8377bef839c249)GPIO12\_P3

| #define GPIO12\_P3   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(3U, 0U) |
| --- |

## [◆ ](#aa63a6fa68392be5d91f17f1512bca933)GPIO13\_P4

| #define GPIO13\_P4   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(4U, 0U) |
| --- |

## [◆ ](#a9c9da9f7d6f9b370c7548f936fe70b65)GPIO14\_P5

| #define GPIO14\_P5   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(5U, 0U) |
| --- |

## [◆ ](#a0b94b2938ede1a6d84b397b12399aa58)GPIO15\_P6

| #define GPIO15\_P6   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(6U, 0U) |
| --- |

## [◆ ](#a48e7884a7dfad77efe683eea6e678e1b)GPIO16\_P7

| #define GPIO16\_P7   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(7U, 0U) |
| --- |

## [◆ ](#a499b75b5acdf56015bc34363e8770625)GPIO17\_P8

| #define GPIO17\_P8   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(8U, 0U) |
| --- |

## [◆ ](#a581e291b3887f522a35a7529db6c6a9b)GPIO1\_P55

| #define GPIO1\_P55   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(55U, 0U) |
| --- |

## [◆ ](#a7bccf18256e2c16eeb9c2712b4123bed)GPIO22\_P15

| #define GPIO22\_P15   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(15U, 0U) |
| --- |

## [◆ ](#a6e86e11b2fa406cf3d0a0ec57d1e856f)GPIO23\_P16

| #define GPIO23\_P16   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(16U, 0U) |
| --- |

## [◆ ](#a80df0d9d7b3c95e556dd6f82f4551f0b)GPIO24\_P17

| #define GPIO24\_P17   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(17U, 0U) |
| --- |

## [◆ ](#ab316bbdba3762342b3823d9eee34809d)GPIO25\_P21

| #define GPIO25\_P21   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(21U, 0U) |
| --- |

## [◆ ](#a91221a9648fa4d08c5b4f928a9756c50)GPIO28\_P18

| #define GPIO28\_P18   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(18U, 0U) |
| --- |

## [◆ ](#abcec00f5b87b8c75cedc5d73ad7107d3)GPIO29\_P20

| #define GPIO29\_P20   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(20U, 0U) |
| --- |

## [◆ ](#ad92d7838cfa819c6ba4a896101d4ffca)GPIO2\_P57

| #define GPIO2\_P57   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(57U, 0U) |
| --- |

## [◆ ](#af1056beafa7c3f45e3096c66e1631096)GPIO30\_P53

| #define GPIO30\_P53   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(53U, 0U) |
| --- |

## [◆ ](#a0ad70dd2e46b8e463283999c065b1031)GPIO31\_P45

| #define GPIO31\_P45   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(45U, 0U) |
| --- |

## [◆ ](#a6f73c352c071329e8b51d62272e6b597)GPIO32\_P52

| #define GPIO32\_P52   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(52U, 0U) |
| --- |

## [◆ ](#a70ea8f18a9106a3c5d43bbee1d8af546)GPIO3\_P58

| #define GPIO3\_P58   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(58U, 0U) |
| --- |

## [◆ ](#aa189b623df8558a6438d176fc406abc2)GPIO5\_P59

| #define GPIO5\_P59   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(59U, 0U) |
| --- |

## [◆ ](#ae248cf8dc867d6f9114cd3aaa51b06ca)GPIO5\_P60

| #define GPIO5\_P60   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(60U, 0U) |
| --- |

## [◆ ](#a9fdaf32c4cf8469a4965405f564066dc)GPIO6\_P61

| #define GPIO6\_P61   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(61U, 0U) |
| --- |

## [◆ ](#a0a6f11f997a0e220dfff39bb2b419219)GPIO7\_P62

| #define GPIO7\_P62   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(62U, 0U) |
| --- |

## [◆ ](#ad36e2c84424950a91028054c3499b579)GPIO8\_P63

| #define GPIO8\_P63   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(63U, 0U) |
| --- |

## [◆ ](#a25a3031376018d5d679597770b0552f0)GPIO9\_P64

| #define GPIO9\_P64   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(64U, 0U) |
| --- |

## [◆ ](#a41607ce5c19fb904cef1b5b9ff065bca)GSPI\_CLK\_P45

| #define GSPI\_CLK\_P45   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(45U, 7U) |
| --- |

## [◆ ](#a0835204b6761fdb5da07401588cb60a8)GSPI\_CLK\_P5

| #define GSPI\_CLK\_P5   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(5U, 7U) |
| --- |

## [◆ ](#a9531166ec008c53ebcb3bb7770bc9cfb)GSPI\_CS\_P50

| #define GSPI\_CS\_P50   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(50U, 9U) |
| --- |

## [◆ ](#a4a2c3ec59d144e1e20147f3fac31c7cf)GSPI\_CS\_P8

| #define GSPI\_CS\_P8   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(8U, 7U) |
| --- |

## [◆ ](#aaadb7b665b0adb1eed8d7a632c361910)GSPI\_MISO\_P53

| #define GSPI\_MISO\_P53   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(53U, 7U) |
| --- |

## [◆ ](#a2e33fd1fd267afccbef0ca274336708d)GSPI\_MISO\_P6

| #define GSPI\_MISO\_P6   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(6U, 7U) |
| --- |

## [◆ ](#a0472ccf0e3dde61e9b10c4ee44034a05)GSPI\_MOSI\_P52

| #define GSPI\_MOSI\_P52   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(52U, 8U) |
| --- |

## [◆ ](#a06cd1b5b0df08a309fc7d9d0eb176948)GSPI\_MOSI\_P7

| #define GSPI\_MOSI\_P7   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(7U, 7U) |
| --- |

## [◆ ](#a4b59e68f954e26a5a22a946c83c7b35c)GT\_CCP00\_P50

| #define GT\_CCP00\_P50   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(50U, 7U) |
| --- |

## [◆ ](#a45b13479b3cdedf5488f122a3b3ec288)GT\_CCP00\_P64

| #define GT\_CCP00\_P64   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(64U, 12U) |
| --- |

## [◆ ](#a41832e073da75fce278ea3f3a10c7981)GT\_CCP01\_P1

| #define GT\_CCP01\_P1   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(1U, 12U) |
| --- |

## [◆ ](#a8d323feb4cf8d2264da5f94853acfcd2)GT\_CCP01\_P55

| #define GT\_CCP01\_P55   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(55U, 7U) |
| --- |

## [◆ ](#a29f1d9fd07affc428b9ec13021951496)GT\_CCP02\_P2

| #define GT\_CCP02\_P2   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(2U, 12U) |
| --- |

## [◆ ](#af126c52c2ae52c91b68e9184004cfdcf)GT\_CCP02\_P57

| #define GT\_CCP02\_P57   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(57U, 7U) |
| --- |

## [◆ ](#a11be8733f58686a917f33eebc3f83f9f)GT\_CCP03\_P3

| #define GT\_CCP03\_P3   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(3U, 12U) |
| --- |

## [◆ ](#a93a7b969c1094f0c7a4811218a6d6b05)GT\_CCP04\_P15

| #define GT\_CCP04\_P15   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(15U, 5U) |
| --- |

## [◆ ](#a469f19224eef6881cc1247eed19c94a9)GT\_CCP04\_P4

| #define GT\_CCP04\_P4   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(4U, 12U) |
| --- |

## [◆ ](#a85dd880198761cbddb32b2d482247bfa)GT\_CCP05\_P5

| #define GT\_CCP05\_P5   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(5U, 12U) |
| --- |

## [◆ ](#ac91e88a5f0e186cea7cf4c1089a93e7e)GT\_CCP05\_P53

| #define GT\_CCP05\_P53   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(53U, 4U) |
| --- |

## [◆ ](#adcfc77087d75e8f687ca40cf102c5672)GT\_CCP05\_P60

| #define GT\_CCP05\_P60   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(60U, 7U) |
| --- |

## [◆ ](#a3ba8bacb70f2bcadaa6dfd786a673bd7)GT\_CCP06\_P17

| #define GT\_CCP06\_P17   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(17U, 4U) |
| --- |

## [◆ ](#a912c145e14635c2fade2b206d71df0a3)GT\_CCP06\_P6

| #define GT\_CCP06\_P6   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(6U, 13U) |
| --- |

## [◆ ](#a1de5f909c12eadb029562bf14197ffc7)GT\_CCP06\_P61

| #define GT\_CCP06\_P61   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(61U, 7U) |
| --- |

## [◆ ](#af36b5558e59ca508f363a52c3fb180a0)GT\_CCP06\_P63

| #define GT\_CCP06\_P63   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(63U, 12U) |
| --- |

## [◆ ](#a2688169c0aa3bfc4333550d77b03f301)GT\_CCP07\_P7

| #define GT\_CCP07\_P7   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(7U, 13U) |
| --- |

## [◆ ](#aa34e4da30d6f3b91df53e14b195650bc)GT\_PWM02\_P21

| #define GT\_PWM02\_P21   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(21U, 9U) |
| --- |

## [◆ ](#a7c7fb987ccc55419a645a4a04b30e200)GT\_PWM03\_P19

| #define GT\_PWM03\_P19   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(19U, 8U) |
| --- |

## [◆ ](#a4a276c8f1545d3b817ced42811b934f7)GT\_PWM05\_P64

| #define GT\_PWM05\_P64   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(64U, 3U) |
| --- |

## [◆ ](#a1b2e5aea3aad1cf49a0c9ed9c1abd0ac)GT\_PWM06\_P1

| #define GT\_PWM06\_P1   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(1U, 3U) |
| --- |

## [◆ ](#a158549be521c32cbadd7fd94a59bc945)GT\_PWM07\_P2

| #define GT\_PWM07\_P2   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(2U, 3U) |
| --- |

## [◆ ](#abd05f625495d2ea978dd73f2163ac895)I2C\_SCL\_P1

| #define I2C\_SCL\_P1   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(1U, 1U) |
| --- |

## [◆ ](#a8267f2892d868a33b27c68ae6673f239)I2C\_SCL\_P16

| #define I2C\_SCL\_P16   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(16U, 9U) |
| --- |

## [◆ ](#a7f43eaa1290d1c51ad8dd0eead54eac8)I2C\_SCL\_P3

| #define I2C\_SCL\_P3   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(3U, 5U) |
| --- |

## [◆ ](#a4894dca0ecb760732bf032d80a6d8a13)I2C\_SCL\_P5

| #define I2C\_SCL\_P5   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(5U, 5U) |
| --- |

## [◆ ](#a0b1353bc11a6e1a156c6dbe4e59f74d0)I2C\_SDA\_P17

| #define I2C\_SDA\_P17   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(17U, 9U) |
| --- |

## [◆ ](#a38fbe2595b40a64618809999d9ff7e88)I2C\_SDA\_P2

| #define I2C\_SDA\_P2   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(2U, 1U) |
| --- |

## [◆ ](#a2ac054fb4527be70688dfbad814da263)I2C\_SDA\_P4

| #define I2C\_SDA\_P4   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(4U, 5U) |
| --- |

## [◆ ](#ac8ded51ba9587b17cf1c2565f635a8a2)I2C\_SDA\_P6

| #define I2C\_SDA\_P6   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(6U, 5U) |
| --- |

## [◆ ](#a449900e101576c23577ae8731ff6d832)MCACLK\_P3

| #define MCACLK\_P3   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(3U, 3U) |
| --- |

## [◆ ](#a4de157ff760a13c620d8bc5730166dfd)MCACLK\_P52

| #define MCACLK\_P52   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(52U, 2U) |
| --- |

## [◆ ](#ad2986e8a3004f19836aaf1264bbb052d)MCACLK\_P53

| #define MCACLK\_P53   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(53U, 2U) |
| --- |

## [◆ ](#a900e65546f481f00fc2cb80218063bfd)MCACLKX\_P62

| #define MCACLKX\_P62   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(62U, 13U) |
| --- |

## [◆ ](#ae4a09b647c36db2a78d4d8a128d47ac5)MCAFSX\_P15

| #define MCAFSX\_P15   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(15U, 7U) |
| --- |

## [◆ ](#a082b74a8cdfc05bef2c377e8d271bac3)MCAFSX\_P17

| #define MCAFSX\_P17   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(17U, 6U) |
| --- |

## [◆ ](#af81018b6a0cfba2b48bcdc9cf864d609)MCAFSX\_P2

| #define MCAFSX\_P2   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(2U, 13U) |
| --- |

## [◆ ](#a0c5127de54dfe7be823dbba91260eeb8)MCAFSX\_P45

| #define MCAFSX\_P45   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(45U, 12U) |
| --- |

## [◆ ](#a8433ec0dd136e712bcffc99562d77a13)MCAFSX\_P53

| #define MCAFSX\_P53   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(53U, 3U) |
| --- |

## [◆ ](#a24efd787cbb04117197d27289eab0d83)MCAFSX\_P63

| #define MCAFSX\_P63   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(63U, 7U) |
| --- |

## [◆ ](#ad0767fcefbfc59f576341422ab3c466f)MCASFX\_P21

| #define MCASFX\_P21   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(21U, 2U) |
| --- |

## [◆ ](#a93408262bf38798525fc1ed43b759759)MCAXR0\_P45

| #define MCAXR0\_P45   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(45U, 6U) |
| --- |

## [◆ ](#a92fa65531018efc9a2fe37d1920d609e)MCAXR0\_P50

| #define MCAXR0\_P50   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(50U, 4U) |
| --- |

## [◆ ](#a85e3fa7f05e7b0f8d2b58741d42e90bc)MCAXR0\_P52

| #define MCAXR0\_P52   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(52U, 4U) |
| --- |

## [◆ ](#a98e96c0252ec68f37144096625e1492d)MCAXR0\_P64

| #define MCAXR0\_P64   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(64U, 7U) |
| --- |

## [◆ ](#a2c2f38b43528c3d2ed0d909cb276a834)MCAXR1\_P50

| #define MCAXR1\_P50   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(50U, 6U) |
| --- |

## [◆ ](#a7f6eb41b90608548c67fe52ac7285678)MCAXR1\_P60

| #define MCAXR1\_P60   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(60U, 6U) |
| --- |

## [◆ ](#acd84f05bdec8c70ee04acb87020286a1)PCLK\_P55

| #define PCLK\_P55   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(55U, 4U) |
| --- |

## [◆ ](#a4ba12e404845b1777c7fc27673a358c6)PDATA10\_P7

| #define PDATA10\_P7   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(7U, 4U) |
| --- |

## [◆ ](#aec9421895f489defea513f9451f19a59)PDATA11\_P8

| #define PDATA11\_P8   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(8U, 4U) |
| --- |

## [◆ ](#aca1510ae9b35a8c0f75d486bcd219feb)PDATA4\_P61

| #define PDATA4\_P61   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(61U, 4U) |
| --- |

## [◆ ](#a0a03dacfa4378314839df59511f7af27)PDATA5\_P60

| #define PDATA5\_P60   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(60U, 4U) |
| --- |

## [◆ ](#aa631c65c36a4db5ba54f9603427911d3)PDATA6\_P59

| #define PDATA6\_P59   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(59U, 4U) |
| --- |

## [◆ ](#a97849d9928b913f404d1a7be447051bf)PDATA7\_P58

| #define PDATA7\_P58   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(58U, 7U) |
| --- |

## [◆ ](#a420084bc2bed97ccfa6cabbdcea111b8)PDATA8\_P5

| #define PDATA8\_P5   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(5U, 4U) |
| --- |

## [◆ ](#a74f7003fe754549a7abd536ce7ca18e0)PDATA9\_P6

| #define PDATA9\_P6   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(6U, 4U) |
| --- |

## [◆ ](#a784b4247574d785820e1960b77d243f8)PHS\_P4

| #define PHS\_P4   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(4U, 4U) |
| --- |

## [◆ ](#a040fa03ccf78c01cf8353dfafaed4363)PVS\_P3

| #define PVS\_P3   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(3U, 4U) |
| --- |

## [◆ ](#a6c881b3b5ceb937e8441bd0cd3b449e8)PWM0\_P17

| #define PWM0\_P17   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(17U, 5U) |
| --- |

## [◆ ](#af0194d8218ffae6e4ca6afdc1b75184c)PXCLK\_P2

| #define PXCLK\_P2   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(2U, 4U) |
| --- |

## [◆ ](#a0348e53054efacbcc5f4b36f5983b483)SDCARD\_CLK\_P1

| #define SDCARD\_CLK\_P1   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(1U, 6U) |
| --- |

## [◆ ](#ad19d6a6d4e575fdedc182d95c426ef7a)SDCARD\_CLK\_P7

| #define SDCARD\_CLK\_P7   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(7U, 8U) |
| --- |

## [◆ ](#af4b6115dd55265aa56f4fd0e4519449d)SDCARD\_CMD\_P2

| #define SDCARD\_CMD\_P2   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(2U, 6U) |
| --- |

## [◆ ](#a23c36223a0811761121eb6992e733191)SDCARD\_CMD\_P8

| #define SDCARD\_CMD\_P8   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(8U, 8U) |
| --- |

## [◆ ](#a1f11274609e837c40dbfcf3f4bb2c65b)SDCARD\_DATA3\_P6

| #define SDCARD\_DATA3\_P6   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(6U, 8U) |
| --- |

## [◆ ](#a18587659510c1d7f7a3fc761b021999d)SDCARD\_DATA\_P64

| #define SDCARD\_DATA\_P64   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(64U, 6U) |
| --- |

## [◆ ](#a2edc3859ba96c9902d3c5eb2298a86ca)SDCARD\_IRQ\_P63

| #define SDCARD\_IRQ\_P63   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(63U, 6U) |
| --- |

## [◆ ](#af651d7aa9e7ee9ed0f39ea4ea72d6c3b)TCK\_P19

| #define TCK\_P19   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(19U, 1U) |
| --- |

## [◆ ](#aa8b475c426b332c82e21567727bb482a)TDI\_P16

| #define TDI\_P16   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(16U, 1U) |
| --- |

## [◆ ](#a16ea3f7a2cb062dcdab07e50b4f5c049)TDO\_P17

| #define TDO\_P17   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(17U, 1U) |
| --- |

## [◆ ](#a381590ba2880c42636058c248f7e0e2e)TI\_CC32XX\_MUX\_MSK

| #define TI\_CC32XX\_MUX\_MSK   0xFU |
| --- |

## [◆ ](#ac9e2e00ac00ddd1eaf84331d18806339)TI\_CC32XX\_MUX\_POS

| #define TI\_CC32XX\_MUX\_POS   0U |
| --- |

## [◆ ](#a40cc14e2a5969a01d7a764fb5bdb84a7)TI\_CC32XX\_PIN\_MSK

| #define TI\_CC32XX\_PIN\_MSK   0x3FU |
| --- |

## [◆ ](#aea6f7d34537febd574f9ea0db1fbf3f3)TI\_CC32XX\_PIN\_POS

| #define TI\_CC32XX\_PIN\_POS   16U |
| --- |

## [◆ ](#a4bf6d48b1ebcaaeb96b0450533dfa428)TI\_CC32XX\_PINMUX

| #define TI\_CC32XX\_PINMUX | ( |  | *pin*, |
| --- | --- | --- | --- |
|  |  |  | *mux* ) |

**Value:**

((((pin)&[TI\_CC32XX\_PIN\_MSK](#a40cc14e2a5969a01d7a764fb5bdb84a7)) << [TI\_CC32XX\_PIN\_POS](#aea6f7d34537febd574f9ea0db1fbf3f3)) | \

(((mux)&[TI\_CC32XX\_MUX\_MSK](#a381590ba2880c42636058c248f7e0e2e)) << [TI\_CC32XX\_MUX\_POS](#ac9e2e00ac00ddd1eaf84331d18806339)))

[TI\_CC32XX\_MUX\_MSK](#a381590ba2880c42636058c248f7e0e2e)

#define TI\_CC32XX\_MUX\_MSK

**Definition** ti-cc32xx-pinctrl.h:33

[TI\_CC32XX\_PIN\_MSK](#a40cc14e2a5969a01d7a764fb5bdb84a7)

#define TI\_CC32XX\_PIN\_MSK

**Definition** ti-cc32xx-pinctrl.h:31

[TI\_CC32XX\_MUX\_POS](#ac9e2e00ac00ddd1eaf84331d18806339)

#define TI\_CC32XX\_MUX\_POS

**Definition** ti-cc32xx-pinctrl.h:34

[TI\_CC32XX\_PIN\_POS](#aea6f7d34537febd574f9ea0db1fbf3f3)

#define TI\_CC32XX\_PIN\_POS

**Definition** ti-cc32xx-pinctrl.h:32

Utility macro to build TI CC32XX pinmux property entry.

Parameters
:   | pin | Pin |
    | --- | --- |
    | mux | Multiplexer choice |

## [◆ ](#a5d14159904ec1c4f56c911e643a7eed4)TMS\_P20

| #define TMS\_P20   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(20U, 1U) |
| --- |

## [◆ ](#abebbd1dd7206417c61aff603dc0d3c3a)UART0\_CTS\_P61

| #define UART0\_CTS\_P61   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(61U, 6U) |
| --- |

## [◆ ](#aa8acf830a7e0ba5aef12422b0f594999)UART0\_CTSN\_P50

| #define UART0\_CTSN\_P50   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(50U, 12U) |
| --- |

## [◆ ](#a202ce4d02639e2277dc70f8c34e96796)UART0\_RTS\_P50

| #define UART0\_RTS\_P50   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(50U, 3U) |
| --- |

## [◆ ](#ae3dd30595d8647e48844b8b9a204eee4)UART0\_RTS\_P52

| #define UART0\_RTS\_P52   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(52U, 6U) |
| --- |

## [◆ ](#a68e13f52aab072bee8eed2de25737730)UART0\_RTS\_P61

| #define UART0\_RTS\_P61   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(61U, 5U) |
| --- |

## [◆ ](#af4ef5b36c0c036734bd924586fabc519)UART0\_RTS\_P62

| #define UART0\_RTS\_P62   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(62U, 10U) |
| --- |

## [◆ ](#a8526e278e737f86b5416d2432e06a961)UART0\_RX\_P4

| #define UART0\_RX\_P4   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(4U, 7U) |
| --- |

## [◆ ](#aec30ecff2290ff162f4940376f092f77)UART0\_RX\_P45

| #define UART0\_RX\_P45   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(45U, 9U) |
| --- |

## [◆ ](#a9220f19106cb9f8840a1b90607948dcc)UART0\_RX\_P57

| #define UART0\_RX\_P57   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(57U, 3U) |
| --- |

## [◆ ](#a0a31d5b2068953d90f7e152cfdeec235)UART0\_TX\_P3

| #define UART0\_TX\_P3   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(3U, 7U) |
| --- |

## [◆ ](#afa26fef4c910605bfc58516bba2b0446)UART0\_TX\_P53

| #define UART0\_TX\_P53   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(53U, 9U) |
| --- |

## [◆ ](#ae02a8d280e708f2b28314c565b8368c7)UART0\_TX\_P55

| #define UART0\_TX\_P55   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(55U, 3U) |
| --- |

## [◆ ](#a29e0564a1b5101a50836a9cfa97a7a63)UART0\_TX\_P62

| #define UART0\_TX\_P62   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(62U, 11U) |
| --- |

## [◆ ](#a182be28929eb2e11c780d3f7bd3914a6)UART1\_CTS\_P61

| #define UART1\_CTS\_P61   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(61U, 3U) |
| --- |

## [◆ ](#afc79f99843ab6ec1fcc46e475516d3ea)UART1\_RTS\_P50

| #define UART1\_RTS\_P50   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(50U, 10U) |
| --- |

## [◆ ](#a2f6c6154904c3dce5496d8c837e4fbf0)UART1\_RTS\_P62

| #define UART1\_RTS\_P62   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(62U, 3U) |
| --- |

## [◆ ](#a632c817fbe28a138a9916a4946ee9da5)UART1\_RX\_P17

| #define UART1\_RX\_P17   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(17U, 2U) |
| --- |

## [◆ ](#a6c343f9636e9d3b43d19b3d0fe9f00b1)UART1\_RX\_P2

| #define UART1\_RX\_P2   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(2U, 7U) |
| --- |

## [◆ ](#ac379119f98304c790ab8cbba4752feec)UART1\_RX\_P45

| #define UART1\_RX\_P45   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(45U, 2U) |
| --- |

## [◆ ](#a2a67e698005d5be4baf74216341adf8e)UART1\_RX\_P57

| #define UART1\_RX\_P57   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(57U, 6U) |
| --- |

## [◆ ](#a20c1984c49c52b45fb9024d45a0bdb27)UART1\_RX\_P59

| #define UART1\_RX\_P59   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(59U, 6U) |
| --- |

## [◆ ](#a9f7daa4bf7f1e01439d84c58da7c7235)UART1\_RX\_P8

| #define UART1\_RX\_P8   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(8U, 5U) |
| --- |

## [◆ ](#a995c80839609dc2f99440020c4b376c4)UART1\_TX\_P1

| #define UART1\_TX\_P1   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(1U, 7U) |
| --- |

## [◆ ](#af2bdaab6fc0f793aee2bc8821869aad6)UART1\_TX\_P16

| #define UART1\_TX\_P16   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(16U, 2U) |
| --- |

## [◆ ](#a06c9f6cc98ffdc8b53495a785fbcb3bd)UART1\_TX\_P55

| #define UART1\_TX\_P55   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(55U, 6U) |
| --- |

## [◆ ](#a33fe230e16d7b9ddfc5c4e5f6affa32d)UART1\_TX\_P58

| #define UART1\_TX\_P58   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(58U, 6U) |
| --- |

## [◆ ](#a3e9e600bebc357ff182f42317b4fbc5f)UART1\_TX\_P7

| #define UART1\_TX\_P7   [TI\_CC32XX\_PINMUX](#a4bf6d48b1ebcaaeb96b0450533dfa428)(7U, 5U) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [ti-cc32xx-pinctrl.h](ti-cc32xx-pinctrl_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
