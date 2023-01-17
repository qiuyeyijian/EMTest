#!/bin/sh

# 回到项目根目录，并拉取分支内容
cd ..
git pull

ID=`netstat -lnp | grep 9821 | awk '{print $7}'|awk -F '/' '{print $1}'`

# 杀死占用9821端口的进程
for id in $ID
do

kill -9 $id
echo "killed $id"

done


nohup yarn docs:build > emtest.log 2>&1 & 
nohub yarn docs:serve > emtest.log 2>&1 & exit

