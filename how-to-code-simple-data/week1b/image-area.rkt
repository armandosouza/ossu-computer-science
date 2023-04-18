;; Image -> Natural
;; produce image's width * height to calculate its area
(require 2htdp/image)
(check-expect (image-area (rectangle 2 3 "solid" "red")) (* 2 3))

;; (define (image-area img) 0) ;stub
;; (define (image-area img)
;;		(...img))

(define (image-area img)
	(* (image-width img) (image-height img)))