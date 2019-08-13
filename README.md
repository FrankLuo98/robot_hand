# robot_hand
## 机械部分 Mechanical part
* 控制部分由两块板组成，rpiHAT板和rasberry pi。将raspberry pi 连接到rpiHAT板上的接口对应请参考该图  
  There are two single board computers; rpiHAT and Raspberry Pi. Refer to the figure for the interface connecting the raspberry pi to     the rpiHAT board.
  ![Alt text](1.jpg?raw=true "Download MQTTBox")

* 实际使用中raspberry pi zero供电可能不够，请使用raspberry pi 3b+（接口对应不变）  
  In fact ,raspberry pi zero may not have enough power, please use raspberry pi 3b+.(Interface corresponding is same as pi zero)

* 如图，从右向左数为1-8号pwm排针一一对应，只有+5V与GND之间有电容的才可以使用  
  As the figure,from right to left is pwm pins 1-8,can only use the servo which have capacitance among VCC and GND.

* 如图，束线中的棕色线为GND，红色线为+5V，黄线为pwm信号。线上蓝色贴纸的编号表达了该线与每根手指舵机的对应关系，1连接大拇指，2连接食指，3连接中指，无名指与小指共用一个电机即4 5。无标号的线中，下方的     线连接控制手腕转动的舵机，上方的线连接手掌中央使大拇指水平转动的舵机。` 该编号与程序中电机编号无关。`   
  As figure, the brown line is GND, the red line is + 5V, and the yellow line is the pwm signal. The number of the blue sticker on the line expresses the correspondence between the line and each finger steering         gear. 1 connects the thumb,     2 connects the index finger, 3 connects the middle finger, the ring finger and the little finger share one steering gear (4 5). For the line do not have number, The lower line       connects the steering gear that controls the wrist     rotation, and the upper line connects the steering gear      in the palm of the hand which make the thumb rotate horizontally. ` This number is independent of the number in the code.` 

## 程序部分 Code part
  作为测试，你可以首先打开根目录下的rpiHAT文件夹   
  As a test, you can first open the rpiHAT folder in the root directory.  
  
      cd rpiHAT
      
  然后打开test.py文件  
  Then open the test.py file.  
  
      nano test.py
      
  其中dict表示了电机与pwm伺服的对应关系  
  * 右边为pwm排针编号1-8号，左边为电机，电机2代表拇指，4代表食指，6代表中指，8代表无名指与小指，1代表大拇指水平移动，3代表手腕。  
  * 如2：4表示大拇指所   连接的线应插到4号pwm排针上，若线连接到的排针与dict里的不符，你需要改变线连接的位置或dict里对应的数字  
  
  Where dict indicates the correspondence between the motor and the pwm servo.  
  * The right side is the pwm pin number No. 1-8, the left side is the motor, the motor 2 is the thumb, the 4 is the index finger, the 6     is the middle finger, the 8 is the ring finger and the little finger, and the 1 make thumb move horizontally, 3 represents the           wrist.  
  * For example, 2:4 means that the line connected to the thumb should be inserted into the 4th pwm pin. If the pin connected to the         line does not match the dict, you need to change the position of the line or the corresponding number in the dict.  
  
 关闭test.py文件，打开你想要测试的json文件  
 Close the test.py and open the json file you want to test.
 
     nano xxx.json
     
修改其中的z的数值以控制某根手指的动作幅度
* 对于"x"2，4，1 来说，0.23为手指张开的极限，0.05为手指弯曲的极限，对于"x"6，8来说则正好相反，对于"x"3来说，转动范围为0.07-0.20  

change the value of z to control the amplitude of the action of a finger.  
* For "x" 2,4,1, 0.23 is the limit of finger opening, and 0.05 is the limit of finger close. For "x" 6,8 is the opposite, for "x"3, the range of rotation is 0.07-0.20  

关闭json文件 运行test.py,查看机械手的动作是否与数值相符  
Run test.py to see if the robot's action matches the value.  
     
     python test.py    
     
各个json文件对应其名字所指向的功能，如phone.json是让机械手做出抓住手机的动作。当然，你可以随时修改数值让它做出不一样的动作，`注意 ，请勿用test.py运行rock_paper_scissors.json程序`  
Each json file corresponds to the function just as its name, such as phone.json is to let the robot make the action of grabbing the phone. Of course, you can change the value at any time to make it perform different actions,` Attention, don't run rock_paper_scissors.json program with test.py`
  
## 关于猜拳游戏，这个游戏目前仍未被完成 This game is still not completed yet.
* 目录~/catkin_ws/src/robot_hand/src下的文件中，finger.py是在使用raspberry pi 3b+ 时使用的类程序，它仍有一些问题，而finger1.py则是之前使用raspberry pi zero及多线程时使用的类程序，请勿弄混。更多的信息详见finger.py及matlab中compare_result.m的程序注释。
* roslaunch程序在目录~/catkin_ws/src/robot_hand/launch下。
* In the file under the directory ~/catkin_ws/src/robot_hand/src, finger.py is a class python file used when using raspberry pi 3b+, it   still has some problems, and finger1.py is the file was used when we using raspberry pi zero and multi-threading. Do not confuse the     class file. More information can be found in the program comments for finger.py and compare_result.m in matlab. The roslaunch program   is in the directory ~/catkin_ws/src/robot_hand/launch.
