;Introduced a new primitive - boolean - and how to use if sentences in Racket
(define I1 (circle 10 "solid" "red"))
(define I2 (circle 20 "solid" "blue"))
(< (image-width I1) (image-width I2))
;Expected output: true
(define (count sen)
	(string-length sen))

(>= (count "Test") (count "Round"))
;Expected output: false

(string=? "foo" "bar")
;Expected output: false

(if (< (image-width I1) (image-width I2))
	"yes"
	"no")
;Expected output: yes, because the I1's width is less than I2's width.

(and (< (image-width I1) (image-width I2))
	 (< (count "Test") (count "Large")))
;Expected output: true, because both expressions are truthy evaluated.

(or (> (image-width I1) (image-width I2))
	(< (count "Testing") (count "Large")))