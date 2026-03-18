---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/pwm.html
original_path: hardware/peripherals/pwm.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Pulse Width Modulation (PWM)

## Overview

## API Reference

Related code samples

[Fade LED](../../samples/basic/fade_led/README.md#fade-led "Fade an LED using the PWM API.")
:   Fade an LED using the PWM API.

[PWM Blinky](../../samples/basic/blinky_pwm/README.md#pwm-blinky "Blink an LED using the PWM API.")
:   Blink an LED using the PWM API.

[PWM RGB LED](../../samples/basic/rgb_led/README.md#rgb-led "Drive an RGB LED using the PWM API.")
:   Drive an RGB LED using the PWM API.

[Servomotor](../../samples/basic/servo_motor/README.md#servo-motor "Drive a servomotor using the PWM API.")
:   Drive a servomotor using the PWM API.

*group* pwm\_interface
:   PWM Interface.

    PWM capture configuration flags

    PWM\_CAPTURE\_TYPE\_PERIOD
    :   PWM pin capture captures period.

    PWM\_CAPTURE\_TYPE\_PULSE
    :   PWM pin capture captures pulse width.

    PWM\_CAPTURE\_TYPE\_BOTH
    :   PWM pin capture captures both period and pulse width.

    PWM\_CAPTURE\_MODE\_SINGLE
    :   PWM pin capture captures a single period/pulse width.

    PWM\_CAPTURE\_MODE\_CONTINUOUS
    :   PWM pin capture captures period/pulse width continuously.

    PWM period set helpers

    The period cell in the PWM specifier needs to be provided in nanoseconds.

    However, in some applications it is more convenient to use another scale.

    PWM\_NSEC(x)
    :   Specify PWM period in nanoseconds.

    PWM\_USEC(x)
    :   Specify PWM period in microseconds.

    PWM\_MSEC(x)
    :   Specify PWM period in milliseconds.

    PWM\_SEC(x)
    :   Specify PWM period in seconds.

    PWM\_HZ(x)
    :   Specify PWM frequency in hertz.

    PWM\_KHZ(x)
    :   Specify PWM frequency in kilohertz.

    PWM polarity flags

    The `PWM_POLARITY_*` flags are used with [pwm\_set\_cycles()](#group__pwm__interface_1gaff280789f7b45fdefc354b3f841fe3ef), [pwm\_set()](#group__pwm__interface_1gadd9049c9a56cd9419736b3514e42dc01) or [pwm\_configure\_capture()](#group__pwm__interface_1ga9603146d7f9c2690c1e1983113d6c6bb) to specify the polarity of a PWM channel.

    The flags are on the lower 8bits of the [pwm\_flags\_t](#group__pwm__interface_1gae1dcfb878163da76041efcedf0960fa0)

    PWM\_POLARITY\_NORMAL
    :   PWM pin normal polarity (active-high pulse).

    PWM\_POLARITY\_INVERTED
    :   PWM pin inverted polarity (active-low pulse).

    Defines

    PWM\_DT\_SPEC\_GET\_BY\_NAME(node\_id, name)
    :   Static initializer for a struct [pwm\_dt\_spec](#structpwm__dt__spec).

        This returns a static initializer for a struct [pwm\_dt\_spec](#structpwm__dt__spec) given a devicetree node identifier and an index.

        Example devicetree fragment:

        ```devicetree
        n: node {
            pwms = <&pwm1 1 1000 PWM_POLARITY_NORMAL>,
                   <&pwm2 3 2000 PWM_POLARITY_INVERTED>;
            pwm-names = "alpha", "beta";
        };
        ```

        Example usage:

        ```c
        const struct pwm_dt_spec spec =
            PWM_DT_SPEC_GET_BY_NAME(DT_NODELABEL(n), alpha);

        // Initializes 'spec' to:
        // {
        //         .dev = DEVICE_DT_GET(DT_NODELABEL(pwm1)),
        //         .channel = 1,
        //         .period = 1000,
        //         .flags = PWM_POLARITY_NORMAL,
        // }
        ```

        The device (dev) must still be checked for readiness, e.g. using [device\_is\_ready()](../../kernel/drivers/index.md#group__device__model_1gaa4944bd850e90cbd52b0489f9b12edfb). It is an error to use this macro unless the node exists, has the ‘pwms’ property, and that ‘pwms’ property specifies a PWM controller, a channel, a period in nanoseconds and optionally flags.

        See also

        [PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME](#group__pwm__interface_1ga104a81a3481362d2da9046c0e93a8cd0)

        Parameters:
        :   - **node\_id** – Devicetree node identifier.
            - **name** – Lowercase-and-underscores name of a pwms element as defined by the node’s pwm-names property.

        Returns:
        :   Static initializer for a struct [pwm\_dt\_spec](#structpwm__dt__spec) for the property.

    PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME(inst, name)
    :   Static initializer for a struct [pwm\_dt\_spec](#structpwm__dt__spec) from a DT\_DRV\_COMPAT instance.

        See also

        [PWM\_DT\_SPEC\_GET\_BY\_NAME](#group__pwm__interface_1ga88b92c580860441c83d1b03db25fc4f1)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **name** – Lowercase-and-underscores name of a pwms element as defined by the node’s pwm-names property.

        Returns:
        :   Static initializer for a struct [pwm\_dt\_spec](#structpwm__dt__spec) for the property.

    PWM\_DT\_SPEC\_GET\_BY\_NAME\_OR(node\_id, name, default\_value)
    :   Like [PWM\_DT\_SPEC\_GET\_BY\_NAME()](#group__pwm__interface_1ga88b92c580860441c83d1b03db25fc4f1), with a fallback to a default value.

        If the devicetree node identifier ‘node\_id’ refers to a node with a property ‘pwms’, this expands to `[PWM_DT_SPEC_GET_BY_NAME(node_id, name)](#group__pwm__interface_1ga88b92c580860441c83d1b03db25fc4f1)`. The `default_value` parameter is not expanded in this case. Otherwise, this expands to `default_value`.

        See also

        [PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME\_OR](#group__pwm__interface_1gac00e53eccaf9eb515aed0921404adb31)

        Parameters:
        :   - **node\_id** – Devicetree node identifier.
            - **name** – Lowercase-and-underscores name of a pwms element as defined by the node’s pwm-names property
            - **default\_value** – Fallback value to expand to.

        Returns:
        :   Static initializer for a struct [pwm\_dt\_spec](#structpwm__dt__spec) for the property, or `default_value` if the node or property do not exist.

    PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME\_OR(inst, name, default\_value)
    :   Like [PWM\_DT\_SPEC\_INST\_GET\_BY\_NAME()](#group__pwm__interface_1ga104a81a3481362d2da9046c0e93a8cd0), with a fallback to a default value.

        See also

        [PWM\_DT\_SPEC\_GET\_BY\_NAME\_OR](#group__pwm__interface_1ga5557add2123a7138b64997cd070e0ee6)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **name** – Lowercase-and-underscores name of a pwms element as defined by the node’s pwm-names property.
            - **default\_value** – Fallback value to expand to.

        Returns:
        :   Static initializer for a struct [pwm\_dt\_spec](#structpwm__dt__spec) for the property, or `default_value` if the node or property do not exist.

    PWM\_DT\_SPEC\_GET\_BY\_IDX(node\_id, idx)
    :   Static initializer for a struct [pwm\_dt\_spec](#structpwm__dt__spec).

        This returns a static initializer for a struct [pwm\_dt\_spec](#structpwm__dt__spec) given a devicetree node identifier and an index.

        Example devicetree fragment:

        ```devicetree
        n: node {
            pwms = <&pwm1 1 1000 PWM_POLARITY_NORMAL>,
                   <&pwm2 3 2000 PWM_POLARITY_INVERTED>;
        };
        ```

        Example usage:

        ```c
        const struct pwm_dt_spec spec =
            PWM_DT_SPEC_GET_BY_IDX(DT_NODELABEL(n), 1);

        // Initializes 'spec' to:
        // {
        //         .dev = DEVICE_DT_GET(DT_NODELABEL(pwm2)),
        //         .channel = 3,
        //         .period = 2000,
        //         .flags = PWM_POLARITY_INVERTED,
        // }
        ```

        The device (dev) must still be checked for readiness, e.g. using [device\_is\_ready()](../../kernel/drivers/index.md#group__device__model_1gaa4944bd850e90cbd52b0489f9b12edfb). It is an error to use this macro unless the node exists, has the ‘pwms’ property, and that ‘pwms’ property specifies a PWM controller, a channel, a period in nanoseconds and optionally flags.

        See also

        [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX](#group__pwm__interface_1ga3c1c557fa4461e61f4a147fc72f87f8d)

        Parameters:
        :   - **node\_id** – Devicetree node identifier.
            - **idx** – Logical index into ‘pwms’ property.

        Returns:
        :   Static initializer for a struct [pwm\_dt\_spec](#structpwm__dt__spec) for the property.

    PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, idx)
    :   Static initializer for a struct [pwm\_dt\_spec](#structpwm__dt__spec) from a DT\_DRV\_COMPAT instance.

        See also

        [PWM\_DT\_SPEC\_GET\_BY\_IDX](#group__pwm__interface_1ga7e8375bcf95ae6a9500ce3aba4586de4)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **idx** – Logical index into ‘pwms’ property.

        Returns:
        :   Static initializer for a struct [pwm\_dt\_spec](#structpwm__dt__spec) for the property.

    PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, idx, default\_value)
    :   Like [PWM\_DT\_SPEC\_GET\_BY\_IDX()](#group__pwm__interface_1ga7e8375bcf95ae6a9500ce3aba4586de4), with a fallback to a default value.

        If the devicetree node identifier ‘node\_id’ refers to a node with a property ‘pwms’, this expands to `[PWM_DT_SPEC_GET_BY_IDX(node_id, idx)](#group__pwm__interface_1ga7e8375bcf95ae6a9500ce3aba4586de4)`. The `default_value` parameter is not expanded in this case. Otherwise, this expands to `default_value`.

        See also

        [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR](#group__pwm__interface_1ga7eeef648c3142fced48b7ab52c9c1ead)

        Parameters:
        :   - **node\_id** – Devicetree node identifier.
            - **idx** – Logical index into ‘pwms’ property.
            - **default\_value** – Fallback value to expand to.

        Returns:
        :   Static initializer for a struct [pwm\_dt\_spec](#structpwm__dt__spec) for the property, or `default_value` if the node or property do not exist.

    PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, idx, default\_value)
    :   Like [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX()](#group__pwm__interface_1ga3c1c557fa4461e61f4a147fc72f87f8d), with a fallback to a default value.

        See also

        [PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR](#group__pwm__interface_1gaf5808fd88b101208681820b53bca33e1)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **idx** – Logical index into ‘pwms’ property.
            - **default\_value** – Fallback value to expand to.

        Returns:
        :   Static initializer for a struct [pwm\_dt\_spec](#structpwm__dt__spec) for the property, or `default_value` if the node or property do not exist.

    PWM\_DT\_SPEC\_GET(node\_id)
    :   Equivalent to `[PWM_DT_SPEC_GET_BY_IDX(node_id, 0)](#group__pwm__interface_1ga7e8375bcf95ae6a9500ce3aba4586de4)`.

        See also

        [PWM\_DT\_SPEC\_GET\_BY\_IDX](#group__pwm__interface_1ga7e8375bcf95ae6a9500ce3aba4586de4)

        See also

        [PWM\_DT\_SPEC\_INST\_GET](#group__pwm__interface_1gaa346428c6cb1f11aafaa6306486e8a4b)

        Parameters:
        :   - **node\_id** – Devicetree node identifier.

        Returns:
        :   Static initializer for a struct [pwm\_dt\_spec](#structpwm__dt__spec) for the property.

    PWM\_DT\_SPEC\_INST\_GET(inst)
    :   Equivalent to `[PWM_DT_SPEC_INST_GET_BY_IDX(inst, 0)](#group__pwm__interface_1ga3c1c557fa4461e61f4a147fc72f87f8d)`.

        See also

        [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX](#group__pwm__interface_1ga3c1c557fa4461e61f4a147fc72f87f8d)

        See also

        [PWM\_DT\_SPEC\_GET](#group__pwm__interface_1ga59a79f0b77c5b71252bde126f333a84b)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number

        Returns:
        :   Static initializer for a struct [pwm\_dt\_spec](#structpwm__dt__spec) for the property.

    PWM\_DT\_SPEC\_GET\_OR(node\_id, default\_value)
    :   Equivalent to `[PWM_DT_SPEC_GET_BY_IDX_OR(node_id, 0, default_value)](#group__pwm__interface_1gaf5808fd88b101208681820b53bca33e1)`.

        See also

        [PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR](#group__pwm__interface_1gaf5808fd88b101208681820b53bca33e1)

        See also

        [PWM\_DT\_SPEC\_INST\_GET\_OR](#group__pwm__interface_1ga6bd84121715beb62a3ca2672dfae0630)

        Parameters:
        :   - **node\_id** – Devicetree node identifier.
            - **default\_value** – Fallback value to expand to.

        Returns:
        :   Static initializer for a struct [pwm\_dt\_spec](#structpwm__dt__spec) for the property.

    PWM\_DT\_SPEC\_INST\_GET\_OR(inst, default\_value)
    :   Equivalent to `[PWM_DT_SPEC_INST_GET_BY_IDX_OR(inst, 0, default_value)](#group__pwm__interface_1ga7eeef648c3142fced48b7ab52c9c1ead)`.

        See also

        [PWM\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR](#group__pwm__interface_1ga7eeef648c3142fced48b7ab52c9c1ead)

        See also

        [PWM\_DT\_SPEC\_GET\_OR](#group__pwm__interface_1ga82f8efe8f0bc088fdda58c09dd4be4ff)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **default\_value** – Fallback value to expand to.

        Returns:
        :   Static initializer for a struct [pwm\_dt\_spec](#structpwm__dt__spec) for the property.

    Typedefs

    typedef uint16\_t pwm\_flags\_t
    :   Provides a type to hold PWM configuration flags.

        The lower 8 bits are used for standard flags. The upper 8 bits are reserved for SoC specific flags.

        See also

        [PWM\_CAPTURE\_FLAGS](#group__pwm__interface_1PWM_CAPTURE_FLAGS).

    typedef void (\*pwm\_capture\_callback\_handler\_t)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel, uint32\_t period\_cycles, uint32\_t pulse\_cycles, int status, void \*user\_data)
    :   PWM capture callback handler function signature.

        Note

        The callback handler will be called in interrupt context.

        Note

        [`CONFIG_PWM_CAPTURE`](../../kconfig.md#CONFIG_PWM_CAPTURE "CONFIG_PWM_CAPTURE") must be selected to enable PWM capture support.

        Param dev:
        :   **[in]** PWM device instance.

        Param channel:
        :   PWM channel.

        Param period\_cycles:
        :   Captured PWM period width (in clock cycles). HW specific.

        Param pulse\_cycles:
        :   Captured PWM pulse width (in clock cycles). HW specific.

        Param status:
        :   Status for the PWM capture (0 if no error, negative errno otherwise. See [pwm\_capture\_cycles()](#group__pwm__interface_1ga09767ae3c8d970675dbf9e3e50291743) return value descriptions for details).

        Param user\_data:
        :   User data passed to [pwm\_configure\_capture()](#group__pwm__interface_1ga9603146d7f9c2690c1e1983113d6c6bb)

    Functions

    int pwm\_set\_cycles(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel, uint32\_t period, uint32\_t pulse, [pwm\_flags\_t](#c.pwm_flags_t) flags)
    :   Set the period and pulse width for a single PWM output.

        The PWM period and pulse width will synchronously be set to the new values without glitches in the PWM signal, but the call will not block for the change to take effect.

        Passing 0 as `pulse` will cause the pin to be driven to a constant inactive level. Passing a non-zero `pulse` equal to `period` will cause the pin to be driven to a constant active level.

        Note

        Not all PWM controllers support synchronous, glitch-free updates of the PWM period and pulse width. Depending on the hardware, changing the PWM period and/or pulse width may cause a glitch in the generated PWM signal.

        Note

        Some multi-channel PWM controllers share the PWM period across all channels. Depending on the hardware, changing the PWM period for one channel may affect the PWM period for the other channels of the same PWM controller.

        Parameters:
        :   - **dev** – **[in]** PWM device instance.
            - **channel** – PWM channel.
            - **period** – Period (in clock cycles) set to the PWM. HW specific.
            - **pulse** – Pulse width (in clock cycles) set to the PWM. HW specific.
            - **flags** – Flags for pin configuration.

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – If pulse > period.
            - **-errno** – Negative errno code on failure.

    int pwm\_get\_cycles\_per\_sec(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel, uint64\_t \*cycles)
    :   Get the clock rate (cycles per second) for a single PWM output.

        Parameters:
        :   - **dev** – **[in]** PWM device instance.
            - **channel** – PWM channel.
            - **cycles** – **[out]** Pointer to the memory to store clock rate (cycles per sec). HW specific.

        Return values:
        :   - **0** – If successful.
            - **-errno** – Negative errno code on failure.

    static inline int pwm\_set(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel, uint32\_t period, uint32\_t pulse, [pwm\_flags\_t](#c.pwm_flags_t) flags)
    :   Set the period and pulse width in nanoseconds for a single PWM output.

        Note

        Utility macros such as [PWM\_MSEC()](#group__pwm__interface_1ga1cccc226a23866dd2dcac9467ff3af0e) can be used to convert from other scales or units to nanoseconds, the units used by this function.

        Parameters:
        :   - **dev** – **[in]** PWM device instance.
            - **channel** – PWM channel.
            - **period** – Period (in nanoseconds) set to the PWM.
            - **pulse** – Pulse width (in nanoseconds) set to the PWM.
            - **flags** – Flags for pin configuration (polarity).

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – If requested period or pulse cycles are not supported.
            - **-errno** – Other negative errno code on failure.

    static inline int pwm\_set\_dt(const struct [pwm\_dt\_spec](#c.pwm_dt_spec) \*spec, uint32\_t period, uint32\_t pulse)
    :   Set the period and pulse width in nanoseconds from a struct [pwm\_dt\_spec](#structpwm__dt__spec) (with custom period).

        This is equivalent to:

        ```text
        pwm_set(spec->dev, spec->channel, period, pulse, spec->flags)
        ```

        The period specified in `spec` is ignored. This API call can be used when the period specified in Devicetree needs to be changed at runtime.

        See also

        [pwm\_set\_pulse\_dt()](#group__pwm__interface_1ga8ff263177143d33c6d0a284b837bc4da)

        Parameters:
        :   - **spec** – **[in]** PWM specification from devicetree.
            - **period** – Period (in nanoseconds) set to the PWM.
            - **pulse** – Pulse width (in nanoseconds) set to the PWM.

        Returns:
        :   A value from [pwm\_set()](#group__pwm__interface_1gadd9049c9a56cd9419736b3514e42dc01).

    static inline int pwm\_set\_pulse\_dt(const struct [pwm\_dt\_spec](#c.pwm_dt_spec) \*spec, uint32\_t pulse)
    :   Set the period and pulse width in nanoseconds from a struct [pwm\_dt\_spec](#structpwm__dt__spec).

        This is equivalent to:

        ```text
        pwm_set(spec->dev, spec->channel, spec->period, pulse, spec->flags)
        ```

        See also

        [pwm\_set\_pulse\_dt()](#group__pwm__interface_1ga8ff263177143d33c6d0a284b837bc4da)

        Parameters:
        :   - **spec** – **[in]** PWM specification from devicetree.
            - **pulse** – Pulse width (in nanoseconds) set to the PWM.

        Returns:
        :   A value from [pwm\_set()](#group__pwm__interface_1gadd9049c9a56cd9419736b3514e42dc01).

    static inline int pwm\_cycles\_to\_usec(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel, uint32\_t cycles, uint64\_t \*usec)
    :   Convert from PWM cycles to microseconds.

        Parameters:
        :   - **dev** – **[in]** PWM device instance.
            - **channel** – PWM channel.
            - **cycles** – Cycles to be converted.
            - **usec** – **[out]** Pointer to the memory to store calculated usec.

        Return values:
        :   - **0** – If successful.
            - **-ERANGE** – If result is too large.
            - **-errno** – Other negative errno code on failure.

    static inline int pwm\_cycles\_to\_nsec(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel, uint32\_t cycles, uint64\_t \*nsec)
    :   Convert from PWM cycles to nanoseconds.

        Parameters:
        :   - **dev** – **[in]** PWM device instance.
            - **channel** – PWM channel.
            - **cycles** – Cycles to be converted.
            - **nsec** – **[out]** Pointer to the memory to store the calculated nsec.

        Return values:
        :   - **0** – If successful.
            - **-ERANGE** – If result is too large.
            - **-errno** – Other negative errno code on failure.

    static inline int pwm\_configure\_capture(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel, [pwm\_flags\_t](#c.pwm_flags_t) flags, [pwm\_capture\_callback\_handler\_t](#c.pwm_capture_callback_handler_t) cb, void \*user\_data)
    :   Configure PWM period/pulse width capture for a single PWM input.

        After configuring PWM capture using this function, the capture can be enabled/disabled using [pwm\_enable\_capture()](#group__pwm__interface_1gad14ca53862a465d1789e8936ce394f9a) and [pwm\_disable\_capture()](#group__pwm__interface_1ga1df2bb40af2fa3ce945cc9cd67edc2bf).

        Note

        This API function cannot be invoked from user space due to the use of a function callback. In user space, one of the simpler API functions ([pwm\_capture\_cycles()](#group__pwm__interface_1ga09767ae3c8d970675dbf9e3e50291743), [pwm\_capture\_usec()](#group__pwm__interface_1ga3a1552ea924eeec21477396da6d3890b), or [pwm\_capture\_nsec()](#group__pwm__interface_1ga6489095d890224d23c5ed05bc884d24a)) can be used instead.

        Note

        [`CONFIG_PWM_CAPTURE`](../../kconfig.md#CONFIG_PWM_CAPTURE "CONFIG_PWM_CAPTURE") must be selected for this function to be available.

        Parameters:
        :   - **dev** – **[in]** PWM device instance.
            - **channel** – PWM channel.
            - **flags** – PWM capture flags
            - **cb** – **[in]** Application callback handler function to be called upon capture
            - **user\_data** – **[in]** User data to pass to the application callback handler function

        Return values:
        :   - **-EINVAL** – if invalid function parameters were given
            - **-ENOSYS** – if PWM capture is not supported or the given flags are not supported
            - **-EIO** – if IO error occurred while configuring
            - **-EBUSY** – if PWM capture is already in progress

    int pwm\_enable\_capture(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel)
    :   Enable PWM period/pulse width capture for a single PWM input.

        The PWM pin must be configured using [pwm\_configure\_capture()](#group__pwm__interface_1ga9603146d7f9c2690c1e1983113d6c6bb) prior to calling this function.

        Note

        [`CONFIG_PWM_CAPTURE`](../../kconfig.md#CONFIG_PWM_CAPTURE "CONFIG_PWM_CAPTURE") must be selected for this function to be available.

        Parameters:
        :   - **dev** – **[in]** PWM device instance.
            - **channel** – PWM channel.

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – if invalid function parameters were given
            - **-ENOSYS** – if PWM capture is not supported
            - **-EIO** – if IO error occurred while enabling PWM capture
            - **-EBUSY** – if PWM capture is already in progress

    int pwm\_disable\_capture(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel)
    :   Disable PWM period/pulse width capture for a single PWM input.

        Note

        [`CONFIG_PWM_CAPTURE`](../../kconfig.md#CONFIG_PWM_CAPTURE "CONFIG_PWM_CAPTURE") must be selected for this function to be available.

        Parameters:
        :   - **dev** – **[in]** PWM device instance.
            - **channel** – PWM channel.

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – if invalid function parameters were given
            - **-ENOSYS** – if PWM capture is not supported
            - **-EIO** – if IO error occurred while disabling PWM capture

    int pwm\_capture\_cycles(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel, [pwm\_flags\_t](#c.pwm_flags_t) flags, uint32\_t \*period, uint32\_t \*pulse, [k\_timeout\_t](../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Capture a single PWM period/pulse width in clock cycles for a single PWM input.

        This API function wraps calls to [pwm\_configure\_capture()](#group__pwm__interface_1ga9603146d7f9c2690c1e1983113d6c6bb), [pwm\_enable\_capture()](#group__pwm__interface_1gad14ca53862a465d1789e8936ce394f9a), and [pwm\_disable\_capture()](#group__pwm__interface_1ga1df2bb40af2fa3ce945cc9cd67edc2bf) and passes the capture result to the caller. The function is blocking until either the PWM capture is completed or a timeout occurs.

        Note

        [`CONFIG_PWM_CAPTURE`](../../kconfig.md#CONFIG_PWM_CAPTURE "CONFIG_PWM_CAPTURE") must be selected for this function to be available.

        Parameters:
        :   - **dev** – **[in]** PWM device instance.
            - **channel** – PWM channel.
            - **flags** – PWM capture flags.
            - **period** – **[out]** Pointer to the memory to store the captured PWM period width (in clock cycles). HW specific.
            - **pulse** – **[out]** Pointer to the memory to store the captured PWM pulse width (in clock cycles). HW specific.
            - **timeout** – Waiting period for the capture to complete.

        Return values:
        :   - **0** – If successful.
            - **-EBUSY** – PWM capture already in progress.
            - **-EAGAIN** – Waiting period timed out.
            - **-EIO** – IO error while capturing.
            - **-ERANGE** – If result is too large.

    static inline int pwm\_capture\_usec(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel, [pwm\_flags\_t](#c.pwm_flags_t) flags, uint64\_t \*period, uint64\_t \*pulse, [k\_timeout\_t](../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Capture a single PWM period/pulse width in microseconds for a single PWM input.

        This API function wraps calls to [pwm\_capture\_cycles()](#group__pwm__interface_1ga09767ae3c8d970675dbf9e3e50291743) and [pwm\_cycles\_to\_usec()](#group__pwm__interface_1gae57fb205e43dde82d96abe79966539a9) and passes the capture result to the caller. The function is blocking until either the PWM capture is completed or a timeout occurs.

        Note

        [`CONFIG_PWM_CAPTURE`](../../kconfig.md#CONFIG_PWM_CAPTURE "CONFIG_PWM_CAPTURE") must be selected for this function to be available.

        Parameters:
        :   - **dev** – **[in]** PWM device instance.
            - **channel** – PWM channel.
            - **flags** – PWM capture flags.
            - **period** – **[out]** Pointer to the memory to store the captured PWM period width (in usec).
            - **pulse** – **[out]** Pointer to the memory to store the captured PWM pulse width (in usec).
            - **timeout** – Waiting period for the capture to complete.

        Return values:
        :   - **0** – If successful.
            - **-EBUSY** – PWM capture already in progress.
            - **-EAGAIN** – Waiting period timed out.
            - **-EIO** – IO error while capturing.
            - **-ERANGE** – If result is too large.
            - **-errno** – Other negative errno code on failure.

    static inline int pwm\_capture\_nsec(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t channel, [pwm\_flags\_t](#c.pwm_flags_t) flags, uint64\_t \*period, uint64\_t \*pulse, [k\_timeout\_t](../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Capture a single PWM period/pulse width in nanoseconds for a single PWM input.

        This API function wraps calls to [pwm\_capture\_cycles()](#group__pwm__interface_1ga09767ae3c8d970675dbf9e3e50291743) and [pwm\_cycles\_to\_nsec()](#group__pwm__interface_1ga6f0281398611dd876386c66a63373a2e) and passes the capture result to the caller. The function is blocking until either the PWM capture is completed or a timeout occurs.

        Note

        [`CONFIG_PWM_CAPTURE`](../../kconfig.md#CONFIG_PWM_CAPTURE "CONFIG_PWM_CAPTURE") must be selected for this function to be available.

        Parameters:
        :   - **dev** – **[in]** PWM device instance.
            - **channel** – PWM channel.
            - **flags** – PWM capture flags.
            - **period** – **[out]** Pointer to the memory to store the captured PWM period width (in nsec).
            - **pulse** – **[out]** Pointer to the memory to store the captured PWM pulse width (in nsec).
            - **timeout** – Waiting period for the capture to complete.

        Return values:
        :   - **0** – If successful.
            - **-EBUSY** – PWM capture already in progress.
            - **-EAGAIN** – Waiting period timed out.
            - **-EIO** – IO error while capturing.
            - **-ERANGE** – If result is too large.
            - **-errno** – Other negative errno code on failure.

    static inline bool pwm\_is\_ready\_dt(const struct [pwm\_dt\_spec](#c.pwm_dt_spec) \*spec)
    :   Validate that the PWM device is ready.

        Parameters:
        :   - **spec** – PWM specification from devicetree

        Return values:
        :   - **true** – If the PWM device is ready for use
            - **false** – If the PWM device is not ready for use

    struct pwm\_dt\_spec
    :   *#include <pwm.h>*

        Container for PWM information specified in devicetree.

        This type contains a pointer to a PWM device, channel number (controlled by the PWM device), the PWM signal period in nanoseconds and the flags applicable to the channel. Note that not all PWM drivers support flags. In such case, flags will be set to 0.

        See also

        [PWM\_DT\_SPEC\_GET\_BY\_NAME](#group__pwm__interface_1ga88b92c580860441c83d1b03db25fc4f1)

        See also

        [PWM\_DT\_SPEC\_GET\_BY\_NAME\_OR](#group__pwm__interface_1ga5557add2123a7138b64997cd070e0ee6)

        See also

        [PWM\_DT\_SPEC\_GET\_BY\_IDX](#group__pwm__interface_1ga7e8375bcf95ae6a9500ce3aba4586de4)

        See also

        [PWM\_DT\_SPEC\_GET\_BY\_IDX\_OR](#group__pwm__interface_1gaf5808fd88b101208681820b53bca33e1)

        See also

        [PWM\_DT\_SPEC\_GET](#group__pwm__interface_1ga59a79f0b77c5b71252bde126f333a84b)

        See also

        [PWM\_DT\_SPEC\_GET\_OR](#group__pwm__interface_1ga82f8efe8f0bc088fdda58c09dd4be4ff)

        Public Members

        const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev
        :   PWM device instance.

        uint32\_t channel
        :   Channel number.

        uint32\_t period
        :   Period in nanoseconds.

        [pwm\_flags\_t](#c.pwm_flags_t) flags
        :   Flags.
