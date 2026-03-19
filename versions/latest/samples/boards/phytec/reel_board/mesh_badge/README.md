---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/samples/boards/phytec/reel_board/mesh_badge/README.html
original_path: samples/boards/phytec/reel_board/mesh_badge/README.html
---

# Bluetooth Mesh badge

[
Browse source code on GitHub
](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/phytec/reel_board/mesh_badge/README.rst/..)

## Overview

This sample app for the reel board showcases Bluetooth Mesh.

The app starts off as a regular Bluetooth GATT peripheral application.
Install the “nRF Connect” app on your phone (available both for
Android and iOS) to access the service that the app exposes. The service
can also be accessed with any Bluetooth LE GATT client from your PC,
however these instructions focus on the necessary steps for phones.

## Steps to set up

1. On your phone, use the nRF Connect app to Scan for devices and look
   for “reel board”
2. Connect to the device. You’ll see a single service - select it
3. Request to write to the characteristic by pressing on the upward pointing
   arrow symbol
4. Select “Text” to enter text instead of hex
5. Enter your name (or any other arbitrary text). Multiple words
   separated by spaces are possible. The font used on the reel display
   allows three rows of up to 12 characters
   wide text. You can force line breaks with a comma.
6. Press “Send” - this will trigger pairing since this is a protected
   characteristic. The passkey for the pairing will be shown on the board’s
   display. Enter the passkey in your phone.
7. Once pairing is complete the board will show the text you sent. If
   you’re not happy with it you can try writing something else.
8. When you’re happy with the text, disconnect from the board (exit the app or
   go back to the device scan page)
9. Once disconnected the board switches over to Bluetooth Mesh mode, and you
   can’t connect to it anymore over GATT.

If you configure multiple boards like this they can communicate with
each other over mesh: by pressing the user button on the board the first
word (name) of the stored text will be sent to all other boards in
the network and cause the other boards to display “<name> says hi!”.

To reset a board to its initial state (disable mesh, erase the stored
text, and make it connectable over GATT):

1. Keep the user button pressed when powering on (or press the reset button
   when powered)
2. Wait until “Resetting Device” is shown

## See also

[Monochrome Character Framebuffer](../../../../../doxygen/html/group__monochrome__character__framebuffer.md)

[Bluetooth Mesh](../../../../../doxygen/html/group__bt__mesh.md)

[Generic Attribute Profile (GATT)](../../../../../doxygen/html/group__bt__gatt.md)

[Bluetooth APIs](../../../../../doxygen/html/group__bluetooth.md)
