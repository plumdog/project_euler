#!/usr/bin/racket -r

;; phi(n) = n*sum_{p|n} (1 - 1/p)
;; 1/phi(n) = (1/n)*sum_{p|n} p/(p - 1)
;; n/phi(n) = sum_{p|n} p/(p - 1)

;;
(define memoize
  (lambda (f) ;; returns a memoized version of function f
    (let ((memo '()))
      (lambda args
        (let ((match (assoc args memo)))    ;; look up args
          (if match
              (cadr match)                  ;; return stored value
              (let ((value (apply f args))) ;; or calculate if necessary
                (set! memo                  ;; and store new value
                      (cons (list args value) memo))
                value)))))))
;;

(define (product l)
  (if (empty? l)
	  1
	  (* (car l) (product (cdr l)))))

(define (n-over-phi n primes)
  (product
   (map (lambda (p) (/ p (- p 1)))
		(filter (lambda (p) (= (remainder n p) 0)) primes))))
				
  

;; I believe this is correct, but far too slow. Need use more facts
;; about gcds and phi values to reduce the work.



(define (remainder x y)
  (if (> x y)
	  (remainder (- x y) y)
	  y))

(define (gcd x y)
  (let ((r (remainder x y)))
	(if (= r 0)
		y
		(gcd y r))))

(define (is-coprime x y)
  (= 1 (gcd x y)))

(define (count-coprime-upto n upto)
  (if (= upto 1)
	  1
	  (+
	   (count-coprime-upto n (- upto 1))
	   (if (is-coprime n upto) 1 0))))

(define (smallest-coprime-divisor n)
  (smallest-coprime-divisor- n 2))

(define (smallest-coprime-divisor- n trial)
  (if (> trial (sqrt n))
	  null
	  (if (= (modulo n trial) 0)
		  (if (is-coprime (/ n trial) trial)
			  (list trial (/ n trial))
			  (smallest-coprime-divisor- n (+ trial 1)))
		  (smallest-coprime-divisor- n (+ trial 1)))))

(define (phi-raw n)
  (let ((divs (smallest-coprime-divisor n)))
	(if (null? divs)
		(count-coprime-upto n (- n 1))
		(*
		 (phi (car divs))
		 (phi (cadr divs))))))

(define phi (memoize phi-raw))

;;(define (n-over-phi n)
;;  (/ n (phi n)))

(define (max-n-for-n-over-phi n sqrtupto)
  (let ((primes (filter-multiples-upto (range 2 n) sqrtupto)))
	(maximise (lambda (m) (n-over-phi m primes)) n 0 0 2)))

(define (maximise f n nmax fmax nmin)
  (if (= n nmin)
	  nmax
	  (let ((my-f (f n)))
		(if (> my-f fmax)
			(maximise f (- n 1) n my-f nmin)
			(maximise f (- n 1) nmax fmax nmin)))))

(define (range from to)
  (if (= from to)
	  '()
	  (cons from (range (+ from 1) to))))

(define (non-trivial-divisor num div)
  (if (= num div)
	  #f
	  (if (= (remainder num div) 0)
		  #t
		  #f)))

(define (filter-multiples candidates num)
  (filter (lambda (x) (not (non-trivial-divisor x num))) candidates))

(define (filter-multiples-upto candidates upto)
  (if (= upto 1)
	  candidates
	  (filter-multiples (filter-multiples-upto candidates (- upto 1)) upto)))
  

(display (max-n-for-n-over-phi 1000000 1000))
;; (display (smallest-coprime-divisor 23))
;; (display (filter-multiples-upto (range 2 1000000) 1000))
(newline)
