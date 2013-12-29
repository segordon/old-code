;; v 1.0
;; (defun say-hello ()
;;   (print "Please type your name:")
;;   (let ((name (read)))
;;     (print "Nice to meet you, ")
;;     (print name)))

(defun say-hello ()
  (princ "Please type your name:")
  (let ((name (read-line)))
    (princ "Nice to meet you, ")
    (princ name)))
