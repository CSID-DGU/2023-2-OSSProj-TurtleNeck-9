#!/bin/bash
BUILD_JAR=$(ls /home/ec2-user/action/build/libs/*.jar)
JAR_NAME=$(basename $BUILD_JAR)
echo "> build 파일명: $JAR_NAME" >> /home/ubuntu/action/deploy.log

#!/bin/bash
DEPLOY_PATH=/home/ubuntu/action/

echo "> 이전 빌드 파일 삭제" >> /home/ubuntu/action/deploy.log
# 'demo-0.0.1-SNAPSHOT.jar'와 'demo-0.0.1-SNAPSHOT-plain.jar' 파일 삭제
find $DEPLOY_PATH -type f \( -name "demo-0.0.1-SNAPSHOT.jar" -o -name "demo-0.0.1-SNAPSHOT-plain.jar" \) -exec rm {} \;

echo "> build 파일 복사" >> /home/ubuntu/action/deploy.log
# 새 빌드 파일 복사
cp /path/to/your/demo-0.0.1-SNAPSHOT.jar $DEPLOY_PATH
cp /path/to/your/demo-0.0.1-SNAPSHOT-plain.jar $DEPLOY_PATH

echo "> 현재 실행중인 애플리케이션 pid 확인" >> /home/ubuntu/action/deploy.log
CURRENT_PID=$(pgrep -f $JAR_NAME)

if [ -z $CURRENT_PID ]
then
  echo "> 현재 구동중인 애플리케이션이 없으므로 종료하지 않습니다." >> /home/ubuntu/action/deploy.log
else
  echo "> kill -15 $CURRENT_PID"
  kill -15 $CURRENT_PID
  sleep 5
fi

DEPLOY_JAR=$DEPLOY_PATH
echo "> DEPLOY_JAR 배포"    >> /home/ubuntu/action/deploy.log
nohup java -jar $DEPLOY_PATH/demo-0.0.1-SNAPSHOT.jar >> /home/ubuntu/deploy.log 2>/home/ubuntu/action/deploy_err.log &
