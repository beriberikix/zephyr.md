---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/input/gpio-kbd.html
original_path: services/input/gpio-kbd.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# GPIO Keyboard Matrix

The [`gpio-kbd-matrix`](../../build/dts/api/bindings/input/gpio-kbd-matrix.md#std-dtcompatible-gpio-kbd-matrix) driver supports a large variety of keyboard
matrix hardware configurations and has numerous options to change its behavior.
This is an overview of some common setups and how they can be supported by the
driver.

The conventional configuration for all of these is that the driver reads on the
row GPIOs (inputs) and selects on the columns GPIOs (output).

## Base use case, no isolation diodes, interrupt capable GPIOs

This is the common configuration found on consumer keyboards with membrane
switches and flexible circuit boards, no isolation diodes, requires ghosting
detection (which is enabled by default).

[![../../_images/no-diodes.svg](../../_images/no-diodes.svg)](../../_images/no-diodes.svg)

A 3x3 matrix, no diodes

The system must support GPIO interrupts, and the interrupt can be enabled on all
row GPIOs at the same time.

```devicetree
kbd-matrix {
     compatible = "gpio-kbd-matrix";
     row-gpios = <&gpio0 0 (GPIO_PULL_UP | GPIO_ACTIVE_LOW)>,
                 <&gpio0 1 (GPIO_PULL_UP | GPIO_ACTIVE_LOW)>,
                 <&gpio0 2 (GPIO_PULL_UP | GPIO_ACTIVE_LOW)>;
     col-gpios = <&gpio0 3 GPIO_ACTIVE_LOW>,
                 <&gpio0 4 GPIO_ACTIVE_LOW>,
                 <&gpio0 5 GPIO_ACTIVE_LOW>;
};
```

In this configuration the matrix scanning library enters idle mode once all
keys are released, and the keyboard matrix thread only wakes up when a key has
been pressed.

GPIOs for columns that are not currently selected are configured in high
impedance mode. This means that the row state may need some time to settle to
avoid misreading the key state from a column to the following one. The settle
time can be tweaked by changing the `settle-time-us` property.

## Isolation diodes

If the matrix has isolation diodes for every key, then it’s possible to:

> - disable ghosting detection, allowing any key combination to be detected
> - configuring the driver to drive unselected columns GPIO to inactive state
>   rather than high impedance, this allows to reduce the settle time
>   (potentially down to 0), and use the more efficient port wide GPIO read APIs
>   (happens automatically if the GPIO pins are sequential)

Matrixes with diodes going from rows to columns must use pull-ups on rows and
active low columns.

[![../../_images/diodes-rc.svg](../../_images/diodes-rc.svg)](../../_images/diodes-rc.svg)

A 3x3 matrix with row to column isolation diodes.

```devicetree
kbd-matrix {
     compatible = "gpio-kbd-matrix";
     row-gpios = <&gpio0 0 (GPIO_PULL_UP | GPIO_ACTIVE_LOW)>,
                 <&gpio0 1 (GPIO_PULL_UP | GPIO_ACTIVE_LOW)>,
                 <&gpio0 2 (GPIO_PULL_UP | GPIO_ACTIVE_LOW)>;
     col-gpios = <&gpio0 3 GPIO_ACTIVE_LOW>,
                 <&gpio0 4 GPIO_ACTIVE_LOW>,
                 <&gpio0 5 GPIO_ACTIVE_LOW>;
     col-drive-inactive;
     settle-time-us = <0>;
     no-ghostkey-check;
};
```

Matrixes with diodes going from columns to rows must use pull-downs on rows and
active high columns.

[![../../_images/diodes-cr.svg](../../_images/diodes-cr.svg)](../../_images/diodes-cr.svg)

A 3x3 matrix with column to row isolation diodes.

```devicetree
kbd-matrix {
     compatible = "gpio-kbd-matrix";
     row-gpios = <&gpio0 0 (GPIO_PULL_DOWN | GPIO_ACTIVE_HIGH)>,
                 <&gpio0 1 (GPIO_PULL_DOWN | GPIO_ACTIVE_HIGH)>,
                 <&gpio0 2 (GPIO_PULL_DOWN | GPIO_ACTIVE_HIGH)>;
     col-gpios = <&gpio0 3 GPIO_ACTIVE_HIGH>,
                 <&gpio0 4 GPIO_ACTIVE_HIGH>,
                 <&gpio0 5 GPIO_ACTIVE_HIGH>;
     col-drive-inactive;
     settle-time-us = <0>;
     no-ghostkey-check;
};
```

## GPIO with no interrupt support

Some GPIO controllers have limitations on GPIO interrupts, and may not support
enabling interrupts on all row GPIOs at the same time.

In this case, the driver can be configured to not use interrupt at all, and
instead idle by selecting all columns and keep polling on the row GPIOs, which
is a single GPIO API operation if the pins are sequential.

This configuration can be enabled by setting the `idle-mode` property to
`poll`:

```devicetree
kbd-matrix {
     compatible = "gpio-kbd-matrix";
     ...
     idle-mode = "poll";
};
```

## GPIO multiplexer

In more extreme cases, such as if the columns are using a multiplexer and it’s
impossible to select all of them at the same time, the driver can be configured
to scan continuously.

This can be done by setting `idle-mode` to `scan` and `poll-timeout-ms`
to `0`.

```devicetree
kbd-matrix {
     compatible = "gpio-kbd-matrix";
     ...
     poll-timeout-ms = <0>;
     idle-mode = "scan";
};
```

## Row and column GPIO selection

If the row GPIOs are sequential and on the same gpio controller, the driver
automatically switches API to read from the whole GPIO port rather than the
individual pins. This is particularly useful if the GPIOs are not memory
mapped, for example on an I2C or SPI port expander, as this significantly
reduces the number of transactions on the corresponding bus.

The same is true for column GPIOs, but only if the matrix is configured for
`col-drive-inactive`, so that is only usable for matrixes with isolation
diodes.

## 16-bit row support

The driver uses an 8-bit datatype to store the row state by default, which
limits the matrix row size to 8. This can be increased to 16 by enabling the
[`CONFIG_INPUT_KBD_MATRIX_16_BIT_ROW`](../../kconfig.md#CONFIG_INPUT_KBD_MATRIX_16_BIT_ROW "CONFIG_INPUT_KBD_MATRIX_16_BIT_ROW") option.

## Actual key mask configuration

If the key matrix is not complete, a map of the keys that are actually
populated can be specified using the actual-key-mask property. This allows
the matrix state to be filtered to remove keys that are not present before
ghosting detection, potentially allowing key combinations that would otherwise
be blocked by it.

For example for a 3x3 matrix missing a key:

[![../../_images/no-sw4.svg](../../_images/no-sw4.svg)](../../_images/no-sw4.svg)

A 3x3 matrix missing a key.

```devicetree
kbd-matrix {
     compatible = "gpio-kbd-matrix";
     ...
     actual-key-mask = <0x07 0x05 0x07>;
};
```

This would allow, for example, to detect pressing `Sw1`, `SW2` and `SW4`
at the same time without triggering anti ghosting.

The actual key mask can be changed at runtime by enabling
[`CONFIG_INPUT_KBD_ACTUAL_KEY_MASK_DYNAMIC`](../../kconfig.md#CONFIG_INPUT_KBD_ACTUAL_KEY_MASK_DYNAMIC "CONFIG_INPUT_KBD_ACTUAL_KEY_MASK_DYNAMIC") and the using the
[`input_kbd_matrix_actual_key_mask_set()`](#c.input_kbd_matrix_actual_key_mask_set) API.

## Keymap configuration

Keyboard matrix devices report a series of x/y/touch events. These can be
mapped to normal key events using the [`input-keymap`](../../build/dts/api/bindings/input/input-keymap.md#std-dtcompatible-input-keymap) driver.

For example, the following would setup a `keymap` device that take the
x/y/touch events as an input and generate corresponding key events as an
output:

```devicetree
kbd {
    ...
    keymap {
        compatible = "input-keymap";
        keymap = <
            MATRIX_KEY(0, 0, INPUT_KEY_1)
            MATRIX_KEY(0, 1, INPUT_KEY_2)
            MATRIX_KEY(0, 2, INPUT_KEY_3)
            MATRIX_KEY(1, 0, INPUT_KEY_4)
            MATRIX_KEY(1, 1, INPUT_KEY_5)
            MATRIX_KEY(1, 2, INPUT_KEY_6)
            MATRIX_KEY(2, 0, INPUT_KEY_7)
            MATRIX_KEY(2, 1, INPUT_KEY_8)
            MATRIX_KEY(2, 2, INPUT_KEY_9)
        >;
        row-size = <3>;
        col-size = <3>;
    };
};
```

## Keyboard matrix shell commands

The shell command `kbd_matrix_state_dump` can be used to test the
functionality of any keyboard matrix driver implemented using the keyboard
matrix library. Once enabled it logs the state of the matrix every time it
changes, and once disabled it prints an or-mask of any key that has been
detected, which can be used to set the `actual-key-mask` property.

The command can be enabled using the
[`CONFIG_INPUT_SHELL_KBD_MATRIX_STATE`](../../kconfig.md#CONFIG_INPUT_SHELL_KBD_MATRIX_STATE "CONFIG_INPUT_SHELL_KBD_MATRIX_STATE").

Example usage:

```shell
uart:~$ device list
devices:
- kbd-matrix (READY)
uart:~$ input kbd_matrix_state_dump kbd-matrix
Keyboard state logging enabled for kbd-matrix
[00:01:41.678,466] <inf> input: kbd-matrix state [01 -- -- --] (1)
[00:01:41.784,912] <inf> input: kbd-matrix state [-- -- -- --] (0)
...
press more buttons
...
uart:~$ input kbd_matrix_state_dump off
Keyboard state logging disabled
[00:01:47.967,651] <inf> input: kbd-matrix key-mask [07 05 07 --] (8)
```

## Keyboard matrix library

The GPIO keyboard matrix driver is based on a generic keyboard matrix library,
which implements the core functionalities such as scanning delays, debouncing,
idle mode etc. This can be reused to implement other keyboard matrix drivers,
potentially application specific.

*group* input\_kbd\_matrix
:   Keyboard Matrix API.

    Defines

    INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_NONE
    :   Special drive\_column argument for not driving any column.

    INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_ALL
    :   Special drive\_column argument for driving all the columns.

    INPUT\_KBD\_MATRIX\_SCAN\_OCURRENCES
    :   Number of tracked scan cycles.

    PRIkbdrow

    INPUT\_KBD\_ACTUAL\_KEY\_MASK\_CONST

    INPUT\_KBD\_MATRIX\_ROW\_BITS
    :   Maximum number of rows.

    INPUT\_KBD\_MATRIX\_DATA\_NAME(node\_id, name)

    INPUT\_KBD\_MATRIX\_DT\_DEFINE\_ROW\_COL(node\_id, \_row\_size, \_col\_size)
    :   Defines the common keyboard matrix support data from devicetree, specify row and col count.

    INPUT\_KBD\_MATRIX\_DT\_DEFINE(node\_id)
    :   Defines the common keyboard matrix support data from devicetree.

    INPUT\_KBD\_MATRIX\_DT\_INST\_DEFINE\_ROW\_COL(inst, row\_size, col\_size)
    :   Defines the common keyboard matrix support data from devicetree instance, specify row and col count.

        Parameters:
        :   - **inst** – Instance.
            - **row\_size** – The matrix row count.
            - **col\_size** – The matrix column count.

    INPUT\_KBD\_MATRIX\_DT\_INST\_DEFINE(inst)
    :   Defines the common keyboard matrix support data from devicetree instance.

        Parameters:
        :   - **inst** – Instance.

    INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT\_ROW\_COL(node\_id, \_api, \_row\_size, \_col\_size)
    :   Initialize common keyboard matrix config from devicetree, specify row and col count.

        Parameters:
        :   - **node\_id** – The devicetree node identifier.
            - **\_api** – Pointer to a [input\_kbd\_matrix\_api](#structinput__kbd__matrix__api) structure.
            - **\_row\_size** – The matrix row count.
            - **\_col\_size** – The matrix column count.

    INPUT\_KBD\_MATRIX\_DT\_COMMON\_CONFIG\_INIT(node\_id, api)
    :   Initialize common keyboard matrix config from devicetree.

        Parameters:
        :   - **node\_id** – The devicetree node identifier.
            - **api** – Pointer to a [input\_kbd\_matrix\_api](#structinput__kbd__matrix__api) structure.

    INPUT\_KBD\_MATRIX\_DT\_INST\_COMMON\_CONFIG\_INIT\_ROW\_COL(inst, api, row\_size, col\_size)
    :   Initialize common keyboard matrix config from devicetree instance, specify row and col count.

        Parameters:
        :   - **inst** – Instance.
            - **api** – Pointer to a [input\_kbd\_matrix\_api](#structinput__kbd__matrix__api) structure.
            - **row\_size** – The matrix row count.
            - **col\_size** – The matrix column count.

    INPUT\_KBD\_MATRIX\_DT\_INST\_COMMON\_CONFIG\_INIT(inst, api)
    :   Initialize common keyboard matrix config from devicetree instance.

        Parameters:
        :   - **inst** – Instance.
            - **api** – Pointer to a [input\_kbd\_matrix\_api](#structinput__kbd__matrix__api) structure.

    INPUT\_KBD\_STRUCT\_CHECK(config, data)
    :   Validate the offset of the common data structures.

        Parameters:
        :   - **config** – Name of the config structure.
            - **data** – Name of the data structure.

    Typedefs

    typedef uint8\_t kbd\_row\_t
    :   Row entry data type.

    Functions

    int input\_kbd\_matrix\_actual\_key\_mask\_set(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t row, uint8\_t col, bool enabled)
    :   Enables or disables a specific row, column combination in the actual key mask.

        This allows enabling or disabling spcific row, column combination in the actual key mask in runtime. It can be useful if some of the keys are not present in some configuration, and the specific configuration is determined in runtime. Requires  [`CONFIG_INPUT_KBD_ACTUAL_KEY_MASK_DYNAMIC`](../../kconfig.md#CONFIG_INPUT_KBD_ACTUAL_KEY_MASK_DYNAMIC "CONFIG_INPUT_KBD_ACTUAL_KEY_MASK_DYNAMIC") to be enabled.

        Parameters:
        :   - **dev** – Pointer to the keyboard matrix device.
            - **row** – The matrix row to enable or disable.
            - **col** – The matrix column to enable or disable.
            - **enabled** – Whether the specificied row, col has to be enabled or disabled.

        Return values:
        :   - **0** – If the change is successful.
            - **-errno** – Negative errno if row or col are out of range for the device.

    void input\_kbd\_matrix\_poll\_start(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Start scanning the keyboard matrix.

        Starts the keyboard matrix scanning cycle, this should be called in reaction of a press event, after the device has been put in detect mode.

        Parameters:
        :   - **dev** – Keyboard matrix device instance.

    void input\_kbd\_matrix\_drive\_column\_hook(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int col)
    :   Drive column hook.

        This can be implemented by the application to handle column selection quirks. Called after the driver specific drive\_column function. Requires  [`CONFIG_INPUT_KBD_DRIVE_COLUMN_HOOK`](../../kconfig.md#CONFIG_INPUT_KBD_DRIVE_COLUMN_HOOK "CONFIG_INPUT_KBD_DRIVE_COLUMN_HOOK") to be enabled.

        Parameters:
        :   - **dev** – Keyboard matrix device instance.
            - **col** – The column to drive, or [INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_NONE](#group__input__kbd__matrix_1ga2f35f23d426f93f71057a31f612a88de) or [INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_ALL](#group__input__kbd__matrix_1ga6d27ba5612c09d80087e854b21fb9e65).

    int input\_kbd\_matrix\_common\_init(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Common function to initialize a keyboard matrix device at init time.

        This function must be called at the end of the device init function.

        Parameters:
        :   - **dev** – Keyboard matrix device instance.

        Return values:
        :   - **0** – If initialized successfully.
            - **-errno** – Negative errno in case of failure.

    struct input\_kbd\_matrix\_api
    :   *#include <input\_kbd\_matrix.h>*

        Keyboard matrix internal APIs.

        Public Members

        void (\*drive\_column)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, int col)
        :   Request to drive a specific column.

            Request to drive a specific matrix column, or none, or all.

            Param dev:
            :   Pointer to the keyboard matrix device.

            Param col:
            :   The column to drive, or [INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_NONE](#group__input__kbd__matrix_1ga2f35f23d426f93f71057a31f612a88de) or [INPUT\_KBD\_MATRIX\_COLUMN\_DRIVE\_ALL](#group__input__kbd__matrix_1ga6d27ba5612c09d80087e854b21fb9e65).

        [kbd\_row\_t](#c.kbd_row_t) (\*read\_row)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev)
        :   Read the matrix row.

            Param dev:
            :   Pointer to the keyboard matrix device.

        void (\*set\_detect\_mode)(const struct [device](../../kernel/drivers/index.md#c.device "device") \*dev, bool enabled)
        :   Request to put the matrix in detection mode.

            Request to put the driver in detection mode, this is called after a request to drive all the column and typically involves reenabling interrupts row pin changes.

            Param dev:
            :   Pointer to the keyboard matrix device.

            Param enable:
            :   Whether detection mode has to be enabled or disabled.

    struct input\_kbd\_matrix\_common\_config
    :   *#include <input\_kbd\_matrix.h>*

        Common keyboard matrix config.

        This structure **must** be placed first in the driver’s config structure.

    struct input\_kbd\_matrix\_common\_data
    :   *#include <input\_kbd\_matrix.h>*

        Common keyboard matrix data.

        This structure **must** be placed first in the driver’s data structure.
