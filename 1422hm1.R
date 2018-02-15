
library(caret)
library(rpart.plot)
library(gplots)
library(ROCR)
library(VIM)
library(lattice)
library(ggplot2)
library(psych)
library(rpart)
setwd("/Users/hubert/Downloads")


college<-read.csv("College.csv")
rownames(college) <- college[,1]

college<-college[ ,-1]
fix(college)
summary(college)
pairs(college[1:10])# produce a scatterplot matrix of the first ten columns or variables of the data
plot(college$Outstate~college$Private)#Which alumnidonate more to their colleges --- those who go to public schools or those who go to private schools?
#in order to know the which alumni donates more,we have to know how to read the boxplot(minimum , max , median,q1 13)//there are some outliers,variability the mass
Elite<-rep("No",  nrow(college))
Elite[college$Top10perc >50]<-"yes"
Elite<- as.factor(Elite)
college<-data.frame(college,Elite)
summary(Elite)# the summary shows that there are 78 ellite schools in totall
par(mfrow = c(2,2))
hist(college$Personal, col = 1, xlab = "Books", ylab = "number")
hist(college$Outstate, col = 3, xlab = "outstate", ylab = "number")
hist(college$Grad.Rate, col = 5, xlab = "Grad Rate", ylab = "number")
hist(college$perc.alumni, col = 4, xlab = "% alumni", ylab = "number")


# problem 2 linear regression

#fist to pick up an attribute willbe strongly correlated with response variable
# a
df <- read.csv("nba.csv", header=T, sep=",")
model <- lm(PTS ~FTA, data=df)
summary(model)#AFTER run several data variables ,i find the positive value of fta is very large(1.75) ,so it is good to be used as a predictor.
names(model)#in order to know how well the model fits the data ,we have to understand that :the rse should be small and r squared should be close to 1 too,from the summary, i know the r squared is far away from 1,so the fittness is not very good  
#print the variable chosen and the correlation plot.
plot(model, 1)
plot(model$fitted.values, model$residuals, 
     xlab = "Fitted values\nlm(sales ~.)", 
     ylab="Residuals", 
     main="Residuals vs. Fitted"); 
abline(model)
# b
set.seed(1122)
index <- sample(1:nrow(df), 250)#samples  250 numbers between 1 and the total rows of the data frame that you read the NBA dataset in
train <- df[index, ]
test <- df[-index, ]# the use of -index as the row variable to gather all the rows that were not in the sampled index

#(c) You are to pick 3-4 attributes
pairs.panels(train[1:23])#this is from psych package, and pick 3-4 attributes that will act as regressors based on the whether value of the num is positive enough,only look at the last line of pts
# plot the correlation between the response variable and the regressors


#(d) Multiple regression (multi-variate):






