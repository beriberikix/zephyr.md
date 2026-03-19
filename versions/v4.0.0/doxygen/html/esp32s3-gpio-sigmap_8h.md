---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/esp32s3-gpio-sigmap_8h.html
original_path: doxygen/html/esp32s3-gpio-sigmap_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32s3-gpio-sigmap.h File Reference

[Go to the source code of this file.](esp32s3-gpio-sigmap_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ESP\_NOSIG](#af80260535bc3aee44c28c972a29483e0)   [ESP\_SIG\_INVAL](esp-pinctrl-common_8h.md#ae0d2e726ab8d90343e5c80e1d9b85ad8) |
| #define | [ESP\_SPIQ\_IN](#aec51ff955c6be50e529affc87ec9d5cb)   0 |
| #define | [ESP\_SPIQ\_OUT](#a5816deeca8853397a830a8eb251704ee)   0 |
| #define | [ESP\_SPID\_IN](#a26c603fd58dbd7526d2be3bb3e37758a)   1 |
| #define | [ESP\_SPID\_OUT](#af81b2fc65b68ed2238ab3367a8731102)   1 |
| #define | [ESP\_SPIHD\_IN](#a49783f877b666aff9362cf605590b991)   2 |
| #define | [ESP\_SPIHD\_OUT](#a8851b5256482790f3304efecafc13afd)   2 |
| #define | [ESP\_SPIWP\_IN](#aa74adc2812d9c6bd143c679fa4d9ca8d)   3 |
| #define | [ESP\_SPIWP\_OUT](#a470408f8102937dc017336e320e6147b)   3 |
| #define | [ESP\_SPICLK\_OUT](#a5f440c922a53085bb7b28f469c2a14b0)   4 |
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
| #define | [ESP\_U0RXD\_IN](#aca502efa55ce2286dc9eba28192681fd)   12 |
| #define | [ESP\_U0TXD\_OUT](#af1e58fb8e7ef86a92171eca7bb1671af)   12 |
| #define | [ESP\_U0CTS\_IN](#a530d7a918a97cd1fff1acf2f90edd4ca)   13 |
| #define | [ESP\_U0RTS\_OUT](#a4257bbc044af6ea3612313e3a0b7e7c9)   13 |
| #define | [ESP\_U0DSR\_IN](#a53e3a4557a4eb1f7f98250abef03c02a)   14 |
| #define | [ESP\_U0DTR\_OUT](#acc8716af947169c9f167bdf215c5314c)   14 |
| #define | [ESP\_U1RXD\_IN](#a2293e0646e0ad2f76d62f76425ae6770)   15 |
| #define | [ESP\_U1TXD\_OUT](#a6053b38147e28e3a7479b38e7d195136)   15 |
| #define | [ESP\_U1CTS\_IN](#a3c005e616da21a058960d6aed79427b3)   16 |
| #define | [ESP\_U1RTS\_OUT](#a8f6399745566bd5caa2020e4dcb2bb3b)   16 |
| #define | [ESP\_U1DSR\_IN](#a5f29b138691540598d0b977dc4bd5971)   17 |
| #define | [ESP\_U1DTR\_OUT](#a1f7df042d40ec6f20b559ef6778d7497)   17 |
| #define | [ESP\_U2RXD\_IN](#abe46ead057c2b66d500ef07e8a84fe0f)   18 |
| #define | [ESP\_U2TXD\_OUT](#a20baac10eb4b76603580e1ea7065213a)   18 |
| #define | [ESP\_U2CTS\_IN](#a735a482aa723130ccb408f0fb7596a0a)   19 |
| #define | [ESP\_U2RTS\_OUT](#a174b50e35d961ded056cea3848110b20)   19 |
| #define | [ESP\_U2DSR\_IN](#a70d4f834bfd182c138257e36a4b04096)   20 |
| #define | [ESP\_U2DTR\_OUT](#a783f6ee9ad46dfd9e34d1473b1e2ad9b)   20 |
| #define | [ESP\_I2S1\_MCLK\_IN](#af00f358d0012d5a4e85a0610f9da2ace)   21 |
| #define | [ESP\_I2S1\_MCLK\_OUT](#aeeb2b00d8b3172832532d96b2282d4d2)   21 |
| #define | [ESP\_I2S0O\_BCK\_IN](#af0b9626d6b7cfd5b5c42a8127897d565)   22 |
| #define | [ESP\_I2S0O\_BCK\_OUT](#a2e76c532bd75a6af4790b30f58c4b8e9)   22 |
| #define | [ESP\_I2S0\_MCLK\_IN](#a329858f11621f706f0a933886246e177)   23 |
| #define | [ESP\_I2S0\_MCLK\_OUT](#acd2f3e9c21da61b98fdc86b8a264d9fd)   23 |
| #define | [ESP\_I2S0O\_WS\_IN](#aad13d05d8d50227859d484deaaf6e34b)   24 |
| #define | [ESP\_I2S0O\_WS\_OUT](#a78693c10e4ac17973e7ac12c1bdf8c97)   24 |
| #define | [ESP\_I2S0I\_SD\_IN](#a8e920eb744585bdec4b5ca8c6a6ec7b6)   25 |
| #define | [ESP\_I2S0O\_SD\_OUT](#a9e263a786610ffa2b60051a03188b67b)   25 |
| #define | [ESP\_I2S0I\_BCK\_IN](#a67905afbcda699d20d8a05a8a66411af)   26 |
| #define | [ESP\_I2S0I\_BCK\_OUT](#abe571a9bad2c0e95049afd8e67c8d158)   26 |
| #define | [ESP\_I2S0I\_WS\_IN](#a4236f62ac75d5f2d56f7b1cc941d7509)   27 |
| #define | [ESP\_I2S0I\_WS\_OUT](#af039bdc8eec9ec95d3ed2bbebabb22cb)   27 |
| #define | [ESP\_I2S1O\_BCK\_IN](#afffede35b0effa00a9d6e1077ac4aaa2)   28 |
| #define | [ESP\_I2S1O\_BCK\_OUT](#afcd05d2cf345dcf816068b0b89ac5a72)   28 |
| #define | [ESP\_I2S1O\_WS\_IN](#a7ac95a35ee6001c340cddd1424f3fa5e)   29 |
| #define | [ESP\_I2S1O\_WS\_OUT](#a84485bdfe1661269506f7ef1f70f4a87)   29 |
| #define | [ESP\_I2S1I\_SD\_IN](#a854ae55e42905b005332084451ddf0ba)   30 |
| #define | [ESP\_I2S1O\_SD\_OUT](#aa97d280d714ad4284f617df4453bdcf6)   30 |
| #define | [ESP\_I2S1I\_BCK\_IN](#a537fd0715c03fd03d914d72d01191b9a)   31 |
| #define | [ESP\_I2S1I\_BCK\_OUT](#a93d4d6602af3ba29121fef124145f4a5)   31 |
| #define | [ESP\_I2S1I\_WS\_IN](#a90b7c81877f6ab8ec1af498db7b8dc0e)   32 |
| #define | [ESP\_I2S1I\_WS\_OUT](#a1ed428a9dd21d57a7311c24f192e032e)   32 |
| #define | [ESP\_PCNT\_SIG\_CH0\_IN0](#acf123456a5b9d94f370309ad39672e34)   33 |
| #define | [ESP\_GPIO\_WLAN\_PRIO](#adf2824b1611032a81fe7b3c41253c0d8)   33 |
| #define | [ESP\_PCNT\_SIG\_CH1\_IN0](#a800813b2c23f7e4bb23e032e0802a459)   34 |
| #define | [ESP\_GPIO\_WLAN\_ACTIVE](#af675ca03172d2dcee1e19ccb5236e087)   34 |
| #define | [ESP\_PCNT\_CTRL\_CH0\_IN0](#a7e3c939b0b32332a35f0bead0aa4a2a6)   35 |
| #define | [ESP\_BB\_DIAG0](#a304bc90cc758f90f6675fea611ab0cfe)   35 |
| #define | [ESP\_PCNT\_CTRL\_CH1\_IN0](#a88c5eb5c7f4169ce3e7f7056b42989a7)   36 |
| #define | [ESP\_BB\_DIAG1](#ad236bf991329914d59c194ff9003974a)   36 |
| #define | [ESP\_PCNT\_SIG\_CH0\_IN1](#a99db3d1c4e07e11fc09a4024a54fcea6)   37 |
| #define | [ESP\_BB\_DIAG2](#a26c20261a5e2f4293b81c802a0a33b19)   37 |
| #define | [ESP\_PCNT\_SIG\_CH1\_IN1](#a730113779d69ca86b257060678f8cbec)   38 |
| #define | [ESP\_BB\_DIAG3](#a5124ef75b703e7805bccd8c93828faae)   38 |
| #define | [ESP\_PCNT\_CTRL\_CH0\_IN1](#a9ec8d490316b9f043fe5e9160a7cf7e0)   39 |
| #define | [ESP\_BB\_DIAG4](#aebd2c37b71d18967bd394b32c820647f)   39 |
| #define | [ESP\_PCNT\_CTRL\_CH1\_IN1](#a0bbfffdef085eb6cedc3d1232766cb38)   40 |
| #define | [ESP\_BB\_DIAG5](#ace166b18a74fb8a42f876d1aa7cfb059)   40 |
| #define | [ESP\_PCNT\_SIG\_CH0\_IN2](#a4f9e798a260fb6ac4c39262f20253244)   41 |
| #define | [ESP\_BB\_DIAG6](#ad5685b19c170cc428cea0ee91f9155b0)   41 |
| #define | [ESP\_PCNT\_SIG\_CH1\_IN2](#a38365b3f9a2b49ef2714c38d00d293c5)   42 |
| #define | [ESP\_BB\_DIAG7](#aedf32208932dfe4471f6a5a7feb652f8)   42 |
| #define | [ESP\_PCNT\_CTRL\_CH0\_IN2](#a540cbfcd205911955effcc9814f9707c)   43 |
| #define | [ESP\_BB\_DIAG8](#a126e2108473183890c6a2e148f8fd2c7)   43 |
| #define | [ESP\_PCNT\_CTRL\_CH1\_IN2](#abf6c210e19582b06e3d6c546a009ef5b)   44 |
| #define | [ESP\_BB\_DIAG9](#a75b60b1b4d53e6fca02b3a4f14ea530e)   44 |
| #define | [ESP\_PCNT\_SIG\_CH0\_IN3](#acd8d20d89508b532a4e2749499263de3)   45 |
| #define | [ESP\_BB\_DIAG10](#aed67caee00b7ceaaaa33b2917aba60f2)   45 |
| #define | [ESP\_PCNT\_SIG\_CH1\_IN3](#ac54a606ee7096db15cdb9453b04ac72d)   46 |
| #define | [ESP\_BB\_DIAG11](#aef4bb5d62b93dfc3f2834404b6945b90)   46 |
| #define | [ESP\_PCNT\_CTRL\_CH0\_IN3](#a96e8bd4584ab671a1b0c3f0adb440943)   47 |
| #define | [ESP\_BB\_DIAG12](#acc6cd70ce139a5639022bec896a3ba5e)   47 |
| #define | [ESP\_PCNT\_CTRL\_CH1\_IN3](#a0a926d350fc11d737b545c53b3ba1671)   48 |
| #define | [ESP\_BB\_DIAG13](#afa72089303bf662a4efc8c068b157f0d)   48 |
| #define | [ESP\_GPIO\_BT\_ACTIVE](#a47d854bfae0f88dc023613e61e6be551)   49 |
| #define | [ESP\_BB\_DIAG14](#a4ef00458e2547f7141741191b92854d8)   49 |
| #define | [ESP\_GPIO\_BT\_PRIORITY](#ab8d0a9090c64518af59274603f035042)   50 |
| #define | [ESP\_BB\_DIAG15](#aed7c06883c6a69303a341454aff409ed)   50 |
| #define | [ESP\_I2S0I\_SD1\_IN](#a9ae165cac1d30c38270f8747caa18f00)   51 |
| #define | [ESP\_BB\_DIAG16](#a1acc29dd7c0517c30299e71c1a6ce7fa)   51 |
| #define | [ESP\_I2S0I\_SD2\_IN](#a5e4fdb79d8fefa835118c21fe6b05cb5)   52 |
| #define | [ESP\_BB\_DIAG17](#a9abbf3178088e44d984b088f53c25ab1)   52 |
| #define | [ESP\_I2S0I\_SD3\_IN](#a39f410a33a8ddc30a37de7d0b5ff821d)   53 |
| #define | [ESP\_BB\_DIAG18](#af75798fba81841339510ecc5f94e542e)   53 |
| #define | [ESP\_CORE1\_GPIO\_IN7](#ae07a10a5b5f791d98034a0ffcaa0a5c1)   54 |
| #define | [ESP\_CORE1\_GPIO\_OUT7](#ac9744120f941e282f182bf4b16b31a34)   54 |
| #define | [ESP\_USB\_EXTPHY\_VP](#a7c2bcf73d61315a0d8c71d68173f9860)   55 |
| #define | [ESP\_USB\_EXTPHY\_OEN](#a28f381128449aed0ae738516df39790c)   55 |
| #define | [ESP\_USB\_EXTPHY\_VM](#aeaa130d2e220f2ebd073983921ad3679)   56 |
| #define | [ESP\_USB\_EXTPHY\_SPEED](#aedb10271abe4c1969eefbc0425681652)   56 |
| #define | [ESP\_USB\_EXTPHY\_RCV](#a095d83d616afb08c4b06d82c4d907fee)   57 |
| #define | [ESP\_USB\_EXTPHY\_VPO](#a88c6a9f957332dac96360dd3f631e59b)   57 |
| #define | [ESP\_USB\_OTG\_IDDIG\_IN](#a22582585ff59bc29c3e011c4d869b1b8)   58 |
| #define | [ESP\_USB\_EXTPHY\_VMO](#abaeb7b2bb8208db93655b442293976aa)   58 |
| #define | [ESP\_USB\_OTG\_AVALID\_IN](#a4d0c408fedb6ba35298c1398eccaa4e2)   59 |
| #define | [ESP\_USB\_EXTPHY\_SUSPND](#a301551d0d524f785b3d0e2c35bc81ce5)   59 |
| #define | [ESP\_USB\_SRP\_BVALID\_IN](#aaafaee30be8e3fed2eb1117ce381dd37)   60 |
| #define | [ESP\_USB\_OTG\_IDPULLUP](#ab7335ddb7641fb62231adf289a7a74a8)   60 |
| #define | [ESP\_USB\_OTG\_VBUSVALID\_IN](#a4e3bd2577c74b857a74f1c367a235bad)   61 |
| #define | [ESP\_USB\_OTG\_DPPULLDOWN](#a04c49eae7bb25687d76a810ab6468353)   61 |
| #define | [ESP\_USB\_SRP\_SESSEND\_IN](#a8601c4fb546ff39782c0fbb14e68bfbd)   62 |
| #define | [ESP\_USB\_OTG\_DMPULLDOWN](#a852717f88ddb411d5b0dc49a3be83282)   62 |
| #define | [ESP\_USB\_OTG\_DRVVBUS](#a6f79de1e3bbc3758362426eecad93d3d)   63 |
| #define | [ESP\_USB\_SRP\_CHRGVBUS](#a49b28cbc76c15cd1395f3b2e1a6ac4d9)   64 |
| #define | [ESP\_USB\_SRP\_DISCHRGVBUS](#a30f3abf038b27fa16a82bdf413eff14c)   65 |
| #define | [ESP\_SPI3\_CLK\_IN](#a0bff2051090f5eaea7edd6e9b4725a3c)   66 |
| #define | [ESP\_SPI3\_CLK\_OUT](#a02cc6c3ead85cf6c4837f05807103521)   66 |
| #define | [ESP\_SPI3\_Q\_IN](#a05a9a2e5983b7895ca1fb05e5cd34709)   67 |
| #define | [ESP\_SPI3\_Q\_OUT](#a6656c910c99e3de854064f4df24faa2d)   67 |
| #define | [ESP\_SPI3\_D\_IN](#ae7cf1730786ba95580b91b00066d3e25)   68 |
| #define | [ESP\_SPI3\_D\_OUT](#aff4a1289beb94c9e23d7c1dd13d71d83)   68 |
| #define | [ESP\_SPI3\_HD\_IN](#a84dd16599428fb4c3da12c221219af40)   69 |
| #define | [ESP\_SPI3\_HD\_OUT](#a73457a024aa63c16c2a5ef8ada2bf8b2)   69 |
| #define | [ESP\_SPI3\_WP\_IN](#ae5ef053fe616dfb189a1a5bf28313647)   70 |
| #define | [ESP\_SPI3\_WP\_OUT](#ab3c345085fafd95b7bd2f83d14a5317c)   70 |
| #define | [ESP\_SPI3\_CS0\_IN](#a485eded26f1b4bd7f03d916dcd4b0753)   71 |
| #define | [ESP\_SPI3\_CS0\_OUT](#a8fc990a73f8fdc8d1004b3dad676a224)   71 |
| #define | [ESP\_SPI3\_CS1\_OUT](#a7f06d2db560a8cd511c9189cd6ed8980)   72 |
| #define | [ESP\_EXT\_ADC\_START](#ae49b4527d8fbd0f5c8e3edc72704c54a)   73 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT0](#a62dfcd88747c61acb53dc85c1751f1d3)   73 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT1](#a5cad9206cfeea93b42e5456228c7d580)   74 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT2](#ab408070e7c700805db165c3876b6c588)   75 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT3](#a438aee217c6c94a2962a3d98935b5717)   76 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT4](#ada93dcffffc15362be4b7432a8033559)   77 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT5](#a34fc029ec45756ca7064580f57db1cc7)   78 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT6](#a28b01adea7e0bcc8b76fe05d58c1cbd0)   79 |
| #define | [ESP\_LEDC\_LS\_SIG\_OUT7](#a2ea140f2da1a15b24dcaa3592909ca35)   80 |
| #define | [ESP\_RMT\_SIG\_IN0](#ad9bae9b4884a356e465656d1ee8d61cd)   81 |
| #define | [ESP\_RMT\_SIG\_OUT0](#a25343fbc20a0c542bcdc21cdfade867b)   81 |
| #define | [ESP\_RMT\_SIG\_IN1](#ab6c6293e6845ba4bf4d05b84102ffdcf)   82 |
| #define | [ESP\_RMT\_SIG\_OUT1](#a6d082fb1c7397d784a3075108e0dea73)   82 |
| #define | [ESP\_RMT\_SIG\_IN2](#af88ebdd0d2d02ac58d720c001ccc155b)   83 |
| #define | [ESP\_RMT\_SIG\_OUT2](#ad657c1ddcf9c335ac7876464b80b2705)   83 |
| #define | [ESP\_RMT\_SIG\_IN3](#a1f930cd82690248b839f16ff7738f32c)   84 |
| #define | [ESP\_RMT\_SIG\_OUT3](#ae60033bb70ca9ff7c2b52368d24a8ab8)   84 |
| #define | [ESP\_USB\_JTAG\_TCK](#ae39a7176534ecc35ed432e6b825cf1ee)   85 |
| #define | [ESP\_USB\_JTAG\_TMS](#aca9c05aba976c762c0ec5fa3603c76e1)   86 |
| #define | [ESP\_USB\_JTAG\_TDI](#ad92972ab672e468cc56c24733114d7db)   87 |
| #define | [ESP\_USB\_JTAG\_TDO](#a880f86e1452afee85e90589f74c17a4d)   88 |
| #define | [ESP\_I2CEXT0\_SCL\_IN](#ab607ce367da34ab0f1bd7fa648273cf1)   89 |
| #define | [ESP\_I2CEXT0\_SCL\_OUT](#a2144cc62df795547ccf2bbe3ee4c629f)   89 |
| #define | [ESP\_I2CEXT0\_SDA\_IN](#afa7061c87135b9dabe5c54f5f4ce16e6)   90 |
| #define | [ESP\_I2CEXT0\_SDA\_OUT](#aabf1378b0ad2028c36c3bb74c81d7049)   90 |
| #define | [ESP\_I2CEXT1\_SCL\_IN](#a1b6324b294e9e018a5909427f4f0ba36)   91 |
| #define | [ESP\_I2CEXT1\_SCL\_OUT](#a3ac49ff21fcb59eeab6350821f9107e5)   91 |
| #define | [ESP\_I2CEXT1\_SDA\_IN](#abb571ec9f2a59fc281837ca8bd3f2daa)   92 |
| #define | [ESP\_I2CEXT1\_SDA\_OUT](#a3922109459dfd033147e4daf1ed4cd32)   92 |
| #define | [ESP\_GPIO\_SD0\_OUT](#ae59035f8269ccd564ba0d7b2b078b3ee)   93 |
| #define | [ESP\_GPIO\_SD1\_OUT](#a3fbed77581ed14fa077f314e812b9c36)   94 |
| #define | [ESP\_GPIO\_SD2\_OUT](#a2668d9083ce28563cc160fe1102e927d)   95 |
| #define | [ESP\_GPIO\_SD3\_OUT](#a9d34f616894f98d7175c41b4ba565f8d)   96 |
| #define | [ESP\_GPIO\_SD4\_OUT](#aa88cedc2785b1e25a21ac70dd5603e68)   97 |
| #define | [ESP\_GPIO\_SD5\_OUT](#af0841a01cf24e79a447daa58a48db9f8)   98 |
| #define | [ESP\_GPIO\_SD6\_OUT](#a8c16952c92f5b28cd39b99771ccb983b)   99 |
| #define | [ESP\_GPIO\_SD7\_OUT](#a7fd22ae53413e708e4b75ad57e1be34a)   100 |
| #define | [ESP\_FSPICLK\_IN](#ade88988460c131e8c6775794588b0eb8)   101 |
| #define | [ESP\_FSPICLK\_OUT](#ab8c5397dc530f6326c3d10b31e59e168)   101 |
| #define | [ESP\_FSPIQ\_IN](#ab603b7bf7d016e85653a5c3be5c01293)   102 |
| #define | [ESP\_FSPIQ\_OUT](#a8b3ea6ad374fa010b46b48072fa87ccb)   102 |
| #define | [ESP\_FSPID\_IN](#a7910521af840d42edd3c0a667cf90c5f)   103 |
| #define | [ESP\_FSPID\_OUT](#a02bd34821e8a4bf0038b9af417ec161a)   103 |
| #define | [ESP\_FSPIHD\_IN](#a60ff087a3d85a356d77f060a6698d00b)   104 |
| #define | [ESP\_FSPIHD\_OUT](#ac71bc137b93bd6c0c8a1ebe24a70a613)   104 |
| #define | [ESP\_FSPIWP\_IN](#a4d4c4a13b820cab6d94da8fe08120a2f)   105 |
| #define | [ESP\_FSPIWP\_OUT](#a83c4f18d726984cc98caeea9b7677ca1)   105 |
| #define | [ESP\_FSPIIO4\_IN](#af751015894fa1cefd780d4c483ed4fe0)   106 |
| #define | [ESP\_FSPIIO4\_OUT](#a5131d3b8c5f15927eb1ab5f5c5831fc7)   106 |
| #define | [ESP\_FSPIIO5\_IN](#aa422ee46d7a699a5de5acfce23544f1b)   107 |
| #define | [ESP\_FSPIIO5\_OUT](#a846120bb034a5178b719de7566af36e9)   107 |
| #define | [ESP\_FSPIIO6\_IN](#afbba101fa32685cf54ff6579245c232b)   108 |
| #define | [ESP\_FSPIIO6\_OUT](#acb72c9ac62375b2ef22c4895fd5c37e9)   108 |
| #define | [ESP\_FSPIIO7\_IN](#a7be0c3215d8ab00a4a87dcf4798207d9)   109 |
| #define | [ESP\_FSPIIO7\_OUT](#a796dc85ea60a5cce0d0c184805164587)   109 |
| #define | [ESP\_FSPICS0\_IN](#a96ca1328e76337d289f6e65faf33d75c)   110 |
| #define | [ESP\_FSPICS0\_OUT](#ad1be1401b282275eaef46b9a598c6a40)   110 |
| #define | [ESP\_FSPICS1\_OUT](#a44ade9179a7ea00586359a009799661d)   111 |
| #define | [ESP\_FSPICS2\_OUT](#af991963f29c5b268a5f8fead8fd15348)   112 |
| #define | [ESP\_FSPICS3\_OUT](#a65d1170c5a68ac7f6a4457c3380ddfde)   113 |
| #define | [ESP\_FSPICS4\_OUT](#a83dafe68703c701dcd07d7ff0aadad01)   114 |
| #define | [ESP\_FSPICS5\_OUT](#ad8fab64bb220fd198a6cd931f4ea1e8e)   115 |
| #define | [ESP\_TWAI\_RX](#ab3da303c2f9226f9648669c17af8377a)   116 |
| #define | [ESP\_TWAI\_TX](#a3b13bb40583aaa0f85de982509247614)   116 |
| #define | [ESP\_TWAI\_BUS\_OFF\_ON](#a6d0d41d1ec0f6fc626861f5857684e6d)   117 |
| #define | [ESP\_TWAI\_CLKOUT](#a1c69791269fdbb2a11f66f33eb4066be)   118 |
| #define | [ESP\_SUBSPICLK\_OUT](#a8fd6be50bb328dfd4ac0943f015b29ee)   119 |
| #define | [ESP\_SUBSPIQ\_IN](#af80ecb5fcd6c02cb5b73478198abef3c)   120 |
| #define | [ESP\_SUBSPIQ\_OUT](#ac75fd67f54d49449451c4924c0b7910a)   120 |
| #define | [ESP\_SUBSPID\_IN](#a0c924000fccdb7ce112822db720dbd8d)   121 |
| #define | [ESP\_SUBSPID\_OUT](#a3b9cab35f71697419266c71583f8a087)   121 |
| #define | [ESP\_SUBSPIHD\_IN](#a9a04da28895e846359a3ea89391b21f6)   122 |
| #define | [ESP\_SUBSPIHD\_OUT](#ab1f7e54d6230ceabc3fee083aab409d1)   122 |
| #define | [ESP\_SUBSPIWP\_IN](#a3c4b2938ef6753d76a752bf9a973de52)   123 |
| #define | [ESP\_SUBSPIWP\_OUT](#a7493ab9a1f0dc10902ce412055579842)   123 |
| #define | [ESP\_SUBSPICS0\_OUT](#a8925d5f830a4bc5ca6114dc06bae3b1f)   124 |
| #define | [ESP\_SUBSPICS1\_OUT](#add0fa80736d0fe196872bb0664c433d4)   125 |
| #define | [ESP\_FSPIDQS\_OUT](#a83baa98d81f816f19e65aafb26f15a3c)   126 |
| #define | [ESP\_SPI3\_CS2\_OUT](#a9e4bf0b0eff43b1f56f17abe22ef24a5)   127 |
| #define | [ESP\_I2S0O\_SD1\_OUT](#a6ab543889d74aa62a4ba609788223f0e)   128 |
| #define | [ESP\_CORE1\_GPIO\_IN0](#a214e2e05cf729479901dd03626ef045e)   129 |
| #define | [ESP\_CORE1\_GPIO\_OUT0](#a1128c2ee52835afdd4ed37ddd94a7a4b)   129 |
| #define | [ESP\_CORE1\_GPIO\_IN1](#a504eadf86e54f9b4c46461374691a567)   130 |
| #define | [ESP\_CORE1\_GPIO\_OUT1](#a82296bbe122bc077945b4dbfd0b27f0d)   130 |
| #define | [ESP\_CORE1\_GPIO\_IN2](#a0f84aadaf4ce6e95434bcd16402158e7)   131 |
| #define | [ESP\_CORE1\_GPIO\_OUT2](#a8b92c91dce2faa4708790c5841c90697)   131 |
| #define | [ESP\_LCD\_CS](#a53a3c23cc0db2b293fda78a6e24545f5)   132 |
| #define | [ESP\_CAM\_DATA\_IN0](#a257ff9bb2ab23b5c9437aa3ae5a8a3a8)   133 |
| #define | [ESP\_LCD\_DATA\_OUT0](#a4f4ff1e21ce7c144e4de031bd42208df)   133 |
| #define | [ESP\_CAM\_DATA\_IN1](#a07a2ceeafe386815dce64e074bc5170b)   134 |
| #define | [ESP\_LCD\_DATA\_OUT1](#a50ed74e778b2a5d5609c29f02f7919d8)   134 |
| #define | [ESP\_CAM\_DATA\_IN2](#ab505f36dbabfd33302db8e231506ec1f)   135 |
| #define | [ESP\_LCD\_DATA\_OUT2](#ad32f77d444995d69e6097d67a5bfacc6)   135 |
| #define | [ESP\_CAM\_DATA\_IN3](#a816bdba373a9d604c148465de08e5793)   136 |
| #define | [ESP\_LCD\_DATA\_OUT3](#a5498b1c545ef91644eaf806325cf7b75)   136 |
| #define | [ESP\_CAM\_DATA\_IN4](#af45144723ca836d01cc79653c4ed44db)   137 |
| #define | [ESP\_LCD\_DATA\_OUT4](#aaa486e7766ddf6954395fdfa23a002bb)   137 |
| #define | [ESP\_CAM\_DATA\_IN5](#af32e65a96dbdcc6f0fa8f17de746b083)   138 |
| #define | [ESP\_LCD\_DATA\_OUT5](#a8f2afaff6454b563b4f6d451034b6bf0)   138 |
| #define | [ESP\_CAM\_DATA\_IN6](#a50bc310217f80e7c592308b0f1e448db)   139 |
| #define | [ESP\_LCD\_DATA\_OUT6](#a921738f261a92792cdaa2cd307502a82)   139 |
| #define | [ESP\_CAM\_DATA\_IN7](#abf73b074dfa771a96a2814f7385c5488)   140 |
| #define | [ESP\_LCD\_DATA\_OUT7](#a2d468c66d6983fbf32bfe0785430a061)   140 |
| #define | [ESP\_CAM\_DATA\_IN8](#a1c77a6730f4bd3ea99b6c062fe801fe1)   141 |
| #define | [ESP\_LCD\_DATA\_OUT8](#ab8d40e58dfd6843f6ddd8731bc3500a7)   141 |
| #define | [ESP\_CAM\_DATA\_IN9](#ad998205ac3c496a8da706c36c6b03dab)   142 |
| #define | [ESP\_LCD\_DATA\_OUT9](#a80649e927dfb699d57d1510d41c77dbf)   142 |
| #define | [ESP\_CAM\_DATA\_IN10](#ad9fc1117b68eba7f5c68551ea1f654d4)   143 |
| #define | [ESP\_LCD\_DATA\_OUT10](#a1181a8301f7b156843f2fa9fcde46ab6)   143 |
| #define | [ESP\_CAM\_DATA\_IN11](#a277093423ffbc1a658d00e5c70edaf43)   144 |
| #define | [ESP\_LCD\_DATA\_OUT11](#a9961daf1b1830c71d5219292ec0b3408)   144 |
| #define | [ESP\_CAM\_DATA\_IN12](#a6be5ed7bad735d0b1f6d548e4baccdfe)   145 |
| #define | [ESP\_LCD\_DATA\_OUT12](#a4ce4d9b69a4972d5811c7b786dd6a087)   145 |
| #define | [ESP\_CAM\_DATA\_IN13](#af575322753a44a6d16bdc9ae057edf94)   146 |
| #define | [ESP\_LCD\_DATA\_OUT13](#a10f62d5ec7fb095c718de9ffc25badac)   146 |
| #define | [ESP\_CAM\_DATA\_IN14](#a5a532d5b315a7285e453988b6e4850da)   147 |
| #define | [ESP\_LCD\_DATA\_OUT14](#aa5733e97bf116dcf3e824dd5ced97d86)   147 |
| #define | [ESP\_CAM\_DATA\_IN15](#a85d788e027a99a1bd235b92919290c08)   148 |
| #define | [ESP\_LCD\_DATA\_OUT15](#a680877bfb8fae097b7878c1547609f6e)   148 |
| #define | [ESP\_CAM\_PCLK](#a692105d3da3d5b8c329052eb83822647)   149 |
| #define | [ESP\_CAM\_CLK](#aaae230831f580a9da491c02880d27bed)   149 |
| #define | [ESP\_CAM\_H\_ENABLE](#a61768a98e2410b1db7b1f7d6a1d899a2)   150 |
| #define | [ESP\_LCD\_H\_ENABLE](#a997c1262b9e18006dc512b22bef27c55)   150 |
| #define | [ESP\_CAM\_H\_SYNC](#a7fe4c5732cae0c8744c8fe4dff9d8789)   151 |
| #define | [ESP\_LCD\_H\_SYNC](#a97e85278e1c6c4b9557608961aafa0db)   151 |
| #define | [ESP\_CAM\_V\_SYNC](#a360710b489ab8657418b55ec18f78281)   152 |
| #define | [ESP\_LCD\_V\_SYNC](#ac88307d440dd2d45896a25e89c8e7f82)   152 |
| #define | [ESP\_LCD\_DC](#a6a8af909a6c89460fa74ca7c295b74d2)   153 |
| #define | [ESP\_LCD\_PCLK](#a39d94c85937af83a1bb2c32cc85dfd26)   154 |
| #define | [ESP\_SUBSPID4\_IN](#aae7066cb62b74cf5e8f64f84bd76ee49)   155 |
| #define | [ESP\_SUBSPID4\_OUT](#aa716d46da29da6affd5fa8851a730f3f)   155 |
| #define | [ESP\_SUBSPID5\_IN](#a051cd2450520fd4abc6f288c8577a12c)   156 |
| #define | [ESP\_SUBSPID5\_OUT](#aece7dc6fc4bca1bd73d9ba856eb0f3fe)   156 |
| #define | [ESP\_SUBSPID6\_IN](#a6d49162b17a1a7cd3f2446c6ca8192ec)   157 |
| #define | [ESP\_SUBSPID6\_OUT](#ab3e8db3219bf7aa7b2503a1fe759d60c)   157 |
| #define | [ESP\_SUBSPID7\_IN](#a34b9a22e0f55a0534199e62b1eaff5b0)   158 |
| #define | [ESP\_SUBSPID7\_OUT](#adb8c01bf2361a8b24e79cf048a7e6535)   158 |
| #define | [ESP\_SUBSPIDQS\_IN](#a6ccb6e41ab48fba76302068ee4433fb8)   159 |
| #define | [ESP\_SUBSPIDQS\_OUT](#a608345dcd6c90e4f19427bb38161501a)   159 |
| #define | [ESP\_PWM0\_SYNC0\_IN](#a60a3fe70a1bc5ba71cb46df782901087)   160 |
| #define | [ESP\_PWM0\_OUT0A](#a9397a79a46feab488c88552013790dfc)   160 |
| #define | [ESP\_PWM0\_SYNC1\_IN](#aca616afbb64ed37982624503545a5a72)   161 |
| #define | [ESP\_PWM0\_OUT0B](#acb3badfaed73f7069ea23dde375db62a)   161 |
| #define | [ESP\_PWM0\_SYNC2\_IN](#a2017681d630abc75e7298c12b86a62ce)   162 |
| #define | [ESP\_PWM0\_OUT1A](#ae52e5bd4be5563caeb9861267e41d947)   162 |
| #define | [ESP\_PWM0\_F0\_IN](#a4a503a957b2fd76f257534b80069caa2)   163 |
| #define | [ESP\_PWM0\_OUT1B](#a9fa8e944ff2d960c141f8375c9aa0b0e)   163 |
| #define | [ESP\_PWM0\_F1\_IN](#af536ae867a3d8bcb7644b48c346b4b50)   164 |
| #define | [ESP\_PWM0\_OUT2A](#abf74a2a32a8c36431e2f21d6cd15a610)   164 |
| #define | [ESP\_PWM0\_F2\_IN](#a83f385e6b8a99314cc641083a203322b)   165 |
| #define | [ESP\_PWM0\_OUT2B](#a563105deedf9f7ed6818ab9a8a8aecdc)   165 |
| #define | [ESP\_PWM0\_CAP0\_IN](#a421b59e20586b4f48b7e81bfa0ad4357)   166 |
| #define | [ESP\_PWM1\_OUT0A](#a4f8f7187a2a8dbf4b104e3a7e7bd5dae)   166 |
| #define | [ESP\_PWM0\_CAP1\_IN](#aea7a8712f1502df47721258470ff5b48)   167 |
| #define | [ESP\_PWM1\_OUT0B](#a553561934aa817659a5c781dfeccfc3e)   167 |
| #define | [ESP\_PWM0\_CAP2\_IN](#ab221240161be67a0f5af577494c8a5ad)   168 |
| #define | [ESP\_PWM1\_OUT1A](#a852f0b23fd2c3d2f90b6bcfccd5f375e)   168 |
| #define | [ESP\_PWM1\_SYNC0\_IN](#a9f251384f8a6a10b0fb173c4bfda88ba)   169 |
| #define | [ESP\_PWM1\_OUT1B](#ab9bc2ae5e0e53935f8b58380dfd397e8)   169 |
| #define | [ESP\_PWM1\_SYNC1\_IN](#a646d7d644b5d4ec403eab7ff793cf7b2)   170 |
| #define | [ESP\_PWM1\_OUT2A](#a8beedf183380bfe83c435f9c5920215e)   170 |
| #define | [ESP\_PWM1\_SYNC2\_IN](#a56a67f8e168a4e7545e3ca4bcf7c8d89)   171 |
| #define | [ESP\_PWM1\_OUT2B](#ae1976c33c4e94a76d09ee5c3aa93f04e)   171 |
| #define | [ESP\_PWM1\_F0\_IN](#a09c262c332e65ccc9eb2d91d976958e3)   172 |
| #define | [ESP\_SDHOST\_CCLK\_OUT\_1](#aff5857c7ef89e0ff32bbb49e393ea003)   172 |
| #define | [ESP\_PWM1\_F1\_IN](#af4b1c0ff4e222f09eee18cbb85cedb67)   173 |
| #define | [ESP\_SDHOST\_CCLK\_OUT\_2](#a00c0010ef6f14d2fa3b374f682dd0b46)   173 |
| #define | [ESP\_PWM1\_F2\_IN](#ac911f11a68e10d359cffe49864739e2d)   174 |
| #define | [ESP\_SDHOST\_RST\_N\_1](#abeb145776728098f097fd5a3a9b89132)   174 |
| #define | [ESP\_PWM1\_CAP0\_IN](#a8f2dcd1f46c2a5a5da3be188dca9e3a0)   175 |
| #define | [ESP\_SDHOST\_RST\_N\_2](#a0536f51d9a6adba1138304fa758db39a)   175 |
| #define | [ESP\_PWM1\_CAP1\_IN](#a8b97c639d66dcb8400aefc344bf490d1)   176 |
| #define | [ESP\_SDHOST\_CCMD\_OD\_PULLUP\_EN\_N176](#ae9e1e3a249d4fa5f330de8b0d0920a75) |
| #define | [ESP\_PWM1\_CAP2\_IN](#a23b8540974bcf9dbd5c0ff92d9b69ac9)   177 |
| #define | [ESP\_SDIO\_TOHOST\_INT\_OUT](#aac3529b76d29e57ad20500c9d1da23f3)   177 |
| #define | [ESP\_SDHOST\_CCMD\_IN\_1](#aa99bd561249d2e1eb4344f298873f503)   178 |
| #define | [ESP\_SDHOST\_CCMD\_OUT\_1](#a5f1a59ccefd8e2388338627978e44059)   178 |
| #define | [ESP\_SDHOST\_CCMD\_IN\_2](#a041fd8cb426a95f145725f246201dacd)   179 |
| #define | [ESP\_SDHOST\_CCMD\_OUT\_2](#a3122a431d37d337935ce459ce2826a5e)   179 |
| #define | [ESP\_SDHOST\_CDATA\_IN\_10](#aa202d8a403ae5dac9a51f66dcc899815)   180 |
| #define | [ESP\_SDHOST\_CDATA\_OUT\_10](#a650be8be910f36d892d2af6b903abe6e)   180 |
| #define | [ESP\_SDHOST\_CDATA\_IN\_11](#a4518625593104880441b0d405eeb9d79)   181 |
| #define | [ESP\_SDHOST\_CDATA\_OUT\_11](#a4e2d79ab775783efc0cdf86115331447)   181 |
| #define | [ESP\_SDHOST\_CDATA\_IN\_12](#abf24ff245054912561d51db5d248770b)   182 |
| #define | [ESP\_SDHOST\_CDATA\_OUT\_12](#ace4ef14e4a0d7b0c28199eb8e837136e)   182 |
| #define | [ESP\_SDHOST\_CDATA\_IN\_13](#a250805f95412af52d358f90ab2ff9cab)   183 |
| #define | [ESP\_SDHOST\_CDATA\_OUT\_13](#a1b9425434296a84ae20e5138e99f3cc7)   183 |
| #define | [ESP\_SDHOST\_CDATA\_IN\_14](#a5aec6c17086301750c3ff542f784c73c)   184 |
| #define | [ESP\_SDHOST\_CDATA\_OUT\_14](#af720ace3a3c5109b440201c529ab9f68)   184 |
| #define | [ESP\_SDHOST\_CDATA\_IN\_15](#a511407191c4f58e59f19d0cbd527f940)   185 |
| #define | [ESP\_SDHOST\_CDATA\_OUT\_15](#a627e3a4e12df8e358d937bbabcaa8eb0)   185 |
| #define | [ESP\_SDHOST\_CDATA\_IN\_16](#ada2bd9384398308507f1827c187e5dd6)   186 |
| #define | [ESP\_SDHOST\_CDATA\_OUT\_16](#a502ca14944ee4d93aabcba4eafa0d900)   186 |
| #define | [ESP\_SDHOST\_CDATA\_IN\_17](#af12e58d00a8085cbafcac751b5a90705)   187 |
| #define | [ESP\_SDHOST\_CDATA\_OUT\_17](#ab695d377e135cac2283bc1c915396494)   187 |
| #define | [ESP\_PCMFSYNC\_IN](#a0ad409b608ef2a418098b4e51d0e7e9a)   188 |
| #define | [ESP\_BT\_AUDIO0\_IRQ](#afd2befcf5eb0c413c0f8447558dc4863)   188 |
| #define | [ESP\_PCMCLK\_IN](#abb4d1f28362c68cf3f1e9f1696602b03)   189 |
| #define | [ESP\_BT\_AUDIO1\_IRQ](#acfe665b9ff21a51b93819a3f123180ad)   189 |
| #define | [ESP\_PCMDIN](#ae94f8dfc2be2c0cf8863a33df76d5295)   190 |
| #define | [ESP\_BT\_AUDIO2\_IRQ](#a77ac554a2a10fc6fa77106e8af9dfc86)   190 |
| #define | [ESP\_RW\_WAKEUP\_REQ](#a7abc844342f6483be73ea503d3f76d89)   191 |
| #define | [ESP\_BLE\_AUDIO0\_IRQ](#ab2e25b779a18acd66533795433291a3d)   191 |
| #define | [ESP\_SDHOST\_DATA\_STROBE\_1](#a13b46bfbdddc6ceedbb30b0f0dc6be5d)   192 |
| #define | [ESP\_BLE\_AUDIO1\_IRQ](#ab4b3d654c674536c2c63070210147372)   192 |
| #define | [ESP\_SDHOST\_DATA\_STROBE\_2](#a209b7dd99039e60f032ac234c14e4c9d)   193 |
| #define | [ESP\_BLE\_AUDIO2\_IRQ](#a637ea6fcad7b2e5fe48cf9e3419fbed6)   193 |
| #define | [ESP\_SDHOST\_CARD\_DETECT\_N\_1](#af3a093b62bef7d1da43e168abee9823b)   194 |
| #define | [ESP\_PCMFSYNC\_OUT](#a8b79d6e15573a684058c9b933f469f09)   194 |
| #define | [ESP\_SDHOST\_CARD\_DETECT\_N\_2](#ab42e6528593924d759ee03f41faa88e9)   195 |
| #define | [ESP\_PCMCLK\_OUT](#a500651ca0d6daa86774a0f45190f8b38)   195 |
| #define | [ESP\_SDHOST\_CARD\_WRITE\_PRT\_1](#a90ed679e9630feb28030c0c1995b85f7)   196 |
| #define | [ESP\_PCMDOUT](#ab3ecd7e5557112172c38bff3b2605e9c)   196 |
| #define | [ESP\_SDHOST\_CARD\_WRITE\_PRT\_2](#a1bc9c1d813aa85230ea95c190145d9bf)   197 |
| #define | [ESP\_BLE\_AUDIO\_SYNC0\_P](#aba2aea8feedc96a0a6b3bba007df49ac)   197 |
| #define | [ESP\_SDHOST\_CARD\_INT\_N\_1](#ad6288e71dadae26fee5cb658c967254e)   198 |
| #define | [ESP\_BLE\_AUDIO\_SYNC1\_P](#a21e5bf1c7c33a39f11d8bf6537ed85bb)   198 |
| #define | [ESP\_SDHOST\_CARD\_INT\_N\_2](#accd3ea038126b88448f33984bd058427)   199 |
| #define | [ESP\_BLE\_AUDIO\_SYNC2\_P](#a961f37a0b2dcb9e183331ef5684f8504)   199 |
| #define | [ESP\_ANT\_SEL0](#aec2dfb198f69d923686404a0a6330833)   200 |
| #define | [ESP\_ANT\_SEL1](#a15c080ea1e4c8e2db9f1640e9b8c4f0a)   201 |
| #define | [ESP\_ANT\_SEL2](#ae3042ff86ecc0f2e78ebe9477055e819)   202 |
| #define | [ESP\_ANT\_SEL3](#ab8e5cca4b9eb1a7bda7868ecd792c76d)   203 |
| #define | [ESP\_ANT\_SEL4](#a821cc4b81f76043b1ecb751118a2f416)   204 |
| #define | [ESP\_ANT\_SEL5](#a28a954881fd9d5f5e7ff25d715f0bcc2)   205 |
| #define | [ESP\_ANT\_SEL6](#a2122dad1966cbe214e9c82cb9a46bd8a)   206 |
| #define | [ESP\_ANT\_SEL7](#a8f9cedf15c49cee3fbac2a22df7675ec)   207 |
| #define | [ESP\_SIG\_IN\_FUNC\_208](#a5e192de902e66cccd6ec3c72ed8ef82a)   208 |
| #define | [ESP\_SIG\_IN\_FUNC208](#a0f6d8766907b91e60e62ae29c5e4b558)   208 |
| #define | [ESP\_SIG\_IN\_FUNC\_209](#a240123ea7ff1b64a70d1bb4866fe174b)   209 |
| #define | [ESP\_SIG\_IN\_FUNC209](#a8fe491023178ce16dd57edae3bdfe87f)   209 |
| #define | [ESP\_SIG\_IN\_FUNC\_210](#a09fe402e83b28df1927599b5daa0b700)   210 |
| #define | [ESP\_SIG\_IN\_FUNC210](#add709f3eecdbe328426cd93013c80c3e)   210 |
| #define | [ESP\_SIG\_IN\_FUNC\_211](#a38bfce1eb51e0913355a02e67d0d1496)   211 |
| #define | [ESP\_SIG\_IN\_FUNC211](#aa286ed797d5ab072404cda4eca929566)   211 |
| #define | [ESP\_SIG\_IN\_FUNC\_212](#ab5f2a06dab84e52c93b6a25172e7b2c4)   212 |
| #define | [ESP\_SIG\_IN\_FUNC212](#a8f25ba37edb68eb23e64395280ab791a)   212 |
| #define | [ESP\_SDHOST\_CDATA\_IN\_20](#a13ca361ff287a452bcdc24992448e59e)   213 |
| #define | [ESP\_SDHOST\_CDATA\_OUT\_20](#a06f93230a36ef5287147a0564b1dfed1)   213 |
| #define | [ESP\_SDHOST\_CDATA\_IN\_21](#ab4c0aef79106c2d286f6d4bce99bd9eb)   214 |
| #define | [ESP\_SDHOST\_CDATA\_OUT\_21](#a6c9f531502c69bcd5889d60837ec0bdb)   214 |
| #define | [ESP\_SDHOST\_CDATA\_IN\_22](#a5e4da4ac40cff37134d19032640fa253)   215 |
| #define | [ESP\_SDHOST\_CDATA\_OUT\_22](#a786692b41d500d85fe88ee63d8e60fd5)   215 |
| #define | [ESP\_SDHOST\_CDATA\_IN\_23](#aae5dec0fc3b263f26798bdfed1122a18)   216 |
| #define | [ESP\_SDHOST\_CDATA\_OUT\_23](#a98324b90550b28d722cb38a3dd122532)   216 |
| #define | [ESP\_SDHOST\_CDATA\_IN\_24](#a098ad3a54b47ed40202ae8c2a9b6f7ec)   217 |
| #define | [ESP\_SDHOST\_CDATA\_OUT\_24](#a6898cbd2b727b76e5208cbc1a102b2a2)   217 |
| #define | [ESP\_SDHOST\_CDATA\_IN\_25](#a22d372ec349ce449aba06bf85cc1c1b5)   218 |
| #define | [ESP\_SDHOST\_CDATA\_OUT\_25](#a638507475f38120dbd76db6f53455f57)   218 |
| #define | [ESP\_SDHOST\_CDATA\_IN\_26](#af78c9aa8fc70487f561271635ff63b64)   219 |
| #define | [ESP\_SDHOST\_CDATA\_OUT\_26](#a492c8431649dc6c429347d9a041a23cd)   219 |
| #define | [ESP\_SDHOST\_CDATA\_IN\_27](#a2177168014217dcc8625d64f4d79e7e2)   220 |
| #define | [ESP\_SDHOST\_CDATA\_OUT\_27](#aece0df9752dd44b35534bda1251c484d)   220 |
| #define | [ESP\_PRO\_ALONEGPIO\_IN0](#a9023b22f85edc25ab88db9f3fb025c4e)   221 |
| #define | [ESP\_PRO\_ALONEGPIO\_OUT0](#ae833440baa7073fbfb51ec80ff728ce5)   221 |
| #define | [ESP\_PRO\_ALONEGPIO\_IN1](#a5e4c12a21678930c86e15cbb6d920767)   222 |
| #define | [ESP\_PRO\_ALONEGPIO\_OUT1](#a5b3065b35c32286fe5ca8d68c033b162)   222 |
| #define | [ESP\_PRO\_ALONEGPIO\_IN2](#a8b82dbe07c785060d2190a13e1fe21ee)   223 |
| #define | [ESP\_PRO\_ALONEGPIO\_OUT2](#a287e800e3fb52dd3b6949e6d185f413c)   223 |
| #define | [ESP\_PRO\_ALONEGPIO\_IN3](#a5f8a8f6143c1552eec5862ce248ca496)   224 |
| #define | [ESP\_PRO\_ALONEGPIO\_OUT3](#a49f220c0a7cae6a580174355a80b2b56)   224 |
| #define | [ESP\_PRO\_ALONEGPIO\_IN4](#ad8ca1006a71cdd738cca02eaf9f923d6)   225 |
| #define | [ESP\_PRO\_ALONEGPIO\_OUT4](#ac1b762f9e0ad1cb60c1e16b0cf7aae0a)   225 |
| #define | [ESP\_PRO\_ALONEGPIO\_IN5](#aa1b04ac7997451778d7fdbb4f00b0114)   226 |
| #define | [ESP\_PRO\_ALONEGPIO\_OUT5](#a5f237780803395dd97bb8306a14dbc92)   226 |
| #define | [ESP\_PRO\_ALONEGPIO\_IN6](#a525900ed7a103a14105afb6ef8caca69)   227 |
| #define | [ESP\_PRO\_ALONEGPIO\_OUT6](#a4cbc6a3551e057f1d943b01c120317f4)   227 |
| #define | [ESP\_PRO\_ALONEGPIO\_IN7](#af6ebbb44bcb763355964ac39293cd1c4)   228 |
| #define | [ESP\_PRO\_ALONEGPIO\_OUT7](#a3d1993f51138a3ccf8ef913e1863f3bd)   228 |
| #define | [ESP\_SYNCERR](#a0206456525cd6dc235ed6892e98731c6)   229 |
| #define | [ESP\_SYNCFOUND\_FLAG](#aa62bd8539c4d89abaa542d8bd4c91efd)   230 |
| #define | [ESP\_EVT\_CNTL\_IMMEDIATE\_ABORT](#ade4ee47d8f72c009686b2454ee77ee60)   231 |
| #define | [ESP\_LINKLBL](#ac5684072c6c5fbbdb6631d73270819dc)   232 |
| #define | [ESP\_DATA\_EN](#a1029a66c0538d7eb1026ced27d54a59b)   233 |
| #define | [ESP\_DATA](#a04dc693cfec6739602b92e86a837c58d)   234 |
| #define | [ESP\_PKT\_TX\_ON](#aecac02e2195c5da81f63ed4c19bd06fb)   235 |
| #define | [ESP\_PKT\_RX\_ON](#a63f7ec6fc7927b0f0fb3bd0dc733de5a)   236 |
| #define | [ESP\_RW\_TX\_ON](#a3b8a7f22861948aa8809aa58ecbdb0ef)   237 |
| #define | [ESP\_RW\_RX\_ON](#a5f93eee3354e5fd70d11fd26c9dd25bb)   238 |
| #define | [ESP\_EVT\_REQ\_P](#af7d8fb5a97cb0e4f3dad1a73fb0610d5)   239 |
| #define | [ESP\_EVT\_STOP\_P](#a10fd19b9a6140fea7e88facaa02686be)   240 |
| #define | [ESP\_BT\_MODE\_ON](#a08a40a396cf075e77aa50acfb811885a)   241 |
| #define | [ESP\_GPIO\_LC\_DIAG0](#a80a3804720f2e69ac5caa52c0ade9d5b)   242 |
| #define | [ESP\_GPIO\_LC\_DIAG1](#ad842d1a31efaf5f3edc70326ac89df9b)   243 |
| #define | [ESP\_GPIO\_LC\_DIAG2](#ad23ea4680ce2cbf713bb456dae84e35b)   244 |
| #define | [ESP\_CH](#a83ab157d422c3004c3dc287c0c804ec5)   245 |
| #define | [ESP\_RX\_WINDOW](#a546d9b83cad2a5b2e64677be087b1f9d)   246 |
| #define | [ESP\_UPDATE\_RX](#a25d03cedd231864f508e405d0ae2fa4b)   247 |
| #define | [ESP\_RX\_STATUS](#ac2450d1a096d1adf2386ba91e0a92f75)   248 |
| #define | [ESP\_CLK\_GPIO](#ae27ee8b3a05b497ec7bea2ed69fc9230)   249 |
| #define | [ESP\_NBT\_BLE](#a9aa8b294d23efae4cd5a6dd741829aad)   250 |
| #define | [ESP\_USB\_JTAG\_TDO\_BRIDGE](#a6b5babfcba4d025bdd1ab709b569fdf2)   251 |
| #define | [ESP\_USB\_JTAG\_TRST](#a4358434232f1f3515d8f5f4961d77520)   251 |
| #define | [ESP\_CORE1\_GPIO\_IN3](#af08fab550c96147c3b1c54ca41eac3b4)   252 |
| #define | [ESP\_CORE1\_GPIO\_OUT3](#a132a8965b837c561f6ec1f0d15bf39cb)   252 |
| #define | [ESP\_CORE1\_GPIO\_IN4](#a830e2f2adc5bf86a4080fa64e7435beb)   253 |
| #define | [ESP\_CORE1\_GPIO\_OUT4](#af8e3c657135901ead83da1c58079bae5)   253 |
| #define | [ESP\_CORE1\_GPIO\_IN5](#adb0166f5083f37eb82469fbab88eb21b)   254 |
| #define | [ESP\_CORE1\_GPIO\_OUT5](#a09461b98dd020d78786ce01c244fda54)   254 |
| #define | [ESP\_CORE1\_GPIO\_IN6](#a765b233e0f1e7dc50424e895dc7ba930)   255 |
| #define | [ESP\_CORE1\_GPIO\_OUT6](#ac087a21dd9d6a84b6bd6f885d02bf0c9)   255 |
| #define | [ESP\_SIG\_GPIO\_OUT](#a645411759ffdc63f51f2cd42632d2720)   256 |
| #define | [ESP\_GPIO\_MAP\_DATE](#afe5c166b887709cdd27bd37df85c45b9)   0x1907040 |

## Macro Definition Documentation

## [◆ ](#aec2dfb198f69d923686404a0a6330833)ESP\_ANT\_SEL0

| #define ESP\_ANT\_SEL0   200 |
| --- |

## [◆ ](#a15c080ea1e4c8e2db9f1640e9b8c4f0a)ESP\_ANT\_SEL1

| #define ESP\_ANT\_SEL1   201 |
| --- |

## [◆ ](#ae3042ff86ecc0f2e78ebe9477055e819)ESP\_ANT\_SEL2

| #define ESP\_ANT\_SEL2   202 |
| --- |

## [◆ ](#ab8e5cca4b9eb1a7bda7868ecd792c76d)ESP\_ANT\_SEL3

| #define ESP\_ANT\_SEL3   203 |
| --- |

## [◆ ](#a821cc4b81f76043b1ecb751118a2f416)ESP\_ANT\_SEL4

| #define ESP\_ANT\_SEL4   204 |
| --- |

## [◆ ](#a28a954881fd9d5f5e7ff25d715f0bcc2)ESP\_ANT\_SEL5

| #define ESP\_ANT\_SEL5   205 |
| --- |

## [◆ ](#a2122dad1966cbe214e9c82cb9a46bd8a)ESP\_ANT\_SEL6

| #define ESP\_ANT\_SEL6   206 |
| --- |

## [◆ ](#a8f9cedf15c49cee3fbac2a22df7675ec)ESP\_ANT\_SEL7

| #define ESP\_ANT\_SEL7   207 |
| --- |

## [◆ ](#a304bc90cc758f90f6675fea611ab0cfe)ESP\_BB\_DIAG0

| #define ESP\_BB\_DIAG0   35 |
| --- |

## [◆ ](#ad236bf991329914d59c194ff9003974a)ESP\_BB\_DIAG1

| #define ESP\_BB\_DIAG1   36 |
| --- |

## [◆ ](#aed67caee00b7ceaaaa33b2917aba60f2)ESP\_BB\_DIAG10

| #define ESP\_BB\_DIAG10   45 |
| --- |

## [◆ ](#aef4bb5d62b93dfc3f2834404b6945b90)ESP\_BB\_DIAG11

| #define ESP\_BB\_DIAG11   46 |
| --- |

## [◆ ](#acc6cd70ce139a5639022bec896a3ba5e)ESP\_BB\_DIAG12

| #define ESP\_BB\_DIAG12   47 |
| --- |

## [◆ ](#afa72089303bf662a4efc8c068b157f0d)ESP\_BB\_DIAG13

| #define ESP\_BB\_DIAG13   48 |
| --- |

## [◆ ](#a4ef00458e2547f7141741191b92854d8)ESP\_BB\_DIAG14

| #define ESP\_BB\_DIAG14   49 |
| --- |

## [◆ ](#aed7c06883c6a69303a341454aff409ed)ESP\_BB\_DIAG15

| #define ESP\_BB\_DIAG15   50 |
| --- |

## [◆ ](#a1acc29dd7c0517c30299e71c1a6ce7fa)ESP\_BB\_DIAG16

| #define ESP\_BB\_DIAG16   51 |
| --- |

## [◆ ](#a9abbf3178088e44d984b088f53c25ab1)ESP\_BB\_DIAG17

| #define ESP\_BB\_DIAG17   52 |
| --- |

## [◆ ](#af75798fba81841339510ecc5f94e542e)ESP\_BB\_DIAG18

| #define ESP\_BB\_DIAG18   53 |
| --- |

## [◆ ](#a26c20261a5e2f4293b81c802a0a33b19)ESP\_BB\_DIAG2

| #define ESP\_BB\_DIAG2   37 |
| --- |

## [◆ ](#a5124ef75b703e7805bccd8c93828faae)ESP\_BB\_DIAG3

| #define ESP\_BB\_DIAG3   38 |
| --- |

## [◆ ](#aebd2c37b71d18967bd394b32c820647f)ESP\_BB\_DIAG4

| #define ESP\_BB\_DIAG4   39 |
| --- |

## [◆ ](#ace166b18a74fb8a42f876d1aa7cfb059)ESP\_BB\_DIAG5

| #define ESP\_BB\_DIAG5   40 |
| --- |

## [◆ ](#ad5685b19c170cc428cea0ee91f9155b0)ESP\_BB\_DIAG6

| #define ESP\_BB\_DIAG6   41 |
| --- |

## [◆ ](#aedf32208932dfe4471f6a5a7feb652f8)ESP\_BB\_DIAG7

| #define ESP\_BB\_DIAG7   42 |
| --- |

## [◆ ](#a126e2108473183890c6a2e148f8fd2c7)ESP\_BB\_DIAG8

| #define ESP\_BB\_DIAG8   43 |
| --- |

## [◆ ](#a75b60b1b4d53e6fca02b3a4f14ea530e)ESP\_BB\_DIAG9

| #define ESP\_BB\_DIAG9   44 |
| --- |

## [◆ ](#ab2e25b779a18acd66533795433291a3d)ESP\_BLE\_AUDIO0\_IRQ

| #define ESP\_BLE\_AUDIO0\_IRQ   191 |
| --- |

## [◆ ](#ab4b3d654c674536c2c63070210147372)ESP\_BLE\_AUDIO1\_IRQ

| #define ESP\_BLE\_AUDIO1\_IRQ   192 |
| --- |

## [◆ ](#a637ea6fcad7b2e5fe48cf9e3419fbed6)ESP\_BLE\_AUDIO2\_IRQ

| #define ESP\_BLE\_AUDIO2\_IRQ   193 |
| --- |

## [◆ ](#aba2aea8feedc96a0a6b3bba007df49ac)ESP\_BLE\_AUDIO\_SYNC0\_P

| #define ESP\_BLE\_AUDIO\_SYNC0\_P   197 |
| --- |

## [◆ ](#a21e5bf1c7c33a39f11d8bf6537ed85bb)ESP\_BLE\_AUDIO\_SYNC1\_P

| #define ESP\_BLE\_AUDIO\_SYNC1\_P   198 |
| --- |

## [◆ ](#a961f37a0b2dcb9e183331ef5684f8504)ESP\_BLE\_AUDIO\_SYNC2\_P

| #define ESP\_BLE\_AUDIO\_SYNC2\_P   199 |
| --- |

## [◆ ](#afd2befcf5eb0c413c0f8447558dc4863)ESP\_BT\_AUDIO0\_IRQ

| #define ESP\_BT\_AUDIO0\_IRQ   188 |
| --- |

## [◆ ](#acfe665b9ff21a51b93819a3f123180ad)ESP\_BT\_AUDIO1\_IRQ

| #define ESP\_BT\_AUDIO1\_IRQ   189 |
| --- |

## [◆ ](#a77ac554a2a10fc6fa77106e8af9dfc86)ESP\_BT\_AUDIO2\_IRQ

| #define ESP\_BT\_AUDIO2\_IRQ   190 |
| --- |

## [◆ ](#a08a40a396cf075e77aa50acfb811885a)ESP\_BT\_MODE\_ON

| #define ESP\_BT\_MODE\_ON   241 |
| --- |

## [◆ ](#aaae230831f580a9da491c02880d27bed)ESP\_CAM\_CLK

| #define ESP\_CAM\_CLK   149 |
| --- |

## [◆ ](#a257ff9bb2ab23b5c9437aa3ae5a8a3a8)ESP\_CAM\_DATA\_IN0

| #define ESP\_CAM\_DATA\_IN0   133 |
| --- |

## [◆ ](#a07a2ceeafe386815dce64e074bc5170b)ESP\_CAM\_DATA\_IN1

| #define ESP\_CAM\_DATA\_IN1   134 |
| --- |

## [◆ ](#ad9fc1117b68eba7f5c68551ea1f654d4)ESP\_CAM\_DATA\_IN10

| #define ESP\_CAM\_DATA\_IN10   143 |
| --- |

## [◆ ](#a277093423ffbc1a658d00e5c70edaf43)ESP\_CAM\_DATA\_IN11

| #define ESP\_CAM\_DATA\_IN11   144 |
| --- |

## [◆ ](#a6be5ed7bad735d0b1f6d548e4baccdfe)ESP\_CAM\_DATA\_IN12

| #define ESP\_CAM\_DATA\_IN12   145 |
| --- |

## [◆ ](#af575322753a44a6d16bdc9ae057edf94)ESP\_CAM\_DATA\_IN13

| #define ESP\_CAM\_DATA\_IN13   146 |
| --- |

## [◆ ](#a5a532d5b315a7285e453988b6e4850da)ESP\_CAM\_DATA\_IN14

| #define ESP\_CAM\_DATA\_IN14   147 |
| --- |

## [◆ ](#a85d788e027a99a1bd235b92919290c08)ESP\_CAM\_DATA\_IN15

| #define ESP\_CAM\_DATA\_IN15   148 |
| --- |

## [◆ ](#ab505f36dbabfd33302db8e231506ec1f)ESP\_CAM\_DATA\_IN2

| #define ESP\_CAM\_DATA\_IN2   135 |
| --- |

## [◆ ](#a816bdba373a9d604c148465de08e5793)ESP\_CAM\_DATA\_IN3

| #define ESP\_CAM\_DATA\_IN3   136 |
| --- |

## [◆ ](#af45144723ca836d01cc79653c4ed44db)ESP\_CAM\_DATA\_IN4

| #define ESP\_CAM\_DATA\_IN4   137 |
| --- |

## [◆ ](#af32e65a96dbdcc6f0fa8f17de746b083)ESP\_CAM\_DATA\_IN5

| #define ESP\_CAM\_DATA\_IN5   138 |
| --- |

## [◆ ](#a50bc310217f80e7c592308b0f1e448db)ESP\_CAM\_DATA\_IN6

| #define ESP\_CAM\_DATA\_IN6   139 |
| --- |

## [◆ ](#abf73b074dfa771a96a2814f7385c5488)ESP\_CAM\_DATA\_IN7

| #define ESP\_CAM\_DATA\_IN7   140 |
| --- |

## [◆ ](#a1c77a6730f4bd3ea99b6c062fe801fe1)ESP\_CAM\_DATA\_IN8

| #define ESP\_CAM\_DATA\_IN8   141 |
| --- |

## [◆ ](#ad998205ac3c496a8da706c36c6b03dab)ESP\_CAM\_DATA\_IN9

| #define ESP\_CAM\_DATA\_IN9   142 |
| --- |

## [◆ ](#a61768a98e2410b1db7b1f7d6a1d899a2)ESP\_CAM\_H\_ENABLE

| #define ESP\_CAM\_H\_ENABLE   150 |
| --- |

## [◆ ](#a7fe4c5732cae0c8744c8fe4dff9d8789)ESP\_CAM\_H\_SYNC

| #define ESP\_CAM\_H\_SYNC   151 |
| --- |

## [◆ ](#a692105d3da3d5b8c329052eb83822647)ESP\_CAM\_PCLK

| #define ESP\_CAM\_PCLK   149 |
| --- |

## [◆ ](#a360710b489ab8657418b55ec18f78281)ESP\_CAM\_V\_SYNC

| #define ESP\_CAM\_V\_SYNC   152 |
| --- |

## [◆ ](#a83ab157d422c3004c3dc287c0c804ec5)ESP\_CH

| #define ESP\_CH   245 |
| --- |

## [◆ ](#ae27ee8b3a05b497ec7bea2ed69fc9230)ESP\_CLK\_GPIO

| #define ESP\_CLK\_GPIO   249 |
| --- |

## [◆ ](#a214e2e05cf729479901dd03626ef045e)ESP\_CORE1\_GPIO\_IN0

| #define ESP\_CORE1\_GPIO\_IN0   129 |
| --- |

## [◆ ](#a504eadf86e54f9b4c46461374691a567)ESP\_CORE1\_GPIO\_IN1

| #define ESP\_CORE1\_GPIO\_IN1   130 |
| --- |

## [◆ ](#a0f84aadaf4ce6e95434bcd16402158e7)ESP\_CORE1\_GPIO\_IN2

| #define ESP\_CORE1\_GPIO\_IN2   131 |
| --- |

## [◆ ](#af08fab550c96147c3b1c54ca41eac3b4)ESP\_CORE1\_GPIO\_IN3

| #define ESP\_CORE1\_GPIO\_IN3   252 |
| --- |

## [◆ ](#a830e2f2adc5bf86a4080fa64e7435beb)ESP\_CORE1\_GPIO\_IN4

| #define ESP\_CORE1\_GPIO\_IN4   253 |
| --- |

## [◆ ](#adb0166f5083f37eb82469fbab88eb21b)ESP\_CORE1\_GPIO\_IN5

| #define ESP\_CORE1\_GPIO\_IN5   254 |
| --- |

## [◆ ](#a765b233e0f1e7dc50424e895dc7ba930)ESP\_CORE1\_GPIO\_IN6

| #define ESP\_CORE1\_GPIO\_IN6   255 |
| --- |

## [◆ ](#ae07a10a5b5f791d98034a0ffcaa0a5c1)ESP\_CORE1\_GPIO\_IN7

| #define ESP\_CORE1\_GPIO\_IN7   54 |
| --- |

## [◆ ](#a1128c2ee52835afdd4ed37ddd94a7a4b)ESP\_CORE1\_GPIO\_OUT0

| #define ESP\_CORE1\_GPIO\_OUT0   129 |
| --- |

## [◆ ](#a82296bbe122bc077945b4dbfd0b27f0d)ESP\_CORE1\_GPIO\_OUT1

| #define ESP\_CORE1\_GPIO\_OUT1   130 |
| --- |

## [◆ ](#a8b92c91dce2faa4708790c5841c90697)ESP\_CORE1\_GPIO\_OUT2

| #define ESP\_CORE1\_GPIO\_OUT2   131 |
| --- |

## [◆ ](#a132a8965b837c561f6ec1f0d15bf39cb)ESP\_CORE1\_GPIO\_OUT3

| #define ESP\_CORE1\_GPIO\_OUT3   252 |
| --- |

## [◆ ](#af8e3c657135901ead83da1c58079bae5)ESP\_CORE1\_GPIO\_OUT4

| #define ESP\_CORE1\_GPIO\_OUT4   253 |
| --- |

## [◆ ](#a09461b98dd020d78786ce01c244fda54)ESP\_CORE1\_GPIO\_OUT5

| #define ESP\_CORE1\_GPIO\_OUT5   254 |
| --- |

## [◆ ](#ac087a21dd9d6a84b6bd6f885d02bf0c9)ESP\_CORE1\_GPIO\_OUT6

| #define ESP\_CORE1\_GPIO\_OUT6   255 |
| --- |

## [◆ ](#ac9744120f941e282f182bf4b16b31a34)ESP\_CORE1\_GPIO\_OUT7

| #define ESP\_CORE1\_GPIO\_OUT7   54 |
| --- |

## [◆ ](#a04dc693cfec6739602b92e86a837c58d)ESP\_DATA

| #define ESP\_DATA   234 |
| --- |

## [◆ ](#a1029a66c0538d7eb1026ced27d54a59b)ESP\_DATA\_EN

| #define ESP\_DATA\_EN   233 |
| --- |

## [◆ ](#ade4ee47d8f72c009686b2454ee77ee60)ESP\_EVT\_CNTL\_IMMEDIATE\_ABORT

| #define ESP\_EVT\_CNTL\_IMMEDIATE\_ABORT   231 |
| --- |

## [◆ ](#af7d8fb5a97cb0e4f3dad1a73fb0610d5)ESP\_EVT\_REQ\_P

| #define ESP\_EVT\_REQ\_P   239 |
| --- |

## [◆ ](#a10fd19b9a6140fea7e88facaa02686be)ESP\_EVT\_STOP\_P

| #define ESP\_EVT\_STOP\_P   240 |
| --- |

## [◆ ](#ae49b4527d8fbd0f5c8e3edc72704c54a)ESP\_EXT\_ADC\_START

| #define ESP\_EXT\_ADC\_START   73 |
| --- |

## [◆ ](#ade88988460c131e8c6775794588b0eb8)ESP\_FSPICLK\_IN

| #define ESP\_FSPICLK\_IN   101 |
| --- |

## [◆ ](#ab8c5397dc530f6326c3d10b31e59e168)ESP\_FSPICLK\_OUT

| #define ESP\_FSPICLK\_OUT   101 |
| --- |

## [◆ ](#a96ca1328e76337d289f6e65faf33d75c)ESP\_FSPICS0\_IN

| #define ESP\_FSPICS0\_IN   110 |
| --- |

## [◆ ](#ad1be1401b282275eaef46b9a598c6a40)ESP\_FSPICS0\_OUT

| #define ESP\_FSPICS0\_OUT   110 |
| --- |

## [◆ ](#a44ade9179a7ea00586359a009799661d)ESP\_FSPICS1\_OUT

| #define ESP\_FSPICS1\_OUT   111 |
| --- |

## [◆ ](#af991963f29c5b268a5f8fead8fd15348)ESP\_FSPICS2\_OUT

| #define ESP\_FSPICS2\_OUT   112 |
| --- |

## [◆ ](#a65d1170c5a68ac7f6a4457c3380ddfde)ESP\_FSPICS3\_OUT

| #define ESP\_FSPICS3\_OUT   113 |
| --- |

## [◆ ](#a83dafe68703c701dcd07d7ff0aadad01)ESP\_FSPICS4\_OUT

| #define ESP\_FSPICS4\_OUT   114 |
| --- |

## [◆ ](#ad8fab64bb220fd198a6cd931f4ea1e8e)ESP\_FSPICS5\_OUT

| #define ESP\_FSPICS5\_OUT   115 |
| --- |

## [◆ ](#a7910521af840d42edd3c0a667cf90c5f)ESP\_FSPID\_IN

| #define ESP\_FSPID\_IN   103 |
| --- |

## [◆ ](#a02bd34821e8a4bf0038b9af417ec161a)ESP\_FSPID\_OUT

| #define ESP\_FSPID\_OUT   103 |
| --- |

## [◆ ](#a83baa98d81f816f19e65aafb26f15a3c)ESP\_FSPIDQS\_OUT

| #define ESP\_FSPIDQS\_OUT   126 |
| --- |

## [◆ ](#a60ff087a3d85a356d77f060a6698d00b)ESP\_FSPIHD\_IN

| #define ESP\_FSPIHD\_IN   104 |
| --- |

## [◆ ](#ac71bc137b93bd6c0c8a1ebe24a70a613)ESP\_FSPIHD\_OUT

| #define ESP\_FSPIHD\_OUT   104 |
| --- |

## [◆ ](#af751015894fa1cefd780d4c483ed4fe0)ESP\_FSPIIO4\_IN

| #define ESP\_FSPIIO4\_IN   106 |
| --- |

## [◆ ](#a5131d3b8c5f15927eb1ab5f5c5831fc7)ESP\_FSPIIO4\_OUT

| #define ESP\_FSPIIO4\_OUT   106 |
| --- |

## [◆ ](#aa422ee46d7a699a5de5acfce23544f1b)ESP\_FSPIIO5\_IN

| #define ESP\_FSPIIO5\_IN   107 |
| --- |

## [◆ ](#a846120bb034a5178b719de7566af36e9)ESP\_FSPIIO5\_OUT

| #define ESP\_FSPIIO5\_OUT   107 |
| --- |

## [◆ ](#afbba101fa32685cf54ff6579245c232b)ESP\_FSPIIO6\_IN

| #define ESP\_FSPIIO6\_IN   108 |
| --- |

## [◆ ](#acb72c9ac62375b2ef22c4895fd5c37e9)ESP\_FSPIIO6\_OUT

| #define ESP\_FSPIIO6\_OUT   108 |
| --- |

## [◆ ](#a7be0c3215d8ab00a4a87dcf4798207d9)ESP\_FSPIIO7\_IN

| #define ESP\_FSPIIO7\_IN   109 |
| --- |

## [◆ ](#a796dc85ea60a5cce0d0c184805164587)ESP\_FSPIIO7\_OUT

| #define ESP\_FSPIIO7\_OUT   109 |
| --- |

## [◆ ](#ab603b7bf7d016e85653a5c3be5c01293)ESP\_FSPIQ\_IN

| #define ESP\_FSPIQ\_IN   102 |
| --- |

## [◆ ](#a8b3ea6ad374fa010b46b48072fa87ccb)ESP\_FSPIQ\_OUT

| #define ESP\_FSPIQ\_OUT   102 |
| --- |

## [◆ ](#a4d4c4a13b820cab6d94da8fe08120a2f)ESP\_FSPIWP\_IN

| #define ESP\_FSPIWP\_IN   105 |
| --- |

## [◆ ](#a83c4f18d726984cc98caeea9b7677ca1)ESP\_FSPIWP\_OUT

| #define ESP\_FSPIWP\_OUT   105 |
| --- |

## [◆ ](#a47d854bfae0f88dc023613e61e6be551)ESP\_GPIO\_BT\_ACTIVE

| #define ESP\_GPIO\_BT\_ACTIVE   49 |
| --- |

## [◆ ](#ab8d0a9090c64518af59274603f035042)ESP\_GPIO\_BT\_PRIORITY

| #define ESP\_GPIO\_BT\_PRIORITY   50 |
| --- |

## [◆ ](#a80a3804720f2e69ac5caa52c0ade9d5b)ESP\_GPIO\_LC\_DIAG0

| #define ESP\_GPIO\_LC\_DIAG0   242 |
| --- |

## [◆ ](#ad842d1a31efaf5f3edc70326ac89df9b)ESP\_GPIO\_LC\_DIAG1

| #define ESP\_GPIO\_LC\_DIAG1   243 |
| --- |

## [◆ ](#ad23ea4680ce2cbf713bb456dae84e35b)ESP\_GPIO\_LC\_DIAG2

| #define ESP\_GPIO\_LC\_DIAG2   244 |
| --- |

## [◆ ](#afe5c166b887709cdd27bd37df85c45b9)ESP\_GPIO\_MAP\_DATE

| #define ESP\_GPIO\_MAP\_DATE   0x1907040 |
| --- |

## [◆ ](#ae59035f8269ccd564ba0d7b2b078b3ee)ESP\_GPIO\_SD0\_OUT

| #define ESP\_GPIO\_SD0\_OUT   93 |
| --- |

## [◆ ](#a3fbed77581ed14fa077f314e812b9c36)ESP\_GPIO\_SD1\_OUT

| #define ESP\_GPIO\_SD1\_OUT   94 |
| --- |

## [◆ ](#a2668d9083ce28563cc160fe1102e927d)ESP\_GPIO\_SD2\_OUT

| #define ESP\_GPIO\_SD2\_OUT   95 |
| --- |

## [◆ ](#a9d34f616894f98d7175c41b4ba565f8d)ESP\_GPIO\_SD3\_OUT

| #define ESP\_GPIO\_SD3\_OUT   96 |
| --- |

## [◆ ](#aa88cedc2785b1e25a21ac70dd5603e68)ESP\_GPIO\_SD4\_OUT

| #define ESP\_GPIO\_SD4\_OUT   97 |
| --- |

## [◆ ](#af0841a01cf24e79a447daa58a48db9f8)ESP\_GPIO\_SD5\_OUT

| #define ESP\_GPIO\_SD5\_OUT   98 |
| --- |

## [◆ ](#a8c16952c92f5b28cd39b99771ccb983b)ESP\_GPIO\_SD6\_OUT

| #define ESP\_GPIO\_SD6\_OUT   99 |
| --- |

## [◆ ](#a7fd22ae53413e708e4b75ad57e1be34a)ESP\_GPIO\_SD7\_OUT

| #define ESP\_GPIO\_SD7\_OUT   100 |
| --- |

## [◆ ](#af675ca03172d2dcee1e19ccb5236e087)ESP\_GPIO\_WLAN\_ACTIVE

| #define ESP\_GPIO\_WLAN\_ACTIVE   34 |
| --- |

## [◆ ](#adf2824b1611032a81fe7b3c41253c0d8)ESP\_GPIO\_WLAN\_PRIO

| #define ESP\_GPIO\_WLAN\_PRIO   33 |
| --- |

## [◆ ](#ab607ce367da34ab0f1bd7fa648273cf1)ESP\_I2CEXT0\_SCL\_IN

| #define ESP\_I2CEXT0\_SCL\_IN   89 |
| --- |

## [◆ ](#a2144cc62df795547ccf2bbe3ee4c629f)ESP\_I2CEXT0\_SCL\_OUT

| #define ESP\_I2CEXT0\_SCL\_OUT   89 |
| --- |

## [◆ ](#afa7061c87135b9dabe5c54f5f4ce16e6)ESP\_I2CEXT0\_SDA\_IN

| #define ESP\_I2CEXT0\_SDA\_IN   90 |
| --- |

## [◆ ](#aabf1378b0ad2028c36c3bb74c81d7049)ESP\_I2CEXT0\_SDA\_OUT

| #define ESP\_I2CEXT0\_SDA\_OUT   90 |
| --- |

## [◆ ](#a1b6324b294e9e018a5909427f4f0ba36)ESP\_I2CEXT1\_SCL\_IN

| #define ESP\_I2CEXT1\_SCL\_IN   91 |
| --- |

## [◆ ](#a3ac49ff21fcb59eeab6350821f9107e5)ESP\_I2CEXT1\_SCL\_OUT

| #define ESP\_I2CEXT1\_SCL\_OUT   91 |
| --- |

## [◆ ](#abb571ec9f2a59fc281837ca8bd3f2daa)ESP\_I2CEXT1\_SDA\_IN

| #define ESP\_I2CEXT1\_SDA\_IN   92 |
| --- |

## [◆ ](#a3922109459dfd033147e4daf1ed4cd32)ESP\_I2CEXT1\_SDA\_OUT

| #define ESP\_I2CEXT1\_SDA\_OUT   92 |
| --- |

## [◆ ](#a329858f11621f706f0a933886246e177)ESP\_I2S0\_MCLK\_IN

| #define ESP\_I2S0\_MCLK\_IN   23 |
| --- |

## [◆ ](#acd2f3e9c21da61b98fdc86b8a264d9fd)ESP\_I2S0\_MCLK\_OUT

| #define ESP\_I2S0\_MCLK\_OUT   23 |
| --- |

## [◆ ](#a67905afbcda699d20d8a05a8a66411af)ESP\_I2S0I\_BCK\_IN

| #define ESP\_I2S0I\_BCK\_IN   26 |
| --- |

## [◆ ](#abe571a9bad2c0e95049afd8e67c8d158)ESP\_I2S0I\_BCK\_OUT

| #define ESP\_I2S0I\_BCK\_OUT   26 |
| --- |

## [◆ ](#a9ae165cac1d30c38270f8747caa18f00)ESP\_I2S0I\_SD1\_IN

| #define ESP\_I2S0I\_SD1\_IN   51 |
| --- |

## [◆ ](#a5e4fdb79d8fefa835118c21fe6b05cb5)ESP\_I2S0I\_SD2\_IN

| #define ESP\_I2S0I\_SD2\_IN   52 |
| --- |

## [◆ ](#a39f410a33a8ddc30a37de7d0b5ff821d)ESP\_I2S0I\_SD3\_IN

| #define ESP\_I2S0I\_SD3\_IN   53 |
| --- |

## [◆ ](#a8e920eb744585bdec4b5ca8c6a6ec7b6)ESP\_I2S0I\_SD\_IN

| #define ESP\_I2S0I\_SD\_IN   25 |
| --- |

## [◆ ](#a4236f62ac75d5f2d56f7b1cc941d7509)ESP\_I2S0I\_WS\_IN

| #define ESP\_I2S0I\_WS\_IN   27 |
| --- |

## [◆ ](#af039bdc8eec9ec95d3ed2bbebabb22cb)ESP\_I2S0I\_WS\_OUT

| #define ESP\_I2S0I\_WS\_OUT   27 |
| --- |

## [◆ ](#af0b9626d6b7cfd5b5c42a8127897d565)ESP\_I2S0O\_BCK\_IN

| #define ESP\_I2S0O\_BCK\_IN   22 |
| --- |

## [◆ ](#a2e76c532bd75a6af4790b30f58c4b8e9)ESP\_I2S0O\_BCK\_OUT

| #define ESP\_I2S0O\_BCK\_OUT   22 |
| --- |

## [◆ ](#a6ab543889d74aa62a4ba609788223f0e)ESP\_I2S0O\_SD1\_OUT

| #define ESP\_I2S0O\_SD1\_OUT   128 |
| --- |

## [◆ ](#a9e263a786610ffa2b60051a03188b67b)ESP\_I2S0O\_SD\_OUT

| #define ESP\_I2S0O\_SD\_OUT   25 |
| --- |

## [◆ ](#aad13d05d8d50227859d484deaaf6e34b)ESP\_I2S0O\_WS\_IN

| #define ESP\_I2S0O\_WS\_IN   24 |
| --- |

## [◆ ](#a78693c10e4ac17973e7ac12c1bdf8c97)ESP\_I2S0O\_WS\_OUT

| #define ESP\_I2S0O\_WS\_OUT   24 |
| --- |

## [◆ ](#af00f358d0012d5a4e85a0610f9da2ace)ESP\_I2S1\_MCLK\_IN

| #define ESP\_I2S1\_MCLK\_IN   21 |
| --- |

## [◆ ](#aeeb2b00d8b3172832532d96b2282d4d2)ESP\_I2S1\_MCLK\_OUT

| #define ESP\_I2S1\_MCLK\_OUT   21 |
| --- |

## [◆ ](#a537fd0715c03fd03d914d72d01191b9a)ESP\_I2S1I\_BCK\_IN

| #define ESP\_I2S1I\_BCK\_IN   31 |
| --- |

## [◆ ](#a93d4d6602af3ba29121fef124145f4a5)ESP\_I2S1I\_BCK\_OUT

| #define ESP\_I2S1I\_BCK\_OUT   31 |
| --- |

## [◆ ](#a854ae55e42905b005332084451ddf0ba)ESP\_I2S1I\_SD\_IN

| #define ESP\_I2S1I\_SD\_IN   30 |
| --- |

## [◆ ](#a90b7c81877f6ab8ec1af498db7b8dc0e)ESP\_I2S1I\_WS\_IN

| #define ESP\_I2S1I\_WS\_IN   32 |
| --- |

## [◆ ](#a1ed428a9dd21d57a7311c24f192e032e)ESP\_I2S1I\_WS\_OUT

| #define ESP\_I2S1I\_WS\_OUT   32 |
| --- |

## [◆ ](#afffede35b0effa00a9d6e1077ac4aaa2)ESP\_I2S1O\_BCK\_IN

| #define ESP\_I2S1O\_BCK\_IN   28 |
| --- |

## [◆ ](#afcd05d2cf345dcf816068b0b89ac5a72)ESP\_I2S1O\_BCK\_OUT

| #define ESP\_I2S1O\_BCK\_OUT   28 |
| --- |

## [◆ ](#aa97d280d714ad4284f617df4453bdcf6)ESP\_I2S1O\_SD\_OUT

| #define ESP\_I2S1O\_SD\_OUT   30 |
| --- |

## [◆ ](#a7ac95a35ee6001c340cddd1424f3fa5e)ESP\_I2S1O\_WS\_IN

| #define ESP\_I2S1O\_WS\_IN   29 |
| --- |

## [◆ ](#a84485bdfe1661269506f7ef1f70f4a87)ESP\_I2S1O\_WS\_OUT

| #define ESP\_I2S1O\_WS\_OUT   29 |
| --- |

## [◆ ](#a53a3c23cc0db2b293fda78a6e24545f5)ESP\_LCD\_CS

| #define ESP\_LCD\_CS   132 |
| --- |

## [◆ ](#a4f4ff1e21ce7c144e4de031bd42208df)ESP\_LCD\_DATA\_OUT0

| #define ESP\_LCD\_DATA\_OUT0   133 |
| --- |

## [◆ ](#a50ed74e778b2a5d5609c29f02f7919d8)ESP\_LCD\_DATA\_OUT1

| #define ESP\_LCD\_DATA\_OUT1   134 |
| --- |

## [◆ ](#a1181a8301f7b156843f2fa9fcde46ab6)ESP\_LCD\_DATA\_OUT10

| #define ESP\_LCD\_DATA\_OUT10   143 |
| --- |

## [◆ ](#a9961daf1b1830c71d5219292ec0b3408)ESP\_LCD\_DATA\_OUT11

| #define ESP\_LCD\_DATA\_OUT11   144 |
| --- |

## [◆ ](#a4ce4d9b69a4972d5811c7b786dd6a087)ESP\_LCD\_DATA\_OUT12

| #define ESP\_LCD\_DATA\_OUT12   145 |
| --- |

## [◆ ](#a10f62d5ec7fb095c718de9ffc25badac)ESP\_LCD\_DATA\_OUT13

| #define ESP\_LCD\_DATA\_OUT13   146 |
| --- |

## [◆ ](#aa5733e97bf116dcf3e824dd5ced97d86)ESP\_LCD\_DATA\_OUT14

| #define ESP\_LCD\_DATA\_OUT14   147 |
| --- |

## [◆ ](#a680877bfb8fae097b7878c1547609f6e)ESP\_LCD\_DATA\_OUT15

| #define ESP\_LCD\_DATA\_OUT15   148 |
| --- |

## [◆ ](#ad32f77d444995d69e6097d67a5bfacc6)ESP\_LCD\_DATA\_OUT2

| #define ESP\_LCD\_DATA\_OUT2   135 |
| --- |

## [◆ ](#a5498b1c545ef91644eaf806325cf7b75)ESP\_LCD\_DATA\_OUT3

| #define ESP\_LCD\_DATA\_OUT3   136 |
| --- |

## [◆ ](#aaa486e7766ddf6954395fdfa23a002bb)ESP\_LCD\_DATA\_OUT4

| #define ESP\_LCD\_DATA\_OUT4   137 |
| --- |

## [◆ ](#a8f2afaff6454b563b4f6d451034b6bf0)ESP\_LCD\_DATA\_OUT5

| #define ESP\_LCD\_DATA\_OUT5   138 |
| --- |

## [◆ ](#a921738f261a92792cdaa2cd307502a82)ESP\_LCD\_DATA\_OUT6

| #define ESP\_LCD\_DATA\_OUT6   139 |
| --- |

## [◆ ](#a2d468c66d6983fbf32bfe0785430a061)ESP\_LCD\_DATA\_OUT7

| #define ESP\_LCD\_DATA\_OUT7   140 |
| --- |

## [◆ ](#ab8d40e58dfd6843f6ddd8731bc3500a7)ESP\_LCD\_DATA\_OUT8

| #define ESP\_LCD\_DATA\_OUT8   141 |
| --- |

## [◆ ](#a80649e927dfb699d57d1510d41c77dbf)ESP\_LCD\_DATA\_OUT9

| #define ESP\_LCD\_DATA\_OUT9   142 |
| --- |

## [◆ ](#a6a8af909a6c89460fa74ca7c295b74d2)ESP\_LCD\_DC

| #define ESP\_LCD\_DC   153 |
| --- |

## [◆ ](#a997c1262b9e18006dc512b22bef27c55)ESP\_LCD\_H\_ENABLE

| #define ESP\_LCD\_H\_ENABLE   150 |
| --- |

## [◆ ](#a97e85278e1c6c4b9557608961aafa0db)ESP\_LCD\_H\_SYNC

| #define ESP\_LCD\_H\_SYNC   151 |
| --- |

## [◆ ](#a39d94c85937af83a1bb2c32cc85dfd26)ESP\_LCD\_PCLK

| #define ESP\_LCD\_PCLK   154 |
| --- |

## [◆ ](#ac88307d440dd2d45896a25e89c8e7f82)ESP\_LCD\_V\_SYNC

| #define ESP\_LCD\_V\_SYNC   152 |
| --- |

## [◆ ](#a62dfcd88747c61acb53dc85c1751f1d3)ESP\_LEDC\_LS\_SIG\_OUT0

| #define ESP\_LEDC\_LS\_SIG\_OUT0   73 |
| --- |

## [◆ ](#a5cad9206cfeea93b42e5456228c7d580)ESP\_LEDC\_LS\_SIG\_OUT1

| #define ESP\_LEDC\_LS\_SIG\_OUT1   74 |
| --- |

## [◆ ](#ab408070e7c700805db165c3876b6c588)ESP\_LEDC\_LS\_SIG\_OUT2

| #define ESP\_LEDC\_LS\_SIG\_OUT2   75 |
| --- |

## [◆ ](#a438aee217c6c94a2962a3d98935b5717)ESP\_LEDC\_LS\_SIG\_OUT3

| #define ESP\_LEDC\_LS\_SIG\_OUT3   76 |
| --- |

## [◆ ](#ada93dcffffc15362be4b7432a8033559)ESP\_LEDC\_LS\_SIG\_OUT4

| #define ESP\_LEDC\_LS\_SIG\_OUT4   77 |
| --- |

## [◆ ](#a34fc029ec45756ca7064580f57db1cc7)ESP\_LEDC\_LS\_SIG\_OUT5

| #define ESP\_LEDC\_LS\_SIG\_OUT5   78 |
| --- |

## [◆ ](#a28b01adea7e0bcc8b76fe05d58c1cbd0)ESP\_LEDC\_LS\_SIG\_OUT6

| #define ESP\_LEDC\_LS\_SIG\_OUT6   79 |
| --- |

## [◆ ](#a2ea140f2da1a15b24dcaa3592909ca35)ESP\_LEDC\_LS\_SIG\_OUT7

| #define ESP\_LEDC\_LS\_SIG\_OUT7   80 |
| --- |

## [◆ ](#ac5684072c6c5fbbdb6631d73270819dc)ESP\_LINKLBL

| #define ESP\_LINKLBL   232 |
| --- |

## [◆ ](#a9aa8b294d23efae4cd5a6dd741829aad)ESP\_NBT\_BLE

| #define ESP\_NBT\_BLE   250 |
| --- |

## [◆ ](#af80260535bc3aee44c28c972a29483e0)ESP\_NOSIG

| #define ESP\_NOSIG   [ESP\_SIG\_INVAL](esp-pinctrl-common_8h.md#ae0d2e726ab8d90343e5c80e1d9b85ad8) |
| --- |

## [◆ ](#abb4d1f28362c68cf3f1e9f1696602b03)ESP\_PCMCLK\_IN

| #define ESP\_PCMCLK\_IN   189 |
| --- |

## [◆ ](#a500651ca0d6daa86774a0f45190f8b38)ESP\_PCMCLK\_OUT

| #define ESP\_PCMCLK\_OUT   195 |
| --- |

## [◆ ](#ae94f8dfc2be2c0cf8863a33df76d5295)ESP\_PCMDIN

| #define ESP\_PCMDIN   190 |
| --- |

## [◆ ](#ab3ecd7e5557112172c38bff3b2605e9c)ESP\_PCMDOUT

| #define ESP\_PCMDOUT   196 |
| --- |

## [◆ ](#a0ad409b608ef2a418098b4e51d0e7e9a)ESP\_PCMFSYNC\_IN

| #define ESP\_PCMFSYNC\_IN   188 |
| --- |

## [◆ ](#a8b79d6e15573a684058c9b933f469f09)ESP\_PCMFSYNC\_OUT

| #define ESP\_PCMFSYNC\_OUT   194 |
| --- |

## [◆ ](#a7e3c939b0b32332a35f0bead0aa4a2a6)ESP\_PCNT\_CTRL\_CH0\_IN0

| #define ESP\_PCNT\_CTRL\_CH0\_IN0   35 |
| --- |

## [◆ ](#a9ec8d490316b9f043fe5e9160a7cf7e0)ESP\_PCNT\_CTRL\_CH0\_IN1

| #define ESP\_PCNT\_CTRL\_CH0\_IN1   39 |
| --- |

## [◆ ](#a540cbfcd205911955effcc9814f9707c)ESP\_PCNT\_CTRL\_CH0\_IN2

| #define ESP\_PCNT\_CTRL\_CH0\_IN2   43 |
| --- |

## [◆ ](#a96e8bd4584ab671a1b0c3f0adb440943)ESP\_PCNT\_CTRL\_CH0\_IN3

| #define ESP\_PCNT\_CTRL\_CH0\_IN3   47 |
| --- |

## [◆ ](#a88c5eb5c7f4169ce3e7f7056b42989a7)ESP\_PCNT\_CTRL\_CH1\_IN0

| #define ESP\_PCNT\_CTRL\_CH1\_IN0   36 |
| --- |

## [◆ ](#a0bbfffdef085eb6cedc3d1232766cb38)ESP\_PCNT\_CTRL\_CH1\_IN1

| #define ESP\_PCNT\_CTRL\_CH1\_IN1   40 |
| --- |

## [◆ ](#abf6c210e19582b06e3d6c546a009ef5b)ESP\_PCNT\_CTRL\_CH1\_IN2

| #define ESP\_PCNT\_CTRL\_CH1\_IN2   44 |
| --- |

## [◆ ](#a0a926d350fc11d737b545c53b3ba1671)ESP\_PCNT\_CTRL\_CH1\_IN3

| #define ESP\_PCNT\_CTRL\_CH1\_IN3   48 |
| --- |

## [◆ ](#acf123456a5b9d94f370309ad39672e34)ESP\_PCNT\_SIG\_CH0\_IN0

| #define ESP\_PCNT\_SIG\_CH0\_IN0   33 |
| --- |

## [◆ ](#a99db3d1c4e07e11fc09a4024a54fcea6)ESP\_PCNT\_SIG\_CH0\_IN1

| #define ESP\_PCNT\_SIG\_CH0\_IN1   37 |
| --- |

## [◆ ](#a4f9e798a260fb6ac4c39262f20253244)ESP\_PCNT\_SIG\_CH0\_IN2

| #define ESP\_PCNT\_SIG\_CH0\_IN2   41 |
| --- |

## [◆ ](#acd8d20d89508b532a4e2749499263de3)ESP\_PCNT\_SIG\_CH0\_IN3

| #define ESP\_PCNT\_SIG\_CH0\_IN3   45 |
| --- |

## [◆ ](#a800813b2c23f7e4bb23e032e0802a459)ESP\_PCNT\_SIG\_CH1\_IN0

| #define ESP\_PCNT\_SIG\_CH1\_IN0   34 |
| --- |

## [◆ ](#a730113779d69ca86b257060678f8cbec)ESP\_PCNT\_SIG\_CH1\_IN1

| #define ESP\_PCNT\_SIG\_CH1\_IN1   38 |
| --- |

## [◆ ](#a38365b3f9a2b49ef2714c38d00d293c5)ESP\_PCNT\_SIG\_CH1\_IN2

| #define ESP\_PCNT\_SIG\_CH1\_IN2   42 |
| --- |

## [◆ ](#ac54a606ee7096db15cdb9453b04ac72d)ESP\_PCNT\_SIG\_CH1\_IN3

| #define ESP\_PCNT\_SIG\_CH1\_IN3   46 |
| --- |

## [◆ ](#a63f7ec6fc7927b0f0fb3bd0dc733de5a)ESP\_PKT\_RX\_ON

| #define ESP\_PKT\_RX\_ON   236 |
| --- |

## [◆ ](#aecac02e2195c5da81f63ed4c19bd06fb)ESP\_PKT\_TX\_ON

| #define ESP\_PKT\_TX\_ON   235 |
| --- |

## [◆ ](#a9023b22f85edc25ab88db9f3fb025c4e)ESP\_PRO\_ALONEGPIO\_IN0

| #define ESP\_PRO\_ALONEGPIO\_IN0   221 |
| --- |

## [◆ ](#a5e4c12a21678930c86e15cbb6d920767)ESP\_PRO\_ALONEGPIO\_IN1

| #define ESP\_PRO\_ALONEGPIO\_IN1   222 |
| --- |

## [◆ ](#a8b82dbe07c785060d2190a13e1fe21ee)ESP\_PRO\_ALONEGPIO\_IN2

| #define ESP\_PRO\_ALONEGPIO\_IN2   223 |
| --- |

## [◆ ](#a5f8a8f6143c1552eec5862ce248ca496)ESP\_PRO\_ALONEGPIO\_IN3

| #define ESP\_PRO\_ALONEGPIO\_IN3   224 |
| --- |

## [◆ ](#ad8ca1006a71cdd738cca02eaf9f923d6)ESP\_PRO\_ALONEGPIO\_IN4

| #define ESP\_PRO\_ALONEGPIO\_IN4   225 |
| --- |

## [◆ ](#aa1b04ac7997451778d7fdbb4f00b0114)ESP\_PRO\_ALONEGPIO\_IN5

| #define ESP\_PRO\_ALONEGPIO\_IN5   226 |
| --- |

## [◆ ](#a525900ed7a103a14105afb6ef8caca69)ESP\_PRO\_ALONEGPIO\_IN6

| #define ESP\_PRO\_ALONEGPIO\_IN6   227 |
| --- |

## [◆ ](#af6ebbb44bcb763355964ac39293cd1c4)ESP\_PRO\_ALONEGPIO\_IN7

| #define ESP\_PRO\_ALONEGPIO\_IN7   228 |
| --- |

## [◆ ](#ae833440baa7073fbfb51ec80ff728ce5)ESP\_PRO\_ALONEGPIO\_OUT0

| #define ESP\_PRO\_ALONEGPIO\_OUT0   221 |
| --- |

## [◆ ](#a5b3065b35c32286fe5ca8d68c033b162)ESP\_PRO\_ALONEGPIO\_OUT1

| #define ESP\_PRO\_ALONEGPIO\_OUT1   222 |
| --- |

## [◆ ](#a287e800e3fb52dd3b6949e6d185f413c)ESP\_PRO\_ALONEGPIO\_OUT2

| #define ESP\_PRO\_ALONEGPIO\_OUT2   223 |
| --- |

## [◆ ](#a49f220c0a7cae6a580174355a80b2b56)ESP\_PRO\_ALONEGPIO\_OUT3

| #define ESP\_PRO\_ALONEGPIO\_OUT3   224 |
| --- |

## [◆ ](#ac1b762f9e0ad1cb60c1e16b0cf7aae0a)ESP\_PRO\_ALONEGPIO\_OUT4

| #define ESP\_PRO\_ALONEGPIO\_OUT4   225 |
| --- |

## [◆ ](#a5f237780803395dd97bb8306a14dbc92)ESP\_PRO\_ALONEGPIO\_OUT5

| #define ESP\_PRO\_ALONEGPIO\_OUT5   226 |
| --- |

## [◆ ](#a4cbc6a3551e057f1d943b01c120317f4)ESP\_PRO\_ALONEGPIO\_OUT6

| #define ESP\_PRO\_ALONEGPIO\_OUT6   227 |
| --- |

## [◆ ](#a3d1993f51138a3ccf8ef913e1863f3bd)ESP\_PRO\_ALONEGPIO\_OUT7

| #define ESP\_PRO\_ALONEGPIO\_OUT7   228 |
| --- |

## [◆ ](#a421b59e20586b4f48b7e81bfa0ad4357)ESP\_PWM0\_CAP0\_IN

| #define ESP\_PWM0\_CAP0\_IN   166 |
| --- |

## [◆ ](#aea7a8712f1502df47721258470ff5b48)ESP\_PWM0\_CAP1\_IN

| #define ESP\_PWM0\_CAP1\_IN   167 |
| --- |

## [◆ ](#ab221240161be67a0f5af577494c8a5ad)ESP\_PWM0\_CAP2\_IN

| #define ESP\_PWM0\_CAP2\_IN   168 |
| --- |

## [◆ ](#a4a503a957b2fd76f257534b80069caa2)ESP\_PWM0\_F0\_IN

| #define ESP\_PWM0\_F0\_IN   163 |
| --- |

## [◆ ](#af536ae867a3d8bcb7644b48c346b4b50)ESP\_PWM0\_F1\_IN

| #define ESP\_PWM0\_F1\_IN   164 |
| --- |

## [◆ ](#a83f385e6b8a99314cc641083a203322b)ESP\_PWM0\_F2\_IN

| #define ESP\_PWM0\_F2\_IN   165 |
| --- |

## [◆ ](#a9397a79a46feab488c88552013790dfc)ESP\_PWM0\_OUT0A

| #define ESP\_PWM0\_OUT0A   160 |
| --- |

## [◆ ](#acb3badfaed73f7069ea23dde375db62a)ESP\_PWM0\_OUT0B

| #define ESP\_PWM0\_OUT0B   161 |
| --- |

## [◆ ](#ae52e5bd4be5563caeb9861267e41d947)ESP\_PWM0\_OUT1A

| #define ESP\_PWM0\_OUT1A   162 |
| --- |

## [◆ ](#a9fa8e944ff2d960c141f8375c9aa0b0e)ESP\_PWM0\_OUT1B

| #define ESP\_PWM0\_OUT1B   163 |
| --- |

## [◆ ](#abf74a2a32a8c36431e2f21d6cd15a610)ESP\_PWM0\_OUT2A

| #define ESP\_PWM0\_OUT2A   164 |
| --- |

## [◆ ](#a563105deedf9f7ed6818ab9a8a8aecdc)ESP\_PWM0\_OUT2B

| #define ESP\_PWM0\_OUT2B   165 |
| --- |

## [◆ ](#a60a3fe70a1bc5ba71cb46df782901087)ESP\_PWM0\_SYNC0\_IN

| #define ESP\_PWM0\_SYNC0\_IN   160 |
| --- |

## [◆ ](#aca616afbb64ed37982624503545a5a72)ESP\_PWM0\_SYNC1\_IN

| #define ESP\_PWM0\_SYNC1\_IN   161 |
| --- |

## [◆ ](#a2017681d630abc75e7298c12b86a62ce)ESP\_PWM0\_SYNC2\_IN

| #define ESP\_PWM0\_SYNC2\_IN   162 |
| --- |

## [◆ ](#a8f2dcd1f46c2a5a5da3be188dca9e3a0)ESP\_PWM1\_CAP0\_IN

| #define ESP\_PWM1\_CAP0\_IN   175 |
| --- |

## [◆ ](#a8b97c639d66dcb8400aefc344bf490d1)ESP\_PWM1\_CAP1\_IN

| #define ESP\_PWM1\_CAP1\_IN   176 |
| --- |

## [◆ ](#a23b8540974bcf9dbd5c0ff92d9b69ac9)ESP\_PWM1\_CAP2\_IN

| #define ESP\_PWM1\_CAP2\_IN   177 |
| --- |

## [◆ ](#a09c262c332e65ccc9eb2d91d976958e3)ESP\_PWM1\_F0\_IN

| #define ESP\_PWM1\_F0\_IN   172 |
| --- |

## [◆ ](#af4b1c0ff4e222f09eee18cbb85cedb67)ESP\_PWM1\_F1\_IN

| #define ESP\_PWM1\_F1\_IN   173 |
| --- |

## [◆ ](#ac911f11a68e10d359cffe49864739e2d)ESP\_PWM1\_F2\_IN

| #define ESP\_PWM1\_F2\_IN   174 |
| --- |

## [◆ ](#a4f8f7187a2a8dbf4b104e3a7e7bd5dae)ESP\_PWM1\_OUT0A

| #define ESP\_PWM1\_OUT0A   166 |
| --- |

## [◆ ](#a553561934aa817659a5c781dfeccfc3e)ESP\_PWM1\_OUT0B

| #define ESP\_PWM1\_OUT0B   167 |
| --- |

## [◆ ](#a852f0b23fd2c3d2f90b6bcfccd5f375e)ESP\_PWM1\_OUT1A

| #define ESP\_PWM1\_OUT1A   168 |
| --- |

## [◆ ](#ab9bc2ae5e0e53935f8b58380dfd397e8)ESP\_PWM1\_OUT1B

| #define ESP\_PWM1\_OUT1B   169 |
| --- |

## [◆ ](#a8beedf183380bfe83c435f9c5920215e)ESP\_PWM1\_OUT2A

| #define ESP\_PWM1\_OUT2A   170 |
| --- |

## [◆ ](#ae1976c33c4e94a76d09ee5c3aa93f04e)ESP\_PWM1\_OUT2B

| #define ESP\_PWM1\_OUT2B   171 |
| --- |

## [◆ ](#a9f251384f8a6a10b0fb173c4bfda88ba)ESP\_PWM1\_SYNC0\_IN

| #define ESP\_PWM1\_SYNC0\_IN   169 |
| --- |

## [◆ ](#a646d7d644b5d4ec403eab7ff793cf7b2)ESP\_PWM1\_SYNC1\_IN

| #define ESP\_PWM1\_SYNC1\_IN   170 |
| --- |

## [◆ ](#a56a67f8e168a4e7545e3ca4bcf7c8d89)ESP\_PWM1\_SYNC2\_IN

| #define ESP\_PWM1\_SYNC2\_IN   171 |
| --- |

## [◆ ](#ad9bae9b4884a356e465656d1ee8d61cd)ESP\_RMT\_SIG\_IN0

| #define ESP\_RMT\_SIG\_IN0   81 |
| --- |

## [◆ ](#ab6c6293e6845ba4bf4d05b84102ffdcf)ESP\_RMT\_SIG\_IN1

| #define ESP\_RMT\_SIG\_IN1   82 |
| --- |

## [◆ ](#af88ebdd0d2d02ac58d720c001ccc155b)ESP\_RMT\_SIG\_IN2

| #define ESP\_RMT\_SIG\_IN2   83 |
| --- |

## [◆ ](#a1f930cd82690248b839f16ff7738f32c)ESP\_RMT\_SIG\_IN3

| #define ESP\_RMT\_SIG\_IN3   84 |
| --- |

## [◆ ](#a25343fbc20a0c542bcdc21cdfade867b)ESP\_RMT\_SIG\_OUT0

| #define ESP\_RMT\_SIG\_OUT0   81 |
| --- |

## [◆ ](#a6d082fb1c7397d784a3075108e0dea73)ESP\_RMT\_SIG\_OUT1

| #define ESP\_RMT\_SIG\_OUT1   82 |
| --- |

## [◆ ](#ad657c1ddcf9c335ac7876464b80b2705)ESP\_RMT\_SIG\_OUT2

| #define ESP\_RMT\_SIG\_OUT2   83 |
| --- |

## [◆ ](#ae60033bb70ca9ff7c2b52368d24a8ab8)ESP\_RMT\_SIG\_OUT3

| #define ESP\_RMT\_SIG\_OUT3   84 |
| --- |

## [◆ ](#a5f93eee3354e5fd70d11fd26c9dd25bb)ESP\_RW\_RX\_ON

| #define ESP\_RW\_RX\_ON   238 |
| --- |

## [◆ ](#a3b8a7f22861948aa8809aa58ecbdb0ef)ESP\_RW\_TX\_ON

| #define ESP\_RW\_TX\_ON   237 |
| --- |

## [◆ ](#a7abc844342f6483be73ea503d3f76d89)ESP\_RW\_WAKEUP\_REQ

| #define ESP\_RW\_WAKEUP\_REQ   191 |
| --- |

## [◆ ](#ac2450d1a096d1adf2386ba91e0a92f75)ESP\_RX\_STATUS

| #define ESP\_RX\_STATUS   248 |
| --- |

## [◆ ](#a546d9b83cad2a5b2e64677be087b1f9d)ESP\_RX\_WINDOW

| #define ESP\_RX\_WINDOW   246 |
| --- |

## [◆ ](#af3a093b62bef7d1da43e168abee9823b)ESP\_SDHOST\_CARD\_DETECT\_N\_1

| #define ESP\_SDHOST\_CARD\_DETECT\_N\_1   194 |
| --- |

## [◆ ](#ab42e6528593924d759ee03f41faa88e9)ESP\_SDHOST\_CARD\_DETECT\_N\_2

| #define ESP\_SDHOST\_CARD\_DETECT\_N\_2   195 |
| --- |

## [◆ ](#ad6288e71dadae26fee5cb658c967254e)ESP\_SDHOST\_CARD\_INT\_N\_1

| #define ESP\_SDHOST\_CARD\_INT\_N\_1   198 |
| --- |

## [◆ ](#accd3ea038126b88448f33984bd058427)ESP\_SDHOST\_CARD\_INT\_N\_2

| #define ESP\_SDHOST\_CARD\_INT\_N\_2   199 |
| --- |

## [◆ ](#a90ed679e9630feb28030c0c1995b85f7)ESP\_SDHOST\_CARD\_WRITE\_PRT\_1

| #define ESP\_SDHOST\_CARD\_WRITE\_PRT\_1   196 |
| --- |

## [◆ ](#a1bc9c1d813aa85230ea95c190145d9bf)ESP\_SDHOST\_CARD\_WRITE\_PRT\_2

| #define ESP\_SDHOST\_CARD\_WRITE\_PRT\_2   197 |
| --- |

## [◆ ](#aff5857c7ef89e0ff32bbb49e393ea003)ESP\_SDHOST\_CCLK\_OUT\_1

| #define ESP\_SDHOST\_CCLK\_OUT\_1   172 |
| --- |

## [◆ ](#a00c0010ef6f14d2fa3b374f682dd0b46)ESP\_SDHOST\_CCLK\_OUT\_2

| #define ESP\_SDHOST\_CCLK\_OUT\_2   173 |
| --- |

## [◆ ](#aa99bd561249d2e1eb4344f298873f503)ESP\_SDHOST\_CCMD\_IN\_1

| #define ESP\_SDHOST\_CCMD\_IN\_1   178 |
| --- |

## [◆ ](#a041fd8cb426a95f145725f246201dacd)ESP\_SDHOST\_CCMD\_IN\_2

| #define ESP\_SDHOST\_CCMD\_IN\_2   179 |
| --- |

## [◆ ](#ae9e1e3a249d4fa5f330de8b0d0920a75)ESP\_SDHOST\_CCMD\_OD\_PULLUP\_EN\_N176

| #define ESP\_SDHOST\_CCMD\_OD\_PULLUP\_EN\_N176 |
| --- |

## [◆ ](#a5f1a59ccefd8e2388338627978e44059)ESP\_SDHOST\_CCMD\_OUT\_1

| #define ESP\_SDHOST\_CCMD\_OUT\_1   178 |
| --- |

## [◆ ](#a3122a431d37d337935ce459ce2826a5e)ESP\_SDHOST\_CCMD\_OUT\_2

| #define ESP\_SDHOST\_CCMD\_OUT\_2   179 |
| --- |

## [◆ ](#aa202d8a403ae5dac9a51f66dcc899815)ESP\_SDHOST\_CDATA\_IN\_10

| #define ESP\_SDHOST\_CDATA\_IN\_10   180 |
| --- |

## [◆ ](#a4518625593104880441b0d405eeb9d79)ESP\_SDHOST\_CDATA\_IN\_11

| #define ESP\_SDHOST\_CDATA\_IN\_11   181 |
| --- |

## [◆ ](#abf24ff245054912561d51db5d248770b)ESP\_SDHOST\_CDATA\_IN\_12

| #define ESP\_SDHOST\_CDATA\_IN\_12   182 |
| --- |

## [◆ ](#a250805f95412af52d358f90ab2ff9cab)ESP\_SDHOST\_CDATA\_IN\_13

| #define ESP\_SDHOST\_CDATA\_IN\_13   183 |
| --- |

## [◆ ](#a5aec6c17086301750c3ff542f784c73c)ESP\_SDHOST\_CDATA\_IN\_14

| #define ESP\_SDHOST\_CDATA\_IN\_14   184 |
| --- |

## [◆ ](#a511407191c4f58e59f19d0cbd527f940)ESP\_SDHOST\_CDATA\_IN\_15

| #define ESP\_SDHOST\_CDATA\_IN\_15   185 |
| --- |

## [◆ ](#ada2bd9384398308507f1827c187e5dd6)ESP\_SDHOST\_CDATA\_IN\_16

| #define ESP\_SDHOST\_CDATA\_IN\_16   186 |
| --- |

## [◆ ](#af12e58d00a8085cbafcac751b5a90705)ESP\_SDHOST\_CDATA\_IN\_17

| #define ESP\_SDHOST\_CDATA\_IN\_17   187 |
| --- |

## [◆ ](#a13ca361ff287a452bcdc24992448e59e)ESP\_SDHOST\_CDATA\_IN\_20

| #define ESP\_SDHOST\_CDATA\_IN\_20   213 |
| --- |

## [◆ ](#ab4c0aef79106c2d286f6d4bce99bd9eb)ESP\_SDHOST\_CDATA\_IN\_21

| #define ESP\_SDHOST\_CDATA\_IN\_21   214 |
| --- |

## [◆ ](#a5e4da4ac40cff37134d19032640fa253)ESP\_SDHOST\_CDATA\_IN\_22

| #define ESP\_SDHOST\_CDATA\_IN\_22   215 |
| --- |

## [◆ ](#aae5dec0fc3b263f26798bdfed1122a18)ESP\_SDHOST\_CDATA\_IN\_23

| #define ESP\_SDHOST\_CDATA\_IN\_23   216 |
| --- |

## [◆ ](#a098ad3a54b47ed40202ae8c2a9b6f7ec)ESP\_SDHOST\_CDATA\_IN\_24

| #define ESP\_SDHOST\_CDATA\_IN\_24   217 |
| --- |

## [◆ ](#a22d372ec349ce449aba06bf85cc1c1b5)ESP\_SDHOST\_CDATA\_IN\_25

| #define ESP\_SDHOST\_CDATA\_IN\_25   218 |
| --- |

## [◆ ](#af78c9aa8fc70487f561271635ff63b64)ESP\_SDHOST\_CDATA\_IN\_26

| #define ESP\_SDHOST\_CDATA\_IN\_26   219 |
| --- |

## [◆ ](#a2177168014217dcc8625d64f4d79e7e2)ESP\_SDHOST\_CDATA\_IN\_27

| #define ESP\_SDHOST\_CDATA\_IN\_27   220 |
| --- |

## [◆ ](#a650be8be910f36d892d2af6b903abe6e)ESP\_SDHOST\_CDATA\_OUT\_10

| #define ESP\_SDHOST\_CDATA\_OUT\_10   180 |
| --- |

## [◆ ](#a4e2d79ab775783efc0cdf86115331447)ESP\_SDHOST\_CDATA\_OUT\_11

| #define ESP\_SDHOST\_CDATA\_OUT\_11   181 |
| --- |

## [◆ ](#ace4ef14e4a0d7b0c28199eb8e837136e)ESP\_SDHOST\_CDATA\_OUT\_12

| #define ESP\_SDHOST\_CDATA\_OUT\_12   182 |
| --- |

## [◆ ](#a1b9425434296a84ae20e5138e99f3cc7)ESP\_SDHOST\_CDATA\_OUT\_13

| #define ESP\_SDHOST\_CDATA\_OUT\_13   183 |
| --- |

## [◆ ](#af720ace3a3c5109b440201c529ab9f68)ESP\_SDHOST\_CDATA\_OUT\_14

| #define ESP\_SDHOST\_CDATA\_OUT\_14   184 |
| --- |

## [◆ ](#a627e3a4e12df8e358d937bbabcaa8eb0)ESP\_SDHOST\_CDATA\_OUT\_15

| #define ESP\_SDHOST\_CDATA\_OUT\_15   185 |
| --- |

## [◆ ](#a502ca14944ee4d93aabcba4eafa0d900)ESP\_SDHOST\_CDATA\_OUT\_16

| #define ESP\_SDHOST\_CDATA\_OUT\_16   186 |
| --- |

## [◆ ](#ab695d377e135cac2283bc1c915396494)ESP\_SDHOST\_CDATA\_OUT\_17

| #define ESP\_SDHOST\_CDATA\_OUT\_17   187 |
| --- |

## [◆ ](#a06f93230a36ef5287147a0564b1dfed1)ESP\_SDHOST\_CDATA\_OUT\_20

| #define ESP\_SDHOST\_CDATA\_OUT\_20   213 |
| --- |

## [◆ ](#a6c9f531502c69bcd5889d60837ec0bdb)ESP\_SDHOST\_CDATA\_OUT\_21

| #define ESP\_SDHOST\_CDATA\_OUT\_21   214 |
| --- |

## [◆ ](#a786692b41d500d85fe88ee63d8e60fd5)ESP\_SDHOST\_CDATA\_OUT\_22

| #define ESP\_SDHOST\_CDATA\_OUT\_22   215 |
| --- |

## [◆ ](#a98324b90550b28d722cb38a3dd122532)ESP\_SDHOST\_CDATA\_OUT\_23

| #define ESP\_SDHOST\_CDATA\_OUT\_23   216 |
| --- |

## [◆ ](#a6898cbd2b727b76e5208cbc1a102b2a2)ESP\_SDHOST\_CDATA\_OUT\_24

| #define ESP\_SDHOST\_CDATA\_OUT\_24   217 |
| --- |

## [◆ ](#a638507475f38120dbd76db6f53455f57)ESP\_SDHOST\_CDATA\_OUT\_25

| #define ESP\_SDHOST\_CDATA\_OUT\_25   218 |
| --- |

## [◆ ](#a492c8431649dc6c429347d9a041a23cd)ESP\_SDHOST\_CDATA\_OUT\_26

| #define ESP\_SDHOST\_CDATA\_OUT\_26   219 |
| --- |

## [◆ ](#aece0df9752dd44b35534bda1251c484d)ESP\_SDHOST\_CDATA\_OUT\_27

| #define ESP\_SDHOST\_CDATA\_OUT\_27   220 |
| --- |

## [◆ ](#a13b46bfbdddc6ceedbb30b0f0dc6be5d)ESP\_SDHOST\_DATA\_STROBE\_1

| #define ESP\_SDHOST\_DATA\_STROBE\_1   192 |
| --- |

## [◆ ](#a209b7dd99039e60f032ac234c14e4c9d)ESP\_SDHOST\_DATA\_STROBE\_2

| #define ESP\_SDHOST\_DATA\_STROBE\_2   193 |
| --- |

## [◆ ](#abeb145776728098f097fd5a3a9b89132)ESP\_SDHOST\_RST\_N\_1

| #define ESP\_SDHOST\_RST\_N\_1   174 |
| --- |

## [◆ ](#a0536f51d9a6adba1138304fa758db39a)ESP\_SDHOST\_RST\_N\_2

| #define ESP\_SDHOST\_RST\_N\_2   175 |
| --- |

## [◆ ](#aac3529b76d29e57ad20500c9d1da23f3)ESP\_SDIO\_TOHOST\_INT\_OUT

| #define ESP\_SDIO\_TOHOST\_INT\_OUT   177 |
| --- |

## [◆ ](#a645411759ffdc63f51f2cd42632d2720)ESP\_SIG\_GPIO\_OUT

| #define ESP\_SIG\_GPIO\_OUT   256 |
| --- |

## [◆ ](#a0f6d8766907b91e60e62ae29c5e4b558)ESP\_SIG\_IN\_FUNC208

| #define ESP\_SIG\_IN\_FUNC208   208 |
| --- |

## [◆ ](#a8fe491023178ce16dd57edae3bdfe87f)ESP\_SIG\_IN\_FUNC209

| #define ESP\_SIG\_IN\_FUNC209   209 |
| --- |

## [◆ ](#add709f3eecdbe328426cd93013c80c3e)ESP\_SIG\_IN\_FUNC210

| #define ESP\_SIG\_IN\_FUNC210   210 |
| --- |

## [◆ ](#aa286ed797d5ab072404cda4eca929566)ESP\_SIG\_IN\_FUNC211

| #define ESP\_SIG\_IN\_FUNC211   211 |
| --- |

## [◆ ](#a8f25ba37edb68eb23e64395280ab791a)ESP\_SIG\_IN\_FUNC212

| #define ESP\_SIG\_IN\_FUNC212   212 |
| --- |

## [◆ ](#a5e192de902e66cccd6ec3c72ed8ef82a)ESP\_SIG\_IN\_FUNC\_208

| #define ESP\_SIG\_IN\_FUNC\_208   208 |
| --- |

## [◆ ](#a240123ea7ff1b64a70d1bb4866fe174b)ESP\_SIG\_IN\_FUNC\_209

| #define ESP\_SIG\_IN\_FUNC\_209   209 |
| --- |

## [◆ ](#a09fe402e83b28df1927599b5daa0b700)ESP\_SIG\_IN\_FUNC\_210

| #define ESP\_SIG\_IN\_FUNC\_210   210 |
| --- |

## [◆ ](#a38bfce1eb51e0913355a02e67d0d1496)ESP\_SIG\_IN\_FUNC\_211

| #define ESP\_SIG\_IN\_FUNC\_211   211 |
| --- |

## [◆ ](#ab5f2a06dab84e52c93b6a25172e7b2c4)ESP\_SIG\_IN\_FUNC\_212

| #define ESP\_SIG\_IN\_FUNC\_212   212 |
| --- |

## [◆ ](#a0bff2051090f5eaea7edd6e9b4725a3c)ESP\_SPI3\_CLK\_IN

| #define ESP\_SPI3\_CLK\_IN   66 |
| --- |

## [◆ ](#a02cc6c3ead85cf6c4837f05807103521)ESP\_SPI3\_CLK\_OUT

| #define ESP\_SPI3\_CLK\_OUT   66 |
| --- |

## [◆ ](#a485eded26f1b4bd7f03d916dcd4b0753)ESP\_SPI3\_CS0\_IN

| #define ESP\_SPI3\_CS0\_IN   71 |
| --- |

## [◆ ](#a8fc990a73f8fdc8d1004b3dad676a224)ESP\_SPI3\_CS0\_OUT

| #define ESP\_SPI3\_CS0\_OUT   71 |
| --- |

## [◆ ](#a7f06d2db560a8cd511c9189cd6ed8980)ESP\_SPI3\_CS1\_OUT

| #define ESP\_SPI3\_CS1\_OUT   72 |
| --- |

## [◆ ](#a9e4bf0b0eff43b1f56f17abe22ef24a5)ESP\_SPI3\_CS2\_OUT

| #define ESP\_SPI3\_CS2\_OUT   127 |
| --- |

## [◆ ](#ae7cf1730786ba95580b91b00066d3e25)ESP\_SPI3\_D\_IN

| #define ESP\_SPI3\_D\_IN   68 |
| --- |

## [◆ ](#aff4a1289beb94c9e23d7c1dd13d71d83)ESP\_SPI3\_D\_OUT

| #define ESP\_SPI3\_D\_OUT   68 |
| --- |

## [◆ ](#a84dd16599428fb4c3da12c221219af40)ESP\_SPI3\_HD\_IN

| #define ESP\_SPI3\_HD\_IN   69 |
| --- |

## [◆ ](#a73457a024aa63c16c2a5ef8ada2bf8b2)ESP\_SPI3\_HD\_OUT

| #define ESP\_SPI3\_HD\_OUT   69 |
| --- |

## [◆ ](#a05a9a2e5983b7895ca1fb05e5cd34709)ESP\_SPI3\_Q\_IN

| #define ESP\_SPI3\_Q\_IN   67 |
| --- |

## [◆ ](#a6656c910c99e3de854064f4df24faa2d)ESP\_SPI3\_Q\_OUT

| #define ESP\_SPI3\_Q\_OUT   67 |
| --- |

## [◆ ](#ae5ef053fe616dfb189a1a5bf28313647)ESP\_SPI3\_WP\_IN

| #define ESP\_SPI3\_WP\_IN   70 |
| --- |

## [◆ ](#ab3c345085fafd95b7bd2f83d14a5317c)ESP\_SPI3\_WP\_OUT

| #define ESP\_SPI3\_WP\_OUT   70 |
| --- |

## [◆ ](#a5f440c922a53085bb7b28f469c2a14b0)ESP\_SPICLK\_OUT

| #define ESP\_SPICLK\_OUT   4 |
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

## [◆ ](#a8fd6be50bb328dfd4ac0943f015b29ee)ESP\_SUBSPICLK\_OUT

| #define ESP\_SUBSPICLK\_OUT   119 |
| --- |

## [◆ ](#a8925d5f830a4bc5ca6114dc06bae3b1f)ESP\_SUBSPICS0\_OUT

| #define ESP\_SUBSPICS0\_OUT   124 |
| --- |

## [◆ ](#add0fa80736d0fe196872bb0664c433d4)ESP\_SUBSPICS1\_OUT

| #define ESP\_SUBSPICS1\_OUT   125 |
| --- |

## [◆ ](#aae7066cb62b74cf5e8f64f84bd76ee49)ESP\_SUBSPID4\_IN

| #define ESP\_SUBSPID4\_IN   155 |
| --- |

## [◆ ](#aa716d46da29da6affd5fa8851a730f3f)ESP\_SUBSPID4\_OUT

| #define ESP\_SUBSPID4\_OUT   155 |
| --- |

## [◆ ](#a051cd2450520fd4abc6f288c8577a12c)ESP\_SUBSPID5\_IN

| #define ESP\_SUBSPID5\_IN   156 |
| --- |

## [◆ ](#aece7dc6fc4bca1bd73d9ba856eb0f3fe)ESP\_SUBSPID5\_OUT

| #define ESP\_SUBSPID5\_OUT   156 |
| --- |

## [◆ ](#a6d49162b17a1a7cd3f2446c6ca8192ec)ESP\_SUBSPID6\_IN

| #define ESP\_SUBSPID6\_IN   157 |
| --- |

## [◆ ](#ab3e8db3219bf7aa7b2503a1fe759d60c)ESP\_SUBSPID6\_OUT

| #define ESP\_SUBSPID6\_OUT   157 |
| --- |

## [◆ ](#a34b9a22e0f55a0534199e62b1eaff5b0)ESP\_SUBSPID7\_IN

| #define ESP\_SUBSPID7\_IN   158 |
| --- |

## [◆ ](#adb8c01bf2361a8b24e79cf048a7e6535)ESP\_SUBSPID7\_OUT

| #define ESP\_SUBSPID7\_OUT   158 |
| --- |

## [◆ ](#a0c924000fccdb7ce112822db720dbd8d)ESP\_SUBSPID\_IN

| #define ESP\_SUBSPID\_IN   121 |
| --- |

## [◆ ](#a3b9cab35f71697419266c71583f8a087)ESP\_SUBSPID\_OUT

| #define ESP\_SUBSPID\_OUT   121 |
| --- |

## [◆ ](#a6ccb6e41ab48fba76302068ee4433fb8)ESP\_SUBSPIDQS\_IN

| #define ESP\_SUBSPIDQS\_IN   159 |
| --- |

## [◆ ](#a608345dcd6c90e4f19427bb38161501a)ESP\_SUBSPIDQS\_OUT

| #define ESP\_SUBSPIDQS\_OUT   159 |
| --- |

## [◆ ](#a9a04da28895e846359a3ea89391b21f6)ESP\_SUBSPIHD\_IN

| #define ESP\_SUBSPIHD\_IN   122 |
| --- |

## [◆ ](#ab1f7e54d6230ceabc3fee083aab409d1)ESP\_SUBSPIHD\_OUT

| #define ESP\_SUBSPIHD\_OUT   122 |
| --- |

## [◆ ](#af80ecb5fcd6c02cb5b73478198abef3c)ESP\_SUBSPIQ\_IN

| #define ESP\_SUBSPIQ\_IN   120 |
| --- |

## [◆ ](#ac75fd67f54d49449451c4924c0b7910a)ESP\_SUBSPIQ\_OUT

| #define ESP\_SUBSPIQ\_OUT   120 |
| --- |

## [◆ ](#a3c4b2938ef6753d76a752bf9a973de52)ESP\_SUBSPIWP\_IN

| #define ESP\_SUBSPIWP\_IN   123 |
| --- |

## [◆ ](#a7493ab9a1f0dc10902ce412055579842)ESP\_SUBSPIWP\_OUT

| #define ESP\_SUBSPIWP\_OUT   123 |
| --- |

## [◆ ](#a0206456525cd6dc235ed6892e98731c6)ESP\_SYNCERR

| #define ESP\_SYNCERR   229 |
| --- |

## [◆ ](#aa62bd8539c4d89abaa542d8bd4c91efd)ESP\_SYNCFOUND\_FLAG

| #define ESP\_SYNCFOUND\_FLAG   230 |
| --- |

## [◆ ](#a6d0d41d1ec0f6fc626861f5857684e6d)ESP\_TWAI\_BUS\_OFF\_ON

| #define ESP\_TWAI\_BUS\_OFF\_ON   117 |
| --- |

## [◆ ](#a1c69791269fdbb2a11f66f33eb4066be)ESP\_TWAI\_CLKOUT

| #define ESP\_TWAI\_CLKOUT   118 |
| --- |

## [◆ ](#ab3da303c2f9226f9648669c17af8377a)ESP\_TWAI\_RX

| #define ESP\_TWAI\_RX   116 |
| --- |

## [◆ ](#a3b13bb40583aaa0f85de982509247614)ESP\_TWAI\_TX

| #define ESP\_TWAI\_TX   116 |
| --- |

## [◆ ](#a530d7a918a97cd1fff1acf2f90edd4ca)ESP\_U0CTS\_IN

| #define ESP\_U0CTS\_IN   13 |
| --- |

## [◆ ](#a53e3a4557a4eb1f7f98250abef03c02a)ESP\_U0DSR\_IN

| #define ESP\_U0DSR\_IN   14 |
| --- |

## [◆ ](#acc8716af947169c9f167bdf215c5314c)ESP\_U0DTR\_OUT

| #define ESP\_U0DTR\_OUT   14 |
| --- |

## [◆ ](#a4257bbc044af6ea3612313e3a0b7e7c9)ESP\_U0RTS\_OUT

| #define ESP\_U0RTS\_OUT   13 |
| --- |

## [◆ ](#aca502efa55ce2286dc9eba28192681fd)ESP\_U0RXD\_IN

| #define ESP\_U0RXD\_IN   12 |
| --- |

## [◆ ](#af1e58fb8e7ef86a92171eca7bb1671af)ESP\_U0TXD\_OUT

| #define ESP\_U0TXD\_OUT   12 |
| --- |

## [◆ ](#a3c005e616da21a058960d6aed79427b3)ESP\_U1CTS\_IN

| #define ESP\_U1CTS\_IN   16 |
| --- |

## [◆ ](#a5f29b138691540598d0b977dc4bd5971)ESP\_U1DSR\_IN

| #define ESP\_U1DSR\_IN   17 |
| --- |

## [◆ ](#a1f7df042d40ec6f20b559ef6778d7497)ESP\_U1DTR\_OUT

| #define ESP\_U1DTR\_OUT   17 |
| --- |

## [◆ ](#a8f6399745566bd5caa2020e4dcb2bb3b)ESP\_U1RTS\_OUT

| #define ESP\_U1RTS\_OUT   16 |
| --- |

## [◆ ](#a2293e0646e0ad2f76d62f76425ae6770)ESP\_U1RXD\_IN

| #define ESP\_U1RXD\_IN   15 |
| --- |

## [◆ ](#a6053b38147e28e3a7479b38e7d195136)ESP\_U1TXD\_OUT

| #define ESP\_U1TXD\_OUT   15 |
| --- |

## [◆ ](#a735a482aa723130ccb408f0fb7596a0a)ESP\_U2CTS\_IN

| #define ESP\_U2CTS\_IN   19 |
| --- |

## [◆ ](#a70d4f834bfd182c138257e36a4b04096)ESP\_U2DSR\_IN

| #define ESP\_U2DSR\_IN   20 |
| --- |

## [◆ ](#a783f6ee9ad46dfd9e34d1473b1e2ad9b)ESP\_U2DTR\_OUT

| #define ESP\_U2DTR\_OUT   20 |
| --- |

## [◆ ](#a174b50e35d961ded056cea3848110b20)ESP\_U2RTS\_OUT

| #define ESP\_U2RTS\_OUT   19 |
| --- |

## [◆ ](#abe46ead057c2b66d500ef07e8a84fe0f)ESP\_U2RXD\_IN

| #define ESP\_U2RXD\_IN   18 |
| --- |

## [◆ ](#a20baac10eb4b76603580e1ea7065213a)ESP\_U2TXD\_OUT

| #define ESP\_U2TXD\_OUT   18 |
| --- |

## [◆ ](#a25d03cedd231864f508e405d0ae2fa4b)ESP\_UPDATE\_RX

| #define ESP\_UPDATE\_RX   247 |
| --- |

## [◆ ](#a28f381128449aed0ae738516df39790c)ESP\_USB\_EXTPHY\_OEN

| #define ESP\_USB\_EXTPHY\_OEN   55 |
| --- |

## [◆ ](#a095d83d616afb08c4b06d82c4d907fee)ESP\_USB\_EXTPHY\_RCV

| #define ESP\_USB\_EXTPHY\_RCV   57 |
| --- |

## [◆ ](#aedb10271abe4c1969eefbc0425681652)ESP\_USB\_EXTPHY\_SPEED

| #define ESP\_USB\_EXTPHY\_SPEED   56 |
| --- |

## [◆ ](#a301551d0d524f785b3d0e2c35bc81ce5)ESP\_USB\_EXTPHY\_SUSPND

| #define ESP\_USB\_EXTPHY\_SUSPND   59 |
| --- |

## [◆ ](#aeaa130d2e220f2ebd073983921ad3679)ESP\_USB\_EXTPHY\_VM

| #define ESP\_USB\_EXTPHY\_VM   56 |
| --- |

## [◆ ](#abaeb7b2bb8208db93655b442293976aa)ESP\_USB\_EXTPHY\_VMO

| #define ESP\_USB\_EXTPHY\_VMO   58 |
| --- |

## [◆ ](#a7c2bcf73d61315a0d8c71d68173f9860)ESP\_USB\_EXTPHY\_VP

| #define ESP\_USB\_EXTPHY\_VP   55 |
| --- |

## [◆ ](#a88c6a9f957332dac96360dd3f631e59b)ESP\_USB\_EXTPHY\_VPO

| #define ESP\_USB\_EXTPHY\_VPO   57 |
| --- |

## [◆ ](#ae39a7176534ecc35ed432e6b825cf1ee)ESP\_USB\_JTAG\_TCK

| #define ESP\_USB\_JTAG\_TCK   85 |
| --- |

## [◆ ](#ad92972ab672e468cc56c24733114d7db)ESP\_USB\_JTAG\_TDI

| #define ESP\_USB\_JTAG\_TDI   87 |
| --- |

## [◆ ](#a880f86e1452afee85e90589f74c17a4d)ESP\_USB\_JTAG\_TDO

| #define ESP\_USB\_JTAG\_TDO   88 |
| --- |

## [◆ ](#a6b5babfcba4d025bdd1ab709b569fdf2)ESP\_USB\_JTAG\_TDO\_BRIDGE

| #define ESP\_USB\_JTAG\_TDO\_BRIDGE   251 |
| --- |

## [◆ ](#aca9c05aba976c762c0ec5fa3603c76e1)ESP\_USB\_JTAG\_TMS

| #define ESP\_USB\_JTAG\_TMS   86 |
| --- |

## [◆ ](#a4358434232f1f3515d8f5f4961d77520)ESP\_USB\_JTAG\_TRST

| #define ESP\_USB\_JTAG\_TRST   251 |
| --- |

## [◆ ](#a4d0c408fedb6ba35298c1398eccaa4e2)ESP\_USB\_OTG\_AVALID\_IN

| #define ESP\_USB\_OTG\_AVALID\_IN   59 |
| --- |

## [◆ ](#a852717f88ddb411d5b0dc49a3be83282)ESP\_USB\_OTG\_DMPULLDOWN

| #define ESP\_USB\_OTG\_DMPULLDOWN   62 |
| --- |

## [◆ ](#a04c49eae7bb25687d76a810ab6468353)ESP\_USB\_OTG\_DPPULLDOWN

| #define ESP\_USB\_OTG\_DPPULLDOWN   61 |
| --- |

## [◆ ](#a6f79de1e3bbc3758362426eecad93d3d)ESP\_USB\_OTG\_DRVVBUS

| #define ESP\_USB\_OTG\_DRVVBUS   63 |
| --- |

## [◆ ](#a22582585ff59bc29c3e011c4d869b1b8)ESP\_USB\_OTG\_IDDIG\_IN

| #define ESP\_USB\_OTG\_IDDIG\_IN   58 |
| --- |

## [◆ ](#ab7335ddb7641fb62231adf289a7a74a8)ESP\_USB\_OTG\_IDPULLUP

| #define ESP\_USB\_OTG\_IDPULLUP   60 |
| --- |

## [◆ ](#a4e3bd2577c74b857a74f1c367a235bad)ESP\_USB\_OTG\_VBUSVALID\_IN

| #define ESP\_USB\_OTG\_VBUSVALID\_IN   61 |
| --- |

## [◆ ](#aaafaee30be8e3fed2eb1117ce381dd37)ESP\_USB\_SRP\_BVALID\_IN

| #define ESP\_USB\_SRP\_BVALID\_IN   60 |
| --- |

## [◆ ](#a49b28cbc76c15cd1395f3b2e1a6ac4d9)ESP\_USB\_SRP\_CHRGVBUS

| #define ESP\_USB\_SRP\_CHRGVBUS   64 |
| --- |

## [◆ ](#a30f3abf038b27fa16a82bdf413eff14c)ESP\_USB\_SRP\_DISCHRGVBUS

| #define ESP\_USB\_SRP\_DISCHRGVBUS   65 |
| --- |

## [◆ ](#a8601c4fb546ff39782c0fbb14e68bfbd)ESP\_USB\_SRP\_SESSEND\_IN

| #define ESP\_USB\_SRP\_SESSEND\_IN   62 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [pinctrl](dir_2c6c4fbd167577104b7f1b7148586168.md)
- [esp32s3-gpio-sigmap.h](esp32s3-gpio-sigmap_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
