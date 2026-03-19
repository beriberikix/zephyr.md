---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/arm__mpu__v7m_8h.html
original_path: doxygen/html/arm__mpu__v7m_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arm\_mpu\_v7m.h File Reference

`#include <cmsis_core.h>`

[Go to the source code of this file.](arm__mpu__v7m_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [arm\_mpu\_region\_attr](structarm__mpu__region__attr.md) |
| struct | [k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md) |

| Macros | |
| --- | --- |
| #define | [NO\_ACCESS](#adb0cdfabc13b3915c548413e3bdae0dd)   0x0 |
| #define | [NO\_ACCESS\_Msk](#ab6960e0c54d19d3180d2f89a69f94ac7)   (([NO\_ACCESS](#adb0cdfabc13b3915c548413e3bdae0dd) << [MPU\_RASR\_AP\_Pos](arm_2cortex__a__r_2mpu_8h.md#ac919b25b709081bac1fe1d30e6ca53d7)) & [MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)) |
| #define | [P\_NA\_U\_NA](#a07a285af1f0c83b06a49b3b7b8751dca)   0x0 |
| #define | [P\_NA\_U\_NA\_Msk](#ab47b49bf96328887c7e2b548170c9d88)   (([P\_NA\_U\_NA](#a07a285af1f0c83b06a49b3b7b8751dca) << [MPU\_RASR\_AP\_Pos](arm_2cortex__a__r_2mpu_8h.md#ac919b25b709081bac1fe1d30e6ca53d7)) & [MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)) |
| #define | [P\_RW\_U\_NA](#a6632f2c0eba4d5aee046a86258100215)   0x1 |
| #define | [P\_RW\_U\_NA\_Msk](#a8a5805b5b1a6ca5cf5f59b2874ec68d7)   (([P\_RW\_U\_NA](#a6632f2c0eba4d5aee046a86258100215) << [MPU\_RASR\_AP\_Pos](arm_2cortex__a__r_2mpu_8h.md#ac919b25b709081bac1fe1d30e6ca53d7)) & [MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)) |
| #define | [P\_RW\_U\_RO](#a723850f2bb2947b771d4a967efc86de3)   0x2 |
| #define | [P\_RW\_U\_RO\_Msk](#abccd688a7c1aa1302bfec6f9ea98b9b8)   (([P\_RW\_U\_RO](#a723850f2bb2947b771d4a967efc86de3) << [MPU\_RASR\_AP\_Pos](arm_2cortex__a__r_2mpu_8h.md#ac919b25b709081bac1fe1d30e6ca53d7)) & [MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)) |
| #define | [P\_RW\_U\_RW](#a8faee650ae8cc79e1d3605f251c3df34)   0x3U |
| #define | [P\_RW\_U\_RW\_Msk](#adc9ba826d1bf9a013724b7a24e9535db)   (([P\_RW\_U\_RW](#a8faee650ae8cc79e1d3605f251c3df34) << [MPU\_RASR\_AP\_Pos](arm_2cortex__a__r_2mpu_8h.md#ac919b25b709081bac1fe1d30e6ca53d7)) & [MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)) |
| #define | [FULL\_ACCESS](#a4da15c917ab4e26cd3e5e39dbec83000)   0x3 |
| #define | [FULL\_ACCESS\_Msk](#a1da8e3113a0446b3d2acbe78b4e40b0c)   (([FULL\_ACCESS](#a4da15c917ab4e26cd3e5e39dbec83000) << [MPU\_RASR\_AP\_Pos](arm_2cortex__a__r_2mpu_8h.md#ac919b25b709081bac1fe1d30e6ca53d7)) & [MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)) |
| #define | [P\_RO\_U\_NA](#ad3012e82dde223bbe84c9e4d7c46e7fd)   0x5 |
| #define | [P\_RO\_U\_NA\_Msk](#aeec24407a5fffaf967a841a26ccf46ed)   (([P\_RO\_U\_NA](#ad3012e82dde223bbe84c9e4d7c46e7fd) << [MPU\_RASR\_AP\_Pos](arm_2cortex__a__r_2mpu_8h.md#ac919b25b709081bac1fe1d30e6ca53d7)) & [MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)) |
| #define | [P\_RO\_U\_RO](#a75fd88fb93da28e84017d4ba6fcb4211)   0x6 |
| #define | [P\_RO\_U\_RO\_Msk](#a4ec38b9015a95b2aafca5e9aa35f1f46)   (([P\_RO\_U\_RO](#a75fd88fb93da28e84017d4ba6fcb4211) << [MPU\_RASR\_AP\_Pos](arm_2cortex__a__r_2mpu_8h.md#ac919b25b709081bac1fe1d30e6ca53d7)) & [MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)) |
| #define | [RO](#a628642b04c07236ae1e986c248a79ae5)   0x7 |
| #define | [RO\_Msk](#a35e3f724856c6947c52885def2e3c0d6)   (([RO](#a628642b04c07236ae1e986c248a79ae5) << [MPU\_RASR\_AP\_Pos](arm_2cortex__a__r_2mpu_8h.md#ac919b25b709081bac1fe1d30e6ca53d7)) & [MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)) |
| #define | [NOT\_EXEC](#a74c8c1c16d8d613d7b32d5fe9bd5d08d)   [MPU\_RASR\_XN\_Msk](arm_2cortex__a__r_2mpu_8h.md#a4f8afc5cc7fca2ada211f8b09c76802e) |
| #define | [STRONGLY\_ORDERED\_SHAREABLE](#ae48be083a1ebbb7d3378b319830486f4)   [MPU\_RASR\_S\_Msk](arm_2cortex__a__r_2mpu_8h.md#a872c0922578c2e74304886579e9a2361) |
| #define | [DEVICE\_SHAREABLE](#a274cfa7f4a2f1f1e799d70c28db866ff)   ([MPU\_RASR\_B\_Msk](arm_2cortex__a__r_2mpu_8h.md#af97de2b86316d5b29931fc6f70b3cba1) | [MPU\_RASR\_S\_Msk](arm_2cortex__a__r_2mpu_8h.md#a872c0922578c2e74304886579e9a2361)) |
| #define | [NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_SHAREABLE](#a918f12d12d1248fdedf627880868f92b)   ([MPU\_RASR\_C\_Msk](arm_2cortex__a__r_2mpu_8h.md#af841f9bee5046fece4f513ecf707a3c1) | [MPU\_RASR\_S\_Msk](arm_2cortex__a__r_2mpu_8h.md#a872c0922578c2e74304886579e9a2361)) |
| #define | [NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_NON\_SHAREABLE](#a25ba780869ac5ae4d9267d6e0c0a31c0)   [MPU\_RASR\_C\_Msk](arm_2cortex__a__r_2mpu_8h.md#af841f9bee5046fece4f513ecf707a3c1) |
| #define | [NORMAL\_OUTER\_INNER\_WRITE\_BACK\_SHAREABLE](#a98ca2a3b1e78f1032b211d1815cc37db)   ([MPU\_RASR\_C\_Msk](arm_2cortex__a__r_2mpu_8h.md#af841f9bee5046fece4f513ecf707a3c1) | [MPU\_RASR\_B\_Msk](arm_2cortex__a__r_2mpu_8h.md#af97de2b86316d5b29931fc6f70b3cba1) | [MPU\_RASR\_S\_Msk](arm_2cortex__a__r_2mpu_8h.md#a872c0922578c2e74304886579e9a2361)) |
| #define | [NORMAL\_OUTER\_INNER\_WRITE\_BACK\_NON\_SHAREABLE](#abcce878498db83cd7be9704ec6cff918)   ([MPU\_RASR\_C\_Msk](arm_2cortex__a__r_2mpu_8h.md#af841f9bee5046fece4f513ecf707a3c1) | [MPU\_RASR\_B\_Msk](arm_2cortex__a__r_2mpu_8h.md#af97de2b86316d5b29931fc6f70b3cba1)) |
| #define | [NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE](#a313a77cea9e62aa04620f88bbb1d784b)   ((1 << [MPU\_RASR\_TEX\_Pos](arm_2cortex__a__r_2mpu_8h.md#a340f1c91469c5bb4ee91bc29ad21c631)) | [MPU\_RASR\_S\_Msk](arm_2cortex__a__r_2mpu_8h.md#a872c0922578c2e74304886579e9a2361)) |
| #define | [NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_NON\_SHAREABLE](#a16b75f4910b2a70d5517b093d48aaafc)   (1 << [MPU\_RASR\_TEX\_Pos](arm_2cortex__a__r_2mpu_8h.md#a340f1c91469c5bb4ee91bc29ad21c631)) |
| #define | [NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_SHAREABLE](#a89f98f53169e8eb0f232287f2e839991)   ((1 << [MPU\_RASR\_TEX\_Pos](arm_2cortex__a__r_2mpu_8h.md#a340f1c91469c5bb4ee91bc29ad21c631)) | [MPU\_RASR\_C\_Msk](arm_2cortex__a__r_2mpu_8h.md#af841f9bee5046fece4f513ecf707a3c1) | [MPU\_RASR\_B\_Msk](arm_2cortex__a__r_2mpu_8h.md#af97de2b86316d5b29931fc6f70b3cba1) | [MPU\_RASR\_S\_Msk](arm_2cortex__a__r_2mpu_8h.md#a872c0922578c2e74304886579e9a2361)) |
| #define | [NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE](#ab5e00d6a3a95abd2a1b3ab1744117d9c)   ((1 << [MPU\_RASR\_TEX\_Pos](arm_2cortex__a__r_2mpu_8h.md#a340f1c91469c5bb4ee91bc29ad21c631)) | [MPU\_RASR\_C\_Msk](arm_2cortex__a__r_2mpu_8h.md#af841f9bee5046fece4f513ecf707a3c1) | [MPU\_RASR\_B\_Msk](arm_2cortex__a__r_2mpu_8h.md#af97de2b86316d5b29931fc6f70b3cba1)) |
| #define | [DEVICE\_NON\_SHAREABLE](#a27a7c7934b8cb593aa2653a828bcd6ca)   (2 << [MPU\_RASR\_TEX\_Pos](arm_2cortex__a__r_2mpu_8h.md#a340f1c91469c5bb4ee91bc29ad21c631)) |
| #define | [SUB\_REGION\_0\_DISABLED](#ad97f565065c8e799b72494ffd2d057cd)   ((0x01 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk) |
| #define | [SUB\_REGION\_1\_DISABLED](#ad7f3c3c3cc4de407f0885a2d26930d1a)   ((0x02 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk) |
| #define | [SUB\_REGION\_2\_DISABLED](#a4939cd3e0ae7cd570a2aeef7c35e6bdc)   ((0x04 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk) |
| #define | [SUB\_REGION\_3\_DISABLED](#a24a64a4fb8bdf8af5422b6896f5215ab)   ((0x08 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk) |
| #define | [SUB\_REGION\_4\_DISABLED](#ae1e5b3747711b1b0e26b8be9d8ee1e73)   ((0x10 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk) |
| #define | [SUB\_REGION\_5\_DISABLED](#ae2810b78a1826f0660dfe07c3e23d493)   ((0x20 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk) |
| #define | [SUB\_REGION\_6\_DISABLED](#a67fcfd53ed1d703d0636d0807fc9c05e)   ((0x40 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk) |
| #define | [SUB\_REGION\_7\_DISABLED](#ad31907a27479655d251d170c66feee4b)   ((0x80 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk) |
| #define | [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(size) |
| #define | [REGION\_32B](#a5cb4dfcb39c8cddde7d00be07abbf186)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(32B) |
| #define | [REGION\_64B](#af0032361a1f7303ea36d4a78484ed991)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(64B) |
| #define | [REGION\_128B](#af93290eb28d2d1eafaa1cad375cb994e)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(128B) |
| #define | [REGION\_256B](#ae4a7b8266e1048e53ab72a96af99dfa9)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(256B) |
| #define | [REGION\_512B](#abef640d835bc8fe9e49ebb23fed5eacc)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(512B) |
| #define | [REGION\_1K](#a9216de2e7190dedac57efc79367a6c49)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(1[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| #define | [REGION\_2K](#aa22b0f233ecd96b8097e45260110845e)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(2[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| #define | [REGION\_4K](#a0dd685b0698d16ea2bed3b7ac3038a41)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(4[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| #define | [REGION\_8K](#a0d4b53088d0e9e4e4552c5b4a496731d)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(8[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| #define | [REGION\_16K](#a1f382e52ddd7a8c50571664736cb2b27)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(16[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| #define | [REGION\_32K](#a5354ce614160f66300ac71616f708a61)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(32[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| #define | [REGION\_64K](#ab75ccffbfbc1389e1303bb2415dc7c24)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(64[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| #define | [REGION\_128K](#ab6ee612fe19a00c67fba398da06f6f09)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(128[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| #define | [REGION\_256K](#a8a949eee20d66206a9c700eb68f4a614)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(256[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| #define | [REGION\_512K](#ae5fc1f5ea7a3bbbc85dce33cee2aa85b)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(512[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| #define | [REGION\_1M](#a1ad0013ace85d499c8d554602066c7e1)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(1[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| #define | [REGION\_2M](#a1bc46af188d58128dce0e7f6bf851515)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(2[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| #define | [REGION\_4M](#a4837e15ddf1dfa198442883d705d5eb1)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(4[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| #define | [REGION\_8M](#a464e54c991784aed5061b93adcfc387e)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(8[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| #define | [REGION\_16M](#ace038f88373aec532761c3c4f5193be3)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(16[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| #define | [REGION\_32M](#a2dacd02f000be694c6e4e1bcfe4e6d6e)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(32[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| #define | [REGION\_64M](#a66785668a244bc13dd0c5553a68384d2)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(64[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| #define | [REGION\_128M](#a2f0bf4c7ad62232ed5a185cb65708be0)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(128[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| #define | [REGION\_256M](#a81428ec21df3db24dee2b09c5f2c3ad5)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(256[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| #define | [REGION\_512M](#a4f61982635b2ed4099836c61811a8ce6)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(512[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| #define | [REGION\_1G](#ac959b468a34a1b202e3682f15bcd26fe)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(1[GB](group__sys-util.md#gaf207e8203eedc05adcf341a24bfa6cbb)) |
| #define | [REGION\_2G](#a97835cec29142060938be2d53438e9f6)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(2[GB](group__sys-util.md#gaf207e8203eedc05adcf341a24bfa6cbb)) |
| #define | [REGION\_4G](#ac14cdd5594b034fa65f3baf6b2e2bde9)   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(4[GB](group__sys-util.md#gaf207e8203eedc05adcf341a24bfa6cbb)) |
| #define | [ARM\_MPU\_REGION\_INIT](#a2ec2a5ebe99ddac405570be52bc3a728)(p\_name, p\_base, p\_size, p\_attr) |
| #define | [REGION\_RAM\_ATTR](#a6398aeba1eacd0df079a35ab3cd69e76)(size) |
| #define | [REGION\_RAM\_NOCACHE\_ATTR](#a0f03b499ca2a55d2a5ae725b98d8ecbf)(size) |
| #define | [REGION\_FLASH\_ATTR](#a27f4a4d075d6c2ecd477c48f0455fe6f)(size) |
| #define | [REGION\_PPB\_ATTR](#a4d9881dc6866259e26659132277f6c9c)(size) |
| #define | [REGION\_IO\_ATTR](#ae8d8bc85a76a356e67c858b7667b75ff)(size) |
| #define | [REGION\_EXTMEM\_ATTR](#aecd4c6b6a33d0ecf4a03d3226f88eba8)(size) |
| #define | [K\_MEM\_PARTITION\_P\_NA\_U\_NA](#a73bc6803ccf24aad395089a4395bd22f) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_RW](#a9b7cc3c51f518517031d76807470aa10) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_RO](#a6636a59c913e035646a1a9e5ed61559d) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_NA](#a3c52d13e42a66beb72d088ac56388951) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_RO](#a708338371e91b5a3f2d44f9ae48849db) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_NA](#a706eaa9c515f1cc859d97ef8455b2f2f) |
| #define | [K\_MEM\_PARTITION\_P\_RWX\_U\_RWX](#a29db5fb48087c0cae596ff212989ed24) |
| #define | [K\_MEM\_PARTITION\_P\_RWX\_U\_RX](#a81878d7a3177ef4c37ea3046da004c9a) |
| #define | [K\_MEM\_PARTITION\_P\_RX\_U\_RX](#a78f9b21aa8b5c894db28328f5a1e2641) |
| #define | [K\_MEM\_PARTITION\_IS\_WRITABLE](#a7879968909ce2f0e33763ae1e2fc9d84)(attr) |
| #define | [K\_MEM\_PARTITION\_IS\_EXECUTABLE](#ab6fb9b9c6c1c968a11ae80bfd70fec26)(attr) |
| #define | [K\_MEM\_PARTITION\_P\_NA\_U\_NA\_NOCACHE](#a0abe69d327f9f9e04781785cd1bfb634) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_RW\_NOCACHE](#afb811f7933ed0147b255c170427e0fb6) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_RO\_NOCACHE](#acb4a60ca2e609aa9b2d4dca10d6a5fee) |
| #define | [K\_MEM\_PARTITION\_P\_RW\_U\_NA\_NOCACHE](#a8c982ab9a12ea1da0b7505c915832e89) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_RO\_NOCACHE](#a840d782e977d03ed4f9ca5858f61d1a5) |
| #define | [K\_MEM\_PARTITION\_P\_RO\_U\_NA\_NOCACHE](#ae47c158f93de002298e0c46a47c6337e) |
| #define | [K\_MEM\_PARTITION\_P\_RWX\_U\_RWX\_NOCACHE](#a5bcd5603dda3c2825a0eca8a7d994d83) |
| #define | [K\_MEM\_PARTITION\_P\_RWX\_U\_RX\_NOCACHE](#a738443a56ab0abe8d04efa98c65763fb) |
| #define | [K\_MEM\_PARTITION\_P\_RX\_U\_RX\_NOCACHE](#a0b22795be27057cc03e6f49d1e1e455d) |

| Typedefs | |
| --- | --- |
| typedef struct [arm\_mpu\_region\_attr](structarm__mpu__region__attr.md) | [arm\_mpu\_region\_attr\_t](#a1bf1c09c9012aa693f7ce40b7af2dae6) |

## Macro Definition Documentation

## [◆ ](#a2ec2a5ebe99ddac405570be52bc3a728)ARM\_MPU\_REGION\_INIT

| #define ARM\_MPU\_REGION\_INIT | ( |  | *p\_name*, |
| --- | --- | --- | --- |
|  |  |  | *p\_base*, |
|  |  |  | *p\_size*, |
|  |  |  | *p\_attr* ) |

**Value:**

{ \

.name = p\_name, \

.base = p\_base, \

.attr = p\_attr(size\_to\_mpu\_rasr\_size(p\_size)), \

}

## [◆ ](#a27a7c7934b8cb593aa2653a828bcd6ca)DEVICE\_NON\_SHAREABLE

| #define DEVICE\_NON\_SHAREABLE   (2 << [MPU\_RASR\_TEX\_Pos](arm_2cortex__a__r_2mpu_8h.md#a340f1c91469c5bb4ee91bc29ad21c631)) |
| --- |

## [◆ ](#a274cfa7f4a2f1f1e799d70c28db866ff)DEVICE\_SHAREABLE

| #define DEVICE\_SHAREABLE   ([MPU\_RASR\_B\_Msk](arm_2cortex__a__r_2mpu_8h.md#af97de2b86316d5b29931fc6f70b3cba1) | [MPU\_RASR\_S\_Msk](arm_2cortex__a__r_2mpu_8h.md#a872c0922578c2e74304886579e9a2361)) |
| --- |

## [◆ ](#a4da15c917ab4e26cd3e5e39dbec83000)FULL\_ACCESS

| #define FULL\_ACCESS   0x3 |
| --- |

## [◆ ](#a1da8e3113a0446b3d2acbe78b4e40b0c)FULL\_ACCESS\_Msk

| #define FULL\_ACCESS\_Msk   (([FULL\_ACCESS](#a4da15c917ab4e26cd3e5e39dbec83000) << [MPU\_RASR\_AP\_Pos](arm_2cortex__a__r_2mpu_8h.md#ac919b25b709081bac1fe1d30e6ca53d7)) & [MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)) |
| --- |

## [◆ ](#ab6fb9b9c6c1c968a11ae80bfd70fec26)K\_MEM\_PARTITION\_IS\_EXECUTABLE

| #define K\_MEM\_PARTITION\_IS\_EXECUTABLE | ( |  | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(!((attr.rasr\_attr) & ([NOT\_EXEC](#a74c8c1c16d8d613d7b32d5fe9bd5d08d))))

[NOT\_EXEC](#a74c8c1c16d8d613d7b32d5fe9bd5d08d)

#define NOT\_EXEC

**Definition** arm\_mpu\_v7m.h:46

## [◆ ](#a7879968909ce2f0e33763ae1e2fc9d84)K\_MEM\_PARTITION\_IS\_WRITABLE

| #define K\_MEM\_PARTITION\_IS\_WRITABLE | ( |  | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

({ \

int \_\_is\_writable\_\_; \

switch (attr.rasr\_attr & [MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)) { \

case [P\_RW\_U\_RW\_Msk](#adc9ba826d1bf9a013724b7a24e9535db): \

case [P\_RW\_U\_RO\_Msk](#abccd688a7c1aa1302bfec6f9ea98b9b8): \

case [P\_RW\_U\_NA\_Msk](#a8a5805b5b1a6ca5cf5f59b2874ec68d7): \

\_\_is\_writable\_\_ = 1; \

break; \

default: \

\_\_is\_writable\_\_ = 0; \

} \

\_\_is\_writable\_\_; \

})

[MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)

#define MPU\_RASR\_AP\_Msk

**Definition** mpu.h:21

[P\_RW\_U\_NA\_Msk](#a8a5805b5b1a6ca5cf5f59b2874ec68d7)

#define P\_RW\_U\_NA\_Msk

**Definition** arm\_mpu\_v7m.h:25

[P\_RW\_U\_RO\_Msk](#abccd688a7c1aa1302bfec6f9ea98b9b8)

#define P\_RW\_U\_RO\_Msk

**Definition** arm\_mpu\_v7m.h:28

[P\_RW\_U\_RW\_Msk](#adc9ba826d1bf9a013724b7a24e9535db)

#define P\_RW\_U\_RW\_Msk

**Definition** arm\_mpu\_v7m.h:31

## [◆ ](#a73bc6803ccf24aad395089a4395bd22f)K\_MEM\_PARTITION\_P\_NA\_U\_NA

| #define K\_MEM\_PARTITION\_P\_NA\_U\_NA |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)){ \

\_K\_MEM\_PARTITION\_P\_NA\_U\_NA | \

[NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE](#ab5e00d6a3a95abd2a1b3ab1744117d9c)})

[NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE](#ab5e00d6a3a95abd2a1b3ab1744117d9c)

#define NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE

**Definition** arm\_mpu\_v7m.h:62

[k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)

**Definition** arm\_mpu\_v7m.h:143

## [◆ ](#a0abe69d327f9f9e04781785cd1bfb634)K\_MEM\_PARTITION\_P\_NA\_U\_NA\_NOCACHE

| #define K\_MEM\_PARTITION\_P\_NA\_U\_NA\_NOCACHE |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)){ \

(\_K\_MEM\_PARTITION\_P\_NA\_U\_NA | [NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE](#a313a77cea9e62aa04620f88bbb1d784b))})

[NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE](#a313a77cea9e62aa04620f88bbb1d784b)

#define NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE

**Definition** arm\_mpu\_v7m.h:58

## [◆ ](#a706eaa9c515f1cc859d97ef8455b2f2f)K\_MEM\_PARTITION\_P\_RO\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RO\_U\_NA |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)){ \

\_K\_MEM\_PARTITION\_P\_RO\_U\_NA | \

[NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE](#ab5e00d6a3a95abd2a1b3ab1744117d9c)})

## [◆ ](#ae47c158f93de002298e0c46a47c6337e)K\_MEM\_PARTITION\_P\_RO\_U\_NA\_NOCACHE

| #define K\_MEM\_PARTITION\_P\_RO\_U\_NA\_NOCACHE |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)){ \

(\_K\_MEM\_PARTITION\_P\_RO\_U\_NA | [NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE](#a313a77cea9e62aa04620f88bbb1d784b))})

## [◆ ](#a708338371e91b5a3f2d44f9ae48849db)K\_MEM\_PARTITION\_P\_RO\_U\_RO

| #define K\_MEM\_PARTITION\_P\_RO\_U\_RO |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)){ \

\_K\_MEM\_PARTITION\_P\_RO\_U\_RO | \

[NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE](#ab5e00d6a3a95abd2a1b3ab1744117d9c)})

## [◆ ](#a840d782e977d03ed4f9ca5858f61d1a5)K\_MEM\_PARTITION\_P\_RO\_U\_RO\_NOCACHE

| #define K\_MEM\_PARTITION\_P\_RO\_U\_RO\_NOCACHE |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)){ \

(\_K\_MEM\_PARTITION\_P\_RO\_U\_RO | [NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE](#a313a77cea9e62aa04620f88bbb1d784b))})

## [◆ ](#a3c52d13e42a66beb72d088ac56388951)K\_MEM\_PARTITION\_P\_RW\_U\_NA

| #define K\_MEM\_PARTITION\_P\_RW\_U\_NA |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)){ \

\_K\_MEM\_PARTITION\_P\_RW\_U\_NA | \

[NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE](#ab5e00d6a3a95abd2a1b3ab1744117d9c)})

## [◆ ](#a8c982ab9a12ea1da0b7505c915832e89)K\_MEM\_PARTITION\_P\_RW\_U\_NA\_NOCACHE

| #define K\_MEM\_PARTITION\_P\_RW\_U\_NA\_NOCACHE |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)){ \

(\_K\_MEM\_PARTITION\_P\_RW\_U\_NA | [NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE](#a313a77cea9e62aa04620f88bbb1d784b))})

## [◆ ](#a6636a59c913e035646a1a9e5ed61559d)K\_MEM\_PARTITION\_P\_RW\_U\_RO

| #define K\_MEM\_PARTITION\_P\_RW\_U\_RO |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)){ \

\_K\_MEM\_PARTITION\_P\_RW\_U\_RO | \

[NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE](#ab5e00d6a3a95abd2a1b3ab1744117d9c)})

## [◆ ](#acb4a60ca2e609aa9b2d4dca10d6a5fee)K\_MEM\_PARTITION\_P\_RW\_U\_RO\_NOCACHE

| #define K\_MEM\_PARTITION\_P\_RW\_U\_RO\_NOCACHE |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)){ \

(\_K\_MEM\_PARTITION\_P\_RW\_U\_RO | [NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE](#a313a77cea9e62aa04620f88bbb1d784b))})

## [◆ ](#a9b7cc3c51f518517031d76807470aa10)K\_MEM\_PARTITION\_P\_RW\_U\_RW

| #define K\_MEM\_PARTITION\_P\_RW\_U\_RW |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)){ \

\_K\_MEM\_PARTITION\_P\_RW\_U\_RW | \

[NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE](#ab5e00d6a3a95abd2a1b3ab1744117d9c)})

## [◆ ](#afb811f7933ed0147b255c170427e0fb6)K\_MEM\_PARTITION\_P\_RW\_U\_RW\_NOCACHE

| #define K\_MEM\_PARTITION\_P\_RW\_U\_RW\_NOCACHE |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)){ \

(\_K\_MEM\_PARTITION\_P\_RW\_U\_RW | [NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE](#a313a77cea9e62aa04620f88bbb1d784b))})

## [◆ ](#a29db5fb48087c0cae596ff212989ed24)K\_MEM\_PARTITION\_P\_RWX\_U\_RWX

| #define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)){ \

\_K\_MEM\_PARTITION\_P\_RWX\_U\_RWX | \

[NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE](#ab5e00d6a3a95abd2a1b3ab1744117d9c)})

## [◆ ](#a5bcd5603dda3c2825a0eca8a7d994d83)K\_MEM\_PARTITION\_P\_RWX\_U\_RWX\_NOCACHE

| #define K\_MEM\_PARTITION\_P\_RWX\_U\_RWX\_NOCACHE |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)){ \

(\_K\_MEM\_PARTITION\_P\_RWX\_U\_RWX | [NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE](#a313a77cea9e62aa04620f88bbb1d784b))})

## [◆ ](#a81878d7a3177ef4c37ea3046da004c9a)K\_MEM\_PARTITION\_P\_RWX\_U\_RX

| #define K\_MEM\_PARTITION\_P\_RWX\_U\_RX |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)){ \

\_K\_MEM\_PARTITION\_P\_RWX\_U\_RX | \

[NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE](#ab5e00d6a3a95abd2a1b3ab1744117d9c)})

## [◆ ](#a738443a56ab0abe8d04efa98c65763fb)K\_MEM\_PARTITION\_P\_RWX\_U\_RX\_NOCACHE

| #define K\_MEM\_PARTITION\_P\_RWX\_U\_RX\_NOCACHE |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)){ \

(\_K\_MEM\_PARTITION\_P\_RWX\_U\_RX | [NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE](#a313a77cea9e62aa04620f88bbb1d784b))})

## [◆ ](#a78f9b21aa8b5c894db28328f5a1e2641)K\_MEM\_PARTITION\_P\_RX\_U\_RX

| #define K\_MEM\_PARTITION\_P\_RX\_U\_RX |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)){ \

\_K\_MEM\_PARTITION\_P\_RX\_U\_RX | \

[NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE](#ab5e00d6a3a95abd2a1b3ab1744117d9c)})

## [◆ ](#a0b22795be27057cc03e6f49d1e1e455d)K\_MEM\_PARTITION\_P\_RX\_U\_RX\_NOCACHE

| #define K\_MEM\_PARTITION\_P\_RX\_U\_RX\_NOCACHE |
| --- |

**Value:**

(([k\_mem\_partition\_attr\_t](structk__mem__partition__attr__t.md)){ \

(\_K\_MEM\_PARTITION\_P\_RX\_U\_RX | [NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE](#a313a77cea9e62aa04620f88bbb1d784b))})

## [◆ ](#adb0cdfabc13b3915c548413e3bdae0dd)NO\_ACCESS

| #define NO\_ACCESS   0x0 |
| --- |

## [◆ ](#ab6960e0c54d19d3180d2f89a69f94ac7)NO\_ACCESS\_Msk

| #define NO\_ACCESS\_Msk   (([NO\_ACCESS](#adb0cdfabc13b3915c548413e3bdae0dd) << [MPU\_RASR\_AP\_Pos](arm_2cortex__a__r_2mpu_8h.md#ac919b25b709081bac1fe1d30e6ca53d7)) & [MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)) |
| --- |

## [◆ ](#a16b75f4910b2a70d5517b093d48aaafc)NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_NON\_SHAREABLE

| #define NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_NON\_SHAREABLE   (1 << [MPU\_RASR\_TEX\_Pos](arm_2cortex__a__r_2mpu_8h.md#a340f1c91469c5bb4ee91bc29ad21c631)) |
| --- |

## [◆ ](#a313a77cea9e62aa04620f88bbb1d784b)NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE

| #define NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_SHAREABLE   ((1 << [MPU\_RASR\_TEX\_Pos](arm_2cortex__a__r_2mpu_8h.md#a340f1c91469c5bb4ee91bc29ad21c631)) | [MPU\_RASR\_S\_Msk](arm_2cortex__a__r_2mpu_8h.md#a872c0922578c2e74304886579e9a2361)) |
| --- |

## [◆ ](#abcce878498db83cd7be9704ec6cff918)NORMAL\_OUTER\_INNER\_WRITE\_BACK\_NON\_SHAREABLE

| #define NORMAL\_OUTER\_INNER\_WRITE\_BACK\_NON\_SHAREABLE   ([MPU\_RASR\_C\_Msk](arm_2cortex__a__r_2mpu_8h.md#af841f9bee5046fece4f513ecf707a3c1) | [MPU\_RASR\_B\_Msk](arm_2cortex__a__r_2mpu_8h.md#af97de2b86316d5b29931fc6f70b3cba1)) |
| --- |

## [◆ ](#a98ca2a3b1e78f1032b211d1815cc37db)NORMAL\_OUTER\_INNER\_WRITE\_BACK\_SHAREABLE

| #define NORMAL\_OUTER\_INNER\_WRITE\_BACK\_SHAREABLE   ([MPU\_RASR\_C\_Msk](arm_2cortex__a__r_2mpu_8h.md#af841f9bee5046fece4f513ecf707a3c1) | [MPU\_RASR\_B\_Msk](arm_2cortex__a__r_2mpu_8h.md#af97de2b86316d5b29931fc6f70b3cba1) | [MPU\_RASR\_S\_Msk](arm_2cortex__a__r_2mpu_8h.md#a872c0922578c2e74304886579e9a2361)) |
| --- |

## [◆ ](#ab5e00d6a3a95abd2a1b3ab1744117d9c)NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE

| #define NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE   ((1 << [MPU\_RASR\_TEX\_Pos](arm_2cortex__a__r_2mpu_8h.md#a340f1c91469c5bb4ee91bc29ad21c631)) | [MPU\_RASR\_C\_Msk](arm_2cortex__a__r_2mpu_8h.md#af841f9bee5046fece4f513ecf707a3c1) | [MPU\_RASR\_B\_Msk](arm_2cortex__a__r_2mpu_8h.md#af97de2b86316d5b29931fc6f70b3cba1)) |
| --- |

## [◆ ](#a89f98f53169e8eb0f232287f2e839991)NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_SHAREABLE

| #define NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_SHAREABLE   ((1 << [MPU\_RASR\_TEX\_Pos](arm_2cortex__a__r_2mpu_8h.md#a340f1c91469c5bb4ee91bc29ad21c631)) | [MPU\_RASR\_C\_Msk](arm_2cortex__a__r_2mpu_8h.md#af841f9bee5046fece4f513ecf707a3c1) | [MPU\_RASR\_B\_Msk](arm_2cortex__a__r_2mpu_8h.md#af97de2b86316d5b29931fc6f70b3cba1) | [MPU\_RASR\_S\_Msk](arm_2cortex__a__r_2mpu_8h.md#a872c0922578c2e74304886579e9a2361)) |
| --- |

## [◆ ](#a25ba780869ac5ae4d9267d6e0c0a31c0)NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_NON\_SHAREABLE

| #define NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_NON\_SHAREABLE   [MPU\_RASR\_C\_Msk](arm_2cortex__a__r_2mpu_8h.md#af841f9bee5046fece4f513ecf707a3c1) |
| --- |

## [◆ ](#a918f12d12d1248fdedf627880868f92b)NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_SHAREABLE

| #define NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_SHAREABLE   ([MPU\_RASR\_C\_Msk](arm_2cortex__a__r_2mpu_8h.md#af841f9bee5046fece4f513ecf707a3c1) | [MPU\_RASR\_S\_Msk](arm_2cortex__a__r_2mpu_8h.md#a872c0922578c2e74304886579e9a2361)) |
| --- |

## [◆ ](#a74c8c1c16d8d613d7b32d5fe9bd5d08d)NOT\_EXEC

| #define NOT\_EXEC   [MPU\_RASR\_XN\_Msk](arm_2cortex__a__r_2mpu_8h.md#a4f8afc5cc7fca2ada211f8b09c76802e) |
| --- |

## [◆ ](#a07a285af1f0c83b06a49b3b7b8751dca)P\_NA\_U\_NA

| #define P\_NA\_U\_NA   0x0 |
| --- |

## [◆ ](#ab47b49bf96328887c7e2b548170c9d88)P\_NA\_U\_NA\_Msk

| #define P\_NA\_U\_NA\_Msk   (([P\_NA\_U\_NA](#a07a285af1f0c83b06a49b3b7b8751dca) << [MPU\_RASR\_AP\_Pos](arm_2cortex__a__r_2mpu_8h.md#ac919b25b709081bac1fe1d30e6ca53d7)) & [MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)) |
| --- |

## [◆ ](#ad3012e82dde223bbe84c9e4d7c46e7fd)P\_RO\_U\_NA

| #define P\_RO\_U\_NA   0x5 |
| --- |

## [◆ ](#aeec24407a5fffaf967a841a26ccf46ed)P\_RO\_U\_NA\_Msk

| #define P\_RO\_U\_NA\_Msk   (([P\_RO\_U\_NA](#ad3012e82dde223bbe84c9e4d7c46e7fd) << [MPU\_RASR\_AP\_Pos](arm_2cortex__a__r_2mpu_8h.md#ac919b25b709081bac1fe1d30e6ca53d7)) & [MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)) |
| --- |

## [◆ ](#a75fd88fb93da28e84017d4ba6fcb4211)P\_RO\_U\_RO

| #define P\_RO\_U\_RO   0x6 |
| --- |

## [◆ ](#a4ec38b9015a95b2aafca5e9aa35f1f46)P\_RO\_U\_RO\_Msk

| #define P\_RO\_U\_RO\_Msk   (([P\_RO\_U\_RO](#a75fd88fb93da28e84017d4ba6fcb4211) << [MPU\_RASR\_AP\_Pos](arm_2cortex__a__r_2mpu_8h.md#ac919b25b709081bac1fe1d30e6ca53d7)) & [MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)) |
| --- |

## [◆ ](#a6632f2c0eba4d5aee046a86258100215)P\_RW\_U\_NA

| #define P\_RW\_U\_NA   0x1 |
| --- |

## [◆ ](#a8a5805b5b1a6ca5cf5f59b2874ec68d7)P\_RW\_U\_NA\_Msk

| #define P\_RW\_U\_NA\_Msk   (([P\_RW\_U\_NA](#a6632f2c0eba4d5aee046a86258100215) << [MPU\_RASR\_AP\_Pos](arm_2cortex__a__r_2mpu_8h.md#ac919b25b709081bac1fe1d30e6ca53d7)) & [MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)) |
| --- |

## [◆ ](#a723850f2bb2947b771d4a967efc86de3)P\_RW\_U\_RO

| #define P\_RW\_U\_RO   0x2 |
| --- |

## [◆ ](#abccd688a7c1aa1302bfec6f9ea98b9b8)P\_RW\_U\_RO\_Msk

| #define P\_RW\_U\_RO\_Msk   (([P\_RW\_U\_RO](#a723850f2bb2947b771d4a967efc86de3) << [MPU\_RASR\_AP\_Pos](arm_2cortex__a__r_2mpu_8h.md#ac919b25b709081bac1fe1d30e6ca53d7)) & [MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)) |
| --- |

## [◆ ](#a8faee650ae8cc79e1d3605f251c3df34)P\_RW\_U\_RW

| #define P\_RW\_U\_RW   0x3U |
| --- |

## [◆ ](#adc9ba826d1bf9a013724b7a24e9535db)P\_RW\_U\_RW\_Msk

| #define P\_RW\_U\_RW\_Msk   (([P\_RW\_U\_RW](#a8faee650ae8cc79e1d3605f251c3df34) << [MPU\_RASR\_AP\_Pos](arm_2cortex__a__r_2mpu_8h.md#ac919b25b709081bac1fe1d30e6ca53d7)) & [MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)) |
| --- |

## [◆ ](#af93290eb28d2d1eafaa1cad375cb994e)REGION\_128B

| #define REGION\_128B   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(128B) |
| --- |

## [◆ ](#ab6ee612fe19a00c67fba398da06f6f09)REGION\_128K

| #define REGION\_128K   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(128[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| --- |

## [◆ ](#a2f0bf4c7ad62232ed5a185cb65708be0)REGION\_128M

| #define REGION\_128M   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(128[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| --- |

## [◆ ](#a1f382e52ddd7a8c50571664736cb2b27)REGION\_16K

| #define REGION\_16K   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(16[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| --- |

## [◆ ](#ace038f88373aec532761c3c4f5193be3)REGION\_16M

| #define REGION\_16M   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(16[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| --- |

## [◆ ](#ac959b468a34a1b202e3682f15bcd26fe)REGION\_1G

| #define REGION\_1G   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(1[GB](group__sys-util.md#gaf207e8203eedc05adcf341a24bfa6cbb)) |
| --- |

## [◆ ](#a9216de2e7190dedac57efc79367a6c49)REGION\_1K

| #define REGION\_1K   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(1[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| --- |

## [◆ ](#a1ad0013ace85d499c8d554602066c7e1)REGION\_1M

| #define REGION\_1M   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(1[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| --- |

## [◆ ](#ae4a7b8266e1048e53ab72a96af99dfa9)REGION\_256B

| #define REGION\_256B   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(256B) |
| --- |

## [◆ ](#a8a949eee20d66206a9c700eb68f4a614)REGION\_256K

| #define REGION\_256K   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(256[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| --- |

## [◆ ](#a81428ec21df3db24dee2b09c5f2c3ad5)REGION\_256M

| #define REGION\_256M   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(256[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| --- |

## [◆ ](#a97835cec29142060938be2d53438e9f6)REGION\_2G

| #define REGION\_2G   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(2[GB](group__sys-util.md#gaf207e8203eedc05adcf341a24bfa6cbb)) |
| --- |

## [◆ ](#aa22b0f233ecd96b8097e45260110845e)REGION\_2K

| #define REGION\_2K   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(2[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| --- |

## [◆ ](#a1bc46af188d58128dce0e7f6bf851515)REGION\_2M

| #define REGION\_2M   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(2[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| --- |

## [◆ ](#a5cb4dfcb39c8cddde7d00be07abbf186)REGION\_32B

| #define REGION\_32B   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(32B) |
| --- |

## [◆ ](#a5354ce614160f66300ac71616f708a61)REGION\_32K

| #define REGION\_32K   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(32[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| --- |

## [◆ ](#a2dacd02f000be694c6e4e1bcfe4e6d6e)REGION\_32M

| #define REGION\_32M   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(32[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| --- |

## [◆ ](#ac14cdd5594b034fa65f3baf6b2e2bde9)REGION\_4G

| #define REGION\_4G   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(4[GB](group__sys-util.md#gaf207e8203eedc05adcf341a24bfa6cbb)) |
| --- |

## [◆ ](#a0dd685b0698d16ea2bed3b7ac3038a41)REGION\_4K

| #define REGION\_4K   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(4[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| --- |

## [◆ ](#a4837e15ddf1dfa198442883d705d5eb1)REGION\_4M

| #define REGION\_4M   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(4[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| --- |

## [◆ ](#abef640d835bc8fe9e49ebb23fed5eacc)REGION\_512B

| #define REGION\_512B   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(512B) |
| --- |

## [◆ ](#ae5fc1f5ea7a3bbbc85dce33cee2aa85b)REGION\_512K

| #define REGION\_512K   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(512[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| --- |

## [◆ ](#a4f61982635b2ed4099836c61811a8ce6)REGION\_512M

| #define REGION\_512M   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(512[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| --- |

## [◆ ](#af0032361a1f7303ea36d4a78484ed991)REGION\_64B

| #define REGION\_64B   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(64B) |
| --- |

## [◆ ](#ab75ccffbfbc1389e1303bb2415dc7c24)REGION\_64K

| #define REGION\_64K   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(64[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| --- |

## [◆ ](#a66785668a244bc13dd0c5553a68384d2)REGION\_64M

| #define REGION\_64M   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(64[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| --- |

## [◆ ](#a0d4b53088d0e9e4e4552c5b4a496731d)REGION\_8K

| #define REGION\_8K   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(8[KB](group__sys-util.md#ga5c723c0cc71b83224ead557db3ab74dd)) |
| --- |

## [◆ ](#a464e54c991784aed5061b93adcfc387e)REGION\_8M

| #define REGION\_8M   [REGION\_SIZE](#acbb181cf8ed1acc7fd43431321e94ee4)(8[MB](group__sys-util.md#ga44d2b171cc92225ec0a76ef70fc9b531)) |
| --- |

## [◆ ](#aecd4c6b6a33d0ecf4a03d3226f88eba8)REGION\_EXTMEM\_ATTR

| #define REGION\_EXTMEM\_ATTR | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{([STRONGLY\_ORDERED\_SHAREABLE](#ae48be083a1ebbb7d3378b319830486f4) | size | [NO\_ACCESS\_Msk](#ab6960e0c54d19d3180d2f89a69f94ac7))}

[NO\_ACCESS\_Msk](#ab6960e0c54d19d3180d2f89a69f94ac7)

#define NO\_ACCESS\_Msk

**Definition** arm\_mpu\_v7m.h:19

[STRONGLY\_ORDERED\_SHAREABLE](#ae48be083a1ebbb7d3378b319830486f4)

#define STRONGLY\_ORDERED\_SHAREABLE

**Definition** arm\_mpu\_v7m.h:49

## [◆ ](#a27f4a4d075d6c2ecd477c48f0455fe6f)REGION\_FLASH\_ATTR

| #define REGION\_FLASH\_ATTR | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{([NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_NON\_SHAREABLE](#a25ba780869ac5ae4d9267d6e0c0a31c0) | size | [RO\_Msk](#a35e3f724856c6947c52885def2e3c0d6))}

[NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_NON\_SHAREABLE](#a25ba780869ac5ae4d9267d6e0c0a31c0)

#define NORMAL\_OUTER\_INNER\_WRITE\_THROUGH\_NON\_SHAREABLE

**Definition** arm\_mpu\_v7m.h:52

[RO\_Msk](#a35e3f724856c6947c52885def2e3c0d6)

#define RO\_Msk

**Definition** arm\_mpu\_v7m.h:43

## [◆ ](#ae8d8bc85a76a356e67c858b7667b75ff)REGION\_IO\_ATTR

| #define REGION\_IO\_ATTR | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{([DEVICE\_NON\_SHAREABLE](#a27a7c7934b8cb593aa2653a828bcd6ca) | size | [P\_RW\_U\_NA\_Msk](#a8a5805b5b1a6ca5cf5f59b2874ec68d7))}

[DEVICE\_NON\_SHAREABLE](#a27a7c7934b8cb593aa2653a828bcd6ca)

#define DEVICE\_NON\_SHAREABLE

**Definition** arm\_mpu\_v7m.h:64

## [◆ ](#a4d9881dc6866259e26659132277f6c9c)REGION\_PPB\_ATTR

| #define REGION\_PPB\_ATTR | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{([STRONGLY\_ORDERED\_SHAREABLE](#ae48be083a1ebbb7d3378b319830486f4) | size | [P\_RW\_U\_NA\_Msk](#a8a5805b5b1a6ca5cf5f59b2874ec68d7))}

## [◆ ](#a6398aeba1eacd0df079a35ab3cd69e76)REGION\_RAM\_ATTR

| #define REGION\_RAM\_ATTR | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{([NORMAL\_OUTER\_INNER\_WRITE\_BACK\_WRITE\_READ\_ALLOCATE\_NON\_SHAREABLE](#ab5e00d6a3a95abd2a1b3ab1744117d9c) | \

IF\_ENABLED(CONFIG\_XIP, ([MPU\_RASR\_XN\_Msk](arm_2cortex__a__r_2mpu_8h.md#a4f8afc5cc7fca2ada211f8b09c76802e) |)) size | [P\_RW\_U\_NA\_Msk](#a8a5805b5b1a6ca5cf5f59b2874ec68d7))}

[MPU\_RASR\_XN\_Msk](arm_2cortex__a__r_2mpu_8h.md#a4f8afc5cc7fca2ada211f8b09c76802e)

#define MPU\_RASR\_XN\_Msk

**Definition** mpu.h:18

## [◆ ](#a0f03b499ca2a55d2a5ae725b98d8ecbf)REGION\_RAM\_NOCACHE\_ATTR

| #define REGION\_RAM\_NOCACHE\_ATTR | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{([NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_NON\_SHAREABLE](#a16b75f4910b2a70d5517b093d48aaafc) | [MPU\_RASR\_XN\_Msk](arm_2cortex__a__r_2mpu_8h.md#a4f8afc5cc7fca2ada211f8b09c76802e) | size | [P\_RW\_U\_NA\_Msk](#a8a5805b5b1a6ca5cf5f59b2874ec68d7))}

[NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_NON\_SHAREABLE](#a16b75f4910b2a70d5517b093d48aaafc)

#define NORMAL\_OUTER\_INNER\_NON\_CACHEABLE\_NON\_SHAREABLE

**Definition** arm\_mpu\_v7m.h:59

## [◆ ](#acbb181cf8ed1acc7fd43431321e94ee4)REGION\_SIZE

| #define REGION\_SIZE | ( |  | *size* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

((ARM\_MPU\_REGION\_SIZE\_##size << [MPU\_RASR\_SIZE\_Pos](arm_2cortex__a__r_2mpu_8h.md#ad90549193db0d2b7e70d3d52cb902710)) & [MPU\_RASR\_SIZE\_Msk](arm_2cortex__a__r_2mpu_8h.md#a222e237e51f20d0e8a8c249295e77298))

[MPU\_RASR\_SIZE\_Msk](arm_2cortex__a__r_2mpu_8h.md#a222e237e51f20d0e8a8c249295e77298)

#define MPU\_RASR\_SIZE\_Msk

**Definition** mpu.h:12

[MPU\_RASR\_SIZE\_Pos](arm_2cortex__a__r_2mpu_8h.md#ad90549193db0d2b7e70d3d52cb902710)

#define MPU\_RASR\_SIZE\_Pos

**Definition** mpu.h:11

## [◆ ](#a628642b04c07236ae1e986c248a79ae5)RO

| #define RO   0x7 |
| --- |

## [◆ ](#a35e3f724856c6947c52885def2e3c0d6)RO\_Msk

| #define RO\_Msk   (([RO](#a628642b04c07236ae1e986c248a79ae5) << [MPU\_RASR\_AP\_Pos](arm_2cortex__a__r_2mpu_8h.md#ac919b25b709081bac1fe1d30e6ca53d7)) & [MPU\_RASR\_AP\_Msk](arm_2cortex__a__r_2mpu_8h.md#a81da5e9383eca09414642d65fcbc14de)) |
| --- |

## [◆ ](#ae48be083a1ebbb7d3378b319830486f4)STRONGLY\_ORDERED\_SHAREABLE

| #define STRONGLY\_ORDERED\_SHAREABLE   [MPU\_RASR\_S\_Msk](arm_2cortex__a__r_2mpu_8h.md#a872c0922578c2e74304886579e9a2361) |
| --- |

## [◆ ](#ad97f565065c8e799b72494ffd2d057cd)SUB\_REGION\_0\_DISABLED

| #define SUB\_REGION\_0\_DISABLED   ((0x01 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk) |
| --- |

## [◆ ](#ad7f3c3c3cc4de407f0885a2d26930d1a)SUB\_REGION\_1\_DISABLED

| #define SUB\_REGION\_1\_DISABLED   ((0x02 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk) |
| --- |

## [◆ ](#a4939cd3e0ae7cd570a2aeef7c35e6bdc)SUB\_REGION\_2\_DISABLED

| #define SUB\_REGION\_2\_DISABLED   ((0x04 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk) |
| --- |

## [◆ ](#a24a64a4fb8bdf8af5422b6896f5215ab)SUB\_REGION\_3\_DISABLED

| #define SUB\_REGION\_3\_DISABLED   ((0x08 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk) |
| --- |

## [◆ ](#ae1e5b3747711b1b0e26b8be9d8ee1e73)SUB\_REGION\_4\_DISABLED

| #define SUB\_REGION\_4\_DISABLED   ((0x10 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk) |
| --- |

## [◆ ](#ae2810b78a1826f0660dfe07c3e23d493)SUB\_REGION\_5\_DISABLED

| #define SUB\_REGION\_5\_DISABLED   ((0x20 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk) |
| --- |

## [◆ ](#a67fcfd53ed1d703d0636d0807fc9c05e)SUB\_REGION\_6\_DISABLED

| #define SUB\_REGION\_6\_DISABLED   ((0x40 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk) |
| --- |

## [◆ ](#ad31907a27479655d251d170c66feee4b)SUB\_REGION\_7\_DISABLED

| #define SUB\_REGION\_7\_DISABLED   ((0x80 << MPU\_RASR\_SRD\_Pos) & MPU\_RASR\_SRD\_Msk) |
| --- |

## Typedef Documentation

## [◆ ](#a1bf1c09c9012aa693f7ce40b7af2dae6)arm\_mpu\_region\_attr\_t

| typedef struct [arm\_mpu\_region\_attr](structarm__mpu__region__attr.md) [arm\_mpu\_region\_attr\_t](#a1bf1c09c9012aa693f7ce40b7af2dae6) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [mpu](dir_56106ba8e9de679e2771f91f794159ff.md)
- [arm\_mpu\_v7m.h](arm__mpu__v7m_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
