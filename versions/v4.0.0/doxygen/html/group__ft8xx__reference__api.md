---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__ft8xx__reference__api.html
original_path: doxygen/html/group__ft8xx__reference__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

FT8xx reference API

[Device Driver APIs](group__io__interfaces.md) » [Miscellaneous Drivers APIs](group__misc__interfaces.md) » [FT8xx driver APIs](group__ft8xx__interface.md)

FT8xx reference API.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [OPT\_3D](#gabf03e1cd7cb18b7c1daf243d4c1dde24)   [FT8XX\_OPT\_3D](group__ft8xx__copro.md#ga304badab7bd34208d499b199080fb557) |
|  | Co-processor widget is drawn in 3D effect. |
| #define | [OPT\_RGB565](#ga53f763f1e5de09b5e51242df87af8fb8)   [FT8XX\_OPT\_RGB565](group__ft8xx__copro.md#ga3a79c1128bdb9fe094843688691a085c) |
|  | Co-processor option to decode the JPEG image to RGB565 format. |
| #define | [OPT\_MONO](#ga2fab787f842bb9193c9df68cb44f93fd)   [FT8XX\_OPT\_MONO](group__ft8xx__copro.md#ga415760ddf94db71ee9a504300bac4661) |
|  | Co-processor option to decode the JPEG image to L8 format, i.e., monochrome. |
| #define | [OPT\_NODL](#ga37f793d8ac3af5f518d024727ce9f710)   [FT8XX\_OPT\_NODL](group__ft8xx__copro.md#gacc953470460b083c0b8bd9ebbc8ed03b) |
|  | No display list commands generated for bitmap decoded from JPEG image. |
| #define | [OPT\_FLAT](#gaa76b9296cd6f2eb4bec3d650b73e69cc)   [FT8XX\_OPT\_FLAT](group__ft8xx__copro.md#ga160b331fb401eec023e0992c6f4c6331) |
|  | Co-processor widget is drawn without 3D effect. |
| #define | [OPT\_SIGNED](#gae0fef45ae7ca3a45286a19a47bd46943)   [FT8XX\_OPT\_SIGNED](group__ft8xx__copro.md#ga5a58155896cdb2d0f1693d203706ce93) |
|  | The number is treated as 32 bit signed integer. |
| #define | [OPT\_CENTERX](#ga65bf92a2956ffee68057ab90be032445)   [FT8XX\_OPT\_CENTERX](group__ft8xx__copro.md#gac2d1ccbb99eaa032ed9d39fc01d32c66) |
|  | Co-processor widget centers horizontally. |
| #define | [OPT\_CENTERY](#gaa28880f2aa7b6d8a51518189ca08382f)   [FT8XX\_OPT\_CENTERY](group__ft8xx__copro.md#ga65b3a1e29ae425b2f1c3e66b4ea1449a) |
|  | Co-processor widget centers vertically. |
| #define | [OPT\_CENTER](#ga830647bc1b42665e27813a46a6a089b7)   [FT8XX\_OPT\_CENTER](group__ft8xx__copro.md#ga013968a6bf9534265c897ab1f4018eb0) |
|  | Co-processor widget centers horizontally and vertically. |
| #define | [OPT\_RIGHTX](#gae0088375e797e08fa3e14dc3124c1e90)   [FT8XX\_OPT\_RIGHTX](group__ft8xx__copro.md#gac864c155bc2121bf8d3954e1ed8dbb7e) |
|  | The label on the Coprocessor widget is right justified. |
| #define | [OPT\_NOBACK](#ga87b8705ac37fc69704f00cc2a9b8e69e)   [FT8XX\_OPT\_NOBACK](group__ft8xx__copro.md#gacb08df4fac256cbf808b133d4159aa29) |
|  | Co-processor widget has no background drawn. |
| #define | [OPT\_NOTICKS](#gaed772e3cf2529e698fa8e69ee73f91f9)   [FT8XX\_OPT\_NOTICKS](group__ft8xx__copro.md#ga50f4fac88e4f4b558450adcda33dae93) |
|  | Co-processor clock widget is drawn without hour ticks. |
| #define | [OPT\_NOHM](#ga1e7090a0dbcee600a5472f5fc4343824)   [FT8XX\_OPT\_NOHM](group__ft8xx__copro.md#ga79938d9c1193d44a527ca8c158117a86) |
|  | Co-processor clock widget is drawn without hour and minutes hands, only seconds hand is drawn. |
| #define | [OPT\_NOPOINTER](#ga0eb8abce5677ca0e6948ec1a003958de)   [FT8XX\_OPT\_NOPOINTER](group__ft8xx__copro.md#ga1a9838a862ec166bfe95d64144b9a052) |
|  | The Co-processor gauge has no pointer. |
| #define | [OPT\_NOSECS](#ga190c29e3a00685c3f8c4906df37720ae)   [FT8XX\_OPT\_NOSECS](group__ft8xx__copro.md#ga6416f4282d2c483d2adba8c1215ab638) |
|  | Co-processor clock widget is drawn without seconds hand. |
| #define | [OPT\_NOHANDS](#gaa9bc6e351e9fb0515c69f3cd32ad5621)   [FT8XX\_OPT\_NOHANDS](group__ft8xx__copro.md#gade56de46694ca420460c1ceb26a33120) |
|  | Co-processor clock widget is drawn without hour, minutes and seconds hands. |
| #define | [BITMAPS](#ga3746a5c44f711b633ca618b6ebb8e75f)   [FT8XX\_BITMAPS](group__ft8xx__dl.md#ga28f7596c367f67f73d701b792300aa09) |
|  | Rectangular pixel arrays, in various color formats. |
| #define | [POINTS](#gae6910994a90091fe877b021c590c894e)   [FT8XX\_POINTS](group__ft8xx__dl.md#ga1d6f49b3817f9927fa1cd3cd42820490) |
|  | Anti-aliased points, point radius is 1-256 pixels. |
| #define | [LINES](#ga321ae946de24c36489276616d13c46cd)   [FT8XX\_LINES](group__ft8xx__dl.md#ga62bcf30c7a9eae4c468e1c7de144ad01) |
|  | Anti-aliased lines, with width from 0 to 4095 1/16th of pixel units. |
| #define | [LINE\_STRIP](#gac300cac409c1526ba5622f15472a25df)   [FT8XX\_LINE\_STRIP](group__ft8xx__dl.md#gac1b1188c36a4078e7db50d3c5aee7d25) |
|  | Anti-aliased lines, connected head-to-tail. |
| #define | [EDGE\_STRIP\_R](#ga8c7fa2526afa79673d93b64f864d2126)   [FT8XX\_EDGE\_STRIP\_R](group__ft8xx__dl.md#ga0b3ce2828323978e9648bfd07caa1065) |
|  | Edge strips for right. |
| #define | [EDGE\_STRIP\_L](#ga3434ce2412337ac0b7d9558ff25181d0)   [FT8XX\_EDGE\_STRIP\_L](group__ft8xx__dl.md#ga97229abf592bba4039f19a98451cdc5b) |
|  | Edge strips for left. |
| #define | [EDGE\_STRIP\_A](#gaa69720d489114390d9493d397cd392b7)   [FT8XX\_EDGE\_STRIP\_A](group__ft8xx__dl.md#gaf5ad60bbe137dbf64281ad8d0be051e0) |
|  | Edge strips for above. |
| #define | [EDGE\_STRIP\_B](#ga20ed5346e45eb4ce0e79f094c7346627)   [FT8XX\_EDGE\_STRIP\_B](group__ft8xx__dl.md#ga9aff3a3c58e12b990130271e845662a8) |
|  | Edge strips for below. |
| #define | [RECTS](#ga5868720577871792983ae813837c6189)   [FT8XX\_RECTS](group__ft8xx__dl.md#ga05077568fea624ed7e3f9e3f6e8d72b8) |
|  | Round-cornered rectangles, curvature of the corners can be adjusted using LINE\_WIDTH. |
| #define | [BEGIN](#ga34b42db00c62ff404a8bd7119fc62327)(prim) |
|  | Begin drawing a graphics primitive. |
| #define | [CLEAR](#ga218ebaaf7d9afe6257021f3c08e59959)(c, [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), t) |
|  | Clear buffers to preset values. |
| #define | [CLEAR\_COLOR\_RGB](#gae6375b17ea6f06bf81357fe9350e1c1c)(red, green, blue) |
|  | Specify clear values for red, green and blue channels. |
| #define | [COLOR\_RGB](#ga59c390601a75b4d869e7cfc58d2430bf)(red, green, blue) |
|  | Set the current color red, green and blue. |
| #define | [DISPLAY](#ga486931aa64c90970e7a4110ada3d0916)() |
|  | End the display list. |
| #define | [END](#ga569b6a4f889b0846cc0a3396f3835a17)() |
|  | End drawing a graphics primitive. |
| #define | [LINE\_WIDTH](#ga8764958e4fa66c3948353226f82cedaf)(width) |
|  | Specify the width of lines to be drawn with primitive [LINES](#ga321ae946de24c36489276616d13c46cd). |
| #define | [TAG](#ga5f17de6768f32dd36135de83c24d0a7b)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
|  | Attach the tag value for the following graphics objects. |
| #define | [VERTEX2F](#ga033cea1b18c3f010aaa0293f6972069a)(x, y) |
|  | Start the operation of graphics primitives at the specified coordinate. |
| #define | [VERTEX2II](#gae779df636416e900ddc15b95cf2a923c)(x, y, handle, cell) |
|  | Start the operation of graphics primitive at the specified coordinates. |

| Enumerations | |
| --- | --- |
| enum | [ft8xx\_memory\_map\_t](#gabbba9344e2d9b81af6313c6b7f12276c) { [RAM\_G](#ggabbba9344e2d9b81af6313c6b7f12276ca8f7e484f38038b0a390e7cad119f2cb4) = FT810\_RAM\_G , [RAM\_DL](#ggabbba9344e2d9b81af6313c6b7f12276caf2eb368364f52dcfc067e40c2a252a84) = FT810\_RAM\_DL , [REG\_](#ggabbba9344e2d9b81af6313c6b7f12276ca0e42504c57b04103704eb19348fea779) = FT810\_REG\_ , [RAM\_CMD](#ggabbba9344e2d9b81af6313c6b7f12276caff47e90e4e3dd7901dfd1cde3fb132f5) = FT810\_RAM\_CMD } |
|  | Main parts of FT810 memory map. [More...](#gabbba9344e2d9b81af6313c6b7f12276c) |
| enum | [ft8xx\_register\_address\_t](#gaa3f6afa02b5f4bed90093f659201d008) {     [REG\_TRIM](#ggaa3f6afa02b5f4bed90093f659201d008a683a15e3c7578fe44f7cee9ca5796f74) = FT810\_REG\_TRIM , [REG\_ID](#ggaa3f6afa02b5f4bed90093f659201d008a6797b58f7ec24dbf469df8a17680fb7a) = FT810\_REG\_ID , [REG\_FRAMES](#ggaa3f6afa02b5f4bed90093f659201d008ad73c12cf386d92029bef895c52a21272) = FT810\_REG\_FRAMES , [REG\_CLOCK](#ggaa3f6afa02b5f4bed90093f659201d008a2dd65dd2f5e8f97f27135c343681af64) = FT810\_REG\_CLOCK ,     [REG\_FREQUENCY](#ggaa3f6afa02b5f4bed90093f659201d008ac447562a0543880a863929676c9a2c21) = FT810\_REG\_FREQUENCY , [REG\_RENDERMODE](#ggaa3f6afa02b5f4bed90093f659201d008aebeab047c1430f0165e36f83e0ff38a9) = FT810\_REG\_RENDERMODE , [REG\_SNAPY](#ggaa3f6afa02b5f4bed90093f659201d008a9cef87cf60803317580a4bd04762bc9f) = FT810\_REG\_SNAPY , [REG\_SNAPSHOT](#ggaa3f6afa02b5f4bed90093f659201d008a81ad0d146fb392f9561bce00c6ed4e6b) = FT810\_REG\_SNAPSHOT ,     [REG\_CPURESET](#ggaa3f6afa02b5f4bed90093f659201d008a569c58d9a986415596b91856b02175b2) = FT810\_REG\_CPURESET , [REG\_TAP\_CRC](#ggaa3f6afa02b5f4bed90093f659201d008a47894772f07899e20c560b47a4b37208) = FT810\_REG\_TAP\_CRC , [REG\_TAP\_MASK](#ggaa3f6afa02b5f4bed90093f659201d008a87efcd914405639dcf24d762becd1ebd) = FT810\_REG\_TAP\_MASK , [REG\_HCYCLE](#ggaa3f6afa02b5f4bed90093f659201d008aec806fab0ed79a1a51e39395147feff2) = FT810\_REG\_HCYCLE ,     [REG\_HOFFSET](#ggaa3f6afa02b5f4bed90093f659201d008a50a3fe216944877cf4a55df00de4bd85) = FT810\_REG\_HOFFSET , [REG\_HSIZE](#ggaa3f6afa02b5f4bed90093f659201d008a3dd43d215eb4b5047b8a14406f85c8e0) = FT810\_REG\_HSIZE , [REG\_HSYNC0](#ggaa3f6afa02b5f4bed90093f659201d008accb71ca34304a4276f6b8c5d2b2e4e6a) = FT810\_REG\_HSYNC0 , [REG\_HSYNC1](#ggaa3f6afa02b5f4bed90093f659201d008a13b32d8ce6608067d1f816065547b559) = FT810\_REG\_HSYNC1 ,     [REG\_VCYCLE](#ggaa3f6afa02b5f4bed90093f659201d008ad360af56001df6e29616a11f087db26a) = FT810\_REG\_VCYCLE , [REG\_VOFFSET](#ggaa3f6afa02b5f4bed90093f659201d008ad1b8daf2ec9fe116c79d59b2d524a8a2) = FT810\_REG\_VOFFSET , [REG\_VSIZE](#ggaa3f6afa02b5f4bed90093f659201d008aa63605dbe4cf7fdb4e1d7994f22aa878) = FT810\_REG\_VSIZE , [REG\_VSYNC0](#ggaa3f6afa02b5f4bed90093f659201d008ae07735ed3259a2112898ee9330cc2050) = FT810\_REG\_VSYNC0 ,     [REG\_VSYNC1](#ggaa3f6afa02b5f4bed90093f659201d008a3193050a59229830b80c5f637a09ecbb) = FT810\_REG\_VSYNC1 , [REG\_DLSWAP](#ggaa3f6afa02b5f4bed90093f659201d008a9a09798569680c1a48880ec40502e019) = FT810\_REG\_DLSWAP , [REG\_ROTATE](#ggaa3f6afa02b5f4bed90093f659201d008ac785fd2e2498944eec5f404229c1a6f3) = FT810\_REG\_ROTATE , [REG\_OUTBITS](#ggaa3f6afa02b5f4bed90093f659201d008a55841781abfc8d3452399c79d69a2009) = FT810\_REG\_OUTBITS ,     [REG\_DITHER](#ggaa3f6afa02b5f4bed90093f659201d008a50c524cae48fcba2477cae9c422a3f5b) = FT810\_REG\_DITHER , [REG\_SWIZZLE](#ggaa3f6afa02b5f4bed90093f659201d008af1c9622660d41f1ebaf3c5151a8526f6) = FT810\_REG\_SWIZZLE , [REG\_CSPREAD](#ggaa3f6afa02b5f4bed90093f659201d008af57b15505b903b9e8d940e1156bfa83d) = FT810\_REG\_CSPREAD , [REG\_PCLK\_POL](#ggaa3f6afa02b5f4bed90093f659201d008a1fbe40f257634301cca0229d68851c6b) = FT810\_REG\_PCLK\_POL ,     [REG\_PCLK](#ggaa3f6afa02b5f4bed90093f659201d008a572feb4e0547d7b40c18c8ff7ed62b55) = FT810\_REG\_PCLK , [REG\_TAG\_X](#ggaa3f6afa02b5f4bed90093f659201d008a1ecdf33453fe848f48f0535ca23b5541) = FT810\_REG\_TAG\_X , [REG\_TAG\_Y](#ggaa3f6afa02b5f4bed90093f659201d008ac41d85f3ba86087e0e0c5c071388d254) = FT810\_REG\_TAG\_Y , [REG\_TAG](#ggaa3f6afa02b5f4bed90093f659201d008ac8690647b7274feef7b7a0695eaf9a6b) = FT810\_REG\_TAG ,     [REG\_VOL\_PB](#ggaa3f6afa02b5f4bed90093f659201d008aa024b09fec9d0440483a33e972550888) = FT810\_REG\_VOL\_PB , [REG\_VOL\_SOUND](#ggaa3f6afa02b5f4bed90093f659201d008aac293daf5a8d5221d5c4167177069970) = FT810\_REG\_VOL\_SOUND , [REG\_SOUND](#ggaa3f6afa02b5f4bed90093f659201d008adb67bd48114184e8ad04cadba731e9fe) = FT810\_REG\_SOUND , [REG\_PLAY](#ggaa3f6afa02b5f4bed90093f659201d008a29570336f1d3a7b15d2f5b76a816faa3) = FT810\_REG\_PLAY ,     [REG\_GPIO\_DIR](#ggaa3f6afa02b5f4bed90093f659201d008a7f82f6066010b61ed49a7a8bd2b9b52e) = FT810\_REG\_GPIO\_DIR , [REG\_GPIO](#ggaa3f6afa02b5f4bed90093f659201d008ad92810bdf452c531a7dda338aff3aad1) = FT810\_REG\_GPIO , [REG\_GPIOX\_DIR](#ggaa3f6afa02b5f4bed90093f659201d008a538bc67838a34c6f1dfbb8bdff984788) = FT810\_REG\_GPIOX\_DIR , [REG\_GPIOX](#ggaa3f6afa02b5f4bed90093f659201d008adc4499b79053ad08a2279b3702b79ced) = FT810\_REG\_GPIOX ,     [REG\_INT\_FLAGS](#ggaa3f6afa02b5f4bed90093f659201d008ab6fd90f08477954798d5a54cb1ddce8f) = FT810\_REG\_INT\_FLAGS , [REG\_INT\_EN](#ggaa3f6afa02b5f4bed90093f659201d008a966071326a92ac6e595b2acbb2445697) = FT810\_REG\_INT\_EN , [REG\_INT\_MASK](#ggaa3f6afa02b5f4bed90093f659201d008aba6637892ddbceafb4e558fbcffe496d) = FT810\_REG\_INT\_MASK , [REG\_PLAYBACK\_START](#ggaa3f6afa02b5f4bed90093f659201d008a95f7b2f9eb12abcdf6885ee984155d8e) = FT810\_REG\_PLAYBACK\_START ,     [REG\_PLAYBACK\_LENGTH](#ggaa3f6afa02b5f4bed90093f659201d008aa9f1905d1f2488f5c9600dc4b27753c2) = FT810\_REG\_PLAYBACK\_LENGTH , [REG\_PLAYBACK\_READPTR](#ggaa3f6afa02b5f4bed90093f659201d008aed471a111f18c5a92bcc5d7ca07e4b6d) = FT810\_REG\_PLAYBACK\_READPTR , [REG\_PLAYBACK\_FREQ](#ggaa3f6afa02b5f4bed90093f659201d008a84a2b99d9ea7f674f019f1d54c1cddc3) = FT810\_REG\_PLAYBACK\_FREQ , [REG\_PLAYBACK\_FORMAT](#ggaa3f6afa02b5f4bed90093f659201d008a68e60e0c855fff63e3a6f767f1b0179c) = FT810\_REG\_PLAYBACK\_FORMAT ,     [REG\_PLAYBACK\_LOOP](#ggaa3f6afa02b5f4bed90093f659201d008a5b712095cc16ff8866d55b95f6e081e5) = FT810\_REG\_PLAYBACK\_LOOP , [REG\_PLAYBACK\_PLAY](#ggaa3f6afa02b5f4bed90093f659201d008a59764d36f28fcf060f164e8fdfb3aba8) = FT810\_REG\_PLAYBACK\_PLAY , [REG\_PWM\_HZ](#ggaa3f6afa02b5f4bed90093f659201d008a884022eead52d6738a4f20f6a543dc50) = FT810\_REG\_PWM\_HZ , [REG\_PWM\_DUTY](#ggaa3f6afa02b5f4bed90093f659201d008a04f552a92ffd030a0cbc07d522197265) = FT810\_REG\_PWM\_DUTY ,     [REG\_CMD\_READ](#ggaa3f6afa02b5f4bed90093f659201d008af5512106f5e7d41845b1cc01ca52bf68) = FT810\_REG\_CMD\_READ , [REG\_CMD\_WRITE](#ggaa3f6afa02b5f4bed90093f659201d008ad878f3fc41274192245aa6c27209ea69) = FT810\_REG\_CMD\_WRITE , [REG\_CMD\_DL](#ggaa3f6afa02b5f4bed90093f659201d008ac1e6dcc3e508a9f5b8f061a06cda7c87) = FT810\_REG\_CMD\_DL , [REG\_TOUCH\_MODE](#ggaa3f6afa02b5f4bed90093f659201d008ae53c8a1517586c00ce5e0d19b2bbea29) = FT810\_REG\_TOUCH\_MODE ,     [REG\_TOUCH\_ADC\_MODE](#ggaa3f6afa02b5f4bed90093f659201d008a2f0c46b14b1dced78eceb5f21c6a898e) = FT810\_REG\_TOUCH\_ADC\_MODE , [REG\_TOUCH\_CHARGE](#ggaa3f6afa02b5f4bed90093f659201d008af0baf00d792cf20622f3716ee6c7fa95) = FT810\_REG\_TOUCH\_CHARGE , [REG\_TOUCH\_SETTLE](#ggaa3f6afa02b5f4bed90093f659201d008a21bec38288166e781f4e42f9e2cd88fb) = FT810\_REG\_TOUCH\_SETTLE , [REG\_TOUCH\_OVERSAMPLE](#ggaa3f6afa02b5f4bed90093f659201d008a78cb160ba1d417523093ce222504df96) = FT810\_REG\_TOUCH\_OVERSAMPLE ,     [REG\_TOUCH\_RZTHRESH](#ggaa3f6afa02b5f4bed90093f659201d008a56440ea6e79d6cb2c6374d8fab01277e) = FT810\_REG\_TOUCH\_RZTHRESH , [REG\_TOUCH\_RAW\_XY](#ggaa3f6afa02b5f4bed90093f659201d008a781bc22bc6c5671201a1740a282e1e0d) = FT810\_REG\_TOUCH\_RAW\_XY , [REG\_TOUCH\_RZ](#ggaa3f6afa02b5f4bed90093f659201d008ad63d6b6752e9a3b25c2d4eec38d9e455) = FT810\_REG\_TOUCH\_RZ , [REG\_TOUCH\_SCREEN\_XY](#ggaa3f6afa02b5f4bed90093f659201d008a857a79d4d62ee1369f10fb746e0d0aa8) = FT810\_REG\_TOUCH\_SCREEN\_XY ,     [REG\_TOUCH\_TAG\_XY](#ggaa3f6afa02b5f4bed90093f659201d008a7546d5a7b068c0b23280a189c6345789) = FT810\_REG\_TOUCH\_TAG\_XY , [REG\_TOUCH\_TAG](#ggaa3f6afa02b5f4bed90093f659201d008a86b3ad977f18ed6948a195f0d0f998af) = FT810\_REG\_TOUCH\_TAG , [REG\_TOUCH\_TRANSFORM\_A](#ggaa3f6afa02b5f4bed90093f659201d008a2725ae9bcc184f701002e0824b6cfdfd) = FT810\_REG\_TOUCH\_TRANSFORM\_A , [REG\_TOUCH\_TRANSFORM\_B](#ggaa3f6afa02b5f4bed90093f659201d008ac93146dd21c9a7e07353ae901ccea745) = FT810\_REG\_TOUCH\_TRANSFORM\_B ,     [REG\_TOUCH\_TRANSFORM\_C](#ggaa3f6afa02b5f4bed90093f659201d008a8717b3386b1e0ad11e34f7fae83ae793) = FT810\_REG\_TOUCH\_TRANSFORM\_C , [REG\_TOUCH\_TRANSFORM\_D](#ggaa3f6afa02b5f4bed90093f659201d008a9988ada9b469290b9c886ba665fb4b48) = FT810\_REG\_TOUCH\_TRANSFORM\_D , [REG\_TOUCH\_TRANSFORM\_E](#ggaa3f6afa02b5f4bed90093f659201d008a36c4f53d2e132c794695983e56cf627c) = FT810\_REG\_TOUCH\_TRANSFORM\_E , [REG\_TOUCH\_TRANSFORM\_F](#ggaa3f6afa02b5f4bed90093f659201d008a041ffbb78a6572c5c1e515843f959315) = FT810\_REG\_TOUCH\_TRANSFORM\_F ,     [REG\_TOUCH\_CONFIG](#ggaa3f6afa02b5f4bed90093f659201d008a8feeb5e4fbc73322825fdd392dbec950) = FT810\_REG\_TOUCH\_CONFIG , [REG\_SPI\_WIDTH](#ggaa3f6afa02b5f4bed90093f659201d008aa382cb5b65f2803e94ce4451ed75b848) = FT810\_REG\_SPI\_WIDTH , [REG\_TOUCH\_DIRECT\_XY](#ggaa3f6afa02b5f4bed90093f659201d008ae8dddb1bf87f77e70a03c4ad73ba51fd) = FT810\_REG\_TOUCH\_DIRECT\_XY , [REG\_TOUCH\_DIRECT\_Z1Z2](#ggaa3f6afa02b5f4bed90093f659201d008a43e6c3532c2f9573e31ddd4ce12fb8c0) = FT810\_REG\_TOUCH\_DIRECT\_Z1Z2 ,     [REG\_CMDB\_SPACE](#ggaa3f6afa02b5f4bed90093f659201d008a327a78d411cf247a6ee6e4ea5541c90c) = FT810\_REG\_CMDB\_SPACE , [REG\_CMDB\_WRITE](#ggaa3f6afa02b5f4bed90093f659201d008ae86016e9d0fb6db20d2c585300759464) = FT810\_REG\_CMDB\_WRITE , [REG\_TRACKER](#ggaa3f6afa02b5f4bed90093f659201d008ad99a270479fd9ce96e1868fb708bacbb) = FT810\_REG\_TRACKER , [REG\_TRACKER1](#ggaa3f6afa02b5f4bed90093f659201d008a49d311578982dec5afa589b0963d0622) = FT810\_REG\_TRACKER1 ,     [REG\_TRACKER2](#ggaa3f6afa02b5f4bed90093f659201d008a3bbab48e1bdad06303e631f62d7bcd76) = FT810\_REG\_TRACKER2 , [REG\_TRACKER3](#ggaa3f6afa02b5f4bed90093f659201d008ac4852d6d1ee6c7b69a3f4386354d5f2c) = FT810\_REG\_TRACKER3 , [REG\_TRACKER4](#ggaa3f6afa02b5f4bed90093f659201d008ac3f442ac6c0010066270e8373efeefcf) = FT810\_REG\_TRACKER4 , [REG\_MEDIAFIFO\_READ](#ggaa3f6afa02b5f4bed90093f659201d008a529da48e0b241ae16e8cbf1d38653c97) = FT810\_REG\_MEDIAFIFO\_READ ,     [REG\_MEDIAFIFO\_WRITE](#ggaa3f6afa02b5f4bed90093f659201d008a11a7b5722d9de6c62222a5c76f0b692b) = FT810\_REG\_MEDIAFIFO\_WRITE   } |
|  | FT810 register addresses. [More...](#gaa3f6afa02b5f4bed90093f659201d008) |

| Functions | |
| --- | --- |
| static void | [wr8](#ga1e9c6203ebb7cc15a736d074bd98c181) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) data) |
|  | Write 1 byte (8 bits) to FT8xx memory. |
| static void | [wr16](#ga8fac4ed55f7ef9d82d8dcb0eb6f09eab) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data) |
|  | Write 2 bytes (16 bits) to FT8xx memory. |
| static void | [wr32](#ga3f6814650684e2c2100d8f9a36505ca0) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) data) |
|  | Write 4 bytes (32 bits) to FT8xx memory. |
| static [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rd8](#gae96efe5496139f508083a21b2299e3d8) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address) |
|  | Read 1 byte (8 bits) from FT8xx memory. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [rd16](#ga2f833e24c067f88801884c93766d7ac7) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address) |
|  | Read 2 bytes (16 bits) from FT8xx memory. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [rd32](#ga0c6f11426fd5412a66e4f5de0a9f0847) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) address) |
|  | Read 4 bytes (32 bits) from FT8xx memory. |
| static void | [cmd](#gacde1ca3945cbe6c828f65051c5c3a615) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) command) |
|  | Execute a display list command by co-processor engine. |
| static void | [cmd\_dlstart](#ga7b9b6a41a878c449b107e51eba058799) (void) |
|  | Start a new display list. |
| static void | [cmd\_swap](#ga194d7e0d47b3d195155a22f86fbe7e7f) (void) |
|  | Swap the current display list. |
| static void | [cmd\_text](#gad642a54deaa36152ca4fea5e31294732) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) font, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) options, const char \*[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)) |
|  | Draw text. |
| static void | [cmd\_number](#gabdaf9e6cd74c0d157d1673b99707e6f2) ([int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) x, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) y, [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) font, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) options, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) n) |
|  | Draw a decimal number. |
| static void | [cmd\_calibrate](#ga26015112ae4c62a944fe671ea2cb0bda) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*result) |
|  | Execute the touch screen calibration routine. |

## Detailed Description

FT8xx reference API.

API defined according to FT800 Programmers Guide API reference definition.

Note
:   Function names defined in this header may easily collide with names provided by other modules. Include this header with caution. If naming conflict occurs instead of including this header, use `ft8xx_` prefixed names.

## Macro Definition Documentation

## [◆ ](#ga34b42db00c62ff404a8bd7119fc62327)BEGIN

| #define BEGIN | ( |  | *prim* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

**Value:**

[FT8XX\_BEGIN](group__ft8xx__dl.md#ga25324ac604e037baf26cdd37341bee44)(prim)

[FT8XX\_BEGIN](group__ft8xx__dl.md#ga25324ac604e037baf26cdd37341bee44)

#define FT8XX\_BEGIN(prim)

Begin drawing a graphics primitive.

**Definition** ft8xx\_dl.h:76

Begin drawing a graphics primitive.

The valid primitives are defined as:

- [BITMAPS](#ga3746a5c44f711b633ca618b6ebb8e75f)
- [POINTS](#gae6910994a90091fe877b021c590c894e)
- [LINES](#ga321ae946de24c36489276616d13c46cd)
- [LINE\_STRIP](#gac300cac409c1526ba5622f15472a25df)
- [EDGE\_STRIP\_R](#ga8c7fa2526afa79673d93b64f864d2126)
- [EDGE\_STRIP\_L](#ga3434ce2412337ac0b7d9558ff25181d0)
- [EDGE\_STRIP\_A](#gaa69720d489114390d9493d397cd392b7)
- [EDGE\_STRIP\_B](#ga20ed5346e45eb4ce0e79f094c7346627)
- [RECTS](#ga5868720577871792983ae813837c6189)

The primitive to be drawn is selected by the [BEGIN](#ga34b42db00c62ff404a8bd7119fc62327) command. Once the primitive is selected, it will be valid till the new primitive is selected by the [BEGIN](#ga34b42db00c62ff404a8bd7119fc62327) command.

Note
:   The primitive drawing operation will not be performed until [VERTEX2II](#gae779df636416e900ddc15b95cf2a923c) or [VERTEX2F](#ga033cea1b18c3f010aaa0293f6972069a) is executed.

Parameters
:   | prim | Graphics primitive |
    | --- | --- |

## [◆ ](#ga3746a5c44f711b633ca618b6ebb8e75f)BITMAPS

| #define BITMAPS   [FT8XX\_BITMAPS](group__ft8xx__dl.md#ga28f7596c367f67f73d701b792300aa09) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Rectangular pixel arrays, in various color formats.

## [◆ ](#ga218ebaaf7d9afe6257021f3c08e59959)CLEAR

| #define CLEAR | ( |  | *c*, |
| --- | --- | --- | --- |
|  |  |  | *[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)*, |
|  |  |  | *t* ) |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

**Value:**

[FT8XX\_CLEAR](group__ft8xx__dl.md#gab0fb60eec6f4c3b68d47f61886e7b933)(c, [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d), t)

[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)

irp nz macro MOVR cc s mov cc s endm endr irp aw macro LDR aa s

**Definition** asm-macro-32-bit-gnu.h:17

[FT8XX\_CLEAR](group__ft8xx__dl.md#gab0fb60eec6f4c3b68d47f61886e7b933)

#define FT8XX\_CLEAR(c, s, t)

Clear buffers to preset values.

**Definition** ft8xx\_dl.h:101

Clear buffers to preset values.

Setting `c` to true will clear the color buffer of the FT8xx to the preset value. Setting this bit to false will maintain the color buffer of the FT8xx with an unchanged value. The preset value is defined in command [CLEAR\_COLOR\_RGB](#gae6375b17ea6f06bf81357fe9350e1c1c) for RGB channel and CLEAR\_COLOR\_A for alpha channel.

Setting `s` to true will clear the stencil buffer of the FT8xx to the preset value. Setting this bit to false will maintain the stencil buffer of the FT8xx with an unchanged value. The preset value is defined in command CLEAR\_STENCIL.

Setting `t` to true will clear the tag buffer of the FT8xx to the preset value. Setting this bit to false will maintain the tag buffer of the FT8xx with an unchanged value. The preset value is defined in command CLEAR\_TAG.

Parameters
:   | c | Clear color buffer |
    | --- | --- |
    | [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) | Clear stencil buffer |
    | t | Clear tag buffer |

## [◆ ](#gae6375b17ea6f06bf81357fe9350e1c1c)CLEAR\_COLOR\_RGB

| #define CLEAR\_COLOR\_RGB | ( |  | *red*, |
| --- | --- | --- | --- |
|  |  |  | *green*, |
|  |  |  | *blue* ) |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

**Value:**

[FT8XX\_CLEAR\_COLOR\_RGB](group__ft8xx__dl.md#ga180b0ed70243277462cf303bc788e094)(red, green, blue)

[FT8XX\_CLEAR\_COLOR\_RGB](group__ft8xx__dl.md#ga180b0ed70243277462cf303bc788e094)

#define FT8XX\_CLEAR\_COLOR\_RGB(red, green, blue)

Specify clear values for red, green and blue channels.

**Definition** ft8xx\_dl.h:113

Specify clear values for red, green and blue channels.

Sets the color values used by a following [CLEAR](#ga218ebaaf7d9afe6257021f3c08e59959).

Parameters
:   | red | Red value used when the color buffer is cleared |
    | --- | --- |
    | green | Green value used when the color buffer is cleared |
    | blue | Blue value used when the color buffer is cleared |

## [◆ ](#ga59c390601a75b4d869e7cfc58d2430bf)COLOR\_RGB

| #define COLOR\_RGB | ( |  | *red*, |
| --- | --- | --- | --- |
|  |  |  | *green*, |
|  |  |  | *blue* ) |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

**Value:**

[FT8XX\_COLOR\_RGB](group__ft8xx__dl.md#ga3bc794705028fc7e8e1b742db180055d)(red, green, blue)

[FT8XX\_COLOR\_RGB](group__ft8xx__dl.md#ga3bc794705028fc7e8e1b742db180055d)

#define FT8XX\_COLOR\_RGB(red, green, blue)

Set the current color red, green and blue.

**Definition** ft8xx\_dl.h:128

Set the current color red, green and blue.

Sets red, green and blue values of the FT8xx color buffer which will be applied to the following draw operation.

Parameters
:   | red | Red value for the current color |
    | --- | --- |
    | green | Green value for the current color |
    | blue | Blue value for the current color |

## [◆ ](#ga486931aa64c90970e7a4110ada3d0916)DISPLAY

| #define DISPLAY | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

**Value:**

[FT8XX\_DISPLAY](group__ft8xx__dl.md#ga135472b1cdf30d4bd69372e36c9960ce)()

[FT8XX\_DISPLAY](group__ft8xx__dl.md#ga135472b1cdf30d4bd69372e36c9960ce)

#define FT8XX\_DISPLAY()

End the display list.

**Definition** ft8xx\_dl.h:138

End the display list.

FT8xx will ignore all the commands following this command.

## [◆ ](#gaa69720d489114390d9493d397cd392b7)EDGE\_STRIP\_A

| #define EDGE\_STRIP\_A   [FT8XX\_EDGE\_STRIP\_A](group__ft8xx__dl.md#gaf5ad60bbe137dbf64281ad8d0be051e0) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Edge strips for above.

## [◆ ](#ga20ed5346e45eb4ce0e79f094c7346627)EDGE\_STRIP\_B

| #define EDGE\_STRIP\_B   [FT8XX\_EDGE\_STRIP\_B](group__ft8xx__dl.md#ga9aff3a3c58e12b990130271e845662a8) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Edge strips for below.

## [◆ ](#ga3434ce2412337ac0b7d9558ff25181d0)EDGE\_STRIP\_L

| #define EDGE\_STRIP\_L   [FT8XX\_EDGE\_STRIP\_L](group__ft8xx__dl.md#ga97229abf592bba4039f19a98451cdc5b) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Edge strips for left.

## [◆ ](#ga8c7fa2526afa79673d93b64f864d2126)EDGE\_STRIP\_R

| #define EDGE\_STRIP\_R   [FT8XX\_EDGE\_STRIP\_R](group__ft8xx__dl.md#ga0b3ce2828323978e9648bfd07caa1065) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Edge strips for right.

## [◆ ](#ga569b6a4f889b0846cc0a3396f3835a17)END

| #define END | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

**Value:**

[FT8XX\_END](group__ft8xx__dl.md#ga8a9d0eb6521459eb7ce50b397de194d9)()

[FT8XX\_END](group__ft8xx__dl.md#ga8a9d0eb6521459eb7ce50b397de194d9)

#define FT8XX\_END()

End drawing a graphics primitive.

**Definition** ft8xx\_dl.h:147

End drawing a graphics primitive.

It is recommended to have an [END](#ga569b6a4f889b0846cc0a3396f3835a17) for each [BEGIN](#ga34b42db00c62ff404a8bd7119fc62327). Whereas advanced users can avoid the usage of [END](#ga569b6a4f889b0846cc0a3396f3835a17) in order to save extra graphics instructions in the display list RAM.

## [◆ ](#gac300cac409c1526ba5622f15472a25df)LINE\_STRIP

| #define LINE\_STRIP   [FT8XX\_LINE\_STRIP](group__ft8xx__dl.md#gac1b1188c36a4078e7db50d3c5aee7d25) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Anti-aliased lines, connected head-to-tail.

## [◆ ](#ga8764958e4fa66c3948353226f82cedaf)LINE\_WIDTH

| #define LINE\_WIDTH | ( |  | *width* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

**Value:**

[FT8XX\_LINE\_WIDTH](group__ft8xx__dl.md#ga1d22204625ef070a6b8d16af7ad97578)(width)

[FT8XX\_LINE\_WIDTH](group__ft8xx__dl.md#ga1d22204625ef070a6b8d16af7ad97578)

#define FT8XX\_LINE\_WIDTH(width)

Specify the width of lines to be drawn with primitive FT8XX\_LINES.

**Definition** ft8xx\_dl.h:162

Specify the width of lines to be drawn with primitive [LINES](#ga321ae946de24c36489276616d13c46cd).

Sets the width of drawn lines. The width is the distance from the center of the line to the outermost drawn pixel, in units of 1/16 pixel. The valid range is from 16 to 4095 in terms of 1/16th pixel units.

Note
:   The [LINE\_WIDTH](#ga8764958e4fa66c3948353226f82cedaf) command will affect the [LINES](#ga321ae946de24c36489276616d13c46cd), [LINE\_STRIP](#gac300cac409c1526ba5622f15472a25df), [RECTS](#ga5868720577871792983ae813837c6189), [EDGE\_STRIP\_A](#gaa69720d489114390d9493d397cd392b7) /B/R/L primitives.

Parameters
:   | width | Line width in 1/16 pixel |
    | --- | --- |

## [◆ ](#ga321ae946de24c36489276616d13c46cd)LINES

| #define LINES   [FT8XX\_LINES](group__ft8xx__dl.md#ga62bcf30c7a9eae4c468e1c7de144ad01) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Anti-aliased lines, with width from 0 to 4095 1/16th of pixel units.

(width is from center of the line to boundary)

## [◆ ](#gabf03e1cd7cb18b7c1daf243d4c1dde24)OPT\_3D

| #define OPT\_3D   [FT8XX\_OPT\_3D](group__ft8xx__copro.md#ga304badab7bd34208d499b199080fb557) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Co-processor widget is drawn in 3D effect.

## [◆ ](#ga830647bc1b42665e27813a46a6a089b7)OPT\_CENTER

| #define OPT\_CENTER   [FT8XX\_OPT\_CENTER](group__ft8xx__copro.md#ga013968a6bf9534265c897ab1f4018eb0) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Co-processor widget centers horizontally and vertically.

## [◆ ](#ga65bf92a2956ffee68057ab90be032445)OPT\_CENTERX

| #define OPT\_CENTERX   [FT8XX\_OPT\_CENTERX](group__ft8xx__copro.md#gac2d1ccbb99eaa032ed9d39fc01d32c66) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Co-processor widget centers horizontally.

## [◆ ](#gaa28880f2aa7b6d8a51518189ca08382f)OPT\_CENTERY

| #define OPT\_CENTERY   [FT8XX\_OPT\_CENTERY](group__ft8xx__copro.md#ga65b3a1e29ae425b2f1c3e66b4ea1449a) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Co-processor widget centers vertically.

## [◆ ](#gaa76b9296cd6f2eb4bec3d650b73e69cc)OPT\_FLAT

| #define OPT\_FLAT   [FT8XX\_OPT\_FLAT](group__ft8xx__copro.md#ga160b331fb401eec023e0992c6f4c6331) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Co-processor widget is drawn without 3D effect.

## [◆ ](#ga2fab787f842bb9193c9df68cb44f93fd)OPT\_MONO

| #define OPT\_MONO   [FT8XX\_OPT\_MONO](group__ft8xx__copro.md#ga415760ddf94db71ee9a504300bac4661) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Co-processor option to decode the JPEG image to L8 format, i.e., monochrome.

## [◆ ](#ga87b8705ac37fc69704f00cc2a9b8e69e)OPT\_NOBACK

| #define OPT\_NOBACK   [FT8XX\_OPT\_NOBACK](group__ft8xx__copro.md#gacb08df4fac256cbf808b133d4159aa29) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Co-processor widget has no background drawn.

## [◆ ](#ga37f793d8ac3af5f518d024727ce9f710)OPT\_NODL

| #define OPT\_NODL   [FT8XX\_OPT\_NODL](group__ft8xx__copro.md#gacc953470460b083c0b8bd9ebbc8ed03b) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

No display list commands generated for bitmap decoded from JPEG image.

## [◆ ](#gaa9bc6e351e9fb0515c69f3cd32ad5621)OPT\_NOHANDS

| #define OPT\_NOHANDS   [FT8XX\_OPT\_NOHANDS](group__ft8xx__copro.md#gade56de46694ca420460c1ceb26a33120) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Co-processor clock widget is drawn without hour, minutes and seconds hands.

## [◆ ](#ga1e7090a0dbcee600a5472f5fc4343824)OPT\_NOHM

| #define OPT\_NOHM   [FT8XX\_OPT\_NOHM](group__ft8xx__copro.md#ga79938d9c1193d44a527ca8c158117a86) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Co-processor clock widget is drawn without hour and minutes hands, only seconds hand is drawn.

## [◆ ](#ga0eb8abce5677ca0e6948ec1a003958de)OPT\_NOPOINTER

| #define OPT\_NOPOINTER   [FT8XX\_OPT\_NOPOINTER](group__ft8xx__copro.md#ga1a9838a862ec166bfe95d64144b9a052) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

The Co-processor gauge has no pointer.

## [◆ ](#ga190c29e3a00685c3f8c4906df37720ae)OPT\_NOSECS

| #define OPT\_NOSECS   [FT8XX\_OPT\_NOSECS](group__ft8xx__copro.md#ga6416f4282d2c483d2adba8c1215ab638) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Co-processor clock widget is drawn without seconds hand.

## [◆ ](#gaed772e3cf2529e698fa8e69ee73f91f9)OPT\_NOTICKS

| #define OPT\_NOTICKS   [FT8XX\_OPT\_NOTICKS](group__ft8xx__copro.md#ga50f4fac88e4f4b558450adcda33dae93) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Co-processor clock widget is drawn without hour ticks.

Gauge widget is drawn without major and minor ticks.

## [◆ ](#ga53f763f1e5de09b5e51242df87af8fb8)OPT\_RGB565

| #define OPT\_RGB565   [FT8XX\_OPT\_RGB565](group__ft8xx__copro.md#ga3a79c1128bdb9fe094843688691a085c) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Co-processor option to decode the JPEG image to RGB565 format.

## [◆ ](#gae0088375e797e08fa3e14dc3124c1e90)OPT\_RIGHTX

| #define OPT\_RIGHTX   [FT8XX\_OPT\_RIGHTX](group__ft8xx__copro.md#gac864c155bc2121bf8d3954e1ed8dbb7e) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

The label on the Coprocessor widget is right justified.

## [◆ ](#gae0fef45ae7ca3a45286a19a47bd46943)OPT\_SIGNED

| #define OPT\_SIGNED   [FT8XX\_OPT\_SIGNED](group__ft8xx__copro.md#ga5a58155896cdb2d0f1693d203706ce93) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

The number is treated as 32 bit signed integer.

## [◆ ](#gae6910994a90091fe877b021c590c894e)POINTS

| #define POINTS   [FT8XX\_POINTS](group__ft8xx__dl.md#ga1d6f49b3817f9927fa1cd3cd42820490) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Anti-aliased points, point radius is 1-256 pixels.

## [◆ ](#ga5868720577871792983ae813837c6189)RECTS

| #define RECTS   [FT8XX\_RECTS](group__ft8xx__dl.md#ga05077568fea624ed7e3f9e3f6e8d72b8) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Round-cornered rectangles, curvature of the corners can be adjusted using LINE\_WIDTH.

## [◆ ](#ga5f17de6768f32dd36135de83c24d0a7b)TAG

| #define TAG | ( |  | *[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

**Value:**

[FT8XX\_TAG](group__ft8xx__dl.md#gab0721051bb3f3cb9f555f696f36dfbbf)([s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d))

[FT8XX\_TAG](group__ft8xx__dl.md#gab0721051bb3f3cb9f555f696f36dfbbf)

#define FT8XX\_TAG(s)

Attach the tag value for the following graphics objects.

**Definition** ft8xx\_dl.h:183

Attach the tag value for the following graphics objects.

The initial value of the tag buffer of the FT8xx is specified by command CLEAR\_TAG and taken effect by command [CLEAR](#ga218ebaaf7d9afe6257021f3c08e59959). [TAG](#ga5f17de6768f32dd36135de83c24d0a7b) command can specify the value of the tag buffer of the FT8xx that applies to the graphics objects when they are drawn on the screen. This [TAG](#ga5f17de6768f32dd36135de83c24d0a7b) value will be assigned to all the following objects, unless the TAG\_MASK command is used to disable it. Once the following graphics objects are drawn, they are attached with the tag value successfully. When the graphics objects attached with the tag value are touched, the register [REG\_TOUCH\_TAG](#ggaa3f6afa02b5f4bed90093f659201d008a86b3ad977f18ed6948a195f0d0f998af) will be updated with the tag value of the graphics object being touched. If there is no [TAG](#ga5f17de6768f32dd36135de83c24d0a7b) commands in one display list, all the graphics objects rendered by the display list will report tag value as 255 in [REG\_TOUCH\_TAG](#ggaa3f6afa02b5f4bed90093f659201d008a86b3ad977f18ed6948a195f0d0f998af) when they were touched.

Parameters
:   | [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) | Tag value 1-255 |
    | --- | --- |

## [◆ ](#ga033cea1b18c3f010aaa0293f6972069a)VERTEX2F

| #define VERTEX2F | ( |  | *x*, |
| --- | --- | --- | --- |
|  |  |  | *y* ) |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

**Value:**

[FT8XX\_VERTEX2F](group__ft8xx__dl.md#ga2648ab069991c02b2e8de62bf13913ab)(x, y)

[FT8XX\_VERTEX2F](group__ft8xx__dl.md#ga2648ab069991c02b2e8de62bf13913ab)

#define FT8XX\_VERTEX2F(x, y)

Start the operation of graphics primitives at the specified coordinate.

**Definition** ft8xx\_dl.h:197

Start the operation of graphics primitives at the specified coordinate.

The range of coordinates is from -16384 to +16383 in terms of 1/16th pixel units. The negative x coordinate value means the coordinate in the left virtual screen from (0, 0), while the negative y coordinate value means the coordinate in the upper virtual screen from (0, 0). If drawing on the negative coordinate position, the drawing operation will not be visible.

Parameters
:   | x | Signed x-coordinate in 1/16 pixel precision |
    | --- | --- |
    | y | Signed y-coordinate in 1/16 pixel precision |

## [◆ ](#gae779df636416e900ddc15b95cf2a923c)VERTEX2II

| #define VERTEX2II | ( |  | *x*, |
| --- | --- | --- | --- |
|  |  |  | *y*, |
|  |  |  | *handle*, |
|  |  |  | *cell* ) |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

**Value:**

[FT8XX\_VERTEX2II](group__ft8xx__dl.md#ga560836cd8c85599f24e5623a3e286b12)(x, y, handle, cell)

[FT8XX\_VERTEX2II](group__ft8xx__dl.md#ga560836cd8c85599f24e5623a3e286b12)

#define FT8XX\_VERTEX2II(x, y, handle, cell)

Start the operation of graphics primitive at the specified coordinates.

**Definition** ft8xx\_dl.h:216

Start the operation of graphics primitive at the specified coordinates.

The valid range of `handle` is from 0 to 31. From 16 to 31 the bitmap handle is dedicated to the FT8xx built-in font.

Cell number is the index of bitmap with same bitmap layout and format. For example, for handle 31, the cell 65 means the character "A" in the largest built in font.

Parameters
:   | x | x-coordinate in pixels, from 0 to 511 |
    | --- | --- |
    | y | y-coordinate in pixels, from 0 to 511 |
    | handle | Bitmap handle |
    | cell | Cell number |

## Enumeration Type Documentation

## [◆ ](#gabbba9344e2d9b81af6313c6b7f12276c)ft8xx\_memory\_map\_t

| enum [ft8xx\_memory\_map\_t](#gabbba9344e2d9b81af6313c6b7f12276c) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Main parts of FT810 memory map.

| Enumerator | |
| --- | --- |
| RAM\_G |  |
| RAM\_DL |  |
| REG\_ |  |
| RAM\_CMD |  |

## [◆ ](#gaa3f6afa02b5f4bed90093f659201d008)ft8xx\_register\_address\_t

| enum [ft8xx\_register\_address\_t](#gaa3f6afa02b5f4bed90093f659201d008) |
| --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

FT810 register addresses.

| Enumerator | |
| --- | --- |
| REG\_TRIM |  |
| REG\_ID |  |
| REG\_FRAMES |  |
| REG\_CLOCK |  |
| REG\_FREQUENCY |  |
| REG\_RENDERMODE |  |
| REG\_SNAPY |  |
| REG\_SNAPSHOT |  |
| REG\_CPURESET |  |
| REG\_TAP\_CRC |  |
| REG\_TAP\_MASK |  |
| REG\_HCYCLE |  |
| REG\_HOFFSET |  |
| REG\_HSIZE |  |
| REG\_HSYNC0 |  |
| REG\_HSYNC1 |  |
| REG\_VCYCLE |  |
| REG\_VOFFSET |  |
| REG\_VSIZE |  |
| REG\_VSYNC0 |  |
| REG\_VSYNC1 |  |
| REG\_DLSWAP |  |
| REG\_ROTATE |  |
| REG\_OUTBITS |  |
| REG\_DITHER |  |
| REG\_SWIZZLE |  |
| REG\_CSPREAD |  |
| REG\_PCLK\_POL |  |
| REG\_PCLK |  |
| REG\_TAG\_X |  |
| REG\_TAG\_Y |  |
| REG\_TAG |  |
| REG\_VOL\_PB |  |
| REG\_VOL\_SOUND |  |
| REG\_SOUND |  |
| REG\_PLAY |  |
| REG\_GPIO\_DIR |  |
| REG\_GPIO |  |
| REG\_GPIOX\_DIR |  |
| REG\_GPIOX |  |
| REG\_INT\_FLAGS |  |
| REG\_INT\_EN |  |
| REG\_INT\_MASK |  |
| REG\_PLAYBACK\_START |  |
| REG\_PLAYBACK\_LENGTH |  |
| REG\_PLAYBACK\_READPTR |  |
| REG\_PLAYBACK\_FREQ |  |
| REG\_PLAYBACK\_FORMAT |  |
| REG\_PLAYBACK\_LOOP |  |
| REG\_PLAYBACK\_PLAY |  |
| REG\_PWM\_HZ |  |
| REG\_PWM\_DUTY |  |
| REG\_CMD\_READ |  |
| REG\_CMD\_WRITE |  |
| REG\_CMD\_DL |  |
| REG\_TOUCH\_MODE |  |
| REG\_TOUCH\_ADC\_MODE |  |
| REG\_TOUCH\_CHARGE |  |
| REG\_TOUCH\_SETTLE |  |
| REG\_TOUCH\_OVERSAMPLE |  |
| REG\_TOUCH\_RZTHRESH |  |
| REG\_TOUCH\_RAW\_XY |  |
| REG\_TOUCH\_RZ |  |
| REG\_TOUCH\_SCREEN\_XY |  |
| REG\_TOUCH\_TAG\_XY |  |
| REG\_TOUCH\_TAG |  |
| REG\_TOUCH\_TRANSFORM\_A |  |
| REG\_TOUCH\_TRANSFORM\_B |  |
| REG\_TOUCH\_TRANSFORM\_C |  |
| REG\_TOUCH\_TRANSFORM\_D |  |
| REG\_TOUCH\_TRANSFORM\_E |  |
| REG\_TOUCH\_TRANSFORM\_F |  |
| REG\_TOUCH\_CONFIG |  |
| REG\_SPI\_WIDTH |  |
| REG\_TOUCH\_DIRECT\_XY |  |
| REG\_TOUCH\_DIRECT\_Z1Z2 |  |
| REG\_CMDB\_SPACE |  |
| REG\_CMDB\_WRITE |  |
| REG\_TRACKER |  |
| REG\_TRACKER1 |  |
| REG\_TRACKER2 |  |
| REG\_TRACKER3 |  |
| REG\_TRACKER4 |  |
| REG\_MEDIAFIFO\_READ |  |
| REG\_MEDIAFIFO\_WRITE |  |

## Function Documentation

## [◆ ](#gacde1ca3945cbe6c828f65051c5c3a615)cmd()

| | void cmd | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *command* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Execute a display list command by co-processor engine.

Parameters
:   | command | Display list command to execute |
    | --- | --- |

## [◆ ](#ga26015112ae4c62a944fe671ea2cb0bda)cmd\_calibrate()

| | void cmd\_calibrate | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *result* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Execute the touch screen calibration routine.

The calibration procedure collects three touches from the touch screen, then computes and loads an appropriate matrix into REG\_TOUCH\_TRANSFORM\_A-F. To use it, create a display list and then use CMD\_CALIBRATE. The co-processor engine overlays the touch targets on the current display list, gathers the calibration input and updates REG\_TOUCH\_TRANSFORM\_A-F.

Parameters
:   | result | Calibration result, written with 0 on failure of calibration |
    | --- | --- |

## [◆ ](#ga7b9b6a41a878c449b107e51eba058799)cmd\_dlstart()

| | void cmd\_dlstart | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Start a new display list.

## [◆ ](#gabdaf9e6cd74c0d157d1673b99707e6f2)cmd\_number()

| | void cmd\_number | ( | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *x*, | | --- | --- | --- | --- | |  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *y*, | |  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *font*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *options*, | |  |  | [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | *n* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Draw a decimal number.

By default (`x`, `y`) is the top-left pixel of the text. OPT\_CENTERX centers the text horizontally, OPT\_CENTERY centers it vertically. OPT\_CENTER centers the text in both directions. OPT\_RIGHTX right-justifies the text, so that the `x` is the rightmost pixel. By default the number is displayed with no leading zeroes, but if a width 1-9 is specified in the `options`, then the number is padded if necessary with leading zeroes so that it has the given width. If OPT\_SIGNED is given, the number is treated as signed, and prefixed by a minus sign if negative.

Parameters
:   | x | x-coordinate of text base, in pixels |
    | --- | --- |
    | y | y-coordinate of text base, in pixels |
    | font | Font to use for text, 0-31. 16-31 are ROM fonts |
    | options | Options to apply |
    | n | The number to display. |

## [◆ ](#ga194d7e0d47b3d195155a22f86fbe7e7f)cmd\_swap()

| | void cmd\_swap | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Swap the current display list.

## [◆ ](#gad642a54deaa36152ca4fea5e31294732)cmd\_text()

| | void cmd\_text | ( | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *x*, | | --- | --- | --- | --- | |  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *y*, | |  |  | [int16\_t](stdint_8h.md#afe270aee8d96ad7f279a4020b9d58bdf) | *font*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *options*, | |  |  | const char \* | *s* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Draw text.

By default (x,y) is the top-left pixel of the text and the value of `options` is zero. OPT\_CENTERX centers the text horizontally, OPT\_CENTERY centers it vertically. OPT\_CENTER centers the text in both directions. OPT\_RIGHTX right-justifies the text, so that the x is the rightmost pixel.

Parameters
:   | x | x-coordinate of text base, in pixels |
    | --- | --- |
    | y | y-coordinate of text base, in pixels |
    | font | Font to use for text, 0-31. 16-31 are ROM fonts |
    | options | Options to apply |
    | [s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d) | Character string to display, terminated with a null character |

## [◆ ](#ga2f833e24c067f88801884c93766d7ac7)rd16()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) rd16 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *address* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Read 2 bytes (16 bits) from FT8xx memory.

Parameters
:   | address | Memory address to read from |
    | --- | --- |

Returns
:   Value read from memory

## [◆ ](#ga0c6f11426fd5412a66e4f5de0a9f0847)rd32()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) rd32 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *address* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Read 4 bytes (32 bits) from FT8xx memory.

Parameters
:   | address | Memory address to read from |
    | --- | --- |

Returns
:   Value read from memory

## [◆ ](#gae96efe5496139f508083a21b2299e3d8)rd8()

| | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) rd8 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *address* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Read 1 byte (8 bits) from FT8xx memory.

Parameters
:   | address | Memory address to read from |
    | --- | --- |

Returns
:   Value read from memory

## [◆ ](#ga8fac4ed55f7ef9d82d8dcb0eb6f09eab)wr16()

| | void wr16 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *address*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Write 2 bytes (16 bits) to FT8xx memory.

Parameters
:   | address | Memory address to write to |
    | --- | --- |
    | data | Value to write |

## [◆ ](#ga3f6814650684e2c2100d8f9a36505ca0)wr32()

| | void wr32 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *address*, | | --- | --- | --- | --- | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Write 4 bytes (32 bits) to FT8xx memory.

Parameters
:   | address | Memory address to write to |
    | --- | --- |
    | data | Value to write |

## [◆ ](#ga1e9c6203ebb7cc15a736d074bd98c181)wr8()

| | void wr8 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *address*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[ft8xx_reference_api.h](ft8xx__reference__api_8h.md)>`

Write 1 byte (8 bits) to FT8xx memory.

Parameters
:   | address | Memory address to write to |
    | --- | --- |
    | data | Byte to write |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
