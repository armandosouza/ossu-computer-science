;A function that produces area of the square, given side s
;; Number -> Number
;; given length of one side of square, produce the area of the square
(check-expect (area 3) 9)
(check-expect (area 4.2) 17.64)

;; (define (area s)
;;	(... s))

(define (area s)
	(* s s))