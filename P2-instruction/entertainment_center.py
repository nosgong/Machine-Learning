import media
import fresh_tomatoes

movieList = {
    'Tomb_Raider' : {
        'title' : 'Tomb Raider',
        'poster_image_url' : 'https://upload.wikimedia.org/wikipedia/en/b/bd/Tomb_Raider_%282018_film%29.png',
        'trailer_url' : 'https://www.youtube.com/watch?v=8ndhidEmUbI'
    },
    'The_Shape_of_Water': {
        'title': 'The Shape of Water',
        'poster_image_url': 'https://upload.wikimedia.org/wikipedia/en/3/37/The_Shape_of_Water_%28film%29.png',
        'trailer_url': 'https://www.youtube.com/watch?v=XFYWazblaUA'
    },
    'Bajrangi_Bhaijaan': {
        'title': 'Bajrangi Bhaijaan',
        'poster_image_url': 'https://upload.wikimedia.org/wikipedia/en/d/dd/Bajrangi_Bhaijaan_Poster.jpg',
        'trailer_url': 'https://www.youtube.com/watch?v=6DCOjq0omBc'
    },
    'Peter_Rabbit': {
        'title': 'Peter Rabbit',
        'poster_image_url': 'https://upload.wikimedia.org/wikipedia/en/3/3d/Peter-rabbit-teaser.jpg',
        'trailer_url': 'https://www.youtube.com/watch?v=3ittn4f0Em4'
    },
    'Three_Billboards': {
        'title': 'Three Billboards Outside Ebbing, Missouri',
        'poster_image_url': 'https://upload.wikimedia.org/wikipedia/en/4/49/Three_Billboards_Outside_Ebbing%2C_Missouri.png',
        'trailer_url': 'https://www.youtube.com/watch?v=Jit3YhGx5pU'
    },
    'The_Leisure_Seeker': {
        'title': 'The Leisure Seeker',
        'poster_image_url': 'https://upload.wikimedia.org/wikipedia/en/e/e7/The_Leisure_Seeker.png',
        'trailer_url': 'https://www.youtube.com/watch?v=VGGKsVFslJ8'
    }
}

movies = []
for k,val in movieList.items():
    movies.append(media.movie(val))
fresh_tomatoes.open_movies_page(movies)
