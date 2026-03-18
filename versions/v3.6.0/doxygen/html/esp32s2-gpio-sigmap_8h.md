---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/esp32s2-gpio-sigmap_8h.html
original_path: doxygen/html/esp32s2-gpio-sigmap_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32s2-gpio-sigmap.h File Reference

[Go to the source code of this file.](esp32s2-gpio-sigmap_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ESP\_NOSIG](#af80260535bc3aee44c28c972a29483e0)   [ESP\_SIG\_INVAL](esp-pinctrl-common_8h.md#ae0d2e726ab8d90343e5c80e1d9b85ad8) |
| #define | [ESP\_SPICLK\_OUT](#a5f440c922a53085bb7b28f469c2a14b0)   [ESP\_SPICLK\_OUT\_MUX](#aaf157f6b85a07f18b181876a7a04f142) |
| #define | [ESP\_CLK\_I2S](#a7f8cd1f168870c1cfa215fc1599ebf74)   [ESP\_CLK\_I2S\_MUX](#ae8f094f6bb8c6594dd56ac6365039f89) |
| #define | [ESP\_FSPICLK\_OUT](#ab8c5397dc530f6326c3d10b31e59e168)   [ESP\_FSPICLK\_OUT\_MUX](#a2054f4af1d18ebb83d9e3439a1b9326e) |
| #define | [ESP\_SPIQ\_IN](#aec51ff955c6be50e529affc87ec9d5cb)   0 |
| #define | [ESP\_SPIQ\_OUT](#a5816deeca8853397a830a8eb251704ee)   0 |
| #define | [ESP\_SPID\_IN](#a26c603fd58dbd7526d2be3bb3e37758a)   1 |
| #define | [ESP\_SPID\_OUT](#af81b2fc65b68ed2238ab3367a8731102)   1 |
| #define | [ESP\_SPIHD\_IN](#a49783f877b666aff9362cf605590b991)   2 |
| #define | [ESP\_SPIHD\_OUT](#a8851b5256482790f3304efecafc13afd)   2 |
| #define | [ESP\_SPIWP\_IN](#aa74adc2812d9c6bd143c679fa4d9ca8d)   3 |
| #define | [ESP\_SPIWP\_OUT](#a470408f8102937dc017336e320e6147b)   3 |
| #define | [ESP\_SPICLK\_OUT\_MUX](#aaf157f6b85a07f18b181876a7a04f142)   4 |
| #define | [ESP\_SPICS0\_OUT](#a5d97c07ba0d8cda594d52310e90fa6a4)   5 |
| #define | [ESP\_SPICS1\_OUT](#aa4a67a38b97a3d466783c0617aa6a0c8)   6 |
| #define | [ESP\_SPID4\_IN](#ade124a5a82af0f49b122b32d69ee8d04)   7 |
| #define | [ESP\_SPID4\_OUT](#a9bd0335c81e6828a5da77af387fbe845)   7 |
| #define | [ESP\_SPID5\_IN](#ae8fa56cbc73756ff3895a937ab1374c2)   8 |
| #define | [ESP\_SPID5\_OUT](#a61317dd1e2daf50f35240fd561180628)   8 |
| #define | [ESP\_SPID6\_IN](#a2d850da0ce491f0049b9920cde48907e)   9 |
| #define | [ESP\_SPID6\_OUT](#a918e6203f9d52d8d2606616a938faea8)   9 |
| #define | [ESP\_SPID7\_IN](#a78073d0d570a71824e00bebe4bbd97d1)   10 |
| #define | [ESP\_SPID7\_OUT](#a0802cd16128bd289444b670a827d0d31)   10 |
| #define | [ESP\_SPIDQS\_IN](#ae891264c3a0289dad5851d44b18707d2)   11 |
| #define | [ESP\_SPIDQS\_OUT](#a88309f7b84da7f6e461139ad137cfb97)   11 |
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
| #define | [ESP\_U1DSR\_IN](#a5f29b138691540598d0b977dc4bd5971)   21 |
| #define | [ESP\_U1DTR\_OUT](#a1f7df042d40ec6f20b559ef6778d7497)   21 |
| #define | [ESP\_I2S0O\_BCK\_IN](#af0b9626d6b7cfd5b5c42a8127897d565)   23 |
| #define | [ESP\_I2S0O\_BCK\_OUT](#a2e76c532bd75a6af4790b30f58c4b8e9)   23 |
| #define | [ESP\_I2S0O\_WS\_IN](#aad13d05d8d50227859d484deaaf6e34b)   25 |
| #define | [ESP\_I2S0O\_WS\_OUT](#a78693c10e4ac17973e7ac12c1bdf8c97)   25 |
| #define | [ESP\_I2S0I\_BCK\_IN](#a67905afbcda699d20d8a05a8a66411af)   27 |
| #define | [ESP\_I2S0I\_BCK\_OUT](#abe571a9bad2c0e95049afd8e67c8d158)   27 |
| #define | [ESP\_I2S0I\_WS\_IN](#a4236f62ac75d5f2d56f7b1cc941d7509)   28 |
| #define | [ESP\_I2S0I\_WS\_OUT](#af039bdc8eec9ec95d3ed2bbebabb22cb)   28 |
| #define | [ESP\_I2CEXT0\_SCL\_IN](#ab607ce367da34ab0f1bd7fa648273cf1)   29 |
| #define | [ESP\_I2CEXT0\_SCL\_OUT](#a2144cc62df795547ccf2bbe3ee4c629f)   29 |
| #define | [ESP\_I2CEXT0\_SDA\_IN](#afa7061c87135b9dabe5c54f5f4ce16e6)   30 |
| #define | [ESP\_I2CEXT0\_SDA\_OUT](#aabf1378b0ad2028c36c3bb74c81d7049)   30 |
| #define | [ESP\_SDIO\_TOHOST\_INT\_OUT](#aac3529b76d29e57ad20500c9d1da23f3)   31 |
| #define | [ESP\_GPIO\_BT\_ACTIVE](#a47d854bfae0f88dc023613e61e6be551)   37 |
| #define | [ESP\_GPIO\_BT\_PRIORITY](#ab8d0a9090c64518af59274603f035042)   38 |
| #define | [ESP\_PCNT\_SIG\_CH0\_IN0](#acf123456a5b9d94f370309ad39672e34)   39 |
| #define | [ESP\_GPIO\_WLAN\_PRIO](#adf2824b1611032a81fe7b3c41253c0d8)   39 |
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
| #define | [ESP\_BB\_DIAG14](#a4ef00458e2547f7141741191b92854d8)   55 |
| #define | [ESP\_BB\_DIAG15](#aed7c06883c6a69303a341454aff409ed)   56 |
| #define | [ESP\_BB\_DIAG16](#a1acc29dd7c0517c30299e71c1a6ce7fa)   57 |
| #define | [ESP\_BB\_DIAG17](#a9abbf3178088e44d984b088f53c25ab1)   58 |
| #define | [ESP\_BB\_DIAG18](#af75798fba81841339510ecc5f94e542e)   59 |
| #define | [ESP\_BB\_DIAG19](#a4102e08a6e29f2164f5aafa109ab734b)   60 |
| #define | [ESP\_USB\_EXTPHY\_VP](#a7c2bcf73d61315a0d8c71d68173f9860)   61 |
| #define | [ESP\_USB\_EXTPHY\_OEN](#a28f381128449aed0ae738516df39790c)   61 |
| #define | [ESP\_USB\_EXTPHY\_VM](#aeaa130d2e220f2ebd073983921ad3679)   62 |
| #define | [ESP\_USB\_EXTPHY\_SPEED](#aedb10271abe4c1969eefbc0425681652)   62 |
| #define | [ESP\_USB\_EXTPHY\_RCV](#a095d83d616afb08c4b06d82c4d907fee)   63 |
| #define | [ESP\_USB\_EXTPHY\_VPO](#a88c6a9f957332dac96360dd3f631e59b)   63 |
| #define | [ESP\_USB\_OTG\_IDDIG\_IN](#a22582585ff59bc29c3e011c4d869b1b8)   64 |
| #define | [ESP\_USB\_EXTPHY\_VMO](#abaeb7b2bb8208db93655b442293976aa)   64 |
| #define | [ESP\_USB\_OTG\_AVALID\_IN](#a4d0c408fedb6ba35298c1398eccaa4e2)   65 |
| #define | [ESP\_USB\_EXTPHY\_SUSPND](#a301551d0d524f785b3d0e2c35bc81ce5)   65 |
| #define | [ESP\_USB\_SRP\_BVALID\_IN](#aaafaee30be8e3fed2eb1117ce381dd37)   66 |
| #define | [ESP\_USB\_OTG\_IDPULLUP](#ab7335ddb7641fb62231adf289a7a74a8)   66 |
| #define | [ESP\_USB\_OTG\_VBUSVALID\_IN](#a4e3bd2577c74b857a74f1c367a235bad)   67 |
| #define | [ESP\_USB\_OTG\_DPPULLDOWN](#a04c49eae7bb25687d76a810ab6468353)   67 |
| #define | [ESP\_USB\_SRP\_SESSEND\_IN](#a8601c4fb546ff39782c0fbb14e68bfbd)   68 |
| #define | [ESP\_USB\_OTG\_DMPULLDOWN](#a852717f88ddb411d5b0dc49a3be83282)   68 |
| #define | [ESP\_USB\_OTG\_DRVVBUS](#a6f79de1e3bbc3758362426eecad93d3d)   69 |
| #define | [ESP\_USB\_SRP\_CHRGVBUS](#a49b28cbc76c15cd1395f3b2e1a6ac4d9)   70 |
| #define | [ESP\_USB\_SRP\_DISCHRGVBUS](#a30f3abf038b27fa16a82bdf413eff14c)   71 |
| #define | [ESP\_SPI3\_CLK\_IN](#a0bff2051090f5eaea7edd6e9b4725a3c)   72 |
| #define | [ESP\_SPI3\_CLK\_OUT\_MUX](#ad58fe98667e0bc1b79849a7a974a8157)   72 |
| #define | [ESP\_SPI3\_Q\_IN](#a05a9a2e5983b7895ca1fb05e5cd34709)   73 |
| #define | [ESP\_SPI3\_Q\_OUT](#a6656c910c99e3de854064f4df24faa2d)   73 |
| #define | [ESP\_SPI3\_D\_IN](#ae7cf1730786ba95580b91b00066d3e25)   74 |
| #define | [ESP\_SPI3\_D\_OUT](#aff4a1289beb94c9e23d7c1dd13d71d83)   74 |
| #define | [ESP\_SPI3\_HD\_IN](#a84dd16599428fb4c3da12c221219af40)   75 |
| #define | [ESP\_SPI3\_HD\_OUT](#a73457a024aa63c16c2a5ef8ada2bf8b2)   75 |
| #define | [ESP\_SPI3\_CS0\_IN](#a485eded26f1b4bd7f03d916dcd4b0753)   76 |
| #define | [ESP\_SPI3\_CS0\_OUT](#a8fc990a73f8fdc8d1004b3dad676a224)   76 |
| #define | [ESP\_SPI3\_CS1\_OUT](#a7f06d2db560a8cd511c9189cd6ed8980)   77 |
| #define | [ESP\_SPI3\_CS2\_OUT](#a9e4bf0b0eff43b1f56f17abe22ef24a5)   78 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT0](#a62dfcd88747c61acb53dc85c1751f1d3)   79 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT1](#a5cad9206cfeea93b42e5456228c7d580)   80 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT2](#ab408070e7c700805db165c3876b6c588)   81 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT3](#a438aee217c6c94a2962a3d98935b5717)   82 |
| #define | [ESP\_RMT\_SIG\_IN0](#ad9bae9b4884a356e465656d1ee8d61cd)   83 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT4](#ada93dcffffc15362be4b7432a8033559)   83 |
| #define | [ESP\_RMT\_SIG\_IN1](#ab6c6293e6845ba4bf4d05b84102ffdcf)   84 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT5](#a34fc029ec45756ca7064580f57db1cc7)   84 |
| #define | [ESP\_RMT\_SIG\_IN2](#af88ebdd0d2d02ac58d720c001ccc155b)   85 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT6](#a28b01adea7e0bcc8b76fe05d58c1cbd0)   85 |
| #define | [ESP\_RMT\_SIG\_IN3](#a1f930cd82690248b839f16ff7738f32c)   86 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT7](#a2ea140f2da1a15b24dcaa3592909ca35)   86 |
| #define | [ESP\_RMT\_SIG\_OUT0](#a25343fbc20a0c542bcdc21cdfade867b)   87 |
| #define | [ESP\_RMT\_SIG\_OUT1](#a6d082fb1c7397d784a3075108e0dea73)   88 |
| #define | [ESP\_RMT\_SIG\_OUT2](#ad657c1ddcf9c335ac7876464b80b2705)   89 |
| #define | [ESP\_RMT\_SIG\_OUT3](#ae60033bb70ca9ff7c2b52368d24a8ab8)   90 |
| #define | [ESP\_EXT\_ADC\_START](#ae49b4527d8fbd0f5c8e3edc72704c54a)   93 |
| #define | [ESP\_I2CEXT1\_SCL\_IN](#a1b6324b294e9e018a5909427f4f0ba36)   95 |
| #define | [ESP\_I2CEXT1\_SCL\_OUT](#a3ac49ff21fcb59eeab6350821f9107e5)   95 |
| #define | [ESP\_I2CEXT1\_SDA\_IN](#abb571ec9f2a59fc281837ca8bd3f2daa)   96 |
| #define | [ESP\_I2CEXT1\_SDA\_OUT](#a3922109459dfd033147e4daf1ed4cd32)   96 |
| #define | [ESP\_GPIO\_SD0\_OUT](#ae59035f8269ccd564ba0d7b2b078b3ee)   100 |
| #define | [ESP\_GPIO\_SD1\_OUT](#a3fbed77581ed14fa077f314e812b9c36)   101 |
| #define | [ESP\_GPIO\_SD2\_OUT](#a2668d9083ce28563cc160fe1102e927d)   102 |
| #define | [ESP\_GPIO\_SD3\_OUT](#a9d34f616894f98d7175c41b4ba565f8d)   103 |
| #define | [ESP\_GPIO\_SD4\_OUT](#aa88cedc2785b1e25a21ac70dd5603e68)   104 |
| #define | [ESP\_GPIO\_SD5\_OUT](#af0841a01cf24e79a447daa58a48db9f8)   105 |
| #define | [ESP\_GPIO\_SD6\_OUT](#a8c16952c92f5b28cd39b99771ccb983b)   106 |
| #define | [ESP\_GPIO\_SD7\_OUT](#a7fd22ae53413e708e4b75ad57e1be34a)   107 |
| #define | [ESP\_FSPICLK\_IN](#ade88988460c131e8c6775794588b0eb8)   108 |
| #define | [ESP\_FSPICLK\_OUT\_MUX](#a2054f4af1d18ebb83d9e3439a1b9326e)   108 |
| #define | [ESP\_FSPIQ\_IN](#ab603b7bf7d016e85653a5c3be5c01293)   109 |
| #define | [ESP\_FSPIQ\_OUT](#a8b3ea6ad374fa010b46b48072fa87ccb)   109 |
| #define | [ESP\_FSPID\_IN](#a7910521af840d42edd3c0a667cf90c5f)   110 |
| #define | [ESP\_FSPID\_OUT](#a02bd34821e8a4bf0038b9af417ec161a)   110 |
| #define | [ESP\_FSPIHD\_IN](#a60ff087a3d85a356d77f060a6698d00b)   111 |
| #define | [ESP\_FSPIHD\_OUT](#ac71bc137b93bd6c0c8a1ebe24a70a613)   111 |
| #define | [ESP\_FSPIWP\_IN](#a4d4c4a13b820cab6d94da8fe08120a2f)   112 |
| #define | [ESP\_FSPIWP\_OUT](#a83c4f18d726984cc98caeea9b7677ca1)   112 |
| #define | [ESP\_FSPIIO4\_IN](#af751015894fa1cefd780d4c483ed4fe0)   113 |
| #define | [ESP\_FSPIIO4\_OUT](#a5131d3b8c5f15927eb1ab5f5c5831fc7)   113 |
| #define | [ESP\_FSPIIO5\_IN](#aa422ee46d7a699a5de5acfce23544f1b)   114 |
| #define | [ESP\_FSPIIO5\_OUT](#a846120bb034a5178b719de7566af36e9)   114 |
| #define | [ESP\_FSPIIO6\_IN](#afbba101fa32685cf54ff6579245c232b)   115 |
| #define | [ESP\_FSPIIO6\_OUT](#acb72c9ac62375b2ef22c4895fd5c37e9)   115 |
| #define | [ESP\_FSPIIO7\_IN](#a7be0c3215d8ab00a4a87dcf4798207d9)   116 |
| #define | [ESP\_FSPIIO7\_OUT](#a796dc85ea60a5cce0d0c184805164587)   116 |
| #define | [ESP\_FSPICS0\_IN](#a96ca1328e76337d289f6e65faf33d75c)   117 |
| #define | [ESP\_FSPICS0\_OUT](#ad1be1401b282275eaef46b9a598c6a40)   117 |
| #define | [ESP\_FSPICS1\_OUT](#a44ade9179a7ea00586359a009799661d)   118 |
| #define | [ESP\_FSPICS2\_OUT](#af991963f29c5b268a5f8fead8fd15348)   119 |
| #define | [ESP\_FSPICS3\_OUT](#a65d1170c5a68ac7f6a4457c3380ddfde)   120 |
| #define | [ESP\_FSPICS4\_OUT](#a83dafe68703c701dcd07d7ff0aadad01)   121 |
| #define | [ESP\_FSPICS5\_OUT](#ad8fab64bb220fd198a6cd931f4ea1e8e)   122 |
| #define | [ESP\_TWAI\_RX](#ab3da303c2f9226f9648669c17af8377a)   123 |
| #define | [ESP\_TWAI\_TX](#a3b13bb40583aaa0f85de982509247614)   123 |
| #define | [ESP\_TWAI\_BUS\_OFF\_ON](#a6d0d41d1ec0f6fc626861f5857684e6d)   124 |
| #define | [ESP\_TWAI\_CLKOUT](#a1c69791269fdbb2a11f66f33eb4066be)   125 |
| #define | [ESP\_SUBSPICLK\_OUT\_MUX](#a0651dd050ec01b150a74bb1f8db2221f)   126 |
| #define | [ESP\_SUBSPIQ\_IN](#af80ecb5fcd6c02cb5b73478198abef3c)   127 |
| #define | [ESP\_SUBSPIQ\_OUT](#ac75fd67f54d49449451c4924c0b7910a)   127 |
| #define | [ESP\_SUBSPID\_IN](#a0c924000fccdb7ce112822db720dbd8d)   128 |
| #define | [ESP\_SUBSPID\_OUT](#a3b9cab35f71697419266c71583f8a087)   128 |
| #define | [ESP\_SUBSPIHD\_IN](#a9a04da28895e846359a3ea89391b21f6)   129 |
| #define | [ESP\_SUBSPIHD\_OUT](#ab1f7e54d6230ceabc3fee083aab409d1)   129 |
| #define | [ESP\_SUBSPIWP\_IN](#a3c4b2938ef6753d76a752bf9a973de52)   130 |
| #define | [ESP\_SUBSPIWP\_OUT](#a7493ab9a1f0dc10902ce412055579842)   130 |
| #define | [ESP\_SUBSPICS0\_OUT](#a8925d5f830a4bc5ca6114dc06bae3b1f)   131 |
| #define | [ESP\_SUBSPICS1\_OUT](#add0fa80736d0fe196872bb0664c433d4)   132 |
| #define | [ESP\_FSPIDQS\_OUT](#a83baa98d81f816f19e65aafb26f15a3c)   133 |
| #define | [ESP\_FSPI\_HSYNC\_OUT](#ac530545e4916a807a391986e544ecda6)   134 |
| #define | [ESP\_FSPI\_VSYNC\_OUT](#a4690fa15ab99eabd6fe2948704ad6255)   135 |
| #define | [ESP\_FSPI\_DE\_OUT](#a68a2f09aae5e8b7d7207cc5c58b031c6)   136 |
| #define | [ESP\_FSPICD\_OUT](#a4bd311f85d48eafbea4d0fd8cd877bc5)   137 |
| #define | [ESP\_SPI3\_CD\_OUT](#a4212588a91a6a9dd44499aec13f9fe7a)   139 |
| #define | [ESP\_SPI3\_DQS\_OUT](#aa9be8338dbdaecb13c5de0c38fbb12ab)   140 |
| #define | [ESP\_I2S0I\_DATA\_IN0](#a433c8fb715a07f27d4b2bcea31b92129)   143 |
| #define | [ESP\_I2S0O\_DATA\_OUT0](#a25101d2b16ca73d9e342a77f6c2fd517)   143 |
| #define | [ESP\_I2S0I\_DATA\_IN1](#a8fdcb030022fc73f03b8b614ec031266)   144 |
| #define | [ESP\_I2S0O\_DATA\_OUT1](#ac3656eb3c8ac2d66cc4f9099d486325b)   144 |
| #define | [ESP\_I2S0I\_DATA\_IN2](#acb82a70ab66b67c43c3df4af940afd20)   145 |
| #define | [ESP\_I2S0O\_DATA\_OUT2](#a87405dd9815c0e43d3dc865aa7459cae)   145 |
| #define | [ESP\_I2S0I\_DATA\_IN3](#af5f006ccd7b9017a077cb19b7e8584a3)   146 |
| #define | [ESP\_I2S0O\_DATA\_OUT3](#ad0e3c64912151b36169741ada3f5aa0b)   146 |
| #define | [ESP\_I2S0I\_DATA\_IN4](#a580ec97414913d720035de8df140ce2e)   147 |
| #define | [ESP\_I2S0O\_DATA\_OUT4](#abeb5e69293e78ceff31a7ed908864367)   147 |
| #define | [ESP\_I2S0I\_DATA\_IN5](#a9d72aac34e99ec34569006dbe140f658)   148 |
| #define | [ESP\_I2S0O\_DATA\_OUT5](#a93af307990b79a253c9be03d0831f175)   148 |
| #define | [ESP\_I2S0I\_DATA\_IN6](#aed35437eb068e4ea079d8755928161c3)   149 |
| #define | [ESP\_I2S0O\_DATA\_OUT6](#ace1b34e6050863a54792e6ac3c965ab8)   149 |
| #define | [ESP\_I2S0I\_DATA\_IN7](#a0a04fda280abc577acf3e20d7a917cc8)   150 |
| #define | [ESP\_I2S0O\_DATA\_OUT7](#a789d483001496ba193846e90fcc70e74)   150 |
| #define | [ESP\_I2S0I\_DATA\_IN8](#ae144f14b04fff35537effc847a2a6520)   151 |
| #define | [ESP\_I2S0O\_DATA\_OUT8](#a8360e859e714712978c0108b2fd7f8b3)   151 |
| #define | [ESP\_I2S0I\_DATA\_IN9](#a54b5575c98e2b363e1cfd556421788d5)   152 |
| #define | [ESP\_I2S0O\_DATA\_OUT9](#a0f347fca42d8d9e9bbf1f46a8c05ee84)   152 |
| #define | [ESP\_I2S0I\_DATA\_IN10](#a36fd66f4834eb96ba5f1ab7560230065)   153 |
| #define | [ESP\_I2S0O\_DATA\_OUT10](#a789443eb05c68f28a9fa99ff43bd3aa4)   153 |
| #define | [ESP\_I2S0I\_DATA\_IN11](#a601911b70e67c09b0bee13be965ea023)   154 |
| #define | [ESP\_I2S0O\_DATA\_OUT11](#ac8c4f8238d7ac8d3610ad7d817b59f0c)   154 |
| #define | [ESP\_I2S0I\_DATA\_IN12](#a1d6581f56d31224a7fe2b2767c815e17)   155 |
| #define | [ESP\_I2S0O\_DATA\_OUT12](#a1817a5bb7d7c6f81189d61844c9369d8)   155 |
| #define | [ESP\_I2S0I\_DATA\_IN13](#a429e25483385ad62fb5d25e25ab16bd1)   156 |
| #define | [ESP\_I2S0O\_DATA\_OUT13](#a4315e0aa620576457d3fe5543daf8a74)   156 |
| #define | [ESP\_I2S0I\_DATA\_IN14](#ac9a9df57a89820c2eb0f3af2ca49fc71)   157 |
| #define | [ESP\_I2S0O\_DATA\_OUT14](#a60cd35bc47b224db197844526ed31562)   157 |
| #define | [ESP\_I2S0I\_DATA\_IN15](#a1c65e11dbd846847daad7fc716955e64)   158 |
| #define | [ESP\_I2S0O\_DATA\_OUT15](#a39a667893007777d45fdcf3c9df17441)   158 |
| #define | [ESP\_I2S0O\_DATA\_OUT16](#a5f6c0a7cf37eec066127d6cfc6fc8558)   159 |
| #define | [ESP\_I2S0O\_DATA\_OUT17](#aaa92d37d180f429df167101a6bcde85f)   160 |
| #define | [ESP\_I2S0O\_DATA\_OUT18](#a1f4f2d0a3535c025d6581e4232bb7fd9)   161 |
| #define | [ESP\_I2S0O\_DATA\_OUT19](#a6676ad67342db70105683dddae6259a2)   162 |
| #define | [ESP\_I2S0O\_DATA\_OUT20](#a2d1be2072be7af3e41d25928de743b6e)   163 |
| #define | [ESP\_I2S0O\_DATA\_OUT21](#a934a97b4ba3f7729b93828fbcfe31c93)   164 |
| #define | [ESP\_I2S0O\_DATA\_OUT22](#a30d03be995708ac60420d0199d8b2b67)   165 |
| #define | [ESP\_I2S0O\_DATA\_OUT23](#a4fa877e0f38365b7f18fe4cb04c865a6)   166 |
| #define | [ESP\_SUBSPID4\_IN](#aae7066cb62b74cf5e8f64f84bd76ee49)   167 |
| #define | [ESP\_SUBSPID4\_OUT](#aa716d46da29da6affd5fa8851a730f3f)   167 |
| #define | [ESP\_SUBSPID5\_IN](#a051cd2450520fd4abc6f288c8577a12c)   168 |
| #define | [ESP\_SUBSPID5\_OUT](#aece7dc6fc4bca1bd73d9ba856eb0f3fe)   168 |
| #define | [ESP\_SUBSPID6\_IN](#a6d49162b17a1a7cd3f2446c6ca8192ec)   169 |
| #define | [ESP\_SUBSPID6\_OUT](#ab3e8db3219bf7aa7b2503a1fe759d60c)   169 |
| #define | [ESP\_SUBSPID7\_IN](#a34b9a22e0f55a0534199e62b1eaff5b0)   170 |
| #define | [ESP\_SUBSPID7\_OUT](#adb8c01bf2361a8b24e79cf048a7e6535)   170 |
| #define | [ESP\_SUBSPIDQS\_IN](#a6ccb6e41ab48fba76302068ee4433fb8)   171 |
| #define | [ESP\_SUBSPIDQS\_OUT](#a608345dcd6c90e4f19427bb38161501a)   171 |
| #define | [ESP\_I2S0I\_H\_SYNC](#aee6979fc359bc990dac8c49371243697)   193 |
| #define | [ESP\_I2S0I\_V\_SYNC](#a99829d36ae815041479b1327a03c9f0a)   194 |
| #define | [ESP\_I2S0I\_H\_ENABLE](#a933b9ae19e0f6cc02bdb202f7cd95b8c)   195 |
| #define | [ESP\_PCMFSYNC\_IN](#a0ad409b608ef2a418098b4e51d0e7e9a)   203 |
| #define | [ESP\_BT\_AUDIO0\_IRQ](#afd2befcf5eb0c413c0f8447558dc4863)   203 |
| #define | [ESP\_PCMCLK\_IN](#abb4d1f28362c68cf3f1e9f1696602b03)   204 |
| #define | [ESP\_BT\_AUDIO1\_IRQ](#acfe665b9ff21a51b93819a3f123180ad)   204 |
| #define | [ESP\_PCMDIN](#ae94f8dfc2be2c0cf8863a33df76d5295)   205 |
| #define | [ESP\_BT\_AUDIO2\_IRQ](#a77ac554a2a10fc6fa77106e8af9dfc86)   205 |
| #define | [ESP\_RW\_WAKEUP\_REQ](#a7abc844342f6483be73ea503d3f76d89)   206 |
| #define | [ESP\_BLE\_AUDIO0\_IRQ](#ab2e25b779a18acd66533795433291a3d)   206 |
| #define | [ESP\_BLE\_AUDIO1\_IRQ](#ab4b3d654c674536c2c63070210147372)   207 |
| #define | [ESP\_BLE\_AUDIO2\_IRQ](#a637ea6fcad7b2e5fe48cf9e3419fbed6)   208 |
| #define | [ESP\_PCMFSYNC\_OUT](#a8b79d6e15573a684058c9b933f469f09)   209 |
| #define | [ESP\_PCMCLK\_OUT](#a500651ca0d6daa86774a0f45190f8b38)   210 |
| #define | [ESP\_PCMDOUT](#ab3ecd7e5557112172c38bff3b2605e9c)   211 |
| #define | [ESP\_BLE\_AUDIO\_SYNC0\_P](#aba2aea8feedc96a0a6b3bba007df49ac)   212 |
| #define | [ESP\_BLE\_AUDIO\_SYNC1\_P](#a21e5bf1c7c33a39f11d8bf6537ed85bb)   213 |
| #define | [ESP\_BLE\_AUDIO\_SYNC2\_P](#a961f37a0b2dcb9e183331ef5684f8504)   214 |
| #define | [ESP\_ANT\_SEL0](#aec2dfb198f69d923686404a0a6330833)   215 |
| #define | [ESP\_ANT\_SEL1](#a15c080ea1e4c8e2db9f1640e9b8c4f0a)   216 |
| #define | [ESP\_ANT\_SEL2](#ae3042ff86ecc0f2e78ebe9477055e819)   217 |
| #define | [ESP\_ANT\_SEL3](#ab8e5cca4b9eb1a7bda7868ecd792c76d)   218 |
| #define | [ESP\_ANT\_SEL4](#a821cc4b81f76043b1ecb751118a2f416)   219 |
| #define | [ESP\_ANT\_SEL5](#a28a954881fd9d5f5e7ff25d715f0bcc2)   220 |
| #define | [ESP\_ANT\_SEL6](#a2122dad1966cbe214e9c82cb9a46bd8a)   221 |
| #define | [ESP\_ANT\_SEL7](#a8f9cedf15c49cee3fbac2a22df7675ec)   222 |
| #define | [ESP\_SIG\_IN\_FUNC\_223](#ae2b550fa907754322b00321e32da00d7)   223 |
| #define | [ESP\_SIG\_IN\_FUNC223](#ad18e273d813830572e425c4cf4abcb38)   223 |
| #define | [ESP\_SIG\_IN\_FUNC\_224](#a5022a9e30fdcf3183a1a44bd3e44496c)   224 |
| #define | [ESP\_SIG\_IN\_FUNC224](#a53d8822e6079bfdfa4f1e643af0c619e)   224 |
| #define | [ESP\_SIG\_IN\_FUNC\_225](#a8a152884133ebca3bd1d72b4f16974bc)   225 |
| #define | [ESP\_SIG\_IN\_FUNC225](#a3dc693b4e8606fc6ae6a7f576f3e5253)   225 |
| #define | [ESP\_SIG\_IN\_FUNC\_226](#adafe9a8c93ada007bf0e33a56ecdf657)   226 |
| #define | [ESP\_SIG\_IN\_FUNC226](#a358aff28052633bbaf7fd267c89310bc)   226 |
| #define | [ESP\_SIG\_IN\_FUNC\_227](#a00bccf8191e16c8fb59632b7ba63211d)   227 |
| #define | [ESP\_SIG\_IN\_FUNC227](#a5e67275e2c4feb45990232eb79856ae0)   227 |
| #define | [ESP\_PRO\_ALONEGPIO\_IN0](#a9023b22f85edc25ab88db9f3fb025c4e)   235 |
| #define | [ESP\_PRO\_ALONEGPIO\_OUT0](#ae833440baa7073fbfb51ec80ff728ce5)   235 |
| #define | [ESP\_PRO\_ALONEGPIO\_IN1](#a5e4c12a21678930c86e15cbb6d920767)   236 |
| #define | [ESP\_PRO\_ALONEGPIO\_OUT1](#a5b3065b35c32286fe5ca8d68c033b162)   236 |
| #define | [ESP\_PRO\_ALONEGPIO\_IN2](#a8b82dbe07c785060d2190a13e1fe21ee)   237 |
| #define | [ESP\_PRO\_ALONEGPIO\_OUT2](#a287e800e3fb52dd3b6949e6d185f413c)   237 |
| #define | [ESP\_PRO\_ALONEGPIO\_IN3](#a5f8a8f6143c1552eec5862ce248ca496)   238 |
| #define | [ESP\_PRO\_ALONEGPIO\_OUT3](#a49f220c0a7cae6a580174355a80b2b56)   238 |
| #define | [ESP\_PRO\_ALONEGPIO\_IN4](#ad8ca1006a71cdd738cca02eaf9f923d6)   239 |
| #define | [ESP\_PRO\_ALONEGPIO\_OUT4](#ac1b762f9e0ad1cb60c1e16b0cf7aae0a)   239 |
| #define | [ESP\_PRO\_ALONEGPIO\_IN5](#aa1b04ac7997451778d7fdbb4f00b0114)   240 |
| #define | [ESP\_PRO\_ALONEGPIO\_OUT5](#a5f237780803395dd97bb8306a14dbc92)   240 |
| #define | [ESP\_PRO\_ALONEGPIO\_IN6](#a525900ed7a103a14105afb6ef8caca69)   241 |
| #define | [ESP\_PRO\_ALONEGPIO\_OUT6](#a4cbc6a3551e057f1d943b01c120317f4)   241 |
| #define | [ESP\_PRO\_ALONEGPIO\_IN7](#af6ebbb44bcb763355964ac39293cd1c4)   242 |
| #define | [ESP\_PRO\_ALONEGPIO\_OUT7](#a3d1993f51138a3ccf8ef913e1863f3bd)   242 |
| #define | [ESP\_CLK\_I2S\_MUX](#ae8f094f6bb8c6594dd56ac6365039f89)   251 |
| #define | [ESP\_SIG\_GPIO\_OUT](#a645411759ffdc63f51f2cd42632d2720)   256 |
| #define | [ESP\_GPIO\_MAP\_DATE](#afe5c166b887709cdd27bd37df85c45b9)   0x1904100 |

## Macro Definition Documentation

## [◆ ](#aec2dfb198f69d923686404a0a6330833)ESP\_ANT\_SEL0

| #define ESP\_ANT\_SEL0   215 |
| --- |

## [◆ ](#a15c080ea1e4c8e2db9f1640e9b8c4f0a)ESP\_ANT\_SEL1

| #define ESP\_ANT\_SEL1   216 |
| --- |

## [◆ ](#ae3042ff86ecc0f2e78ebe9477055e819)ESP\_ANT\_SEL2

| #define ESP\_ANT\_SEL2   217 |
| --- |

## [◆ ](#ab8e5cca4b9eb1a7bda7868ecd792c76d)ESP\_ANT\_SEL3

| #define ESP\_ANT\_SEL3   218 |
| --- |

## [◆ ](#a821cc4b81f76043b1ecb751118a2f416)ESP\_ANT\_SEL4

| #define ESP\_ANT\_SEL4   219 |
| --- |

## [◆ ](#a28a954881fd9d5f5e7ff25d715f0bcc2)ESP\_ANT\_SEL5

| #define ESP\_ANT\_SEL5   220 |
| --- |

## [◆ ](#a2122dad1966cbe214e9c82cb9a46bd8a)ESP\_ANT\_SEL6

| #define ESP\_ANT\_SEL6   221 |
| --- |

## [◆ ](#a8f9cedf15c49cee3fbac2a22df7675ec)ESP\_ANT\_SEL7

| #define ESP\_ANT\_SEL7   222 |
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

| #define ESP\_BLE\_AUDIO0\_IRQ   206 |
| --- |

## [◆ ](#ab4b3d654c674536c2c63070210147372)ESP\_BLE\_AUDIO1\_IRQ

| #define ESP\_BLE\_AUDIO1\_IRQ   207 |
| --- |

## [◆ ](#a637ea6fcad7b2e5fe48cf9e3419fbed6)ESP\_BLE\_AUDIO2\_IRQ

| #define ESP\_BLE\_AUDIO2\_IRQ   208 |
| --- |

## [◆ ](#aba2aea8feedc96a0a6b3bba007df49ac)ESP\_BLE\_AUDIO\_SYNC0\_P

| #define ESP\_BLE\_AUDIO\_SYNC0\_P   212 |
| --- |

## [◆ ](#a21e5bf1c7c33a39f11d8bf6537ed85bb)ESP\_BLE\_AUDIO\_SYNC1\_P

| #define ESP\_BLE\_AUDIO\_SYNC1\_P   213 |
| --- |

## [◆ ](#a961f37a0b2dcb9e183331ef5684f8504)ESP\_BLE\_AUDIO\_SYNC2\_P

| #define ESP\_BLE\_AUDIO\_SYNC2\_P   214 |
| --- |

## [◆ ](#afd2befcf5eb0c413c0f8447558dc4863)ESP\_BT\_AUDIO0\_IRQ

| #define ESP\_BT\_AUDIO0\_IRQ   203 |
| --- |

## [◆ ](#acfe665b9ff21a51b93819a3f123180ad)ESP\_BT\_AUDIO1\_IRQ

| #define ESP\_BT\_AUDIO1\_IRQ   204 |
| --- |

## [◆ ](#a77ac554a2a10fc6fa77106e8af9dfc86)ESP\_BT\_AUDIO2\_IRQ

| #define ESP\_BT\_AUDIO2\_IRQ   205 |
| --- |

## [◆ ](#a7f8cd1f168870c1cfa215fc1599ebf74)ESP\_CLK\_I2S

| #define ESP\_CLK\_I2S   [ESP\_CLK\_I2S\_MUX](#ae8f094f6bb8c6594dd56ac6365039f89) |
| --- |

## [◆ ](#ae8f094f6bb8c6594dd56ac6365039f89)ESP\_CLK\_I2S\_MUX

| #define ESP\_CLK\_I2S\_MUX   251 |
| --- |

## [◆ ](#ae49b4527d8fbd0f5c8e3edc72704c54a)ESP\_EXT\_ADC\_START

| #define ESP\_EXT\_ADC\_START   93 |
| --- |

## [◆ ](#a68a2f09aae5e8b7d7207cc5c58b031c6)ESP\_FSPI\_DE\_OUT

| #define ESP\_FSPI\_DE\_OUT   136 |
| --- |

## [◆ ](#ac530545e4916a807a391986e544ecda6)ESP\_FSPI\_HSYNC\_OUT

| #define ESP\_FSPI\_HSYNC\_OUT   134 |
| --- |

## [◆ ](#a4690fa15ab99eabd6fe2948704ad6255)ESP\_FSPI\_VSYNC\_OUT

| #define ESP\_FSPI\_VSYNC\_OUT   135 |
| --- |

## [◆ ](#a4bd311f85d48eafbea4d0fd8cd877bc5)ESP\_FSPICD\_OUT

| #define ESP\_FSPICD\_OUT   137 |
| --- |

## [◆ ](#ade88988460c131e8c6775794588b0eb8)ESP\_FSPICLK\_IN

| #define ESP\_FSPICLK\_IN   108 |
| --- |

## [◆ ](#ab8c5397dc530f6326c3d10b31e59e168)ESP\_FSPICLK\_OUT

| #define ESP\_FSPICLK\_OUT   [ESP\_FSPICLK\_OUT\_MUX](#a2054f4af1d18ebb83d9e3439a1b9326e) |
| --- |

## [◆ ](#a2054f4af1d18ebb83d9e3439a1b9326e)ESP\_FSPICLK\_OUT\_MUX

| #define ESP\_FSPICLK\_OUT\_MUX   108 |
| --- |

## [◆ ](#a96ca1328e76337d289f6e65faf33d75c)ESP\_FSPICS0\_IN

| #define ESP\_FSPICS0\_IN   117 |
| --- |

## [◆ ](#ad1be1401b282275eaef46b9a598c6a40)ESP\_FSPICS0\_OUT

| #define ESP\_FSPICS0\_OUT   117 |
| --- |

## [◆ ](#a44ade9179a7ea00586359a009799661d)ESP\_FSPICS1\_OUT

| #define ESP\_FSPICS1\_OUT   118 |
| --- |

## [◆ ](#af991963f29c5b268a5f8fead8fd15348)ESP\_FSPICS2\_OUT

| #define ESP\_FSPICS2\_OUT   119 |
| --- |

## [◆ ](#a65d1170c5a68ac7f6a4457c3380ddfde)ESP\_FSPICS3\_OUT

| #define ESP\_FSPICS3\_OUT   120 |
| --- |

## [◆ ](#a83dafe68703c701dcd07d7ff0aadad01)ESP\_FSPICS4\_OUT

| #define ESP\_FSPICS4\_OUT   121 |
| --- |

## [◆ ](#ad8fab64bb220fd198a6cd931f4ea1e8e)ESP\_FSPICS5\_OUT

| #define ESP\_FSPICS5\_OUT   122 |
| --- |

## [◆ ](#a7910521af840d42edd3c0a667cf90c5f)ESP\_FSPID\_IN

| #define ESP\_FSPID\_IN   110 |
| --- |

## [◆ ](#a02bd34821e8a4bf0038b9af417ec161a)ESP\_FSPID\_OUT

| #define ESP\_FSPID\_OUT   110 |
| --- |

## [◆ ](#a83baa98d81f816f19e65aafb26f15a3c)ESP\_FSPIDQS\_OUT

| #define ESP\_FSPIDQS\_OUT   133 |
| --- |

## [◆ ](#a60ff087a3d85a356d77f060a6698d00b)ESP\_FSPIHD\_IN

| #define ESP\_FSPIHD\_IN   111 |
| --- |

## [◆ ](#ac71bc137b93bd6c0c8a1ebe24a70a613)ESP\_FSPIHD\_OUT

| #define ESP\_FSPIHD\_OUT   111 |
| --- |

## [◆ ](#af751015894fa1cefd780d4c483ed4fe0)ESP\_FSPIIO4\_IN

| #define ESP\_FSPIIO4\_IN   113 |
| --- |

## [◆ ](#a5131d3b8c5f15927eb1ab5f5c5831fc7)ESP\_FSPIIO4\_OUT

| #define ESP\_FSPIIO4\_OUT   113 |
| --- |

## [◆ ](#aa422ee46d7a699a5de5acfce23544f1b)ESP\_FSPIIO5\_IN

| #define ESP\_FSPIIO5\_IN   114 |
| --- |

## [◆ ](#a846120bb034a5178b719de7566af36e9)ESP\_FSPIIO5\_OUT

| #define ESP\_FSPIIO5\_OUT   114 |
| --- |

## [◆ ](#afbba101fa32685cf54ff6579245c232b)ESP\_FSPIIO6\_IN

| #define ESP\_FSPIIO6\_IN   115 |
| --- |

## [◆ ](#acb72c9ac62375b2ef22c4895fd5c37e9)ESP\_FSPIIO6\_OUT

| #define ESP\_FSPIIO6\_OUT   115 |
| --- |

## [◆ ](#a7be0c3215d8ab00a4a87dcf4798207d9)ESP\_FSPIIO7\_IN

| #define ESP\_FSPIIO7\_IN   116 |
| --- |

## [◆ ](#a796dc85ea60a5cce0d0c184805164587)ESP\_FSPIIO7\_OUT

| #define ESP\_FSPIIO7\_OUT   116 |
| --- |

## [◆ ](#ab603b7bf7d016e85653a5c3be5c01293)ESP\_FSPIQ\_IN

| #define ESP\_FSPIQ\_IN   109 |
| --- |

## [◆ ](#a8b3ea6ad374fa010b46b48072fa87ccb)ESP\_FSPIQ\_OUT

| #define ESP\_FSPIQ\_OUT   109 |
| --- |

## [◆ ](#a4d4c4a13b820cab6d94da8fe08120a2f)ESP\_FSPIWP\_IN

| #define ESP\_FSPIWP\_IN   112 |
| --- |

## [◆ ](#a83c4f18d726984cc98caeea9b7677ca1)ESP\_FSPIWP\_OUT

| #define ESP\_FSPIWP\_OUT   112 |
| --- |

## [◆ ](#a47d854bfae0f88dc023613e61e6be551)ESP\_GPIO\_BT\_ACTIVE

| #define ESP\_GPIO\_BT\_ACTIVE   37 |
| --- |

## [◆ ](#ab8d0a9090c64518af59274603f035042)ESP\_GPIO\_BT\_PRIORITY

| #define ESP\_GPIO\_BT\_PRIORITY   38 |
| --- |

## [◆ ](#afe5c166b887709cdd27bd37df85c45b9)ESP\_GPIO\_MAP\_DATE

| #define ESP\_GPIO\_MAP\_DATE   0x1904100 |
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

## [◆ ](#adf2824b1611032a81fe7b3c41253c0d8)ESP\_GPIO\_WLAN\_PRIO

| #define ESP\_GPIO\_WLAN\_PRIO   39 |
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

## [◆ ](#a67905afbcda699d20d8a05a8a66411af)ESP\_I2S0I\_BCK\_IN

| #define ESP\_I2S0I\_BCK\_IN   27 |
| --- |

## [◆ ](#abe571a9bad2c0e95049afd8e67c8d158)ESP\_I2S0I\_BCK\_OUT

| #define ESP\_I2S0I\_BCK\_OUT   27 |
| --- |

## [◆ ](#a433c8fb715a07f27d4b2bcea31b92129)ESP\_I2S0I\_DATA\_IN0

| #define ESP\_I2S0I\_DATA\_IN0   143 |
| --- |

## [◆ ](#a8fdcb030022fc73f03b8b614ec031266)ESP\_I2S0I\_DATA\_IN1

| #define ESP\_I2S0I\_DATA\_IN1   144 |
| --- |

## [◆ ](#a36fd66f4834eb96ba5f1ab7560230065)ESP\_I2S0I\_DATA\_IN10

| #define ESP\_I2S0I\_DATA\_IN10   153 |
| --- |

## [◆ ](#a601911b70e67c09b0bee13be965ea023)ESP\_I2S0I\_DATA\_IN11

| #define ESP\_I2S0I\_DATA\_IN11   154 |
| --- |

## [◆ ](#a1d6581f56d31224a7fe2b2767c815e17)ESP\_I2S0I\_DATA\_IN12

| #define ESP\_I2S0I\_DATA\_IN12   155 |
| --- |

## [◆ ](#a429e25483385ad62fb5d25e25ab16bd1)ESP\_I2S0I\_DATA\_IN13

| #define ESP\_I2S0I\_DATA\_IN13   156 |
| --- |

## [◆ ](#ac9a9df57a89820c2eb0f3af2ca49fc71)ESP\_I2S0I\_DATA\_IN14

| #define ESP\_I2S0I\_DATA\_IN14   157 |
| --- |

## [◆ ](#a1c65e11dbd846847daad7fc716955e64)ESP\_I2S0I\_DATA\_IN15

| #define ESP\_I2S0I\_DATA\_IN15   158 |
| --- |

## [◆ ](#acb82a70ab66b67c43c3df4af940afd20)ESP\_I2S0I\_DATA\_IN2

| #define ESP\_I2S0I\_DATA\_IN2   145 |
| --- |

## [◆ ](#af5f006ccd7b9017a077cb19b7e8584a3)ESP\_I2S0I\_DATA\_IN3

| #define ESP\_I2S0I\_DATA\_IN3   146 |
| --- |

## [◆ ](#a580ec97414913d720035de8df140ce2e)ESP\_I2S0I\_DATA\_IN4

| #define ESP\_I2S0I\_DATA\_IN4   147 |
| --- |

## [◆ ](#a9d72aac34e99ec34569006dbe140f658)ESP\_I2S0I\_DATA\_IN5

| #define ESP\_I2S0I\_DATA\_IN5   148 |
| --- |

## [◆ ](#aed35437eb068e4ea079d8755928161c3)ESP\_I2S0I\_DATA\_IN6

| #define ESP\_I2S0I\_DATA\_IN6   149 |
| --- |

## [◆ ](#a0a04fda280abc577acf3e20d7a917cc8)ESP\_I2S0I\_DATA\_IN7

| #define ESP\_I2S0I\_DATA\_IN7   150 |
| --- |

## [◆ ](#ae144f14b04fff35537effc847a2a6520)ESP\_I2S0I\_DATA\_IN8

| #define ESP\_I2S0I\_DATA\_IN8   151 |
| --- |

## [◆ ](#a54b5575c98e2b363e1cfd556421788d5)ESP\_I2S0I\_DATA\_IN9

| #define ESP\_I2S0I\_DATA\_IN9   152 |
| --- |

## [◆ ](#a933b9ae19e0f6cc02bdb202f7cd95b8c)ESP\_I2S0I\_H\_ENABLE

| #define ESP\_I2S0I\_H\_ENABLE   195 |
| --- |

## [◆ ](#aee6979fc359bc990dac8c49371243697)ESP\_I2S0I\_H\_SYNC

| #define ESP\_I2S0I\_H\_SYNC   193 |
| --- |

## [◆ ](#a99829d36ae815041479b1327a03c9f0a)ESP\_I2S0I\_V\_SYNC

| #define ESP\_I2S0I\_V\_SYNC   194 |
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

| #define ESP\_I2S0O\_DATA\_OUT0   143 |
| --- |

## [◆ ](#ac3656eb3c8ac2d66cc4f9099d486325b)ESP\_I2S0O\_DATA\_OUT1

| #define ESP\_I2S0O\_DATA\_OUT1   144 |
| --- |

## [◆ ](#a789443eb05c68f28a9fa99ff43bd3aa4)ESP\_I2S0O\_DATA\_OUT10

| #define ESP\_I2S0O\_DATA\_OUT10   153 |
| --- |

## [◆ ](#ac8c4f8238d7ac8d3610ad7d817b59f0c)ESP\_I2S0O\_DATA\_OUT11

| #define ESP\_I2S0O\_DATA\_OUT11   154 |
| --- |

## [◆ ](#a1817a5bb7d7c6f81189d61844c9369d8)ESP\_I2S0O\_DATA\_OUT12

| #define ESP\_I2S0O\_DATA\_OUT12   155 |
| --- |

## [◆ ](#a4315e0aa620576457d3fe5543daf8a74)ESP\_I2S0O\_DATA\_OUT13

| #define ESP\_I2S0O\_DATA\_OUT13   156 |
| --- |

## [◆ ](#a60cd35bc47b224db197844526ed31562)ESP\_I2S0O\_DATA\_OUT14

| #define ESP\_I2S0O\_DATA\_OUT14   157 |
| --- |

## [◆ ](#a39a667893007777d45fdcf3c9df17441)ESP\_I2S0O\_DATA\_OUT15

| #define ESP\_I2S0O\_DATA\_OUT15   158 |
| --- |

## [◆ ](#a5f6c0a7cf37eec066127d6cfc6fc8558)ESP\_I2S0O\_DATA\_OUT16

| #define ESP\_I2S0O\_DATA\_OUT16   159 |
| --- |

## [◆ ](#aaa92d37d180f429df167101a6bcde85f)ESP\_I2S0O\_DATA\_OUT17

| #define ESP\_I2S0O\_DATA\_OUT17   160 |
| --- |

## [◆ ](#a1f4f2d0a3535c025d6581e4232bb7fd9)ESP\_I2S0O\_DATA\_OUT18

| #define ESP\_I2S0O\_DATA\_OUT18   161 |
| --- |

## [◆ ](#a6676ad67342db70105683dddae6259a2)ESP\_I2S0O\_DATA\_OUT19

| #define ESP\_I2S0O\_DATA\_OUT19   162 |
| --- |

## [◆ ](#a87405dd9815c0e43d3dc865aa7459cae)ESP\_I2S0O\_DATA\_OUT2

| #define ESP\_I2S0O\_DATA\_OUT2   145 |
| --- |

## [◆ ](#a2d1be2072be7af3e41d25928de743b6e)ESP\_I2S0O\_DATA\_OUT20

| #define ESP\_I2S0O\_DATA\_OUT20   163 |
| --- |

## [◆ ](#a934a97b4ba3f7729b93828fbcfe31c93)ESP\_I2S0O\_DATA\_OUT21

| #define ESP\_I2S0O\_DATA\_OUT21   164 |
| --- |

## [◆ ](#a30d03be995708ac60420d0199d8b2b67)ESP\_I2S0O\_DATA\_OUT22

| #define ESP\_I2S0O\_DATA\_OUT22   165 |
| --- |

## [◆ ](#a4fa877e0f38365b7f18fe4cb04c865a6)ESP\_I2S0O\_DATA\_OUT23

| #define ESP\_I2S0O\_DATA\_OUT23   166 |
| --- |

## [◆ ](#ad0e3c64912151b36169741ada3f5aa0b)ESP\_I2S0O\_DATA\_OUT3

| #define ESP\_I2S0O\_DATA\_OUT3   146 |
| --- |

## [◆ ](#abeb5e69293e78ceff31a7ed908864367)ESP\_I2S0O\_DATA\_OUT4

| #define ESP\_I2S0O\_DATA\_OUT4   147 |
| --- |

## [◆ ](#a93af307990b79a253c9be03d0831f175)ESP\_I2S0O\_DATA\_OUT5

| #define ESP\_I2S0O\_DATA\_OUT5   148 |
| --- |

## [◆ ](#ace1b34e6050863a54792e6ac3c965ab8)ESP\_I2S0O\_DATA\_OUT6

| #define ESP\_I2S0O\_DATA\_OUT6   149 |
| --- |

## [◆ ](#a789d483001496ba193846e90fcc70e74)ESP\_I2S0O\_DATA\_OUT7

| #define ESP\_I2S0O\_DATA\_OUT7   150 |
| --- |

## [◆ ](#a8360e859e714712978c0108b2fd7f8b3)ESP\_I2S0O\_DATA\_OUT8

| #define ESP\_I2S0O\_DATA\_OUT8   151 |
| --- |

## [◆ ](#a0f347fca42d8d9e9bbf1f46a8c05ee84)ESP\_I2S0O\_DATA\_OUT9

| #define ESP\_I2S0O\_DATA\_OUT9   152 |
| --- |

## [◆ ](#aad13d05d8d50227859d484deaaf6e34b)ESP\_I2S0O\_WS\_IN

| #define ESP\_I2S0O\_WS\_IN   25 |
| --- |

## [◆ ](#a78693c10e4ac17973e7ac12c1bdf8c97)ESP\_I2S0O\_WS\_OUT

| #define ESP\_I2S0O\_WS\_OUT   25 |
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

| #define ESP\_PCMCLK\_IN   204 |
| --- |

## [◆ ](#a500651ca0d6daa86774a0f45190f8b38)ESP\_PCMCLK\_OUT

| #define ESP\_PCMCLK\_OUT   210 |
| --- |

## [◆ ](#ae94f8dfc2be2c0cf8863a33df76d5295)ESP\_PCMDIN

| #define ESP\_PCMDIN   205 |
| --- |

## [◆ ](#ab3ecd7e5557112172c38bff3b2605e9c)ESP\_PCMDOUT

| #define ESP\_PCMDOUT   211 |
| --- |

## [◆ ](#a0ad409b608ef2a418098b4e51d0e7e9a)ESP\_PCMFSYNC\_IN

| #define ESP\_PCMFSYNC\_IN   203 |
| --- |

## [◆ ](#a8b79d6e15573a684058c9b933f469f09)ESP\_PCMFSYNC\_OUT

| #define ESP\_PCMFSYNC\_OUT   209 |
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

## [◆ ](#a9023b22f85edc25ab88db9f3fb025c4e)ESP\_PRO\_ALONEGPIO\_IN0

| #define ESP\_PRO\_ALONEGPIO\_IN0   235 |
| --- |

## [◆ ](#a5e4c12a21678930c86e15cbb6d920767)ESP\_PRO\_ALONEGPIO\_IN1

| #define ESP\_PRO\_ALONEGPIO\_IN1   236 |
| --- |

## [◆ ](#a8b82dbe07c785060d2190a13e1fe21ee)ESP\_PRO\_ALONEGPIO\_IN2

| #define ESP\_PRO\_ALONEGPIO\_IN2   237 |
| --- |

## [◆ ](#a5f8a8f6143c1552eec5862ce248ca496)ESP\_PRO\_ALONEGPIO\_IN3

| #define ESP\_PRO\_ALONEGPIO\_IN3   238 |
| --- |

## [◆ ](#ad8ca1006a71cdd738cca02eaf9f923d6)ESP\_PRO\_ALONEGPIO\_IN4

| #define ESP\_PRO\_ALONEGPIO\_IN4   239 |
| --- |

## [◆ ](#aa1b04ac7997451778d7fdbb4f00b0114)ESP\_PRO\_ALONEGPIO\_IN5

| #define ESP\_PRO\_ALONEGPIO\_IN5   240 |
| --- |

## [◆ ](#a525900ed7a103a14105afb6ef8caca69)ESP\_PRO\_ALONEGPIO\_IN6

| #define ESP\_PRO\_ALONEGPIO\_IN6   241 |
| --- |

## [◆ ](#af6ebbb44bcb763355964ac39293cd1c4)ESP\_PRO\_ALONEGPIO\_IN7

| #define ESP\_PRO\_ALONEGPIO\_IN7   242 |
| --- |

## [◆ ](#ae833440baa7073fbfb51ec80ff728ce5)ESP\_PRO\_ALONEGPIO\_OUT0

| #define ESP\_PRO\_ALONEGPIO\_OUT0   235 |
| --- |

## [◆ ](#a5b3065b35c32286fe5ca8d68c033b162)ESP\_PRO\_ALONEGPIO\_OUT1

| #define ESP\_PRO\_ALONEGPIO\_OUT1   236 |
| --- |

## [◆ ](#a287e800e3fb52dd3b6949e6d185f413c)ESP\_PRO\_ALONEGPIO\_OUT2

| #define ESP\_PRO\_ALONEGPIO\_OUT2   237 |
| --- |

## [◆ ](#a49f220c0a7cae6a580174355a80b2b56)ESP\_PRO\_ALONEGPIO\_OUT3

| #define ESP\_PRO\_ALONEGPIO\_OUT3   238 |
| --- |

## [◆ ](#ac1b762f9e0ad1cb60c1e16b0cf7aae0a)ESP\_PRO\_ALONEGPIO\_OUT4

| #define ESP\_PRO\_ALONEGPIO\_OUT4   239 |
| --- |

## [◆ ](#a5f237780803395dd97bb8306a14dbc92)ESP\_PRO\_ALONEGPIO\_OUT5

| #define ESP\_PRO\_ALONEGPIO\_OUT5   240 |
| --- |

## [◆ ](#a4cbc6a3551e057f1d943b01c120317f4)ESP\_PRO\_ALONEGPIO\_OUT6

| #define ESP\_PRO\_ALONEGPIO\_OUT6   241 |
| --- |

## [◆ ](#a3d1993f51138a3ccf8ef913e1863f3bd)ESP\_PRO\_ALONEGPIO\_OUT7

| #define ESP\_PRO\_ALONEGPIO\_OUT7   242 |
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

## [◆ ](#a7abc844342f6483be73ea503d3f76d89)ESP\_RW\_WAKEUP\_REQ

| #define ESP\_RW\_WAKEUP\_REQ   206 |
| --- |

## [◆ ](#aac3529b76d29e57ad20500c9d1da23f3)ESP\_SDIO\_TOHOST\_INT\_OUT

| #define ESP\_SDIO\_TOHOST\_INT\_OUT   31 |
| --- |

## [◆ ](#a645411759ffdc63f51f2cd42632d2720)ESP\_SIG\_GPIO\_OUT

| #define ESP\_SIG\_GPIO\_OUT   256 |
| --- |

## [◆ ](#ad18e273d813830572e425c4cf4abcb38)ESP\_SIG\_IN\_FUNC223

| #define ESP\_SIG\_IN\_FUNC223   223 |
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

## [◆ ](#ae2b550fa907754322b00321e32da00d7)ESP\_SIG\_IN\_FUNC\_223

| #define ESP\_SIG\_IN\_FUNC\_223   223 |
| --- |

## [◆ ](#a5022a9e30fdcf3183a1a44bd3e44496c)ESP\_SIG\_IN\_FUNC\_224

| #define ESP\_SIG\_IN\_FUNC\_224   224 |
| --- |

## [◆ ](#a8a152884133ebca3bd1d72b4f16974bc)ESP\_SIG\_IN\_FUNC\_225

| #define ESP\_SIG\_IN\_FUNC\_225   225 |
| --- |

## [◆ ](#adafe9a8c93ada007bf0e33a56ecdf657)ESP\_SIG\_IN\_FUNC\_226

| #define ESP\_SIG\_IN\_FUNC\_226   226 |
| --- |

## [◆ ](#a00bccf8191e16c8fb59632b7ba63211d)ESP\_SIG\_IN\_FUNC\_227

| #define ESP\_SIG\_IN\_FUNC\_227   227 |
| --- |

## [◆ ](#a4212588a91a6a9dd44499aec13f9fe7a)ESP\_SPI3\_CD\_OUT

| #define ESP\_SPI3\_CD\_OUT   139 |
| --- |

## [◆ ](#a0bff2051090f5eaea7edd6e9b4725a3c)ESP\_SPI3\_CLK\_IN

| #define ESP\_SPI3\_CLK\_IN   72 |
| --- |

## [◆ ](#ad58fe98667e0bc1b79849a7a974a8157)ESP\_SPI3\_CLK\_OUT\_MUX

| #define ESP\_SPI3\_CLK\_OUT\_MUX   72 |
| --- |

## [◆ ](#a485eded26f1b4bd7f03d916dcd4b0753)ESP\_SPI3\_CS0\_IN

| #define ESP\_SPI3\_CS0\_IN   76 |
| --- |

## [◆ ](#a8fc990a73f8fdc8d1004b3dad676a224)ESP\_SPI3\_CS0\_OUT

| #define ESP\_SPI3\_CS0\_OUT   76 |
| --- |

## [◆ ](#a7f06d2db560a8cd511c9189cd6ed8980)ESP\_SPI3\_CS1\_OUT

| #define ESP\_SPI3\_CS1\_OUT   77 |
| --- |

## [◆ ](#a9e4bf0b0eff43b1f56f17abe22ef24a5)ESP\_SPI3\_CS2\_OUT

| #define ESP\_SPI3\_CS2\_OUT   78 |
| --- |

## [◆ ](#ae7cf1730786ba95580b91b00066d3e25)ESP\_SPI3\_D\_IN

| #define ESP\_SPI3\_D\_IN   74 |
| --- |

## [◆ ](#aff4a1289beb94c9e23d7c1dd13d71d83)ESP\_SPI3\_D\_OUT

| #define ESP\_SPI3\_D\_OUT   74 |
| --- |

## [◆ ](#aa9be8338dbdaecb13c5de0c38fbb12ab)ESP\_SPI3\_DQS\_OUT

| #define ESP\_SPI3\_DQS\_OUT   140 |
| --- |

## [◆ ](#a84dd16599428fb4c3da12c221219af40)ESP\_SPI3\_HD\_IN

| #define ESP\_SPI3\_HD\_IN   75 |
| --- |

## [◆ ](#a73457a024aa63c16c2a5ef8ada2bf8b2)ESP\_SPI3\_HD\_OUT

| #define ESP\_SPI3\_HD\_OUT   75 |
| --- |

## [◆ ](#a05a9a2e5983b7895ca1fb05e5cd34709)ESP\_SPI3\_Q\_IN

| #define ESP\_SPI3\_Q\_IN   73 |
| --- |

## [◆ ](#a6656c910c99e3de854064f4df24faa2d)ESP\_SPI3\_Q\_OUT

| #define ESP\_SPI3\_Q\_OUT   73 |
| --- |

## [◆ ](#a5f440c922a53085bb7b28f469c2a14b0)ESP\_SPICLK\_OUT

| #define ESP\_SPICLK\_OUT   [ESP\_SPICLK\_OUT\_MUX](#aaf157f6b85a07f18b181876a7a04f142) |
| --- |

## [◆ ](#aaf157f6b85a07f18b181876a7a04f142)ESP\_SPICLK\_OUT\_MUX

| #define ESP\_SPICLK\_OUT\_MUX   4 |
| --- |

## [◆ ](#a5d97c07ba0d8cda594d52310e90fa6a4)ESP\_SPICS0\_OUT

| #define ESP\_SPICS0\_OUT   5 |
| --- |

## [◆ ](#aa4a67a38b97a3d466783c0617aa6a0c8)ESP\_SPICS1\_OUT

| #define ESP\_SPICS1\_OUT   6 |
| --- |

## [◆ ](#ade124a5a82af0f49b122b32d69ee8d04)ESP\_SPID4\_IN

| #define ESP\_SPID4\_IN   7 |
| --- |

## [◆ ](#a9bd0335c81e6828a5da77af387fbe845)ESP\_SPID4\_OUT

| #define ESP\_SPID4\_OUT   7 |
| --- |

## [◆ ](#ae8fa56cbc73756ff3895a937ab1374c2)ESP\_SPID5\_IN

| #define ESP\_SPID5\_IN   8 |
| --- |

## [◆ ](#a61317dd1e2daf50f35240fd561180628)ESP\_SPID5\_OUT

| #define ESP\_SPID5\_OUT   8 |
| --- |

## [◆ ](#a2d850da0ce491f0049b9920cde48907e)ESP\_SPID6\_IN

| #define ESP\_SPID6\_IN   9 |
| --- |

## [◆ ](#a918e6203f9d52d8d2606616a938faea8)ESP\_SPID6\_OUT

| #define ESP\_SPID6\_OUT   9 |
| --- |

## [◆ ](#a78073d0d570a71824e00bebe4bbd97d1)ESP\_SPID7\_IN

| #define ESP\_SPID7\_IN   10 |
| --- |

## [◆ ](#a0802cd16128bd289444b670a827d0d31)ESP\_SPID7\_OUT

| #define ESP\_SPID7\_OUT   10 |
| --- |

## [◆ ](#a26c603fd58dbd7526d2be3bb3e37758a)ESP\_SPID\_IN

| #define ESP\_SPID\_IN   1 |
| --- |

## [◆ ](#af81b2fc65b68ed2238ab3367a8731102)ESP\_SPID\_OUT

| #define ESP\_SPID\_OUT   1 |
| --- |

## [◆ ](#ae891264c3a0289dad5851d44b18707d2)ESP\_SPIDQS\_IN

| #define ESP\_SPIDQS\_IN   11 |
| --- |

## [◆ ](#a88309f7b84da7f6e461139ad137cfb97)ESP\_SPIDQS\_OUT

| #define ESP\_SPIDQS\_OUT   11 |
| --- |

## [◆ ](#a49783f877b666aff9362cf605590b991)ESP\_SPIHD\_IN

| #define ESP\_SPIHD\_IN   2 |
| --- |

## [◆ ](#a8851b5256482790f3304efecafc13afd)ESP\_SPIHD\_OUT

| #define ESP\_SPIHD\_OUT   2 |
| --- |

## [◆ ](#aec51ff955c6be50e529affc87ec9d5cb)ESP\_SPIQ\_IN

| #define ESP\_SPIQ\_IN   0 |
| --- |

## [◆ ](#a5816deeca8853397a830a8eb251704ee)ESP\_SPIQ\_OUT

| #define ESP\_SPIQ\_OUT   0 |
| --- |

## [◆ ](#aa74adc2812d9c6bd143c679fa4d9ca8d)ESP\_SPIWP\_IN

| #define ESP\_SPIWP\_IN   3 |
| --- |

## [◆ ](#a470408f8102937dc017336e320e6147b)ESP\_SPIWP\_OUT

| #define ESP\_SPIWP\_OUT   3 |
| --- |

## [◆ ](#a0651dd050ec01b150a74bb1f8db2221f)ESP\_SUBSPICLK\_OUT\_MUX

| #define ESP\_SUBSPICLK\_OUT\_MUX   126 |
| --- |

## [◆ ](#a8925d5f830a4bc5ca6114dc06bae3b1f)ESP\_SUBSPICS0\_OUT

| #define ESP\_SUBSPICS0\_OUT   131 |
| --- |

## [◆ ](#add0fa80736d0fe196872bb0664c433d4)ESP\_SUBSPICS1\_OUT

| #define ESP\_SUBSPICS1\_OUT   132 |
| --- |

## [◆ ](#aae7066cb62b74cf5e8f64f84bd76ee49)ESP\_SUBSPID4\_IN

| #define ESP\_SUBSPID4\_IN   167 |
| --- |

## [◆ ](#aa716d46da29da6affd5fa8851a730f3f)ESP\_SUBSPID4\_OUT

| #define ESP\_SUBSPID4\_OUT   167 |
| --- |

## [◆ ](#a051cd2450520fd4abc6f288c8577a12c)ESP\_SUBSPID5\_IN

| #define ESP\_SUBSPID5\_IN   168 |
| --- |

## [◆ ](#aece7dc6fc4bca1bd73d9ba856eb0f3fe)ESP\_SUBSPID5\_OUT

| #define ESP\_SUBSPID5\_OUT   168 |
| --- |

## [◆ ](#a6d49162b17a1a7cd3f2446c6ca8192ec)ESP\_SUBSPID6\_IN

| #define ESP\_SUBSPID6\_IN   169 |
| --- |

## [◆ ](#ab3e8db3219bf7aa7b2503a1fe759d60c)ESP\_SUBSPID6\_OUT

| #define ESP\_SUBSPID6\_OUT   169 |
| --- |

## [◆ ](#a34b9a22e0f55a0534199e62b1eaff5b0)ESP\_SUBSPID7\_IN

| #define ESP\_SUBSPID7\_IN   170 |
| --- |

## [◆ ](#adb8c01bf2361a8b24e79cf048a7e6535)ESP\_SUBSPID7\_OUT

| #define ESP\_SUBSPID7\_OUT   170 |
| --- |

## [◆ ](#a0c924000fccdb7ce112822db720dbd8d)ESP\_SUBSPID\_IN

| #define ESP\_SUBSPID\_IN   128 |
| --- |

## [◆ ](#a3b9cab35f71697419266c71583f8a087)ESP\_SUBSPID\_OUT

| #define ESP\_SUBSPID\_OUT   128 |
| --- |

## [◆ ](#a6ccb6e41ab48fba76302068ee4433fb8)ESP\_SUBSPIDQS\_IN

| #define ESP\_SUBSPIDQS\_IN   171 |
| --- |

## [◆ ](#a608345dcd6c90e4f19427bb38161501a)ESP\_SUBSPIDQS\_OUT

| #define ESP\_SUBSPIDQS\_OUT   171 |
| --- |

## [◆ ](#a9a04da28895e846359a3ea89391b21f6)ESP\_SUBSPIHD\_IN

| #define ESP\_SUBSPIHD\_IN   129 |
| --- |

## [◆ ](#ab1f7e54d6230ceabc3fee083aab409d1)ESP\_SUBSPIHD\_OUT

| #define ESP\_SUBSPIHD\_OUT   129 |
| --- |

## [◆ ](#af80ecb5fcd6c02cb5b73478198abef3c)ESP\_SUBSPIQ\_IN

| #define ESP\_SUBSPIQ\_IN   127 |
| --- |

## [◆ ](#ac75fd67f54d49449451c4924c0b7910a)ESP\_SUBSPIQ\_OUT

| #define ESP\_SUBSPIQ\_OUT   127 |
| --- |

## [◆ ](#a3c4b2938ef6753d76a752bf9a973de52)ESP\_SUBSPIWP\_IN

| #define ESP\_SUBSPIWP\_IN   130 |
| --- |

## [◆ ](#a7493ab9a1f0dc10902ce412055579842)ESP\_SUBSPIWP\_OUT

| #define ESP\_SUBSPIWP\_OUT   130 |
| --- |

## [◆ ](#a6d0d41d1ec0f6fc626861f5857684e6d)ESP\_TWAI\_BUS\_OFF\_ON

| #define ESP\_TWAI\_BUS\_OFF\_ON   124 |
| --- |

## [◆ ](#a1c69791269fdbb2a11f66f33eb4066be)ESP\_TWAI\_CLKOUT

| #define ESP\_TWAI\_CLKOUT   125 |
| --- |

## [◆ ](#ab3da303c2f9226f9648669c17af8377a)ESP\_TWAI\_RX

| #define ESP\_TWAI\_RX   123 |
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

## [◆ ](#a5f29b138691540598d0b977dc4bd5971)ESP\_U1DSR\_IN

| #define ESP\_U1DSR\_IN   21 |
| --- |

## [◆ ](#a1f7df042d40ec6f20b559ef6778d7497)ESP\_U1DTR\_OUT

| #define ESP\_U1DTR\_OUT   21 |
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

## [◆ ](#a28f381128449aed0ae738516df39790c)ESP\_USB\_EXTPHY\_OEN

| #define ESP\_USB\_EXTPHY\_OEN   61 |
| --- |

## [◆ ](#a095d83d616afb08c4b06d82c4d907fee)ESP\_USB\_EXTPHY\_RCV

| #define ESP\_USB\_EXTPHY\_RCV   63 |
| --- |

## [◆ ](#aedb10271abe4c1969eefbc0425681652)ESP\_USB\_EXTPHY\_SPEED

| #define ESP\_USB\_EXTPHY\_SPEED   62 |
| --- |

## [◆ ](#a301551d0d524f785b3d0e2c35bc81ce5)ESP\_USB\_EXTPHY\_SUSPND

| #define ESP\_USB\_EXTPHY\_SUSPND   65 |
| --- |

## [◆ ](#aeaa130d2e220f2ebd073983921ad3679)ESP\_USB\_EXTPHY\_VM

| #define ESP\_USB\_EXTPHY\_VM   62 |
| --- |

## [◆ ](#abaeb7b2bb8208db93655b442293976aa)ESP\_USB\_EXTPHY\_VMO

| #define ESP\_USB\_EXTPHY\_VMO   64 |
| --- |

## [◆ ](#a7c2bcf73d61315a0d8c71d68173f9860)ESP\_USB\_EXTPHY\_VP

| #define ESP\_USB\_EXTPHY\_VP   61 |
| --- |

## [◆ ](#a88c6a9f957332dac96360dd3f631e59b)ESP\_USB\_EXTPHY\_VPO

| #define ESP\_USB\_EXTPHY\_VPO   63 |
| --- |

## [◆ ](#a4d0c408fedb6ba35298c1398eccaa4e2)ESP\_USB\_OTG\_AVALID\_IN

| #define ESP\_USB\_OTG\_AVALID\_IN   65 |
| --- |

## [◆ ](#a852717f88ddb411d5b0dc49a3be83282)ESP\_USB\_OTG\_DMPULLDOWN

| #define ESP\_USB\_OTG\_DMPULLDOWN   68 |
| --- |

## [◆ ](#a04c49eae7bb25687d76a810ab6468353)ESP\_USB\_OTG\_DPPULLDOWN

| #define ESP\_USB\_OTG\_DPPULLDOWN   67 |
| --- |

## [◆ ](#a6f79de1e3bbc3758362426eecad93d3d)ESP\_USB\_OTG\_DRVVBUS

| #define ESP\_USB\_OTG\_DRVVBUS   69 |
| --- |

## [◆ ](#a22582585ff59bc29c3e011c4d869b1b8)ESP\_USB\_OTG\_IDDIG\_IN

| #define ESP\_USB\_OTG\_IDDIG\_IN   64 |
| --- |

## [◆ ](#ab7335ddb7641fb62231adf289a7a74a8)ESP\_USB\_OTG\_IDPULLUP

| #define ESP\_USB\_OTG\_IDPULLUP   66 |
| --- |

## [◆ ](#a4e3bd2577c74b857a74f1c367a235bad)ESP\_USB\_OTG\_VBUSVALID\_IN

| #define ESP\_USB\_OTG\_VBUSVALID\_IN   67 |
| --- |

## [◆ ](#aaafaee30be8e3fed2eb1117ce381dd37)ESP\_USB\_SRP\_BVALID\_IN

| #define ESP\_USB\_SRP\_BVALID\_IN   66 |
| --- |

## [◆ ](#a49b28cbc76c15cd1395f3b2e1a6ac4d9)ESP\_USB\_SRP\_CHRGVBUS

| #define ESP\_USB\_SRP\_CHRGVBUS   70 |
| --- |

## [◆ ](#a30f3abf038b27fa16a82bdf413eff14c)ESP\_USB\_SRP\_DISCHRGVBUS

| #define ESP\_USB\_SRP\_DISCHRGVBUS   71 |
| --- |

## [◆ ](#a8601c4fb546ff39782c0fbb14e68bfbd)ESP\_USB\_SRP\_SESSEND\_IN

| #define ESP\_USB\_SRP\_SESSEND\_IN   68 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [esp32s2-gpio-sigmap.h](esp32s2-gpio-sigmap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
