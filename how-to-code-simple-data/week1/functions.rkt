;Functions
(define (bulb c)
	(circle 40 "solid" c))

(bulb "purple")
;Expected output: a purple circle with radius 40

(bulb (string-append "re" "d"))