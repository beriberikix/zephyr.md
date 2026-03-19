---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nrf__comp_8h.html
original_path: doxygen/html/nrf__comp_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nrf\_comp.h File Reference

`#include <[zephyr/drivers/comparator.h](comparator_8h_source.md)>`

[Go to the source code of this file.](nrf__comp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [comp\_nrf\_comp\_se\_config](structcomp__nrf__comp__se__config.md) |
|  | Single-ended mode configuration structure. [More...](structcomp__nrf__comp__se__config.md#details) |
| struct | [comp\_nrf\_comp\_diff\_config](structcomp__nrf__comp__diff__config.md) |
|  | Differential mode configuration structure. [More...](structcomp__nrf__comp__diff__config.md#details) |

| Enumerations | |
| --- | --- |
| enum | [comp\_nrf\_comp\_psel](#a939aadd5e7172aa0b5e128c1aaf9d9bd) {     [COMP\_NRF\_COMP\_PSEL\_AIN0](#a939aadd5e7172aa0b5e128c1aaf9d9bda2b1c2decdb25c675f1e393fa8b43977e) , [COMP\_NRF\_COMP\_PSEL\_AIN1](#a939aadd5e7172aa0b5e128c1aaf9d9bdac37f4b34cae292cf99a3f93b80d407d6) , [COMP\_NRF\_COMP\_PSEL\_AIN2](#a939aadd5e7172aa0b5e128c1aaf9d9bda5e37908bf483008126c34d25edbc137b) , [COMP\_NRF\_COMP\_PSEL\_AIN3](#a939aadd5e7172aa0b5e128c1aaf9d9bda6a9e897dbcb2f651c454d22b9ca790e7) ,     [COMP\_NRF\_COMP\_PSEL\_AIN4](#a939aadd5e7172aa0b5e128c1aaf9d9bdac2a45cbf6105c6f66873193db6587ea1) , [COMP\_NRF\_COMP\_PSEL\_AIN5](#a939aadd5e7172aa0b5e128c1aaf9d9bda1432d8a42cbed9bc2db034a2a17f884a) , [COMP\_NRF\_COMP\_PSEL\_AIN6](#a939aadd5e7172aa0b5e128c1aaf9d9bda671739cd4df3ce2ed598b32e025f4f21) , [COMP\_NRF\_COMP\_PSEL\_AIN7](#a939aadd5e7172aa0b5e128c1aaf9d9bda0c790a921c22f4c62fe57bf9ac451d18) ,     [COMP\_NRF\_COMP\_PSEL\_VDD\_DIV2](#a939aadd5e7172aa0b5e128c1aaf9d9bda8c21dbfce40ed06ceb4504dc027301c4) , [COMP\_NRF\_COMP\_PSEL\_VDDH\_DIV5](#a939aadd5e7172aa0b5e128c1aaf9d9bda54b4306c4934add27acdc58d408b8ccc)   } |
|  | Positive input selection. [More...](#a939aadd5e7172aa0b5e128c1aaf9d9bd) |
| enum | [comp\_nrf\_comp\_extrefsel](#a3f3b16a44f7144021081965686af2270) {     [COMP\_NRF\_COMP\_EXTREFSEL\_AIN0](#a3f3b16a44f7144021081965686af2270af4f8c27fcace2bb5d835a2abd08b9185) , [COMP\_NRF\_COMP\_EXTREFSEL\_AIN1](#a3f3b16a44f7144021081965686af2270aa583f7d396f0f7ad248991499990a4ed) , [COMP\_NRF\_COMP\_EXTREFSEL\_AIN2](#a3f3b16a44f7144021081965686af2270ac6308f6e909ee744f9506ed560768459) , [COMP\_NRF\_COMP\_EXTREFSEL\_AIN3](#a3f3b16a44f7144021081965686af2270a2c213b044a0446bb545b37f5e21a58e1) ,     [COMP\_NRF\_COMP\_EXTREFSEL\_AIN4](#a3f3b16a44f7144021081965686af2270afc90e5b29390f758a14cdfdc656d0de1) , [COMP\_NRF\_COMP\_EXTREFSEL\_AIN5](#a3f3b16a44f7144021081965686af2270a547593f189f1a0a393b5ad85f3468743) , [COMP\_NRF\_COMP\_EXTREFSEL\_AIN6](#a3f3b16a44f7144021081965686af2270a7e7af9bf1f3ddffa54263ddb42d0cae5) , [COMP\_NRF\_COMP\_EXTREFSEL\_AIN7](#a3f3b16a44f7144021081965686af2270a215961c3f17346248d64ce9b2fccadba)   } |
|  | External reference selection. [More...](#a3f3b16a44f7144021081965686af2270) |
| enum | [comp\_nrf\_comp\_refsel](#a661d2e37c4acd5551b77e5bf2437b553) {     [COMP\_NRF\_COMP\_REFSEL\_INT\_1V2](#a661d2e37c4acd5551b77e5bf2437b553abfa40254064295fec8c5882402f7f0d2) , [COMP\_NRF\_COMP\_REFSEL\_INT\_1V8](#a661d2e37c4acd5551b77e5bf2437b553abf7088360f68099140b06de7d3f4b4e7) , [COMP\_NRF\_COMP\_REFSEL\_INT\_2V4](#a661d2e37c4acd5551b77e5bf2437b553a3670bac3f83f144ca1373a4ea6c0107c) , [COMP\_NRF\_COMP\_REFSEL\_AVDDAO1V8](#a661d2e37c4acd5551b77e5bf2437b553a87eba8036aea56146b734ee47a9cd6ca) ,     [COMP\_NRF\_COMP\_REFSEL\_VDD](#a661d2e37c4acd5551b77e5bf2437b553a0e8f3057261749e3a15333d42e49512f) , [COMP\_NRF\_COMP\_REFSEL\_AREF](#a661d2e37c4acd5551b77e5bf2437b553ab0ae8de9e72cf723645691166e9fbb2e)   } |
|  | Reference selection. [More...](#a661d2e37c4acd5551b77e5bf2437b553) |
| enum | [comp\_nrf\_comp\_sp\_mode](#ad13baf7c262d5fb2321ea5140180b3b1) { [COMP\_NRF\_COMP\_SP\_MODE\_LOW](#ad13baf7c262d5fb2321ea5140180b3b1a108433aa9b89eeca9a706e67d5eb8826) , [COMP\_NRF\_COMP\_SP\_MODE\_NORMAL](#ad13baf7c262d5fb2321ea5140180b3b1a1fb59dd0aa818e279c5e4d15b620fac5) , [COMP\_NRF\_COMP\_SP\_MODE\_HIGH](#ad13baf7c262d5fb2321ea5140180b3b1aeb3aad272a4b6cd1269180306357bd98) } |
|  | Speed mode selection. [More...](#ad13baf7c262d5fb2321ea5140180b3b1) |
| enum | [comp\_nrf\_comp\_isource](#a74444aeafb5a2bf633ffd706cc6b9010) { [COMP\_NRF\_COMP\_ISOURCE\_DISABLED](#a74444aeafb5a2bf633ffd706cc6b9010a3d47ebd769b9d4b9668d7c6502294043) , [COMP\_NRF\_COMP\_ISOURCE\_2UA5](#a74444aeafb5a2bf633ffd706cc6b9010ab413c10f12cbfb5b2e550f8fa07992c2) , [COMP\_NRF\_COMP\_ISOURCE\_5UA](#a74444aeafb5a2bf633ffd706cc6b9010a1890799d7f32b44f1a870ed67a8707a0) , [COMP\_NRF\_COMP\_ISOURCE\_10UA](#a74444aeafb5a2bf633ffd706cc6b9010a16df414be65b65763e5938bc37bb392f) } |
|  | Current source configuration. [More...](#a74444aeafb5a2bf633ffd706cc6b9010) |

| Functions | |
| --- | --- |
| int | [comp\_nrf\_comp\_configure\_se](#aca8ca4ea25fbfbe962f754ef79bcb356) (const struct [device](structdevice.md) \*dev, const struct [comp\_nrf\_comp\_se\_config](structcomp__nrf__comp__se__config.md) \*config) |
|  | Configure comparator in single-ended mode. |
| int | [comp\_nrf\_comp\_configure\_diff](#a63ca5bf56504df5c9d0904609c433e11) (const struct [device](structdevice.md) \*dev, const struct [comp\_nrf\_comp\_diff\_config](structcomp__nrf__comp__diff__config.md) \*config) |
|  | Configure comparator in differential mode. |

## Enumeration Type Documentation

## [◆ ](#a3f3b16a44f7144021081965686af2270)comp\_nrf\_comp\_extrefsel

| enum [comp\_nrf\_comp\_extrefsel](#a3f3b16a44f7144021081965686af2270) |
| --- |

External reference selection.

| Enumerator | |
| --- | --- |
| COMP\_NRF\_COMP\_EXTREFSEL\_AIN0 | AIN0 external input. |
| COMP\_NRF\_COMP\_EXTREFSEL\_AIN1 | AIN1 external input. |
| COMP\_NRF\_COMP\_EXTREFSEL\_AIN2 | AIN2 external input. |
| COMP\_NRF\_COMP\_EXTREFSEL\_AIN3 | AIN3 external input. |
| COMP\_NRF\_COMP\_EXTREFSEL\_AIN4 | AIN4 external input. |
| COMP\_NRF\_COMP\_EXTREFSEL\_AIN5 | AIN5 external input. |
| COMP\_NRF\_COMP\_EXTREFSEL\_AIN6 | AIN6 external input. |
| COMP\_NRF\_COMP\_EXTREFSEL\_AIN7 | AIN7 external input. |

## [◆ ](#a74444aeafb5a2bf633ffd706cc6b9010)comp\_nrf\_comp\_isource

| enum [comp\_nrf\_comp\_isource](#a74444aeafb5a2bf633ffd706cc6b9010) |
| --- |

Current source configuration.

| Enumerator | |
| --- | --- |
| COMP\_NRF\_COMP\_ISOURCE\_DISABLED | Current source disabled. |
| COMP\_NRF\_COMP\_ISOURCE\_2UA5 | 2.5uA current source enabled |
| COMP\_NRF\_COMP\_ISOURCE\_5UA | 5uA current source enabled |
| COMP\_NRF\_COMP\_ISOURCE\_10UA | 10uA current source enabled |

## [◆ ](#a939aadd5e7172aa0b5e128c1aaf9d9bd)comp\_nrf\_comp\_psel

| enum [comp\_nrf\_comp\_psel](#a939aadd5e7172aa0b5e128c1aaf9d9bd) |
| --- |

Positive input selection.

| Enumerator | |
| --- | --- |
| COMP\_NRF\_COMP\_PSEL\_AIN0 | AIN0 external input. |
| COMP\_NRF\_COMP\_PSEL\_AIN1 | AIN1 external input. |
| COMP\_NRF\_COMP\_PSEL\_AIN2 | AIN2 external input. |
| COMP\_NRF\_COMP\_PSEL\_AIN3 | AIN3 external input. |
| COMP\_NRF\_COMP\_PSEL\_AIN4 | AIN4 external input. |
| COMP\_NRF\_COMP\_PSEL\_AIN5 | AIN5 external input. |
| COMP\_NRF\_COMP\_PSEL\_AIN6 | AIN6 external input. |
| COMP\_NRF\_COMP\_PSEL\_AIN7 | AIN7 external input. |
| COMP\_NRF\_COMP\_PSEL\_VDD\_DIV2 | VDD / 2. |
| COMP\_NRF\_COMP\_PSEL\_VDDH\_DIV5 | VDDH / 5. |

## [◆ ](#a661d2e37c4acd5551b77e5bf2437b553)comp\_nrf\_comp\_refsel

| enum [comp\_nrf\_comp\_refsel](#a661d2e37c4acd5551b77e5bf2437b553) |
| --- |

Reference selection.

| Enumerator | |
| --- | --- |
| COMP\_NRF\_COMP\_REFSEL\_INT\_1V2 | Internal 1.2V reference. |
| COMP\_NRF\_COMP\_REFSEL\_INT\_1V8 | Internal 1.8V reference. |
| COMP\_NRF\_COMP\_REFSEL\_INT\_2V4 | Internal 2.4V reference. |
| COMP\_NRF\_COMP\_REFSEL\_AVDDAO1V8 | AVDD 1.8V reference. |
| COMP\_NRF\_COMP\_REFSEL\_VDD | VDD reference. |
| COMP\_NRF\_COMP\_REFSEL\_AREF | Use external analog reference. |

## [◆ ](#ad13baf7c262d5fb2321ea5140180b3b1)comp\_nrf\_comp\_sp\_mode

| enum [comp\_nrf\_comp\_sp\_mode](#ad13baf7c262d5fb2321ea5140180b3b1) |
| --- |

Speed mode selection.

| Enumerator | |
| --- | --- |
| COMP\_NRF\_COMP\_SP\_MODE\_LOW | Low-power mode. |
| COMP\_NRF\_COMP\_SP\_MODE\_NORMAL | Normal mode. |
| COMP\_NRF\_COMP\_SP\_MODE\_HIGH | High-speed mode. |

## Function Documentation

## [◆ ](#a63ca5bf56504df5c9d0904609c433e11)comp\_nrf\_comp\_configure\_diff()

| int comp\_nrf\_comp\_configure\_diff | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [comp\_nrf\_comp\_diff\_config](structcomp__nrf__comp__diff__config.md) \* | *config* ) |

Configure comparator in differential mode.

Parameters
:   | dev | Comparator device instance |
    | --- | --- |
    | config | Differential mode configuration |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | errno-code otherwise |

## [◆ ](#aca8ca4ea25fbfbe962f754ef79bcb356)comp\_nrf\_comp\_configure\_se()

| int comp\_nrf\_comp\_configure\_se | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [comp\_nrf\_comp\_se\_config](structcomp__nrf__comp__se__config.md) \* | *config* ) |

Configure comparator in single-ended mode.

Parameters
:   | dev | Comparator device instance |
    | --- | --- |
    | config | Single-ended mode configuration |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | errno-code otherwise |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [comparator](dir_25be445c737a80f4854b3956f06e1693.md)
- [nrf\_comp.h](nrf__comp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
