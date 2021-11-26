const App =  require('./app')
const BlogController = require('./controllers/blog.controller');

const app = new App(process.env.NAVER_PORT, [new BlogController()]);

app.listen();