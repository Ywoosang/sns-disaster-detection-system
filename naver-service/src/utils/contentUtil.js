module.exports = (title,content) => {
    const blogTitle = title.replace('</b>','').replace('<b>','').replace(',','').replace('.','')
    const blogContent = content.replace('</b>','').replace('<b>','').replace(',','').replace('.','')
    return blogTitle + blogContent;
}