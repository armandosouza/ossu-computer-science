;Create an image
(require 2htdp/image)
(define (tile color)
	(square 20 "solid" color))
(above 
	(beside (tile "blue") (tile "yellow"))
	(beside (tile "yellow") (tile "blue")))
;2 rows of 2 squares, with yellow and blue color