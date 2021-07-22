# MDL Genetic Algorithms Report

##### Team number : 46

##### Team V

##### Team members :

##### 1.varun Chowdary(2019101114).

##### 2.Abhijith chelpuri(2019111036).

#### The project is applying genetic algorithm on the overfit vector givento obtain a better vector such that it’s MSE is lower on train,validation and test data.

## Getting started:

The genetic algorithm is a search heuristic that is inspired by Charles Darwin’s
theory of natural evolution. This algorithm reflects the process of natural
selection where the fittest individuals are selected for reproduction in order to
produce offspring of the next generation.

The main code for the project is in main.py file.

This is the final code after so many changes in the code some are minor and
some are major.


## BASIC SUMMARY OF THE ALGORITHM:

### INTIALIZING POPULATION:

In the start we have intialized the population from the given overfit randomly
around the given vector as shown:

We have initialized the population size to 24.Which remains constant
throughout the generations.(Basic rule of genetic algorithm).

I have done Value1-1 because when I assigned the value between 0 and 11
from my observations most of the time the first index in the vector is not
getting changed so I did this.

The genetic Algorithm selects 6 Fittest parents from the population.

Number of Parents selected From population: 6.

Next generation population and how are they obtained:

1.From the Crossover of Previous generation parents: 9.

2.From the crossover of the vectors obtained from crossover : 9.

3.From the mutation of Parents in previous generations : 3.

4.From the crossover of mutations obtained in previous generation: 3.

The Above parameters changes throughout the Process of Getting the best
vector.

Then we calculated Fitness of the each Vector in the population Then Choose
as above told 6 parents.


Then we implemented The crossover and mutation of the parent and the
vectors obtained in the before mutation and crossover.

In algorithm we implemented something different from normal genetic
algorithm.

### CALCULATING ERRORS FOR THE POPULATION:

We put all the errors in the fitness 2-D array which has both validation error
and the train error in it in the index (i,o) and (i,1)

### CREATING PARENT POPULATION:

What we have done here is simply is taking the population with least errors the
argsort() function does this in the ascending order and then we placed the
arrays in the parents array.


### CREATING CROSSOVER FOR POPULATION OF NEXT

### GENERATION:

This is what we have done for crossover for the parents i.e population which
have the least error.

##### offspring_crossover = crossover(parents)

##### population[ 0 : 9 ,:]=offspring_crossover[ 0 : 9 ,:]

There is a crossover which functions as below:

The crossover is done as above we have selected parents randomly from
parents and then performed the **simulated binary crossover**.

### CROSSOVER OF THE CHILDREN OBTAINED ABOVE:

We have performed the crossover of the children obtained in the above
generation to make the population more better and to reduce the requests in
a way.

It is done as below


And the crossover function is same as above.

### MUTATION OF THE PARENTS OBTAINED FROM POPULATION:

We have performed mutation on the parents we got from the population and
then performed mutation on those we changes the population of mutation
and how far we go from the parents in the code several times.

AS shown below:

The size of the mutation varied from time to time in our process to get the best
vectors.

#### MUTATION OF THE MUTATION VECTORS OBTAINED ABOVE:

We have performed double mutation on the already mutated vectors this is an
improvement of the first code we have written at some stage this is done so
that we have some vectors different from the parent vectors so that we have a
wide view of the vectors in a single generation. It is done as Shown below.



### Crossover Function:

- The crossover function is done so as to get the children from the parents
    to get a offspring.
- We did crossover in a random and we got children By crossing vectors
    form the parent population.
- The intial crossover is not simulated binary crossover it is a simple
    crossover of parents.
- We did simulated crossover after a series of a good number of normal
    crossover we found this method when are searching how to get best
    vector
- The idea of this is simple as below:
-


###### •

- Now this converts to more simpler way as follows:
- Now we implemented as below.
- We have selected parents randomly as parent1_idx and paren2_idx and
    crossed then to get children.

### MUTATION FUNCTION:

The mutation function is done as below and then it returns the
offspring_mutaion.We decrease the size of the mutation from 6 to 3 as
mutation vectors where too far away.

- We have done mutation with varying parameters in our process to get
    best vectors.


- We have selected some different numbers between different ranges and
    multiplied with the value in the vector which we wanted to change so
    that mutation is done. The part of the vector is also selected randomly
    as to maintain uniformity and not selecting same thing everytime.
- The range in which the vector is mutated is very crucial and we changed
    it between very small to small values.
- As a small change can effect the vector and it’s errors in a negative way
    which we found so many times we had to be more careful everytime we
    did it.
- The mutation population may seem small but it was changed in the
    process.

```
The mutation is done as shown below
```
### FITNESS FUNCTION :

For the created population then we calculated the fitness of the each vector by
getting errors from the get_errors of each vector.


- We have calculated errors for each vector in population and then took
    parents from them as we told above.
- Better the fitness Better the vector.
- We got two vectors from the get_errors and I used a combination of
    both to calculate fitness.
- From fitness I have assigned parents for next generation.
- Fitness is calculated as err[i] + (trainfactor * error[0])
- Train factor is changed from time to time.By which we obtained a
    balance between the validation and train error where in intial given
    overfit vector there is a large gap.
- Intially the train error is low and validation error is high so we put a
    factor of 0.x to give more importance to validation error we increased
    values and at 0.7 not exactly we found a balance between these two.

The code for calculating the fitness is shown below.

### HYPER PARAMETERS:

- POPULATION SIZE: We initially had the population around 40 then we changed to 24 so as to reduce the size because we have small number of requests per day and to use them effectively we did this.

- CROSSOVER POPULATION COUNT: Intially we distributed the population uniformly across the mutation and crossover as 6 but as we proceeded we we have increased the crossover the population to 9 and the double crossover to 9 so total 18.

- MUTATION POPULATION: We initially distributed population uniformly between mutation and crossover because initially we thought and then decreased the population to a minimal amount of 3 because they were similar and they impacted us in a negative way.

- TRAINFACTOR:We used train factor as to give more importance to test error than the validation one.First we considered only one but later we gave importance but less to test error.

- MUTATION RANGE:We had varied this from around a range of ( -1.x,+1.x) to a small range of (-.x,+.x) we have done this to keep our view sometimes large when we are getting similar vectors to a small value when vectors obtained variey considerably.

- DISTRIBUTION INDEX:we varied the distribution index between 2 to 5 according to what we do in simulated binary then what higher value of it indicates parents and children are closer to each other.

### HUERISTICS APPLIED:

- **TRAINFACTOR:**

##### First we took only test error and proceeded but It produced better results only for some generation then they found not to decreases so I implemented this so as to get better at both of them and at this point errors were still high.

- **MODIFYING TRAIN FACOTR:**

##### At start we have given a fixed train factor of 0.7 so as to give importance but less to validation error but after I discovered I neglected one and the are going far away I decided to change from time to time so as to get low values for both. This helped us but not in a great way.

- **SIMULATED CROSSOVER:**

##### we implement this after long time of starting project where there was no improvement in vectors. In this also we changes the distribution index from time to time.

##### These are the heuristics applied

### STATISTICAL INFORMATION:
We have changed the train factor from 0 to 2 .What I have observed is that is that when I had 0 then I observed that the difference grow between them and only one got better then I changes values between them so as to consider other one also when I did this I got better vectors I did’nt store these but this is what I have observed.


