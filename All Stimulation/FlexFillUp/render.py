import json
from vpython import*
import time

"""用 writepos 來輸入位置，用fresh來輸出
變數:
fps:fps

Ball_renderlog_pos_add 球的位置檔案 加入型
檔案名稱:Ball-renderlog-pos.txt
Wall_renderlog_pos_add 牆的位置檔案 加入型
檔案名稱:Wall-renderlog-pos.txt

Ball_renderlog_data_add 球的資訊檔案 加入型
檔案名稱:Ball-renderlog-data.txt
Wall_renderlog_data_add 牆的資訊檔案 加入型
檔案名稱:Wall-renderlog-data.txt



Ball_renderlog_pos_read 球的位置檔案 讀取型
Wall_renderlog_pos_read 牆的位置檔案 讀取型
Ball_renderlog_data_read 球的資訊檔案 讀取型
Wall_renderlog_data_read 牆的資訊檔案 讀取型

上面是寫給我看的，下面是寫給大家看的
使用說明:
開始的時候，先用initialize()
每增加一顆球，就把球的編號/位置/半徑/顏色丟進 Ball_writedata(number,pos,radius,color) 其中pos跟color 要是vec
每增加一面牆，就把牆的編號/位置/尺寸/法向量/水平向量/透明度/顏色丟進 Wall_writedata(number,pos,size,up,axis,opacity,color)其中pos,size,up,axis,color要是vec
球計算完後，把編號跟位置丟進writepos(number,pos)(牆也一樣，不過牆沒更新的話就不要丟)
每經過一輪(一個rate)，執行refresh()
最後結束的時候，執行end()
撥動畫就用這個程式撥


"""
scene = canvas(width=1400, height=800, fov = 0.03, align = 'left', center=vec(0.3, 0, 0), background=vec(0.5,0.5,0))

renderpass = ""

fps = 24.0

Ball_renderlog_pos_add = open(renderpass+'Ball-renderlog-pos.txt','a')
Wall_renderlog_pos_add = open(renderpass+'Wall-renderlog-pos.txt','a')

Ball_renderlog_data_add = open(renderpass+'Ball-renderlog-data.txt','a')
Wall_renderlog_data_add = open(renderpass+'Wall-renderlog-data.txt','a')

Ball_posdict = {}
Wall_posdict = {}




def Ball_writedata(number,pos,radius,color):
    json.dump({number:[number,[pos.x,pos.y,pos.z],radius,[color.x,color.y,color.z]]},Ball_renderlog_data_add)
    Ball_renderlog_data_add.write("\n")

def Wall_writedata(number,pos,size,up,axis,opacity,color):
    json.dump({number:[number,[pos.x,pos.y,pos.z],[size.x,size.y,size.z],[up.x,up.y,up.z],[axis.x,axis.y,axis.z],opacity,[color.x,color.y,color.z]]},Wall_renderlog_data_add)
    Wall_renderlog_data_add.write("\n")



def initialize():
    global renderpass
    with open(renderpass+'Ball-renderlog-pos.txt','w') as Ball_renderlog_pos_write:
        Ball_renderlog_pos_write.write("")
        Ball_renderlog_pos_write.close()
    with open(renderpass+'Wall-renderlog-pos.txt','w') as Wall_renderlog_pos_write:
        Wall_renderlog_pos_write.write("")
        Wall_renderlog_pos_write.close()
    with open(renderpass+'Ball-renderlog-data.txt','w') as Ball_renderlog_data_write:
        Ball_renderlog_data_write.write("")
        Ball_renderlog_data_write.close()
    with open(renderpass+'Wall-renderlog-data.txt','w') as Wall_renderlog_data_write:
        Wall_renderlog_data_write.write("")
        Wall_renderlog_data_write.close()

    

def Ball_writepos(number,pos):
    Ball_posdict.update({number:[pos.x,pos.y,pos.z]})

def Wall_writepos(number,pos):
    Wall_posdict.update({number:[pos.x,pos.y,pos.z]})

def refresh():
    json.dump(Ball_posdict,Ball_renderlog_pos_add)
    Ball_renderlog_pos_add.write("\n")
    Ball_posdict.clear()
    if len(Wall_posdict) == 0:
        Wall_renderlog_pos_add.write('1')
        Wall_renderlog_pos_add.write('\n')
    else:
        json.dump(Wall_posdict,Wall_renderlog_pos_add)
        Wall_renderlog_pos_add.write("\n")
        Wall_posdict.clear()

    print("refresh")

def end():
    Ball_renderlog_data_add.close()
    Wall_renderlog_data_add.close()
    Ball_renderlog_pos_add.close()
    Wall_renderlog_pos_add.close()



""" 
測試用
initialize()

writepos(0,(1,1,1))

refresh()

end()"""

def animation():
    Ball_renderlog_pos_read = open(renderpass+'Ball-renderlog-pos.txt','r')
    Wall_renderlog_pos_read = open(renderpass+'Wall-renderlog-pos.txt','r')
    Ball_renderlog_data_read = open(renderpass+'Ball-renderlog-data.txt','r')
    Wall_renderlog_data_read = open(renderpass+'Wall-renderlog-data.txt','r')


    Balls = {}
    Balls_data = Ball_renderlog_data_read.readlines()
    Ball_renderlog_data_read.close()

    data = {}

    for i in Balls_data:
        data.update(json.loads(i))


    for i in data.values():
        Balls.update({str(i[0]):sphere(pos = vec(i[1][0],i[1][1],i[1][2]),radius = i[2],color = vec(i[3][0],i[3][1],i[3][2]))})

    data.clear()

    Walls = {}
    Walls_data = Wall_renderlog_data_read.readlines()
    Wall_renderlog_data_read.close()

    for i in Walls_data:
        data.update(json.loads(i))

    for i in data.values():
        Walls.update({str(i[0]):box(pos = vec(i[1][0],i[1][1],i[1][2]), size = vec(i[2][0], i[2][1], i[2][2]), up = vec(i[3][0],i[3][1],i[3][2]),axis = vec(i[4][0],i[4][1],i[4][2]),opacity = i[5],color = vec(i[6][0],i[6][1],i[6][2]))})


    Ball_output = []
    Ball_output = Ball_renderlog_pos_read.readlines()
    for i in range(len(Ball_output)):
        Ball_output[i] = json.loads(Ball_output[i])

    Wall_output = []
    Wall_output = Wall_renderlog_pos_read.readlines()
    for i in range(len(Wall_output)):
        Wall_output[i] = json.loads(Wall_output[i])

    time.sleep(1.0)
    time_start = time.time()
    for frame in range(len(Ball_output)):
        rate(fps)
        for num in Ball_output[frame].keys():
            Balls[num].pos = vec(Ball_output[frame][num][0],Ball_output[frame][num][1],Ball_output[frame][num][2])
        if Wall_output[frame] == 1:
            pass
        else:
            for num in Wall_output[frame].keys():
                Walls[num].pos = vec(Wall_output[frame][num][0],Wall_output[frame][num][1],Wall_output[frame][num][2])

    for i in Balls.values():
        i.visible = False

    for i in Walls.values():
        i.visible = False


    time_finish = time.time()

    print(time_finish - time_start)

    print("end")





