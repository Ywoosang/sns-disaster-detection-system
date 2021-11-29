import axios from 'axios';

export const postMail = async(manager,mailText) => {
    axios({
        method: "post",
        url: "https://disasterback.cf/api/mail",
        data: {
          mailText: mailText,
          manager: manager,
        }
    })
  };