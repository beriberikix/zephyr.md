---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/devicetree_8h.html
original_path: doxygen/html/devicetree_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

devicetree.h File Reference

Devicetree main header.
[More...](#details)

`#include <zephyr/devicetree_generated.h>`  
`#include <[zephyr/irq_multilevel.h](irq__multilevel_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/devicetree/io-channels.h](io-channels_8h_source.md)>`  
`#include <[zephyr/devicetree/clocks.h](clocks_8h_source.md)>`  
`#include <[zephyr/devicetree/gpio.h](devicetree_2gpio_8h_source.md)>`  
`#include <[zephyr/devicetree/spi.h](devicetree_2spi_8h_source.md)>`  
`#include <[zephyr/devicetree/dma.h](devicetree_2dma_8h_source.md)>`  
`#include <[zephyr/devicetree/pwms.h](pwms_8h_source.md)>`  
`#include <[zephyr/devicetree/fixed-partitions.h](fixed-partitions_8h_source.md)>`  
`#include <[zephyr/devicetree/ordinals.h](ordinals_8h_source.md)>`  
`#include <[zephyr/devicetree/pinctrl.h](devicetree_2pinctrl_8h_source.md)>`  
`#include <[zephyr/devicetree/can.h](devicetree_2can_8h_source.md)>`  
`#include <[zephyr/devicetree/reset.h](devicetree_2reset_8h_source.md)>`  
`#include <[zephyr/devicetree/mbox.h](devicetree_2mbox_8h_source.md)>`  
`#include <[zephyr/devicetree/port-endpoint.h](port-endpoint_8h_source.md)>`

[Go to the source code of this file.](devicetree_8h_source.md)

| Macros | |
| --- | --- |
| #define | [DT\_INVALID\_NODE](group__devicetree-generic-id.md#ga710cc4455dd7e738f43f750153163855)   \_ |
|  | Name for an invalid node identifier. |
| #define | [DT\_ROOT](group__devicetree-generic-id.md#gad65aa36621281687b22fa5d72db33e86)   DT\_N |
|  | Node identifier for the root node in the devicetree. |
| #define | [DT\_PATH](group__devicetree-generic-id.md#ga015b4819473797982e83cae497697086)(...) |
|  | Get a node identifier for a devicetree path. |
| #define | [DT\_NODELABEL](group__devicetree-generic-id.md#gab7d23294a6bf7fd44a98b48ec47d8a79)(label) |
|  | Get a node identifier for a node label. |
| #define | [DT\_ALIAS](group__devicetree-generic-id.md#gaa49e19bbc39dc0d6f16b78a5d02482c9)(alias) |
|  | Get a node identifier from /aliases. |
| #define | [DT\_HAS\_ALIAS](group__devicetree-generic-id.md#ga1f6c459577dbb195192bef33a30c5d51)(alias\_name) |
|  | Test if the devicetree has a given alias. |
| #define | [DT\_NODE\_HASH](group__devicetree-generic-id.md#ga067821c9b49437ac9333fd2a0443f1fc)(node\_id) |
|  | Get the hash associated with a DT node. |
| #define | [DT\_INST](group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead)(inst, compat) |
|  | Get a node identifier for an instance of a compatible. |
| #define | [DT\_PARENT](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)(node\_id) |
|  | Get a node identifier for a parent node. |
| #define | [DT\_GPARENT](group__devicetree-generic-id.md#gaa4eccf276a426cbbc6e440d72b692753)(node\_id) |
|  | Get a node identifier for a grandparent node. |
| #define | [DT\_CHILD](group__devicetree-generic-id.md#ga88259608f4e9083ccc2e9ca5ec2c212e)(node\_id, child) |
|  | Get a node identifier for a child node. |
| #define | [DT\_COMPAT\_GET\_ANY\_STATUS\_OKAY](group__devicetree-generic-id.md#ga4858c378b098dcb7c35de1db25442acc)(compat) |
|  | Get a node identifier for a status okay node with a compatible. |
| #define | [DT\_NODE\_PATH](group__devicetree-generic-id.md#gacd79818b99724d834e3bb7ae74ee02cf)(node\_id) |
|  | Get a devicetree node's full path as a string literal. |
| #define | [DT\_NODE\_FULL\_NAME](group__devicetree-generic-id.md#ga8a8ab5d12fe59787433d1add94fb1667)(node\_id) |
|  | Get a devicetree node's name with unit-address as a string literal. |
| #define | [DT\_NODE\_FULL\_NAME\_UNQUOTED](group__devicetree-generic-id.md#ga8832fb6fa0e0555884621d210440fdcd)(node\_id) |
|  | Get the node's full name, including the unit-address, as an unquoted sequence of tokens. |
| #define | [DT\_NODE\_FULL\_NAME\_TOKEN](group__devicetree-generic-id.md#gad24b51e728175e7d347407f2131a3850)(node\_id) |
|  | Get the node's full name, including the unit-address, as a token. |
| #define | [DT\_NODE\_FULL\_NAME\_UPPER\_TOKEN](group__devicetree-generic-id.md#gab966ae50efe46cc3a54f086f508edb3b)(node\_id) |
|  | Like [DT\_NODE\_FULL\_NAME\_TOKEN()](group__devicetree-generic-id.md#gad24b51e728175e7d347407f2131a3850 "Get the node's full name, including the unit-address, as a token."), but uppercased. |
| #define | [DT\_NODE\_CHILD\_IDX](group__devicetree-generic-id.md#ga34452788d4fed1fce3e6650d61246866)(node\_id) |
|  | Get a devicetree node's index into its parent's list of children. |
| #define | [DT\_CHILD\_NUM](group__devicetree-generic-id.md#ga37cf660c2a7a844f70191d21b6543dc1)(node\_id) |
|  | Get the number of child nodes of a given node. |
| #define | [DT\_CHILD\_NUM\_STATUS\_OKAY](group__devicetree-generic-id.md#ga98544b8fd880fdd632f18e2410d39739)(node\_id) |
|  | Get the number of child nodes of a given node which child nodes' status are okay. |
| #define | [DT\_SAME\_NODE](group__devicetree-generic-id.md#ga977d0ad58626e3ab906064fdcdace5e6)(node\_id1, node\_id2) |
|  | Do `node_id1` and `node_id2` refer to the same node? |
| #define | [DT\_NODELABEL\_STRING\_ARRAY](group__devicetree-generic-id.md#ga0114cbfa3a2075558769d4632b7bb1e9)(node\_id) |
|  | Get a devicetree node's node labels as an array of strings. |
| #define | [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, prop) |
|  | Get a devicetree property value. |
| #define | [DT\_PROP\_LEN](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)(node\_id, prop) |
|  | Get a property's logical length. |
| #define | [DT\_PROP\_LEN\_OR](group__devicetree-generic-prop.md#gabd2d8a9242818c7a9bf981114c912d75)(node\_id, prop, default\_value) |
|  | Like [DT\_PROP\_LEN()](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6 "Get a property's logical length."), but with a fallback to `default_value`. |
| #define | [DT\_PROP\_HAS\_IDX](group__devicetree-generic-prop.md#ga479dfc704087eea7e7c5af42ae98576c)(node\_id, prop, idx) |
|  | Is index `idx` valid for an array type property? |
| #define | [DT\_PROP\_HAS\_NAME](group__devicetree-generic-prop.md#gae46c100aecd299eaea51e033890d9a58)(node\_id, prop, name) |
|  | Is name `name` available in a foo-names property? |
| #define | [DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)(node\_id, prop, idx) |
|  | Get the value at index `idx` in an array type property. |
| #define | [DT\_PROP\_LAST](group__devicetree-generic-prop.md#ga05a04871d83b31834c134a64636dcd8a)(node\_id, prop) |
|  | Get the last element of an array type property. |
| #define | [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(node\_id, prop, default\_value) |
|  | Like [DT\_PROP()](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b "Get a devicetree property value."), but with a fallback to `default_value`. |
| #define | [DT\_ENUM\_IDX\_BY\_IDX](group__devicetree-generic-prop.md#gae2e5f62d8f0c1eefcbb60ec7a5e84be2)(node\_id, prop, idx) |
|  | Get a property array value's index into its enumeration values. |
| #define | [DT\_ENUM\_IDX](group__devicetree-generic-prop.md#ga6c1a3b93e30429c1c69a7e2d8fe2d840)(node\_id, prop) |
|  | Equivalent to [DT\_ENUM\_IDX\_BY\_IDX(node\_id, prop, 0)](group__devicetree-generic-prop.md#gae2e5f62d8f0c1eefcbb60ec7a5e84be2 "DT_ENUM_IDX_BY_IDX(node_id, prop, 0)"). |
| #define | [DT\_ENUM\_IDX\_BY\_IDX\_OR](group__devicetree-generic-prop.md#gac4892f2a54e05bd922f8c85db9c16d73)(node\_id, prop, idx, default\_idx\_value) |
|  | Like [DT\_ENUM\_IDX\_BY\_IDX()](group__devicetree-generic-prop.md#gae2e5f62d8f0c1eefcbb60ec7a5e84be2 "Get a property array value's index into its enumeration values."), but with a fallback to a default enum index. |
| #define | [DT\_ENUM\_IDX\_OR](group__devicetree-generic-prop.md#gac3616e3aa1a025235032786de8d31576)(node\_id, prop, default\_idx\_value) |
|  | Equivalent to [DT\_ENUM\_IDX\_BY\_IDX\_OR(node\_id, prop, 0, default\_idx\_value)](group__devicetree-generic-prop.md#gac4892f2a54e05bd922f8c85db9c16d73 "Like DT_ENUM_IDX_BY_IDX(), but with a fallback to a default enum index."). |
| #define | [DT\_ENUM\_HAS\_VALUE\_BY\_IDX](group__devicetree-generic-prop.md#ga3c8b19de88ffdb4246567bb54ef6e6a4)(node\_id, prop, idx, value) |
|  | Does a node enumeration property array have a given value? |
| #define | [DT\_ENUM\_HAS\_VALUE](group__devicetree-generic-prop.md#ga72e66a2b7a159d8b6210ef9be015c955)(node\_id, prop, value) |
|  | Equivalent to [DT\_ENUM\_HAS\_VALUE\_BY\_IDX(node\_id, prop, 0, value)](group__devicetree-generic-prop.md#ga3c8b19de88ffdb4246567bb54ef6e6a4 "Does a node enumeration property array have a given value?"). |
| #define | [DT\_STRING\_TOKEN](group__devicetree-generic-prop.md#ga5995350cc7fd2d12ef7daa2487d1db54)(node\_id, prop) |
|  | Get a string property's value as a token. |
| #define | [DT\_STRING\_TOKEN\_OR](group__devicetree-generic-prop.md#ga5c7c7f82abd34403d4e9a6e0c5703e4c)(node\_id, prop, default\_value) |
|  | Like [DT\_STRING\_TOKEN()](group__devicetree-generic-prop.md#ga5995350cc7fd2d12ef7daa2487d1db54 "Get a string property's value as a token."), but with a fallback to `default_value`. |
| #define | [DT\_STRING\_UPPER\_TOKEN](group__devicetree-generic-prop.md#gae0b5e2b6633a98ead17ec20d3494658f)(node\_id, prop) |
|  | Like [DT\_STRING\_TOKEN()](group__devicetree-generic-prop.md#ga5995350cc7fd2d12ef7daa2487d1db54 "Get a string property's value as a token."), but uppercased. |
| #define | [DT\_STRING\_UPPER\_TOKEN\_OR](group__devicetree-generic-prop.md#gab79f5274c82d025d805ec94d2935c9b9)(node\_id, prop, default\_value) |
|  | Like [DT\_STRING\_UPPER\_TOKEN()](group__devicetree-generic-prop.md#gae0b5e2b6633a98ead17ec20d3494658f "Like DT_STRING_TOKEN(), but uppercased."), but with a fallback to `default_value`. |
| #define | [DT\_STRING\_UNQUOTED](group__devicetree-generic-prop.md#gad71ae303ce20e116a75c23ca552c2225)(node\_id, prop) |
|  | Get a string property's value as an unquoted sequence of tokens. |
| #define | [DT\_STRING\_UNQUOTED\_OR](group__devicetree-generic-prop.md#gad9fefdcc15e991ba526300cd20f7c2fa)(node\_id, prop, default\_value) |
|  | Like [DT\_STRING\_UNQUOTED()](group__devicetree-generic-prop.md#gad71ae303ce20e116a75c23ca552c2225 "Get a string property's value as an unquoted sequence of tokens."), but with a fallback to `default_value`. |
| #define | [DT\_STRING\_TOKEN\_BY\_IDX](group__devicetree-generic-prop.md#ga583e5e2e3c897f1095073e6192061d3a)(node\_id, prop, idx) |
|  | Get an element out of a string-array property as a token. |
| #define | [DT\_STRING\_UPPER\_TOKEN\_BY\_IDX](group__devicetree-generic-prop.md#ga73105b3402fbd6f82274a8b4a2ca6b35)(node\_id, prop, idx) |
|  | Like [DT\_STRING\_TOKEN\_BY\_IDX()](group__devicetree-generic-prop.md#ga583e5e2e3c897f1095073e6192061d3a "Get an element out of a string-array property as a token."), but uppercased. |
| #define | [DT\_STRING\_UNQUOTED\_BY\_IDX](group__devicetree-generic-prop.md#ga3736709d70fdcb00bf305fd500f9ab64)(node\_id, prop, idx) |
|  | Get a string array item value as an unquoted sequence of tokens. |
| #define | [DT\_PROP\_BY\_PHANDLE\_IDX](group__devicetree-generic-prop.md#gaeba973992914d493cff5506ecf86a00d)(node\_id, phs, idx, prop) |
|  | Get a property value from a phandle in a property. |
| #define | [DT\_PROP\_BY\_PHANDLE\_IDX\_OR](group__devicetree-generic-prop.md#gad1c6a6544eac7bc77c1ed4aebd15df2b)(node\_id, phs, idx, prop, default\_value) |
|  | Like [DT\_PROP\_BY\_PHANDLE\_IDX()](group__devicetree-generic-prop.md#gaeba973992914d493cff5506ecf86a00d "Get a property value from a phandle in a property."), but with a fallback to `default_value`. |
| #define | [DT\_PROP\_BY\_PHANDLE](group__devicetree-generic-prop.md#gabc1b099dda97fb03a9259a8b21fc04d2)(node\_id, ph, prop) |
|  | Get a property value from a phandle's node. |
| #define | [DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)(node\_id, pha, idx, cell) |
|  | Get a phandle-array specifier cell value at an index. |
| #define | [DT\_PHA\_BY\_IDX\_OR](group__devicetree-generic-prop.md#gad830ed96dbc4f7dac3455153e0a944d6)(node\_id, pha, idx, cell, default\_value) |
|  | Like [DT\_PHA\_BY\_IDX()](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed "Get a phandle-array specifier cell value at an index."), but with a fallback to `default_value`. |
| #define | [DT\_PHA](group__devicetree-generic-prop.md#gacef5921973a55433161fe0be3f8f628d)(node\_id, pha, cell) |
|  | Equivalent to [DT\_PHA\_BY\_IDX(node\_id, pha, 0, cell)](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed "Get a phandle-array specifier cell value at an index."). |
| #define | [DT\_PHA\_OR](group__devicetree-generic-prop.md#ga886559b058b24164b62ab95215d860bd)(node\_id, pha, cell, default\_value) |
|  | Like [DT\_PHA()](group__devicetree-generic-prop.md#gacef5921973a55433161fe0be3f8f628d "Equivalent to DT_PHA_BY_IDX(node_id, pha, 0, cell)."), but with a fallback to `default_value`. |
| #define | [DT\_PHA\_BY\_NAME](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)(node\_id, pha, name, cell) |
|  | Get a value within a phandle-array specifier by name. |
| #define | [DT\_PHA\_BY\_NAME\_OR](group__devicetree-generic-prop.md#ga79cda6ca70cc1e27b034ad096d4f4401)(node\_id, pha, name, cell, default\_value) |
|  | Like [DT\_PHA\_BY\_NAME()](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26 "Get a value within a phandle-array specifier by name."), but with a fallback to `default_value`. |
| #define | [DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)(node\_id, pha, name) |
|  | Get a phandle's node identifier from a phandle array by `name`. |
| #define | [DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)(node\_id, prop, idx) |
|  | Get a node identifier for a phandle in a property. |
| #define | [DT\_PHANDLE](group__devicetree-generic-prop.md#ga7bd77c49472ba4547d87f00f40fd7171)(node\_id, prop) |
|  | Get a node identifier for a phandle property's value. |
| #define | [DT\_NUM\_RANGES](group__devicetree-ranges-prop.md#ga784cff5ee4c0439c429cc3c26c4410fc)(node\_id) |
|  | Get the number of range blocks in the ranges property. |
| #define | [DT\_RANGES\_HAS\_IDX](group__devicetree-ranges-prop.md#gac6f54058c58b06935bd2deae9f1ec2db)(node\_id, idx) |
|  | Is `idx` a valid range block index? |
| #define | [DT\_RANGES\_HAS\_CHILD\_BUS\_FLAGS\_AT\_IDX](group__devicetree-ranges-prop.md#ga3730c9176911bd8cc762f447eb020ecd)(node\_id, idx) |
|  | Does a ranges property have child bus flags at index? |
| #define | [DT\_RANGES\_CHILD\_BUS\_FLAGS\_BY\_IDX](group__devicetree-ranges-prop.md#ga32a9c873d3ec1f5d7922c38eaafd1af8)(node\_id, idx) |
|  | Get the ranges property child bus flags at index. |
| #define | [DT\_RANGES\_CHILD\_BUS\_ADDRESS\_BY\_IDX](group__devicetree-ranges-prop.md#ga449940559213086b15151ec00e46607d)(node\_id, idx) |
|  | Get the ranges property child bus address at index. |
| #define | [DT\_RANGES\_PARENT\_BUS\_ADDRESS\_BY\_IDX](group__devicetree-ranges-prop.md#ga48d493ad616438ace2396c0312a242ba)(node\_id, idx) |
|  | Get the ranges property parent bus address at index. |
| #define | [DT\_RANGES\_LENGTH\_BY\_IDX](group__devicetree-ranges-prop.md#ga52677a5bc86f9132a09b6bc37153afb2)(node\_id, idx) |
|  | Get the ranges property length at index. |
| #define | [DT\_FOREACH\_RANGE](group__devicetree-ranges-prop.md#ga4c71a8adcfe6c53b480775510c92a632)(node\_id, fn) |
|  | Invokes `fn` for each entry of `node_id` ranges property. |
| #define | [DT\_NODE\_VENDOR\_BY\_IDX](group__devicetree-generic-vendor.md#gafcd6cc682b573d61c7e28c8e3bafc747)(node\_id, idx) |
|  | Get the vendor at index `idx` as a string literal. |
| #define | [DT\_NODE\_VENDOR\_HAS\_IDX](group__devicetree-generic-vendor.md#gabfa4130fa24457c457961caa7e2c6276)(node\_id, idx) |
|  | Does a node's compatible property have a vendor at an index? |
| #define | [DT\_NODE\_VENDOR\_BY\_IDX\_OR](group__devicetree-generic-vendor.md#gaa71b1152516847d51582b9b23c472f3d)(node\_id, idx, default\_value) |
|  | Like [DT\_NODE\_VENDOR\_BY\_IDX()](group__devicetree-generic-vendor.md#gafcd6cc682b573d61c7e28c8e3bafc747 "Get the vendor at index idx as a string literal."), but with a fallback to default\_value. |
| #define | [DT\_NODE\_VENDOR\_OR](group__devicetree-generic-vendor.md#gad91ad9294d36eb151c96e719f1a5b0ef)(node\_id, default\_value) |
|  | Get the node's (only) vendor as a string literal. |
| #define | [DT\_NODE\_MODEL\_BY\_IDX](group__devicetree-generic-vendor.md#gae4bbd66726d930d878588f9bb9f4d500)(node\_id, idx) |
|  | Get the model at index "idx" as a string literal. |
| #define | [DT\_NODE\_MODEL\_HAS\_IDX](group__devicetree-generic-vendor.md#ga2ff3c91b22fae081d00d96964f465aa2)(node\_id, idx) |
|  | Does a node's compatible property have a model at an index? |
| #define | [DT\_NODE\_MODEL\_BY\_IDX\_OR](group__devicetree-generic-vendor.md#ga98a2ff981359088e2e995017791176b1)(node\_id, idx, default\_value) |
|  | Like [DT\_NODE\_MODEL\_BY\_IDX()](group__devicetree-generic-vendor.md#gae4bbd66726d930d878588f9bb9f4d500 "Get the model at index "idx" as a string literal."), but with a fallback to default\_value. |
| #define | [DT\_NODE\_MODEL\_OR](group__devicetree-generic-vendor.md#ga239f5fc9f6f33cf83e6c7ebfeef15d0f)(node\_id, default\_value) |
|  | Get the node's (only) model as a string literal. |
| #define | [DT\_NUM\_REGS](group__devicetree-reg-prop.md#ga6cdd22b6a2881b09ed63d9d262566a0a)(node\_id) |
|  | Get the number of register blocks in the reg property. |
| #define | [DT\_REG\_HAS\_IDX](group__devicetree-reg-prop.md#ga59aa43231678d08eeac6e5b344048f02)(node\_id, idx) |
|  | Is `idx` a valid register block index? |
| #define | [DT\_REG\_HAS\_NAME](group__devicetree-reg-prop.md#ga2c68672c60d95725b69371c3ab306d24)(node\_id, name) |
|  | Is `name` a valid register block name? |
| #define | [DT\_REG\_ADDR\_BY\_IDX\_RAW](group__devicetree-reg-prop.md#ga226e23a6bb94beee690ff6e1cdfbab91)(node\_id, idx) |
|  | Get the base raw address of the register block at index `idx`. |
| #define | [DT\_REG\_ADDR\_RAW](group__devicetree-reg-prop.md#ga14ebfb75548e45279f3954a75a5f9ac1)(node\_id) |
|  | Get a node's (only) register block raw address. |
| #define | [DT\_REG\_ADDR\_BY\_IDX](group__devicetree-reg-prop.md#gac540b00bb12d0662f6aefe6ac0cff243)(node\_id, idx) |
|  | Get the base address of the register block at index `idx`. |
| #define | [DT\_REG\_SIZE\_BY\_IDX](group__devicetree-reg-prop.md#ga9a703d688e4b983689b8579e0e7d9f48)(node\_id, idx) |
|  | Get the size of the register block at index `idx`. |
| #define | [DT\_REG\_ADDR](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e)(node\_id) |
|  | Get a node's (only) register block address. |
| #define | [DT\_REG\_ADDR\_U64](group__devicetree-reg-prop.md#gaf77354db552821a865b93f709b25e410)(node\_id) |
|  | 64-bit version of [DT\_REG\_ADDR()](group__devicetree-reg-prop.md#gac6d8279c32351ced4c0ac7f32270974e "Get a node's (only) register block address.") |
| #define | [DT\_REG\_SIZE](group__devicetree-reg-prop.md#gad223efc6c77d008e55c3588953e85bfb)(node\_id) |
|  | Get a node's (only) register block size. |
| #define | [DT\_REG\_ADDR\_BY\_NAME](group__devicetree-reg-prop.md#gaeb5863e878bbd3a362e17616403da692)(node\_id, name) |
|  | Get a register block's base address by name. |
| #define | [DT\_REG\_ADDR\_BY\_NAME\_OR](group__devicetree-reg-prop.md#ga3f0a35f6b07da983be6fa63bdfb82732)(node\_id, name, default\_value) |
|  | Like [DT\_REG\_ADDR\_BY\_NAME()](group__devicetree-reg-prop.md#gaeb5863e878bbd3a362e17616403da692 "Get a register block's base address by name."), but with a fallback to `default_value`. |
| #define | [DT\_REG\_ADDR\_BY\_NAME\_U64](group__devicetree-reg-prop.md#gaf03f1b5518ff146d6de986f867fcc2c8)(node\_id, name) |
|  | 64-bit version of [DT\_REG\_ADDR\_BY\_NAME()](group__devicetree-reg-prop.md#gaeb5863e878bbd3a362e17616403da692 "Get a register block's base address by name.") |
| #define | [DT\_REG\_SIZE\_BY\_NAME](group__devicetree-reg-prop.md#ga042988feb27e58989baa7abb4930409e)(node\_id, name) |
|  | Get a register block's size by name. |
| #define | [DT\_REG\_SIZE\_BY\_NAME\_OR](group__devicetree-reg-prop.md#ga823daf216d17b80f4d049c75358078ed)(node\_id, name, default\_value) |
|  | Like [DT\_REG\_SIZE\_BY\_NAME()](group__devicetree-reg-prop.md#ga042988feb27e58989baa7abb4930409e "Get a register block's size by name."), but with a fallback to `default_value`. |
| #define | [DT\_NUM\_IRQS](group__devicetree-interrupts-prop.md#ga2985e5d55d2d9dbbbe93ba855d5db320)(node\_id) |
|  | Get the number of interrupt sources for the node. |
| #define | [DT\_NUM\_NODELABELS](group__devicetree-interrupts-prop.md#ga7b63eb05db40d7b95ccb62a9fd1f4404)(node\_id) |
|  | Get the number of node labels that a node has. |
| #define | [DT\_IRQ\_LEVEL](group__devicetree-interrupts-prop.md#ga4b6c7ad21691c40047373e5073e740c9)(node\_id) |
|  | Get the interrupt level for the node. |
| #define | [DT\_IRQ\_HAS\_IDX](group__devicetree-interrupts-prop.md#ga238a290dc6cea9479104ff8f95de1c4c)(node\_id, idx) |
|  | Is `idx` a valid interrupt index? |
| #define | [DT\_IRQ\_HAS\_CELL\_AT\_IDX](group__devicetree-interrupts-prop.md#ga739ebdd4bd01d6b7beb75d915174206f)(node\_id, idx, cell) |
|  | Does an interrupts property have a named cell specifier at an index? |
| #define | [DT\_IRQ\_HAS\_CELL](group__devicetree-interrupts-prop.md#gab9c94ee39db7913598a755c6172fe036)(node\_id, cell) |
|  | Equivalent to [DT\_IRQ\_HAS\_CELL\_AT\_IDX(node\_id, 0, cell)](group__devicetree-interrupts-prop.md#ga739ebdd4bd01d6b7beb75d915174206f "Does an interrupts property have a named cell specifier at an index?"). |
| #define | [DT\_IRQ\_HAS\_NAME](group__devicetree-interrupts-prop.md#ga1c757ff5e4d15f1b3020b30f72c0dd5d)(node\_id, name) |
|  | Does an interrupts property have a named specifier value at an index? |
| #define | [DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)(node\_id, idx, cell) |
|  | Get a value within an interrupt specifier at an index. |
| #define | [DT\_IRQ\_BY\_NAME](group__devicetree-interrupts-prop.md#ga904917c0a407343ef0185e9e6fe96812)(node\_id, name, cell) |
|  | Get a value within an interrupt specifier by name. |
| #define | [DT\_IRQ](group__devicetree-interrupts-prop.md#gabf60fbd528d300a26c0b4e66fe80a53f)(node\_id, cell) |
|  | Get an interrupt specifier's value Equivalent to [DT\_IRQ\_BY\_IDX(node\_id, 0, cell)](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f "Get a value within an interrupt specifier at an index."). |
| #define | [DT\_IRQ\_INTC\_BY\_IDX](group__devicetree-interrupts-prop.md#ga061a34529fb2bbac9fe8615056d71ea4)(node\_id, idx) |
|  | Get an interrupt specifier's interrupt controller by index. |
| #define | [DT\_IRQ\_INTC\_BY\_NAME](group__devicetree-interrupts-prop.md#gabee933352a948bd824beccc00c13387d)(node\_id, name) |
|  | Get an interrupt specifier's interrupt controller by name. |
| #define | [DT\_IRQ\_INTC](group__devicetree-interrupts-prop.md#ga11d2680614de65fd8cb4a3909e93e9c9)(node\_id) |
|  | Get an interrupt specifier's interrupt controller. |
| #define | [DT\_IRQN\_BY\_IDX](group__devicetree-interrupts-prop.md#gaad6d6b27ea731a05a186a5dde8757698)(node\_id, idx) |
|  | Get the node's Zephyr interrupt number at index If `CONFIG_MULTI_LEVEL_INTERRUPTS` is enabled, the interrupt number at index will be multi-level encoded. |
| #define | [DT\_IRQN](group__devicetree-interrupts-prop.md#ga5e00c208388736ce9b5bc0088a77cd95)(node\_id) |
|  | Get a node's (only) irq number. |
| #define | [DT\_CHOSEN](group__devicetree-generic-chosen.md#ga3412d0acecffa828984cf9e2c89889ed)(prop) |
|  | Get a node identifier for a /chosen node property. |
| #define | [DT\_HAS\_CHOSEN](group__devicetree-generic-chosen.md#ga9df6bacab5f579284f5f3c1e4856cd15)(prop) |
|  | Test if the devicetree has a /chosen node. |
| #define | [DT\_FOREACH\_NODE](group__devicetree-generic-foreach.md#gad27b29ae71a3d3294984fd3bc721121d)(fn) |
|  | Invokes `fn` for every node in the tree. |
| #define | [DT\_FOREACH\_NODE\_VARGS](group__devicetree-generic-foreach.md#ga4e708120bf839568b1215a6c21c54eed)(fn, ...) |
|  | Invokes `fn` for every node in the tree with multiple arguments. |
| #define | [DT\_FOREACH\_STATUS\_OKAY\_NODE](group__devicetree-generic-foreach.md#ga926f68202042c9db05390e628787f916)(fn) |
|  | Invokes `fn` for every status okay node in the tree. |
| #define | [DT\_FOREACH\_STATUS\_OKAY\_NODE\_VARGS](group__devicetree-generic-foreach.md#ga9aa3ee2b90a4ec30621597f4d1448c51)(fn, ...) |
|  | Invokes `fn` for every status okay node in the tree with multiple arguments. |
| #define | [DT\_FOREACH\_ANCESTOR](group__devicetree-generic-foreach.md#gac4f9fee38bffbd5d315d386fe3c7bc91)(node\_id, fn) |
|  | Invokes `fn` for each ancestor of `node_id`. |
| #define | [DT\_FOREACH\_CHILD](group__devicetree-generic-foreach.md#ga2f4eead8e8190110f5c0eb353e6a408f)(node\_id, fn) |
|  | Invokes `fn` for each child of `node_id`. |
| #define | [DT\_FOREACH\_CHILD\_SEP](group__devicetree-generic-foreach.md#ga1fbeb335d66745803dbf7a185bf10afc)(node\_id, fn, sep) |
|  | Invokes `fn` for each child of `node_id` with a separator. |
| #define | [DT\_FOREACH\_CHILD\_VARGS](group__devicetree-generic-foreach.md#gae7461e9fa4687bf88cdd7c76f30986de)(node\_id, fn, ...) |
|  | Invokes `fn` for each child of `node_id` with multiple arguments. |
| #define | [DT\_FOREACH\_CHILD\_SEP\_VARGS](group__devicetree-generic-foreach.md#ga0042485aef7caaa48fa252b76a6629aa)(node\_id, fn, sep, ...) |
|  | Invokes `fn` for each child of `node_id` with separator and multiple arguments. |
| #define | [DT\_FOREACH\_CHILD\_STATUS\_OKAY](group__devicetree-generic-foreach.md#gae907df926b94f1da52b1ab701392f3bd)(node\_id, fn) |
|  | Call `fn` on the child nodes with status okay. |
| #define | [DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP](group__devicetree-generic-foreach.md#ga97414c01ebbb6df5ee2862c0ee9d44ce)(node\_id, fn, sep) |
|  | Call `fn` on the child nodes with status okay with separator. |
| #define | [DT\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS](group__devicetree-generic-foreach.md#ga8bbf6992e5f90d8a28035ea6211dd2a3)(node\_id, fn, ...) |
|  | Call `fn` on the child nodes with status okay with multiple arguments. |
| #define | [DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS](group__devicetree-generic-foreach.md#gaf46c1ac296f0d6c9388c3ca6fb4ca5cd)(node\_id, fn, sep, ...) |
|  | Call `fn` on the child nodes with status okay with separator and multiple arguments. |
| #define | [DT\_FOREACH\_PROP\_ELEM](group__devicetree-generic-foreach.md#ga118a0477ab297a1bda9e16acf556babc)(node\_id, prop, fn) |
|  | Invokes `fn` for each element in the value of property `prop`. |
| #define | [DT\_FOREACH\_PROP\_ELEM\_SEP](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)(node\_id, prop, fn, sep) |
|  | Invokes `fn` for each element in the value of property `prop` with separator. |
| #define | [DT\_FOREACH\_PROP\_ELEM\_VARGS](group__devicetree-generic-foreach.md#gaae36970d49c860414374c76e136a9607)(node\_id, prop, fn, ...) |
|  | Invokes `fn` for each element in the value of property `prop` with multiple arguments. |
| #define | [DT\_FOREACH\_PROP\_ELEM\_SEP\_VARGS](group__devicetree-generic-foreach.md#ga29120ee8718b889273dc2649ab25438f)(node\_id, prop, fn, sep, ...) |
|  | Invokes `fn` for each element in the value of property `prop` with multiple arguments and a separator. |
| #define | [DT\_FOREACH\_STATUS\_OKAY](group__devicetree-generic-foreach.md#ga52b34316d269cc8d8ef2244d3ca460b8)(compat, fn) |
|  | Invokes `fn` for each status okay node of a compatible. |
| #define | [DT\_FOREACH\_STATUS\_OKAY\_VARGS](group__devicetree-generic-foreach.md#ga99cf30d6cf4847ed99ba7d81ad2b49d0)(compat, fn, ...) |
|  | Invokes `fn` for each status okay node of a compatible with multiple arguments. |
| #define | [DT\_COMPAT\_FOREACH\_STATUS\_OKAY\_VARGS](group__devicetree-generic-foreach.md#ga368d08572b01efacdad370e6ceb515f9)(compat, fn, ...) |
|  | Call `fn` on all nodes with compatible compat and status okay with multiple arguments. |
| #define | [DT\_FOREACH\_NODELABEL](group__devicetree-generic-foreach.md#gad5585436896efc4c5154a93b5980d3b0)(node\_id, fn) |
|  | Invokes `fn` for each node label of a given node. |
| #define | [DT\_FOREACH\_NODELABEL\_VARGS](group__devicetree-generic-foreach.md#ga2a88abdb46158bcf36a8c976a1e2186d)(node\_id, fn, ...) |
|  | Invokes `fn` for each node label of a given node with multiple arguments. |
| #define | [DT\_NODE\_EXISTS](group__devicetree-generic-exist.md#ga9d5cf40051d042b853f6b0088fd4500a)(node\_id) |
|  | Does a node identifier refer to a node? |
| #define | [DT\_NODE\_HAS\_STATUS](group__devicetree-generic-exist.md#ga3b769d8105c7679e1d0575a1e7f1f653)(node\_id, status) |
|  | Does a node identifier refer to a node with a status? |
| #define | [DT\_NODE\_HAS\_STATUS\_OKAY](group__devicetree-generic-exist.md#gaed773a8782fe00db90e8599ff673e8ed)(node\_id) |
|  | Does a node identifier refer to a node with a status okay? |
| #define | [DT\_HAS\_COMPAT\_STATUS\_OKAY](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)(compat) |
|  | Does the devicetree have a status okay node with a compatible? |
| #define | [DT\_NUM\_INST\_STATUS\_OKAY](group__devicetree-generic-exist.md#ga45c268d7f0d604a72dc0bcf5cd0733b0)(compat) |
|  | Get the number of instances of a given compatible with status okay. |
| #define | [DT\_NODE\_HAS\_COMPAT](group__devicetree-generic-exist.md#gad8912ba5db980713e72257472ded3ced)(node\_id, compat) |
|  | Does a devicetree node match a compatible? |
| #define | [DT\_NODE\_HAS\_COMPAT\_STATUS](group__devicetree-generic-exist.md#ga9bf6258fbeb0c5cd1fd15b9c9be9228a)(node\_id, compat, status) |
|  | Does a devicetree node have a compatible and status? |
| #define | [DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, prop) |
|  | Does a devicetree node have a property? |
| #define | [DT\_PHA\_HAS\_CELL\_AT\_IDX](group__devicetree-generic-exist.md#gacfbd6a2cb3038e5aba1e2216d65ebc78)(node\_id, pha, idx, cell) |
|  | Does a phandle array have a named cell specifier at an index? |
| #define | [DT\_PHA\_HAS\_CELL](group__devicetree-generic-exist.md#gaece280102681cbadf318c5dabfb3d719)(node\_id, pha, cell) |
|  | Equivalent to [DT\_PHA\_HAS\_CELL\_AT\_IDX(node\_id, pha, 0, cell)](group__devicetree-generic-exist.md#gacfbd6a2cb3038e5aba1e2216d65ebc78 "Does a phandle array have a named cell specifier at an index?"). |
| #define | [DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)(node\_id) |
|  | Node's bus controller. |
| #define | [DT\_ON\_BUS](group__devicetree-generic-bus.md#gabe5eea44ff838c11dc5b75f9ec2a9317)(node\_id, bus) |
|  | Is a node on a bus of a given type? |
| #define | [DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst) |
|  | Node identifier for an instance of a DT\_DRV\_COMPAT compatible. |
| #define | [DT\_INST\_PARENT](group__devicetree-inst.md#ga176760ce1a019020b5465eebd4f44ff5)(inst) |
|  | Get a DT\_DRV\_COMPAT parent's node identifier. |
| #define | [DT\_INST\_GPARENT](group__devicetree-inst.md#ga5c68d697534682988a51a343abed05c9)(inst) |
|  | Get a DT\_DRV\_COMPAT grandparent's node identifier. |
| #define | [DT\_INST\_CHILD](group__devicetree-inst.md#gaaa4bfec30b277e0a8e2b0285a988d61d)(inst, child) |
|  | Get a node identifier for a child node of [DT\_DRV\_INST(inst)](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1 "Node identifier for an instance of a DT_DRV_COMPAT compatible."). |
| #define | [DT\_INST\_CHILD\_NUM](group__devicetree-inst.md#ga49e2e39f4d93956217584df40316290b)(inst) |
|  | Get the number of child nodes of a given node. |
| #define | [DT\_INST\_CHILD\_NUM\_STATUS\_OKAY](group__devicetree-inst.md#ga1a54403986077e46684c5198f4d53421)(inst) |
|  | Get the number of child nodes of a given node. |
| #define | [DT\_INST\_NODELABEL\_STRING\_ARRAY](group__devicetree-inst.md#gaabb1a53b444221d82d865ec8d23c8278)(inst) |
|  | Get a string array of [DT\_DRV\_INST(inst)](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1 "Node identifier for an instance of a DT_DRV_COMPAT compatible.")'s node labels. |
| #define | [DT\_INST\_NUM\_NODELABELS](group__devicetree-inst.md#ga2c43ec7309f5cdf8139a8b5fab63f786)(inst) |
|  | Get the number of node labels by instance number. |
| #define | [DT\_INST\_FOREACH\_CHILD](group__devicetree-inst.md#ga98f3fccc6f3004f72c3602a5f2b3a08e)(inst, fn) |
|  | Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1 "Node identifier for an instance of a DT_DRV_COMPAT compatible."). |
| #define | [DT\_INST\_FOREACH\_CHILD\_SEP](group__devicetree-inst.md#gae8d01eb2d6a576246f225a5cbbec34e5)(inst, fn, sep) |
|  | Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1 "Node identifier for an instance of a DT_DRV_COMPAT compatible.") with a separator. |
| #define | [DT\_INST\_FOREACH\_CHILD\_VARGS](group__devicetree-inst.md#ga455cb42d31b575d79f8cbbebbd353651)(inst, fn, ...) |
|  | Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1 "Node identifier for an instance of a DT_DRV_COMPAT compatible."). |
| #define | [DT\_INST\_FOREACH\_CHILD\_SEP\_VARGS](group__devicetree-inst.md#gac70fcf3052d9dfa949d7e197fece1413)(inst, fn, sep, ...) |
|  | Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1 "Node identifier for an instance of a DT_DRV_COMPAT compatible.") with separator. |
| #define | [DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY](group__devicetree-inst.md#gad416dd269b1af1e392ef81397b9bc814)(inst, fn) |
|  | Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1 "Node identifier for an instance of a DT_DRV_COMPAT compatible.") with status okay. |
| #define | [DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP](group__devicetree-inst.md#gae28554827ab7aaac3578ef07747a589d)(inst, fn, sep) |
|  | Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1 "Node identifier for an instance of a DT_DRV_COMPAT compatible.") with status okay and with separator. |
| #define | [DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS](group__devicetree-inst.md#gac6dd19b2b6e603c11701cd07daec73d3)(inst, fn, ...) |
|  | Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1 "Node identifier for an instance of a DT_DRV_COMPAT compatible.") with status okay and multiple arguments. |
| #define | [DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS](group__devicetree-inst.md#ga236cca0984f1c701c9b4855111c6cb29)(inst, fn, sep, ...) |
|  | Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1 "Node identifier for an instance of a DT_DRV_COMPAT compatible.") with status okay and with separator and multiple arguments. |
| #define | [DT\_INST\_ENUM\_IDX\_BY\_IDX](group__devicetree-inst.md#ga9de99aff4800b0f6f461fdb48bcc3969)(inst, prop, idx) |
|  | Get a DT\_DRV\_COMPAT property array value's index into its enumeration values. |
| #define | [DT\_INST\_ENUM\_IDX](group__devicetree-inst.md#ga866d6c28eb7a72ba9831c7ee1ecb98d2)(inst, prop) |
|  | Get a DT\_DRV\_COMPAT value's index into its enumeration values. |
| #define | [DT\_INST\_ENUM\_IDX\_BY\_IDX\_OR](group__devicetree-inst.md#ga48315c386a33d9384078c4a4fcccfd5d)(inst, prop, idx, default\_idx\_value) |
|  | Like [DT\_INST\_ENUM\_IDX\_BY\_IDX()](group__devicetree-inst.md#ga9de99aff4800b0f6f461fdb48bcc3969 "Get a DT_DRV_COMPAT property array value's index into its enumeration values."), but with a fallback to a default enum index. |
| #define | [DT\_INST\_ENUM\_IDX\_OR](group__devicetree-inst.md#gafbf64148f9171ffd322f7689297e0da8)(inst, prop, default\_idx\_value) |
|  | Like [DT\_INST\_ENUM\_IDX()](group__devicetree-inst.md#ga866d6c28eb7a72ba9831c7ee1ecb98d2 "Get a DT_DRV_COMPAT value's index into its enumeration values."), but with a fallback to a default enum index. |
| #define | [DT\_INST\_ENUM\_HAS\_VALUE\_BY\_IDX](group__devicetree-inst.md#ga5057571e3996451258ae5c29a06d9ede)(inst, prop, idx, value) |
|  | Does a DT\_DRV\_COMPAT enumeration property have a given value by index? |
| #define | [DT\_INST\_ENUM\_HAS\_VALUE](group__devicetree-inst.md#ga80b0321efd592a63e39400e5327bb601)(inst, prop, value) |
|  | Does a DT\_DRV\_COMPAT enumeration property have a given value? |
| #define | [DT\_INST\_PROP](group__devicetree-inst.md#ga9dce2e631b2a94804e8f2bcc76c6eff8)(inst, prop) |
|  | Get a DT\_DRV\_COMPAT instance property. |
| #define | [DT\_INST\_PROP\_LEN](group__devicetree-inst.md#ga9471df75ff3c4f8d2298bb69c581b365)(inst, prop) |
|  | Get a DT\_DRV\_COMPAT property length. |
| #define | [DT\_INST\_PROP\_HAS\_IDX](group__devicetree-inst.md#ga2c51745f8d51b1d9cdfb1cde69911d48)(inst, prop, idx) |
|  | Is index `idx` valid for an array type property on a DT\_DRV\_COMPAT instance? |
| #define | [DT\_INST\_PROP\_HAS\_NAME](group__devicetree-inst.md#ga75e13dcdbcc51da1334fa14653411dd8)(inst, prop, name) |
|  | Is name `name` available in a foo-names property? |
| #define | [DT\_INST\_PROP\_BY\_IDX](group__devicetree-inst.md#ga5b60f4ed4f5dadc5dd425f5905f23b00)(inst, prop, idx) |
|  | Get a DT\_DRV\_COMPAT element value in an array property. |
| #define | [DT\_INST\_PROP\_OR](group__devicetree-inst.md#gaa51bd8f5b016244e0256b3ed9aceee7f)(inst, prop, default\_value) |
|  | Like [DT\_INST\_PROP()](group__devicetree-inst.md#ga9dce2e631b2a94804e8f2bcc76c6eff8 "Get a DT_DRV_COMPAT instance property."), but with a fallback to `default_value`. |
| #define | [DT\_INST\_PROP\_LEN\_OR](group__devicetree-inst.md#ga9be8fdcc8c4032748b47f497efa19173)(inst, prop, default\_value) |
|  | Like [DT\_INST\_PROP\_LEN()](group__devicetree-inst.md#ga9471df75ff3c4f8d2298bb69c581b365 "Get a DT_DRV_COMPAT property length."), but with a fallback to `default_value`. |
| #define | [DT\_INST\_STRING\_TOKEN](group__devicetree-inst.md#ga8e8c72187ce0d47fd24e4585f3d48484)(inst, prop) |
|  | Get a DT\_DRV\_COMPAT instance's string property's value as a token. |
| #define | [DT\_INST\_STRING\_UPPER\_TOKEN](group__devicetree-inst.md#ga0487d19ae023acb9b0eb613317f31aa5)(inst, prop) |
|  | Like [DT\_INST\_STRING\_TOKEN()](group__devicetree-inst.md#ga8e8c72187ce0d47fd24e4585f3d48484 "Get a DT_DRV_COMPAT instance's string property's value as a token."), but uppercased. |
| #define | [DT\_INST\_STRING\_UNQUOTED](group__devicetree-inst.md#ga1c4fc4c808113cb6e0d7b54af9869228)(inst, prop) |
|  | Get a DT\_DRV\_COMPAT instance's string property's value as an unquoted sequence of tokens. |
| #define | [DT\_INST\_STRING\_TOKEN\_BY\_IDX](group__devicetree-inst.md#gae1c28cbd9c1869112d2ae5c7ddf00b97)(inst, prop, idx) |
|  | Get an element out of string-array property as a token. |
| #define | [DT\_INST\_STRING\_UPPER\_TOKEN\_BY\_IDX](group__devicetree-inst.md#ga4ceceec8375d70b40a4dec1a8ab5ee29)(inst, prop, idx) |
|  | Like [DT\_INST\_STRING\_TOKEN\_BY\_IDX()](group__devicetree-inst.md#gae1c28cbd9c1869112d2ae5c7ddf00b97 "Get an element out of string-array property as a token."), but uppercased. |
| #define | [DT\_INST\_STRING\_UNQUOTED\_BY\_IDX](group__devicetree-inst.md#gac5768077e2a3d14a69efc653cfc59d5d)(inst, prop, idx) |
|  | Get an element out of string-array property as an unquoted sequence of tokens. |
| #define | [DT\_INST\_PROP\_BY\_PHANDLE](group__devicetree-inst.md#ga1f26b1c5b6c7a8c3c02c09d72a00afa5)(inst, ph, prop) |
|  | Get a DT\_DRV\_COMPAT instance's property value from a phandle's node. |
| #define | [DT\_INST\_PROP\_BY\_PHANDLE\_IDX](group__devicetree-inst.md#gad027963bdf159942cf6fb28b04e8d48e)(inst, phs, idx, prop) |
|  | Get a DT\_DRV\_COMPAT instance's property value from a phandle in a property. |
| #define | [DT\_INST\_PHA\_BY\_IDX](group__devicetree-inst.md#gaac886e11906d628acad1d73ed3a64018)(inst, pha, idx, cell) |
|  | Get a DT\_DRV\_COMPAT instance's phandle-array specifier value at an index. |
| #define | [DT\_INST\_PHA\_BY\_IDX\_OR](group__devicetree-inst.md#ga3db4c00e072bd93fa92e36907b2b5e86)(inst, pha, idx, cell, default\_value) |
|  | Like [DT\_INST\_PHA\_BY\_IDX()](group__devicetree-inst.md#gaac886e11906d628acad1d73ed3a64018 "Get a DT_DRV_COMPAT instance's phandle-array specifier value at an index."), but with a fallback to default\_value. |
| #define | [DT\_INST\_PHA](group__devicetree-inst.md#ga0de189f14fa7dd38a99382b7f2adbff8)(inst, pha, cell) |
|  | Get a DT\_DRV\_COMPAT instance's phandle-array specifier value Equivalent to [DT\_INST\_PHA\_BY\_IDX(inst, pha, 0, cell)](group__devicetree-inst.md#gaac886e11906d628acad1d73ed3a64018 "Get a DT_DRV_COMPAT instance's phandle-array specifier value at an index."). |
| #define | [DT\_INST\_PHA\_OR](group__devicetree-inst.md#ga491ad421602e41c4295bac61b595fc94)(inst, pha, cell, default\_value) |
|  | Like [DT\_INST\_PHA()](group__devicetree-inst.md#ga0de189f14fa7dd38a99382b7f2adbff8 "Get a DT_DRV_COMPAT instance's phandle-array specifier value Equivalent to DT_INST_PHA_BY_IDX(inst,..."), but with a fallback to default\_value. |
| #define | [DT\_INST\_PHA\_BY\_NAME](group__devicetree-inst.md#ga25418914c5190df10c842744aa967dc8)(inst, pha, name, cell) |
|  | Get a DT\_DRV\_COMPAT instance's value within a phandle-array specifier by name. |
| #define | [DT\_INST\_PHA\_BY\_NAME\_OR](group__devicetree-inst.md#gaaebc5c643b60319f7e767e46ca226729)(inst, pha, name, cell, default\_value) |
|  | Like [DT\_INST\_PHA\_BY\_NAME()](group__devicetree-inst.md#ga25418914c5190df10c842744aa967dc8 "Get a DT_DRV_COMPAT instance's value within a phandle-array specifier by name."), but with a fallback to default\_value. |
| #define | [DT\_INST\_PHANDLE\_BY\_NAME](group__devicetree-inst.md#ga64d8ddaad8b2d3852e30686d3adf6551)(inst, pha, name) |
|  | Get a DT\_DRV\_COMPAT instance's phandle node identifier from a phandle array by name. |
| #define | [DT\_INST\_PHANDLE\_BY\_IDX](group__devicetree-inst.md#ga10d93a1f9a9f5e225508c4c383654b1c)(inst, prop, idx) |
|  | Get a DT\_DRV\_COMPAT instance's node identifier for a phandle in a property. |
| #define | [DT\_INST\_PHANDLE](group__devicetree-inst.md#ga81c10f478c86e5a4c18eb7a990447137)(inst, prop) |
|  | Get a DT\_DRV\_COMPAT instance's node identifier for a phandle property's value. |
| #define | [DT\_INST\_REG\_HAS\_IDX](group__devicetree-inst.md#ga26bbff9ebaed549140d2530a0b99e8a4)(inst, idx) |
|  | is `idx` a valid register block index on a DT\_DRV\_COMPAT instance? |
| #define | [DT\_INST\_REG\_HAS\_NAME](group__devicetree-inst.md#ga8b15b84b03c3dc6fd9d7e127a44392b3)(inst, name) |
|  | is `name` a valid register block name on a DT\_DRV\_COMPAT instance? |
| #define | [DT\_INST\_REG\_ADDR\_BY\_IDX\_RAW](group__devicetree-inst.md#gade870f8f5c78c3c6244ada35049334a5)(inst, idx) |
|  | Get a DT\_DRV\_COMPAT instance's idx-th register block's raw address. |
| #define | [DT\_INST\_REG\_ADDR\_BY\_IDX](group__devicetree-inst.md#ga0fe0403821883598da6cfad4f3962115)(inst, idx) |
|  | Get a DT\_DRV\_COMPAT instance's idx-th register block's address. |
| #define | [DT\_INST\_REG\_SIZE\_BY\_IDX](group__devicetree-inst.md#gab1152c9f069c69b0269c1a4e744b9dd9)(inst, idx) |
|  | Get a DT\_DRV\_COMPAT instance's idx-th register block's size. |
| #define | [DT\_INST\_REG\_ADDR\_BY\_NAME](group__devicetree-inst.md#ga722d6f7b97136aa9229242e4ba7dd25c)(inst, name) |
|  | Get a DT\_DRV\_COMPAT's register block address by name. |
| #define | [DT\_INST\_REG\_ADDR\_BY\_NAME\_OR](group__devicetree-inst.md#gaf8d6ec7f68f566360743f7ea7cb7f8fb)(inst, name, default\_value) |
|  | Like [DT\_INST\_REG\_ADDR\_BY\_NAME()](group__devicetree-inst.md#ga722d6f7b97136aa9229242e4ba7dd25c "Get a DT_DRV_COMPAT's register block address by name."), but with a fallback to `default_value`. |
| #define | [DT\_INST\_REG\_ADDR\_BY\_NAME\_U64](group__devicetree-inst.md#ga8af83c4c65e607b93aa60a690295d625)(inst, name) |
|  | 64-bit version of [DT\_INST\_REG\_ADDR\_BY\_NAME()](group__devicetree-inst.md#ga722d6f7b97136aa9229242e4ba7dd25c "Get a DT_DRV_COMPAT's register block address by name.") |
| #define | [DT\_INST\_REG\_SIZE\_BY\_NAME](group__devicetree-inst.md#gaf82457c5dcfef7eeba074afb95d48714)(inst, name) |
|  | Get a DT\_DRV\_COMPAT's register block size by name. |
| #define | [DT\_INST\_REG\_SIZE\_BY\_NAME\_OR](group__devicetree-inst.md#ga8494b94b6dbec875eba61e10f269cce6)(inst, name, default\_value) |
|  | Like [DT\_INST\_REG\_SIZE\_BY\_NAME()](group__devicetree-inst.md#gaf82457c5dcfef7eeba074afb95d48714 "Get a DT_DRV_COMPAT's register block size by name."), but with a fallback to `default_value`. |
| #define | [DT\_INST\_REG\_ADDR\_RAW](group__devicetree-inst.md#ga79627566ff2486cfd2425a04974d71a3)(inst) |
|  | Get a DT\_DRV\_COMPAT's (only) register block raw address. |
| #define | [DT\_INST\_REG\_ADDR](group__devicetree-inst.md#gafde8fa67b94ac959ba2e24b44b3386a7)(inst) |
|  | Get a DT\_DRV\_COMPAT's (only) register block address. |
| #define | [DT\_INST\_REG\_ADDR\_U64](group__devicetree-inst.md#gaba47dcabd8754eda87e35efd7289f976)(inst) |
|  | 64-bit version of [DT\_INST\_REG\_ADDR()](group__devicetree-inst.md#gafde8fa67b94ac959ba2e24b44b3386a7 "Get a DT_DRV_COMPAT's (only) register block address.") |
| #define | [DT\_INST\_REG\_SIZE](group__devicetree-inst.md#gaa7cea29435e1db59470302abb5ee88dd)(inst) |
|  | Get a DT\_DRV\_COMPAT's (only) register block size. |
| #define | [DT\_INST\_NUM\_IRQS](group__devicetree-inst.md#ga446d4b9c267e7c9da73dfb8a07701f2a)(inst) |
|  | Get a DT\_DRV\_COMPAT's number of interrupts. |
| #define | [DT\_INST\_IRQ\_LEVEL](group__devicetree-inst.md#ga5c06043fd17c891e2cbbe0508248b638)(inst) |
|  | Get a DT\_DRV\_COMPAT interrupt level. |
| #define | [DT\_INST\_IRQ\_BY\_IDX](group__devicetree-inst.md#gad0d69a61ad842aa1dc3a5d4a304c3f2f)(inst, idx, cell) |
|  | Get a DT\_DRV\_COMPAT interrupt specifier value at an index. |
| #define | [DT\_INST\_IRQ\_INTC\_BY\_IDX](group__devicetree-inst.md#gab29f18e52d7475245c9fbeb4cd8e7769)(inst, idx) |
|  | Get a DT\_DRV\_COMPAT interrupt specifier's interrupt controller by index. |
| #define | [DT\_INST\_IRQ\_INTC\_BY\_NAME](group__devicetree-inst.md#gadd0f339e10b071da34d44922ad0c7bfd)(inst, name) |
|  | Get a DT\_DRV\_COMPAT interrupt specifier's interrupt controller by name. |
| #define | [DT\_INST\_IRQ\_INTC](group__devicetree-inst.md#gabf127c8370af849d2b5560e87ee04809)(inst) |
|  | Get a DT\_DRV\_COMPAT interrupt specifier's interrupt controller. |
| #define | [DT\_INST\_IRQ\_BY\_NAME](group__devicetree-inst.md#ga1ff6f24f9c97d4b611e4bf50ce5175d3)(inst, name, cell) |
|  | Get a DT\_DRV\_COMPAT interrupt specifier value by name. |
| #define | [DT\_INST\_IRQ](group__devicetree-inst.md#ga789eb58422bab7b3a79b487c4a8a82d6)(inst, cell) |
|  | Get a DT\_DRV\_COMPAT interrupt specifier's value. |
| #define | [DT\_INST\_IRQN](group__devicetree-inst.md#ga4e5a5f20f5dd9ea4cfda61def2c16ed3)(inst) |
|  | Get a DT\_DRV\_COMPAT's (only) irq number. |
| #define | [DT\_INST\_IRQN\_BY\_IDX](group__devicetree-inst.md#gaeb0c023f53ed87a6707bbca8ba05ce45)(inst, idx) |
|  | Get a DT\_DRV\_COMPAT's irq number at index. |
| #define | [DT\_INST\_BUS](group__devicetree-inst.md#gacecb46743315738dcd9a0765ea78276a)(inst) |
|  | Get a DT\_DRV\_COMPAT's bus node identifier. |
| #define | [DT\_INST\_ON\_BUS](group__devicetree-inst.md#ga7a29bda946b399a7af92ec9cd09b4e98)(inst, bus) |
|  | Test if a DT\_DRV\_COMPAT's bus type is a given type. |
| #define | [DT\_INST\_STRING\_TOKEN\_OR](group__devicetree-inst.md#ga79fd00d1ece5538f7705c241ab869ea8)(inst, name, default\_value) |
|  | Like [DT\_INST\_STRING\_TOKEN()](group__devicetree-inst.md#ga8e8c72187ce0d47fd24e4585f3d48484 "Get a DT_DRV_COMPAT instance's string property's value as a token."), but with a fallback to `default_value`. |
| #define | [DT\_INST\_STRING\_UPPER\_TOKEN\_OR](group__devicetree-inst.md#ga72981780b2ede73c49ef9e5a7c6247c2)(inst, name, default\_value) |
|  | Like [DT\_INST\_STRING\_UPPER\_TOKEN()](group__devicetree-inst.md#ga0487d19ae023acb9b0eb613317f31aa5 "Like DT_INST_STRING_TOKEN(), but uppercased."), but with a fallback to `default_value`. |
| #define | [DT\_INST\_STRING\_UNQUOTED\_OR](group__devicetree-inst.md#ga56bc0c0a46f6be421082119604cde643)(inst, name, default\_value) |
|  | Like [DT\_INST\_STRING\_UNQUOTED()](group__devicetree-inst.md#ga1c4fc4c808113cb6e0d7b54af9869228 "Get a DT_DRV_COMPAT instance's string property's value as an unquoted sequence of tokens."), but with a fallback to `default_value`. |
| #define | [DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY](group__devicetree-inst.md#ga1727af4beed08b248a98ad68bc5f1027)(compat, bus) |
|  | Test if any enabled node with the given compatible is on the given bus type. |
| #define | [DT\_ANY\_INST\_ON\_BUS\_STATUS\_OKAY](group__devicetree-inst.md#gaa4ff1fe4242399fbd667fbee7e98040a)(bus) |
|  | Test if any DT\_DRV\_COMPAT node is on a bus of a given type and has status okay. |
| #define | [DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY](group__devicetree-inst.md#gaf2a45df474090b0403dffe1b7b82b735)(prop) |
|  | Check if any DT\_DRV\_COMPAT node with status okay has a given property. |
| #define | [DT\_ANY\_COMPAT\_HAS\_PROP\_STATUS\_OKAY](group__devicetree-inst.md#ga052727464d4f04768eaa71b7522c9a61)(compat, prop) |
|  | Check if any device node with status okay has a given property. |
| #define | [DT\_ANY\_INST\_HAS\_BOOL\_STATUS\_OKAY](group__devicetree-inst.md#gab3d2f48ad95c4e2af76eed5e34735b18)(prop) |
|  | Check if any DT\_DRV\_COMPAT node with status okay has a given boolean property that exists. |
| #define | [DT\_INST\_FOREACH\_STATUS\_OKAY](group__devicetree-inst.md#gaeac7ed0f4a6820a6e5d7dadb6d62d6e7)(fn) |
|  | Call `fn` on all nodes with compatible DT\_DRV\_COMPAT and status okay. |
| #define | [DT\_INST\_FOREACH\_STATUS\_OKAY\_VARGS](group__devicetree-inst.md#ga1b9fd4b9c37a23e52e69ea23f7aedb38)(fn, ...) |
|  | Call `fn` on all nodes with compatible DT\_DRV\_COMPAT and status okay with multiple arguments. |
| #define | [DT\_INST\_FOREACH\_NODELABEL](group__devicetree-inst.md#gafd15350971dee495f955f2fcc7edd82c)(inst, fn) |
|  | Call `fn` on all node labels for a given DT\_DRV\_COMPAT instance. |
| #define | [DT\_INST\_FOREACH\_NODELABEL\_VARGS](group__devicetree-inst.md#ga3cf2a5bc8bad5ef8d47feb56c8215ca6)(inst, fn, ...) |
|  | Call `fn` on all node labels for a given DT\_DRV\_COMPAT instance with multiple arguments. |
| #define | [DT\_INST\_FOREACH\_PROP\_ELEM](group__devicetree-inst.md#gaf163f2f85b3893ca46c87f0fcbe65255)(inst, prop, fn) |
|  | Invokes `fn` for each element of property `prop` for a DT\_DRV\_COMPAT instance. |
| #define | [DT\_INST\_FOREACH\_PROP\_ELEM\_SEP](group__devicetree-inst.md#ga08de2f0ba1a6ec395f198e06c5f52373)(inst, prop, fn, sep) |
|  | Invokes `fn` for each element of property `prop` for a DT\_DRV\_COMPAT instance with a separator. |
| #define | [DT\_INST\_FOREACH\_PROP\_ELEM\_VARGS](group__devicetree-inst.md#ga31b9022f7add3d77417b78ed67d544e3)(inst, prop, fn, ...) |
|  | Invokes `fn` for each element of property `prop` for a DT\_DRV\_COMPAT instance with multiple arguments. |
| #define | [DT\_INST\_FOREACH\_PROP\_ELEM\_SEP\_VARGS](group__devicetree-inst.md#ga41b9dfd3519809bfc3c1c500780d6a2d)(inst, prop, fn, sep, ...) |
|  | Invokes `fn` for each element of property `prop` for a DT\_DRV\_COMPAT instance with multiple arguments and a separator. |
| #define | [DT\_INST\_NODE\_HAS\_PROP](group__devicetree-inst.md#gaa03419e2d9c887a81e16e96b5947bccb)(inst, prop) |
|  | Does a DT\_DRV\_COMPAT instance have a property? |
| #define | [DT\_INST\_NODE\_HAS\_COMPAT](group__devicetree-inst.md#gaf88c7dc0e935ad7097e317e54c362ba0)(inst, compat) |
|  | Does a DT\_DRV\_COMPAT instance have the compatible? |
| #define | [DT\_INST\_PHA\_HAS\_CELL\_AT\_IDX](group__devicetree-inst.md#gae054b89701ec9fae577320fb7b9cae1e)(inst, pha, idx, cell) |
|  | Does a phandle array have a named cell specifier at an index for a DT\_DRV\_COMPAT instance? |
| #define | [DT\_INST\_PHA\_HAS\_CELL](group__devicetree-inst.md#gab8083dae430aeb93a967bbf98aa9eefc)(inst, pha, cell) |
|  | Does a phandle array have a named cell specifier at index 0 for a DT\_DRV\_COMPAT instance? |
| #define | [DT\_INST\_IRQ\_HAS\_IDX](group__devicetree-inst.md#gabb45132ef78818512c02bdf1f5a38068)(inst, idx) |
|  | is index valid for interrupt property on a DT\_DRV\_COMPAT instance? |
| #define | [DT\_INST\_IRQ\_HAS\_CELL\_AT\_IDX](group__devicetree-inst.md#gab176ff07912cea915c811406e8f5e386)(inst, idx, cell) |
|  | Does a DT\_DRV\_COMPAT instance have an interrupt named cell specifier? |
| #define | [DT\_INST\_IRQ\_HAS\_CELL](group__devicetree-inst.md#gabec43df3451bd917120b283d76c57054)(inst, cell) |
|  | Does a DT\_DRV\_COMPAT instance have an interrupt value? |
| #define | [DT\_INST\_IRQ\_HAS\_NAME](group__devicetree-inst.md#gaa038ffc9b4f5c897a4a9e6d0e9836ffd)(inst, name) |
|  | Does a DT\_DRV\_COMPAT instance have an interrupt value? |

## Detailed Description

Devicetree main header.

API for accessing the current application's devicetree macros.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [devicetree.h](devicetree_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
