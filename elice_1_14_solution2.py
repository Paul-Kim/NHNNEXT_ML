import statsmodels.api
import numpy

def main():
    (N, X, Y) = read_data()

    results = do_multivariate_regression(N, X, Y)
    print(results.summary())

    effective_variables = get_effective_variables(results)
    print(effective_variables)
    
    #print_students_data()

def read_data():
    # 1
    file = []
    N = []
    X = []
    Y = []
    with open("students.dat") as f:
        for line in f:
            file.append(line.strip())
    
    Xname = file[0].split() #X1~X5 name
    Yname = Xname.pop() #GPA
    N = [Xname, Yname] #get name
    
    #print(Xname)
    #print(Yname)
    #print(file)
    
    for i in range(1,len(file)):
        file[i] = file[i].split()
        
        # Y must be 1-dimensional numpy.array.
        Y.append(float(file[i].pop()))
        X.append(file[i])
        
    for x in X:
        for j in range(0,5):
            x[j] = float(x[j])
    
    #print(X)
    #print(Y)
        
    X = numpy.array(X)
    Y = numpy.array(Y)
    return (N, X, Y)

def do_multivariate_regression(N, X, Y):
    
    sm = statsmodels.api
    # 2
    #print(X.shape)
    #print(Y.shape)
    
    #X = sm.add_constant(X)
    results = sm.OLS(Y, X).fit()
    
    return results

def get_effective_variables(results):
    eff_vars = []
    # 3
    for i in range(0,5):
        #print(results.pvalues[i])
        if 0.05 > results.pvalues[i] :
            eff_vars.append("x%d" % (i+1) )

    return eff_vars

def print_students_data():
    with open("students.dat") as f:
        for line in f:
            print(line)

if __name__ == "__main__":
    main()