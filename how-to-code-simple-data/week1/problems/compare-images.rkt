;Based on the two constants provided, write three expressions to determine
(define IMAGE1 (rectangle 10 15 "solid" "red"))
(define IMAGE2 (rectangle 15 10 "solid" "red"))
;IMAGE1 is taller than IMAGE2
(if (> (image-height IMAGE1) (image-height IMAGE2))
	"IMAGE1 is taller than IMAGE2"
	"IMAGE2 is taller than IMAGE1")
;IMAGE1 is narrower than IMAGE2
(if (> (image-height IMAGE1) (image-height IMAGE2))
	"IMAGE1 is narrower than IMAGE2"
	"IMAGE2 is narrower than IMAGE1")
;IMAGE1 has both the same width AND height as IMAGE2
(if (and (= (image-width IMAGE1) (image-width IMAGE2))
		 (= (image-height IMAGE1) (image-height IMAGE2)))
	"IMAGE1 and IMAGE2 have the same width and height"
	"IMAGE1 and IMAGE2 haven't the same width and height"
)