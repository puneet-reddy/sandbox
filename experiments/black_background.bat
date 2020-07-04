
REM Hack to force the background to black instead of the random
REM colorful nonsense that's forced on us
cd "C:\Users\css112720\AppData\Roaming\Microsoft\Windows\Themes"
del /s /Q *

REM Below line forces the background to refresh.
RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters 1, True