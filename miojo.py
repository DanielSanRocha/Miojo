import sys
from algorithms import minimizeCoefficientsBezout

def main():
    if(len(sys.argv) != 4):
        print("Este programa necessita de exatamente 3 parametros! " + str(len(sys.argv)-1) + " foram passados.")
        return -1

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = int(sys.argv[3])

        result = minimizeCoefficientsBezout(a,b,c)

        if(result == False):
            print("Nao e possivel resolver o problema com estes valores ou a entrada e invalida")
            return -1
        else:
            coeff0 = result['coeff0']
            coeff1 = result['coeff1']
            print(max(a*coeff0,b*coeff1))
            
            return 0

    except:
        print("Um dos parametros passados nao pode ser convertido em um inteiro!")
        return -1


if __name__ == "__main__":
    main()
