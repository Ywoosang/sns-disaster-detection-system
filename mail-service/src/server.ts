import * as  express from 'express';
import mailer from './mail';

const app = express(); 

app.get('/mail', (req, res) => {
  const email:string = 'opellong11@khu.ac.kr';
  let emailParam = {
    toEmail: email,     // 수신할 이메일
    subject: '[SNS 재난 알리미] 재난 정보가 감지되었습니다',   // 메일 제목
    text: `주목할 만한 SNS 재난 정보가 있습니다.`                // 메일 내용
  };
  mailer.sendGmail(emailParam);
  res.status(200).json({
    "message" : "담당자에게 메일 전송을 완료했습니다."
  });
});

// 404 라우터
app.use((req,res,next)=>{
    res.status(404).json({ msg : 'Page Not Found'});
  });

app.use((error, req, res, next) => {
    // 에러 로깅
    // errorLogger.error(error.stack);
    console.error(error)
    // AJAX 요청인 경우
    if (req.is('json') || req.is('multipart/form-data')) {
      res.status(500).json({ message: '시스템 오류가 발생했습니다.' });
    }
  });

const port = 3000;
app.listen(port,()=>{
    console.log('server start',port);
});

 