---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__devicetree-inst.html
original_path: doxygen/html/group__devicetree-inst.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Instance-based devicetree APIs

[Devicetree](group__devicetree.md)

| Macros | |
| --- | --- |
| #define | [DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst) |
|  | Node identifier for an instance of a DT\_DRV\_COMPAT compatible. |
| #define | [DT\_INST\_PARENT](#ga176760ce1a019020b5465eebd4f44ff5)(inst) |
|  | Get a DT\_DRV\_COMPAT parent's node identifier. |
| #define | [DT\_INST\_GPARENT](#ga5c68d697534682988a51a343abed05c9)(inst) |
|  | Get a DT\_DRV\_COMPAT grandparent's node identifier. |
| #define | [DT\_INST\_CHILD](#gaaa4bfec30b277e0a8e2b0285a988d61d)(inst, child) |
|  | Get a node identifier for a child node of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1). |
| #define | [DT\_INST\_CHILD\_NUM](#ga49e2e39f4d93956217584df40316290b)(inst) |
|  | Get the number of child nodes of a given node. |
| #define | [DT\_INST\_CHILD\_NUM\_STATUS\_OKAY](#ga1a54403986077e46684c5198f4d53421)(inst) |
|  | Get the number of child nodes of a given node. |
| #define | [DT\_INST\_NODELABEL\_STRING\_ARRAY](#gaabb1a53b444221d82d865ec8d23c8278)(inst) |
|  | Get a string array of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1)'s node labels. |
| #define | [DT\_INST\_NUM\_NODELABELS](#ga2c43ec7309f5cdf8139a8b5fab63f786)(inst) |
|  | Get the number of node labels by instance number. |
| #define | [DT\_INST\_FOREACH\_CHILD](#ga98f3fccc6f3004f72c3602a5f2b3a08e)(inst, fn) |
|  | Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1). |
| #define | [DT\_INST\_FOREACH\_CHILD\_SEP](#gae8d01eb2d6a576246f225a5cbbec34e5)(inst, fn, sep) |
|  | Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1) with a separator. |
| #define | [DT\_INST\_FOREACH\_CHILD\_VARGS](#ga455cb42d31b575d79f8cbbebbd353651)(inst, fn, ...) |
|  | Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1). |
| #define | [DT\_INST\_FOREACH\_CHILD\_SEP\_VARGS](#gac70fcf3052d9dfa949d7e197fece1413)(inst, fn, sep, ...) |
|  | Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1) with separator. |
| #define | [DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY](#gad416dd269b1af1e392ef81397b9bc814)(inst, fn) |
|  | Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1) with status okay. |
| #define | [DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP](#gae28554827ab7aaac3578ef07747a589d)(inst, fn, sep) |
|  | Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1) with status okay and with separator. |
| #define | [DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS](#gac6dd19b2b6e603c11701cd07daec73d3)(inst, fn, ...) |
|  | Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1) with status okay and multiple arguments. |
| #define | [DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS](#ga236cca0984f1c701c9b4855111c6cb29)(inst, fn, sep, ...) |
|  | Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1) with status okay and with separator and multiple arguments. |
| #define | [DT\_INST\_ENUM\_IDX\_BY\_IDX](#ga9de99aff4800b0f6f461fdb48bcc3969)(inst, prop, idx) |
|  | Get a DT\_DRV\_COMPAT property array value's index into its enumeration values. |
| #define | [DT\_INST\_ENUM\_IDX](#ga866d6c28eb7a72ba9831c7ee1ecb98d2)(inst, prop) |
|  | Get a DT\_DRV\_COMPAT value's index into its enumeration values. |
| #define | [DT\_INST\_ENUM\_IDX\_BY\_IDX\_OR](#ga48315c386a33d9384078c4a4fcccfd5d)(inst, prop, idx, default\_idx\_value) |
|  | Like [DT\_INST\_ENUM\_IDX\_BY\_IDX()](#ga9de99aff4800b0f6f461fdb48bcc3969), but with a fallback to a default enum index. |
| #define | [DT\_INST\_ENUM\_IDX\_OR](#gafbf64148f9171ffd322f7689297e0da8)(inst, prop, default\_idx\_value) |
|  | Like [DT\_INST\_ENUM\_IDX()](#ga866d6c28eb7a72ba9831c7ee1ecb98d2), but with a fallback to a default enum index. |
| #define | [DT\_INST\_ENUM\_HAS\_VALUE\_BY\_IDX](#ga5057571e3996451258ae5c29a06d9ede)(inst, prop, idx, value) |
|  | Does a DT\_DRV\_COMPAT enumeration property have a given value by index? |
| #define | [DT\_INST\_ENUM\_HAS\_VALUE](#ga80b0321efd592a63e39400e5327bb601)(inst, prop, value) |
|  | Does a DT\_DRV\_COMPAT enumeration property have a given value? |
| #define | [DT\_INST\_PROP](#ga9dce2e631b2a94804e8f2bcc76c6eff8)(inst, prop) |
|  | Get a DT\_DRV\_COMPAT instance property. |
| #define | [DT\_INST\_PROP\_LEN](#ga9471df75ff3c4f8d2298bb69c581b365)(inst, prop) |
|  | Get a DT\_DRV\_COMPAT property length. |
| #define | [DT\_INST\_PROP\_HAS\_IDX](#ga2c51745f8d51b1d9cdfb1cde69911d48)(inst, prop, idx) |
|  | Is index `idx` valid for an array type property on a DT\_DRV\_COMPAT instance? |
| #define | [DT\_INST\_PROP\_HAS\_NAME](#ga75e13dcdbcc51da1334fa14653411dd8)(inst, prop, name) |
|  | Is name `name` available in a foo-names property? |
| #define | [DT\_INST\_PROP\_BY\_IDX](#ga5b60f4ed4f5dadc5dd425f5905f23b00)(inst, prop, idx) |
|  | Get a DT\_DRV\_COMPAT element value in an array property. |
| #define | [DT\_INST\_PROP\_OR](#gaa51bd8f5b016244e0256b3ed9aceee7f)(inst, prop, default\_value) |
|  | Like [DT\_INST\_PROP()](#ga9dce2e631b2a94804e8f2bcc76c6eff8), but with a fallback to `default_value`. |
| #define | [DT\_INST\_PROP\_LEN\_OR](#ga9be8fdcc8c4032748b47f497efa19173)(inst, prop, default\_value) |
|  | Like [DT\_INST\_PROP\_LEN()](#ga9471df75ff3c4f8d2298bb69c581b365), but with a fallback to `default_value`. |
| #define | [DT\_INST\_STRING\_TOKEN](#ga8e8c72187ce0d47fd24e4585f3d48484)(inst, prop) |
|  | Get a DT\_DRV\_COMPAT instance's string property's value as a token. |
| #define | [DT\_INST\_STRING\_UPPER\_TOKEN](#ga0487d19ae023acb9b0eb613317f31aa5)(inst, prop) |
|  | Like [DT\_INST\_STRING\_TOKEN()](#ga8e8c72187ce0d47fd24e4585f3d48484), but uppercased. |
| #define | [DT\_INST\_STRING\_UNQUOTED](#ga1c4fc4c808113cb6e0d7b54af9869228)(inst, prop) |
|  | Get a DT\_DRV\_COMPAT instance's string property's value as an unquoted sequence of tokens. |
| #define | [DT\_INST\_STRING\_TOKEN\_BY\_IDX](#gae1c28cbd9c1869112d2ae5c7ddf00b97)(inst, prop, idx) |
|  | Get an element out of string-array property as a token. |
| #define | [DT\_INST\_STRING\_UPPER\_TOKEN\_BY\_IDX](#ga4ceceec8375d70b40a4dec1a8ab5ee29)(inst, prop, idx) |
|  | Like [DT\_INST\_STRING\_TOKEN\_BY\_IDX()](#gae1c28cbd9c1869112d2ae5c7ddf00b97), but uppercased. |
| #define | [DT\_INST\_STRING\_UNQUOTED\_BY\_IDX](#gac5768077e2a3d14a69efc653cfc59d5d)(inst, prop, idx) |
|  | Get an element out of string-array property as an unquoted sequence of tokens. |
| #define | [DT\_INST\_PROP\_BY\_PHANDLE](#ga1f26b1c5b6c7a8c3c02c09d72a00afa5)(inst, ph, prop) |
|  | Get a DT\_DRV\_COMPAT instance's property value from a phandle's node. |
| #define | [DT\_INST\_PROP\_BY\_PHANDLE\_IDX](#gad027963bdf159942cf6fb28b04e8d48e)(inst, phs, idx, prop) |
|  | Get a DT\_DRV\_COMPAT instance's property value from a phandle in a property. |
| #define | [DT\_INST\_PHA\_BY\_IDX](#gaac886e11906d628acad1d73ed3a64018)(inst, pha, idx, cell) |
|  | Get a DT\_DRV\_COMPAT instance's phandle-array specifier value at an index. |
| #define | [DT\_INST\_PHA\_BY\_IDX\_OR](#ga3db4c00e072bd93fa92e36907b2b5e86)(inst, pha, idx, cell, default\_value) |
|  | Like [DT\_INST\_PHA\_BY\_IDX()](#gaac886e11906d628acad1d73ed3a64018), but with a fallback to default\_value. |
| #define | [DT\_INST\_PHA](#ga0de189f14fa7dd38a99382b7f2adbff8)(inst, pha, cell) |
|  | Get a DT\_DRV\_COMPAT instance's phandle-array specifier value Equivalent to [DT\_INST\_PHA\_BY\_IDX(inst, pha, 0, cell)](#gaac886e11906d628acad1d73ed3a64018). |
| #define | [DT\_INST\_PHA\_OR](#ga491ad421602e41c4295bac61b595fc94)(inst, pha, cell, default\_value) |
|  | Like [DT\_INST\_PHA()](#ga0de189f14fa7dd38a99382b7f2adbff8), but with a fallback to default\_value. |
| #define | [DT\_INST\_PHA\_BY\_NAME](#ga25418914c5190df10c842744aa967dc8)(inst, pha, name, cell) |
|  | Get a DT\_DRV\_COMPAT instance's value within a phandle-array specifier by name. |
| #define | [DT\_INST\_PHA\_BY\_NAME\_OR](#gaaebc5c643b60319f7e767e46ca226729)(inst, pha, name, cell, default\_value) |
|  | Like [DT\_INST\_PHA\_BY\_NAME()](#ga25418914c5190df10c842744aa967dc8), but with a fallback to default\_value. |
| #define | [DT\_INST\_PHANDLE\_BY\_NAME](#ga64d8ddaad8b2d3852e30686d3adf6551)(inst, pha, name) |
|  | Get a DT\_DRV\_COMPAT instance's phandle node identifier from a phandle array by name. |
| #define | [DT\_INST\_PHANDLE\_BY\_IDX](#ga10d93a1f9a9f5e225508c4c383654b1c)(inst, prop, idx) |
|  | Get a DT\_DRV\_COMPAT instance's node identifier for a phandle in a property. |
| #define | [DT\_INST\_PHANDLE](#ga81c10f478c86e5a4c18eb7a990447137)(inst, prop) |
|  | Get a DT\_DRV\_COMPAT instance's node identifier for a phandle property's value. |
| #define | [DT\_INST\_REG\_HAS\_IDX](#ga26bbff9ebaed549140d2530a0b99e8a4)(inst, idx) |
|  | is `idx` a valid register block index on a DT\_DRV\_COMPAT instance? |
| #define | [DT\_INST\_REG\_HAS\_NAME](#ga8b15b84b03c3dc6fd9d7e127a44392b3)(inst, name) |
|  | is `name` a valid register block name on a DT\_DRV\_COMPAT instance? |
| #define | [DT\_INST\_REG\_ADDR\_BY\_IDX\_RAW](#gade870f8f5c78c3c6244ada35049334a5)(inst, idx) |
|  | Get a DT\_DRV\_COMPAT instance's idx-th register block's raw address. |
| #define | [DT\_INST\_REG\_ADDR\_BY\_IDX](#ga0fe0403821883598da6cfad4f3962115)(inst, idx) |
|  | Get a DT\_DRV\_COMPAT instance's idx-th register block's address. |
| #define | [DT\_INST\_REG\_SIZE\_BY\_IDX](#gab1152c9f069c69b0269c1a4e744b9dd9)(inst, idx) |
|  | Get a DT\_DRV\_COMPAT instance's idx-th register block's size. |
| #define | [DT\_INST\_REG\_ADDR\_BY\_NAME](#ga722d6f7b97136aa9229242e4ba7dd25c)(inst, name) |
|  | Get a DT\_DRV\_COMPAT's register block address by name. |
| #define | [DT\_INST\_REG\_ADDR\_BY\_NAME\_OR](#gaf8d6ec7f68f566360743f7ea7cb7f8fb)(inst, name, default\_value) |
|  | Like [DT\_INST\_REG\_ADDR\_BY\_NAME()](#ga722d6f7b97136aa9229242e4ba7dd25c), but with a fallback to `default_value`. |
| #define | [DT\_INST\_REG\_ADDR\_BY\_NAME\_U64](#ga8af83c4c65e607b93aa60a690295d625)(inst, name) |
|  | 64-bit version of [DT\_INST\_REG\_ADDR\_BY\_NAME()](#ga722d6f7b97136aa9229242e4ba7dd25c) |
| #define | [DT\_INST\_REG\_SIZE\_BY\_NAME](#gaf82457c5dcfef7eeba074afb95d48714)(inst, name) |
|  | Get a DT\_DRV\_COMPAT's register block size by name. |
| #define | [DT\_INST\_REG\_SIZE\_BY\_NAME\_OR](#ga8494b94b6dbec875eba61e10f269cce6)(inst, name, default\_value) |
|  | Like [DT\_INST\_REG\_SIZE\_BY\_NAME()](#gaf82457c5dcfef7eeba074afb95d48714), but with a fallback to `default_value`. |
| #define | [DT\_INST\_REG\_ADDR\_RAW](#ga79627566ff2486cfd2425a04974d71a3)(inst) |
|  | Get a DT\_DRV\_COMPAT's (only) register block raw address. |
| #define | [DT\_INST\_REG\_ADDR](#gafde8fa67b94ac959ba2e24b44b3386a7)(inst) |
|  | Get a DT\_DRV\_COMPAT's (only) register block address. |
| #define | [DT\_INST\_REG\_ADDR\_U64](#gaba47dcabd8754eda87e35efd7289f976)(inst) |
|  | 64-bit version of [DT\_INST\_REG\_ADDR()](#gafde8fa67b94ac959ba2e24b44b3386a7) |
| #define | [DT\_INST\_REG\_SIZE](#gaa7cea29435e1db59470302abb5ee88dd)(inst) |
|  | Get a DT\_DRV\_COMPAT's (only) register block size. |
| #define | [DT\_INST\_NUM\_IRQS](#ga446d4b9c267e7c9da73dfb8a07701f2a)(inst) |
|  | Get a DT\_DRV\_COMPAT's number of interrupts. |
| #define | [DT\_INST\_IRQ\_LEVEL](#ga5c06043fd17c891e2cbbe0508248b638)(inst) |
|  | Get a DT\_DRV\_COMPAT interrupt level. |
| #define | [DT\_INST\_IRQ\_BY\_IDX](#gad0d69a61ad842aa1dc3a5d4a304c3f2f)(inst, idx, cell) |
|  | Get a DT\_DRV\_COMPAT interrupt specifier value at an index. |
| #define | [DT\_INST\_IRQ\_INTC\_BY\_IDX](#gab29f18e52d7475245c9fbeb4cd8e7769)(inst, idx) |
|  | Get a DT\_DRV\_COMPAT interrupt specifier's interrupt controller by index. |
| #define | [DT\_INST\_IRQ\_INTC\_BY\_NAME](#gadd0f339e10b071da34d44922ad0c7bfd)(inst, name) |
|  | Get a DT\_DRV\_COMPAT interrupt specifier's interrupt controller by name. |
| #define | [DT\_INST\_IRQ\_INTC](#gabf127c8370af849d2b5560e87ee04809)(inst) |
|  | Get a DT\_DRV\_COMPAT interrupt specifier's interrupt controller. |
| #define | [DT\_INST\_IRQ\_BY\_NAME](#ga1ff6f24f9c97d4b611e4bf50ce5175d3)(inst, name, cell) |
|  | Get a DT\_DRV\_COMPAT interrupt specifier value by name. |
| #define | [DT\_INST\_IRQ](#ga789eb58422bab7b3a79b487c4a8a82d6)(inst, cell) |
|  | Get a DT\_DRV\_COMPAT interrupt specifier's value. |
| #define | [DT\_INST\_IRQN](#ga4e5a5f20f5dd9ea4cfda61def2c16ed3)(inst) |
|  | Get a DT\_DRV\_COMPAT's (only) irq number. |
| #define | [DT\_INST\_IRQN\_BY\_IDX](#gaeb0c023f53ed87a6707bbca8ba05ce45)(inst, idx) |
|  | Get a DT\_DRV\_COMPAT's irq number at index. |
| #define | [DT\_INST\_BUS](#gacecb46743315738dcd9a0765ea78276a)(inst) |
|  | Get a DT\_DRV\_COMPAT's bus node identifier. |
| #define | [DT\_INST\_ON\_BUS](#ga7a29bda946b399a7af92ec9cd09b4e98)(inst, bus) |
|  | Test if a DT\_DRV\_COMPAT's bus type is a given type. |
| #define | [DT\_INST\_STRING\_TOKEN\_OR](#ga79fd00d1ece5538f7705c241ab869ea8)(inst, name, default\_value) |
|  | Like [DT\_INST\_STRING\_TOKEN()](#ga8e8c72187ce0d47fd24e4585f3d48484), but with a fallback to `default_value`. |
| #define | [DT\_INST\_STRING\_UPPER\_TOKEN\_OR](#ga72981780b2ede73c49ef9e5a7c6247c2)(inst, name, default\_value) |
|  | Like [DT\_INST\_STRING\_UPPER\_TOKEN()](#ga0487d19ae023acb9b0eb613317f31aa5), but with a fallback to `default_value`. |
| #define | [DT\_INST\_STRING\_UNQUOTED\_OR](#ga56bc0c0a46f6be421082119604cde643)(inst, name, default\_value) |
|  | Like [DT\_INST\_STRING\_UNQUOTED()](#ga1c4fc4c808113cb6e0d7b54af9869228), but with a fallback to `default_value`. |
| #define | [DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY](#ga1727af4beed08b248a98ad68bc5f1027)(compat, bus) |
|  | Test if any enabled node with the given compatible is on the given bus type. |
| #define | [DT\_ANY\_INST\_ON\_BUS\_STATUS\_OKAY](#gaa4ff1fe4242399fbd667fbee7e98040a)(bus) |
|  | Test if any DT\_DRV\_COMPAT node is on a bus of a given type and has status okay. |
| #define | [DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY](#gaf2a45df474090b0403dffe1b7b82b735)(prop) |
|  | Check if any DT\_DRV\_COMPAT node with status okay has a given property. |
| #define | [DT\_ANY\_COMPAT\_HAS\_PROP\_STATUS\_OKAY](#ga052727464d4f04768eaa71b7522c9a61)(compat, prop) |
|  | Check if any device node with status okay has a given property. |
| #define | [DT\_ANY\_INST\_HAS\_BOOL\_STATUS\_OKAY](#gab3d2f48ad95c4e2af76eed5e34735b18)(prop) |
|  | Check if any DT\_DRV\_COMPAT node with status okay has a given boolean property that exists. |
| #define | [DT\_INST\_FOREACH\_STATUS\_OKAY](#gaeac7ed0f4a6820a6e5d7dadb6d62d6e7)(fn) |
|  | Call `fn` on all nodes with compatible DT\_DRV\_COMPAT and status okay. |
| #define | [DT\_INST\_FOREACH\_STATUS\_OKAY\_VARGS](#ga1b9fd4b9c37a23e52e69ea23f7aedb38)(fn, ...) |
|  | Call `fn` on all nodes with compatible DT\_DRV\_COMPAT and status okay with multiple arguments. |
| #define | [DT\_INST\_FOREACH\_NODELABEL](#gafd15350971dee495f955f2fcc7edd82c)(inst, fn) |
|  | Call `fn` on all node labels for a given DT\_DRV\_COMPAT instance. |
| #define | [DT\_INST\_FOREACH\_NODELABEL\_VARGS](#ga3cf2a5bc8bad5ef8d47feb56c8215ca6)(inst, fn, ...) |
|  | Call `fn` on all node labels for a given DT\_DRV\_COMPAT instance with multiple arguments. |
| #define | [DT\_INST\_FOREACH\_PROP\_ELEM](#gaf163f2f85b3893ca46c87f0fcbe65255)(inst, prop, fn) |
|  | Invokes `fn` for each element of property `prop` for a DT\_DRV\_COMPAT instance. |
| #define | [DT\_INST\_FOREACH\_PROP\_ELEM\_SEP](#ga08de2f0ba1a6ec395f198e06c5f52373)(inst, prop, fn, sep) |
|  | Invokes `fn` for each element of property `prop` for a DT\_DRV\_COMPAT instance with a separator. |
| #define | [DT\_INST\_FOREACH\_PROP\_ELEM\_VARGS](#ga31b9022f7add3d77417b78ed67d544e3)(inst, prop, fn, ...) |
|  | Invokes `fn` for each element of property `prop` for a DT\_DRV\_COMPAT instance with multiple arguments. |
| #define | [DT\_INST\_FOREACH\_PROP\_ELEM\_SEP\_VARGS](#ga41b9dfd3519809bfc3c1c500780d6a2d)(inst, prop, fn, sep, ...) |
|  | Invokes `fn` for each element of property `prop` for a DT\_DRV\_COMPAT instance with multiple arguments and a separator. |
| #define | [DT\_INST\_NODE\_HAS\_PROP](#gaa03419e2d9c887a81e16e96b5947bccb)(inst, prop) |
|  | Does a DT\_DRV\_COMPAT instance have a property? |
| #define | [DT\_INST\_NODE\_HAS\_COMPAT](#gaf88c7dc0e935ad7097e317e54c362ba0)(inst, compat) |
|  | Does a DT\_DRV\_COMPAT instance have the compatible? |
| #define | [DT\_INST\_PHA\_HAS\_CELL\_AT\_IDX](#gae054b89701ec9fae577320fb7b9cae1e)(inst, pha, idx, cell) |
|  | Does a phandle array have a named cell specifier at an index for a DT\_DRV\_COMPAT instance? |
| #define | [DT\_INST\_PHA\_HAS\_CELL](#gab8083dae430aeb93a967bbf98aa9eefc)(inst, pha, cell) |
|  | Does a phandle array have a named cell specifier at index 0 for a DT\_DRV\_COMPAT instance? |
| #define | [DT\_INST\_IRQ\_HAS\_IDX](#gabb45132ef78818512c02bdf1f5a38068)(inst, idx) |
|  | is index valid for interrupt property on a DT\_DRV\_COMPAT instance? |
| #define | [DT\_INST\_IRQ\_HAS\_CELL\_AT\_IDX](#gab176ff07912cea915c811406e8f5e386)(inst, idx, cell) |
|  | Does a DT\_DRV\_COMPAT instance have an interrupt named cell specifier? |
| #define | [DT\_INST\_IRQ\_HAS\_CELL](#gabec43df3451bd917120b283d76c57054)(inst, cell) |
|  | Does a DT\_DRV\_COMPAT instance have an interrupt value? |
| #define | [DT\_INST\_IRQ\_HAS\_NAME](#gaa038ffc9b4f5c897a4a9e6d0e9836ffd)(inst, name) |
|  | Does a DT\_DRV\_COMPAT instance have an interrupt value? |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#ga052727464d4f04768eaa71b7522c9a61)DT\_ANY\_COMPAT\_HAS\_PROP\_STATUS\_OKAY

| #define DT\_ANY\_COMPAT\_HAS\_PROP\_STATUS\_OKAY | ( |  | *compat*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

([DT\_COMPAT\_FOREACH\_STATUS\_OKAY\_VARGS](group__devicetree-generic-foreach.md#ga368d08572b01efacdad370e6ceb515f9)(compat, DT\_COMPAT\_NODE\_HAS\_PROP\_AND\_OR, prop) 0)

[DT\_COMPAT\_FOREACH\_STATUS\_OKAY\_VARGS](group__devicetree-generic-foreach.md#ga368d08572b01efacdad370e6ceb515f9)

#define DT\_COMPAT\_FOREACH\_STATUS\_OKAY\_VARGS(compat, fn,...)

Call fn on all nodes with compatible compat and status okay with multiple arguments.

**Definition** devicetree.h:3533

Check if any device node with status okay has a given property.

Parameters
:   | compat | lowercase-and-underscores devicetree compatible |
    | --- | --- |
    | prop | lowercase-and-underscores property name |

Example devicetree overlay:

&i2c0 {

sensor0: sensor@0 {

compatible = "vnd,some-sensor";

status = "okay";

reg = <0>;

foo = <1>;

bar = <2>;

};

sensor1: sensor@1 {

compatible = "vnd,some-sensor";

status = "okay";

reg = <1>;

foo = <2>;

};

sensor2: sensor@2 {

compatible = "vnd,some-sensor";

status = "disabled";

reg = <2>;

baz = <1>;

};

};

Example usage:

[DT\_ANY\_COMPAT\_HAS\_PROP\_STATUS\_OKAY](#ga052727464d4f04768eaa71b7522c9a61)(vnd\_some\_sensor, foo) // 1

[DT\_ANY\_COMPAT\_HAS\_PROP\_STATUS\_OKAY](#ga052727464d4f04768eaa71b7522c9a61)(vnd\_some\_sensor, bar) // 1

[DT\_ANY\_COMPAT\_HAS\_PROP\_STATUS\_OKAY](#ga052727464d4f04768eaa71b7522c9a61)(vnd\_some\_sensor, baz) // 0

[DT\_ANY\_COMPAT\_HAS\_PROP\_STATUS\_OKAY](#ga052727464d4f04768eaa71b7522c9a61)

#define DT\_ANY\_COMPAT\_HAS\_PROP\_STATUS\_OKAY(compat, prop)

Check if any device node with status okay has a given property.

**Definition** devicetree.h:4867

## [◆ ](#gab3d2f48ad95c4e2af76eed5e34735b18)DT\_ANY\_INST\_HAS\_BOOL\_STATUS\_OKAY

| #define DT\_ANY\_INST\_HAS\_BOOL\_STATUS\_OKAY | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([IS\_EMPTY](group__sys-util.md#gab9487eea703d51cb1f235432dab4a1c7)(DT\_ANY\_INST\_HAS\_BOOL\_STATUS\_OKAY\_(prop)), (0), (1))

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:203

[IS\_EMPTY](group__sys-util.md#gab9487eea703d51cb1f235432dab4a1c7)

#define IS\_EMPTY(...)

Check if a macro has a replacement expression.

**Definition** util\_macro.h:301

Check if any DT\_DRV\_COMPAT node with status okay has a given boolean property that exists.

This differs from [DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY](#gaf2a45df474090b0403dffe1b7b82b735) because even when not present on a node, the boolean property is generated with a value of 0 and therefore exists.

Parameters
:   | prop | lowercase-and-underscores property name |
    | --- | --- |

Example devicetree overlay:

&i2c0 {

sensor0: sensor@0 {

compatible = "vnd,some-sensor";

status = "okay";

reg = <0>;

foo;

bar;

};

sensor1: sensor@1 {

compatible = "vnd,some-sensor";

status = "okay";

reg = <1>;

foo;

};

sensor2: sensor@2 {

compatible = "vnd,some-sensor";

status = "disabled";

reg = <2>;

baz;

};

};

Example usage:

#define DT\_DRV\_COMPAT vnd\_some\_sensor

[DT\_ANY\_INST\_HAS\_BOOL\_STATUS\_OKAY](#gab3d2f48ad95c4e2af76eed5e34735b18)(foo) // 1

[DT\_ANY\_INST\_HAS\_BOOL\_STATUS\_OKAY](#gab3d2f48ad95c4e2af76eed5e34735b18)(bar) // 1

[DT\_ANY\_INST\_HAS\_BOOL\_STATUS\_OKAY](#gab3d2f48ad95c4e2af76eed5e34735b18)(baz) // 0

[DT\_ANY\_INST\_HAS\_BOOL\_STATUS\_OKAY](#gab3d2f48ad95c4e2af76eed5e34735b18)

#define DT\_ANY\_INST\_HAS\_BOOL\_STATUS\_OKAY(prop)

Check if any DT\_DRV\_COMPAT node with status okay has a given boolean property that exists.

**Definition** devicetree.h:4917

## [◆ ](#gaf2a45df474090b0403dffe1b7b82b735)DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY

| #define DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY | ( |  | *prop* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([IS\_EMPTY](group__sys-util.md#gab9487eea703d51cb1f235432dab4a1c7)(DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY\_(prop)), (0), (1))

Check if any DT\_DRV\_COMPAT node with status okay has a given property.

Parameters
:   | prop | lowercase-and-underscores property name |
    | --- | --- |

Example devicetree overlay:

&i2c0 {

sensor0: sensor@0 {

compatible = "vnd,some-sensor";

status = "okay";

reg = <0>;

foo = <1>;

bar = <2>;

};

sensor1: sensor@1 {

compatible = "vnd,some-sensor";

status = "okay";

reg = <1>;

foo = <2>;

};

sensor2: sensor@2 {

compatible = "vnd,some-sensor";

status = "disabled";

reg = <2>;

baz = <1>;

};

};

Example usage:

#define DT\_DRV\_COMPAT vnd\_some\_sensor

[DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY](#gaf2a45df474090b0403dffe1b7b82b735)(foo) // 1

[DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY](#gaf2a45df474090b0403dffe1b7b82b735)(bar) // 1

[DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY](#gaf2a45df474090b0403dffe1b7b82b735)(baz) // 0

[DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY](#gaf2a45df474090b0403dffe1b7b82b735)

#define DT\_ANY\_INST\_HAS\_PROP\_STATUS\_OKAY(prop)

Check if any DT\_DRV\_COMPAT node with status okay has a given property.

**Definition** devicetree.h:4820

## [◆ ](#gaa4ff1fe4242399fbd667fbee7e98040a)DT\_ANY\_INST\_ON\_BUS\_STATUS\_OKAY

| #define DT\_ANY\_INST\_ON\_BUS\_STATUS\_OKAY | ( |  | *bus* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY](#ga1727af4beed08b248a98ad68bc5f1027)(DT\_DRV\_COMPAT, bus)

[DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY](#ga1727af4beed08b248a98ad68bc5f1027)

#define DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY(compat, bus)

Test if any enabled node with the given compatible is on the given bus type.

**Definition** devicetree.h:4738

Test if any DT\_DRV\_COMPAT node is on a bus of a given type and has status okay.

This is a special-purpose macro which can be useful when writing drivers for devices which can appear on multiple buses. One example is a sensor device which may be wired on an I2C or SPI bus.

Example devicetree overlay:

&i2c0 {

temp: temperature-sensor@76 {

compatible = "vnd,some-sensor";

reg = <0x76>;

};

};

Example usage, assuming i2c0 is an I2C bus controller node, and therefore temp is on an I2C bus:

#define DT\_DRV\_COMPAT vnd\_some\_sensor

[DT\_ANY\_INST\_ON\_BUS\_STATUS\_OKAY](#gaa4ff1fe4242399fbd667fbee7e98040a)(i2c) // 1

[DT\_ANY\_INST\_ON\_BUS\_STATUS\_OKAY](#gaa4ff1fe4242399fbd667fbee7e98040a)

#define DT\_ANY\_INST\_ON\_BUS\_STATUS\_OKAY(bus)

Test if any DT\_DRV\_COMPAT node is on a bus of a given type and has status okay.

**Definition** devicetree.h:4773

Parameters
:   | bus | a binding's bus type as a C token, lowercased and without quotes |
    | --- | --- |

Returns
:   1 if any enabled node with that compatible is on that bus type, 0 otherwise

## [◆ ](#ga219f413efba2f4c0151468b9a25a8dc1)DT\_DRV\_INST

| #define DT\_DRV\_INST | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_INST](group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead)(inst, DT\_DRV\_COMPAT)

[DT\_INST](group__devicetree-generic-id.md#gae199b930cb21ff38dab284a696093ead)

#define DT\_INST(inst, compat)

Get a node identifier for an instance of a compatible.

**Definition** devicetree.h:349

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   a node identifier for the node with DT\_DRV\_COMPAT compatible and instance number `inst`

## [◆ ](#ga1727af4beed08b248a98ad68bc5f1027)DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY

| #define DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY | ( |  | *compat*, |
| --- | --- | --- | --- |
|  |  |  | *bus* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)(DT\_CAT4(DT\_COMPAT\_, compat, \_BUS\_, bus))

[IS\_ENABLED](group__sys-util.md#ga111fe4e9d63758262fc6810a782cb32a)

#define IS\_ENABLED(config\_macro)

Check for macro definition in compiler-visible expressions.

**Definition** util\_macro.h:148

Test if any enabled node with the given compatible is on the given bus type.

This is like [DT\_ANY\_INST\_ON\_BUS\_STATUS\_OKAY()](#gaa4ff1fe4242399fbd667fbee7e98040a), except it can also be useful for handling multiple compatibles in single source file.

Example devicetree overlay:

&i2c0 {

temp: temperature-sensor@76 {

compatible = "vnd,some-sensor";

reg = <0x76>;

};

};

Example usage, assuming i2c0 is an I2C bus controller node, and therefore temp is on an I2C bus:

[DT\_HAS\_COMPAT\_ON\_BUS\_STATUS\_OKAY](#ga1727af4beed08b248a98ad68bc5f1027)(vnd\_some\_sensor, i2c) // 1

Parameters
:   | compat | lowercase-and-underscores compatible, without quotes |
    | --- | --- |
    | bus | a binding's bus type as a C token, lowercased and without quotes |

Returns
:   1 if any enabled node with that compatible is on that bus type, 0 otherwise

## [◆ ](#gacecb46743315738dcd9a0765ea78276a)DT\_INST\_BUS

| #define DT\_INST\_BUS | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_BUS](group__devicetree-generic-bus.md#ga1082d31ac2dafdf9e085d4c23f2169dc)

#define DT\_BUS(node\_id)

Node's bus controller.

**Definition** devicetree.h:3861

[DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3909

Get a DT\_DRV\_COMPAT's bus node identifier.

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   node identifier for the instance's bus node

## [◆ ](#gaaa4bfec30b277e0a8e2b0285a988d61d)DT\_INST\_CHILD

| #define DT\_INST\_CHILD | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *child* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_CHILD](group__devicetree-generic-id.md#ga88259608f4e9083ccc2e9ca5ec2c212e)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), child)

[DT\_CHILD](group__devicetree-generic-id.md#ga88259608f4e9083ccc2e9ca5ec2c212e)

#define DT\_CHILD(node\_id, child)

Get a node identifier for a child node.

**Definition** devicetree.h:436

Get a node identifier for a child node of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1).

Parameters
:   | inst | instance number |
    | --- | --- |
    | child | lowercase-and-underscores child node name |

Returns
:   node identifier for the node with the name referred to by 'child'

See also
:   [DT\_CHILD](group__devicetree-generic-id.md#ga88259608f4e9083ccc2e9ca5ec2c212e "Get a node identifier for a child node.")

## [◆ ](#ga49e2e39f4d93956217584df40316290b)DT\_INST\_CHILD\_NUM

| #define DT\_INST\_CHILD\_NUM | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_CHILD\_NUM](group__devicetree-generic-id.md#ga37cf660c2a7a844f70191d21b6543dc1)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_CHILD\_NUM](group__devicetree-generic-id.md#ga37cf660c2a7a844f70191d21b6543dc1)

#define DT\_CHILD\_NUM(node\_id)

Get the number of child nodes of a given node.

**Definition** devicetree.h:659

Get the number of child nodes of a given node.

This is equivalent to

See also
:   [DT\_CHILD\_NUM(DT\_DRV\_INST(inst))](group__devicetree-generic-id.md#ga37cf660c2a7a844f70191d21b6543dc1 "Get the number of child nodes of a given node.").

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |

Returns
:   Number of child nodes

## [◆ ](#ga1a54403986077e46684c5198f4d53421)DT\_INST\_CHILD\_NUM\_STATUS\_OKAY

| #define DT\_INST\_CHILD\_NUM\_STATUS\_OKAY | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_CHILD\_NUM\_STATUS\_OKAY](group__devicetree-generic-id.md#ga98544b8fd880fdd632f18e2410d39739)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_CHILD\_NUM\_STATUS\_OKAY](group__devicetree-generic-id.md#ga98544b8fd880fdd632f18e2410d39739)

#define DT\_CHILD\_NUM\_STATUS\_OKAY(node\_id)

Get the number of child nodes of a given node which child nodes' status are okay.

**Definition** devicetree.h:669

Get the number of child nodes of a given node.

This is equivalent to

See also
:   [DT\_CHILD\_NUM\_STATUS\_OKAY(DT\_DRV\_INST(inst))](group__devicetree-generic-id.md#ga98544b8fd880fdd632f18e2410d39739 "Get the number of child nodes of a given node which child nodes' status are okay.").

Parameters
:   | inst | Devicetree instance number |
    | --- | --- |

Returns
:   Number of child nodes which status are okay

## [◆ ](#ga80b0321efd592a63e39400e5327bb601)DT\_INST\_ENUM\_HAS\_VALUE

| #define DT\_INST\_ENUM\_HAS\_VALUE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_ENUM\_HAS\_VALUE](group__devicetree-generic-prop.md#ga72e66a2b7a159d8b6210ef9be015c955)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, value)

[DT\_ENUM\_HAS\_VALUE](group__devicetree-generic-prop.md#ga72e66a2b7a159d8b6210ef9be015c955)

#define DT\_ENUM\_HAS\_VALUE(node\_id, prop, value)

Equivalent to DT\_ENUM\_HAS\_VALUE\_BY\_IDX(node\_id, prop, 0, value).

**Definition** devicetree.h:1054

Does a DT\_DRV\_COMPAT enumeration property have a given value?

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | value | lowercase-and-underscores enumeration value |

Returns
:   1 if the node property has the value *value*, 0 otherwise.

## [◆ ](#ga5057571e3996451258ae5c29a06d9ede)DT\_INST\_ENUM\_HAS\_VALUE\_BY\_IDX

| #define DT\_INST\_ENUM\_HAS\_VALUE\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx*, |
|  |  |  | *value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_ENUM\_HAS\_VALUE\_BY\_IDX](group__devicetree-generic-prop.md#ga3c8b19de88ffdb4246567bb54ef6e6a4)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, idx, value)

[DT\_ENUM\_HAS\_VALUE\_BY\_IDX](group__devicetree-generic-prop.md#ga3c8b19de88ffdb4246567bb54ef6e6a4)

#define DT\_ENUM\_HAS\_VALUE\_BY\_IDX(node\_id, prop, idx, value)

Does a node enumeration property array have a given value?

**Definition** devicetree.h:1044

Does a DT\_DRV\_COMPAT enumeration property have a given value by index?

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | idx | the index to get |
    | value | lowercase-and-underscores enumeration value |

Returns
:   zero-based index of the property's value in its enum

## [◆ ](#ga866d6c28eb7a72ba9831c7ee1ecb98d2)DT\_INST\_ENUM\_IDX

| #define DT\_INST\_ENUM\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_ENUM\_IDX](group__devicetree-generic-prop.md#ga6c1a3b93e30429c1c69a7e2d8fe2d840)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop)

[DT\_ENUM\_IDX](group__devicetree-generic-prop.md#ga6c1a3b93e30429c1c69a7e2d8fe2d840)

#define DT\_ENUM\_IDX(node\_id, prop)

Equivalent to DT\_ENUM\_IDX\_BY\_IDX(node\_id, prop, 0).

**Definition** devicetree.h:1003

Get a DT\_DRV\_COMPAT value's index into its enumeration values.

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |

Returns
:   zero-based index of the property's value in its enum: list

## [◆ ](#ga9de99aff4800b0f6f461fdb48bcc3969)DT\_INST\_ENUM\_IDX\_BY\_IDX

| #define DT\_INST\_ENUM\_IDX\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_ENUM\_IDX\_BY\_IDX](group__devicetree-generic-prop.md#gae2e5f62d8f0c1eefcbb60ec7a5e84be2)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, idx)

[DT\_ENUM\_IDX\_BY\_IDX](group__devicetree-generic-prop.md#gae2e5f62d8f0c1eefcbb60ec7a5e84be2)

#define DT\_ENUM\_IDX\_BY\_IDX(node\_id, prop, idx)

Get a property array value's index into its enumeration values.

**Definition** devicetree.h:994

Get a DT\_DRV\_COMPAT property array value's index into its enumeration values.

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | idx | the index to get |

Returns
:   zero-based index of the property's value in its enum: list

## [◆ ](#ga48315c386a33d9384078c4a4fcccfd5d)DT\_INST\_ENUM\_IDX\_BY\_IDX\_OR

| #define DT\_INST\_ENUM\_IDX\_BY\_IDX\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx*, |
|  |  |  | *default\_idx\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_ENUM\_IDX\_BY\_IDX\_OR](group__devicetree-generic-prop.md#gac4892f2a54e05bd922f8c85db9c16d73)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, idx, default\_idx\_value)

[DT\_ENUM\_IDX\_BY\_IDX\_OR](group__devicetree-generic-prop.md#gac4892f2a54e05bd922f8c85db9c16d73)

#define DT\_ENUM\_IDX\_BY\_IDX\_OR(node\_id, prop, idx, default\_idx\_value)

Like DT\_ENUM\_IDX\_BY\_IDX(), but with a fallback to a default enum index.

**Definition** devicetree.h:1020

Like [DT\_INST\_ENUM\_IDX\_BY\_IDX()](#ga9de99aff4800b0f6f461fdb48bcc3969), but with a fallback to a default enum index.

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | idx | the index to get |
    | default\_idx\_value | a fallback index value to expand to |

Returns
:   zero-based index of the property's value in its enum if present, default\_idx\_value otherwise

## [◆ ](#gafbf64148f9171ffd322f7689297e0da8)DT\_INST\_ENUM\_IDX\_OR

| #define DT\_INST\_ENUM\_IDX\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *default\_idx\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_ENUM\_IDX\_OR](group__devicetree-generic-prop.md#gac3616e3aa1a025235032786de8d31576)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, default\_idx\_value)

[DT\_ENUM\_IDX\_OR](group__devicetree-generic-prop.md#gac3616e3aa1a025235032786de8d31576)

#define DT\_ENUM\_IDX\_OR(node\_id, prop, default\_idx\_value)

Equivalent to DT\_ENUM\_IDX\_BY\_IDX\_OR(node\_id, prop, 0, default\_idx\_value).

**Definition** devicetree.h:1032

Like [DT\_INST\_ENUM\_IDX()](#ga866d6c28eb7a72ba9831c7ee1ecb98d2), but with a fallback to a default enum index.

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | default\_idx\_value | a fallback index value to expand to |

Returns
:   zero-based index of the property's value in its enum if present, default\_idx\_value otherwise

## [◆ ](#ga98f3fccc6f3004f72c3602a5f2b3a08e)DT\_INST\_FOREACH\_CHILD

| #define DT\_INST\_FOREACH\_CHILD | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *fn* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_FOREACH\_CHILD](group__devicetree-generic-foreach.md#ga2f4eead8e8190110f5c0eb353e6a408f)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), fn)

[DT\_FOREACH\_CHILD](group__devicetree-generic-foreach.md#ga2f4eead8e8190110f5c0eb353e6a408f)

#define DT\_FOREACH\_CHILD(node\_id, fn)

Invokes fn for each child of node\_id.

**Definition** devicetree.h:3110

Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1).

The macro `fn` should take one argument, which is the node identifier for the child node.

The children will be iterated over in the same order as they appear in the final devicetree.

Parameters
:   | inst | instance number |
    | --- | --- |
    | fn | macro to invoke on each child node identifier |

See also
:   [DT\_FOREACH\_CHILD](group__devicetree-generic-foreach.md#ga2f4eead8e8190110f5c0eb353e6a408f "Invokes fn for each child of node_id.")

## [◆ ](#gae8d01eb2d6a576246f225a5cbbec34e5)DT\_INST\_FOREACH\_CHILD\_SEP

| #define DT\_INST\_FOREACH\_CHILD\_SEP | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *fn*, |
|  |  |  | *sep* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_FOREACH\_CHILD\_SEP](group__devicetree-generic-foreach.md#ga1fbeb335d66745803dbf7a185bf10afc)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), fn, sep)

[DT\_FOREACH\_CHILD\_SEP](group__devicetree-generic-foreach.md#ga1fbeb335d66745803dbf7a185bf10afc)

#define DT\_FOREACH\_CHILD\_SEP(node\_id, fn, sep)

Invokes fn for each child of node\_id with a separator.

**Definition** devicetree.h:3153

Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1) with a separator.

The macro `fn` should take one argument, which is the node identifier for the child node.

Parameters
:   | inst | instance number |
    | --- | --- |
    | fn | macro to invoke on each child node identifier |
    | sep | Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator. |

See also
:   [DT\_FOREACH\_CHILD\_SEP](group__devicetree-generic-foreach.md#ga1fbeb335d66745803dbf7a185bf10afc "Invokes fn for each child of node_id with a separator.")

## [◆ ](#gac70fcf3052d9dfa949d7e197fece1413)DT\_INST\_FOREACH\_CHILD\_SEP\_VARGS

| #define DT\_INST\_FOREACH\_CHILD\_SEP\_VARGS | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *fn*, |
|  |  |  | *sep*, |
|  |  |  | ... ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_FOREACH\_CHILD\_SEP\_VARGS](group__devicetree-generic-foreach.md#ga0042485aef7caaa48fa252b76a6629aa)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), fn, sep, \_\_VA\_ARGS\_\_)

[DT\_FOREACH\_CHILD\_SEP\_VARGS](group__devicetree-generic-foreach.md#ga0042485aef7caaa48fa252b76a6629aa)

#define DT\_FOREACH\_CHILD\_SEP\_VARGS(node\_id, fn, sep,...)

Invokes fn for each child of node\_id with separator and multiple arguments.

**Definition** devicetree.h:3189

Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1) with separator.

The macro `fn` takes multiple arguments. The first should be the node identifier for the child node. The remaining are passed-in by the caller.

Parameters
:   | inst | instance number |
    | --- | --- |
    | fn | macro to invoke on each child node identifier |
    | sep | Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator. |
    | ... | variable number of arguments to pass to `fn` |

See also
:   [DT\_FOREACH\_CHILD\_SEP\_VARGS](group__devicetree-generic-foreach.md#ga0042485aef7caaa48fa252b76a6629aa "Invokes fn for each child of node_id with separator and multiple arguments.")

## [◆ ](#gad416dd269b1af1e392ef81397b9bc814)DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY

| #define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *fn* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_FOREACH\_CHILD\_STATUS\_OKAY](group__devicetree-generic-foreach.md#gae907df926b94f1da52b1ab701392f3bd)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), fn)

[DT\_FOREACH\_CHILD\_STATUS\_OKAY](group__devicetree-generic-foreach.md#gae907df926b94f1da52b1ab701392f3bd)

#define DT\_FOREACH\_CHILD\_STATUS\_OKAY(node\_id, fn)

Call fn on the child nodes with status okay.

**Definition** devicetree.h:3207

Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1) with status okay.

The macro `fn` should take one argument, which is the node identifier for the child node.

Parameters
:   | inst | instance number |
    | --- | --- |
    | fn | macro to invoke on each child node identifier |

See also
:   [DT\_FOREACH\_CHILD\_STATUS\_OKAY](group__devicetree-generic-foreach.md#gae907df926b94f1da52b1ab701392f3bd "Call fn on the child nodes with status okay.")

## [◆ ](#gae28554827ab7aaac3578ef07747a589d)DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP

| #define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *fn*, |
|  |  |  | *sep* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP](group__devicetree-generic-foreach.md#ga97414c01ebbb6df5ee2862c0ee9d44ce)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), fn, sep)

[DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP](group__devicetree-generic-foreach.md#ga97414c01ebbb6df5ee2862c0ee9d44ce)

#define DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP(node\_id, fn, sep)

Call fn on the child nodes with status okay with separator.

**Definition** devicetree.h:3226

Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1) with status okay and with separator.

The macro `fn` should take one argument, which is the node identifier for the child node.

Parameters
:   | inst | instance number |
    | --- | --- |
    | fn | macro to invoke on each child node identifier |
    | sep | Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator. |

See also
:   [DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP](group__devicetree-generic-foreach.md#ga97414c01ebbb6df5ee2862c0ee9d44ce "Call fn on the child nodes with status okay with separator.")

## [◆ ](#ga236cca0984f1c701c9b4855111c6cb29)DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS

| #define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *fn*, |
|  |  |  | *sep*, |
|  |  |  | ... ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS](group__devicetree-generic-foreach.md#gaf46c1ac296f0d6c9388c3ca6fb4ca5cd)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), fn, sep, \_\_VA\_ARGS\_\_)

[DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS](group__devicetree-generic-foreach.md#gaf46c1ac296f0d6c9388c3ca6fb4ca5cd)

#define DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS(node\_id, fn, sep,...)

Call fn on the child nodes with status okay with separator and multiple arguments.

**Definition** devicetree.h:3269

Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1) with status okay and with separator and multiple arguments.

The macro `fn` takes multiple arguments. The first should be the node identifier for the child node. The remaining are passed-in by the caller.

Parameters
:   | inst | instance number |
    | --- | --- |
    | fn | macro to invoke on each child node identifier |
    | sep | Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator. |
    | ... | variable number of arguments to pass to `fn` |

See also
:   [DT\_FOREACH\_CHILD\_STATUS\_OKAY\_SEP\_VARGS](group__devicetree-generic-foreach.md#gaf46c1ac296f0d6c9388c3ca6fb4ca5cd "Call fn on the child nodes with status okay with separator and multiple arguments.")

## [◆ ](#gac6dd19b2b6e603c11701cd07daec73d3)DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS

| #define DT\_INST\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *fn*, |
|  |  |  | ... ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS](group__devicetree-generic-foreach.md#ga8bbf6992e5f90d8a28035ea6211dd2a3)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), fn, \_\_VA\_ARGS\_\_)

[DT\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS](group__devicetree-generic-foreach.md#ga8bbf6992e5f90d8a28035ea6211dd2a3)

#define DT\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS(node\_id, fn,...)

Call fn on the child nodes with status okay with multiple arguments.

**Definition** devicetree.h:3248

Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1) with status okay and multiple arguments.

The macro `fn` takes multiple arguments. The first should be the node identifier for the child node. The remaining are passed-in by the caller.

Parameters
:   | inst | instance number |
    | --- | --- |
    | fn | macro to invoke on each child node identifier |
    | ... | variable number of arguments to pass to `fn` |

See also
:   [DT\_FOREACH\_CHILD\_STATUS\_OKAY\_VARGS](group__devicetree-generic-foreach.md#ga8bbf6992e5f90d8a28035ea6211dd2a3 "Call fn on the child nodes with status okay with multiple arguments.")

## [◆ ](#ga455cb42d31b575d79f8cbbebbd353651)DT\_INST\_FOREACH\_CHILD\_VARGS

| #define DT\_INST\_FOREACH\_CHILD\_VARGS | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *fn*, |
|  |  |  | ... ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_FOREACH\_CHILD\_VARGS](group__devicetree-generic-foreach.md#gae7461e9fa4687bf88cdd7c76f30986de)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), fn, \_\_VA\_ARGS\_\_)

[DT\_FOREACH\_CHILD\_VARGS](group__devicetree-generic-foreach.md#gae7461e9fa4687bf88cdd7c76f30986de)

#define DT\_FOREACH\_CHILD\_VARGS(node\_id, fn,...)

Invokes fn for each child of node\_id with multiple arguments.

**Definition** devicetree.h:3171

Call `fn` on all child nodes of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1).

The macro `fn` takes multiple arguments. The first should be the node identifier for the child node. The remaining are passed-in by the caller.

The children will be iterated over in the same order as they appear in the final devicetree.

Parameters
:   | inst | instance number |
    | --- | --- |
    | fn | macro to invoke on each child node identifier |
    | ... | variable number of arguments to pass to `fn` |

See also
:   [DT\_FOREACH\_CHILD](group__devicetree-generic-foreach.md#ga2f4eead8e8190110f5c0eb353e6a408f "Invokes fn for each child of node_id.")

## [◆ ](#gafd15350971dee495f955f2fcc7edd82c)DT\_INST\_FOREACH\_NODELABEL

| #define DT\_INST\_FOREACH\_NODELABEL | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *fn* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_FOREACH\_NODELABEL](group__devicetree-generic-foreach.md#gad5585436896efc4c5154a93b5980d3b0)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), fn)

[DT\_FOREACH\_NODELABEL](group__devicetree-generic-foreach.md#gad5585436896efc4c5154a93b5980d3b0)

#define DT\_FOREACH\_NODELABEL(node\_id, fn)

Invokes fn for each node label of a given node.

**Definition** devicetree.h:3578

Call `fn` on all node labels for a given DT\_DRV\_COMPAT instance.

Equivalent to [DT\_FOREACH\_NODELABEL(DT\_DRV\_INST(inst), fn)](group__devicetree-generic-foreach.md#gad5585436896efc4c5154a93b5980d3b0 "Invokes fn for each node label of a given node.").

Parameters
:   | inst | instance number |
    | --- | --- |
    | fn | macro which will be passed each node label for the node with that instance number |

## [◆ ](#ga3cf2a5bc8bad5ef8d47feb56c8215ca6)DT\_INST\_FOREACH\_NODELABEL\_VARGS

| #define DT\_INST\_FOREACH\_NODELABEL\_VARGS | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *fn*, |
|  |  |  | ... ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_FOREACH\_NODELABEL\_VARGS](group__devicetree-generic-foreach.md#ga2a88abdb46158bcf36a8c976a1e2186d)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), fn, \_\_VA\_ARGS\_\_)

[DT\_FOREACH\_NODELABEL\_VARGS](group__devicetree-generic-foreach.md#ga2a88abdb46158bcf36a8c976a1e2186d)

#define DT\_FOREACH\_NODELABEL\_VARGS(node\_id, fn,...)

Invokes fn for each node label of a given node with multiple arguments.

**Definition** devicetree.h:3617

Call `fn` on all node labels for a given DT\_DRV\_COMPAT instance with multiple arguments.

Equivalent to [DT\_FOREACH\_NODELABEL\_VARGS(DT\_DRV\_INST(inst), fn, ...)](group__devicetree-generic-foreach.md#ga2a88abdb46158bcf36a8c976a1e2186d "Invokes fn for each node label of a given node with multiple arguments.").

Parameters
:   | inst | instance number |
    | --- | --- |
    | fn | macro which will be passed each node label for the node with that instance number |
    | ... | additional arguments to pass to `fn` |

## [◆ ](#gaf163f2f85b3893ca46c87f0fcbe65255)DT\_INST\_FOREACH\_PROP\_ELEM

| #define DT\_INST\_FOREACH\_PROP\_ELEM | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *fn* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_FOREACH\_PROP\_ELEM](group__devicetree-generic-foreach.md#ga118a0477ab297a1bda9e16acf556babc)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, fn)

[DT\_FOREACH\_PROP\_ELEM](group__devicetree-generic-foreach.md#ga118a0477ab297a1bda9e16acf556babc)

#define DT\_FOREACH\_PROP\_ELEM(node\_id, prop, fn)

Invokes fn for each element in the value of property prop.

**Definition** devicetree.h:3322

Invokes `fn` for each element of property `prop` for a DT\_DRV\_COMPAT instance.

Equivalent to [DT\_FOREACH\_PROP\_ELEM(DT\_DRV\_INST(inst), prop, fn)](group__devicetree-generic-foreach.md#ga118a0477ab297a1bda9e16acf556babc "Invokes fn for each element in the value of property prop.").

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | fn | macro to invoke |

## [◆ ](#ga08de2f0ba1a6ec395f198e06c5f52373)DT\_INST\_FOREACH\_PROP\_ELEM\_SEP

| #define DT\_INST\_FOREACH\_PROP\_ELEM\_SEP | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *fn*, |
|  |  |  | *sep* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_FOREACH\_PROP\_ELEM\_SEP](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, fn, sep)

[DT\_FOREACH\_PROP\_ELEM\_SEP](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8)

#define DT\_FOREACH\_PROP\_ELEM\_SEP(node\_id, prop, fn, sep)

Invokes fn for each element in the value of property prop with separator.

**Definition** devicetree.h:3367

Invokes `fn` for each element of property `prop` for a DT\_DRV\_COMPAT instance with a separator.

Equivalent to [DT\_FOREACH\_PROP\_ELEM\_SEP(DT\_DRV\_INST(inst), prop, fn, sep)](group__devicetree-generic-foreach.md#ga72d0b6859b4fc61cde518aee118d9ed8 "Invokes fn for each element in the value of property prop with separator.").

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | fn | macro to invoke |
    | sep | Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator. |

## [◆ ](#ga41b9dfd3519809bfc3c1c500780d6a2d)DT\_INST\_FOREACH\_PROP\_ELEM\_SEP\_VARGS

| #define DT\_INST\_FOREACH\_PROP\_ELEM\_SEP\_VARGS | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *fn*, |
|  |  |  | *sep*, |
|  |  |  | ... ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_FOREACH\_PROP\_ELEM\_SEP\_VARGS](group__devicetree-generic-foreach.md#ga29120ee8718b889273dc2649ab25438f)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, fn, sep, \

\_\_VA\_ARGS\_\_)

[DT\_FOREACH\_PROP\_ELEM\_SEP\_VARGS](group__devicetree-generic-foreach.md#ga29120ee8718b889273dc2649ab25438f)

#define DT\_FOREACH\_PROP\_ELEM\_SEP\_VARGS(node\_id, prop, fn, sep,...)

Invokes fn for each element in the value of property prop with multiple arguments and a separator.

**Definition** devicetree.h:3409

Invokes `fn` for each element of property `prop` for a DT\_DRV\_COMPAT instance with multiple arguments and a separator.

Equivalent to DT\_FOREACH\_PROP\_ELEM\_SEP\_VARGS([DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1), prop, fn, sep, **VA\_ARGS**)

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | fn | macro to invoke |
    | sep | Separator (e.g. comma or semicolon). Must be in parentheses; this is required to enable providing a comma as separator. |
    | ... | variable number of arguments to pass to fn |

See also
:   [DT\_INST\_FOREACH\_PROP\_ELEM](#gaf163f2f85b3893ca46c87f0fcbe65255)

## [◆ ](#ga31b9022f7add3d77417b78ed67d544e3)DT\_INST\_FOREACH\_PROP\_ELEM\_VARGS

| #define DT\_INST\_FOREACH\_PROP\_ELEM\_VARGS | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *fn*, |
|  |  |  | ... ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_FOREACH\_PROP\_ELEM\_VARGS](group__devicetree-generic-foreach.md#gaae36970d49c860414374c76e136a9607)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, fn, \_\_VA\_ARGS\_\_)

[DT\_FOREACH\_PROP\_ELEM\_VARGS](group__devicetree-generic-foreach.md#gaae36970d49c860414374c76e136a9607)

#define DT\_FOREACH\_PROP\_ELEM\_VARGS(node\_id, prop, fn,...)

Invokes fn for each element in the value of property prop with multiple arguments.

**Definition** devicetree.h:3390

Invokes `fn` for each element of property `prop` for a DT\_DRV\_COMPAT instance with multiple arguments.

Equivalent to DT\_FOREACH\_PROP\_ELEM\_VARGS([DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1), prop, fn, **VA\_ARGS**)

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | fn | macro to invoke |
    | ... | variable number of arguments to pass to `fn` |

See also
:   [DT\_INST\_FOREACH\_PROP\_ELEM](#gaf163f2f85b3893ca46c87f0fcbe65255)

## [◆ ](#gaeac7ed0f4a6820a6e5d7dadb6d62d6e7)DT\_INST\_FOREACH\_STATUS\_OKAY

| #define DT\_INST\_FOREACH\_STATUS\_OKAY | ( |  | *fn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_HAS\_COMPAT\_STATUS\_OKAY](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)(DT\_DRV\_COMPAT), \

([UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(DT\_FOREACH\_OKAY\_INST\_, \

DT\_DRV\_COMPAT)(fn)), \

())

[DT\_HAS\_COMPAT\_STATUS\_OKAY](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)

#define DT\_HAS\_COMPAT\_STATUS\_OKAY(compat)

Does the devicetree have a status okay node with a compatible?

**Definition** devicetree.h:3711

[UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)

#define UTIL\_CAT(a,...)

**Definition** util\_internal.h:104

Call `fn` on all nodes with compatible DT\_DRV\_COMPAT and status okay.

This macro calls fn(inst) on each inst number that refers to a node with status okay. Whitespace is added between invocations.

Example devicetree fragment:

a {

compatible = "vnd,device";

status = "okay";

foobar = "DEV\_A";

};

b {

compatible = "vnd,device";

status = "okay";

foobar = "DEV\_B";

};

c {

compatible = "vnd,device";

status = "disabled";

foobar = "DEV\_C";

};

Example usage:

#define DT\_DRV\_COMPAT vnd\_device

#define MY\_FN(inst) DT\_INST\_PROP(inst, foobar),

[DT\_INST\_FOREACH\_STATUS\_OKAY](#gaeac7ed0f4a6820a6e5d7dadb6d62d6e7)(MY\_FN)

[DT\_INST\_FOREACH\_STATUS\_OKAY](#gaeac7ed0f4a6820a6e5d7dadb6d62d6e7)

#define DT\_INST\_FOREACH\_STATUS\_OKAY(fn)

Call fn on all nodes with compatible DT\_DRV\_COMPAT and status okay.

**Definition** devicetree.h:4985

This expands to:

MY\_FN(0) MY\_FN(1)

and from there, to either this:

```
"DEV_A", "DEV_B",
```

or this:

```
"DEV_B", "DEV_A",
```

No guarantees are made about the order that a and b appear in the expansion.

Note that `fn` is responsible for adding commas, semicolons, or other separators or terminators.

Device drivers should use this macro whenever possible to instantiate a struct device for each enabled node in the devicetree of the driver's compatible DT\_DRV\_COMPAT.

Parameters
:   | fn | Macro to call for each enabled node. Must accept an instance number as its only parameter. |
    | --- | --- |

## [◆ ](#ga1b9fd4b9c37a23e52e69ea23f7aedb38)DT\_INST\_FOREACH\_STATUS\_OKAY\_VARGS

| #define DT\_INST\_FOREACH\_STATUS\_OKAY\_VARGS | ( |  | *fn*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_HAS\_COMPAT\_STATUS\_OKAY](group__devicetree-generic-exist.md#ga916e11b66fdaab46e93c25241b62b52a)(DT\_DRV\_COMPAT), \

([UTIL\_CAT](util__internal_8h.md#a7e7766e792d1638bfbbc9d0f328d3d0d)(DT\_FOREACH\_OKAY\_INST\_VARGS\_, \

DT\_DRV\_COMPAT)(fn, \_\_VA\_ARGS\_\_)), \

())

Call `fn` on all nodes with compatible DT\_DRV\_COMPAT and status okay with multiple arguments.

Parameters
:   | fn | Macro to call for each enabled node. Must accept an instance number. |
    | --- | --- |
    | ... | variable number of arguments to pass to `fn` |

See also
:   [DT\_INST\_FOREACH\_STATUS\_OKAY](#gaeac7ed0f4a6820a6e5d7dadb6d62d6e7)
:   [DT\_COMPAT\_FOREACH\_STATUS\_OKAY\_VARGS](group__devicetree-generic-foreach.md#ga368d08572b01efacdad370e6ceb515f9 "Call fn on all nodes with compatible compat and status okay with multiple arguments.")

## [◆ ](#ga5c68d697534682988a51a343abed05c9)DT\_INST\_GPARENT

| #define DT\_INST\_GPARENT | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_GPARENT](group__devicetree-generic-id.md#gaa4eccf276a426cbbc6e440d72b692753)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_GPARENT](group__devicetree-generic-id.md#gaa4eccf276a426cbbc6e440d72b692753)

#define DT\_GPARENT(node\_id)

Get a node identifier for a grandparent node.

**Definition** devicetree.h:399

Get a DT\_DRV\_COMPAT grandparent's node identifier.

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   a node identifier for the instance's grandparent

See also
:   [DT\_GPARENT](group__devicetree-generic-id.md#gaa4eccf276a426cbbc6e440d72b692753 "Get a node identifier for a grandparent node.")

## [◆ ](#ga789eb58422bab7b3a79b487c4a8a82d6)DT\_INST\_IRQ

| #define DT\_INST\_IRQ | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_INST\_IRQ\_BY\_IDX](#gad0d69a61ad842aa1dc3a5d4a304c3f2f)(inst, 0, cell)

[DT\_INST\_IRQ\_BY\_IDX](#gad0d69a61ad842aa1dc3a5d4a304c3f2f)

#define DT\_INST\_IRQ\_BY\_IDX(inst, idx, cell)

Get a DT\_DRV\_COMPAT interrupt specifier value at an index.

**Definition** devicetree.h:4594

Get a DT\_DRV\_COMPAT interrupt specifier's value.

Parameters
:   | inst | instance number |
    | --- | --- |
    | cell | cell name specifier |

Returns
:   the named value at that index

## [◆ ](#gad0d69a61ad842aa1dc3a5d4a304c3f2f)DT\_INST\_IRQ\_BY\_IDX

| #define DT\_INST\_IRQ\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx, cell)

[DT\_IRQ\_BY\_IDX](group__devicetree-interrupts-prop.md#ga3779b2115eac60ab32adfc8d212e973f)

#define DT\_IRQ\_BY\_IDX(node\_id, idx, cell)

Get a value within an interrupt specifier at an index.

**Definition** devicetree.h:2678

Get a DT\_DRV\_COMPAT interrupt specifier value at an index.

Parameters
:   | inst | instance number |
    | --- | --- |
    | idx | logical index into the interrupt specifier array |
    | cell | cell name specifier |

Returns
:   the named value at the specifier given by the index

## [◆ ](#ga1ff6f24f9c97d4b611e4bf50ce5175d3)DT\_INST\_IRQ\_BY\_NAME

| #define DT\_INST\_IRQ\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_IRQ\_BY\_NAME](group__devicetree-interrupts-prop.md#ga904917c0a407343ef0185e9e6fe96812)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name, cell)

[DT\_IRQ\_BY\_NAME](group__devicetree-interrupts-prop.md#ga904917c0a407343ef0185e9e6fe96812)

#define DT\_IRQ\_BY\_NAME(node\_id, name, cell)

Get a value within an interrupt specifier by name.

**Definition** devicetree.h:2696

Get a DT\_DRV\_COMPAT interrupt specifier value by name.

Parameters
:   | inst | instance number |
    | --- | --- |
    | name | lowercase-and-underscores interrupt specifier name |
    | cell | cell name specifier |

Returns
:   the named value at the specifier given by the index

## [◆ ](#gabec43df3451bd917120b283d76c57054)DT\_INST\_IRQ\_HAS\_CELL

| #define DT\_INST\_IRQ\_HAS\_CELL | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_INST\_IRQ\_HAS\_CELL\_AT\_IDX](#gab176ff07912cea915c811406e8f5e386)(inst, 0, cell)

[DT\_INST\_IRQ\_HAS\_CELL\_AT\_IDX](#gab176ff07912cea915c811406e8f5e386)

#define DT\_INST\_IRQ\_HAS\_CELL\_AT\_IDX(inst, idx, cell)

Does a DT\_DRV\_COMPAT instance have an interrupt named cell specifier?

**Definition** devicetree.h:5161

Does a DT\_DRV\_COMPAT instance have an interrupt value?

Parameters
:   | inst | instance number |
    | --- | --- |
    | cell | named cell value whose existence to check |

Returns
:   1 if the named `cell` exists in the interrupt specifier at index 0 0 otherwise.

## [◆ ](#gab176ff07912cea915c811406e8f5e386)DT\_INST\_IRQ\_HAS\_CELL\_AT\_IDX

| #define DT\_INST\_IRQ\_HAS\_CELL\_AT\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx*, |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_IRQ\_HAS\_CELL\_AT\_IDX](group__devicetree-interrupts-prop.md#ga739ebdd4bd01d6b7beb75d915174206f)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx, cell)

[DT\_IRQ\_HAS\_CELL\_AT\_IDX](group__devicetree-interrupts-prop.md#ga739ebdd4bd01d6b7beb75d915174206f)

#define DT\_IRQ\_HAS\_CELL\_AT\_IDX(node\_id, idx, cell)

Does an interrupts property have a named cell specifier at an index?

**Definition** devicetree.h:2619

Does a DT\_DRV\_COMPAT instance have an interrupt named cell specifier?

Parameters
:   | inst | instance number |
    | --- | --- |
    | idx | index to check |
    | cell | named cell value whose existence to check |

Returns
:   1 if the named `cell` exists in the interrupt specifier at index `idx` 0 otherwise.

## [◆ ](#gabb45132ef78818512c02bdf1f5a38068)DT\_INST\_IRQ\_HAS\_IDX

| #define DT\_INST\_IRQ\_HAS\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_IRQ\_HAS\_IDX](group__devicetree-interrupts-prop.md#ga238a290dc6cea9479104ff8f95de1c4c)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

[DT\_IRQ\_HAS\_IDX](group__devicetree-interrupts-prop.md#ga238a290dc6cea9479104ff8f95de1c4c)

#define DT\_IRQ\_HAS\_IDX(node\_id, idx)

Is idx a valid interrupt index?

**Definition** devicetree.h:2606

is index valid for interrupt property on a DT\_DRV\_COMPAT instance?

Parameters
:   | inst | instance number |
    | --- | --- |
    | idx | logical index into the interrupt specifier array |

Returns
:   1 if the `idx` is valid for the interrupt property 0 otherwise.

## [◆ ](#gaa038ffc9b4f5c897a4a9e6d0e9836ffd)DT\_INST\_IRQ\_HAS\_NAME

| #define DT\_INST\_IRQ\_HAS\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_IRQ\_HAS\_NAME](group__devicetree-interrupts-prop.md#ga1c757ff5e4d15f1b3020b30f72c0dd5d)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_IRQ\_HAS\_NAME](group__devicetree-interrupts-prop.md#ga1c757ff5e4d15f1b3020b30f72c0dd5d)

#define DT\_IRQ\_HAS\_NAME(node\_id, name)

Does an interrupts property have a named specifier value at an index?

**Definition** devicetree.h:2640

Does a DT\_DRV\_COMPAT instance have an interrupt value?

Parameters
:   | inst | instance number |
    | --- | --- |
    | name | lowercase-and-underscores interrupt specifier name |

Returns
:   1 if `name` is a valid named specifier

## [◆ ](#gabf127c8370af849d2b5560e87ee04809)DT\_INST\_IRQ\_INTC

| #define DT\_INST\_IRQ\_INTC | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_INST\_IRQ\_INTC\_BY\_IDX](#gab29f18e52d7475245c9fbeb4cd8e7769)(inst, 0)

[DT\_INST\_IRQ\_INTC\_BY\_IDX](#gab29f18e52d7475245c9fbeb4cd8e7769)

#define DT\_INST\_IRQ\_INTC\_BY\_IDX(inst, idx)

Get a DT\_DRV\_COMPAT interrupt specifier's interrupt controller by index.

**Definition** devicetree.h:4603

Get a DT\_DRV\_COMPAT interrupt specifier's interrupt controller.

Note
:   Equivalent to [DT\_INST\_IRQ\_INTC\_BY\_IDX(node\_id, 0)](#gab29f18e52d7475245c9fbeb4cd8e7769)

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   node\_id of interrupt specifier's interrupt controller

See also
:   [DT\_INST\_IRQ\_INTC\_BY\_IDX()](#gab29f18e52d7475245c9fbeb4cd8e7769)

## [◆ ](#gab29f18e52d7475245c9fbeb4cd8e7769)DT\_INST\_IRQ\_INTC\_BY\_IDX

| #define DT\_INST\_IRQ\_INTC\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_IRQ\_INTC\_BY\_IDX](group__devicetree-interrupts-prop.md#ga061a34529fb2bbac9fe8615056d71ea4)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

[DT\_IRQ\_INTC\_BY\_IDX](group__devicetree-interrupts-prop.md#ga061a34529fb2bbac9fe8615056d71ea4)

#define DT\_IRQ\_INTC\_BY\_IDX(node\_id, idx)

Get an interrupt specifier's interrupt controller by index.

**Definition** devicetree.h:2750

Get a DT\_DRV\_COMPAT interrupt specifier's interrupt controller by index.

Parameters
:   | inst | instance number |
    | --- | --- |
    | idx | interrupt specifier's index |

Returns
:   node\_id of interrupt specifier's interrupt controller

## [◆ ](#gadd0f339e10b071da34d44922ad0c7bfd)DT\_INST\_IRQ\_INTC\_BY\_NAME

| #define DT\_INST\_IRQ\_INTC\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_IRQ\_INTC\_BY\_NAME](group__devicetree-interrupts-prop.md#gabee933352a948bd824beccc00c13387d)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_IRQ\_INTC\_BY\_NAME](group__devicetree-interrupts-prop.md#gabee933352a948bd824beccc00c13387d)

#define DT\_IRQ\_INTC\_BY\_NAME(node\_id, name)

Get an interrupt specifier's interrupt controller by name.

**Definition** devicetree.h:2797

Get a DT\_DRV\_COMPAT interrupt specifier's interrupt controller by name.

Parameters
:   | inst | instance number |
    | --- | --- |
    | name | interrupt specifier's name |

Returns
:   node\_id of interrupt specifier's interrupt controller

## [◆ ](#ga5c06043fd17c891e2cbbe0508248b638)DT\_INST\_IRQ\_LEVEL

| #define DT\_INST\_IRQ\_LEVEL | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_IRQ\_LEVEL](group__devicetree-interrupts-prop.md#ga4b6c7ad21691c40047373e5073e740c9)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_IRQ\_LEVEL](group__devicetree-interrupts-prop.md#ga4b6c7ad21691c40047373e5073e740c9)

#define DT\_IRQ\_LEVEL(node\_id)

Get the interrupt level for the node.

**Definition** devicetree.h:2594

Get a DT\_DRV\_COMPAT interrupt level.

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   interrupt level

## [◆ ](#ga4e5a5f20f5dd9ea4cfda61def2c16ed3)DT\_INST\_IRQN

| #define DT\_INST\_IRQN | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_IRQN](group__devicetree-interrupts-prop.md#ga5e00c208388736ce9b5bc0088a77cd95)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_IRQN](group__devicetree-interrupts-prop.md#ga5e00c208388736ce9b5bc0088a77cd95)

#define DT\_IRQN(node\_id)

Get a node's (only) irq number.

**Definition** devicetree.h:2894

Get a DT\_DRV\_COMPAT's (only) irq number.

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   the interrupt number for the node's only interrupt

## [◆ ](#gaeb0c023f53ed87a6707bbca8ba05ce45)DT\_INST\_IRQN\_BY\_IDX

| #define DT\_INST\_IRQN\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_IRQN\_BY\_IDX](group__devicetree-interrupts-prop.md#gaad6d6b27ea731a05a186a5dde8757698)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

[DT\_IRQN\_BY\_IDX](group__devicetree-interrupts-prop.md#gaad6d6b27ea731a05a186a5dde8757698)

#define DT\_IRQN\_BY\_IDX(node\_id, idx)

Get the node's Zephyr interrupt number at index If CONFIG\_MULTI\_LEVEL\_INTERRUPTS is enabled,...

**Definition** devicetree.h:2879

Get a DT\_DRV\_COMPAT's irq number at index.

Parameters
:   | inst | instance number |
    | --- | --- |
    | idx | logical index into the interrupt specifier array |

Returns
:   the interrupt number for the node's idx-th interrupt

## [◆ ](#gaf88c7dc0e935ad7097e317e54c362ba0)DT\_INST\_NODE\_HAS\_COMPAT

| #define DT\_INST\_NODE\_HAS\_COMPAT | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *compat* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_NODE\_HAS\_COMPAT](group__devicetree-generic-exist.md#gad8912ba5db980713e72257472ded3ced)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), compat)

[DT\_NODE\_HAS\_COMPAT](group__devicetree-generic-exist.md#gad8912ba5db980713e72257472ded3ced)

#define DT\_NODE\_HAS\_COMPAT(node\_id, compat)

Does a devicetree node match a compatible?

**Definition** devicetree.h:3751

Does a DT\_DRV\_COMPAT instance have the compatible?

Parameters
:   | inst | instance number |
    | --- | --- |
    | compat | lowercase-and-underscores compatible, without quotes |

Returns
:   1 if the instance matches the compatible, 0 otherwise.

## [◆ ](#gaa03419e2d9c887a81e16e96b5947bccb)DT\_INST\_NODE\_HAS\_PROP

| #define DT\_INST\_NODE\_HAS\_PROP | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop)

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)

#define DT\_NODE\_HAS\_PROP(node\_id, prop)

Does a devicetree node have a property?

**Definition** devicetree.h:3784

Does a DT\_DRV\_COMPAT instance have a property?

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |

Returns
:   1 if the instance has the property, 0 otherwise.

## [◆ ](#gaabb1a53b444221d82d865ec8d23c8278)DT\_INST\_NODELABEL\_STRING\_ARRAY

| #define DT\_INST\_NODELABEL\_STRING\_ARRAY | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_NODELABEL\_STRING\_ARRAY](group__devicetree-generic-id.md#ga0114cbfa3a2075558769d4632b7bb1e9)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_NODELABEL\_STRING\_ARRAY](group__devicetree-generic-id.md#ga0114cbfa3a2075558769d4632b7bb1e9)

#define DT\_NODELABEL\_STRING\_ARRAY(node\_id)

Get a devicetree node's node labels as an array of strings.

**Definition** devicetree.h:719

Get a string array of [DT\_DRV\_INST(inst)](#ga219f413efba2f4c0151468b9a25a8dc1)'s node labels.

Equivalent to [DT\_NODELABEL\_STRING\_ARRAY(DT\_DRV\_INST(inst))](group__devicetree-generic-id.md#ga0114cbfa3a2075558769d4632b7bb1e9 "Get a devicetree node's node labels as an array of strings.").

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   an array initializer for an array of the instance's node labels as strings

## [◆ ](#ga446d4b9c267e7c9da73dfb8a07701f2a)DT\_INST\_NUM\_IRQS

| #define DT\_INST\_NUM\_IRQS | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_NUM\_IRQS](group__devicetree-interrupts-prop.md#ga2985e5d55d2d9dbbbe93ba855d5db320)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_NUM\_IRQS](group__devicetree-interrupts-prop.md#ga2985e5d55d2d9dbbbe93ba855d5db320)

#define DT\_NUM\_IRQS(node\_id)

Get the number of interrupt sources for the node.

**Definition** devicetree.h:2560

Get a DT\_DRV\_COMPAT's number of interrupts.

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   number of interrupts

## [◆ ](#ga2c43ec7309f5cdf8139a8b5fab63f786)DT\_INST\_NUM\_NODELABELS

| #define DT\_INST\_NUM\_NODELABELS | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_NUM\_NODELABELS](group__devicetree-interrupts-prop.md#ga7b63eb05db40d7b95ccb62a9fd1f4404)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_NUM\_NODELABELS](group__devicetree-interrupts-prop.md#ga7b63eb05db40d7b95ccb62a9fd1f4404)

#define DT\_NUM\_NODELABELS(node\_id)

Get the number of node labels that a node has.

**Definition** devicetree.h:2586

Get the number of node labels by instance number.

Equivalent to [DT\_NUM\_NODELABELS(DT\_DRV\_INST(inst))](group__devicetree-interrupts-prop.md#ga7b63eb05db40d7b95ccb62a9fd1f4404 "Get the number of node labels that a node has.").

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   the number of node labels that the node with that instance number has

## [◆ ](#ga7a29bda946b399a7af92ec9cd09b4e98)DT\_INST\_ON\_BUS

| #define DT\_INST\_ON\_BUS | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *bus* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_ON\_BUS](group__devicetree-generic-bus.md#gabe5eea44ff838c11dc5b75f9ec2a9317)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), bus)

[DT\_ON\_BUS](group__devicetree-generic-bus.md#gabe5eea44ff838c11dc5b75f9ec2a9317)

#define DT\_ON\_BUS(node\_id, bus)

Is a node on a bus of a given type?

**Definition** devicetree.h:3891

Test if a DT\_DRV\_COMPAT's bus type is a given type.

Parameters
:   | inst | instance number |
    | --- | --- |
    | bus | a binding's bus type as a C token, lowercased and without quotes |

Returns
:   1 if the given instance is on a bus of the given type, 0 otherwise

## [◆ ](#ga176760ce1a019020b5465eebd4f44ff5)DT\_INST\_PARENT

| #define DT\_INST\_PARENT | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PARENT](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_PARENT](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b)

#define DT\_PARENT(node\_id)

Get a node identifier for a parent node.

**Definition** devicetree.h:374

Get a DT\_DRV\_COMPAT parent's node identifier.

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   a node identifier for the instance's parent

See also
:   [DT\_PARENT](group__devicetree-generic-id.md#ga3ac56d491510275ee1321446796ab63b "Get a node identifier for a parent node.")

## [◆ ](#ga0de189f14fa7dd38a99382b7f2adbff8)DT\_INST\_PHA

| #define DT\_INST\_PHA | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *pha*, |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_INST\_PHA\_BY\_IDX](#gaac886e11906d628acad1d73ed3a64018)(inst, pha, 0, cell)

[DT\_INST\_PHA\_BY\_IDX](#gaac886e11906d628acad1d73ed3a64018)

#define DT\_INST\_PHA\_BY\_IDX(inst, pha, idx, cell)

Get a DT\_DRV\_COMPAT instance's phandle-array specifier value at an index.

**Definition** devicetree.h:4346

Get a DT\_DRV\_COMPAT instance's phandle-array specifier value Equivalent to [DT\_INST\_PHA\_BY\_IDX(inst, pha, 0, cell)](#gaac886e11906d628acad1d73ed3a64018).

Parameters
:   | inst | instance number |
    | --- | --- |
    | pha | lowercase-and-underscores property with type phandle-array |
    | cell | binding's cell name for the specifier at `pha` index 0 |

Returns
:   the cell value

## [◆ ](#gaac886e11906d628acad1d73ed3a64018)DT\_INST\_PHA\_BY\_IDX

| #define DT\_INST\_PHA\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *pha*, |
|  |  |  | *idx*, |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), pha, idx, cell)

[DT\_PHA\_BY\_IDX](group__devicetree-generic-prop.md#ga118b63fd22c20ef940ac2fa073c126ed)

#define DT\_PHA\_BY\_IDX(node\_id, pha, idx, cell)

Get a phandle-array specifier cell value at an index.

**Definition** devicetree.h:1564

Get a DT\_DRV\_COMPAT instance's phandle-array specifier value at an index.

Parameters
:   | inst | instance number |
    | --- | --- |
    | pha | lowercase-and-underscores property with type phandle-array |
    | idx | logical index into the property `pha` |
    | cell | binding's cell name within the specifier at index `idx` |

Returns
:   the value of the cell inside the specifier at index `idx`

## [◆ ](#ga3db4c00e072bd93fa92e36907b2b5e86)DT\_INST\_PHA\_BY\_IDX\_OR

| #define DT\_INST\_PHA\_BY\_IDX\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *pha*, |
|  |  |  | *idx*, |
|  |  |  | *cell*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PHA\_BY\_IDX\_OR](group__devicetree-generic-prop.md#gad830ed96dbc4f7dac3455153e0a944d6)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), pha, idx, cell, default\_value)

[DT\_PHA\_BY\_IDX\_OR](group__devicetree-generic-prop.md#gad830ed96dbc4f7dac3455153e0a944d6)

#define DT\_PHA\_BY\_IDX\_OR(node\_id, pha, idx, cell, default\_value)

Like DT\_PHA\_BY\_IDX(), but with a fallback to default\_value.

**Definition** devicetree.h:1590

Like [DT\_INST\_PHA\_BY\_IDX()](#gaac886e11906d628acad1d73ed3a64018), but with a fallback to default\_value.

Parameters
:   | inst | instance number |
    | --- | --- |
    | pha | lowercase-and-underscores property with type phandle-array |
    | idx | logical index into the property `pha` |
    | cell | binding's cell name within the specifier at index `idx` |
    | default\_value | a fallback value to expand to |

Returns
:   [DT\_INST\_PHA\_BY\_IDX(inst, pha, idx, cell)](#gaac886e11906d628acad1d73ed3a64018) or default\_value

## [◆ ](#ga25418914c5190df10c842744aa967dc8)DT\_INST\_PHA\_BY\_NAME

| #define DT\_INST\_PHA\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *pha*, |
|  |  |  | *name*, |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PHA\_BY\_NAME](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), pha, name, cell)

[DT\_PHA\_BY\_NAME](group__devicetree-generic-prop.md#gae469615356a867c49416da15bdc44a26)

#define DT\_PHA\_BY\_NAME(node\_id, pha, name, cell)

Get a value within a phandle-array specifier by name.

**Definition** devicetree.h:1659

Get a DT\_DRV\_COMPAT instance's value within a phandle-array specifier by name.

Parameters
:   | inst | instance number |
    | --- | --- |
    | pha | lowercase-and-underscores property with type phandle-array |
    | name | lowercase-and-underscores name of a specifier in `pha` |
    | cell | binding's cell name for the named specifier |

Returns
:   the cell value

## [◆ ](#gaaebc5c643b60319f7e767e46ca226729)DT\_INST\_PHA\_BY\_NAME\_OR

| #define DT\_INST\_PHA\_BY\_NAME\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *pha*, |
|  |  |  | *name*, |
|  |  |  | *cell*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PHA\_BY\_NAME\_OR](group__devicetree-generic-prop.md#ga79cda6ca70cc1e27b034ad096d4f4401)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), pha, name, cell, default\_value)

[DT\_PHA\_BY\_NAME\_OR](group__devicetree-generic-prop.md#ga79cda6ca70cc1e27b034ad096d4f4401)

#define DT\_PHA\_BY\_NAME\_OR(node\_id, pha, name, cell, default\_value)

Like DT\_PHA\_BY\_NAME(), but with a fallback to default\_value.

**Definition** devicetree.h:1683

Like [DT\_INST\_PHA\_BY\_NAME()](#ga25418914c5190df10c842744aa967dc8), but with a fallback to default\_value.

Parameters
:   | inst | instance number |
    | --- | --- |
    | pha | lowercase-and-underscores property with type phandle-array |
    | name | lowercase-and-underscores name of a specifier in `pha` |
    | cell | binding's cell name for the named specifier |
    | default\_value | a fallback value to expand to |

Returns
:   [DT\_INST\_PHA\_BY\_NAME(inst, pha, name, cell)](#ga25418914c5190df10c842744aa967dc8) or default\_value

## [◆ ](#gab8083dae430aeb93a967bbf98aa9eefc)DT\_INST\_PHA\_HAS\_CELL

| #define DT\_INST\_PHA\_HAS\_CELL | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *pha*, |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_INST\_PHA\_HAS\_CELL\_AT\_IDX](#gae054b89701ec9fae577320fb7b9cae1e)(inst, pha, 0, cell)

[DT\_INST\_PHA\_HAS\_CELL\_AT\_IDX](#gae054b89701ec9fae577320fb7b9cae1e)

#define DT\_INST\_PHA\_HAS\_CELL\_AT\_IDX(inst, pha, idx, cell)

Does a phandle array have a named cell specifier at an index for a DT\_DRV\_COMPAT instance?

**Definition** devicetree.h:5129

Does a phandle array have a named cell specifier at index 0 for a DT\_DRV\_COMPAT instance?

Parameters
:   | inst | instance number |
    | --- | --- |
    | pha | lowercase-and-underscores property with type phandle-array |
    | cell | named cell value whose existence to check |

Returns
:   1 if the named `cell` exists in the specifier at index 0, 0 otherwise.

## [◆ ](#gae054b89701ec9fae577320fb7b9cae1e)DT\_INST\_PHA\_HAS\_CELL\_AT\_IDX

| #define DT\_INST\_PHA\_HAS\_CELL\_AT\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *pha*, |
|  |  |  | *idx*, |
|  |  |  | *cell* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PHA\_HAS\_CELL\_AT\_IDX](group__devicetree-generic-exist.md#gacfbd6a2cb3038e5aba1e2216d65ebc78)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), pha, idx, cell)

[DT\_PHA\_HAS\_CELL\_AT\_IDX](group__devicetree-generic-exist.md#gacfbd6a2cb3038e5aba1e2216d65ebc78)

#define DT\_PHA\_HAS\_CELL\_AT\_IDX(node\_id, pha, idx, cell)

Does a phandle array have a named cell specifier at an index?

**Definition** devicetree.h:3804

Does a phandle array have a named cell specifier at an index for a DT\_DRV\_COMPAT instance?

Parameters
:   | inst | instance number |
    | --- | --- |
    | pha | lowercase-and-underscores property with type phandle-array |
    | idx | index to check |
    | cell | named cell value whose existence to check |

Returns
:   1 if the named `cell` exists in the specifier at index `idx`, 0 otherwise.

## [◆ ](#ga491ad421602e41c4295bac61b595fc94)DT\_INST\_PHA\_OR

| #define DT\_INST\_PHA\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *pha*, |
|  |  |  | *cell*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_INST\_PHA\_BY\_IDX\_OR](#ga3db4c00e072bd93fa92e36907b2b5e86)(inst, pha, 0, cell, default\_value)

[DT\_INST\_PHA\_BY\_IDX\_OR](#ga3db4c00e072bd93fa92e36907b2b5e86)

#define DT\_INST\_PHA\_BY\_IDX\_OR(inst, pha, idx, cell, default\_value)

Like DT\_INST\_PHA\_BY\_IDX(), but with a fallback to default\_value.

**Definition** devicetree.h:4358

Like [DT\_INST\_PHA()](#ga0de189f14fa7dd38a99382b7f2adbff8), but with a fallback to default\_value.

Parameters
:   | inst | instance number |
    | --- | --- |
    | pha | lowercase-and-underscores property with type phandle-array |
    | cell | binding's cell name for the specifier at `pha` index 0 |
    | default\_value | a fallback value to expand to |

Returns
:   [DT\_INST\_PHA(inst, pha, cell)](#ga0de189f14fa7dd38a99382b7f2adbff8) or default\_value

## [◆ ](#ga81c10f478c86e5a4c18eb7a990447137)DT\_INST\_PHANDLE

| #define DT\_INST\_PHANDLE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_INST\_PHANDLE\_BY\_IDX](#ga10d93a1f9a9f5e225508c4c383654b1c)(inst, prop, 0)

[DT\_INST\_PHANDLE\_BY\_IDX](#ga10d93a1f9a9f5e225508c4c383654b1c)

#define DT\_INST\_PHANDLE\_BY\_IDX(inst, prop, idx)

Get a DT\_DRV\_COMPAT instance's node identifier for a phandle in a property.

**Definition** devicetree.h:4426

Get a DT\_DRV\_COMPAT instance's node identifier for a phandle property's value.

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property of `inst` with type phandle |

Returns
:   a node identifier for the node pointed to by "ph"

## [◆ ](#ga10d93a1f9a9f5e225508c4c383654b1c)DT\_INST\_PHANDLE\_BY\_IDX

| #define DT\_INST\_PHANDLE\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, idx)

[DT\_PHANDLE\_BY\_IDX](group__devicetree-generic-prop.md#ga8ff163c240878a988d29d727671671de)

#define DT\_PHANDLE\_BY\_IDX(node\_id, prop, idx)

Get a node identifier for a phandle in a property.

**Definition** devicetree.h:1785

Get a DT\_DRV\_COMPAT instance's node identifier for a phandle in a property.

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name in `inst` with type phandle, phandles or phandle-array |
    | idx | index into `prop` |

Returns
:   a node identifier for the phandle at index `idx` in `prop`

## [◆ ](#ga64d8ddaad8b2d3852e30686d3adf6551)DT\_INST\_PHANDLE\_BY\_NAME

| #define DT\_INST\_PHANDLE\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *pha*, |
|  |  |  | *name* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), pha, name) \

[DT\_PHANDLE\_BY\_NAME](group__devicetree-generic-prop.md#ga65c90d2d96255b8569c5b869b637c2fd)

#define DT\_PHANDLE\_BY\_NAME(node\_id, pha, name)

Get a phandle's node identifier from a phandle array by name.

**Definition** devicetree.h:1733

Get a DT\_DRV\_COMPAT instance's phandle node identifier from a phandle array by name.

Parameters
:   | inst | instance number |
    | --- | --- |
    | pha | lowercase-and-underscores property with type phandle-array |
    | name | lowercase-and-underscores name of an element in `pha` |

Returns
:   node identifier for the phandle at the element named "name"

## [◆ ](#ga9dce2e631b2a94804e8f2bcc76c6eff8)DT\_INST\_PROP

| #define DT\_INST\_PROP | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop)

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:762

Get a DT\_DRV\_COMPAT instance property.

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |

Returns
:   a representation of the property's value

## [◆ ](#ga5b60f4ed4f5dadc5dd425f5905f23b00)DT\_INST\_PROP\_BY\_IDX

| #define DT\_INST\_PROP\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, idx)

[DT\_PROP\_BY\_IDX](group__devicetree-generic-prop.md#ga52ad691ea4cae633ca702020e939d461)

#define DT\_PROP\_BY\_IDX(node\_id, prop, idx)

Get the value at index idx in an array type property.

**Definition** devicetree.h:908

Get a DT\_DRV\_COMPAT element value in an array property.

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | idx | the index to get |

Returns
:   a representation of the idx-th element of the property

## [◆ ](#ga1f26b1c5b6c7a8c3c02c09d72a00afa5)DT\_INST\_PROP\_BY\_PHANDLE

| #define DT\_INST\_PROP\_BY\_PHANDLE | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *ph*, |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_INST\_PROP\_BY\_PHANDLE\_IDX](#gad027963bdf159942cf6fb28b04e8d48e)(inst, ph, 0, prop)

[DT\_INST\_PROP\_BY\_PHANDLE\_IDX](#gad027963bdf159942cf6fb28b04e8d48e)

#define DT\_INST\_PROP\_BY\_PHANDLE\_IDX(inst, phs, idx, prop)

Get a DT\_DRV\_COMPAT instance's property value from a phandle in a property.

**Definition** devicetree.h:4335

Get a DT\_DRV\_COMPAT instance's property value from a phandle's node.

Parameters
:   | inst | instance number |
    | --- | --- |
    | ph | lowercase-and-underscores property of `inst` with type phandle |
    | prop | lowercase-and-underscores property of the phandle's node |

Returns
:   the value of `prop` as described in the [DT\_PROP()](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b "Get a devicetree property value.") documentation

## [◆ ](#gad027963bdf159942cf6fb28b04e8d48e)DT\_INST\_PROP\_BY\_PHANDLE\_IDX

| #define DT\_INST\_PROP\_BY\_PHANDLE\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *phs*, |
|  |  |  | *idx*, |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PROP\_BY\_PHANDLE\_IDX](group__devicetree-generic-prop.md#gaeba973992914d493cff5506ecf86a00d)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), phs, idx, prop)

[DT\_PROP\_BY\_PHANDLE\_IDX](group__devicetree-generic-prop.md#gaeba973992914d493cff5506ecf86a00d)

#define DT\_PROP\_BY\_PHANDLE\_IDX(node\_id, phs, idx, prop)

Get a property value from a phandle in a property.

**Definition** devicetree.h:1471

Get a DT\_DRV\_COMPAT instance's property value from a phandle in a property.

Parameters
:   | inst | instance number |
    | --- | --- |
    | phs | lowercase-and-underscores property with type phandle, phandles, or phandle-array |
    | idx | logical index into "phs", which must be zero if "phs" has type phandle |
    | prop | lowercase-and-underscores property of the phandle's node |

Returns
:   the value of `prop` as described in the [DT\_PROP()](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b "Get a devicetree property value.") documentation

## [◆ ](#ga2c51745f8d51b1d9cdfb1cde69911d48)DT\_INST\_PROP\_HAS\_IDX

| #define DT\_INST\_PROP\_HAS\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PROP\_HAS\_IDX](group__devicetree-generic-prop.md#ga479dfc704087eea7e7c5af42ae98576c)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, idx)

[DT\_PROP\_HAS\_IDX](group__devicetree-generic-prop.md#ga479dfc704087eea7e7c5af42ae98576c)

#define DT\_PROP\_HAS\_IDX(node\_id, prop, idx)

Is index idx valid for an array type property?

**Definition** devicetree.h:836

Is index `idx` valid for an array type property on a DT\_DRV\_COMPAT instance?

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | idx | index to check |

Returns
:   1 if `idx` is a valid index into the given property, 0 otherwise.

## [◆ ](#ga75e13dcdbcc51da1334fa14653411dd8)DT\_INST\_PROP\_HAS\_NAME

| #define DT\_INST\_PROP\_HAS\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *name* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PROP\_HAS\_NAME](group__devicetree-generic-prop.md#gae46c100aecd299eaea51e033890d9a58)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, name)

[DT\_PROP\_HAS\_NAME](group__devicetree-generic-prop.md#gae46c100aecd299eaea51e033890d9a58)

#define DT\_PROP\_HAS\_NAME(node\_id, prop, name)

Is name name available in a foo-names property?

**Definition** devicetree.h:871

Is name `name` available in a foo-names property?

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | a lowercase-and-underscores prop-names type property |
    | name | a lowercase-and-underscores name to check |

Returns
:   An expression which evaluates to 1 if `name` is an available name into the given property, and 0 otherwise.

## [◆ ](#ga9471df75ff3c4f8d2298bb69c581b365)DT\_INST\_PROP\_LEN

| #define DT\_INST\_PROP\_LEN | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PROP\_LEN](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop)

[DT\_PROP\_LEN](group__devicetree-generic-prop.md#gaa7f5afcedd1f54be79a5337e8e28a5b6)

#define DT\_PROP\_LEN(node\_id, prop)

Get a property's logical length.

**Definition** devicetree.h:796

Get a DT\_DRV\_COMPAT property length.

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |

Returns
:   logical length of the property

## [◆ ](#ga9be8fdcc8c4032748b47f497efa19173)DT\_INST\_PROP\_LEN\_OR

| #define DT\_INST\_PROP\_LEN\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PROP\_LEN\_OR](group__devicetree-generic-prop.md#gabd2d8a9242818c7a9bf981114c912d75)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, default\_value)

[DT\_PROP\_LEN\_OR](group__devicetree-generic-prop.md#gabd2d8a9242818c7a9bf981114c912d75)

#define DT\_PROP\_LEN\_OR(node\_id, prop, default\_value)

Like DT\_PROP\_LEN(), but with a fallback to default\_value.

**Definition** devicetree.h:812

Like [DT\_INST\_PROP\_LEN()](#ga9471df75ff3c4f8d2298bb69c581b365), but with a fallback to `default_value`.

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | default\_value | a fallback value to expand to |

Returns
:   [DT\_INST\_PROP\_LEN(inst, prop)](#ga9471df75ff3c4f8d2298bb69c581b365) or `default_value`

## [◆ ](#gaa51bd8f5b016244e0256b3ed9aceee7f)DT\_INST\_PROP\_OR

| #define DT\_INST\_PROP\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, default\_value)

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)

#define DT\_PROP\_OR(node\_id, prop, default\_value)

Like DT\_PROP(), but with a fallback to default\_value.

**Definition** devicetree.h:935

Like [DT\_INST\_PROP()](#ga9dce2e631b2a94804e8f2bcc76c6eff8), but with a fallback to `default_value`.

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | default\_value | a fallback value to expand to |

Returns
:   [DT\_INST\_PROP(inst, prop)](#ga9dce2e631b2a94804e8f2bcc76c6eff8) or `default_value`

## [◆ ](#gafde8fa67b94ac959ba2e24b44b3386a7)DT\_INST\_REG\_ADDR

| #define DT\_INST\_REG\_ADDR | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_INST\_REG\_ADDR\_BY\_IDX](#ga0fe0403821883598da6cfad4f3962115)(inst, 0)

[DT\_INST\_REG\_ADDR\_BY\_IDX](#ga0fe0403821883598da6cfad4f3962115)

#define DT\_INST\_REG\_ADDR\_BY\_IDX(inst, idx)

Get a DT\_DRV\_COMPAT instance's idx-th register block's address.

**Definition** devicetree.h:4471

Get a DT\_DRV\_COMPAT's (only) register block address.

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   instance's register block address

## [◆ ](#ga0fe0403821883598da6cfad4f3962115)DT\_INST\_REG\_ADDR\_BY\_IDX

| #define DT\_INST\_REG\_ADDR\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_REG\_ADDR\_BY\_IDX](group__devicetree-reg-prop.md#gac540b00bb12d0662f6aefe6ac0cff243)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

[DT\_REG\_ADDR\_BY\_IDX](group__devicetree-reg-prop.md#gac540b00bb12d0662f6aefe6ac0cff243)

#define DT\_REG\_ADDR\_BY\_IDX(node\_id, idx)

Get the base address of the register block at index idx.

**Definition** devicetree.h:2437

Get a DT\_DRV\_COMPAT instance's idx-th register block's address.

Parameters
:   | inst | instance number |
    | --- | --- |
    | idx | index of the register whose address to return |

Returns
:   address of the instance's idx-th register block

## [◆ ](#gade870f8f5c78c3c6244ada35049334a5)DT\_INST\_REG\_ADDR\_BY\_IDX\_RAW

| #define DT\_INST\_REG\_ADDR\_BY\_IDX\_RAW | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_REG\_ADDR\_BY\_IDX\_RAW](group__devicetree-reg-prop.md#ga226e23a6bb94beee690ff6e1cdfbab91)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

[DT\_REG\_ADDR\_BY\_IDX\_RAW](group__devicetree-reg-prop.md#ga226e23a6bb94beee690ff6e1cdfbab91)

#define DT\_REG\_ADDR\_BY\_IDX\_RAW(node\_id, idx)

Get the base raw address of the register block at index idx.

**Definition** devicetree.h:2414

Get a DT\_DRV\_COMPAT instance's idx-th register block's raw address.

Parameters
:   | inst | instance number |
    | --- | --- |
    | idx | index of the register whose address to return |

Returns
:   address of the instance's idx-th register block

## [◆ ](#ga722d6f7b97136aa9229242e4ba7dd25c)DT\_INST\_REG\_ADDR\_BY\_NAME

| #define DT\_INST\_REG\_ADDR\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_REG\_ADDR\_BY\_NAME](group__devicetree-reg-prop.md#gaeb5863e878bbd3a362e17616403da692)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_REG\_ADDR\_BY\_NAME](group__devicetree-reg-prop.md#gaeb5863e878bbd3a362e17616403da692)

#define DT\_REG\_ADDR\_BY\_NAME(node\_id, name)

Get a register block's base address by name.

**Definition** devicetree.h:2490

Get a DT\_DRV\_COMPAT's register block address by name.

Parameters
:   | inst | instance number |
    | --- | --- |
    | name | lowercase-and-underscores register specifier name |

Returns
:   address of the register block with the given `name`

## [◆ ](#gaf8d6ec7f68f566360743f7ea7cb7f8fb)DT\_INST\_REG\_ADDR\_BY\_NAME\_OR

| #define DT\_INST\_REG\_ADDR\_BY\_NAME\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_REG\_ADDR\_BY\_NAME\_OR](group__devicetree-reg-prop.md#ga3f0a35f6b07da983be6fa63bdfb82732)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name, default\_value)

[DT\_REG\_ADDR\_BY\_NAME\_OR](group__devicetree-reg-prop.md#ga3f0a35f6b07da983be6fa63bdfb82732)

#define DT\_REG\_ADDR\_BY\_NAME\_OR(node\_id, name, default\_value)

Like DT\_REG\_ADDR\_BY\_NAME(), but with a fallback to default\_value.

**Definition** devicetree.h:2501

Like [DT\_INST\_REG\_ADDR\_BY\_NAME()](#ga722d6f7b97136aa9229242e4ba7dd25c), but with a fallback to `default_value`.

Parameters
:   | inst | instance number |
    | --- | --- |
    | name | lowercase-and-underscores register specifier name |
    | default\_value | a fallback value to expand to |

Returns
:   address of the register block specified by name if present, `default_value` otherwise

## [◆ ](#ga8af83c4c65e607b93aa60a690295d625)DT\_INST\_REG\_ADDR\_BY\_NAME\_U64

| #define DT\_INST\_REG\_ADDR\_BY\_NAME\_U64 | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_REG\_ADDR\_BY\_NAME\_U64](group__devicetree-reg-prop.md#gaf03f1b5518ff146d6de986f867fcc2c8)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_REG\_ADDR\_BY\_NAME\_U64](group__devicetree-reg-prop.md#gaf03f1b5518ff146d6de986f867fcc2c8)

#define DT\_REG\_ADDR\_BY\_NAME\_U64(node\_id, name)

64-bit version of DT\_REG\_ADDR\_BY\_NAME()

**Definition** devicetree.h:2517

64-bit version of [DT\_INST\_REG\_ADDR\_BY\_NAME()](#ga722d6f7b97136aa9229242e4ba7dd25c)

This macro version adds the appropriate suffix for 64-bit unsigned integer literals. Note that this macro is equivalent to [DT\_INST\_REG\_ADDR\_BY\_NAME()](#ga722d6f7b97136aa9229242e4ba7dd25c) in linker/ASM context.

Parameters
:   | inst | instance number |
    | --- | --- |
    | name | lowercase-and-underscores register specifier name |

Returns
:   address of the register block with the given `name`

## [◆ ](#ga79627566ff2486cfd2425a04974d71a3)DT\_INST\_REG\_ADDR\_RAW

| #define DT\_INST\_REG\_ADDR\_RAW | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_INST\_REG\_ADDR\_BY\_IDX\_RAW](#gade870f8f5c78c3c6244ada35049334a5)(inst, 0)

[DT\_INST\_REG\_ADDR\_BY\_IDX\_RAW](#gade870f8f5c78c3c6244ada35049334a5)

#define DT\_INST\_REG\_ADDR\_BY\_IDX\_RAW(inst, idx)

Get a DT\_DRV\_COMPAT instance's idx-th register block's raw address.

**Definition** devicetree.h:4463

Get a DT\_DRV\_COMPAT's (only) register block raw address.

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   instance's register block address

## [◆ ](#gaba47dcabd8754eda87e35efd7289f976)DT\_INST\_REG\_ADDR\_U64

| #define DT\_INST\_REG\_ADDR\_U64 | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_REG\_ADDR\_U64](group__devicetree-reg-prop.md#gaf77354db552821a865b93f709b25e410)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[DT\_REG\_ADDR\_U64](group__devicetree-reg-prop.md#gaf77354db552821a865b93f709b25e410)

#define DT\_REG\_ADDR\_U64(node\_id)

64-bit version of DT\_REG\_ADDR()

**Definition** devicetree.h:2473

64-bit version of [DT\_INST\_REG\_ADDR()](#gafde8fa67b94ac959ba2e24b44b3386a7)

This macro version adds the appropriate suffix for 64-bit unsigned integer literals. Note that this macro is equivalent to [DT\_INST\_REG\_ADDR()](#gafde8fa67b94ac959ba2e24b44b3386a7) in linker/ASM context.

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   instance's register block address

## [◆ ](#ga26bbff9ebaed549140d2530a0b99e8a4)DT\_INST\_REG\_HAS\_IDX

| #define DT\_INST\_REG\_HAS\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_REG\_HAS\_IDX](group__devicetree-reg-prop.md#ga59aa43231678d08eeac6e5b344048f02)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

[DT\_REG\_HAS\_IDX](group__devicetree-reg-prop.md#ga59aa43231678d08eeac6e5b344048f02)

#define DT\_REG\_HAS\_IDX(node\_id, idx)

Is idx a valid register block index?

**Definition** devicetree.h:2386

is `idx` a valid register block index on a DT\_DRV\_COMPAT instance?

Parameters
:   | inst | instance number |
    | --- | --- |
    | idx | index to check |

Returns
:   1 if `idx` is a valid register block index, 0 otherwise.

## [◆ ](#ga8b15b84b03c3dc6fd9d7e127a44392b3)DT\_INST\_REG\_HAS\_NAME

| #define DT\_INST\_REG\_HAS\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_REG\_HAS\_NAME](group__devicetree-reg-prop.md#ga2c68672c60d95725b69371c3ab306d24)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_REG\_HAS\_NAME](group__devicetree-reg-prop.md#ga2c68672c60d95725b69371c3ab306d24)

#define DT\_REG\_HAS\_NAME(node\_id, name)

Is name a valid register block name?

**Definition** devicetree.h:2400

is `name` a valid register block name on a DT\_DRV\_COMPAT instance?

Parameters
:   | inst | instance number |
    | --- | --- |
    | name | name to check |

Returns
:   1 if `name` is a valid register block name, 0 otherwise.

## [◆ ](#gaa7cea29435e1db59470302abb5ee88dd)DT\_INST\_REG\_SIZE

| #define DT\_INST\_REG\_SIZE | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_INST\_REG\_SIZE\_BY\_IDX](#gab1152c9f069c69b0269c1a4e744b9dd9)(inst, 0)

[DT\_INST\_REG\_SIZE\_BY\_IDX](#gab1152c9f069c69b0269c1a4e744b9dd9)

#define DT\_INST\_REG\_SIZE\_BY\_IDX(inst, idx)

Get a DT\_DRV\_COMPAT instance's idx-th register block's size.

**Definition** devicetree.h:4479

Get a DT\_DRV\_COMPAT's (only) register block size.

Parameters
:   | inst | instance number |
    | --- | --- |

Returns
:   instance's register block size

## [◆ ](#gab1152c9f069c69b0269c1a4e744b9dd9)DT\_INST\_REG\_SIZE\_BY\_IDX

| #define DT\_INST\_REG\_SIZE\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_REG\_SIZE\_BY\_IDX](group__devicetree-reg-prop.md#ga9a703d688e4b983689b8579e0e7d9f48)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), idx)

[DT\_REG\_SIZE\_BY\_IDX](group__devicetree-reg-prop.md#ga9a703d688e4b983689b8579e0e7d9f48)

#define DT\_REG\_SIZE\_BY\_IDX(node\_id, idx)

Get the size of the register block at index idx.

**Definition** devicetree.h:2451

Get a DT\_DRV\_COMPAT instance's idx-th register block's size.

Parameters
:   | inst | instance number |
    | --- | --- |
    | idx | index of the register whose size to return |

Returns
:   size of the instance's idx-th register block

## [◆ ](#gaf82457c5dcfef7eeba074afb95d48714)DT\_INST\_REG\_SIZE\_BY\_NAME

| #define DT\_INST\_REG\_SIZE\_BY\_NAME | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_REG\_SIZE\_BY\_NAME](group__devicetree-reg-prop.md#ga042988feb27e58989baa7abb4930409e)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name)

[DT\_REG\_SIZE\_BY\_NAME](group__devicetree-reg-prop.md#ga042988feb27e58989baa7abb4930409e)

#define DT\_REG\_SIZE\_BY\_NAME(node\_id, name)

Get a register block's size by name.

**Definition** devicetree.h:2526

Get a DT\_DRV\_COMPAT's register block size by name.

Parameters
:   | inst | instance number |
    | --- | --- |
    | name | lowercase-and-underscores register specifier name |

Returns
:   size of the register block with the given `name`

## [◆ ](#ga8494b94b6dbec875eba61e10f269cce6)DT\_INST\_REG\_SIZE\_BY\_NAME\_OR

| #define DT\_INST\_REG\_SIZE\_BY\_NAME\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_REG\_SIZE\_BY\_NAME\_OR](group__devicetree-reg-prop.md#ga823daf216d17b80f4d049c75358078ed)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name, default\_value)

[DT\_REG\_SIZE\_BY\_NAME\_OR](group__devicetree-reg-prop.md#ga823daf216d17b80f4d049c75358078ed)

#define DT\_REG\_SIZE\_BY\_NAME\_OR(node\_id, name, default\_value)

Like DT\_REG\_SIZE\_BY\_NAME(), but with a fallback to default\_value.

**Definition** devicetree.h:2537

Like [DT\_INST\_REG\_SIZE\_BY\_NAME()](#gaf82457c5dcfef7eeba074afb95d48714), but with a fallback to `default_value`.

Parameters
:   | inst | instance number |
    | --- | --- |
    | name | lowercase-and-underscores register specifier name |
    | default\_value | a fallback value to expand to |

Returns
:   size of the register block specified by name if present, `default_value` otherwise

## [◆ ](#ga8e8c72187ce0d47fd24e4585f3d48484)DT\_INST\_STRING\_TOKEN

| #define DT\_INST\_STRING\_TOKEN | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_STRING\_TOKEN](group__devicetree-generic-prop.md#ga5995350cc7fd2d12ef7daa2487d1db54)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop)

[DT\_STRING\_TOKEN](group__devicetree-generic-prop.md#ga5995350cc7fd2d12ef7daa2487d1db54)

#define DT\_STRING\_TOKEN(node\_id, prop)

Get a string property's value as a token.

**Definition** devicetree.h:1116

Get a DT\_DRV\_COMPAT instance's string property's value as a token.

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |

Returns
:   the value of `prop` as a token, i.e. without any quotes and with special characters converted to underscores

## [◆ ](#gae1c28cbd9c1869112d2ae5c7ddf00b97)DT\_INST\_STRING\_TOKEN\_BY\_IDX

| #define DT\_INST\_STRING\_TOKEN\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_STRING\_TOKEN\_BY\_IDX](group__devicetree-generic-prop.md#ga583e5e2e3c897f1095073e6192061d3a)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, idx)

[DT\_STRING\_TOKEN\_BY\_IDX](group__devicetree-generic-prop.md#ga583e5e2e3c897f1095073e6192061d3a)

#define DT\_STRING\_TOKEN\_BY\_IDX(node\_id, prop, idx)

Get an element out of a string-array property as a token.

**Definition** devicetree.h:1322

Get an element out of string-array property as a token.

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | idx | the index to get |

Returns
:   the element in `prop` at index `idx` as a token

## [◆ ](#ga79fd00d1ece5538f7705c241ab869ea8)DT\_INST\_STRING\_TOKEN\_OR

| #define DT\_INST\_STRING\_TOKEN\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_STRING\_TOKEN\_OR](group__devicetree-generic-prop.md#ga5c7c7f82abd34403d4e9a6e0c5703e4c)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name, default\_value)

[DT\_STRING\_TOKEN\_OR](group__devicetree-generic-prop.md#ga5c7c7f82abd34403d4e9a6e0c5703e4c)

#define DT\_STRING\_TOKEN\_OR(node\_id, prop, default\_value)

Like DT\_STRING\_TOKEN(), but with a fallback to default\_value.

**Definition** devicetree.h:1132

Like [DT\_INST\_STRING\_TOKEN()](#ga8e8c72187ce0d47fd24e4585f3d48484), but with a fallback to `default_value`.

Parameters
:   | inst | instance number |
    | --- | --- |
    | name | lowercase-and-underscores property name |
    | default\_value | a fallback value to expand to |

Returns
:   if `prop` exists, its value as a token, i.e. without any quotes and with special characters converted to underscores. Otherwise `default_value`

## [◆ ](#ga1c4fc4c808113cb6e0d7b54af9869228)DT\_INST\_STRING\_UNQUOTED

| #define DT\_INST\_STRING\_UNQUOTED | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_STRING\_UNQUOTED](group__devicetree-generic-prop.md#gad71ae303ce20e116a75c23ca552c2225)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop)

[DT\_STRING\_UNQUOTED](group__devicetree-generic-prop.md#gad71ae303ce20e116a75c23ca552c2225)

#define DT\_STRING\_UNQUOTED(node\_id, prop)

Get a string property's value as an unquoted sequence of tokens.

**Definition** devicetree.h:1254

Get a DT\_DRV\_COMPAT instance's string property's value as an unquoted sequence of tokens.

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |

Returns
:   the value of `prop` as a sequence of tokens, with no quotes

## [◆ ](#gac5768077e2a3d14a69efc653cfc59d5d)DT\_INST\_STRING\_UNQUOTED\_BY\_IDX

| #define DT\_INST\_STRING\_UNQUOTED\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_STRING\_UNQUOTED\_BY\_IDX](group__devicetree-generic-prop.md#ga3736709d70fdcb00bf305fd500f9ab64)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, idx)

[DT\_STRING\_UNQUOTED\_BY\_IDX](group__devicetree-generic-prop.md#ga3736709d70fdcb00bf305fd500f9ab64)

#define DT\_STRING\_UNQUOTED\_BY\_IDX(node\_id, prop, idx)

Get a string array item value as an unquoted sequence of tokens.

**Definition** devicetree.h:1415

Get an element out of string-array property as an unquoted sequence of tokens.

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | idx | the index to get |

Returns
:   the value of `prop` at index `idx` as a sequence of tokens, with no quotes

## [◆ ](#ga56bc0c0a46f6be421082119604cde643)DT\_INST\_STRING\_UNQUOTED\_OR

| #define DT\_INST\_STRING\_UNQUOTED\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_STRING\_UNQUOTED\_OR](group__devicetree-generic-prop.md#gad9fefdcc15e991ba526300cd20f7c2fa)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name, default\_value)

[DT\_STRING\_UNQUOTED\_OR](group__devicetree-generic-prop.md#gad9fefdcc15e991ba526300cd20f7c2fa)

#define DT\_STRING\_UNQUOTED\_OR(node\_id, prop, default\_value)

Like DT\_STRING\_UNQUOTED(), but with a fallback to default\_value.

**Definition** devicetree.h:1271

Like [DT\_INST\_STRING\_UNQUOTED()](#ga1c4fc4c808113cb6e0d7b54af9869228), but with a fallback to `default_value`.

Parameters
:   | inst | instance number |
    | --- | --- |
    | name | lowercase-and-underscores property name |
    | default\_value | a fallback value to expand to |

Returns
:   the property's value as a sequence of tokens, with no quotes, or `default_value`

## [◆ ](#ga0487d19ae023acb9b0eb613317f31aa5)DT\_INST\_STRING\_UPPER\_TOKEN

| #define DT\_INST\_STRING\_UPPER\_TOKEN | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_STRING\_UPPER\_TOKEN](group__devicetree-generic-prop.md#gae0b5e2b6633a98ead17ec20d3494658f)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop)

[DT\_STRING\_UPPER\_TOKEN](group__devicetree-generic-prop.md#gae0b5e2b6633a98ead17ec20d3494658f)

#define DT\_STRING\_UPPER\_TOKEN(node\_id, prop)

Like DT\_STRING\_TOKEN(), but uppercased.

**Definition** devicetree.h:1193

Like [DT\_INST\_STRING\_TOKEN()](#ga8e8c72187ce0d47fd24e4585f3d48484), but uppercased.

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |

Returns
:   the value of `prop` as an uppercased token, i.e. without any quotes and with special characters converted to underscores

## [◆ ](#ga4ceceec8375d70b40a4dec1a8ab5ee29)DT\_INST\_STRING\_UPPER\_TOKEN\_BY\_IDX

| #define DT\_INST\_STRING\_UPPER\_TOKEN\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_STRING\_UPPER\_TOKEN\_BY\_IDX](group__devicetree-generic-prop.md#ga73105b3402fbd6f82274a8b4a2ca6b35)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, idx)

[DT\_STRING\_UPPER\_TOKEN\_BY\_IDX](group__devicetree-generic-prop.md#ga73105b3402fbd6f82274a8b4a2ca6b35)

#define DT\_STRING\_UPPER\_TOKEN\_BY\_IDX(node\_id, prop, idx)

Like DT\_STRING\_TOKEN\_BY\_IDX(), but uppercased.

**Definition** devicetree.h:1372

Like [DT\_INST\_STRING\_TOKEN\_BY\_IDX()](#gae1c28cbd9c1869112d2ae5c7ddf00b97), but uppercased.

Parameters
:   | inst | instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | idx | the index to get |

Returns
:   the element in `prop` at index `idx` as an uppercased token

## [◆ ](#ga72981780b2ede73c49ef9e5a7c6247c2)DT\_INST\_STRING\_UPPER\_TOKEN\_OR

| #define DT\_INST\_STRING\_UPPER\_TOKEN\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *name*, |
|  |  |  | *default\_value* ) |

`#include <[devicetree.h](devicetree_8h.md)>`

**Value:**

[DT\_STRING\_UPPER\_TOKEN\_OR](group__devicetree-generic-prop.md#gab79f5274c82d025d805ec94d2935c9b9)([DT\_DRV\_INST](#ga219f413efba2f4c0151468b9a25a8dc1)(inst), name, default\_value)

[DT\_STRING\_UPPER\_TOKEN\_OR](group__devicetree-generic-prop.md#gab79f5274c82d025d805ec94d2935c9b9)

#define DT\_STRING\_UPPER\_TOKEN\_OR(node\_id, prop, default\_value)

Like DT\_STRING\_UPPER\_TOKEN(), but with a fallback to default\_value.

**Definition** devicetree.h:1210

Like [DT\_INST\_STRING\_UPPER\_TOKEN()](#ga0487d19ae023acb9b0eb613317f31aa5), but with a fallback to `default_value`.

Parameters
:   | inst | instance number |
    | --- | --- |
    | name | lowercase-and-underscores property name |
    | default\_value | a fallback value to expand to |

Returns
:   the property's value as an uppercased token, or `default_value`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
