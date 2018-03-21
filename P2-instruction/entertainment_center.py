import media
import fresh_tomatoes

movieList = {
    'Tomb_Raider' : {
        'title' : 'Tomb Raider',
        'poster_image_url' : 'https://upload.wikimedia.org/wikipedia/en/b/bd/Tomb_Raider_%282018_film%29.png',
        'trailer_url' : 'http://player.youku.com/player.php/sid/XMzQ1NjQxOTk3Ng==/v.swf'
    },
    'The_Shape_of_Water': {
        'title': 'The Shape of Water',
        'poster_image_url': 'https://upload.wikimedia.org/wikipedia/en/3/37/The_Shape_of_Water_%28film%29.png',
        'trailer_url': 'http://player.youku.com/player.php/sid/XMzQ1NjkwOTE2NA==/v.swf'
    },
    'Bajrangi_Bhaijaan': {
        'title': 'Bajrangi Bhaijaan',
        'poster_image_url': 'https://upload.wikimedia.org/wikipedia/en/d/dd/Bajrangi_Bhaijaan_Poster.jpg',
        'trailer_url': 'http://player.youku.com/player.php/sid/XMzM2OTU1Mjg0OA==/v.swf'
    },
    'Peter_Rabbit': {
        'title': 'Peter Rabbit',
        'poster_image_url': 'https://upload.wikimedia.org/wikipedia/en/3/3d/Peter-rabbit-teaser.jpg',
        'trailer_url': 'http://player.youku.com/player.php/sid/XMzQyNTI0Mjg2NA==/v.swf'
    },
    'Three_Billboards': {
        'title': 'Three Billboards Outside Ebbing, Missouri',
        'poster_image_url': 'https://upload.wikimedia.org/wikipedia/en/4/49/Three_Billboards_Outside_Ebbing%2C_Missouri.png',
        'trailer_url': 'http://player.youku.com/player.php/sid/XMzMzMTczNjMwNA==/v.swf'
    },
    'The_Leisure_Seeker': {
        'title': 'The Leisure Seeker',
        'poster_image_url': 'https://upload.wikimedia.org/wikipedia/en/e/e7/The_Leisure_Seeker.png',
        'trailer_url': 'http://player.youku.com/player.php/sid/XMzQxNjYyMTA3Mg==/v.swf'
    }
}

movies = []
for val in movieList:
    movies.push(val)

fresh_tomatoes.open_movies_page(movies)