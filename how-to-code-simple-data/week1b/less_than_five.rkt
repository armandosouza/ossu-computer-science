;Design a function to check if the length of a string is less than 5
;; String -> Boolean
;; Consumes a string and produces a boolean to check if the string length is less than 5
;; (define (less_five s) false) ;stub
(check-expect (less_five "test") true)
(check-expect (less_five "computer") false)

;; (define (less_five s)
;;		(...s))		;template

(define (less_five s)
	(> 5 (string-length s)))