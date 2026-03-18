---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2gpio_8h.html
original_path: doxygen/html/drivers_2gpio_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gpio.h File Reference

Public APIs for GPIO drivers.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <[zephyr/dt-bindings/gpio/gpio.h](dt-bindings_2gpio_2gpio_8h_source.md)>`  
`#include <syscalls/gpio.h>`

[Go to the source code of this file.](drivers_2gpio_8h_source.md)

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
| #define | [GPIO\_DT\_SPEC\_GET\_BY\_IDX](group__gpio__interface.md#gacb1077b77aecf8f1a9c7636ea583c4cf)(node\_id, prop, idx) |
|  | Static initializer for a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")`. |
| #define | [GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR](group__gpio__interface.md#ga3db4fa464e191016287f4c4d7eb9a983)(node\_id, prop, idx, default\_value) |
|  | Like [GPIO\_DT\_SPEC\_GET\_BY\_IDX()](group__gpio__interface.md#gacb1077b77aecf8f1a9c7636ea583c4cf "Static initializer for a gpio_dt_spec."), with a fallback to a default value. |
| #define | [GPIO\_DT\_SPEC\_GET](group__gpio__interface.md#ga2fa6bb5880f46984f9fc29c70f7d503e)(node\_id, prop) |
|  | Equivalent to [GPIO\_DT\_SPEC\_GET\_BY\_IDX(node\_id, prop, 0)](group__gpio__interface.md#gacb1077b77aecf8f1a9c7636ea583c4cf "Static initializer for a gpio_dt_spec."). |
| #define | [GPIO\_DT\_SPEC\_GET\_OR](group__gpio__interface.md#ga26b2205aa82819df1d80a22761352e71)(node\_id, prop, default\_value) |
|  | Equivalent to [GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, prop, 0, default\_value)](group__gpio__interface.md#ga3db4fa464e191016287f4c4d7eb9a983 "Like GPIO_DT_SPEC_GET_BY_IDX(), with a fallback to a default value."). |
| #define | [GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX](group__gpio__interface.md#gabbdbef450f14fd0af73667e2728ad084)(inst, prop, idx) |
|  | Static initializer for a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")` from a DT\_DRV\_COMPAT instance's GPIO property at an index. |
| #define | [GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR](group__gpio__interface.md#gaf07edf6bc88af18e9976c76f6c3c3bf1)(inst, prop, idx, default\_value) |
|  | Static initializer for a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")` from a DT\_DRV\_COMPAT instance's GPIO property at an index, with fallback. |
| #define | [GPIO\_DT\_SPEC\_INST\_GET](group__gpio__interface.md#ga168f5c6e39a0111191f606a9a0826e89)(inst, prop) |
|  | Equivalent to [GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, prop, 0)](group__gpio__interface.md#gabbdbef450f14fd0af73667e2728ad084 "Static initializer for a gpio_dt_spec from a DT_DRV_COMPAT instance's GPIO property at an index."). |
| #define | [GPIO\_DT\_SPEC\_INST\_GET\_OR](group__gpio__interface.md#gae6b4a354c3cf0e042a390aac4bc37c69)(inst, prop, default\_value) |
|  | Equivalent to [GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, prop, 0, default\_value)](group__gpio__interface.md#gaf07edf6bc88af18e9976c76f6c3c3bf1 "Static initializer for a gpio_dt_spec from a DT_DRV_COMPAT instance's GPIO property at an index,..."). |
| #define | [GPIO\_DT\_RESERVED\_RANGES\_NGPIOS](group__gpio__interface.md#ga439c3d29aa585b00853aba6d6416028a)(node\_id, ngpios) |
|  | Makes a bitmask of reserved GPIOs from DT `"gpio-reserved-ranges"` property and `"ngpios"` argument. |
| #define | [GPIO\_DT\_RESERVED\_RANGES](group__gpio__interface.md#ga648fcc0633d57b52d3df683efda98440)(node\_id) |
|  | Makes a bitmask of reserved GPIOs from the `"gpio-reserved-ranges"` and `"ngpios"` DT properties values. |
| #define | [GPIO\_DT\_INST\_RESERVED\_RANGES\_NGPIOS](group__gpio__interface.md#gaebaea00f6f7649c61651e8d50c7cdf07)(inst, ngpios) |
|  | Makes a bitmask of reserved GPIOs from a DT\_DRV\_COMPAT instance's `"gpio-reserved-ranges"` property and `"ngpios"` argument. |
| #define | [GPIO\_DT\_INST\_RESERVED\_RANGES](group__gpio__interface.md#ga9136b467eaddcc734bc6a0a7d8b34e14)(inst) |
|  | Make a bitmask of reserved GPIOs from a DT\_DRV\_COMPAT instance's GPIO `"gpio-reserved-ranges"` and `"ngpios"` properties. |
| #define | [GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC](group__gpio__interface.md#ga274e09d7082d97b2f90c6a7fd4b71d49)(node\_id, ngpios) |
|  | Makes a bitmask of allowed GPIOs from DT `"gpio-reserved-ranges"` property and `"ngpios"` argument. |
| #define | [GPIO\_DT\_INST\_PORT\_PIN\_MASK\_NGPIOS\_EXC](group__gpio__interface.md#ga856fe8042e496a39ef3a4e19fff2c4ce)(inst, ngpios) |
|  | Makes a bitmask of allowed GPIOs from a DT\_DRV\_COMPAT instance's `"gpio-reserved-ranges"` property and `"ngpios"` argument. |
| #define | [GPIO\_MAX\_PINS\_PER\_PORT](group__gpio__interface.md#ga1449ba90eaec5e6144fe4faae21f2e3f)   ([sizeof](retained__mem_8h.md#a8c945f5e523f7f88fe4d09bfe304240e)([gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f)) \* \_\_CHAR\_BIT\_\_) |
|  | Maximum number of pins that are supported by [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f "Identifies a set of pins associated with a port."). |
| GPIO input/output configuration flags | |
| #define | [GPIO\_INPUT](group__gpio__interface.md#ga7be6a0cc9aa65da1d4ee5751b4085853)   (1U << 16) |
|  | Enables pin as input. |
| #define | [GPIO\_OUTPUT](group__gpio__interface.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1)   (1U << 17) |
|  | Enables pin as output, no change to the output state. |
| #define | [GPIO\_DISCONNECTED](group__gpio__interface.md#gaf82306c09450f6933366c4b821db21ed)   0 |
|  | Disables pin for both input and output. |
| #define | [GPIO\_OUTPUT\_LOW](group__gpio__interface.md#gaf85baf9f9c1ba554324b4cd7064487b0)   ([GPIO\_OUTPUT](group__gpio__interface.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1) | GPIO\_OUTPUT\_INIT\_LOW) |
|  | Configures GPIO pin as output and initializes it to a low state. |
| #define | [GPIO\_OUTPUT\_HIGH](group__gpio__interface.md#ga10d31f204c0e927017d571352422fb09)   ([GPIO\_OUTPUT](group__gpio__interface.md#ga0db9fe8a278e6ab7c5c6f14fe58e5eb1) | GPIO\_OUTPUT\_INIT\_HIGH) |
|  | Configures GPIO pin as output and initializes it to a high state. |
| #define | [GPIO\_OUTPUT\_INACTIVE](group__gpio__interface.md#ga1e1d6be5f2f788f89468a0ce8b854634) |
|  | Configures GPIO pin as output and initializes it to a logic 0. |
| #define | [GPIO\_OUTPUT\_ACTIVE](group__gpio__interface.md#ga0f5cc126d6a690eb3e303eb29aa718ce) |
|  | Configures GPIO pin as output and initializes it to a logic 1. |
| GPIO interrupt configuration flags | |
| The GPIO\_INT\_\* flags are used to specify how input GPIO pins will trigger interrupts.  The interrupts can be sensitive to pin physical or logical level. Interrupts sensitive to pin logical level take into account GPIO\_ACTIVE\_LOW flag. If a pin was configured as Active Low, physical level low will be considered as logical level 1 (an active state), physical level high will be considered as logical level 0 (an inactive state). The GPIO controller should reset the interrupt status, such as clearing the pending bit, etc, when configuring the interrupt triggering properties. Applications should use the GPIO\_INT\_MODE\_ENABLE\_ONLY and GPIO\_INT\_MODE\_DISABLE\_ONLY flags to enable and disable interrupts on the pin without changing any GPIO settings. | |
| #define | [GPIO\_INT\_DISABLE](group__gpio__interface.md#ga91657faac28f9b213105dd61a419dd5a)   (1U << 21) |
|  | Disables GPIO pin interrupt. |
| #define | [GPIO\_INT\_EDGE\_RISING](group__gpio__interface.md#gaed642a4e482f73aa917477370d0e241b) |
|  | Configures GPIO interrupt to be triggered on pin rising edge and enables it. |
| #define | [GPIO\_INT\_EDGE\_FALLING](group__gpio__interface.md#ga73bed10383a27d4a03feb300e64af8e8) |
|  | Configures GPIO interrupt to be triggered on pin falling edge and enables it. |
| #define | [GPIO\_INT\_EDGE\_BOTH](group__gpio__interface.md#ga10fa307ab17d02819108165a09f8e08b) |
|  | Configures GPIO interrupt to be triggered on pin rising or falling edge and enables it. |
| #define | [GPIO\_INT\_LEVEL\_LOW](group__gpio__interface.md#gaddbb5ad576875af9c2d73b73df55c893) |
|  | Configures GPIO interrupt to be triggered on pin physical level low and enables it. |
| #define | [GPIO\_INT\_LEVEL\_HIGH](group__gpio__interface.md#ga233690d9a6a64bc9f804e3caa6d4a88f) |
|  | Configures GPIO interrupt to be triggered on pin physical level high and enables it. |
| #define | [GPIO\_INT\_EDGE\_TO\_INACTIVE](group__gpio__interface.md#ga7b922529a3cb9396b0d82ca823e9d010) |
|  | Configures GPIO interrupt to be triggered on pin state change to logical level 0 and enables it. |
| #define | [GPIO\_INT\_EDGE\_TO\_ACTIVE](group__gpio__interface.md#ga35d2ff0e041236d82004a4bb2b5bf634) |
|  | Configures GPIO interrupt to be triggered on pin state change to logical level 1 and enables it. |
| #define | [GPIO\_INT\_LEVEL\_INACTIVE](group__gpio__interface.md#gacb9bb1b63f172af2da7eb193e234c4f2) |
|  | Configures GPIO interrupt to be triggered on pin logical level 0 and enables it. |
| #define | [GPIO\_INT\_LEVEL\_ACTIVE](group__gpio__interface.md#gae51c68ff83959994bb942bb253505ca1) |
|  | Configures GPIO interrupt to be triggered on pin logical level 1 and enables it. |

| Typedefs | |
| --- | --- |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) |
|  | Identifies a set of pins associated with a port. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) |
|  | Provides values for a set of pins associated with a port. |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) |
|  | Provides a type to hold a GPIO pin index. |
| typedef [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [gpio\_dt\_flags\_t](group__gpio__interface.md#gad435719dccdc37c05852960a7218fbd2) |
|  | Provides a type to hold GPIO devicetree flags. |
| typedef [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) |
|  | Provides a type to hold GPIO configuration flags. |
| typedef void(\* | [gpio\_callback\_handler\_t](group__gpio__interface.md#gaf0aa40279d32b1b8332f2f23a39510af)) (const struct [device](structdevice.md) \*port, struct [gpio\_callback](structgpio__callback.md) \*cb, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins) |
|  | Define the application callback handler function signature. |

| Functions | |
| --- | --- |
| static [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [gpio\_is\_ready\_dt](group__gpio__interface.md#gaaec9ad17c08a0d527d66445fe82d8327) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec) |
|  | Validate that GPIO port is ready. |
| int | [gpio\_pin\_interrupt\_configure](group__gpio__interface.md#ga9618f254365381063439a0e9c5e787cb) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin, [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Configure pin interrupt. |
| static int | [gpio\_pin\_interrupt\_configure\_dt](group__gpio__interface.md#ga24f0b4ad30e6a8c81f51a2813478c793) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec, [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Configure pin interrupts from a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")`. |
| int | [gpio\_pin\_configure](group__gpio__interface.md#gaed4a2051d76db7eead8ed1719ce2ba33) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin, [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Configure a single pin. |
| static int | [gpio\_pin\_configure\_dt](group__gpio__interface.md#ga423db4f985098ddcaa504ec430e91913) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec, [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) extra\_flags) |
|  | Configure a single pin from a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")` and some extra flags. |
| int | [gpio\_port\_get\_direction](group__gpio__interface.md#gad2b2945dbe6987ac425e000721a894c4) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) map, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*inputs, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) \*outputs) |
|  | Get direction of select pins in a port. |
| static int | [gpio\_pin\_is\_input](group__gpio__interface.md#ga1454bc223fc2200aff3c4aab7d747da2) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin) |
|  | Check if `pin` is configured for input. |
| static int | [gpio\_pin\_is\_input\_dt](group__gpio__interface.md#ga7aaec28a83cac63bd87fc94cc72664b1) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec) |
|  | Check if a single pin from `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")` is configured for input. |
| static int | [gpio\_pin\_is\_output](group__gpio__interface.md#ga3b854d759180e222299ea445b401acc1) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin) |
|  | Check if `pin` is configured for output. |
| static int | [gpio\_pin\_is\_output\_dt](group__gpio__interface.md#ga2255c5681d17952ab89a4b6016d8e80d) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec) |
|  | Check if a single pin from `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")` is configured for output. |
| int | [gpio\_pin\_get\_config](group__gpio__interface.md#ga133284b60a13c6dc50b87c1d04259f5e) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin, [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Get a configuration of a single pin. |
| static int | [gpio\_pin\_get\_config\_dt](group__gpio__interface.md#ga820448aa4be8b14839bc6a00c9f34bb4) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec, [gpio\_flags\_t](group__gpio__interface.md#ga5f5cb5e7dae6d58e072bb450af029d2e) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Get a configuration of a single pin from a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")`. |
| int | [gpio\_port\_get\_raw](group__gpio__interface.md#gae2a49b36cae2e17fc665a3bd844f50b4) (const struct [device](structdevice.md) \*port, [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value) |
|  | Get physical level of all input pins in a port. |
| static int | [gpio\_port\_get](group__gpio__interface.md#gae578c8163fb8fe5600d1ca9e5d7526b1) (const struct [device](structdevice.md) \*port, [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) \*value) |
|  | Get logical level of all input pins in a port. |
| int | [gpio\_port\_set\_masked\_raw](group__gpio__interface.md#ga9e7b50d720fda362941acc1e3b3b2922) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask, [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value) |
|  | Set physical level of output pins in a port. |
| static int | [gpio\_port\_set\_masked](group__gpio__interface.md#gac653e70270019d599732ab78693dd1fd) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) mask, [gpio\_port\_value\_t](group__gpio__interface.md#gabcebe24c93486896e1dfc2459ec25693) value) |
|  | Set logical level of output pins in a port. |
| int | [gpio\_port\_set\_bits\_raw](group__gpio__interface.md#ga18e6ca0df95566fecc0633efb04a075a) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins) |
|  | Set physical level of selected output pins to high. |
| static int | [gpio\_port\_set\_bits](group__gpio__interface.md#ga570b669af237df991c4a55cff6ec3253) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins) |
|  | Set logical level of selected output pins to active. |
| int | [gpio\_port\_clear\_bits\_raw](group__gpio__interface.md#ga9d2c9daeec7ce127fc786ead566ad27f) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins) |
|  | Set physical level of selected output pins to low. |
| static int | [gpio\_port\_clear\_bits](group__gpio__interface.md#gac1660707a44cc8a3aa08b25685b4b20b) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins) |
|  | Set logical level of selected output pins to inactive. |
| int | [gpio\_port\_toggle\_bits](group__gpio__interface.md#ga82977d8706fb9f464db455bd0e9ac2e4) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pins) |
|  | Toggle level of selected output pins. |
| static int | [gpio\_port\_set\_clr\_bits\_raw](group__gpio__interface.md#ga6e7ca22e83a70d3ddcf0de068b377c2d) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) set\_pins, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) clear\_pins) |
|  | Set physical level of selected output pins. |
| static int | [gpio\_port\_set\_clr\_bits](group__gpio__interface.md#ga77880d217f5dd1fc1c72ce791254449b) (const struct [device](structdevice.md) \*port, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) set\_pins, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) clear\_pins) |
|  | Set logical level of selected output pins. |
| static int | [gpio\_pin\_get\_raw](group__gpio__interface.md#ga0fc52723b78019258bb306c771c430a1) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin) |
|  | Get physical level of an input pin. |
| static int | [gpio\_pin\_get](group__gpio__interface.md#ga154a4ea3d3084910f02df31dc0779be6) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin) |
|  | Get logical level of an input pin. |
| static int | [gpio\_pin\_get\_dt](group__gpio__interface.md#gaabeb2d0d98856c7ff78be36651d6bbc1) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec) |
|  | Get logical level of an input pin from a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")`. |
| static int | [gpio\_pin\_set\_raw](group__gpio__interface.md#gae28f0fa2576530083aa86d819d0d5cca) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin, int value) |
|  | Set physical level of an output pin. |
| static int | [gpio\_pin\_set](group__gpio__interface.md#gabfab69282fb99be119760436f2d18a9b) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin, int value) |
|  | Set logical level of an output pin. |
| static int | [gpio\_pin\_set\_dt](group__gpio__interface.md#ga541064fb9e575c0c559c101754466fa8) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec, int value) |
|  | Set logical level of a output pin from a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")`. |
| static int | [gpio\_pin\_toggle](group__gpio__interface.md#gaabf948471d313ff19410f1741dd16957) (const struct [device](structdevice.md) \*port, [gpio\_pin\_t](group__gpio__interface.md#ga38179eb7a46a743c12cfac28f347fb34) pin) |
|  | Toggle pin level. |
| static int | [gpio\_pin\_toggle\_dt](group__gpio__interface.md#ga3272e866489da6c2e12c48f803c59e81) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec) |
|  | Toggle pin level from a `[gpio_dt_spec](structgpio__dt__spec.md "Container for GPIO pin information specified in devicetree.")`. |
| static void | [gpio\_init\_callback](group__gpio__interface.md#ga7a7dd7c1f3a2135a9f378e1c34b6232c) (struct [gpio\_callback](structgpio__callback.md) \*callback, [gpio\_callback\_handler\_t](group__gpio__interface.md#gaf0aa40279d32b1b8332f2f23a39510af) handler, [gpio\_port\_pins\_t](group__gpio__interface.md#ga7f40ed51f14fd8000e9b52ab347b273f) pin\_mask) |
|  | Helper to initialize a struct [gpio\_callback](structgpio__callback.md "GPIO callback structure.") properly. |
| static int | [gpio\_add\_callback](group__gpio__interface.md#ga05fd15af20386d69f9332354285b0cca) (const struct [device](structdevice.md) \*port, struct [gpio\_callback](structgpio__callback.md) \*callback) |
|  | Add an application callback. |
| static int | [gpio\_add\_callback\_dt](group__gpio__interface.md#ga54845eb95bc9636c3e6ff285300b6979) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec, struct [gpio\_callback](structgpio__callback.md) \*callback) |
|  | Add an application callback. |
| static int | [gpio\_remove\_callback](group__gpio__interface.md#gac1e94ba8faac79f469447e9b5d2f8c06) (const struct [device](structdevice.md) \*port, struct [gpio\_callback](structgpio__callback.md) \*callback) |
|  | Remove an application callback. |
| static int | [gpio\_remove\_callback\_dt](group__gpio__interface.md#ga2c9f8fee2addfc0aeeeeb011d534f304) (const struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*spec, struct [gpio\_callback](structgpio__callback.md) \*callback) |
|  | Remove an application callback. |
| int | [gpio\_get\_pending\_int](group__gpio__interface.md#ga3f9e45de172a27f49c31a072c0c241e1) (const struct [device](structdevice.md) \*dev) |
|  | Function to get pending interrupts. |

## Detailed Description

Public APIs for GPIO drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [gpio.h](drivers_2gpio_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1
