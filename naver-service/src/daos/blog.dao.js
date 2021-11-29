// mongoose Model
const BlogData = require('../model/blogData.model');

class BlogDao {
    async create(blogData) {
        const isExist = await BlogData.findOne({ 'link': blogData.getLink() });
        if (!isExist) {
            const newData = new BlogData({
                service: 'naver',
                content: blogData.getContent(),
                link: blogData.getLink(),
                date: blogData.getDate(),
                keyword: blogData.getKeyword(),
                sns: blogData.getSns()
            });
            await newData.save();
        }
    }
}

module.exports = BlogDao;