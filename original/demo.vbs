Set FSO = CreateObject("Scripting.FileSystemObject")
Set F = FSO.GetFile(Wscript.ScriptFullName)
 
Set WshShell = WScript.CreateObject("WScript.Shell") 
DesktopPath = WshShell.SpecialFolders("Desktop") 
Lnk_Title = "\demo@mining_20_bot.lnk" 
Set Shortcut = WshShell.CreateShortcut(DesktopPath&Lnk_Title) 
 
Shortcut.TargetPath = WshShell.ExpandEnvironmentStrings(FSO.GetParentFolderName(F) + "\demo.bat") 
Shortcut.WorkingDirectory = WshShell.ExpandEnvironmentStrings(FSO.GetParentFolderName(F)) 
Shortcut.IconLocation = FSO.GetParentFolderName(F) + "\demo.ico"
Shortcut.WindowStyle = 1 
 
Shortcut.Save 

Dim Res,Text,Title  ' ��������� ����������

Text="��������  �����������. ������� � ����� � ������ �� ������� �����! ���������� �� ��������� � ����. ������ � @btc_faerm_pro. �� ���� ������� ����� 1 ���!"

Title="������!"

' ������� ���������� ���� �� �����

Res=MsgBox(Text,vbOkCancel+vbInformation+vbDefaultButton2,Title)

' ����������, ����� �� ������ ���� ������ � ���������� ����

If Res=vbOk Then

 MsgBox "��������� �������������. ����� �����! ���������� ����� � �����, � ������� �� ������������ ����!"

Else

 MsgBox "����, �� ����� ������ ������ �����?"

End If
