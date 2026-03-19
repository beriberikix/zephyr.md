---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/basic/blinky/README.html
original_path: samples/basic/blinky/README.html
---

# Blinky

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/basic/blinky/README.rst/..)

## Overview

The Blinky sample blinks an LED forever using the [GPIO API](../../../hardware/peripherals/gpio.md#gpio-api).

The source code shows how to:

1. Get a pin specification from the [devicetree](../../../build/dts/index.md#dt-guide) as a
   [`gpio_dt_spec`](../../../doxygen/html/structgpio__dt__spec.md)
2. Configure the GPIO pin as an output
3. Toggle the pin forever

See [PWM Blinky](../blinky_pwm/README.md#pwm-blinky "Blink an LED using the PWM API.") for a similar sample that uses the PWM API instead.

## Requirements

Your board must:

1. Have an LED connected via a GPIO pin (these are called “User LEDs” on many of
   Zephyr’s [Supported Boards and Shields](../../../boards/index.md#boards)).
2. Have the LED configured using the `led0` devicetree alias.

## Building and Running

Build and flash Blinky as follows, changing `reel_board` for your board:

```shell
west build -b reel_board samples/basic/blinky
west flash
```

After flashing, the LED starts to blink and messages with the current LED state
are printed on the console. If a runtime error occurs, the sample exits without
printing to the console.

## Build errors

You will see a build error at the source code line defining the `struct
gpio_dt_spec led` variable if you try to build Blinky for an unsupported
board.

On GCC-based toolchains, the error looks like this:

```text
error: '__device_dts_ord_DT_N_ALIAS_led_P_gpios_IDX_0_PH_ORD' undeclared here (not in a function)
```

## Adding board support

To add support for your board, add something like this to your devicetree:

```dts
/ {
     aliases {
             led0 = &myled0;
     };

     leds {
             compatible = "gpio-leds";
             myled0: led_0 {
                     gpios = <&gpio0 13 GPIO_ACTIVE_LOW>;
             };
     };
};
```

The above sets your board’s `led0` alias to use pin 13 on GPIO controller
`gpio0`. The pin flags [`GPIO_ACTIVE_HIGH`](../../../doxygen/html/group__gpio__interface.md#gad93badd2828d065e7fd14cf40dd05039) mean the LED is on when
the pin is set to its high state, and off when the pin is in its low state.

Tips:

- See [`gpio-leds`](../../../build/dts/api/bindings/led/gpio-leds.md#std-dtcompatible-gpio-leds) for more information on defining GPIO-based LEDs
  in devicetree.
- If you’re not sure what to do, check the devicetrees for supported boards which
  use the same SoC as your target. See [Get your devicetree and generated header](../../../build/dts/howtos.md#get-devicetree-outputs) for details.
- See [include/zephyr/dt-bindings/gpio/gpio.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/dt-bindings/gpio/gpio.h) for the flags you can use
  in devicetree.
- If the LED is built in to your board hardware, the alias should be defined in
  your [BOARD.dts file](../../../build/dts/intro-input-output.md#devicetree-in-out-files). Otherwise, you can
  define one in a [devicetree overlay](../../../build/dts/howtos.md#set-devicetree-overlays).

## See also

[GPIO Driver APIs](../../../doxygen/html/group__gpio__interface.md)
