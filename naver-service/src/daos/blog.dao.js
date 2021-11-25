// mongoose Model
const BlogData = require('../model/blogData.model');

class BlogDao {
    async create(blogData) {
        const isExist = await BlogData.findOne({ 'link': blogData.getLink() });
        if (isExist) {
            console.log('----------이미 존재하는 데이터---------------')
        } else {
            console.log('블로그 데이터', blogData)
            console.log('----------------삽입 완료--------------------')
            const newData = new BlogData({
                content: blogData.getContent(),
                link: blogData.getLink(),
                date: blogData.getDate(),
                keyword: blogData.getKeyword()
            });
            await newData.save();
        }
    }
}

module.exports = BlogDao;