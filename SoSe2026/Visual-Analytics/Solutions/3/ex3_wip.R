library(tidyverse)
library(stringr)
library(magrittr)
library(cluster)
library(dbscan)
library(patchwork)
library(proxy)

# Task 1 Solution

student <- read_csv("clustering-student-mat.csv")
# head(student)

scale_student <- scale(student)
# head(scale_student)

set.seed(123)
kmeans_result <- kmeans(scale_student, centers = 2)
aggregate(student, by=list(kmeans_result$cluster), FUN=mean)
intermediate <- data.frame(scale_student, kmeans_result$cluster)

#print(intermediate)
#print(kmeans_result)

k3 <- kmeans(scale_student, centers = 3)
inter3 <- data.frame(scale_student, k3$cluster)

k4 <- kmeans(scale_student, centers = 4)
inter4 <- data.frame(scale_student, k4$cluster)

k5 <- kmeans(scale_student, centers = 5)
inter5 <- data.frame(scale_student, k5$cluster)

k6 <- kmeans(scale_student, centers = 6)
inter6 <- data.frame(scale_student, k6$cluster)


k7 <- kmeans(scale_student, centers = 7)
inter7 <- data.frame(scale_student, k7$cluster)

k8 <- kmeans(scale_student, centers = 8)
inter8 <- data.frame(scale_student, k8$cluster)

p2 <- ggplot(intermediate, aes(Exam1, Exam2, color=kmeans_result.cluster)) + geom_point()
p3 <- ggplot(inter3, aes(Exam1, Exam2, color=k3.cluster)) + geom_point()
p4 <- ggplot(inter4, aes(Exam1, Exam2, color=k4.cluster)) + geom_point()
p5 <- ggplot(inter5, aes(Exam1, Exam2, color=k5.cluster)) + geom_point()
p6 <- ggplot(inter6, aes(Exam1, Exam2, color=k6.cluster)) + geom_point()
p7 <- ggplot(inter7, aes(Exam1, Exam2, color=k7.cluster)) + geom_point()
p8 <- ggplot(inter8, aes(Exam1, Exam2, color=k8.cluster)) + geom_point()

(p2 | p3) / 
(p4 | p5) /
(p6 | p7) /
(p8)

# Task 2 solution

mx <- as.matrix(scale_student)

db1 <- dbscan(mx, eps=1, minPts = 4)
db5 <- dbscan(mx, eps=5, minPts = 4)
db10 <- dbscan(mx, eps=10, minPts = 4)

pairs(mx, col=db1$cluster + 1L, main="eps=1")
pairs(mx, col=db5$cluster + 1L, main="eps=5")
pairs(mx, col=db10$cluster + 1L, main="eps=10")

# Task 3 solution

silk1 <- silhouette(kmeans_result$cluster, dist(scale_student))
silk1 <- silhouette(k3$cluster, dist(scale_student))
silk1 <- silhouette(k4$cluster, dist(scale_student))
silk1 <- silhouette(k5$cluster, dist(scale_student))
silk1 <- silhouette(k6$cluster, dist(scale_student))
silk1 <- silhouette(k7$cluster, dist(scale_student))
silk1 <- silhouette(k8$cluster, dist(scale_student))
plot(silk1)

db_silk_1 <- silhouette(db1$cluster, dist(scale_student))
db_silk_1 <- silhouette(db5$cluster, dist(scale_student))
db_silk_1 <- silhouette(db10$cluster, dist(scale_student))
plot(db_silk_1)

# Task 4

dm <- tribble(~p1,~p2,~p3,~p4,~p5,
              0.00, 0.02, 0.90, 0.36, 0.53,
              0.02, 0.00, 0.65, 0.15, 0.24,
              0.90, 0.65, 0.00, 0.59, 0.45,
              0.36, 0.15, 0.59, 0.00, 0.56,
              0.53, 0.24, 0.45, 0.56, 0.00) %>% as.matrix()
rownames(dm) <- letters[1:5]
colnames(dm) <- letters[1:5]
fit <- hclust(as.dist(dm), method = "single")
plot(fit)