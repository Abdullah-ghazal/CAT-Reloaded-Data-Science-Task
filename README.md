# CAT-Realoded DataScience Task - Beginner
## Question (1):
## 1. Define mean, median, and mode. Give a real-world example of when each would be the most appropriate measure of central tendency.
### Definitions:
- **Mean**: is the sum of some sample devided by its number.(Average)

  ***Example***: when the teacher calculate students’ average scores across a class which this value (mean) represents the most students in the class.

- **Median**: is the middle value of some of samples, in the dataset.  

  ***Example***: In a dataset like {1, 2, 3, 4, 5}, the median is 3.

- **Mode**: is the sample which is the most frequent in data.(1,2,3,3,3,4,5,5) => 3  

  ***Example***:  when someone ask a question, and you need to know the most frequent answer from students, usually it is the correct answer.

---

## 2. Explain the concept of variance and standard deviation. How are they related?
- **Standard Deviation**: is the measure of the typical distance between data and the mean
- **Variance**: determines how far each number is from the mean value in a given data set  

- The relation between(variance & standard deviation) => variance = (standard deviation)^2

---

## 3. What do you know about Left and right skewness? And what happens to mean, median and mode in each case?
- **Skewness**: is the degree of asymmetry in a probability distribution.
  - **Left Skewness**: the tail is longer at the Left
    - **Mode**: Constant
    - **Median**: Deviates left
    - **Mean**: Deviates left more than the median
    ![image](https://github.com/user-attachments/assets/d670023b-bd4c-49dd-845d-461a4ae66b15)


  - **Right Skewness**: the tail is longer at the Right
    - **Mode:** Constant
    - **Median:** Deviates right
    - **Mean:** Deviates right more than the median
  ![image](https://github.com/user-attachments/assets/fd666a6e-9722-43b8-a995-4f598ac47633)

---

## 4. What do you know about outliers? Give a real-world example demonstrating your understanding.
- **Definition**: it is an abnormal data points that differs from other data (abnormal points)
    It is falling outside 1.5 * (IQR)

  **Example**: In a classroom, if most students score between 70-90, a score of 20 would be an outlier.

  ![image](https://github.com/user-attachments/assets/a910962c-c083-45bf-bc16-106a6c5449ec)


---

## 5. What’s the difference between population and sample? Do the same measurements (mean, mode, median) apply to both?
### (i)
  **Population**: is the group of elements you want to study, like people, cars, students….
  
  **Sample**: is a specific subset of elements of the population, which is repents the behavior of all elements(population).  

### (ii) YES
 - **mean:** 
        1.  Population=> mean = (sum of population elements)/(no.of elements)
        2.  Sample => mean = (sum of sample elements) / (no.of elements)
 - **mode:** is the same (the most frequent element in population or sample)
 - **median:** is the middle value of dataset in population or sample.

---

## 6.  What is the difference between a discrete and a continuous random variable?
> First, if we define the random variable we say: it is a variable that assigns a numerical value to each outcome in a sample space.

- **Discrete**: is a variable that assigns values we can count
                EX: (1,2,3,4,5,6)
  ![image](https://github.com/user-attachments/assets/86ccc237-e89a-421c-a85b-39974398b758)


- **Continuous**: is a variable that assigns values we can’t count.
                Ex: (Temperature, Time, ….)
  ![image](https://github.com/user-attachments/assets/5f0dd6ba-0374-4b4c-a1ed-c907a16b4893)

---

## 7. What’s the difference between probability mass function and probability density function?
- **probability mass function (PMF):** used to describe the discrete random variables.
- **probability density function (PDF):** used to describe the continuous random variables.

***Note:*** 

    - for PMF => the summation of properties of all elements = 1
    - for PDF => the integration of properties of all elements   = 1

---

## 8. In normal distribution, what is the percentage of data falls within two standard deviations of the mean?
 ***percentage*** = 95% 

 ![image](https://github.com/user-attachments/assets/67256241-1b63-4750-95ac-0d7d482f3695)


----

## Question 2
![image](https://github.com/user-attachments/assets/7de96241-bdc2-4be5-b6a6-f68118757947)

- ### I) For this sample, estimate mean, median, mode, variance and standard deviation.
  => [1 1 1 3 3 3 4 4 6 7 9 9 9 9 11 12 13 13 14 14]
  <img src="https://github.com/user-attachments/assets/cbebe1d1-2fa7-4205-af17-53b68863895a" 
     alt="Coding" 
     width="200" 
     height="250" 
     align="right" >
     
### 1) Mean:
= sum(F*X)/sum(F)
= (1*3 + 3*3 + 4*2 + 6 *1+ 7*1 + 9*4 + 11*1 + 12*1 + 13*2 +     14*2)/(3+3+2+1+1+4+1+1+2+2)
= 7.3


### 2) Median:
= (sum(F)+1)/2
= (20+1)/2 = 10.5 => (8 - 9)
Median = 9

### 3) Mode:
= 9

### 4) Variance (s):
S =  400.2/20 = 20.01
<img src="![image](https://github.com/user-attachments/assets/17ad1c5c-f21d-4bc2-b540-e77b99cd0114)" 
     alt="Coding" 
     width="200" 
     height="250" 
     align="right" >

### 5) Standard Deviation:
	= sqrt(20.01) = 4.4732

- ### II) Demonstrate how it will differ if it was the whole population.
 #### => mean – median – mode => is constant.
 #### => for variance, standard deviation => change

---

## Question 3
![image](https://github.com/user-attachments/assets/5c364a39-1d0b-4617-adc5-397a97637edb)
- ## i) What do you say about the distribution of this sample? How it will affect the mean, median and mode?
#### For calc median: [2.5, 5, 8, 8, 19, 34, 64, 103, 152, 210]
- **The shape is:** Left-skewed.
  
- Mean = (1*2.5 + 2*2.5 +3*3+4*0+5*11+6*15+7*30+8*39+9*49+10*58 ) /(210)
       = (1704.5) / (210) = 8.116
- Median = (105.5) => (103 - 152) => (9)
                     = 9
- Mode = 10

- Median: Deviates left
- Mean:  Deviate left more than median
- mode > median > mean

--- 
## Question 4
### 1.	What do you know about Python’s containers?
- **Container:** is an object(list, or any data structures) containing an other object(integers).
  ***Example:*** list, tuple, set, dictionary, string,…

### 3.	How would you reverse a list in python in one line? (Don’t use reverse() method).
- Using slicing:
Original_list = [1, 2, 3, 4, 5].

Reversed_list = Original_list[ : : -1]

### 4.	Compare between continue, break and pass.
- a.	Continue: 
=> Skips the current iteration to the next iteration of the loop.
<img src="https://github.com/user-attachments/assets/6892268f-ce6e-4ada-a52d-cb26d9bd7630" alt="Coding" width="200" height="250" align="middle">

- b.	Break:
=>  exits the loop at a specific iteration.
<img src="https://github.com/user-attachments/assets/5685cda4-fa20-4c5d-94ec-0f6619d1278c" 
     alt="Coding" 
     width="200" 
     height="250" 
     align="middle" >

- c.	Pass: 
=> When it is executed, nothing happens, we use it to avoid error when empty code is not allowed.
- Ex: i) without path:
<img src="https://github.com/user-attachments/assets/b00d1f30-32b1-4fe9-bbb5-b9797a51ccdd" 
     alt="Coding" 
     width="200" 
     height="250" 
     align="middle" >

- ii) with pass
<img src="https://github.com/user-attachments/assets/aea2f052-f278-4e3d-a43a-065ddf6b3f01" 
     alt="Coding" 
     width="200" 
     height="250" 
     align="middle" >

### 5) What is the output of this code?
<img src="https://github.com/user-attachments/assets/34861f92-7765-40f6-9ac0-d8562acc9435" 
     alt="Coding" 
     width="200" 
     height="250" 
     align="middle" >
=> [11, 2, 3, 4, 5]

### 6) What is the output of this function?
<img src="https://github.com/user-attachments/assets/1cc1e876-66e8-4307-b569-821c2fb4ab57 " 
     alt="Coding" 
     width="200" 
     height="250" 
     align="middle" >
=> [1] [1, 1] [1, 1, 1]
