# CMD & Powershell notes

## Find environment variables values

use the `set` command and you'll get an output like so:

```cmd
C:\Users\HP>set
PROMPT=$P$G
__COMPAT_LAYER=DetectorsAppHealth
ALLUSERSPROFILE=C:\ProgramData
APPDATA=C:\Users\HP\AppData\Roaming
COLORTERM=truecolor
CommonProgramFiles=C:\Program Files\Common Files
CommonProgramFiles(x86)=C:\Program Files (x86)\Common Files
CommonProgramW6432=C:\Program Files\Common Files
COMPUTERNAME=DESKTOP-MJ9GB9T
ComSpec=C:\Windows\system32\cmd.exe
DriverData=C:\Windows\System32\Drivers\DriverData
FPS_BROWSER_APP_PROFILE_STRING=Internet Explorer
FPS_BROWSER_USER_PROFILE_STRING=Default
HOMEDRIVE=C:
HOMEPATH=\Users\HP
IntelliJ IDEA Community Edition=C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2024.3.5\bin;
JD2_HOME=C:\Users\HP\AppData\Local\JDownloader 2
LOCALAPPDATA=C:\Users\HP\AppData\Local
LOGONSERVER=\\DESKTOP-MJ9GB9T
NUMBER_OF_PROCESSORS=4
OneDrive=C:\Users\HP\OneDrive
OS=Windows_NT
Path=C:\Program Files\Common Files\Oracle\Java\javapath;C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Program Files\Git\cmd;C:\Program Files\nodejs\;C:\Program Files\WezTerm;;C:\Ruby32-x64\bin;C:\Users\HP\AppData\Local\Programs\Python\Python310\Scripts\;C:\Users\HP\AppData\Local\Programs\Python\Python310\;C:\Users\HP\AppData\Local\Microsoft\WindowsApps;D:\DOWNLOADS\Compressed\OneCommander3.14.1.0;C:\Program Files\AtomicParsleyWindows\Release\;C:\Users\HP\AppData\Local\Programs\Neovim\bin;C:\Program Files (x86)\Java\jre1.8.0_361\bin;C:\Program Files\Java\jdk-20\bin;C:\Program Files\Git\bin;C:\Program Files\apache-maven-3.9.1\bin;D:\DOWNLOADS\Programs\fd-v8.7.0-i686-pc-windows-msvc\;C:\Users\HP\AppData\Local\Microsoft\WinGet\Packages\Helix.Helix_Microsoft.Winget.Source_8wekyb3d8bbwe\helix-23.05-x86_64-windows\;D:\DOWNLOADS\Programs\yt-dlp.exe;C:\Users\HP\AppData\Local\Microsoft\WinGet\Packages\ajeetdsouza.zoxide_Microsoft.Winget.Source_8wekyb3d8bbwe;C:\Users\HP\emacs-29.3\bin;C:\MinGW\bin;C:\Program Files\JetBrains\IntelliJ IDEA Community Edition 2024.3.5\bin;;C:\Users\HP\lazygit_0.49.0_Windows_x86_64;C:\Program Files\PostgreSQL\17\bin;C:\Users\HP\marksman;C:\Users\HP\AppData\Roaming\npm;C:\Users\HP\AppData\Local\Programs\Microsoft VS Code\bin
PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.RB;.RBW;.RB;.RBW
PROCESSOR_ARCHITECTURE=AMD64
PROCESSOR_IDENTIFIER=Intel64 Family 6 Model 142 Stepping 9, GenuineIntel
PROCESSOR_LEVEL=6
PROCESSOR_REVISION=8e09
ProgramData=C:\ProgramData
ProgramFiles=C:\Program Files
ProgramFiles(x86)=C:\Program Files (x86)
ProgramW6432=C:\Program Files
PSModulePath=C:\Program Files\WindowsPowerShell\Modules;C:\Windows\system32\WindowsPowerShell\v1.0\Modules
PUBLIC=C:\Users\Public
SESSIONNAME=Console
SystemDrive=C:
SystemRoot=C:\Windows
TEMP=C:\Users\HP\AppData\Local\Temp
TERM=xterm-256color
TERM_PROGRAM=WezTerm
TERM_PROGRAM_VERSION=20240203-110809-5046fc22
TMP=C:\Users\HP\AppData\Local\Temp
USERDOMAIN=DESKTOP-MJ9GB9T
USERDOMAIN_ROAMINGPROFILE=DESKTOP-MJ9GB9T
USERNAME=HP
USERPROFILE=C:\Users\HP
WEZTERM_EXECUTABLE=C:\Program Files\WezTerm\wezterm-gui.exe
WEZTERM_EXECUTABLE_DIR=C:\Program Files\WezTerm
WEZTERM_PANE=0
WEZTERM_UNIX_SOCKET=C:\Users\HP\.local/share/wezterm\gui-sock-10232
windir=C:\Windows
WSLENV=TERM:COLORTERM:TERM_PROGRAM:TERM_PROGRAM_VERSION
ZES_ENABLE_SYSMAN=1
```

