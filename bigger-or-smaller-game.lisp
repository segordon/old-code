;; define the big and small values
(defparameter *small* 1)
(defparameter *big* 100)

;; use arithmetic shift to halve the sum of two numbers (avg)
(defun guess-my-number ()
  (ash (+ *small* *big*) -1))

;;define smaller/bigger functions

;;smaller
(defun smaller ()
  (setf *big* (1- (guess-my-number)))
  (guess-my-number))

;;bigger
(defun bigger ()
  (setf *small* (1+ (guess-my-number)))
  (guess-my-number))

;;reset function
(defun start-over ()
  (defparameter *small* 1)
  (defparameter *big* 100)
  (guess-my-number))

