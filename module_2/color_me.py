#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:MC.Lee
# 高级版colorme，兼容windows,用法示例在模块底部
# python3.6
#----------------------------
# 写的稍微复杂，为了展示一些用法，希望同学积极重构，更简单易用
# 知识点：
# 1、字符串查找、切片、替换、处理 列表 字典
# 2、类的动态方法，动态属性 反射 ，关系（关联继承）
# 3、函数的参数 返回值
# 4、魔术方法__getattr__
# 5、类的私有方法
# 6、stdout标准输出 



import sys
import ctypes


class ColorMe(object):
    def __init__(self):
        self.colorController = self.default_style()
        self.foreColor,self.backColor = self.__colorList()
        
    
    def default_style(self):
        if 'win' in sys.platform:
            colorController = WinClolorStyle()
        else:
            colorController = LinuxColorStyle()
        return colorController

    def __colorList(self):
        foreground = []
        background = []
        for key in self.colorController.__dict__:
            if 'FOREGROUND' in key:
                foreground.append((key.replace("FOREGROUND_","")).lower())
            if 'BACKGROUND' in key:
                background.append((key.replace("BACKGROUND_","")).lower())
        return foreground,background

    def __getattr__(self,method):
        func = self.__selectMethod(method)
        return func
    
    def __selectMethod(self,method):
        method = method.lower()
        color = self.__findColorInMethod(method)
        color.insert(0,'print')
        func_name = ''.join(color)
        func = getattr(self.colorController,func_name)
        return func
    
    def __reUpper(self,color_list):
        if len(color_list) == 0:
            raise Exception(f"{self.__class__.__name__}没有此方法", AttributeError)
        else:
            keys = ['Dark','Sky']
            colors = []
            for color in color_list:
                for key in keys:
                    index = color.find(key.lower())
                    if index == 0 and len(key) < len(color):
                        color = color.replace(key.lower(),"")
                        color = f'{key}{color[0].upper()}{color[1:]}'
                    else:
                        color = f'{color[0].upper()}{color[1:]}'
                colors.append(color)
        return colors

    def __findColorInMethod(self,method):
        method = method.replace('print',"")
        findColor = []
        for color in self.foreColor:
            index = method.find(color)
            if index == 0 and len(color) <= len(method):
                findColor.append(color)
                method = method.replace(color,"")
                if len(method) == 0:
                    return self.__reUpper(findColor)
                else:
                    continue
        return self.__reUpper(findColor)
    

    def __parseColorArgs(self,color_args):
        '''
        @color_args 颜色设置元组(fgcolor,bgcolor,show_style)fgcolor前景颜色即字体颜色；bgroundcolor 背景颜色,默认None,缺省设置； show_style 显示格式,默认None,高亮显示
        '''
        if isinstance(color_args,tuple):
            if len(color_args) == 3:
                fgcolor = self.__changeArgsToValue(color_args[0],'fore')
                bgcolor = self.__changeArgsToValue(color_args[1],'back')
                show_style = self.__changeArgsToValue(color_args[2],'showtype')
            elif len(color_args) == 2:
                fgcolor = self.__changeArgsToValue(color_args[0],'fore')
                bgcolor = self.__changeArgsToValue(color_args[1],'back')
                show_style = None
            elif len(color_args) == 1:
                fgcolor = self.__changeArgsToValue(color_args[0],'fore')
                bgcolor = None
                show_style = None
            else:
                raise Exception('颜色参数错误！')
        elif isinstance(color_args,str):
            fgcolor = self.__changeArgsToValue(color_args,'fore')
            bgcolor = None
            show_style = None
        else:
            raise Exception('颜色参数错误！')
        return fgcolor ,bgcolor ,show_style
    
    def __changeArgsToValue(self,arg,arg_type):
        agrs_dict = {}
        res = None
        prefix = ''
        if arg_type == 'fore':
            for key in self.colorController.__dict__:
                if 'FOREGROUND' in key:
                    agrs_dict[key]=self.colorController.__dict__[key]
                    prefix = 'FOREGROUND_'
        elif arg_type == 'back':
            for key in self.colorController.__dict__:
                if 'BACKGROUND' in key:
                    agrs_dict[key]=self.colorController.__dict__[key]
                    prefix = 'BACKGROUND_'
        elif arg_type == 'showtype':
            for key in self.colorController.__dict__:
                if 'BACKGROUND' not in key and 'FOREGROUND' not in key:
                    agrs_dict[key]=self.colorController.__dict__[key]
                    prefix = ''
        else:
            raise Exception("颜色参数类型错误")
        ####
        if arg:
            arg = arg.upper()
            for key,value in agrs_dict.items():
                if f'{prefix}{arg}' == key:
                    res = value
                    break
        else:
            res = None
        return res
        

    def colorTXT(self,msg,color):
        '''
        设置字体颜色
        @msg 要设置的字符串,string
        @color 颜色设置元组(fgcolor,bgcolor,show_style)fgcolor前景颜色即字体颜色 bgcolor 背景颜色,默认None show_style 显示格式,默认None,高亮显示 
        @color String或tuple ,string时为只设置前景色，值为颜色名称
        '''
        method = getattr(self.colorController,"colorTXT")
        fgcolor,bgcolor,show_style = self.__parseColorArgs(color)
        method(str(msg),fgcolor,bgcolor,show_style)


