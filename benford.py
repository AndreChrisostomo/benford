import matplotlib.pyplot as plt


# files = ['LULA1.txt', 'LULA2.txt', 'JAIR1.txt', 'JAIR2.txt']
def benford(data):
    # with open(data,'r') as f:
    for i, x in enumerate(data):
        if type(x) == int:
            data[i] = str(x)

    digit1 = []
    digit2 = []
    digit3 = []
    digit4 = []
    digit5 = []
    digit6 = []
    digit7 = []
    digit8 = []
    digit9 = []
    digit0 = []
    
    # i = f.readline()
    for line in data:
        primeiro_digito = line[0]
        if primeiro_digito == '1':
            digit1.append(primeiro_digito)
            
        elif primeiro_digito == '2':
            digit2.append(primeiro_digito)
            
        elif primeiro_digito == '3':
            digit3.append(primeiro_digito)
            
        elif primeiro_digito == '4':
            digit4.append(primeiro_digito)
            
        elif primeiro_digito == '5':
            digit5.append(primeiro_digito)
            
        elif primeiro_digito == '6':
            digit6.append(primeiro_digito)
            
        elif primeiro_digito == '7':
            digit7.append(primeiro_digito)
            
        elif primeiro_digito == '8':
            digit8.append(primeiro_digito)
            
        elif primeiro_digito == '9':
            digit9.append(primeiro_digito)
            
        elif primeiro_digito == '0':
            digit0.append(primeiro_digito)
            


        labels = '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
        sizes = [len(digit1), len(digit2), len(digit3), len(digit4), len(digit5), len(digit6), len(digit7), len(digit8), len(digit9), len(digit0)]
        #percentage of len
        sizes_p = [i / 100 for i in sizes]

        #plot bar chart
        plt.plot(labels,sizes_p)
        if data == 'LULA1.txt':
            plt.title('LULA PRIMEIRO TURNO')
        elif data == 'LULA2.txt':
            plt.title('LULA SEGUNDO TURNO')
        elif data == 'JAIR1.txt':
            plt.title('JAIR PRIMEIRO TURNO')
        elif data == 'JAIR2.txt':
            plt.title('JAIR SEGUNDO TURNO')
        
        plt.xlabel('DIGITOS')
        plt.ylabel('FREQUENCIA')
        plt.show()

        print(sizes)


        