---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/hardware/peripherals/display/index.html
original_path: hardware/peripherals/display/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# Display Interface

## API Reference

### Generic Display Interface

Related code samples

[Display](../../../samples/drivers/display/README.md#display "Draw basic rectangles on a display device.")
:   Draw basic rectangles on a display device.

[LVGL basic sample](../../../samples/subsys/display/lvgl/README.md#lvgl "Display a "Hello World" and react to user input using LVGL.")
:   Display a "Hello World" and react to user input using LVGL.

[LVGL demos](../../../samples/modules/lvgl/demos/README.md#lvgl-demos "Run LVGL built-in demos.")
:   Run LVGL built-in demos.

[LVGL line chart with accelerometer data](../../../samples/modules/lvgl/accelerometer_chart/README.md#lvgl-accelerometer-chart "Display acceleration data on a real-time chart using LVGL.")
:   Display acceleration data on a real-time chart using LVGL.

*group* Display Interface
:   Display Interface.

    **Since**
    :   1.14

    **Version**
    :   0.8.0

    Defines

    DISPLAY\_BITS\_PER\_PIXEL(fmt)
    :   Bits required per pixel for display format.

        This macro expands to the number of bits required for a given display format. It can be used to allocate a framebuffer based on a given display format type

    Typedefs

    typedef int (\*display\_blanking\_on\_api)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Callback API to turn on display blanking See [display\_blanking\_on()](#group__display__interface_1gac6ad1f33067165e4c3bf7c0c345bb4e4) for argument description.

    typedef int (\*display\_blanking\_off\_api)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Callback API to turn off display blanking See [display\_blanking\_off()](#group__display__interface_1ga4d9e288891a6bde679c3aa00b9913e1d) for argument description.

    typedef int (\*display\_write\_api)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const uint16\_t x, const uint16\_t y, const struct [display\_buffer\_descriptor](#c.display_buffer_descriptor) \*desc, const void \*buf)
    :   Callback API for writing data to the display See [display\_write()](#group__display__interface_1ga3a5114b4537039fc4d3258678b82cd18) for argument description.

    typedef int (\*display\_read\_api)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const uint16\_t x, const uint16\_t y, const struct [display\_buffer\_descriptor](#c.display_buffer_descriptor) \*desc, void \*buf)
    :   Callback API for reading data from the display See [display\_read()](#group__display__interface_1ga3f497776520b0eac16b8aea80ccbbcfc) for argument description.

    typedef void \*(\*display\_get\_framebuffer\_api)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Callback API to get framebuffer pointer See [display\_get\_framebuffer()](#group__display__interface_1ga4b66d380e46909caaa7317857f84a9e8) for argument description.

    typedef int (\*display\_set\_brightness\_api)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t brightness)
    :   Callback API to set display brightness See [display\_set\_brightness()](#group__display__interface_1gad5cdeb245d17c8d680a5843b3cce1f8c) for argument description.

    typedef int (\*display\_set\_contrast\_api)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t contrast)
    :   Callback API to set display contrast See [display\_set\_contrast()](#group__display__interface_1ga855c72f72238b25f23e95e50546e2f27) for argument description.

    typedef void (\*display\_get\_capabilities\_api)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [display\_capabilities](#c.display_capabilities) \*capabilities)
    :   Callback API to get display capabilities See [display\_get\_capabilities()](#group__display__interface_1ga6a13e42773be13b141ebd8f047f8db50) for argument description.

    typedef int (\*display\_set\_pixel\_format\_api)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const enum [display\_pixel\_format](#c.display_pixel_format) pixel\_format)
    :   Callback API to set pixel format used by the display See [display\_set\_pixel\_format()](#group__display__interface_1ga7ede828663090760c2558a231d9f2150) for argument description.

    typedef int (\*display\_set\_orientation\_api)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const enum [display\_orientation](#c.display_orientation) orientation)
    :   Callback API to set orientation used by the display See [display\_set\_orientation()](#group__display__interface_1ga4e0a4dc2e434144874af014b8e7c4394) for argument description.

    Enums

    enum display\_pixel\_format
    :   Display pixel formats.

        Display pixel format enumeration.

        In case a pixel format consists out of multiple bytes the byte order is big endian.

        *Values:*

        enumerator PIXEL\_FORMAT\_RGB\_888 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   24-bit RGB

        enumerator PIXEL\_FORMAT\_MONO01 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   Monochrome (0=Black 1=White).

        enumerator PIXEL\_FORMAT\_MONO10 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   Monochrome (1=Black 0=White).

        enumerator PIXEL\_FORMAT\_ARGB\_8888 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(3)
        :   32-bit ARGB

        enumerator PIXEL\_FORMAT\_RGB\_565 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(4)
        :   16-bit RGB

        enumerator PIXEL\_FORMAT\_BGR\_565 = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(5)
        :   16-bit BGR

    enum display\_screen\_info
    :   Display screen information.

        *Values:*

        enumerator SCREEN\_INFO\_MONO\_VTILED = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)
        :   If selected, one octet represents 8 pixels ordered vertically, otherwise ordered horizontally.

        enumerator SCREEN\_INFO\_MONO\_MSB\_FIRST = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)
        :   If selected, the MSB represents the first pixel, otherwise MSB represents the last pixel.

        enumerator SCREEN\_INFO\_EPD = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)
        :   Electrophoretic Display.

        enumerator SCREEN\_INFO\_DOUBLE\_BUFFER = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(3)
        :   Screen has two alternating ram buffers.

        enumerator SCREEN\_INFO\_X\_ALIGNMENT\_WIDTH = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(4)
        :   Screen has x alignment constrained to width.

    enum display\_orientation
    :   Enumeration with possible display orientation.

        *Values:*

        enumerator DISPLAY\_ORIENTATION\_NORMAL
        :   No rotation.

        enumerator DISPLAY\_ORIENTATION\_ROTATED\_90
        :   Rotated 90 degrees clockwise.

        enumerator DISPLAY\_ORIENTATION\_ROTATED\_180
        :   Rotated 180 degrees clockwise.

        enumerator DISPLAY\_ORIENTATION\_ROTATED\_270
        :   Rotated 270 degrees clockwise.

    Functions

    static inline int display\_write(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const uint16\_t x, const uint16\_t y, const struct [display\_buffer\_descriptor](#c.display_buffer_descriptor) \*desc, const void \*buf)
    :   Write data to display.

        Parameters:
        :   - **dev** – Pointer to device structure
            - **x** – x Coordinate of the upper left corner where to write the buffer
            - **y** – y Coordinate of the upper left corner where to write the buffer
            - **desc** – Pointer to a structure describing the buffer layout
            - **buf** – Pointer to buffer array

        Return values:
        :   **0** – on success else negative errno code.

    static inline int display\_read(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const uint16\_t x, const uint16\_t y, const struct [display\_buffer\_descriptor](#c.display_buffer_descriptor) \*desc, void \*buf)
    :   Read data from display.

        Parameters:
        :   - **dev** – Pointer to device structure
            - **x** – x Coordinate of the upper left corner where to read from
            - **y** – y Coordinate of the upper left corner where to read from
            - **desc** – Pointer to a structure describing the buffer layout
            - **buf** – Pointer to buffer array

        Return values:
        :   - **0** – on success else negative errno code.
            - **-ENOSYS** – if not implemented.

    static inline void \*display\_get\_framebuffer(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get pointer to framebuffer for direct access.

        Parameters:
        :   - **dev** – Pointer to device structure

        Return values:
        :   **Pointer** – to frame buffer or NULL if direct framebuffer access is not supported

    static inline int display\_blanking\_on(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Turn display blanking on.

        This function blanks the complete display. The content of the frame buffer will be retained while blanking is enabled and the frame buffer will be accessible for read and write operations.

        In case backlight control is supported by the driver the backlight is turned off. The backlight configuration is retained and accessible for configuration.

        In case the driver supports display blanking the initial state of the driver would be the same as if this function was called.

        Parameters:
        :   - **dev** – Pointer to device structure

        Return values:
        :   - **0** – on success else negative errno code.
            - **-ENOSYS** – if not implemented.

    static inline int display\_blanking\_off(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Turn display blanking off.

        Restore the frame buffer content to the display. In case backlight control is supported by the driver the backlight configuration is restored.

        Parameters:
        :   - **dev** – Pointer to device structure

        Return values:
        :   - **0** – on success else negative errno code.
            - **-ENOSYS** – if not implemented.

    static inline int display\_set\_brightness(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t brightness)
    :   Set the brightness of the display.

        Set the brightness of the display in steps of 1/256, where 255 is full brightness and 0 is minimal.

        Parameters:
        :   - **dev** – Pointer to device structure
            - **brightness** – Brightness in steps of 1/256

        Return values:
        :   - **0** – on success else negative errno code.
            - **-ENOSYS** – if not implemented.

    static inline int display\_set\_contrast(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t contrast)
    :   Set the contrast of the display.

        Set the contrast of the display in steps of 1/256, where 255 is maximum difference and 0 is minimal.

        Parameters:
        :   - **dev** – Pointer to device structure
            - **contrast** – Contrast in steps of 1/256

        Return values:
        :   - **0** – on success else negative errno code.
            - **-ENOSYS** – if not implemented.

    static inline void display\_get\_capabilities(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, struct [display\_capabilities](#c.display_capabilities) \*capabilities)
    :   Get display capabilities.

        Parameters:
        :   - **dev** – Pointer to device structure
            - **capabilities** – Pointer to capabilities structure to populate

    static inline int display\_set\_pixel\_format(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const enum [display\_pixel\_format](#c.display_pixel_format) pixel\_format)
    :   Set pixel format used by the display.

        Parameters:
        :   - **dev** – Pointer to device structure
            - **pixel\_format** – Pixel format to be used by display

        Return values:
        :   - **0** – on success else negative errno code.
            - **-ENOSYS** – if not implemented.

    static inline int display\_set\_orientation(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const enum [display\_orientation](#c.display_orientation) orientation)
    :   Set display orientation.

        Parameters:
        :   - **dev** – Pointer to device structure
            - **orientation** – Orientation to be used by display

        Return values:
        :   - **0** – on success else negative errno code.
            - **-ENOSYS** – if not implemented.

    struct display\_capabilities
    :   *#include <display.h>*

        Structure holding display capabilities.

        Public Members

        uint16\_t x\_resolution
        :   Display resolution in the X direction.

        uint16\_t y\_resolution
        :   Display resolution in the Y direction.

        uint32\_t supported\_pixel\_formats
        :   Bitwise or of pixel formats supported by the display.

        uint32\_t screen\_info
        :   Information about display panel.

        enum [display\_pixel\_format](#c.display_pixel_format) current\_pixel\_format
        :   Currently active pixel format for the display.

        enum [display\_orientation](#c.display_orientation) current\_orientation
        :   Current display orientation.

    struct display\_buffer\_descriptor
    :   *#include <display.h>*

        Structure to describe display data buffer layout.

        Public Members

        uint32\_t buf\_size
        :   Data buffer size in bytes.

        uint16\_t width
        :   Data buffer row width in pixels.

        uint16\_t height
        :   Data buffer column height in pixels.

        uint16\_t pitch
        :   Number of pixels between consecutive rows in the data buffer.

    struct display\_driver\_api
    :   *#include <display.h>*

        Display driver API API which a display driver should expose.

### Grove LCD Display

Related code samples

[Grove LCD](../../../samples/drivers/misc/grove_display/README.md#grove-lcd "Display an incrementing counter and change the backlight color.")
:   Display an incrementing counter and change the backlight color.

*group* Grove display APIs
:   Grove display APIs.

    Defines

    GLCD\_DS\_DISPLAY\_ON

    GLCD\_DS\_DISPLAY\_OFF

    GLCD\_DS\_CURSOR\_ON

    GLCD\_DS\_CURSOR\_OFF

    GLCD\_DS\_BLINK\_ON

    GLCD\_DS\_BLINK\_OFF

    GLCD\_IS\_SHIFT\_INCREMENT

    GLCD\_IS\_SHIFT\_DECREMENT

    GLCD\_IS\_ENTRY\_LEFT

    GLCD\_IS\_ENTRY\_RIGHT

    GLCD\_FS\_8BIT\_MODE

    GLCD\_FS\_ROWS\_2

    GLCD\_FS\_ROWS\_1

    GLCD\_FS\_DOT\_SIZE\_BIG

    GLCD\_FS\_DOT\_SIZE\_LITTLE

    GROVE\_RGB\_WHITE

    GROVE\_RGB\_RED

    GROVE\_RGB\_GREEN

    GROVE\_RGB\_BLUE

    Functions

    void glcd\_print(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, char \*data, uint32\_t size)
    :   Send text to the screen.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance.
            - **data** – the ASCII text to display
            - **size** – the length of the text in bytes

    void glcd\_cursor\_pos\_set(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t col, uint8\_t row)
    :   Set text cursor position for next additions.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance.
            - **col** – the column for the cursor to be moved to (0-15)
            - **row** – the row it should be moved to (0 or 1)

    void glcd\_clear(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Clear the current display.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance.

    void glcd\_display\_state\_set(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t opt)
    :   Function to change the display state.

        This function provides the user the ability to change the state of the display as per needed. Controlling things like powering on or off the screen, the option to display the cursor or not, and the ability to blink the cursor.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance.
            - **opt** – An 8bit bitmask of GLCD\_DS\_\* options.

    uint8\_t glcd\_display\_state\_get(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   return the display feature set associated with the device

        Parameters:
        :   - **dev** – the Grove LCD to get the display features set

        Returns:
        :   the display feature set associated with the device.

    void glcd\_input\_state\_set(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t opt)
    :   Function to change the input state.

        This function provides the user the ability to change the state of the text input. Controlling things like text entry from the left or right side, and how far to increment on new text

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance.
            - **opt** – A bitmask of GLCD\_IS\_\* options

    uint8\_t glcd\_input\_state\_get(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   return the input set associated with the device

        Parameters:
        :   - **dev** – the Grove LCD to get the input features set

        Returns:
        :   the input set associated with the device.

    void glcd\_function\_set(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t opt)
    :   Function to set the functional state of the display.

        This function provides the user the ability to change the state of the display as per needed. Controlling things like the number of rows, dot size, and text display quality.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance.
            - **opt** – A bitmask of GLCD\_FS\_\* options

    uint8\_t glcd\_function\_get(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   return the function set associated with the device

        Parameters:
        :   - **dev** – the Grove LCD to get the functions set

        Returns:
        :   the function features set associated with the device.

    void glcd\_color\_select(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t color)
    :   Set LCD background to a predefined color.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance.
            - **color** – One of the predefined color options

    void glcd\_color\_set(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t r, uint8\_t g, uint8\_t b)
    :   Set LCD background to custom RGB color value.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance.
            - **r** – A numeric value for the red color (max is 255)
            - **g** – A numeric value for the green color (max is 255)
            - **b** – A numeric value for the blue color (max is 255)

### BBC micro:bit Display

*group* BBC micro:bit display APIs
:   BBC micro:bit display APIs.

    Defines

    MB\_IMAGE(\_rows...)
    :   Generate an image object from a given array rows/columns.

        This helper takes an array of 5 rows, each consisting of 5 0/1 values which correspond to the columns of that row. The value 0 means the pixel is disabled whereas a 1 means the pixel is enabled.

        The pixels go from left to right and top to bottom, i.e. top-left corner is the first row’s first value, top-right is the first rows last value, and bottom-right corner is the last value of the last (5th) row. As an example, the following would create a smiley face image:

        Parameters:
        :   - **\_rows** – Each of the 5 rows represented as a 5-value column array.

        Returns:
        :   Image bitmap that can be passed e.g. to [mb\_display\_image()](#group__mb__display_1ga2a6e20d57d0d65033281dd7c3ea19126).

    Enums

    enum mb\_display\_mode
    :   Display mode.

        First 16 bits are reserved for modes, last 16 for flags.

        *Values:*

        enumerator MB\_DISPLAY\_MODE\_DEFAULT
        :   Default mode (“single” for images, “scroll” for text).

        enumerator MB\_DISPLAY\_MODE\_SINGLE
        :   Display images sequentially, one at a time.

        enumerator MB\_DISPLAY\_MODE\_SCROLL
        :   Display images by scrolling.

        enumerator MB\_DISPLAY\_FLAG\_LOOP = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(16)
        :   Loop back to the beginning when reaching the last image.

    Functions

    struct mb\_display \*mb\_display\_get(void)
    :   Get a pointer to the BBC micro:bit display object.

        Returns:
        :   Pointer to display object.

    void mb\_display\_image(struct mb\_display \*disp, uint32\_t mode, int32\_t duration, const struct [mb\_image](#c.mb_image) \*img, uint8\_t img\_count)
    :   Display one or more images on the BBC micro:bit LED display.

        This function takes an array of one or more images and renders them sequentially on the micro:bit display. The call is asynchronous, i.e. the processing of the display happens in the background. If there is another image being displayed it will be canceled and the new one takes over.

        Parameters:
        :   - **disp** – Display object.
            - **mode** – One of the MB\_DISPLAY\_MODE\_\* options.
            - **duration** – Duration how long to show each image (in milliseconds), or SYS\_FOREVER\_MS.
            - **img** – Array of image bitmaps (struct [mb\_image](#structmb__image) objects).
            - **img\_count** – Number of images in ‘img’ array.

    void mb\_display\_print(struct mb\_display \*disp, uint32\_t mode, int32\_t duration, const char \*fmt, ...)
    :   Print a string of characters on the BBC micro:bit LED display.

        This function takes a printf-style format string and outputs it in a scrolling fashion to the display.

        The call is asynchronous, i.e. the processing of the display happens in the background. If there is another image or string being displayed it will be canceled and the new one takes over.

        Parameters:
        :   - **disp** – Display object.
            - **mode** – One of the MB\_DISPLAY\_MODE\_\* options.
            - **duration** – Duration how long to show each character (in milliseconds), or SYS\_FOREVER\_MS.
            - **fmt** – printf-style format string
            - **...** – Optional list of format arguments.

    void mb\_display\_stop(struct mb\_display \*disp)
    :   Stop the ongoing display of an image.

        Parameters:
        :   - **disp** – Display object.

    struct mb\_image
    :   *#include <mb\_display.h>*

        Representation of a BBC micro:bit display image.

        This struct should normally not be used directly, rather created using the [MB\_IMAGE()](#group__mb__display_1ga529a5650acaf699b23b4b4234127cf2c) macro.

### Monochrome Character Framebuffer

Related code samples

[Character Framebuffer shell module](../../../samples/subsys/display/cfb_shell/README.md#cfb-shell-sample "Use the CFB shell module to interact with a monochrome display.")
:   Use the CFB shell module to interact with a monochrome display.

[Character frame buffer](../../../samples/subsys/display/cfb/README.md#character-frame-buffer "Display character strings using the Character Frame Buffer (CFB).")
:   Display character strings using the Character Frame Buffer (CFB).

[Custom fonts](../../../samples/subsys/display/cfb_custom_font/README.md#cfb-custom-fonts "Generate and use a custom font.")
:   Generate and use a custom font.

*group* Monochrome Character Framebuffer
:   Public Monochrome Character Framebuffer API.

    Defines

    FONT\_ENTRY\_DEFINE(\_name, \_width, \_height, \_caps, \_data, \_fc, \_lc)
    :   Macro for creating a font entry.

        Parameters:
        :   - **\_name** – Name of the font entry.
            - **\_width** – Width of the font in pixels
            - **\_height** – Height of the font in pixels.
            - **\_caps** – Font capabilities.
            - **\_data** – Raw data of the font.
            - **\_fc** – Character mapped to first font element.
            - **\_lc** – Character mapped to last font element.

    Enums

    enum cfb\_display\_param
    :   *Values:*

        enumerator CFB\_DISPLAY\_HEIGH = 0

        enumerator CFB\_DISPLAY\_WIDTH

        enumerator CFB\_DISPLAY\_PPT

        enumerator CFB\_DISPLAY\_ROWS

        enumerator CFB\_DISPLAY\_COLS

    enum cfb\_font\_caps
    :   *Values:*

        enumerator CFB\_FONT\_MONO\_VPACKED = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(0)

        enumerator CFB\_FONT\_MONO\_HPACKED = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(1)

        enumerator CFB\_FONT\_MSB\_FIRST = [BIT](../../../kernel/util/index.md#c.BIT "BIT")(2)

    Functions

    int cfb\_print(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const char \*const str, uint16\_t x, uint16\_t y)
    :   Print a string into the framebuffer.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance
            - **str** – String to print
            - **x** – Position in X direction of the beginning of the string
            - **y** – Position in Y direction of the beginning of the string

        Returns:
        :   0 on success, negative value otherwise

    int cfb\_draw\_text(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const char \*const str, int16\_t x, int16\_t y)
    :   Print a string into the framebuffer.

        For compare to cfb\_print, cfb\_draw\_text accept non tile-aligned coords and not line wrapping.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance
            - **str** – String to print
            - **x** – Position in X direction of the beginning of the string
            - **y** – Position in Y direction of the beginning of the string

        Returns:
        :   0 on success, negative value otherwise

    int cfb\_draw\_point(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const struct [cfb\_position](#c.cfb_position) \*pos)
    :   Draw a point.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance
            - **pos** – position of the point

        Returns:
        :   0 on success, negative value otherwise

    int cfb\_draw\_line(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const struct [cfb\_position](#c.cfb_position) \*start, const struct [cfb\_position](#c.cfb_position) \*end)
    :   Draw a line.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance
            - **start** – start position of the line
            - **end** – end position of the line

        Returns:
        :   0 on success, negative value otherwise

    int cfb\_draw\_rect(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const struct [cfb\_position](#c.cfb_position) \*start, const struct [cfb\_position](#c.cfb_position) \*end)
    :   Draw a rectangle.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance
            - **start** – Top-Left position of the rectangle
            - **end** – Bottom-Right position of the rectangle

        Returns:
        :   0 on success, negative value otherwise

    int cfb\_framebuffer\_clear(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, bool clear\_display)
    :   Clear framebuffer.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance
            - **clear\_display** – Clear the display as well

        Returns:
        :   0 on success, negative value otherwise

    int cfb\_framebuffer\_invert(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Invert Pixels.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance

        Returns:
        :   0 on success, negative value otherwise

    int cfb\_invert\_area(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint16\_t x, uint16\_t y, uint16\_t width, uint16\_t height)
    :   Invert Pixels in selected area.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance
            - **x** – Position in X direction of the beginning of area
            - **y** – Position in Y direction of the beginning of area
            - **width** – Width of area in pixels
            - **height** – Height of area in pixels

        Returns:
        :   0 on success, negative value otherwise

    int cfb\_framebuffer\_finalize(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Finalize framebuffer and write it to display RAM, invert or reorder pixels if necessary.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance

        Returns:
        :   0 on success, negative value otherwise

    int cfb\_get\_display\_parameter(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [cfb\_display\_param](#c.cfb_display_param))
    :   Get display parameter.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance
            - **cfb\_display\_param** – One of the display parameters

        Returns:
        :   Display parameter value

    int cfb\_framebuffer\_set\_font(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t idx)
    :   Set font.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance
            - **idx** – Font index

        Returns:
        :   0 on success, negative value otherwise

    int cfb\_set\_kerning(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, int8\_t kerning)
    :   Set font kerning (spacing between individual letters).

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance
            - **kerning** – Font kerning

        Returns:
        :   0 on success, negative value otherwise

    int cfb\_get\_font\_size(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, uint8\_t idx, uint8\_t \*width, uint8\_t \*height)
    :   Get font size.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance
            - **idx** – Font index
            - **width** – Pointers to the variable where the font width will be stored.
            - **height** – Pointers to the variable where the font height will be stored.

        Returns:
        :   0 on success, negative value otherwise

    int cfb\_get\_numof\_fonts(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get number of fonts.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance

        Returns:
        :   number of fonts

    int cfb\_framebuffer\_init(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Initialize Character Framebuffer.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance

        Returns:
        :   0 on success, negative value otherwise

    void cfb\_framebuffer\_deinit(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Deinitialize Character Framebuffer.

        Parameters:
        :   - **dev** – Pointer to device structure for driver instance

    struct cfb\_font
    :   *#include <cfb.h>*

    struct cfb\_position
    :   *#include <cfb.h>*
