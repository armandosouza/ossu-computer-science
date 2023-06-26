;;Cond Expressions - how to evaluate it
(cond [(> 1 2) "bigger"]
	  [(= 1 2) "equal"]
	  [(< 1 2) "smaller"])
;Expected output: smaller

(cond [(< 3 2) "smaller"]
	  [(= 3 2) "equal"]
	  [(> 3 2) "bigger"])

(cond [false "smaller"]
	  [(= 3 2) "equal"]
	  [(> 3 2) "bigger"])

(cond [(= 3 2) "equal"]
	  [(> 3 2) "bigger"])

(cond false "equal"]
	  [(> 3 2) "bigger"])

(cond [(> 3 2) "bigger"])

(cond [true "bigger"])
"bigger"