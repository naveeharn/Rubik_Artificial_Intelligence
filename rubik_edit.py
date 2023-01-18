import random
import math
def gen_rubik():
    rubik =[
        '#0','#0','#0','W1','W2','W3','#0','#0','#0','#0','#0','#0',
        '#0','#0','#0','W4','W5','W6','#0','#0','#0','#0','#0','#0',
        '#0','#0','#0','W7','W8','W9','#0','#0','#0','#0','#0','#0',
        'O1','O2','O3','G1','G2','G3','R1','R2','R3','B1','B2','B3',
        'O4','O5','O6','G4','G5','G6','R4','R5','R6','B4','B5','B6',
        'O7','O8','O9','G7','G8','G9','R7','R8','R9','B7','B8','B9',
        '#0','#0','#0','Y1','Y2','Y3','#0','#0','#0','#0','#0','#0',
        '#0','#0','#0','Y4','Y5','Y6','#0','#0','#0','#0','#0','#0',
        '#0','#0','#0','Y7','Y8','Y9','#0','#0','#0','#0','#0','#0',]
    # rubik =[
    #     '000','001','002','003','004','005','006','007','008','009','010','011',
    #     '100','101','102','103','104','105','106','107','108','109','110','111',
    #     '200','201','202','203','204','205','206','207','208','209','210','211',
    #     '300','301','302','303','304','305','306','307','308','309','310','311',
    #     '400','401','402','403','404','405','406','407','408','409','410','411',
    #     '500','501','502','503','504','505','506','507','508','509','510','511',
    #     '600','601','602','603','604','605','606','607','608','609','610','611',
    #     '700','701','702','703','704','705','706','707','708','709','710','711',
    #     '800','801','802','803','804','805','806','807','808','809','810','811',]
    return rubik
def same_face_spin(rubik,topleft):
    #samefacespin
    #mid
    #304 -> 405
    temp = rubik[topleft+2+12]
    rubik[topleft+2+12] = rubik [topleft+1]
    #405 -> 504
    temp2 = rubik[topleft+1+12*2]
    rubik[topleft+1+12*2] = temp
    #504 -> 403
    temp = rubik[topleft + 12]
    rubik[topleft+12] = temp2
    #403 -> 304
    rubik[topleft+1] = temp
    #edge
    #303 -> 305
    temp = rubik[topleft+2]
    rubik[topleft+2] = rubik[topleft]
    #305 -> 505
    temp2 = rubik[topleft+2+12*2]
    rubik[topleft+2+12*2] = temp
    #505 -> 503
    temp = rubik[topleft+12*2]
    rubik[topleft+12*2] = temp2
    #503 -> 303
    rubik[topleft] = temp
    return rubik
def resame_face_spin(rubik,topleft):

    temp = rubik[topleft+12]
    rubik[topleft+12] = rubik[topleft+1]

    temp2 = rubik[topleft+12*2+1]
    rubik[topleft+12*2+1] = temp

    temp = rubik[topleft+12+2]
    rubik[topleft+12+2] = temp2

    rubik[topleft+1] = temp

    temp = rubik[topleft+12*2]
    rubik[topleft+12*2] = rubik[topleft]

    temp2 = rubik[topleft+12*2+2]
    rubik[topleft+12*2+2] = temp

    temp = rubik[topleft+2]
    rubik[topleft+2] = temp2

    rubik[topleft] = temp

    return rubik
def show_rubik(rubik):
    for i in range(len(rubik)):
        if rubik[i] == '#0':
            print("  ",end=" ")
        else:    
            print (rubik[i],end=" ")
        if (i)%12 == 11:
            print("")
def F(rubik):
    for i in range(3):
        temp = rubik[2*12+3+i]
        rubik [2*12+3+i] =rubik [(5-i)*12+2]

        temp2 = rubik [(3+i)*12+6]
        rubik[(3+i)*12+6] = temp

        temp = rubik [6*12+5-i]
        rubik [6*12+5-i] = temp2

        rubik [(5-i)*12+2] = temp
    rubik = same_face_spin(rubik,3*12+3)
    return rubik
def R(rubik):
    for i in range(3):
        temp = rubik[(5-i)*12+9]
        rubik [(5-i)*12+9] = rubik[i*12+5]

        temp2 = rubik[(6+i)*12+5]
        rubik[(6+i)*12+5] = temp

        temp = rubik[(3+i)*12 +5]
        rubik[(3+i)*12 +5] = temp2

        rubik[i*12+5] = temp
    rubik = same_face_spin(rubik,3*12+6)
    return rubik
def U(rubik):
    for i in range(3):
        #300 -> 309
        temp = rubik[3*12+9+i]
        rubik [3*12+9+i] = rubik[3*12+i]
        #309 -> 306
        temp2 = rubik[(3*12+6+i)]
        rubik[(3*12+6+i)] = temp
        #306 -> 303
        temp = rubik[(3*12+3+i)]
        rubik[(3*12+3+i)] = temp2
        #303 -> 300
        rubik[3*12+i] = temp 
    rubik = same_face_spin(rubik,3)
    return rubik
def B(rubik):
    for i in range(3):
        #300 -> 803
        temp = rubik[8*12+3+i]
        rubik[8*12+3+i] = rubik[(3+i)*12]
        #803 -> 508
        temp2 =rubik [(5-i)*12 +8]
        rubik [(5-i)*12 +8] = temp
        #508 -> 003
        temp = rubik[5-i]
        rubik[5-i] = temp2
        #003 -> 301
        rubik[(3+i)*12] = temp
    rubik = same_face_spin(rubik,3*12+9)
    return rubik
