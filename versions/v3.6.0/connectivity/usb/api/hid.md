---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/usb/api/hid.html
original_path: connectivity/usb/api/hid.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Human Interface Devices (HID)

Common USB HID part that can be used outside of USB support, defined in
header file [include/zephyr/usb/class/hid.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/usb/class/hid.h).

## HID types reference

*group* usb\_hid\_definitions
:   hid.h API

    USB HID types and values

    USB\_HID\_VERSION
    :   HID Specification release v1.11.

    USB\_DESC\_HID
    :   USB HID Class HID descriptor type.

    USB\_DESC\_HID\_REPORT
    :   USB HID Class Report descriptor type.

    USB\_DESC\_HID\_PHYSICAL
    :   USB HID Class physical descriptor type.

    USB\_HID\_GET\_REPORT
    :   USB HID Class GetReport bRequest value.

    USB\_HID\_GET\_IDLE
    :   USB HID Class GetIdle bRequest value.

    USB\_HID\_GET\_PROTOCOL
    :   USB HID Class GetProtocol bRequest value.

    USB\_HID\_SET\_REPORT
    :   USB HID Class SetReport bRequest value.

    USB\_HID\_SET\_IDLE
    :   USB HID Class SetIdle bRequest value.

    USB\_HID\_SET\_PROTOCOL
    :   USB HID Class SetProtocol bRequest value.

    HID\_BOOT\_IFACE\_CODE\_NONE
    :   USB HID Boot Interface Protocol (bInterfaceProtocol) Code None.

    HID\_BOOT\_IFACE\_CODE\_KEYBOARD
    :   USB HID Boot Interface Protocol (bInterfaceProtocol) Code Keyboard.

    HID\_BOOT\_IFACE\_CODE\_MOUSE
    :   USB HID Boot Interface Protocol (bInterfaceProtocol) Code Mouse.

    HID\_PROTOCOL\_BOOT
    :   USB HID Class Boot protocol code.

    HID\_PROTOCOL\_REPORT
    :   USB HID Class Report protocol code.

    HID\_ITEM\_TYPE\_MAIN
    :   HID Main item type.

    HID\_ITEM\_TYPE\_GLOBAL
    :   HID Global item type.

    HID\_ITEM\_TYPE\_LOCAL
    :   HID Local item type.

    HID\_ITEM\_TAG\_INPUT
    :   HID Input item tag.

    HID\_ITEM\_TAG\_OUTPUT
    :   HID Output item tag.

    HID\_ITEM\_TAG\_COLLECTION
    :   HID Collection item tag.

    HID\_ITEM\_TAG\_FEATURE
    :   HID Feature item tag.

    HID\_ITEM\_TAG\_COLLECTION\_END
    :   HID End Collection item tag.

    HID\_ITEM\_TAG\_USAGE\_PAGE
    :   HID Usage Page item tag.

    HID\_ITEM\_TAG\_LOGICAL\_MIN
    :   HID Logical Minimum item tag.

    HID\_ITEM\_TAG\_LOGICAL\_MAX
    :   HID Logical Maximum item tag.

    HID\_ITEM\_TAG\_PHYSICAL\_MIN
    :   HID Physical Minimum item tag.

    HID\_ITEM\_TAG\_PHYSICAL\_MAX
    :   HID Physical Maximum item tag.

    HID\_ITEM\_TAG\_UNIT\_EXPONENT
    :   HID Unit Exponent item tag.

    HID\_ITEM\_TAG\_UNIT
    :   HID Unit item tag.

    HID\_ITEM\_TAG\_REPORT\_SIZE
    :   HID Report Size item tag.

    HID\_ITEM\_TAG\_REPORT\_ID
    :   HID Report ID item tag.

    HID\_ITEM\_TAG\_REPORT\_COUNT
    :   HID Report count item tag.

    HID\_ITEM\_TAG\_USAGE
    :   HID Usage item tag.

    HID\_ITEM\_TAG\_USAGE\_MIN
    :   HID Usage Minimum item tag.

    HID\_ITEM\_TAG\_USAGE\_MAX
    :   HID Usage Maximum item tag.

    HID\_COLLECTION\_PHYSICAL
    :   Physical collection type.

    HID\_COLLECTION\_APPLICATION
    :   Application collection type.

    HID\_COLLECTION\_LOGICAL
    :   Logical collection type.

    HID\_COLLECTION\_REPORT
    :   Report collection type.

    HID\_COLLECTION\_NAMED\_ARRAY
    :   Named Array collection type.

    HID\_COLLECTION\_USAGE\_SWITCH
    :   Usage Switch collection type.

    HID\_COLLECTION\_MODIFIER
    :   Modifier collection type.

    HID\_USAGE\_GEN\_DESKTOP
    :   HID Generic Desktop Controls Usage page.

    HID\_USAGE\_GEN\_KEYBOARD
    :   HID Keyboard Usage page.

    HID\_USAGE\_GEN\_LEDS
    :   HID LEDs Usage page.

    HID\_USAGE\_GEN\_BUTTON
    :   HID Button Usage page.

    HID\_USAGE\_GEN\_DESKTOP\_UNDEFINED
    :   HID Generic Desktop Undefined Usage ID.

    HID\_USAGE\_GEN\_DESKTOP\_POINTER
    :   HID Generic Desktop Pointer Usage ID.

    HID\_USAGE\_GEN\_DESKTOP\_MOUSE
    :   HID Generic Desktop Mouse Usage ID.

    HID\_USAGE\_GEN\_DESKTOP\_JOYSTICK
    :   HID Generic Desktop Joystick Usage ID.

    HID\_USAGE\_GEN\_DESKTOP\_GAMEPAD
    :   HID Generic Desktop Gamepad Usage ID.

    HID\_USAGE\_GEN\_DESKTOP\_KEYBOARD
    :   HID Generic Desktop Keyboard Usage ID.

    HID\_USAGE\_GEN\_DESKTOP\_KEYPAD
    :   HID Generic Desktop Keypad Usage ID.

    HID\_USAGE\_GEN\_DESKTOP\_X
    :   HID Generic Desktop X Usage ID.

    HID\_USAGE\_GEN\_DESKTOP\_Y
    :   HID Generic Desktop Y Usage ID.

    HID\_USAGE\_GEN\_DESKTOP\_WHEEL
    :   HID Generic Desktop Wheel Usage ID.

