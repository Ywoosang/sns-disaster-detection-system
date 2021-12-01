 ![header](https://capsule-render.vercel.app/api?type=wave&color=auto&height=300&section=header&text=SNS-Disaster-Detection-System&fontSize=50)
 <div align=center>
 
 <h3 align=right>TEAM moreAI</h3>
 </div>
 

## 📚목차
1. [📃 Description](#📃-description)
2. [🌍 Environment](#🌍-environment)
3. [📥 Usage](#📥-usage)
4. [🔉 APIs](#🔉-APIs)

## 📃 Description

>### Instragram, Naver blog, Twitter 상의 재난 관련 비정형 소셜 데이터를 수집해 실시간 재난 정보를 제공하는 서비스입니다.<br>

### dashboard
![image](https://user-images.githubusercontent.com/68385605/143953402-4de2b491-db02-4ef4-82b7-5868caa49f71.png)

### 서비스 목록

* [실시간 재난 언급량 순위 제공](#실시간-재난-언급량-순위-제공)
* [시간대별 재난 언급량 제공](#시간대별-재난-언급량-제공)
* [실시간 SNS 트렌드 분석](#실시간-sns-트렌드-분석)
* [재난 상황 추정 시 이메일 전송](#재난-상황-추정-시-이메일-전송)



### 실시간 재난 언급량 순위 제공
![image](https://user-images.githubusercontent.com/68385605/143953317-1c441705-895f-4ae7-809c-6dc0c230e5f6.png)

실시간으로 SNS에서 언급되고 있는 재난들의 언급량 순위를 막대 그래프로 시각화해서 보여줍니다.
### 시간대별 재난 언급량 제공
![image](https://user-images.githubusercontent.com/68385605/143953242-f81fb9b5-5552-432f-a962-fa4cbb0bd07d.png)

![image](https://user-images.githubusercontent.com/68385605/143953160-3c4c8e24-4984-4b01-900e-75942a2378b2.png)

시간대별로 SNS에서 재난이 언급된 횟수를 꺾은선 그래프로 시각화해서 보여줍니다.

### 실시간 SNS 트렌드 분석
![image](https://user-images.githubusercontent.com/68385605/143953030-4230c83e-5373-435a-8ba9-4e5a09da4490.png)

sns 상의 비정형 언어 데이터를 nlp를 통해 필터링하여 재난과 관련되어 언급되고 있는 내용들을 실시간으로 나타냅니다.

### 재난 상황 추정 시 이메일 전송
![image](https://user-images.githubusercontent.com/68385605/143953478-6169b34d-380b-41af-87af-147346a05098.png)

![이메일 전송](./.readme/1-4-1.jpg)<br>

특정 키워드의 언급량이 급격히 늘어났을 때, 관리자에게 메일을 전송합니다.<br>
또한 사용자가 메일을 직접 전송할 수도 있습니다. 

### Ping 테스트
![image](https://user-images.githubusercontent.com/68385605/143953986-7a47df26-b46a-4cb4-91c1-57dfeb072041.png)


사용자가 직접 데이터베이스의 raw 데이터를 조회하도록 제공합니다. 실시간 데이터베이스에 저장되는 재난 관련 데이터를 확인할 수 있습니다.  

## 🌍 Environment

* Container: ![도커](https://img.shields.io/badge/docker-blue)
* proxy sever : ![ngnix](https://img.shields.io/badge/nginx-brightgreen)
* Language : ![파이썬](https://img.shields.io/badge/python-blue) ![자스](https://img.shields.io/badge/javascript-orange) ![타스](https://img.shields.io/badge/typescript-skyblue) ![html](https://img.shields.io/badge/html-red) ![html](https://img.shields.io/badge/css-yellow)
* Framework : ![Vue](https://img.shields.io/badge/Vue.js-green) ![node](https://img.shields.io/badge/node.js-brightgreen) ![flask](https://img.shields.io/badge/flask-gray)
* Database:  ![mysql](https://img.shields.io/badge/mysql-8.0-blue) ![mongo](https://img.shields.io/badge/mongo-5.0.3-brightgreen)

## 📥 Usage

```
 docker-compose up
```

### front setup
```
npm install
```

## 🔉 APIs

```
1. GET /api/instagram/data
```
* request
 * parameters

|파라미터|내용|
|------|---|
|start|불러올 인스타그램 게시물의 최소 게시 시각|
|end|불러올 인스타그램 게시물의 최대 게시 시각|
* response
```python
    {
       "data":[
           {
               "content": "너무 행복해지는 뉴스 봤다",
                "sns": "@c2u8B1 너무 행복해지는 뉴스 봤다....",
                "date": "2021-11-27-08-56",
                "link" : "https://www.instagram.com/p/CWsfshMB25s/",
                "keyword": "폭설",
                "service" :"instagram"
           }   
       ]
    }
```

```
2. GET /api/instagram/ping
```
* request
* response
    * 최신 데이터 20개를 받는다.
```python
 
    {
       "data":[
           { 
             "content": "너무 행복해지는 뉴스 봤다",
                "link" : "https://www.instagram.com/p/CWsfshMB25s/",
                "keyword": "폭설",
                "service" :"instagram"
           }
       ]
    }
```


```
3. GET /api/naver/data
```
* request
    - parameters


|파라미터|내용|
|------|---|
|start|불러올 네이버 게시물의 최소 게시 시각|
|end|불러올 네이버 게시물의 최대 게시 시각|
* response
```javascript
     {
       "data":[
           { 
              "content": 코스피 70P 폭락 국내 첫 오미크론 감염 의심자 발생 국내 10세 미만 첫 <b>코로나</b> 사망 … “사후 <b>확진</b>” 日·스웨덴도 뚫렸다.. ", 
              "keyword": "코로나", 
              "date": "2021-12-01-13-40", 
              "link": "https://blog.naver.com/hahaha_girl?Redirect=Log&logNo=222583783650", 
              "service": "naver" 
              
           }
       ]
    }
```
    
```
4. GET /api/naver/ping
```
* request
* response
    * 최신 데이터 20개를 받는다.
```python
     {
       "data":[
           { 
             "content": 코스피 70P 폭락 국내 첫 오미크론 감염 의심자 발생 국내 10세 미만 첫 <b>코로나</b> 사망 … “사후 <b>확진</b>” 日·스웨덴도 뚫렸다.. ", 
              "keyword": "코로나", 
              "link": "https://blog.naver.com/hahaha_girl?Redirect=Log&logNo=222583783650", 
              "service": "naver" 
           }
       ]
    }
```
```
5. GET /api/twitter/data
```
* request
 * Parameters

|파라미터|내용|
|------|---|
|start|불러올 트위터 게시물의 최소 게시 시각|
|end|불러올 트위터 게시물의 최대 게시 시각|

* response
```javascript
    {
       "data":[
           { 
             "content": "저 여의도 (국제금융센터)몰과 더현대서울 쪽은 공사할 때부터 공사장 붕괴",
             "sns" : "저 여의도 (국제금융센터)몰과 더현대서울 쪽은 공사할 때부터 공사장 붕괴, 지반 붕괴 사고가 계속 있던 곳이라 너무 무섭다 내가 본 것만도 최소 ,회 저렇게 높고 덩치"
             "keyword": "붕괴",
             "date": "2021-11-30-07-32",
             "link": "twitter.com/1264535986374991875/status/1465373170681073667", 
             "service": "twitter" 
           }
       ]
    }
```
```
6. GET /api/twitter/ping
```
* request
* response
    * 최신 데이터 20개를 받는다.
```javascript
    {
       "data":[
           { 
             "content": " 저 여의도 (국제금융센터)몰과 더현대서울 쪽은 공사할 때부터 공사장 붕괴", 
             "keyword": "붕괴", "date": "2021-11-29T17:32:43.000Z", 
             "link": "twitter.com/1264535986374991875/status/1465373170681073667", 
             "service": "twitter" 
           }
       ]
    }
```
```
7. GET /mail
```
* request
* response
```typescript
{}
```

```
8. GET /model
```
* request
    - parameter

|파라미터|내용|
|------|---|
|start|분석한 게시물의 최소 게시 시각|
|end|분석한 게시물의 최대 게시 시각|

* response
```python
     {
       "data":[
           { 
             "content": "저 여의도 (국제금융센터)몰과 더현대서울 쪽은 공사할 때부터 공사장 붕괴",
             "sns" : "저 여의도 (국제금융센터)몰과 더현대서울 쪽은 공사할 때부터 공사장 붕괴, 지반 붕괴 사고가 계속 있던 곳이라 너무 무섭다 내가 본 것만도 최소 ,회 저렇게 높고 덩치"
             "keyword": "붕괴",
             "date": "2021-11-30-07-32",
             "link": "twitter.com/1264535986374991875/status/1465373170681073667", 
             "service": "twitter" 
           }
       ]
    }
``` 

```
9. GET /model/ping
```
* request
* response
    * 최신 데이터 20개를 받는다.
```python
    {
       "data":[
           { 
             "content": " 저 여의도 (국제금융센터)몰과 더현대서울 쪽은 공사할 때부터 공사장 붕괴", 
             "keyword": "붕괴", "date": "2021-11-29T17:32:43.000Z", 
             "link": "twitter.com/1264535986374991875/status/1465373170681073667", 
             "service": "twitter" 
           }
       ]
    }
``` 

