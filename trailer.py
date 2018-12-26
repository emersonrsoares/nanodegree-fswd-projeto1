import movies
import movie_trailer


# Objeto que tem os parametros que serão passados para a class Movie
movie1 = movies.Movie("VINGADORES: ULTIMATO", "Após Thanos eliminar metade das criaturas vivas, os Vingadores precisam lidar com a dor da perda de amigos e seus entes queridos. Com Tony Stark (Robert Downey Jr.) vagando perdido no espaço sem água nem comida, Steve Rogers (Chris Evans) e Natasha Romanov (Scarlett Johansson) precisam liderar a resistência contra o titã louco.", "https://bit.ly/2BDK67m", "https://www.youtube.com/watch?v=g6ng8iy-l0U", "25/04/2019")

movie2 = movies.Movie("ERA UMA VEZ UM DEADPOOL", "Determinado a provar que Deadpool 2 é um filme para toda a família, Wade Wilson limpa todos os palavrões e sangue da narrativa e sequestra o ator e diretor Fred Savage para reencenar A Princesa Prometida. Savage é obrigado a ouvir o 'conto de fadas' do Mercenário Tagarela, incluindo sua luta com Cable e a formação da X-Force.", "https://bit.ly/2V8Q5Ka", "https://www.youtube.com/watch?v=_SiPmxKk7pI", "27/12/2018")

movie3 = movies.Movie("DRAGON BALL SUPER BROLY", "Apesar da Terra estar em um período de calmaria, Goku se recusa a parar de treinar constantemente - ele quer estar pronto para quando uma nova ameaça surgir. O que ele não imaginava era que seu novo inimigo seria Broly, um poderoso super saiyajin sedento por vingança, que deseja destruir todos que encontrar pela frente.", "https://bit.ly/2Vbhmvt", "https://www.youtube.com/watch?v=_K91eeP25NA", "03/01/2019")

movie4 = movies.Movie("O REI LEÃO", "Simba (Donald Glover) é um jovem leão cujo destino é se tornar o rei da selva. Tudo corre bem, até que uma grande tragédia atinge sua vida mudando sua trajetória para sempre. A sinopse oficial ainda não foi divulgada.", "https://bit.ly/2GSnPsv", "https://www.youtube.com/watch?v=J57HnR6FPW0", "18/07/2019")

movie5 = movies.Movie("CREED II", "Adonis Creed (Michael B. Jordan) saiu mais forte do que nunca de sua luta contra 'Pretty' Ricky Conlan (Tony Bellew), e segue sua trajetória rumo ao campeonato mundial de boxe, contra toda a desconfiança que acompanha a sombra de seu pai e com o apoio de Rocky (Sylvester Stallone). Sua próxima luta não será tão simples, ele precisa enfrentar um adversário que possui uma forte ligação com o passado de sua família, o que torna tudo ainda mais complexo.", "https://bit.ly/2ENMyv1", "https://www.youtube.com/watch?v=HKXoW8FISj4", "27/11/2018")

movie6 = movies.Movie("CULPA", "O policial Asger Holm (Jakob Cedergren) está acostumado a trabalhar nas ruas de Copenhaguem, mas devido a um conflito ético no trabalho, é confinado à mesa de emergências. Encarregado de receber ligações e transmitir às delegacias responsáveis, ele é surpreendido pela chamada de uma mulher desesperada, tentando comunicar o seu sequestro sem chamar a atenção do sequestrador. Infelizmente, ela precisa desligar antes de ser descoberta, de modo que Asger dispõe de poucas informações para encontrá-la. Começa a corrida contra o relógio para descobrir onde ela está, para mobilizar os policiais mais próximos e salvar a vítima antes que uma tragédia aconteça.", "https://bit.ly/2ENE2wn", "https://www.youtube.com/watch?v=LxHgMEZY3VM", "27/12/2018")

# array com as instancias e seus dados
movie = [movie1, movie2, movie3, movie4, movie5, movie6]

# Chamada do método open_movies_page, responsável por passar os parametos ao código que gera o html e abre o browser.
movie_trailer.open_movies_page(movie)
