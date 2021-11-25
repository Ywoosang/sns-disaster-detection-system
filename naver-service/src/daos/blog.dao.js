// mongoose Model
const BlogData = require('../model/blogData.model');

class BlogDao {
    async create(blogData) {
        const isExist = await BlogData.findOne({ 'link': blogData.getLink() });
        if (!isExist) {
            console.log('-----------------INSERT-------------------')
            console.log(blogData)
            console.log('------------------DONE--------------------')
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