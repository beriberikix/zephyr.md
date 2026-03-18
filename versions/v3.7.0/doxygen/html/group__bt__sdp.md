---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/group__bt__sdp.html
original_path: doxygen/html/group__bt__sdp.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Service Discovery Protocol (SDP)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

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
| #define | [BT\_SDP\_SERVER\_RECORD\_HANDLE](#ga610e7cab0a598f272eeb2838f4c4c996)   0x0000 |
| #define | [BT\_SDP\_PRIMARY\_LANG\_BASE](#gab502c9288e5f01dfdaaf8390bb3f6e49)   0x0100 |
| #define | [BT\_SDP\_ATTR\_SVCNAME\_PRIMARY](#ga76737502226c623bf508ae53a6015e08)   (0x0000 + [BT\_SDP\_PRIMARY\_LANG\_BASE](#gab502c9288e5f01dfdaaf8390bb3f6e49)) |
| #define | [BT\_SDP\_ATTR\_SVCDESC\_PRIMARY](#ga3e991ec1d5467c0b3ce5d9a7e750a300)   (0x0001 + [BT\_SDP\_PRIMARY\_LANG\_BASE](#gab502c9288e5f01dfdaaf8390bb3f6e49)) |
| #define | [BT\_SDP\_ATTR\_PROVNAME\_PRIMARY](#gab8b0110be857d6eca206e00c3b5e373a)   (0x0002 + [BT\_SDP\_PRIMARY\_LANG\_BASE](#gab502c9288e5f01dfdaaf8390bb3f6e49)) |
| #define | [BT\_SDP\_TYPE\_DESC\_MASK](#ga3eb2a5501341f6c5186a27219cf27cdf)   0xf8 |
| #define | [BT\_SDP\_SIZE\_DESC\_MASK](#ga2d1040ccd11d1dd4c697525ebc323243)   0x07 |
| #define | [BT\_SDP\_SIZE\_INDEX\_OFFSET](#ga6e8f843aeb2d325058214d2a1454737a)   5 |
| #define | [BT\_SDP\_ARRAY\_8](#gaef264fa3621c3df7a164128bb95b30fc)(...) |
|  | Declare an array of 8-bit elements in an attribute. |
| #define | [BT\_SDP\_ARRAY\_16](#gaa4bb67164ae1f16b26081668d00f45c7)(...) |
|  | Declare an array of 16-bit elements in an attribute. |
| #define | [BT\_SDP\_ARRAY\_32](#ga7a17ee4872190a087cf2e5ea4db9e737)(...) |
|  | Declare an array of 32-bit elements in an attribute. |
| #define | [BT\_SDP\_TYPE\_SIZE](#ga66778ac38fb5b82d3b514fe0da008393)(\_type) |
|  | Declare a fixed-size data element header. |
| #define | [BT\_SDP\_TYPE\_SIZE\_VAR](#gabbb2bd6a8321513082851fe73dfa44bc)(\_type, \_size) |
|  | Declare a variable-size data element header. |
| #define | [BT\_SDP\_DATA\_ELEM\_LIST](#gaa2954f3df4d0ee9684721cbc6182e37c)(...) |
|  | Declare a list of data elements. |
| #define | [BT\_SDP\_NEW\_SERVICE](#gaee13722587e4eb8c4beaaa0abad88fe5) |
|  | SDP New Service Record Declaration Macro. |
| #define | [BT\_SDP\_LIST](#ga25b31454ee5b5fe23b617b5256ba00c4)(\_att\_id, \_type\_size, \_data\_elem\_seq) |
|  | Generic SDP List Attribute Declaration Macro. |
| #define | [BT\_SDP\_SERVICE\_ID](#gaa57f3c9a52ae29c02d7577be99f91e7c)(\_uuid) |
|  | SDP Service ID Attribute Declaration Macro. |
| #define | [BT\_SDP\_SERVICE\_NAME](#ga83de8e62415d3e31b3b5434b9db633d0)(\_name) |
|  | SDP Name Attribute Declaration Macro. |
| #define | [BT\_SDP\_SUPPORTED\_FEATURES](#ga096c84414b429aa05bed45cf6175361e)(\_features) |
|  | SDP Supported Features Attribute Declaration Macro. |
| #define | [BT\_SDP\_RECORD](#ga555f10b8f3ae3710c6dda9f37e78547b)(\_attrs) |
|  | SDP Service Declaration Macro. |

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [bt\_sdp\_discover\_func\_t](#gae5fa4166e3b909f9dcaace11b302f98f)) (struct bt\_conn \*conn, struct [bt\_sdp\_client\_result](structbt__sdp__client__result.md) \*result) |
|  | Callback type reporting to user that there is a resolved result on remote for given UUID and the result record buffer can be used by user for further inspection. |

| Enumerations | |
| --- | --- |
| enum | { [BT\_SDP\_DISCOVER\_UUID\_STOP](#gga278df12ff5def68ca4663defd178582ca990fbea48866b2acb7ccd67391b19636) = 0 , [BT\_SDP\_DISCOVER\_UUID\_CONTINUE](#gga278df12ff5def68ca4663defd178582ca94e15ea86b69d65ca9c1947d1e2157ef) } |
|  | Helper enum to be used as return value of [bt\_sdp\_discover\_func\_t](#gae5fa4166e3b909f9dcaace11b302f98f). [More...](#ga278df12ff5def68ca4663defd178582c) |
| enum | [bt\_sdp\_proto](#gaf01cb8d69aee9e06ab944ceae4d7df7c) { [BT\_SDP\_PROTO\_RFCOMM](#ggaf01cb8d69aee9e06ab944ceae4d7df7ca1ccc0f7ecd38ef83d6c1bb6afd72d71d) = 0x0003 , [BT\_SDP\_PROTO\_L2CAP](#ggaf01cb8d69aee9e06ab944ceae4d7df7ca197184aa86b3777edca7c58e3597e688) = 0x0100 } |
|  | Protocols to be asked about specific parameters. [More...](#gaf01cb8d69aee9e06ab944ceae4d7df7c) |

| Functions | |
| --- | --- |
| int | [bt\_sdp\_register\_service](#ga6006e3cd593ef793273fb291913790fa) (struct [bt\_sdp\_record](structbt__sdp__record.md) \*service) |
|  | Register a Service Record. |
| int | [bt\_sdp\_discover](#gaf49c299d269ee7b93d41e6ce71df9f77) (struct bt\_conn \*conn, const struct [bt\_sdp\_discover\_params](structbt__sdp__discover__params.md) \*params) |
|  | Allows user to start SDP discovery session. |
| int | [bt\_sdp\_discover\_cancel](#ga4659915e85ac2f440d6ea6be71f856fa) (struct bt\_conn \*conn, const struct [bt\_sdp\_discover\_params](structbt__sdp__discover__params.md) \*params) |
|  | Release waiting SDP discovery request. |
| int | [bt\_sdp\_get\_proto\_param](#gaff14678f465af239ac79d1e34bdb9409) (const struct [net\_buf](structnet__buf.md) \*buf, enum [bt\_sdp\_proto](#gaf01cb8d69aee9e06ab944ceae4d7df7c) proto, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*param) |
|  | Give to user parameter value related to given stacked protocol UUID. |
| int | [bt\_sdp\_get\_addl\_proto\_param](#gacfcec85582954a80ba94822175d61092) (const struct [net\_buf](structnet__buf.md) \*buf, enum [bt\_sdp\_proto](#gaf01cb8d69aee9e06ab944ceae4d7df7c) proto, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) param\_index, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*param) |
|  | Get additional parameter value related to given stacked protocol UUID. |
| int | [bt\_sdp\_get\_profile\_version](#ga9e7d4bd0a407fe8254410f907db90f00) (const struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) profile, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*version) |
|  | Get profile version. |
| int | [bt\_sdp\_get\_features](#gae1c3110dfe24a939cc02d998c4699ca7) (const struct [net\_buf](structnet__buf.md) \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*features) |
|  | Get SupportedFeatures attribute value. |

| Service class identifiers of standard services and service groups | |
| --- | --- |
| #define | [BT\_SDP\_SDP\_SERVER\_SVCLASS](#gac2c2379f8e483939826297dc49657837)   0x1000 |
|  | Service Discovery Server. |
| #define | [BT\_SDP\_BROWSE\_GRP\_DESC\_SVCLASS](#gabe05780702a9be7da54a8c04f79ad752)   0x1001 |
|  | Browse Group Descriptor. |
| #define | [BT\_SDP\_PUBLIC\_BROWSE\_GROUP](#ga383233a0ff3159ed653786490a4c06ae)   0x1002 |
|  | Public Browse Group. |
| #define | [BT\_SDP\_SERIAL\_PORT\_SVCLASS](#gab1234d808a7e347328bf95ad065fd9c4)   0x1101 |
|  | Serial Port. |
| #define | [BT\_SDP\_LAN\_ACCESS\_SVCLASS](#gaf0199837105ded0d65314e573da6a3ed)   0x1102 |
|  | LAN Access Using PPP. |
| #define | [BT\_SDP\_DIALUP\_NET\_SVCLASS](#gaab655c1f93029ed64743156734e2519e)   0x1103 |
|  | Dialup Networking. |
| #define | [BT\_SDP\_IRMC\_SYNC\_SVCLASS](#ga28fc78fc21e4d88569e5ca5727ed6202)   0x1104 |
|  | IrMC Sync. |
| #define | [BT\_SDP\_OBEX\_OBJPUSH\_SVCLASS](#gaaf64788e0cc6d54a8511c07af22f6740)   0x1105 |
|  | OBEX Object Push. |
| #define | [BT\_SDP\_OBEX\_FILETRANS\_SVCLASS](#gacd25278a573edcb16aa4b60f8ffad20d)   0x1106 |
|  | OBEX File Transfer. |
| #define | [BT\_SDP\_IRMC\_SYNC\_CMD\_SVCLASS](#ga39d4ce2465b10c10ee746c1491c49bea)   0x1107 |
|  | IrMC Sync Command. |
| #define | [BT\_SDP\_HEADSET\_SVCLASS](#ga6eb16aacf468b460fa7675ffc4703e68)   0x1108 |
|  | Headset. |
| #define | [BT\_SDP\_CORDLESS\_TELEPHONY\_SVCLASS](#ga16e1bc10528ac82f6cec822912f97d8c)   0x1109 |
|  | Cordless Telephony. |
| #define | [BT\_SDP\_AUDIO\_SOURCE\_SVCLASS](#gafeb3a3184a0b83e0045187cbe3cf24dc)   0x110a |
|  | Audio Source. |
| #define | [BT\_SDP\_AUDIO\_SINK\_SVCLASS](#gaa0e334873b5477523572caa2359a4098)   0x110b |
|  | Audio Sink. |
| #define | [BT\_SDP\_AV\_REMOTE\_TARGET\_SVCLASS](#gafe96e9d32797a83c793f0ed278054b80)   0x110c |
|  | A/V Remote Control Target. |
| #define | [BT\_SDP\_ADVANCED\_AUDIO\_SVCLASS](#ga2fdc3eb32196b5135b7f595a36cacb4c)   0x110d |
|  | Advanced Audio Distribution. |
| #define | [BT\_SDP\_AV\_REMOTE\_SVCLASS](#gaea94250bed4c5e6ad47749a1237778f5)   0x110e |
|  | A/V Remote Control. |
| #define | [BT\_SDP\_AV\_REMOTE\_CONTROLLER\_SVCLASS](#gaaae997769dfc8325c38830707f4d22e3)   0x110f |
|  | A/V Remote Control Controller. |
| #define | [BT\_SDP\_INTERCOM\_SVCLASS](#ga9681e34d78cea87e413fa4be40e4239a)   0x1110 |
|  | Intercom. |
| #define | [BT\_SDP\_FAX\_SVCLASS](#ga31962fab5bed7c54311c4b291713a836)   0x1111 |
|  | Fax. |
| #define | [BT\_SDP\_HEADSET\_AGW\_SVCLASS](#ga4c9322cf28a8b1aa96828152e8ee7379)   0x1112 |
|  | Headset AG. |
| #define | [BT\_SDP\_WAP\_SVCLASS](#ga2ab79d7ff4e88820773cf24f0b0b6e20)   0x1113 |
|  | WAP. |
| #define | [BT\_SDP\_WAP\_CLIENT\_SVCLASS](#ga22624d29917aaeaa0c281d9517178821)   0x1114 |
|  | WAP Client. |
| #define | [BT\_SDP\_PANU\_SVCLASS](#gaa9abb444e3b43c1164d6b450b1c066e5)   0x1115 |
|  | Personal Area Networking User. |
| #define | [BT\_SDP\_NAP\_SVCLASS](#ga78a7be1db8be8d7eece0d17c629dd009)   0x1116 |
|  | Network Access Point. |
| #define | [BT\_SDP\_GN\_SVCLASS](#gaed2d6f72c344e2e9b9bdcefd23cb4086)   0x1117 |
|  | Group Network. |
| #define | [BT\_SDP\_DIRECT\_PRINTING\_SVCLASS](#ga30f6edbd67d96f7752a223409c8e4431)   0x1118 |
|  | Direct Printing. |
| #define | [BT\_SDP\_REFERENCE\_PRINTING\_SVCLASS](#ga6bc247854656613d2fa9b47d55bd69d6)   0x1119 |
|  | Reference Printing. |
| #define | [BT\_SDP\_IMAGING\_SVCLASS](#ga08730b1fd7088101fadb85e5dc13fd24)   0x111a |
|  | Basic Imaging Profile. |
| #define | [BT\_SDP\_IMAGING\_RESPONDER\_SVCLASS](#gaf19cd136b780ef303c1290b26ab2ca17)   0x111b |
|  | Imaging Responder. |
| #define | [BT\_SDP\_IMAGING\_ARCHIVE\_SVCLASS](#ga3f04a28d9764a0c7755babe379c25393)   0x111c |
|  | Imaging Automatic Archive. |
| #define | [BT\_SDP\_IMAGING\_REFOBJS\_SVCLASS](#ga51a4cfc28f86a650b03a7bbe6e5b883a)   0x111d |
|  | Imaging Referenced Objects. |
| #define | [BT\_SDP\_HANDSFREE\_SVCLASS](#gab9f99989420545b3b0e71da6c5475f90)   0x111e |
|  | Handsfree. |
| #define | [BT\_SDP\_HANDSFREE\_AGW\_SVCLASS](#ga1c44ae236a292c91dc81539c9c89947c)   0x111f |
|  | Handsfree Audio Gateway. |
| #define | [BT\_SDP\_DIRECT\_PRT\_REFOBJS\_SVCLASS](#ga79d34c3b7641cf523adf6515720ceceb)   0x1120 |
|  | Direct Printing Reference Objects Service. |
| #define | [BT\_SDP\_REFLECTED\_UI\_SVCLASS](#ga78607a42f5228b37d348614b12e48a77)   0x1121 |
|  | Reflected UI. |
| #define | [BT\_SDP\_BASIC\_PRINTING\_SVCLASS](#gac727f387a55a76c9a071cf62792f50e4)   0x1122 |
|  | Basic Printing. |
| #define | [BT\_SDP\_PRINTING\_STATUS\_SVCLASS](#ga9298ac73a26a1ab2e53733f404e5c6ea)   0x1123 |
|  | Printing Status. |
| #define | [BT\_SDP\_HID\_SVCLASS](#gab63eab5791898a47bd540eed4d55cddc)   0x1124 |
|  | Human Interface Device Service. |
| #define | [BT\_SDP\_HCR\_SVCLASS](#ga873f8e03aeb696d3eb287a8d00796a4f)   0x1125 |
|  | Hardcopy Cable Replacement. |
| #define | [BT\_SDP\_HCR\_PRINT\_SVCLASS](#ga4ca1e6eb6fe385e526f8d84ed65ab285)   0x1126 |
|  | HCR Print. |
| #define | [BT\_SDP\_HCR\_SCAN\_SVCLASS](#ga621afe0f5a6d176c26e140c4162bee07)   0x1127 |
|  | HCR Scan. |
| #define | [BT\_SDP\_CIP\_SVCLASS](#ga9617c02c6999d9fe987e91c6c2dc5dca)   0x1128 |
|  | Common ISDN Access. |
| #define | [BT\_SDP\_VIDEO\_CONF\_GW\_SVCLASS](#ga3e087c095a78f07efae660eceae9c11e)   0x1129 |
|  | Video Conferencing Gateway. |
| #define | [BT\_SDP\_UDI\_MT\_SVCLASS](#ga629179357eff2cd60621f0e1e435df06)   0x112a |
|  | UDI MT. |
| #define | [BT\_SDP\_UDI\_TA\_SVCLASS](#ga846599abf75f1cbb27028aea8a619f31)   0x112b |
|  | UDI TA. |
| #define | [BT\_SDP\_AV\_SVCLASS](#gab7a8499dbb73a2700389d55d331bd23e)   0x112c |
|  | Audio/Video. |
| #define | [BT\_SDP\_SAP\_SVCLASS](#gad2234f8e0bce0e6b55d18c7a7c950e1d)   0x112d |
|  | SIM Access. |
| #define | [BT\_SDP\_PBAP\_PCE\_SVCLASS](#gaec2475b7ba36b860c0f8a9cfc33df4a8)   0x112e |
|  | Phonebook Access Client. |
| #define | [BT\_SDP\_PBAP\_PSE\_SVCLASS](#ga612bb83e9f08edd163433a5fbe9528fc)   0x112f |
|  | Phonebook Access Server. |
| #define | [BT\_SDP\_PBAP\_SVCLASS](#ga60a9fad26300c15e988e101f90c06435)   0x1130 |
|  | Phonebook Access. |
| #define | [BT\_SDP\_MAP\_MSE\_SVCLASS](#ga58f5cc54014e3723720e7c3b7ba82fd8)   0x1132 |
|  | Message Access Server. |
| #define | [BT\_SDP\_MAP\_MCE\_SVCLASS](#ga47849c599678f7ec48c237b8b36e9cb7)   0x1133 |
|  | Message Notification Server. |
| #define | [BT\_SDP\_MAP\_SVCLASS](#gaec665050af4cc3affcef3912bb212fc0)   0x1134 |
|  | Message Access Profile. |
| #define | [BT\_SDP\_GNSS\_SVCLASS](#ga300585062ed9ae05daca226cb3c5440d)   0x1135 |
|  | GNSS. |
| #define | [BT\_SDP\_GNSS\_SERVER\_SVCLASS](#gacdfb8ca6a776f57a2df38b4a6eaa8403)   0x1136 |
|  | GNSS Server. |
| #define | [BT\_SDP\_MPS\_SC\_SVCLASS](#ga9cce7e3a576329661b363b102cefa494)   0x113a |
|  | MPS SC. |
| #define | [BT\_SDP\_MPS\_SVCLASS](#gaf847b2675482d3bb9674f569c3604e40)   0x113b |
|  | MPS. |
| #define | [BT\_SDP\_PNP\_INFO\_SVCLASS](#gaed5403661e0eb8f798a950bead59369a)   0x1200 |
|  | PnP Information. |
| #define | [BT\_SDP\_GENERIC\_NETWORKING\_SVCLASS](#ga1b9a169ff4db4fda939cba3ce21f808b)   0x1201 |
|  | Generic Networking. |
| #define | [BT\_SDP\_GENERIC\_FILETRANS\_SVCLASS](#gaa8e5c423fca1fb0d06504cdc5be276d1)   0x1202 |
|  | Generic File Transfer. |
| #define | [BT\_SDP\_GENERIC\_AUDIO\_SVCLASS](#gaec7548467ffb686b22a907d05e38f275)   0x1203 |
|  | Generic Audio. |
| #define | [BT\_SDP\_GENERIC\_TELEPHONY\_SVCLASS](#ga010b005cfdb69c67cfc7e3c5c8426778)   0x1204 |
|  | Generic Telephony. |
| #define | [BT\_SDP\_UPNP\_SVCLASS](#ga9e7fa3bcf139462a2c33f90b526e1ad1)   0x1205 |
|  | UPnP Service. |
| #define | [BT\_SDP\_UPNP\_IP\_SVCLASS](#ga102b24708429877c4f37a5008fb176b1)   0x1206 |
|  | UPnP IP Service. |
| #define | [BT\_SDP\_UPNP\_PAN\_SVCLASS](#ga3f50947a742b24089f86193e773d623b)   0x1300 |
|  | UPnP IP PAN. |
| #define | [BT\_SDP\_UPNP\_LAP\_SVCLASS](#gad418094573383e6252719abed97d24dd)   0x1301 |
|  | UPnP IP LAP. |
| #define | [BT\_SDP\_UPNP\_L2CAP\_SVCLASS](#gad4d97c0b664c48bdc0842f92240409c7)   0x1302 |
|  | UPnP IP L2CAP. |
| #define | [BT\_SDP\_VIDEO\_SOURCE\_SVCLASS](#ga17d7fb3a77ef7266ea2d760fb3696a83)   0x1303 |
|  | Video Source. |
| #define | [BT\_SDP\_VIDEO\_SINK\_SVCLASS](#ga1e3428b6d0197bd7c9d72154c025e9f5)   0x1304 |
|  | Video Sink. |
| #define | [BT\_SDP\_VIDEO\_DISTRIBUTION\_SVCLASS](#ga4e2ef8310c9396f9fb7781ab4732f308)   0x1305 |
|  | Video Distribution. |
| #define | [BT\_SDP\_HDP\_SVCLASS](#gaf8fc80f3b2ff245b7d354aa0488bb42b)   0x1400 |
|  | HDP. |
| #define | [BT\_SDP\_HDP\_SOURCE\_SVCLASS](#ga87ba9fdf39fb99397a6dec4d92b6e3f1)   0x1401 |
|  | HDP Source. |
| #define | [BT\_SDP\_HDP\_SINK\_SVCLASS](#ga2125a92c6eb724a63d04188919a12bf1)   0x1402 |
|  | HDP Sink. |
| #define | [BT\_SDP\_GENERIC\_ACCESS\_SVCLASS](#gae8010af5b12cd1c1b1633a4d2c9f5ab0)   0x1800 |
|  | Generic Access Profile. |
| #define | [BT\_SDP\_GENERIC\_ATTRIB\_SVCLASS](#gad3f345431526bb713921f4b51c48b056)   0x1801 |
|  | Generic Attribute Profile. |
| #define | [BT\_SDP\_APPLE\_AGENT\_SVCLASS](#ga694b04c2dae3b06b7fd66640468a5a38)   0x2112 |
|  | Apple Agent. |

| Attribute identifier codes | |
| --- | --- |
| Possible values for attribute-id are listed below.  See SDP Spec, section "Service Attribute Definitions" for more details. | |
| #define | [BT\_SDP\_ATTR\_RECORD\_HANDLE](#ga38f32cae462272b51eb4edca0c5c95a2)   0x0000 |
|  | Service Record Handle. |
| #define | [BT\_SDP\_ATTR\_SVCLASS\_ID\_LIST](#gab5c5be56c54d3f8bd4ac6defff0b1e7c)   0x0001 |
|  | Service Class ID List. |
| #define | [BT\_SDP\_ATTR\_RECORD\_STATE](#ga4d458591f8eba26feaab1220c49f6a29)   0x0002 |
|  | Service Record State. |
| #define | [BT\_SDP\_ATTR\_SERVICE\_ID](#gad2149fd761f7ae2ea6ef761ab2545ab4)   0x0003 |
|  | Service ID. |
| #define | [BT\_SDP\_ATTR\_PROTO\_DESC\_LIST](#ga3e7dad966deab42ff9fa0fd04d3d4514)   0x0004 |
|  | Protocol Descriptor List. |
| #define | [BT\_SDP\_ATTR\_BROWSE\_GRP\_LIST](#ga2609212bf5400c31351bc3ec5f60a7e1)   0x0005 |
|  | Browse Group List. |
| #define | [BT\_SDP\_ATTR\_LANG\_BASE\_ATTR\_ID\_LIST](#ga462ec997a81c6b439a24e2de085676ab)   0x0006 |
|  | Language Base Attribute ID List. |
| #define | [BT\_SDP\_ATTR\_SVCINFO\_TTL](#ga7ef037ed6628aa7354736295e0e4ec77)   0x0007 |
|  | Service Info Time to Live. |
| #define | [BT\_SDP\_ATTR\_SERVICE\_AVAILABILITY](#gaf55a72ce05def1da08d15a23cee4c5e3)   0x0008 |
|  | Service Availability. |
| #define | [BT\_SDP\_ATTR\_PROFILE\_DESC\_LIST](#ga0b5b19caa523e4cb9da8a2bfc6eab20a)   0x0009 |
|  | Bluetooth Profile Descriptor List. |
| #define | [BT\_SDP\_ATTR\_DOC\_URL](#gad8302739bca706f6da851d912ada0f82)   0x000a |
|  | Documentation URL. |
| #define | [BT\_SDP\_ATTR\_CLNT\_EXEC\_URL](#ga0bc613d68dace4cce7a4eec654f5a1e4)   0x000b |
|  | Client Executable URL. |
| #define | [BT\_SDP\_ATTR\_ICON\_URL](#ga365048bcb0ad2989aec9dd0d89abbfb9)   0x000c |
|  | Icon URL. |
| #define | [BT\_SDP\_ATTR\_ADD\_PROTO\_DESC\_LIST](#gaf7f0b2f30ede36cf280bf31c5e76a99c)   0x000d |
|  | Additional Protocol Descriptor List. |
| #define | [BT\_SDP\_ATTR\_GROUP\_ID](#ga15a104c78357f2353cd49eb858de057d)   0x0200 |
|  | Group ID. |
| #define | [BT\_SDP\_ATTR\_IP\_SUBNET](#ga23a63b424ab381048cb898ebbdb64a02)   0x0200 |
|  | IP Subnet. |
| #define | [BT\_SDP\_ATTR\_VERSION\_NUM\_LIST](#gab698c476197acca0d499e39f7f246c66)   0x0200 |
|  | Version Number List. |
| #define | [BT\_SDP\_ATTR\_SUPPORTED\_FEATURES\_LIST](#ga8a693e5265c7801e3c1125473c31445f)   0x0200 |
|  | Supported Features List. |
| #define | [BT\_SDP\_ATTR\_GOEP\_L2CAP\_PSM](#gac7583b3d2a0ebc82e5cf2e6705249201)   0x0200 |
|  | GOEP L2CAP PSM. |
| #define | [BT\_SDP\_ATTR\_SVCDB\_STATE](#gab8fe8881b4470ab3522e710e36470ddb)   0x0201 |
|  | Service Database State. |
| #define | [BT\_SDP\_ATTR\_MPSD\_SCENARIOS](#ga39b3436f9da303bd2ce1ad38f072ed9f)   0x0200 |
|  | MPSD Scenarios. |
| #define | [BT\_SDP\_ATTR\_MPMD\_SCENARIOS](#gaa3cc3d9a6ac7375e66b0892631698fd0)   0x0201 |
|  | MPMD Scenarios. |
| #define | [BT\_SDP\_ATTR\_MPS\_DEPENDENCIES](#ga45795e50564492ac9bce8d6832883741)   0x0202 |
|  | Supported Profiles & Protocols. |
| #define | [BT\_SDP\_ATTR\_SERVICE\_VERSION](#ga230f70b576c14ba1dbe0cf6eda6220e0)   0x0300 |
|  | Service Version. |
| #define | [BT\_SDP\_ATTR\_EXTERNAL\_NETWORK](#ga617dc829eb1192cd283bef67a357d75f)   0x0301 |
|  | External Network. |
| #define | [BT\_SDP\_ATTR\_SUPPORTED\_DATA\_STORES\_LIST](#gae12e2daea8febbbd047c1c3843f56933)   0x0301 |
|  | Supported Data Stores List. |
| #define | [BT\_SDP\_ATTR\_DATA\_EXCHANGE\_SPEC](#ga4732f83c88de43a90ca3d58a136907b6)   0x0301 |
|  | Data Exchange Specification. |
| #define | [BT\_SDP\_ATTR\_NETWORK](#ga9c78d47f54e82a51f7d04a6f6c97663c)   0x0301 |
|  | Network. |
| #define | [BT\_SDP\_ATTR\_FAX\_CLASS1\_SUPPORT](#gaeebfb4a085417db65241b21a27258d84)   0x0302 |
|  | Fax Class 1 Support. |
| #define | [BT\_SDP\_ATTR\_REMOTE\_AUDIO\_VOLUME\_CONTROL](#gaa122bfee476a8e83346823e23978f7a0)   0x0302 |
|  | Remote Audio Volume Control. |
| #define | [BT\_SDP\_ATTR\_MCAP\_SUPPORTED\_PROCEDURES](#ga54e285c7a12becef9742093e1777c06b)   0x0302 |
|  | MCAP Supported Procedures. |
| #define | [BT\_SDP\_ATTR\_FAX\_CLASS20\_SUPPORT](#ga861470cd4b505d074abb727ba72c088a)   0x0303 |
|  | Fax Class 2.0 Support. |
| #define | [BT\_SDP\_ATTR\_SUPPORTED\_FORMATS\_LIST](#gac12ed37044c3f12c2d41b1fd23eacada)   0x0303 |
|  | Supported Formats List. |
| #define | [BT\_SDP\_ATTR\_FAX\_CLASS2\_SUPPORT](#ga2475947ccdb9f30ece61a34959fd6ce2)   0x0304 |
|  | Fax Class 2 Support (vendor-specific). |
| #define | [BT\_SDP\_ATTR\_AUDIO\_FEEDBACK\_SUPPORT](#gac4906f9fa368fbf604830cd5c5fdcb57)   0x0305 |
|  | Audio Feedback Support. |
| #define | [BT\_SDP\_ATTR\_NETWORK\_ADDRESS](#ga74dacfd7807d7f3ec7a7594a9329f0b2)   0x0306 |
|  | Network Address. |
| #define | [BT\_SDP\_ATTR\_WAP\_GATEWAY](#ga1ef964c955473601910ee3997b9ce5cd)   0x0307 |
|  | WAP Gateway. |
| #define | [BT\_SDP\_ATTR\_HOMEPAGE\_URL](#gafeff5e5b60bd47c44f8edbe8ff7e78a0)   0x0308 |
|  | Homepage URL. |
| #define | [BT\_SDP\_ATTR\_WAP\_STACK\_TYPE](#gae1a3ff84a5588e55258c35ee57d6a5b5)   0x0309 |
|  | WAP Stack Type. |
| #define | [BT\_SDP\_ATTR\_SECURITY\_DESC](#ga21214c2236a5dca24a45998640761e7b)   0x030a |
|  | Security Description. |
| #define | [BT\_SDP\_ATTR\_NET\_ACCESS\_TYPE](#ga13851f9f9a5ba8514d20cffbe5eb9f14)   0x030b |
|  | Net Access Type. |
| #define | [BT\_SDP\_ATTR\_MAX\_NET\_ACCESSRATE](#ga7347caab1c7e8755250567d9d8cc7266)   0x030c |
|  | Max Net Access Rate. |
| #define | [BT\_SDP\_ATTR\_IP4\_SUBNET](#ga01c0cdb8975484242e6c4b052dabfd91)   0x030d |
|  | IPv4 Subnet. |
| #define | [BT\_SDP\_ATTR\_IP6\_SUBNET](#ga10b3d4826904489d474af5e9c21c0831)   0x030e |
|  | IPv6 Subnet. |
| #define | [BT\_SDP\_ATTR\_SUPPORTED\_CAPABILITIES](#ga5347dbc038ac9c259d17c14ed9a812d3)   0x0310 |
|  | BIP Supported Capabilities. |
| #define | [BT\_SDP\_ATTR\_SUPPORTED\_FEATURES](#ga498d9beaa7877570fe834d854de36fcb)   0x0311 |
|  | BIP Supported Features. |
| #define | [BT\_SDP\_ATTR\_SUPPORTED\_FUNCTIONS](#gabc7cdfd247da5e2ecfd441c0436471f3)   0x0312 |
|  | BIP Supported Functions. |
| #define | [BT\_SDP\_ATTR\_TOTAL\_IMAGING\_DATA\_CAPACITY](#gadbce181b739c201070d6abcbdc4139f4)   0x0313 |
|  | BIP Total Imaging Data Capacity. |
| #define | [BT\_SDP\_ATTR\_SUPPORTED\_REPOSITORIES](#gada3d989d6c8c0664ba0bf998414a0328)   0x0314 |
|  | Supported Repositories. |
| #define | [BT\_SDP\_ATTR\_MAS\_INSTANCE\_ID](#ga03d653957d68b5d0eeda1fa7c9aa4587)   0x0315 |
|  | MAS Instance ID. |
| #define | [BT\_SDP\_ATTR\_SUPPORTED\_MESSAGE\_TYPES](#ga41fc674e8571556397135734d28b829a)   0x0316 |
|  | Supported Message Types. |
| #define | [BT\_SDP\_ATTR\_PBAP\_SUPPORTED\_FEATURES](#gaa681b17ebfe013c196cf372dcd030c6e)   0x0317 |
|  | PBAP Supported Features. |
| #define | [BT\_SDP\_ATTR\_MAP\_SUPPORTED\_FEATURES](#gaa50f16945c15f7a954c10dbc8fc394bf)   0x0317 |
|  | MAP Supported Features. |
| #define | [BT\_SDP\_ATTR\_SPECIFICATION\_ID](#ga4af959fbdfe7cee84008642091df948d)   0x0200 |
|  | Specification ID. |
| #define | [BT\_SDP\_ATTR\_VENDOR\_ID](#gab5c2534491b43cfc9d2c7e8807b29ff2)   0x0201 |
|  | Vendor ID. |
| #define | [BT\_SDP\_ATTR\_PRODUCT\_ID](#gaac9298efffbcf07303f972a12b50f4b6)   0x0202 |
|  | Product ID. |
| #define | [BT\_SDP\_ATTR\_VERSION](#gae0f4af728f964ee1c11d86b785575a87)   0x0203 |
|  | Version. |
| #define | [BT\_SDP\_ATTR\_PRIMARY\_RECORD](#ga0868f7d90e3944f105028868511896cf)   0x0204 |
|  | Primary Record. |
| #define | [BT\_SDP\_ATTR\_VENDOR\_ID\_SOURCE](#gad0ac4a65c51ccdf4cd128eb8697e56ca)   0x0205 |
|  | Vendor ID Source. |
| #define | [BT\_SDP\_ATTR\_HID\_DEVICE\_RELEASE\_NUMBER](#gab33be247c7574e985dfb34e3c121dd23)   0x0200 |
|  | HID Device Release Number. |
| #define | [BT\_SDP\_ATTR\_HID\_PARSER\_VERSION](#ga8bb0a4f69b029048958a1395cc98d285)   0x0201 |
|  | HID Parser Version. |
| #define | [BT\_SDP\_ATTR\_HID\_DEVICE\_SUBCLASS](#ga43aa99ef47032c04be1bdee571dcfa5c)   0x0202 |
|  | HID Device Subclass. |
| #define | [BT\_SDP\_ATTR\_HID\_COUNTRY\_CODE](#ga5c06a7b07412b0a319656208700ac48e)   0x0203 |
|  | HID Country Code. |
| #define | [BT\_SDP\_ATTR\_HID\_VIRTUAL\_CABLE](#ga26ff5394958b41c5a595952992e0bbbe)   0x0204 |
|  | HID Virtual Cable. |
| #define | [BT\_SDP\_ATTR\_HID\_RECONNECT\_INITIATE](#ga30c601e79bd47f29bcc8325ac19a8391)   0x0205 |
|  | HID Reconnect Initiate. |
| #define | [BT\_SDP\_ATTR\_HID\_DESCRIPTOR\_LIST](#gaadf6a1c7740d5055e1877142b75d07c2)   0x0206 |
|  | HID Descriptor List. |
| #define | [BT\_SDP\_ATTR\_HID\_LANG\_ID\_BASE\_LIST](#ga732063505ff39f236b03646f8b7a78c6)   0x0207 |
|  | HID Language ID Base List. |
| #define | [BT\_SDP\_ATTR\_HID\_SDP\_DISABLE](#ga498779c65f410192862aa288cb1e277f)   0x0208 |
|  | HID SDP Disable. |
| #define | [BT\_SDP\_ATTR\_HID\_BATTERY\_POWER](#gac92ef24a03422abdc6ca932e0675aa57)   0x0209 |
|  | HID Battery Power. |
| #define | [BT\_SDP\_ATTR\_HID\_REMOTE\_WAKEUP](#ga4bd0452184af1530887b0a785e30fca7)   0x020a |
|  | HID Remote Wakeup. |
| #define | [BT\_SDP\_ATTR\_HID\_PROFILE\_VERSION](#gaa792255345fe4f62062a848aebb220c7)   0x020b |
|  | HID Profile Version. |
| #define | [BT\_SDP\_ATTR\_HID\_SUPERVISION\_TIMEOUT](#ga1cd5f256115ef60736eb1089bf66988c)   0x020c |
|  | HID Supervision Timeout. |
| #define | [BT\_SDP\_ATTR\_HID\_NORMALLY\_CONNECTABLE](#ga866194b8e0ec3eebe086998ae0c6e2ab)   0x020d |
|  | HID Normally Connectable. |
| #define | [BT\_SDP\_ATTR\_HID\_BOOT\_DEVICE](#ga511980e049b047618f97ac38a4ea3f4e)   0x020e |
|  | HID Boot Device. |

| The Data representation in SDP PDUs (pps 339, 340 of BT SDP Spec) | |
| --- | --- |
| These are the exact data type+size descriptor values that go into the PDU buffer.  The datatype (leading 5bits) + size descriptor (last 3 bits) is 8 bits. The size descriptor is critical to extract the right number of bytes for the data value from the PDU.  For most basic types, the datatype+size descriptor is straightforward. However for constructed types and strings, the size of the data is in the next "n" bytes following the 8 bits (datatype+size) descriptor. Exactly what the "n" is specified in the 3 bits of the data size descriptor.  TextString and URLString can be of size 2^{8, 16, 32} bytes DataSequence and DataSequenceAlternates can be of size 2^{8, 16, 32} The size are computed post-facto in the API and are not known apriori. | |
| #define | [BT\_SDP\_DATA\_NIL](#ga36f257de103356c3ebeb55e23186ed99)   0x00 |
|  | Nil, the null type. |
| #define | [BT\_SDP\_UINT8](#ga546a46c2aa7eb3306eb46768fb8737a4)   0x08 |
|  | Unsigned 8-bit integer. |
| #define | [BT\_SDP\_UINT16](#ga1129f3a1364f29c9ce36f6f74ca21327)   0x09 |
|  | Unsigned 16-bit integer. |
| #define | [BT\_SDP\_UINT32](#ga4f3bcb36dfce975c2d9ab68894a9e49c)   0x0a |
|  | Unsigned 32-bit integer. |
| #define | [BT\_SDP\_UINT64](#ga11261bf1c63a6d463ed41225c1e1a0c7)   0x0b |
|  | Unsigned 64-bit integer. |
| #define | [BT\_SDP\_UINT128](#ga9a815c6efe976f29e9f6f35a566245fd)   0x0c |
|  | Unsigned 128-bit integer. |
| #define | [BT\_SDP\_INT8](#gaeed1818ca1bf762b23ab2bfcd18b8a66)   0x10 |
|  | Signed 8-bit integer. |
| #define | [BT\_SDP\_INT16](#gaf6a3795d22cff4a522a2225339fb5a57)   0x11 |
|  | Signed 16-bit integer. |
| #define | [BT\_SDP\_INT32](#ga0ad987ebeac3dab3ef2196f4dfeca1ab)   0x12 |
|  | Signed 32-bit integer. |
| #define | [BT\_SDP\_INT64](#gaae793fef5690c6013e6e0e34ededb75f)   0x13 |
|  | Signed 64-bit integer. |
| #define | [BT\_SDP\_INT128](#gaf754bbfd9cdc0e6a2bf7d6c46fab3f29)   0x14 |
|  | Signed 128-bit integer. |
| #define | [BT\_SDP\_UUID\_UNSPEC](#ga4f829572cca9669a8a96a857874bb022)   0x18 |
|  | UUID, unspecified size. |
| #define | [BT\_SDP\_UUID16](#ga45598f1c663acd3a3e5a409696cb3d2f)   0x19 |
|  | UUID, 16-bit. |
| #define | [BT\_SDP\_UUID32](#ga78245bb059feb3ec039e05aba24746e7)   0x1a |
|  | UUID, 32-bit. |
| #define | [BT\_SDP\_UUID128](#gaadf48ba3e96687fff99ff58789d79a50)   0x1c |
|  | UUID, 128-bit. |
| #define | [BT\_SDP\_TEXT\_STR\_UNSPEC](#gaca9942a42701cda835a5bf7b7aaf1d75)   0x20 |
|  | Text string, unspecified size. |
| #define | [BT\_SDP\_TEXT\_STR8](#ga885ace6b1def91f3fa4dd16cb391d2b8)   0x25 |
|  | Text string, 8-bit length. |
| #define | [BT\_SDP\_TEXT\_STR16](#gaa5301cdac5fc9299837f29b92aa3c10b)   0x26 |
|  | Text string, 16-bit length. |
| #define | [BT\_SDP\_TEXT\_STR32](#ga29657a21117a3fbe05942778a8d7637e)   0x27 |
|  | Text string, 32-bit length. |
| #define | [BT\_SDP\_BOOL](#gac48f198f6609fac95db69c09ac69efab)   0x28 |
|  | Boolean. |
| #define | [BT\_SDP\_SEQ\_UNSPEC](#gaa884191d772bfa24484cb33c0f614334)   0x30 |
|  | Data element sequence, unspecified size. |
| #define | [BT\_SDP\_SEQ8](#ga5a64e3bec70b40114a3160dbfb1e484b)   0x35 |
|  | Data element sequence, 8-bit length. |
| #define | [BT\_SDP\_SEQ16](#gadf5b15a0296a872ffefc24bbc90dc45b)   0x36 |
|  | Data element sequence, 16-bit length. |
| #define | [BT\_SDP\_SEQ32](#ga639e86b5103168917cb7202100e3124d)   0x37 |
|  | Data element sequence, 32-bit length. |
| #define | [BT\_SDP\_ALT\_UNSPEC](#gaee1bd735929cb2c4bca48cc7663407fd)   0x38 |
|  | Data element alternative, unspecified size. |
| #define | [BT\_SDP\_ALT8](#gab7460f41f05a418d58f4b6807d84cb40)   0x3d |
|  | Data element alternative, 8-bit length. |
| #define | [BT\_SDP\_ALT16](#gab976bc87f0dcba0e4bc61575ea04ccc7)   0x3e |
|  | Data element alternative, 16-bit length. |
| #define | [BT\_SDP\_ALT32](#ga420936f672ae31ca701ae277b69d592a)   0x3f |
|  | Data element alternative, 32-bit length. |
| #define | [BT\_SDP\_URL\_STR\_UNSPEC](#ga32a7a79422f52b75c2eb2d2eb467dc00)   0x40 |
|  | URL string, unspecified size. |
| #define | [BT\_SDP\_URL\_STR8](#gafb2a77d6097c8c4cf9f01b7e16df26f1)   0x45 |
|  | URL string, 8-bit length. |
| #define | [BT\_SDP\_URL\_STR16](#gac1acc712468e5af1f54022ac3551882a)   0x46 |
|  | URL string, 16-bit length. |
| #define | [BT\_SDP\_URL\_STR32](#ga37476681e9d4eee53b710c44e2da9a2f)   0x47 |
|  | URL string, 32-bit length. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga2fdc3eb32196b5135b7f595a36cacb4c)BT\_SDP\_ADVANCED\_AUDIO\_SVCLASS

| #define BT\_SDP\_ADVANCED\_AUDIO\_SVCLASS   0x110d |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Advanced Audio Distribution.

## [◆ ](#gab976bc87f0dcba0e4bc61575ea04ccc7)BT\_SDP\_ALT16

| #define BT\_SDP\_ALT16   0x3e |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Data element alternative, 16-bit length.

## [◆ ](#ga420936f672ae31ca701ae277b69d592a)BT\_SDP\_ALT32

| #define BT\_SDP\_ALT32   0x3f |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Data element alternative, 32-bit length.

## [◆ ](#gab7460f41f05a418d58f4b6807d84cb40)BT\_SDP\_ALT8

| #define BT\_SDP\_ALT8   0x3d |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Data element alternative, 8-bit length.

## [◆ ](#gaee1bd735929cb2c4bca48cc7663407fd)BT\_SDP\_ALT\_UNSPEC

| #define BT\_SDP\_ALT\_UNSPEC   0x38 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Data element alternative, unspecified size.

## [◆ ](#ga694b04c2dae3b06b7fd66640468a5a38)BT\_SDP\_APPLE\_AGENT\_SVCLASS

| #define BT\_SDP\_APPLE\_AGENT\_SVCLASS   0x2112 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Apple Agent.

## [◆ ](#gaa4bb67164ae1f16b26081668d00f45c7)BT\_SDP\_ARRAY\_16

| #define BT\_SDP\_ARRAY\_16 | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sdp.h](sdp_8h.md)>`

**Value:**

(([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)[]) {\_\_VA\_ARGS\_\_})

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

Declare an array of 16-bit elements in an attribute.

## [◆ ](#ga7a17ee4872190a087cf2e5ea4db9e737)BT\_SDP\_ARRAY\_32

| #define BT\_SDP\_ARRAY\_32 | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sdp.h](sdp_8h.md)>`

**Value:**

(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)[]) {\_\_VA\_ARGS\_\_})

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

Declare an array of 32-bit elements in an attribute.

## [◆ ](#gaef264fa3621c3df7a164128bb95b30fc)BT\_SDP\_ARRAY\_8

| #define BT\_SDP\_ARRAY\_8 | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sdp.h](sdp_8h.md)>`

**Value:**

(([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)[]) {\_\_VA\_ARGS\_\_})

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

Declare an array of 8-bit elements in an attribute.

## [◆ ](#gaf7f0b2f30ede36cf280bf31c5e76a99c)BT\_SDP\_ATTR\_ADD\_PROTO\_DESC\_LIST

| #define BT\_SDP\_ATTR\_ADD\_PROTO\_DESC\_LIST   0x000d |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Additional Protocol Descriptor List.

## [◆ ](#gac4906f9fa368fbf604830cd5c5fdcb57)BT\_SDP\_ATTR\_AUDIO\_FEEDBACK\_SUPPORT

| #define BT\_SDP\_ATTR\_AUDIO\_FEEDBACK\_SUPPORT   0x0305 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Audio Feedback Support.

## [◆ ](#ga2609212bf5400c31351bc3ec5f60a7e1)BT\_SDP\_ATTR\_BROWSE\_GRP\_LIST

| #define BT\_SDP\_ATTR\_BROWSE\_GRP\_LIST   0x0005 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Browse Group List.

## [◆ ](#ga0bc613d68dace4cce7a4eec654f5a1e4)BT\_SDP\_ATTR\_CLNT\_EXEC\_URL

| #define BT\_SDP\_ATTR\_CLNT\_EXEC\_URL   0x000b |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Client Executable URL.

## [◆ ](#ga4732f83c88de43a90ca3d58a136907b6)BT\_SDP\_ATTR\_DATA\_EXCHANGE\_SPEC

| #define BT\_SDP\_ATTR\_DATA\_EXCHANGE\_SPEC   0x0301 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Data Exchange Specification.

## [◆ ](#gad8302739bca706f6da851d912ada0f82)BT\_SDP\_ATTR\_DOC\_URL

| #define BT\_SDP\_ATTR\_DOC\_URL   0x000a |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Documentation URL.

## [◆ ](#ga617dc829eb1192cd283bef67a357d75f)BT\_SDP\_ATTR\_EXTERNAL\_NETWORK

| #define BT\_SDP\_ATTR\_EXTERNAL\_NETWORK   0x0301 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

External Network.

## [◆ ](#gaeebfb4a085417db65241b21a27258d84)BT\_SDP\_ATTR\_FAX\_CLASS1\_SUPPORT

| #define BT\_SDP\_ATTR\_FAX\_CLASS1\_SUPPORT   0x0302 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Fax Class 1 Support.

## [◆ ](#ga861470cd4b505d074abb727ba72c088a)BT\_SDP\_ATTR\_FAX\_CLASS20\_SUPPORT

| #define BT\_SDP\_ATTR\_FAX\_CLASS20\_SUPPORT   0x0303 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Fax Class 2.0 Support.

## [◆ ](#ga2475947ccdb9f30ece61a34959fd6ce2)BT\_SDP\_ATTR\_FAX\_CLASS2\_SUPPORT

| #define BT\_SDP\_ATTR\_FAX\_CLASS2\_SUPPORT   0x0304 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Fax Class 2 Support (vendor-specific).

## [◆ ](#gac7583b3d2a0ebc82e5cf2e6705249201)BT\_SDP\_ATTR\_GOEP\_L2CAP\_PSM

| #define BT\_SDP\_ATTR\_GOEP\_L2CAP\_PSM   0x0200 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

GOEP L2CAP PSM.

## [◆ ](#ga15a104c78357f2353cd49eb858de057d)BT\_SDP\_ATTR\_GROUP\_ID

| #define BT\_SDP\_ATTR\_GROUP\_ID   0x0200 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Group ID.

## [◆ ](#gac92ef24a03422abdc6ca932e0675aa57)BT\_SDP\_ATTR\_HID\_BATTERY\_POWER

| #define BT\_SDP\_ATTR\_HID\_BATTERY\_POWER   0x0209 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HID Battery Power.

## [◆ ](#ga511980e049b047618f97ac38a4ea3f4e)BT\_SDP\_ATTR\_HID\_BOOT\_DEVICE

| #define BT\_SDP\_ATTR\_HID\_BOOT\_DEVICE   0x020e |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HID Boot Device.

## [◆ ](#ga5c06a7b07412b0a319656208700ac48e)BT\_SDP\_ATTR\_HID\_COUNTRY\_CODE

| #define BT\_SDP\_ATTR\_HID\_COUNTRY\_CODE   0x0203 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HID Country Code.

## [◆ ](#gaadf6a1c7740d5055e1877142b75d07c2)BT\_SDP\_ATTR\_HID\_DESCRIPTOR\_LIST

| #define BT\_SDP\_ATTR\_HID\_DESCRIPTOR\_LIST   0x0206 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HID Descriptor List.

## [◆ ](#gab33be247c7574e985dfb34e3c121dd23)BT\_SDP\_ATTR\_HID\_DEVICE\_RELEASE\_NUMBER

| #define BT\_SDP\_ATTR\_HID\_DEVICE\_RELEASE\_NUMBER   0x0200 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HID Device Release Number.

## [◆ ](#ga43aa99ef47032c04be1bdee571dcfa5c)BT\_SDP\_ATTR\_HID\_DEVICE\_SUBCLASS

| #define BT\_SDP\_ATTR\_HID\_DEVICE\_SUBCLASS   0x0202 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HID Device Subclass.

## [◆ ](#ga732063505ff39f236b03646f8b7a78c6)BT\_SDP\_ATTR\_HID\_LANG\_ID\_BASE\_LIST

| #define BT\_SDP\_ATTR\_HID\_LANG\_ID\_BASE\_LIST   0x0207 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HID Language ID Base List.

## [◆ ](#ga866194b8e0ec3eebe086998ae0c6e2ab)BT\_SDP\_ATTR\_HID\_NORMALLY\_CONNECTABLE

| #define BT\_SDP\_ATTR\_HID\_NORMALLY\_CONNECTABLE   0x020d |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HID Normally Connectable.

## [◆ ](#ga8bb0a4f69b029048958a1395cc98d285)BT\_SDP\_ATTR\_HID\_PARSER\_VERSION

| #define BT\_SDP\_ATTR\_HID\_PARSER\_VERSION   0x0201 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HID Parser Version.

## [◆ ](#gaa792255345fe4f62062a848aebb220c7)BT\_SDP\_ATTR\_HID\_PROFILE\_VERSION

| #define BT\_SDP\_ATTR\_HID\_PROFILE\_VERSION   0x020b |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HID Profile Version.

## [◆ ](#ga30c601e79bd47f29bcc8325ac19a8391)BT\_SDP\_ATTR\_HID\_RECONNECT\_INITIATE

| #define BT\_SDP\_ATTR\_HID\_RECONNECT\_INITIATE   0x0205 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HID Reconnect Initiate.

## [◆ ](#ga4bd0452184af1530887b0a785e30fca7)BT\_SDP\_ATTR\_HID\_REMOTE\_WAKEUP

| #define BT\_SDP\_ATTR\_HID\_REMOTE\_WAKEUP   0x020a |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HID Remote Wakeup.

## [◆ ](#ga498779c65f410192862aa288cb1e277f)BT\_SDP\_ATTR\_HID\_SDP\_DISABLE

| #define BT\_SDP\_ATTR\_HID\_SDP\_DISABLE   0x0208 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HID SDP Disable.

## [◆ ](#ga1cd5f256115ef60736eb1089bf66988c)BT\_SDP\_ATTR\_HID\_SUPERVISION\_TIMEOUT

| #define BT\_SDP\_ATTR\_HID\_SUPERVISION\_TIMEOUT   0x020c |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HID Supervision Timeout.

## [◆ ](#ga26ff5394958b41c5a595952992e0bbbe)BT\_SDP\_ATTR\_HID\_VIRTUAL\_CABLE

| #define BT\_SDP\_ATTR\_HID\_VIRTUAL\_CABLE   0x0204 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HID Virtual Cable.

## [◆ ](#gafeff5e5b60bd47c44f8edbe8ff7e78a0)BT\_SDP\_ATTR\_HOMEPAGE\_URL

| #define BT\_SDP\_ATTR\_HOMEPAGE\_URL   0x0308 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Homepage URL.

## [◆ ](#ga365048bcb0ad2989aec9dd0d89abbfb9)BT\_SDP\_ATTR\_ICON\_URL

| #define BT\_SDP\_ATTR\_ICON\_URL   0x000c |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Icon URL.

## [◆ ](#ga01c0cdb8975484242e6c4b052dabfd91)BT\_SDP\_ATTR\_IP4\_SUBNET

| #define BT\_SDP\_ATTR\_IP4\_SUBNET   0x030d |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

IPv4 Subnet.

## [◆ ](#ga10b3d4826904489d474af5e9c21c0831)BT\_SDP\_ATTR\_IP6\_SUBNET

| #define BT\_SDP\_ATTR\_IP6\_SUBNET   0x030e |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

IPv6 Subnet.

## [◆ ](#ga23a63b424ab381048cb898ebbdb64a02)BT\_SDP\_ATTR\_IP\_SUBNET

| #define BT\_SDP\_ATTR\_IP\_SUBNET   0x0200 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

IP Subnet.

## [◆ ](#ga462ec997a81c6b439a24e2de085676ab)BT\_SDP\_ATTR\_LANG\_BASE\_ATTR\_ID\_LIST

| #define BT\_SDP\_ATTR\_LANG\_BASE\_ATTR\_ID\_LIST   0x0006 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Language Base Attribute ID List.

## [◆ ](#gaa50f16945c15f7a954c10dbc8fc394bf)BT\_SDP\_ATTR\_MAP\_SUPPORTED\_FEATURES

| #define BT\_SDP\_ATTR\_MAP\_SUPPORTED\_FEATURES   0x0317 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

MAP Supported Features.

## [◆ ](#ga03d653957d68b5d0eeda1fa7c9aa4587)BT\_SDP\_ATTR\_MAS\_INSTANCE\_ID

| #define BT\_SDP\_ATTR\_MAS\_INSTANCE\_ID   0x0315 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

MAS Instance ID.

## [◆ ](#ga7347caab1c7e8755250567d9d8cc7266)BT\_SDP\_ATTR\_MAX\_NET\_ACCESSRATE

| #define BT\_SDP\_ATTR\_MAX\_NET\_ACCESSRATE   0x030c |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Max Net Access Rate.

## [◆ ](#ga54e285c7a12becef9742093e1777c06b)BT\_SDP\_ATTR\_MCAP\_SUPPORTED\_PROCEDURES

| #define BT\_SDP\_ATTR\_MCAP\_SUPPORTED\_PROCEDURES   0x0302 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

MCAP Supported Procedures.

## [◆ ](#gaa3cc3d9a6ac7375e66b0892631698fd0)BT\_SDP\_ATTR\_MPMD\_SCENARIOS

| #define BT\_SDP\_ATTR\_MPMD\_SCENARIOS   0x0201 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

MPMD Scenarios.

## [◆ ](#ga45795e50564492ac9bce8d6832883741)BT\_SDP\_ATTR\_MPS\_DEPENDENCIES

| #define BT\_SDP\_ATTR\_MPS\_DEPENDENCIES   0x0202 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Supported Profiles & Protocols.

## [◆ ](#ga39b3436f9da303bd2ce1ad38f072ed9f)BT\_SDP\_ATTR\_MPSD\_SCENARIOS

| #define BT\_SDP\_ATTR\_MPSD\_SCENARIOS   0x0200 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

MPSD Scenarios.

## [◆ ](#ga13851f9f9a5ba8514d20cffbe5eb9f14)BT\_SDP\_ATTR\_NET\_ACCESS\_TYPE

| #define BT\_SDP\_ATTR\_NET\_ACCESS\_TYPE   0x030b |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Net Access Type.

## [◆ ](#ga9c78d47f54e82a51f7d04a6f6c97663c)BT\_SDP\_ATTR\_NETWORK

| #define BT\_SDP\_ATTR\_NETWORK   0x0301 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Network.

## [◆ ](#ga74dacfd7807d7f3ec7a7594a9329f0b2)BT\_SDP\_ATTR\_NETWORK\_ADDRESS

| #define BT\_SDP\_ATTR\_NETWORK\_ADDRESS   0x0306 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Network Address.

## [◆ ](#gaa681b17ebfe013c196cf372dcd030c6e)BT\_SDP\_ATTR\_PBAP\_SUPPORTED\_FEATURES

| #define BT\_SDP\_ATTR\_PBAP\_SUPPORTED\_FEATURES   0x0317 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

PBAP Supported Features.

## [◆ ](#ga0868f7d90e3944f105028868511896cf)BT\_SDP\_ATTR\_PRIMARY\_RECORD

| #define BT\_SDP\_ATTR\_PRIMARY\_RECORD   0x0204 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Primary Record.

## [◆ ](#gaac9298efffbcf07303f972a12b50f4b6)BT\_SDP\_ATTR\_PRODUCT\_ID

| #define BT\_SDP\_ATTR\_PRODUCT\_ID   0x0202 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Product ID.

## [◆ ](#ga0b5b19caa523e4cb9da8a2bfc6eab20a)BT\_SDP\_ATTR\_PROFILE\_DESC\_LIST

| #define BT\_SDP\_ATTR\_PROFILE\_DESC\_LIST   0x0009 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Bluetooth Profile Descriptor List.

## [◆ ](#ga3e7dad966deab42ff9fa0fd04d3d4514)BT\_SDP\_ATTR\_PROTO\_DESC\_LIST

| #define BT\_SDP\_ATTR\_PROTO\_DESC\_LIST   0x0004 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Protocol Descriptor List.

## [◆ ](#gab8b0110be857d6eca206e00c3b5e373a)BT\_SDP\_ATTR\_PROVNAME\_PRIMARY

| #define BT\_SDP\_ATTR\_PROVNAME\_PRIMARY   (0x0002 + [BT\_SDP\_PRIMARY\_LANG\_BASE](#gab502c9288e5f01dfdaaf8390bb3f6e49)) |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

## [◆ ](#ga38f32cae462272b51eb4edca0c5c95a2)BT\_SDP\_ATTR\_RECORD\_HANDLE

| #define BT\_SDP\_ATTR\_RECORD\_HANDLE   0x0000 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Service Record Handle.

## [◆ ](#ga4d458591f8eba26feaab1220c49f6a29)BT\_SDP\_ATTR\_RECORD\_STATE

| #define BT\_SDP\_ATTR\_RECORD\_STATE   0x0002 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Service Record State.

## [◆ ](#gaa122bfee476a8e83346823e23978f7a0)BT\_SDP\_ATTR\_REMOTE\_AUDIO\_VOLUME\_CONTROL

| #define BT\_SDP\_ATTR\_REMOTE\_AUDIO\_VOLUME\_CONTROL   0x0302 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Remote Audio Volume Control.

## [◆ ](#ga21214c2236a5dca24a45998640761e7b)BT\_SDP\_ATTR\_SECURITY\_DESC

| #define BT\_SDP\_ATTR\_SECURITY\_DESC   0x030a |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Security Description.

## [◆ ](#gaf55a72ce05def1da08d15a23cee4c5e3)BT\_SDP\_ATTR\_SERVICE\_AVAILABILITY

| #define BT\_SDP\_ATTR\_SERVICE\_AVAILABILITY   0x0008 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Service Availability.

## [◆ ](#gad2149fd761f7ae2ea6ef761ab2545ab4)BT\_SDP\_ATTR\_SERVICE\_ID

| #define BT\_SDP\_ATTR\_SERVICE\_ID   0x0003 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Service ID.

## [◆ ](#ga230f70b576c14ba1dbe0cf6eda6220e0)BT\_SDP\_ATTR\_SERVICE\_VERSION

| #define BT\_SDP\_ATTR\_SERVICE\_VERSION   0x0300 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Service Version.

## [◆ ](#ga4af959fbdfe7cee84008642091df948d)BT\_SDP\_ATTR\_SPECIFICATION\_ID

| #define BT\_SDP\_ATTR\_SPECIFICATION\_ID   0x0200 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Specification ID.

## [◆ ](#ga5347dbc038ac9c259d17c14ed9a812d3)BT\_SDP\_ATTR\_SUPPORTED\_CAPABILITIES

| #define BT\_SDP\_ATTR\_SUPPORTED\_CAPABILITIES   0x0310 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

BIP Supported Capabilities.

## [◆ ](#gae12e2daea8febbbd047c1c3843f56933)BT\_SDP\_ATTR\_SUPPORTED\_DATA\_STORES\_LIST

| #define BT\_SDP\_ATTR\_SUPPORTED\_DATA\_STORES\_LIST   0x0301 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Supported Data Stores List.

## [◆ ](#ga498d9beaa7877570fe834d854de36fcb)BT\_SDP\_ATTR\_SUPPORTED\_FEATURES

| #define BT\_SDP\_ATTR\_SUPPORTED\_FEATURES   0x0311 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

BIP Supported Features.

## [◆ ](#ga8a693e5265c7801e3c1125473c31445f)BT\_SDP\_ATTR\_SUPPORTED\_FEATURES\_LIST

| #define BT\_SDP\_ATTR\_SUPPORTED\_FEATURES\_LIST   0x0200 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Supported Features List.

## [◆ ](#gac12ed37044c3f12c2d41b1fd23eacada)BT\_SDP\_ATTR\_SUPPORTED\_FORMATS\_LIST

| #define BT\_SDP\_ATTR\_SUPPORTED\_FORMATS\_LIST   0x0303 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Supported Formats List.

## [◆ ](#gabc7cdfd247da5e2ecfd441c0436471f3)BT\_SDP\_ATTR\_SUPPORTED\_FUNCTIONS

| #define BT\_SDP\_ATTR\_SUPPORTED\_FUNCTIONS   0x0312 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

BIP Supported Functions.

## [◆ ](#ga41fc674e8571556397135734d28b829a)BT\_SDP\_ATTR\_SUPPORTED\_MESSAGE\_TYPES

| #define BT\_SDP\_ATTR\_SUPPORTED\_MESSAGE\_TYPES   0x0316 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Supported Message Types.

## [◆ ](#gada3d989d6c8c0664ba0bf998414a0328)BT\_SDP\_ATTR\_SUPPORTED\_REPOSITORIES

| #define BT\_SDP\_ATTR\_SUPPORTED\_REPOSITORIES   0x0314 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Supported Repositories.

## [◆ ](#gab8fe8881b4470ab3522e710e36470ddb)BT\_SDP\_ATTR\_SVCDB\_STATE

| #define BT\_SDP\_ATTR\_SVCDB\_STATE   0x0201 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Service Database State.

## [◆ ](#ga3e991ec1d5467c0b3ce5d9a7e750a300)BT\_SDP\_ATTR\_SVCDESC\_PRIMARY

| #define BT\_SDP\_ATTR\_SVCDESC\_PRIMARY   (0x0001 + [BT\_SDP\_PRIMARY\_LANG\_BASE](#gab502c9288e5f01dfdaaf8390bb3f6e49)) |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

## [◆ ](#ga7ef037ed6628aa7354736295e0e4ec77)BT\_SDP\_ATTR\_SVCINFO\_TTL

| #define BT\_SDP\_ATTR\_SVCINFO\_TTL   0x0007 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Service Info Time to Live.

## [◆ ](#gab5c5be56c54d3f8bd4ac6defff0b1e7c)BT\_SDP\_ATTR\_SVCLASS\_ID\_LIST

| #define BT\_SDP\_ATTR\_SVCLASS\_ID\_LIST   0x0001 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Service Class ID List.

## [◆ ](#ga76737502226c623bf508ae53a6015e08)BT\_SDP\_ATTR\_SVCNAME\_PRIMARY

| #define BT\_SDP\_ATTR\_SVCNAME\_PRIMARY   (0x0000 + [BT\_SDP\_PRIMARY\_LANG\_BASE](#gab502c9288e5f01dfdaaf8390bb3f6e49)) |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

## [◆ ](#gadbce181b739c201070d6abcbdc4139f4)BT\_SDP\_ATTR\_TOTAL\_IMAGING\_DATA\_CAPACITY

| #define BT\_SDP\_ATTR\_TOTAL\_IMAGING\_DATA\_CAPACITY   0x0313 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

BIP Total Imaging Data Capacity.

## [◆ ](#gab5c2534491b43cfc9d2c7e8807b29ff2)BT\_SDP\_ATTR\_VENDOR\_ID

| #define BT\_SDP\_ATTR\_VENDOR\_ID   0x0201 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Vendor ID.

## [◆ ](#gad0ac4a65c51ccdf4cd128eb8697e56ca)BT\_SDP\_ATTR\_VENDOR\_ID\_SOURCE

| #define BT\_SDP\_ATTR\_VENDOR\_ID\_SOURCE   0x0205 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Vendor ID Source.

## [◆ ](#gae0f4af728f964ee1c11d86b785575a87)BT\_SDP\_ATTR\_VERSION

| #define BT\_SDP\_ATTR\_VERSION   0x0203 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Version.

## [◆ ](#gab698c476197acca0d499e39f7f246c66)BT\_SDP\_ATTR\_VERSION\_NUM\_LIST

| #define BT\_SDP\_ATTR\_VERSION\_NUM\_LIST   0x0200 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Version Number List.

## [◆ ](#ga1ef964c955473601910ee3997b9ce5cd)BT\_SDP\_ATTR\_WAP\_GATEWAY

| #define BT\_SDP\_ATTR\_WAP\_GATEWAY   0x0307 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

WAP Gateway.

## [◆ ](#gae1a3ff84a5588e55258c35ee57d6a5b5)BT\_SDP\_ATTR\_WAP\_STACK\_TYPE

| #define BT\_SDP\_ATTR\_WAP\_STACK\_TYPE   0x0309 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

WAP Stack Type.

## [◆ ](#gaa0e334873b5477523572caa2359a4098)BT\_SDP\_AUDIO\_SINK\_SVCLASS

| #define BT\_SDP\_AUDIO\_SINK\_SVCLASS   0x110b |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Audio Sink.

## [◆ ](#gafeb3a3184a0b83e0045187cbe3cf24dc)BT\_SDP\_AUDIO\_SOURCE\_SVCLASS

| #define BT\_SDP\_AUDIO\_SOURCE\_SVCLASS   0x110a |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Audio Source.

## [◆ ](#gaaae997769dfc8325c38830707f4d22e3)BT\_SDP\_AV\_REMOTE\_CONTROLLER\_SVCLASS

| #define BT\_SDP\_AV\_REMOTE\_CONTROLLER\_SVCLASS   0x110f |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

A/V Remote Control Controller.

## [◆ ](#gaea94250bed4c5e6ad47749a1237778f5)BT\_SDP\_AV\_REMOTE\_SVCLASS

| #define BT\_SDP\_AV\_REMOTE\_SVCLASS   0x110e |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

A/V Remote Control.

## [◆ ](#gafe96e9d32797a83c793f0ed278054b80)BT\_SDP\_AV\_REMOTE\_TARGET\_SVCLASS

| #define BT\_SDP\_AV\_REMOTE\_TARGET\_SVCLASS   0x110c |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

A/V Remote Control Target.

## [◆ ](#gab7a8499dbb73a2700389d55d331bd23e)BT\_SDP\_AV\_SVCLASS

| #define BT\_SDP\_AV\_SVCLASS   0x112c |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Audio/Video.

## [◆ ](#gac727f387a55a76c9a071cf62792f50e4)BT\_SDP\_BASIC\_PRINTING\_SVCLASS

| #define BT\_SDP\_BASIC\_PRINTING\_SVCLASS   0x1122 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Basic Printing.

## [◆ ](#gac48f198f6609fac95db69c09ac69efab)BT\_SDP\_BOOL

| #define BT\_SDP\_BOOL   0x28 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Boolean.

## [◆ ](#gabe05780702a9be7da54a8c04f79ad752)BT\_SDP\_BROWSE\_GRP\_DESC\_SVCLASS

| #define BT\_SDP\_BROWSE\_GRP\_DESC\_SVCLASS   0x1001 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Browse Group Descriptor.

## [◆ ](#ga9617c02c6999d9fe987e91c6c2dc5dca)BT\_SDP\_CIP\_SVCLASS

| #define BT\_SDP\_CIP\_SVCLASS   0x1128 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Common ISDN Access.

## [◆ ](#ga16e1bc10528ac82f6cec822912f97d8c)BT\_SDP\_CORDLESS\_TELEPHONY\_SVCLASS

| #define BT\_SDP\_CORDLESS\_TELEPHONY\_SVCLASS   0x1109 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Cordless Telephony.

## [◆ ](#gaa2954f3df4d0ee9684721cbc6182e37c)BT\_SDP\_DATA\_ELEM\_LIST

| #define BT\_SDP\_DATA\_ELEM\_LIST | ( |  | ... | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sdp.h](sdp_8h.md)>`

**Value:**

((struct [bt\_sdp\_data\_elem](structbt__sdp__data__elem.md)[]) {\_\_VA\_ARGS\_\_})

[bt\_sdp\_data\_elem](structbt__sdp__data__elem.md)

SDP Generic Data Element Value.

**Definition** sdp.h:287

Declare a list of data elements.

## [◆ ](#ga36f257de103356c3ebeb55e23186ed99)BT\_SDP\_DATA\_NIL

| #define BT\_SDP\_DATA\_NIL   0x00 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Nil, the null type.

## [◆ ](#gaab655c1f93029ed64743156734e2519e)BT\_SDP\_DIALUP\_NET\_SVCLASS

| #define BT\_SDP\_DIALUP\_NET\_SVCLASS   0x1103 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Dialup Networking.

## [◆ ](#ga30f6edbd67d96f7752a223409c8e4431)BT\_SDP\_DIRECT\_PRINTING\_SVCLASS

| #define BT\_SDP\_DIRECT\_PRINTING\_SVCLASS   0x1118 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Direct Printing.

## [◆ ](#ga79d34c3b7641cf523adf6515720ceceb)BT\_SDP\_DIRECT\_PRT\_REFOBJS\_SVCLASS

| #define BT\_SDP\_DIRECT\_PRT\_REFOBJS\_SVCLASS   0x1120 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Direct Printing Reference Objects Service.

## [◆ ](#ga31962fab5bed7c54311c4b291713a836)BT\_SDP\_FAX\_SVCLASS

| #define BT\_SDP\_FAX\_SVCLASS   0x1111 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Fax.

## [◆ ](#gae8010af5b12cd1c1b1633a4d2c9f5ab0)BT\_SDP\_GENERIC\_ACCESS\_SVCLASS

| #define BT\_SDP\_GENERIC\_ACCESS\_SVCLASS   0x1800 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Generic Access Profile.

## [◆ ](#gad3f345431526bb713921f4b51c48b056)BT\_SDP\_GENERIC\_ATTRIB\_SVCLASS

| #define BT\_SDP\_GENERIC\_ATTRIB\_SVCLASS   0x1801 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Generic Attribute Profile.

## [◆ ](#gaec7548467ffb686b22a907d05e38f275)BT\_SDP\_GENERIC\_AUDIO\_SVCLASS

| #define BT\_SDP\_GENERIC\_AUDIO\_SVCLASS   0x1203 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Generic Audio.

## [◆ ](#gaa8e5c423fca1fb0d06504cdc5be276d1)BT\_SDP\_GENERIC\_FILETRANS\_SVCLASS

| #define BT\_SDP\_GENERIC\_FILETRANS\_SVCLASS   0x1202 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Generic File Transfer.

## [◆ ](#ga1b9a169ff4db4fda939cba3ce21f808b)BT\_SDP\_GENERIC\_NETWORKING\_SVCLASS

| #define BT\_SDP\_GENERIC\_NETWORKING\_SVCLASS   0x1201 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Generic Networking.

## [◆ ](#ga010b005cfdb69c67cfc7e3c5c8426778)BT\_SDP\_GENERIC\_TELEPHONY\_SVCLASS

| #define BT\_SDP\_GENERIC\_TELEPHONY\_SVCLASS   0x1204 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Generic Telephony.

## [◆ ](#gaed2d6f72c344e2e9b9bdcefd23cb4086)BT\_SDP\_GN\_SVCLASS

| #define BT\_SDP\_GN\_SVCLASS   0x1117 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Group Network.

## [◆ ](#gacdfb8ca6a776f57a2df38b4a6eaa8403)BT\_SDP\_GNSS\_SERVER\_SVCLASS

| #define BT\_SDP\_GNSS\_SERVER\_SVCLASS   0x1136 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

GNSS Server.

## [◆ ](#ga300585062ed9ae05daca226cb3c5440d)BT\_SDP\_GNSS\_SVCLASS

| #define BT\_SDP\_GNSS\_SVCLASS   0x1135 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

GNSS.

## [◆ ](#ga1c44ae236a292c91dc81539c9c89947c)BT\_SDP\_HANDSFREE\_AGW\_SVCLASS

| #define BT\_SDP\_HANDSFREE\_AGW\_SVCLASS   0x111f |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Handsfree Audio Gateway.

## [◆ ](#gab9f99989420545b3b0e71da6c5475f90)BT\_SDP\_HANDSFREE\_SVCLASS

| #define BT\_SDP\_HANDSFREE\_SVCLASS   0x111e |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Handsfree.

## [◆ ](#ga4ca1e6eb6fe385e526f8d84ed65ab285)BT\_SDP\_HCR\_PRINT\_SVCLASS

| #define BT\_SDP\_HCR\_PRINT\_SVCLASS   0x1126 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HCR Print.

## [◆ ](#ga621afe0f5a6d176c26e140c4162bee07)BT\_SDP\_HCR\_SCAN\_SVCLASS

| #define BT\_SDP\_HCR\_SCAN\_SVCLASS   0x1127 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HCR Scan.

## [◆ ](#ga873f8e03aeb696d3eb287a8d00796a4f)BT\_SDP\_HCR\_SVCLASS

| #define BT\_SDP\_HCR\_SVCLASS   0x1125 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Hardcopy Cable Replacement.

## [◆ ](#ga2125a92c6eb724a63d04188919a12bf1)BT\_SDP\_HDP\_SINK\_SVCLASS

| #define BT\_SDP\_HDP\_SINK\_SVCLASS   0x1402 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HDP Sink.

## [◆ ](#ga87ba9fdf39fb99397a6dec4d92b6e3f1)BT\_SDP\_HDP\_SOURCE\_SVCLASS

| #define BT\_SDP\_HDP\_SOURCE\_SVCLASS   0x1401 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HDP Source.

## [◆ ](#gaf8fc80f3b2ff245b7d354aa0488bb42b)BT\_SDP\_HDP\_SVCLASS

| #define BT\_SDP\_HDP\_SVCLASS   0x1400 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

HDP.

## [◆ ](#ga4c9322cf28a8b1aa96828152e8ee7379)BT\_SDP\_HEADSET\_AGW\_SVCLASS

| #define BT\_SDP\_HEADSET\_AGW\_SVCLASS   0x1112 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Headset AG.

## [◆ ](#ga6eb16aacf468b460fa7675ffc4703e68)BT\_SDP\_HEADSET\_SVCLASS

| #define BT\_SDP\_HEADSET\_SVCLASS   0x1108 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Headset.

## [◆ ](#gab63eab5791898a47bd540eed4d55cddc)BT\_SDP\_HID\_SVCLASS

| #define BT\_SDP\_HID\_SVCLASS   0x1124 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Human Interface Device Service.

## [◆ ](#ga3f04a28d9764a0c7755babe379c25393)BT\_SDP\_IMAGING\_ARCHIVE\_SVCLASS

| #define BT\_SDP\_IMAGING\_ARCHIVE\_SVCLASS   0x111c |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Imaging Automatic Archive.

## [◆ ](#ga51a4cfc28f86a650b03a7bbe6e5b883a)BT\_SDP\_IMAGING\_REFOBJS\_SVCLASS

| #define BT\_SDP\_IMAGING\_REFOBJS\_SVCLASS   0x111d |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Imaging Referenced Objects.

## [◆ ](#gaf19cd136b780ef303c1290b26ab2ca17)BT\_SDP\_IMAGING\_RESPONDER\_SVCLASS

| #define BT\_SDP\_IMAGING\_RESPONDER\_SVCLASS   0x111b |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Imaging Responder.

## [◆ ](#ga08730b1fd7088101fadb85e5dc13fd24)BT\_SDP\_IMAGING\_SVCLASS

| #define BT\_SDP\_IMAGING\_SVCLASS   0x111a |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Basic Imaging Profile.

## [◆ ](#gaf754bbfd9cdc0e6a2bf7d6c46fab3f29)BT\_SDP\_INT128

| #define BT\_SDP\_INT128   0x14 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Signed 128-bit integer.

## [◆ ](#gaf6a3795d22cff4a522a2225339fb5a57)BT\_SDP\_INT16

| #define BT\_SDP\_INT16   0x11 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Signed 16-bit integer.

## [◆ ](#ga0ad987ebeac3dab3ef2196f4dfeca1ab)BT\_SDP\_INT32

| #define BT\_SDP\_INT32   0x12 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Signed 32-bit integer.

## [◆ ](#gaae793fef5690c6013e6e0e34ededb75f)BT\_SDP\_INT64

| #define BT\_SDP\_INT64   0x13 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Signed 64-bit integer.

## [◆ ](#gaeed1818ca1bf762b23ab2bfcd18b8a66)BT\_SDP\_INT8

| #define BT\_SDP\_INT8   0x10 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Signed 8-bit integer.

## [◆ ](#ga9681e34d78cea87e413fa4be40e4239a)BT\_SDP\_INTERCOM\_SVCLASS

| #define BT\_SDP\_INTERCOM\_SVCLASS   0x1110 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Intercom.

## [◆ ](#ga39d4ce2465b10c10ee746c1491c49bea)BT\_SDP\_IRMC\_SYNC\_CMD\_SVCLASS

| #define BT\_SDP\_IRMC\_SYNC\_CMD\_SVCLASS   0x1107 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

IrMC Sync Command.

## [◆ ](#ga28fc78fc21e4d88569e5ca5727ed6202)BT\_SDP\_IRMC\_SYNC\_SVCLASS

| #define BT\_SDP\_IRMC\_SYNC\_SVCLASS   0x1104 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

IrMC Sync.

## [◆ ](#gaf0199837105ded0d65314e573da6a3ed)BT\_SDP\_LAN\_ACCESS\_SVCLASS

| #define BT\_SDP\_LAN\_ACCESS\_SVCLASS   0x1102 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

LAN Access Using PPP.

## [◆ ](#ga25b31454ee5b5fe23b617b5256ba00c4)BT\_SDP\_LIST

| #define BT\_SDP\_LIST | ( |  | *\_att\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_type\_size*, |
|  |  |  | *\_data\_elem\_seq* ) |

`#include <[sdp.h](sdp_8h.md)>`

**Value:**

{ \

\_att\_id, { \_type\_size, \_data\_elem\_seq } \

}

Generic SDP List Attribute Declaration Macro.

Helper macro to declare a list attribute.

Parameters
:   | \_att\_id | List Attribute ID. |
    | --- | --- |
    | \_data\_elem\_seq | Data element sequence for the list. |
    | \_type\_size | SDP type and size descriptor. |

## [◆ ](#ga47849c599678f7ec48c237b8b36e9cb7)BT\_SDP\_MAP\_MCE\_SVCLASS

| #define BT\_SDP\_MAP\_MCE\_SVCLASS   0x1133 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Message Notification Server.

## [◆ ](#ga58f5cc54014e3723720e7c3b7ba82fd8)BT\_SDP\_MAP\_MSE\_SVCLASS

| #define BT\_SDP\_MAP\_MSE\_SVCLASS   0x1132 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Message Access Server.

## [◆ ](#gaec665050af4cc3affcef3912bb212fc0)BT\_SDP\_MAP\_SVCLASS

| #define BT\_SDP\_MAP\_SVCLASS   0x1134 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Message Access Profile.

## [◆ ](#ga9cce7e3a576329661b363b102cefa494)BT\_SDP\_MPS\_SC\_SVCLASS

| #define BT\_SDP\_MPS\_SC\_SVCLASS   0x113a |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

MPS SC.

## [◆ ](#gaf847b2675482d3bb9674f569c3604e40)BT\_SDP\_MPS\_SVCLASS

| #define BT\_SDP\_MPS\_SVCLASS   0x113b |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

MPS.

## [◆ ](#ga78a7be1db8be8d7eece0d17c629dd009)BT\_SDP\_NAP\_SVCLASS

| #define BT\_SDP\_NAP\_SVCLASS   0x1116 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Network Access Point.

## [◆ ](#gaee13722587e4eb8c4beaaa0abad88fe5)BT\_SDP\_NEW\_SERVICE

| #define BT\_SDP\_NEW\_SERVICE |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

**Value:**

{ \

[BT\_SDP\_ATTR\_RECORD\_HANDLE](#ga38f32cae462272b51eb4edca0c5c95a2), \

{ [BT\_SDP\_TYPE\_SIZE](#ga66778ac38fb5b82d3b514fe0da008393)([BT\_SDP\_UINT32](#ga4f3bcb36dfce975c2d9ab68894a9e49c)), [BT\_SDP\_ARRAY\_32](#ga7a17ee4872190a087cf2e5ea4db9e737)(0) } \

}, \

{ \

[BT\_SDP\_ATTR\_RECORD\_STATE](#ga4d458591f8eba26feaab1220c49f6a29), \

{ [BT\_SDP\_TYPE\_SIZE](#ga66778ac38fb5b82d3b514fe0da008393)([BT\_SDP\_UINT32](#ga4f3bcb36dfce975c2d9ab68894a9e49c)), [BT\_SDP\_ARRAY\_32](#ga7a17ee4872190a087cf2e5ea4db9e737)(0) } \

}, \

{ \

[BT\_SDP\_ATTR\_LANG\_BASE\_ATTR\_ID\_LIST](#ga462ec997a81c6b439a24e2de085676ab), \

{ [BT\_SDP\_TYPE\_SIZE\_VAR](#gabbb2bd6a8321513082851fe73dfa44bc)([BT\_SDP\_SEQ8](#ga5a64e3bec70b40114a3160dbfb1e484b), 9), \

BT\_SDP\_DATA\_ELEM\_LIST( \

{ [BT\_SDP\_TYPE\_SIZE](#ga66778ac38fb5b82d3b514fe0da008393)([BT\_SDP\_UINT16](#ga1129f3a1364f29c9ce36f6f74ca21327)), [BT\_SDP\_ARRAY\_8](#gaef264fa3621c3df7a164128bb95b30fc)('n', 'e') }, \

{ [BT\_SDP\_TYPE\_SIZE](#ga66778ac38fb5b82d3b514fe0da008393)([BT\_SDP\_UINT16](#ga1129f3a1364f29c9ce36f6f74ca21327)), [BT\_SDP\_ARRAY\_16](#gaa4bb67164ae1f16b26081668d00f45c7)(106) }, \

{ [BT\_SDP\_TYPE\_SIZE](#ga66778ac38fb5b82d3b514fe0da008393)([BT\_SDP\_UINT16](#ga1129f3a1364f29c9ce36f6f74ca21327)), \

BT\_SDP\_ARRAY\_16([BT\_SDP\_PRIMARY\_LANG\_BASE](#gab502c9288e5f01dfdaaf8390bb3f6e49)) } \

), \

} \

}, \

{ \

[BT\_SDP\_ATTR\_BROWSE\_GRP\_LIST](#ga2609212bf5400c31351bc3ec5f60a7e1), \

{ [BT\_SDP\_TYPE\_SIZE\_VAR](#gabbb2bd6a8321513082851fe73dfa44bc)([BT\_SDP\_SEQ8](#ga5a64e3bec70b40114a3160dbfb1e484b), 3), \

BT\_SDP\_DATA\_ELEM\_LIST( \

{ [BT\_SDP\_TYPE\_SIZE](#ga66778ac38fb5b82d3b514fe0da008393)([BT\_SDP\_UUID16](#ga45598f1c663acd3a3e5a409696cb3d2f)), \

BT\_SDP\_ARRAY\_16([BT\_SDP\_PUBLIC\_BROWSE\_GROUP](#ga383233a0ff3159ed653786490a4c06ae)) }, \

), \

} \

}

[BT\_SDP\_UINT16](#ga1129f3a1364f29c9ce36f6f74ca21327)

#define BT\_SDP\_UINT16

Unsigned 16-bit integer.

**Definition** sdp.h:248

[BT\_SDP\_ATTR\_BROWSE\_GRP\_LIST](#ga2609212bf5400c31351bc3ec5f60a7e1)

#define BT\_SDP\_ATTR\_BROWSE\_GRP\_LIST

Browse Group List.

**Definition** sdp.h:133

[BT\_SDP\_PUBLIC\_BROWSE\_GROUP](#ga383233a0ff3159ed653786490a4c06ae)

#define BT\_SDP\_PUBLIC\_BROWSE\_GROUP

Public Browse Group.

**Definition** sdp.h:39

[BT\_SDP\_ATTR\_RECORD\_HANDLE](#ga38f32cae462272b51eb4edca0c5c95a2)

#define BT\_SDP\_ATTR\_RECORD\_HANDLE

Service Record Handle.

**Definition** sdp.h:128

[BT\_SDP\_UUID16](#ga45598f1c663acd3a3e5a409696cb3d2f)

#define BT\_SDP\_UUID16

UUID, 16-bit.

**Definition** sdp.h:258

[BT\_SDP\_ATTR\_LANG\_BASE\_ATTR\_ID\_LIST](#ga462ec997a81c6b439a24e2de085676ab)

#define BT\_SDP\_ATTR\_LANG\_BASE\_ATTR\_ID\_LIST

Language Base Attribute ID List.

**Definition** sdp.h:134

[BT\_SDP\_ATTR\_RECORD\_STATE](#ga4d458591f8eba26feaab1220c49f6a29)

#define BT\_SDP\_ATTR\_RECORD\_STATE

Service Record State.

**Definition** sdp.h:130

[BT\_SDP\_UINT32](#ga4f3bcb36dfce975c2d9ab68894a9e49c)

#define BT\_SDP\_UINT32

Unsigned 32-bit integer.

**Definition** sdp.h:249

[BT\_SDP\_SEQ8](#ga5a64e3bec70b40114a3160dbfb1e484b)

#define BT\_SDP\_SEQ8

Data element sequence, 8-bit length.

**Definition** sdp.h:267

[BT\_SDP\_TYPE\_SIZE](#ga66778ac38fb5b82d3b514fe0da008393)

#define BT\_SDP\_TYPE\_SIZE(\_type)

Declare a fixed-size data element header.

**Definition** sdp.h:335

[BT\_SDP\_ARRAY\_32](#ga7a17ee4872190a087cf2e5ea4db9e737)

#define BT\_SDP\_ARRAY\_32(...)

Declare an array of 32-bit elements in an attribute.

**Definition** sdp.h:328

[BT\_SDP\_ARRAY\_16](#gaa4bb67164ae1f16b26081668d00f45c7)

#define BT\_SDP\_ARRAY\_16(...)

Declare an array of 16-bit elements in an attribute.

**Definition** sdp.h:323

[BT\_SDP\_PRIMARY\_LANG\_BASE](#gab502c9288e5f01dfdaaf8390bb3f6e49)

#define BT\_SDP\_PRIMARY\_LANG\_BASE

**Definition** sdp.h:219

[BT\_SDP\_TYPE\_SIZE\_VAR](#gabbb2bd6a8321513082851fe73dfa44bc)

#define BT\_SDP\_TYPE\_SIZE\_VAR(\_type, \_size)

Declare a variable-size data element header.

**Definition** sdp.h:345

[BT\_SDP\_ARRAY\_8](#gaef264fa3621c3df7a164128bb95b30fc)

#define BT\_SDP\_ARRAY\_8(...)

Declare an array of 8-bit elements in an attribute.

**Definition** sdp.h:318

SDP New Service Record Declaration Macro.

Helper macro to declare a new service record. Default attributes: Record Handle, Record State, Language Base, Root Browse Group

## [◆ ](#gacd25278a573edcb16aa4b60f8ffad20d)BT\_SDP\_OBEX\_FILETRANS\_SVCLASS

| #define BT\_SDP\_OBEX\_FILETRANS\_SVCLASS   0x1106 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

OBEX File Transfer.

## [◆ ](#gaaf64788e0cc6d54a8511c07af22f6740)BT\_SDP\_OBEX\_OBJPUSH\_SVCLASS

| #define BT\_SDP\_OBEX\_OBJPUSH\_SVCLASS   0x1105 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

OBEX Object Push.

## [◆ ](#gaa9abb444e3b43c1164d6b450b1c066e5)BT\_SDP\_PANU\_SVCLASS

| #define BT\_SDP\_PANU\_SVCLASS   0x1115 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Personal Area Networking User.

## [◆ ](#gaec2475b7ba36b860c0f8a9cfc33df4a8)BT\_SDP\_PBAP\_PCE\_SVCLASS

| #define BT\_SDP\_PBAP\_PCE\_SVCLASS   0x112e |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Phonebook Access Client.

## [◆ ](#ga612bb83e9f08edd163433a5fbe9528fc)BT\_SDP\_PBAP\_PSE\_SVCLASS

| #define BT\_SDP\_PBAP\_PSE\_SVCLASS   0x112f |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Phonebook Access Server.

## [◆ ](#ga60a9fad26300c15e988e101f90c06435)BT\_SDP\_PBAP\_SVCLASS

| #define BT\_SDP\_PBAP\_SVCLASS   0x1130 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Phonebook Access.

## [◆ ](#gaed5403661e0eb8f798a950bead59369a)BT\_SDP\_PNP\_INFO\_SVCLASS

| #define BT\_SDP\_PNP\_INFO\_SVCLASS   0x1200 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

PnP Information.

## [◆ ](#gab502c9288e5f01dfdaaf8390bb3f6e49)BT\_SDP\_PRIMARY\_LANG\_BASE

| #define BT\_SDP\_PRIMARY\_LANG\_BASE   0x0100 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

## [◆ ](#ga9298ac73a26a1ab2e53733f404e5c6ea)BT\_SDP\_PRINTING\_STATUS\_SVCLASS

| #define BT\_SDP\_PRINTING\_STATUS\_SVCLASS   0x1123 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Printing Status.

## [◆ ](#ga383233a0ff3159ed653786490a4c06ae)BT\_SDP\_PUBLIC\_BROWSE\_GROUP

| #define BT\_SDP\_PUBLIC\_BROWSE\_GROUP   0x1002 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Public Browse Group.

## [◆ ](#ga555f10b8f3ae3710c6dda9f37e78547b)BT\_SDP\_RECORD

| #define BT\_SDP\_RECORD | ( |  | *\_attrs* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sdp.h](sdp_8h.md)>`

**Value:**

{ \

.attrs = \_attrs, \

.attr\_count = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)((\_attrs)), \

}

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:127

SDP Service Declaration Macro.

Helper macro to declare a service.

Parameters
:   | \_attrs | List of attributes for the service record. |
    | --- | --- |

## [◆ ](#ga6bc247854656613d2fa9b47d55bd69d6)BT\_SDP\_REFERENCE\_PRINTING\_SVCLASS

| #define BT\_SDP\_REFERENCE\_PRINTING\_SVCLASS   0x1119 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Reference Printing.

## [◆ ](#ga78607a42f5228b37d348614b12e48a77)BT\_SDP\_REFLECTED\_UI\_SVCLASS

| #define BT\_SDP\_REFLECTED\_UI\_SVCLASS   0x1121 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Reflected UI.

## [◆ ](#gad2234f8e0bce0e6b55d18c7a7c950e1d)BT\_SDP\_SAP\_SVCLASS

| #define BT\_SDP\_SAP\_SVCLASS   0x112d |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

SIM Access.

## [◆ ](#gac2c2379f8e483939826297dc49657837)BT\_SDP\_SDP\_SERVER\_SVCLASS

| #define BT\_SDP\_SDP\_SERVER\_SVCLASS   0x1000 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Service Discovery Server.

## [◆ ](#gadf5b15a0296a872ffefc24bbc90dc45b)BT\_SDP\_SEQ16

| #define BT\_SDP\_SEQ16   0x36 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Data element sequence, 16-bit length.

## [◆ ](#ga639e86b5103168917cb7202100e3124d)BT\_SDP\_SEQ32

| #define BT\_SDP\_SEQ32   0x37 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Data element sequence, 32-bit length.

## [◆ ](#ga5a64e3bec70b40114a3160dbfb1e484b)BT\_SDP\_SEQ8

| #define BT\_SDP\_SEQ8   0x35 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Data element sequence, 8-bit length.

## [◆ ](#gaa884191d772bfa24484cb33c0f614334)BT\_SDP\_SEQ\_UNSPEC

| #define BT\_SDP\_SEQ\_UNSPEC   0x30 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Data element sequence, unspecified size.

## [◆ ](#gab1234d808a7e347328bf95ad065fd9c4)BT\_SDP\_SERIAL\_PORT\_SVCLASS

| #define BT\_SDP\_SERIAL\_PORT\_SVCLASS   0x1101 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Serial Port.

## [◆ ](#ga610e7cab0a598f272eeb2838f4c4c996)BT\_SDP\_SERVER\_RECORD\_HANDLE

| #define BT\_SDP\_SERVER\_RECORD\_HANDLE   0x0000 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

## [◆ ](#gaa57f3c9a52ae29c02d7577be99f91e7c)BT\_SDP\_SERVICE\_ID

| #define BT\_SDP\_SERVICE\_ID | ( |  | *\_uuid* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sdp.h](sdp_8h.md)>`

**Value:**

{ \

[BT\_SDP\_ATTR\_SERVICE\_ID](#gad2149fd761f7ae2ea6ef761ab2545ab4), \

{ [BT\_SDP\_TYPE\_SIZE](#ga66778ac38fb5b82d3b514fe0da008393)([BT\_SDP\_UUID16](#ga45598f1c663acd3a3e5a409696cb3d2f)), &((struct [bt\_uuid\_16](structbt__uuid__16.md)) \_uuid) } \

}

[BT\_SDP\_ATTR\_SERVICE\_ID](#gad2149fd761f7ae2ea6ef761ab2545ab4)

#define BT\_SDP\_ATTR\_SERVICE\_ID

Service ID.

**Definition** sdp.h:131

[bt\_uuid\_16](structbt__uuid__16.md)

**Definition** uuid.h:53

SDP Service ID Attribute Declaration Macro.

Helper macro to declare a service ID attribute.

Parameters
:   | \_uuid | Service ID 16bit UUID. |
    | --- | --- |

## [◆ ](#ga83de8e62415d3e31b3b5434b9db633d0)BT\_SDP\_SERVICE\_NAME

| #define BT\_SDP\_SERVICE\_NAME | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sdp.h](sdp_8h.md)>`

**Value:**

{ \

[BT\_SDP\_ATTR\_SVCNAME\_PRIMARY](#ga76737502226c623bf508ae53a6015e08), \

{ [BT\_SDP\_TYPE\_SIZE\_VAR](#gabbb2bd6a8321513082851fe73dfa44bc)([BT\_SDP\_TEXT\_STR8](#ga885ace6b1def91f3fa4dd16cb391d2b8), (sizeof(\_name)-1)), \_name } \

}

[BT\_SDP\_ATTR\_SVCNAME\_PRIMARY](#ga76737502226c623bf508ae53a6015e08)

#define BT\_SDP\_ATTR\_SVCNAME\_PRIMARY

**Definition** sdp.h:221

[BT\_SDP\_TEXT\_STR8](#ga885ace6b1def91f3fa4dd16cb391d2b8)

#define BT\_SDP\_TEXT\_STR8

Text string, 8-bit length.

**Definition** sdp.h:262

SDP Name Attribute Declaration Macro.

Helper macro to declare a service name attribute.

Parameters
:   | \_name | Service name as a string (up to 256 chars). |
    | --- | --- |

## [◆ ](#ga2d1040ccd11d1dd4c697525ebc323243)BT\_SDP\_SIZE\_DESC\_MASK

| #define BT\_SDP\_SIZE\_DESC\_MASK   0x07 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

## [◆ ](#ga6e8f843aeb2d325058214d2a1454737a)BT\_SDP\_SIZE\_INDEX\_OFFSET

| #define BT\_SDP\_SIZE\_INDEX\_OFFSET   5 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

## [◆ ](#ga096c84414b429aa05bed45cf6175361e)BT\_SDP\_SUPPORTED\_FEATURES

| #define BT\_SDP\_SUPPORTED\_FEATURES | ( |  | *\_features* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sdp.h](sdp_8h.md)>`

**Value:**

{ \

[BT\_SDP\_ATTR\_SUPPORTED\_FEATURES](#ga498d9beaa7877570fe834d854de36fcb), \

{ [BT\_SDP\_TYPE\_SIZE](#ga66778ac38fb5b82d3b514fe0da008393)([BT\_SDP\_UINT16](#ga1129f3a1364f29c9ce36f6f74ca21327)), [BT\_SDP\_ARRAY\_16](#gaa4bb67164ae1f16b26081668d00f45c7)(\_features) } \

}

[BT\_SDP\_ATTR\_SUPPORTED\_FEATURES](#ga498d9beaa7877570fe834d854de36fcb)

#define BT\_SDP\_ATTR\_SUPPORTED\_FEATURES

BIP Supported Features.

**Definition** sdp.h:176

SDP Supported Features Attribute Declaration Macro.

Helper macro to declare supported features of a profile/protocol.

Parameters
:   | \_features | Feature mask as 16bit unsigned integer. |
    | --- | --- |

## [◆ ](#gaa5301cdac5fc9299837f29b92aa3c10b)BT\_SDP\_TEXT\_STR16

| #define BT\_SDP\_TEXT\_STR16   0x26 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Text string, 16-bit length.

## [◆ ](#ga29657a21117a3fbe05942778a8d7637e)BT\_SDP\_TEXT\_STR32

| #define BT\_SDP\_TEXT\_STR32   0x27 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Text string, 32-bit length.

## [◆ ](#ga885ace6b1def91f3fa4dd16cb391d2b8)BT\_SDP\_TEXT\_STR8

| #define BT\_SDP\_TEXT\_STR8   0x25 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Text string, 8-bit length.

## [◆ ](#gaca9942a42701cda835a5bf7b7aaf1d75)BT\_SDP\_TEXT\_STR\_UNSPEC

| #define BT\_SDP\_TEXT\_STR\_UNSPEC   0x20 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Text string, unspecified size.

## [◆ ](#ga3eb2a5501341f6c5186a27219cf27cdf)BT\_SDP\_TYPE\_DESC\_MASK

| #define BT\_SDP\_TYPE\_DESC\_MASK   0xf8 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

## [◆ ](#ga66778ac38fb5b82d3b514fe0da008393)BT\_SDP\_TYPE\_SIZE

| #define BT\_SDP\_TYPE\_SIZE | ( |  | *\_type* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sdp.h](sdp_8h.md)>`

**Value:**

.type = \_type, \

.data\_size = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(\_type & [BT\_SDP\_SIZE\_DESC\_MASK](#ga2d1040ccd11d1dd4c697525ebc323243)), \

.total\_size = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(\_type & [BT\_SDP\_SIZE\_DESC\_MASK](#ga2d1040ccd11d1dd4c697525ebc323243)) + 1

[BT\_SDP\_SIZE\_DESC\_MASK](#ga2d1040ccd11d1dd4c697525ebc323243)

#define BT\_SDP\_SIZE\_DESC\_MASK

**Definition** sdp.h:283

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

Declare a fixed-size data element header.

Parameters
:   | \_type | Data element header containing type and size descriptors. |
    | --- | --- |

## [◆ ](#gabbb2bd6a8321513082851fe73dfa44bc)BT\_SDP\_TYPE\_SIZE\_VAR

| #define BT\_SDP\_TYPE\_SIZE\_VAR | ( |  | *\_type*, |
| --- | --- | --- | --- |
|  |  |  | *\_size* ) |

`#include <[sdp.h](sdp_8h.md)>`

**Value:**

.type = \_type, \

.data\_size = \_size, \

.total\_size = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)((\_type & [BT\_SDP\_SIZE\_DESC\_MASK](#ga2d1040ccd11d1dd4c697525ebc323243)) - \

[BT\_SDP\_SIZE\_INDEX\_OFFSET](#ga6e8f843aeb2d325058214d2a1454737a)) + \_size + 1

[BT\_SDP\_SIZE\_INDEX\_OFFSET](#ga6e8f843aeb2d325058214d2a1454737a)

#define BT\_SDP\_SIZE\_INDEX\_OFFSET

**Definition** sdp.h:284

Declare a variable-size data element header.

Parameters
:   | \_type | Data element header containing type and size descriptors. |
    | --- | --- |
    | \_size | The actual size of the data. |

## [◆ ](#ga629179357eff2cd60621f0e1e435df06)BT\_SDP\_UDI\_MT\_SVCLASS

| #define BT\_SDP\_UDI\_MT\_SVCLASS   0x112a |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

UDI MT.

## [◆ ](#ga846599abf75f1cbb27028aea8a619f31)BT\_SDP\_UDI\_TA\_SVCLASS

| #define BT\_SDP\_UDI\_TA\_SVCLASS   0x112b |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

UDI TA.

## [◆ ](#ga9a815c6efe976f29e9f6f35a566245fd)BT\_SDP\_UINT128

| #define BT\_SDP\_UINT128   0x0c |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Unsigned 128-bit integer.

## [◆ ](#ga1129f3a1364f29c9ce36f6f74ca21327)BT\_SDP\_UINT16

| #define BT\_SDP\_UINT16   0x09 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Unsigned 16-bit integer.

## [◆ ](#ga4f3bcb36dfce975c2d9ab68894a9e49c)BT\_SDP\_UINT32

| #define BT\_SDP\_UINT32   0x0a |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Unsigned 32-bit integer.

## [◆ ](#ga11261bf1c63a6d463ed41225c1e1a0c7)BT\_SDP\_UINT64

| #define BT\_SDP\_UINT64   0x0b |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Unsigned 64-bit integer.

## [◆ ](#ga546a46c2aa7eb3306eb46768fb8737a4)BT\_SDP\_UINT8

| #define BT\_SDP\_UINT8   0x08 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Unsigned 8-bit integer.

## [◆ ](#ga102b24708429877c4f37a5008fb176b1)BT\_SDP\_UPNP\_IP\_SVCLASS

| #define BT\_SDP\_UPNP\_IP\_SVCLASS   0x1206 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

UPnP IP Service.

## [◆ ](#gad4d97c0b664c48bdc0842f92240409c7)BT\_SDP\_UPNP\_L2CAP\_SVCLASS

| #define BT\_SDP\_UPNP\_L2CAP\_SVCLASS   0x1302 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

UPnP IP L2CAP.

## [◆ ](#gad418094573383e6252719abed97d24dd)BT\_SDP\_UPNP\_LAP\_SVCLASS

| #define BT\_SDP\_UPNP\_LAP\_SVCLASS   0x1301 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

UPnP IP LAP.

## [◆ ](#ga3f50947a742b24089f86193e773d623b)BT\_SDP\_UPNP\_PAN\_SVCLASS

| #define BT\_SDP\_UPNP\_PAN\_SVCLASS   0x1300 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

UPnP IP PAN.

## [◆ ](#ga9e7fa3bcf139462a2c33f90b526e1ad1)BT\_SDP\_UPNP\_SVCLASS

| #define BT\_SDP\_UPNP\_SVCLASS   0x1205 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

UPnP Service.

## [◆ ](#gac1acc712468e5af1f54022ac3551882a)BT\_SDP\_URL\_STR16

| #define BT\_SDP\_URL\_STR16   0x46 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

URL string, 16-bit length.

## [◆ ](#ga37476681e9d4eee53b710c44e2da9a2f)BT\_SDP\_URL\_STR32

| #define BT\_SDP\_URL\_STR32   0x47 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

URL string, 32-bit length.

## [◆ ](#gafb2a77d6097c8c4cf9f01b7e16df26f1)BT\_SDP\_URL\_STR8

| #define BT\_SDP\_URL\_STR8   0x45 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

URL string, 8-bit length.

## [◆ ](#ga32a7a79422f52b75c2eb2d2eb467dc00)BT\_SDP\_URL\_STR\_UNSPEC

| #define BT\_SDP\_URL\_STR\_UNSPEC   0x40 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

URL string, unspecified size.

## [◆ ](#gaadf48ba3e96687fff99ff58789d79a50)BT\_SDP\_UUID128

| #define BT\_SDP\_UUID128   0x1c |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

UUID, 128-bit.

## [◆ ](#ga45598f1c663acd3a3e5a409696cb3d2f)BT\_SDP\_UUID16

| #define BT\_SDP\_UUID16   0x19 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

UUID, 16-bit.

## [◆ ](#ga78245bb059feb3ec039e05aba24746e7)BT\_SDP\_UUID32

| #define BT\_SDP\_UUID32   0x1a |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

UUID, 32-bit.

## [◆ ](#ga4f829572cca9669a8a96a857874bb022)BT\_SDP\_UUID\_UNSPEC

| #define BT\_SDP\_UUID\_UNSPEC   0x18 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

UUID, unspecified size.

## [◆ ](#ga3e087c095a78f07efae660eceae9c11e)BT\_SDP\_VIDEO\_CONF\_GW\_SVCLASS

| #define BT\_SDP\_VIDEO\_CONF\_GW\_SVCLASS   0x1129 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Video Conferencing Gateway.

## [◆ ](#ga4e2ef8310c9396f9fb7781ab4732f308)BT\_SDP\_VIDEO\_DISTRIBUTION\_SVCLASS

| #define BT\_SDP\_VIDEO\_DISTRIBUTION\_SVCLASS   0x1305 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Video Distribution.

## [◆ ](#ga1e3428b6d0197bd7c9d72154c025e9f5)BT\_SDP\_VIDEO\_SINK\_SVCLASS

| #define BT\_SDP\_VIDEO\_SINK\_SVCLASS   0x1304 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Video Sink.

## [◆ ](#ga17d7fb3a77ef7266ea2d760fb3696a83)BT\_SDP\_VIDEO\_SOURCE\_SVCLASS

| #define BT\_SDP\_VIDEO\_SOURCE\_SVCLASS   0x1303 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Video Source.

## [◆ ](#ga22624d29917aaeaa0c281d9517178821)BT\_SDP\_WAP\_CLIENT\_SVCLASS

| #define BT\_SDP\_WAP\_CLIENT\_SVCLASS   0x1114 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

WAP Client.

## [◆ ](#ga2ab79d7ff4e88820773cf24f0b0b6e20)BT\_SDP\_WAP\_SVCLASS

| #define BT\_SDP\_WAP\_SVCLASS   0x1113 |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

WAP.

## Typedef Documentation

## [◆ ](#gae5fa4166e3b909f9dcaace11b302f98f)bt\_sdp\_discover\_func\_t

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* bt\_sdp\_discover\_func\_t) (struct bt\_conn \*conn, struct [bt\_sdp\_client\_result](structbt__sdp__client__result.md) \*result) |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Callback type reporting to user that there is a resolved result on remote for given UUID and the result record buffer can be used by user for further inspection.

A function of this type is given by the user to the [bt\_sdp\_discover\_params](structbt__sdp__discover__params.md "Main user structure used in SDP discovery of remote.") object. It'll be called on each valid record discovery completion for given UUID. When UUID resolution gives back no records then NULL is passed to the user. Otherwise user can get valid record(s) and then the internal hint 'next record' is set to false saying the UUID resolution is complete or the hint can be set by caller to true meaning that next record is available for given UUID. The returned function value allows the user to control retrieving follow-up resolved records if any. If the user doesn't want to read more resolved records for given UUID since current record data fulfills its requirements then should return BT\_SDP\_DISCOVER\_UUID\_STOP. Otherwise returned value means more subcall iterations are allowable.

Parameters
:   | conn | Connection object identifying connection to queried remote. |
    | --- | --- |
    | result | Object pointing to logical unparsed SDP record collected on base of response driven by given UUID. |

Returns
:   BT\_SDP\_DISCOVER\_UUID\_STOP in case of no more need to read next record data and continue discovery for given UUID. By returning BT\_SDP\_DISCOVER\_UUID\_CONTINUE user allows this discovery continuation.

## Enumeration Type Documentation

## [◆ ](#ga278df12ff5def68ca4663defd178582c)anonymous enum

| anonymous enum |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Helper enum to be used as return value of [bt\_sdp\_discover\_func\_t](#gae5fa4166e3b909f9dcaace11b302f98f).

The value informs the caller to perform further pending actions or stop them.

| Enumerator | |
| --- | --- |
| BT\_SDP\_DISCOVER\_UUID\_STOP |  |
| BT\_SDP\_DISCOVER\_UUID\_CONTINUE |  |

## [◆ ](#gaf01cb8d69aee9e06ab944ceae4d7df7c)bt\_sdp\_proto

| enum [bt\_sdp\_proto](#gaf01cb8d69aee9e06ab944ceae4d7df7c) |
| --- |

`#include <[sdp.h](sdp_8h.md)>`

Protocols to be asked about specific parameters.

| Enumerator | |
| --- | --- |
| BT\_SDP\_PROTO\_RFCOMM |  |
| BT\_SDP\_PROTO\_L2CAP |  |

## Function Documentation

## [◆ ](#gaf49c299d269ee7b93d41e6ce71df9f77)bt\_sdp\_discover()

| int bt\_sdp\_discover | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_sdp\_discover\_params](structbt__sdp__discover__params.md) \* | *params* ) |

`#include <[sdp.h](sdp_8h.md)>`

Allows user to start SDP discovery session.

The function performs SDP service discovery on remote server driven by user delivered discovery parameters. Discovery session is made as soon as no SDP transaction is ongoing between peers and if any then this one is queued to be processed at discovery completion of previous one. On the service discovery completion the callback function will be called to get feedback to user about findings.

Parameters
:   | conn | Object identifying connection to remote. |
    | --- | --- |
    | params | SDP discovery parameters. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga4659915e85ac2f440d6ea6be71f856fa)bt\_sdp\_discover\_cancel()

| int bt\_sdp\_discover\_cancel | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_sdp\_discover\_params](structbt__sdp__discover__params.md) \* | *params* ) |

`#include <[sdp.h](sdp_8h.md)>`

Release waiting SDP discovery request.

It can cancel valid waiting SDP client request identified by SDP discovery parameters object.

Parameters
:   | conn | Object identifying connection to remote. |
    | --- | --- |
    | params | SDP discovery parameters. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gacfcec85582954a80ba94822175d61092)bt\_sdp\_get\_addl\_proto\_param()

| int bt\_sdp\_get\_addl\_proto\_param | ( | const struct [net\_buf](structnet__buf.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_sdp\_proto](#gaf01cb8d69aee9e06ab944ceae4d7df7c) | *proto*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *param\_index*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *param* ) |

`#include <[sdp.h](sdp_8h.md)>`

Get additional parameter value related to given stacked protocol UUID.

API extracts specific parameter associated with given protocol UUID available in Additional Protocol Descriptor List attribute.

Parameters
:   |  | buf | Original buffered raw record data. |
    | --- | --- | --- |
    |  | proto | Known protocol to be checked like RFCOMM or L2CAP. |
    |  | param\_index | There may be more than one parameter related to the given protocol UUID. This function returns the result that is indexed by this parameter. It's value is from 0, 0 means the first matched result, 1 means the second matched result. |
    | [out] | param | On success populated by found parameter value. |

Returns
:   0 on success when a specific parameter associated with a given protocol value is found, or negative if error occurred during processing.

## [◆ ](#gae1c3110dfe24a939cc02d998c4699ca7)bt\_sdp\_get\_features()

| int bt\_sdp\_get\_features | ( | const struct [net\_buf](structnet__buf.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *features* ) |

`#include <[sdp.h](sdp_8h.md)>`

Get SupportedFeatures attribute value.

Allows if exposed by remote retrieve SupportedFeature attribute.

Parameters
:   | buf | Buffer holding original raw record data from remote. |
    | --- | --- |
    | features | On success object to be populated with SupportedFeature mask. |

Returns
:   0 on success if feature found and valid, negative in case any error

## [◆ ](#ga9e7d4bd0a407fe8254410f907db90f00)bt\_sdp\_get\_profile\_version()

| int bt\_sdp\_get\_profile\_version | ( | const struct [net\_buf](structnet__buf.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *profile*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *version* ) |

`#include <[sdp.h](sdp_8h.md)>`

Get profile version.

Helper API extracting remote profile version number. To get it proper generic profile parameter needs to be selected usually listed in SDP Interoperability Requirements section for given profile specification.

Parameters
:   | buf | Original buffered raw record data. |
    | --- | --- |
    | profile | Profile family identifier the profile belongs. |
    | version | On success populated by found version number. |

Returns
:   0 on success, negative value if error occurred during processing.

## [◆ ](#gaff14678f465af239ac79d1e34bdb9409)bt\_sdp\_get\_proto\_param()

| int bt\_sdp\_get\_proto\_param | ( | const struct [net\_buf](structnet__buf.md) \* | *buf*, |
| --- | --- | --- | --- |
|  |  | enum [bt\_sdp\_proto](#gaf01cb8d69aee9e06ab944ceae4d7df7c) | *proto*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | *param* ) |

`#include <[sdp.h](sdp_8h.md)>`

Give to user parameter value related to given stacked protocol UUID.

API extracts specific parameter associated with given protocol UUID available in Protocol Descriptor List attribute.

Parameters
:   | buf | Original buffered raw record data. |
    | --- | --- |
    | proto | Known protocol to be checked like RFCOMM or L2CAP. |
    | param | On success populated by found parameter value. |

Returns
:   0 on success when specific parameter associated with given protocol value is found, or negative if error occurred during processing.

## [◆ ](#ga6006e3cd593ef793273fb291913790fa)bt\_sdp\_register\_service()

| int bt\_sdp\_register\_service | ( | struct [bt\_sdp\_record](structbt__sdp__record.md) \* | *service* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[sdp.h](sdp_8h.md)>`

Register a Service Record.

Register a Service Record. Applications can make use of macros such as BT\_SDP\_DECLARE\_SERVICE, BT\_SDP\_LIST, BT\_SDP\_SERVICE\_ID, BT\_SDP\_SERVICE\_NAME, etc. A service declaration must start with BT\_SDP\_NEW\_SERVICE.

Parameters
:   | service | Service record declared using BT\_SDP\_DECLARE\_SERVICE. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
