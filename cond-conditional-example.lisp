(defvar *arch-enemy* nil)

(defun pudding-eater (person)
  (cond ((eq person 'henry) (setf *arch-enemy* 'stupid-lisp-alien)
         '(curse you lisp aliene - you ate my pudding))
        ((eq person 'johnny) (setf *arch-enemy* 'useless-old-johnny)
         '(I hope you choked on my pudding johnny))
        (t '(why dont you eat my pudding ))))
