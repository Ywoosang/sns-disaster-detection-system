class BlogDataDto {
    constructor(content,link,date,keyword){
        this.content = content;
        this.date = date;
        this.link = link;
        this.keyword = keyword;
    }

    getContent() {
        return this.content;
    }

    getDate() {
        return this.date;
    }

    getLink(){
        return this.link;
    }

    getKeyword(){
        return this.keyword;
    }
}

module.exports = BlogDataDto;