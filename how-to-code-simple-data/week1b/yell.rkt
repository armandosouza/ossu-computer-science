;Design a function called yell that consumes strings like 'hello' and adds '!' to produce strings like 'hello!'
;; String -> String
;; adds ! to the end of a string
;; (define (yell s) s)

(check-expect (yell "test") "test!")
(check-expect (yell "hi") "hi!")

;; (define (yell s)
;; 	(string-append s "!"))

(define (yell s)
	(string-append s "!"))