# -*- coding: utf-8 -*-
"""Created on <dagens dato>"""
__author__ = "Ane Kleiven"
__email__ = "ane.kleiven@nmbu.no"
"""                        """

# Obligatorisk innlevering 7 

# lisp string 

lisp = '''
(defun LaTeX-newline ()
  "Start a new line potentially staying within comments.
This depends on `LaTeX-insert-into-comments'."
  (interactive)
  (if LaTeX-insert-into-comments
      (cond ((and (save-excursion (skip-chars-backward " \t") (bolp))
                  (save-excursion
                    (skip-chars-forward " \t")
                    (looking-at (concat TeX-comment-start-regexp "+"))))
             (beginning-of-line)
             (insert (buffer-substring-no-properties
                      (line-beginning-position) (match-end 0)))
             (newline))
            ((and (not (bolp))
                  (save-excursion
                    (skip-chars-forward " \t") (not (TeX-escaped-p)))
                  (looking-at
                   (concat "[ \t]*" TeX-comment-start-regexp "+[ \t]*")))
             (delete-region (match-beginning 0) (match-end 0))
             (indent-new-comment-line))
            ;; `indent-new-comment-line' does nothing when
            ;; `comment-auto-fill-only-comments' is non-nil, so we
            ;; must be sure to be in a comment before calling it.  In
            ;; any other case `newline' is used.
            ((TeX-in-comment)
             (indent-new-comment-line))
            (t
             (newline)))
    (newline)))
'''

# define the function for checking parentheses 

def check_parentheses(text):
    # filter out all except parentheses
    filtered_text = [character for character in text if character in '()']
    print(filtered_text)
    
    # make a list with 1 and -1 for open and closed parentheses
    par_values = [1 if character == '(' else -1 for character in filtered_text]
    print(par_values)
    
    # make a list with the iterative sum 
    iterative_sum = [sum(par_values[:i+1]) for i in range(len(par_values))]
    print(iterative_sum)
    
    # calculate the max_depth 
    max_depth = max(iterative_sum) if iterative_sum else 0
    
    # check if parentheses is_valid
    is_valid = all(x >= 0 for x in iterative_sum) 
    
    # check if parentheses is_balanced 
    is_balanced = iterative_sum[-1] == 0  
    
    # return results 
    return max_depth, is_valid, is_balanced


# use the check parentheses function on lisp string 

res = check_parentheses(lisp)
print('Lisp results:')
print(f"max_depth: {res[0]} valid: {res[1]} balanced: {res[2]}")


""" 
max_depth: 8
is_valid: True
is_balanced: True 

"""        


