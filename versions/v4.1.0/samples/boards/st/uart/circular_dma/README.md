---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/boards/st/uart/circular_dma/README.html
original_path: samples/boards/st/uart/circular_dma/README.html
---

# UART circular mode

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/st/uart/circular_dma/README.rst/..)

## Overview

This sample demonstrates how to use STM32 UART serial driver with DMA in circular mode.
It reads data from the console and echoes it back.

By default, the UART peripheral that is normally assigned to the Zephyr shell
is used, hence the majority of boards should be able to run this sample.

## Building and Running

Build and flash the sample as follows, changing `nucleo_g071rb` for
your board:

```shell
west build -b nucleo_g071rb samples/boards/st/uart/circular_dma
west flash
```

### Sample Output

```shell
Enter message to fill RX buffer size and press enter :
# Type e.g. :
# "Lorem Ipsum is simply dummy text of the printing and typesetting industry.
# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
# when an unknown printer took a galley of type and scrambled it to make a type specimen book.
# It has survived not only five centuries, but also the leap into electronic typesetting,
# remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing software
# like Aldus PageMaker including versions of Lorem Ipsum."

Lorem Ipsum is simply dummy text of the printing and typesetting industry.
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a type specimen book.
It has survived not only five centuries, but also the leap into electronic typesetting,
remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset
sheets containing Lorem Ipsum passages, and more recently with desktop publishing software
like Aldus PageMaker including versions of Lorem Ipsum.
```

## See also

[UART Interface](../../../../../doxygen/html/group__uart__interface.md)
