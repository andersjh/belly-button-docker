# Belly Button Homework "Dockerized"

Docker is very important in the current job market.  This brief introduction is meant as a "bootcamp" (i.e. not "gentle") introduction to what Docker brings to the table.  The main focus is on Windows as Docker on Mac / Linux is much more straight forward.

## Lots Exciting Changes in the Windows Ecosystem!

### WSL2 - True Linux Kernel Running in Windows:

[WSL 2 and Docker](https://www.youtube.com/watch?v=5RQbdMn04Oc)

[Install WSL2 on Windows](https://docs.microsoft.com/en-us/windows/wsl/install-win10)'

Docker is really meant to work with Windows 10 Professional and NOT Windows 10 Home.  If your are going to do a lot of Windows work, I would consider spending the $100 to upgrade to Windows Pro.

The following "trick" may or may not work but could save you $100 if you don't have Windows Professional.

Do the following:
- Start Windows Powershell as Admininstrator
- cd into c:\windows\system32
- create a vir.bat file with the following code and then run it:
```
pushd "%~dp0"
dir /b %SystemRoot%\servicing\Packages\*Hyper-V*.mum >hyper-v.txt
for /f %%i in ('findstr /i . hyper-v.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i"
del hyper-v.txt
Dism /online /enable-feature /featurename:Microsoft-Hyper-V -All /LimitAccess /ALL
pause
```
- reboot
- confirm / enable required features by:
-- "Turn Windows Features On Off" and make sure the following are on:
<b><img src="markdownmonstericon.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />



