---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__bt__mesh__prov.html
original_path: doxygen/html/group__bt__mesh__prov.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Provisioning

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md)

Provisioning.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_dev\_capabilities](structbt__mesh__dev__capabilities.md) |
|  | Device Capabilities. [More...](structbt__mesh__dev__capabilities.md#details) |
| struct | [bt\_mesh\_prov](structbt__mesh__prov.md) |
|  | Provisioning properties & capabilities. [More...](structbt__mesh__prov.md#details) |

| Enumerations | |
| --- | --- |
| enum | { [BT\_MESH\_PROV\_AUTH\_CMAC\_AES128\_AES\_CCM](#ggabe5586cff0697e137730a52728978681affa8679d8be1a12714a34ed09c3b05dd) , [BT\_MESH\_PROV\_AUTH\_HMAC\_SHA256\_AES\_CCM](#ggabe5586cff0697e137730a52728978681a292bf2e4d29f0bd0d746bbb871f2ee5a) } |
|  | Available authentication algorithms. [More...](#gabe5586cff0697e137730a52728978681) |
| enum | { [BT\_MESH\_STATIC\_OOB\_AVAILABLE](#ggabec90bd95082b9dc8fa3ca27a9d7bc66a30e46fe23e508029b570e1f107b38d40) = BIT(0) , [BT\_MESH\_OOB\_AUTH\_REQUIRED](#ggabec90bd95082b9dc8fa3ca27a9d7bc66a61f859a15fabc8d9fd278dabe5a86a37) = BIT(1) } |
|  | OOB Type field values. [More...](#gabec90bd95082b9dc8fa3ca27a9d7bc66) |
| enum | [bt\_mesh\_output\_action\_t](#ga5512b81ef7eeb45b0a12ef62234c8795) {     [BT\_MESH\_NO\_OUTPUT](#gga5512b81ef7eeb45b0a12ef62234c8795ad009060fd1f501c8362a63e6c020b113) = 0 , [BT\_MESH\_BLINK](#gga5512b81ef7eeb45b0a12ef62234c8795ac38333011b4f76b036a04e41f1f71e83) = BIT(0) , [BT\_MESH\_BEEP](#gga5512b81ef7eeb45b0a12ef62234c8795ae50031a39d19181df17ee6de1a12272c) = BIT(1) , [BT\_MESH\_VIBRATE](#gga5512b81ef7eeb45b0a12ef62234c8795ab45021af96db0465f5edc6e0ea7b6079) = BIT(2) ,     [BT\_MESH\_DISPLAY\_NUMBER](#gga5512b81ef7eeb45b0a12ef62234c8795a3586ffa3e36247e0d90b83c3f075e591) = BIT(3) , [BT\_MESH\_DISPLAY\_STRING](#gga5512b81ef7eeb45b0a12ef62234c8795aa07d600f2afe278729bb4e35d41bf29b) = BIT(4)   } |
|  | Available Provisioning output authentication actions. [More...](#ga5512b81ef7eeb45b0a12ef62234c8795) |
| enum | [bt\_mesh\_input\_action\_t](#gaf71f3dbdef6b8c085e9a4f068e1f60c5) {     [BT\_MESH\_NO\_INPUT](#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ac721b070cad51f1cd9aa1f0b60e59056) = 0 , [BT\_MESH\_PUSH](#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ae4902ce51142fa49d2d5e97165d6f51c) = BIT(0) , [BT\_MESH\_TWIST](#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ad6f22211d09614181cb5b0f42300a9ee) = BIT(1) , [BT\_MESH\_ENTER\_NUMBER](#ggaf71f3dbdef6b8c085e9a4f068e1f60c5aa0de3817e863d1f06888100de24fb4b0) = BIT(2) ,     [BT\_MESH\_ENTER\_STRING](#ggaf71f3dbdef6b8c085e9a4f068e1f60c5a5d6bd8e6110c8f53245840aead4201c2) = BIT(3)   } |
|  | Available Provisioning input authentication actions. [More...](#gaf71f3dbdef6b8c085e9a4f068e1f60c5) |
| enum | [bt\_mesh\_prov\_bearer\_t](#gaa157eb0fee30c28092a11993872b8fdd) { [BT\_MESH\_PROV\_ADV](#ggaa157eb0fee30c28092a11993872b8fdda5142f018a5426a047688c6507b3af4f8) = BIT(0) , [BT\_MESH\_PROV\_GATT](#ggaa157eb0fee30c28092a11993872b8fdda27c9c1278acc887214a4a30294bf52d8) = BIT(1) , [BT\_MESH\_PROV\_REMOTE](#ggaa157eb0fee30c28092a11993872b8fdda4222d03b09ba43b6ea772738b8987501) = BIT(2) } |
|  | Available Provisioning bearers. [More...](#gaa157eb0fee30c28092a11993872b8fdd) |
| enum | [bt\_mesh\_prov\_oob\_info\_t](#gaf93f7b49dada5c3f7accc54663648e48) {     [BT\_MESH\_PROV\_OOB\_OTHER](#ggaf93f7b49dada5c3f7accc54663648e48a487ffb56c8c15a37b69fa1699fff301a) = BIT(0) , [BT\_MESH\_PROV\_OOB\_URI](#ggaf93f7b49dada5c3f7accc54663648e48ad861e8de3c1fbc1658a6d0fba38785dd) = BIT(1) , [BT\_MESH\_PROV\_OOB\_2D\_CODE](#ggaf93f7b49dada5c3f7accc54663648e48a34d005022a75446a386006f7690a473e) = BIT(2) , [BT\_MESH\_PROV\_OOB\_BAR\_CODE](#ggaf93f7b49dada5c3f7accc54663648e48abe8fd10b49a7bb6c7499eb73ae3876d3) = BIT(3) ,     [BT\_MESH\_PROV\_OOB\_NFC](#ggaf93f7b49dada5c3f7accc54663648e48ad9b4089a740d47950c02b4389d29df56) = BIT(4) , [BT\_MESH\_PROV\_OOB\_NUMBER](#ggaf93f7b49dada5c3f7accc54663648e48ac5d40459453afebc841f32e1f0b33fbc) = BIT(5) , [BT\_MESH\_PROV\_OOB\_STRING](#ggaf93f7b49dada5c3f7accc54663648e48a8553379d579a418a6453669323b18088) = BIT(6) , [BT\_MESH\_PROV\_OOB\_CERTIFICATE](#ggaf93f7b49dada5c3f7accc54663648e48a00eb3ba6b7940b02d2fe3892100f497e) = BIT(7) ,     [BT\_MESH\_PROV\_OOB\_RECORDS](#ggaf93f7b49dada5c3f7accc54663648e48aa10724108397ab8d48a3aac2817992f2) = BIT(8) , [BT\_MESH\_PROV\_OOB\_ON\_BOX](#ggaf93f7b49dada5c3f7accc54663648e48adbbc3c3829bb7caf1a4a5fd2066f3b4a) = BIT(11) , [BT\_MESH\_PROV\_OOB\_IN\_BOX](#ggaf93f7b49dada5c3f7accc54663648e48ae855a27a18bfb6ea03f0ff6165e4a291) = BIT(12) , [BT\_MESH\_PROV\_OOB\_ON\_PAPER](#ggaf93f7b49dada5c3f7accc54663648e48a137946e3d53b996b77bebeda5fa930cb) = BIT(13) ,     [BT\_MESH\_PROV\_OOB\_IN\_MANUAL](#ggaf93f7b49dada5c3f7accc54663648e48a4a8a7e4ab87cf360abdb167076349072) = BIT(14) , [BT\_MESH\_PROV\_OOB\_ON\_DEV](#ggaf93f7b49dada5c3f7accc54663648e48aa73dd9517eec86e51b48d256fc9660da) = BIT(15)   } |
|  | Out of Band information location. [More...](#gaf93f7b49dada5c3f7accc54663648e48) |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_input\_string](#ga2592abf429b40ef9242bce26f5bd085e) (const char \*str) |
|  | Provide provisioning input OOB string. |
| int | [bt\_mesh\_input\_number](#gace8cbf2a6e9144d3118054f234de02ef) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num) |
|  | Provide provisioning input OOB number. |
| int | [bt\_mesh\_prov\_remote\_pub\_key\_set](#gae33b5b6e9650b49d46494b4a81b18674) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) public\_key[64]) |
|  | Provide Device public key. |
| int | [bt\_mesh\_auth\_method\_set\_input](#ga80be35bf7287e62cb47d8fba99d648a9) ([bt\_mesh\_input\_action\_t](#gaf71f3dbdef6b8c085e9a4f068e1f60c5) action, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size) |
|  | Use Input OOB authentication. |
| int | [bt\_mesh\_auth\_method\_set\_output](#gad66ccc725a1cfdf2b79076f22f853f84) ([bt\_mesh\_output\_action\_t](#ga5512b81ef7eeb45b0a12ef62234c8795) action, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size) |
|  | Use Output OOB authentication. |
| int | [bt\_mesh\_auth\_method\_set\_static](#ga7b6024dc32f6ec7f26cbf91545911084) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*static\_val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size) |
|  | Use static OOB authentication. |
| int | [bt\_mesh\_auth\_method\_set\_none](#gabab41ebdcae2eaa109e03cb2d8fa78c6) (void) |
|  | Don't use OOB authentication. |
| int | [bt\_mesh\_prov\_enable](#ga6c8dc1b09d4cde8738be83c992b860a9) ([bt\_mesh\_prov\_bearer\_t](#gaa157eb0fee30c28092a11993872b8fdd) bearers) |
|  | Enable specific provisioning bearers. |
| int | [bt\_mesh\_prov\_disable](#gac7e084e7d12a93377d49b1c3d6313399) ([bt\_mesh\_prov\_bearer\_t](#gaa157eb0fee30c28092a11993872b8fdd) bearers) |
|  | Disable specific provisioning bearers. |
| int | [bt\_mesh\_provision](#ga4ed6e078c1c0f197758c8dbb23db30f6) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_key[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) iv\_index, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dev\_key[16]) |
|  | Provision the local Mesh Node. |
| int | [bt\_mesh\_provision\_adv](#ga0bfae4ebda53052cfa027c3a7ae51ec8) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uuid[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attention\_duration) |
|  | Provision a Mesh Node using PB-ADV. |
| int | [bt\_mesh\_provision\_gatt](#ga60666e0d7629caf36026974621bae664) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uuid[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attention\_duration) |
|  | Provision a Mesh Node using PB-GATT. |
| int | [bt\_mesh\_provision\_remote](#ga9fc414e4e15d6b3ab0dae5483ed62982) (struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uuid[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
|  | Provision a Mesh Node using PB-Remote. |
| int | [bt\_mesh\_reprovision\_remote](#gaa02583390f635ac251d22ed9ff953974) (struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) comp\_change) |
|  | Reprovision a Mesh Node using PB-Remote. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_is\_provisioned](#ga0307e62001ba7fa303ed311ebc47f116) (void) |
|  | Check if the local node has been provisioned. |

## Detailed Description

Provisioning.

## Enumeration Type Documentation

## [◆ ](#gabe5586cff0697e137730a52728978681)anonymous enum

| anonymous enum |
| --- |

`#include <[main.h](main_8h.md)>`

Available authentication algorithms.

| Enumerator | |
| --- | --- |
| BT\_MESH\_PROV\_AUTH\_CMAC\_AES128\_AES\_CCM |  |
| BT\_MESH\_PROV\_AUTH\_HMAC\_SHA256\_AES\_CCM |  |

## [◆ ](#gabec90bd95082b9dc8fa3ca27a9d7bc66)anonymous enum

| anonymous enum |
| --- |

`#include <[main.h](main_8h.md)>`

OOB Type field values.

| Enumerator | |
| --- | --- |
| BT\_MESH\_STATIC\_OOB\_AVAILABLE | Static OOB information available. |
| BT\_MESH\_OOB\_AUTH\_REQUIRED | OOB authentication required. |

## [◆ ](#gaf71f3dbdef6b8c085e9a4f068e1f60c5)bt\_mesh\_input\_action\_t

| enum [bt\_mesh\_input\_action\_t](#gaf71f3dbdef6b8c085e9a4f068e1f60c5) |
| --- |

`#include <[main.h](main_8h.md)>`

Available Provisioning input authentication actions.

| Enumerator | |
| --- | --- |
| BT\_MESH\_NO\_INPUT |  |
| BT\_MESH\_PUSH | Push. |
| BT\_MESH\_TWIST | Twist. |
| BT\_MESH\_ENTER\_NUMBER | Input number. |
| BT\_MESH\_ENTER\_STRING | Input alphanumeric. |

## [◆ ](#ga5512b81ef7eeb45b0a12ef62234c8795)bt\_mesh\_output\_action\_t

| enum [bt\_mesh\_output\_action\_t](#ga5512b81ef7eeb45b0a12ef62234c8795) |
| --- |

`#include <[main.h](main_8h.md)>`

Available Provisioning output authentication actions.

| Enumerator | |
| --- | --- |
| BT\_MESH\_NO\_OUTPUT |  |
| BT\_MESH\_BLINK | Blink. |
| BT\_MESH\_BEEP | Beep. |
| BT\_MESH\_VIBRATE | Vibrate. |
| BT\_MESH\_DISPLAY\_NUMBER | Output numeric. |
| BT\_MESH\_DISPLAY\_STRING | Output alphanumeric. |

## [◆ ](#gaa157eb0fee30c28092a11993872b8fdd)bt\_mesh\_prov\_bearer\_t

| enum [bt\_mesh\_prov\_bearer\_t](#gaa157eb0fee30c28092a11993872b8fdd) |
| --- |

`#include <[main.h](main_8h.md)>`

Available Provisioning bearers.

| Enumerator | |
| --- | --- |
| BT\_MESH\_PROV\_ADV | PB-ADV bearer. |
| BT\_MESH\_PROV\_GATT | PB-GATT bearer. |
| BT\_MESH\_PROV\_REMOTE | PB-Remote bearer. |

## [◆ ](#gaf93f7b49dada5c3f7accc54663648e48)bt\_mesh\_prov\_oob\_info\_t

| enum [bt\_mesh\_prov\_oob\_info\_t](#gaf93f7b49dada5c3f7accc54663648e48) |
| --- |

`#include <[main.h](main_8h.md)>`

Out of Band information location.

| Enumerator | |
| --- | --- |
| BT\_MESH\_PROV\_OOB\_OTHER | Other. |
| BT\_MESH\_PROV\_OOB\_URI | Electronic / URI. |
| BT\_MESH\_PROV\_OOB\_2D\_CODE | 2D machine-readable code |
| BT\_MESH\_PROV\_OOB\_BAR\_CODE | Bar Code. |
| BT\_MESH\_PROV\_OOB\_NFC | Near Field Communication (NFC). |
| BT\_MESH\_PROV\_OOB\_NUMBER | Number. |
| BT\_MESH\_PROV\_OOB\_STRING | String. |
| BT\_MESH\_PROV\_OOB\_CERTIFICATE | Support for certificate-based provisioning. |
| BT\_MESH\_PROV\_OOB\_RECORDS | Support for provisioning records. |
| BT\_MESH\_PROV\_OOB\_ON\_BOX | On box. |
| BT\_MESH\_PROV\_OOB\_IN\_BOX | Inside box. |
| BT\_MESH\_PROV\_OOB\_ON\_PAPER | On piece of paper. |
| BT\_MESH\_PROV\_OOB\_IN\_MANUAL | Inside manual. |
| BT\_MESH\_PROV\_OOB\_ON\_DEV | On device. |

## Function Documentation

## [◆ ](#ga80be35bf7287e62cb47d8fba99d648a9)bt\_mesh\_auth\_method\_set\_input()

| int bt\_mesh\_auth\_method\_set\_input | ( | [bt\_mesh\_input\_action\_t](#gaf71f3dbdef6b8c085e9a4f068e1f60c5) | *action*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *size* ) |

`#include <[main.h](main_8h.md)>`

Use Input OOB authentication.

Provisioner only.

Instruct the unprovisioned device to use the specified Input OOB authentication action. When using [BT\_MESH\_PUSH](#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ae4902ce51142fa49d2d5e97165d6f51c), [BT\_MESH\_TWIST](#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ad6f22211d09614181cb5b0f42300a9ee) or [BT\_MESH\_ENTER\_NUMBER](#ggaf71f3dbdef6b8c085e9a4f068e1f60c5aa0de3817e863d1f06888100de24fb4b0), the [bt\_mesh\_prov::output\_number](structbt__mesh__prov.md#af5c30f061ba8b0a713a3d54068dd68cc "bt_mesh_prov::output_number") callback is called with a random number that has to be entered on the unprovisioned device.

When using [BT\_MESH\_ENTER\_STRING](#ggaf71f3dbdef6b8c085e9a4f068e1f60c5a5d6bd8e6110c8f53245840aead4201c2), the [bt\_mesh\_prov::output\_string](structbt__mesh__prov.md#a28284efee6478637446702d7839f6b8c "bt_mesh_prov::output_string") callback is called with a random string that has to be entered on the unprovisioned device.

Parameters
:   | action | Authentication action used by the unprovisioned device. |
    | --- | --- |
    | size | Authentication size. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gabab41ebdcae2eaa109e03cb2d8fa78c6)bt\_mesh\_auth\_method\_set\_none()

| int bt\_mesh\_auth\_method\_set\_none | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[main.h](main_8h.md)>`

Don't use OOB authentication.

Provisioner only.

Don't use any authentication when provisioning new devices. This is the default behavior.

Warning
:   Not using any authentication exposes the mesh network to impersonation attacks, where attackers can pretend to be the unprovisioned device to gain access to the network. Authentication is strongly encouraged.

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gad66ccc725a1cfdf2b79076f22f853f84)bt\_mesh\_auth\_method\_set\_output()

| int bt\_mesh\_auth\_method\_set\_output | ( | [bt\_mesh\_output\_action\_t](#ga5512b81ef7eeb45b0a12ef62234c8795) | *action*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *size* ) |

`#include <[main.h](main_8h.md)>`

Use Output OOB authentication.

Provisioner only.

Instruct the unprovisioned device to use the specified Output OOB authentication action. The [bt\_mesh\_prov::input](structbt__mesh__prov.md#a31eff9c903ac721bbca7ab586dda9e80 "bt_mesh_prov::input") callback will be called.

When using [BT\_MESH\_BLINK](#gga5512b81ef7eeb45b0a12ef62234c8795ac38333011b4f76b036a04e41f1f71e83), [BT\_MESH\_BEEP](#gga5512b81ef7eeb45b0a12ef62234c8795ae50031a39d19181df17ee6de1a12272c), [BT\_MESH\_VIBRATE](#gga5512b81ef7eeb45b0a12ef62234c8795ab45021af96db0465f5edc6e0ea7b6079) or [BT\_MESH\_DISPLAY\_NUMBER](#gga5512b81ef7eeb45b0a12ef62234c8795a3586ffa3e36247e0d90b83c3f075e591), and the application has to call [bt\_mesh\_input\_number](#gace8cbf2a6e9144d3118054f234de02ef) with the random number indicated by the unprovisioned device.

When using [BT\_MESH\_DISPLAY\_STRING](#gga5512b81ef7eeb45b0a12ef62234c8795aa07d600f2afe278729bb4e35d41bf29b), the application has to call [bt\_mesh\_input\_string](#ga2592abf429b40ef9242bce26f5bd085e) with the random string displayed by the unprovisioned device.

Parameters
:   | action | Authentication action used by the unprovisioned device. |
    | --- | --- |
    | size | Authentication size. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga7b6024dc32f6ec7f26cbf91545911084)bt\_mesh\_auth\_method\_set\_static()

| int bt\_mesh\_auth\_method\_set\_static | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *static\_val*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *size* ) |

`#include <[main.h](main_8h.md)>`

Use static OOB authentication.

Provisioner only.

Instruct the unprovisioned device to use static OOB authentication, and use the given static authentication value when provisioning.

Parameters
:   | static\_val | Static OOB value. |
    | --- | --- |
    | size | Static OOB value size. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gace8cbf2a6e9144d3118054f234de02ef)bt\_mesh\_input\_number()

| int bt\_mesh\_input\_number | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *num* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[main.h](main_8h.md)>`

Provide provisioning input OOB number.

This is intended to be called after the [bt\_mesh\_prov](structbt__mesh__prov.md "Provisioning properties & capabilities.") input callback has been called with BT\_MESH\_ENTER\_NUMBER as the action.

Parameters
:   | num | Number. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga2592abf429b40ef9242bce26f5bd085e)bt\_mesh\_input\_string()

| int bt\_mesh\_input\_string | ( | const char \* | *str* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[main.h](main_8h.md)>`

Provide provisioning input OOB string.

This is intended to be called after the [bt\_mesh\_prov](structbt__mesh__prov.md "Provisioning properties & capabilities.") input callback has been called with BT\_MESH\_ENTER\_STRING as the action.

Parameters
:   | str | String. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga0307e62001ba7fa303ed311ebc47f116)bt\_mesh\_is\_provisioned()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_is\_provisioned | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[main.h](main_8h.md)>`

Check if the local node has been provisioned.

This API can be used to check if the local node has been provisioned or not. It can e.g. be helpful to determine if there was a stored network in flash, i.e. if the network was restored after calling [settings\_load()](group__settings.md#ga89c6d618df81f197cc5c1a2018b00648 "Load serialized items from registered persistence sources.").

Returns
:   True if the node is provisioned. False otherwise.

## [◆ ](#gac7e084e7d12a93377d49b1c3d6313399)bt\_mesh\_prov\_disable()

| int bt\_mesh\_prov\_disable | ( | [bt\_mesh\_prov\_bearer\_t](#gaa157eb0fee30c28092a11993872b8fdd) | *bearers* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[main.h](main_8h.md)>`

Disable specific provisioning bearers.

Disable one or more provisioning bearers.

Parameters
:   | bearers | Bit-wise or of provisioning bearers. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga6c8dc1b09d4cde8738be83c992b860a9)bt\_mesh\_prov\_enable()

| int bt\_mesh\_prov\_enable | ( | [bt\_mesh\_prov\_bearer\_t](#gaa157eb0fee30c28092a11993872b8fdd) | *bearers* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[main.h](main_8h.md)>`

Enable specific provisioning bearers.

Enable one or more provisioning bearers.

Parameters
:   | bearers | Bit-wise or of provisioning bearers. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gae33b5b6e9650b49d46494b4a81b18674)bt\_mesh\_prov\_remote\_pub\_key\_set()

| int bt\_mesh\_prov\_remote\_pub\_key\_set | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *public\_key*[64] | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[main.h](main_8h.md)>`

Provide Device public key.

Parameters
:   | public\_key | Device public key in big-endian. |
    | --- | --- |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga4ed6e078c1c0f197758c8dbb23db30f6)bt\_mesh\_provision()

| int bt\_mesh\_provision | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *net\_key*[16], |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *flags*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *iv\_index*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *dev\_key*[16] ) |

`#include <[main.h](main_8h.md)>`

Provision the local Mesh Node.

This API should normally not be used directly by the application. The only exception is for testing purposes where manual provisioning is desired without an actual external provisioner.

Parameters
:   | net\_key | Network Key |
    | --- | --- |
    | net\_idx | Network Key Index |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Provisioning Flags |
    | iv\_index | IV Index |
    | addr | Primary element address |
    | dev\_key | Device Key |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga0bfae4ebda53052cfa027c3a7ae51ec8)bt\_mesh\_provision\_adv()

| int bt\_mesh\_provision\_adv | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *uuid*[16], |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *attention\_duration* ) |

`#include <[main.h](main_8h.md)>`

Provision a Mesh Node using PB-ADV.

Parameters
:   | uuid | UUID |
    | --- | --- |
    | net\_idx | Network Key Index |
    | addr | Address to assign to remote device. If addr is 0, the lowest available address will be chosen. |
    | attention\_duration | The attention duration to be send to remote device |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga60666e0d7629caf36026974621bae664)bt\_mesh\_provision\_gatt()

| int bt\_mesh\_provision\_gatt | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *uuid*[16], |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *attention\_duration* ) |

`#include <[main.h](main_8h.md)>`

Provision a Mesh Node using PB-GATT.

Parameters
:   | uuid | UUID |
    | --- | --- |
    | net\_idx | Network Key Index |
    | addr | Address to assign to remote device. If addr is 0, the lowest available address will be chosen. |
    | attention\_duration | The attention duration to be send to remote device |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#ga9fc414e4e15d6b3ab0dae5483ed62982)bt\_mesh\_provision\_remote()

| int bt\_mesh\_provision\_remote | ( | struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \* | *srv*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *uuid*[16], |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *net\_idx*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr* ) |

`#include <[main.h](main_8h.md)>`

Provision a Mesh Node using PB-Remote.

Parameters
:   | cli | Remote Provisioning Client Model to provision with. |
    | --- | --- |
    | srv | Remote Provisioning Server that should be used to tunnel the provisioning. |
    | uuid | UUID of the unprovisioned node |
    | net\_idx | Network Key Index to give to the unprovisioned node. |
    | addr | Address to assign to remote device. If addr is 0, the lowest available address will be chosen. |

Returns
:   Zero on success or (negative) error code otherwise.

## [◆ ](#gaa02583390f635ac251d22ed9ff953974)bt\_mesh\_reprovision\_remote()

| int bt\_mesh\_reprovision\_remote | ( | struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \* | *cli*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \* | *srv*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *addr*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *comp\_change* ) |

`#include <[main.h](main_8h.md)>`

Reprovision a Mesh Node using PB-Remote.

Reprovisioning can be used to change the device key, unicast address and composition data of another device. The reprovisioning procedure uses the same protocol as normal provisioning, with the same level of security.

There are three tiers of reprovisioning:

1. Refreshing the device key
2. Refreshing the device key and node address. Composition data may change, including the number of elements.
3. Refreshing the device key and composition data, in case the composition data of the target node changed due to a firmware update or a similar procedure.

The target node indicates that its composition data changed by instantiating its composition data page 128. If the number of elements have changed, it may be necessary to move the unicast address of the target node as well, to avoid overlapping addresses.

Note
:   Changing the unicast addresses of the target node requires changes to all nodes that publish directly to any of the target node's models.

Parameters
:   | cli | Remote Provisioning Client Model to provision on |
    | --- | --- |
    | srv | Remote Provisioning Server to reprovision |
    | addr | Address to assign to remote device. If addr is 0, the lowest available address will be chosen. |
    | comp\_change | The target node has indicated that its composition data has changed. Note that the target node will reject the update if this isn't true. |

Returns
:   Zero on success or (negative) error code otherwise.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
