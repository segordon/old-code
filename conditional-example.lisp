(defun pudding-eater (person)
  (case person
    ((henry) (setf *arch-enemy* 'stupid-lisp-alien)
     '(curse you lisp alien))
    ((johnny) (setf *arch-enemy* 'useless-old-johnny)
     '(I hope you choked johnny))
    (otherwise '(why you eat pudding stranger ?))))
