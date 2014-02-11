# PyYad is a library that binds Python and YAD
# For more info visit www.python.org, code.google.com/p/yad and www.loc4n.com
# PyYad is developed by Artur 'hoOmE' Paiva <dr.hoome@gmail.com> at www.loc4n.com
# PyYad is under GPLv3 - http://www.gnu.org/licenses/gpl.html
#

# String that save the version of PyYad
pyversion="0.1.2 Alpha"

# Print versions information
def version():
    from sys import version_info
    from subprocess import check_output
    from locale import getdefaultlocale
    yad=check_output(["yad","--version"]).splitlines()[0]
    encoding = getdefaultlocale()[1]
    yad = yad.decode(encoding)
    return("PyYad Version: %s\nPython Version: %d.%d.%d\nYAD Version: %s" % (pyversion,version_info[0],version_info[1],version_info[2],yad))

# Check if YAD is installed
def checkyad():
    from os import system
    if system("yad --version > /dev/null") != 0:
        returned = False
    else:
        returned = True
    return(returned)

# Check if python is new (2.7 or newest)
def checkpython():
    from sys import version_info
    if version_info < (2,7):
        returned = False
    else:
        returned = True
    return(returned)

class yad:
    yadwindow="yad "
    title="Apolo" # Title of YAD Window
    wicon="" # Window Icon
    width=300 # Window Width
    height=150 # Window Height
    geometry=None # Array with (w,h,x and y)
    text="" # Text inside the YAD window
    textAlign=None # Text alignment (center,left,right or fill)
    image="stock_media_play"   # Add a image
    imgOnTop=False # Add the image on top
    buttonlist= ["Oka:int(2)"] # Array list with buttons
    buttons=True # Enable Buttons (true/false)
    markup=True # Enable markup (true/false)
    borders=0 # Add borders to window
    alwaysPrintResult=False # Always print Result (true/false)
    selectableLabels=False # Selectable Labels (true/false)
    sticky=False # sticky window (true/false)
    fixed=False # fixed window (true/false)
    onTop=True # Window on top of others (true/false)
    center=True # window on center of desktop (true/false)
    mouse=False # window on mouse position (true/false)
    decoration=True # window decoration (true/false)
    taskbar=True # show window on taskbar
    killParent=None # kill PID together when closing window
    printXid=False # print window xid
    sync=False # make X calls synchronous
    display=None # set X display to show window

    # Start YAD class
    def __init__(self):
        from os import system
        if system("yad --version > /dev/null") != 0:
            print("Missing YAD on your system or your YAD version is too old!")


    # Generate a form dialog
    def form(self,fields=None,align="left",columns=1,separator=None,iseparator=None,scroll=False):
        if fields != None:
            for field in fields:
                self.yadwindow+="--field=\"%s\" " % field
        self.yadwindow+="--align=\"%s\" " % align
        self.yadwindow+="--columns=%d " % columns
        if sepatator != None:
            self.yadwindow+="--separator=\"%s\" " % separator
        if isepatator != None:
            self.yadwindow+="--item-separator=\"%s\" " % iseparator
        if scroll == True:
            self.yadwindow+="--scroll "

    # Generate the YAD code
    def __build(self):
        self.yadwindow+="--title=\"%s\" " % self.title
        self.yadwindow+="--window-icon=\"%s\" " % self.wicon
        self.yadwindow+="--width=%d " % self.width
        self.yadwindow+="--height=%d " % self.height
        self.yadwindow+="--text=\"%s\" " % self.text
        self.yadwindow+="--borders=%d " % self.borders
        if self.geometry != None:
            self.yadwindow+="--geometry=\"%dx%d+%d+%d\" " % self.geometry
        if self.textAlign != None:
            self.yadwindow+="--text-align=\"%s\" " % self.textAlign
        if self.image != None:
            self.yadwindow+="--image=\"%s\" " % self.image
        if self.imgOnTop == True:
            self.yadwindow+="--image-on-top "
        if self.buttonlist != None:
            if type(self.buttonlist[0]) == str:
                self.yadwindow+="--button=\"%s:%d\" " % self.buttonlist
            else:
                for item in self.buttonlist:
                    self.yadwindow+="--button=\"%s:%d\" " % item
        if self.buttons == False:
            self.yadwindow+="--no-buttons "
        if self.markup == False:
            self.yadwindow+="--no-markup "
        if self.alwaysPrintResult == True:
            self.yadwindow+="--arways-print-result "
        if self.selectableLabels == True:
            self.yadwindow+="--selectable-labels "
        if self.sticky == True:
            self.yadwindow+="--sticky "
        if self.fixed == True:
            self.yadwindow+="--fixed "
        if self.onTop == True:
            self.yadwindow+="--on-top "
        if self.center == True:
            self.yadwindow+="--center "
        if self.mouse == True:
            self.yadwindow+="--mouse "
        if self.decoration == False:
            self.yadwindow+="--undecorated "
        if self.taskbar == False:
            self.yadwindow+="--skip-taskbar "
        if self.killParent != None:
            self.yadwindow+="--kill-parent=%d " % self.killParent
        if self.printXid == True:
            self.yadwindow+="--print-xid "
        if self.sync == True:
            self.yadwindow+="--sync "
        if self.display != None:
            self.yadwindow+="--display=%s " % self.display

    # Show a YAD window
    def show(self):
        self.__build()
        from subprocess import check_output
        self.yadwindow+=" ;echo $?"
        from locale import getdefaultlocale
        encoding = getdefaultlocale()[1]
        result = check_output(self.yadwindow,shell=True).decode(encoding)
        return(result.splitlines())

    # Show YAD window code
    def code(self):
        self.__build()
        return(self.yadwindow)

    # Clean YAD
    def clean(self):
        self.yadwindow="yad "
