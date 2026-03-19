---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/hci__vs_8h.html
original_path: doxygen/html/hci__vs_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hci\_vs.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/bluetooth/hci.h](hci_8h_source.md)>`

[Go to the source code of this file.](hci__vs_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_hci\_rp\_vs\_read\_version\_info](structbt__hci__rp__vs__read__version__info.md) |
| struct | [bt\_hci\_rp\_vs\_read\_supported\_commands](structbt__hci__rp__vs__read__supported__commands.md) |
| struct | [bt\_hci\_rp\_vs\_read\_supported\_features](structbt__hci__rp__vs__read__supported__features.md) |
| struct | [bt\_hci\_cp\_vs\_set\_event\_mask](structbt__hci__cp__vs__set__event__mask.md) |
| struct | [bt\_hci\_cp\_vs\_reset](structbt__hci__cp__vs__reset.md) |
| struct | [bt\_hci\_cp\_vs\_write\_bd\_addr](structbt__hci__cp__vs__write__bd__addr.md) |
| struct | [bt\_hci\_cp\_vs\_set\_trace\_enable](structbt__hci__cp__vs__set__trace__enable.md) |
| struct | [bt\_hci\_rp\_vs\_read\_build\_info](structbt__hci__rp__vs__read__build__info.md) |
| struct | [bt\_hci\_vs\_static\_addr](structbt__hci__vs__static__addr.md) |
| struct | [bt\_hci\_rp\_vs\_read\_static\_addrs](structbt__hci__rp__vs__read__static__addrs.md) |
| struct | [bt\_hci\_rp\_vs\_read\_key\_hierarchy\_roots](structbt__hci__rp__vs__read__key__hierarchy__roots.md) |
| struct | [bt\_hci\_rp\_vs\_read\_chip\_temp](structbt__hci__rp__vs__read__chip__temp.md) |
| struct | [bt\_hci\_vs\_cmd](structbt__hci__vs__cmd.md) |
| struct | [bt\_hci\_rp\_vs\_read\_host\_stack\_cmds](structbt__hci__rp__vs__read__host__stack__cmds.md) |
| struct | [bt\_hci\_cp\_vs\_set\_scan\_req\_reports](structbt__hci__cp__vs__set__scan__req__reports.md) |
| struct | [bt\_hci\_cp\_vs\_write\_tx\_power\_level](structbt__hci__cp__vs__write__tx__power__level.md) |
| struct | [bt\_hci\_rp\_vs\_write\_tx\_power\_level](structbt__hci__rp__vs__write__tx__power__level.md) |
| struct | [bt\_hci\_cp\_vs\_read\_tx\_power\_level](structbt__hci__cp__vs__read__tx__power__level.md) |
| struct | [bt\_hci\_rp\_vs\_read\_tx\_power\_level](structbt__hci__rp__vs__read__tx__power__level.md) |
| struct | [bt\_hci\_rp\_vs\_read\_usb\_transport\_mode](structbt__hci__rp__vs__read__usb__transport__mode.md) |
| struct | [bt\_hci\_cp\_vs\_set\_usb\_transport\_mode](structbt__hci__cp__vs__set__usb__transport__mode.md) |
| struct | [bt\_hci\_cp\_vs\_set\_min\_num\_used\_chans](structbt__hci__cp__vs__set__min__num__used__chans.md) |
| struct | [bt\_hci\_evt\_vs](structbt__hci__evt__vs.md) |
| struct | [bt\_hci\_vs\_fata\_error\_cpu\_data\_cortex\_m](structbt__hci__vs__fata__error__cpu__data__cortex__m.md) |
| struct | [bt\_hci\_vs\_fatal\_error\_stack\_frame](structbt__hci__vs__fatal__error__stack__frame.md) |
| struct | [bt\_hci\_evt\_vs\_fatal\_error\_trace\_data](structbt__hci__evt__vs__fatal__error__trace__data.md) |
| struct | [bt\_hci\_evt\_vs\_fatal\_error](structbt__hci__evt__vs__fatal__error.md) |
| struct | [bt\_hci\_evt\_vs\_trace\_info](structbt__hci__evt__vs__trace__info.md) |
| struct | [bt\_hci\_evt\_vs\_scan\_req\_rx](structbt__hci__evt__vs__scan__req__rx.md) |
| struct | [bt\_hci\_le\_iq\_sample16](structbt__hci__le__iq__sample16.md) |
| struct | [bt\_hci\_evt\_vs\_le\_connectionless\_iq\_report](structbt__hci__evt__vs__le__connectionless__iq__report.md) |
| struct | [bt\_hci\_evt\_vs\_le\_connection\_iq\_report](structbt__hci__evt__vs__le__connection__iq__report.md) |
| struct | [bt\_hci\_cp\_mesh](structbt__hci__cp__mesh.md) |
| struct | [bt\_hci\_rp\_mesh\_get\_opts](structbt__hci__rp__mesh__get__opts.md) |
| struct | [bt\_hci\_mesh\_pattern](structbt__hci__mesh__pattern.md) |
| struct | [bt\_hci\_cp\_mesh\_set\_scan\_filter](structbt__hci__cp__mesh__set__scan__filter.md) |
| struct | [bt\_hci\_rp\_mesh\_set\_scan\_filter](structbt__hci__rp__mesh__set__scan__filter.md) |
| struct | [bt\_hci\_cp\_mesh\_advertise](structbt__hci__cp__mesh__advertise.md) |
| struct | [bt\_hci\_rp\_mesh\_advertise](structbt__hci__rp__mesh__advertise.md) |
| struct | [bt\_hci\_cp\_mesh\_advertise\_timed](structbt__hci__cp__mesh__advertise__timed.md) |
| struct | [bt\_hci\_rp\_mesh\_advertise\_timed](structbt__hci__rp__mesh__advertise__timed.md) |
| struct | [bt\_hci\_cp\_mesh\_advertise\_cancel](structbt__hci__cp__mesh__advertise__cancel.md) |
| struct | [bt\_hci\_rp\_mesh\_advertise\_cancel](structbt__hci__rp__mesh__advertise__cancel.md) |
| struct | [bt\_hci\_cp\_mesh\_set\_scanning](structbt__hci__cp__mesh__set__scanning.md) |
| struct | [bt\_hci\_rp\_mesh\_set\_scanning](structbt__hci__rp__mesh__set__scanning.md) |
| struct | [bt\_hci\_evt\_mesh](structbt__hci__evt__mesh.md) |
| struct | [bt\_hci\_evt\_mesh\_adv\_complete](structbt__hci__evt__mesh__adv__complete.md) |
| struct | [bt\_hci\_evt\_mesh\_scan\_report](structbt__hci__evt__mesh__scan__report.md) |
| struct | [bt\_hci\_evt\_mesh\_scanning\_report](structbt__hci__evt__mesh__scanning__report.md) |

| Macros | |
| --- | --- |
| #define | [BT\_VS\_CMD\_BIT\_VERSION](#a98cda5172947a82dfee334a5db41b0bb)   0 |
| #define | [BT\_VS\_CMD\_BIT\_SUP\_CMD](#a2eec9eff49fc0d8f4e4f746dd7498478)   1 |
| #define | [BT\_VS\_CMD\_BIT\_SUP\_FEAT](#a418e0fd9c322671c1124835752b25678)   2 |
| #define | [BT\_VS\_CMD\_BIT\_SET\_EVT\_MASK](#ab1b627847e323e94949b53665e47f20f)   3 |
| #define | [BT\_VS\_CMD\_BIT\_RESET](#a020ca307df4c66bcd4c4f6da42d22e40)   4 |
| #define | [BT\_VS\_CMD\_BIT\_WRITE\_BDADDR](#ac8fa0f7e3d5b802f1797c77d988bc172)   5 |
| #define | [BT\_VS\_CMD\_BIT\_SET\_TRACE\_ENABLE](#ad57ee37a93208d3127e5ba36933b0d36)   6 |
| #define | [BT\_VS\_CMD\_BIT\_READ\_BUILD\_INFO](#aaae2460cf69b0ad51aedf57c72d42103)   7 |
| #define | [BT\_VS\_CMD\_BIT\_READ\_STATIC\_ADDRS](#a27e19ec90e057244db7f632887a46ec1)   8 |
| #define | [BT\_VS\_CMD\_BIT\_READ\_KEY\_ROOTS](#aa8b39f4ac968cf0cdb18073de1aa1ad5)   9 |
| #define | [BT\_VS\_CMD\_BIT\_READ\_CHIP\_TEMP](#a96cee049fdf09d1e22aa2204a080c956)   10 |
| #define | [BT\_VS\_CMD\_BIT\_READ\_HOST\_STACK\_CMD](#a072226e7bfd637f71a03971e18d795e5)   11 |
| #define | [BT\_VS\_CMD\_BIT\_SET\_SCAN\_REP\_ENABLE](#ac16322768bdd4688b2cefb4ea7b8c26f)   12 |
| #define | [BT\_VS\_CMD\_BIT\_WRITE\_TX\_POWER](#a3f720e278e3aeefd11e9682d683e448b)   13 |
| #define | [BT\_VS\_CMD\_BIT\_READ\_TX\_POWER](#a9af8f8bde7f33db3f32aa2aa5bda4012)   14 |
| #define | [BT\_VS\_CMD\_SUP\_FEAT](#a6f43e26c34622d9b9b2cf0a6ba53a393)([cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
| #define | [BT\_VS\_CMD\_READ\_STATIC\_ADDRS](#af5ef90c96d5798cef8ad32f8d6094d53)([cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
| #define | [BT\_VS\_CMD\_READ\_KEY\_ROOTS](#aa81a670c17714854306b0044e9fb6392)([cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)) |
| #define | [BT\_HCI\_VS\_HW\_PLAT\_INTEL](#a35bf58cbe551d8e3e56fa687828a5ee7)   0x0001 |
| #define | [BT\_HCI\_VS\_HW\_PLAT\_NORDIC](#a533362f9e60a77ce5c787d26241a2200)   0x0002 |
| #define | [BT\_HCI\_VS\_HW\_PLAT\_NXP](#a0813745772dc53d5eb8d78ca016e0b3c)   0x0003 |
| #define | [BT\_HCI\_VS\_HW\_VAR\_NORDIC\_NRF51X](#aef40f22484598bcd15885f1cf27a3a7e)   0x0001 |
| #define | [BT\_HCI\_VS\_HW\_VAR\_NORDIC\_NRF52X](#a990c9b5feb8fa1756d2270127a8909f9)   0x0002 |
| #define | [BT\_HCI\_VS\_HW\_VAR\_NORDIC\_NRF53X](#a040e6267e8b8cd77db9668f018d9cc83)   0x0003 |
| #define | [BT\_HCI\_VS\_HW\_VAR\_NORDIC\_NRF54HX](#af6d066382f1d824b14d32b2d67f5d353)   0x0004 |
| #define | [BT\_HCI\_VS\_HW\_VAR\_NORDIC\_NRF54LX](#ab88e2f4a0810421cbe017c8c709ace7e)   0x0005 |
| #define | [BT\_HCI\_VS\_FW\_VAR\_STANDARD\_CTLR](#ac7e92cbb6a56d20b641be9304372a457)   0x0001 |
| #define | [BT\_HCI\_VS\_FW\_VAR\_VS\_CTLR](#aa41b3f0e21f47343262aca3648c1f02d)   0x0002 |
| #define | [BT\_HCI\_VS\_FW\_VAR\_FW\_LOADER](#a6514cac9da9792697b18a2bf7906aaae)   0x0003 |
| #define | [BT\_HCI\_VS\_FW\_VAR\_RESCUE\_IMG](#a551e878d9131dfc94f9a2ac304661e87)   0x0004 |
| #define | [BT\_HCI\_OP\_VS\_READ\_VERSION\_INFO](#a7877a1d36a2370abd622eef05cf25795)   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0001) |
| #define | [BT\_HCI\_OP\_VS\_READ\_SUPPORTED\_COMMANDS](#aeb5ac33d62cbd0c1db44a387fe99520c)   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0002) |
| #define | [BT\_HCI\_OP\_VS\_READ\_SUPPORTED\_FEATURES](#a77537f2ac77e6f4b25b840726899bb8d)   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0003) |
| #define | [BT\_HCI\_OP\_VS\_SET\_EVENT\_MASK](#a3d99ba16d2510f12c9b8a7fd7cd6e5e9)   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0004) |
| #define | [BT\_HCI\_VS\_RESET\_SOFT](#a2c47a3d7d4b69e33b5caf5e69ae80abf)   0x00 |
| #define | [BT\_HCI\_VS\_RESET\_HARD](#a50933b6556620154780af3c54ee987a5)   0x01 |
| #define | [BT\_HCI\_OP\_VS\_RESET](#ad3e609f9713edcc0fd5a23fa6042df6d)   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0005) |
| #define | [BT\_HCI\_OP\_VS\_WRITE\_BD\_ADDR](#a81e2e5d7a5c4def4b86ab7074551c5bf)   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0006) |
| #define | [BT\_HCI\_VS\_TRACE\_DISABLED](#afd977fec9cc90cc3e3f304dbb181fac4)   0x00 |
| #define | [BT\_HCI\_VS\_TRACE\_ENABLED](#a22c18b5e3fc458394ef9d20595ff5019)   0x01 |
| #define | [BT\_HCI\_VS\_TRACE\_HCI\_EVTS](#a3851c5deb79a1530e448a8cfa0eed2ed)   0x00 |
| #define | [BT\_HCI\_VS\_TRACE\_VDC](#a72f7e148fe28d21381870f57b30b87e1)   0x01 |
| #define | [BT\_HCI\_OP\_VS\_SET\_TRACE\_ENABLE](#a285f127f83f4c241372aa7258b4cad70)   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0007) |
| #define | [BT\_HCI\_OP\_VS\_READ\_BUILD\_INFO](#a6a4f182f0aeeb80e59474f785adda864)   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0008) |
| #define | [BT\_HCI\_OP\_VS\_READ\_STATIC\_ADDRS](#a0306297daa39e9b73c0953b56ac0fb16)   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0009) |
| #define | [BT\_HCI\_OP\_VS\_READ\_KEY\_HIERARCHY\_ROOTS](#a11cb133e491f6ed0e796f2cb6cd07731)   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x000a) |
| #define | [BT\_HCI\_OP\_VS\_READ\_CHIP\_TEMP](#aabf7e4c3ac3b35f22787ad9a448b8220)   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x000b) |
| #define | [BT\_HCI\_VS\_VID\_ANDROID](#a8f9f21d0b193bfdd1e4d1a98b4a96f04)   0x0001 |
| #define | [BT\_HCI\_VS\_VID\_MICROSOFT](#ab028da372f594f1e698335c3f083bd7f)   0x0002 |
| #define | [BT\_HCI\_OP\_VS\_READ\_HOST\_STACK\_CMDS](#a33eb32eabc404d0a73a0b75523210778)   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x000c) |
| #define | [BT\_HCI\_VS\_SCAN\_REQ\_REPORTS\_DISABLED](#a4025336d067b79bead25b45de0ed33cf)   0x00 |
| #define | [BT\_HCI\_VS\_SCAN\_REQ\_REPORTS\_ENABLED](#a7be2294229731b3a004788a739d6f616)   0x01 |
| #define | [BT\_HCI\_OP\_VS\_SET\_SCAN\_REQ\_REPORTS](#ac1e36447ba26e70b4a95073e200cc549)   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x000d) |
| #define | [BT\_HCI\_VS\_LL\_HANDLE\_TYPE\_ADV](#a1f0308641bb308088c49ca241d1293a8)   0x00 |
| #define | [BT\_HCI\_VS\_LL\_HANDLE\_TYPE\_SCAN](#a36e1663258f24c7f5ea8235efcb8b1f6)   0x01 |
| #define | [BT\_HCI\_VS\_LL\_HANDLE\_TYPE\_CONN](#a9ae772dcf1042953552a44c41d41f3e9)   0x02 |
| #define | [BT\_HCI\_VS\_LL\_TX\_POWER\_LEVEL\_NO\_PREF](#a17d4ed99163918297a67a4c00de38728)   0x7F |
| #define | [BT\_HCI\_OP\_VS\_WRITE\_TX\_POWER\_LEVEL](#a29b5fda3541bfd8d69db72e46688d180)   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x000e) |
| #define | [BT\_HCI\_OP\_VS\_READ\_TX\_POWER\_LEVEL](#ad18fb75b6b25758cec63ea30ada16394)   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x000f) |
| #define | [BT\_HCI\_OP\_VS\_READ\_USB\_TRANSPORT\_MODE](#ae51d60b72e66a4eae8e5d608e0ab339b)   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0010) |
| #define | [BT\_HCI\_VS\_USB\_H2\_MODE](#a86badb7e68535ef6d741e03c63811578)   0x00 |
| #define | [BT\_HCI\_VS\_USB\_H4\_MODE](#a758ccb4c0f666df106f550af15025e02)   0x01 |
| #define | [BT\_HCI\_OP\_VS\_SET\_USB\_TRANSPORT\_MODE](#adcf0e45c997c88301a5f4ba9240eb071)   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0011) |
| #define | [BT\_HCI\_OP\_VS\_SET\_MIN\_NUM\_USED\_CHANS](#a6c499204a11f76fe28cc88df665f4af0)   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0012) |
| #define | [BT\_HCI\_EVT\_VS\_FATAL\_ERROR](#a32cd953a56ecfc3eb62b71a8d626c93d)   0x02 |
| #define | [BT\_HCI\_EVT\_VS\_ERROR\_DATA\_TYPE\_STACK\_FRAME](#a20356ed318eead6aab20ef19b6d7c0df)   0x01 |
| #define | [BT\_HCI\_EVT\_VS\_ERROR\_DATA\_TYPE\_CTRL\_ASSERT](#ae9900729ac120c6fb68314b1e0984516)   0x02 |
| #define | [BT\_HCI\_EVT\_VS\_ERROR\_DATA\_TYPE\_TRACE](#a7ed9dbedd215a7ed4b040b6486d49b98)   0x03 |
| #define | [BT\_HCI\_EVT\_VS\_ERROR\_CPU\_TYPE\_CORTEX\_M](#a36a880f6a4f53465f38f70387b52b006)   0x01 |
| #define | [BT\_HCI\_VS\_TRACE\_LMP\_TX](#aa56a360e3cdf72fc87216685179edd41)   0x01 |
| #define | [BT\_HCI\_VS\_TRACE\_LMP\_RX](#aa27a4038be1c6e9cfb756e78d9b07df9)   0x02 |
| #define | [BT\_HCI\_VS\_TRACE\_LLCP\_TX](#a4a212cd52bdd9343bdab8d27ae5d650e)   0x03 |
| #define | [BT\_HCI\_VS\_TRACE\_LLCP\_RX](#a2c69ab6f964ed5cd95419a9771363b64)   0x04 |
| #define | [BT\_HCI\_VS\_TRACE\_LE\_CONN\_IND](#affed427819b721735e31fbcc52f40b5f)   0x05 |
| #define | [BT\_HCI\_EVT\_VS\_TRACE\_INFO](#a43dd9ebf0a175aa0bc244f99df278344)   0x03 |
| #define | [BT\_HCI\_EVT\_VS\_SCAN\_REQ\_RX](#ac4fae4567bb2ba2866ed24ccfc328f63)   0x04 |
| #define | [BT\_HCI\_EVT\_VS\_LE\_CONNECTIONLESS\_IQ\_REPORT](#a8b0ced9392cbf33794100794f964d53f)   0x5 |
| #define | [BT\_HCI\_VS\_LE\_CTE\_REPORT\_NO\_VALID\_SAMPLE](#a71d87ba67638aca600ebbe615a0d4122)   0x8000 |
| #define | [BT\_HCI\_EVT\_VS\_LE\_CONNECTION\_IQ\_REPORT](#a6066be0390be7f611e0e3f4bfab030df)   0x6 |
| #define | [BT\_EVT\_MASK\_VS\_FATAL\_ERROR](#a365da8f1041d55948caa4bf60ea349bd)   [BT\_EVT\_BIT](hci__types_8h.md#a25201544478590f6ee87a829410c612b)(1) |
| #define | [BT\_EVT\_MASK\_VS\_TRACE\_INFO](#aae4f865bf37b8933de070e16ea3047ec)   [BT\_EVT\_BIT](hci__types_8h.md#a25201544478590f6ee87a829410c612b)(2) |
| #define | [BT\_EVT\_MASK\_VS\_SCAN\_REQ\_RX](#a9b4fcdd0de4197b3eb1ac65602e30408)   [BT\_EVT\_BIT](hci__types_8h.md#a25201544478590f6ee87a829410c612b)(3) |
| #define | [BT\_EVT\_MASK\_VS\_LE\_CONNECTIONLESS\_IQ\_REPORT](#a74d2cf07f64f35318ec4ba24fd570dff)   [BT\_EVT\_BIT](hci__types_8h.md#a25201544478590f6ee87a829410c612b)(4) |
| #define | [BT\_EVT\_MASK\_VS\_LE\_CONNECTION\_IQ\_REPORT](#a3971e9541300e12abb4ff36679d9b1f1)   [BT\_EVT\_BIT](hci__types_8h.md#a25201544478590f6ee87a829410c612b)(5) |
| #define | [DEFAULT\_VS\_EVT\_MASK](#a2f8e8f0070bde0e62019c71cc343fbe6) |
| #define | [BT\_HCI\_MESH\_REVISION](#aeb5fdec34a0dfbf5d56a1aa42ba53318)   0x01 |
| #define | [BT\_HCI\_OP\_VS\_MESH](#ad03814f2ae0c377234c5a340388b6ad1)   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0042) |
| #define | [BT\_HCI\_MESH\_EVT\_PREFIX](#a4817a57b69eda704a5a85198aa734792)   0xF0 |
| #define | [BT\_HCI\_OC\_MESH\_GET\_OPTS](#af4cbb4f987c728312a0d00bea62db1c6)   0x00 |
| #define | [BT\_HCI\_MESH\_PATTERN\_LEN\_MAX](#aa31c2257092c0fdce4865ad5af1031ad)   0x0f |
| #define | [BT\_HCI\_OC\_MESH\_SET\_SCAN\_FILTER](#af22f7e03d43595b10ebb6b2cfbe26540)   0x01 |
| #define | [BT\_HCI\_OC\_MESH\_ADVERTISE](#ac73a04914ed07491fde6d463d111a9e2)   0x02 |
| #define | [BT\_HCI\_OC\_MESH\_ADVERTISE\_TIMED](#a9f894b55f3db9df8bb2f710eb736ef1a)   0x03 |
| #define | [BT\_HCI\_OC\_MESH\_ADVERTISE\_CANCEL](#a02491eb40b1874b4fdfb9eac5c3520c0)   0x04 |
| #define | [BT\_HCI\_OC\_MESH\_SET\_SCANNING](#a4225e58654df90330fe007a8e99f4bdb)   0x05 |
| #define | [BT\_HCI\_EVT\_MESH\_ADV\_COMPLETE](#af6e0159b30b73f3bbe8f5df7cdad8ef6)   0x00 |
| #define | [BT\_HCI\_EVT\_MESH\_SCANNING\_REPORT](#a77e3ea0a8f95449a11e4119c30313fe9)   0x01 |

| Functions | |
| --- | --- |
| struct [net\_buf](structnet__buf.md) \* | [hci\_vs\_err\_stack\_frame](#aa90c2106bbb977f1ea8532212ff01b4d) ([unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int reason, const struct [arch\_esf](structarch__esf.md) \*esf) |
| struct [net\_buf](structnet__buf.md) \* | [hci\_vs\_err\_trace](#a9a91c493cc947492d5a172a15abe9a4e) (const char \*file, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) line, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) pc) |
| struct [net\_buf](structnet__buf.md) \* | [hci\_vs\_err\_assert](#afc9ea0e4f2260bf59336f2c66532d9b1) (const char \*file, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) line) |

## Macro Definition Documentation

## [◆ ](#a365da8f1041d55948caa4bf60ea349bd)BT\_EVT\_MASK\_VS\_FATAL\_ERROR

| #define BT\_EVT\_MASK\_VS\_FATAL\_ERROR   [BT\_EVT\_BIT](hci__types_8h.md#a25201544478590f6ee87a829410c612b)(1) |
| --- |

## [◆ ](#a3971e9541300e12abb4ff36679d9b1f1)BT\_EVT\_MASK\_VS\_LE\_CONNECTION\_IQ\_REPORT

| #define BT\_EVT\_MASK\_VS\_LE\_CONNECTION\_IQ\_REPORT   [BT\_EVT\_BIT](hci__types_8h.md#a25201544478590f6ee87a829410c612b)(5) |
| --- |

## [◆ ](#a74d2cf07f64f35318ec4ba24fd570dff)BT\_EVT\_MASK\_VS\_LE\_CONNECTIONLESS\_IQ\_REPORT

| #define BT\_EVT\_MASK\_VS\_LE\_CONNECTIONLESS\_IQ\_REPORT   [BT\_EVT\_BIT](hci__types_8h.md#a25201544478590f6ee87a829410c612b)(4) |
| --- |

## [◆ ](#a9b4fcdd0de4197b3eb1ac65602e30408)BT\_EVT\_MASK\_VS\_SCAN\_REQ\_RX

| #define BT\_EVT\_MASK\_VS\_SCAN\_REQ\_RX   [BT\_EVT\_BIT](hci__types_8h.md#a25201544478590f6ee87a829410c612b)(3) |
| --- |

## [◆ ](#aae4f865bf37b8933de070e16ea3047ec)BT\_EVT\_MASK\_VS\_TRACE\_INFO

| #define BT\_EVT\_MASK\_VS\_TRACE\_INFO   [BT\_EVT\_BIT](hci__types_8h.md#a25201544478590f6ee87a829410c612b)(2) |
| --- |

## [◆ ](#af6e0159b30b73f3bbe8f5df7cdad8ef6)BT\_HCI\_EVT\_MESH\_ADV\_COMPLETE

| #define BT\_HCI\_EVT\_MESH\_ADV\_COMPLETE   0x00 |
| --- |

## [◆ ](#a77e3ea0a8f95449a11e4119c30313fe9)BT\_HCI\_EVT\_MESH\_SCANNING\_REPORT

| #define BT\_HCI\_EVT\_MESH\_SCANNING\_REPORT   0x01 |
| --- |

## [◆ ](#a36a880f6a4f53465f38f70387b52b006)BT\_HCI\_EVT\_VS\_ERROR\_CPU\_TYPE\_CORTEX\_M

| #define BT\_HCI\_EVT\_VS\_ERROR\_CPU\_TYPE\_CORTEX\_M   0x01 |
| --- |

## [◆ ](#ae9900729ac120c6fb68314b1e0984516)BT\_HCI\_EVT\_VS\_ERROR\_DATA\_TYPE\_CTRL\_ASSERT

| #define BT\_HCI\_EVT\_VS\_ERROR\_DATA\_TYPE\_CTRL\_ASSERT   0x02 |
| --- |

## [◆ ](#a20356ed318eead6aab20ef19b6d7c0df)BT\_HCI\_EVT\_VS\_ERROR\_DATA\_TYPE\_STACK\_FRAME

| #define BT\_HCI\_EVT\_VS\_ERROR\_DATA\_TYPE\_STACK\_FRAME   0x01 |
| --- |

## [◆ ](#a7ed9dbedd215a7ed4b040b6486d49b98)BT\_HCI\_EVT\_VS\_ERROR\_DATA\_TYPE\_TRACE

| #define BT\_HCI\_EVT\_VS\_ERROR\_DATA\_TYPE\_TRACE   0x03 |
| --- |

## [◆ ](#a32cd953a56ecfc3eb62b71a8d626c93d)BT\_HCI\_EVT\_VS\_FATAL\_ERROR

| #define BT\_HCI\_EVT\_VS\_FATAL\_ERROR   0x02 |
| --- |

## [◆ ](#a6066be0390be7f611e0e3f4bfab030df)BT\_HCI\_EVT\_VS\_LE\_CONNECTION\_IQ\_REPORT

| #define BT\_HCI\_EVT\_VS\_LE\_CONNECTION\_IQ\_REPORT   0x6 |
| --- |

## [◆ ](#a8b0ced9392cbf33794100794f964d53f)BT\_HCI\_EVT\_VS\_LE\_CONNECTIONLESS\_IQ\_REPORT

| #define BT\_HCI\_EVT\_VS\_LE\_CONNECTIONLESS\_IQ\_REPORT   0x5 |
| --- |

## [◆ ](#ac4fae4567bb2ba2866ed24ccfc328f63)BT\_HCI\_EVT\_VS\_SCAN\_REQ\_RX

| #define BT\_HCI\_EVT\_VS\_SCAN\_REQ\_RX   0x04 |
| --- |

## [◆ ](#a43dd9ebf0a175aa0bc244f99df278344)BT\_HCI\_EVT\_VS\_TRACE\_INFO

| #define BT\_HCI\_EVT\_VS\_TRACE\_INFO   0x03 |
| --- |

## [◆ ](#a4817a57b69eda704a5a85198aa734792)BT\_HCI\_MESH\_EVT\_PREFIX

| #define BT\_HCI\_MESH\_EVT\_PREFIX   0xF0 |
| --- |

## [◆ ](#aa31c2257092c0fdce4865ad5af1031ad)BT\_HCI\_MESH\_PATTERN\_LEN\_MAX

| #define BT\_HCI\_MESH\_PATTERN\_LEN\_MAX   0x0f |
| --- |

## [◆ ](#aeb5fdec34a0dfbf5d56a1aa42ba53318)BT\_HCI\_MESH\_REVISION

| #define BT\_HCI\_MESH\_REVISION   0x01 |
| --- |

## [◆ ](#ac73a04914ed07491fde6d463d111a9e2)BT\_HCI\_OC\_MESH\_ADVERTISE

| #define BT\_HCI\_OC\_MESH\_ADVERTISE   0x02 |
| --- |

## [◆ ](#a02491eb40b1874b4fdfb9eac5c3520c0)BT\_HCI\_OC\_MESH\_ADVERTISE\_CANCEL

| #define BT\_HCI\_OC\_MESH\_ADVERTISE\_CANCEL   0x04 |
| --- |

## [◆ ](#a9f894b55f3db9df8bb2f710eb736ef1a)BT\_HCI\_OC\_MESH\_ADVERTISE\_TIMED

| #define BT\_HCI\_OC\_MESH\_ADVERTISE\_TIMED   0x03 |
| --- |

## [◆ ](#af4cbb4f987c728312a0d00bea62db1c6)BT\_HCI\_OC\_MESH\_GET\_OPTS

| #define BT\_HCI\_OC\_MESH\_GET\_OPTS   0x00 |
| --- |

## [◆ ](#af22f7e03d43595b10ebb6b2cfbe26540)BT\_HCI\_OC\_MESH\_SET\_SCAN\_FILTER

| #define BT\_HCI\_OC\_MESH\_SET\_SCAN\_FILTER   0x01 |
| --- |

## [◆ ](#a4225e58654df90330fe007a8e99f4bdb)BT\_HCI\_OC\_MESH\_SET\_SCANNING

| #define BT\_HCI\_OC\_MESH\_SET\_SCANNING   0x05 |
| --- |

## [◆ ](#ad03814f2ae0c377234c5a340388b6ad1)BT\_HCI\_OP\_VS\_MESH

| #define BT\_HCI\_OP\_VS\_MESH   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0042) |
| --- |

## [◆ ](#a6a4f182f0aeeb80e59474f785adda864)BT\_HCI\_OP\_VS\_READ\_BUILD\_INFO

| #define BT\_HCI\_OP\_VS\_READ\_BUILD\_INFO   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0008) |
| --- |

## [◆ ](#aabf7e4c3ac3b35f22787ad9a448b8220)BT\_HCI\_OP\_VS\_READ\_CHIP\_TEMP

| #define BT\_HCI\_OP\_VS\_READ\_CHIP\_TEMP   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x000b) |
| --- |

## [◆ ](#a33eb32eabc404d0a73a0b75523210778)BT\_HCI\_OP\_VS\_READ\_HOST\_STACK\_CMDS

| #define BT\_HCI\_OP\_VS\_READ\_HOST\_STACK\_CMDS   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x000c) |
| --- |

## [◆ ](#a11cb133e491f6ed0e796f2cb6cd07731)BT\_HCI\_OP\_VS\_READ\_KEY\_HIERARCHY\_ROOTS

| #define BT\_HCI\_OP\_VS\_READ\_KEY\_HIERARCHY\_ROOTS   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x000a) |
| --- |

## [◆ ](#a0306297daa39e9b73c0953b56ac0fb16)BT\_HCI\_OP\_VS\_READ\_STATIC\_ADDRS

| #define BT\_HCI\_OP\_VS\_READ\_STATIC\_ADDRS   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0009) |
| --- |

## [◆ ](#aeb5ac33d62cbd0c1db44a387fe99520c)BT\_HCI\_OP\_VS\_READ\_SUPPORTED\_COMMANDS

| #define BT\_HCI\_OP\_VS\_READ\_SUPPORTED\_COMMANDS   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0002) |
| --- |

## [◆ ](#a77537f2ac77e6f4b25b840726899bb8d)BT\_HCI\_OP\_VS\_READ\_SUPPORTED\_FEATURES

| #define BT\_HCI\_OP\_VS\_READ\_SUPPORTED\_FEATURES   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0003) |
| --- |

## [◆ ](#ad18fb75b6b25758cec63ea30ada16394)BT\_HCI\_OP\_VS\_READ\_TX\_POWER\_LEVEL

| #define BT\_HCI\_OP\_VS\_READ\_TX\_POWER\_LEVEL   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x000f) |
| --- |

## [◆ ](#ae51d60b72e66a4eae8e5d608e0ab339b)BT\_HCI\_OP\_VS\_READ\_USB\_TRANSPORT\_MODE

| #define BT\_HCI\_OP\_VS\_READ\_USB\_TRANSPORT\_MODE   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0010) |
| --- |

## [◆ ](#a7877a1d36a2370abd622eef05cf25795)BT\_HCI\_OP\_VS\_READ\_VERSION\_INFO

| #define BT\_HCI\_OP\_VS\_READ\_VERSION\_INFO   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0001) |
| --- |

## [◆ ](#ad3e609f9713edcc0fd5a23fa6042df6d)BT\_HCI\_OP\_VS\_RESET

| #define BT\_HCI\_OP\_VS\_RESET   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0005) |
| --- |

## [◆ ](#a3d99ba16d2510f12c9b8a7fd7cd6e5e9)BT\_HCI\_OP\_VS\_SET\_EVENT\_MASK

| #define BT\_HCI\_OP\_VS\_SET\_EVENT\_MASK   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0004) |
| --- |

## [◆ ](#a6c499204a11f76fe28cc88df665f4af0)BT\_HCI\_OP\_VS\_SET\_MIN\_NUM\_USED\_CHANS

| #define BT\_HCI\_OP\_VS\_SET\_MIN\_NUM\_USED\_CHANS   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0012) |
| --- |

## [◆ ](#ac1e36447ba26e70b4a95073e200cc549)BT\_HCI\_OP\_VS\_SET\_SCAN\_REQ\_REPORTS

| #define BT\_HCI\_OP\_VS\_SET\_SCAN\_REQ\_REPORTS   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x000d) |
| --- |

## [◆ ](#a285f127f83f4c241372aa7258b4cad70)BT\_HCI\_OP\_VS\_SET\_TRACE\_ENABLE

| #define BT\_HCI\_OP\_VS\_SET\_TRACE\_ENABLE   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0007) |
| --- |

## [◆ ](#adcf0e45c997c88301a5f4ba9240eb071)BT\_HCI\_OP\_VS\_SET\_USB\_TRANSPORT\_MODE

| #define BT\_HCI\_OP\_VS\_SET\_USB\_TRANSPORT\_MODE   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0011) |
| --- |

## [◆ ](#a81e2e5d7a5c4def4b86ab7074551c5bf)BT\_HCI\_OP\_VS\_WRITE\_BD\_ADDR

| #define BT\_HCI\_OP\_VS\_WRITE\_BD\_ADDR   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x0006) |
| --- |

## [◆ ](#a29b5fda3541bfd8d69db72e46688d180)BT\_HCI\_OP\_VS\_WRITE\_TX\_POWER\_LEVEL

| #define BT\_HCI\_OP\_VS\_WRITE\_TX\_POWER\_LEVEL   [BT\_OP](hci__types_8h.md#a7e006e0f69c498601f2c64a4ce3d8101)([BT\_OGF\_VS](hci__types_8h.md#a6b682cb6e4f489ffb67b05280b3dbd65), 0x000e) |
| --- |

## [◆ ](#a6514cac9da9792697b18a2bf7906aaae)BT\_HCI\_VS\_FW\_VAR\_FW\_LOADER

| #define BT\_HCI\_VS\_FW\_VAR\_FW\_LOADER   0x0003 |
| --- |

## [◆ ](#a551e878d9131dfc94f9a2ac304661e87)BT\_HCI\_VS\_FW\_VAR\_RESCUE\_IMG

| #define BT\_HCI\_VS\_FW\_VAR\_RESCUE\_IMG   0x0004 |
| --- |

## [◆ ](#ac7e92cbb6a56d20b641be9304372a457)BT\_HCI\_VS\_FW\_VAR\_STANDARD\_CTLR

| #define BT\_HCI\_VS\_FW\_VAR\_STANDARD\_CTLR   0x0001 |
| --- |

## [◆ ](#aa41b3f0e21f47343262aca3648c1f02d)BT\_HCI\_VS\_FW\_VAR\_VS\_CTLR

| #define BT\_HCI\_VS\_FW\_VAR\_VS\_CTLR   0x0002 |
| --- |

## [◆ ](#a35bf58cbe551d8e3e56fa687828a5ee7)BT\_HCI\_VS\_HW\_PLAT\_INTEL

| #define BT\_HCI\_VS\_HW\_PLAT\_INTEL   0x0001 |
| --- |

## [◆ ](#a533362f9e60a77ce5c787d26241a2200)BT\_HCI\_VS\_HW\_PLAT\_NORDIC

| #define BT\_HCI\_VS\_HW\_PLAT\_NORDIC   0x0002 |
| --- |

## [◆ ](#a0813745772dc53d5eb8d78ca016e0b3c)BT\_HCI\_VS\_HW\_PLAT\_NXP

| #define BT\_HCI\_VS\_HW\_PLAT\_NXP   0x0003 |
| --- |

## [◆ ](#aef40f22484598bcd15885f1cf27a3a7e)BT\_HCI\_VS\_HW\_VAR\_NORDIC\_NRF51X

| #define BT\_HCI\_VS\_HW\_VAR\_NORDIC\_NRF51X   0x0001 |
| --- |

## [◆ ](#a990c9b5feb8fa1756d2270127a8909f9)BT\_HCI\_VS\_HW\_VAR\_NORDIC\_NRF52X

| #define BT\_HCI\_VS\_HW\_VAR\_NORDIC\_NRF52X   0x0002 |
| --- |

## [◆ ](#a040e6267e8b8cd77db9668f018d9cc83)BT\_HCI\_VS\_HW\_VAR\_NORDIC\_NRF53X

| #define BT\_HCI\_VS\_HW\_VAR\_NORDIC\_NRF53X   0x0003 |
| --- |

## [◆ ](#af6d066382f1d824b14d32b2d67f5d353)BT\_HCI\_VS\_HW\_VAR\_NORDIC\_NRF54HX

| #define BT\_HCI\_VS\_HW\_VAR\_NORDIC\_NRF54HX   0x0004 |
| --- |

## [◆ ](#ab88e2f4a0810421cbe017c8c709ace7e)BT\_HCI\_VS\_HW\_VAR\_NORDIC\_NRF54LX

| #define BT\_HCI\_VS\_HW\_VAR\_NORDIC\_NRF54LX   0x0005 |
| --- |

## [◆ ](#a71d87ba67638aca600ebbe615a0d4122)BT\_HCI\_VS\_LE\_CTE\_REPORT\_NO\_VALID\_SAMPLE

| #define BT\_HCI\_VS\_LE\_CTE\_REPORT\_NO\_VALID\_SAMPLE   0x8000 |
| --- |

## [◆ ](#a1f0308641bb308088c49ca241d1293a8)BT\_HCI\_VS\_LL\_HANDLE\_TYPE\_ADV

| #define BT\_HCI\_VS\_LL\_HANDLE\_TYPE\_ADV   0x00 |
| --- |

## [◆ ](#a9ae772dcf1042953552a44c41d41f3e9)BT\_HCI\_VS\_LL\_HANDLE\_TYPE\_CONN

| #define BT\_HCI\_VS\_LL\_HANDLE\_TYPE\_CONN   0x02 |
| --- |

## [◆ ](#a36e1663258f24c7f5ea8235efcb8b1f6)BT\_HCI\_VS\_LL\_HANDLE\_TYPE\_SCAN

| #define BT\_HCI\_VS\_LL\_HANDLE\_TYPE\_SCAN   0x01 |
| --- |

## [◆ ](#a17d4ed99163918297a67a4c00de38728)BT\_HCI\_VS\_LL\_TX\_POWER\_LEVEL\_NO\_PREF

| #define BT\_HCI\_VS\_LL\_TX\_POWER\_LEVEL\_NO\_PREF   0x7F |
| --- |

## [◆ ](#a50933b6556620154780af3c54ee987a5)BT\_HCI\_VS\_RESET\_HARD

| #define BT\_HCI\_VS\_RESET\_HARD   0x01 |
| --- |

## [◆ ](#a2c47a3d7d4b69e33b5caf5e69ae80abf)BT\_HCI\_VS\_RESET\_SOFT

| #define BT\_HCI\_VS\_RESET\_SOFT   0x00 |
| --- |

## [◆ ](#a4025336d067b79bead25b45de0ed33cf)BT\_HCI\_VS\_SCAN\_REQ\_REPORTS\_DISABLED

| #define BT\_HCI\_VS\_SCAN\_REQ\_REPORTS\_DISABLED   0x00 |
| --- |

## [◆ ](#a7be2294229731b3a004788a739d6f616)BT\_HCI\_VS\_SCAN\_REQ\_REPORTS\_ENABLED

| #define BT\_HCI\_VS\_SCAN\_REQ\_REPORTS\_ENABLED   0x01 |
| --- |

## [◆ ](#afd977fec9cc90cc3e3f304dbb181fac4)BT\_HCI\_VS\_TRACE\_DISABLED

| #define BT\_HCI\_VS\_TRACE\_DISABLED   0x00 |
| --- |

## [◆ ](#a22c18b5e3fc458394ef9d20595ff5019)BT\_HCI\_VS\_TRACE\_ENABLED

| #define BT\_HCI\_VS\_TRACE\_ENABLED   0x01 |
| --- |

## [◆ ](#a3851c5deb79a1530e448a8cfa0eed2ed)BT\_HCI\_VS\_TRACE\_HCI\_EVTS

| #define BT\_HCI\_VS\_TRACE\_HCI\_EVTS   0x00 |
| --- |

## [◆ ](#affed427819b721735e31fbcc52f40b5f)BT\_HCI\_VS\_TRACE\_LE\_CONN\_IND

| #define BT\_HCI\_VS\_TRACE\_LE\_CONN\_IND   0x05 |
| --- |

## [◆ ](#a2c69ab6f964ed5cd95419a9771363b64)BT\_HCI\_VS\_TRACE\_LLCP\_RX

| #define BT\_HCI\_VS\_TRACE\_LLCP\_RX   0x04 |
| --- |

## [◆ ](#a4a212cd52bdd9343bdab8d27ae5d650e)BT\_HCI\_VS\_TRACE\_LLCP\_TX

| #define BT\_HCI\_VS\_TRACE\_LLCP\_TX   0x03 |
| --- |

## [◆ ](#aa27a4038be1c6e9cfb756e78d9b07df9)BT\_HCI\_VS\_TRACE\_LMP\_RX

| #define BT\_HCI\_VS\_TRACE\_LMP\_RX   0x02 |
| --- |

## [◆ ](#aa56a360e3cdf72fc87216685179edd41)BT\_HCI\_VS\_TRACE\_LMP\_TX

| #define BT\_HCI\_VS\_TRACE\_LMP\_TX   0x01 |
| --- |

## [◆ ](#a72f7e148fe28d21381870f57b30b87e1)BT\_HCI\_VS\_TRACE\_VDC

| #define BT\_HCI\_VS\_TRACE\_VDC   0x01 |
| --- |

## [◆ ](#a86badb7e68535ef6d741e03c63811578)BT\_HCI\_VS\_USB\_H2\_MODE

| #define BT\_HCI\_VS\_USB\_H2\_MODE   0x00 |
| --- |

## [◆ ](#a758ccb4c0f666df106f550af15025e02)BT\_HCI\_VS\_USB\_H4\_MODE

| #define BT\_HCI\_VS\_USB\_H4\_MODE   0x01 |
| --- |

## [◆ ](#a8f9f21d0b193bfdd1e4d1a98b4a96f04)BT\_HCI\_VS\_VID\_ANDROID

| #define BT\_HCI\_VS\_VID\_ANDROID   0x0001 |
| --- |

## [◆ ](#ab028da372f594f1e698335c3f083bd7f)BT\_HCI\_VS\_VID\_MICROSOFT

| #define BT\_HCI\_VS\_VID\_MICROSOFT   0x0002 |
| --- |

## [◆ ](#aaae2460cf69b0ad51aedf57c72d42103)BT\_VS\_CMD\_BIT\_READ\_BUILD\_INFO

| #define BT\_VS\_CMD\_BIT\_READ\_BUILD\_INFO   7 |
| --- |

## [◆ ](#a96cee049fdf09d1e22aa2204a080c956)BT\_VS\_CMD\_BIT\_READ\_CHIP\_TEMP

| #define BT\_VS\_CMD\_BIT\_READ\_CHIP\_TEMP   10 |
| --- |

## [◆ ](#a072226e7bfd637f71a03971e18d795e5)BT\_VS\_CMD\_BIT\_READ\_HOST\_STACK\_CMD

| #define BT\_VS\_CMD\_BIT\_READ\_HOST\_STACK\_CMD   11 |
| --- |

## [◆ ](#aa8b39f4ac968cf0cdb18073de1aa1ad5)BT\_VS\_CMD\_BIT\_READ\_KEY\_ROOTS

| #define BT\_VS\_CMD\_BIT\_READ\_KEY\_ROOTS   9 |
| --- |

## [◆ ](#a27e19ec90e057244db7f632887a46ec1)BT\_VS\_CMD\_BIT\_READ\_STATIC\_ADDRS

| #define BT\_VS\_CMD\_BIT\_READ\_STATIC\_ADDRS   8 |
| --- |

## [◆ ](#a9af8f8bde7f33db3f32aa2aa5bda4012)BT\_VS\_CMD\_BIT\_READ\_TX\_POWER

| #define BT\_VS\_CMD\_BIT\_READ\_TX\_POWER   14 |
| --- |

## [◆ ](#a020ca307df4c66bcd4c4f6da42d22e40)BT\_VS\_CMD\_BIT\_RESET

| #define BT\_VS\_CMD\_BIT\_RESET   4 |
| --- |

## [◆ ](#ab1b627847e323e94949b53665e47f20f)BT\_VS\_CMD\_BIT\_SET\_EVT\_MASK

| #define BT\_VS\_CMD\_BIT\_SET\_EVT\_MASK   3 |
| --- |

## [◆ ](#ac16322768bdd4688b2cefb4ea7b8c26f)BT\_VS\_CMD\_BIT\_SET\_SCAN\_REP\_ENABLE

| #define BT\_VS\_CMD\_BIT\_SET\_SCAN\_REP\_ENABLE   12 |
| --- |

## [◆ ](#ad57ee37a93208d3127e5ba36933b0d36)BT\_VS\_CMD\_BIT\_SET\_TRACE\_ENABLE

| #define BT\_VS\_CMD\_BIT\_SET\_TRACE\_ENABLE   6 |
| --- |

## [◆ ](#a2eec9eff49fc0d8f4e4f746dd7498478)BT\_VS\_CMD\_BIT\_SUP\_CMD

| #define BT\_VS\_CMD\_BIT\_SUP\_CMD   1 |
| --- |

## [◆ ](#a418e0fd9c322671c1124835752b25678)BT\_VS\_CMD\_BIT\_SUP\_FEAT

| #define BT\_VS\_CMD\_BIT\_SUP\_FEAT   2 |
| --- |

## [◆ ](#a98cda5172947a82dfee334a5db41b0bb)BT\_VS\_CMD\_BIT\_VERSION

| #define BT\_VS\_CMD\_BIT\_VERSION   0 |
| --- |

## [◆ ](#ac8fa0f7e3d5b802f1797c77d988bc172)BT\_VS\_CMD\_BIT\_WRITE\_BDADDR

| #define BT\_VS\_CMD\_BIT\_WRITE\_BDADDR   5 |
| --- |

## [◆ ](#a3f720e278e3aeefd11e9682d683e448b)BT\_VS\_CMD\_BIT\_WRITE\_TX\_POWER

| #define BT\_VS\_CMD\_BIT\_WRITE\_TX\_POWER   13 |
| --- |

## [◆ ](#aa81a670c17714854306b0044e9fb6392)BT\_VS\_CMD\_READ\_KEY\_ROOTS

| #define BT\_VS\_CMD\_READ\_KEY\_ROOTS | ( |  | *[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](hci__types_8h.md#a6bf20989952fed3726bc45873beb896e)([cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), \

[BT\_VS\_CMD\_BIT\_READ\_KEY\_ROOTS](#aa8b39f4ac968cf0cdb18073de1aa1ad5))

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[BT\_LE\_FEAT\_TEST](hci__types_8h.md#a6bf20989952fed3726bc45873beb896e)

#define BT\_LE\_FEAT\_TEST(feat, n)

**Definition** hci\_types.h:208

[BT\_VS\_CMD\_BIT\_READ\_KEY\_ROOTS](#aa8b39f4ac968cf0cdb18073de1aa1ad5)

#define BT\_VS\_CMD\_BIT\_READ\_KEY\_ROOTS

**Definition** hci\_vs.h:29

## [◆ ](#af5ef90c96d5798cef8ad32f8d6094d53)BT\_VS\_CMD\_READ\_STATIC\_ADDRS

| #define BT\_VS\_CMD\_READ\_STATIC\_ADDRS | ( |  | *[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](hci__types_8h.md#a6bf20989952fed3726bc45873beb896e)([cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), \

[BT\_VS\_CMD\_BIT\_READ\_STATIC\_ADDRS](#a27e19ec90e057244db7f632887a46ec1))

[BT\_VS\_CMD\_BIT\_READ\_STATIC\_ADDRS](#a27e19ec90e057244db7f632887a46ec1)

#define BT\_VS\_CMD\_BIT\_READ\_STATIC\_ADDRS

**Definition** hci\_vs.h:28

## [◆ ](#a6f43e26c34622d9b9b2cf0a6ba53a393)BT\_VS\_CMD\_SUP\_FEAT

| #define BT\_VS\_CMD\_SUP\_FEAT | ( |  | *[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_LE\_FEAT\_TEST](hci__types_8h.md#a6bf20989952fed3726bc45873beb896e)([cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), \

[BT\_VS\_CMD\_BIT\_SUP\_FEAT](#a418e0fd9c322671c1124835752b25678))

[BT\_VS\_CMD\_BIT\_SUP\_FEAT](#a418e0fd9c322671c1124835752b25678)

#define BT\_VS\_CMD\_BIT\_SUP\_FEAT

**Definition** hci\_vs.h:22

## [◆ ](#a2f8e8f0070bde0e62019c71cc343fbe6)DEFAULT\_VS\_EVT\_MASK

| #define DEFAULT\_VS\_EVT\_MASK |
| --- |

**Value:**

[BT\_EVT\_MASK\_VS\_FATAL\_ERROR](#a365da8f1041d55948caa4bf60ea349bd) | [BT\_EVT\_MASK\_VS\_TRACE\_INFO](#aae4f865bf37b8933de070e16ea3047ec) | [BT\_EVT\_MASK\_VS\_SCAN\_REQ\_RX](#a9b4fcdd0de4197b3eb1ac65602e30408) | \

[BT\_EVT\_MASK\_VS\_LE\_CONNECTIONLESS\_IQ\_REPORT](#a74d2cf07f64f35318ec4ba24fd570dff) | \

[BT\_EVT\_MASK\_VS\_LE\_CONNECTION\_IQ\_REPORT](#a3971e9541300e12abb4ff36679d9b1f1)

[BT\_EVT\_MASK\_VS\_FATAL\_ERROR](#a365da8f1041d55948caa4bf60ea349bd)

#define BT\_EVT\_MASK\_VS\_FATAL\_ERROR

**Definition** hci\_vs.h:307

[BT\_EVT\_MASK\_VS\_LE\_CONNECTION\_IQ\_REPORT](#a3971e9541300e12abb4ff36679d9b1f1)

#define BT\_EVT\_MASK\_VS\_LE\_CONNECTION\_IQ\_REPORT

**Definition** hci\_vs.h:311

[BT\_EVT\_MASK\_VS\_LE\_CONNECTIONLESS\_IQ\_REPORT](#a74d2cf07f64f35318ec4ba24fd570dff)

#define BT\_EVT\_MASK\_VS\_LE\_CONNECTIONLESS\_IQ\_REPORT

**Definition** hci\_vs.h:310

[BT\_EVT\_MASK\_VS\_SCAN\_REQ\_RX](#a9b4fcdd0de4197b3eb1ac65602e30408)

#define BT\_EVT\_MASK\_VS\_SCAN\_REQ\_RX

**Definition** hci\_vs.h:309

[BT\_EVT\_MASK\_VS\_TRACE\_INFO](#aae4f865bf37b8933de070e16ea3047ec)

#define BT\_EVT\_MASK\_VS\_TRACE\_INFO

**Definition** hci\_vs.h:308

## Function Documentation

## [◆ ](#afc9ea0e4f2260bf59336f2c66532d9b1)hci\_vs\_err\_assert()

| struct [net\_buf](structnet__buf.md) \* hci\_vs\_err\_assert | ( | const char \* | *file*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *line* ) |

## [◆ ](#aa90c2106bbb977f1ea8532212ff01b4d)hci\_vs\_err\_stack\_frame()

| struct [net\_buf](structnet__buf.md) \* hci\_vs\_err\_stack\_frame | ( | [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | *reason*, |
| --- | --- | --- | --- |
|  |  | const struct [arch\_esf](structarch__esf.md) \* | *esf* ) |

## [◆ ](#a9a91c493cc947492d5a172a15abe9a4e)hci\_vs\_err\_trace()

| struct [net\_buf](structnet__buf.md) \* hci\_vs\_err\_trace | ( | const char \* | *file*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *line*, |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *pc* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [hci\_vs.h](hci__vs_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
