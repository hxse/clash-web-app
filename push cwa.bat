chcp 65001
set /p c=请输入commit:
git add .
git commit -m "%c%"
git push https://"$env:hxse_github_token"@github.com/hxse/clash-web-app.git
pause
