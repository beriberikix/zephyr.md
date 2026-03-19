---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mii_8h.html
original_path: doxygen/html/mii_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mii.h File Reference

Definitions for IEEE 802.3, Section 2 MII compatible PHY transceivers.
[More...](#details)

[Go to the source code of this file.](mii_8h_source.md)

| Macros | |
| --- | --- |
| #define | [MII\_BMCR](group__ethernet__mii.md#ga9137acedc42ff140f244da7473cff29e)   0x0 |
|  | Basic Mode Control Register. |
| #define | [MII\_BMSR](group__ethernet__mii.md#gaa2f632686d6298a7c898b1c805586aab)   0x1 |
|  | Basic Mode Status Register. |
| #define | [MII\_PHYID1R](group__ethernet__mii.md#ga87196e916598cea91b6ce400ad0cc34a)   0x2 |
|  | PHY ID 1 Register. |
| #define | [MII\_PHYID2R](group__ethernet__mii.md#ga40766cdb8f9c3ffee64720f0f0ea2f15)   0x3 |
|  | PHY ID 2 Register. |
| #define | [MII\_ANAR](group__ethernet__mii.md#gaacb2ab0ea5579b5d9e30b075991add1d)   0x4 |
|  | Auto-Negotiation Advertisement Register. |
| #define | [MII\_ANLPAR](group__ethernet__mii.md#ga445e8381a9ea9724054bfacc10bb4c81)   0x5 |
|  | Auto-Negotiation Link Partner Ability Reg. |
| #define | [MII\_ANER](group__ethernet__mii.md#ga6e5634d8831e21f963ddc16b91d5f6b9)   0x6 |
|  | Auto-Negotiation Expansion Register. |
| #define | [MII\_ANNPTR](group__ethernet__mii.md#ga3f3ed3ecfd22b34b840ff2473ca68490)   0x7 |
|  | Auto-Negotiation Next Page Transmit Register. |
| #define | [MII\_ANLPRNPR](group__ethernet__mii.md#gaf17d80457d4a609d16793870d4a76bdf)   0x8 |
|  | Auto-Negotiation Link Partner Received Next Page Reg. |
| #define | [MII\_1KTCR](group__ethernet__mii.md#ga9e258e8e518579ac5f9a8809ddc6aedb)   0x9 |
|  | 1000BASE-T Control Register |
| #define | [MII\_1KSTSR](group__ethernet__mii.md#ga49a74b346b13cc80c159c0f8f6b9c0f0)   0xa |
|  | 1000BASE-T Status Register |
| #define | [MII\_MMD\_ACR](group__ethernet__mii.md#ga7d6687385994aac21782308af560b224)   0xd |
|  | MMD Access Control Register. |
| #define | [MII\_MMD\_AADR](group__ethernet__mii.md#ga378832f55be1a03977c829f09dd1d364)   0xe |
|  | MMD Access Address Data Register. |
| #define | [MII\_ESTAT](group__ethernet__mii.md#gaa705f43dba50029d5395379e1f2b802d)   0xf |
|  | Extended Status Register. |
| #define | [MII\_BMCR\_RESET](group__ethernet__mii.md#ga1001ac1540dc5bb6c4962f63b5fd6c3a)   (1 << 15) |
|  | PHY reset. |
| #define | [MII\_BMCR\_LOOPBACK](group__ethernet__mii.md#gaaade3d675167c736186a03dad857a7c9)   (1 << 14) |
|  | enable loopback mode |
| #define | [MII\_BMCR\_SPEED\_LSB](group__ethernet__mii.md#ga19ef6d51e7bc231892635d856dd6a747)   (1 << 13) |
|  | 10=1000Mbps 01=100Mbps; 00=10Mbps |
| #define | [MII\_BMCR\_AUTONEG\_ENABLE](group__ethernet__mii.md#gaf58b450219ae18dfa2526c685a0402a7)   (1 << 12) |
|  | Auto-Negotiation enable. |
| #define | [MII\_BMCR\_POWER\_DOWN](group__ethernet__mii.md#ga2598b7655be14619dffc44b9a6db36b8)   (1 << 11) |
|  | power down mode |
| #define | [MII\_BMCR\_ISOLATE](group__ethernet__mii.md#ga288b983fab32fb073cc42c3817b2c217)   (1 << 10) |
|  | isolate electrically PHY from MII |
| #define | [MII\_BMCR\_AUTONEG\_RESTART](group__ethernet__mii.md#ga110d6e1bfdbb37aa95cf1b32c54d8fa0)   (1 << 9) |
|  | restart auto-negotiation |
| #define | [MII\_BMCR\_DUPLEX\_MODE](group__ethernet__mii.md#ga288bc52d6545ec634e6c2da04dbe86d3)   (1 << 8) |
|  | full duplex mode |
| #define | [MII\_BMCR\_SPEED\_MSB](group__ethernet__mii.md#ga94e2ff6468b89371ec22a087ad5477d4)   (1 << 6) |
|  | 10=1000Mbps 01=100Mbps; 00=10Mbps |
| #define | [MII\_BMCR\_SPEED\_MASK](group__ethernet__mii.md#gaf562ae173424ea0d41afd68d11f87115)   (1 << 6 | 1 << 13) |
|  | Link Speed Field. |
| #define | [MII\_BMCR\_SPEED\_10](group__ethernet__mii.md#ga4d31aeaad35fe6a358aef1eef1c5b4cf)   (0 << 6 | 0 << 13) |
|  | select speed 10 Mb/s |
| #define | [MII\_BMCR\_SPEED\_100](group__ethernet__mii.md#gaf52c7fc2b468c142ae63605a201900d4)   (0 << 6 | 1 << 13) |
|  | select speed 100 Mb/s |
| #define | [MII\_BMCR\_SPEED\_1000](group__ethernet__mii.md#gaae2f486072b95b3e829d0e1bd4b8d893)   (1 << 6 | 0 << 13) |
|  | select speed 1000 Mb/s |
| #define | [MII\_BMSR\_100BASE\_T4](group__ethernet__mii.md#gac8a404aa082745cb7699739bf58fc530)   (1 << 15) |
|  | 100BASE-T4 capable |
| #define | [MII\_BMSR\_100BASE\_X\_FULL](group__ethernet__mii.md#ga090c828a41acfc824b56ec2a9a57082a)   (1 << 14) |
|  | 100BASE-X full duplex capable |
| #define | [MII\_BMSR\_100BASE\_X\_HALF](group__ethernet__mii.md#ga608ec5361c44f25c34ae6138ae7ffef9)   (1 << 13) |
|  | 100BASE-X half duplex capable |
| #define | [MII\_BMSR\_10\_FULL](group__ethernet__mii.md#ga4f085921a6b0f0586326b1bdc8f62b31)   (1 << 12) |
|  | 10 Mb/s full duplex capable |
| #define | [MII\_BMSR\_10\_HALF](group__ethernet__mii.md#ga8505886511fef3ec2d8630a957de4478)   (1 << 11) |
|  | 10 Mb/s half duplex capable |
| #define | [MII\_BMSR\_100BASE\_T2\_FULL](group__ethernet__mii.md#ga93fb7b79b3da2ae1757fe98237dd2d6b)   (1 << 10) |
|  | 100BASE-T2 full duplex capable |
| #define | [MII\_BMSR\_100BASE\_T2\_HALF](group__ethernet__mii.md#gafb0d83d336eda611d45580be48f15d02)   (1 << 9) |
|  | 100BASE-T2 half duplex capable |
| #define | [MII\_BMSR\_EXTEND\_STATUS](group__ethernet__mii.md#ga24992988cde973ce2a954fe372a5ad0e)   (1 << 8) |
|  | extend status information in reg 15 |
| #define | [MII\_BMSR\_MF\_PREAMB\_SUPPR](group__ethernet__mii.md#gae85e29e0f9a50898f93ff6e5a5f763e4)   (1 << 6) |
|  | PHY accepts management frames with preamble suppressed. |
| #define | [MII\_BMSR\_AUTONEG\_COMPLETE](group__ethernet__mii.md#gac5b9ac6b54ce146c91197660c2ccd207)   (1 << 5) |
|  | Auto-negotiation process completed. |
| #define | [MII\_BMSR\_REMOTE\_FAULT](group__ethernet__mii.md#ga0dd8421740c52ecd5e6a53e969d2e48a)   (1 << 4) |
|  | remote fault detected |
| #define | [MII\_BMSR\_AUTONEG\_ABILITY](group__ethernet__mii.md#gafc344357c76d6a41c5fa432d55355fce)   (1 << 3) |
|  | PHY is able to perform Auto-Negotiation. |
| #define | [MII\_BMSR\_LINK\_STATUS](group__ethernet__mii.md#ga884d39c456206cee38ce5a9a9ca01599)   (1 << 2) |
|  | link is up |
| #define | [MII\_BMSR\_JABBER\_DETECT](group__ethernet__mii.md#gad9ef4a2223dfee6826b0fdc8b25802ea)   (1 << 1) |
|  | jabber condition detected |
| #define | [MII\_BMSR\_EXTEND\_CAPAB](group__ethernet__mii.md#gab225377deb09eb179b7efee199c7edd4)   (1 << 0) |
|  | extended register capabilities |
| #define | [MII\_ADVERTISE\_NEXT\_PAGE](group__ethernet__mii.md#ga4e567fc428a19d55c13c6be38091ed59)   (1 << 15) |
|  | next page |
| #define | [MII\_ADVERTISE\_LPACK](group__ethernet__mii.md#gaca8ed07be80166e8abaefb4135008989)   (1 << 14) |
|  | link partner acknowledge response |
| #define | [MII\_ADVERTISE\_REMOTE\_FAULT](group__ethernet__mii.md#ga3e1cfef9ac347b86324d25c1d00a07ef)   (1 << 13) |
|  | remote fault |
| #define | [MII\_ADVERTISE\_ASYM\_PAUSE](group__ethernet__mii.md#gaf8b5e7fc3226b89b875f46a50165e332)   (1 << 11) |
|  | try for asymmetric pause |
| #define | [MII\_ADVERTISE\_PAUSE](group__ethernet__mii.md#ga7b3dfbe50b37378cbf45d15f9ef88c7f)   (1 << 10) |
|  | try for pause |
| #define | [MII\_ADVERTISE\_100BASE\_T4](group__ethernet__mii.md#ga11a26530d734fb68be5538ac36019821)   (1 << 9) |
|  | try for 100BASE-T4 support |
| #define | [MII\_ADVERTISE\_100\_FULL](group__ethernet__mii.md#ga72f632c88cf6c472b893c326d7a8d263)   (1 << 8) |
|  | try for 100BASE-X full duplex support |
| #define | [MII\_ADVERTISE\_100\_HALF](group__ethernet__mii.md#ga357539fe99d327cae0e76acd5059876f)   (1 << 7) |
|  | try for 100BASE-X support |
| #define | [MII\_ADVERTISE\_10\_FULL](group__ethernet__mii.md#ga44ee311ef785619a215de80fc0286a4c)   (1 << 6) |
|  | try for 10 Mb/s full duplex support |
| #define | [MII\_ADVERTISE\_10\_HALF](group__ethernet__mii.md#gac5c508943ce4006fa2f934c25436fdb5)   (1 << 5) |
|  | try for 10 Mb/s half duplex support |
| #define | [MII\_ADVERTISE\_SEL\_MASK](group__ethernet__mii.md#gac01baecf625bbb6d55a14ac0c2b181bd)   (0x1F << 0) |
|  | Selector Field Mask. |
| #define | [MII\_ADVERTISE\_SEL\_IEEE\_802\_3](group__ethernet__mii.md#ga9abdfc8110120f54612c712d86cab3ac)   0x01 |
|  | Selector Field. |
| #define | [MII\_ADVERTISE\_1000\_FULL](group__ethernet__mii.md#ga028ddaf632ced31e57249883c90ed921)   (1 << 9) |
|  | try for 1000BASE-T full duplex support |
| #define | [MII\_ADVERTISE\_1000\_HALF](group__ethernet__mii.md#ga5f36d375690560688185d1207687611b)   (1 << 8) |
|  | try for 1000BASE-T half duplex support |
| #define | [MII\_ADVERTISE\_ALL](group__ethernet__mii.md#gacac6f915a8d0e3f8244c571646b3fc92) |
|  | Advertise all speeds. |
| #define | [MII\_ESTAT\_1000BASE\_X\_FULL](group__ethernet__mii.md#ga846525a526aa9704a175c84771e48290)   (1 << 15) |
|  | 1000BASE-X full-duplex capable |
| #define | [MII\_ESTAT\_1000BASE\_X\_HALF](group__ethernet__mii.md#gabec9696aa599caca1131f869827bbc95)   (1 << 14) |
|  | 1000BASE-X half-duplex capable |
| #define | [MII\_ESTAT\_1000BASE\_T\_FULL](group__ethernet__mii.md#gada0831dbbb86ff717b40c23c73345731)   (1 << 13) |
|  | 1000BASE-T full-duplex capable |
| #define | [MII\_ESTAT\_1000BASE\_T\_HALF](group__ethernet__mii.md#ga42e8d732fd9806e218599871fd1291d5)   (1 << 12) |
|  | 1000BASE-T half-duplex capable |
| #define | [MII\_MMD\_ACR\_DEVAD\_MASK](group__ethernet__mii.md#gae4ac896c90a75cdc4869797708823673)   (0x1F << 0) |
|  | DEVAD Mask. |
| #define | [MII\_MMD\_ACR\_ADDR](group__ethernet__mii.md#ga0f312eab9b4d51af4a72f7cb3898754a)   (0x00 << 14) |
|  | Address Data bits. |
| #define | [MII\_MMD\_ACR\_DATA\_NO\_POS\_INC](group__ethernet__mii.md#ga6cac36daf5db44274cd60a05b77819f4)   (0x01 << 14) |
| #define | [MII\_MMD\_ACR\_DATA\_RW\_POS\_INC](group__ethernet__mii.md#ga3be4dced4eec405c42467ba51c5efb9c)   (0x10 << 14) |
| #define | [MII\_MMD\_ACR\_DATA\_W\_POS\_INC](group__ethernet__mii.md#ga48f56892c3e8d6ec7e90a7e36dd67309)   (0x11 << 14) |

## Detailed Description

Definitions for IEEE 802.3, Section 2 MII compatible PHY transceivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [mii.h](mii_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
