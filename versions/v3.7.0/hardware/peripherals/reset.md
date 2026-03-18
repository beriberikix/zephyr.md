---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/reset.html
original_path: hardware/peripherals/reset.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Reset Controller

## Overview

Reset controllers are units that control the reset signals to multiple
peripherals. The reset controller API allows peripheral drivers to request
control over their reset input signals, including the ability to assert,
deassert and toggle those signals. Also, the reset status of the reset input
signal can be checked.

Mainly, the line\_assert and line\_deassert API functions are optional because
in most cases we want to toggle the reset signals.

## Configuration Options

Related configuration options:

- [`CONFIG_RESET`](../../kconfig.md#CONFIG_RESET "CONFIG_RESET")

## API Reference

*group* Reset Controller Interface
:   Reset Controller Interface.

    **Since**
    :   3.1

    **Version**
    :   0.2.0

    Defines

    RESET\_DT\_SPEC\_GET\_BY\_IDX(node\_id, idx)
    :   Static initializer for a `[reset_dt_spec](#structreset__dt__spec)`.

        This returns a static initializer for a `[reset_dt_spec](#structreset__dt__spec)` structure given a devicetree node identifier, a property specifying a Reset Controller and an index.

        Example devicetree fragment:

        ```text
         n: node {
            resets = <&reset 10>;
         }
        ```

        Example usage:

        ```text
         const struct reset_dt_spec spec = RESET_DT_SPEC_GET_BY_IDX(DT_NODELABEL(n), 0);
         // Initializes 'spec' to:
         // {
         //         .dev = DEVICE_DT_GET(DT_NODELABEL(reset)),
         //         .id = 10
         // }
        ```

        The ‘reset’ field must still be checked for readiness, e.g. using [device\_is\_ready()](../../kernel/drivers/index.md#group__device__model_1gaa4944bd850e90cbd52b0489f9b12edfb). It is an error to use this macro unless the node exists, has the given property, and that property specifies a reset controller reset line id as shown above.

        Parameters:
        :   - **node\_id** – devicetree node identifier
            - **idx** – logical index into “resets”

        Returns:
        :   static initializer for a struct [reset\_dt\_spec](#structreset__dt__spec) for the property

    RESET\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, idx, default\_value)
    :   Like [RESET\_DT\_SPEC\_GET\_BY\_IDX()](#group__reset__controller__interface_1ga9f2e9e2e14a6ec9d2848979c77ecad9b), with a fallback to a default value.

        If the devicetree node identifier ‘node\_id’ refers to a node with a ‘resets’ property, this expands to `[RESET_DT_SPEC_GET_BY_IDX(node_id, idx)](#group__reset__controller__interface_1ga9f2e9e2e14a6ec9d2848979c77ecad9b)`. The `default_value` parameter is not expanded in this case.

        Otherwise, this expands to `default_value`.

        Parameters:
        :   - **node\_id** – devicetree node identifier
            - **idx** – logical index into the ‘resets’ property
            - **default\_value** – fallback value to expand to

        Returns:
        :   static initializer for a struct [reset\_dt\_spec](#structreset__dt__spec) for the property, or default\_value if the node or property do not exist

    RESET\_DT\_SPEC\_GET(node\_id)
    :   Equivalent to [RESET\_DT\_SPEC\_GET\_BY\_IDX(node\_id, 0)](#group__reset__controller__interface_1ga9f2e9e2e14a6ec9d2848979c77ecad9b).

        See also

        [RESET\_DT\_SPEC\_GET\_BY\_IDX()](#group__reset__controller__interface_1ga9f2e9e2e14a6ec9d2848979c77ecad9b)

        Parameters:
        :   - **node\_id** – devicetree node identifier

        Returns:
        :   static initializer for a struct [reset\_dt\_spec](#structreset__dt__spec) for the property

    RESET\_DT\_SPEC\_GET\_OR(node\_id, default\_value)
    :   Equivalent to [RESET\_DT\_SPEC\_GET\_BY\_IDX\_OR(node\_id, 0, default\_value)](#group__reset__controller__interface_1ga594221ce06a743b591ef285856981793).

        Parameters:
        :   - **node\_id** – devicetree node identifier
            - **default\_value** – fallback value to expand to

        Returns:
        :   static initializer for a struct [reset\_dt\_spec](#structreset__dt__spec) for the property, or default\_value if the node or property do not exist

    RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, idx)
    :   Static initializer for a `[reset_dt_spec](#structreset__dt__spec)` from a DT\_DRV\_COMPAT instance’s Reset Controller property at an index.

        See also

        [RESET\_DT\_SPEC\_GET\_BY\_IDX()](#group__reset__controller__interface_1ga9f2e9e2e14a6ec9d2848979c77ecad9b)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **idx** – logical index into “resets”

        Returns:
        :   static initializer for a struct [reset\_dt\_spec](#structreset__dt__spec) for the property

    RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(inst, idx, default\_value)
    :   Static initializer for a `[reset_dt_spec](#structreset__dt__spec)` from a DT\_DRV\_COMPAT instance’s ‘resets’ property at an index, with fallback.

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **idx** – logical index into the ‘resets’ property
            - **default\_value** – fallback value to expand to

        Returns:
        :   static initializer for a struct [reset\_dt\_spec](#structreset__dt__spec) for the property, or default\_value if the node or property do not exist

    RESET\_DT\_SPEC\_INST\_GET(inst)
    :   Equivalent to [RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX(inst, 0)](#group__reset__controller__interface_1ga539688cb73d17aa02b137fc90965350b).

        See also

        [RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX()](#group__reset__controller__interface_1ga539688cb73d17aa02b137fc90965350b)

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number

        Returns:
        :   static initializer for a struct [reset\_dt\_spec](#structreset__dt__spec) for the property

    RESET\_DT\_SPEC\_INST\_GET\_OR(inst, default\_value)
    :   Equivalent to [RESET\_DT\_SPEC\_INST\_GET\_BY\_IDX\_OR(node\_id, 0, default\_value)](#group__reset__controller__interface_1ga7d14fdead7518b4070ec7123130311b2).

        Parameters:
        :   - **inst** – DT\_DRV\_COMPAT instance number
            - **default\_value** – fallback value to expand to

        Returns:
        :   static initializer for a struct [reset\_dt\_spec](#structreset__dt__spec) for the property, or default\_value if the node or property do not exist

    Functions

    int reset\_status(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t id, uint8\_t \*status)
    :   Get the reset status.

        This function returns the reset status of the device.

        Parameters:
        :   - **dev** – Reset controller device.
            - **id** – Reset line.
            - **status** – Where to write the reset status.

        Return values:
        :   - **0** – On success.
            - **-ENOSYS** – If the functionality is not implemented by the driver.
            - **-errno** – Other negative errno in case of failure.

    static inline int reset\_status\_dt(const struct [reset\_dt\_spec](#c.reset_dt_spec) \*spec, uint8\_t \*status)
    :   Get the reset status from a `[reset_dt_spec](#structreset__dt__spec)`.

        This is equivalent to:

        reset\_status(spec->dev, spec->id, status);

        Parameters:
        :   - **spec** – Reset controller specification from devicetree
            - **status** – Where to write the reset status.

        Returns:
        :   a value from [reset\_status()](#group__reset__controller__interface_1gad58d0bfcf0b9cd4ba11b163e97ba8762)

    int reset\_line\_assert(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t id)
    :   Put the device in reset state.

        This function sets/clears the reset bits of the device, depending on the logic level (active-high/active-low).

        Parameters:
        :   - **dev** – Reset controller device.
            - **id** – Reset line.

        Return values:
        :   - **0** – On success.
            - **-ENOSYS** – If the functionality is not implemented by the driver.
            - **-errno** – Other negative errno in case of failure.

    static inline int reset\_line\_assert\_dt(const struct [reset\_dt\_spec](#c.reset_dt_spec) \*spec)
    :   Assert the reset state from a `[reset_dt_spec](#structreset__dt__spec)`.

        This is equivalent to:

        ```text
        reset_line_assert(spec->dev, spec->id);
        ```

        Parameters:
        :   - **spec** – Reset controller specification from devicetree

        Returns:
        :   a value from [reset\_line\_assert()](#group__reset__controller__interface_1gab7b58d253be9083b4ed7c35bc60c6aa6)

    int reset\_line\_deassert(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t id)
    :   Take out the device from reset state.

        This function sets/clears the reset bits of the device, depending on the logic level (active-low/active-high).

        Parameters:
        :   - **dev** – Reset controller device.
            - **id** – Reset line.

        Return values:
        :   - **0** – On success.
            - **-ENOSYS** – If the functionality is not implemented by the driver.
            - **-errno** – Other negative errno in case of failure.

    static inline int reset\_line\_deassert\_dt(const struct [reset\_dt\_spec](#c.reset_dt_spec) \*spec)
    :   Deassert the reset state from a `[reset_dt_spec](#structreset__dt__spec)`.

        This is equivalent to:

        ```text
        reset_line_deassert(spec->dev, spec->id)
        ```

        Parameters:
        :   - **spec** – Reset controller specification from devicetree

        Returns:
        :   a value from [reset\_line\_deassert()](#group__reset__controller__interface_1gaadd2d70e57e620e9f12900c561fea941)

    int reset\_line\_toggle(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint32\_t id)
    :   Reset the device.

        This function performs reset for a device (assert + deassert).

        Parameters:
        :   - **dev** – Reset controller device.
            - **id** – Reset line.

        Return values:
        :   - **0** – On success.
            - **-ENOSYS** – If the functionality is not implemented by the driver.
            - **-errno** – Other negative errno in case of failure.

    static inline int reset\_line\_toggle\_dt(const struct [reset\_dt\_spec](#c.reset_dt_spec) \*spec)
    :   Reset the device from a `[reset_dt_spec](#structreset__dt__spec)`.

        This is equivalent to:

        ```text
        reset_line_toggle(spec->dev, spec->id)
        ```

        Parameters:
        :   - **spec** – Reset controller specification from devicetree

        Returns:
        :   a value from [reset\_line\_toggle()](#group__reset__controller__interface_1ga29fb7d474e46d7a5a69ab8fb87ddbc5e)

    struct reset\_dt\_spec
    :   *#include <reset.h>*

        Reset controller device configuration.

        Public Members

        const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev
        :   Reset controller device.

        uint32\_t id
        :   Reset line.
