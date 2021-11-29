import axios from 'axios';

export const postMail = async(manager,mailText) => {
    axios({
        method: "post",
        url: "http://localhost:8080/api/mail",
        data: {
          mailText: mailText,
          manager: manager,
        }
    })
  };