## HID items reference

*group* usb\_hid\_items
:   Defines

    HID\_ITEM(bTag, bType, bSize)
    :   Define HID short item.

        Parameters:
        :   - **bTag** – Item tag
            - **bType** – Item type
            - **bSize** – Item data size

        Returns:
        :   HID Input item

    HID\_INPUT(a)
    :   Define HID Input item with the data length of one byte.

        For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1ga3696f0782268d504b0c8bb540236779f), [HID\_KEYBOARD\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1gaea973ffbe1612187c90614133956cfd6)

        Parameters:
        :   - **a** – Input item data

        Returns:
        :   HID Input item

    HID\_OUTPUT(a)
    :   Define HID Output item with the data length of one byte.

        For usage examples, see [HID\_KEYBOARD\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1gaea973ffbe1612187c90614133956cfd6)

        Parameters:
        :   - **a** – Output item data

        Returns:
        :   HID Output item

    HID\_FEATURE(a)
    :   Define HID Feature item with the data length of one byte.

        Parameters:
        :   - **a** – Feature item data

        Returns:
        :   HID Feature item

    HID\_COLLECTION(a)
    :   Define HID Collection item with the data length of one byte.

        For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1ga3696f0782268d504b0c8bb540236779f), [HID\_KEYBOARD\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1gaea973ffbe1612187c90614133956cfd6)

        Parameters:
        :   - **a** – Collection item data

        Returns:
        :   HID Collection item

    HID\_END\_COLLECTION
    :   Define HID End Collection (non-data) item.

        For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1ga3696f0782268d504b0c8bb540236779f), [HID\_KEYBOARD\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1gaea973ffbe1612187c90614133956cfd6)

        Returns:
        :   HID End Collection item

    HID\_USAGE\_PAGE(page)
    :   Define HID Usage Page item.

        For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1ga3696f0782268d504b0c8bb540236779f), [HID\_KEYBOARD\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1gaea973ffbe1612187c90614133956cfd6)

        Parameters:
        :   - **page** – Usage Page

        Returns:
        :   HID Usage Page item

    HID\_LOGICAL\_MIN8(a)
    :   Define HID Logical Minimum item with the data length of one byte.

        For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1ga3696f0782268d504b0c8bb540236779f), [HID\_KEYBOARD\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1gaea973ffbe1612187c90614133956cfd6)

        Parameters:
        :   - **a** – Minimum value in logical units

        Returns:
        :   HID Logical Minimum item

    HID\_LOGICAL\_MAX8(a)
    :   Define HID Logical Maximum item with the data length of one byte.

        For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1ga3696f0782268d504b0c8bb540236779f), [HID\_KEYBOARD\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1gaea973ffbe1612187c90614133956cfd6)

        Parameters:
        :   - **a** – Maximum value in logical units

        Returns:
        :   HID Logical Maximum item

    HID\_LOGICAL\_MIN16(a, b)
    :   Define HID Logical Minimum item with the data length of two bytes.

        Parameters:
        :   - **a** – Minimum value lower byte
            - **b** – Minimum value higher byte

        Returns:
        :   HID Logical Minimum item

    HID\_LOGICAL\_MAX16(a, b)
    :   Define HID Logical Maximum item with the data length of two bytes.

        Parameters:
        :   - **a** – Minimum value lower byte
            - **b** – Minimum value higher byte

        Returns:
        :   HID Logical Maximum item

    HID\_LOGICAL\_MIN32(a, b, c, d)
    :   Define HID Logical Minimum item with the data length of four bytes.

        Parameters:
        :   - **a** – Minimum value lower byte
            - **b** – Minimum value low middle byte
            - **c** – Minimum value high middle byte
            - **d** – Minimum value higher byte

        Returns:
        :   HID Logical Minimum item

    HID\_LOGICAL\_MAX32(a, b, c, d)
    :   Define HID Logical Maximum item with the data length of four bytes.

        Parameters:
        :   - **a** – Minimum value lower byte
            - **b** – Minimum value low middle byte
            - **c** – Minimum value high middle byte
            - **d** – Minimum value higher byte

        Returns:
        :   HID Logical Maximum item

    HID\_REPORT\_SIZE(size)
    :   Define HID Report Size item with the data length of one byte.

        For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1ga3696f0782268d504b0c8bb540236779f), [HID\_KEYBOARD\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1gaea973ffbe1612187c90614133956cfd6)

        Parameters:
        :   - **size** – Report field size in bits

        Returns:
        :   HID Report Size item

    HID\_REPORT\_ID(id)
    :   Define HID Report ID item with the data length of one byte.

        Parameters:
        :   - **id** – Report ID

        Returns:
        :   HID Report ID item

    HID\_REPORT\_COUNT(count)
    :   Define HID Report Count item with the data length of one byte.

        For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1ga3696f0782268d504b0c8bb540236779f), [HID\_KEYBOARD\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1gaea973ffbe1612187c90614133956cfd6)

        Parameters:
        :   - **count** – Number of data fields included in the report

        Returns:
        :   HID Report Count item

    HID\_USAGE(idx)
    :   Define HID Usage Index item with the data length of one byte.

        For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1ga3696f0782268d504b0c8bb540236779f), [HID\_KEYBOARD\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1gaea973ffbe1612187c90614133956cfd6)

        Parameters:
        :   - **idx** – Number of data fields included in the report

        Returns:
        :   HID Usage Index item

    HID\_USAGE\_MIN8(a)
    :   Define HID Usage Minimum item with the data length of one byte.

        For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1ga3696f0782268d504b0c8bb540236779f), [HID\_KEYBOARD\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1gaea973ffbe1612187c90614133956cfd6)

        Parameters:
        :   - **a** – Starting Usage

        Returns:
        :   HID Usage Minimum item

    HID\_USAGE\_MAX8(a)
    :   Define HID Usage Maximum item with the data length of one byte.

        For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1ga3696f0782268d504b0c8bb540236779f), [HID\_KEYBOARD\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1gaea973ffbe1612187c90614133956cfd6)

        Parameters:
        :   - **a** – Ending Usage

        Returns:
        :   HID Usage Maximum item

    HID\_USAGE\_MIN16(a, b)
    :   Define HID Usage Minimum item with the data length of two bytes.

        For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1ga3696f0782268d504b0c8bb540236779f), [HID\_KEYBOARD\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1gaea973ffbe1612187c90614133956cfd6)

        Parameters:
        :   - **a** – Starting Usage lower byte
            - **b** – Starting Usage higher byte

        Returns:
        :   HID Usage Minimum item

    HID\_USAGE\_MAX16(a, b)
    :   Define HID Usage Maximum item with the data length of two bytes.

        For usage examples, see [HID\_MOUSE\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1ga3696f0782268d504b0c8bb540236779f), [HID\_KEYBOARD\_REPORT\_DESC()](#group__usb__hid__mk__report__desc_1gaea973ffbe1612187c90614133956cfd6)

        Parameters:
        :   - **a** – Ending Usage lower byte
            - **b** – Ending Usage higher byte

        Returns:
        :   HID Usage Maximum item

## HID Mouse and Keyboard report descriptors

The pre-defined Mouse and Keyboard report descriptors can be used by
a HID device implementation or simply as examples.

*group* usb\_hid\_mk\_report\_desc
:   Defines

    HID\_MOUSE\_REPORT\_DESC(bcnt)
    :   Simple HID mouse report descriptor for n button mouse.

        Parameters:
        :   - **bcnt** – Button count. Allowed values from 1 to 8.

    HID\_KEYBOARD\_REPORT\_DESC()
    :   Simple HID keyboard report descriptor.

    Enums

    enum hid\_kbd\_code
    :   HID keyboard button codes.

        *Values:*

        enumerator HID\_KEY\_A = 4

        enumerator HID\_KEY\_B = 5

        enumerator HID\_KEY\_C = 6

        enumerator HID\_KEY\_D = 7

        enumerator HID\_KEY\_E = 8

        enumerator HID\_KEY\_F = 9

        enumerator HID\_KEY\_G = 10

        enumerator HID\_KEY\_H = 11

        enumerator HID\_KEY\_I = 12

        enumerator HID\_KEY\_J = 13

        enumerator HID\_KEY\_K = 14

        enumerator HID\_KEY\_L = 15

        enumerator HID\_KEY\_M = 16

        enumerator HID\_KEY\_N = 17

        enumerator HID\_KEY\_O = 18

        enumerator HID\_KEY\_P = 19

        enumerator HID\_KEY\_Q = 20

        enumerator HID\_KEY\_R = 21

        enumerator HID\_KEY\_S = 22

        enumerator HID\_KEY\_T = 23

        enumerator HID\_KEY\_U = 24

        enumerator HID\_KEY\_V = 25

        enumerator HID\_KEY\_W = 26

        enumerator HID\_KEY\_X = 27

        enumerator HID\_KEY\_Y = 28

        enumerator HID\_KEY\_Z = 29

        enumerator HID\_KEY\_1 = 30

        enumerator HID\_KEY\_2 = 31

        enumerator HID\_KEY\_3 = 32

        enumerator HID\_KEY\_4 = 33

        enumerator HID\_KEY\_5 = 34

        enumerator HID\_KEY\_6 = 35

        enumerator HID\_KEY\_7 = 36

        enumerator HID\_KEY\_8 = 37

        enumerator HID\_KEY\_9 = 38

        enumerator HID\_KEY\_0 = 39

        enumerator HID\_KEY\_ENTER = 40

        enumerator HID\_KEY\_ESC = 41

        enumerator HID\_KEY\_BACKSPACE = 42

        enumerator HID\_KEY\_TAB = 43

        enumerator HID\_KEY\_SPACE = 44

        enumerator HID\_KEY\_MINUS = 45

        enumerator HID\_KEY\_EQUAL = 46

        enumerator HID\_KEY\_LEFTBRACE = 47

        enumerator HID\_KEY\_RIGHTBRACE = 48

        enumerator HID\_KEY\_BACKSLASH = 49

        enumerator HID\_KEY\_HASH = 50

        enumerator HID\_KEY\_SEMICOLON = 51

        enumerator HID\_KEY\_APOSTROPHE = 52

        enumerator HID\_KEY\_GRAVE = 53

        enumerator HID\_KEY\_COMMA = 54

        enumerator HID\_KEY\_DOT = 55

        enumerator HID\_KEY\_SLASH = 56

        enumerator HID\_KEY\_CAPSLOCK = 57

        enumerator HID\_KEY\_F1 = 58

        enumerator HID\_KEY\_F2 = 59

        enumerator HID\_KEY\_F3 = 60

        enumerator HID\_KEY\_F4 = 61

        enumerator HID\_KEY\_F5 = 62

        enumerator HID\_KEY\_F6 = 63

        enumerator HID\_KEY\_F7 = 64

        enumerator HID\_KEY\_F8 = 65

        enumerator HID\_KEY\_F9 = 66

        enumerator HID\_KEY\_F10 = 67

        enumerator HID\_KEY\_F11 = 68

        enumerator HID\_KEY\_F12 = 69

        enumerator HID\_KEY\_SYSRQ = 70

        enumerator HID\_KEY\_SCROLLLOCK = 71

        enumerator HID\_KEY\_PAUSE = 72

        enumerator HID\_KEY\_INSERT = 73

        enumerator HID\_KEY\_HOME = 74

        enumerator HID\_KEY\_PAGEUP = 75

        enumerator HID\_KEY\_DELETE = 76

        enumerator HID\_KEY\_END = 77

        enumerator HID\_KEY\_PAGEDOWN = 78

        enumerator HID\_KEY\_RIGHT = 79

        enumerator HID\_KEY\_LEFT = 80

        enumerator HID\_KEY\_DOWN = 81

        enumerator HID\_KEY\_UP = 82

        enumerator HID\_KEY\_NUMLOCK = 83

        enumerator HID\_KEY\_KPSLASH = 84

        enumerator HID\_KEY\_KPASTERISK = 85

        enumerator HID\_KEY\_KPMINUS = 86

        enumerator HID\_KEY\_KPPLUS = 87

        enumerator HID\_KEY\_KPENTER = 88

        enumerator HID\_KEY\_KP\_1 = 89

        enumerator HID\_KEY\_KP\_2 = 90

        enumerator HID\_KEY\_KP\_3 = 91

        enumerator HID\_KEY\_KP\_4 = 92

        enumerator HID\_KEY\_KP\_5 = 93

        enumerator HID\_KEY\_KP\_6 = 94

        enumerator HID\_KEY\_KP\_7 = 95

        enumerator HID\_KEY\_KP\_8 = 96

        enumerator HID\_KEY\_KP\_9 = 97

        enumerator HID\_KEY\_KP\_0 = 98

    enum hid\_kbd\_modifier
    :   HID keyboard modifiers.

        *Values:*

        enumerator HID\_KBD\_MODIFIER\_NONE = 0x00

        enumerator HID\_KBD\_MODIFIER\_LEFT\_CTRL = 0x01

        enumerator HID\_KBD\_MODIFIER\_LEFT\_SHIFT = 0x02

        enumerator HID\_KBD\_MODIFIER\_LEFT\_ALT = 0x04

        enumerator HID\_KBD\_MODIFIER\_LEFT\_UI = 0x08

        enumerator HID\_KBD\_MODIFIER\_RIGHT\_CTRL = 0x10

        enumerator HID\_KBD\_MODIFIER\_RIGHT\_SHIFT = 0x20

        enumerator HID\_KBD\_MODIFIER\_RIGHT\_ALT = 0x40

        enumerator HID\_KBD\_MODIFIER\_RIGHT\_UI = 0x80

    enum hid\_kbd\_led
    :   HID keyboard LEDs.

        *Values:*

        enumerator HID\_KBD\_LED\_NUM\_LOCK = 0x01

        enumerator HID\_KBD\_LED\_CAPS\_LOCK = 0x02

        enumerator HID\_KBD\_LED\_SCROLL\_LOCK = 0x04

        enumerator HID\_KBD\_LED\_COMPOSE = 0x08

        enumerator HID\_KBD\_LED\_KANA = 0x10
