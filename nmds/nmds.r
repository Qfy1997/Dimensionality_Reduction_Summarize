library(vegan)
> data("iris")
> rownames(iris) <- paste0("Sample",1:nrow(iris))
> 
> head(iris)
        Sepal.Length Sepal.Width Petal.Length Petal.Width Species
Sample1          5.1         3.5          1.4         0.2  setosa
Sample2          4.9         3.0          1.4         0.2  setosa
Sample3          4.7         3.2          1.3         0.2  setosa
Sample4          4.6         3.1          1.5         0.2  setosa
Sample5          5.0         3.6          1.4         0.2  setosa
Sample6          5.4         3.9          1.7         0.4  setosa
> data_iris<-iris[,-5]
> head(data_iris)
        Sepal.Length Sepal.Width Petal.Length Petal.Width
Sample1          5.1         3.5          1.4         0.2
Sample2          4.9         3.0          1.4         0.2
Sample3          4.7         3.2          1.3         0.2
Sample4          4.6         3.1          1.5         0.2
Sample5          5.0         3.6          1.4         0.2
Sample6          5.4         3.9          1.7         0.4
set.seed(1)
> iris_nmds <- metaMDS(data_iris, distance="bray", k=2, try=20, trymax=50, autotransform=T,
+                                              model="global", stress=1, maxit=200, parallel=2, noshare=F)
Run 0 stress 0.03775523 
Run 1 stress 0.03775521 
... New best solution
... Procrustes: rmse 8.899606e-06  max resid 9.094553e-05 
... Similar to previous best
Run 2 stress 0.03775524 
... Procrustes: rmse 1.020071e-05  max resid 4.172967e-05 
... Similar to previous best
Run 3 stress 0.03775525 
... Procrustes: rmse 1.138463e-05  max resid 4.68872e-05 
... Similar to previous best
Run 4 stress 0.05418169 
Run 5 stress 0.03775527 
... Procrustes: rmse 1.546513e-05  max resid 6.222323e-05 
... Similar to previous best
Run 6 stress 0.03775523 
... Procrustes: rmse 7.565293e-06  max resid 3.064085e-05 
... Similar to previous best
Run 7 stress 0.04709622 
Run 8 stress 0.0377552 
... New best solution
... Procrustes: rmse 5.056184e-06  max resid 2.201342e-05 
... Similar to previous best
Run 9 stress 0.05317 
Run 10 stress 0.06031998 
Run 11 stress 0.03775522 
... Procrustes: rmse 6.767236e-06  max resid 3.236913e-05 
... Similar to previous best
Run 12 stress 0.04709621 
Run 13 stress 0.05376138 
Run 14 stress 0.03775519 
... New best solution
... Procrustes: rmse 2.922055e-06  max resid 1.176576e-05 
... Similar to previous best
Run 15 stress 0.03775525 
... Procrustes: rmse 1.936989e-05  max resid 8.370867e-05 
... Similar to previous best
Run 16 stress 0.03775521 
... Procrustes: rmse 6.338141e-06  max resid 2.692558e-05 
... Similar to previous best
Run 17 stress 0.03775527 
... Procrustes: rmse 2.271558e-05  max resid 9.753559e-05 
... Similar to previous best
Run 18 stress 0.03775521 
... Procrustes: rmse 5.36883e-06  max resid 2.44535e-05 
... Similar to previous best
Run 19 stress 0.0528996 
Run 20 stress 0.04713711 
*** Best solution repeated 5 times
> stressplot(iris_nmds)
> iris_nmds_sample_result <- as.data.frame(scores(iris_nmds,"sites"))
> head(iris_nmds_sample_result)
             NMDS1       NMDS2
Sample1 -0.3306351  0.04484127
Sample2 -0.3353756 -0.03144932
Sample3 -0.3707610 -0.01344881
Sample4 -0.3577781 -0.03313785
Sample5 -0.3440980  0.04849401
Sample6 -0.2648507  0.10404665
> speciescolumn<-iris[,"Species"]
> iris_nmds_sample_result$speciescolumn<-speciescolumn
> head(iris_nmds_sample_result)
             NMDS1       NMDS2 speciescolumn
Sample1 -0.3306351  0.04484127        setosa
Sample2 -0.3353756 -0.03144932        setosa
Sample3 -0.3707610 -0.01344881        setosa
Sample4 -0.3577781 -0.03313785        setosa
Sample5 -0.3440980  0.04849401        setosa
Sample6 -0.2648507  0.10404665        setosa
> library(ggplot2)
> library(ggalt)
p1 <- ggplot() + 
+     geom_point(data=iris_nmds_sample_result, 
+         aes(x=NMDS1,y=NMDS2,
+             colour=speciescolumn,group=speciescolumn),size=3) + # add the point markers
+     geom_encircle(data=iris_nmds_sample_result,
+     aes(x=NMDS1,y=NMDS2,fill=speciescolumn,group=speciescolumn), alpha=0.1, show.legend = F) +
+     geom_hline(aes(yintercept=0),color="grey", linetype=3) + 
+     geom_vline(aes(xintercept=0),color="grey", linetype=3) + 
+     labs(title=paste0("Stress: ", round(iris_nmds$stress,3))) + 
+     theme_classic()
> p1