# Nick Weekly updates

## 02-24-2017

- **Past week:** Browsed various issues and worked on two Novice ones.
- **Got stuck on:** Not knowing which issues have been addressed and to what
	extent. This update did not get merged the first time around; I most
	likely cloned the repo without forking.
- **Coming week:** Run project by Stéfan and see what he thinks is the best
	approach.

## 03-03-2017

- **Past week:** Filed bug [#2554](https://github.com/scikit-image/scikit-image/issues/2554) 
	and worked on PR [#2555](https://github.com/scikit-image/scikit-image/pull/2555)
	which addresses issue [#2538](https://github.com/scikit-image/scikit-image/issues/2538).
	Scoured every file for argument name name changes (e.g. img -> image), and
	began deprecating `skimage.morphology`'s shapes (moving to standalone
	module).
- **Got stuck on:** Untangling `skimage.morphology` dependencies on
	`skimage.morphology.selem`. Will ask Stéfan for help.
- **Coming week:** Hopefully finish this PR and review changes necessary.