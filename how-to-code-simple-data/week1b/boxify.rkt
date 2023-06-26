;;Design a function to put a box around the given image
;;Image -> Image
;;Given an image, produce a "boxified" image
(require 2htdp/image)
(check-expect (boxify (rectangle 2 3 "solid" "red")) 
	(overlay (rectangle 4 6 "outline" "black") (rectangle 2 3 "solid" "red")))

;;(define (boxify img) (rectangle 0 0 "solid" "black"))	stub
;;(define (boxify img) 
;;	(...img))

(define (boxify img) 
	(overlay 
		(rectangle (* (image-width img) 1.5) (* (image-height img) 1.5) "outline" "black") img))