class LinuxColorStyle:
    def __init__(self):
        self.RESET = "\033[0m"
        self.LIGHT = "\033[1;"
        self.BLOD = "\033[2;"
        self.UNDERLINR = "\033[4;"
        self.BLINK = "\033[5;"
        # 前景色
        self.FOREGROUND_BLACK = "30;"
        self.FOREGROUND_RED = "31;"
        self.FOREGROUND_GREEN = "32;"
        self.FOREGROUND_YELLOW = "33;"
        self.FOREGROUND_BLUE = "34;"
        self.FOREGROUND_PURPLE = "35;"
        self.FOREGROUND_CYAN = "36;"
        self.FOREGROUND_WHITE = "37;"
        # 背景色
        self.BACKGROUND_DEFAULT = "1m;"
        self.BACKGROUND_BLACK = "40m"
        self.BACKGROUND_RED = "41m"
        self.BACKGROUND_GREEN = "42m"
        self.BACKGROUND_YELLOW = "43m"
        self.BACKGROUND_BLUE = "44m"
        self.BACKGROUND_PURPLE = "45m"
        self.BACKGROUND_CYAN = "46m"
        self.BACKGROUND_WHITE = "47m"

    def __colorMsg(self,show_style,foregound_color,background_color,msg):
        msg = f"{show_style}{foregound_color}{background_color}{msg}{self.RESET}"
        return msg
    
    def colorTXT(self,msg,fgcolor,bgcolor,show_style):
        '''
        颜色字体函数
        @return 返回linux控制台颜色代码包裹的字符串
        @msg 需要改变颜色的文字，string
        @fgcolor前景颜色即字体颜色
        @bgcolor 背景颜色,默认None
        @show_style 显示格式,默认None,高亮显示    
        '''
        show_style,background_color = self.__defaultStyle(show_style,bgcolor)
        msg = self.__colorMsg(show_style,fgcolor,bgcolor,msg)
        self.__showMsg(msg)

    
    def __showMsg(self,msg):
        sys.stdout.write(msg)
        sys.stdout.flush()

    def __defaultStyle(self,show_style=None,background_color=None):
        '''
        设置默认的显示格式和背景色
        @show_style 显示格式
        '''
        if show_style is None:
            show_style = self.LIGHT
        if background_color is None:
            background_color = self.BACKGROUND_DEFAULT
        return show_style,background_color

    def printBlue(self,msg):
        show_style,background_color = self.__defaultStyle()
        msg = self.__colorMsg(show_style,self.FOREGROUND_BLUE,background_color,msg)
        self.__showMsg(msg)

    def printRed(self,msg):
        show_style,background_color = self.__defaultStyle()
        msg = self.__colorMsg(show_style,self.FOREGROUND_RED,background_color,msg)
        self.__showMsg(msg)

    def printGreen(self,msg):
        show_style,background_color = self.__defaultStyle()
        msg = self.__colorMsg(show_style,self.FOREGROUND_GREEN,background_color,msg)
        self.__showMsg(msg)

    def printBlack(self,msg):
        show_style,background_color = self.__defaultStyle()
        msg = self.__colorMsg(show_style,self.FOREGROUND_BLACK,self.BACKGROUND_WHITE,msg)
        self.__showMsg(msg)

    def printWhite(self,msg):
        show_style,background_color = self.__defaultStyle()
        msg = self.__colorMsg(show_style,self.FOREGROUND_WHITE,background_color,msg)
        self.__showMsg(msg)

    def printYellow(self,msg):
        show_style,background_color = self.__defaultStyle()
        msg = self.__colorMsg(show_style,self.FOREGROUND_YELLOW,background_color,msg)
        self.__showMsg(msg)

    def printPurple(self,msg):
        show_style,background_color = self.__defaultStyle()
        msg = self.__colorMsg(show_style,self.FOREGROUND_PURPLE,background_color,msg)
        self.__showMsg(msg)

    def printCyan(self,msg):
        show_style,background_color = self.__defaultStyle()
        msg = self.__colorMsg(show_style,self.FOREGROUND_CYAN,background_color,msg)
        self.__showMsg(msg)



