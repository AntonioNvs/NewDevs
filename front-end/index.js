const url = new Request('http://localhost:5000/news')

const sectionNews = document.getElementById('information')
const loadText = document.getElementById('text-load')

let news = [];

fetch(url)
    .then(response => response.json())
    .then(response => loadDOM(response.articles))

// Manipulação da DOM 

function loadDOM(news) {
    for(var i = 0; i < news.length; i++) {
        const title = document.createElement('a')
        const description = document.createElement('h3')
        const img = document.createElement('img')
        const div = document.createElement('div')
        const feedInformation = document.createElement('div')
        
        const url = news[i].url
        const url_image = news[i].urlToImage
        const text = news[i].title
        const descrip = news[i].description

        description.innerHTML  = descrip
        description.className = 'news'

        img.src = url_image
        img.className = 'news'

        title.text = text
        title.className = 'news'
        title.href = url
        title.target = '_blank'

        feedInformation.appendChild(title)
        feedInformation.appendChild(description)
        feedInformation.className = 'feed-information'

        div.appendChild(feedInformation)
        div.appendChild(img)

        div.className = 'feed'

        loadText.remove()
        sectionNews.appendChild(div)
    }
} 





