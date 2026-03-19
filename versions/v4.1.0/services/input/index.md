---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/services/input/index.html
original_path: services/input/index.html
---

# Input

The input subsystem provides an API for dispatching input events from input
devices to the application.

## Input Events

The subsystem is built around the [`input_event`](../../doxygen/html/structinput__event.md) structure. An input
event represents a change in an individual event entity, for example the state
of a single button, or a movement in a single axis.

The [`input_event`](../../doxygen/html/structinput__event.md) structure describes the specific event, and
includes a synchronization bit to indicate that the device reached a stable
state, for example when the events corresponding to multiple axes of a
multi-axis device have been reported.

## Input Devices

An input device can report input events directly using [`input_report()`](../../doxygen/html/group__input__interface.md#gafe511e2ca9402ff539ebd05b8f28929e)
or any related function; for example buttons or other on-off input entities
would use [`input_report_key()`](../../doxygen/html/group__input__interface.md#gaeb9fa2d4bb990e67ab0a2bd20a141d20).

Complex devices may use a combination of multiple events, and set the `sync`
bit once the output is stable.

The `input_report*` functions take a [`device`](../../doxygen/html/structdevice.md) pointer, which is
used to indicate which device reported the event and can be used by subscribers
to only receive events from a specific device. If there’s no actual device
associated with the event, it can be set to `NULL`, in which case only
subscribers with no device filter will receive the event.

## Application API

An application can register a callback using the
[`INPUT_CALLBACK_DEFINE`](../../doxygen/html/group__input__interface.md#gac986cdf392f9aa0a771c8e4e92c479a3) macro. If a device node is specified, the
callback is only invoked for events from the specific device, otherwise the
callback will receive all the events in the system. This is the only type of
filtering supported, any more complex filtering logic has to be implemented in
the callback itself.

The subsystem can operate synchronously or by using an event queue, depending
on the [`CONFIG_INPUT_MODE`](../../kconfig.md#CONFIG_INPUT_MODE "CONFIG_INPUT_MODE") option. If the input thread is used,
all the events are added to a queue and executed in a common `input` thread.
If the thread is not used, the callback are invoked directly in the input
driver context.

The synchronous mode can be used in a simple application to keep a minimal
footprint, or in a complex application with an existing event model, where the
callback is just a wrapper to pipe back the event in a more complex application
specific event system.

## HID code mapping

A common use case for input devices is to use them to generate HID reports. For
this purpose, the [`input_to_hid_code()`](../../doxygen/html/group__input__interface.md#ga094b3ccfc2e111c4b2a000e9c2fe133c) and
[`input_to_hid_modifier()`](../../doxygen/html/group__input__interface.md#ga86ac2267d08e91bcc09c5b091042cfde) functions can be used to map input codes to HID
codes and modifiers.

## Kscan Compatibility

Input devices generating X/Y/Touch events can be used in existing applications
based on the [Keyboard Scan](../../hardware/peripherals/kscan.md#kscan-api) API by enabling both
[`CONFIG_INPUT`](../../kconfig.md#CONFIG_INPUT "CONFIG_INPUT") and [`CONFIG_KSCAN`](../../kconfig.md#CONFIG_KSCAN "CONFIG_KSCAN"), defining a
[`zephyr,kscan-input`](../../build/dts/api/bindings/kscan/zephyr%2Ckscan-input.md#std-dtcompatible-zephyr-kscan-input) node as a child node of the corresponding
input device and pointing the `zephyr,keyboard-scan` chosen node to the
compatibility device node, for example:

```devicetree
chosen {
    zephyr,keyboard-scan = &kscan_input;
};

ft5336@38 {
    ...
    kscan_input: kscan-input {
        compatible = "zephyr,kscan-input";
    };
};
```

## General Purpose Drivers

- [`adc-keys`](../../build/dts/api/bindings/input/adc-keys.md#std-dtcompatible-adc-keys): for buttons connected to a resistor ladder.
- [`analog-axis`](../../build/dts/api/bindings/input/analog-axis.md#std-dtcompatible-analog-axis): for absolute position devices connected to an
  ADC input (thumbsticks, sliders…).
- [`gpio-kbd-matrix`](../../build/dts/api/bindings/input/gpio-kbd-matrix.md#std-dtcompatible-gpio-kbd-matrix): for GPIO-connected keyboard matrices.
- [`gpio-keys`](../../build/dts/api/bindings/input/gpio-keys.md#std-dtcompatible-gpio-keys): for switches directly connected to a GPIO,
  implements button debouncing.
- [`gpio-qdec`](../../build/dts/api/bindings/input/gpio-qdec.md#std-dtcompatible-gpio-qdec): for GPIO-connected quadrature encoders.
- [`input-keymap`](../../build/dts/api/bindings/input/input-keymap.md#std-dtcompatible-input-keymap): maps row/col/touch events from a keyboard
  matrix to key events.
- [`zephyr,input-longpress`](../../build/dts/api/bindings/input/zephyr%2Cinput-longpress.md#std-dtcompatible-zephyr-input-longpress): listens for key events, emits events
  for short and long press.
- [`zephyr,input-double-tap`](../../build/dts/api/bindings/input/zephyr%2Cinput-double-tap.md#std-dtcompatible-zephyr-input-double-tap): listens for key events, emits events
  for input double taps
- [`zephyr,lvgl-button-input`](../../build/dts/api/bindings/input/zephyr%2Clvgl-button-input.md#std-dtcompatible-zephyr-lvgl-button-input)
  [`zephyr,lvgl-encoder-input`](../../build/dts/api/bindings/input/zephyr%2Clvgl-encoder-input.md#std-dtcompatible-zephyr-lvgl-encoder-input)
  [`zephyr,lvgl-keypad-input`](../../build/dts/api/bindings/input/zephyr%2Clvgl-keypad-input.md#std-dtcompatible-zephyr-lvgl-keypad-input)
  [`zephyr,lvgl-pointer-input`](../../build/dts/api/bindings/input/zephyr%2Clvgl-pointer-input.md#std-dtcompatible-zephyr-lvgl-pointer-input): listens for input events and
  translates those to various types of LVGL input devices.

## Detailed Driver Documentation

## API Reference

[Input Interface](../../doxygen/html/group__input__interface.md)

Related code samples

- [LVGL basic sample](../../samples/subsys/display/lvgl/README.md#lvgl "Display a "Hello World" and react to user input using LVGL.")Display a "Hello World" and react to user input using LVGL.
- [USB HID keyboard](../../samples/subsys/usb/hid-keyboard/README.md#usb-hid-keyboard "Implement a basic HID keyboard device.")Implement a basic HID keyboard device.
- [USB HID mouse](../../samples/subsys/usb/hid-mouse/README.md#usb-hid-mouse "Implement a basic HID mouse device.")Implement a basic HID mouse device.

## Input Event Definitions

[Input Event Definitions](../../doxygen/html/group__input__events.md)

Related code samples

- [Draw touch events](../../samples/subsys/input/draw_touch_events/README.md#draw_touch_events "Visualize touch events on a display.")Visualize touch events on a display.
- [Input dump](../../samples/subsys/input/input_dump/README.md#input-dump "Print all input events.")Print all input events.
- [USB MIDI2 device](../../samples/subsys/usb/midi/README.md#usb-midi2-device "Implements a simple USB MIDI loopback and keyboard device.")Implements a simple USB MIDI loopback and keyboard device.

## Analog Axis API Reference

[Analog axis API](../../doxygen/html/group__input__analog__axis.md)

## Touchscreen API Reference

[Touchscreen Event Report API](../../doxygen/html/group__touch__events.md)
