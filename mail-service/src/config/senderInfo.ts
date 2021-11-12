import * as dotenv from 'dotenv';
dotenv.config();

export default  {
    "user": process.env.GMAIL,
    "pass": process.env.GMAIL_PASSWORD
}

