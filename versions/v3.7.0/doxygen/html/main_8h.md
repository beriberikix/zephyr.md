---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/main_8h.html
original_path: doxygen/html/main_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

main.h File Reference

Bluetooth Mesh Protocol APIs.
[More...](#details)

`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](main_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_dev\_capabilities](structbt__mesh__dev__capabilities.md) |
|  | Device Capabilities. [More...](structbt__mesh__dev__capabilities.md#details) |
| struct | [bt\_mesh\_prov](structbt__mesh__prov.md) |
|  | Provisioning properties & capabilities. [More...](structbt__mesh__prov.md#details) |
| struct | [bt\_mesh\_lpn\_cb](structbt__mesh__lpn__cb.md) |
|  | Low Power Node callback functions. [More...](structbt__mesh__lpn__cb.md#details) |
| struct | [bt\_mesh\_friend\_cb](structbt__mesh__friend__cb.md) |
|  | Friend Node callback functions. [More...](structbt__mesh__friend__cb.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_NET\_PRIMARY](group__bt__mesh.md#ga0d6985da3c7be76732ee103458b77121)   0x000 |
|  | Primary Network Key index. |
| #define | [BT\_MESH\_FEAT\_RELAY](group__bt__mesh.md#gac588eefe83db94784a420ce063f02b55)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
|  | Relay feature. |
| #define | [BT\_MESH\_FEAT\_PROXY](group__bt__mesh.md#gaee648ce202316c56d4d588cb0ad5aeb4)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
|  | GATT Proxy feature. |
| #define | [BT\_MESH\_FEAT\_FRIEND](group__bt__mesh.md#ga8f27086b3bc3c4a6e14621836f9f8e80)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
|  | Friend feature. |
| #define | [BT\_MESH\_FEAT\_LOW\_POWER](group__bt__mesh.md#gaad71a36c82b4e4d3fa334ecff5cc0171)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
|  | Low Power Node feature. |
| #define | [BT\_MESH\_FEAT\_SUPPORTED](group__bt__mesh.md#gac337fd8688d70e862974e010ad42a11b) |
|  | Supported heartbeat publication features. |
| #define | [BT\_MESH\_LPN\_CB\_DEFINE](group__bt__mesh.md#gac18d4ce09495a8ade098a6320bb26ec2)(\_name) |
|  | Register a callback structure for Friendship events. |
| #define | [BT\_MESH\_FRIEND\_CB\_DEFINE](group__bt__mesh.md#ga4f00fa03af86b39e24140eb09c51ca4c)(\_name) |
|  | Register a callback structure for Friendship events. |

| Enumerations | |
| --- | --- |
| enum | { [BT\_MESH\_PROV\_AUTH\_CMAC\_AES128\_AES\_CCM](group__bt__mesh__prov.md#ggabe5586cff0697e137730a52728978681affa8679d8be1a12714a34ed09c3b05dd) , [BT\_MESH\_PROV\_AUTH\_HMAC\_SHA256\_AES\_CCM](group__bt__mesh__prov.md#ggabe5586cff0697e137730a52728978681a292bf2e4d29f0bd0d746bbb871f2ee5a) } |
|  | Available authentication algorithms. [More...](group__bt__mesh__prov.md#gabe5586cff0697e137730a52728978681) |
| enum | { [BT\_MESH\_STATIC\_OOB\_AVAILABLE](group__bt__mesh__prov.md#ggabec90bd95082b9dc8fa3ca27a9d7bc66a30e46fe23e508029b570e1f107b38d40) = BIT(0) , [BT\_MESH\_OOB\_AUTH\_REQUIRED](group__bt__mesh__prov.md#ggabec90bd95082b9dc8fa3ca27a9d7bc66a61f859a15fabc8d9fd278dabe5a86a37) = BIT(1) } |
|  | OOB Type field values. [More...](group__bt__mesh__prov.md#gabec90bd95082b9dc8fa3ca27a9d7bc66) |
| enum | [bt\_mesh\_output\_action\_t](group__bt__mesh__prov.md#ga5512b81ef7eeb45b0a12ef62234c8795) {     [BT\_MESH\_NO\_OUTPUT](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795ad009060fd1f501c8362a63e6c020b113) = 0 , [BT\_MESH\_BLINK](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795ac38333011b4f76b036a04e41f1f71e83) = BIT(0) , [BT\_MESH\_BEEP](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795ae50031a39d19181df17ee6de1a12272c) = BIT(1) , [BT\_MESH\_VIBRATE](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795ab45021af96db0465f5edc6e0ea7b6079) = BIT(2) ,     [BT\_MESH\_DISPLAY\_NUMBER](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795a3586ffa3e36247e0d90b83c3f075e591) = BIT(3) , [BT\_MESH\_DISPLAY\_STRING](group__bt__mesh__prov.md#gga5512b81ef7eeb45b0a12ef62234c8795aa07d600f2afe278729bb4e35d41bf29b) = BIT(4)   } |
|  | Available Provisioning output authentication actions. [More...](group__bt__mesh__prov.md#ga5512b81ef7eeb45b0a12ef62234c8795) |
| enum | [bt\_mesh\_input\_action\_t](group__bt__mesh__prov.md#gaf71f3dbdef6b8c085e9a4f068e1f60c5) {     [BT\_MESH\_NO\_INPUT](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ac721b070cad51f1cd9aa1f0b60e59056) = 0 , [BT\_MESH\_PUSH](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ae4902ce51142fa49d2d5e97165d6f51c) = BIT(0) , [BT\_MESH\_TWIST](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5ad6f22211d09614181cb5b0f42300a9ee) = BIT(1) , [BT\_MESH\_ENTER\_NUMBER](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5aa0de3817e863d1f06888100de24fb4b0) = BIT(2) ,     [BT\_MESH\_ENTER\_STRING](group__bt__mesh__prov.md#ggaf71f3dbdef6b8c085e9a4f068e1f60c5a5d6bd8e6110c8f53245840aead4201c2) = BIT(3)   } |
|  | Available Provisioning input authentication actions. [More...](group__bt__mesh__prov.md#gaf71f3dbdef6b8c085e9a4f068e1f60c5) |
| enum | [bt\_mesh\_prov\_bearer\_t](group__bt__mesh__prov.md#gaa157eb0fee30c28092a11993872b8fdd) { [BT\_MESH\_PROV\_ADV](group__bt__mesh__prov.md#ggaa157eb0fee30c28092a11993872b8fdda5142f018a5426a047688c6507b3af4f8) = BIT(0) , [BT\_MESH\_PROV\_GATT](group__bt__mesh__prov.md#ggaa157eb0fee30c28092a11993872b8fdda27c9c1278acc887214a4a30294bf52d8) = BIT(1) , [BT\_MESH\_PROV\_REMOTE](group__bt__mesh__prov.md#ggaa157eb0fee30c28092a11993872b8fdda4222d03b09ba43b6ea772738b8987501) = BIT(2) } |
|  | Available Provisioning bearers. [More...](group__bt__mesh__prov.md#gaa157eb0fee30c28092a11993872b8fdd) |
| enum | [bt\_mesh\_prov\_oob\_info\_t](group__bt__mesh__prov.md#gaf93f7b49dada5c3f7accc54663648e48) {     [BT\_MESH\_PROV\_OOB\_OTHER](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a487ffb56c8c15a37b69fa1699fff301a) = BIT(0) , [BT\_MESH\_PROV\_OOB\_URI](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48ad861e8de3c1fbc1658a6d0fba38785dd) = BIT(1) , [BT\_MESH\_PROV\_OOB\_2D\_CODE](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a34d005022a75446a386006f7690a473e) = BIT(2) , [BT\_MESH\_PROV\_OOB\_BAR\_CODE](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48abe8fd10b49a7bb6c7499eb73ae3876d3) = BIT(3) ,     [BT\_MESH\_PROV\_OOB\_NFC](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48ad9b4089a740d47950c02b4389d29df56) = BIT(4) , [BT\_MESH\_PROV\_OOB\_NUMBER](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48ac5d40459453afebc841f32e1f0b33fbc) = BIT(5) , [BT\_MESH\_PROV\_OOB\_STRING](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a8553379d579a418a6453669323b18088) = BIT(6) , [BT\_MESH\_PROV\_OOB\_CERTIFICATE](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a00eb3ba6b7940b02d2fe3892100f497e) = BIT(7) ,     [BT\_MESH\_PROV\_OOB\_RECORDS](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48aa10724108397ab8d48a3aac2817992f2) = BIT(8) , [BT\_MESH\_PROV\_OOB\_ON\_BOX](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48adbbc3c3829bb7caf1a4a5fd2066f3b4a) = BIT(11) , [BT\_MESH\_PROV\_OOB\_IN\_BOX](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48ae855a27a18bfb6ea03f0ff6165e4a291) = BIT(12) , [BT\_MESH\_PROV\_OOB\_ON\_PAPER](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a137946e3d53b996b77bebeda5fa930cb) = BIT(13) ,     [BT\_MESH\_PROV\_OOB\_IN\_MANUAL](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48a4a8a7e4ab87cf360abdb167076349072) = BIT(14) , [BT\_MESH\_PROV\_OOB\_ON\_DEV](group__bt__mesh__prov.md#ggaf93f7b49dada5c3f7accc54663648e48aa73dd9517eec86e51b48d256fc9660da) = BIT(15)   } |
|  | Out of Band information location. [More...](group__bt__mesh__prov.md#gaf93f7b49dada5c3f7accc54663648e48) |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_input\_string](group__bt__mesh__prov.md#ga2592abf429b40ef9242bce26f5bd085e) (const char \*str) |
|  | Provide provisioning input OOB string. |
| int | [bt\_mesh\_input\_number](group__bt__mesh__prov.md#gace8cbf2a6e9144d3118054f234de02ef) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num) |
|  | Provide provisioning input OOB number. |
| int | [bt\_mesh\_prov\_remote\_pub\_key\_set](group__bt__mesh__prov.md#gae33b5b6e9650b49d46494b4a81b18674) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) public\_key[64]) |
|  | Provide Device public key. |
| int | [bt\_mesh\_auth\_method\_set\_input](group__bt__mesh__prov.md#ga80be35bf7287e62cb47d8fba99d648a9) ([bt\_mesh\_input\_action\_t](group__bt__mesh__prov.md#gaf71f3dbdef6b8c085e9a4f068e1f60c5) action, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size) |
|  | Use Input OOB authentication. |
| int | [bt\_mesh\_auth\_method\_set\_output](group__bt__mesh__prov.md#gad66ccc725a1cfdf2b79076f22f853f84) ([bt\_mesh\_output\_action\_t](group__bt__mesh__prov.md#ga5512b81ef7eeb45b0a12ef62234c8795) action, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size) |
|  | Use Output OOB authentication. |
| int | [bt\_mesh\_auth\_method\_set\_static](group__bt__mesh__prov.md#ga7b6024dc32f6ec7f26cbf91545911084) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*static\_val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size) |
|  | Use static OOB authentication. |
| int | [bt\_mesh\_auth\_method\_set\_none](group__bt__mesh__prov.md#gabab41ebdcae2eaa109e03cb2d8fa78c6) (void) |
|  | Don't use OOB authentication. |
| int | [bt\_mesh\_prov\_enable](group__bt__mesh__prov.md#ga6c8dc1b09d4cde8738be83c992b860a9) ([bt\_mesh\_prov\_bearer\_t](group__bt__mesh__prov.md#gaa157eb0fee30c28092a11993872b8fdd) bearers) |
|  | Enable specific provisioning bearers. |
| int | [bt\_mesh\_prov\_disable](group__bt__mesh__prov.md#gac7e084e7d12a93377d49b1c3d6313399) ([bt\_mesh\_prov\_bearer\_t](group__bt__mesh__prov.md#gaa157eb0fee30c28092a11993872b8fdd) bearers) |
|  | Disable specific provisioning bearers. |
| int | [bt\_mesh\_provision](group__bt__mesh__prov.md#ga4ed6e078c1c0f197758c8dbb23db30f6) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) net\_key[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) iv\_index, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dev\_key[16]) |
|  | Provision the local Mesh Node. |
| int | [bt\_mesh\_provision\_adv](group__bt__mesh__prov.md#ga0bfae4ebda53052cfa027c3a7ae51ec8) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uuid[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attention\_duration) |
|  | Provision a Mesh Node using PB-ADV. |
| int | [bt\_mesh\_provision\_gatt](group__bt__mesh__prov.md#ga60666e0d7629caf36026974621bae664) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uuid[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) attention\_duration) |
|  | Provision a Mesh Node using PB-GATT. |
| int | [bt\_mesh\_provision\_remote](group__bt__mesh__prov.md#ga9fc414e4e15d6b3ab0dae5483ed62982) (struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) uuid[16], [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) net\_idx, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
|  | Provision a Mesh Node using PB-Remote. |
| int | [bt\_mesh\_reprovision\_remote](group__bt__mesh__prov.md#gaa02583390f635ac251d22ed9ff953974) (struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*srv, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) comp\_change) |
|  | Reprovision a Mesh Node using PB-Remote. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_is\_provisioned](group__bt__mesh__prov.md#ga0307e62001ba7fa303ed311ebc47f116) (void) |
|  | Check if the local node has been provisioned. |
| int | [bt\_mesh\_init](group__bt__mesh.md#ga521def6f74467a9bd3f2757c6aabd405) (const struct [bt\_mesh\_prov](structbt__mesh__prov.md) \*prov, const struct [bt\_mesh\_comp](structbt__mesh__comp.md) \*comp) |
|  | Initialize Mesh support. |
| void | [bt\_mesh\_reset](group__bt__mesh.md#ga69fc65f4e07e6007388473f139e5d8d8) (void) |
|  | Reset the state of the local Mesh node. |
| int | [bt\_mesh\_suspend](group__bt__mesh.md#ga6c209dbad6881f1e9634d9b7d42f2c34) (void) |
|  | Suspend the Mesh network temporarily. |
| int | [bt\_mesh\_resume](group__bt__mesh.md#gaa9114ce8941e641dbb23828d7c0451fd) (void) |
|  | Resume a suspended Mesh network. |
| void | [bt\_mesh\_iv\_update\_test](group__bt__mesh.md#ga3fdc601bd036477f6bdf212667c6b0c9) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Toggle the IV Update test mode. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_iv\_update](group__bt__mesh.md#gacdf00423b03057fdf3a4207ee579eb74) (void) |
|  | Toggle the IV Update state. |
| int | [bt\_mesh\_lpn\_set](group__bt__mesh.md#ga7964f5b1abb7b12728e4ec224c95c849) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enable) |
|  | Toggle the Low Power feature of the local device. |
| int | [bt\_mesh\_lpn\_poll](group__bt__mesh.md#ga3fd66605950a55e299ca3a7cc697d453) (void) |
|  | Send out a Friend Poll message. |
| int | [bt\_mesh\_friend\_terminate](group__bt__mesh.md#ga28b9b1d7d732e300be8d4bbffdbad391) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) lpn\_addr) |
|  | Terminate Friendship. |
| void | [bt\_mesh\_rpl\_pending\_store](group__bt__mesh.md#ga62f9a72c4e9dc5e4f3f42bd4df4fe452) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr) |
|  | Store pending RPL entry(ies) in the persistent storage. |
| const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [bt\_mesh\_va\_uuid\_get](group__bt__mesh.md#ga20fe74e33e6a35c452cd076c78aa4f05) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*uuid, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*retaddr) |
|  | Iterate stored Label UUIDs. |

## Detailed Description

Bluetooth Mesh Protocol APIs.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [main.h](main_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
