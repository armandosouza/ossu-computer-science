;;Design a function that pluralizes a given word.
;;Signature: String -> String
;;Purpose: Consumes a string and produces a pluralized string
;;Stub: (define (pluralizes s) "")

(check-expect (pluralizes "test") "tests")
(check-expect (pluralizes "ground") "grounds")

;;Template
;;(define (pluralizes s) 
;;	(...s))

(define (pluralizes s)
	(string-append s "s"))