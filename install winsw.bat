sudo winsw install .\winsw_config\clash_control.xml
sudo winsw install .\winsw_config\download_sub.xml
sudo winsw install .\winsw_config\loop_update.xml
sudo winsw install .\winsw_config\run_clash.xml
sudo winsw install .\winsw_config\subcovert.xml

cd ".\python_script"
pip install -r requirements.txt
pause