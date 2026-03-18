---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/samples/basic/button/README.html
original_path: samples/basic/button/README.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Button

## Overview

A simple button demo showcasing the use of GPIO input with interrupts.
The sample prints a message to the console each time a button is pressed.

## Requirements

The board hardware must have a push button connected via a GPIO pin. These are
called “User buttons” on many of Zephyr’s [Supported Boards](../../../boards/index.md#boards).

The button must be configured using the `sw0` [devicetree](../../../build/dts/index.md#dt-guide)
alias, usually in the [BOARD.dts file](../../../build/dts/intro-input-output.md#devicetree-in-out-files). You will
see this error if you try to build this sample for an unsupported board:

```text
Unsupported board: sw0 devicetree alias is not defined
```

You may see additional build errors if the `sw0` alias exists, but is not
properly defined.

The sample additionally supports an optional `led0` devicetree alias. This is
the same alias used by the [Blinky](../blinky/README.md#blinky "Blink an LED forever using the GPIO API.") sample. If this is provided, the LED
will be turned on when the button is pressed, and turned off off when it is
released.

### Devicetree details

This section provides more details on devicetree configuration.

Here is a minimal devicetree fragment which supports this sample. This only
includes a `sw0` alias; the optional `led0` alias is left out for
simplicity.

```devicetree
/ {
     aliases {
             sw0 = &button0;
     };

     soc {
             gpio0: gpio@0 {
                     status = "okay";
                     gpio-controller;
                     #gpio-cells = <2>;
                     /* ... */
             };
     };

     buttons {
             compatible = "gpio-keys";
             button0: button_0 {
                     gpios = < &gpio0 PIN FLAGS >;
                     label = "User button";
             };
             /* ... other buttons ... */
     };
};
```

As shown, the `sw0` devicetree alias must point to a child node of a node
with a “gpio-keys” [compatible](../../../build/dts/intro-syntax-structure.md#dt-important-props).

The above situation is for the common case where:

- `gpio0` is an example node label referring to a GPIO controller
- `PIN` should be a pin number, like `8` or `0`
- `FLAGS` should be a logical OR of [GPIO configuration flags](../../../hardware/peripherals/gpio.md#gpio-api)
  meant to apply to the button, such as `(GPIO_PULL_UP | GPIO_ACTIVE_LOW)`

This assumes the common case, where `#gpio-cells = <2>` in the `gpio0`
node, and that the GPIO controller’s devicetree binding names those two cells
“pin” and “flags” like so:

```yaml
gpio-cells:
  - pin
  - flags
```

This sample requires a `pin` cell in the `gpios` property. The `flags`
cell is optional, however, and the sample still works if the GPIO cells
do not contain `flags`.

## Building and Running

This sample can be built for multiple boards, in this example we will build it
for the nucleo\_f103rb board:

```shell
west build -b nucleo_f103rb samples/basic/button
```

After startup, the program looks up a predefined GPIO device, and configures the
pin in input mode, enabling interrupt generation on falling edge. During each
iteration of the main loop, the state of GPIO line is monitored and printed to
the serial console. When the input button gets pressed, the interrupt handler
will print an information about this event along with its timestamp.
