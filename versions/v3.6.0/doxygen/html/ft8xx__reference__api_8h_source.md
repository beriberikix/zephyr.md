---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/ft8xx__reference__api_8h_source.html
original_path: doxygen/html/ft8xx__reference__api_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ft8xx\_reference\_api.h

[Go to the documentation of this file.](ft8xx__reference__api_8h.md)

1/\*

2 \* Copyright (c) 2021 Hubert Miś

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_REFERENCE\_API\_H\_

13#define ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_REFERENCE\_API\_H\_

14

15#include <[stdint.h](stdint_8h.md)>

16

17#include <[zephyr/drivers/misc/ft8xx/ft8xx\_copro.h](ft8xx__copro_8h.md)>

18#include <[zephyr/drivers/misc/ft8xx/ft8xx\_common.h](ft8xx__common_8h.md)>

19#include <[zephyr/drivers/misc/ft8xx/ft8xx\_dl.h](ft8xx__dl_8h.md)>

20#include <[zephyr/drivers/misc/ft8xx/ft8xx\_memory.h](ft8xx__memory_8h.md)>

21

22#ifdef \_\_cplusplus

23extern "C" {

24#endif

25

40

[ 47](group__ft8xx__reference__api.md#ga1e9c6203ebb7cc15a736d074bd98c181)static inline void [wr8](group__ft8xx__reference__api.md#ga1e9c6203ebb7cc15a736d074bd98c181)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data)

48{

49 [ft8xx\_wr8](group__ft8xx__common.md#ga7623499f328d820b1e84d2a3834a89a2)(address, data);

50}

51

[ 58](group__ft8xx__reference__api.md#ga8fac4ed55f7ef9d82d8dcb0eb6f09eab)static inline void [wr16](group__ft8xx__reference__api.md#ga8fac4ed55f7ef9d82d8dcb0eb6f09eab)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data)

59{

60 [ft8xx\_wr16](group__ft8xx__common.md#gadfbff24d8fb246081cefbc51190b32e5)(address, data);

61}

62

[ 69](group__ft8xx__reference__api.md#ga3f6814650684e2c2100d8f9a36505ca0)static inline void [wr32](group__ft8xx__reference__api.md#ga3f6814650684e2c2100d8f9a36505ca0)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data)

70{

71 [ft8xx\_wr32](group__ft8xx__common.md#ga3158d2c2605f66fc22bbf336d780b8bf)(address, data);

72}

73

[ 81](group__ft8xx__reference__api.md#gae96efe5496139f508083a21b2299e3d8)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rd8](group__ft8xx__reference__api.md#gae96efe5496139f508083a21b2299e3d8)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address)

82{

83 return [ft8xx\_rd8](group__ft8xx__common.md#gac7ed90cf4a51fc9139c49ce352a25385)(address);

84}

85

[ 93](group__ft8xx__reference__api.md#ga2f833e24c067f88801884c93766d7ac7)static inline [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [rd16](group__ft8xx__reference__api.md#ga2f833e24c067f88801884c93766d7ac7)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address)

94{

95 return [ft8xx\_rd16](group__ft8xx__common.md#gad52c57f65516917792cb07f6d2f2bf71)(address);

96}

97

[ 105](group__ft8xx__reference__api.md#ga0c6f11426fd5412a66e4f5de0a9f0847)static inline [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [rd32](group__ft8xx__reference__api.md#ga0c6f11426fd5412a66e4f5de0a9f0847)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address)

106{

107 return [ft8xx\_rd32](group__ft8xx__common.md#ga9e78caa02181c65a5c5dac39438ca3e3)(address);

108}

109

110

[ 112](group__ft8xx__reference__api.md#gabf03e1cd7cb18b7c1daf243d4c1dde24)#define OPT\_3D FT8XX\_OPT\_3D

[ 114](group__ft8xx__reference__api.md#ga53f763f1e5de09b5e51242df87af8fb8)#define OPT\_RGB565 FT8XX\_OPT\_RGB565

[ 116](group__ft8xx__reference__api.md#ga2fab787f842bb9193c9df68cb44f93fd)#define OPT\_MONO FT8XX\_OPT\_MONO

[ 118](group__ft8xx__reference__api.md#ga37f793d8ac3af5f518d024727ce9f710)#define OPT\_NODL FT8XX\_OPT\_NODL

[ 120](group__ft8xx__reference__api.md#gaa76b9296cd6f2eb4bec3d650b73e69cc)#define OPT\_FLAT FT8XX\_OPT\_FLAT

[ 122](group__ft8xx__reference__api.md#gae0fef45ae7ca3a45286a19a47bd46943)#define OPT\_SIGNED FT8XX\_OPT\_SIGNED

[ 124](group__ft8xx__reference__api.md#ga65bf92a2956ffee68057ab90be032445)#define OPT\_CENTERX FT8XX\_OPT\_CENTERX

[ 126](group__ft8xx__reference__api.md#gaa28880f2aa7b6d8a51518189ca08382f)#define OPT\_CENTERY FT8XX\_OPT\_CENTERY

[ 128](group__ft8xx__reference__api.md#ga830647bc1b42665e27813a46a6a089b7)#define OPT\_CENTER FT8XX\_OPT\_CENTER

[ 130](group__ft8xx__reference__api.md#gae0088375e797e08fa3e14dc3124c1e90)#define OPT\_RIGHTX FT8XX\_OPT\_RIGHTX

[ 132](group__ft8xx__reference__api.md#ga87b8705ac37fc69704f00cc2a9b8e69e)#define OPT\_NOBACK FT8XX\_OPT\_NOBACK

[ 136](group__ft8xx__reference__api.md#gaed772e3cf2529e698fa8e69ee73f91f9)#define OPT\_NOTICKS FT8XX\_OPT\_NOTICKS

[ 140](group__ft8xx__reference__api.md#ga1e7090a0dbcee600a5472f5fc4343824)#define OPT\_NOHM FT8XX\_OPT\_NOHM

[ 142](group__ft8xx__reference__api.md#ga0eb8abce5677ca0e6948ec1a003958de)#define OPT\_NOPOINTER FT8XX\_OPT\_NOPOINTER

[ 144](group__ft8xx__reference__api.md#ga190c29e3a00685c3f8c4906df37720ae)#define OPT\_NOSECS FT8XX\_OPT\_NOSECS

[ 146](group__ft8xx__reference__api.md#gaa9bc6e351e9fb0515c69f3cd32ad5621)#define OPT\_NOHANDS FT8XX\_OPT\_NOHANDS

147

[ 153](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)static inline void [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) command)

154{

155 [ft8xx\_copro\_cmd](group__ft8xx__copro.md#gae64451b001196d2062d2d0a940dadcee)(command);

156}

157

[ 161](group__ft8xx__reference__api.md#ga7b9b6a41a878c449b107e51eba058799)static inline void [cmd\_dlstart](group__ft8xx__reference__api.md#ga7b9b6a41a878c449b107e51eba058799)(void)

162{

163 [ft8xx\_copro\_cmd\_dlstart](group__ft8xx__copro.md#ga5ac02fe4d5d3af941b3eca7bc18a9602)();

164}

165

[ 169](group__ft8xx__reference__api.md#ga194d7e0d47b3d195155a22f86fbe7e7f)static inline void [cmd\_swap](group__ft8xx__reference__api.md#ga194d7e0d47b3d195155a22f86fbe7e7f)(void)

170{

171 [ft8xx\_copro\_cmd\_swap](group__ft8xx__copro.md#gaa6df956e01bc2919c147f6eafb839929)();

172}

173

[ 188](group__ft8xx__reference__api.md#gad642a54deaa36152ca4fea5e31294732)static inline void [cmd\_text](group__ft8xx__reference__api.md#gad642a54deaa36152ca4fea5e31294732)([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x,

189 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y,

190 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) font,

191 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) options,

192 const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d))

193{

194 [ft8xx\_copro\_cmd\_text](group__ft8xx__copro.md#gac5cf196bb23196642415b73cb377e345)(x, y, font, options, [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d));

195}

196

[ 215](group__ft8xx__reference__api.md#gabdaf9e6cd74c0d157d1673b99707e6f2)static inline void [cmd\_number](group__ft8xx__reference__api.md#gabdaf9e6cd74c0d157d1673b99707e6f2)([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x,

216 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y,

217 [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) font,

218 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) options,

219 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) n)

220{

221 [ft8xx\_copro\_cmd\_number](group__ft8xx__copro.md#ga6193d853b2105a120619343ccaa62c0c)(x, y, font, options, n);

222}

223

[ 235](group__ft8xx__reference__api.md#ga26015112ae4c62a944fe671ea2cb0bda)static inline void [cmd\_calibrate](group__ft8xx__reference__api.md#ga26015112ae4c62a944fe671ea2cb0bda)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result)

236{

237 [ft8xx\_copro\_cmd\_calibrate](group__ft8xx__copro.md#ga770a86ae67d3d30135bc3c48ab4e888b)(result);

238}

239

240

[ 242](group__ft8xx__reference__api.md#ga3746a5c44f711b633ca618b6ebb8e75f)#define BITMAPS FT8XX\_BITMAPS

[ 244](group__ft8xx__reference__api.md#gae6910994a90091fe877b021c590c894e)#define POINTS FT8XX\_POINTS

[ 249](group__ft8xx__reference__api.md#ga321ae946de24c36489276616d13c46cd)#define LINES FT8XX\_LINES

[ 251](group__ft8xx__reference__api.md#gac300cac409c1526ba5622f15472a25df)#define LINE\_STRIP FT8XX\_LINE\_STRIP

[ 253](group__ft8xx__reference__api.md#ga8c7fa2526afa79673d93b64f864d2126)#define EDGE\_STRIP\_R FT8XX\_EDGE\_STRIP\_R

[ 255](group__ft8xx__reference__api.md#ga3434ce2412337ac0b7d9558ff25181d0)#define EDGE\_STRIP\_L FT8XX\_EDGE\_STRIP\_L

[ 257](group__ft8xx__reference__api.md#gaa69720d489114390d9493d397cd392b7)#define EDGE\_STRIP\_A FT8XX\_EDGE\_STRIP\_A

[ 259](group__ft8xx__reference__api.md#ga20ed5346e45eb4ce0e79f094c7346627)#define EDGE\_STRIP\_B FT8XX\_EDGE\_STRIP\_B

[ 264](group__ft8xx__reference__api.md#ga5868720577871792983ae813837c6189)#define RECTS FT8XX\_RECTS

265

[ 289](group__ft8xx__reference__api.md#ga34b42db00c62ff404a8bd7119fc62327)#define BEGIN(prim) FT8XX\_BEGIN(prim)

290

[ 312](group__ft8xx__reference__api.md#ga218ebaaf7d9afe6257021f3c08e59959)#define CLEAR(c, s, t) FT8XX\_CLEAR(c, s, t)

313

[ 323](group__ft8xx__reference__api.md#gae6375b17ea6f06bf81357fe9350e1c1c)#define CLEAR\_COLOR\_RGB(red, green, blue) FT8XX\_CLEAR\_COLOR\_RGB(red, green, blue)

324

[ 335](group__ft8xx__reference__api.md#ga59c390601a75b4d869e7cfc58d2430bf)#define COLOR\_RGB(red, green, blue) FT8XX\_COLOR\_RGB(red, green, blue)

336

[ 342](group__ft8xx__reference__api.md#ga486931aa64c90970e7a4110ada3d0916)#define DISPLAY() FT8XX\_DISPLAY()

343

[ 351](group__ft8xx__reference__api.md#ga569b6a4f889b0846cc0a3396f3835a17)#define END() FT8XX\_END()

352

[ 365](group__ft8xx__reference__api.md#ga8764958e4fa66c3948353226f82cedaf)#define LINE\_WIDTH(width) FT8XX\_LINE\_WIDTH(width)

366

[ 385](group__ft8xx__reference__api.md#ga5f17de6768f32dd36135de83c24d0a7b)#define TAG(s) FT8XX\_TAG(s)

386

[ 399](group__ft8xx__reference__api.md#ga033cea1b18c3f010aaa0293f6972069a)#define VERTEX2F(x, y) FT8XX\_VERTEX2F(x, y)

400

[ 416](group__ft8xx__reference__api.md#gae779df636416e900ddc15b95cf2a923c)#define VERTEX2II(x, y, handle, cell) FT8XX\_VERTEX2II(x, y, handle, cell)

417

418

419#if defined(CONFIG\_FT800)

421enum [ft8xx\_memory\_map\_t](group__ft8xx__reference__api.md#gabbba9344e2d9b81af6313c6b7f12276c) {

422 [RAM\_G](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276ca8f7e484f38038b0a390e7cad119f2cb4) = [FT800\_RAM\_G](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a0f292b470f74c0c625292850d1f6d91c),

423 ROM\_CHIPID = [FT800\_ROM\_CHIPID](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69ae186b0781a832f3adedb21e9d2e05300),

424 ROM\_FONT = [FT800\_ROM\_FONT](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a4f2b840d1343d34a13f5859f35241714),

425 ROM\_FONT\_ADDR = [FT800\_ROM\_FONT\_ADDR](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a0b846c1c3f54c88a66fee75ae1310893),

426 [RAM\_DL](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276caf2eb368364f52dcfc067e40c2a252a84) = [FT800\_RAM\_DL](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69ad7f0dc26c1313aa315bbeba0b648a013),

427 RAM\_PAL = [FT800\_RAM\_PAL](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a5a01dedda4d91a94bb7dd42eeef5f357),

428 [REG\_](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276ca0e42504c57b04103704eb19348fea779) = [FT800\_REG\_](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a4a88dd5f6ec5d1adf451467db195604c),

429 [RAM\_CMD](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276caff47e90e4e3dd7901dfd1cde3fb132f5) = [FT800\_RAM\_CMD](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a2c37aff19d6aa8801f257bc689428373)

430};

431#else /\* Definition of FT810 memory map \*/

[ 433](group__ft8xx__reference__api.md#gabbba9344e2d9b81af6313c6b7f12276c)enum [ft8xx\_memory\_map\_t](group__ft8xx__reference__api.md#gabbba9344e2d9b81af6313c6b7f12276c) {

[ 434](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276ca8f7e484f38038b0a390e7cad119f2cb4) [RAM\_G](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276ca8f7e484f38038b0a390e7cad119f2cb4) = [FT810\_RAM\_G](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeeaa5619b0f2ba721cfc070ee09886af264),

[ 435](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276caf2eb368364f52dcfc067e40c2a252a84) [RAM\_DL](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276caf2eb368364f52dcfc067e40c2a252a84) = [FT810\_RAM\_DL](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeea408b88147f94626dabe1e8b81f72b9ea),

[ 436](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276ca0e42504c57b04103704eb19348fea779) [REG\_](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276ca0e42504c57b04103704eb19348fea779) = [FT810\_REG\_](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeea0f483ff9a2c538fccc2326f431201a57),

[ 437](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276caff47e90e4e3dd7901dfd1cde3fb132f5) [RAM\_CMD](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276caff47e90e4e3dd7901dfd1cde3fb132f5) = [FT810\_RAM\_CMD](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeea06a9355b36b87b1b0fa79a6f468e46bb)

438};

439#endif

440

441#if defined(CONFIG\_FT800)

443enum [ft8xx\_register\_address\_t](group__ft8xx__reference__api.md#gaa3f6afa02b5f4bed90093f659201d008) {

444 [REG\_ID](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a6797b58f7ec24dbf469df8a17680fb7a) = [FT800\_REG\_ID](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7946c63f4dd93692634c08ec0b4657e4),

445 [REG\_FRAMES](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad73c12cf386d92029bef895c52a21272) = [FT800\_REG\_FRAMES](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa45d948244f4decd8863f5def65a78db),

446 [REG\_CLOCK](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a2dd65dd2f5e8f97f27135c343681af64) = [FT800\_REG\_CLOCK](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a46376ddea2bccf9e0af33d78a05f635a),

447 [REG\_FREQUENCY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac447562a0543880a863929676c9a2c21) = [FT800\_REG\_FREQUENCY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a0a864b5230c4ed04ac4a18f7e9c85af5),

448 [REG\_RENDERMODE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aebeab047c1430f0165e36f83e0ff38a9) = [FT800\_REG\_RENDERMODE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a1ca1c284f1f3e2ae75c4874f0c569c7c),

449 [REG\_SNAPY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a9cef87cf60803317580a4bd04762bc9f) = [FT800\_REG\_SNAPY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a6bcedb4e986dba59c0c689356022d992),

450 [REG\_SNAPSHOT](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a81ad0d146fb392f9561bce00c6ed4e6b) = [FT800\_REG\_SNAPSHOT](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a382043bf7f2381a4fad71adeae73db2d),

451 [REG\_CPURESET](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a569c58d9a986415596b91856b02175b2) = [FT800\_REG\_CPURESET](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4411395eca792d4d23f63242fea6307e),

452 [REG\_TAP\_CRC](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a47894772f07899e20c560b47a4b37208) = [FT800\_REG\_TAP\_CRC](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2b36ffdd93c6f41bd08f732099608a99),

453 [REG\_TAP\_MASK](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a87efcd914405639dcf24d762becd1ebd) = [FT800\_REG\_TAP\_MASK](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3c6f1a0898055d4eec3ddfbde56f6a51),

454 [REG\_HCYCLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aec806fab0ed79a1a51e39395147feff2) = [FT800\_REG\_HCYCLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa2b46aa7465a2e38a9947e0b5868f6c7),

455 [REG\_HOFFSET](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a50a3fe216944877cf4a55df00de4bd85) = [FT800\_REG\_HOFFSET](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3179545d22570761b9bf0598ff24219a),

456 [REG\_HSIZE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a3dd43d215eb4b5047b8a14406f85c8e0) = [FT800\_REG\_HSIZE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7b46068735f066e0d2fa6a0ccb073001),

457 [REG\_HSYNC0](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008accb71ca34304a4276f6b8c5d2b2e4e6a) = [FT800\_REG\_HSYNC0](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a5d365f03f5dcd630191f050963c4fc9c),

458 [REG\_HSYNC1](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a13b32d8ce6608067d1f816065547b559) = [FT800\_REG\_HSYNC1](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7c4d1b3a4a5dc128d52fd91352342a70),

459 [REG\_VCYCLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad360af56001df6e29616a11f087db26a) = [FT800\_REG\_VCYCLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aaf8bdfc1924c2269c9db3933499cd23c),

460 [REG\_VOFFSET](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad1b8daf2ec9fe116c79d59b2d524a8a2) = [FT800\_REG\_VOFFSET](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7d9903cc3452f77287ce411c831e6567),

461 [REG\_VSIZE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aa63605dbe4cf7fdb4e1d7994f22aa878) = [FT800\_REG\_VSIZE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2f17cc86a455d13b2f92ada17319a94e),

462 [REG\_VSYNC0](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ae07735ed3259a2112898ee9330cc2050) = [FT800\_REG\_VSYNC0](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a0a6dcbe431ec103262ee805acaee9897),

463 [REG\_VSYNC1](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a3193050a59229830b80c5f637a09ecbb) = [FT800\_REG\_VSYNC1](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6abcd84b4d56e71b558a79f10d97b66ea1),

464 [REG\_DLSWAP](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a9a09798569680c1a48880ec40502e019) = [FT800\_REG\_DLSWAP](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a9f726cc401387bbe8aa3366047467688),

465 [REG\_ROTATE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac785fd2e2498944eec5f404229c1a6f3) = [FT800\_REG\_ROTATE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ab9bf90e77f7946d4466e3b8d444d64e4),

466 [REG\_OUTBITS](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a55841781abfc8d3452399c79d69a2009) = [FT800\_REG\_OUTBITS](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3d5e1b30a5d1889b14b77f8a4bfecf7b),

467 [REG\_DITHER](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a50c524cae48fcba2477cae9c422a3f5b) = [FT800\_REG\_DITHER](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2ba06eef07c7b881c2b331aa090329ed),

468 [REG\_SWIZZLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af1c9622660d41f1ebaf3c5151a8526f6) = [FT800\_REG\_SWIZZLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a161a252ef247cad31f812c88fbfcdf6f),

469 [REG\_CSPREAD](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af57b15505b903b9e8d940e1156bfa83d) = [FT800\_REG\_CSPREAD](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aaf65490a7a4b55309bc8943b065eef17),

470 [REG\_PCLK\_POL](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a1fbe40f257634301cca0229d68851c6b) = [FT800\_REG\_PCLK\_POL](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a9ded0eeda09a9cce3bf111c0a49dd391),

471 [REG\_PCLK](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a572feb4e0547d7b40c18c8ff7ed62b55) = [FT800\_REG\_PCLK](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a8947fb21fa7a7fa4a26bdaea5dbe79c5),

472 [REG\_TAG\_X](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a1ecdf33453fe848f48f0535ca23b5541) = [FT800\_REG\_TAG\_X](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a424e4e6fb301bb6833a46f813fc5895a),

473 [REG\_TAG\_Y](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac41d85f3ba86087e0e0c5c071388d254) = [FT800\_REG\_TAG\_Y](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7f8c3d2a08a68b741ded594eafbfaae4),

474 [REG\_TAG](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac8690647b7274feef7b7a0695eaf9a6b) = [FT800\_REG\_TAG](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a83136b05a9a6f64867f39c50fb0079d2),

475 [REG\_VOL\_PB](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aa024b09fec9d0440483a33e972550888) = [FT800\_REG\_VOL\_PB](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4f0e1449b7ab28bf29f52bf3544c442f),

476 [REG\_VOL\_SOUND](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aac293daf5a8d5221d5c4167177069970) = [FT800\_REG\_VOL\_SOUND](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a5672933c464d2408ad0a6a046fddc1d2),

477 [REG\_SOUND](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008adb67bd48114184e8ad04cadba731e9fe) = [FT800\_REG\_SOUND](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2f0f00e3bbd1b9f9fb09c9d2b65382d7),

478 [REG\_PLAY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a29570336f1d3a7b15d2f5b76a816faa3) = [FT800\_REG\_PLAY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a0187a790b87eca35892431c600248e71),

479 [REG\_GPIO\_DIR](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a7f82f6066010b61ed49a7a8bd2b9b52e) = [FT800\_REG\_GPIO\_DIR](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2c4d02cf887f3ec87b99cd32ae8b355b),

480 [REG\_GPIO](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad92810bdf452c531a7dda338aff3aad1) = [FT800\_REG\_GPIO](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6af7d0154293ba1228a0e04bb923bf9b39),

481

482 [REG\_INT\_FLAGS](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ab6fd90f08477954798d5a54cb1ddce8f) = [FT800\_REG\_INT\_FLAGS](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4fbbc34adc25d9147f2a8007a537ddbd),

483 [REG\_INT\_EN](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a966071326a92ac6e595b2acbb2445697) = [FT800\_REG\_INT\_EN](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa31af794f56d1f4f831ef65c3daf1087),

484 [REG\_INT\_MASK](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aba6637892ddbceafb4e558fbcffe496d) = [FT800\_REG\_INT\_MASK](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa6461f2c17d723ecd672babedbb1e9fc),

485 [REG\_PLAYBACK\_START](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a95f7b2f9eb12abcdf6885ee984155d8e) = [FT800\_REG\_PLAYBACK\_START](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ac159bfb8d704e46aa4be4859d1e476af),

486 [REG\_PLAYBACK\_LENGTH](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aa9f1905d1f2488f5c9600dc4b27753c2) = [FT800\_REG\_PLAYBACK\_LENGTH](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a097806c1c7281e5cbaf0e992888c2e97),

487 [REG\_PLAYBACK\_READPTR](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aed471a111f18c5a92bcc5d7ca07e4b6d) = [FT800\_REG\_PLAYBACK\_READPTR](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aec4e118a3fe1cf3e1f2b5df6b376a651),

488 [REG\_PLAYBACK\_FREQ](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a84a2b99d9ea7f674f019f1d54c1cddc3) = [FT800\_REG\_PLAYBACK\_FREQ](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa8c6fb57011ad08bf0a1d0b48eb5599a),

489 [REG\_PLAYBACK\_FORMAT](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a68e60e0c855fff63e3a6f767f1b0179c) = [FT800\_REG\_PLAYBACK\_FORMAT](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a13f744aa7a089e177a36623239d12961),

490 [REG\_PLAYBACK\_LOOP](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a5b712095cc16ff8866d55b95f6e081e5) = [FT800\_REG\_PLAYBACK\_LOOP](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ab62b5bbfdf948265ad10129ead4d8a63),

491 [REG\_PLAYBACK\_PLAY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a59764d36f28fcf060f164e8fdfb3aba8) = [FT800\_REG\_PLAYBACK\_PLAY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a15006a5d2ab004ca8b5a9a75be095b5b),

492 [REG\_PWM\_HZ](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a884022eead52d6738a4f20f6a543dc50) = [FT800\_REG\_PWM\_HZ](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ac321e2d68978123ab259a2d84d186719),

493 [REG\_PWM\_DUTY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a04f552a92ffd030a0cbc07d522197265) = [FT800\_REG\_PWM\_DUTY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ae14e09a184dbe44390ce7d5576b30d4c),

494 REG\_MACRO\_0 = [FT800\_REG\_MACRO\_0](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ae95328740c30d541b4dc79466734306c),

495 REG\_MACRO\_1 = [FT800\_REG\_MACRO\_1](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a9bce17c193b9c809bef0770bc65b37cf),

496

497 [REG\_CMD\_READ](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af5512106f5e7d41845b1cc01ca52bf68) = [FT800\_REG\_CMD\_READ](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa2cb7424ec77d9a35179824cd2fecb47),

498 [REG\_CMD\_WRITE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad878f3fc41274192245aa6c27209ea69) = [FT800\_REG\_CMD\_WRITE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4911a990964958a6e2bf4842e87ab101),

499 [REG\_CMD\_DL](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac1e6dcc3e508a9f5b8f061a06cda7c87) = [FT800\_REG\_CMD\_DL](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a23f9fdc1d48d6410fc600359842b16ea),

500 [REG\_TOUCH\_MODE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ae53c8a1517586c00ce5e0d19b2bbea29) = [FT800\_REG\_TOUCH\_MODE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ada6b5afbed95413c1988131384c02b1b),

501 [REG\_TOUCH\_ADC\_MODE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a2f0c46b14b1dced78eceb5f21c6a898e) = [FT800\_REG\_TOUCH\_ADC\_MODE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a65b43042fe7dbc44bd15fb472bba33a4),

502 [REG\_TOUCH\_CHARGE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af0baf00d792cf20622f3716ee6c7fa95) = [FT800\_REG\_TOUCH\_CHARGE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a69b981de24b4da81175c9ac74c8454f5),

503 [REG\_TOUCH\_SETTLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a21bec38288166e781f4e42f9e2cd88fb) = [FT800\_REG\_TOUCH\_SETTLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ae02db7afd08bd1c06f6e1f9e06e81d33),

504 [REG\_TOUCH\_OVERSAMPLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a78cb160ba1d417523093ce222504df96) = [FT800\_REG\_TOUCH\_OVERSAMPLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a87e989861d85d683c95e8de44f74f58b),

505 [REG\_TOUCH\_RZTHRESH](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a56440ea6e79d6cb2c6374d8fab01277e) = [FT800\_REG\_TOUCH\_RZTHRESH](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a70f721a708b36ef255270d02680e4e7f),

506 [REG\_TOUCH\_RAW\_XY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a781bc22bc6c5671201a1740a282e1e0d) = [FT800\_REG\_TOUCH\_RAW\_XY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a8ef80aeaaffd974b2e246ad15c98f916),

507 [REG\_TOUCH\_RZ](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad63d6b6752e9a3b25c2d4eec38d9e455) = [FT800\_REG\_TOUCH\_RZ](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ab66136540b44e2f37a0f920fbd3cbcc4),

508 [REG\_TOUCH\_SCREEN\_XY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a857a79d4d62ee1369f10fb746e0d0aa8) = [FT800\_REG\_TOUCH\_SCREEN\_XY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a99fc0fc08ee942b7783951674837d57d),

509 [REG\_TOUCH\_TAG\_XY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a7546d5a7b068c0b23280a189c6345789) = [FT800\_REG\_TOUCH\_TAG\_XY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a86ba740c280900a1dd4273422b9ca8b6),

510 [REG\_TOUCH\_TAG](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a86b3ad977f18ed6948a195f0d0f998af) = [FT800\_REG\_TOUCH\_TAG](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a245e5594218702bc2c30c1b50ec44329),

511 [REG\_TOUCH\_TRANSFORM\_A](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a2725ae9bcc184f701002e0824b6cfdfd) = [FT800\_REG\_TOUCH\_TRANSFORM\_A](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a183fd00d406e113b8b72b8c5b5fc5880),

512 [REG\_TOUCH\_TRANSFORM\_B](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac93146dd21c9a7e07353ae901ccea745) = [FT800\_REG\_TOUCH\_TRANSFORM\_B](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6acd3161021e315e1a2f91f21ccdc48d8a),

513 [REG\_TOUCH\_TRANSFORM\_C](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a8717b3386b1e0ad11e34f7fae83ae793) = [FT800\_REG\_TOUCH\_TRANSFORM\_C](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4b3e903dfed68a7eb7f7734e18aca9e0),

514 [REG\_TOUCH\_TRANSFORM\_D](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a9988ada9b469290b9c886ba665fb4b48) = [FT800\_REG\_TOUCH\_TRANSFORM\_D](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a386a6293cd82485934b3865bd3f1956b),

515 [REG\_TOUCH\_TRANSFORM\_E](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a36c4f53d2e132c794695983e56cf627c) = [FT800\_REG\_TOUCH\_TRANSFORM\_E](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4f188f88f9a032fdb6f3c87ed352d4bb),

516 [REG\_TOUCH\_TRANSFORM\_F](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a041ffbb78a6572c5c1e515843f959315) = [FT800\_REG\_TOUCH\_TRANSFORM\_F](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a1d01f5fe890a4d7670cf91a7cd48402f),

517

518 [REG\_TOUCH\_DIRECT\_XY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ae8dddb1bf87f77e70a03c4ad73ba51fd) = [FT800\_REG\_TOUCH\_DIRECT\_XY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a1745bb57bcf9872b308c49a151a43f1f),

519 [REG\_TOUCH\_DIRECT\_Z1Z2](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a43e6c3532c2f9573e31ddd4ce12fb8c0) = [FT800\_REG\_TOUCH\_DIRECT\_Z1Z2](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a43bcc194c075b385073ed73a562b8cfa),

520

521 [REG\_TRACKER](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad99a270479fd9ce96e1868fb708bacbb) = [FT800\_REG\_TRACKER](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3397b2a86a97997d01780d52ec23b84c)

522};

523#else /\* Definition of FT810 registers \*/

[ 525](group__ft8xx__reference__api.md#gaa3f6afa02b5f4bed90093f659201d008)enum [ft8xx\_register\_address\_t](group__ft8xx__reference__api.md#gaa3f6afa02b5f4bed90093f659201d008) {

[ 526](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a683a15e3c7578fe44f7cee9ca5796f74) [REG\_TRIM](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a683a15e3c7578fe44f7cee9ca5796f74) = [FT810\_REG\_TRIM](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ad35d6fc19bc4fe86802105c48489553e),

527

[ 528](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a6797b58f7ec24dbf469df8a17680fb7a) [REG\_ID](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a6797b58f7ec24dbf469df8a17680fb7a) = [FT810\_REG\_ID](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8e81832420166c89993a4f0629d5765d),

[ 529](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad73c12cf386d92029bef895c52a21272) [REG\_FRAMES](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad73c12cf386d92029bef895c52a21272) = [FT810\_REG\_FRAMES](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab75607baa4c4121c34364f4118f990d2),

[ 530](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a2dd65dd2f5e8f97f27135c343681af64) [REG\_CLOCK](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a2dd65dd2f5e8f97f27135c343681af64) = [FT810\_REG\_CLOCK](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a222e9d43895af76d103f9fbd09c40832),

[ 531](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac447562a0543880a863929676c9a2c21) [REG\_FREQUENCY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac447562a0543880a863929676c9a2c21) = [FT810\_REG\_FREQUENCY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a3f09f2fd706996b97173f587637aee53),

[ 532](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aebeab047c1430f0165e36f83e0ff38a9) [REG\_RENDERMODE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aebeab047c1430f0165e36f83e0ff38a9) = [FT810\_REG\_RENDERMODE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a32f5dfe4ebc13114ecf9336670f74a31),

[ 533](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a9cef87cf60803317580a4bd04762bc9f) [REG\_SNAPY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a9cef87cf60803317580a4bd04762bc9f) = [FT810\_REG\_SNAPY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a1f9721ea190d82af17332d60cb8eb795),

[ 534](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a81ad0d146fb392f9561bce00c6ed4e6b) [REG\_SNAPSHOT](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a81ad0d146fb392f9561bce00c6ed4e6b) = [FT810\_REG\_SNAPSHOT](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a104e72273989d38213fc070b4fd4a676),

[ 535](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a569c58d9a986415596b91856b02175b2) [REG\_CPURESET](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a569c58d9a986415596b91856b02175b2) = [FT810\_REG\_CPURESET](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae2bae2d6191190c95a76e4cc1a6bc9d1),

[ 536](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a47894772f07899e20c560b47a4b37208) [REG\_TAP\_CRC](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a47894772f07899e20c560b47a4b37208) = [FT810\_REG\_TAP\_CRC](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a6e302da1712f086b26d08e46f7a9f1d1),

[ 537](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a87efcd914405639dcf24d762becd1ebd) [REG\_TAP\_MASK](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a87efcd914405639dcf24d762becd1ebd) = [FT810\_REG\_TAP\_MASK](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a369d654c43692ef193493063338888aa),

[ 538](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aec806fab0ed79a1a51e39395147feff2) [REG\_HCYCLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aec806fab0ed79a1a51e39395147feff2) = [FT810\_REG\_HCYCLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a68ae24f87a50c7790ac987c6e2ccab2b),

[ 539](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a50a3fe216944877cf4a55df00de4bd85) [REG\_HOFFSET](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a50a3fe216944877cf4a55df00de4bd85) = [FT810\_REG\_HOFFSET](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a95853b0fc36aca1c168611334a39037f),

[ 540](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a3dd43d215eb4b5047b8a14406f85c8e0) [REG\_HSIZE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a3dd43d215eb4b5047b8a14406f85c8e0) = [FT810\_REG\_HSIZE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af89832af70c53e320337f633985ce295),

[ 541](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008accb71ca34304a4276f6b8c5d2b2e4e6a) [REG\_HSYNC0](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008accb71ca34304a4276f6b8c5d2b2e4e6a) = [FT810\_REG\_HSYNC0](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a086b28d18b9c49e51ef734c2f6e6ce21),

[ 542](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a13b32d8ce6608067d1f816065547b559) [REG\_HSYNC1](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a13b32d8ce6608067d1f816065547b559) = [FT810\_REG\_HSYNC1](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a533ec4682d3b9649a59e012a53ab55de),

[ 543](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad360af56001df6e29616a11f087db26a) [REG\_VCYCLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad360af56001df6e29616a11f087db26a) = [FT810\_REG\_VCYCLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a9e43b1a3872c21a26981a35c03fea93d),

[ 544](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad1b8daf2ec9fe116c79d59b2d524a8a2) [REG\_VOFFSET](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad1b8daf2ec9fe116c79d59b2d524a8a2) = [FT810\_REG\_VOFFSET](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a2a155f858da556270114a3f9d989ef85),

[ 545](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aa63605dbe4cf7fdb4e1d7994f22aa878) [REG\_VSIZE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aa63605dbe4cf7fdb4e1d7994f22aa878) = [FT810\_REG\_VSIZE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352acafecb336293cd24b363e33ca9fdce5a),

[ 546](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ae07735ed3259a2112898ee9330cc2050) [REG\_VSYNC0](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ae07735ed3259a2112898ee9330cc2050) = [FT810\_REG\_VSYNC0](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352afd3caed713df1d318d62cbd73fdfe3c6),

[ 547](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a3193050a59229830b80c5f637a09ecbb) [REG\_VSYNC1](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a3193050a59229830b80c5f637a09ecbb) = [FT810\_REG\_VSYNC1](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a3deeabcda1f9453dc2d865e8b19715a8),

[ 548](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a9a09798569680c1a48880ec40502e019) [REG\_DLSWAP](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a9a09798569680c1a48880ec40502e019) = [FT810\_REG\_DLSWAP](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352afb81eec26bd13732949ae8f8186fdd26),

[ 549](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac785fd2e2498944eec5f404229c1a6f3) [REG\_ROTATE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac785fd2e2498944eec5f404229c1a6f3) = [FT810\_REG\_ROTATE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a54935aeb6c13623f68c5c74c3db722ff),

[ 550](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a55841781abfc8d3452399c79d69a2009) [REG\_OUTBITS](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a55841781abfc8d3452399c79d69a2009) = [FT810\_REG\_OUTBITS](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aff30b9219c582c8ceac17f115a18375d),

[ 551](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a50c524cae48fcba2477cae9c422a3f5b) [REG\_DITHER](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a50c524cae48fcba2477cae9c422a3f5b) = [FT810\_REG\_DITHER](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a61e1d7c2e2ed9a0ee4b372dd9c7df63a),

[ 552](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af1c9622660d41f1ebaf3c5151a8526f6) [REG\_SWIZZLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af1c9622660d41f1ebaf3c5151a8526f6) = [FT810\_REG\_SWIZZLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ad633919822dadc636420824948e75315),

[ 553](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af57b15505b903b9e8d940e1156bfa83d) [REG\_CSPREAD](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af57b15505b903b9e8d940e1156bfa83d) = [FT810\_REG\_CSPREAD](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352abfa8c39566c4c41501588b815a5c52ad),

[ 554](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a1fbe40f257634301cca0229d68851c6b) [REG\_PCLK\_POL](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a1fbe40f257634301cca0229d68851c6b) = [FT810\_REG\_PCLK\_POL](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a83d5ff35dc2d6af8e461a45ea2239af6),

[ 555](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a572feb4e0547d7b40c18c8ff7ed62b55) [REG\_PCLK](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a572feb4e0547d7b40c18c8ff7ed62b55) = [FT810\_REG\_PCLK](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aff03cfb6400f883999cc01c0cf832812),

[ 556](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a1ecdf33453fe848f48f0535ca23b5541) [REG\_TAG\_X](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a1ecdf33453fe848f48f0535ca23b5541) = [FT810\_REG\_TAG\_X](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab45bcc55b80d016ef2ac8ea98ace2108),

[ 557](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac41d85f3ba86087e0e0c5c071388d254) [REG\_TAG\_Y](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac41d85f3ba86087e0e0c5c071388d254) = [FT810\_REG\_TAG\_Y](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a22089e51c2e0e4d373589c398a54ca05),

[ 558](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac8690647b7274feef7b7a0695eaf9a6b) [REG\_TAG](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac8690647b7274feef7b7a0695eaf9a6b) = [FT810\_REG\_TAG](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af8919f80edc86615089d8bafd40f68fd),

[ 559](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aa024b09fec9d0440483a33e972550888) [REG\_VOL\_PB](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aa024b09fec9d0440483a33e972550888) = [FT810\_REG\_VOL\_PB](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aade1a34c921a4d22fe87aa6575bef164),

[ 560](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aac293daf5a8d5221d5c4167177069970) [REG\_VOL\_SOUND](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aac293daf5a8d5221d5c4167177069970) = [FT810\_REG\_VOL\_SOUND](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a98246b3329620a8e252d7ee4a302783e),

[ 561](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008adb67bd48114184e8ad04cadba731e9fe) [REG\_SOUND](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008adb67bd48114184e8ad04cadba731e9fe) = [FT810\_REG\_SOUND](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a5d019d200409c2dd4b57f727afedf815),

[ 562](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a29570336f1d3a7b15d2f5b76a816faa3) [REG\_PLAY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a29570336f1d3a7b15d2f5b76a816faa3) = [FT810\_REG\_PLAY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab83798a30fa11e5e6d7f8e197b0327a4),

[ 563](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a7f82f6066010b61ed49a7a8bd2b9b52e) [REG\_GPIO\_DIR](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a7f82f6066010b61ed49a7a8bd2b9b52e) = [FT810\_REG\_GPIO\_DIR](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aba2af4d5da3f34693261ef48710d22ee),

[ 564](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad92810bdf452c531a7dda338aff3aad1) [REG\_GPIO](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad92810bdf452c531a7dda338aff3aad1) = [FT810\_REG\_GPIO](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab7400ab33f66708dd08fcf8ae543dba5),

[ 565](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a538bc67838a34c6f1dfbb8bdff984788) [REG\_GPIOX\_DIR](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a538bc67838a34c6f1dfbb8bdff984788) = [FT810\_REG\_GPIOX\_DIR](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aec26223f49f0b0b2d418fb0f6a340f8b),

[ 566](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008adc4499b79053ad08a2279b3702b79ced) [REG\_GPIOX](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008adc4499b79053ad08a2279b3702b79ced) = [FT810\_REG\_GPIOX](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae45783e98c43d87be2667155efbafbca),

567

[ 568](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ab6fd90f08477954798d5a54cb1ddce8f) [REG\_INT\_FLAGS](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ab6fd90f08477954798d5a54cb1ddce8f) = [FT810\_REG\_INT\_FLAGS](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352afcc92c93fe9dd983cd13dd5beb91ee9f),

[ 569](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a966071326a92ac6e595b2acbb2445697) [REG\_INT\_EN](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a966071326a92ac6e595b2acbb2445697) = [FT810\_REG\_INT\_EN](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a6ad1c0050228bfdfca87bca6a4a0a571),

[ 570](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aba6637892ddbceafb4e558fbcffe496d) [REG\_INT\_MASK](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aba6637892ddbceafb4e558fbcffe496d) = [FT810\_REG\_INT\_MASK](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a5a21ce38ac3699f4c9e5f8f0e7bc8555),

[ 571](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a95f7b2f9eb12abcdf6885ee984155d8e) [REG\_PLAYBACK\_START](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a95f7b2f9eb12abcdf6885ee984155d8e) = [FT810\_REG\_PLAYBACK\_START](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab45c8dab2a9d9e7f2c02e40205b957fe),

[ 572](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aa9f1905d1f2488f5c9600dc4b27753c2) [REG\_PLAYBACK\_LENGTH](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aa9f1905d1f2488f5c9600dc4b27753c2) = [FT810\_REG\_PLAYBACK\_LENGTH](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a206979e1f9edf49aca24f8afb07e7f48),

[ 573](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aed471a111f18c5a92bcc5d7ca07e4b6d) [REG\_PLAYBACK\_READPTR](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aed471a111f18c5a92bcc5d7ca07e4b6d) = [FT810\_REG\_PLAYBACK\_READPTR](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a60dd200c41f58057d20169ff833d4f82),

[ 574](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a84a2b99d9ea7f674f019f1d54c1cddc3) [REG\_PLAYBACK\_FREQ](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a84a2b99d9ea7f674f019f1d54c1cddc3) = [FT810\_REG\_PLAYBACK\_FREQ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8f85d80231d8978144112e41b375ccc7),

[ 575](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a68e60e0c855fff63e3a6f767f1b0179c) [REG\_PLAYBACK\_FORMAT](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a68e60e0c855fff63e3a6f767f1b0179c) = [FT810\_REG\_PLAYBACK\_FORMAT](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a304779eb0c7eca705a3c9fbf3d23fdb2),

[ 576](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a5b712095cc16ff8866d55b95f6e081e5) [REG\_PLAYBACK\_LOOP](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a5b712095cc16ff8866d55b95f6e081e5) = [FT810\_REG\_PLAYBACK\_LOOP](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a0b2882f45164307c678cba35232bcbf9),

[ 577](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a59764d36f28fcf060f164e8fdfb3aba8) [REG\_PLAYBACK\_PLAY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a59764d36f28fcf060f164e8fdfb3aba8) = [FT810\_REG\_PLAYBACK\_PLAY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aeba859d489260879a08e922c04e9ca8e),

[ 578](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a884022eead52d6738a4f20f6a543dc50) [REG\_PWM\_HZ](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a884022eead52d6738a4f20f6a543dc50) = [FT810\_REG\_PWM\_HZ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a75c68657acd7582c3028f0802d155771),

[ 579](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a04f552a92ffd030a0cbc07d522197265) [REG\_PWM\_DUTY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a04f552a92ffd030a0cbc07d522197265) = [FT810\_REG\_PWM\_DUTY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a0558ac04acd45a6bf1e9100ec3a0a278),

580

[ 581](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af5512106f5e7d41845b1cc01ca52bf68) [REG\_CMD\_READ](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af5512106f5e7d41845b1cc01ca52bf68) = [FT810\_REG\_CMD\_READ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a81b9c8fd550b60b9b4cd1aae7a97efb9),

[ 582](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad878f3fc41274192245aa6c27209ea69) [REG\_CMD\_WRITE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad878f3fc41274192245aa6c27209ea69) = [FT810\_REG\_CMD\_WRITE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae2b2865e053ed356d915a6f9afd62caf),

[ 583](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac1e6dcc3e508a9f5b8f061a06cda7c87) [REG\_CMD\_DL](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac1e6dcc3e508a9f5b8f061a06cda7c87) = [FT810\_REG\_CMD\_DL](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae393b55425eb2f67bb289e0e2041649c),

[ 584](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ae53c8a1517586c00ce5e0d19b2bbea29) [REG\_TOUCH\_MODE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ae53c8a1517586c00ce5e0d19b2bbea29) = [FT810\_REG\_TOUCH\_MODE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a67e068b57d9917ba093bfb8b073cf712),

[ 585](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a2f0c46b14b1dced78eceb5f21c6a898e) [REG\_TOUCH\_ADC\_MODE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a2f0c46b14b1dced78eceb5f21c6a898e) = [FT810\_REG\_TOUCH\_ADC\_MODE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a2bb9ad22a0d93b7facb92f49be1ac63a),

[ 586](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af0baf00d792cf20622f3716ee6c7fa95) [REG\_TOUCH\_CHARGE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af0baf00d792cf20622f3716ee6c7fa95) = [FT810\_REG\_TOUCH\_CHARGE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae54293de74687bf2db5fdf9b0682ca44),

[ 587](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a21bec38288166e781f4e42f9e2cd88fb) [REG\_TOUCH\_SETTLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a21bec38288166e781f4e42f9e2cd88fb) = [FT810\_REG\_TOUCH\_SETTLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a0e712682bd8d083f0ee25b284c242cdf),

[ 588](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a78cb160ba1d417523093ce222504df96) [REG\_TOUCH\_OVERSAMPLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a78cb160ba1d417523093ce222504df96) = [FT810\_REG\_TOUCH\_OVERSAMPLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a779e92fbc0655c0889a3760025f8880a),

[ 589](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a56440ea6e79d6cb2c6374d8fab01277e) [REG\_TOUCH\_RZTHRESH](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a56440ea6e79d6cb2c6374d8fab01277e) = [FT810\_REG\_TOUCH\_RZTHRESH](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa102086576124d6931a3a08673e8fc0d),

[ 590](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a781bc22bc6c5671201a1740a282e1e0d) [REG\_TOUCH\_RAW\_XY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a781bc22bc6c5671201a1740a282e1e0d) = [FT810\_REG\_TOUCH\_RAW\_XY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a359efc1f478e7653bb567fcfa20fb575),

[ 591](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad63d6b6752e9a3b25c2d4eec38d9e455) [REG\_TOUCH\_RZ](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad63d6b6752e9a3b25c2d4eec38d9e455) = [FT810\_REG\_TOUCH\_RZ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a6a0dee898cc286ec6a2f91536fb0c8b4),

[ 592](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a857a79d4d62ee1369f10fb746e0d0aa8) [REG\_TOUCH\_SCREEN\_XY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a857a79d4d62ee1369f10fb746e0d0aa8) = [FT810\_REG\_TOUCH\_SCREEN\_XY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af62bbcce8fca40ef48253ed77959ff55),

[ 593](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a7546d5a7b068c0b23280a189c6345789) [REG\_TOUCH\_TAG\_XY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a7546d5a7b068c0b23280a189c6345789) = [FT810\_REG\_TOUCH\_TAG\_XY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a4e6013b98cf73db7e09b7952f1f29e5b),

[ 594](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a86b3ad977f18ed6948a195f0d0f998af) [REG\_TOUCH\_TAG](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a86b3ad977f18ed6948a195f0d0f998af) = [FT810\_REG\_TOUCH\_TAG](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a97ef048be3e5f39cc5ce6e7f12326a23),

[ 595](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a2725ae9bcc184f701002e0824b6cfdfd) [REG\_TOUCH\_TRANSFORM\_A](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a2725ae9bcc184f701002e0824b6cfdfd) = [FT810\_REG\_TOUCH\_TRANSFORM\_A](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa2341295c30b0121eeb8d117764a5baf),

[ 596](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac93146dd21c9a7e07353ae901ccea745) [REG\_TOUCH\_TRANSFORM\_B](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac93146dd21c9a7e07353ae901ccea745) = [FT810\_REG\_TOUCH\_TRANSFORM\_B](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa25eab9796730236361b037fc522509d),

[ 597](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a8717b3386b1e0ad11e34f7fae83ae793) [REG\_TOUCH\_TRANSFORM\_C](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a8717b3386b1e0ad11e34f7fae83ae793) = [FT810\_REG\_TOUCH\_TRANSFORM\_C](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aaafde672b6470275a6055520a0534bb2),

[ 598](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a9988ada9b469290b9c886ba665fb4b48) [REG\_TOUCH\_TRANSFORM\_D](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a9988ada9b469290b9c886ba665fb4b48) = [FT810\_REG\_TOUCH\_TRANSFORM\_D](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a71f116560ffc21a45eece099f0155e52),

[ 599](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a36c4f53d2e132c794695983e56cf627c) [REG\_TOUCH\_TRANSFORM\_E](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a36c4f53d2e132c794695983e56cf627c) = [FT810\_REG\_TOUCH\_TRANSFORM\_E](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa61ca8fc286257f7f70057a5026b0867),

[ 600](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a041ffbb78a6572c5c1e515843f959315) [REG\_TOUCH\_TRANSFORM\_F](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a041ffbb78a6572c5c1e515843f959315) = [FT810\_REG\_TOUCH\_TRANSFORM\_F](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a03912bde6f4ad32381c50772b89ec2bc),

[ 601](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a8feeb5e4fbc73322825fdd392dbec950) [REG\_TOUCH\_CONFIG](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a8feeb5e4fbc73322825fdd392dbec950) = [FT810\_REG\_TOUCH\_CONFIG](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a1190faa2c60e6a2dc8661eb7da7461c6),

602

[ 603](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aa382cb5b65f2803e94ce4451ed75b848) [REG\_SPI\_WIDTH](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aa382cb5b65f2803e94ce4451ed75b848) = [FT810\_REG\_SPI\_WIDTH](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8366bdc17c88345c80aab6f061090312),

604

[ 605](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ae8dddb1bf87f77e70a03c4ad73ba51fd) [REG\_TOUCH\_DIRECT\_XY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ae8dddb1bf87f77e70a03c4ad73ba51fd) = [FT810\_REG\_TOUCH\_DIRECT\_XY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8807a786fb4c6d42e739a32b3f6078f8),

[ 606](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a43e6c3532c2f9573e31ddd4ce12fb8c0) [REG\_TOUCH\_DIRECT\_Z1Z2](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a43e6c3532c2f9573e31ddd4ce12fb8c0) = [FT810\_REG\_TOUCH\_DIRECT\_Z1Z2](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ad439205ca55294a850c88e9f87fb08b4),

607

[ 608](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a327a78d411cf247a6ee6e4ea5541c90c) [REG\_CMDB\_SPACE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a327a78d411cf247a6ee6e4ea5541c90c) = [FT810\_REG\_CMDB\_SPACE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a85c5d599f609c97e80cf87fd0d922784),

[ 609](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ae86016e9d0fb6db20d2c585300759464) [REG\_CMDB\_WRITE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ae86016e9d0fb6db20d2c585300759464) = [FT810\_REG\_CMDB\_WRITE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aea1698cade20d8ab5807d60a7e4dbb3b),

610

[ 611](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad99a270479fd9ce96e1868fb708bacbb) [REG\_TRACKER](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad99a270479fd9ce96e1868fb708bacbb) = [FT810\_REG\_TRACKER](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a43adc41a79ea8af3bbf769b796f7c223),

[ 612](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a49d311578982dec5afa589b0963d0622) [REG\_TRACKER1](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a49d311578982dec5afa589b0963d0622) = [FT810\_REG\_TRACKER1](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aebe60fc86ac3088108447de01191bc4e),

[ 613](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a3bbab48e1bdad06303e631f62d7bcd76) [REG\_TRACKER2](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a3bbab48e1bdad06303e631f62d7bcd76) = [FT810\_REG\_TRACKER2](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af6d6ece41191d230932dbfaae10c0762),

[ 614](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac4852d6d1ee6c7b69a3f4386354d5f2c) [REG\_TRACKER3](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac4852d6d1ee6c7b69a3f4386354d5f2c) = [FT810\_REG\_TRACKER3](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a4449f285050e761b3fd78feebefe4335),

[ 615](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac3f442ac6c0010066270e8373efeefcf) [REG\_TRACKER4](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac3f442ac6c0010066270e8373efeefcf) = [FT810\_REG\_TRACKER4](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a9a887d54a3ba0dad157fafddc6573aed),

[ 616](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a529da48e0b241ae16e8cbf1d38653c97) [REG\_MEDIAFIFO\_READ](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a529da48e0b241ae16e8cbf1d38653c97) = [FT810\_REG\_MEDIAFIFO\_READ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8da19290bfcd66b76ff929bb9dd3e568),

[ 617](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a11a7b5722d9de6c62222a5c76f0b692b) [REG\_MEDIAFIFO\_WRITE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a11a7b5722d9de6c62222a5c76f0b692b) = [FT810\_REG\_MEDIAFIFO\_WRITE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa905904989c14075318323a10fac0abe),

618};

619#endif

620

624

625#ifdef \_\_cplusplus

626}

627#endif

628

629#endif /\* ZEPHYR\_DRIVERS\_MISC\_FT8XX\_FT8XX\_REFERENCE\_API\_H\_ \*/

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

[ft8xx\_common.h](ft8xx__common_8h.md)

FT8XX common functions.

[ft8xx\_copro.h](ft8xx__copro_8h.md)

FT8XX coprocessor functions.

[ft8xx\_dl.h](ft8xx__dl_8h.md)

FT8XX display list commands.

[ft8xx\_memory.h](ft8xx__memory_8h.md)

FT8XX memory map.

[ft8xx\_wr32](group__ft8xx__common.md#ga3158d2c2605f66fc22bbf336d780b8bf)

void ft8xx\_wr32(uint32\_t address, uint32\_t data)

Write 4 bytes (32 bits) to FT8xx memory.

[ft8xx\_wr8](group__ft8xx__common.md#ga7623499f328d820b1e84d2a3834a89a2)

void ft8xx\_wr8(uint32\_t address, uint8\_t data)

Write 1 byte (8 bits) to FT8xx memory.

[ft8xx\_rd32](group__ft8xx__common.md#ga9e78caa02181c65a5c5dac39438ca3e3)

uint32\_t ft8xx\_rd32(uint32\_t address)

Read 4 bytes (32 bits) from FT8xx memory.

[ft8xx\_rd8](group__ft8xx__common.md#gac7ed90cf4a51fc9139c49ce352a25385)

uint8\_t ft8xx\_rd8(uint32\_t address)

Read 1 byte (8 bits) from FT8xx memory.

[ft8xx\_rd16](group__ft8xx__common.md#gad52c57f65516917792cb07f6d2f2bf71)

uint16\_t ft8xx\_rd16(uint32\_t address)

Read 2 bytes (16 bits) from FT8xx memory.

[ft8xx\_wr16](group__ft8xx__common.md#gadfbff24d8fb246081cefbc51190b32e5)

void ft8xx\_wr16(uint32\_t address, uint16\_t data)

Write 2 bytes (16 bits) to FT8xx memory.

[ft8xx\_copro\_cmd\_dlstart](group__ft8xx__copro.md#ga5ac02fe4d5d3af941b3eca7bc18a9602)

void ft8xx\_copro\_cmd\_dlstart(void)

Start a new display list.

[ft8xx\_copro\_cmd\_number](group__ft8xx__copro.md#ga6193d853b2105a120619343ccaa62c0c)

void ft8xx\_copro\_cmd\_number(int16\_t x, int16\_t y, int16\_t font, uint16\_t options, int32\_t n)

Draw a decimal number.

[ft8xx\_copro\_cmd\_calibrate](group__ft8xx__copro.md#ga770a86ae67d3d30135bc3c48ab4e888b)

void ft8xx\_copro\_cmd\_calibrate(uint32\_t \*result)

Execute the touch screen calibration routine.

[ft8xx\_copro\_cmd\_swap](group__ft8xx__copro.md#gaa6df956e01bc2919c147f6eafb839929)

void ft8xx\_copro\_cmd\_swap(void)

Swap the current display list.

[ft8xx\_copro\_cmd\_text](group__ft8xx__copro.md#gac5cf196bb23196642415b73cb377e345)

void ft8xx\_copro\_cmd\_text(int16\_t x, int16\_t y, int16\_t font, uint16\_t options, const char \*s)

Draw text.

[ft8xx\_copro\_cmd](group__ft8xx__copro.md#gae64451b001196d2062d2d0a940dadcee)

void ft8xx\_copro\_cmd(uint32\_t cmd)

Execute a display list command by co-processor engine.

[FT800\_REG\_PLAY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a0187a790b87eca35892431c600248e71)

@ FT800\_REG\_PLAY

**Definition** ft8xx\_memory.h:82

[FT800\_REG\_PLAYBACK\_LENGTH](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a097806c1c7281e5cbaf0e992888c2e97)

@ FT800\_REG\_PLAYBACK\_LENGTH

**Definition** ft8xx\_memory.h:90

[FT800\_REG\_VSYNC0](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a0a6dcbe431ec103262ee805acaee9897)

@ FT800\_REG\_VSYNC0

**Definition** ft8xx\_memory.h:66

[FT800\_REG\_FREQUENCY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a0a864b5230c4ed04ac4a18f7e9c85af5)

@ FT800\_REG\_FREQUENCY

**Definition** ft8xx\_memory.h:51

[FT800\_REG\_PLAYBACK\_FORMAT](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a13f744aa7a089e177a36623239d12961)

@ FT800\_REG\_PLAYBACK\_FORMAT

**Definition** ft8xx\_memory.h:93

[FT800\_REG\_PLAYBACK\_PLAY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a15006a5d2ab004ca8b5a9a75be095b5b)

@ FT800\_REG\_PLAYBACK\_PLAY

**Definition** ft8xx\_memory.h:95

[FT800\_REG\_SWIZZLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a161a252ef247cad31f812c88fbfcdf6f)

@ FT800\_REG\_SWIZZLE

**Definition** ft8xx\_memory.h:72

[FT800\_REG\_TOUCH\_DIRECT\_XY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a1745bb57bcf9872b308c49a151a43f1f)

@ FT800\_REG\_TOUCH\_DIRECT\_XY

**Definition** ft8xx\_memory.h:122

[FT800\_REG\_TOUCH\_TRANSFORM\_A](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a183fd00d406e113b8b72b8c5b5fc5880)

@ FT800\_REG\_TOUCH\_TRANSFORM\_A

**Definition** ft8xx\_memory.h:115

[FT800\_REG\_RENDERMODE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a1ca1c284f1f3e2ae75c4874f0c569c7c)

@ FT800\_REG\_RENDERMODE

**Definition** ft8xx\_memory.h:52

[FT800\_REG\_TOUCH\_TRANSFORM\_F](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a1d01f5fe890a4d7670cf91a7cd48402f)

@ FT800\_REG\_TOUCH\_TRANSFORM\_F

**Definition** ft8xx\_memory.h:120

[FT800\_REG\_CMD\_DL](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a23f9fdc1d48d6410fc600359842b16ea)

@ FT800\_REG\_CMD\_DL

**Definition** ft8xx\_memory.h:103

[FT800\_REG\_TOUCH\_TAG](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a245e5594218702bc2c30c1b50ec44329)

@ FT800\_REG\_TOUCH\_TAG

**Definition** ft8xx\_memory.h:114

[FT800\_REG\_TAP\_CRC](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2b36ffdd93c6f41bd08f732099608a99)

@ FT800\_REG\_TAP\_CRC

**Definition** ft8xx\_memory.h:56

[FT800\_REG\_DITHER](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2ba06eef07c7b881c2b331aa090329ed)

@ FT800\_REG\_DITHER

**Definition** ft8xx\_memory.h:71

[FT800\_REG\_GPIO\_DIR](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2c4d02cf887f3ec87b99cd32ae8b355b)

@ FT800\_REG\_GPIO\_DIR

**Definition** ft8xx\_memory.h:83

[FT800\_REG\_SOUND](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2f0f00e3bbd1b9f9fb09c9d2b65382d7)

@ FT800\_REG\_SOUND

**Definition** ft8xx\_memory.h:81

[FT800\_REG\_VSIZE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a2f17cc86a455d13b2f92ada17319a94e)

@ FT800\_REG\_VSIZE

**Definition** ft8xx\_memory.h:65

[FT800\_REG\_HOFFSET](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3179545d22570761b9bf0598ff24219a)

@ FT800\_REG\_HOFFSET

**Definition** ft8xx\_memory.h:59

[FT800\_REG\_TRACKER](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3397b2a86a97997d01780d52ec23b84c)

@ FT800\_REG\_TRACKER

**Definition** ft8xx\_memory.h:125

[FT800\_REG\_SNAPSHOT](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a382043bf7f2381a4fad71adeae73db2d)

@ FT800\_REG\_SNAPSHOT

**Definition** ft8xx\_memory.h:54

[FT800\_REG\_TOUCH\_TRANSFORM\_D](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a386a6293cd82485934b3865bd3f1956b)

@ FT800\_REG\_TOUCH\_TRANSFORM\_D

**Definition** ft8xx\_memory.h:118

[FT800\_REG\_TAP\_MASK](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3c6f1a0898055d4eec3ddfbde56f6a51)

@ FT800\_REG\_TAP\_MASK

**Definition** ft8xx\_memory.h:57

[FT800\_REG\_OUTBITS](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a3d5e1b30a5d1889b14b77f8a4bfecf7b)

@ FT800\_REG\_OUTBITS

**Definition** ft8xx\_memory.h:70

[FT800\_REG\_TAG\_X](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a424e4e6fb301bb6833a46f813fc5895a)

@ FT800\_REG\_TAG\_X

**Definition** ft8xx\_memory.h:76

[FT800\_REG\_TOUCH\_DIRECT\_Z1Z2](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a43bcc194c075b385073ed73a562b8cfa)

@ FT800\_REG\_TOUCH\_DIRECT\_Z1Z2

**Definition** ft8xx\_memory.h:123

[FT800\_REG\_CPURESET](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4411395eca792d4d23f63242fea6307e)

@ FT800\_REG\_CPURESET

**Definition** ft8xx\_memory.h:55

[FT800\_REG\_CLOCK](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a46376ddea2bccf9e0af33d78a05f635a)

@ FT800\_REG\_CLOCK

**Definition** ft8xx\_memory.h:50

[FT800\_REG\_CMD\_WRITE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4911a990964958a6e2bf4842e87ab101)

@ FT800\_REG\_CMD\_WRITE

**Definition** ft8xx\_memory.h:102

[FT800\_REG\_TOUCH\_TRANSFORM\_C](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4b3e903dfed68a7eb7f7734e18aca9e0)

@ FT800\_REG\_TOUCH\_TRANSFORM\_C

**Definition** ft8xx\_memory.h:117

[FT800\_REG\_VOL\_PB](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4f0e1449b7ab28bf29f52bf3544c442f)

@ FT800\_REG\_VOL\_PB

**Definition** ft8xx\_memory.h:79

[FT800\_REG\_TOUCH\_TRANSFORM\_E](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4f188f88f9a032fdb6f3c87ed352d4bb)

@ FT800\_REG\_TOUCH\_TRANSFORM\_E

**Definition** ft8xx\_memory.h:119

[FT800\_REG\_INT\_FLAGS](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a4fbbc34adc25d9147f2a8007a537ddbd)

@ FT800\_REG\_INT\_FLAGS

**Definition** ft8xx\_memory.h:86

[FT800\_REG\_VOL\_SOUND](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a5672933c464d2408ad0a6a046fddc1d2)

@ FT800\_REG\_VOL\_SOUND

**Definition** ft8xx\_memory.h:80

[FT800\_REG\_HSYNC0](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a5d365f03f5dcd630191f050963c4fc9c)

@ FT800\_REG\_HSYNC0

**Definition** ft8xx\_memory.h:61

[FT800\_REG\_TOUCH\_ADC\_MODE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a65b43042fe7dbc44bd15fb472bba33a4)

@ FT800\_REG\_TOUCH\_ADC\_MODE

**Definition** ft8xx\_memory.h:105

[FT800\_REG\_TOUCH\_CHARGE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a69b981de24b4da81175c9ac74c8454f5)

@ FT800\_REG\_TOUCH\_CHARGE

**Definition** ft8xx\_memory.h:106

[FT800\_REG\_SNAPY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a6bcedb4e986dba59c0c689356022d992)

@ FT800\_REG\_SNAPY

**Definition** ft8xx\_memory.h:53

[FT800\_REG\_TOUCH\_RZTHRESH](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a70f721a708b36ef255270d02680e4e7f)

@ FT800\_REG\_TOUCH\_RZTHRESH

**Definition** ft8xx\_memory.h:109

[FT800\_REG\_ID](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7946c63f4dd93692634c08ec0b4657e4)

@ FT800\_REG\_ID

**Definition** ft8xx\_memory.h:48

[FT800\_REG\_HSIZE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7b46068735f066e0d2fa6a0ccb073001)

@ FT800\_REG\_HSIZE

**Definition** ft8xx\_memory.h:60

[FT800\_REG\_HSYNC1](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7c4d1b3a4a5dc128d52fd91352342a70)

@ FT800\_REG\_HSYNC1

**Definition** ft8xx\_memory.h:62

[FT800\_REG\_VOFFSET](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7d9903cc3452f77287ce411c831e6567)

@ FT800\_REG\_VOFFSET

**Definition** ft8xx\_memory.h:64

[FT800\_REG\_TAG\_Y](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a7f8c3d2a08a68b741ded594eafbfaae4)

@ FT800\_REG\_TAG\_Y

**Definition** ft8xx\_memory.h:77

[FT800\_REG\_TAG](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a83136b05a9a6f64867f39c50fb0079d2)

@ FT800\_REG\_TAG

**Definition** ft8xx\_memory.h:78

[FT800\_REG\_TOUCH\_TAG\_XY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a86ba740c280900a1dd4273422b9ca8b6)

@ FT800\_REG\_TOUCH\_TAG\_XY

**Definition** ft8xx\_memory.h:113

[FT800\_REG\_TOUCH\_OVERSAMPLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a87e989861d85d683c95e8de44f74f58b)

@ FT800\_REG\_TOUCH\_OVERSAMPLE

**Definition** ft8xx\_memory.h:108

[FT800\_REG\_PCLK](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a8947fb21fa7a7fa4a26bdaea5dbe79c5)

@ FT800\_REG\_PCLK

**Definition** ft8xx\_memory.h:75

[FT800\_REG\_TOUCH\_RAW\_XY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a8ef80aeaaffd974b2e246ad15c98f916)

@ FT800\_REG\_TOUCH\_RAW\_XY

**Definition** ft8xx\_memory.h:110

[FT800\_REG\_TOUCH\_SCREEN\_XY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a99fc0fc08ee942b7783951674837d57d)

@ FT800\_REG\_TOUCH\_SCREEN\_XY

**Definition** ft8xx\_memory.h:112

[FT800\_REG\_MACRO\_1](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a9bce17c193b9c809bef0770bc65b37cf)

@ FT800\_REG\_MACRO\_1

**Definition** ft8xx\_memory.h:99

[FT800\_REG\_PCLK\_POL](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a9ded0eeda09a9cce3bf111c0a49dd391)

@ FT800\_REG\_PCLK\_POL

**Definition** ft8xx\_memory.h:74

[FT800\_REG\_DLSWAP](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6a9f726cc401387bbe8aa3366047467688)

@ FT800\_REG\_DLSWAP

**Definition** ft8xx\_memory.h:68

[FT800\_REG\_HCYCLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa2b46aa7465a2e38a9947e0b5868f6c7)

@ FT800\_REG\_HCYCLE

**Definition** ft8xx\_memory.h:58

[FT800\_REG\_CMD\_READ](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa2cb7424ec77d9a35179824cd2fecb47)

@ FT800\_REG\_CMD\_READ

**Definition** ft8xx\_memory.h:101

[FT800\_REG\_INT\_EN](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa31af794f56d1f4f831ef65c3daf1087)

@ FT800\_REG\_INT\_EN

**Definition** ft8xx\_memory.h:87

[FT800\_REG\_FRAMES](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa45d948244f4decd8863f5def65a78db)

@ FT800\_REG\_FRAMES

**Definition** ft8xx\_memory.h:49

[FT800\_REG\_INT\_MASK](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa6461f2c17d723ecd672babedbb1e9fc)

@ FT800\_REG\_INT\_MASK

**Definition** ft8xx\_memory.h:88

[FT800\_REG\_PLAYBACK\_FREQ](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aa8c6fb57011ad08bf0a1d0b48eb5599a)

@ FT800\_REG\_PLAYBACK\_FREQ

**Definition** ft8xx\_memory.h:92

[FT800\_REG\_CSPREAD](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aaf65490a7a4b55309bc8943b065eef17)

@ FT800\_REG\_CSPREAD

**Definition** ft8xx\_memory.h:73

[FT800\_REG\_VCYCLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aaf8bdfc1924c2269c9db3933499cd23c)

@ FT800\_REG\_VCYCLE

**Definition** ft8xx\_memory.h:63

[FT800\_REG\_PLAYBACK\_LOOP](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ab62b5bbfdf948265ad10129ead4d8a63)

@ FT800\_REG\_PLAYBACK\_LOOP

**Definition** ft8xx\_memory.h:94

[FT800\_REG\_TOUCH\_RZ](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ab66136540b44e2f37a0f920fbd3cbcc4)

@ FT800\_REG\_TOUCH\_RZ

**Definition** ft8xx\_memory.h:111

[FT800\_REG\_ROTATE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ab9bf90e77f7946d4466e3b8d444d64e4)

@ FT800\_REG\_ROTATE

**Definition** ft8xx\_memory.h:69

[FT800\_REG\_VSYNC1](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6abcd84b4d56e71b558a79f10d97b66ea1)

@ FT800\_REG\_VSYNC1

**Definition** ft8xx\_memory.h:67

[FT800\_REG\_PLAYBACK\_START](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ac159bfb8d704e46aa4be4859d1e476af)

@ FT800\_REG\_PLAYBACK\_START

**Definition** ft8xx\_memory.h:89

[FT800\_REG\_PWM\_HZ](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ac321e2d68978123ab259a2d84d186719)

@ FT800\_REG\_PWM\_HZ

**Definition** ft8xx\_memory.h:96

[FT800\_REG\_TOUCH\_TRANSFORM\_B](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6acd3161021e315e1a2f91f21ccdc48d8a)

@ FT800\_REG\_TOUCH\_TRANSFORM\_B

**Definition** ft8xx\_memory.h:116

[FT800\_REG\_TOUCH\_MODE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ada6b5afbed95413c1988131384c02b1b)

@ FT800\_REG\_TOUCH\_MODE

**Definition** ft8xx\_memory.h:104

[FT800\_REG\_TOUCH\_SETTLE](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ae02db7afd08bd1c06f6e1f9e06e81d33)

@ FT800\_REG\_TOUCH\_SETTLE

**Definition** ft8xx\_memory.h:107

[FT800\_REG\_PWM\_DUTY](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ae14e09a184dbe44390ce7d5576b30d4c)

@ FT800\_REG\_PWM\_DUTY

**Definition** ft8xx\_memory.h:97

[FT800\_REG\_MACRO\_0](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6ae95328740c30d541b4dc79466734306c)

@ FT800\_REG\_MACRO\_0

**Definition** ft8xx\_memory.h:98

[FT800\_REG\_PLAYBACK\_READPTR](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6aec4e118a3fe1cf3e1f2b5df6b376a651)

@ FT800\_REG\_PLAYBACK\_READPTR

**Definition** ft8xx\_memory.h:91

[FT800\_REG\_GPIO](group__ft8xx__memory.md#gga3c885b333acd851fed4d74886656d2c6af7d0154293ba1228a0e04bb923bf9b39)

@ FT800\_REG\_GPIO

**Definition** ft8xx\_memory.h:84

[FT810\_REG\_TOUCH\_TRANSFORM\_F](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a03912bde6f4ad32381c50772b89ec2bc)

@ FT810\_REG\_TOUCH\_TRANSFORM\_F

**Definition** ft8xx\_memory.h:204

[FT810\_REG\_PWM\_DUTY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a0558ac04acd45a6bf1e9100ec3a0a278)

@ FT810\_REG\_PWM\_DUTY

**Definition** ft8xx\_memory.h:183

[FT810\_REG\_HSYNC0](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a086b28d18b9c49e51ef734c2f6e6ce21)

@ FT810\_REG\_HSYNC0

**Definition** ft8xx\_memory.h:145

[FT810\_REG\_PLAYBACK\_LOOP](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a0b2882f45164307c678cba35232bcbf9)

@ FT810\_REG\_PLAYBACK\_LOOP

**Definition** ft8xx\_memory.h:180

[FT810\_REG\_TOUCH\_SETTLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a0e712682bd8d083f0ee25b284c242cdf)

@ FT810\_REG\_TOUCH\_SETTLE

**Definition** ft8xx\_memory.h:191

[FT810\_REG\_SNAPSHOT](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a104e72273989d38213fc070b4fd4a676)

@ FT810\_REG\_SNAPSHOT

**Definition** ft8xx\_memory.h:138

[FT810\_REG\_TOUCH\_CONFIG](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a1190faa2c60e6a2dc8661eb7da7461c6)

@ FT810\_REG\_TOUCH\_CONFIG

**Definition** ft8xx\_memory.h:205

[FT810\_REG\_SNAPY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a1f9721ea190d82af17332d60cb8eb795)

@ FT810\_REG\_SNAPY

**Definition** ft8xx\_memory.h:137

[FT810\_REG\_PLAYBACK\_LENGTH](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a206979e1f9edf49aca24f8afb07e7f48)

@ FT810\_REG\_PLAYBACK\_LENGTH

**Definition** ft8xx\_memory.h:176

[FT810\_REG\_TAG\_Y](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a22089e51c2e0e4d373589c398a54ca05)

@ FT810\_REG\_TAG\_Y

**Definition** ft8xx\_memory.h:161

[FT810\_REG\_CLOCK](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a222e9d43895af76d103f9fbd09c40832)

@ FT810\_REG\_CLOCK

**Definition** ft8xx\_memory.h:134

[FT810\_REG\_VOFFSET](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a2a155f858da556270114a3f9d989ef85)

@ FT810\_REG\_VOFFSET

**Definition** ft8xx\_memory.h:148

[FT810\_REG\_TOUCH\_ADC\_MODE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a2bb9ad22a0d93b7facb92f49be1ac63a)

@ FT810\_REG\_TOUCH\_ADC\_MODE

**Definition** ft8xx\_memory.h:189

[FT810\_REG\_PLAYBACK\_FORMAT](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a304779eb0c7eca705a3c9fbf3d23fdb2)

@ FT810\_REG\_PLAYBACK\_FORMAT

**Definition** ft8xx\_memory.h:179

[FT810\_REG\_RENDERMODE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a32f5dfe4ebc13114ecf9336670f74a31)

@ FT810\_REG\_RENDERMODE

**Definition** ft8xx\_memory.h:136

[FT810\_REG\_TOUCH\_RAW\_XY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a359efc1f478e7653bb567fcfa20fb575)

@ FT810\_REG\_TOUCH\_RAW\_XY

**Definition** ft8xx\_memory.h:194

[FT810\_REG\_TAP\_MASK](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a369d654c43692ef193493063338888aa)

@ FT810\_REG\_TAP\_MASK

**Definition** ft8xx\_memory.h:141

[FT810\_REG\_VSYNC1](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a3deeabcda1f9453dc2d865e8b19715a8)

@ FT810\_REG\_VSYNC1

**Definition** ft8xx\_memory.h:151

[FT810\_REG\_FREQUENCY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a3f09f2fd706996b97173f587637aee53)

@ FT810\_REG\_FREQUENCY

**Definition** ft8xx\_memory.h:135

[FT810\_REG\_TRACKER](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a43adc41a79ea8af3bbf769b796f7c223)

@ FT810\_REG\_TRACKER

**Definition** ft8xx\_memory.h:215

[FT810\_REG\_TRACKER3](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a4449f285050e761b3fd78feebefe4335)

@ FT810\_REG\_TRACKER3

**Definition** ft8xx\_memory.h:218

[FT810\_REG\_TOUCH\_TAG\_XY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a4e6013b98cf73db7e09b7952f1f29e5b)

@ FT810\_REG\_TOUCH\_TAG\_XY

**Definition** ft8xx\_memory.h:197

[FT810\_REG\_HSYNC1](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a533ec4682d3b9649a59e012a53ab55de)

@ FT810\_REG\_HSYNC1

**Definition** ft8xx\_memory.h:146

[FT810\_REG\_ROTATE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a54935aeb6c13623f68c5c74c3db722ff)

@ FT810\_REG\_ROTATE

**Definition** ft8xx\_memory.h:153

[FT810\_REG\_INT\_MASK](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a5a21ce38ac3699f4c9e5f8f0e7bc8555)

@ FT810\_REG\_INT\_MASK

**Definition** ft8xx\_memory.h:174

[FT810\_REG\_SOUND](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a5d019d200409c2dd4b57f727afedf815)

@ FT810\_REG\_SOUND

**Definition** ft8xx\_memory.h:165

[FT810\_REG\_PLAYBACK\_READPTR](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a60dd200c41f58057d20169ff833d4f82)

@ FT810\_REG\_PLAYBACK\_READPTR

**Definition** ft8xx\_memory.h:177

[FT810\_REG\_DITHER](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a61e1d7c2e2ed9a0ee4b372dd9c7df63a)

@ FT810\_REG\_DITHER

**Definition** ft8xx\_memory.h:155

[FT810\_REG\_TOUCH\_MODE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a67e068b57d9917ba093bfb8b073cf712)

@ FT810\_REG\_TOUCH\_MODE

**Definition** ft8xx\_memory.h:188

[FT810\_REG\_HCYCLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a68ae24f87a50c7790ac987c6e2ccab2b)

@ FT810\_REG\_HCYCLE

**Definition** ft8xx\_memory.h:142

[FT810\_REG\_TOUCH\_RZ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a6a0dee898cc286ec6a2f91536fb0c8b4)

@ FT810\_REG\_TOUCH\_RZ

**Definition** ft8xx\_memory.h:195

[FT810\_REG\_INT\_EN](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a6ad1c0050228bfdfca87bca6a4a0a571)

@ FT810\_REG\_INT\_EN

**Definition** ft8xx\_memory.h:173

[FT810\_REG\_TAP\_CRC](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a6e302da1712f086b26d08e46f7a9f1d1)

@ FT810\_REG\_TAP\_CRC

**Definition** ft8xx\_memory.h:140

[FT810\_REG\_TOUCH\_TRANSFORM\_D](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a71f116560ffc21a45eece099f0155e52)

@ FT810\_REG\_TOUCH\_TRANSFORM\_D

**Definition** ft8xx\_memory.h:202

[FT810\_REG\_PWM\_HZ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a75c68657acd7582c3028f0802d155771)

@ FT810\_REG\_PWM\_HZ

**Definition** ft8xx\_memory.h:182

[FT810\_REG\_TOUCH\_OVERSAMPLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a779e92fbc0655c0889a3760025f8880a)

@ FT810\_REG\_TOUCH\_OVERSAMPLE

**Definition** ft8xx\_memory.h:192

[FT810\_REG\_CMD\_READ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a81b9c8fd550b60b9b4cd1aae7a97efb9)

@ FT810\_REG\_CMD\_READ

**Definition** ft8xx\_memory.h:185

[FT810\_REG\_SPI\_WIDTH](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8366bdc17c88345c80aab6f061090312)

@ FT810\_REG\_SPI\_WIDTH

**Definition** ft8xx\_memory.h:207

[FT810\_REG\_PCLK\_POL](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a83d5ff35dc2d6af8e461a45ea2239af6)

@ FT810\_REG\_PCLK\_POL

**Definition** ft8xx\_memory.h:158

[FT810\_REG\_CMDB\_SPACE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a85c5d599f609c97e80cf87fd0d922784)

@ FT810\_REG\_CMDB\_SPACE

**Definition** ft8xx\_memory.h:212

[FT810\_REG\_TOUCH\_DIRECT\_XY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8807a786fb4c6d42e739a32b3f6078f8)

@ FT810\_REG\_TOUCH\_DIRECT\_XY

**Definition** ft8xx\_memory.h:209

[FT810\_REG\_MEDIAFIFO\_READ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8da19290bfcd66b76ff929bb9dd3e568)

@ FT810\_REG\_MEDIAFIFO\_READ

**Definition** ft8xx\_memory.h:220

[FT810\_REG\_ID](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8e81832420166c89993a4f0629d5765d)

@ FT810\_REG\_ID

**Definition** ft8xx\_memory.h:132

[FT810\_REG\_PLAYBACK\_FREQ](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a8f85d80231d8978144112e41b375ccc7)

@ FT810\_REG\_PLAYBACK\_FREQ

**Definition** ft8xx\_memory.h:178

[FT810\_REG\_HOFFSET](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a95853b0fc36aca1c168611334a39037f)

@ FT810\_REG\_HOFFSET

**Definition** ft8xx\_memory.h:143

[FT810\_REG\_TOUCH\_TAG](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a97ef048be3e5f39cc5ce6e7f12326a23)

@ FT810\_REG\_TOUCH\_TAG

**Definition** ft8xx\_memory.h:198

[FT810\_REG\_VOL\_SOUND](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a98246b3329620a8e252d7ee4a302783e)

@ FT810\_REG\_VOL\_SOUND

**Definition** ft8xx\_memory.h:164

[FT810\_REG\_TRACKER4](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a9a887d54a3ba0dad157fafddc6573aed)

@ FT810\_REG\_TRACKER4

**Definition** ft8xx\_memory.h:219

[FT810\_REG\_VCYCLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352a9e43b1a3872c21a26981a35c03fea93d)

@ FT810\_REG\_VCYCLE

**Definition** ft8xx\_memory.h:147

[FT810\_REG\_TOUCH\_RZTHRESH](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa102086576124d6931a3a08673e8fc0d)

@ FT810\_REG\_TOUCH\_RZTHRESH

**Definition** ft8xx\_memory.h:193

[FT810\_REG\_TOUCH\_TRANSFORM\_A](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa2341295c30b0121eeb8d117764a5baf)

@ FT810\_REG\_TOUCH\_TRANSFORM\_A

**Definition** ft8xx\_memory.h:199

[FT810\_REG\_TOUCH\_TRANSFORM\_B](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa25eab9796730236361b037fc522509d)

@ FT810\_REG\_TOUCH\_TRANSFORM\_B

**Definition** ft8xx\_memory.h:200

[FT810\_REG\_TOUCH\_TRANSFORM\_E](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa61ca8fc286257f7f70057a5026b0867)

@ FT810\_REG\_TOUCH\_TRANSFORM\_E

**Definition** ft8xx\_memory.h:203

[FT810\_REG\_MEDIAFIFO\_WRITE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aa905904989c14075318323a10fac0abe)

@ FT810\_REG\_MEDIAFIFO\_WRITE

**Definition** ft8xx\_memory.h:221

[FT810\_REG\_TOUCH\_TRANSFORM\_C](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aaafde672b6470275a6055520a0534bb2)

@ FT810\_REG\_TOUCH\_TRANSFORM\_C

**Definition** ft8xx\_memory.h:201

[FT810\_REG\_VOL\_PB](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aade1a34c921a4d22fe87aa6575bef164)

@ FT810\_REG\_VOL\_PB

**Definition** ft8xx\_memory.h:163

[FT810\_REG\_TAG\_X](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab45bcc55b80d016ef2ac8ea98ace2108)

@ FT810\_REG\_TAG\_X

**Definition** ft8xx\_memory.h:160

[FT810\_REG\_PLAYBACK\_START](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab45c8dab2a9d9e7f2c02e40205b957fe)

@ FT810\_REG\_PLAYBACK\_START

**Definition** ft8xx\_memory.h:175

[FT810\_REG\_GPIO](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab7400ab33f66708dd08fcf8ae543dba5)

@ FT810\_REG\_GPIO

**Definition** ft8xx\_memory.h:168

[FT810\_REG\_FRAMES](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab75607baa4c4121c34364f4118f990d2)

@ FT810\_REG\_FRAMES

**Definition** ft8xx\_memory.h:133

[FT810\_REG\_PLAY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ab83798a30fa11e5e6d7f8e197b0327a4)

@ FT810\_REG\_PLAY

**Definition** ft8xx\_memory.h:166

[FT810\_REG\_GPIO\_DIR](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aba2af4d5da3f34693261ef48710d22ee)

@ FT810\_REG\_GPIO\_DIR

**Definition** ft8xx\_memory.h:167

[FT810\_REG\_CSPREAD](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352abfa8c39566c4c41501588b815a5c52ad)

@ FT810\_REG\_CSPREAD

**Definition** ft8xx\_memory.h:157

[FT810\_REG\_VSIZE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352acafecb336293cd24b363e33ca9fdce5a)

@ FT810\_REG\_VSIZE

**Definition** ft8xx\_memory.h:149

[FT810\_REG\_TRIM](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ad35d6fc19bc4fe86802105c48489553e)

@ FT810\_REG\_TRIM

**Definition** ft8xx\_memory.h:130

[FT810\_REG\_TOUCH\_DIRECT\_Z1Z2](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ad439205ca55294a850c88e9f87fb08b4)

@ FT810\_REG\_TOUCH\_DIRECT\_Z1Z2

**Definition** ft8xx\_memory.h:210

[FT810\_REG\_SWIZZLE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ad633919822dadc636420824948e75315)

@ FT810\_REG\_SWIZZLE

**Definition** ft8xx\_memory.h:156

[FT810\_REG\_CMD\_WRITE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae2b2865e053ed356d915a6f9afd62caf)

@ FT810\_REG\_CMD\_WRITE

**Definition** ft8xx\_memory.h:186

[FT810\_REG\_CPURESET](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae2bae2d6191190c95a76e4cc1a6bc9d1)

@ FT810\_REG\_CPURESET

**Definition** ft8xx\_memory.h:139

[FT810\_REG\_CMD\_DL](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae393b55425eb2f67bb289e0e2041649c)

@ FT810\_REG\_CMD\_DL

**Definition** ft8xx\_memory.h:187

[FT810\_REG\_GPIOX](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae45783e98c43d87be2667155efbafbca)

@ FT810\_REG\_GPIOX

**Definition** ft8xx\_memory.h:170

[FT810\_REG\_TOUCH\_CHARGE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352ae54293de74687bf2db5fdf9b0682ca44)

@ FT810\_REG\_TOUCH\_CHARGE

**Definition** ft8xx\_memory.h:190

[FT810\_REG\_CMDB\_WRITE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aea1698cade20d8ab5807d60a7e4dbb3b)

@ FT810\_REG\_CMDB\_WRITE

**Definition** ft8xx\_memory.h:213

[FT810\_REG\_PLAYBACK\_PLAY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aeba859d489260879a08e922c04e9ca8e)

@ FT810\_REG\_PLAYBACK\_PLAY

**Definition** ft8xx\_memory.h:181

[FT810\_REG\_TRACKER1](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aebe60fc86ac3088108447de01191bc4e)

@ FT810\_REG\_TRACKER1

**Definition** ft8xx\_memory.h:216

[FT810\_REG\_GPIOX\_DIR](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aec26223f49f0b0b2d418fb0f6a340f8b)

@ FT810\_REG\_GPIOX\_DIR

**Definition** ft8xx\_memory.h:169

[FT810\_REG\_TOUCH\_SCREEN\_XY](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af62bbcce8fca40ef48253ed77959ff55)

@ FT810\_REG\_TOUCH\_SCREEN\_XY

**Definition** ft8xx\_memory.h:196

[FT810\_REG\_TRACKER2](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af6d6ece41191d230932dbfaae10c0762)

@ FT810\_REG\_TRACKER2

**Definition** ft8xx\_memory.h:217

[FT810\_REG\_TAG](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af8919f80edc86615089d8bafd40f68fd)

@ FT810\_REG\_TAG

**Definition** ft8xx\_memory.h:162

[FT810\_REG\_HSIZE](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352af89832af70c53e320337f633985ce295)

@ FT810\_REG\_HSIZE

**Definition** ft8xx\_memory.h:144

[FT810\_REG\_DLSWAP](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352afb81eec26bd13732949ae8f8186fdd26)

@ FT810\_REG\_DLSWAP

**Definition** ft8xx\_memory.h:152

[FT810\_REG\_INT\_FLAGS](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352afcc92c93fe9dd983cd13dd5beb91ee9f)

@ FT810\_REG\_INT\_FLAGS

**Definition** ft8xx\_memory.h:172

[FT810\_REG\_VSYNC0](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352afd3caed713df1d318d62cbd73fdfe3c6)

@ FT810\_REG\_VSYNC0

**Definition** ft8xx\_memory.h:150

[FT810\_REG\_PCLK](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aff03cfb6400f883999cc01c0cf832812)

@ FT810\_REG\_PCLK

**Definition** ft8xx\_memory.h:159

[FT810\_REG\_OUTBITS](group__ft8xx__memory.md#gga495a8c0706389e9b3677846d772eb352aff30b9219c582c8ceac17f115a18375d)

@ FT810\_REG\_OUTBITS

**Definition** ft8xx\_memory.h:154

[FT810\_RAM\_CMD](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeea06a9355b36b87b1b0fa79a6f468e46bb)

@ FT810\_RAM\_CMD

**Definition** ft8xx\_memory.h:43

[FT810\_REG\_](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeea0f483ff9a2c538fccc2326f431201a57)

@ FT810\_REG\_

**Definition** ft8xx\_memory.h:42

[FT810\_RAM\_DL](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeea408b88147f94626dabe1e8b81f72b9ea)

@ FT810\_RAM\_DL

**Definition** ft8xx\_memory.h:41

[FT810\_RAM\_G](group__ft8xx__memory.md#gga6c8d08697812fb4e6292ff533e753aeeaa5619b0f2ba721cfc070ee09886af264)

@ FT810\_RAM\_G

**Definition** ft8xx\_memory.h:40

[FT800\_ROM\_FONT\_ADDR](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a0b846c1c3f54c88a66fee75ae1310893)

@ FT800\_ROM\_FONT\_ADDR

**Definition** ft8xx\_memory.h:31

[FT800\_RAM\_G](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a0f292b470f74c0c625292850d1f6d91c)

@ FT800\_RAM\_G

**Definition** ft8xx\_memory.h:28

[FT800\_RAM\_CMD](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a2c37aff19d6aa8801f257bc689428373)

@ FT800\_RAM\_CMD

**Definition** ft8xx\_memory.h:35

[FT800\_REG\_](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a4a88dd5f6ec5d1adf451467db195604c)

@ FT800\_REG\_

**Definition** ft8xx\_memory.h:34

[FT800\_ROM\_FONT](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a4f2b840d1343d34a13f5859f35241714)

@ FT800\_ROM\_FONT

**Definition** ft8xx\_memory.h:30

[FT800\_RAM\_PAL](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69a5a01dedda4d91a94bb7dd42eeef5f357)

@ FT800\_RAM\_PAL

**Definition** ft8xx\_memory.h:33

[FT800\_RAM\_DL](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69ad7f0dc26c1313aa315bbeba0b648a013)

@ FT800\_RAM\_DL

**Definition** ft8xx\_memory.h:32

[FT800\_ROM\_CHIPID](group__ft8xx__memory.md#gga91adc1665d20e88c087ddb10b5e5ef69ae186b0781a832f3adedb21e9d2e05300)

@ FT800\_ROM\_CHIPID

**Definition** ft8xx\_memory.h:29

[rd32](group__ft8xx__reference__api.md#ga0c6f11426fd5412a66e4f5de0a9f0847)

static uint32\_t rd32(uint32\_t address)

Read 4 bytes (32 bits) from FT8xx memory.

**Definition** ft8xx\_reference\_api.h:105

[cmd\_swap](group__ft8xx__reference__api.md#ga194d7e0d47b3d195155a22f86fbe7e7f)

static void cmd\_swap(void)

Swap the current display list.

**Definition** ft8xx\_reference\_api.h:169

[wr8](group__ft8xx__reference__api.md#ga1e9c6203ebb7cc15a736d074bd98c181)

static void wr8(uint32\_t address, uint8\_t data)

Write 1 byte (8 bits) to FT8xx memory.

**Definition** ft8xx\_reference\_api.h:47

[cmd\_calibrate](group__ft8xx__reference__api.md#ga26015112ae4c62a944fe671ea2cb0bda)

static void cmd\_calibrate(uint32\_t \*result)

Execute the touch screen calibration routine.

**Definition** ft8xx\_reference\_api.h:235

[rd16](group__ft8xx__reference__api.md#ga2f833e24c067f88801884c93766d7ac7)

static uint16\_t rd16(uint32\_t address)

Read 2 bytes (16 bits) from FT8xx memory.

**Definition** ft8xx\_reference\_api.h:93

[wr32](group__ft8xx__reference__api.md#ga3f6814650684e2c2100d8f9a36505ca0)

static void wr32(uint32\_t address, uint32\_t data)

Write 4 bytes (32 bits) to FT8xx memory.

**Definition** ft8xx\_reference\_api.h:69

[cmd\_dlstart](group__ft8xx__reference__api.md#ga7b9b6a41a878c449b107e51eba058799)

static void cmd\_dlstart(void)

Start a new display list.

**Definition** ft8xx\_reference\_api.h:161

[wr16](group__ft8xx__reference__api.md#ga8fac4ed55f7ef9d82d8dcb0eb6f09eab)

static void wr16(uint32\_t address, uint16\_t data)

Write 2 bytes (16 bits) to FT8xx memory.

**Definition** ft8xx\_reference\_api.h:58

[ft8xx\_register\_address\_t](group__ft8xx__reference__api.md#gaa3f6afa02b5f4bed90093f659201d008)

ft8xx\_register\_address\_t

FT810 register addresses.

**Definition** ft8xx\_reference\_api.h:525

[ft8xx\_memory\_map\_t](group__ft8xx__reference__api.md#gabbba9344e2d9b81af6313c6b7f12276c)

ft8xx\_memory\_map\_t

Main parts of FT810 memory map.

**Definition** ft8xx\_reference\_api.h:433

[cmd\_number](group__ft8xx__reference__api.md#gabdaf9e6cd74c0d157d1673b99707e6f2)

static void cmd\_number(int16\_t x, int16\_t y, int16\_t font, uint16\_t options, int32\_t n)

Draw a decimal number.

**Definition** ft8xx\_reference\_api.h:215

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[cmd\_text](group__ft8xx__reference__api.md#gad642a54deaa36152ca4fea5e31294732)

static void cmd\_text(int16\_t x, int16\_t y, int16\_t font, uint16\_t options, const char \*s)

Draw text.

**Definition** ft8xx\_reference\_api.h:188

[rd8](group__ft8xx__reference__api.md#gae96efe5496139f508083a21b2299e3d8)

static uint8\_t rd8(uint32\_t address)

Read 1 byte (8 bits) from FT8xx memory.

**Definition** ft8xx\_reference\_api.h:81

[REG\_TOUCH\_TRANSFORM\_F](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a041ffbb78a6572c5c1e515843f959315)

@ REG\_TOUCH\_TRANSFORM\_F

**Definition** ft8xx\_reference\_api.h:600

[REG\_PWM\_DUTY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a04f552a92ffd030a0cbc07d522197265)

@ REG\_PWM\_DUTY

**Definition** ft8xx\_reference\_api.h:579

[REG\_MEDIAFIFO\_WRITE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a11a7b5722d9de6c62222a5c76f0b692b)

@ REG\_MEDIAFIFO\_WRITE

**Definition** ft8xx\_reference\_api.h:617

[REG\_HSYNC1](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a13b32d8ce6608067d1f816065547b559)

@ REG\_HSYNC1

**Definition** ft8xx\_reference\_api.h:542

[REG\_TAG\_X](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a1ecdf33453fe848f48f0535ca23b5541)

@ REG\_TAG\_X

**Definition** ft8xx\_reference\_api.h:556

[REG\_PCLK\_POL](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a1fbe40f257634301cca0229d68851c6b)

@ REG\_PCLK\_POL

**Definition** ft8xx\_reference\_api.h:554

[REG\_TOUCH\_SETTLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a21bec38288166e781f4e42f9e2cd88fb)

@ REG\_TOUCH\_SETTLE

**Definition** ft8xx\_reference\_api.h:587

[REG\_TOUCH\_TRANSFORM\_A](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a2725ae9bcc184f701002e0824b6cfdfd)

@ REG\_TOUCH\_TRANSFORM\_A

**Definition** ft8xx\_reference\_api.h:595

[REG\_PLAY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a29570336f1d3a7b15d2f5b76a816faa3)

@ REG\_PLAY

**Definition** ft8xx\_reference\_api.h:562

[REG\_CLOCK](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a2dd65dd2f5e8f97f27135c343681af64)

@ REG\_CLOCK

**Definition** ft8xx\_reference\_api.h:530

[REG\_TOUCH\_ADC\_MODE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a2f0c46b14b1dced78eceb5f21c6a898e)

@ REG\_TOUCH\_ADC\_MODE

**Definition** ft8xx\_reference\_api.h:585

[REG\_VSYNC1](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a3193050a59229830b80c5f637a09ecbb)

@ REG\_VSYNC1

**Definition** ft8xx\_reference\_api.h:547

[REG\_CMDB\_SPACE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a327a78d411cf247a6ee6e4ea5541c90c)

@ REG\_CMDB\_SPACE

**Definition** ft8xx\_reference\_api.h:608

[REG\_TOUCH\_TRANSFORM\_E](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a36c4f53d2e132c794695983e56cf627c)

@ REG\_TOUCH\_TRANSFORM\_E

**Definition** ft8xx\_reference\_api.h:599

[REG\_TRACKER2](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a3bbab48e1bdad06303e631f62d7bcd76)

@ REG\_TRACKER2

**Definition** ft8xx\_reference\_api.h:613

[REG\_HSIZE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a3dd43d215eb4b5047b8a14406f85c8e0)

@ REG\_HSIZE

**Definition** ft8xx\_reference\_api.h:540

[REG\_TOUCH\_DIRECT\_Z1Z2](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a43e6c3532c2f9573e31ddd4ce12fb8c0)

@ REG\_TOUCH\_DIRECT\_Z1Z2

**Definition** ft8xx\_reference\_api.h:606

[REG\_TAP\_CRC](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a47894772f07899e20c560b47a4b37208)

@ REG\_TAP\_CRC

**Definition** ft8xx\_reference\_api.h:536

[REG\_TRACKER1](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a49d311578982dec5afa589b0963d0622)

@ REG\_TRACKER1

**Definition** ft8xx\_reference\_api.h:612

[REG\_HOFFSET](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a50a3fe216944877cf4a55df00de4bd85)

@ REG\_HOFFSET

**Definition** ft8xx\_reference\_api.h:539

[REG\_DITHER](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a50c524cae48fcba2477cae9c422a3f5b)

@ REG\_DITHER

**Definition** ft8xx\_reference\_api.h:551

[REG\_MEDIAFIFO\_READ](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a529da48e0b241ae16e8cbf1d38653c97)

@ REG\_MEDIAFIFO\_READ

**Definition** ft8xx\_reference\_api.h:616

[REG\_GPIOX\_DIR](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a538bc67838a34c6f1dfbb8bdff984788)

@ REG\_GPIOX\_DIR

**Definition** ft8xx\_reference\_api.h:565

[REG\_OUTBITS](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a55841781abfc8d3452399c79d69a2009)

@ REG\_OUTBITS

**Definition** ft8xx\_reference\_api.h:550

[REG\_TOUCH\_RZTHRESH](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a56440ea6e79d6cb2c6374d8fab01277e)

@ REG\_TOUCH\_RZTHRESH

**Definition** ft8xx\_reference\_api.h:589

[REG\_CPURESET](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a569c58d9a986415596b91856b02175b2)

@ REG\_CPURESET

**Definition** ft8xx\_reference\_api.h:535

[REG\_PCLK](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a572feb4e0547d7b40c18c8ff7ed62b55)

@ REG\_PCLK

**Definition** ft8xx\_reference\_api.h:555

[REG\_PLAYBACK\_PLAY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a59764d36f28fcf060f164e8fdfb3aba8)

@ REG\_PLAYBACK\_PLAY

**Definition** ft8xx\_reference\_api.h:577

[REG\_PLAYBACK\_LOOP](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a5b712095cc16ff8866d55b95f6e081e5)

@ REG\_PLAYBACK\_LOOP

**Definition** ft8xx\_reference\_api.h:576

[REG\_ID](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a6797b58f7ec24dbf469df8a17680fb7a)

@ REG\_ID

**Definition** ft8xx\_reference\_api.h:528

[REG\_TRIM](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a683a15e3c7578fe44f7cee9ca5796f74)

@ REG\_TRIM

**Definition** ft8xx\_reference\_api.h:526

[REG\_PLAYBACK\_FORMAT](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a68e60e0c855fff63e3a6f767f1b0179c)

@ REG\_PLAYBACK\_FORMAT

**Definition** ft8xx\_reference\_api.h:575

[REG\_TOUCH\_TAG\_XY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a7546d5a7b068c0b23280a189c6345789)

@ REG\_TOUCH\_TAG\_XY

**Definition** ft8xx\_reference\_api.h:593

[REG\_TOUCH\_RAW\_XY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a781bc22bc6c5671201a1740a282e1e0d)

@ REG\_TOUCH\_RAW\_XY

**Definition** ft8xx\_reference\_api.h:590

[REG\_TOUCH\_OVERSAMPLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a78cb160ba1d417523093ce222504df96)

@ REG\_TOUCH\_OVERSAMPLE

**Definition** ft8xx\_reference\_api.h:588

[REG\_GPIO\_DIR](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a7f82f6066010b61ed49a7a8bd2b9b52e)

@ REG\_GPIO\_DIR

**Definition** ft8xx\_reference\_api.h:563

[REG\_SNAPSHOT](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a81ad0d146fb392f9561bce00c6ed4e6b)

@ REG\_SNAPSHOT

**Definition** ft8xx\_reference\_api.h:534

[REG\_PLAYBACK\_FREQ](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a84a2b99d9ea7f674f019f1d54c1cddc3)

@ REG\_PLAYBACK\_FREQ

**Definition** ft8xx\_reference\_api.h:574

[REG\_TOUCH\_SCREEN\_XY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a857a79d4d62ee1369f10fb746e0d0aa8)

@ REG\_TOUCH\_SCREEN\_XY

**Definition** ft8xx\_reference\_api.h:592

[REG\_TOUCH\_TAG](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a86b3ad977f18ed6948a195f0d0f998af)

@ REG\_TOUCH\_TAG

**Definition** ft8xx\_reference\_api.h:594

[REG\_TOUCH\_TRANSFORM\_C](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a8717b3386b1e0ad11e34f7fae83ae793)

@ REG\_TOUCH\_TRANSFORM\_C

**Definition** ft8xx\_reference\_api.h:597

[REG\_TAP\_MASK](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a87efcd914405639dcf24d762becd1ebd)

@ REG\_TAP\_MASK

**Definition** ft8xx\_reference\_api.h:537

[REG\_PWM\_HZ](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a884022eead52d6738a4f20f6a543dc50)

@ REG\_PWM\_HZ

**Definition** ft8xx\_reference\_api.h:578

[REG\_TOUCH\_CONFIG](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a8feeb5e4fbc73322825fdd392dbec950)

@ REG\_TOUCH\_CONFIG

**Definition** ft8xx\_reference\_api.h:601

[REG\_PLAYBACK\_START](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a95f7b2f9eb12abcdf6885ee984155d8e)

@ REG\_PLAYBACK\_START

**Definition** ft8xx\_reference\_api.h:571

[REG\_INT\_EN](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a966071326a92ac6e595b2acbb2445697)

@ REG\_INT\_EN

**Definition** ft8xx\_reference\_api.h:569

[REG\_TOUCH\_TRANSFORM\_D](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a9988ada9b469290b9c886ba665fb4b48)

@ REG\_TOUCH\_TRANSFORM\_D

**Definition** ft8xx\_reference\_api.h:598

[REG\_DLSWAP](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a9a09798569680c1a48880ec40502e019)

@ REG\_DLSWAP

**Definition** ft8xx\_reference\_api.h:548

[REG\_SNAPY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a9cef87cf60803317580a4bd04762bc9f)

@ REG\_SNAPY

**Definition** ft8xx\_reference\_api.h:533

[REG\_VOL\_PB](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aa024b09fec9d0440483a33e972550888)

@ REG\_VOL\_PB

**Definition** ft8xx\_reference\_api.h:559

[REG\_SPI\_WIDTH](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aa382cb5b65f2803e94ce4451ed75b848)

@ REG\_SPI\_WIDTH

**Definition** ft8xx\_reference\_api.h:603

[REG\_VSIZE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aa63605dbe4cf7fdb4e1d7994f22aa878)

@ REG\_VSIZE

**Definition** ft8xx\_reference\_api.h:545

[REG\_PLAYBACK\_LENGTH](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aa9f1905d1f2488f5c9600dc4b27753c2)

@ REG\_PLAYBACK\_LENGTH

**Definition** ft8xx\_reference\_api.h:572

[REG\_VOL\_SOUND](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aac293daf5a8d5221d5c4167177069970)

@ REG\_VOL\_SOUND

**Definition** ft8xx\_reference\_api.h:560

[REG\_INT\_FLAGS](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ab6fd90f08477954798d5a54cb1ddce8f)

@ REG\_INT\_FLAGS

**Definition** ft8xx\_reference\_api.h:568

[REG\_INT\_MASK](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aba6637892ddbceafb4e558fbcffe496d)

@ REG\_INT\_MASK

**Definition** ft8xx\_reference\_api.h:570

[REG\_CMD\_DL](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac1e6dcc3e508a9f5b8f061a06cda7c87)

@ REG\_CMD\_DL

**Definition** ft8xx\_reference\_api.h:583

[REG\_TRACKER4](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac3f442ac6c0010066270e8373efeefcf)

@ REG\_TRACKER4

**Definition** ft8xx\_reference\_api.h:615

[REG\_TAG\_Y](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac41d85f3ba86087e0e0c5c071388d254)

@ REG\_TAG\_Y

**Definition** ft8xx\_reference\_api.h:557

[REG\_FREQUENCY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac447562a0543880a863929676c9a2c21)

@ REG\_FREQUENCY

**Definition** ft8xx\_reference\_api.h:531

[REG\_TRACKER3](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac4852d6d1ee6c7b69a3f4386354d5f2c)

@ REG\_TRACKER3

**Definition** ft8xx\_reference\_api.h:614

[REG\_ROTATE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac785fd2e2498944eec5f404229c1a6f3)

@ REG\_ROTATE

**Definition** ft8xx\_reference\_api.h:549

[REG\_TAG](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac8690647b7274feef7b7a0695eaf9a6b)

@ REG\_TAG

**Definition** ft8xx\_reference\_api.h:558

[REG\_TOUCH\_TRANSFORM\_B](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac93146dd21c9a7e07353ae901ccea745)

@ REG\_TOUCH\_TRANSFORM\_B

**Definition** ft8xx\_reference\_api.h:596

[REG\_HSYNC0](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008accb71ca34304a4276f6b8c5d2b2e4e6a)

@ REG\_HSYNC0

**Definition** ft8xx\_reference\_api.h:541

[REG\_VOFFSET](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad1b8daf2ec9fe116c79d59b2d524a8a2)

@ REG\_VOFFSET

**Definition** ft8xx\_reference\_api.h:544

[REG\_VCYCLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad360af56001df6e29616a11f087db26a)

@ REG\_VCYCLE

**Definition** ft8xx\_reference\_api.h:543

[REG\_TOUCH\_RZ](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad63d6b6752e9a3b25c2d4eec38d9e455)

@ REG\_TOUCH\_RZ

**Definition** ft8xx\_reference\_api.h:591

[REG\_FRAMES](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad73c12cf386d92029bef895c52a21272)

@ REG\_FRAMES

**Definition** ft8xx\_reference\_api.h:529

[REG\_CMD\_WRITE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad878f3fc41274192245aa6c27209ea69)

@ REG\_CMD\_WRITE

**Definition** ft8xx\_reference\_api.h:582

[REG\_GPIO](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad92810bdf452c531a7dda338aff3aad1)

@ REG\_GPIO

**Definition** ft8xx\_reference\_api.h:564

[REG\_TRACKER](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad99a270479fd9ce96e1868fb708bacbb)

@ REG\_TRACKER

**Definition** ft8xx\_reference\_api.h:611

[REG\_SOUND](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008adb67bd48114184e8ad04cadba731e9fe)

@ REG\_SOUND

**Definition** ft8xx\_reference\_api.h:561

[REG\_GPIOX](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008adc4499b79053ad08a2279b3702b79ced)

@ REG\_GPIOX

**Definition** ft8xx\_reference\_api.h:566

[REG\_VSYNC0](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ae07735ed3259a2112898ee9330cc2050)

@ REG\_VSYNC0

**Definition** ft8xx\_reference\_api.h:546

[REG\_TOUCH\_MODE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ae53c8a1517586c00ce5e0d19b2bbea29)

@ REG\_TOUCH\_MODE

**Definition** ft8xx\_reference\_api.h:584

[REG\_CMDB\_WRITE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ae86016e9d0fb6db20d2c585300759464)

@ REG\_CMDB\_WRITE

**Definition** ft8xx\_reference\_api.h:609

[REG\_TOUCH\_DIRECT\_XY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ae8dddb1bf87f77e70a03c4ad73ba51fd)

@ REG\_TOUCH\_DIRECT\_XY

**Definition** ft8xx\_reference\_api.h:605

[REG\_RENDERMODE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aebeab047c1430f0165e36f83e0ff38a9)

@ REG\_RENDERMODE

**Definition** ft8xx\_reference\_api.h:532

[REG\_HCYCLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aec806fab0ed79a1a51e39395147feff2)

@ REG\_HCYCLE

**Definition** ft8xx\_reference\_api.h:538

[REG\_PLAYBACK\_READPTR](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aed471a111f18c5a92bcc5d7ca07e4b6d)

@ REG\_PLAYBACK\_READPTR

**Definition** ft8xx\_reference\_api.h:573

[REG\_TOUCH\_CHARGE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af0baf00d792cf20622f3716ee6c7fa95)

@ REG\_TOUCH\_CHARGE

**Definition** ft8xx\_reference\_api.h:586

[REG\_SWIZZLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af1c9622660d41f1ebaf3c5151a8526f6)

@ REG\_SWIZZLE

**Definition** ft8xx\_reference\_api.h:552

[REG\_CMD\_READ](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af5512106f5e7d41845b1cc01ca52bf68)

@ REG\_CMD\_READ

**Definition** ft8xx\_reference\_api.h:581

[REG\_CSPREAD](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af57b15505b903b9e8d940e1156bfa83d)

@ REG\_CSPREAD

**Definition** ft8xx\_reference\_api.h:553

[REG\_](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276ca0e42504c57b04103704eb19348fea779)

@ REG\_

**Definition** ft8xx\_reference\_api.h:436

[RAM\_G](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276ca8f7e484f38038b0a390e7cad119f2cb4)

@ RAM\_G

**Definition** ft8xx\_reference\_api.h:434

[RAM\_DL](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276caf2eb368364f52dcfc067e40c2a252a84)

@ RAM\_DL

**Definition** ft8xx\_reference\_api.h:435

[RAM\_CMD](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276caff47e90e4e3dd7901dfd1cde3fb132f5)

@ RAM\_CMD

**Definition** ft8xx\_reference\_api.h:437

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf)

\_\_INT16\_TYPE\_\_ int16\_t

**Definition** stdint.h:73

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [ft8xx](dir_2b36ac0e023aa45869ab11e4334d802b.md)
- [ft8xx\_reference\_api.h](ft8xx__reference__api_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
