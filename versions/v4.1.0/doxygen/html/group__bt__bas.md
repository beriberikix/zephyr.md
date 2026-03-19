---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__bas.html
original_path: doxygen/html/group__bt__bas.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Battery Service (BAS)

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md)

Battery Service (BAS).
[More...](#details)

| Enumerations | |
| --- | --- |
| enum | [bt\_bas\_bcs\_flags](#ga56d26a8cde072959e8d8b75ee4fb2819) { [BT\_BAS\_BCS\_BATTERY\_CRITICAL\_STATE](#gga56d26a8cde072959e8d8b75ee4fb2819ad45c2b537f66cc7118357616120fa8a5) = BIT(0) , [BT\_BAS\_BCS\_IMMEDIATE\_SERVICE\_REQUIRED](#gga56d26a8cde072959e8d8b75ee4fb2819af82ae1d0e53efa882ff21d4e67b9ba7a) = BIT(1) } |
|  | Battery Critical Status Characteristic flags. [More...](#ga56d26a8cde072959e8d8b75ee4fb2819) |
| enum | [bt\_bas\_bls\_flags](#ga7c425f7fd9e908e327810f89d7645745) { [BT\_BAS\_BLS\_FLAG\_IDENTIFIER\_PRESENT](#gga7c425f7fd9e908e327810f89d7645745a69d60021c1d1772f461f0e90eadd9b46) = BIT(0) , [BT\_BAS\_BLS\_FLAG\_BATTERY\_LEVEL\_PRESENT](#gga7c425f7fd9e908e327810f89d7645745a74cb90028ebf42119c8c69a3801591ba) = BIT(1) , [BT\_BAS\_BLS\_FLAG\_ADDITIONAL\_STATUS\_PRESENT](#gga7c425f7fd9e908e327810f89d7645745add93cefc8c583aa0edd71ed66edbea3d) = BIT(2) } |
|  | Battery Level Status Characteristic flags. [More...](#ga7c425f7fd9e908e327810f89d7645745) |
| enum | [bt\_bas\_bls\_battery\_present](#ga31d5d4a7184243ffe9d925714de4367f) { [BT\_BAS\_BLS\_BATTERY\_NOT\_PRESENT](#gga31d5d4a7184243ffe9d925714de4367fae373a1d0f3875bafbdcab7c1cca0f522) = 0 , [BT\_BAS\_BLS\_BATTERY\_PRESENT](#gga31d5d4a7184243ffe9d925714de4367fa63b460de845ef9cb7423c82008b2ed49) = 1 } |
|  | Battery Present Status. [More...](#ga31d5d4a7184243ffe9d925714de4367f) |
| enum | [bt\_bas\_bls\_wired\_power\_source](#ga4e3f58a5f7c8715f3f8f24b96229b71c) { [BT\_BAS\_BLS\_WIRED\_POWER\_NOT\_CONNECTED](#gga4e3f58a5f7c8715f3f8f24b96229b71ca98d72b37dce3b29dcc901bb58d3e6acf) = 0 , [BT\_BAS\_BLS\_WIRED\_POWER\_CONNECTED](#gga4e3f58a5f7c8715f3f8f24b96229b71cadabb6df4477b9483e18cd3bd77ef8adc) = 1 , [BT\_BAS\_BLS\_WIRED\_POWER\_UNKNOWN](#gga4e3f58a5f7c8715f3f8f24b96229b71ca2064d10fa9b52c40142eb4f8a9ef2799) = 2 } |
|  | Wired External Power Source Status. [More...](#ga4e3f58a5f7c8715f3f8f24b96229b71c) |
| enum | [bt\_bas\_bls\_wireless\_power\_source](#gaf76a1eea78e9ff5c35977c41b00fb64d) { [BT\_BAS\_BLS\_WIRELESS\_POWER\_NOT\_CONNECTED](#ggaf76a1eea78e9ff5c35977c41b00fb64dab90caed6b5b1fef37f79176ae6221383) = 0 , [BT\_BAS\_BLS\_WIRELESS\_POWER\_CONNECTED](#ggaf76a1eea78e9ff5c35977c41b00fb64da3f2f11b307bb6e641792e4e85fe3a363) = 1 , [BT\_BAS\_BLS\_WIRELESS\_POWER\_UNKNOWN](#ggaf76a1eea78e9ff5c35977c41b00fb64daafeab5f57d1a12770bc9ac95161e1af8) = 2 } |
|  | Wireless External Power Source Status. [More...](#gaf76a1eea78e9ff5c35977c41b00fb64d) |
| enum | [bt\_bas\_bls\_battery\_charge\_state](#ga3584a3e7b7194bf244f414d6860b1313) { [BT\_BAS\_BLS\_CHARGE\_STATE\_UNKNOWN](#gga3584a3e7b7194bf244f414d6860b1313a663b3a9a4490600c56f2784246bbe58c) = 0 , [BT\_BAS\_BLS\_CHARGE\_STATE\_CHARGING](#gga3584a3e7b7194bf244f414d6860b1313a35249a218c5c15a24e9b529991282ab9) = 1 , [BT\_BAS\_BLS\_CHARGE\_STATE\_DISCHARGING\_ACTIVE](#gga3584a3e7b7194bf244f414d6860b1313aba3c8d0d791dae18b6aa3149619e4e02) = 2 , [BT\_BAS\_BLS\_CHARGE\_STATE\_DISCHARGING\_INACTIVE](#gga3584a3e7b7194bf244f414d6860b1313a23a496ecd4b7e7d33ee7a2f0021c4f1a) = 3 } |
|  | Battery Charge State. [More...](#ga3584a3e7b7194bf244f414d6860b1313) |
| enum | [bt\_bas\_bls\_battery\_charge\_level](#gad374826ce9465bbf344b1f25b16c574c) { [BT\_BAS\_BLS\_CHARGE\_LEVEL\_UNKNOWN](#ggad374826ce9465bbf344b1f25b16c574cabdd600d10005a09cbce4f5584cb3bb58) = 0 , [BT\_BAS\_BLS\_CHARGE\_LEVEL\_GOOD](#ggad374826ce9465bbf344b1f25b16c574cae08b7620b5babb731a6c8e8bf12b1387) = 1 , [BT\_BAS\_BLS\_CHARGE\_LEVEL\_LOW](#ggad374826ce9465bbf344b1f25b16c574ca27d8f485ee4ee50bb8d9c02049b9679e) = 2 , [BT\_BAS\_BLS\_CHARGE\_LEVEL\_CRITICAL](#ggad374826ce9465bbf344b1f25b16c574ca46fa5393ea4acefae2d2ffdfaef2a31d) = 3 } |
|  | Battery Charge Level. [More...](#gad374826ce9465bbf344b1f25b16c574c) |
| enum | [bt\_bas\_bls\_battery\_charge\_type](#ga9f09b045f9db8aa2f2e21adb0a65c3aa) {     [BT\_BAS\_BLS\_CHARGE\_TYPE\_UNKNOWN](#gga9f09b045f9db8aa2f2e21adb0a65c3aaa0c681a700639a1ba8b3cf3e5afc70e64) = 0 , [BT\_BAS\_BLS\_CHARGE\_TYPE\_CONSTANT\_CURRENT](#gga9f09b045f9db8aa2f2e21adb0a65c3aaa5a9f93290d6b11596771e7e9bbc357af) = 1 , [BT\_BAS\_BLS\_CHARGE\_TYPE\_CONSTANT\_VOLTAGE](#gga9f09b045f9db8aa2f2e21adb0a65c3aaa5dc3c38414be857fd5d2cf98a0edc730) = 2 , [BT\_BAS\_BLS\_CHARGE\_TYPE\_TRICKLE](#gga9f09b045f9db8aa2f2e21adb0a65c3aaade1f3bc7dab9c768feb8d70c149ffbda) = 3 ,     [BT\_BAS\_BLS\_CHARGE\_TYPE\_FLOAT](#gga9f09b045f9db8aa2f2e21adb0a65c3aaabbf719d116ec24bbf327c8e7a2eb50c0) = 4   } |
|  | Battery Charge Type. [More...](#ga9f09b045f9db8aa2f2e21adb0a65c3aa) |
| enum | [bt\_bas\_bls\_charging\_fault\_reason](#gad981cab4d2a285ee72481b54836cf35b) { [BT\_BAS\_BLS\_FAULT\_REASON\_NONE](#ggad981cab4d2a285ee72481b54836cf35bab8d7bcea2ab1d76a66727e11a520654a) = 0 , [BT\_BAS\_BLS\_FAULT\_REASON\_BATTERY](#ggad981cab4d2a285ee72481b54836cf35ba7bea7165cbba98284b9941cf8809787f) = BIT(0) , [BT\_BAS\_BLS\_FAULT\_REASON\_EXTERNAL\_POWER](#ggad981cab4d2a285ee72481b54836cf35ba527c9490662f70b789ecb0d37f90df3b) = BIT(1) , [BT\_BAS\_BLS\_FAULT\_REASON\_OTHER](#ggad981cab4d2a285ee72481b54836cf35ba8c70a47828ed3b90c08e742dff3c0ab7) = BIT(2) } |
|  | Charging Fault Reason. [More...](#gad981cab4d2a285ee72481b54836cf35b) |
| enum | [bt\_bas\_bls\_service\_required](#gad410bdd972f09f0314b696ce31e6d82d) { [BT\_BAS\_BLS\_SERVICE\_REQUIRED\_FALSE](#ggad410bdd972f09f0314b696ce31e6d82daa50e305c82d8081877576953e07241db) = 0 , [BT\_BAS\_BLS\_SERVICE\_REQUIRED\_TRUE](#ggad410bdd972f09f0314b696ce31e6d82da683bc2d562e99ae0c691eb3611206f00) = 1 , [BT\_BAS\_BLS\_SERVICE\_REQUIRED\_UNKNOWN](#ggad410bdd972f09f0314b696ce31e6d82dae36621eac964d7f2b8b5959de11ba870) = 2 } |
|  | Service Required Status. [More...](#gad410bdd972f09f0314b696ce31e6d82d) |
| enum | [bt\_bas\_bls\_battery\_fault](#ga6976a11ffe2c9a9b2fff82763be2edee) { [BT\_BAS\_BLS\_BATTERY\_FAULT\_NO](#gga6976a11ffe2c9a9b2fff82763be2edeeab119e2a0a3600269f752dfc7f271edee) = 0 , [BT\_BAS\_BLS\_BATTERY\_FAULT\_YES](#gga6976a11ffe2c9a9b2fff82763be2edeea6af59b287c252dbb04d6ab6cdbbf6d6f) = 1 } |
|  | Battery Fault Status. [More...](#ga6976a11ffe2c9a9b2fff82763be2edee) |

| Functions | |
| --- | --- |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_bas\_get\_battery\_level](#gadbe0f52d04d90372d603af66b693e980) (void) |
|  | Read battery level value. |
| int | [bt\_bas\_set\_battery\_level](#gac8d519830c34b9c8370366e2593dbeba) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) level) |
|  | Update battery level value. |
| void | [bt\_bas\_bls\_set\_battery\_present](#ga5e0325af9dcd362dd3c1691832be5677) (enum [bt\_bas\_bls\_battery\_present](#ga31d5d4a7184243ffe9d925714de4367f) present) |
|  | Set the battery present status. |
| void | [bt\_bas\_bls\_set\_wired\_external\_power\_source](#ga7bf36a53494e2ecfbb5ccd218f29f51f) (enum [bt\_bas\_bls\_wired\_power\_source](#ga4e3f58a5f7c8715f3f8f24b96229b71c) source) |
|  | Set the wired external power source status. |
| void | [bt\_bas\_bls\_set\_wireless\_external\_power\_source](#gae1cbafd30e1d78437c78d44df25aa005) (enum [bt\_bas\_bls\_wireless\_power\_source](#gaf76a1eea78e9ff5c35977c41b00fb64d) source) |
|  | Set the wireless external power source status. |
| void | [bt\_bas\_bls\_set\_battery\_charge\_state](#ga60b153c4d291ed4b16ce1f9d2dc1b45d) (enum [bt\_bas\_bls\_battery\_charge\_state](#ga3584a3e7b7194bf244f414d6860b1313) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Set the battery charge state. |
| void | [bt\_bas\_bls\_set\_battery\_charge\_level](#gac8e32530f966c7699d3c28e6685bcee5) (enum [bt\_bas\_bls\_battery\_charge\_level](#gad374826ce9465bbf344b1f25b16c574c) level) |
|  | Set the battery charge level. |
| void | [bt\_bas\_bls\_set\_battery\_charge\_type](#ga3cea34f717f2df01b6f49bed80f27f44) (enum [bt\_bas\_bls\_battery\_charge\_type](#ga9f09b045f9db8aa2f2e21adb0a65c3aa) type) |
|  | Set the battery charge type. |
| void | [bt\_bas\_bls\_set\_charging\_fault\_reason](#ga7996edb35bcca878062360b24036b6f8) (enum [bt\_bas\_bls\_charging\_fault\_reason](#gad981cab4d2a285ee72481b54836cf35b) reason) |
|  | Set the charging fault reason. |
| void | [bt\_bas\_bls\_set\_identifier](#gafd74ef933734960a64f1ee1e80e9e335) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) identifier) |
|  | Set the identifier of the battery. |
| void | [bt\_bas\_bls\_set\_service\_required](#gaa94f308b6e135a3957191499778275ec) (enum [bt\_bas\_bls\_service\_required](#gad410bdd972f09f0314b696ce31e6d82d) value) |
|  | Set the service required status. |
| void | [bt\_bas\_bls\_set\_battery\_fault](#ga9c50ed6a493adee208a59b17c48702f8) (enum [bt\_bas\_bls\_battery\_fault](#ga6976a11ffe2c9a9b2fff82763be2edee) value) |
|  | Set the battery fault status. |

## Detailed Description

Battery Service (BAS).

[Experimental] Users should note that the APIs can change as a part of ongoing development.

## Enumeration Type Documentation

## [◆ ](#ga56d26a8cde072959e8d8b75ee4fb2819)bt\_bas\_bcs\_flags

| enum [bt\_bas\_bcs\_flags](#ga56d26a8cde072959e8d8b75ee4fb2819) |
| --- |

`#include <[bas.h](bas_8h.md)>`

Battery Critical Status Characteristic flags.

Enumeration for the flags indicating the presence of various fields in the Battery Critical Status characteristic.

| Enumerator | |
| --- | --- |
| BT\_BAS\_BCS\_BATTERY\_CRITICAL\_STATE | Battery Critical Status Bit 0: Critical Power State. |
| BT\_BAS\_BCS\_IMMEDIATE\_SERVICE\_REQUIRED | Battery Critical Status Bit 1: Immediate Service Required. |

## [◆ ](#gad374826ce9465bbf344b1f25b16c574c)bt\_bas\_bls\_battery\_charge\_level

| enum [bt\_bas\_bls\_battery\_charge\_level](#gad374826ce9465bbf344b1f25b16c574c) |
| --- |

`#include <[bas.h](bas_8h.md)>`

Battery Charge Level.

Enumeration for the level of charge in the battery.

| Enumerator | |
| --- | --- |
| BT\_BAS\_BLS\_CHARGE\_LEVEL\_UNKNOWN | Battery charge level is unknown. |
| BT\_BAS\_BLS\_CHARGE\_LEVEL\_GOOD | Battery charge level is good. |
| BT\_BAS\_BLS\_CHARGE\_LEVEL\_LOW | Battery charge level is low. |
| BT\_BAS\_BLS\_CHARGE\_LEVEL\_CRITICAL | Battery charge level is critical. |

## [◆ ](#ga3584a3e7b7194bf244f414d6860b1313)bt\_bas\_bls\_battery\_charge\_state

| enum [bt\_bas\_bls\_battery\_charge\_state](#ga3584a3e7b7194bf244f414d6860b1313) |
| --- |

`#include <[bas.h](bas_8h.md)>`

Battery Charge State.

Enumeration for the charge state of the battery.

| Enumerator | |
| --- | --- |
| BT\_BAS\_BLS\_CHARGE\_STATE\_UNKNOWN | Battery charge state is unknown. |
| BT\_BAS\_BLS\_CHARGE\_STATE\_CHARGING | Battery is currently charging. |
| BT\_BAS\_BLS\_CHARGE\_STATE\_DISCHARGING\_ACTIVE | Battery is discharging actively. |
| BT\_BAS\_BLS\_CHARGE\_STATE\_DISCHARGING\_INACTIVE | Battery is discharging but inactive. |

## [◆ ](#ga9f09b045f9db8aa2f2e21adb0a65c3aa)bt\_bas\_bls\_battery\_charge\_type

| enum [bt\_bas\_bls\_battery\_charge\_type](#ga9f09b045f9db8aa2f2e21adb0a65c3aa) |
| --- |

`#include <[bas.h](bas_8h.md)>`

Battery Charge Type.

Enumeration for the type of charging applied to the battery.

| Enumerator | |
| --- | --- |
| BT\_BAS\_BLS\_CHARGE\_TYPE\_UNKNOWN | Battery charge type is unknown or not charging. |
| BT\_BAS\_BLS\_CHARGE\_TYPE\_CONSTANT\_CURRENT | Battery is charged using constant current. |
| BT\_BAS\_BLS\_CHARGE\_TYPE\_CONSTANT\_VOLTAGE | Battery is charged using constant voltage. |
| BT\_BAS\_BLS\_CHARGE\_TYPE\_TRICKLE | Battery is charged using trickle charge. |
| BT\_BAS\_BLS\_CHARGE\_TYPE\_FLOAT | Battery is charged using float charge. |

## [◆ ](#ga6976a11ffe2c9a9b2fff82763be2edee)bt\_bas\_bls\_battery\_fault

| enum [bt\_bas\_bls\_battery\_fault](#ga6976a11ffe2c9a9b2fff82763be2edee) |
| --- |

`#include <[bas.h](bas_8h.md)>`

Battery Fault Status.

Enumeration for the fault status of the battery.

| Enumerator | |
| --- | --- |
| BT\_BAS\_BLS\_BATTERY\_FAULT\_NO | No battery fault. |
| BT\_BAS\_BLS\_BATTERY\_FAULT\_YES | Battery fault present. |

## [◆ ](#ga31d5d4a7184243ffe9d925714de4367f)bt\_bas\_bls\_battery\_present

| enum [bt\_bas\_bls\_battery\_present](#ga31d5d4a7184243ffe9d925714de4367f) |
| --- |

`#include <[bas.h](bas_8h.md)>`

Battery Present Status.

Enumeration for the presence of the battery.

| Enumerator | |
| --- | --- |
| BT\_BAS\_BLS\_BATTERY\_NOT\_PRESENT | Battery is not present. |
| BT\_BAS\_BLS\_BATTERY\_PRESENT | Battery is present. |

## [◆ ](#gad981cab4d2a285ee72481b54836cf35b)bt\_bas\_bls\_charging\_fault\_reason

| enum [bt\_bas\_bls\_charging\_fault\_reason](#gad981cab4d2a285ee72481b54836cf35b) |
| --- |

`#include <[bas.h](bas_8h.md)>`

Charging Fault Reason.

Enumeration for the reasons of charging faults.

| Enumerator | |
| --- | --- |
| BT\_BAS\_BLS\_FAULT\_REASON\_NONE | No charging fault. |
| BT\_BAS\_BLS\_FAULT\_REASON\_BATTERY | Charging fault due to battery issue. |
| BT\_BAS\_BLS\_FAULT\_REASON\_EXTERNAL\_POWER | Charging fault due to external power source issue. |
| BT\_BAS\_BLS\_FAULT\_REASON\_OTHER | Charging fault for other reasons. |

## [◆ ](#ga7c425f7fd9e908e327810f89d7645745)bt\_bas\_bls\_flags

| enum [bt\_bas\_bls\_flags](#ga7c425f7fd9e908e327810f89d7645745) |
| --- |

`#include <[bas.h](bas_8h.md)>`

Battery Level Status Characteristic flags.

Enumeration for the flags indicating the presence of various fields in the Battery Level Status characteristic.

| Enumerator | |
| --- | --- |
| BT\_BAS\_BLS\_FLAG\_IDENTIFIER\_PRESENT | Bit indicating that the Battery Level Status identifier is present. |
| BT\_BAS\_BLS\_FLAG\_BATTERY\_LEVEL\_PRESENT | Bit indicating that the Battery Level is present. |
| BT\_BAS\_BLS\_FLAG\_ADDITIONAL\_STATUS\_PRESENT | Bit indicating that additional status information is present. |

## [◆ ](#gad410bdd972f09f0314b696ce31e6d82d)bt\_bas\_bls\_service\_required

| enum [bt\_bas\_bls\_service\_required](#gad410bdd972f09f0314b696ce31e6d82d) |
| --- |

`#include <[bas.h](bas_8h.md)>`

Service Required Status.

Enumeration for whether the service is required.

| Enumerator | |
| --- | --- |
| BT\_BAS\_BLS\_SERVICE\_REQUIRED\_FALSE | Service is not required. |
| BT\_BAS\_BLS\_SERVICE\_REQUIRED\_TRUE | Service is required. |
| BT\_BAS\_BLS\_SERVICE\_REQUIRED\_UNKNOWN | Service requirement is unknown. |

## [◆ ](#ga4e3f58a5f7c8715f3f8f24b96229b71c)bt\_bas\_bls\_wired\_power\_source

| enum [bt\_bas\_bls\_wired\_power\_source](#ga4e3f58a5f7c8715f3f8f24b96229b71c) |
| --- |

`#include <[bas.h](bas_8h.md)>`

Wired External Power Source Status.

Enumeration for the status of the wired external power source.

| Enumerator | |
| --- | --- |
| BT\_BAS\_BLS\_WIRED\_POWER\_NOT\_CONNECTED | Wired external power source is not connected. |
| BT\_BAS\_BLS\_WIRED\_POWER\_CONNECTED | Wired external power source is connected. |
| BT\_BAS\_BLS\_WIRED\_POWER\_UNKNOWN | Wired external power source status is unknown. |

## [◆ ](#gaf76a1eea78e9ff5c35977c41b00fb64d)bt\_bas\_bls\_wireless\_power\_source

| enum [bt\_bas\_bls\_wireless\_power\_source](#gaf76a1eea78e9ff5c35977c41b00fb64d) |
| --- |

`#include <[bas.h](bas_8h.md)>`

Wireless External Power Source Status.

Enumeration for the status of the wireless external power source.

| Enumerator | |
| --- | --- |
| BT\_BAS\_BLS\_WIRELESS\_POWER\_NOT\_CONNECTED | Wireless external power source is not connected. |
| BT\_BAS\_BLS\_WIRELESS\_POWER\_CONNECTED | Wireless external power source is connected. |
| BT\_BAS\_BLS\_WIRELESS\_POWER\_UNKNOWN | Wireless external power source status is unknown. |

## Function Documentation

## [◆ ](#gac8e32530f966c7699d3c28e6685bcee5)bt\_bas\_bls\_set\_battery\_charge\_level()

| void bt\_bas\_bls\_set\_battery\_charge\_level | ( | enum [bt\_bas\_bls\_battery\_charge\_level](#gad374826ce9465bbf344b1f25b16c574c) | *level* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bas.h](bas_8h.md)>`

Set the battery charge level.

Parameters
:   | level | The battery charge level to set. |
    | --- | --- |

## [◆ ](#ga60b153c4d291ed4b16ce1f9d2dc1b45d)bt\_bas\_bls\_set\_battery\_charge\_state()

| void bt\_bas\_bls\_set\_battery\_charge\_state | ( | enum [bt\_bas\_bls\_battery\_charge\_state](#ga3584a3e7b7194bf244f414d6860b1313) | *state* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bas.h](bas_8h.md)>`

Set the battery charge state.

Parameters
:   | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | The battery charge state to set. |
    | --- | --- |

## [◆ ](#ga3cea34f717f2df01b6f49bed80f27f44)bt\_bas\_bls\_set\_battery\_charge\_type()

| void bt\_bas\_bls\_set\_battery\_charge\_type | ( | enum [bt\_bas\_bls\_battery\_charge\_type](#ga9f09b045f9db8aa2f2e21adb0a65c3aa) | *type* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bas.h](bas_8h.md)>`

Set the battery charge type.

Parameters
:   | type | The battery charge type to set. |
    | --- | --- |

## [◆ ](#ga9c50ed6a493adee208a59b17c48702f8)bt\_bas\_bls\_set\_battery\_fault()

| void bt\_bas\_bls\_set\_battery\_fault | ( | enum [bt\_bas\_bls\_battery\_fault](#ga6976a11ffe2c9a9b2fff82763be2edee) | *value* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bas.h](bas_8h.md)>`

Set the battery fault status.

Attention
:   Available only when the following Kconfig option is enabled: `CONFIG_BT_BAS_BLS_ADDITIONAL_STATUS_PRESENT`.

Parameters
:   | value | Battery fault status to set. |
    | --- | --- |

## [◆ ](#ga5e0325af9dcd362dd3c1691832be5677)bt\_bas\_bls\_set\_battery\_present()

| void bt\_bas\_bls\_set\_battery\_present | ( | enum [bt\_bas\_bls\_battery\_present](#ga31d5d4a7184243ffe9d925714de4367f) | *present* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bas.h](bas_8h.md)>`

Set the battery present status.

Parameters
:   | present | The battery present status to set. |
    | --- | --- |

## [◆ ](#ga7996edb35bcca878062360b24036b6f8)bt\_bas\_bls\_set\_charging\_fault\_reason()

| void bt\_bas\_bls\_set\_charging\_fault\_reason | ( | enum [bt\_bas\_bls\_charging\_fault\_reason](#gad981cab4d2a285ee72481b54836cf35b) | *reason* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bas.h](bas_8h.md)>`

Set the charging fault reason.

Parameters
:   | reason | The charging fault reason to set. |
    | --- | --- |

## [◆ ](#gafd74ef933734960a64f1ee1e80e9e335)bt\_bas\_bls\_set\_identifier()

| void bt\_bas\_bls\_set\_identifier | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *identifier* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bas.h](bas_8h.md)>`

Set the identifier of the battery.

Attention
:   Available only when the following Kconfig option is enabled: `CONFIG_BT_BAS_BLS_IDENTIFIER_PRESENT`.

Parameters
:   | identifier | Identifier to set. |
    | --- | --- |

## [◆ ](#gaa94f308b6e135a3957191499778275ec)bt\_bas\_bls\_set\_service\_required()

| void bt\_bas\_bls\_set\_service\_required | ( | enum [bt\_bas\_bls\_service\_required](#gad410bdd972f09f0314b696ce31e6d82d) | *value* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bas.h](bas_8h.md)>`

Set the service required status.

Attention
:   Available only when the following Kconfig option is enabled: `CONFIG_BT_BAS_BLS_ADDITIONAL_STATUS_PRESENT`.

Parameters
:   | value | Service required status to set. |
    | --- | --- |

## [◆ ](#ga7bf36a53494e2ecfbb5ccd218f29f51f)bt\_bas\_bls\_set\_wired\_external\_power\_source()

| void bt\_bas\_bls\_set\_wired\_external\_power\_source | ( | enum [bt\_bas\_bls\_wired\_power\_source](#ga4e3f58a5f7c8715f3f8f24b96229b71c) | *source* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bas.h](bas_8h.md)>`

Set the wired external power source status.

Parameters
:   | source | The wired external power source status to set. |
    | --- | --- |

## [◆ ](#gae1cbafd30e1d78437c78d44df25aa005)bt\_bas\_bls\_set\_wireless\_external\_power\_source()

| void bt\_bas\_bls\_set\_wireless\_external\_power\_source | ( | enum [bt\_bas\_bls\_wireless\_power\_source](#gaf76a1eea78e9ff5c35977c41b00fb64d) | *source* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bas.h](bas_8h.md)>`

Set the wireless external power source status.

Parameters
:   | source | The wireless external power source status to set. |
    | --- | --- |

## [◆ ](#gadbe0f52d04d90372d603af66b693e980)bt\_bas\_get\_battery\_level()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_bas\_get\_battery\_level | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bas.h](bas_8h.md)>`

Read battery level value.

Read the characteristic value of the battery level

Returns
:   The battery level in percent.

## [◆ ](#gac8d519830c34b9c8370366e2593dbeba)bt\_bas\_set\_battery\_level()

| int bt\_bas\_set\_battery\_level | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *level* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[bas.h](bas_8h.md)>`

Update battery level value.

Update the characteristic value of the battery level This will send a GATT notification to all current subscribers.

Parameters
:   | level | The battery level in percent. |
    | --- | --- |

Returns
:   Zero in case of success and error code in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
