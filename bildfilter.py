from simpleimage import Image


def main():
    img = Image('images/simba.jpg')

    W = img.getWidth()
    H = img.getHeight()
    for x in range(0, W):
	    for y in range(0, H):
             colors = img.getColorAtPos(x,y)
             summe1 = colors[0]
             summe2 = colors[1]
             summe3 = colors[2]
             summe = 0
             summe = summe + summe1
             summe = summe + summe2
             summe = summe + summe3
             durchschnitt = summe/3
             if (durchschnitt > 153):
                values = (durchschnitt,durchschnitt,durchschnitt)
                img.setColorAtPos(x,y,values)
                img.getColorAtPos(x,y)
    img.show()




      
            
    
                
                
                

if __name__ == '__main__':
    main()
