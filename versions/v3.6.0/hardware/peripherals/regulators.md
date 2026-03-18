---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/hardware/peripherals/regulators.html
original_path: hardware/peripherals/regulators.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Regulators

This subsystem provides control of voltage and current regulators. A common
example is a GPIO that controls a transistor that supplies current to a device
that is not always needed. Another example is a PMIC, typically a much more
complex device.

The `*-supply` devicetree properties are used to identify the regulator(s)
that a devicetree node directly depends on. Within the driver for the node the
regulator API is used to issue requests for power when the device is to be
active, and release the power request when the device shuts down.

The simplest case where a regulator is needed is one where there is only one
client. For those situations the cost of using the regulator device
infrastructure is not justified, and `*-gpios` devicetree properties should be
used. There is no device interface to these regulators as they are entirely
controlled within the driver for the corresponding node, e.g. a sensor.

## API Reference

*group* regulator\_interface
:   Regulator Interface.

    Regulator error flags.

    REGULATOR\_ERROR\_OVER\_VOLTAGE
    :   Voltage is too high.

    REGULATOR\_ERROR\_OVER\_CURRENT
    :   Current is too high.

    REGULATOR\_ERROR\_OVER\_TEMP
    :   Temperature is too high.

    Typedefs

    typedef uint8\_t regulator\_dvs\_state\_t
    :   Opaque type to store regulator DVS states.

    typedef uint8\_t regulator\_mode\_t
    :   Opaque type to store regulator modes.

    typedef uint8\_t regulator\_error\_flags\_t
    :   Opaque bit map for regulator error flags (see [REGULATOR\_ERRORS](#group__regulator__interface_1REGULATOR_ERRORS)).

    Functions

    int regulator\_enable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Enable a regulator.

        Reference-counted request that a regulator be turned on. A regulator is considered “on” when it has reached a stable/usable state. Regulators that are always on, or configured in devicetree with `regulator-always-on` will always stay enabled, and so this function will always succeed.

        Parameters:
        :   - **dev** – Regulator device instance

        Return values:
        :   - **0** – If regulator has been successfully enabled.
            - **-errno** – Negative errno in case of failure.
            - **-ENOTSUP** – If regulator enablement can not be controlled.

    bool regulator\_is\_enabled(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Check if a regulator is enabled.

        Parameters:
        :   - **dev** – Regulator device instance.

        Return values:
        :   - **true** – If regulator is enabled.
            - **false** – If regulator is disabled.

    int regulator\_disable(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Disable a regulator.

        Release a regulator after a previous [regulator\_enable()](#group__regulator__interface_1ga06e3109b9607521fe07686c6d601e460) completed successfully. Regulators that are always on, or configured in devicetree with `regulator-always-on` will always stay enabled, and so this function will always succeed.

        This must be invoked at most once for each successful [regulator\_enable()](#group__regulator__interface_1ga06e3109b9607521fe07686c6d601e460).

        Parameters:
        :   - **dev** – Regulator device instance.

        Return values:
        :   - **0** – If regulator has been successfully disabled.
            - **-errno** – Negative errno in case of failure.
            - **-ENOTSUP** – If regulator disablement can not be controlled.

    static inline unsigned int regulator\_count\_voltages(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Obtain the number of supported voltage levels.

        Each voltage level supported by a regulator gets an index, starting from zero. The total number of supported voltage levels can be used together with [regulator\_list\_voltage()](#group__regulator__interface_1ga62d9ea1d7dc2987101cf31b324ca7c51) to list all supported voltage levels.

        Parameters:
        :   - **dev** – Regulator device instance.

        Returns:
        :   Number of supported voltages.

    static inline int regulator\_list\_voltage(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, unsigned int idx, int32\_t \*volt\_uv)
    :   Obtain the value of a voltage given an index.

        Each voltage level supported by a regulator gets an index, starting from zero. Together with [regulator\_count\_voltages()](#group__regulator__interface_1ga96bf136ff2deca774931ca27300b03a6), this function can be used to iterate over all supported voltages.

        Parameters:
        :   - **dev** – Regulator device instance.
            - **idx** – Voltage index.
            - **volt\_uv** – **[out]** Where voltage for the given `index` will be stored, in microvolts.

        Return values:
        :   - **0** – If `index` corresponds to a supported voltage.
            - **-EINVAL** – If `index` does not correspond to a supported voltage.

    bool regulator\_is\_supported\_voltage(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int32\_t min\_uv, int32\_t max\_uv)
    :   Check if a voltage within a window is supported.

        Parameters:
        :   - **dev** – Regulator device instance.
            - **min\_uv** – Minimum voltage in microvolts.
            - **max\_uv** – maximum voltage in microvolts.

        Return values:
        :   - **true** – If voltage is supported.
            - **false** – If voltage is not supported.

    int regulator\_set\_voltage(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int32\_t min\_uv, int32\_t max\_uv)
    :   Set the output voltage.

        The output voltage will be configured to the closest supported output voltage. [regulator\_get\_voltage()](#group__regulator__interface_1gaa0114ee43a137ee98f98f5bce93d8579) can be used to obtain the actual configured voltage. The voltage will be applied to the active or selected mode. Output voltage may be limited using `regulator-min-microvolt` and/or `regulator-max-microvolt` in devicetree.

        Parameters:
        :   - **dev** – Regulator device instance.
            - **min\_uv** – Minimum acceptable voltage in microvolts.
            - **max\_uv** – Maximum acceptable voltage in microvolts.

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – If the given voltage window is not valid.
            - **-ENOSYS** – If function is not implemented.
            - **-errno** – In case of any other error.

    static inline int regulator\_get\_voltage(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int32\_t \*volt\_uv)
    :   Obtain output voltage.

        Parameters:
        :   - **dev** – Regulator device instance.
            - **volt\_uv** – **[out]** Where configured output voltage will be stored.

        Return values:
        :   - **0** – If successful
            - **-ENOSYS** – If function is not implemented.
            - **-errno** – In case of any other error.

    static inline unsigned int regulator\_count\_current\_limits(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Obtain the number of supported current limit levels.

        Each current limit level supported by a regulator gets an index, starting from zero. The total number of supported current limit levels can be used together with [regulator\_list\_current\_limit()](#group__regulator__interface_1gaf12002954c6fc0ab9689f4dd2ec39518) to list all supported current limit levels.

        Parameters:
        :   - **dev** – Regulator device instance.

        Returns:
        :   Number of supported current limits.

    static inline int regulator\_list\_current\_limit(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, unsigned int idx, int32\_t \*current\_ua)
    :   Obtain the value of a current limit given an index.

        Each current limit level supported by a regulator gets an index, starting from zero. Together with [regulator\_count\_current\_limits()](#group__regulator__interface_1ga27de51302b5222f860457c5b8bd494d6), this function can be used to iterate over all supported current limits.

        Parameters:
        :   - **dev** – Regulator device instance.
            - **idx** – Current index.
            - **current\_ua** – **[out]** Where current for the given `index` will be stored, in microamps.

        Return values:
        :   - **0** – If `index` corresponds to a supported current limit.
            - **-EINVAL** – If `index` does not correspond to a supported current limit.

    int regulator\_set\_current\_limit(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int32\_t min\_ua, int32\_t max\_ua)
    :   Set output current limit.

        The output current limit will be configured to the closest supported output current limit. [regulator\_get\_current\_limit()](#group__regulator__interface_1ga88c3ddeed962b5368713ad8fef0e7d7a) can be used to obtain the actual configured current limit. Current may be limited using `current-min-microamp` and/or `current-max-microamp` in Devicetree.

        Parameters:
        :   - **dev** – Regulator device instance.
            - **min\_ua** – Minimum acceptable current limit in microamps.
            - **max\_ua** – Maximum acceptable current limit in microamps.

        Return values:
        :   - **0** – If successful.
            - **-EINVAL** – If the given current limit window is not valid.
            - **-ENOSYS** – If function is not implemented.
            - **-errno** – In case of any other error.

    static inline int regulator\_get\_current\_limit(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int32\_t \*curr\_ua)
    :   Get output current limit.

        Parameters:
        :   - **dev** – Regulator device instance.
            - **curr\_ua** – **[out]** Where output current limit will be stored.

        Return values:
        :   - **0** – If successful.
            - **-ENOSYS** – If function is not implemented.
            - **-errno** – In case of any other error.

    int regulator\_set\_mode(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [regulator\_mode\_t](#c.regulator_mode_t) mode)
    :   Set mode.

        Regulators can support multiple modes in order to permit different voltage configuration or better power savings. This API will apply a mode for the regulator. Allowed modes may be limited using `regulator-allowed-modes` devicetree property.

        Parameters:
        :   - **dev** – Regulator device instance.
            - **mode** – Mode to select for this regulator.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – If mode is not supported.
            - **-ENOSYS** – If function is not implemented.
            - **-errno** – In case of any other error.

    static inline int regulator\_get\_mode(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [regulator\_mode\_t](#c.regulator_mode_t) \*mode)
    :   Get mode.

        Parameters:
        :   - **dev** – Regulator device instance.
            - **mode** – **[out]** Where mode will be stored.

        Return values:
        :   - **0** – If successful.
            - **-ENOSYS** – If function is not implemented.
            - **-errno** – In case of any other error.

    static inline int regulator\_set\_active\_discharge(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool active\_discharge)
    :   Set active discharge setting.

        Parameters:
        :   - **dev** – Regulator device instance.
            - **active\_discharge** – Active discharge enable or disable.

        Return values:
        :   - **0** – If successful.
            - **-ENOSYS** – If function is not implemented.
            - **-errno** – In case of any other error.

    static inline int regulator\_get\_active\_discharge(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool \*active\_discharge)
    :   Get active discharge setting.

        Parameters:
        :   - **dev** – Regulator device instance.
            - **active\_discharge** – **[out]** Where active discharge will be stored.

        Return values:
        :   - **0** – If successful.
            - **-ENOSYS** – If function is not implemented.
            - **-errno** – In case of any other error.

    static inline int regulator\_get\_error\_flags(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, [regulator\_error\_flags\_t](#c.regulator_error_flags_t) \*flags)
    :   Get active error flags.

        Parameters:
        :   - **dev** – Regulator device instance.
            - **flags** – Where error flags will be stored.

        Return values:
        :   - **0** – If successful.
            - **-ENOSYS** – If function is not implemented.
            - **-errno** – In case of any other error.
