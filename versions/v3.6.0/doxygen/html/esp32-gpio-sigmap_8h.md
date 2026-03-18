---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/esp32-gpio-sigmap_8h.html
original_path: doxygen/html/esp32-gpio-sigmap_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32-gpio-sigmap.h File Reference

[Go to the source code of this file.](esp32-gpio-sigmap_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ESP\_NOSIG](#af80260535bc3aee44c28c972a29483e0)   [ESP\_SIG\_INVAL](esp-pinctrl-common_8h.md#ae0d2e726ab8d90343e5c80e1d9b85ad8) |
| #define | [ESP\_SPICLK\_IN](#a89331a24c2b322eda2d32394ec1f08bc)   0 |
| #define | [ESP\_SPICLK\_OUT](#a5f440c922a53085bb7b28f469c2a14b0)   0 |
| #define | [ESP\_SPIQ\_IN](#aec51ff955c6be50e529affc87ec9d5cb)   1 |
| #define | [ESP\_SPIQ\_OUT](#a5816deeca8853397a830a8eb251704ee)   1 |
| #define | [ESP\_SPID\_IN](#a26c603fd58dbd7526d2be3bb3e37758a)   2 |
| #define | [ESP\_SPID\_OUT](#af81b2fc65b68ed2238ab3367a8731102)   2 |
| #define | [ESP\_SPIHD\_IN](#a49783f877b666aff9362cf605590b991)   3 |
| #define | [ESP\_SPIHD\_OUT](#a8851b5256482790f3304efecafc13afd)   3 |
| #define | [ESP\_SPIWP\_IN](#aa74adc2812d9c6bd143c679fa4d9ca8d)   4 |
| #define | [ESP\_SPIWP\_OUT](#a470408f8102937dc017336e320e6147b)   4 |
| #define | [ESP\_SPICS0\_IN](#a7bf90419c18c69d0438a4d349e9cbdb2)   5 |
| #define | [ESP\_SPICS0\_OUT](#a5d97c07ba0d8cda594d52310e90fa6a4)   5 |
| #define | [ESP\_SPICS1\_IN](#afe3e0ee1116416992306c25420ca6efa)   6 |
| #define | [ESP\_SPICS1\_OUT](#aa4a67a38b97a3d466783c0617aa6a0c8)   6 |
| #define | [ESP\_SPICS2\_IN](#abce40937f1557fdae2dce1a96a8aab3d)   7 |
| #define | [ESP\_SPICS2\_OUT](#afdb41f1d4bc9948ea4e723e6f43a9363)   7 |
| #define | [ESP\_HSPICLK\_IN](#aa214d49ff0a9292fecc67fd8746a3201)   8 |
| #define | [ESP\_HSPICLK\_OUT](#a028245349e09fe0dac8a5d16023d6884)   8 |
| #define | [ESP\_HSPIQ\_IN](#ad73beba22fb7e7d4d2ddf56c0f260e96)   9 |
| #define | [ESP\_HSPIQ\_OUT](#a0a3b5b9357369087ac3b4aea4065b277)   9 |
| #define | [ESP\_HSPID\_IN](#a051bfe73e21998d1401febd110a98996)   10 |
| #define | [ESP\_HSPID\_OUT](#ab91738160e1970f528b96c97cd71fbf4)   10 |
| #define | [ESP\_HSPICS0\_IN](#a3cf30db72dad00ef614fdb2739dccfe6)   11 |
| #define | [ESP\_HSPICS0\_OUT](#a5e584dd081acca27717085cc7cf901f8)   11 |
| #define | [ESP\_HSPIHD\_IN](#a8f77392a0ce164e7b943c9cc80465b3f)   12 |
| #define | [ESP\_HSPIHD\_OUT](#aecbf07e7ff7852bf6b45dd88a65aaa70)   12 |
| #define | [ESP\_HSPIWP\_IN](#a34ead95b59d395722b17c73b0ce219d1)   13 |
| #define | [ESP\_HSPIWP\_OUT](#a904860708852fdec4d3e29e7cc6192f7)   13 |
| #define | [ESP\_U0RXD\_IN](#aca502efa55ce2286dc9eba28192681fd)   14 |
| #define | [ESP\_U0TXD\_OUT](#af1e58fb8e7ef86a92171eca7bb1671af)   14 |
| #define | [ESP\_U0CTS\_IN](#a530d7a918a97cd1fff1acf2f90edd4ca)   15 |
| #define | [ESP\_U0RTS\_OUT](#a4257bbc044af6ea3612313e3a0b7e7c9)   15 |
| #define | [ESP\_U0DSR\_IN](#a53e3a4557a4eb1f7f98250abef03c02a)   16 |
| #define | [ESP\_U0DTR\_OUT](#acc8716af947169c9f167bdf215c5314c)   16 |
| #define | [ESP\_U1RXD\_IN](#a2293e0646e0ad2f76d62f76425ae6770)   17 |
| #define | [ESP\_U1TXD\_OUT](#a6053b38147e28e3a7479b38e7d195136)   17 |
| #define | [ESP\_U1CTS\_IN](#a3c005e616da21a058960d6aed79427b3)   18 |
| #define | [ESP\_U1RTS\_OUT](#a8f6399745566bd5caa2020e4dcb2bb3b)   18 |
| #define | [ESP\_I2CM\_SCL\_O](#a3b913756d12daf98239924b1947d4717)   19 |
| #define | [ESP\_I2CM\_SDA\_I](#a367bd6cd5bfd5d5c7d751ee8e83cb74a)   20 |
| #define | [ESP\_I2CM\_SDA\_O](#a92f1f15e271687d72d19f3b1028f8a9e)   20 |
| #define | [ESP\_EXT\_I2C\_SCL\_O](#aadedd8576af305e1d6d56c8fa6dd30bc)   21 |
| #define | [ESP\_EXT\_I2C\_SDA\_O](#a55fa3484edd1c42124fc641667004506)   22 |
| #define | [ESP\_EXT\_I2C\_SDA\_I](#ae1190b3753881bd745085f76b9f6c165)   22 |
| #define | [ESP\_I2S0O\_BCK\_IN](#af0b9626d6b7cfd5b5c42a8127897d565)   23 |
| #define | [ESP\_I2S0O\_BCK\_OUT](#a2e76c532bd75a6af4790b30f58c4b8e9)   23 |
| #define | [ESP\_I2S1O\_BCK\_IN](#afffede35b0effa00a9d6e1077ac4aaa2)   24 |
| #define | [ESP\_I2S1O\_BCK\_OUT](#afcd05d2cf345dcf816068b0b89ac5a72)   24 |
| #define | [ESP\_I2S0O\_WS\_IN](#aad13d05d8d50227859d484deaaf6e34b)   25 |
| #define | [ESP\_I2S0O\_WS\_OUT](#a78693c10e4ac17973e7ac12c1bdf8c97)   25 |
| #define | [ESP\_I2S1O\_WS\_IN](#a7ac95a35ee6001c340cddd1424f3fa5e)   26 |
| #define | [ESP\_I2S1O\_WS\_OUT](#a84485bdfe1661269506f7ef1f70f4a87)   26 |
| #define | [ESP\_I2S0I\_BCK\_IN](#a67905afbcda699d20d8a05a8a66411af)   27 |
| #define | [ESP\_I2S0I\_BCK\_OUT](#abe571a9bad2c0e95049afd8e67c8d158)   27 |
| #define | [ESP\_I2S0I\_WS\_IN](#a4236f62ac75d5f2d56f7b1cc941d7509)   28 |
| #define | [ESP\_I2S0I\_WS\_OUT](#af039bdc8eec9ec95d3ed2bbebabb22cb)   28 |
| #define | [ESP\_I2CEXT0\_SCL\_IN](#ab607ce367da34ab0f1bd7fa648273cf1)   29 |
| #define | [ESP\_I2CEXT0\_SCL\_OUT](#a2144cc62df795547ccf2bbe3ee4c629f)   29 |
| #define | [ESP\_I2CEXT0\_SDA\_IN](#afa7061c87135b9dabe5c54f5f4ce16e6)   30 |
| #define | [ESP\_I2CEXT0\_SDA\_OUT](#aabf1378b0ad2028c36c3bb74c81d7049)   30 |
| #define | [ESP\_PWM0\_SYNC0\_IN](#a60a3fe70a1bc5ba71cb46df782901087)   31 |
| #define | [ESP\_SDIO\_TOHOST\_INT\_OUT](#aac3529b76d29e57ad20500c9d1da23f3)   31 |
| #define | [ESP\_PWM0\_SYNC1\_IN](#aca616afbb64ed37982624503545a5a72)   32 |
| #define | [ESP\_PWM0\_OUT0A](#a9397a79a46feab488c88552013790dfc)   32 |
| #define | [ESP\_PWM0\_SYNC2\_IN](#a2017681d630abc75e7298c12b86a62ce)   33 |
| #define | [ESP\_PWM0\_OUT0B](#acb3badfaed73f7069ea23dde375db62a)   33 |
| #define | [ESP\_PWM0\_F0\_IN](#a4a503a957b2fd76f257534b80069caa2)   34 |
| #define | [ESP\_PWM0\_OUT1A](#ae52e5bd4be5563caeb9861267e41d947)   34 |
| #define | [ESP\_PWM0\_F1\_IN](#af536ae867a3d8bcb7644b48c346b4b50)   35 |
| #define | [ESP\_PWM0\_OUT1B](#a9fa8e944ff2d960c141f8375c9aa0b0e)   35 |
| #define | [ESP\_PWM0\_F2\_IN](#a83f385e6b8a99314cc641083a203322b)   36 |
| #define | [ESP\_PWM0\_OUT2A](#abf74a2a32a8c36431e2f21d6cd15a610)   36 |
| #define | [ESP\_GPIO\_BT\_ACTIVE](#a47d854bfae0f88dc023613e61e6be551)   37 |
| #define | [ESP\_PWM0\_OUT2B](#a563105deedf9f7ed6818ab9a8a8aecdc)   37 |
| #define | [ESP\_GPIO\_BT\_PRIORITY](#ab8d0a9090c64518af59274603f035042)   38 |
| #define | [ESP\_PCNT\_SIG\_CH0\_IN0](#acf123456a5b9d94f370309ad39672e34)   39 |
| #define | [ESP\_PCNT\_SIG\_CH1\_IN0](#a800813b2c23f7e4bb23e032e0802a459)   40 |
| #define | [ESP\_GPIO\_WLAN\_ACTIVE](#af675ca03172d2dcee1e19ccb5236e087)   40 |
| #define | [ESP\_PCNT\_CTRL\_CH0\_IN0](#a7e3c939b0b32332a35f0bead0aa4a2a6)   41 |
| #define | [ESP\_BB\_DIAG0](#a304bc90cc758f90f6675fea611ab0cfe)   41 |
| #define | [ESP\_PCNT\_CTRL\_CH1\_IN0](#a88c5eb5c7f4169ce3e7f7056b42989a7)   42 |
| #define | [ESP\_BB\_DIAG1](#ad236bf991329914d59c194ff9003974a)   42 |
| #define | [ESP\_PCNT\_SIG\_CH0\_IN1](#a99db3d1c4e07e11fc09a4024a54fcea6)   43 |
| #define | [ESP\_BB\_DIAG2](#a26c20261a5e2f4293b81c802a0a33b19)   43 |
| #define | [ESP\_PCNT\_SIG\_CH1\_IN1](#a730113779d69ca86b257060678f8cbec)   44 |
| #define | [ESP\_BB\_DIAG3](#a5124ef75b703e7805bccd8c93828faae)   44 |
| #define | [ESP\_PCNT\_CTRL\_CH0\_IN1](#a9ec8d490316b9f043fe5e9160a7cf7e0)   45 |
| #define | [ESP\_BB\_DIAG4](#aebd2c37b71d18967bd394b32c820647f)   45 |
| #define | [ESP\_PCNT\_CTRL\_CH1\_IN1](#a0bbfffdef085eb6cedc3d1232766cb38)   46 |
| #define | [ESP\_BB\_DIAG5](#ace166b18a74fb8a42f876d1aa7cfb059)   46 |
| #define | [ESP\_PCNT\_SIG\_CH0\_IN2](#a4f9e798a260fb6ac4c39262f20253244)   47 |
| #define | [ESP\_BB\_DIAG6](#ad5685b19c170cc428cea0ee91f9155b0)   47 |
| #define | [ESP\_PCNT\_SIG\_CH1\_IN2](#a38365b3f9a2b49ef2714c38d00d293c5)   48 |
| #define | [ESP\_BB\_DIAG7](#aedf32208932dfe4471f6a5a7feb652f8)   48 |
| #define | [ESP\_PCNT\_CTRL\_CH0\_IN2](#a540cbfcd205911955effcc9814f9707c)   49 |
| #define | [ESP\_BB\_DIAG8](#a126e2108473183890c6a2e148f8fd2c7)   49 |
| #define | [ESP\_PCNT\_CTRL\_CH1\_IN2](#abf6c210e19582b06e3d6c546a009ef5b)   50 |
| #define | [ESP\_BB\_DIAG9](#a75b60b1b4d53e6fca02b3a4f14ea530e)   50 |
| #define | [ESP\_PCNT\_SIG\_CH0\_IN3](#acd8d20d89508b532a4e2749499263de3)   51 |
| #define | [ESP\_BB\_DIAG10](#aed67caee00b7ceaaaa33b2917aba60f2)   51 |
| #define | [ESP\_PCNT\_SIG\_CH1\_IN3](#ac54a606ee7096db15cdb9453b04ac72d)   52 |
| #define | [ESP\_BB\_DIAG11](#aef4bb5d62b93dfc3f2834404b6945b90)   52 |
| #define | [ESP\_PCNT\_CTRL\_CH0\_IN3](#a96e8bd4584ab671a1b0c3f0adb440943)   53 |
| #define | [ESP\_BB\_DIAG12](#acc6cd70ce139a5639022bec896a3ba5e)   53 |
| #define | [ESP\_PCNT\_CTRL\_CH1\_IN3](#a0a926d350fc11d737b545c53b3ba1671)   54 |
| #define | [ESP\_BB\_DIAG13](#afa72089303bf662a4efc8c068b157f0d)   54 |
| #define | [ESP\_PCNT\_SIG\_CH0\_IN4](#a0db0b3f57cffafbd98a8ba3a17a6cbc0)   55 |
| #define | [ESP\_BB\_DIAG14](#a4ef00458e2547f7141741191b92854d8)   55 |
| #define | [ESP\_PCNT\_SIG\_CH1\_IN4](#a0d17b8a68ec65a03d73119f26a6811ab)   56 |
| #define | [ESP\_BB\_DIAG15](#aed7c06883c6a69303a341454aff409ed)   56 |
| #define | [ESP\_PCNT\_CTRL\_CH0\_IN4](#ae5a4af55bcd763eab98fa85fe09c78df)   57 |
| #define | [ESP\_BB\_DIAG16](#a1acc29dd7c0517c30299e71c1a6ce7fa)   57 |
| #define | [ESP\_PCNT\_CTRL\_CH1\_IN4](#a0a1247ca451b38941f488721cc4df99d)   58 |
| #define | [ESP\_BB\_DIAG17](#a9abbf3178088e44d984b088f53c25ab1)   58 |
| #define | [ESP\_BB\_DIAG18](#af75798fba81841339510ecc5f94e542e)   59 |
| #define | [ESP\_BB\_DIAG19](#a4102e08a6e29f2164f5aafa109ab734b)   60 |
| #define | [ESP\_HSPICS1\_IN](#ae424fe3b3c2d6a48bdf3b9f72c0b3a3b)   61 |
| #define | [ESP\_HSPICS1\_OUT](#a8180ffc727af6c61530679be1a33ddb6)   61 |
| #define | [ESP\_HSPICS2\_IN](#aa718d7483400f89985652d1aa6b338d7)   62 |
| #define | [ESP\_HSPICS2\_OUT](#ad5849b71710c8fa5799b230fe5f40c4c)   62 |
| #define | [ESP\_VSPICLK\_IN](#ad86c783e1f7a935adc312d9a15894c9a)   63 |
| #define | [ESP\_VSPICLK\_OUT](#ada1b28a229c5f3e37a2e3d729e3f8300)   63 |
| #define | [ESP\_VSPIQ\_IN](#a4a68acaff9e8aa24b9ef3d2b1e349c10)   64 |
| #define | [ESP\_VSPIQ\_OUT](#a9651cadb9acf4b9f436752504c113b84)   64 |
| #define | [ESP\_VSPID\_IN](#aa22893d39ca3b946c7f5a36febc44a62)   65 |
| #define | [ESP\_VSPID\_OUT](#a6b9b2395789e3afbfdbf9c2faaa90b84)   65 |
| #define | [ESP\_VSPIHD\_IN](#a38c28112b8871b2f61021228961620ca)   66 |
| #define | [ESP\_VSPIHD\_OUT](#ac3b80d593bb67b9bb55be918ea1ac07c)   66 |
| #define | [ESP\_VSPIWP\_IN](#ae2f52f231a2faa56c586fd5c6afe6fc3)   67 |
| #define | [ESP\_VSPIWP\_OUT](#a69a257fe558c166843ce24c03b0347c9)   67 |
| #define | [ESP\_VSPICS0\_IN](#add4fa23bc4c1d3973d0656837c352385)   68 |
| #define | [ESP\_VSPICS0\_OUT](#ac813c68db44d91d27f040722e4d49c72)   68 |
| #define | [ESP\_VSPICS1\_IN](#a51ea9a0228493852dd9c38bfd91f102b)   69 |
| #define | [ESP\_VSPICS1\_OUT](#aad60ac2b393861f7366213d682e1089e)   69 |
| #define | [ESP\_VSPICS2\_IN](#a10f41168ec052c1414604b15bcb59d7e)   70 |
| #define | [ESP\_VSPICS2\_OUT](#ac6aaeb62e6e1c246a7a07071b162f283)   70 |
| #define | [ESP\_PCNT\_SIG\_CH0\_IN5](#acd9159d1c2dd971ec52a4965a41651f9)   71 |
| #define | [ESP\_LEDC\_HS\_SIG\_OUT0](#a67c3c6dabfb9930fa544b339eb44b0c8)   71 |
| #define | [ESP\_PCNT\_SIG\_CH1\_IN5](#a2da313499920b543ac0645fd2fc15f89)   72 |
| #define | [ESP\_LEDC\_HS\_SIG\_OUT1](#a6c5eb01aeacb1b28fe6db3e2b86ac82d)   72 |
| #define | [ESP\_PCNT\_CTRL\_CH0\_IN5](#aad99a4e2a52277508ba2ce89724acb7d)   73 |
| #define | [ESP\_LEDC\_HS\_SIG\_OUT2](#a1ae7688b4ab2ce508465491840623f85)   73 |
| #define | [ESP\_PCNT\_CTRL\_CH1\_IN5](#a9a0fede369d254f3a8be2fe8122f6b40)   74 |
| #define | [ESP\_LEDC\_HS\_SIG\_OUT3](#a0bb8f5d68a451926a18807510b22ab82)   74 |
| #define | [ESP\_PCNT\_SIG\_CH0\_IN6](#a0bbe8fe0f0d42eb511cbde58704c2c52)   75 |
| #define | [ESP\_LEDC\_HS\_SIG\_OUT4](#a6b3461968ccad6864885f9e91678e233)   75 |
| #define | [ESP\_PCNT\_SIG\_CH1\_IN6](#acb6e28da094bab3c0a86c1ec9df8b304)   76 |
| #define | [ESP\_LEDC\_HS\_SIG\_OUT5](#a8b412e40a386c2350b0f48a76304d37a)   76 |
| #define | [ESP\_PCNT\_CTRL\_CH0\_IN6](#a33b5a2894d2b4d566a9237361127cc38)   77 |
| #define | [ESP\_LEDC\_HS\_SIG\_OUT6](#a59a5b060f9a7aa2c8a2288b1db64b399)   77 |
| #define | [ESP\_PCNT\_CTRL\_CH1\_IN6](#ae345f6de908812d12034e2d0de82954c)   78 |
| #define | [ESP\_LEDC\_HS\_SIG\_OUT7](#adc3771298c3367482d6bbc51da03efed)   78 |
| #define | [ESP\_PCNT\_SIG\_CH0\_IN7](#a43b536b3cbea05abb8637bf9e3b0942d)   79 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT0](#a62dfcd88747c61acb53dc85c1751f1d3)   79 |
| #define | [ESP\_PCNT\_SIG\_CH1\_IN7](#a79fd1b052af27cc9a3c7861cee7f564d)   80 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT1](#a5cad9206cfeea93b42e5456228c7d580)   80 |
| #define | [ESP\_PCNT\_CTRL\_CH0\_IN7](#aef672312a16d80f9d72648642f301e27)   81 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT2](#ab408070e7c700805db165c3876b6c588)   81 |
| #define | [ESP\_PCNT\_CTRL\_CH1\_IN7](#a8e7561886c8adb74a97f9cf2e1bf9474)   82 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT3](#a438aee217c6c94a2962a3d98935b5717)   82 |
| #define | [ESP\_RMT\_SIG\_IN0](#ad9bae9b4884a356e465656d1ee8d61cd)   83 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT4](#ada93dcffffc15362be4b7432a8033559)   83 |
| #define | [ESP\_RMT\_SIG\_IN1](#ab6c6293e6845ba4bf4d05b84102ffdcf)   84 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT5](#a34fc029ec45756ca7064580f57db1cc7)   84 |
| #define | [ESP\_RMT\_SIG\_IN2](#af88ebdd0d2d02ac58d720c001ccc155b)   85 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT6](#a28b01adea7e0bcc8b76fe05d58c1cbd0)   85 |
| #define | [ESP\_RMT\_SIG\_IN3](#a1f930cd82690248b839f16ff7738f32c)   86 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT7](#a2ea140f2da1a15b24dcaa3592909ca35)   86 |
| #define | [ESP\_RMT\_SIG\_IN4](#abb899bebca2479d2f3da6f125ecfee6d)   87 |
| #define | [ESP\_RMT\_SIG\_OUT0](#a25343fbc20a0c542bcdc21cdfade867b)   87 |
| #define | [ESP\_RMT\_SIG\_IN5](#a714a3df55af99e8661d4954d3f15b82b)   88 |
| #define | [ESP\_RMT\_SIG\_OUT1](#a6d082fb1c7397d784a3075108e0dea73)   88 |
| #define | [ESP\_RMT\_SIG\_IN6](#adbd91079070e29944373c581f0a71648)   89 |
| #define | [ESP\_RMT\_SIG\_OUT2](#ad657c1ddcf9c335ac7876464b80b2705)   89 |
| #define | [ESP\_RMT\_SIG\_IN7](#a5ebafc69aa5f118c0cc979e61e02a275)   90 |
| #define | [ESP\_RMT\_SIG\_OUT3](#ae60033bb70ca9ff7c2b52368d24a8ab8)   90 |
| #define | [ESP\_RMT\_SIG\_OUT4](#a9c614eec345307660df0d575a388fc18)   91 |
| #define | [ESP\_RMT\_SIG\_OUT5](#a0d230c83605e61e777367c964e9adf50)   92 |
| #define | [ESP\_EXT\_ADC\_START](#ae49b4527d8fbd0f5c8e3edc72704c54a)   93 |
| #define | [ESP\_RMT\_SIG\_OUT6](#ac064d26fd0af1e07ff3e4f6a65eb96d6)   93 |
| #define | [ESP\_TWAI\_RX](#ab3da303c2f9226f9648669c17af8377a)   94 |
| #define | [ESP\_CAN\_RX](#ae677e5752545b920c4ec1a1af2ba62d7)   [ESP\_TWAI\_RX](#ab3da303c2f9226f9648669c17af8377a) |
| #define | [ESP\_RMT\_SIG\_OUT7](#acade07ae7ae28a41d56938238dbcb243)   94 |
| #define | [ESP\_I2CEXT1\_SCL\_IN](#a1b6324b294e9e018a5909427f4f0ba36)   95 |
| #define | [ESP\_I2CEXT1\_SCL\_OUT](#a3ac49ff21fcb59eeab6350821f9107e5)   95 |
| #define | [ESP\_I2CEXT1\_SDA\_IN](#abb571ec9f2a59fc281837ca8bd3f2daa)   96 |
| #define | [ESP\_I2CEXT1\_SDA\_OUT](#a3922109459dfd033147e4daf1ed4cd32)   96 |
| #define | [ESP\_HOST\_CARD\_DETECT\_N\_1](#a13ae6d0ee0d8ddf620510da5e798e891)   97 |
| #define | [ESP\_HOST\_CCMD\_OD\_PULLUP\_EN\_N](#a9f4b256b7638344a20473c7c26636dc7)   97 |
| #define | [ESP\_HOST\_CARD\_DETECT\_N\_2](#ade4729b566a4c2c832a904e25855ff6c)   98 |
| #define | [ESP\_HOST\_RST\_N\_1](#ae508559cba27c21b34bcdbdde8996205)   98 |
| #define | [ESP\_HOST\_CARD\_WRITE\_PRT\_1](#a3c789c83cee9adb9e7de20379e3e9920)   99 |
| #define | [ESP\_HOST\_RST\_N\_2](#a3c6ce500141f358b2b646250eb08cf63)   99 |
| #define | [ESP\_HOST\_CARD\_WRITE\_PRT\_2](#ab9a2b7cc8d56cf5e1b84ccc79b150777)   100 |
| #define | [ESP\_GPIO\_SD0\_OUT](#ae59035f8269ccd564ba0d7b2b078b3ee)   100 |
| #define | [ESP\_HOST\_CARD\_INT\_N\_1](#afcf037aca22111997331336e4e61b758)   101 |
| #define | [ESP\_GPIO\_SD1\_OUT](#a3fbed77581ed14fa077f314e812b9c36)   101 |
| #define | [ESP\_HOST\_CARD\_INT\_N\_2](#a2627ab7d6dfe0820ad06168d71b2c521)   102 |
| #define | [ESP\_GPIO\_SD2\_OUT](#a2668d9083ce28563cc160fe1102e927d)   102 |
| #define | [ESP\_PWM1\_SYNC0\_IN](#a9f251384f8a6a10b0fb173c4bfda88ba)   103 |
| #define | [ESP\_GPIO\_SD3\_OUT](#a9d34f616894f98d7175c41b4ba565f8d)   103 |
| #define | [ESP\_PWM1\_SYNC1\_IN](#a646d7d644b5d4ec403eab7ff793cf7b2)   104 |
| #define | [ESP\_GPIO\_SD4\_OUT](#aa88cedc2785b1e25a21ac70dd5603e68)   104 |
| #define | [ESP\_PWM1\_SYNC2\_IN](#a56a67f8e168a4e7545e3ca4bcf7c8d89)   105 |
| #define | [ESP\_GPIO\_SD5\_OUT](#af0841a01cf24e79a447daa58a48db9f8)   105 |
| #define | [ESP\_PWM1\_F0\_IN](#a09c262c332e65ccc9eb2d91d976958e3)   106 |
| #define | [ESP\_GPIO\_SD6\_OUT](#a8c16952c92f5b28cd39b99771ccb983b)   106 |
| #define | [ESP\_PWM1\_F1\_IN](#af4b1c0ff4e222f09eee18cbb85cedb67)   107 |
| #define | [ESP\_GPIO\_SD7\_OUT](#a7fd22ae53413e708e4b75ad57e1be34a)   107 |
| #define | [ESP\_PWM1\_F2\_IN](#ac911f11a68e10d359cffe49864739e2d)   108 |
| #define | [ESP\_PWM1\_OUT0A](#a4f8f7187a2a8dbf4b104e3a7e7bd5dae)   108 |
| #define | [ESP\_PWM0\_CAP0\_IN](#a421b59e20586b4f48b7e81bfa0ad4357)   109 |
| #define | [ESP\_PWM1\_OUT0B](#a553561934aa817659a5c781dfeccfc3e)   109 |
| #define | [ESP\_PWM0\_CAP1\_IN](#aea7a8712f1502df47721258470ff5b48)   110 |
| #define | [ESP\_PWM1\_OUT1A](#a852f0b23fd2c3d2f90b6bcfccd5f375e)   110 |
| #define | [ESP\_PWM0\_CAP2\_IN](#ab221240161be67a0f5af577494c8a5ad)   111 |
| #define | [ESP\_PWM1\_OUT1B](#ab9bc2ae5e0e53935f8b58380dfd397e8)   111 |
| #define | [ESP\_PWM1\_CAP0\_IN](#a8f2dcd1f46c2a5a5da3be188dca9e3a0)   112 |
| #define | [ESP\_PWM1\_OUT2A](#a8beedf183380bfe83c435f9c5920215e)   112 |
| #define | [ESP\_PWM1\_CAP1\_IN](#a8b97c639d66dcb8400aefc344bf490d1)   113 |
| #define | [ESP\_PWM1\_OUT2B](#ae1976c33c4e94a76d09ee5c3aa93f04e)   113 |
| #define | [ESP\_PWM1\_CAP2\_IN](#a23b8540974bcf9dbd5c0ff92d9b69ac9)   114 |
| #define | [ESP\_PWM2\_OUT1H](#a753b38e12b1f85b784fde4a2e5fe32dd)   114 |
| #define | [ESP\_PWM2\_FLTA](#a74f13800576db201b1fd1d7a9bb524a9)   115 |
| #define | [ESP\_PWM2\_OUT1L](#a4c2fa0f40cee1cecdd005a59a425f6d6)   115 |
| #define | [ESP\_PWM2\_FLTB](#a8c099a688fb38f70e0ccb612e06b9660)   116 |
| #define | [ESP\_PWM2\_OUT2H](#ae4f80ffadc78379f72d144f2a11a0206)   116 |
| #define | [ESP\_PWM2\_CAP1\_IN](#a8579ce8c805c3c716ae2cb5f25bbe97c)   117 |
| #define | [ESP\_PWM2\_OUT2L](#a7e9a685c18803840ba071883c07f06d7)   117 |
| #define | [ESP\_PWM2\_CAP2\_IN](#a9d82c3bacb9e2b5bcf91b6e4dd0fd4da)   118 |
| #define | [ESP\_PWM2\_OUT3H](#ad88de44d7bb5029b3c1a03d3794daf00)   118 |
| #define | [ESP\_PWM2\_CAP3\_IN](#a2d35b94ffe6f71ba30df8a8310617c40)   119 |
| #define | [ESP\_PWM2\_OUT3L](#a859e4b24d8586d5da9eeab47728dd452)   119 |
| #define | [ESP\_PWM3\_FLTA](#a631090142094c0bda20be7ffb1f02a8c)   120 |
| #define | [ESP\_PWM2\_OUT4H](#ab063692b7281339c45df0073a320c42c)   120 |
| #define | [ESP\_PWM3\_FLTB](#a70c73eb9e03c8a13c421853cff0e0e23)   121 |
| #define | [ESP\_PWM2\_OUT4L](#a9fa3278b518d107120ccc4ac0921e8c0)   121 |
| #define | [ESP\_PWM3\_CAP1\_IN](#a5a55904f853eb6093af945d111c386ff)   122 |
| #define | [ESP\_PWM3\_CAP2\_IN](#a5daa89c51257d2795ba15b7cb8dce579)   123 |
| #define | [ESP\_TWAI\_TX](#a3b13bb40583aaa0f85de982509247614)   123 |
| #define | [ESP\_CAN\_TX](#a46ca3f4f0055cdf64523d8d41fcd1485)   [ESP\_TWAI\_TX](#a3b13bb40583aaa0f85de982509247614) |
| #define | [ESP\_PWM3\_CAP3\_IN](#a491b268fd8a94e272df6f8aac3c0035d)   124 |
| #define | [ESP\_TWAI\_BUS\_OFF\_ON](#a6d0d41d1ec0f6fc626861f5857684e6d)   124 |
| #define | [ESP\_CAN\_BUS\_OFF\_ON](#a11d09cd4c1511f60cc4e62fd0d08cc14)   [ESP\_TWAI\_BUS\_OFF\_ON](#a6d0d41d1ec0f6fc626861f5857684e6d) |
| #define | [ESP\_TWAI\_CLKOUT](#a1c69791269fdbb2a11f66f33eb4066be)   125 |
| #define | [ESP\_CAN\_CLKOUT](#adcdcf8cf367f5e300a0ef24e5242e24e)   [ESP\_TWAI\_CLKOUT](#a1c69791269fdbb2a11f66f33eb4066be) |
| #define | [ESP\_SPID4\_IN](#ade124a5a82af0f49b122b32d69ee8d04)   128 |
| #define | [ESP\_SPID4\_OUT](#a9bd0335c81e6828a5da77af387fbe845)   128 |
| #define | [ESP\_SPID5\_IN](#ae8fa56cbc73756ff3895a937ab1374c2)   129 |
| #define | [ESP\_SPID5\_OUT](#a61317dd1e2daf50f35240fd561180628)   129 |
| #define | [ESP\_SPID6\_IN](#a2d850da0ce491f0049b9920cde48907e)   130 |
| #define | [ESP\_SPID6\_OUT](#a918e6203f9d52d8d2606616a938faea8)   130 |
| #define | [ESP\_SPID7\_IN](#a78073d0d570a71824e00bebe4bbd97d1)   131 |
| #define | [ESP\_SPID7\_OUT](#a0802cd16128bd289444b670a827d0d31)   131 |
| #define | [ESP\_HSPID4\_IN](#a505ba36f1599fde5e0d3fb3e7fee48e8)   132 |
| #define | [ESP\_HSPID4\_OUT](#ab0b0a1c8b8853e8f0ee32520fda3e60a)   132 |
| #define | [ESP\_HSPID5\_IN](#aff173225a50d084c8a2eba896bc1d997)   133 |
| #define | [ESP\_HSPID5\_OUT](#a93e270e899394753396e1169788514fd)   133 |
| #define | [ESP\_HSPID6\_IN](#ad4f964c0362c9bfa048ea9d088bd664b)   134 |
| #define | [ESP\_HSPID6\_OUT](#acc7e51ae7ce29705de1b21fb73ce47b2)   134 |
| #define | [ESP\_HSPID7\_IN](#a900bbb4a69611c3555229ecff07d6884)   135 |
| #define | [ESP\_HSPID7\_OUT](#a3c4fef7fa93c2d8e58391867d08a76db)   135 |
| #define | [ESP\_VSPID4\_IN](#a2b113b6c0e20b45e6d6eb46e68fffc61)   136 |
| #define | [ESP\_VSPID4\_OUT](#a66a6ee40ae8cfe23fe1ebaf725dae520)   136 |
| #define | [ESP\_VSPID5\_IN](#a8b992ce66e57278426a55c8a8eb8bfb4)   137 |
| #define | [ESP\_VSPID5\_OUT](#afd44862cfff0e324ad97277f7a683f90)   137 |
| #define | [ESP\_VSPID6\_IN](#a2bc2b10d868874d9425c7e14dc9ae8ae)   138 |
| #define | [ESP\_VSPID6\_OUT](#ab715945639b250cd34d675c72b0dd3d0)   138 |
| #define | [ESP\_VSPID7\_IN](#a27c874bce841f39f8341b5b86a5f319f)   139 |
| #define | [ESP\_VSPID7\_OUT](#a6f0007738394059a68b7973b8f4c4b14)   139 |
| #define | [ESP\_I2S0I\_DATA\_IN0](#a433c8fb715a07f27d4b2bcea31b92129)   140 |
| #define | [ESP\_I2S0O\_DATA\_OUT0](#a25101d2b16ca73d9e342a77f6c2fd517)   140 |
| #define | [ESP\_I2S0I\_DATA\_IN1](#a8fdcb030022fc73f03b8b614ec031266)   141 |
| #define | [ESP\_I2S0O\_DATA\_OUT1](#ac3656eb3c8ac2d66cc4f9099d486325b)   141 |
| #define | [ESP\_I2S0I\_DATA\_IN2](#acb82a70ab66b67c43c3df4af940afd20)   142 |
| #define | [ESP\_I2S0O\_DATA\_OUT2](#a87405dd9815c0e43d3dc865aa7459cae)   142 |
| #define | [ESP\_I2S0I\_DATA\_IN3](#af5f006ccd7b9017a077cb19b7e8584a3)   143 |
| #define | [ESP\_I2S0O\_DATA\_OUT3](#ad0e3c64912151b36169741ada3f5aa0b)   143 |
| #define | [ESP\_I2S0I\_DATA\_IN4](#a580ec97414913d720035de8df140ce2e)   144 |
| #define | [ESP\_I2S0O\_DATA\_OUT4](#abeb5e69293e78ceff31a7ed908864367)   144 |
| #define | [ESP\_I2S0I\_DATA\_IN5](#a9d72aac34e99ec34569006dbe140f658)   145 |
| #define | [ESP\_I2S0O\_DATA\_OUT5](#a93af307990b79a253c9be03d0831f175)   145 |
| #define | [ESP\_I2S0I\_DATA\_IN6](#aed35437eb068e4ea079d8755928161c3)   146 |
| #define | [ESP\_I2S0O\_DATA\_OUT6](#ace1b34e6050863a54792e6ac3c965ab8)   146 |
| #define | [ESP\_I2S0I\_DATA\_IN7](#a0a04fda280abc577acf3e20d7a917cc8)   147 |
| #define | [ESP\_I2S0O\_DATA\_OUT7](#a789d483001496ba193846e90fcc70e74)   147 |
| #define | [ESP\_I2S0I\_DATA\_IN8](#ae144f14b04fff35537effc847a2a6520)   148 |
| #define | [ESP\_I2S0O\_DATA\_OUT8](#a8360e859e714712978c0108b2fd7f8b3)   148 |
| #define | [ESP\_I2S0I\_DATA\_IN9](#a54b5575c98e2b363e1cfd556421788d5)   149 |
| #define | [ESP\_I2S0O\_DATA\_OUT9](#a0f347fca42d8d9e9bbf1f46a8c05ee84)   149 |
| #define | [ESP\_I2S0I\_DATA\_IN10](#a36fd66f4834eb96ba5f1ab7560230065)   150 |
| #define | [ESP\_I2S0O\_DATA\_OUT10](#a789443eb05c68f28a9fa99ff43bd3aa4)   150 |
| #define | [ESP\_I2S0I\_DATA\_IN11](#a601911b70e67c09b0bee13be965ea023)   151 |
| #define | [ESP\_I2S0O\_DATA\_OUT11](#ac8c4f8238d7ac8d3610ad7d817b59f0c)   151 |
| #define | [ESP\_I2S0I\_DATA\_IN12](#a1d6581f56d31224a7fe2b2767c815e17)   152 |
| #define | [ESP\_I2S0O\_DATA\_OUT12](#a1817a5bb7d7c6f81189d61844c9369d8)   152 |
| #define | [ESP\_I2S0I\_DATA\_IN13](#a429e25483385ad62fb5d25e25ab16bd1)   153 |
| #define | [ESP\_I2S0O\_DATA\_OUT13](#a4315e0aa620576457d3fe5543daf8a74)   153 |
| #define | [ESP\_I2S0I\_DATA\_IN14](#ac9a9df57a89820c2eb0f3af2ca49fc71)   154 |
| #define | [ESP\_I2S0O\_DATA\_OUT14](#a60cd35bc47b224db197844526ed31562)   154 |
| #define | [ESP\_I2S0I\_DATA\_IN15](#a1c65e11dbd846847daad7fc716955e64)   155 |
| #define | [ESP\_I2S0O\_DATA\_OUT15](#a39a667893007777d45fdcf3c9df17441)   155 |
| #define | [ESP\_I2S0O\_DATA\_OUT16](#a5f6c0a7cf37eec066127d6cfc6fc8558)   156 |
| #define | [ESP\_I2S0O\_DATA\_OUT17](#aaa92d37d180f429df167101a6bcde85f)   157 |
| #define | [ESP\_I2S0O\_DATA\_OUT18](#a1f4f2d0a3535c025d6581e4232bb7fd9)   158 |
| #define | [ESP\_I2S0O\_DATA\_OUT19](#a6676ad67342db70105683dddae6259a2)   159 |
| #define | [ESP\_I2S0O\_DATA\_OUT20](#a2d1be2072be7af3e41d25928de743b6e)   160 |
| #define | [ESP\_I2S0O\_DATA\_OUT21](#a934a97b4ba3f7729b93828fbcfe31c93)   161 |
| #define | [ESP\_I2S0O\_DATA\_OUT22](#a30d03be995708ac60420d0199d8b2b67)   162 |
| #define | [ESP\_I2S0O\_DATA\_OUT23](#a4fa877e0f38365b7f18fe4cb04c865a6)   163 |
| #define | [ESP\_I2S1I\_BCK\_IN](#a537fd0715c03fd03d914d72d01191b9a)   164 |
| #define | [ESP\_I2S1I\_BCK\_OUT](#a93d4d6602af3ba29121fef124145f4a5)   164 |
| #define | [ESP\_I2S1I\_WS\_IN](#a90b7c81877f6ab8ec1af498db7b8dc0e)   165 |
| #define | [ESP\_I2S1I\_WS\_OUT](#a1ed428a9dd21d57a7311c24f192e032e)   165 |
| #define | [ESP\_I2S1I\_DATA\_IN0](#a9d1dc7d4111b61424340211e781ea69f)   166 |
| #define | [ESP\_I2S1O\_DATA\_OUT0](#ab84e1317095fb6bfa3430fe89bc224a5)   166 |
| #define | [ESP\_I2S1I\_DATA\_IN1](#ae6785d70222fdbbafd35d071d0cdb0e4)   167 |
| #define | [ESP\_I2S1O\_DATA\_OUT1](#aaa2d63ff218a8076af7f2b3660568ca8)   167 |
| #define | [ESP\_I2S1I\_DATA\_IN2](#a5da7649d7b767380f6f2f71b77cf8bba)   168 |
| #define | [ESP\_I2S1O\_DATA\_OUT2](#a784456ac7505866a951f95743eb64ad9)   168 |
| #define | [ESP\_I2S1I\_DATA\_IN3](#aa558326938553d7c2d46e517e40c5d04)   169 |
| #define | [ESP\_I2S1O\_DATA\_OUT3](#addfba96887c05f004e5269e4a4cd79cb)   169 |
| #define | [ESP\_I2S1I\_DATA\_IN4](#acab17ad09415adc40ab1e667892083f9)   170 |
| #define | [ESP\_I2S1O\_DATA\_OUT4](#ab64ac73a1315f81270960e63cb6ed03b)   170 |
| #define | [ESP\_I2S1I\_DATA\_IN5](#ae2d0876f20d0de257d5eb09a359a6505)   171 |
| #define | [ESP\_I2S1O\_DATA\_OUT5](#a51f7de3b3383b7aae4dd80d823d13de9)   171 |
| #define | [ESP\_I2S1I\_DATA\_IN6](#a68f2324c96ea3232da52319d807914c6)   172 |
| #define | [ESP\_I2S1O\_DATA\_OUT6](#ac62a71c9664aa54d9ff025e4b048f1e9)   172 |
| #define | [ESP\_I2S1I\_DATA\_IN7](#a172ba0e7e04badee170f40ebe4de25f7)   173 |
| #define | [ESP\_I2S1O\_DATA\_OUT7](#ac5b206725ee940c0fb263bab1d487beb)   173 |
| #define | [ESP\_I2S1I\_DATA\_IN8](#a4618631d905b0e585889e096d33d2984)   174 |
| #define | [ESP\_I2S1O\_DATA\_OUT8](#a1c2b0a187daf4c85eecacc7ec80d5390)   174 |
| #define | [ESP\_I2S1I\_DATA\_IN9](#a1ddb0ee5a8bd7fe10c6751bd0f555b03)   175 |
| #define | [ESP\_I2S1O\_DATA\_OUT9](#aa2b8df142ed103952ef28ecaa0b29211)   175 |
| #define | [ESP\_I2S1I\_DATA\_IN10](#a7703547c6989806b67d55679bb49a4e2)   176 |
| #define | [ESP\_I2S1O\_DATA\_OUT10](#a70bd885f98e86cbb8b6f902d50a7849b)   176 |
| #define | [ESP\_I2S1I\_DATA\_IN11](#a5dca552908b449888450d37a1293bc38)   177 |
| #define | [ESP\_I2S1O\_DATA\_OUT11](#a5b8850f0017ea7fc9400451ae6ddc5c9)   177 |
| #define | [ESP\_I2S1I\_DATA\_IN12](#ae4667a8147f4134f4e7047336dd6b86e)   178 |
| #define | [ESP\_I2S1O\_DATA\_OUT12](#a9ab14a7194f76ecd2098a20c4c9a7a85)   178 |
| #define | [ESP\_I2S1I\_DATA\_IN13](#ad2144cf6647e3dbd41c6c39aa99774d7)   179 |
| #define | [ESP\_I2S1O\_DATA\_OUT13](#ae55f123f6025af96f2080d712484b123)   179 |
| #define | [ESP\_I2S1I\_DATA\_IN14](#abe0e8a8dd3b25ba528759f2d4a221648)   180 |
| #define | [ESP\_I2S1O\_DATA\_OUT14](#ae5f72a0583f4c2493fbb3f05dff3ab9a)   180 |
| #define | [ESP\_I2S1I\_DATA\_IN15](#a6efb5c5233ff10f5b78e2577d93b000a)   181 |
| #define | [ESP\_I2S1O\_DATA\_OUT15](#ab0a2dc0591a1e75f00647ac61027cfc1)   181 |
| #define | [ESP\_I2S1O\_DATA\_OUT16](#a0e93229ac648d7a3f7669cceaead3d71)   182 |
| #define | [ESP\_I2S1O\_DATA\_OUT17](#a037301cb8f5f4ced97f0ff785e870bca)   183 |
| #define | [ESP\_I2S1O\_DATA\_OUT18](#ae8f469295056b0587b126a7145fff52a)   184 |
| #define | [ESP\_I2S1O\_DATA\_OUT19](#adfe0560be76144c27c19b1b5320fdd44)   185 |
| #define | [ESP\_I2S1O\_DATA\_OUT20](#a9d4d2f91b498ccdcae739eea987c5ab2)   186 |
| #define | [ESP\_I2S1O\_DATA\_OUT21](#ab9c22dce791b02172243e7c552d5844a)   187 |
| #define | [ESP\_I2S1O\_DATA\_OUT22](#aaf29fc7404162b609acda92d435137cd)   188 |
| #define | [ESP\_I2S1O\_DATA\_OUT23](#a8f70a80284b6d28c5946ae3fe3e6e523)   189 |
| #define | [ESP\_I2S0I\_H\_SYNC](#aee6979fc359bc990dac8c49371243697)   190 |
| #define | [ESP\_PWM3\_OUT1H](#a05a84bb83d210e337787ff9c45c5cb61)   190 |
| #define | [ESP\_I2S0I\_V\_SYNC](#a99829d36ae815041479b1327a03c9f0a)   191 |
| #define | [ESP\_PWM3\_OUT1L](#aaf153ad217db09d6c01ad8819d5668e1)   191 |
| #define | [ESP\_I2S0I\_H\_ENABLE](#a933b9ae19e0f6cc02bdb202f7cd95b8c)   192 |
| #define | [ESP\_PWM3\_OUT2H](#a00bd2dcac50be50c6029d4de24a6f79e)   192 |
| #define | [ESP\_I2S1I\_H\_SYNC](#a8687f02a776a320521c90879afbf5037)   193 |
| #define | [ESP\_PWM3\_OUT2L](#a84e7640acf4ca35def262e9ea0b1a02e)   193 |
| #define | [ESP\_I2S1I\_V\_SYNC](#a4de19b242ceb33bc1e5e40444a354794)   194 |
| #define | [ESP\_PWM3\_OUT3H](#abcd90afa184c72bbc240e326701b2dc6)   194 |
| #define | [ESP\_I2S1I\_H\_ENABLE](#a9190b9d81f047f5f31fa11ea123a468e)   195 |
| #define | [ESP\_PWM3\_OUT3L](#aa792a2cc579f68ef0fff17978c02fb9d)   195 |
| #define | [ESP\_PWM3\_OUT4H](#ae01b405622ea50f62ba87d49d5fb4f82)   196 |
| #define | [ESP\_PWM3\_OUT4L](#aea0a96c204965f794806ce7c6013263b)   197 |
| #define | [ESP\_U2RXD\_IN](#abe46ead057c2b66d500ef07e8a84fe0f)   198 |
| #define | [ESP\_U2TXD\_OUT](#a20baac10eb4b76603580e1ea7065213a)   198 |
| #define | [ESP\_U2CTS\_IN](#a735a482aa723130ccb408f0fb7596a0a)   199 |
| #define | [ESP\_U2RTS\_OUT](#a174b50e35d961ded056cea3848110b20)   199 |
| #define | [ESP\_EMAC\_MDC\_I](#a4569f8cb129de440a41616beff6b938b)   200 |
| #define | [ESP\_EMAC\_MDC\_O](#a2f2df30f4a55a81215948fdea44a04a7)   200 |
| #define | [ESP\_EMAC\_MDI\_I](#a12b04715f671516d1182830f5a725c8c)   201 |
| #define | [ESP\_EMAC\_MDO\_O](#a0451fae682abbbae4403c71563a0cc13)   201 |
| #define | [ESP\_EMAC\_CRS\_I](#a7502b28e820501ef7672eb073103bbca)   202 |
| #define | [ESP\_EMAC\_CRS\_O](#a639473ccf7cb6f4fb26cd16fa091be29)   202 |
| #define | [ESP\_EMAC\_COL\_I](#af7dc8e7c55aa23adf5041c52066ba0f3)   203 |
| #define | [ESP\_EMAC\_COL\_O](#a35ee616dbcd0bad26525bbff33ffd72d)   203 |
| #define | [ESP\_PCMFSYNC\_IN](#a0ad409b608ef2a418098b4e51d0e7e9a)   204 |
| #define | [ESP\_BT\_AUDIO0\_IRQ](#afd2befcf5eb0c413c0f8447558dc4863)   204 |
| #define | [ESP\_PCMCLK\_IN](#abb4d1f28362c68cf3f1e9f1696602b03)   205 |
| #define | [ESP\_BT\_AUDIO1\_IRQ](#acfe665b9ff21a51b93819a3f123180ad)   205 |
| #define | [ESP\_PCMDIN](#ae94f8dfc2be2c0cf8863a33df76d5295)   206 |
| #define | [ESP\_BT\_AUDIO2\_IRQ](#a77ac554a2a10fc6fa77106e8af9dfc86)   206 |
| #define | [ESP\_BLE\_AUDIO0\_IRQ](#ab2e25b779a18acd66533795433291a3d)   207 |
| #define | [ESP\_BLE\_AUDIO1\_IRQ](#ab4b3d654c674536c2c63070210147372)   208 |
| #define | [ESP\_BLE\_AUDIO2\_IRQ](#a637ea6fcad7b2e5fe48cf9e3419fbed6)   209 |
| #define | [ESP\_PCMFSYNC\_OUT](#a8b79d6e15573a684058c9b933f469f09)   210 |
| #define | [ESP\_PCMCLK\_OUT](#a500651ca0d6daa86774a0f45190f8b38)   211 |
| #define | [ESP\_PCMDOUT](#ab3ecd7e5557112172c38bff3b2605e9c)   212 |
| #define | [ESP\_BLE\_AUDIO\_SYNC0\_P](#aba2aea8feedc96a0a6b3bba007df49ac)   213 |
| #define | [ESP\_BLE\_AUDIO\_SYNC1\_P](#a21e5bf1c7c33a39f11d8bf6537ed85bb)   214 |
| #define | [ESP\_BLE\_AUDIO\_SYNC2\_P](#a961f37a0b2dcb9e183331ef5684f8504)   215 |
| #define | [ESP\_ANT\_SEL0](#aec2dfb198f69d923686404a0a6330833)   216 |
| #define | [ESP\_ANT\_SEL1](#a15c080ea1e4c8e2db9f1640e9b8c4f0a)   217 |
| #define | [ESP\_ANT\_SEL2](#ae3042ff86ecc0f2e78ebe9477055e819)   218 |
| #define | [ESP\_ANT\_SEL3](#ab8e5cca4b9eb1a7bda7868ecd792c76d)   219 |
| #define | [ESP\_ANT\_SEL4](#a821cc4b81f76043b1ecb751118a2f416)   220 |
| #define | [ESP\_ANT\_SEL5](#a28a954881fd9d5f5e7ff25d715f0bcc2)   221 |
| #define | [ESP\_ANT\_SEL6](#a2122dad1966cbe214e9c82cb9a46bd8a)   222 |
| #define | [ESP\_ANT\_SEL7](#a8f9cedf15c49cee3fbac2a22df7675ec)   223 |
| #define | [ESP\_SIG\_IN\_FUNC224](#a53d8822e6079bfdfa4f1e643af0c619e)   224 |
| #define | [ESP\_SIG\_IN\_FUNC225](#a3dc693b4e8606fc6ae6a7f576f3e5253)   225 |
| #define | [ESP\_SIG\_IN\_FUNC226](#a358aff28052633bbaf7fd267c89310bc)   226 |
| #define | [ESP\_SIG\_IN\_FUNC227](#a5e67275e2c4feb45990232eb79856ae0)   227 |
| #define | [ESP\_SIG\_IN\_FUNC228](#a58c1a730743d75abbf8967ec8edc02de)   228 |
| #define | [ESP\_SIG\_GPIO\_OUT](#a645411759ffdc63f51f2cd42632d2720)   256 |
| #define | [ESP\_ADC1\_CH0](#a8f9a1d5717dc093e1412c91bdab92b9c)   0 |
| #define | [ESP\_ADC1\_CH1](#a0daf4a421144f0121e0d28ca8dc7db34)   1 |
| #define | [ESP\_ADC1\_CH2](#a546eff66d04c69c705916a9707ad5699)   2 |
| #define | [ESP\_ADC1\_CH3](#a0f4c4c9e9ef0a49d3c855c537d296bc3)   3 |
| #define | [ESP\_ADC1\_CH6](#a3b8e642cc63f034ac2751aa7c8f50b4d)   4 |
| #define | [ESP\_ADC1\_CH7](#a3e1e8a6040fbf0a3bb7931c8e7c5a179)   5 |
| #define | [ESP\_ADC2\_CH8](#abb40001800391a6683f876ccf8dc1ab9)   6 |
| #define | [ESP\_ADC2\_CH9](#a4eb0d2ce846da9ab31ff7d96251a594d)   7 |
| #define | [ESP\_DAC1\_OUT](#aae161d452532910ddb4a916eb483358b)   6 |
| #define | [ESP\_DAC2\_OUT](#a7bff6832e7ea4df4dc5f3eb29601c7e7)   7 |
| #define | [ESP\_ADC1\_CH5](#af85ff915121094c9e7b78486c54db848)   8 |
| #define | [ESP\_ADC1\_CH4](#a60e74929edc167861259227292e64307)   9 |
| #define | [ESP\_ADC2\_CH0](#a7db119623e8c8434cb3d724b0d97391c)   10 |
| #define | [ESP\_ADC2\_CH1](#a597733c1b61ad742a28be41df9edc33e)   11 |
| #define | [ESP\_ADC2\_CH2](#aebb2be056176553f0102ec5f8dbec752)   12 |
| #define | [ESP\_ADC2\_CH3](#affd91511897a0013d19b58125eb7fcfe)   13 |
| #define | [ESP\_ADC2\_CH4](#a1a85c794198f40665d339118c74cc7e2)   14 |
| #define | [ESP\_ADC2\_CH5](#a1d8b7231d9b93934d78763ac64e59a09)   15 |
| #define | [ESP\_ADC2\_CH6](#a5a4861a6b871a91cd98d8c709d55a9b5)   16 |
| #define | [ESP\_ADC2\_CH7](#a3fa5b9a5dcb7661c47e309211d35fcb8)   17 |

## Macro Definition Documentation

## [◆ ](#a8f9a1d5717dc093e1412c91bdab92b9c)ESP\_ADC1\_CH0

| #define ESP\_ADC1\_CH0   0 |
| --- |

## [◆ ](#a0daf4a421144f0121e0d28ca8dc7db34)ESP\_ADC1\_CH1

| #define ESP\_ADC1\_CH1   1 |
| --- |

## [◆ ](#a546eff66d04c69c705916a9707ad5699)ESP\_ADC1\_CH2

| #define ESP\_ADC1\_CH2   2 |
| --- |

## [◆ ](#a0f4c4c9e9ef0a49d3c855c537d296bc3)ESP\_ADC1\_CH3

| #define ESP\_ADC1\_CH3   3 |
| --- |

## [◆ ](#a60e74929edc167861259227292e64307)ESP\_ADC1\_CH4

| #define ESP\_ADC1\_CH4   9 |
| --- |

## [◆ ](#af85ff915121094c9e7b78486c54db848)ESP\_ADC1\_CH5

| #define ESP\_ADC1\_CH5   8 |
| --- |

## [◆ ](#a3b8e642cc63f034ac2751aa7c8f50b4d)ESP\_ADC1\_CH6

| #define ESP\_ADC1\_CH6   4 |
| --- |

## [◆ ](#a3e1e8a6040fbf0a3bb7931c8e7c5a179)ESP\_ADC1\_CH7

| #define ESP\_ADC1\_CH7   5 |
| --- |

## [◆ ](#a7db119623e8c8434cb3d724b0d97391c)ESP\_ADC2\_CH0

| #define ESP\_ADC2\_CH0   10 |
| --- |

## [◆ ](#a597733c1b61ad742a28be41df9edc33e)ESP\_ADC2\_CH1

| #define ESP\_ADC2\_CH1   11 |
| --- |

## [◆ ](#aebb2be056176553f0102ec5f8dbec752)ESP\_ADC2\_CH2

| #define ESP\_ADC2\_CH2   12 |
| --- |

## [◆ ](#affd91511897a0013d19b58125eb7fcfe)ESP\_ADC2\_CH3

| #define ESP\_ADC2\_CH3   13 |
| --- |

## [◆ ](#a1a85c794198f40665d339118c74cc7e2)ESP\_ADC2\_CH4

| #define ESP\_ADC2\_CH4   14 |
| --- |

## [◆ ](#a1d8b7231d9b93934d78763ac64e59a09)ESP\_ADC2\_CH5

| #define ESP\_ADC2\_CH5   15 |
| --- |

## [◆ ](#a5a4861a6b871a91cd98d8c709d55a9b5)ESP\_ADC2\_CH6

| #define ESP\_ADC2\_CH6   16 |
| --- |

## [◆ ](#a3fa5b9a5dcb7661c47e309211d35fcb8)ESP\_ADC2\_CH7

| #define ESP\_ADC2\_CH7   17 |
| --- |

## [◆ ](#abb40001800391a6683f876ccf8dc1ab9)ESP\_ADC2\_CH8

| #define ESP\_ADC2\_CH8   6 |
| --- |

## [◆ ](#a4eb0d2ce846da9ab31ff7d96251a594d)ESP\_ADC2\_CH9

| #define ESP\_ADC2\_CH9   7 |
| --- |

## [◆ ](#aec2dfb198f69d923686404a0a6330833)ESP\_ANT\_SEL0

| #define ESP\_ANT\_SEL0   216 |
| --- |

## [◆ ](#a15c080ea1e4c8e2db9f1640e9b8c4f0a)ESP\_ANT\_SEL1

| #define ESP\_ANT\_SEL1   217 |
| --- |

## [◆ ](#ae3042ff86ecc0f2e78ebe9477055e819)ESP\_ANT\_SEL2

| #define ESP\_ANT\_SEL2   218 |
| --- |

## [◆ ](#ab8e5cca4b9eb1a7bda7868ecd792c76d)ESP\_ANT\_SEL3

| #define ESP\_ANT\_SEL3   219 |
| --- |

## [◆ ](#a821cc4b81f76043b1ecb751118a2f416)ESP\_ANT\_SEL4

| #define ESP\_ANT\_SEL4   220 |
| --- |

## [◆ ](#a28a954881fd9d5f5e7ff25d715f0bcc2)ESP\_ANT\_SEL5

| #define ESP\_ANT\_SEL5   221 |
| --- |

## [◆ ](#a2122dad1966cbe214e9c82cb9a46bd8a)ESP\_ANT\_SEL6

| #define ESP\_ANT\_SEL6   222 |
| --- |

## [◆ ](#a8f9cedf15c49cee3fbac2a22df7675ec)ESP\_ANT\_SEL7

| #define ESP\_ANT\_SEL7   223 |
| --- |

## [◆ ](#a304bc90cc758f90f6675fea611ab0cfe)ESP\_BB\_DIAG0

| #define ESP\_BB\_DIAG0   41 |
| --- |

## [◆ ](#ad236bf991329914d59c194ff9003974a)ESP\_BB\_DIAG1

| #define ESP\_BB\_DIAG1   42 |
| --- |

## [◆ ](#aed67caee00b7ceaaaa33b2917aba60f2)ESP\_BB\_DIAG10

| #define ESP\_BB\_DIAG10   51 |
| --- |

## [◆ ](#aef4bb5d62b93dfc3f2834404b6945b90)ESP\_BB\_DIAG11

| #define ESP\_BB\_DIAG11   52 |
| --- |

## [◆ ](#acc6cd70ce139a5639022bec896a3ba5e)ESP\_BB\_DIAG12

| #define ESP\_BB\_DIAG12   53 |
| --- |

## [◆ ](#afa72089303bf662a4efc8c068b157f0d)ESP\_BB\_DIAG13

| #define ESP\_BB\_DIAG13   54 |
| --- |

## [◆ ](#a4ef00458e2547f7141741191b92854d8)ESP\_BB\_DIAG14

| #define ESP\_BB\_DIAG14   55 |
| --- |

## [◆ ](#aed7c06883c6a69303a341454aff409ed)ESP\_BB\_DIAG15

| #define ESP\_BB\_DIAG15   56 |
| --- |

## [◆ ](#a1acc29dd7c0517c30299e71c1a6ce7fa)ESP\_BB\_DIAG16

| #define ESP\_BB\_DIAG16   57 |
| --- |

## [◆ ](#a9abbf3178088e44d984b088f53c25ab1)ESP\_BB\_DIAG17

| #define ESP\_BB\_DIAG17   58 |
| --- |

## [◆ ](#af75798fba81841339510ecc5f94e542e)ESP\_BB\_DIAG18

| #define ESP\_BB\_DIAG18   59 |
| --- |

## [◆ ](#a4102e08a6e29f2164f5aafa109ab734b)ESP\_BB\_DIAG19

| #define ESP\_BB\_DIAG19   60 |
| --- |

## [◆ ](#a26c20261a5e2f4293b81c802a0a33b19)ESP\_BB\_DIAG2

| #define ESP\_BB\_DIAG2   43 |
| --- |

## [◆ ](#a5124ef75b703e7805bccd8c93828faae)ESP\_BB\_DIAG3

| #define ESP\_BB\_DIAG3   44 |
| --- |

## [◆ ](#aebd2c37b71d18967bd394b32c820647f)ESP\_BB\_DIAG4

| #define ESP\_BB\_DIAG4   45 |
| --- |

## [◆ ](#ace166b18a74fb8a42f876d1aa7cfb059)ESP\_BB\_DIAG5

| #define ESP\_BB\_DIAG5   46 |
| --- |

## [◆ ](#ad5685b19c170cc428cea0ee91f9155b0)ESP\_BB\_DIAG6

| #define ESP\_BB\_DIAG6   47 |
| --- |

## [◆ ](#aedf32208932dfe4471f6a5a7feb652f8)ESP\_BB\_DIAG7

| #define ESP\_BB\_DIAG7   48 |
| --- |

## [◆ ](#a126e2108473183890c6a2e148f8fd2c7)ESP\_BB\_DIAG8

| #define ESP\_BB\_DIAG8   49 |
| --- |

## [◆ ](#a75b60b1b4d53e6fca02b3a4f14ea530e)ESP\_BB\_DIAG9

| #define ESP\_BB\_DIAG9   50 |
| --- |

## [◆ ](#ab2e25b779a18acd66533795433291a3d)ESP\_BLE\_AUDIO0\_IRQ

| #define ESP\_BLE\_AUDIO0\_IRQ   207 |
| --- |

## [◆ ](#ab4b3d654c674536c2c63070210147372)ESP\_BLE\_AUDIO1\_IRQ

| #define ESP\_BLE\_AUDIO1\_IRQ   208 |
| --- |

## [◆ ](#a637ea6fcad7b2e5fe48cf9e3419fbed6)ESP\_BLE\_AUDIO2\_IRQ

| #define ESP\_BLE\_AUDIO2\_IRQ   209 |
| --- |

## [◆ ](#aba2aea8feedc96a0a6b3bba007df49ac)ESP\_BLE\_AUDIO\_SYNC0\_P

| #define ESP\_BLE\_AUDIO\_SYNC0\_P   213 |
| --- |

## [◆ ](#a21e5bf1c7c33a39f11d8bf6537ed85bb)ESP\_BLE\_AUDIO\_SYNC1\_P

| #define ESP\_BLE\_AUDIO\_SYNC1\_P   214 |
| --- |

## [◆ ](#a961f37a0b2dcb9e183331ef5684f8504)ESP\_BLE\_AUDIO\_SYNC2\_P

| #define ESP\_BLE\_AUDIO\_SYNC2\_P   215 |
| --- |

## [◆ ](#afd2befcf5eb0c413c0f8447558dc4863)ESP\_BT\_AUDIO0\_IRQ

| #define ESP\_BT\_AUDIO0\_IRQ   204 |
| --- |

## [◆ ](#acfe665b9ff21a51b93819a3f123180ad)ESP\_BT\_AUDIO1\_IRQ

| #define ESP\_BT\_AUDIO1\_IRQ   205 |
| --- |

## [◆ ](#a77ac554a2a10fc6fa77106e8af9dfc86)ESP\_BT\_AUDIO2\_IRQ

| #define ESP\_BT\_AUDIO2\_IRQ   206 |
| --- |

## [◆ ](#a11d09cd4c1511f60cc4e62fd0d08cc14)ESP\_CAN\_BUS\_OFF\_ON

| #define ESP\_CAN\_BUS\_OFF\_ON   [ESP\_TWAI\_BUS\_OFF\_ON](#a6d0d41d1ec0f6fc626861f5857684e6d) |
| --- |

## [◆ ](#adcdcf8cf367f5e300a0ef24e5242e24e)ESP\_CAN\_CLKOUT

| #define ESP\_CAN\_CLKOUT   [ESP\_TWAI\_CLKOUT](#a1c69791269fdbb2a11f66f33eb4066be) |
| --- |

## [◆ ](#ae677e5752545b920c4ec1a1af2ba62d7)ESP\_CAN\_RX

| #define ESP\_CAN\_RX   [ESP\_TWAI\_RX](#ab3da303c2f9226f9648669c17af8377a) |
| --- |

## [◆ ](#a46ca3f4f0055cdf64523d8d41fcd1485)ESP\_CAN\_TX

| #define ESP\_CAN\_TX   [ESP\_TWAI\_TX](#a3b13bb40583aaa0f85de982509247614) |
| --- |

## [◆ ](#aae161d452532910ddb4a916eb483358b)ESP\_DAC1\_OUT

| #define ESP\_DAC1\_OUT   6 |
| --- |

## [◆ ](#a7bff6832e7ea4df4dc5f3eb29601c7e7)ESP\_DAC2\_OUT

| #define ESP\_DAC2\_OUT   7 |
| --- |

## [◆ ](#af7dc8e7c55aa23adf5041c52066ba0f3)ESP\_EMAC\_COL\_I

| #define ESP\_EMAC\_COL\_I   203 |
| --- |

## [◆ ](#a35ee616dbcd0bad26525bbff33ffd72d)ESP\_EMAC\_COL\_O

| #define ESP\_EMAC\_COL\_O   203 |
| --- |

## [◆ ](#a7502b28e820501ef7672eb073103bbca)ESP\_EMAC\_CRS\_I

| #define ESP\_EMAC\_CRS\_I   202 |
| --- |

## [◆ ](#a639473ccf7cb6f4fb26cd16fa091be29)ESP\_EMAC\_CRS\_O

| #define ESP\_EMAC\_CRS\_O   202 |
| --- |

## [◆ ](#a4569f8cb129de440a41616beff6b938b)ESP\_EMAC\_MDC\_I

| #define ESP\_EMAC\_MDC\_I   200 |
| --- |

## [◆ ](#a2f2df30f4a55a81215948fdea44a04a7)ESP\_EMAC\_MDC\_O

| #define ESP\_EMAC\_MDC\_O   200 |
| --- |

## [◆ ](#a12b04715f671516d1182830f5a725c8c)ESP\_EMAC\_MDI\_I

| #define ESP\_EMAC\_MDI\_I   201 |
| --- |

## [◆ ](#a0451fae682abbbae4403c71563a0cc13)ESP\_EMAC\_MDO\_O

| #define ESP\_EMAC\_MDO\_O   201 |
| --- |

## [◆ ](#ae49b4527d8fbd0f5c8e3edc72704c54a)ESP\_EXT\_ADC\_START

| #define ESP\_EXT\_ADC\_START   93 |
| --- |

## [◆ ](#aadedd8576af305e1d6d56c8fa6dd30bc)ESP\_EXT\_I2C\_SCL\_O

| #define ESP\_EXT\_I2C\_SCL\_O   21 |
| --- |

## [◆ ](#ae1190b3753881bd745085f76b9f6c165)ESP\_EXT\_I2C\_SDA\_I

| #define ESP\_EXT\_I2C\_SDA\_I   22 |
| --- |

## [◆ ](#a55fa3484edd1c42124fc641667004506)ESP\_EXT\_I2C\_SDA\_O

| #define ESP\_EXT\_I2C\_SDA\_O   22 |
| --- |

## [◆ ](#a47d854bfae0f88dc023613e61e6be551)ESP\_GPIO\_BT\_ACTIVE

| #define ESP\_GPIO\_BT\_ACTIVE   37 |
| --- |

## [◆ ](#ab8d0a9090c64518af59274603f035042)ESP\_GPIO\_BT\_PRIORITY

| #define ESP\_GPIO\_BT\_PRIORITY   38 |
| --- |

## [◆ ](#ae59035f8269ccd564ba0d7b2b078b3ee)ESP\_GPIO\_SD0\_OUT

| #define ESP\_GPIO\_SD0\_OUT   100 |
| --- |

## [◆ ](#a3fbed77581ed14fa077f314e812b9c36)ESP\_GPIO\_SD1\_OUT

| #define ESP\_GPIO\_SD1\_OUT   101 |
| --- |

## [◆ ](#a2668d9083ce28563cc160fe1102e927d)ESP\_GPIO\_SD2\_OUT

| #define ESP\_GPIO\_SD2\_OUT   102 |
| --- |

## [◆ ](#a9d34f616894f98d7175c41b4ba565f8d)ESP\_GPIO\_SD3\_OUT

| #define ESP\_GPIO\_SD3\_OUT   103 |
| --- |

## [◆ ](#aa88cedc2785b1e25a21ac70dd5603e68)ESP\_GPIO\_SD4\_OUT

| #define ESP\_GPIO\_SD4\_OUT   104 |
| --- |

## [◆ ](#af0841a01cf24e79a447daa58a48db9f8)ESP\_GPIO\_SD5\_OUT

| #define ESP\_GPIO\_SD5\_OUT   105 |
| --- |

## [◆ ](#a8c16952c92f5b28cd39b99771ccb983b)ESP\_GPIO\_SD6\_OUT

| #define ESP\_GPIO\_SD6\_OUT   106 |
| --- |

## [◆ ](#a7fd22ae53413e708e4b75ad57e1be34a)ESP\_GPIO\_SD7\_OUT

| #define ESP\_GPIO\_SD7\_OUT   107 |
| --- |

## [◆ ](#af675ca03172d2dcee1e19ccb5236e087)ESP\_GPIO\_WLAN\_ACTIVE

| #define ESP\_GPIO\_WLAN\_ACTIVE   40 |
| --- |

## [◆ ](#a13ae6d0ee0d8ddf620510da5e798e891)ESP\_HOST\_CARD\_DETECT\_N\_1

| #define ESP\_HOST\_CARD\_DETECT\_N\_1   97 |
| --- |

## [◆ ](#ade4729b566a4c2c832a904e25855ff6c)ESP\_HOST\_CARD\_DETECT\_N\_2

| #define ESP\_HOST\_CARD\_DETECT\_N\_2   98 |
| --- |

## [◆ ](#afcf037aca22111997331336e4e61b758)ESP\_HOST\_CARD\_INT\_N\_1

| #define ESP\_HOST\_CARD\_INT\_N\_1   101 |
| --- |

## [◆ ](#a2627ab7d6dfe0820ad06168d71b2c521)ESP\_HOST\_CARD\_INT\_N\_2

| #define ESP\_HOST\_CARD\_INT\_N\_2   102 |
| --- |

## [◆ ](#a3c789c83cee9adb9e7de20379e3e9920)ESP\_HOST\_CARD\_WRITE\_PRT\_1

| #define ESP\_HOST\_CARD\_WRITE\_PRT\_1   99 |
| --- |

## [◆ ](#ab9a2b7cc8d56cf5e1b84ccc79b150777)ESP\_HOST\_CARD\_WRITE\_PRT\_2

| #define ESP\_HOST\_CARD\_WRITE\_PRT\_2   100 |
| --- |

## [◆ ](#a9f4b256b7638344a20473c7c26636dc7)ESP\_HOST\_CCMD\_OD\_PULLUP\_EN\_N

| #define ESP\_HOST\_CCMD\_OD\_PULLUP\_EN\_N   97 |
| --- |

## [◆ ](#ae508559cba27c21b34bcdbdde8996205)ESP\_HOST\_RST\_N\_1

| #define ESP\_HOST\_RST\_N\_1   98 |
| --- |

## [◆ ](#a3c6ce500141f358b2b646250eb08cf63)ESP\_HOST\_RST\_N\_2

| #define ESP\_HOST\_RST\_N\_2   99 |
| --- |

## [◆ ](#aa214d49ff0a9292fecc67fd8746a3201)ESP\_HSPICLK\_IN

| #define ESP\_HSPICLK\_IN   8 |
| --- |

## [◆ ](#a028245349e09fe0dac8a5d16023d6884)ESP\_HSPICLK\_OUT

| #define ESP\_HSPICLK\_OUT   8 |
| --- |

## [◆ ](#a3cf30db72dad00ef614fdb2739dccfe6)ESP\_HSPICS0\_IN

| #define ESP\_HSPICS0\_IN   11 |
| --- |

## [◆ ](#a5e584dd081acca27717085cc7cf901f8)ESP\_HSPICS0\_OUT

| #define ESP\_HSPICS0\_OUT   11 |
| --- |

## [◆ ](#ae424fe3b3c2d6a48bdf3b9f72c0b3a3b)ESP\_HSPICS1\_IN

| #define ESP\_HSPICS1\_IN   61 |
| --- |

## [◆ ](#a8180ffc727af6c61530679be1a33ddb6)ESP\_HSPICS1\_OUT

| #define ESP\_HSPICS1\_OUT   61 |
| --- |

## [◆ ](#aa718d7483400f89985652d1aa6b338d7)ESP\_HSPICS2\_IN

| #define ESP\_HSPICS2\_IN   62 |
| --- |

## [◆ ](#ad5849b71710c8fa5799b230fe5f40c4c)ESP\_HSPICS2\_OUT

| #define ESP\_HSPICS2\_OUT   62 |
| --- |

## [◆ ](#a505ba36f1599fde5e0d3fb3e7fee48e8)ESP\_HSPID4\_IN

| #define ESP\_HSPID4\_IN   132 |
| --- |

## [◆ ](#ab0b0a1c8b8853e8f0ee32520fda3e60a)ESP\_HSPID4\_OUT

| #define ESP\_HSPID4\_OUT   132 |
| --- |

## [◆ ](#aff173225a50d084c8a2eba896bc1d997)ESP\_HSPID5\_IN

| #define ESP\_HSPID5\_IN   133 |
| --- |

## [◆ ](#a93e270e899394753396e1169788514fd)ESP\_HSPID5\_OUT

| #define ESP\_HSPID5\_OUT   133 |
| --- |

## [◆ ](#ad4f964c0362c9bfa048ea9d088bd664b)ESP\_HSPID6\_IN

| #define ESP\_HSPID6\_IN   134 |
| --- |

## [◆ ](#acc7e51ae7ce29705de1b21fb73ce47b2)ESP\_HSPID6\_OUT

| #define ESP\_HSPID6\_OUT   134 |
| --- |

## [◆ ](#a900bbb4a69611c3555229ecff07d6884)ESP\_HSPID7\_IN

| #define ESP\_HSPID7\_IN   135 |
| --- |

## [◆ ](#a3c4fef7fa93c2d8e58391867d08a76db)ESP\_HSPID7\_OUT

| #define ESP\_HSPID7\_OUT   135 |
| --- |

## [◆ ](#a051bfe73e21998d1401febd110a98996)ESP\_HSPID\_IN

| #define ESP\_HSPID\_IN   10 |
| --- |

## [◆ ](#ab91738160e1970f528b96c97cd71fbf4)ESP\_HSPID\_OUT

| #define ESP\_HSPID\_OUT   10 |
| --- |

## [◆ ](#a8f77392a0ce164e7b943c9cc80465b3f)ESP\_HSPIHD\_IN

| #define ESP\_HSPIHD\_IN   12 |
| --- |

## [◆ ](#aecbf07e7ff7852bf6b45dd88a65aaa70)ESP\_HSPIHD\_OUT

| #define ESP\_HSPIHD\_OUT   12 |
| --- |

## [◆ ](#ad73beba22fb7e7d4d2ddf56c0f260e96)ESP\_HSPIQ\_IN

| #define ESP\_HSPIQ\_IN   9 |
| --- |

## [◆ ](#a0a3b5b9357369087ac3b4aea4065b277)ESP\_HSPIQ\_OUT

| #define ESP\_HSPIQ\_OUT   9 |
| --- |

## [◆ ](#a34ead95b59d395722b17c73b0ce219d1)ESP\_HSPIWP\_IN

| #define ESP\_HSPIWP\_IN   13 |
| --- |

## [◆ ](#a904860708852fdec4d3e29e7cc6192f7)ESP\_HSPIWP\_OUT

| #define ESP\_HSPIWP\_OUT   13 |
| --- |

## [◆ ](#ab607ce367da34ab0f1bd7fa648273cf1)ESP\_I2CEXT0\_SCL\_IN

| #define ESP\_I2CEXT0\_SCL\_IN   29 |
| --- |

## [◆ ](#a2144cc62df795547ccf2bbe3ee4c629f)ESP\_I2CEXT0\_SCL\_OUT

| #define ESP\_I2CEXT0\_SCL\_OUT   29 |
| --- |

## [◆ ](#afa7061c87135b9dabe5c54f5f4ce16e6)ESP\_I2CEXT0\_SDA\_IN

| #define ESP\_I2CEXT0\_SDA\_IN   30 |
| --- |

## [◆ ](#aabf1378b0ad2028c36c3bb74c81d7049)ESP\_I2CEXT0\_SDA\_OUT

| #define ESP\_I2CEXT0\_SDA\_OUT   30 |
| --- |

## [◆ ](#a1b6324b294e9e018a5909427f4f0ba36)ESP\_I2CEXT1\_SCL\_IN

| #define ESP\_I2CEXT1\_SCL\_IN   95 |
| --- |

## [◆ ](#a3ac49ff21fcb59eeab6350821f9107e5)ESP\_I2CEXT1\_SCL\_OUT

| #define ESP\_I2CEXT1\_SCL\_OUT   95 |
| --- |

## [◆ ](#abb571ec9f2a59fc281837ca8bd3f2daa)ESP\_I2CEXT1\_SDA\_IN

| #define ESP\_I2CEXT1\_SDA\_IN   96 |
| --- |

## [◆ ](#a3922109459dfd033147e4daf1ed4cd32)ESP\_I2CEXT1\_SDA\_OUT

| #define ESP\_I2CEXT1\_SDA\_OUT   96 |
| --- |

## [◆ ](#a3b913756d12daf98239924b1947d4717)ESP\_I2CM\_SCL\_O

| #define ESP\_I2CM\_SCL\_O   19 |
| --- |

## [◆ ](#a367bd6cd5bfd5d5c7d751ee8e83cb74a)ESP\_I2CM\_SDA\_I

| #define ESP\_I2CM\_SDA\_I   20 |
| --- |

## [◆ ](#a92f1f15e271687d72d19f3b1028f8a9e)ESP\_I2CM\_SDA\_O

| #define ESP\_I2CM\_SDA\_O   20 |
| --- |

## [◆ ](#a67905afbcda699d20d8a05a8a66411af)ESP\_I2S0I\_BCK\_IN

| #define ESP\_I2S0I\_BCK\_IN   27 |
| --- |

## [◆ ](#abe571a9bad2c0e95049afd8e67c8d158)ESP\_I2S0I\_BCK\_OUT

| #define ESP\_I2S0I\_BCK\_OUT   27 |
| --- |

## [◆ ](#a433c8fb715a07f27d4b2bcea31b92129)ESP\_I2S0I\_DATA\_IN0

| #define ESP\_I2S0I\_DATA\_IN0   140 |
| --- |

## [◆ ](#a8fdcb030022fc73f03b8b614ec031266)ESP\_I2S0I\_DATA\_IN1

| #define ESP\_I2S0I\_DATA\_IN1   141 |
| --- |

## [◆ ](#a36fd66f4834eb96ba5f1ab7560230065)ESP\_I2S0I\_DATA\_IN10

| #define ESP\_I2S0I\_DATA\_IN10   150 |
| --- |

## [◆ ](#a601911b70e67c09b0bee13be965ea023)ESP\_I2S0I\_DATA\_IN11

| #define ESP\_I2S0I\_DATA\_IN11   151 |
| --- |

## [◆ ](#a1d6581f56d31224a7fe2b2767c815e17)ESP\_I2S0I\_DATA\_IN12

| #define ESP\_I2S0I\_DATA\_IN12   152 |
| --- |

## [◆ ](#a429e25483385ad62fb5d25e25ab16bd1)ESP\_I2S0I\_DATA\_IN13

| #define ESP\_I2S0I\_DATA\_IN13   153 |
| --- |

## [◆ ](#ac9a9df57a89820c2eb0f3af2ca49fc71)ESP\_I2S0I\_DATA\_IN14

| #define ESP\_I2S0I\_DATA\_IN14   154 |
| --- |

## [◆ ](#a1c65e11dbd846847daad7fc716955e64)ESP\_I2S0I\_DATA\_IN15

| #define ESP\_I2S0I\_DATA\_IN15   155 |
| --- |

## [◆ ](#acb82a70ab66b67c43c3df4af940afd20)ESP\_I2S0I\_DATA\_IN2

| #define ESP\_I2S0I\_DATA\_IN2   142 |
| --- |

## [◆ ](#af5f006ccd7b9017a077cb19b7e8584a3)ESP\_I2S0I\_DATA\_IN3

| #define ESP\_I2S0I\_DATA\_IN3   143 |
| --- |

## [◆ ](#a580ec97414913d720035de8df140ce2e)ESP\_I2S0I\_DATA\_IN4

| #define ESP\_I2S0I\_DATA\_IN4   144 |
| --- |

## [◆ ](#a9d72aac34e99ec34569006dbe140f658)ESP\_I2S0I\_DATA\_IN5

| #define ESP\_I2S0I\_DATA\_IN5   145 |
| --- |

## [◆ ](#aed35437eb068e4ea079d8755928161c3)ESP\_I2S0I\_DATA\_IN6

| #define ESP\_I2S0I\_DATA\_IN6   146 |
| --- |

## [◆ ](#a0a04fda280abc577acf3e20d7a917cc8)ESP\_I2S0I\_DATA\_IN7

| #define ESP\_I2S0I\_DATA\_IN7   147 |
| --- |

## [◆ ](#ae144f14b04fff35537effc847a2a6520)ESP\_I2S0I\_DATA\_IN8

| #define ESP\_I2S0I\_DATA\_IN8   148 |
| --- |

## [◆ ](#a54b5575c98e2b363e1cfd556421788d5)ESP\_I2S0I\_DATA\_IN9

| #define ESP\_I2S0I\_DATA\_IN9   149 |
| --- |

## [◆ ](#a933b9ae19e0f6cc02bdb202f7cd95b8c)ESP\_I2S0I\_H\_ENABLE

| #define ESP\_I2S0I\_H\_ENABLE   192 |
| --- |

## [◆ ](#aee6979fc359bc990dac8c49371243697)ESP\_I2S0I\_H\_SYNC

| #define ESP\_I2S0I\_H\_SYNC   190 |
| --- |

## [◆ ](#a99829d36ae815041479b1327a03c9f0a)ESP\_I2S0I\_V\_SYNC

| #define ESP\_I2S0I\_V\_SYNC   191 |
| --- |

## [◆ ](#a4236f62ac75d5f2d56f7b1cc941d7509)ESP\_I2S0I\_WS\_IN

| #define ESP\_I2S0I\_WS\_IN   28 |
| --- |

## [◆ ](#af039bdc8eec9ec95d3ed2bbebabb22cb)ESP\_I2S0I\_WS\_OUT

| #define ESP\_I2S0I\_WS\_OUT   28 |
| --- |

## [◆ ](#af0b9626d6b7cfd5b5c42a8127897d565)ESP\_I2S0O\_BCK\_IN

| #define ESP\_I2S0O\_BCK\_IN   23 |
| --- |

## [◆ ](#a2e76c532bd75a6af4790b30f58c4b8e9)ESP\_I2S0O\_BCK\_OUT

| #define ESP\_I2S0O\_BCK\_OUT   23 |
| --- |

## [◆ ](#a25101d2b16ca73d9e342a77f6c2fd517)ESP\_I2S0O\_DATA\_OUT0

| #define ESP\_I2S0O\_DATA\_OUT0   140 |
| --- |

## [◆ ](#ac3656eb3c8ac2d66cc4f9099d486325b)ESP\_I2S0O\_DATA\_OUT1

| #define ESP\_I2S0O\_DATA\_OUT1   141 |
| --- |

## [◆ ](#a789443eb05c68f28a9fa99ff43bd3aa4)ESP\_I2S0O\_DATA\_OUT10

| #define ESP\_I2S0O\_DATA\_OUT10   150 |
| --- |

## [◆ ](#ac8c4f8238d7ac8d3610ad7d817b59f0c)ESP\_I2S0O\_DATA\_OUT11

| #define ESP\_I2S0O\_DATA\_OUT11   151 |
| --- |

## [◆ ](#a1817a5bb7d7c6f81189d61844c9369d8)ESP\_I2S0O\_DATA\_OUT12

| #define ESP\_I2S0O\_DATA\_OUT12   152 |
| --- |

## [◆ ](#a4315e0aa620576457d3fe5543daf8a74)ESP\_I2S0O\_DATA\_OUT13

| #define ESP\_I2S0O\_DATA\_OUT13   153 |
| --- |

## [◆ ](#a60cd35bc47b224db197844526ed31562)ESP\_I2S0O\_DATA\_OUT14

| #define ESP\_I2S0O\_DATA\_OUT14   154 |
| --- |

## [◆ ](#a39a667893007777d45fdcf3c9df17441)ESP\_I2S0O\_DATA\_OUT15

| #define ESP\_I2S0O\_DATA\_OUT15   155 |
| --- |

## [◆ ](#a5f6c0a7cf37eec066127d6cfc6fc8558)ESP\_I2S0O\_DATA\_OUT16

| #define ESP\_I2S0O\_DATA\_OUT16   156 |
| --- |

## [◆ ](#aaa92d37d180f429df167101a6bcde85f)ESP\_I2S0O\_DATA\_OUT17

| #define ESP\_I2S0O\_DATA\_OUT17   157 |
| --- |

## [◆ ](#a1f4f2d0a3535c025d6581e4232bb7fd9)ESP\_I2S0O\_DATA\_OUT18

| #define ESP\_I2S0O\_DATA\_OUT18   158 |
| --- |

## [◆ ](#a6676ad67342db70105683dddae6259a2)ESP\_I2S0O\_DATA\_OUT19

| #define ESP\_I2S0O\_DATA\_OUT19   159 |
| --- |

## [◆ ](#a87405dd9815c0e43d3dc865aa7459cae)ESP\_I2S0O\_DATA\_OUT2

| #define ESP\_I2S0O\_DATA\_OUT2   142 |
| --- |

## [◆ ](#a2d1be2072be7af3e41d25928de743b6e)ESP\_I2S0O\_DATA\_OUT20

| #define ESP\_I2S0O\_DATA\_OUT20   160 |
| --- |

## [◆ ](#a934a97b4ba3f7729b93828fbcfe31c93)ESP\_I2S0O\_DATA\_OUT21

| #define ESP\_I2S0O\_DATA\_OUT21   161 |
| --- |

## [◆ ](#a30d03be995708ac60420d0199d8b2b67)ESP\_I2S0O\_DATA\_OUT22

| #define ESP\_I2S0O\_DATA\_OUT22   162 |
| --- |

## [◆ ](#a4fa877e0f38365b7f18fe4cb04c865a6)ESP\_I2S0O\_DATA\_OUT23

| #define ESP\_I2S0O\_DATA\_OUT23   163 |
| --- |

## [◆ ](#ad0e3c64912151b36169741ada3f5aa0b)ESP\_I2S0O\_DATA\_OUT3

| #define ESP\_I2S0O\_DATA\_OUT3   143 |
| --- |

## [◆ ](#abeb5e69293e78ceff31a7ed908864367)ESP\_I2S0O\_DATA\_OUT4

| #define ESP\_I2S0O\_DATA\_OUT4   144 |
| --- |

## [◆ ](#a93af307990b79a253c9be03d0831f175)ESP\_I2S0O\_DATA\_OUT5

| #define ESP\_I2S0O\_DATA\_OUT5   145 |
| --- |

## [◆ ](#ace1b34e6050863a54792e6ac3c965ab8)ESP\_I2S0O\_DATA\_OUT6

| #define ESP\_I2S0O\_DATA\_OUT6   146 |
| --- |

## [◆ ](#a789d483001496ba193846e90fcc70e74)ESP\_I2S0O\_DATA\_OUT7

| #define ESP\_I2S0O\_DATA\_OUT7   147 |
| --- |

## [◆ ](#a8360e859e714712978c0108b2fd7f8b3)ESP\_I2S0O\_DATA\_OUT8

| #define ESP\_I2S0O\_DATA\_OUT8   148 |
| --- |

## [◆ ](#a0f347fca42d8d9e9bbf1f46a8c05ee84)ESP\_I2S0O\_DATA\_OUT9

| #define ESP\_I2S0O\_DATA\_OUT9   149 |
| --- |

## [◆ ](#aad13d05d8d50227859d484deaaf6e34b)ESP\_I2S0O\_WS\_IN

| #define ESP\_I2S0O\_WS\_IN   25 |
| --- |

## [◆ ](#a78693c10e4ac17973e7ac12c1bdf8c97)ESP\_I2S0O\_WS\_OUT

| #define ESP\_I2S0O\_WS\_OUT   25 |
| --- |

## [◆ ](#a537fd0715c03fd03d914d72d01191b9a)ESP\_I2S1I\_BCK\_IN

| #define ESP\_I2S1I\_BCK\_IN   164 |
| --- |

## [◆ ](#a93d4d6602af3ba29121fef124145f4a5)ESP\_I2S1I\_BCK\_OUT

| #define ESP\_I2S1I\_BCK\_OUT   164 |
| --- |

## [◆ ](#a9d1dc7d4111b61424340211e781ea69f)ESP\_I2S1I\_DATA\_IN0

| #define ESP\_I2S1I\_DATA\_IN0   166 |
| --- |

## [◆ ](#ae6785d70222fdbbafd35d071d0cdb0e4)ESP\_I2S1I\_DATA\_IN1

| #define ESP\_I2S1I\_DATA\_IN1   167 |
| --- |

## [◆ ](#a7703547c6989806b67d55679bb49a4e2)ESP\_I2S1I\_DATA\_IN10

| #define ESP\_I2S1I\_DATA\_IN10   176 |
| --- |

## [◆ ](#a5dca552908b449888450d37a1293bc38)ESP\_I2S1I\_DATA\_IN11

| #define ESP\_I2S1I\_DATA\_IN11   177 |
| --- |

## [◆ ](#ae4667a8147f4134f4e7047336dd6b86e)ESP\_I2S1I\_DATA\_IN12

| #define ESP\_I2S1I\_DATA\_IN12   178 |
| --- |

## [◆ ](#ad2144cf6647e3dbd41c6c39aa99774d7)ESP\_I2S1I\_DATA\_IN13

| #define ESP\_I2S1I\_DATA\_IN13   179 |
| --- |

## [◆ ](#abe0e8a8dd3b25ba528759f2d4a221648)ESP\_I2S1I\_DATA\_IN14

| #define ESP\_I2S1I\_DATA\_IN14   180 |
| --- |

## [◆ ](#a6efb5c5233ff10f5b78e2577d93b000a)ESP\_I2S1I\_DATA\_IN15

| #define ESP\_I2S1I\_DATA\_IN15   181 |
| --- |

## [◆ ](#a5da7649d7b767380f6f2f71b77cf8bba)ESP\_I2S1I\_DATA\_IN2

| #define ESP\_I2S1I\_DATA\_IN2   168 |
| --- |

## [◆ ](#aa558326938553d7c2d46e517e40c5d04)ESP\_I2S1I\_DATA\_IN3

| #define ESP\_I2S1I\_DATA\_IN3   169 |
| --- |

## [◆ ](#acab17ad09415adc40ab1e667892083f9)ESP\_I2S1I\_DATA\_IN4

| #define ESP\_I2S1I\_DATA\_IN4   170 |
| --- |

## [◆ ](#ae2d0876f20d0de257d5eb09a359a6505)ESP\_I2S1I\_DATA\_IN5

| #define ESP\_I2S1I\_DATA\_IN5   171 |
| --- |

## [◆ ](#a68f2324c96ea3232da52319d807914c6)ESP\_I2S1I\_DATA\_IN6

| #define ESP\_I2S1I\_DATA\_IN6   172 |
| --- |

## [◆ ](#a172ba0e7e04badee170f40ebe4de25f7)ESP\_I2S1I\_DATA\_IN7

| #define ESP\_I2S1I\_DATA\_IN7   173 |
| --- |

## [◆ ](#a4618631d905b0e585889e096d33d2984)ESP\_I2S1I\_DATA\_IN8

| #define ESP\_I2S1I\_DATA\_IN8   174 |
| --- |

## [◆ ](#a1ddb0ee5a8bd7fe10c6751bd0f555b03)ESP\_I2S1I\_DATA\_IN9

| #define ESP\_I2S1I\_DATA\_IN9   175 |
| --- |

## [◆ ](#a9190b9d81f047f5f31fa11ea123a468e)ESP\_I2S1I\_H\_ENABLE

| #define ESP\_I2S1I\_H\_ENABLE   195 |
| --- |

## [◆ ](#a8687f02a776a320521c90879afbf5037)ESP\_I2S1I\_H\_SYNC

| #define ESP\_I2S1I\_H\_SYNC   193 |
| --- |

## [◆ ](#a4de19b242ceb33bc1e5e40444a354794)ESP\_I2S1I\_V\_SYNC

| #define ESP\_I2S1I\_V\_SYNC   194 |
| --- |

## [◆ ](#a90b7c81877f6ab8ec1af498db7b8dc0e)ESP\_I2S1I\_WS\_IN

| #define ESP\_I2S1I\_WS\_IN   165 |
| --- |

## [◆ ](#a1ed428a9dd21d57a7311c24f192e032e)ESP\_I2S1I\_WS\_OUT

| #define ESP\_I2S1I\_WS\_OUT   165 |
| --- |

## [◆ ](#afffede35b0effa00a9d6e1077ac4aaa2)ESP\_I2S1O\_BCK\_IN

| #define ESP\_I2S1O\_BCK\_IN   24 |
| --- |

## [◆ ](#afcd05d2cf345dcf816068b0b89ac5a72)ESP\_I2S1O\_BCK\_OUT

| #define ESP\_I2S1O\_BCK\_OUT   24 |
| --- |

## [◆ ](#ab84e1317095fb6bfa3430fe89bc224a5)ESP\_I2S1O\_DATA\_OUT0

| #define ESP\_I2S1O\_DATA\_OUT0   166 |
| --- |

## [◆ ](#aaa2d63ff218a8076af7f2b3660568ca8)ESP\_I2S1O\_DATA\_OUT1

| #define ESP\_I2S1O\_DATA\_OUT1   167 |
| --- |

## [◆ ](#a70bd885f98e86cbb8b6f902d50a7849b)ESP\_I2S1O\_DATA\_OUT10

| #define ESP\_I2S1O\_DATA\_OUT10   176 |
| --- |

## [◆ ](#a5b8850f0017ea7fc9400451ae6ddc5c9)ESP\_I2S1O\_DATA\_OUT11

| #define ESP\_I2S1O\_DATA\_OUT11   177 |
| --- |

## [◆ ](#a9ab14a7194f76ecd2098a20c4c9a7a85)ESP\_I2S1O\_DATA\_OUT12

| #define ESP\_I2S1O\_DATA\_OUT12   178 |
| --- |

## [◆ ](#ae55f123f6025af96f2080d712484b123)ESP\_I2S1O\_DATA\_OUT13

| #define ESP\_I2S1O\_DATA\_OUT13   179 |
| --- |

## [◆ ](#ae5f72a0583f4c2493fbb3f05dff3ab9a)ESP\_I2S1O\_DATA\_OUT14

| #define ESP\_I2S1O\_DATA\_OUT14   180 |
| --- |

## [◆ ](#ab0a2dc0591a1e75f00647ac61027cfc1)ESP\_I2S1O\_DATA\_OUT15

| #define ESP\_I2S1O\_DATA\_OUT15   181 |
| --- |

## [◆ ](#a0e93229ac648d7a3f7669cceaead3d71)ESP\_I2S1O\_DATA\_OUT16

| #define ESP\_I2S1O\_DATA\_OUT16   182 |
| --- |

## [◆ ](#a037301cb8f5f4ced97f0ff785e870bca)ESP\_I2S1O\_DATA\_OUT17

| #define ESP\_I2S1O\_DATA\_OUT17   183 |
| --- |

## [◆ ](#ae8f469295056b0587b126a7145fff52a)ESP\_I2S1O\_DATA\_OUT18

| #define ESP\_I2S1O\_DATA\_OUT18   184 |
| --- |

## [◆ ](#adfe0560be76144c27c19b1b5320fdd44)ESP\_I2S1O\_DATA\_OUT19

| #define ESP\_I2S1O\_DATA\_OUT19   185 |
| --- |

## [◆ ](#a784456ac7505866a951f95743eb64ad9)ESP\_I2S1O\_DATA\_OUT2

| #define ESP\_I2S1O\_DATA\_OUT2   168 |
| --- |

## [◆ ](#a9d4d2f91b498ccdcae739eea987c5ab2)ESP\_I2S1O\_DATA\_OUT20

| #define ESP\_I2S1O\_DATA\_OUT20   186 |
| --- |

## [◆ ](#ab9c22dce791b02172243e7c552d5844a)ESP\_I2S1O\_DATA\_OUT21

| #define ESP\_I2S1O\_DATA\_OUT21   187 |
| --- |

## [◆ ](#aaf29fc7404162b609acda92d435137cd)ESP\_I2S1O\_DATA\_OUT22

| #define ESP\_I2S1O\_DATA\_OUT22   188 |
| --- |

## [◆ ](#a8f70a80284b6d28c5946ae3fe3e6e523)ESP\_I2S1O\_DATA\_OUT23

| #define ESP\_I2S1O\_DATA\_OUT23   189 |
| --- |

## [◆ ](#addfba96887c05f004e5269e4a4cd79cb)ESP\_I2S1O\_DATA\_OUT3

| #define ESP\_I2S1O\_DATA\_OUT3   169 |
| --- |

## [◆ ](#ab64ac73a1315f81270960e63cb6ed03b)ESP\_I2S1O\_DATA\_OUT4

| #define ESP\_I2S1O\_DATA\_OUT4   170 |
| --- |

## [◆ ](#a51f7de3b3383b7aae4dd80d823d13de9)ESP\_I2S1O\_DATA\_OUT5

| #define ESP\_I2S1O\_DATA\_OUT5   171 |
| --- |

## [◆ ](#ac62a71c9664aa54d9ff025e4b048f1e9)ESP\_I2S1O\_DATA\_OUT6

| #define ESP\_I2S1O\_DATA\_OUT6   172 |
| --- |

## [◆ ](#ac5b206725ee940c0fb263bab1d487beb)ESP\_I2S1O\_DATA\_OUT7

| #define ESP\_I2S1O\_DATA\_OUT7   173 |
| --- |

## [◆ ](#a1c2b0a187daf4c85eecacc7ec80d5390)ESP\_I2S1O\_DATA\_OUT8

| #define ESP\_I2S1O\_DATA\_OUT8   174 |
| --- |

## [◆ ](#aa2b8df142ed103952ef28ecaa0b29211)ESP\_I2S1O\_DATA\_OUT9

| #define ESP\_I2S1O\_DATA\_OUT9   175 |
| --- |

## [◆ ](#a7ac95a35ee6001c340cddd1424f3fa5e)ESP\_I2S1O\_WS\_IN

| #define ESP\_I2S1O\_WS\_IN   26 |
| --- |

## [◆ ](#a84485bdfe1661269506f7ef1f70f4a87)ESP\_I2S1O\_WS\_OUT

| #define ESP\_I2S1O\_WS\_OUT   26 |
| --- |

## [◆ ](#a67c3c6dabfb9930fa544b339eb44b0c8)ESP\_LEDC\_HS\_SIG\_OUT0

| #define ESP\_LEDC\_HS\_SIG\_OUT0   71 |
| --- |

## [◆ ](#a6c5eb01aeacb1b28fe6db3e2b86ac82d)ESP\_LEDC\_HS\_SIG\_OUT1

| #define ESP\_LEDC\_HS\_SIG\_OUT1   72 |
| --- |

## [◆ ](#a1ae7688b4ab2ce508465491840623f85)ESP\_LEDC\_HS\_SIG\_OUT2

| #define ESP\_LEDC\_HS\_SIG\_OUT2   73 |
| --- |

## [◆ ](#a0bb8f5d68a451926a18807510b22ab82)ESP\_LEDC\_HS\_SIG\_OUT3

| #define ESP\_LEDC\_HS\_SIG\_OUT3   74 |
| --- |

## [◆ ](#a6b3461968ccad6864885f9e91678e233)ESP\_LEDC\_HS\_SIG\_OUT4

| #define ESP\_LEDC\_HS\_SIG\_OUT4   75 |
| --- |

## [◆ ](#a8b412e40a386c2350b0f48a76304d37a)ESP\_LEDC\_HS\_SIG\_OUT5

| #define ESP\_LEDC\_HS\_SIG\_OUT5   76 |
| --- |

## [◆ ](#a59a5b060f9a7aa2c8a2288b1db64b399)ESP\_LEDC\_HS\_SIG\_OUT6

| #define ESP\_LEDC\_HS\_SIG\_OUT6   77 |
| --- |

## [◆ ](#adc3771298c3367482d6bbc51da03efed)ESP\_LEDC\_HS\_SIG\_OUT7

| #define ESP\_LEDC\_HS\_SIG\_OUT7   78 |
| --- |

## [◆ ](#a62dfcd88747c61acb53dc85c1751f1d3)ESP\_LEDC\_LS\_SIG\_OUT0

| #define ESP\_LEDC\_LS\_SIG\_OUT0   79 |
| --- |

## [◆ ](#a5cad9206cfeea93b42e5456228c7d580)ESP\_LEDC\_LS\_SIG\_OUT1

| #define ESP\_LEDC\_LS\_SIG\_OUT1   80 |
| --- |

## [◆ ](#ab408070e7c700805db165c3876b6c588)ESP\_LEDC\_LS\_SIG\_OUT2

| #define ESP\_LEDC\_LS\_SIG\_OUT2   81 |
| --- |

## [◆ ](#a438aee217c6c94a2962a3d98935b5717)ESP\_LEDC\_LS\_SIG\_OUT3

| #define ESP\_LEDC\_LS\_SIG\_OUT3   82 |
| --- |

## [◆ ](#ada93dcffffc15362be4b7432a8033559)ESP\_LEDC\_LS\_SIG\_OUT4

| #define ESP\_LEDC\_LS\_SIG\_OUT4   83 |
| --- |

## [◆ ](#a34fc029ec45756ca7064580f57db1cc7)ESP\_LEDC\_LS\_SIG\_OUT5

| #define ESP\_LEDC\_LS\_SIG\_OUT5   84 |
| --- |

## [◆ ](#a28b01adea7e0bcc8b76fe05d58c1cbd0)ESP\_LEDC\_LS\_SIG\_OUT6

| #define ESP\_LEDC\_LS\_SIG\_OUT6   85 |
| --- |

## [◆ ](#a2ea140f2da1a15b24dcaa3592909ca35)ESP\_LEDC\_LS\_SIG\_OUT7

| #define ESP\_LEDC\_LS\_SIG\_OUT7   86 |
| --- |

## [◆ ](#af80260535bc3aee44c28c972a29483e0)ESP\_NOSIG

| #define ESP\_NOSIG   [ESP\_SIG\_INVAL](esp-pinctrl-common_8h.md#ae0d2e726ab8d90343e5c80e1d9b85ad8) |
| --- |

## [◆ ](#abb4d1f28362c68cf3f1e9f1696602b03)ESP\_PCMCLK\_IN

| #define ESP\_PCMCLK\_IN   205 |
| --- |

## [◆ ](#a500651ca0d6daa86774a0f45190f8b38)ESP\_PCMCLK\_OUT

| #define ESP\_PCMCLK\_OUT   211 |
| --- |

## [◆ ](#ae94f8dfc2be2c0cf8863a33df76d5295)ESP\_PCMDIN

| #define ESP\_PCMDIN   206 |
| --- |

## [◆ ](#ab3ecd7e5557112172c38bff3b2605e9c)ESP\_PCMDOUT

| #define ESP\_PCMDOUT   212 |
| --- |

## [◆ ](#a0ad409b608ef2a418098b4e51d0e7e9a)ESP\_PCMFSYNC\_IN

| #define ESP\_PCMFSYNC\_IN   204 |
| --- |

## [◆ ](#a8b79d6e15573a684058c9b933f469f09)ESP\_PCMFSYNC\_OUT

| #define ESP\_PCMFSYNC\_OUT   210 |
| --- |

## [◆ ](#a7e3c939b0b32332a35f0bead0aa4a2a6)ESP\_PCNT\_CTRL\_CH0\_IN0

| #define ESP\_PCNT\_CTRL\_CH0\_IN0   41 |
| --- |

## [◆ ](#a9ec8d490316b9f043fe5e9160a7cf7e0)ESP\_PCNT\_CTRL\_CH0\_IN1

| #define ESP\_PCNT\_CTRL\_CH0\_IN1   45 |
| --- |

## [◆ ](#a540cbfcd205911955effcc9814f9707c)ESP\_PCNT\_CTRL\_CH0\_IN2

| #define ESP\_PCNT\_CTRL\_CH0\_IN2   49 |
| --- |

## [◆ ](#a96e8bd4584ab671a1b0c3f0adb440943)ESP\_PCNT\_CTRL\_CH0\_IN3

| #define ESP\_PCNT\_CTRL\_CH0\_IN3   53 |
| --- |

## [◆ ](#ae5a4af55bcd763eab98fa85fe09c78df)ESP\_PCNT\_CTRL\_CH0\_IN4

| #define ESP\_PCNT\_CTRL\_CH0\_IN4   57 |
| --- |

## [◆ ](#aad99a4e2a52277508ba2ce89724acb7d)ESP\_PCNT\_CTRL\_CH0\_IN5

| #define ESP\_PCNT\_CTRL\_CH0\_IN5   73 |
| --- |

## [◆ ](#a33b5a2894d2b4d566a9237361127cc38)ESP\_PCNT\_CTRL\_CH0\_IN6

| #define ESP\_PCNT\_CTRL\_CH0\_IN6   77 |
| --- |

## [◆ ](#aef672312a16d80f9d72648642f301e27)ESP\_PCNT\_CTRL\_CH0\_IN7

| #define ESP\_PCNT\_CTRL\_CH0\_IN7   81 |
| --- |

## [◆ ](#a88c5eb5c7f4169ce3e7f7056b42989a7)ESP\_PCNT\_CTRL\_CH1\_IN0

| #define ESP\_PCNT\_CTRL\_CH1\_IN0   42 |
| --- |

## [◆ ](#a0bbfffdef085eb6cedc3d1232766cb38)ESP\_PCNT\_CTRL\_CH1\_IN1

| #define ESP\_PCNT\_CTRL\_CH1\_IN1   46 |
| --- |

## [◆ ](#abf6c210e19582b06e3d6c546a009ef5b)ESP\_PCNT\_CTRL\_CH1\_IN2

| #define ESP\_PCNT\_CTRL\_CH1\_IN2   50 |
| --- |

## [◆ ](#a0a926d350fc11d737b545c53b3ba1671)ESP\_PCNT\_CTRL\_CH1\_IN3

| #define ESP\_PCNT\_CTRL\_CH1\_IN3   54 |
| --- |

## [◆ ](#a0a1247ca451b38941f488721cc4df99d)ESP\_PCNT\_CTRL\_CH1\_IN4

| #define ESP\_PCNT\_CTRL\_CH1\_IN4   58 |
| --- |

## [◆ ](#a9a0fede369d254f3a8be2fe8122f6b40)ESP\_PCNT\_CTRL\_CH1\_IN5

| #define ESP\_PCNT\_CTRL\_CH1\_IN5   74 |
| --- |

## [◆ ](#ae345f6de908812d12034e2d0de82954c)ESP\_PCNT\_CTRL\_CH1\_IN6

| #define ESP\_PCNT\_CTRL\_CH1\_IN6   78 |
| --- |

## [◆ ](#a8e7561886c8adb74a97f9cf2e1bf9474)ESP\_PCNT\_CTRL\_CH1\_IN7

| #define ESP\_PCNT\_CTRL\_CH1\_IN7   82 |
| --- |

## [◆ ](#acf123456a5b9d94f370309ad39672e34)ESP\_PCNT\_SIG\_CH0\_IN0

| #define ESP\_PCNT\_SIG\_CH0\_IN0   39 |
| --- |

## [◆ ](#a99db3d1c4e07e11fc09a4024a54fcea6)ESP\_PCNT\_SIG\_CH0\_IN1

| #define ESP\_PCNT\_SIG\_CH0\_IN1   43 |
| --- |

## [◆ ](#a4f9e798a260fb6ac4c39262f20253244)ESP\_PCNT\_SIG\_CH0\_IN2

| #define ESP\_PCNT\_SIG\_CH0\_IN2   47 |
| --- |

## [◆ ](#acd8d20d89508b532a4e2749499263de3)ESP\_PCNT\_SIG\_CH0\_IN3

| #define ESP\_PCNT\_SIG\_CH0\_IN3   51 |
| --- |

## [◆ ](#a0db0b3f57cffafbd98a8ba3a17a6cbc0)ESP\_PCNT\_SIG\_CH0\_IN4

| #define ESP\_PCNT\_SIG\_CH0\_IN4   55 |
| --- |

## [◆ ](#acd9159d1c2dd971ec52a4965a41651f9)ESP\_PCNT\_SIG\_CH0\_IN5

| #define ESP\_PCNT\_SIG\_CH0\_IN5   71 |
| --- |

## [◆ ](#a0bbe8fe0f0d42eb511cbde58704c2c52)ESP\_PCNT\_SIG\_CH0\_IN6

| #define ESP\_PCNT\_SIG\_CH0\_IN6   75 |
| --- |

## [◆ ](#a43b536b3cbea05abb8637bf9e3b0942d)ESP\_PCNT\_SIG\_CH0\_IN7

| #define ESP\_PCNT\_SIG\_CH0\_IN7   79 |
| --- |

## [◆ ](#a800813b2c23f7e4bb23e032e0802a459)ESP\_PCNT\_SIG\_CH1\_IN0

| #define ESP\_PCNT\_SIG\_CH1\_IN0   40 |
| --- |

## [◆ ](#a730113779d69ca86b257060678f8cbec)ESP\_PCNT\_SIG\_CH1\_IN1

| #define ESP\_PCNT\_SIG\_CH1\_IN1   44 |
| --- |

## [◆ ](#a38365b3f9a2b49ef2714c38d00d293c5)ESP\_PCNT\_SIG\_CH1\_IN2

| #define ESP\_PCNT\_SIG\_CH1\_IN2   48 |
| --- |

## [◆ ](#ac54a606ee7096db15cdb9453b04ac72d)ESP\_PCNT\_SIG\_CH1\_IN3

| #define ESP\_PCNT\_SIG\_CH1\_IN3   52 |
| --- |

## [◆ ](#a0d17b8a68ec65a03d73119f26a6811ab)ESP\_PCNT\_SIG\_CH1\_IN4

| #define ESP\_PCNT\_SIG\_CH1\_IN4   56 |
| --- |

## [◆ ](#a2da313499920b543ac0645fd2fc15f89)ESP\_PCNT\_SIG\_CH1\_IN5

| #define ESP\_PCNT\_SIG\_CH1\_IN5   72 |
| --- |

## [◆ ](#acb6e28da094bab3c0a86c1ec9df8b304)ESP\_PCNT\_SIG\_CH1\_IN6

| #define ESP\_PCNT\_SIG\_CH1\_IN6   76 |
| --- |

## [◆ ](#a79fd1b052af27cc9a3c7861cee7f564d)ESP\_PCNT\_SIG\_CH1\_IN7

| #define ESP\_PCNT\_SIG\_CH1\_IN7   80 |
| --- |

## [◆ ](#a421b59e20586b4f48b7e81bfa0ad4357)ESP\_PWM0\_CAP0\_IN

| #define ESP\_PWM0\_CAP0\_IN   109 |
| --- |

## [◆ ](#aea7a8712f1502df47721258470ff5b48)ESP\_PWM0\_CAP1\_IN

| #define ESP\_PWM0\_CAP1\_IN   110 |
| --- |

## [◆ ](#ab221240161be67a0f5af577494c8a5ad)ESP\_PWM0\_CAP2\_IN

| #define ESP\_PWM0\_CAP2\_IN   111 |
| --- |

## [◆ ](#a4a503a957b2fd76f257534b80069caa2)ESP\_PWM0\_F0\_IN

| #define ESP\_PWM0\_F0\_IN   34 |
| --- |

## [◆ ](#af536ae867a3d8bcb7644b48c346b4b50)ESP\_PWM0\_F1\_IN

| #define ESP\_PWM0\_F1\_IN   35 |
| --- |

## [◆ ](#a83f385e6b8a99314cc641083a203322b)ESP\_PWM0\_F2\_IN

| #define ESP\_PWM0\_F2\_IN   36 |
| --- |

## [◆ ](#a9397a79a46feab488c88552013790dfc)ESP\_PWM0\_OUT0A

| #define ESP\_PWM0\_OUT0A   32 |
| --- |

## [◆ ](#acb3badfaed73f7069ea23dde375db62a)ESP\_PWM0\_OUT0B

| #define ESP\_PWM0\_OUT0B   33 |
| --- |

## [◆ ](#ae52e5bd4be5563caeb9861267e41d947)ESP\_PWM0\_OUT1A

| #define ESP\_PWM0\_OUT1A   34 |
| --- |

## [◆ ](#a9fa8e944ff2d960c141f8375c9aa0b0e)ESP\_PWM0\_OUT1B

| #define ESP\_PWM0\_OUT1B   35 |
| --- |

## [◆ ](#abf74a2a32a8c36431e2f21d6cd15a610)ESP\_PWM0\_OUT2A

| #define ESP\_PWM0\_OUT2A   36 |
| --- |

## [◆ ](#a563105deedf9f7ed6818ab9a8a8aecdc)ESP\_PWM0\_OUT2B

| #define ESP\_PWM0\_OUT2B   37 |
| --- |

## [◆ ](#a60a3fe70a1bc5ba71cb46df782901087)ESP\_PWM0\_SYNC0\_IN

| #define ESP\_PWM0\_SYNC0\_IN   31 |
| --- |

## [◆ ](#aca616afbb64ed37982624503545a5a72)ESP\_PWM0\_SYNC1\_IN

| #define ESP\_PWM0\_SYNC1\_IN   32 |
| --- |

## [◆ ](#a2017681d630abc75e7298c12b86a62ce)ESP\_PWM0\_SYNC2\_IN

| #define ESP\_PWM0\_SYNC2\_IN   33 |
| --- |

## [◆ ](#a8f2dcd1f46c2a5a5da3be188dca9e3a0)ESP\_PWM1\_CAP0\_IN

| #define ESP\_PWM1\_CAP0\_IN   112 |
| --- |

## [◆ ](#a8b97c639d66dcb8400aefc344bf490d1)ESP\_PWM1\_CAP1\_IN

| #define ESP\_PWM1\_CAP1\_IN   113 |
| --- |

## [◆ ](#a23b8540974bcf9dbd5c0ff92d9b69ac9)ESP\_PWM1\_CAP2\_IN

| #define ESP\_PWM1\_CAP2\_IN   114 |
| --- |

## [◆ ](#a09c262c332e65ccc9eb2d91d976958e3)ESP\_PWM1\_F0\_IN

| #define ESP\_PWM1\_F0\_IN   106 |
| --- |

## [◆ ](#af4b1c0ff4e222f09eee18cbb85cedb67)ESP\_PWM1\_F1\_IN

| #define ESP\_PWM1\_F1\_IN   107 |
| --- |

## [◆ ](#ac911f11a68e10d359cffe49864739e2d)ESP\_PWM1\_F2\_IN

| #define ESP\_PWM1\_F2\_IN   108 |
| --- |

## [◆ ](#a4f8f7187a2a8dbf4b104e3a7e7bd5dae)ESP\_PWM1\_OUT0A

| #define ESP\_PWM1\_OUT0A   108 |
| --- |

## [◆ ](#a553561934aa817659a5c781dfeccfc3e)ESP\_PWM1\_OUT0B

| #define ESP\_PWM1\_OUT0B   109 |
| --- |

## [◆ ](#a852f0b23fd2c3d2f90b6bcfccd5f375e)ESP\_PWM1\_OUT1A

| #define ESP\_PWM1\_OUT1A   110 |
| --- |

## [◆ ](#ab9bc2ae5e0e53935f8b58380dfd397e8)ESP\_PWM1\_OUT1B

| #define ESP\_PWM1\_OUT1B   111 |
| --- |

## [◆ ](#a8beedf183380bfe83c435f9c5920215e)ESP\_PWM1\_OUT2A

| #define ESP\_PWM1\_OUT2A   112 |
| --- |

## [◆ ](#ae1976c33c4e94a76d09ee5c3aa93f04e)ESP\_PWM1\_OUT2B

| #define ESP\_PWM1\_OUT2B   113 |
| --- |

## [◆ ](#a9f251384f8a6a10b0fb173c4bfda88ba)ESP\_PWM1\_SYNC0\_IN

| #define ESP\_PWM1\_SYNC0\_IN   103 |
| --- |

## [◆ ](#a646d7d644b5d4ec403eab7ff793cf7b2)ESP\_PWM1\_SYNC1\_IN

| #define ESP\_PWM1\_SYNC1\_IN   104 |
| --- |

## [◆ ](#a56a67f8e168a4e7545e3ca4bcf7c8d89)ESP\_PWM1\_SYNC2\_IN

| #define ESP\_PWM1\_SYNC2\_IN   105 |
| --- |

## [◆ ](#a8579ce8c805c3c716ae2cb5f25bbe97c)ESP\_PWM2\_CAP1\_IN

| #define ESP\_PWM2\_CAP1\_IN   117 |
| --- |

## [◆ ](#a9d82c3bacb9e2b5bcf91b6e4dd0fd4da)ESP\_PWM2\_CAP2\_IN

| #define ESP\_PWM2\_CAP2\_IN   118 |
| --- |

## [◆ ](#a2d35b94ffe6f71ba30df8a8310617c40)ESP\_PWM2\_CAP3\_IN

| #define ESP\_PWM2\_CAP3\_IN   119 |
| --- |

## [◆ ](#a74f13800576db201b1fd1d7a9bb524a9)ESP\_PWM2\_FLTA

| #define ESP\_PWM2\_FLTA   115 |
| --- |

## [◆ ](#a8c099a688fb38f70e0ccb612e06b9660)ESP\_PWM2\_FLTB

| #define ESP\_PWM2\_FLTB   116 |
| --- |

## [◆ ](#a753b38e12b1f85b784fde4a2e5fe32dd)ESP\_PWM2\_OUT1H

| #define ESP\_PWM2\_OUT1H   114 |
| --- |

## [◆ ](#a4c2fa0f40cee1cecdd005a59a425f6d6)ESP\_PWM2\_OUT1L

| #define ESP\_PWM2\_OUT1L   115 |
| --- |

## [◆ ](#ae4f80ffadc78379f72d144f2a11a0206)ESP\_PWM2\_OUT2H

| #define ESP\_PWM2\_OUT2H   116 |
| --- |

## [◆ ](#a7e9a685c18803840ba071883c07f06d7)ESP\_PWM2\_OUT2L

| #define ESP\_PWM2\_OUT2L   117 |
| --- |

## [◆ ](#ad88de44d7bb5029b3c1a03d3794daf00)ESP\_PWM2\_OUT3H

| #define ESP\_PWM2\_OUT3H   118 |
| --- |

## [◆ ](#a859e4b24d8586d5da9eeab47728dd452)ESP\_PWM2\_OUT3L

| #define ESP\_PWM2\_OUT3L   119 |
| --- |

## [◆ ](#ab063692b7281339c45df0073a320c42c)ESP\_PWM2\_OUT4H

| #define ESP\_PWM2\_OUT4H   120 |
| --- |

## [◆ ](#a9fa3278b518d107120ccc4ac0921e8c0)ESP\_PWM2\_OUT4L

| #define ESP\_PWM2\_OUT4L   121 |
| --- |

## [◆ ](#a5a55904f853eb6093af945d111c386ff)ESP\_PWM3\_CAP1\_IN

| #define ESP\_PWM3\_CAP1\_IN   122 |
| --- |

## [◆ ](#a5daa89c51257d2795ba15b7cb8dce579)ESP\_PWM3\_CAP2\_IN

| #define ESP\_PWM3\_CAP2\_IN   123 |
| --- |

## [◆ ](#a491b268fd8a94e272df6f8aac3c0035d)ESP\_PWM3\_CAP3\_IN

| #define ESP\_PWM3\_CAP3\_IN   124 |
| --- |

## [◆ ](#a631090142094c0bda20be7ffb1f02a8c)ESP\_PWM3\_FLTA

| #define ESP\_PWM3\_FLTA   120 |
| --- |

## [◆ ](#a70c73eb9e03c8a13c421853cff0e0e23)ESP\_PWM3\_FLTB

| #define ESP\_PWM3\_FLTB   121 |
| --- |

## [◆ ](#a05a84bb83d210e337787ff9c45c5cb61)ESP\_PWM3\_OUT1H

| #define ESP\_PWM3\_OUT1H   190 |
| --- |

## [◆ ](#aaf153ad217db09d6c01ad8819d5668e1)ESP\_PWM3\_OUT1L

| #define ESP\_PWM3\_OUT1L   191 |
| --- |

## [◆ ](#a00bd2dcac50be50c6029d4de24a6f79e)ESP\_PWM3\_OUT2H

| #define ESP\_PWM3\_OUT2H   192 |
| --- |

## [◆ ](#a84e7640acf4ca35def262e9ea0b1a02e)ESP\_PWM3\_OUT2L

| #define ESP\_PWM3\_OUT2L   193 |
| --- |

## [◆ ](#abcd90afa184c72bbc240e326701b2dc6)ESP\_PWM3\_OUT3H

| #define ESP\_PWM3\_OUT3H   194 |
| --- |

## [◆ ](#aa792a2cc579f68ef0fff17978c02fb9d)ESP\_PWM3\_OUT3L

| #define ESP\_PWM3\_OUT3L   195 |
| --- |

## [◆ ](#ae01b405622ea50f62ba87d49d5fb4f82)ESP\_PWM3\_OUT4H

| #define ESP\_PWM3\_OUT4H   196 |
| --- |

## [◆ ](#aea0a96c204965f794806ce7c6013263b)ESP\_PWM3\_OUT4L

| #define ESP\_PWM3\_OUT4L   197 |
| --- |

## [◆ ](#ad9bae9b4884a356e465656d1ee8d61cd)ESP\_RMT\_SIG\_IN0

| #define ESP\_RMT\_SIG\_IN0   83 |
| --- |

## [◆ ](#ab6c6293e6845ba4bf4d05b84102ffdcf)ESP\_RMT\_SIG\_IN1

| #define ESP\_RMT\_SIG\_IN1   84 |
| --- |

## [◆ ](#af88ebdd0d2d02ac58d720c001ccc155b)ESP\_RMT\_SIG\_IN2

| #define ESP\_RMT\_SIG\_IN2   85 |
| --- |

## [◆ ](#a1f930cd82690248b839f16ff7738f32c)ESP\_RMT\_SIG\_IN3

| #define ESP\_RMT\_SIG\_IN3   86 |
| --- |

## [◆ ](#abb899bebca2479d2f3da6f125ecfee6d)ESP\_RMT\_SIG\_IN4

| #define ESP\_RMT\_SIG\_IN4   87 |
| --- |

## [◆ ](#a714a3df55af99e8661d4954d3f15b82b)ESP\_RMT\_SIG\_IN5

| #define ESP\_RMT\_SIG\_IN5   88 |
| --- |

## [◆ ](#adbd91079070e29944373c581f0a71648)ESP\_RMT\_SIG\_IN6

| #define ESP\_RMT\_SIG\_IN6   89 |
| --- |

## [◆ ](#a5ebafc69aa5f118c0cc979e61e02a275)ESP\_RMT\_SIG\_IN7

| #define ESP\_RMT\_SIG\_IN7   90 |
| --- |

## [◆ ](#a25343fbc20a0c542bcdc21cdfade867b)ESP\_RMT\_SIG\_OUT0

| #define ESP\_RMT\_SIG\_OUT0   87 |
| --- |

## [◆ ](#a6d082fb1c7397d784a3075108e0dea73)ESP\_RMT\_SIG\_OUT1

| #define ESP\_RMT\_SIG\_OUT1   88 |
| --- |

## [◆ ](#ad657c1ddcf9c335ac7876464b80b2705)ESP\_RMT\_SIG\_OUT2

| #define ESP\_RMT\_SIG\_OUT2   89 |
| --- |

## [◆ ](#ae60033bb70ca9ff7c2b52368d24a8ab8)ESP\_RMT\_SIG\_OUT3

| #define ESP\_RMT\_SIG\_OUT3   90 |
| --- |

## [◆ ](#a9c614eec345307660df0d575a388fc18)ESP\_RMT\_SIG\_OUT4

| #define ESP\_RMT\_SIG\_OUT4   91 |
| --- |

## [◆ ](#a0d230c83605e61e777367c964e9adf50)ESP\_RMT\_SIG\_OUT5

| #define ESP\_RMT\_SIG\_OUT5   92 |
| --- |

## [◆ ](#ac064d26fd0af1e07ff3e4f6a65eb96d6)ESP\_RMT\_SIG\_OUT6

| #define ESP\_RMT\_SIG\_OUT6   93 |
| --- |

## [◆ ](#acade07ae7ae28a41d56938238dbcb243)ESP\_RMT\_SIG\_OUT7

| #define ESP\_RMT\_SIG\_OUT7   94 |
| --- |

## [◆ ](#aac3529b76d29e57ad20500c9d1da23f3)ESP\_SDIO\_TOHOST\_INT\_OUT

| #define ESP\_SDIO\_TOHOST\_INT\_OUT   31 |
| --- |

## [◆ ](#a645411759ffdc63f51f2cd42632d2720)ESP\_SIG\_GPIO\_OUT

| #define ESP\_SIG\_GPIO\_OUT   256 |
| --- |

## [◆ ](#a53d8822e6079bfdfa4f1e643af0c619e)ESP\_SIG\_IN\_FUNC224

| #define ESP\_SIG\_IN\_FUNC224   224 |
| --- |

## [◆ ](#a3dc693b4e8606fc6ae6a7f576f3e5253)ESP\_SIG\_IN\_FUNC225

| #define ESP\_SIG\_IN\_FUNC225   225 |
| --- |

## [◆ ](#a358aff28052633bbaf7fd267c89310bc)ESP\_SIG\_IN\_FUNC226

| #define ESP\_SIG\_IN\_FUNC226   226 |
| --- |

## [◆ ](#a5e67275e2c4feb45990232eb79856ae0)ESP\_SIG\_IN\_FUNC227

| #define ESP\_SIG\_IN\_FUNC227   227 |
| --- |

## [◆ ](#a58c1a730743d75abbf8967ec8edc02de)ESP\_SIG\_IN\_FUNC228

| #define ESP\_SIG\_IN\_FUNC228   228 |
| --- |

## [◆ ](#a89331a24c2b322eda2d32394ec1f08bc)ESP\_SPICLK\_IN

| #define ESP\_SPICLK\_IN   0 |
| --- |

## [◆ ](#a5f440c922a53085bb7b28f469c2a14b0)ESP\_SPICLK\_OUT

| #define ESP\_SPICLK\_OUT   0 |
| --- |

## [◆ ](#a7bf90419c18c69d0438a4d349e9cbdb2)ESP\_SPICS0\_IN

| #define ESP\_SPICS0\_IN   5 |
| --- |

## [◆ ](#a5d97c07ba0d8cda594d52310e90fa6a4)ESP\_SPICS0\_OUT

| #define ESP\_SPICS0\_OUT   5 |
| --- |

## [◆ ](#afe3e0ee1116416992306c25420ca6efa)ESP\_SPICS1\_IN

| #define ESP\_SPICS1\_IN   6 |
| --- |

## [◆ ](#aa4a67a38b97a3d466783c0617aa6a0c8)ESP\_SPICS1\_OUT

| #define ESP\_SPICS1\_OUT   6 |
| --- |

## [◆ ](#abce40937f1557fdae2dce1a96a8aab3d)ESP\_SPICS2\_IN

| #define ESP\_SPICS2\_IN   7 |
| --- |

## [◆ ](#afdb41f1d4bc9948ea4e723e6f43a9363)ESP\_SPICS2\_OUT

| #define ESP\_SPICS2\_OUT   7 |
| --- |

## [◆ ](#ade124a5a82af0f49b122b32d69ee8d04)ESP\_SPID4\_IN

| #define ESP\_SPID4\_IN   128 |
| --- |

## [◆ ](#a9bd0335c81e6828a5da77af387fbe845)ESP\_SPID4\_OUT

| #define ESP\_SPID4\_OUT   128 |
| --- |

## [◆ ](#ae8fa56cbc73756ff3895a937ab1374c2)ESP\_SPID5\_IN

| #define ESP\_SPID5\_IN   129 |
| --- |

## [◆ ](#a61317dd1e2daf50f35240fd561180628)ESP\_SPID5\_OUT

| #define ESP\_SPID5\_OUT   129 |
| --- |

## [◆ ](#a2d850da0ce491f0049b9920cde48907e)ESP\_SPID6\_IN

| #define ESP\_SPID6\_IN   130 |
| --- |

## [◆ ](#a918e6203f9d52d8d2606616a938faea8)ESP\_SPID6\_OUT

| #define ESP\_SPID6\_OUT   130 |
| --- |

## [◆ ](#a78073d0d570a71824e00bebe4bbd97d1)ESP\_SPID7\_IN

| #define ESP\_SPID7\_IN   131 |
| --- |

## [◆ ](#a0802cd16128bd289444b670a827d0d31)ESP\_SPID7\_OUT

| #define ESP\_SPID7\_OUT   131 |
| --- |

## [◆ ](#a26c603fd58dbd7526d2be3bb3e37758a)ESP\_SPID\_IN

| #define ESP\_SPID\_IN   2 |
| --- |

## [◆ ](#af81b2fc65b68ed2238ab3367a8731102)ESP\_SPID\_OUT

| #define ESP\_SPID\_OUT   2 |
| --- |

## [◆ ](#a49783f877b666aff9362cf605590b991)ESP\_SPIHD\_IN

| #define ESP\_SPIHD\_IN   3 |
| --- |

## [◆ ](#a8851b5256482790f3304efecafc13afd)ESP\_SPIHD\_OUT

| #define ESP\_SPIHD\_OUT   3 |
| --- |

## [◆ ](#aec51ff955c6be50e529affc87ec9d5cb)ESP\_SPIQ\_IN

| #define ESP\_SPIQ\_IN   1 |
| --- |

## [◆ ](#a5816deeca8853397a830a8eb251704ee)ESP\_SPIQ\_OUT

| #define ESP\_SPIQ\_OUT   1 |
| --- |

## [◆ ](#aa74adc2812d9c6bd143c679fa4d9ca8d)ESP\_SPIWP\_IN

| #define ESP\_SPIWP\_IN   4 |
| --- |

## [◆ ](#a470408f8102937dc017336e320e6147b)ESP\_SPIWP\_OUT

| #define ESP\_SPIWP\_OUT   4 |
| --- |

## [◆ ](#a6d0d41d1ec0f6fc626861f5857684e6d)ESP\_TWAI\_BUS\_OFF\_ON

| #define ESP\_TWAI\_BUS\_OFF\_ON   124 |
| --- |

## [◆ ](#a1c69791269fdbb2a11f66f33eb4066be)ESP\_TWAI\_CLKOUT

| #define ESP\_TWAI\_CLKOUT   125 |
| --- |

## [◆ ](#ab3da303c2f9226f9648669c17af8377a)ESP\_TWAI\_RX

| #define ESP\_TWAI\_RX   94 |
| --- |

## [◆ ](#a3b13bb40583aaa0f85de982509247614)ESP\_TWAI\_TX

| #define ESP\_TWAI\_TX   123 |
| --- |

## [◆ ](#a530d7a918a97cd1fff1acf2f90edd4ca)ESP\_U0CTS\_IN

| #define ESP\_U0CTS\_IN   15 |
| --- |

## [◆ ](#a53e3a4557a4eb1f7f98250abef03c02a)ESP\_U0DSR\_IN

| #define ESP\_U0DSR\_IN   16 |
| --- |

## [◆ ](#acc8716af947169c9f167bdf215c5314c)ESP\_U0DTR\_OUT

| #define ESP\_U0DTR\_OUT   16 |
| --- |

## [◆ ](#a4257bbc044af6ea3612313e3a0b7e7c9)ESP\_U0RTS\_OUT

| #define ESP\_U0RTS\_OUT   15 |
| --- |

## [◆ ](#aca502efa55ce2286dc9eba28192681fd)ESP\_U0RXD\_IN

| #define ESP\_U0RXD\_IN   14 |
| --- |

## [◆ ](#af1e58fb8e7ef86a92171eca7bb1671af)ESP\_U0TXD\_OUT

| #define ESP\_U0TXD\_OUT   14 |
| --- |

## [◆ ](#a3c005e616da21a058960d6aed79427b3)ESP\_U1CTS\_IN

| #define ESP\_U1CTS\_IN   18 |
| --- |

## [◆ ](#a8f6399745566bd5caa2020e4dcb2bb3b)ESP\_U1RTS\_OUT

| #define ESP\_U1RTS\_OUT   18 |
| --- |

## [◆ ](#a2293e0646e0ad2f76d62f76425ae6770)ESP\_U1RXD\_IN

| #define ESP\_U1RXD\_IN   17 |
| --- |

## [◆ ](#a6053b38147e28e3a7479b38e7d195136)ESP\_U1TXD\_OUT

| #define ESP\_U1TXD\_OUT   17 |
| --- |

## [◆ ](#a735a482aa723130ccb408f0fb7596a0a)ESP\_U2CTS\_IN

| #define ESP\_U2CTS\_IN   199 |
| --- |

## [◆ ](#a174b50e35d961ded056cea3848110b20)ESP\_U2RTS\_OUT

| #define ESP\_U2RTS\_OUT   199 |
| --- |

## [◆ ](#abe46ead057c2b66d500ef07e8a84fe0f)ESP\_U2RXD\_IN

| #define ESP\_U2RXD\_IN   198 |
| --- |

## [◆ ](#a20baac10eb4b76603580e1ea7065213a)ESP\_U2TXD\_OUT

| #define ESP\_U2TXD\_OUT   198 |
| --- |

## [◆ ](#ad86c783e1f7a935adc312d9a15894c9a)ESP\_VSPICLK\_IN

| #define ESP\_VSPICLK\_IN   63 |
| --- |

## [◆ ](#ada1b28a229c5f3e37a2e3d729e3f8300)ESP\_VSPICLK\_OUT

| #define ESP\_VSPICLK\_OUT   63 |
| --- |

## [◆ ](#add4fa23bc4c1d3973d0656837c352385)ESP\_VSPICS0\_IN

| #define ESP\_VSPICS0\_IN   68 |
| --- |

## [◆ ](#ac813c68db44d91d27f040722e4d49c72)ESP\_VSPICS0\_OUT

| #define ESP\_VSPICS0\_OUT   68 |
| --- |

## [◆ ](#a51ea9a0228493852dd9c38bfd91f102b)ESP\_VSPICS1\_IN

| #define ESP\_VSPICS1\_IN   69 |
| --- |

## [◆ ](#aad60ac2b393861f7366213d682e1089e)ESP\_VSPICS1\_OUT

| #define ESP\_VSPICS1\_OUT   69 |
| --- |

## [◆ ](#a10f41168ec052c1414604b15bcb59d7e)ESP\_VSPICS2\_IN

| #define ESP\_VSPICS2\_IN   70 |
| --- |

## [◆ ](#ac6aaeb62e6e1c246a7a07071b162f283)ESP\_VSPICS2\_OUT

| #define ESP\_VSPICS2\_OUT   70 |
| --- |

## [◆ ](#a2b113b6c0e20b45e6d6eb46e68fffc61)ESP\_VSPID4\_IN

| #define ESP\_VSPID4\_IN   136 |
| --- |

## [◆ ](#a66a6ee40ae8cfe23fe1ebaf725dae520)ESP\_VSPID4\_OUT

| #define ESP\_VSPID4\_OUT   136 |
| --- |

## [◆ ](#a8b992ce66e57278426a55c8a8eb8bfb4)ESP\_VSPID5\_IN

| #define ESP\_VSPID5\_IN   137 |
| --- |

## [◆ ](#afd44862cfff0e324ad97277f7a683f90)ESP\_VSPID5\_OUT

| #define ESP\_VSPID5\_OUT   137 |
| --- |

## [◆ ](#a2bc2b10d868874d9425c7e14dc9ae8ae)ESP\_VSPID6\_IN

| #define ESP\_VSPID6\_IN   138 |
| --- |

## [◆ ](#ab715945639b250cd34d675c72b0dd3d0)ESP\_VSPID6\_OUT

| #define ESP\_VSPID6\_OUT   138 |
| --- |

## [◆ ](#a27c874bce841f39f8341b5b86a5f319f)ESP\_VSPID7\_IN

| #define ESP\_VSPID7\_IN   139 |
| --- |

## [◆ ](#a6f0007738394059a68b7973b8f4c4b14)ESP\_VSPID7\_OUT

| #define ESP\_VSPID7\_OUT   139 |
| --- |

## [◆ ](#aa22893d39ca3b946c7f5a36febc44a62)ESP\_VSPID\_IN

| #define ESP\_VSPID\_IN   65 |
| --- |

## [◆ ](#a6b9b2395789e3afbfdbf9c2faaa90b84)ESP\_VSPID\_OUT

| #define ESP\_VSPID\_OUT   65 |
| --- |

## [◆ ](#a38c28112b8871b2f61021228961620ca)ESP\_VSPIHD\_IN

| #define ESP\_VSPIHD\_IN   66 |
| --- |

## [◆ ](#ac3b80d593bb67b9bb55be918ea1ac07c)ESP\_VSPIHD\_OUT

| #define ESP\_VSPIHD\_OUT   66 |
| --- |

## [◆ ](#a4a68acaff9e8aa24b9ef3d2b1e349c10)ESP\_VSPIQ\_IN

| #define ESP\_VSPIQ\_IN   64 |
| --- |

## [◆ ](#a9651cadb9acf4b9f436752504c113b84)ESP\_VSPIQ\_OUT

| #define ESP\_VSPIQ\_OUT   64 |
| --- |

## [◆ ](#ae2f52f231a2faa56c586fd5c6afe6fc3)ESP\_VSPIWP\_IN

| #define ESP\_VSPIWP\_IN   67 |
| --- |

## [◆ ](#a69a257fe558c166843ce24c03b0347c9)ESP\_VSPIWP\_OUT

| #define ESP\_VSPIWP\_OUT   67 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [esp32-gpio-sigmap.h](esp32-gpio-sigmap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
