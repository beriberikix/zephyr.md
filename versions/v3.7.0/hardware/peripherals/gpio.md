---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/gpio.html
original_path: hardware/peripherals/gpio.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# General-Purpose Input/Output (GPIO)

## Overview

## Configuration Options

Related configuration options:

- [`CONFIG_GPIO`](../../kconfig.md#CONFIG_GPIO "CONFIG_GPIO")

## API Reference

Related code samples

[Basic thread manipulation](../../samples/basic/threads/README.md#multi-thread-blinky "Spawn multiple threads that blink LEDs and print information to the console.")
:   Spawn multiple threads that blink LEDs and print information to the console.

[Blinky](../../samples/basic/blinky/README.md#blinky "Blink an LED forever using the GPIO API.")
:   Blink an LED forever using the GPIO API.

[Button](../../samples/basic/button/README.md#button "Handle GPIO inputs with interrupts.")
:   Handle GPIO inputs with interrupts.

[GPIO with custom Devicetree binding](../../samples/basic/custom_dts_binding/README.md#gpio-custom-dts-binding "Use custom Devicetree binding to control a GPIO.")
:   Use custom Devicetree binding to control a GPIO.

[HD44780 LCD controller](../../samples/drivers/lcd_hd44780/README.md#lcd-hd44780 "Control an HD44780-based LCD display using GPIO pins.")
:   Control an HD44780-based LCD display using GPIO pins.

[X-NUCLEO-53L0A1 shield](../../samples/shields/x_nucleo_53l0a1/README.md#x-nucleo-53l0a1 "Interact with the 7-segment display and VL53L0X ranging sensor of an X-NUCLEO-53L0A1 shield.")
:   Interact with the 7-segment display and VL53L0X ranging sensor of an X-NUCLEO-53L0A1 shield.

*group* GPIO Driver APIs
:   GPIO Driver APIs.

    **Since**
    :   1.0

    **Version**
    :   1.0.0

    GPIO input/output configuration flags

    GPIO\_INPUT
    :   Enables pin as input.

    GPIO\_OUTPUT
    :   Enables pin as output, no change to the output state.

    GPIO\_DISCONNECTED
    :   Disables pin for both input and output.

    GPIO\_OUTPUT\_LOW
    :   Configures GPIO pin as output and initializes it to a low state.

    GPIO\_OUTPUT\_HIGH
    :   Configures GPIO pin as output and initializes it to a high state.

    GPIO\_OUTPUT\_INACTIVE
    :   Configures GPIO pin as output and initializes it to a logic 0.

    GPIO\_OUTPUT\_ACTIVE
    :   Configures GPIO pin as output and initializes it to a logic 1.

    GPIO interrupt configuration flags

    The `GPIO_INT_*` flags are used to specify how input GPIO pins will trigger interrupts.

    The interrupts can be sensitive to pin physical or logical level. Interrupts sensitive to pin logical level take into account GPIO\_ACTIVE\_LOW flag. If a pin was configured as Active Low, physical level low will be considered as logical level 1 (an active state), physical level high will be considered as logical level 0 (an inactive state). The GPIO controller should reset the interrupt status, such as clearing the pending bit, etc, when configuring the interrupt triggering properties. Applications should use the `GPIO_INT_MODE_ENABLE_ONLY` and `GPIO_INT_MODE_DISABLE_ONLY` flags to enable and disable interrupts on the pin without changing any GPIO settings.

    GPIO\_INT\_DISABLE
    :   Disables GPIO pin interrupt.

    GPIO\_INT\_EDGE\_RISING
    :   Configures GPIO interrupt to be triggered on pin rising edge and enables it.

    GPIO\_INT\_EDGE\_FALLING
    :   Configures GPIO interrupt to be triggered on pin falling edge and enables it.

    GPIO\_INT\_EDGE\_BOTH
    :   Configures GPIO interrupt to be triggered on pin rising or falling edge and enables it.

    GPIO\_INT\_LEVEL\_LOW
    :   Configures GPIO interrupt to be triggered on pin physical level low and enables it.

    GPIO\_INT\_LEVEL\_HIGH
    :   Configures GPIO interrupt to be triggered on pin physical level high and enables it.

    GPIO\_INT\_EDGE\_TO\_INACTIVE
    :   Configures GPIO interrupt to be triggered on pin state change to logical level 0 and enables it.

    GPIO\_INT\_EDGE\_TO\_ACTIVE
    :   Configures GPIO interrupt to be triggered on pin state change to logical level 1 and enables it.

    GPIO\_INT\_LEVEL\_INACTIVE
    :   Configures GPIO interrupt to be triggered on pin logical level 0 and enables it.

    GPIO\_INT\_LEVEL\_ACTIVE
    :   Configures GPIO interrupt to be triggered on pin logical level 1 and enables it.

    GPIO pin active level flags

    GPIO\_ACTIVE\_LOW
    :   GPIO pin is active (has logical value ‘1’) in low state.

    GPIO\_ACTIVE\_HIGH
    :   GPIO pin is active (has logical value ‘1’) in high state.

    GPIO pin drive flags

    GPIO\_OPEN\_DRAIN
    :   Configures GPIO output in open drain mode (wired AND).

        Note

        ‘Open Drain’ mode also known as ‘Open Collector’ is an output configuration which behaves like a switch that is either connected to ground or disconnected.

    GPIO\_OPEN\_SOURCE
    :   Configures GPIO output in open source mode (wired OR).

        Note

        ‘Open Source’ is a term used by software engineers to describe output mode opposite to ‘Open Drain’. It behaves like a switch that is either connected to power supply or disconnected. There exist no corresponding hardware schematic and the term is generally unknown to hardware engineers.

    GPIO pin bias flags

    GPIO\_PULL\_UP
    :   Enables GPIO pin pull-up.

    GPIO\_PULL\_DOWN
    :   Enable GPIO pin pull-down.

    Unnamed Group

    STM32\_GPIO\_WKUP
    :   STM32 GPIO specific flags.

        The driver flags are encoded in the 8 upper bits of [gpio\_dt\_flags\_t](#group__gpio__interface_1gad435719dccdc37c05852960a7218fbd2) as follows:

        - Bit 8: Configure a GPIO pin to power on the system after Poweroff. Configures a GPIO pin to power on the system after Poweroff. This flag is reserved to GPIO pins that are associated with wake-up pins in STM32 PWR devicetree node, through the property “wkup-gpios”.

    Defines

    GPIO\_DT\_SPEC\_GET\_BY\_IDX(node\_id, prop, idx)
    :   Static initializer for a `[gpio_dt_spec](#structgpio__dt__spec)`.

        This returns a static initializer for a `[gpio_dt_spec](#structgpio__dt__spec)` structure given a devicetree node identifier, a property specifying a GPIO and an index.

        Example devicetree fragment:

        ```text
         n: node {
            foo-gpios = <&gpio0 1 GPIO_ACTIVE_LOW>,
                        <&gpio1 2 GPIO_ACTIVE_LOW>;
         }
        ```

        Example usage:

        ```text
         const struct gpio_dt_spec spec = GPIO_DT_SPEC_GET_BY_IDX(DT_NODELABEL(n),
                                                             foo_gpios, 1);
         // Initializes 'spec' to:
         // {
         //         .port = DEVICE_DT_GET(DT_NODELABEL(gpio1)),
         //         .pin = 2,
         //         .dt_flags = GPIO_ACTIVE_LOW
         // }
        ```

        The ‘gpio’ field must still be checked for readiness, e.g. using [device\_is\_ready()](../../kernel/drivers/index.md#group__device__model_1gaa4944bd850e90cbd52b0489f9b12edfb). It is an error to use this macro unless the node exists, has the given property, and that property specifies a GPIO controller, pin number, and flags as shown above.

        Parameters:
        :   - **node\_id** – devicetree node identifier
            - **prop** – lowercase-and-underscores property name
            - **idx** – logical index into “prop”

        Returns:
        :   static initializer for a struct [gpio\_dt\_spec](#structgpio__dt__spec) for the property

    GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, prop, idx, default\_value)
    :   Like [GPIO\_DT\_SPEC\_GET\_BY\_IDX()](#group__gpio__interface_1gacb1077b77aecf8f1a9c7636ea583c4cf), with a fallback to a default value.

        If the devicetree node identifier ‘node\_id’ refers to a node with a property ‘prop’, this expands to `[GPIO_DT_SPEC_GET_BY_IDX(node_id, prop, idx)](#group__gpio__interface_1gacb1077b77aecf8f1a9c7636ea583c4cf)`. The `default_value` parameter is not expanded in this case.

        Otherwise, this expands to `default_value`.

        Parameters:
        :   - **node\_id** – devicetree node identifier
            - **prop** – lowercase-and-underscores property name
            - **idx** – logical index into “prop”
            - **default\_value** – fallback value to expand to

        Returns:
        :   static initializer for a struct [gpio\_dt\_spec](#structgpio__dt__spec) for the property, or default\_value if the node or property do not exist

    GPIO\_DT\_SPEC\_GET(node\_id, prop)
    :   Equivalent to [GPIO\_DT\_SPEC\_GET\_BY\_IDX(node\_id, prop, 0)](#group__gpio__interface_1gacb1077b77aecf8f1a9c7636ea583c4cf).

        See also

        [GPIO\_DT\_SPEC\_GET\_BY\_IDX()](#group__gpio__interface_1gacb1077b77aecf8f1a9c7636ea583c4cf)

        Parameters:
        :   - **node\_id** – devicetree node identifier
            - **prop** – lowercase-and-underscores property name

        Returns:
        :   static initializer for a struct [gpio\_dt\_spec](#structgpio__dt__spec) for the property

    GPIO\_DT\_SPEC\_GET\_OR(node\_id, prop, default\_value)
    :   Equivalent to [GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, prop, 0, default\_value)](#group__gpio__interface_1ga3db4fa464e191016287f4c4d7eb9a983).

        See also

        [GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR()](#group__gpio__interface_1ga3db4fa464e191016287f4c4d7eb9a983)

        Parameters:
        :   - **node\_id** – devicetree node identifier
            - **prop** – lowercase-and-underscores property name
            - **default\_value** – fallback value to expand to

        Returns:
        :   static initializer for a struct [gpio\_dt\_spec](#structgpio__dt__spec) for the property

    GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, prop, idx)
    :   Static initializer for a `[gpio_dt_spec](#structgpio__dt__spec)` from a DT\_DRV\_COMPAT instance’s GPIO property at an index.

        See also

        [GPIO\_DT\_SPEC\_GET\_BY\_IDX()](#group__gpio__interface_1gacb1077b77aecf8f1a9c7636ea583c4cf)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **prop** – lowercase-and-underscores property name
            - **idx** – logical index into “prop”

        Returns:
        :   static initializer for a struct [gpio\_dt\_spec](#structgpio__dt__spec) for the property

    GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, prop, idx, default\_value)
    :   Static initializer for a `[gpio_dt_spec](#structgpio__dt__spec)` from a DT\_DRV\_COMPAT instance’s GPIO property at an index, with fallback.

        See also

        [GPIO\_DT\_SPEC\_GET\_BY\_IDX()](#group__gpio__interface_1gacb1077b77aecf8f1a9c7636ea583c4cf)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **prop** – lowercase-and-underscores property name
            - **idx** – logical index into “prop”
            - **default\_value** – fallback value to expand to

        Returns:
        :   static initializer for a struct [gpio\_dt\_spec](#structgpio__dt__spec) for the property

    GPIO\_DT\_SPEC\_INST\_GET(inst, prop)
    :   Equivalent to [GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, prop, 0)](#group__gpio__interface_1gabbdbef450f14fd0af73667e2728ad084).

        See also

        [GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX()](#group__gpio__interface_1gabbdbef450f14fd0af73667e2728ad084)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **prop** – lowercase-and-underscores property name

        Returns:
        :   static initializer for a struct [gpio\_dt\_spec](#structgpio__dt__spec) for the property

    GPIO\_DT\_SPEC\_INST\_GET\_OR(inst, prop, default\_value)
    :   Equivalent to [GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, prop, 0, default\_value)](#group__gpio__interface_1gaf07edf6bc88af18e9976c76f6c3c3bf1).

        See also

        [GPIO\_DT\_SPEC\_INST\_GET\_BY\_IDX()](#group__gpio__interface_1gabbdbef450f14fd0af73667e2728ad084)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **prop** – lowercase-and-underscores property name
            - **default\_value** – fallback value to expand to

        Returns:
        :   static initializer for a struct [gpio\_dt\_spec](#structgpio__dt__spec) for the property

    GPIO\_DT\_RESERVED\_RANGES\_NGPIOS(node\_id, ngpios)
    :   Makes a bitmask of reserved GPIOs from DT `"gpio-reserved-ranges"` property and `"ngpios"` argument.

        This macro returns the value as a bitmask of the `"gpio-reserved-ranges"` property. This property defines the disabled (or ‘reserved’) GPIOs in the range `0`…ngpios-1 and is specified as an array of value’s pairs that define the start offset and size of the reserved ranges.

        For example, setting “gpio-reserved-ranges = <3 2>, <10 1>;” means that GPIO offsets 3, 4 and 10 cannot be used even if `ngpios` = <18>.

        The implementation constraint is inherited from common DT limitations: a maximum of 64 pairs can be used (with result limited to bitsize of [gpio\_port\_pins\_t](#group__gpio__interface_1ga7f40ed51f14fd8000e9b52ab347b273f) type).

        NB: Due to the nature of C macros, some incorrect tuple definitions (for example, overlapping or out of range) will produce undefined results.

        Also be aware that if `ngpios` is less than 32 (bit size of DT int type), then all unused MSBs outside the range defined by `ngpios` will be marked as reserved too.

        Example devicetree fragment:

        ```devicetree
        a {
                compatible = "some,gpio-controller";
                ngpios = <32>;
                gpio-reserved-ranges = <0  4>, <5  3>, <9  5>, <11 2>, <15 2>,
                                        <18 2>, <21 1>, <23 1>, <25 4>, <30 2>;
        };

        b {
                compatible = "some,gpio-controller";
                ngpios = <18>;
                gpio-reserved-ranges = <3 2>, <10 1>;
        };
        ```

        Example usage:

        ```c
        struct some_config {
                uint32_t ngpios;
                uint32_t gpios_reserved;
        };

        static const struct some_config dev_cfg_a = {
                .ngpios = DT_PROP_OR(DT_LABEL(a), ngpios, 0),
                .gpios_reserved = GPIO_DT_RESERVED_RANGES_NGPIOS(DT_LABEL(a),
                                        DT_PROP(DT_LABEL(a), ngpios)),
        };

        static const struct some_config dev_cfg_b = {
                .ngpios = DT_PROP_OR(DT_LABEL(b), ngpios, 0),
                .gpios_reserved = GPIO_DT_RESERVED_RANGES_NGPIOS(DT_LABEL(b),
                                        DT_PROP(DT_LABEL(b), ngpios)),
        };
        ```

        This expands to:

        ```c
        struct some_config {
                uint32_t ngpios;
                uint32_t gpios_reserved;
        };

        static const struct some_config dev_cfg_a = {
                .ngpios = 32,
                .gpios_reserved = 0xdeadbeef,
                               // 0b1101 1110 1010 1101 1011 1110 1110 1111

        static const struct some_config dev_cfg_b = {
                .ngpios = 18,
                .gpios_reserved = 0xfffc0418,
                               // 0b1111 1111 1111 1100 0000 0100 0001 1000
                               // unused MSBs were marked as reserved too
        };
        ```

        Parameters:
        :   - **node\_id** – GPIO controller node identifier.
            - **ngpios** – number of GPIOs.

        Returns:
        :   the bitmask of reserved gpios

    GPIO\_DT\_RESERVED\_RANGES(node\_id)
    :   Makes a bitmask of reserved GPIOs from the `"gpio-reserved-ranges"` and `"ngpios"` DT properties values.

        Parameters:
        :   - **node\_id** – GPIO controller node identifier.

        Returns:
        :   the bitmask of reserved gpios

    GPIO\_DT\_INST\_RESERVED\_RANGES\_NGPIOS(inst, ngpios)
    :   Makes a bitmask of reserved GPIOs from a DT\_DRV\_COMPAT instance’s `"gpio-reserved-ranges"` property and `"ngpios"` argument.

        See also

        [GPIO\_DT\_RESERVED\_RANGES()](#group__gpio__interface_1ga648fcc0633d57b52d3df683efda98440)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **ngpios** – number of GPIOs

        Returns:
        :   the bitmask of reserved gpios

    GPIO\_DT\_INST\_RESERVED\_RANGES(inst)
    :   Make a bitmask of reserved GPIOs from a DT\_DRV\_COMPAT instance’s GPIO `"gpio-reserved-ranges"` and `"ngpios"` properties.

        See also

        [GPIO\_DT\_RESERVED\_RANGES()](#group__gpio__interface_1ga648fcc0633d57b52d3df683efda98440)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number

        Returns:
        :   the bitmask of reserved gpios

    GPIO\_DT\_PORT\_PIN\_MASK\_NGPIOS\_EXC(node\_id, ngpios)
    :   Makes a bitmask of allowed GPIOs from DT `"gpio-reserved-ranges"` property and `"ngpios"` argument.

        This macro is paired with [GPIO\_DT\_RESERVED\_RANGES\_NGPIOS()](#group__gpio__interface_1ga439c3d29aa585b00853aba6d6416028a), however unlike the latter, it returns a bitmask of ALLOWED gpios.

        Example devicetree fragment:

        ```devicetree
        a {
           compatible = "some,gpio-controller";
           ngpios = <32>;
           gpio-reserved-ranges = <0 8>, <9 5>, <15 16>;
        };
        ```

        Example usage:

        ```c
        struct some_config {
           uint32_t port_pin_mask;
        };

        static const struct some_config dev_cfg = {
           .port_pin_mask = GPIO_DT_PORT_PIN_MASK_NGPIOS_EXC(
                                   DT_LABEL(a), 32),
        };
        ```

        This expands to:

        ```c
        struct some_config {
           uint32_t port_pin_mask;
        };

        static const struct some_config dev_cfg = {
           .port_pin_mask = 0x80004100,
                           // 0b1000 0000 0000 0000 0100 0001 00000 000
        };
        ```

        Parameters:
        :   - **node\_id** – GPIO controller node identifier.
            - **ngpios** – number of GPIOs

        Returns:
        :   the bitmask of allowed gpios

    GPIO\_DT\_INST\_PORT\_PIN\_MASK\_NGPIOS\_EXC(inst, ngpios)
    :   Makes a bitmask of allowed GPIOs from a DT\_DRV\_COMPAT instance’s `"gpio-reserved-ranges"` property and `"ngpios"` argument.

        See also

        GPIO\_DT\_NGPIOS\_PORT\_PIN\_MASK\_EXC()

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **ngpios** – number of GPIOs

        Returns:
        :   the bitmask of allowed gpios

    GPIO\_MAX\_PINS\_PER\_PORT
    :   Maximum number of pins that are supported by `[gpio_port_pins_t](#group__gpio__interface_1ga7f40ed51f14fd8000e9b52ab347b273f)`.

    GPIO\_DT\_FLAGS\_MASK
    :   Mask for DT GPIO flags.

    GPIO\_INT\_WAKEUP
    :   Configures GPIO interrupt to wakeup the system from low power mode.

    Typedefs

    typedef uint32\_t gpio\_port\_pins\_t
    :   Identifies a set of pins associated with a port.

        The pin with index n is present in the set if and only if the bit identified by (1U << n) is set.

    typedef uint32\_t gpio\_port\_value\_t
    :   Provides values for a set of pins associated with a port.

        The value for a pin with index n is high (physical mode) or active (logical mode) if and only if the bit identified by (1U << n) is set. Otherwise the value for the pin is low (physical mode) or inactive (logical mode).

        Values of this type are often paired with a `[gpio_port_pins_t](#group__gpio__interface_1ga7f40ed51f14fd8000e9b52ab347b273f)` value that specifies which encoded pin values are valid for the operation.

    typedef uint8\_t gpio\_pin\_t
    :   Provides a type to hold a GPIO pin index.

        This reduced-size type is sufficient to record a pin number, e.g. from a devicetree GPIOS property.

    typedef uint16\_t gpio\_dt\_flags\_t
    :   Provides a type to hold GPIO devicetree flags.

        All GPIO flags that can be expressed in devicetree fit in the low 16 bits of the full flags field, so use a reduced-size type to record that part of a GPIOS property.

        The lower 8 bits are used for standard flags. The upper 8 bits are reserved for SoC specific flags.

    typedef uint32\_t gpio\_flags\_t
    :   Provides a type to hold GPIO configuration flags.

        This type is sufficient to hold all flags used to control GPIO configuration, whether pin or interrupt.

    typedef void (\*gpio\_callback\_handler\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, struct [gpio\_callback](#c.gpio_callback) \*cb, [gpio\_port\_pins\_t](#c.gpio_port_pins_t) pins)
    :   Define the application callback handler function signature.

        Note: cb pointer can be used to retrieve private data through [CONTAINER\_OF()](../../kernel/util/index.md#group__sys-util_1gac5bc561d1bfd1bf68877fe577779bd2f) if original struct [gpio\_callback](#structgpio__callback) is stored in another private structure.

        Param port:
        :   Device struct for the GPIO device.

        Param cb:
        :   Original struct [gpio\_callback](#structgpio__callback) owning this handler

        Param pins:
        :   Mask of pins that triggers the callback handler

    Functions

    static inline bool gpio\_is\_ready\_dt(const struct [gpio\_dt\_spec](#c.gpio_dt_spec) \*spec)
    :   Validate that GPIO port is ready.

        Parameters:
        :   - **spec** – GPIO specification from devicetree

        Return values:
        :   - **true** – if the GPIO spec is ready for use.
            - **false** – if the GPIO spec is not ready for use.

    int gpio\_pin\_interrupt\_configure(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_pin\_t](#c.gpio_pin_t) pin, [gpio\_flags\_t](#c.gpio_flags_t) flags)
    :   Configure pin interrupt.

        Note

        This function can also be used to configure interrupts on pins not controlled directly by the GPIO module. That is, pins which are routed to other modules such as I2C, SPI, UART.

        Parameters:
        :   - **port** – Pointer to device structure for the driver instance.
            - **pin** – Pin number.
            - **flags** – Interrupt configuration flags as defined by GPIO\_INT\_\*.

        Return values:
        :   - **0** – If successful.
            - **-ENOSYS** – If the operation is not implemented by the driver.
            - **-ENOTSUP** – If any of the configuration options is not supported (unless otherwise directed by flag documentation).
            - **-EINVAL** – Invalid argument.
            - **-EBUSY** – Interrupt line required to configure pin interrupt is already in use.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    static inline int gpio\_pin\_interrupt\_configure\_dt(const struct [gpio\_dt\_spec](#c.gpio_dt_spec) \*spec, [gpio\_flags\_t](#c.gpio_flags_t) flags)
    :   Configure pin interrupts from a `[gpio_dt_spec](#structgpio__dt__spec)`.

        This is equivalent to:

        ```text
        gpio_pin_interrupt_configure(spec->port, spec->pin, flags);
        ```

        The `spec->dt_flags` value is not used.

        Parameters:
        :   - **spec** – GPIO specification from devicetree
            - **flags** – interrupt configuration flags

        Returns:
        :   a value from [gpio\_pin\_interrupt\_configure()](#group__gpio__interface_1ga9618f254365381063439a0e9c5e787cb)

    int gpio\_pin\_configure(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_pin\_t](#c.gpio_pin_t) pin, [gpio\_flags\_t](#c.gpio_flags_t) flags)
    :   Configure a single pin.

        Parameters:
        :   - **port** – Pointer to device structure for the driver instance.
            - **pin** – Pin number to configure.
            - **flags** – Flags for pin configuration: ‘GPIO input/output configuration flags’, ‘GPIO pin drive flags’, ‘GPIO pin bias flags’.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – if any of the configuration options is not supported (unless otherwise directed by flag documentation).
            - **-EINVAL** – Invalid argument.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    static inline int gpio\_pin\_configure\_dt(const struct [gpio\_dt\_spec](#c.gpio_dt_spec) \*spec, [gpio\_flags\_t](#c.gpio_flags_t) extra\_flags)
    :   Configure a single pin from a `[gpio_dt_spec](#structgpio__dt__spec)` and some extra flags.

        This is equivalent to:

        ```text
        gpio_pin_configure(spec->port, spec->pin, spec->dt_flags | extra_flags);
        ```

        Parameters:
        :   - **spec** – GPIO specification from devicetree
            - **extra\_flags** – additional flags

        Returns:
        :   a value from [gpio\_pin\_configure()](#group__gpio__interface_1gaed4a2051d76db7eead8ed1719ce2ba33)

    int gpio\_port\_get\_direction(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_port\_pins\_t](#c.gpio_port_pins_t) map, [gpio\_port\_pins\_t](#c.gpio_port_pins_t) \*inputs, [gpio\_port\_pins\_t](#c.gpio_port_pins_t) \*outputs)
    :   Get direction of select pins in a port.

        Retrieve direction of each pin specified in `map`.

        If `inputs` or `outputs` is NULL, then this function does not get the respective input or output direction information.

        Parameters:
        :   - **port** – Pointer to the device structure for the driver instance.
            - **map** – Bitmap of pin directions to query.
            - **inputs** – Pointer to a variable where input directions will be stored.
            - **outputs** – Pointer to a variable where output directions will be stored.

        Return values:
        :   - **0** – If successful.
            - **-ENOSYS** – if the underlying driver does not support this call.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    static inline int gpio\_pin\_is\_input(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_pin\_t](#c.gpio_pin_t) pin)
    :   Check if `pin` is configured for input.

        Parameters:
        :   - **port** – Pointer to device structure for the driver instance.
            - **pin** – Pin number to query the direction of

        Return values:
        :   - **1** – if `pin` is configured as [GPIO\_INPUT](#group__gpio__interface_1ga7be6a0cc9aa65da1d4ee5751b4085853).
            - **0** – if `pin` is not configured as [GPIO\_INPUT](#group__gpio__interface_1ga7be6a0cc9aa65da1d4ee5751b4085853).
            - **-ENOSYS** – if the underlying driver does not support this call.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    static inline int gpio\_pin\_is\_input\_dt(const struct [gpio\_dt\_spec](#c.gpio_dt_spec) \*spec)
    :   Check if a single pin from `[gpio_dt_spec](#structgpio__dt__spec)` is configured for input.

        This is equivalent to:

        ```text
        gpio_pin_is_input(spec->port, spec->pin);
        ```

        Parameters:
        :   - **spec** – GPIO specification from devicetree.

        Returns:
        :   A value from [gpio\_pin\_is\_input()](#group__gpio__interface_1ga1454bc223fc2200aff3c4aab7d747da2).

    static inline int gpio\_pin\_is\_output(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_pin\_t](#c.gpio_pin_t) pin)
    :   Check if `pin` is configured for output.

        Parameters:
        :   - **port** – Pointer to device structure for the driver instance.
            - **pin** – Pin number to query the direction of

        Return values:
        :   - **1** – if `pin` is configured as [GPIO\_OUTPUT](#group__gpio__interface_1ga0db9fe8a278e6ab7c5c6f14fe58e5eb1).
            - **0** – if `pin` is not configured as [GPIO\_OUTPUT](#group__gpio__interface_1ga0db9fe8a278e6ab7c5c6f14fe58e5eb1).
            - **-ENOSYS** – if the underlying driver does not support this call.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    static inline int gpio\_pin\_is\_output\_dt(const struct [gpio\_dt\_spec](#c.gpio_dt_spec) \*spec)
    :   Check if a single pin from `[gpio_dt_spec](#structgpio__dt__spec)` is configured for output.

        This is equivalent to:

        ```text
        gpio_pin_is_output(spec->port, spec->pin);
        ```

        Parameters:
        :   - **spec** – GPIO specification from devicetree.

        Returns:
        :   A value from [gpio\_pin\_is\_output()](#group__gpio__interface_1ga3b854d759180e222299ea445b401acc1).

    int gpio\_pin\_get\_config(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_pin\_t](#c.gpio_pin_t) pin, [gpio\_flags\_t](#c.gpio_flags_t) \*flags)
    :   Get a configuration of a single pin.

        Parameters:
        :   - **port** – Pointer to device structure for the driver instance.
            - **pin** – Pin number which configuration is get.
            - **flags** – Pointer to variable in which the current configuration will be stored if function is successful.

        Return values:
        :   - **0** – If successful.
            - **-ENOSYS** – if getting current pin configuration is not implemented by the driver.
            - **-EINVAL** – Invalid argument.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    static inline int gpio\_pin\_get\_config\_dt(const struct [gpio\_dt\_spec](#c.gpio_dt_spec) \*spec, [gpio\_flags\_t](#c.gpio_flags_t) \*flags)
    :   Get a configuration of a single pin from a `[gpio_dt_spec](#structgpio__dt__spec)`.

        This is equivalent to:

        ```text
        gpio_pin_get_config(spec->port, spec->pin, flags);
        ```

        Parameters:
        :   - **spec** – GPIO specification from devicetree
            - **flags** – Pointer to variable in which the current configuration will be stored if function is successful.

        Returns:
        :   a value from [gpio\_pin\_configure()](#group__gpio__interface_1gaed4a2051d76db7eead8ed1719ce2ba33)

    int gpio\_port\_get\_raw(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_port\_value\_t](#c.gpio_port_value_t) \*value)
    :   Get physical level of all input pins in a port.

        A low physical level on the pin will be interpreted as value 0. A high physical level will be interpreted as value 1. This function ignores GPIO\_ACTIVE\_LOW flag.

        Value of a pin with index n will be represented by bit n in the returned port value.

        Parameters:
        :   - **port** – Pointer to the device structure for the driver instance.
            - **value** – Pointer to a variable where pin values will be stored.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    static inline int gpio\_port\_get(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_port\_value\_t](#c.gpio_port_value_t) \*value)
    :   Get logical level of all input pins in a port.

        Get logical level of an input pin taking into account GPIO\_ACTIVE\_LOW flag. If pin is configured as Active High, a low physical level will be interpreted as logical value 0. If pin is configured as Active Low, a low physical level will be interpreted as logical value 1.

        Value of a pin with index n will be represented by bit n in the returned port value.

        Parameters:
        :   - **port** – Pointer to the device structure for the driver instance.
            - **value** – Pointer to a variable where pin values will be stored.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    int gpio\_port\_set\_masked\_raw(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_port\_pins\_t](#c.gpio_port_pins_t) mask, [gpio\_port\_value\_t](#c.gpio_port_value_t) value)
    :   Set physical level of output pins in a port.

        Writing value 0 to the pin will set it to a low physical level. Writing value 1 will set it to a high physical level. This function ignores GPIO\_ACTIVE\_LOW flag.

        Pin with index n is represented by bit n in mask and value parameter.

        Parameters:
        :   - **port** – Pointer to the device structure for the driver instance.
            - **mask** – Mask indicating which pins will be modified.
            - **value** – Value assigned to the output pins.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    static inline int gpio\_port\_set\_masked(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_port\_pins\_t](#c.gpio_port_pins_t) mask, [gpio\_port\_value\_t](#c.gpio_port_value_t) value)
    :   Set logical level of output pins in a port.

        Set logical level of an output pin taking into account GPIO\_ACTIVE\_LOW flag. Value 0 sets the pin in logical 0 / inactive state. Value 1 sets the pin in logical 1 / active state. If pin is configured as Active High, the default, setting it in inactive state will force the pin to a low physical level. If pin is configured as Active Low, setting it in inactive state will force the pin to a high physical level.

        Pin with index n is represented by bit n in mask and value parameter.

        Parameters:
        :   - **port** – Pointer to the device structure for the driver instance.
            - **mask** – Mask indicating which pins will be modified.
            - **value** – Value assigned to the output pins.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    int gpio\_port\_set\_bits\_raw(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_port\_pins\_t](#c.gpio_port_pins_t) pins)
    :   Set physical level of selected output pins to high.

        Parameters:
        :   - **port** – Pointer to the device structure for the driver instance.
            - **pins** – Value indicating which pins will be modified.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    static inline int gpio\_port\_set\_bits(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_port\_pins\_t](#c.gpio_port_pins_t) pins)
    :   Set logical level of selected output pins to active.

        Parameters:
        :   - **port** – Pointer to the device structure for the driver instance.
            - **pins** – Value indicating which pins will be modified.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    int gpio\_port\_clear\_bits\_raw(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_port\_pins\_t](#c.gpio_port_pins_t) pins)
    :   Set physical level of selected output pins to low.

        Parameters:
        :   - **port** – Pointer to the device structure for the driver instance.
            - **pins** – Value indicating which pins will be modified.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    static inline int gpio\_port\_clear\_bits(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_port\_pins\_t](#c.gpio_port_pins_t) pins)
    :   Set logical level of selected output pins to inactive.

        Parameters:
        :   - **port** – Pointer to the device structure for the driver instance.
            - **pins** – Value indicating which pins will be modified.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    int gpio\_port\_toggle\_bits(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_port\_pins\_t](#c.gpio_port_pins_t) pins)
    :   Toggle level of selected output pins.

        Parameters:
        :   - **port** – Pointer to the device structure for the driver instance.
            - **pins** – Value indicating which pins will be modified.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    static inline int gpio\_port\_set\_clr\_bits\_raw(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_port\_pins\_t](#c.gpio_port_pins_t) set\_pins, [gpio\_port\_pins\_t](#c.gpio_port_pins_t) clear\_pins)
    :   Set physical level of selected output pins.

        Parameters:
        :   - **port** – Pointer to the device structure for the driver instance.
            - **set\_pins** – Value indicating which pins will be set to high.
            - **clear\_pins** – Value indicating which pins will be set to low.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    static inline int gpio\_port\_set\_clr\_bits(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_port\_pins\_t](#c.gpio_port_pins_t) set\_pins, [gpio\_port\_pins\_t](#c.gpio_port_pins_t) clear\_pins)
    :   Set logical level of selected output pins.

        Parameters:
        :   - **port** – Pointer to the device structure for the driver instance.
            - **set\_pins** – Value indicating which pins will be set to active.
            - **clear\_pins** – Value indicating which pins will be set to inactive.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    static inline int gpio\_pin\_get\_raw(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_pin\_t](#c.gpio_pin_t) pin)
    :   Get physical level of an input pin.

        A low physical level on the pin will be interpreted as value 0. A high physical level will be interpreted as value 1. This function ignores GPIO\_ACTIVE\_LOW flag.

        Parameters:
        :   - **port** – Pointer to the device structure for the driver instance.
            - **pin** – Pin number.

        Return values:
        :   - **1** – If pin physical level is high.
            - **0** – If pin physical level is low.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    static inline int gpio\_pin\_get(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_pin\_t](#c.gpio_pin_t) pin)
    :   Get logical level of an input pin.

        Get logical level of an input pin taking into account GPIO\_ACTIVE\_LOW flag. If pin is configured as Active High, a low physical level will be interpreted as logical value 0. If pin is configured as Active Low, a low physical level will be interpreted as logical value 1.

        Note: If pin is configured as Active High, the default, [gpio\_pin\_get()](#group__gpio__interface_1ga154a4ea3d3084910f02df31dc0779be6) function is equivalent to [gpio\_pin\_get\_raw()](#group__gpio__interface_1ga0fc52723b78019258bb306c771c430a1).

        Parameters:
        :   - **port** – Pointer to the device structure for the driver instance.
            - **pin** – Pin number.

        Return values:
        :   - **1** – If pin logical value is 1 / active.
            - **0** – If pin logical value is 0 / inactive.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    static inline int gpio\_pin\_get\_dt(const struct [gpio\_dt\_spec](#c.gpio_dt_spec) \*spec)
    :   Get logical level of an input pin from a `[gpio_dt_spec](#structgpio__dt__spec)`.

        This is equivalent to:

        ```text
        gpio_pin_get(spec->port, spec->pin);
        ```

        Parameters:
        :   - **spec** – GPIO specification from devicetree

        Returns:
        :   a value from [gpio\_pin\_get()](#group__gpio__interface_1ga154a4ea3d3084910f02df31dc0779be6)

    static inline int gpio\_pin\_set\_raw(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_pin\_t](#c.gpio_pin_t) pin, int value)
    :   Set physical level of an output pin.

        Writing value 0 to the pin will set it to a low physical level. Writing any value other than 0 will set it to a high physical level. This function ignores GPIO\_ACTIVE\_LOW flag.

        Parameters:
        :   - **port** – Pointer to the device structure for the driver instance.
            - **pin** – Pin number.
            - **value** – Value assigned to the pin.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    static inline int gpio\_pin\_set(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_pin\_t](#c.gpio_pin_t) pin, int value)
    :   Set logical level of an output pin.

        Set logical level of an output pin taking into account GPIO\_ACTIVE\_LOW flag. Value 0 sets the pin in logical 0 / inactive state. Any value other than 0 sets the pin in logical 1 / active state. If pin is configured as Active High, the default, setting it in inactive state will force the pin to a low physical level. If pin is configured as Active Low, setting it in inactive state will force the pin to a high physical level.

        Note: If pin is configured as Active High, [gpio\_pin\_set()](#group__gpio__interface_1gabfab69282fb99be119760436f2d18a9b) function is equivalent to [gpio\_pin\_set\_raw()](#group__gpio__interface_1gae28f0fa2576530083aa86d819d0d5cca).

        Parameters:
        :   - **port** – Pointer to the device structure for the driver instance.
            - **pin** – Pin number.
            - **value** – Value assigned to the pin.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    static inline int gpio\_pin\_set\_dt(const struct [gpio\_dt\_spec](#c.gpio_dt_spec) \*spec, int value)
    :   Set logical level of a output pin from a `[gpio_dt_spec](#structgpio__dt__spec)`.

        This is equivalent to:

        ```text
        gpio_pin_set(spec->port, spec->pin, value);
        ```

        Parameters:
        :   - **spec** – GPIO specification from devicetree
            - **value** – Value assigned to the pin.

        Returns:
        :   a value from [gpio\_pin\_set()](#group__gpio__interface_1gabfab69282fb99be119760436f2d18a9b)

    static inline int gpio\_pin\_toggle(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, [gpio\_pin\_t](#c.gpio_pin_t) pin)
    :   Toggle pin level.

        Parameters:
        :   - **port** – Pointer to the device structure for the driver instance.
            - **pin** – Pin number.

        Return values:
        :   - **0** – If successful.
            - **-EIO** – I/O error when accessing an external GPIO chip.
            - **-EWOULDBLOCK** – if operation would block.

    static inline int gpio\_pin\_toggle\_dt(const struct [gpio\_dt\_spec](#c.gpio_dt_spec) \*spec)
    :   Toggle pin level from a `[gpio_dt_spec](#structgpio__dt__spec)`.

        This is equivalent to:

        ```text
        gpio_pin_toggle(spec->port, spec->pin);
        ```

        Parameters:
        :   - **spec** – GPIO specification from devicetree

        Returns:
        :   a value from [gpio\_pin\_toggle()](#group__gpio__interface_1gaabf948471d313ff19410f1741dd16957)

    static inline void gpio\_init\_callback(struct [gpio\_callback](#c.gpio_callback) \*callback, [gpio\_callback\_handler\_t](#c.gpio_callback_handler_t) handler, [gpio\_port\_pins\_t](#c.gpio_port_pins_t) pin\_mask)
    :   Helper to initialize a struct [gpio\_callback](#structgpio__callback) properly.

        Parameters:
        :   - **callback** – A valid Application’s callback structure pointer.
            - **handler** – A valid handler function pointer.
            - **pin\_mask** – A bit mask of relevant pins for the handler

    static inline int gpio\_add\_callback(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, struct [gpio\_callback](#c.gpio_callback) \*callback)
    :   Add an application callback.

        Note: enables to add as many callback as needed on the same port.

        Note

        Callbacks may be added to the device from within a callback handler invocation, but whether they are invoked for the current GPIO event is not specified.

        Parameters:
        :   - **port** – Pointer to the device structure for the driver instance.
            - **callback** – A valid Application’s callback structure pointer.

        Return values:
        :   - **0** – If successful
            - **-ENOSYS** – If driver does not implement the operation
            - **-errno** – Other negative errno code on failure.

    static inline int gpio\_add\_callback\_dt(const struct [gpio\_dt\_spec](#c.gpio_dt_spec) \*spec, struct [gpio\_callback](#c.gpio_callback) \*callback)
    :   Add an application callback.

        This is equivalent to:

        ```text
        gpio_add_callback(spec->port, callback);
        ```

        Parameters:
        :   - **spec** – GPIO specification from devicetree.
            - **callback** – A valid application’s callback structure pointer.

        Returns:
        :   a value from [gpio\_add\_callback()](#group__gpio__interface_1ga05fd15af20386d69f9332354285b0cca).

    static inline int gpio\_remove\_callback(const struct [device](../../kernel/drivers/index.md#c.device "device") \*port, struct [gpio\_callback](#c.gpio_callback) \*callback)
    :   Remove an application callback.

        Note: enables to remove as many callbacks as added through [gpio\_add\_callback()](#group__gpio__interface_1ga05fd15af20386d69f9332354285b0cca).

        Warning

        It is explicitly permitted, within a callback handler, to remove the registration for the callback that is running, i.e. `callback`. Attempts to remove other registrations on the same device may result in undefined behavior, including failure to invoke callbacks that remain registered and unintended invocation of removed callbacks.

        Parameters:
        :   - **port** – Pointer to the device structure for the driver instance.
            - **callback** – A valid application’s callback structure pointer.

        Return values:
        :   - **0** – If successful
            - **-ENOSYS** – If driver does not implement the operation
            - **-errno** – Other negative errno code on failure.

    static inline int gpio\_remove\_callback\_dt(const struct [gpio\_dt\_spec](#c.gpio_dt_spec) \*spec, struct [gpio\_callback](#c.gpio_callback) \*callback)
    :   Remove an application callback.

        This is equivalent to:

        ```text
        gpio_remove_callback(spec->port, callback);
        ```

        Parameters:
        :   - **spec** – GPIO specification from devicetree.
            - **callback** – A valid application’s callback structure pointer.

        Returns:
        :   a value from [gpio\_remove\_callback()](#group__gpio__interface_1gac1e94ba8faac79f469447e9b5d2f8c06).

    int gpio\_get\_pending\_int(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Function to get pending interrupts.

        The purpose of this function is to return the interrupt status register for the device. This is especially useful when waking up from low power states to check the wake up source.

        Parameters:
        :   - **dev** – Pointer to the device structure for the driver instance.

        Return values:
        :   - **status** – != 0 if at least one gpio interrupt is pending.
            - **0** – if no gpio interrupt is pending.
            - **-ENOSYS** – If driver does not implement the operation

    struct gpio\_dt\_spec
    :   *#include <gpio.h>*

        Container for GPIO pin information specified in devicetree.

        This type contains a pointer to a GPIO device, pin number for a pin controlled by that device, and the subset of pin configuration flags which may be given in devicetree.

        See also

        [GPIO\_DT\_SPEC\_GET\_BY\_IDX](#group__gpio__interface_1gacb1077b77aecf8f1a9c7636ea583c4cf)

        See also

        [GPIO\_DT\_SPEC\_GET\_BY\_IDX\_OR](#group__gpio__interface_1ga3db4fa464e191016287f4c4d7eb9a983)

        See also

        [GPIO\_DT\_SPEC\_GET](#group__gpio__interface_1ga2fa6bb5880f46984f9fc29c70f7d503e)

        See also

        [GPIO\_DT\_SPEC\_GET\_OR](#group__gpio__interface_1ga26b2205aa82819df1d80a22761352e71)

        Public Members

        const struct [device](../../kernel/drivers/index.md#c.device "device") \*port
        :   GPIO device controlling the pin.

        [gpio\_pin\_t](#c.gpio_pin_t) pin
        :   The pin’s number on the device.

        [gpio\_dt\_flags\_t](#c.gpio_dt_flags_t) dt\_flags
        :   The pin’s configuration flags as specified in devicetree.

    struct gpio\_driver\_config
    :   *#include <gpio.h>*

        This structure is common to all GPIO drivers and is expected to be the first element in the object pointed to by the config field in the device structure.

        Public Members

        [gpio\_port\_pins\_t](#c.gpio_port_pins_t) port\_pin\_mask
        :   Mask identifying pins supported by the controller.

            Initialization of this mask is the responsibility of device instance generation in the driver.

    struct gpio\_driver\_data
    :   *#include <gpio.h>*

        This structure is common to all GPIO drivers and is expected to be the first element in the driver’s struct driver\_data declaration.

        Public Members

        [gpio\_port\_pins\_t](#c.gpio_port_pins_t) invert
        :   Mask identifying pins that are configured as active low.

            Management of this mask is the responsibility of the wrapper functions in this header.

    struct gpio\_callback
    :   *#include <gpio.h>*

        GPIO callback structure.

        Used to register a callback in the driver instance callback list. As many callbacks as needed can be added as long as each of them are unique pointers of struct [gpio\_callback](#structgpio__callback). Beware such structure should not be allocated on stack.

        Note: To help setting it, see [gpio\_init\_callback()](#group__gpio__interface_1ga7a7dd7c1f3a2135a9f378e1c34b6232c) below

        Public Members

        [sys\_snode\_t](../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   This is meant to be used in the driver and the user should not mess with it (see drivers/gpio/gpio\_utils.h).

        [gpio\_callback\_handler\_t](#c.gpio_callback_handler_t) handler
        :   Actual callback function being called when relevant.

        [gpio\_port\_pins\_t](#c.gpio_port_pins_t) pin\_mask
        :   A mask of pins the callback is interested in, if 0 the callback will never be called.

            Such pin\_mask can be modified whenever necessary by the owner, and thus will affect the handler being called or not. The selected pins must be configured to trigger an interrupt.
