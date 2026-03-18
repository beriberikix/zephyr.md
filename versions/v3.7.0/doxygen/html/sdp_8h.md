---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/sdp_8h.html
original_path: doxygen/html/sdp_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sdp.h File Reference

Service Discovery Protocol handling.
[More...](#details)

`#include <[zephyr/bluetooth/uuid.h](uuid_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`

[Go to the source code of this file.](sdp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_sdp\_data\_elem](structbt__sdp__data__elem.md) |
|  | SDP Generic Data Element Value. [More...](structbt__sdp__data__elem.md#details) |
| struct | [bt\_sdp\_attribute](structbt__sdp__attribute.md) |
|  | SDP Attribute Value. [More...](structbt__sdp__attribute.md#details) |
| struct | [bt\_sdp\_record](structbt__sdp__record.md) |
|  | SDP Service Record Value. [More...](structbt__sdp__record.md#details) |
| struct | [bt\_sdp\_client\_result](structbt__sdp__client__result.md) |
|  | Generic SDP Client Query Result data holder. [More...](structbt__sdp__client__result.md#details) |
| struct | [bt\_sdp\_discover\_params](structbt__sdp__discover__params.md) |
|  | Main user structure used in SDP discovery of remote. [More...](structbt__sdp__discover__params.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_SDP\_SERVER\_RECORD\_HANDLE](group__bt__sdp.md#ga610e7cab0a598f272eeb2838f4c4c996)   0x0000 |
| #define | [BT\_SDP\_PRIMARY\_LANG\_BASE](group__bt__sdp.md#gab502c9288e5f01dfdaaf8390bb3f6e49)   0x0100 |
| #define | [BT\_SDP\_ATTR\_SVCNAME\_PRIMARY](group__bt__sdp.md#ga76737502226c623bf508ae53a6015e08)   (0x0000 + [BT\_SDP\_PRIMARY\_LANG\_BASE](group__bt__sdp.md#gab502c9288e5f01dfdaaf8390bb3f6e49)) |
| #define | [BT\_SDP\_ATTR\_SVCDESC\_PRIMARY](group__bt__sdp.md#ga3e991ec1d5467c0b3ce5d9a7e750a300)   (0x0001 + [BT\_SDP\_PRIMARY\_LANG\_BASE](group__bt__sdp.md#gab502c9288e5f01dfdaaf8390bb3f6e49)) |
| #define | [BT\_SDP\_ATTR\_PROVNAME\_PRIMARY](group__bt__sdp.md#gab8b0110be857d6eca206e00c3b5e373a)   (0x0002 + [BT\_SDP\_PRIMARY\_LANG\_BASE](group__bt__sdp.md#gab502c9288e5f01dfdaaf8390bb3f6e49)) |
| #define | [BT\_SDP\_TYPE\_DESC\_MASK](group__bt__sdp.md#ga3eb2a5501341f6c5186a27219cf27cdf)   0xf8 |
| #define | [BT\_SDP\_SIZE\_DESC\_MASK](group__bt__sdp.md#ga2d1040ccd11d1dd4c697525ebc323243)   0x07 |
| #define | [BT\_SDP\_SIZE\_INDEX\_OFFSET](group__bt__sdp.md#ga6e8f843aeb2d325058214d2a1454737a)   5 |
| #define | [BT\_SDP\_ARRAY\_8](group__bt__sdp.md#gaef264fa3621c3df7a164128bb95b30fc)(...) |
|  | Declare an array of 8-bit elements in an attribute. |
| #define | [BT\_SDP\_ARRAY\_16](group__bt__sdp.md#gaa4bb67164ae1f16b26081668d00f45c7)(...) |
|  | Declare an array of 16-bit elements in an attribute. |
| #define | [BT\_SDP\_ARRAY\_32](group__bt__sdp.md#ga7a17ee4872190a087cf2e5ea4db9e737)(...) |
|  | Declare an array of 32-bit elements in an attribute. |
| #define | [BT\_SDP\_TYPE\_SIZE](group__bt__sdp.md#ga66778ac38fb5b82d3b514fe0da008393)(\_type) |
|  | Declare a fixed-size data element header. |
| #define | [BT\_SDP\_TYPE\_SIZE\_VAR](group__bt__sdp.md#gabbb2bd6a8321513082851fe73dfa44bc)(\_type, \_size) |
|  | Declare a variable-size data element header. |
| #define | [BT\_SDP\_DATA\_ELEM\_LIST](group__bt__sdp.md#gaa2954f3df4d0ee9684721cbc6182e37c)(...) |
|  | Declare a list of data elements. |
| #define | [BT\_SDP\_NEW\_SERVICE](group__bt__sdp.md#gaee13722587e4eb8c4beaaa0abad88fe5) |
|  | SDP New Service Record Declaration Macro. |
| #define | [BT\_SDP\_LIST](group__bt__sdp.md#ga25b31454ee5b5fe23b617b5256ba00c4)(\_att\_id, \_type\_size, \_data\_elem\_seq) |
|  | Generic SDP List Attribute Declaration Macro. |
| #define | [BT\_SDP\_SERVICE\_ID](group__bt__sdp.md#gaa57f3c9a52ae29c02d7577be99f91e7c)(\_uuid) |
|  | SDP Service ID Attribute Declaration Macro. |
| #define | [BT\_SDP\_SERVICE\_NAME](group__bt__sdp.md#ga83de8e62415d3e31b3b5434b9db633d0)(\_name) |
|  | SDP Name Attribute Declaration Macro. |
| #define | [BT\_SDP\_SUPPORTED\_FEATURES](group__bt__sdp.md#ga096c84414b429aa05bed45cf6175361e)(\_features) |
|  | SDP Supported Features Attribute Declaration Macro. |
| #define | [BT\_SDP\_RECORD](group__bt__sdp.md#ga555f10b8f3ae3710c6dda9f37e78547b)(\_attrs) |
|  | SDP Service Declaration Macro. |
| Service class identifiers of standard services and service groups | |
| #define | [BT\_SDP\_SDP\_SERVER\_SVCLASS](group__bt__sdp.md#gac2c2379f8e483939826297dc49657837)   0x1000 |
|  | Service Discovery Server. |
| #define | [BT\_SDP\_BROWSE\_GRP\_DESC\_SVCLASS](group__bt__sdp.md#gabe05780702a9be7da54a8c04f79ad752)   0x1001 |
|  | Browse Group Descriptor. |
| #define | [BT\_SDP\_PUBLIC\_BROWSE\_GROUP](group__bt__sdp.md#ga383233a0ff3159ed653786490a4c06ae)   0x1002 |
|  | Public Browse Group. |
| #define | [BT\_SDP\_SERIAL\_PORT\_SVCLASS](group__bt__sdp.md#gab1234d808a7e347328bf95ad065fd9c4)   0x1101 |
|  | Serial Port. |
| #define | [BT\_SDP\_LAN\_ACCESS\_SVCLASS](group__bt__sdp.md#gaf0199837105ded0d65314e573da6a3ed)   0x1102 |
|  | LAN Access Using PPP. |
| #define | [BT\_SDP\_DIALUP\_NET\_SVCLASS](group__bt__sdp.md#gaab655c1f93029ed64743156734e2519e)   0x1103 |
|  | Dialup Networking. |
| #define | [BT\_SDP\_IRMC\_SYNC\_SVCLASS](group__bt__sdp.md#ga28fc78fc21e4d88569e5ca5727ed6202)   0x1104 |
|  | IrMC Sync. |
| #define | [BT\_SDP\_OBEX\_OBJPUSH\_SVCLASS](group__bt__sdp.md#gaaf64788e0cc6d54a8511c07af22f6740)   0x1105 |
|  | OBEX Object Push. |
| #define | [BT\_SDP\_OBEX\_FILETRANS\_SVCLASS](group__bt__sdp.md#gacd25278a573edcb16aa4b60f8ffad20d)   0x1106 |
|  | OBEX File Transfer. |
| #define | [BT\_SDP\_IRMC\_SYNC\_CMD\_SVCLASS](group__bt__sdp.md#ga39d4ce2465b10c10ee746c1491c49bea)   0x1107 |
|  | IrMC Sync Command. |
| #define | [BT\_SDP\_HEADSET\_SVCLASS](group__bt__sdp.md#ga6eb16aacf468b460fa7675ffc4703e68)   0x1108 |
|  | Headset. |
| #define | [BT\_SDP\_CORDLESS\_TELEPHONY\_SVCLASS](group__bt__sdp.md#ga16e1bc10528ac82f6cec822912f97d8c)   0x1109 |
|  | Cordless Telephony. |
| #define | [BT\_SDP\_AUDIO\_SOURCE\_SVCLASS](group__bt__sdp.md#gafeb3a3184a0b83e0045187cbe3cf24dc)   0x110a |
|  | Audio Source. |
| #define | [BT\_SDP\_AUDIO\_SINK\_SVCLASS](group__bt__sdp.md#gaa0e334873b5477523572caa2359a4098)   0x110b |
|  | Audio Sink. |
| #define | [BT\_SDP\_AV\_REMOTE\_TARGET\_SVCLASS](group__bt__sdp.md#gafe96e9d32797a83c793f0ed278054b80)   0x110c |
|  | A/V Remote Control Target. |
| #define | [BT\_SDP\_ADVANCED\_AUDIO\_SVCLASS](group__bt__sdp.md#ga2fdc3eb32196b5135b7f595a36cacb4c)   0x110d |
|  | Advanced Audio Distribution. |
| #define | [BT\_SDP\_AV\_REMOTE\_SVCLASS](group__bt__sdp.md#gaea94250bed4c5e6ad47749a1237778f5)   0x110e |
|  | A/V Remote Control. |
| #define | [BT\_SDP\_AV\_REMOTE\_CONTROLLER\_SVCLASS](group__bt__sdp.md#gaaae997769dfc8325c38830707f4d22e3)   0x110f |
|  | A/V Remote Control Controller. |
| #define | [BT\_SDP\_INTERCOM\_SVCLASS](group__bt__sdp.md#ga9681e34d78cea87e413fa4be40e4239a)   0x1110 |
|  | Intercom. |
| #define | [BT\_SDP\_FAX\_SVCLASS](group__bt__sdp.md#ga31962fab5bed7c54311c4b291713a836)   0x1111 |
|  | Fax. |
| #define | [BT\_SDP\_HEADSET\_AGW\_SVCLASS](group__bt__sdp.md#ga4c9322cf28a8b1aa96828152e8ee7379)   0x1112 |
|  | Headset AG. |
| #define | [BT\_SDP\_WAP\_SVCLASS](group__bt__sdp.md#ga2ab79d7ff4e88820773cf24f0b0b6e20)   0x1113 |
|  | WAP. |
| #define | [BT\_SDP\_WAP\_CLIENT\_SVCLASS](group__bt__sdp.md#ga22624d29917aaeaa0c281d9517178821)   0x1114 |
|  | WAP Client. |
| #define | [BT\_SDP\_PANU\_SVCLASS](group__bt__sdp.md#gaa9abb444e3b43c1164d6b450b1c066e5)   0x1115 |
|  | Personal Area Networking User. |
| #define | [BT\_SDP\_NAP\_SVCLASS](group__bt__sdp.md#ga78a7be1db8be8d7eece0d17c629dd009)   0x1116 |
|  | Network Access Point. |
| #define | [BT\_SDP\_GN\_SVCLASS](group__bt__sdp.md#gaed2d6f72c344e2e9b9bdcefd23cb4086)   0x1117 |
|  | Group Network. |
| #define | [BT\_SDP\_DIRECT\_PRINTING\_SVCLASS](group__bt__sdp.md#ga30f6edbd67d96f7752a223409c8e4431)   0x1118 |
|  | Direct Printing. |
| #define | [BT\_SDP\_REFERENCE\_PRINTING\_SVCLASS](group__bt__sdp.md#ga6bc247854656613d2fa9b47d55bd69d6)   0x1119 |
|  | Reference Printing. |
| #define | [BT\_SDP\_IMAGING\_SVCLASS](group__bt__sdp.md#ga08730b1fd7088101fadb85e5dc13fd24)   0x111a |
|  | Basic Imaging Profile. |
| #define | [BT\_SDP\_IMAGING\_RESPONDER\_SVCLASS](group__bt__sdp.md#gaf19cd136b780ef303c1290b26ab2ca17)   0x111b |
|  | Imaging Responder. |
| #define | [BT\_SDP\_IMAGING\_ARCHIVE\_SVCLASS](group__bt__sdp.md#ga3f04a28d9764a0c7755babe379c25393)   0x111c |
|  | Imaging Automatic Archive. |
| #define | [BT\_SDP\_IMAGING\_REFOBJS\_SVCLASS](group__bt__sdp.md#ga51a4cfc28f86a650b03a7bbe6e5b883a)   0x111d |
|  | Imaging Referenced Objects. |
| #define | [BT\_SDP\_HANDSFREE\_SVCLASS](group__bt__sdp.md#gab9f99989420545b3b0e71da6c5475f90)   0x111e |
|  | Handsfree. |
| #define | [BT\_SDP\_HANDSFREE\_AGW\_SVCLASS](group__bt__sdp.md#ga1c44ae236a292c91dc81539c9c89947c)   0x111f |
|  | Handsfree Audio Gateway. |
| #define | [BT\_SDP\_DIRECT\_PRT\_REFOBJS\_SVCLASS](group__bt__sdp.md#ga79d34c3b7641cf523adf6515720ceceb)   0x1120 |
|  | Direct Printing Reference Objects Service. |
| #define | [BT\_SDP\_REFLECTED\_UI\_SVCLASS](group__bt__sdp.md#ga78607a42f5228b37d348614b12e48a77)   0x1121 |
|  | Reflected UI. |
| #define | [BT\_SDP\_BASIC\_PRINTING\_SVCLASS](group__bt__sdp.md#gac727f387a55a76c9a071cf62792f50e4)   0x1122 |
|  | Basic Printing. |
| #define | [BT\_SDP\_PRINTING\_STATUS\_SVCLASS](group__bt__sdp.md#ga9298ac73a26a1ab2e53733f404e5c6ea)   0x1123 |
|  | Printing Status. |
| #define | [BT\_SDP\_HID\_SVCLASS](group__bt__sdp.md#gab63eab5791898a47bd540eed4d55cddc)   0x1124 |
|  | Human Interface Device Service. |
| #define | [BT\_SDP\_HCR\_SVCLASS](group__bt__sdp.md#ga873f8e03aeb696d3eb287a8d00796a4f)   0x1125 |
|  | Hardcopy Cable Replacement. |
| #define | [BT\_SDP\_HCR\_PRINT\_SVCLASS](group__bt__sdp.md#ga4ca1e6eb6fe385e526f8d84ed65ab285)   0x1126 |
|  | HCR Print. |
| #define | [BT\_SDP\_HCR\_SCAN\_SVCLASS](group__bt__sdp.md#ga621afe0f5a6d176c26e140c4162bee07)   0x1127 |
|  | HCR Scan. |
| #define | [BT\_SDP\_CIP\_SVCLASS](group__bt__sdp.md#ga9617c02c6999d9fe987e91c6c2dc5dca)   0x1128 |
|  | Common ISDN Access. |
| #define | [BT\_SDP\_VIDEO\_CONF\_GW\_SVCLASS](group__bt__sdp.md#ga3e087c095a78f07efae660eceae9c11e)   0x1129 |
|  | Video Conferencing Gateway. |
| #define | [BT\_SDP\_UDI\_MT\_SVCLASS](group__bt__sdp.md#ga629179357eff2cd60621f0e1e435df06)   0x112a |
|  | UDI MT. |
| #define | [BT\_SDP\_UDI\_TA\_SVCLASS](group__bt__sdp.md#ga846599abf75f1cbb27028aea8a619f31)   0x112b |
|  | UDI TA. |
| #define | [BT\_SDP\_AV\_SVCLASS](group__bt__sdp.md#gab7a8499dbb73a2700389d55d331bd23e)   0x112c |
|  | Audio/Video. |
| #define | [BT\_SDP\_SAP\_SVCLASS](group__bt__sdp.md#gad2234f8e0bce0e6b55d18c7a7c950e1d)   0x112d |
|  | SIM Access. |
| #define | [BT\_SDP\_PBAP\_PCE\_SVCLASS](group__bt__sdp.md#gaec2475b7ba36b860c0f8a9cfc33df4a8)   0x112e |
|  | Phonebook Access Client. |
| #define | [BT\_SDP\_PBAP\_PSE\_SVCLASS](group__bt__sdp.md#ga612bb83e9f08edd163433a5fbe9528fc)   0x112f |
|  | Phonebook Access Server. |
| #define | [BT\_SDP\_PBAP\_SVCLASS](group__bt__sdp.md#ga60a9fad26300c15e988e101f90c06435)   0x1130 |
|  | Phonebook Access. |
| #define | [BT\_SDP\_MAP\_MSE\_SVCLASS](group__bt__sdp.md#ga58f5cc54014e3723720e7c3b7ba82fd8)   0x1132 |
|  | Message Access Server. |
| #define | [BT\_SDP\_MAP\_MCE\_SVCLASS](group__bt__sdp.md#ga47849c599678f7ec48c237b8b36e9cb7)   0x1133 |
|  | Message Notification Server. |
| #define | [BT\_SDP\_MAP\_SVCLASS](group__bt__sdp.md#gaec665050af4cc3affcef3912bb212fc0)   0x1134 |
|  | Message Access Profile. |
| #define | [BT\_SDP\_GNSS\_SVCLASS](group__bt__sdp.md#ga300585062ed9ae05daca226cb3c5440d)   0x1135 |
|  | GNSS. |
| #define | [BT\_SDP\_GNSS\_SERVER\_SVCLASS](group__bt__sdp.md#gacdfb8ca6a776f57a2df38b4a6eaa8403)   0x1136 |
|  | GNSS Server. |
| #define | [BT\_SDP\_MPS\_SC\_SVCLASS](group__bt__sdp.md#ga9cce7e3a576329661b363b102cefa494)   0x113a |
|  | MPS SC. |
| #define | [BT\_SDP\_MPS\_SVCLASS](group__bt__sdp.md#gaf847b2675482d3bb9674f569c3604e40)   0x113b |
|  | MPS. |
| #define | [BT\_SDP\_PNP\_INFO\_SVCLASS](group__bt__sdp.md#gaed5403661e0eb8f798a950bead59369a)   0x1200 |
|  | PnP Information. |
| #define | [BT\_SDP\_GENERIC\_NETWORKING\_SVCLASS](group__bt__sdp.md#ga1b9a169ff4db4fda939cba3ce21f808b)   0x1201 |
|  | Generic Networking. |
| #define | [BT\_SDP\_GENERIC\_FILETRANS\_SVCLASS](group__bt__sdp.md#gaa8e5c423fca1fb0d06504cdc5be276d1)   0x1202 |
|  | Generic File Transfer. |
| #define | [BT\_SDP\_GENERIC\_AUDIO\_SVCLASS](group__bt__sdp.md#gaec7548467ffb686b22a907d05e38f275)   0x1203 |
|  | Generic Audio. |
| #define | [BT\_SDP\_GENERIC\_TELEPHONY\_SVCLASS](group__bt__sdp.md#ga010b005cfdb69c67cfc7e3c5c8426778)   0x1204 |
|  | Generic Telephony. |
| #define | [BT\_SDP\_UPNP\_SVCLASS](group__bt__sdp.md#ga9e7fa3bcf139462a2c33f90b526e1ad1)   0x1205 |
|  | UPnP Service. |
| #define | [BT\_SDP\_UPNP\_IP\_SVCLASS](group__bt__sdp.md#ga102b24708429877c4f37a5008fb176b1)   0x1206 |
|  | UPnP IP Service. |
| #define | [BT\_SDP\_UPNP\_PAN\_SVCLASS](group__bt__sdp.md#ga3f50947a742b24089f86193e773d623b)   0x1300 |
|  | UPnP IP PAN. |
| #define | [BT\_SDP\_UPNP\_LAP\_SVCLASS](group__bt__sdp.md#gad418094573383e6252719abed97d24dd)   0x1301 |
|  | UPnP IP LAP. |
| #define | [BT\_SDP\_UPNP\_L2CAP\_SVCLASS](group__bt__sdp.md#gad4d97c0b664c48bdc0842f92240409c7)   0x1302 |
|  | UPnP IP L2CAP. |
| #define | [BT\_SDP\_VIDEO\_SOURCE\_SVCLASS](group__bt__sdp.md#ga17d7fb3a77ef7266ea2d760fb3696a83)   0x1303 |
|  | Video Source. |
| #define | [BT\_SDP\_VIDEO\_SINK\_SVCLASS](group__bt__sdp.md#ga1e3428b6d0197bd7c9d72154c025e9f5)   0x1304 |
|  | Video Sink. |
| #define | [BT\_SDP\_VIDEO\_DISTRIBUTION\_SVCLASS](group__bt__sdp.md#ga4e2ef8310c9396f9fb7781ab4732f308)   0x1305 |
|  | Video Distribution. |
| #define | [BT\_SDP\_HDP\_SVCLASS](group__bt__sdp.md#gaf8fc80f3b2ff245b7d354aa0488bb42b)   0x1400 |
|  | HDP. |
| #define | [BT\_SDP\_HDP\_SOURCE\_SVCLASS](group__bt__sdp.md#ga87ba9fdf39fb99397a6dec4d92b6e3f1)   0x1401 |
|  | HDP Source. |
| #define | [BT\_SDP\_HDP\_SINK\_SVCLASS](group__bt__sdp.md#ga2125a92c6eb724a63d04188919a12bf1)   0x1402 |
|  | HDP Sink. |
| #define | [BT\_SDP\_GENERIC\_ACCESS\_SVCLASS](group__bt__sdp.md#gae8010af5b12cd1c1b1633a4d2c9f5ab0)   0x1800 |
|  | Generic Access Profile. |
| #define | [BT\_SDP\_GENERIC\_ATTRIB\_SVCLASS](group__bt__sdp.md#gad3f345431526bb713921f4b51c48b056)   0x1801 |
|  | Generic Attribute Profile. |
| #define | [BT\_SDP\_APPLE\_AGENT\_SVCLASS](group__bt__sdp.md#ga694b04c2dae3b06b7fd66640468a5a38)   0x2112 |
|  | Apple Agent. |
| Attribute identifier codes | |
| Possible values for attribute-id are listed below.  See SDP Spec, section "Service Attribute Definitions" for more details. | |
| #define | [BT\_SDP\_ATTR\_RECORD\_HANDLE](group__bt__sdp.md#ga38f32cae462272b51eb4edca0c5c95a2)   0x0000 |
|  | Service Record Handle. |
| #define | [BT\_SDP\_ATTR\_SVCLASS\_ID\_LIST](group__bt__sdp.md#gab5c5be56c54d3f8bd4ac6defff0b1e7c)   0x0001 |
|  | Service Class ID List. |
| #define | [BT\_SDP\_ATTR\_RECORD\_STATE](group__bt__sdp.md#ga4d458591f8eba26feaab1220c49f6a29)   0x0002 |
|  | Service Record State. |
| #define | [BT\_SDP\_ATTR\_SERVICE\_ID](group__bt__sdp.md#gad2149fd761f7ae2ea6ef761ab2545ab4)   0x0003 |
|  | Service ID. |
| #define | [BT\_SDP\_ATTR\_PROTO\_DESC\_LIST](group__bt__sdp.md#ga3e7dad966deab42ff9fa0fd04d3d4514)   0x0004 |
|  | Protocol Descriptor List. |
| #define | [BT\_SDP\_ATTR\_BROWSE\_GRP\_LIST](group__bt__sdp.md#ga2609212bf5400c31351bc3ec5f60a7e1)   0x0005 |
|  | Browse Group List. |
| #define | [BT\_SDP\_ATTR\_LANG\_BASE\_ATTR\_ID\_LIST](group__bt__sdp.md#ga462ec997a81c6b439a24e2de085676ab)   0x0006 |
|  | Language Base Attribute ID List. |
| #define | [BT\_SDP\_ATTR\_SVCINFO\_TTL](group__bt__sdp.md#ga7ef037ed6628aa7354736295e0e4ec77)   0x0007 |
|  | Service Info Time to Live. |
| #define | [BT\_SDP\_ATTR\_SERVICE\_AVAILABILITY](group__bt__sdp.md#gaf55a72ce05def1da08d15a23cee4c5e3)   0x0008 |
|  | Service Availability. |
| #define | [BT\_SDP\_ATTR\_PROFILE\_DESC\_LIST](group__bt__sdp.md#ga0b5b19caa523e4cb9da8a2bfc6eab20a)   0x0009 |
|  | Bluetooth Profile Descriptor List. |
| #define | [BT\_SDP\_ATTR\_DOC\_URL](group__bt__sdp.md#gad8302739bca706f6da851d912ada0f82)   0x000a |
|  | Documentation URL. |
| #define | [BT\_SDP\_ATTR\_CLNT\_EXEC\_URL](group__bt__sdp.md#ga0bc613d68dace4cce7a4eec654f5a1e4)   0x000b |
|  | Client Executable URL. |
| #define | [BT\_SDP\_ATTR\_ICON\_URL](group__bt__sdp.md#ga365048bcb0ad2989aec9dd0d89abbfb9)   0x000c |
|  | Icon URL. |
| #define | [BT\_SDP\_ATTR\_ADD\_PROTO\_DESC\_LIST](group__bt__sdp.md#gaf7f0b2f30ede36cf280bf31c5e76a99c)   0x000d |
|  | Additional Protocol Descriptor List. |
| #define | [BT\_SDP\_ATTR\_GROUP\_ID](group__bt__sdp.md#ga15a104c78357f2353cd49eb858de057d)   0x0200 |
|  | Group ID. |
| #define | [BT\_SDP\_ATTR\_IP\_SUBNET](group__bt__sdp.md#ga23a63b424ab381048cb898ebbdb64a02)   0x0200 |
|  | IP Subnet. |
| #define | [BT\_SDP\_ATTR\_VERSION\_NUM\_LIST](group__bt__sdp.md#gab698c476197acca0d499e39f7f246c66)   0x0200 |
|  | Version Number List. |
| #define | [BT\_SDP\_ATTR\_SUPPORTED\_FEATURES\_LIST](group__bt__sdp.md#ga8a693e5265c7801e3c1125473c31445f)   0x0200 |
|  | Supported Features List. |
| #define | [BT\_SDP\_ATTR\_GOEP\_L2CAP\_PSM](group__bt__sdp.md#gac7583b3d2a0ebc82e5cf2e6705249201)   0x0200 |
|  | GOEP L2CAP PSM. |
| #define | [BT\_SDP\_ATTR\_SVCDB\_STATE](group__bt__sdp.md#gab8fe8881b4470ab3522e710e36470ddb)   0x0201 |
|  | Service Database State. |
| #define | [BT\_SDP\_ATTR\_MPSD\_SCENARIOS](group__bt__sdp.md#ga39b3436f9da303bd2ce1ad38f072ed9f)   0x0200 |
|  | MPSD Scenarios. |
| #define | [BT\_SDP\_ATTR\_MPMD\_SCENARIOS](group__bt__sdp.md#gaa3cc3d9a6ac7375e66b0892631698fd0)   0x0201 |
|  | MPMD Scenarios. |
| #define | [BT\_SDP\_ATTR\_MPS\_DEPENDENCIES](group__bt__sdp.md#ga45795e50564492ac9bce8d6832883741)   0x0202 |
|  | Supported Profiles & Protocols. |
| #define | [BT\_SDP\_ATTR\_SERVICE\_VERSION](group__bt__sdp.md#ga230f70b576c14ba1dbe0cf6eda6220e0)   0x0300 |
|  | Service Version. |
| #define | [BT\_SDP\_ATTR\_EXTERNAL\_NETWORK](group__bt__sdp.md#ga617dc829eb1192cd283bef67a357d75f)   0x0301 |
|  | External Network. |
| #define | [BT\_SDP\_ATTR\_SUPPORTED\_DATA\_STORES\_LIST](group__bt__sdp.md#gae12e2daea8febbbd047c1c3843f56933)   0x0301 |
|  | Supported Data Stores List. |
| #define | [BT\_SDP\_ATTR\_DATA\_EXCHANGE\_SPEC](group__bt__sdp.md#ga4732f83c88de43a90ca3d58a136907b6)   0x0301 |
|  | Data Exchange Specification. |
| #define | [BT\_SDP\_ATTR\_NETWORK](group__bt__sdp.md#ga9c78d47f54e82a51f7d04a6f6c97663c)   0x0301 |
|  | Network. |
| #define | [BT\_SDP\_ATTR\_FAX\_CLASS1\_SUPPORT](group__bt__sdp.md#gaeebfb4a085417db65241b21a27258d84)   0x0302 |
|  | Fax Class 1 Support. |
| #define | [BT\_SDP\_ATTR\_REMOTE\_AUDIO\_VOLUME\_CONTROL](group__bt__sdp.md#gaa122bfee476a8e83346823e23978f7a0)   0x0302 |
|  | Remote Audio Volume Control. |
| #define | [BT\_SDP\_ATTR\_MCAP\_SUPPORTED\_PROCEDURES](group__bt__sdp.md#ga54e285c7a12becef9742093e1777c06b)   0x0302 |
|  | MCAP Supported Procedures. |
| #define | [BT\_SDP\_ATTR\_FAX\_CLASS20\_SUPPORT](group__bt__sdp.md#ga861470cd4b505d074abb727ba72c088a)   0x0303 |
|  | Fax Class 2.0 Support. |
| #define | [BT\_SDP\_ATTR\_SUPPORTED\_FORMATS\_LIST](group__bt__sdp.md#gac12ed37044c3f12c2d41b1fd23eacada)   0x0303 |
|  | Supported Formats List. |
| #define | [BT\_SDP\_ATTR\_FAX\_CLASS2\_SUPPORT](group__bt__sdp.md#ga2475947ccdb9f30ece61a34959fd6ce2)   0x0304 |
|  | Fax Class 2 Support (vendor-specific). |
| #define | [BT\_SDP\_ATTR\_AUDIO\_FEEDBACK\_SUPPORT](group__bt__sdp.md#gac4906f9fa368fbf604830cd5c5fdcb57)   0x0305 |
|  | Audio Feedback Support. |
| #define | [BT\_SDP\_ATTR\_NETWORK\_ADDRESS](group__bt__sdp.md#ga74dacfd7807d7f3ec7a7594a9329f0b2)   0x0306 |
|  | Network Address. |
| #define | [BT\_SDP\_ATTR\_WAP\_GATEWAY](group__bt__sdp.md#ga1ef964c955473601910ee3997b9ce5cd)   0x0307 |
|  | WAP Gateway. |
| #define | [BT\_SDP\_ATTR\_HOMEPAGE\_URL](group__bt__sdp.md#gafeff5e5b60bd47c44f8edbe8ff7e78a0)   0x0308 |
|  | Homepage URL. |
| #define | [BT\_SDP\_ATTR\_WAP\_STACK\_TYPE](group__bt__sdp.md#gae1a3ff84a5588e55258c35ee57d6a5b5)   0x0309 |
|  | WAP Stack Type. |
| #define | [BT\_SDP\_ATTR\_SECURITY\_DESC](group__bt__sdp.md#ga21214c2236a5dca24a45998640761e7b)   0x030a |
|  | Security Description. |
| #define | [BT\_SDP\_ATTR\_NET\_ACCESS\_TYPE](group__bt__sdp.md#ga13851f9f9a5ba8514d20cffbe5eb9f14)   0x030b |
|  | Net Access Type. |
| #define | [BT\_SDP\_ATTR\_MAX\_NET\_ACCESSRATE](group__bt__sdp.md#ga7347caab1c7e8755250567d9d8cc7266)   0x030c |
|  | Max Net Access Rate. |
| #define | [BT\_SDP\_ATTR\_IP4\_SUBNET](group__bt__sdp.md#ga01c0cdb8975484242e6c4b052dabfd91)   0x030d |
|  | IPv4 Subnet. |
| #define | [BT\_SDP\_ATTR\_IP6\_SUBNET](group__bt__sdp.md#ga10b3d4826904489d474af5e9c21c0831)   0x030e |
|  | IPv6 Subnet. |
| #define | [BT\_SDP\_ATTR\_SUPPORTED\_CAPABILITIES](group__bt__sdp.md#ga5347dbc038ac9c259d17c14ed9a812d3)   0x0310 |
|  | BIP Supported Capabilities. |
| #define | [BT\_SDP\_ATTR\_SUPPORTED\_FEATURES](group__bt__sdp.md#ga498d9beaa7877570fe834d854de36fcb)   0x0311 |
|  | BIP Supported Features. |
| #define | [BT\_SDP\_ATTR\_SUPPORTED\_FUNCTIONS](group__bt__sdp.md#gabc7cdfd247da5e2ecfd441c0436471f3)   0x0312 |
|  | BIP Supported Functions. |
| #define | [BT\_SDP\_ATTR\_TOTAL\_IMAGING\_DATA\_CAPACITY](group__bt__sdp.md#gadbce181b739c201070d6abcbdc4139f4)   0x0313 |
|  | BIP Total Imaging Data Capacity. |
| #define | [BT\_SDP\_ATTR\_SUPPORTED\_REPOSITORIES](group__bt__sdp.md#gada3d989d6c8c0664ba0bf998414a0328)   0x0314 |
|  | Supported Repositories. |
| #define | [BT\_SDP\_ATTR\_MAS\_INSTANCE\_ID](group__bt__sdp.md#ga03d653957d68b5d0eeda1fa7c9aa4587)   0x0315 |
|  | MAS Instance ID. |
| #define | [BT\_SDP\_ATTR\_SUPPORTED\_MESSAGE\_TYPES](group__bt__sdp.md#ga41fc674e8571556397135734d28b829a)   0x0316 |
|  | Supported Message Types. |
| #define | [BT\_SDP\_ATTR\_PBAP\_SUPPORTED\_FEATURES](group__bt__sdp.md#gaa681b17ebfe013c196cf372dcd030c6e)   0x0317 |
|  | PBAP Supported Features. |
| #define | [BT\_SDP\_ATTR\_MAP\_SUPPORTED\_FEATURES](group__bt__sdp.md#gaa50f16945c15f7a954c10dbc8fc394bf)   0x0317 |
|  | MAP Supported Features. |
| #define | [BT\_SDP\_ATTR\_SPECIFICATION\_ID](group__bt__sdp.md#ga4af959fbdfe7cee84008642091df948d)   0x0200 |
|  | Specification ID. |
| #define | [BT\_SDP\_ATTR\_VENDOR\_ID](group__bt__sdp.md#gab5c2534491b43cfc9d2c7e8807b29ff2)   0x0201 |
|  | Vendor ID. |
| #define | [BT\_SDP\_ATTR\_PRODUCT\_ID](group__bt__sdp.md#gaac9298efffbcf07303f972a12b50f4b6)   0x0202 |
|  | Product ID. |
| #define | [BT\_SDP\_ATTR\_VERSION](group__bt__sdp.md#gae0f4af728f964ee1c11d86b785575a87)   0x0203 |
|  | Version. |
| #define | [BT\_SDP\_ATTR\_PRIMARY\_RECORD](group__bt__sdp.md#ga0868f7d90e3944f105028868511896cf)   0x0204 |
|  | Primary Record. |
| #define | [BT\_SDP\_ATTR\_VENDOR\_ID\_SOURCE](group__bt__sdp.md#gad0ac4a65c51ccdf4cd128eb8697e56ca)   0x0205 |
|  | Vendor ID Source. |
| #define | [BT\_SDP\_ATTR\_HID\_DEVICE\_RELEASE\_NUMBER](group__bt__sdp.md#gab33be247c7574e985dfb34e3c121dd23)   0x0200 |
|  | HID Device Release Number. |
| #define | [BT\_SDP\_ATTR\_HID\_PARSER\_VERSION](group__bt__sdp.md#ga8bb0a4f69b029048958a1395cc98d285)   0x0201 |
|  | HID Parser Version. |
| #define | [BT\_SDP\_ATTR\_HID\_DEVICE\_SUBCLASS](group__bt__sdp.md#ga43aa99ef47032c04be1bdee571dcfa5c)   0x0202 |
|  | HID Device Subclass. |
| #define | [BT\_SDP\_ATTR\_HID\_COUNTRY\_CODE](group__bt__sdp.md#ga5c06a7b07412b0a319656208700ac48e)   0x0203 |
|  | HID Country Code. |
| #define | [BT\_SDP\_ATTR\_HID\_VIRTUAL\_CABLE](group__bt__sdp.md#ga26ff5394958b41c5a595952992e0bbbe)   0x0204 |
|  | HID Virtual Cable. |
| #define | [BT\_SDP\_ATTR\_HID\_RECONNECT\_INITIATE](group__bt__sdp.md#ga30c601e79bd47f29bcc8325ac19a8391)   0x0205 |
|  | HID Reconnect Initiate. |
| #define | [BT\_SDP\_ATTR\_HID\_DESCRIPTOR\_LIST](group__bt__sdp.md#gaadf6a1c7740d5055e1877142b75d07c2)   0x0206 |
|  | HID Descriptor List. |
| #define | [BT\_SDP\_ATTR\_HID\_LANG\_ID\_BASE\_LIST](group__bt__sdp.md#ga732063505ff39f236b03646f8b7a78c6)   0x0207 |
|  | HID Language ID Base List. |
| #define | [BT\_SDP\_ATTR\_HID\_SDP\_DISABLE](group__bt__sdp.md#ga498779c65f410192862aa288cb1e277f)   0x0208 |
|  | HID SDP Disable. |
| #define | [BT\_SDP\_ATTR\_HID\_BATTERY\_POWER](group__bt__sdp.md#gac92ef24a03422abdc6ca932e0675aa57)   0x0209 |
|  | HID Battery Power. |
| #define | [BT\_SDP\_ATTR\_HID\_REMOTE\_WAKEUP](group__bt__sdp.md#ga4bd0452184af1530887b0a785e30fca7)   0x020a |
|  | HID Remote Wakeup. |
| #define | [BT\_SDP\_ATTR\_HID\_PROFILE\_VERSION](group__bt__sdp.md#gaa792255345fe4f62062a848aebb220c7)   0x020b |
|  | HID Profile Version. |
| #define | [BT\_SDP\_ATTR\_HID\_SUPERVISION\_TIMEOUT](group__bt__sdp.md#ga1cd5f256115ef60736eb1089bf66988c)   0x020c |
|  | HID Supervision Timeout. |
| #define | [BT\_SDP\_ATTR\_HID\_NORMALLY\_CONNECTABLE](group__bt__sdp.md#ga866194b8e0ec3eebe086998ae0c6e2ab)   0x020d |
|  | HID Normally Connectable. |
| #define | [BT\_SDP\_ATTR\_HID\_BOOT\_DEVICE](group__bt__sdp.md#ga511980e049b047618f97ac38a4ea3f4e)   0x020e |
|  | HID Boot Device. |
| The Data representation in SDP PDUs (pps 339, 340 of BT SDP Spec) | |
| These are the exact data type+size descriptor values that go into the PDU buffer.  The datatype (leading 5bits) + size descriptor (last 3 bits) is 8 bits. The size descriptor is critical to extract the right number of bytes for the data value from the PDU.  For most basic types, the datatype+size descriptor is straightforward. However for constructed types and strings, the size of the data is in the next "n" bytes following the 8 bits (datatype+size) descriptor. Exactly what the "n" is specified in the 3 bits of the data size descriptor.  TextString and URLString can be of size 2^{8, 16, 32} bytes DataSequence and DataSequenceAlternates can be of size 2^{8, 16, 32} The size are computed post-facto in the API and are not known apriori. | |
| #define | [BT\_SDP\_DATA\_NIL](group__bt__sdp.md#ga36f257de103356c3ebeb55e23186ed99)   0x00 |
|  | Nil, the null type. |
| #define | [BT\_SDP\_UINT8](group__bt__sdp.md#ga546a46c2aa7eb3306eb46768fb8737a4)   0x08 |
|  | Unsigned 8-bit integer. |
| #define | [BT\_SDP\_UINT16](group__bt__sdp.md#ga1129f3a1364f29c9ce36f6f74ca21327)   0x09 |
|  | Unsigned 16-bit integer. |
| #define | [BT\_SDP\_UINT32](group__bt__sdp.md#ga4f3bcb36dfce975c2d9ab68894a9e49c)   0x0a |
|  | Unsigned 32-bit integer. |
| #define | [BT\_SDP\_UINT64](group__bt__sdp.md#ga11261bf1c63a6d463ed41225c1e1a0c7)   0x0b |
|  | Unsigned 64-bit integer. |
| #define | [BT\_SDP\_UINT128](group__bt__sdp.md#ga9a815c6efe976f29e9f6f35a566245fd)   0x0c |
|  | Unsigned 128-bit integer. |
| #define | [BT\_SDP\_INT8](group__bt__sdp.md#gaeed1818ca1bf762b23ab2bfcd18b8a66)   0x10 |
|  | Signed 8-bit integer. |
| #define | [BT\_SDP\_INT16](group__bt__sdp.md#gaf6a3795d22cff4a522a2225339fb5a57)   0x11 |
|  | Signed 16-bit integer. |
| #define | [BT\_SDP\_INT32](group__bt__sdp.md#ga0ad987ebeac3dab3ef2196f4dfeca1ab)   0x12 |
|  | Signed 32-bit integer. |
| #define | [BT\_SDP\_INT64](group__bt__sdp.md#gaae793fef5690c6013e6e0e34ededb75f)   0x13 |
|  | Signed 64-bit integer. |
| #define | [BT\_SDP\_INT128](group__bt__sdp.md#gaf754bbfd9cdc0e6a2bf7d6c46fab3f29)   0x14 |
|  | Signed 128-bit integer. |
| #define | [BT\_SDP\_UUID\_UNSPEC](group__bt__sdp.md#ga4f829572cca9669a8a96a857874bb022)   0x18 |
|  | UUID, unspecified size. |
| #define | [BT\_SDP\_UUID16](group__bt__sdp.md#ga45598f1c663acd3a3e5a409696cb3d2f)   0x19 |
|  | UUID, 16-bit. |
| #define | [BT\_SDP\_UUID32](group__bt__sdp.md#ga78245bb059feb3ec039e05aba24746e7)   0x1a |
|  | UUID, 32-bit. |
| #define | [BT\_SDP\_UUID128](group__bt__sdp.md#gaadf48ba3e96687fff99ff58789d79a50)   0x1c |
|  | UUID, 128-bit. |
| #define | [BT\_SDP\_TEXT\_STR\_UNSPEC](group__bt__sdp.md#gaca9942a42701cda835a5bf7b7aaf1d75)   0x20 |
|  | Text string, unspecified size. |
| #define | [BT\_SDP\_TEXT\_STR8](group__bt__sdp.md#ga885ace6b1def91f3fa4dd16cb391d2b8)   0x25 |
|  | Text string, 8-bit length. |
| #define | [BT\_SDP\_TEXT\_STR16](group__bt__sdp.md#gaa5301cdac5fc9299837f29b92aa3c10b)   0x26 |
|  | Text string, 16-bit length. |
| #define | [BT\_SDP\_TEXT\_STR32](group__bt__sdp.md#ga29657a21117a3fbe05942778a8d7637e)   0x27 |
|  | Text string, 32-bit length. |
| #define | [BT\_SDP\_BOOL](group__bt__sdp.md#gac48f198f6609fac95db69c09ac69efab)   0x28 |
|  | Boolean. |
| #define | [BT\_SDP\_SEQ\_UNSPEC](group__bt__sdp.md#gaa884191d772bfa24484cb33c0f614334)   0x30 |
|  | Data element sequence, unspecified size. |
| #define | [BT\_SDP\_SEQ8](group__bt__sdp.md#ga5a64e3bec70b40114a3160dbfb1e484b)   0x35 |
|  | Data element sequence, 8-bit length. |
| #define | [BT\_SDP\_SEQ16](group__bt__sdp.md#gadf5b15a0296a872ffefc24bbc90dc45b)   0x36 |
|  | Data element sequence, 16-bit length. |
| #define | [BT\_SDP\_SEQ32](group__bt__sdp.md#ga639e86b5103168917cb7202100e3124d)   0x37 |
|  | Data element sequence, 32-bit length. |
| #define | [BT\_SDP\_ALT\_UNSPEC](group__bt__sdp.md#gaee1bd735929cb2c4bca48cc7663407fd)   0x38 |
|  | Data element alternative, unspecified size. |
| #define | [BT\_SDP\_ALT8](group__bt__sdp.md#gab7460f41f05a418d58f4b6807d84cb40)   0x3d |
|  | Data element alternative, 8-bit length. |
| #define | [BT\_SDP\_ALT16](group__bt__sdp.md#gab976bc87f0dcba0e4bc61575ea04ccc7)   0x3e |
|  | Data element alternative, 16-bit length. |
| #define | [BT\_SDP\_ALT32](group__bt__sdp.md#ga420936f672ae31ca701ae277b69d592a)   0x3f |
|  | Data element alternative, 32-bit length. |
| #define | [BT\_SDP\_URL\_STR\_UNSPEC](group__bt__sdp.md#ga32a7a79422f52b75c2eb2d2eb467dc00)   0x40 |
|  | URL string, unspecified size. |
| #define | [BT\_SDP\_URL\_STR8](group__bt__sdp.md#gafb2a77d6097c8c4cf9f01b7e16df26f1)   0x45 |
|  | URL string, 8-bit length. |
| #define | [BT\_SDP\_URL\_STR16](group__bt__sdp.md#gac1acc712468e5af1f54022ac3551882a)   0x46 |
|  | URL string, 16-bit length. |
| #define | [BT\_SDP\_URL\_STR32](group__bt__sdp.md#ga37476681e9d4eee53b710c44e2da9a2f)   0x47 |
|  | URL string, 32-bit length. |

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [bt\_sdp\_discover\_func\_t](group__bt__sdp.md#gae5fa4166e3b909f9dcaace11b302f98f)) (struct bt\_conn \*conn, struct [bt\_sdp\_client\_result](structbt__sdp__client__result.md) \*result) |
|  | Callback type reporting to user that there is a resolved result on remote for given UUID and the result record buffer can be used by user for further inspection. |

| Enumerations | |
| --- | --- |
| enum | { [BT\_SDP\_DISCOVER\_UUID\_STOP](group__bt__sdp.md#gga278df12ff5def68ca4663defd178582ca990fbea48866b2acb7ccd67391b19636) = 0 , [BT\_SDP\_DISCOVER\_UUID\_CONTINUE](group__bt__sdp.md#gga278df12ff5def68ca4663defd178582ca94e15ea86b69d65ca9c1947d1e2157ef) } |
|  | Helper enum to be used as return value of [bt\_sdp\_discover\_func\_t](group__bt__sdp.md#gae5fa4166e3b909f9dcaace11b302f98f "Callback type reporting to user that there is a resolved result on remote for given UUID and the resu..."). [More...](group__bt__sdp.md#ga278df12ff5def68ca4663defd178582c) |
| enum | [bt\_sdp\_proto](group__bt__sdp.md#gaf01cb8d69aee9e06ab944ceae4d7df7c) { [BT\_SDP\_PROTO\_RFCOMM](group__bt__sdp.md#ggaf01cb8d69aee9e06ab944ceae4d7df7ca1ccc0f7ecd38ef83d6c1bb6afd72d71d) = 0x0003 , [BT\_SDP\_PROTO\_L2CAP](group__bt__sdp.md#ggaf01cb8d69aee9e06ab944ceae4d7df7ca197184aa86b3777edca7c58e3597e688) = 0x0100 } |
|  | Protocols to be asked about specific parameters. [More...](group__bt__sdp.md#gaf01cb8d69aee9e06ab944ceae4d7df7c) |

| Functions | |
| --- | --- |
| int | [bt\_sdp\_register\_service](group__bt__sdp.md#ga6006e3cd593ef793273fb291913790fa) (struct [bt\_sdp\_record](structbt__sdp__record.md) \*service) |
|  | Register a Service Record. |
| int | [bt\_sdp\_discover](group__bt__sdp.md#gaf49c299d269ee7b93d41e6ce71df9f77) (struct bt\_conn \*conn, const struct [bt\_sdp\_discover\_params](structbt__sdp__discover__params.md) \*params) |
|  | Allows user to start SDP discovery session. |
| int | [bt\_sdp\_discover\_cancel](group__bt__sdp.md#ga4659915e85ac2f440d6ea6be71f856fa) (struct bt\_conn \*conn, const struct [bt\_sdp\_discover\_params](structbt__sdp__discover__params.md) \*params) |
|  | Release waiting SDP discovery request. |
| int | [bt\_sdp\_get\_proto\_param](group__bt__sdp.md#gaff14678f465af239ac79d1e34bdb9409) (const struct [net\_buf](structnet__buf.md) \*buf, enum [bt\_sdp\_proto](group__bt__sdp.md#gaf01cb8d69aee9e06ab944ceae4d7df7c) proto, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*param) |
|  | Give to user parameter value related to given stacked protocol UUID. |
| int | [bt\_sdp\_get\_addl\_proto\_param](group__bt__sdp.md#gacfcec85582954a80ba94822175d61092) (const struct [net\_buf](structnet__buf.md) \*buf, enum [bt\_sdp\_proto](group__bt__sdp.md#gaf01cb8d69aee9e06ab944ceae4d7df7c) proto, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) param\_index, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*param) |
|  | Get additional parameter value related to given stacked protocol UUID. |
| int | [bt\_sdp\_get\_profile\_version](group__bt__sdp.md#ga9e7d4bd0a407fe8254410f907db90f00) (const struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) profile, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*version) |
|  | Get profile version. |
| int | [bt\_sdp\_get\_features](group__bt__sdp.md#gae1c3110dfe24a939cc02d998c4699ca7) (const struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*features) |
|  | Get SupportedFeatures attribute value. |

## Detailed Description

Service Discovery Protocol handling.

Service Discovery Protocol (SDP).

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [classic](dir_28cc012f073a9d41ddbe6a63c5d8e2de.md)
- [sdp.h](sdp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
