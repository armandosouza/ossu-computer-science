;; Design a data definition to represent a seat number in a row, where each row has 32 seats (in a perfect shape of a theatre)

;; Interval
;; SeatNum is Natural[1, 32]
;; interp. seat numbers in a row, 1 and 32 are aisle seats
(define SN1  1)
(define SN2 15)
(define SN3 32)

(define (fn-for-seat-num sn)
	(... sn))

;; Template rules used:
;; non-atomic distinct: Natural[1, 32]