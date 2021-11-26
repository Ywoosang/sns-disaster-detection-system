class BlogDataDto {
    constructor(content,link,date,keyword,sns){
        this.content = content;
        this.date = date;
        this.link = link;
        this.keyword = keyword;
        this.sns = sns;
    }

    getSns(){
        return this.sns
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