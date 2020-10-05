const url = new Request('http://localhost:5000/health')

fetch(url)
    .then(body => body.json())
    .then(response => loadDOM(response))

const sectionNews = document.getElementById('information')
const loadText = document.getElementById('text-load')
// Replica isso em cada uma das páginas para mim? só copiar e colar o arquivo

function loadDOM(news) {
    console.log(news)
    for(var i = 0; i < news.length; i++) {
        const title = document.createElement('a')
        const img = document.createElement('img')
        const description = document.createElement('h3')
        const div = document.createElement('div')
        const feedInformation = document.createElement('div')

        const descrip = news[i].description
        const url = news[i].url
        const url_image = news[i].img
        const text = news[i].title

        description.innerHTML = descrip
        description.className = 'news'
        
        img.src = url_image
        img.className = 'image'

        title.text = text
        title.className = 'h1_esporte'
        title.href = url
        title.target = '_blank'

        feedInformation.appendChild(title)
        feedInformation.appendChild(description)
        feedInformation.className = 'feed-information'

        
        div.appendChild(feedInformation)

        url_image !='' ? div.appendChild(img) : null
        
        div.className = 'feed'

        loadText.remove()
        sectionNews.appendChild(div)
    }
}