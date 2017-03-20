# Yue weekly updates

## 02-17-2017

- **Past week:** Went over unsharp masking paper with Kostya and Stefan and wrote code for most part of the algorithm described in the paper 
- **Got stuck on:** Unsure of how to implement adaptive updates for lambda1 and lambda2.
- **Coming week:** Compare codes and ideas with Kostya and finish writing an initial version implementation of unsharp masking. 

## 03-10-2017

- **Past week:** Compared codes with Kostya and completed working code for the unsharp masking algorithm.
- **Got stuck on:** Values of the parameters that worked with our test images were very different from the values suggested in the paper. 
- **Coming week:** Test code more thoroughly, fix any bugs and refine code.

## 03-17-2017

- **Past week:** Worked with Stefan to optimize unsharp masking code. Remove almost all nested loops and tried reimplementing inversion of precision of gradient matrices.
- **Got stuck on:** Calculating precision of gradient still takes a lot of time. Have trouble applying precision_of_gradient function efficiently on the entire auto-correlation matrix.
- **Coming week:** Try to optimize unsharp masking more. Research ways to do efficient inversions on 2 by 2 matrices.