class WinClolorStyle:
    def __init__(self):
        self.FOREGROUND_BLACK = 0x00 # black.
        self.FOREGROUND_DARKBLUE = 0x01 # dark blue.
        self.FOREGROUND_DARKGREEN = 0x02 # dark green.
        self.FOREGROUND_DARKSKYBLUE = 0x03 # dark skyblue.
        self.FOREGROUND_DARKRED = 0x04 # dark red.
        self.FOREGROUND_DARKPINK = 0x05 # dark pink.
        self.FOREGROUND_DARKYELLOW = 0x06 # dark yellow.
        self.FOREGROUND_DARKWHITE = 0x07 # dark white.
        self.FOREGROUND_DARKGRAY = 0x08 # dark gray.
        self.FOREGROUND_BLUE = 0x09 # blue.
        self.FOREGROUND_GREEN = 0x0a # green.
        self.FOREGROUND_SKYBLUE = 0x0b # skyblue.
        self.FOREGROUND_RED = 0x0c # red.
        self.FOREGROUND_PINK = 0x0d # pink.
        self.FOREGROUND_YELLOW = 0x0e # yellow.
        self.FOREGROUND_WHITE = 0x0f # white.
        self.FOREGROUND_INTENSITY = 8 # 前景高亮
        # Windows CMD命令行 背景颜色定义 background colors
        self.BACKGROUND_DARKBLUE = 0x10 # dark blue.
        self.BACKGROUND_DARKGREEN = 0x20 # dark green.
        self.BACKGROUND_DARKSKYBLUE = 0x30 # dark skyblue.
        self.BACKGROUND_DARKRED = 0x40 # dark red.
        self.BACKGROUND_DARKPINK = 0x50 # dark pink.
        self.BACKGROUND_DARKYELLOW = 0x60 # dark yellow.
        self.BACKGROUND_DARKWHITE = 0x70 # dark white.
        self.BACKGROUND_DARKGRAY = 0x80 # dark gray.
        self.BACKGROUND_BLUE = 0x90 # blue.
        self.BACKGROUND_GREEN = 0xa0 # green.
        self.BACKGROUND_SKYBLUE = 0xb0 # skyblue.
        self.BACKGROUND_RED = 0xc0 # red.
        self.BACKGROUND_PINK = 0xd0 # pink.
        self.BACKGROUND_YELLOW = 0xe0 # yellow.
        self.BACKGROUND_WHITE = 0xf0 # white.
        self.BACKGROUND_INTENSITY = 128
        # 标准输出句柄
        STD_INPUT_HANDLE = -10
        STD_OUTPUT_HANDLE = -11
        STD_ERROR_HANDLE = -12
        self.std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

    def set_cmd_text_color(self,color):
        handle = self.std_out_handle
        Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
        return Bool

    def resetColor(self):
        self.set_cmd_text_color(self.FOREGROUND_RED | self.FOREGROUND_GREEN | self.FOREGROUND_BLUE)


    def colorTXT(self,msg,fgcolor,bgcolor,show_style):
        fgcolor = 0 if fgcolor is None else fgcolor
        bgcolor = 0 if bgcolor is None else bgcolor
        self.set_cmd_text_color(fgcolor | bgcolor)
        sys.stdout.write(msg)
        sys.stdout.flush()
        self.resetColor()

    #暗蓝色
    #dark blue
    def printDarkBlue(self,msg):
        self.set_cmd_text_color(self.FOREGROUND_DARKBLUE)
        sys.stdout.write(msg)
        sys.stdout.flush()
        self.resetColor()

    #暗绿色
    #dark green
    def printDarkGreen(self,msg):
        self.set_cmd_text_color(self.FOREGROUND_DARKGREEN)
        sys.stdout.write(msg)
        sys.stdout.flush()
        self.resetColor()

    #暗天蓝色
    #dark sky blue
    def printDarkSkyBlue(self,msg):
        self.set_cmd_text_color(self.FOREGROUND_DARKSKYBLUE)
        sys.stdout.write(msg)
        sys.stdout.flush()
        self.resetColor()

    #暗红色
    #dark red
    def printDarkRed(self,msg):
        self.set_cmd_text_color(self.FOREGROUND_DARKRED)
        sys.stdout.write(msg)
        sys.stdout.flush()
        self.resetColor()

    #暗粉红色
    #dark pink
    def printDarkPink(self,msg):
        self.set_cmd_text_color(self.FOREGROUND_DARKPINK)
        sys.stdout.write(self,msg)
        sys.stdout.flush()
        self.resetColor()

    #暗黄色
    #dark yellow
    def printDarkYellow(self,msg):
        self.set_cmd_text_color(self.FOREGROUND_DARKYELLOW)
        sys.stdout.write(msg)
        sys.stdout.flush()
        self.resetColor()

    #暗白色
    #dark white
    def printDarkWhite(self,msg):
        self.set_cmd_text_color(self.FOREGROUND_DARKWHITE)
        sys.stdout.write(msg)
        sys.stdout.flush()
        self.resetColor()

    #暗灰色
    #dark gray
    def printDarkGray(self,msg):
        self.set_cmd_text_color(self.FOREGROUND_DARKGRAY)
        sys.stdout.write(msg)
        sys.stdout.flush()
        self.resetColor()

    #蓝色
    #blue
    def printBlue(self,msg):
        self.set_cmd_text_color(self.FOREGROUND_BLUE)
        sys.stdout.write(msg)
        sys.stdout.flush()
        self.resetColor()

    #绿色
    #green
    def printGreen(self,msg):
        self.set_cmd_text_color(self.FOREGROUND_GREEN)
        sys.stdout.write(msg)
        sys.stdout.flush()
        self.resetColor()

    #天蓝色
    #sky blue
    def printSkyBlue(self,msg):
        self.set_cmd_text_color(self.FOREGROUND_SKYBLUE)
        sys.stdout.write(msg)
        sys.stdout.flush()
        self.resetColor()

    #红色
    #red
    def printRed(self,msg):
        self.set_cmd_text_color(self.FOREGROUND_RED)
        sys.stdout.write(msg)
        sys.stdout.flush()
        self.resetColor()

    #粉红色
    #pink
    def printPink(self,msg):
        self.set_cmd_text_color(self.FOREGROUND_PINK)
        sys.stdout.write(msg)
        sys.stdout.flush()
        self.resetColor()

    #黄色
    #yellow
    def printYellow(self,msg):
        self.set_cmd_text_color(self.FOREGROUND_YELLOW)
        sys.stdout.write(msg)
        sys.stdout.flush()
        self.resetColor()

    #白色
    #white
    def printWhite(self,msg):
        self.set_cmd_text_color(self.FOREGROUND_WHITE)
        sys.stdout.write(msg)
        sys.stdout.flush()
        self.resetColor()


if __name__ == "__main__":
    # ColorMe()
    a = "颜色"
    # ColorMe().colorTXT("颜色","Blue")
    # ColorMe().printBlue("yans")
    # print(LinuxColorStyle().__dict__)
    # ColorMe().aaa("sdad")
    ColorMe().printdarkblue("颜色显示")
    ColorMe().pink("来个粉色")
    ColorMe().colorTXT('我是蓝字黄底',('blue','yellow'))
    ColorMe().colorTXT('我是红字','red')
    

    