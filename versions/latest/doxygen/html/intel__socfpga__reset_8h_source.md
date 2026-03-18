---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/intel__socfpga__reset_8h_source.html
original_path: doxygen/html/intel__socfpga__reset_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

intel\_socfpga\_reset.h

[Go to the documentation of this file.](intel__socfpga__reset_8h.md)

1/\*

2 \* SPDX-License-Identifier: Apache-2.0

3 \*

4 \* Copyright (C) 2023, Intel Corporation

5 \*

6 \*/

7

8#ifndef ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_INTEL\_SOCFPGA\_RESET\_H\_

9#define ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_INTEL\_SOCFPGA\_RESET\_H\_

10

11/\* The Reset line value will be used by the reset controller driver to

12 \* derive the register offset and the associated device bit to perform

13 \* device assert and de-assert.

14 \*

15 \* The reset lines should be passed as a parameter to the resets property

16 \* of the driver node in dtsi which will call reset-controller driver to

17 \* assert/de-assert itself.

18 \*

19 \* Example: Deriving Reset Line value

20 \* per0modrst register offset = 0x24;

21 \* NAND RSTLINE pin = 5;

22 \* RSTMGR\_NAND\_RSTLINE = (0x24 \* 8) + 5 = 293

23 \*/

24

[ 25](intel__socfpga__reset_8h.md#a585154051b7dbf46359c3b343cb88ee7)#define RSTMGR\_SDMCOLDRST\_RSTLINE 0

[ 26](intel__socfpga__reset_8h.md#ada7dd08adc2fe898fb18b4a0c7caa3e6)#define RSTMGR\_SDMWARMRST\_RSTLINE 1

[ 27](intel__socfpga__reset_8h.md#acc2a4393193216677993aac2c3e39383)#define RSTMGR\_SDMLASTPORRST\_RSTLINE 2

[ 28](intel__socfpga__reset_8h.md#ad7b55a6c11754a4117571a4b0bfcce03)#define RSTMGR\_L4WD0RST\_RSTLINE 16

[ 29](intel__socfpga__reset_8h.md#af88c555204bfbf0e2e4e63dbbe617b25)#define RSTMGR\_L4WD1RST\_RSTLINE 17

[ 30](intel__socfpga__reset_8h.md#addee8be9550973555759a27863beda6d)#define RSTMGR\_L4WD2RST\_RSTLINE 18

[ 31](intel__socfpga__reset_8h.md#a472aa6066e3e72e141a7ad16874b82ed)#define RSTMGR\_L4WD3RST\_RSTLINE 19

[ 32](intel__socfpga__reset_8h.md#a0b7857fa4ead0b712de1797e3c9665ea)#define RSTMGR\_L4WD4RST\_RSTLINE 20

[ 33](intel__socfpga__reset_8h.md#af11cd90de5c492cc39b6abe79e35cca3)#define RSTMGR\_DEBUGRST\_RSTLINE 21

[ 34](intel__socfpga__reset_8h.md#a5c0bd4df44114d9a568944da9c2fe572)#define RSTMGR\_CSDAPRST\_RSTLINE 22

[ 35](intel__socfpga__reset_8h.md#a2c4c744fcd15f30aa79f156a6b1f9e1f)#define RSTMGR\_EMIFTIMEOUT\_RSTLINE 64

[ 36](intel__socfpga__reset_8h.md#a23e3f86776c276a5e5f005e0f1066e98)#define RSTMGR\_FPGAHSTIMEOUT\_RSTLINE 66

[ 37](intel__socfpga__reset_8h.md#a4c6cc335ac18aeae909288259d26cb7d)#define RSTMGR\_ETRSTALLTIMEOUT\_RSTLINE 67

[ 38](intel__socfpga__reset_8h.md#ac7d848a04958359fb8a8061721dea09d)#define RSTMGR\_LWSOC2FPGATIMEOUT\_RSTLINE 72

[ 39](intel__socfpga__reset_8h.md#ae522b9b126638e62fd5dc897e4dda03f)#define RSTMGR\_SOC2FPGATIMEOUT\_RSTLINE 73

[ 40](intel__socfpga__reset_8h.md#a422d06dce0174ecc0fea6abab12d2498)#define RSTMGR\_F2SDRAMTIMEOUT\_RSTLINE 74

[ 41](intel__socfpga__reset_8h.md#a03a7ba7ad57b2c7473475ab6ac48b8a6)#define RSTMGR\_F2STIMEOUT\_RSTLINE 75

[ 42](intel__socfpga__reset_8h.md#a24b92f54005d6700167970a6b6c9c38d)#define RSTMGR\_L3NOCDBGTIMEOUT\_RSTLINE 79

[ 43](intel__socfpga__reset_8h.md#aa1be8f78e28752fa2476bbe8601d721e)#define RSTMGR\_DEBUGL3NOCTIMEOUT\_RSTLINE 80

[ 44](intel__socfpga__reset_8h.md#acc85e22aefcbec3c832e79bca5d445db)#define RSTMGR\_EMIF\_FLUSH\_RSTLINE 128

[ 45](intel__socfpga__reset_8h.md#a6fc00e0e6d64b312f5db809e2501aa8c)#define RSTMGR\_FPGAHSEN\_RSTLINE 130

[ 46](intel__socfpga__reset_8h.md#aec42bb3bf9fb43332139e56601a1f717)#define RSTMGR\_ETRSTALLEN\_RSTLINE 131

[ 47](intel__socfpga__reset_8h.md#a4f8d4aae414244c763e942863e6327b4)#define RSTMGR\_LWSOC2FPGA\_FLUSH\_RSTLINE 137

[ 48](intel__socfpga__reset_8h.md#a974e4413029a0bd76fa3a72fb23ce424)#define RSTMGR\_SOC2FPGA\_FLUSH\_RSTLINE 138

[ 49](intel__socfpga__reset_8h.md#a1c9dad218dbbc504fb64d023319c0153)#define RSTMGR\_F2SDRAM\_FLUSH\_RSTLINE 139

[ 50](intel__socfpga__reset_8h.md#a22ed34d72d389c7952a411f0a6039fae)#define RSTMGR\_F2SOC\_FLUSH\_RSTLINE 140

[ 51](intel__socfpga__reset_8h.md#a027d4f38ff1e47e66566b1de4e8607ed)#define RSTMGR\_L3NOC\_DBG\_RSTLINE 144

[ 52](intel__socfpga__reset_8h.md#a65ce5421ecd5257a9bbd9859a5327c41)#define RSTMGR\_DEBUG\_L3NOC\_RSTLINE 145

[ 53](intel__socfpga__reset_8h.md#a096df778de6c181e296007f6bf7ae72c)#define RSTMGR\_EMIF\_FLUSH\_REQ\_RSTLINE 160

[ 54](intel__socfpga__reset_8h.md#a53fb988dc2177ca3b9de2873d8ba78f2)#define RSTMGR\_FPGAHSREQ\_RSTLINE 162

[ 55](intel__socfpga__reset_8h.md#ae6381d91677b3668876d3d9960fdeaea)#define RSTMGR\_ETRSTALLREQ\_RSTLINE 163

[ 56](intel__socfpga__reset_8h.md#a06462a7bbd730d88f4f5af956d9c6145)#define RSTMGR\_LWSOC2FPGA\_FLUSH\_REQ\_RSTLINE 169

[ 57](intel__socfpga__reset_8h.md#a25371eb9f5dc642190275bc609344993)#define RSTMGR\_SOC2FPGA\_FLUSH\_REQ\_RSTLINE 170

[ 58](intel__socfpga__reset_8h.md#a74a9a1a964ff55c2dda03bab20504d32)#define RSTMGR\_F2SDRAM\_FLUSH\_REQ\_RSTLINE 171

[ 59](intel__socfpga__reset_8h.md#a5181d95163350f63dd84d2c8d2eea563)#define RSTMGR\_F2S\_FLUSH\_REQ\_RSTLINE 172

[ 60](intel__socfpga__reset_8h.md#acfaf0bc836199746c9e9a2fbc6f10ba7)#define RSTMGR\_L3NOC\_DBG\_REQ\_RSTLINE 176

[ 61](intel__socfpga__reset_8h.md#af5061586441dc39e84f43efea93edb9e)#define RSTMGR\_DEBUG\_L3NOC\_REQ\_RSTLINE 177

[ 62](intel__socfpga__reset_8h.md#a8c7db588d809ed729a14abd9d14e6d72)#define RSTMGR\_EMIF\_FLUSH\_ACK\_RSTLINE 192

[ 63](intel__socfpga__reset_8h.md#a38d45c134a0a6d7f5a341bacb3587f9b)#define RSTMGR\_FPGAHSACK\_RSTLINE 194

[ 64](intel__socfpga__reset_8h.md#ab89f7f3813a6f9328e490fc73b60ca98)#define RSTMGR\_ETRSTALLACK\_RSTLINE 195

[ 65](intel__socfpga__reset_8h.md#a9dcc6361c91e5574cfb59ddac8f6fd0a)#define RSTMGR\_LWSOC2FPGA\_FLUSH\_ACK\_RSTLINE 201

[ 66](intel__socfpga__reset_8h.md#abfb876a63a51e4af7c3e41595c49f95e)#define RSTMGR\_SOC2FPGA\_FLUSH\_ACK\_RSTLINE 202

[ 67](intel__socfpga__reset_8h.md#a847f55a29c0c71b8823d752b6772542d)#define RSTMGR\_F2SDRAM\_FLUSH\_ACK\_RSTLINE 203

[ 68](intel__socfpga__reset_8h.md#a22d82b4660a71d349ef7f6d51b4ea84d)#define RSTMGR\_F2S\_FLUSH\_ACK\_RSTLINE 204

[ 69](intel__socfpga__reset_8h.md#a7e28c0b94a3642b5a9bcc6578507baaf)#define RSTMGR\_L3NOC\_DBG\_ACK\_RSTLINE 208

[ 70](intel__socfpga__reset_8h.md#a8b9fff3b2d2ee11f86830b7960c14fdc)#define RSTMGR\_DEBUG\_L3NOC\_ACK\_RSTLINE 209

[ 71](intel__socfpga__reset_8h.md#a5986c0861bbd91a277c86e35ad7c2697)#define RSTMGR\_ETRSTALLWARMRST\_RSTLINE 224

[ 72](intel__socfpga__reset_8h.md#abc19e710d19fa723ed961d603c0ee481)#define RSTMGR\_TSN0\_RSTLINE 288

[ 73](intel__socfpga__reset_8h.md#ac54f3d8be989467a8c2614f7cbd258d8)#define RSTMGR\_TSN1\_RSTLINE 289

[ 74](intel__socfpga__reset_8h.md#a07e5632d3587678a19a236cb0555583f)#define RSTMGR\_TSN2\_RSTLINE 290

[ 75](intel__socfpga__reset_8h.md#ad8fdc2c3565845ec0ed24f1037d4fe54)#define RSTMGR\_USB0\_RSTLINE 291

[ 76](intel__socfpga__reset_8h.md#a29719d049694afd1eb3ffba4c20f0dc2)#define RSTMGR\_USB1\_RSTLINE 292

[ 77](intel__socfpga__reset_8h.md#afbe21f3e39f5f7c608dbb141f9d08939)#define RSTMGR\_NAND\_RSTLINE 293

[ 78](intel__socfpga__reset_8h.md#a4cb58de3422e1c6ce0b3faacefe68588)#define RSTMGR\_SOFTPHY\_RSTLINE 294

[ 79](intel__socfpga__reset_8h.md#ac33b56c9e2df3e00e926f0f61fa54790)#define RSTMGR\_SDMMC\_RSTLINE 295

[ 80](intel__socfpga__reset_8h.md#a623bbf4826b0e39a7901dae99182b3c8)#define RSTMGR\_TSN0ECC\_RSTLINE 296

[ 81](intel__socfpga__reset_8h.md#a7ed105f6e6e568d49c92f312409ea854)#define RSTMGR\_TSN1ECC\_RSTLINE 297

[ 82](intel__socfpga__reset_8h.md#a84f5dc45defb0ab93134a96730bbb6aa)#define RSTMGR\_TSN2ECC\_RSTLINE 298

[ 83](intel__socfpga__reset_8h.md#acf82c79cb3f5673427cd59424e60dac0)#define RSTMGR\_USB0ECC\_RSTLINE 299

[ 84](intel__socfpga__reset_8h.md#abacded7d156188a657baccef36dc8352)#define RSTMGR\_USB1ECC\_RSTLINE 300

[ 85](intel__socfpga__reset_8h.md#a75c819e461a1e16a8b1550d11d32bdbe)#define RSTMGR\_NANDECC\_RSTLINE 301

[ 86](intel__socfpga__reset_8h.md#a52b788acab6b89ab6ab866a52a34123c)#define RSTMGR\_SDMMCECC\_RSTLINE 303

[ 87](intel__socfpga__reset_8h.md#a9c60e629df27657e03d783ad28dc4536)#define RSTMGR\_DMA\_RSTLINE 304

[ 88](intel__socfpga__reset_8h.md#ad90b8ac65d4a01685cef402a578005e2)#define RSTMGR\_SPIM0\_RSTLINE 305

[ 89](intel__socfpga__reset_8h.md#af7dd0bbe30d752d9daa5055eef861429)#define RSTMGR\_SPIM1\_RSTLINE 306

[ 90](intel__socfpga__reset_8h.md#ab15b14a102bb406da22d0e44b5101791)#define RSTMGR\_SPIS0\_RSTLINE 307

[ 91](intel__socfpga__reset_8h.md#a23cdb6b512cfcddaae83ea80f40911c3)#define RSTMGR\_SPIS1\_RSTLINE 308

[ 92](intel__socfpga__reset_8h.md#a4e5975d01bc4247b2a07779a7482faff)#define RSTMGR\_DMAECC\_RSTLINE 309

[ 93](intel__socfpga__reset_8h.md#a67704f9262daf85de0ceda0f5c65036b)#define RSTMGR\_EMACPTP\_RSTLINE 310

[ 94](intel__socfpga__reset_8h.md#a06f828739e22a4a483148daa9310d87d)#define RSTMGR\_DMAIF0\_RSTLINE 312

[ 95](intel__socfpga__reset_8h.md#a58d59e581e7cbf360e59c3955051136b)#define RSTMGR\_DMAIF1\_RSTLINE 313

[ 96](intel__socfpga__reset_8h.md#a4197cf59b7f126eb8b95347ff154bed0)#define RSTMGR\_DMAIF2\_RSTLINE 314

[ 97](intel__socfpga__reset_8h.md#a56d5e8d6a269c3cc5385c9f1c4a7222a)#define RSTMGR\_DMAIF3\_RSTLINE 315

[ 98](intel__socfpga__reset_8h.md#a32b19baf7eb10fce4dd52d62dcfe7d2e)#define RSTMGR\_DMAIF4\_RSTLINE 316

[ 99](intel__socfpga__reset_8h.md#a2fd7c7028304ed477884717e3b29f444)#define RSTMGR\_DMAIF5\_RSTLINE 317

[ 100](intel__socfpga__reset_8h.md#a622d9a32d696e344579d0d9c700eb408)#define RSTMGR\_DMAIF6\_RSTLINE 318

[ 101](intel__socfpga__reset_8h.md#ab5a70171fcfda89bc574a306abc9514a)#define RSTMGR\_DMAIF7\_RSTLINE 319

[ 102](intel__socfpga__reset_8h.md#a962c8dc409b32c05461410fd1432b63d)#define RSTMGR\_WATCHDOG0\_RSTLINE 320

[ 103](intel__socfpga__reset_8h.md#a27b2ce66bf0b781bc332637a5839fc7e)#define RSTMGR\_WATCHDOG1\_RSTLINE 321

[ 104](intel__socfpga__reset_8h.md#a57a5b6d287582da91705ec9dca7cb748)#define RSTMGR\_WATCHDOG2\_RSTLINE 322

[ 105](intel__socfpga__reset_8h.md#a16d59d153db75024d08f029705bb2113)#define RSTMGR\_WATCHDOG3\_RSTLINE 323

[ 106](intel__socfpga__reset_8h.md#aae8be8b5bf8ba79acafac67bca76fd07)#define RSTMGR\_L4SYSTIMER0\_RSTLINE 324

[ 107](intel__socfpga__reset_8h.md#ad7d6087df511622d34696bf032db2217)#define RSTMGR\_L4SYSTIMER1\_RSTLINE 325

[ 108](intel__socfpga__reset_8h.md#a532716c0bcf0535be451a35762479995)#define RSTMGR\_SPTIMER0\_RSTLINE 326

[ 109](intel__socfpga__reset_8h.md#a8af37e22b5a8a9191de46925aab13ef1)#define RSTMGR\_SPTIMER1\_RSTLINE 327

[ 110](intel__socfpga__reset_8h.md#ac57c12e78099bad648343fc04886b01d)#define RSTMGR\_I2C0\_RSTLINE 328

[ 111](intel__socfpga__reset_8h.md#a10bb94717d19bd42e0c6093fcbfd09ba)#define RSTMGR\_I2C1\_RSTLINE 329

[ 112](intel__socfpga__reset_8h.md#a5d3606f401130658eb815ab59190b455)#define RSTMGR\_I2C2\_RSTLINE 330

[ 113](intel__socfpga__reset_8h.md#a796b1b1b385333d7a4a0a3c4d4468fc5)#define RSTMGR\_I2C3\_RSTLINE 331

[ 114](intel__socfpga__reset_8h.md#a72b79a6cb15ef7f14d87ec52306bd801)#define RSTMGR\_I2C4\_RSTLINE 332

[ 115](intel__socfpga__reset_8h.md#a38f86cb0db46703c94f48610f47daed8)#define RSTMGR\_I3C0\_RSTLINE 333

[ 116](intel__socfpga__reset_8h.md#a81880e530aec6268f1cbe5498d1e982a)#define RSTMGR\_I3C1\_RSTLINE 334

[ 117](intel__socfpga__reset_8h.md#a577f1885fe5bc1d6fc32c3f861494d46)#define RSTMGR\_UART0\_RSTLINE 336

[ 118](intel__socfpga__reset_8h.md#ac516c17df2e2f6e28224696b52a273c4)#define RSTMGR\_UART1\_RSTLINE 337

[ 119](intel__socfpga__reset_8h.md#af53b30d174c00f5d155a1b0d3d6ed120)#define RSTMGR\_GPIO0\_RSTLINE 344

[ 120](intel__socfpga__reset_8h.md#aaa2d5d32ae7be05e2f6d536b9a8cf383)#define RSTMGR\_GPIO1\_RSTLINE 345

[ 121](intel__socfpga__reset_8h.md#a8fffd79b568e69beb85783c25ebb637a)#define RSTMGR\_WATCHDOG4\_RSTLINE 346

[ 122](intel__socfpga__reset_8h.md#a8c4197983db16222334c196115ab2646)#define RSTMGR\_SOC2FPGA\_RSTLINE 352

[ 123](intel__socfpga__reset_8h.md#afcd4d63727fe68dd63a521675f296d71)#define RSTMGR\_LWSOC2FPGA\_RSTLINE 353

[ 124](intel__socfpga__reset_8h.md#a39fa1dafa254c587b03cabd52c3da0d3)#define RSTMGR\_FPGA2SOC\_RSTLINE 354

[ 125](intel__socfpga__reset_8h.md#a38d72a8a1d40aac1902ca01d6983e8bd)#define RSTMGR\_FPGA2SDRAM\_RSTLINE 355

[ 126](intel__socfpga__reset_8h.md#a2fc735d622800d0c1bfb3f927db8b200)#define RSTMGR\_MPFE\_RSTLINE 358

[ 127](intel__socfpga__reset_8h.md#ae921296149380455af880518dbd3f175)#define RSTMGR\_DBG\_RST\_RSTLINE 480

[ 128](intel__socfpga__reset_8h.md#a0ab33f9e850b87fab5fe5774b3997d8b)#define RSTMGR\_SOC2FPGA\_WARM\_RSTLINE 608

[ 129](intel__socfpga__reset_8h.md#a8e103cc2f9b39cb20f8daca553d0c7c3)#define RSTMGR\_LWSOC2FPGA\_WARM\_RSTLINE 609

[ 130](intel__socfpga__reset_8h.md#a651a172ba0de8436a11e88a362cf4371)#define RSTMGR\_FPGA2SOC\_WARM\_RSTLINE 610

[ 131](intel__socfpga__reset_8h.md#a4fac58bc49b6dc627e23c899816265fa)#define RSTMGR\_FPGA2SDRAM\_WARM\_RSTLINE 611

[ 132](intel__socfpga__reset_8h.md#afa1b7ebd62f41bf5745871580c393f9e)#define RSTMGR\_MPFE\_WARM\_RSTLINE 614

133

134#endif /\* ZEPHYR\_INCLUDE\_DT\_BINDINGS\_RESET\_INTEL\_SOCFPGA\_RESET\_H\_ \*/

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [reset](dir_10e63a26bda611813cb588c12a3608a6.md)
- [intel\_socfpga\_reset.h](intel__socfpga__reset_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
