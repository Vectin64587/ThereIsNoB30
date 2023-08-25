import ast,sqlite3
diff_name = {0: "Pst", 1: "Prs", 2: "Ftr", 3: "Byd"}

def GetSongDiff(son_id,son_diff):
    con_song = sqlite3.connect('arcsong.db')
    cursor_song = con_song.cursor()
    selectsongline = cursor_song.execute("SELECT * FROM charts WHERE song_id = ? AND rating_class = ?", (son_id, son_diff)) #选中待计算曲目行
    line_temp = selectsongline.fetchone()   #获取该行信息
    if line_temp:
        diff_temp = line_temp[16]
        # print(diff_temp/10)
        return diff_temp/10

# with open("all_song.txt", 'r') as f:
#     content = f.read()
    #print(content)
def b30_generate(raw_data):
    # 合并多个字典为一个字典
    merged_dict = {}
    for data_dict in raw_data:
        merged_dict.update(data_dict)

    # 按ptt大小进行降序排序
    sorted_songs = sorted(merged_dict.items(), key=lambda item: item[1]['ptt'], reverse=True)

    # 构建新的字典，仅保留前30个歌曲
    result_dict = {}
    for song_name, song_info in sorted_songs[:30]:
        diff = song_info['diff']
        new_key = f"{song_name} - {diff_name[diff]}"
        # result_dict[new_key] = {
        #     'score': song_info['score'],
        #     'diff': diff,
        #     'ptt': song_info['ptt']
        # }
        result_dict[new_key] = [song_info['score'],GetSongDiff(song_name,diff),song_info['ptt']]

    return result_dict
