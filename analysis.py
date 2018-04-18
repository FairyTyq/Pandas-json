import json
import pandas

def analysis(file_tmp,user_id):
    time = 0
    minutes = 0

    '''
    1.使用 Pandas 读取数据
    2.使用 Pandas选择数据
    '''
    file_content = pandas.read_json(file_tmp)
    data = file_content[file_content['user_id']==user_id]
    times = data[['user_id','minutes']].groupby('user_id').count()['minutes']
    minutes = data[['user_id','minutes']].groupby('user_id').sum()['minutes']
    #print('Times:%s,Minutes:%s'%(times,minutes))
    return times,minutes

#if __name__ == '__main__':
#    fp = '/home/shiyanlou/Code/user_study.json'
#    analysis(fp,2)
