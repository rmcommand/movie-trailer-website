__author__ = 'rm00'
import fresh_tomatoes
import rmedia

#Movie title, storyline, poster and youtube file information that is exported to the webpage
the_matrix = rmedia.Movie("The Matrix", ("Depicts a dystopian future in which reality perceived by humans is in the Matrix"),
                         "http://ia.media-imdb.com/images/M/MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@._V1_SX640_SY720_.jpg",
                         "https://www.youtube.com/watch?v=vKQi3bBA1y8")

inception = rmedia.Movie("Inception", ("A thief who steals corporate secrets through use of dream-sharing technology"),
                        "http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")

equilibrium = rmedia.Movie("Equilibrium", ("In a Fascist future where all forms of feeling are illegal, a man in charge of enforcing the law rises to overthrow the system"),
                        "http://ia.media-imdb.com/images/M/MV5BMTkzMzA1OTI3N15BMl5BanBnXkFtZTYwMzUyMDg5._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=raleKODYeg0")


the_dark_knight = rmedia.Movie("The Dark Knight", ("When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice."),
                        "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=yQ5U8suTUw0")

the_dark_knight_rises = rmedia.Movie("The Dark Knight Rises", ("Eight years after the Joker's reign of anarchy, the Dark Knight is forced to return from his imposed exile to save Gotham City from the brutal guerrilla terrorist Bane with the help of the enigmatic Catwoman."),
                        "http://ia.media-imdb.com/images/M/MV5BMTk4ODQzNDY3Ml5BMl5BanBnXkFtZTcwODA0NTM4Nw@@._V1_SX214_AL_.jpg",
                        "https://www.youtube.com/watch?v=g8evyE9TuYk")

akira = rmedia.Movie("Akira", ("A secret military project endangers Neo-Tokyo when it turns a biker gang member into a rampaging psionic psychopath that only two kids and a group of psionics can stop."),
                        "http://upload.wikimedia.org/wikipedia/en/5/5d/AKIRA_%281988_poster%29.jpg",
                        "https://www.youtube.com/watch?v=7G5zQW4TinQ&safe=active")

the_empire_strikes_back = rmedia.Movie("The Empire Strikes Back", ("After the rebels have been brutally overpowered by the Empire on their newly established base, Luke Skywalker takes advanced Jedi training with Master Yoda, while his friends are pursued by Darth Vader as part of his plan to capture Luke."),
                        "http://upload.wikimedia.org/wikipedia/en/3/3c/SW_-_Empire_Strikes_Back.jpg",
                        "https://www.youtube.com/watch?v=8Hm-9Sai9To")

return_of_the_jedi = rmedia.Movie("Return of the Jedi", ("With the rise of the empire shaking the galaxy at its core, the rebels are driven deep into hiding. The rebels risk all with one last strike."),
                        "http://upload.wikimedia.org/wikipedia/en/b/b2/ReturnOfTheJediPoster1983.jpg",
                        "https://www.youtube.com/watch?v=5UfA_aKBGMc")

attack_of_the_clones = rmedia.Movie("Attack of the Clone", ("Ten years after initially meeting, Anakin Skywalker shares a forbidden romance with Padme, while Obi-Wan investigates an assassination attempt on the Senator and discovers a secret clone army crafted for the Jedi."),
                        "http://img1.wikia.nocookie.net/__cb20130822173923/starwars/images/2/24/EPII_AotC_poster.png",
                        "https://www.youtube.com/watch?v=5UfA_aKBGMc")

#Order of movie files
movies = (the_matrix, inception, equilibrium, the_dark_knight, the_dark_knight_rises, akira, the_empire_strikes_back,
          return_of_the_jedi, attack_of_the_clones)

#Fresh tomato py script that formats information to an HTML page
fresh_tomatoes.open_movies_page(movies)
