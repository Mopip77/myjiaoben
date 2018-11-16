#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.



; 我将CapLock 改成了Alt 基本所有快捷键都是基于这个Alt键 正常姿势就能使用快捷键


;;;;;function change



; ctrl+\ -> 使用剪贴板的图片
^\::
Run D:\Program\Anaconda3\pythonw.exe D:\babun\.babun\cygwin\home\Mopip77\.myjiaoben\photoscaner_gui.py
return


;Cmder cmd下鼠标侧键（返回）换成Enter
~XButton1::
if WinActive("ahk_exe ConEmu64.exe") or WinActive cmd or WinActive("ahk_exe mintty.exe")
{
	Send {Enter}
}
return


; alt-c -> ctrl-c
!c::
Send ^c
return

; alt-v -> ctrl-v 同时区分是否在cmder cmd下
!v::
if WinActive("ahk_exe ConEmu64.exe") or WinActive cmd or WinActive("ahk_exe mintty.exe")
{
	Send +{Ins}
}
else
{
	Send ^v
}
return

; alt-x -> ctrl-x
!x::
Send ^x
return

; alt-w -> ctrl-w 同时区分是否在cmder cmd下
!w::
if WinActive("ahk_exe ConEmu64.exe") or WinActive cmd or WinActive("ahk_exe mintty.exe")
{
	Send exit{Enter}
}
else
{
	Send ^w
}
return

; alt-s -> ctrl-s
!s::
Send ^s
return

; alt-a -> ctrl-a
!a::
Send ^a
return

; alt-b -> ctrl-b
!b::
Send ^b
return

; alt-f -> Esc
!f::
Send {Esc}
return

; alt-j -> down
!j::
Send {Down}
return

; alt-k -> Up
!k::
Send {Up}
return

; alt-h -> Left
!h::
Send {Left}
return

; alt-l -> Right
!l::
Send {Right}
return

; alt-enter -> ctrl-enter
!Enter::
Send ^{Enter}
return


; alt-n -> Home
!n::
Send {Home}
return

; alt-m -> End
!m::
Send {End}
return


; alt-t -> alt-f4
!t::
Send !{F4}
return

; alt-BS -> ctrl-BS
!BS::
Send ^{BS}
return







;;;;Run app

; alt-r -> babun
!r::
Run babun
return

; alt-Space -> chrome
!Space::
Run chrome
return

; alt-p -> notepad
!p::
Run notepad
return




;;;;fast input

; 可以绑定按键快捷输入密码，邮箱，手机号
; 由于隐私此处省略

