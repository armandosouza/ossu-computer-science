;; Design a function that produces a Boolean if the given city is the best city in the world

;; CityName is String
;; interp. the name of a city
(define CN1 "Vancouver")
(define CN2 "Boston")
#;
(define (fn-for-city-name cn)
	(... cn))

;; Template rules used:
;; atomic non-distinct: String

;; Functions
;; CityName -> Boolean
;; produce true if the given city is the best city in the world
(check-expect (best? "Boston") false)
(check-expect (best? "Rio de Janeiro") true)

; (define (best? cn) false) stub

;; (define (best? cn)
;; 	 (... cn))			template

(define (best? cn)
	(string=? "Rio de Janeiro"))