(defun hi () (format t "hello world"))
(funcall #'hi)
(write " ")
(apply #'hi nil)