def L(rubik):
    for i in range(3):
        #003 -> 303
        temp = rubik[(3+i)*12+3]
        rubik[(3+i)*12+3] = rubik[(i*12)+3]
        #303 -> 603
        temp2 = rubik [(6+i)*12+3]
        rubik [(6+i)*12+3] = temp
        #603 -> 511
        temp = rubik [(5-i)*12+11]
        rubik [(5-i)*12+11] = temp2
        #511 -> 003
        rubik[(i*12)+3] = temp
    rubik = same_face_spin(rubik,3*12)
    return rubik
def D(rubik):
    for i in range(3):
        #500 -> 503
        temp = rubik[(5*12)+3+i]
        rubik[(5*12)+3+i] = rubik[(5*12)+i]
        #503 -> 506
        temp2 = rubik[(5*12)+6+i]
        rubik[(5*12)+6+i] = temp
        #506 -> 509
        temp = rubik[(5*12)+9+i]
        rubik[(5*12)+9+i] = temp2
        #509 ->500
        rubik[(5*12)+i] = temp
    rubik = same_face_spin(rubik,6*12+3)
    return rubik

def reF(rubik):
    for i in range (3):
        #302 ->603
        temp = rubik[(6*12)+3+i]
        rubik[(6*12)+3+i] = rubik[(3+i)*12+2]
        #603 -> 506
        temp2 = rubik [(5-i)*12+6]
        rubik [(5-i)*12+6] = temp
        #506 -> 205
        temp = rubik [(2*12)+5-i]
        rubik [(2*12)+5-i] = temp2
        #205 -> 302
        rubik [(3+i)*12+2] = temp
    rubik = resame_face_spin(rubik,3*12+3)
    return rubik
def reR(rubik):
    for i in range(3):
        #005 -> 305
        temp = rubik[(3+i)*12+5]
        rubik[(3+i)*12+5] = rubik [(i*12)+5]
        #305 -> 605
        temp2 = rubik[(6+i)*12+5]
        rubik[(6+i)*12+5] = temp
        #605 -> 509
        temp = rubik[(5-i)*12+9]
        rubik[(5-i)*12+9] =temp2
        #509 -> 005
        rubik[(i*12)+5] = temp
    rubik = resame_face_spin(rubik,3*12+6)
    return rubik
def reU(rubik):
    for i in range(3):
        #300 -> 303
        temp = rubik[(3*12)+3+i]
        rubik[(3*12)+3+i] = rubik[(3*12)+i]
        #303 -> 306
        temp2 = rubik[(3*12)+6+i]
        rubik[(3*12)+6+i]= temp
        #306 -> 309
        temp = rubik[3*12+9+i]
        rubik[(3*12)+9+i] = temp2
        #309-> 300
        rubik[(3*12)+i] = temp
    rubik = resame_face_spin(rubik,3)
    return rubik
def reB(rubik):
    for i in range(3):
        #003 -> 308
        temp = rubik[(3+i)*12+8]
        rubik[(3+i)*12+8] = rubik[3+i]
        #308 -> 805
        temp2 = rubik[(8*12)+5-i]
        rubik[(8*12)+5-i] = temp
        #805 -> 500
        temp = rubik[(5-i)*12]
        rubik[(5-i)*12] = temp2
        #500-> 003
        rubik[3+i] =temp
    rubik = resame_face_spin(rubik,3*12+9)
    return rubik
def reL(rubik):
    for i in range(3):
        #003 ->511
        temp = rubik[(5-i)*12+11]
        rubik[(5-i)*12+11] = rubik[(i*12)+3]
        #511 ->603
        temp2 = rubik[(6+i)*12+3]
        rubik[(6+i)*12+3] = temp
        #603 -> 303
        temp = rubik[(3+i)*12+3]
        rubik[(3+i)*12+3] = temp2
        #303 -> 003
        rubik[(i*12)+3]=temp
    rubik = resame_face_spin(rubik,3*12)
    return rubik
def reD(rubik):
    for i in range(3):
        #500 -> 509
        temp = rubik[(5*12)+9+i]
        rubik[(5*12)+9+i]= rubik[(5*12)+i]
        #509 -> 506
        temp2 = rubik[(5*12)+6+i]
        rubik[(5*12)+6+i] = temp
        #506 -> 503
        temp = rubik[(5*12)+3+i]
        rubik[(5*12)+3+i] = temp2
        #503 -> 500
        rubik[(5*12)+i]= temp
    rubik = resame_face_spin(rubik,6*12+3)
    return rubik

def scramble(rubik,times):
    for i in range(times):
        r = int(math.floor(random.random() * 12))
        match r:
            case 0:
                print("F")
                rubik = F(rubik)
            case 1:
                print("R")
                rubik = R(rubik)
            case 2:
                print("U")
                rubik = U(rubik)
            case 3:
                print("B")
                rubik = B(rubik)
            case 4:
                print("L")
                rubik = L(rubik)
            case 5:
                print("D")
                rubik = D(rubik)
            case 6:
                print("reF")
                rubik = reF(rubik)
            case 7:
                print("reR")
                rubik = reR(rubik)
            case 8:
                print("reU")
                rubik = reU(rubik)
            case 9:
                print("reB")
                rubik = reB(rubik)
            case 10:
                print("reL")
                rubik = reL(rubik)
            case 11:
                print("reD")
                rubik = reD(rubik)
    return rubik

if __name__ == '__main__':
    rubik = gen_rubik()
    rubik = scramble(rubik,5)
    show_rubik(rubik)
