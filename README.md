# 2023-2-OSSProj-TurtleNeck-9

2023-2 오픈소스소프트웨어프로젝트 
9조 거북목의 레포지토리입니다.

## 📌 프로젝트 주제

동국대학교 공과대학 시간표 추천 서비스

## Team Detail

<!--

| 이름   | 전공           | E-mail |
| ------ | -------------- | ------------------- |
| 정지만 | 산업시스템공학과 | wlaks2317@gmail.com |
| 김성준 | 산업시스템공학과 | jobcho6320@naver.com |
| 황재영 | 수학과        | jaey0913@dongguk.edu | -->

<div>

|<img src="https://avatars.githubusercontent.com/u/67041750?v=4" width="80">|         <img src="https://avatars.githubusercontent.com/u/89504367?v=4" width="80">         | <img src="https://avatars.githubusercontent.com/hwangjy0913" width="80"> |
|:---:|:-------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------:|
|[정지만](https://github.com/jjm2317)|                            [김성준](https://github.com/SeongJoon-K)                            |                  [황재영](https://github.com/hwangjy0913)                   |
|산업시스템공학과|                                          산업시스템공학과                                           |                                   수학과                                    |
|Frontend|                                           Backend                                           |                             Machine Learning                             |
| |   AWS ec2, s3 기반 자동배포 및 빌드 구축  <br/>시간표 조회 구현, 로그인, 회원가입, <br/>Spring security JWT 인증인가   |         훈련 데이터 전처리, <br/> 모델 훈련 및 훈련 가중치 저장 <br/> ML 서버, 훈련 모델 생성 <br/> 예측 알고리즘 BeamSearch 구현            |

</div>

## ⌨️ 커밋 컨벤션 

다음 컨벤션을 따릅니다.

| 커밋 타입 | 설명                               |
|-----------|----------------------------------|
| `feat`    | 새로운 기능을 추가할 경우                   |
| `fix`     | 버그를 고친 경우                        |
| `style`   | 코드 포맷 변경, 세미 콜론 누락, 코드 수정이 없는 경우 |
| `refactor`| 리팩토링 하는 경우                       |
| `chore`   | 자잘한 수정 사항 반영                     |
| `docs`    | 문서를 수정한 경우                       |
| `test`    | 테스트 추가                           |
## 🛠️ Tech Stack

<div align=center>

### ✔️Back-end
  
  <img src="https://img.shields.io/badge/amazon codedeploy-4479A1?style=for-the-badge&logo=amazon d&logoColor=white">
  <img src="https://img.shields.io/badge/amazon ec2-FF9900?style=for-the-badge&logo=amazon ec2&logoColor=white">
<img src="https://img.shields.io/badge/amazon rds-Fz1100?style=for-the-badge&logo=amazon rds&logoColor=white">
<img src="https://img.shields.io/badge/amazon s3-569A31?style=for-the-badge&logo=amazon s3&logoColor=white">
<img src="https://img.shields.io/badge/intellijidea-000000?style=for-the-badge&logo=IntelliJ&logoColor=white"><img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
  <img src="https://img.shields.io/badge/fontawesome-528DD7?style=for-the-badge&logo=fontawesome&logoColor=white">


<img src="https://img.shields.io/badge/springboot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white">
  <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white">
<img src="https://img.shields.io/badge/ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white">

### ✔️Frond-end

  <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
  <img src="https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=React&logoColor=black">

  <img src="https://img.shields.io/badge/Redux-764ABC?style=for-the-badge&logo=Redux&logoColor=purple"><img src="https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=Next.js&logoColor=white">


### ✔️ ML
  <img src="https://img.shields.io/badge/tensorflow-black?style=for-the-badge&logo=tensorflow">
  <img src="https://img.shields.io/badge/Pandas-blue?style=for-the-badge&logo=pandas">
  <img src="https://img.shields.io/badge/Google%20Colab-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/flask-black?style=for-the-badge&logo=Flask">
  <img src="https://img.shields.io/badge/numpy-white?style=for-the-badge&logo=NumPy&logoColor=black">
</div>

## 💻 개발 환경

### OS

- Ubuntu 22.04 LTS

### Backend
- Java 17 (Corretto 17)
- Spring Boot v3.1.4
- MySQL 8.0.33
- Intellij
- Gradle v8.3

### Frontend
- Node 20
- HTML5, CSS, JavaScript
- React 18
- BootStrap v5.2
- Visual Studio Code v1.78.2

### Storage
- AWS RDS t3.micro
- AWS S3

### ML
- Python 3.10.12
- Tensorflow 2.15.0
- Pandas 2.1.3
- Visual Studio Code 1.84.2
- Google Colab


## 📌 프로젝트 내용 (Description)

동국대학교 공과대학 시간표 추천시스템을 통해서 학생들의 기존 수강 과목을 기반하여, 전공 과목간의 연속성을 확보
전공별로 진로 분야가 다른 공과대학 학생들의 학업 성취도 고취 및 취업 시장에서의 경쟁력을 확보할 수 있도록 함.

## 🛒 ERD

![](docs/images/ERD.png)

##  사용한 오픈소스 라이브러리 


### Frontend

- "@babel/core": "^7.23.2"
- "@babel/preset-react": "^7.22.15"
- "@babel/preset-typescript": "^7.23.2"
- "@storybook/addon-essentials": "^7.5.2"
- "@storybook/addon-interactions": "^7.5.2"
- "@storybook/addon-links": "^7.5.2"
- "@storybook/addon-onboarding": "^1.0.8"
- "@storybook/blocks": "^7.5.2"
- "@storybook/react": "^7.5.2"
- "@storybook/react-webpack5": "^7.5.2"
- "@storybook/testing-library": "^0.2.2"
- "@types/react": "^18.2.34"
- "@types/react-dom": "^18.2.14"
- "@typescript-eslint/eslint-plugin": "^6.4.0"
- "@typescript-eslint/parser": "^6.9.1"
- "babel-loader": "^9.1.3"
- "css-loader": "^6.8.1"
- "eslint": "^8.0.1"
- "eslint-config-prettier": "^9.0.0"
- "eslint-plugin-import": "^2.25.2"
- "eslint-plugin-n": "^15.0.0 || ^16.0.0 "
- "eslint-plugin-prettier": "^5.0.1"
- "eslint-plugin-promise": "^6.0.0"
- "eslint-plugin-react": "^7.33.2"
- "eslint-plugin-storybook": "^0.6.15"
- "html-webpack-plugin": "^5.5.3"
- "prettier": "3.0.3"
- "storybook": "^7.5.2"
- "style-loader": "^3.3.3"
- "typescript": "^5.2.2"
- "webpack": "^5.89.0"
- "webpack-cli": "^5.1.4"
- "webpack-dev-server": "^4.15.1"
- "@emotion/react": "^11.11.1"
- "@emotion/styled": "^11.11.0"
- "@fontsource/roboto": "^5.0.8"
- "@mui/icons-material": "^5.14.16"
- "@mui/material": "^5.14.16"
- "@mui/styles": "^5.14.19"
- "@tanstack/react-query": "^5.4.3"
- "@tanstack/react-query-devtools": "^5.4.3"
- "axios": "^1.6.0"
- "react": "^18.2.0"
- "react-dom": "^18.2.0"
- "react-material-ui-carousel": "^3.4.2"
- "react-router-dom": "^6.18.0"


## 환경 설정 및 실행 CLI

### Frontend

```bash
// in /frontend
yarn install
yarn start
```


## License

해당 프로젝트는 MIT License를 따릅니다.
