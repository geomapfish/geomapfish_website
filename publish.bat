cd %~dp0

rmdir /s /q %~dp0\output

mkdir output

cd output

git init

git remote add origin https://github.com/geomapfish/geomapfish.github.io.git

git fetch origin

git merge origin/master

cd ..

Scripts\pelican content -s publishconf.py

cd output

git add --all

git commit -m "Update"

git push origin master

pause