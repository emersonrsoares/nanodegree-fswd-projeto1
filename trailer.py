import media
import fresh_tomatoes

soad = media.Movie("System Of a Down", "Uma ótima banda de rock", "https://i.pinimg.com/originals/0b/5d/c5/0b5dc5ad4c3eae272f36d3d87a91ba27.jpg", "https://www.youtube.com/watch?v=DnGdoEa1tPg")

raimundos = media.Movie("Raimundos", "Banda brasileira de Rock", "http://radiocidade.uvv.br/wp-content/uploads/2018/12/47065835_318784618942283_1055781610797924352_n.png","https://www.youtube.com/watch?v=7ICZrd5b75g")

megadeth = media.Movie("Megadeth", "Banda mundialmente conhecida de Rock", "https://f4.bcbits.com/img/a0298531282_10.jpg","https://www.youtube.com/watch?v=aU-dKoFZT0A")

a7x = media.Movie("Avenged Sevenfold", "Banda americana de Rock", "https://j.b5z.net/i/u/6127364/i/avegened_sevenfold_32_ezr2__1_.jpg","https://www.youtube.com/watch?v=cU1Uav0T8S4")

angra = media.Movie("Angra", "Uma banda brasileira de Heavy Metal ", "https://dpz4c7q921os3.cloudfront.net/images/events/13254/f00a24c18f19dad9007dbca7ca2b4e47.jpg", "https://www.youtube.com/watch?v=TXHmgHP6GkQ")

metallica = media.Movie("Metallica", "Uma das melhores bandas de heavy metal", "https://images-na.ssl-images-amazon.com/images/I/41w3DUSNUpL._SL500_AC_SS350_.jpg", "https://www.youtube.com/watch?v=zPpKCrIjaiw")

movies = [soad, raimundos, megadeth, a7x, angra, metallica]

fresh_tomatoes.open_movies_page(movies)