import sys
from algorithms import minimizeCoefficientsBezout, InputAlgorithmException, ImpossibilityAlgorithmException

def main():
    if(len(sys.argv) != 4):
        print("Este programa necessita de exatamente 3 parametros! " + str(len(sys.argv)-1) + " foram passados.")
        return -1

    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = int(sys.argv[3])

        result = minimizeCoefficientsBezout(a,b,c)
        coeff0 = result['coeff0']
        coeff1 = result['coeff1']
        print(max(a*coeff0,b*coeff1))


    except ValueError:
        print("Um dos parametros passados nao pode ser convertido em um inteiro!")
        return -1
    except InputAlgorithmException:
        print("Os parametros enviados nao respeitam os requisitos do problema!")
        return -1
    except ImpossibilityAlgorithmException:
        print("Nao e possivel resolver o problema com estas inputs!")
        return -1

    return 0

if __name__ == "__main__":
    main()
