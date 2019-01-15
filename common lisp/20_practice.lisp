(defun inputnum ()
 (format t "input a number")
 (let ((val (read)))
   (if (numberp val)
       val
       (inputnum))))
