#!/bin/bash
DEPLOY_PATH=/home/ubuntu/action/  # 배포 경로

# 필요한 경우, 디렉토리 생성
mkdir -p $DEPLOY_PATH

# 이전 빌드 파일 삭제
echo "> 이전 빌드 파일 삭제" >> $DEPLOY_PATH/deploy.log
find $DEPLOY_PATH -type f \( -name "demo-0.0.1-SNAPSHOT.jar" -o -name "demo-0.0.1-SNAPSHOT-plain.jar" \) -exec rm {} \;

# 새 빌드 파일의 경로 찾기
BUILD_JAR=$(ls /home/ubuntu/2023-2-OSSProj-TurtleNeck-9/backend/build/libs/demo-0.0.1-SNAPSHOT.jar)
JAR_NAME=$(basename $BUILD_JAR)
echo "> build 파일명: $JAR_NAME" >> $DEPLOY_PATH/deploy.log

# build 파일 복사
echo "> build 파일 복사" >> $DEPLOY_PATH/deploy.log
cp $BUILD_JAR $DEPLOY_PATH

# 현재 실행중인 애플리케이션의 PID 확인
echo "> 현재 실행중인 애플리케이션 pid 확인" >> $DEPLOY_PATH/deploy.log
CURRENT_PID=$(pgrep -f $JAR_NAME)

if [ -z $CURRENT_PID ]
then
  echo "> 현재 구동중인 애플리케이션이 없으므로 종료하지 않습니다." >> $DEPLOY_PATH/deploy.log
else
  echo "> kill -15 $CURRENT_PID"
  kill -15 $CURRENT_PID
  sleep 5
fi

# JAR 파일 배포
echo "> DEPLOY_JAR 배포" >> $DEPLOY_PATH/deploy.log
nohup java -jar $DEPLOY_PATH/$JAR_NAME >> $DEPLOY_PATH/deploy.log 2>>$DEPLOY_PATH/deploy_err.log &
