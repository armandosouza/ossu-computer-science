;Design a function that consumes an image and determines whether the image is tall
;; Image -> Boolean
;; produce true if the image is tall
(require 2htdp/image)
(check-expect (tall (rectangle 3 4 "solid" "red")) true)
(check-expect (tall (rectangle 5 3 "solid" "blue")) false)

;; (define (tall img) false)	;stub
;; (define (tall img)			;template
;;		(...img))

(define (tall img)
	(if (> (image-height img) (image-width img))
		true
		false))