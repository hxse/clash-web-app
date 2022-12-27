set drive=%cd:~0,2%
set cwd=%cd%
%~d0
cd %~dp0

sudo winsw restart .\winsw_config\subcovert.xml
sudo winsw restart .\winsw_config\download_sub.xml
sudo winsw restart .\winsw_config\clash_control.xml
sudo winsw restart .\winsw_config\clash_yacd.xml
sudo winsw restart .\winsw_config\run_clash.xml
sudo winsw restart .\winsw_config\loop_update.xml

%drive%
cd %cwd%
