function best = GeneticosNoNeg(fun, P, gen, pm)
%% Version 1.1
% P is a cell(our population) of vectors(our chromosomes) in Rn with non negative entrances. 
% gen is the number of generations that we'll generate
% pm is the probability of mutation of a chromosome

% This algoritm will optimize with respect the function fun:Rn -> R under the constrain x>=0.
% This algorithm output is the best solution found.  
n = length(P);

% Elitism is aplied to this algorithm by keeping the best member of every generation. 
Elite(1,gen) = {zeros(1,1)}; 
value=zeros(1,gen); %In many cases, is computationally expensive to evaluate the objective function
for i = 1:gen 
    P = Mutation(P, pm, n);
    v = PobValue(fun, P, n);
    [P, v]= Selection(P, v, n);
    [value(i),j] = min(v);
    Elite{i} = P{j};
    A = Aptitudes(v, n);    
    NextGen = Intercourse(P, n, A);
    v1 = PobValue(fun, NextGen, n);
    [~,k] = max(v1);
    NextGen{k} = P{j};
    P = NextGen;
end

[~,k] = min(value);
best = Elite{k};
end




function v = PobValue(fun, P, n)
%% Here the shromosomes of the population P are evaluated by the funtion
%% fun.
v = zeros(n,1);
for i = 1:n
    v(i) = fun(P{i});
end
end

function [P, v]= Selection(P, v, n)
%% The population P is ordered with respect the vector of values v.
for i = 2:n
    for j = 1:n-1
        if v(i) < v(j)
            v1 = v(i);
            v(i) = v(j);
            v(j) = v1;
            aux1 = P{i};
            P{i} = P{j};
            P{j} = aux1;
        end
    end
end
end

function A = Aptitudes(v,n)
%% A is probability distribution. This distribution is created so the best 
%% chromosomes are selected to produce a new population. 
v = 1./v;
A = zeros(1,n);
s = sum(v);
A(1) = v(1)/s;
for i=2:n
    A(i) = A(i-1)+v(i)/s;
end
end
 
function NextGen = Intercourse(P, n, A)
%% A new population is created using our population P and the aptitudes
%% vector A. |P| needs to be a pair number 
m = length(P{1});
prob = rand(1,n);
coor = randi([1,m],1,n/2);
index = zeros(1,n);
%In this stage, the recombination indeces are defined by using random numbers.
for i = 1:n
    j = 1;
    while index(i) == 0
        if prob(i) < A(j) 
            index(i) = j-1;
        end
        j = j+1;
    end
end

NextGen(1,n) = {zeros(1,1)};
% the recombination occurs in this stage.
for i = 1:2:n
    NextGen{i} = P{index(i)};
    NextGen{i+1} = P{index(i+1)};
    for j = coor(i/2+0.5):m
        aux = P{i}(j);
        P{i}(j) = P{i+1}(j);
        P{i+1}(j) = aux;
    end
end
end

function P = Mutation(P, pm, n)
%% The mutation of a chromosome ocures with probability pm.
%% If a mutation ocurres in an index j, the new gen will be 
%% a random number with exponential distributrion with parameter 1/x_j
m = length(P{1});
for i = 1:n
    if pm > rand
        j = randi(m);
        P{i}(j) = ExpDist(P{i}(j));
    end
end
end


function x = ExpDist(mean)
x = -mean*log(1-rand);
end
