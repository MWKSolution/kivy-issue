# Kivy + PyInstaller + Windows issue  

---  

After packaging Kivy application for Windows using PyInstaller ***Unable to get a Window, abort.*** error could apper.  
When console is activated for window application log would look something like this:  

```
[DEBUG  ] [ImageSDL2   ] Load <C:\...\default.png>
[WARNING] [Image       ] Unable to load image <C:\...\default.png>
[CRITICAL] [Window      ] Unable to find any valuable Window provider. Please enable debug logging  
                          (e.g. add -d if running from the command line, or change the log level in the config)  
                           and re-run your app to identify potential causes
sdl2 - Exception: SDL2: Unable to load image
  File "c:\...\venv\lib\site-packages\kivy\core\__init__.py", line 71, in core_select_lib
    cls = cls()
  File "c:\...\venv\lib\site-packages\kivy\core\window\window_sdl2.py", line 165, in __init__
    super(WindowSDL, self).__init__()
  File "c:\...\venv\lib\site-packages\kivy\core\window\__init__.py", line 1071, in __init__
    self.create_window()
  File "c:\...\venv\lib\site-packages\kivy\core\window\window_sdl2.py", line 362, in create_window
    super(WindowSDL, self).create_window()
  File "c:\...\venv\lib\site-packages\kivy\core\window\__init__.py", line 1450, in create_window
    self.render_context = RenderContext()
  File "kivy\graphics\instructions.pyx", line 797, in kivy.graphics.instructions.RenderContext.__init__
  File "c:\...\venv\lib\site-packages\kivy\core\image\__init__.py", line 561, in __init__
    self.filename = arg
  File "c:\...\venv\lib\site-packages\kivy\core\image\__init__.py", line 754, in _set_filename
    image = ImageLoader.load(
  File "c:\...\venv\lib\site-packages\kivy\core\image\__init__.py", line 460, in load
    im = loader(filename, **kwargs)
  File "c:\...\venv\lib\site-packages\kivy\core\image\__init__.py", line 223, in __init__
    self._data = self.load(filename)
  File "c:\...\venv\lib\site-packages\kivy\core\image\img_sdl2.py", line 47, in load
    raise Exception('SDL2: Unable to load image')

 import 'kivy.core.window' # <_frozen_importlib_external.SourcelessFileLoader object at 0x0000000003BB4D00>
[CRITICAL] [App         ] Unable to get a Window, abort.
```
The problem is that PyInstaller don't include two DLL files into package:  
```
libpng16-16.dll
zlib1.dll
```
They should be added manually to the package for exe file to run properly. They are in ***\venv\share\sdl2\bin*** of current project.  
Copy them *(for example)* to ***\dlls***, and add line in ***main.spec*** file in ***Analysis*** class:  
```
binaries=[('dlls/libpng16-16.dll', '.'), ('dlls/zlib1.dll', '.')],
```  
Then run  
```
pyinstaller main.spec
```
This time application should work.