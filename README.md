# bashprint
Python script to use colors and text formatting in (bash) terminal output

This script consists of two classes. [Template](#template) and [Tools](#tools)
# Template:
This class allows you to create an object where you can specify a color and other attributes. If you later call this object with a string, that string will be returned and the specified attributes will be applied.

The default is:
```python
foreground=False,background=False,bold=False,dim=False,underlined=False,blink=False,hidden=False
```
foreground and background, expect a number between 0 and 255.
What number maps to what color can be shown with [Tools.color_palate()](#color_palate)

bold, dim, underlined, blink and hidden can be set to True

This is an example use case: 
```python
from bashprint import Template,Tools

highlighted = Template(background=11,underlined=True,bold=True,foreground=16)

text = 'This is normal, ' + highlighted('this is highlighted') + ' and this again is not!'

Tools.bashprint(text)
```
The output of should look something like this:

![image](https://user-images.githubusercontent.com/81306399/180852738-c9024a16-e68d-46d9-86bc-ee18d97ed8ec.png)


Not all attributes are supported by all terminal emulators.

# Tools:
## bashprint:
This function is an alternative to the integrated print function that uses bash and therefore supports the used formatting.

Up until now, I exclusively tested this on Linux (Pop-OS). If this results in issues on other operating systems, there is a chance I will update this function accordingly. 

## color_palate:

Calling this function echos the color palette with all available colors and the corresponding numbers. 

The output should look something like this:

![image](https://user-images.githubusercontent.com/81306399/180854560-dda9569a-e40e-4f4e-81fd-5c8b3b7f6415.png)

And again this will look slightly different on other terminal emulators.
