---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/bas_8h.html
original_path: doxygen/html/bas_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bas.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`

[Go to the source code of this file.](bas_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [bt\_bas\_bcs\_flags](group__bt__bas.md#ga56d26a8cde072959e8d8b75ee4fb2819) { [BT\_BAS\_BCS\_BATTERY\_CRITICAL\_STATE](group__bt__bas.md#gga56d26a8cde072959e8d8b75ee4fb2819ad45c2b537f66cc7118357616120fa8a5) = BIT(0) , [BT\_BAS\_BCS\_IMMEDIATE\_SERVICE\_REQUIRED](group__bt__bas.md#gga56d26a8cde072959e8d8b75ee4fb2819af82ae1d0e53efa882ff21d4e67b9ba7a) = BIT(1) } |
|  | Battery Critical Status Characteristic flags. [More...](group__bt__bas.md#ga56d26a8cde072959e8d8b75ee4fb2819) |
| enum | [bt\_bas\_bls\_flags](group__bt__bas.md#ga7c425f7fd9e908e327810f89d7645745) { [BT\_BAS\_BLS\_FLAG\_IDENTIFIER\_PRESENT](group__bt__bas.md#gga7c425f7fd9e908e327810f89d7645745a69d60021c1d1772f461f0e90eadd9b46) = BIT(0) , [BT\_BAS\_BLS\_FLAG\_BATTERY\_LEVEL\_PRESENT](group__bt__bas.md#gga7c425f7fd9e908e327810f89d7645745a74cb90028ebf42119c8c69a3801591ba) = BIT(1) , [BT\_BAS\_BLS\_FLAG\_ADDITIONAL\_STATUS\_PRESENT](group__bt__bas.md#gga7c425f7fd9e908e327810f89d7645745add93cefc8c583aa0edd71ed66edbea3d) = BIT(2) } |
|  | Battery Level Status Characteristic flags. [More...](group__bt__bas.md#ga7c425f7fd9e908e327810f89d7645745) |
| enum | [bt\_bas\_bls\_battery\_present](group__bt__bas.md#ga31d5d4a7184243ffe9d925714de4367f) { [BT\_BAS\_BLS\_BATTERY\_NOT\_PRESENT](group__bt__bas.md#gga31d5d4a7184243ffe9d925714de4367fae373a1d0f3875bafbdcab7c1cca0f522) = 0 , [BT\_BAS\_BLS\_BATTERY\_PRESENT](group__bt__bas.md#gga31d5d4a7184243ffe9d925714de4367fa63b460de845ef9cb7423c82008b2ed49) = 1 } |
|  | Battery Present Status. [More...](group__bt__bas.md#ga31d5d4a7184243ffe9d925714de4367f) |
| enum | [bt\_bas\_bls\_wired\_power\_source](group__bt__bas.md#ga4e3f58a5f7c8715f3f8f24b96229b71c) { [BT\_BAS\_BLS\_WIRED\_POWER\_NOT\_CONNECTED](group__bt__bas.md#gga4e3f58a5f7c8715f3f8f24b96229b71ca98d72b37dce3b29dcc901bb58d3e6acf) = 0 , [BT\_BAS\_BLS\_WIRED\_POWER\_CONNECTED](group__bt__bas.md#gga4e3f58a5f7c8715f3f8f24b96229b71cadabb6df4477b9483e18cd3bd77ef8adc) = 1 , [BT\_BAS\_BLS\_WIRED\_POWER\_UNKNOWN](group__bt__bas.md#gga4e3f58a5f7c8715f3f8f24b96229b71ca2064d10fa9b52c40142eb4f8a9ef2799) = 2 } |
|  | Wired External Power Source Status. [More...](group__bt__bas.md#ga4e3f58a5f7c8715f3f8f24b96229b71c) |
| enum | [bt\_bas\_bls\_wireless\_power\_source](group__bt__bas.md#gaf76a1eea78e9ff5c35977c41b00fb64d) { [BT\_BAS\_BLS\_WIRELESS\_POWER\_NOT\_CONNECTED](group__bt__bas.md#ggaf76a1eea78e9ff5c35977c41b00fb64dab90caed6b5b1fef37f79176ae6221383) = 0 , [BT\_BAS\_BLS\_WIRELESS\_POWER\_CONNECTED](group__bt__bas.md#ggaf76a1eea78e9ff5c35977c41b00fb64da3f2f11b307bb6e641792e4e85fe3a363) = 1 , [BT\_BAS\_BLS\_WIRELESS\_POWER\_UNKNOWN](group__bt__bas.md#ggaf76a1eea78e9ff5c35977c41b00fb64daafeab5f57d1a12770bc9ac95161e1af8) = 2 } |
|  | Wireless External Power Source Status. [More...](group__bt__bas.md#gaf76a1eea78e9ff5c35977c41b00fb64d) |
| enum | [bt\_bas\_bls\_battery\_charge\_state](group__bt__bas.md#ga3584a3e7b7194bf244f414d6860b1313) { [BT\_BAS\_BLS\_CHARGE\_STATE\_UNKNOWN](group__bt__bas.md#gga3584a3e7b7194bf244f414d6860b1313a663b3a9a4490600c56f2784246bbe58c) = 0 , [BT\_BAS\_BLS\_CHARGE\_STATE\_CHARGING](group__bt__bas.md#gga3584a3e7b7194bf244f414d6860b1313a35249a218c5c15a24e9b529991282ab9) = 1 , [BT\_BAS\_BLS\_CHARGE\_STATE\_DISCHARGING\_ACTIVE](group__bt__bas.md#gga3584a3e7b7194bf244f414d6860b1313aba3c8d0d791dae18b6aa3149619e4e02) = 2 , [BT\_BAS\_BLS\_CHARGE\_STATE\_DISCHARGING\_INACTIVE](group__bt__bas.md#gga3584a3e7b7194bf244f414d6860b1313a23a496ecd4b7e7d33ee7a2f0021c4f1a) = 3 } |
|  | Battery Charge State. [More...](group__bt__bas.md#ga3584a3e7b7194bf244f414d6860b1313) |
| enum | [bt\_bas\_bls\_battery\_charge\_level](group__bt__bas.md#gad374826ce9465bbf344b1f25b16c574c) { [BT\_BAS\_BLS\_CHARGE\_LEVEL\_UNKNOWN](group__bt__bas.md#ggad374826ce9465bbf344b1f25b16c574cabdd600d10005a09cbce4f5584cb3bb58) = 0 , [BT\_BAS\_BLS\_CHARGE\_LEVEL\_GOOD](group__bt__bas.md#ggad374826ce9465bbf344b1f25b16c574cae08b7620b5babb731a6c8e8bf12b1387) = 1 , [BT\_BAS\_BLS\_CHARGE\_LEVEL\_LOW](group__bt__bas.md#ggad374826ce9465bbf344b1f25b16c574ca27d8f485ee4ee50bb8d9c02049b9679e) = 2 , [BT\_BAS\_BLS\_CHARGE\_LEVEL\_CRITICAL](group__bt__bas.md#ggad374826ce9465bbf344b1f25b16c574ca46fa5393ea4acefae2d2ffdfaef2a31d) = 3 } |
|  | Battery Charge Level. [More...](group__bt__bas.md#gad374826ce9465bbf344b1f25b16c574c) |
| enum | [bt\_bas\_bls\_battery\_charge\_type](group__bt__bas.md#ga9f09b045f9db8aa2f2e21adb0a65c3aa) {     [BT\_BAS\_BLS\_CHARGE\_TYPE\_UNKNOWN](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaa0c681a700639a1ba8b3cf3e5afc70e64) = 0 , [BT\_BAS\_BLS\_CHARGE\_TYPE\_CONSTANT\_CURRENT](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaa5a9f93290d6b11596771e7e9bbc357af) = 1 , [BT\_BAS\_BLS\_CHARGE\_TYPE\_CONSTANT\_VOLTAGE](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaa5dc3c38414be857fd5d2cf98a0edc730) = 2 , [BT\_BAS\_BLS\_CHARGE\_TYPE\_TRICKLE](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaade1f3bc7dab9c768feb8d70c149ffbda) = 3 ,     [BT\_BAS\_BLS\_CHARGE\_TYPE\_FLOAT](group__bt__bas.md#gga9f09b045f9db8aa2f2e21adb0a65c3aaabbf719d116ec24bbf327c8e7a2eb50c0) = 4   } |
|  | Battery Charge Type. [More...](group__bt__bas.md#ga9f09b045f9db8aa2f2e21adb0a65c3aa) |
| enum | [bt\_bas\_bls\_charging\_fault\_reason](group__bt__bas.md#gad981cab4d2a285ee72481b54836cf35b) { [BT\_BAS\_BLS\_FAULT\_REASON\_NONE](group__bt__bas.md#ggad981cab4d2a285ee72481b54836cf35bab8d7bcea2ab1d76a66727e11a520654a) = 0 , [BT\_BAS\_BLS\_FAULT\_REASON\_BATTERY](group__bt__bas.md#ggad981cab4d2a285ee72481b54836cf35ba7bea7165cbba98284b9941cf8809787f) = BIT(0) , [BT\_BAS\_BLS\_FAULT\_REASON\_EXTERNAL\_POWER](group__bt__bas.md#ggad981cab4d2a285ee72481b54836cf35ba527c9490662f70b789ecb0d37f90df3b) = BIT(1) , [BT\_BAS\_BLS\_FAULT\_REASON\_OTHER](group__bt__bas.md#ggad981cab4d2a285ee72481b54836cf35ba8c70a47828ed3b90c08e742dff3c0ab7) = BIT(2) } |
|  | Charging Fault Reason. [More...](group__bt__bas.md#gad981cab4d2a285ee72481b54836cf35b) |
| enum | [bt\_bas\_bls\_service\_required](group__bt__bas.md#gad410bdd972f09f0314b696ce31e6d82d) { [BT\_BAS\_BLS\_SERVICE\_REQUIRED\_FALSE](group__bt__bas.md#ggad410bdd972f09f0314b696ce31e6d82daa50e305c82d8081877576953e07241db) = 0 , [BT\_BAS\_BLS\_SERVICE\_REQUIRED\_TRUE](group__bt__bas.md#ggad410bdd972f09f0314b696ce31e6d82da683bc2d562e99ae0c691eb3611206f00) = 1 , [BT\_BAS\_BLS\_SERVICE\_REQUIRED\_UNKNOWN](group__bt__bas.md#ggad410bdd972f09f0314b696ce31e6d82dae36621eac964d7f2b8b5959de11ba870) = 2 } |
|  | Service Required Status. [More...](group__bt__bas.md#gad410bdd972f09f0314b696ce31e6d82d) |
| enum | [bt\_bas\_bls\_battery\_fault](group__bt__bas.md#ga6976a11ffe2c9a9b2fff82763be2edee) { [BT\_BAS\_BLS\_BATTERY\_FAULT\_NO](group__bt__bas.md#gga6976a11ffe2c9a9b2fff82763be2edeeab119e2a0a3600269f752dfc7f271edee) = 0 , [BT\_BAS\_BLS\_BATTERY\_FAULT\_YES](group__bt__bas.md#gga6976a11ffe2c9a9b2fff82763be2edeea6af59b287c252dbb04d6ab6cdbbf6d6f) = 1 } |
|  | Battery Fault Status. [More...](group__bt__bas.md#ga6976a11ffe2c9a9b2fff82763be2edee) |

| Functions | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_bas\_get\_battery\_level](group__bt__bas.md#gadbe0f52d04d90372d603af66b693e980) (void) |
|  | Read battery level value. |
| int | [bt\_bas\_set\_battery\_level](group__bt__bas.md#gac8d519830c34b9c8370366e2593dbeba) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level) |
|  | Update battery level value. |
| void | [bt\_bas\_bls\_set\_battery\_present](group__bt__bas.md#ga5e0325af9dcd362dd3c1691832be5677) (enum [bt\_bas\_bls\_battery\_present](group__bt__bas.md#ga31d5d4a7184243ffe9d925714de4367f) present) |
|  | Set the battery present status. |
| void | [bt\_bas\_bls\_set\_wired\_external\_power\_source](group__bt__bas.md#ga7bf36a53494e2ecfbb5ccd218f29f51f) (enum [bt\_bas\_bls\_wired\_power\_source](group__bt__bas.md#ga4e3f58a5f7c8715f3f8f24b96229b71c) source) |
|  | Set the wired external power source status. |
| void | [bt\_bas\_bls\_set\_wireless\_external\_power\_source](group__bt__bas.md#gae1cbafd30e1d78437c78d44df25aa005) (enum [bt\_bas\_bls\_wireless\_power\_source](group__bt__bas.md#gaf76a1eea78e9ff5c35977c41b00fb64d) source) |
|  | Set the wireless external power source status. |
| void | [bt\_bas\_bls\_set\_battery\_charge\_state](group__bt__bas.md#ga60b153c4d291ed4b16ce1f9d2dc1b45d) (enum [bt\_bas\_bls\_battery\_charge\_state](group__bt__bas.md#ga3584a3e7b7194bf244f414d6860b1313) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Set the battery charge state. |
| void | [bt\_bas\_bls\_set\_battery\_charge\_level](group__bt__bas.md#gac8e32530f966c7699d3c28e6685bcee5) (enum [bt\_bas\_bls\_battery\_charge\_level](group__bt__bas.md#gad374826ce9465bbf344b1f25b16c574c) level) |
|  | Set the battery charge level. |
| void | [bt\_bas\_bls\_set\_battery\_charge\_type](group__bt__bas.md#ga3cea34f717f2df01b6f49bed80f27f44) (enum [bt\_bas\_bls\_battery\_charge\_type](group__bt__bas.md#ga9f09b045f9db8aa2f2e21adb0a65c3aa) type) |
|  | Set the battery charge type. |
| void | [bt\_bas\_bls\_set\_charging\_fault\_reason](group__bt__bas.md#ga7996edb35bcca878062360b24036b6f8) (enum [bt\_bas\_bls\_charging\_fault\_reason](group__bt__bas.md#gad981cab4d2a285ee72481b54836cf35b) reason) |
|  | Set the charging fault reason. |
| void | [bt\_bas\_bls\_set\_identifier](group__bt__bas.md#gafd74ef933734960a64f1ee1e80e9e335) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) identifier) |
|  | Set the identifier of the battery. |
| void | [bt\_bas\_bls\_set\_service\_required](group__bt__bas.md#gaa94f308b6e135a3957191499778275ec) (enum [bt\_bas\_bls\_service\_required](group__bt__bas.md#gad410bdd972f09f0314b696ce31e6d82d) value) |
|  | Set the service required status. |
| void | [bt\_bas\_bls\_set\_battery\_fault](group__bt__bas.md#ga9c50ed6a493adee208a59b17c48702f8) (enum [bt\_bas\_bls\_battery\_fault](group__bt__bas.md#ga6976a11ffe2c9a9b2fff82763be2edee) value) |
|  | Set the battery fault status. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [services](dir_e4028deab123aca136adb6f86dc413ad.md)
- [bas.h](bas_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
