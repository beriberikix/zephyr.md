---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/ft8xx__reference__api_8h.html
original_path: doxygen/html/ft8xx__reference__api_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ft8xx\_reference\_api.h File Reference

FT8XX reference API.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/drivers/misc/ft8xx/ft8xx_copro.h](ft8xx__copro_8h_source.md)>`  
`#include <[zephyr/drivers/misc/ft8xx/ft8xx_common.h](ft8xx__common_8h_source.md)>`  
`#include <[zephyr/drivers/misc/ft8xx/ft8xx_dl.h](ft8xx__dl_8h_source.md)>`  
`#include <[zephyr/drivers/misc/ft8xx/ft8xx_memory.h](ft8xx__memory_8h_source.md)>`

[Go to the source code of this file.](ft8xx__reference__api_8h_source.md)

| Macros | |
| --- | --- |
| #define | [OPT\_3D](group__ft8xx__reference__api.md#gabf03e1cd7cb18b7c1daf243d4c1dde24)   [FT8XX\_OPT\_3D](group__ft8xx__copro.md#ga304badab7bd34208d499b199080fb557) |
|  | Co-processor widget is drawn in 3D effect. |
| #define | [OPT\_RGB565](group__ft8xx__reference__api.md#ga53f763f1e5de09b5e51242df87af8fb8)   [FT8XX\_OPT\_RGB565](group__ft8xx__copro.md#ga3a79c1128bdb9fe094843688691a085c) |
|  | Co-processor option to decode the JPEG image to RGB565 format. |
| #define | [OPT\_MONO](group__ft8xx__reference__api.md#ga2fab787f842bb9193c9df68cb44f93fd)   [FT8XX\_OPT\_MONO](group__ft8xx__copro.md#ga415760ddf94db71ee9a504300bac4661) |
|  | Co-processor option to decode the JPEG image to L8 format, i.e., monochrome. |
| #define | [OPT\_NODL](group__ft8xx__reference__api.md#ga37f793d8ac3af5f518d024727ce9f710)   [FT8XX\_OPT\_NODL](group__ft8xx__copro.md#gacc953470460b083c0b8bd9ebbc8ed03b) |
|  | No display list commands generated for bitmap decoded from JPEG image. |
| #define | [OPT\_FLAT](group__ft8xx__reference__api.md#gaa76b9296cd6f2eb4bec3d650b73e69cc)   [FT8XX\_OPT\_FLAT](group__ft8xx__copro.md#ga160b331fb401eec023e0992c6f4c6331) |
|  | Co-processor widget is drawn without 3D effect. |
| #define | [OPT\_SIGNED](group__ft8xx__reference__api.md#gae0fef45ae7ca3a45286a19a47bd46943)   [FT8XX\_OPT\_SIGNED](group__ft8xx__copro.md#ga5a58155896cdb2d0f1693d203706ce93) |
|  | The number is treated as 32 bit signed integer. |
| #define | [OPT\_CENTERX](group__ft8xx__reference__api.md#ga65bf92a2956ffee68057ab90be032445)   [FT8XX\_OPT\_CENTERX](group__ft8xx__copro.md#gac2d1ccbb99eaa032ed9d39fc01d32c66) |
|  | Co-processor widget centers horizontally. |
| #define | [OPT\_CENTERY](group__ft8xx__reference__api.md#gaa28880f2aa7b6d8a51518189ca08382f)   [FT8XX\_OPT\_CENTERY](group__ft8xx__copro.md#ga65b3a1e29ae425b2f1c3e66b4ea1449a) |
|  | Co-processor widget centers vertically. |
| #define | [OPT\_CENTER](group__ft8xx__reference__api.md#ga830647bc1b42665e27813a46a6a089b7)   [FT8XX\_OPT\_CENTER](group__ft8xx__copro.md#ga013968a6bf9534265c897ab1f4018eb0) |
|  | Co-processor widget centers horizontally and vertically. |
| #define | [OPT\_RIGHTX](group__ft8xx__reference__api.md#gae0088375e797e08fa3e14dc3124c1e90)   [FT8XX\_OPT\_RIGHTX](group__ft8xx__copro.md#gac864c155bc2121bf8d3954e1ed8dbb7e) |
|  | The label on the Coprocessor widget is right justified. |
| #define | [OPT\_NOBACK](group__ft8xx__reference__api.md#ga87b8705ac37fc69704f00cc2a9b8e69e)   [FT8XX\_OPT\_NOBACK](group__ft8xx__copro.md#gacb08df4fac256cbf808b133d4159aa29) |
|  | Co-processor widget has no background drawn. |
| #define | [OPT\_NOTICKS](group__ft8xx__reference__api.md#gaed772e3cf2529e698fa8e69ee73f91f9)   [FT8XX\_OPT\_NOTICKS](group__ft8xx__copro.md#ga50f4fac88e4f4b558450adcda33dae93) |
|  | Co-processor clock widget is drawn without hour ticks. |
| #define | [OPT\_NOHM](group__ft8xx__reference__api.md#ga1e7090a0dbcee600a5472f5fc4343824)   [FT8XX\_OPT\_NOHM](group__ft8xx__copro.md#ga79938d9c1193d44a527ca8c158117a86) |
|  | Co-processor clock widget is drawn without hour and minutes hands, only seconds hand is drawn. |
| #define | [OPT\_NOPOINTER](group__ft8xx__reference__api.md#ga0eb8abce5677ca0e6948ec1a003958de)   [FT8XX\_OPT\_NOPOINTER](group__ft8xx__copro.md#ga1a9838a862ec166bfe95d64144b9a052) |
|  | The Co-processor gauge has no pointer. |
| #define | [OPT\_NOSECS](group__ft8xx__reference__api.md#ga190c29e3a00685c3f8c4906df37720ae)   [FT8XX\_OPT\_NOSECS](group__ft8xx__copro.md#ga6416f4282d2c483d2adba8c1215ab638) |
|  | Co-processor clock widget is drawn without seconds hand. |
| #define | [OPT\_NOHANDS](group__ft8xx__reference__api.md#gaa9bc6e351e9fb0515c69f3cd32ad5621)   [FT8XX\_OPT\_NOHANDS](group__ft8xx__copro.md#gade56de46694ca420460c1ceb26a33120) |
|  | Co-processor clock widget is drawn without hour, minutes and seconds hands. |
| #define | [BITMAPS](group__ft8xx__reference__api.md#ga3746a5c44f711b633ca618b6ebb8e75f)   [FT8XX\_BITMAPS](group__ft8xx__dl.md#ga28f7596c367f67f73d701b792300aa09) |
|  | Rectangular pixel arrays, in various color formats. |
| #define | [POINTS](group__ft8xx__reference__api.md#gae6910994a90091fe877b021c590c894e)   [FT8XX\_POINTS](group__ft8xx__dl.md#ga1d6f49b3817f9927fa1cd3cd42820490) |
|  | Anti-aliased points, point radius is 1-256 pixels. |
| #define | [LINES](group__ft8xx__reference__api.md#ga321ae946de24c36489276616d13c46cd)   [FT8XX\_LINES](group__ft8xx__dl.md#ga62bcf30c7a9eae4c468e1c7de144ad01) |
|  | Anti-aliased lines, with width from 0 to 4095 1/16th of pixel units. |
| #define | [LINE\_STRIP](group__ft8xx__reference__api.md#gac300cac409c1526ba5622f15472a25df)   [FT8XX\_LINE\_STRIP](group__ft8xx__dl.md#gac1b1188c36a4078e7db50d3c5aee7d25) |
|  | Anti-aliased lines, connected head-to-tail. |
| #define | [EDGE\_STRIP\_R](group__ft8xx__reference__api.md#ga8c7fa2526afa79673d93b64f864d2126)   [FT8XX\_EDGE\_STRIP\_R](group__ft8xx__dl.md#ga0b3ce2828323978e9648bfd07caa1065) |
|  | Edge strips for right. |
| #define | [EDGE\_STRIP\_L](group__ft8xx__reference__api.md#ga3434ce2412337ac0b7d9558ff25181d0)   [FT8XX\_EDGE\_STRIP\_L](group__ft8xx__dl.md#ga97229abf592bba4039f19a98451cdc5b) |
|  | Edge strips for left. |
| #define | [EDGE\_STRIP\_A](group__ft8xx__reference__api.md#gaa69720d489114390d9493d397cd392b7)   [FT8XX\_EDGE\_STRIP\_A](group__ft8xx__dl.md#gaf5ad60bbe137dbf64281ad8d0be051e0) |
|  | Edge strips for above. |
| #define | [EDGE\_STRIP\_B](group__ft8xx__reference__api.md#ga20ed5346e45eb4ce0e79f094c7346627)   [FT8XX\_EDGE\_STRIP\_B](group__ft8xx__dl.md#ga9aff3a3c58e12b990130271e845662a8) |
|  | Edge strips for below. |
| #define | [RECTS](group__ft8xx__reference__api.md#ga5868720577871792983ae813837c6189)   [FT8XX\_RECTS](group__ft8xx__dl.md#ga05077568fea624ed7e3f9e3f6e8d72b8) |
|  | Round-cornered rectangles, curvature of the corners can be adjusted using LINE\_WIDTH. |
| #define | [BEGIN](group__ft8xx__reference__api.md#ga34b42db00c62ff404a8bd7119fc62327)(prim) |
|  | Begin drawing a graphics primitive. |
| #define | [CLEAR](group__ft8xx__reference__api.md#ga218ebaaf7d9afe6257021f3c08e59959)(c, [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), t) |
|  | Clear buffers to preset values. |
| #define | [CLEAR\_COLOR\_RGB](group__ft8xx__reference__api.md#gae6375b17ea6f06bf81357fe9350e1c1c)(red, green, blue) |
|  | Specify clear values for red, green and blue channels. |
| #define | [COLOR\_RGB](group__ft8xx__reference__api.md#ga59c390601a75b4d869e7cfc58d2430bf)(red, green, blue) |
|  | Set the current color red, green and blue. |
| #define | [DISPLAY](group__ft8xx__reference__api.md#ga486931aa64c90970e7a4110ada3d0916)() |
|  | End the display list. |
| #define | [END](group__ft8xx__reference__api.md#ga569b6a4f889b0846cc0a3396f3835a17)() |
|  | End drawing a graphics primitive. |
| #define | [LINE\_WIDTH](group__ft8xx__reference__api.md#ga8764958e4fa66c3948353226f82cedaf)(width) |
|  | Specify the width of lines to be drawn with primitive [LINES](group__ft8xx__reference__api.md#ga321ae946de24c36489276616d13c46cd "LINES"). |
| #define | [TAG](group__ft8xx__reference__api.md#ga5f17de6768f32dd36135de83c24d0a7b)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
|  | Attach the tag value for the following graphics objects. |
| #define | [VERTEX2F](group__ft8xx__reference__api.md#ga033cea1b18c3f010aaa0293f6972069a)(x, y) |
|  | Start the operation of graphics primitives at the specified coordinate. |
| #define | [VERTEX2II](group__ft8xx__reference__api.md#gae779df636416e900ddc15b95cf2a923c)(x, y, handle, cell) |
|  | Start the operation of graphics primitive at the specified coordinates. |

| Enumerations | |
| --- | --- |
| enum | [ft8xx\_memory\_map\_t](group__ft8xx__reference__api.md#gabbba9344e2d9b81af6313c6b7f12276c) { [RAM\_G](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276ca8f7e484f38038b0a390e7cad119f2cb4) = FT810\_RAM\_G , [RAM\_DL](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276caf2eb368364f52dcfc067e40c2a252a84) = FT810\_RAM\_DL , [REG\_](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276ca0e42504c57b04103704eb19348fea779) = FT810\_REG\_ , [RAM\_CMD](group__ft8xx__reference__api.md#ggabbba9344e2d9b81af6313c6b7f12276caff47e90e4e3dd7901dfd1cde3fb132f5) = FT810\_RAM\_CMD } |
|  | Main parts of FT810 memory map. [More...](group__ft8xx__reference__api.md#gabbba9344e2d9b81af6313c6b7f12276c) |
| enum | [ft8xx\_register\_address\_t](group__ft8xx__reference__api.md#gaa3f6afa02b5f4bed90093f659201d008) {     [REG\_TRIM](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a683a15e3c7578fe44f7cee9ca5796f74) = FT810\_REG\_TRIM , [REG\_ID](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a6797b58f7ec24dbf469df8a17680fb7a) = FT810\_REG\_ID , [REG\_FRAMES](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad73c12cf386d92029bef895c52a21272) = FT810\_REG\_FRAMES , [REG\_CLOCK](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a2dd65dd2f5e8f97f27135c343681af64) = FT810\_REG\_CLOCK ,     [REG\_FREQUENCY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac447562a0543880a863929676c9a2c21) = FT810\_REG\_FREQUENCY , [REG\_RENDERMODE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aebeab047c1430f0165e36f83e0ff38a9) = FT810\_REG\_RENDERMODE , [REG\_SNAPY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a9cef87cf60803317580a4bd04762bc9f) = FT810\_REG\_SNAPY , [REG\_SNAPSHOT](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a81ad0d146fb392f9561bce00c6ed4e6b) = FT810\_REG\_SNAPSHOT ,     [REG\_CPURESET](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a569c58d9a986415596b91856b02175b2) = FT810\_REG\_CPURESET , [REG\_TAP\_CRC](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a47894772f07899e20c560b47a4b37208) = FT810\_REG\_TAP\_CRC , [REG\_TAP\_MASK](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a87efcd914405639dcf24d762becd1ebd) = FT810\_REG\_TAP\_MASK , [REG\_HCYCLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aec806fab0ed79a1a51e39395147feff2) = FT810\_REG\_HCYCLE ,     [REG\_HOFFSET](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a50a3fe216944877cf4a55df00de4bd85) = FT810\_REG\_HOFFSET , [REG\_HSIZE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a3dd43d215eb4b5047b8a14406f85c8e0) = FT810\_REG\_HSIZE , [REG\_HSYNC0](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008accb71ca34304a4276f6b8c5d2b2e4e6a) = FT810\_REG\_HSYNC0 , [REG\_HSYNC1](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a13b32d8ce6608067d1f816065547b559) = FT810\_REG\_HSYNC1 ,     [REG\_VCYCLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad360af56001df6e29616a11f087db26a) = FT810\_REG\_VCYCLE , [REG\_VOFFSET](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad1b8daf2ec9fe116c79d59b2d524a8a2) = FT810\_REG\_VOFFSET , [REG\_VSIZE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aa63605dbe4cf7fdb4e1d7994f22aa878) = FT810\_REG\_VSIZE , [REG\_VSYNC0](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ae07735ed3259a2112898ee9330cc2050) = FT810\_REG\_VSYNC0 ,     [REG\_VSYNC1](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a3193050a59229830b80c5f637a09ecbb) = FT810\_REG\_VSYNC1 , [REG\_DLSWAP](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a9a09798569680c1a48880ec40502e019) = FT810\_REG\_DLSWAP , [REG\_ROTATE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac785fd2e2498944eec5f404229c1a6f3) = FT810\_REG\_ROTATE , [REG\_OUTBITS](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a55841781abfc8d3452399c79d69a2009) = FT810\_REG\_OUTBITS ,     [REG\_DITHER](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a50c524cae48fcba2477cae9c422a3f5b) = FT810\_REG\_DITHER , [REG\_SWIZZLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af1c9622660d41f1ebaf3c5151a8526f6) = FT810\_REG\_SWIZZLE , [REG\_CSPREAD](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af57b15505b903b9e8d940e1156bfa83d) = FT810\_REG\_CSPREAD , [REG\_PCLK\_POL](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a1fbe40f257634301cca0229d68851c6b) = FT810\_REG\_PCLK\_POL ,     [REG\_PCLK](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a572feb4e0547d7b40c18c8ff7ed62b55) = FT810\_REG\_PCLK , [REG\_TAG\_X](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a1ecdf33453fe848f48f0535ca23b5541) = FT810\_REG\_TAG\_X , [REG\_TAG\_Y](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac41d85f3ba86087e0e0c5c071388d254) = FT810\_REG\_TAG\_Y , [REG\_TAG](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac8690647b7274feef7b7a0695eaf9a6b) = FT810\_REG\_TAG ,     [REG\_VOL\_PB](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aa024b09fec9d0440483a33e972550888) = FT810\_REG\_VOL\_PB , [REG\_VOL\_SOUND](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aac293daf5a8d5221d5c4167177069970) = FT810\_REG\_VOL\_SOUND , [REG\_SOUND](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008adb67bd48114184e8ad04cadba731e9fe) = FT810\_REG\_SOUND , [REG\_PLAY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a29570336f1d3a7b15d2f5b76a816faa3) = FT810\_REG\_PLAY ,     [REG\_GPIO\_DIR](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a7f82f6066010b61ed49a7a8bd2b9b52e) = FT810\_REG\_GPIO\_DIR , [REG\_GPIO](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad92810bdf452c531a7dda338aff3aad1) = FT810\_REG\_GPIO , [REG\_GPIOX\_DIR](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a538bc67838a34c6f1dfbb8bdff984788) = FT810\_REG\_GPIOX\_DIR , [REG\_GPIOX](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008adc4499b79053ad08a2279b3702b79ced) = FT810\_REG\_GPIOX ,     [REG\_INT\_FLAGS](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ab6fd90f08477954798d5a54cb1ddce8f) = FT810\_REG\_INT\_FLAGS , [REG\_INT\_EN](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a966071326a92ac6e595b2acbb2445697) = FT810\_REG\_INT\_EN , [REG\_INT\_MASK](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aba6637892ddbceafb4e558fbcffe496d) = FT810\_REG\_INT\_MASK , [REG\_PLAYBACK\_START](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a95f7b2f9eb12abcdf6885ee984155d8e) = FT810\_REG\_PLAYBACK\_START ,     [REG\_PLAYBACK\_LENGTH](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aa9f1905d1f2488f5c9600dc4b27753c2) = FT810\_REG\_PLAYBACK\_LENGTH , [REG\_PLAYBACK\_READPTR](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aed471a111f18c5a92bcc5d7ca07e4b6d) = FT810\_REG\_PLAYBACK\_READPTR , [REG\_PLAYBACK\_FREQ](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a84a2b99d9ea7f674f019f1d54c1cddc3) = FT810\_REG\_PLAYBACK\_FREQ , [REG\_PLAYBACK\_FORMAT](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a68e60e0c855fff63e3a6f767f1b0179c) = FT810\_REG\_PLAYBACK\_FORMAT ,     [REG\_PLAYBACK\_LOOP](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a5b712095cc16ff8866d55b95f6e081e5) = FT810\_REG\_PLAYBACK\_LOOP , [REG\_PLAYBACK\_PLAY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a59764d36f28fcf060f164e8fdfb3aba8) = FT810\_REG\_PLAYBACK\_PLAY , [REG\_PWM\_HZ](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a884022eead52d6738a4f20f6a543dc50) = FT810\_REG\_PWM\_HZ , [REG\_PWM\_DUTY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a04f552a92ffd030a0cbc07d522197265) = FT810\_REG\_PWM\_DUTY ,     [REG\_CMD\_READ](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af5512106f5e7d41845b1cc01ca52bf68) = FT810\_REG\_CMD\_READ , [REG\_CMD\_WRITE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad878f3fc41274192245aa6c27209ea69) = FT810\_REG\_CMD\_WRITE , [REG\_CMD\_DL](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac1e6dcc3e508a9f5b8f061a06cda7c87) = FT810\_REG\_CMD\_DL , [REG\_TOUCH\_MODE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ae53c8a1517586c00ce5e0d19b2bbea29) = FT810\_REG\_TOUCH\_MODE ,     [REG\_TOUCH\_ADC\_MODE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a2f0c46b14b1dced78eceb5f21c6a898e) = FT810\_REG\_TOUCH\_ADC\_MODE , [REG\_TOUCH\_CHARGE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008af0baf00d792cf20622f3716ee6c7fa95) = FT810\_REG\_TOUCH\_CHARGE , [REG\_TOUCH\_SETTLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a21bec38288166e781f4e42f9e2cd88fb) = FT810\_REG\_TOUCH\_SETTLE , [REG\_TOUCH\_OVERSAMPLE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a78cb160ba1d417523093ce222504df96) = FT810\_REG\_TOUCH\_OVERSAMPLE ,     [REG\_TOUCH\_RZTHRESH](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a56440ea6e79d6cb2c6374d8fab01277e) = FT810\_REG\_TOUCH\_RZTHRESH , [REG\_TOUCH\_RAW\_XY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a781bc22bc6c5671201a1740a282e1e0d) = FT810\_REG\_TOUCH\_RAW\_XY , [REG\_TOUCH\_RZ](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad63d6b6752e9a3b25c2d4eec38d9e455) = FT810\_REG\_TOUCH\_RZ , [REG\_TOUCH\_SCREEN\_XY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a857a79d4d62ee1369f10fb746e0d0aa8) = FT810\_REG\_TOUCH\_SCREEN\_XY ,     [REG\_TOUCH\_TAG\_XY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a7546d5a7b068c0b23280a189c6345789) = FT810\_REG\_TOUCH\_TAG\_XY , [REG\_TOUCH\_TAG](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a86b3ad977f18ed6948a195f0d0f998af) = FT810\_REG\_TOUCH\_TAG , [REG\_TOUCH\_TRANSFORM\_A](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a2725ae9bcc184f701002e0824b6cfdfd) = FT810\_REG\_TOUCH\_TRANSFORM\_A , [REG\_TOUCH\_TRANSFORM\_B](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac93146dd21c9a7e07353ae901ccea745) = FT810\_REG\_TOUCH\_TRANSFORM\_B ,     [REG\_TOUCH\_TRANSFORM\_C](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a8717b3386b1e0ad11e34f7fae83ae793) = FT810\_REG\_TOUCH\_TRANSFORM\_C , [REG\_TOUCH\_TRANSFORM\_D](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a9988ada9b469290b9c886ba665fb4b48) = FT810\_REG\_TOUCH\_TRANSFORM\_D , [REG\_TOUCH\_TRANSFORM\_E](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a36c4f53d2e132c794695983e56cf627c) = FT810\_REG\_TOUCH\_TRANSFORM\_E , [REG\_TOUCH\_TRANSFORM\_F](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a041ffbb78a6572c5c1e515843f959315) = FT810\_REG\_TOUCH\_TRANSFORM\_F ,     [REG\_TOUCH\_CONFIG](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a8feeb5e4fbc73322825fdd392dbec950) = FT810\_REG\_TOUCH\_CONFIG , [REG\_SPI\_WIDTH](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008aa382cb5b65f2803e94ce4451ed75b848) = FT810\_REG\_SPI\_WIDTH , [REG\_TOUCH\_DIRECT\_XY](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ae8dddb1bf87f77e70a03c4ad73ba51fd) = FT810\_REG\_TOUCH\_DIRECT\_XY , [REG\_TOUCH\_DIRECT\_Z1Z2](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a43e6c3532c2f9573e31ddd4ce12fb8c0) = FT810\_REG\_TOUCH\_DIRECT\_Z1Z2 ,     [REG\_CMDB\_SPACE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a327a78d411cf247a6ee6e4ea5541c90c) = FT810\_REG\_CMDB\_SPACE , [REG\_CMDB\_WRITE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ae86016e9d0fb6db20d2c585300759464) = FT810\_REG\_CMDB\_WRITE , [REG\_TRACKER](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ad99a270479fd9ce96e1868fb708bacbb) = FT810\_REG\_TRACKER , [REG\_TRACKER1](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a49d311578982dec5afa589b0963d0622) = FT810\_REG\_TRACKER1 ,     [REG\_TRACKER2](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a3bbab48e1bdad06303e631f62d7bcd76) = FT810\_REG\_TRACKER2 , [REG\_TRACKER3](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac4852d6d1ee6c7b69a3f4386354d5f2c) = FT810\_REG\_TRACKER3 , [REG\_TRACKER4](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008ac3f442ac6c0010066270e8373efeefcf) = FT810\_REG\_TRACKER4 , [REG\_MEDIAFIFO\_READ](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a529da48e0b241ae16e8cbf1d38653c97) = FT810\_REG\_MEDIAFIFO\_READ ,     [REG\_MEDIAFIFO\_WRITE](group__ft8xx__reference__api.md#ggaa3f6afa02b5f4bed90093f659201d008a11a7b5722d9de6c62222a5c76f0b692b) = FT810\_REG\_MEDIAFIFO\_WRITE   } |
|  | FT810 register addresses. [More...](group__ft8xx__reference__api.md#gaa3f6afa02b5f4bed90093f659201d008) |

| Functions | |
| --- | --- |
| static void | [wr8](group__ft8xx__reference__api.md#ga1e9c6203ebb7cc15a736d074bd98c181) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data) |
|  | Write 1 byte (8 bits) to FT8xx memory. |
| static void | [wr16](group__ft8xx__reference__api.md#ga8fac4ed55f7ef9d82d8dcb0eb6f09eab) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data) |
|  | Write 2 bytes (16 bits) to FT8xx memory. |
| static void | [wr32](group__ft8xx__reference__api.md#ga3f6814650684e2c2100d8f9a36505ca0) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
|  | Write 4 bytes (32 bits) to FT8xx memory. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rd8](group__ft8xx__reference__api.md#gae96efe5496139f508083a21b2299e3d8) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address) |
|  | Read 1 byte (8 bits) from FT8xx memory. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [rd16](group__ft8xx__reference__api.md#ga2f833e24c067f88801884c93766d7ac7) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address) |
|  | Read 2 bytes (16 bits) from FT8xx memory. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rd32](group__ft8xx__reference__api.md#ga0c6f11426fd5412a66e4f5de0a9f0847) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address) |
|  | Read 4 bytes (32 bits) from FT8xx memory. |
| static void | [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) command) |
|  | Execute a display list command by co-processor engine. |
| static void | [cmd\_dlstart](group__ft8xx__reference__api.md#ga7b9b6a41a878c449b107e51eba058799) (void) |
|  | Start a new display list. |
| static void | [cmd\_swap](group__ft8xx__reference__api.md#ga194d7e0d47b3d195155a22f86fbe7e7f) (void) |
|  | Swap the current display list. |
| static void | [cmd\_text](group__ft8xx__reference__api.md#gad642a54deaa36152ca4fea5e31294732) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) font, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) options, const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
|  | Draw text. |
| static void | [cmd\_number](group__ft8xx__reference__api.md#gabdaf9e6cd74c0d157d1673b99707e6f2) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) font, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) options, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) n) |
|  | Draw a decimal number. |
| static void | [cmd\_calibrate](group__ft8xx__reference__api.md#ga26015112ae4c62a944fe671ea2cb0bda) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result) |
|  | Execute the touch screen calibration routine. |

## Detailed Description

FT8XX reference API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [misc](dir_3d7f76f006150d60bf1fdbf1492e8004.md)
- [ft8xx](dir_2b36ac0e023aa45869ab11e4334d802b.md)
- [ft8xx\_reference\_api.h](ft8xx__reference__api_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
