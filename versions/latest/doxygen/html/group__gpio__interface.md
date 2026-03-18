---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__gpio__interface.html
original_path: doxygen/html/group__gpio__interface.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

GPIO Driver APIs

[Device Driver APIs](group__io__interfaces.md)

GPIO Driver APIs.
[More...](#details)

| Topics | |
| --- | --- |
|  | [Emulated GPIO](group__gpio__emul.md) |
|  | Emulated GPIO backend API. |
|  | [nPM1300-specific GPIO Flags](group__gpio__interface__npm1300.md) |
|  | nPM1300-specific GPIO Flags |
|  | [nPM6001-specific GPIO Flags](group__gpio__interface__npm6001.md) |
|  | nPM6001-specific GPIO Flags |
|  | [nRF-specific GPIO Flags](group__gpio__interface__nrf.md) |
|  | nRF-specific GPIO Flags |

| Data Structures | |
| --- | --- |
| struct | [gpio\_dt\_spec](structgpio__dt__spec.md) |
|  | Container for GPIO pin information specified in devicetree. [More...](structgpio__dt__spec.md#details) |
| struct | [gpio\_driver\_config](structgpio__driver__config.md) |
|  | This structure is common to all GPIO drivers and is expected to be the first element in the object pointed to by the config field in the device structure. [More...](structgpio__driver__config.md#details) |
| struct | [gpio\_driver\_data](structgpio__driver__data.md) |
|  | This structure is common to all GPIO drivers and is expected to be the first element in the driver's struct driver\_data declaration. [More...](structgpio__driver__data.md#details) |
| struct | [gpio\_callback](structgpio__callback.md) |
|  | GPIO callback structure. [More...](structgpio__callback.md#details) |

| Macros | |
| --- | --- |
| #define | [GPIO\_DT\_SPEC\_GET\_BY\_IDX](#gacb1077b77aecf8f1a9c7636ea583c4cf)(node\_id, prop, idx) |
|  | Static initializer for a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")`. |
| #define | [GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR](#ga3db4fa464e191016287f4c4d7eb9a983)(node\_id, prop, idx, default\_value) |
|  | Like [GPIO\_DT\_SPEC\_GET\_BY\_IDX()](#gacb1077b77aecf8f1a9c7636ea583c4cf), with a fallback to a default value. |
| #define | [GPIO\_DT\_SPEC\_GET](#ga2fa6bb5880f46984f9fc29c70f7d503e)(node\_id, prop) |
|  | Equivalent to [GPIO\_DT\_SPEC\_GET\_BY\_IDX(node\_id, prop, 0)](#gacb1077b77aecf8f1a9c7636ea583c4cf). |
| #define | [GPIO\_DT\_SPEC\_GET\_OR](#ga26b2205aa82819df1d80a22761352e71)(node\_id, prop, default\_value) |
|  | Equivalent to [GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, prop, 0, default\_value)](#ga3db4fa464e191016287f4c4d7eb9a983). |
| #define | [GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX](#gabbdbef450f14fd0af73667e2728ad084)(inst, prop, idx) |
|  | Static initializer for a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")` from a DT\_DRV\_COMPAT instance's GPIO property at an index. |
| #define | [GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR](#gaf07edf6bc88af18e9976c76f6c3c3bf1)(inst, prop, idx, default\_value) |
|  | Static initializer for a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")` from a DT\_DRV\_COMPAT instance's GPIO property at an index, with fallback. |
| #define | [GPIO\_DT\_SPEC\_INST\_GET](#ga168f5c6e39a0111191f606a9a0826e89)(inst, prop) |
|  | Equivalent to [GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, prop, 0)](#gabbdbef450f14fd0af73667e2728ad084). |
| #define | [GPIO\_DT\_SPEC\_INST\_GET\_OR](#gae6b4a354c3cf0e042a390aac4bc37c69)(inst, prop, default\_value) |
|  | Equivalent to [GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, prop, 0, default\_value)](#gaf07edf6bc88af18e9976c76f6c3c3bf1). |
| #define | [GPIO\_DT\_RESERVED\_RANGES\_NGPIOS](#ga439c3d29aa585b00853aba6d6416028a)(node\_id, ngpios) |
|  | Makes a bitmask of reserved GPIOs from DT `"gpio-reserved-ranges"` property and `"ngpios"` argument. |
| #define | [GPIO\_DT\_RESERVED\_RANGES](#ga648fcc0633d57b52d3df683efda98440)(node\_id) |
|  | Makes a bitmask of reserved GPIOs from the `"gpio-reserved-ranges"` and `"ngpios"` DT properties values. |
| #define | [GPIO\_DT\_INST\_RESERVED\_RANGES\_NGPIOS](#gaebaea00f6f7649c61651e8d50c7cdf07)(inst, ngpios) |
|  | Makes a bitmask of reserved GPIOs from a DT\_DRV\_COMPAT instance's `"gpio-reserved-ranges"` property and `"ngpios"` argument. |
| #define | [GPIO\_DT\_INST\_RESERVED\_RANGES](#ga9136b467eaddcc734bc6a0a7d8b34e14)(inst) |
|  | Make a bitmask of reserved GPIOs from a DT\_DRV\_COMPAT instance's GPIO `"gpio-reserved-ranges"` and `"ngpios"` properties. |
| #define | [GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC](#ga274e09d7082d97b2f90c6a7fd4b71d49)(node\_id, ngpios) |
|  | Makes a bitmask of allowed GPIOs from DT `"gpio-reserved-ranges"` property and `"ngpios"` argument. |
| #define | [GPIO\_DT\_INST\_PORT\_PIN\_MASK\_NGPIOS\_EXC](#ga856fe8042e496a39ef3a4e19fff2c4ce)(inst, ngpios) |
|  | Makes a bitmask of allowed GPIOs from a DT\_DRV\_COMPAT instance's `"gpio-reserved-ranges"` property and `"ngpios"` argument. |
| #define | [GPIO\_MAX\_PINS\_PER\_PORT](#ga1449ba90eaec5e6144fe4faae21f2e3f)   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f)) \* \_\_CHAR\_BIT\_\_) |
|  | Maximum number of pins that are supported by [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f). |
| #define | [GPIO\_DT\_FLAGS\_MASK](#ga335bf7efee07e03961ab91a86295897a)   0x3F |
|  | Mask for DT GPIO flags. |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) |
|  | Identifies a set of pins associated with a port. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [gpio\_port\_value\_t](#gabcebe24c93486896e1dfc2459ec25693) |
|  | Provides values for a set of pins associated with a port. |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) |
|  | Provides a type to hold a GPIO pin index. |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [gpio\_dt\_flags\_t](#gad435719dccdc37c05852960a7218fbd2) |
|  | Provides a type to hold GPIO devicetree flags. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [gpio\_flags\_t](#ga5f5cb5e7dae6d58e072bb450af029d2e) |
|  | Provides a type to hold GPIO configuration flags. |
| typedef void(\* | [gpio\_callback\_handler\_t](#gaf0aa40279d32b1b8332f2f23a39510af)) (const struct [device](structdevice.md) \*port, struct [gpio\_callback](structgpio__callback.md) \*cb, [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) pins) |
|  | Define the application callback handler function signature. |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [gpio\_is\_ready\_dt](#gaaec9ad17c08a0d527d66445fe82d8327) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec) |
|  | Validate that GPIO port is ready. |
| int | [gpio\_pin\_interrupt\_configure](#ga9618f254365381063439a0e9c5e787cb) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) pin, [gpio\_flags\_t](#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Configure pin interrupt. |
| static int | [gpio\_pin\_interrupt\_configure\_dt](#ga24f0b4ad30e6a8c81f51a2813478c793) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec, [gpio\_flags\_t](#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Configure pin interrupts from a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")`. |
| int | [gpio\_pin\_configure](#gaed4a2051d76db7eead8ed1719ce2ba33) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) pin, [gpio\_flags\_t](#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Configure a single pin. |
| static int | [gpio\_pin\_configure\_dt](#ga423db4f985098ddcaa504ec430e91913) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec, [gpio\_flags\_t](#ga5f5cb5e7dae6d58e072bb450af029d2e) extra\_flags) |
|  | Configure a single pin from a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")` and some extra flags. |
| int | [gpio\_port\_get\_direction](#gad2b2945dbe6987ac425e000721a894c4) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) map, [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) \*inputs, [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) \*outputs) |
|  | Get direction of select pins in a port. |
| static int | [gpio\_pin\_is\_input](#ga1454bc223fc2200aff3c4aab7d747da2) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) pin) |
|  | Check if `pin` is configured for input. |
| static int | [gpio\_pin\_is\_input\_dt](#ga7aaec28a83cac63bd87fc94cc72664b1) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec) |
|  | Check if a single pin from `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")` is configured for input. |
| static int | [gpio\_pin\_is\_output](#ga3b854d759180e222299ea445b401acc1) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) pin) |
|  | Check if `pin` is configured for output. |
| static int | [gpio\_pin\_is\_output\_dt](#ga2255c5681d17952ab89a4b6016d8e80d) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec) |
|  | Check if a single pin from `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")` is configured for output. |
| int | [gpio\_pin\_get\_config](#ga133284b60a13c6dc50b87c1d04259f5e) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) pin, [gpio\_flags\_t](#ga5f5cb5e7dae6d58e072bb450af029d2e) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Get a configuration of a single pin. |
| static int | [gpio\_pin\_get\_config\_dt](#ga820448aa4be8b14839bc6a00c9f34bb4) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec, [gpio\_flags\_t](#ga5f5cb5e7dae6d58e072bb450af029d2e) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Get a configuration of a single pin from a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")`. |
| int | [gpio\_port\_get\_raw](#gae2a49b36cae2e17fc665a3bd844f50b4) (const struct [device](structdevice.md) \*port, [gpio\_port\_value\_t](#gabcebe24c93486896e1dfc2459ec25693) \*value) |
|  | Get physical level of all input pins in a port. |
| static int | [gpio\_port\_get](#gae578c8163fb8fe5600d1ca9e5d7526b1) (const struct [device](structdevice.md) \*port, [gpio\_port\_value\_t](#gabcebe24c93486896e1dfc2459ec25693) \*value) |
|  | Get logical level of all input pins in a port. |
| int | [gpio\_port\_set\_masked\_raw](#ga9e7b50d720fda362941acc1e3b3b2922) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) mask, [gpio\_port\_value\_t](#gabcebe24c93486896e1dfc2459ec25693) value) |
|  | Set physical level of output pins in a port. |
| static int | [gpio\_port\_set\_masked](#gac653e70270019d599732ab78693dd1fd) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) mask, [gpio\_port\_value\_t](#gabcebe24c93486896e1dfc2459ec25693) value) |
|  | Set logical level of output pins in a port. |
| int | [gpio\_port\_set\_bits\_raw](#ga18e6ca0df95566fecc0633efb04a075a) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) pins) |
|  | Set physical level of selected output pins to high. |
| static int | [gpio\_port\_set\_bits](#ga570b669af237df991c4a55cff6ec3253) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) pins) |
|  | Set logical level of selected output pins to active. |
| int | [gpio\_port\_clear\_bits\_raw](#ga9d2c9daeec7ce127fc786ead566ad27f) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) pins) |
|  | Set physical level of selected output pins to low. |
| static int | [gpio\_port\_clear\_bits](#gac1660707a44cc8a3aa08b25685b4b20b) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) pins) |
|  | Set logical level of selected output pins to inactive. |
| int | [gpio\_port\_toggle\_bits](#ga82977d8706fb9f464db455bd0e9ac2e4) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) pins) |
|  | Toggle level of selected output pins. |
| static int | [gpio\_port\_set\_clr\_bits\_raw](#ga6e7ca22e83a70d3ddcf0de068b377c2d) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) set\_pins, [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) clear\_pins) |
|  | Set physical level of selected output pins. |
| static int | [gpio\_port\_set\_clr\_bits](#ga77880d217f5dd1fc1c72ce791254449b) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) set\_pins, [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) clear\_pins) |
|  | Set logical level of selected output pins. |
| static int | [gpio\_pin\_get\_raw](#ga0fc52723b78019258bb306c771c430a1) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) pin) |
|  | Get physical level of an input pin. |
| static int | [gpio\_pin\_get](#ga154a4ea3d3084910f02df31dc0779be6) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) pin) |
|  | Get logical level of an input pin. |
| static int | [gpio\_pin\_get\_dt](#gaabeb2d0d98856c7ff78be36651d6bbc1) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec) |
|  | Get logical level of an input pin from a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")`. |
| static int | [gpio\_pin\_set\_raw](#gae28f0fa2576530083aa86d819d0d5cca) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) pin, int value) |
|  | Set physical level of an output pin. |
| static int | [gpio\_pin\_set](#gabfab69282fb99be119760436f2d18a9b) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) pin, int value) |
|  | Set logical level of an output pin. |
| static int | [gpio\_pin\_set\_dt](#ga541064fb9e575c0c559c101754466fa8) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec, int value) |
|  | Set logical level of a output pin from a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")`. |
| static int | [gpio\_pin\_toggle](#gaabf948471d313ff19410f1741dd16957) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) pin) |
|  | Toggle pin level. |
| static int | [gpio\_pin\_toggle\_dt](#ga3272e866489da6c2e12c48f803c59e81) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec) |
|  | Toggle pin level from a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")`. |
| static void | [gpio\_init\_callback](#ga7a7dd7c1f3a2135a9f378e1c34b6232c) (struct [gpio\_callback](structgpio__callback.md) \*callback, [gpio\_callback\_handler\_t](#gaf0aa40279d32b1b8332f2f23a39510af) handler, [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) pin\_mask) |
|  | Helper to initialize a struct [gpio\_callback](structgpio__callback.md "GPIO callback structure.") properly. |
| static int | [gpio\_add\_callback](#ga05fd15af20386d69f9332354285b0cca) (const struct [device](structdevice.md) \*port, struct [gpio\_callback](structgpio__callback.md) \*callback) |
|  | Add an application callback. |
| static int | [gpio\_add\_callback\_dt](#ga54845eb95bc9636c3e6ff285300b6979) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec, struct [gpio\_callback](structgpio__callback.md) \*callback) |
|  | Add an application callback. |
| static int | [gpio\_remove\_callback](#gac1e94ba8faac79f469447e9b5d2f8c06) (const struct [device](structdevice.md) \*port, struct [gpio\_callback](structgpio__callback.md) \*callback) |
|  | Remove an application callback. |
| static int | [gpio\_remove\_callback\_dt](#ga2c9f8fee2addfc0aeeeeb011d534f304) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec, struct [gpio\_callback](structgpio__callback.md) \*callback) |
|  | Remove an application callback. |
| int | [gpio\_get\_pending\_int](#ga3f9e45de172a27f49c31a072c0c241e1) (const struct [device](structdevice.md) \*dev) |
|  | Function to get pending interrupts. |

| GPIO input/output configuration flags | |
| --- | --- |
| #define | [GPIO\_INPUT](#ga7be6a0cc9aa65da1d4ee5751b4085853)   (1U << 16) |
|  | Enables pin as input. |
| #define | [GPIO\_OUTPUT](#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)   (1U << 17) |
|  | Enables pin as output, no change to the output state. |
| #define | [GPIO\_DISCONNECTED](#gaf82306c09450f6933366c4b821db21ed)   0 |
|  | Disables pin for both input and output. |
| #define | [GPIO\_OUTPUT\_LOW](#gaf85baf9f9c1ba554324b4cd7064487b0)   ([GPIO\_OUTPUT](#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1) | GPIO\_OUTPUT\_INIT\_LOW) |
|  | Configures GPIO pin as output and initializes it to a low state. |
| #define | [GPIO\_OUTPUT\_HIGH](#ga10d31f204c0e927017d571352422fb09)   ([GPIO\_OUTPUT](#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1) | GPIO\_OUTPUT\_INIT\_HIGH) |
|  | Configures GPIO pin as output and initializes it to a high state. |
| #define | [GPIO\_OUTPUT\_INACTIVE](#ga1e1d6be5f2f788f89468a0ce8b854634) |
|  | Configures GPIO pin as output and initializes it to a logic 0. |
| #define | [GPIO\_OUTPUT\_ACTIVE](#ga0f5cc126d6a690eb3e303eb29aa718ce) |
|  | Configures GPIO pin as output and initializes it to a logic 1. |

| GPIO interrupt configuration flags | |
| --- | --- |
| The GPIO\_INT\_\* flags are used to specify how input GPIO pins will trigger interrupts.  The interrupts can be sensitive to pin physical or logical level. Interrupts sensitive to pin logical level take into account GPIO\_ACTIVE\_LOW flag. If a pin was configured as Active Low, physical level low will be considered as logical level 1 (an active state), physical level high will be considered as logical level 0 (an inactive state). The GPIO controller should reset the interrupt status, such as clearing the pending bit, etc, when configuring the interrupt triggering properties. Applications should use the GPIO\_INT\_MODE\_ENABLE\_ONLY and GPIO\_INT\_MODE\_DISABLE\_ONLY flags to enable and disable interrupts on the pin without changing any GPIO settings. | |
| #define | [GPIO\_INT\_DISABLE](#ga91657faac28f9b213105dd61a419dd5a)   (1U << 21) |
|  | Disables GPIO pin interrupt. |
| #define | [GPIO\_INT\_EDGE\_RISING](#gaed642a4e482f73aa917477370d0e241b) |
|  | Configures GPIO interrupt to be triggered on pin rising edge and enables it. |
| #define | [GPIO\_INT\_EDGE\_FALLING](#ga73bed10383a27d4a03feb300e64af8e8) |
|  | Configures GPIO interrupt to be triggered on pin falling edge and enables it. |
| #define | [GPIO\_INT\_EDGE\_BOTH](#ga10fa307ab17d02819108165a09f8e08b) |
|  | Configures GPIO interrupt to be triggered on pin rising or falling edge and enables it. |
| #define | [GPIO\_INT\_LEVEL\_LOW](#gaddbb5ad576875af9c2d73b73df55c893) |
|  | Configures GPIO interrupt to be triggered on pin physical level low and enables it. |
| #define | [GPIO\_INT\_LEVEL\_HIGH](#ga233690d9a6a64bc9f804e3caa6d4a88f) |
|  | Configures GPIO interrupt to be triggered on pin physical level high and enables it. |
| #define | [GPIO\_INT\_EDGE\_TO\_INACTIVE](#ga7b922529a3cb9396b0d82ca823e9d010) |
|  | Configures GPIO interrupt to be triggered on pin state change to logical level 0 and enables it. |
| #define | [GPIO\_INT\_EDGE\_TO\_ACTIVE](#ga35d2ff0e041236d82004a4bb2b5bf634) |
|  | Configures GPIO interrupt to be triggered on pin state change to logical level 1 and enables it. |
| #define | [GPIO\_INT\_LEVEL\_INACTIVE](#gacb9bb1b63f172af2da7eb193e234c4f2) |
|  | Configures GPIO interrupt to be triggered on pin logical level 0 and enables it. |
| #define | [GPIO\_INT\_LEVEL\_ACTIVE](#gae51c68ff83959994bb942bb253505ca1) |
|  | Configures GPIO interrupt to be triggered on pin logical level 1 and enables it. |

| GPIO pin active level flags | |
| --- | --- |
| #define | [GPIO\_ACTIVE\_LOW](#ga62cea8989df2425e5e5e712217d65f46)   (1 << 0) |
|  | GPIO pin is active (has logical value '1') in low state. |
| #define | [GPIO\_ACTIVE\_HIGH](#gad93badd2828d065e7fd14cf40dd05039)   (0 << 0) |
|  | GPIO pin is active (has logical value '1') in high state. |

| GPIO pin drive flags | |
| --- | --- |
| #define | [GPIO\_OPEN\_DRAIN](#ga72b7ac5b3613d972b88268bee9068e35)   (GPIO\_SINGLE\_ENDED | GPIO\_LINE\_OPEN\_DRAIN) |
|  | Configures GPIO output in open drain mode (wired AND). |
| #define | [GPIO\_OPEN\_SOURCE](#ga5ace024873272a3f6727fc186afa0320)   (GPIO\_SINGLE\_ENDED | GPIO\_LINE\_OPEN\_SOURCE) |
|  | Configures GPIO output in open source mode (wired OR). |

| GPIO pin bias flags | |
| --- | --- |
| #define | [GPIO\_PULL\_UP](#gaaa7921da231fd2b96575fa522e2c1970)   (1 << 4) |
|  | Enables GPIO pin pull-up. |
| #define | [GPIO\_PULL\_DOWN](#gadec1802e074f3021d464da09cd66c7cf)   (1 << 5) |
|  | Enable GPIO pin pull-down. |

## Detailed Description

GPIO Driver APIs.

## Macro Definition Documentation

## [◆ ](#gad93badd2828d065e7fd14cf40dd05039)GPIO\_ACTIVE\_HIGH

| #define GPIO\_ACTIVE\_HIGH   (0 << 0) |
| --- |

`#include <[gpio.h](dt-bindings_2gpio_2gpio_8h.md)>`

GPIO pin is active (has logical value '1') in high state.

## [◆ ](#ga62cea8989df2425e5e5e712217d65f46)GPIO\_ACTIVE\_LOW

| #define GPIO\_ACTIVE\_LOW   (1 << 0) |
| --- |

`#include <[gpio.h](dt-bindings_2gpio_2gpio_8h.md)>`

GPIO pin is active (has logical value '1') in low state.

## [◆ ](#gaf82306c09450f6933366c4b821db21ed)GPIO\_DISCONNECTED

| #define GPIO\_DISCONNECTED   0 |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Disables pin for both input and output.

## [◆ ](#ga335bf7efee07e03961ab91a86295897a)GPIO\_DT\_FLAGS\_MASK

| #define GPIO\_DT\_FLAGS\_MASK   0x3F |
| --- |

`#include <[gpio.h](dt-bindings_2gpio_2gpio_8h.md)>`

Mask for DT GPIO flags.

## [◆ ](#ga856fe8042e496a39ef3a4e19fff2c4ce)GPIO\_DT\_INST\_PORT\_PIN\_MASK\_NGPIOS\_EXC

| #define GPIO\_DT\_INST\_PORT\_PIN\_MASK\_NGPIOS\_EXC | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *ngpios* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

[GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC](#ga274e09d7082d97b2f90c6a7fd4b71d49)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), ngpios)

[DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)

#define DT\_DRV\_INST(inst)

Node identifier for an instance of a DT\_DRV\_COMPAT compatible.

**Definition** devicetree.h:3410

[GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC](#ga274e09d7082d97b2f90c6a7fd4b71d49)

#define GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC(node\_id, ngpios)

Makes a bitmask of allowed GPIOs from DT "gpio-reserved-ranges" property and "ngpios" argument.

**Definition** gpio.h:655

Makes a bitmask of allowed GPIOs from a DT\_DRV\_COMPAT instance's `"gpio-reserved-ranges"` property and `"ngpios"` argument.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | ngpios | number of GPIOs |

Returns
:   the bitmask of allowed gpios

See also
:   GPIO\_DT\_NGPIOS\_PORT\_PIN\_MASK\_EXC()

## [◆ ](#ga9136b467eaddcc734bc6a0a7d8b34e14)GPIO\_DT\_INST\_RESERVED\_RANGES

| #define GPIO\_DT\_INST\_RESERVED\_RANGES | ( |  | *inst* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

[GPIO\_DT\_RESERVED\_RANGES](#ga648fcc0633d57b52d3df683efda98440)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst))

[GPIO\_DT\_RESERVED\_RANGES](#ga648fcc0633d57b52d3df683efda98440)

#define GPIO\_DT\_RESERVED\_RANGES(node\_id)

Makes a bitmask of reserved GPIOs from the "gpio-reserved-ranges" and "ngpios" DT properties values.

**Definition** gpio.h:581

Make a bitmask of reserved GPIOs from a DT\_DRV\_COMPAT instance's GPIO `"gpio-reserved-ranges"` and `"ngpios"` properties.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the bitmask of reserved gpios

See also
:   [GPIO\_DT\_RESERVED\_RANGES()](#ga648fcc0633d57b52d3df683efda98440)

## [◆ ](#gaebaea00f6f7649c61651e8d50c7cdf07)GPIO\_DT\_INST\_RESERVED\_RANGES\_NGPIOS

| #define GPIO\_DT\_INST\_RESERVED\_RANGES\_NGPIOS | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *ngpios* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

[GPIO\_DT\_RESERVED\_RANGES\_NGPIOS](#ga439c3d29aa585b00853aba6d6416028a)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), ngpios)

[GPIO\_DT\_RESERVED\_RANGES\_NGPIOS](#ga439c3d29aa585b00853aba6d6416028a)

#define GPIO\_DT\_RESERVED\_RANGES\_NGPIOS(node\_id, ngpios)

Makes a bitmask of reserved GPIOs from DT "gpio-reserved-ranges" property and "ngpios" argument.

**Definition** gpio.h:564

Makes a bitmask of reserved GPIOs from a DT\_DRV\_COMPAT instance's `"gpio-reserved-ranges"` property and `"ngpios"` argument.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |

Returns
:   the bitmask of reserved gpios

Parameters
:   | ngpios | number of GPIOs |
    | --- | --- |

See also
:   [GPIO\_DT\_RESERVED\_RANGES()](#ga648fcc0633d57b52d3df683efda98440)

## [◆ ](#ga274e09d7082d97b2f90c6a7fd4b71d49)GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC

| #define GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *ngpios* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

(([gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f)) \

COND\_CODE\_0(ngpios, \

(0), \

([COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, gpio\_reserved\_ranges), \

(([GENMASK64](group__sys-util.md#gab631f8a0ecb6fde5b22df40607868f04)(ngpios - 1, 0) & \

~[GPIO\_DT\_RESERVED\_RANGES\_NGPIOS](#ga439c3d29aa585b00853aba6d6416028a)(node\_id, ngpios))), \

([GENMASK64](group__sys-util.md#gab631f8a0ecb6fde5b22df40607868f04)(ngpios - 1, 0))) \

) \

))

[DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)

#define DT\_NODE\_HAS\_PROP(node\_id, prop)

Does a devicetree node have a property?

**Definition** devicetree.h:3285

[gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f)

uint32\_t gpio\_port\_pins\_t

Identifies a set of pins associated with a port.

**Definition** gpio.h:231

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)

#define COND\_CODE\_1(\_flag, \_if\_1\_code, \_else\_code)

Insert code depending on whether \_flag expands to 1 or not.

**Definition** util\_macro.h:179

[GENMASK64](group__sys-util.md#gab631f8a0ecb6fde5b22df40607868f04)

#define GENMASK64(h, l)

Create a contiguous 64-bit bitmask starting at bit position l and ending at position h.

**Definition** util.h:74

Makes a bitmask of allowed GPIOs from DT `"gpio-reserved-ranges"` property and `"ngpios"` argument.

This macro is paired with [GPIO\_DT\_RESERVED\_RANGES\_NGPIOS()](#ga439c3d29aa585b00853aba6d6416028a), however unlike the latter, it returns a bitmask of ALLOWED gpios.

Example devicetree fragment:

a {

compatible = "some,gpio-controller";

ngpios = <32>;

gpio-reserved-ranges = <0 8>, <9 5>, <15 16>;

};

Example usage:

struct some\_config {

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) port\_pin\_mask;

};

static const struct some\_config dev\_cfg = {

.port\_pin\_mask = [GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC](#ga274e09d7082d97b2f90c6a7fd4b71d49)(

DT\_LABEL(a), 32),

};

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

This expands to:

struct some\_config {

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) port\_pin\_mask;

};

static const struct some\_config dev\_cfg = {

.port\_pin\_mask = 0x80004100,

// 0b1000 0000 0000 0000 0100 0001 00000 000

};

Parameters
:   | node\_id | GPIO controller node identifier. |
    | --- | --- |
    | ngpios | number of GPIOs |

Returns
:   the bitmask of allowed gpios

## [◆ ](#ga648fcc0633d57b52d3df683efda98440)GPIO\_DT\_RESERVED\_RANGES

| #define GPIO\_DT\_RESERVED\_RANGES | ( |  | *node\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

[GPIO\_DT\_RESERVED\_RANGES\_NGPIOS](#ga439c3d29aa585b00853aba6d6416028a)(node\_id, [DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(node\_id, ngpios))

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)

#define DT\_PROP(node\_id, prop)

Get a devicetree property value.

**Definition** devicetree.h:615

Makes a bitmask of reserved GPIOs from the `"gpio-reserved-ranges"` and `"ngpios"` DT properties values.

Parameters
:   | node\_id | GPIO controller node identifier. |
    | --- | --- |

Returns
:   the bitmask of reserved gpios

## [◆ ](#ga439c3d29aa585b00853aba6d6416028a)GPIO\_DT\_RESERVED\_RANGES\_NGPIOS

| #define GPIO\_DT\_RESERVED\_RANGES\_NGPIOS | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *ngpios* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

(([gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f)) \

COND\_CODE\_1([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, gpio\_reserved\_ranges), \

([GENMASK64](group__sys-util.md#gab631f8a0ecb6fde5b22df40607868f04)([BITS\_PER\_LONG\_LONG](group__sys-util.md#gaeb3fa0f8ac477da6575363a158f36891) - 1, ngpios) \

| [FOR\_EACH\_FIXED\_ARG](group__sys-util.md#ga1a2b2aa21d7cc37f33e6a62abd2ae340)(Z\_GPIO\_GEN\_RESERVED\_RANGES\_COND, \

(|), \

node\_id, \

[LIST\_DROP\_EMPTY](group__sys-util.md#gab9762d5128988f7f4f5d51213ea52025)(Z\_SPARSE\_LIST\_ODD\_NUMBERS))), \

(0)))

[FOR\_EACH\_FIXED\_ARG](group__sys-util.md#ga1a2b2aa21d7cc37f33e6a62abd2ae340)

#define FOR\_EACH\_FIXED\_ARG(F, sep, fixed\_arg,...)

Call macro F on each provided argument, with an additional fixed argument as a parameter.

**Definition** util\_macro.h:585

[LIST\_DROP\_EMPTY](group__sys-util.md#gab9762d5128988f7f4f5d51213ea52025)

#define LIST\_DROP\_EMPTY(...)

Remove empty arguments from list.

**Definition** util\_macro.h:315

[BITS\_PER\_LONG\_LONG](group__sys-util.md#gaeb3fa0f8ac477da6575363a158f36891)

#define BITS\_PER\_LONG\_LONG

Number of bits in a long long int.

**Definition** util.h:61

Makes a bitmask of reserved GPIOs from DT `"gpio-reserved-ranges"` property and `"ngpios"` argument.

This macro returns the value as a bitmask of the `"gpio-reserved-ranges"` property. This property defines the disabled (or 'reserved') GPIOs in the range `0`...ngpios-1 and is specified as an array of value's pairs that define the start offset and size of the reserved ranges.

For example, setting "gpio-reserved-ranges = <3 2>, <10 1>;" means that GPIO offsets 3, 4 and 10 cannot be used even if `ngpios` = <18>.

The implementation constraint is inherited from common DT limitations: a maximum of 64 pairs can be used (with result limited to bitsize of [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) type).

NB: Due to the nature of C macros, some incorrect tuple definitions (for example, overlapping or out of range) will produce undefined results.

Also be aware that if `ngpios` is less than 32 (bit size of DT int type), then all unused MSBs outside the range defined by `ngpios` will be marked as reserved too.

Example devicetree fragment:

a {

compatible = "some,gpio-controller";

ngpios = <32>;

gpio-reserved-ranges = <0 4>, <5 3>, <9 5>, <11 2>, <15 2>,

<18 2>, <21 1>, <23 1>, <25 4>, <30 2>;

};

b {

compatible = "some,gpio-controller";

ngpios = <18>;

gpio-reserved-ranges = <3 2>, <10 1>;

};

Example usage:

struct some\_config {

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ngpios;

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpios\_reserved;

};

static const struct some\_config dev\_cfg\_a = {

.ngpios = [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(DT\_LABEL(a), ngpios, 0),

.gpios\_reserved = [GPIO\_DT\_RESERVED\_RANGES\_NGPIOS](#ga439c3d29aa585b00853aba6d6416028a)(DT\_LABEL(a),

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(DT\_LABEL(a), ngpios)),

};

static const struct some\_config dev\_cfg\_b = {

.ngpios = [DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)(DT\_LABEL(b), ngpios, 0),

.gpios\_reserved = [GPIO\_DT\_RESERVED\_RANGES\_NGPIOS](#ga439c3d29aa585b00853aba6d6416028a)(DT\_LABEL(b),

[DT\_PROP](group__devicetree-generic-prop.md#ga8e1fd9ebacd85d2013df027d041d506b)(DT\_LABEL(b), ngpios)),

};

[DT\_PROP\_OR](group__devicetree-generic-prop.md#ga5e5bfc9b1a6627b3f73014329e96340f)

#define DT\_PROP\_OR(node\_id, prop, default\_value)

Like DT\_PROP(), but with a fallback to default\_value.

**Definition** devicetree.h:777

This expands to:

struct some\_config {

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ngpios;

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) gpios\_reserved;

};

static const struct some\_config dev\_cfg\_a = {

.ngpios = 32,

.gpios\_reserved = 0xdeadbeef,

// 0b1101 1110 1010 1101 1011 1110 1110 1111

static const struct some\_config dev\_cfg\_b = {

.ngpios = 18,

.gpios\_reserved = 0xfffc0418,

// 0b1111 1111 1111 1100 0000 0100 0001 1000

// unused MSBs were marked as reserved too

};

Parameters
:   | node\_id | GPIO controller node identifier. |
    | --- | --- |
    | ngpios | number of GPIOs. |

Returns
:   the bitmask of reserved gpios

## [◆ ](#ga2fa6bb5880f46984f9fc29c70f7d503e)GPIO\_DT\_SPEC\_GET

| #define GPIO\_DT\_SPEC\_GET | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

[GPIO\_DT\_SPEC\_GET\_BY\_IDX](#gacb1077b77aecf8f1a9c7636ea583c4cf)(node\_id, prop, 0)

[GPIO\_DT\_SPEC\_GET\_BY\_IDX](#gacb1077b77aecf8f1a9c7636ea583c4cf)

#define GPIO\_DT\_SPEC\_GET\_BY\_IDX(node\_id, prop, idx)

Static initializer for a gpio\_dt\_spec.

**Definition** gpio.h:329

Equivalent to [GPIO\_DT\_SPEC\_GET\_BY\_IDX(node\_id, prop, 0)](#gacb1077b77aecf8f1a9c7636ea583c4cf).

Parameters
:   | node\_id | devicetree node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |

Returns
:   static initializer for a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for the property

See also
:   [GPIO\_DT\_SPEC\_GET\_BY\_IDX()](#gacb1077b77aecf8f1a9c7636ea583c4cf)

## [◆ ](#gacb1077b77aecf8f1a9c7636ea583c4cf)GPIO\_DT\_SPEC\_GET\_BY\_IDX

| #define GPIO\_DT\_SPEC\_GET\_BY\_IDX | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

{ \

.port = [DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)([DT\_GPIO\_CTLR\_BY\_IDX](group__devicetree-gpio.md#ga97bd46d2ab88d392a3f336f4d23184eb)(node\_id, prop, idx)),\

.pin = [DT\_GPIO\_PIN\_BY\_IDX](group__devicetree-gpio.md#ga8f7d82567056266bab1603865f8b27af)(node\_id, prop, idx), \

.dt\_flags = [DT\_GPIO\_FLAGS\_BY\_IDX](group__devicetree-gpio.md#ga672b2597b99194b8cbd42b3f3401d2b5)(node\_id, prop, idx), \

}

[DEVICE\_DT\_GET](group__device__model.md#ga9a65996ce21f43acb7db061e23b48ec7)

#define DEVICE\_DT\_GET(node\_id)

Get a device reference from a devicetree node identifier.

**Definition** device.h:233

[DT\_GPIO\_FLAGS\_BY\_IDX](group__devicetree-gpio.md#ga672b2597b99194b8cbd42b3f3401d2b5)

#define DT\_GPIO\_FLAGS\_BY\_IDX(node\_id, gpio\_pha, idx)

Get a GPIO specifier's flags cell at an index.

**Definition** gpio.h:165

[DT\_GPIO\_PIN\_BY\_IDX](group__devicetree-gpio.md#ga8f7d82567056266bab1603865f8b27af)

#define DT\_GPIO\_PIN\_BY\_IDX(node\_id, gpio\_pha, idx)

Get a GPIO specifier's pin cell at an index.

**Definition** gpio.h:109

[DT\_GPIO\_CTLR\_BY\_IDX](group__devicetree-gpio.md#ga97bd46d2ab88d392a3f336f4d23184eb)

#define DT\_GPIO\_CTLR\_BY\_IDX(node\_id, gpio\_pha, idx)

Get the node identifier for the controller phandle from a gpio phandle-array property at an index.

**Definition** gpio.h:53

Static initializer for a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")`.

This returns a static initializer for a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")` structure given a devicetree node identifier, a property specifying a GPIO and an index.

Example devicetree fragment:

```
 n: node {
    foo-gpios = <&gpio0 1 GPIO_ACTIVE_LOW>,
                <&gpio1 2 GPIO_ACTIVE_LOW>;
 }
```

Example usage:

```
 const struct gpio_dt_spec spec = GPIO_DT_SPEC_GET_BY_IDX(DT_NODELABEL(n),
                                                     foo_gpios, 1);
 // Initializes 'spec' to:
 // {
 //         .port = DEVICE_DT_GET(DT_NODELABEL(gpio1)),
 //         .pin = 2,
 //         .dt_flags = GPIO_ACTIVE_LOW
 // }
```

The 'gpio' field must still be checked for readiness, e.g. using [device\_is\_ready()](group__device__model.md#gaa4944bd850e90cbd52b0489f9b12edfb "Verify that a device is ready for use."). It is an error to use this macro unless the node exists, has the given property, and that property specifies a GPIO controller, pin number, and flags as shown above.

Parameters
:   | node\_id | devicetree node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | idx | logical index into "prop" |

Returns
:   static initializer for a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for the property

## [◆ ](#ga3db4fa464e191016287f4c4d7eb9a983)GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR

| #define GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx*, |
|  |  |  | *default\_value* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_NODE\_HAS\_PROP](group__devicetree-generic-exist.md#gacce67bf20541cd2d07d8540058964692)(node\_id, prop), \

([GPIO\_DT\_SPEC\_GET\_BY\_IDX](#gacb1077b77aecf8f1a9c7636ea583c4cf)(node\_id, prop, idx)), \

(default\_value))

Like [GPIO\_DT\_SPEC\_GET\_BY\_IDX()](#gacb1077b77aecf8f1a9c7636ea583c4cf), with a fallback to a default value.

If the devicetree node identifier 'node\_id' refers to a node with a property 'prop', this expands to [GPIO\_DT\_SPEC\_GET\_BY\_IDX(node\_id, prop, idx)](#gacb1077b77aecf8f1a9c7636ea583c4cf). The `default_value` parameter is not expanded in this case.

Otherwise, this expands to `default_value`.

Parameters
:   | node\_id | devicetree node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | idx | logical index into "prop" |
    | default\_value | fallback value to expand to |

Returns
:   static initializer for a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for the property, or default\_value if the node or property do not exist

## [◆ ](#ga26b2205aa82819df1d80a22761352e71)GPIO\_DT\_SPEC\_GET\_OR

| #define GPIO\_DT\_SPEC\_GET\_OR | ( |  | *node\_id*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *default\_value* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

[GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR](#ga3db4fa464e191016287f4c4d7eb9a983)(node\_id, prop, 0, default\_value)

[GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR](#ga3db4fa464e191016287f4c4d7eb9a983)

#define GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, prop, idx, default\_value)

Like GPIO\_DT\_SPEC\_GET\_BY\_IDX(), with a fallback to a default value.

**Definition** gpio.h:353

Equivalent to [GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, prop, 0, default\_value)](#ga3db4fa464e191016287f4c4d7eb9a983).

Parameters
:   | node\_id | devicetree node identifier |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | default\_value | fallback value to expand to |

Returns
:   static initializer for a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for the property

See also
:   [GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR()](#ga3db4fa464e191016287f4c4d7eb9a983)

## [◆ ](#ga168f5c6e39a0111191f606a9a0826e89)GPIO\_DT\_SPEC\_INST\_GET

| #define GPIO\_DT\_SPEC\_INST\_GET | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

[GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX](#gabbdbef450f14fd0af73667e2728ad084)(inst, prop, 0)

[GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX](#gabbdbef450f14fd0af73667e2728ad084)

#define GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, prop, idx)

Static initializer for a gpio\_dt\_spec from a DT\_DRV\_COMPAT instance's GPIO property at an index.

**Definition** gpio.h:392

Equivalent to [GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, prop, 0)](#gabbdbef450f14fd0af73667e2728ad084).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |

Returns
:   static initializer for a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for the property

See also
:   [GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX()](#gabbdbef450f14fd0af73667e2728ad084)

## [◆ ](#gabbdbef450f14fd0af73667e2728ad084)GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX

| #define GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

[GPIO\_DT\_SPEC\_GET\_BY\_IDX](#gacb1077b77aecf8f1a9c7636ea583c4cf)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, idx)

Static initializer for a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")` from a DT\_DRV\_COMPAT instance's GPIO property at an index.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | idx | logical index into "prop" |

Returns
:   static initializer for a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for the property

See also
:   [GPIO\_DT\_SPEC\_GET\_BY\_IDX()](#gacb1077b77aecf8f1a9c7636ea583c4cf)

## [◆ ](#gaf07edf6bc88af18e9976c76f6c3c3bf1)GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR

| #define GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *idx*, |
|  |  |  | *default\_value* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

[COND\_CODE\_1](group__sys-util.md#ga358bc3e7669c860a98839a51cd526b20)([DT\_PROP\_HAS\_IDX](group__devicetree-generic-prop.md#ga479dfc704087eea7e7c5af42ae98576c)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, idx), \

([GPIO\_DT\_SPEC\_GET\_BY\_IDX](#gacb1077b77aecf8f1a9c7636ea583c4cf)([DT\_DRV\_INST](group__devicetree-inst.md#ga219f413efba2f4c0151468b9a25a8dc1)(inst), prop, idx)), \

(default\_value))

[DT\_PROP\_HAS\_IDX](group__devicetree-generic-prop.md#ga479dfc704087eea7e7c5af42ae98576c)

#define DT\_PROP\_HAS\_IDX(node\_id, prop, idx)

Is index idx valid for an array type property?

**Definition** devicetree.h:689

Static initializer for a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")` from a DT\_DRV\_COMPAT instance's GPIO property at an index, with fallback.

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | idx | logical index into "prop" |
    | default\_value | fallback value to expand to |

Returns
:   static initializer for a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for the property

See also
:   [GPIO\_DT\_SPEC\_GET\_BY\_IDX()](#gacb1077b77aecf8f1a9c7636ea583c4cf)

## [◆ ](#gae6b4a354c3cf0e042a390aac4bc37c69)GPIO\_DT\_SPEC\_INST\_GET\_OR

| #define GPIO\_DT\_SPEC\_INST\_GET\_OR | ( |  | *inst*, |
| --- | --- | --- | --- |
|  |  |  | *prop*, |
|  |  |  | *default\_value* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

[GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR](#gaf07edf6bc88af18e9976c76f6c3c3bf1)(inst, prop, 0, default\_value)

[GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR](#gaf07edf6bc88af18e9976c76f6c3c3bf1)

#define GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, prop, idx, default\_value)

Static initializer for a gpio\_dt\_spec from a DT\_DRV\_COMPAT instance's GPIO property at an index,...

**Definition** gpio.h:406

Equivalent to [GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, prop, 0, default\_value)](#gaf07edf6bc88af18e9976c76f6c3c3bf1).

Parameters
:   | inst | DT\_DRV\_COMPAT instance number |
    | --- | --- |
    | prop | lowercase-and-underscores property name |
    | default\_value | fallback value to expand to |

Returns
:   static initializer for a struct [gpio\_dt\_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.") for the property

See also
:   [GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX()](#gabbdbef450f14fd0af73667e2728ad084)

## [◆ ](#ga7be6a0cc9aa65da1d4ee5751b4085853)GPIO\_INPUT

| #define GPIO\_INPUT   (1U << 16) |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Enables pin as input.

## [◆ ](#ga91657faac28f9b213105dd61a419dd5a)GPIO\_INT\_DISABLE

| #define GPIO\_INT\_DISABLE   (1U << 21) |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Disables GPIO pin interrupt.

## [◆ ](#ga10fa307ab17d02819108165a09f8e08b)GPIO\_INT\_EDGE\_BOTH

| #define GPIO\_INT\_EDGE\_BOTH |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

(GPIO\_INT\_ENABLE | \

GPIO\_INT\_EDGE | \

GPIO\_INT\_LOW\_0 | \

GPIO\_INT\_HIGH\_1)

Configures GPIO interrupt to be triggered on pin rising or falling edge and enables it.

## [◆ ](#ga73bed10383a27d4a03feb300e64af8e8)GPIO\_INT\_EDGE\_FALLING

| #define GPIO\_INT\_EDGE\_FALLING |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

(GPIO\_INT\_ENABLE | \

GPIO\_INT\_EDGE | \

GPIO\_INT\_LOW\_0)

Configures GPIO interrupt to be triggered on pin falling edge and enables it.

## [◆ ](#gaed642a4e482f73aa917477370d0e241b)GPIO\_INT\_EDGE\_RISING

| #define GPIO\_INT\_EDGE\_RISING |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

(GPIO\_INT\_ENABLE | \

GPIO\_INT\_EDGE | \

GPIO\_INT\_HIGH\_1)

Configures GPIO interrupt to be triggered on pin rising edge and enables it.

## [◆ ](#ga35d2ff0e041236d82004a4bb2b5bf634)GPIO\_INT\_EDGE\_TO\_ACTIVE

| #define GPIO\_INT\_EDGE\_TO\_ACTIVE |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

(GPIO\_INT\_ENABLE | \

GPIO\_INT\_LEVELS\_LOGICAL | \

GPIO\_INT\_EDGE | \

GPIO\_INT\_HIGH\_1)

Configures GPIO interrupt to be triggered on pin state change to logical level 1 and enables it.

## [◆ ](#ga7b922529a3cb9396b0d82ca823e9d010)GPIO\_INT\_EDGE\_TO\_INACTIVE

| #define GPIO\_INT\_EDGE\_TO\_INACTIVE |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

(GPIO\_INT\_ENABLE | \

GPIO\_INT\_LEVELS\_LOGICAL | \

GPIO\_INT\_EDGE | \

GPIO\_INT\_LOW\_0)

Configures GPIO interrupt to be triggered on pin state change to logical level 0 and enables it.

## [◆ ](#gae51c68ff83959994bb942bb253505ca1)GPIO\_INT\_LEVEL\_ACTIVE

| #define GPIO\_INT\_LEVEL\_ACTIVE |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

(GPIO\_INT\_ENABLE | \

GPIO\_INT\_LEVELS\_LOGICAL | \

GPIO\_INT\_HIGH\_1)

Configures GPIO interrupt to be triggered on pin logical level 1 and enables it.

## [◆ ](#ga233690d9a6a64bc9f804e3caa6d4a88f)GPIO\_INT\_LEVEL\_HIGH

| #define GPIO\_INT\_LEVEL\_HIGH |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

(GPIO\_INT\_ENABLE | \

GPIO\_INT\_HIGH\_1)

Configures GPIO interrupt to be triggered on pin physical level high and enables it.

## [◆ ](#gacb9bb1b63f172af2da7eb193e234c4f2)GPIO\_INT\_LEVEL\_INACTIVE

| #define GPIO\_INT\_LEVEL\_INACTIVE |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

(GPIO\_INT\_ENABLE | \

GPIO\_INT\_LEVELS\_LOGICAL | \

GPIO\_INT\_LOW\_0)

Configures GPIO interrupt to be triggered on pin logical level 0 and enables it.

## [◆ ](#gaddbb5ad576875af9c2d73b73df55c893)GPIO\_INT\_LEVEL\_LOW

| #define GPIO\_INT\_LEVEL\_LOW |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

(GPIO\_INT\_ENABLE | \

GPIO\_INT\_LOW\_0)

Configures GPIO interrupt to be triggered on pin physical level low and enables it.

## [◆ ](#ga1449ba90eaec5e6144fe4faae21f2e3f)GPIO\_MAX\_PINS\_PER\_PORT

| #define GPIO\_MAX\_PINS\_PER\_PORT   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f)) \* \_\_CHAR\_BIT\_\_) |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Maximum number of pins that are supported by [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f).

## [◆ ](#ga72b7ac5b3613d972b88268bee9068e35)GPIO\_OPEN\_DRAIN

| #define GPIO\_OPEN\_DRAIN   (GPIO\_SINGLE\_ENDED | GPIO\_LINE\_OPEN\_DRAIN) |
| --- |

`#include <[gpio.h](dt-bindings_2gpio_2gpio_8h.md)>`

Configures GPIO output in open drain mode (wired AND).

Note
:   'Open Drain' mode also known as 'Open Collector' is an output configuration which behaves like a switch that is either connected to ground or disconnected.

## [◆ ](#ga5ace024873272a3f6727fc186afa0320)GPIO\_OPEN\_SOURCE

| #define GPIO\_OPEN\_SOURCE   (GPIO\_SINGLE\_ENDED | GPIO\_LINE\_OPEN\_SOURCE) |
| --- |

`#include <[gpio.h](dt-bindings_2gpio_2gpio_8h.md)>`

Configures GPIO output in open source mode (wired OR).

Note
:   'Open Source' is a term used by software engineers to describe output mode opposite to 'Open Drain'. It behaves like a switch that is either connected to power supply or disconnected. There exist no corresponding hardware schematic and the term is generally unknown to hardware engineers.

## [◆ ](#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)GPIO\_OUTPUT

| #define GPIO\_OUTPUT   (1U << 17) |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Enables pin as output, no change to the output state.

## [◆ ](#ga0f5cc126d6a690eb3e303eb29aa718ce)GPIO\_OUTPUT\_ACTIVE

| #define GPIO\_OUTPUT\_ACTIVE |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

([GPIO\_OUTPUT](#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1) | \

GPIO\_OUTPUT\_INIT\_HIGH | \

GPIO\_OUTPUT\_INIT\_LOGICAL)

[GPIO\_OUTPUT](#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)

#define GPIO\_OUTPUT

Enables pin as output, no change to the output state.

**Definition** gpio.h:48

Configures GPIO pin as output and initializes it to a logic 1.

## [◆ ](#ga10d31f204c0e927017d571352422fb09)GPIO\_OUTPUT\_HIGH

| #define GPIO\_OUTPUT\_HIGH   ([GPIO\_OUTPUT](#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1) | GPIO\_OUTPUT\_INIT\_HIGH) |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Configures GPIO pin as output and initializes it to a high state.

## [◆ ](#ga1e1d6be5f2f788f89468a0ce8b854634)GPIO\_OUTPUT\_INACTIVE

| #define GPIO\_OUTPUT\_INACTIVE |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

**Value:**

([GPIO\_OUTPUT](#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1) | \

GPIO\_OUTPUT\_INIT\_LOW | \

GPIO\_OUTPUT\_INIT\_LOGICAL)

Configures GPIO pin as output and initializes it to a logic 0.

## [◆ ](#gaf85baf9f9c1ba554324b4cd7064487b0)GPIO\_OUTPUT\_LOW

| #define GPIO\_OUTPUT\_LOW   ([GPIO\_OUTPUT](#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1) | GPIO\_OUTPUT\_INIT\_LOW) |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Configures GPIO pin as output and initializes it to a low state.

## [◆ ](#gadec1802e074f3021d464da09cd66c7cf)GPIO\_PULL\_DOWN

| #define GPIO\_PULL\_DOWN   (1 << 5) |
| --- |

`#include <[gpio.h](dt-bindings_2gpio_2gpio_8h.md)>`

Enable GPIO pin pull-down.

## [◆ ](#gaaa7921da231fd2b96575fa522e2c1970)GPIO\_PULL\_UP

| #define GPIO\_PULL\_UP   (1 << 4) |
| --- |

`#include <[gpio.h](dt-bindings_2gpio_2gpio_8h.md)>`

Enables GPIO pin pull-up.

## Typedef Documentation

## [◆ ](#gaf0aa40279d32b1b8332f2f23a39510af)gpio\_callback\_handler\_t

| typedef void(\* gpio\_callback\_handler\_t) (const struct [device](structdevice.md) \*port, struct [gpio\_callback](structgpio__callback.md) \*cb, [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) pins) |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Define the application callback handler function signature.

Parameters
:   | port | Device struct for the GPIO device. |
    | --- | --- |
    | cb | Original struct [gpio\_callback](structgpio__callback.md "GPIO callback structure.") owning this handler |
    | pins | Mask of pins that triggers the callback handler |

Note: cb pointer can be used to retrieve private data through [CONTAINER\_OF()](group__sys-util.md#gac5bc561d1bfd1bf68877fe577779bd2f "Get a pointer to a structure containing the element.") if original struct [gpio\_callback](structgpio__callback.md "GPIO callback structure.") is stored in another private structure.

## [◆ ](#gad435719dccdc37c05852960a7218fbd2)gpio\_dt\_flags\_t

| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [gpio\_dt\_flags\_t](#gad435719dccdc37c05852960a7218fbd2) |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Provides a type to hold GPIO devicetree flags.

All GPIO flags that can be expressed in devicetree fit in the low 16 bits of the full flags field, so use a reduced-size type to record that part of a GPIOS property.

The lower 8 bits are used for standard flags. The upper 8 bits are reserved for SoC specific flags.

## [◆ ](#ga5f5cb5e7dae6d58e072bb450af029d2e)gpio\_flags\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [gpio\_flags\_t](#ga5f5cb5e7dae6d58e072bb450af029d2e) |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Provides a type to hold GPIO configuration flags.

This type is sufficient to hold all flags used to control GPIO configuration, whether pin or interrupt.

## [◆ ](#ga38179eb7a46a743c12cfac28f347fb34)gpio\_pin\_t

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Provides a type to hold a GPIO pin index.

This reduced-size type is sufficient to record a pin number, e.g. from a devicetree GPIOS property.

## [◆ ](#ga7f40ed51f14fd8000e9b52ab347b273f)gpio\_port\_pins\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Identifies a set of pins associated with a port.

The pin with index n is present in the set if and only if the bit identified by (1U << n) is set.

## [◆ ](#gabcebe24c93486896e1dfc2459ec25693)gpio\_port\_value\_t

| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [gpio\_port\_value\_t](#gabcebe24c93486896e1dfc2459ec25693) |
| --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Provides values for a set of pins associated with a port.

The value for a pin with index n is high (physical mode) or active (logical mode) if and only if the bit identified by (1U << n) is set. Otherwise the value for the pin is low (physical mode) or inactive (logical mode).

Values of this type are often paired with a [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) value that specifies which encoded pin values are valid for the operation.

## Function Documentation

## [◆ ](#ga05fd15af20386d69f9332354285b0cca)gpio\_add\_callback()

| | int gpio\_add\_callback | ( | const struct [device](structdevice.md) \* | *port*, | | --- | --- | --- | --- | |  |  | struct [gpio\_callback](structgpio__callback.md) \* | *callback* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Add an application callback.

Parameters
:   | port | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | callback | A valid Application's callback structure pointer. |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -ENOSYS | If driver does not implement the operation |
    | -errno | Other negative errno code on failure. |

Note
:   Callbacks may be added to the device from within a callback handler invocation, but whether they are invoked for the current GPIO event is not specified.

Note: enables to add as many callback as needed on the same port.

## [◆ ](#ga54845eb95bc9636c3e6ff285300b6979)gpio\_add\_callback\_dt()

| | int gpio\_add\_callback\_dt | ( | const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | struct [gpio\_callback](structgpio__callback.md) \* | *callback* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Add an application callback.

This is equivalent to:

```
gpio_add_callback(spec->port, callback);
```

Parameters
:   | spec | GPIO specification from devicetree. |
    | --- | --- |
    | callback | A valid application's callback structure pointer. |

Returns
:   a value from [gpio\_add\_callback()](#ga05fd15af20386d69f9332354285b0cca).

## [◆ ](#ga3f9e45de172a27f49c31a072c0c241e1)gpio\_get\_pending\_int()

| int gpio\_get\_pending\_int | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Function to get pending interrupts.

The purpose of this function is to return the interrupt status register for the device. This is especially useful when waking up from low power states to check the wake up source.

Parameters
:   | dev | Pointer to the device structure for the driver instance. |
    | --- | --- |

Return values
:   | status | != 0 if at least one gpio interrupt is pending. |
    | --- | --- |
    | 0 | if no gpio interrupt is pending. |
    | -ENOSYS | If driver does not implement the operation |

## [◆ ](#ga7a7dd7c1f3a2135a9f378e1c34b6232c)gpio\_init\_callback()

| | void gpio\_init\_callback | ( | struct [gpio\_callback](structgpio__callback.md) \* | *callback*, | | --- | --- | --- | --- | |  |  | [gpio\_callback\_handler\_t](#gaf0aa40279d32b1b8332f2f23a39510af) | *handler*, | |  |  | [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) | *pin\_mask* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Helper to initialize a struct [gpio\_callback](structgpio__callback.md "GPIO callback structure.") properly.

Parameters
:   | callback | A valid Application's callback structure pointer. |
    | --- | --- |
    | handler | A valid handler function pointer. |
    | pin\_mask | A bit mask of relevant pins for the handler |

## [◆ ](#gaaec9ad17c08a0d527d66445fe82d8327)gpio\_is\_ready\_dt()

| | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) gpio\_is\_ready\_dt | ( | const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Validate that GPIO port is ready.

Parameters
:   | spec | GPIO specification from devicetree |
    | --- | --- |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | if the GPIO spec is ready for use. |
    | --- | --- |
    | [false](stdbool_8h.md#a65e9886d74aaee76545e83dd09011727) | if the GPIO spec is not ready for use. |

## [◆ ](#gaed4a2051d76db7eead8ed1719ce2ba33)gpio\_pin\_configure()

| int gpio\_pin\_configure | ( | const struct [device](structdevice.md) \* | *port*, |
| --- | --- | --- | --- |
|  |  | [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) | *pin*, |
|  |  | [gpio\_flags\_t](#ga5f5cb5e7dae6d58e072bb450af029d2e) | *flags* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Configure a single pin.

Parameters
:   | port | Pointer to device structure for the driver instance. |
    | --- | --- |
    | pin | Pin number to configure. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Flags for pin configuration: 'GPIO input/output configuration flags', 'GPIO pin drive flags', 'GPIO pin bias flags'. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOTSUP | if any of the configuration options is not supported (unless otherwise directed by flag documentation). |
    | -EINVAL | Invalid argument. |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#ga423db4f985098ddcaa504ec430e91913)gpio\_pin\_configure\_dt()

| | int gpio\_pin\_configure\_dt | ( | const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | [gpio\_flags\_t](#ga5f5cb5e7dae6d58e072bb450af029d2e) | *extra\_flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Configure a single pin from a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")` and some extra flags.

This is equivalent to:

```
gpio_pin_configure(spec->port, spec->pin, spec->dt_flags | extra_flags);
```

Parameters
:   | spec | GPIO specification from devicetree |
    | --- | --- |
    | extra\_flags | additional flags |

Returns
:   a value from [gpio\_pin\_configure()](#gaed4a2051d76db7eead8ed1719ce2ba33)

## [◆ ](#ga154a4ea3d3084910f02df31dc0779be6)gpio\_pin\_get()

| | int gpio\_pin\_get | ( | const struct [device](structdevice.md) \* | *port*, | | --- | --- | --- | --- | |  |  | [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) | *pin* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Get logical level of an input pin.

Get logical level of an input pin taking into account GPIO\_ACTIVE\_LOW flag. If pin is configured as Active High, a low physical level will be interpreted as logical value 0. If pin is configured as Active Low, a low physical level will be interpreted as logical value 1.

Note: If pin is configured as Active High, the default, [gpio\_pin\_get()](#ga154a4ea3d3084910f02df31dc0779be6) function is equivalent to [gpio\_pin\_get\_raw()](#ga0fc52723b78019258bb306c771c430a1).

Parameters
:   | port | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pin | Pin number. |

Return values
:   | 1 | If pin logical value is 1 / active. |
    | --- | --- |
    | 0 | If pin logical value is 0 / inactive. |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#ga133284b60a13c6dc50b87c1d04259f5e)gpio\_pin\_get\_config()

| int gpio\_pin\_get\_config | ( | const struct [device](structdevice.md) \* | *port*, |
| --- | --- | --- | --- |
|  |  | [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) | *pin*, |
|  |  | [gpio\_flags\_t](#ga5f5cb5e7dae6d58e072bb450af029d2e) \* | *flags* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Get a configuration of a single pin.

Parameters
:   | port | Pointer to device structure for the driver instance. |
    | --- | --- |
    | pin | Pin number which configuration is get. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Pointer to variable in which the current configuration will be stored if function is successful. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | if getting current pin configuration is not implemented by the driver. |
    | -EINVAL | Invalid argument. |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#ga820448aa4be8b14839bc6a00c9f34bb4)gpio\_pin\_get\_config\_dt()

| | int gpio\_pin\_get\_config\_dt | ( | const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | [gpio\_flags\_t](#ga5f5cb5e7dae6d58e072bb450af029d2e) \* | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Get a configuration of a single pin from a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")`.

This is equivalent to:

```
gpio_pin_get_config(spec->port, spec->pin, flags);
```

Parameters
:   | spec | GPIO specification from devicetree |
    | --- | --- |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Pointer to variable in which the current configuration will be stored if function is successful. |

Returns
:   a value from [gpio\_pin\_configure()](#gaed4a2051d76db7eead8ed1719ce2ba33)

## [◆ ](#gaabeb2d0d98856c7ff78be36651d6bbc1)gpio\_pin\_get\_dt()

| | int gpio\_pin\_get\_dt | ( | const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Get logical level of an input pin from a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")`.

This is equivalent to:

```
gpio_pin_get(spec->port, spec->pin);
```

Parameters
:   | spec | GPIO specification from devicetree |
    | --- | --- |

Returns
:   a value from [gpio\_pin\_get()](#ga154a4ea3d3084910f02df31dc0779be6)

## [◆ ](#ga0fc52723b78019258bb306c771c430a1)gpio\_pin\_get\_raw()

| | int gpio\_pin\_get\_raw | ( | const struct [device](structdevice.md) \* | *port*, | | --- | --- | --- | --- | |  |  | [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) | *pin* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Get physical level of an input pin.

A low physical level on the pin will be interpreted as value 0. A high physical level will be interpreted as value 1. This function ignores GPIO\_ACTIVE\_LOW flag.

Parameters
:   | port | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pin | Pin number. |

Return values
:   | 1 | If pin physical level is high. |
    | --- | --- |
    | 0 | If pin physical level is low. |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#ga9618f254365381063439a0e9c5e787cb)gpio\_pin\_interrupt\_configure()

| int gpio\_pin\_interrupt\_configure | ( | const struct [device](structdevice.md) \* | *port*, |
| --- | --- | --- | --- |
|  |  | [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) | *pin*, |
|  |  | [gpio\_flags\_t](#ga5f5cb5e7dae6d58e072bb450af029d2e) | *flags* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Configure pin interrupt.

Note
:   This function can also be used to configure interrupts on pins not controlled directly by the GPIO module. That is, pins which are routed to other modules such as I2C, SPI, UART.

Parameters
:   | port | Pointer to device structure for the driver instance. |
    | --- | --- |
    | pin | Pin number. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Interrupt configuration flags as defined by GPIO\_INT\_\*. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | If the operation is not implemented by the driver. |
    | -ENOTSUP | If any of the configuration options is not supported (unless otherwise directed by flag documentation). |
    | -EINVAL | Invalid argument. |
    | -EBUSY | Interrupt line required to configure pin interrupt is already in use. |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#ga24f0b4ad30e6a8c81f51a2813478c793)gpio\_pin\_interrupt\_configure\_dt()

| | int gpio\_pin\_interrupt\_configure\_dt | ( | const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | [gpio\_flags\_t](#ga5f5cb5e7dae6d58e072bb450af029d2e) | *flags* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Configure pin interrupts from a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")`.

This is equivalent to:

```
gpio_pin_interrupt_configure(spec->port, spec->pin, flags);
```

The spec->dt\_flags value is not used.

Parameters
:   | spec | GPIO specification from devicetree |
    | --- | --- |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | interrupt configuration flags |

Returns
:   a value from [gpio\_pin\_interrupt\_configure()](#ga9618f254365381063439a0e9c5e787cb)

## [◆ ](#ga1454bc223fc2200aff3c4aab7d747da2)gpio\_pin\_is\_input()

| | int gpio\_pin\_is\_input | ( | const struct [device](structdevice.md) \* | *port*, | | --- | --- | --- | --- | |  |  | [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) | *pin* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Check if `pin` is configured for input.

Parameters
:   | port | Pointer to device structure for the driver instance. |
    | --- | --- |
    | pin | Pin number to query the direction of |

Return values
:   | 1 | if `pin` is configured as [GPIO\_INPUT](#ga7be6a0cc9aa65da1d4ee5751b4085853). |
    | --- | --- |
    | 0 | if `pin` is not configured as [GPIO\_INPUT](#ga7be6a0cc9aa65da1d4ee5751b4085853). |
    | -ENOSYS | if the underlying driver does not support this call. |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#ga7aaec28a83cac63bd87fc94cc72664b1)gpio\_pin\_is\_input\_dt()

| | int gpio\_pin\_is\_input\_dt | ( | const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Check if a single pin from `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")` is configured for input.

This is equivalent to:

```
gpio_pin_is_input(spec->port, spec->pin);
```

Parameters
:   | spec | GPIO specification from devicetree. |
    | --- | --- |

Returns
:   A value from [gpio\_pin\_is\_input()](#ga1454bc223fc2200aff3c4aab7d747da2).

## [◆ ](#ga3b854d759180e222299ea445b401acc1)gpio\_pin\_is\_output()

| | int gpio\_pin\_is\_output | ( | const struct [device](structdevice.md) \* | *port*, | | --- | --- | --- | --- | |  |  | [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) | *pin* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Check if `pin` is configured for output.

Parameters
:   | port | Pointer to device structure for the driver instance. |
    | --- | --- |
    | pin | Pin number to query the direction of |

Return values
:   | 1 | if `pin` is configured as [GPIO\_OUTPUT](#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1). |
    | --- | --- |
    | 0 | if `pin` is not configured as [GPIO\_OUTPUT](#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1). |
    | -ENOSYS | if the underlying driver does not support this call. |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#ga2255c5681d17952ab89a4b6016d8e80d)gpio\_pin\_is\_output\_dt()

| | int gpio\_pin\_is\_output\_dt | ( | const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Check if a single pin from `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")` is configured for output.

This is equivalent to:

```
gpio_pin_is_output(spec->port, spec->pin);
```

Parameters
:   | spec | GPIO specification from devicetree. |
    | --- | --- |

Returns
:   A value from [gpio\_pin\_is\_output()](#ga3b854d759180e222299ea445b401acc1).

## [◆ ](#gabfab69282fb99be119760436f2d18a9b)gpio\_pin\_set()

| | int gpio\_pin\_set | ( | const struct [device](structdevice.md) \* | *port*, | | --- | --- | --- | --- | |  |  | [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) | *pin*, | |  |  | int | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Set logical level of an output pin.

Set logical level of an output pin taking into account GPIO\_ACTIVE\_LOW flag. Value 0 sets the pin in logical 0 / inactive state. Any value other than 0 sets the pin in logical 1 / active state. If pin is configured as Active High, the default, setting it in inactive state will force the pin to a low physical level. If pin is configured as Active Low, setting it in inactive state will force the pin to a high physical level.

Note: If pin is configured as Active High, [gpio\_pin\_set()](#gabfab69282fb99be119760436f2d18a9b) function is equivalent to [gpio\_pin\_set\_raw()](#gae28f0fa2576530083aa86d819d0d5cca).

Parameters
:   | port | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pin | Pin number. |
    | value | Value assigned to the pin. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#ga541064fb9e575c0c559c101754466fa8)gpio\_pin\_set\_dt()

| | int gpio\_pin\_set\_dt | ( | const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | int | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Set logical level of a output pin from a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")`.

This is equivalent to:

```
gpio_pin_set(spec->port, spec->pin, value);
```

Parameters
:   | spec | GPIO specification from devicetree |
    | --- | --- |
    | value | Value assigned to the pin. |

Returns
:   a value from [gpio\_pin\_set()](#gabfab69282fb99be119760436f2d18a9b)

## [◆ ](#gae28f0fa2576530083aa86d819d0d5cca)gpio\_pin\_set\_raw()

| | int gpio\_pin\_set\_raw | ( | const struct [device](structdevice.md) \* | *port*, | | --- | --- | --- | --- | |  |  | [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) | *pin*, | |  |  | int | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Set physical level of an output pin.

Writing value 0 to the pin will set it to a low physical level. Writing any value other than 0 will set it to a high physical level. This function ignores GPIO\_ACTIVE\_LOW flag.

Parameters
:   | port | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pin | Pin number. |
    | value | Value assigned to the pin. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#gaabf948471d313ff19410f1741dd16957)gpio\_pin\_toggle()

| | int gpio\_pin\_toggle | ( | const struct [device](structdevice.md) \* | *port*, | | --- | --- | --- | --- | |  |  | [gpio\_pin\_t](#ga38179eb7a46a743c12cfac28f347fb34) | *pin* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Toggle pin level.

Parameters
:   | port | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pin | Pin number. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#ga3272e866489da6c2e12c48f803c59e81)gpio\_pin\_toggle\_dt()

| | int gpio\_pin\_toggle\_dt | ( | const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \* | *spec* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Toggle pin level from a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")`.

This is equivalent to:

```
gpio_pin_toggle(spec->port, spec->pin);
```

Parameters
:   | spec | GPIO specification from devicetree |
    | --- | --- |

Returns
:   a value from [gpio\_pin\_toggle()](#gaabf948471d313ff19410f1741dd16957)

## [◆ ](#gac1660707a44cc8a3aa08b25685b4b20b)gpio\_port\_clear\_bits()

| | int gpio\_port\_clear\_bits | ( | const struct [device](structdevice.md) \* | *port*, | | --- | --- | --- | --- | |  |  | [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) | *pins* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Set logical level of selected output pins to inactive.

Parameters
:   | port | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pins | Value indicating which pins will be modified. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#ga9d2c9daeec7ce127fc786ead566ad27f)gpio\_port\_clear\_bits\_raw()

| int gpio\_port\_clear\_bits\_raw | ( | const struct [device](structdevice.md) \* | *port*, |
| --- | --- | --- | --- |
|  |  | [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) | *pins* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Set physical level of selected output pins to low.

Parameters
:   | port | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pins | Value indicating which pins will be modified. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#gae578c8163fb8fe5600d1ca9e5d7526b1)gpio\_port\_get()

| | int gpio\_port\_get | ( | const struct [device](structdevice.md) \* | *port*, | | --- | --- | --- | --- | |  |  | [gpio\_port\_value\_t](#gabcebe24c93486896e1dfc2459ec25693) \* | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Get logical level of all input pins in a port.

Get logical level of an input pin taking into account GPIO\_ACTIVE\_LOW flag. If pin is configured as Active High, a low physical level will be interpreted as logical value 0. If pin is configured as Active Low, a low physical level will be interpreted as logical value 1.

Value of a pin with index n will be represented by bit n in the returned port value.

Parameters
:   | port | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | value | Pointer to a variable where pin values will be stored. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#gad2b2945dbe6987ac425e000721a894c4)gpio\_port\_get\_direction()

| int gpio\_port\_get\_direction | ( | const struct [device](structdevice.md) \* | *port*, |
| --- | --- | --- | --- |
|  |  | [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) | *map*, |
|  |  | [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) \* | *inputs*, |
|  |  | [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) \* | *outputs* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Get direction of select pins in a port.

Retrieve direction of each pin specified in `map`.

If `inputs` or `outputs` is NULL, then this function does not get the respective input or output direction information.

Parameters
:   | port | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | map | Bitmap of pin directions to query. |
    | inputs | Pointer to a variable where input directions will be stored. |
    | outputs | Pointer to a variable where output directions will be stored. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -ENOSYS | if the underlying driver does not support this call. |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#gae2a49b36cae2e17fc665a3bd844f50b4)gpio\_port\_get\_raw()

| int gpio\_port\_get\_raw | ( | const struct [device](structdevice.md) \* | *port*, |
| --- | --- | --- | --- |
|  |  | [gpio\_port\_value\_t](#gabcebe24c93486896e1dfc2459ec25693) \* | *value* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Get physical level of all input pins in a port.

A low physical level on the pin will be interpreted as value 0. A high physical level will be interpreted as value 1. This function ignores GPIO\_ACTIVE\_LOW flag.

Value of a pin with index n will be represented by bit n in the returned port value.

Parameters
:   | port | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | value | Pointer to a variable where pin values will be stored. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#ga570b669af237df991c4a55cff6ec3253)gpio\_port\_set\_bits()

| | int gpio\_port\_set\_bits | ( | const struct [device](structdevice.md) \* | *port*, | | --- | --- | --- | --- | |  |  | [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) | *pins* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Set logical level of selected output pins to active.

Parameters
:   | port | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pins | Value indicating which pins will be modified. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#ga18e6ca0df95566fecc0633efb04a075a)gpio\_port\_set\_bits\_raw()

| int gpio\_port\_set\_bits\_raw | ( | const struct [device](structdevice.md) \* | *port*, |
| --- | --- | --- | --- |
|  |  | [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) | *pins* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Set physical level of selected output pins to high.

Parameters
:   | port | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pins | Value indicating which pins will be modified. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#ga77880d217f5dd1fc1c72ce791254449b)gpio\_port\_set\_clr\_bits()

| | int gpio\_port\_set\_clr\_bits | ( | const struct [device](structdevice.md) \* | *port*, | | --- | --- | --- | --- | |  |  | [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) | *set\_pins*, | |  |  | [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) | *clear\_pins* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Set logical level of selected output pins.

Parameters
:   | port | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | set\_pins | Value indicating which pins will be set to active. |
    | clear\_pins | Value indicating which pins will be set to inactive. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#ga6e7ca22e83a70d3ddcf0de068b377c2d)gpio\_port\_set\_clr\_bits\_raw()

| | int gpio\_port\_set\_clr\_bits\_raw | ( | const struct [device](structdevice.md) \* | *port*, | | --- | --- | --- | --- | |  |  | [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) | *set\_pins*, | |  |  | [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) | *clear\_pins* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Set physical level of selected output pins.

Parameters
:   | port | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | set\_pins | Value indicating which pins will be set to high. |
    | clear\_pins | Value indicating which pins will be set to low. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#gac653e70270019d599732ab78693dd1fd)gpio\_port\_set\_masked()

| | int gpio\_port\_set\_masked | ( | const struct [device](structdevice.md) \* | *port*, | | --- | --- | --- | --- | |  |  | [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) | *mask*, | |  |  | [gpio\_port\_value\_t](#gabcebe24c93486896e1dfc2459ec25693) | *value* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Set logical level of output pins in a port.

Set logical level of an output pin taking into account GPIO\_ACTIVE\_LOW flag. Value 0 sets the pin in logical 0 / inactive state. Value 1 sets the pin in logical 1 / active state. If pin is configured as Active High, the default, setting it in inactive state will force the pin to a low physical level. If pin is configured as Active Low, setting it in inactive state will force the pin to a high physical level.

Pin with index n is represented by bit n in mask and value parameter.

Parameters
:   | port | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | mask | Mask indicating which pins will be modified. |
    | value | Value assigned to the output pins. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#ga9e7b50d720fda362941acc1e3b3b2922)gpio\_port\_set\_masked\_raw()

| int gpio\_port\_set\_masked\_raw | ( | const struct [device](structdevice.md) \* | *port*, |
| --- | --- | --- | --- |
|  |  | [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) | *mask*, |
|  |  | [gpio\_port\_value\_t](#gabcebe24c93486896e1dfc2459ec25693) | *value* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Set physical level of output pins in a port.

Writing value 0 to the pin will set it to a low physical level. Writing value 1 will set it to a high physical level. This function ignores GPIO\_ACTIVE\_LOW flag.

Pin with index n is represented by bit n in mask and value parameter.

Parameters
:   | port | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | mask | Mask indicating which pins will be modified. |
    | value | Value assigned to the output pins. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#ga82977d8706fb9f464db455bd0e9ac2e4)gpio\_port\_toggle\_bits()

| int gpio\_port\_toggle\_bits | ( | const struct [device](structdevice.md) \* | *port*, |
| --- | --- | --- | --- |
|  |  | [gpio\_port\_pins\_t](#ga7f40ed51f14fd8000e9b52ab347b273f) | *pins* ) |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Toggle level of selected output pins.

Parameters
:   | port | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | pins | Value indicating which pins will be modified. |

Return values
:   | 0 | If successful. |
    | --- | --- |
    | -EIO | I/O error when accessing an external GPIO chip. |
    | -EWOULDBLOCK | if operation would block. |

## [◆ ](#gac1e94ba8faac79f469447e9b5d2f8c06)gpio\_remove\_callback()

| | int gpio\_remove\_callback | ( | const struct [device](structdevice.md) \* | *port*, | | --- | --- | --- | --- | |  |  | struct [gpio\_callback](structgpio__callback.md) \* | *callback* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Remove an application callback.

Parameters
:   | port | Pointer to the device structure for the driver instance. |
    | --- | --- |
    | callback | A valid application's callback structure pointer. |

Return values
:   | 0 | If successful |
    | --- | --- |
    | -ENOSYS | If driver does not implement the operation |
    | -errno | Other negative errno code on failure. |

Warning
:   It is explicitly permitted, within a callback handler, to remove the registration for the callback that is running, i.e. `callback`. Attempts to remove other registrations on the same device may result in undefined behavior, including failure to invoke callbacks that remain registered and unintended invocation of removed callbacks.

Note: enables to remove as many callbacks as added through [gpio\_add\_callback()](#ga05fd15af20386d69f9332354285b0cca).

## [◆ ](#ga2c9f8fee2addfc0aeeeeb011d534f304)gpio\_remove\_callback\_dt()

| | int gpio\_remove\_callback\_dt | ( | const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \* | *spec*, | | --- | --- | --- | --- | |  |  | struct [gpio\_callback](structgpio__callback.md) \* | *callback* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gpio.h](drivers_2gpio_8h.md)>`

Remove an application callback.

This is equivalent to:

```
gpio_remove_callback(spec->port, callback);
```

Parameters
:   | spec | GPIO specification from devicetree. |
    | --- | --- |
    | callback | A valid application's callback structure pointer. |

Returns
:   a value from [gpio\_remove\_callback()](#gac1e94ba8faac79f469447e9b5d2f8c06).

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
