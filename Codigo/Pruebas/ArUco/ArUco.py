import cv2
from cv2 import sqrt
from cv2 import sort
import numpy as np
from cv2 import putText # Import the OpenCV library
import numpy as np # Import Numpy library
import pickle

def PPDisstance(A, B):
  return ((A[0] - B[0])**2 + (A[1] - B[1])**2)**0.5

'''qq
	long double GetArea() {
		long double area = 0;q
		for(int i = 0; i < vertices.size(); i++) {
			area += vertices[i].GetX() * vertices[(i + 1) % vertices.size()].GetY() - vertices[(i + 1) % vertices.size()].GetX() * vertices[i].GetY();
		}
		return abs(area) / 2;
	}
'''
def Error_lado_cuadrado(ladoA, ladoB,ladoC,ladoD):
  return (ladoA + ladoB + ladoC + ladoD)/4

def PolygonArea(vertices):
  area = 0
  for i in range(len(vertices)):
    area += vertices[i][0] * vertices[(i+1) % len(vertices)][1] - vertices[(i+1) % len(vertices)][0] * vertices[i][1]
  return abs(area) / 2



desired_aruco_dictionary = "DICT_ARUCO_ORIGINAL"
centimeters = 31.3
areaOfPolygon = 0

mapa = {"values":[]}
# The different ArUco dictionaries built into the OpenCV library. 
ARUCO_DICT = {
  "DICT_4X4_50": cv2.aruco.DICT_4X4_50,
  "DICT_4X4_100": cv2.aruco.DICT_4X4_100,
  "DICT_4X4_250": cv2.aruco.DICT_4X4_250,
  "DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
  "DICT_5X5_50": cv2.aruco.DICT_5X5_50,
  "DICT_5X5_100": cv2.aruco.DICT_5X5_100,
  "DICT_5X5_250": cv2.aruco.DICT_5X5_250,
  "DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
  "DICT_6X6_50": cv2.aruco.DICT_6X6_50,
  "DICT_6X6_100": cv2.aruco.DICT_6X6_100,
  "DICT_6X6_250": cv2.aruco.DICT_6X6_250,
  "DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
  "DICT_7X7_50": cv2.aruco.DICT_7X7_50,
  "DICT_7X7_100": cv2.aruco.DICT_7X7_100,
  "DICT_7X7_250": cv2.aruco.DICT_7X7_250,
  "DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
  "DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL
}
  
def main():
  global centimeters, areaOfPolygonq
  """
  Main method of the program.
  """
  # Check that we have a valid ArUco marker
  if ARUCO_DICT.get(desired_aruco_dictionary, None) is None:
    print("[INFO] ArUCo tag of '{}' is not supported".format(
      args["type"]))
    sys.exit()
     
  # Load the ArUco dictionary
  print("[INFO] detecting '{}' markers...".format(
    desired_aruco_dictionary))
  this_aruco_dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_5X5_50)
  this_aruco_parameters = cv2.aruco.DetectorParameters_create()
   
  # Start the video stream
  url = "http://192.168.68.104:8080/video"
  url2 = "http://10.22.152.216:8080/video"
  cap = cv2.VideoCapture(0)
  
  

   
  while(True):
  
    # Capture frame-by-frame
    # This method returns True/False as well
    # as the video frame.
    ret, frame = cap.read()  
     
    # Detect ArUco markers in the video frame
    (corners, ids, rejected) = cv2.aruco.detectMarkers(
      frame, this_aruco_dictionary, parameters=this_aruco_parameters)
       
    # Check that at least one ArUco marker was detected
    if len(corners) > 0:
      # Flatten the ArUco IDs list
      ids = ids.flatten()
       
      # Loop over the detected ArUco corners
      for (marker_corner, marker_id) in zip(corners, ids):
       
        # Extract the marker corners
        corners = marker_corner.reshape((4, 2))
        (top_left, top_right, bottom_right, bottom_left) = corners
        # Convert the (x,y) coordinate pairs to integers
        top_right = (int(top_right[0]), int(top_right[1]))
        bottom_right = (int(bottom_right[0]), int(bottom_right[1]))
        bottom_left = (int(bottom_left[0]), int(bottom_left[1]))
        top_left = (int(top_left[0]), int(top_left[1]))
        def shape():
          figurativa = ''
          return figurativa

         
        # Draw the bounding box of the ArUco detection
        cv2.line(frame, top_left, top_right, (0, 255, 0), 2)
        cv2.line(frame, top_right, bottom_right, (0, 255, 0), 2)
        cv2.line(frame, bottom_right, bottom_left, (0, 255, 0), 2)
        cv2.line(frame, bottom_left, top_left, (0, 255, 0), 2)
         
        # Calculate and draw the center of the ArUco marker
        center_x = int((top_left[0] + bottom_right[0]) / 2.0)
        center_y = int((top_left[1] + bottom_right[1]) / 2.0)
        cv2.circle(frame, (center_x, center_y), 4, (0, 0, 255), -1)
         
        # Draw the ArUco marker ID on the video frame
        # The ID is always located at the top_left of the ArUco marker
        cv2.putText(frame, str(marker_id), 
          (top_left[0], top_left[1] - 15),
          cv2.FONT_HERSHEY_SIMPLEX,
          0.5, (0, 255, 0), 2)
        
        vertices = []
        vertices.append(top_left)
        vertices.append(top_right)
        vertices.append(bottom_right)
        vertices.append(bottom_left)
        lado_izquierdo = abs(PPDisstance(top_left, bottom_left))
        lado_arriba = abs(PPDisstance(top_left, top_right))
        lado_derecho =  abs(PPDisstance(top_right, bottom_right))
        lado_abajo = abs(PPDisstance(bottom_left, bottom_right))
        lados = [lado_izquierdo,lado_derecho,lado_arriba,lado_abajo]
        lados.sort()
        ladomayor = lados[3]
        #istancia = (47763 - abs(-643424531 + 5630000*ladomayor)**0.5)/563
        distancia = 8418.27334095/ladomayor**0.98619329

        #cv2.putText(frame, str(distanceN),  (top_left[0], top_left[1] - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        #cv2.putText(frame, str(areaOfPolygon),  (top_left[0], top_left[1] - 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.putText(frame, str(distancia)[0:5] + " cm",  (top_left[0], top_left[1] - 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 250, 250), 8)
        #print(areaOfPolygon)
        #print(perimetro)
        #print(distancia)

  
    # Display the resulting frame
    cv2.imshow('frame',frame)
          
    # If "q" is pressed on the keyboard, 
    # exit this loop
    if cv2.waitKey(1) & 0xFF == ord('f'):
      mapa["values"].append((centimeters, distancia))
      print((centimeters, distancia))
      centimeters += 1
      print("agregar muestra")
      
    if cv2.waitKey(1) & 0xFF == ord('q'):
      print("bye")
      break
  
  # Close down the video stream
  cap.release() 
  cv2.destroyAllWindows()
   
if __name__ == '__main__':
  print(__doc__)
  main()
  
  with open('mapa2.pickle', 'wb') as handle:
      pickle.dump(mapa, handle, protocol=pickle.HIGHEST_PROTOCOL)

#Prueba valores de pixeles
# cantidad = 40
# disxpix = np.zeros((2,cantidad))
# for i in range (cantidad -1):
#   disxpix[0][i] = input("distancia")
#   disxpix[1][i] = input("pixeles")
# for i in range(cantidad -1):
#   print("distancia", i, disxpix[0][i])
#   print("pixeles", i, disxpix[1][i])
# print(PolygonArea(vertices))
