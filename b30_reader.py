import sqlite3,tkinter
from b30_generator import generate_image


#一些变量

global song_inf,ptt_list,total_ptt
difficulty = ['Past','Present','Future','Beyond']
song_inf = [{},{},{},{}]#按难度分类曲目信息
ptt_list = []
total_ptt = 0
st3file = ""
# st3file = "st3.db3"
cursor_song = None
# inputsongid = input("id:")


#获取曲目定数
def GetSongDiff(son_id,son_diff):
    selectsongline = cursor_song.execute("SELECT * FROM charts WHERE song_id = ? AND rating_class = ?", (son_id, son_diff)) #选中待计算曲目行
    line_temp = selectsongline.fetchone()   #获取该行信息
    if line_temp:
        diff_temp = line_temp[16]
        # print(diff_temp/10)
        return(diff_temp/10)


#ptt单曲计算

def pttCal(son_id,son_diff,son_score):
    diff_temp = GetSongDiff(son_id,son_diff)
    # print(diff_temp)
    #按照wiki进行计算
    if son_score >= 10000000:
        single_ptt = diff_temp + 2
    elif son_score >= 9800000 and son_score < 10000000:
        single_ptt = diff_temp + 1 + ((son_score-9800000)/20000)*0.1
    elif son_score < 9800000:
        single_ptt = diff_temp + ((son_score-9500000)/30000)*0.1
    return single_ptt

def start(st3):

    global cursor_song

    song_inf = [{},{},{},{}]#按难度分类曲目信息
    ptt_list = []
    total_ptt = 0


    #链接sqlite数据库
    con_st3 = sqlite3.connect(st3)
    con_song = sqlite3.connect('arcsong.db')

    #创建游标
    cursor_st3 = con_st3.cursor()
    cursor_song = con_song.cursor()

    select_st3line = cursor_st3.execute("SELECT * FROM scores")

    while True:
        line = select_st3line.fetchone()   #获取一行数据
        if line:
            #分别获取song_id,song_score,song_diff
            song_id = line[8]
            song_score = line[2]
            song_diff = line[9]

            #向ptt列表添加数据
            ptt_list.append(pttCal(song_id,song_diff,song_score))

            #向song_inf写入曲目信息 键分别为三维难度 曲目id 元素包含分数与三维难度 ptt
            song_inf[song_diff][song_id] = {"score":song_score,"diff":song_diff,"ptt":pttCal(song_id,song_diff,song_score)}


            # print(song_id+" "+str(song_score))  #输出曲目id及其分数
        else:
            break

    #降序排序pttList
    ptt_list.sort(reverse=True)

    #计算不探分最高ptt

    #计算不推分最高ptt
    for i in range(30):
        total_ptt += ptt_list[i]
    # print(total_ptt/30)
    return total_ptt/30

# print(pttCal("dialnote",2,9766717))

#选中score列大于10000000的行
# cursor_st3.execute("SELECT * FROM scores where score > 9900000")
# while True:
#     #获取一行数据
#     pm = cursor_st3.fetchone()
#     #输出此行第八列（song_id）
#     if pm:
#         song_id = pm[8]
#         print(song_id+" "+str(difficulty[pm[9]]))
#     else:
#         break


