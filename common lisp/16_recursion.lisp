(defun ismember (obj lst)
   (if (null lst)
       nil
   (if (eql (car lst) obj)
       lst
       (ismember obj (cdr lst)))))
(write (ismember 'b '(a b c d)))
(write " ")
(write (ismember 'l '(a b c d)))
