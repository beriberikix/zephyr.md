---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/arc__connect_8h.html
original_path: doxygen/html/arc__connect_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

arc\_connect.h File Reference

ARCv2 ARC Connect driver.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/arch/arc/v2/aux_regs.h](aux__regs_8h_source.md)>`

[Go to the source code of this file.](arc__connect_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [arc\_connect\_cmd](structarc__connect__cmd.md) |
| struct | [arc\_connect\_bcr](structarc__connect__bcr.md) |
| struct | [arc\_connect\_idu\_bcr](structarc__connect__idu__bcr.md) |

| Macros | |
| --- | --- |
| #define | [ARC\_CONNECT\_CMD\_CHECK\_CORE\_ID](#aa0916ff664e0555cca8d89a91a97f0af)   0x0 |
| #define | [ARC\_CONNECT\_CMD\_INTRPT\_GENERATE\_IRQ](#a60b0ff098e6b3b90844e9114b736e850)   0x1 |
| #define | [ARC\_CONNECT\_CMD\_INTRPT\_GENERATE\_ACK](#a96eb8f0b5182143b5d4e9837a28cbe96)   0x2 |
| #define | [ARC\_CONNECT\_CMD\_INTRPT\_READ\_STATUS](#af4d24daffda05ed8dff95fe6b8ebb54d)   0x3 |
| #define | [ARC\_CONNECT\_CMD\_INTRPT\_CHECK\_SOURCE](#a4385db77797902d33cdd68040b4e44d5)   0x4 |
| #define | [ARC\_CONNECT\_CMD\_SEMA\_CLAIM\_AND\_READ](#ad371fa315bc739421c302d9f5836aea0)   0x11 |
| #define | [ARC\_CONNECT\_CMD\_SEMA\_RELEASE](#aeb3a29644bb96b3ae1466c65573310a5)   0x12 |
| #define | [ARC\_CONNECT\_CMD\_SEMA\_FORCE\_RELEASE](#a98224c548cd6a21711c65a14a7e1f7ea)   0x13 |
| #define | [ARC\_CONNECT\_CMD\_MSG\_SRAM\_SET\_ADDR](#a6a0cc8aafee6d4234f461f38653ff86b)   0x21 |
| #define | [ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_ADDR](#a079317281d49d8e57f2a08ce5b396aa4)   0x22 |
| #define | [ARC\_CONNECT\_CMD\_MSG\_SRAM\_SET\_ADDR\_OFFSET](#abf3ca67becaed32adec81175a393aa25)   0x23 |
| #define | [ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_ADDR\_OFFSET](#a4a09502754de405e3ed9f1459865281c)   0x24 |
| #define | [ARC\_CONNECT\_CMD\_MSG\_SRAM\_WRITE](#a19e19e783ad81f6738e01cdaf551910a)   0x25 |
| #define | [ARC\_CONNECT\_CMD\_MSG\_SRAM\_WRITE\_INC](#ad9c105f0ec703aaccaefa51e058b8e66)   0x26 |
| #define | [ARC\_CONNECT\_CMD\_MSG\_SRAM\_WRITE\_IMM](#a7ef798f2fb76d2376233b2ac4563bda4)   0x27 |
| #define | [ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ](#a95abc6ae373160a7fdd95eeeaffbf068)   0x28 |
| #define | [ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_INC](#a1fa49a1bd5740431b7e1031ec3f4e3a5)   0x29 |
| #define | [ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_IMM](#a2291642fff8644955ed8c91dd5459f58)   0x2a |
| #define | [ARC\_CONNECT\_CMD\_MSG\_SRAM\_SET\_ECC\_CTRL](#abfa2e40196acb76717e6ac5d7d2ccea2)   0x2b |
| #define | [ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_ECC\_CTRL](#a250624ed309ab3ce6158dfd472c7e62b)   0x2c |
| #define | [ARC\_CONNECT\_CMD\_DEBUG\_RESET](#a5de7138d686356bf695c73f7991a5cd2)   0x31 |
| #define | [ARC\_CONNECT\_CMD\_DEBUG\_HALT](#a79d027948ada6f25c40858a1842a3165)   0x32 |
| #define | [ARC\_CONNECT\_CMD\_DEBUG\_RUN](#a9f9f9f414b3dda3487078154993fa4b9)   0x33 |
| #define | [ARC\_CONNECT\_CMD\_DEBUG\_SET\_MASK](#af4560d50adc746f660695b60e5a534ef)   0x34 |
| #define | [ARC\_CONNECT\_CMD\_DEBUG\_READ\_MASK](#a1e1efe68fe11446d8c54685e820f2dd0)   0x35 |
| #define | [ARC\_CONNECT\_CMD\_DEBUG\_SET\_SELECT](#a1c22504f72eccdd532d39525c3a3938e)   0x36 |
| #define | [ARC\_CONNECT\_CMD\_DEBUG\_READ\_SELECT](#ad825597a6a0948fa0e8c6d8d16169c93)   0x37 |
| #define | [ARC\_CONNECT\_CMD\_DEBUG\_READ\_EN](#a09feefc3b1b8d7f818dcdc7fe817a594)   0x38 |
| #define | [ARC\_CONNECT\_CMD\_DEBUG\_READ\_CMD](#aaf0860d01aca22d2c057418603bed930)   0x39 |
| #define | [ARC\_CONNECT\_CMD\_DEBUG\_READ\_CORE](#a2e5ddca1dfc8e24cb5cb7825e9be9ba1)   0x3a |
| #define | [ARC\_CONNECT\_CMD\_DEBUG\_MASK\_SH](#a286b79aaff7ec2eb5df86927abf2fa0f)   0x08 /\* if a self-halt occurs, a global halt is triggered \*/ |
| #define | [ARC\_CONNECT\_CMD\_DEBUG\_MASK\_BH](#af109c1e8746d8f33d170db073cc2df9e)   0x04 /\* if a breakpoint caused halt occurs, a global halt is triggered \*/ |
| #define | [ARC\_CONNECT\_CMD\_DEBUG\_MASK\_AH](#a677a6e9abbd1ff3657f17bf5f272ad9a)   0x02 /\* if an actionpoint caused halt occurs, a global halt is triggered \*/ |
| #define | [ARC\_CONNECT\_CMD\_DEBUG\_MASK\_H](#a9f2c6449b60ac3123e4ef3b98c12c4f1)   0x01 /\* whenever the core is halted, a global halt is triggered \*/ |
| #define | [ARC\_CONNECT\_CMD\_GFRC\_CLEAR](#a32332ac2356d0b7bc1f2d2f8642f8bd0)   0x41 |
| #define | [ARC\_CONNECT\_CMD\_GFRC\_READ\_LO](#aa8a28e07e540f418bf016538d42bde82)   0x42 |
| #define | [ARC\_CONNECT\_CMD\_GFRC\_READ\_HI](#a706c63576dd21a2b924911fb121782f4)   0x43 |
| #define | [ARC\_CONNECT\_CMD\_GFRC\_ENABLE](#a14c5bf6c6fbea0b73204f147411efb19)   0x44 |
| #define | [ARC\_CONNECT\_CMD\_GFRC\_DISABLE](#ab1a780f10bb9cc5718607b4e8cdbbba4)   0x45 |
| #define | [ARC\_CONNECT\_CMD\_GFRC\_READ\_DISABLE](#a886660fefc56e449dfdb1f0db3047730)   0x46 |
| #define | [ARC\_CONNECT\_CMD\_GFRC\_SET\_CORE](#a0944e99eebe084f942bdb7c22b74bfc0)   0x47 |
| #define | [ARC\_CONNECT\_CMD\_GFRC\_READ\_CORE](#a588d0b3b5272afd4164920b468e4bf31)   0x48 |
| #define | [ARC\_CONNECT\_CMD\_GFRC\_READ\_HALT](#aaf7a4f5122847621acb233e7849a6b6d)   0x49 |
| #define | [ARC\_CONNECT\_CMD\_PDM\_SET\_PM](#a497ee266769c5ca951a402895dead4a8)   0x81 |
| #define | [ARC\_CONNECT\_CMD\_PDM\_READ\_PSTATUS](#afd8a691965ed96ac3e5949f529598450)   0x82 |
| #define | [ARC\_CONNECT\_CMD\_PMU\_SET\_PUCNT](#a187e3d3614537efd81bff08788f083b9)   0x51 |
| #define | [ARC\_CONNECT\_CMD\_PMU\_READ\_PUCNT](#a1028729196bcc91e5d16341d78ad97ee)   0x52 |
| #define | [ARC\_CONNECT\_CMD\_PMU\_SET\_RSTCNT](#a0f819573b0c71f6719813ca40d181d2a)   0x53 |
| #define | [ARC\_CONNECT\_CMD\_PMU\_READ\_RSTCNT](#ae3f58528546b78730f9e48a024927913)   0x54 |
| #define | [ARC\_CONNECT\_CMD\_PMU\_SET\_PDCNT](#a756ac1596057df9ffc4a12d048a678d1)   0x55 |
| #define | [ARC\_CONNECT\_CMD\_PMU\_READ\_PDCNT](#a22c2df120423e7243719d223130ec0d3)   0x56 |
| #define | [ARC\_CONNECT\_CMD\_IDU\_ENABLE](#afcc229c691acfb72afc9ab344ff0fc07)   0x71 |
| #define | [ARC\_CONNECT\_CMD\_IDU\_DISABLE](#a22292ad920b7222e1bf3d057cee6a9c0)   0x72 |
| #define | [ARC\_CONNECT\_CMD\_IDU\_READ\_ENABLE](#a99f1e171858a67934a83ecc5f96b367d)   0x73 |
| #define | [ARC\_CONNECT\_CMD\_IDU\_SET\_MODE](#a0ac262572bd76b18d6a36c96557a8880)   0x74 |
| #define | [ARC\_CONNECT\_CMD\_IDU\_READ\_MODE](#a7a699283d26fe84104ed4d57d09657e2)   0x75 |
| #define | [ARC\_CONNECT\_CMD\_IDU\_SET\_DEST](#afb2d3ade8e16c9f302fa245c5a27b186)   0x76 |
| #define | [ARC\_CONNECT\_CMD\_IDU\_READ\_DEST](#adf49a1317a314ac6c2fc9b796f9577c8)   0x77 |
| #define | [ARC\_CONNECT\_CMD\_IDU\_GEN\_CIRQ](#a20b34806c9402e938874f0fb9cbe42d9)   0x78 |
| #define | [ARC\_CONNECT\_CMD\_IDU\_ACK\_CIRQ](#abe7202c5a016c9a94eeb6d8995eea03c)   0x79 |
| #define | [ARC\_CONNECT\_CMD\_IDU\_CHECK\_STATUS](#a4c3da41b3dec1043ad46607d945895a9)   0x7a |
| #define | [ARC\_CONNECT\_CMD\_IDU\_CHECK\_SOURCE](#a8a306828e1fef2bbf7aa30a95c2b2359)   0x7b |
| #define | [ARC\_CONNECT\_CMD\_IDU\_SET\_MASK](#a066d1063d46301167e19ae2a9011c5f8)   0x7c |
| #define | [ARC\_CONNECT\_CMD\_IDU\_READ\_MASK](#a45b6e97825dccc8b73943a9eaa2a876c)   0x7d |
| #define | [ARC\_CONNECT\_CMD\_IDU\_CHECK\_FIRST](#ae6a517147194f518687ad0ac8eb107a6)   0x7e |
| #define | [ARC\_CONNECT\_IDU\_IRQ\_START](#a4e5782d78d6200b217740c83be9ac9de)   24 |
| #define | [ARC\_CONNECT\_INTRPT\_TRIGGER\_LEVEL](#ad1978b6fef840e5f15b239d995a1d9d4)   0 |
| #define | [ARC\_CONNECT\_INTRPT\_TRIGGER\_EDGE](#a75b642dd17f8851fb7cb2109fafd7578)   1 |
| #define | [ARC\_CONNECT\_DISTRI\_MODE\_ROUND\_ROBIN](#af3566e4fd9229da92068284811608f5b)   0 |
| #define | [ARC\_CONNECT\_DISTRI\_MODE\_FIRST\_ACK](#aff9e1c8c2e14244286702d8038d4dc9b)   1 |
| #define | [ARC\_CONNECT\_DISTRI\_ALL\_DEST](#a26667f2090d8ebd9229ca02964491644)   2 |

## Detailed Description

ARCv2 ARC Connect driver.

ARCv2 ARC Connect driver interface. Included by arc/arch.h.

## Macro Definition Documentation

## [◆ ](#aa0916ff664e0555cca8d89a91a97f0af)ARC\_CONNECT\_CMD\_CHECK\_CORE\_ID

| #define ARC\_CONNECT\_CMD\_CHECK\_CORE\_ID   0x0 |
| --- |

## [◆ ](#a79d027948ada6f25c40858a1842a3165)ARC\_CONNECT\_CMD\_DEBUG\_HALT

| #define ARC\_CONNECT\_CMD\_DEBUG\_HALT   0x32 |
| --- |

## [◆ ](#a677a6e9abbd1ff3657f17bf5f272ad9a)ARC\_CONNECT\_CMD\_DEBUG\_MASK\_AH

| #define ARC\_CONNECT\_CMD\_DEBUG\_MASK\_AH   0x02 /\* if an actionpoint caused halt occurs, a global halt is triggered \*/ |
| --- |

## [◆ ](#af109c1e8746d8f33d170db073cc2df9e)ARC\_CONNECT\_CMD\_DEBUG\_MASK\_BH

| #define ARC\_CONNECT\_CMD\_DEBUG\_MASK\_BH   0x04 /\* if a breakpoint caused halt occurs, a global halt is triggered \*/ |
| --- |

## [◆ ](#a9f2c6449b60ac3123e4ef3b98c12c4f1)ARC\_CONNECT\_CMD\_DEBUG\_MASK\_H

| #define ARC\_CONNECT\_CMD\_DEBUG\_MASK\_H   0x01 /\* whenever the core is halted, a global halt is triggered \*/ |
| --- |

## [◆ ](#a286b79aaff7ec2eb5df86927abf2fa0f)ARC\_CONNECT\_CMD\_DEBUG\_MASK\_SH

| #define ARC\_CONNECT\_CMD\_DEBUG\_MASK\_SH   0x08 /\* if a self-halt occurs, a global halt is triggered \*/ |
| --- |

## [◆ ](#aaf0860d01aca22d2c057418603bed930)ARC\_CONNECT\_CMD\_DEBUG\_READ\_CMD

| #define ARC\_CONNECT\_CMD\_DEBUG\_READ\_CMD   0x39 |
| --- |

## [◆ ](#a2e5ddca1dfc8e24cb5cb7825e9be9ba1)ARC\_CONNECT\_CMD\_DEBUG\_READ\_CORE

| #define ARC\_CONNECT\_CMD\_DEBUG\_READ\_CORE   0x3a |
| --- |

## [◆ ](#a09feefc3b1b8d7f818dcdc7fe817a594)ARC\_CONNECT\_CMD\_DEBUG\_READ\_EN

| #define ARC\_CONNECT\_CMD\_DEBUG\_READ\_EN   0x38 |
| --- |

## [◆ ](#a1e1efe68fe11446d8c54685e820f2dd0)ARC\_CONNECT\_CMD\_DEBUG\_READ\_MASK

| #define ARC\_CONNECT\_CMD\_DEBUG\_READ\_MASK   0x35 |
| --- |

## [◆ ](#ad825597a6a0948fa0e8c6d8d16169c93)ARC\_CONNECT\_CMD\_DEBUG\_READ\_SELECT

| #define ARC\_CONNECT\_CMD\_DEBUG\_READ\_SELECT   0x37 |
| --- |

## [◆ ](#a5de7138d686356bf695c73f7991a5cd2)ARC\_CONNECT\_CMD\_DEBUG\_RESET

| #define ARC\_CONNECT\_CMD\_DEBUG\_RESET   0x31 |
| --- |

## [◆ ](#a9f9f9f414b3dda3487078154993fa4b9)ARC\_CONNECT\_CMD\_DEBUG\_RUN

| #define ARC\_CONNECT\_CMD\_DEBUG\_RUN   0x33 |
| --- |

## [◆ ](#af4560d50adc746f660695b60e5a534ef)ARC\_CONNECT\_CMD\_DEBUG\_SET\_MASK

| #define ARC\_CONNECT\_CMD\_DEBUG\_SET\_MASK   0x34 |
| --- |

## [◆ ](#a1c22504f72eccdd532d39525c3a3938e)ARC\_CONNECT\_CMD\_DEBUG\_SET\_SELECT

| #define ARC\_CONNECT\_CMD\_DEBUG\_SET\_SELECT   0x36 |
| --- |

## [◆ ](#a32332ac2356d0b7bc1f2d2f8642f8bd0)ARC\_CONNECT\_CMD\_GFRC\_CLEAR

| #define ARC\_CONNECT\_CMD\_GFRC\_CLEAR   0x41 |
| --- |

## [◆ ](#ab1a780f10bb9cc5718607b4e8cdbbba4)ARC\_CONNECT\_CMD\_GFRC\_DISABLE

| #define ARC\_CONNECT\_CMD\_GFRC\_DISABLE   0x45 |
| --- |

## [◆ ](#a14c5bf6c6fbea0b73204f147411efb19)ARC\_CONNECT\_CMD\_GFRC\_ENABLE

| #define ARC\_CONNECT\_CMD\_GFRC\_ENABLE   0x44 |
| --- |

## [◆ ](#a588d0b3b5272afd4164920b468e4bf31)ARC\_CONNECT\_CMD\_GFRC\_READ\_CORE

| #define ARC\_CONNECT\_CMD\_GFRC\_READ\_CORE   0x48 |
| --- |

## [◆ ](#a886660fefc56e449dfdb1f0db3047730)ARC\_CONNECT\_CMD\_GFRC\_READ\_DISABLE

| #define ARC\_CONNECT\_CMD\_GFRC\_READ\_DISABLE   0x46 |
| --- |

## [◆ ](#aaf7a4f5122847621acb233e7849a6b6d)ARC\_CONNECT\_CMD\_GFRC\_READ\_HALT

| #define ARC\_CONNECT\_CMD\_GFRC\_READ\_HALT   0x49 |
| --- |

## [◆ ](#a706c63576dd21a2b924911fb121782f4)ARC\_CONNECT\_CMD\_GFRC\_READ\_HI

| #define ARC\_CONNECT\_CMD\_GFRC\_READ\_HI   0x43 |
| --- |

## [◆ ](#aa8a28e07e540f418bf016538d42bde82)ARC\_CONNECT\_CMD\_GFRC\_READ\_LO

| #define ARC\_CONNECT\_CMD\_GFRC\_READ\_LO   0x42 |
| --- |

## [◆ ](#a0944e99eebe084f942bdb7c22b74bfc0)ARC\_CONNECT\_CMD\_GFRC\_SET\_CORE

| #define ARC\_CONNECT\_CMD\_GFRC\_SET\_CORE   0x47 |
| --- |

## [◆ ](#abe7202c5a016c9a94eeb6d8995eea03c)ARC\_CONNECT\_CMD\_IDU\_ACK\_CIRQ

| #define ARC\_CONNECT\_CMD\_IDU\_ACK\_CIRQ   0x79 |
| --- |

## [◆ ](#ae6a517147194f518687ad0ac8eb107a6)ARC\_CONNECT\_CMD\_IDU\_CHECK\_FIRST

| #define ARC\_CONNECT\_CMD\_IDU\_CHECK\_FIRST   0x7e |
| --- |

## [◆ ](#a8a306828e1fef2bbf7aa30a95c2b2359)ARC\_CONNECT\_CMD\_IDU\_CHECK\_SOURCE

| #define ARC\_CONNECT\_CMD\_IDU\_CHECK\_SOURCE   0x7b |
| --- |

## [◆ ](#a4c3da41b3dec1043ad46607d945895a9)ARC\_CONNECT\_CMD\_IDU\_CHECK\_STATUS

| #define ARC\_CONNECT\_CMD\_IDU\_CHECK\_STATUS   0x7a |
| --- |

## [◆ ](#a22292ad920b7222e1bf3d057cee6a9c0)ARC\_CONNECT\_CMD\_IDU\_DISABLE

| #define ARC\_CONNECT\_CMD\_IDU\_DISABLE   0x72 |
| --- |

## [◆ ](#afcc229c691acfb72afc9ab344ff0fc07)ARC\_CONNECT\_CMD\_IDU\_ENABLE

| #define ARC\_CONNECT\_CMD\_IDU\_ENABLE   0x71 |
| --- |

## [◆ ](#a20b34806c9402e938874f0fb9cbe42d9)ARC\_CONNECT\_CMD\_IDU\_GEN\_CIRQ

| #define ARC\_CONNECT\_CMD\_IDU\_GEN\_CIRQ   0x78 |
| --- |

## [◆ ](#adf49a1317a314ac6c2fc9b796f9577c8)ARC\_CONNECT\_CMD\_IDU\_READ\_DEST

| #define ARC\_CONNECT\_CMD\_IDU\_READ\_DEST   0x77 |
| --- |

## [◆ ](#a99f1e171858a67934a83ecc5f96b367d)ARC\_CONNECT\_CMD\_IDU\_READ\_ENABLE

| #define ARC\_CONNECT\_CMD\_IDU\_READ\_ENABLE   0x73 |
| --- |

## [◆ ](#a45b6e97825dccc8b73943a9eaa2a876c)ARC\_CONNECT\_CMD\_IDU\_READ\_MASK

| #define ARC\_CONNECT\_CMD\_IDU\_READ\_MASK   0x7d |
| --- |

## [◆ ](#a7a699283d26fe84104ed4d57d09657e2)ARC\_CONNECT\_CMD\_IDU\_READ\_MODE

| #define ARC\_CONNECT\_CMD\_IDU\_READ\_MODE   0x75 |
| --- |

## [◆ ](#afb2d3ade8e16c9f302fa245c5a27b186)ARC\_CONNECT\_CMD\_IDU\_SET\_DEST

| #define ARC\_CONNECT\_CMD\_IDU\_SET\_DEST   0x76 |
| --- |

## [◆ ](#a066d1063d46301167e19ae2a9011c5f8)ARC\_CONNECT\_CMD\_IDU\_SET\_MASK

| #define ARC\_CONNECT\_CMD\_IDU\_SET\_MASK   0x7c |
| --- |

## [◆ ](#a0ac262572bd76b18d6a36c96557a8880)ARC\_CONNECT\_CMD\_IDU\_SET\_MODE

| #define ARC\_CONNECT\_CMD\_IDU\_SET\_MODE   0x74 |
| --- |

## [◆ ](#a4385db77797902d33cdd68040b4e44d5)ARC\_CONNECT\_CMD\_INTRPT\_CHECK\_SOURCE

| #define ARC\_CONNECT\_CMD\_INTRPT\_CHECK\_SOURCE   0x4 |
| --- |

## [◆ ](#a96eb8f0b5182143b5d4e9837a28cbe96)ARC\_CONNECT\_CMD\_INTRPT\_GENERATE\_ACK

| #define ARC\_CONNECT\_CMD\_INTRPT\_GENERATE\_ACK   0x2 |
| --- |

## [◆ ](#a60b0ff098e6b3b90844e9114b736e850)ARC\_CONNECT\_CMD\_INTRPT\_GENERATE\_IRQ

| #define ARC\_CONNECT\_CMD\_INTRPT\_GENERATE\_IRQ   0x1 |
| --- |

## [◆ ](#af4d24daffda05ed8dff95fe6b8ebb54d)ARC\_CONNECT\_CMD\_INTRPT\_READ\_STATUS

| #define ARC\_CONNECT\_CMD\_INTRPT\_READ\_STATUS   0x3 |
| --- |

## [◆ ](#a95abc6ae373160a7fdd95eeeaffbf068)ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ

| #define ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ   0x28 |
| --- |

## [◆ ](#a079317281d49d8e57f2a08ce5b396aa4)ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_ADDR

| #define ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_ADDR   0x22 |
| --- |

## [◆ ](#a4a09502754de405e3ed9f1459865281c)ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_ADDR\_OFFSET

| #define ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_ADDR\_OFFSET   0x24 |
| --- |

## [◆ ](#a250624ed309ab3ce6158dfd472c7e62b)ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_ECC\_CTRL

| #define ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_ECC\_CTRL   0x2c |
| --- |

## [◆ ](#a2291642fff8644955ed8c91dd5459f58)ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_IMM

| #define ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_IMM   0x2a |
| --- |

## [◆ ](#a1fa49a1bd5740431b7e1031ec3f4e3a5)ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_INC

| #define ARC\_CONNECT\_CMD\_MSG\_SRAM\_READ\_INC   0x29 |
| --- |

## [◆ ](#a6a0cc8aafee6d4234f461f38653ff86b)ARC\_CONNECT\_CMD\_MSG\_SRAM\_SET\_ADDR

| #define ARC\_CONNECT\_CMD\_MSG\_SRAM\_SET\_ADDR   0x21 |
| --- |

## [◆ ](#abf3ca67becaed32adec81175a393aa25)ARC\_CONNECT\_CMD\_MSG\_SRAM\_SET\_ADDR\_OFFSET

| #define ARC\_CONNECT\_CMD\_MSG\_SRAM\_SET\_ADDR\_OFFSET   0x23 |
| --- |

## [◆ ](#abfa2e40196acb76717e6ac5d7d2ccea2)ARC\_CONNECT\_CMD\_MSG\_SRAM\_SET\_ECC\_CTRL

| #define ARC\_CONNECT\_CMD\_MSG\_SRAM\_SET\_ECC\_CTRL   0x2b |
| --- |

## [◆ ](#a19e19e783ad81f6738e01cdaf551910a)ARC\_CONNECT\_CMD\_MSG\_SRAM\_WRITE

| #define ARC\_CONNECT\_CMD\_MSG\_SRAM\_WRITE   0x25 |
| --- |

## [◆ ](#a7ef798f2fb76d2376233b2ac4563bda4)ARC\_CONNECT\_CMD\_MSG\_SRAM\_WRITE\_IMM

| #define ARC\_CONNECT\_CMD\_MSG\_SRAM\_WRITE\_IMM   0x27 |
| --- |

## [◆ ](#ad9c105f0ec703aaccaefa51e058b8e66)ARC\_CONNECT\_CMD\_MSG\_SRAM\_WRITE\_INC

| #define ARC\_CONNECT\_CMD\_MSG\_SRAM\_WRITE\_INC   0x26 |
| --- |

## [◆ ](#afd8a691965ed96ac3e5949f529598450)ARC\_CONNECT\_CMD\_PDM\_READ\_PSTATUS

| #define ARC\_CONNECT\_CMD\_PDM\_READ\_PSTATUS   0x82 |
| --- |

## [◆ ](#a497ee266769c5ca951a402895dead4a8)ARC\_CONNECT\_CMD\_PDM\_SET\_PM

| #define ARC\_CONNECT\_CMD\_PDM\_SET\_PM   0x81 |
| --- |

## [◆ ](#a22c2df120423e7243719d223130ec0d3)ARC\_CONNECT\_CMD\_PMU\_READ\_PDCNT

| #define ARC\_CONNECT\_CMD\_PMU\_READ\_PDCNT   0x56 |
| --- |

## [◆ ](#a1028729196bcc91e5d16341d78ad97ee)ARC\_CONNECT\_CMD\_PMU\_READ\_PUCNT

| #define ARC\_CONNECT\_CMD\_PMU\_READ\_PUCNT   0x52 |
| --- |

## [◆ ](#ae3f58528546b78730f9e48a024927913)ARC\_CONNECT\_CMD\_PMU\_READ\_RSTCNT

| #define ARC\_CONNECT\_CMD\_PMU\_READ\_RSTCNT   0x54 |
| --- |

## [◆ ](#a756ac1596057df9ffc4a12d048a678d1)ARC\_CONNECT\_CMD\_PMU\_SET\_PDCNT

| #define ARC\_CONNECT\_CMD\_PMU\_SET\_PDCNT   0x55 |
| --- |

## [◆ ](#a187e3d3614537efd81bff08788f083b9)ARC\_CONNECT\_CMD\_PMU\_SET\_PUCNT

| #define ARC\_CONNECT\_CMD\_PMU\_SET\_PUCNT   0x51 |
| --- |

## [◆ ](#a0f819573b0c71f6719813ca40d181d2a)ARC\_CONNECT\_CMD\_PMU\_SET\_RSTCNT

| #define ARC\_CONNECT\_CMD\_PMU\_SET\_RSTCNT   0x53 |
| --- |

## [◆ ](#ad371fa315bc739421c302d9f5836aea0)ARC\_CONNECT\_CMD\_SEMA\_CLAIM\_AND\_READ

| #define ARC\_CONNECT\_CMD\_SEMA\_CLAIM\_AND\_READ   0x11 |
| --- |

## [◆ ](#a98224c548cd6a21711c65a14a7e1f7ea)ARC\_CONNECT\_CMD\_SEMA\_FORCE\_RELEASE

| #define ARC\_CONNECT\_CMD\_SEMA\_FORCE\_RELEASE   0x13 |
| --- |

## [◆ ](#aeb3a29644bb96b3ae1466c65573310a5)ARC\_CONNECT\_CMD\_SEMA\_RELEASE

| #define ARC\_CONNECT\_CMD\_SEMA\_RELEASE   0x12 |
| --- |

## [◆ ](#a26667f2090d8ebd9229ca02964491644)ARC\_CONNECT\_DISTRI\_ALL\_DEST

| #define ARC\_CONNECT\_DISTRI\_ALL\_DEST   2 |
| --- |

## [◆ ](#aff9e1c8c2e14244286702d8038d4dc9b)ARC\_CONNECT\_DISTRI\_MODE\_FIRST\_ACK

| #define ARC\_CONNECT\_DISTRI\_MODE\_FIRST\_ACK   1 |
| --- |

## [◆ ](#af3566e4fd9229da92068284811608f5b)ARC\_CONNECT\_DISTRI\_MODE\_ROUND\_ROBIN

| #define ARC\_CONNECT\_DISTRI\_MODE\_ROUND\_ROBIN   0 |
| --- |

## [◆ ](#a4e5782d78d6200b217740c83be9ac9de)ARC\_CONNECT\_IDU\_IRQ\_START

| #define ARC\_CONNECT\_IDU\_IRQ\_START   24 |
| --- |

## [◆ ](#a75b642dd17f8851fb7cb2109fafd7578)ARC\_CONNECT\_INTRPT\_TRIGGER\_EDGE

| #define ARC\_CONNECT\_INTRPT\_TRIGGER\_EDGE   1 |
| --- |

## [◆ ](#ad1978b6fef840e5f15b239d995a1d9d4)ARC\_CONNECT\_INTRPT\_TRIGGER\_LEVEL

| #define ARC\_CONNECT\_INTRPT\_TRIGGER\_LEVEL   0 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arc](dir_f98dedd53b120205ea2191b01dc1bb98.md)
- [v2](dir_3e6dec649f819729d9137b059e4fc1a1.md)
- [arc\_connect.h](arc__connect_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
