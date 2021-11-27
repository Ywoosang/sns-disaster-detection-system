 ![header](https://capsule-render.vercel.app/api?type=wave&color=auto&height=300&section=header&text=NLP-Service&fontSize=50)
 <div align=center>
 
 <h3 align=right>NLP Service</h3>
 </div>
 
 
## 목차
1. [📃 Korean Sentence Splitter](#📃-KSS <a href='https://github.com/likejazz/korean-sentence-splitter'>link</a>)
2. [🌍 FastText](#🌍-NLP Model - Vectorizer)
3. [📥 Kmeans](#📥- Unsupervised Learning - Clustering)

## 📃 Korean Sentence Splitter

>### 한국어 문단을 인풋으로 받아 문단을 문장 단위로 잘라 List로 반환해주는 모듈입니다.<br>

### dashboard
![재난 언급량 순위](./.readme/dashboard1.jpg)<br>

### 서비스 목록

* [실시간 재난 언급량 순위 제공](#실시간-재난-언급량-순위-제공)
* [시간대별 재난 언급량 제공](#시간대별-재난-언급량-제공)
* [실시간 SNS 트렌드 분석](#실시간-sns-트렌드-분석)
* [재난 상황 추정 시 이메일 전송](#재난-상황-추정-시-이메일-전송)



### 실시간 재난 언급량 순위 제공
![재난 언급량 순위](./.readme/1-1.JPG)<br>
실시간으로 SNS에서 언급되고 있는 재난들의 언급량 순위를 막대 그래프로 시각화해서 보여줍니다.
### 시간대별 재난 언급량 제공
![시간대별 재난 언급량](./.readme/1-2.JPG)<br>
![시간대별 재난 언급량](./.readme/1-2-2.jpg)<br>
시간대별로 SNS에서 재난이 언급된 횟수를 꺾은선 그래프로 시각화해서 보여줍니다.

### 실시간 SNS 트렌드 분석
![실시간 SNS 트렌드 분석](./.readme/1-3.JPG)<br>
sns 상의 비정형 언어 데이터를 nlp를 통해 분석하여 재난이 어떤 주제들과 연관되어 언급되고 있는지 실시간으로 나타냅니다.

### 재난 상황 추정 시 이메일 전송
![이메일 전송](./.readme/1-4.jpg)<br>
![이메일 전송](./.readme/1-4-1.jpg)<br>

특정 재난의 언급량이 급격히 일어날 때, 재난 상황임을 감지하고 메일을 전송합니다.

## 🌍 Environment

* Container: ![도커](https://img.shields.io/badge/docker-blue)
* proxy sever : ![ngnix](https://img.shields.io/badge/nginx-brightgreen)
* Language : ![파이썬](https://img.shields.io/badge/python-blue) ![자스](https://img.shields.io/badge/javascript-orange) ![타스](https://img.shields.io/badge/typescript-skyblue)
* Frameworks : ![Vue](https://img.shields.io/badge/Vue.js-green) ![node](https://img.shields.io/badge/node.js-brightgreen) ![flask](https://img.shields.io/badge/flask-gray)
* Database:  ![mysql](https://img.shields.io/badge/mysql-8.0-blue)![mongo](https://img.shields.io/badge/mongo-5.0.3-brightgreen)

## 📥 Usage

```
 docker-compose up
```



