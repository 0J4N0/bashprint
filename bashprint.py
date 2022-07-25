import subprocess

class Template:
    '''
    This class allows you to create an object where you can specify a color and other attributes. 
    If you later call this object with a string,
    that string will be returned and the specified attributes will be applied.

    foreground and background, expect a number between 0 and 255. What number maps to what color can be shown with Tools.color_palate()
    
    bold, dim, underlined, blink and hidden can be set to True

    '''
    def __init__(self,foreground=False,background=False,bold=False,dim=False,underlined=False,blink=False,hidden=False):
        self.foreground = foreground
        self.background = background
        self.bold = bold
        self.dim = dim
        self.underlined = underlined
        self.blink = blink
        self.hidden = hidden
    
    def __call__(self,text:str)->str:
        out = f'\\e[48;5;{self.background}m' if self.background else f'\\e[49m'
        if self.bold: out += '\\e[1m'
        if self.dim: out += '\\e[2m'
        if self.underlined: out += '\\e[4m'
        if self.blink: out += '\\e[5m'
        if self.hidden: out += '\\e[8m'
        out += f'\\e[38;5;{self.foreground}m' if self.foreground else f'\\e[39m'
        out += f'{text}'
        out += '\\e[0m'
        return out 

class Tools:
    def bashprint(text:str)->None:
        """
        This function is an alternative to the integrated print function that uses bash and therefore supports the used formatting.
        """
        subprocess.call(["bash","-c",f'echo -e "{text}"'])
    
    def color_palate()->None:
        """
        Calling this function echos the color palette with all available colors and the corresponding numbers. 
        """
        out = '\\n'
        count = 0
        for i in range(16):
            for j in range(16):
                out += Template(foreground=f'{(i*16) + j}')(f'{(i*16) + j}'.zfill(3)) + ' '
            out += '\\n'
            for j in range(16):
                out += Template(background=f'{(i*16) + j}')('   ') + ' '
            out += '\\n'
            if i%16 == 0: out += '\\n'
        Tools.bashprint(out)
    
