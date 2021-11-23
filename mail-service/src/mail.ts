import * as nodemailer from 'nodemailer'; 
import senderInfo from './config/senderInfo'; 
// 메일발송 객체
const mailSender = {
  // 메일발송 함수
  sendGmail: function (param) {
    var transporter = nodemailer.createTransport({
      // service: 'gmail',   // 메일 보내는 곳
      port: 587,
      host: 'smtp.gmail.com',  
      secure: false,  
      requireTLS: true ,
      auth: {
        user: senderInfo.user,  // 보내는 메일의 주소
        pass: senderInfo.pass   // 보내는 메일의 비밀번호
      }
    });
    // 메일 옵션
    const mailOptions = {
      from: senderInfo.user, // 보내는 메일의 주소
      // 받는 사람
      to: 'opellong11@khu.ac.kr', // 수신할 이메일
      subject: param.subject, // 메일 제목
      text: param.text, // 메일 내용
      html: `<b>안녕하세요</b>`,
    };
    
    // 메일 발송    
    transporter.sendMail(mailOptions, function (error, info) {
      if (error) {
        console.log(error);
      } else {
        console.log('Email sent: ' + info.response);
      }
    });

  }
}

export default mailSender;