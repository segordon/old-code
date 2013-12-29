;; begin alist. insert descriptions with keys into nodes variable
(defparameter *nodes*
  '((living-room (you are in the living room.
                                      a wizard is snoring loudly on the couch.))
                        (garden (you are in a beautiful garden.
                                 there is a well in front of you.))
                        (attic (you are in the attic.
                                there is a giant welding torching in the corner.))))

;; function to allow the player to figure out their own location.
  (defun describe-location (location nodes)
    (cadr (assoc location nodes)))

;; function to define map edges (paths from locations in the node
;; global variable
(defparameter *edges*
  '((living-room (garden west door)
     (attic upstairs ladder))
    (garden (living-room east door))
    (attic (living-room downstairs ladder))))

;; function to build a description of a given edge using symbols
;; gathered -- this is also the first example of quasiquoting
(defun describe-path (edge)
  `(there is a ,(caddr edge) going ,(cadr edge) from here.))

;; function to describe all edges to a given location
(defun describe-paths (location edges)
  (apply #'append (mapcar #'describe-path (cdr (assoc location edges)))))

;; objects
(defparameter *objects* '(whiskey bucket frog chain))

;; object locations
(defparameter *object-locations* '((whiskey living-room)
                                   (bucket living-room)
                                   (chain garden)
                                   (frog garden)))

;; list object visible from location
(defun objects-at (loc objs obj-locs)
  (labels ((at-loc-p (obj)
             (eq (cadr (assoc obj obj-locs)) loc)))
    (remove-if-not #'at-loc-p objs)))

;; describe objects visible from location
(defun describe-objects (loc objs obj-loc)
  (labels ((describe-obj (obj)
             `(you see a ,obj on the floor.)))
    (apply #'append (mapcar #'describe-obj (objects-at loc objs obj-loc)))))

;; define and initialize the player's position
(defparameter *location* 'living-room)

;; define a function for player to look around with
(defun look ()
  (append (describe-location *location* *nodes*)
          (describe-paths *location* *edges*)
          (describe-objects *location* *objects* *object-locations*)))

;; define a function to allow players to walk
(defun walk (direction)
  (let ((next (find direction
                    (cdr (assoc *location* *edges*))
                    :key #'cadr)))
    (if next
        (progn (setf *location* (car next))
               (look))
        '(you cannot go that way.))))

;; allow the player to pick up objects
(defun pickup (object)
  (cond ((member object
                 (objects-at *location* *objects* *object-locations*))
         (push (list object 'body) *object-locations*)
         `(you are now carrying the ,object))
        (t '(you cannot get that.))))

;; function to allow player to check inventory
(defun inventory ()
  (cons 'items- (objects-at 'body *objects* *object-locations*)))

;; customize game REPL
(defun game-repl ()
  (let ((cmd (game-read)))
    (unless (eq (car cmd) 'quit)
      (game-print (game-eval cmd))
      (game-repl))))

;; customize game read
(defun game-read ()
  (let ((cmd (read-from-string
              (concatenate 'string "(" (read-line) ")"))))
    (flet ((quote-it (x)
             (list 'quote x)))
      (cons (car cmd) (mapcar #'quote-it (cdr cmd))))))
