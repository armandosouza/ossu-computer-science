;String methods in BS Language
(string-append "test" " " "another test")
;Expected output: test another test
(string-length "avenue")
;Expected output: 6
(substring "Armando" 0 4)
;Expected output: Arma

;Images
(require 2htdp/image)
;A circle with radius 10, solid line and red color
(circle 10 "solid" "red")
;A rectangle with height 20, width 40, outline and blue color
(rectangle 20 40 "outline" "blue")
;Text Test with font size 22 and black color
(text "Test" 22 "black")