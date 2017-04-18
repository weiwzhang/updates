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

## 03-24-2017

- **Past week:** Cleaned up code a little and added condition to stop iteration. Used python profiling tool to analyze running time and efficiency of individual code blocks/helper functions within main function.
- **Got stuck on:** Code is still not efficient enough, need to speed up local variance calculation
- **Coming week:** Rewrite local variance calculation using scipy.LowLevelCallable. Continue profile and optimize code.

## 04-07-2017
- **Past week:** Rewrote local variance calculation using Cython and scipy.LowLevelCallable. Decreased the percentage of the runtime occupied from around 55%~60% to 20%~25%. Decreased total runtime for 120 iterations on a ~300x400 image from ~6s to ~3s.
- **Got stuck on:** Used profiling after speeding up local variance calculations and found that calculating precision of gradiant now takes up the most time. Not sure how to optimize.
- **Coming week:** Research ways to optimize precision of gradient.

## 04-14-2017
- **Past week:** Modified cython code and python code with the help of Stefan to further speed up local variance calculation. Rewrote precision of gradient calculation in cython to decrease runtime.
- **Got stuck on:** Some matrix calculations are still a little slow.
- **Coming week:** Clean up and rewrite entire code in cython.
