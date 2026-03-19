---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__ethernet__mii.html
original_path: doxygen/html/group__ethernet__mii.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Ethernet MII Support Functions

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Ethernet Support Functions](group__ethernet.md)

Ethernet MII (media independent interface) functions.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [MII\_BMCR](#ga9137acedc42ff140f244da7473cff29e)   0x0 |
|  | Basic Mode Control Register. |
| #define | [MII\_BMSR](#gaa2f632686d6298a7c898b1c805586aab)   0x1 |
|  | Basic Mode Status Register. |
| #define | [MII\_PHYID1R](#ga87196e916598cea91b6ce400ad0cc34a)   0x2 |
|  | PHY ID 1 Register. |
| #define | [MII\_PHYID2R](#ga40766cdb8f9c3ffee64720f0f0ea2f15)   0x3 |
|  | PHY ID 2 Register. |
| #define | [MII\_ANAR](#gaacb2ab0ea5579b5d9e30b075991add1d)   0x4 |
|  | Auto-Negotiation Advertisement Register. |
| #define | [MII\_ANLPAR](#ga445e8381a9ea9724054bfacc10bb4c81)   0x5 |
|  | Auto-Negotiation Link Partner Ability Reg. |
| #define | [MII\_ANER](#ga6e5634d8831e21f963ddc16b91d5f6b9)   0x6 |
|  | Auto-Negotiation Expansion Register. |
| #define | [MII\_ANNPTR](#ga3f3ed3ecfd22b34b840ff2473ca68490)   0x7 |
|  | Auto-Negotiation Next Page Transmit Register. |
| #define | [MII\_ANLPRNPR](#gaf17d80457d4a609d16793870d4a76bdf)   0x8 |
|  | Auto-Negotiation Link Partner Received Next Page Reg. |
| #define | [MII\_1KTCR](#ga9e258e8e518579ac5f9a8809ddc6aedb)   0x9 |
|  | 1000BASE-T Control Register |
| #define | [MII\_1KSTSR](#ga49a74b346b13cc80c159c0f8f6b9c0f0)   0xa |
|  | 1000BASE-T Status Register |
| #define | [MII\_MMD\_ACR](#ga7d6687385994aac21782308af560b224)   0xd |
|  | MMD Access Control Register. |
| #define | [MII\_MMD\_AADR](#ga378832f55be1a03977c829f09dd1d364)   0xe |
|  | MMD Access Address Data Register. |
| #define | [MII\_ESTAT](#gaa705f43dba50029d5395379e1f2b802d)   0xf |
|  | Extended Status Register. |
| #define | [MII\_BMCR\_RESET](#ga1001ac1540dc5bb6c4962f63b5fd6c3a)   (1 << 15) |
|  | PHY reset. |
| #define | [MII\_BMCR\_LOOPBACK](#gaaade3d675167c736186a03dad857a7c9)   (1 << 14) |
|  | enable loopback mode |
| #define | [MII\_BMCR\_SPEED\_LSB](#ga19ef6d51e7bc231892635d856dd6a747)   (1 << 13) |
|  | 10=1000Mbps 01=100Mbps; 00=10Mbps |
| #define | [MII\_BMCR\_AUTONEG\_ENABLE](#gaf58b450219ae18dfa2526c685a0402a7)   (1 << 12) |
|  | Auto-Negotiation enable. |
| #define | [MII\_BMCR\_POWER\_DOWN](#ga2598b7655be14619dffc44b9a6db36b8)   (1 << 11) |
|  | power down mode |
| #define | [MII\_BMCR\_ISOLATE](#ga288b983fab32fb073cc42c3817b2c217)   (1 << 10) |
|  | isolate electrically PHY from MII |
| #define | [MII\_BMCR\_AUTONEG\_RESTART](#ga110d6e1bfdbb37aa95cf1b32c54d8fa0)   (1 << 9) |
|  | restart auto-negotiation |
| #define | [MII\_BMCR\_DUPLEX\_MODE](#ga288bc52d6545ec634e6c2da04dbe86d3)   (1 << 8) |
|  | full duplex mode |
| #define | [MII\_BMCR\_SPEED\_MSB](#ga94e2ff6468b89371ec22a087ad5477d4)   (1 << 6) |
|  | 10=1000Mbps 01=100Mbps; 00=10Mbps |
| #define | [MII\_BMCR\_SPEED\_MASK](#gaf562ae173424ea0d41afd68d11f87115)   (1 << 6 | 1 << 13) |
|  | Link Speed Field. |
| #define | [MII\_BMCR\_SPEED\_10](#ga4d31aeaad35fe6a358aef1eef1c5b4cf)   (0 << 6 | 0 << 13) |
|  | select speed 10 Mb/s |
| #define | [MII\_BMCR\_SPEED\_100](#gaf52c7fc2b468c142ae63605a201900d4)   (0 << 6 | 1 << 13) |
|  | select speed 100 Mb/s |
| #define | [MII\_BMCR\_SPEED\_1000](#gaae2f486072b95b3e829d0e1bd4b8d893)   (1 << 6 | 0 << 13) |
|  | select speed 1000 Mb/s |
| #define | [MII\_BMSR\_100BASE\_T4](#gac8a404aa082745cb7699739bf58fc530)   (1 << 15) |
|  | 100BASE-T4 capable |
| #define | [MII\_BMSR\_100BASE\_X\_FULL](#ga090c828a41acfc824b56ec2a9a57082a)   (1 << 14) |
|  | 100BASE-X full duplex capable |
| #define | [MII\_BMSR\_100BASE\_X\_HALF](#ga608ec5361c44f25c34ae6138ae7ffef9)   (1 << 13) |
|  | 100BASE-X half duplex capable |
| #define | [MII\_BMSR\_10\_FULL](#ga4f085921a6b0f0586326b1bdc8f62b31)   (1 << 12) |
|  | 10 Mb/s full duplex capable |
| #define | [MII\_BMSR\_10\_HALF](#ga8505886511fef3ec2d8630a957de4478)   (1 << 11) |
|  | 10 Mb/s half duplex capable |
| #define | [MII\_BMSR\_100BASE\_T2\_FULL](#ga93fb7b79b3da2ae1757fe98237dd2d6b)   (1 << 10) |
|  | 100BASE-T2 full duplex capable |
| #define | [MII\_BMSR\_100BASE\_T2\_HALF](#gafb0d83d336eda611d45580be48f15d02)   (1 << 9) |
|  | 100BASE-T2 half duplex capable |
| #define | [MII\_BMSR\_EXTEND\_STATUS](#ga24992988cde973ce2a954fe372a5ad0e)   (1 << 8) |
|  | extend status information in reg 15 |
| #define | [MII\_BMSR\_MF\_PREAMB\_SUPPR](#gae85e29e0f9a50898f93ff6e5a5f763e4)   (1 << 6) |
|  | PHY accepts management frames with preamble suppressed. |
| #define | [MII\_BMSR\_AUTONEG\_COMPLETE](#gac5b9ac6b54ce146c91197660c2ccd207)   (1 << 5) |
|  | Auto-negotiation process completed. |
| #define | [MII\_BMSR\_REMOTE\_FAULT](#ga0dd8421740c52ecd5e6a53e969d2e48a)   (1 << 4) |
|  | remote fault detected |
| #define | [MII\_BMSR\_AUTONEG\_ABILITY](#gafc344357c76d6a41c5fa432d55355fce)   (1 << 3) |
|  | PHY is able to perform Auto-Negotiation. |
| #define | [MII\_BMSR\_LINK\_STATUS](#ga884d39c456206cee38ce5a9a9ca01599)   (1 << 2) |
|  | link is up |
| #define | [MII\_BMSR\_JABBER\_DETECT](#gad9ef4a2223dfee6826b0fdc8b25802ea)   (1 << 1) |
|  | jabber condition detected |
| #define | [MII\_BMSR\_EXTEND\_CAPAB](#gab225377deb09eb179b7efee199c7edd4)   (1 << 0) |
|  | extended register capabilities |
| #define | [MII\_ADVERTISE\_NEXT\_PAGE](#ga4e567fc428a19d55c13c6be38091ed59)   (1 << 15) |
|  | next page |
| #define | [MII\_ADVERTISE\_LPACK](#gaca8ed07be80166e8abaefb4135008989)   (1 << 14) |
|  | link partner acknowledge response |
| #define | [MII\_ADVERTISE\_REMOTE\_FAULT](#ga3e1cfef9ac347b86324d25c1d00a07ef)   (1 << 13) |
|  | remote fault |
| #define | [MII\_ADVERTISE\_ASYM\_PAUSE](#gaf8b5e7fc3226b89b875f46a50165e332)   (1 << 11) |
|  | try for asymmetric pause |
| #define | [MII\_ADVERTISE\_PAUSE](#ga7b3dfbe50b37378cbf45d15f9ef88c7f)   (1 << 10) |
|  | try for pause |
| #define | [MII\_ADVERTISE\_100BASE\_T4](#ga11a26530d734fb68be5538ac36019821)   (1 << 9) |
|  | try for 100BASE-T4 support |
| #define | [MII\_ADVERTISE\_100\_FULL](#ga72f632c88cf6c472b893c326d7a8d263)   (1 << 8) |
|  | try for 100BASE-X full duplex support |
| #define | [MII\_ADVERTISE\_100\_HALF](#ga357539fe99d327cae0e76acd5059876f)   (1 << 7) |
|  | try for 100BASE-X support |
| #define | [MII\_ADVERTISE\_10\_FULL](#ga44ee311ef785619a215de80fc0286a4c)   (1 << 6) |
|  | try for 10 Mb/s full duplex support |
| #define | [MII\_ADVERTISE\_10\_HALF](#gac5c508943ce4006fa2f934c25436fdb5)   (1 << 5) |
|  | try for 10 Mb/s half duplex support |
| #define | [MII\_ADVERTISE\_SEL\_MASK](#gac01baecf625bbb6d55a14ac0c2b181bd)   (0x1F << 0) |
|  | Selector Field Mask. |
| #define | [MII\_ADVERTISE\_SEL\_IEEE\_802\_3](#ga9abdfc8110120f54612c712d86cab3ac)   0x01 |
|  | Selector Field. |
| #define | [MII\_ADVERTISE\_1000\_FULL](#ga028ddaf632ced31e57249883c90ed921)   (1 << 9) |
|  | try for 1000BASE-T full duplex support |
| #define | [MII\_ADVERTISE\_1000\_HALF](#ga5f36d375690560688185d1207687611b)   (1 << 8) |
|  | try for 1000BASE-T half duplex support |
| #define | [MII\_ADVERTISE\_ALL](#gacac6f915a8d0e3f8244c571646b3fc92) |
|  | Advertise all speeds. |
| #define | [MII\_ESTAT\_1000BASE\_X\_FULL](#ga846525a526aa9704a175c84771e48290)   (1 << 15) |
|  | 1000BASE-X full-duplex capable |
| #define | [MII\_ESTAT\_1000BASE\_X\_HALF](#gabec9696aa599caca1131f869827bbc95)   (1 << 14) |
|  | 1000BASE-X half-duplex capable |
| #define | [MII\_ESTAT\_1000BASE\_T\_FULL](#gada0831dbbb86ff717b40c23c73345731)   (1 << 13) |
|  | 1000BASE-T full-duplex capable |
| #define | [MII\_ESTAT\_1000BASE\_T\_HALF](#ga42e8d732fd9806e218599871fd1291d5)   (1 << 12) |
|  | 1000BASE-T half-duplex capable |
| #define | [MII\_MMD\_ACR\_DEVAD\_MASK](#gae4ac896c90a75cdc4869797708823673)   (0x1F << 0) |
|  | DEVAD Mask. |
| #define | [MII\_MMD\_ACR\_ADDR](#ga0f312eab9b4d51af4a72f7cb3898754a)   (0x00 << 14) |
|  | Address Data bits. |
| #define | [MII\_MMD\_ACR\_DATA\_NO\_POS\_INC](#ga6cac36daf5db44274cd60a05b77819f4)   (0x01 << 14) |
| #define | [MII\_MMD\_ACR\_DATA\_RW\_POS\_INC](#ga3be4dced4eec405c42467ba51c5efb9c)   (0x10 << 14) |
| #define | [MII\_MMD\_ACR\_DATA\_W\_POS\_INC](#ga48f56892c3e8d6ec7e90a7e36dd67309)   (0x11 << 14) |

## Detailed Description

Ethernet MII (media independent interface) functions.

Since
:   1.7

Version
:   0.8.0

## Macro Definition Documentation

## [◆ ](#ga49a74b346b13cc80c159c0f8f6b9c0f0)MII\_1KSTSR

| #define MII\_1KSTSR   0xa |
| --- |

`#include <[mii.h](mii_8h.md)>`

1000BASE-T Status Register

## [◆ ](#ga9e258e8e518579ac5f9a8809ddc6aedb)MII\_1KTCR

| #define MII\_1KTCR   0x9 |
| --- |

`#include <[mii.h](mii_8h.md)>`

1000BASE-T Control Register

## [◆ ](#ga028ddaf632ced31e57249883c90ed921)MII\_ADVERTISE\_1000\_FULL

| #define MII\_ADVERTISE\_1000\_FULL   (1 << 9) |
| --- |

`#include <[mii.h](mii_8h.md)>`

try for 1000BASE-T full duplex support

## [◆ ](#ga5f36d375690560688185d1207687611b)MII\_ADVERTISE\_1000\_HALF

| #define MII\_ADVERTISE\_1000\_HALF   (1 << 8) |
| --- |

`#include <[mii.h](mii_8h.md)>`

try for 1000BASE-T half duplex support

## [◆ ](#ga72f632c88cf6c472b893c326d7a8d263)MII\_ADVERTISE\_100\_FULL

| #define MII\_ADVERTISE\_100\_FULL   (1 << 8) |
| --- |

`#include <[mii.h](mii_8h.md)>`

try for 100BASE-X full duplex support

## [◆ ](#ga357539fe99d327cae0e76acd5059876f)MII\_ADVERTISE\_100\_HALF

| #define MII\_ADVERTISE\_100\_HALF   (1 << 7) |
| --- |

`#include <[mii.h](mii_8h.md)>`

try for 100BASE-X support

## [◆ ](#ga11a26530d734fb68be5538ac36019821)MII\_ADVERTISE\_100BASE\_T4

| #define MII\_ADVERTISE\_100BASE\_T4   (1 << 9) |
| --- |

`#include <[mii.h](mii_8h.md)>`

try for 100BASE-T4 support

## [◆ ](#ga44ee311ef785619a215de80fc0286a4c)MII\_ADVERTISE\_10\_FULL

| #define MII\_ADVERTISE\_10\_FULL   (1 << 6) |
| --- |

`#include <[mii.h](mii_8h.md)>`

try for 10 Mb/s full duplex support

## [◆ ](#gac5c508943ce4006fa2f934c25436fdb5)MII\_ADVERTISE\_10\_HALF

| #define MII\_ADVERTISE\_10\_HALF   (1 << 5) |
| --- |

`#include <[mii.h](mii_8h.md)>`

try for 10 Mb/s half duplex support

## [◆ ](#gacac6f915a8d0e3f8244c571646b3fc92)MII\_ADVERTISE\_ALL

| #define MII\_ADVERTISE\_ALL |
| --- |

`#include <[mii.h](mii_8h.md)>`

**Value:**

([MII\_ADVERTISE\_10\_HALF](#gac5c508943ce4006fa2f934c25436fdb5) | [MII\_ADVERTISE\_10\_FULL](#ga44ee311ef785619a215de80fc0286a4c) |\

[MII\_ADVERTISE\_100\_HALF](#ga357539fe99d327cae0e76acd5059876f) | [MII\_ADVERTISE\_100\_FULL](#ga72f632c88cf6c472b893c326d7a8d263) |\

[MII\_ADVERTISE\_SEL\_IEEE\_802\_3](#ga9abdfc8110120f54612c712d86cab3ac))

[MII\_ADVERTISE\_100\_HALF](#ga357539fe99d327cae0e76acd5059876f)

#define MII\_ADVERTISE\_100\_HALF

try for 100BASE-X support

**Definition** mii.h:131

[MII\_ADVERTISE\_10\_FULL](#ga44ee311ef785619a215de80fc0286a4c)

#define MII\_ADVERTISE\_10\_FULL

try for 10 Mb/s full duplex support

**Definition** mii.h:133

[MII\_ADVERTISE\_100\_FULL](#ga72f632c88cf6c472b893c326d7a8d263)

#define MII\_ADVERTISE\_100\_FULL

try for 100BASE-X full duplex support

**Definition** mii.h:129

[MII\_ADVERTISE\_SEL\_IEEE\_802\_3](#ga9abdfc8110120f54612c712d86cab3ac)

#define MII\_ADVERTISE\_SEL\_IEEE\_802\_3

Selector Field.

**Definition** mii.h:139

[MII\_ADVERTISE\_10\_HALF](#gac5c508943ce4006fa2f934c25436fdb5)

#define MII\_ADVERTISE\_10\_HALF

try for 10 Mb/s half duplex support

**Definition** mii.h:135

Advertise all speeds.

## [◆ ](#gaf8b5e7fc3226b89b875f46a50165e332)MII\_ADVERTISE\_ASYM\_PAUSE

| #define MII\_ADVERTISE\_ASYM\_PAUSE   (1 << 11) |
| --- |

`#include <[mii.h](mii_8h.md)>`

try for asymmetric pause

## [◆ ](#gaca8ed07be80166e8abaefb4135008989)MII\_ADVERTISE\_LPACK

| #define MII\_ADVERTISE\_LPACK   (1 << 14) |
| --- |

`#include <[mii.h](mii_8h.md)>`

link partner acknowledge response

## [◆ ](#ga4e567fc428a19d55c13c6be38091ed59)MII\_ADVERTISE\_NEXT\_PAGE

| #define MII\_ADVERTISE\_NEXT\_PAGE   (1 << 15) |
| --- |

`#include <[mii.h](mii_8h.md)>`

next page

## [◆ ](#ga7b3dfbe50b37378cbf45d15f9ef88c7f)MII\_ADVERTISE\_PAUSE

| #define MII\_ADVERTISE\_PAUSE   (1 << 10) |
| --- |

`#include <[mii.h](mii_8h.md)>`

try for pause

## [◆ ](#ga3e1cfef9ac347b86324d25c1d00a07ef)MII\_ADVERTISE\_REMOTE\_FAULT

| #define MII\_ADVERTISE\_REMOTE\_FAULT   (1 << 13) |
| --- |

`#include <[mii.h](mii_8h.md)>`

remote fault

## [◆ ](#ga9abdfc8110120f54612c712d86cab3ac)MII\_ADVERTISE\_SEL\_IEEE\_802\_3

| #define MII\_ADVERTISE\_SEL\_IEEE\_802\_3   0x01 |
| --- |

`#include <[mii.h](mii_8h.md)>`

Selector Field.

## [◆ ](#gac01baecf625bbb6d55a14ac0c2b181bd)MII\_ADVERTISE\_SEL\_MASK

| #define MII\_ADVERTISE\_SEL\_MASK   (0x1F << 0) |
| --- |

`#include <[mii.h](mii_8h.md)>`

Selector Field Mask.

## [◆ ](#gaacb2ab0ea5579b5d9e30b075991add1d)MII\_ANAR

| #define MII\_ANAR   0x4 |
| --- |

`#include <[mii.h](mii_8h.md)>`

Auto-Negotiation Advertisement Register.

## [◆ ](#ga6e5634d8831e21f963ddc16b91d5f6b9)MII\_ANER

| #define MII\_ANER   0x6 |
| --- |

`#include <[mii.h](mii_8h.md)>`

Auto-Negotiation Expansion Register.

## [◆ ](#ga445e8381a9ea9724054bfacc10bb4c81)MII\_ANLPAR

| #define MII\_ANLPAR   0x5 |
| --- |

`#include <[mii.h](mii_8h.md)>`

Auto-Negotiation Link Partner Ability Reg.

## [◆ ](#gaf17d80457d4a609d16793870d4a76bdf)MII\_ANLPRNPR

| #define MII\_ANLPRNPR   0x8 |
| --- |

`#include <[mii.h](mii_8h.md)>`

Auto-Negotiation Link Partner Received Next Page Reg.

## [◆ ](#ga3f3ed3ecfd22b34b840ff2473ca68490)MII\_ANNPTR

| #define MII\_ANNPTR   0x7 |
| --- |

`#include <[mii.h](mii_8h.md)>`

Auto-Negotiation Next Page Transmit Register.

## [◆ ](#ga9137acedc42ff140f244da7473cff29e)MII\_BMCR

| #define MII\_BMCR   0x0 |
| --- |

`#include <[mii.h](mii_8h.md)>`

Basic Mode Control Register.

## [◆ ](#gaf58b450219ae18dfa2526c685a0402a7)MII\_BMCR\_AUTONEG\_ENABLE

| #define MII\_BMCR\_AUTONEG\_ENABLE   (1 << 12) |
| --- |

`#include <[mii.h](mii_8h.md)>`

Auto-Negotiation enable.

## [◆ ](#ga110d6e1bfdbb37aa95cf1b32c54d8fa0)MII\_BMCR\_AUTONEG\_RESTART

| #define MII\_BMCR\_AUTONEG\_RESTART   (1 << 9) |
| --- |

`#include <[mii.h](mii_8h.md)>`

restart auto-negotiation

## [◆ ](#ga288bc52d6545ec634e6c2da04dbe86d3)MII\_BMCR\_DUPLEX\_MODE

| #define MII\_BMCR\_DUPLEX\_MODE   (1 << 8) |
| --- |

`#include <[mii.h](mii_8h.md)>`

full duplex mode

## [◆ ](#ga288b983fab32fb073cc42c3817b2c217)MII\_BMCR\_ISOLATE

| #define MII\_BMCR\_ISOLATE   (1 << 10) |
| --- |

`#include <[mii.h](mii_8h.md)>`

isolate electrically PHY from MII

## [◆ ](#gaaade3d675167c736186a03dad857a7c9)MII\_BMCR\_LOOPBACK

| #define MII\_BMCR\_LOOPBACK   (1 << 14) |
| --- |

`#include <[mii.h](mii_8h.md)>`

enable loopback mode

## [◆ ](#ga2598b7655be14619dffc44b9a6db36b8)MII\_BMCR\_POWER\_DOWN

| #define MII\_BMCR\_POWER\_DOWN   (1 << 11) |
| --- |

`#include <[mii.h](mii_8h.md)>`

power down mode

## [◆ ](#ga1001ac1540dc5bb6c4962f63b5fd6c3a)MII\_BMCR\_RESET

| #define MII\_BMCR\_RESET   (1 << 15) |
| --- |

`#include <[mii.h](mii_8h.md)>`

PHY reset.

## [◆ ](#ga4d31aeaad35fe6a358aef1eef1c5b4cf)MII\_BMCR\_SPEED\_10

| #define MII\_BMCR\_SPEED\_10   (0 << 6 | 0 << 13) |
| --- |

`#include <[mii.h](mii_8h.md)>`

select speed 10 Mb/s

## [◆ ](#gaf52c7fc2b468c142ae63605a201900d4)MII\_BMCR\_SPEED\_100

| #define MII\_BMCR\_SPEED\_100   (0 << 6 | 1 << 13) |
| --- |

`#include <[mii.h](mii_8h.md)>`

select speed 100 Mb/s

## [◆ ](#gaae2f486072b95b3e829d0e1bd4b8d893)MII\_BMCR\_SPEED\_1000

| #define MII\_BMCR\_SPEED\_1000   (1 << 6 | 0 << 13) |
| --- |

`#include <[mii.h](mii_8h.md)>`

select speed 1000 Mb/s

## [◆ ](#ga19ef6d51e7bc231892635d856dd6a747)MII\_BMCR\_SPEED\_LSB

| #define MII\_BMCR\_SPEED\_LSB   (1 << 13) |
| --- |

`#include <[mii.h](mii_8h.md)>`

10=1000Mbps 01=100Mbps; 00=10Mbps

## [◆ ](#gaf562ae173424ea0d41afd68d11f87115)MII\_BMCR\_SPEED\_MASK

| #define MII\_BMCR\_SPEED\_MASK   (1 << 6 | 1 << 13) |
| --- |

`#include <[mii.h](mii_8h.md)>`

Link Speed Field.

## [◆ ](#ga94e2ff6468b89371ec22a087ad5477d4)MII\_BMCR\_SPEED\_MSB

| #define MII\_BMCR\_SPEED\_MSB   (1 << 6) |
| --- |

`#include <[mii.h](mii_8h.md)>`

10=1000Mbps 01=100Mbps; 00=10Mbps

## [◆ ](#gaa2f632686d6298a7c898b1c805586aab)MII\_BMSR

| #define MII\_BMSR   0x1 |
| --- |

`#include <[mii.h](mii_8h.md)>`

Basic Mode Status Register.

## [◆ ](#ga93fb7b79b3da2ae1757fe98237dd2d6b)MII\_BMSR\_100BASE\_T2\_FULL

| #define MII\_BMSR\_100BASE\_T2\_FULL   (1 << 10) |
| --- |

`#include <[mii.h](mii_8h.md)>`

100BASE-T2 full duplex capable

## [◆ ](#gafb0d83d336eda611d45580be48f15d02)MII\_BMSR\_100BASE\_T2\_HALF

| #define MII\_BMSR\_100BASE\_T2\_HALF   (1 << 9) |
| --- |

`#include <[mii.h](mii_8h.md)>`

100BASE-T2 half duplex capable

## [◆ ](#gac8a404aa082745cb7699739bf58fc530)MII\_BMSR\_100BASE\_T4

| #define MII\_BMSR\_100BASE\_T4   (1 << 15) |
| --- |

`#include <[mii.h](mii_8h.md)>`

100BASE-T4 capable

## [◆ ](#ga090c828a41acfc824b56ec2a9a57082a)MII\_BMSR\_100BASE\_X\_FULL

| #define MII\_BMSR\_100BASE\_X\_FULL   (1 << 14) |
| --- |

`#include <[mii.h](mii_8h.md)>`

100BASE-X full duplex capable

## [◆ ](#ga608ec5361c44f25c34ae6138ae7ffef9)MII\_BMSR\_100BASE\_X\_HALF

| #define MII\_BMSR\_100BASE\_X\_HALF   (1 << 13) |
| --- |

`#include <[mii.h](mii_8h.md)>`

100BASE-X half duplex capable

## [◆ ](#ga4f085921a6b0f0586326b1bdc8f62b31)MII\_BMSR\_10\_FULL

| #define MII\_BMSR\_10\_FULL   (1 << 12) |
| --- |

`#include <[mii.h](mii_8h.md)>`

10 Mb/s full duplex capable

## [◆ ](#ga8505886511fef3ec2d8630a957de4478)MII\_BMSR\_10\_HALF

| #define MII\_BMSR\_10\_HALF   (1 << 11) |
| --- |

`#include <[mii.h](mii_8h.md)>`

10 Mb/s half duplex capable

## [◆ ](#gafc344357c76d6a41c5fa432d55355fce)MII\_BMSR\_AUTONEG\_ABILITY

| #define MII\_BMSR\_AUTONEG\_ABILITY   (1 << 3) |
| --- |

`#include <[mii.h](mii_8h.md)>`

PHY is able to perform Auto-Negotiation.

## [◆ ](#gac5b9ac6b54ce146c91197660c2ccd207)MII\_BMSR\_AUTONEG\_COMPLETE

| #define MII\_BMSR\_AUTONEG\_COMPLETE   (1 << 5) |
| --- |

`#include <[mii.h](mii_8h.md)>`

Auto-negotiation process completed.

## [◆ ](#gab225377deb09eb179b7efee199c7edd4)MII\_BMSR\_EXTEND\_CAPAB

| #define MII\_BMSR\_EXTEND\_CAPAB   (1 << 0) |
| --- |

`#include <[mii.h](mii_8h.md)>`

extended register capabilities

## [◆ ](#ga24992988cde973ce2a954fe372a5ad0e)MII\_BMSR\_EXTEND\_STATUS

| #define MII\_BMSR\_EXTEND\_STATUS   (1 << 8) |
| --- |

`#include <[mii.h](mii_8h.md)>`

extend status information in reg 15

## [◆ ](#gad9ef4a2223dfee6826b0fdc8b25802ea)MII\_BMSR\_JABBER\_DETECT

| #define MII\_BMSR\_JABBER\_DETECT   (1 << 1) |
| --- |

`#include <[mii.h](mii_8h.md)>`

jabber condition detected

## [◆ ](#ga884d39c456206cee38ce5a9a9ca01599)MII\_BMSR\_LINK\_STATUS

| #define MII\_BMSR\_LINK\_STATUS   (1 << 2) |
| --- |

`#include <[mii.h](mii_8h.md)>`

link is up

## [◆ ](#gae85e29e0f9a50898f93ff6e5a5f763e4)MII\_BMSR\_MF\_PREAMB\_SUPPR

| #define MII\_BMSR\_MF\_PREAMB\_SUPPR   (1 << 6) |
| --- |

`#include <[mii.h](mii_8h.md)>`

PHY accepts management frames with preamble suppressed.

## [◆ ](#ga0dd8421740c52ecd5e6a53e969d2e48a)MII\_BMSR\_REMOTE\_FAULT

| #define MII\_BMSR\_REMOTE\_FAULT   (1 << 4) |
| --- |

`#include <[mii.h](mii_8h.md)>`

remote fault detected

## [◆ ](#gaa705f43dba50029d5395379e1f2b802d)MII\_ESTAT

| #define MII\_ESTAT   0xf |
| --- |

`#include <[mii.h](mii_8h.md)>`

Extended Status Register.

## [◆ ](#gada0831dbbb86ff717b40c23c73345731)MII\_ESTAT\_1000BASE\_T\_FULL

| #define MII\_ESTAT\_1000BASE\_T\_FULL   (1 << 13) |
| --- |

`#include <[mii.h](mii_8h.md)>`

1000BASE-T full-duplex capable

## [◆ ](#ga42e8d732fd9806e218599871fd1291d5)MII\_ESTAT\_1000BASE\_T\_HALF

| #define MII\_ESTAT\_1000BASE\_T\_HALF   (1 << 12) |
| --- |

`#include <[mii.h](mii_8h.md)>`

1000BASE-T half-duplex capable

## [◆ ](#ga846525a526aa9704a175c84771e48290)MII\_ESTAT\_1000BASE\_X\_FULL

| #define MII\_ESTAT\_1000BASE\_X\_FULL   (1 << 15) |
| --- |

`#include <[mii.h](mii_8h.md)>`

1000BASE-X full-duplex capable

## [◆ ](#gabec9696aa599caca1131f869827bbc95)MII\_ESTAT\_1000BASE\_X\_HALF

| #define MII\_ESTAT\_1000BASE\_X\_HALF   (1 << 14) |
| --- |

`#include <[mii.h](mii_8h.md)>`

1000BASE-X half-duplex capable

## [◆ ](#ga378832f55be1a03977c829f09dd1d364)MII\_MMD\_AADR

| #define MII\_MMD\_AADR   0xe |
| --- |

`#include <[mii.h](mii_8h.md)>`

MMD Access Address Data Register.

## [◆ ](#ga7d6687385994aac21782308af560b224)MII\_MMD\_ACR

| #define MII\_MMD\_ACR   0xd |
| --- |

`#include <[mii.h](mii_8h.md)>`

MMD Access Control Register.

## [◆ ](#ga0f312eab9b4d51af4a72f7cb3898754a)MII\_MMD\_ACR\_ADDR

| #define MII\_MMD\_ACR\_ADDR   (0x00 << 14) |
| --- |

`#include <[mii.h](mii_8h.md)>`

Address Data bits.

## [◆ ](#ga6cac36daf5db44274cd60a05b77819f4)MII\_MMD\_ACR\_DATA\_NO\_POS\_INC

| #define MII\_MMD\_ACR\_DATA\_NO\_POS\_INC   (0x01 << 14) |
| --- |

`#include <[mii.h](mii_8h.md)>`

## [◆ ](#ga3be4dced4eec405c42467ba51c5efb9c)MII\_MMD\_ACR\_DATA\_RW\_POS\_INC

| #define MII\_MMD\_ACR\_DATA\_RW\_POS\_INC   (0x10 << 14) |
| --- |

`#include <[mii.h](mii_8h.md)>`

## [◆ ](#ga48f56892c3e8d6ec7e90a7e36dd67309)MII\_MMD\_ACR\_DATA\_W\_POS\_INC

| #define MII\_MMD\_ACR\_DATA\_W\_POS\_INC   (0x11 << 14) |
| --- |

`#include <[mii.h](mii_8h.md)>`

## [◆ ](#gae4ac896c90a75cdc4869797708823673)MII\_MMD\_ACR\_DEVAD\_MASK

| #define MII\_MMD\_ACR\_DEVAD\_MASK   (0x1F << 0) |
| --- |

`#include <[mii.h](mii_8h.md)>`

DEVAD Mask.

## [◆ ](#ga87196e916598cea91b6ce400ad0cc34a)MII\_PHYID1R

| #define MII\_PHYID1R   0x2 |
| --- |

`#include <[mii.h](mii_8h.md)>`

PHY ID 1 Register.

## [◆ ](#ga40766cdb8f9c3ffee64720f0f0ea2f15)MII\_PHYID2R

| #define MII\_PHYID2R   0x3 |
| --- |

`#include <[mii.h](mii_8h.md)>`

PHY ID 2 Register.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
