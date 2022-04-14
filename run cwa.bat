set drive=%cd:~0,2%
set cwd=%cd%
%~d0
cd %~dp0

gsudo winsw restart .\winsw_config\subcovert.xml
gsudo winsw restart .\winsw_config\download_sub.xml
gsudo winsw restart .\winsw_config\clash_control.xml
gsudo winsw restart .\winsw_config\run_clash.xml
gsudo winsw restart .\winsw_config\loop_update.xml

%drive%
cd %cwd%