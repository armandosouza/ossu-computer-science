;; Design a data definition to represent a letter grade in a course
;; LetterGrade is one of:
;; - "A"
;; - "B"
;; - "C"
;; interp. the letter grade in a course
;; <examples are redundant for enumeration>
(define (fn-for-letter-grade lg)
	(cond [(string=? lg "A") (...)]
		  [(string=? lg "A") (...)]
		  [(string=? lg "A") (...)]))

;; Template rules used:
;; - one of: 3 cases
;; - atomic distinct value: "A"
;; - atomic distinct value: "B"
;; - atomic distinct value: "C"