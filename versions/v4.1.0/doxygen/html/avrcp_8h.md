---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/avrcp_8h.html
original_path: doxygen/html/avrcp_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

avrcp.h File Reference

Audio Video Remote Control Profile header.
[More...](#details)

[Go to the source code of this file.](avrcp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_avrcp\_unit\_info\_rsp](structbt__avrcp__unit__info__rsp.md) |
| struct | [bt\_avrcp\_subunit\_info\_rsp](structbt__avrcp__subunit__info__rsp.md) |
| struct | [bt\_avrcp\_passthrough\_rsp](structbt__avrcp__passthrough__rsp.md) |
| struct | [bt\_avrcp\_cb](structbt__avrcp__cb.md) |

| Enumerations | |
| --- | --- |
| enum | [bt\_avrcp\_ctype\_t](#a2a4c610e00ba9832f954f30bd6b6618e) {     [BT\_AVRCP\_CTYPE\_CONTROL](#a2a4c610e00ba9832f954f30bd6b6618ea1a2aa36da42f3751f3a94b218118ae04) = 0x0 , [BT\_AVRCP\_CTYPE\_STATUS](#a2a4c610e00ba9832f954f30bd6b6618ea9a1b0564c98a0637a2ca5a0b97c3e6ce) = 0x1 , [BT\_AVRCP\_CTYPE\_SPECIFIC\_INQUIRY](#a2a4c610e00ba9832f954f30bd6b6618eac4c9dfbce497d9a043d7ac42ee932bdb) = 0x2 , [BT\_AVRCP\_CTYPE\_NOTIFY](#a2a4c610e00ba9832f954f30bd6b6618ead58dcc95df3973a7bed94068be913290) = 0x3 ,     [BT\_AVRCP\_CTYPE\_GENERAL\_INQUIRY](#a2a4c610e00ba9832f954f30bd6b6618ea0eefcdda49616cf818efdc0a7b5975f7) = 0x4   } |
|  | AV/C command types. [More...](#a2a4c610e00ba9832f954f30bd6b6618e) |
| enum | [bt\_avrcp\_rsp\_t](#aba2d8faec2c3baf7403199ea8a509326) {     [BT\_AVRCP\_RSP\_NOT\_IMPLEMENTED](#aba2d8faec2c3baf7403199ea8a509326a8a4cfe6ca8f5b92402c029d02b625696) = 0x8 , [BT\_AVRCP\_RSP\_ACCEPTED](#aba2d8faec2c3baf7403199ea8a509326a2c93dc0bfd19305d8012b73001989cd8) = 0x9 , [BT\_AVRCP\_RSP\_REJECTED](#aba2d8faec2c3baf7403199ea8a509326a1775849a3c303b61975c569cc85e943c) = 0xa , [BT\_AVRCP\_RSP\_IN\_TRANSITION](#aba2d8faec2c3baf7403199ea8a509326ab4b63e5cf84ea34895702ceea5ae81ad) = 0xb ,     [BT\_AVRCP\_RSP\_IMPLEMENTED](#aba2d8faec2c3baf7403199ea8a509326aa49f2871cf4e5f493128f574ad0d6144) = 0xc , [BT\_AVRCP\_RSP\_STABLE](#aba2d8faec2c3baf7403199ea8a509326a4136d697a8a0ea5daa1a6e89b314b992) = 0xc , [BT\_AVRCP\_RSP\_CHANGED](#aba2d8faec2c3baf7403199ea8a509326acf6f13da82b371efbcdf03fbedcb6988) = 0xd , [BT\_AVRCP\_RSP\_INTERIM](#aba2d8faec2c3baf7403199ea8a509326a4a2ed58a814be12b93753a6458b15e88) = 0xf   } |
|  | AV/C response codes. [More...](#aba2d8faec2c3baf7403199ea8a509326) |
| enum | [bt\_avrcp\_opid\_t](#a3c997d96028343a0a5a4948dabe19b84) {     [BT\_AVRCP\_OPID\_SELECT](#a3c997d96028343a0a5a4948dabe19b84acbaded78ac1e41d16464ea9db667c27f) = 0x00 , [BT\_AVRCP\_OPID\_UP](#a3c997d96028343a0a5a4948dabe19b84aae8fe4a27cf2b70bb289f38d4016b9d9) = 0x01 , [BT\_AVRCP\_OPID\_DOWN](#a3c997d96028343a0a5a4948dabe19b84a0d81584ba5cc6bb9c790b87fcf638537) = 0x02 , [BT\_AVRCP\_OPID\_LEFT](#a3c997d96028343a0a5a4948dabe19b84a734fa5664a306957cb28eec36806e4ba) = 0x03 ,     [BT\_AVRCP\_OPID\_RIGHT](#a3c997d96028343a0a5a4948dabe19b84a9030a666a42a54b02b4c7f876f1ae9d2) = 0x04 , [BT\_AVRCP\_OPID\_RIGHT\_UP](#a3c997d96028343a0a5a4948dabe19b84a831592a4b2634815f9716e80252dce63) = 0x05 , [BT\_AVRCP\_OPID\_RIGHT\_DOWN](#a3c997d96028343a0a5a4948dabe19b84a61d7145a6aa482256cd8aaad7bb96745) = 0x06 , [BT\_AVRCP\_OPID\_LEFT\_UP](#a3c997d96028343a0a5a4948dabe19b84a8445dd492ab9e6a9b387162f2f7ab779) = 0x07 ,     [BT\_AVRCP\_OPID\_LEFT\_DOWN](#a3c997d96028343a0a5a4948dabe19b84a6660a000e5bc1d8ead271924a3780366) = 0x08 , [BT\_AVRCP\_OPID\_ROOT\_MENU](#a3c997d96028343a0a5a4948dabe19b84a002efdb93a2dd52bb5bbec05d9537f87) = 0x09 , [BT\_AVRCP\_OPID\_SETUP\_MENU](#a3c997d96028343a0a5a4948dabe19b84a827d1eaa2f12a37219fc1f78f617d372) = 0x0a , [BT\_AVRCP\_OPID\_CONTENTS\_MENU](#a3c997d96028343a0a5a4948dabe19b84aa9d64afb98b2fc91cae3810990451472) = 0x0b ,     [BT\_AVRCP\_OPID\_FAVORITE\_MENU](#a3c997d96028343a0a5a4948dabe19b84a470fa709a8a7e35ec12a593ae9dd1574) = 0x0c , [BT\_AVRCP\_OPID\_EXIT](#a3c997d96028343a0a5a4948dabe19b84a9ecca98aa1f55ee6a2b6824e0940a7c3) = 0x0d , [BT\_AVRCP\_OPID\_0](#a3c997d96028343a0a5a4948dabe19b84ae6430b447ccd9e15d0ef2ae62152bade) = 0x20 , [BT\_AVRCP\_OPID\_1](#a3c997d96028343a0a5a4948dabe19b84a94ca82a18f2c06379160e69675d927d0) = 0x21 ,     [BT\_AVRCP\_OPID\_2](#a3c997d96028343a0a5a4948dabe19b84acb3f6e1f71628853bb457bfb8163c566) = 0x22 , [BT\_AVRCP\_OPID\_3](#a3c997d96028343a0a5a4948dabe19b84af1d1ea7e57a0a16c8e6ad8b9961d4459) = 0x23 , [BT\_AVRCP\_OPID\_4](#a3c997d96028343a0a5a4948dabe19b84a23d18efccc7b1940e72b62b08fa5ab6c) = 0x24 , [BT\_AVRCP\_OPID\_5](#a3c997d96028343a0a5a4948dabe19b84a91a40f7dfb02c38cd7998adf5fe948b5) = 0x25 ,     [BT\_AVRCP\_OPID\_6](#a3c997d96028343a0a5a4948dabe19b84a029017bcc52cf7c4ffac3db5f92f4e2a) = 0x26 , [BT\_AVRCP\_OPID\_7](#a3c997d96028343a0a5a4948dabe19b84aac755d13a6f53ead21818a9fb90217ff) = 0x27 , [BT\_AVRCP\_OPID\_8](#a3c997d96028343a0a5a4948dabe19b84ac751478296cc6a9e5de77fdf3c8fce06) = 0x28 , [BT\_AVRCP\_OPID\_9](#a3c997d96028343a0a5a4948dabe19b84a07ed4fda3e230d4e95576a25c6d02dcb) = 0x29 ,     [BT\_AVRCP\_OPID\_DOT](#a3c997d96028343a0a5a4948dabe19b84a5d3a33be8473fc401e3f38a9f234debf) = 0x2a , [BT\_AVRCP\_OPID\_ENTER](#a3c997d96028343a0a5a4948dabe19b84a28d5c8b1960aa1e70c0659c40cac32ae) = 0x2b , [BT\_AVRCP\_OPID\_CLEAR](#a3c997d96028343a0a5a4948dabe19b84ae6046a270ff9f8939059248cddc7a8a2) = 0x2c , [BT\_AVRCP\_OPID\_CHANNEL\_UP](#a3c997d96028343a0a5a4948dabe19b84ad39e69c55c571eb3c2492d5aa086e586) = 0x30 ,     [BT\_AVRCP\_OPID\_CHANNEL\_DOWN](#a3c997d96028343a0a5a4948dabe19b84a300bbf8fe3236a55bfc97e2d7d8323de) = 0x31 , [BT\_AVRCP\_OPID\_PREVIOUS\_CHANNEL](#a3c997d96028343a0a5a4948dabe19b84a3e59a9dc846182d2bc26cf2e5960558e) = 0x32 , [BT\_AVRCP\_OPID\_SOUND\_SELECT](#a3c997d96028343a0a5a4948dabe19b84a1fb2420a2130a9f22f1837c0c3e0896b) = 0x33 , [BT\_AVRCP\_OPID\_INPUT\_SELECT](#a3c997d96028343a0a5a4948dabe19b84a8fa3d0ac9fc3feefedf3b2d370df748c) = 0x34 ,     [BT\_AVRCP\_OPID\_DISPLAY\_INFORMATION](#a3c997d96028343a0a5a4948dabe19b84a735b97b85b1183c862955131a09b1eef) = 0x35 , [BT\_AVRCP\_OPID\_HELP](#a3c997d96028343a0a5a4948dabe19b84ab3a7619c2c3cafe2eab868d471c8066b) = 0x36 , [BT\_AVRCP\_OPID\_PAGE\_UP](#a3c997d96028343a0a5a4948dabe19b84a93ffda310d3a0999256b42cd4652e321) = 0x37 , [BT\_AVRCP\_OPID\_PAGE\_DOWN](#a3c997d96028343a0a5a4948dabe19b84a3078b64d3c759e83d04923ca6bcf079a) = 0x38 ,     [BT\_AVRCP\_OPID\_POWER](#a3c997d96028343a0a5a4948dabe19b84a9623c492b7a04750fb3938dde65a9358) = 0x40 , [BT\_AVRCP\_OPID\_VOLUME\_UP](#a3c997d96028343a0a5a4948dabe19b84af5f5b89b6f81961f7bf235c91f59b487) = 0x41 , [BT\_AVRCP\_OPID\_VOLUME\_DOWN](#a3c997d96028343a0a5a4948dabe19b84a49d2a954862bdf45c30ed734e5a29a62) = 0x42 , [BT\_AVRCP\_OPID\_MUTE](#a3c997d96028343a0a5a4948dabe19b84a5c37fbe03a5e7b8cda842262f7a504e1) = 0x43 ,     [BT\_AVRCP\_OPID\_PLAY](#a3c997d96028343a0a5a4948dabe19b84ae76461b7c08169ad190a83545b9e584b) = 0x44 , [BT\_AVRCP\_OPID\_STOP](#a3c997d96028343a0a5a4948dabe19b84a69254767fc4183e1534b12cd6bd88f60) = 0x45 , [BT\_AVRCP\_OPID\_PAUSE](#a3c997d96028343a0a5a4948dabe19b84a0e7877d88781dbacdac095c7d36f186a) = 0x46 , [BT\_AVRCP\_OPID\_RECORD](#a3c997d96028343a0a5a4948dabe19b84a8364f5d44be3b666f5d995368e3dda27) = 0x47 ,     [BT\_AVRCP\_OPID\_REWIND](#a3c997d96028343a0a5a4948dabe19b84a4bba25ed6730766902ecb92e4f546dc8) = 0x48 , [BT\_AVRCP\_OPID\_FAST\_FORWARD](#a3c997d96028343a0a5a4948dabe19b84a6c83aff2115939aa17f6bbd68c792e4f) = 0x49 , [BT\_AVRCP\_OPID\_EJECT](#a3c997d96028343a0a5a4948dabe19b84ae34d68953054ef4446403a1e240e3344) = 0x4a , [BT\_AVRCP\_OPID\_FORWARD](#a3c997d96028343a0a5a4948dabe19b84a004689a6684c527035f06fa8d715a09e) = 0x4b ,     [BT\_AVRCP\_OPID\_BACKWARD](#a3c997d96028343a0a5a4948dabe19b84a0030ffc7149baf83def17e4e2be76f23) = 0x4c , [BT\_AVRCP\_OPID\_ANGLE](#a3c997d96028343a0a5a4948dabe19b84afc51d7bc6acd64c3dbeb1f10a06113c2) = 0x50 , [BT\_AVRCP\_OPID\_SUBPICTURE](#a3c997d96028343a0a5a4948dabe19b84ac1e3dd409b98c71eaf12567ce5028a98) = 0x51 , [BT\_AVRCP\_OPID\_F1](#a3c997d96028343a0a5a4948dabe19b84a91595d93490cfe27e239c799e927b2b5) = 0x71 ,     [BT\_AVRCP\_OPID\_F2](#a3c997d96028343a0a5a4948dabe19b84a8b0656fed7b936e131a5c9dbdb32a7a4) = 0x72 , [BT\_AVRCP\_OPID\_F3](#a3c997d96028343a0a5a4948dabe19b84a1380078d446b892a25b8b2d28a405e40) = 0x73 , [BT\_AVRCP\_OPID\_F4](#a3c997d96028343a0a5a4948dabe19b84a01fc4e91d59b8c530fe142d2f1c95283) = 0x74 , [BT\_AVRCP\_OPID\_F5](#a3c997d96028343a0a5a4948dabe19b84a86a61c08b203d0bcc8b8a3ed5090ef7d) = 0x75 ,     [BT\_AVRCP\_OPID\_VENDOR\_UNIQUE](#a3c997d96028343a0a5a4948dabe19b84ad6eac39b4aced31534fde97a411b8c4d) = 0x7e   } |
|  | AV/C operation ids used in AVRCP passthrough commands. [More...](#a3c997d96028343a0a5a4948dabe19b84) |
| enum | [bt\_avrcp\_button\_state\_t](#a15f9f868b056f17ea12d96530b7da881) { [BT\_AVRCP\_BUTTON\_PRESSED](#a15f9f868b056f17ea12d96530b7da881a1465f08940f04a7b35832e6d5f73a4e3) = 0 , [BT\_AVRCP\_BUTTON\_RELEASED](#a15f9f868b056f17ea12d96530b7da881a0eb47ec4ca3d7e0bf613de53d5e50706) = 1 } |
|  | AVRCP button state flag. [More...](#a15f9f868b056f17ea12d96530b7da881) |

| Functions | |
| --- | --- |
| struct bt\_avrcp \* | [bt\_avrcp\_connect](#addc1f4f530b9e3eb4a669fe606479c59) (struct bt\_conn \*conn) |
|  | Connect AVRCP. |
| int | [bt\_avrcp\_disconnect](#af68c54ea0b17ebaa9872d271b0fee9bd) (struct bt\_avrcp \*avrcp) |
|  | Disconnect AVRCP. |
| int | [bt\_avrcp\_register\_cb](#aedb1bc8dd553aa44fdaec2b9f5c76607) (const struct [bt\_avrcp\_cb](structbt__avrcp__cb.md) \*cb) |
|  | Register callback. |
| int | [bt\_avrcp\_get\_unit\_info](#aba521a01fea4e7aee8b40ba72ca10bcf) (struct bt\_avrcp \*avrcp) |
|  | Get AVRCP Unit Info. |
| int | [bt\_avrcp\_get\_subunit\_info](#a127eaf05867a84fb5183e044fdfb55c0) (struct bt\_avrcp \*avrcp) |
|  | Get AVRCP Subunit Info. |
| int | [bt\_avrcp\_passthrough](#afeea270bacac6a59af74c02fc1d98945) (struct bt\_avrcp \*avrcp, [bt\_avrcp\_opid\_t](#a3c997d96028343a0a5a4948dabe19b84) operation\_id, [bt\_avrcp\_button\_state\_t](#a15f9f868b056f17ea12d96530b7da881) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*payload, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) len) |
|  | Send AVRCP Pass Through command. |

## Detailed Description

Audio Video Remote Control Profile header.

## Enumeration Type Documentation

## [◆ ](#a15f9f868b056f17ea12d96530b7da881)bt\_avrcp\_button\_state\_t

| enum [bt\_avrcp\_button\_state\_t](#a15f9f868b056f17ea12d96530b7da881) |
| --- |

AVRCP button state flag.

| Enumerator | |
| --- | --- |
| BT\_AVRCP\_BUTTON\_PRESSED |  |
| BT\_AVRCP\_BUTTON\_RELEASED |  |

## [◆ ](#a2a4c610e00ba9832f954f30bd6b6618e)bt\_avrcp\_ctype\_t

| enum [bt\_avrcp\_ctype\_t](#a2a4c610e00ba9832f954f30bd6b6618e) |
| --- |

AV/C command types.

| Enumerator | |
| --- | --- |
| BT\_AVRCP\_CTYPE\_CONTROL |  |
| BT\_AVRCP\_CTYPE\_STATUS |  |
| BT\_AVRCP\_CTYPE\_SPECIFIC\_INQUIRY |  |
| BT\_AVRCP\_CTYPE\_NOTIFY |  |
| BT\_AVRCP\_CTYPE\_GENERAL\_INQUIRY |  |

## [◆ ](#a3c997d96028343a0a5a4948dabe19b84)bt\_avrcp\_opid\_t

| enum [bt\_avrcp\_opid\_t](#a3c997d96028343a0a5a4948dabe19b84) |
| --- |

AV/C operation ids used in AVRCP passthrough commands.

| Enumerator | |
| --- | --- |
| BT\_AVRCP\_OPID\_SELECT |  |
| BT\_AVRCP\_OPID\_UP |  |
| BT\_AVRCP\_OPID\_DOWN |  |
| BT\_AVRCP\_OPID\_LEFT |  |
| BT\_AVRCP\_OPID\_RIGHT |  |
| BT\_AVRCP\_OPID\_RIGHT\_UP |  |
| BT\_AVRCP\_OPID\_RIGHT\_DOWN |  |
| BT\_AVRCP\_OPID\_LEFT\_UP |  |
| BT\_AVRCP\_OPID\_LEFT\_DOWN |  |
| BT\_AVRCP\_OPID\_ROOT\_MENU |  |
| BT\_AVRCP\_OPID\_SETUP\_MENU |  |
| BT\_AVRCP\_OPID\_CONTENTS\_MENU |  |
| BT\_AVRCP\_OPID\_FAVORITE\_MENU |  |
| BT\_AVRCP\_OPID\_EXIT |  |
| BT\_AVRCP\_OPID\_0 |  |
| BT\_AVRCP\_OPID\_1 |  |
| BT\_AVRCP\_OPID\_2 |  |
| BT\_AVRCP\_OPID\_3 |  |
| BT\_AVRCP\_OPID\_4 |  |
| BT\_AVRCP\_OPID\_5 |  |
| BT\_AVRCP\_OPID\_6 |  |
| BT\_AVRCP\_OPID\_7 |  |
| BT\_AVRCP\_OPID\_8 |  |
| BT\_AVRCP\_OPID\_9 |  |
| BT\_AVRCP\_OPID\_DOT |  |
| BT\_AVRCP\_OPID\_ENTER |  |
| BT\_AVRCP\_OPID\_CLEAR |  |
| BT\_AVRCP\_OPID\_CHANNEL\_UP |  |
| BT\_AVRCP\_OPID\_CHANNEL\_DOWN |  |
| BT\_AVRCP\_OPID\_PREVIOUS\_CHANNEL |  |
| BT\_AVRCP\_OPID\_SOUND\_SELECT |  |
| BT\_AVRCP\_OPID\_INPUT\_SELECT |  |
| BT\_AVRCP\_OPID\_DISPLAY\_INFORMATION |  |
| BT\_AVRCP\_OPID\_HELP |  |
| BT\_AVRCP\_OPID\_PAGE\_UP |  |
| BT\_AVRCP\_OPID\_PAGE\_DOWN |  |
| BT\_AVRCP\_OPID\_POWER |  |
| BT\_AVRCP\_OPID\_VOLUME\_UP |  |
| BT\_AVRCP\_OPID\_VOLUME\_DOWN |  |
| BT\_AVRCP\_OPID\_MUTE |  |
| BT\_AVRCP\_OPID\_PLAY |  |
| BT\_AVRCP\_OPID\_STOP |  |
| BT\_AVRCP\_OPID\_PAUSE |  |
| BT\_AVRCP\_OPID\_RECORD |  |
| BT\_AVRCP\_OPID\_REWIND |  |
| BT\_AVRCP\_OPID\_FAST\_FORWARD |  |
| BT\_AVRCP\_OPID\_EJECT |  |
| BT\_AVRCP\_OPID\_FORWARD |  |
| BT\_AVRCP\_OPID\_BACKWARD |  |
| BT\_AVRCP\_OPID\_ANGLE |  |
| BT\_AVRCP\_OPID\_SUBPICTURE |  |
| BT\_AVRCP\_OPID\_F1 |  |
| BT\_AVRCP\_OPID\_F2 |  |
| BT\_AVRCP\_OPID\_F3 |  |
| BT\_AVRCP\_OPID\_F4 |  |
| BT\_AVRCP\_OPID\_F5 |  |
| BT\_AVRCP\_OPID\_VENDOR\_UNIQUE |  |

## [◆ ](#aba2d8faec2c3baf7403199ea8a509326)bt\_avrcp\_rsp\_t

| enum [bt\_avrcp\_rsp\_t](#aba2d8faec2c3baf7403199ea8a509326) |
| --- |

AV/C response codes.

| Enumerator | |
| --- | --- |
| BT\_AVRCP\_RSP\_NOT\_IMPLEMENTED |  |
| BT\_AVRCP\_RSP\_ACCEPTED |  |
| BT\_AVRCP\_RSP\_REJECTED |  |
| BT\_AVRCP\_RSP\_IN\_TRANSITION |  |
| BT\_AVRCP\_RSP\_IMPLEMENTED | For SPECIFIC\_INQUIRY and GENERAL\_INQUIRY commands. |
| BT\_AVRCP\_RSP\_STABLE | For STATUS commands. |
| BT\_AVRCP\_RSP\_CHANGED |  |
| BT\_AVRCP\_RSP\_INTERIM |  |

## Function Documentation

## [◆ ](#addc1f4f530b9e3eb4a669fe606479c59)bt\_avrcp\_connect()

| struct bt\_avrcp \* bt\_avrcp\_connect | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

Connect AVRCP.

This function is to be called after the conn parameter is obtained by performing a GAP procedure. The API is to be used to establish AVRCP connection between devices.

Parameters
:   | conn | Pointer to bt\_conn structure. |
    | --- | --- |

Returns
:   pointer to struct bt\_avrcp in case of success or NULL in case of error.

## [◆ ](#af68c54ea0b17ebaa9872d271b0fee9bd)bt\_avrcp\_disconnect()

| int bt\_avrcp\_disconnect | ( | struct bt\_avrcp \* | *avrcp* | ) |  |
| --- | --- | --- | --- | --- | --- |

Disconnect AVRCP.

This function close AVCTP L2CAP connection.

Parameters
:   | avrcp | The AVRCP instance. |
    | --- | --- |

Returns
:   0 in case of success or error code in case of error.

## [◆ ](#a127eaf05867a84fb5183e044fdfb55c0)bt\_avrcp\_get\_subunit\_info()

| int bt\_avrcp\_get\_subunit\_info | ( | struct bt\_avrcp \* | *avrcp* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get AVRCP Subunit Info.

This function obtains information about the subunit(s) of an AV/C unit. A device with AVRCP may support other subunits than the panel subunit if other profiles co-exist in the device.

Parameters
:   | avrcp | The AVRCP instance. |
    | --- | --- |

Returns
:   0 in case of success or error code in case of error.

## [◆ ](#aba521a01fea4e7aee8b40ba72ca10bcf)bt\_avrcp\_get\_unit\_info()

| int bt\_avrcp\_get\_unit\_info | ( | struct bt\_avrcp \* | *avrcp* | ) |  |
| --- | --- | --- | --- | --- | --- |

Get AVRCP Unit Info.

This function obtains information that pertains to the AV/C unit as a whole.

Parameters
:   | avrcp | The AVRCP instance. |
    | --- | --- |

Returns
:   0 in case of success or error code in case of error.

## [◆ ](#afeea270bacac6a59af74c02fc1d98945)bt\_avrcp\_passthrough()

| int bt\_avrcp\_passthrough | ( | struct bt\_avrcp \* | *avrcp*, |
| --- | --- | --- | --- |
|  |  | [bt\_avrcp\_opid\_t](#a3c997d96028343a0a5a4948dabe19b84) | *operation\_id*, |
|  |  | [bt\_avrcp\_button\_state\_t](#a15f9f868b056f17ea12d96530b7da881) | *state*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *payload*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *len* ) |

Send AVRCP Pass Through command.

This function send a pass through command to the remote device. Passsthhrough command is used to transfer user operation information from a CT to Panel subunit of TG.

Parameters
:   | avrcp | The AVRCP instance. |
    | --- | --- |
    | operation\_id | The user operation id. |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | The button state. |
    | payload | The payload of the pass through command. Should not be NULL if len is not zero. |
    | len | The length of the payload. |

Returns
:   0 in case of success or error code in case of error.

## [◆ ](#aedb1bc8dd553aa44fdaec2b9f5c76607)bt\_avrcp\_register\_cb()

| int bt\_avrcp\_register\_cb | ( | const struct [bt\_avrcp\_cb](structbt__avrcp__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

Register callback.

Register AVRCP callbacks to monitor the state and interact with the remote device.

Parameters
:   | cb | The callback function. |
    | --- | --- |

Returns
:   0 in case of success or error code in case of error.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [avrcp.h](avrcp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
