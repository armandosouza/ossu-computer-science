;Write out the evaluation step-by-step
(define (foo s)
  (if (string=? (substring s 0 1) "a")
      (string-append s "a")
      s))

(foo (substring "abcde" 0 3))
;(foo (substring "abcde" 0 3))
;(foo abc)
;(if (string=? (substring s 0 1) "a")) - Check if the first letter of parameter s is equal to "a" - True
;(string-append s "a") - Append "a" to parameter s
;Result: abca